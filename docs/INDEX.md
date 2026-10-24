# docs/ index

70 markdown files, of which exactly one was reachable from any top-level document before
this index existed. Two of the best — `pipeline-architecture.md`, with a mermaid DAG of
the whole pipeline, and `installation.md` — were linked from nothing, so a reader
concluded there was no architecture documentation.

Grouped by what you want. Dated files are **session records**: what was measured on that
day and what was decided. They are not superseded by later ones unless one says so, and
the reasoning in them is usually the point.

## Start here

| | |
|---|---|
| [`pipeline-architecture.md`](pipeline-architecture.md) | the DAG, stage by stage. The best single overview. |
| [`installation.md`](installation.md) | setting up the environment; better than README's Setup section |
| [`RESUME-HERE.md`](RESUME-HERE.md) | where work actually stopped, newest first |
| [`related-work.md`](related-work.md) | what else exists, and every reference the method rests on |
| [`ai-involvement.md`](ai-involvement.md) | how this repository was written, and what checks make it verifiable |

## What the tool's output is worth

Read these before trusting a status.

| | |
|---|---|
| [`2026-10-23-baseline.md`](2026-10-23-baseline.md) | the frozen comparison run, the full tier-2 matrix, and the precision figure: 2 of 9 `declining` calls were real failures |
| [`2026-10-04-pipeline-review.md`](2026-10-04-pipeline-review.md) | the original stage-by-stage review; the estimand critique starts here |
| [`2026-10-20-pipeline-audit.md`](2026-10-20-pipeline-audit.md) | the later audit, with the bench-panel evidence |
| [`2026-10-23-wave4-holdout.md`](2026-10-23-wave4-holdout.md) | why the 49 cases are a development set, and what leave-one-out can and cannot say |
| [`validation-cases.tsv`](validation-cases.tsv) | the cases themselves (the development set) |
| [`validation-cases-heldout.tsv`](validation-cases-heldout.tsv) | empty on purpose; spent the first time a threshold decision reads it |

## The 2026-10-23 plan of attack, in order

| | |
|---|---|
| [`2026-10-23-wave1-report-honesty.md`](2026-10-23-wave1-report-honesty.md) | 704 of 1,512 lineage intervals were zero-width; 19 assays held a status their entry denies |
| [`2026-10-23-wave2-diverged-and-patent.md`](2026-10-23-wave2-diverged-and-patent.md) | `count_diverged_as_fail` tested and kept off; patent records excluded on mechanism |
| [`2026-10-23-wave3-bd-miss.md`](2026-10-23-wave3-bd-miss.md) | the Bd failure: probe sites deposited by 2013 and discarded twice |
| [`2026-10-23-wave3-usutu.md`](2026-10-23-wave3-usutu.md) | a false alarm traced to the flat 3' penalty window |
| [`2026-10-23-wave3-influenza.md`](2026-10-23-wave3-influenza.md) | the miss is `reduced` counting as detected for a probe assay |
| [`2026-10-23-wave3-holm.md`](2026-10-23-wave3-holm.md) | Holm replaces BH, and moves nothing yet |
| [`2026-10-23-wave5-config-schema.md`](2026-10-23-wave5-config-schema.md) | `config.yaml` gets a schema; six defaults lose their second home |
| [`2026-10-23-wave5-triage.md`](2026-10-23-wave5-triage.md) | the report leads with ten assays; anchors instead of JavaScript |
| [`2026-10-23-wave5-what-active-means.md`](2026-10-23-wave5-what-active-means.md) | 173 drafts are eligible, 100 carry no oligo doubt. A maintainer decision |
| [`2026-10-23-wave5-engineering.md`](2026-10-23-wave5-engineering.md) | the memory hazard, and the two refactors deliberately not done |
| [`2026-10-23-oligo-adjudication.md`](2026-10-23-oligo-adjudication.md) | every `near:` and `absent` oligo read against its paper, then screened: 2 corrections kept, 2 reverted because they destroyed a working assay, agreement 84% -> 90% |
| [`2026-10-23-verified-doi-gate.md`](2026-10-23-verified-doi-gate.md) | only verified-DOI assays are live; 10 moved to `pending/`; the seed list's fields and importer removed |
| [`2026-10-23-wave5-elsevier-and-oligo-flags.md`](2026-10-23-wave5-elsevier-and-oligo-flags.md) | the Elsevier block opened: 68 oligos newly checkable; 6 of 21 near-misses are the matcher finding sibling primers |
| [`bayesian-scoring-plan.md`](bayesian-scoring-plan.md) | design only: the three things "Bayesian scoring" could mean, with a kill-test each |

