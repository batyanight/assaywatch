# TODO before the next full run: better timekeeping markers

Written 2026-10-18 during the 2026-10-17 full run.

**Status, 2026-10-23: ALL SEVEN ARE DONE.** Item 7 landed today; see
"Item 7 as built" below, and note that it does not do quite what this list asked
for, because what it asked for turned out to be unavailable at the moment the
report is written. The line that used to stand here - "Nothing here has been implemented" -
was true when written and stale for days afterwards. Per item:

| # | item | state |
|---|---|---|
| 1 | stage banners + run manifest JSON | **done** - `RunManifest` writes stage wall times to `results/<date>/run-timing.json`, and `onstart` prints the run banner (`Snakefile:244-281`) |
| 2 | per-rule `benchmark:` (wall time, max RSS) | **done 2026-10-22** for `retrieve` and `screen_archive`, with one caveat below: on macOS only the wall-time columns fill in |
| 3 | retrieval/screening progress lines | **done** - `screening_progress(RETRIEVED, SCREENED)` feeds the heartbeat from bytes screened, not step count |
| 4 | heartbeat file | **done** - `.tmp/heartbeat-<date>.json`, `heartbeat_seconds` configurable (default 60) |
| 5 | weighted ETA | **done** - `timing.weighted_eta`, projected from bytes rather than remaining steps |
| 6 | stuck detector | **done** - `heartbeat(stall_after=...)`, `stall_seconds` configurable (default 900) |
| 7 | final per-stage summary + top 10 slowest groups in the report footer | **done 2026-10-23** - `report.timing_lines`, rendered into both the markdown and the HTML report. Only benchmarks written inside the run's own window are counted, which is what makes the sleep problem below harmless |

Read "What the numbers say" below before touching any of it: the benchmarks on disk were written across 91 minutes of laptop
sleep. The RUN_DATE bug
recorded at the bottom of this file is **fixed** (`timing.resolve_run_date` +
`write_run_marker`, `Snakefile:79`); it is kept below as the record of why.

## Item 7 as built (2026-10-23)

`assaywatch.report.timing_lines` appends a `## Run timing` section to both the
markdown and the HTML report, from `assaywatch.timing.read_screen_benchmarks`.
Two things about it are not what this list asked for, and both are forced:

**The stage table usually describes the PREVIOUS run.** The Snakefile closes its
`workflow` stage in `onsuccess`, which fires *after* the `report` rule, so while
the report is being written this run's own stage has no duration yet. A footer
that insisted on this run's stages would have printed an empty table in every
run forever. So the footer prefers this run's stages when they are complete - a
report re-rendered by hand afterwards, which is how it was developed - and falls
back to the most recent completed run, saying which it is showing. Changing that
would mean moving the report after `onsuccess`, which is a pipeline-shape change
for a footer.

**Only benchmarks written inside the run's own window are counted**, filtered on
file mtime against the manifest's `started`/`finished`. This is what defuses the
sleep problem recorded below: a benchmark is keyed by archive rather than by run
date, deliberately, so a cached screen keeps its old measurement and a bare
directory read mixes generations - including the 2026-10-22 files that span 91
minutes of suspension. A run whose screens were all cached measured nothing, and
the footer says exactly that rather than ranking stale rows. Four tests pin these
two behaviours, because both failure modes are silent: a stale row looks like a
measurement and an empty table looks like a fast run.

The macOS caveat travels with the numbers rather than living only here: the
footer states in the report that `max_rss` and `cpu_time` read `NA` on this
platform, so the column shown is elapsed time and not CPU.

### Found while populating clean benchmarks: 10 orphan retrieval groups

Item 7 needed one set of benchmarks taken on a machine that stayed awake, so
every archive was force-rescreened under `caffeinate`. Targeting every archive on
disk failed at DAG construction:

    InputFunctionException in rule screen_archive:
    KeyError: (2093, 'q4185828e3e')

That archive's group is not in the registry any more. Ten groups are in that
state - 21 archives, 658 MB, and 99 entries in `data/retrieved/manifest.json`
that look like ordinary retrieval state. A group dies two ways, both routine: an
assay leaves `registry/`, or its `target.query` changes, since the group name is
a hash of the query. Three of the ten were orphaned *that same day* by moving ten
entries to `pending/`.

