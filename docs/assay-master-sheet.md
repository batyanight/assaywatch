# Assay master sheet

`assay-master-sheet.tsv` has one row per assay, 172 rows and 34 columns. Open it in a spreadsheet; this page is the key and the caveats.

Regenerate after any registry change:

```bash
python scripts/master_sheet.py
```

## Where each column comes from

| source | columns |
|---|---|
| `registry/*.yaml` | ids, gene, taxid, scope, chemistry, amplicon, oligos, flags |
| Crossref (`papers-index.cache.json`) | year, first author, journal, title |
| NCBI Taxonomy (`taxa-cache.json`) | scientific name, common name, rank |
| last verification run | `sequence_verification` |
| computed | `degeneracy_fold`, `degeneracy_tier`, `retrieval_group` |

Nothing is filled in from memory.

## Two columns that need reading carefully

**`taxon_common_name` is NCBI's, and is blank for most rows (12 of 172 have one).** A blank means NCBI publishes no common name for that taxid, not that none exists. It is left blank on purpose: a plausible common name invented to fill the cell would be indistinguishable from a real one.

**`taxon_name_differs` marks the 2 rows where NCBI's current scientific name is not the name the registry entry carries.** These are ICTV renames that propagated into NCBI - Herpesviridae became Orthoherpesviridae, Canine morbillivirus became Morbillivirus canis. The taxid is unchanged and is what retrieval uses, so screening is unaffected; both names are kept because a reader searching either one should find the assay.

## Scope

`scope_query` is the Entrez term ANDed onto the taxon, i.e. which loci are actually pulled from GenBank. 65 of 172 assays have one; the rest are screened against their whole taxon. `retrieval_group` is `taxid/slug`, and assays sharing a group share one archive, so changing a query splits an assay off into its own fetch.

## Verification and flags

`sequence_verification` counts how each oligo fared against its own paper: `exact` means found inside an oligo the paper lists, `in-text` means found somewhere in the paper but not in a listed oligo, `absent` means not found, and `no-full-text`/`no-doi` mean it could not be checked at all. Blank means the entry was added after the last run.

`needs_review` is non-empty for 116 of 172 assays. A flag is a known, recorded caveat, not a defect to hide.
