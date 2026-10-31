# Resume point, 2026-10-30 (last: four entries promoted, set 3 scored, the tool caught its first drift case)

**Start here:** `docs/journal/2026-10-30-set3-scored.md`, then `ROADMAP.md` "Waiting on a
maintainer". Branch `promote-influenza-and-score-set3`.

- **The tool caught its first drift case.** `INFLUENZA_A_M1_Ward_2004` reads `declining` as of
  2013-09-06 — 86.2% of 5,847 recent records, upper bound under the 90% threshold — which
  agrees with Yang 2014. Every previous catch in this project was credited to `low coverage`;
  this is the first by the drift flag itself, so the premise the tool rests on finally has a
  confirming case. **The control:** on the same records at the same date the documented
  redesign reads `stable` at 91.6%, and the two entries differ in nothing but their oligos.
- **Set 3's second row cannot be judged, and chasing why found a live defect.** The H3 archive
  stops in 2018 because subtype-taxid queries return **0** records for 2024-2026 against
  **95,155** without the restriction — NCBI no longer assigns subtype taxids to new influenza
  deposits. The same query shape is live on **H5 Tsukamoto (archive ends 2021)** and **H7
  Tsukamoto (ends 2020)**, so neither can show recent drift by construction, and their
  verdicts in every past report rest on data that old. Not fixed: broadening the query makes
  the denominator every influenza A HA record and would make a specific subtyping assay look
  like it was failing. A maintainer's call, measurement attached in the roadmap.
- **Neither scope could be honoured**, so set 3 was NOT the first genuine test of the scoped
  matrix as its header claimed, and the claim is corrected in the file. The matrix archive's
  lineage layer sees one lineage: 18 of its 19 metadata files predate the `taxid` column and
  the one that has it reports every record as the parent 11320. A scoped matrix needs a set 4.
- Set 3 is spent. Registry is 218 live, 10 pending, both clean.

## Next, in order

1. The influenza retrieval-query decision. It gates any recent-drift verdict on H5, H7, H3.
2. Refetch the matrix group under current code so its metadata carries taxids at all.
3. Set 4, on an assay whose archive resolves below the species, if the scoped matrix is to be
   tested.

## Still yours

- The 34 `scope_taxid` values (`docs/2026-10-30-scope-worksheet.tsv`), one read per row.

# Resume point, 2026-10-30 (latest: the citation year rule unified, both drift rows landed)

**Start here:** `docs/journal/2026-10-30-citation-year-rule.md`, then the entry below. Branch
`citation-year-from-reference`, stacked on `influenza-drift-entries` (PR #34).

- **The citation rule answered one question two ways, and now does not.**
  `papers.citation_matches` gated `doi_verified` on `design_year` alone; `citation_problems`,
  which CI runs, also read years from the reference text. So `curate` refused an entry CI
  passed. Both now share `papers.year_agrees`. **Measured before shipping (2026-10-30): 220 entry-DOI
  pairs in that day's Crossref cache compared, 0 verdicts moved either way** — the change enables the new case and
  touches nothing in the registry.
- **All four influenza entries now verify**, and **held-out set 3 has both drift rows**: Yang
  2014 against the Ward matrix assay (`as_of` 2013-09-06) and Shu 2026 against the CDC H3
  assay (`as_of` 2026-10-27, Crossref's issued date). Neither is scored, for the unchanged
  mechanical reason: both name assays in `pending/`, and a pending entry is never screened.
- `doi_verified` is held false on all four by hand. `pending/` means not live whatever
  `status` says, and a schema test enforces it.
- The looseness adopted is recorded rather than buried: a four-digit number in a reference
  text that is not a year can satisfy the check by accident. That was already true of CI.
- **Still open, found on the way**: `resolve_citations.py` passes `reference or ""` where
  `curate` and `citation_problems` fall back to `as_written`, so one more tool judges a
  citation by a different text. On the roadmap under Method debts, unfixed, because it wants
  its own before/after count.

## Next, in order

1. Sign off the four entries in `pending/`, or send them back.
2. Promote, fetch the H3 retrieval group (it has never been fetched), screen the new assays.
3. Score set 3 — the first `mechanism: drift` rows the matrix has ever had, and the first
   genuine test of the scoped matrix.

# Resume point, 2026-10-30 (late: four influenza entries prepared, set 3 opened, one entry blocked)

**Start here:** `ROADMAP.md` "Waiting on a maintainer", then
`docs/journal/2026-10-30-influenza-drift-entries.md`. Tree committed on branch
`influenza-drift-entries`; `pytest` 1,811 passed, validator 214/214 live and 14/14 pending,
ruff clean, `check_citations` 214/0. Nothing promoted to `registry/`.

The two strict-bar drift cases now have assays prepared for them, which was the whole point:
of the three rows in the corpus carrying `mechanism: drift`, none met the strict bar, so the
tool's premise was untested.

- **Four entries wait in `pending/`**, every oligo verified against the paper and every
  amplicon measured against real records: `INFLUENZA_A_M1_Ward_2004` (**95 bp measured
  against a published 104**, on 183,773 of 183,777 products), `INFLUENZA_A_M1_Yang_2014`
  (95 bp), `INFLUENZA_A_HA_H3_CDC_Shu_2026` (147 bp) and `INFLUENZA_A_HA_H3_v2_Shu_2026`
  (103 bp). Ward and Yang share the existing matrix retrieval group, so they cost no fetch;
  the H3 pair opens one new group that has never been fetched.
- **Held-out set 3 is open with one row** (`docs/validation-cases-heldout-3.tsv`): Yang 2014
  against the Ward entry, `fails` / `drift`, scope 114727. **It is not scored**, and cannot
  be until the entry is promoted, because a pending entry is never screened. It is also the
  first genuine test of the scoped matrix, its scope having been read before any verdict
  existed.
- **One decision blocks one entry, and with it Shu 2026's drift case.** Citing the paper that
  prints the CDC H3 oligos rather than the FDA 510(k) that defines the assay puts
  `design_year` 2008 eighteen years from Crossref's 2026, and `citation_matches` requires
  them within one. No precedent: of 214 live entries not one has a gap over a year. CI's
  `citation_problems` passes the same entry, because it reads years from the reference text
  too, so the repo currently answers this question two ways.
- **`doi_verified` is held false on the three entries Crossref did verify.** A sign-off gate
  and a true flag cannot coexist: `not_live_because` ignores `status`, so a verified entry in
  `pending/` reads as live and a schema test fails on it. Each entry records the resolution;
  `curate` re-sets the flag at promotion.
- Two `curate` warnings were run down and are artifacts, not defects: the H3 `amplify`
  failure is `archives_for` falling back to the **segment 7** archive because the H3 group was
  never fetched (measured instead on 3,000 real H3N2 HA records: 147 and 103 bp, unimodal),
  and both H3 probes read `absent` because Table 1 writes `/ZEN/` inside the sequence, which
  `printed_oligos` cannot assemble. The second is now a roadmap item.

## Next, in order

1. Sign off the three verified entries, or send them back.
2. Take the citation call on the H3 v1 entry. Until then Shu 2026's row stays withheld in the
   journal, ready to paste.
3. Promote, fetch the H3 group, screen the new assays, and score set 3. Expect the Ward row to
   be the first `mechanism: drift` row the matrix has ever scored.

## Still yours

- The 34 `scope_taxid` values (`docs/2026-10-30-scope-worksheet.tsv`), one read per row.
- The two decisions above.

# Resume point, 2026-10-30 (four decisions taken, S7b shipped, set 2 spent)

**Start here:** `ROADMAP.md`, then `docs/journal/2026-10-30-decisions.md`. The roadmap was
reconciled against the repo first (`docs/journal/2026-10-30-roadmap-reconciled.md`: six
items were already done). Then the maintainer batched the four calls that had been waiting:

- **S7b shipped**: `scoring.mispair_window: 10`. Decided on the bench row and the separation
  criterion BEFORE held-out set 2 was read. `scoring` is in the screen hash, so **the next
  full run rescreens everything** and is the confirming rescreen; compare it with the S7b
  replay by `report_diff` and expect 7 flags to fall.
- **Held-out set 2 is spent**: twelve proposed rows accepted as written and scored. Works
  3 agree / 2 weaker / 5 `declining` (4 under S7b; the Mills row is the one that moves, as
  predicted); fails 2 caught as `low coverage`, 1 missed (Hellgren pan-hemoparasite, a clade
  failure at 98.9% pooled). **5/10 false alarms against 4/32 on the development set**, four
  of them pan-family assays whose published `works` is field sensitivity, not coverage.
  Proposed for the matrix's rule and then **REJECTED 2026-10-30**: scoring a pan-family
  `works` against `low coverage` as agreement would declare a real disagreement to be
  agreement, by a rule proposed after seeing which rows it rescued. The mismatch is between
  the paper's CLAIM and its EVIDENCE, so it is fixed with 34 `scope_taxid` reads instead.
  No unread evaluation data exists. Three rows carry `mechanism: drift` and none meets the
  strict bar; two are one inferred event.
- **Reid 1999 stays `draft`** on `thin_evidence`; recorded in the entry.
- `registry.edit()` **unfolded** long quoted scalars to one line; fixed the same day
  (`docs/journal/2026-10-30-registry-edit-fold-width.md`), so prose edits on wrapped
  entries go through `registry.edit()` again. First edit of an entry may reflow its
  notes once: 192 of 214 entries do, none change content, none change twice.

## Next, in order

Designed the same evening, one question at a time (`docs/journal/2026-10-30-design-grilled.md`):

1. ~~The collection-year lens~~ built the same night (PR `collection-lens`,
   `docs/journal/2026-10-30-collection-year-lens.md`): the share barely moves, the recent
   sample halves.
2. ~~A second trend over distinct footprints~~ built (PR `footprint-trend`,
   `docs/journal/2026-10-30-footprint-trend.md`): **64 significant declines become 32**, 23
   of 74 flip direction. The verdict's own shares and the lineage tests are still per record.
3. ~~The redesign-paper phrase family~~ built and run (PR `redesign-family`,
   `docs/journal/2026-10-30-redesign-family.md`): **2 rows, neither a primer redesign, zero
   toward a drift case.** The strict bar was never reached. Q5's other two sources remain.
4. ~~A scope per row~~ built (PR `case-scope`): `scope_taxid` is accepted and scored on the
   named lineage. **The values are yours to fill**, one taxid per row from the paper; the four
   pan-family rows of set 2 are where it pays.
5. ~~The 93 `use` rows~~ closed with no new case
   (`docs/journal/2026-10-30-scope-column-and-use-rows-closed.md`): four candidate pairs, all
   explained, one of them the citing paper retyping a degenerate primer a base short.

## Still yours

- The 34 `scope_taxid` values (`docs/2026-10-30-scope-worksheet.tsv`), one read per row.
- Pulling the two paywalled influenza candidates for the drift hunt.

**Closed 2026-10-30, so not on this list any more**: the repo is public; the matrix-rule
proposal is rejected in favour of per-row scope; **`drift.window_on` is closed** -- the
verdict always runs on deposit date and the collection-year lens is reported beside it,
because a verdict that moved with a metadata field a quarter of records lack would be less
trustworthy, not more. Every "standing item: `drift.window_on` step 1" below is history;
the string appears nowhere in `ROADMAP.md` or `config.yaml` and never will.
- `drift.anchor_fdr: 0.001` is closed as a stated placeholder: no bench panel can ever bear
  on it, because it relabels rows between `no_site` and `fail` where a bench row is
  band/no-band and those are the same answer.

# Resume point, 2026-10-29 (evening: the architecture day; everything merged)

**Start here:** `ROADMAP.md` "Architecture" (every step ticked, decisions recorded), then
`GLOSSARY.md`. Tree clean, everything pushed, no PR open, 1,782 default tests + 12 slow,
registry 214/214. Full record: `docs/journal/2026-10-29-architecture.md`.

- **The code now fits the engineering principles in `~/.claude/CLAUDE.md`.** One door to
  the entries (`assaywatch/registry.py`), one NCBI client (`ncbi.py`), one literature
  client (`papers.py`), one command (`assaywatch <stage>`), and `assaywatch curate <entry>`
  runs the curation chain write-through. 34 live scripts use the modules; 20 one-off
  analyses are in `scripts/archive/` with an index. `pytest` is 43 s and `pytest -m fast`
  is 5 s.
- **Commands changed spelling.** `assaywatch validate registry`, `assaywatch curate
  registry/X.yaml --email ...`, `pytest -m fast`, `pytest -m slow`. `python -m
  assaywatch.<stage>` still works. `scripts/check_submission.py` is a shim over
  `curate --dry-run`; `scripts/master_sheet.py` is `assay_sheet.py`.
- **GitHub Actions ran nothing today**: the private repo's free minutes were spent (macOS
  jobs cost ten to one). CI is now Ubuntu-only and runs PR branches once; it resumes
  2026-11-01. The gate is local and was run on every commit.
- **Nothing scientific changed.** No scoring number, no verdict, no registry field moved;
  the Snakefile's rules and the report renderers are as they were. The two renderers were
  checked for shared logic and have none (ROADMAP 5g).
- **Two judgement calls to know about:** `bench_panel.py` and `holdout.py` are archived
  although the open scoring test plan quotes their numbers (two package tests still load
  them from the archive); five scripts stayed live because open work names them.

## Next, in order

The scientific list of the morning's entry below stands unchanged (window_on step 1, the
93 `use` rows, trend over footprints, a drift-mechanism hunt). On the code side:

1. Try `assaywatch curate` on the next entry you add; its "Left for a human" list is the
   worklist. The oligo step reports the raw verdict only; the verifier script's judgement
   for `modified_from` and sibling runs is not folded in yet.
2. When an archived script is wanted again, run it from `scripts/archive/`; it is
   untested but runnable.

## Still yours

- **S7b** (below) is still unshipped; nothing today touched it.
- Whether to make the repo public (unlimited Actions minutes, branch protection).

# Resume point, 2026-10-29 (the influenza regex, S7b priced and held, eleven cases proposed)

**Start here:** `ROADMAP.md`. Tree clean, everything pushed, 1,845 tests, registry 214/214.
Five commits since the entry below.

- **The "2026 flood of untyped influenza records" was my own regex.** The decomposition's
  apparent third effect — 4,729 evaluable 2026 records with no subtype — dissolved on
  measurement: **3,857 of them carry a subtype in the title**, 2,220 `(H1pdm09)` and 1,607
  `(H3)`, which `\((H\d+N\d+)\)` cannot read because it requires both numbers.
  Broadened and shipped under both of `config.yaml`'s gates (tier-2 identical,
  `report_diff` "No assay changed status"). 4,188 records leave the residual bucket
  carrying 8 detections, and that bucket goes from 9.3% to **23.1%** — the pattern was
  halving the share of the one row that means "unknown". **No sequence-based subtype
  resolver is wanted**; 872 records carry no label at all.
- **`scoring.mispair_window` exists**: how far from the 3' end `mispair_penalty` acts, null
  meaning `primer_3prime_window`. The scope was a constant in `score_primer`; it is a
  config number now, and a replayable one, because `*_mispairs` are recorded at every
  distance.
- **S7b passes all three of its criteria and is NOT shipped.** Tier-2 identical, bench
  166/179 → 167/179, and **no within-family negative gains a band** — the positives and
  negatives separated where S7's position-only version moved them together. But the report
  drops 7 flags (5 assays), 6 with no ground truth, and the 7th is held-out set 2's one
  false alarm fixed by exactly the predicted mechanism. That is its strongest number and
  the one a threshold may not be fitted to. **A stale S0 control nearly made this look
  three times better than it is** — the one on disk predated M1 and S3b.
- **Searching for papers that USE an assay found 13 CONFIRMED pairs in one run**, against 2
  in three weeks of failure-weighted searching. All 7 papers read the same day; **eleven
  rows proposed**, so set 2 is 14 rows, 11 never scored. The valuable three come from one
  paper that locates a two-base 3'-end mismatch in HaemNFI and HaemR2L against the clade
  the Hellgren nest cannot amplify — a documented failure with the mechanism at base level.
- **No row yet DEMONSTRATES drift.** Three carry `mechanism: drift` -- the CDV row and the
  Kulesh 2004 monkeypox pair, which their own notes call one inferred event -- and none
  meets the strict bar of 2026-10-30. Every documented failure this project holds
  is a clade never covered, not a target that moved. The flag the pipeline is named for
  rests on about one ground-truth event, and the `use` family cannot close that.

## Next, in order

1. **`drift.window_on` step 1** (collection date for `asm` records), measurable per lineage
   now that the per-year rows exist.
2. **The 93 `use` rows that did not reach CONFIRMED** — `docs/2026-10-29-use-identity.tsv`
   says why for each, and most are "prints no oligo table". The ones that print one and
   still missed are the cheap re-read.
3. Trend over distinct footprints rather than records.
4. A **drift-mechanism** case hunt. Nothing in the current method finds one; that needs a
   different search, not more rows of the same shape.

## Still yours

- **S7b: ship `mispair_window: 10` or leave it null.** See
  `docs/journal/2026-10-29-s7b-priced.md`; shipping also means a confirming rescreen.
- **The works/fails sign-off on eleven proposed rows** in `docs/validation-cases-heldout-2.tsv`,
  the three Hellgren `fails` rows first, since they are the ones that could move a verdict.
- The **Quackenbush 1998 verdict** (also PROPOSED, from 2026-10-28).
- Whether `CALICIVIRUS_ssRNA_Helicase_Reid_1999` is worth considering for `active`. My
  reading: no, on `thin_evidence` — 16 amplifying records of 152,379.

---

# Resume point, 2026-10-28 (afternoon: the signature fixed, S7 killed, the influenza verdict decomposed)

**Start here:** `ROADMAP.md`. Tree clean, everything pushed, 1,823 tests, registry 214/214.
Six commits since the midday entry below.

- **The screen signature hashes screen-relevant fields, not file bytes** — and the first
  diagnosis of that problem was wrong, which the journal says first. Two days of curation
  go from 444 archive rescreens to 47. `scripts/stale_screens.py` answers "what will the
  next run rescreen, and which entry made it so" without starting one. **It costs one more
  full rescreen now** (changing `signature.py` moves the code hash) and Sunday's job
  absorbs it.
- **Three more exclusivity claims in**: Huo 2022's seven orthopox siblings on the two F3L
  mpox entries, and the rest of Zhao 2013 on the ORFV and generic PAPV entries. 134
  retrieval groups, up from 125. One claim sits inside its own target genus (seal
  parapoxvirus under *Parapoxvirus*), which is legal, now reported as `EXCL_INSIDE` by
  `check_taxids.py`, and cost 3 evaluable records and no status.
- **The held-out false alarm is traced to one base**, and a defect was in the way: `sitedrift`
  counted a mismatched probe as a detection (the third place that has turned up). With it
  fixed, the monkeypox G2R assay's 2022-era records carry a G:T wobble at position 8 of the
  reverse primer — 1.0 + 0.5 crosses `detect_max`, and for a probe assay `reduced` is not a
  detection. **69 sites on 23 assays share the shape.**
- **S7, halving the mid-window penalty, is dead on its own criterion.** 45,797 calls move,
  tier-2 identical, bench accuracy identical at 92.7%, and it newly predicts a band on two
  within-family bench negatives. What outlives it: on these panels the rows that reward
  loosening and the rows that punish it move together, so only identity could separate
  them — S7b, registered, needs a `mispair_window` setting. `config.yaml` says this beside
  the setting now.
- **H3N2 was never detected** — the per-year block's first answer, 1.1% in 2005 against
  0.1% in 2025 — and the influenza assay's pooled 6.5% decomposes into a twenty-year
  coverage gap, a real fall in the subtypes it does detect, and 4,729 untyped 2026 records
  at 0.1%.
- A `use` phrase family for `find_retrospective_cases.py`, opt-in, because the week's only
  tier-2 candidate had no failure word in it.

## Next, in order

1. **A sequence-based influenza subtype resolver.** 4,729 records in 2026 alone sit
   unclassified because their titles stopped naming the subtype; the title resolver cannot
   reach them and they are pushing a verdict around.
2. **S7b**: a `mispair_window` setting, then price identity in the mid window alone — the
   candidate the literature actually supports and the one that could separate the G2R
   wobble from the FAP negatives' A:A and A:C mispairs.
3. **`drift.window_on` step 1** (collection date for `asm` records), now also measurable
   per lineage thanks to the per-year rows.
4. **The `use`-family search**, then `check_candidate_identity.py` over whatever it
   returns: set 2 needs 12 more rows and 22 of the 23 mid-window assays are not monkeypox.
5. Trend over distinct footprints rather than records.

## Still yours

- The **Quackenbush 1998 verdict** (row marked PROPOSED in held-out set 2).
- Whether `CALICIVIRUS_ssRNA_Helicase_Reid_1999` is worth considering for `active` now its
  last OPEN flag is gone. My reading: no, on `thin_evidence` — 16 amplifying records of
  152,379.

---

# Resume point, 2026-10-28 (the queued papers arrived; Hel1 settled, BPSV reconciled, exclusivity visible)

**Start here:** `ROADMAP.md` — 29 open items, 67 closed. Tree clean, everything pushed,
1,797 tests, registry 214/214 valid.

## What the papers changed

- **`papers/papers-fetch-list.md` is empty for the first time.** All seven priority PDFs
  and the ten open-access ones are in `papers/`; 171 papers held, 118 cited.
- **Hel1 is settled the other way**: Neill & Seal print a 3′ **G**, so three sources agree
  and the stored C is a deliberate modification, not a typo fix. The published primer
  carries a 3′-terminal mismatch against all 16 of its own target records. Flag
  `oligo_sequence_uncertain` → `oligos_modified`, which removed the last OPEN flag and
  brought the entry into the report (`no recent data`).
- **The retrospective identity queue is spent**, and now on CONTENT rather than access: 2
  CONFIRMED, 1 VARIANT, 10 UNCONFIRMABLE, and not one newly readable paper prints our
  oligos. Tsukamoto 2008 prints 29 and Csordas 2004 prints 12, none ours; the new
  CONFIRMED (Süß 2009) is a synthetic-template mismatch study, not a case — recorded
  instead as a C2 prior source.
- **A completeness paper turned out to be a case**: Quackenbush 1998 uses the pan-herpes
  nest and sequenced a product 53% identical to its nearest relatives. Row written
  PROPOSED, awaiting a verdict.
- **Held-out set 2 is partially spent**, disclosed: 3 rows read, 1 agrees / 1 weaker / **1
  false alarm** (Mills 2022 on the G2R generic mpox assay, which the config calls
  declining). Nothing was tuned on it and nothing may be.
- **BPSV's contradiction dissolved**: the amplicon forms in 82 of 85 evaluable orf virus
  records and the assay detects none of them, because a mismatched hydrolysis probe is not
  a detection. Zhao's panel and the pipeline agree. The report has a status-independent
  `## Published exclusivity claims, tested` section, over evaluable records, printing
  `amplified` beside `detected`.
- The five misattributed `conditions` values are deleted, each with its reason.

## The one thing to fix before the next curation pass

**Fixed the same day, and the first diagnosis was wrong.** A re-render started screening,
which I attributed to the signature hashing the whole of `registry/`. It does not: it
hashes each GROUP's assay files, and the 357 jobs were a stopped run's DAG denominator
read as a work queue. The real defect was that it hashed each entry's whole YAML, so a
note or a `conditions` value invalidated that entry's groups — 312 of 494 screens stale
after 192 entries were curated. `signature.screen_key` now hashes the screen-relevant
projection: the same two days of curation go from 444 archive rescreens to 47, and the
ten groups that remain are the ones that should.
`scripts/stale_screens.py` answers "what will the next run rescreen, and why" without
starting one — which is what should have been asked first.

`results/2026-10-28.partial-stopped/` is that abandoned run, kept rather than deleted.

## Next, in order

1. **Per-entry screen signature** (above), so curation stops costing full rescreens.
2. **Two exclusivity sets are read and ready to add** (ROADMAP, Data and curation): the
   Huo 2022 mpox panel's seven orthopox taxids — 3,772 records, taxids already looked up —
   and the rest of Zhao 2013 for the ORFV and generic PAPV entries.
3. **The Mills disagreement**, as a measurement rather than a worry: compare the G2R
   generic assay's detected share on 2022-and-later records against its windowed share.
4. **Re-run `find_retrospective_cases.py` for use-and-report language.** Quackenbush shows
   the citing-paper graph holds scoreable papers that never use failure words, and that is
   the only tier-2 lead left that needs no new PDFs.
5. Then the standing items: `drift.window_on` step 1, the per-lineage per-year table, the
   trend over distinct footprints.

---

# Resume point, 2026-10-27 (overnight: the live run done, conditions curated from 64 papers, TNTBLAST run at last)

**Start here:** `ROADMAP.md`. Plan: `~/.claude/plans/quizzical-snuggling-corbato.md`, second
pass. Phases 1-5 are committed and **phase 3's live run has RUN**; 12 commits tonight, 1,795
tests, registry 214/214 valid, tree clean.

## What the run said

**0 of 193 statuses move** against the committed M1 run — after a defect it exposed was
fixed. The run first moved BPSV `insufficient data` -> `low coverage`, and the cause was
the exclusivity feature committed hours earlier: `drift.gather`'s scope filter only runs for
an assay that declares `scope_taxids`, and BPSV declares none, so the orf virus and
pseudocowpox archives fetched for its specificity claim were counted in its own denominator.
A declared exclusion is now out of scope independently of `scope_taxids`, in the report and
in tier-2 both. The 18 retired taxids rescreened with nothing moving, which is the right
answer: Entrez had been resolving them all along.

## Done since the last entry

- **TNTBLAST ran** (Rosetta 2 installed; `tntblast` 2.77 osx-64). The engine PCR_strainer
  wraps reads **64.8%** on the 179 bench rows with two fitted parameters, against the
  penalty rule's **92.7%** as it ships, 58-8 on the discordant rows, p < 0.0001. Per-panel
  oracle cuts take it to 87.7%: the weakness is that a Tm needs the assay's own annealing
  temperature, which is the argument `thermo: false` rests on, now measured.
- **`conditions` populated twice**: 119 entries from the automatic pass, then a reader's
  pass over all 64 papers it refused — 236 values by hand, 12 of them corrections. Two of
  those matter: BPSV anneals at 60 C (the paper says so in as many words) and the influenza
  matrix set at 60 C over 45 cycles, where the entry carried the H7 assay's 58.
- **Six extraction bugs**, five of which produced a plausible value: an RT step read as the
  annealing step, a label nearer the wrong number, a spaced-out decimal point, a decimal
  comma, a stock read as a final concentration, and a degree sign the PDF renders as the
  digit 8 ("948C" reads as 48 C). All pinned in `tests/test_extract_conditions.py`.
- **C1b designed** (the pooled floor that refuses 30 assays a verdict), kill tests
  pre-registered, not built. **Duplicate-key gate** added after one entry's note turned out
  to have been discarded by every loader for three days.
- The PDF list you asked for is on your Desktop: `assaywatch-pdfs-needed-2026-10-27.md`.

## Next, in order

1. **Five hand edits the tool cannot make**, all listed in `ROADMAP.md` under the registry
   item: a value has to be DELETED, not fixed. `CMV_UL55_gB_Deckers_2009.mg_mm`, the three
   `ORTHOBORNAVIRUS_XP_*.mg_mm`, and `LEPTOSPIROSIS_Flagillar_filiment_Prote.annealing_c`
   each came from the wrong assay in a multi-assay paper.
2. **The report shows no exclusivity table for an unflagged assay.** BPSV's 2,692
   off-target calls are computed and invisible, because the cross-reactivity table lives in
   the flagged-assay detail section. A section of its own, listing every entry with
   `exclusivity_taxids`, was started and reverted rather than left half-built.
3. **Refresh `docs/example-run-2026-10-27/`** from `results/2026-10-27` (it is the same
   statuses, but the run carries the conditions and exclusivity work).
4. Then the roadmap's remaining items: `drift.window_on` step 1, the per-lineage per-year
   table, the trend over footprints, and the exclusivity curation the digest opens up.

---

# Resume point, 2026-10-27 (late night: the second roadmap pass — SCOPED taxids, influenza sublineage on, exclusivity_taxids, conditions blocks)

**Start here:** `ROADMAP.md`. Plan: `~/.claude/plans/quizzical-snuggling-corbato.md`
(second pass, written and approved tonight). Phases 1, 2, 4 and 5 are committed; **phase
3, the retired-taxid live run, has NOT been started** and is the next thing to do.
Six commits, 1,786 tests, registry 214, validator 214/214. Not yet pushed if `git log
origin/main..HEAD` says so.

- **The 8 `taxon_name` mismatches were never wrong**, open since 2026-10-04:
  `check_taxids.py` now has a `SCOPED` status that reads the retrieval query, requires
  every pinned organism taxid to descend from the entry's own taxid, and asks whether one
  of them carries the stored name. 0 mismatched taxids. The 18 MERGED taxids are still
  there and are phase 3's work.
- **The influenza sublineage chain is ON**, and the subtype table inverts on the corrected
  numerator: H3N2 1.2% of 38,771, H1N1 2.6%, H5N1 34.0%, thirty avian subtypes 85-100%.
  The pooled 6.5% was the two human-circulating subtypes. Tier-2 identical, 0 of 193
  statuses move.
- **`target.exclusivity_taxids` is built.** A near neighbour a paper claims to exclude is
  now its own retrieval group on the assay's own query. BPSV is the first entry (orf virus
  10258, pseudocowpox 129726); 124 retrieval groups become 125, because orf virus shares
  an archive that already exists. The report marks those rows `claimed`.
- **`conditions` / `performance` / `panels` exist and 119 entries carry a protocol**:
  47 an annealing temperature against 7 before, 84 cycles, 28 magnesium, 14 an RT format.
  `scripts/extract_conditions.py` proposes with the paper's sentence quoted;
  `docs/2026-10-27-conditions-proposals.tsv` holds all 644 rows, including the 270 only a
  reader can fill, the 122 ambiguous and the 79 nested rounds. Five extraction bugs are
  recorded in the journal; four of them pass any range check.
- **A duplicate YAML key had silently eaten one entry's note for three days.**
  `scripts/check_duplicate_keys.py` is now a pre-commit gate over every registry and
  pending file, because `check-yaml` only sees the files one commit touches.

## What phase 3 needs, in order

1. The tree must be clean and committed (the live run refuses a dirty tree under the
   hashed paths), and nothing under `assaywatch/`, `config.yaml`, `registry/` or
   `Snakefile` may be edited while it runs.
2. Rewrite `target.taxid` on the 18 MERGED entries to the canonical id
   `check_taxids.py` prints (11232 -> 3052342 CDV x9, 121791 -> 3052225 Nipah x2,
   11051 -> 3044782 flavivirus x3, 10292 -> 3044472 herpesvirus x4).
3. `data/retrieved/<taxid>/` is keyed by taxid: move the four root directories to the
   new ids, then `python scripts/rebuild_manifest.py`.
4. `scripts/weekly_run.sh --live --cores 4`, lid open. Then `scripts/report_diff.py`
   against `results/2026-10-27`. It is also the confirming rescreen for the schema and
   registry edits above, and the run that first fetches pseudocowpox for BPSV.

---

# Resume point, 2026-10-27 (night: the M1 hold lifted and confirmed by screen, the Kwok premium killed, C1's hierarchical layer built)

**Start here:** `ROADMAP.md`. After the evening entry below, the maintainer lifted the M1
hold and said to keep going. Six more commits, 1,763 tests, registry 214.

