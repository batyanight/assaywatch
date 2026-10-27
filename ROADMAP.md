# Roadmap

**This is the only to-do list in the repository.** If work is open, it is in
`## Open work` below. Nothing else is authoritative:

- `docs/RESUME-HERE.md` says where the last session stopped and what it found. It
  no longer carries a list of its own.
- `docs/YYYY-MM-DD-*.md` are session records. Several end in "Next steps" or
  "Still open"; those were true on the date in the filename and are kept as
  history, not as a queue. Anything in them that is still live has been lifted
  into this file, with a pointer back.
- `papers/papers-fetch-list.md` is the one exception, and it is a fetch queue
  rather than a work list: PDFs that need a human and a proxy. The work those
  PDFs unblock is tier-2 validation, below.

New ideas go here, not into the sprint. Scope for v0.1 is frozen in the build plan.

---

# Open work

## Waiting on a maintainer, minutes each

- **The contributor promise.** `CONTRIBUTING.md` ships without the two-week
  review commitment that was planned for it. That is a promise about your own
  time, so it is yours to make or drop.
- **The two Priority 1 decisions of 2026-10-27 are taken** and are recorded in
  `## Done`: the Leetz case opened a new held-out set, and TNTBLAST waits until
  someone installs Rosetta 2, builds it for arm64, or runs it on the cluster.

## Shipped today, and what it still owes

- **S5 is live: `by_chemistry.conventional.primer_3prime_penalty: 2.0`** (2026-10-27).
  `strategies/s5-conventional-3prime-penalty.yaml` drops `primer_3prime_penalty`
  from 3.0 to 2.0 for `conventional` only. It is **priced, not proven**
  (`docs/journal/2026-10-27-terminal-mismatch-refuted-penalty-priced.md`):

  - bench panels: fixes 6 of 179 rows, breaks 0, McNemar exact p = 0.0312, and
    none of the 16 negatives that can punish a loosening moves. Nothing is fitted,
    so that is not an in-sample figure;
  - registry replay over 2.72M rows: 19,081 calls move, every one `fail` ->
    `reduced`; documented failures caught stays 6/11; the PPV of `declining` goes
    2/9 -> 3/9 and false alarms 5/32 -> 4/32, because exactly two tier-2 cases move
    and they move in opposite directions on purpose.

  Both pre-registered kill criteria survived, and the confirming rescreen covered
  **6 of the 84 affected assays, 280,818 rows, 0 call disagreements**, i.e. 14,261 of
  the 19,081 moved calls (74.7%) including both assays that carry a verdict move. The
  91 penalty differences all run pessimistic — the real screen finds a better
  candidate than a replay can see.

  **What it still owes, now that it is live:**

  - **The next full pipeline run has not happened yet.** Every number in the
    committed report predates this change, and the scoring config is part of the
    cache key, so the next `snakemake` rescreens. Expect the 13 statuses the probe
    switch moved and whatever S5 moves on top; the two verdicts measured here are
    `Pan_flavivirus_NS5_3_round2` (a false alarm dropped) and the Forslund FAP case
    (`low coverage` -> `declining`).
  - **78 small movers were never rescreened** — 4,820 calls between them, at most
    395 each, so none can move a verdict alone. Still not the same as having checked.
  - **2.0 is coarser than the evidence deserves.** Kwok 1990 and Stadhouders 2010
    both report that the cost of a mismatch depends on its IDENTITY, which
    `scoring.mispair_penalty` can express per pair and a single positional number
    cannot. 2.5 was priced on the same rows and fixes only 2 of the 6.

  **Why this item no longer names `terminal_mismatch_fails`.** For three weeks it
  did, and the 23 false negatives against 1 false positive were read as its
  evidence. Scored directly, exempting conventional chemistry from it moves **0 of
  179 bench rows** — the same answer the 2026-10-26 registry-wide measurement gave
  from the other end (251 calls of 2.7M, no verdict changed), because a record whose
  primer carries a terminal mismatch almost always carries others that already
  exceed `reduced_max`. The pessimism is real; that knob is not where it lives.

  **The threshold coincidence is why the penalty is the live suspect.**
  `primer_3prime_penalty: 3.0` equals `reduced_max: 3.0`, so one mismatch anywhere
  in the last five bases lands precisely on the detect/fail boundary — and 74.7% of
  all 284,062 `fail` calls sit within one 3'-window mismatch of it (2026-10-27 run).

  **One figure from this item's history must not be quoted.**
  `CALICIVIRUS_ssRNA_Helicase_Reid_1999` was read as carrying a 3'-terminal
  mismatch in Hel1 against all 16 of its own target records, and
  `terminal_mismatch_fails` alone was said to drive it to near-total failure
  against a paper reporting the assay working. That mismatch was an error in our
  stored copy of the oligo, not a chemistry effect. The 2026-10-24 correction of
  Hel1's 3'-terminal base from G to C — the form the template carries in all 16
  design targets, and the only form that reproduces the published 357 bp product
  — removed it. **Do not quote "0 of 30".**

