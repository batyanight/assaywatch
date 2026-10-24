# Resume point, 2026-10-23 (waves 0-5 of the plan of attack landed; see below)

## 0b. Timekeeping is finished, and 658 MB of archives belong to nobody

`docs/2026-10-18-pipeline-timekeeping-todo.md`. **All seven items are done**: item 7
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
moving ten entries to `pending/`. `scripts/orphan_archives.py` reports them and
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
screen byte for byte. Resizing alone reruns nothing. And the local wall-time gain at `--cores 4` is
expected to be small: the real wins are the tail, via `priority`, which had been
ranking a 52-second archive near the back of the queue because it was 10 MB, and
correct CPU requests on SLURM.

## 0a. The oligo flags are adjudicated; four sequences were wrong

`docs/2026-10-23-oligo-adjudication.md`. Every `near:` and `absent` row was read
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

`docs/2026-10-23-verified-doi-gate.md`. `registry/` holds 198 entries, all
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

- **Wave 0** `docs/2026-10-23-baseline.md` — `results/baseline-2026-10-22/` frozen as the
  comparison point, the full tier-2 matrix, and the first precision figure ever computed:
  **2 of 9 `declining` calls were real failures**.
- **Wave 1** `docs/2026-10-23-wave1-report-honesty.md` — **704 of 1,512 per-lineage
  intervals were zero-width** (a Wald interval in `lineage.py`); 19 assays carried a
  status their own registry entry denies; the duplication check never saw an overridden
  flag.
- **Wave 2** `docs/2026-10-23-wave2-diverged-and-patent.md` — `count_diverged_as_fail`
  tested and **kept off** (55 of Bd's 63 `diverged` records are 2014 JAM81 mRNAs matched
  by chance); `exclude_patent_records` turned **on**, on mechanism, without tier-2
  approval, with the rule for doing that written beside the setting.
- **Wave 3** `-wave3-bd-miss.md`, `-wave3-usutu.md`, `-wave3-influenza.md`,
  `-wave3-holm.md` — all three documented misses are **scoring** problems, not
  statistical ones. Holm replaced BH and moved nothing yet.
- **Wave 4** `docs/2026-10-23-wave4-holdout.md` — `validation-cases.tsv` is now labelled
  the **development set**; `scripts/holdout.py` prices what tuning on it bought;
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
(`scripts/promote.py`, and `docs/2026-10-23-wave5-what-active-means.md` recommends
`--tier clean` — the oligo-provenance objection to promoting is now much weaker, 38
uncheckable rather than 106, so this decision is ripe); collect held-out cases (plan 4.2, shared with the C2 bench corpus in
`docs/bayesian-scoring-plan.md`); build the archive-scale anchor test that
`count_diverged_as_fail` needs; and `subcluster.py`, built, tested and still unwired.

## 2026-10-22, M1 tier-2: DECIDED. The wobble discount is reverted

Full write-up: `docs/2026-10-22-M1-tier2.md`.

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
measured against. Write-up: `docs/2026-10-22-unsigned-screens-cleared.md`.

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
passes 44/44. Full write-up in `docs/2026-10-18-pipeline-timekeeping-todo.md`, which now has
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
`docs/2026-10-17-estimand-plan.md`, which a parallel session shipped from two days later
(BH not Bonferroni, `mechanism` column not `lineage`, species-rank grouping, no
`drift.subgroup`). It also conflicted on this file with ~140 commits of staleness on its
side. Salvaged into `docs/2026-10-22-lineage-plan-salvage.md` before closing:

- **A GenBank-availability ceiling nobody on main had written down.** If Lotta 2019's cyt b
  sequences postdate the 2016-12-31 cutoff, the two Hellgren rows are uncatchable by any
  in-silico method and **the honest ceiling is 9 of 11, not 11** - i.e. every "N of 11" in
  the project quotes an unreachable denominator. Distinct from the taxid-resolution ceiling
  in `docs/2026-10-18-recalibration.md`. Checkable locally with no network (archives carry
  deposition dates); it was Phase 0's go/no-go and was never run. It does NOT weaken the
  M1 revert - that rests on the pooled coverage call, a different estimand.
- **Footprint groups as lineage units**, with the per-unit `no_site`/`diverged` exclusion
  share. main groups by taxonomy only and has no equivalent disclosure.
- **Still open: do `partial` rows count as successes when the tool names their gap?** The
  other two decisions the PR asked for were settled de facto on main. This one decides what
  the paper's main figure claims.

## 2026-10-22, the `.supp` convention reached the oligo verifier; 3 citations resolved