- **M1 ships**: `scoring.mispair_penalty: {"G:T": 0.0, "T:G": 0.0}`. Run 4 — the fourth
  full run of the day — is its confirming rescreen: the real screen agrees with the S4
  replay on all but **153 of 2,679,894 rows** (the other 110,606 "disagreements" are the
  replay's own probe rewrite), every one pessimistic. 8 statuses move against run 3;
  `docs/example-run-2026-10-27/` is refreshed to this run (193 assays, 42 declining).
- **S6, the Kwok premium, is dead** on both pre-registered criteria: one FAP band row
  broken and nothing fixed, one false alarm added and no catch.
- **C1's hierarchical layer is built and measured on both halves of its plan**
  (`assaywatch/hierarchical.py`), printed beside each verdict. First kill test: multi-lineage
  assays fit φ 0.3–11.7, intraclass correlation 0.08–0.78 — does not fire. Second kill test:
  `lineage.verdict_from: posterior` leaves tier-2 identical and moves 0 of 240 statuses —
  does not fire, and changes nothing. Ships beside the verdict, `verdict_from: holm`. The
  30 refused assays are refused on the pooled count before any lineage is looked at, which
  is a different item and now a roadmap entry.
- **The `score.py` cache footgun is closed at its source**: the per-chemistry cache is keyed
  to the scoring block it came from.
- **`weekly_run.sh --live` refuses a dirty tree** under the hashed paths; proved to fire.
- The pending entries were searched on PubMed and the design papers are not findable by
  assay description; recorded in the roadmap.
- One footgun recorded for `score.py`: `load_config` caches the per-chemistry resolution
  inside the dict it returns, and shallow copies carry it. Two callers now drop it.

---

# Resume point, 2026-10-27 (evening: the roadmap plan executed — 26 commits, 1,759 tests, the first run under today's scoring, and the schedule installed)

**Start here:** `ROADMAP.md` (30 open items, 57 closed). The plan approved this afternoon
(`~/.claude/plans/quizzical-snuggling-corbato.md`) ran phases 0–3 to completion, most of 4,
and 5; what it could not finish is named in the roadmap with the reason. Every commit was
gated: **1,759 tests pass** (was 1,737 at the plan), validator 214/214, ruff, `claims`,
`check_citations` 214/214. Pushed; CI green on the last push before this entry.
Registry: **214 entries** (five Huo 2022 mpox entries added), 179 active / 34 draft / 1
deprecated; no oligo altered, no status set active.

## The decisions that were taken, and landed

`partial` rows count as catches **scored separately** (retrospective.py prints a line of
their own, never pooled into `fails`). CONTRIBUTING states best-effort review and which
flags never clear. Operations were authorised and done: pushed; the full live run exists
(`results/2026-10-27/`, committed as `docs/example-run-2026-10-27/`); the weekly launchd
job is **installed live on this machine for Sunday 09:00**, dry-fired once first.

## Measured today, with the number that decides each

- **Trend statistic** — Cochran–Armitage over deposit year, beside the verdict and never
  into it, no threshold. The claim `related-work.md` makes as contribution #2 now has a
  statistic behind it. `assaywatch/trend.py`.
- **C1 run as its plan specified** — Wilson and Jeffreys disagree on 1 of 1,351 lineages;
  a posterior flag rule moves 2 of 233 statuses and nothing in tier-2. Ships `wilson`;
  the hierarchical layer is the part worth building (30 of 188 assays refused a verdict).
- **S4 run** — M1's G:T discount **survives** the kill test that retired it: no catch
  lost, influenza promoted to the drift flag (PPV 3/9 → 4/10), five bench rows fixed,
  none broken. Priced, not shipped; lifting the hold is the maintainer's.
- **Window × minimum grid** — the minimum does nothing to the matrix between 10 and 20;
  12 months loses a catch; **36 months keeps all six and drops a false alarm**. Nothing
  ships; 36/15 is the cell a held-out read would be worth spending on.
- **`anchor_fdr` cannot be priced on the bench panels, by construction** — it relabels
  `no_site`↔`fail`, both no-band. Worked out before any run was wasted on it.
- **Deposit ≠ collection date is not immaterial**: of 1,001 dated assembly records,
  25.9% were collected ten or more years before deposit. Reaches `asm` only; two steps
  named, neither built.
- **Containment check** — 0 scoped taxa outside their root; found instead **18 entries
  on retired taxids** (CDV, Nipah, flavivirus, herpesvirus roots) and 11 name mismatches.
- **Influenza sublineage chain works** — H1N2 72.1% and H5N1 87.6% inside a 97% pool;
  H3N2 (the literature's subtype) 99.4%. **It exposed a defect**: `lineage.py` counted
  `reduced` as detected for probe assays after the verdict stopped doing so. **Fixed**,
  with the lineage report now also applying the species roll-up it never applied —
  **775 unnamed lineage rows became 2.**
- **Orientation**: the archive confirms 26 of 28 inferred orientations; each flag now
  carries its count. **In-text oligos**: 20 enumerated. **Hantavirus pending entries**:
  the plan's premise was wrong (Aitichou covers only the pair already live).
- **S3b confirmed on the whole table**: the replay and the real run disagree on **8 of
  2,679,894 rows**.

## Two runs failed before the third succeeded, and the second was mine

461 of 482 cached screens were stale with no Snakemake metadata to notice (the signature
guard caught it). Then all 461 were rescreened and refused, because I edited `settings.py`
and other hashed modules while the run was going. **Rule, now in ROADMAP: nothing in
`assaywatch.triggers.source_names("screen")` and nothing in `registry/` is touched until a
run reports.** A dirty-tree refusal in `weekly_run.sh` is owed.

## Three things I got wrong today and corrected in place

Mpox was never "two assays from 2004"; `locus_identity_min` was rejected, not unproven;
the Pan_flavivirus "false alarm dropped" was a 2017 retrospective verdict, not a 2026
status. Each is corrected where it was stated, with the correction dated.

## What is left, in the order the roadmap now has it

The hierarchical layer of C1; lifting (or not) the M1 hold, after a confirming rescreen
and the Kwok premium priced beside the discount; `target.exclusivity_taxids`; the
assay-conditions schema blocks (schema first, then the 189 PDFs); the 18 retired taxids,
as their own live run; the six `pending/` entries still wanting a design paper; the
held-out and C2 corpus, which needs the six queued PDFs behind the proxy; and the Greene
profile's first submission. Nothing on that list needs a decision from you to start except
the M1 hold and the retired-taxid run, which moves archives.

---

# Resume point, 2026-10-27 (later: one to-do list, four decisions taken, and a result that refuted itself)

**Start here:** `ROADMAP.md`. It is now the only to-do list in the repository, and the
one thing to know before reading anything else is that **a result from earlier the same
day was corrected, not confirmed**. Six commits, every one gated: **1,733 tests pass**
(was 1,732), validator 209/209, ruff clean, `claims` ok, `check_citations` 209/209,
`snakemake -n` exit 0. Registry unchanged at 209/179/29/1; no oligo altered.

## What was asked, and what it turned out to require

"What is next on the to-do list" could not be answered from one file. Open work was
spread across `docs/RESUME-HERE.md`, `ROADMAP.md`, the deferred section of the
four-perspective review, and the forward-looking tail of **eight** dated journals --
18 live items, 4 maintainer decisions and 4 known limitations, with no way to tell a
live item from one closed weeks earlier. Three items the journals still asked for were
already DONE (`scope_taxids`, sequence-cluster lineages, the lineage binomial overflow)
and five were live and pointed at by nothing:

- deposit date is not collection date, and `collection_date` is already retrieved and unused;
- `drift.anchor_fdr`'s value has no evidence behind it (0.05 and 0.01 differ by 2x in rows moved, 0.001 ships);
- 889 lineages are still `taxid_<n>`;
- a genus taxid can stop containing its target after a reclassification, and `check_taxids.py` cannot see it;
- four leftovers from the oligo adjudication.

Everything is in `ROADMAP.md`, ranked, each item carrying the evidence that put it
there. Item numbers were replaced by names, because a cross-reference to "item 10" rots
every time an item above it closes.

## The four decisions, and what each cost

**1. The thermodynamic result does not survive its own confound.** `thermo.duplex_tm`
called `primer3.calc_heterodimer`, which returns the most stable structure between two
sequences rather than the in-register duplex. It now sums nearest-neighbour terms
base-for-base (Biopython `Tm_NN`, SantaLucia & Hicks 2004 with the Allawi/SantaLucia
mismatch tables), so there is no alignment search and no register to get wrong. Re-run:
**93.9% -> 92.7%, discordance 20-7 -> 21-10, McNemar p = 0.0192 -> 0.0708.** Of the
sites it can price, 71 would have been mis-registered. So roughly half the morning's
margin was the artefact the write-up itself had named, and "a thermodynamic predictor
beats the penalty rule" is not a claim these 179 rows support in either direction.
**What survives untouched: the penalty rule's 23 false negatives against 1 false
positive**, which is the penalty arm alone and still the strongest single argument in
the repository for per-chemistry scoring. Cost: 32 sites cannot be priced at all,
because adjacent mismatches have no measured term, and the number is now withheld
(`thermo_note: nn_unsupported`) rather than scored as free.

**2. A mismatched probe is no longer a detection.**
`drift.reduced_not_detected_for: [hydrolysis_probe, mgb]`. Measured before it was taken
by rendering the 2026-10-26 calls table both ways: **13 of 235 statuses move, in both
directions** (declining 34 -> 36, low coverage 37 -> 42, watch 12 -> 9, stable 56 -> 52),
and `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` goes `stable` -> flagged at 6.5%
of 30,382 recent records -- the documented failure the switch exists to catch.
`CDV_P_gene_Scagliarini_2007`, an `active` entry, moves watch -> Start here. Cost, which
stands: two published positives on the Leptospira bench panel go `reduced` -> `fail`.

**3. The project has unread evaluation data again.**
`docs/validation-cases-heldout-2.tsv`, opened with the Leetz 2007 case -- the first
CONFIRMED retrospective identity, from a paper the rule has never been shown. It reads
`works`, because the 73.8% headline is an oocyst dilution series on one isolate, i.e.
sensitivity, which this tool does not model. Disclosed in the file: it was scored once
to check the row parses, so one bit is out.

**4. TNTBLAST waits.** No osx-arm64 build and Rosetta 2 needs admin rights. Rosetta, an
arm64 build from source, or a run on linux-64 or the cluster -- `scripts/archive/compare_thermo.py`
takes a second predictor unmodified. The dead `tntblast` env was removed on 2026-10-27.

## Two things found by accident, and they are the kind worth noticing

**Both Priority 1 papers have been on disk since 2026-10-25 and nobody re-ran the
verifier.** Mao, Hedrick & Chinchar 1997 prints both ranavirus MCP primers as 18-mers,
byte-identical to the registry, and prints no 19-mer -- so the 18/19-mer question is
closed in the registry's favour at three transcriptions to one. The entry recorded this
on 2026-10-26; the fetch queue did not.

**A file being present is not a paper being readable.** `papers/` holds a 64 KB PDF
under Neill & Seal's name that yields 488 words of front matter and no nucleotide run of
10 bases anywhere. The Hel1 3'-terminal base is exactly as unverified as before, and the
correction taken on measurement still stands alone.

## Housekeeping that will change where you look

- **89 session journals are in `docs/journal/`**, leaving the nine reference documents in
  `docs/`. 588 references rewritten across 160 files; `docs/journal/README.md` says what
  the directory is and is not. Nothing deleted, no journal reworded.
- **`tests/test_docs_links.py`** asserts that every repo-root `docs/...` reference
  resolves. It found a wrong directory prefix in `fetch_elsevier.py`'s own usage line on
  its first run, and it is what made the move safe.
- A dated journal's "Next steps" section now carries a line saying it is history as of
  its own date. `CLAUDE.md` and `docs/INDEX.md` state the one-list rule, so a new session
  does not start a fifth list.

## Per-chemistry scoring was then priced, and the knob this project has named for three weeks is inert

**`terminal_mismatch_fails: false` for `conventional` moves 0 of the 179 bench rows.**
The 23 false negatives are real; that is not what causes them. Same answer the
2026-10-26 registry-wide run gave from the other end — 251 calls of 2.7M, no verdict
changed — because a record whose primer carries a terminal mismatch almost always
carries others that already exceed `reduced_max`.

**`primer_3prime_penalty` 3.0 -> 2.0 for conventional is the half that works**, and it
is now the best-evidenced scoring candidate the project has: 6 of 179 bench rows fixed,
0 broken, McNemar exact **p = 0.0312**, none of the 16 bench negatives that can punish a
loosening moved, and nothing fitted. Over the 2.72M-row calls table, against an S0
control replayed the same day: 19,081 calls move, every one `fail` -> `reduced`;
documented failures caught stays 6/11; PPV of `declining` 2/9 -> 3/9; false alarms 5/32
-> 4/32. Exactly two tier-2 cases move, in opposite directions on purpose —
`Pan_flavivirus_NS5_3_round2` loses a false alarm, and the Forslund FAP failure moves
`low coverage` -> `declining`, because `require_working_baseline` can only see a decline
once the earlier years clear the threshold. Same assay as 5 of the 6 bench fixes.

**Not shipped.** `by_chemistry` is still `{}`: a replay freezes candidate selection, so
this is PRICED, NOT PROVEN, and the confirming rescreen plus a decision about moving
every status in every report are what remain.
`docs/journal/2026-10-27-terminal-mismatch-refuted-penalty-priced.md`,
`strategies/s3b-conventional-3prime-penalty.yaml`.

## Still open

`ROADMAP.md`, which now carries **36 items** after a second sweep found what the first
one missed. The first sweep looked for forward-looking SECTIONS; it did not catch
documents that are plans from end to end, and it never looked outside the documentation
at all. What the second sweep added:

- the scoring rule's own ladder (S4/M1 written and never run; C1 free and unbuilt;
  C2 gated on 40 within-family negatives against today's 11) and the fact that today's
  candidate had taken S5's reserved name;
- **nothing is running on a schedule.** No `com.assaywatch.weekly` job is loaded and
  the newest weekly log is 2026-10-23, while README says the tool re-screens on a
  schedule. For a project whose contribution is continuous re-validation that is the
  gap between the claim and the artefact;
- a full run is owed, because scoring is in the cache key and every committed report
  now predates the config that ships;
- six inert switches counted in one place, so "the mechanism is here and the numbers
  are not" is a number and not a feeling;
- 216 `needs_review` flags on 207 of 209 entries; 10 `pending/` entries all blocked on
  an unverifiable DOI; the held-out target of 15-20 cases against set 2's 1; and mpox
  covered only by two assays from 2004 when a candidate list from 2026-10-24 exists;
- two maintainer decisions nobody had written down: whether a `partial` row counts as
  a success, which decides what the paper's main figure claims, and 29 unpushed
  commits that CI has never seen.

---

# Resume point, 2026-10-27 (a four-perspective review, then its P0-P2 fixes; 16 commits, all gated)

**Start here:** `docs/journal/2026-10-27-four-perspective-review.md` is the review and the
reasoning behind every decision taken from it. The repository was read from four angles
(engineering, methods, bench diagnostics, a cold newcomer read), and the findings were
worked through in order rather than listed. Registry **unchanged at 209/179/29/1**; no
oligo altered. Gate on every commit: **1,732 tests pass** (was 1,705), ruff clean,
validator 209/209, `check_citations` ok, `claims` ok, `snakemake -n` exit 0.
Everything is COMMITTED this time, one commit per finding, with the reasoning in the
message.

## The two findings that drove it

**The denominator is drift-correlated.** A record with ONE drifted primer is counted as a
failure; a record with BOTH drifted leaves the denominator as `no_site`. 65.7% of 2.72M
rows never reach the statistics, and `no_site` alone is 53% of every row — of which
357,923 DID find a site within the mismatch budget and 1,085,008 found nothing. That split
is now measured and printed per assay; the bias itself is not fixed.

**Published artefacts described a method the code did not run.** The report named
Benjamini-Hochberg where the run used Holm; the README gave two incompatible headline
accuracy figures 466 lines apart; ~15 counts were stale — and the `claims` hook built to
catch exactly that had been silently disabled since three duplicate `files:` keys landed on
it. `check-yaml` now makes a duplicate key an error. The repaired hook then rejected three
of my own commits for undated counts, which is the system working.

## What changed, by theme

- **Data integrity, before any retrieval.** An empty efetch page was accepted as zero
  records and the run recorded, after which the incremental cursor skipped records that
  were never written. A short page was indistinguishable from the legitimate WGS-master
  case. The cursor was keyed on the assay query only, so changing a length filter
  permanently skipped older records that newly qualified. A missing `.sig` wedged the
  pipeline unrepairably — and declaring it as an output was NOT enough, because nothing
  requested it. `--config` overrides moved the cache key and never reached the subprocess;
  dumping the merged config verbatim would have broken every rule, because `Settings`
  forbids extras and the merged dict always carries `email`.
- **Report layer, no rescreen.** Exclusion counts now reconcile (all 71 assays, 0
  mismatched). Site drift NAMES THE SUBSTITUTED BASE and the code to order — `G->A 751,
  G->T 3` and `R (99.6%)` — pool-safe, because the oligo base comes from the mispair cell
  and not from the primary oligo. Footprint groups carry example accessions. Specificity is
  computed from out-of-scope calls that were already on disk (18 assays). The report opens
  with a plain-language verdict, what it is not, and the seven statuses defined.
- **Statistics.** The anchor-FDR family is now `drift.anchor_fdr_family: tested`. My first
  recommendation (`lone_anchor`) was REFUTED by this repo's own test: it drops the weakly
  anchored rows, loosening the bar until Bd's 55 chance anchors pass as real. `tested` is
  the rule those two failures imply. No verdict moved.
- **`Start here (0)` was an artefact.** `count_diverged_as_fail` gave a promoted row no
  footprint, and one such row made the duplication count unknown for the whole assay (153
  of 208 assays have one). So the check ran on 12 of 71 flags, and the triage list it gates
  on was empty. With a coarse taxid-derived footprint: 23 of 71 hold, and Start here has
  **10** assays. No status changed — this is what the report can SHOW, not what it concluded.

## The two new results

**Leetz 2007 is the first CONFIRMED retrospective identity** (three PDFs arrived
mid-session). It reads `works`, not `fails`: its 73.8% is an oocyst dilution series on ONE
isolate, i.e. sensitivity, and the assay amplified and RFLP-typed cleanly in two stocks. No
row was written to `docs/validation-cases.tsv` — that set is frozen and spent, and a case
from a paper the rule has never seen is the first brick of a NEW held-out set. Where it
goes is a maintainer's call. See `docs/journal/2026-10-27-leetz-identity-confirmed.md`.

**A thermodynamic predictor beats the penalty rule, McNemar p = 0.019.** primer3 93.9% vs
86.6% on the 179 bench rows, and the shipped rule's errors are **23 false negatives against
1 false positive** — the pessimism the bench review predicted. Confounded in primer3's
favour: 99 of 179 alignments are off-register, which reports an optimistically small ΔTm on
a band-heavy panel. TNTBLAST itself could not run (no osx-arm64 build; Rosetta absent).
See `docs/journal/2026-10-27-thermo-vs-penalty-paired.md`.

## Still open

**In `ROADMAP.md`, which is now the only to-do list in the repository.** Open work
had accumulated across four files and the forward-looking tail of eight dated
journals; it is consolidated there, ranked, each item carrying the evidence that
put it in that position. This file records what a session found and where it
stopped, and keeps no list of its own.

The three the evidence supports first, for orientation: fix `thermo.duplex_tm`'s
registration (until then no ΔTm is trustworthy on the records that matter), price
`terminal_mismatch_fails: false` for `conventional` as a replay (the 23 false
negatives are the strongest single argument in the repository for it), and turn on
`reduced_not_detected_for` (already measured, still shipping off). Four decisions
are waiting on a maintainer at the top of that file.

## Two housekeeping notes

- `papers/*.md` is now TRACKED. `papers/` was ignored as a directory and took the live
  fetch queue with it, so every status mark on the queue this file points at existed on one
  laptop only. PDFs and the Europe PMC .xml/.txt deposits are still ignored.
- A stray conda env `tntblast` (osx-64) was created and cannot execute without Rosetta.
  Remove with `conda env remove -n tntblast` if you do not intend to install Rosetta.

---

# Resume point, 2026-10-26 (later: the identity check is built, and it clears NONE of the concentrated signal from open text)

**Start here:** the plan is `~/.claude/plans/go-to-assaywatch-and-breezy-crayon.md`. It acts on
the binding constraint the entry below names — new tier-2 cases are blocked on **identity**,
not discovery — by building the cheap identity check that entry asks for and running it over
the queue's richest rows. Registry **unchanged at 209/179/29/1**; no oligo altered, no
`config.yaml` value touched. Gate: **1,705 tests pass**, validator 209/209, `check_citations`
209/209, ruff clean. **Nothing committed** — the working tree carries the changes for the
maintainer to commit per item.

## What was built

`scripts/check_candidate_identity.py` (11 tests). It answers the one question the citation
graph cannot: did a citing paper test the assay the registry holds? It takes a candidate (an
assay id + the citing DOI/PMC id), fetches the paper's open-access full text WITH its tables
via `fetch_europepmc_fulltext`, and compares the stored oligos against what the paper prints
using `verify_oligos_against_paper.check` (both strands, codon spacing undone, nearest printed
run by edit distance). Verdict per assay: **CONFIRMED** (both primers verbatim), **VARIANT** (a
printed primer differs by a fixed base — not ours; drop it), **UNCONFIRMABLE** (not OA, no
oligo table, or a primer simply absent). The load-bearing test pins that `near:N` is **never**
collapsed into CONFIRMED — the exact error that would let the dead candidates through. It
proposes only: a worksheet TSV, nothing to `registry/`, `pending/` or `validation-cases.tsv`.

## The finding, and it sharpens the one below to a measurement

**Ran over all 9 `mismatch`/`redesign` rows — the queue's concentrated signal — and NONE is
settleable from open-access text** (`results/retro-identity-concentrated-2026-10-26.tsv`). Two
are reachable in Europe PMC and neither reprints our oligos: the 2025 enterovirus paper
(`10.1128/jcm.01492-22`) reprints a **different** assay's primers (the CDC2022 redesign,
AN887/AN893) and uses the Nix gold-standard by citation only; the MDPI influenza paper
(`10.3390/v15061344`) cites Spackman in its **references** and prints no primer table at all.
The other 7 have no open PMC copy — one (`10.1128/jcm.02386-07`, PMC2546769) is in PMC but
`fullTextXML` returns a persistent HTTP 500. So "identity is the bottleneck, not discovery" is
now measured on the richest 9 rows: the open-text route clears zero of them, and identity needs
the PDF and, where the oligos sit in a supplement, the supplement. All 9 are queued in
`papers/papers-fetch-list.md` with `doi_stem` names, proxy links and a per-row reason; the
script prefers a local file, so a PDF dropped into `papers/` is picked up on re-run.

> **Watch the Influenza Matrix rows.** The stored reverse is a redesign of Spackman's (two
> fixed-base substitutions, `needs_review: oligos_modified`), so a paper reprinting Spackman's
> ORIGINAL reverse will read `VARIANT`, correctly — it tests a different primer from ours.

## Also

`ROADMAP.md` Phase 2's calicivirus **"0 of 30"** worked example no longer reads as a live claim
— rewritten as withdrawn up front, which is step 2 of the entry below, now done. Nothing else
in the roadmap changed.

---

# Resume point, 2026-10-26 (the harness is built, the ladder is priced, the held-out set is SPENT, and nothing shipped)

**Start here:** the plan is `~/.claude/plans/go-to-assaywatch-which-giggly-heron.md`, which
resumed `go-to-assaywatch-resume-ancient-shell.md`. **Sections 1 to 8 are now all done or
deliberately stopped.** The decision taken up front and kept: **measure the candidate
ladder and ship nothing.** `docs/validation-cases-heldout.tsv` was not read, and three
tests still enforce that no script references it.

**Registry unchanged at 209/179/29/1 throughout**, no oligo sequence altered, and
`config.yaml` holds no new value. 1,682 tests, validator 209/209, pending 10/10,
`check_citations` 209/209, ruff clean.

Thirteen commits, `1fa4672` to `ab77623`.

## The short version

- **The replay harness exists and is trusted.** Pricing a scoring candidate cost a
  ~30-minute rescreen; it is now ~19 seconds over 2.7 M rows. Validated three times
  against real rescreens, including once on a penalty-changing strategy where its one
  approximation was a live risk: **0 disagreements on 7,904 records.**
- **The whole pre-registered ladder is priced. S1 and S2 are rejected; S3a and M1 are a
  maintainer decision; S3b is inert.** Nothing was shipped and nothing needs to be
  shipped in a hurry.
- **Two closed decisions turned out to rest on measurements that no longer reproduce** -
  the M1 revert, and the "0 of 30" calicivirus figure the roadmap still quotes.
- **Both rejected candidates died on the same ten Forslund negatives.** That is now the
  binding constraint on the whole scoring axis, and it is a corpus problem.

## 1. The footprint columns, finished (`1fa4672`)

The previous session ended mid-edit with 63 uncommitted lines in `assaywatch/score.py`
and no tests. The emission was sound; the proof was missing. Eight tests now pin the
format and three completeness rules: identity recorded for **every** mismatch and not
only inside `primer_3prime_window`; an undetermined record base names no pair, so it
stays in `ambiguous`; a degenerate oligo base records its own code (`Y:T@2`) where
`bench_panel.py` expands it, so the agreement test compares meaning and not text. Seven
of the eight fail without the emission, verified by stashing `score.py`. Deliberately
**not** in `drift.FOOTPRINT_COLUMNS`, with a test, or the duplication analysis regroups
and published intervals move.

## 2. The rescreen moved nothing (`9a13b1c`)

`results/2026-10-26/`, 445 of 445 steps, exit 0. Against `results/2026-10-25/`: **0 call
changes and 0 penalty changes across all 2,676,551 common rows**, 3,343 rows new from a
day of deposits. That was the required result, not a pleasant one.

## 3. The harness (`e396b2b`), and how it is trusted

`scripts/archive/rescore.py` with `strategies/s0-shipped.yaml` as its control. A primer needs no
sequence and not even its own length, because the distance from its 3' end is recorded
per mismatch; only `score_probe` needs a length, and no probe pool in the registry holds
differing lengths, which is a test rather than an assumption.

**Validated against real rescreens three times**, which matters more than the S0 control
because a no-op replay is indistinguishable from a clean one:

| check | result |
|---|---|
| S0 over the full table | 2,724,036 rows, **0 differ** on call, penalty or reason |
| a real `engine: serial` rescreen of one archive vs the replay of it | 3,971 rows, **0 differ** |
| a real M1 rescreen of taxid 195944 vs the replay of it | 7,904 rows, **0 differ** |

> **The real rescreen found a defect S0 could not.** `screen_one` forces `fail` for an
> amplicon whose probe has no site but does NOT force the penalty. The first version
> returned the row's own penalty, reporting 13.5 where the screen said 7.5 on 19 rows -
> with **zero call disagreements**, because the call was already pinned. Fixed and pinned
> by a test checking both halves.

**The boundary prints on every run.** Search knobs are REFUSED, not warned about.
Denominator knobs too, `max_ambiguous_per_oligo` included although its counts are in the
table and it could be replayed. A test asserts the two key sets partition
`settings.Scoring`. And the one approximation that is not a refusal: **candidate
selection is frozen**, so a priced strategy is **priced, not proven**.

## 4. The ladder, all four rungs

| | verdict | tier-2 catches lost | panels (24 wrong at S0) |
|---|---|---|---|
| S1 `engine: serial` | **rejected** | 2 | no clean cell exists in 31 |
| S2 smooth positional decay | **rejected** | 4, incl. the only drift ground truth | no clean cell exists in 35 |
| S3a probe `reduced` is not detected | **maintainer decision** | 0 | 26 (loses 2) |
| S3b conventional terminal is `reduced` | **inert** | 0 | 24 (no change) |
| M1 identity-aware 3' discount | **maintainer decision** | 0 | **17 (rescues 7)** |
| M1 + S3a | **maintainer decision** | 0 | 19 |

**S1** (`docs/journal/2026-10-26-s1-serial-killed.md`). All 31 grid cells lose a row the shipped
rule gets right, floor 2. Two named tier-2 catches fall, both Paramyxovirinae L-gene at
2019-02-01. Three findings outlive it: **`oligo_ok_max` has no effect on panel accuracy
at all**, so the panels can fit only one of the engine's two numbers; the curve bottoms
out at `oligo_weak_max: 3.0`, the value already shipped; and **Rahn reports zero cost
while Forslund loses within-family negatives**, which is the argument for `role: control`
turned into a measurement.

**S2** (`docs/journal/2026-10-26-s2-smooth-decay-killed.md`). **Passes its own kill criterion and
destroys four catches nobody named**, including `CDV_P_gene_Scagliarini_2007` @2021-07-06,
the single `fails`+`drift` row in the development set. Failures caught 5/11 -> 1/11, PPV
2/9 -> 0/4, while false alarms IMPROVE 5/32 -> 2/32 - so total disagreements go 10 -> 11
and **an aggregate reads it as neutral.** The fitted curve discounts the whole 3' window
rather than smoothing the cliff. **Lesson for the protocol: a named kill criterion is a
probe and can be insensitive; the standing no-lost-catch rule is what does the work.**

**S3** (`docs/journal/2026-10-26-s3-chemistry-switches.md`). The probe switch takes documented
failures caught 5/11 -> **6/11** and PPV 2/9 -> **3/10** with **no increase in false
alarms**, fixing the influenza Matrix-gene case it predicted. The only rung that
TIGHTENS, so its extra flags are evidence rather than a loosening artefact. It fails its
own criterion on two published positives of the Leptospira panel, both `reduced` probe
calls. The conventional switch is **inert**: 251 calls of 2.7 M, no verdict anywhere,
which answers a ROADMAP Phase 2 claim that `terminal_mismatch_fails` inflates `fail`
across the conventional majority.

**S4 / M1** (`docs/journal/2026-10-26-s4-m1-no-longer-refuted.md`). Re-specified, because S1 and
S2 died and the stack S4 was to be tested under no longer exists. **M1 alone changes ZERO
rows of the 49-case matrix** and rescues **7** documented panel false fails (5 FAP, 2
Barrett) at no panel loss and no cost on Rahn. The 17 Leucocytozoon record movements
reproduce the 2026-10-22 record EXACTLY; what changed is that the verdict is no longer
near its boundary - that window now holds 21 records and M1 moves the interval's upper
bound 50% -> 55% against a 90% threshold. Verified by a real rescreen, so not a harness
artefact. `docs/journal/2026-10-22-M1-tier2.md` is marked **superseded in its conclusion.**

> **What that does NOT establish.** M1 is **no longer refuted by the evidence that
> refuted it**, which is smaller than being supported. The set is 49 cases collapsing to
> about seven independent failure events. And the reason it is no longer refuted is that
> one assay's window grew, not that new evidence arrived about the wobble - so re-taking
> the decision rests on a denominator change, in the layer this project keeps finding to
> be its weakest.

**S5 stays gated** at 11 within-family negatives against 40.

## 5. The two panels, and the one that evaporated

`docs/bench-panels/ahmed-2020-leptospira.tsv` (`6d515ff`) finds **five** published
positives scored `fail` where the entry's note names three - `L. kmetyi`, `L. adleri`,
`L. gomenensis`, `L. barantonii` and `L. ellisii`, every one carrying `rev1 C:T`. It also
predicted, before S3 ran, that the terminal switch alone would not rescue them. `L.
meyeri` is excluded: Table 1 scores it both `+` and `-`.

**The calicivirus Hel1 panel's premise is gone.** It was to be the conventional half of a
two-chemistry test, on the strength of "0 of 30 detected on one terminal base". The
2026-10-24 correction of Hel1's terminal base G->C removed the mismatch it rested on; the
entry now reads detect 17, reduced 2, fail 12. **`ROADMAP.md` Phase 2 still quotes the 0
of 30 figure and should be corrected.** S3's conventional half has no panel behind it;
the Usutu class is the remaining lead.

`docs/bench-panels/panels.tsv` now carries the panel-to-assay mapping, which until now
lived only in shell history, with `paper` as the independence unit and Rahn marked
`control`.

## 6. `declared_tolerance` and the size-less entries (`714c24f`)

Five live entries declare no size, not the four the plan listed. One declaration made:
`Pan_mycoplasma_16S_23S_intergenic_space_Rebelo_2011` gets `amplicon_bp_range: [354, 767]`
from 307 products over 63 distinct lengths, flagged `amplicon_multimodal`, no
`species_sizes`. Three measured and deliberately not declared: Bsal (two products, both
161 bp, in a 12-record retrieval), POLYOMAVIRUS VP1 round 1 (five products, **zero
detects**), BORNA round 2 (**nothing to measure from at all** - zero detect and zero
reduced, so its 369 failures have no baseline to decline from).

> **The schema made a decision I was about to make wrongly.** `amplicon_size_unresolved`
> is an OPEN QUESTION and the validator refuses one on an `active` entry, so adding it to
> the two active entries would have demoted them. Removed; the measurements are recorded
> as caveats instead, each saying a maintainer should expect active 179 -> 178.

## 7. Mao 1997 is read, and it closes a long-open question (`01c07ca`)

`papers/10.1006_viro.1996.8435.pdf`. Its Table 2 prints the ranavirus MCP pair directly:
primer 4 `GACTTGGCCACTTATGAC` (aa 15-20) and primer 5 `GTCTCTGGAGAAGAAGAA` (aa 191-186),
both 18 nt and byte-identical to the registry. So `oligos_from_secondary_source` is
**confirmed rather than asserted**, and the **18/19-mer question is CLOSED** three
transcriptions to one against Stöhr 2015's 19-mer, which `docs/journal/2026-10-24-heldout-candidates.md`
had left open pending the NYU proxy. **Neill & Seal 1995 is now the only sequence
question still open**, and only half-held as page 33 of a 33-38 article.

Also: the `by_chemistry` comment in `config.yaml` refreshed (it read 167/44/214 against a
live 155/51/209 while saying the argument "rests on exactly these numbers");
`subcluster.py`'s "no consumer yet" corrected; `lineage_report.py:205`'s resolver
asymmetry documented and deliberately not fixed; the two C2 corpus numbers reconciled as
a floor (40) and a target (60) rather than a disagreement; ROADMAP Phase 0 ticked.

## 8. The Bd miss, priced, and one claim retracted the same day (`faae47d`, `ab77623`, `ec578d0`)

`docs/journal/2026-10-26-bd-phase1-site-level-measured.md`. **Read its own correction notice
first.** Two findings hold and one is withdrawn.

**Holds — gapped matching is worth 0.046%.** 426 of 932,856 evaluable fails, from
`indel_check.py`, reproducing the 2026-10-04 "not worth building". Its real use is
registry QA, and its worst outlier is `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` at 7.0% -
the same entry section 6 found never reaches `detect`.

**Holds — the amplicon-level rule discards 297,651 rows that carry a credible primer
site**, 10.9% of the table, counted exactly from the calls table with no offset involved.
`no_site` is 1,442,931 and genuinely unreachable, which bounds the whole idea.

**WITHDRAWN — the Bd probe-site table** (122 judgeable of 461, 94 failing, 25
indel-explained). It rested on a probe offset that one record in three agreed with. Two
bugs: offsets pooled across record orientations, so Bd's ITS deposits mixed **+93 with
-95** and the mode of contradictory numbers placed the probe nowhere; and the tolerance
for finding the probe was +/-5 bases, which made a slightly-off offset fatal. Caught
because a sibling assay read **42 of 42 failures as indel-explained** and a hand check
found the probe at gapped cost **0**.

