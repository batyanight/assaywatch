# 2026-11-05 — next-run edits, and the Chlamydia assembly check that failed

**Finding: adding *Chlamydia* assemblies would double count, so the maintainer decided against them. Measuring it also found RefSeq and GenBank copies of one genome counting as two records in
17 of 219 assays.** The other decided edits are in. Nothing here has been screened, so no number on the
site moves until the next run.

## *Chlamydia* assemblies: not applied

Under taxid 810, NCBI Datasets lists 493 assemblies at complete or chromosome level. The archive's
`"complete genome"[Title]` term already reaches 379. Assembly records use GCA ids and nuccore records use
CP ids, so nothing would catch the overlap. 114 are missing: 70 chromosome level and 44 complete, 42 of
them *C. trachomatis*.

## RefSeq twins

`NZ_CP017733` and `CP017733` are one genome. Pairs on the 2026-11-01 calls:

| assay | pairs | records |
|---|---|---|
| *Mycoplasma* 16S, four entries | 1,651 | 24,246 |
| MTB IS6110 | 477 | 4,811 |
| MTB IS1081 | 377 | 1,468 |
| *Leptospira* lipL32 | 194 | 2,822 |
| Mycoplasmatota 16S | 168 | 528 |
| Messmer round 1 | 127 | 1,668 |

The effect on verdicts is not measured. It's on the roadmap.

## Entered

- **Zimmermann round 2.** Stores `GCCTTGTGTTTCTATGTTTG`, with the printed form in `modified_from`. New
  field `print_error`, valid only with `oligo_sequence_uncertain`, so the status stays withheld. This is
  the one exception to published sequences only, by maintainer decision. `amplicon_bp` is 441, from all
  248 records with exact sites, M99375 included.
- **FT443.** Long 1993 tails it with digoxigenin and reads a dot blot, so a new chemistry
  `hybridization_probe` holds it. The penalties are an assumption, and the probe is exact in all 1,021
  products.
- **Li 2010 IMV.** `txid10270` joins the query. Crocodilepox was already in RPO147's query: the 2026-11-04
  journal line is wrong.
- **Lozano and Li IMV notes** corrected against the papers.
