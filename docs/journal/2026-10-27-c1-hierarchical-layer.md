# C1's hierarchical layer is built and printed beside each verdict; its kill test waits for a run to read

2026-10-27, late. The conjugate half of C1 was measured this afternoon and changed almost
nothing (`2026-10-27-c1-posterior-flag-rule.md`). What that measurement argued for was
the half of C1 that was never about the flag rule: 30 of 188 assays are refused a verdict
for want of records, and the lineage layer takes an argmin over noisy shares and reports
it with no acknowledgement of the winner's curse. `docs/bayesian-scoring-plan.md` calls the
hierarchical layer "the real prize". It now exists.

## What is built

`assaywatch/hierarchical.py`. For one assay with lineages l,

    θ_l ~ Beta(μ·φ, (1−μ)·φ),   k_l ~ Binomial(n_l, θ_l)

fitted by the method of moments — μ is the pooled share; φ comes off the excess of the
between-lineage variance over binomial sampling (Kleinman 1973's beta-binomial
estimator, ρ = 1/(φ+1) the intraclass correlation) — and then every lineage's posterior
is conjugate and closed-form: `Beta(k + μφ, n−k + (1−μ)φ)`, its mean the shrunk share,
its 2.5/97.5% quantiles the credible interval, and `P(θ_l < threshold)` a regularised
incomplete beta, the same call `interval.jeffreys_interval` already makes. The plan said
"deterministic first, sampling only if forced"; this is the deterministic version and
nothing samples.

Three things the report does separately today fall out of it: lineages with few records
shrink toward μ and large ones barely move (what Holm is there to do); φ *is* the
pseudo-replication the footprint check estimates by hand, because clones make lineage
shares more extreme than sampling allows and φ comes out small; and the
`min_records_per_lineage` floor is soft — the fit is made on lineages above the floor,
but every lineage with a record gets a posterior, so a 12-record lineage is pulled toward
μ and reported rather than being invisible.

`drift._lineage_check` fits it after the existing per-lineage stats and the report prints
one clause after the lineage material:

> hierarchical fit over 57 lineages: mu = 97.1%, phi = 41.3 (intraclass correlation
> 0.024); worst lineage after shrinkage H1N2 at 72.6% (70.6%–74.5%, raw 72.1% on 1917);
> P(some lineage < 90%) = 1.000 treating lineages as independent given the fit.
> Reported beside the verdict; not a verdict input

(an illustration of the shape, not a measured line; the first real one is in the next
run's report).

## Two honest limits, stated in the module

`P(min θ < threshold)` is `1 − Π(1 − p_l)`, which treats the lineage posteriors as
independent given (μ, φ); they are not exactly, since the pair was estimated from the
same data. And moment matching can find the lineages *less* spread than binomial sampling
predicts — pooled records, a handful of lineages — in which case φ is undefined; the fit
says so and falls back to each lineage's own Jeffreys posterior rather than inventing a
number. A test pins both behaviours on constructed data, and a third pins that two assays
with identical pooled counts finalise identically whether or not a fit is attached.

## What it is not, yet

Not a verdict input. The plan's kill test for this layer — "the fitted φ implies no
overdispersion (records really are independent) or shrinkage removes a documented catch"
— needs the layer printed beside the existing verdicts over a real run, and tier-2 re-read
with the posterior worst lineage in place of the Holm one. The run in progress as this is
written (the first under M1) will carry the first real lines; reading them is the next
step, and only after that is "should the shrunk worst lineage drive the override" a
question with evidence behind it.
