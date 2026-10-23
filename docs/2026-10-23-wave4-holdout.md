# Wave 4: leave-one-out comes back clean, and that is the problem (2026-10-23)

Plan items 4.1, 4.3 and 4.4. The 49 cases in `docs/validation-cases.tsv` are now
labelled the **development set**, and `scripts/holdout.py` prices what tuning on them
bought.

## What was measured

Leave-one-out over a stated selection rule — "pick the grid cell with fewest
disagreements" — on the one pair of settings the project has already swept
(`docs/2026-10-21-drift-window-calibration.md`): `recent_window_months` x
`min_records_for_drift`, 5 x 4 cells. Evidence loads once and all 20 cells score in
process.

```
shipped cell (24, 15): 10 disagreements
in-sample best (60, 15): 7 disagreements

  in-sample agreement            18/49 = 37% (95% CI 25%-51%)
  LEAVE-ONE-OUT agreement        18/49 = 37% (95% CI 25%-51%)
  in-sample disagreement          7/49 = 14% (95% CI 7%-27%)
  LEAVE-ONE-OUT disagreement      8/49 = 16% (95% CI 9%-29%)

  optimism of the in-sample figure: -1 disagreement
  cells the rule picked across folds: {(60, 15): 48, (60, 10): 1}
```

## Two findings, and the second matters more

**1. The shipped thresholds are not fitted to this set.** The in-sample optimum is
(60, 15) at 7 disagreements; what ships is (24, 15) at 10. The maintainer left three
disagreements on the table. That tempers the overfitting worry on this pair
specifically: `docs/2026-10-23-baseline.md` says seven settings were "accepted or
rejected on their effect on this matrix", and for the window the honest version is that
the matrix was consulted and then **overruled**.

**2. LOO prices this rule's optimism at about one case — and the rule it validates is
one the project was right to reject.** 48 of 49 folds pick (60, 15), so the selection is
stable and generalises within the sample. But a 60-month "recent" window means an assay
is judged on five years of deposits, and
`docs/2026-10-21-drift-window-calibration.md:72-86` measured what that hides: four
assays read healthy at 60 months while their last 12 months sit 20-41 points lower,
including `FILOVIRUS_ssRNA_L_gene` (87.7% over 60 months, 51.4% over the last 12) and
`PAPILLOMAVIRUS_dsDNA_L1_gene` (86.0% vs 65.7%). A drift monitor exists to warn early;
the development set scores historical as-of accuracy and **cannot see the cost of
warning late**, so it prefers a long window for a reason that has nothing to do with
being right.

So LOO measured the wrong thing, accurately. It is the right tool for "did this rule
overfit the sample" and it is blind to "is the sample measuring what we care about". A
clean cross-validation result on a mis-specified objective is the most misleading number
available, and it is why resampling cannot substitute for held-out cases.

## What this does and does not license

- **Does:** report the window/minimum pair without the overfitting caveat, since LOO
  prices its optimism at one case and the shipped value is three worse than the optimum.
- **Does not:** license tuning anything else on this set. Six further settings were
  decided on it with no sweepable range, so no resampling can price them:
  `drift.require_working_baseline`, `lineage.require_working_baseline`,
  `lineage.min_records_per_lineage`, `lineage.group_at_rank`,
  `lineage.unclassified_is_bucket`, and `scoring.mispair_penalty` (shipped, then
  reverted). `scripts/holdout.py` names them in its output rather than leaving the gap
  implicit.
- **Does not:** license `scoring.by_chemistry` (plan item 4.5). Wave 3 produced three
  concrete calibration cases pulling in both directions —
  `docs/2026-10-23-wave3-usutu.md` (conventional scored too harshly),
  `docs/2026-10-23-wave3-influenza.md` (probe `reduced` counted as success),
  `docs/2026-10-23-wave3-bd-miss.md` (amplicon-level and ungapped) — and all three are
  in the development set. Fitting a per-chemistry table on them and reporting the
  improvement would be the exact error this wave exists to stop.

## The held-out set: protocol, not intention

`docs/validation-cases-heldout.tsv` is created empty with the same columns and one rule
in its header: **no threshold decision may consult it until the thresholds are final.**
To make that enforceable rather than aspirational, `scripts/retrospective.py --cases`
takes one file at a time and nothing reads the held-out file by default.

Collection target, from the plan: **15-20 cases, at least 5 with `mechanism: drift`**,
since the development set has exactly one. `scripts/scan_literature.py` is the lead
finder (it proposes and never adds), and `docs/2026-10-06-lab-leads.md` holds 188
unworked rows. The sweep shares its reading with the C2 bench corpus
(`docs/bayesian-scoring-plan.md`): assay-level outcomes for tier-2, per-type or
per-strain band tables for C2, one pass through each paper.

What qualifies, same bar as the development set: a paper, erratum or redesign that
reports how an assay **already in the registry** performed, with an `as_of` date no
later than the sequences the authors could have seen. What does not: a new assay's own
validation against its own panel, which says nothing about drift.
