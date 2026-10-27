#!/bin/bash
# The weekly re-screen, for a scheduler. DRY RUN UNLESS --live IS PASSED.
#
# README.md and CITATION.cff both say this project "re-screens it on a schedule".
# Until 2026-10-23 there was no schedule: every run was a human typing
# `caffeinate -i snakemake` with the lid open, and scripts/report_diff.py was
# written for "the weekly run's summary" on a job that did not exist. The commit
# log shows the result -- bursts on 10-03/04/05, then 10-14, 10-18, 10-20, 10-22.
#
#   scripts/weekly_run.sh                 # dry run: prints the job plan, fetches nothing
#   scripts/weekly_run.sh --live          # the real run
#   scripts/weekly_run.sh --live --cores 8
#
# WHY DRY RUN IS THE DEFAULT. A live run reaches eutils.ncbi.nlm.nih.gov and
# api.ncbi.nlm.nih.gov, needs a contact address and an API key, and writes
# gigabytes to data/retrieved/ that are NOT reproducible on request (retrieval is
# incremental by mdat, so each archive is the set of records that changed since
# the last run). A scheduler that starts doing that because a script was
# installed is a scheduler doing something nobody agreed to. Install the job,
# watch a dry run fire, then add --live.
set -euo pipefail

CORES=4
LIVE=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --live) LIVE=1; shift ;;
    --cores) CORES="$2"; shift 2 ;;
    -h|--help) sed -n '2,30p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

cd "$(dirname "$0")/.."
REPO="$PWD"
LOGDIR="$REPO/results/weekly-logs"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/$(date +%Y-%m-%d-%H%M).log"

# launchd gives a process almost no environment: no conda, often no PATH beyond
# /usr/bin. `conda run` is how the pre-commit hooks already invoke this env, so
# it is the one mechanism that works in both places.
CONDA="${CONDA_EXE:-/opt/homebrew/Caskroom/miniforge/base/bin/conda}"
if [[ ! -x "$CONDA" ]]; then
  echo "no conda at $CONDA; set CONDA_EXE" | tee -a "$LOG" >&2
  exit 1
fi
RUN=("$CONDA" run --no-capture-output -n assaywatch)

{
  echo "=== $(date -Iseconds) weekly run, live=$LIVE, cores=$CORES ==="

  # The contact address NCBI requires. Read from the same place the pipeline
  # does rather than being written into a scheduled job.
  EMAIL=""
  if [[ -f "$REPO/.secrets/email" ]]; then EMAIL="$(tr -d '[:space:]' < "$REPO/.secrets/email")"; fi

  if [[ "$LIVE" -eq 0 ]]; then
    echo "--- DRY RUN (no fetch, no screen; pass --live to run for real) ---"
    "${RUN[@]}" snakemake -n --cores "$CORES" ${EMAIL:+--config email="$EMAIL"}
    echo "--- dry run finished; nothing was fetched or written ---"
    exit 0
  fi

  if [[ -z "$EMAIL" ]]; then
    echo "refusing a live run with no contact address: write one to .secrets/email" >&2
    exit 1
  fi
  "${RUN[@]}" python -m assaywatch.credentials

  # `caffeinate -i` asserts PreventUserIdleSystemSleep, which does NOT stop
  # clamshell sleep: a 2026-10-22 run spent 1h31m of 1h47m asleep with the lid
  # shut. Nothing here can fix that; the install note says to leave the lid open.
  # --rerun-incomplete, which profiles/slurm/config.yaml has always set and this
  # path did not. Combined with a kill mid-job (the clamshell sleep above, or a
  # power loss), Snakemake leaves its incomplete-output marker and the NEXT
  # scheduled run aborts with "Incomplete files exist" instead of resuming --
  # into results/weekly-logs/launchd.err, which nobody reads. So one interrupted
  # Sunday silently cost every Sunday after it.
  caffeinate -i "${RUN[@]}" snakemake --cores "$CORES" --rerun-incomplete --config email="$EMAIL"

  # What changed, if anything. --quiet prints nothing on a quiet week, which is
  # what this script was written for.
  echo "--- what changed since the previous run ---"
  "${RUN[@]}" python scripts/report_diff.py --quiet || true
  echo "=== $(date -Iseconds) done ==="
} 2>&1 | tee -a "$LOG"
