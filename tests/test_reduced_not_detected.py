"""`drift.reduced_not_detected_for`: a `reduced` probe call need not be a detection.

Built 2026-10-26 and shipped EMPTY, the same pattern as `scoring.engine: serial`,
`scoring.by_chemistry` and `scoring.locus_identity_min` - the mechanism is here and
the numbers are not. So the first thing these tests pin is that it is inert, because
an accidentally-live switch would move published verdicts for 51 entries.

Priced in docs/2026-10-26-s3-chemistry-switches.md: on for `hydrolysis_probe` and
`mgb` it takes documented failures caught from 5/11 to 6/11 with no increase in false
alarms, and costs two published positives on the Leptospira panel.
"""

from __future__ import annotations

from collections import Counter

from assaywatch.drift import (
    DETECTED_CALLS,
    DETECTED_CALLS_NO_REDUCED,
    AssayDrift,
    YearStats,
    reduced_not_detected_ids,
)
from assaywatch.score import load_config

CFG = load_config()
CHEMISTRY = {"PROBE": "hydrolysis_probe", "MGB": "mgb", "CONV": "conventional", "SYBR": "sybr"}


def test_the_shipped_config_leaves_the_switch_empty_and_selects_nothing():
    """The load-bearing test. A live switch would move 51 entries' verdicts."""
    assert CFG["drift"]["reduced_not_detected_for"] == []
    assert reduced_not_detected_ids(CHEMISTRY, CFG) == set()


def test_the_default_detected_share_is_detect_plus_reduced():
    """What `drift.py` has always done, and what every published figure rests on."""
    assert DETECTED_CALLS == ("detect", "reduced")
    y = YearStats(2026, Counter({"detect": 3, "reduced": 2, "fail": 5}))
    assert y.detected == 5
    assert y.evaluable == 10
    assert y.fraction == 0.5


def test_a_named_chemistry_drops_reduced_from_the_numerator_only():
    """`evaluable` must not move, or this becomes a denominator change.

    Taking a row out of the numerator and leaving the denominator alone is exactly
    what "not detected" means. Moving both would make it a different candidate on the
    axis that produced three failures on 2026-10-25.
    """
    y = YearStats(2026, Counter({"detect": 3, "reduced": 2, "fail": 5}), DETECTED_CALLS_NO_REDUCED)
    assert y.detected == 3
    assert y.evaluable == 10, "the denominator must be untouched"
    assert y.fraction == 0.3


def test_only_the_named_chemistries_are_selected():
    cfg = {"drift": {"reduced_not_detected_for": ["hydrolysis_probe", "mgb"]}}
    assert reduced_not_detected_ids(CHEMISTRY, cfg) == {"PROBE", "MGB"}
    one = {"drift": {"reduced_not_detected_for": ["mgb"]}}
    assert reduced_not_detected_ids(CHEMISTRY, one) == {"MGB"}
    # A chemistry no assay has selects nothing rather than erroring.
    assert reduced_not_detected_ids(CHEMISTRY, {"drift": {"reduced_not_detected_for": ["rpa"]}}) == set()


def test_an_assay_drift_propagates_its_answer_to_every_year_it_builds():
    """One assay cannot disagree with itself across years.

    `_tally_window` creates a `YearStats` per deposit year and `finalise` creates two
    more for the recent and baseline windows. If any of them kept the default while
    the assay did not, a year table and its own summary line would disagree.
    """
    a = AssayDrift("A", detected_calls=DETECTED_CALLS_NO_REDUCED, recent_from=2024)
    a.recent_counts = Counter({"detect": 1, "reduced": 4, "fail": 0})
    a.baseline_counts = Counter({"detect": 5, "reduced": 0, "fail": 0})
    a.finalise()
    assert a.recent_detected == 1, "reduced must not count toward the recent numerator"
    assert a.recent_evaluable == 5, "but it must stay in the denominator"
    assert a.baseline_detected == 5


def test_the_default_assay_drift_is_unchanged_by_the_new_field():
    """Regression guard: every hand-built caller omits it and must behave as before."""
    a = AssayDrift("A", recent_from=2024)
    assert a.detected_calls == DETECTED_CALLS
    a.recent_counts = Counter({"detect": 1, "reduced": 4, "fail": 0})
    a.baseline_counts = Counter({"detect": 5})
    a.finalise()
    assert a.recent_detected == 5