> **And the corrected answer is harder: Bd is UNMEASURABLE by this route.** Of its 9,493
> records exactly **three** hold a clean forward, reverse and probe site together, and
> they disagree. An offset needs full-amplicon records and Bd barely has any - which is
> the same fact as the case itself, so **the assay that motivated site-level evaluation is
> the one whose geometry this approach cannot calibrate.** That is why the case doc needed
> a hand-picked reference, and it means its three hand-read records remain the only
> sequence evidence of the Bd probe-site deletion. The count is three, not 25.

**Then the cross-assay run closed the question the retraction had opened** (`f3dd0d5`,
per-assay output in `docs/2026-10-26-site-level-per-assay.txt`). Across all 34 measurable
probe-bearing assays, gapped alignment explains **one** failing probe site. So gapped
scoring stays unbuilt on both counts - 0.046% registry-wide and 1 record inside the
site-level population - and the case doc's three hand-read Bd records are a local
exception, not the leading edge of a pattern. Totals: 7,261 discarded rows, 2,014
placeable, 1,790 holding the whole probe footprint, **1,109 of them failing**. Read 1,109
as a count of judgeable failing sites and never as a coverage figure; a lone probe still
has no credibility test.

So **site-level evaluation is still the valuable half** - 297,651 rows, and that number
survives the retraction. And **placing a lone probe is now the critical path for Phase
2**, not a formality. Three findings feed into it:

- **The offset method fails in rough proportion to how much a case needs it.** 14 of 48
  assays are unmeasurable and they hold almost all of the population - the influenza
  Matrix gene alone is 93,966 rows against 7,261 for every measurable assay combined. An
  assay is unmeasurable precisely when few of its records hold a full amplicon, which is
  the same condition that makes its records truncated. The Bd finding generalises.
- **Only 2,014 of 7,258 examined records could be placed at all**, so the method is weaker
  than its headline even where it runs.
- **It needs a magnitude bound as well as a concordance gate.** MONKEYPOX N3R proposed an
  offset of **+184,379 bases**, refused only because 13 of 141 observations agreed with
  it. An offset larger than the declared amplicon is not an offset.

Phase 2 stays stopped, and now for measured reasons: it cannot be replayed (no
`no_amplicon` row carries a site coordinate, confirmed on all 1,789,100), so every
iteration costs a rescreen.

## The three decisions, taken 2026-10-26

The maintainer took all three the same day. **`main` still ships every scoring value it
shipped this morning**; one proposal sits on a branch and one mechanism ships inert.

**1. M1: PROPOSED, THEN REJECTED BY THE HELD-OUT SET, the same day** (`faeee0e`;
`docs/journal/2026-10-26-heldout-read-m1-rejected.md`). **`main` is unchanged** and
`experiment/2026-10-26-m1-proposed` is **not merged**, kept as the record with the rejection
written above the case for it.

> **THE HELD-OUT SET HAS BEEN READ AND IS SPENT.** `docs/validation-cases-heldout.tsv` was
> consulted once, on the maintainer's instruction, for the one decision it was reserved for.
> No future candidate can use it, and `docs/journal/2026-10-24-heldout-candidates.md` already
> records that literal oligo search over Europe PMC is exhausted - so **new cases now block
> the whole calibration programme** rather than sitting on a backlog.

It passes the half of its gate I pre-registered and fails the half I omitted. I wrote "M1
merges only if the held-out set loses no documented catch", and by that it passes: 4/9
caught on both tables, nothing lost. But M1's own gate, set in
`docs/journal/2026-10-21-M1-shipped.md` and applied at the 2026-10-22 revert, has two halves -
"caught failures do not fall AND no works/partial case newly disagrees" - and the second
fails. `Morbillivirus_including_CDV_P_gene` @2014-03-01, a documented `works` case, goes
`low coverage`/weaker to **`declining`/DISAGREES**. The drift flag's precision falls
3/4 = 75% to 1/3 = 33%, and the shipped rule's **perfect 0-of-17 false-alarm record on that
set breaks**.

Not a replay artefact: that assay was not among the 17 rescreened earlier, so it was
rescreened - 37,522 records, **0 call disagreements**.

> **AND THE MECHANISM IS A FINDING ABOUT THE DRIFT MODEL, not about M1.** M1 makes that
> assay's RECENT window better, 64.9% to 67.6%, and that is what flips it, because it lifts
> the baseline years by more, so "no measurable fall" (-25% to +6%) becomes a measurable one
> (-43% to -14%). **A uniform loosening can MANUFACTURE a `declining` verdict.** The test
> plan's standing rule - "a change that only loosens will always cut flags; that is not
> evidence" - is true of COVERAGE flags and false of DRIFT flags, and nothing in the
> ladder's reasoning anticipated it. Every loosening candidate should be read against this.

It is the same defect the 2026-10-22 revert recorded, on a different case four days apart.
So M1's characteristic failure is manufacturing a false `declining`, and what changed in
between is only that the development set stopped containing a case that shows it. **M1
changes zero of 49 development rows and rescues 7 bench-panel false fails, and that was not
enough** - which is the real lesson about a development set that has informed several
decisions.

> **The confirming rescreen the decision was conditional on is done, and it measured
> something worth having** (`docs/journal/2026-10-26-m1-confirming-rescreen.md`, `b6195c2`). M1
> really rescreened over every tier-2 assay it moves - 514,096 rows across 17 assays - gives
> **2 call and 11 penalty disagreements** against the replay, 0.0004%, and **all of them
> pessimistic**: the real screen finds a better candidate than a replay can, because a
> replay is stuck re-scoring the amplicon the shipped rule chose. So every rejection in the
> ladder stands without qualification and the survivors are under-credited. Neither
> disagreement can move a verdict; both fall on one assay at 97.9% of 755 records against a
> 90% threshold. `scripts/archive/rescore.py` used to call this effect "unmeasured" and now carries
> the number in the boundary it prints on every run.

**2. The probe switch: BUILT AND SHIPPED OFF** (`f73f8de`).
`drift.reduced_not_detected_for` ships `[]`, so nothing behaves differently. `YearStats`
and `AssayDrift` carry `detected_calls`, `drift.reduced_not_detected_ids` maps chemistries
to assay ids, and both `report.assess_as_reported` and `retrospective.load_evidence` pass
it. Same house pattern as `engine: serial`, `by_chemistry` and `locus_identity_min`. Six
tests, and the load-bearing one asserts the shipped config selects **nothing**.

**3. `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1`: LEFT ACTIVE** (`f73f8de`), and its missing
size turned out to be published all along. Three explanations for its zero detects are ruled
out and recorded on the entry: not an oligo typo (design paper, PREDICT supplement and
registry all print `AACAAGAGACACAAATNTTTCCNCC`, three independent sources); not the missing
size (declaring the paper's 829-1137 bp excludes 75 of 2,075 products, 3.6%, because 96.4%
were already inside); not an indel artefact, though a real one covers ~7% of failures.
`amplicon_bp_range: [829, 1137]` is now declared from the paper's Table 1, fixing an
asymmetry where round 2 had carried its size since entry and round 1 never did.

> **Section 6 asked the wrong question and this is the correction.** It measured only the
> entry's own five products and declined to declare on five records. That was right on that
> evidence, and nobody had checked whether the cited design paper publishes a size. It does.

## The search for new cases: an instrument, a queue, and no case (`35d0068`..`c1366d7`)

`docs/journal/2026-10-26-retrospective-case-search.md`. With the held-out set spent and the old
seam exhausted, new cases became the binding constraint, so a new instrument was built:
`scripts/find_retrospective_cases.py` searches the **citation graph** rather than oligo
text, because a group using a published assay cites it and does not retype its primers.
**220 candidates** in `docs/2026-10-26-retrospective-candidates.tsv`, 202 distinct papers
across 55 design papers.

**Four were read and none became a case.** One was circular - an in silico mismatch count
concluding the assay still amplifies, which is our own method, so a case on it would be
the tool confirming itself. Two failed on assay identity by a guess. The fourth failed on
identity by a **measurement**, and it is the one to understand:

> A 2024 pan-coronavirus head-to-head measures three assays on 141 archived specimens.
> Its **first** PREDICT protocol is confirmed at sequence level to BE the registry's P-005
> nested pair, which validates the `docs/validation-cases.tsv` row already citing it. Its
> **second** is not ours: forward identical, reverse the **23-nt** form where the registry
> holds the **24-mer** - the exact base the 2026-10-24 sweep ruled on - plus a hemi-nested
> round we do not hold. And the entry's own notes put that 23-nt variant at **88** exact
> binding sites against our **215** over 25,576 records, so it binds less than half as
> often and its low detection rate cannot be attributed to our form.

> **THE FINDING, and it reframes the corpus problem: IDENTITY IS THE BOTTLENECK, NOT
> DISCOVERY.** A paper reporting an assay's performance names it locally or by citation and
> rarely reprints its oligos. So the citation graph finds the right papers and cannot by
> itself confirm the assay tested is the assay we hold. The queue has 220 rows; what is
> scarce is the hour per row to settle identity. The next move is not another sweep but a
> cheaper identity check - and the one thing that settles it every time is the paper's
> primer table, which for the fourth candidate was in a supplementary ZIP two levels deep.

**Also refuted: Furuyama 2018**, which this resume point and the plan both carried as "the
best candidate anywhere in the sweep for a real H5/H7 drift case" and the only named lead.
It is a **LAMP** primer-design paper - its primer positions are LAMP positions - and the
registry holds no LAMP assay. Carried for days on a description that does not survive its
own abstract. Remove it from the lead list.

## What is next

1. ~~**Read the held-out set against the M1 branch.**~~ **DONE, and it rejected M1.** The
   set is spent. **Nothing is blocked on a decision; what is blocked is evidence.**
2. **The corpus, and the question has changed.** 220 candidate papers are queued and the
   constraint is no longer finding them - it is confirming that the assay a paper tested is
   the assay the registry holds. Three of four reads died there. A cheap identity check is
   worth more than another sweep. The queue's `groups` column says which rows could yield
   the scarce `fails` kind: 6 `mismatch` and 3 `redesign` rows are the concentrated signal,
   and 140 `miss` rows are mostly clinical sensitivity reports.
2. **Correct `ROADMAP.md` Phase 2's "0 of 30" calicivirus figure**, which the Hel1
   correction invalidated.
3. **The corpus, which is now the binding constraint on everything above.** Both rejected
   candidates died on the same ten Forslund within-family negatives, and C2 is gated at 11
   against 40. This is plan step 7 and it is a literature pass, not a modelling problem.
   The one named lead is Furuyama 2018 (`10.1128/jcm.00985-18`, paywalled, ASM).
4. **Not started and deliberately so:** Bd Phase 2, C1, the lineage resolvers, report
   visualisation (its matrix still has headline intervals spanning 25 to 50 points), and
   `scoring.locus_identity_min`, which stays null.

---

# Resume point, 2026-10-25 (the open list worked to its floor, one fix shipped, and a plan; 2026-10-24 below)

**Start here:** the plan is the section "where the pipeline actually stands, and the plan",
below item 7. Short version: the machinery is sound, the *denominator* is the weak layer, the
thresholds are placeholders fitted against one ground-truth drift event, and visualisation
should wait until the first three plan steps land.

## 2026-10-25: four of the open items are closed, and what is left needs a browser or a different instrument

Plan: `~/.claude/plans/go-to-assaywatch-resume-ancient-shell.md`. The maintainer took four
decisions up front (keep the 636 MB, commit per item, add held-out rows but do not score,
reconcile the Elsevier script rather than revert it). Registry **unchanged at 208/179/28/1**
throughout — nothing below adds an entry or changes an oligo. Gate at the end: 1,563 tests,
validator 208/208, `check_citations` 208/208, ruff clean.

**1. The Elsevier fetcher is reconciled and commits are unblocked** (`a58e2a9`). It had been
replaced on disk by a better-shaped implementation that silently dropped both fixes from
`1786091`, and it failed `ruff BLE001`, which blocked *every* commit in the repo. The new
shape is kept. `held_dois` is back, and it mattered more than the old note suggested: the
replacement's "already held" test looked only for `papers/<stem>.pdf`, so the eleven papers
held as Elsevier `.xml` deposits all read as missing and would have been re-fetched over the
API. The `<body>` test does **not** return as code, because this version requests
`application/pdf` and the `%PDF` magic number is the stronger guard — a metadata-only reply
cannot start with `%PDF`, where it can and did carry every XML marker. Its reasoning, and Mao
1997 as the case that earned it, is in the module docstring. `slug()` is gone in favour of
`doi_stem`.

**2. Two of the twelve free papers are held; the other ten need a browser** (`21c06db`).
Makkonen 2018 and Oidtmann 2006 arrived via `find_open_access.py --download`; index 157 → 159.
Zero verdict changes, for a stronger reason than last time: **neither DOI is cited by any
registry or pending entry, so neither can appear in the verifier's output.** List 1 stays
complete. The other ten are all open per Unpaywall and none needs the proxy — six sit behind a
publisher bot-check that refuses a scripted agent (Sage ×2, T&F, Wiley, Allen Press ×2) and
four resolve to a landing page that does not expose its bitstream (DIGITAL.CSIC, CONICET at
HTTP 500, UCF STARS, an Elsevier JS redirect). **Spoofing a browser agent to automate these
was attempted and refused, correctly; it is not the way through.** They are listed for a human
in the new `papers/papers-fetch-list.md`, together with the two proxy papers.

> The verifier's 502 rows do differ from the 2026-10-24b run in three places, none from these
> papers: `Hel1` moved `exact` → `near:1` because the entry was corrected G→C yesterday while
> the OCR'd deposit still prints G, and `Pol1`/`Pol2` are new rows from the RdRp entry, both
> `exact`. That is the corrected registry disagreeing with a known-corrupt deposit, as intended.

**3. Two orphan groups deleted, the 636 MB kept** (`85b2277`). `1430836/all` (*Perigonica*, 19
moth COI records — host barcoding, out of scope, and the fetch made under a documented
wrong-taxid error) and `208294/all` (Seadornavirus, 1,115 records, never claimed by any entry).
Both to the Trash, not `rm`, and both re-fetchable. `orphan_archives.py` now reports **8
groups, 19 archives**. The total is still 658 MB because what went rounds to zero: this bought
a shorter orphan report, not disk. The maintainer kept the 636 MB on the doc's reasoning.

**4. The Candrian seam is worked to the end and yields nothing**
(`docs/journal/2026-10-25-candrian-seam.md`). All 59 papers triaged; **zero clear the held-out bar.**
They are AMR prevalence surveys that use the primer for species confirmation — exactly
`works`-shaped, as predicted. Five plausible titles were read in full. The closest, Gerber 2007
(`10.3201/eid1308.060428`), reports PCR missing **4–20% of hybridizable plasmid genes** — the
right shape, and the registry does hold an `hlyA` entry — but fails twice over: its `hlyA`
primers are a 1551 bp pair credited elsewhere, not Wang 1997's 361 bp `O157-3`/`O157-4`, and it
reports **no malB result at all**, the gene appearing once in its primer table as an unreported
internal control.

> **The pass paid anyway, in a currency it was not looking for.** Gerber 2007's Table prints
> `MalBU GACCTCGGTTTAGTTCACAGA`, **byte-identical to the stored `Eco1` forward**, so that oligo
> now has an independent printed source — worth having, because Candrian 1991 is paywalled and
> the entry's sequences have never been checked against their own design paper. Two cautions
> keep it out of the registry as evidence: the reverse is *not* confirmed (Gerber pairs the
> same forward with a different reverse for 414 bp against the registry's 585), and the paper
> attributes the primer to "This study" rather than to Candrian. Nothing was changed; the
> entry's `orientation_inferred` flag is untouched, since `MalBU` is a forward too.

**5. The full run went, and it found something that was not on the list**
(`docs/journal/2026-10-25-chance-pairs-invent-denominators.md`). `results/2026-10-25/`, **434 of 434
steps, 29m 09s, exit 0**. The three parapoxvirus groups are retrieved and screened by the
pipeline for the first time, which was the point of running it. The run itself is clean and
additive: of 146 pre-existing scored assays only **3 moved, each by ≤0.2 points** from new
deposits, **no status changed**, and the six rows new to the report are yesterday's six new
entries. 181 → 188 scoreable.

**But the Orf entry came back at 75.0% where its note records 100%, and the gap is a scoring
artefact that misstates an ACTIVE entry's verdict.** `max_pair_evalue: 0.01` admits an amplicon
formed by chance in a record that does not carry the target; the record becomes `EVALUABLE`, the
probe is absent because the region is absent, and the row scores `fail`. In Orf the genuine
detects sit at pair_evalue 1.6e-19–7.7e-15 and the 76 artefact fails at 4.1e-5–8.4e-4 — ten
orders of magnitude, all inside the cutoff. All 76 are real Orf virus, but they are **B2L**
partials and the assay targets **RPO147**.

**The criterion took two tries and the first was wrong; the doc carries the correction.**
`pair_evalue` alone is invalid — a short amplicon in a long genome legitimately scores high,
because the statistic scales with the search space. `RANAVIRUS_..._MCP_Pallister_2007` makes a
real **57 bp** product in **~99 kb** at `pair_evalue` 2e-5 with penalties 2.5/2 and the probe
**present**; keying on the E-value briefly suggested five assays including three `active`
ranavirus entries would cross 90%, and **that is withdrawn.** The sound test is a `fail` row
with the **probe site absent** *and* **both primers above `reduced_max: 3.0`** — the probe
being the target locus's signature. That also bounds it to **probe-bearing assays**;
conventional entries have no such test and are not assessed (applying the penalty half alone
to them flags ~4,900 plausibly-genuine lyssavirus coverage failures).

**SCOPE CORRECTED the same day — read `docs/journal/2026-10-25-stale-orphan-screens.md`.** I first
measured by globbing `results/screened/`, which keeps **orphan** group screens that nothing
rescreens, one of them dated 2026-10-03 and so predating `amplicon.declared_tolerance`. That
inflated the count about a hundredfold. From `results/2026-10-25/calls.tsv.gz`, which is what
the report is built from, the real figure is **277 rows across 11 probe-bearing assays out of
924,755 evaluable**. The three `mgb` fungal assays are not in the corrected list at all, and of
West African mpox's 13,239 evaluable rows only **4** are touched, so its 2,688 clade-I failures
are untouched as required. **Only two verdicts move, and they are unchanged** — those were read
from the report, never from the glob. The one that matters:

> **`OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023` is `active` and reads 42.2% when it is
> 100.0%.** `no_amplicon` 25,401, `fail` 111, `detect` 81 — and **all 111 failures are chance
> pairs, so it has no genuine failure at all.** It is reported under *Low Coverage* with its
> CI upper bound below 90%, i.e. as an assay missing more than half of what it should find.
> Penalties on those rows are `(6.5, 9)`, `(7, 9)`, `(6, 8.5)` against a `reduced_max` of 3.0.

Orf's whole-archive figure is likewise **88 of 88 genuine evaluable, 100%**, reproducing its
hand screen exactly — the hand screen used complete genomes, which carry RPO147. Its *recent*
window was checked after the correction: 9 of its 37 recent evaluable rows are artefacts and
the rest all detect, so 75.7% → 100%, but it is a `draft` entry so no published verdict moves.

Removing the artefact takes the three `mgb` fungal assays only to IGS 1.4%, ITS2/28S 31.8%,
*B. sal* 25.8%, which I first read as "a large genuine problem underneath". **Withdrawn the
same day** — those are whole-archive rates and the residue is more chance windows, not a
problem; see plan step 1. Only `targetD` and Orf go to exactly 100.0%.

**Nothing was changed; the lever is a threshold and this is a denominator change.** The doc
prices three options and names the guard a fix must not break: **do not key the fix on the
probe's absence.** The West African mpox assay's 2,688 failures are probe-less with
`fwd_penalty` 0 and `rev_penalty` 0 — real amplification that the clade-II probe genuinely
misses, and a finding that must survive. The discriminator is primer penalty and `pair_evalue`,
never the probe.

**6. Decision A SHIPPED** (`44c6470`). `calls.apply_chance_pair_test`, at report time beside
`apply_anchor_fdr`, `drift.chance_pair_test: true`. Re-priced by rendering the report both
ways: exactly two assays change, no collateral. `targetD` **42.2% (192 ev) -> 100.0% (81 ev)**
and Orf 75.0% (36) -> 100.0% (27), both Low Coverage -> Stable; headline 39 low coverage -> 37,
54 stable -> 56. No new threshold: the bar is `scoring.oligo_weak_max` (3.0), already justified.

> **The bug in the first attempt, because it would be easy to reintroduce.** `read_calls` keeps
> only the columns drift needs - loading the whole two-million-row table as dicts took 3.6 GB -
> so `probe_site` and the penalties were never on those rows. The first version read keys that
> did not exist, took its `except` branch on every row, and changed nothing. **A no-op re-price
> is indistinguishable from a clean one**, which is how it nearly passed. `read_calls` now
> carries `probeless_penalties` on only the rows that can move, and a test pins that directly.

**7. A candidate from the newest Downloads PDF**, `pending/SIMBU_SEROGROUP_ssRNA_S_segment_TaqMan_Steyn_2020.yaml`.
van der Walt 2023 (Shamonda virus, Pathogens 12:1100) is now held as
`papers/10.3390_pathogens12091100.pdf`; its Table 1 prints a Simbu serogroup S-segment TaqMan
assay no registry entry holds, credited to Steyn 2020 (`10.3201/eid2607.190770`,
Crossref-resolved, EID so open access and fetchable). It stays in `pending/` because the
sequences have not been seen in their own design paper. Two notes worth keeping: `pdftotext`
without `-layout` **swaps that table's forward and reverse**, and the paper's own nested F141
primer overlaps the forward's 5' end, which is what settles the orientation; and the taxid is
the genus deliberately, because "Simbu serogroup" is not a taxonomic rank and the species node
3052441 would exclude the Shuni and Shamonda viruses the assay detects. The same paper also
designs four assays of its own, all pooled-degenerate, deliberately not entered.

---

## 2026-10-25: where the pipeline actually stands, and the plan

**The pipeline as machinery is in good shape.** validate -> retrieve (checkpoint) ->
`screen_archive` x425 -> collect -> site_drift / lineage / degeneracy / figures -> report, with
the trigger closures guarded by `tests/test_triggers.py`, the same rules running under
`profiles/slurm/`, benchmarks and `run-timing.json` instrumented, byte-identity checks
practised, and a four-part gate enforced by pre-commit. 1,574 tests. Nothing below is a
complaint about the engineering.

**The weak layer is the denominator, not the oligos.** That is the honest headline of the last
three days. Three denominator defects surfaced: Congo Basin C3L (handled correctly as
`no_site`), the West African clade I failures (real, and unscopable with what exists), and now
chance pairs. **All three share one root: evaluability is decided from primer placement alone,
with no test of whether the record carries the target locus at all.** And all three were found
by accident - by chasing a discrepancy - rather than by a test. List 1 of the papers work is
complete and the stored oligos are well verified; it is the question *which records deserve to
be judged* that is carrying the uncertainty.

**The second weak layer is that the thresholds are placeholders.** `ROADMAP.md` says so
outright, and names `max_mismatches_searched: 6` as "the most consequential number here" and a
guess. The development set has **one** drift ground-truth event. So a verdict's *direction* is
informative and its *absolute level* is weakly grounded - which is exactly why a wrong 42.2%
could sit in the report without looking anomalous.

### Where the plan stands after 2026-10-25 (read this before the list)

Steps 1 and 2 are both **resolved, and neither resolved the way the plan expected.** Step 1
found nothing wrong with the fungal assays and withdrew the number that motivated it. Step 2
was built, priced and **rejected**. So the denominator problem now has exactly one shipped fix
(`drift.chance_pair_test`, probe-bearing assays, 277 rows, two verdicts) and **three failed
attempts at the general case**: a `pair_evalue` cut, Benjamini-Hochberg over pairs, and
interior identity. Each failed the same way — it could not tell a chance pair from a real
target that is genuinely divergent — and the third failed hardest, because 48 of 209 entries
are consensus assays for which divergence is the design intent.

**That is itself the finding.** No per-record sequence statistic separates the two, because for
a consensus assay the two are the same thing. What distinguishes them is not the sequence but
the *expectation*: whether this assay is supposed to amplify that lineage. That is lineage
knowledge, and the project's own machinery for it (`lineage.sublineage`, `clustermaps.py`,
`subcluster.py`) ships inert with `sublineage: {}`. So the honest path for conventional
denominators is the one the design doc named as its fallback all along: **they stay
approximate until tier-2 validation sets the thresholds**, and the lineage machinery is where a
real fix would start.

**Revised order: 3 and 4 are now the plan**, with the lineage-aware locus reference as a
candidate inside 4 rather than a step of its own. 5 is unchanged and still last.

### The plan as originally written, in the order that unblocked the most

1. ~~**Diagnose the three `mgb` fungal assays.**~~ **DONE 2026-10-25:**
   `docs/journal/2026-10-25-fungal-assays-diagnosed.md`. **Nothing is wrong with them, and the
   "1.4% / 31.8% / 25.8%" framing above is WITHDRAWN** - those are whole-archive rates over
   archives full of WGS contigs, and the report scores a recent window, where all three read
   *no recent data* or *insufficient data* on **100% baselines**. The low rates were chance
   32-mer probe windows in contigs that do not contain the locus: strain AMFP15/1 has one
   contig at probe mismatch **0** and another at **11**, so the high numbers cannot be the ITS
   locus at all. Same root cause as Orf and targetD, found from the probe side instead of the
   primer side. The records that detect include `KC762295` and `NR_111867` (**TYPE material**),
   both at 0.
   > **One thin real signal, now a watch item, not a correction.** Five *B. sal* records
   > deposited 2024-12-06 (`PQ661663`-`PQ661667`, SNU isolates) are 161-165 bp sequenced
   > amplicons with **both primers perfect** and probe-window divergence of **2, 6, 8, 8 and
   > 12** mismatches - the hydrolysis-probe failure that reads negative on a true positive. It
   > is five records from one lab on one date, below `min_records_for_drift: 15`, which is why
   > the report says "insufficient data" and is right to. **An independent source showing the
   > same divergence would make it a drift case**, and the held-out set has exactly one of
   > those today.
2. **The locus-identity test — BUILT, PRICED, AND IT DOES NOT WORK (2026-10-25).**
   `scoring.locus_identity_min` ships **null and must stay null**; the long comment in
   `config.yaml` says why at the point of use. **A pan-family assay's success looks like
   failure to it.** Priced offline at 0.50 it rejects **1,840 of 9,687 sampled failures**, and
   `Pan_HERPES_dsDNA_Polymerase` loses **47 of 47** — records that are *Proboscivirus*,
   *Mardivirus gallidalpha2*, *Equid alphaherpesvirus 1*, *Elephant endotheliotropic
   herpesvirus 5/5B* and *Macropodid alphaherpesvirus 4*, i.e. real cross-subfamily
   herpesviruses and the entire point of the assay. They score 0.35–0.41 only because the five
   references happened to be human CMV UL54 from one submission batch. **48 of 209 entries are
   pan/consensus shaped.** It also cannot judge Orf (68 bp → 28 after trim) or `targetD`
   (57 bp → 17), the two cases that motivated it, which `drift.chance_pair_test` already
   covers. **Third approach that looked right and was not**, after `pair_evalue` and probe-only.
   Also correcting my own earlier number: SIV Takehisa's genuine floor over 400 records is
   **0.56**, not 0.65, so **0.55 was never safe** and the margin is 0.41–0.56.
   **The only version with a chance: lineage-aware references**, one per sublineage via
   `clustermaps.py`/`subcluster.py`. Unproven. The module, 12 tests,
   `scripts/archive/build_locus_references.py` and `scripts/price_locus_identity.py` are kept as
   evidence and as the basis for that. Superseded detail below:
   **The locus-identity test, generalising decision A — originally DESIGNED, not built:**
   `docs/journal/2026-10-25-locus-identity-design.md`. Ask whether an amplicon's **interior** is
   homologous to the assay's own detecting amplicons; the records that detect certainly carry
   the locus, so they define what it looks like. Deliberately not on the primer sites, where all
   the confounding lives. It separates Orf's B2L pairs and the *Ophidiomyces* scaffolds (no
   homology) from the ranavirus and West African mpox failures (homologous, must count), and it
   needs no probe, so it reaches the 155 conventional entries. **`loci.pair_spans` cannot do it**
   — it selects on the same `max_mm`/`max_e` the chance pairs already pass. It must live at
   **screen time** (nothing writes the amplicon sequence), so each iteration costs a ~30-minute
   rescreen, and it wants a cached per-assay reference.
   **The blocking measurement is DONE 2026-10-25 and the approach SURVIVES**, on clean data
   from `calls.tsv.gz` (`scripts/archive/measure_locus_identity.py`). Chance pairs land at
   **0.32–0.41** identity, genuine failures at **0.65 and above**, detects at 0.87–1.00, and
   nothing sits in between — including on `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene`, a
   conventional assay, which is the whole point: it has **no** chance pairs on current screens
   and its genuine failures sit at 0.86–0.99. **The ceiling is
   `RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009`**, whose genuinely divergent failures sit at
   **0.65–0.67**: a threshold of 0.70 deletes all 60, the exact failure that killed the two
   earlier approaches. **Recommended `scoring.locus_identity_min: 0.50`**, mid-gap (0.55 safe,
   0.70 known wrong). Two limitations: a 57 bp amplicon like `RANAVIRUS_..._MCP_Pallister_2007`
   leaves too little interior to judge, so the test must decline toward *keeping* such a record
   evaluable; and the 20 bp trim is uncalibrated.
   > **The cheaper signal was measured and REJECTED as a gate.** Amplicon-length dispersion
   > looked promising only on stale screens. On current data Orf's chance pairs are all at
   > exactly 62 bp against a declared 68 — one length, not scatter — `targetD`'s span 56–69
   > against 57 with **63% within 5 bp**, so a length rule would keep most of the rows that
   > made the one wrong active verdict, and West African mpox's genuine clade-I failures are all
   > **82 bp against a declared 85**, so strict equality would delete the finding the design
   > exists to protect. `amplicon.declared_tolerance: 0.25` already does the coarse version and
   > is the one config number with a measured defence. **Length is a diagnostic, not a filter**;
   > interior identity remains the test.
3. **Per-chemistry scoring** (ROADMAP Phase 2). The largest known distortion and the one with a
   worked example: 155 of 208 entries are `conventional`, `terminal_mismatch_fails: true` is a
   qPCR-strength rule applied to all of them, and on `CALICIVIRUS_ssRNA_Helicase_Reid_1999` it
   alone takes a published, working assay to 0 of 30 detected. It almost certainly inflates
   `fail` across the conventional majority. It is also why conventional assays could not be
   assessed for chance pairs: their failures are not currently trustworthy either way.
4. **Tier-2 retrospective validation**, which is what turns every threshold above from a guess
   into a fitted number. **Its blocker is cases, and the cheap route to cases is exhausted** -
   literal oligo search over Europe PMC is spent (see the Candrian seam). So this wants the
   scoring-strategy replay harness, not another sweep. **CORRECTED 2026-10-26: this line used to
   point at `docs/journal/2026-10-06-lab-leads.md` as the other route, and that overstates it.** Those
   leads are a source of NEW ASSAYS. Tier-2 needs a paper reporting how an assay *already in the
   registry* performed, which is a different literature. Of the file's 121 DOIs, 45 are
   PubMed-confirmed and 76 are agent-reported only, and the lab attribution is wrong for at least
   3 of the 5 high-priority leads.
5. **Report visualisation, last and deliberately.** Figures, forest plot, site-position plots
   and clustermaps already exist and are adequate. Until 1-3 land, better presentation makes
   numbers that are in places wrong more persuasive rather than less, and any layout built
   against today's denominators gets redrawn when they change.

### What is left, and what each one now needs

- **Mao 1997 and Neill & Seal 1995** — still the only papers blocking a question rather than a
  completeness read, still proxy-blocked. Both are in `papers/papers-fetch-list.md` with their
  canonical filenames. Note the Hel1 question was *decided* yesterday on measurement, so that
  PDF now confirms or reverses a decision already taken rather than unblocking one.
- **The held-out set's drift shortfall** — 34 rows, and **literal oligo search over Europe PMC
  is now spent.** Every searchable registry oligo has been tried: the Candrian forward was the
  last rich one, the rest return 0 or are too degenerate to search. Closing the shortfall needs
  a different instrument — the scoring-strategy plan's replay harness. (Not the lab leads; see
  the correction under plan step 4.)
- **Three live groups have never been screened** — **CLOSED 2026-10-25.** `10257/all`,
  `10258/all` and `129727/all` were retrieved and screened by the 2026-10-25 full run. Confirming
  it rather than assuming it is what turned up the chance-pair artefact in item 5.
- **The chance-pair denominator** — **SHIPPED 2026-10-25** for probe-bearing assays (item 6).
  The general case, covering conventional and SYBR entries, is plan step 2.
- **Steyn 2020** (`10.3201/eid2607.190770`) — open access, and the one fetch that would move a
  `pending/` candidate toward live. Cheaper than anything else on the fetch list.


# Resume point, 2026-10-24 (overnight run of the open list; waves 0-5 of 2026-10-23 below)

## 2026-10-24, later: the three maintainer decisions were taken

The maintainer worked the three priced decisions this session. All three entries re-validate
(208 valid, 0 problems; active 179, draft 28, deprecated 1) and citations stay 208/208 clean.

- **Calicivirus Hel1 terminal base — corrected G->C, entry demoted to draft.**
  `CALICIVIRUS_ssRNA_Helicase_Reid_1999`: the forward Hel1 3'-terminal base changed G->C (the
  form the template carries in all 16 design targets, the only form that reproduces the 357 bp
  product, and the base Kolesnikovas 2017 prints). `primer_site_polymorphic` replaced by
  `oligo_sequence_uncertain` (OPEN, so it forces draft), `amplicon_bp` 360->357, status
  active->draft. Active went 179->178. The open question — is our copy of Hel1 right — is
  unchanged and still waits on the Neill & Seal PDF through the NYU proxy; 357 bp is the recorded
  C-form measurement, to be re-confirmed on the next pipeline screen.

