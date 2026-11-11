# The frozen run, checked: ten status moves, every one with its cause, and one real catch

2026-11-11, step 14 of the v0.3.0 release plan. The run is `results/2026-11-10/`, started
21:43 on 2026-11-10 after a first attempt died at 32 minutes, finished 01:52, 4 h 8 min
of wall time, `status: success`, 664 of 664 steps. Checked against `results/2026-11-01/`.

## The run itself

- **The first attempt died at 32 minutes and it was NCBI, not this code.** `esearch` returned
  "Search Backend failed" on 45 of 147 retrieval groups. The same taxon answered HTTP 200
  minutes later. Nothing was lost: Snakemake discarded the one partial output and the 32
  groups already fetched were kept, and the restart added `--retries 3` on the command line
  (not in the Snakefile, which was frozen) so a transient NCBI failure retries instead of
  ending a five-hour job. The restart had zero errors.
- **Retrieval took 74 minutes, not the roadmap's 50**, because two groups had no previous
  archive and fetched from scratch: Chordopoxvirinae under its new Leporipoxvirus query (about
  900 MB, the siblings under the same taxon being 945 and 926 MB) and a Mycobacterium group.
  The other 149 groups were incremental; 63 wrote a new archive and 88 had nothing new.
- **Composition took about 2 h 15 min at a 5.1 GB peak observed**, against the 4 h 10 min and
  12.1 GB measured on 2026-11-01. Faster and smaller than declared; the declaration stands.
- **The machine was on battery by the maintainer's decision** for the first 2 h 20 min, then on
  mains. It did not matter, and it could have.
- **The reference cache answered all but 6 spike batches** (`references-missing.txt`:
  DQ177235, LC782778, OR361515, OR361538, PV872084, PZ806872). Those six spike sentences omit
  their study clause this release. The next warming pass picks them up.

## The status diff, attributed

| 2026-11-01 | 2026-11-10 |
|---|---|
| 95 stable, 34 declining, 26 low coverage, 26 insufficient data, 16 no recent data, 5 watch | 92 stable, 31 declining, 21 low coverage, 32 insufficient data, 15 no recent data, 6 watch |

Ten assays changed status. Seven were expected from the fixes, two follow from a scope
broadened on rereading, and one is new data.

| assay | move | cause |
|---|---|---|
| `Vibrio_coralliilyticus_vcpA_Wilson_2013_vcpAF` | stable → insufficient data | **step 1**, RefSeq twins: predicted on 2026-11-06 |
| `Vibrio_coralliilyticus_vcpA_Wilson_2013_vcpARTF` | stable → insufficient data | **step 1**, same |
| `Orthobunyavirus_S_Briese_2007_BUNS_5_U_6` | low coverage → insufficient data | **step 1**, predicted |
| `Serpentovirinae_PP1b_Uccellini_2014_PythonNido6F` | low coverage → insufficient data | **decided 2026-11-04**: narrowed to ball python nidovirus, predicted to read exactly this |
| `Serpentovirinae_PP1b_Uccellini_2014_PythonNodoF` | low coverage → insufficient data | same |
| `Haemosporida_cytb_Hellgren_2004_HaemF` | low coverage → stable | **step 2**: 480 → 525 bp, the primers-excluded size, so the real products are inside the window |
| `Leucocytozoon_cytb_Hellgren_2004` | declining → stable | **step 2**: 478 → 524 bp, the same fix |
| `Batravirus_terminase_Licheri_2020_pan` | no recent data → insufficient data | **step 3**: RaHV-5 joined the scope and the retrieval moved to the order, so recent records exist but fewer than 15 |
| `Deformed_wing_virus_B_polyprotein_Rossi_2024` | declining → watch | **step 6a**: retrieval moved to the species node with *Varroa destructor virus 1* in scope, which the paper equates with DWV-B; 16 → 22 recent records, 75.0% → 81.8%, and the interval now reaches 90% |
| `Morbillivirus_P_Barrett_1993_Grosh_F` | stable → declining | **new data, see below**: nothing that screens changed on this entry |

Six left the report and one joined it, all by decision: `Dependoparvovirus_VP1_Gao_2002_2` and
`Morbillivirus_P_Barrett_1993_MorbF` are the two duplicates step 6b withheld; the two Keele
2009 entries and `West_Nile_virus_E_Lanciotti_2001` are the three step 6a withheld;
`Sarcocystis_18S_5_8S_Kutkiene_2010_ShortITS1R` went to `pending/` before this release; and
`Francisella_tularensis_tul4_Long_1993` appears for the first time because FT443 is stored and
its withholding flag is off.

## The catch: Barrett 1993's P-gene primers miss the 2025 European PPRV genomes

`Morbillivirus_P_Barrett_1993_Grosh_F` reads `declining` on a lineage override. Its pooled
share is 96.8% and stable. The *Morbillivirus caprinae* lineage, PPRV, is not: 307 evaluable
records, 235 detected, 76.5%, down from 264 / 235 / 89.0% on 2026-11-01, and 55.6% in the
recent window against 90.7% on earlier records.

