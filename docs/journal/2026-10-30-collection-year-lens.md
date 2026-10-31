# The collection-year lens: on this archive the backlog changes the denominator, not the share

2026-10-30. Built as decided that evening (`2026-10-30-design-grilled.md` Q1 to Q3): not a
`drift.window_on` switch but a report-wide section that re-dates every assembly record by the
year it was collected and recomputes the recent share beside the deposit-clock one. The
verdict is untouched; both columns are the same plain pooled year-granularity window over the
same asm rows, so they differ by the clock and nothing else.

## What changed in the code

- `assemblies.py` writes a `collected` metadata column, the BioSample collection date as
  given. The title keeps "; collected X" so older readers still work.
- `metadata.collection_year()` keeps only a four-digit year (ISO prefixes and
  `13-May-2010`); "missing", "not collected" and ranges such as `2010/2011` are undatable,
  by decision. `metadata.read_collection_years()` reads the column where there is one and the
  title tail where there is not, for `asm/` archives only.
- `report.collection_lens_rows()` and `LensRow`; `lens_section_md` and the HTML block, both
  rendered from one `lens_cells()` so the two documents cannot differ. The section appears
  only when the calls table holds `GCA_`/`GCF_` records.
- Three glossary terms: deposit date, collection date, collection-year lens.

## What it says on the 2026-10-27 run

2,988 asm rows over 13 assays. Of the records behind them, between 56% and 85% carry a
collection year (E. coli 204 of 325, Leptospira 123 of 144, Salmonella 219 of 304).

| assay | asm records | with collection year | recent share by deposit year | recent share by collection year | gap |
|---|---|---|---|---|---|
| `E_coli_ETEC_LT_Victor_1991` | 325 | 204 | 0.0% of 1 | no recent records | - |
| `E_coli_O157_hlyA_Wang_1997` | 325 | 204 | 100.0% of 4 | no recent records | - |
| `E_coli_malB_Candrian_1991` | 325 | 204 | 56.7% of 60 | 64.0% of 25 | +7.3 points |
| `LEPTOSPIRA_lipL32_Ahmed_2020` | 144 | 123 | no recent records | no recent records | - |
| `LEPTOSPIROSIS_Flagillar_filiment_Prote` | 144 | 123 | 100.0% of 38 | 100.0% of 16 | +0.0 points |
| `MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018` | 289 | 197 | 100.0% of 55 | 100.0% of 25 | +0.0 points |
| `MYCOBACTERIUM_TB_complex_IS6110_Boniotti_2014` | 289 | 197 | 100.0% of 54 | 100.0% of 25 | +0.0 points |
| `MYCOBACTERIUM_TB_complex_helicase_MTCHeli_Hermes_2018` | 289 | 197 | 100.0% of 57 | 100.0% of 25 | +0.0 points |
| `MYCOBACTERIUM_genus_16S_rRNA_Hermes_2018` | 305 | 197 | 100.0% of 57 | 100.0% of 22 | +0.0 points |
| `Salmonella_invA_Rahn_1992` | 304 | 219 | 100.0% of 60 | 100.0% of 21 | +0.0 points |
| `Shigella_ipaH_Sethabutr_1993` | 173 | 107 | 100.0% of 54 | 100.0% of 18 | +0.0 points |
| `Yersinia_enterocolitica_Ibrahim_1992` | 35 | 23 | 100.0% of 15 | 100.0% of 4 | +0.0 points |
| `Yersinia_pseudotuberculosis_Wang_1997` | 41 | 21 | 100.0% of 16 | 100.0% of 3 | +0.0 points |


**The share barely moves; the sample does.** Every assay at 100% by deposit year is 100% by
collection year. The one assay with a real recent fall, `E_coli_malB_Candrian_1991`, reads
56.7% of 60 by deposit and 64.0% of 25 by collection: a 7-point gap on a quarter of the n,
inside the deposit clock's own interval. What the lens shows instead is how much smaller the
"recent" set is once a record is dated by when its isolate existed: 60 to 25 for E. coli, 55 to
25 for the MTC assays, 60 to 21 for Salmonella. So for these bacterial targets the backlog
signal measured on 2026-10-27 (median lag 5 years) does not manufacture a decline; it inflates
the recent denominator with isolates from the past, which makes the verdict's interval
narrower than the biology warrants. That is the same shape as the duplication finding, from
the other side.

Two rows show the lens's own limit: ETEC LT and O157 hlyA have 1 and 4 evaluable recent
records by deposit and none by collection year, because the recent-by-collection window is
2024 onward at year granularity and almost nothing collected since 2024 has been assembled
and deposited yet. A collection-dated window is structurally late by exactly the backlog.

## What was not done, on purpose

Nuccore records (99.9% of calls) carry no collection date in `esummary`; `/collection_date`
is a source-feature qualifier, so bringing them into the lens is a retrieval change plus a
re-fetch of every archive. Priced separately, if at all. The lens did not need a config key
and got none; nothing in the screen hash's closure moved, so the Sunday run is unaffected.
