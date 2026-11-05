# 2026-11-04 — 64 entries' scopes reread against 36 papers and the database of their day

**Finding: 21 entries were broadened and no verdict moved. Every narrowing was tested and none
was applied; two would change a status, and neither makes the assay look better on evidence.**
Most of the gaps are list lag: `scope_taxids` were built from a snapshot of NCBI's tree, and NCBI
has since added species and placed new species nodes above the listed taxa. Records under those
nodes had silently left the denominator.

Asked: update the scopes, but only to broaden them; test anything proposed for narrowing; reread
the papers on scope and place them in the database of their time; test for submission error.

## Method

- **Entries.** The 54 with a scope or `scope_narrower_than_taxid`, plus Uccellini, Messmer, Victor,
  Li 1995, the Bd ITS pair and Leucocytozoon: 64 entries, 36 papers, all held and read. The other
  live entries were not reread, so the roadmap's whole-registry report stays open.
- **Reading.** Claim, what was tested, what the design rested on, then the curator note, in that
  order so the note could not anchor the reading. Subagents read; their taxids came from a local
  cache, so each edit's taxid was checked live against NCBI taxonomy.
- **Verdicts.** Three temporary registries (baseline, broadened, narrowed) through
  `assaywatch.site extract` on the 2026-11-01 calls, which is the report's own scope logic. The
  baseline reproduced the published `run.json` for all 33 assays.
- **Database then.** Cumulative records by `pdat` through the design year, from the coverage count
  behind the composition panel. These are today's records by release date, so a later
  reclassification or withdrawal can move them. They bound what could have been seen.
- **Submission error, on Bd.** All 9,493 archived records BLASTed against the mitochondrion
  (BK072406), an rDNA contig and two nuclear assemblies, and the title's claim set against what the
  sequence is.

## What was broadened

No status moved. `recent` and `baseline` are detected/evaluable.

| entries | added | effect |
|---|---|---|
| Wellehan 2004, 2 | 7 adenovirus species | round 2 recent 1202/1252 to 1240/1290 |
| Johne 2005, 3 | 1 polyomavirus species | recent 19/990 to 19/992 on 2 of the 3 |
| VanDevanter 1996, 2; Chmielewicz 2001, 2 | *Cervid gammaherpesvirus* | out of scope 2 to 1 on VanDevanter |
| Zhao 2013 | new species nodes above orf, pseudocowpox, BPSV | recent 32/33 to 34/35; 84 records back in scope |
| Nix 2006, 2 | E6, E9, E11, E13, PV1 species nodes | round 2 recent 837/4639 to 852/4679 |
| Moureau 2007 | 1 species | 1 record, no evaluable change |
| Tong 2008, 2 | 1 species | round 1 recent 3113/4276 to 3119/4282 |
| Quan 2010, 2 | 11 species | round 1 recent 853/1647 to 867/1661 |
| Licheri 2020 european | species node above the listed taxon | none |
| Gallardo-Romero 2011 | 3 species nodes, VPXV_CA85, borealpox | baseline 7/7 to 7/8 |
| Lozano 1997, 2 | Reptarenavirus, Hartmanivirus, Antennavirus, Innmovirus | ARS16V baseline 388/989 to 388/1034, ARS3V 931/1419 to 931/1428 |

**Two of these go beyond what the paper tested,** so they carry the new caveat flag
`scope_wider_than_paper_tested`:

- **Lozano 1997.** The wording claims all members including undescribed ones, from 11 sequences of
  8 viruses, with 65 arenavirus records in the database by 1997. Those four genera were unknown to
  it. The wording reaches them; the evidence does not. Added on the wording, as instructed. All 45 and 9
  evaluable records this adds are misses.
- **Gallardo-Romero 2011.** "North American orthopoxviruses" is defined there as three viruses.
  Borealpox was not among them. Its one genome, MN240300, reads `fail` (penalty 11, 156 bp
  product), and is the entry's only scored miss. The oligos were not designed against it.

## Held: broadening that needs a maintainer or a new fetch

- **Hellgren 2004, `219829` "unclassified Plasmodium".** 1,833 sibling species sit outside the
  scope, about 1,209 of them bird-style lineage names, and some are chimpanzee or gorilla labelled.
  Adding the node would take HaemF baseline 479/1914 to 640/2773 and HaemNFI 859/983 to 1158/1448,
  with no status change, and would break the entry's avian restriction, which is curatorial rather
  than the paper's. Not applied.
- **Li 2010 IMV, Leporipoxvirus.** The paper's Table 1 lists it as low GC and counts it among its
  seven genera, contradicting the entry's note. The fix is a query edit, which needs a new fetch,
  and takes effect on the next run.
- **Li 2010 RPO147, crocodilepox** sits outside the query; the paper's High GC group includes it.
- **Rhabdoviridae 3425105-7, Thraupis sayaca bornavirus, calicivirus BCV/CCV/PCV/RCV:** the paper
  does not settle them, or the taxonomy was not resolved.