Full write-up: `docs/2026-10-22-supplements-and-three-citations.md`.

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
- **Open, wants the maintainer**: the three `ORTHOBORNAVIRUS_XP_*` Sigrist entries. Their
  supplement IS now read and DOES carry a primer table (Table S4), and none of their oligos is in
  it; `BornaPCA6` is 1 edit from the printed `PaBVcon_1401+`, and Table S5 prints `BornaA_A674N`
  where the registry has `BornaA_A647N`. Also open: the Enterovirus 5'UTR-VP4/VP2 pair, where
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
  refactor. **Pull before starting a session from now on.**
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
`docs/2026-10-21-drift-window-calibration.md`) showed the knobs act separately: the minimum
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
     `docs/2026-10-20-tier2-rename-resolution.md`.
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
- **Scope curation is not the lever `docs/2026-10-20-pan-family-override.md` point 3 took it for**
  (`docs/2026-10-20-scope-curation.md`). Four design papers read; in all four the firing lineage is
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
  `docs/2026-10-19-subtaxid-resolution.md`. **Wired in (step 1 of 4):** `lineage.sublineage`
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
- **scope_taxids now match descendants** (`docs/2026-10-19-scope-ancestry.md`). Exact matching
  dropped strain/no-rank records under each listed species, about 90% of in-scope records. The
  "14→9 disagreements" below was measured on that remainder. With ancestry, tier-2 is
  **6/12 failures caught, 14 disagreements** (was 5/12, 9). The new disagreements are pan-family
  `low coverage` pooled statuses overridden to `declining` by a lineage at 0%. Limiting the
  override to stable/watch drops caught failures to 1/12, so the open question is the estimand
  for pan-family assays, not a rule. Rebuild the tree with `scripts/build_taxonomy_cache.py`
  after a retrieval brings new taxa.
