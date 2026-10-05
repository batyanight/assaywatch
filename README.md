# AssayWatch

Continuous in-silico re-validation of published PCR/qPCR diagnostic assays
against newly deposited GenBank sequences. Assays are designed against the
handful of sequences available at publication and then run for years while
the database accumulates divergent strains nobody re-screens them against.
AssayWatch keeps a version-controlled registry of assays and re-screens it on a
schedule, reporting predicted detection by year of deposit and flagging drift.

Status: Phase 1 complete end to end — retrieve, screen, assess drift, report —
and wired into a Snakefile. Retrieval is tested against canned E-utilities
responses but has not yet been run against the live NCBI API; that is the next
thing to do. See ROADMAP.md.

## Layout

```
registry/        one YAML per assay; validated on every commit (138 WCS pathogen assays, all draft)
assaywatch/      the package
  schema.py        pydantic models = the registry schema
  validate.py      `python -m assaywatch.validate registry`
  iupac.py         degenerate-base helpers, inosine, three-state comparison
  degeneracy.py    primer-pool accounting; `python -m assaywatch.degeneracy registry`
  match.py         exhaustive search for oligo binding sites, both strands
  score.py         position-weighted mismatch penalty and the per-record call
  retrieve.py      NCBI fetch, incremental, archived; `python -m assaywatch.retrieve`
  drift.py         per-assay proportions with Wilson / Newcombe intervals
  report.py        `python -m assaywatch.report` -> report.md and a standalone report.html
  screen.py        `python -m assaywatch.screen <assays> <fasta>` -> TSV of calls
  thermo.py        optional duplex Tm / ΔTm columns per oligo (primer3-py); never scored
  gapped.py        gapped oligo search used only by scripts/indel_check.py; never scored
  chance.py        E-value of a primer pair: could it be chance in a record this long?
  assemblies.py    NCBI Datasets genome sampling for bacterial targets (`asm` groups)
  fasta.py         minimal FASTA reader
Snakefile          the pipeline; profiles/slurm/ runs the same rules on a cluster
scripts/         one-off import of the WCS primer spreadsheet (parse -> curate -> resolve),
                 plus registry QA: check_taxids.py (taxid vs NCBI name), indel_check.py
tests/           pytest; includes "every registry file validates"
config.yaml      scoring thresholds and paths; no numbers live in code
data/retrieved/  per-taxon FASTA archives (git-ignored; Phase 1)
results/         per-run scored tables and reports (git-ignored; Phase 1)
```

## Setup (macOS, conda)

```bash
conda env create -f environment.yml   # primer3-py comes from bioconda; pip cannot build it on arm64
conda activate assaywatch
pre-commit install
pytest -q && python -m assaywatch.validate registry
```

`environment.yml` installs the package in editable mode (`pip: -e .`), so
`import assaywatch` works from any directory and edits are live.

## Registry rules

A file is one assay: forward + reverse primer, optional probe, target taxon,
citation. `status: draft` files only need correct structure and IUPAC oligos
of 15-40 nt. `status: active` additionally requires `target.taxid`, a DOI with
`doi_verified: true`, `design_year`, `submitted_by`, and an empty
`needs_review`. The validator enforces this; CI and the pre-commit hook run it.
Unknown keys are rejected, so a typo in a field name fails the commit rather
than being silently ignored.

Inosine is written as N in `seq` (the original is kept in `seq_as_written`).
Extra oligos found in a source (degenerate cocktails, dye variants) sit under
`oligos.alternates` with an explicit `orientation`.

## Importing from the WCS spreadsheet

```bash
cd scripts
python parse_wcs_primers.py --xlsx Primers_for_WCS_Molecular_Lab_updated_021518.xlsx --out-dir out
python apply_curation.py --drafts out/registry_draft --curation curation.yaml --out ../registry
python resolve_citations.py --registry ../registry --email you@example.org
```