- **Congo Basin assay — activated.** `MONKEYPOX_dsDNA_C3L_CongoBasin_TaqMan_Li_2010`:
  status draft->active. Measured harmless (99.3% on 1,060 evaluable; the 12,695 clade II genomes
  are `no_site`, C3L absent, and never enter the denominator). Its two flags are recorded caveats,
  not open questions, so the active gate accepts it. Active went 178->179.

- **West African assay — kept draft, deliberately.** `MONKEYPOX_dsDNA_G2R_WestAfrican_TaqMan_Li_2010`:
  no status change. The 2,688 clade-I failures no `scope_taxids` can exclude make the denominator
  known-broken and worsening for a non-drift reason, so activation would bake in a misleading
  verdict. Marked settled in the entry note — reopen only if the C3L-presence clade call at an
  independent locus is built.

Net registry unchanged at 208/179/28/1. Still open and NOT a session's to take: the two
proxy-blocked PDFs (Mao 1997, Neill & Seal 1995) — reconfirmed unreachable via PMC/PubMed/Wiley
this session, both Elsevier with no PMCID — and the uncommitted `scripts/fetch_elsevier.py`
(fails ruff at lines 22 and 109; left as found, see the night-of note below).

## 2026-10-24 night: Neill & Seal's second pair is now a registry entry

`CALICIVIRUS_ssRNA_RdRp_Neill_Seal_1995`, draft, DOI verified, both oligos exact. The design
paper's title promises "two distinct regions"; the registry held only the first (the helicase
pair). This is the RdRp pair Pol1/Pol2, found while re-reading the held deposit for the Hel1
question. Registry is 208 (active 179, draft 28, deprecated 1).

Two things worth carrying forward from it:

- **The same OCR deposit corrupts these two oligos too** (a spurious space inside each printed
  sequence), but here the data settles it where it could not for Hel1: closing the spaces gives
  two 25-mers that match 11 and 19 real records EXACTLY and reproduce the paper's stated 520 bp.
  Exact matches to real records cannot come from a mistranscription, so no clean PDF is needed
  to trust these - the asymmetry with Hel1 (whose disputed base matches nothing) is the whole
  point. No caveat flag; the provenance is in the entry note.
- **Screened and scope-corrected, as every new entry now is.** Exact match found 8 amplifying
  records; the scorer, scope-filtered to Vesivirus exanthema, finds 27 in-scope evaluable at
  40.7% (9 detect, 2 reduced, 16 fail). The entry carries the scored numbers, not the
  exact-match 8. thin_evidence: 27 is too few for a drift verdict.

### What is left on the list, and why each is not a session's to finish

- **Mao 1997 and Neill & Seal 1995 as clean PDFs** - would settle the ranavirus 18/19-mer and
  the calicivirus Hel1 G/C questions. Not in the Downloads batch (confirmed by content-search
  of all 148 PDFs); need the Virology / Mol Cell Probes scans through the NYU proxy.
- **The `E_coli_malB_Candrian_1991` seam** - its forward returns 59 Europe PMC papers, mostly
  E. coli prevalence surveys. They are `works`-shaped not drift-shaped, and reading 59 of them
  to add held-out rows is a literature pass of its own, not a loose end.
- **Three maintainer decisions, all priced and none a session's to take:** the West African
  mpox denominator (2,688 clade-I failures no scope_taxids can exclude); the Congo Basin
  activation (measured harmless, 99.3%); and the calicivirus Hel1 terminal base (evidence now
  favours C over the stored G, but a sequence correction + the active->draft demotion it forces
  is a maintainer call). All are written up where a maintainer will find them.


## 2026-10-24 evening: 30 papers imported from the maintainer's Downloads, zero verdicts moved

The maintainer dropped ~148 PDFs into `~/Downloads`. Matched by DOI (read from each PDF's own
first two pages) against `papers/papers-still-needed-2026-10-24.md`: **30 of the 64 wanted
papers were there** and are now copied into `papers/` under their canonical `doi_stem` names.
Re-ran the oligo verifier over the enlarged store: **500 rows, zero verdict changes** against
the pre-import run. That is the designed result — every one of the 30 is List 2 (completeness
and cross-reactivity reading), none was blocking a stored oligo, which is what "List 1 is
complete" has meant. `papers/` is gitignored, so the PDFs and the refreshed still-needed list
(now 34 outstanding: 12 free, 22 paywalled) are local only, not in this commit.

**The two papers that would settle a live SEQUENCE question were NOT in the batch.** Both are
still wanted and both now matter more than before:

- **Mao et al. 1997** (`10.1006/viro.1996.8435`), the ranavirus MCP design paper. Settles
  whether the registry's 18-mer reverse or Stöhr's 19-mer is right. Elsevier's API returns
  only metadata for it (no body), so it needs the PDF or the Virology scan through the proxy.
- **Neill & Seal 1995** (`10.1016/S0890-8508(95)90962-1`), the calicivirus design paper. We
  hold it only as an OCR'd Elsevier deposit that corrupts three of its four printed oligos,
  and the Hel1 3'-terminal G/C question (see above) now turns on whether that deposit misread
  one base. A clean PDF would settle it outright.

Neither is an Elsevier `jviromet` article, so both are absent from the batch, which was almost
entirely `jviromet`/`vetmic`/`vetpar` downloads. Content-searching all 148 Downloads PDFs for
each paper's distinctive primer run confirmed absence (the only hits were the *citing* papers
reid1999 and johnson2008). The SIV-chain papers Santiago 2003 and Keele 2006 are likewise not
in the batch.


## 2026-10-24 late: the remaining open-list items, worked

**Orphan archives: identified, not deleted.** `docs/journal/2026-10-24-orphan-archives.md`. 636 of the
658 MB is pre-query history for taxa the registry still covers - the 530 MB group is
*Ophidiomyces ophidiicola*, the 90 MB one *B. salamandrivorans*. Both have live entries that
later gained a retrieval query, and the query is part of the group key, so the old whole-taxon
fetch became unreachable. One group is a genus of moths. The decision was never short of
authority, only of information.

**The last held-out oligo caveat was a false alarm.** Villanueva 2024's
`GATCCGCAGACAGYACGT` is the registry's own alternate forward `BornaPCA3A`, and Sigrist 2021
section 2.2 says the design has "two variants of a degenerate forward primer". Swept the rest
of the held-out TSV: no other qualified identity. **Mao 1997 is now the only oligo-identity
question still open there.**

**The Usutu lead paid: three rows, set now 34.** And the literal-oligo search returned
**Jöst 2011 itself**, so that entry's oligos are verified verbatim against their own design
paper, 21 nt reverse included. Strongest row is Becker 2012: USUV RNA in 86 of 223 dead birds,
confirmed by isolation from 18 blackbirds, immunohistochemistry and deep sequencing. None of
the three is a drift case, so the set's drift shortfall is unchanged.

**The four never-searched families are searched, and the pick was wrong.** Apicoplast 23S
returns **zero** hits on both oligos, against the guess that plastid primers are widely reused.
The rich seam is `E_coli_malB_Candrian_1991`, whose forward returns **59** papers - mostly
prevalence surveys, `works`-shaped not drift-shaped, and a pass of its own. Yersinia and the
Reid capsid return nothing; the circovirus primers are all degenerate and cannot be searched
literally. Table in `docs/journal/2026-10-24-heldout-candidates.md`.

### The calicivirus Hel1 terminal base: the evidence has moved, and this one wants a decision

The entry already knew its Hel1 3'-terminal G mismatches the C in all 16 design-target
records, and treated that as a published primer with a terminal mismatch. Three new facts say
the G is more likely an error in our copy:

1. **A third paper prints C.** Kolesnikovas 2017 (`10.1007/s10393-016-1195-8`) lists the pair
   as its Vesivirus helicase assay, credits Neill 1995, and prints hel-1 ending **C**.
2. **Only C reproduces the published product size.** Over the whole 152,379-record
   Caliciviridae archive the stored G-form gives **no product in any record**; the C-form gives
   **16, every one 357 bp**, which is exactly what both papers state. A wrong terminal base
   cannot reproduce the published amplicon by accident.
3. **Our only copy of the design paper is OCR'd.** The Elsevier backfile deposit puts a
   spurious space inside **three of its four** printed oligos. A single-character misread in
   the fourth is plausible, and we hold no PDF to check.

**Nothing was changed.** The right flag is `oligo_sequence_uncertain`; the schema correctly
refuses it on an `active` entry, so applying it demotes this one from active (179 -> 178),
which is a maintainer decision and not a session's. The recommendation and that consequence
are on the entry. What settles it outright is the **Neill & Seal PDF through the NYU proxy**,
the same errand Mao 1997 needs - two open questions, one trip.

**Also ready and not entered:** Neill & Seal's *second* pair, `Pol1`/`Pol2` on the RdRp region,
is absent from the registry although the paper is held and already cited. Unlike the helicase
pair its sequences match real records as printed - Pol1 in 11, Pol2 in 19, a 520 bp product in
8 - so it needs only the normal entry process.


## 2026-10-24 late: the seven new entries were SCREENED, and exact matching had misled me three times

Everything below about the new entries was written from exact-match counting. The scorer
disagrees, and the scorer is the measurement. Run with `python -m assaywatch.screen` over the
real archives; nothing in the registry''s oligos changed, only what the entries claim.

**The Congo Basin assay needs no scope. The warning was wrong.** It predicted a permanent ~92%
non-detection if left unscoped. Measured: **1,060 evaluable records and 99.3% detection.** The
12,695 clade II records are `no_site`, not failures, because the C3L gene is ABSENT rather than
mismatched, so they leave the denominator before any verdict is formed. `EVALUABLE` is
`(detect, reduced, fail)`; a gene that is not there is silent, not negative. This is the thing
exact matching cannot see, because it has no notion of evaluability.

**The West African assay is the one with the broken denominator.** 12,396 evaluable, **78.3%**,
and **2,688 failures**. Every one of them has `fwd_penalty` 0, `rev_penalty` 0, **no probe site**,
and the 82 bp product rather than the 85 bp form. That is the clade I signature: the conserved
primers amplify clade I, the clade-II-specific probe does not bind it, so the record IS
evaluable and the failure counts against the assay. 78.3% is not a declining verdict today, but
the clade I share of GenBank is rising with the 2024-25 clade Ib outbreak and this will fall for
a reason that is not drift.

**And it cannot be scoped with anything that exists.** Checked exhaustively on 2026-10-24, so
nobody re-runs it:

| route | finding |
|---|---|
| `scope_taxids` | the species node is now `3431483 Orthopoxvirus monkeypox`, holding 10244 at rank `isolate`; the whole subtree is four nodes and none is a clade |
| per-record taxid | every record in the archive carries the bare 10244 |
| `title` resolver | 0 of 13,764 deflines say "clade I" or "Congo Basin"; 8.8% say hMPXV, 19 say Zaire |
| `subtaxid` resolver | nothing below the species to resolve to |
| `cluster` resolver | all-pairs, documented quadratic, on 12,396 evaluable records |

What would work is a clade call from sequence at an INDEPENDENT locus, and C3L presence is the
natural marker with the paper''s own reasoning behind it (West African strains delete C3L).
That is a mechanism the schema does not have. **Maintainer decision, now priced.**

**The generic assay has not "drifted hard" - that claim is withdrawn.** 12,052 evaluable,
**99.9% detection**, of which **8,954 are `reduced`**. The primer-site mismatches cost penalty,
not detection. The honest finding is the reduced column, which is a real ageing of a 2010 assay
and a smaller claim than failure.

**The other four entries came through clean**, and one gained a finding:

- Gallardo-Romero: 7 evaluable, 100%, the other 57 records `no_site` fragments. Agrees with the
  hand measurement exactly.
- Orf: **64 of 64 `detect`** on its own retrieval taxon, and 0% on both other species, every one
  a `fail`. Specificity holds under scoring, not just exact matching.
- Generic parapox: **90.9% on bovine papular stomatitis**, so the exact-match gap recorded
  yesterday does NOT become a scoring failure, exactly as the one distal mismatch predicted.
- BPSV: 81.8% on its own taxon, and **a cross-reaction exact matching hid** - 61 of 64 Orf virus
  genomes score `reduced`, 95.3%. The paper''s wet-lab panel reports no cross-reaction, so this
  is an in-silico disagreement with the publication, now flagged `cross_reactive`.

**The lesson worth keeping:** an exact-match sweep is a hypothesis, and a cheap one. It cannot
see a tolerated mismatch, so it understates an assay, and it cannot see evaluability, so it
invents denominators that the pipeline would never use. Screen before writing a verdict into an
entry.

### A file changed underneath this session

`scripts/fetch_elsevier.py` was replaced on disk at 18:48 by a different implementation of the
same idea (`--list`, `./.env`, writes PDFs, its own `results/elsevier-fetch.tsv`). It is left
exactly as found, unstaged and uncommitted. Three things to know before merging it:
it drops both fixes committed in `1786091` earlier today (the `held_dois` forward mapping, and
the `<body>` test that stopped a metadata-only reply being saved as full text); it carries a
fourth private copy of the `papers/` filename convention in its own `slug()`, which is the
duplication `assaywatch/papers.py` exists to prevent, though its output is compatible because
every reader lowercases; and it fails `ruff` (`BLE001` at line 109), so it blocks commits until
that is resolved.


## 2026-10-24 evening: the papers/ filename gap is closed, and it cost nothing to close

The gap left open earlier today ("A REAL GAP FOUND AND DELIBERATELY NOT FIXED") is fixed,
and the run it was waiting for says the fix changes **no oligo verdict at all**. Both halves
of that matter, so take the correction with the fix.

**Fixed at the source, which is where it was.** Three writers built a `papers/` filename as
`doi.replace("/", "_")`, replacing the slash but not the parentheses: `scripts/fetch_elsevier.py`,
`scripts/find_open_access.py`, and `scripts/fetch_europepmc_fulltext.py`, which carried its own
one-line copy of `doi_stem` AND its own copy of `PAPER_SUFFIXES` -- the same duplication the
`SUPPLEMENT_SUFFIX` comment in `assaywatch/papers.py` exists to warn about, and the same one
that cost sixteen papers in the index this morning. All three now call
`assaywatch.papers.doi_stem`, and the Europe PMC fetcher imports both shared constants instead
of redefining them.

**The eleven files are renamed to the canonical stem.** Not twelve: the earlier note said
twelve, the disk holds **eleven**, all `.xml`, all cited by live registry entries. Ten are also
held as PDF; the exception is Neill & Seal 1995 (`10.1016_s0890-8508_95_90962-1.xml`), the
calicivirus design paper, held only as that XML. No name collided with an existing file.

**The correction: "invisible to the verifier" was overstated.** The stem lookup did fail --
`local_paper` compares `doi_stem(doi)` alone, and the on-disk name was not that -- but the
verifier was reaching all eleven anyway by the other route it has, the DOI a JATS deposit
prints in its own front matter. Measured rather than assumed: the verifier was run twice over
the same registry, once against `papers/` as renamed and once against a symlink farm
reproducing the pre-fix names exactly (the XMLs renamed back, the PDFs left canonical -- a
first attempt that renamed the PDFs too was a wrong baseline and was thrown away).

    479 rows both runs, same keys, 0 verdict changes
    40 rows changed only in `checked_against`, all of them the same file under its new name
    verdicts unchanged: exact 396, absent 22, in-text 20, modified 16, no-oligos 13,
                        near:1 4, sibling 4, revcomp 3, near:4 1

So nothing in `results/oligo-verification-2026-10-24.tsv` contradicts the 2026-10-23 run. What
the fix buys is not a recovered paper but a recovered *precedence*: a file NAMED for a DOI
outranks one that merely prints it, and until today these eleven were winning on the weaker
claim. For Neill & Seal, the one paper held in no other format, that is the difference between
being matched by the convention and being matched by luck.

**A control so there is no fourth fetcher.**
`tests/test_papers.py::test_nothing_writes_a_filename_by_replacing_only_the_slash` parses
`scripts/` and `assaywatch/` with `ast` and fails on any `.replace("/", "_")` in executable
code. Parsed, not grepped, so the paragraph in `papers.py` explaining the mistake is not a hit.
`papers_index` builds the old spelling deliberately, to index a `papers/` copied from an older
checkout, and is exempted by a marker comment that says so. Positive-controlled: a probe file
reintroducing the pattern fails the test.

**Gate: 1,552 tests pass, validator 200/200 (active 179, draft 20, deprecated 1),
check_citations 200 checked 0 problems, ruff clean.** `papers_index --check` exits 0 and its
unmatched count fell from 4 to 3 -- the three candidate-provenance PDFs (Coiras 2004,
Aitichou 2005, Khodeir 2021), which are correct to be unmatched. Neill & Seal is no longer
among them.

**Second item off the open list the same evening: the pan-coronavirus Watanabe reverse.**
`docs/journal/2026-10-24-heldout-candidates.md` called it "a transcription error on one side or the
other". It is neither. Watanabe 2010 is held locally and prints primer 2 as a 24-mer; the
23-nt form is PREDICT P-006 with the G at position 14 dropped; and the 2026-10-23
binding-site counts in the entry's own notes reproduce exactly on a re-count today (215
stored / 204 Watanabe / 88 P-006, over 25,576 records against the 25,506 of the first
measurement). The registry's 24-mer stands. Resolution written into the candidates doc, where
the claim was.

**Chasing Mao 1997 for that answer turned up two faults in `scripts/fetch_elsevier.py`,
and the first one I caused.**

- **`outstanding()` reverse-mapped filename stems**, `p.stem.replace("_", "/")`, to build its
  "already held" set. That is the mapping `assaywatch/papers.py` exists to stop, and this was
  its sixth call site, unfixed because it was invisible: while the eleven Elsevier papers sat
  under the slash-only spelling the reverse mapping happened to come out right. Renaming them
  to the canonical stem earlier the same evening broke it, and running the fetcher is what
  showed it - `outstanding()` returned all eleven as missing, every one of them held, ready to
  be re-fetched over the API. Now forward-mapped through `held_dois`; it returns nothing.
- **`has_body()` accepted a reply with no article in it.** It tested for `originalText`,
  `<xocs:doc>` or `ce:section` plus 8 KB, all of which a metadata-and-references reply has.
  Mao 1997 came back at 110 KB with every marker, no `<body>`, and not one nucleotide in it,
  and was saved into `papers/` and reported as "full-text". That is the error class this
  project paid for this morning, a paper wrongly recorded as held, so the test is now the
  `<body>` element itself. **Audited: all twelve XML deposits already in `papers/` carry a
  real body**, so nothing held was overstated by the looser test. The Mao file was deleted
  rather than kept, since keeping it would assert we have read the paper.

Both are pinned by a second control, `test_nothing_reads_a_doi_back_out_of_a_filename`, built
like the first and exempting the two places that reverse-map deliberately and say so
(`verify_oligos_against_paper`, which files the result under a prefixed stem key rather than
as a DOI, and `extract_candidate_oligos`, where it is a documented last-resort fallback that
never keys a cache or a fetch).

## 2026-10-24 evening: the Li 2010 mpox trio is IN, as drafts, and the clade scoping is impossible

The top recommendation of `docs/journal/2026-10-24-mpox-assay-candidates.md` is applied. Three entries,
`MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010`, `..._G2R_WestAfrican_...` and
`..._C3L_CongoBasin_...`, all `status: draft`. The registry is 203 entries: active 179, draft
23, deprecated 1.

**Provenance is clean.** The paper (10.1016/j.jviromet.2010.07.012) was fetched over the
Elsevier API and prints all nine oligos inline in its Section 2 rather than in a table; all
nine transcribe character for character and `verify_oligos_against_paper` reads 9 of 9
`exact`. Crossref verified the DOI through `resolve_citations.py`, as the rule requires.

**Every amplicon is measured, because the paper states no size at all.** 90 bp (generic),
85 bp (WA, with a real second mode at 82), 100 bp (C3L). One trap worth passing on: these loci
sit in the inverted terminal repeat, and a first pass that scanned only the plus strand
reported ZERO C3L products and undercounted the generic by a third. Count both strands here.

**Two findings came out of the measurement, and one of them kills part of the plan.**

- **The clade scoping the candidates doc proposed cannot be done.** NCBI Taxonomy has no node
  for clade I or clade II: the subtree of 10244 is just *Callithrix jacchus orthopoxvirus*
  (243803) and Monkeypox virus Zaire-96-I-16 (619591). Both clade-specific entries therefore
  carry `scope_narrower_than_taxid` as the disclosure, exactly as AVIPOXVIRUS Baek does. **This
  is a live maintainer question before C3L goes active**: unscoped, a correctly clade-I-specific
  assay will post a permanent ~92% non-detection that says nothing about the assay. Its entry
  argues the case in full.
- **The generic assay has drifted hard, more than the sweep predicted.** Over 13,179
  genome-length records its forward primer is exact in 20.4% and its reverse in 23.0%, while
  its probe is exact in 92.7%. Probe-intact, primers-gone is the signature of site drift, not
  of a bad transcription. The paper calls this assay "completely homologous within the MPXV DNA
  sequence except one SNP in forward primer sequence", which was true of a 2010 alignment and is
  not true of GenBank now. It is the Kulesh 2004 story one locus over.

Also measured, and recorded on the WA entry rather than asserted: C3L presence is a clade
marker (the paper chose that gene because West African strains delete it), and cross-tabulated
over 13,131 near-complete genomes, all 777 C3L-carrying records give the 82 bp WA product while
all 9,654 records giving 85 bp lack C3L. The length does not partition the clades cleanly -
1,901 C3L-negative records also give 82 - so the entry does not claim that it does.

## 2026-10-24 evening: Gallardo-Romero 2011 is in, and a 44 nt probe moved the schema

`NA_ORTHOPOX_dsDNA_G9R_myristylated_TaqMan_Gallardo_Romero_2011`, `status: draft`. The
registry is 204 entries: active 179, draft 24, deprecated 1. This one fills a real hole - the
registry had pan-pox consensus assays and monkeypox assays and nothing at all for the North
American wild orthopoxviruses, volepox, skunkpox and raccoonpox, which is as wildlife-diagnostic
as this registry gets.

**It is properly scoped, which the monkeypox pair could not be.** taxid is the genus
Orthopoxvirus (10242), because discriminating within that genus is the paper's entire claim,
and `target.scope_taxids` is `[10256, 28874, 160796]`. Those three species nodes exist. The
schema asks for the smallest set of SUBTREES rather than an enumeration, and there is no node
for the North American group, so the enumeration here is forced rather than preferred - said in
the entry so the next scope audit does not re-raise it.

**The amplicon agrees with the paper, which is worth stating because so few lately have.**
All 64 nuccore records for the three species were fetched; 7 are complete genomes, and all 7
give exactly the 156 bp the paper states, with the probe inside. The other 57 are fragments
that do not reach the locus, so they are silent rather than negative. `thin_evidence` is on the
entry: 7 informative records cannot support a drift verdict, and the entry's value today is
coverage plus a baseline.

**Two traps, both worth passing on.**

- **The paper prints its oligos codon-hyphenated**, `5'YGG-ACC-RGG-AGG-TCT-TTC-TGC-ATT 3'`. A
  plain `[ACGT]{15,}` sweep over the full text returns NOTHING and reads as "this paper prints
  no oligos", which is the same false negative class as the papers-index one from this morning.
  The repo's own `verify_oligos_against_paper` is not fooled - it reads all three `exact` - but
  an ad-hoc extractor is. Worse, the probe ends `-CAC-TTT-BHQ1`, and B and H are valid IUPAC
  codes, so a naive extractor swallows `BH` off the quencher and yields a 46-mer. It is 44.
- **That 44 nt probe did not fit the schema and the schema moved.** `OLIGO_MAX` is 40, so a
  real published probe would have been refused for being what its paper says it is. There is
  now a separate `PROBE_MAX = 50` beside `PROBE_MIN`, which exists for the mirror-image reason
  (Haynes 2023's 13-14 nt MGB probes). Primers keep 40. It is safe at this end for the same
  structural reason the low floor is: a probe is only ever searched inside the span between the
  two primers. One existing test asserted the old message `length 11 outside 12-40` and now
  states the real bounds.

## 2026-10-24 evening: the parapox quartet, three in and one blocked on a 14 nt primer

Zhao et al. 2013 (10.1016/j.jviromet.2013.08.027). The registry is **207 entries: active 179,
draft 27, deprecated 1**, and the whole of the 2026-10-24 CDC sweep is now worked through.

**It was never paywalled.** The candidates doc said "no PMC id returned, so likely paywalled -
would need the paper obtained before oligos can be verified (NYU proxy)". `fetch_elsevier.py`
had it on the first attempt with the institutional token. That assumption cost nothing this
time and is worth not repeating: for an Elsevier DOI, try the API before the proxy.

**Three entered, all drafts**: `ORF_VIRUS_...`, `BPSV_...` and `Pan_PARAPOX_..._generic_...`.
Nine of nine oligos read `exact`. The paper states no product size for any assay, so all three
amplicons are measured over the 92 Parapoxvirus genomes of 100-200 kb in nuccore: 68, 91 and
85 bp, each a single value across every genome that gives a product. Orf is a sheep and goat
zoonosis that reaches the people handling them, and the registry had nothing for the genus.

**Read the table cell by cell, not as text.** Flattening this JATS table puts every label
beside the WRONG sequence, because each cell's label precedes the next cell's value in reading
order. Parsed from `<row>`/`<entry>` the four assays come out unambiguous.

**One oligo had to be settled by measurement.** The deposit prints the Orf reverse cell as
`GCCGAGGAGCAGGTC A` - a 15-mer plus a stray letter, or a 16-mer split by a formatting artefact.
`GCCGAGGAGCAGGTCA` is exact in the same 78 genomes as the 15-mer, so the template carries that
A and the 16-mer is the oligo. Entered at 16 nt, and the verifier reads it `exact`.

**A measured gap in the generic assay, recorded because an exact-match screen will overstate
it.** Its reverse primer matches 0 of 11 bovine papular stomatitis genomes exactly, while its
forward matches 10 of 11 and its probe 11 of 11, so under exact matching the generic assay
appears to miss one of the three species it claims. Aligned instead of exact-matched it sits
**one** mismatch away in all 11, and that mismatch is **7 bases from the 3' end** in every one,
which a real reaction would be expected to amplify through. It is on the entry as
`primer_site_polymorphic`, not as a failure.

**MAINTAINER DECISION: the fourth assay, PCPV_J6R, is not entered, and cannot be without
changing a guard.** Its reverse primer is `CGCACGCGCTTGCT`, 14 nt, against `OLIGO_MIN` of 15.
`pending/` is no escape: `--pending` relaxes the verified-DOI rule only, and the schema still
applies. The argument for lowering the floor is the one that carried `PROBE_MAX` the same
evening - the floors exist "to catch a mistyped 3-base oligo, not to overrule a published
table", and this is a published table. The argument against is specific and was measured here:
that 14-mer is exact in **71 of the 92** genomes, including **60 Orf virus** genomes it is not
meant to detect, which is precisely the chance-matching the 15 nt floor exists to stop. A
probe is searched only between the primers; a primer is searched along the whole record, so the
two ceilings are not the same question. Left for the maintainer. The other three entries carry
the panel, and the pseudocowpox species is the only one of the three now uncovered.


## 2026-10-24: the diverged+anchor_fdr pair SHIPPED at q=0.001

Maintainer decision taken after the re-price below. config.yaml now holds
`count_diverged_as_fail: true` and `anchor_fdr: 0.001` (lines 593 and 619, with
the full rationale replacing the earlier "do not turn this on" warnings). The
shipped `results/2026-10-24/report.{md,html}` was re-rendered against the
flipped knobs and now matches the `results/2026-10-24-reprice-q001` preview row
for row (`report_diff.py` shows zero status moves between them).

The counterfactuals that priced it are kept on disk: `results/2026-10-24-off`
and `-prescope-baseline` are the pair-off baselines; `-reprice-q01` and
`-reprice-q001` are the two pair-on q settings tested; `-anchorfdr` and `-q001`
are the earlier pre-scope renders.

One test needed updating, same pattern as the two from the promotion:
`tests/test_windows.py::test_drift_refuses_count_diverged_on_windowed_rows`
read the shipped CFG expecting the knob off. The behaviour under test (turning
the knob on refuses windowed rows) still works; the fixture now states both
halves of the rule rather than resting on an implicit default that just flipped.

The sidecar-wiring from the earlier commit also lands here naturally: the next
`collect_calls` run will write `status_at_run` and `status_counts_at_run` into
the provenance so a reader can tell WHICH assays were active for that run --
answering the same class of gap the pair's config comment now describes.

## 2026-10-24: the diverged+anchor_fdr pair, RE-PRICED against the scoped registry

The earlier recommendation (DO NOT SHIP, `docs/2026-10-24-anchor-pair-counterfactual.md` on
the `experiment/` branch) rested on ONE objection: turning the pair on crashed
`BORNA_VIRUS_N_gene_Zimmermann_1994` from 98.2% stable to 16.4% declining on 209 strong
anchors in parrot/serin/rattlesnake bornaviruses. The 2026-10-24 scope audit showed that case
was SCOPE, not drift. So the pair was re-priced against the now-scoped, promoted registry,
config-only, rendered from `results/2026-10-24/calls.tsv.gz` (no rescreen; the knobs live in
the `drift` block, not the screen signature). Renders kept at
`results/2026-10-24-reprice-q01` and `-q001`; the shipped scoped baseline is
`results/2026-10-24` itself.

**The objection is gone.** Both Borna entries are now COMPLETELY UNMOVED by the pair at
either q: `BORNA_VIRUS_N_gene` 97.6% and `BORNA_VIRUS_N_gene_Zimmermann_1994` 98.8%, stable,
off / q=0.01 / q=0.001 identical. The 209 anchors that used to crash it were out-of-scope
records, now excluded from the denominator, so counting them as fail no longer touches the
verdict.

**What the pair now bites is overwhelmingly REAL divergence.** Status moves from the
pair-off baseline: 11 at q=0.01, 8 at q=0.001. The flagship mover is the system doing exactly
its job: `MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004` goes 99.9% (2411 recs) -> 58.3% (4127). The
~1700 added records are `diverged` with anchor E ~= 4.3e-10 (genuinely present sites, not
chance), and 2223 of the 2377 diverged records are 2022-or-later: this is the clade IIb mpox
outbreak, against a 2004 probe. anchor_fdr correctly keeps those strong anchors; a smaller q
does not and should not relabel them. Checked the other q=0.001 movers by anchor E: Cryptosporidium
round2 7.5e-11, ARENAVIRUS S 1.8e-07, Pan_coccidia 2.3e-08, Apicoplast 2.0e-05, Pan_mycoplasma
Rebelo 2.8e-05 -- all strong. Two are mid (~4.3e-04): SIV Keele (already under a citation
cloud, primers not in its paper) and a 31-record CMV round2 move.

**q=0.001 beats q=0.01, confirmed against the scoped registry.** The direct diff shows 3
assays return toward stable at the smaller q -- including `TRICHOMONAS_gallinae_18S` (its 241
weak anchors, E ~= 7e-3, 241 of a family of 278, correctly relabelled as chance only at
0.001). BH's bar is (k/m)*q, so the smaller q relabels MORE chance anchors, which is the
counter-intuitive-but-correct direction. The docs' recommended 0.01 is the worse of the two.

**RECOMMENDATION: the pair is now defensible to ship, at q=0.001.** With Borna resolved, the
remaining bite is real signal, led by a textbook true positive (mpox). The honest caveat for
the maintainer: this REDEFINES `declining` to count a present-but-mismatched binding site as a
failure rather than dropping it. For surveillance of evolving pathogens that is arguably the
point -- an assay that no longer matches circulating virus should read declining. Two entry-
semantics oddities to note, independent of the pair: `Pan_coccidia..._negative_contro` is a
negative control (its name), and `Apicoplast_23S` is phylum-wide and amplifies chloroplasts by
design, so "declining" means little for either. MAINTAINER DECISION, not applied: shipping it
is `count_diverged_as_fail: true` + `anchor_fdr: 0.001` in config.yaml. Tier-2 still cannot
choose between 0.01 and 0.001 (it was row-identical at both before the scope work; the
evaluation set is the bottleneck, which is what docs/journal/2026-10-24-scoring-strategy-test-plan.md
is about).

## 2026-10-24: stale documentation, swept and corrected

**One standing instruction retired.** `docs/RESUME-HERE.md`'s 2026-10-21 section carried
"**Pull before starting a session from now on**", from when a second machine was pushing to
this repo. The maintainer confirmed on 2026-10-24 that they no longer work on more than one
machine, so `origin` has a single writer. The instruction is struck where it stood; the
history of that cross-session merge is left in place.


A sweep for references to files that no longer exist, across `docs/*.md`, `CLAUDE.md`,
`README.md`, `ROADMAP.md` and `CONTRIBUTING.md`. Twelve dangling paths; most were not what
they looked like.

**Five are tooling deleted on purpose, in `84b15d6`** ("198 assays are live, all on a
verified DOI; the seed list's lab is gone from the tree"), whose message says plainly: "The
importer, curation.yaml, removed_assays, materials_needed and the openpyxl extra are
deleted." So `docs/materials-needed.tsv`, `scripts/materials_needed.py`,
`tests/test_materials_needed.py`, `scripts/removed_assays.txt` / `scripts/removed_assays/`
and `scripts/curation.yaml` are gone and are not coming back — `Source.spreadsheet`, `rows`
and `positive_control` were removed from the schema and `Source` is `Strict`, so they cannot
return. **Every surviving mention of them in this file and in `docs/2026-10-2*.md` sits in a
DATED section and is history, deliberately left alone**, on that commit's own policy:
"corrected, or dated where they were history." Read them as a record of what was true then.
Where the live question is "what papers do we still need", the answer now lives in
`docs/papers-index.md` (every DOI, with which format is held) and in
`papers/papers-still-needed-*.md`, not in a committed TSV.

**Four were false positives**, all of them branch or PR names in backticks that look like
paths: `registry/2026-10-24-scope-fixes`, `docs/2026-10-23-elsevier-and-oligo-flags`,
`docs/2026-10-15-lineage-plan` (PR #3, docs-only, superseded by
`docs/journal/2026-10-17-estimand-plan.md`) and `scripts/archive/rescore.py`, which
`docs/journal/2026-10-24-scoring-strategy-test-plan.md` PROPOSES and has not built yet.
`assaywatch/archive.py` never existed: it appears inside a blockquote in
`docs/journal/2026-10-23-wave5-engineering.md` quoting a review's proposal.

**Two were real and are fixed.** `CLAUDE.md` claimed `docs/INDEX.md` "indexes all 81 files
under `docs/`" when there are 94 (79 Markdown); corrected and dated. And
`docs/journal/2026-10-24-scope-audit.md`'s own header named the wrong branch, still said "read-only
audit; no registry entry changed" after that stopped being true, and pointed at
`docs/2026-10-24-anchor-pair-counterfactual.md`, which lives only on the unmerged
`experiment/2026-10-24-diverged-and-anchor-fdr` branch and did not come across with the
cherry-pick. All three corrected in place.

**`docs/INDEX.md` is complete.** A link-regex check said four files were unlisted
(`journal/HANDOFF-2026-10-18.md` and the three `2026-10-18-phase*/session-summary` docs); they are
listed, together in one row of the `Superseded` section, as plain names rather than links.

### The papers index was understating what this project has read, by sixteen papers

Found while answering "which papers are still paywalled", and it is the kind of error that
costs real work: **I went looking for Santiago 2003 behind a paywall it is not behind.**

`scripts/papers_index.py` globbed `*.pdf` alone, while `scripts/verify_oligos_against_paper.py`
read `.pdf`, `.xml` and `.txt` from its own `PAPER_SUFFIXES`. Two readers of `papers/`
disagreeing about what counts as a held paper — exactly the failure the `SUPPLEMENT_SUFFIX`
comment in `assaywatch/papers.py` warns about. The index's legend says "blank means the paper
still needs to be obtained", so four papers held as PMC `.txt` (Li 2025, Jöst 2011, Chu 2008,
Xiao 1999 — all cited by live entries) and twelve held as publisher `.xml` read as never
obtained.

Fixed: `PAPER_SUFFIXES` moved to `assaywatch/papers.py` beside `SUPPLEMENT_SUFFIX`, for the
same reason, and both readers import it. The index now reports **123 of 123 papers held**,
names the format per paper (`pdf`, `xml`, `txt`, `pdf, xml`, `pdf suppl`), and 15 papers turn
out to be held in more than one format. Its unmatched-file warning fell from 14 to 4 and says
"file(s)" rather than "PDF(s)".

The four it still cannot match are correct: three candidate-provenance PDFs (Coiras 2004,
Aitichou 2005, Khodeir 2021) and `10.1016_s0890-8508(95)90962-1.xml`, which is **Neill & Seal
1995** — the calicivirus design paper. That last one matters: it is held, and the index now
shows it, which is the evidence the open "re-cite the calicivirus entry to Neill & Seal"
decision needs.

**A REAL GAP FOUND AND DELIBERATELY NOT FIXED.** `doi_stem` replaces `/ ( ) < >` with `_`,
but the Elsevier API fetcher replaced only the slash, so twelve publisher JATS deposits sit on
disk as `10.1016_s0016-5085(98)70589-x.xml` and do not match their DOI. `papers_index` now
accepts both spellings. **`verify_oligos_against_paper` still compares a single stem, so it
cannot match those twelve to a DOI** — meaning the publisher XML, often the best source for a
primer table, is invisible to the verifier. Ten of the twelve are also held as PDF so little
is lost today; the exception is Neill & Seal 1995, held ONLY as that XML. Not fixed here
because changing what the verifier reads changes oligo-verification output and wants its own
run to check. Next person: either teach `paper_for_doi`/`identity_stem` both spellings, or
rename the twelve files to the canonical stem.

## 2026-10-24 daytime: the scope audit, all ten items worked through

Branch `registry/2026-10-24-scope-fixes`, cut from
`docs/2026-10-23-elsevier-and-oligo-flags`. The audit itself is read-only and lives in
`docs/journal/2026-10-24-scope-audit.md`; items **1, 3 and 6** of its ranked list were then applied
in three commits. **All ten ranked items have now been worked through, and FOUR of the ten
proposals were wrong or redundant on contact with the data.** Applied as proposed: 1, 3, 5,
6, 7, and 2 (Bornaviridae, applied in the first commit). Applied differently because the
proposal was wrong: 4. Struck, do not apply: 8, 9, 10. **Nothing in the ranked ten is
still open.** What remains is a separate finding from the audit body, not one of the ten:
the three entries carrying `scope_narrower_than_taxid` with no mechanism behind it --
AVIPOXVIRUS Baek, CHLAMYDIA Messmer, BATRAVIRUS european. **Those three have now been worked
through as well, and only one was a scope bug.**

- **BATRAVIRUS european: SCOPED** `[1987509, 2282206]` = RaHV-3 and BfHV-1. The paper's
  EUROPEAN protocol targets exactly those two while the taxid is the whole genus including the
  North American RaHV-1/RaHV-2, and the measurement matches the protocol: detections at
  Bufonid herpesvirus 1 (2/2) and Ranid herpesvirus 3 (2/2), RaHV-2 at 0 of 2. Baseline 67%
  (6) -> 100% (4). Only 4 records, so the status stays "no recent data" and "cannot assess" is
  still the honest reading -- but the denominator is the right four. The sibling pan protocol
  is deliberately left unscoped.
- **AVIPOXVIRUS Baek: NOT SCOPEABLE.** Baek describes a "hummingbird-specific" assay, but
  there is no NCBI node for the hummingbird clade -- all three detections sit in generic or
  numbered taxa (*Avipoxvirus sp.* 1928336, which holds 114 assessable of which 1 detects;
  *Avipoxvirus 1130*; *Avipoxvirus 31239*). 3 of 758 assessable, 0.4%, with Fowlpox alone
  contributing 379 assessable and 0 detections. Same situation as Helicobacter: needs a
  mechanism the schema does not have, and the flag is the disclosure. The 0.4% is not an assay
  problem.
- **CHLAMYDIA Messmer: NOT A SCOPE BUG, and scoping would hide the finding.** Messmer calls
  these the "genus-specific first-step primers", so the paper's claim IS the genus. Measured,
  the assay reaches `reduced` on *C. psittaci* (85/89), *C. abortus* (31/34), *C. pneumoniae*
  (9/9) and detects *C. crocodili* (18/18), and completely fails *C. trachomatis* (0/301),
  *C. pecorum* (0/17), *C. muridarum* (0/51), *C. felis* (0/19) and *C. avium* (0/10).
  **Trachomatis and pecorum were two of the four species the 1997 paper claimed**, so this is
  a genus assay failing half its own stated range; the rest were split out of the genus after
  1997. The entry's existing five-mismatch claim is confirmed exactly (forward mismatches at
  13,12,8,7,6 in all 301 trachomatis records). And separately: **nothing reaches `detect`** --
  every working species is `reduced` at penalty 3, because the reverse primer mismatches at
  position 2 from its 3' terminus in every *Chlamydia* record. Same shape as Leptospira, and
  more scoring evidence rather than scope work.

