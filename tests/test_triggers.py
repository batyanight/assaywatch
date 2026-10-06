"""The Snakefile's rerun triggers: which files each rule depends on, and that editing them reruns it.

The failure these guard against is silent. A rule that does not notice an edit to
the code it runs leaves yesterday's results in place and the next report looks
fine. It happened twice already (schema.py and validate.py missing from the
screening list; collect_calls losing its trigger when its logic moved into a
module), so the list of files is now derived from the imports rather than kept by
hand, and the wiring is checked here.

Three layers, because each catches something the others cannot:

- `assaywatch.triggers` on a synthetic package: the import walk itself;
- the real package and the Snakefile text: the facts that were once wrong, and that
  every rule that runs a module hashes it;
- real Snakemake, where it is installed: that an edit actually lists the rule for
  rerun. Skipped without it (CI installs only the package), but it is the only
  layer that tests Snakemake's behaviour rather than our reading of it.
"""

from __future__ import annotations

import gzip
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from assaywatch.triggers import direct_imports, import_closure, source_names

ROOT = Path(__file__).resolve().parents[1]
SNAKEFILE = (ROOT / "Snakefile").read_text()


# --------------------------------------------------------------------------
# The import walk
# --------------------------------------------------------------------------


@pytest.fixture
def package(tmp_path):
    """a -> b -> c -> d, with every import style, plus an unreachable f and a cycle."""
    files = {
        # top-level `from`, parenthesised multi-line names
        "a": "from assaywatch.b import (\n    x,\n    y,\n)\n",
        # an import made inside a function, as report.py does with load_config
        "b": "def main():\n    from assaywatch.c import load\n    import assaywatch.g\n",
        # `from assaywatch import d, e`: d is a module, e is only a name
        "c": "from assaywatch import d, e\n",
        # a cycle back to a
        "d": "from assaywatch.a import z\n",
        "e": "",  # a module, so `from assaywatch import d, e` reaches it
        "f": "from assaywatch.a import z\n",  # imports into the graph, but nothing imports f
        "g": "",
        # third-party and standard-library imports are not ours
        "h": "import csv\nfrom pathlib import Path\nimport yaml\nfrom assaywatch.g import q\n",
        "i": "# from assaywatch.g import mentioned_in_a_comment\nx = 'from assaywatch.g import in_a_string'\n",
    }
    for name, body in files.items():
        (tmp_path / f"{name}.py").write_text(body)
    return tmp_path


def test_the_walk_follows_every_import_style_and_stops_at_cycles(package):
    assert import_closure("a", package) == {"a", "b", "c", "d", "e", "g"}
    assert source_names("a", package) == ["a.py", "b.py", "c.py", "d.py", "e.py", "g.py"]


def test_only_modules_that_exist_in_the_package_count(package):
    assert direct_imports("h", package) == {"g"}  # csv, pathlib and yaml are not assaywatch's
    (package / "g.py").unlink()
    assert direct_imports("h", package) == set()


def test_a_name_imported_from_the_package_that_is_not_a_module_is_ignored(package):
    (package / "e.py").unlink()
    assert "e" not in import_closure("c", package)


def test_a_comment_or_string_mentioning_an_import_is_not_one(package):
    assert direct_imports("i", package) == set()


def test_a_module_not_reachable_from_the_start_is_not_included(package):
    assert "f" not in import_closure("a", package)
    assert import_closure("f", package) >= {"f", "a", "b", "c", "d", "e", "g"}


def test_walk_reads_nested_imports_in_the_real_package():
    """report.py imports score.py only inside main(), which is the case that
    motivates following indented imports."""
    assert "score" in direct_imports("report")
    assert "score.py" in source_names("report")


# --------------------------------------------------------------------------
# The facts that were wrong, and the wiring
# --------------------------------------------------------------------------


def test_screening_depends_on_the_two_files_the_hand_kept_list_missed():
    names = source_names("screen")
    assert "schema.py" in names and "validate.py" in names
    assert "screen.py" in names and "score.py" in names


