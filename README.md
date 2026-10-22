# AssayWatch

Continuous in-silico re-validation of published PCR/qPCR diagnostic assays
against newly deposited GenBank sequences. Assays are designed against the
handful of sequences available at publication and then run for years while
the database accumulates divergent strains nobody re-screens them against.
AssayWatch keeps a version-controlled registry of assays and re-screens it on a
schedule, reporting predicted detection by year of deposit and flagging drift.

Status: Phase 1 complete end to end — retrieve, screen, assess drift, report —
and wired into a Snakefile. Retrieval is tested against canned E-utilities
responses and has been run against the live NCBI API: the 2026-10-06 run screened
208 of the 211 non-deprecated registry assays against records fetched that day.
See ROADMAP.md.

For a worked example that runs offline in a second, see `examples/README.md`.

## Layout

```
registry/        one YAML per assay; validated on every commit. `python -m
                 assaywatch.validate registry` prints the counts rather than this
                 file quoting them, because the ones written here by hand drifted
                 as the registry grew: 214 files on 2026-10-14, of which 210 are
                 draft and 44 carry a probe
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
                 plus registry QA: check_taxids.py (taxid vs NCBI name), indel_check.py,
                 check_amplicons.py (stored amplicon_bp vs measured, over every archive),
                 verify_oligos_against_paper.py (stored oligo vs the paper that is cited).
                 Papers come in by three routes, in this order: find_open_access.py
                 (Unpaywall/OpenAlex -> a PDF), fetch_europepmc_fulltext.py (open full
                 text as XML, tables included), import_pmc_fulltext.py (the same corpus
                 as JSON, for an environment with no direct network).
tests/           pytest; includes "every registry file validates"
config.yaml      scoring thresholds and paths; no numbers live in code
data/retrieved/  per-taxon FASTA archives (git-ignored; Phase 1)
results/         per-run scored tables and reports (git-ignored; Phase 1)
```

## Contributing an assay

`CONTRIBUTING.md` has the submission template and the review process.
`scripts/check_submission.py` checks a candidate entry — schema, undeclared 5'
cloning tails, degeneracy, that the DOI resolves to the paper named, that the
taxid still means what it says, and above all whether the oligos find their
amplicon in real records. `scripts/scan_literature.py` proposes recently
published assays for targets already in the registry, and never adds any.

## Setup (macOS, conda)

```bash
conda env create -f environment.yml   # primer3-py comes from bioconda; pip cannot build it on arm64
conda activate assaywatch
pre-commit install
pytest -q && python -m assaywatch.validate registry
```

`environment.yml` installs the package in editable mode (`pip: -e .`), so
`import assaywatch` works from any directory and edits are live.

`environment.yml` pins the decisions (Python, Snakemake minor, ruff) and names
every dependency a documented command needs, but leaves the transitive graph to
the solver, so two machines can still differ in a sub-dependency. For an exact,
cross-platform pin, regenerate the lock after any `environment.yml` change:

```bash
conda-lock -f environment.yml -p osx-arm64 -p linux-64   # writes conda-lock.yml
conda-lock install -n assaywatch conda-lock.yml          # install from the lock
```

`conda-lock.yml` is committed and ships in the sdist (`MANIFEST.in`); the plain
`conda env create` above stays the quick path.

## Registry rules

A file is one assay: forward + reverse primer, optional probe, target taxon,
citation. `status: draft` files only need correct structure and IUPAC oligos
of 15-40 nt, except that a probe may be as short as 12 nt (published MGB probes run
13-14). `status: active` additionally requires `target.taxid`, a DOI with
`doi_verified: true`, `design_year`, and no *open* review flag — every one of
them evidence about the assay rather than about who entered it, which is why
`submitted_by` is not among them. The validator enforces this; CI and the
pre-commit hook run it.
Unknown keys are rejected, so a typo in a field name fails the commit rather
than being silently ignored.

`needs_review` is a list of `{flag, note}` items drawn from one controlled
vocabulary, defined with its reasoning in `assaywatch/review.py`. A flag is
either an **open question** a human still has to answer, which holds the entry
at `draft`, or a **recorded caveat** that is settled and merely disclosed —
`nested_protocol`, `oligos_modified`, `amplicon_measured_not_published` — which
does not. `note` carries one line of specifics where the flag alone is not
enough; the full record stays in `source.notes_curator`. Flags that would only
restate another field (`citation.doi`, `design_year`, `target.taxid`) are not in
the vocabulary, because a stored restatement goes stale the moment the field is
filled: `scripts/materials_needed.py` derives those gaps instead.

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