## Method debts

- **A trend over deposit year is claimed and never tested.** No
  Cochran-Armitage, no logistic regression on year, no rank correlation. The
  verdict is a two-window contrast against a pooled historical baseline, so an
  assay whose target had one large deposition burst in 2014 has its baseline set
  by 2014. `docs/related-work.md` claims decay "as a trend rather than as a
  single pass/fail" as contribution #2; what ships is a single pass/fail against
  a pooled comparator.

- **The drift rules interact and are untested.** `recent_window_months: 24`
  with `min_records_for_drift: 20` is why Bd (Boyle 2004) read "insufficient
  data" at 100% detected on 17 recent records: shorten the window and assays
  fall below the minimum, lengthen it and real change is diluted. Validation has
  to set the pair together, not each alone. `max_window_months: 60` widens the
  window per assay when it holds too few records, which treats the symptom.

- **`drift.anchor_fdr`'s value has no evidence behind it.** 0.05 and 0.01
  differ by a factor of two in rows moved (7,206 against 13,693; 2026-10-24
  run), 0.001 is what ships, and tier-2 separates them on one row. The choice
  wants the bench panels or a held-out set. `docs/journal/2026-10-24-archive-anchor.md`.

- **Deposit date is not collection date.** `collection_date` is already
  retrieved for `asm` groups and then unused, so a 2025 deposit of 1990s
  isolates enters the recent window as current diversity. The data is on disk;
  this is the same shape as the specificity fix, which took a day.

- **Populate `lineage.sublineage` for the segmented RNA viruses.**
  `lineage.group_at_rank: species` with `sublineage: {}` means the influenza
  matrix assay is one lineage of 74,861 records reading stable at 97.1%
  (2026-10-26 run), while the paper `docs/related-work.md` names as the
  benchmark found H3N2 carrying a probe-interfering mutation circulating since
  2010. H1N1, H3N2 and H5N1 are all *Influenza A virus*. The fix is written as a
  commented worked example in `config.yaml` for this exact assay id and never
  populated. The resolver chain it needs already exists
  (`lineage.build_resolvers`, including homology clusters via
  `assaywatch.subcluster`).

- **`target.exclusivity_taxids`, plus retrieval for it.** `scope_taxids`
  already excludes out-of-scope records from the drift denominator and the
  report computes specificity from the out-of-scope calls that happen to be on
  disk (18 assays, 2026-10-27). What is missing is fetching a near-neighbour an
  assay explicitly claims to exclude: BPSV cannot be tested for specificity at
  all today, because nothing retrieves the neighbour.

## Validation, which sets every threshold above

