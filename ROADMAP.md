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
- Two documents are plans from end to end rather than records with a tail —
  `docs/bayesian-scoring-plan.md` and
  `docs/journal/2026-10-24-scoring-strategy-test-plan.md`. They keep their detail,
  their pre-registered predictions and their kill criteria; what is OPEN in them is
  summarised under "The scoring rule's own test plan" below. The first sweep missed
  both, because it looked for forward-looking sections and these have no other kind.

New ideas go here, not into the sprint. Scope for v0.1 is frozen in the build plan.

---

# Open work

## Waiting on a maintainer, minutes each

- **One proposed tier-2 row needs a works/fails verdict**: Quackenbush 1998 on
  `Pan_HERPES_dsDNA_Polymerase_round2`, written into
  `docs/validation-cases-heldout-2.tsv` marked PROPOSED on 2026-10-28 and read as
  `works` — the nest sequenced a ~250 bp product from five green turtle fibropapillomas
  that is 53% identical to its nearest relatives. The arguable part is stated in the
  file: the same paper reports tumour-free skin and two olive ridley turtles as PCR
  negative, which is a true negative and not a failure.
- **Whether any entry becomes `active`.** `CALICIVIRUS_ssRNA_Helicase_Reid_1999` lost its
  only OPEN flag on 2026-10-28 (`oligo_sequence_uncertain` → `oligos_modified`), so it is
  now eligible on the schema's terms; `thin_evidence` and 16 amplifying records of
  152,379 are the reason not to. Nothing else changed status.
- **Everything the fetch list was waiting for is in** (2026-10-28), and the two Priority 1
  decisions of 2026-10-27 are taken and recorded in `## Done`.

## Shipped today, and what it still owes

- **S3b is live: `by_chemistry.conventional.primer_3prime_penalty: 2.0`** (2026-10-27).
  `strategies/s3b-conventional-3prime-penalty.yaml` drops `primer_3prime_penalty`
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
    switch moved and whatever S3b moves on top; the two verdicts measured here are
    `Pan_flavivirus_NS5_3_round2` (a false alarm dropped) and the Forslund FAP case
    (`low coverage` -> `declining`).
  - ~~78 small movers were never rescreened~~ — the 2026-10-27 run rescreened
    everything, and the replay agrees with it on all but 8 of 2,679,894 shared rows
    (6 `fail` -> `no_amplicon`, 2 `fail` -> `reduced`, none on a tier-2 case). Closed.
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

## The scoring rule's own test plan, which this file did not list until 2026-10-27

The scoring method has a ladder of candidates and a kill criterion for each, written
down on 2026-10-24 in `docs/journal/2026-10-24-scoring-strategy-test-plan.md` Part 1,
and a three-project Bayesian plan in `docs/bayesian-scoring-plan.md`. Neither was ever
in this file — the consolidation of 2026-10-27 swept the forward-looking TAILS of
journals and missed two documents that are forward-looking from end to end. What ships
today is the **budget rule**: a position-weighted additive penalty, binned at
`detect_max` 1.0 and `reduced_max` 3.0, with `terminal_mismatch_fails: true` and, since
2026-10-27, a 2.0 3'-window penalty for conventional PCR.

- **S5 = C2: the Bayesian per-record model, and it is GATED.**
  `P(detect) = P(fwd ok) x P(rev ok) x P(probe reports)`, each logistic over identity,
  position, adjacency and length, with chemistry as a hierarchical intercept and priors
  from Kwok and Stadhouders. **The gate is at least 40 within-family negatives across
  several independent papers; there are 11.** Below 40 it is not fitted, and nothing
  fitted on 11 would be defended. So the blocker is the corpus sweep — the same
  literature pass as held-out case collection, one read per paper for both — and not
  the modelling. C2 is also what `docs/related-work.md` would need before claiming a
  probabilistic matcher.
- **Done, so that the list is not read as "no Bayes anywhere": C3**, the Bayesian
  treatment of the validation matrix, ships — every proportion `scripts/retrospective.py`
  prints carries a Jeffreys interval, which is why the tier-2 figures read "3/9 = 33%
  (95% CrI 10%-65%)" rather than a bare percentage.

- **S7b = identity in the mid window, registered 2026-10-28 and unpriced.** Extend
  `scoring.mispair_penalty` to the mid window ALONE — identity rather than position, which
  is what Kwok 1990 and Stadhouders 2010 measure. The unscoped version was measured and
  rejected on 2026-10-22 (it erased internal wobbles and cost three documented catches);
  mid-only has never been tried, and it is the candidate that could discount the G:T
  wobble costing the monkeypox G2R assay its verdict while leaving the A:A and A:C
  mispairs in the FAP negatives at full price. Needs a `mispair_window` setting rather
  than a config overlay, which is why it is not priced yet.

