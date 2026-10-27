"""Interval estimates for a binomial proportion, and for a difference of two.

WHY A MODULE OF ITS OWN. These lived in `drift.py`, which is layered above
`lineage.py` -- so when the per-lineage work needed an interval it could not
import one without a cycle, and it grew its own:
`lineage.confidence_interval_wald`. That left the pipeline computing two
different estimators for the same measurement, one of them the Wald interval
`wilson_interval`'s own docstring argues against, while the report's header said
"Intervals are Wilson 95%" of both. The shipped 2026-10-22 report printed
"detects only 0.0% (0.0%-0.0%)" on 428 records as the evidence for a `declining`
call. A zero-width 95% interval is not a finding.

So the estimator moves below both callers rather than being copied into the
second one. This module imports nothing from the package, which is the whole
point: `drift.py` and `lineage.py` can both have it. Same move, same reason, as
`signature.py`.

WHY WILSON AND NEWCOMBE. The textbook normal-approximation (Wald) interval
misbehaves exactly where this project lives. It can return bounds outside
[0, 1], and at k = 0 or k = n it collapses to zero width and claims certainty
from the handful of records a sparsely sequenced taxon offers. Wilson inverts
the score test instead and stays sensible at both ends (Wilson 1927,
doi:10.1080/01621459.1927.10502953; Brown, Cai & DasGupta 2001,
doi:10.1214/ss/1009213286, is the standard account of why Wald should not be
used). For the change from a baseline, Newcombe's hybrid-score method builds the
interval for a difference of proportions out of the two Wilson intervals and
keeps that behaviour where baselines near 100% live (Newcombe 1998, method 10,
doi:10.1002/(SICI)1097-0258(19980430)17:8<873::AID-SIM779>3.0.CO;2-I).

Both are closed-form arithmetic, so every figure in a report can be recomputed
by hand from the counts in its own per-year table. `tests/test_drift.py` pins
them against published worked examples.
"""

from __future__ import annotations

import math

#: Two-sided 95%, to full precision rather than the 1.96 of a textbook margin.
#: `lineage.py` had its own `z: float = 1.96`, so one pipeline carried two.
Z95 = 1.959963984540054


def wilson_interval(k: int, n: int, z: float = Z95) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion. (0, 1) when n == 0."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = (z / d) * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    lower, upper = centre - half, centre + half
    # At k = 0 the bound is analytically 0, and at k = n analytically 1, but
    # `centre - half` leaves a residue of ~3e-18 there. Clamping restores the
    # exact value rather than reporting a bound of 3.5e-18, which is what
    # statsmodels' reference implementation returns and what tests/test_drift.py
    # holds this to.
    if k == 0:
        lower = 0.0
    if k == n:
        upper = 1.0
    return (max(0.0, lower), min(1.0, upper))


def jeffreys_interval(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Equal-tailed Jeffreys credible interval: the Beta(k+0.5, n-k+0.5) quantiles.

    WHY A THIRD ESTIMATOR, when Wilson is already here and good. Not for the
    report - for the VALIDATION MATRIX, where the counts are single digits and
    the question is different. Wilson answers "what proportion of records does
    this assay detect", over hundreds or thousands. This answers "how well does
    the tool agree with the literature", over 49 cases that collapse to about
    seven independent failure events, and at those counts the interval is the
    finding. `docs/bayesian-scoring-plan.md` C3 puts it exactly: a PPV whose 95%
    interval runs from 5% to 54% "cannot adjudicate a '-1 FP, 0 TP' threshold
    change, and seven settings have been accepted or rejected on exactly that
    kind of delta."

    Jeffreys rather than Wilson here because it is the Bayesian interval with the
    reference prior Beta(0.5, 0.5), so it reads as a statement about the
    quantity rather than about a procedure, and `docs/journal/2026-10-23-baseline.md`
    already quotes its figures - computed by hand, because this function did not
    exist. Brown, Cai & DasGupta 2001 (doi:10.1214/ss/1009213286) recommend it
    for small n alongside Wilson.

    NOT CLOSED FORM, unlike everything else in this module: a Beta quantile has
    no elementary expression, so this is the one figure here that cannot be
    recomputed by hand from the counts. It needs `scipy`, which is the
    `[lineage]` extra rather than a hard dependency, so the import is inside the
    function - the same pattern and the same reason as
    `lineage.worst_lineage_verdict`, and it keeps this module importable by the
    CI job that installs no extras.

    The conventional modification at the edges: at k = 0 the lower bound is 0 and
    at k = n the upper bound is 1, rather than the bare quantile's small residue.
    `n == 0` gives (0, 1), as `wilson_interval` does.

    Pinned in tests against all three figures `docs/journal/2026-10-23-baseline.md`
    reports: 5/11 -> (20.0%, 73.0%), 5/8 -> (29.5%, 88.1%), 2/9 -> (4.9%, 54.4%).
    """
    if n == 0:
        return (0.0, 1.0)
    try:
        from scipy.special import betaincinv
    except ImportError as exc:  # pragma: no cover - mirrors lineage.py's guidance
        raise SystemExit("jeffreys_interval needs scipy: pip install -e '.[lineage]'") from exc
    a, b = k + 0.5, n - k + 0.5
    lower = 0.0 if k == 0 else float(betaincinv(a, b, alpha / 2))
    upper = 1.0 if k == n else float(betaincinv(a, b, 1 - alpha / 2))
    return (max(0.0, lower), min(1.0, upper))


def posterior_below(k: int, n: int, threshold: float) -> float:
    """P(theta < threshold | k of n) under the Jeffreys prior Beta(0.5, 0.5).

    The flag rule `docs/bayesian-scoring-plan.md` C1 proposes in place of "the Wilson
    upper bound is below the threshold": the posterior probability that the true
    detected share is under the bar. Same prior as `jeffreys_interval`, so the two
    agree about what the data say and differ only in how the question is put --
    an interval's edge against a probability mass. 0.5 when n == 0, which is what
    the prior says and what a caller must treat as "no evidence", never as a flag.

    Needs scipy for the regularised incomplete beta, imported inside for the same
    reason `jeffreys_interval` does.
    """
    if n == 0:
        return 0.5
    try:
        from scipy.special import betainc
    except ImportError as exc:  # pragma: no cover - mirrors jeffreys_interval
        raise SystemExit("posterior_below needs scipy: pip install -e '.[lineage]'") from exc
    return float(betainc(k + 0.5, n - k + 0.5, threshold))


def newcombe_difference(k1: int, n1: int, k2: int, n2: int, z: float = Z95) -> tuple[float, float]:
    """CI for p1 - p2 (recent minus baseline) from the two Wilson intervals."""
    if n1 == 0 or n2 == 0:
        return (-1.0, 1.0)
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson_interval(k1, n1, z)
    l2, u2 = wilson_interval(k2, n2, z)
    lower = (p1 - p2) - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    upper = (p1 - p2) + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return (max(-1.0, lower), min(1.0, upper))