`curation.yaml` is the only place outside-knowledge (taxids, DOIs) is entered;
the parser is deterministic. Its `exclude` section is where scope is decided:
host-identification, DNA barcoding, eDNA, internal-control and kingdom-level
universal primers are parsed but not written to the registry, because they
target the host or a whole kingdom rather than a pathogen and the drift
question does not apply to them in the same form. `scripts/removed_assays.txt`
lists the 38 that were dropped; removing an id from `exclude` and rerunning
`apply_curation.py` brings it back. `resolve_citations.py` confirms DOIs against
Crossref and fills missing taxids from NCBI Taxonomy.

## Screening

```bash
python -m assaywatch.screen registry/CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004.yaml \
    tests/fixtures/records.fasta -o calls.tsv
```

`--workers N` screens one archive across N processes; the output is byte for
byte the same as with one worker (assays in registry order, records in archive
order), and memory stays at a few batches of `--chunk-bp` bases however large
the archive is.

One row per (assay, record) with the call, the total penalty, the amplicon
coordinates, and each oligo's mismatches expressed as distance from its 3' end
(1 = the terminal base). Four calls:

| call | meaning |
|---|---|
| detect | total penalty <= `detect_max` |
| reduced | <= `reduced_max`; amplifies but expect a Ct shift |
| fail | above `reduced_max`, a mismatch at a primer's 3'-terminal base, or no probe site inside the amplicon |
| indeterminate | more than `max_ambiguous_per_oligo` undetermined record bases under an oligo |
| no_amplicon | no primer pair in the right orientation and size range |

`no_amplicon` and `indeterminate` are kept separate from `fail` on purpose: a
partial record, or one full of ambiguity codes, is a sequence-quality problem
rather than an assay problem, and mixing the two would make every rough
GenBank entry look like drift.

### Degeneracy is never penalised

Each position of an oligo against a record resolves to one of three states,
not two (`iupac.base_state`):

| state | example | effect |
|---|---|---|
| match | primer `Y`, record `C` or `T` | nothing; this is what degeneracy is for |
| mismatch | primer `A`, record `S` (C or G) | scored by position, as usual |
| unknown | primer `A`, record `R` (A or G), or any record `N` | counted, never charged |

The third state is the one that matters for degenerate assays. Pan-family
primers need degeneracy precisely because they target sparsely and unevenly
sequenced taxa, and those are the records with ambiguity codes in them.
Charging an `R` or an `N` as a mismatch would tax those assays for the
submitter's sequencing quality and would make real drift indistinguishable
from missing information. It would also be wrong at the 3'-terminal base,
where a definite mismatch is fatal but an undetermined base says nothing.

Undetermined positions are reported per oligo (`fwd_ambiguous`,
`rev_ambiguous`, `probe_ambiguous`). Once an oligo's footprint carries more
than `max_ambiguous_per_oligo` of them, too little of the binding site is known
to judge and the record is called `indeterminate`. That cap also stops a run of
Ns elsewhere in a record — which matches every oligo — from being reported as a
clean amplicon.

### Degeneracy is reported instead

Not penalising degeneracy creates the opposite bias: an oligo full of N matches
everything by construction, so a heavily degenerate assay can never be seen to
drift and its `detect` calls approach a tautology. That is a property of the
assay, not of any record, so it is reported alongside the drift numbers rather
than folded into them. Every row of a screen carries `degeneracy_fold` and
`degeneracy_tier` for its assay, and

```bash
python -m assaywatch.degeneracy registry --tier severe
```

lists the assays whose in-silico coverage should be read with the most
suspicion. Of the 138 imported WCS assays, 74 are negligible, 19 moderate,
25 high and 21 severe — the severe end being the PREDICT pan-family consensus
PCRs, which is expected and is the point of them.

The headline `total_fold` multiplies every oligo, primers and probe, because
all of it is reagent that does not participate in detecting a given template,
and `log2(total_fold)` is reported as `dCq`: a first-order estimate of the Cq
delay, since the log of a product is the sum of the logs. The components stay
visible, because they fail differently. Primer dilution attacks amplification:
annealing is pseudo-first-order in primer concentration, efficiency sits in
the base of the exponential, and a deficit compounds until the reaction does
not take off. Probe dilution attacks only the readout: a hydrolysis probe is
cleaved from the amplicon and is not part of the amplification mechanism, so a
diluted probe reports a smaller share of whatever was made, which is a fixed
offset of about log2(n) cycles. An assay at 4096-fold that is all primers may
not amplify; one that is all probe amplifies fine and reports late. `dCq` is
therefore a lower bound at the high end, not a prediction.

