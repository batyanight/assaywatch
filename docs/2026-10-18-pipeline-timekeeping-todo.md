# TODO before the next full run: better timekeeping markers

Written 2026-10-18 during the 2026-10-17 full run.

**Status, re-checked 2026-10-22: most of this shipped. Items 2 and 7 are what is
left.** The line that used to stand here - "Nothing here has been implemented" -
was true when written and stale for days afterwards. Per item:

| # | item | state |
|---|---|---|
| 1 | stage banners + run manifest JSON | **done** - `RunManifest` writes stage wall times to `results/<date>/run-timing.json`, and `onstart` prints the run banner (`Snakefile:244-281`) |
| 2 | per-rule `benchmark:` (wall time, max RSS) | **done 2026-10-22** for `retrieve` and `screen_archive`, with one caveat below: on macOS only the wall-time columns fill in |
| 3 | retrieval/screening progress lines | **done** - `screening_progress(RETRIEVED, SCREENED)` feeds the heartbeat from bytes screened, not step count |
| 4 | heartbeat file | **done** - `.tmp/heartbeat-<date>.json`, `heartbeat_seconds` configurable (default 60) |
| 5 | weighted ETA | **done** - `timing.weighted_eta`, projected from bytes rather than remaining steps |
| 6 | stuck detector | **done** - `heartbeat(stall_after=...)`, `stall_seconds` configurable (default 900) |
| 7 | final per-stage summary + top 10 slowest groups in the report footer | **OPEN** - the only column that fills in on macOS is wall time, and it counts machine sleep (measured below), so a slowest-groups table needs either a run known to have stayed awake or `cpu_time`, which reads NA here |

**Item 7 is the only one left.** Read "What the numbers say" below before
building it: the benchmarks on disk were written across 91 minutes of laptop
sleep. The RUN_DATE bug
recorded at the bottom of this file is **fixed** (`timing.resolve_run_date` +
`write_run_marker`, `Snakefile:79`); it is kept below as the record of why.

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

### A real finding about the thread heuristic

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
