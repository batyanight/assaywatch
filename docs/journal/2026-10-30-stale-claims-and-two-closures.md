# Five stale claims, two closures, and what a summary line cost

2026-10-30, later the same day as `2026-10-30-decisions-round-2.md`. No new capability;
this is the record of what that day's documents got wrong and two questions taken off the
open list.

## The expensive one: a progress line that averaged

`scripts/backfill_collection_dates.py` printed `rate = n / (now - started)`, a cumulative
mean, and called it a rate. This fetch opens slowly while NCBI works off whatever load
preceded it and then recovers, so the slow opening dominates the figure for tens of
thousands of records.

The consequence was not cosmetic. A run that had climbed to **69 records/sec with 4.5
hours left**, and had taken **no retry in 110,000 records**, printed `0.8-1.0 rec/s` and
`eta 424 h` in its first four lines. It was stopped on that reading, reported to the
maintainer as NCBI throttling the key, and a plan was written around a throttle that did
not exist. The earlier "decay from 78 to 11 records/sec" in the first run was the same
artifact in reverse: a mean dragged by one slow patch, not a falling rate.

The retry and split counters added to diagnose it were correct and were read wrongly --
over the first 400 records rather than the whole run, where they sat frozen at 38 and 10.

**The lesson worth keeping**: an instrument that answers "how long has this taken" cannot
answer "how long is left", and a figure that is monotonically recovering looks exactly like
one that is degrading if you only read its first lines. The line now prints a 120-second
window and the average side by side.

## Two bugs the summary line hid

- **`newest_run()` sorted lexicographically.** `'b' > '2'`, so
  `results/baseline-2026-10-22` sorted after `results/2026-10-27` and the whole backfill
  worked a five-day-old run's accession list. Most accessions overlap, so the sidecar is not
  wasted, but ~3,700 records present only in the current run would never have been asked
  for and the lens would have counted them undatable.
- **425 record ids are not accessions.** Shaped `pdb|29TK|N`; no flatfile answers for them.
  Settled unasked.

## Three stale figures

| Claim | Was | Is |
|---|---|---|
| backfill throughput | ~150 records/sec sustained | never measured sustained; see above |
| `needs_review` flags | 216 on 207 of 209 entries (2026-10-27) | **227 on 154 of 214** |
| twelve set-2 row cells | "(PROPOSED, awaiting sign-off)" | signed off 2026-10-30 |

The flag count is worth a note on method: on 2026-10-30, `grep -c 'flag:'` counted 228
flags and an inventory pass reported a different entry count again. The loader says 227 on
154, and the loader is what the validator and the report read. **Take a registry count from `registry.load_one`, not from a pattern.** Also
recorded, because it wasted a count tonight: `rg` on this machine returned 0 for a pattern
where `grep` returned 425, so numbers here come from `grep` or the loader.

## Two closures

**`drift.window_on` is closed.** It survived as a standing item in four `RESUME-HERE.md`
Next lists while appearing nowhere in `ROADMAP.md` or `config.yaml`. The verdict always
runs on deposit date; collection year is reported beside it as a lens that moves no status.
The reason is worth keeping: a verdict that moved with a metadata field a quarter of
records lack would be less trustworthy, not more.

**`drift.anchor_fdr: 0.001` is closed as a stated placeholder**, not carried as debt. No
bench panel can ever bear on it, and that is provable rather than a matter of effort: it
relabels rows between `no_site` and `fail`, and a bench row records band or no band, where
those are the same answer. Tier-2 separates 0.01 from 0.001 on one row. A mechanism
argument, one cross-check and one tier-2 row is the honest status, and no instrument short
of a new held-out corpus could improve it.

## The matrix rule, rejected

Recorded here because `RESUME-HERE.md` still listed it as the maintainer's open call:
scoring a pan-family `works` against `low coverage` as agreement is **rejected**. It would
declare a real disagreement to be agreement, by a rule proposed after seeing which rows it
rescued. The mismatch is between a paper's CLAIM and its EVIDENCE, and it is fixed with the
34 `scope_taxid` reads instead.
