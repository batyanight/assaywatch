# 2026-11-01 — the 18 `no recent data` assays, each query and scope questioned

**Finding: all 18 verdicts are true statements about deposition. None is a retrieval
artefact.** Two queries carry a latent risk and two scopes leave out a related virus;
none of the four moves a verdict today. One query (Ophidiomyces) fetches ~185 records
that can never carry its product and is to be narrowed in the next release.

ROADMAP asked (Data and curation, "the 49 assays the website does not list") that each
`no recent data` assay be "checked against its archive's deposit-year distribution,
because that is how a stale retrieval query presents". This is that check, extended to
scope after the influenza episode (`2026-10-30-set3-scored.md`) showed the query
agreeing with itself while being blind.

All NCBI counts are live, taken 2026-11-01. "Window" is the report's recent window,
deposits from 2024-10-01 (`2024/10/01:2026/11/01[PDAT]`). The list of 18 is the
`no recent data` rows of the 2026-10-31 report (`results/2026-10-31/report.md`).

## Method

Five tests. Each answers a different way an assay can read `no recent data` while
records exist.

1. **Archive profile.** For each assay: its retrieval group
   (`registry.archive_dir`), the record count, the newest `created` date, the records in
   the window, and what the 2026-10-31 screen called each recent record (`call` and
   `exclusion` from `calls.tsv.gz`). This splits the 18 into archives with nothing
   recent (7) and archives with recent records none of which are evaluable (11).
   `scripts/check_archive_recency.py --months 24 --verbose` gives the newest-deposit
   half of this for every group.
2. **Query against NCBI, three counts.** The query exactly as `retrieve.build_query`
   emits it, over all dates and over the window; then the bare taxid over the window.
   Query-all equal to the archive count means the archive holds everything the query
   can see. A taxid-window count above the query-window count means the query's own
   filter is excluding recent records, and those records are then listed and read.
3. **Organism-name search across all taxids.** The influenza failure: new records
   filed under a taxid the query does not name. Searched by common name, abbreviation
   and the ICTV binomial, with no taxid restriction, over the window.
4. **Scope taxa.** For entries with `scope_taxids`: the in-scope count in the window,
   then recent records in the parent taxon outside the scope, grouped by taxid, to see
   whether a new or renamed sibling taxon is absorbing records the assay claims.
5. **What a title filter excludes, assemblies included.** For title-filtered queries:
   `txid... AND window NOT (query)` read record by record, and `datasets summary genome
   taxon` for assemblies. Where assemblies are excluded and the target region is a
   repeat, tile a known target record (25-mers every 100 nt) against an assembly of the
   SAME strain. That says whether assemblies can carry the region at all.

The commands, in the form used:

    W='2024/10/01:2026/11/01[PDAT]'
    c(){ esearch -db nuccore -query "$1" < /dev/null 2>/dev/null | xtract -pattern ENTREZ_DIRECT -element Count 2>/dev/null; }
    c "txid<TAXID>[Organism:exp] AND 100:100000000[SLEN] AND (<target.query>)"           # 2, all dates
    c "txid<TAXID>[Organism:exp] AND 100:100000000[SLEN] AND (<target.query>) AND $W"    # 2, window
    c "txid<TAXID>[Organism:exp] AND $W"                                                 # 2, taxid only
    c "(<name>[All Fields] OR <abbrev>[All Fields]) AND $W"                              # 3
    datasets summary genome taxon <TAXID> --as-json-lines | jq -r '[.accession,.assembly_info.release_date] | @tsv'   # 5

**`2>/dev/null` is not cosmetic.** When a quoted phrase is absent from NCBI's index
(`QuotedPhraseNotFound`), esearch retries and writes the full request URL to stderr,
`api_key` included. It did so in this session's output. Rerun any suspicious count
without the quoted phrase.

## Results: archive with nothing recent (7 assays, 6 groups)

| assay(s) | archive (newest) | query all / window | taxid window | name search, window | reading |
|---|---|---|---|---|---|
| `Leporid_gammaherpesvirus_5_gB_AbadeDosSantos_2021` | 5 (2021-03) | 5 / 0 | 0 | 0 | quiet |
| `Intranuclear_coccidium_JW_2004_18S_Alvarez_2013` | 2 (2018-10) | 2 / 0 | 0 | 0; 2 ever, both archived | quiet |
| `Sunshinevirus_L_Hyndman_2012_SunshineS1`, `_2` | 8 | 8 / 3 | 3 | 3 | the 3 are patent records (circular-RNA constructs), excluded as patents; quiet |
| `Elephant_endotheliotropic_herpesvirus_5_POL_Latimer_2012_round1`, `round2`, `round2B` | 20 (2024-06) | 20 / 0 | 49, genus | 0 | the genus's 49 are EEHV1A, EEHV1 and EEHV4; quiet |
| `Elephant_endotheliotropic_herpesvirus_6_POL_Latimer_2012_round2` | 6 (2021-11) | 6 / 0 | same 49 | 0 | quiet; see latent risk |
| `Batravirus_terminase_Licheri_2020_european`, `pan_FW4_RV4` | 8 (2019-02) | 8 / 0 | **7** | 8 | quiet; see below |

