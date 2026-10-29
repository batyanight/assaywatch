"""Every key in config.yaml is read by something.

`lineage.taxid_backfill` was declared and read nowhere for three days, while the
path it names was hardcoded in `report.py` and `lineage_report.py` - so the
setting looked configurable, was not, and the audit had to find it by hand. It
was the only dead key of 73. This is the cheap check that keeps it that way:
config.yaml is where this project puts decisions, and a key nothing reads is
either a decision with no effect or a consumer with a hardcoded answer.

The match is deliberately crude - the key's name as a quoted literal anywhere in
the package, the scripts or the Snakefile. That cannot tell `cfg["lineage"]` from
the word "lineage" in a dict unrelated to config, so it under-reports. It is a
floor, not a proof, and it is enough to catch a key that nothing mentions at all.
"""

from __future__ import annotations

import json
import re
from collections.abc import Iterator
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


# Dicts whose immediate keys are data - mispair labels, chemistry names, assay
# or taxid ids - not nested config settings. Their liveness is the parent key's
# (mispair_penalty IS read by score.py); their contents are validated by
# dedicated code (score.check_chemistry_overrides, the mispair lookup), not by
# name here. Recursing in would treat a data value like "T:G" as a setting read
# nowhere, which it is not. They passed silently until mispair_penalty shipped a
# non-empty table on 2026-10-21 - the first populated one.
DATA_TABLES = {"mispair_penalty", "by_chemistry", "sublineage"}


def key_paths(node: dict, path: tuple[str, ...] = ()) -> Iterator[tuple[str, ...]]:
    """Every key in the tree, as a dotted path."""
    for k, v in node.items():
        yield (*path, k)
        if isinstance(v, dict) and k not in DATA_TABLES:
            yield from key_paths(v, (*path, k))


def sources() -> str:
    files = [*sorted((ROOT / "assaywatch").glob("*.py")), *sorted((ROOT / "scripts").glob("*.py"))]
    return "\n".join(p.read_text() for p in [*files, ROOT / "Snakefile"])


def mentioned(key: str, src: str) -> bool:
    return f'"{key}"' in src or f"'{key}'" in src


def test_no_config_key_is_read_by_nothing():
    cfg = yaml.safe_load((ROOT / "config.yaml").read_text())
    src = sources()
    dead = [".".join(p) for p in key_paths(cfg) if not mentioned(p[-1], src)]
    assert not dead, "declared in config.yaml and read nowhere:\n  " + "\n  ".join(dead)


def test_the_check_can_see_a_key_nothing_reads():
    """Without this, a bug in `mentioned` would make the test above vacuous."""
    assert not mentioned("taxid_backfill", 'sidecar = retrieved / ".meta.taxid.backfill.tsv.gz"')
    assert mentioned("taxid_backfill", 'lineage_cfg.get("taxid_backfill")')


def test_the_config_has_the_keys_this_check_is_worth_running_on():
    cfg = yaml.safe_load((ROOT / "config.yaml").read_text())
    assert len(list(key_paths(cfg))) > 50  # 73 on 2026-10-21; a near-empty config would pass vacuously


def test_a_cache_file_has_one_format_and_one_writer():
    """Two shapes in one path cost 247 cached taxon records once already.

    `docs/taxa-cache.json` is the lineage analysis's taxid -> name mapping, read
    by `lineage.load_taxa_cache` out of a `taxa` sub-object and named in
    config.yaml. `scripts/assay_sheet.py` keyed a full NCBI record by taxid
    string in the same file, so whichever ran last won: commit 780df17 wrote the
    lineage stub over 247 records, and the next assay_sheet run would have
    written them back over the stub. They are separate files from 2026-10-21.

    The check is on the shapes rather than the paths, because renaming either
    default back would reintroduce the collision without touching this string.
    """
    lineage_path = yaml.safe_load((ROOT / "config.yaml").read_text())["lineage"]["taxa_cache"]
    lineage_cache = json.loads((ROOT / lineage_path).read_text())
    assert set(lineage_cache) == {"description", "taxa"}, (
        f"{lineage_path} holds something other than the lineage mapping; "
        "another writer has claimed it (see scripts/assay_sheet.py --taxa-cache)"
    )
    assert all(k.isdigit() for k in lineage_cache["taxa"])

    # The path assay_sheet.py writes, read off its argparse default rather than
    # searched for: that file names docs/taxa-cache.json in a comment saying not
    # to use it, and a substring search would read the warning as the bug.
    src = (ROOT / "scripts" / "assay_sheet.py").read_text()
    default = re.search(r'add_argument\(\s*"--taxa-cache".*?default=([^)]*\))', src, re.S)
    assert default, "could not find assay_sheet.py's --taxa-cache default"
    assert "taxa-cache.json" not in default.group(1), (
        f"assay_sheet.py defaults to {lineage_path}, which the lineage analysis owns"
    )


def test_the_docs_index_covers_every_doc_and_has_no_broken_links():
    """54 of 55 docs/ files were reachable from no top-level document, so two of
    the best -- pipeline-architecture.md, with a DAG of the whole pipeline, and
    installation.md -- were invisible and a reader concluded there was no
    architecture documentation. An index only helps while it is complete."""
    import re
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    index = (docs / "INDEX.md").read_text()
    linked = set(re.findall(r"\]\(([^)]+)\)", index)) | set(
        re.findall(r"`([0-9A-Za-z._-]+\.(?:md|tsv))`", index)
    )
    present = {p.name for p in docs.glob("*.md")} | {p.name for p in docs.glob("*.tsv")}

    missing = sorted(present - linked - {"INDEX.md"})
    assert not missing, f"docs/ files absent from docs/INDEX.md: {missing}"

    broken = sorted(link for link in linked if link.endswith((".md", ".tsv")) and not (docs / link).exists())
    assert not broken, f"docs/INDEX.md links to files that do not exist: {broken}"

    # and the index is reachable itself, which is the whole point
    assert "docs/INDEX.md" in (root / "README.md").read_text()
