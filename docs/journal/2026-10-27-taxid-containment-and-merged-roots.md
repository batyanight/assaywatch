# A scoped taxon can leave its retrieval root silently; the check for it found something else

2026-10-27. `scripts/check_taxids.py` compared each entry's `taxon_name` with NCBI's name
for its `taxid` and nothing more. The roadmap item behind this entry: *Mycoplasmopsis
agassizii* and *Mycoplasmoides testudinis* both left genus *Mycoplasma*, so a
genus-rooted retrieval stops fetching the organism an assay names and no check sees it,
because the genus still exists and still has its name.

    python scripts/check_taxids.py --registry registry --email <you> --quiet

## The check

`ESCAPED`: for every entry in `target.scope_taxids`, NCBI's `LineageEx` ancestor list
must contain the assay's `target.taxid`. Report only, like the rest of the script;
exit 1 on any hit.

**Its first run reported 4,113 escapes, and every one was wrong.** *Orthoflavivirus
dengue* was listed as "no longer inside 11051 (*Orthoflavivirus*)". It is inside it.
What had happened is that **11051 is a retired id**: NCBI merged it into 3044782, so
every child's ancestor list carries the new id and the registry's old root was never in
it. The herpesvirus family root (10292 → 3044472) did the same for 3,464 of the 4,113.
Containment is now tested against the canonical id of the root, and a merged root is
reported on its own line rather than as four thousand false escapes.

**Second run: 0 scoped taxa outside their retrieval root.** The Mycoplasma case that
motivated the check does not trigger it, and that is correct rather than a miss:
`MYCOPLASMA_16S_Turtles_only_Feldman_2006` is rooted at the phylum (544448) and selects
its three chelonian species by Entrez `query`, not by `scope_taxids`, and a species named
in a query is found wherever taxonomy files it. The check guards the shape of entry that
would be bitten; today none is.

## What it found instead

**18 entries carry a taxid NCBI has merged away** (`MERGED` lines):

| old id | now | entries |
|---|---|---|
| 11232 | 3052342 *Morbillivirus canis* | 9 CDV entries (Mueller 2011 ×4, Elia 2006, Halecker 2021 ×2, Scagliarini 2007, Geiselhardt 2022) |
| 121791 | 3052225 *Henipavirus nipahense* | `Nipah_N_gene`, `Nipah_N_gene_2` |
| 11051 | 3044782 *Orthoflavivirus* | `Pan_Flavivirus_NS5_gene`, `Pan_flavivirus_NS5_3_round1`, `_round2` |
| 10292 | 3044472 *Orthoherpesviridae* | `Pan_HERPES_dsDNA_Polymerase`, `_round2`, `_Terminase`, `_round2` |

Retrieval still works — esearch resolves a merged id — which is exactly why nothing
noticed. An entry carrying a retired id is one taxonomy release away from carrying
nothing. **Not fixed here, and the reason is cost, not doubt:** `data/retrieved/` is
keyed by taxid, so changing `target.taxid` moves the retrieval group and re-fetches the
archive — for the flavivirus root that is 29 MB and the whole history of a group, and
for CDV nine entries at once. It is a registry edit that must be made with a live run
and a `report_diff` behind it, not slipped in while one is in progress. ROADMAP carries
it with that cost named.

**11 `taxon_name` mismatches that predate today**, in two kinds:

- *ICTV binomial renames where NCBI's `OtherNames` does not carry the old common name*:
  `ABPV_capsid_Rossi_2024` (Acute bee paralysis virus → *Aparavirus apisacutum*),
  `BQCV_capsid_Rossi_2024` (Black queen cell virus → *Triatovirus nigereginacellulae*),
  `SBV_polyprotein_Rossi_2024` (Sacbrood virus → *Iflavirus sacbroodi*). The taxid is
  right; the stored name is the name the paper used. House pattern for this is the NCBI
  name with the paper's name in parentheses, and it changes no retrieval.
- *A species-level name on a genus-level taxid, scoped by query*: `LMBV_dsDNA_MCP_Grizzle_2003`
  (Largemouth bass virus on 10492 *Ranavirus*) and the seven
  `PROBOSCIVIRUS_POL_Latimer_2010_EEHV*` entries (EEHV3/4, 5, 6 on 548689
  *Proboscivirus*). These are the Mycoplasma shape exactly — the entry is deliberately
  rooted above its target and narrowed by query — and `MISMATCH` is the wrong word for a
  deliberate choice. They want either a `RANK`-style status that recognises "name is
  below taxid, and the query says so" or a note in the entry; the check cannot tell
  deliberate from wrong on its own.

The script exits 1 on these 11 as it always has. Nobody had run it since 2026-10-04.
