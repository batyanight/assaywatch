# 2026-11-04 — the 33 assays with under 30 evaluable records, each scope questioned

**Finding: 22 of the 33 are low for honest reasons, and 11 are not.** Of those 11, one has a
scope that is too broad, with the same fault in two siblings outside the 33; four cannot reach
a source of sequence the taxon has; and six have a scope narrow enough to be a question for
the maintainer. Nothing in the registry changed.

Asked: assays with very low numbers of accessions need their scopes checked. The cut-off is
under 30 evaluable records in the recent and baseline windows of the 2026-11-01 run. It is a
choice, not a measurement: 13 assays sit under 10, 33 under 30, 60 under 100. The 2026-11-01
pass (`2026-11-01-no-recent-data-scope-check.md`) asked whether each archive was current. This
asks whether the scope is why the count is low.

## Method

Per assay: what each screened record's call and exclusion were (`calls.tsv.gz`); `build_query`'s
query against the bare taxid, all dates and from 2024-10-01 (`esearch`); assemblies under the
taxon (`datasets summary genome taxon`), against `config.yaml assemblies.taxa`; and for the
suspect ones, the evaluable records by species.

## Scope too broad

**`Serpentovirinae_PP1b_Uccellini_2014_PythonNido7F`, and its siblings `_PythonNido6F` and
`_PythonNodoF`.** The paper's table is titled for amplifying a 3,408 nt fragment of ball python
nidovirus. The entries' target is the whole subfamily with no scope. By species:

| entry | Ball python nidovirus (taxid 1986118) | everything else in the subfamily |
|---|---|---|
| `_PythonNido7F` | 5 detect | 7 detect, 14 fail, 2 reduced |
| `_PythonNido6F` | 4 detect, 1 reduced | 1 detect, 50 fail |
| `_PythonNodoF` | 4 detect | 8 detect, 32 fail |

Detection on the virus the primers were written for is 13 of 14 with the one miss `reduced`, on
very few records. Elsewhere in the subfamily 96 of 114 calls are `fail`. `_PythonNido6F` and
`_PythonNodoF` currently read `low coverage` on the site, and this is why. Much of the rest is `Serpentovirinae sp.`, an unresolved node, so a scope of
1986118 alone could drop records that are the same virus; that needs reading before it is set.
A curator's note of 2026-10-14 already questions whether these genome-walking primers belong in
a drift registry at all. That decision comes first.

## Cannot reach a source the taxon has

- **`Chlamydia_pneumoniae_16S_Messmer_1997_round2`.** The query returns 48 of 9,172 records for
  the taxon, and 9 of 245 since 2024-10-01. 30 complete or chromosome-level assemblies exist, and
  *Chlamydia* is not in `assemblies.taxa`. A genome carries 16S but is not titled for it. This is
  the same shape as the Chlamydia 16S share recorded on 2026-11-03.
- **`Batrachochytrium_dendrobatidis_mtDNA_Ghosh_2021_BdGPL`, `_BdCAPE`.** 9,491 records screened,
  8 and 9 evaluable, because the Ghosh sites are on few records (`no_site` on about 9,400; corrected the same day: most of those are `XM_` predicted mRNAs, not ITS, `2026-11-04-scope-reread.md`). 42 records are titled
  mitochondrial and 1 is over 5 kb. 9 assemblies exist, one chromosome-level (JEL423, 2025), and
  the taxon is not in `assemblies.taxa`. Whether those assemblies hold the mitochondrial contig
  has not been tested.
- **`Escherichia_coli_LT_Victor_1991`.** Already recorded on 2026-11-01: an unenriched genome
  sample misses a plasmid-borne pathotype gene.

## Narrow scope, a question for the maintainer

- **`Caliciviridae_capsid_Reid_1999`, `_helicase_Neill_1995`, `_RdRp_Neill_1995`.** Scope is the
  one species `Vesivirus exanthema`; retrieval is the family, 67,633 to 84,874 records for 49 to
  115 in scope. The capsid entry's note says the paper develops it for marine caliciviruses. Is
  the claim one species or the marine vesiviruses? Retrieval could also narrow to the genus
  whichever way that goes, since everything outside the scope is dropped anyway.
- **`Orthopoxvirus_G9R_Gallardo-Romero_2011`.** Scope is raccoonpox, volepox and skunkpox.
  Borealpox is a North American orthopoxvirus described after the paper. Noted 2026-11-01.
- **`Batravirus_terminase_Licheri_2020_european`, `_pan`.** Ranid herpesvirus 5 sits outside the
  taxon. Noted 2026-11-01.

## Low for honest reasons (22)

| assays | why |
|---|---|
| Intranuclear coccidium, Sunshinevirus x2, Leporid gammaherpesvirus 5 | few sequences exist: 2, 8 and 10 for the taxon, and the extra LepGHV5 records are its polymerase |
| *Eimeria furonis* | 12 of 17 records are 437 bp partials, `truncated` |
| EEHV3/4 x3, EEHV5 x3, EEHV6 | queries catch the genomes; each species has 1 to 83 records and none in the window |
| Ferlavirus x3 | query equals taxon, 64 records |
| *Vairimorpha apis* | query 78 of 1,030, but 1 of 3 in the window and 1 assembly |
| Bovine papular stomatitis virus | query 129 of 140 |
| Orthobornavirus passerine | scope is canary and estrildid bornavirus, as the entry states; the 1,275 outside are other orthobornaviruses |
| Mycoplasmatota 16S | named three species, 534 records; most are partials that do not span 994 bp |
| Ophidiomyces IGS, ITS2 | IGS on the roadmap already. ITS2: 88 assemblies not tested for the rDNA |
| *B. salamandrivorans* | archive holds all 12 deposited through October. 19 more were deposited 2026-11-01, after the fetch, and 7 of those seen are 444 bp clones, so the next run may lift this one |

## What did not get tested

Papers were not reopened for this pass. "Scope as the paper claims it" rests on curator notes
except where stated. Ophidiomyces ITS2 and the *B. dendrobatidis* assemblies were counted, not
screened.