`scripts/orphan_archives.py` reports them, attributing each to a `pending/` entry
where that explains it, and deletes nothing: an assay waiting on a DOI comes back,
and its archives are the history its baseline needs. It also names the mirror-image
gap, a live group with no archive at all (currently `209/all`).

## Item 2 as built (2026-10-22)

`benchmark:` on `retrieve` and `screen_archive`, under `results/benchmarks/`:

- `results/benchmarks/retrieve/<date>.tsv` - one per day, matching the rule's own
  date-keyed output. Retrieval is one job for all groups and it is the stage that
  has run for hours, so this is the number the PANPOX stall would have produced.
- `results/benchmarks/screen/<taxid>/<group>/<stem>.tsv` - keyed by the archive,
  **deliberately not by run date.** A screen is cached across runs, so a
  date-keyed benchmark would be missing for every cached archive on the next run.
  Verified that this does not churn the cache: `snakemake -n` after adding the
  directive schedules **zero** `screen_archive` jobs, i.e. a missing benchmark
  file does not invalidate a screen. `tests/test_triggers.py` still passes 44/44,
  so the rerun sets are unchanged.
- A benchmark therefore exists exactly where its screen does, holds the most
  recent measurement for that archive, and carries no timestamp of its own - when
  it was taken is its mtime, the same evidence `screened_at` rests on.

**The macOS caveat, so nobody re-investigates a column of NA.** On this laptop
these files record **wall time only**. Snakemake samples with psutil's
`memory_full_info()`, which macOS refuses for a child process (`AccessDenied`,
verified directly), and its sampling loop skips a process it cannot read without
ever setting `data_collected` - so `max_rss`, `max_vms`, `max_uss`, `max_pss`,
`io_in`, `io_out`, `mean_load` and `cpu_time` all read `NA` however long the job
runs. A 0.44 s screen and a 7.9 s screen both behave this way, so job length is
not the reason. psutil's plain `memory_info()` *does* work here, so this is
Snakemake's choice of the uss/pss-capable call rather than macOS being unable to
report RSS; `io_counters` genuinely does not exist on Darwin. **On Linux - CI, and
Greene - the memory columns fill in**, which is where the `mem_mb` and `threads`
guesses in `screen_archive` are finally checkable against what an archive costs.

**Populated 2026-10-22**, and the data immediately undercut the plan. All 330 forced:
`snakemake-2026-10-22-benchmarks.txt`, 336/336 steps, **1h 46m 49s**, and
`calls.tsv.gz` came back with the **same sha256** (`1eadcaa5...`), so the rescreen
changed nothing but the timing files - the determinism `collect` buys with
`mtime=0` is real.

### What the numbers say, and what they cannot say

**The sampler is free.** One screen job run alone: **36.55 s** by its own
benchmark, 38.6 s by the shell. The same work with no Snakemake at all:
**37.6 s**. So the `benchmark:` directive costs nothing measurable, and the NA
columns are not a sign of overhead.

**But the `s` column counts time the machine was asleep.** The populate run read
1h 46m 49s elapsed. `pmset -g log` for that window:

| | |
|---|---:|
| run elapsed | 1:46:49 |
| **asleep** (first event: `Clamshell Sleep` at 15:42:55, 11 min in, then maintenance-sleep cycles on battery) | **1:30:57** |
| **awake** | **0:15:52** |

The same forced rescreen of the same 330 archives earlier that afternoon took
**15m 11s**. Against 15m 52s of awake time, the pipeline did identical work in
identical time: **there was no slowdown at all.** The lid was closed, and
Snakemake's benchmark measures wall clock (`time.time()` deltas), which keeps
advancing while the system is suspended.

So a benchmark for any job that spanned a sleep boundary is inflated by however
long the machine was out. `11320/q2ebd5918b3` recorded **1180.1 s** and takes
**40.3 s** run alone; `10508/all` recorded 120.7 s against 36.6 s alone. Those
gaps are suspension, not CPU starvation - and the "effective parallelism of
1.13x" that follows from dividing summed job time by elapsed is an artefact of
the same thing, since 7,222 s of job time cannot fit in 952 s of awake machine
unless the jobs' own clocks were running while nothing executed.

