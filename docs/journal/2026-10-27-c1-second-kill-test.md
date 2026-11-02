# C1's second kill test: driving the override from the shrunk worst lineage moves nothing

2026-10-27, night. The hierarchical layer's first read (`2026-10-27-m1-confirming-rescreen.md`)
cleared the plan's first kill test: the fitted φ says the lineages of a pan-family assay are
far from independent. The second — "shrinkage removes a documented catch" — needed a way to
let the shrunk worst lineage drive the override in place of the Holm-corrected argmin.
`lineage.verdict_from: holm | posterior` now exists for that; it ships `holm`.

    python scripts/retrospective.py --calls results/2026-10-27/calls.tsv.gz \
        --cases docs/validation-cases.tsv --config <config with lineage.verdict_from: posterior>

Under `posterior`, `_worst_lineage` names the worst lineage AFTER shrinkage and fails the
assay when its posterior mass under the threshold exceeds `posterior_credibility: 0.95`.
It falls back to Holm when the fit found no overdispersion (nothing to shrink across) or
when the shrunk worst lineage sits below the assessability floor and so has no row the
report could show — a lineage the report cannot name must not drive its verdict.

## Tier-2, on the M1 run

| | holm (ships) | posterior |
|---|---|---|
| documented failures caught | 6/11 | 6/11 |
| PPV of `declining` | 4/10 | 4/10 |
| false alarms | 4/32 | 4/32 |
| partial gaps named | 2/6 | 2/6 |

**The per-case diff is empty.** No catch is removed, so the second kill test does not fire;
no catch is added either.

## The whole report, on the M1 run

193 assays, 42 declining, 34 low coverage, 8 watch, 30 insufficient data, 19 no recent
data, 60 stable — under both rules. **0 of 240 statuses move.**

## What this decides

The hierarchical layer is now measured on both halves of its plan and on the full report,
and the answer is the one the plan half-expected for the conjugate layer and did not expect
for this one: **as a verdict input it changes nothing.** Where Holm rejects a lineage, the
shrunk posterior rejects it too, because the lineages that fail are failing on hundreds or
thousands of records and shrinkage barely touches them; where the posterior would differ —
thin lineages pulled toward μ — those lineages are below the floor and were never driving a
verdict in the first place.

So it ships as it was built: **beside the verdict, not into it.** `verdict_from: holm` stays.
What the layer earns is the honesty of its numbers rather than a different decision — the
0.0% (0.0%–0.0%) lineages read 1.3% (0.0%–4.7%), the intraclass correlation says in a
parameter what the duplication check says in prose, and a reader can see the winner's curse
quantified. The plan's remaining ambition for C1 — making the assessability floor soft so
that some of the 30 refused assays get a verdict — is not what this layer does, because the
floor is applied to the pooled recent count, not to lineages. That is a different item and
the roadmap now says so.

Also in this commit: `score.load_config` keys its per-chemistry cache to the `scoring`
block it was computed from, so a shallow copy that swaps the block recomputes instead of
answering from the shipped table. The footgun that bit twice today is closed at its source.
