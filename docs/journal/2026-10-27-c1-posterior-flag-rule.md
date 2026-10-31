# C1, the one-afternoon experiment: a posterior flag rule moves 2 statuses of 233 and nothing in tier-2

2026-10-27. `docs/bayesian-scoring-plan.md` C1 proposes replacing the Wilson interval
and the flag rule with a Beta posterior — `P(θ < 0.90 | data) > 0.95` as the bar, and
later a hierarchical layer so a sparse assay borrows strength. Its own prediction, in its
own words: "C1-conjugate alone will **not** move the tier-2 matrix much: it changes the
extremes and the wording... **If the matrix is the only thing measured, C1 will look like
it did nothing.** Measure the flag count, the refused count, and the flagged share too."
The plan specified a first experiment. This is that experiment, run as written.

    python scripts/c1_intervals.py results/baseline-2026-10-22/lineage.md
    python scripts/retrospective.py --calls results/2026-10-26/calls.tsv.gz \
        --cases docs/validation-cases.tsv --config <config with drift.flag_rule: posterior>

## Part one: every per-lineage interval, three ways

1,351 lineage rows across 161 assays in the 2026-10-22 lineage report, recomputed from
their counts as Wald (what that report shipped), Wilson (what ships now) and Jeffreys.

| | Wald | Wilson | Jeffreys |
|---|---:|---:|---:|
| lineages whose whole interval sits below 90% | 493 | 501 | 500 |
| flagged by this estimator and not by Wilson | 0 | — | 1 |
| intervals of zero width (k = 0 or k = n) | **704** | 0 | 0 |

Mean |Wilson width − Jeffreys width| on lineages with ≥ 100 records: **0.0033**. The
two estimators disagree about the bar on **one lineage in 1,351**. The only thing the
2026-10-22 column got wrong that either fixes is the 704 zero-width intervals — "detects
only 0.0% (0.0%–0.0%)" on 43 records as evidence for a `declining` call — and Wilson
already fixed that on 2026-10-23. There is nothing left for Jeffreys to fix there.

## Part two: the posterior flag rule on the whole report and on tier-2

`drift.flag_rule` now exists with two values. `wilson`, which ships: the recent share is
below the bar when its Wilson 95% upper bound is. `posterior`: the Jeffreys posterior
mass under the bar exceeds `drift.flag_posterior_credibility: 0.95`. Same prior as the
Jeffreys intervals the tier-2 matrix already prints, so the two agree about what the
data say and differ only in how the question is put — an interval's edge against a
probability mass. The `declining` / `low coverage` split (the Newcombe change interval)
and the `insufficient data` refusal are untouched under either rule, by design: C1
conjugate is about the flag, and the refusal is what the hierarchical layer is for.

**Where the two rules can disagree, measured exhaustively** over every (k, n) with
15 ≤ n ≤ 400: 69,156 cells agree, **425 disagree, and every disagreement runs one way** —
the posterior flags where Wilson does not, never the reverse, and only at small n (13 of
17, 18 of 23, 19 of 24, ...). A two-sided 95% Wilson bound is a one-sided 97.5% bar; a
95% posterior mass is a one-sided 95% bar. That gap is the whole difference, and it
only bites where the interval is wide. A test pins the direction.

**On the 2026-10-26 run, re-rendered under both rules:**

| | wilson | posterior |
|---|---|---|
| declining | 36 | 36 |
| low coverage | 42 | **44** |
| watch | 9 | **7** |
| insufficient data (refused) | 30 | 30 |
| stable | 52 | 52 |
| Start here | 10 | 10 |

**2 of 233 statuses move**, both `watch` → `low coverage`, both small-n assays:
`CBPV_RNA1_Rossi_2024` and `RANAVIRUS_dsDNA_variable_intergenic_regi_Pallister_2007`.
No `declining` call gains or loses. The refused count does not move, and cannot: this
rule says nothing about `min_records_for_drift`.

**On tier-2, identical.** Every one of the 49 cases reads the same verdict under both
rules: catches 6/11, PPV 2/9, false alarms 5/32, partial gaps named 2/6, 15 declined.
Not "much the same" — the per-case diff is empty.

## What this decides

**The conjugate half of C1 is measured and it buys the two watch→low-coverage moves
above, at the price of a dependency on scipy in the verdict path.** The plan's kill test
is "it reproduces the Wilson flag on every assay *and* loses a documented catch"; it
loses nothing, so it is not killed, and it changes almost nothing, so it does not ship.
`drift.flag_rule` stays `wilson`. The mechanism stays, as the project's pattern for a
measured-and-not-adopted candidate, so this does not have to be rebuilt to be re-asked.

**The hierarchical layer is the part of C1 that was never about the flag rule**, and the
numbers above say why it is the part worth building: 30 of 188 assays are refused a
verdict for want of records, and no change to how the bar is read touches that. A
Beta-binomial with shrinkage across lineages of one assay, or across assays of one
chemistry, is what lets a 17-record assay say something. That is the open item;
`docs/bayesian-scoring-plan.md` C1 "The hierarchical layer" is its design, and its kill
test is written there: the fitted overdispersion implies independence, or shrinkage
removes a documented catch.

## Caveats stated once

The flagged-share measurement the plan asks for is the `low coverage`/`declining` count
above; the "48 assays currently refused" figure in the plan was the 2026-10-22 run's,
and the equivalent today is 30. Both renders and both tier-2 runs are off the cached
2026-10-26 calls table under the config that shipped on 2026-10-27 (probe switch and
S3b included), so they describe the rule and not the archive.
