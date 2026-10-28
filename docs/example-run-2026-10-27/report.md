# AssayWatch report — 2026-10-27

188 assays screened: 42 declining, 34 low coverage, 7 watch, 30 insufficient data, 19 no recent data, 56 stable. 20 further screened assays are not scoreable and carry no status.

**In one line:** of 188 published assays re-checked against GenBank records deposited up to 2026-10-27, 42 appear to be detecting measurably less of their target than they once did, and 34 have never covered much of the taxon they are screened against. 10 are listed under Start here as worth looking at first.

**What cannot be said at all:** 69 of 208 screened assays carry no usable verdict -- 30 with too few recent records, 19 with nothing newly deposited, and 20 not scoreable at all. A further 26 are held off the triage list because their primer pools are so degenerate that an in-silico detection is close to a tautology. Sparsely sequenced targets are exactly the ones this tool is for, and they are the ones it can say least about.

**What this is not.** Every number here is a prediction from sequence alone: whether each oligo still matches what has been deposited, never whether the reaction still works at the bench. No assay was run in a laboratory. There is no thermodynamic model and no limit of detection, so this cannot tell a missed cycle-threshold cutoff from a faint band. A flag is a reason to pull an assay's records and look, never a result.

**The verdicts.** `declining` -- detection has fallen from a level that previously cleared the threshold. `low coverage` -- detection is below the threshold but was never measurably higher, usually an assay screened against more diversity than it was designed for. `watch` -- below the threshold, but the interval still reaches it, so there are too few records to be sure. `insufficient data` -- too few recent evaluable records to judge; never flagged. `no recent data` -- nothing new deposited in the window. `stable` -- no evidence of loss. `not scoreable` -- a registry problem, such as an unresolved product size, rather than anything about the assay.

Registry status: 178 active, 10 draft. `draft` is a maintainer sign-off, not a data check: 7 of the 10 drafts here already carry a verified DOI, a taxid and a design year with no open review question. What does vary between entries is oligo provenance, flagged in the note column of every row below.

**Duplication check:** 20 of 76 flagged assays still hold when duplicated records are discounted (each distinct binding-site footprint counted once, and the sample size cut to the number of footprints). The note on each assay that did not hold says which test it failed.

Previous successful run: 2026-10-26 (1 day earlier).

Recent window: 24 months, widened for 53 assays that held too few records; earliest shown Oct 2024; threshold 90% detected; at least 15 recent evaluable records to flag. Deprecated assays are not screened.

## Start here (10)

Of 76 flagged assays, these are ordered by how much can be acted
on: a measured fall before a scope gap, entries whose oligo provenance is not in
doubt first, then the largest shortfall below the threshold on the most records.

