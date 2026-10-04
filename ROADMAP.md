# Roadmap

Scope for v0.1 is frozen in the build plan; new ideas go here, not into the sprint.

## Phase 0 (current)
- [x] repo, environment.yml, pre-commit, CI
- [x] YAML schema (pydantic) and validator
- [x] registry imported from the WCS spreadsheet (138 pathogen assays; 38 host/barcoding/universal primers excluded as out of scope)
- [ ] 5 assays promoted to `active`: Bd (Boyle 2004), Bsal (Blooi 2013), Oo ITS2 (Bohuski 2015), ranavirus MCP (Pallister 2007), CDV P (Scagliarini 2007)
- [ ] run `scripts/resolve_citations.py` once; review BAD lines
- [ ] name, license (MIT code / CC-BY registry), IP question asked in writing

## Phase 1: core pipeline
- [x] `match`: exhaustive vectorised search, both strands, held to brute force in tests
- [x] `score`: position-weighted penalty from config.yaml, five-way call per record
- [x] three-state base comparison: degeneracy and undetermined record bases cost nothing
- [x] inosine handled as a single promiscuous molecule, not as N
- [x] degeneracy accounting reported next to the drift signal, never scored
- [x] `screen` CLI: assays x FASTA -> TSV of calls
- [x] synthetic fixture set with hand-derived expected calls (61 records, 5 assays)
- [x] `retrieve`: Entrez esearch/esummary/efetch per taxid, mdat-filtered, gzip archive + manifest
- [x] wire the stages into a Snakefile with a checkpoint; SLURM profile
- [x] first live NCBI dry run (2026-10-03): 28 taxa fetchable whole, 19 needed gene-targeted queries
- [x] first live fetch (2026-10-03): 25 taxa, ~470k records, 1.1 GB; fixed dropped connections on genome-sized pages and expired history handles
- [x] gene-targeted retrieval groups; per-group screening
- [ ] dry-run the 19 gene-targeted groups and decide which to opt past the cap
- [x] `drift`: Wilson / Newcombe intervals, minimum-evidence guard, evaluable denominator
- [x] `report`: markdown + self-contained HTML, per-year tables, coverage-gap table,
      degeneracy note beside the coverage trend
- [ ] parasail gapped local alignment as an option, if indel-containing records turn out to matter

## Later
- assembly-level retrieval for bacterial targets (NCBI Datasets: sample N assemblies per year,
  extract the locus); nuccore gene-level deposits stop at roughly 2012 for enteric bacteria
  and the WGS contigs that replaced them are excluded from retrieval by title
- optional thermodynamic score column (primer3-py)
- SLURM executor profile for Greene
- contributor template, two-week review promise
