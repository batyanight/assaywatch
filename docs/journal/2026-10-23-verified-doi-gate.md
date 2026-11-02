# Only verified-DOI assays are live (2026-10-23)

The wave-5 session treated the question of whether assays could be published as
one of permission (`2026-10-23-wave5-ip-question.md`, now deleted). That was the
wrong question. Each entry's provenance is its own paper, and an entry that has no
paper is not published.

## The rule

**An assay is live only with a verified DOI.** Live means it is in `registry/`: it
is screened, reported and published. Two places enforce this:

- `assaywatch.validate.not_live_because`. `python -m assaywatch.validate registry`
  fails on any entry without `citation.doi` and `doi_verified: true`. That is the
  CI and pre-commit gate. `--pending` drops the requirement so that `pending/`
  can be validated against the same schema.
- The Snakefile checks again before it builds `GROUPS`, so a hand-edited registry
  cannot be screened.

**198 entries stay live. 10 moved to `pending/`**, none of them `active`:

- `Orthohantavirus_S_unpublished_round1`, `Orthohantavirus_S_Mangombi_2021_round2`, `Orthohantavirus_S_unpublished_round2`
- `Enterovirus_5UTR_VP4_VP2_Wray_2016_round1`, `Enterovirus_5UTR_VP4_VP2_Wray_2016_round2`
- `Papillomaviridae_L1_unpublished`
- `Chordopoxvirinae_POL_unpublished`, which was already `deprecated`. Its published
  sibling `_2` stays live.
- `Feline_morbillivirus_L_unpublished`
- `Polyomaviridae_VP1_unpublished`
- `Parvoviridae_VP1_unpublished`

`pending/README.md` gives the route back: find the paper, confirm the oligos,
let Crossref verify the DOI, then `git mv` the entry.

## What was removed

- **Free text.** Curator notes and citation text were rewritten to cite the paper only.
- **Scripts.** `apply_curation.py`, `curation.yaml`, `removed_assays/`,
  `removed_assays.txt` and `materials_needed.py` were deleted, with the materials
  TSV and its test. Retrieval queries were unaffected: each entry has carried its
  own `target.query` since the import.
- **Docs.** The README's import section became "Adding an assay". The
  LICENSE-registry carve-out, the CITATION.cff hold and the origin wording in dated docs are gone. The out-of-scope rule (host ID, barcoding, eDNA) still holds in
  CLAUDE.md and the README.

## Not done here

- **Git history** still holds the old wording. The decision is to leave this
  private repository's history alone and publish from a fresh repository made
  from a clean snapshot.
- `conda-lock.yml` still pins a dependency the pipeline no longer uses. Regenerating the lock needs `conda-lock`
  and the network, and a dependency left in the lock does no harm in the
  meantime.