| assay | status | detected (recent) | 95% CI | evaluable | baseline (n) |
|---|---|---|---|---|---|
| `CDV_H_gene_Mueller_2011_1` | declining | 66.3% | 56%-75% | 95 | 94% (418) |
| `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` | declining | 6.5% | 6%-7% | 30382 | 21% (59909) |
| `Pan_flavivirus_NS5_3_round1` | declining | 35.4% | 34%-36% | 9489 | 45% (24647) |
| `West_Nile_Virus_Envelope_glycoprotein_E_Lanciotti_2001` | declining | 63.6% | 61%-66% | 1722 | 87% (5362) |
| `PARVOVIRUS_ssDNA_VP1_gene_dependovirus` | declining | 45.3% | 39%-51% | 256 | 72% (1772) |
| `Pan_coccidia_SSU_rDNA_negative_contro_Garner_2006` | low coverage | 23.8% | 22%-26% | 1653 | 36% (10186) |
| `Cryptosporidium_18SrDNA_Xiao_1999_round2` | low coverage | 71.6% | 65%-77% | 225 | 63% (1437) |
| `ARENAVIRUS_ssRNA_S_gene` | low coverage | 14.3% | 8%-24% | 70 | 39% (988) |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` | low coverage | 0.0% | 0%-0.6% | 650 | 0.3% (1715) |
| `POXVIRUSES_dsDNA_Polymerase` | low coverage | 4.1% | 4%-5% | 5142 | 3% (9346) |

Kept off this list but unchanged in the tables below: 26 are degeneracy high or severe, where in-silico detection is close to a tautology; 40 carry a flag the duplication check did not confirm.

`detected` means predicted to amplify (`detect` or `reduced`). The denominator is
evaluable records only: those where both primers landed in the right orientation and
size range. Records with no amplicon, or too many undetermined bases to judge, are
counted separately and excluded, so a bad sequencing year cannot look like drift.
Intervals are Wilson 95%, pooled and per lineage alike. A **pooled** flag needs the
upper bound of the recent interval to fall below the threshold. **Declining** means the
share has also fallen from the baseline (the interval for the change excludes zero):
that is drift. **Low coverage** means below threshold without a measurable fall: usually
an assay screened against more diversity than it was designed for.

A **lineage** can also flag an assay whose pooled share clears the threshold, and that
is the point of measuring per lineage: a pan-family assay can miss one clade entirely
while detecting most of what is deposited. Such a row is marked `pooled: <status>` and
its note names the lineage, its share and its own earlier share. The lineage rule is
not the pooled one: it is an exact binomial test against the threshold,
Holm-adjusted across that assay's lineages, so it is the looser of
the two and nothing controls error across assays. Read a lineage override as a reason to look at
that clade, not as a measurement of the assay.

## Declining (42)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `RETROVIRUS_RNA_polymerase_SIV_Keele_2009` | active | 0.0% | 0%-2% | 224 | 6% (3623) | 4x negligible | fails: too_few,change | detected share 0.0% (0%-2%) since Oct 2024, upper bound below the 90% threshold; change from baseline -7% to -5%. |
| `ABPV_capsid_Rossi_2024` | active | 5.6% | 1.0%-26% | 18 | 82% (106) | 4608x severe | fails: too_few | detected share 5.6% (1.0%-26%) since Oct 2024, upper bound below the 90% threshold; change from baseline -84% to -55%. 8 patent records excluded. |
| `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` | active | 6.5% | 6%-7% | 30382 | 21% (59909) | 32x moderate | holds | detected share 6.5% (6%-7%) since Oct 2024, upper bound below the 90% threshold; change from baseline -15% to -14%. Entry flags: oligos_modified. |
| `Pan_Plasmodium_sp_and_Haemopro_cytochrome_c` | active | 8.8% | 5%-14% | 148 | 16% (1625) | 1x negligible | fails: change | detected share 8.8% (5%-14%) since Oct 2024, upper bound below the 90% threshold; change from baseline -12% to -2%; separately, lineage Haemoproteus sp. (191679) (65 records) detects only 7.7% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: oligos_from_secondary_source, oligos_read_from_figure. 20251 out-of-scope records excluded. |
| `ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010` | active | 12.2% | 9%-16% | 361 | 49% (671) | 147456x severe | holds | detected share 12.2% (9%-16%) since Oct 2024, upper bound below the 90% threshold; change from baseline -42% to -32%; separately, lineage Orthoreovirus piscis (3431498) (182 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 52 patent records excluded. |
| `MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004` (pooled: low coverage) | active | 15.0% | 14%-16% | 4113 | 7% (8255) | 1x negligible | fails: too_few,change | pooled share 15.0% has low coverage, but lineage Orthopoxvirus monkeypox (3431483) (2409 records) detects 25.6% (23.9%-27.4%); lineage verdict overrides to declining. Entry flags: primer_site_polymorphic. 5 patent records excluded. |
| `RHABDOVIRUS_ssRNA_L_gene_round1` (pooled: low coverage) | active | 17.5% | 16%-20% | 1295 | 19% (5455) | 221184x severe | fails: change | pooled share 17.5% has low coverage, but lineage Lyssavirus rabies (11292) (968 records) detects only 15.3% (13.2%-17.7%), down from 17.7% on 3678 earlier records; lineage verdict overrides to declining. 769 out-of-scope records excluded. |
| `ENTEROVIRUS_ssRNA_VP3_VP1_round2` (pooled: low coverage) | active | 18.5% | 17%-20% | 4533 | 12% (35931) | 16384x severe | fails: change | pooled share 18.5% has low coverage, but lineage Enterovirus betacoxsackie (3428502) (1063 records) detects 67.6% (64.8%-70.4%); lineage verdict overrides to declining. Entry flags: amplicon_measured_not_published. 40 out-of-scope records excluded. |
| `Leucocytozoon_cyt_c_Hellgren_2004` (pooled: low coverage) | active | 25.9% | 19%-35% | 112 | 15% (1309) | 1x negligible | fails: change | pooled share 25.9% has low coverage, but lineage Leucocytozoon sp. (1504291) (88 records) detects 33.0% (24.0%-43.3%), down from 90.2% on 122 earlier records; lineage verdict overrides to declining. Entry flags: cross_reactive, orientation_inferred. |
| `Pan_flavivirus_NS5_3_round2` (pooled: low coverage) | active | 26.2% | 25%-27% | 9443 | 34% (24659) | 648x high | fails: change | pooled share 26.2% has low coverage, but lineage Orthoflavivirus japonicum (3048158) (186 records) detects only 3.8% (1.8%-7.6%), down from 58.3% on 494 earlier records; lineage verdict overrides to declining. Entry flags: oligos_from_secondary_source. 1 out-of-scope records excluded. |
| `Pan_flavivirus_NS5_3_round1` (pooled: low coverage) | active | 35.4% | 34%-36% | 9489 | 45% (24647) | 16x moderate | holds | pooled share 35.4% has low coverage, but lineage Orthoflavivirus usutuense (3048443) (428 records) detects only 0.0% (0.0%-0.9%), down from 12.3% on 592 earlier records; lineage verdict overrides to declining. Entry flags: amplicon_measured_not_published, oligos_from_secondary_source. 1 out-of-scope records excluded. |
| `DWVB_polyprotein_Rossi_2024` | active | 37.5% | 18%-61% | 16 | 90% (41) | 1x negligible | fails: too_few | detected share 37.5% (18%-61%) since Oct 2024, upper bound below the 90% threshold; change from baseline -73% to -26%. Entry flags: oligos_from_secondary_source, scope_narrower_than_taxid. |
| `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme` (pooled: low coverage) | draft | 38.7% | 36%-41% | 1743 | 46% (6250) | 384x high | fails: change | pooled share 38.7% has low coverage, but lineage Bat coronavirus (1508220) (172 records) detects only 25.0% (19.1%-32.0%), down from 73.9% on 176 earlier records; lineage verdict overrides to declining. Entry flags: oligos_modified. |
| `CIRCOVIRUSES_ssDNA_vertebrate_Rep_Gene_Mankertz_2000_round1` | active | 38.7% | 35%-42% | 679 | 56% (8702) | 1536x high | holds | detected share 38.7% (35%-42%) since Oct 2024, upper bound below the 90% threshold; change from baseline -21% to -14%; separately, lineage Circovirus canine (3047721) (33 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: orientation_inferred. 222 patent records excluded. |
| `Pan_mycoplasma_16S_23S_intergenic_space_Rebelo_2011` | active | 39.1% | 31%-47% | 138 | 51% (523) | 8x negligible | fails: change | detected share 39.1% (31%-47%) since Oct 2024, upper bound below the 90% threshold; change from baseline -21% to -3%. Entry flags: amplicon_multimodal. 55 patent records excluded. |
| `CDV_H_gene_Mueller_2011_4` | active | 44.8% | 35%-55% | 87 | 69% (276) | 1x negligible | fails: change | detected share 44.8% (35%-55%) since Oct 2024, upper bound below the 90% threshold; change from baseline -36% to -12%. Entry flags: pairing_is_curator_reading. 61 patent records excluded. |
| `PARVOVIRUS_ssDNA_VP1_gene_dependovirus` | active | 45.3% | 39%-51% | 256 | 72% (1772) | 1x negligible | holds | detected share 45.3% (39%-51%) since Oct 2024, upper bound below the 90% threshold; change from baseline -33% to -20%; separately, lineage Dependoparvovirus anseriform1 (1511895) (125 records) detects only 12.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: oligos_modified. 6845 patent records excluded. |
| `MONKEYPOX_dsDNA_G2R_WestAfrican_TaqMan_Li_2010` | draft | 45.9% | 44%-47% | 4351 | 95% (8109) | 1x negligible | fails: too_few | detected share 45.9% (44%-47%) since Oct 2024, upper bound below the 90% threshold; change from baseline -51% to -48%. 5 patent records excluded. 4 chance-pair records excluded (drift.chance_pair_test). |
| `CHLAMYDIA_trachomatis_16S_Messmer_1997_round2` | active | 46.2% | 32%-61% | 39 | 74% (323) | 1x negligible | fails: too_few,footprint,change | detected share 46.2% (32%-61%) since Oct 2024, upper bound below the 90% threshold; change from baseline -43% to -12%. Entry flags: primer_site_polymorphic. 1 patent records excluded. |
| `ARENAVIRUS_ssRNA_S_gene_2` (pooled: low coverage) | active | 47.1% | 39%-55% | 138 | 62% (1418) | 256x high | fails: change | pooled share 47.1% has low coverage, but lineage Mammarenavirus lassaense (3052310) (37 records) detects 75.7% (59.9%-86.6%); lineage verdict overrides to declining. Entry flags: oligos_modified, orientation_inferred. 473 out-of-scope records excluded. 226 patent records excluded. |
| `PD_WNS_ITS1_Shuey_2014` | active | 50.0% | 28%-72% | 16 | 86% (441) | 1x negligible | fails: too_few,change | detected share 50.0% (28%-72%) since Oct 2023, upper bound below the 90% threshold; change from baseline -58% to -14% (window widened to 36 months to reach 15 evaluable records). |
| `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_Lan_2010_round1` (pooled: low coverage) | active | 51.9% | 50%-54% | 1641 | 55% (5429) | 1327104x severe | fails: change | pooled share 51.9% has low coverage, but lineage Alphacoronavirus chicagoense (3433756) (165 records) detects only 0.0% (0.0%-2.3%), down from 21.4% on 168 earlier records; lineage verdict overrides to declining. 262 out-of-scope records excluded. |
| `SBV_polyprotein_Rossi_2024` | active | 52.4% | 38%-67% | 42 | 87% (323) | 6x negligible | fails: too_few | detected share 52.4% (38%-67%) since Oct 2024, upper bound below the 90% threshold; change from baseline -50% to -20%. Entry flags: oligos_from_secondary_source. 1 patent records excluded. |
| `CDV_N_gene_Elia_2006` (pooled: low coverage) | active | 57.1% | 48%-66% | 105 | 51% (554) | 1x negligible | fails: change | pooled share 57.1% has low coverage, but lineage Morbillivirus canis (3052342) (105 records) detects 57.1% (47.6%-66.2%); lineage verdict overrides to declining. Entry flags: amplicon_disagrees_with_paper, citation_is_indirect, oligos_from_secondary_source. 61 patent records excluded. |
| `MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010` (pooled: low coverage) | draft | 57.9% | 56%-59% | 4328 | 7% (7987) | 1x negligible | fails: too_few,footprint,change | pooled share 57.9% has low coverage, but lineage Orthopoxvirus monkeypox (3431483) (4163 records) detects 60.2% (58.7%-61.7%); lineage verdict overrides to declining. 5 patent records excluded. |
| `E_coli_malB_Candrian_1991` | active | 59.2% | 45%-72% | 49 | 74% (277) | 1x negligible | fails: too_few,change | detected share 59.2% (45%-72%) since Oct 2024, upper bound below the 90% threshold; change from baseline -30% to -1%. Entry flags: orientation_inferred. |
| `INFLUENZA_A_ssRNA_NP_Tsukamoto_2010` (pooled: low coverage) | active | 60.7% | 60%-61% | 69571 | 61% (117340) | 128x moderate | fails: change | pooled share 60.7% has low coverage, but lineage Alphainfluenzavirus influenzae (2955291) (69561 records) detects 60.7% (60.4%-61.1%), down from 60.9% on 117286 earlier records; lineage verdict overrides to declining. Entry flags: retrieval_scope_incomplete. |
| `FILOVIRUS_ssRNA_L_gene` | active | 62.1% | 52%-71% | 95 | 98% (3818) | 2x negligible | fails: too_few,footprint | detected share 62.1% (52%-71%) since Oct 2024, upper bound below the 90% threshold; change from baseline -46% to -27%; separately, lineage Orthoebolavirus bundibugyoense (3052458) (35 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: pairing_is_curator_reading. 85 patent records excluded. |
| `Pan_hemoparasite_cytochrome_c_Hellgren_2004` | active | 62.4% | 55%-69% | 194 | 79% (829) | 1x negligible | fails: change | detected share 62.4% (55%-69%) since Oct 2024, upper bound below the 90% threshold; change from baseline -24% to -9%. Entry flags: oligos_not_in_cited_paper, orientation_inferred. 13071 out-of-scope records excluded. |
| `West_Nile_Virus_Envelope_glycoprotein_E_Lanciotti_2001` | active | 63.6% | 61%-66% | 1722 | 87% (5362) | 1x negligible | holds | detected share 63.6% (61%-66%) since Oct 2024, upper bound below the 90% threshold; change from baseline -26% to -21%. Entry flags: oligos_modified. 89 patent records excluded. |
| `BQCV_capsid_Rossi_2024` | active | 65.1% | 57%-72% | 152 | 83% (1057) | 1x negligible | fails: change | detected share 65.1% (57%-72%) since Oct 2024, upper bound below the 90% threshold; change from baseline -26% to -11%. Entry flags: oligos_from_secondary_source. 3 patent records excluded. |
| `RHABDOVIRUS_ssRNA_L_gene_round2` (pooled: low coverage) | active | 66.2% | 64%-69% | 1271 | 66% (5352) | 36864x severe | fails: change | pooled share 66.2% has low coverage, but lineage Lyssavirus rabies (11292) (939 records) detects 68.8% (65.8%-71.7%); lineage verdict overrides to declining. Entry flags: oligos_from_secondary_source. 769 out-of-scope records excluded. |
| `CDV_H_gene_Mueller_2011_1` | active | 66.3% | 56%-75% | 95 | 94% (418) | 2x negligible | holds | detected share 66.3% (56%-75%) since Oct 2024, upper bound below the 90% threshold; change from baseline -38% to -19%. 61 patent records excluded. |
| `CDV_H_gene_Mueller_2011_2` (pooled: low coverage) | active | 66.5% | 59%-73% | 188 | 64% (1744) | 1x negligible | fails: change | pooled share 66.5% has low coverage, but lineage Morbillivirus canis (3052342) (188 records) detects 66.5% (59.5%-72.8%); lineage verdict overrides to declining. Entry flags: pairing_is_curator_reading. 61 patent records excluded. |
| `Pan_HERPES_dsDNA_Polymerase_round2` | active | 71.4% | 67%-76% | 357 | 80% (3350) | 12288x severe | fails: change | detected share 71.4% (67%-76%) since Oct 2024, upper bound below the 90% threshold; change from baseline -14% to -4%. Entry flags: orientation_inferred. 2 out-of-scope records excluded. |
| `PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999` (pooled: low coverage) | active | 73.2% | 71%-75% | 1591 | 54% (14684) | 288x high | fails: change | pooled share 73.2% has low coverage, but lineage Alphapapillomavirus 9 (337041) (320 records) detects only 12.8% (9.6%-16.9%), down from 43.5% on 9521 earlier records; lineage verdict overrides to declining. Entry flags: orientation_inferred. 1064 patent records excluded. |
| `CDV_P_gene_Scagliarini_2007` (pooled: low coverage) | active | 75.3% | 66%-83% | 93 | 71% (509) | 1x negligible | fails: change | pooled share 75.3% has low coverage, but lineage Morbillivirus canis (3052342) (93 records) detects 75.3% (65.6%-82.9%); lineage verdict overrides to declining. 61 patent records excluded. |
| `ADENOVIRUS_dsDNA_Hexon_gene` (pooled: low coverage) | active | 76.3% | 74%-78% | 1499 | 68% (4736) | 16x moderate | fails: change | pooled share 76.3% has low coverage, but lineage Mastadenovirus caesari (3241411) (185 records) detects only 65.4% (58.3%-71.9%), down from 71.1% on 795 earlier records; lineage verdict overrides to declining. Entry flags: cross_reactive. 1043 patent records excluded. |
| `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2` (pooled: low coverage) | active | 79.2% | 77%-81% | 1569 | 69% (5313) | 12288x severe | fails: change | pooled share 79.2% has low coverage, but lineage Betacoronavirus sp. (1928434) (47 records) detects only 19.1% (10.4%-32.5%), down from 100.0% on 15 earlier records; lineage verdict overrides to declining. 262 out-of-scope records excluded. |
| `Pan_HERPES_dsDNA_Terminase_round2` | active | 79.5% | 75%-83% | 331 | 92% (2790) | 128x moderate | fails: recent | detected share 79.5% (75%-83%) since Oct 2024, upper bound below the 90% threshold; change from baseline -18% to -9%; separately, lineage Varicellovirus humanalpha3 (3050294) (54 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 1 out-of-scope records excluded. |
| `HANTAVIRUS_ssRNA_S_segment` (pooled: watch) | active | 88.0% | 85%-91% | 443 | 96% (3848) | 31104x severe | fails: recent | pooled share 88.0% is above the 90% threshold, but lineage Orthohantavirus tulaense (3052503) (102 records) detects only 64.7% (55.1%-73.3%), down from 93.3% on 386 earlier records; lineage verdict overrides to declining. Entry flags: nested_protocol. 83 patent records excluded. |
| `ALPHAVIRUSES_Togaviridae_ssRNA_NSP4_gene_round2` (pooled: stable) | active | 98.8% | 98%-99% | 3885 | 94% (4845) | 256x high | fails: recent,change | pooled share 98.8% is above the 90% threshold, but lineage Alphavirus getah (3426303) (97 records) detects only 82.5% (73.7%-88.8%), down from 88.1% on 118 earlier records; lineage verdict overrides to declining. 339 patent records excluded. |

## Low Coverage (34)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `AVIPOXVIRUS_dsDNA_4b_core_Baek_2020` | active | 0.0% | 0%-5% | 78 | 0.3% (1005) | 1x negligible | fails: too_few | detected share 0.0% (0%-5%) since Oct 2024, upper bound below the 90% threshold; change from baseline -0.9% to +4% (no measurable fall from a baseline of 0.3%). Entry flags: scope_narrower_than_taxid. 7 patent records excluded. |
| `Apicoplast_23S_LSU_Large_subunit_Molecular_2005` | active | 0.0% | 0%-12% | 27 | 0% (85) | 8x negligible | fails: too_few | detected share 0.0% (0%-12%) since Oct 2024, upper bound below the 90% threshold; change from baseline -4% to +12% (no measurable fall from a baseline of 0%). Entry flags: cross_reactive. |
| `Helicobacter_16S_Conley_2021` | active | 0.0% | 0%-5% | 75 | 0% (1080) | 1x negligible | fails: too_few | detected share 0.0% (0%-5%) since Oct 2024, upper bound below the 90% threshold; change from baseline -0.4% to +5% (no measurable fall from a baseline of 0%). Entry flags: amplicon_disagrees_with_paper, cross_reactive, retrieval_scope_incomplete, scope_narrower_than_taxid, thin_evidence. 1 patent records excluded. |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` | active | 0.0% | 0%-0.6% | 650 | 0.3% (1715) | 128x moderate | holds | detected share 0.0% (0%-0.6%) since Oct 2024, upper bound below the 90% threshold; change from baseline -0.7% to +0.3% (no measurable fall from a baseline of 0.3%); separately, lineage Betapolyomavirus hominis (1891762) (548 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: nested_protocol. 7 out-of-scope records excluded. 372 patent records excluded. |
| `RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009` | active | 0.0% | 0%-2% | 226 | 3% (5073) | 144x high | fails: too_few | detected share 0.0% (0%-2%) since Oct 2024, upper bound below the 90% threshold; change from baseline -4% to -1% (fell less than the 5% that counts as declining, from a baseline of 3%); separately, lineage Lentivirus simimdef (3418654) (226 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: amplicon_measured_not_published. |
| `ORTHOBUNYAVIRUS_ssRNA_M_segment_internal_Briese_2007` | active | 0.3% | 0.1%-2% | 296 | 31% (262) | 4096x high | fails: too_few | detected share 0.3% (0.1%-2%) since Oct 2024, upper bound below the 90% threshold; change from baseline -36% to -25% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 31%); separately, lineage Orthobunyavirus oropoucheense (3052429) (278 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round2` | active | 2.0% | 1%-3% | 944 | 9% (5658) | 1536x high | holds | detected share 2.0% (1%-3%) since Oct 2024, upper bound below the 90% threshold; change from baseline -8% to -6% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 9%); separately, lineage Betapolyomavirus hominis (1891762) (811 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: amplicon_measured_not_published, nested_protocol. Same oligos as POLYOMAVIRUS_dsDNA_VP1_Johne_2005. 7 out-of-scope records excluded. 372 patent records excluded. |
| `POLYOMAVIRUS_dsDNA_VP1_Johne_2005` | active | 2.0% | 1%-3% | 944 | 9% (5658) | 1536x high | holds | detected share 2.0% (1%-3%) since Oct 2024, upper bound below the 90% threshold; change from baseline -8% to -6% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 9%); separately, lineage Betapolyomavirus hominis (1891762) (811 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: nested_protocol. Same oligos as POLYOMAVIRUS_dsDNA_PREDICT_VP1_round2. 7 out-of-scope records excluded. 372 patent records excluded. |
| `POXVIRUSES_dsDNA_Polymerase` | active | 4.1% | 4%-5% | 5142 | 3% (9346) | 1x negligible | holds | detected share 4.1% (4%-5%) since Oct 2024, upper bound below the 90% threshold; change from baseline +0.9% to +2% (rose from a baseline of 3%); separately, lineage Orthopoxvirus monkeypox (3431483) (4869 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 735 patent records excluded. |
| `Snake_nidovirus_PP1b_Uccellini_2014_2` | active | 4.3% | 0.8%-21% | 23 | 14% (37) | 1x negligible | fails: too_few | detected share 4.3% (0.8%-21%) since Oct 2023, upper bound below the 90% threshold; change from baseline -24% to +9% (no measurable fall from a baseline of 14%) (window widened to 36 months to reach 15 evaluable records). Entry flags: pairing_is_curator_reading. 11 patent records excluded. |
| `ORTHOBUNYAVIRUS_ssRNA_M_segment` | active | 5.0% | 0.9%-24% | 20 | 29% (207) | 192x high | fails: too_few | detected share 5.0% (0.9%-24%) since Oct 2022, upper bound below the 90% threshold; change from baseline -31% to -4% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 29%) (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_multimodal. |
| `ORTHOBUNYAVIRUS_ssRNA_L_segment_Briese_2007` | active | 13.0% | 5%-32% | 23 | 30% (169) | 64x moderate | fails: too_few | detected share 13.0% (5%-32%) since Oct 2022, upper bound below the 90% threshold; change from baseline -28% to +4% (no measurable fall from a baseline of 30%) (window widened to 48 months to reach 15 evaluable records). |
| `ARENAVIRUS_ssRNA_S_gene` | active | 14.3% | 8%-24% | 70 | 39% (988) | 8x negligible | holds | detected share 14.3% (8%-24%) since Oct 2024, upper bound below the 90% threshold; change from baseline -32% to -14% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 39%). Entry flags: orientation_inferred. 473 out-of-scope records excluded. 226 patent records excluded. |
| `Snake_nidovirus_PP1b_Uccellini_2014_3` | active | 17.6% | 6%-41% | 17 | 33% (27) | 1x negligible | fails: too_few | detected share 17.6% (6%-41%) since Oct 2023, upper bound below the 90% threshold; change from baseline -38% to +12% (no measurable fall from a baseline of 33%) (window widened to 36 months to reach 15 evaluable records). 11 patent records excluded. |
| `Pan_coccidia_SSU_rDNA_negative_contro_Garner_2006` | active | 23.8% | 22%-26% | 1653 | 36% (10186) | 128x moderate | holds | detected share 23.8% (22%-26%) since Oct 2024, upper bound below the 90% threshold; change from baseline -14% to -10% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 36%). Entry flags: cross_reactive. |
| `ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010_round1` | active | 24.0% | 20%-29% | 358 | 50% (627) | 331776x severe | holds | detected share 24.0% (20%-29%) since Oct 2024, upper bound below the 90% threshold; change from baseline -32% to -20% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 50%); separately, lineage Orthoreovirus piscis (3431498) (182 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: pairing_is_curator_reading. 52 patent records excluded. |
| `DWVA_polyprotein_Rossi_2024` | active | 25.0% | 13%-43% | 28 | 80% (40) | 1x negligible | fails: too_few | detected share 25.0% (13%-43%) since Oct 2024, upper bound below the 90% threshold; change from baseline -71% to -31% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 80%). Entry flags: oligos_from_secondary_source, scope_narrower_than_taxid. |
| `ORTHOBUNYAVIRUS_ssRNA_S_segment` | active | 26.7% | 11%-52% | 15 | 34% (166) | 1x negligible | fails: too_few | detected share 26.7% (11%-52%) since Oct 2022, upper bound below the 90% threshold; change from baseline -25% to +19% (no measurable fall from a baseline of 34%) (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_multimodal. |
| `CIRCOVIRUSES_ssDNA_vertebrate_Rep_Gene_round2` | active | 30.7% | 28%-34% | 748 | 39% (8657) | 1536x high | holds | detected share 30.7% (28%-34%) since Oct 2024, upper bound below the 90% threshold; change from baseline -11% to -4% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 39%); separately, lineage Circovirus pigeon (3050342) (69 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: orientation_inferred. 222 patent records excluded. |
| `SSU_rRNA_gene_Plasmodium_SSU_rDNA_Grim_2003` | active | 31.8% | 16%-53% | 22 | 47% (712) | 1x negligible | fails: too_few,footprint | detected share 31.8% (16%-53%) since Oct 2023, upper bound below the 90% threshold; change from baseline -31% to +6% (no measurable fall from a baseline of 47%) (window widened to 36 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published. |
| `ASTROVIRUS_RdRp_Chu_2008_round1` | active | 34.6% | 31%-38% | 691 | 48% (2234) | 2048x high | holds | detected share 34.6% (31%-38%) since Oct 2024, upper bound below the 90% threshold; change from baseline -18% to -9% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 48%); lineage Mamastrovirus suisencephalomyelitidis (3703181) (35 records) detects only 8.6%, but neither it nor the pooled share ever cleared the threshold, so there is no fall to call a decline. Entry flags: amplicon_measured_not_published, nested_protocol. 29 patent records excluded. |
| `CHLAMYDIA_genus_16S_Messmer_1997_round1` | active | 40.7% | 31%-51% | 86 | 39% (728) | 1x negligible | fails: too_few | detected share 40.7% (31%-51%) since Oct 2024, upper bound below the 90% threshold; change from baseline -9% to +13% (no measurable fall from a baseline of 39%); separately, lineage Chlamydia trachomatis (813) (39 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: primer_site_polymorphic, scope_narrower_than_taxid. 1 patent records excluded. |
| `SARCOCYSTIS_18S_5_8s_rDNA_short_Kutkiene_2010` | active | 61.1% | 39%-80% | 18 | 47% (172) | 16x moderate | fails: too_few | detected share 61.1% (39%-80%) since Oct 2022, upper bound below the 90% threshold; change from baseline -10% to +34% (no measurable fall from a baseline of 47%) (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_multimodal. |
| `Paramyxovirinae_Polymerase_L_gene_round2` | active | 61.7% | 60%-63% | 3971 | 10% (4906) | 384x high | holds | detected share 61.7% (60%-63%) since Oct 2024, upper bound below the 90% threshold; change from baseline +50% to +53% (rose from a baseline of 10%); separately, lineage Morbillivirus canis (3052342) (84 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 73 out-of-scope records excluded. |
| `AVIPOXVIRUS_dsDNA_4b_core_Farias_2010` | active | 62.5% | 43%-79% | 24 | 77% (228) | 1x negligible | fails: too_few | detected share 62.5% (43%-79%) since Oct 2024, upper bound below the 90% threshold; change from baseline -35% to +3% (no measurable fall from a baseline of 77%). Entry flags: amplicon_disagrees_with_paper. 7 patent records excluded. 1 chance-pair records excluded (drift.chance_pair_test). |
| `Cryptosporidium_18SrDNA_Xiao_1999_round2` | active | 71.6% | 65%-77% | 225 | 63% (1437) | 1x negligible | holds | detected share 71.6% (65%-77%) since Oct 2024, upper bound below the 90% threshold; change from baseline +2% to +14% (rose from a baseline of 63%). |
| `Paramyxovirinae_Polymerase_L_gene_Tong_2008_round1` | active | 72.3% | 71%-74% | 4278 | 36% (6505) | 768x high | holds | detected share 72.3% (71%-74%) since Oct 2024, upper bound below the 90% threshold; change from baseline +35% to +38% (rose from a baseline of 36%); separately, lineage Orthorubulavirus hominis (3052556) (126 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 73 out-of-scope records excluded. |
| `Encephalitozoon_18S_General_Encephalitoz_Muller_1999` | active | 72.7% | 56%-85% | 33 | 71% (83) | 1x negligible | fails: too_few,recent,footprint | detected share 72.7% (56%-85%) since Oct 2022, upper bound below the 90% threshold; change from baseline -17% to +18% (no measurable fall from a baseline of 71%) (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published. 4 patent records excluded. |
| `ASTROVIRUS_RdRp_Chu_2008_round2` | active | 78.4% | 75%-81% | 716 | 78% (2591) | 1536x high | holds | detected share 78.4% (75%-81%) since Oct 2024, upper bound below the 90% threshold; change from baseline -3% to +4% (no measurable fall from a baseline of 78%); separately, lineage Goose astrovirus (1349999) (46 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: nested_protocol. 29 patent records excluded. |
| `ADENOVIRUS_dsDNA_Polymerase_Primate_speci` | active | 84.9% | 83%-87% | 1086 | 74% (2936) | 1x negligible | fails: recent | detected share 84.9% (83%-87%) since Oct 2024, upper bound below the 90% threshold; change from baseline +8% to +14% (rose from a baseline of 74%); separately, lineage Mastadenovirus faecale (3241426) (100 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 1012 patent records excluded. |
| `ADENOVIRUS_dsDNA_Hexon_gene_round2` | active | 87.9% | 86%-89% | 1427 | 89% (4267) | 8x negligible | fails: recent | detected share 87.9% (86%-89%) since Oct 2024, upper bound below the 90% threshold; change from baseline -3% to +0.8% (no measurable fall from a baseline of 89%); separately, lineage Aviadenovirus hepatitidis (3426530) (49 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 1043 patent records excluded. |
| `ADENOVIRUS_dsDNA_Polymerase_Primate_speci_Casas_2005` (pooled: stable) | active | 90.6% | 89%-92% | 1079 | 78% (2875) | 16x moderate | fails: recent | detected share 90.6% (89%-92%) since Oct 2024; separately, lineage Mastadenovirus faecale (3241426) (103 records) detects only 43.7% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 1012 patent records excluded. |
| `Morbillivirus_including_CDV_P_gene` (pooled: stable) | active | 95.6% | 95%-96% | 2820 | 79% (2118) | 1x negligible | fails: recent | detected share 95.6% (95%-96%) since Oct 2024; separately, lineage Morbillivirus caprinae (3052343) (81 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: amplicon_measured_not_published. Same oligos as Morbillivirus_including_CDV_P_gene_Barrett_2003. 181 patent records excluded. |
| `Morbillivirus_including_CDV_P_gene_Barrett_2003` (pooled: stable) | active | 95.6% | 95%-96% | 2820 | 79% (2118) | 1x negligible | fails: recent | detected share 95.6% (95%-96%) since Oct 2024; separately, lineage Morbillivirus caprinae (3052343) (81 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Same oligos as Morbillivirus_including_CDV_P_gene. 181 patent records excluded. |

## Watch (7)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `SARCOCYSTIS_18S_5_8s_rDNA_long_2010` | active | 80.0% | 55%-93% | 15 | 99% (154) | 1x negligible | - | detected share 80.0% is below the 90% threshold, but its interval (55%-93%) still reaches it (window widened to 48 months to reach 15 evaluable records). |
| `VIBRIO_coralliilyticus_dnaJ_Pollock_2010` | active | 80.0% | 55%-93% | 15 | 61% (56) | 2x negligible | - | detected share 80.0% is below the 90% threshold, but its interval (55%-93%) still reaches it. Entry flags: primer_site_polymorphic. |
| `RANAVIRUS_dsDNA_variable_intergenic_regi_Pallister_2007` | active | 84.7% | 75%-91% | 72 | 90% (178) | 1x negligible | - | detected share 84.7% is below the 90% threshold, but its interval (75%-91%) still reaches it. Entry flags: amplicon_multimodal, oligos_from_secondary_source. |
| `Entamoeba_18S_small_subunit_SSU` | draft | 87.5% | 78%-93% | 80 | 98% (134) | 288x high | - | detected share 87.5% is below the 90% threshold, but its interval (78%-93%) still reaches it (window widened to 48 months to reach 15 evaluable records). Entry flags: oligos_modified. |
| `RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Johnson_2008` | active | 89.5% | 81%-95% | 76 | 80% (250) | 1x negligible | - | detected share 89.5% is below the 90% threshold, but its interval (81%-95%) still reaches it. Entry flags: amplicon_disagrees_with_paper, oligos_from_secondary_source. |
| `MONKEYPOX_dsDNA_F3L_MGB_Kulesh_2004` | active | 89.7% | 89%-91% | 4469 | 99% (8564) | 1x negligible | - | detected share 89.7% is below the 90% threshold, but its interval (89%-91%) still reaches it. 5 patent records excluded. |
| `RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007` | active | 89.9% | 81%-95% | 79 | 81% (273) | 1x negligible | - | detected share 89.9% is below the 90% threshold, but its interval (81%-95%) still reaches it. Entry flags: amplicon_measured_not_published, oligos_read_from_figure. |

## Insufficient Data (30)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `B_salamandrivorans_Internal_transcribes_spa_Blooi_2013` | active | 0.0% | 0%-43% | 5 | 100% (1) | 1x negligible | - | 5 evaluable records since Oct 2024, below the minimum of 15; the detected share is 0% (0%-43%), too wide to act on. Entry flags: oligos_from_secondary_source. |
| `CHYTRID_Bd_mtDNA_lineage_BdCAPE_Ghosh_2021` | active | 0.0% | 0%-56% | 3 | 0% (6) | 1x negligible | - | 3 evaluable records since Oct 2024, below the minimum of 15; the detected share is 0% (0%-56%), too wide to act on. Entry flags: oligos_read_from_figure, scope_narrower_than_taxid. 2 patent records excluded. |
| `Pan_reptilian_paramyxovirus_HN_gene_Ahne_1999` | active | 0.0% | 0%-39% | 6 | 18% (22) | 1x negligible | - | 6 evaluable records since Oct 2021, below the minimum of 15; the detected share is 0% (0%-39%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published. 3 patent records excluded. |
| `Pan_reptilian_paramyxovirus_L_Ahne_1999` | active | 0.0% | 0%-39% | 6 | 43% (14) | 1x negligible | - | 6 evaluable records since Oct 2021, below the minimum of 15; the detected share is 0% (0%-39%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. 3 patent records excluded. |
| `Pan_reptilian_paramyxovirus_L_Ahne_1999_2` | active | 0.0% | 0%-39% | 6 | 25% (16) | 1x negligible | - | 6 evaluable records since Oct 2021, below the minimum of 15; the detected share is 0% (0%-39%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. 3 patent records excluded. |
| `LMBV_dsDNA_MCP_Grizzle_2003` | active | 16.7% | 5%-45% | 12 | 45% (22) | 1x negligible | - | 12 evaluable records since Oct 2021, below the minimum of 15; the detected share is 17% (5%-45%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `ORTHOBUNYAVIRUS_ssRNA_M_segment_5prime_Briese_2007` | active | 21.4% | 8%-48% | 14 | 7% (76) | 128x moderate | - | 14 evaluable records since Oct 2021, below the minimum of 15; the detected share is 21% (8%-48%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Reptarenavirus_GP_Aqrawi_2015` | active | 22.2% | 6%-55% | 9 | 59% (105) | 16x moderate | - | 9 evaluable records since Oct 2021, below the minimum of 15; the detected share is 22% (6%-55%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. |
| `Snake_nidovirus_PP1b_Uccellini_2014_1` | active | 40.0% | 17%-69% | 10 | 33% (18) | 1x negligible | - | 10 evaluable records since Oct 2021, below the minimum of 15; the detected share is 40% (17%-69%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: pairing_is_curator_reading. 11 patent records excluded. |
| `ORTHOBORNAVIRUS_XP_passerine_Sigrist_2021` | active | 50.0% | 15%-85% | 4 | 78% (23) | 64x moderate | - | 4 evaluable records since Oct 2021, below the minimum of 15; the detected share is 50% (15%-85%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: cross_reactive, oligos_read_from_figure. 1275 out-of-scope records excluded. |
| `Ferlavirus_L_gene_Hyndman_2012` | active | 57.1% | 25%-84% | 7 | 41% (46) | 1x negligible | - | 7 evaluable records since Oct 2021, below the minimum of 15; the detected share is 57% (25%-84%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. 3 patent records excluded. |
| `Encephalitozoon_Polar_tube_protein_E_cun_Xiao_2001` | active | 58.3% | 32%-81% | 12 | 43% (23) | 1x negligible | - | 12 evaluable records since Oct 2021, below the minimum of 15; the detected share is 58% (32%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_multimodal, thin_evidence. 3 patent records excluded. |
| `PROBOSCIVIRUS_POL_Latimer_2010_panEEHV_round1` | active | 58.3% | 32%-81% | 12 | 65% (20) | 1024x high | - | 12 evaluable records since Oct 2021, below the minimum of 15; the detected share is 58% (32%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Snake_fungus_Ophidiomyces_ophi_ITS2_28S_Bohuski_2015` | active | 62.5% | 31%-86% | 8 | 100% (17) | 1x negligible | - | 8 evaluable records since Oct 2021, below the minimum of 15; the detected share is 62% (31%-86%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `BPSV_dsDNA_RPO147_J6R_TaqMan_Zhao_2013` | draft | 77.8% | 45%-94% | 9 | 100% (10) | 1x negligible | - | 9 evaluable records since Oct 2021, below the minimum of 15; the detected share is 78% (45%-94%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published, chemistry_detail_missing, cross_reactive, thin_evidence. 2 patent records excluded. |
| `PROBOSCIVIRUS_POL_Latimer_2010_panEEHV_round2` | active | 92.9% | 69%-99% | 14 | 100% (25) | 1024x high | - | 14 evaluable records since Oct 2021, below the minimum of 15; the detected share is 93% (69%-99%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `CHLAMYDIA_pneumoniae_16S_Messmer_1997_round2` | active | 100.0% | 57%-100% | 5 | 100% (11) | 1x negligible | - | 5 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (57%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `CHYTRID_Bd_mtDNA_lineage_BdGPL_Ghosh_2021` | active | 100.0% | 34%-100% | 2 | 33% (6) | 1x negligible | - | 2 evaluable records since Oct 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on. Entry flags: oligos_read_from_figure, scope_narrower_than_taxid. 2 patent records excluded. |
| `Cryptosporidium_18SrDNA_Xiao_1999_round1` | active | 100.0% | 78%-100% | 14 | 92% (131) | 1x negligible | - | 14 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (78%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_modified. |
| `E_coli_ETEC_LT_Victor_1991` | active | 100.0% | 21%-100% | 1 | 96% (27) | 1x negligible | - | 1 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (21%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: citation_is_indirect, oligos_from_secondary_source, orientation_inferred. |
| `E_coli_O157_hlyA_Wang_1997` | active | 100.0% | 34%-100% | 2 | 100% (96) | 1x negligible | - | 2 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. |
| `MYCOPLASMA_16S_Turtles_only_Feldman_2006` | active | 100.0% | 34%-100% | 2 | 100% (27) | 1x negligible | - | 2 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `NOSEMA_apis_SSU_Martin-Hernandez_2007` | active | 100.0% | 51%-100% | 4 | 100% (19) | 1x negligible | - | 4 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (51%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_read_from_figure. |
| `NOSEMA_bombi_SSU_Kato_2020` | active | 100.0% | 70%-100% | 9 | 74% (72) | 1x negligible | - | 9 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (70%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_from_secondary_source. |
| `PARANANNIZZIOPSIS_ITS_Lorch_2023` | active | 100.0% | 72%-100% | 10 | 100% (20) | 1x negligible | - | 10 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (72%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `PROBOSCIVIRUS_POL_Latimer_2010_EEHV34_round1` | active | 100.0% | 34%-100% | 2 | 78% (9) | 1x negligible | - | 2 evaluable records since Oct 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on. |
| `PROBOSCIVIRUS_POL_Latimer_2010_EEHV34_round2` | active | 100.0% | 34%-100% | 2 | 100% (10) | 1x negligible | - | 2 evaluable records since Oct 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on. |
| `PROBOSCIVIRUS_POL_Latimer_2010_EEHV34_round3` | active | 100.0% | 51%-100% | 4 | 91% (11) | 1x negligible | - | 4 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (51%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Pan_reptilian_paramyxovirus_HN_gene_Ahne_1999_round2` | active | 100.0% | 61%-100% | 6 | 79% (24) | 1x negligible | - | 6 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (61%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published. 3 patent records excluded. |
| `REPTARENAVIRUS_S_segment_GP2_Baggio_2023` | active | 100.0% | 70%-100% | 9 | 95% (105) | 1x negligible | - | 9 evaluable records since Oct 2021, below the minimum of 15; the detected share is 100% (70%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: pooled_as_one_assay. |

## No Recent Data (19)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `BATRAVIRUS_terminase_Licheri_2020_european_FW2_RV1` | active | - | - | 0 | 100% (4) | 128x moderate | - | no evaluable records deposited since Oct 2024. Entry flags: scope_narrower_than_taxid. 4 out-of-scope records excluded. |
| `BATRAVIRUS_terminase_Licheri_2020_pan_FW4_RV4` | active | - | - | 0 | 100% (8) | 995328x severe | - | no evaluable records deposited since Oct 2024. |
| `CALICIVIRUS_ssRNA_Capsid` | active | - | - | 0 | 82% (11) | 1x negligible | - | no evaluable records deposited since Oct 2024. 67551 out-of-scope records excluded. |
| `CALICIVIRUS_ssRNA_RdRp_Neill_Seal_1995` | draft | - | - | 0 | 40% (25) | 1x negligible | - | no evaluable records deposited since Oct 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: thin_evidence. 84725 out-of-scope records excluded. 4 patent records excluded. |
| `INFLUENZA_A_ssRNA_HA_H5_Tsukamoto_2010` | active | - | - | 0 | 87% (7600) | 8192x severe | - | no evaluable records deposited since Oct 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_multimodal, retrieval_scope_incomplete. |
| `INFLUENZA_A_ssRNA_HA_H7_Tsukamoto_2010` | active | - | - | 0 | 56% (3290) | 12288x severe | - | no evaluable records deposited since Oct 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: primer_site_polymorphic, retrieval_scope_incomplete. |
| `LEPORID_GAMMAHERPESVIRUS_5_gB_Abade_dos_Santos_2021_taqman` | active | - | - | 0 | 100% (5) | 1x negligible | - | no evaluable records deposited since Oct 2024. Entry flags: shares_oligos_with_sibling. |
| `NA_ORTHOPOX_dsDNA_G9R_myristylated_TaqMan_Gallardo_Romero_2011` | draft | - | - | 0 | 100% (7) | 384x high | - | no evaluable records deposited since Oct 2024. Entry flags: thin_evidence. 18244 out-of-scope records excluded. |
| `PERKINSEA_NAG01_18S_cladeAC_Smilansky_2021` | active | - | - | 0 | 50% (391) | 4x negligible | - | no evaluable records deposited since Oct 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_from_secondary_source. 1389 out-of-scope records excluded. |
| `PERKINSEA_NAG01_18S_cladeD_Smilansky_2021` | active | - | - | 0 | 42% (391) | 4x negligible | - | no evaluable records deposited since Oct 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_from_secondary_source, retrieval_scope_incomplete. 1389 out-of-scope records excluded. |
| `PROBOSCIVIRUS_POL_Latimer_2010_EEHV5_round1` | active | - | - | 0 | 100% (9) | 1x negligible | - | no evaluable records deposited since Oct 2024. |
| `PROBOSCIVIRUS_POL_Latimer_2010_EEHV5_round2` | active | - | - | 0 | 100% (14) | 1x negligible | - | no evaluable records deposited since Oct 2024. |
| `PROBOSCIVIRUS_POL_Latimer_2010_EEHV5_round2B` | active | - | - | 0 | 100% (10) | 1x negligible | - | no evaluable records deposited since Oct 2024. |
| `PROBOSCIVIRUS_POL_Latimer_2010_EEHV6_round2` | active | - | - | 0 | 100% (1) | 64x moderate | - | no evaluable records deposited since Oct 2024. Entry flags: thin_evidence. |
| `Pan_coccidia_SSUrDNA_of_E_furonis_Gen_2011` | active | - | - | 0 | 100% (5) | 1x negligible | - | no evaluable records deposited since Oct 2024. |
| `Snake_fungus_Ophidiomyces_ophi_IGS_Bohuski_2015` | active | - | - | 0 | 100% (11) | 1x negligible | - | no evaluable records deposited since Oct 2024. |
| `Sunshinevirus_RdRp_Hyndman_2012_1` | active | - | - | 0 | 100% (2) | 1x negligible | - | no evaluable records deposited since Oct 2024. Entry flags: orientation_inferred. 3 patent records excluded. |
| `Sunshinevirus_RdRp_Hyndman_2012_2` | active | - | - | 0 | 100% (2) | 1x negligible | - | no evaluable records deposited since Oct 2024. Entry flags: orientation_inferred. 3 patent records excluded. |
| `Tortoise_intranuclear_coccidia_18SrDNA` | active | - | - | 0 | 100% (1) | 1x negligible | - | no evaluable records deposited since Oct 2024. |

## Stable (56)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `USUTU_ssRNA_NS1_realtime_Jost_2011` | active | 90.1% | 87%-93% | 392 | 95% (684) | 1x negligible | - | detected share 90.1% (87%-93%) since Oct 2024. Entry flags: primer_site_polymorphic. 2 patent records excluded. |
| `CMV_UL55_gB_Deckers_2009_round2` | active | 90.6% | 76%-97% | 32 | 94% (542) | 32x moderate | - | detected share 90.6% (76%-97%) since Oct 2024. Entry flags: citation_is_indirect. 762 patent records excluded. |
| `Pan_HERPES_dsDNA_Terminase` | active | 91.5% | 88%-94% | 282 | 89% (2329) | 128x moderate | - | detected share 91.5% (88%-94%) since Oct 2024. Entry flags: orientation_inferred. 1 out-of-scope records excluded. |
| `TILV_ssRNA_segment3_ME1_ME2_Kembou_2017` | active | 92.0% | 75%-98% | 25 | 97% (77) | 1x negligible | - | detected share 92.0% (75%-98%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records). Entry flags: citation_is_indirect, thin_evidence. |
| `CBPV_RNA1_Rossi_2024` | active | 92.3% | 76%-98% | 26 | 87% (124) | 16x moderate | - | detected share 92.3% (76%-98%) since Oct 2024. 3 patent records excluded. |
| `BOCAVIRUS_ssDNA_NS1_gene_round1` | active | 92.9% | 90%-95% | 425 | 64% (1625) | 1024x high | - | detected share 92.9% (90%-95%) since Oct 2024. 13 patent records excluded. |
| `CHLAMYDIA_psittaci_16S_Messmer_1997_round2` | active | 93.8% | 72%-99% | 16 | 98% (146) | 1x negligible | - | detected share 93.8% (72%-99%) since Oct 2024. Entry flags: cross_reactive. |
| `Helicobacter_Pan_Helicobacter_16S_Jim_Fox_1998` | active | 94.1% | 84%-98% | 51 | 89% (484) | 1x negligible | - | detected share 94.1% (84%-98%) since Oct 2024. Entry flags: amplicon_measured_not_published, orientation_inferred. 1 patent records excluded. |
| `POXVIRUSES_dsDNA_Topoisomerase` | active | 94.4% | 94%-95% | 5092 | 97% (9462) | 1x negligible | - | detected share 94.4% (94%-95%) since Oct 2024. 735 patent records excluded. |
| `BOCAVIRUS_ssDNA_NS1_gene_round2` | active | 95.2% | 93%-97% | 415 | 68% (1526) | 2048x high | - | detected share 95.2% (93%-97%) since Oct 2024. 13 patent records excluded. |
| `ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2` | active | 95.8% | 94%-97% | 711 | 90% (2598) | 131072x severe | - | detected share 95.8% (94%-97%) since Oct 2024. Entry flags: nested_protocol. 29 patent records excluded. |
| `ADENOVIRUS_dsDNA_Pan_Polymerase_round2` | active | 96.0% | 95%-97% | 1251 | 97% (3608) | 10616832x severe | - | detected share 96.0% (95%-97%) since Oct 2024. Entry flags: amplicon_multimodal. 159 out-of-scope records excluded. 991 patent records excluded. |
| `CDV_P_gene_Mix7_Halecker_2021` | active | 96.5% | 90%-99% | 86 | 91% (287) | 16x moderate | - | detected share 96.5% (90%-99%) since Oct 2024. 61 patent records excluded. |
| `CDV_H_gene_Mueller_2011_3` | active | 96.8% | 93%-99% | 186 | 96% (1692) | 1x negligible | - | detected share 96.8% (93%-99%) since Oct 2024. Entry flags: pairing_is_curator_reading. 61 patent records excluded. |
| `CMV_UL55_gB_Deckers_2009` | active | 96.9% | 84%-99% | 32 | 84% (595) | 256x high | - | detected share 96.9% (84%-99%) since Oct 2024. Entry flags: citation_is_indirect. 762 patent records excluded. |
| `CMV_UL55_gB_Prepens_2007_round1` | active | 96.9% | 84%-99% | 32 | 91% (643) | 512x high | - | detected share 96.9% (84%-99%) since Oct 2024. Entry flags: amplicon_measured_not_published. 762 patent records excluded. |
| `CMV_UL55_gB_Prepens_2007_round2` | active | 96.9% | 84%-99% | 32 | 97% (664) | 8192x severe | - | detected share 96.9% (84%-99%) since Oct 2024. Entry flags: amplicon_measured_not_published. 762 patent records excluded. |
| `Pan_PARAPOX_dsDNA_RPO147_J6R_generic_TaqMan_Zhao_2013` | draft | 96.9% | 84%-99% | 32 | 95% (86) | 1x negligible | - | detected share 96.9% (84%-99%) since Oct 2024. Entry flags: amplicon_measured_not_published, chemistry_detail_missing, primer_site_polymorphic. 322 out-of-scope records excluded. 53 patent records excluded. |
| `PHLEBOVIRUS_ssRNA_L_segment_round2` | active | 97.2% | 93%-99% | 142 | 85% (320) | 8192x severe | - | detected share 97.2% (93%-99%) since Oct 2024. |
| `Pan_Flavivirus_NS5_gene` | active | 97.3% | 97%-98% | 9398 | 98% (24378) | 768x high | - | detected share 97.3% (97%-98%) since Oct 2024. 1 out-of-scope records excluded. |
| `MONKEYPOX_dsDNA_C3L_CongoBasin_TaqMan_Li_2010` | active | 97.9% | 96%-99% | 609 | 98% (464) | 1x negligible | - | detected share 97.9% (96%-99%) since Oct 2024. Entry flags: amplicon_measured_not_published, scope_narrower_than_taxid. 5 patent records excluded. 2 chance-pair records excluded (drift.chance_pair_test). |
| `PHLEBOVIRUS_ssRNA_L_segment_round1` | active | 98.1% | 90%-100% | 54 | 96% (216) | 256x high | - | detected share 98.1% (90%-100%) since Oct 2024. |
| `LEPTOSPIRA_lipL32_Ahmed_2020` | active | 98.2% | 96%-99% | 442 | 88% (1472) | 32x moderate | - | detected share 98.2% (96%-99%) since Oct 2024. Entry flags: primer_site_polymorphic, scope_narrower_than_taxid. 42 chance-pair records excluded (drift.chance_pair_test). |
| `ADENOVIRUS_dsDNA_Pan_Polymerase_round1` | active | 98.4% | 97%-99% | 1175 | 91% (3783) | 1811939328x severe | - | detected share 98.4% (97%-99%) since Oct 2024. Entry flags: amplicon_multimodal. 159 out-of-scope records excluded. 991 patent records excluded. |
| `POXVIRUSES_dsDNA_Polymerase_short_2` | active | 98.5% | 98%-99% | 5351 | 97% (9708) | 4x negligible | - | detected share 98.5% (98%-99%) since Oct 2024. Entry flags: oligos_from_secondary_source, oligos_modified, pairing_is_curator_reading. 735 patent records excluded. |
| `ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round1` | active | 98.6% | 97%-99% | 694 | 96% (2360) | 32768x severe | - | detected share 98.6% (97%-99%) since Oct 2024. 29 patent records excluded. |
| `RETROVIRUS_RNA_polymerase_SIV` | active | 98.7% | 96%-100% | 226 | 54% (4988) | 4x negligible | - | detected share 98.7% (96%-100%) since Oct 2024. |
| `BORNA_VIRUS_N_gene` | active | 98.8% | 96%-100% | 165 | 98% (150) | 1x negligible | - | detected share 98.8% (96%-100%) since Oct 2023 (window widened to 36 months to reach 15 evaluable records). Entry flags: oligos_not_in_cited_paper, orientation_inferred. 1005 out-of-scope records excluded. 12 patent records excluded. |
| `PARVOVIRUS_ssDNA_VP1_gene_dependovirus_2002` | active | 98.8% | 97%-100% | 256 | 98% (1775) | 6912x severe | - | detected share 98.8% (97%-100%) since Oct 2024. Entry flags: oligos_modified. 6845 patent records excluded. |
| `Helicobacter_Pan_Helicobacter_16S_short_Fox_1998` | active | 99.0% | 95%-100% | 102 | 91% (1049) | 1x negligible | - | detected share 99.0% (95%-100%) since Oct 2024. Entry flags: shares_oligos_with_sibling. 1 patent records excluded. |
| `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene_round2` | active | 99.1% | 99%-99% | 2043 | 98% (11904) | 96x moderate | - | detected share 99.1% (99%-99%) since Oct 2024. 47 patent records excluded. |
| `ENTEROVIRUS_ssRNA_VP3_VP1` | active | 99.1% | 98%-99% | 1222 | 96% (8093) | 64x moderate | - | detected share 99.1% (98%-99%) since Oct 2024. Entry flags: amplicon_disagrees_with_paper. 40 out-of-scope records excluded. |
| `RETROVIRUS_RNA_polymerase_SIV_Characterization_2001` | active | 99.6% | 98%-100% | 226 | 98% (3785) | 576x high | - | detected share 99.6% (98%-100%) since Oct 2024. Entry flags: orientation_inferred. |
| `ALPHAVIRUSES_Togaviridae_ssRNA_NSP4_gene_round1` | active | 99.7% | 99%-100% | 3773 | 95% (4713) | 512x high | - | detected share 99.7% (99%-100%) since Oct 2024. Entry flags: oligos_modified. 339 patent records excluded. |
| `BORNA_VIRUS_N_gene_Zimmermann_1994` | active | 100.0% | 98%-100% | 165 | 98% (147) | 1x negligible | - | detected share 100.0% (98%-100%) since Oct 2023 (window widened to 36 months to reach 15 evaluable records). Entry flags: nested_protocol. 1005 out-of-scope records excluded. 12 patent records excluded. |
| `CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004` | active | 100.0% | 82%-100% | 17 | 87% (163) | 1x negligible | - | detected share 100.0% (82%-100%) since Oct 2024. Entry flags: orientation_inferred. 2 patent records excluded. |
| `CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004` | active | 100.0% | 82%-100% | 17 | 97% (162) | 1x negligible | - | detected share 100.0% (82%-100%) since Oct 2024. Entry flags: amplicon_measured_not_published. 2 patent records excluded. |
| `FILOVIRUS_ssRNA_L_gene_2` | active | 100.0% | 87%-100% | 25 | 99% (3537) | 288x high | - | detected share 100.0% (87%-100%) since Oct 2024. Entry flags: oligos_modified. 85 patent records excluded. |
| `MYCOBACTERIUM_TB_complex_IS6110_Boniotti_2014` | active | 100.0% | 99%-100% | 274 | 100% (3738) | 1x negligible | - | detected share 100.0% (99%-100%) since Oct 2024. 6 patent records excluded. |
| `MYCOPLASMA_gallisepticum_parE_Kang_2023` | active | 100.0% | 88%-100% | 27 | 100% (68) | 1x negligible | - | detected share 100.0% (88%-100%) since Oct 2023 (window widened to 36 months to reach 15 evaluable records). |
| `NOSEMA_ceranae_SSU_Martin-Hernandez_2007` | active | 100.0% | 88%-100% | 28 | 79% (849) | 1x negligible | - | detected share 100.0% (88%-100%) since Oct 2024. Entry flags: oligos_read_from_figure. |
| `Nipah_N_gene` | active | 100.0% | 85%-100% | 21 | 93% (186) | 1x negligible | - | detected share 100.0% (85%-100%) since Oct 2024. 13 patent records excluded. |
| `Nipah_N_gene_2` | active | 100.0% | 86%-100% | 23 | 98% (275) | 1x negligible | - | detected share 100.0% (86%-100%) since Oct 2024. Entry flags: oligos_from_secondary_source, primer_site_polymorphic. 13 patent records excluded. |
| `OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023` | active | 100.0% | 95%-100% | 81 | - | 1x negligible | - | detected share 100.0% (95%-100%) since Oct 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: chemistry_detail_missing, pairing_is_curator_reading, retrieval_scope_incomplete, thin_evidence. 111 chance-pair records excluded (drift.chance_pair_test). |
| `ORF_VIRUS_dsDNA_RPO147_J6R_TaqMan_Zhao_2013` | draft | 100.0% | 88%-100% | 27 | 100% (56) | 1x negligible | - | detected share 100.0% (88%-100%) since Oct 2024. Entry flags: amplicon_measured_not_published, chemistry_detail_missing. 51 patent records excluded. 76 chance-pair records excluded (drift.chance_pair_test). |
| `ORTHOBORNAVIRUS_XP_aquatic_Sigrist_2021` | active | 100.0% | 82%-100% | 18 | 100% (21) | 16x moderate | - | detected share 100.0% (82%-100%) since Oct 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: chemistry_detail_missing, oligos_read_from_figure. 1278 out-of-scope records excluded. |
| `ORTHOBORNAVIRUS_XP_psittacine_Sigrist_2021` | active | 100.0% | 90%-100% | 35 | 97% (59) | 64x moderate | - | detected share 100.0% (90%-100%) since Oct 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_read_from_figure. 721 out-of-scope records excluded. |
| `RETROVIRUS_RNA_polymerase_SIV_2` | active | 100.0% | 98%-100% | 226 | 83% (4495) | 768x high | - | detected share 100.0% (98%-100%) since Oct 2024. Entry flags: orientation_inferred. |
| `RETROVIRUS_RNA_polymerase_SIV_3` | draft | 100.0% | 98%-100% | 226 | 99% (4991) | 27648x severe | - | detected share 100.0% (98%-100%) since Oct 2024. Entry flags: cross_reactive. |
| `Salmonella_invA_Rahn_1992` | active | 100.0% | 93%-100% | 55 | 98% (409) | 1x negligible | - | detected share 100.0% (93%-100%) since Oct 2024. Entry flags: oligos_not_in_cited_paper, orientation_inferred. |
| `Shigella_ipaH_Sethabutr_1993` | active | 100.0% | 91%-100% | 38 | 98% (168) | 1x negligible | - | detected share 100.0% (91%-100%) since Oct 2024. Entry flags: orientation_inferred. |
| `TRICHOMONAS_gallinae_18S_Renteria_Solis_2020` | active | 100.0% | 85%-100% | 21 | 100% (46) | 1x negligible | - | detected share 100.0% (85%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records). |
| `VIBRIO_coralliilyticus_vcpA_ORF_Wilson_2013` | active | 100.0% | 81%-100% | 16 | 89% (19) | 1x negligible | - | detected share 100.0% (81%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_disagrees_with_paper, oligos_from_secondary_source. |
| `VIBRIO_coralliilyticus_vcpA_Wilson_2013` | active | 100.0% | 81%-100% | 16 | 89% (19) | 1x negligible | - | detected share 100.0% (81%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records). |
| `Yersinia_enterocolitica_Ibrahim_1992` | active | 100.0% | 80%-100% | 15 | 100% (22) | 1x negligible | - | detected share 100.0% (80%-100%) since Oct 2023 (window widened to 36 months to reach 15 evaluable records). Entry flags: amplicon_disagrees_with_paper, oligos_not_in_cited_paper, orientation_inferred. |
| `Yersinia_pseudotuberculosis_Wang_1997` | active | 100.0% | 81%-100% | 16 | 100% (49) | 1x negligible | - | detected share 100.0% (81%-100%) since Oct 2022 (window widened to 48 months to reach 15 evaluable records). Entry flags: orientation_inferred. 2 patent records excluded. |

## Not scoreable (20)

These assays were screened, and their records still count in the nested,
degeneracy and per-lineage tables, but their entry carries a review item that
means a status would not be a statement about the assay: either an open question
a human has to answer, or a readout this pipeline cannot model. No status is shown
for them, including the one they would otherwise have had.

| assay | entry | why | note |
|---|---|---|---|
| `BORNA_VIRUS_N_gene_Zimmermann_1994_round2` | draft | `amplicon_size_unresolved` | no product size is declared |
| `CALICIVIRUS_ssRNA_Helicase_Reid_1999` | draft | `oligo_sequence_uncertain` | Hel1 forward terminal base corrected G->C on 2026-10-24 (maintainer decision): C is what all 16 design targets carry and the only form giving the published 357 bp; the two G sources are a 1999 table and an OCR deposit. No clean PDF held, so the copy stays uncertain pending the NYU-proxy scan. OPEN flag, so the entry is draft. Full rationale in notes_curator. |
| `CDV_P_gene_Mix3_Halecker_2021` | draft | `duplicate_entry_unresolved` | overlaps CDV_P_gene_Scagliarini_2007: shares CDV3-R, and the forward and probe are degenerate modifications of it; decide whether both entries stay |
| `CDV_P_gene_panCDV_Geiselhardt_2022` | draft | `target_scope_unresolved` | also detects PDV (Morbillivirus phocae, txid3052347) while the taxid here is CDV only; decide whether a PDV-scoped entry is wanted |
| `FRANCISELLA_tularensis_tul4_Long_1993` | draft | `oligo_sequence_uncertain` | the probe is omitted: the OCR of its sequence was not reliable enough to enter |
| `LEPTOSPIROSIS_Flagillar_filiment_Prote` | draft | `not_validated` |  |
| `LMBV_dsDNA_MCP_RPA_Li_2025` | active | `not_screenable` | the chemistry is RPA; the penalties are calibrated on PCR |
| `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` | draft | `not_validated` |  |
| `MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018` | draft | `citation_unresolved` | oligos come from an uncitable source (anonymous, 2017) |
| `MYCOBACTERIUM_TB_complex_helicase_MTCHeli_Hermes_2018` | draft | `citation_unresolved` | oligos come from an uncitable source (anonymous, 2017) |
| `MYCOBACTERIUM_genus_16S_rRNA_Hermes_2018` | draft | `citation_unresolved` | oligos come from an uncitable source (Nieter, 2016) |
| `ORTHOBUNYAVIRUS_ssRNA_S_segment_Cac_Briese_2007` | draft | `target_scope_unresolved` | the source never states what this assay is meant to cover |
| `ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997` | draft | `not_screenable` | identification is by product size plus an XbaI digest, which the screen cannot model |
|  |  | `oligo_source_unresolved` | a Meyer 1994 origin is suspected but not established |
| `PANPOX_dsDNA_highGC_RNApol_Li_2010` | draft | `retrieval_stale` | the retrieval query changed on 2026-10-17; these numbers predate it |
| `PANPOX_dsDNA_lowGC_IMV_Li_2010` | draft | `retrieval_stale` | the retrieval query changed on 2026-10-17; these numbers predate it |
| `Pan_HERPES_dsDNA_Polymerase` | draft | `duplicate_entry_unresolved` | whether the DFA variant and the PREDICT version are one entry or two is unresolved |
| `Pan_mycoplasma_16S_23S_intergenic_space` | draft | `oligo_source_unresolved` | the partner primer has no attributed source |
| `Pan_mycoplasma_16S_23S_intergenic_space_3` | draft | `oligo_source_unresolved` | the partner primer has no attributed source |
| `Pan_mycoplasma_16S_All_Van_1992` | draft | `do_not_use` |  |
| `SIMBU_SEROGROUP_ssRNA_S_segment_TaqMan_Steyn_2020` | draft | `amplicon_size_unresolved` | published 152 bp against a printed 152-304 span that is 153 bp inclusive; to be measured, not argued |

## Detail for flagged assays

**Duplication check:** 20 of 76 flagged assays still hold when duplicated records are discounted (each distinct binding-site footprint counted once, and the sample size cut to the number of footprints). The note on each assay that did not hold says which test it failed.

### `RETROVIRUS_RNA_polymerase_SIV_Keele_2009`

RETROVIRUS (RNA) — polymerase (SIV)  
Designed 2009, doi:10.1038/nature08200  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1990 | 0 | 1 | 0% |
| 1991 | 0 | 2 | 0% |
| 1992 | 0 | 0 | - |
| 1993 | 0 | 8 | 0% |
| 1994 | 1 | 1 | 100% |
| 1995 | 0 | 1 | 0% |
| 1996 | 1 | 1 | 100% |
| 1997 | 0 | 1 | 0% |
| 1998 | 0 | 1 | 0% |
| 1999 | 1 | 2 | 50% |
| 2001 | 7 | 16 | 44% |
| 2002 | 5 | 9 | 56% |
| 2003 | 3 | 7 | 43% |
| 2004 | 0 | 29 | 0% |
| 2005 | 0 | 4 | 0% |
| 2006 | 1 | 11 | 9% |
| 2007 | 5 | 6 | 83% |
| 2008 | 1 | 7 | 14% |
| 2009 | 5 | 46 | 11% |
| 2010 | 3 | 22 | 14% |
| 2011 | 6 | 7 | 86% |
| 2012 | 2 | 6 | 33% |
| 2013 | 0 | 660 | 0% |
| 2014 | 13 | 54 | 24% |
| 2015 | 3 | 6 | 50% |
| 2016 | 0 | 93 | 0% |
| 2017 | 170 | 172 | 99% |
| 2018 | 1 | 1 | 100% |
| 2019 | 1 | 383 | 0.3% |
| 2020 | 0 | 113 | 0% |
| 2021 | 1 | 99 | 1% |
| 2022 | 1 | 3 | 33% |
| 2023 | 0 | 3 | 0% |
| 2024 | 0 | 1848 | 0% |
| 2025 | 0 | 204 | 0% |
| 2026 | 0 | 20 | 0% |

*trend over deposit year: falling, z = -14.42, two-sided p = 3.83e-47 across 35 years and 3847 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 224 recent records share 2 distinct footprints (112.0 per footprint), of which 223 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 2 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 2 and 74 independent observations the fall from baseline is -14% to +59%, which no longer excludes zero.

**Denominator:** 3847 of 8252 screened records are evaluable (46.6%); 4405 are not. Every share above is taken over the evaluable ones.

Excluded: 4405 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3467 no_site, 683 chance_anchor, 251 truncated, 4 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 3513 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2948 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 519 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ABPV_capsid_Rossi_2024`

ACUTE BEE PARALYSIS VIRUS — capsid gene RT-qPCR, MGB probe (Rossi 2024)  
Designed 2024, doi:10.3390/microorganisms12061105  
**Degeneracy:** 4608-fold degenerate (288-fold primers x 16-fold probe); ~12 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1999 | 0 | 1 | 0% |
| 2000 | 2 | 2 | 100% |
| 2001 | 8 | 10 | 80% |
| 2002 | 20 | 21 | 95% |
| 2003 | 3 | 3 | 100% |
| 2004 | 0 | 0 | - |
| 2006 | 0 | 0 | - |
| 2007 | 0 | 0 | - |
| 2008 | 3 | 3 | 100% |
| 2009 | 2 | 2 | 100% |
| 2010 | 2 | 2 | 100% |
| 2011 | 17 | 17 | 100% |
| 2013 | 0 | 0 | - |
| 2014 | 1 | 1 | 100% |
| 2015 | 0 | 3 | 0% |
| 2016 | 0 | 0 | - |
| 2017 | 1 | 1 | 100% |
| 2018 | 1 | 1 | 100% |
| 2019 | 1 | 2 | 50% |
| 2020 | 0 | 0 | - |
| 2021 | 16 | 18 | 89% |
| 2022 | 5 | 11 | 45% |
| 2023 | 5 | 6 | 83% |
| 2024 | 0 | 2 | 0% |
| 2025 | 1 | 11 | 9% |
| 2026 | 0 | 7 | 0% |

*trend over deposit year: falling, z = -5.30, two-sided p = 1.13e-07 across 20 years and 124 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 8 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 18 recent records share 8 distinct footprints (2.2 per footprint), of which 1 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 8 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 124 of 982 screened records are evaluable (12.6%); 858 are not. Every share above is taken over the evaluable ones.

Excluded: 858 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 850 no_site, 8 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 2 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 850 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003`

Influenza A virus — matrix gene real-time RT-PCR (Spackman, modified)  
Designed 2002, doi:10.1128/JCM.40.9.3256-3260.2002  
**Degeneracy:** 32-fold degenerate (32-fold primers x 1-fold probe); ~5 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 1 | 1 | 100% |
| 1987 | 1 | 2 | 50% |
| 1988 | 1 | 2 | 50% |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 1 | 0% |
| 1992 | 0 | 1 | 0% |
| 1993 | 1 | 1 | 100% |
| 1994 | 0 | 2 | 0% |
| 1997 | 4 | 4 | 100% |
| 1998 | 1 | 1 | 100% |
| 1999 | 2 | 5 | 40% |
| 2000 | 5 | 7 | 71% |
| 2001 | 8 | 42 | 19% |
| 2002 | 13 | 14 | 93% |
| 2003 | 42 | 45 | 93% |
| 2004 | 53 | 55 | 96% |
| 2005 | 83 | 648 | 13% |
| 2006 | 618 | 1357 | 46% |
| 2007 | 316 | 777 | 41% |
| 2008 | 398 | 626 | 64% |
| 2009 | 738 | 1772 | 42% |
| 2010 | 667 | 2192 | 30% |
| 2011 | 158 | 306 | 52% |
| 2012 | 126 | 537 | 23% |
| 2013 | 261 | 849 | 31% |
| 2014 | 351 | 1216 | 29% |
| 2015 | 444 | 872 | 51% |
| 2016 | 769 | 4246 | 18% |
| 2017 | 1197 | 2055 | 58% |
| 2018 | 1566 | 5180 | 30% |
| 2019 | 917 | 7429 | 12% |
| 2020 | 1561 | 5221 | 30% |
| 2021 | 904 | 2050 | 44% |
| 2022 | 449 | 5435 | 8% |
| 2023 | 316 | 8063 | 4% |
| 2024 | 770 | 10126 | 8% |
| 2025 | 1267 | 16674 | 8% |
| 2026 | 494 | 12477 | 4% |

*trend over deposit year: falling, z = -91.54, two-sided p = 0 across 37 years and 90291 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 30382 recent records share 156 distinct footprints (194.8 per footprint), of which 33 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 156 independent observations (one per footprint) the interval around the 6% detected share is 4%-11%, and counting each footprint once, 17 of 156 footprints amplify (11%; interval 7%-17%); each is below the 90% threshold, and the fall from baseline (-18% to -9%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 90291 of 184766 screened records are evaluable (48.9%); 94475 are not. Every share above is taken over the evaluable ones.

Excluded: 7 indeterminate, 94468 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 93194 truncated, 1169 no_site, 102 chance_anchor, 3 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 667 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1169 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Pan_Plasmodium_sp_and_Haemopro_cytochrome_c`

Pan-Plasmodium sp. and Haemoproteus sp. — cytochrome c  
Designed 2004, doi:10.1645/GE-184R1  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1998 | 3 | 3 | 100% |
| 2000 | 0 | 0 | - |
| 2002 | 6 | 36 | 17% |
| 2003 | 0 | 0 | - |
| 2004 | 3 | 5 | 60% |
| 2005 | 1 | 63 | 2% |
| 2006 | 4 | 26 | 15% |
| 2007 | 0 | 22 | 0% |
| 2008 | 0 | 60 | 0% |
| 2009 | 2 | 38 | 5% |
| 2010 | 16 | 85 | 19% |
| 2011 | 9 | 83 | 11% |
| 2012 | 1 | 29 | 3% |
| 2013 | 7 | 17 | 41% |
| 2014 | 1 | 218 | 0.5% |
| 2015 | 8 | 57 | 14% |
| 2016 | 9 | 39 | 23% |
| 2017 | 51 | 208 | 25% |
| 2018 | 24 | 64 | 38% |
| 2019 | 3 | 37 | 8% |
| 2020 | 5 | 262 | 2% |
| 2021 | 1 | 14 | 7% |
| 2022 | 73 | 81 | 90% |
| 2023 | 16 | 103 | 16% |
| 2024 | 26 | 78 | 33% |
| 2025 | 8 | 76 | 11% |
| 2026 | 4 | 69 | 6% |

*trend over deposit year: rising, z = +5.21, two-sided p = 1.93e-07 across 25 years and 1773 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 20251 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Hepatocystis sp. SSJ-2010 (903504) | 125 | 125 | 100% |
| Hepatocystis sp. TLG-2012 (1266736) | 74 | 74 | 100% |
| Plasmodium billcollinsi (720590) | 42 | 42 | 100% |
| Plasmodium tupinambi (3448513) | 29 | 29 | 100% |
| Plasmodiidae sp. (2605378) | 22 | 22 | 100% |
| Plasmodium brasilianum (5824) | 12 | 12 | 100% |
| taxid 31271 | 10 | 10 | 100% |
| taxid 138297 | 10 | 10 | 100% |
| taxid 5826 | 6 | 6 | 100% |
| Nycteria sp. JS-2015 (1649013) | 6 | 6 | 100% |
| _+3163 more taxa_ | | | |


**Duplication check:** 148 recent records share 23 distinct footprints (6.4 per footprint), of which 40 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 23 and 304 independent observations the fall from baseline is -16% to +11%, which no longer excludes zero.

**Denominator:** 1773 of 11788 screened records are evaluable (15.0%); 10015 are not. Every share above is taken over the evaluable ones.

Excluded: 10015 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 8993 no_site, 1002 truncated, 20 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 981 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 5 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 8988 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010`

ORTHOREOVIRUS (dsRNA) — RNA polymerase  
Designed 2010, doi:10.1177/104063871002200106  
**Degeneracy:** 147456-fold degenerate (147456-fold primers x 1-fold probe); ~17 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 0 | - |
| 1987 | 0 | 0 | - |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 1 | 1 | 100% |
| 1994 | 2 | 2 | 100% |
| 1995 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 1 | 1 | 100% |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 0 | 0 | - |
| 2005 | 1 | 1 | 100% |
| 2006 | 2 | 2 | 100% |
| 2007 | 1 | 1 | 100% |
| 2008 | 0 | 0 | - |
| 2009 | 3 | 6 | 50% |
| 2010 | 5 | 7 | 71% |
| 2011 | 3 | 10 | 30% |
| 2012 | 27 | 29 | 93% |
| 2013 | 6 | 15 | 40% |
| 2014 | 11 | 33 | 33% |
| 2015 | 18 | 32 | 56% |
| 2016 | 10 | 24 | 42% |
| 2017 | 13 | 18 | 72% |
| 2018 | 11 | 33 | 33% |
| 2019 | 12 | 32 | 38% |
| 2020 | 27 | 152 | 18% |
| 2021 | 43 | 60 | 72% |
| 2022 | 32 | 46 | 70% |
| 2023 | 36 | 72 | 50% |
| 2024 | 70 | 99 | 71% |
| 2025 | 27 | 322 | 8% |
| 2026 | 14 | 34 | 41% |

*trend over deposit year: falling, z = -7.66, two-sided p = 1.79e-14 across 24 years and 1032 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 52 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 361 recent records share 26 distinct footprints (13.9 per footprint). Both reductions leave the flag in place: with only 26 independent observations (one per footprint) the interval around the 12% detected share is 4%-30%, and counting each footprint once, 11 of 26 footprints amplify (42%; interval 26%-61%); each is below the 90% threshold, and the fall from baseline (-51% to -17%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 1032 of 14479 screened records are evaluable (7.1%); 13447 are not. Every share above is taken over the evaluable ones.

Excluded: 13447 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 13154 no_site, 219 chance_anchor, 74 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 3 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 205 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 12949 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004`

**Lineage override:** pooled status was low coverage.  
MONKEYPOX virus (dsDNA) — N3R MGB TaqMan (Kulesh 2004)  
Designed 2004, doi:10.1038/labinvest.3700143  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 2 | 2 | 100% |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 2 | 3 | 67% |
| 2005 | 7 | 7 | 100% |
| 2007 | 0 | 0 | - |
| 2008 | 0 | 0 | - |
| 2009 | 0 | 0 | - |
| 2010 | 1 | 5 | 20% |
| 2011 | 2 | 2 | 100% |
| 2012 | 0 | 0 | - |
| 2013 | 1 | 2 | 50% |
| 2014 | 24 | 24 | 100% |
| 2015 | 10 | 11 | 91% |
| 2018 | 0 | 1 | 0% |
| 2019 | 0 | 8 | 0% |
| 2020 | 24 | 35 | 69% |
| 2022 | 2 | 3365 | 0.1% |
| 2023 | 2 | 2954 | 0.1% |
| 2024 | 483 | 2045 | 24% |
| 2025 | 276 | 1742 | 16% |
| 2026 | 338 | 2162 | 16% |

*trend over deposit year: rising, z = +12.24, two-sided p = 1.8e-34 across 16 years and 12368 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 5 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 4113 recent records share 6 distinct footprints (685.5 per footprint), of which 1704 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 6 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 6 and 12 independent observations the fall from baseline is -21% to +48%, which no longer excludes zero.

**Denominator:** 12368 of 13752 screened records are evaluable (89.9%); 1384 are not. Every share above is taken over the evaluable ones.

Excluded: 13 indeterminate, 1371 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 734 no_site, 616 no_pair, 21 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 2377 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 733 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `RHABDOVIRUS_ssRNA_L_gene_round1`

**Lineage override:** pooled status was low coverage.  
RHABDOVIRUS (ssRNA) — L (pan-rhabdovirus, PREDICT P-016 round 1)  
Designed 2005, doi:10.1099/vir.0.81128-0  
**Degeneracy:** 221184-fold degenerate (221184-fold primers x 1-fold probe); ~18 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 1 | 1 | 100% |
| 1986 | 1 | 1 | 100% |
| 1988 | 0 | 0 | - |
| 1989 | 1 | 1 | 100% |
| 1990 | 2 | 2 | 100% |
| 1993 | 2 | 3 | 67% |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 5 | 0% |
| 1997 | 2 | 6 | 33% |
| 1999 | 0 | 10 | 0% |
| 2000 | 3 | 4 | 75% |
| 2001 | 0 | 1 | 0% |
| 2002 | 5 | 7 | 71% |
| 2003 | 0 | 2 | 0% |
| 2004 | 0 | 3 | 0% |
| 2005 | 1 | 8 | 12% |
| 2006 | 0 | 3 | 0% |
| 2007 | 19 | 27 | 70% |
| 2008 | 23 | 42 | 55% |
| 2009 | 10 | 27 | 37% |
| 2010 | 15 | 31 | 48% |
| 2011 | 6 | 22 | 27% |
| 2012 | 54 | 218 | 25% |
| 2013 | 29 | 59 | 49% |
| 2014 | 43 | 98 | 44% |
| 2015 | 195 | 317 | 62% |
| 2016 | 64 | 388 | 16% |
| 2017 | 49 | 569 | 9% |
| 2018 | 57 | 295 | 19% |
| 2019 | 33 | 692 | 5% |
| 2020 | 79 | 494 | 16% |
| 2021 | 67 | 247 | 27% |
| 2022 | 98 | 452 | 22% |
| 2023 | 128 | 960 | 13% |
| 2024 | 84 | 992 | 8% |
| 2025 | 116 | 455 | 25% |
| 2026 | 65 | 308 | 21% |

*trend over deposit year: falling, z = -12.61, two-sided p = 1.85e-36 across 35 years and 6750 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 769 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| taxid 11307 | 4 | 4 | 100% |
| Betanucleorhabdovirus taraxi (3427245) | 2 | 2 | 100% |
| Betanucleorhabdovirus picridis (3427244) | 2 | 2 | 100% |
| taxid 2563012 | 2 | 2 | 100% |
| Artemisia betanucleorhabdovirus 2 (3478605) | 1 | 1 | 100% |
| Hogweed alphacytorhabdovirus 1 (3478598) | 1 | 1 | 100% |
| Alphaplatrhavirus dendriticum (3426245) | 1 | 1 | 100% |
| Betanucleorhabdovirus sp. 'kurdistanfragariae' (3449943) | 1 | 1 | 100% |
| Beet leaf curl betanucleorhabdovirus (3118959) | 1 | 1 | 100% |
| taxid 3064197 | 1 | 1 | 100% |
| _+192 more taxa_ | | | |


**Duplication check:** 1295 recent records share 181 distinct footprints (7.2 per footprint), of which 36 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 181 and 525 independent observations the fall from baseline is -7% to +6%, which no longer excludes zero.

**Denominator:** 6750 of 9126 screened records are evaluable (74.0%); 2376 are not. Every share above is taken over the evaluable ones.

Excluded: 9 indeterminate, 2367 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 2101 no_site, 170 truncated, 95 chance_anchor, 1 chance_only. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 128 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 138 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1963 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ENTEROVIRUS_ssRNA_VP3_VP1_round2`

**Lineage override:** pooled status was low coverage.  
ENTEROVIRUS (ssRNA) — VP3/VP1  
Designed 2006, doi:10.1128/JCM.00542-06  
**Degeneracy:** 16384-fold degenerate (16384-fold primers x 1-fold probe); ~14 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 3 | 3 | 100% |
| 1983 | 0 | 2 | 0% |
| 1985 | 0 | 1 | 0% |
| 1987 | 0 | 2 | 0% |
| 1988 | 2 | 2 | 100% |
| 1989 | 1 | 2 | 50% |
| 1990 | 0 | 1 | 0% |
| 1992 | 2 | 3 | 67% |
| 1993 | 3 | 19 | 16% |
| 1994 | 3 | 17 | 18% |
| 1995 | 1 | 3 | 33% |
| 1996 | 1 | 1 | 100% |
| 1997 | 6 | 51 | 12% |
| 1998 | 30 | 42 | 71% |
| 1999 | 37 | 343 | 11% |
| 2000 | 8 | 78 | 10% |
| 2001 | 26 | 258 | 10% |
| 2002 | 45 | 194 | 23% |
| 2003 | 47 | 444 | 11% |
| 2004 | 23 | 111 | 21% |
| 2005 | 73 | 294 | 25% |
| 2006 | 39 | 252 | 15% |
| 2007 | 35 | 337 | 10% |
| 2008 | 70 | 443 | 16% |
| 2009 | 116 | 751 | 15% |
| 2010 | 76 | 833 | 9% |
| 2011 | 66 | 1233 | 5% |
| 2012 | 278 | 1952 | 14% |
| 2013 | 326 | 2137 | 15% |
| 2014 | 213 | 2934 | 7% |
| 2015 | 310 | 2530 | 12% |
| 2016 | 137 | 1789 | 8% |
| 2017 | 86 | 2477 | 3% |
| 2018 | 154 | 3027 | 5% |
| 2019 | 700 | 2462 | 28% |
| 2020 | 289 | 1997 | 14% |
| 2021 | 76 | 2701 | 3% |
| 2022 | 164 | 1873 | 9% |
| 2023 | 679 | 2674 | 25% |
| 2024 | 411 | 1931 | 21% |
| 2025 | 407 | 2337 | 17% |
| 2026 | 369 | 1923 | 19% |

*trend over deposit year: rising, z = +9.66, two-sided p = 4.44e-22 across 42 years and 40464 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 40 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Enterovirus PV1 (3569731) | 1 | 1 | 100% |
| Enterovirus E11 (3569727) | 13 | 14 | 93% |
| Enterovirus E9 (3569730) | 1 | 2 | 50% |
| Enterovirus E13 (3569728) | 0 | 16 | 0% |
| Enterovirus E6 (3569729) | 0 | 7 | 0% |


**Duplication check:** 4533 recent records share 307 distinct footprints (14.8 per footprint), of which 1425 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 307 and 2141 independent observations the fall from baseline is +2% to +11%, which no longer excludes zero.

**Denominator:** 40464 of 73230 screened records are evaluable (55.3%); 32766 are not. Every share above is taken over the evaluable ones.

Excluded: 32766 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 25012 no_site, 5387 truncated, 2346 chance_anchor, 21 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 16342 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 307 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 24705 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Leucocytozoon_cyt_c_Hellgren_2004`

**Lineage override:** pooled status was low coverage.  
For Leucocytozoon spp. (X-reacts weakly with haemoproteus) — cytochrome c  
Designed 2004, doi:10.1645/GE-184R1  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 2002 | 2 | 2 | 100% |
| 2004 | 0 | 0 | - |
| 2005 | 0 | 39 | 0% |
| 2006 | 1 | 1 | 100% |
| 2007 | 0 | 3 | 0% |
| 2008 | 29 | 35 | 83% |
| 2009 | 4 | 4 | 100% |
| 2010 | 0 | 9 | 0% |
| 2011 | 0 | 1 | 0% |
| 2012 | 0 | 0 | - |
| 2013 | 3 | 32 | 9% |
| 2014 | 2 | 152 | 1% |
| 2015 | 3 | 17 | 18% |
| 2016 | 4 | 4 | 100% |
| 2017 | 12 | 33 | 36% |
| 2018 | 18 | 24 | 75% |
| 2019 | 0 | 698 | 0% |
| 2020 | 61 | 67 | 91% |
| 2021 | 0 | 69 | 0% |
| 2022 | 3 | 34 | 9% |
| 2023 | 16 | 31 | 52% |
| 2024 | 45 | 55 | 82% |
| 2025 | 20 | 76 | 26% |
| 2026 | 8 | 35 | 23% |

*trend over deposit year: rising, z = +2.93, two-sided p = 0.00343 across 22 years and 1421 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 112 recent records share 23 distinct footprints (4.9 per footprint), of which 24 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 23 and 106 independent observations the fall from baseline is -5% to +32%, which no longer excludes zero.

**Denominator:** 1421 of 7904 screened records are evaluable (18.0%); 6483 are not. Every share above is taken over the evaluable ones.

Excluded: 6483 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 6293 no_site, 177 truncated, 13 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 1081 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 42 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 6251 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Pan_flavivirus_NS5_3_round2`

**Lineage override:** pooled status was low coverage.  
Pan-flavivirus — NS5-3  
Designed 2001, doi:10.1128/JCM.39.5.1922-1927.2001  
**Degeneracy:** 648-fold degenerate (648-fold primers x 1-fold probe); each member is ~1.5e-03 of the reaction, ~9 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1986 | 0 | 2 | 0% |
| 1987 | 0 | 0 | - |
| 1988 | 1 | 2 | 50% |
| 1989 | 1 | 1 | 100% |
| 1990 | 0 | 1 | 0% |
| 1991 | 1 | 1 | 100% |
| 1992 | 0 | 5 | 0% |
| 1993 | 8 | 12 | 67% |
| 1994 | 1 | 1 | 100% |
| 1995 | 2 | 11 | 18% |
| 1996 | 1 | 2 | 50% |
| 1997 | 22 | 70 | 31% |
| 1998 | 3 | 22 | 14% |
| 1999 | 9 | 24 | 38% |
| 2000 | 11 | 33 | 33% |
| 2001 | 9 | 31 | 29% |
| 2002 | 13 | 32 | 41% |
| 2003 | 23 | 37 | 62% |
| 2004 | 78 | 99 | 79% |
| 2005 | 186 | 240 | 78% |
| 2006 | 80 | 120 | 67% |
| 2007 | 118 | 218 | 54% |
| 2008 | 133 | 1015 | 13% |
| 2009 | 332 | 1331 | 25% |
| 2010 | 287 | 425 | 68% |
| 2011 | 420 | 624 | 67% |
| 2012 | 107 | 328 | 33% |
| 2013 | 158 | 306 | 52% |
| 2014 | 505 | 823 | 61% |
| 2015 | 362 | 571 | 63% |
| 2016 | 668 | 1054 | 63% |
| 2017 | 423 | 1463 | 29% |
| 2018 | 311 | 1118 | 28% |
| 2019 | 182 | 717 | 25% |
| 2020 | 371 | 1836 | 20% |
| 2021 | 979 | 3363 | 29% |
| 2022 | 343 | 1550 | 22% |
| 2023 | 1036 | 3864 | 27% |
| 2024 | 1520 | 3992 | 38% |
| 2025 | 1432 | 3220 | 44% |
| 2026 | 685 | 5538 | 12% |

*trend over deposit year: falling, z = -24.48, two-sided p = 2.45e-132 across 40 years and 34102 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 1 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Balclutha incisa flavivirus 1 (3140651) | 0 | 1 | 0% |


**Duplication check:** 9443 recent records share 141 distinct footprints (67.0 per footprint), of which 244 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 141 and 316 independent observations the fall from baseline is -16% to +2%, which no longer excludes zero.

**Denominator:** 34102 of 61178 screened records are evaluable (55.7%); 27076 are not. Every share above is taken over the evaluable ones.

Excluded: 16 indeterminate, 27060 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 25495 no_site, 1406 truncated, 159 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 494 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 14281 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 11214 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Pan_flavivirus_NS5_3_round1`

**Lineage override:** pooled status was low coverage.  
Pan-flavivirus — NS5-3  
Designed 2001, doi:10.1128/JCM.39.5.1922-1927.2001  
**Degeneracy:** 16-fold degenerate (16-fold primers x 1-fold probe); ~4 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1986 | 2 | 2 | 100% |
| 1987 | 0 | 0 | - |
| 1988 | 1 | 2 | 50% |
| 1989 | 1 | 1 | 100% |
| 1990 | 1 | 1 | 100% |
| 1991 | 1 | 1 | 100% |
| 1992 | 0 | 5 | 0% |
| 1993 | 8 | 12 | 67% |
| 1994 | 1 | 1 | 100% |
| 1995 | 6 | 11 | 55% |
| 1996 | 1 | 2 | 50% |
| 1997 | 8 | 12 | 67% |
| 1998 | 13 | 22 | 59% |
| 1999 | 11 | 24 | 46% |
| 2000 | 15 | 34 | 44% |
| 2001 | 11 | 31 | 35% |
| 2002 | 18 | 33 | 55% |
| 2003 | 19 | 32 | 59% |
| 2004 | 86 | 99 | 87% |
| 2005 | 189 | 240 | 79% |
| 2006 | 83 | 120 | 69% |
| 2007 | 112 | 211 | 53% |
| 2008 | 179 | 1016 | 18% |
| 2009 | 360 | 1333 | 27% |
| 2010 | 297 | 417 | 71% |
| 2011 | 468 | 614 | 76% |
| 2012 | 138 | 333 | 41% |
| 2013 | 160 | 320 | 50% |
| 2014 | 522 | 815 | 64% |
| 2015 | 336 | 568 | 59% |
| 2016 | 816 | 1052 | 78% |
| 2017 | 735 | 1460 | 50% |
| 2018 | 537 | 1122 | 48% |
| 2019 | 255 | 709 | 36% |
| 2020 | 627 | 1840 | 34% |
| 2021 | 1343 | 3378 | 40% |
| 2022 | 518 | 1549 | 33% |
| 2023 | 1458 | 3904 | 37% |
| 2024 | 2087 | 4006 | 52% |
| 2025 | 1655 | 3226 | 51% |
| 2026 | 1265 | 5578 | 23% |

*trend over deposit year: falling, z = -17.32, two-sided p = 3.37e-67 across 40 years and 34136 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 1 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Balclutha incisa flavivirus 1 (3140651) | 0 | 1 | 0% |


**Duplication check:** 9489 recent records share 192 distinct footprints (49.4 per footprint), of which 315 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 192 independent observations (one per footprint) the interval around the 35% detected share is 29%-42%, and counting each footprint once, 66 of 192 footprints amplify (34%; interval 28%-41%); each is below the 90% threshold, and the fall from baseline (-17% to -0.7%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 34136 of 61178 screened records are evaluable (55.8%); 27042 are not. Every share above is taken over the evaluable ones.

Excluded: 12 indeterminate, 27030 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 25750 no_site, 1242 truncated, 38 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 640 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1716 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 24034 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `DWVB_polyprotein_Rossi_2024`

DEFORMED WING VIRUS B — polyprotein gene RT-qPCR, MGB probe (Rossi 2024)  
Designed 2024, doi:10.3390/microorganisms12061105  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 2020 | 0 | 0 | - |
| 2022 | 0 | 0 | - |
| 2023 | 37 | 41 | 90% |
| 2024 | 0 | 0 | - |
| 2025 | 3 | 10 | 30% |
| 2026 | 3 | 6 | 50% |

*trend over deposit year: falling, z = -3.83, two-sided p = 0.000127 across 3 years and 57 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 16 recent records share 8 distinct footprints (2.0 per footprint). This flag does not hold up: only 8 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 57 of 737 screened records are evaluable (7.7%); 680 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 679 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 670 no_site, 9 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 670 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme`

**Lineage override:** pooled status was low coverage.  
CORONAVIRUS (ssRNA) — RNA-dependent RNA polymerase  
Designed ?, doi:10.3201/eid1608.100208  
**Degeneracy:** 384-fold degenerate (384-fold primers x 1-fold probe); each member is ~2.6e-03 of the reaction, ~9 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 1 | 2 | 50% |
| 1997 | 2 | 2 | 100% |
| 1998 | 0 | 0 | - |
| 1999 | 1 | 1 | 100% |
| 2000 | 5 | 5 | 100% |
| 2001 | 5 | 7 | 71% |
| 2002 | 1 | 1 | 100% |
| 2003 | 1 | 61 | 2% |
| 2004 | 5 | 76 | 7% |
| 2005 | 5 | 32 | 16% |
| 2006 | 53 | 73 | 73% |
| 2007 | 25 | 38 | 66% |
| 2008 | 14 | 28 | 50% |
| 2009 | 50 | 111 | 45% |
| 2010 | 21 | 48 | 44% |
| 2011 | 13 | 86 | 15% |
| 2012 | 38 | 100 | 38% |
| 2013 | 97 | 209 | 46% |
| 2014 | 121 | 333 | 36% |
| 2015 | 298 | 477 | 62% |
| 2016 | 96 | 287 | 33% |
| 2017 | 361 | 656 | 55% |
| 2018 | 202 | 431 | 47% |
| 2019 | 131 | 313 | 42% |
| 2020 | 277 | 459 | 60% |
| 2021 | 187 | 457 | 41% |
| 2022 | 202 | 499 | 40% |
| 2023 | 528 | 1139 | 46% |
| 2024 | 256 | 468 | 55% |
| 2025 | 286 | 970 | 29% |
| 2026 | 296 | 624 | 47% |

*trend over deposit year: falling, z = -0.13, two-sided p = 0.897 across 30 years and 7993 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 1743 recent records share 126 distinct footprints (13.8 per footprint), of which 19 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 126 and 302 independent observations the fall from baseline is -18% to +3%, which no longer excludes zero.

**Denominator:** 7993 of 25559 screened records are evaluable (31.3%); 17566 are not. Every share above is taken over the evaluable ones.

Excluded: 2 indeterminate, 17564 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 14531 no_site, 2750 truncated, 283 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 69 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 51 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 14480 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CIRCOVIRUSES_ssDNA_vertebrate_Rep_Gene_Mankertz_2000_round1`

CIRCOVIRUSES- (ssDNA) (vertebrate circoviruses) — Rep Gene  
Designed 2000, doi:10.1007/s007050070002  
**Degeneracy:** 1536-fold degenerate (1536-fold primers x 1-fold probe); each member is ~6.5e-04 of the reaction, ~11 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1996 | 1 | 1 | 100% |
| 1997 | 2 | 2 | 100% |
| 1998 | 12 | 15 | 80% |
| 1999 | 9 | 11 | 82% |
| 2000 | 30 | 33 | 91% |
| 2001 | 23 | 28 | 82% |
| 2002 | 31 | 42 | 74% |
| 2003 | 57 | 65 | 88% |
| 2004 | 60 | 70 | 86% |
| 2005 | 53 | 67 | 79% |
| 2006 | 51 | 68 | 75% |
| 2007 | 142 | 166 | 86% |
| 2008 | 132 | 146 | 90% |
| 2009 | 176 | 184 | 96% |
| 2010 | 123 | 131 | 94% |
| 2011 | 215 | 232 | 93% |
| 2012 | 132 | 157 | 84% |
| 2013 | 183 | 217 | 84% |
| 2014 | 252 | 324 | 78% |
| 2015 | 272 | 372 | 73% |
| 2016 | 326 | 406 | 80% |
| 2017 | 255 | 476 | 54% |
| 2018 | 278 | 575 | 48% |
| 2019 | 370 | 786 | 47% |
| 2020 | 152 | 419 | 36% |
| 2021 | 317 | 825 | 38% |
| 2022 | 417 | 732 | 57% |
| 2023 | 525 | 1177 | 45% |
| 2024 | 305 | 993 | 31% |
| 2025 | 149 | 353 | 42% |
| 2026 | 108 | 308 | 35% |

*trend over deposit year: falling, z = -33.28, two-sided p = 7.37e-243 across 31 years and 9381 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 222 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 679 recent records share 71 distinct footprints (9.6 per footprint), of which 268 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 71 independent observations (one per footprint) the interval around the 39% detected share is 28%-50%, and counting each footprint once, 7 of 71 footprints amplify (10%; interval 5%-19%); each is below the 90% threshold, and the fall from baseline (-29% to -5%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 9381 of 24095 screened records are evaluable (38.9%); 14714 are not. Every share above is taken over the evaluable ones.

Excluded: 6 indeterminate, 14708 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 13539 no_site, 940 truncated, 135 chance_anchor, 94 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 2997 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 13539 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Pan_mycoplasma_16S_23S_intergenic_space_Rebelo_2011`

Pan-mycoplasma — 16S-23S intergenic spacer region  
Designed 2011, doi:10.1177/1040638711416846  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1983 | 0 | 0 | - |
| 1985 | 0 | 0 | - |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 0 | - |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 0 | 0 | - |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 0 | 0 | - |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 11 | 19 | 58% |
| 2005 | 3 | 6 | 50% |
| 2006 | 22 | 22 | 100% |
| 2007 | 1 | 2 | 50% |
| 2008 | 7 | 8 | 88% |
| 2009 | 3 | 5 | 60% |
| 2010 | 10 | 13 | 77% |
| 2011 | 0 | 4 | 0% |
| 2012 | 2 | 4 | 50% |
| 2013 | 0 | 4 | 0% |
| 2014 | 11 | 25 | 44% |
| 2015 | 28 | 46 | 61% |
| 2016 | 0 | 13 | 0% |
| 2017 | 3 | 5 | 60% |
| 2018 | 23 | 33 | 70% |
| 2019 | 34 | 91 | 37% |
| 2020 | 16 | 50 | 32% |
| 2021 | 24 | 43 | 56% |
| 2022 | 21 | 46 | 46% |
| 2023 | 9 | 43 | 21% |
| 2024 | 41 | 43 | 95% |
| 2025 | 32 | 106 | 30% |
| 2026 | 20 | 30 | 67% |

*trend over deposit year: falling, z = -3.52, two-sided p = 0.000432 across 23 years and 661 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Per species** (product size names the species here, 354-767 bp, so the share above pools readouts that mean different things; Oct 2024 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Mycoplasma tracheobuteonis (3568880) | - | 8 | 8 | 100% |
| Mycoplasma sp. (2108) | - | 4 | 5 | 80% |
| Mycoplasma milvi (3398775) | - | 3 | 3 | 100% |
| Mycoplasma paraquilae (3398773) | - | 3 | 3 | 100% |
| Mycoplasma razini (3398776) | - | 3 | 3 | 100% |
| Mycoplasma aquilae (1312741) | - | 2 | 2 | 100% |
| Mycoplasma corogypsi (2106) | - | 2 | 2 | 100% |
| Mycoplasma crocodyli (50052) | - | 2 | 2 | 100% |
| Mycoplasma hafezii (525886) | - | 2 | 2 | 100% |
| Mycoplasma haliaeeti (3398774) | - | 2 | 2 | 100% |
| Mycoplasma marinum (1937190) | - | 2 | 2 | 100% |
| Mycoplasma sp. 125 (3447505) | - | 2 | 2 | 100% |
| Mycoplasma sp. 1579d (3699021) | - | 2 | 2 | 100% |
| Mycoplasma sp. 332 (3458236) | - | 2 | 2 | 100% |
| Mycoplasma sp. 3341 (3447506) | - | 2 | 2 | 100% |
| Mycoplasma sp. 3686h (3699019) | - | 0 | 2 | 0% |
| Mycoplasma sp. 480 (3440155) | - | 2 | 2 | 100% |
| Mycoplasma todarodis (1937191) | - | 2 | 2 | 100% |
| Mycoplasma amphoriforme (273136) | - | 0 | 1 | 0% |
| Mycoplasma pogonae (3472838) | - | 1 | 1 | 100% |
| Mycoplasma sp. 10961 (3458677) | - | 1 | 1 | 100% |
| Mycoplasma sp. 11548 (3458678) | - | 1 | 1 | 100% |
| Mycoplasma sp. 128 (3458463) | - | 1 | 1 | 100% |
| Mycoplasma sp. 13536 (3458679) | - | 1 | 1 | 100% |
| Mycoplasma sp. 3392 (3458465) | - | 1 | 1 | 100% |
| Mycoplasma sp. 392 (3458466) | - | 1 | 1 | 100% |
| Mycoplasma sp. 4044 (3458467) | - | 1 | 1 | 100% |
| Mycoplasma sp. 6934 (3458676) | - | 1 | 1 | 100% |

**Patent records:** 55 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 138 recent records share 16 distinct footprints (8.6 per footprint), of which 80 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 16 and 58 independent observations the fall from baseline is -35% to +15%, which no longer excludes zero.

**Denominator:** 661 of 24191 screened records are evaluable (2.7%); 23530 are not. Every share above is taken over the evaluable ones.

Excluded: 23530 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 22553 no_site, 825 truncated, 152 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 316 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 4829 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 17724 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CDV_H_gene_Mueller_2011_4`

Canine distemper virus specific — H gene  
Designed 2011, doi:10.7589/0090-3558-47.3.725  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 1 | 1 | 100% |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 2 | 2 | 100% |
| 1999 | 1 | 1 | 100% |
| 2000 | 1 | 1 | 100% |
| 2001 | 1 | 1 | 100% |
| 2002 | 3 | 3 | 100% |
| 2003 | 3 | 5 | 60% |
| 2004 | 2 | 2 | 100% |
| 2005 | 3 | 3 | 100% |
| 2006 | 0 | 0 | - |
| 2007 | 0 | 4 | 0% |
| 2008 | 5 | 5 | 100% |
| 2009 | 1 | 4 | 25% |
| 2010 | 3 | 3 | 100% |
| 2011 | 2 | 3 | 67% |
| 2012 | 7 | 7 | 100% |
| 2013 | 1 | 9 | 11% |
| 2014 | 5 | 15 | 33% |
| 2015 | 8 | 8 | 100% |
| 2016 | 11 | 21 | 52% |
| 2017 | 8 | 10 | 80% |
| 2018 | 18 | 24 | 75% |
| 2019 | 18 | 23 | 78% |
| 2020 | 43 | 51 | 84% |
| 2021 | 8 | 9 | 89% |
| 2022 | 16 | 41 | 39% |
| 2023 | 12 | 12 | 100% |
| 2024 | 9 | 10 | 90% |
| 2025 | 3 | 12 | 25% |
| 2026 | 35 | 73 | 48% |

*trend over deposit year: falling, z = -2.47, two-sided p = 0.0136 across 29 years and 363 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 61 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 87 recent records share 16 distinct footprints (5.4 per footprint). This flag does not hold up: with only 16 and 54 independent observations the fall from baseline is -48% to +2%, which no longer excludes zero.

**Denominator:** 363 of 3952 screened records are evaluable (9.2%); 3589 are not. Every share above is taken over the evaluable ones.

Excluded: 3589 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1797 truncated, 1554 no_site, 238 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 2 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 114 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1440 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `PARVOVIRUS_ssDNA_VP1_gene_dependovirus`

PARVOVIRUS (ssDNA) — VP1 gene (dependovirus)  
Designed 2002, doi:10.1073/pnas.182412299  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 0 | - |
| 1984 | 0 | 0 | - |
| 1988 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1991 | 1 | 1 | 100% |
| 1993 | 1 | 1 | 100% |
| 1994 | 0 | 0 | - |
| 1995 | 3 | 6 | 50% |
| 1996 | 2 | 2 | 100% |
| 1997 | 0 | 2 | 0% |
| 1998 | 3 | 3 | 100% |
| 1999 | 2 | 4 | 50% |
| 2001 | 3 | 4 | 75% |
| 2002 | 2 | 2 | 100% |
| 2003 | 38 | 41 | 93% |
| 2004 | 96 | 114 | 84% |
| 2005 | 4 | 8 | 50% |
| 2006 | 5 | 15 | 33% |
| 2007 | 8 | 14 | 57% |
| 2008 | 21 | 31 | 68% |
| 2009 | 1 | 16 | 6% |
| 2010 | 1 | 4 | 25% |
| 2011 | 449 | 472 | 95% |
| 2012 | 1 | 3 | 33% |
| 2013 | 11 | 25 | 44% |
| 2014 | 45 | 60 | 75% |
| 2015 | 11 | 49 | 22% |
| 2016 | 23 | 45 | 51% |
| 2017 | 6 | 22 | 27% |
| 2018 | 227 | 284 | 80% |
| 2019 | 87 | 122 | 71% |
| 2020 | 33 | 84 | 39% |
| 2021 | 114 | 139 | 82% |
| 2022 | 55 | 80 | 69% |
| 2023 | 9 | 51 | 18% |
| 2024 | 11 | 75 | 15% |
| 2025 | 81 | 117 | 69% |
| 2026 | 35 | 132 | 27% |

*trend over deposit year: falling, z = -12.52, two-sided p = 6.09e-36 across 33 years and 2028 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 6845 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 256 recent records share 48 distinct footprints (5.3 per footprint), of which 1 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 48 independent observations (one per footprint) the interval around the 45% detected share is 32%-59%, and counting each footprint once, 25 of 48 footprints amplify (52%; interval 38%-66%); each is below the 90% threshold, and the fall from baseline (-41% to -11%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 2028 of 3240 screened records are evaluable (62.6%); 1212 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 1211 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 905 no_site, 301 truncated, 3 no_pair, 2 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 29 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 905 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `MONKEYPOX_dsDNA_G2R_WestAfrican_TaqMan_Li_2010`

MONKEYPOX virus (dsDNA) — G2R_WA West African clade TaqMan (Li 2010)  
Designed 2010, doi:10.1016/j.jviromet.2010.07.012  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 9 | 13 | 69% |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 0 | 2 | 0% |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 1 | 2 | 50% |
| 2005 | 5 | 7 | 71% |
| 2007 | 0 | 0 | - |
| 2008 | 0 | 0 | - |
| 2009 | 0 | 0 | - |
| 2010 | 0 | 1 | 0% |
| 2011 | 0 | 2 | 0% |
| 2012 | 0 | 0 | - |
| 2013 | 0 | 2 | 0% |
| 2014 | 1 | 24 | 4% |
| 2015 | 5 | 11 | 45% |
| 2018 | 0 | 0 | - |
| 2019 | 8 | 8 | 100% |
| 2020 | 27 | 37 | 73% |
| 2022 | 3313 | 3315 | 100% |
| 2023 | 3007 | 3015 | 100% |
| 2024 | 1542 | 1881 | 82% |
| 2025 | 1017 | 1767 | 58% |
| 2026 | 773 | 2373 | 33% |

*trend over deposit year: falling, z = -49.23, two-sided p = 0 across 16 years and 12460 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 5 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 4351 recent records share 7 distinct footprints (621.6 per footprint), of which 30 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 7 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 12460 of 13752 screened records are evaluable (90.6%); 1292 are not. Every share above is taken over the evaluable ones.

Excluded: 10 indeterminate, 1282 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1272 no_site, 4 chance_pair, 3 no_pair, 3 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 68 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 732 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 540 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CHLAMYDIA_trachomatis_16S_Messmer_1997_round2`

CHLAMYDIA TRACHOMATIS — 16S rRNA nested multiplex PCR, second step (Messmer 1997)  
Designed 1997, doi:10.1128/jcm.35.8.2043-2046.1997  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1996 | 0 | 1 | 0% |
| 1997 | 2 | 6 | 33% |
| 1998 | 0 | 1 | 0% |
| 2001 | 0 | 1 | 0% |
| 2005 | 8 | 21 | 38% |
| 2008 | 2 | 2 | 100% |
| 2009 | 0 | 3 | 0% |
| 2010 | 3 | 9 | 33% |
| 2011 | 1 | 2 | 50% |
| 2012 | 13 | 22 | 59% |
| 2013 | 20 | 22 | 91% |
| 2015 | 8 | 12 | 67% |
| 2016 | 7 | 9 | 78% |
| 2017 | 6 | 33 | 18% |
| 2019 | 2 | 2 | 100% |
| 2021 | 155 | 159 | 97% |
| 2022 | 2 | 2 | 100% |
| 2024 | 10 | 17 | 59% |
| 2025 | 16 | 36 | 44% |
| 2026 | 2 | 2 | 100% |

*trend over deposit year: rising, z = +5.38, two-sided p = 7.26e-08 across 20 years and 362 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 1 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 39 recent records share 4 distinct footprints (9.8 per footprint). This flag does not hold up: only 4 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; counting each footprint once, 3 of 4 footprints amplify (75%; interval 30%-95%), which reaches the 90% threshold: the failing records are concentrated on few footprints; with only 4 and 4 independent observations the fall from baseline is -67% to +30%, which no longer excludes zero. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 362 of 378 screened records are evaluable (95.8%); 16 are not. Every share above is taken over the evaluable ones.

Excluded: 16 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 16 no_site. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 9 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ARENAVIRUS_ssRNA_S_gene_2`

**Lineage override:** pooled status was low coverage.  
ARENAVIRUS (ssRNA) — S gene  
Designed 1997, doi:10.1016/S0168-1702(97)01458-5  
**Degeneracy:** 256-fold degenerate (256-fold primers x 1-fold probe); each member is ~3.9e-03 of the reaction, ~8 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 1 | 0% |
| 1986 | 0 | 0 | - |
| 1987 | 1 | 1 | 100% |
| 1989 | 3 | 5 | 60% |
| 1990 | 1 | 1 | 100% |
| 1991 | 1 | 1 | 100% |
| 1992 | 1 | 1 | 100% |
| 1993 | 4 | 4 | 100% |
| 1995 | 3 | 3 | 100% |
| 1996 | 2 | 2 | 100% |
| 1997 | 2 | 6 | 33% |
| 1998 | 0 | 4 | 0% |
| 1999 | 1 | 1 | 100% |
| 2000 | 2 | 4 | 50% |
| 2001 | 2 | 7 | 29% |
| 2002 | 6 | 19 | 32% |
| 2003 | 4 | 5 | 80% |
| 2004 | 10 | 20 | 50% |
| 2005 | 2 | 3 | 67% |
| 2006 | 11 | 15 | 73% |
| 2007 | 3 | 13 | 23% |
| 2008 | 11 | 22 | 50% |
| 2009 | 34 | 51 | 67% |
| 2010 | 10 | 24 | 42% |
| 2011 | 11 | 28 | 39% |
| 2012 | 34 | 45 | 76% |
| 2013 | 3 | 9 | 33% |
| 2014 | 198 | 225 | 88% |
| 2015 | 18 | 23 | 78% |
| 2016 | 13 | 25 | 52% |
| 2017 | 20 | 37 | 54% |
| 2018 | 261 | 443 | 59% |
| 2019 | 50 | 63 | 79% |
| 2020 | 10 | 43 | 23% |
| 2021 | 32 | 39 | 82% |
| 2022 | 38 | 60 | 63% |
| 2023 | 67 | 145 | 46% |
| 2024 | 14 | 23 | 61% |
| 2025 | 16 | 61 | 26% |
| 2026 | 48 | 74 | 65% |

*trend over deposit year: falling, z = -2.22, two-sided p = 0.0261 across 39 years and 1556 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 473 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| unidentified Reptarenavirus (1654823) | 0 | 210 | 0% |
| taxid 1672385 | 0 | 15 | 0% |
| taxid 2447921 | 0 | 12 | 0% |
| taxid 1382279 | 0 | 12 | 0% |
| taxid 2447931 | 0 | 9 | 0% |
| Aurora borealis virus (1672381) | 0 | 9 | 0% |
| Aurora borealis virus 3 (2447924) | 0 | 9 | 0% |
| taxid 2116467 | 0 | 9 | 0% |
| taxid 1303019 | 0 | 9 | 0% |
| Alethinophid 3 reptarenavirus (1653399) | 0 | 8 | 0% |
| _+57 more taxa_ | | | |


**Patent records:** 226 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 138 recent records share 43 distinct footprints (3.2 per footprint). This flag does not hold up: with only 43 and 195 independent observations the fall from baseline is -31% to +1%, which no longer excludes zero.

**Denominator:** 1556 of 5755 screened records are evaluable (27.0%); 4199 are not. Every share above is taken over the evaluable ones.

Excluded: 2 indeterminate, 4197 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3767 no_site, 383 chance_only, 46 chance_anchor, 1 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 3726 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 41 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `PD_WNS_ITS1_Shuey_2014`

PSEUDOGYMNOASCUS DESTRUCTANS (white-nose syndrome) — ITS1 qPCR (Shuey 2014)  
Designed 2014, doi:10.1128/aem.02897-13  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 2008 | 10 | 10 | 100% |
| 2009 | 16 | 16 | 100% |
| 2010 | 60 | 60 | 100% |
| 2011 | 17 | 17 | 100% |
| 2012 | 14 | 14 | 100% |
| 2013 | 18 | 18 | 100% |
| 2014 | 13 | 14 | 93% |
| 2015 | 63 | 63 | 100% |
| 2016 | 1 | 5 | 20% |
| 2017 | 5 | 11 | 45% |
| 2018 | 3 | 8 | 38% |
| 2019 | 130 | 144 | 90% |
| 2020 | 0 | 11 | 0% |
| 2021 | 19 | 25 | 76% |
| 2022 | 10 | 15 | 67% |
| 2023 | 0 | 10 | 0% |
| 2024 | 1 | 4 | 25% |
| 2025 | 7 | 12 | 58% |

*trend over deposit year: falling, z = -8.40, two-sided p = 4.58e-17 across 18 years and 457 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 16 recent records share 4 distinct footprints (4.0 per footprint). This flag does not hold up: only 4 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 4 and 12 independent observations the fall from baseline is -72% to +9%, which no longer excludes zero.

**Denominator:** 457 of 12691 screened records are evaluable (3.6%); 12234 are not. Every share above is taken over the evaluable ones.

Excluded: 12234 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 12226 no_site, 5 chance_anchor, 3 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 3 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 18 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 12208 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_Lan_2010_round1`

**Lineage override:** pooled status was low coverage.  
CORONAVIRUS (ssRNA) — RNA-dependent RNA polymerase  
Designed 2010, doi:10.1128/mBio.00208-10  
**Degeneracy:** 1327104-fold degenerate (1327104-fold primers x 1-fold probe); ~20 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 2 | 2 | 100% |
| 1997 | 2 | 2 | 100% |
| 1998 | 0 | 0 | - |
| 1999 | 1 | 1 | 100% |
| 2000 | 5 | 5 | 100% |
| 2001 | 5 | 7 | 71% |
| 2002 | 1 | 1 | 100% |
| 2003 | 50 | 50 | 100% |
| 2004 | 60 | 67 | 90% |
| 2005 | 30 | 32 | 94% |
| 2006 | 20 | 45 | 44% |
| 2007 | 15 | 32 | 47% |
| 2008 | 14 | 28 | 50% |
| 2009 | 88 | 92 | 96% |
| 2010 | 35 | 45 | 78% |
| 2011 | 73 | 86 | 85% |
| 2012 | 50 | 98 | 51% |
| 2013 | 110 | 178 | 62% |
| 2014 | 154 | 237 | 65% |
| 2015 | 193 | 361 | 53% |
| 2016 | 168 | 287 | 59% |
| 2017 | 237 | 597 | 40% |
| 2018 | 158 | 370 | 43% |
| 2019 | 140 | 285 | 49% |
| 2020 | 202 | 362 | 56% |
| 2021 | 215 | 378 | 57% |
| 2022 | 274 | 466 | 59% |
| 2023 | 510 | 1021 | 50% |
| 2024 | 213 | 443 | 48% |
| 2025 | 478 | 922 | 52% |
| 2026 | 336 | 570 | 59% |

*trend over deposit year: falling, z = -8.11, two-sided p = 4.91e-16 across 30 years and 7070 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 262 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Rodent coronavirus MmONCAN (3687432) | 1 | 2 | 50% |
| Rodent coronavirus PlONCAN (3687427) | 10 | 23 | 43% |
| Rodent coronavirus PmONCAN (3687430) | 3 | 19 | 16% |
| Betacoronavirus (694002) | 0 | 158 | 0% |
| Alphacoronavirus (693996) | 0 | 42 | 0% |
| Rodent coronavirus CgONCAN (3687429) | 0 | 6 | 0% |
| Rodent coronavirus MpONCAN (3687431) | 0 | 4 | 0% |
| Igacovirus sp. (3049965) | 0 | 2 | 0% |
| Rodent coronavirus NiONCAN (3687428) | 0 | 2 | 0% |
| Malhaem virus 1 (3456161) | 0 | 1 | 0% |
| _+3 more taxa_ | | | |


**Duplication check:** 1641 recent records share 201 distinct footprints (8.2 per footprint), of which 24 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 201 and 480 independent observations the fall from baseline is -11% to +5%, which no longer excludes zero.

**Denominator:** 7070 of 25297 screened records are evaluable (27.9%); 18227 are not. Every share above is taken over the evaluable ones.

Excluded: 18227 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 18180 no_site, 31 chance_anchor, 16 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 76 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 18178 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `SBV_polyprotein_Rossi_2024`

SACBROOD VIRUS — polyprotein gene RT-qPCR, hydrolysis probe (Rossi 2024)  
Designed 2024, doi:10.3390/microorganisms12061105  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1999 | 2 | 2 | 100% |
| 2000 | 0 | 0 | - |
| 2001 | 12 | 14 | 86% |
| 2002 | 1 | 1 | 100% |
| 2003 | 3 | 3 | 100% |
| 2004 | 1 | 1 | 100% |
| 2006 | 0 | 0 | - |
| 2007 | 1 | 1 | 100% |
| 2008 | 0 | 0 | - |
| 2009 | 1 | 1 | 100% |
| 2010 | 0 | 1 | 0% |
| 2011 | 12 | 12 | 100% |
| 2012 | 13 | 15 | 87% |
| 2013 | 8 | 11 | 73% |
| 2014 | 28 | 33 | 85% |
| 2015 | 6 | 6 | 100% |
| 2016 | 4 | 4 | 100% |
| 2017 | 11 | 14 | 79% |
| 2018 | 9 | 15 | 60% |
| 2019 | 17 | 17 | 100% |
| 2020 | 6 | 8 | 75% |
| 2021 | 92 | 96 | 96% |
| 2022 | 14 | 14 | 100% |
| 2023 | 13 | 17 | 76% |
| 2024 | 28 | 38 | 74% |
| 2025 | 17 | 32 | 53% |
| 2026 | 5 | 9 | 56% |

*trend over deposit year: falling, z = -2.49, two-sided p = 0.0127 across 24 years and 365 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 1 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 42 recent records share 12 distinct footprints (3.5 per footprint). This flag does not hold up: only 12 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 365 of 899 screened records are evaluable (40.6%); 534 are not. Every share above is taken over the evaluable ones.

Excluded: 534 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 524 no_site, 10 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 1 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 524 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CDV_N_gene_Elia_2006`

**Lineage override:** pooled status was low coverage.  
CANINE DISTEMPER VIRUS — N gene TaqMan RT-qPCR (Elia 2006)  
Designed 2006, doi:10.1016/j.jviromet.2006.05.004  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 1 | 0% |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 0 | 0 | - |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 2 | 0% |
| 1999 | 7 | 9 | 78% |
| 2000 | 0 | 1 | 0% |
| 2001 | 0 | 1 | 0% |
| 2002 | 0 | 3 | 0% |
| 2003 | 6 | 6 | 100% |
| 2004 | 4 | 6 | 67% |
| 2005 | 9 | 12 | 75% |
| 2006 | 4 | 6 | 67% |
| 2007 | 3 | 5 | 60% |
| 2008 | 6 | 17 | 35% |
| 2009 | 7 | 32 | 22% |
| 2010 | 7 | 13 | 54% |
| 2011 | 11 | 18 | 61% |
| 2012 | 26 | 33 | 79% |
| 2013 | 37 | 45 | 82% |
| 2014 | 9 | 22 | 41% |
| 2015 | 5 | 10 | 50% |
| 2016 | 35 | 50 | 70% |
| 2017 | 3 | 14 | 21% |
| 2018 | 12 | 33 | 36% |
| 2019 | 10 | 27 | 37% |
| 2020 | 30 | 77 | 39% |
| 2021 | 20 | 21 | 95% |
| 2022 | 15 | 57 | 26% |
| 2023 | 4 | 21 | 19% |
| 2024 | 11 | 14 | 79% |
| 2025 | 8 | 26 | 31% |
| 2026 | 51 | 77 | 66% |

*trend over deposit year: falling, z = -1.32, two-sided p = 0.187 across 30 years and 659 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 61 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 105 recent records share 23 distinct footprints (4.6 per footprint). This flag does not hold up: with only 23 and 89 independent observations the fall from baseline is -16% to +27%, which no longer excludes zero.

**Denominator:** 659 of 3952 screened records are evaluable (16.7%); 3293 are not. Every share above is taken over the evaluable ones.

Excluded: 3293 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3282 no_site, 11 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 3282 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010`

**Lineage override:** pooled status was low coverage.  
MONKEYPOX virus (dsDNA) — G2R_G generic TaqMan (Li 2010)  
Designed 2010, doi:10.1016/j.jviromet.2010.07.012  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 12 | 13 | 92% |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 2 | 2 | 100% |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 1 | 2 | 50% |
| 2005 | 7 | 7 | 100% |
| 2007 | 0 | 0 | - |
| 2008 | 0 | 0 | - |
| 2009 | 0 | 0 | - |
| 2010 | 1 | 5 | 20% |
| 2011 | 2 | 2 | 100% |
| 2012 | 0 | 0 | - |
| 2013 | 2 | 2 | 100% |
| 2014 | 24 | 24 | 100% |
| 2015 | 11 | 11 | 100% |
| 2018 | 0 | 0 | - |
| 2019 | 8 | 8 | 100% |
| 2020 | 37 | 37 | 100% |
| 2022 | 86 | 3274 | 3% |
| 2023 | 16 | 2949 | 0.5% |
| 2024 | 376 | 1862 | 20% |
| 2025 | 999 | 1745 | 57% |
| 2026 | 1506 | 2372 | 63% |

*trend over deposit year: rising, z = +41.25, two-sided p = 0 across 16 years and 12315 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 5 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 4328 recent records share 11 distinct footprints (393.5 per footprint), of which 165 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 11 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; counting each footprint once, 9 of 11 footprints amplify (82%; interval 52%-95%), which reaches the 90% threshold: the failing records are concentrated on few footprints; with only 11 and 25 independent observations the fall from baseline is +19% to +74%, which no longer excludes zero. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 12315 of 13752 screened records are evaluable (89.6%); 1437 are not. Every share above is taken over the evaluable ones.

Excluded: 11 indeterminate, 1426 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1406 no_site, 9 truncated, 7 no_pair, 4 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 263 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1404 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `E_coli_malB_Candrian_1991`

E. coli-malB promoter  
Designed 1991, doi:10.1016/0168-1605(91)90148-I  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 1 | 1 | 100% |
| 2002 | 1 | 1 | 100% |
| 2004 | 1 | 1 | 100% |
| 2006 | 4 | 4 | 100% |
| 2007 | 1 | 2 | 50% |
| 2008 | 10 | 12 | 83% |
| 2009 | 8 | 11 | 73% |
| 2010 | 11 | 12 | 92% |
| 2011 | 5 | 5 | 100% |
| 2012 | 7 | 10 | 70% |
| 2013 | 5 | 7 | 71% |
| 2014 | 17 | 20 | 85% |
| 2015 | 17 | 20 | 85% |
| 2016 | 10 | 20 | 50% |
| 2017 | 16 | 20 | 80% |
| 2018 | 13 | 20 | 65% |
| 2019 | 16 | 20 | 80% |
| 2020 | 12 | 20 | 60% |
| 2021 | 16 | 20 | 80% |
| 2022 | 14 | 20 | 70% |
| 2023 | 15 | 20 | 75% |
| 2024 | 11 | 20 | 55% |
| 2025 | 14 | 20 | 70% |
| 2026 | 9 | 20 | 45% |

*trend over deposit year: falling, z = -3.08, two-sided p = 0.00206 across 24 years and 326 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 49 recent records share 5 distinct footprints (9.8 per footprint). This flag does not hold up: only 5 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 5 and 6 independent observations the fall from baseline is -56% to +33%, which no longer excludes zero.

**Denominator:** 326 of 401 screened records are evaluable (81.3%); 75 are not. Every share above is taken over the evaluable ones.

Excluded: 75 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 73 no_site, 2 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 73 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `INFLUENZA_A_ssRNA_NP_Tsukamoto_2010`

**Lineage override:** pooled status was low coverage.  
Influenza A virus — nucleoprotein (NP) gene rRT-PCR (Tsukamoto 2010)  
Designed 2010, doi:10.1128/JCM.01264-10  
**Degeneracy:** 128-fold degenerate (16-fold primers x 8-fold probe); ~7 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 1 | 0% |
| 1987 | 0 | 1 | 0% |
| 1988 | 2 | 3 | 67% |
| 1989 | 11 | 15 | 73% |
| 1990 | 22 | 30 | 73% |
| 1991 | 2 | 8 | 25% |
| 1992 | 8 | 9 | 89% |
| 1993 | 74 | 89 | 83% |
| 1994 | 6 | 8 | 75% |
| 1995 | 4 | 4 | 100% |
| 1996 | 0 | 3 | 0% |
| 1997 | 1 | 2 | 50% |
| 1998 | 13 | 17 | 76% |
| 1999 | 26 | 30 | 87% |
| 2000 | 39 | 44 | 89% |
| 2001 | 22 | 32 | 69% |
| 2002 | 40 | 50 | 80% |
| 2003 | 73 | 109 | 67% |
| 2004 | 117 | 130 | 90% |
| 2005 | 194 | 837 | 23% |
| 2006 | 987 | 1947 | 51% |
| 2007 | 629 | 1193 | 53% |
| 2008 | 914 | 1146 | 80% |
| 2009 | 2164 | 2647 | 82% |
| 2010 | 2844 | 3433 | 83% |
| 2011 | 2424 | 3029 | 80% |
| 2012 | 2473 | 3505 | 71% |
| 2013 | 3967 | 4903 | 81% |
| 2014 | 3283 | 4739 | 69% |
| 2015 | 3788 | 5106 | 74% |
| 2016 | 4424 | 7102 | 62% |
| 2017 | 3720 | 7889 | 47% |
| 2018 | 3936 | 6893 | 57% |
| 2019 | 5509 | 11712 | 47% |
| 2020 | 6090 | 7525 | 81% |
| 2021 | 2691 | 3132 | 86% |
| 2022 | 2683 | 8804 | 30% |
| 2023 | 7170 | 13397 | 54% |
| 2024 | 15666 | 23412 | 67% |
| 2025 | 22100 | 35912 | 62% |
| 2026 | 15539 | 28063 | 55% |

*trend over deposit year: falling, z = -30.72, two-sided p = 2.95e-207 across 41 years and 186911 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 69571 recent records share 202 distinct footprints (344.4 per footprint), of which 10 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 202 and 472 independent observations the fall from baseline is -8% to +8%, which no longer excludes zero.

**Denominator:** 186911 of 191425 screened records are evaluable (97.6%); 4514 are not. Every share above is taken over the evaluable ones.

Excluded: 12 indeterminate, 4502 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3304 truncated, 1196 no_site, 2 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 64 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 41 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1155 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `FILOVIRUS_ssRNA_L_gene`

FILOVIRUS (ssRNA) — L gene  
Designed 2007, doi:10.1128/Jcm.01893-06  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1989 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1991 | 0 | 0 | - |
| 1992 | 2 | 2 | 100% |
| 1993 | 1 | 1 | 100% |
| 1994 | 2 | 2 | 100% |
| 1995 | 1 | 1 | 100% |
| 1996 | 0 | 0 | - |
| 1997 | 1 | 1 | 100% |
| 1998 | 0 | 0 | - |
| 1999 | 2 | 2 | 100% |
| 2000 | 1 | 1 | 100% |
| 2001 | 1 | 1 | 100% |
| 2002 | 4 | 4 | 100% |
| 2003 | 2 | 2 | 100% |
| 2004 | 5 | 5 | 100% |
| 2005 | 1 | 1 | 100% |
| 2006 | 13 | 13 | 100% |
| 2007 | 3 | 3 | 100% |
| 2008 | 1 | 3 | 33% |
| 2009 | 29 | 29 | 100% |
| 2010 | 18 | 32 | 56% |
| 2011 | 4 | 8 | 50% |
| 2012 | 36 | 36 | 100% |
| 2013 | 29 | 33 | 88% |
| 2014 | 119 | 119 | 100% |
| 2015 | 949 | 952 | 100% |
| 2016 | 921 | 921 | 100% |
| 2017 | 149 | 151 | 99% |
| 2018 | 222 | 227 | 98% |
| 2019 | 276 | 276 | 100% |
| 2020 | 10 | 27 | 37% |
| 2021 | 691 | 694 | 100% |
| 2022 | 29 | 34 | 85% |
| 2023 | 154 | 160 | 96% |
| 2024 | 94 | 96 | 98% |
| 2025 | 9 | 9 | 100% |
| 2026 | 32 | 67 | 48% |

*trend over deposit year: falling, z = -7.22, two-sided p = 5.27e-13 across 33 years and 3913 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 85 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 95 recent records share 8 distinct footprints (11.9 per footprint). This flag does not hold up: only 8 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; counting each footprint once, 6 of 8 footprints amplify (75%; interval 41%-93%), which reaches the 90% threshold: the failing records are concentrated on few footprints. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 3913 of 4601 screened records are evaluable (85.0%); 688 are not. Every share above is taken over the evaluable ones.

Excluded: 6 indeterminate, 682 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 525 no_site, 114 chance_anchor, 43 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 1 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 523 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Pan_hemoparasite_cytochrome_c_Hellgren_2004`

Pan-hemoparasite — cytochrome c  
Designed 2004, doi:10.1645/GE-184R1  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1998 | 3 | 3 | 100% |
| 2000 | 0 | 0 | - |
| 2002 | 37 | 38 | 97% |
| 2003 | 0 | 0 | - |
| 2004 | 5 | 5 | 100% |
| 2005 | 1 | 41 | 2% |
| 2006 | 15 | 15 | 100% |
| 2007 | 3 | 3 | 100% |
| 2008 | 27 | 32 | 84% |
| 2009 | 34 | 41 | 83% |
| 2010 | 71 | 81 | 88% |
| 2011 | 19 | 32 | 59% |
| 2012 | 1 | 7 | 14% |
| 2013 | 8 | 11 | 73% |
| 2014 | 12 | 13 | 92% |
| 2015 | 14 | 14 | 100% |
| 2016 | 11 | 12 | 92% |
| 2017 | 70 | 76 | 92% |
| 2018 | 75 | 78 | 96% |
| 2019 | 6 | 16 | 38% |
| 2020 | 85 | 87 | 98% |
| 2021 | 4 | 4 | 100% |
| 2022 | 59 | 61 | 97% |
| 2023 | 87 | 99 | 88% |
| 2024 | 7 | 61 | 11% |
| 2025 | 69 | 121 | 57% |
| 2026 | 51 | 72 | 71% |

*trend over deposit year: falling, z = -2.07, two-sided p = 0.0382 across 25 years and 1023 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 13071 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Hepatocystis sp. TLG-2012 (1266736) | 74 | 74 | 100% |
| Plasmodium tupinambi (3448513) | 29 | 29 | 100% |
| Haemosporida sp. B LB-2015 (1699100) | 27 | 27 | 100% |
| Plasmodium sp. BM-2016a (1830315) | 24 | 24 | 100% |
| Plasmodiidae sp. (2605378) | 22 | 22 | 100% |
| Plasmodium brasilianum (5824) | 12 | 12 | 100% |
| Haemosporida sp. A LB-2015 (1699099) | 11 | 11 | 100% |
| Nycteria heischi (1891981) | 10 | 10 | 100% |
| taxid 31271 | 10 | 10 | 100% |
| taxid 138297 | 10 | 10 | 100% |
| _+1970 more taxa_ | | | |


**Duplication check:** 194 recent records share 33 distinct footprints (5.9 per footprint). This flag does not hold up: with only 33 and 89 independent observations the fall from baseline is -35% to +0.9%, which no longer excludes zero.

**Denominator:** 1023 of 18968 screened records are evaluable (5.4%); 17945 are not. Every share above is taken over the evaluable ones.

Excluded: 17945 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 16581 no_site, 948 truncated, 402 chance_anchor, 14 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 2 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 4998 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 11583 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `West_Nile_Virus_Envelope_glycoprotein_E_Lanciotti_2001`

West Nile Virus — Envelope glycoprotein E  
Designed 2001, doi:10.1128/JCM.39.12.4506-4513.2001  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1988 | 0 | 0 | - |
| 1993 | 0 | 3 | 0% |
| 1995 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1999 | 6 | 6 | 100% |
| 2000 | 4 | 4 | 100% |
| 2001 | 43 | 82 | 52% |
| 2002 | 15 | 16 | 94% |
| 2003 | 23 | 36 | 64% |
| 2004 | 88 | 89 | 99% |
| 2005 | 97 | 97 | 100% |
| 2006 | 333 | 335 | 99% |
| 2007 | 84 | 85 | 99% |
| 2008 | 158 | 168 | 94% |
| 2009 | 33 | 33 | 100% |
| 2010 | 521 | 535 | 97% |
| 2011 | 218 | 223 | 98% |
| 2012 | 59 | 64 | 92% |
| 2013 | 84 | 101 | 83% |
| 2014 | 621 | 633 | 98% |
| 2015 | 122 | 161 | 76% |
| 2016 | 478 | 524 | 91% |
| 2017 | 36 | 47 | 77% |
| 2018 | 178 | 206 | 86% |
| 2019 | 477 | 500 | 95% |
| 2020 | 50 | 113 | 44% |
| 2021 | 7 | 31 | 23% |
| 2022 | 124 | 246 | 50% |
| 2023 | 796 | 943 | 84% |
| 2024 | 669 | 762 | 88% |
| 2025 | 401 | 636 | 63% |
| 2026 | 36 | 405 | 9% |

*trend over deposit year: falling, z = -25.58, two-sided p = 2.45e-144 across 29 years and 7084 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 89 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1722 recent records share 38 distinct footprints (45.3 per footprint), of which 4 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 38 independent observations (one per footprint) the interval around the 64% detected share is 48%-77%, and counting each footprint once, 29 of 38 footprints amplify (76%; interval 61%-87%); each is below the 90% threshold, and the fall from baseline (-40% to -8%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 7084 of 9062 screened records are evaluable (78.2%); 1978 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 1977 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1699 no_site, 150 truncated, 128 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 37 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 16 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1683 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `BQCV_capsid_Rossi_2024`

BLACK QUEEN CELL VIRUS — capsid gene RT-qPCR, MGB probe (Rossi 2024)  
Designed 2024, doi:10.3390/microorganisms12061105  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1999 | 0 | 0 | - |
| 2000 | 2 | 2 | 100% |
| 2002 | 1 | 1 | 100% |
| 2003 | 0 | 0 | - |
| 2004 | 1 | 1 | 100% |
| 2005 | 1 | 1 | 100% |
| 2006 | 1 | 1 | 100% |
| 2007 | 1 | 1 | 100% |
| 2008 | 5 | 6 | 83% |
| 2009 | 4 | 4 | 100% |
| 2010 | 7 | 8 | 88% |
| 2011 | 46 | 77 | 60% |
| 2012 | 50 | 51 | 98% |
| 2013 | 6 | 6 | 100% |
| 2014 | 19 | 19 | 100% |
| 2015 | 80 | 98 | 82% |
| 2016 | 37 | 38 | 97% |
| 2017 | 23 | 36 | 64% |
| 2018 | 77 | 90 | 86% |
| 2019 | 136 | 143 | 95% |
| 2020 | 55 | 79 | 70% |
| 2021 | 121 | 131 | 92% |
| 2022 | 24 | 43 | 56% |
| 2023 | 92 | 104 | 88% |
| 2024 | 153 | 195 | 78% |
| 2025 | 23 | 40 | 57% |
| 2026 | 15 | 34 | 44% |

*trend over deposit year: falling, z = -2.49, two-sided p = 0.0129 across 25 years and 1209 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 3 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 152 recent records share 25 distinct footprints (6.1 per footprint). This flag does not hold up: with only 25 and 79 independent observations the fall from baseline is -39% to +0.1%, which no longer excludes zero.

**Denominator:** 1209 of 1593 screened records are evaluable (75.9%); 384 are not. Every share above is taken over the evaluable ones.

Excluded: 3 indeterminate, 381 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 343 no_site, 28 chance_anchor, 10 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 3 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 30 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 313 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `RHABDOVIRUS_ssRNA_L_gene_round2`

**Lineage override:** pooled status was low coverage.  
RHABDOVIRUS (ssRNA) — L (pan-rhabdovirus, PREDICT P-016 round 2)  
Designed 2005, doi:10.1099/vir.0.81128-0  
**Degeneracy:** 36864-fold degenerate (36864-fold primers x 1-fold probe); ~15 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 1 | 1 | 100% |
| 1986 | 1 | 1 | 100% |
| 1988 | 0 | 0 | - |
| 1989 | 1 | 1 | 100% |
| 1990 | 2 | 2 | 100% |
| 1993 | 2 | 2 | 100% |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 2 | 0% |
| 1997 | 4 | 4 | 100% |
| 1999 | 2 | 2 | 100% |
| 2000 | 4 | 4 | 100% |
| 2001 | 1 | 1 | 100% |
| 2002 | 6 | 7 | 86% |
| 2003 | 2 | 2 | 100% |
| 2004 | 2 | 2 | 100% |
| 2005 | 4 | 7 | 57% |
| 2006 | 3 | 5 | 60% |
| 2007 | 22 | 27 | 81% |
| 2008 | 38 | 42 | 90% |
| 2009 | 21 | 21 | 100% |
| 2010 | 51 | 54 | 94% |
| 2011 | 18 | 20 | 90% |
| 2012 | 197 | 214 | 92% |
| 2013 | 52 | 56 | 93% |
| 2014 | 79 | 92 | 86% |
| 2015 | 252 | 316 | 80% |
| 2016 | 294 | 397 | 74% |
| 2017 | 163 | 582 | 28% |
| 2018 | 154 | 301 | 51% |
| 2019 | 275 | 609 | 45% |
| 2020 | 337 | 445 | 76% |
| 2021 | 167 | 244 | 68% |
| 2022 | 304 | 459 | 66% |
| 2023 | 813 | 969 | 84% |
| 2024 | 654 | 1000 | 65% |
| 2025 | 206 | 431 | 48% |
| 2026 | 236 | 301 | 78% |

*trend over deposit year: falling, z = -2.33, two-sided p = 0.0197 across 35 years and 6623 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 769 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| taxid 3083351 | 4 | 4 | 100% |
| taxid 3128382 | 1 | 1 | 100% |
| Betaplatrhavirus himastelon (3427268) | 1 | 1 | 100% |
| taxid 3084896 | 1 | 1 | 100% |
| taxid 3084895 | 1 | 1 | 100% |
| taxid 2910403 | 1 | 1 | 100% |
| taxid 2910388 | 1 | 1 | 100% |
| taxid 2910389 | 1 | 1 | 100% |
| taxid 2793798 | 1 | 1 | 100% |
| taxid 2729339 | 1 | 1 | 100% |
| _+192 more taxa_ | | | |


**Duplication check:** 1271 recent records share 108 distinct footprints (11.8 per footprint), of which 16 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 108 and 225 independent observations the fall from baseline is -11% to +11%, which no longer excludes zero.

**Denominator:** 6623 of 9126 screened records are evaluable (72.6%); 2503 are not. Every share above is taken over the evaluable ones.

Excluded: 10 indeterminate, 2493 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 2038 no_site, 403 truncated, 44 chance_anchor, 8 chance_only. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 47 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1302 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 736 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CDV_H_gene_Mueller_2011_1`

Canine distemper virus specific — H gene  
Designed 2011, doi:10.7589/0090-3558-47.3.725  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 1 | 1 | 100% |
| 1994 | 1 | 1 | 100% |
| 1995 | 0 | 0 | - |
| 1996 | 10 | 10 | 100% |
| 1997 | 3 | 3 | 100% |
| 1998 | 3 | 3 | 100% |
| 1999 | 5 | 5 | 100% |
| 2000 | 2 | 2 | 100% |
| 2001 | 1 | 1 | 100% |
| 2002 | 4 | 4 | 100% |
| 2003 | 5 | 5 | 100% |
| 2004 | 10 | 10 | 100% |
| 2005 | 8 | 9 | 89% |
| 2006 | 1 | 1 | 100% |
| 2007 | 4 | 4 | 100% |
| 2008 | 8 | 8 | 100% |
| 2009 | 24 | 24 | 100% |
| 2010 | 3 | 3 | 100% |
| 2011 | 4 | 4 | 100% |
| 2012 | 7 | 7 | 100% |
| 2013 | 9 | 9 | 100% |
| 2014 | 15 | 16 | 94% |
| 2015 | 8 | 8 | 100% |
| 2016 | 22 | 24 | 92% |
| 2017 | 16 | 16 | 100% |
| 2018 | 81 | 86 | 94% |
| 2019 | 21 | 24 | 88% |
| 2020 | 43 | 52 | 83% |
| 2021 | 8 | 10 | 80% |
| 2022 | 41 | 41 | 100% |
| 2023 | 10 | 12 | 83% |
| 2024 | 17 | 17 | 100% |
| 2025 | 12 | 13 | 92% |
| 2026 | 49 | 80 | 61% |

*trend over deposit year: falling, z = -5.82, two-sided p = 5.91e-09 across 33 years and 513 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 61 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 95 recent records share 24 distinct footprints (4.0 per footprint). Both reductions leave the flag in place: with only 24 independent observations (one per footprint) the interval around the 66% detected share is 46%-82%, and counting each footprint once, 16 of 24 footprints amplify (67%; interval 47%-82%); each is below the 90% threshold, and the fall from baseline (-48% to -10%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 513 of 3952 screened records are evaluable (13.0%); 3439 are not. Every share above is taken over the evaluable ones.

Excluded: 3439 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1846 no_site, 1531 truncated, 62 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 5 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 384 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1462 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CDV_H_gene_Mueller_2011_2`

**Lineage override:** pooled status was low coverage.  
Canine distemper virus specific — H gene  
Designed 2011, doi:10.7589/0090-3558-47.3.725  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 1 | 1 | 100% |
| 1994 | 1 | 1 | 100% |
| 1995 | 0 | 0 | - |
| 1996 | 12 | 13 | 92% |
| 1997 | 0 | 3 | 0% |
| 1998 | 2 | 3 | 67% |
| 1999 | 7 | 8 | 88% |
| 2000 | 2 | 2 | 100% |
| 2001 | 4 | 5 | 80% |
| 2002 | 5 | 5 | 100% |
| 2003 | 9 | 11 | 82% |
| 2004 | 15 | 15 | 100% |
| 2005 | 16 | 37 | 43% |
| 2006 | 12 | 18 | 67% |
| 2007 | 31 | 50 | 62% |
| 2008 | 16 | 54 | 30% |
| 2009 | 40 | 116 | 34% |
| 2010 | 28 | 47 | 60% |
| 2011 | 43 | 57 | 75% |
| 2012 | 23 | 57 | 40% |
| 2013 | 33 | 57 | 58% |
| 2014 | 82 | 111 | 74% |
| 2015 | 15 | 52 | 29% |
| 2016 | 16 | 51 | 31% |
| 2017 | 40 | 84 | 48% |
| 2018 | 105 | 165 | 64% |
| 2019 | 49 | 76 | 64% |
| 2020 | 72 | 104 | 69% |
| 2021 | 228 | 257 | 89% |
| 2022 | 89 | 103 | 86% |
| 2023 | 93 | 97 | 96% |
| 2024 | 29 | 88 | 33% |
| 2025 | 21 | 35 | 60% |
| 2026 | 101 | 149 | 68% |

*trend over deposit year: rising, z = +5.79, two-sided p = 6.86e-09 across 33 years and 1932 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 61 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 188 recent records share 48 distinct footprints (3.9 per footprint). This flag does not hold up: with only 48 and 163 independent observations the fall from baseline is -13% to +17%, which no longer excludes zero.

**Denominator:** 1932 of 3952 screened records are evaluable (48.9%); 2020 are not. Every share above is taken over the evaluable ones.

Excluded: 2020 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1575 no_site, 434 truncated, 11 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 5 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 40 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1535 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Pan_HERPES_dsDNA_Polymerase_round2`

Pan-HERPES (dsDNA) — Polymerase  
Designed 1996, doi:10.1128/jcm.34.7.1666-1671.1996  
**Degeneracy:** 12288-fold degenerate (12288-fold primers x 1-fold probe); ~14 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1986 | 1 | 1 | 100% |
| 1987 | 3 | 3 | 100% |
| 1988 | 2 | 2 | 100% |
| 1989 | 0 | 0 | - |
| 1990 | 2 | 2 | 100% |
| 1991 | 1 | 2 | 50% |
| 1992 | 2 | 2 | 100% |
| 1993 | 2 | 3 | 67% |
| 1994 | 0 | 1 | 0% |
| 1995 | 2 | 4 | 50% |
| 1996 | 0 | 1 | 0% |
| 1997 | 5 | 11 | 45% |
| 1998 | 1 | 6 | 17% |
| 1999 | 1 | 15 | 7% |
| 2000 | 2 | 15 | 13% |
| 2001 | 10 | 20 | 50% |
| 2002 | 7 | 9 | 78% |
| 2003 | 7 | 12 | 58% |
| 2004 | 21 | 41 | 51% |
| 2005 | 16 | 28 | 57% |
| 2006 | 12 | 17 | 71% |
| 2007 | 7 | 17 | 41% |
| 2008 | 9 | 16 | 56% |
| 2009 | 5 | 17 | 29% |
| 2010 | 73 | 76 | 96% |
| 2011 | 69 | 92 | 75% |
| 2012 | 130 | 159 | 82% |
| 2013 | 52 | 67 | 78% |
| 2014 | 63 | 104 | 61% |
| 2015 | 187 | 235 | 80% |
| 2016 | 252 | 279 | 90% |
| 2017 | 176 | 216 | 81% |
| 2018 | 248 | 303 | 82% |
| 2019 | 560 | 611 | 92% |
| 2020 | 55 | 69 | 80% |
| 2021 | 75 | 105 | 71% |
| 2022 | 150 | 231 | 65% |
| 2023 | 217 | 273 | 79% |
| 2024 | 316 | 359 | 88% |
| 2025 | 119 | 165 | 72% |
| 2026 | 74 | 118 | 63% |

*trend over deposit year: rising, z = +6.48, two-sided p = 8.94e-11 across 40 years and 3707 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 2 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Cervid gammaherpesvirus (3683214) | 0 | 1 | 0% |
| synthetic construct (32630) | 0 | 1 | 0% |


**Duplication check:** 357 recent records share 32 distinct footprints (11.2 per footprint), of which 3 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 32 and 160 independent observations the fall from baseline is -27% to +6%, which no longer excludes zero.

**Denominator:** 3707 of 7711 screened records are evaluable (48.1%); 4004 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 4003 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 2274 no_site, 1122 truncated, 343 no_pair, 264 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 36 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 20 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 2254 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999`

**Lineage override:** pooled status was low coverage.  
PAPILLOMAVIRUS (dsDNA) — L1 gene  
Designed 1999, doi:10.1099/0022-1317-80-9-2437  
**Degeneracy:** 288-fold degenerate (288-fold primers x 1-fold probe); each member is ~3.5e-03 of the reaction, ~8 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 2 | 0% |
| 1984 | 0 | 0 | - |
| 1985 | 2 | 2 | 100% |
| 1986 | 3 | 3 | 100% |
| 1987 | 4 | 4 | 100% |
| 1988 | 1 | 1 | 100% |
| 1989 | 1 | 1 | 100% |
| 1990 | 1 | 1 | 100% |
| 1991 | 3 | 7 | 43% |
| 1992 | 2 | 3 | 67% |
| 1993 | 48 | 63 | 76% |
| 1994 | 3 | 5 | 60% |
| 1995 | 20 | 58 | 34% |
| 1996 | 4 | 7 | 57% |
| 1997 | 3 | 12 | 25% |
| 1998 | 22 | 27 | 81% |
| 1999 | 3 | 8 | 38% |
| 2000 | 7 | 13 | 54% |
| 2001 | 9 | 11 | 82% |
| 2002 | 6 | 25 | 24% |
| 2003 | 7 | 21 | 33% |
| 2004 | 14 | 22 | 64% |
| 2005 | 37 | 56 | 66% |
| 2006 | 13 | 33 | 39% |
| 2007 | 70 | 96 | 73% |
| 2008 | 131 | 160 | 82% |
| 2009 | 43 | 147 | 29% |
| 2010 | 123 | 142 | 87% |
| 2011 | 591 | 678 | 87% |
| 2012 | 184 | 377 | 49% |
| 2013 | 150 | 190 | 79% |
| 2014 | 314 | 393 | 80% |
| 2015 | 141 | 216 | 65% |
| 2016 | 417 | 909 | 46% |
| 2017 | 413 | 703 | 59% |
| 2018 | 299 | 3266 | 9% |
| 2019 | 154 | 348 | 44% |
| 2020 | 487 | 1500 | 32% |
| 2021 | 2177 | 2329 | 93% |
| 2022 | 406 | 716 | 57% |
| 2023 | 528 | 684 | 77% |
| 2024 | 1087 | 1448 | 75% |
| 2025 | 983 | 1215 | 81% |
| 2026 | 179 | 373 | 48% |

*trend over deposit year: rising, z = +11.19, two-sided p = 4.51e-29 across 43 years and 16275 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 1064 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1591 recent records share 200 distinct footprints (8.0 per footprint), of which 3 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 200 and 864 independent observations the fall from baseline is +12% to +26%, which no longer excludes zero.

**Denominator:** 16275 of 41947 screened records are evaluable (38.8%); 25672 are not. Every share above is taken over the evaluable ones.

Excluded: 57 indeterminate, 25615 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 24134 no_site, 535 chance_only, 525 truncated, 405 chance_anchor, 16 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 59 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 9066 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 15068 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CDV_P_gene_Scagliarini_2007`

**Lineage override:** pooled status was low coverage.  
Canine distemper virus — P gene real-time RT-PCR CDVF4/CDVR3 (Scagliarini 2007)  
Designed 2007, doi:10.1007/s11259-007-0020-9  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 1 | 1 | 100% |
| 1992 | 0 | 0 | - |
| 1993 | 1 | 1 | 100% |
| 1994 | 0 | 0 | - |
| 1995 | 1 | 1 | 100% |
| 1996 | 1 | 2 | 50% |
| 1997 | 0 | 0 | - |
| 1998 | 2 | 2 | 100% |
| 1999 | 5 | 7 | 71% |
| 2000 | 6 | 7 | 86% |
| 2001 | 2 | 2 | 100% |
| 2002 | 3 | 3 | 100% |
| 2003 | 23 | 29 | 79% |
| 2004 | 2 | 2 | 100% |
| 2005 | 22 | 28 | 79% |
| 2006 | 4 | 8 | 50% |
| 2007 | 11 | 22 | 50% |
| 2008 | 14 | 16 | 88% |
| 2009 | 24 | 29 | 83% |
| 2010 | 11 | 22 | 50% |
| 2011 | 8 | 10 | 80% |
| 2012 | 23 | 35 | 66% |
| 2013 | 15 | 22 | 68% |
| 2014 | 3 | 16 | 19% |
| 2015 | 12 | 21 | 57% |
| 2016 | 25 | 27 | 93% |
| 2017 | 10 | 11 | 91% |
| 2018 | 14 | 24 | 58% |
| 2019 | 29 | 30 | 97% |
| 2020 | 34 | 50 | 68% |
| 2021 | 3 | 9 | 33% |
| 2022 | 37 | 43 | 86% |
| 2023 | 3 | 14 | 21% |
| 2024 | 14 | 17 | 82% |
| 2025 | 12 | 15 | 80% |
| 2026 | 56 | 76 | 74% |

*trend over deposit year: falling, z = -0.22, two-sided p = 0.823 across 33 years and 602 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 61 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 93 recent records share 19 distinct footprints (4.9 per footprint). This flag does not hold up: with only 19 and 54 independent observations the fall from baseline is -20% to +24%, which no longer excludes zero.

**Denominator:** 602 of 3952 screened records are evaluable (15.2%); 3350 are not. Every share above is taken over the evaluable ones.

Excluded: 3350 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3343 no_site, 7 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 2 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 3343 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ADENOVIRUS_dsDNA_Hexon_gene`

**Lineage override:** pooled status was low coverage.  
ADENOVIRUS (dsDNA) — Hexon gene  
Designed 2005, doi:10.1128/JCM.43.12.6176-6182.2005  
**Degeneracy:** 16-fold degenerate (16-fold primers x 1-fold probe); ~4 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 0 | - |
| 1983 | 0 | 0 | - |
| 1984 | 0 | 0 | - |
| 1985 | 1 | 1 | 100% |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 0 | - |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 2 | 3 | 67% |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 11 | 13 | 85% |
| 1994 | 0 | 1 | 0% |
| 1995 | 3 | 5 | 60% |
| 1996 | 0 | 8 | 0% |
| 1997 | 1 | 2 | 50% |
| 1998 | 3 | 6 | 50% |
| 1999 | 10 | 14 | 71% |
| 2000 | 2 | 15 | 13% |
| 2001 | 22 | 27 | 81% |
| 2002 | 5 | 9 | 56% |
| 2003 | 37 | 45 | 82% |
| 2004 | 21 | 29 | 72% |
| 2005 | 96 | 103 | 93% |
| 2006 | 19 | 20 | 95% |
| 2007 | 23 | 44 | 52% |
| 2008 | 107 | 125 | 86% |
| 2009 | 90 | 102 | 88% |
| 2010 | 59 | 92 | 64% |
| 2011 | 55 | 83 | 66% |
| 2012 | 81 | 97 | 84% |
| 2013 | 152 | 195 | 78% |
| 2014 | 70 | 93 | 75% |
| 2015 | 134 | 160 | 84% |
| 2016 | 53 | 165 | 32% |
| 2017 | 141 | 245 | 58% |
| 2018 | 108 | 130 | 83% |
| 2019 | 126 | 250 | 50% |
| 2020 | 428 | 592 | 72% |
| 2021 | 446 | 508 | 88% |
| 2022 | 259 | 462 | 56% |
| 2023 | 451 | 733 | 62% |
| 2024 | 278 | 442 | 63% |
| 2025 | 341 | 542 | 63% |
| 2026 | 723 | 874 | 83% |

*trend over deposit year: falling, z = -1.73, two-sided p = 0.0832 across 36 years and 6235 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 1043 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1499 recent records share 94 distinct footprints (15.9 per footprint), of which 105 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 94 and 266 independent observations the fall from baseline is -2% to +18%, which no longer excludes zero.

**Denominator:** 6235 of 37920 screened records are evaluable (16.4%); 31685 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 31684 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 24257 no_site, 6185 truncated, 882 chance_anchor, 348 chance_only, 12 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 385 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 13816 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 10441 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2`

**Lineage override:** pooled status was low coverage.  
CORONAVIRUS (ssRNA) — RNA-dependent RNA polymerase  
Designed 2010, doi:10.1128/mBio.00208-10  
**Degeneracy:** 12288-fold degenerate (12288-fold primers x 1-fold probe); ~14 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 2 | 2 | 100% |
| 1997 | 2 | 2 | 100% |
| 1998 | 0 | 0 | - |
| 1999 | 1 | 1 | 100% |
| 2000 | 5 | 5 | 100% |
| 2001 | 7 | 7 | 100% |
| 2002 | 1 | 1 | 100% |
| 2003 | 2 | 50 | 4% |
| 2004 | 8 | 66 | 12% |
| 2005 | 13 | 32 | 41% |
| 2006 | 18 | 45 | 40% |
| 2007 | 33 | 37 | 89% |
| 2008 | 16 | 24 | 67% |
| 2009 | 47 | 92 | 51% |
| 2010 | 32 | 45 | 71% |
| 2011 | 39 | 86 | 45% |
| 2012 | 65 | 88 | 74% |
| 2013 | 103 | 183 | 56% |
| 2014 | 164 | 222 | 74% |
| 2015 | 223 | 353 | 63% |
| 2016 | 182 | 250 | 73% |
| 2017 | 349 | 577 | 60% |
| 2018 | 252 | 349 | 72% |
| 2019 | 212 | 276 | 77% |
| 2020 | 246 | 343 | 72% |
| 2021 | 189 | 344 | 55% |
| 2022 | 428 | 530 | 81% |
| 2023 | 795 | 1022 | 78% |
| 2024 | 301 | 417 | 72% |
| 2025 | 748 | 871 | 86% |
| 2026 | 422 | 562 | 75% |

*trend over deposit year: rising, z = +16.34, two-sided p = 4.85e-60 across 30 years and 6882 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 262 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Rodent coronavirus MmONCAN (3687432) | 1 | 2 | 50% |
| Rodent coronavirus PlONCAN (3687427) | 10 | 23 | 43% |
| Rodent coronavirus PmONCAN (3687430) | 3 | 19 | 16% |
| Betacoronavirus (694002) | 0 | 158 | 0% |
| Alphacoronavirus (693996) | 0 | 42 | 0% |
| Rodent coronavirus CgONCAN (3687429) | 0 | 6 | 0% |
| Rodent coronavirus MpONCAN (3687431) | 0 | 4 | 0% |
| Igacovirus sp. (3049965) | 0 | 2 | 0% |
| Rodent coronavirus NiONCAN (3687428) | 0 | 2 | 0% |
| Malhaem virus 1 (3456161) | 0 | 1 | 0% |
| _+3 more taxa_ | | | |


**Duplication check:** 1569 recent records share 89 distinct footprints (17.6 per footprint), of which 9 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 89 and 160 independent observations the fall from baseline is -1% to +21%, which no longer excludes zero.

**Denominator:** 6882 of 25297 screened records are evaluable (27.2%); 18415 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 18414 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 18022 no_site, 295 chance_only, 68 chance_anchor, 29 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 32 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2340 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 15682 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Pan_HERPES_dsDNA_Terminase_round2`

Pan-HERPES (dsDNA) — Terminase  
Designed 2001, doi:10.1016/S0168-1702(00)00252-5  
**Degeneracy:** 128-fold degenerate (128-fold primers x 1-fold probe); ~7 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1987 | 0 | 2 | 0% |
| 1990 | 3 | 3 | 100% |
| 1991 | 0 | 0 | - |
| 1992 | 1 | 3 | 33% |
| 1993 | 2 | 2 | 100% |
| 1995 | 2 | 3 | 67% |
| 1996 | 1 | 1 | 100% |
| 1997 | 5 | 6 | 83% |
| 1998 | 2 | 5 | 40% |
| 1999 | 6 | 7 | 86% |
| 2000 | 9 | 11 | 82% |
| 2001 | 7 | 7 | 100% |
| 2002 | 4 | 6 | 67% |
| 2003 | 13 | 14 | 93% |
| 2004 | 10 | 12 | 83% |
| 2005 | 6 | 11 | 55% |
| 2006 | 32 | 43 | 74% |
| 2007 | 6 | 9 | 67% |
| 2008 | 7 | 8 | 88% |
| 2009 | 24 | 25 | 96% |
| 2010 | 9 | 9 | 100% |
| 2011 | 67 | 91 | 74% |
| 2012 | 44 | 46 | 96% |
| 2013 | 38 | 40 | 95% |
| 2014 | 64 | 70 | 91% |
| 2015 | 325 | 328 | 99% |
| 2016 | 199 | 216 | 92% |
| 2017 | 208 | 217 | 96% |
| 2018 | 284 | 288 | 99% |
| 2019 | 324 | 395 | 82% |
| 2020 | 70 | 74 | 95% |
| 2021 | 97 | 107 | 91% |
| 2022 | 205 | 207 | 99% |
| 2023 | 237 | 250 | 95% |
| 2024 | 334 | 345 | 97% |
| 2025 | 95 | 149 | 64% |
| 2026 | 99 | 111 | 89% |

*trend over deposit year: rising, z = +2.94, two-sided p = 0.00326 across 36 years and 3121 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 1 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| synthetic construct (32630) | 1 | 1 | 100% |


**Duplication check:** 331 recent records share 30 distinct footprints (11.0 per footprint). This flag does not hold up: with only 30 independent observations (one per footprint) the interval around the 79% detected share is 62%-90%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 3121 of 3810 screened records are evaluable (81.9%); 689 are not. Every share above is taken over the evaluable ones.

Excluded: 4 indeterminate, 685 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 567 no_site, 86 chance_anchor, 30 chance_only, 2 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 423 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 144 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `HANTAVIRUS_ssRNA_S_segment`

**Lineage override:** pooled status was watch.  
HANTAVIRUS (ssRNA) — S segment  
Designed 2013, doi:10.1128/mbio.00598-13  
**Degeneracy:** 31104-fold degenerate (31104-fold primers x 1-fold probe); ~15 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1987 | 1 | 1 | 100% |
| 1990 | 1 | 1 | 100% |
| 1991 | 2 | 2 | 100% |
| 1992 | 1 | 1 | 100% |
| 1993 | 6 | 6 | 100% |
| 1994 | 19 | 19 | 100% |
| 1995 | 25 | 25 | 100% |
| 1996 | 9 | 9 | 100% |
| 1997 | 16 | 17 | 94% |
| 1998 | 19 | 20 | 95% |
| 1999 | 17 | 17 | 100% |
| 2000 | 23 | 23 | 100% |
| 2001 | 55 | 57 | 96% |
| 2002 | 13 | 13 | 100% |
| 2003 | 30 | 30 | 100% |
| 2004 | 21 | 21 | 100% |
| 2005 | 27 | 27 | 100% |
| 2006 | 20 | 22 | 91% |
| 2007 | 99 | 99 | 100% |
| 2008 | 94 | 99 | 95% |
| 2009 | 89 | 93 | 96% |
| 2010 | 63 | 83 | 76% |
| 2011 | 104 | 107 | 97% |
| 2012 | 277 | 278 | 100% |
| 2013 | 191 | 194 | 98% |
| 2014 | 186 | 199 | 93% |
| 2015 | 46 | 47 | 98% |
| 2016 | 211 | 214 | 99% |
| 2017 | 86 | 95 | 91% |
| 2018 | 271 | 285 | 95% |
| 2019 | 193 | 217 | 89% |
| 2020 | 198 | 203 | 98% |
| 2021 | 657 | 660 | 100% |
| 2022 | 122 | 131 | 93% |
| 2023 | 286 | 293 | 98% |
| 2024 | 242 | 252 | 96% |
| 2025 | 194 | 199 | 97% |
| 2026 | 187 | 232 | 81% |

*trend over deposit year: falling, z = -3.37, two-sided p = 0.00074 across 38 years and 4291 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 83 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 443 recent records share 42 distinct footprints (10.5 per footprint). This flag does not hold up: with only 42 independent observations (one per footprint) the interval around the 88% detected share is 75%-95%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 4291 of 16096 screened records are evaluable (26.7%); 11805 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 11804 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 5460 chance_only, 5129 no_site, 1109 truncated, 106 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 4916 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 213 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ALPHAVIRUSES_Togaviridae_ssRNA_NSP4_gene_round2`

**Lineage override:** pooled status was stable.  
ALPHAVIRUSES (Togaviridae  ssRNA) — NSP4 gene  
Designed 2001, doi:10.1016/S0166-0934(01)00306-8  
**Degeneracy:** 256-fold degenerate (256-fold primers x 1-fold probe); each member is ~3.9e-03 of the reaction, ~8 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 0 | - |
| 1983 | 0 | 0 | - |
| 1984 | 0 | 0 | - |
| 1985 | 1 | 1 | 100% |
| 1987 | 2 | 2 | 100% |
| 1988 | 0 | 0 | - |
| 1989 | 1 | 1 | 100% |
| 1990 | 1 | 1 | 100% |
| 1991 | 2 | 2 | 100% |
| 1992 | 1 | 1 | 100% |
| 1993 | 9 | 9 | 100% |
| 1994 | 1 | 1 | 100% |
| 1995 | 0 | 0 | - |
| 1996 | 7 | 7 | 100% |
| 1997 | 5 | 5 | 100% |
| 1998 | 4 | 4 | 100% |
| 1999 | 12 | 12 | 100% |
| 2000 | 3 | 3 | 100% |
| 2001 | 6 | 6 | 100% |
| 2002 | 6 | 12 | 50% |
| 2003 | 2 | 2 | 100% |
| 2004 | 7 | 7 | 100% |
| 2005 | 16 | 20 | 80% |
| 2006 | 15 | 17 | 88% |
| 2007 | 55 | 55 | 100% |
| 2008 | 19 | 19 | 100% |
| 2009 | 88 | 88 | 100% |
| 2010 | 52 | 66 | 79% |
| 2011 | 20 | 20 | 100% |
| 2012 | 41 | 42 | 98% |
| 2013 | 139 | 149 | 93% |
| 2014 | 167 | 169 | 99% |
| 2015 | 91 | 120 | 76% |
| 2016 | 464 | 467 | 99% |
| 2017 | 352 | 358 | 98% |
| 2018 | 113 | 143 | 79% |
| 2019 | 285 | 305 | 93% |
| 2020 | 392 | 424 | 92% |
| 2021 | 211 | 224 | 94% |
| 2022 | 329 | 443 | 74% |
| 2023 | 1254 | 1264 | 99% |
| 2024 | 412 | 421 | 98% |
| 2025 | 457 | 472 | 97% |
| 2026 | 3338 | 3368 | 99% |

*trend over deposit year: rising, z = +8.88, two-sided p = 6.5e-19 across 39 years and 8730 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 339 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 3885 recent records share 19 distinct footprints (204.5 per footprint), of which 5 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 19 independent observations (one per footprint) the interval around the 99% detected share is 81%-100%, which no longer rules out the 90% threshold; with only 19 and 54 independent observations the fall from baseline is -13% to +15%, which no longer excludes zero. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 8730 of 17842 screened records are evaluable (48.9%); 9112 are not. Every share above is taken over the evaluable ones.

Excluded: 295 indeterminate, 8817 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 8767 no_site, 31 chance_anchor, 19 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 198 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1034 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7733 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `AVIPOXVIRUS_dsDNA_4b_core_Baek_2020`

AVIPOXVIRUS (dsDNA) — hummingbird 4b core protein TaqMan MGB (Baek 2020)  
Designed 2020, doi:10.1371/journal.pone.0230701  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1988 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 0 | 1 | 0% |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 1 | 0% |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 2 | 0% |
| 2001 | 0 | 0 | - |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 0 | 18 | 0% |
| 2005 | 0 | 13 | 0% |
| 2006 | 0 | 23 | 0% |
| 2007 | 0 | 2 | 0% |
| 2008 | 0 | 33 | 0% |
| 2009 | 0 | 30 | 0% |
| 2010 | 0 | 4 | 0% |
| 2011 | 0 | 57 | 0% |
| 2012 | 0 | 15 | 0% |
| 2013 | 0 | 145 | 0% |
| 2014 | 1 | 38 | 3% |
| 2015 | 0 | 12 | 0% |
| 2016 | 0 | 28 | 0% |
| 2017 | 0 | 38 | 0% |
| 2018 | 0 | 187 | 0% |
| 2019 | 0 | 58 | 0% |
| 2020 | 1 | 24 | 4% |
| 2021 | 0 | 22 | 0% |
| 2022 | 0 | 82 | 0% |
| 2023 | 1 | 115 | 0.9% |
| 2024 | 0 | 66 | 0% |
| 2025 | 0 | 37 | 0% |
| 2026 | 0 | 32 | 0% |

*trend over deposit year: rising, z = +0.57, two-sided p = 0.567 across 26 years and 1083 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 7 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 78 recent records share 5 distinct footprints (15.6 per footprint), of which 26 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 5 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 1083 of 1727 screened records are evaluable (62.7%); 644 are not. Every share above is taken over the evaluable ones.

Excluded: 644 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 616 no_site, 18 truncated, 10 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 328 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 12 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 604 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Apicoplast_23S_LSU_Large_subunit_Molecular_2005`

Apicoplast — 23S LSU (Large subunit)  
Designed 2000, doi:10.1099/00221287-146-2-315  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1997 | 0 | 1 | 0% |
| 1998 | 0 | 1 | 0% |
| 1999 | 0 | 0 | - |
| 2001 | 0 | 3 | 0% |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 2 | 0% |
| 2004 | 0 | 0 | - |
| 2006 | 0 | 1 | 0% |
| 2007 | 0 | 0 | - |
| 2009 | 0 | 12 | 0% |
| 2010 | 0 | 1 | 0% |
| 2011 | 0 | 0 | - |
| 2012 | 0 | 1 | 0% |
| 2013 | 0 | 2 | 0% |
| 2014 | 0 | 2 | 0% |
| 2015 | 0 | 2 | 0% |
| 2016 | 0 | 13 | 0% |
| 2017 | 0 | 1 | 0% |
| 2018 | 0 | 2 | 0% |
| 2019 | 0 | 24 | 0% |
| 2020 | 0 | 3 | 0% |
| 2021 | 0 | 1 | 0% |
| 2022 | 0 | 1 | 0% |
| 2023 | 0 | 4 | 0% |
| 2024 | 0 | 8 | 0% |
| 2025 | 0 | 23 | 0% |
| 2026 | 0 | 4 | 0% |

*trend over deposit year: not tested (fewer than 3 years with evaluable records, or no variation)*

**Duplication check:** 27 recent records share 5 distinct footprints (5.4 per footprint), of which 27 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 5 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 112 of 329 screened records are evaluable (34.0%); 217 are not. Every share above is taken over the evaluable ones.

Excluded: 217 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 199 no_site, 15 chance_anchor, 3 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 111 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 46 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 153 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Helicobacter_16S_Conley_2021`

Helicobacter — 16S rRNA qPCR (Helico New F/R + PROBE1)  
Designed 2021, doi:10.1371/journal.pone.0247010  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1992 | 0 | 11 | 0% |
| 1993 | 0 | 31 | 0% |
| 1994 | 0 | 5 | 0% |
| 1995 | 0 | 2 | 0% |
| 1996 | 0 | 8 | 0% |
| 1997 | 0 | 18 | 0% |
| 1998 | 0 | 10 | 0% |
| 1999 | 0 | 20 | 0% |
| 2000 | 0 | 26 | 0% |
| 2001 | 0 | 34 | 0% |
| 2002 | 0 | 46 | 0% |
| 2003 | 0 | 25 | 0% |
| 2004 | 0 | 59 | 0% |
| 2005 | 0 | 64 | 0% |
| 2006 | 0 | 21 | 0% |
| 2007 | 0 | 22 | 0% |
| 2008 | 0 | 48 | 0% |
| 2009 | 0 | 24 | 0% |
| 2010 | 0 | 202 | 0% |
| 2011 | 0 | 22 | 0% |
| 2012 | 0 | 14 | 0% |
| 2013 | 0 | 52 | 0% |
| 2014 | 0 | 36 | 0% |
| 2015 | 0 | 16 | 0% |
| 2016 | 0 | 19 | 0% |
| 2017 | 0 | 21 | 0% |
| 2018 | 0 | 12 | 0% |
| 2019 | 0 | 23 | 0% |
| 2020 | 0 | 16 | 0% |
| 2021 | 0 | 85 | 0% |
| 2022 | 0 | 44 | 0% |
| 2023 | 0 | 33 | 0% |
| 2024 | 0 | 14 | 0% |
| 2025 | 0 | 20 | 0% |
| 2026 | 0 | 52 | 0% |

*trend over deposit year: not tested (fewer than 3 years with evaluable records, or no variation)*

**Patent records:** 1 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 75 recent records share 6 distinct footprints (12.5 per footprint), of which 57 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 6 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 1155 of 3025 screened records are evaluable (38.2%); 1870 are not. Every share above is taken over the evaluable ones.

Excluded: 1870 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1110 no_site, 616 truncated, 141 no_pair, 3 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 360 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1110 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1`

POLYOMAVIRUS (dsDNA) — PREDICT VP1  
Designed 2005, doi:10.1128/JVI.79.6.3883-3887.2005  
**Degeneracy:** 128-fold degenerate (128-fold primers x 1-fold probe); ~7 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 3 | 0% |
| 1983 | 0 | 0 | - |
| 1984 | 0 | 0 | - |
| 1985 | 0 | 3 | 0% |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 1 | 0% |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 1 | 0% |
| 1990 | 0 | 1 | 0% |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 0 | 9 | 0% |
| 1994 | 0 | 1 | 0% |
| 1995 | 0 | 2 | 0% |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 1 | 0% |
| 1998 | 0 | 0 | - |
| 1999 | 0 | 7 | 0% |
| 2000 | 0 | 7 | 0% |
| 2001 | 0 | 7 | 0% |
| 2002 | 0 | 1 | 0% |
| 2003 | 0 | 7 | 0% |
| 2004 | 0 | 16 | 0% |
| 2005 | 0 | 10 | 0% |
| 2006 | 0 | 79 | 0% |
| 2007 | 0 | 97 | 0% |
| 2008 | 0 | 74 | 0% |
| 2009 | 0 | 41 | 0% |
| 2010 | 0 | 37 | 0% |
| 2011 | 0 | 21 | 0% |
| 2012 | 3 | 53 | 6% |
| 2013 | 0 | 28 | 0% |
| 2014 | 0 | 31 | 0% |
| 2015 | 0 | 73 | 0% |
| 2016 | 0 | 26 | 0% |
| 2017 | 0 | 41 | 0% |
| 2018 | 1 | 38 | 3% |
| 2019 | 0 | 259 | 0% |
| 2020 | 0 | 43 | 0% |
| 2021 | 0 | 63 | 0% |
| 2022 | 1 | 144 | 0.7% |
| 2023 | 0 | 201 | 0% |
| 2024 | 0 | 360 | 0% |
| 2025 | 0 | 349 | 0% |
| 2026 | 0 | 230 | 0% |

*trend over deposit year: falling, z = -1.22, two-sided p = 0.223 across 37 years and 2365 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Per species** (product size names the species here, 829-1137 bp, so the share above pools readouts that mean different things; Oct 2024 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Betapolyomavirus hominis (1891762) | - | 0 | 548 | 0% |
| Polyomaviridae sp. (2202645) | - | 0 | 20 | 0% |
| Betapolyomavirus tertihominis (1891764) | - | 0 | 7 | 0% |
| Deltapolyomavirus decihominis (1208309) | - | 0 | 6 | 0% |
| Epsilonpolyomavirus bovis (1891754) | - | 0 | 4 | 0% |
| Alphapolyomavirus sp. (2809142) | - | 0 | 3 | 0% |
| Gammapolyomavirus avis (1891747) | - | 0 | 3 | 0% |
| Polyomavirus sp. (36362) | - | 0 | 2 | 0% |
| Alphapolyomavirus muris (1891730) | - | 0 | 1 | 0% |
| Alphapolyomavirus sominutus (2955305) | - | 0 | 1 | 0% |
| Betapolyomavirus secumuris (1891770) | - | 0 | 1 | 0% |

**Out of scope:** 7 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| synthetic construct (32630) | 0 | 3 | 0% |
| Mirounga angustirostris polyomavirus 1 (3902555) | 0 | 2 | 0% |
| Homo sapiens (9606) | 0 | 1 | 0% |
| Cricetulus griseus (10029) | 0 | 1 | 0% |


**Patent records:** 372 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 650 recent records share 36 distinct footprints (18.1 per footprint), of which 54 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 36 independent observations (one per footprint) the interval around the 0% detected share is 0%-10%, and counting each footprint once, 0 of 36 footprints amplify (0%; interval 0%-10%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 2365 of 14158 screened records are evaluable (16.7%); 11793 are not. Every share above is taken over the evaluable ones.

Excluded: 11793 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 8492 no_site, 1970 truncated, 1323 chance_anchor, 8 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 299 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 44 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 8448 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009`

RETROVIRUS (RNA) — polymerase (SIV)  
Designed 2009, doi:10.1128/JVI.02311-08  
**Degeneracy:** 144-fold degenerate (144-fold primers x 1-fold probe); each member is ~6.9e-03 of the reaction, ~7 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1990 | 0 | 1 | 0% |
| 1991 | 0 | 2 | 0% |
| 1992 | 0 | 2 | 0% |
| 1993 | 0 | 12 | 0% |
| 1994 | 0 | 1 | 0% |
| 1995 | 0 | 1 | 0% |
| 1996 | 1 | 2 | 50% |
| 1997 | 0 | 2 | 0% |
| 1998 | 0 | 3 | 0% |
| 1999 | 2 | 3 | 67% |
| 2001 | 0 | 8 | 0% |
| 2002 | 1 | 7 | 14% |
| 2003 | 1 | 10 | 10% |
| 2004 | 0 | 28 | 0% |
| 2005 | 0 | 14 | 0% |
| 2006 | 3 | 20 | 15% |
| 2007 | 0 | 8 | 0% |
| 2008 | 2 | 9 | 22% |
| 2009 | 5 | 1244 | 0.4% |
| 2010 | 0 | 863 | 0% |
| 2011 | 3 | 7 | 43% |
| 2012 | 2 | 11 | 18% |
| 2013 | 1 | 39 | 3% |
| 2014 | 0 | 7 | 0% |
| 2015 | 9 | 10 | 90% |
| 2016 | 0 | 87 | 0% |
| 2017 | 126 | 173 | 73% |
| 2018 | 0 | 1 | 0% |
| 2019 | 0 | 384 | 0% |
| 2020 | 0 | 155 | 0% |
| 2021 | 1 | 99 | 1% |
| 2022 | 1 | 3 | 33% |
| 2023 | 0 | 3 | 0% |
| 2024 | 0 | 1854 | 0% |
| 2025 | 0 | 206 | 0% |
| 2026 | 0 | 20 | 0% |

*trend over deposit year: falling, z = -1.86, two-sided p = 0.0623 across 36 years and 5299 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 226 recent records share 3 distinct footprints (75.3 per footprint). This flag does not hold up: only 3 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 5299 of 8252 screened records are evaluable (64.2%); 2953 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 2952 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1454 truncated, 1423 no_site, 74 chance_anchor, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 269 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 6 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1417 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ORTHOBUNYAVIRUS_ssRNA_M_segment_internal_Briese_2007`

ORTHOBUNYAVIRUS (ssRNA) — M segment internal, BUN-M-IXf/XIIr (Briese 2007)  
Designed 2007, doi:10.1007/s00705-007-1069-z  
**Degeneracy:** 4096-fold degenerate (4096-fold primers x 1-fold probe); each member is ~2.4e-04 of the reaction, ~12 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1989 | 1 | 1 | 100% |
| 1993 | 1 | 1 | 100% |
| 1995 | 0 | 2 | 0% |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 2 | 4 | 50% |
| 1999 | 1 | 1 | 100% |
| 2000 | 7 | 7 | 100% |
| 2001 | 4 | 4 | 100% |
| 2002 | 0 | 2 | 0% |
| 2003 | 4 | 6 | 67% |
| 2004 | 1 | 2 | 50% |
| 2005 | 0 | 0 | - |
| 2006 | 2 | 6 | 33% |
| 2007 | 0 | 5 | 0% |
| 2008 | 0 | 0 | - |
| 2009 | 2 | 3 | 67% |
| 2010 | 0 | 4 | 0% |
| 2011 | 0 | 0 | - |
| 2012 | 0 | 0 | - |
| 2013 | 0 | 2 | 0% |
| 2014 | 5 | 21 | 24% |
| 2015 | 8 | 23 | 35% |
| 2016 | 16 | 42 | 38% |
| 2017 | 5 | 30 | 17% |
| 2018 | 3 | 10 | 30% |
| 2019 | 1 | 27 | 4% |
| 2020 | 2 | 3 | 67% |
| 2021 | 8 | 10 | 80% |
| 2022 | 6 | 12 | 50% |
| 2023 | 2 | 20 | 10% |
| 2024 | 0 | 19 | 0% |
| 2025 | 0 | 104 | 0% |
| 2026 | 1 | 187 | 0.5% |

*trend over deposit year: falling, z = -11.29, two-sided p = 1.41e-29 across 28 years and 558 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 296 recent records share 11 distinct footprints (26.9 per footprint), of which 7 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 11 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 558 of 2083 screened records are evaluable (26.8%); 1525 are not. Every share above is taken over the evaluable ones.

Excluded: 1525 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1296 no_site, 179 chance_only, 47 chance_anchor, 2 no_pair, 1 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 27 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 887 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 409 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round2`

POLYOMAVIRUS (dsDNA) — PREDICT VP1  
Designed 2005, doi:10.1128/JVI.79.6.3883-3887.2005  
**Degeneracy:** 1536-fold degenerate (1536-fold primers x 1-fold probe); each member is ~6.5e-04 of the reaction, ~11 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 1 | 4 | 25% |
| 1983 | 0 | 0 | - |
| 1984 | 0 | 0 | - |
| 1985 | 2 | 3 | 67% |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 1 | 0% |
| 1988 | 2 | 2 | 100% |
| 1989 | 0 | 2 | 0% |
| 1990 | 1 | 2 | 50% |
| 1991 | 0 | 4 | 0% |
| 1992 | 0 | 0 | - |
| 1993 | 4 | 30 | 13% |
| 1994 | 0 | 5 | 0% |
| 1995 | 2 | 20 | 10% |
| 1996 | 0 | 4 | 0% |
| 1997 | 0 | 262 | 0% |
| 1998 | 1 | 19 | 5% |
| 1999 | 1 | 64 | 2% |
| 2000 | 10 | 269 | 4% |
| 2001 | 1 | 254 | 0.4% |
| 2002 | 0 | 471 | 0% |
| 2003 | 4 | 85 | 5% |
| 2004 | 7 | 170 | 4% |
| 2005 | 0 | 118 | 0% |
| 2006 | 0 | 152 | 0% |
| 2007 | 1 | 98 | 1% |
| 2008 | 3 | 112 | 3% |
| 2009 | 13 | 116 | 11% |
| 2010 | 4 | 60 | 7% |
| 2011 | 5 | 761 | 0.7% |
| 2012 | 17 | 241 | 7% |
| 2013 | 7 | 103 | 7% |
| 2014 | 3 | 85 | 4% |
| 2015 | 33 | 145 | 23% |
| 2016 | 11 | 83 | 13% |
| 2017 | 10 | 81 | 12% |
| 2018 | 52 | 328 | 16% |
| 2019 | 192 | 544 | 35% |
| 2020 | 33 | 68 | 49% |
| 2021 | 9 | 123 | 7% |
| 2022 | 9 | 191 | 5% |
| 2023 | 28 | 267 | 10% |
| 2024 | 36 | 386 | 9% |
| 2025 | 3 | 436 | 0.7% |
| 2026 | 14 | 433 | 3% |

*trend over deposit year: rising, z = +10.59, two-sided p = 3.37e-26 across 41 years and 6602 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 7 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| synthetic construct (32630) | 0 | 3 | 0% |
| Mirounga angustirostris polyomavirus 1 (3902555) | 0 | 2 | 0% |
| Homo sapiens (9606) | 0 | 1 | 0% |
| Cricetulus griseus (10029) | 0 | 1 | 0% |


**Patent records:** 372 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 944 recent records share 46 distinct footprints (20.5 per footprint), of which 35 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 46 independent observations (one per footprint) the interval around the 2% detected share is 0.3%-11%, and counting each footprint once, 9 of 46 footprints amplify (20%; interval 11%-33%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 6602 of 14158 screened records are evaluable (46.6%); 7556 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 7555 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 7122 no_site, 430 truncated, 3 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 179 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7122 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `POLYOMAVIRUS_dsDNA_VP1_Johne_2005`

POLYOMAVIRUS (dsDNA) — VP1  
Designed 2005, doi:10.1128/JVI.79.6.3883-3887.2005  
**Degeneracy:** 1536-fold degenerate (1536-fold primers x 1-fold probe); each member is ~6.5e-04 of the reaction, ~11 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 1 | 4 | 25% |
| 1983 | 0 | 0 | - |
| 1984 | 0 | 0 | - |
| 1985 | 2 | 3 | 67% |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 1 | 0% |
| 1988 | 2 | 2 | 100% |
| 1989 | 0 | 2 | 0% |
| 1990 | 1 | 2 | 50% |
| 1991 | 0 | 4 | 0% |
| 1992 | 0 | 0 | - |
| 1993 | 4 | 30 | 13% |
| 1994 | 0 | 5 | 0% |
| 1995 | 2 | 20 | 10% |
| 1996 | 0 | 4 | 0% |
| 1997 | 0 | 262 | 0% |
| 1998 | 1 | 19 | 5% |
| 1999 | 1 | 64 | 2% |
| 2000 | 10 | 269 | 4% |
| 2001 | 1 | 254 | 0.4% |
| 2002 | 0 | 471 | 0% |
| 2003 | 4 | 85 | 5% |
| 2004 | 7 | 170 | 4% |
| 2005 | 0 | 118 | 0% |
| 2006 | 0 | 152 | 0% |
| 2007 | 1 | 98 | 1% |
| 2008 | 3 | 112 | 3% |
| 2009 | 13 | 116 | 11% |
| 2010 | 4 | 60 | 7% |
| 2011 | 5 | 761 | 0.7% |
| 2012 | 17 | 241 | 7% |
| 2013 | 7 | 103 | 7% |
| 2014 | 3 | 85 | 4% |
| 2015 | 33 | 145 | 23% |
| 2016 | 11 | 83 | 13% |
| 2017 | 10 | 81 | 12% |
| 2018 | 52 | 328 | 16% |
| 2019 | 192 | 544 | 35% |
| 2020 | 33 | 68 | 49% |
| 2021 | 9 | 123 | 7% |
| 2022 | 9 | 191 | 5% |
| 2023 | 28 | 267 | 10% |
| 2024 | 36 | 386 | 9% |
| 2025 | 3 | 436 | 0.7% |
| 2026 | 14 | 433 | 3% |

*trend over deposit year: rising, z = +10.59, two-sided p = 3.37e-26 across 41 years and 6602 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 7 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| synthetic construct (32630) | 0 | 3 | 0% |
| Mirounga angustirostris polyomavirus 1 (3902555) | 0 | 2 | 0% |
| Homo sapiens (9606) | 0 | 1 | 0% |
| Cricetulus griseus (10029) | 0 | 1 | 0% |


**Patent records:** 372 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 944 recent records share 46 distinct footprints (20.5 per footprint), of which 35 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 46 independent observations (one per footprint) the interval around the 2% detected share is 0.3%-11%, and counting each footprint once, 9 of 46 footprints amplify (20%; interval 11%-33%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 6602 of 14158 screened records are evaluable (46.6%); 7556 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 7555 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 7122 no_site, 430 truncated, 3 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 179 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7122 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `POXVIRUSES_dsDNA_Polymerase`

POXVIRUSES (dsDNA) — Polymerase  
Designed 2006, doi:10.1007/s00705-005-0679-6  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1984 | 0 | 0 | - |
| 1985 | 0 | 0 | - |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 0 | - |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 1 | 0% |
| 1991 | 0 | 1 | 0% |
| 1992 | 0 | 0 | - |
| 1993 | 0 | 2 | 0% |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 1 | 0% |
| 1998 | 0 | 2 | 0% |
| 1999 | 0 | 6 | 0% |
| 2000 | 0 | 3 | 0% |
| 2001 | 2 | 6 | 33% |
| 2002 | 11 | 17 | 65% |
| 2003 | 4 | 8 | 50% |
| 2004 | 2 | 8 | 25% |
| 2005 | 6 | 23 | 26% |
| 2006 | 0 | 21 | 0% |
| 2007 | 0 | 6 | 0% |
| 2008 | 0 | 5 | 0% |
| 2009 | 1 | 14 | 7% |
| 2010 | 0 | 19 | 0% |
| 2011 | 1 | 15 | 7% |
| 2012 | 0 | 37 | 0% |
| 2013 | 14 | 71 | 20% |
| 2014 | 1 | 72 | 1% |
| 2015 | 0 | 26 | 0% |
| 2016 | 6 | 21 | 29% |
| 2017 | 5 | 77 | 6% |
| 2018 | 8 | 66 | 12% |
| 2019 | 16 | 104 | 15% |
| 2020 | 15 | 69 | 22% |
| 2021 | 18 | 46 | 39% |
| 2022 | 31 | 3491 | 0.9% |
| 2023 | 64 | 3185 | 2% |
| 2024 | 45 | 2152 | 2% |
| 2025 | 98 | 2244 | 4% |
| 2026 | 99 | 2669 | 4% |

*trend over deposit year: falling, z = -9.73, two-sided p = 2.2e-22 across 33 years and 14488 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 735 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 5142 recent records share 17 distinct footprints (302.5 per footprint), of which 2 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 17 independent observations (one per footprint) the interval around the 4% detected share is 0.5%-25%, and counting each footprint once, 4 of 17 footprints amplify (24%; interval 10%-47%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 14488 of 28586 screened records are evaluable (50.7%); 14098 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 14097 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 13750 no_site, 247 chance_anchor, 97 truncated, 3 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 24 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 496 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 13254 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Snake_nidovirus_PP1b_Uccellini_2014_2`

NIDOVIRUS (ssRNA)-SNAKE — PP1b  
Designed 2014, doi:10.1186/1743-422X-11-144  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 2014 | 3 | 3 | 100% |
| 2016 | 0 | 3 | 0% |
| 2017 | 0 | 3 | 0% |
| 2018 | 1 | 3 | 33% |
| 2019 | 1 | 17 | 6% |
| 2020 | 0 | 4 | 0% |
| 2021 | 0 | 0 | - |
| 2023 | 0 | 4 | 0% |
| 2024 | 0 | 16 | 0% |
| 2025 | 0 | 4 | 0% |
| 2026 | 1 | 3 | 33% |

*trend over deposit year: falling, z = -2.61, two-sided p = 0.00913 across 10 years and 60 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 11 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 23 recent records share 14 distinct footprints (1.6 per footprint), of which 4 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 14 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 60 of 279 screened records are evaluable (21.5%); 219 are not. Every share above is taken over the evaluable ones.

Excluded: 219 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 151 no_site, 56 truncated, 12 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 4 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 8 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 143 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ORTHOBUNYAVIRUS_ssRNA_M_segment`

ORTHOBUNYAVIRUS (ssRNA) — M segment (PREDICT P-023)  
Designed 2007, doi:10.1007/s00705-007-1069-z  
**Degeneracy:** 192-fold degenerate (192-fold primers x 1-fold probe); each member is ~5.2e-03 of the reaction, ~8 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1989 | 1 | 1 | 100% |
| 1993 | 1 | 2 | 50% |
| 1995 | 2 | 2 | 100% |
| 1996 | 0 | 7 | 0% |
| 1997 | 0 | 0 | - |
| 1998 | 4 | 4 | 100% |
| 1999 | 1 | 1 | 100% |
| 2000 | 7 | 7 | 100% |
| 2001 | 4 | 5 | 80% |
| 2002 | 2 | 3 | 67% |
| 2003 | 4 | 6 | 67% |
| 2004 | 0 | 5 | 0% |
| 2005 | 0 | 0 | - |
| 2006 | 0 | 0 | - |
| 2007 | 0 | 5 | 0% |
| 2008 | 0 | 0 | - |
| 2009 | 2 | 6 | 33% |
| 2010 | 0 | 4 | 0% |
| 2011 | 0 | 0 | - |
| 2012 | 0 | 2 | 0% |
| 2013 | 1 | 5 | 20% |
| 2014 | 4 | 29 | 14% |
| 2015 | 2 | 20 | 10% |
| 2016 | 4 | 21 | 19% |
| 2017 | 12 | 29 | 41% |
| 2018 | 3 | 13 | 23% |
| 2019 | 1 | 10 | 10% |
| 2020 | 1 | 7 | 14% |
| 2021 | 3 | 11 | 27% |
| 2022 | 0 | 4 | 0% |
| 2023 | 0 | 6 | 0% |
| 2024 | 0 | 9 | 0% |
| 2025 | 0 | 2 | 0% |
| 2026 | 1 | 1 | 100% |

*trend over deposit year: falling, z = -4.94, two-sided p = 8e-07 across 29 years and 227 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Per species** (product size names the species here, 201-1090 bp, so the share above pools readouts that mean different things; Oct 2022 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Orthobunyavirus oropoucheense (3052429) | - | 0 | 10 | 0% |
| Orthobunyavirus bunyamweraense (3052381) | - | 0 | 2 | 0% |
| Orthobunyavirus kowanyamaense (3060477) | - | 0 | 2 | 0% |
| Orthobunyavirus manzanillaense (3052416) | - | 0 | 2 | 0% |
| Orthobunyavirus cacheense (3052385) | - | 1 | 1 | 100% |
| Orthobunyavirus lacrosseense (3052409) | - | 0 | 1 | 0% |
| Orthobunyavirus schmallenbergense (3052437) | - | 0 | 1 | 0% |
| Orthobunyavirus trinitiense (3052451) | - | 0 | 1 | 0% |

**Duplication check:** 20 recent records share 14 distinct footprints (1.4 per footprint). This flag does not hold up: only 14 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 227 of 2083 screened records are evaluable (10.9%); 1856 are not. Every share above is taken over the evaluable ones.

Excluded: 1856 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1428 chance_only, 408 no_site, 20 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 408 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 0 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ORTHOBUNYAVIRUS_ssRNA_L_segment_Briese_2007`

ORTHOBUNYAVIRUS (ssRNA) — L segment, BUNL-5n/BUNL650R (Briese 2007)  
Designed 2007, doi:10.1007/s00705-007-1069-z  
**Degeneracy:** 64-fold degenerate (64-fold primers x 1-fold probe); ~6 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1990 | 0 | 0 | - |
| 1991 | 1 | 1 | 100% |
| 1994 | 1 | 1 | 100% |
| 2001 | 0 | 0 | - |
| 2002 | 1 | 1 | 100% |
| 2003 | 0 | 0 | - |
| 2004 | 0 | 0 | - |
| 2006 | 0 | 1 | 0% |
| 2007 | 0 | 1 | 0% |
| 2008 | 0 | 6 | 0% |
| 2009 | 0 | 0 | - |
| 2010 | 3 | 6 | 50% |
| 2011 | 14 | 16 | 88% |
| 2012 | 0 | 7 | 0% |
| 2013 | 1 | 4 | 25% |
| 2014 | 10 | 19 | 53% |
| 2015 | 1 | 16 | 6% |
| 2016 | 1 | 30 | 3% |
| 2017 | 13 | 15 | 87% |
| 2018 | 2 | 12 | 17% |
| 2019 | 0 | 7 | 0% |
| 2020 | 0 | 15 | 0% |
| 2021 | 1 | 10 | 10% |
| 2022 | 3 | 7 | 43% |
| 2023 | 1 | 6 | 17% |
| 2024 | 0 | 6 | 0% |
| 2025 | 0 | 4 | 0% |
| 2026 | 0 | 1 | 0% |

*trend over deposit year: falling, z = -4.20, two-sided p = 2.63e-05 across 23 years and 192 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 23 recent records share 13 distinct footprints (1.8 per footprint), of which 5 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 13 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 192 of 2143 screened records are evaluable (9.0%); 1951 are not. Every share above is taken over the evaluable ones.

Excluded: 1951 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1756 no_site, 112 truncated, 75 chance_anchor, 8 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 34 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1753 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 3 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ARENAVIRUS_ssRNA_S_gene`

ARENAVIRUS (ssRNA) — S gene  
Designed 1997, doi:10.1016/S0168-1702(97)01458-5  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 2 | 2 | 100% |
| 1986 | 1 | 1 | 100% |
| 1987 | 1 | 1 | 100% |
| 1989 | 7 | 8 | 88% |
| 1990 | 1 | 3 | 33% |
| 1991 | 0 | 0 | - |
| 1992 | 1 | 1 | 100% |
| 1993 | 4 | 7 | 57% |
| 1995 | 0 | 1 | 0% |
| 1996 | 2 | 2 | 100% |
| 1997 | 1 | 4 | 25% |
| 1998 | 4 | 7 | 57% |
| 1999 | 0 | 12 | 0% |
| 2000 | 1 | 1 | 100% |
| 2001 | 1 | 3 | 33% |
| 2002 | 12 | 18 | 67% |
| 2003 | 3 | 10 | 30% |
| 2004 | 13 | 44 | 30% |
| 2005 | 2 | 3 | 67% |
| 2006 | 9 | 22 | 41% |
| 2007 | 9 | 22 | 41% |
| 2008 | 13 | 43 | 30% |
| 2009 | 30 | 63 | 48% |
| 2010 | 6 | 25 | 24% |
| 2011 | 15 | 45 | 33% |
| 2012 | 33 | 64 | 52% |
| 2013 | 3 | 10 | 30% |
| 2014 | 70 | 150 | 47% |
| 2015 | 14 | 28 | 50% |
| 2016 | 15 | 28 | 54% |
| 2017 | 19 | 46 | 41% |
| 2018 | 7 | 70 | 10% |
| 2019 | 14 | 38 | 37% |
| 2020 | 9 | 27 | 33% |
| 2021 | 6 | 23 | 26% |
| 2022 | 20 | 54 | 37% |
| 2023 | 29 | 79 | 37% |
| 2024 | 11 | 26 | 42% |
| 2025 | 3 | 33 | 9% |
| 2026 | 6 | 34 | 18% |

*trend over deposit year: falling, z = -4.09, two-sided p = 4.23e-05 across 39 years and 1058 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 473 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| unidentified Reptarenavirus (1654823) | 0 | 210 | 0% |
| taxid 1672385 | 0 | 15 | 0% |
| taxid 2447921 | 0 | 12 | 0% |
| taxid 1382279 | 0 | 12 | 0% |
| taxid 2447931 | 0 | 9 | 0% |
| Aurora borealis virus (1672381) | 0 | 9 | 0% |
| Aurora borealis virus 3 (2447924) | 0 | 9 | 0% |
| taxid 2116467 | 0 | 9 | 0% |
| taxid 1303019 | 0 | 9 | 0% |
| Alethinophid 3 reptarenavirus (1653399) | 0 | 8 | 0% |
| _+57 more taxa_ | | | |


**Patent records:** 226 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 70 recent records share 39 distinct footprints (1.8 per footprint), of which 39 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 39 independent observations (one per footprint) the interval around the 14% detected share is 7%-28%, and counting each footprint once, 10 of 39 footprints amplify (26%; interval 15%-41%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 1058 of 5755 screened records are evaluable (18.4%); 4697 are not. Every share above is taken over the evaluable ones.

Excluded: 3 indeterminate, 4694 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3948 no_site, 367 chance_anchor, 320 truncated, 46 no_pair, 13 chance_only. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 405 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2572 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1376 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Snake_nidovirus_PP1b_Uccellini_2014_3`

NIDOVIRUS (ssRNA)-SNAKE — PP1b  
Designed 2014, doi:10.1186/1743-422X-11-144  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 2014 | 2 | 2 | 100% |
| 2016 | 0 | 1 | 0% |
| 2017 | 2 | 2 | 100% |
| 2018 | 1 | 2 | 50% |
| 2019 | 4 | 13 | 31% |
| 2020 | 0 | 3 | 0% |
| 2021 | 0 | 1 | 0% |
| 2023 | 0 | 3 | 0% |
| 2024 | 2 | 12 | 17% |
| 2025 | 0 | 3 | 0% |
| 2026 | 1 | 2 | 50% |

*trend over deposit year: falling, z = -2.40, two-sided p = 0.0165 across 11 years and 44 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 11 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 17 recent records share 13 distinct footprints (1.3 per footprint). This flag does not hold up: only 13 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 44 of 279 screened records are evaluable (15.8%); 235 are not. Every share above is taken over the evaluable ones.

Excluded: 235 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 183 no_site, 50 chance_anchor, 2 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 38 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 145 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Pan_coccidia_SSU_rDNA_negative_contro_Garner_2006`

Pan-coccidia — SSU rDNA (negative control works) use as primary screen  
Designed 2006, doi:10.1354/vp.43-3-311  
**Degeneracy:** 128-fold degenerate (128-fold primers x 1-fold probe); ~7 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1989 | 0 | 1 | 0% |
| 1991 | 0 | 0 | - |
| 1992 | 4 | 8 | 50% |
| 1993 | 7 | 16 | 44% |
| 1994 | 7 | 15 | 47% |
| 1995 | 3 | 4 | 75% |
| 1996 | 3 | 6 | 50% |
| 1997 | 17 | 35 | 49% |
| 1998 | 22 | 35 | 63% |
| 1999 | 23 | 64 | 36% |
| 2000 | 2 | 16 | 12% |
| 2001 | 44 | 67 | 66% |
| 2002 | 13 | 32 | 41% |
| 2003 | 9 | 64 | 14% |
| 2004 | 25 | 113 | 22% |
| 2005 | 66 | 185 | 36% |
| 2006 | 31 | 78 | 40% |
| 2007 | 72 | 321 | 22% |
| 2008 | 121 | 399 | 30% |
| 2009 | 41 | 139 | 29% |
| 2010 | 85 | 303 | 28% |
| 2011 | 147 | 268 | 55% |
| 2012 | 134 | 317 | 42% |
| 2013 | 279 | 498 | 56% |
| 2014 | 201 | 495 | 41% |
| 2015 | 226 | 367 | 62% |
| 2016 | 288 | 631 | 46% |
| 2017 | 381 | 698 | 55% |
| 2018 | 326 | 708 | 46% |
| 2019 | 207 | 819 | 25% |
| 2020 | 260 | 697 | 37% |
| 2021 | 152 | 758 | 20% |
| 2022 | 105 | 428 | 25% |
| 2023 | 141 | 803 | 18% |
| 2024 | 234 | 975 | 24% |
| 2025 | 199 | 930 | 21% |
| 2026 | 167 | 546 | 31% |

*trend over deposit year: falling, z = -12.85, two-sided p = 9.16e-38 across 36 years and 11839 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 1653 recent records share 133 distinct footprints (12.4 per footprint), of which 1212 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 133 independent observations (one per footprint) the interval around the 24% detected share is 17%-32%, and counting each footprint once, 17 of 133 footprints amplify (13%; interval 8%-20%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 11839 of 56412 screened records are evaluable (21.0%); 44573 are not. Every share above is taken over the evaluable ones.

Excluded: 44573 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 30867 no_site, 12840 truncated, 494 no_pair, 372 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 7366 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1443 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 29424 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010_round1`

ORTHOREOVIRUS (dsRNA) — RNA polymerase  
Designed 2010, doi:10.1177/104063871002200106  
**Degeneracy:** 331776-fold degenerate (331776-fold primers x 1-fold probe); ~18 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 0 | - |
| 1987 | 0 | 0 | - |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 1 | 1 | 100% |
| 1994 | 2 | 2 | 100% |
| 1995 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 1 | 1 | 100% |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 0 | 0 | - |
| 2005 | 0 | 0 | - |
| 2006 | 2 | 2 | 100% |
| 2007 | 1 | 1 | 100% |
| 2008 | 0 | 0 | - |
| 2009 | 3 | 6 | 50% |
| 2010 | 5 | 7 | 71% |
| 2011 | 4 | 8 | 50% |
| 2012 | 10 | 12 | 83% |
| 2013 | 4 | 15 | 27% |
| 2014 | 15 | 33 | 45% |
| 2015 | 18 | 32 | 56% |
| 2016 | 9 | 24 | 38% |
| 2017 | 10 | 18 | 56% |
| 2018 | 11 | 33 | 33% |
| 2019 | 12 | 31 | 39% |
| 2020 | 28 | 152 | 18% |
| 2021 | 18 | 35 | 51% |
| 2022 | 32 | 46 | 70% |
| 2023 | 49 | 74 | 66% |
| 2024 | 81 | 99 | 82% |
| 2025 | 70 | 319 | 22% |
| 2026 | 13 | 34 | 38% |

*trend over deposit year: falling, z = -3.38, two-sided p = 0.00073 across 23 years and 985 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 52 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 358 recent records share 33 distinct footprints (10.8 per footprint). Both reductions leave the flag in place: with only 33 independent observations (one per footprint) the interval around the 24% detected share is 13%-41%, and counting each footprint once, 17 of 33 footprints amplify (52%; interval 35%-67%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 985 of 14479 screened records are evaluable (6.8%); 13494 are not. Every share above is taken over the evaluable ones.

Excluded: 13494 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 13170 no_site, 265 chance_anchor, 59 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 7610 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 5560 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `DWVA_polyprotein_Rossi_2024`

DEFORMED WING VIRUS A — polyprotein gene RT-qPCR, MGB probe (Rossi 2024)  
Designed 2024, doi:10.3390/microorganisms12061105  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 2022 | 3 | 6 | 50% |
| 2023 | 27 | 32 | 84% |
| 2024 | 2 | 2 | 100% |
| 2025 | 4 | 21 | 19% |
| 2026 | 3 | 7 | 43% |

*trend over deposit year: falling, z = -3.54, two-sided p = 0.0004 across 5 years and 68 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 28 recent records share 13 distinct footprints (2.2 per footprint). This flag does not hold up: only 13 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 68 of 223 screened records are evaluable (30.5%); 155 are not. Every share above is taken over the evaluable ones.

Excluded: 155 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 140 no_site, 15 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 2 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 138 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ORTHOBUNYAVIRUS_ssRNA_S_segment`

ORTHOBUNYAVIRUS (ssRNA) — S segment (PREDICT P-022)  
Designed 2007, doi:10.1007/s00705-007-1069-z  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1989 | 0 | 1 | 0% |
| 1993 | 2 | 3 | 67% |
| 1995 | 0 | 2 | 0% |
| 1996 | 7 | 7 | 100% |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 3 | 0% |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 0 | 0 | - |
| 2002 | 2 | 9 | 22% |
| 2003 | 0 | 1 | 0% |
| 2004 | 2 | 3 | 67% |
| 2005 | 0 | 0 | - |
| 2006 | 0 | 0 | - |
| 2007 | 2 | 12 | 17% |
| 2008 | 0 | 0 | - |
| 2009 | 7 | 10 | 70% |
| 2010 | 1 | 2 | 50% |
| 2011 | 4 | 4 | 100% |
| 2012 | 2 | 5 | 40% |
| 2013 | 1 | 8 | 12% |
| 2014 | 6 | 14 | 43% |
| 2015 | 1 | 10 | 10% |
| 2016 | 10 | 20 | 50% |
| 2017 | 0 | 7 | 0% |
| 2018 | 4 | 17 | 24% |
| 2019 | 2 | 13 | 15% |
| 2020 | 3 | 7 | 43% |
| 2021 | 0 | 6 | 0% |
| 2022 | 0 | 4 | 0% |
| 2023 | 4 | 8 | 50% |
| 2024 | 0 | 1 | 0% |
| 2025 | 0 | 4 | 0% |
| 2026 | 0 | 0 | - |

*trend over deposit year: falling, z = -2.49, two-sided p = 0.0126 across 26 years and 181 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Per species** (product size names the species here, 283-1120 bp, so the share above pools readouts that mean different things; Oct 2022 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Orthobunyavirus ebiense (3060469) | - | 0 | 3 | 0% |
| Orthobunyavirus bunyamweraense (3052381) | - | 0 | 2 | 0% |
| Orthobunyavirus kowanyamaense (3060477) | - | 0 | 2 | 0% |
| Orthobunyavirus oropoucheense (3052429) | - | 1 | 2 | 50% |
| Orthobunyavirus akabaneense (1933178) | - | 0 | 1 | 0% |
| Orthobunyavirus infirmati (3060473) | - | 0 | 1 | 0% |
| Orthobunyavirus manzanillaense (3052416) | - | 1 | 1 | 100% |
| Orthobunyavirus oyoense (3052430) | - | 1 | 1 | 100% |
| Orthobunyavirus trinitiense (3052451) | - | 1 | 1 | 100% |
| Orthobunyavirus umbreense (3060503) | - | 0 | 1 | 0% |

**Duplication check:** 15 recent records share 12 distinct footprints (1.2 per footprint). This flag does not hold up: only 12 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 181 of 2083 screened records are evaluable (8.7%); 1902 are not. Every share above is taken over the evaluable ones.

Excluded: 1902 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1209 chance_only, 685 no_site, 5 no_pair, 3 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 662 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 23 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CIRCOVIRUSES_ssDNA_vertebrate_Rep_Gene_round2`

CIRCOVIRUSES- (ssDNA) (vertebrate circoviruses) — Rep Gene  
Designed 2000, doi:10.1007/s007050070002  
**Degeneracy:** 1536-fold degenerate (1536-fold primers x 1-fold probe); each member is ~6.5e-04 of the reaction, ~11 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1996 | 1 | 1 | 100% |
| 1997 | 1 | 2 | 50% |
| 1998 | 5 | 15 | 33% |
| 1999 | 4 | 11 | 36% |
| 2000 | 13 | 33 | 39% |
| 2001 | 4 | 30 | 13% |
| 2002 | 4 | 42 | 10% |
| 2003 | 23 | 82 | 28% |
| 2004 | 24 | 73 | 33% |
| 2005 | 39 | 103 | 38% |
| 2006 | 21 | 73 | 29% |
| 2007 | 15 | 171 | 9% |
| 2008 | 40 | 156 | 26% |
| 2009 | 70 | 201 | 35% |
| 2010 | 51 | 180 | 28% |
| 2011 | 100 | 272 | 37% |
| 2012 | 175 | 269 | 65% |
| 2013 | 162 | 257 | 63% |
| 2014 | 269 | 469 | 57% |
| 2015 | 142 | 366 | 39% |
| 2016 | 238 | 401 | 59% |
| 2017 | 312 | 631 | 49% |
| 2018 | 164 | 396 | 41% |
| 2019 | 225 | 520 | 43% |
| 2020 | 57 | 269 | 21% |
| 2021 | 174 | 770 | 23% |
| 2022 | 275 | 722 | 38% |
| 2023 | 503 | 1097 | 46% |
| 2024 | 235 | 1077 | 22% |
| 2025 | 139 | 387 | 36% |
| 2026 | 81 | 329 | 25% |

*trend over deposit year: falling, z = -4.58, two-sided p = 4.73e-06 across 31 years and 9405 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 222 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 748 recent records share 82 distinct footprints (9.1 per footprint), of which 276 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 82 independent observations (one per footprint) the interval around the 31% detected share is 22%-41%, and counting each footprint once, 20 of 82 footprints amplify (24%; interval 16%-35%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 9405 of 24095 screened records are evaluable (39.0%); 14690 are not. Every share above is taken over the evaluable ones.

Excluded: 14690 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 14121 no_site, 421 truncated, 89 no_pair, 59 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 1703 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 14121 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `SSU_rRNA_gene_Plasmodium_SSU_rDNA_Grim_2003`

SSU rRNA gene (Plasmodium) — SSU rDNA  
Designed 1995, doi:10.1006/expr.1995.1107  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1989 | 0 | 0 | - |
| 1991 | 0 | 0 | - |
| 1992 | 4 | 4 | 100% |
| 1993 | 1 | 1 | 100% |
| 1995 | 2 | 2 | 100% |
| 1996 | 4 | 9 | 44% |
| 1997 | 3 | 3 | 100% |
| 1998 | 5 | 5 | 100% |
| 1999 | 15 | 21 | 71% |
| 2000 | 0 | 0 | - |
| 2001 | 1 | 1 | 100% |
| 2002 | 3 | 3 | 100% |
| 2003 | 1 | 11 | 9% |
| 2004 | 6 | 17 | 35% |
| 2005 | 1 | 1 | 100% |
| 2006 | 70 | 70 | 100% |
| 2007 | 21 | 21 | 100% |
| 2008 | 13 | 26 | 50% |
| 2009 | 2 | 14 | 14% |
| 2010 | 1 | 13 | 8% |
| 2011 | 0 | 8 | 0% |
| 2012 | 2 | 2 | 100% |
| 2013 | 0 | 14 | 0% |
| 2014 | 23 | 142 | 16% |
| 2015 | 1 | 8 | 12% |
| 2016 | 1 | 99 | 1% |
| 2017 | 5 | 10 | 50% |
| 2018 | 5 | 9 | 56% |
| 2019 | 136 | 170 | 80% |
| 2020 | 3 | 22 | 14% |
| 2021 | 3 | 3 | 100% |
| 2022 | 1 | 2 | 50% |
| 2023 | 1 | 1 | 100% |
| 2024 | 7 | 18 | 39% |
| 2025 | 0 | 1 | 0% |
| 2026 | 0 | 3 | 0% |

*trend over deposit year: falling, z = -4.31, two-sided p = 1.6e-05 across 33 years and 734 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 22 recent records share 2 distinct footprints (11.0 per footprint). This flag does not hold up: only 2 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; counting each footprint once, 1 of 2 footprints amplify (50%; interval 9%-91%), which reaches the 90% threshold: the failing records are concentrated on few footprints. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 734 of 2712 screened records are evaluable (27.1%); 1978 are not. Every share above is taken over the evaluable ones.

Excluded: 1978 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1426 no_site, 538 truncated, 7 chance_only, 5 no_pair, 2 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 15 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 705 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 721 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ASTROVIRUS_RdRp_Chu_2008_round1`

Astrovirus pan-family RdRp heminested PCR (Chu 2008), round 1  
Designed 2008, doi:10.1128/jvi.00857-08  
**Degeneracy:** 2048-fold degenerate (2048-fold primers x 1-fold probe); each member is ~4.9e-04 of the reaction, ~11 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1992 | 0 | 0 | - |
| 1993 | 3 | 3 | 100% |
| 1994 | 4 | 4 | 100% |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 2 | 4 | 50% |
| 1998 | 0 | 0 | - |
| 1999 | 1 | 2 | 50% |
| 2000 | 1 | 3 | 33% |
| 2001 | 0 | 0 | - |
| 2002 | 0 | 0 | - |
| 2003 | 2 | 2 | 100% |
| 2004 | 1 | 2 | 50% |
| 2005 | 4 | 4 | 100% |
| 2006 | 18 | 27 | 67% |
| 2007 | 47 | 67 | 70% |
| 2008 | 16 | 23 | 70% |
| 2009 | 27 | 106 | 25% |
| 2010 | 8 | 17 | 47% |
| 2011 | 27 | 46 | 59% |
| 2012 | 24 | 53 | 45% |
| 2013 | 23 | 37 | 62% |
| 2014 | 20 | 38 | 53% |
| 2015 | 30 | 62 | 48% |
| 2016 | 48 | 105 | 46% |
| 2017 | 19 | 82 | 23% |
| 2018 | 54 | 100 | 54% |
| 2019 | 84 | 137 | 61% |
| 2020 | 49 | 147 | 33% |
| 2021 | 92 | 199 | 46% |
| 2022 | 152 | 320 | 48% |
| 2023 | 237 | 458 | 52% |
| 2024 | 114 | 221 | 52% |
| 2025 | 119 | 466 | 26% |
| 2026 | 88 | 190 | 46% |

*trend over deposit year: falling, z = -4.67, two-sided p = 3.07e-06 across 29 years and 2925 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Per species** (product size names the species here, 337-477 bp, so the share above pools readouts that mean different things; Oct 2024 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Mamastrovirus sp. (1912147) | - | 18 | 126 | 14% |
| Mamastrovirus suisvulgaris (3703182) | - | 2 | 87 | 2% |
| Porcine astrovirus 2 (1105378) | - | 9 | 48 | 19% |
| Goose astrovirus (1349999) | - | 42 | 45 | 93% |
| Bovine astrovirus (1435485) | - | 14 | 37 | 38% |
| Mamastrovirus suisencephalomyelitidis (3703181) | - | 3 | 35 | 9% |
| Mamastrovirus hominis (3430629) | - | 31 | 31 | 100% |
| Porcine astrovirus 5 (1093928) | - | 17 | 28 | 61% |
| Astroviridae sp. (2585114) | - | 2 | 18 | 11% |
| Human astrovirus (1868658) | - | 18 | 18 | 100% |
| Astroviridae (39733) | - | 12 | 17 | 71% |
| Caprine astrovirus (2870633) | - | 6 | 17 | 35% |
| Mamastrovirus felis (3430626) | - | 16 | 16 | 100% |
| Avastrovirus intestini (3426506) | - | 0 | 14 | 0% |
| Chicken astrovirus (336959) | - | 2 | 14 | 14% |
| Bat astrovirus (1697918) | - | 7 | 13 | 54% |
| Canine astrovirus (1157338) | - | 2 | 13 | 15% |
| Avastrovirus sp. (2809168) | - | 2 | 12 | 17% |
| Mamastrovirus ovis (3430634) | - | 7 | 11 | 64% |
| Astrovirus sp. (178530) | - | 0 | 7 | 0% |
| Mamastrovirus suisorientalis (3430637) | - | 4 | 7 | 57% |
| Goose astrovirus 2 (2810457) | - | 6 | 6 | 100% |
| Porcine astrovirus 1 (1559735) | - | 1 | 6 | 17% |
| Mamastrovirus (249588) | - | 0 | 4 | 0% |
| Turkey astrovirus (70793) | - | 1 | 4 | 25% |
| Goat astrovirus (2461425) | - | 2 | 3 | 67% |
| Mamastrovirus melbournense (3430631) | - | 0 | 3 | 0% |
| Rodent astrovirus (1914442) | - | 1 | 3 | 33% |
| Avastrovirus (249589) | - | 1 | 2 | 50% |
| Avastrovirus galli (3426505) | - | 0 | 2 | 0% |
| California sea lion astrovirus 5 (1073954) | - | 2 | 2 | 100% |
| California sea lion astrovirus 8 (1073957) | - | 2 | 2 | 100% |
| Mamastrovirus canis (3430625) | - | 0 | 2 | 0% |
| Murine astrovirus (1141625) | - | 0 | 2 | 0% |
| Pigeon astrovirus (3079711) | - | 0 | 2 | 0% |
| Possum astrovirus (3462434) | - | 0 | 2 | 0% |
| Rat mamastrovirus (3400669) | - | 1 | 2 | 50% |
| Water buffalo astrovirus (1495051) | - | 1 | 2 | 50% |
| Astrovirus MLB3 (1247114) | - | 0 | 1 | 0% |
| Avian astrovirus 2 (2936979) | - | 0 | 1 | 0% |
| Avian astrovirus 3 (3067165) | - | 0 | 1 | 0% |
| Avian astrovirus 4 (3067166) | - | 0 | 1 | 0% |
| Bastrovirus Rat/77 (2766746) | - | 0 | 1 | 0% |
| Bastrovirus Rat/78 (2766747) | - | 0 | 1 | 0% |
| Chenqi Marmot Astrovirus (3434963) | - | 0 | 1 | 0% |
| Civet astrovirus (2917191) | - | 0 | 1 | 0% |
| Cricetulus longicaudatus mamastrovirus (3349301) | - | 0 | 1 | 0% |
| Fox astrovirus (1328104) | - | 0 | 1 | 0% |
| Jingmen rodent astrovirus 2 (3077485) | - | 0 | 1 | 0% |
| Jingmen rodent astrovirus 3 (3077486) | - | 0 | 1 | 0% |
| Longquan rodent astrovirus 1 (3077491) | - | 0 | 1 | 0% |
| Lophuromys chrysopus mamastrovirus (3400663) | - | 1 | 1 | 100% |
| Murine astrovirus 2 (2171380) | - | 0 | 1 | 0% |
| New Zealand sea lion astrovirus 1 (3411705) | - | 1 | 1 | 100% |
| Rat astrovirus Rn/S510/Guangzhou (2093375) | - | 1 | 1 | 100% |
| Spider bastrovirus 1 (3727807) | - | 0 | 1 | 0% |
| Wufeng rodent astrovirus 1 (3077498) | - | 0 | 1 | 0% |
| Yunnan rodent mamastrovirus 1 (3386095) | - | 0 | 1 | 0% |
| Yunnan rodent mamastrovirus 2 (3386096) | - | 1 | 1 | 100% |
| Yunnan rodent mamastrovirus 3 (3386097) | - | 0 | 1 | 0% |
| Yunnan rodent mamastrovirus 4 (3386098) | - | 0 | 1 | 0% |
| Yunnan rodent mamastrovirus 5 (3386099) | - | 1 | 1 | 100% |
| Yunnan shrew mamastrovirus 1 (3386119) | - | 1 | 1 | 100% |
| Yunnan shrew mamastrovirus 2 (3386120) | - | 1 | 1 | 100% |

**Patent records:** 29 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 691 recent records share 104 distinct footprints (6.6 per footprint), of which 2 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 104 independent observations (one per footprint) the interval around the 35% detected share is 26%-44%, and counting each footprint once, 43 of 104 footprints amplify (41%; interval 32%-51%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 2925 of 16713 screened records are evaluable (17.5%); 13788 are not. Every share above is taken over the evaluable ones.

Excluded: 13788 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 11956 no_site, 1326 truncated, 488 chance_anchor, 17 chance_only, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 20 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 4054 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7902 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `CHLAMYDIA_genus_16S_Messmer_1997_round1`

CHLAMYDIA (genus) — 16S rRNA nested multiplex PCR, first step (Messmer 1997)  
Designed 1997, doi:10.1128/jcm.35.8.2043-2046.1997  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1989 | 0 | 0 | - |
| 1993 | 1 | 1 | 100% |
| 1995 | 2 | 2 | 100% |
| 1996 | 0 | 1 | 0% |
| 1997 | 64 | 77 | 83% |
| 1998 | 0 | 1 | 0% |
| 1999 | 1 | 2 | 50% |
| 2000 | 1 | 2 | 50% |
| 2001 | 0 | 1 | 0% |
| 2002 | 0 | 0 | - |
| 2003 | 7 | 9 | 78% |
| 2004 | 1 | 1 | 100% |
| 2005 | 1 | 22 | 5% |
| 2006 | 2 | 3 | 67% |
| 2007 | 1 | 2 | 50% |
| 2008 | 1 | 3 | 33% |
| 2009 | 2 | 12 | 17% |
| 2010 | 4 | 16 | 25% |
| 2011 | 15 | 21 | 71% |
| 2012 | 10 | 39 | 26% |
| 2013 | 7 | 38 | 18% |
| 2014 | 0 | 8 | 0% |
| 2015 | 25 | 53 | 47% |
| 2016 | 0 | 12 | 0% |
| 2017 | 20 | 57 | 35% |
| 2018 | 6 | 32 | 19% |
| 2019 | 19 | 26 | 73% |
| 2020 | 14 | 15 | 93% |
| 2021 | 38 | 210 | 18% |
| 2022 | 25 | 27 | 93% |
| 2023 | 1 | 1 | 100% |
| 2024 | 22 | 40 | 55% |
| 2025 | 24 | 61 | 39% |
| 2026 | 6 | 19 | 32% |

*trend over deposit year: falling, z = -5.66, two-sided p = 1.47e-08 across 32 years and 814 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 1 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 86 recent records share 10 distinct footprints (8.6 per footprint). This flag does not hold up: only 10 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 814 of 1667 screened records are evaluable (48.8%); 853 are not. Every share above is taken over the evaluable ones.

Excluded: 853 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 432 truncated, 402 no_site, 13 chance_anchor, 6 chance_only. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 21 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 155 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 247 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `SARCOCYSTIS_18S_5_8s_rDNA_short_Kutkiene_2010`

SARCOCYSTIS — 18S-5.8s rDNA(short)  
Designed 2010, doi:10.1007/s00436-010-1945-4  
**Degeneracy:** 16-fold degenerate (16-fold primers x 1-fold probe); ~4 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1992 | 0 | 0 | - |
| 1993 | 0 | 0 | - |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 1 | 0% |
| 2001 | 0 | 1 | 0% |
| 2002 | 1 | 6 | 17% |
| 2003 | 0 | 0 | - |
| 2004 | 0 | 3 | 0% |
| 2005 | 1 | 6 | 17% |
| 2006 | 0 | 0 | - |
| 2007 | 0 | 0 | - |
| 2008 | 0 | 0 | - |
| 2009 | 0 | 0 | - |
| 2010 | 0 | 0 | - |
| 2011 | 0 | 0 | - |
| 2012 | 0 | 0 | - |
| 2013 | 0 | 0 | - |
| 2014 | 34 | 35 | 97% |
| 2015 | 3 | 35 | 9% |
| 2016 | 9 | 15 | 60% |
| 2017 | 0 | 7 | 0% |
| 2018 | 22 | 31 | 71% |
| 2019 | 0 | 21 | 0% |
| 2020 | 5 | 5 | 100% |
| 2021 | 6 | 6 | 100% |
| 2022 | 0 | 0 | - |
| 2023 | 4 | 4 | 100% |
| 2024 | 7 | 8 | 88% |
| 2025 | 0 | 6 | 0% |
| 2026 | 0 | 0 | - |

*trend over deposit year: rising, z = +2.30, two-sided p = 0.0214 across 16 years and 190 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Per species** (product size names the species here, 225-846 bp, so the share above pools readouts that mean different things; Oct 2022 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Sarcocystis calchasi (1344799) | 247-248 | 7 | 8 | 88% |
| Sarcocystis arctica (1434935) | 254 | 4 | 4 | 100% |
| Sarcocystis chenggongensis (3475062) | - | 0 | 4 | 0% |
| Sarcocystis medusiformis (1929461) | - | 0 | 2 | 0% |

**Duplication check:** 18 recent records share 5 distinct footprints (3.6 per footprint). This flag does not hold up: only 5 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 190 of 30869 screened records are evaluable (0.6%); 30679 are not. Every share above is taken over the evaluable ones.

Excluded: 30679 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 28565 no_site, 1739 truncated, 287 chance_anchor, 88 chance_only. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 20651 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7914 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Paramyxovirinae_Polymerase_L_gene_round2`

Paramyxovirinae — Polymerase (L gene)  
Designed 2008, doi:10.1128/JCM.00192-08  
**Degeneracy:** 384-fold degenerate (384-fold primers x 1-fold probe); each member is ~2.6e-03 of the reaction, ~9 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1987 | 0 | 1 | 0% |
| 1989 | 0 | 2 | 0% |
| 1991 | 0 | 0 | - |
| 1993 | 0 | 9 | 0% |
| 1994 | 0 | 1 | 0% |
| 1995 | 2 | 6 | 33% |
| 1996 | 0 | 4 | 0% |
| 1997 | 0 | 1 | 0% |
| 1998 | 0 | 11 | 0% |
| 1999 | 1 | 15 | 7% |
| 2000 | 0 | 17 | 0% |
| 2001 | 0 | 16 | 0% |
| 2002 | 0 | 7 | 0% |
| 2003 | 0 | 19 | 0% |
| 2004 | 0 | 45 | 0% |
| 2005 | 0 | 25 | 0% |
| 2006 | 0 | 17 | 0% |
| 2007 | 1 | 20 | 5% |
| 2008 | 1 | 31 | 3% |
| 2009 | 1 | 61 | 2% |
| 2010 | 1 | 49 | 2% |
| 2011 | 4 | 64 | 6% |
| 2012 | 3 | 148 | 2% |
| 2013 | 0 | 145 | 0% |
| 2014 | 0 | 178 | 0% |
| 2015 | 12 | 138 | 9% |
| 2016 | 0 | 111 | 0% |
| 2017 | 8 | 378 | 2% |
| 2018 | 26 | 400 | 6% |
| 2019 | 16 | 371 | 4% |
| 2020 | 69 | 464 | 15% |
| 2021 | 141 | 364 | 39% |
| 2022 | 15 | 567 | 3% |
| 2023 | 101 | 503 | 20% |
| 2024 | 128 | 788 | 16% |
| 2025 | 663 | 1592 | 42% |
| 2026 | 1761 | 2309 | 76% |

*trend over deposit year: rising, z = +40.54, two-sided p = 0 across 36 years and 8877 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 73 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Pyeongtaek Microtus paramyxovirus (3412626) | 0 | 73 | 0% |


**Duplication check:** 3971 recent records share 150 distinct footprints (26.5 per footprint), of which 42 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 150 independent observations (one per footprint) the interval around the 62% detected share is 54%-69%, and counting each footprint once, 10 of 150 footprints amplify (7%; interval 4%-12%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 8877 of 15367 screened records are evaluable (57.8%); 6490 are not. Every share above is taken over the evaluable ones.

Excluded: 11 indeterminate, 6479 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 5909 no_site, 496 chance_anchor, 72 truncated, 2 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 165 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1604 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 4305 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `AVIPOXVIRUS_dsDNA_4b_core_Farias_2010`

AVIPOXVIRUS (dsDNA) — 4b core protein TaqMan (Farias 2010)  
Designed 2010, doi:10.1371/journal.pone.0010745  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1988 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 0 | 0 | - |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 0 | 0 | - |
| 2002 | 0 | 0 | - |
| 2003 | 1 | 1 | 100% |
| 2004 | 4 | 4 | 100% |
| 2005 | 0 | 0 | - |
| 2006 | 2 | 5 | 40% |
| 2007 | 0 | 0 | - |
| 2008 | 22 | 22 | 100% |
| 2009 | 8 | 10 | 80% |
| 2010 | 2 | 2 | 100% |
| 2011 | 23 | 28 | 82% |
| 2012 | 0 | 0 | - |
| 2013 | 46 | 64 | 72% |
| 2014 | 1 | 1 | 100% |
| 2015 | 2 | 2 | 100% |
| 2016 | 0 | 6 | 0% |
| 2017 | 6 | 10 | 60% |
| 2018 | 6 | 12 | 50% |
| 2019 | 1 | 4 | 25% |
| 2020 | 2 | 3 | 67% |
| 2021 | 0 | 2 | 0% |
| 2022 | 14 | 16 | 88% |
| 2023 | 28 | 29 | 97% |
| 2024 | 7 | 8 | 88% |
| 2025 | 14 | 15 | 93% |
| 2026 | 1 | 8 | 12% |

*trend over deposit year: falling, z = -0.88, two-sided p = 0.377 across 21 years and 252 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 7 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 24 recent records share 6 distinct footprints (4.0 per footprint). This flag does not hold up: only 6 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 252 of 1727 screened records are evaluable (14.6%); 1475 are not. Every share above is taken over the evaluable ones.

Excluded: 1475 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1389 no_site, 55 truncated, 30 chance_anchor, 1 chance_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 2 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 92 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1297 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Cryptosporidium_18SrDNA_Xiao_1999_round2`

CRYPTOSPORIDIA — 18SrDNA  
Designed 1999, doi:10.1128/aem.65.4.1578-1583.1999  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1992 | 4 | 4 | 100% |
| 1993 | 5 | 5 | 100% |
| 1994 | 2 | 2 | 100% |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1998 | 15 | 15 | 100% |
| 1999 | 27 | 27 | 100% |
| 2000 | 13 | 13 | 100% |
| 2001 | 1 | 1 | 100% |
| 2002 | 7 | 7 | 100% |
| 2003 | 17 | 18 | 94% |
| 2004 | 2 | 2 | 100% |
| 2005 | 15 | 17 | 88% |
| 2006 | 7 | 11 | 64% |
| 2007 | 19 | 22 | 86% |
| 2008 | 12 | 28 | 43% |
| 2009 | 38 | 100 | 38% |
| 2010 | 41 | 44 | 93% |
| 2011 | 22 | 23 | 96% |
| 2012 | 36 | 44 | 82% |
| 2013 | 27 | 36 | 75% |
| 2014 | 66 | 91 | 73% |
| 2015 | 56 | 66 | 85% |
| 2016 | 3 | 7 | 43% |
| 2017 | 60 | 82 | 73% |
| 2018 | 26 | 40 | 65% |
| 2019 | 61 | 78 | 78% |
| 2020 | 22 | 79 | 28% |
| 2021 | 18 | 43 | 42% |
| 2022 | 45 | 58 | 78% |
| 2023 | 140 | 345 | 41% |
| 2024 | 104 | 139 | 75% |
| 2025 | 99 | 114 | 87% |
| 2026 | 59 | 101 | 58% |

*trend over deposit year: falling, z = -6.68, two-sided p = 2.47e-11 across 32 years and 1662 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Duplication check:** 225 recent records share 32 distinct footprints (7.0 per footprint), of which 56 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 32 independent observations (one per footprint) the interval around the 72% detected share is 54%-84%, and counting each footprint once, 8 of 32 footprints amplify (25%; interval 13%-42%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 1662 of 14962 screened records are evaluable (11.1%); 13300 are not. Every share above is taken over the evaluable ones.

Excluded: 13300 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 10817 no_site, 2407 truncated, 43 chance_anchor, 33 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 484 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 10817 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Paramyxovirinae_Polymerase_L_gene_Tong_2008_round1`

Paramyxovirinae — Polymerase (L gene)  
Designed 2008, doi:10.1128/JCM.00192-08  
**Degeneracy:** 768-fold degenerate (768-fold primers x 1-fold probe); each member is ~1.3e-03 of the reaction, ~10 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1987 | 1 | 1 | 100% |
| 1989 | 1 | 2 | 50% |
| 1991 | 0 | 3 | 0% |
| 1993 | 2 | 11 | 18% |
| 1994 | 1 | 1 | 100% |
| 1995 | 6 | 6 | 100% |
| 1996 | 2 | 3 | 67% |
| 1997 | 0 | 2 | 0% |
| 1998 | 9 | 12 | 75% |
| 1999 | 14 | 15 | 93% |
| 2000 | 9 | 19 | 47% |
| 2001 | 6 | 18 | 33% |
| 2002 | 5 | 11 | 45% |
| 2003 | 14 | 23 | 61% |
| 2004 | 10 | 45 | 22% |
| 2005 | 20 | 26 | 77% |
| 2006 | 6 | 17 | 35% |
| 2007 | 8 | 22 | 36% |
| 2008 | 14 | 29 | 48% |
| 2009 | 22 | 66 | 33% |
| 2010 | 12 | 57 | 21% |
| 2011 | 42 | 65 | 65% |
| 2012 | 70 | 156 | 45% |
| 2013 | 38 | 154 | 25% |
| 2014 | 50 | 209 | 24% |
| 2015 | 84 | 147 | 57% |
| 2016 | 43 | 120 | 36% |
| 2017 | 82 | 555 | 15% |
| 2018 | 110 | 519 | 21% |
| 2019 | 96 | 467 | 21% |
| 2020 | 289 | 688 | 42% |
| 2021 | 232 | 709 | 33% |
| 2022 | 364 | 694 | 52% |
| 2023 | 318 | 542 | 59% |
| 2024 | 396 | 1165 | 34% |
| 2025 | 957 | 1780 | 54% |
| 2026 | 2095 | 2424 | 86% |

*trend over deposit year: rising, z = +26.11, two-sided p = 3.02e-150 across 37 years and 10783 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Out of scope:** 73 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts.

| off-target taxon | predicted detected | screened | share |
|---|---|---|---|
| Pyeongtaek Microtus paramyxovirus (3412626) | 6 | 73 | 8% |


**Duplication check:** 4278 recent records share 187 distinct footprints (22.9 per footprint), of which 69 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 187 independent observations (one per footprint) the interval around the 72% detected share is 66%-78%, and counting each footprint once, 92 of 187 footprints amplify (49%; interval 42%-56%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 10783 of 15367 screened records are evaluable (70.2%); 4584 are not. Every share above is taken over the evaluable ones.

Excluded: 7 indeterminate, 4577 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 4024 no_site, 416 truncated, 137 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 223 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 86 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 3938 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Encephalitozoon_18S_General_Encephalitoz_Muller_1999`

Encephalitozoon — 18S (General Encephalitozoon)  
Designed 1999, doi:10.1128/CDLI.6.2.243-246.1999  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 6 | 6 | 100% |
| 1994 | 1 | 1 | 100% |
| 1995 | 3 | 3 | 100% |
| 1996 | 3 | 3 | 100% |
| 1997 | 0 | 0 | - |
| 1998 | 2 | 2 | 100% |
| 1999 | 5 | 5 | 100% |
| 2000 | 1 | 1 | 100% |
| 2001 | 4 | 4 | 100% |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 0 | 0 | - |
| 2005 | 0 | 0 | - |
| 2006 | 0 | 6 | 0% |
| 2007 | 0 | 0 | - |
| 2008 | 2 | 2 | 100% |
| 2009 | 0 | 0 | - |
| 2010 | 6 | 8 | 75% |
| 2011 | 0 | 0 | - |
| 2012 | 8 | 12 | 67% |
| 2013 | 2 | 2 | 100% |
| 2014 | 0 | 0 | - |
| 2015 | 0 | 0 | - |
| 2016 | 1 | 1 | 100% |
| 2017 | 0 | 0 | - |
| 2018 | 0 | 0 | - |
| 2019 | 0 | 0 | - |
| 2020 | 0 | 0 | - |
| 2021 | 3 | 3 | 100% |
| 2022 | 14 | 26 | 54% |
| 2023 | 22 | 22 | 100% |
| 2024 | 0 | 0 | - |
| 2025 | 0 | 3 | 0% |
| 2026 | 0 | 6 | 0% |

*trend over deposit year: falling, z = -2.73, two-sided p = 0.00626 across 19 years and 116 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 4 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 33 recent records share 4 distinct footprints (8.2 per footprint). This flag does not hold up: only 4 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 4 independent observations (one per footprint) the interval around the 73% detected share is 28%-95%, which no longer rules out the 90% threshold; counting each footprint once, 3 of 4 footprints amplify (75%; interval 30%-95%), which reaches the 90% threshold: the failing records are concentrated on few footprints. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 116 of 9091 screened records are evaluable (1.3%); 8975 are not. Every share above is taken over the evaluable ones.

Excluded: 8975 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 8688 no_site, 208 chance_anchor, 79 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 11 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 248 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 8440 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ASTROVIRUS_RdRp_Chu_2008_round2`

Astrovirus pan-family RdRp heminested PCR (Chu 2008), round 2  
Designed 2008, doi:10.1128/jvi.00857-08  
**Degeneracy:** 1536-fold degenerate (1536-fold primers x 1-fold probe); each member is ~6.5e-04 of the reaction, ~11 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1992 | 0 | 0 | - |
| 1993 | 3 | 3 | 100% |
| 1994 | 4 | 4 | 100% |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 2 | 4 | 50% |
| 1998 | 0 | 0 | - |
| 1999 | 2 | 2 | 100% |
| 2000 | 3 | 3 | 100% |
| 2001 | 0 | 0 | - |
| 2002 | 0 | 0 | - |
| 2003 | 2 | 2 | 100% |
| 2004 | 2 | 2 | 100% |
| 2005 | 4 | 4 | 100% |
| 2006 | 24 | 24 | 100% |
| 2007 | 71 | 73 | 97% |
| 2008 | 22 | 23 | 96% |
| 2009 | 108 | 113 | 96% |
| 2010 | 13 | 17 | 76% |
| 2011 | 42 | 52 | 81% |
| 2012 | 60 | 66 | 91% |
| 2013 | 28 | 30 | 93% |
| 2014 | 44 | 47 | 94% |
| 2015 | 97 | 119 | 82% |
| 2016 | 120 | 128 | 94% |
| 2017 | 100 | 136 | 74% |
| 2018 | 81 | 114 | 71% |
| 2019 | 173 | 204 | 85% |
| 2020 | 102 | 170 | 60% |
| 2021 | 173 | 222 | 78% |
| 2022 | 224 | 330 | 68% |
| 2023 | 348 | 496 | 70% |
| 2024 | 191 | 238 | 80% |
| 2025 | 390 | 490 | 80% |
| 2026 | 138 | 191 | 72% |

*trend over deposit year: falling, z = -7.94, two-sided p = 2e-15 across 29 years and 3307 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Per species** (product size names the species here, 367-489 bp, so the share above pools readouts that mean different things; Oct 2024 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Mamastrovirus sp. (1912147) | - | 108 | 128 | 84% |
| Mamastrovirus suisvulgaris (3703182) | - | 84 | 87 | 97% |
| Porcine astrovirus 2 (1105378) | - | 43 | 48 | 90% |
| Goose astrovirus (1349999) | - | 0 | 46 | 0% |
| Bovine astrovirus (1435485) | - | 32 | 37 | 86% |
| Mamastrovirus suisencephalomyelitidis (3703181) | - | 28 | 35 | 80% |
| Mamastrovirus hominis (3430629) | - | 31 | 31 | 100% |
| Porcine astrovirus 5 (1093928) | - | 21 | 28 | 75% |
| Human astrovirus (1868658) | - | 19 | 19 | 100% |
| Astroviridae (39733) | - | 17 | 18 | 94% |
| Astroviridae sp. (2585114) | - | 13 | 17 | 76% |
| Bat astrovirus (1697918) | - | 16 | 16 | 100% |
| Caprine astrovirus (2870633) | - | 13 | 16 | 81% |
| Mamastrovirus felis (3430626) | - | 16 | 16 | 100% |
| Rodent astrovirus (1914442) | - | 14 | 16 | 88% |
| Avastrovirus intestini (3426506) | - | 1 | 14 | 7% |
| Chicken astrovirus (336959) | - | 6 | 14 | 43% |
| Astrovirus sp. (178530) | - | 8 | 13 | 62% |
| Avastrovirus sp. (2809168) | - | 8 | 13 | 62% |
| Canine astrovirus (1157338) | - | 13 | 13 | 100% |
| Mamastrovirus ovis (3430634) | - | 10 | 11 | 91% |
| Mamastrovirus suisorientalis (3430637) | - | 7 | 7 | 100% |
| Goose astrovirus 2 (2810457) | - | 0 | 6 | 0% |
| Porcine astrovirus 1 (1559735) | - | 6 | 6 | 100% |
| Mamastrovirus (249588) | - | 4 | 4 | 100% |
| Mamastrovirus melbournense (3430631) | - | 2 | 4 | 50% |
| Turkey astrovirus (70793) | - | 4 | 4 | 100% |
| Goat astrovirus (2461425) | - | 3 | 3 | 100% |
| Avastrovirus (249589) | - | 2 | 2 | 100% |
| Avian nephritis virus (1354735) | - | 0 | 2 | 0% |
| California sea lion astrovirus 5 (1073954) | - | 2 | 2 | 100% |
| California sea lion astrovirus 8 (1073957) | - | 2 | 2 | 100% |
| Mamastrovirus canis (3430625) | - | 2 | 2 | 100% |
| Murine astrovirus (1141625) | - | 1 | 2 | 50% |
| Pigeon astrovirus (3079711) | - | 2 | 2 | 100% |
| Possum astrovirus (3462434) | - | 2 | 2 | 100% |
| Rat mamastrovirus (3400669) | - | 2 | 2 | 100% |
| Water buffalo astrovirus (1495051) | - | 1 | 2 | 50% |
| Astrovirus MLB3 (1247114) | - | 1 | 1 | 100% |
| Avastrovirus galli (3426505) | - | 1 | 1 | 100% |
| Avian astrovirus 2 (2936979) | - | 0 | 1 | 0% |
| Avian astrovirus 3 (3067165) | - | 1 | 1 | 100% |
| Avian astrovirus 4 (3067166) | - | 1 | 1 | 100% |
| Chenqi Marmot Astrovirus (3434963) | - | 0 | 1 | 0% |
| Civet astrovirus (2917191) | - | 0 | 1 | 0% |
| Cricetulus longicaudatus mamastrovirus (3349301) | - | 1 | 1 | 100% |
| Fox astrovirus (1328104) | - | 1 | 1 | 100% |
| Jingmen rodent astrovirus 2 (3077485) | - | 1 | 1 | 100% |
| Jingmen rodent astrovirus 3 (3077486) | - | 0 | 1 | 0% |
| Longquan rodent astrovirus 1 (3077491) | - | 1 | 1 | 100% |
| Lophuromys chrysopus mamastrovirus (3400663) | - | 1 | 1 | 100% |
| Murine astrovirus 2 (2171380) | - | 1 | 1 | 100% |
| New Zealand sea lion astrovirus 1 (3411705) | - | 1 | 1 | 100% |
| Rat astrovirus Rn/S510/Guangzhou (2093375) | - | 1 | 1 | 100% |
| Wufeng rodent astrovirus 1 (3077498) | - | 1 | 1 | 100% |
| Yunnan rodent mamastrovirus 1 (3386095) | - | 1 | 1 | 100% |
| Yunnan rodent mamastrovirus 2 (3386096) | - | 0 | 1 | 0% |
| Yunnan rodent mamastrovirus 3 (3386097) | - | 1 | 1 | 100% |
| Yunnan rodent mamastrovirus 4 (3386098) | - | 0 | 1 | 0% |
| Yunnan rodent mamastrovirus 5 (3386099) | - | 1 | 1 | 100% |
| Yunnan shrew mamastrovirus 1 (3386119) | - | 1 | 1 | 100% |
| Yunnan shrew mamastrovirus 2 (3386120) | - | 1 | 1 | 100% |

**Patent records:** 29 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 716 recent records share 101 distinct footprints (7.1 per footprint), of which 2 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 101 independent observations (one per footprint) the interval around the 78% detected share is 69%-85%, and counting each footprint once, 71 of 101 footprints amplify (70%; interval 61%-78%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 3307 of 16713 screened records are evaluable (19.8%); 13406 are not. Every share above is taken over the evaluable ones.

Excluded: 13406 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 11765 no_site, 935 truncated, 501 chance_anchor, 204 chance_only, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 6 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 4801 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 6964 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ADENOVIRUS_dsDNA_Polymerase_Primate_speci`

ADENOVIRUS (dsDNA) — Polymerase (Primate-specific)  
Designed 2009, doi:10.1371/journal.ppat.1000503  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 0 | - |
| 1983 | 0 | 0 | - |
| 1984 | 0 | 0 | - |
| 1985 | 2 | 2 | 100% |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 1 | 0% |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 4 | 8 | 50% |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 0 | - |
| 1996 | 1 | 6 | 17% |
| 1997 | 0 | 1 | 0% |
| 1998 | 0 | 3 | 0% |
| 1999 | 1 | 4 | 25% |
| 2000 | 0 | 2 | 0% |
| 2001 | 9 | 12 | 75% |
| 2002 | 4 | 6 | 67% |
| 2003 | 5 | 11 | 45% |
| 2004 | 20 | 29 | 69% |
| 2005 | 24 | 28 | 86% |
| 2006 | 17 | 18 | 94% |
| 2007 | 9 | 11 | 82% |
| 2008 | 29 | 32 | 91% |
| 2009 | 74 | 80 | 92% |
| 2010 | 27 | 38 | 71% |
| 2011 | 20 | 30 | 67% |
| 2012 | 65 | 71 | 92% |
| 2013 | 88 | 105 | 84% |
| 2014 | 41 | 49 | 84% |
| 2015 | 60 | 75 | 80% |
| 2016 | 53 | 64 | 83% |
| 2017 | 137 | 152 | 90% |
| 2018 | 136 | 164 | 83% |
| 2019 | 126 | 151 | 83% |
| 2020 | 198 | 296 | 67% |
| 2021 | 292 | 349 | 84% |
| 2022 | 162 | 412 | 39% |
| 2023 | 390 | 497 | 78% |
| 2024 | 229 | 311 | 74% |
| 2025 | 285 | 374 | 76% |
| 2026 | 577 | 630 | 92% |

*trend over deposit year: rising, z = +1.01, two-sided p = 0.311 across 34 years and 4022 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 1012 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1086 recent records share 53 distinct footprints (20.5 per footprint), of which 22 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 53 independent observations (one per footprint) the interval around the 85% detected share is 73%-92%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 4022 of 29202 screened records are evaluable (13.8%); 25180 are not. Every share above is taken over the evaluable ones.

Excluded: 25180 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 24889 no_site, 289 truncated, 2 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 143 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 24889 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ADENOVIRUS_dsDNA_Hexon_gene_round2`

ADENOVIRUS (dsDNA) — Hexon gene  
Designed 2005, doi:10.1128/JCM.43.12.6176-6182.2005  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 0 | - |
| 1983 | 0 | 0 | - |
| 1984 | 0 | 0 | - |
| 1985 | 1 | 2 | 50% |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 1 | 0% |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 2 | 4 | 50% |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 1 | 0% |
| 1993 | 11 | 12 | 92% |
| 1994 | 0 | 1 | 0% |
| 1995 | 3 | 3 | 100% |
| 1996 | 2 | 6 | 33% |
| 1997 | 1 | 2 | 50% |
| 1998 | 3 | 7 | 43% |
| 1999 | 13 | 13 | 100% |
| 2000 | 2 | 6 | 33% |
| 2001 | 20 | 23 | 87% |
| 2002 | 5 | 7 | 71% |
| 2003 | 40 | 42 | 95% |
| 2004 | 25 | 29 | 86% |
| 2005 | 99 | 107 | 93% |
| 2006 | 20 | 22 | 91% |
| 2007 | 26 | 34 | 76% |
| 2008 | 113 | 115 | 98% |
| 2009 | 100 | 103 | 97% |
| 2010 | 61 | 93 | 66% |
| 2011 | 67 | 80 | 84% |
| 2012 | 89 | 90 | 99% |
| 2013 | 165 | 168 | 98% |
| 2014 | 79 | 90 | 88% |
| 2015 | 146 | 165 | 88% |
| 2016 | 59 | 93 | 63% |
| 2017 | 151 | 180 | 84% |
| 2018 | 107 | 141 | 76% |
| 2019 | 156 | 189 | 83% |
| 2020 | 559 | 574 | 97% |
| 2021 | 498 | 516 | 97% |
| 2022 | 341 | 415 | 82% |
| 2023 | 577 | 618 | 93% |
| 2024 | 339 | 399 | 85% |
| 2025 | 383 | 483 | 79% |
| 2026 | 788 | 860 | 92% |

*trend over deposit year: rising, z = +1.77, two-sided p = 0.0767 across 38 years and 5694 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 1043 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1427 recent records share 85 distinct footprints (16.8 per footprint), of which 27 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 85 independent observations (one per footprint) the interval around the 88% detected share is 79%-93%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 5694 of 37920 screened records are evaluable (15.0%); 32226 are not. Every share above is taken over the evaluable ones.

Excluded: 2 indeterminate, 32224 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 21485 no_site, 5254 chance_only, 4830 truncated, 569 chance_anchor, 86 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 39 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 15772 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 5713 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `ADENOVIRUS_dsDNA_Polymerase_Primate_speci_Casas_2005`

**Lineage override:** pooled status was stable.  
ADENOVIRUS (dsDNA) — Polymerase (Primate-specific)  
Designed 2009, doi:10.1371/journal.ppat.1000503  
**Degeneracy:** 16-fold degenerate (16-fold primers x 1-fold probe); ~4 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 0 | - |
| 1983 | 0 | 0 | - |
| 1984 | 0 | 0 | - |
| 1985 | 2 | 2 | 100% |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 1 | 0% |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 6 | 8 | 75% |
| 1994 | 0 | 0 | - |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 4 | 0% |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
| 1999 | 1 | 4 | 25% |
| 2000 | 0 | 0 | - |
| 2001 | 10 | 10 | 100% |
| 2002 | 3 | 4 | 75% |
| 2003 | 6 | 10 | 60% |
| 2004 | 21 | 25 | 84% |
| 2005 | 20 | 27 | 74% |
| 2006 | 16 | 18 | 89% |
| 2007 | 9 | 9 | 100% |
| 2008 | 25 | 31 | 81% |
| 2009 | 72 | 78 | 92% |
| 2010 | 28 | 40 | 70% |
| 2011 | 21 | 27 | 78% |
| 2012 | 70 | 71 | 99% |
| 2013 | 93 | 104 | 89% |
| 2014 | 39 | 49 | 80% |
| 2015 | 56 | 64 | 88% |
| 2016 | 46 | 64 | 72% |
| 2017 | 122 | 150 | 81% |
| 2018 | 137 | 160 | 86% |
| 2019 | 136 | 145 | 94% |
| 2020 | 198 | 293 | 68% |
| 2021 | 298 | 348 | 86% |
| 2022 | 220 | 409 | 54% |
| 2023 | 407 | 495 | 82% |
| 2024 | 228 | 306 | 75% |
| 2025 | 339 | 371 | 91% |
| 2026 | 582 | 627 | 93% |

*trend over deposit year: rising, z = +1.95, two-sided p = 0.0512 across 31 years and 3954 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 1012 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1079 recent records share 37 distinct footprints (29.2 per footprint), of which 23 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 37 independent observations (one per footprint) the interval around the 91% detected share is 77%-97%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 3954 of 29202 screened records are evaluable (13.5%); 25248 are not. Every share above is taken over the evaluable ones.

Excluded: 25248 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 25076 no_site, 154 truncated, 15 chance_anchor, 3 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 82 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 24 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 25052 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Morbillivirus_including_CDV_P_gene`

**Lineage override:** pooled status was stable.  
Morbillivirus (including CDV) — P gene  
Designed 1993, doi:10.1006/viro.1993.1217  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 0 | - |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 0 | - |
| 1988 | 1 | 1 | 100% |
| 1989 | 0 | 0 | - |
| 1990 | 1 | 1 | 100% |
| 1991 | 4 | 4 | 100% |
| 1992 | 3 | 3 | 100% |
| 1993 | 7 | 8 | 88% |
| 1994 | 2 | 2 | 100% |
| 1995 | 6 | 7 | 86% |
| 1996 | 2 | 2 | 100% |
| 1997 | 1 | 1 | 100% |
| 1998 | 6 | 6 | 100% |
| 1999 | 3 | 4 | 75% |
| 2000 | 13 | 13 | 100% |
| 2001 | 3 | 4 | 75% |
| 2002 | 16 | 16 | 100% |
| 2003 | 7 | 9 | 78% |
| 2004 | 3 | 6 | 50% |
| 2005 | 8 | 9 | 89% |
| 2006 | 5 | 5 | 100% |
| 2007 | 23 | 25 | 92% |
| 2008 | 47 | 48 | 98% |
| 2009 | 13 | 14 | 93% |
| 2010 | 79 | 113 | 70% |
| 2011 | 114 | 121 | 94% |
| 2012 | 16 | 21 | 76% |
| 2013 | 9 | 10 | 90% |
| 2014 | 112 | 127 | 88% |
| 2015 | 73 | 84 | 87% |
| 2016 | 31 | 46 | 67% |
| 2017 | 19 | 57 | 33% |
| 2018 | 66 | 87 | 76% |
| 2019 | 67 | 73 | 92% |
| 2020 | 203 | 278 | 73% |
| 2021 | 200 | 232 | 86% |
| 2022 | 211 | 318 | 66% |
| 2023 | 172 | 195 | 88% |
| 2024 | 161 | 198 | 81% |
| 2025 | 718 | 774 | 93% |
| 2026 | 1950 | 2016 | 97% |

*trend over deposit year: rising, z = +8.98, two-sided p = 2.78e-19 across 38 years and 4938 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 181 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 2820 recent records share 36 distinct footprints (78.3 per footprint), of which 19 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 36 independent observations (one per footprint) the interval around the 96% detected share is 84%-99%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 4938 of 37338 screened records are evaluable (13.2%); 32400 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 32399 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 31840 no_site, 502 chance_anchor, 56 truncated, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 23 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2419 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 29421 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Morbillivirus_including_CDV_P_gene_Barrett_2003`

**Lineage override:** pooled status was stable.  
Morbillivirus (including CDV) — P gene  
Designed 1993, doi:10.1006/viro.1993.1217  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1985 | 0 | 0 | - |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 0 | - |
| 1988 | 1 | 1 | 100% |
| 1989 | 0 | 0 | - |
| 1990 | 1 | 1 | 100% |
| 1991 | 4 | 4 | 100% |
| 1992 | 3 | 3 | 100% |
| 1993 | 7 | 8 | 88% |
| 1994 | 2 | 2 | 100% |
| 1995 | 6 | 7 | 86% |
| 1996 | 2 | 2 | 100% |
| 1997 | 1 | 1 | 100% |
| 1998 | 6 | 6 | 100% |
| 1999 | 3 | 4 | 75% |
| 2000 | 13 | 13 | 100% |
| 2001 | 3 | 4 | 75% |
| 2002 | 16 | 16 | 100% |
| 2003 | 7 | 9 | 78% |
| 2004 | 3 | 6 | 50% |
| 2005 | 8 | 9 | 89% |
| 2006 | 5 | 5 | 100% |
| 2007 | 23 | 25 | 92% |
| 2008 | 47 | 48 | 98% |
| 2009 | 13 | 14 | 93% |
| 2010 | 79 | 113 | 70% |
| 2011 | 114 | 121 | 94% |
| 2012 | 16 | 21 | 76% |
| 2013 | 9 | 10 | 90% |
| 2014 | 112 | 127 | 88% |
| 2015 | 73 | 84 | 87% |
| 2016 | 31 | 46 | 67% |
| 2017 | 19 | 57 | 33% |
| 2018 | 66 | 87 | 76% |
| 2019 | 67 | 73 | 92% |
| 2020 | 203 | 278 | 73% |
| 2021 | 200 | 232 | 86% |
| 2022 | 211 | 318 | 66% |
| 2023 | 172 | 195 | 88% |
| 2024 | 161 | 198 | 81% |
| 2025 | 718 | 774 | 93% |
| 2026 | 1950 | 2016 | 97% |

*trend over deposit year: rising, z = +8.98, two-sided p = 2.78e-19 across 38 years and 4938 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty)*

**Patent records:** 181 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 2820 recent records share 36 distinct footprints (78.3 per footprint), of which 19 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 36 independent observations (one per footprint) the interval around the 96% detected share is 84%-99%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 4938 of 37338 screened records are evaluable (13.2%); 32400 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 32399 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 31840 no_site, 502 chance_anchor, 56 truncated, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 23 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2419 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 29421 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

## Nested protocols (24)

Rounds are scored separately above, and that stands: either product can be read on a gel.
This section adds what neither row can say alone — the share of records **both** rounds
reach, which is what the protocol delivers when it is run as published. Round 2's own
figure is what it would do as a direct PCR; where round 1 has drifted, part of that
coverage is unreachable because the inner reaction gets no enriched template.

A round-1 failure is either a scored `fail` or a record labelled `diverged`: one primer
site found, the partner's window present, nothing credible in it. That label is
reliable for some assays and mostly chance for others (a lone primer hit in an
unrelated record clears the per-record bar), so the last column says how many of each
family's round-1 failures rest on it. Where most of them do, read the nest loss as
an upper bound.

**10 of 24** lose coverage this way. A further 1 are labelled as rounds but do not nest, so no conditional coverage is computed for them.

| protocol | round 1 | round 2 alone | run as a nest | records | inner inside outer | round 1 failures (diverged) |
|---|---|---|---|---|---|---|
| `RHABDOVIRUS_ssRNA_L_gene` | 19% | 63% | 18% | 6,926 | yes | 5,638 (248 diverged) |
| `ASTROVIRUS_RdRp_Chu_2008` | 46% | 80% | 36% | 2,901 | yes | 1,576 (20 diverged) |
| `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` (not scoreable) | 59% | 100% | 59% | 13,567 | yes | 5,574 (18 diverged) |
| `PROBOSCIVIRUS_POL_Latimer_2010_panEEHV` | 62% | 97% | 59% | 32 | yes | 12 (0 diverged) |
| `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_Lan_2010` | 57% | 71% | 46% | 6,754 | yes | 2,911 (53 diverged) |
| `ADENOVIRUS_dsDNA_Hexon_gene` | 79% | 92% | 79% | 5,863 | yes | 1,203 (37 diverged) |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1` | 0.2% | 11% | 0% | 2,316 | yes | 2,311 (289 diverged) |
| `Pan_HERPES_dsDNA_Terminase` | 90% | 90% | 81% | 2,586 | yes | 256 (20 diverged) |
| `CMV_UL55_gB_Deckers_2009_Prepens_2007` | 92% | 98% | 92% | 732 | yes | 58 (2 diverged) |
| `Cryptosporidium_18SrDNA_Xiao_1999` | 93% | 98% | 92% | 145 | yes | 10 (2 diverged) |
| `Pan_flavivirus_NS5_3` | 42% | 32% | 28% | 33,881 | yes | 19,538 (441 diverged) |
| `ADENOVIRUS_dsDNA_Polymerase_Primate_speci_Casas_2005` | 82% | 79% | 77% | 4,243 | yes | 750 (68 diverged) |
| `CIRCOVIRUSES_ssDNA_vertebrate_Rep_Gene_Mankertz_2000` | 70% | 36% | 33% | 7,506 | yes | 2,280 (1,166 diverged) |
| `ALPHAVIRUSES_Togaviridae_ssRNA_NSP4_gene` | 97% | 96% | 94% | 8,356 | yes | 234 (223 diverged) |
| `ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme` | 97% | 97% | 95% | 3,060 | yes | 102 (20 diverged) |
| `ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010` | 41% | 34% | 32% | 987 | yes | 585 (0 diverged) |
| `PHLEBOVIRUS_ssRNA_L_segment` | 97% | 96% | 94% | 269 | yes | 8 (1 diverged) |
| `Pan_HERPES_dsDNA_Polymerase` (not scoreable) | 98% | 80% | 79% | 3,462 | yes | 69 (26 diverged) |
| `CMV_UL55_gB_Deckers_2009_Deckers_2009` | 95% | 95% | 94% | 589 | yes | 28 (0 diverged) |
| `ENTEROVIRUS_ssRNA_VP3_VP1` | 97% | 12% | not a nest | 6,843 | **no** (56/3,794) | 172 (0 diverged) |
| `ADENOVIRUS_dsDNA_Pan_Polymerase` | 99% | 99% | 99% | 4,958 | yes | 35 (0 diverged) |
| `RETROVIRUS_SIV_pol_PREDICT_P029` | 99% | 99% | 98% | 3,965 | yes | 28 (0 diverged) |
| `Paramyxovirinae_Polymerase_L_gene_Tong_2008` | 61% | 33% | 33% | 8,831 | yes | 3,473 (112 diverged) |
| `BOCAVIRUS_ssDNA_NS1_gene` | 74% | 74% | 74% | 1,941 | yes | 511 (504 diverged) |

**`ENTEROVIRUS_ssRNA_VP3_VP1`** — These entries are labelled as rounds of one protocol, but their amplicons do not nest: on 3,794 records scored by both, the inner product lies inside the outer on 56. A nested reaction amplifies the outer product, so these two cannot be running that way - either the round labels are wrong or they are separate assays that share a name. No conditional coverage is reported for them, because conditioning round 2 on a round 1 that does not feed it would invent a number. Curation, not a calculation.

**`RHABDOVIRUS_ssRNA_L_gene`** — Run as published, this nest detects 18.0% of the 6,926 records both rounds can be judged on: round 1 reaches 18.6% and round 2 62.5% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 44.6% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. The rounds share reverse, so their failures are not independent - an escape there takes both.

**`ASTROVIRUS_RdRp_Chu_2008`** — Run as published, this nest detects 36.3% of the 2,901 records both rounds can be judged on: round 1 reaches 45.7% and round 2 80.1% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 43.8% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. The rounds share reverse, so their failures are not independent - an escape there takes both.

**`LYSSAVIRUSES_ssRNA_Nucleoprotein_gene`** — Run as published, this nest detects 58.8% of the 13,567 records both rounds can be judged on: round 1 reaches 58.9% and round 2 99.6% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 40.8% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. That crosses the 90% threshold: round 2 alone reads as working and the protocol does not.

**`PROBOSCIVIRUS_POL_Latimer_2010_panEEHV`** — Run as published, this nest detects 59.4% of the 32 records both rounds can be judged on: round 1 reaches 62.5% and round 2 96.9% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 37.5% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. That crosses the 90% threshold: round 2 alone reads as working and the protocol does not. The rounds share reverse, so their failures are not independent - an escape there takes both.

**`CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_Lan_2010`** — Run as published, this nest detects 46.2% of the 6,754 records both rounds can be judged on: round 1 reaches 56.9% and round 2 71.2% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 25.1% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template.

**`ADENOVIRUS_dsDNA_Hexon_gene`** — Run as published, this nest detects 78.9% of the 5,863 records both rounds can be judged on: round 1 reaches 79.5% and round 2 91.6% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 12.7% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. That crosses the 90% threshold: round 2 alone reads as working and the protocol does not. The rounds share reverse, so their failures are not independent - an escape there takes both.

**`POLYOMAVIRUS_dsDNA_PREDICT_VP1`** — Run as published, this nest detects 0.0% of the 2,316 records both rounds can be judged on: round 1 reaches 0.2% and round 2 10.8% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 10.8% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template.

**`Pan_HERPES_dsDNA_Terminase`** — Run as published, this nest detects 81.3% of the 2,586 records both rounds can be judged on: round 1 reaches 90.1% and round 2 89.9% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 8.6% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template.

**`CMV_UL55_gB_Deckers_2009_Prepens_2007`** — Run as published, this nest detects 92.1% of the 732 records both rounds can be judged on: round 1 reaches 92.1% and round 2 98.5% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 6.4% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template.

**`Cryptosporidium_18SrDNA_Xiao_1999`** — Run as published, this nest detects 91.7% of the 145 records both rounds can be judged on: round 1 reaches 93.1% and round 2 97.9% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 6.2% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template.

3 further entries declare a `source.nested_round` but have no sibling by id, so their protocol could not be assembled and nothing is reported for them: `BORNA_VIRUS_N_gene_Zimmermann_1994_round2`, `PROBOSCIVIRUS_POL_Latimer_2010_EEHV6_round2`, `Pan_reptilian_paramyxovirus_HN_gene_Ahne_1999_round2`. Which entries belong together is a curation question — the Chlamydia nest, for one, runs a genus-level round 1 into three species-specific round 2 entries on three taxids.

## Coverage gaps

These assays cannot be validated against sequence data because the sequence data
does not exist. For wildlife pathogens this is usually the finding, not a caveat.
An assay with no taxid was never searched: that is a registry gap, not a data gap.

| assay | taxon | taxid | evaluable | screened |
|---|---|---|---|---|
| `BATRAVIRUS_terminase_Licheri_2020_european_FW2_RV1` | Batravirus (formerly Batrachovirus) | 3044671 | 4 | 4 |
| `BATRAVIRUS_terminase_Licheri_2020_pan_FW4_RV4` | Batravirus (formerly Batrachovirus) | 3044671 | 8 | 8 |
| `B_salamandrivorans_Internal_transcribes_spa_Blooi_2013` | Batrachochytrium salamandrivorans | 1357716 | 6 | 12 |
| `CHYTRID_Bd_mtDNA_lineage_BdCAPE_Ghosh_2021` | Batrachochytrium dendrobatidis | 109871 | 9 | 9491 |
| `CHYTRID_Bd_mtDNA_lineage_BdGPL_Ghosh_2021` | Batrachochytrium dendrobatidis | 109871 | 8 | 9491 |
| `LEPORID_GAMMAHERPESVIRUS_5_gB_Abade_dos_Santos_2021_taqman` | Leporid gammaherpesvirus 5 | 2729004 | 5 | 5 |
| `NA_ORTHOPOX_dsDNA_G9R_myristylated_TaqMan_Gallardo_Romero_2011` | Orthopoxvirus | 10242 | 7 | 64 |
| `PROBOSCIVIRUS_POL_Latimer_2010_EEHV5_round1` | Elephant endotheliotropic herpesvirus 5 | 548689 | 9 | 20 |
| `PROBOSCIVIRUS_POL_Latimer_2010_EEHV6_round2` | Elephant endotheliotropic herpesvirus 6 | 548689 | 1 | 6 |
| `Pan_coccidia_SSUrDNA_of_E_furonis_Gen_2011` | Eimeria furonis | 352384 | 5 | 17 |
| `Sunshinevirus_RdRp_Hyndman_2012_1` | Sunshinevirus | 1921703 | 2 | 5 |
| `Sunshinevirus_RdRp_Hyndman_2012_2` | Sunshinevirus | 1921703 | 2 | 5 |
| `Tortoise_intranuclear_coccidia_18SrDNA` | Intranuclear coccidium JW-2004 | 293274 | 1 | 2 |

## Run timing

Stage times below are the last completed run, 2026-10-26 (30m 20s in all): this run's own stages are still open while its report is being written.

| stage | wall time |
|---|---:|
| workflow | 30m 20s |

124 retrieval groups were screened in this run, 1h 24m 14s of job time in all. The 10 slowest:

| group | archives | wall time | share |
|---|---:|---:|---:|
| `10244/all` | 9 | 8m 59s | 11% |
| `10241/all` | 12 | 6m 47s | 8% |
| `10242/all` | 9 | 6m 04s | 7% |
| `77643/q8c2ce9448f` | 1 | 5m 01s | 6% |
| `1387563/qdb308affab` | 1 | 4m 19s | 5% |
| `171/q4a36c8adaa` | 6 | 3m 37s | 4% |
| `10241/q059a427e43` | 10 | 3m 23s | 4% |
| `77643/qa99de05d40` | 1 | 3m 19s | 4% |
| `11051/q63c5fca5b3` | 17 | 2m 39s | 3% |
| `10508/all` | 9 | 2m 17s | 3% |

Wall time per archive, summed per group, from Snakemake's `benchmark:` files. On macOS this is the only column that exists - `max_rss` and `cpu_time` read `NA` there - so these are elapsed times, not CPU, and a job that spanned a machine sleep would be inflated by it. Only benchmarks written during this run are counted.
