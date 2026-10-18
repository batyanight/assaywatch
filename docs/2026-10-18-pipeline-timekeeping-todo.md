# TODO before the next full run: better timekeeping markers

Written 2026-10-18 during the 2026-10-17 full run. Nothing here has been implemented.

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

## Bug found 2026-10-18: RUN_DATE recomputed mid-run crosses midnight
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