Dead, and recorded so they are not re-proposed: **S1** serial per-oligo gates (no
threshold pair passed its own criterion, 2026-10-26), **S2** a smooth positional decay
replacing the 5/5/rest step (2026-10-26), **S6** the Kwok premium on severe mispairs
(breaks a bench row and adds a false alarm for no catch, 2026-10-27), **S7** halving the
mid-window penalty (identical tier-2 and identical 92.7% bench accuracy, and it newly
predicts a band on two within-family bench negatives, 2026-10-28), and the
**thermodynamic** engine, which has never been a scoring input and whose measured
advantage over the penalty rule evaporated once its register was fixed (2026-10-27,
p = 0.019 -> 0.071). **S4/M1 shipped** 2026-10-27.

## Operations

- **The weekly re-screen is installed on this machine only** (2026-10-27, live,
  Sunday 09:00, lid open; `docs/journal/2026-10-27-live-run-and-schedule.md`). It is
  machine-local state: the other MacBooks are not scheduled, and README's "re-screens
  on a schedule" is true of exactly one laptop. `scripts/weekly_run.sh --live` now
  refuses a tree with uncommitted changes under `assaywatch/`, `config.yaml`,
  `registry/` or `Snakefile` (`--allow-dirty` overrides, knowingly) — the guard the
  second failed run of 2026-10-27 needed, proved to fire on an untracked probe file.
- **The full run under today's scoring exists**: `results/2026-10-27/`, committed as
  `docs/example-run-2026-10-27/`. 16 statuses moved against 2026-10-26, the probe
  switch's and S3b's among them, and the S3b replay was checked against it row for
  row: 8 call disagreements in 2,679,894. **Owed by that run**: the groups of the 31
  entries edited afterwards (28 orientation notes, 3 renames) and the five new mpox
  entries rescreen on Sunday, because the signature hashes the registry.

  **Two runs on 2026-10-27 failed at `collect_calls`, and the second was self-inflicted.**
  The first found 461 of 482 cached screens stale against the new scoring config —
  Snakemake held no metadata record for them, so its params trigger never fired, and
  the signature guard in `collect.py` was the backstop that caught it (correctly: delete
  and rerun). The second rescreened all 461 and was refused at collect because
  `settings.py`, `config.yaml` and other modules in the screen hash's import closure
  were edited and committed WHILE IT RAN, so every fresh screen carried a signature the
  pipeline no longer expected by the time it was read. The guard cannot tell an
  innocent mid-run edit from a stale cache, and should not try. Both halves of the fix
  are in: `scripts/weekly_run.sh` refuses `--live` while any path under `assaywatch/`,
  `config.yaml`, `registry/` or `Snakefile` is dirty, so a scheduled run never starts on
  a half-edited tree; and the rule for the human is that nothing in that closure is
  touched until the run reports.
- **Two inert switches, grouped here because each is the same shape**: a mechanism
  built, tested, and shipped off for want of evidence.
  `lineage.unclassified_is_bucket: false` (tier-2 is unchanged by it, so there is
  nothing to ship it on) and `thermo: false` (needs the annealing conditions the
  registry does not carry). Two have left the list by being turned on:
  `scoring.mispair_penalty` carries the G:T / T:G discount (M1) and
  `lineage.sublineage` carries the influenza chain, both 2026-10-27. None is a
  defect. The list exists so that "the mechanism is here and the numbers are not"
  stays a count rather than a feeling.

  Two switches that were listed here on 2026-10-27 do not belong: they are not
  waiting for evidence, the evidence came in against them. `scoring.engine: serial`
  is S1, rejected 2026-10-26. `scoring.locus_identity_min: null` was built, priced at
  0.50 over the 2026-10-25 run and **rejected the same day**: it throws out 1,840 of
  9,687 sampled failures, concentrated exactly where it must not — `Pan_HERPES`
  loses 47 of 47, because for a pan-family or consensus assay a divergent amplicon
  interior is what SUCCESS looks like
  (`docs/journal/2026-10-25-locus-identity-design.md`). Both are in the dead list
  under the scoring test plan above, and `locus_identity_min` must stay null.

## Method debts

- **One mid-window mismatch is the boundary, and it drives 69 sites on 23 assays**
  (traced 2026-10-28, `docs/journal/2026-10-28-g2r-false-alarm-traced.md`). Held-out set
  2's one false alarm has a single mechanical cause, followed to the base: the 2022-era
  monkeypox records carry a G:T wobble at position 8 of the G2R reverse primer and an A>G
  at position 21 of the forward, which price at 1.0 + 0.5 and cross `detect_max: 1.0`, so
  8,947 records score `reduced` — and for a hydrolysis probe `reduced` is not a detection.
  M1's identity discount prices G:T at 0.0 but applies only inside the 3′ window, by the
  measured decision of 2026-10-22. Every step is deliberate; together they say a primer
  with one internal wobble detects nothing, where Mills 2022 validated the assay
  clinically.

  **The generalisation is the item.** `primer_mid_penalty: 1.0` equals `detect_max: 1.0`,
  so one mid-window mismatch sits exactly on the band boundary and a second anywhere
  pushes past it — the same coincidence already recorded for `primer_3prime_penalty: 3.0`
  against `reduced_max: 3.0`. Over the run's site table, **69 sites across 23 assays**
  show a non-3′ mismatch carried by ≥200 records where detection falls from >80% to <20%,
  split 36 on `low coverage` assays and 33 on `declining` ones.

  **What may and may not settle it.** Not the Mills row: tuning on it would make held-out
  data a second development set. The bench panels may be spent, and the first question is
  whether any of their 179 rows turns on a single mid-window mismatch — if none does, the
  mid-window penalty rests on nothing this project can measure, and `config.yaml` should
  say so. A second held-out row would settle it properly, and 22 of those 23 assays are
  not monkeypox.
