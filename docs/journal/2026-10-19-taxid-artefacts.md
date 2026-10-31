# Taxid artefacts in lineage grouping (2026-10-19)

Follow-up to `docs/journal/2026-10-19-pan-family-cases.md`, which left two disagreements
firing on taxids that "only look new": Polyomavirus Johne on 1891763 and
Enterovirus VP3/VP1 round2 on 1193974. **Evidence:** `results/2026-10-17/calls.tsv.gz`
with assay IDs mapped through `docs/rename-mapping.tsv` (as before), working-baseline
gate on, taxonomy cache rebuilt today with ranks.

## What the two taxids are

**1891763 is JC polyomavirus under a second taxid.** It is the species
*Betapolyomavirus secuhominis*. Older JCPyV records carry 10632 "JC polyomavirus"
(no rank), its child. For Johne 2005, 10632 is 0% detected in every deposit year
1989-2025 (about 3,000 evaluable records, 7 detected), so the gate correctly
excuses it as never covered. 1891763 appears only from 2018 (0/56, 0/7), so as a
separate lineage it had no earlier measured year and passed as new to the archive.

**1193974 is a bucket.** "Human enterovirus", rank species, sits under the no-rank
node "unclassified Enterovirus". For VP3/VP1 round2 its 33 records from 2018
(0% detected) are one Xiamen CDC batch, isolates sampled 2009-2015, every name
ending `-CA6`: coxsackievirus A6 filed untyped. Under its own taxid 86107, CVA6
has been measured since 2013 and is all but never covered (0/68 in 2013, 0/59 in
2014, 0/79 in 2017; 50/132 in 2018 is the exception).

Same mechanism both times: one virus under two taxids, so exact-taxid grouping
gives one copy a fake "new lineage" pass through the gate.

## What changed

- `scripts/build_taxonomy_cache.py` stores ranks (25,346 non-"no rank" nodes) and
  the names of the 363 "unclassified ..." nodes. Parents are unchanged (113,553).
  Cache 322 KB -> 394 KB. All names would have been 1.4 MB.
- `Taxonomy.species_of` and `Taxonomy.in_unclassified`.
- `lineage.group_at_rank: species` (**on**): a record's taxid is rolled up to its
  species-rank ancestor before lineage grouping.
- `lineage.unclassified_is_bucket` (**off**): under the gate, a lineage under an
  "unclassified" node cannot pass as new.
- `_lineage_check`: one lineage that holds every recent record, in an assay that
  never cleared the threshold in an earlier year, does not override. See West Nile.

## Tier-2

| variant | failures caught | disagreements | moved |
|---|---:|---:|---|
| exact taxid (before) | 4/11 | 13 | |
| species roll-up, no whole-pool rule | 4/11 | 13 | Johne fixed; West Nile Lanciotti 2001 (2003, `works`) weaker -> declining |
| + whole-pool rule (all lineages) | 3/11 | 13 | West Nile back to weaker; CDV Scagliarini 2021 lost |
| + whole-pool rule, never-worked only (**shipped**) | **4/11** | **12** | Johne fixed, nothing else |
| bucket rule, either grouping | unchanged | unchanged | |

**West Nile vs CDV.** Rolled up, each is one species: one lineage that is nearly the
whole pool, pooled `low coverage`. CDV used to work (baseline 87%, a year above
threshold), so its catch is the "worked, now failing" path and is kept. West Nile
never cleared the threshold (baseline 53%) and passed as "new" only because its
early years were thin. The lineage check adds nothing when the lineage is the
pool, so for a never-worked assay it no longer overrides. With exact taxids the
rule changes no tier-2 row.

**Why the bucket rule is off.** It removes 1193974, and then the next lineage down
drives `declining` (taxid 12074 at 79.7%; rolled up, *Enterovirus betacoxsackie* at
28.8%). This case disagrees because pooled detection is 10.7% and a failing lineage
overrides a pooled `low coverage`, the pan-family estimand question that is still
open. The bucket artefact is real but is not what decides this case.

## Current statuses (2026-10-17 calls, as of 2026-10-17)

Four of the 201 current assays scored move. (The 2026-10-17 calls predate the
`de06851` registry purge. The copy used here mapped the 27 renamed IDs but kept
12 of the 13 removed assays. One of them, CDV F gene "need_to_order_2", also
moved, and is left out here. Tier-2 is unaffected: no validation case names a
removed assay.)

- `low coverage` now, with the gap named: Adenovirus Hexon round2 (was watch),
  Paramyxovirinae Tong round1 (was declining on 11224; now names species 3049953,
  548 records, 0%), Poxviruses Polymerase (was declining at 4.0%).
- `declining` now: **Orthopoxvirus ATI Meyer 1997** (was stable at 95.3% pooled).
  Vaccinia strain taxids, each below the per-lineage floor before, roll up to
  10245: 112 records at 83.0% (76-90%). Worth looking at by hand, not suppressing.

## Next

- Orthopox ATI on vaccinia: which strains fail, and where in the ATI amplicon.
- The pan-family `low coverage` -> `declining` override (enterovirus round2 is the
  clearest case; it is also why the bucket rule had nothing to fix).