The 70 records new to this assay since 2026-11-01 are the whole story. 43 are evaluable,
every one of those is *caprinae*, every one is `fail`, and they are one batch: consecutive accessions **PZ271096 to PZ271138**, deposited 2026-10-31, complete and
partial genomes titled *Morbillivirus caprinae strain Albania/Shkoder/D4861/2025* through
*Austria/Horn*: the 2024-2025 PPRV incursion into Europe. Every one of the 43 carries the
same six forward-primer mismatches (positions 2, 9, 10, 14, 16 and 17 from the 3' end) and
three in the reverse. The other 27 new records have no amplicon at all.

Nothing on this entry changed that could screen differently: step 6b edited its `claim`, a
note sentence and a flag note. The 2026-11-01 run had the same 235 detections. This is the
per-lineage override (`worst_lineage_verdict`) firing on a deposit the designers could not
have seen, which is the premise of the tool. It is a different mechanism from the one that
caught influenza M1 Ward 2004 in held-out set 3, and it is the first time either has fired
on a live run against a deposit made after the previous run.

Worth the maintainer's eye before publishing: whether the Barrett P-gene set is in use for
PPRV anywhere, because on these genomes it would read negative.

## The rest of step 14

- **Invariant: composition cells sum to the graph, 0 mismatches** over 6,078 assay-years of the
  215 assays in the extract (`local/release-work-2026-11-10/invariant.py`, the method of
  2026-11-04).
- **Extract and render**: `website/data/run.json` and `composition.json` (schema 2) from the
  frozen run; 215 assay pages and the nest pages re-rendered.
- **The test the freeze left red is green**: `test_the_extract_still_describes_the_registry_it_was_taken_from`
  passes now that the extract carries FT443's chemistry. Full suite 2,241 passed; `pytest -m slow`
  12 passed.
- **Three pages by eye.** `Chlamydia_16S_Messmer_1997_round1` carries two spike sentences with
  their study clauses from the warmed cache (1997, 43 consecutive accessions from one *C.
  psittaci* phylogeny; 2021, 151 from a recombination study). `Monkeypox_virus_G2R_Li_2010_G2R_WA_F`
  carries its page note. `Bornaviridae_N_Zimmermann_1994_round2` reads "status withheld" in the
  Verdict row and stops at Scope. Section order is the 2026-11-10 order on all three.
- **`website/index.md`'s status table was wrong before this run and is corrected.** It was
  headed "2026-11-01 run" and read 75 / 42 / 29 / 32 / 18 / 5 / 14; the 2026-11-01 `run.json` it
  is built from counts 70 / 40 / 29 / 34 / 18 / 5 / 19. Now 2026-11-10 from `run.json`: stable 70,
  declining 41, low coverage 27, insufficient data 36, no recent data 17, watch 6, no status 18.
  **Three bases exist and the release should name which it quotes**: the site's `run.json` (215
  rows, withheld as "no status"), `report.md`'s table (what `report_diff` reads: 95 stable on
  2026-11-01 and 92 on 2026-11-10, because it lists protocol and round rows differently), and the
  hand table. The CHANGELOG draft quotes `report.md`'s and says so.
- **The gate, `assaywatch scope-check` on the frozen calls, its first real run**: 120 flags over
  the 215 assays, none a verdict (`local/release-work-2026-11-10/scope-check-frozen.tsv`). By kind:
  `taxid_over_query` 71 and `query_names_taxid` 21, both of which over-fire on purpose and are the
  standing watch list; `archive_stale` 13 and `query_sees_nothing` 9, every one on an assay already
  reading `no recent data` or `insufficient data`, and each either in the roadmap's "cleared, do
  not chase again" list (E. coli LT, Shigella ipaH, Y. enterocolitica, on assembly retrieval) or
  documented on 2026-11-01 (EEHV5 and 6, Batravirus european, Ophidiomyces IGS, Reptarenavirus);
  `scope_empty` 2; `scope_taxid_gained_parent` 4. The last two kinds were read one by one:
  - `Orthobornavirus_XP_Sigrist_2021_aquatic` is `stable` with no in-scope record in the gate's
    24-month window. Not a contradiction: its report row says the window was widened to 60 months
    to reach 15 evaluable records, and the page says so.
  - `Orthopoxvirus_G9R_Gallardo-Romero_2011`, `scope_empty`, reads `no recent data`. Consistent.
  - The three Uccellini entries' scope `1986118` has gained a species parent, `3240428`
    *Pregotovirus pythonis*, and `taxonomy.within` would drop records filed at the parent. **Zero
    window records are filed there today** (the group's newest archive holds two window records,
    at 1986118 and 1912590), so this is a watch item, not a loss. Same shape for DWV-B's `232800`
    under `3047792`, which is that entry's own retrieval taxid.
- **Six taxids are missing from `drift.scope_taxonomy` and were matched exactly** during this run,
  42 records in all: 1336684 (32 records, under 198112, a new deformed-wing-virus node), 3904487,
  3904488 and 3904489 (7, under 11270), 3904934 (2, under 11974) and 3467847 (1, under 3044472). NCBI
  created them after the cache was built. A record whose ancestry the cache cannot see is in scope
  only if its own id is named, so some of the 42 may sit outside a scope that would otherwise hold
  them. Rebuilding the cache changes an input the report rule hashes, so it is for the next run,
  with these ids as the check that the rebuild reached them.

## Verdict on step 14

Every invariant holds, every test is green, every status move has its cause, and the one surprise
is the tool working. Nothing here is a stop. **Step 15 waits for the maintainer's go.**