- **The 30 refused assays are refused on the POOLED recent count, not per lineage**, so
  the hierarchical layer cannot reach them: `min_records_for_drift` gates `finalise`
  before any lineage is looked at. **Designed 2026-10-27 as C1b** in
  `docs/bayesian-scoring-plan.md`, with its two kill tests pre-registered, the
  alternatives priced and rejected, and the cost stated — it borrows a prior across
  assays of one chemistry, which are not exchangeable in any honest sense, so the prior
  does real work where the within-assay layer's barely did. Not built. What it would be
  worth: tier-2 declines to judge 3 of its 11 documented failures, which is the whole
  difference between "6/11 caught" and "6/8 among the cases it judged at all".

- **`drift.anchor_fdr`'s value has no evidence behind it, and the bench panels
  cannot supply any.** 0.05 and 0.01 differ by a factor of two in rows moved (7,206
  against 13,693; 2026-10-24 run), 0.001 is what ships, and tier-2 separates them on
  one row (`docs/journal/2026-10-24-archive-anchor.md`). The plan of 2026-10-27 said
  to price it on the 179 bench rows the way the penalty was; **that is impossible by
  construction**, worked out before any run: `anchor_fdr` relabels rows between
  `no_site` and `fail`, and a bench row is scored band / no_band, where `no_site`
  and `fail` are the same answer. No value of `anchor_fdr` can move a single bench
  prediction. What is left is a held-out read, which is item 4d's corpus, or
  accepting that 0.001 is a placeholder with one tier-2 row behind it and saying so
  in `config.yaml`, which it already does.

- **Deposit date is not collection date, and it is not immaterial** (measured
  2026-10-27, `docs/journal/2026-10-27-deposit-vs-collection-date.md`). Of 1,447
  assembly records on disk, 1,001 carry a collection year; the median lag to deposit
  is 5 years, **25.9% were collected ten or more years before they were deposited**,
  9.8% twenty or more. For a bacterial target built from complete genomes, "recent
  deposits" is partly a sequencing-backlog signal. Two steps, neither built: (1) for
  `asm` records, carry `collection_date` as a metadata column (it is parsed today and
  written only into the title string) and add `drift.window_on: deposit | collection`,
  default `deposit`, with records lacking a date falling back and being counted;
  (2) for nuccore — 99.9% of the calls table — `/collection_date` is a source-feature
  qualifier, not an `esummary` field, so it is a retrieval change plus a re-fetch of
  every archive, to be priced before it is built. A window that uses collection date
  for 0.1% of records is a different kind of wrong, so step 1 must say in the report
  which records it applied to.

- **`target.exclusivity_taxids`: three sets in, and the rest is one paper at a time**
  (2026-10-28). `scripts/extract_exclusivity.py` prints every sentence in which a paper
  claims its assay does NOT amplify something — **118 of the 178 papers on disk carry at
  least one** — and most are not usable as they stand: a pan-family paper's claim is
  usually about antibodies or "unrelated agents", and the 17 assays whose reports show
  out-of-scope records are showing within-family taxa and synthetic constructs that no
  paper claimed to exclude. What is usable is the species-specific assays, where the paper
  names the neighbour it must be told apart from. BPSV, the two Huo 2022 F3L mpox entries,
  the ORFV entry and the generic PAPV entry now carry them (134 retrieval groups, up from
  125); seven of the nine new groups hold nothing until the next run fetches them. What is
  left is reading, and the retrieval cost is the thing to weigh — each named taxon is a
  new archive, though the orthopox set is only 3,772 records.