**Batravirus.** The query excludes 7 window records under its own taxid: Bufonid
herpesvirus 1, `UNVERIFIED`, unannotated, 90-192 bp (PV005823-29, 2025-03-01). The
product is 200 bp, so none could hold it; excluding them changes nothing. The name search
found an eighth: **Ranid herpesvirus 5, complete genome** (PV243667, 2025-11-21, 221 kb),
which NCBI places in "unclassified Herpesvirales" (taxid 3467605), outside Batravirus
(3044671). No taxid query can see it. Whether a new batrachian herpesvirus belongs in the
pan pair's scope is a curation question, not a defect: ROADMAP.

**EEHV6, latent.** The query names one taxid, 768739, under "unclassified Proboscivirus".
EEHV5 already went through the change this risks: NCBI added `Proboscivirus
elephantidbeta5` (3050275) beside the old 768738, and the EEHV5 query names both. When an
`elephantidbeta6` taxon appears, new EEHV6 records will likely land under it and this
query will go blind without complaint, which is the influenza mechanism. Name search for
EEHV6 over the window: 0, so nothing is missed today. ROADMAP.

## Results: archive current, nothing evaluable (11 assays)

| assay(s) | recent in archive, fates | scope test | reading |
|---|---|---|---|
| `Caliciviridae_capsid_Reid_1999`, `_Helicase_Reid_1999`, `_RdRp_Neill_Seal_1995` | 10,330 / 13,458; almost all `no_site` | scope Vesivirus exanthema (3433198): 4 in window, all 130 bp patent records. Recent vesiviruses outside it: feline calicivirus, canine vesivirus (20), mink calicivirus (7), stoat vesivirus (3), 2 genus-level | quiet; the scope is the paper's claim |
| `Orthopoxvirus_G9R_Gallardo-Romero_2011` | 6,980; 6,414 `fail` are monkeypox, out of scope | scope raccoonpox, volepox, skunkpox: **0** in window | quiet; borealpox not in scope, below |
| `Perkinsea_18S_Smilansky_2021_cladeAC`, `_cladeD_` | 239 (all Perkinsea): 140 `truncated`, 89 `no_site`, 9 `diverged` | scope uncultured Perkinsea (373149): 137 in window, same 137 under query + scope, so the archive holds them | quiet; short environmental reads do not span the 287 bp product |
| `Eimeria_furonis_18S_Sledge_2011` | 12, all `truncated` (437 bp partials) | taxid window 12 = archive | quiet |
| `Ophidiomyces_ophidiicola_IGS_Bohuski_2015` | 55, all `no_site` (ITS/SSU records) | below | quiet; query to narrow |

**Borealpox.** Borealpox virus (formerly Alaskapox, 2602439) is a fourth North American
orthopoxvirus and is not in `scope_taxids`. That matches the 2011 paper, which predates
its description, and only one borealpox genome has ever been deposited (MN240300, 2019),
none in the window. A curation question: ROADMAP.

**Ophidiomyces: the target is the IGS, and assemblies cannot supply it.** The question
was raised whether the assay targets ITS. The data says IGS: every record the assay has
ever scored (11, all `detect` at 133 bp) is a 28S-18S intergenic spacer sequence
(KP691505-14, 2015; MT459829, 2020), and it has never produced a product on any of
the ~185 ITS, SSU or LSU records in its archive. Only 11 IGS-titled records exist for
the taxid, none in the window. (Paper not in `papers/`, so the paper's wording was not
read here.)

The title filter excludes about 90 genome assemblies, one in the window
(GCA_982397405.1, released 2026-04-10). Test 5: the 1,306 bp IGS record of strain
CBS 122913 (KP691505) tiled against the 2022 assembly of the same strain
(GCF_022830035.1) is present over its first ~500 nt (the 28S end) and absent over every
IGS window. The assembly stops where the rDNA repeat's spacer begins. The 2026 assembly
lacks even the 28S stretch. Neither contains an exact primer match. So excluding
assemblies loses nothing, and the verdict stands.

