# Running the re-screen on a schedule (macOS)

`README.md` and `CITATION.cff` both say AssayWatch "re-screens it on a schedule".
Until 2026-10-23 there was no schedule: every run was a human typing
`caffeinate -i snakemake` with the lid open, and `scripts/report_diff.py` was written
for "the weekly run's summary" on a job that did not exist. The commit log shows what
that produces — bursts on 2026-10-03/04/05, then 10-14, 10-18, 10-20, 10-22.

## Why launchd and not GitHub Actions

Retrieval needs `eutils.ncbi.nlm.nih.gov` and `api.ncbi.nlm.nih.gov`, and `CLAUDE.md`
records that cloud sandboxes have been blocked from them. A scheduled Action could run
the tests and the validator but not the part that makes the report new, so the schedule
has to live on a machine that can reach NCBI.

## Install

```bash
mkdir -p results/weekly-logs
sed "s|REPO_PATH|$PWD|g" profiles/launchd/com.assaywatch.weekly.plist \
  > ~/Library/LaunchAgents/com.assaywatch.weekly.plist
launchctl load ~/Library/LaunchAgents/com.assaywatch.weekly.plist

# fire it once now, without waiting for Sunday, to see it work
launchctl start com.assaywatch.weekly
tail -f results/weekly-logs/*.log
```

**As installed it is a dry run.** It prints the job plan and fetches nothing. Once a dry
run has fired and the log looks right, add `--live`:

```xml
<key>ProgramArguments</key>
<array>
  <string>REPO_PATH/scripts/weekly_run.sh</string>
  <string>--live</string>
</array>
```

then `launchctl unload` and `load` again. A live run needs a contact address in
`.secrets/email` and refuses to start without one; it checks the NCBI key through
`assaywatch credentials` before fetching.

## What it does

1. `conda run -n assaywatch` — launchd gives a process almost no environment, and this
   is the same mechanism the pre-commit hooks already use.
2. `caffeinate -i snakemake --cores 4 --config email=...`.
3. `scripts/report_diff.py --quiet`, which prints nothing on a quiet week.

Everything is tee'd to `results/weekly-logs/<timestamp>.log` (gitignored with the rest
of `results/`).

## Leave the lid open

`caffeinate -i` asserts `PreventUserIdleSystemSleep`, which does **not** stop clamshell
sleep. A 2026-10-22 run was suspended eleven minutes in and spent 1h31m of its 1h47m
asleep, doing its real work around the gaps — the run completed correctly but every
`benchmark:` wall time measured the closed lid. The job is scheduled for Sunday 09:00
rather than overnight for this reason: it is a slot a person can leave the lid open for.
A machine that does not sleep is better still.

## Uninstall

```bash
launchctl unload ~/Library/LaunchAgents/com.assaywatch.weekly.plist
rm ~/Library/LaunchAgents/com.assaywatch.weekly.plist
```

## Not installed by this repository

Nothing here installs itself. A scheduled job that reaches an external API and writes
gigabytes is something a person opts into, on a machine they chose, which is also why
the default is a dry run.
