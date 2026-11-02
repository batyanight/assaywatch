"""The lineage layer counts a detection the way the pooled share does, per assay.

Found 2026-10-27 by enabling the influenza sublineage chain: report.md had the matrix
assay at 6.5% and `declining` while lineage.md had every one of its subtypes between
72% and 100%, from the same calls. `drift.reduced_not_detected_for` had made a `reduced`
probe call not a detection in `drift.YearStats`, and `lineage.py` still hard-coded
`("detect", "reduced")`. Since `worst_lineage_verdict` can override a pooled status,
the override was reading a different assay from the one the verdict described.
"""

from __future__ import annotations

from assaywatch.drift import DETECTED_CALLS, DETECTED_CALLS_NO_REDUCED, AssayDrift, YearStats
from assaywatch.lineage import (
    DETECTED_DEFAULT,
    lineages_ever_covered,
    lineages_never_covered,
    per_lineage_stats,
)

CACHE = {11320: "Influenza A virus"}


def _calls(detect: int, reduced: int, fail: int, year: int = 2025) -> list[dict]:
    rows = []
    for i in range(detect):
        rows.append({"record_id": f"D{i}", "call": "detect", "taxid": 11320, "year": year})
    for i in range(reduced):
        rows.append({"record_id": f"R{i}", "call": "reduced", "taxid": 11320, "year": year})
    for i in range(fail):
        rows.append({"record_id": f"F{i}", "call": "fail", "taxid": 11320, "year": year})
    return rows


def test_the_default_is_still_detect_plus_reduced_and_matches_drift():
    assert DETECTED_DEFAULT == DETECTED_CALLS == ("detect", "reduced")
    stats = per_lineage_stats(_calls(5, 3, 2), CACHE, {}, min_records=1)
    assert stats[0].n_detected == 8 and stats[0].n_evaluable == 10


def test_a_probe_assay_counts_reduced_as_not_detected_in_the_lineage_table():
    """The numerator moves, the denominator does not: a `reduced` row is still evaluable."""
    stats = per_lineage_stats(
        _calls(5, 3, 2), CACHE, {}, min_records=1, detected_calls=DETECTED_CALLS_NO_REDUCED
    )
    assert stats[0].n_detected == 5
    assert stats[0].n_evaluable == 10, "taking reduced out of the numerator must not shrink the denominator"
    assert stats[0].share == 0.5


def test_ever_and_never_covered_use_the_same_numerator():
    """A baseline year of 20 detect + 70 reduced + 10 fail is 90% to a primer assay and
    20% to a probe assay. Under the default it cleared the threshold; under the probe
    numerator it never did -- and that is the difference between `declining` and
    `low coverage` once a failing recent window arrives."""
    base = _calls(20, 70, 10, year=2019)
    assert lineages_ever_covered(base, CACHE, {}, 0.9, 10) == {"Influenza A virus"}
    assert lineages_never_covered(base, CACHE, {}, 0.9, 10) == set()
    probe = DETECTED_CALLS_NO_REDUCED
    assert lineages_ever_covered(base, CACHE, {}, 0.9, 10, detected_calls=probe) == set()
    assert lineages_never_covered(base, CACHE, {}, 0.9, 10, detected_calls=probe) == {"Influenza A virus"}


def test_an_assay_drift_hands_its_own_detected_calls_to_the_lineage_layer():
    """The pooled numerator and the lineage numerator come from one field."""
    a = AssayDrift("PROBE", recent_from=2024, detected_calls=DETECTED_CALLS_NO_REDUCED)
    a.years[2025] = YearStats(2025, detected_calls=a.detected_calls)
    a.years[2025].counts.update({"detect": 5, "reduced": 3, "fail": 2})
    a.finalise()
    # Pooled: 5 of 10. The lineage layer, given the same field, must say the same.
    assert (a.recent_detected, a.recent_evaluable) == (5, 10)
    stats = per_lineage_stats(_calls(5, 3, 2), CACHE, {}, min_records=1, detected_calls=a.detected_calls)
    assert (stats[0].n_detected, stats[0].n_evaluable) == (a.recent_detected, a.recent_evaluable)


def test_the_per_year_block_only_covers_lineages_below_the_threshold():
    """Per year, worst first, capped -- and built on the same grouping as the share table.

    `lineage.md` could say a lineage detects 1.2% and not whether that is a fall or has
    always been so, which is the question the influenza matrix assay's 57 subtypes raised
    on 2026-10-27. The answer for H3N2 turned out to be "always": 1.1% in 2005 and 0.1%
    in 2025 (docs/journal/2026-10-28-influenza-decomposed.md).
    """
    from assaywatch.lineage_report import render_lineage_report

    # Two lineages: one healthy, one failing, both above the floor.
    calls = []
    for i in range(30):
        calls.append({"record_id": f"good{i}", "call": "detect", "taxid": 11320})
    for i in range(30):
        calls.append({"record_id": f"bad{i}", "call": "fail", "taxid": 11321})
    years = {f"good{i}": 2020 + i % 2 for i in range(30)} | {f"bad{i}": 2020 + i % 2 for i in range(30)}
    cache = {11320: "healthy_lineage", 11321: "failing_lineage"}

    md = render_lineage_report({"A": calls}, cache, {}, min_records=10, years=years, threshold=0.9)
    assert "**failing_lineage**" in md, "a lineage below the threshold needs its years shown"
    assert "**healthy_lineage**" not in md, "a healthy lineage does not need a year table"
    assert "| 2020 | 15 | 0 | 0.0% |" in md
    # Without years the block is absent entirely, so the report is unchanged for a caller
    # that does not have dates.
    assert "Per year" not in render_lineage_report({"A": calls}, cache, {}, min_records=10)
