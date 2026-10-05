"""Drift statistics. Interval values are checked against published figures.

The Wilson and Newcombe numbers below are standard worked examples; if a
refactor changes them, the refactor is wrong, not the test.
"""

from datetime import date

import pytest

from assaywatch.drift import (
    AssayDrift,
    YearStats,
    assess,
    coverage_gaps,
    newcombe_difference,
    recent_cutoff_year,
    wilson_interval,
)

CFG = {
    "drift": {
        "detect_fraction_threshold": 0.90,
        "recent_window_months": 24,
        "min_records_for_drift": 20,
        "min_records_for_coverage": 10,
    }
}
TODAY = date(2026, 10, 3)


@pytest.mark.parametrize(
    "k,n,lo,hi",
    [
        (0, 10, 0.0000, 0.2775),
        (10, 10, 0.7225, 1.0000),
        (3, 5, 0.2307, 0.8824),
        (45, 50, 0.7864, 0.9565),
    ],
)
def test_wilson_matches_published_values(k, n, lo, hi):
    got = wilson_interval(k, n)
    assert got[0] == pytest.approx(lo, abs=5e-4)
    assert got[1] == pytest.approx(hi, abs=5e-4)


def test_wilson_never_leaves_the_unit_interval_at_the_extremes():
    """The normal approximation can return bounds below 0 or above 1; this must not."""
    for k, n in [(0, 3), (3, 3), (1, 200), (199, 200)]:
        lo, hi = wilson_interval(k, n)
        assert 0.0 <= lo <= hi <= 1.0


def test_wilson_has_width_even_when_every_record_agrees():
    """k == n is not certainty. The normal approximation claims it is."""
    lo, hi = wilson_interval(8, 8)
    assert lo < 1.0 and hi == 1.0 and lo < 0.7


def test_empty_sample_is_maximally_uncertain():
    assert wilson_interval(0, 0) == (0.0, 1.0)
    assert newcombe_difference(0, 0, 5, 10) == (-1.0, 1.0)


def test_newcombe_difference_brackets_the_point_estimate():
    lo, hi = newcombe_difference(45, 50, 98, 100)
    assert lo < (45 / 50 - 98 / 100) < hi
    assert hi < 0  # a real drop: the interval excludes zero


def records(year_counts):
    """{year: {call: n}} -> flat call rows plus the year lookup."""
    calls, years = [], {}
    i = 0
    for year, counts in year_counts.items():
        for call, n in counts.items():
            for _ in range(n):
                rid = f"AB{i:05d}"
                calls.append({"assay_id": "A", "record_id": rid, "call": call})
                years[rid] = year
                i += 1
    return calls, years


def test_recent_window_is_derived_from_months():
    assert recent_cutoff_year(CFG, TODAY) == 2024