- **Tier 2: retrospective validation.** Assemble assays with published
  follow-up — a paper, erratum or redesign reporting the assay failing on
  particular lineages, or reporting it still working — and ask whether
  AssayWatch flags what the literature found, using only records deposited
  before that paper. That gives a confusion matrix, and the thresholds become
  whatever optimises it rather than whatever looked sensible. **Every number in
  `config.yaml` is a placeholder set by eye**, so until this exists the
  statuses read as "worth looking at", not as measurements. It is also the
  paper's main figure.

  **The binding constraint was identity, and with every PDF in it is now CONTENT.**
  `scripts/check_candidate_identity.py` over the `mismatch`/`redesign` rows read 1
  CONFIRMED / 1 VARIANT / 11 UNCONFIRMABLE on 2026-10-27, with 6 of those waiting on a
  PDF. All six arrived 2026-10-28 and the queue now reads **2 CONFIRMED, 1 VARIANT, 10
  UNCONFIRMABLE** (`results/retro-identity-2026-10-28.tsv`) — and **not one of the newly
  readable papers prints our oligos**. Tsukamoto 2008 prints 29 and Csordas 2004 prints
  12, none ours; the second CONFIRMED (Süß 2009 on the Salmonella invA pair) is a
  synthetic-template mismatch study and not a case at all. So this queue is spent: no
  document will settle the remaining rows, and the next tier-2 rows have to come from a
  different search rather than from more fetching.

  **Where they will come from instead.** Quackenbush 1998 was in the batch as a
  *completeness* paper and turned out to be a tier-2 candidate — it uses the pan-herpes
  nest and reports what it found. That is the pattern worth exploiting: the citing-paper
  graph was searched for phrases about FAILURE, and a paper that simply USES a registry
  assay and reports a result is just as scoreable. `scripts/find_retrospective_cases.py`
  could be re-run for use-and-report language, which is a cheap change to a script and
  the only lead left that does not need new PDFs.

  **Set 2 is partially spent**: 3 rows, all read 2026-10-28, 1 agrees / 1 weaker / 1
  false alarm. See the held-out item under Data and curation.

## Data and curation

- **216 `needs_review` flags sit on 207 of the 209 entries** (2026-10-27). Not a
  backlog of errors — a flag is an honest label on a reading that could not be made
  from the source — but it is 216 open readings, and some classes are actionable
  where others are permanent. Largest: `orientation_inferred` 28,
  `amplicon_measured_not_published` 20, `oligos_from_secondary_source` 19,
  `oligos_modified` 14, `scope_narrower_than_taxid` 13,
  `pairing_is_curator_reading` 11. `oligos_modified` never clears, because it is true.
  **`orientation_inferred` is measured** (2026-10-27, `scripts/check_orientation.py`):
  the archive yields products under the stored orientation for 26 of the 28, from 20 to
  16,410 per entry, and for none does it yield zero; the two Sunshinevirus pairs yield 2
  each on 8 records. The flag records provenance and stays; what is owed is a `note`
  on each of the 26 carrying its number — 26 registry edits, after the live run.
  `pairing_is_curator_reading` needs the paper's protocol text, one read each.
  The 20 `in-text` oligos are enumerated in `docs/2026-10-27-in-text-oligos.tsv`.
- **10 entries sit in `pending/`, every one of them for want of a verifiable DOI.**
  The three pending `HANTAVIRUS_ssRNA_S_segment` nests (F2/R2, F3/R3, F4/R3) are the
  hard case, and the plan of 2026-10-27 was wrong about them: it proposed citing
  Aitichou 2005 with `oligos_modified`, but Aitichou prints only HANTAV1U/L, the
  ancestors of UHantaF1/R1 — and that pair is already live in `registry/` citing
  Anthony 2013, which prints it. Nothing on disk prints the three pending pairs; their
  nesting was read off amplicon geometry and one shared reverse primer, and their own
  note says to re-check that first if a source appears. They stay pending until one
  does. Of the other seven, two are `as_written: unpublished` protocol oligos (pan-parvo
  VP1, polyomavirus VP1) and stay pending by definition. The rest were searched on
  PubMed on 2026-10-27 and not found: for the feline morbillivirus L-gene pair the only
  hit is De Luca 2018 (10.1016/j.jviromet.2018.05.002), which targets P/V/C and only
  cites "a generic RT-PCR targeting the L gene"; for the enterovirus EVRV1/EVRV2 pair,
  four papers USE a 5'-UTR/VP2 assay and none designs one; for the poxvirus polymerase
  set, nothing. The design papers, if they exist, are not findable by assay description,
  which is the same wall the identity work hit.
- **The held-out collection target is not met, and set 2 is now partially spent.** It
  holds 3 rows against a target of 15-20 with at least 5 of `mechanism: drift`, and set 1
  is spent. All three of set 2's rows were read on 2026-10-28 (disclosed in the file and in
  `docs/journal/2026-10-28-papers-arrived.md`) because checking that a proposed row parses
  scores every row: **1 agrees, 1 weaker, 1 false alarm**. The false alarm is the
  informative one — Mills 2022 validated the G2R generic monkeypox assay on 2022 outbreak
  clinical specimens and the shipped config calls it `declining`. Nothing was changed
  because of it and nothing may be. **One row awaits the maintainer's verdict**: Quackenbush
  1998 on `Pan_HERPES_dsDNA_Polymerase_round2`, proposed `works`.
  `docs/journal/2026-10-24-heldout-candidates.md` records the first sweep and the gap
  that stayed open. This is the same literature pass as the within-family negative
  corpus that gates C2, so one read per paper serves both.
