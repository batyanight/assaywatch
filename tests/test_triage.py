"""`report.triage`: what leads the report, and the two things that may not.

Triage is lexicographic over criteria whose direction is individually obvious, so each
criterion gets a test that varies it alone. The 2026-10-27 addition is criterion 1b: a
`declining` row whose own note names the failing lineage as "a coverage gap rather
than drift" is sound, but the action it points to is a scope question, so it must not
lead a list whose audience is "a lab with no bioinformatician". Nothing here changes a
status; triage orders rows it is handed and never relabels one.
"""

from __future__ import annotations

from assaywatch.drift import AssayDrift
from assaywatch.report import StatusRow, triage


def _row(
    assay_id: str, fraction: float, note: str = "", degeneracy=None, duplication: str = "holds"
) -> StatusRow:
    return StatusRow(
        assay_id=assay_id,
        assay_name=assay_id,
        entry="active",
        pooled="",
        fraction=fraction,
        ci=(fraction - 0.05, fraction + 0.05),
        evaluable=500,
        baseline=(0.95, 1000),
        degeneracy=degeneracy,
        duplication=duplication,
        note=note,
        drift=AssayDrift(assay_id),
    )


GAP = "lineage X (123) (40 records) detects only 0.0% and was below the threshold in every earlier year, so that lineage is a coverage gap rather than drift"


def test_a_declining_row_that_names_a_coverage_gap_follows_the_others_and_precedes_low_coverage():
    rows_by_status = [
        ("declining", [_row("GAP_FIRST_ALPHABETICALLY", 0.30, note=GAP), _row("REAL_DRIFT", 0.60)]),
        ("low coverage", [_row("NEVER_COVERED", 0.10)]),
    ]
    tr = triage(rows_by_status, assays={}, limit=10)
    assert [r.assay_id for r in tr.rows] == ["REAL_DRIFT", "GAP_FIRST_ALPHABETICALLY", "NEVER_COVERED"]
    # Nothing was relabelled: the input rows are the output rows.
    assert {r.assay_id for r in tr.rows} == {"GAP_FIRST_ALPHABETICALLY", "REAL_DRIFT", "NEVER_COVERED"}
    assert tr.total_flagged == 3 and tr.held_degenerate == 0 and tr.held_unconfirmed == 0


def test_within_the_same_class_the_lower_share_still_leads():
    rows_by_status = [("declining", [_row("MILD", 0.80, note=GAP), _row("SEVERE", 0.20, note=GAP)])]
    tr = triage(rows_by_status, assays={}, limit=10)
    assert [r.assay_id for r in tr.rows] == ["SEVERE", "MILD"]


def test_the_two_exclusions_still_hold_rows_back_without_dropping_them():
    rows_by_status = [
        (
            "declining",
            [
                _row("DEGENERATE", 0.10, degeneracy=(4096, "severe")),
                _row("UNCONFIRMED", 0.10, duplication="fails: recent"),
                _row("CLEAN", 0.50),
            ],
        )
    ]
    tr = triage(rows_by_status, assays={}, limit=10)
    assert [r.assay_id for r in tr.rows] == ["CLEAN"]
    assert tr.total_flagged == 3 and tr.held_degenerate == 1 and tr.held_unconfirmed == 1
