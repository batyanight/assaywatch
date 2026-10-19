# What the per-lineage share counts as detected (step 2): experiment

**Date:** 2026-10-19
**Status:** experiment only; nothing shipped. Re-run after the `scope_taxids` fix
below, because the baseline it was measured against is biased.

## Question

`per_lineage_stats` counts `detect` and `reduced` as detected. Before the 2010-05-30
cutoff, the 2009 H1N1 Matrix records are 1,295 `reduced` and 1 `detect`. Slomka 2010
says efficiency fell outside acceptable limits, which is a failure for a qPCR. Does
counting `reduced` as not detected, for probe chemistries, recover the influenza
false negative, and what does it cost?

## Method

Tier-2 on `results/2026-10-17/calls.tsv.gz`. Old assay IDs were mapped to the
current ones with `docs/rename-mapping.tsv`. Variants were applied in a scratch
script by wrapping `AssayDrift._lineage_check` (relabel `reduced` as `fail` for the
chosen assays before the lineage grouping only; the pooled share is unchanged) and
by passing `assess()` an influenza resolver chain directly:

- **subtype:** `\((H\d+N\d+)\)` from the title.
- **pdm split:** subtype, but H1N1 with strain year >= 2009 (`/(\d{4})\(H1N1\)`)
  gets its own group. This stands in for pdm09; the subtype alone can't separate
  pdm09 from seasonal H1N1.

## Result (50 cases, 12 `fails`)

| variant | failures caught | `works` agree | disagreements |
|---|---:|---:|---:|
| baseline | 4 | 9 | 9 |
| flu split by subtype | 4 | 9 | 9 |
| flu split by subtype + pdm | 4 | 9 | 9 |
| detect-only for probe chemistries (44 assays), no split | 4 | 9 | 9 |
| **detect-only for probe chemistries + flu pdm split** | **5** | 9 | **8** |
| detect-only for every assay | 4 | 8 | 10 |

The combination is the only variant that changes a probe case. It flips Influenza
Matrix 2003 (2010-05-30) from `stable` to `declining`, which agrees with Slomka.
Applying detect-only to every assay adds a false alarm (Adenovirus Pan Polymerase
round2, a `works` case).

Cost outside the validation set (current statuses as of 2026-10-17, baseline vs
the combination): 6 of 212 assays change, all to `declining`:

| assay | chemistry | was | worst lineage, detect-only |
|---|---|---|---|
| CBPV_RNA1_Rossi_2024 | mgb | stable | taxid 180822, 38/47 |
| CDV_N_gene_Elia_2006 | hydrolysis_probe | watch | taxid 3052342, 51/88 |
| DWVB_polyprotein_Rossi_2024 | mgb | watch | taxid 2498590, 23/34 |
| INFLUENZA_A Matrix 2003 | mgb | stable | H3N2, 46/15,326 |
| MONKEYPOX_N3R_MGB_Kulesh_2004 | mgb | stable | taxid 10244, 533/2,338 |
| SBV_polyprotein_Rossi_2024 | hydrolysis_probe | watch | taxid 89463, 23/40 |

## Reading

One validation case gained, and six unvalidated verdicts moved. Only 6 of the 50
cases are probe chemistries, so the validation set can't say whether those six
are correct alarms or false ones. `reduced` is a penalty band (mismatches that
cost efficiency), and for many probe assays it means a Ct shift, not a missed
sample (Stadhouders 2010). Don't ship it into the verdict on this evidence.

Before deciding:
1. Add `works` and `fails` cases for probe/qPCR assays, especially the six above:
   current influenza M-gene, Kulesh MPXV N3R, and the Rossi 2024 bee-virus panel.
2. Consider reporting the detect-only lineage share in `lineage.md` as a diagnostic
   rather than a verdict input.

## Found while doing this

- **12 assay IDs in `docs/validation-cases.tsv` had been renamed** by the
  2026-10-18 primer-name audit (13 rows). Fixed. On the next pipeline run those
  cases would have gone silently to "no data". `scripts/populate_scope_taxids.sh`
  also pointed at the old CDV filename.
- **`scope_taxids` exact matching excludes most in-scope records.** Records at strain
  and no-rank taxids under a listed species (e.g. 3139435 "canine distemper virus"
  under 3052342 *Morbillivirus canis*) are dropped. In every scoped assay most
  excluded records are such descendants: Pan-flavivirus NS5 round1 keeps 498 and
  drops 31,756, all descendants. Enterovirus round2 keeps 259 and drops 23,868,
  23,829 of them descendants. CDV P gene keeps 0 of 604, because its scope taxid
  11232 has been merged into 3052342 at NCBI. Every tier-2 number since
  scope_taxids landed (including the 14 -> 9 disagreements) was measured on these
  leftovers.