- **The registry is becoming an assay registry; what is left needs the maintainer, not
  another pass.** Two passes landed 2026-10-27 (`## Done`): the automatic one over the
  values a paper states once, and a reader's pass over all 64 papers the first refused.
  What remains:

  - **Three entries carry a value that is now disbelieved and cannot be replaced by the
    tool**, because `extract_conditions.py` only adds and fixes and these need a
    DELETION: `CMV_UL55_gB_Deckers_2009`'s `mg_mm` and the three Sigrist
    `ORTHOBORNAVIRUS_XP_*` entries' `mg_mm` came from the conventional arm of a paper
    whose probe assay is the registry entry, and `LEPTOSPIROSIS_Flagillar_filiment_Prote`'s
    `annealing_c` is one of three programmes in a MassTag paper and cannot be attributed
    to the flaB assay. A hand edit each.
  - **The remaining rows in `docs/2026-10-27-conditions-proposals.tsv`**: the LoDs and
    master mixes, which are quoted prose rather than numbers, and the oligo
    concentrations, where only a reader can say whether a number is a stock or a final
    concentration. Both passes left them deliberately.
  - **`panels` is untouched.** Each one is a table in a paper and a read of its own.
  - **Two protocol shapes the schema cannot hold**: a touchdown or step-down (Lan 2010,
    Bocavirus, a 1998 SIV nest) has no single annealing temperature, and Ahne 1999
    deliberately varied its own between 40 and 50 °C by isolate. Each affected entry
    records the temperature its working cycles run at, or none, and says so.

  Lifting `thermo: false` is arguable for the entries that now carry an annealing
  temperature and still dishonest for the rest.

- **Registry coverage.** Audit the PREDICT consensus-PCR panel for gaps, and
  add assays in current wildlife-lab use that PREDICT never covered — fungal,
  bacterial and parasitic targets especially. Sequences only from a source that
  can be read and cited, never transcribed from a secondary list.

- **18 entries carry a taxid NCBI has merged away**, found 2026-10-27 by the new
  containment check: 11232 → 3052342 (9 CDV entries), 121791 → 3052225 (2 Nipah),
  11051 → 3044782 (3 flavivirus), 10292 → 3044472 (4 herpesvirus). Retrieval still
  resolves a merged id, which is why nothing noticed, and an entry on a retired id is
  one taxonomy release from an empty archive. **The fix has a cost**: `data/retrieved/`
  is keyed by taxid, so changing `target.taxid` moves the group and re-fetches it. Do
  it as its own live run with a `report_diff` behind it.
  `docs/journal/2026-10-27-taxid-containment-and-merged-roots.md`.
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

- **The Greene SLURM profile is written and UNTESTED.** `profiles/slurm-greene/config.yaml`
  (2026-10-27) carries the partition / account / QoS stanzas, the `/scratch` filesystem
  and 60-day purge, the compute-node network question, and the `sinfo` / `sacctmgr` /
  `sacct` commands that fill each VERIFY value — written as teaching material, since
  the mechanics are new. It cannot be tested from this laptop. First submission on a
  login node closes it; until then every value marked VERIFY is a guess with the
  command that checks it beside it.

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
- [x] **Per-lineage per-year rows, and the influenza verdict decomposed** (2026-10-28,
      `docs/journal/2026-10-28-influenza-decomposed.md`). `lineage.md` carries a per-year
      block under each lineage below the threshold — 252 blocks, 3,652 rows, grouped by the
      same `lineage.lineage_of` the share table uses, from deposit years read in the
      metadata pass that already ran. It answered the question it was built for on its first
      run: H3N2 has **never** been detected by the influenza matrix assay, 1.1% in 2005
      against 0.1% in 2025, so that lineage is a coverage gap of twenty years' standing and
      not drift. It also separated two effects inside one pooled 6.5%: that gap and a real
      fall in the subtypes the assay does detect (88–90% in 2009–2011 to 32–56% since 2022).
      One population proportion cannot tell those apart, which is the 2026-10-04 review's
      complaint from the other side.
- [x] **The "2026 flood of untyped influenza records" was a regex that could not read a
      partial subtype** (2026-10-28, same journal). The decomposition's apparent third
      effect was 4,729 evaluable 2026 records "whose title names no subtype", and the item
      opened on it asked for a resolver that reads the subtype from the sequence. Measuring
      the bucket first killed that: **3,857 of the 4,729 carry a subtype in the title**
      (2,220 `H1pdm09`, 1,607 `H3`), and the shipped `\((H\d+N\d+)\)` required both numbers.
      Broadened to `\((H\d+(?:N\d+v?|Nx|pdm\d+)?|Hx(?:N\d+|Nx)?)\)` and shipped under both
      of `config.yaml`'s gates (tier-2 identical, `report_diff` "No assay changed status").
      4,188 records across all years leave the residual bucket carrying 8 detections, into
      H1pdm09 (0 of 2,220), H3 (5 of 1,745), H1, HxN2, H3Nx — effect 1 again, since
      `H1pdm09` is pandemic H1N1 and `H3` is H3N2 with the N untyped. The residual
      *Alphainfluenzavirus influenzae* row goes from 9.3% to **23.1%**: the pattern was not
      only missing labels, it was halving the share of the row that means "unknown". **No
      sequence-based subtype resolver is wanted** — 872 records carry no label at all.