**`caffeinate -i` does not survive a closed lid.** That is the command in
`CLAUDE.md`, and it asserts `PreventUserIdleSystemSleep` only - the log shows the
system entering `Clamshell Sleep` straight through it. For a run you intend to
leave alone, keep the lid open, or run it somewhere that does not sleep. A
suspended run is not merely slow: it silently writes timing data that is mostly
measuring the suspension.

**What this leaves of item 2.** The sampler is free and the directive is
harmless, but on this laptop the useful column is wall time, wall time is only
meaningful for a run you know stayed awake, and the contention- and
suspension-immune column (`cpu_time`) is one macOS reports as NA. The benchmarks
currently on disk were written across 91 minutes of sleep and should be treated
as contaminated: re-populate with the lid open before building anything on them,
and cost a single archive by running it alone, as the solo figures above do.

### The clean benchmarks, 2026-10-23, and what they settle

Populated under `caffeinate -dims` with the machine awake throughout: 335 of 335
live archives force-rescreened, **13m 54s elapsed, exit 0**, 335 benchmark files
written inside the run's own window (`snakemake-2026-10-23-benchmarks.txt`).
Summed job time is **25m 10s**, so effective parallelism on 4 cores was **1.81x** -
a real number, where the 1.13x computed from the contaminated set was an artefact
of job clocks running while nothing executed.

**The sleep diagnosis is confirmed to the second.** The two archives the section
above costed solo now read, under contention and awake:

| archive | contaminated | solo (section above) | clean, under contention |
|---|---:|---:|---:|
| `11320/q2ebd5918b3/2026-10-03` | 1180.1 s | 40.3 s | **36.4 s** |
| `10508/all/2026-10-03` | 120.7 s | 36.6 s | **40.4 s** |

So the 2026-10-22 files were measuring the suspension, exactly as diagnosed, and
nothing was wrong with the pipeline. `report.timing_lines` now filters benchmarks
to the run's own window so a contaminated file cannot be ranked again.

### The thread heuristic, FIXED 2026-10-23: the missing variable was the assay count

Both `threads` and `priority` on `screen_archive` now come from predicted work
(`assaywatch.timing.screen_core_seconds`, constants in `config.yaml` under
`screen:`) instead of from gzipped bytes:

    core-seconds ~ 1.47 + 0.1937*(MB x assays) + 1.55e-4*(records x assays)

R2 = 0.952 on the 335 clean benchmarks. The model space, same data, same fit:

| model | R2 |
|---|---:|
| `records x assays` alone | 0.091 |
| gzipped MB alone | 0.827 |
| MB + records | 0.845 |
| MB + records + assays (additive) | 0.849 |
| `MB x assays` alone | 0.944 |
| **`MB x assays` + `records x assays`** | **0.952** |

**The missing variable was never a choice between bytes and records: it was the
number of assays in the group.** An archive is screened against every assay that
asked for its group, so the same records cost three times as much in a group of
three - which is mechanical, not fitted, and lifts R2 from 0.845 to 0.944 on its
own. The record term adds the last 0.008 and is what sizes a record-dense archive
correctly.

So the proposal in the section below was wrong twice over: bytes are the better
single predictor (0.827 against 0.091), *and* the variable that mattered was
neither of them. It is kept below as the record of a hypothesis the measurement
refuted.

What changes, for the jobs that were mis-sized (threads at `--cores 16`):

| archive | MB | records | assays | old | new |
|---|---:|---:|---:|---:|---:|
| `11320/qdf5abd73c1` | 10.1 | 190,101 | 1 | 1 | **2** |
| `11051/q63c5fca5b3` | 27.5 | 59,558 | 3 | 1 | **3** |
| `12059/qbb80900029` | 12.8 | 73,182 | 2 | 1 | **2** |
| `10508/all` | 54.5 | 38,847 | 4 | 2 | **5** |
| `10242/all` | 761.1 | 17,417 | 1 | 16 | **10** |
| `10241/all` | 803.0 | 28,388 | 3 | 16 | 16 |