## Design documents, agreed before the code

| | |
|---|---|
| [`2026-10-17-estimand-plan.md`](2026-10-17-estimand-plan.md) | the lineage-conditional estimand, with its own falsifiable prediction |
| [`2026-10-19-subtaxid-resolution.md`](2026-10-19-subtaxid-resolution.md) | grouping below the taxid: subtype, title, sequence cluster |
| [`2026-10-19-lineage-detected-definition.md`](2026-10-19-lineage-detected-definition.md) | what "detected" means per lineage |
| [`2026-10-19-scope-ancestry.md`](2026-10-19-scope-ancestry.md) | scope by taxonomy ancestry rather than exact taxid |

## Calibration and threshold decisions

| | |
|---|---|
| [`2026-10-21-drift-window-calibration.md`](2026-10-21-drift-window-calibration.md) | the window/minimum grid, and why the grid optimum was overruled |
| [`2026-10-18-recalibration.md`](2026-10-18-recalibration.md) | an earlier recalibration pass |
| [`2026-10-21-M1-identity-aware-penalty.md`](2026-10-21-M1-identity-aware-penalty.md) | the mispair-identity candidate |
| [`2026-10-21-M1-shipped.md`](2026-10-21-M1-shipped.md) | M1 shipping |
| [`2026-10-22-M1-tier2.md`](2026-10-22-M1-tier2.md) | M1 reverted: it lost a documented catch. The confusion matrix of record |
| [`2026-10-21-M2-step0-killtest.md`](2026-10-21-M2-step0-killtest.md) | M2 killed at step 0: NN ΔG inverts Kwok's ordering |
| [`2026-10-19-conventional-override-validation.md`](2026-10-19-conventional-override-validation.md) | the per-chemistry override, tried and reverted |
| [`2026-10-19-pan-family-cases.md`](2026-10-19-pan-family-cases.md), [`2026-10-20-pan-family-override.md`](2026-10-20-pan-family-override.md) | pan-family assays and the lineage override |
| [`2026-10-19-orthopox-ati-vaccinia.md`](2026-10-19-orthopox-ati-vaccinia.md) | the hand-checked false positive that patent records caused |

## Bench panels: the only truth below the assay level

`docs/bench-panels/*.tsv` with a header comment recording what was read and from where.
Measured per panel in `2026-10-23-wave2-diverged-and-patent.md`: 160 labelled outcomes,
but only 11 of the 52 negatives are within-family, which is what gates the C2 model.

[`2026-10-19-fap-bench-panel.md`](2026-10-19-fap-bench-panel.md) ·
[`2026-10-20-meyer-ati-bench-panel.md`](2026-10-20-meyer-ati-bench-panel.md) ·
[`2026-10-20-mycoplasma-bench-panel.md`](2026-10-20-mycoplasma-bench-panel.md) ·
[`2026-10-20-rahn-invA-bench-panel.md`](2026-10-20-rahn-invA-bench-panel.md)

## Registry provenance and curation

| | |
|---|---|
| [`2026-10-05-hallucination-audit.md`](2026-10-05-hallucination-audit.md) | the repo-wide audit for fabricated content, and the gates that followed |
| [`2026-10-04-provenance-audit.md`](2026-10-04-provenance-audit.md) | where each entry's oligos came from |
| [`2026-10-05-sequence-provenance-sweep.md`](2026-10-05-sequence-provenance-sweep.md), [`2026-10-05-sequence-verification.md`](2026-10-05-sequence-verification.md) | sequence verification passes |
| [`2026-10-21-predict-primer-provenance.md`](2026-10-21-predict-primer-provenance.md) | the PREDICT panel's provenance |
| [`2026-10-20-scope-curation.md`](2026-10-20-scope-curation.md), [`2026-10-17-flagged-decisions.md`](2026-10-17-flagged-decisions.md) | per-entry curation decisions |
| [`2026-10-14-amplicon-sizes-measured.md`](2026-10-14-amplicon-sizes-measured.md) | amplicon sizes measured rather than quoted |
| [`2026-10-19-taxid-artefacts.md`](2026-10-19-taxid-artefacts.md), [`2026-10-19-subtaxid-resolution.md`](2026-10-19-subtaxid-resolution.md) | taxonomy artefacts |
| [`papers-index.md`](papers-index.md) | the durable record of which papers the registry rests on (`papers/` is gitignored) |
| [`2026-10-05-papers-needed.md`](2026-10-05-papers-needed.md), [`2026-10-05-doi-candidates.md`](2026-10-05-doi-candidates.md) | what still needs reading |
| [`2026-10-06-lab-leads.md`](2026-10-06-lab-leads.md) | 188 unworked leads, with an explicit account of how far to trust them |

