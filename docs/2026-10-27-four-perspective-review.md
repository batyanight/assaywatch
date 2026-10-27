# Four-perspective review, and the decisions it forced

2026-10-27. The repository was read end to end from four angles — senior software
engineer, computational biologist, bench molecular diagnostics scientist, and a
newcomer following the README cold. This is the record of what was found, what
was decided, and the reasoning behind each decision, so that none of it has to be
re-derived.

Baseline at review time: 1,705 tests passing, ruff clean, 209 registry entries
valid (179 active, 29 draft, 1 deprecated; 51 with a probe), 442 commits since
2026-10-03, 2,724,036 rows in `results/2026-10-26/calls.tsv.gz`.

---

## The two findings that matter most

**1. The denominator is the central scientific problem, and it is drift-correlated.**

Of 2,724,036 screened rows, 932,965 are evaluable (34.2%) and 1,789,100 are
`no_amplicon` (65.7%). The exclusion breakdown:

| exclusion | rows | share of exclusions |
|---|---:|---:|
| `no_site` | 1,442,931 | 80.6% |
| `truncated` | 230,844 | 12.9% |
| `diverged` | 63,738 | 3.6% |
| `chance_only` | 48,518 | 2.7% |
| `no_pair` | 3,069 | 0.2% |

`no_site` is 53% of every row the pipeline produces and is not split further. It
conflates two unrelated facts: the record does not contain the target locus, and
the record contains it with primers drifted past
`scoring.max_mismatches_searched: 6`.

The bias has a mechanism. A record with ONE good primer and one drifted primer is
`diverged`, and under `count_diverged_as_fail: true` it enters the denominator as
a failure. A record with BOTH primers drifted is `no_site` and leaves entirely.
So the denominator admits singly-drifted records and silently drops
doubly-drifted ones — missingness correlated with the quantity being estimated,
in the optimistic direction, on top of the deposition bias already documented in
`config.yaml`.

Partly recoverable today and never looked at: 357,923 of the 1,442,931 `no_site`
rows DID find at least one primer site within the six-mismatch budget and were
dropped for failing `max_site_evalue: 0.01`; 1,085,008 found nothing at all.
Those 357,923 carry a recorded `anchor_evalue`, so the split needs no new data.

**2. Published artefacts described a method the code did not run.**

Fixed in `be1a712`; the reasoning is in that commit message. The pattern matters
more than the instances: the hook built to catch stale quoted counts
(`scripts/claims.py`) had been disabled since whenever three duplicate `files:`
keys landed on it, because YAML takes last-wins silently. A gate that cannot fail
is not a gate, and `check-yaml` is now in place so a duplicate key is an error.

---

## Decision: the anchor-FDR family is restricted to rows that can move

**The setting.** `drift.anchor_fdr_family`, default `lone_anchor`. The
alternative, `all_no_amplicon`, reproduces the previous behaviour.

**What the test does.** A long record gives an oligo many positions to land in.
Under a six-mismatch budget some landings are chance: the primer matches a random
stretch because the genome is long, not because the locus is present. When one
primer anchors by chance and the other finds nothing, the record is labelled
`diverged`, asserting that the site is present and has drifted — a false claim
about a record that never held the target. The worked case is Bd: 55 of 63
`diverged` records are 2014 JAM81 mRNAs with no ITS locus, anchored by the
reverse primer at five or six mismatches.

Each candidate row carries an E-value, the expected number of times an oligo this
good would land in a random record of that length and composition. It is used as
a p-value, which it approximates for E much less than 1. Benjamini-Hochberg then
sorts ascending and finds the largest rank k with p(k) <= (k/m)·q; rows at or
below that p are kept as real failures, and rows above it are relabelled
`chance_anchor` and leave the failure numerator.

**Why the family size is load-bearing.** The bar is (k/m)·q, so a larger m means
a smaller bar at every rank, so fewer anchors are kept, so MORE real failures are
relabelled as chance. The previous family included about 1.08 million `no_site`
rows. Almost none carries an E-value, so they enter as p = 1; they can never
clear the bar themselves, and the code only ever relabels `diverged`, `truncated`
and `no_pair`, so they can never move either. Their entire effect was to shrink
the bar for the rows that can.

**The principle.** A multiple-comparisons family is the set of tests among which
error is being controlled. A row with no test statistic, which can neither be
rejected nor acted on, is not a test. Including it controls nothing and only
dilutes. Note the previous family was not "every `no_amplicon` row" in any case,
since `chance_only` and `chance_pair` were already outside it — an arbitrary
middle position rather than a principled one.