def test_the_report_depends_on_the_drift_code():
    assert {"report.py", "drift.py", "degeneracy.py", "schema.py"} <= set(source_names("report"))


def test_collect_depends_on_its_own_module():
    assert source_names("collect") == ["collect.py"]


def rule_blocks(text: str) -> dict[str, str]:
    """{rule name: its text} for every rule and checkpoint in a Snakefile."""
    parts = re.split(r"^(?:rule|checkpoint)[ \t]+(\w+):", text, flags=re.M)
    return {parts[i]: parts[i + 1] for i in range(1, len(parts), 2)}


def test_the_screening_code_list_is_derived_not_hand_kept():
    assert re.search(r'^_CODE = source_names\("screen"\)$', SNAKEFILE, re.M)


@pytest.mark.parametrize(
    "rule, module, uses",
    [
        ("collect_calls", "collect", "_COLLECT_CODE"),
        ("report", "report", '_REPORT_PARAMS["code"]'),
        ("degeneracy_table", "degeneracy", '_DEGENERACY_PARAMS["code"]'),
    ],
)
def test_every_downstream_rule_carries_a_hash_of_its_code_as_a_param(rule, module, uses):
    """These rules run a module, so Snakemake sees none of their code. `params`
    is the only thing that reruns them when the module is edited."""
    block = rule_blocks(SNAKEFILE)[rule]
    assert "params:" in block and uses in block, f"{rule} does not hash {module}"
    assert f'source_names("{module}")' in SNAKEFILE


def test_every_rule_that_runs_an_assaywatch_module_is_accounted_for():
    """A new rule that calls `python -m assaywatch.x` must either hash x or say,
    here, why not. retrieve is exempt on purpose: its params are the groups asked
    for, because refetching on a code edit would hit NCBI for nothing; validate is
    exempt because it only gates the run."""
    exempt = {
        "retrieve": "refetching on a code edit costs NCBI calls",
        "validate": "gates the run; no output",
    }
    hashed = {"screen_archive": "screen", "report": "report", "degeneracy_table": "degeneracy"}
    for rule, block in rule_blocks(SNAKEFILE).items():
        for module in re.findall(r"python -m assaywatch\.(\w+)", block):
            assert rule in exempt or hashed.get(rule) == module, (
                f"rule {rule!r} runs assaywatch.{module} but nothing hashes it: add a params hash "
                "(see _package_hash in the Snakefile) or exempt it here with a reason"
            )


# --------------------------------------------------------------------------
# Real Snakemake
# --------------------------------------------------------------------------


def _snakemake(tree: Path, *args: str) -> subprocess.CompletedProcess:
    """Run Snakemake in `tree` with that copy of the package first on the path.

    The rules shell out to `python -m assaywatch...`, so `python` has to be this
    interpreter, and `assaywatch` has to be the tree's copy, not the checkout's.
    """
    today = date.today().isoformat()
    env = {
        **os.environ,
        "PYTHONPATH": str(tree),
        "PATH": f"{Path(sys.executable).parent}{os.pathsep}{os.environ.get('PATH', '')}",
    }
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "snakemake",
            "--cores",
            "2",
            "--config",
            "email=t@example.org",
            f"run_date={today}",
            *args,
        ],
        cwd=tree,
        capture_output=True,
        text=True,
        env=env,
    )


def _planned(result: subprocess.CompletedProcess) -> set[str]:
    """Rules listed to run in a dry-run, minus the `all` target."""
    return set(re.findall(r"^(?:local)?(?:rule|checkpoint) (\w+):", result.stdout, flags=re.M)) - {"all"}


