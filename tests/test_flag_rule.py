"""`drift.flag_rule`: how "below the threshold" is decided, and that it ships unchanged.

C1 of docs/bayesian-scoring-plan.md proposes replacing "the Wilson upper bound is under
the threshold" with "the posterior probability the share is under it exceeds 0.95". The
mechanism exists so the plan's experiment can run off the cached calls table; it ships
OFF, and the first test pins that, because every published figure rests on the Wilson
rule.
"""

from __future__ import annotations

import math

import pytest

from assaywatch.drift import AssayDrift, YearStats
from assaywatch.interval import jeffreys_interval, posterior_below
from assaywatch.score import load_config

pytest.importorskip("scipy")


def test_the_shipped_config_flags_on_the_wilson_bound():
    cfg = load_config()
    assert cfg["drift"]["flag_rule"] == "wilson"
    assert cfg["drift"]["flag_posterior_credibility"] == 0.95


def test_posterior_below_is_the_jeffreys_mass_under_the_bar():
    """Consistency with the interval already shipped: the equal-tailed 95% Jeffreys
    interval's upper bound sits where exactly 2.5% of the mass lies above it, so the
    posterior mass below that bound is 0.975 by construction."""
    k, n = 85, 100
    _, hi = jeffreys_interval(k, n)
    assert math.isclose(posterior_below(k, n, hi), 0.975, abs_tol=1e-9)
    # Symmetry: the mass below the share's own point estimate is about one half.
    assert 0.4 < posterior_below(k, n, k / n) < 0.6
    # No data, no evidence: the prior's answer, never a flag.
    assert posterior_below(0, 0, 0.9) == 0.5


def test_the_two_rules_agree_on_a_clear_case_and_can_differ_at_the_edge():
    """Large n far below the bar: both flag. The plan's prediction is that they agree
    almost everywhere; the mechanism is for finding where they do not."""

    def build(k: int, n: int, rule: str) -> AssayDrift:
        a = AssayDrift("A", recent_from=2024, flag_rule=rule)
        a.years[2025] = YearStats(2025)
        a.years[2025].counts["detect"] = k
        a.years[2025].counts["fail"] = n - k
        a.finalise()
        return a

    assert build(60, 100, "wilson").status == build(60, 100, "posterior").status == "low coverage"
    assert build(99, 100, "wilson").status == build(99, 100, "posterior").status == "stable"
    # Measured over every (k, n) with 15 <= n <= 400 on 2026-10-27: the two rules
    # disagree on 425 cells and agree on 69,156, and EVERY disagreement runs one way --
    # the posterior flags where Wilson does not, never the reverse, and only at small
    # n (13/17, 18/23, 19/24, ...). That is the plan's prediction: C1 changes the
    # extremes and nothing else. Pin the direction and that the band exists.
    wilson_only, posterior_only = 0, 0
    for n in range(15, 41):
        for k in range(n // 2, n + 1):
            w = build(k, n, "wilson").status in ("low coverage", "declining")
            p = build(k, n, "posterior").status in ("low coverage", "declining")
            wilson_only += w and not p
            posterior_only += p and not w
    assert wilson_only == 0, "a share Wilson flags must also be flagged by the posterior"
    assert posterior_only > 0, "the rules never disagreed at small n; the switch would be inert"
