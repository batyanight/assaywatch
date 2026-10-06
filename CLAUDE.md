# CLAUDE.md — AssayWatch

Context for Claude Code and Cowork sessions. Read this, then `docs/RESUME-HERE.md`
for where work left off. Keep this file short; detail lives in the docs it points to.

## What this is
Continuous in-silico re-validation of published PCR/qPCR assays against newly
deposited GenBank sequences. One YAML per assay in `registry/`, a Python package
in `assaywatch/`, a Snakefile that runs retrieve -> screen -> drift -> report.
Full layout: `README.md`. Plan and status: `ROADMAP.md`.

## Scope (decided, do not reopen)
- Pathogen assays only. Host barcoding (COI etc.), eDNA and host-ID assays are
  out of scope and stay out of `registry/` (see `scripts/removed_assays.txt`).
- Source registry: WCS Molecular Lab primer spreadsheet, plus literature additions.

## Environment
    conda activate assaywatch          # environment.yml; package installed editable
    pytest -q && python -m assaywatch.validate registry
    ruff check . && ruff format --check .
NCBI CLIs are in the env: `esearch | efetch` (Entrez Direct) and `datasets`
(NCBI Datasets). Prefer them for quick GenBank/taxonomy lookups over writing
one-off Python, and over asking Batya to download files by hand.
CI (`.github/workflows/validate.yml`) also runs `python scripts/check_citations.py`.
A change is not done until all of these pass.

## Rules that the registry rests on
- Measure, never quote. `amplicon_bp` and oligo sequences are verified against
  real GenBank records and the cited paper's own table before entry.
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

## Gitignored scratch
`data/retrieved/`, `results/`, `.snakemake/`, `snakemake*.txt`, `dryrun*.txt`,
`fetch*.txt`. Don't treat these as source of truth for anything committed.

## Cluster
`profiles/slurm/` runs the same Snakemake rules on SLURM. When suggesting a
cluster run, explain the job script / profile mechanics; the user is learning HPC.

## Working with Batya
- Expert in molecular diagnostics and PCR; learning Python, stats and
  bioinformatics methods. Explain why code works and define jargon.
- When a file changes, give the complete updated file, never a partial diff to
  apply by hand. One command block to run at a time.
- Blunt, no filler. Commit messages state the finding, not the activity
  (see `git log`).