The query `ITS[Title] OR ITS2[Title] OR ... OR "ribosomal DNA"[Title]` fetches records
that cannot carry the product: about 185 of the 196 in the archive. Narrowing it to
`IGS[Title] OR "intergenic spacer"[Title]` would shrink the group and move no result.
Changing a query changes the retrieval group, so it waits for the next release.

## What went to ROADMAP

- Ophidiomyces query narrowed, next release.
- EEHV6 query: add the species-level taxon when NCBI creates one.
- RaHV-5 and the Batravirus pan pair's scope; borealpox and the G9R scope. Maintainer
  questions.
- The ROADMAP item that asked for this check, ticked with a pointer here.
- A standing scope verification before every release (`CONTRIBUTING.md`, Releasing).
- From the wider sweep below: Panpox Leporipoxvirus, the plasmid-gene sample, the
  Hantavirus pending trio, and a script for the release check.

## The wider sweep: `insufficient data`, stale groups, sub-taxid queries, `pending/`

Run the same day over 61 entries: the 30 `insufficient data` assays, the stale groups
`check_archive_recency.py` lists, every live entry whose `target.query` names a taxid
(23), and the 10 `pending/` candidates. Tests 1, 2 and 4 by script (query all dates and
window, bare taxid window, scope window, archive count and newest deposit), then the
flagged ones by hand.

**A test that measured nothing, caught.** The script's name search used
`"<taxon_name>"[Organism]`, which NCBI resolves back to the same taxid, so it returned 0
for every entry by construction. Test 3 must be free text (`[All Fields]` or `[Title]`).
Redone that way for Reptarenavirus, B. salamandrivorans, Paranannizziopsis and
Ferlavirus: the hits outside each taxid are host genomes and salamander transcriptomes,
not misfiled pathogen records.

**A false alarm, measured and cleared.** `calls.tsv.gz` (2026-10-31) has 3,462,260 rows of
which 70,095 repeat an (assay, record) pair, and several archives hold exactly twice
what their query returns (E. coli LT 122 against 61). Both are the incremental archive:
two fetches a day apart each hold every record. `report.read_calls` collapses to one row
per accession before drift (`tests/test_report.py::
test_calls_are_deduplicated_to_one_row_per_accession`), so no verdict counts a record
twice.

**Gene-titled bacterial queries that see nothing recent are not blind.** E. coli LT,
Shigella ipaH, Y. enterocolitica and E. coli hlyA all have queries returning 0-3 records
in the window against 31,850-3,202,443 for the taxon. Their taxa are on assembly-level
retrieval (`config.yaml assemblies.taxa`), which supplies the recent records: Shigella
ipaH has 38 evaluable since Oct 2024 and Y. enterocolitica 15.

**Findings that are weaknesses:**

1. **Plasmid and pathotype genes in a random species sample.** Assembly retrieval takes
   up to 20 complete or chromosome-level E. coli genomes per release year, not enriched
   for any pathotype. Of the sampled genomes, ETEC LT (`Escherichia_coli_LT_Victor_1991`) has
   no binding site in 315 of 325 rows and O157 hlyA (`Escherichia_coli_hlyA_Wang_1997`) in 291
   of 325 (counts include the duplicate archive rows). The gene is absent from most
   sampled genomes, so the evaluable count stays at 1 and 2, and `insufficient data` there
   is a statement about the sample, not about deposition.
2. **Panpox: Leporipoxvirus excluded on a reading the same note contradicts.** Both Li
   2010 entries exclude Leporipoxvirus and Macropopoxvirus from both queries (2026-10-17:
   "Li 2010 does not say where the crossover sits"). The 2026-10-05 part of the low-GC
   note, written from the paper's Methods, lists Leporipoxvirus in the low-GC group, and
   that day's screen amplified myxoma. 36 Leporipoxvirus records sit in the window today
   (32 myxoma virus, 3 under the new binomial `Leporipoxvirus myxoma`, 1 rabbit fibroma).
   Needs the PDF read again.
3. **Queries that name sub-taxids** (11 entries outside influenza, which `title_requires`
   now handles): coronavirus RdRp x3 (SARS-CoV-2, 2697049), LMBV x2, Mycoplasma turtles,
   Panpox x2 (genus lists), EEHV3/4 x3, EEHV5 x3, EEHV6. None is blind today: LMBV
   Grizzle's five taxids do not include the new species `Ranavirus micropterus1`
   (3432136) that the Li 2025 entry names, but no record sits at that node directly
   (0 of 59 in the window). Each is the influenza mechanism waiting for NCBI to re-file a
   taxon, which is what the release gate's test 2 is for.
