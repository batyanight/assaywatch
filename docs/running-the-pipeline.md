# Running the pipeline

Moved out of `README.md` on 2026-10-31, unchanged, when the README was cut to a
front page. Setup is in [`installation.md`](installation.md); the stage-by-stage
design is in [`pipeline-architecture.md`](pipeline-architecture.md). This is the
operational half: what to run, what grows on disk, how retrieval groups work, and
how to run it on a cluster.

## Running the pipeline

```bash
caffeinate -i snakemake --cores 4 --config email=you@example.org
```

On a schedule, which is what "re-screens it on a schedule" above means:

```bash
scripts/weekly_run.sh            # dry run: prints the job plan, fetches nothing
scripts/weekly_run.sh --live     # the real run, then report_diff for what changed
```

`profiles/launchd/` installs that weekly on macOS and `profiles/launchd/README.md`
explains why it is not a GitHub Action (NCBI is unreachable from cloud sandboxes) and
why the installed job is a dry run until you add `--live`. Each report prints when the
previous successful run finished, so a stale one says so.

Five stages: validate the registry, retrieve what is new for each group,
screen every archive not yet screened, collect, report. `caffeinate -i` keeps a
Mac from idle-sleeping until the run ends.

**Keep the lid open.** `caffeinate -i` asserts `PreventUserIdleSystemSleep`, and
closing the lid is not idle sleep: a 2026-10-22 run was suspended by
`Clamshell Sleep` eleven minutes in and spent 1h 31m of its 1h 47m asleep, doing
its 15 minutes of real work around the gaps. The run completes correctly, but
`benchmark:` wall times (and the heartbeat's elapsed) count the suspension, so
the timing data is mostly measuring the closed lid. Leave the lid open, or run it
somewhere that does not sleep.

**Big archives go first and get more cores.** Each screen job takes one worker
per `screen_mb_per_thread` (default 25) gzipped MB, capped by `--cores`, and
its priority is its size, so the largest archive starts first instead of
running alone on one core after everything else has finished.

**Cached screens are redone when they would change.** Each screen job carries
a signature of its group's assay files, the scoring settings in config.yaml and
the screening code. Edit an assay, change a threshold or update the matcher, and
the next run rescreens exactly the archives affected; nothing to force by hand.

**Reports are cumulative.** Every archive ever fetched is screened once and the
result is cached under `results/screened/<taxid>/<group>/<archive>.tsv`. Each
report is built from all of those, with the newest version of each accession
winning, so a group with nothing new this week is still in the report and next
week only the new archives cost anything. `--config run_date=...` only renames
the report folder.

**A calls table says what produced it**, in `results/<date>/calls.provenance.json`:
every screen that went into it with the time it was written, its rows and its
assay count, plus the screening code-and-config hash, the git commit and the
signature the pipeline expects for each group. Because reports are cumulative,
the table is a mosaic — a run mixes archives screened tonight with archives
screened three weeks ago under whatever the config said then — so the sidecar
records per-archive facts and the span of screening times rather than claiming
one set of settings for the whole table. It exists because
`results/2026-10-18/calls.tsv.gz` turned out to have been screened under a
scoring override that was reverted the next day, and the only way anyone
established that was to notice a commit landing three minutes after the run
finished. A cached screen still carries no record of its own settings; the
sidecar makes the gap visible rather than closing it.

**State is kept apart from outputs.** Snakemake deletes a rule's declared
outputs before it runs the rule. The retrieval manifest and the sequence
archives must outlive any one run, so neither is ever declared as an output:
`retrieve`'s output is a small per-day run record in `data/retrieved/runs/`,
and the manifest beside it is state the retrieve code manages itself, written
atomically. Archives are never overwritten either: a second run on the same day
writes `<date>_2.fasta.gz`. If the manifest is ever lost or damaged,
`python scripts/rebuild_manifest.py` rebuilds it from the archives on disk.
Retrieval and the rebuild take an exclusive lock on `data/retrieved/.lock` for
as long as they run, so a second run started meanwhile stops with a message
rather than racing on the manifest (dry runs need no lock).

`retrieve` is a Snakemake **checkpoint**: which archives exist is not known
until it has run, so the job graph is re-evaluated after it finishes and the
screening jobs are created from what is actually on disk.

### What grows on disk, and what is safe to delete

```bash
python scripts/storage_report.py          # measures; deletes nothing, ever
```

Keeping every archive is what makes a past report reproducible, so
`data/retrieved/` only grows — 9.1 GB across 134 groups on 2026-10-30, against
491 MB of cached screens and 236 MB of reports. Run the script rather than
trusting these figures; they are a measurement with a date, not a property. The
instinct when that fills a disk is to delete the biggest thing, and here the
biggest thing is the only thing that cannot be recovered:

| | 2026-10-30 | recoverable? |
|---|---|---|
| `data/retrieved/*.fasta.gz` | 9.1 GB | **no** — retrieval is incremental (`datetype=mdat`), so each archive is the set of records that changed since the previous run, which NCBI will not reproduce on request; records are also revised and withdrawn |
| `data/retrieved/*.meta.tsv.gz` | 22 MB | **no**, and it carries the deposit dates the whole drift statistic is indexed on — 0.2% of the volume for the most irreplaceable part of it |
| `results/screened/` | 491 MB | yes, deterministically, ~54 min on 10 cores |
| `results/<date>/` | 236 MB over 23 runs | yes, minutes, from the screens |

So the order that loses least is: old reports, then the screen cache, then —
only after deciding their records are not wanted again — **orphaned groups**.
A group is a (taxid, query) pair taken from the registry; re-scope a query or
retire an assay and its archives stay on disk, screened by nothing and reported
in nothing. There are 6, holding 608 MB, and the report says for each how much
of it the live groups still hold (`1387563/all` is 506 MB of which 6,856
accessions appear in no live group). Deleting one is reversible only in the
sense that re-scoping brings the group back — not the deposits that have
changed or gone meanwhile.

The report also measures **cross-group duplication**, which is the archive
format working as designed rather than a fault: archives are stored per group,
while a record belongs to every group whose query matches it. On gene-sized
records that is cheap; on the Mycobacterium complex it is not — `77643`'s two
query groups share 822 whole-genome accessions, about 253 MB, and
`1387563/qdb308affab` is wholly contained in the orphaned `1387563/all`.
Fixing it properly means storing each record once and having groups reference
it, which is an archive format change, so for now it is reported rather than
repaired.

### Retrieval groups and gene-targeted queries

A retrieval group is a (taxid, query) pair, and the archive lives at
`data/retrieved/<taxid>/<group>/<date>.fasta.gz` — `all` when the whole taxon
is fetched, a short hash of the query otherwise. The query is the assay's own
`target.query`, an Entrez term ANDed onto the taxon:

```yaml
target:
  taxid: 28901
  taxon_name: Salmonella enterica
  query: invA[Gene] OR "invasion protein"[Title] OR invA[Title]
```

Without it the group is the whole taxon, which is right for Bd (nine thousand
records) and absurd for E. coli (sixteen million, almost all whole-genome
shotgun contigs). The 44 assays on taxa too large to fetch whole carry a query
set in their own entry's `target.query`; the terms OR together gene
names, title phrases and `"complete genome"[Title]` because annotation is
inconsistent and a complete genome always carries the locus. A record the
query misses is a record the assay is not judged against — a coverage cost,
not a scoring error — and `--dry-run` reports each group's count so the
query can be widened or narrowed before anything is fetched.

Each group is then screened only against the assays that asked for it
(`screen --only`), so a gene-targeted archive is never diluted with another
gene's `no_amplicon` rows. SARS-CoV-2 is excluded from the pan-coronavirus
groups by a `NOT txid2697049` clause: nine million near-identical surveillance
records would swamp a wildlife statistic. The clause is one line to remove.

### Assembly-level retrieval for bacteria

For enteric bacteria the gene-level nuccore deposits stop around 2012: since
then invA, ipaH, LT and the rest arrive inside whole-genome assemblies, which
the gene queries exclude. Taxids listed under `assemblies.taxa` in config.yaml
(E. coli, Shigella, Salmonella, both Yersinia, Leptospira) therefore get a
second group, `asm`, filled from NCBI Datasets (`assaywatch/assemblies.py`):

* GenBank complete genomes and chromosomes, listed from the compact TSV genome
  report (release-date windows are halved until each fits in one page, since
  that endpoint has no continuation token);
* at most `per_year` (default 20) per release year, in SHA-1-of-accession order,
  which is arbitrary with respect to biology and stable, so reruns pick the same
  genomes and incremental runs only top up short years;
* each genome cut down, in memory, to the windows where one of the taxon's
  assays could form an amplicon distinguishable from chance (see below), joined
  by N spacers longer than any amplicon. One record per assembly, id = the
  assembly accession, `created` = its release date; the BioSample collection
  date is kept in the title.

On *Y. pseudotuberculosis* (41 complete genomes) that is 76 seconds and a 4 kB
archive: one 440 bp Wang 1997 amplicon per genome, all `detect`. The first full
sample across the six taxa is about 1,100 genomes.

### Chance primer pairs

The six-mismatch search budget is generous so that a drifted site is still
found and scored. On a long record that has a cost: an 18-mer has a site within
six mismatches every few kilobases of random sequence, so a 5 Mb genome holds
hundreds of facing primer pairs in amplicon range. Every amplicon therefore
carries a `pair_evalue` (`assaywatch/chance.py`): the expected number of pairs
at least as good in a random record of the same length and base composition.
A perfect pair in a genome is around 1e-11; six-and-six in a genome is around
1600; five-and-five in a 1 kb gene record is around 0.002.

Assembly extraction always uses it (`assemblies.max_pair_evalue`, 0.01).
Scoring uses it too (`scoring.max_pair_evalue: 0.01`, set 2026-10-04): a pair
above the threshold is `no_amplicon`, not `fail`. In the first full run a
quarter of all `fail` calls had both primers at five or more mismatches, and
for the herpesvirus, adenovirus and lyssavirus assays their amplicon lengths
matched no `detect` at all. Turning the guard on moved 114,093 `fail` calls to
`no_amplicon` and only 5 `reduced` ones. Set it to `null` to report the
E-value without acting on it.

### Retrieval decisions

These shape what the drift metric can see, so they sit in `config.yaml` rather
than in code:

| setting | default | why |
|---|---|---|
| `min_length` | 100 | a fragment shorter than any amplicon can only produce `no_amplicon` noise |
| `max_records_per_taxon` | 100000 | influenza A alone is over a million records and would dominate a weekly run |
| `large_taxa_allowed` | `[11320]` | taxa past the cap are opted in by taxid, deliberately, one at a time (influenza A segment 7, accepted 2026-10-03) |
| `incremental_overlap_days` | 3 | each incremental run re-asks for the last few days, for records NCBI indexes late |
| `query_suffix` | none | a global term ANDed onto every group, e.g. `NOT "whole genome shotgun"[Title]` |

A group over the cap is skipped and logged; the run continues and exits zero,
so one oversized taxon never blocks the weekly report. `--strict` makes a skip
fatal for the cases where that is wanted.

Runs are **incremental by default**. The manifest records the date of the last
successful run per taxon and the next run asks only for records added or
modified since, using `datetype=mdat` rather than `pdat`: a submitter revising
a sequence can turn a mismatch into a match, so revisions matter as much as new
deposits. `--full` ignores the manifest, which is what you want after changing
the length filter or the query.

Each run writes `data/retrieved/<taxid>/<group>/<date>.fasta.gz` plus a
`.meta.tsv.gz` carrying accession, creation date, update date, length and
title. The dates are the point: the drift question is whether coverage has
fallen *since the assay was designed*, which needs a year per record, and FASTA
headers do not carry one while full GenBank flatfiles are an order of magnitude
more data to move. Nothing is deduplicated at fetch time — each archive is a
self-describing snapshot of what that query returned that day, which is what
makes a past report reproducible.

The query is `txid<taxid>[Organism:exp]`. The `exp` expands down the taxonomy,
so a genus-level taxid picks up every species under it, which is what a
pan-genus assay should be screened against and why the registry stores a taxid
rather than a name.

### On a cluster

```bash
pip install snakemake-executor-plugin-slurm
snakemake --profile profiles/slurm --config email=you@example.org
```

Nothing in the Snakefile changes. Snakemake submits each job with `sbatch`
instead of running it, waits for the scheduler and collects the outputs; a
rule's `resources:` block becomes the `sbatch` request, which is why
`screen_archive` declares `mem_mb` (scaled with its threads) and `runtime`. The profile sets how many jobs
may sit in the queue at once (not how many cores), the partition and the
defaults. Retrieval stays a single job on purpose: NCBI's rate limit is global,
so parallel fetch jobs would each sleep for their own limit and together exceed
it. The parallelism worth having is in scoring, which is pure CPU and
embarrassingly parallel across taxa.