`priority` moved too, and that is the half that pays locally: it ranked a
52-second archive near the back of the queue because it was 10 MB, so the long
pole was left until last - the exact failure the original comment on that rule
said it existed to prevent.

**One cost, worth recording.** Putting the constants in `config.yaml` meant a new
block in `settings.py`, and `settings.py` is inside `screen.py`'s import closure,
so `_code_hash` changed and all 335 screens were invalidated. That is the trigger
working as designed: a module that *could* change a call must invalidate, whether
or not this one does. `screen.py` never reads the `screen:` block, so the forced
rescreen is expected to reproduce every screen byte for byte -- checksums were
taken beforehand and the comparison is the check. Resizing a job on its own reruns
nothing, because neither `threads` nor `priority` is in the signature.

### MEASURED, and the threads half of this lost

Forcing all 335 archives at `--cores 4`, against the byte rule's 13m 54s:

| | byte rule | cost model, `core_seconds_per_worker: 15` |
|---|---:|---:|
| summed job time | 25.2 min | **27.2 min** (+8%) |
| effective parallelism | 1.81x | **1.47x** |
| elapsed | 13m 54s | **18m 33s** (+33%) |

Both numbers move the same way and **contention cannot explain the first**: a
rise in summed job time is extra real work, not waiting. Each extra worker pays
about 1.5 s of process start-up plus its pickling, and a job holding four cores
stops four jobs holding one each. Snakemake packs single-threaded jobs better
than this model splits them.

So `core_seconds_per_worker` is **100**, measured rather than guessed, and
locally almost every archive is back to one worker. **Confirmed 2026-10-24**: the
forced run of all 335 live archives at 100 took **11m 40s** wall, 29.0 min summed,
2.47x parallelism, every screen byte-identical (`config.yaml` `screen:` has the
three-row table). The figure of about 14 minutes this section predicted was pessimistic. What the cost model keeps is
the two things that cost nothing:

- **`priority`.** The record-dense archives were never short of workers - they
  were running LAST, because priority ranked them by bytes too. A 10 MB archive
  costing 52 s now outranks a 55 MB one costing 15 s, which is the tail fix the
  original comment on that rule claimed to be for.
- **Cluster requests.** `threads` is the sbatch CPU count, and the byte rule
  asked for 16 CPUs for any archive over 400 MB regardless of how many assays
  wanted it. The biggest now ask for 5, 3, 3 and 2.

The lesson is the same one the oligo work produced earlier the same day: the
printed argument for a change is not evidence that the change helps, and the
only way to tell was to run it. Both halves of the heuristic looked equally
well-motivated; one was worth keeping.

### The earlier hypothesis about the thread heuristic, refuted above

The section below proposed sizing workers on record count rather than gzipped
bytes. On the clean data that is backwards. Across all 335 archives:

| predictor of screening seconds | all (n=335) | above the ~1.2 s startup floor (n=66) |
|---|---:|---:|
| gzipped MB | **+0.776** | **+0.753** |
| record count | +0.490 | +0.289 |

Bytes are the better single predictor, and get *more* so once the fixed
process-startup cost is excluded. Replacing bytes with records would have made the
heuristic worse.

What is real is a narrower fault: the worst-sized jobs are **small archives holding
very many short records**, which the byte rule gives one worker.

| archive | s | MB | records | workers |
|---|---:|---:|---:|---:|
| `10241/all/2026-10-03` | 108.6 | 803.0 | 28,388 | 16 |
| `77643/q8c2ce9448f/2026-10-07` | 88.8 | 1496.6 | 1,179 | 16 |
| `11051/q63c5fca5b3/2026-10-03` | 60.5 | 27.5 | 59,558 | **1** |
| `11320/qdf5abd73c1/2026-10-06` | 52.5 | 10.1 | 190,101 | **1** |
| `12059/qbb80900029/2026-10-03` | 43.6 | 12.8 | 73,182 | **1** |
| `11320/q2ebd5918b3/2026-10-03` | 36.4 | 5.8 | 182,556 | **1** |