Degeneracy is a concentration effect, not a binding effect: a pool of *n*
oligos contributes roughly 1/*n* of the nominal concentration to any one
template, which costs sensitivity rather than coverage. **Inosine is not
degeneracy.** An inosine-containing primer is one molecule that pairs
promiscuously, which is exactly why designers reach for it, and it pays no
concentration cost. The registry stores inosine as `N` in `seq` to keep that
field strict IUPAC and keeps the original in `seq_as_written`; matching and
degeneracy both read `seq_as_written`, so I pairs with C, A and T, is `unknown`
opposite G (a real but poor pair), and counts as one molecule. Reading the
PREDICT filovirus reverse primer from `seq` instead would call it 8192-fold
degenerate when it is 8-fold: the difference between an unusable assay and a
working one.

### Thermodynamics are reported, not scored

The mismatch penalty is positional. What a mismatch does to binding depends on
which mismatch it is and what surrounds it, so `--thermo` (or `thermo: true` in
config.yaml for the pipeline) adds the primer3 nearest-neighbour Tm of each
oligo on its actual binding site, and its shift from a perfect site:

| column | meaning |
|---|---|
| `fwd_tm`, `rev_tm`, `probe_tm` | duplex Tm (°C) on the record's site |
| `fwd_dtm`, `rev_dtm`, `probe_dtm` | that Tm minus the same oligo's Tm on a perfect site |
| `thermo_min_dtm` | the worst ΔTm across the assay's oligos |
| `thermo_note` | `inosine` when inosine was modelled as the base it faces (an upper bound) |

ΔTm is the column to read: absolute Tm depends on the salt and oligo
concentrations in `thermo_conditions`, which differ between protocols, and the
shift caused by the record's mismatches depends on them much less. Degenerate
positions take the record's base when the pool has it (that pool member is the
one that amplifies), and undetermined record bases are modelled as matches, as
in scoring. On the flavivirus archive the median worst ΔTm was −5 °C for
`detect`, −12 °C for `reduced` and −17 °C for `fail`; the extra columns cost
no measurable screening time. Calls are identical with or without `--thermo`.

## Matching

`find_sites(oligo, record, max_mismatches)` returns every ungapped site on
either strand within the mismatch budget. The search is exhaustive by
construction: a 256-entry lookup table per oligo position is applied to the
record as a numpy array, giving the mismatch count at every alignment offset
in L vectorised passes, and only the offsets within budget are revisited to
recover which positions mismatched. A 25 nt oligo against a 30 kb record takes
about 5 ms; one probe-based assay against 1000 records of 1.5 kb takes under a
second.

Undetermined record bases are free when a site is *scored* but count against
the budget when it is *found*: a window of Ns is not evidence of a binding
site, and without this rule every offset in a scaffold gap matched every oligo
perfectly and the pair scoring went cubic (the first live run spent nine hours
on the Bd archive). A site with a few undetermined bases is still found and is
called `indeterminate` if there are too many to judge.

Raising `max_mismatches` can only add sites, never move or remove one, which
`tests/test_match.py` asserts along with equality against a brute-force scan
on random and degenerate sequences. Gaps are not modelled: a binding site with
an indel in it is not a working primer site, and treating it as one would
invent amplicons that do not exist.

## Fixtures

`tests/fixtures/` holds 84 synthetic records built by `tests/make_fixtures.py`:
a perfect amplicon per assay, then copies with substitutions planted at known
distances from each oligo's 3' end, plus an unrelated random record. Two plans edit both ends of one
oligo at once, which the seeded matcher that preceded the current one could
not find at all; three plant ambiguity codes, including at the 3'-terminal
base, to pin down the no-penalty rule. The expected call for every record was worked out by hand
from `config.yaml` before the scorer ran, and `tests/test_score.py` asserts
it. Regenerate with:

```bash
python tests/make_fixtures.py && pytest -q
```

## Running the pipeline

```bash
caffeinate -i snakemake --cores 4 --config email=you@nyu.edu
```

Five stages: validate the registry, retrieve what is new for each group,
screen every archive not yet screened, collect, report. `caffeinate -i` keeps a
Mac from idle-sleeping until the run ends.

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
set in `scripts/curation.yaml` under `queries`; the terms OR together gene
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
snakemake --profile profiles/slurm --config email=you@nyu.edu
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

## The drift call

`report.md` renders on GitHub; `report.html` is self-contained (inline SVG, no
CDN, no JavaScript) so it opens from a file:// path or GitHub Pages in a lab
with no bioinformatician.

**What goes in the denominator.** Only `detect`, `reduced` and `fail`: records
where both primers landed in the right orientation and size range, so the call
is a statement about the assay. `no_amplicon` and `indeterminate` are counted
and shown but excluded, because a record missing the locus, or truncated, or
full of ambiguity codes says something about GenBank rather than about the
assay. Folding them in would let a bad sequencing year look exactly like drift.
`reduced` counts as detected: it amplifies, just later.

**Why intervals and not just the fraction.** A wildlife assay may have five
records in the last two years. Three failing is 40% detected, which looks
alarming and means nothing — the 95% interval runs from about 10% to 70%.
Flagging on point estimates would bury real signals under noise from exactly
the sparsely sequenced taxa this tool exists to serve. So an assay is flagged
only when the *upper* bound of its recent interval falls below the
threshold: the data must be inconsistent with the assay still working, not
merely consistent with it failing. A flagged assay is then one of two things:

* **declining**: the Newcombe interval for the change from baseline lies wholly
  below zero. The share has fallen; that is drift.
* **low coverage**: below threshold, but not measurably lower than before (or
  no baseline to compare with). The first full run showed why this needs its
  own name: the gorilla/chimpanzee SIV assay of Takehisa 2009 screened against
  all SIV, or a "turtles only" Mycoplasma assay against the whole genus, sits
  at the same low share in every year. That is an assay used beyond its design,
  not one that has drifted.

**The recent window widens when records are scarce.** It is
`recent_window_months` long, but for an assay with fewer than
`min_records_for_drift` evaluable records in that window it extends a year at a
time, up to `max_window_months`, and the assay reports the window it used.
Without this, an assay for a sparsely sequenced taxon is judgeable only in the
years following a deposition burst: Bd ITS records arrive 56 in 2012 and then
four, so the standard Bd assay read "stable" in 2014 and "insufficient data"
every year after, on no change in the assay. Widening can only add older
records, never drop recent ones. On the 2026-10-04 run, 116 of 141 assays use
the plain 24-month window.

Below `min_records_for_drift` it is reported
as **insufficient data** and never flagged, whatever the fraction looks like;
below threshold with an interval that still covers it, it is **watch**.

The interval is Wilson rather than the textbook normal approximation, which
misbehaves near 0 and 1 — it can return bounds outside [0, 1], and at k = n it
collapses to zero width and claims certainty from a handful of records. The
change from baseline uses the Newcombe hybrid-score interval, which builds a CI
for a difference of proportions out of the two Wilson intervals and keeps that
good behaviour at the extremes, where baselines near 100% live. Both are
closed-form arithmetic, so every figure in the report can be recomputed by hand
from the counts in the per-year table.

**Joining calls to deposit years** is the one fiddly part. The screen stage
keys on the FASTA record id, which from NCBI carries a version (`AB123456.1`);
the metadata keys on the esummary caption, which does not (`AB123456`). The
join strips the version from both sides, and where several versions of one
accession appear, the latest revision wins rather than both being counted.

**Coverage gaps** list assays whose target has fewer than
`min_records_for_coverage` evaluable records. An assay cannot be shown to work
against diversity nobody has sequenced, and for wildlife pathogens that is
usually the finding rather than a caveat.