- **Tier 2: retrospective validation.** Assemble assays with published
  follow-up — a paper, erratum or redesign reporting the assay failing on
  particular lineages, or reporting it still working — and ask whether
  AssayWatch flags what the literature found, using only records deposited
  before that paper. That gives a confusion matrix, and the thresholds become
  whatever optimises it rather than whatever looked sensible. **Every number in
  `config.yaml` is a placeholder set by eye**, so until this exists the
  statuses read as "worth looking at", not as measurements. It is also the
  paper's main figure.

  **The binding constraint is identity, not discovery**, and it is measured:
  `scripts/check_candidate_identity.py` ran over all 9 `mismatch`/`redesign`
  rows — the queue's concentrated signal — and open-access text settles none of
  them (`results/retro-identity-concentrated-2026-10-26.tsv`). Re-run with the
  PDFs that have arrived since, 2026-10-27: **1 CONFIRMED, 1 VARIANT, 11
  UNCONFIRMABLE**, of which 6 wait on a PDF, 1 on a persistent Europe PMC HTTP
  500 (PMC2546769), and 4 are closed on CONTENT — the paper simply does not
  print our oligos, so no document will settle them. The one CONFIRMED row
  opened `docs/validation-cases-heldout-2.tsv` on 2026-10-27.

  The next rows therefore need the 6 queued PDFs, not more searching. The
  identity script prefers a local file, so a PDF dropped into `papers/` is
  picked up on re-run — and a file being present is not the same as being
  readable: the Neill & Seal copy on disk yields no sequence at all
  (`papers/papers-fetch-list.md`).

## Data and curation

- **889 lineages are still `taxid_<n>`** (2026-10-23 run).
  `name_lineages_from_taxonomy` names only what the taxonomy cache holds; the
  rest need `scripts/build_taxonomy_cache.py` rerun or an NCBI lookup. A data
  task, not a code one.

- **The registry is a primer registry, not an assay registry.** Annealing or
  cycling appears in 7 of 209 entries, LoD or efficiency in 23, master mix or
  Mg²⁺ in 2, sample matrix in 6, and one-step versus two-step RT in none
  (2026-10-27). That is why `thermo: false` must ship: a ΔTm of −6 °C is
  irrelevant at Ta 50 and fatal at Ta 62, and the schema cannot say which. Fix
  shape: `conditions` / `format` / `performance` / `panels` blocks. Deferred
  because the fix is re-reading papers, which is curation time.

- **Registry coverage.** Audit the PREDICT consensus-PCR panel for gaps, and
  add assays in current wildlife-lab use that PREDICT never covered — fungal,
  bacterial and parasitic targets especially. Sequences only from a source that
  can be read and cited, never transcribed from a secondary list.

- **A genus taxid can stop containing its target.** *Mycoplasmopsis agassizii*
  and *Mycoplasmoides testudinis* both left genus *Mycoplasma*, so a
  genus-rooted retrieval silently stops fetching the organism the assay names.
  `scripts/check_taxids.py` cannot see this; it needs a check that every named
  target organism is still inside its assay's retrieval root. Cheap, and
  silently wrong today.

- **Four leftovers from the oligo adjudication** (`docs/journal/2026-10-23-oligo-adjudication.md`),
  none of them blocking: the 20 `in-text` rows, where a sequence occurs in the
  paper but in no listed oligo and may have been found inside a printed target
  rather than a primer table, never enumerated;
  `BORNA_VIRUS_N_gene_Zimmermann_1994_round2`, which reads 0% by construction
  because storing the measured form would mean storing a sequence no paper
  prints; whether `CALICIVIRUS_ssRNA_Helicase_Reid_1999` should be re-cited to
  Neill & Seal 1995 once that PDF arrives (see tier-2 validation); and
  `ORTHOBORNAVIRUS_XP_aquatic_Sigrist_2021`, which stores its reporter as
  "Alexa 647N" where Figure 2C labels the probe A647N, the conventional short
  form of Atto 647N — not screened, not changed, recorded.

  The lesson from that session is worth keeping: "the paper wins" is the right
  default for a *sequence* and the wrong default for a *correction*. Two of
  four changes the printed evidence supported would have destroyed a working
  assay, and only screening caught it. Any future oligo correction should be
  screened against its own archive before it is committed, with the
  before/after detected share reported.

