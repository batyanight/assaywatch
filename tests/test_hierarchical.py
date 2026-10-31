"""`assaywatch/hierarchical.py`: one Beta-binomial over an assay's lineages, reported beside the verdict.

The plan's kill test for this layer is "the fitted phi implies no overdispersion, or
shrinkage removes a documented catch". Neither can be run here; what can is that the
estimator says what it should on constructed data, that shrinkage pulls the right way
by the right amount, and that nothing in the verdict reads it.
"""

from __future__ import annotations

import math

import pytest

from assaywatch.drift import AssayDrift, YearStats
from assaywatch.hierarchical import _moment_match, describe, fit_assay

pytest.importorskip("scipy")


def test_lineages_no_more_spread_than_binomial_sampling_fit_no_overdispersion():
    """Every lineage at the same share: the between-lineage variance is nothing but
    sampling noise, and the estimator must say "no phi" rather than invent one."""
    groups = [(f"L{i}", 90, 100) for i in range(6)]
    mu, phi = _moment_match([(k, n) for _, k, n in groups])
    assert math.isclose(mu, 0.9)
    assert phi is None
    fit = fit_assay(groups, threshold=0.9)
    assert fit is not None and fit.phi is None and fit.p_any_below is None
    assert "no shrinkage" in describe(fit, 0.9)


def test_overdispersed_lineages_fit_a_finite_phi_and_shrink_toward_mu():
    """Three lineages at 60%, 90% and 99% of 200 records each: far more spread than
    binomial noise, so phi is finite, and the lowest shrinks UP toward mu, the highest
    DOWN, each by less than its distance to mu."""
    groups = [("low", 120, 200), ("mid", 180, 200), ("high", 198, 200)]
    fit = fit_assay(groups, threshold=0.9)
    assert fit is not None and fit.phi is not None and fit.phi > 0
    by = {p.lineage: p for p in fit.lineages}
    assert by["low"].share < by["low"].shrunk < fit.mu
    assert fit.mu < by["high"].shrunk < by["high"].share
    assert by["low"].lo < by["low"].shrunk < by["low"].hi
    # The worst lineage is the first in the sorted tuple, and its P(theta < 0.9) is
    # near 1 at 120 of 200.
    assert fit.lineages[0].lineage == "low" and fit.lineages[0].p_below > 0.99
    assert fit.p_any_below is not None and fit.p_any_below > 0.99


def test_a_small_lineage_shrinks_more_than_a_large_one():
    """Same raw share, 20 records against 2,000: the small one borrows strength."""
    groups = [("tiny", 14, 20), ("huge", 1400, 2000), ("a", 190, 200), ("b", 195, 200), ("c", 150, 200)]
    fit = fit_assay(groups, threshold=0.9, min_records=30)
    assert fit is not None and fit.phi is not None
    by = {p.lineage: p for p in fit.lineages}
    assert by["tiny"].share == by["huge"].share == 0.7
    assert abs(by["tiny"].shrunk - 0.7) > abs(by["huge"].shrunk - 0.7)
    # `tiny` is below the fitting floor and still gets a posterior: that is the point.
    assert fit.n_lineages == 4


def test_the_verdict_never_reads_the_fit():
    """Two hand-built assays, identical pooled counts, finalise identically whether or
    not a hierarchical fit is attached afterwards."""

    def build(with_fit: bool) -> AssayDrift:
        a = AssayDrift("A", recent_from=2024)
        a.years[2025] = YearStats(2025)
        a.years[2025].counts.update({"detect": 40, "fail": 60})
        if with_fit:
            a.hierarchical = fit_assay([("x", 10, 50), ("y", 30, 50)], 0.9)
        a.finalise()  # once per object: the years fallback accumulates on repeat
        return a

    plain, fitted = build(False), build(True)
    assert fitted.hierarchical is not None and plain.hierarchical is None
    assert (plain.status, plain.recent_ci, plain.note) == (fitted.status, fitted.recent_ci, fitted.note)


def test_the_posterior_verdict_switch_ships_off_and_reads_the_shrunk_worst_lineage():
    """`lineage.verdict_from: posterior` is the mechanism for the plan's second kill test.

    It ships `holm`. Under `posterior`, `_worst_lineage` names the SHRUNK worst lineage and
    fails the assay when its posterior mass under the threshold exceeds the credibility;
    when the fit found no overdispersion, or the shrunk worst lineage has no row above the
    floor, it falls back to Holm rather than naming a lineage the report cannot show.
    """
    from assaywatch.lineage import LineageStats
    from assaywatch.score import load_config

    assert load_config()["lineage"]["verdict_from"] == "holm"

    def stat(name, k, n):
        return LineageStats("A", name, None, n, k, k / n, 0.0, 1.0)

    stats = [stat("low", 120, 200), stat("mid", 180, 200), stat("high", 198, 200)]
    a = AssayDrift("A", lineage_verdict_from="posterior")
    a.hierarchical = fit_assay([("low", 120, 200), ("mid", 180, 200), ("high", 198, 200)], 0.9)
    verdict, idx = a._worst_lineage(stats)
    assert verdict == "failing" and stats[idx].lineage_name == "low"

    # No overdispersion -> no fit to read -> Holm decides.
    b = AssayDrift("B", lineage_verdict_from="posterior")
    b.hierarchical = fit_assay([("x", 90, 100), ("y", 90, 100), ("z", 90, 100)], 0.9)
    assert b.hierarchical is not None and b.hierarchical.phi is None
    holm = AssayDrift("B")._worst_lineage([stat("x", 90, 100), stat("y", 90, 100), stat("z", 90, 100)])
    assert b._worst_lineage([stat("x", 90, 100), stat("y", 90, 100), stat("z", 90, 100)]) == holm
