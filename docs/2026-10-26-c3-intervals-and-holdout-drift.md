# The matrix now carries its own uncertainty, and it says no candidate can be judged on one case

Plan step 2 (C3, the cheap third of `docs/bayesian-scoring-plan.md`). Two things: the tier-2
matrix reports Jeffreys credible intervals instead of nothing, and `holdout.py`'s recorded
optimism figure has moved since it was written down.

## `interval.jeffreys_interval`, and why a third estimator

`assaywatch/interval.py` already holds Wilson and Newcombe, and they are the right estimators
for the report: hundreds or thousands of records per assay, and a question about *proportion of
records detected*. The validation matrix is a different measurement with single-digit counts —
49 cases that collapse to about **seven independent failure events** — and a different question:
*how well does the tool agree with the literature*. `docs/bayesian-scoring-plan.md` C3 states the
consequence exactly: a PPV whose 95% interval runs from 5% to 54% "cannot adjudicate a '−1 FP,
0 TP' threshold change, and seven settings have been accepted or rejected on exactly that kind
of delta."

Jeffreys is the equal-tailed credible interval of Beta(k+0.5, n−k+0.5) — the Bayesian interval
under the reference prior, recommended for small n by Brown, Cai & DasGupta 2001
(doi:10.1214/ss/1009213286). `docs/2026-10-23-baseline.md` already quoted its figures, computed
by hand because the function did not exist. It does now, and it **reproduces all three to the
decimal they were printed at**: 5/11 → (20.0%, 73.0%), 5/8 → (29.5%, 88.1%), 2/9 → (4.9%, 54.4%).
Those three are the test.

Two deliberate choices. It is **not closed form** — a Beta quantile has no elementary
expression, so it is the one figure in that module which cannot be recomputed by hand from the
counts, and the docstring says so rather than letting the module's "closed-form arithmetic"
promise cover it. And scipy is imported **inside** the function, the same pattern and the same
reason as `lineage.worst_lineage_verdict`: scipy is the `[lineage]` extra, there is a CI job that
installs no extras, and a summary line must not be the thing that makes a dependency mandatory.
`retrospective.py --intervals` defaults to `jeffreys` and falls back to `wilson` if scipy is
absent.

**The estimator is now named in the output**, which is not pedantry. The shipped 2026-10-22
report said "Intervals are Wilson 95%" over numbers half of which were Wald, and that is how a
zero-width interval reached a verdict. A Wilson line prints `CI` and a Jeffreys line prints
`CrI`, because one is a confidence interval about a procedure and the other a credible interval
about the quantity.

## What the matrix looks like with its uncertainty showing

Against `results/2026-10-25/calls.tsv.gz`:

```
precision (intervals: jeffreys):
  declining calls that were documented failures (PPV): 2/9 = 22% (95% CrI 5%-54%)
  documented failures caught: 5/11 = 45% (95% CrI 20%-73%)
    among the cases it judged at all: 5/8 = 62% (95% CrI 29%-88%)
    declined to judge: 3 of 11 `fails` cases
    credited to: low coverage 3, declining 2
    caught by the drift flag itself (declining): 2/11 = 18% (95% CrI 4%-47%)
  failure cases by mechanism: coverage 10, drift 1
  working assays called declining (false alarms): 5/32 = 16% (95% CrI 6%-31%)
```

**Every headline spans 25 to 50 percentage points.** That is the point of doing this before the
candidate ladder rather than after: it is now visible on the page that a one- or two-case delta
on this set is not a result, which is the discipline
`docs/2026-10-24-scoring-strategy-test-plan.md` asks for and the standard that killed M1 and the
conventional override.

**`undecided` is now reported as missing data, not as a miss.** The script printed one
denominator; it prints both. The tool declining to judge a case is a different event from
judging it wrong — 3 of the 11 `fails` rows are declined — so `5/11 = 45%` charges it for
silence and `5/8 = 62%` hides how often it is silent. `docs/2026-10-23-baseline.md` always
reported both; the script now does too.

## `holdout.py`'s optimism has moved, and it was not recorded

`docs/2026-10-23-wave4-holdout.md` reports leave-one-out disagreement **8/49** and optimism
**−1**, with the selection rule picking `{(60,15): 48, (60,10): 1}`. Measured today against
`results/2026-10-25/calls.tsv.gz`:

| | recorded 2026-10-23 | today |
|---|---|---|
| shipped cell (24, 15) | 10 disagreements | 10 disagreements |
| in-sample best (60, 15) | 7 disagreements | 7 disagreements |
| LOO disagreement | **8/49** | **10/49** (20%, 95% CI 11%–34%) |
| optimism of the in-sample figure | **−1** | **−3** |
| cells picked across folds | `{(60,15): 48, (60,10): 1}` | `{(60,15): 46, (60,10): 1, (48,15): 2}` |

The in-sample figures are identical and the out-of-sample ones are worse: the selection rule now
disagrees on two more held-out folds and wanders to a third grid cell on two of them. **Recorded,
not chased** — the plausible cause is simply that the calls table has changed under it (three
days of new deposits, the verified-DOI gate, the chance-pair test), and nothing here says which.
What matters is that a quoted optimism figure drifted without anyone noticing, so it should be
re-measured rather than cited, and the number above is the one to cite until the next run.

Note also that `holdout.py` picked the wrong calls table by default until today (plan step 1.2,
`sorted(...)[-1]` ranking `baseline-2026-10-22` above `2026-10-25`), so a bare invocation was
scoring the frozen baseline. Both runs above name their table explicitly.

## What this does not do

It does not change a verdict, a threshold or a call: `interval.py` gains a function and
`retrospective.py` gains a flag and two lines of output. The matrix's cell counts are unchanged
at 5 agrees / 3 disagrees among `fails`, which is what `docs/2026-10-23-baseline.md` froze.

And it does not fix the thing the intervals reveal. **The drift flag still has one ground-truth
event**, and the held-out set adds none — its two `drift` rows are `expect: partial`, which
`classify()` never consults `mechanism` for. Widening those intervals is a corpus problem, which
is plan step 7 and is long.
