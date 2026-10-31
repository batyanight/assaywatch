# Only verified-DOI assays are live, and the seed list is gone (2026-10-23)

The registry was started from a lab primer list. That list was meant only as a
starting point for curation, and the pipeline was meant to stand on its own.
The 2026-10-20 cleanup removed the list's ordering flags and nothing else. Every
imported entry still named the list's file, carried its row numbers and the
lab's positive-control samples, and several held the lab's own notes. The README,
LICENSE-registry, CITATION.cff and CLAUDE.md all described the registry as
derived from it. The wave-5 session then treated this as a question of
permission to publish (`2026-10-23-wave5-ip-question.md`, now deleted). That was
the wrong question. Each entry's provenance is its own paper, and an entry that
has no paper is not published.

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

- `HANTAVIRUS_ssRNA_S_segment_2`, `HANTAVIRUS_ssRNA_S_segment_round2`, `HANTAVIRUS_ssRNA_S_segment_round2_2`
- `ENTEROVIRUS_ssRNA_5_UTR_VP4_VP2_round1`, `ENTEROVIRUS_ssRNA_5_UTR_VP4_VP2_round2`
- `PAPILLOMAVIRUS_dsDNA_L1_gene`
- `POXVIRUSES_dsDNA_Polymerase_short`, which was already `deprecated`. Its published
  sibling `_2` stays live.
- `Feline_Morbillivirus_L_gene`
- `POLYOMAVIRUS_dsDNA_VP1`
- `PARVOVIRUS_ssDNA_VP1_gene_pan_parvo`

`pending/README.md` gives the route back: find the paper, confirm the oligos,
let Crossref verify the DOI, then `git mv` the entry.

## What was removed

- **Schema.** `Source.spreadsheet`, `Source.rows` and `Source.positive_control`
  are gone. All three came from the list: its filename, its row numbers, and the
  lab's control samples, some with case numbers. `Source` is `Strict`, so these
  fields cannot come back by accident.
- **Registry data.** The list-sourced `source.notes` were stripped from 11 entries.
  These were the lab's verbatim comments, including case accessions and
  wet-lab experience. The stripping script checked that each file still parses
  to the original data minus those keys.
- **Free text.** About a dozen `as_written` values and curator notes named the lab,
  its staff or its controls. Each one was rewritten to cite the paper only, or
  "the seed list" where the curation history needs a referent.
- **Scripts.** The list importer, `apply_curation.py`, `curation.yaml`,
  `removed_assays/`, `removed_assays.txt` and `materials_needed.py` were deleted,
  with the materials TSV, its test and the `openpyxl` dependency (the `import`
  extra). Retrieval queries were unaffected. `curation.yaml`'s `queries` section
  was only ever the importer's input; each entry has carried its own
  `target.query` since the import.
- **Docs.** The README's import section became "Adding an assay". The
  LICENSE-registry carve-out, the CITATION.cff hold and the lab wording in dated
  docs are gone. The out-of-scope rule (host ID, barcoding, eDNA) still holds in
  CLAUDE.md and the README.

## Not done here

- **Git history** still holds the old wording. The decision is to leave this
  private repository's history alone and publish from a fresh repository made
  from a clean snapshot.
- `conda-lock.yml` still pins `openpyxl`. Regenerating the lock needs `conda-lock`
  and the network, and a dependency left in the lock does no harm in the
  meantime.