## Hygiene

- **Documentation is overgrown by roughly 5:1 on the axis that matters**: 85
  dated session journals totalling ~124,000 words against 10 evergreen
  documents totalling ~52,000, for ~34,000 lines of code (2026-10-27). The
  journals are worth keeping — several record a prediction that turned out
  wrong instead of quietly correcting it. The problem is that they are filed as
  documentation. Shape: `docs/journal/` and about twelve current reference
  documents. Not acted on, because it is a judgement about your own research
  record.

- **Report triage, not report correctness.** Two groups should not lead the
  report: the `declining` rows whose note ends "a coverage gap, not drift", and
  the degeneracy-severe assays. Neither is a wrong status — the first are sound
  pooled calls whose note describes a lineage, and degeneracy is reported
  beside a verdict and never folded into one. `Start here` now orders 10 assays
  (2026-10-27) and is the mechanism this would use.

- **A SLURM profile aimed at Greene.** `profiles/slurm/` runs the same rules on
  SLURM generically; nothing in it is tuned to NYU's partitions, QoS or module
  stack.

## Known limitations, recorded and not work

- **Majority contamination.** `ENTEROVIRUS_ssRNA_VP3_VP1_round2` cannot be
  addressed by the archive-anchor mechanism by construction
  (`docs/journal/2026-10-24-archive-anchor.md`).
- **The denominator is drift-correlated.** A record with one drifted primer
  counts as a failure; a record with both drifted leaves the denominator as
  `no_site`. 65.7% of 2.72M rows never reach the statistics, and `no_site` alone
  is 53% of every row — 357,923 of which did find a site within the mismatch
  budget and 1,085,008 of which found nothing (2026-10-27 run). The split is
  measured and printed per assay; the bias itself is not fixed, and may not be
  fixable without a different estimand.
- **Records are not independent.** The duplication check removes the duplication
  it can see (identical footprints); clade structure beyond that is unaddressed,
  so the footprint count is not a lower bound on the effective sample size.
- **ARTIC-style tiled schemes** are out of scope (2026-10-04): they would need a
  scheme object of many amplicons reporting dropout rather than one assay per
  pair, and quick-lab/primerschemes is CC BY-SA 4.0, which the registry licence
  would have to accommodate.

---

# The placeholders, for the record

`scoring` (3'/mid/5' primer penalties 3.0 / 1.0 / 0.5 over windows of 5, probe
centre/outer 2.0 / 1.0, `detect_max` 1.0, `reduced_max` 3.0,
`terminal_mismatch_fails` true, `max_ambiguous_per_oligo` 2,
`max_mismatches_searched` 6, `max_pair_evalue` 0.01); `drift`
(`detect_fraction_threshold` 0.90, `recent_window_months` 24,
`min_records_for_drift` 20, `min_records_for_coverage` 10, `min_decline` 0.05);
`degeneracy.tiers` (8 / 128 / 4096); `assemblies.per_year` 20.

One of those is no longer only eyeballed. `drift.min_decline` 0.05 has regulatory
precedent: FDA's *Policy for Evaluating Impact of Viral Mutations on COVID-19 Tests
(Revised)* (January 2023, docket FDA-2020-D-0987) tells molecular test developers to
align their primer/probe sequences against public genome databases periodically and to
act when mutations "reduce performance by 5% or more from the previously established
performance". A regulator arrived at the same floor independently, so the number is
defensible even though this project did not derive it. Two caveats are recorded beside
the setting in `config.yaml`: the policy is tied to the section 564 COVID-19
declaration, and its 5% is not stated as points or relative, where ours is percentage
points of detected share.

---

# Done

