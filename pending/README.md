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

1. Set `citation.doi` and leave `doi_verified: false`.
2. Run `assaywatch curate pending/<id>.yaml --email you@example.org`. It fetches
   the paper when an open copy exists, judges every oligo against what the paper
   prints, and sets `doi_verified: true` itself when Crossref agrees with the
   reference. Crossref is the only thing that may set that field. Clear the
   "Left for a human" list it prints.
3. `git mv pending/<id>.yaml registry/` and run the validator on `registry/`.

An entry with no published source stays here. It never goes live.
