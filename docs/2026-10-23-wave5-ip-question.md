# The WCS spreadsheet provenance question (2026-10-23)

`ROADMAP.md` has carried `IP question asked in writing` as an unticked Phase 0 item
since the repository was created. This records exactly what needs answering, what is
blocked until it is, and a draft to send. **Nothing has been sent yet** — the draft
below is for the maintainer to send, edit or discard.

## Why it blocks things

The repository is private today, so nothing is published and nothing is wrong. Four
things are waiting on it, and each would be hard to undo:

| blocked | why |
|---|---|
| making the repository public | 138 of 208 registry entries derive from an internal WCS Molecular Lab spreadsheet |
| a Zenodo DOI / `date-released` | a DOI is a permanent, citable assertion of redistribution rights (`CITATION.cff` now says this) |
| `LICENSE-registry` taking full effect | it currently offers CC-BY on the **curation** only, and excludes six entries by name |
| any paper describing the registry | a methods paper has to say where the assays came from |

## What is actually in question

Three distinct things, and they do not have the same answer:

1. **The 138 entries imported from the spreadsheet.** For most, the spreadsheet was a
   finding aid: the entry's oligos were verified against the cited paper's own table
   (`scripts/verify_oligos_against_paper.py`), and the sequences are facts published in
   that paper. The spreadsheet's contribution is the selection and the lab's annotations.
2. **Six entries whose oligos have no published source at all**, listed as
   `in-house-unpublished` in `docs/oligos-without-doi.tsv` (13 oligos):
   `Entamoeba_18S_small_subunit_SSU`, `Feline_Morbillivirus_L_gene`,
   `PAPILLOMAVIRUS_dsDNA_L1_gene`, `PARVOVIRUS_ssDNA_VP1_gene_pan_parvo`,
   `POLYOMAVIRUS_dsDNA_VP1`, `POXVIRUSES_dsDNA_Polymerase_short`. One records
   "Developed in house by" a named colleague. These are the lab's own unpublished
   design work, and publishing them without permission would be publishing someone
   else's unpublished result.
3. **The spreadsheet's own annotations** — which assay the lab ran for which target,
   positive controls, protocol notes. Some of this reached `source.notes_curator`.

## Draft (not sent)

> Subject: Permission to publish the assay registry derived from the Molecular Lab
> primer spreadsheet
>
> Dear [name],
>
> I have been building a tool called AssayWatch, which re-screens published PCR and
> qPCR assays against newly deposited GenBank sequences and reports when an assay's
> predicted coverage has fallen. The registry it works from started as the Molecular
> Lab's primer spreadsheet (`Primers_for_WCS_Molecular_Lab_updated_021518.xlsx`), which
> I used as the list of assays worth tracking.
>
> I would like to make the project public, and eventually to publish a short methods
> paper. Before I do either I want your decision in writing on three things.
>
> **1. The 138 assays imported from the spreadsheet.** For almost all of these the
> spreadsheet told me *which* assay to track and I then read the oligo sequences out of
> the published paper the assay comes from, verified the DOI against Crossref and
> measured the amplicon against real GenBank records. What I would be publishing is a
> curated list of already-published assays, plus my own verification. May I publish
> that, and how would you like the lab credited — as a data source in the paper's
> acknowledgements, as a co-author line, or not named?
>
> **2. Six assays with no published source.** These carry oligos recorded in the
> spreadsheet as in-house or unpublished, one of them attributed to a named colleague.
> I have listed them below. These are the lab's own unpublished design work and I will
> not publish them without explicit permission. The options as I see them: publish with
> an attribution you specify; hold them out of the public registry and keep them local;
> or publish them as part of a paper with the designer as a co-author. I am happy with
> any of the three, and the default if I do not hear back is to hold them out.
>
> [list the six entries]
>
> **3. The spreadsheet's own annotations.** Some of the lab's notes about which assay
> was used for which target are in my per-entry notes. If any of that is sensitive —
> for example anything about specific cases or submitters — tell me and I will remove
> it. I have not included anything about individual samples or animals.
>
> For context on what is being asked: the code would be MIT licensed, the registry
> CC-BY-4.0, and a public release would carry a permanent DOI, so this is a decision
> that is hard to reverse. I would rather wait for an answer than publish and
> apologise. If it is easier to discuss than to write, I am glad to, but I would like
> the decision itself in email so the project can record it.
>
> Thank you,
> Batya Nightingale

## Before sending

- Confirm the right recipient and whether institutional review, not just the lab, has
  to approve.
- Attach or inline the six entries' ids and oligo names from
  `docs/oligos-without-doi.tsv` (not the sequences, if that is the lab's preference).
- Check whether the registry's `source.notes_curator` contains anything about specific
  submissions; `scripts/materials_needed.py` and `docs/assay-master-sheet.tsv` are the
  places to look.

## When an answer arrives

Record it here with the date and the exact wording of the permission, tick
`ROADMAP.md`, update `LICENSE-registry`'s third bullet, and only then mint a DOI. If the
answer is "hold the six out", the mechanism already exists:
`scripts/curation.yaml`'s `exclude` section drops an assay from the registry on a
rerun of `apply_curation.py`, and `scripts/removed_assays.txt` is the record of what
was dropped and why.