## Phase 0
- [x] repo, environment.yml, pre-commit, CI
- [x] YAML schema (pydantic) and validator
- [x] registry seeded from a primer list and curated against the literature (host/barcoding/universal primers excluded as out of scope)
- [x] 5 assays promoted to `active`: Bd (Boyle 2004) done 2026-10-04 (stable, 100% of 54 recent);
      Bsal (Blooi 2013) and Oo ITS2 (Bohuski 2015) await their rDNA-query data; ranavirus MCP
      (Pallister 2007) and CDV P (Scagliarini 2007) were "watch" at ~88%.
      Satisfied; ticked 2026-10-26 after confirming all of them, plus Oo IGS and the
      Pallister intergenic pair, read `status: active`. The rDNA-query data arrived and the
      two "watch" assays were promoted on their own evidence, so the wording above is the
      state this item was WRITTEN in, not the state it closed in
- [x] run `scripts/resolve_citations.py` once (2026-10-04): 64 DOIs verified, 21 taxids filled;
      5 BAD DOIs left for review. `scripts/check_taxids.py` found and fixed 3 wrong taxids
- [x] name, license (MIT code / CC-BY registry)
- [x] only assays with a verified DOI are live; the rest wait in `pending/` (2026-10-23)

## Phase 1: core pipeline
- [x] `match`: exhaustive vectorised search, both strands, held to brute force in tests
- [x] `score`: position-weighted penalty from config.yaml, five-way call per record
- [x] three-state base comparison: degeneracy and undetermined record bases cost nothing
- [x] inosine handled as a single promiscuous molecule, not as N
- [x] degeneracy accounting reported next to the drift signal, never scored
- [x] `screen` CLI: assays x FASTA -> TSV of calls
- [x] synthetic fixture set with hand-derived expected calls (61 records, 5 assays)
- [x] `retrieve`: Entrez esearch/esummary/efetch per taxid, mdat-filtered, gzip archive + manifest
- [x] wire the stages into a Snakefile with a checkpoint; SLURM profile
- [x] first live NCBI dry run (2026-10-03): 28 taxa fetchable whole, 19 needed gene-targeted queries
- [x] first live fetch (2026-10-03): 25 taxa, ~470k records, 1.1 GB; fixed dropped connections on genome-sized pages and expired history handles
- [x] gene-targeted retrieval groups; per-group screening
- [x] dry-run the gene-targeted groups; WGS contigs excluded for bacteria; influenza opted in
- [x] first full pipeline run (2026-10-03/04): N-gaps in scaffolds made pairing cubic; fixed
- [x] manifest is state, not a Snakemake output (it was being deleted each run); atomic writes;
      archives never overwritten; `scripts/rebuild_manifest.py`
- [x] cumulative reports from cached per-archive screens
- [x] screen large archives across cores (`screen --workers`, byte-identical output); biggest archives first
- [x] `drift`: Wilson / Newcombe intervals, minimum-evidence guard, evaluable denominator
- [x] assembly-level retrieval for bacterial targets (`asm` groups, NCBI Datasets): N complete
      genomes per release year, cut to credible amplicon windows
- [x] screen amplicons on both strands (minus-strand targets were never found)
- [x] `pair_evalue` per amplicon (chance.py); scoring guard available, off by default
- [x] `scoring.max_pair_evalue: 0.01`; flagged assays split into declining / low coverage (2026-10-04)
- [x] check the two suspected oligo typos (Sarcocystis long rev, Circovirus Mankertz fwd) against
      the papers (2026-10-04, `docs/journal/2026-10-04-first-run-review.md` "Follow-up"). Sarcocystis
      P-ITSR WAS a typo, an extra C from the spreadsheet, and is corrected (98% failing -> 96%
      detected). Circovirus #174 is NOT a typo: the paper prints the extra T, so the registry
      keeps the published sequence. Both flags cleared
- [x] optional thermodynamic columns (`screen --thermo`, primer3-py): per-oligo Tm and ΔTm, never scored
- [x] `report`: markdown + self-contained HTML, per-year tables, coverage-gap table,
      degeneracy note beside the coverage trend
- [x] indel check (`scripts/indel_check.py`, 2026-10-04): across 69k sampled fail / one-primer
      no_amplicon calls, a clean single-base indel explains well under 1% of evaluable records
      for every assay but three. Gapped scoring (parasail) is not worth building. The three
      outliers are consistent same-position indels across all records, i.e. registry oligo
      typos, which makes the script a registry QA tool