def test_stable_assay_is_not_flagged():
    calls, years = records({2024: {"detect": 40}, 2025: {"detect": 38, "reduced": 2}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "stable" and a.recent_fraction == 1.0


def test_reduced_counts_as_detected():
    """`reduced` amplifies, just later. It is a sensitivity note, not a miss."""
    calls, years = records({2025: {"reduced": 30}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_detected == 30 and a.status == "stable"


def test_clear_drift_is_flagged():
    calls, years = records({2020: {"detect": 100}, 2025: {"detect": 20, "fail": 30}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "declining"
    assert a.recent_ci[1] < 0.90
    assert a.change_ci[1] < 0  # the drop excludes zero


def test_low_but_unchanged_share_is_low_coverage_not_drift():
    """An assay that never covered this pool: same low share before and after."""
    calls, years = records({2015: {"detect": 30, "fail": 70}, 2025: {"detect": 30, "fail": 70}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "low coverage" and a.change_ci[0] < 0 < a.change_ci[1]
    assert "no measurable fall" in a.note


def test_below_threshold_with_no_baseline_is_low_coverage():
    calls, years = records({2025: {"detect": 10, "fail": 40}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "low coverage" and "no baseline" in a.note


def test_small_sample_is_never_flagged_however_bad_it_looks():
    """Three failures out of five is 40 percent and means nothing at n = 5."""
    calls, years = records({2025: {"detect": 2, "fail": 3}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "insufficient data"
    assert "too wide to act on" in a.note


def test_borderline_assay_is_watched_not_flagged():
    """Below threshold on the point estimate, but the interval still covers it."""
    calls, years = records({2025: {"detect": 22, "fail": 3}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_fraction < 0.90 < a.recent_ci[1]
    assert a.status == "watch"


def test_no_amplicon_and_indeterminate_stay_out_of_the_denominator():
    """A bad sequencing year must not look like drift."""
    calls, years = records({2025: {"detect": 25, "no_amplicon": 500, "indeterminate": 80}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_evaluable == 25 and a.recent_fraction == 1.0
    assert a.status == "stable"
    assert a.unevaluable() == {"no_amplicon": 500, "indeterminate": 80}


def test_records_without_a_deposit_year_are_skipped_and_reported():
    calls, years = records({2025: {"detect": 25}})
    calls.append({"assay_id": "A", "record_id": "NOYEAR", "call": "fail"})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.recent_evaluable == 25
    assert "1 records skipped" in a.note


def test_old_data_only_is_not_called_stable():
    calls, years = records({2015: {"detect": 200}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.status == "no recent data"


def test_baseline_and_recent_split_on_the_cutoff_year():
    calls, years = records({2023: {"detect": 50}, 2024: {"detect": 30, "fail": 10}})
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.baseline_evaluable == 50 and a.recent_evaluable == 40


def test_coverage_gap_lists_assays_with_too_little_data():
    calls, years = records({2025: {"detect": 4}})
    drifts = assess(calls, years, CFG, today=TODAY)
    taxa = {"A": (109871, "Batrachochytrium dendrobatidis"), "B": (1, "Never screened")}
    gaps = {g["assay_id"]: g for g in coverage_gaps(drifts, taxa, CFG)}
    assert gaps["A"]["evaluable"] == 4
    assert gaps["B"]["evaluable"] == 0  # an assay with no records at all is the worst gap


def test_thresholds_come_from_config():
    calls, years = records({2025: {"detect": 22, "fail": 3}})
    strict = {"drift": {**CFG["drift"], "detect_fraction_threshold": 0.99}}
    assert assess(calls, years, strict, today=TODAY)["A"].status == "low coverage"  # no baseline
    loose = {"drift": {**CFG["drift"], "min_records_for_drift": 1000}}
    assert assess(calls, years, loose, today=TODAY)["A"].status == "insufficient data"


def test_year_stats_can_be_assembled_directly():
    a = AssayDrift("A", recent_from=2024)
    a.years[2025] = YearStats(2025)
    a.years[2025].counts["detect"] = 30
    a.finalise()
    assert a.recent_evaluable == 30 and a.status == "stable"


def test_a_real_but_tiny_fall_is_not_declining():
    """1% -> 0% over thousands of records excludes zero, and still says nothing about drift."""
    cfg = {"drift": {**CFG["drift"], "min_decline": 0.05}}
    calls, years = records({2015: {"detect": 30, "fail": 2970}, 2025: {"fail": 3000}})
    a = assess(calls, years, cfg, today=TODAY)["A"]
    assert a.change_ci[1] < 0 and a.status == "low coverage"
    assert "fell less than" in a.note
    big = {"drift": {**CFG["drift"], "min_decline": 0.05}}
    calls, years = records({2015: {"detect": 90, "fail": 10}, 2025: {"detect": 40, "fail": 60}})
    assert assess(calls, years, big, today=TODAY)["A"].status == "declining"


def test_window_widens_for_a_sparsely_deposited_target():
    """Bd ITS records arrive in bursts; a fixed window makes the assay unjudgeable between them."""
    cfg = {"drift": {**CFG["drift"], "max_window_months": 60}}
    # 8 records inside 24 months, 30 more in the two years before that.
    calls, years = records({2022: {"detect": 30}, 2025: {"detect": 8}})
    fixed = assess(calls, years, CFG, today=TODAY)["A"]
    assert fixed.status == "insufficient data" and fixed.window_months == 24
    wide = assess(calls, years, cfg, today=TODAY)["A"]
    assert wide.status == "stable" and wide.window_months > 24
    assert wide.recent_evaluable == 38 and "widened" in wide.note


def test_a_dense_target_keeps_the_standard_window():
    cfg = {"drift": {**CFG["drift"], "max_window_months": 60}}
    calls, years = records({2022: {"detect": 500}, 2025: {"detect": 200, "fail": 100}})
    a = assess(calls, years, cfg, today=TODAY)["A"]
    assert a.window_months == 24 and a.recent_evaluable == 300
    assert "widened" not in a.note


def test_widening_never_drops_a_recent_record():
    cfg = {"drift": {**CFG["drift"], "max_window_months": 60}}
    calls, years = records({2021: {"fail": 40}, 2025: {"detect": 5}})
    a = assess(calls, years, cfg, today=TODAY)["A"]
    assert a.recent_evaluable >= 5 and a.recent_detected >= 5