## First runs and early findings

[`2026-10-04-first-run-review.md`](2026-10-04-first-run-review.md) ·
[`2026-10-04-assay-investigations.md`](2026-10-04-assay-investigations.md) ·
[`2026-10-04-literature-audit.md`](2026-10-04-literature-audit.md) ·
[`2026-10-05-amplicon-audit.md`](2026-10-05-amplicon-audit.md) ·
[`2026-10-06-research-findings.md`](2026-10-06-research-findings.md) ·
[`2026-10-05-cloud-session-findings.md`](2026-10-05-cloud-session-findings.md)

## Superseded

Kept because the reasoning is still the record, but do not act on them.

| | superseded by |
|---|---|
| `HANDOFF-2026-10-18.md`, `2026-10-18-phase1-complete.md`, `2026-10-18-phase2-handoff.md`, `2026-10-18-session-summary.md` | four documents for one day with no stated precedence. `RESUME-HERE.md` is the live one |
| [`2026-10-22-lineage-plan-salvage.md`](2026-10-22-lineage-plan-salvage.md) | what was kept from the closed PR #3 |
| [`2026-10-05-verification-handoff.md`](2026-10-05-verification-handoff.md), [`2026-10-05-list2-worklist.md`](2026-10-05-list2-worklist.md) | worklists from completed passes |
| [`2026-10-18-pipeline-timekeeping-todo.md`](2026-10-18-pipeline-timekeeping-todo.md) | the timekeeping markers; 5 of 7 shipped |

## Derived tables and worklists

Generated or maintained TSVs. Read columns with `mlr --itsv --opprint head -n 3 FILE`.

| | |
|---|---|
| [`assay-master-sheet.tsv`](assay-master-sheet.tsv), [`assay-master-sheet.md`](assay-master-sheet.md) | one row per assay, generated by `scripts/master_sheet.py` |
| [`oligos-without-doi.tsv`](oligos-without-doi.tsv) | the 33 oligos with no citable source, grouped by where the answer must come from. The `unpublished` group is in `pending/` until a paper turns up |
| [`design-era.tsv`](design-era.tsv) | how much sequence has arrived since each assay was designed, by `scripts/design_era.py`. 71 of 193 assays were designed when their taxon held fewer than 50 archived records |
| [`rename-mapping.tsv`](rename-mapping.tsv) | assay-id renames and removals, so an old calls table still matches |
| [`predict-supplement-verification.tsv`](predict-supplement-verification.tsv) | PREDICT oligos against the published supplements |
| [`needs-review-migration.tsv`](needs-review-migration.tsv) | the one-off migration to the controlled review vocabulary |
| [`2026-10-06-lab-leads.tsv`](2026-10-06-lab-leads.tsv) | the 188 leads behind `2026-10-06-lab-leads.md` |
| [`2026-10-05-pmc-abstract-only.tsv`](2026-10-05-pmc-abstract-only.tsv) | papers where only an abstract was reachable |

## Narrower records

| | |
|---|---|
| [`2026-10-17-nested-family-key.md`](2026-10-17-nested-family-key.md) | how nested rounds are paired into families |
| [`2026-10-20-tier2-rename-resolution.md`](2026-10-20-tier2-rename-resolution.md) | why a validation case must never match nothing silently |
| [`2026-10-22-supplements-and-three-citations.md`](2026-10-22-supplements-and-three-citations.md) | a supplement in `papers/` that the verifier could not see |
| [`2026-10-22-unsigned-screens-cleared.md`](2026-10-22-unsigned-screens-cleared.md) | 20 screens with no signature record, and the file that fixed it |
