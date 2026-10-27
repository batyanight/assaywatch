"""A trend test over deposit year. Reported beside the verdict, never folded into it.

WHY THIS EXISTS. `docs/related-work.md` lists "detection indexed by deposit year,
which makes decay visible as a trend rather than as a single pass/fail" as the
project's second contribution, and until 2026-10-27 nothing in the pipeline tested
for a trend. The verdict is a two-window contrast -- the recent window against a
pooled historical baseline -- so an assay whose target had one large deposition
burst in 2014 has its baseline set by 2014, and a steady year-on-year slide and a
single step look identical to it. The per-year table was printed and never read
by anything.

WHAT IT IS. The Cochran-Armitage test for trend (Cochran 1954,
doi:10.2307/3001616; Armitage 1955, doi:10.2307/3001775): for K ordered groups
with n_i trials and d_i successes and scores x_i, under the null of a common
proportion p the statistic

    T = sum_i x_i (d_i - n_i p),   Var(T) = p (1 - p) [ sum_i n_i x_i^2 - (sum_i n_i x_i)^2 / N ]

is asymptotically normal, so z = T / sqrt(Var) and the two-sided p-value is
erfc(|z| / sqrt 2). The scores here are the deposit years themselves, so z < 0 is
a declining share with later deposits. Closed form, no scipy, recomputable by hand
from the per-year table the report already prints -- the same standard
`interval.py` holds its estimators to.

WHAT IT IS NOT. Not a verdict input. The house rule is that a statistic reported
beside a status never moves the status (`drift.py`, degeneracy, the duplication
check all follow it), and there is NO threshold here: a p-value is printed, and
whether 0.05 or 0.001 would be the bar is a question the project has no evidence
to answer, so it is not asked. Not a model of records as independent either: the
same clade structure that makes every interval in the report too narrow makes this
z too large, and the duplication check's footprint count is the honest denominator
it does not have. Read it as "is there a direction", not as "how sure".

The minimum number of years with evaluable records is a config value
(`drift.trend_min_years`), because below three points a "trend" is a line through
two numbers.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Trend:
    """One assay's trend over deposit year."""

    z: float
    p: float
    n_years: int
    n_records: int

    @property
    def direction(self) -> str:
        return "falling" if self.z < 0 else "rising" if self.z > 0 else "flat"


def cochran_armitage(
    years: list[tuple[int, int, int]],
    min_years: int = 3,
) -> Trend | None:
    """Trend over `(year, detected, evaluable)` rows; None when it cannot be tested.

    None, not a z of 0, when fewer than `min_years` years carry evaluable records,
    or when every record detects or none does -- the variance is zero there and
    "no trend" would be the wrong reading of "no variation to test".
    """
    rows = [(float(y), int(d), int(n)) for y, d, n in years if n > 0]
    if len(rows) < min_years:
        return None
    total_n = sum(n for _, _, n in rows)
    total_d = sum(d for _, d, _ in rows)
    p = total_d / total_n
    if p <= 0.0 or p >= 1.0:
        return None
    # Centre the scores on their n-weighted mean so T is the covariance of score
    # and outcome; numerically identical to the textbook form and better behaved
    # for scores in the thousands (calendar years).
    mean_x = sum(n * x for x, _, n in rows) / total_n
    t = sum((x - mean_x) * (d - n * p) for x, d, n in rows)
    var = p * (1 - p) * sum(n * (x - mean_x) ** 2 for x, _, n in rows)
    if var <= 0.0:
        return None
    z = t / math.sqrt(var)
    p_two_sided = math.erfc(abs(z) / math.sqrt(2))
    return Trend(z=z, p=p_two_sided, n_years=len(rows), n_records=total_n)


def describe(trend: Trend | None, min_years: int) -> str:
    """One clause for a report, or the reason there is none."""
    if trend is None:
        return (
            f"trend over deposit year: not tested (fewer than {min_years} years with "
            "evaluable records, or no variation)"
        )
    return (
        f"trend over deposit year: {trend.direction}, z = {trend.z:+.2f}, two-sided p = {trend.p:.3g} "
        f"across {trend.n_years} years and {trend.n_records} records (Cochran-Armitage; records are not "
        f"independent, so read the direction and not the certainty)"
    )