- **Perkinsea 453764** is outside the retrieval taxon, already flagged.

## Narrowing: tested, not applied

| proposal | current | narrowed |
|---|---|---|
| Uccellini `_PythonNido6F` to ball python nidovirus 1986118 | `low coverage`, recent 1/23, base 5/37 | `insufficient data`, recent 1/1, base 4/4 |
| Uccellini `_PythonNido7F` | `insufficient data`, 4/10, 10/18 | `insufficient data`, 1/1, 4/4 |
| Uccellini `_PythonNodoF` | `low coverage`, 3/17, 9/27 | `insufficient data`, 1/1, 3/3 |
| Baek 2020 to the 3 hummingbird-pox nodes | `low coverage`, 0/78, 3/1005 | `low coverage`, 0/41, 3/168 |
| Ahmed 2020 to 14 pathogenic *Leptospira* | `stable`, 406/414, 1330/1523 | `stable`, 390/394, 1210/1314 |
| Steyn 2020 to 7 Simbu species | no status, 0/71, 1/408 | no status, 0/71, 1/372 |
| Nix 2006 without the rhinoviruses | `stable` / `declining` | unchanged status; round 1 base 7790/8093 to 6318/6494 |
| Scaramozzino 2001 without Kamiti River, Ngoye, Culex flavivirus | `declining` | unchanged |
| Quan 2010 without Letovirinae and Pitovirinae | `declining` | unchanged |
| Li 2010 IMV without Avipoxvirus | `stable` | unchanged |
| Li 2010 RPO147 without sealpox | `stable` | unchanged |

**Uccellini is the only case where narrowing changes a status,** and the status it gives is less
informative, because almost nothing remains. The paper names seven overlapping pairs that amplify
one 3,408-nt contig of one virus, and never presents them as a diagnostic. By identity to KJ541759,
`Serpentovirinae sp.` is mostly 70-85% or below, so that node is not the same virus hiding under
a poor label; at most two records per entry reach 85-95%. Whether these entries belong in the registry
is still the first question, and it is the maintainer's.

**Baek's low detection is real at either scope:** 0 of 41 recent on the nodes nearest the paper's
own virus. A taxid scope can't separate it further, since one of its detects sits under the
catch-all 1928336.

**No taxon node to test against:** Huo 2022, Li 2010 C3L, Ghosh 2021, Smilansky 2021 and Conley
2021 are lineage or organism claims inside one taxid. They read broader than the paper, and scope
can't express the difference. Conley's target has one record, MG910456, outside the retrieval.

## The database at the time

Taxon and query records released through the design year, against today:

| paper | design | taxon then / now | what the paper says it rested on |
|---|---|---|---|
| Neill 1995 | 1995 | 144 / 85,698 | own clones of SMSV 1 and 4 |
| Li 1995 | 1995 | 1,434 / 634,683 (query 12 / 2,729) | 8 aligned SSU sequences of 7 species |
| Zimmermann 1994 | 1994 | 8 / 1,586 | one clone, pAB5 |
| VanDevanter 1996 | 1996 | 1,548 / 77,354 | conserved motifs, 7 GenBank loci listed |
| Lozano 1997 | 1997 | 65 / 6,574 | "all reported" S RNAs: 11 sequences of 8 viruses |
| Messmer 1997 | 1997 | 427 / 131,544 | not stated; names 3 species |
| Reid 1999 | 1999 | 541 / 85,698 | marine caliciviruses "sequenced so far", no count |
| Scaramozzino 2001 | 2001 | 1,932 / 108,185 | "30 different flaviviruses" are 30 strains of 5 species |
| Hellgren 2004 | 2004 | query 635 / 32,073 | published avian mtDNA, no count |
| Boyle 2004 | 2004 | 45 / 9,514 | 4 isolates, plus 29 field sequences unpublished |
| Wellehan 2004 | 2004 | 1,638 / 40,244 | not stated |
| Johne 2005 | 2005 | 2,652 / 15,849 | 10 genomes |
| Bourhy 2005 | 2005 | 4,958 / 47,014 | L gene of 10 members |
| Nix 2006 | 2006 | 11,767 / 149,713 | 64 prototype strains |
| Moureau 2007 | 2007 | 7,914 / 108,185 | "all available" in the genus, no count |
| Tong 2008 | 2008 | 9,713 / 86,832 | 29 nonredundant genomes, 4 L genes |
| Quan 2010 | 2010 | 8,076 / 9,296,876 | "available" RdRp genes, no count |
| Li 2010 JCM | 2010 | 4,416 / 30,844 | 24 genomes |
| Gallardo-Romero 2011 | 2011 | 2,852 / 19,599 | one strain per North American species |
| Uccellini 2014 | 2014 | 3 / 290 | own contig |
| Licheri 2020 | 2020 | 9 / 17 | 4 sequences |
| Ahmed 2020 | 2020 | 254,209 / 325,205 | 97 strains of 10 pathogenic species |
| Baek 2020 | 2020 | 1,264 / 1,762 | one accession, JX418296 |
| Ghosh 2021 | 2021 | 9,218 / 9,514 | 150 isolates' mtDNA, bias stated |
| Rossi 2024 | 2024 | 161 / 249 | 110 DWVA, 46 DWVB, searched 27 April 2024 |