- [x] **A registry edit that cannot change a call no longer rescreens anything**
  (2026-10-28, `docs/journal/2026-10-28-screen-signature-projection.md`). **The claim
  this item was opened with was wrong**: the signature was already per-group, not
  whole-registry — `screen_signature(taxid, group)` hashed only that group's own assay
  files, and the "357 screen jobs" read off a stopped run were the post-checkpoint DAG's
  denominator, not a work queue. What was true is subtler: it hashed each entry's whole
  YAML, so a curator's note, a review-flag wording or a `conditions` block invalidated
  every group holding that entry. `signature.screen_key` now hashes the screen-relevant
  projection instead. Replaying the two days of curation: **108 of 125 groups and 444
  archives rescreen under the old scheme, 10 groups and 47 archives under the new one**,
  and those 10 are the ones that should — four retired-taxid roots, BPSV and its two
  neighbours gaining `exclusivity_taxids`, the calicivirus flag change, and the
  orthoreovirus pair gaining a flag.
- [x] **A published exclusivity claim is visible, and the first one tested reconciles two
      numbers this registry carried in contradiction** (2026-10-28,
      `docs/journal/2026-10-28-bpsv-exclusivity-reconciled.md`). The report has a
      status-independent `## Published exclusivity claims, tested` section, because the
      cross-reactivity table lived inside the flagged-assay detail block and BPSV is
      `insufficient data` — so its 2,692 off-target calls were computed and invisible, which
      is the usual case for an assay whose neighbour had to be fetched. Two fixes made it
      worth printing: the denominator is EVALUABLE off-target records, not everything
      screened (the orf virus claim read "0 of 2,498" where 2,413 of those records hold no
      product for anything), and `amplified` prints beside `detected`, because a mismatched
      hydrolysis probe is not a detection and the assay forms a product in 82 of 85
      evaluable orf virus records while detecting none of them. The 2026-10-24 hand screen
      and Zhao's panel were never in conflict: the primers are genus-specific and the probe
      separates the species, which is what the paper says.
- [x] **A reader's pass over the 64 papers the automatic one refused** (2026-10-27,
      `docs/journal/2026-10-27-conditions-curator-pass.md`). 236 values read by hand with
      the sentence each came from, and **twelve values an earlier pass had written
      corrected**, every one of them an attribution rather than an extraction: Xiao 1999's
      two programmes (55 °C is the nested RFLP protocol the registry holds, 60 °C the
      full-length SSU it cloned), Latimer 2010's "redundant POL PCR" against "all other
      PCR amplification", Zhao 2013 saying in its own words that BPSV is kept at 60 where
      the automatic pass had read 62.5 off the PCPV assay, and Spackman 2002's matrix set
      at 60 °C where the entry carried the H7 assay's 58. A sixth extraction bug came out
      of it: a degree sign the PDF renders as the digit 8, so "948C" matched as 48 °C —
      which is where `Pan_HERPES_dsDNA_Polymerase`'s 48 came from, against a paper that
      prints 46. Re-running the whole pass after the fix moved 2 of 644 proposals, both
      that entry, and recovered two values whose hand-read agrees.
- [x] **The registry knows what temperature 119 of its assays ran at** (2026-10-27,
      `docs/journal/2026-10-27-conditions-first-pass.md`). `conditions` / `performance`
      / `panels` validated empty first, then `scripts/extract_conditions.py` read the
      178 papers on disk and proposed 644 values with the sentence each came from;
      `--apply --only-sole` took the 292 that need no judgement. Five extraction bugs
      were found by looking at the numbers, four of which pass any range check — a
      spaced-out decimal point read 25 mM where the paper says 1.25, a decimal comma
      read 0 mM, and a 50 mM stock was read as a final concentration the same sentence
      states as 1.5 mM. `format` is not a block, and the reason is in the commit.
- [x] **A registry key given twice loaded silently, and one entry's note was lost for
      three days** (2026-10-27). `yaml.safe_load` takes last-wins, so two
      `notes_curator` keys left the first value in the file and in no loaded entry,
      past the validator, the screen and the report. `scripts/check_duplicate_keys.py`
      walks the node tree — by the time there is a dict the evidence is gone — and runs
      over every registry and pending file on any registry commit, where `check-yaml`
      sees only the files one commit touches. That is the second gate in two days found
      to be looking at a subset, both times through a duplicate YAML key.
- [x] **A near neighbour a paper claims to exclude is fetched on purpose** (2026-10-27).
      `target.exclusivity_taxids`: each named taxon becomes its own retrieval group on
      the assay's own query, so a published specificity claim can be screened instead of
      being represented by whatever happened to be on disk. No new group kind and no new
      cap; the scope filter already keeps those records out of the denominator and the
      cross-reactivity table already shows them, now marked `claimed` so a reader can
      tell a specificity result from a coincidence. The schema refuses the target's own
      taxid and anything also in `scope_taxids`. BPSV is the first entry: 124 retrieval
      groups become 125, because its orf virus arm shares the archive `ORF_VIRUS_...
      _Zhao_2013` already fetches and only pseudocowpox virus is new.
