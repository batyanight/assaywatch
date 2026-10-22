# CLAUDE.md — AssayWatch

Context for Claude Code sessions. Read this, then `docs/RESUME-HERE.md` for where
work left off. Keep this file short; detail lives in the docs it points to.
Personal working preferences live in `~/.claude/CLAUDE.md`, not here.

## What this is
Continuous in-silico re-validation of published PCR/qPCR assays against newly
deposited GenBank sequences. One YAML per assay in `registry/`, a Python package
in `assaywatch/`, a Snakefile that runs retrieve -> screen -> drift -> report.
Full layout and usage: `README.md`. Plan and status: `ROADMAP.md`.

## Scope (decided, do not reopen)
- Pathogen assays only. Host barcoding (COI etc.), eDNA and host-ID assays are
  out of scope and stay out of `registry/` (see `scripts/removed_assays.txt`).
- Source registry: WCS Molecular Lab primer spreadsheet, plus literature additions.

## Commands
    conda activate assaywatch                      # environment.yml; package installed editable
    pytest -q && python -m assaywatch.validate registry
    ruff check . && ruff format --check .
    python scripts/check_citations.py              # CI runs this too
    snakemake -n                                   # dry run: prints the job plan, downloads nothing
    caffeinate -i snakemake --cores 4 --config email=you@example.org   # lid OPEN: -i does not stop clamshell sleep
    snakemake --profile profiles/slurm --config email=you@example.org   # same rules on SLURM
A change is not done until pytest, the validator, ruff and check_citations pass.
NCBI CLIs are in the env: `esearch | efetch` (Entrez Direct) and `datasets`
(NCBI Datasets). Prefer them for quick GenBank/taxonomy lookups over writing
one-off Python, and over asking Batya to download files by hand.

## Reading this repo cheaply
Search and summarise; don't read large files whole. `rg`, `fd`, `jq`, `mlr` are
on PATH (Homebrew). If one is missing, say so rather than falling back to `cat`.
- `docs/YYYY-MM-DD-*.md` are dated session records. Historical: open one only
  when `docs/RESUME-HERE.md` or the task points to it.
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
  `scripts/resolve_citations.py` + `scripts/check_citations.py` may approve it.
  If Crossref is unreachable, the entry waits.
- No scoring numbers in code. Thresholds live in `config.yaml`, with their
  justification (or the admission there is none) in comments.
- Only a maintainer sets `status: active`.

## Network and secrets
- Needs `eutils.ncbi.nlm.nih.gov`, `api.ncbi.nlm.nih.gov`, `api.crossref.org`,
  `api.unpaywall.org`, `api.openalex.org`, `www.ebi.ac.uk`. Cloud sandboxes have
  been blocked from these; run network steps on the Mac.
- NCBI key: `$NCBI_API_KEY` or `.secrets/ncbi.key`. Check with
  `python -m assaywatch.credentials`. Never print, log or commit a key.
- `papers/` holds copyrighted PDFs: gitignored, local only, never commit.

## Scratch, not source of truth
`data/retrieved/`, `results/`, `.snakemake/`, `snakemake*.txt`, `dryrun*.txt`,
`fetch*.txt` are gitignored run state and logs, not inputs.

## Cluster
`profiles/slurm/` runs the same Snakemake rules on SLURM. When suggesting a
cluster run, explain the job script / profile mechanics; Batya is learning HPC.

## Git
Commit messages state the finding, not the activity (see `git log`).