- **Pan-family cases audited** (`docs/2026-10-19-pan-family-cases.md`). The lineage override
  fires on lineages never detected at any point in their history (MERS-CoV 0/558 for pan-CoV,
  Zika for pan-flavivirus, *P. falciparum* for the avian Hellgren primers), and three of its five
  pan-family "caught" failures are caught for the wrong reason. New
  `lineage.require_working_baseline` (shipped off) excuses a lineage measured earlier and never
  covered, but not a new one. With it on, tier-2 is 4/12 caught and 14 disagreements, and the
  two lost catches are coverage-type `fails`. **Done 2026-10-19:** `mechanism` column on
  `fails` cases (11 coverage, 1 drift), gate **on**: 6/12 caught, 12 disagreements. **Step 2 done:** Hellgren
  assays scoped to avian haemosporidia; unsupported Pan_Plasmodium case retired; FAP left family-wide
  because Forslund 1999 amplified HPV16. Tier-2 4/11 caught, 13 disagreements (the wrong-reason catches gone).
  **FAP vs HPV16 done** (`docs/2026-10-19-fap-bench-panel.md`): HPV16 fails on one G·T wobble 5 nt from
  the 3' end. On Forslund's own 70-type panel the scorer fails 14 of 60 types the bench amplified;
  12 of those rest only on T:G mispairs. First type-level evidence for identity-aware 3' penalties;
  no config change. `scripts/bench_panel.py` + `docs/bench-panels/` take more panels.
  **Taxid artefacts done** (`docs/2026-10-19-taxid-artefacts.md`): lineages now group at species
  rank (`lineage.group_at_rank`, taxonomy cache carries ranks). JCPyV was split across 10632/1891763.
  Tier-2 **4/11 caught, 12 disagreements** (was 13). 1193974 is an unclassified bucket of CVA6; the
  bucket rule ships off because that case disagrees on the next lineage down anyway.
  Current statuses: 4 of 201 move (the commit message's "5 of 213" counted removed assays
  still in the 2026-10-17 calls). The gate's "17 of 213" had the same flaw: on current IDs
  it is 13 of 201 with exact-taxid grouping, 16 with the roll-up on. Every status count
  from the 2026-10-17 calls needs the removed IDs dropped; the next screening run fixes it.
  **Orthopox ATI read by hand** (`docs/2026-10-19-orthopox-ati-vaccinia.md`): 101 of its 112 recent
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
  **Patent option: no tier-2 case can judge it** (`docs/2026-10-19-orthopox-ati-vaccinia.md`,
  2026-10-20 section). Searched both arenavirus and all three dependoparvovirus assays: with the
  option on and off the verdicts are identical at every date before 2026. And the direction
  reverses for AAV — patents are detected MORE than natural records (exact Gao pair 84.3% vs
  45.3%), so there they mask a real coverage gap instead of creating a false one. `pan_parvo`'s
  `declining` is not patent-driven. It needs evidence tier-2 cannot supply.
  **Pan-family override settled** (`docs/2026-10-20-pan-family-override.md`): a failing lineage can
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
  (`docs/2026-10-20-scope-curation.md` lists them, with the ADENOVIRUS Hexon composite held for a
  maintainer call). The "cases for the above-pooled pattern" item is partly answered: see the BFDV
  and LCM examples in that doc.
  **TODO: the 19 pipeline-audit proposals** (`docs/2026-10-20-pipeline-audit.md` §5), each
  approval-gated individually, ranked in its §7. Top of the list: ~~**M1**~~ MECHANISM DONE
  2026-10-21 (`docs/2026-10-21-M1-identity-aware-penalty.md`): `scoring.mispair_penalty` ships `{}`
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
  `scripts/verify_predict_supplement.py` parses all 41 protocol sections: **74 of 74 oligos in the
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
  2026-10-21** (`docs/2026-10-21-M2-step0-killtest.md`): the gating kill-test shows
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
`docs/2026-10-19-scope-ancestry.md`. The 14→9 result below predates that and is superseded.) Out-of-scope records are excluded
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
fails. Design: `docs/2026-10-17-estimand-plan.md`. Implementation:
`docs/2026-10-18-phase2-handoff.md`. The import is lazy (scipy/statsmodels stay optional for
rules that don't use lineage analysis).

Recalibration (`docs/2026-10-18-recalibration.md`, run 2026-10-18) against 50 validation
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
  `docs/2026-10-14-amplicon-sizes-measured.md`. A mistranscribed `amplicon_bp` now voids an
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
| validation | **50 cases**; **4 of 11** `fails` caught, **10 disagreements**, 17 undecided — the same on the 2026-10-17 and 2026-10-20 calls once renamed ids resolve (`docs/2026-10-20-tier2-rename-resolution.md`). CORRECTION: an earlier edit of this file said 2026-10-17 gave 3/11 and 9 and that 2026-10-20 reproduced the published figure "for the first time". Both were wrong. The published 4/11 was always right; the 3/11 was this repo silently scoring 13 case rows as `no data` because their assay ids had been renamed, and the 22→17 undecided movement between the two tables was that bug, not the newer run's extra records. |
| last full run | **2026-10-20** (21:25–21:54, 28m 54s, 291/291 steps, `status: success`), the first on the current config since the conventional override was reverted: 208 assays — 37 declining, 38 low coverage, 11 watch, 43 insufficient data, 17 no recent data, 62 stable. Control that it is really the current scorer: Paramyxovirinae L round1 reads 5,135 `fail` / 1,884 `reduced`, matching 2026-10-17's 5,131 / 1,884 against 2026-10-18's 33 / 6,984. |
| do not measure on | `results/2026-10-18/calls.tsv.gz`, screened under the reverted `by_chemistry.conventional` override (see 2026-10-20 above). `results/2026-10-15/` and earlier predate the lineage estimand. |

Verified against the repo 2026-10-20.

## Why the remaining work wants the local machine

`papers/` is gitignored (copyrighted PDFs), and cloud sessions are denied
`eutils.ncbi.nlm.nih.gov`, `www.ebi.ac.uk`, `api.crossref.org`, `api.unpaywall.org` and
`api.openalex.org`, so they cannot measure `amplicon_bp`, verify a DOI or retrieve. A cloud
session can read and review code, and PubMed/PMC through an MCP tool. Full write-up:
`docs/2026-10-05-cloud-session-findings.md`.

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

    python scripts/diff_printed_oligos.py --papers papers --old-rev 826a905
    python scripts/diff_printed_oligos.py --papers papers --old-rev 50430bb --extractor-only --fail-on-loss

It reads each paper with the old and the new reader, taking the old script straight from git, and
lists oligos LOST and GAINED. Read the lost ones first. `--fail-on-loss` exits 1 on a loss and 2
if nothing was compared, since an empty comparison proves nothing. If anything is lost on a real
PDF, send me the file name and the sequence, and the threshold gets fixed before the verdicts are
trusted.

## Then, in value order

0. ~~**The lineage-conditional estimand.**~~ **DONE (2026-10-18).** Design:
   `docs/2026-10-17-estimand-plan.md`. Implementation: `docs/2026-10-18-phase2-handoff.md`.
   Recalibration: `docs/2026-10-18-recalibration.md`. Catches 6 of 12 documented failures.
   Remaining disagreements are structural (pan-family scope and taxid resolution), not threshold.
   **Pan-family scope logic code done (`24ca7a7`); populate registry on Mac.**
1. **Nested families — mostly DONE 2026-10-17, see `docs/2026-10-17-nested-family-key.md`.**
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
2. **Flagged decisions — nine settled 2026-10-17, see `docs/2026-10-17-flagged-decisions.md`.**
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
   `docs/2026-10-05-doi-candidates.md` plus the two Wang 1997 entries are applied and
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
   one-knob-at-a-time tests to run next: `docs/2026-10-19-conventional-override-validation.md`.
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
