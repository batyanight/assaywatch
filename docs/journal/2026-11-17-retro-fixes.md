# The split run's launch mistakes are now guarded, and the documented Mac half planned nothing

2026-11-17, items 1 to 4 of that day's retro on the composition session
(`docs/journal/2026-11-17-composition-on-the-air.md`). No run was made; everything
here was checked on the test pipeline in `tests/test_triggers.py`.

## A new run date over an unfinished run is refused

The run date stays pinned only until a run succeeds, and the Air half of a split run
(`--omit-from composition`) succeeds without writing `report.html`. So a launch with
no `run_date` after it pins a new date and runs a whole new run, which is how
2026-11-17 started on the Air.

The Snakefile now asks `timing.unfinished_run(RESULTS, RUN_DATE)` before it lets a
launch pin a new date. That returns the latest folder under `results/` named exactly
as a date and earlier than the new one, if it has no `report.html`. If there is one,
the launch stops (a dry run too), names the folder, and says to pass either
`run_date=<that date>` to finish it or `new_run=1` to start a new run anyway. A named
`run_date` and a resumed pin skip the check. Hand-named copies such as
`2026-10-28.partial-stopped` are not runs, and only the latest earlier run counts: the
Mac's `results/` has older folders without a report (2026-10-11, 2026-10-23) and its
latest, 2026-11-10, has one, so the Mac's next run is not blocked.

On the Air, 2026-11-17 is pinned as a failed run. Until the pin ages out (48 hours
from its start) a launch there resumes 2026-11-17 and the check does not apply. After
that, a launch with no `run_date` is refused, because `results/2026-11-17/` has no
report; 2026-11-15 there has none either, since its report was built on the Mac. The
choice then is to finish 2026-11-17 by name or to start fresh with `new_run=1`.

The check cannot tell a split run waiting for its second half from a run that failed,
and its message says both. That matters for `scripts/weekly_run.sh`, which launches
with no `run_date`: after a failed run whose pin has aged out, every weekly launch now
stops at parse time until someone finishes the run or passes `new_run=1`. Before, it
started a new run and left the failed folder behind. Spec #28's rewrite of the script
has to decide which it wants; ROADMAP says so.

The `slow` test plants an earlier run folder without a report and checks that a dry
run is refused, that `new_run=1` lets it through, and that a named `run_date` needs no
flag. It failed against the Snakefile before the change.

## The documented Mac half planned nothing

The guide's command, `snakemake -n --cores 4 --allowed-rules composition
lineage_analysis report --config ...`, says "Nothing to be done" on Snakemake 9.27.1
with `composition`'s outputs, `lineage.md` and the report missing. Naming
`RESULTS/RUN_DATE/report.html` and `RESULTS/RUN_DATE/lineage.md` before `--config`
plans exactly the three rules. A `slow` test now runs both forms, with the guide's
`retrieved_dir=data/retrieved-air results_dir=results-air`, on a copy of the test
pipeline renamed to those folders, with no `.snakemake/` (the Mac holds no metadata for
the Air's files) and with those outputs removed: the corrected one plans `composition`,
`lineage_analysis` and `report`, the old one plans nothing. Why `--allowed-rules`
drops `rule all` was not looked into.

## The rest

- `profiles/slurm-air/config.yaml` and the running guide say per-rule resource
  overrides go in the profile, never in `--set-resources` on the command line, which
  replaces the profile's whole block.
- `rule composition` writes `results/benchmarks/composition/<run date>.tsv` (under
  `results_dir`, like the other benchmarks), so the next run on the Air records its
  peak. On the Mac the memory columns read NA, as for every benchmark there. `results/*`
  in `.gitignore` already covers it.