## Phase 2, the parts that are closed
- [x] **The ΔTm column is in register** (2026-10-27). `thermo.duplex_tm` called
      `primer3.calc_heterodimer`, which returns the most stable structure between two
      sequences; on a mismatched site that is a shifted, shorter, near-perfect duplex
      reporting an optimistically small ΔTm, least trustworthy on exactly the records
      the report is about. It now sums nearest-neighbour terms base-for-base
      (Biopython `MeltingTemp.Tm_NN`, SantaLucia & Hicks 2004 with the
      Allawi/SantaLucia mismatch tables), so there is no alignment search and no
      register to get wrong. **Re-running the bench comparison cost the
      thermodynamic arm half its margin: p = 0.0192 became p = 0.0708**, so the
      "thermodynamics beats the penalty rule" claim does not survive its own
      confound, while the penalty rule's 23 false negatives against 1 false positive
      do. Adjacent mismatches have no measured term, so 32 sites are withheld with
      `thermo_note: nn_unsupported` rather than scored as free.
      `docs/journal/2026-10-27-thermo-vs-penalty-paired.md`.
- [x] **`reduced_not_detected_for: [hydrolysis_probe, mgb]`** (2026-10-27). A
      mismatched hydrolysis probe is no longer counted as a detection: detection IS
      the probe, and there is no gel to look at. Measured before it was taken, by
      rendering the 2026-10-26 calls table both ways — 13 of 235 statuses move, in
      both directions, and `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` goes
      `stable` -> flagged at 6.5% of 30,382 recent records, which is the documented
      failure this switch exists to catch. It costs two published positives on the
      Leptospira bench panel; that cost stands and is recorded beside the setting.
- [x] **A new held-out set, opened with the first confirmed identity** (2026-10-27).
      `docs/validation-cases-heldout-2.tsv`. The development set is frozen and the
      first held-out set was read on 2026-10-26, so the project had no unread
      evaluation data; the Leetz 2007 case went there rather than into the dev set,
      because a dev-set row can never be un-read. It reads `works`: the paper's
      73.8% is an oocyst dilution series on one isolate, which is sensitivity, and
      this tool does not model sensitivity.
- [x] **The TNTBLAST arm is deferred, not forgotten** (decided 2026-10-27). No
      osx-arm64 build, and Rosetta 2 is a system change needing admin rights. It
      waits for Rosetta, an arm64 build from source, or a run on linux-64 or the
      cluster; `scripts/compare_thermo.py` takes a second predictor unmodified.
- [x] **The ranavirus MCP 18/19-mer question is closed** (2026-10-26, confirmed
      2026-10-27 by re-running the verifier). Mao, Hedrick & Chinchar 1997 has been
      on disk since 2026-10-25 and its Table 2 prints both primers as 18-mers,
      byte-identical to the registry, with no 19-mer anywhere. Stöhr 2015's extra 3'
      T is a later extension, not a base this registry dropped.
- [x] the recent window now widens per assay (`max_window_months`, 60) when the
      standard window holds too few records, which is what made Bd unjudgeable;
      `scripts/retrospective.py` recomputes any past date's verdict, so the
      window and the minimum can be calibrated together against real cases
