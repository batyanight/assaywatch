# scope_taxids: ancestry matching

**Date:** 2026-10-19
**Change:** a record is in scope when its taxid **or any ancestor** is in the assay's
`scope_taxids`, with merged taxids followed on both sides
(`assaywatch/taxonomy.py`, tree in `docs/taxonomy-cache.json.gz`, built by
`scripts/build_taxonomy_cache.py`; `drift.scope_taxonomy` in `config.yaml`).

## The bug

`scope_taxids` lists species. Matching was exact, so a record annotated below
species rank was excluded: a strain, or since NCBI moved virus species to binomial
names, a no-rank child that keeps the old common name (3139435 "canine distemper
virus" under 3052342 *Morbillivirus canis*). Excluded records over all time, on the
2026-10-17 calls:

| scoped assay | excluded, exact | excluded, ancestry |
|---|---:|---:|
| ADENOVIRUS_dsDNA_Pan_Polymerase_round1 | 30,855 | 159 |
| CDV_P_gene_Scagliarini_2007 | all (scope 11232 merged) | 0 |
| CORONAVIRUS RdRp Lan 2010 round1 / round2 | 12,067 | 203 |
| ENTEROVIRUS_ssRNA_VP3_VP1_round2 | 71,569 | 40 |
| POLYOMAVIRUS_dsDNA_VP1_Johne_2005 | 6,848 | 5 |
| Pan_Flavivirus_NS5_gene, NS5_3 round1 / round2 | 58,478 | 1 |
| Pan_HERPES Polymerase / round2 | 5,673 | 2 |
| Pan_HERPES Terminase / round2 | 3,566 | 1 |
| Paramyxovirinae_Polymerase_L_gene_Tong_2008_round1 | 11,431 | 73 |

The tree covers every taxid in the archives and the registry: 110,814 requested,
113,553 parent links, 4 merges, 0 missing. The four merges are 10292 -> 3044472
(Orthoherpesviridae), 11051 -> 3044782 (Orthoflavivirus), 11232 -> 3052342
(*Morbillivirus canis*) and 121791 -> 3052225 (Nipah). Only CDV P gene used a merged
id inside `scope_taxids`; it is now `[3052342]`. Eighteen assays use one as
`target.taxid`, which is the retrieval key. They are left alone: NCBI resolves the
merge (`txid11232[Organism:exp]` and `txid3052342[Organism:exp]` both return
4,080 nuccore records).

## Tier-2, same evidence (2026-10-17 calls, renamed IDs)

| scope | failures caught | `works` agree | disagreements | undecided |
|---|---:|---:|---:|---:|
| exact | 5/12 | 10 | 9 | 17 |
| ancestry | 6/12 | 9 | **14** | 17 |

The 2026-10-18 result "scope_taxids took disagreements 14 -> 9" was measured on
the ~10% of in-scope records annotated at exactly species rank. With all of them
counted, five pan-family `works`/`partial` cases turn `declining`. They share one
mechanism: the pooled status is `low coverage` (the assay never covered that
diversity), and the lineage override turns it into `declining` because one lineage
is at 0%. Examples: Pan-flavivirus NS5 against Zika (taxid 64320) at 0/262, and
Pan-herpes polymerase round2 against taxid 10359 at 0/52. Paramyxovirinae Tong
round1 (`fails`, 2019) is caught for the first time, at a pooled 18% of 1,056.

Restricting the override to pooled `stable`/`watch` is not the fix. It brings the
disagreements to 10 but caught failures to **1/12**, because Forslund, Hellgren
and Pan-Plasmodium are caught by the same `low coverage` -> `declining` path. The
tool can't currently tell "a lineage the assay is meant to detect, and misses"
from "diversity it never covered". That is a question about the estimand and about
what each validation case's `expect` means for a pan-family assay, not a rule tweak.

## Also noticed

- An assay whose every record is out of scope drops out of `assess()` altogether
  and reads "no data", instead of reporting 0 in scope. That is how CDV P gene
  disappeared. A test now pins the behaviour.
- `sitedrift.py` calls `assess()` without taxids or scope, so the site-drift page
  selects assays by a status that can differ from the report's.
