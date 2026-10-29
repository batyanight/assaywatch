# pending/

Assay entries that are **not live**: they have no DOI that Crossref has confirmed,
so the pipeline never screens them, the report never lists them, and they are not
part of the published registry.

The rule is enforced in two places. `assaywatch validate registry` fails
on any entry without `citation.doi_verified: true`, which is the CI and pre-commit
gate. The Snakefile repeats the check before planning a run.

These entries use the same schema as `registry/`, and are checked with

    assaywatch validate pending --pending

## How an entry goes live

1. Find the paper that prints the oligos, and confirm every sequence against its
   own table (`scripts/verify_oligos_against_paper.py --assay <id>`).
2. Set `citation.doi` and leave `doi_verified: false`.
3. Run `python scripts/resolve_citations.py --registry pending --email you@example.org`.
   Crossref is the only thing that may set `doi_verified: true`.
4. `git mv pending/<id>.yaml registry/` and run the validator on `registry/`.

An entry with no published source stays here. It never goes live.
