"""C1, the hierarchical layer: an assay's lineages share one Beta-binomial. Reported, never a verdict.

THE MODEL (docs/bayesian-scoring-plan.md, "The hierarchical layer, which is the real
prize"). For assay a and lineage l,

    theta_al ~ Beta(mu_a * phi_a, (1 - mu_a) * phi_a)
    k_al     ~ Binomial(n_al, theta_al)

mu_a is the assay's overall detection level, phi_a its concentration -- the inverse
of the overdispersion across lineages. Three things the report does separately today
fall out of it at once: lineages with few records shrink toward mu_a and those with
many barely move (which is what Holm is there to do); phi_a IS the pseudo-replication
the footprint check estimates by hand (near-identical clones make lineage shares more
extreme than binomial sampling allows, phi comes out small, every interval widens);
and the hard `min_records_per_lineage` floor becomes soft, because a 25-record lineage
gets a posterior instead of being invisible.

DETERMINISTIC, BY DESIGN. The plan says "empirical Bayes -- moment-matching or marginal
maximum likelihood, then closed-form posteriors (Efron 2004). scipy-only,
deterministic, and most of the benefit." This is the moment-matching half: mu is the
pooled share, phi is read off the excess of the between-lineage variance over what
binomial sampling alone would produce (Kleinman 1973, the standard estimator for the
beta-binomial). Posteriors are then conjugate and closed-form, and the one probability
that is not -- P(theta < threshold) -- is a regularised incomplete beta, which is the
same call `interval.jeffreys_interval` already makes.

WHAT IT IS NOT, YET. Not a verdict input: `drift.finalise` and `_lineage_check` never
read it, and a test pins that. The plan's kill test for this layer -- "the fitted phi
implies no overdispersion (records really are independent) or shrinkage removes a
documented catch" -- can only be run once this is printed beside the existing verdicts
over a real run and tier-2 is re-read with the posterior worst lineage in place of the
Holm one. This module makes that measurement possible; it does not make it.

TWO HONEST LIMITS. P(min_l theta_l < threshold) is computed as 1 - prod(1 - p_l),
which treats the lineage posteriors as independent given (mu, phi); they are not
exactly, because (mu, phi) were estimated from the same data. And moment matching can
return a negative overdispersion when lineages are MORE alike than binomial sampling
predicts (pooled records, a handful of lineages); phi is then undefined and the fit
says so instead of inventing a number.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LineagePosterior:
    """One lineage under the assay's fitted Beta-binomial."""

    lineage: str
    n: int
    k: int
    share: float  # k / n, the raw share
    shrunk: float  # posterior mean, pulled toward the assay's mu
    lo: float  # equal-tailed 95% credible interval
    hi: float
    p_below: float  # P(theta < threshold | k, n, mu, phi)


@dataclass(frozen=True)
class HierarchicalFit:
    """An assay's Beta-binomial over its lineages, plus every lineage's posterior."""

    mu: float
    phi: float | None  # None: the lineages are at least as alike as binomial sampling allows
    n_lineages: int
    n_records: int
    lineages: tuple[LineagePosterior, ...]
    p_any_below: float | None  # 1 - prod(1 - p_below); None when phi is None

    @property
    def overdispersed(self) -> bool | None:
        """Were the lineage shares more spread than binomial sampling predicts?"""
        return None if self.phi is None else True