@pytest.fixture(scope="module")
def tree(tmp_path_factory):
    """A copy of the pipeline with one real archive planted and a full run done, offline.

    The retrieval checkpoint is satisfied by a planted run record (its output) written
    after `.registry-valid`, exactly what a day's earlier run leaves behind.
    """
    pytest.importorskip("snakemake")
    t = tmp_path_factory.mktemp("pipeline")
    for name in ("Snakefile", "config.yaml"):
        shutil.copy(ROOT / name, t / name)
    shutil.copytree(ROOT / "assaywatch", t / "assaywatch", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(ROOT / "registry", t / "registry")

    from assaywatch.retrieve import targets_from_registry

    groups = targets_from_registry([t / "registry"], {})
    taxid, group = next(k for k in sorted(groups) if k[1] == "all")
    archive = t / "data" / "retrieved" / str(taxid) / group
    archive.mkdir(parents=True)
    fixtures = (ROOT / "tests" / "fixtures" / "records.fasta").read_bytes()
    with gzip.open(archive / "2026-10-04.fasta.gz", "wb") as fh:
        fh.write(fixtures)

    today = date.today().isoformat()
    (t / "results" / today).mkdir(parents=True)
    (t / "results" / today / ".registry-valid").touch()
    (t / "data" / "retrieved" / "runs").mkdir(parents=True)
    (t / "data" / "retrieved" / "runs" / f"{today}.json").write_text("{}")

    first = _snakemake(t)
    assert first.returncode == 0, first.stdout[-2000:] + first.stderr[-2000:]
    again = _snakemake(t, "-n")
    assert again.returncode == 0 and not _planned(again), "a finished tree should have nothing to do"
    return t


def _edited(tree: Path, relative: str, new_text):
    """Apply `new_text(old)` to a file and return a function that puts it back."""
    path = tree / relative
    old = path.read_text()
    new = new_text(old)
    assert new != old, f"the edit to {relative} changed nothing, so the test below would prove nothing"
    path.write_text(new)
    return lambda: path.write_text(old)


@pytest.mark.parametrize(
    "relative, edit, expected",
    [
        # logic moved out of a run: block must still rerun it, and what follows it
        ("assaywatch/collect.py", lambda s: s + "\n# edited\n", {"collect_calls", "report"}),
        ("assaywatch/drift.py", lambda s: s + "\n# edited\n", {"report"}),
        ("assaywatch/report.py", lambda s: s + "\n# edited\n", {"report"}),
        # schema.py and validate.py once rescreened nothing
        (
            "assaywatch/schema.py",
            lambda s: s + "\n# edited\n",
            {"screen_archive", "degeneracy_table", "collect_calls", "report"},
        ),
        (
            "assaywatch/validate.py",
            lambda s: s + "\n# edited\n",
            {"screen_archive", "degeneracy_table", "collect_calls", "report"},
        ),
        # a module no rule runs or imports reruns nothing
        ("assaywatch/credentials.py", lambda s: s + "\n# edited\n", set()),
        # a drift setting reaches the report and nothing upstream of it
        (
            "config.yaml",
            lambda s: s.replace("min_records_for_coverage: 10", "min_records_for_coverage: 11"),
            {"report"},
        ),
    ],
    ids=[
        "collect.py",
        "drift.py",
        "report.py",
        "schema.py",
        "validate.py",
        "unrelated module",
        "drift config",
    ],
)
def test_an_edit_reruns_exactly_the_rules_that_depend_on_it(tree, relative, edit, expected):
    restore = _edited(tree, relative, edit)
    try:
        assert _planned(_snakemake(tree, "-n")) == expected
    finally:
        restore()
    assert not _planned(_snakemake(tree, "-n")), "restoring the file should leave nothing to do"


def test_editing_an_assay_nothing_screens_still_refreshes_the_degeneracy_table_and_report(tree):
    """degeneracy.tsv and the report read every assay, and neither names the
    registry as an input. Before they hashed it, only an added or removed file
    (which changes the directory's mtime) reran them."""
    from assaywatch.retrieve import targets_from_registry

    groups = targets_from_registry([tree / "registry"], {})
    planted = next((tree / "data" / "retrieved").glob("[0-9]*"))  # the one group with an archive
    screened = groups[(int(planted.name), next(planted.iterdir()).name)]["assays"]
    outside = next(p for p in sorted((tree / "registry").glob("*.yaml")) if p.stem not in screened)
    restore = _edited(tree, f"registry/{outside.name}", lambda s: s + "\n# edited\n")
    try:
        assert _planned(_snakemake(tree, "-n")) == {"degeneracy_table", "report"}
    finally:
        restore()
