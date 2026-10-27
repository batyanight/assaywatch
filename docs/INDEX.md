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
| [`validation-cases-heldout.tsv`](validation-cases-heldout.tsv) | 34 rows as of 2026-10-24, unscored; spent the first time a threshold decision reads it |
| [`2026-10-24-heldout-candidates.md`](2026-10-24-heldout-candidates.md) | the first held-out sweep: 31 rows from 17 papers, and why the 5-drift-case target was missed |
| [`2026-10-26-bd-phase1-site-level-measured.md`](2026-10-26-bd-phase1-site-level-measured.md) | The Bd miss priced, measurement only, and **the doc corrects itself the same day**. Two findings hold: the amplicon-level rule discards **297,651 rows that carry a credible primer site** (10.9% of the table, exact from the calls table), and gapped matching explains 426 of 932,856 evaluable fails (**0.046%**), reproducing 2026-10-04's "not worth building". The third is WITHDRAWN: a Bd probe-site table (122 judgeable, 94 failing, 25 indel-explained) rested on an offset one record in three agreed with. **Bd turns out to be unmeasurable by this route** - only 3 of its 9,493 records hold all three sites and they disagree - which is the same fact as the case itself, so the assay that motivated site-level evaluation is the one whose geometry it cannot calibrate. Caught because a sibling assay read 42 of 42 failures as indel-explained where a hand check found the probe at gapped cost 0. Confirms site-level evaluation cannot be replayed: no `no_amplicon` row carries a site coordinate |
| [`2026-10-26-retrospective-case-search.md`](2026-10-26-retrospective-case-search.md) | A NEW instrument for retrospective cases after the old seam and the held-out set were both spent: the CITATION GRAPH rather than oligo text, since a group using a published assay cites it and does not retype its primers. 220 candidates in `docs/2026-10-26-retrospective-candidates.tsv`. Four read: one rejected as CIRCULAR (an in silico mismatch count, the same method as ours), two unresolved on ASSAY IDENTITY, one that pays. **The finding that matters: identity is the bottleneck, not discovery** - a performance report names the assay locally or by citation and rarely reprints its oligos. One new `fails` case is proposed pending one supplementary table. Also refutes Furuyama 2018, carried for days as the only named drift lead: it is a LAMP primer paper and the registry holds no LAMP assay |
| [`2026-10-26-heldout-read-m1-rejected.md`](2026-10-26-heldout-read-m1-rejected.md) | **THE HELD-OUT SET HAS BEEN READ AND IS SPENT** (2026-10-26, on the maintainer's instruction, for the one decision it was reserved for). **M1 is REJECTED**: it passes the half of its gate I pre-registered (no catch lost, 4/9 both) and fails the half I omitted, which is its own documented gate from 2026-10-21 - a `works` case newly disagrees. The drift flag's precision falls 3/4 to 1/3 and the shipped rule's PERFECT 0-of-17 false-alarm record on this set breaks. Confirmed by a real rescreen of 37,522 records, 0 call disagreements, so the false alarm is M1's and not the harness's. **And the mechanism is a finding about the drift model: a uniform loosening can MANUFACTURE a `declining` verdict** by lifting the baseline more than the recent window - M1 makes this assay's recent share BETTER, 64.9% to 67.6%, and that is what flips it. Same defect as the 2026-10-22 revert, on a case four days and one set apart |
| [`2026-10-26-m1-confirming-rescreen.md`](2026-10-26-m1-confirming-rescreen.md) | **M1 is PROPOSED for shipping** (branch `experiment/2026-10-26-m1-proposed`, not on main, because the held-out set has not been read). Records the confirming rescreen the decision was conditional on, and with it **the first measurement of the replay harness's one approximation**: M1 really rescreened over every tier-2 assay it moves, 514,096 rows, gives 2 call and 11 penalty disagreements against the replay - 0.0004%, and ALL of them pessimistic, because a replay is stuck re-scoring the amplicon the shipped rule chose. So every rejection in the ladder stands without qualification and the survivors are under-credited. Neither disagreement can move a verdict: both fall on one assay sitting at 97.9% of 755 records against a 90% threshold |
| [`2026-10-26-s4-m1-no-longer-refuted.md`](2026-10-26-s4-m1-no-longer-refuted.md) | S4, re-specified because S1 and S2 died. **M1 alone now changes ZERO rows of the 49-case tier-2 matrix**, so both halves of the gate it failed on 2026-10-22 pass, while rescuing 7 documented panel false fails (5 FAP, 2 Barrett) at no panel loss and no cost on the Rahn control. The 17 Leucocytozoon record movements reproduce EXACTLY; what changed is that the verdict is no longer near its boundary - its recent window now holds 21 records and M1 moves the interval's upper bound 50% -> 55% against a 90% threshold. Verified by a real rescreen (7,904 records, 0 replay disagreements), so not a harness artefact. **A closed decision rests on a measurement that no longer reproduces**; `docs/2026-10-22-M1-tier2.md` is marked superseded in its conclusion. Also ends the ladder: four rungs, two rejected, two a maintainer decision, none shipped |
| [`2026-10-26-s3-chemistry-switches.md`](2026-10-26-s3-chemistry-switches.md) | S3's two per-chemistry switches, and **the chemistry axis carries signal on one side only**. The probe switch (a `reduced` probe call is not a detection) takes documented failures caught 5/11 -> 6/11 and PPV 2/9 -> 3/10 **with no increase in false alarms**, fixing the influenza Matrix-gene case it predicted - the only rung that tightens, so its extra flags are evidence rather than a loosening artefact. It fails its own kill criterion on two published positives of the Leptospira panel, both `reduced` probe calls, so it is **the first candidate that is a maintainer decision rather than a rejection**. The conventional terminal-mismatch switch is **inert**: 251 calls of 2.7 M and no verdict anywhere, which answers a ROADMAP Phase 2 claim that `terminal_mismatch_fails` inflates `fail` across the conventional majority |
| [`2026-10-26-s2-smooth-decay-killed.md`](2026-10-26-s2-smooth-decay-killed.md) | S2 (a smooth exponential positional decay) **passes its own pre-registered kill criterion and loses four documented catches nobody named**, including `CDV_P_gene_Scagliarini_2007` @2021-07-06, the project's ONLY drift ground-truth event. Documented failures caught 5/11 -> 1/11, PPV 2/9 -> 0/4, while false alarms IMPROVE 5/32 -> 2/32 - so total disagreements go 10 -> 11 and **an aggregate reads the candidate as neutral**. The fitted curve turns out to discount the whole 3' window (d=5 costs less than half of today), which is where drift signal lives. Lesson for the protocol: a named kill criterion is a probe and can be insensitive; the standing no-lost-catch rule is what does the work |
| [`2026-10-26-s1-serial-killed.md`](2026-10-26-s1-serial-killed.md) | S1 (`engine: serial`) is the first rung of the pre-registered ladder and it is **dead on its own criterion, twice over**: no threshold pair in the grid is clean on the panels, and tier-2 loses two named documented catches (both Paramyxovirinae L-gene at 2019-02-01). Three findings outlive it - **`oligo_ok_max` has no effect on panel accuracy at all**, so the panels can fit only one of its two numbers; the curve bottoms out at `oligo_weak_max: 3.0`, the value already shipped; and **Rahn reports zero cost while Forslund loses within-family negatives**, which is the argument for `role: control` turned into a measurement. Also records that netting would have read a 46% error reduction out of losing seven of ten informative negatives |
| [`2026-10-26-c3-intervals-and-holdout-drift.md`](2026-10-26-c3-intervals-and-holdout-drift.md) | the tier-2 matrix now carries Jeffreys credible intervals (`interval.jeffreys_interval`, pinned against the three figures `2026-10-23-baseline.md` computed by hand), and every headline spans 25-50 points - so a one- or two-case delta on this set is visibly not a result. Also reports `undecided` as missing data rather than a miss, and records that `holdout.py`'s optimism has drifted from the recorded -1 to -3 |
| [`2026-10-25-stale-orphan-screens.md`](2026-10-25-stale-orphan-screens.md) | **read before any whole-archive measurement.** `results/screened/` keeps ORPHAN group screens that nothing rescreens - one dated 2026-10-03, before `declared_tolerance` - so globbing it reads months-old scoring rules as current. Inflated three of 2026-10-25's measurements ~100x. Corrects the chance-pair scope to **277 rows in 11 assays** (not 26,691 in 6), re-runs the locus-identity measurement cleaner (gap 0.41-0.65), and explains why amplicon length is a diagnostic and not a filter. The rule: measure from `results/<run>/calls.tsv.gz` |
| [`2026-10-25-fungal-assays-diagnosed.md`](2026-10-25-fungal-assays-diagnosed.md) | plan step 1, done: the three `mgb` fungal assays are NOT broken and the "1.4%/31.8%/25.8%" framing is withdrawn - those were whole-archive rates, and the report correctly reads no-recent-data / insufficient-data on 100% baselines. The low rates were chance 32-mer windows in WGS contigs (AMFP15/1 has one contig at probe 0 mm and another at 11). Finds one thin real signal: five 2024 *B. sal* ITS amplicon deposits with perfect primers and 2-12 probe mismatches, below the drift minimum and from one lab |
| [`2026-10-25-locus-identity-design.md`](2026-10-25-locus-identity-design.md) | step 2, built and priced and **it does not work** - `locus_identity_min` ships null and must stay null, because a pan-family assay's divergent amplicon IS its success (Pan_HERPES loses 47/47 real cross-subfamily herpesviruses). Third approach that looked right and was not. Keeps the module, tests and pricing script as the basis for a lineage-aware version. Originally designed as: testing whether an amplicon is the assay's locus at all, by homology of its INTERIOR to the assay's own detecting amplicons. Covers the 155 conventional entries the chance-pair test cannot. Says what will not work and why (`pair_spans`, coordinates, the probe, `pair_evalue`), that it must live at screen time and so costs a rescreen per iteration, and the measurement that must precede any threshold |
| [`2026-10-25-chance-pairs-invent-denominators.md`](2026-10-25-chance-pairs-invent-denominators.md) | chance primer pairs make records that lack the target `EVALUABLE`, then fail them. 26,691 rows in 6 probe-bearing assays; two verdicts move, one an ACTIVE entry reading **42.2% when every genuine record detects (100%)**. Carries a same-day correction: `pair_evalue` alone is an invalid test (a 57 bp product in 99 kb legitimately scores high), so the withdrawn claim that three active ranavirus entries cross 90% is recorded there too. Names two guards a fix must not break. Maintainer decision |
| [`2026-10-25-candrian-seam.md`](2026-10-25-candrian-seam.md) | the 59-paper Candrian seam worked to the end: zero held-out rows, and why the closest call (Gerber 2007, PCR missing 4-20% of plasmid genes) does not count. Confirms the stored `Eco1` forward against an independent printed source. Literal oligo search over Europe PMC is now spent |

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
| [`2026-10-24-genbank-ceiling.md`](2026-10-24-genbank-ceiling.md) | the GenBank-availability ceiling is 11, not 9: Lotta's fusiform-lineage mitogenome was public from 2014 and the screen calls it `fail` |
| [`2026-10-24-archive-anchor.md`](2026-10-24-archive-anchor.md) | the lone-anchor test at archive scale: BH over an assay's no_amplicon rows, Bd loses 50 chance anchors and SIV Keele loses none, ships off |
| [`2026-10-24-scoring-strategy-test-plan.md`](2026-10-24-scoring-strategy-test-plan.md) | plan: a replay harness (footprint columns, `rescore.py`, frozen sets) and a pre-registered ladder of scoring candidates ending in the Bayesian C2 model |
| [`2026-10-24-scope-audit.md`](2026-10-24-scope-audit.md) | which entries are judged against organisms they were never designed for: 146 broader than species, `scope_taxids` already exists and is applied unevenly, and Helicobacter cannot reach its own reference sequence; all ten items worked through, 7 assays change status (Borna declining -> stable, Sigrist aquatic 0.0% -> 100.0%), and FOUR of the ten proposals were wrong or redundant on contact with the data -- read the closing sections before acting |
| [`2026-10-24-mpox-assay-candidates.md`](2026-10-24-mpox-assay-candidates.md) | literature pass for a modern mpox qPCR to ADD (the Kulesh 2004 N3R entry reads 58% on clade IIb): the Li 2010 G2R/C3L reference-standard trio is the top pick, with sequences; nothing applied |

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
`docs/bench-panels/panels.tsv` maps each panel to the registry entry it scores and names
its `paper`, which is the independence unit for leave-one-panel-out, and its `role`:
`fitting`, or `control` for Rahn, whose negatives are other genera and so are never a
fitting set. Measured per panel in `2026-10-23-wave2-diverged-and-patent.md`: 160 labelled
outcomes, but only 11 of the 52 negatives are within-family, which is what gates the C2
model. `docs/bench-panels/ahmed-2020-leptospira.tsv` was added 2026-10-26 and finds five published positives
scored `fail`, all on one 3'-terminal reverse mismatch.

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
| [`2026-10-24-orphan-archives.md`](2026-10-24-orphan-archives.md) | what each of the 10 orphan archive groups actually is: 636 of the 658 MB is pre-query history for taxa still covered (530 MB is *Ophidiomyces*, 90 MB *B. salamandrivorans*), one group is a genus of moths; the two 0 MB groups (the moths and Seadornavirus) were deleted 2026-10-25, the 636 MB kept |
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
| [`2026-10-18-pipeline-timekeeping-todo.md`](2026-10-18-pipeline-timekeeping-todo.md) | the timekeeping markers; all 7 shipped by 2026-10-23 |

## Derived tables and worklists

Generated or maintained TSVs. Read columns with `mlr --itsv --opprint head -n 3 FILE`.

| | |
|---|---|
| [`2026-10-26-retrospective-candidates.tsv`](2026-10-26-retrospective-candidates.tsv) | the retrospective-case reading queue from `scripts/find_retrospective_cases.py`: 220 papers that cite a registry assay's design paper AND report failure language in their abstract. **Every row is a reading assignment, not a case.** `groups` says what kind of case a row could become; `miss` and `mismatch` are the scarce `fails` kind. Triage and the four rows already read: `2026-10-26-retrospective-case-search.md` |
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