**A product has to be the size the assay says it is.** `amplicon.declared_tolerance`
(0.25, on since 2026-10-14) constrains a call to the assay's own `amplicon_bp`,
within a quarter either way, instead of only to the global 50–3000 bp window. A
1931 bp product is not a 194 bp assay amplifying: the extension time, probe
geometry and efficiency belong to something else. The tolerance is measured
rather than chosen — over the 2026-10-07 run, |observed/declared − 1| has a knee
at about 0.2 and flattens past it, so 0.25 keeps 99.3% of the calls that had a
declared size. Applied to that run it would move 59,141 rows out of the
denominator, 54,966 of them `fail`, which is the correction running in the
pessimistic direction: most oversized products were being counted against the
assay. It does mean a mistranscribed `amplicon_bp` now voids an assay's calls instead
of being inert, so `scripts/check_amplicons.py` is the thing to run when an
assay's numbers collapse.

What the filter mostly catches, though, is not a wrong number but **two products
in one entry**. The three assays whose measured product sat furthest from their
declared size each hold a second amplicon in `oligos.alternates` — a nested
secondary pair, or an alternative reverse — and `score.oligo_pools` treats
alternates as interchangeable members of one pool, which is right for a
consensus cocktail and wrong for a second round. Measured over the first 400
records of each archive — 290 for the nidovirus one, which holds no more —
their declared pairs give 1320, 161 and 1695 bp against a declared 1319, 163
and 1694: the stored numbers are right, and it was the alternate's product
being credited to the assay. With the filter on, the out-of-window combination
is `no_amplicon` and the screener falls back to the declared pair. 20 of 214
entries could form a second product this way. The fix is curation — one entry
per round, as the CMV gB and adenovirus polymerase assays already have.

### What the scoring rule assumes about PCR, and where it is wrong

The penalties come from one well-supported fact and several guesses, and it is
worth knowing which is which before reading a call.

