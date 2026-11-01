# AssayWatch

[![CI](https://github.com/batyanight/assaywatch/actions/workflows/validate.yml/badge.svg)](https://github.com/batyanight/assaywatch/actions/workflows/validate.yml)
[![Docs](https://github.com/batyanight/assaywatch/actions/workflows/site.yml/badge.svg)](https://batyanight.github.io/assaywatch/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23841793.svg)](https://doi.org/10.5281/zenodo.23841793)
[![Release](https://img.shields.io/github/v/release/batyanight/assaywatch)](https://github.com/batyanight/assaywatch/releases)
[![Code MIT](https://img.shields.io/badge/code-MIT-blue)](LICENSE)
[![Registry CC--BY--4.0](https://img.shields.io/badge/registry-CC--BY--4.0-blue)](LICENSE-registry)

**Continuous in-silico re-validation of published PCR/qPCR diagnostic assays against
newly deposited GenBank sequences.**

An assay is designed against the sequences that existed when it was designed, then used
for years while GenBank fills with strains nobody re-screens it against. Nothing tells
you when the primers stop matching — the reaction just comes back negative, and a
negative looks the same whether the pathogen was absent or the primers missed it.

AssayWatch keeps a version-controlled registry of **218 published assays**, each citing a
paper whose DOI Crossref has confirmed, screens every one against the GenBank records of
its own target, and reports predicted detection **by year of deposit**, so decay reads as
a trend rather than a snapshot. The registry and that time axis are the contribution; the
screening engine is the means.

### 📊 [Browse every assay →](https://batyanight.github.io/assaywatch/assays/)

The website has a dashboard per assay — detection by deposit year, where the mismatches
sit on each oligo, the per-lineage breakdown — plus
[scoring methods](https://batyanight.github.io/assaywatch/scoring/),
[how a run works](https://batyanight.github.io/assaywatch/pipeline/),
[validation](https://batyanight.github.io/assaywatch/validation/),
[known limitations](https://batyanight.github.io/assaywatch/limitations/),
[scoping](https://batyanight.github.io/assaywatch/scoping/) and the
[glossary](https://batyanight.github.io/assaywatch/glossary/).

## Read this before trusting a status

**A status is worth reading, not quoting.** `declining` means "worth looking at", not
"this assay has failed" — and the project measures how often it is right rather than
asserting it. Against the 50-case development set on the 2026-10-31 run, **4 of 10
`declining` calls were real documented failures** (95% CrI 15%–70%), catching **6 of 11**
documented failures with 4 false alarms in 32 working assays. All three held-out sets
scored *worse*. Nineteen thresholds decide every verdict and all but one were set by eye.

[`docs/state-of-the-project.md`](docs/state-of-the-project.md) is the one-page version of
what the output is worth; [`ROADMAP.md`](ROADMAP.md) is the only to-do list.

## The premise has one confirming case

On 2026-10-30 the tool caught its first documented failure through the drift flag itself
rather than through `low coverage`. Scored as of September 2013, on records deposited
before the paper that reported the problem:

| assay | status | detected share |
|---|---|---|
| `INFLUENZA_A_M1_Ward_2004` | **declining** | 86.2% of 5,847 records |
| `INFLUENZA_A_M1_Yang_2014` — the documented redesign | **stable** | 91.6% on the same records |

The two entries differ in nothing but their oligos — same retrieval group, archive, date
window, scoring config and chemistry — so the verdict difference is attributable to the
primer and probe sequences and nothing else. That control is what makes the case worth
more than the verdict. One case is one case: the second row of that held-out set is a
miss, and [why](https://batyanight.github.io/assaywatch/validation/) is more
instructive than the catch.

## See the output without installing anything

[`docs/example-run-2026-10-31/report.md`](docs/example-run-2026-10-31/report.md) is one
real run, committed. On the 2026-10-31 run, 217 assays screened: 72 stable, 42 declining, 31 low
coverage, 30 insufficient data, 18 no recent data, 5 watch, and 19 given no status
because their entries say a verdict would not be a statement. Its companion
[`site-drift.md`](docs/example-run-2026-10-31/site-drift.md) names the base to order at
each drifted primer position.

Then [`examples/`](examples/README.md) runs the screening step on your own machine,
offline, in under a second.

## Quick start

```bash
conda env create -f environment.yml && conda activate assaywatch
pytest -q && assaywatch validate registry      # the gate, ~45 s
python examples/make_example_fasta.py
python -m assaywatch.screen \
  registry/CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004.yaml \
  examples/bd-example.fasta -o calls.tsv
```

A full run needs an NCBI key and hours of fetching:
[`docs/running-the-pipeline.md`](docs/running-the-pipeline.md).

## Where things are

| | |
|---|---|
| what the output is worth, in one page | [`docs/state-of-the-project.md`](docs/state-of-the-project.md) |
| screening, scoring and the drift call, in full | [`docs/screening-and-the-drift-call.md`](docs/screening-and-the-drift-call.md) |
| running the pipeline, disk, retrieval groups, cluster | [`docs/running-the-pipeline.md`](docs/running-the-pipeline.md) |
| the pipeline's design, stage by stage | [`docs/pipeline-architecture.md`](docs/pipeline-architecture.md) |
| setup in more detail | [`docs/installation.md`](docs/installation.md) |
| everything under `docs/` — 10 reference documents, 138 journals, 25 data files (2026-10-31) | [`docs/INDEX.md`](docs/INDEX.md) |
| the project vocabulary, used in code and commits | [`GLOSSARY.md`](GLOSSARY.md) |
| submitting an assay | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| what changed between releases | [`CHANGELOG.md`](CHANGELOG.md) |

## Related work

Matching oligos against sequence and counting mismatches is not new, and two existing
tools do it thermodynamically rather than with a positional penalty table:
[PCR_strainer](https://github.com/BCCDC-PHL/PCR_strainer) assesses assay inclusivity
against genome sets via TNTBLAST, and [GoPrime](https://doi.org/10.3390/pathogens9040303)
fits a model of real-time PCR performance from sequence instead of asserting one.
[NEB's Primer Monitor](https://primer-monitor.neb.com/) is the closest thing to this
project's premise — continuous monitoring of registered primers against new GenBank
deposits, with alerts — and covers SARS-CoV-2 and RSV.
[ViralPrimer](https://doi.org/10.1093/bioinformatics/btae657),
[PCRv](https://doi.org/10.1016/j.jviromet.2019.05.002) and
[openPrimeR](https://doi.org/10.1016/j.jim.2020.112752) cover the rest of the space.

What none of them has is a **curated registry of published wildlife and One-Health
pathogen assays** — citations verified against Crossref, amplicon sizes measured on
real records rather than read off a gel band, provenance caveats under a controlled
vocabulary — screened **by year of deposit** so decay reads as a trend rather than a
pass/fail against today's database. That registry and that axis are the contribution;
the screening engine is the means. A third intended difference, a lineage-conditional
estimand, is designed and only partly built, so it is not yet a contribution.

`docs/related-work.md` has the comparison in full, plus the methodological and
statistical references the scoring rule and the drift call rest on.
## Provenance

Code is MIT (`LICENSE`); the registry and the curated tables are CC-BY-4.0
(`LICENSE-registry`). Every entry in `registry/` cites a paper whose DOI Crossref has
confirmed; assays without one wait in `pending/` and are never screened or published.

Most of this repository was written by Claude (Anthropic) in a Claude Code session,
directed by the author: 581 of the 640 development commits carried a co-authorship
trailer (2026-10-31). This repository begins at a single commit because it was recreated
from a clean tree on 2026-10-31; the development history is retained privately and is
not reconstructible from here. `docs/ai-involvement.md` says what that means, why the
history was not published, and which checks in the repository make every factual claim
here verifiable rather than taken on trust.
## Setup (macOS, conda)

```bash
conda env create -f environment.yml   # primer3-py comes from bioconda; pip cannot build it on arm64
conda activate assaywatch
pre-commit install
pytest -q && assaywatch validate registry
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
filled, so those gaps are derived from the fields instead.

Inosine is written as N in `seq` (the original is kept in `seq_as_written`).
Extra oligos found in a source (degenerate cocktails, dye variants) sit under
`oligos.alternates` with an explicit `orientation`.
## Adding an assay

Write one YAML per assay in `registry/`, reading the oligos, amplicon and design
year from the cited paper's own table, enter the DOI with `doi_verified: false`,
then let Crossref confirm it:

```bash
python scripts/resolve_citations.py --registry registry --email you@example.org
assaywatch validate registry
```

Only an entry with a verified DOI is live. The validator and the Snakefile both
refuse an entry without one; an assay that has no paper yet waits in `pending/`.
Host-identification, DNA barcoding, eDNA, internal-control and kingdom-level
universal primers are out of scope: they target the host or a whole kingdom
rather than a pathogen, and the drift question does not apply to them in the
same form.
## Contributing an assay

`CONTRIBUTING.md` has the submission template and the review process.
`scripts/check_submission.py` checks a candidate entry — schema, undeclared 5'
cloning tails, degeneracy, that the DOI resolves to the paper named, that the
taxid still means what it says, and above all whether the oligos find their
amplicon in real records. `scripts/scan_literature.py` proposes recently
published assays for targets already in the registry, and never adds any.
## Layout

```
registry/        one YAML per assay; validated on every commit. `python -m
                 assaywatch.validate registry` prints the counts rather than this
                 file quoting them, because the ones written here by hand drifted
                 as the registry grew: 214 files on 2026-10-14, of which 210 were
                 draft and 44 carried a probe (2026-10-14)
assaywatch/      the package
  schema.py        pydantic models = the registry schema
  registry.py      the one door to the entries: load / load_one / write / edit (comment-preserving) / archive_dir
  validate.py      `assaywatch validate registry`; its loaders are registry.py's
  curate.py        `assaywatch curate <entry>`: the curation chain, write-through, stopping where judgement is needed
  printed.py       what a paper prints, and whether a stored oligo is in it (exact / revcomp / in-text / near / absent)
  iupac.py         degenerate-base helpers, inosine, three-state comparison
  degeneracy.py    primer-pool accounting; `assaywatch degeneracy registry`
  match.py         exhaustive search for oligo binding sites, both strands
  score.py         position-weighted mismatch penalty and the per-record call
  ncbi.py          the one NCBI client: key, pacing, retry, taxonomy parsers, and the only writer of the taxonomy caches
  retrieve.py      NCBI fetch, incremental, archived; `assaywatch retrieve`
  drift.py         per-assay proportions with Wilson / Newcombe intervals
  report.py        `assaywatch report` -> report.md and a standalone report.html
  screen.py        `assaywatch screen <assays> <fasta>` -> TSV of calls
  thermo.py        optional duplex Tm / ΔTm columns per oligo (primer3-py); never scored
  gapped.py        gapped oligo search used only by scripts/indel_check.py; never scored
  chance.py        E-value of a primer pair: could it be chance in a record this long?
  assemblies.py    NCBI Datasets genome sampling for bacterial targets (`asm` groups)
  fasta.py         minimal FASTA reader
  papers.py        the papers/ naming convention and the literature client: Crossref, open-access routes, Europe PMC
                   full text, Elsevier, storage, and `obtain`, the chain curate runs
Snakefile          the pipeline; profiles/slurm/ runs the same rules on a cluster
pending/         entries waiting for a verified DOI; never screened (pending/README.md)
scripts/         registry QA: check_taxids.py (taxid vs NCBI name), indel_check.py,
                 check_amplicons.py (stored amplicon_bp vs measured, over every archive),
                 verify_oligos_against_paper.py (stored oligo vs the paper that is cited),
                 orphan_archives.py (archives on disk that no live assay asks for).
                 Papers come in by three routes, in this order: find_open_access.py
                 (Unpaywall/OpenAlex -> a PDF), fetch_europepmc_fulltext.py (open full
                 text as XML, tables included), import_pmc_fulltext.py (the same corpus
                 as JSON, for an environment with no direct network).
tests/           pytest; includes "every registry file validates"
config.yaml      scoring thresholds and paths; no numbers live in code
data/retrieved/  per-taxon FASTA archives (git-ignored; Phase 1)
results/         per-run scored tables and reports (git-ignored; Phase 1)
```
