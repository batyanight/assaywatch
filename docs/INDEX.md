# docs/ index

**Nine reference documents sit in `docs/`; the 105 dated session records are in
[`journal/`](journal/README.md).** Until 2026-10-27 they were all one flat directory, so
a reader met the journals before the nine documents written to be read — a ratio of
roughly 5:1 in words on the axis that matters (~124,000 against ~52,000, for ~34,000
lines of code). Nothing was deleted and no journal lost a word.

The journals are worth keeping, which is why they were filed rather than pruned: several
record a prediction that turned out wrong instead of quietly correcting it, and that is
the most useful thing in them.

Grouped by what you want. Dated files are **session records**: what was measured on that
day and what was decided. They are not superseded by later ones unless one says so, and
the reasoning in them is usually the point.

**None of them is a to-do list.** Eight end in "Next steps" or "Still open"; each of
those sections carries a line saying it is history as of its own date. Open work lives in
ROADMAP.md at the repository root, which is the only to-do list here.

## Start here

| | |
|---|---|
| [`journal/README.md`](journal/README.md) | what the 89 dated session records are, what they are not, and why a wrong prediction is left standing in them |
| [`pipeline-architecture.md`](pipeline-architecture.md) | the DAG, stage by stage. The best single overview. |
| [`installation.md`](installation.md) | setting up the environment; better than README's Setup section |
| [`RESUME-HERE.md`](RESUME-HERE.md) | where work actually stopped, newest first |
| [`related-work.md`](related-work.md) | what else exists, and every reference the method rests on |
| [`ai-involvement.md`](ai-involvement.md) | how this repository was written, and what checks make it verifiable |
| [`journal/2026-10-27-four-perspective-review.md`](journal/2026-10-27-four-perspective-review.md) | the repo read from four angles (engineering, methods, bench, newcomer): the denominator problem, the decisions it forced and their reasoning, and what was deliberately deferred |
| [`journal/2026-10-27-c1-second-kill-test.md`](journal/2026-10-27-c1-second-kill-test.md) | `lineage.verdict_from: posterior` drives the override from the shrunk worst lineage: tier-2 identical, 0 of 240 statuses move. The hierarchical layer is measured on both halves of its plan and ships beside the verdict, not into it |
| [`journal/2026-10-27-m1-confirming-rescreen.md`](journal/2026-10-27-m1-confirming-rescreen.md) | the real screen under M1 agrees with its replay to 153 rows in 2.68M (the other 110,606 are the replay's own probe rewrite), 8 statuses move against run 3, and the hierarchical layer's first lines show intraclass correlations of 0.08-0.78: the lineages are nothing like independent, so the plan's first kill test does not fire |
| [`journal/2026-10-27-s6-kwok-premium-killed.md`](journal/2026-10-27-s6-kwok-premium-killed.md) | the other half of the Kwok table -- A:G, G:A, C:C, A:A as penalty increases -- killed on both pre-registered criteria: breaks a FAP band row, fixes nothing, adds a false alarm and no catch. The discount half ships; this half does not |
| [`journal/2026-10-27-c1-hierarchical-layer.md`](journal/2026-10-27-c1-hierarchical-layer.md) | C1's hierarchical layer built: one Beta-binomial over an assay's lineages, fitted by moments, every lineage shrunk and given a posterior, printed beside the verdict and never into it. Its kill test waits for the first run that carries it |
| [`journal/2026-10-27-live-run-and-schedule.md`](journal/2026-10-27-live-run-and-schedule.md) | the first full run under today's scoring (16 statuses move against 2026-10-26, both S3b predictions checked and one corrected), S3b confirmed on the whole table (8 call disagreements in 2.68M rows), two failed runs explained -- one self-inflicted -- and the weekly launchd job installed live for Sunday 09:00 |
| [`journal/2026-10-27-s4-m1-survives.md`](journal/2026-10-27-s4-m1-survives.md) | **M1, the G:T wobble discount retired on 2026-10-22, survives its own kill test** once `reduced` is not a detection for probes: no catch lost, the influenza case promoted to the drift flag (PPV 3/9 -> 4/10), five bench rows fixed and none broken. Priced, not proven, not shipped; the hold is the maintainer's |
| [`journal/2026-10-27-retired-taxids.md`](journal/2026-10-27-retired-taxids.md) | 18 entries move off taxids NCBI merged away, with no archive re-fetched. **The manifest was remapped, not rebuilt**: a rebuild indexes one entry per archive, 497 where the manifest holds 3,409, and the 2,910 "nothing new" runs are what carry the retrieval cursor |
| [`journal/2026-10-27-conditions-first-pass.md`](journal/2026-10-27-conditions-first-pass.md) | the first populate pass of `conditions`: 119 entries gain a protocol (47 an annealing temperature, against 7 before), proposed from 178 papers with every sentence quoted. **Five extraction bugs found by looking at the numbers, four of which pass any range check** -- a spaced-out decimal point, a decimal comma, a stock read as a final concentration |
| [`journal/2026-10-27-influenza-sublineage-enabled.md`](journal/2026-10-27-influenza-sublineage-enabled.md) | the chain is ON for the influenza matrix assay, and on the corrected numerator the subtype table inverts: **H3N2 reads 1.2% of 38,771 records and H1N1 2.6%, while thirty avian subtypes read 85-100%**. The pooled 6.5% was the two human-circulating subtypes. Tier-2 identical, 0 of 193 statuses move, so it is adopted for what it reports |
| [`journal/2026-10-27-influenza-sublineage.md`](journal/2026-10-27-influenza-sublineage.md) | the title resolver splits the influenza matrix assay into 57 subtypes: H1N2 reads 72.1% and H5N1 87.6% inside a 97% pool, H3N2 99.4% (the literature's subtype is not the one that fails here). **Exposed a defect: lineage.py still counts `reduced` as detected for probe assays**, so the lineage layer and the verdict disagree |
| [`journal/2026-10-27-window-minimum-grid.md`](journal/2026-10-27-window-minimum-grid.md) | the drift window and the record minimum priced together on the development set: the minimum does nothing to the matrix between 10 and 20 (it only trades refusals), 12 months loses a documented catch, **36 months keeps every catch and drops a false alarm**. Nothing ships; the cell a held-out read would be worth spending on is named |
| [`journal/2026-10-27-curation-measurements.md`](journal/2026-10-27-curation-measurements.md) | `orientation_inferred`: the archive yields products under the stored orientation for 26 of 28 flagged entries and zero for none; the 20 `in-text` oligos enumerated; the Hantavirus pending entries cannot be cited to Aitichou (the plan assumed they could); the 11 taxon_name mismatches split into two kinds |
| [`journal/2026-10-27-deposit-vs-collection-date.md`](journal/2026-10-27-deposit-vs-collection-date.md) | measured before building: of 1,001 dated assembly records, **a quarter were collected ten or more years before deposit** (median lag 5 years). Reaches `asm` groups only; nuccore carries no collection date without a re-fetch. Not immaterial, not built |
| [`journal/2026-10-27-c1-posterior-flag-rule.md`](journal/2026-10-27-c1-posterior-flag-rule.md) | **C1 run as its plan specified.** 1,351 lineage intervals three ways (Wilson and Jeffreys disagree on one); a posterior flag rule moves 2 of 233 statuses, both `watch` -> `low coverage` at small n, and changes nothing in tier-2. Stays `wilson`; the hierarchical layer is the part worth building |
| [`journal/2026-10-27-taxid-containment-and-merged-roots.md`](journal/2026-10-27-taxid-containment-and-merged-roots.md) | `check_taxids.py` now tests that every scoped taxon is still inside its retrieval root. Its first run reported 4,113 escapes, all false, because **18 entries carry taxids NCBI has merged away** (CDV, Nipah, the flavivirus and herpesvirus roots) — and 11 `taxon_name` mismatches nobody had looked at since 2026-10-04 |
| [`journal/2026-10-27-trend-statistic.md`](journal/2026-10-27-trend-statistic.md) | the report now runs a Cochran-Armitage trend over deposit year under each flagged assay's per-year table — beside the verdict, never into it, with no threshold. The claim `related-work.md` makes as contribution #2 finally has a statistic behind it |
| [`journal/2026-10-27-terminal-mismatch-refuted-penalty-priced.md`](journal/2026-10-27-terminal-mismatch-refuted-penalty-priced.md) | **the per-chemistry candidate this project named for three weeks is inert, and the one beside it is not.** `terminal_mismatch_fails: false` for conventional moves 0 of 179 bench rows; `primer_3prime_penalty` 3.0 -> 2.0 fixes 6 and breaks 0 (p = 0.031), moves 19,081 calls fail -> reduced, and improves the PPV of `declining` 2/9 -> 3/9 with no catch lost. Priced, not proven |
| [`journal/2026-10-27-thermo-vs-penalty-paired.md`](journal/2026-10-27-thermo-vs-penalty-paired.md) | **the first head-to-head against a physically grounded predictor, and its own correction.** A thermodynamic arm beat the penalty rule at p = 0.019 — then the register was fixed and the margin fell to p = 0.071, i.e. half of it was the mis-registration artefact this write-up predicted. What survives the fix: the penalty rule's errors are **23 false negatives against 1 false positive** |
| [`example-run-2026-10-27/report.md`](example-run-2026-10-27/report.md) | **the current committed run, under today's scoring** (probe switch, S3b and M1 live): 193 assays, 42 declining, 10 on Start here. [site-drift.md](example-run-2026-10-27/site-drift.md) beside it names the replacement base at each drifted primer position |
| [`example-run-2026-10-26/report.md`](example-run-2026-10-26/report.md) | the last run under the scoring that shipped before 2026-10-27, kept so the two can be diffed. What the tool actually produces, readable without installing anything. [site-drift.md](example-run-2026-10-26/site-drift.md) beside it names the replacement base at each drifted primer position |
| [`journal/2026-10-27-leetz-identity-confirmed.md`](journal/2026-10-27-leetz-identity-confirmed.md) | the first CONFIRMED retrospective identity (Leetz 2007 / Xiao round2) and why it reads `works` despite a 73.8% headline; two other rows closed on content. Raises where a fresh case should be written, since both the dev and held-out sets are spent |

## What the tool's output is worth

Read these before trusting a status.

| | |
|---|---|
| [`journal/2026-10-23-baseline.md`](journal/2026-10-23-baseline.md) | the frozen comparison run, the full tier-2 matrix, and the precision figure: 2 of 9 `declining` calls were real failures |
| [`journal/2026-10-04-pipeline-review.md`](journal/2026-10-04-pipeline-review.md) | the original stage-by-stage review; the estimand critique starts here |
| [`journal/2026-10-20-pipeline-audit.md`](journal/2026-10-20-pipeline-audit.md) | the later audit, with the bench-panel evidence |
| [`journal/2026-10-23-wave4-holdout.md`](journal/2026-10-23-wave4-holdout.md) | why the 49 cases are a development set, and what leave-one-out can and cannot say |
| [`validation-cases.tsv`](validation-cases.tsv) | the cases themselves (the development set) |
| [`validation-cases-heldout.tsv`](validation-cases-heldout.tsv) | 34 rows as of 2026-10-24; **spent** — read on 2026-10-26 |
| [`validation-cases-heldout-2.tsv`](validation-cases-heldout-2.tsv) | the current held-out set, opened 2026-10-27 with the first CONFIRMED retrospective identity. One row. No threshold decision may consult it |
| [`journal/2026-10-24-heldout-candidates.md`](journal/2026-10-24-heldout-candidates.md) | the first held-out sweep: 31 rows from 17 papers, and why the 5-drift-case target was missed |
| [`journal/2026-10-26-bd-phase1-site-level-measured.md`](journal/2026-10-26-bd-phase1-site-level-measured.md) | The Bd miss priced, measurement only, and **the doc corrects itself the same day**. Two findings hold: the amplicon-level rule discards **297,651 rows that carry a credible primer site** (10.9% of the table, exact from the calls table), and gapped matching explains 426 of 932,856 evaluable fails (**0.046%**), reproducing 2026-10-04's "not worth building". The third is WITHDRAWN: a Bd probe-site table (122 judgeable, 94 failing, 25 indel-explained) rested on an offset one record in three agreed with. **Bd turns out to be unmeasurable by this route** - only 3 of its 9,493 records hold all three sites and they disagree - which is the same fact as the case itself, so the assay that motivated site-level evaluation is the one whose geometry it cannot calibrate. Caught because a sibling assay read 42 of 42 failures as indel-explained where a hand check found the probe at gapped cost 0. Confirms site-level evaluation cannot be replayed: no `no_amplicon` row carries a site coordinate |
| [`journal/2026-10-26-retrospective-case-search.md`](journal/2026-10-26-retrospective-case-search.md) | A NEW instrument after the old seam and the held-out set were both spent: the CITATION GRAPH rather than oligo text, since a group using a published assay cites it and does not retype its primers. 220 candidates in `docs/2026-10-26-retrospective-candidates.tsv`. **Four read and NONE became a case.** One was circular (an in silico mismatch count, our own method); two failed on assay identity by a guess; the fourth failed on identity by a MEASUREMENT - its reverse primer is the 23-nt PREDICT form where the registry holds the 24-mer, the exact base the 2026-10-24 sweep ruled on, and the registry's own notes put that variant at 88 exact binding sites against our 215. **The finding: identity is the bottleneck, not discovery.** Confirms in passing that the P-005 pair IS the paper's first protocol, so the existing case row is correctly identified. Also refutes Furuyama 2018, carried for days as the only named drift lead: a LAMP primer paper, and the registry holds no LAMP assay |
| [`journal/2026-10-26-heldout-read-m1-rejected.md`](journal/2026-10-26-heldout-read-m1-rejected.md) | **THE HELD-OUT SET HAS BEEN READ AND IS SPENT** (2026-10-26, on the maintainer's instruction, for the one decision it was reserved for). **M1 is REJECTED**: it passes the half of its gate I pre-registered (no catch lost, 4/9 both) and fails the half I omitted, which is its own documented gate from 2026-10-21 - a `works` case newly disagrees. The drift flag's precision falls 3/4 to 1/3 and the shipped rule's PERFECT 0-of-17 false-alarm record on this set breaks. Confirmed by a real rescreen of 37,522 records, 0 call disagreements, so the false alarm is M1's and not the harness's. **And the mechanism is a finding about the drift model: a uniform loosening can MANUFACTURE a `declining` verdict** by lifting the baseline more than the recent window - M1 makes this assay's recent share BETTER, 64.9% to 67.6%, and that is what flips it. Same defect as the 2026-10-22 revert, on a case four days and one set apart |
| [`journal/2026-10-26-m1-confirming-rescreen.md`](journal/2026-10-26-m1-confirming-rescreen.md) | **M1 is PROPOSED for shipping** (branch `experiment/2026-10-26-m1-proposed`, not on main, because the held-out set has not been read). Records the confirming rescreen the decision was conditional on, and with it **the first measurement of the replay harness's one approximation**: M1 really rescreened over every tier-2 assay it moves, 514,096 rows, gives 2 call and 11 penalty disagreements against the replay - 0.0004%, and ALL of them pessimistic, because a replay is stuck re-scoring the amplicon the shipped rule chose. So every rejection in the ladder stands without qualification and the survivors are under-credited. Neither disagreement can move a verdict: both fall on one assay sitting at 97.9% of 755 records against a 90% threshold |
| [`journal/2026-10-26-s4-m1-no-longer-refuted.md`](journal/2026-10-26-s4-m1-no-longer-refuted.md) | S4, re-specified because S1 and S2 died. **M1 alone now changes ZERO rows of the 49-case tier-2 matrix**, so both halves of the gate it failed on 2026-10-22 pass, while rescuing 7 documented panel false fails (5 FAP, 2 Barrett) at no panel loss and no cost on the Rahn control. The 17 Leucocytozoon record movements reproduce EXACTLY; what changed is that the verdict is no longer near its boundary - its recent window now holds 21 records and M1 moves the interval's upper bound 50% -> 55% against a 90% threshold. Verified by a real rescreen (7,904 records, 0 replay disagreements), so not a harness artefact. **A closed decision rests on a measurement that no longer reproduces**; `docs/journal/2026-10-22-M1-tier2.md` is marked superseded in its conclusion. Also ends the ladder: four rungs, two rejected, two a maintainer decision, none shipped |
| [`journal/2026-10-26-s3-chemistry-switches.md`](journal/2026-10-26-s3-chemistry-switches.md) | S3's two per-chemistry switches, and **the chemistry axis carries signal on one side only**. The probe switch (a `reduced` probe call is not a detection) takes documented failures caught 5/11 -> 6/11 and PPV 2/9 -> 3/10 **with no increase in false alarms**, fixing the influenza Matrix-gene case it predicted - the only rung that tightens, so its extra flags are evidence rather than a loosening artefact. It fails its own kill criterion on two published positives of the Leptospira panel, both `reduced` probe calls, so it is **the first candidate that is a maintainer decision rather than a rejection**. The conventional terminal-mismatch switch is **inert**: 251 calls of 2.7 M and no verdict anywhere, which answers a ROADMAP Phase 2 claim that `terminal_mismatch_fails` inflates `fail` across the conventional majority |
| [`journal/2026-10-26-s2-smooth-decay-killed.md`](journal/2026-10-26-s2-smooth-decay-killed.md) | S2 (a smooth exponential positional decay) **passes its own pre-registered kill criterion and loses four documented catches nobody named**, including `CDV_P_gene_Scagliarini_2007` @2021-07-06, the project's ONLY drift ground-truth event. Documented failures caught 5/11 -> 1/11, PPV 2/9 -> 0/4, while false alarms IMPROVE 5/32 -> 2/32 - so total disagreements go 10 -> 11 and **an aggregate reads the candidate as neutral**. The fitted curve turns out to discount the whole 3' window (d=5 costs less than half of today), which is where drift signal lives. Lesson for the protocol: a named kill criterion is a probe and can be insensitive; the standing no-lost-catch rule is what does the work |
| [`journal/2026-10-26-s1-serial-killed.md`](journal/2026-10-26-s1-serial-killed.md) | S1 (`engine: serial`) is the first rung of the pre-registered ladder and it is **dead on its own criterion, twice over**: no threshold pair in the grid is clean on the panels, and tier-2 loses two named documented catches (both Paramyxovirinae L-gene at 2019-02-01). Three findings outlive it - **`oligo_ok_max` has no effect on panel accuracy at all**, so the panels can fit only one of its two numbers; the curve bottoms out at `oligo_weak_max: 3.0`, the value already shipped; and **Rahn reports zero cost while Forslund loses within-family negatives**, which is the argument for `role: control` turned into a measurement. Also records that netting would have read a 46% error reduction out of losing seven of ten informative negatives |
| [`journal/2026-10-26-c3-intervals-and-holdout-drift.md`](journal/2026-10-26-c3-intervals-and-holdout-drift.md) | the tier-2 matrix now carries Jeffreys credible intervals (`interval.jeffreys_interval`, pinned against the three figures `journal/2026-10-23-baseline.md` computed by hand), and every headline spans 25-50 points - so a one- or two-case delta on this set is visibly not a result. Also reports `undecided` as missing data rather than a miss, and records that `holdout.py`'s optimism has drifted from the recorded -1 to -3 |
| [`journal/2026-10-25-stale-orphan-screens.md`](journal/2026-10-25-stale-orphan-screens.md) | **read before any whole-archive measurement.** `results/screened/` keeps ORPHAN group screens that nothing rescreens - one dated 2026-10-03, before `declared_tolerance` - so globbing it reads months-old scoring rules as current. Inflated three of 2026-10-25's measurements ~100x. Corrects the chance-pair scope to **277 rows in 11 assays** (not 26,691 in 6), re-runs the locus-identity measurement cleaner (gap 0.41-0.65), and explains why amplicon length is a diagnostic and not a filter. The rule: measure from `results/<run>/calls.tsv.gz` |
| [`journal/2026-10-25-fungal-assays-diagnosed.md`](journal/2026-10-25-fungal-assays-diagnosed.md) | plan step 1, done: the three `mgb` fungal assays are NOT broken and the "1.4%/31.8%/25.8%" framing is withdrawn - those were whole-archive rates, and the report correctly reads no-recent-data / insufficient-data on 100% baselines. The low rates were chance 32-mer windows in WGS contigs (AMFP15/1 has one contig at probe 0 mm and another at 11). Finds one thin real signal: five 2024 *B. sal* ITS amplicon deposits with perfect primers and 2-12 probe mismatches, below the drift minimum and from one lab |
| [`journal/2026-10-25-locus-identity-design.md`](journal/2026-10-25-locus-identity-design.md) | step 2, built and priced and **it does not work** - `locus_identity_min` ships null and must stay null, because a pan-family assay's divergent amplicon IS its success (Pan_HERPES loses 47/47 real cross-subfamily herpesviruses). Third approach that looked right and was not. Keeps the module, tests and pricing script as the basis for a lineage-aware version. Originally designed as: testing whether an amplicon is the assay's locus at all, by homology of its INTERIOR to the assay's own detecting amplicons. Covers the 155 conventional entries the chance-pair test cannot. Says what will not work and why (`pair_spans`, coordinates, the probe, `pair_evalue`), that it must live at screen time and so costs a rescreen per iteration, and the measurement that must precede any threshold |
| [`journal/2026-10-25-chance-pairs-invent-denominators.md`](journal/2026-10-25-chance-pairs-invent-denominators.md) | chance primer pairs make records that lack the target `EVALUABLE`, then fail them. 26,691 rows in 6 probe-bearing assays; two verdicts move, one an ACTIVE entry reading **42.2% when every genuine record detects (100%)**. Carries a same-day correction: `pair_evalue` alone is an invalid test (a 57 bp product in 99 kb legitimately scores high), so the withdrawn claim that three active ranavirus entries cross 90% is recorded there too. Names two guards a fix must not break. Maintainer decision |
| [`journal/2026-10-25-candrian-seam.md`](journal/2026-10-25-candrian-seam.md) | the 59-paper Candrian seam worked to the end: zero held-out rows, and why the closest call (Gerber 2007, PCR missing 4-20% of plasmid genes) does not count. Confirms the stored `Eco1` forward against an independent printed source. Literal oligo search over Europe PMC is now spent |

## The 2026-10-23 plan of attack, in order

| | |
|---|---|
| [`journal/2026-10-23-wave1-report-honesty.md`](journal/2026-10-23-wave1-report-honesty.md) | 704 of 1,512 lineage intervals were zero-width; 19 assays held a status their entry denies |
| [`journal/2026-10-23-wave2-diverged-and-patent.md`](journal/2026-10-23-wave2-diverged-and-patent.md) | `count_diverged_as_fail` tested and kept off; patent records excluded on mechanism |
| [`journal/2026-10-23-wave3-bd-miss.md`](journal/2026-10-23-wave3-bd-miss.md) | the Bd failure: probe sites deposited by 2013 and discarded twice |
| [`journal/2026-10-23-wave3-usutu.md`](journal/2026-10-23-wave3-usutu.md) | a false alarm traced to the flat 3' penalty window |
| [`journal/2026-10-23-wave3-influenza.md`](journal/2026-10-23-wave3-influenza.md) | the miss is `reduced` counting as detected for a probe assay |
| [`journal/2026-10-23-wave3-holm.md`](journal/2026-10-23-wave3-holm.md) | Holm replaces BH, and moves nothing yet |
| [`journal/2026-10-23-wave5-config-schema.md`](journal/2026-10-23-wave5-config-schema.md) | `config.yaml` gets a schema; six defaults lose their second home |
| [`journal/2026-10-23-wave5-triage.md`](journal/2026-10-23-wave5-triage.md) | the report leads with ten assays; anchors instead of JavaScript |
| [`journal/2026-10-23-wave5-what-active-means.md`](journal/2026-10-23-wave5-what-active-means.md) | 173 drafts are eligible, 100 carry no oligo doubt. A maintainer decision |
| [`journal/2026-10-23-wave5-engineering.md`](journal/2026-10-23-wave5-engineering.md) | the memory hazard, and the two refactors deliberately not done |
| [`journal/2026-10-23-oligo-adjudication.md`](journal/2026-10-23-oligo-adjudication.md) | every `near:` and `absent` oligo read against its paper, then screened: 2 corrections kept, 2 reverted because they destroyed a working assay, agreement 84% -> 90% |
| [`journal/2026-10-23-verified-doi-gate.md`](journal/2026-10-23-verified-doi-gate.md) | only verified-DOI assays are live; 10 moved to `pending/`; the seed list's fields and importer removed |
| [`journal/2026-10-23-wave5-elsevier-and-oligo-flags.md`](journal/2026-10-23-wave5-elsevier-and-oligo-flags.md) | the Elsevier block opened: 68 oligos newly checkable; 6 of 21 near-misses are the matcher finding sibling primers |
| [`bayesian-scoring-plan.md`](bayesian-scoring-plan.md) | design only: the three things "Bayesian scoring" could mean, with a kill-test each |
| [`journal/2026-10-24-genbank-ceiling.md`](journal/2026-10-24-genbank-ceiling.md) | the GenBank-availability ceiling is 11, not 9: Lotta's fusiform-lineage mitogenome was public from 2014 and the screen calls it `fail` |
| [`journal/2026-10-24-archive-anchor.md`](journal/2026-10-24-archive-anchor.md) | the lone-anchor test at archive scale: BH over an assay's no_amplicon rows, Bd loses 50 chance anchors and SIV Keele loses none, ships off |
| [`journal/2026-10-24-scoring-strategy-test-plan.md`](journal/2026-10-24-scoring-strategy-test-plan.md) | plan: a replay harness (footprint columns, `rescore.py`, frozen sets) and a pre-registered ladder of scoring candidates ending in the Bayesian C2 model |
| [`journal/2026-10-24-scope-audit.md`](journal/2026-10-24-scope-audit.md) | which entries are judged against organisms they were never designed for: 146 broader than species, `scope_taxids` already exists and is applied unevenly, and Helicobacter cannot reach its own reference sequence; all ten items worked through, 7 assays change status (Borna declining -> stable, Sigrist aquatic 0.0% -> 100.0%), and FOUR of the ten proposals were wrong or redundant on contact with the data -- read the closing sections before acting |
| [`journal/2026-10-24-mpox-assay-candidates.md`](journal/2026-10-24-mpox-assay-candidates.md) | literature pass for a modern mpox qPCR to ADD (the Kulesh 2004 N3R entry reads 58% on clade IIb): the Li 2010 G2R/C3L reference-standard trio is the top pick, with sequences; nothing applied |

## Design documents, agreed before the code

| | |
|---|---|
| [`journal/2026-10-17-estimand-plan.md`](journal/2026-10-17-estimand-plan.md) | the lineage-conditional estimand, with its own falsifiable prediction |
| [`journal/2026-10-19-subtaxid-resolution.md`](journal/2026-10-19-subtaxid-resolution.md) | grouping below the taxid: subtype, title, sequence cluster |
| [`journal/2026-10-19-lineage-detected-definition.md`](journal/2026-10-19-lineage-detected-definition.md) | what "detected" means per lineage |
| [`journal/2026-10-19-scope-ancestry.md`](journal/2026-10-19-scope-ancestry.md) | scope by taxonomy ancestry rather than exact taxid |

## Calibration and threshold decisions

| | |
|---|---|
| [`journal/2026-10-21-drift-window-calibration.md`](journal/2026-10-21-drift-window-calibration.md) | the window/minimum grid, and why the grid optimum was overruled |
| [`journal/2026-10-18-recalibration.md`](journal/2026-10-18-recalibration.md) | an earlier recalibration pass |
| [`journal/2026-10-21-M1-identity-aware-penalty.md`](journal/2026-10-21-M1-identity-aware-penalty.md) | the mispair-identity candidate |
| [`journal/2026-10-21-M1-shipped.md`](journal/2026-10-21-M1-shipped.md) | M1 shipping |
| [`journal/2026-10-22-M1-tier2.md`](journal/2026-10-22-M1-tier2.md) | M1 reverted: it lost a documented catch. The confusion matrix of record |
| [`journal/2026-10-21-M2-step0-killtest.md`](journal/2026-10-21-M2-step0-killtest.md) | M2 killed at step 0: NN ΔG inverts Kwok's ordering |
| [`journal/2026-10-19-conventional-override-validation.md`](journal/2026-10-19-conventional-override-validation.md) | the per-chemistry override, tried and reverted |
| [`journal/2026-10-19-pan-family-cases.md`](journal/2026-10-19-pan-family-cases.md), [`journal/2026-10-20-pan-family-override.md`](journal/2026-10-20-pan-family-override.md) | pan-family assays and the lineage override |
| [`journal/2026-10-19-orthopox-ati-vaccinia.md`](journal/2026-10-19-orthopox-ati-vaccinia.md) | the hand-checked false positive that patent records caused |

## Bench panels: the only truth below the assay level

`docs/bench-panels/*.tsv` with a header comment recording what was read and from where.
`docs/bench-panels/panels.tsv` maps each panel to the registry entry it scores and names
its `paper`, which is the independence unit for leave-one-panel-out, and its `role`:
`fitting`, or `control` for Rahn, whose negatives are other genera and so are never a
fitting set. Measured per panel in `journal/2026-10-23-wave2-diverged-and-patent.md`: 160 labelled
outcomes, but only 11 of the 52 negatives are within-family, which is what gates the C2
model. `docs/bench-panels/ahmed-2020-leptospira.tsv` was added 2026-10-26 and finds five published positives
scored `fail`, all on one 3'-terminal reverse mismatch.

[`journal/2026-10-19-fap-bench-panel.md`](journal/2026-10-19-fap-bench-panel.md) ·
[`journal/2026-10-20-meyer-ati-bench-panel.md`](journal/2026-10-20-meyer-ati-bench-panel.md) ·
[`journal/2026-10-20-mycoplasma-bench-panel.md`](journal/2026-10-20-mycoplasma-bench-panel.md) ·
[`journal/2026-10-20-rahn-invA-bench-panel.md`](journal/2026-10-20-rahn-invA-bench-panel.md)

## Registry provenance and curation

| | |
|---|---|
| [`journal/2026-10-05-hallucination-audit.md`](journal/2026-10-05-hallucination-audit.md) | the repo-wide audit for fabricated content, and the gates that followed |
| [`journal/2026-10-04-provenance-audit.md`](journal/2026-10-04-provenance-audit.md) | where each entry's oligos came from |
| [`journal/2026-10-05-sequence-provenance-sweep.md`](journal/2026-10-05-sequence-provenance-sweep.md), [`journal/2026-10-05-sequence-verification.md`](journal/2026-10-05-sequence-verification.md) | sequence verification passes |
| [`journal/2026-10-21-predict-primer-provenance.md`](journal/2026-10-21-predict-primer-provenance.md) | the PREDICT panel's provenance |
| [`journal/2026-10-20-scope-curation.md`](journal/2026-10-20-scope-curation.md), [`journal/2026-10-17-flagged-decisions.md`](journal/2026-10-17-flagged-decisions.md) | per-entry curation decisions |
| [`journal/2026-10-14-amplicon-sizes-measured.md`](journal/2026-10-14-amplicon-sizes-measured.md) | amplicon sizes measured rather than quoted |
| [`journal/2026-10-19-taxid-artefacts.md`](journal/2026-10-19-taxid-artefacts.md), [`journal/2026-10-19-subtaxid-resolution.md`](journal/2026-10-19-subtaxid-resolution.md) | taxonomy artefacts |
| [`journal/2026-10-24-orphan-archives.md`](journal/2026-10-24-orphan-archives.md) | what each of the 10 orphan archive groups actually is: 636 of the 658 MB is pre-query history for taxa still covered (530 MB is *Ophidiomyces*, 90 MB *B. salamandrivorans*), one group is a genus of moths; the two 0 MB groups (the moths and Seadornavirus) were deleted 2026-10-25, the 636 MB kept |
| [`papers-index.md`](papers-index.md) | the durable record of which papers the registry rests on (`papers/` is gitignored) |
| [`journal/2026-10-05-papers-needed.md`](journal/2026-10-05-papers-needed.md), [`journal/2026-10-05-doi-candidates.md`](journal/2026-10-05-doi-candidates.md) | what still needs reading |
| [`journal/2026-10-06-lab-leads.md`](journal/2026-10-06-lab-leads.md) | 188 unworked leads, with an explicit account of how far to trust them |

## First runs and early findings

[`journal/2026-10-04-first-run-review.md`](journal/2026-10-04-first-run-review.md) ·
[`journal/2026-10-04-assay-investigations.md`](journal/2026-10-04-assay-investigations.md) ·
[`journal/2026-10-04-literature-audit.md`](journal/2026-10-04-literature-audit.md) ·
[`journal/2026-10-05-amplicon-audit.md`](journal/2026-10-05-amplicon-audit.md) ·
[`journal/2026-10-06-research-findings.md`](journal/2026-10-06-research-findings.md) ·
[`journal/2026-10-05-cloud-session-findings.md`](journal/2026-10-05-cloud-session-findings.md)

## Superseded

Kept because the reasoning is still the record, but do not act on them.

| | superseded by |
|---|---|
| `journal/HANDOFF-2026-10-18.md`, `journal/2026-10-18-phase1-complete.md`, `journal/2026-10-18-phase2-handoff.md`, `journal/2026-10-18-session-summary.md` | four documents for one day with no stated precedence. `RESUME-HERE.md` is the live one |
| [`journal/2026-10-22-lineage-plan-salvage.md`](journal/2026-10-22-lineage-plan-salvage.md) | what was kept from the closed PR #3 |
| [`journal/2026-10-05-verification-handoff.md`](journal/2026-10-05-verification-handoff.md), [`journal/2026-10-05-list2-worklist.md`](journal/2026-10-05-list2-worklist.md) | worklists from completed passes |
| [`journal/2026-10-18-pipeline-timekeeping-todo.md`](journal/2026-10-18-pipeline-timekeeping-todo.md) | the timekeeping markers; all 7 shipped by 2026-10-23 |

## Derived tables and worklists

Generated or maintained TSVs. Read columns with `mlr --itsv --opprint head -n 3 FILE`.

| | |
|---|---|
| [`2026-10-27-conditions-proposals.tsv`](2026-10-27-conditions-proposals.tsv) | every thermal-protocol value `scripts/extract_conditions.py` found in the 178 papers on disk, with the sentence it came from quoted beside it: 644 proposals over 211 entries. 292 of them (the values the paper states once, labelled by the paper itself, no nested round) were applied to 119 registry entries; the rest are the reader's. `papers/` is gitignored, so this file is the record of what was read |
| [`2026-10-27-in-text-oligos.tsv`](2026-10-27-in-text-oligos.tsv) | the 20 oligos whose stored sequence occurs in the cited paper's text but in no table the extractor could parse — enumerated for the first time 2026-10-27; each needs one human read of one page, and none changes a sequence |
| [`2026-10-26-retrospective-candidates.tsv`](2026-10-26-retrospective-candidates.tsv) | the retrospective-case reading queue from `scripts/find_retrospective_cases.py`: 220 papers that cite a registry assay's design paper AND report failure language in their abstract. **Every row is a reading assignment, not a case.** `groups` says what kind of case a row could become; `miss` and `mismatch` are the scarce `fails` kind. Triage and the four rows already read: `journal/2026-10-26-retrospective-case-search.md` |
| [`assay-master-sheet.tsv`](assay-master-sheet.tsv), [`assay-master-sheet.md`](assay-master-sheet.md) | one row per assay, generated by `scripts/master_sheet.py` |
| [`oligos-without-doi.tsv`](oligos-without-doi.tsv) | the 33 oligos with no citable source, grouped by where the answer must come from. The `unpublished` group is in `pending/` until a paper turns up |
| [`design-era.tsv`](design-era.tsv) | how much sequence has arrived since each assay was designed, by `scripts/design_era.py`. 71 of 193 assays were designed when their taxon held fewer than 50 archived records |
| [`rename-mapping.tsv`](rename-mapping.tsv) | assay-id renames and removals, so an old calls table still matches |
| [`predict-supplement-verification.tsv`](predict-supplement-verification.tsv) | PREDICT oligos against the published supplements |
| [`needs-review-migration.tsv`](needs-review-migration.tsv) | the one-off migration to the controlled review vocabulary |
| [`2026-10-06-lab-leads.tsv`](2026-10-06-lab-leads.tsv) | the 188 leads behind `journal/2026-10-06-lab-leads.md` |
| [`2026-10-05-pmc-abstract-only.tsv`](2026-10-05-pmc-abstract-only.tsv) | papers where only an abstract was reachable |

## Narrower records

| | |
|---|---|
| [`journal/2026-10-17-nested-family-key.md`](journal/2026-10-17-nested-family-key.md) | how nested rounds are paired into families |
| [`journal/2026-10-20-tier2-rename-resolution.md`](journal/2026-10-20-tier2-rename-resolution.md) | why a validation case must never match nothing silently |
| [`journal/2026-10-22-supplements-and-three-citations.md`](journal/2026-10-22-supplements-and-three-citations.md) | a supplement in `papers/` that the verifier could not see |
| [`journal/2026-10-22-unsigned-screens-cleared.md`](journal/2026-10-22-unsigned-screens-cleared.md) | 20 screens with no signature record, and the file that fixed it |