def _moment_match(groups: list[tuple[int, int]]) -> tuple[float, float | None]:
    """(mu, phi) by the method of moments over (k, n) groups; phi None if not overdispersed.

    With p_i = k_i / n_i and weights n_i, the between-group variance of the shares
    exceeds the binomial expectation mu(1-mu) * sum(1/n_i)/m by an amount that is
    rho * mu(1-mu) * (1 - mean(1/n_i)), where rho = 1 / (phi + 1) is the intraclass
    correlation of a beta-binomial (Kleinman 1973). Solving for rho gives phi.
    """
    n_tot = sum(n for _, n in groups)
    k_tot = sum(k for k, _ in groups)
    mu = k_tot / n_tot
    m = len(groups)
    if m < 2 or mu <= 0.0 or mu >= 1.0:
        return mu, None
    var_between = sum(n * (k / n - mu) ** 2 for k, n in groups) / n_tot
    mean_inv_n = sum(n * (1 / n) for _, n in groups) / n_tot  # = m / n_tot
    binomial_part = mu * (1 - mu) * mean_inv_n
    excess = var_between - binomial_part
    scale = mu * (1 - mu) * (1 - mean_inv_n)
    if excess <= 0.0 or scale <= 0.0:
        return mu, None
    rho = min(excess / scale, 0.999999)
    return mu, (1 - rho) / rho


def fit_assay(
    groups: list[tuple[str, int, int]],
    threshold: float,
    min_records: int = 1,
) -> HierarchicalFit | None:
    """Fit one assay's lineages; `groups` is (lineage, k_detected, n_evaluable).

    Lineages below `min_records` evaluable are left out of the FIT (they would
    dominate a moment estimate with noise) but still get a posterior, which is the
    whole point of shrinkage: a 12-record lineage is reported, pulled toward mu.
    None when there is nothing to fit on.
    """
    try:
        from scipy.special import betainc, betaincinv
    except ImportError as exc:  # pragma: no cover - mirrors interval.jeffreys_interval
        raise SystemExit("the hierarchical layer needs scipy: pip install -e '.[lineage]'") from exc

    fit_on = [(k, n) for _, k, n in groups if n >= min_records and n > 0]
    if not fit_on:
        return None
    mu, phi = _moment_match(fit_on)

    posteriors: list[LineagePosterior] = []
    p_any = 1.0
    for lineage, k, n in groups:
        if n == 0:
            continue
        if phi is None:
            # No overdispersion to borrow: fall back to the Jeffreys posterior for
            # each lineage alone, which is what the report's intervals already are.
            a, b = k + 0.5, n - k + 0.5
        else:
            a, b = k + mu * phi, n - k + (1 - mu) * phi
        mean = a / (a + b)
        lo = 0.0 if k == 0 and phi is None else float(betaincinv(a, b, 0.025))
        hi = 1.0 if k == n and phi is None else float(betaincinv(a, b, 0.975))
        p_below = float(betainc(a, b, threshold))
        posteriors.append(LineagePosterior(lineage, n, k, k / n, mean, lo, hi, p_below))
        p_any *= 1 - p_below
    return HierarchicalFit(
        mu=mu,
        phi=phi,
        n_lineages=len(fit_on),
        n_records=sum(n for _, _, n in groups),
        lineages=tuple(sorted(posteriors, key=lambda p: p.shrunk)),
        p_any_below=(None if phi is None else 1 - p_any),
    )


def describe(fit: HierarchicalFit | None, threshold: float) -> str:
    """One clause for a report, or why there is none."""
    if fit is None:
        return "hierarchical fit: no lineage with enough records to fit on"
    if fit.phi is None:
        return (
            f"hierarchical fit over {fit.n_lineages} lineages: mu = {fit.mu:.1%}, lineages no more spread "
            f"than binomial sampling predicts, so no shrinkage was applied and each posterior is the "
            f"lineage alone"
        )
    worst = fit.lineages[0]
    return (
        f"hierarchical fit over {fit.n_lineages} lineages: mu = {fit.mu:.1%}, phi = {fit.phi:.1f} "
        f"(intraclass correlation {1 / (fit.phi + 1):.3f}); worst lineage after shrinkage {worst.lineage} at "
        f"{worst.shrunk:.1%} ({worst.lo:.1%}-{worst.hi:.1%}, raw {worst.share:.1%} on {worst.n}); "
        f"P(some lineage < {threshold:.0%}) = {fit.p_any_below:.3f} treating lineages as independent "
        f"given the fit. "
        f"Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)"
    )