- [x] **Duplication check** (2026-10-05, review 3.3, partial). Each assay now also reports how many
      distinct binding-site footprints sit behind its recent window, the interval at that many
      independent draws, and for a flagged assay whether the flag survives it. Reported beside a
      verdict and never into one: a test pins that statuses and intervals are identical with and
      without footprints. This removes the duplication it can SEE (identical footprints); clade
      structure beyond that is still unaddressed, so it is not a lower bound on the effective
      sample size. The review's "weight each distinct haplotype equally" was rejected: one
      sequencing error in a primer site is a unique failing footprint, so a healthy assay would
      read as mostly failing. Corrected 2026-10-06 after two adversarial reviews: a flag now
      needs at least `min_records_for_drift` distinct footprints to be reported as surviving
      (it had reassured at every count below that, up to 19), must also stay below the
      threshold when each distinct footprint is counted once (the sample-size reduction alone
      cannot see one clone carrying the failures), and records with no footprint information
      make the count unknown instead of counting as one real footprint.
      Corrected again 2026-10-27: `count_diverged_as_fail` gave a promoted row no footprint, and
      one such row made the count unknown for the whole assay, so the check ran on 12 of 71 flags
      and the triage list it gates on was empty. With a coarse taxid-derived footprint, 23 of 71
      hold and `Start here` shows 10 assays. No status changed.
- [x] **What the report claims is now what it measured** (2026-10-14, from an
      external review). Three changes, none of them to a computation:
      `declining` requires the assay to have cleared the threshold in some
      earlier year (`drift.require_working_baseline`), which moves 14 of the 37
      assays flagged on 2026-10-07 — all pan-family consensus PCRs screened
      against a whole taxon — into `low coverage` with a note that they are
      also falling; the duplication result (35 of 84 flags held) is printed
      beside the flag counts at the top instead of only inside the per-assay
      detail; and both reports carry an `entry` column plus a header line
      saying how much of the registry is `draft`: on 2026-10-14, 210 of 214 entries
      were (205 of 208 on 2026-10-23), and the table had presented them exactly
      like the one `active` assay.
      Registry counts are now printed by `python -m assaywatch.validate
      registry` rather than written into prose, where they had drifted to
      164/142/21 against an actual 214/167/44.
      Extended 2026-10-27: the report named Benjamini-Hochberg where the run used Holm, so the
      label is now read from `config.yaml`; exclusion counts reconcile for all 71 assays; and
      the `claims` hook built to catch stale prose counts had been silently disabled since three
      duplicate `files:` keys landed on it, which `check-yaml` now makes an error.
- [x] **Pan-family scope logic** (`target.scope_taxids`): records outside an
      assay's declared scope leave the drift denominator and are reported as
      cross-reactivity instead. Asked for 2026-10-18, shipped; the specificity
      arm built on it 2026-10-27.
- [x] **Sequence-cluster lineages** (`assaywatch.subcluster`,
      `lineage.cluster_resolver`): assays whose target species carries
      within-taxid diversity at the primer sites can be grouped by primer-site
      homology and each cluster treated as a lineage. Asked for 2026-10-18.
- [x] **The lineage binomial no longer overflows.** `comb(n, k) * p**k * q**(n-k)`
      went to nan above n ~ 1030; it is computed through `binom.cdf` instead
      (`assaywatch/lineage.py`). Asked for 2026-10-18.
- [x] **Data integrity before any retrieval** (2026-10-27). An empty efetch page was
      accepted as zero records and the run recorded, after which the incremental cursor
      skipped records that were never written; a short page was indistinguishable from the
      legitimate WGS-master case; the cursor was keyed on the assay query only, so changing
      a length filter permanently skipped older records that newly qualified; a missing
      `.sig` wedged the pipeline unrepairably, and declaring it as an output was not enough
      because nothing requested it; and `--config` overrides moved the cache key, triggered
      a full rescreen, and never reached the subprocess.

## Review history

`docs/journal/2026-10-04-pipeline-review.md` reviews the pipeline stage by stage from a
software and a methods angle. Its short version — the estimand is wrong (one
population proportion per assay cannot see a lineage-conditional failure, which
is why validation caught 1 of 12), the denominator conditions on the outcome,
records are not independent so the intervals are too narrow, and declared
amplicon sizes are not enforced — is still the best one-paragraph statement of
what is wrong with the method. Amplicon enforcement shipped; the other three are
items 4–9 and the limitations above.

`docs/journal/2026-10-27-four-perspective-review.md` is the most recent, read from four
angles (engineering, methods, bench diagnostics, a cold newcomer read), and every
open item it raised is in this file.