- [x] **The influenza matrix probe is failing on H3N2 and H1N1 and working on the avian
      subtypes** (2026-10-27, `docs/journal/2026-10-27-influenza-sublineage-enabled.md`).
      `lineage.sublineage` is on for that assay: a title regex splits one NCBI name into
      57 subtypes, and on the corrected numerator the ordering inverts against the
      pre-fix table — H3N2 1.2% of 38,771, H1N1 2.6% of 27,725, H5N1 34.0%, and thirty
      avian subtypes at 85–100%. The pooled 6.5% is the two human-circulating subtypes;
      a single proportion could not say that. Enabling it moves nothing (tier-2 identical
      case for case, 0 of 193 statuses), so it is adopted for what it reports.
- [x] **The `taxon_name` mismatches are closed at both ends, and 0 remain** (2026-10-27,
      open since 2026-10-04). Three were ICTV binomial renames where the stored name was
      the paper's (ABPV, BQCV, SBV), renamed with the paper's name kept in parentheses.
      The other eight were never wrong: a species-level name on a deliberate genus-level
      taxid narrowed by explicit organism taxids in the query (Grizzle 2003 LMBV on genus
      *Ranavirus*, seven Latimer 2010 EEHV entries on genus *Proboscivirus*), which
      `check_taxids.py` could only read as `MISMATCH`. It now has a `SCOPED` status that
      reads the query, requires every pinned organism taxid to descend from the entry's
      own taxid — a query reaching outside the root is the Mycoplasma failure again and
      still reports `MISMATCH` — and then asks whether one of them carries the stored
      name. All eight resolve, naming the species they fetch. 0 mismatched taxids.
- [x] **C1's hierarchical layer, measured on both halves of its plan** (2026-10-27).
      Built (`assaywatch/hierarchical.py`), printed beside every verdict; first kill test
      does not fire (φ 0.3–11.7 on multi-lineage assays, intraclass correlation
      0.08–0.78); second kill test does not fire either — `lineage.verdict_from: posterior`
      leaves tier-2 identical and moves 0 of 240 statuses
      (`docs/journal/2026-10-27-c1-second-kill-test.md`). As a verdict input it changes
      nothing, so it ships beside the verdict with `verdict_from: holm`. What it earns is
      honest numbers for thin lineages, not a different decision.
- [x] **`score.load_config`'s per-chemistry cache is keyed to the scoring block it came
      from** (2026-10-27), so a shallow copy that swaps the block recomputes instead of
      answering from the shipped table — the footgun that bit two callers today.
- [x] **M1 ships: `scoring.mispair_penalty: {"G:T": 0.0, "T:G": 0.0}`** (hold lifted
      2026-10-27, a maintainer decision, after S4 measured its only documented cost away:
      no catch lost, the influenza 2010 case promoted to the drift flag, PPV 3/9 -> 4/10,
      five bench rows fixed and none broken). The rule is no longer wholly identity-blind.
      **Confirmed by screen the same night** (`docs/journal/2026-10-27-m1-confirming-rescreen.md`):
      the real run agrees with the S4 replay on all but 153 of 2,679,894 rows, every
      disagreement pessimistic; 8 statuses move against the pre-M1 run. The Kwok premium — A:G, G:A, C:C at 2.0, A:A at 1.5 — was priced
      the same evening as S6 and **killed on both pre-registered criteria**: one FAP
      band row broken and nothing fixed, one false alarm added and no catch
      (`docs/journal/2026-10-27-s6-kwok-premium-killed.md`). The discount half is the
      half this registry can use.
- [x] **Five Huo 2022 entries add clade- and lineage-level mpox typing** (2026-10-27).
      Two multiplex panels designed on 138 poxvirus genomes, one entry per probe: clade
      IIa/IIb, clade I and non-MPXV orthopoxvirus on one F3L-region pair (179 bp,
      measured on 28,921 products), B.1 and non-B.1 SNP probes on a second (81 bp). 15 of
      15 oligos `exact` against the open text; DOI resolved and checked; all `draft`.
      Mills/Greninger 2022, the other candidate, designs nothing — its G2R set IS the
      registry's Li 2010 generic entry, which made it the second row of held-out set 2
      instead (`docs/validation-cases-heldout-2.tsv`, a `works` case on 2022 clinical
      specimens with identity read from the page).
- [x] **28 `orientation_inferred` flags carry the archive's answer** (2026-10-27): the
      product count under the stored orientation from the 2026-10-27 run, appended to
      each flag's note and never substituted for it. 26 confirmed by twenty or more
      products, two Sunshinevirus pairs too thin to say. Three bee-virus `taxon_name`s
      now carry NCBI's binomial with the paper's name in parentheses.
- [x] **The full run under today's scoring, published** (2026-10-27,
      `docs/example-run-2026-10-27/`, `docs/journal/2026-10-27-live-run-and-schedule.md`).
      16 statuses move against 2026-10-26; both S3b predictions checked, one of them
      corrected in the write-up (the flavivirus move was a 2017 retrospective verdict, not
      a 2026 status). S3b's replay agrees with the real screen on all but 8 of 2,679,894
      rows, which closes the 78 unrescreened movers. The weekly launchd job is installed
      live on this machine for Sunday 09:00.