**The fact.** A polymerase extends from the primer's 3'-OH, so a mismatch there
sits in the catalytic site, while one near the 5' end costs only a little duplex
stability on an oligo that has 19 other matched bases. Weighting mismatches by
distance from the 3' end is therefore the right shape (Kwok et al. 1990,
[10.1093/nar/18.4.999](https://doi.org/10.1093/nar/18.4.999); Stadhouders et al.
2010, [10.2353/jmoldx.2010.090035](https://doi.org/10.2353/jmoldx.2010.090035)).

**The guesses, in rough order of how much they matter.**

1. *The penalty is blind to which mismatch it is.* Both papers above find
   identity dominates: at the 3' terminus, A:A, A:G, G:A and C:C suppress yield
   by orders of magnitude (>7 Cq in Stadhouders), while T:G, T:C and T:T are
   nearly free (<1.5 Cq) — a T:G wobble still stacks. So
   `terminal_mismatch_fails` is right for about half of terminal mismatches and
   wrong for the rest. The *E. coli* malB result survives this because all 92
   failures are a single A→G at the reverse 3' base, which is in the severe
   class; the rule did not know that when it fired.
2. *Penalties from the three oligos are summed into one budget*, but amplification
   needs forward **and** reverse and detection needs the probe on top. Those are
   serial gates. Three trivial mismatches, one per oligo, land in the same bin as
   one near-lethal 3'-proximal mismatch.
3. *One table serves 167 conventional PCRs and 44 probe assays.* A 100-fold yield
   loss is a missed Cq cutoff in qPCR and often still a visible band after 40
   cycles of endpoint PCR. The same `fail` is printed for both.
4. *Probe geometry is length-blind, and MGB-blind.* Of the 44 probe assays here,
   22 are MGB (the other 22 are plain hydrolysis probes), and the minor-groove binder
   adds roughly 15–20 °C of Tm and makes short probes viable; such a probe tolerates
   mismatches a bare oligo of the same length would not. `--thermo` computes the real duplex ΔTm and is the better
   guide where it is available.
5. *Mismatches add linearly*, so two adjacent ones — which destroy a contiguous
   run of base stacking — are under-penalised relative to two spread apart.

None of this is hidden in code: every threshold is annotated in `config.yaml`
with its justification or an admission that it has none, and the standing
numbers are in
[docs/2026-10-04-pipeline-review.md](docs/2026-10-04-pipeline-review.md).
Against 46 cases from published follow-up the tool flags 1 of 12 documented
failures, so a call is a reason to look, not a result.

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
caffeinate -i snakemake --cores 4 --config email=you@example.org
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
`data/retrieved/` only grows — 7.8 GB across 127 groups on 2026-10-14, against
457 MB of cached screens and 44 MB of reports. The instinct when that fills a
disk is to delete the biggest thing, and here the biggest thing is the only
thing that cannot be recovered:

| | 2026-10-14 | recoverable? |
|---|---|---|
| `data/retrieved/*.fasta.gz` | 7.8 GB | **no** — retrieval is incremental (`datetype=mdat`), so each archive is the set of records that changed since the previous run, which NCBI will not reproduce on request; records are also revised and withdrawn |
| `data/retrieved/*.meta.tsv.gz` | 19 MB | **no**, and it carries the deposit dates the whole drift statistic is indexed on — 0.2% of the volume for the most irreplaceable part of it |
| `results/screened/` | 457 MB | yes, deterministically, ~45 min on 10 cores |
| `results/<date>/` | 44 MB | yes, minutes, from the screens |

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
  below zero, the fall is at least `min_decline`, **and** the assay cleared the
  threshold in some earlier year (`drift.require_working_baseline`, on since
  2026-10-14). The share has fallen from a level that worked; that is drift.
  The last condition is what keeps the word honest: without it 14 of the 37
  assays called declining on 2026-10-07 were pan-family consensus PCRs that
  never covered the taxon they are screened against — a fall from 14% to 0% is
  a change in which clades were deposited, not an assay degrading. The test is
  per year, not on the aggregate baseline, which a long decline drags down by
  itself. Those 14 are now **low coverage**, and their note says they are also
  falling.
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

**What the fraction estimates, and what it does not.** The intervals above
assume records are independent draws from the population the assay is used on.
Neither half holds:

* *GenBank samples sequencing effort, not circulating diversity.* An outbreak
  deposits hundreds of near-identical sequences from one transmission chain;
  endemic background deposits none. The effective sample size is the number of
  independent lineages, so a Wilson interval computed on record counts is
  narrower than the evidence warrants.
* *Deposition is correlated with detection.* A locus is often sequenced
  *because* an assay amplified it, and a variant that escapes PCR may never be
  deposited. The bias runs toward optimism, which makes `declining` strong
  evidence and `stable` weak evidence. They are not symmetric.
* *One proportion per assay is the wrong estimand for most real failures.*
  Published failures are nearly always lineage-conditional — fails on clade B,
  on the lineage circulating in one region, on the fish ranaviruses the assay
  never claimed. A clade that is 5% of deposits can be 100% of a region's cases,
  and averaging it away is precisely why the retrospective harness catches 1 of
  12 documented failures. Per-clade fractions are the fix, and are not built.

So `detect_fraction_threshold: 0.90` is a judgement about tolerable
surveillance loss, not a property of PCR: an assay missing 1 in 10 targets is
still fine for prevalence and useless for ruling out disease in one animal.

**Joining calls to deposit years** is the one fiddly part. The screen stage
keys on the FASTA record id, which from NCBI carries a version (`AB123456.1`);
the metadata keys on the esummary caption, which does not (`AB123456`). The
join strips the version from both sides, and where several versions of one
accession appear, the latest revision wins rather than both being counted.

**Nested protocols are scored per round, then round 2 is warned about round 1.**
A nested or semi-nested protocol is several entries here, one per round, and each
is screened independently — which is right, because either product can be read on
a gel, so a round whose primers still match is a usable assay on its own. But
round 2's figure answers "would these primers bind this sequence", which is the
question for round 2 run *directly*; run as published its template is round 1's
product, so a record whose outer primers have drifted yields nothing however well
the inner pair matches. The report therefore adds a **Nested protocols** table
giving each round's own share beside the share of records *both* rounds reach.

On the 2026-10-07 records that gap is large for a few families and absent for
most: `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` reads 99.5% for round 2 alone and
**32.4% run as a nest**, because round 1 escapes on two thirds of the records
round 2 would otherwise reach; `BOCAVIRUS_ssDNA_NS1_gene` and
`Pan_flavivirus_NS5_3` lose essentially nothing. Only round-1 failures that are
the assay's fault count — a `fail`, or a `no_amplicon` labelled `diverged` — on
the same reasoning the drift denominator already uses.

Nothing here changes a status: it is reported beside the per-round rows, as
degeneracy and thermodynamics are. The dependency is one-directional, since round
2 failing leaves round 1's product perfectly readable.

**And the nesting itself is checked**, which nothing did before: on records both
rounds score, does the inner amplicon actually lie inside the outer? Three
families fail that test and get no conditional coverage, because conditioning
round 2 on a round 1 that does not feed it would invent a number. The clearest is
`CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme`, whose two amplicons are **disjoint**
— about 2.7 kb apart in the RdRp gene — so whatever the `_round2` suffix says,
these are two assays rather than two rounds. Round order comes from
`source.nested_round` rather than the id, because the id does not always carry it:
the Landolfi orthoreovirus base entry holds the paper's *second* round, and taking
the base as the outer round inverted that pair until the containment check caught
it.

**Coverage gaps** list assays whose target has fewer than
`min_records_for_coverage` evaluable records. An assay cannot be shown to work
against diversity nobody has sequenced, and for wildlife pathogens that is
usually the finding rather than a caveat.
