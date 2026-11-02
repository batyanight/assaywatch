"""`assaywatch/trend.py`: a trend over deposit year, reported beside the verdict.

The verdict is a two-window contrast, so a steady slide and a single step read the
same to it; the per-year table was printed and never read by anything. This tests the
Cochran-Armitage statistic the report now prints under that table, and the one rule
that matters more than its value: it never moves a status.
"""

from __future__ import annotations

import math

from assaywatch.drift import AssayDrift, YearStats
from assaywatch.trend import cochran_armitage, describe


def _years(table: dict[int, tuple[int, int]]) -> list[tuple[int, int, int]]:
    return [(y, d, n) for y, (d, n) in table.items()]


def test_a_monotone_decline_is_falling_and_a_hand_computed_z_matches():
    """Four years, 100 records each, detected 95 -> 90 -> 80 -> 70.

    By hand: p = 335/400 = 0.8375; centred scores -1.5, -0.5, 0.5, 1.5;
    T = sum x (d - n p) = (-1.5)(11.25) + (-0.5)(6.25) + (0.5)(-3.75) + (1.5)(-13.75)
      = -16.875 - 3.125 - 1.875 - 20.625 = -42.5;
    Var = p(1-p) * sum n x^2 = 0.8375 * 0.1625 * 500 = 68.046875;
    z = -42.5 / sqrt(68.046875) = -5.152.
    """
    t = cochran_armitage(_years({2020: (95, 100), 2021: (90, 100), 2022: (80, 100), 2023: (70, 100)}))
    assert t is not None
    assert t.direction == "falling"
    assert math.isclose(t.z, -42.5 / math.sqrt(68.046875), rel_tol=1e-9)
    assert t.p < 1e-6
    assert (t.n_years, t.n_records) == (4, 400)


def test_a_single_burst_year_is_not_a_trend():
    """A flat share with one big deposition year: the two-window verdict can be fooled
    by where the burst falls, and this must not be."""
    t = cochran_armitage(_years({2014: (900, 1000), 2019: (90, 100), 2022: (90, 100), 2025: (90, 100)}))
    assert t is not None
    assert math.isclose(t.z, 0.0, abs_tol=1e-9)
    assert t.p > 0.99


def test_too_few_years_or_no_variation_gives_none_not_zero():
    assert cochran_armitage(_years({2024: (10, 10), 2025: (8, 10)})) is None, "two points are not a trend"
    assert cochran_armitage(_years({2023: (10, 10), 2024: (10, 10), 2025: (10, 10)})) is None, "all detect"
    assert cochran_armitage(_years({2023: (0, 10), 2024: (0, 10), 2025: (0, 10)})) is None, "none detect"
    # Years with no evaluable records do not count toward the minimum.
    assert cochran_armitage(_years({2022: (5, 10), 2023: (0, 0), 2024: (4, 10)})) is None
    assert "not tested" in describe(None, 3)


def test_the_trend_is_computed_in_finalise_and_the_verdict_ignores_it():
    """The house rule: beside the verdict, never into it.

    Two assays with the same recent and baseline windows but opposite trends inside
    the baseline must get the same status, interval and note.
    """
    rising, falling = AssayDrift("R", recent_from=2024), AssayDrift("F", recent_from=2024)
    for a, order in ((rising, (60, 70, 80)), (falling, (80, 70, 60))):
        for year, det in zip((2021, 2022, 2023), order, strict=True):
            a.years[year] = YearStats(year)
            a.years[year].counts["detect"] = det
            a.years[year].counts["fail"] = 100 - det
        a.years[2025] = YearStats(2025)
        a.years[2025].counts["detect"] = 40
        a.years[2025].counts["fail"] = 60
        a.finalise()
    assert rising.trend is not None and falling.trend is not None
    # Both fall into the same 2025 drop, so both z are negative; the baseline that
    # was already sliding is steeper. The point is that they DIFFER while every
    # verdict quantity below is identical.
    assert falling.trend.z < rising.trend.z < 0
    assert (rising.status, rising.recent_ci, rising.change_ci, rising.note) == (
        falling.status,
        falling.recent_ci,
        falling.change_ci,
        falling.note,
    )
    assert "Cochran-Armitage" in describe(rising.trend, 3)


# --- the second trend, over distinct footprints (2026-10-30, design-grilled Q4) --------------


def _rows(year_table):
    """{year: [(call, footprint, copies)]} -> call rows carrying a footprint, plus the years."""
    calls, years, i = [], {}, 0
    for year, specs in year_table.items():
        for call, fp, copies in specs:
            for _ in range(copies):
                rid = f"FP{i:05d}"
                calls.append({"assay_id": "A", "record_id": rid, "call": call, "footprint": fp})
                years[rid] = year
                i += 1
    return calls, years


def test_the_footprint_trend_discounts_duplicated_records_and_never_moves_the_verdict():
    """Three baseline years with five distinct detecting footprints each; then 2023, where
    one clone was deposited a hundred times; then 2025, where one failing clone was deposited
    a hundred times. By record that is a steep slide carried by two clones; by footprint it is
    five, five, five, one, zero -- still falling, but on 17 observations rather than 215."""
    from test_drift import CFG, TODAY

    from assaywatch.drift import assess

    table = {y: [("detect", f"f{y}{k}", 1) for k in range(5)] for y in (2020, 2021, 2022)}
    table[2023] = [("detect", "clone23", 100)]
    table[2025] = [("fail", "clone25", 100)]
    calls, years = _rows(table)
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.trend is not None and a.trend_by_footprint is not None
    assert a.trend.n_records == 215 and a.trend_by_footprint.n_records == 17
    assert a.trend.direction == a.trend_by_footprint.direction == "falling"
    assert abs(a.trend_by_footprint.z) < abs(a.trend.z)
    # The verdict is what the records say; neither trend touches it.
    assert a.status == "declining" and a.recent_fraction == 0.0

    text = describe(a.trend, 3, by_footprint=a.trend_by_footprint, footprints_known=True)
    assert "by distinct footprint" in text and "17 footprints" in text
    assert "upper bound" in text and "lower bound" in text


def test_the_footprint_trend_is_absent_when_any_evaluable_row_lacks_a_footprint():
    from test_drift import CFG, TODAY

    from assaywatch.drift import assess

    table = {y: [("detect", f"f{y}", 3), ("fail", f"g{y}", 2)] for y in (2020, 2021, 2022, 2025)}
    calls, years = _rows(table)
    calls[0]["footprint"] = None  # one row from a screen that wrote no footprint columns
    a = assess(calls, years, CFG, today=TODAY)["A"]
    assert a.trend is not None and a.trend_by_footprint is None and a.recent_footprints is None
    text = describe(a.trend, 3, by_footprint=None, footprints_known=False)
    assert "footprints are unknown" in text


def test_the_two_trends_say_so_when_they_disagree_on_direction():
    from assaywatch.trend import Trend

    rec = Trend(z=-3.0, p=0.003, n_years=4, n_records=400)
    fp = Trend(z=0.4, p=0.7, n_years=4, n_records=12)
    text = describe(rec, 3, by_footprint=fp, footprints_known=True)
    assert "disagree on direction" in text
    same = describe(
        rec, 3, by_footprint=Trend(z=-1.1, p=0.27, n_years=4, n_records=12), footprints_known=True
    )
    assert "disagree" not in same