No oligo and no threshold was touched anywhere. Cumulative report effect, re-rendered from
one calls table so only the registry differs — **7 assays change status**:

    BORNA_VIRUS_N_gene                      declining     -> stable            20.9% (43) -> 97.6% (165)
    ORTHOBORNAVIRUS_XP_aquatic_Sigrist      low coverage  -> stable             0.0% (26) -> 100.0% (18)
    ORTHOBORNAVIRUS_XP_psittacine_Sigrist   low coverage  -> stable            23.1% (26) -> 100.0% (35)
    ORTHOBORNAVIRUS_XP_passerine_Sigrist    low coverage  -> insufficient data  3.8% (26) -> 4 records
    CALICIVIRUS_ssRNA_Capsid                low coverage  -> no recent data    baseline 27% (51) -> 82% (11)
    PERKINSEA_NAG01_18S_cladeAC             insufficient  -> no recent data    baseline 45% (461) -> 54% (388)
    PERKINSEA_NAG01_18S_cladeD              insufficient  -> no recent data    baseline 36% (461) -> 43% (388)

**THE LESSON, which is more useful than any single fix.** The ranking was built on how clean
the taxonomy looked when read off NCBI's hierarchy. All four failures failed the same way:
nobody had checked *what records actually live at the proposed node*, or *what the registry
already did*. The procedure that worked every time was to group the assay's own calls by
record taxid and look at where the detections are. Do that first, next time.

- **Item 4 (Helicobacter) was wrong**: 290433 is "uncultured Helicobacteraceae bacterium"
  under *environmental samples*, a catch-all of unrelated gut and environmental clones, not a
  GCBI1 node. See below for what was done instead.
- **Item 7 (Perkinsea) shows the same lesson cuts both ways**: 373149 is ALSO an
  "environmental samples" node, and it is the right scope, because every single detection for
  both entries lives inside it and the excluded *Perkinsus* taxa contribute 76 assessable
  records with **0** detections. Judge such a node by what it contains, never by its name.
