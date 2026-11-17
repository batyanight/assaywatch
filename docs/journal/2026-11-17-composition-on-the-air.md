# Composition does not fit on the Air: killed at 6.6 GB, and two launch mistakes on the way

2026-11-17, step 1 of spec #28 (every routine run on the Air). The question was whether
`composition` peaks at 4.8 GB or less on the Air, so that it could be declared at
`mem_mb=5500` and the whole run move there. It does not. The 2026-11-15 run was finished
on the Mac instead, by the split run in `docs/running-the-pipeline.md`.

## The result

- **`composition` was killed by the kernel's OOM killer at 12:49 PM**, 53 minutes in, at
  6,613,088 kB anonymous resident memory (`journalctl -k`: "Out of memory: Killed process
  ... (assaywatch) total-vm:10277816kB, anon-rss:6613088kB"). The sampler, every 5 s on
  the largest `assaywatch composition` process, last saw 6.45 GB at 12:44 PM. The true peak
  is higher than 6.6 GB and unknown, since the process never finished.
- Spec #28's threshold was 4.8 GB. This is over it, so by decision 4 the next step is to
  reduce `composition`'s memory, starting with the record-id set passed to
  `read_collection_years`. The Air keeps `omit-from composition` until then.
- SLURM on the Air does not enforce memory, so the 5,500 MB request only let the job
  start. The kernel ended it: 7.3 GB of RAM and the 4 GB swap file were not enough with
  the machine otherwise idle.
- The 2026-11-10 run's "5.1 GB peak observed" on the Mac does not predict the Air. The
  data differs (this run screened 181 archives, the first full set the Air has made), and
  that figure was never a benchmark.
- **The reference warm-up fits.** `composition --references prefetch` on the 2026-11-15
  calls took 2 min 40 s at a 3.6 GB peak (`/usr/bin/time -v`: 3,600,764 kB), exit 0.

The measurement ran on the 2026-11-17 data, not 2026-11-15's (see the first mistake).
The two are a similar size: 2026-11-17 was an incremental fetch of 331 MB on top of the
same history.

## Mistake 1: the run date was no longer pinned

The plan was to finish the 2026-11-15 run on the Air with its last three rules. The
launch script ran `snakemake --profile profiles/slurm-air` with no `run_date`, after the
Air half of 2026-11-15 had ended with `status: success`. The run date stays pinned only
until a run succeeds, so this call pinned a new date, 2026-11-17, and started a whole new
run: `retrieve` (71 new archive files, 331 MB of FASTA, `data/retrieved/runs/2026-11-17.json`
and the manifest advanced), screening, `collect_calls`, `refseq_twins`, and then
`composition` on that run's calls.

Nothing was corrupted: the 2026-11-17 archives are a real incremental fetch, and the
2026-11-15 folder was not touched. But 2026-11-17 is now a failed, pinned run, and the
next Snakemake call on the Air will resume it. The fix is the one the Mac half already
uses: name the date, `--config run_date=2026-11-15`.

## Mistake 2: `--set-resources` on the command line replaced the profile's

The launch passed `--set-resources composition:mem_mb=5500` on the command line. That
replaced the Air profile's whole `set-resources` block instead of adding to it, so
`figures` and `site_drift` fell back to the Snakefile's 6000 MB and `sbatch` refused them:
"Memory specification can not be satisfied". For spec #28's weekly script this means a
per-rule override belongs in the profile, never on the command line.

## Found on the way

- **The Mac-half command in `docs/running-the-pipeline.md` does nothing on Snakemake
  9.27.** With `--allowed-rules composition lineage_analysis report` and no targets, the
  dry run reports "Nothing to be done", although `report.html` and `lineage.md` are
  missing. Naming them as targets plans exactly the three rules. Probably `--allowed-rules`
  also excludes `rule all`; not checked further.
- **Earlier the same day, `figures` and `site_drift` failed on the Air** because
  `asm` archives carry no taxid column and the Air had no taxid backfill sidecar. The
  Mac's sidecar was copied over (SHA-256 matched) to finish the Air half. Ticket #30.

## Finishing 2026-11-15 on the Mac

The Air's `data/retrieved/` and `results/` were copied to `data/retrieved-air/` and
`results-air/`, leaving out everything dated 2026-11-17, with the backfill sidecar and the
reference cache the Air had warmed. Started 1:24 PM:

    snakemake results-air/2026-11-15/report.html results-air/2026-11-15/lineage.md --cores 4 \
      --allowed-rules composition lineage_analysis report \
      --config run_date=2026-11-15 retrieved_dir=data/retrieved-air results_dir=results-air email=...

Finished 3:31 PM, 3 of 3 steps: `composition.json`, `composition.tsv`, `lineage.md`,
`report.html` and `report.md` in `results-air/2026-11-15/`. No `references-missing.txt`
was written, so the cache warmed on the Air covered every spike batch.

- `composition` ran 1:23 PM to 3:26 PM (2 h 3 min); `lineage_analysis` and `report`
  took 5 minutes after it.
- `/usr/bin/time -l` on the whole Snakemake call: 7,645 s real, 7,602 s user, and a
  **maximum resident set size of 10,646,175,744 bytes (9.9 GiB)**. The figure is the
  largest single descendant, which is `composition`. User time close to real time says
  the run was not paused for long, if at all, while the lid was closed for the commute.

So on the same data size, `composition` needs about 9.9 GiB on the Mac. Against that, the
Air's 6.6 GB kill point is no surprise, and the 2026-11-10 "5.1 GB observed" was an
underestimate or a smaller run. The 13000 MB declaration in the Snakefile still holds;
the 4.8 GB target for the Air is roughly half of what the stage uses today.