4. **`pending/` nested naming.** The three Hantavirus S-segment candidates are
   `_S_segment_2` (532 bp), `_round2` (236) and `_round2_2` (417): which pairs nest
   inside which cannot be read from the ids. The Enterovirus pair is round1/round2 and
   clear. All 10 candidates' queries are current (19 to 8,678 records in the window);
   none is blocked by retrieval, only by `doi_verified`.

## Other databases: cheap tests

Asked whether sources beyond GenBank (MalAvi and others) should be screened. Most
candidates are INSDC-derived; one earns a place by adding sequences INSDC lacks or
labels that fix a known problem. Three cheap tests:

- **MalAvi.** The registry's `Haemosporida_cytb_Hellgren_2004_HaemF` is HaemF/HaemR2,
  the inner pair of the Hellgren 2004 nest (`Haemosporida_cytb_Hellgren_2004_HaemNFI`
  is the outer, HaemNFI/HaemNR3), and its product is MalAvi's lineage fragment. Of 5,488
  haemosporidian cyt b partials in GenBank (`txid5819`, "cytochrome b" in title,
  300-700 bp, 2023-2026), the commonest lengths are 477 (1,262), 479 (1,138), 478 (843)
  and 475 (562), and only 73 contain the 3'-terminal 12 nt of both primers. Depositors
  trim the primers, as MalAvi's fragment does, so neither source can supply screenable
  sequences for this pair; the screen's evaluable records come from longer records,
  mitochondrial genomes among them. MalAvi's server did not answer (two addresses,
  20 s timeouts). Side finding: the entry stores `amplicon_bp: 480`, the
  primer-excluded convention, against a measured 525 (2026-10-05 audit) with no
  disclosure flag.
