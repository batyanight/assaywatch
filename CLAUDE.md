# CLAUDE.md — AssayWatch

Context for Claude Code sessions. Read this, then `docs/RESUME-HERE.md` for where
work left off. Keep this file short; detail lives in the docs it points to.
Personal working preferences live in `~/.claude/CLAUDE.md`, not here.

## What this is
Continuous in-silico re-validation of published PCR/qPCR assays against newly
deposited GenBank sequences. One YAML per assay in `registry/`, a Python package
in `assaywatch/`, a Snakefile that runs retrieve -> screen -> drift -> report.
Full layout and usage: `README.md`. Plan and status: `ROADMAP.md`.

**One to-do list: `ROADMAP.md`.** Open work goes there and nowhere else. A dated
doc under `docs/` is a record of what one session found; where it ends in "Next
steps" or "Still open", that was true on its own date and is marked as history.
`docs/RESUME-HERE.md` says where work stopped and keeps no list. Finishing an
item means ticking it in `ROADMAP.md`, not writing a new list in a new file.
The one deliberate exception is `papers/papers-fetch-list.md`, a queue of PDFs
that need a human and a proxy rather than a list of work.

## Scope (decided, do not reopen)
- Pathogen assays only. Host barcoding (COI etc.), eDNA and host-ID assays are
  out of scope and stay out of `registry/`.
- Source: the literature. Every entry cites its own paper; never mention the seed
  primer list the registry was started from, or any lab, as a source.
- Live = in `registry/`, and only with `citation.doi_verified: true` (the validator
  and Snakefile both refuse anything else). Entries waiting for a paper sit in
  `pending/`; `assaywatch validate pending --pending` checks them.

## Commands
    conda activate assaywatch                      # environment.yml; package installed editable
    assaywatch curate registry/ENTRY.yaml --email you@example.org   # the curation chain on one entry; --dry-run, --offline
    pytest -m fast                                 # pure functions on the fixtures, ~5 s: the write-test-run loop
    pytest -q && assaywatch validate registry   # everything except `slow`, ~45 s
    pytest -m slow                                 # the Snakemake dry-run tests (~80 s); CI runs them as their own job
    ruff check . && ruff format --check .
    python scripts/check_citations.py              # CI runs this too
    snakemake -n                                   # dry run: prints the job plan, downloads nothing
    caffeinate -i snakemake --cores 4 --config email=you@example.org   # lid OPEN: -i does not stop clamshell sleep
    scripts/weekly_run.sh [--live]                 # the scheduled run; dry by default. profiles/launchd/
    snakemake --profile profiles/slurm --config email=you@example.org   # same rules on SLURM
A change is not done until pytest, the validator, ruff and check_citations pass. Run `pytest -m slow` as well when a change touches the
Snakefile, a `config.yaml` section a rule hashes, or which modules a stage imports.
NCBI CLIs are in the env: `esearch | efetch` (Entrez Direct) and `datasets`
(NCBI Datasets). Prefer them for quick GenBank/taxonomy lookups over writing
one-off Python, and over asking Batya to download files by hand.

## Reading this repo cheaply
Search and summarise; don't read large files whole. `rg`, `fd`, `jq`, `mlr` are
on PATH (Homebrew). If one is missing, say so rather than falling back to `cat`.
- `GLOSSARY.md` is the project vocabulary: use its terms in names, comments and commit messages, and add a term there before inventing a new word.
- `docs/INDEX.md` indexes everything under `docs/` (9 reference documents, 128 journals
  and 23 data files as of 2026-10-30), grouped by what you want, with a `Superseded`
  section. Start there rather than guessing from filenames.
- `docs/journal/YYYY-MM-DD-*.md` are dated session records, and `docs/*.md` is the
  short reference set. A journal is history: open one only when `docs/INDEX.md`,
  `docs/RESUME-HERE.md` or the task points to it, and write a new session's record
  into `docs/journal/`, never into `docs/`.
- `registry/` holds 200+ assay YAMLs. Find entries with `rg` (e.g.
  `rg -l 'Canine distemper' registry/`) or run the validator; never open them in bulk.
- `docs/*.tsv` (master sheet, lab leads, validation cases): see columns with
  `mlr --itsv --opprint head -n 3 FILE`, then filter or count with `mlr`.
- `docs/papers-index.cache.json`, `docs/taxon-records.cache.json`,
  `docs/taxa-cache.json`: caches; query with `jq`. The last two are different
  things and must not be merged: `taxa-cache.json` is the lineage analysis's
  taxid -> name map (`config.yaml` `lineage.taxa_cache`).
- `papers/*.pdf`: locate the oligo table with
  `pdftotext FILE.pdf - | rg -n -i 'primer|probe|sequence'` before reading pages.
- `config.yaml` is long and heavily commented; read only the section for the
  threshold in question.

## Rules that the registry rests on
- Measure, never quote. `amplicon_bp` and oligo sequences are verified against
  real GenBank records and the cited paper's own table before entry.
- For SIZE specifically, the measurement also wins: where a measured product
  length and a published one disagree, the registry takes the measured value and
  discloses the difference (`amplicon_disagrees_with_paper`). A published size is
  usually a gel band read against a ladder; ours is computed from where the
  primers sit. The paper still says whether the length *varies*, which is what
  calls for `amplicon_bp_range`. Reasoning in `config.yaml` under `amplicon:`.
- No citation from memory. A DOI is entered with `doi_verified: false` and only
  Crossref, through `assaywatch curate` (or `scripts/resolve_citations.py`) and
  checked by `scripts/check_citations.py`, may approve it.
  If Crossref is unreachable, the entry waits.
- No scoring numbers in code. Thresholds live in `config.yaml`, with their
  justification (or the admission there is none) in comments.
- Only a maintainer sets `status: active`.

## Network and secrets
- Needs `eutils.ncbi.nlm.nih.gov`, `api.ncbi.nlm.nih.gov`, `api.crossref.org`,
  `api.unpaywall.org`, `api.openalex.org`, `www.ebi.ac.uk`. Cloud sandboxes have
  been blocked from these; run network steps on the Mac.
- NCBI key: `$NCBI_API_KEY` or `.secrets/ncbi.key`. Check with
  `assaywatch credentials`. Never print, log or commit a key.
- `papers/` holds copyrighted PDFs: gitignored, local only, never commit.

## Scratch, not source of truth
`data/retrieved/`, `results/`, `.snakemake/`, `snakemake*.txt`, `dryrun*.txt`,
`fetch*.txt` are gitignored run state and logs, not inputs.

## Cluster
`profiles/slurm/` runs the same Snakemake rules on SLURM. When suggesting a
cluster run, explain the job script / profile mechanics; Batya is learning HPC.

## Git
Commit messages state the finding, not the activity (see `git log`).