**What the table is for.** Papers before 2010 saw under 17% of today's taxon, most of them under
8%, and designed from a handful of sequences, so "all" and "universal" in them mean all of what existed.
That reading is why the additions above were made on the paper's taxon wording rather than its
strain list, and why a later fail on a virus described after the paper isn't evidence against the
paper. Recent designs saw most of today's records, so their low numbers need another explanation.
Taxon counts include every gene of the taxon, so they say how much existed, not how much of the
target gene. Quan's today is dominated by 2021 onward: 2,994,605 records in 2021 alone against
3,590 in 2019.

## Submission error

**Bd: no record found that isn't Bd, and no title found that misstates its gene.**

| title claims | mitochondrial | rDNA reference | Bd nuclear | weak hit | no hit |
|---|---|---|---|---|---|
| ITS/5.8S | 0 | 358 | 114 | 0 | 0 |
| mitochondrial | 13 | 0 | 0 | 0 | 0 |
| predicted mRNA (`XM_`) | 3 | 4 | 7,574 | 805 | 0 |
| genome pieces | 24 | 5 | 433 | 11 | 0 |
| other rDNA | 0 | 2 | 39 | 0 | 0 |
| gene or mRNA | 0 | 0 | 16 | 0 | 0 |
| other | 6 | 3 | 81 | 2 | 0 |

- The 114 are real ITS: they align at 92-100% to rDNA copies in the assemblies, and missed the one
  contig used as the rDNA reference.
- **MT730717** (JEL0405) is the one open candidate: titled SSU-ITS-LSU, 94.8% over 2,036 of its
  4,622 bp to Bd, no site for either ITS assay. Its sibling MT730780 detects. The remote BLAST was
  stopped before returning, so its species is unconfirmed.
- The 805 `XM_` weak hits are read as splicing, from their annotation; they were not checked singly.

**Depositors' records can't test the primers that made them.** 398 records are `truncated` on
Boyle. Annis's forward primer ends `GTCACG` and Boyle's probe starts `CGAGTC`, so they overlap by
2 bases. 145 records start exactly at offset 92 before the reverse site, and 134 of those begin
`AGTCGAACAAAAT`: Annis amplicons with primers trimmed, 2 bases into Boyle's probe. The exclusion
is correct. The consequence is that ITS deposits mostly cannot show drift at those sites, whatever
is happening there.

**Bd mitochondrial.** The 8 and 9 evaluable records for the Ghosh entries are honest. A query
would lose records: 30 of the 43 mitochondrial records found aren't titled as mitochondrial. So
that narrowing fails too. RTP6's mitochondrial contigs (QUAD01000020, 021) resolve by accession
but not under the taxon search, and `assemblies.levels` wouldn't reach them at contig level, so
adding Bd to `assemblies.taxa` gains nothing at present settings: JEL423 is already archived.

**Uccellini.** A title-against-genome-position screen flagged 59 of 290 records; that screen is
too crude to call mislabelling, because a multi-gene title matches anywhere. Thirteen records have
no hit to the reference. Eleven records in the archive are patent sequences of about 410 bp from
circular RNA filings, filed under this taxon. All 33 of their calls are `no_amplicon`, so they
don't reach a denominator.

**Not tested:** this was not run on the rest of the registry.

## In the papers themselves

These correct the record; none was acted on here.

- Lozano's curator note says the paper amplified LCM, Lassa, Mopeia and Pichindé. That list is the
  alignment set. Amplified: Junín MC2, LCM WE, Tacaribe, Pampa.
- Li 2010 IMV's note says the paper doesn't place the GC crossover. Its Table 1 does.
- Hellgren: 480 and 478 are stated excluding primers; 525 appears nowhere in the paper.
- Uccellini Table 2's positions contradict its primers.
- Ahmed Table 1 lists *L. meyeri* as both pathogenic and saprophytic.
- Quan Fig. 3 gives NC_006577 for both HKU1 and MHV. Nix prints E10 as reovirus, E28 as
  rhinovirus 1A and EV72 as hepatitis A. Tong says all 25 viruses were detected by the pan primers,
  then that three amplified only with subgroup primers.
- Messmer's paper reports *C. trachomatis* amplified, and the entry's screen has round 1 at 0 of
  301. Scope doesn't explain that.

## Correction to this morning's record

`2026-11-04-low-accession-scope-check.md` says Bd's records are "nearly all ITS". They are not:
about 8,300 of 9,493 are `XM_` predicted mRNAs. Corrected there.

## Files

Registry: 21 entries, plus `scope_wider_than_paper_tested` in `assaywatch/review.py`. The paper
readings and scratch tests were not committed: they quote copyrighted text.