Four of the ten slowest jobs run single-threaded, while a 1.5 GB archive holding
1,179 records gets 16 workers for 89 s of work and takes cores from the queue. So
the fix is not to swap the predictor but to take the maximum of a byte term and a
record term, and to stop over-provisioning the few huge, record-sparse archives.
*(Implemented later the same day, once the assay-count term was found; see the
FIXED section above. The recommendation in this paragraph - take the maximum of a
byte term and a record term - is not what shipped: a product term on the assay
count fits far better than a maximum of two independent terms.)*

### The earlier note on the thread heuristic (kept; its hypothesis is corrected above)

`threads` and `priority` are both `archive_mb(input)`-derived
(`SCREEN_MB_PER_THREAD = 25`), and cost does not track bytes:
`11320/q2ebd5918b3` is **6 MB** and holds **165,492** records, so it gets
`6 // 25 -> max(1, 0) = 1` worker and the lowest priority in the queue, while a
52 MB archive gets 2. Solo, the 6 MB archive costs about as much as the 52 MB one
(40.3 s at 1 worker vs 36.6 s at 2). Sizing on record count rather than gzipped
bytes is the obvious next move, and it is now measurable - but measure it solo,
per the section above.

## What went wrong
- I could not give a trustworthy time-to-finish at any point. Retrieval stalled for hours
  on the low-GC PANPOX group (24,014 records, ~756 MB) and the log gave no way to tell
  slow from stuck except watching archive size by hand.
- Snakemake's "N of 249 steps (X%)" counts every job equally, so it says nothing
  about time remaining: quick jobs and the heavy PANPOX screens weigh the same.
- No wall-clock timestamps on stage boundaries. Retrieval end (checkpoint written 23:57)
  was only recoverable from a file mtime.
- Process inspection (pgrep/ps) failed in the sandbox (sysmond error), so liveness had
  to be inferred from log mtime.

## Proposed markers
1. Stage banners with ISO timestamps: run start, retrieval start/end, screening start/end,
   report start/end, written to the log and to a small run manifest JSON.
2. Per-rule start/end times: add Snakemake `benchmark:` to retrieve and screen_archive
   rules (wall time, max RSS) so past runs give real per-group durations.
3. Retrieval progress lines per group: records fetched / available, MB, rate, elapsed,
   written every N pages, not only at group completion.
4. Heartbeat file (e.g. .tmp/run-<stem>.heartbeat) rewritten every ~60 s with timestamp,
   current rule/group and counters, so liveness does not depend on pgrep.
5. Weighted ETA: record each archive's size/record count and the per-record screening
   rate from the previous run's benchmarks, and report ETA as remaining weighted work,
   not remaining steps.
6. Stuck detector: warn if a group's archive has not grown for N minutes.
7. Final summary: total wall time per stage and the top 10 slowest groups, appended to
   the report footer.

## Notes
- Implementing this touches Snakefile/screening code, so do it between runs, not during one.
- Benchmarks from the 2026-10-17 run (if kept) can seed the first weighted ETA.

## Bug found 2026-10-18 (FIXED 2026-10-21): RUN_DATE recomputed mid-run crosses midnight
The 2026-10-17 run started 22:49 but `collect_calls` executed at 00:18 the next
day. `RUN_DATE = config.get("run_date") or date.today()` (Snakefile:49) is
evaluated fresh per Snakemake process, so Snakemake wrote
`results/2026-10-18/calls.tsv.gz` while the run's actual targets
(`results/2026-10-17/report.html`, `.../degeneracy.tsv`) stayed pinned to the
17th. Result: `collect_calls` succeeded but tripped a MissingOutputException
against the stale target, and `report`/`degeneracy_table` never ran even though
every screen (246/246) was already cached and correct.

Fix: pin RUN_DATE once at the top of the Snakefile invocation (e.g. write it to
a small marker file on first job, or require `--config run_date=...` for any
run expected to cross midnight) rather than recomputing `date.today()` live.
This is the same root cause the timekeeping markers above are meant to fix —
a stage-start timestamp captured once, not re-derived per process.

Recovery used this time: `results/2026-10-18/calls.tsv.gz` has the right data
(2.73M rows, well-formed); rerun with `--config run_date=2026-10-17` after
moving/symlinking the file, so only `report` + `degeneracy_table` re-execute.
