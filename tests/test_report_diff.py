"""scripts/report_diff.py: the two ways a run-to-run diff reads a report wrong.

Both bugs were silent - the script printed a confident summary either way.
A heading the script does not recognise used to become a status, so
"## Nested protocols" turned into a bucket of 20 assays that the report itself
never put there, and neither run's buckets summed to its own assay count. And
with no id resolution, the 27 renames and 13 removals of October 2026 printed
as 56 assays gone and 33 arrived, burying the 23 real status changes.
"""

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("report_diff", ROOT / "scripts" / "report_diff.py")
report_diff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report_diff)

HEADER = "| assay | entry | detected (recent) |\n|---|---|---|\n"


def _report(run: Path, sections: dict[str, list[str]]) -> Path:
    """A run directory holding a report.md with the sections given, in order."""
    run.mkdir(parents=True, exist_ok=True)
    out = [f"# AssayWatch report - {run.name}", ""]
    for heading, rows in sections.items():
        out += [f"## {heading} ({len(rows)})", "", HEADER + "\n".join(rows), ""]
    (run / "report.md").write_text("\n".join(out) + "\n")
    return run


def _renames(path: Path, rows: list[tuple[str, str, str, str]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = ["old_id\taction\tnew_id\treason"] + ["\t".join(r) for r in rows]
    path.write_text("\n".join(body) + "\n")
    return path


def test_a_heading_that_is_not_a_status_is_not_read_as_one(tmp_path):
    """The statuses are a closed set from assaywatch/drift.py; sections are not.

    `A` sits in both Declining and Nested protocols, which is normal - the
    nested section lists a protocol by its round-1 id. Only the status section
    may speak for its status.
    """
    run = _report(
        tmp_path / "2026-10-20",
        {
            "Declining": ["| `A` | draft | 11.7% |"],
            "Stable": ["| `B` | draft | 99.0% |"],
            "Nested protocols": ["| `A` | 32% | 100% |"],
            "Coverage gaps": ["| `C` | Apicomplexa | 5794 |"],
        },
    )
    s = report_diff.statuses(run / "report.md")
    assert s == {"A": "declining", "B": "stable"}
    assert "nested protocols" not in report_diff.counts(s)
    assert "C" not in s  # a coverage-gap assay was never screened, so it has no status


def test_a_pooled_tag_does_not_hide_the_row(tmp_path):
    """A lineage override prints "(pooled: low coverage)" beside the id.

    21 of the 208 rows in the 2026-10-20 report carry that tag. Missing them
    parsed 187 ids and lost exactly the 17 declining and 4 low coverage assays
    the lineage rules had just moved - the opposite of the point of the diff.
    """
    run = _report(
        tmp_path / "2026-10-20",
        {"Declining": ["| `A` (pooled: low coverage) | draft | 11.7% |", "| `B` | draft | 20.9% |"]},
    )
    assert report_diff.statuses(run / "report.md") == {"A": "declining", "B": "declining"}


def test_the_counts_account_for_every_assay_in_the_report(tmp_path):
    """The symptom of both heading bugs: buckets that do not sum to the rows."""
    run = _report(
        tmp_path / "2026-10-20",
        {
            "Declining": ["| `A` (pooled: stable) | draft | 11.7% |"],
            "Low Coverage": ["| `B` | draft | 0.0% |"],
            "Nested protocols": ["| `A` | 32% | 100% |", "| `B` | 18% | 45% |"],
        },
    )
    assert report_diff.counts(report_diff.statuses(run / "report.md")) == "1 declining, 1 low coverage"


def test_a_renamed_assay_is_tracked_as_one_assay(tmp_path, capsys):
    """RENAME is followed, so a rename is a status change and not a pair of lists."""
    old = _report(tmp_path / "2026-10-17", {"Low Coverage": ["| `OLD_id` | draft | 85% |"]})
    new = _report(tmp_path / "2026-10-20", {"Declining": ["| `NEW_id` | draft | 11% |"]})
    renames = _renames(
        tmp_path / "docs" / "rename-mapping.tsv", [("OLD_id", "RENAME", "NEW_id", "DOI added")]
    )

    assert report_diff.main([str(old), str(new), "--renames", str(renames)]) == 0
    out = capsys.readouterr().out
    assert "low coverage -> declining: NEW_id (was `OLD_id`)" in out
    assert "no longer in the report" not in out
    assert "new in the report" not in out


def test_a_removed_assay_is_reported_as_removed_not_as_disappeared(tmp_path, capsys):
    """12 of the 13 REMOVEs are in the 2026-10-17 report; they left on purpose."""
    old = _report(
        tmp_path / "2026-10-17", {"Stable": ["| `DROP_me` | draft | 99% |", "| `KEEP_me` | draft | 99% |"]}
    )
    new = _report(tmp_path / "2026-10-20", {"Stable": ["| `KEEP_me` | draft | 99% |"]})
    renames = _renames(
        tmp_path / "docs" / "rename-mapping.tsv", [("DROP_me", "REMOVE", "", "doi: null, unpublished")]
    )

    assert report_diff.main([str(old), str(new), "--renames", str(renames)]) == 0
    out = capsys.readouterr().out
    assert "1 removed from the registry: DROP_me" in out
    assert "no longer in the report" not in out


def test_a_report_holding_both_ids_keeps_them_apart_and_says_so(tmp_path, capsys):
    """The 2026-10-20 run screened a calls table older than the rename, so three
    assays were scored twice, under both names. Folding the old row onto the new
    one would pick one of two statuses at random, so the script reports it."""
    old = _report(tmp_path / "2026-10-17", {"Stable": ["| `OLD_id` | draft | 99% |"]})
    new = _report(
        tmp_path / "2026-10-20",
        {"No Recent Data": ["| `OLD_id` | draft | - |"], "Declining": ["| `NEW_id` | draft | 11% |"]},
    )
    renames = _renames(
        tmp_path / "docs" / "rename-mapping.tsv", [("OLD_id", "RENAME", "NEW_id", "DOI added")]
    )

    assert report_diff.main([str(old), str(new), "--renames", str(renames)]) == 0
    out = capsys.readouterr().out
    assert "scored twice in 2026-10-20, under both the old and new id: OLD_id" in out
    assert report_diff.counts(report_diff.statuses(new / "report.md")) in out  # both rows still counted


def test_a_missing_mapping_is_not_an_error(tmp_path, capsys):
    """The diff must still run on a machine without docs/, as the loader in
    scripts/lineage_override_audit.py also allows."""
    old = _report(tmp_path / "2026-10-17", {"Stable": ["| `A` | draft | 99% |"]})
    new = _report(tmp_path / "2026-10-20", {"Watch": ["| `A` | draft | 89% |"]})
    assert report_diff.main([str(old), str(new), "--renames", str(tmp_path / "nope.tsv")]) == 0
    assert "stable -> watch: A" in capsys.readouterr().out


def test_the_real_mapping_resolves_in_one_step():
    """`resolve` follows a rename once. Two renames of the same assay, or a
    RENAME onto an id that is itself renamed, would need a chain walk - the
    mapping has neither, and this fails when one appears.
    """
    renamed, removed = report_diff.rename_map(ROOT / "docs" / "rename-mapping.tsv")
    assert renamed and removed
    assert not (set(renamed.values()) & (set(renamed) | removed)), "a rename target is itself renamed"
    assert len(set(renamed.values())) == len(renamed), "two old ids resolve to one new id"


def test_only_plain_dated_run_directories_are_picked_automatically(tmp_path: Path):
    """The third guard against a bug that has now appeared twice.

    `results/` holds experiment directories beside the dated runs -- `baseline-2026-10-22`,
    `2026-10-24-anchorfdr`, `indel_check`, `2026-10-28.partial-stopped` -- and a
    lexicographic sort puts letters AFTER digits. Taking the last two of everything picked
    `2026-10-31` as the OLD run and `baseline-2026-10-22` as the NEW one, so the release
    run's own summary diffed two directories it had nothing to do with and reported four
    newly added assays as having vanished. It invented a regression.

    `backfill_collection_dates.newest_run()` had the identical bug and was fixed in place
    without anyone looking for siblings. This asserts the rule that makes both safe: a
    candidate must be named exactly YYYY-MM-DD.
    """
    import importlib.util

    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location("report_diff", root / "scripts" / "report_diff.py")
    assert spec and spec.loader
    rd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rd)

    results = tmp_path / "results"
    for name in (
        "2026-10-27",
        "2026-10-31",
        "baseline-2026-10-22",
        "2026-10-24-anchorfdr",
        "indel_check",
        "2026-10-28.partial-stopped",
    ):
        d = results / name
        d.mkdir(parents=True)
        (d / "report.md").write_text("# report\n")
    # a dated directory with no report is not a candidate either
    (results / "2026-11-01").mkdir()

    picked = rd._dated_runs(results)
    assert [p.name for p in picked] == ["2026-10-27", "2026-10-31"]
    assert picked[-2].name == "2026-10-27" and picked[-1].name == "2026-10-31"