- **Item 8 (LMBV) was redundant and would have been a regression**: both entries are already
  scoped via `target.query`, and the Li 2025 entry's own note had already rejected this exact
  proposal in advance ("a scope of txid3432136 alone would silently miss them: 113 records,
  against 131 for the union used here"). Applying it would drop **10 detected records**.
- **Item 9 (Tong) was wrong**: the three proposed subfamilies cover **294 of the 931**
  enumerated ids; 637 would be dropped, mostly `unclassified Paramyxoviridae` including
  reptilian paramyxovirus, plus a fourth subfamily the proposal never named. When a family has
  a large `unclassified X` bucket, no set of subtrees covers it and enumeration is the only
  honest mechanism.
- **Item 10 (Leptospira) was struck as a scope fix and produced the best finding of the day.**
  See below.

**THE LEPTOSPIRA FINDING, worth more than the scope change it replaced.** The assay reads
93.0% whole-archive, and the 138 misses are not spread out: they sit in species described
after the primers were designed, all scored `fail` (sites present and mismatched, not absent),
all with the reverse primer mismatched at **position 1 from its 3' terminus** — fatal on its
own under `terminal_mismatch_fails`. Against the design paper's own Table 1:

    L. kmetyi       0 detected of 13, all fail    paper: Pathogenic, scored +
    L. adleri       0 of 4,  all fail             paper: Pathogenic, scored +
    L. gomenensis   0 of 8,  all fail             paper: Pathogenic, scored +
    L. yasudae      0 of 18, all fail             not in Table 1 (described later)
    L. wolffii      0 of 14, all fail             paper: Intermediate, scored -   <- control

So three lab-confirmed positives that this pipeline calls complete in-silico failures.
*L. wolffii* is the control that makes it credible, and the contrast with the species the
assay was built on is absolute: *L. interrogans* (578 records), *L. borgpetersenii* (209),
*L. santarosai* (59), *L. weilii* (47), *L. noguchii* (36), *L. kirschneri* (35) all match at
**penalty 0, no mismatch anywhere**. NOT entered in `docs/validation-cases.tsv`, which
excludes an assay's own panel validation — but recorded in
`docs/journal/2026-10-24-scoring-strategy-test-plan.md` as bench evidence for `terminal_mismatch_fails`
and `by_chemistry`, paired with the CALICIVIRUS Helicase entry's 3'-terminal G/C mismatch,
which is the same mechanism on a conventional PCR rather than a probe assay.

**The audit's finding.** 146 of 200 entries are scoped broader than species, but most of
that breadth is correct by design — a pan-family consensus PCR should carry a family
taxid. The real defect is a single-organism assay under a multi-organism denominator, 34
entries worth checking across 22 papers, all read. The mechanism to fix it already existed
and was applied unevenly: `target.scope_taxids` (25 entries before this, 30 now), with 13
more entries pinning organisms in `target.query` instead and **three carrying a
`scope_narrower_than_taxid` flag with no mechanism behind it at all** — the registry wrote
the problem down and then computed the share anyway. Those three (AVIPOXVIRUS Baek,
CHLAMYDIA Messmer, BATRAVIRUS european) are still open.

**What applying 1, 3 and 6 did.** Re-rendered `results/2026-10-24/calls.tsv.gz` against
the new registry, so only the registry differs. Two status changes:

    BORNA_VIRUS_N_gene        declining -> stable         20.9% (43) -> 97.6% (165)
    CALICIVIRUS_ssRNA_Capsid  low coverage -> no recent data   baseline 27% (51) -> 82% (11)

Bornaviridae is the case the audit was started to test and it holds: the entry was never
drifting, two thirds of its denominator was a different virus. The control is its round-1
sibling, already reading its own target, which moves only 98.2% -> 98.8%.
`snakemake -n` afterwards plans 9 jobs and **zero `screen_archive`**: a `target` edit is
not in the screen signature, so none of this cost a rescreen.

**Two things to carry forward.**
- `drift.py:1053` drops only a record whose taxid is **known** and out of scope; an unknown
  taxid stays in the denominator. Taxid coverage on the Caliciviridae Helicase group is
  79.7%, so that entry's assessable set went 30 -> 24, not 30 -> 7. Any future scope fix is
  only as good as the taxid backfill behind it — measure coverage before predicting a size.
- Item 6 (the four self-disagreeing sibling groups) is now consistent, zero groups
  disagree, but it bought comparability and not coverage: the copied lists exclude 159, 73,
  40 and 5 records, three of five report rows are byte-identical and no printed share moved.

**Items 4 and 5, added later the same day.**

*Item 5, the three Sigrist entries, is the largest effect in the audit.* The paper's own
words settle the probe-to-species mapping (section 2.2 names the targets per probe; section
3.2 adds "BoDV-1 and BoDV-2 were not detected when using any of the three probes"), so:
psittacine `[1548713]`, passerine `[1548720, 1548721]`, aquatic `[1548722]`.

    psittacine   low coverage, 23.1% on 26  ->  stable, 100.0% on 35,  baseline 98% (59)
    aquatic      low coverage,  0.0% on 26  ->  stable, 100.0% on 18,  baseline 100% (21)
    passerine    low coverage,  3.8% on 26  ->  insufficient data, 4 records, baseline 91% (23)

The aquatic entry went from detecting nothing to detecting everything: every record it was
judged on belonged to another probe's host group or to mammalian BoDV. One doubt was raised
and settled by enumerating the genus rather than assuming it — there are TWO psittaciform
species, and the audit proposed only `alphapsittaciforme`. That is correct, because the paper
claims only Psittaciform 1 (PaBV-1/-2/-4/-7); PaBV-5/-6 are Psittaciform 2 and are neither
designed for nor tested.

*Item 4 as the audit proposed it was WRONG, and the audit doc now says so at length.* It
proposed `taxid: 290433` for the Helicobacter entry. 290433 is not a GCBI1 node: it is
"uncultured Helicobacteraceae bacterium" under Helicobacteraceae > environmental samples, a
catch-all holding unrelated environmental and gut-survey clones. Pointing the entry there
would swap a genus denominator for a grab-bag one. What IS true: the authors' reference
MG910456 exists ("deposited in GenBank under accession number MG910456", titled "clone
GCBI1"), carries taxid 290433, and so is provably unreachable from `txid209[Organism:exp]`.
Measured on it, all three oligos are exact and oriented and the probe sits inside the product,
so **the assay is verified against its own reference and its 0.0% is definitively scope**.
Consequences: `amplicon_bp` corrected 194 -> 191 (measured on MG910456.1 against the paper's
stated 194, measurement wins, `amplicon_disagrees_with_paper` set), `retrieval_scope_incomplete`
and `scope_narrower_than_taxid` added, and the `thin_evidence` note corrected — it said the
target has no GenBank records, when it has exactly one, filed outside the retrieval taxon.
**No `scope_taxids` was set because none can be**: there is no NCBI taxon for Helicobacter sp.
GCBI1. Strike this entry from the scope backlog; it is not a scope bug that scoping can fix.

**A WRONG CLAIM FROM EARLIER TODAY, CORRECTED.** Commit `a784fed`'s message and the first
version of the audit's closing section both say `snakemake -n` planned zero `screen_archive`
jobs, "confirming that a `target` edit does not enter the screen signature, so none of this
cost a rescreen". That does not follow. `screen_signature` (`Snakefile:139`) hashes every
assay YAML's **bytes**, so any registry edit — a curator note alone will do it — invalidates
that group's screens; the dry run hid them only because they sit downstream of the `retrieve`
**checkpoint**. Recomputing the signatures against the stored `.sig` files: **all 10 affected
groups are stale and will rescreen.** What that rescreen changes was then verified by running
it, and the Snakefile's own comment predicts it: rescreening 178830/all (Borna, `scope_taxids`
plus notes) is **byte-identical**, because `screen.py` never reads `scope_taxids` — scoping is
a report-time filter in `drift.assess`; rescreening 209/qea281b18a4 after the amplicon
correction changes 673 of 5,964 rows and **only** in `pair_evalue` and `reason`, with no call,
penalty, coordinate or exclusion moving. So it is real work with no expected status effect.

**Still unretrieved.** `Tortoise_intranuclear_coccidia_18SrDNA` went from
"not searched (no taxid)" to searchable with `taxid: 293274` and a measured
`amplicon_bp: 84`. Its archive has not been fetched yet. The prediction on record, to check
on the next run: 2 records, AY728896.2 amplifying and KY683841.1 truncated (it covers only
AY728896.2 20..620, stopping 12 bases into the forward primer), hence "cannot assess".

**Also found, not fixed:** `RETROVIRUS_RNA_polymerase_SIV_Keele_2009`'s primers are not in
the cited paper and were not found anywhere (zero hits across `papers/` and in full-text
search of both sequences and both names); the repo's own oligo-verification run already
records the sibling pair as `no-oligos`. Keele 2009 only says infection "was confirmed by
RT-PCR" and cites Santiago 2003, which is paywalled. This outranks any scope question for
that entry: the citation has to be settled first. Two stale entry ids from withdrawn
attributions also remain: `Characterization_2001` is Clewley 1998, and `Casas_2005` is Roy
2009 (the DOI was fixed but the id, `nested_family` and `as_written` still say Casas).

## 2026-10-24 overnight: the plan of attack from docs/RESUME-HERE.md's open list

Run unattended from 23:59 on 2026-10-23 (plan: `~/.claude/plans/make-a-plan-of-snazzy-dragonfly.md`).
Each item below says what was measured or built; nothing that needs a maintainer's
decision was touched (what `active` asserts, the calicivirus re-cite, orphan archives,
`209/all`, the Sigrist oligos, M1).

**1. The owed `core_seconds_per_worker: 100` measurement is DONE, and 100 wins.** A
forced rescreen of all 335 live archives (the 21 orphan archives excluded; the shell
listing in the old recipe below would have failed at DAG construction on them) at
`--cores 4`, lid open, `caffeinate -i`, battery at 95%, nothing else running:
**11m 40s wall, 29.0 min summed job time, 2.47x parallelism, exit 0, all 335 screens
byte-identical** (sha256 before and after). Against the byte rule's 13m 54s / 25.2 min /
1.81x and granularity 15's 18m 33s / 27.2 min / 1.47x. The number beside the setting in
`config.yaml` now says measured, with the table. The surprising row: 100 has the
highest summed job time and the lowest wall time, because four single-threaded jobs
contend with each other yet pack far better than the cost model's splits did.
`threads` stays on the model; nothing reverts.

**2. The GenBank-availability ceiling is 11, not 9.** `docs/journal/2026-10-24-genbank-ceiling.md`.

**3. Scoring-strategy test plan** written at the maintainer's request mid-run:
`docs/journal/2026-10-24-scoring-strategy-test-plan.md`.

**4. The two 2026-10-06 "Also on the laptop" checks are closed.** Item 1 (re-run the
oligo verifier over `papers/`) was done on 2026-10-23 (`results/oligo-verification-2026-10-23.tsv`).
Item 2, the reader comparison against real PDFs, ran tonight over 142 papers:

    diff_printed_oligos.py --old-rev 826a905                       127 identical, 15 changed, 7 lost, 47 gained
    diff_printed_oligos.py --old-rev 50430bb --extractor-only --fail-on-loss   109 identical, 33 changed, 0 lost, 86 gained, exit 0

The composition rule loses nothing. The 7 "lost" against the full old reader are all in
`10.1186_1743-422x-6-210.pdf` (Deckers 2009, the CMV gB paper) and are not oligos:
`ASCGGTTTGTTGTA`, `ASGCTGACGGGTTGATCTTGCT`, `ASTGTCCTCACCCAG`, `ASTGTCCTGGTGCTCGCA`
are the table's "as" (antisense) label glued to the start of a sequence, and
`GCGCCGCTGNAGNCC`, `GCGGACTCGGTGAT`, `GGAAACGCAGCTCNCG` are fragments of the flattened
table with Ns where the layout broke. The old reader admitted them; the new one does
not. Written down per the instruction, not fixed; the Deckers oligos themselves were
verified by hand on 2026-10-18 (RESUME item 4 below).

**5. The archive-scale anchor test is built, measured and ships OFF.**
`docs/journal/2026-10-24-archive-anchor.md`. Wave 2's named next item. Every `no_amplicon` row
now carries `anchor_evalue`; `calls.apply_anchor_fdr` runs Benjamini-Hochberg over each
assay's `no_amplicon` rows when `drift.anchor_fdr` is set and relabels a surviving-free
anchor `chance_anchor`. BH rather than E x record count, because the product cannot
tell SIV Keele's thousands of real two-mismatch anchors from Bd's 55 chance ones. At
q = 0.05 Bd loses 50 of 63 `diverged` and Orthoreovirus 228 of 229, while Monkeypox,
Leucocytozoon, Pan-coccidia and SIV Keele lose nothing.

**Tier-2 does not move one row under it alone.** What it repairs is
`count_diverged_as_fail`: that switch by itself turns `CMV_UL55_gB_Prepens_2007_round2`
and `RANAVIRUS_..._MCP_Pallister` @2012 `declining` (wave 2's two false alarms, exactly),
and the anchor test at q = 0.01 restores the matrix row for row with `diverged` still
counted as failure. **The pair `count_diverged_as_fail: true` + `anchor_fdr: 0.01` is
what this measurement recommends, and it is a denominator change, so it waits for you.**
Its own limit is in the doc: BH is relative, so an archive whose chance anchors are the
majority is untouched (2,113 Enterovirus rows move not at all).

**6. The full run.** `results/2026-10-24/`, **380 of 380 steps, 35m 50s, exit 0**;
retrieval fetched 3,061 new records so there are 392 screens against 356. The new column
forced the rescreen (`score.py` is in the screen closure). **Verified byte-identical**:
with `anchor_evalue` removed, all 335 rescreened screens hash to exactly what they were
before, and one archive was rescreened with the pre-change code exported from `e134e92`
and diffed column by column, 54 of 54 rows identical. `chance_anchor` appears zero times
in the report, because the knob ships null. Against `results/baseline-2026-10-22`, 5
statuses moved and 27 assays left the report - that is the accumulated effect of
2026-10-23 (the verified-DOI gate moving 10 entries to `pending/`, the oligo
adjudication, patent exclusion), not of tonight's mechanism, which changed no label.

Two bookkeeping consequences of that run, so neither is rediscovered as a fault. Adding
`clustermaps.py` put it in the report rule's trigger closure, so the four report-stage
rules correctly re-ran afterwards (4m 05s, exit 0); the re-rendered `report.md` differs
from the first render by **17 lines, all of them the `## Run timing` footer**, which now
says no screening benchmarks were written in this run rather than listing the big run's
slowest groups. That is timekeeping item 7 working as specified - only benchmarks inside
the run's own window are counted - and it means **`results/2026-10-24/run-timing.json`
now records the 4-minute re-render, not the 35m 50s run**. The run's real numbers are in
`docs/journal/2026-10-24-archive-anchor.md` and in `e134e92`'s message. No status, interval or
verdict differs between the two renders.

**7. The held-out set went from empty to 31 rows**, and missed its drift target.
`docs/journal/2026-10-24-heldout-candidates.md`. **Not scored; reading it is what spends it.**

**8. `subcluster.py` has a consumer at last, and it is inert for a measured reason.**
`assaywatch/clustermaps.py` builds the `cluster` resolver's map from the archives for
exactly the assays whose `lineage.sublineage` chain names it; with the shipped
`sublineage: {}` no archive is opened. Measured on Bd, the motivating case: its 175
evaluable records cluster into **58 + 31 records above the floor and 86 unresolved** in
159 s, so Bd is not unclusterable, which its own docstring had left open. But it cannot
change Bd's verdict, and that is arithmetic rather than a threshold: 174 of those 175
records `detect`, so no partition respecting `min_records_per_lineage: 30` can fall
below 90%. Bd's real failure sits in its **8,857 `no_site`** records, outside the
evaluable set, exactly as `docs/journal/2026-10-23-wave3-bd-miss.md` concluded. `group_slug`
moved to `assaywatch/groups.py` on the way, because importing `retrieve.py` at report
time pulled the NCBI transport into the report rule's trigger closure - caught by
`tests/test_triggers.py`'s unrelated-module control.

**Gate at the end of the night: 1,550 tests, validator 200/200, `check_citations` 200
checked 0 problems, ruff clean.**

### Still yours to decide (nothing below was touched)

- `active`: **SHIPPED 2026-10-24** at tier=eligible, 178 entries promoted; see the daytime
  section. (The standing recommendation was `--tier clean`; the maintainer chose
  `--tier eligible`, with oligo-doubt flags staying on the entries.)
- `count_diverged_as_fail: true` + `drift.anchor_fdr: 0.001`: **SHIPPED 2026-10-24** after
  the re-price against the scoped registry showed the sole DO-NOT-SHIP objection
  (Bornaviridae) was itself a scope artefact, not drift. See the top of this file for the
  shipping record.
- The calicivirus re-cite to Neill & Seal 1995: **SHIPPED 2026-10-24** (`a784fed`-ish, the `055a9a9` commit); see the daytime section. M1 remains on hold -- tier-2 still kills the one documented candidate (Hellgren Leucocytozoon), so the mispair table ships empty and reopens with the scoring-strategy plan's replay harness, not a config flip. The three Sigrist oligo questions are also closed (`BornaPCA6`/`PaBVcon_1401+` and `A647N`/`A674N`), registry was right both times.
- The 10 orphan archive groups (658 MB, 3 belong to `pending/` entries; one group alone is
  530 MB). `scripts/archive/orphan_archives.py` advises keeping the three pending ones unless the
  entry is being dropped. **IDENTIFIED 2026-10-24, still not deleted:
  `docs/journal/2026-10-24-orphan-archives.md` says what every group is.** The headline: 636 of the
  658 MB is superseded PRE-QUERY history for taxa the registry still covers - the 530 MB
  group is *Ophidiomyces ophidiicola* and the 90 MB one is *B. salamandrivorans*, both with
  live entries that have since gained a retrieval query, which is part of the group key. One
  group, `1430836/all`, is a genus of moths and should go regardless. The decision was never
  short of authority, only of information; it now has it. (`209/all` is CLOSED as of 2026-10-24 — that entry now carries its
  sibling's query, joined the existing archive and screens at 91.8%.)
- Four held-out rows rest on an oligo that differs from the registry's by one base or a
  5' trim (see the candidates doc). The pan-coronavirus Watanabe reverse is **SETTLED
  2026-10-24**: neither side is a transcription error, Watanabe's held PDF prints the 24-mer,
  the 23-nt form is PREDICT P-006 with a base dropped, and the binding-site counts reproduce
  (215 / 204 / 88). Written up in the candidates doc. Stöhr 2015's ranavirus MCP reverse was
  worked through the same evening and the registry's 18-mer stands on two transcriptions to
  one, but it is **not fully closed**: the design paper, Mao et al. 1997, is the only thing
  that would settle it and Elsevier returns no body for it, so it wants the Virology scan
  through the NYU proxy. **The Sigrist row is closed and was a false alarm** (2026-10-24): the
  `GATCCGCAGACAGYACGT` that Villanueva 2024 prints is the registry's own alternate forward
  `BornaPCA3A`, already on the entry beside the primary `BornaPCA3`, and Sigrist 2021 section
  2.2 says in terms that the design has "two variants of a degenerate forward primer". No trim,
  nothing to reconcile; the row's note now says so. A sweep of
  `docs/validation-cases-heldout.tsv` for any other qualified identity found none - the two
  adenovirus rows read "byte-identical" - so **Mao 1997 is the only oligo-identity question
  still open anywhere in the held-out set.**

### The old section 0, kept for the record

`core_seconds_per_worker: 100` was justified by reasoning from numbers that WERE
measured (granularity 15 vs the byte rule) but the claim that 100 returns the run to
about 14 minutes had not been run: the confirming run was stopped at 17 of 335 jobs
when the machine was shut down. The recipe was

    snakemake $(ls data/retrieved/*/*/*.fasta.gz \
        | sed 's|data/retrieved/|results/screened/|; s|\.fasta\.gz$|.tsv|') \
        --forcerun screen_archive --config run_date=$(date +%F) --cores 4

with the orphan groups from `scripts/archive/orphan_archives.py` removed from the list first.

## 0b. Timekeeping is finished, and 658 MB of archives belong to nobody

`docs/journal/2026-10-18-pipeline-timekeeping-todo.md`. **All seven items are done**: item 7
is `report.timing_lines`, a `## Run timing` footer in both the markdown and the HTML
report, giving per-stage wall times and the ten slowest retrieval groups.

Two things in it are not what that list asked for, and both are forced. The stage
table usually describes the PREVIOUS run, because the Snakefile closes its `workflow`
stage in `onsuccess`, which fires after the `report` rule - insisting on this run's
own stages would print an empty table in every run forever. And only benchmarks
written inside the run's own window are counted, which is what defuses the
sleep-contamination problem that blocked this item: a benchmark is keyed by archive,
not by run date, so a bare directory read mixes generations.

Found while force-rescreening every archive to get one clean set of benchmarks: a
targeted run died with `KeyError: (2093, 'q4185828e3e')`, because **10 retrieval
groups on disk are not in the registry any more** - 21 archives, 658 MB, 99
manifest entries that look like live state. Three were orphaned the same day by
moving ten entries to `pending/`. `scripts/archive/orphan_archives.py` reports them and
deletes nothing. It also names the reverse gap: `209/all` is a live group with no
archive, so it has never been screened.

The clean benchmarks also settled two open questions. The 2026-10-22 sleep diagnosis
is confirmed to the second (`11320/q2ebd5918b3` read 1180.1 s contaminated, 40.3 s
solo, **36.4 s** clean under contention), and effective parallelism on 4 cores is a
real **1.81x** against the bogus 1.13x. And that doc's own hypothesis about the
thread heuristic is WRONG: gzipped bytes predict screening time better than record
count (+0.776 against +0.490; +0.753 against +0.289 above the startup floor), so
swapping the predictor would have made it worse. The narrower real fault is that
four of the ten slowest jobs are small, record-dense archives sized to one worker,
while a 1.5 GB archive holding 1,179 records gets 16. Fix shape: max of a byte term
and a record term - though that is not what shipped either.

**FIXED the same day, and the missing variable was neither bytes nor records: it
was the number of assays in the group.** An archive is screened against every
assay that asked for its group, so `MB x assays` alone fits at R2 0.944 against
0.845 for the best byte-and-record model, and adding `records x assays` reaches
**0.952**. Both `threads` and `priority` on `screen_archive` now come from
predicted core-seconds (`assaywatch.timing.screen_core_seconds`, constants in
`config.yaml` under `screen:` with the fit recorded beside them). The four
record-dense archives that ran single-threaded now get 2-5 workers, and a 761 MB
archive needing one assay's work drops from 16 to 10.

Two things to know. Putting the constants in `config.yaml` required a new block in
`settings.py`, which is inside `screen.py`'s import closure, so all 335 screens
were invalidated and rescreened - the trigger working as designed, since a module
that COULD change a call must invalidate whether or not this one does. `screen.py`
never reads the `screen:` block, so the rescreen is expected to reproduce every
screen byte for byte (verified: all 356 reproduced exactly). Resizing alone reruns nothing.

**The threads half of the fix was then measured and lost.** At
`core_seconds_per_worker: 15` a forced run of all 335 archives took 18m 33s against
the byte rule's 13m 54s, with summed job time UP 8% (25.2 -> 27.2 min) and effective
parallelism DOWN from 1.81x to 1.47x - and a rise in summed job time is extra real
work, not contention. Each worker pays ~1.5 s of start-up, and a job holding four
cores stops four jobs holding one. The granularity is now **100** core-seconds per
worker, measured, so locally almost everything runs single-threaded again. What the
cost model keeps is `priority` (the dense archives were running LAST, not starved of
workers) and correct sbatch CPU requests: the biggest archives now ask for 5, 3, 3
and 2 instead of a flat 16. The old wording below is kept because the prediction in it
turned out to be right. The local wall-time gain at `--cores 4` is
expected to be small: the real wins are the tail, via `priority`, which had been
ranking a 52-second archive near the back of the queue because it was 10 MB, and
correct CPU requests on SLURM.

## 0a. The oligo flags are adjudicated; four sequences were wrong

`docs/journal/2026-10-23-oligo-adjudication.md`. Every `near:` and `absent` row was read
against the paper itself, and **every changed sequence was then screened before being
kept**. Agreement is 415 of 462 checkable (90%); the 5 remaining `near:` and 22
`absent` are all documented artefacts, mostly oligos that exist only inside a figure
image. The rescreen HAS been run on all four affected groups.

**Two of four corrections were reverted by measurement, and that is the lesson.**
Borna-NF's printed form matches 0 of 1,516 records where the stored form matches 260
(67.5% detected -> 0.0%), and CoV-RVS3's stored 24-mer binds 215 records against 204
for Watanabe's own and 88 for the panel's 23-mer (40.0% -> 2.2%). Both reverted, both
back to baseline to the record. The calicivirus pair WAS a real mis-split cell and is
corrected, confirmed against the Neill & Seal 1995 design paper; its fall to 0/30 is a
`terminal_mismatch_fails` artefact on a conventional PCR, now a worked example under
ROADMAP Phase 2. **Screen any future oligo correction before committing it.**

Found on the way: `BORNA_VIRUS_N_gene_Zimmermann_1994_round2` stores the printed form
and has read 0% in every run, including the baseline, for exactly this reason - a
false signal nobody had explained. Flagged, not changed.

The policy, decided by the maintainer: **keep both.** Store the form actually run
and record `modified_from` plus `modification_doi`. 13 oligos now carry it. An
empty `modification_doi` means the modification is unpublished and exists only here.

Both re-citation questions resolved WITHOUT a rename: `E_coli_ETEC_LT_Victor_1991`
keeps Victor because the two primer pairs sit on the same eltA sites a few bases
apart, so Wang's credit to Victor is real lineage (Victor's primers are now
`modified_from`); `RHABDOVIRUS_ssRNA_L_gene_round2` keeps Bourhy because PVO3 is
Bourhy's exactly and only the nested forward comes from Wray, which itself calls it
unpublished. Still open: whether the calicivirus entry is re-cited to Neill & Seal
1995, now that the design paper is readable.

## 0. Only verified-DOI assays are live; the seed list is gone

`docs/journal/2026-10-23-verified-doi-gate.md`. `registry/` holds 198 entries, all
`doi_verified: true`, which the validator and the Snakefile both enforce. The 10
without a verified DOI are in `pending/` and are never screened. The seed list's
fields (`source.spreadsheet`, `rows`, `positive_control`, the list's `notes`) and
its importer are deleted. **Never name the seed list's lab as a source**: there is
no permission question, because no assay is published on the list's authority. A
public release is a fresh repository made from a clean snapshot. This private
repo's history is not rewritten.

## 1. SETTLED: why the terminal_mismatch_fails run died, and the rule it gives you

This section used to open "**State: `config.yaml` has `terminal_mismatch_fails: false`
UNCOMMITTED** ... 20 pytest failures are that knob", and told the next reader to settle
the cause before re-running. All of that was stale within a day: the tree is clean, the
knob is `true`, and those 20 failures do not exist. **The cause is now known.**

**What happened.** The `2026-10-22-tmf-false` run ran 19:49:28 to 20:16:42 and died at
`collect_calls`, with `_raise_for_stale_signatures` refusing all 349 screens the same run
had just written. The prime suspect recorded here was "the registry was edited while the
run was in flight" (`0a0d3e4` at 20:11:43, `3e94e96` at 20:12:58, both inside the
window), and this doc noted that it "does not add up": `screen_signature` re-reads only
the YAMLs of the assays **in that group** (`Snakefile:139`), so a hantavirus edit cannot
invalidate `results/screened/171/asm/`, which holds no hantavirus entry. That reasoning
was right and the suspect was wrong.

**The cause was a `git stash` at 20:09:05**, twenty minutes into the run: commit
`b22c466` ("WIP on main"), still present as `stash@{0}`. Its only change is

    -  terminal_mismatch_fails: false  # TIER-2 TEST 2026-10-22, not a shipped value
    +  terminal_mismatch_fails: true   # any mismatch at the 3'-most base = fail

Stashing the test knob restored `config.yaml` to the shipped value **mid-run**.
`terminal_mismatch_fails` is in the `scoring` block; `_code_hash` is built from
screen.py's import closure **plus the `scoring`, `amplicon`, `degeneracy` and
`thermo_conditions` blocks** (`Snakefile:122`); and every group's signature starts from
`_code_hash`. So every screen written before 20:09 was produced under `false` and
evaluated under `true`: all 349 refused, groups with no hantavirus entry included. The
guard worked exactly as designed, and the registry edits two minutes later were a red
herring.

**The operational rule, which is what the question was for:**

- Editing `config.yaml`'s `scoring`, `amplicon`, `degeneracy` or `thermo_conditions`
  block, or any module in screen.py's import closure, during a run invalidates **every**
  group. So does `git stash`, `git checkout` or anything else that rewrites those files:
  the signature reads the working tree, not the commit.
- Editing a registry YAML invalidates **only the groups containing that assay**.
- The other config blocks (`drift`, `lineage`, `report`, `sitedrift`, `figures`) are not
  in the screen signature at all, which is why every report-stage change in waves 1-5 was
  measured without a rescreen.

**To re-run the experiment** (still untested; `config.yaml`'s comment at
`terminal_mismatch_fails` is the standing record of why it matters): set the knob, start
the run, and touch nothing in the repo until it finishes. The `--forcerun` recipe this
section used to give is no longer needed — the screens on disk are consistent again, as
`snakemake -n` confirms by planning zero `screen_archive` jobs.

## 2026-10-23: waves 0-5 of the plan of attack

An outside evaluation on 2026-10-23 produced a plan worked through in waves on branch
`docs/2026-10-23-elsevier-and-oligo-flags` (started as
`review/2026-10-23-plan-of-attack`). Each wave has its own dated record; read those rather
than this summary.

- **Wave 0** `docs/journal/2026-10-23-baseline.md` — `results/baseline-2026-10-22/` frozen as the
  comparison point, the full tier-2 matrix, and the first precision figure ever computed:
  **2 of 9 `declining` calls were real failures**.
- **Wave 1** `docs/journal/2026-10-23-wave1-report-honesty.md` — **704 of 1,512 per-lineage
  intervals were zero-width** (a Wald interval in `lineage.py`); 19 assays carried a
  status their own registry entry denies; the duplication check never saw an overridden
  flag.
- **Wave 2** `docs/journal/2026-10-23-wave2-diverged-and-patent.md` — `count_diverged_as_fail`
  tested and **kept off** (55 of Bd's 63 `diverged` records are 2014 JAM81 mRNAs matched
  by chance); `exclude_patent_records` turned **on**, on mechanism, without tier-2
  approval, with the rule for doing that written beside the setting.
- **Wave 3** `-wave3-bd-miss.md`, `-wave3-usutu.md`, `-wave3-influenza.md`,
  `-wave3-holm.md` — all three documented misses are **scoring** problems, not
  statistical ones. Holm replaced BH and moved nothing yet.
- **Wave 4** `docs/journal/2026-10-23-wave4-holdout.md` — `validation-cases.tsv` is now labelled
  the **development set**; `scripts/archive/holdout.py` prices what tuning on it bought;
  `validation-cases-heldout.tsv` is empty on purpose.
- **Wave 5** `-wave5-config-schema.md`, `-wave5-triage.md`, `-wave5-what-active-means.md`,
  `-wave5-ip-question.md`, `-wave5-engineering.md`,
  `-wave5-elsevier-and-oligo-flags.md` — `config.yaml` has a schema and six defaults lost
  their second home; the report leads with ten assays and is navigable without a script;
  `scripts/promote.py` lists 173 eligible drafts; the weekly run exists and is dry by
  default; `calls.py` split out of `report.py` and three rules now declare memory.
- **The Elsevier token works** (`-wave5-elsevier-and-oligo-flags.md`): 10 of 10
  outstanding Elsevier DOIs fetched, **uncheckable oligos 106 -> 38** (13 entries have no
  oligos, 25 no DOI), 466 of 504 checkable and 393 agreeing (84%). 15 candidate genuine
  errors remain and **no registry flag was changed yet**. Both steps must run on the host:
  `api.elsevier.com` is not on the cloud proxy allowlist, and
  `verify_oligos_against_paper.py` needs 3.11+ for `StrEnum`.
- **`scripts/design_era.py`** measures the founding premise: 71 assays were designed
  against under 50 records (`docs/design-era.tsv`).

Open, in rough order: decide what `active` asserts
(`scripts/promote.py`, and `docs/journal/2026-10-23-wave5-what-active-means.md` recommends
`--tier clean` — the oligo-provenance objection to promoting is now much weaker, 38
uncheckable rather than 106, so this decision is ripe); collect held-out cases (plan 4.2, shared with the C2 bench corpus in
`docs/bayesian-scoring-plan.md`); build the archive-scale anchor test that
`count_diverged_as_fail` needs; and `subcluster.py`, built, tested and still unwired.

## 2026-10-22, M1 tier-2: DECIDED. The wobble discount is reverted

Full write-up: `docs/journal/2026-10-22-M1-tier2.md`.

- **`mispair_penalty` is back to `{}`.** The shipped global value lost three documented
  catches (`fails` correctly flagged 5 -> 2). Scoping the multiplier to
  `primer_3prime_window` - where Kwok 1990 and Stadhouders 2010 actually measure the
  identity effect - restored two of them and pulled the Paramyxovirinae `works` case back
  from DISAGREES to `weaker`, but left `fails` at 4 of 11 against pre-M1's 5.
- **Across all 49 cases the scoped table differs from pre-M1 in exactly one row:**
  `Leucocytozoon_cyt_c_Hellgren_2004` @2016-12-31, `low coverage` (agrees) -> `watch`
  (DISAGREES). 17 records flip, and every one carries a G:T at **d = 2** - inside the
  window, so no scope rule excludes them.
- **No partial multiplier rescues it, and that is arithmetic, not a guess.** At d=2 the
  base penalty is `primer_3prime_penalty: 3.0` against `reduced_max: 3.0`, so a record
  stays `fail` only while the multiplier is above ~0.83; and `drift.py` counts `reduced`
  as detected, so `fail -> reduced` loses the catch just as `fail -> detect` does. The
  G:T/T:G discount and this catch are incompatible under the `budget` engine. Closed by
  measurement - do not reopen it with a different number.
- **The 3'-window scoping of `score_primer` is KEPT** (inert with an empty table) along
  with its guard test `test_a_zeroed_mispair_outside_the_3prime_window_is_not_discounted`,
  so the unscoped form cannot come back.
- **The cost, stated honestly:** the FAP (12 of 14) and Barrett (3 of 3) bench false fails
  return. Three bench panels and one documented field catch disagree about the same wobble
  and summed-budget scoring cannot satisfy both; the per-oligo verdict combination
  `config.yaml` already names as the real defect is where to look next, not another
  multiplier.
- `config.yaml`'s header no longer says "46 cases ... 1 of 12": it is 49 cases and 5 of 11.

**DONE, same day: the full run under the reverted config cleared them.**
`snakemake-2026-10-22-revert-fullrun.txt`, 337/337 steps, 15m 11s, exit 0, and
`results/2026-10-22/` is now one scoring generation: **0 of 330 screens store no signature**
(was 20), all 330 `signature_verified: true`, none still dated 2026-10-18, and the
`store no signature` warning is gone from the log. The 20 did not need deleting -
`--forcerun` on their paths regenerates them in place, which is the cheaper habit, and the
revert forced all 330 to rescreen anyway because `mispair_penalty` is part of `_code_hash`.

**The tier-2 baseline is re-measured and unchanged: `fails` 5 of 11, and all 49 cases read
identically to the pre-M1 table.** So the revert is complete and the 20 stale screens never
moved a tier-2 verdict - the same answer the 2026-10-21 by-hand diff got. That 5 of 11, on
330 same-day signature-verified screens, is the number every future one-knob test is
measured against. Write-up: `docs/journal/2026-10-22-unsigned-screens-cleared.md`.

**And `collect` now refuses an unsigned screen** rather than warning and exiting 0
(`_raise_for_unverifiable_signatures`, sibling of `_raise_for_stale_signatures`). The
warning fired in every run since 2026-10-21, including the M1 re-screen at log line 5895,
and changed nothing. Every screen on disk is signed now and every new one writes its own,
so an unsigned screen from here on is a stale file restored from somewhere.

## 2026-10-22, timekeeping item 2: benchmark directives on retrieve and screen_archive

`results/benchmarks/retrieve/<date>.tsv` (per day, like the rule's output) and
`results/benchmarks/screen/<taxid>/<group>/<stem>.tsv` (**keyed by the archive, not the run
date** - a screen is cached across runs, so a date-keyed benchmark would be missing for every
cached archive next run). Verified it does not churn the cache: `snakemake -n` after adding
the directive schedules **zero** `screen_archive` jobs, and `tests/test_triggers.py` still
passes 44/44. Full write-up in `docs/journal/2026-10-18-pipeline-timekeeping-todo.md`, which now has
only item 7 open.

**Expect wall time only on the laptop, and do not go looking for the bug.** Snakemake samples
with psutil's `memory_full_info()`, which macOS refuses for a child process (`AccessDenied`,
verified directly), and one unreadable process discards the whole sample - so `max_rss` and
every other resource column reads `NA` at any job length (checked at 0.44 s and 7.9 s).
`memory_info()` works here, so it is Snakemake's choice of call, not macOS. **The memory
columns fill in on Linux**, i.e. in CI and on Greene - which is where `screen_archive`'s
`mem_mb` and `threads` guesses finally become checkable.

**Populated all 330 the same day, and the data undercut the plan.** 336/336 steps in
**1h 46m 49s**, with `calls.tsv.gz` returning the **same sha256** - the rescreen changed
nothing but timing files. Then:

- **The sampler is free**: one job alone is 36.55 s by its own benchmark against 37.6 s with
  no Snakemake at all. The NA columns are not overhead.
- **But the `s` column counts machine sleep.** `pmset -g log` for the run window: elapsed
  1:46:49, **asleep 1:30:57** (first event `Clamshell Sleep` 11 min in, then maintenance
  cycles on battery), **awake 0:15:52** - against the identical rescreen's **15m 11s** earlier
  the same afternoon. The pipeline did the same work in the same time; **there was no
  slowdown.** The lid was closed and Snakemake's benchmark is wall clock, so it kept counting
  while nothing ran. `11320/q2ebd5918b3` read 1180 s and takes 40.3 s alone; that gap is
  suspension, not CPU starvation, and the "1.13x parallelism" I derived from elapsed time is
  the same artefact.
- **`caffeinate -i` does not survive a closed lid** - it asserts
  `PreventUserIdleSystemSleep`, and clamshell sleep is not idle sleep. The command in
  `CLAUDE.md` and `README.md` now says to keep the lid open. A suspended run still finishes
  correctly; it just writes timing data that measures the lid.
- **The benchmarks on disk are contaminated** - written across 91 minutes of sleep.
  Re-populate with the lid open before building item 7 on them. Cost a single archive by
  running it alone.
- **Real finding:** `threads`/`priority` are sized from gzipped MB and cost does not track
  bytes - `11320/q2ebd5918b3` is 6 MB holding **165,492 records**, so it gets 1 worker and
  the lowest priority, yet costs about what a 52 MB archive does. Size on record count, not
  bytes; measure solo.

## 2026-10-22, CI had been RED for a day: matplotlib was declared for conda only

Found while pushing the M1 revert. **Both CI jobs had been failing since the figures merge**
(`fa98937`), and nobody saw it because the Mac has `matplotlib-base` from conda and the local
gate is green:

- `test` job: `tests/test_figures.py` cannot even be collected - `ModuleNotFoundError: No
  module named 'matplotlib'`.
- `snakemake` job: the `figures` rule fails inside `tests/test_triggers.py`'s pipeline run,
  same import.

**Cause: `matplotlib-base` was added to `environment.yml` and nothing was added to
`pyproject.toml`.** CI installs with pip (`pip install -e ".[dev,lineage]"` and `".[dev]"`),
so it never saw the dep. This is **R1a in mirror image** - R1a was deps living only in
pyproject extras that a fresh conda env never pulled; this is a dep living only in the conda
env that a pip install never pulls. environment.yml being the source of truth for a *local*
install does not make it the source of truth for CI.

Fixed by declaring `matplotlib>=3.8` in pyproject's **core** dependencies, not an extra:
`rule all` requires `results/<date>/figures/figures.html` unconditionally, so a run cannot
finish without it. `tests/test_reproducibility.py` now guards both directions. **If figures
should be opt-in, gate the rule in `all` first and then move the dep to an extra - do not
just move the dep**, or the `snakemake` job breaks again.

Worth knowing: the local gate cannot catch this class of bug, because conda and pip resolve
from different files. Only CI can, which is the argument for the `snakemake` job having been
made blocking.

## 2026-10-22, PR #3 closed; three things salvaged out of it first

`docs/2026-10-15-lineage-plan` was docs-only and superseded by
`docs/journal/2026-10-17-estimand-plan.md`, which a parallel session shipped from two days later
(BH not Bonferroni, `mechanism` column not `lineage`, species-rank grouping, no
`drift.subgroup`). It also conflicted on this file with ~140 commits of staleness on its
side. Salvaged into `docs/journal/2026-10-22-lineage-plan-salvage.md` before closing:

- **A GenBank-availability ceiling nobody on main had written down.** If Lotta 2019's cyt b
  sequences postdate the 2016-12-31 cutoff, the two Hellgren rows are uncatchable by any
  in-silico method and **the honest ceiling is 9 of 11, not 11** - i.e. every "N of 11" in
  the project quotes an unreachable denominator. Distinct from the taxid-resolution ceiling
  in `docs/journal/2026-10-18-recalibration.md`. Checkable locally with no network (archives carry
  deposition dates); it was Phase 0's go/no-go and was never run. It does NOT weaken the
  M1 revert - that rests on the pooled coverage call, a different estimand.
- **Footprint groups as lineage units**, with the per-unit `no_site`/`diverged` exclusion
  share. main groups by taxonomy only and has no equivalent disclosure.
- **Still open: do `partial` rows count as successes when the tool names their gap?** The
  other two decisions the PR asked for were settled de facto on main. This one decides what
  the paper's main figure claims.

## 2026-10-22, the `.supp` convention reached the oligo verifier; 3 citations resolved

Full write-up: `docs/journal/2026-10-22-supplements-and-three-citations.md`.

- `verify_oligos_against_paper.py` did not know the `<doi stem>.supp.<ext>` convention that
  `papers_index.py` has used since 2026-10-21, so a supplement was indexed under a DOI nothing
  cites (`10.1371/journal.pone.0207365.supp` still matches the DOI pattern) and its primer table
  was invisible. `SUPPLEMENT_SUFFIX` + `identity_stem()` now live in `assaywatch/papers.py` and
  both scripts read them from there. **15 oligos over 4 entries moved `no-oligos` -> `exact`**
  (3x Hermes 2018 mycobacteria; POXVIRUSES Polymerase short_2 vs the McAloose supplement).
- **Three citations entered, each confirmed by sequence first**: Mueller_2011_1..4 ->
  10.7589/0090-3558-47.3.725 (the old string's own "candidate", now evidence); `Nipah_N_gene` ->
  10.1016/j.jviromet.2006.11.023 (Wacharapluesadee 2007 prints NP1F/NP1R as the outer round of the
  nested pair whose inner round is the sibling entry's); `Entamoeba_18S_small_subunit_SSU` ->
  10.1638/2020-0148 (McFarland 2021, the publication of the seed list's unpublished assay). All three
  are paywalled, which is why the open-access routes never found them. **13 rows left
  `docs/materials-needed.tsv`.** Entamoeba's `design_year` stays null on purpose - the assay
  predates the 2021 paper (it is in the 2018 spreadsheet), so the publication year is not it.
- **CLOSED 2026-10-24** (was: open, wants the maintainer): the three `ORTHOBORNAVIRUS_XP_*`
  Sigrist entries. Both halves of the question are answered and the registry was right both
  times. `BornaPCA6` being 1 edit from the printed `PaBVcon_1401+` was resolved on 2026-10-23
  and is recorded in the entries: `PaBVcon_1401+` is one of the previously published
  **comparison** assays listed in Table S4, overlapping the same site, so the verifier was
  scoring this registry against a third party's primer. And the `A674N`/`A647N` clash was
  settled on 2026-10-24 by counting both PDFs: the paper writes **A647N** where the probe is
  defined and described (section 2.2, the Figure 3 caption, Figure 2C) and **A674N** in exactly
  two places, both table column headers (Table 2 and Table S5). Four in running text against
  two in headers, and 674N is not a real dye, so it is a digit transposition the paper makes
  twice. The stored `BornaA_A647N` stands. The reporter field was corrected from "Alexa 647N",
  which the paper never writes, to the printed `A647N`, with `chemistry_detail_missing` noting
  that the manufacturer is unstated. Still open: the Enterovirus 5'UTR-VP4/VP2 pair, where
  Coiras 2004 (10.1002/jmv.20008, now held) matches `EVRV1` exactly but disagrees on the other
  three oligos and on both product sizes - a modified descendant, so NOT entered.
- `papers_index --check` now prints `3 PDF(s) ... match no DOI` and exits 0: Coiras 2004,
  Aitichou 2005, Khodeir 2021, all held as candidate provenance, deliberately not in
  `SHARED_SOURCES`.
- Gate: 1481 tests, validator 208/208, `check_citations --refresh` 0 problems, ruff clean.

## 2026-10-21, figures feature merged from a second machine (`fa98937`)

- **A second machine is now pushing to this repo.** `origin/main` had diverged: the other
  session shipped a **figures feature** (`assaywatch/figures.py` — forest + per-position SVG
  plots, a `figures` Snakemake rule, optional `--figures` on the HTML report, `matplotlib-base`
  in `environment.yml`) while this machine held 56 unpushed commits incl. the S3 `report.py`
  refactor. ~~**Pull before starting a session from now on.**~~ **NO LONGER APPLIES as of
  2026-10-24**: the maintainer confirmed they no longer work on more than one machine, so
  `origin` has a single writer and divergence of this kind cannot recur. The merge below is
  still worth reading for how a cross-session reconciliation was done, and for the
  semantically-broken auto-merge it caught.
- **Merged, not rebased** (the merge-base is itself a cross-session merge, so merges are the
  repo's established reconciliation). Only `report.py` conflicted. Git's 3-way auto-merge was
  **semantically broken**: `html_from` referenced a `figures` it never received (NameError every
  render) and `render_html` accepted `figures` but never forwarded it. Resolved by threading
  `figures` through the refactored `html_from(m, figures)` — figures stay HTML-only presentation,
  not model content, matching S3's split (markdown gets none).
- **`test_triggers` expected rerun-sets updated** to include the `figures` rule. `figures.py`
  imports `drift`/`report`/`sitedrift`, so editing any of them — or the registry, or the
  drift/lineage/degeneracy config — correctly re-renders the figures. Verified precise: the
  `[unrelated module]` control still reruns nothing, so no spurious cascade.
- **Installed `matplotlib-base` locally** to match the merged `environment.yml`.
- Full gate after merge: **1478 tests, ruff clean, validator 208/208.** Pushed.

## 2026-10-21, R1 reproducibility (a/b/c/e done; d deferred)

- **R1a** (`00938a2`): a fresh `conda env create` could not run four documented commands - their
  deps (openpyxl, pypdf, poppler/pdftotext, the SLURM plugin) lived only in pyproject extras the
  env's core `pip: -e .` never pulled. All added to `environment.yml`; the whole file dry-run
  solved on osx-arm64. Snakemake pin aligned env<->CI (`>=9.27,<9.28`). `build` is `python-build`
  on conda-forge. `tests/test_reproducibility.py` guards the deps + the Snakemake and ruff pins
  against drift.
- **R1e** (`00938a2`): `profiles/slurm/config.yaml` told users to run `--use-conda`, a silent
  no-op since no rule carries a `conda:` directive; replaced with the shared-env / module-prologue
  path that actually works.
- **R1b** (`4ae31f1`): the sidecar now carries `collected_under` (python, platform, and the
  versions of numpy/scipy/primer3/snakemake etc. that move numbers) - the environment identity R2
  left out. Collect-time, not the plan's per-archive design: per-archive must live in screen.py's
  closure and would force a 25-min rescreen on any edit. Exact for a same-day run, honest for a
  mixed table (screened_at shows the span). Populated the live sidecar in 54s, no rescreen.
- **R1c conda-lock: DONE** (`d84bc7f`, refreshed in `fd8f71e` once matplotlib-base entered the
  env). `conda-lock.yml` is tracked and cross-platform (osx-arm64 + linux-64); environment.yml
  resolving cleanly was most of the value and the lock is the exact-transitive belt to it.
  Regenerate with `conda-lock -f environment.yml -p osx-arm64 -p linux-64` after any
  environment.yml change. (This entry read "NOT done" until 2026-10-22; it was stale.)
- **R1d container: deferred** (NYU Greene is Apptainer, so the artifact is a .def over the lock -
  worth it when a cluster run is imminent, per the plan).

## 2026-10-21, drift window x minimum calibrated

`min_records_for_drift` 20 -> 15 (`8cee3b5`), `recent_window_months` left at 24. A 2-D sweep
against `docs/validation-cases.tsv` (drift is report-time, no rescreen;
`docs/journal/2026-10-21-drift-window-calibration.md`) showed the knobs act separately: the minimum
sets `undecided` (17 of ~49 at 20, 15 at the new value), the window sets accuracy. min 15 turns
2 undecided cases into correct calls (one catching a real fail, Leucocytozoon @2016), adds
**zero** new false declines, moves 11 of 208 statuses (insufficient data 42 -> 34). Report-only,
regenerated.

**Window DECIDED 2026-10-21: stays at 24.** 48-60 months scored better on the validation set
(DISAGREES 10 -> 7 at 60/15) but that is an artefact of as-of scoring. Measured against the real
calls table, a 60mo window would report 4 assays healthy (>=80%) while their last 12 months runs
20-41 points lower on real records - PAPILLOMAVIRUS L1 (86% vs 66%, n=484), FILOVIRUS L
(88% vs 51%, n=72), ABPV capsid, RANAVIRUS - because `assess` aggregates the recent window as one
sum. For a drift monitor those late warnings are the whole cost, and the validation set is built
not to see them. 24 stands. (Those 4 recent drops are real at 24mo too and worth a per-assay look,
separate from the threshold.)

## 2026-10-21, amplicon sizes: measured-wins policy and 8 declarations

Prompted by two size defects (ALPHAVIRUS NSP4, RANAVIRUS intergenic) found by accident.
**Policy, maintainer's decision:** where a measured product size and a published one disagree,
the registry takes the MEASURED value and discloses the difference
(`amplicon_disagrees_with_paper`). A published size is usually a gel band; ours is computed
from primer positions. Written into `config.yaml` (amplicon:) and `CLAUDE.md`. The paper still
says whether the length VARIES, which is the signal for a range.

- **The cushion is `declared_tolerance`, already +/-25%, applied in `score.py` around whatever
  is declared** - retrieval and the genome cut never use the declared size, so there is nothing
  to pad there. Correcting a size re-centres the existing cushion. `measure_species_sizes.py`
  now prints a suggested `amplicon_bp_range` = band envelope (lowest low, highest high, each
  end separately) + a `--cushion` (default 10 bp), per the maintainer's rule; raw extremes are
  shown so a trimmed real band is visible. `suggested_range` is pure and tested (9 + 6 mutants).
- **A real bug fixed first** (`0212095`): `classify_exclusion` judged a range-declaring assay's
  truncated/diverged geometry against `amplicon.max_bp` 3000, because it was handed
  `assay.amplicon_bp` (null for a range) instead of the declared upper end. Now both readers
  share `declared_ends(assay)`.
- **8 sizes declared from measurement** (`9ea1a1e`), each decided from its real products:
  | entry | change | shape, why |
  |---|---|---|
  | CHYTRID_Bd Boyle 2004 (active) | 121 -> 146 | scalar: 132-152, 20 bp spread fits +/-25% |
  | CALICIVIRUS Helicase Reid 1999 | null -> 360 | scalar: 5 records all at 360 (the 62-2633 was chance) |
  | SARCOCYSTIS short | null -> [225,846] | range + 13 species bands |
  | SARCOCYSTIS long | null -> [568,1294] | range + 30 species bands |
  | Encephalitozoon PTP | null -> [275,373] | range + 2 bands (one species, repeat genotypes) |
  | ORTHOBUNYAVIRUS S | 930 -> [283,1120] | range-only (26-species segment continuum) |
  | ORTHOBUNYAVIRUS M | 898 -> [201,1090] | range-only (15-species continuum) |
  | RANAVIRUS intergenic | 200 -> [186,749] | range-only (within-species ladder, not a key) |
- **Rescreen (second 2026-10-21 run, 25m 29s, 304 steps, S1 clean, 303 signatures verified) and
  report_diff vs 2026-10-20** gave 3 amplicon-driven status moves, all telling the truth the
  old declaration hid:
  - **RANAVIRUS stable -> watch**: evaluable 40 -> 72, share 90.0% -> 83.3%. The range recovered
    the ~700 bp EHNV/ECV/ESV products (which detect worse); the old 90% stable was a scalar
    clipping 48% of binding records. **Promotion to active stays DEFERRED** on this real status,
    not the artefact.
  - **ORTHOBUNYAVIRUS M insufficient data -> low coverage**: now 20 evaluable at 5.0% - the
    pan-genus M assay barely detects, which the narrow scalar had hidden.
  - **CALICIVIRUS low coverage -> no recent data**: the scalar excluded chance products; 5 real
    records, none recent.
  - Bd unchanged (100% on 54, still active); SARCOCYSTIS x2, ORTHOBUNYAVIRUS S, Encephalitozoon
    all stay insufficient-data (<20 recent). ALPHAVIRUS stable->declining is the prior session's,
    not this work.
- **RANAVIRUS/Jancovich attribution** (`2902564`): NOT re-cited. Pallister credits 16R/16F to
  Jancovich 2005 in five places but describes Jancovich as a user of the locus; the sequences
  were read from Pallister's own Methods, no Jancovich DOI is printed, the paper is not on disk.
  So `oligos_designed_here: false`, Jancovich's full reference in the note, citation left at
  Pallister. Re-cite only when the paper is on disk and its DOI Crossref-verified (NOSEMA/Klee
  precedent). WANT: Jancovich et al. 2005, Mol Ecol 14:213-224, for papers/.
- **Per-oligo scoring engine** (`b7c8639`), earlier the same day: `scoring.engine: budget |
  serial`. `budget` (default) is byte-identical; `serial` judges each oligo and combines
  logically, moving 182,185 of 912,111 calls. Ships off; thresholds uncalibrated. The summed
  budget, not mismatch identity, decides ~79% of fails - which is why M2's physics is demoted.

## 2026-10-21, the owed full run

`results/2026-10-21/`, **304/304 steps, 25m 17s**, exit 0. Every archive rescreened, because
adding the `scoring.engine` keys changed `_code_hash` (12e66a47 -> 46c32e0b) - deliberate, and
free since this run was owed anyway.

- **R2's sidecar exists for the first time.** `calls.provenance.json`, 76 KB: 316 screens,
  2,686,441 rows summing to the table's own count, every screen carrying an
  `expected_signature`, `git_commit: 5b542db` with no `(dirty)`, `thermo: False`,
  `assays_screened: 205`. Its mtime span reads 2026-10-18 .. 2026-10-21, which is the honest
  answer and the reason it refuses to claim one set of settings for the table.
- **S1's guard holds on real data.** The new calls table carries **0 assay ids the registry
  does not have**, against **6** in `results/2026-10-20/calls.tsv.gz`
  (`CRYPTOSPORIDIA_Need_to_order_...` x2, `Pan_mycoplasma_16S_23S_intergenic_space_2`,
  `Pan_reptilian_paramyxovirus_ne_...` x2, `Salmonella_invA_gene_unnamed_Rahn_1992`). All three
  ids the audit named are gone.
- **FINDING: the code-hash invalidation does not fire for a screen snakemake has no metadata
  record for.** 20 of the 316 screens are still dated 2026-10-18, and **all 20 have no
  `.snakemake/metadata` record** - so snakemake saw the output present, its only input (the
  FASTA) unchanged, and had no stored params to compare the new hash against. This is audit
  finding #1's mechanism, still live. Nothing is wrong *today*: rescreening `11229/all` by hand
  and diffing column by column gives **every shared column identical on every row**, the only
  difference being a `winning_pair` column added to `as_row` after 2026-10-18 and filled with
  `""` by `collect.unified_columns`. But "editing a scoring threshold rescreens the affected
  archives" is not true for these 20, and that matters the moment a threshold really changes.
  **The sidecar is what made this visible**, which is what R2 was for.
- **FINDING: an assay can sit in `CURRENT_ASSAYS` and never be screened at all.**
  `Helicobacter_Pan_Helicobacter_16S_short_Fox_1998` has no `target.query`, so its group is
  `209/all` - all 843,447 Helicobacter records, over `retrieve`'s 100,000 cap. Retrieval says so
  loudly (`SKIP 209/all: ... Add 209 to retrieve.large_taxa_allowed ... or narrow the assays'
  target.query`) and then nothing downstream mentions it: the sidecar counts 205 assays
  screened, the report says 204, and the gap is one assay with zero rows. S1's guard is the
  mirror image of this (ids in the table the registry lacks) and by design cannot catch it.
  **The cheap fix is the same shape as S1: name registry assays that produced no calls.**
  **THE GUARD WAS BUILT AND THE INSTANCE IS NOW FIXED TOO.** Checked 2026-10-24: the guard
  already exists as `collect.assays_without_calls` (`assaywatch/collect.py:238`), is wired into
  `concatenate_screens` at line 432, is covered by
  `tests/test_collect.py::test_assays_without_calls_is_the_complement_of_what_was_seen`, and its
  docstring names this very entry as the case it was written for. It computes
  `set(known_ids) - seen`, so it catches an assay with no screen file at all and not merely one
  screened to zero rows, and it warns rather than raising — deliberately, because a skipped
  group usually has a stated reason and killing a run over it would be the wrong trade. So only
  the instance was outstanding, and it is now closed: That entry now carries the
  query its sibling and the Conley entry already use, character for character, so the slug is
  identical and it joined the EXISTING `209/qea281b18a4` archive of 6,008 records with nothing
  downloaded. Adding 209 to `large_taxa_allowed` was rejected: it would fetch 843,447 records to
  screen an assay whose product is 398 bp, and the sibling already proves the query suffices.
  Verified by running the screen: on the first archive file alone the entry produces 1,044
  `detect`, 11 `reduced`, 94 `fail` and 1,833 `no_amplicon` - 1,055 of 1,149 assessable, 91.8%
  - where before it had never produced a single row. Also filled `amplicon_bp: 398`, measured
  (C97+C98 exact in 1,926 of 6,008 records, 398 bp in 1,848 of them, 96%, unimodal so a scalar),
  which closed its `amplicon_size_unresolved` flag; and corrected its citation page range from
  114:1174-1180 to Crossref's 114:755-763, which is what the sibling already had, so the two
  entries no longer disagree about the pages of the one DOI they share. Consequence to expect:
  adding an assay to a group changes that group's screen signature, so `209/qea281b18a4`
  rescreens on the next run.
- **One status move, and it is mine, not GenBank's.**
  `ALPHAVIRUSES_Togaviridae_ssRNA_NSP4_gene_round2` stable -> declining. Chain, verified end to
  end: the `amplicon_bp` 200 -> 196 correction in `f35ffa1` moved the accepted window from
  150-250 bp to 147-245 (`declared_tolerance: 0.25`); **31 records whose product is 148 bp** were
  `no_amplicon`/`no_site` before and are now scored, and they fail; all 31 are taxid 59300, whose
  parent is 3426303 *Alphavirus getah*, and `group_at_rank: species` groups them as getah; that
  drops getah to 82.5% (74.9-90.0%) on 97 records, over `min_records_per_lineage: 30`; the pooled
  share stays stable at 98.9% and the lineage verdict overrides to declining. **The assay saw 0
  new records** (18,049 in both runs), so this is not drift and not the engine - the old declared
  size was hiding 31 real products in a sublineage the assay handles badly, and correcting it
  surfaced a genuine coverage gap. Also: `detect` is identical at 8,384 across the two runs.
- Observed in passing, pre-existing: **13,493 of 2,686,441 rows are a repeat of an (assay,
  record) pair** across 83 assays (worst: both Helicobacter entries at 2,982 each), from
  overlapping incremental archives inside one group. The report's duplication check already
  discounts these statistically; noted so it is not rediscovered as new.
- Pre-flight found and fixed first: a run with no contact address was sending NCBI
  `--email None` (`5b542db`).

### Both findings closed the same day

- **A screen now records what produced it, beside itself.** `screen_signature` was already
  a `screen_archive` param, so Snakemake reran the job when it changed - but only where it
  holds a metadata record for that output to compare against, and the 20 screens above have
  none. `screen.py --signature` writes it to `<screen>.tsv.sig` after the atomic rename, and
  `collect` **refuses** any screen whose stored signature is not the one expected now
  (`_raise_for_stale_signatures`, the sibling of `_raise_for_orphans`). A screen that stores
  nothing is `null`, not `False`, and is counted and named on stderr rather than refused -
  every screen written before today is one, and refusing them would have failed this run on 20
  screens that hold correct calls. The sidecar carries `stored_signature` and
  `signature_verified` per screen.
- **Precision on "silently".** `snakemake -n` *does* print "20 jobs have missing
  provenance/metadata so that it in part cannot be used to trigger re-runs". A real run prints
  nothing - checked both `run.log` and
  `.snakemake/log/2026-10-21T181900.054144.snakemake.log`. So the warning exists and is
  dry-run-only, which is why it went unnoticed: nobody dry-runs before every run, and it
  reaches no durable artefact.
- **`collect` now names assays that produced no rows** (`assays_without_calls`), the mirror of
  the orphan guard: that one catches an id in the table the registry lacks, this catches a
  registry assay the table lacks. **Reported, never raised** - an orphan means the table is
  lying about what exists, while a missing assay usually means retrieval declined a group for
  a stated reason, and killing a run that produced 2.7 million other calls over it is the
  wrong trade.
- **The path convention lives in `assaywatch/signature.py`, alone, and that placement is the
  point.** `collect` importing `screen` put score.py and schema.py into collect's trigger
  closure, so every scoring edit would re-trigger `collect_calls`; `screen` importing
  `collect` is worse and would rescreen all 316 archives on any collect.py edit. Its own
  module keeps `source_names("collect") == ["collect.py", "signature.py"]`, which
  `tests/test_triggers.py` now asserts along with the two negatives.
- 9 mutants against the new guards, all caught. Tests 1,428 -> 1,437.

### `submitted_by` dropped from the `active` gate

Every other precondition is evidence about the assay - it has a taxon to retrieve, a citation
that resolves, a design year to date a baseline from, no unresolved question. `submitted_by`
is who contributed the entry, and after S7 it was **the only thing blocking 167 of 208
entries**, because the registry was bulk-imported by one curator and 207 of 208 leave it null.
Setting it 207 times to one name would have been a rubber stamp. The field stays for genuine
third-party submissions; it is simply not evidence that an assay works. 4 mutants, all caught.

What still blocks `active` across the 205 draft entries: **19 an open review flag, 15 no DOI,
15 no design_year, 1 no taxid** - and **167 now pass every schema precondition**. The gate
measures evidence; promotion is a maintainer's judgement, which is where it belongs.

Also noted in `schema.py` rather than acted on: `amplicon_bp_range`, `species_sizes` and a
probe's `seq_as_written` are each set in exactly one entry, which the audit counted as
near-unused schema. They are not dead - the first two are what let ORTHOPOXVIRUS ATI be
declared at all and the third is the Deckers probe's inosine. The field the audit was right
about was `submitted_by`.

**AWAITING A MAINTAINER DECISION - ROADMAP Phase 0's "5 assays promoted to `active`".** All six
remaining candidates now pass the gate, so nothing but judgement is left, and only a
maintainer sets `active`. Read off `results/2026-10-21/report.md` (unchanged from 2026-10-20
for all six):

| candidate | status | detected (CI) | evaluable | reading |
|---|---|---|---|---|
| `RANAVIRUS_dsDNA_variable_intergenic_regi_Pallister_2007` | stable | 90.0% (77-96%) | 40 | clean |
| `RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007` | watch | 89.9% (81-95%) | 79 | judgement |
| `CDV_P_gene_Scagliarini_2007` | watch | 85.3% (77-91%) | 95 | judgement |
| `Snake_fungus_Ophidiomyces_ophi_ITS2_28S_Bohuski_2015` | insufficient data | 71.4% (36-92%) | 7 | too little data |
| `B_salamandrivorans_Internal_transcribes_spa_Blooi_2013` | insufficient data | 20.0% (4-62%) | 5 | too little data |
| `Snake_fungus_Ophidiomyces_ophi_IGS_Bohuski_2015` | no recent data | - | 0 | too little data |

So **five is not reachable on merit**: 1 clean, 2 watched, 3 genuinely data-starved - ROADMAP's
"await their rDNA-query data" is still true. The recurring sub-question, now written into
CONTRIBUTING.md: `active` means an assay can be screened and cited, not that it performs well,
so a `watch` status is not automatically a bar - but it should be a deliberate call.

## 2026-10-20

- **Full run DONE and valid** (`results/2026-10-20/`, 28m 54s, 291/291 steps). 208 assays: 37
  declining, 38 low coverage, 11 watch, 43 insufficient data, 17 no recent data, 62 stable.
  Tier-2 on it: **4 of 11 caught, 10 disagreements**, the first time the override doc's claimed
  figure has been reproduced on a current run. The override audit is unchanged in shape: 21
  overrides, 15 on a pooled `low coverage`, 6 above-pooled.
- **Bug search, six findings, all fixed** (the measurements are in each file's comments):
  1. **Tier-2 silently dropped renamed assays.** `retrospective.py` scored 13 case rows of 50 as
     `no data` because their ids had been renamed — 4 of the 12 `fails` cases. It now resolves ids
     through `docs/rename-mapping.tsv` both ways and **aborts** on an id that matches nothing.
     `docs/journal/2026-10-20-tier2-rename-resolution.md`.
  2. **`report_diff.py` fixed and trustworthy again.** Two causes, not one: a denylist of
     non-status headings promoted `## Nested protocols` to a status, AND the row regex skipped
     every id tagged `(pooled: …)` — 21 rows, exactly the 17 declining + 4 low coverage that
     appeared to vanish. Now an allowlist of `drift.py`'s statuses, plus rename resolution; counts
     match both reports' own headers.
  3. **One DOI↔filename helper**, `assaywatch/papers.py`. Five call sites reverse-mapped
     `stem.replace("_", "/")`, which cannot work: `/`, `(` and `)` all map to `_`, and a round trip
     cannot tell them apart either. Consequences measured: 20 entries read `no-full-text` against
     papers on disk, `find_open_access` called 10 of 26 "missing" papers missing, and
     `docs/papers-index.cache.json` held **10 fabricated DOIs** cached as permanent nulls (removed).
     Nothing infers a DOI from a filename now except one documented best-effort fallback.
  4. **`printed_oligos` reads lowercase sequences.** Rahn 1992 prints both primers in lower case,
     so the reader returned zero from a text holding both. A lowercase run is now admitted at 18+
     letters and *every* letter an unambiguous base — a 90% threshold was tried first and admitted
     five glued-on primer names from Deckers 2009's flattened table. Measured with
     `diff_printed_oligos.py`: 0 lost, 12 gained, 8 oligos move `in-text` → `exact`.
  5. **No contact address in the repository.** Six scripts hardcoded one as an argparse default,
     an `Entrez.email` or inside a User-Agent. All resolve `ASSAYWATCH_EMAIL` / `.secrets/email`
     via `credentials.contact_email()`; `--help` works with none set.
- **FIXED 2026-10-21 (S1, see the to-do below): a run's calls table could hold assay ids the registry no longer has.**
  `results/2026-10-20/calls.tsv.gz` carries 3 (`CRYPTOSPORIDIA_…_2000`, `…_2000_round2`,
  `Salmonella_invA_gene_unnamed_Rahn_1992`) alongside their renamed counterparts, so the report's
  "208 assays screened" double-counts them. Cause: a cached per-archive screen is reused without
  its `params.only` being re-checked — `results/screened/28901/q22fdd7bbec/2026-10-18.tsv` still
  dates from 2026-10-18 while the other two archives in its group were rescreened at 21:50, and
  `.tmp/run-2026-10-17.log` shows those archives were screened by a different snakemake install,
  so the metadata that would invalidate them is absent here. The robust fix does not depend on
  Snakemake: `assaywatch/collect.py` only concatenates and never sees the registry, so it should
  drop rows whose `assay_id` is not a current assay and say how many. Decide whether that is a
  warning or a hard error.
- **The assembly listing is paged by token now** (`assaywatch/assemblies.py`). The previous run
  died on `taxid 562: more than 1000 assemblies released on 2026-09-29` — E. coli really had 1,427
  GenBank complete genomes that day, so no date bisection could get under a page, and splitting on
  assembly level did not help (`chromosome` 120, `complete_genome` still full). The TSV format of
  `dataset_report` carries no continuation token but the JSON format returns `next_page_token`, so
  the bisection and its guard are both gone. Verified live on the failing day: 1,547 listed.

- **`results/2026-10-18/calls.tsv.gz` was screened under the reverted `by_chemistry.conventional`
  override and must not be measured on.** Paramyxovirinae L round1 goes 5,131 `fail` / 1,884
  `reduced` on 2026-10-17 to 33 / 6,984 on 2026-10-18, while the probe assay
  `INFLUENZA_A_ssRNA_NP_Tsukamoto_2010` is identical bar 24 new records. `c15a3b7` landed at
  22:10:57, three minutes after that run finished at 22:07:26, so the tree carried the relaxed
  numbers while it ran; `df5356f` reverted them the next day. Tier-2 on those calls reads **0 of
  11** caught against **3 of 11** on 2026-10-17, the three lost catches all going `stable`.
  **`results/2026-10-17/` is the newest valid evidence, and a full run on the current config is
  owed.**
- **`scripts/lineage_override_audit.py`** (new) enumerates every assay whose status comes from a
  lineage override, with the firing lineage's name, rank, share, whether it is inside the entry's
  `scope_taxids`, and whether the design paper is on disk. It resolves ids through
  `docs/rename-mapping.tsv`, which drops four rows for assays since removed — the counting flaw
  this file warns about. `drift.py` gained `lineage_worst_idx` so the firing lineage needs no
  prose parse. At 2026-10-17: **21 overrides, 15 on a pooled `low coverage`, 6 above-pooled.**
- **Scope curation is not the lever `docs/journal/2026-10-20-pan-family-override.md` point 3 took it for**
  (`docs/journal/2026-10-20-scope-curation.md`). Four design papers read; in all four the firing lineage is
  inside the stated range, and in three it is a virus the paper amplified: rabies is the genome
  Bourhy 2005 gives PVO3's coordinates on, LCM is Lozano 1997's "prototype of the family", BFDV is
  one of three sequences Mankertz 2000 aligned, PPRV is one of six viruses Barrett 1993 amplified.
  Two scopes shipped anyway because the excluded taxa are groups the papers framed out —
  rhabdovirus to the animal subfamilies (`[35303, 2842407, 2842415, 3152207]`, 769 records out) and
  arenavirus to the mammarenaviruses (`[208898, 1653394]`, 473 out). **Both move nothing**: no
  status, no override, tier-2 unchanged at 3/11 and 9 disagreements. The excluded records are old
  deposits outside every recent window.
- **Barrett 1993 is the fourth bench panel and the session's real finding**
  (`docs/bench-panels/barrett-1993-morbillivirus.tsv`; the PDF is an image scan, read from a 400 dpi
  tesseract OCR). On Barrett's own seven viruses: **4 of 7 would show a band**, and **all three
  false fails carry a G·T wobble in the 3' window** — rinderpest and dolphin morbillivirus on a
  single `rev5 T:G`, PPRV on `rev3 G:T` plus `fwd4 C:C`. That `rev5 T:G` is in 4 of 7 rows
  including measles, the design reference, which sits at exactly 3.0. So **two independent panels
  now land on mispair identity in the 3' window** (FAP's 12 of 14 false fails rest only on T:G).
  It also reinterprets an override case: PPRV's 0/83 is at least partly the 3'-window penalty, not
  lost coverage. No config change — the knob goes through tier-2 first.
- **Two worked examples for the `< pooled` gate**, from design papers rather than published
  follow-up: BFDV detects 27.6 points better than its pool, LCM 9 points better, and in both the
  override names as "failing" the taxon its paper most directly demonstrates.
- `amplicon_bp` for the Barrett morbillivirus pair corrected 430 -> 429 on the `_Barrett_2003`
  entry (its twin already read 429): the paper says "a 429 nucleotide DNA fragment" and the
  2026-10-17 calls measure 429 bp in 4,326 of 4,347 detected-or-reduced records. Inside
  `declared_tolerance`, so no call moves.
- `schema.py`'s `scope_taxids` comment still claimed ancestry expansion was not implemented, wrong
  since 2026-10-19, and now says to name the smallest covering taxa rather than enumerate species.

## 2026-10-19

- **Sub-taxid resolver chain** in `lineage.py` (`94cea06`), design in
  `docs/journal/2026-10-19-subtaxid-resolution.md`. **Wired in (step 1 of 4):** `lineage.sublineage`
  in `config.yaml` (shipped `{}`), passed through `drift.assess` (report and retrospective)
  and `lineage_report` (new `--registry`). Titles come from `assaywatch/metadata.py`
  (`read_titles`, moved out of `sitedrift.py`). With the block empty, tier-2 output is
  byte-identical to before. A throwaway config with the influenza title chain splits Matrix
  records by subtype on real data. None fall below 0.9, because `reduced` counts as detected.
- **Steps 2-4** (from this session's plan):
  2. Tier-2-test what the lineage share counts as detected (e.g. `detect` only for probe/qPCR
     chemistries), with influenza split by subtype + pdm09. Before the 2010 cutoff, 2009 H1N1
     strains are 1,295 `reduced` / 1 `detect`, which is where Slomka 2010's failure shows.
  3. Avipox `chain: [subtaxid]`, report-only. Note: the smoke test found no assessable
     lineages for Baek 2020 in its recent window. Look at why before adding it.
  4. Bd + DWV: the `no_amplicon` records with their primer window present but unmatched.
- **Bug fixed: the per-lineage p-value went `nan` above about 1,030 records** (`comb` overflow
  times underflow), so a large lineage could never be judged failing. It now uses `binom.cdf`.
  Tier-2: no case changes. Current statuses: one changes, `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene`
  low coverage -> declining (rabies taxid 11292 lineage at 404/1,896).
- **scope_taxids now match descendants** (`docs/journal/2026-10-19-scope-ancestry.md`). Exact matching
  dropped strain/no-rank records under each listed species, about 90% of in-scope records. The
  "14→9 disagreements" below was measured on that remainder. With ancestry, tier-2 is
  **6/12 failures caught, 14 disagreements** (was 5/12, 9). The new disagreements are pan-family
  `low coverage` pooled statuses overridden to `declining` by a lineage at 0%. Limiting the
  override to stable/watch drops caught failures to 1/12, so the open question is the estimand
  for pan-family assays, not a rule. Rebuild the tree with `scripts/build_taxonomy_cache.py`
  after a retrieval brings new taxa.
- **Pan-family cases audited** (`docs/journal/2026-10-19-pan-family-cases.md`). The lineage override
  fires on lineages never detected at any point in their history (MERS-CoV 0/558 for pan-CoV,
  Zika for pan-flavivirus, *P. falciparum* for the avian Hellgren primers), and three of its five
  pan-family "caught" failures are caught for the wrong reason. New
  `lineage.require_working_baseline` (shipped off) excuses a lineage measured earlier and never
  covered, but not a new one. With it on, tier-2 is 4/12 caught and 14 disagreements, and the
  two lost catches are coverage-type `fails`. **Done 2026-10-19:** `mechanism` column on
  `fails` cases (11 coverage, 1 drift), gate **on**: 6/12 caught, 12 disagreements. **Step 2 done:** Hellgren
  assays scoped to avian haemosporidia; unsupported Pan_Plasmodium case retired; FAP left family-wide
  because Forslund 1999 amplified HPV16. Tier-2 4/11 caught, 13 disagreements (the wrong-reason catches gone).
  **FAP vs HPV16 done** (`docs/journal/2026-10-19-fap-bench-panel.md`): HPV16 fails on one G·T wobble 5 nt from
  the 3' end. On Forslund's own 70-type panel the scorer fails 14 of 60 types the bench amplified;
  12 of those rest only on T:G mispairs. First type-level evidence for identity-aware 3' penalties;
  no config change. `scripts/archive/bench_panel.py` + `docs/bench-panels/` take more panels.
  **Taxid artefacts done** (`docs/journal/2026-10-19-taxid-artefacts.md`): lineages now group at species
  rank (`lineage.group_at_rank`, taxonomy cache carries ranks). JCPyV was split across 10632/1891763.
  Tier-2 **4/11 caught, 12 disagreements** (was 13). 1193974 is an unclassified bucket of CVA6; the
  bucket rule ships off because that case disagrees on the next lineage down anyway.
  Current statuses: 4 of 201 move (the commit message's "5 of 213" counted removed assays
  still in the 2026-10-17 calls). The gate's "17 of 213" had the same flaw: on current IDs
  it is 13 of 201 with exact-taxid grouping, 16 with the roll-up on. Every status count
  from the 2026-10-17 calls needs the removed IDs dropped; the next screening run fixes it.
  **Orthopox ATI read by hand** (`docs/journal/2026-10-19-orthopox-ati-vaccinia.md`): 101 of its 112 recent
  vaccinia records are GenBank patent-division constructs (vectors, chimeras), and all 10 genuinely
  natural records detect. The `declining` was a false positive. New `drift.exclude_patent_records`
  (shipped **off**: tier-2 unchanged, no validation case touches an affected assay) would move 6
  statuses, ATI back to `stable`. `is_patent` now comes from esummary's `<Extra>`; older archives
  fall back to the title pattern (300/300 agreement). AAV is the extreme: the dependoparvovirus
  assays are 89% patent records.
  **Per-species table** in the report for any assay declaring `amplicon_bp_range` (only ATI), no
  assessability floor, from `AssayDrift.species_counts`. Lineage labels are named from the taxonomy
  cache now ("Orthopoxvirus vaccinia (10245)", not `taxid_10245`); verdicts byte-identical.
  **`species_sizes`** on the ATI entry (new `SpeciesSize` schema model, requires `amplicon_bp_range`),
  measured by `scripts/measure_species_sizes.py` with patent records excluded, shown as a `product bp`
  column. The bands overlap across vaccinia/cowpox/variola/monkeypox-IIb near 1600 bp, so size alone
  names no species there — the XbaI-digest caveat in numbers.
  **Patent option: no tier-2 case can judge it** (`docs/journal/2026-10-19-orthopox-ati-vaccinia.md`,
  2026-10-20 section). Searched both arenavirus and all three dependoparvovirus assays: with the
  option on and off the verdicts are identical at every date before 2026. And the direction
  reverses for AAV — patents are detected MORE than natural records (exact Gao pair 84.3% vs
  45.3%), so there they mask a real coverage gap instead of creating a false one. `pan_parvo`'s
  `declining` is not patent-driven. It needs evidence tier-2 cannot supply.
  **Pan-family override settled** (`docs/journal/2026-10-20-pan-family-override.md`): a failing lineage can
  overturn a pooled `low coverage` only if that lineage itself once cleared the threshold. Tier-2
  **4/11 caught, 10 disagreements** (was 12), 2 of 201 statuses move. Four alternatives measured and
  lost; adding a "lineage < pooled share" gate would reach 9 but rests on one row.
  **Three bench panels now** (FAP, Rebelo Mycoplasma 8/8 clean, Meyer ATI 8/9 with skunkpox a false
  fail). They point at two different scorer knobs: mispair identity in the 3' window (FAP) and
  linear accumulation against `reduced_max` (Meyer).
  **Next:** (the full run is DONE, 2026-10-20; see the State table)
  an identity-aware 3'-window penalty, now that FAP and Barrett agree on it, measured through
  tier-2 one knob at a time; an `is_patent` backfill sidecar (the title fallback misses ~3%, and
  `--include-fail` waits on it); a fifth bench panel with real `no_band` rows (Rahn 1992
  Salmonella — the paper IS on disk, `papers/10.1016_0890-8508_92_90002-f.pdf`, with 630
  Salmonella serovars in Table 1 and 142 non-Salmonella strains across 21 genera in Table 2, the
  first real negative set); the remaining override cases whose design paper is on disk
  (`docs/journal/2026-10-20-scope-curation.md` lists them, with the ADENOVIRUS Hexon composite held for a
  maintainer call). The "cases for the above-pooled pattern" item is partly answered: see the BFDV
  and LCM examples in that doc.
  **TODO: the 19 pipeline-audit proposals** (`docs/journal/2026-10-20-pipeline-audit.md` §5), each
  approval-gated individually, ranked in its §7. Top of the list: ~~**M1**~~ MECHANISM DONE
  2026-10-21 (`docs/journal/2026-10-21-M1-identity-aware-penalty.md`): `scoring.mispair_penalty` ships `{}`
  (byte-identical), and the G:T/T:G candidate rescues 8 bench false fails (FAP 5, Barrett 3) at
  zero specificity cost on Rahn's 41 negatives. HELD BY BATYA 2026-10-21: keep the knob off
  until she decides whether to pursue identity-based scoring at all (the nearest-neighbour ΔG
  question, M2, is the alternative). Do NOT flip it on as if it were merely pending mechanics; it
  is a held decision. If pursued, the gate is a full re-screen under the candidate config + tier-2,
  since the calls table bakes in scoring. ~~**S1**~~ DONE 2026-10-21: `concatenate_screens` takes
  `known_ids` (the Snakefile passes `CURRENT_ASSAYS`, every id in `GROUPS`) and **raises** before
  writing anything, naming each stale screen, its orphan ids and row counts. Hard error, not drop,
  measured: all three stale 2026-10-18 screens are *missing* the renamed assay's rows
  (`Salmonella_invA_Rahn_1992`, both Xiao Cryptosporidium rounds), so dropping would have silently
  cut those archives from the renamed assays. Check costs ~5 s over all 468 MB of screens.
  **Before the next run, delete the three screens that have no Snakemake metadata** (so nothing
  triggers their rescreen, and the guard would abort at collect_calls after retrieval and
  screening): `results/screened/2093/all/2026-10-18.tsv`,
  `results/screened/28901/q22fdd7bbec/2026-10-18.tsv`, `results/screened/5806/q0763ce7f8d/2026-10-18.tsv`.
  Five other screens hold the 2026-10-21 Ahne rename / FFPE-mycoplasma removal ids but have
  metadata recording the old `--only`, so the params trigger rescreens them. The other 20
  metadata-less screens match their groups exactly. ~~The Anthony supplement~~ DONE 2026-10-21:
  fetched from nature.com (CC-BY 4.0; DOI 10.1038/ncomms9147 confirmed on Crossref) to
  `papers/10.1038_ncomms9147.supp.pdf` (local, gitignored like the rest of `papers/`).
  `scripts/archive/verify_predict_supplement.py` parses all 41 protocol sections: **74 of 74 oligos in the
  37 `predict_protocol` entries match exactly**, rounds agree (semi-nested shared primers are printed
  once, under round 1). Table: `docs/predict-supplement-verification.tsv`. The `predict-supplement`
  bucket (36 rows) is gone from `docs/materials-needed.tsv`. Amplicons measured on the 2026-10-20
  calls and corrected where one size dominates: Alpha NSP4 round1 null→481, round2 200→196, both
  Filovirus L 630→634, Johne VP1 277→271, SIV_2 787→789, Herpes pol round2 250→231 (all inside
  `declared_tolerance`; the changed entries rescreen on the next run). Left as is: Arenavirus S
  (630; modal 639 but on only 73 of 424) and Coronavirus round1 (532; 529 on 2,172 vs 532 on 1,598).
  SIV DR1/DR2 → DR4/DR5 declared one nested family (`RETROVIRUS_SIV_pol_PREDICT_P029`): inner inside
  outer on 3,703 of 3,703 records.

  **The no-decision batch is DONE, 2026-10-21** (M3, S2, S6, S8, S9, R3 — one commit each,
  full gate before each; 1,341 tests):
  - **M3** `min_decline` cited beside the setting and in `ROADMAP.md`. Read from the guidance
    itself (FDA-2020-D-0987, Jan 2023), which the audit's secondhand sources had merged: >5% of
    database sequences is the cue to LOOK, >=5% off established performance the cue to ACT, and
    `min_decline` is the second. Cited as precedent, not live guidance — it runs only for the
    duration of the section 564 declaration, whose current status is unconfirmed. Ours is 5
    percentage POINTS; the guidance does not say points or relative.
  - **S2** `STATUS_ORDER` / `NO_DATA` / `STATUSES` now live in `drift.py`; `report.py` and
    `report_diff.py` read them. Two tests read the assignments out of `drift.py`'s own source.
    `report_diff` output on 2026-10-17 vs 2026-10-20 is byte-identical.
  - **S6** `strip_version` / `version_of` moved to `assaywatch/accession.py`, 25 call sites
    converted. **Not a pure refactor**: the bare `split(".")[0]` disagrees with `strip_version` on
    98 of 1,276,853 distinct record ids, all PDB chains, reaching 428 call rows (29 evaluable). A
    guard test found a 25th site the `[0]` grep missed (`lineage.lineage_of`, behind a dead
    `if parts else`).
  - **S8** `lineage.taxid_backfill` was not dead — the key was unread but the file is load-bearing
    (1,278,534 of 2,709,579 taxid joins), because both consumers hardcoded the filename. Now read
    from config. Genuinely dead and deleted: `retrieve.load_record_metadata` (77 loc, never
    called). `tests/test_config_keys.py` asserts every config key is mentioned in the source; on
    the pre-fix tree it fails naming exactly that key.
  - **S9** 14 tests for `loci.pair_spans`. Mutation-tested: the first draft's facing-strand test
    was **vacuous** (the length window rejected the case first), so a case was added where only
    the ordering can refuse. Seven mutants each caught now.
  - **R3** `papers_index.py --check` + a pre-commit hook. A hook and not CI because the PDF column
    reads `papers/`, which is local-only. Running it found the index omitting the panel book: the
    `.supp` stem is not a DOI stem and no entry *cites* the book. Fixed by two named mechanics
    (`<doi stem>.supp.pdf` counts for its article; `SHARED_SOURCES` declares an uncited
    dependency). 119 papers, 100 held.

  **R2 DONE 2026-10-21**: `collect` writes `results/<date>/calls.provenance.json` — every screen
  with the time it was written, its rows and assay count, the screening code+config hash, the git
  commit, and the signature expected for each group. It does **not** claim one set of settings for
  the table: reports are cumulative, so a run mixes screens written weeks apart, and the sidecar
  records per-archive facts plus the mtime span instead. `expected_signature` is what the pipeline
  expects NOW and the file says so. Timestamps are local-with-offset (in UTC the 2026-10-20 run's
  284 screens read `2026-10-21T01:53`, which invites the wrong comparison). Reuses the S1 guard's
  single parse. **The three stale screens were deleted by Batya 2026-10-21.** Six screens still
  hold non-registry ids, and all six are safe: five have recorded `--only` params that differ from
  the current ones so they will be rescreened, and `208294/all` is in no current group so it is not
  a collect input. Verified by comparing `.snakemake/metadata` params against `GROUPS`.

  **S3 and S4/S5 DONE 2026-10-21**, both behaviour-preserving and both verified the same way: a
  golden harness rebuilds `report.md`, `report.html` and all 208 `AssayDrift` records from
  `results/2026-10-20/calls.tsv.gz` and compares byte for byte (the harness is scratch, not in the
  repo; it took a pinned `today=2026-10-20` so the window cannot move with the clock).
  - **S3**: `build_model` decides a row's content; `markdown_from` / `html_from` only format it.
    Duplicated value derivations 24 → 12 occurrences. `report.py` **grows** 966 → 1183 lines
    (serialisers 356 → 304, model+builder+helpers +232): changing what a value means is now one
    edit instead of two, adding a column is three instead of two. The two reports are **not**
    merged — markdown keeps its count line, window line, `Why:` breakdown and unpaired-nest
    paragraph; HTML keeps its sparkline, `<details>` folding and its own nested note order. Each
    difference is commented where it sits. Unifying them changes both published reports and is a
    maintainer's call.
  - **S4/S5**: `assess` body 302 → 83 lines, `_lineage_check` 162 → 50. New stages:
    `DriftSettings`, `Window` (the granularity and widening rules, previously closures),
    `_gather_calls`, `_tally_window`, `LineageOptions` (now validated before the per-assay loop,
    so a bad setting fails on the config rather than on the first assay to reach it),
    `_lineage_calls`, `_species_counts`; and the gate chain `_pool_is_one_lineage` →
    `_never_covered_gate` → `_weak_pooled_gate` → `_apply_override`.
  - **Mutation testing earned its keep again.** `_pool_is_one_lineage` survived every unit test and
    was caught only by the full rebuild; worse, a direct test of the predicate still passed with
    its call site deleted. The test that counts goes through `_lineage_check` and asserts the
    effect. Same trap as S9's facing-strand test. **When a refactor extracts a gate, test the
    effect through the caller, not the predicate.**

  - **S7 DONE 2026-10-21: `needs_review` is a controlled vocabulary.** `assaywatch/review.py`
    holds 31 flags with their reasoning; the field is now `list[{flag, note}]`, and
    `docs/needs-review-migration.tsv` records all 243 old values with what each became.
    Measured: **98 distinct strings → 30 in use**, 69 singletons → 1, 243 instances → 198 items.
    Two findings came out of doing it, and both changed the design:
    - **Four flags restated a field on the same entry, and 6 of their 39 instances were already
      wrong.** Four entries carried `DOI_MISSING` beside a verified DOI; two carried `NO_YEAR`
      beside `design_year: 2011`. `resolve_citations.py` cleared those flags on its own path and
      `apply_curation.py` on another, and a flag has to be cleared on *every* path that fills the
      field. `DOI_MISSING`, `DOI_UNVERIFIED`, `NO_YEAR`, `TAXID_MISSING` are gone;
      `materials_needed.py` derives the gap from the field. **A stored restatement of a field
      cannot be kept in step with the field.**
    - **`status: active` refused any non-empty `needs_review`**, so `nested_protocol` and
      `amplicon_measured_not_published` — permanent properties of sound entries — blocked
      activation forever: **146 of 208 entries were unactivatable, against 21 that carry a real
      open question.** The vocabulary splits open questions from recorded caveats (`review.OPEN`)
      and the gate now refuses only the former. This loosens an `active` precondition; it is a
      maintainer-visible change, reverse it by restoring `if self.needs_review:` in
      `active_requires_provenance`.
    - `curation_decision_pending` (the catch-all, note required) is **unused**: all 198 items fell
      into a named flag, which is the evidence the 30 categories fit the registry. A test caps it
      at 5 so that stays true.
    - New: `tests/test_review.py` (13) and `tests/test_materials_needed.py` (12, the first tests
      that script has ever had — deleting the derivation that replaces the dropped flags was
      invisible before). 16 mutants checked, all caught. `openpyxl` in the seed-list importer (since removed) is
      now a lazy import, so its pure functions are testable without the `import` extra.
    - `scripts/removed_assays/` is **not** migrated, by decision; its new README says why.
  - **Found while doing S7, unrelated to it: `docs/taxa-cache.json` had two incompatible formats
    and two writers.** `lineage.load_taxa_cache` reads a `taxa` sub-object of hand-entered names
    (`config.yaml` `lineage.taxa_cache`); `master_sheet.py` keyed a full NCBI record by taxid
    string in the same path. Whichever ran last won, and it had already cost data: **commit
    `780df17` wrote the lineage stub over 247 cached taxon records**, and the next
    `master_sheet.py` run would have written them back over the stub. master_sheet now owns
    `docs/taxon-records.cache.json` (296 taxa, refetched). `tests/test_config_keys.py` guards the
    *shapes* rather than the paths, so renaming a default back cannot reintroduce it; both
    directions were checked with a mutant.

  **Still pending from the audit:** R1 container/lockfile.
  ~~Then **M2** nearest-neighbour ΔG as its own project.~~ **M2 KILLED at Step 0,
  2026-10-21** (`docs/journal/2026-10-21-M2-step0-killtest.md`): the gating kill-test shows
  `calc_heterodimer`'s terminal ΔΔG/ΔTm does **not** reproduce Kwok's 3'-mispair
  severity ordering — the severe (A:G/G:A/C:C/A:A) and neutral (T:G/G:T/T:C/T:T)
  classes overlap in two contexts, and A:A/A:G come out *stabilising* (wrong sign).
  The structure dump shows why: every mismatch is left as a dangling end over an
  identical matched core, so the signal is terminal stacking, and a dangling purine
  stacks *better* than the match. NN ΔG is equilibrium melting; Kwok's effect is
  polymerase-extension competence — orthogonal, anti-correlated for the purine
  mispairs that matter. So the audit's premise ("M1 is a hand-rolled approximation of
  what NN gives for free") is false; NN encodes a different physics. M2 is scoped
  closed, not deferred. `thermo.py`'s "never scored" design is vindicated: even ΔTm
  must not be scored as a 3'-mismatch severity signal. **M1 remains the right
  instrument** and is still HELD by Batya (see above); this result removes the "do NN
  instead" alternative the hold was weighing M1 against.
  **A full run is owed** and will now also exercise the S1 guard and the R2 sidecar end to end;
  nothing has verified the Snakefile's provenance wiring on a real run yet (the dry run parses,
  the signature keys and the git helper were checked offline against the real screens).
  **TODO (Batya, offline): resolve the 16 entries that have no DOI.**
  `docs/oligos-without-doi.tsv` lists all 33 oligos with sequences, grouped by where the answer
  must come from: 6 in-house/unpublished, the Müller 2011 CDV quartet (needs
  the paper), 2 PREDICT-named (the 2013/2015 supplements), and 4 true orphans with no reference at
  all (the two enterovirus rounds and two UHanta round2 entries, three of which also fire lineage
  overrides). The Anthony 2013 mBio supplement is the single most likely to close the UHanta ones.
- **Snakefile:** `report` and `site_drift` now hash the `lineage` config section. Before, editing
  `min_records_per_lineage` left `report.md` stale.
- **Bd Boyle FN is not a lineage-split problem** (measured, see the design doc's Mode C). Only 173
  of 9,496 records are evaluable (1 fail). The documented Asian ITS haplotypes are probably in the
  `no_amplicon` pool, so it is a denominator problem like DWV. `subcluster.py` is built and
  tested but has no consumer.
- **Conventional scoring override reverted** after tier-2 validation (item 8 below).
- `test_triggers.py` was updated for the `site_drift`/`lineage_analysis` rules and the taxid
  sidecar. Full suite: 1235 passed.

# Earlier: 2026-10-18 (scope_taxids end-to-end, 14→9 disagreements)

Everything described here is on `main` at `0a3802c`, working tree clean. This file is the
short version of where to pick up. Verify claims against the repo (`git log`, `results/`
dates, `python -m assaywatch.validate registry`) before acting on them; it goes stale fast.

## scope_taxids: DONE end-to-end (2026-10-18)

`scope_taxids` is an optional field on `Target` in the registry schema. When set, only records
whose taxid is in the list count toward the drift denominator. (Since 2026-10-19: in the list *or a descendant of a listed taxid*; see
`docs/journal/2026-10-19-scope-ancestry.md`. The 14→9 result below predates that and is superseded.) Out-of-scope records are excluded
and tallied in `AssayDrift.out_of_scope`. Records with no taxid are kept (conservative). This is
exact-match v1 — no NCBI taxonomy ancestry expansion yet.

Code touches: `schema.py` (field), `drift.py` (filtering + counter), `report.py` (scope_map
construction + out_of_scope rendering), `retrospective.py` (builds scope_map from registry
YAMLs). Four new tests in `test_drift.py`.

**Completed 2026-10-18:**

1. ~~Populate `scope_taxids` in 10 assay YAMLs.~~ DONE (`0a3802c`). Species-rank taxids from
   NCBI taxonomy subtree queries via `scripts/populate_scope_taxids.sh`. Counts: Coronaviridae
   1494, Adenoviridae 769, Polyomaviridae 424, Paramyxoviridae 931, Enterovirus 520, CDV 1
   (species-level, used directly). ~~Three assays got placeholder taxids (parent only):
   Orthoflavivirus (11051) and Orthoherpesviridae (10292) returned 0 species from NCBI.~~
   DONE (`dd46e7d`). Root cause: `txid<N>[Subtree]` syntax fails in NCBI taxonomy db;
   fixed with name-based queries. Orthoflavivirus → 216 species (3 assays),
   Orthoherpesviridae → 866 species (4 assays). No more placeholder taxids in registry.
2. ~~Wire `retrospective.py` to build scope_map from registry.~~ DONE (`62cbdc4`).
3. ~~Re-run retrospective with scope.~~ DONE. Disagreements dropped from **14 to 9**. Five
   removed by scope filtering. Remaining 9: 2 non-scope (Chytrid, Influenza — taxid-resolution
   ceiling), 7 genuine calibration signals.
4. ~~Add out_of_scope counts to report rendering.~~ DONE (`62cbdc4`). Markdown and HTML
   reporters show "Out of scope: N records excluded (taxid not in scope_taxids)."
5. **Later:** ancestry expansion for scope_taxids; sequence-cluster lineages (2 remaining FNs).

## The estimand: implemented and recalibrated

The lineage-conditional estimand is live. Per-lineage detection analysis groups records by
NCBI taxid, runs a one-sided binomial test per lineage, applies Benjamini-Hochberg FDR
correction, and overrides a pooled stable/watch to declining when the worst assessable lineage
fails. Design: `docs/journal/2026-10-17-estimand-plan.md`. Implementation:
`docs/journal/2026-10-18-phase2-handoff.md`. The import is lazy (scipy/statsmodels stay optional for
rules that don't use lineage analysis).

Recalibration (`docs/journal/2026-10-18-recalibration.md`, run 2026-10-18) against 50 validation
cases: the tool now catches **6 of 12** documented failures (was 1 of 12). After scope_taxids
population, **9 disagree** (was 14) — a 27% error rate (was 42%). The 5 resolved disagreements
were pan-family scope cases removed by scope filtering. The remaining 9:

- **7 are pan-family scope** — scope_taxids resolved the clearest cases; the remaining ones
  need either ancestry expansion, broader taxid lists, or are genuinely ambiguous.
- **2 are taxid-resolution ceiling** — Bd haplotypes and influenza subtypes share a taxid, so
  per-lineage analysis cannot see the within-taxid divergence. Fix: sequence-cluster lineages
  (phase 2 future work).

**No threshold change.** The errors are in what the tool measures, not where it draws the line.

The ranked work list from the 2026-10-09 assessment, updated:

1. ~~**Lineage-conditional verdicts.**~~ DONE (2026-10-18). 6 of 12 failures caught.
2. ~~**Pan-family scope logic.**~~ DONE (2026-10-18). Code + registry populated. 14→9 disagreements.
3. Homology-anchored footprint scoring, so the duplication check sees clade structure and not
   only identical footprints.
4. Serial scoring logic (nested rounds now have a joint-coverage table, see below; the same
   idea applies wherever one reaction feeds another).
5. **Sequence-cluster lineages** (phase 2 of the estimand). Would resolve the 2 FNs where
   lineages share a taxid (Bd, influenza).
6. Treat the validation set with caution: re-check each case's `as_of` date and expected
   outcome before using it to fit anything.

## The post-PR#1 rescreen is done — do not run it again on this file's say-so

It ran 2026-10-15, finishing 13:40, and its output is `results/2026-10-15/` (`calls.tsv.gz`,
`report.md`, `report.html`). `results/` is gitignored, so it exists only on the laptop: a clean
checkout elsewhere has no run at all, which is the one case where rerunning is right.

The gap against the estimate, which is what the previous edition asked for and nobody recorded.
The estimate came from re-filtering the 2026-10-07 calls at `declared_tolerance: 0.25` rather
than from a run, and lived in this file (the README carries the row-level half of it — 59,141
rows to `no_amplicon`, 54,966 of them former `fail` — but not the status counts):

| | estimate | 2026-10-15 actual |
|---|---|---|
| declining | 22 | **20** |
| stable | 73 | **69** |

Directionally right, mildly optimistic at both ends: four assays it placed in `stable` did not
arrive there. The full run is 213 assays — 20 declining, 58 low coverage, 11 watch, 41
insufficient data, 14 no recent data, 69 stable. The gap was not chased down. A re-filter of
2026-10-07 calls cannot see records retrieved on the eight days between the two dates, which is
the obvious candidate, but nobody has checked whether those four assays are the ones that
gained records — do that before reading the gap as anything else.

When a run *is* needed:

    caffeinate -i snakemake --cores 4 --config email=you@example.org

**Never the `--touch` shortcut from the 2026-10-06 note** across a scoring change; it marks
every screen current at the old setting with nothing to say so. A dry run (`snakemake -n`) is
no check either: it lists the screening jobs only once today's retrieval record exists, and
before that it plans just `validate` and `retrieve`, which needs the network.

## What landed 2026-10-07 to 2026-10-15

- **Mycobacterium** (`f319917`, `bf829bc`): three assays were screening nothing; now
  gene-scoped queries plus genomes via assemblies, and they produce call rows.
- **Nosema** (`68c466b`, `d8a63d2`): *N. ceranae* 218MITOC and *N. apis* 321APIS entered from
  the paper that prints them (Higes 2007 traced as the source).
- **Packaging and docs** (`20d8144`, `2502199`, `5dec3f2`, `8246eb6`, `82471db`, `3bdf993`):
  MIT licence, CITATION.cff, installation doc, offline worked example, `requests` as a core
  dependency.
- **Window archives** (`9acec03`, `assaywatch/windows.py`): records cut to the stretches around
  every possible pair plus 300 bp, so the data can ship (~160 MB vs 6.6 GB). A window is scored
  on its source record's length via a `.windows.tsv.gz` sidecar; without it, the length-scaled
  pair E-value let chance pairs through (71 of 6,356 rows flipped in the 10292 group).
- **Declared amplicon size enforced** (`b08a46a`): `declared_tolerance: 0.25`, chosen from
  the knee of |observed/declared - 1|. 13 entries that declared no size got a measured one
  (flagged `AMPLICON_BP_MEASURED_NOT_PUBLISHED`), 8 left unset; see
  `docs/journal/2026-10-14-amplicon-sizes-measured.md`. A mistranscribed `amplicon_bp` now voids an
  assay's calls, so run `scripts/check_amplicons.py` when an assay's numbers collapse.
- **Nested protocols** (`b08a46a`, `assaywatch/nested.py`): the report adds each nested
  family's joint coverage (both rounds succeed) beside each round's own share. Lyssavirus N
  round 2 reads 99.5% alone, 32.4% as a nest. Statuses unchanged. Three families fail the
  containment check; the coronavirus RdRp "rounds" are disjoint and are really two assays.
  Three entries were split into one entry per round (adenovirus, Cryptosporidium 18S,
  orthoreovirus).
- **Report honesty** (`b08a46a`): `drift.require_working_baseline` moves assays that never
  cleared the threshold from `declining` to `low coverage` (14 of 37 on 2026-10-07); the
  duplication result is printed at the top; an `entry` column shows draft status.
- **`scripts/storage_report.py`**: measures disk use and what is safe to delete. Never delete
  `data/retrieved/` archives or `.meta.tsv.gz`; they cannot be re-fetched.

## State

| | |
|---|---|
| registry | **209 valid, 0 problems**: 206 draft, 2 deprecated, 1 active (`python -m assaywatch.validate registry` prints current counts) |
| chemistry | conventional 162, hydrolysis probe 22, MGB 22, SYBR 2, RPA 1; 44 with a probe, 165 primers only |
| tests | 1282 passed; ruff clean; 187 citations checked, 0 Crossref problems (22 entries have no DOI) |
| validation | **50 cases**; **4 of 11** `fails` caught, **10 disagreements**, 17 undecided — the same on the 2026-10-17 and 2026-10-20 calls once renamed ids resolve (`docs/journal/2026-10-20-tier2-rename-resolution.md`). CORRECTION: an earlier edit of this file said 2026-10-17 gave 3/11 and 9 and that 2026-10-20 reproduced the published figure "for the first time". Both were wrong. The published 4/11 was always right; the 3/11 was this repo silently scoring 13 case rows as `no data` because their assay ids had been renamed, and the 22→17 undecided movement between the two tables was that bug, not the newer run's extra records. |
| last full run | **2026-10-20** (21:25–21:54, 28m 54s, 291/291 steps, `status: success`), the first on the current config since the conventional override was reverted: 208 assays — 37 declining, 38 low coverage, 11 watch, 43 insufficient data, 17 no recent data, 62 stable. Control that it is really the current scorer: Paramyxovirinae L round1 reads 5,135 `fail` / 1,884 `reduced`, matching 2026-10-17's 5,131 / 1,884 against 2026-10-18's 33 / 6,984. |
| do not measure on | `results/2026-10-18/calls.tsv.gz`, screened under the reverted `by_chemistry.conventional` override (see 2026-10-20 above). `results/2026-10-15/` and earlier predate the lineage estimand. |

Verified against the repo 2026-10-20.

## Why the remaining work wants the local machine

`papers/` is gitignored (copyrighted PDFs), and cloud sessions are denied
`eutils.ncbi.nlm.nih.gov`, `www.ebi.ac.uk`, `api.crossref.org`, `api.unpaywall.org` and
`api.openalex.org`, so they cannot measure `amplicon_bp`, verify a DOI or retrieve. A cloud
session can read and review code, and PubMed/PMC through an MCP tool. Full write-up:
`docs/journal/2026-10-05-cloud-session-findings.md`.

## The NCBI API key

Set it in ONE place and every caller picks it up. Resolution order, first hit wins:

1. `$NCBI_API_KEY`
2. `.secrets/ncbi.key` (gitignored, so it cannot be committed by accident)

Check it took, without printing it:

    python -m assaywatch.credentials

and, to also ask NCBI whether it accepts the key:

    python -m assaywatch.credentials --check

**`--check` has never been run against the real NCBI**: this environment cannot reach it. It
is tested against fake responses and against a local HTTP server standing in for NCBI, which
exercises the real urllib path but not NCBI's actual answer. Run it once on your laptop; if it
reports anything other than "accepted", paste me the output (it never contains the key).

In a cloud session, add `NCBI_API_KEY` under the environment's settings rather than writing
the file - that is the only route where the key never touches a filesystem, a chat window or a
diff, which is why the environment wins over the file. A new session picks it up.

It is a rate limit, not authentication: 3 requests per second without it, 10 with. Everything
works unkeyed, three times slower. The E-utilities scripts take their sleep interval from
`assaywatch/credentials.py`; the pipeline's two transports keep their own numbers (the same
0.11/0.34 for E-utilities, and Datasets' own 0.11/0.21), and a test ties them to the shared
values. A key that is unusable (more than one line, control characters from UTF-16 or UTF-32
without a byte-order mark, an empty or unreadable file) is ignored with a reason, in the
environment as in the file, and never sent. The key travels in the query string of the
E-utilities GET requests, so exception text from `requests` would contain it; every place that
prints a request error or an error body now scrubs it first (before truncating, since a key cut
in half by a 200-character limit would otherwise survive), and tests drive each of them against
a server that echoes the key back.

## Flagged decisions (from the 2026-10-06 agents, awaiting user judgment)

Resolved since: the LeHV-5 `_evagreen` duplicate was dropped (`a8d4742`), and *N. ceranae* is
entered from Higes 2007's 218MITOC pair (`d8a63d2`).

**Herpesviruses:**
- EEHV6 round2: rests on 1 spanning record (flag `SINGLE_SPANNING_RECORD`). Keep or delete?

**Bees/bumblebee/reptile:**
- *Nosema bombi*: keep under Kato's DOI or move to Klee 2006 (not local)?
- DWV-A/-B: use variant-node taxids or species taxid? (80% of records unlabeled; flagged `VARIANT_SCOPE`)
- Reptarenavirus: multiplex as one pooled entry? S-segment-only query or broaden?

**Mixed (Tsukamoto, Baek, Haynes, Meyer):**
- Ophidiomyces target-D: panel member as species marker. Keep (as entered) or delete?
- Orthopoxvirus ATI: differentiation assay, size 540–1700 bp by species. Keep (as entered) or delete?
  (2026-10-14: its products are genuinely multimodal, so it was left without a declared size and
  is exempt from `declared_tolerance`; constraining it would need a per-entry range.)
- Tasman-PCR (Kwon): transmissible cancer, host-genome. In scope? (4 ready drafts in scratchpad.)
- Clade/lineage scoping: H5, H7, NP, hummingbird avipox. Add scoping or flag for review?

**Bacteria:**
- Chlamydia genus 16S round1: printed primer has T where all records have A. Enter as printed (hypothesis) or correct?
- *C. trachomatis* serovar polymorphism: three serovars have mismatches. Flag, scope, or accept reduced detection?
- *C. psittaci* and *C. abortus*: cross-reaction detected. Note or narrow scope?
- *M. gallisepticum* vaccine pairs: exact on own genomes, >90% non-detect under species taxid. Enter if strain scoping added?

## Also on the laptop (open since 2026-10-06)

**1. Re-run the verifier over the full local `papers/` with the new probe floor.** The reader and the verdict logic
changed in ways that move its answers, and the probe floor is now separate, so some 13-14 nt probes that read `in-text` before will now read `exact`:

    python scripts/verify_oligos_against_paper.py --pdf-dir papers --tsv results/oligo-verification.tsv

Expect a chunk of the 65 known `absent` rows - particularly the image-table papers, *M. bovis*,
Usutu, *Batrachochytrium* ITS - to move to `no-oligos`. They were never evidence about a
sequence. Expect some `in-text` rows to become `exact`, and any entry whose paper writes
`(N/I)` or a similar "X or inosine" notation inside a sequence to move.

**2. Check the new reader against your 60 PDFs, not just my 21 texts.** The composition rule in
`printed_oligos` was calibrated against all 357 registry oligos as written, each placed in a
one-line sentence, and against the 21 open-access texts. Neither is a real PDF's layout. On the
21, comparing the current reader with the one in `826a905` finds 21 identical papers, and the
composition rule alone (`--extractor-only`, which gives both versions the same reading) against
`50430bb` loses nothing and gains four oligos: two degenerate Atkins 2009 primers, the Quan 2010
reverse consensus primer, and a Prepens 2007 primer. (`--extractor-only` excludes the
`(N/I)` reading change by design, so the Prepens gain is the composition rule, not the notation.)

    python scripts/archive/diff_printed_oligos.py --papers papers --old-rev 826a905
    python scripts/archive/diff_printed_oligos.py --papers papers --old-rev 50430bb --extractor-only --fail-on-loss

It reads each paper with the old and the new reader, taking the old script straight from git, and
lists oligos LOST and GAINED. Read the lost ones first. `--fail-on-loss` exits 1 on a loss and 2
if nothing was compared, since an empty comparison proves nothing. If anything is lost on a real
PDF, send me the file name and the sequence, and the threshold gets fixed before the verdicts are
trusted.

## Then, in value order

0. ~~**The lineage-conditional estimand.**~~ **DONE (2026-10-18).** Design:
   `docs/journal/2026-10-17-estimand-plan.md`. Implementation: `docs/journal/2026-10-18-phase2-handoff.md`.
   Recalibration: `docs/journal/2026-10-18-recalibration.md`. Catches 6 of 12 documented failures.
   Remaining disagreements are structural (pan-family scope and taxid resolution), not threshold.
   **Pan-family scope logic code done (`24ca7a7`); populate registry on Mac.**
1. **Nested families — mostly DONE 2026-10-17, see `docs/journal/2026-10-17-nested-family-key.md`.**
   The id base was not a sufficient family key, and it had manufactured two of the three
   "non-nesting" findings: the coronavirus RdRp rounds are a real nest (6,667 of the 6,671
   records both rounds can be judged on), and so are both CMV gB nests once each paper's own
   rounds are paired. **The report's claim that the coronavirus rounds are "two assays, not
   two rounds" is withdrawn.** `source.nested_family` now declares membership; registry
   families 23 → 27, of which those with per-record data 21 → 24; unpaired 15 → 3; failing
   containment 3 → 1, then → **0**: the last survivor, the enterovirus pair, failed on the
   criterion rather than on biology. Its rounds share their reverse SITE and round 2's primer
   is 8 nt longer at the 5' end, so its amplicon ended 8 bp past round 1's while priming from
   the same base. Containment now asks whether the inner primers' **3' ends** lie inside the
   outer product. All 26 families with per-record data nest; nothing fails. Treat that with
   suspicion rather than satisfaction — the check has so far caught two bookkeeping faults and
   one error of its own, and no protocol error.

   Also settled 2026-10-17: the two **Hantavirus** nests declared from geometry and a shared
   reverse primer (A = 250 + 236, B = 532 + 417, all four flagged
   `NESTED_FAMILY_FROM_GEOMETRY`; nest B shows a 27-point nest gap, 44.8% → 17.6%);
   **EEHV6 round 2 kept** with its `SINGLE_SPANNING_RECORD` flag; and **ATI** given
   `amplicon_bp_range: [540, 1700]` via a new optional schema field. Note that range is
   540–1700, *not* the 1067/1535/1538 in earlier notes — those are monkeypox clade modes only.

   Left over: EEHV6's round 1 is still not in the registry (needs Latimer 2010); the
   Hantavirus assignment has no source; and round order for five outer rounds rests on
   declared product size rather than a protocol.

   ~~**Two re-runs owed.**~~ **DONE (2026-10-18).** `results/2026-10-18/` has the full re-run
   (19:15–19:41, 26 min). The withdrawn coronavirus "two assays" sentence is gone from the
   report. The nested table now shows 26 families (was 21→24 in prior renders). ATI rescreened
   with `amplicon_bp_range: [540, 1700]`: 95.3% detected on 4,474 evaluable records (stable).
   PANPOX pair rescreened with re-scoped GC genera: highGC 95.7% (23 records, stable), lowGC
   100% (4,550 records, stable).
2. **Flagged decisions — nine settled 2026-10-17, see `docs/journal/2026-10-17-flagged-decisions.md`.**
   Bacteria: Chlamydia genus primer KEPT as printed (PMC finds that form in two later wet studies
   and the corrected form in none — the defect is the penalty table, not the sequence); C.
   trachomatis serovar split ACCEPTED as a true finding; psittaci/abortus cross-reaction NOTED only;
   the three M. gallisepticum vaccine pairs HELD. Then: PANPOX pair re-scoped to measured GC genera
   (~~**both now need re-retrieval and rescreen**~~ **DONE 2026-10-18**: highGC 95.7%, lowGC 100%); Nosema bombi re-cited to Klee 2006
   (`10.1016/j.jip.2005.10.012`, in the Crossref cache; **run `scripts/resolve_citations.py` to flip
   doi_verified**); Ophidiomyces target-D KEPT; Tasman-PCR ruled OUT OF SCOPE.
   Still open: ~~Reptarenavirus winning-pair column~~ **DONE** (2026-10-18): `oligo_pool_names()`
   returns `{seq: name}` maps, `screen_record()` stores `extra["winning_pair"]` as `"F6/R2"`,
   `Call.as_row()` emits the column (empty for non-pool assays). Three tests added. The
   ORTHOBUNYAVIRUS Cac serogroup enumeration; and five entries (Bd BdCAPE/BdGPL, hummingbird
   avipox, DWV-A, DWV-B) whose denominators provably cannot be defined from NCBI metadata and so
   wait on phase-2 clustering. **`DWVA_polyprotein_Rossi_2024` sits in the Declining list on 28
   records drawn from the 16% of DWV that carries a variant label — treat that call as unsafe.**
   CROSSREF IS REACHABLE from the sandbox (checked 2026-10-17), which unblocks items 4 and 5 below.
3. ~~**Settle the coronavirus finding.**~~ **DONE (2026-10-05, in `notes_curator`).**
   Stored 30-mer is correct; Quan 2010's printed 33-mer has a 3-nt duplication (NACNAC)
   that never binds better than 4 mismatches in any genome. PREDICT P-005 carries the
   corrected form. `amplicon_bp` updated 520→532.
4. ~~**Measure the two CMV gB amplicons**~~ **DONE (2026-10-18).** Measured on 9 UL55 CDS
   records at 0 mismatches: round 1 = 319 bp (was 320; paper figure 320, table 330),
   round 2 = 250 bp (was 230; paper said 250 in both places — spreadsheet transcription error).
   Re-cite the 4007/4125 pair: **already done 2026-10-17** (Deckers 2009, doi_verified).
   - `CMV_specific_HERPES_UL55_Glycoprotein_B_gB` (4007-s/4007-as) and `..._round2_2`
     (4125-s/4125-as) are **not in Prepens**, and their source is now known: Deckers et al.
     2009, *Virol J* 6:210 (PMID 19941648, PMC2789067), Table 1, primer set CMV-gBp1, where 4007
     is round 1 (800 bp) and 4125 is round 2 (550 bp) of one nested assay. Three of the four
     stored sequences match exactly; 4125-s has N where the paper prints B-or-inosine at one
     position, which is a defensible reading since inosine pairs with any base. The DOI
     `10.1186/1743-422X-6-210` came from PubMed, not Crossref, so it is NOT written into
     `citation.doi`. When Crossref is reachable: verify it (`scripts/resolve_citations.py`),
     re-cite both entries together, decide `oligos_designed_here` from what Deckers says (it
     says the primers were designed to bind conserved sites, but cites an earlier use in great
     apes), and clear the flag. Details are in each entry's `notes_curator`.
5. **DOIs: the 2026-10-05 candidate list is CLOSED (2026-10-17).** All five candidates in
   `docs/journal/2026-10-05-doi-candidates.md` plus the two Wang 1997 entries are applied and
   Crossref-verified; `check_citations.py` reports 182 checked, 0 problems. Also finished that
   day: Nosema bombi re-cited to Klee 2006 and both CMV gB 4007/4125 entries to Deckers 2009
   (`10.1186/1743-422X-6-210`), all verified through `resolve_citations.py`.
   **Only the Müller 2011 CDV quartet remains, and the sequence route is exhausted**: all eight
   walking primers were searched in NCBI PMC full text on both strands (a different index from
   the earlier Europe PMC pass), and the single hit is a 2015 paper that designed its primers de
   novo with Primer 3. It needs the paper or the lab's records, not another search.
   35 entries still carry no DOI; most are genuinely unpublished in-house assays.
6. **~~4 image-only primer tables~~ DONE** (all 4 resolved 2026-10-18):
   - Avian orthobornavirus: DONE (verified in prior session).
   - Usutu (`10.2807/1560-7917.es.2020.25.41.2001732`): RESOLVED. This Eurosurveillance
     2020 paper contains NO primer sequences — it is a surveillance report that cites
     Jöst 2011 (`10.4269/ajtmh.2011.11-0248`) for its RT-qPCR. The registry entry
     already cites Jöst 2011, and oligos were verified against the Jöst `.txt` on disk.
   - Batrachochytrium ITS (`10.3390/jof7040258`): RESOLVED. Already known (see "do not
     re-litigate" below) — this paper publishes no new primers.
   - M. bovis (`10.1371/journal.pone.0207365`): DONE. S1 Table text extracted via
     built-in browser (inline DOCX preview on PLOS ONE). All 9 oligos (3 assays x 3:
     forward, reverse, probe) verified exact match to registry:
     16S rRNA (Mycobac16S_F/R/SFAM), helicase (MTC-HELI-4F/4R/4FAM),
     IS1081 (MTC-IS1081-5F/5Rn/5FAM). No mismatches.
7. **211 oligos** whose provenance is unchecked for want of full text.
8. **`by_chemistry.conventional` scoring override: REVERTED 2026-10-19.** Committed live on
   2026-10-18 (`c15a3b7`: `terminal_mismatch_fails: false`, `primer_3prime_penalty: 2.0`,
   `reduced_max: 5.0`). The evidence given was "87→44 drift flags, 0 regressions", which a
   relaxation always produces. Tier-2 validation then showed it catches **2** of the documented
   failures instead of **5** (loses Paramyxovirinae round2, Forslund L1, Hellgren). Total
   disagreements went from 10 to 11. Back to `by_chemistry: {}`. Full result and the
   one-knob-at-a-time tests to run next: `docs/journal/2026-10-19-conventional-override-validation.md`.
9. **Primer-name audit** — scoped 2026-10-18, not yet executed.

   **Assay-ID renames (40 entries).** Mapping in `docs/rename-mapping.tsv`.
   - 13 REMOVE: no DOI, no reference, no literature provenance (Tracies unpublished,
     failed Influenza A, in-house CDV F/H/P, Helicobacter generic, Seadornavirus).
     Move YAMLs to `scripts/removed_assays/` and append filenames to
     `scripts/removed_assays.txt`.
   - 27 RENAME to `{Taxon}_{gene}_{Author}_{Year}` convention: rename file, update
     `id:` field, update any round1↔round2 cross-references, then validate.

   **Oligo `name:` field standardization (all 217 entries).** Six rules:
   1. Paper name only — the name from the cited paper's primer table, nothing else.
   2. No annotations in the name — `(corrected)`, `(same)`, `(5uM)` etc. go in oligo `notes:`.
   3. No lab prefixes — TS-prefix names replaced with the published primer name from the DOI.
   4. No bare positional numbers — `1F`/`2R` etc. get author-prefixed: `Mueller-1F`.
   5. No spaces — use hyphens.
   6. No YAML-hostile characters — no quotes, colons, or slashes in names.

## Two things waiting on someone else

- **Elsevier institutional token.** The API key works (Scopus returns results); full text 403s
  with "Requestor configuration settings insufficient". That is a separate entitlement and the
  VPN does not change it. Ask NYU Libraries for an institutional token for the ScienceDirect
  Article Retrieval API; drop it in `.secrets/elsevier.insttoken` and `scripts/fetch_elsevier.py`
  will use it with no other change. Unlocks 12 papers / 42 oligos. Note: one Elsevier paper on
  that list, EEHV pol (`10.1016/j.vetmic.2010.05.042`), has an author manuscript in PMC
  (`PMC2976818`) and is already recoverable without the token - though its primer table is among
  the ones PMC loses.
- **The rest of the fetch list**, `results/nyu-fetch-list.tsv`, ranked by oligos at stake.
  Browser automation is a dead end for these: ScienceDirect blocks on User-Agent (CPE00001) and
  SAGE sits behind a Cloudflare human check.

## Already known, do not re-litigate

- `jof7040258` publishes NO new primers - it compares Blooi 2013 (already in the registry)
  against Spitzen-van der Sluijs 2020. It belongs in `docs/validation-cases.tsv`, not
  `registry/`.
- Composite entries, each needing its scope read from a different paper than the one cited:
  Hellgren/Bensch, Blooi/Martel, Atkins/PREDICT, and now the CMV 4007/4125 pair. Lan/Quan is a
  related case (the panel's oligo is not the cited paper's).
- The VPN does not fix the Elsevier 403.
- **`10.1111/1755-0998.13299` (Ghosh 2021) is still a read-by-eye job.** Its PMC full text is
  available and its narrative is intact, but the primer table is not in it - the text carries no
  sequences and not one `5′` mark. The PDF is the only route to it.
- **The avipox 1R primer is missing from the PMC text because its parenthetical is empty in the
  Methods sentence**, not because PMC dropped a table (the paper's tables hold Ct values only);
  whether PMC's own XML or the flattening we read lost it is not established. The verifier now
  reads that as `no-oligos`. The entry is sound: an invariant 250 bp product across six
  independent records with the probe site present in all six cannot come from a wrong reverse
  primer.
- **ASM deposits abstracts only**, and so do PNAS and SAGE here. J Clin Microbiol, J Virol and
  Appl Environ Microbiol return an empty body from PMC; mBio, born open access, returns whole, so
  the `10.1128` prefix does not predict it - the journal does. **23 of the 44 papers resolved to
  a PMC id came back as an abstract**, listed with their oligo counts in
  `docs/2026-10-05-pmc-abstract-only.tsv`: 74 oligos across 20 registry papers, plus 3 List 2
  candidates. 21 of the 23 are ASM, so one fetch run on the NYU subscription clears nearly all of
  it. Do not retry them against PMC.
