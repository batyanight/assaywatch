# The report now tests for a trend over deposit year, beside the verdict and never into it

2026-10-27. `docs/related-work.md` has listed "detection indexed by deposit year, which
makes decay visible as a trend rather than as a single pass/fail" as the project's
second contribution since the file was written. Until today nothing in the pipeline
tested for a trend. The verdict is a two-window contrast — the recent window against a
pooled historical baseline — so a steady year-on-year slide and a single step read
identically to it, and an assay whose target had one large deposition burst in 2014 has
its baseline set by 2014. The per-year table was printed in every report and read by
nothing.

## What ships

`assaywatch/trend.py`: the Cochran–Armitage test for trend with the deposit years as
scores. For K years with n_i evaluable records and d_i detected, under a common
proportion p,

    T = Σ x_i (d_i − n_i p),   Var(T) = p(1−p) Σ n_i (x_i − x̄)²,   z = T / √Var,

two-sided p = erfc(|z|/√2). Closed form, no scipy, recomputable by hand from the
per-year table the report already prints — the standard `interval.py` holds its own
estimators to. `drift.finalise` computes it after the intervals and the report prints one
clause under each flagged assay's per-year table:

> trend over deposit year: falling, z = −5.15, two-sided p = 2.6e-07 across 4 years and
> 400 records (Cochran-Armitage; records are not independent, so read the direction and
> not the certainty)

That example is the test's hand-computed case: 95 → 90 → 80 → 70 of 100 per year, which
gives T = −42.5, Var = 68.047, z = −5.152. A flat 90% share with one 1,000-record burst
year gives z = 0 exactly, which is the case the two-window verdict can be fooled by.

## Three rules, stated because each was a choice

**It never moves a status.** The house rule for everything reported beside a verdict —
degeneracy, the duplication check, the specificity arm — and a test pins it: two assays
with identical recent and baseline windows but opposite trends inside the baseline get
the same status, the same intervals and the same note, and different z.

**There is no threshold.** Whether 0.05 or 0.001 would be the bar is a question this
project has no evidence to answer, so no number is written and nothing is asked of the
p-value. The one setting is `drift.trend_min_years: 3`, the count of years with
evaluable records below which no trend is reported, and that floor is the meaning of the
word rather than a fitted value: two points are a line.

**It is not a model of independent records.** The same clade structure that makes every
interval in the report too narrow makes this z too large. The duplication check's
footprint count is the honest denominator it does not have, so the printed clause says
to read the direction and not the certainty. A version of this test over distinct
footprints rather than records is the obvious next step and is not built.

## What it corrects

`docs/related-work.md` contribution #2 now says what ships: the verdict is still a
two-window contrast, and what makes the series more than a table is this statistic,
reported and not folded in.