**The objection considered and rejected.** Keeping only rows with an E-value is
selection, and selection can bias. But it is selection on "a test was performed",
not on the test's outcome. It would be illegitimate only if rows were dropped
according to how large their p-value was, which is not what this does.

**The honest cost.** Restricting the family makes results look WORSE, not better:
a larger bar retains more anchors as genuine failures, so more assays flag. That
direction is part of why the choice is trustworthy — it does not flatter the
tool. But the cost is real, because the `declining` flag's positive predictive
value is already 2 of 9, so additional flags may be additional false alarms. This
is why the behaviour is a config switch with its reasoning recorded, not a
hardcoded decision: the measured effect of both settings is reported, and the
choice can be reversed in one line.

**Measured effect of the previous family**, from the shipped table at q = 0.001:
12,199 rows across 121 of 195 assays were relabelled `chance_anchor` purely
because of the padding. Because the padding scales with archive size and
composition, it partly re-created the archive-size dependence that
`apply_anchor_fdr` exists to remove. Per-assay examples:

| assay | m (padded) | m (lone-anchor) | relabelled, padded | relabelled, restricted |
|---|---:|---:|---:|---:|
| `ENTEROVIRUS_ssRNA_VP3_VP1_round2` | 49,109 | 24,097 | 4,580 | 2,334 |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` | 12,462 | 3,634 | 3,367 | 1,347 |
| `CALICIVIRUS_ssRNA_RdRp_Neill_Seal_1995` | 84,784 | 806 | 790 | 375 |
| `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme` | 17,727 | 3,196 | 1,083 | 279 |

---

## Decision: the clustering safeguard is restored, and the answer is expected to be bad

`report.md` reads "2 of 14 flagged assays still hold when duplicated records are
discounted ... (57 could not be checked)" against **71** flagged assays (34
declining + 37 low coverage). So two flags are confirmed not to rest on
duplicated records, twelve of the fourteen testable flags fail the check, and 57
cannot be tested at all.

The cause is mechanical and perfectly correlated with the denominator choice.
`drift.py` sets a row's footprint to `None` when a `diverged` record is promoted
to `fail`, because such a row was never scored and carries no mismatch columns —
individually correct, since unknown is not a footprint. But the footprint count
is then made unknown for the WHOLE assay if any evaluable row lacks one, and 153
of 208 assays have at least one `diverged` row.

The system consequence was never priced: **the option that admits the most
failure evidence is the option that disables the check on whether that evidence
is clones.** The two are mutually exclusive by construction.

Decision: give a promoted `diverged` row a coarse footprint of its own, from
taxid or a title-derived organism, labelled as coarse in the output so it is not
read as a mismatch footprint, so the count stays computable and the question can
be answered for all 71.

**Expect a worse answer**, and report it as the finding rather than retuning.
Twelve of the fourteen currently testable flags already fail. `SIV Keele` sits at
0.0% of 223 records and `Pan_flavivirus_NS5_3_round1` at 19.3% of 9,476, both
`unchecked`, and SIV Keele is the assay whose anchors this project already
describes as roughly 7,000 near-identical records from one source.

---

## Decision: specificity is computed from records already on disk

Out-of-scope records are screened and then discarded with only a count printed
("20251 out-of-scope records excluded"). Their calls exist in `calls.tsv.gz` and
are never summarised, and nothing in the package computes cross-reactivity. So an
assay that predicted-detects 95% of its out-of-scope records and one that detects
0% produce identical report rows. For a registry holding pan-family consensus
assays beside species-specific TaqMans, that is the missing half of the question.

The value is already demonstrated by hand: `BPSV_dsDNA_RPO147_J6R_TaqMan_Zhao_2013`
is a BPSV-specific probe assay, exact-match clean on Orf virus, whose own scorer
calls 61 of 64 Orf virus genomes `reduced` — 95.3% predicted detection — against
a paper whose wet-lab panel shows no cross-reaction.

Gate the report on the PROBE having a site rather than the primers, because for a
genus-wide design the primers are shared deliberately and the probe carries the
specificity.

---

## Decision: the external comparison is run, in whichever direction it lands

No head-to-head against any established tool has ever been run. PCR_strainer,
TNTBLAST, openPrimeR, GoPrime, Primer Monitor, PCRv and ViralPrimer appear only
as prose in `docs/related-work.md` and the README; none is in `environment.yml`,
and `results/benchmarks/` holds Snakemake wall-clock, not accuracy.

The experiment: run thermonucleotideBLAST via `pcr-strainer` over the 179
bench-panel accessions in `docs/bench-panels/`, score the same rows with the
penalty rule, and compare the two against the published wet-lab labels with
McNemar's test — which examines only the discordant pairs, the rows where the two
predictors disagree, and asks whether the disagreements fall asymmetrically. That
pairing is what makes 179 rows informative where two independent accuracy
estimates with 20-point intervals are not, and it is why the in-sample 5/11
versus 6/11 deltas this project has been weighing are uninformative: they are
unpaired comparisons resting on about seven independent failure events.

Framing fixed in advance: TNTBLAST is a model, not ground truth. The 179 labelled
rows are the arbiter. Disagreement localises where the penalty table is wrong
rather than proving which engine is right. **If the thermodynamic engine wins,
the finding is "replace the engine, keep the registry and the longitudinal
axis", which is still the contribution** — the registry, the verified citations,
the measured amplicons and the deposit-year axis do not depend on the scoring
rule.

---

## Recorded but not acted on

> *History, as of 2026-10-27. The live list is `ROADMAP.md`, the only to-do file
> in the repository; anything below that is still open was lifted into it.*

These were found, judged real, and deliberately deferred. Each is a decision not
to act now, not an oversight.

- **Three scoring facts that should temper every reported number.** 74.7% of all
  284,062 `fail` calls sit within one 3'-window mismatch of the detect/fail
  boundary, and `primer_3prime_penalty: 3.0` exactly equals `reduced_max: 3.0`,
  so a single mismatch in the last five bases lands precisely on the class edge.
  Per-chemistry scoring ships empty, so one qPCR-grade penalty table and a global
  `terminal_mismatch_fails: true` cover 155 conventional PCRs — meaning the
  `fail` fraction on three-quarters of the registry is systematically
  pessimistic. And 26,691 `reduced` calls on probe-bearing assays carry
  mismatches in the probe itself and count as detections, 11,956 of them with
  both primers perfect; `docs/2026-10-26-s3-chemistry-switches.md` measured that
  counting those as non-detections improves catches 5/11 → 6/11 and precision
  2/9 → 3/10 with no increase in false alarms, and it still ships off.
- **A trend over deposit year is claimed and never tested.** There is no
  Cochran-Armitage test, no logistic regression on year, no rank correlation. The
  verdict is a two-window contrast against a pooled historical baseline, so an
  assay whose target had one large deposition burst in 2014 has its baseline set
  by 2014. `docs/related-work.md` claims decay "as a trend rather than as a
  single pass/fail" as contribution #2; what ships is a single pass/fail against
  a pooled comparator.
- **The lineage-conditional estimand is inoperative on the project's own
  flagship case.** `lineage.group_at_rank: species` with `sublineage: {}` means
  the influenza matrix assay is ONE lineage of 74,861 records reading 97.1%,
  while the paper `related-work.md` names as the benchmark found H3N2 carrying a
  probe-interfering mutation circulating since 2010. H1N1, H3N2 and H5N1 are all
  *Influenza A virus*. The fix is written as a commented worked example in
  `config.yaml` for this exact assay id and never populated.
- **Deposit date is not collection date**, and `collection_date` is already
  retrieved for `asm` groups and then unused. A 2025 deposit of 1990s isolates
  enters the recent window as current diversity.
- **Three silent data-integrity defects** in retrieval and the workflow, fixed in
  the phase following this commit: a short or empty efetch page accepted as a
  success and committed to the manifest; the incremental cursor keyed on the
  assay query only, so changing a length filter permanently skips older records
  that newly qualify; and `--config` overrides that move the cache key, trigger a
  full rescreen, and never reach the subprocess.
- **The registry is a primer registry, not an assay registry.** Annealing or
  cycling appears in 7 of 209 entries, LoD or efficiency in 23, master mix or
  Mg²⁺ in 2, sample matrix in 6, and one-step versus two-step RT in none. That is
  why `thermo: false` must ship: a ΔTm of −6 °C is irrelevant at Ta 50 and fatal
  at Ta 62, and the schema cannot say which. Deferred because the fix is
  re-reading papers, which is curation time.
- **Documentation is overgrown by roughly 5:1 on the axis that matters**: 85
  dated session journals totalling ~124,000 words against 10 evergreen documents
  totalling ~52,000, for ~34,000 lines of code, with a single 33,406-word file
  named as a pointer. The journals are worth keeping — several record a
  prediction that turned out wrong instead of quietly correcting it. The problem
  is that they are filed as documentation. Recommended: `docs/journal/` and about
  twelve current reference documents. Not acted on, because it is a judgement
  about the author's own research record.