- **E. coli pathotype selection (EnteroBase's use case) inside NCBI.** Assembly records
  carry no serotype text (0 O157 among 5,636 complete or chromosome-level E. coli
  assemblies in the window), but BioSamples do: 6,462 with serovar O157 and 1,001 naming
  ETEC in the window. Linked to assemblies, the O157 set gives 6,086: 5,975 contig, 108
  scaffold, 2 complete, 1 chromosome. The sampler takes only complete and chromosome
  levels, which is why it cannot reach them.
- **GISAID** was not tested: access and redistribution terms come first.

## Test 4 on scored verdicts: the scope decides the haemosporidian denominator

The first pass covered undecided statuses only. Redone the same day on the 18 scored
assays with `scope_taxids` (11 `declining`, 7 `low coverage`): for each, the window
counts inside and outside the scope, and the taxids of what falls outside.

**A column of mine that measured nothing, caught before it was reported.** The first
run printed a "no taxid" count read from each group's own metadata sidecars, and made it
look as though the scope could not apply to most recent records (3,126 of 3,151 for the
haemosporidian group). It is wrong: `report.py` builds the accession -> taxid map from
`data/retrieved/.meta.taxid.backfill.tsv.gz` AND the sidecars. Measured against the real
map, all 18 assays have a taxid for **every** recent record (531 to 13,074 each, 0
missing). Scope applies to all of them.

**The finding: `Haemosporida_cytb_Hellgren_2004_HaemF` rests on 155 evaluable
records while 816 recent records of its own genus sit outside its scope.** The scope is
seven nodes: five Plasmodium SUBGENERA (Haemamoeba, Huffia, Novyella, Giovannolaia,
Bennettinia), the Haemoproteus genus, and 587283. Of the group's 3,151 recent records,
816 are filed at `Plasmodium sp.` (31272), which NCBI places under "unclassified
Plasmodium" and so inside no subgenus. `taxonomy.within` therefore drops every one.

What those 816 hold, from the 2026-10-31 calls: 506 `no_site`, 151 `truncated`,
86 `diverged`, 59 `detect`, 10 `reduced`, 4 `fail`. So between 73 and 159 of them are
evaluable depending on `count_diverged_as_fail`, against the 155 the published verdict
rests on, and 69 of them are detections. Including them would roughly double the
denominator and move the share up from 10.3%; it would not by itself clear the 90%
threshold.

Whether they belong in scope is a curation question, not a bug, and the entry's own name
is the argument for it: the assay is "Pan *Plasmodium* sp. and *Haemoproteus*", and an
indeterminate avian *Plasmodium* deposited from a cyt b fragment is exactly what it is
for. Against that, an unclassified node is not evidence the record is in an avian
subgenus. Either way the verdict currently turns on a taxonomic filing decision.
`Leucocytozoon sp.` (764 records) is correctly outside; `Haemoproteus sp.` (524) is
correctly inside. `Haemosporida_cytb_Hellgren_2004_HaemNFI` shares the group and the
scope, reads `declining` at 66.8% of 193, and excludes 13,071 records.

**New taxa drifting outside a scope, the influenza mechanism in slow motion.** Small
today, and worth re-running before each release:

| assay (status) | outside scope, window | what they are |
|---|---|---|
| `Enterovirus_VP3_VP1_Nix_2006_round2` (declining) | 40 | `Enterovirus E11` (3569727), `E13`, `E6`, `E9`, `PV1` — new species nodes under "unclassified Enterovirus", against a 520-taxid scope |
| `Paramyxoviridae_L_Tong_2008*` x2 (low coverage) | 73 | all `Pyeongtaek Microtus paramyxovirus` (3412626), "unclassified Paramyxoviridae" |
| `CORONAVIRUS_..._Lan_2010_round1`, `_round2` (declining) | 62 | `Rodent coronavirus PlONCAN`/`PmONCAN`/`CgONCAN`/`MpONCAN`, "unclassified Orthocoronavirinae" |
| `Rhabdoviridae_L_Bourhy_2005_round1` (declining) | 149 | plant rhabdoviruses (eggplant mottled dwarf and relatives) — out of scope on purpose |
| the rest (10 assays) | 0 to 2 | nothing: one snake virus, one leafhopper flavivirus, one cervid herpesvirus, two seal polyomaviruses |

The pattern in the first three rows is the same one: NCBI creates a node under
"unclassified X" and records land outside an enumerated scope that has no way to know.

## Test 4 on the `stable` and `watch` assays: a second way a scope goes stale

Same test, the remaining 11 scored assays carrying `scope_taxids` (10 `stable`, 1
`watch`). One new failure mode, one confirmation, no verdict moved.

**The new mode: a scope's taxid becomes a CHILD of a node NCBI then files records at.**
`Parapoxvirus_RPO147_Zhao_2013` scopes [10258 `Orf virus`,
129726 `Pseudocowpox virus`, 129727 `Bovine papular stomatitis virus`]. Under the ICTV
binomial renaming, NCBI created species nodes `Parapoxvirus orf` (3431389),
`Parapoxvirus pseudocowpox` (3431390) and `Parapoxvirus bovinestomatitis` (3431388), and
made the old names their children: `Orf virus`'s lineage now ENDS in `Parapoxvirus orf`.
`taxonomy.within` asks whether a record's taxid sits inside a scope taxid, and a parent
does not sit inside its child, so every record filed at the new species node is dropped.

In the window, 84 of the group's 513 recent records are already at the three new nodes
(80 at `Parapoxvirus orf` alone, against 381 still at `Orf virus`), and the assay's
verdict rests on 33 evaluable records.

**The effect today is negligible, and saying so matters.** Of those 84, 79 have no primer
site, 2 are `truncated`, 1 is `diverged` and 2 are `detect` — so including them would add
about 3 evaluable records to 33 and move `stable` at 97.0% nowhere. The finding is
prospective: 17% of recent orf records already sit at the new node, that share will rise
as NCBI re-files, and nothing in the pipeline would say so. It is a different shape from
the `Plasmodium sp.` case, where the excluded records were material to the verdict, and
from the "new node under unclassified X" cases, where the new node is a sibling rather
than a parent. A scope audit has to look for both.

**The rest.** `Adenoviridae_POL_Wellehan_2004_round1`/`round2`: 40 outside, 36 of them
`Quail adenovirus` (3467836), a new node. `Enterovirus_VP3_VP1_Nix_2006_round1`: the same 40
`Enterovirus E11`/`E13`/`E6`/`E9`/`PV1` as its `declining` round2 sibling.
`Orthoflavivirus_NS5_Moureau_2007` 1 outside, `Orthoherpesviridae_terminase_Chmielewicz_2001_round1` 0.
`Rhabdoviridae_L_Bourhy_2005_round2`: 149 plant rhabdoviruses, out of scope on purpose.
`BORNA_VIRUS_N_gene` and `..._Zimmermann_1994`: 156 of 174 outside, almost all parrot
bornaviruses, which is correct — these are Borna disease virus entries and the
psittacine assay is a separate entry.
`Orthobornavirus_XP_Sigrist_2021_aquatic` reads 0 in scope in the 24-month window, which
looks alarming and is not: its scope taxon `Orthobornavirus avisaquaticae` (1548722) is
current and simply had no deposit, and the verdict comes from the window widened to 60
months (18 evaluable, 100%). The widening is doing exactly what it exists for.