- [x] **The unnamed lineages were a missing roll-up, not missing names** (2026-10-27).
      775 of the 1,390 rows in the 2026-10-26 lineage report read `taxid_<n>`. Three
      diagnoses in one day, each measured: rebuilding the taxonomy cache named 3; keeping
      names for no-rank grouping keys named 3 more; and then the cause — every one of the
      322 taxids HAS a species above it (MPXV is 10244, no rank, under species 3431483),
      and `lineage_report.py` never applied `lineage.group_at_rank: species`, which
      `drift.py` applies for report.md. So lineage.md said `taxid_10244` where report.md
      said "Orthopoxvirus monkeypox (3431483)" of the same records. The roll-up is now
      applied in both: 1,941,507 call rows roll up, **775 unnamed rows become 2**, and
      1,390 rows become 1,084 because strain-level rows merge into their species.
- [x] **The lineage layer counts a detection the way the verdict does** (2026-10-27).
      `lineage.py` hard-coded `("detect", "reduced")`; since the probe switch that is wrong
      for 51 entries, and the influenza matrix assay read 6.5% pooled and 72–100% per
      subtype from the same calls, with `worst_lineage_verdict` able to override a status
      on the wrong numerator. `per_lineage_stats`, `lineages_never_covered` and
      `lineages_ever_covered` take the assay's `detected_calls`; `drift.py` passes its own
      and `lineage_report.py` reads the chemistry map the way `report.py` does. Four tests
      pin that the numerator moves and the denominator does not.
- [x] **The window and the minimum are priced together** (2026-10-27,
      `scripts/window_grid.py`, `docs/journal/2026-10-27-window-minimum-grid.md`). On the
      development set the minimum does nothing to the matrix between 10 and 20 — it only
      trades refusals (14 / 15 / 16 declined) — and at 30 it refuses 20 for no gain. The
      window does: 12 months loses a documented catch (kill), 36 months keeps all six and
      drops one false alarm (4/32, PPV 2/8). Nothing ships, because the set is spent for
      threshold-setting; 36 / 15 is the one cell a held-out read would be worth spending on.
- [x] **Triage no longer leads with a coverage gap** (2026-10-27). Degeneracy-severe
      assays were already held off the Start here list; `declining` rows whose own note
      says the failing lineage is "a coverage gap rather than drift" now sort after the
      rest of `declining` and before `low coverage`. No status changes; a test pins that
      the rows handed in are the rows handed out. `report.triage` criterion 1b.
- [x] **C1 conjugate, measured as its plan specified** (2026-10-27). Every per-lineage
      interval in the 2026-10-22 report three ways: Wilson and Jeffreys disagree on 1 of
      1,351 lineages, and the 704 zero-width Wald intervals were the only real defect,
      already fixed by Wilson on 2026-10-23. `drift.flag_rule: posterior` (P(θ < 0.90) >
      0.95, Jeffreys prior) moves 2 of 233 statuses, both `watch` -> `low coverage` at
      small n, and leaves tier-2 identical case for case. Exhaustively over 15 <= n <=
      400 the two rules disagree on 425 of 69,581 cells and the posterior always flags
      MORE. Not killed, not adopted: ships `wilson`, mechanism kept.
      `docs/journal/2026-10-27-c1-posterior-flag-rule.md`.
- [x] **A scoped taxon that leaves its retrieval root is now detected** (2026-10-27).
      `scripts/check_taxids.py` tests every `scope_taxids` entry's NCBI ancestor list for
      the assay's `target.taxid`, resolving merged ids first — its first run reported
      4,113 escapes, every one a false reading of a merged root, which is how the 18
      retired taxids above were found. Second run: 0 escapes. The Mycoplasma case that
      motivated it is rooted at a phylum and scoped by query, so it is not the shape
      this guards; nothing in the registry is, today.
- [x] **A trend statistic exists** (2026-10-27). `assaywatch/trend.py` runs the
      Cochran-Armitage test over deposit year and the report prints z and a two-sided p
      under every flagged assay's per-year table. Beside the verdict, never into it — a
      test pins that two assays with opposite trends inside the same baseline get
      identical statuses — and with no threshold, because the project has no evidence
      to set one. `related-work.md` contribution #2 now says what ships. Still owed: a
      version over distinct footprints rather than records, since the same clade
      structure that narrows every interval inflates this z.
      `docs/journal/2026-10-27-trend-statistic.md`.
- [x] **`partial` rows count as catches, scored separately** (decided 2026-10-27). The
      third of the three decisions PR #3 asked for, and the last to be settled.
      `scripts/retrospective.py` prints a `partial gaps named` line of its own and the
      `fails` numerator — the paper's main figure — never includes one. A test pins
      that the two lines move independently.
- [x] **CONTRIBUTING states best-effort review, no turnaround** (2026-10-27), and says
      what makes a submission quick to review: validator passing, a resolvable DOI, and
      oligos readable from the cited paper's own table.
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
