# AssayWatch report — 2026-11-01

202 assays screened: 42 declining, 32 low coverage, 5 watch, 30 insufficient data, 18 no recent data, 75 stable. 17 further screened assays are not scoreable and carry no status.

31 nested protocols, counted apart because a protocol is not an assay and its rounds are listed above in their own right: 8 declining, 5 low coverage, 5 insufficient data, 2 no recent data, 11 stable.

**In one line:** of 202 published assays re-checked against GenBank records deposited up to 2026-11-01, 42 appear to be detecting measurably less of their target than they once did, and 32 have never covered much of the taxon they are screened against. 10 are listed under Start here as worth looking at first.

**What cannot be said at all:** 65 of 219 screened assays carry no usable verdict -- 30 with too few recent records, 18 with nothing newly deposited, and 17 not scoreable at all. A further 26 are held off the triage list because their primer pools are so degenerate that an in-silico detection is close to a tautology. Sparsely sequenced targets are exactly the ones this tool is for, and they are the ones it can say least about.

**What this is not.** Every number here is a prediction from sequence alone: whether each oligo still matches what has been deposited, never whether the reaction still works at the bench. No assay was run in a laboratory. There is no thermodynamic model and no limit of detection, so this cannot tell a missed cycle-threshold cutoff from a faint band. A flag is a reason to pull an assay's records and look, never a result.

**The verdicts.** `declining` -- detection has fallen from a level that previously cleared the threshold. `low coverage` -- detection is below the threshold but was never measurably higher, usually an assay screened against more diversity than it was designed for. `watch` -- below the threshold, but the interval still reaches it, so there are too few records to be sure. `insufficient data` -- too few recent evaluable records to judge; never flagged. `no recent data` -- nothing new deposited in the window. `stable` -- no evidence of loss. `not scoreable` -- a registry problem, such as an unresolved product size, rather than anything about the assay.

Registry status: 177 active, 25 draft. `draft` is a maintainer sign-off, not a data check: 22 of the 25 drafts here already carry a verified DOI, a taxid and a design year with no open review question. What does vary between entries is oligo provenance, flagged in the note column of every row below.

**Duplication check:** 26 of 74 flagged assays still hold when duplicated records are discounted (each distinct binding-site footprint counted once, and the sample size cut to the number of footprints). The note on each assay that did not hold says which test it failed.

Previous successful run: 2026-10-31 (1 day earlier).

Recent window: 24 months, widened for 51 assays that held too few records; earliest shown Nov 2024; threshold 90% detected; at least 15 recent evaluable records to flag. Deprecated assays are not screened.

## Start here (10)

Of 74 flagged assays, these are ordered by how much can be acted
on: a measured fall before a scope gap, entries whose oligo provenance is not in
doubt first, then the largest shortfall below the threshold on the most records.

| assay | status | detected (recent) | 95% CI | evaluable | baseline (n) |
|---|---|---|---|---|---|
| `Monkeypox_virus_SNP183519_Huo_2022` | declining | 34.4% | 33%-36% | 4822 | 90% (8388) |
| `Monkeypox_virus_F3L_Huo_2022_cladeIIab` | declining | 43.0% | 42%-44% | 4919 | 93% (8585) |
| `Morbillivirus_canis_H_Muller_2011_Mueller_1F` | declining | 68.1% | 58%-77% | 94 | 94% (419) |
| `Influenza_A_virus_M_Spackman_2002` | declining | 6.5% | 6%-7% | 30380 | 21% (59921) |
| `Enterovirus_5UTR_VP4_VP2_Wray_2016_round2` | declining | 52.5% | 50%-55% | 1203 | 84% (7509) |
| `West_Nile_virus_E_Lanciotti_2001` | declining | 63.8% | 61%-66% | 1722 | 87% (5369) |
| `Haemosporida_cytb_Hellgren_2004_HaemNFI` | declining | 72.2% | 67%-77% | 263 | 87% (983) |
| `Apicomplexa_18S_Garner_2006` | low coverage | 24.5% | 22%-27% | 1649 | 37% (10192) |
| `Cryptosporidium_18S_Xiao_1999_round2` | low coverage | 71.4% | 65%-77% | 224 | 64% (1438) |
| `Arenaviridae_S_Lozano_1997_ARS16V` | low coverage | 13.0% | 7%-23% | 69 | 39% (989) |

Kept off this list but unchanged in the tables below: 26 are degeneracy high or severe, where in-silico detection is close to a tautology; 31 carry a flag the duplication check did not confirm.

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
| `Simian_immunodeficiency_virus_pol_Keele_2009_PTS_spol_F2` | active | 0.0% | 0%-2% | 224 | 7% (3623) | 4x negligible | fails: too_few,change | detected share 0.0% (0%-2%) since Nov 2024, upper bound below the 90% threshold; change from baseline -8% to -5%. |
| `Simian_immunodeficiency_virus_pol_Takehisa_2009_HahnF2` (pooled: low coverage) | active | 0.0% | 0%-2% | 226 | 4% (5073) | 144x high | fails: too_few,change | pooled share 0.0% has low coverage, but lineage Lentivirus simimdef (3418654) (226 records) detects 0.0% (0.0%-1.7%), down from 4.4% on 4804 earlier records; lineage verdict overrides to declining. Entry flags: amplicon_measured_not_published. |
| `Aparavirus_apisacutum_capsid_Rossi_2024` | active | 5.6% | 1.0%-26% | 18 | 83% (106) | 4608x severe | fails: too_few | detected share 5.6% (1.0%-26%) since Nov 2024, upper bound below the 90% threshold; change from baseline -85% to -56%. 8 patent records excluded. |
| `Influenza_A_virus_M_Spackman_2002` | active | 6.5% | 6%-7% | 30380 | 21% (59921) | 32x moderate | holds | detected share 6.5% (6%-7%) since Nov 2024, upper bound below the 90% threshold; change from baseline -15% to -14%. Entry flags: oligos_modified. |
| `Monkeypox_virus_N3R_Kulesh_2004` (pooled: low coverage) | active | 14.1% | 13%-15% | 4535 | 7% (8272) | 1x negligible | fails: too_few,change | pooled share 14.1% has low coverage, but lineage Orthopoxvirus monkeypox (3431483) (2417 records) detects 26.4% (24.7%-28.2%); lineage verdict overrides to declining. Entry flags: primer_site_polymorphic. 5 patent records excluded. |
| `Enterovirus_VP3_VP1_Nix_2006_round2` (pooled: low coverage) | active | 18.0% | 17%-19% | 4639 | 12% (35931) | 16384x severe | fails: change | pooled share 18.0% has low coverage, but lineage Enterovirus betacoxsackie (3428502) (1063 records) detects 67.6% (64.8%-70.4%); lineage verdict overrides to declining. Entry flags: amplicon_measured_not_published. 40 out-of-scope records excluded. |
| `Leucocytozoon_cytb_Hellgren_2004` (pooled: low coverage) | active | 26.3% | 19%-35% | 114 | 16% (1309) | 1x negligible | fails: change | pooled share 26.3% has low coverage, but lineage Leucocytozoon sp. (1504291) (88 records) detects 34.1% (25.0%-44.5%), down from 92.6% on 122 earlier records; lineage verdict overrides to declining. Entry flags: orientation_inferred. |
| `Orthoflavivirus_NS5_Scaramozzino_2001_round2` (pooled: low coverage) | active | 29.9% | 29%-31% | 9444 | 36% (24672) | 648x high | fails: change | pooled share 29.9% has low coverage, but lineage Orthoflavivirus japonicum (3048158) (186 records) detects only 4.3% (2.2%-8.3%), down from 59.7% on 494 earlier records; lineage verdict overrides to declining. Entry flags: oligos_from_secondary_source. 1 out-of-scope records excluded. |
| `Monkeypox_virus_SNP183519_Huo_2022` | draft | 34.4% | 33%-36% | 4822 | 90% (8388) | 1x negligible | holds | detected share 34.4% (33%-36%) since Nov 2024, upper bound below the 90% threshold; change from baseline -57% to -54%. Entry flags: amplicon_measured_not_published, scope_narrower_than_taxid. 5 patent records excluded. |
| `Circoviridae_Rep_Mankertz_2000_round1` | active | 38.9% | 35%-43% | 678 | 56% (8703) | 1536x high | holds | detected share 38.9% (35%-43%) since Nov 2024, upper bound below the 90% threshold; change from baseline -21% to -14%; separately, lineage Circovirus canine (3047721) (33 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: orientation_inferred. 222 patent records excluded. |
| `Mycoplasma_16S23S_ITS_Rebelo_2011_Myco16_23S_F` | active | 40.6% | 33%-49% | 138 | 51% (523) | 8x negligible | fails: change | detected share 40.6% (33%-49%) since Nov 2024, upper bound below the 90% threshold; change from baseline -20% to -1%. Entry flags: amplicon_multimodal. 55 patent records excluded. |
| `Coronaviridae_RdRp_Watanabe_2010` (pooled: low coverage) | draft | 41.5% | 39%-44% | 1749 | 48% (6250) | 384x high | fails: change | pooled share 41.5% has low coverage, but lineage Bat coronavirus (1508220) (172 records) detects only 25.6% (19.6%-32.6%), down from 75.6% on 176 earlier records; lineage verdict overrides to declining. Entry flags: oligos_modified. |
| `Monkeypox_virus_G2R_Li_2010_G2R_WA_F` | draft | 41.6% | 40%-43% | 4767 | 95% (8132) | 1x negligible | fails: too_few | detected share 41.6% (40%-43%) since Nov 2024, upper bound below the 90% threshold; change from baseline -55% to -52%. 5 patent records excluded. |
| `Monkeypox_virus_F3L_Huo_2022_cladeIIab` | draft | 43.0% | 42%-44% | 4919 | 93% (8585) | 1x negligible | holds | detected share 43.0% (42%-44%) since Nov 2024, upper bound below the 90% threshold; change from baseline -51% to -48%. Entry flags: amplicon_measured_not_published, scope_narrower_than_taxid. 3772 out-of-scope records excluded. 5 patent records excluded. |
| `Chlamydia_trachomatis_16S_Messmer_1997_round2` | active | 46.2% | 32%-61% | 39 | 74% (323) | 1x negligible | fails: too_few,footprint,change | detected share 46.2% (32%-61%) since Nov 2024, upper bound below the 90% threshold; change from baseline -43% to -12%. Entry flags: primer_site_polymorphic. 1 patent records excluded. |
| `Orthoreovirus_RdRp_Landolfi_2010_round1` | active | 47.8% | 43%-53% | 356 | 71% (629) | 331776x severe | fails: footprint | detected share 47.8% (43%-53%) since Nov 2024, upper bound below the 90% threshold; change from baseline -30% to -17%; separately, lineage Orthoreovirus piscis (3431498) (182 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: conditions_not_printed, pairing_is_curator_reading. 52 patent records excluded. |
| `Monkeypox_virus_F3L_Huo_2022_cladeI` (pooled: low coverage) | draft | 49.4% | 48%-51% | 4918 | 6% (8585) | 1x negligible | fails: change | pooled share 49.4% has low coverage, but lineage Orthopoxvirus monkeypox (3431483) (4551 records) detects 53.4% (52.0%-54.9%); lineage verdict overrides to declining. Entry flags: amplicon_measured_not_published, scope_narrower_than_taxid. 3772 out-of-scope records excluded. 5 patent records excluded. |
| `Pseudogymnoascus_destructans_ITS1_Shuey_2014` | active | 50.0% | 28%-72% | 16 | 86% (441) | 1x negligible | fails: too_few,change | detected share 50.0% (28%-72%) since Nov 2023, upper bound below the 90% threshold; change from baseline -58% to -14% (window widened to 36 months to reach 15 evaluable records). |
| `Coronaviridae_RdRp_Quan_2010_round1` (pooled: low coverage) | active | 51.8% | 49%-54% | 1647 | 55% (5429) | 1327104x severe | fails: change | pooled share 51.8% has low coverage, but lineage Alphacoronavirus chicagoense (3433756) (166 records) detects only 0.0% (0.0%-2.3%), down from 21.4% on 168 earlier records; lineage verdict overrides to declining. 262 out-of-scope records excluded. |
| `Arenaviridae_S_Lozano_1997_ARS3V` (pooled: low coverage) | active | 51.8% | 44%-60% | 137 | 66% (1419) | 256x high | fails: change | pooled share 51.8% has low coverage, but lineage Mammarenavirus lassaense (3052310) (36 records) detects 77.8% (61.9%-88.3%); lineage verdict overrides to declining. Entry flags: oligos_modified, orientation_inferred. 473 out-of-scope records excluded. 226 patent records excluded. |
| `Enterovirus_5UTR_VP4_VP2_Wray_2016_round2` | draft | 52.5% | 50%-55% | 1203 | 84% (7509) | 32x moderate | holds | detected share 52.5% (50%-55%) since Nov 2024, upper bound below the 90% threshold; change from baseline -34% to -28%. Entry flags: amplicon_measured_not_published, orientation_inferred. |
| `Influenza_A_virus_M1_Ward_2004` (pooled: low coverage) | draft | 59.2% | 59%-60% | 70513 | 59% (113382) | 1x negligible | fails: change | pooled share 59.2% has low coverage, but lineage Alphainfluenzavirus influenzae (2955291) (70501 records) detects 59.2% (58.9%-59.6%); lineage verdict overrides to declining. Entry flags: amplicon_disagrees_with_paper. |
| `Orthoflavivirus_NS5_Scaramozzino_2001_round1` (pooled: low coverage) | active | 59.7% | 59%-61% | 9490 | 53% (24660) | 16x moderate | fails: change | pooled share 59.7% has low coverage, but lineage Orthoflavivirus usutuense (3048443) (428 records) detects only 0.0% (0.0%-0.9%), down from 12.3% on 592 earlier records; lineage verdict overrides to declining. Entry flags: amplicon_measured_not_published, oligos_from_secondary_source. 1 out-of-scope records excluded. |
| `Iflavirus_sacbroodi_polyprotein_Rossi_2024` | active | 60.4% | 47%-72% | 53 | 87% (324) | 6x negligible | fails: too_few | detected share 60.4% (47%-72%) since Nov 2024, upper bound below the 90% threshold; change from baseline -40% to -14%. Entry flags: oligos_from_secondary_source. 1 patent records excluded. |
| `Morbillivirus_canis_N_Elia_2006` (pooled: low coverage) | active | 60.6% | 51%-69% | 104 | 51% (555) | 1x negligible | fails: change | pooled share 60.6% has low coverage, but lineage Morbillivirus canis (3052342) (104 records) detects 60.6% (51.0%-69.4%); lineage verdict overrides to declining. Entry flags: amplicon_disagrees_with_paper, citation_is_indirect, oligos_from_secondary_source. 61 patent records excluded. |
| `Influenza_A_virus_NP_Tsukamoto_2010` (pooled: low coverage) | active | 60.8% | 60%-61% | 69581 | 61% (117437) | 128x moderate | fails: change | pooled share 60.8% has low coverage, but lineage Alphainfluenzavirus influenzae (2955291) (69571 records) detects 60.8% (60.5%-61.2%), down from 61.2% on 117383 earlier records; lineage verdict overrides to declining. Entry flags: retrieval_scope_incomplete. |
| `Escherichia_coli_malB_Candrian_1991` (pooled: low coverage) | active | 62.2% | 48%-75% | 45 | 73% (281) | 1x negligible | fails: too_few,change | pooled share 62.2% has low coverage, but lineage unresolved (45 records) detects 62.2% (47.6%-74.9%), down from 73.2% on 280 earlier records; lineage verdict overrides to declining. Entry flags: orientation_inferred. |
| `West_Nile_virus_E_Lanciotti_2001` | active | 63.8% | 61%-66% | 1722 | 87% (5369) | 1x negligible | holds | detected share 63.8% (61%-66%) since Nov 2024, upper bound below the 90% threshold; change from baseline -26% to -21%. Entry flags: oligos_modified. 89 patent records excluded. |
| `Morbillivirus_canis_H_Muller_2011_Mueller_1F` | active | 68.1% | 58%-77% | 94 | 94% (419) | 2x negligible | holds | detected share 68.1% (58%-77%) since Nov 2024, upper bound below the 90% threshold; change from baseline -36% to -17%. 61 patent records excluded. |
| `Triatovirus_nigereginacellulae_capsid_Rossi_2024` | active | 69.2% | 62%-76% | 172 | 83% (1057) | 1x negligible | fails: change | detected share 69.2% (62%-76%) since Nov 2024, upper bound below the 90% threshold; change from baseline -22% to -7%. Entry flags: oligos_from_secondary_source. 3 patent records excluded. |
| `Orthoreovirus_RdRp_Landolfi_2010_round2` | active | 69.6% | 65%-74% | 359 | 88% (673) | 147456x severe | holds | detected share 69.6% (65%-74%) since Nov 2024, upper bound below the 90% threshold; change from baseline -24% to -13%. Entry flags: conditions_not_printed. 52 patent records excluded. |
| `Rhabdoviridae_L_Bourhy_2005_round1` (pooled: low coverage) | active | 69.9% | 67%-72% | 1309 | 74% (5458) | 221184x severe | fails: change | pooled share 69.9% has low coverage, but lineage Lyssavirus rabies (11292) (970 records) detects 84.8% (82.5%-87.0%), down from 95.1% on 3678 earlier records; lineage verdict overrides to declining. 769 out-of-scope records excluded. |
| `Haemosporida_cytb_Hellgren_2004_HaemNFI` | active | 72.2% | 67%-77% | 263 | 87% (983) | 1x negligible | holds | detected share 72.2% (67%-77%) since Nov 2024, upper bound below the 90% threshold; change from baseline -21% to -10%. Entry flags: oligos_not_in_cited_paper, orientation_inferred. 8901 out-of-scope records excluded. |
| `Deformed_wing_virus_B_polyprotein_Rossi_2024` | active | 75.0% | 51%-90% | 16 | 100% (41) | 1x negligible | fails: too_few,recent,change | detected share 75.0% (51%-90%) since Nov 2024, upper bound below the 90% threshold; change from baseline -49% to -8%. Entry flags: oligos_from_secondary_source, scope_narrower_than_taxid. |
| `Papillomaviridae_L1_Forslund_1999` (pooled: low coverage) | active | 75.1% | 73%-77% | 1591 | 56% (14684) | 288x high | fails: change | pooled share 75.1% has low coverage, but lineage Alphapapillomavirus 9 (337041) (320 records) detects only 12.8% (9.6%-16.9%), down from 43.7% on 9521 earlier records; lineage verdict overrides to declining. Entry flags: orientation_inferred. 1064 patent records excluded. |
| `Adenoviridae_hexon_Casas_2005_round1` (pooled: low coverage) | active | 78.1% | 76%-80% | 1500 | 74% (4736) | 16x moderate | fails: change | pooled share 78.1% has low coverage, but lineage Mastadenovirus caesari (3241411) (185 records) detects only 65.4% (58.3%-71.9%), down from 71.3% on 795 earlier records; lineage verdict overrides to declining. 1043 patent records excluded. |
| `Coronaviridae_RdRp_Quan_2010_round2` (pooled: low coverage) | active | 79.2% | 77%-81% | 1575 | 69% (5313) | 12288x severe | fails: change | pooled share 79.2% has low coverage, but lineage Betacoronavirus sp. (1928434) (47 records) detects only 19.1% (10.4%-32.5%), down from 100.0% on 15 earlier records; lineage verdict overrides to declining. 262 out-of-scope records excluded. |
| `Influenza_A_virus_HA_H7_Tsukamoto_2010` (pooled: low coverage) | active | 79.3% | 72%-85% | 150 | 54% (4305) | 12288x severe | fails: recent,change | pooled share 79.3% has low coverage, but lineage Alphainfluenzavirus influenzae (2955291) (150 records) detects 79.3% (72.2%-85.0%); lineage verdict overrides to declining. Entry flags: primer_site_polymorphic, retrieval_scope_incomplete. |
| `Orthoherpesviridae_terminase_Chmielewicz_2001_round2` | active | 79.8% | 75%-84% | 332 | 92% (2791) | 128x moderate | fails: recent,change | detected share 79.8% (75%-84%) since Nov 2024, upper bound below the 90% threshold; change from baseline -17% to -8%; separately, lineage Varicellovirus humanalpha3 (3050294) (54 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 1 out-of-scope records excluded. |
| `Morbillivirus_canis_P_Scagliarini_2007` (pooled: low coverage) | active | 80.4% | 71%-87% | 92 | 74% (510) | 1x negligible | fails: recent,change | pooled share 80.4% has low coverage, but lineage Morbillivirus canis (3052342) (92 records) detects 80.4% (71.2%-87.3%); lineage verdict overrides to declining. 61 patent records excluded. |
| `Orthohantavirus_S_Anthony_2013_round1` (pooled: watch) | active | 88.0% | 85%-91% | 443 | 96% (3849) | 31104x severe | fails: recent | pooled share 88.0% is above the 90% threshold, but lineage Orthohantavirus tulaense (3052503) (102 records) detects only 64.7% (55.1%-73.3%), down from 93.3% on 386 earlier records; lineage verdict overrides to declining. Entry flags: nested_protocol. 83 patent records excluded. |
| `Alphavirus_nsP4_Sanchez-Seco_2001_round2` (pooled: stable) | active | 98.8% | 98%-99% | 3891 | 94% (4851) | 256x high | fails: recent,change | pooled share 98.8% is above the 90% threshold, but lineage Alphavirus getah (3426303) (99 records) detects only 82.8% (74.2%-89.0%), down from 88.1% on 118 earlier records; lineage verdict overrides to declining. 339 patent records excluded. |

## Low Coverage (32)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Apicomplexa_23S_Zhu_2000` | active | 0.0% | 0%-12% | 29 | 0% (85) | 8x negligible | fails: too_few | detected share 0.0% (0%-12%) since Nov 2024, upper bound below the 90% threshold; change from baseline -4% to +12% (no measurable fall from a baseline of 0%). |
| `Avipoxvirus_4b_Baek_2020` | active | 0.0% | 0%-5% | 78 | 0.3% (1005) | 1x negligible | fails: too_few | detected share 0.0% (0%-5%) since Nov 2024, upper bound below the 90% threshold; change from baseline -0.9% to +4% (no measurable fall from a baseline of 0.3%). Entry flags: scope_narrower_than_taxid. 7 patent records excluded. |
| `Helicobacter_16S_Conley_2021` | active | 0.0% | 0%-5% | 75 | 0% (1080) | 1x negligible | fails: too_few | detected share 0.0% (0%-5%) since Nov 2024, upper bound below the 90% threshold; change from baseline -0.4% to +5% (no measurable fall from a baseline of 0%). Entry flags: amplicon_disagrees_with_paper, retrieval_scope_incomplete, scope_narrower_than_taxid, thin_evidence. 1 patent records excluded. |
| `Influenza_A_virus_HA_H3_Shu_2026` | draft | 0.2% | 0.2%-0.3% | 26806 | 8% (64867) | 8x negligible | holds | detected share 0.2% (0.2%-0.3%) since Nov 2024, upper bound below the 90% threshold; change from baseline -8% to -7% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 8%); separately, lineage Alphainfluenzavirus influenzae (2955291) (26769 records) detects only 0.2% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: citation_is_indirect, conditions_not_printed, oligos_from_secondary_source, retrieval_scope_incomplete. 1773 chance-pair records excluded (drift.chance_pair_test). |
| `Orthobunyavirus_M_Briese_2007_BUN_M_IXf` | active | 0.3% | 0.1%-2% | 296 | 35% (262) | 4096x high | fails: too_few | detected share 0.3% (0.1%-2%) since Nov 2024, upper bound below the 90% threshold; change from baseline -41% to -29% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 35%); separately, lineage Orthobunyavirus oropoucheense (3052429) (278 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. |
| `Orthopoxvirus_F3L_Huo_2022` | draft | 0.5% | 0.4%-0.7% | 5686 | 4% (8986) | 1x negligible | holds | detected share 0.5% (0.4%-0.7%) since Nov 2024, upper bound below the 90% threshold; change from baseline -4% to -3% (fell less than the 5% that counts as declining, from a baseline of 4%); separately, lineage Orthopoxvirus monkeypox (3431483) (5158 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: amplicon_measured_not_published. 1272 patent records excluded. |
| `Polyomaviridae_VP1_Johne_2005_round1` | active | 0.8% | 0.3%-2% | 650 | 0.5% (1715) | 128x moderate | holds | detected share 0.8% (0.3%-2%) since Nov 2024, upper bound below the 90% threshold; change from baseline -0.3% to +1% (no measurable fall from a baseline of 0.5%); separately, lineage Betapolyomavirus hominis (1891762) (548 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: nested_protocol. 7 out-of-scope records excluded. 372 patent records excluded. |
| `Polyomaviridae_VP1_Johne_2005` | active | 1.9% | 1%-3% | 990 | 9% (5658) | 1536x high | holds | detected share 1.9% (1%-3%) since Nov 2024, upper bound below the 90% threshold; change from baseline -8% to -6% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 9%); separately, lineage Betapolyomavirus hominis (1891762) (857 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: nested_protocol. Same oligos as Polyomaviridae_VP1_Johne_2005_round2. 7 out-of-scope records excluded. 372 patent records excluded. |
| `Polyomaviridae_VP1_Johne_2005_round2` | active | 1.9% | 1%-3% | 990 | 9% (5658) | 1536x high | holds | detected share 1.9% (1%-3%) since Nov 2024, upper bound below the 90% threshold; change from baseline -8% to -6% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 9%); separately, lineage Betapolyomavirus hominis (1891762) (857 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: amplicon_measured_not_published, nested_protocol. Same oligos as Polyomaviridae_VP1_Johne_2005. 7 out-of-scope records excluded. 372 patent records excluded. |
| `Chordopoxvirinae_POL_Bracht_2006` | active | 3.7% | 3%-4% | 5650 | 3% (9333) | 1x negligible | holds | detected share 3.7% (3%-4%) since Nov 2024, upper bound below the 90% threshold; change from baseline +0.6% to +2% (rose from a baseline of 3%); separately, lineage Orthopoxvirus monkeypox (3431483) (5377 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 1439 patent records excluded. |
| `Serpentovirinae_PP1b_Uccellini_2014_PythonNido6F` | active | 4.3% | 0.8%-21% | 23 | 14% (37) | 1x negligible | fails: too_few | detected share 4.3% (0.8%-21%) since Nov 2023, upper bound below the 90% threshold; change from baseline -24% to +9% (no measurable fall from a baseline of 14%) (window widened to 36 months to reach 15 evaluable records). Entry flags: pairing_is_curator_reading. 11 patent records excluded. |
| `Monkeypox_virus_SNP183524_Huo_2022` | draft | 9.1% | 8%-10% | 4821 | 3% (8387) | 1x negligible | holds | detected share 9.1% (8%-10%) since Nov 2024, upper bound below the 90% threshold; change from baseline +5% to +7% (rose from a baseline of 3%); separately, lineage Orthopoxvirus monkeypox (3431483) (4776 records) detects only 9.1% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: amplicon_measured_not_published, scope_narrower_than_taxid. 5 patent records excluded. |
| `Arenaviridae_S_Lozano_1997_ARS16V` | active | 13.0% | 7%-23% | 69 | 39% (989) | 8x negligible | holds | detected share 13.0% (7%-23%) since Nov 2024, upper bound below the 90% threshold; change from baseline -33% to -16% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 39%). Entry flags: orientation_inferred. 473 out-of-scope records excluded. 226 patent records excluded. |
| `Orthobunyavirus_L_Briese_2007` | active | 13.0% | 5%-32% | 23 | 30% (169) | 64x moderate | fails: too_few | detected share 13.0% (5%-32%) since Nov 2022, upper bound below the 90% threshold; change from baseline -28% to +4% (no measurable fall from a baseline of 30%) (window widened to 48 months to reach 15 evaluable records). |
| `Serpentovirinae_PP1b_Uccellini_2014_PythonNodoF` | active | 17.6% | 6%-41% | 17 | 33% (27) | 1x negligible | fails: too_few | detected share 17.6% (6%-41%) since Nov 2023, upper bound below the 90% threshold; change from baseline -38% to +12% (no measurable fall from a baseline of 33%) (window widened to 36 months to reach 15 evaluable records). 11 patent records excluded. |
| `Apicomplexa_18S_Garner_2006` | active | 24.5% | 22%-27% | 1649 | 37% (10192) | 128x moderate | holds | detected share 24.5% (22%-27%) since Nov 2024, upper bound below the 90% threshold; change from baseline -15% to -10% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 37%). |
| `Orthobunyavirus_S_Briese_2007_BUNS_5_U_6` | active | 26.7% | 11%-52% | 15 | 36% (166) | 1x negligible | fails: too_few | detected share 26.7% (11%-52%) since Nov 2022, upper bound below the 90% threshold; change from baseline -27% to +17% (no measurable fall from a baseline of 36%) (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_multimodal. |
| `Haemosporida_cytb_Hellgren_2004_HaemF` | active | 27.2% | 23%-32% | 313 | 25% (1914) | 1x negligible | holds | detected share 27.2% (23%-32%) since Nov 2024, upper bound below the 90% threshold; change from baseline -3% to +8% (no measurable fall from a baseline of 25%); separately, lineage Haemoproteus sp. (191679) (65 records) detects only 7.7% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: oligos_from_secondary_source, oligos_read_from_figure. 16087 out-of-scope records excluded. |
| `Circoviridae_Rep_Mankertz_2000_round2` | active | 30.2% | 27%-34% | 741 | 39% (8664) | 1536x high | holds | detected share 30.2% (27%-34%) since Nov 2024, upper bound below the 90% threshold; change from baseline -12% to -5% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 39%); separately, lineage Circovirus pigeon (3050342) (69 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: orientation_inferred. 222 patent records excluded. |
| `Plasmodium_18S_Li_1995` | active | 31.8% | 16%-53% | 22 | 47% (712) | 1x negligible | fails: too_few,footprint | detected share 31.8% (16%-53%) since Nov 2023, upper bound below the 90% threshold; change from baseline -31% to +6% (no measurable fall from a baseline of 47%) (window widened to 36 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published. |
| `Astroviridae_RdRp_Chu_2008_round1` | active | 34.0% | 31%-38% | 679 | 51% (2246) | 2048x high | holds | detected share 34.0% (31%-38%) since Nov 2024, upper bound below the 90% threshold; change from baseline -21% to -13% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 51%); lineage Mamastrovirus suisencephalomyelitidis (3703181) (35 records) detects only 8.6%, but neither it nor the pooled share ever cleared the threshold, so there is no fall to call a decline. Entry flags: amplicon_measured_not_published, nested_protocol. 29 patent records excluded. |
| `Chlamydia_16S_Messmer_1997_round1` | active | 41.2% | 31%-52% | 85 | 40% (729) | 1x negligible | fails: too_few | detected share 41.2% (31%-52%) since Nov 2024, upper bound below the 90% threshold; change from baseline -10% to +12% (no measurable fall from a baseline of 40%); separately, lineage Chlamydia trachomatis (813) (39 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: primer_site_polymorphic, scope_narrower_than_taxid. 1 patent records excluded. |
| `Deformed_wing_virus_A_polyprotein_Rossi_2024` | active | 48.9% | 35%-63% | 47 | 88% (40) | 1x negligible | holds | detected share 48.9% (35%-63%) since Nov 2024, upper bound below the 90% threshold; change from baseline -54% to -19% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 88%). Entry flags: oligos_from_secondary_source, scope_narrower_than_taxid. |
| `Orthobunyavirus_M_Briese_2007_M3560_F` | active | 60.0% | 39%-78% | 20 | 42% (207) | 192x high | fails: too_few | detected share 60.0% (39%-78%) since Nov 2022, upper bound below the 90% threshold; change from baseline -4% to +37% (no measurable fall from a baseline of 42%) (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_multimodal. |
| `Sarcocystis_18S_5_8S_Kutkiene_2010_ShortITS1R` | active | 61.1% | 39%-80% | 18 | 49% (172) | 16x moderate | fails: too_few | detected share 61.1% (39%-80%) since Nov 2022, upper bound below the 90% threshold; change from baseline -11% to +32% (no measurable fall from a baseline of 49%) (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_multimodal. |
| `Paramyxoviridae_L_Tong_2008_round2` | active | 61.7% | 60%-63% | 3968 | 10% (4912) | 384x high | holds | detected share 61.7% (60%-63%) since Nov 2024, upper bound below the 90% threshold; change from baseline +50% to +53% (rose from a baseline of 10%); separately, lineage Morbillivirus canis (3052342) (83 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 73 out-of-scope records excluded. |
| `Avipoxvirus_4b_Farias_2010` | active | 62.5% | 43%-79% | 24 | 76% (229) | 1x negligible | fails: too_few | detected share 62.5% (43%-79%) since Nov 2024, upper bound below the 90% threshold; change from baseline -34% to +3% (no measurable fall from a baseline of 76%). Entry flags: amplicon_disagrees_with_paper. 7 patent records excluded. |
| `Cryptosporidium_18S_Xiao_1999_round2` | active | 71.4% | 65%-77% | 224 | 64% (1438) | 1x negligible | holds | detected share 71.4% (65%-77%) since Nov 2024, upper bound below the 90% threshold; change from baseline +1% to +14% (rose from a baseline of 64%). |
| `Paramyxoviridae_L_Tong_2008_round1` | active | 72.8% | 71%-74% | 4276 | 38% (6512) | 768x high | holds | detected share 72.8% (71%-74%) since Nov 2024, upper bound below the 90% threshold; change from baseline +33% to +37% (rose from a baseline of 38%); separately, lineage Orthorubulavirus hominis (3052556) (126 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 73 out-of-scope records excluded. |
| `Astroviridae_RdRp_Chu_2008_round2` | active | 78.0% | 75%-81% | 704 | 78% (2603) | 1536x high | holds | detected share 78.0% (75%-81%) since Nov 2024, upper bound below the 90% threshold; change from baseline -3% to +4% (no measurable fall from a baseline of 78%); separately, lineage Goose astrovirus (1349999) (46 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: nested_protocol. 29 patent records excluded. |
| `Orthoherpesviridae_POL_VanDevanter_1996_round2` | active | 82.9% | 79%-86% | 356 | 85% (3353) | 12288x severe | fails: recent | detected share 82.9% (79%-86%) since Nov 2024, upper bound below the 90% threshold; change from baseline -7% to +1% (no measurable fall from a baseline of 85%). Entry flags: orientation_inferred. 2 out-of-scope records excluded. |
| `Adenoviridae_hexon_Casas_2005_round2` | active | 88.0% | 86%-90% | 1429 | 91% (4267) | 8x negligible | fails: recent | detected share 88.0% (86%-90%) since Nov 2024, upper bound below the 90% threshold; change from baseline -5% to -1.0% (fell less than the 5% that counts as declining, from a baseline of 91%); separately, lineage Aviadenovirus hepatitidis (3426530) (49 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. 1043 patent records excluded. |

## Watch (5)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Sarcocystis_18S_5_8S_Kutkiene_2010_P_ITSR` | active | 80.0% | 55%-93% | 15 | 99% (154) | 1x negligible | - | detected share 80.0% is below the 90% threshold, but its interval (55%-93%) still reaches it (window widened to 48 months to reach 15 evaluable records). |
| `Vibrio_coralliilyticus_dnaJ_Pollock_2010` | active | 83.3% | 61%-94% | 18 | 61% (56) | 2x negligible | - | detected share 83.3% is below the 90% threshold, but its interval (61%-94%) still reaches it. Entry flags: primer_site_polymorphic. |
| `Ranavirus_VIR_Pallister_2007` | active | 88.9% | 80%-94% | 72 | 91% (178) | 1x negligible | - | detected share 88.9% is below the 90% threshold, but its interval (80%-94%) still reaches it. Entry flags: amplicon_multimodal, oligos_from_secondary_source. |
| `Morbillivirus_canis_H_Muller_2011_Mueller_2F` | active | 89.8% | 85%-93% | 187 | 91% (1745) | 1x negligible | - | detected share 89.8% is below the 90% threshold, but its interval (85%-93%) still reaches it. Entry flags: pairing_is_curator_reading. 61 patent records excluded. |
| `Ranavirus_MCP_Pallister_2007` | active | 89.9% | 81%-95% | 79 | 88% (273) | 1x negligible | - | detected share 89.9% is below the 90% threshold, but its interval (81%-95%) still reaches it. Entry flags: amplicon_measured_not_published, oligos_read_from_figure. |

## Insufficient Data (30)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Batrachochytrium_dendrobatidis_mtDNA_Ghosh_2021_BdCAPE` | active | 0.0% | 0%-56% | 3 | 0% (6) | 1x negligible | - | 3 evaluable records since Nov 2024, below the minimum of 15; the detected share is 0% (0%-56%), too wide to act on. Entry flags: oligos_read_from_figure, scope_narrower_than_taxid. 2 patent records excluded. |
| `Batrachochytrium_salamandrivorans_ITS1_5_8S_Blooi_2013` | active | 0.0% | 0%-43% | 5 | 100% (1) | 1x negligible | - | 5 evaluable records since Nov 2024, below the minimum of 15; the detected share is 0% (0%-43%), too wide to act on. Entry flags: oligos_from_secondary_source. |
| `Largemouth_bass_virus_MCP_Grizzle_2003` | active | 16.7% | 5%-45% | 12 | 45% (22) | 1x negligible | - | 12 evaluable records since Nov 2021, below the minimum of 15; the detected share is 17% (5%-45%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Orthobunyavirus_M_Briese_2007_BUN_S5_F` | active | 21.4% | 8%-48% | 14 | 7% (76) | 128x moderate | - | 14 evaluable records since Nov 2021, below the minimum of 15; the detected share is 21% (8%-48%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Reptarenavirus_GP_Aqrawi_2015` | active | 22.2% | 6%-55% | 9 | 70% (105) | 16x moderate | - | 9 evaluable records since Nov 2021, below the minimum of 15; the detected share is 22% (6%-55%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. |
| `Serpentovirinae_PP1b_Uccellini_2014_PythonNido7F` | active | 40.0% | 17%-69% | 10 | 56% (18) | 1x negligible | - | 10 evaluable records since Nov 2021, below the minimum of 15; the detected share is 40% (17%-69%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: pairing_is_curator_reading. 11 patent records excluded. |
| `Ferlavirus_L_Ahne_1999_AhneL5` | active | 50.0% | 19%-81% | 6 | 50% (14) | 1x negligible | - | 6 evaluable records since Nov 2021, below the minimum of 15; the detected share is 50% (19%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. 3 patent records excluded. |
| `Ferlavirus_L_Ahne_1999_AhneL7` | active | 50.0% | 19%-81% | 6 | 69% (16) | 1x negligible | - | 6 evaluable records since Nov 2021, below the minimum of 15; the detected share is 50% (19%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. 3 patent records excluded. |
| `Orthobornavirus_XP_Sigrist_2021_passerine` | active | 50.0% | 15%-85% | 4 | 78% (23) | 64x moderate | - | 4 evaluable records since Nov 2021, below the minimum of 15; the detected share is 50% (15%-85%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: cross_reactive, oligos_read_from_figure. 1275 out-of-scope records excluded. |
| `Encephalitozoon_cuniculi_PTP_Xiao_2001` | active | 58.3% | 32%-81% | 12 | 43% (23) | 1x negligible | - | 12 evaluable records since Nov 2021, below the minimum of 15; the detected share is 58% (32%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_multimodal, thin_evidence. 3 patent records excluded. |
| `Proboscivirus_POL_Latimer_2012_round1` | active | 58.3% | 32%-81% | 12 | 65% (20) | 1024x high | - | 12 evaluable records since Nov 2021, below the minimum of 15; the detected share is 58% (32%-81%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Ophidiomyces_ophidiicola_ITS2_Bohuski_2015` | active | 62.5% | 31%-86% | 8 | 100% (17) | 1x negligible | - | 8 evaluable records since Nov 2021, below the minimum of 15; the detected share is 62% (31%-86%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Ferlavirus_HN_Ahne_1999_round1` | active | 66.7% | 30%-90% | 6 | 95% (22) | 1x negligible | - | 6 evaluable records since Nov 2021, below the minimum of 15; the detected share is 67% (30%-90%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published. 3 patent records excluded. |
| `Ferlavirus_L_Hyndman_2012` | active | 85.7% | 49%-97% | 7 | 46% (46) | 1x negligible | - | 7 evaluable records since Nov 2021, below the minimum of 15; the detected share is 86% (49%-97%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. 3 patent records excluded. |
| `Proboscivirus_POL_Latimer_2012_round2` | active | 92.9% | 69%-99% | 14 | 100% (25) | 1024x high | - | 14 evaluable records since Nov 2021, below the minimum of 15; the detected share is 93% (69%-99%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Batrachochytrium_dendrobatidis_mtDNA_Ghosh_2021_BdGPL` | active | 100.0% | 34%-100% | 2 | 33% (6) | 1x negligible | - | 2 evaluable records since Nov 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on. Entry flags: oligos_read_from_figure, scope_narrower_than_taxid. 2 patent records excluded. |
| `Bovine_papular_stomatitis_virus_RPO147_Zhao_2013` | draft | 100.0% | 72%-100% | 10 | 100% (10) | 1x negligible | - | 10 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (72%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published, chemistry_detail_missing, cross_reactive, thin_evidence. 2692 out-of-scope records excluded. 2 patent records excluded. |
| `Chlamydia_pneumoniae_16S_Messmer_1997_round2` | active | 100.0% | 57%-100% | 5 | 100% (11) | 1x negligible | - | 5 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (57%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Cryptosporidium_18S_Xiao_1999_round1` | active | 100.0% | 78%-100% | 14 | 95% (131) | 1x negligible | - | 14 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (78%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_modified. |
| `Elephant_endotheliotropic_herpesvirus_3_and_4_POL_Latimer_2012_round1` | active | 100.0% | 34%-100% | 2 | 78% (9) | 1x negligible | - | 2 evaluable records since Nov 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on. |
| `Elephant_endotheliotropic_herpesvirus_3_and_4_POL_Latimer_2012_round2` | active | 100.0% | 34%-100% | 2 | 100% (10) | 1x negligible | - | 2 evaluable records since Nov 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on. |
| `Elephant_endotheliotropic_herpesvirus_3_and_4_POL_Latimer_2012_round3` | active | 100.0% | 51%-100% | 4 | 91% (11) | 1x negligible | - | 4 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (51%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Escherichia_coli_LT_Victor_1991` | active | 100.0% | 21%-100% | 1 | 96% (27) | 1x negligible | - | 1 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (21%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: citation_is_indirect, oligos_from_secondary_source, orientation_inferred. |
| `Escherichia_coli_hlyA_Wang_1997` | active | 100.0% | 34%-100% | 2 | 100% (96) | 1x negligible | - | 2 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: orientation_inferred. |
| `Ferlavirus_HN_Ahne_1999_round2` | active | 100.0% | 61%-100% | 6 | 96% (24) | 1x negligible | - | 6 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (61%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published. 3 patent records excluded. |
| `Mycoplasmatota_16S_Feldman_2006` | active | 100.0% | 34%-100% | 2 | 100% (27) | 1x negligible | - | 2 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Paranannizziopsis_ITS_Lorch_2023` | active | 100.0% | 72%-100% | 10 | 100% (20) | 1x negligible | - | 10 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (72%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |
| `Reptarenavirus_GP2_Baggio_2023` | active | 100.0% | 70%-100% | 9 | 95% (105) | 1x negligible | - | 9 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (70%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: pooled_as_one_assay. |
| `Vairimorpha_apis_18S_Martin-Hernandez_2007` | active | 100.0% | 51%-100% | 4 | 100% (19) | 1x negligible | - | 4 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (51%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_read_from_figure. |
| `Vairimorpha_bombi_18S_Klee_2006` | active | 100.0% | 70%-100% | 9 | 74% (72) | 1x negligible | - | 9 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (70%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_from_secondary_source. |

## No Recent Data (18)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Batravirus_terminase_Licheri_2020_european` | active | - | - | 0 | 100% (4) | 128x moderate | - | no evaluable records deposited since Nov 2024. Entry flags: scope_narrower_than_taxid. 4 out-of-scope records excluded. |
| `Batravirus_terminase_Licheri_2020_pan` | active | - | - | 0 | 100% (8) | 995328x severe | - | no evaluable records deposited since Nov 2024. |
| `Caliciviridae_RdRp_Neill_1995` | draft | - | - | 0 | 40% (25) | 1x negligible | - | no evaluable records deposited since Nov 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: thin_evidence. 84751 out-of-scope records excluded. 4 patent records excluded. |
| `Caliciviridae_capsid_Reid_1999` | active | - | - | 0 | 100% (11) | 1x negligible | - | no evaluable records deposited since Nov 2024. 67577 out-of-scope records excluded. |
| `Caliciviridae_helicase_Neill_1995` | draft | - | - | 0 | 79% (24) | 1x negligible | - | no evaluable records deposited since Nov 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_modified, thin_evidence. 84751 out-of-scope records excluded. 4 patent records excluded. |
| `Eimeria_furonis_18S_Sledge_2011` | active | - | - | 0 | 100% (5) | 1x negligible | - | no evaluable records deposited since Nov 2024. |
| `Elephant_endotheliotropic_herpesvirus_5_POL_Latimer_2012_round1` | active | - | - | 0 | 100% (9) | 1x negligible | - | no evaluable records deposited since Nov 2024. |
| `Elephant_endotheliotropic_herpesvirus_5_POL_Latimer_2012_round2` | active | - | - | 0 | 100% (14) | 1x negligible | - | no evaluable records deposited since Nov 2024. |
| `Elephant_endotheliotropic_herpesvirus_5_POL_Latimer_2012_round2B` | active | - | - | 0 | 100% (10) | 1x negligible | - | no evaluable records deposited since Nov 2024. |
| `Elephant_endotheliotropic_herpesvirus_6_POL_Latimer_2012_round2` | active | - | - | 0 | 100% (1) | 64x moderate | - | no evaluable records deposited since Nov 2024. Entry flags: nested_parent_not_held, thin_evidence. |
| `Intranuclear_coccidium_JW_2004_18S_Alvarez_2013` | active | - | - | 0 | 100% (1) | 1x negligible | - | no evaluable records deposited since Nov 2024. |
| `Leporid_gammaherpesvirus_5_gB_AbadeDosSantos_2021` | active | - | - | 0 | 100% (5) | 1x negligible | - | no evaluable records deposited since Nov 2024. Entry flags: shares_oligos_with_sibling. |
| `Ophidiomyces_ophidiicola_IGS_Bohuski_2015` | active | - | - | 0 | 100% (11) | 1x negligible | - | no evaluable records deposited since Nov 2024. |
| `Orthopoxvirus_G9R_Gallardo-Romero_2011` | draft | - | - | 0 | 100% (7) | 384x high | - | no evaluable records deposited since Nov 2024. Entry flags: thin_evidence. 18787 out-of-scope records excluded. |
| `Perkinsea_18S_Smilansky_2021_cladeAC` | active | - | - | 0 | 50% (391) | 4x negligible | - | no evaluable records deposited since Nov 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_from_secondary_source. 1389 out-of-scope records excluded. |
| `Perkinsea_18S_Smilansky_2021_cladeD` | active | - | - | 0 | 42% (391) | 4x negligible | - | no evaluable records deposited since Nov 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_from_secondary_source, retrieval_scope_incomplete. 1389 out-of-scope records excluded. |
| `Sunshinevirus_L_Hyndman_2012_SunshineS1` | active | - | - | 0 | 100% (2) | 1x negligible | - | no evaluable records deposited since Nov 2024. Entry flags: orientation_inferred. 3 patent records excluded. |
| `Sunshinevirus_L_Hyndman_2012_SunshineS2` | active | - | - | 0 | 100% (2) | 1x negligible | - | no evaluable records deposited since Nov 2024. Entry flags: orientation_inferred. 3 patent records excluded. |

## Stable (75)

| assay | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Usutu_virus_NS1_Jost_2011` | active | 90.1% | 87%-93% | 392 | 96% (684) | 1x negligible | - | detected share 90.1% (87%-93%) since Nov 2024. Entry flags: primer_site_polymorphic. 2 patent records excluded. |
| `Monkeypox_virus_F3L_Kulesh_2004` | active | 90.5% | 90%-91% | 4903 | 99% (8583) | 1x negligible | - | detected share 90.5% (90%-91%) since Nov 2024. 5 patent records excluded. |
| `Cytomegalovirus_gB_Deckers_2009_round2` | active | 90.6% | 76%-97% | 32 | 94% (542) | 32x moderate | - | detected share 90.6% (76%-97%) since Nov 2024. Entry flags: citation_is_indirect. 762 patent records excluded. |
| `Rhabdoviridae_L_Bourhy_2005_round2` | active | 91.2% | 90%-93% | 1282 | 95% (5352) | 36864x severe | - | detected share 91.2% (90%-93%) since Nov 2024. Entry flags: oligos_from_secondary_source. 769 out-of-scope records excluded. |
| `Orthoherpesviridae_terminase_Chmielewicz_2001_round1` | active | 91.5% | 88%-94% | 284 | 89% (2329) | 128x moderate | - | detected share 91.5% (88%-94%) since Nov 2024. Entry flags: orientation_inferred. 1 out-of-scope records excluded. |
| `Dependoparvovirus_VP1_Gao_2002_1` | active | 91.8% | 88%-95% | 256 | 89% (1772) | 1x negligible | - | detected share 91.8% (88%-95%) since Nov 2024. Entry flags: oligos_modified. Same oligos as Dependoparvovirus_VP1_Gao_2002_2. 6845 patent records excluded. |
| `Dependoparvovirus_VP1_Gao_2002_2` | active | 91.8% | 88%-95% | 256 | 89% (1772) | 1x negligible | - | detected share 91.8% (88%-95%) since Nov 2024. Same oligos as Dependoparvovirus_VP1_Gao_2002_1. 6845 patent records excluded. |
| `Tilapinevirus_tilapiae_seg3_KembouTsofack_2017` | active | 92.0% | 75%-98% | 25 | 99% (77) | 1x negligible | - | detected share 92.0% (75%-98%) since Nov 2022 (window widened to 48 months to reach 15 evaluable records). Entry flags: citation_is_indirect, thin_evidence. |
| `Bocaparvovirus_NS1_Kapoor_2010_round1` | active | 92.9% | 90%-95% | 425 | 64% (1625) | 1024x high | - | detected share 92.9% (90%-95%) since Nov 2024. 13 patent records excluded. |
| `Influenza_A_virus_HA_H3_Shu_2026_v2` | draft | 93.6% | 93%-94% | 26909 | 84% (72253) | 16x moderate | - | detected share 93.6% (93%-94%) since Nov 2024. Entry flags: oligos_modified, retrieval_scope_incomplete, thin_evidence. 1058 chance-pair records excluded (drift.chance_pair_test). |
| `Helicobacter_16S_Fox_1998_C05` | active | 94.1% | 84%-98% | 51 | 89% (484) | 1x negligible | - | detected share 94.1% (84%-98%) since Nov 2024. Entry flags: amplicon_measured_not_published, orientation_inferred. 1 patent records excluded. |
| `Mastadenovirus_POL_Roy_2009_round2` | active | 94.3% | 93%-96% | 1086 | 83% (2936) | 1x negligible | - | detected share 94.3% (93%-96%) since Nov 2024. 1012 patent records excluded. |
| `Chordopoxvirinae_topoisomerase_Bracht_2006` | active | 94.8% | 94%-95% | 5606 | 98% (9444) | 1x negligible | - | detected share 94.8% (94%-95%) since Nov 2024. 1439 patent records excluded. |
| `Bocaparvovirus_NS1_Kapoor_2010_round2` | active | 95.2% | 93%-97% | 415 | 68% (1526) | 2048x high | - | detected share 95.2% (93%-97%) since Nov 2024. 13 patent records excluded. |
| `Chordopoxvirinae_RPO147_Li_2010` | draft | 95.2% | 77%-99% | 21 | 97% (184) | 1x negligible | - | detected share 95.2% (77%-99%) since Nov 2024. Entry flags: scope_narrower_than_taxid. 78 patent records excluded. |
| `Adenoviridae_POL_Wellehan_2004_round2` | active | 96.0% | 95%-97% | 1252 | 97% (3608) | 10616832x severe | - | detected share 96.0% (95%-97%) since Nov 2024. Entry flags: amplicon_multimodal. 160 out-of-scope records excluded. 991 patent records excluded. |
| `Astroviridae_RdRp_Atkins_2008_round2` | active | 96.1% | 94%-97% | 698 | 91% (2611) | 131072x severe | - | detected share 96.1% (94%-97%) since Nov 2024. Entry flags: nested_protocol. 29 patent records excluded. |
| `Influenza_A_virus_HA_H5_Tsukamoto_2010` | active | 96.2% | 96%-96% | 20890 | 88% (14950) | 8192x severe | - | detected share 96.2% (96%-96%) since Nov 2024. Entry flags: amplicon_multimodal, retrieval_scope_incomplete. 25 patent records excluded. |
| `Chronic_bee_paralysis_virus_RNA1_Rossi_2024` | active | 96.3% | 82%-99% | 27 | 90% (124) | 16x moderate | - | detected share 96.3% (82%-99%) since Nov 2024. 3 patent records excluded. |
| `Orthohantavirus_S_Mangombi_2021_round2` | draft | 96.5% | 94%-98% | 402 | 93% (3986) | 5184x severe | - | detected share 96.5% (94%-98%) since Nov 2024. Entry flags: nested_protocol. 83 patent records excluded. |
| `Monkeypox_virus_G2R_Li_2010_G2R_G_F` | draft | 96.5% | 96%-97% | 4745 | 99% (8006) | 1x negligible | - | detected share 96.5% (96%-97%) since Nov 2024. 5 patent records excluded. |
| `Cytomegalovirus_gB_Deckers_2009_round1` | active | 96.9% | 84%-99% | 32 | 94% (595) | 256x high | - | detected share 96.9% (84%-99%) since Nov 2024. Entry flags: citation_is_indirect. 762 patent records excluded. |
| `Cytomegalovirus_gB_Prepens_2007_round1` | active | 96.9% | 84%-99% | 32 | 91% (643) | 512x high | - | detected share 96.9% (84%-99%) since Nov 2024. Entry flags: amplicon_measured_not_published. 762 patent records excluded. |
| `Cytomegalovirus_gB_Prepens_2007_round2` | active | 96.9% | 84%-99% | 32 | 97% (664) | 8192x severe | - | detected share 96.9% (84%-99%) since Nov 2024. Entry flags: amplicon_measured_not_published. 762 patent records excluded. |
| `Influenza_A_virus_M1_Yang_2014` | draft | 96.9% | 97%-97% | 70517 | 93% (113385) | 128x moderate | - | detected share 96.9% (97%-97%) since Nov 2024. Entry flags: amplicon_disagrees_with_paper, oligos_modified, orientation_inferred. |
| `Parapoxvirus_RPO147_Zhao_2013` | draft | 97.0% | 85%-99% | 33 | 95% (86) | 1x negligible | - | detected share 97.0% (85%-99%) since Nov 2024. Entry flags: amplicon_measured_not_published, chemistry_detail_missing, primer_site_polymorphic. 698 out-of-scope records excluded. 53 patent records excluded. |
| `Phlebovirus_L_Sanchez-Seco_2003_round2` | active | 97.2% | 93%-99% | 142 | 85% (320) | 8192x severe | - | detected share 97.2% (93%-99%) since Nov 2024. |
| `Mastadenovirus_POL_Roy_2009_round1` | active | 97.2% | 96%-98% | 1079 | 87% (2875) | 16x moderate | - | detected share 97.2% (96%-98%) since Nov 2024. 1012 patent records excluded. |
| `Orthoflavivirus_NS5_Moureau_2007` | active | 97.7% | 97%-98% | 9399 | 99% (24391) | 768x high | - | detected share 97.7% (97%-98%) since Nov 2024. 1 out-of-scope records excluded. |
| `Chordopoxvirinae_IMV_Li_2010` | draft | 97.9% | 98%-98% | 5764 | 98% (9166) | 1x negligible | - | detected share 97.9% (98%-98%) since Nov 2024. Entry flags: scope_narrower_than_taxid. 1360 patent records excluded. |
| `Leptospira_lipL32_Ahmed_2020` | active | 98.1% | 96%-99% | 414 | 87% (1523) | 32x moderate | - | detected share 98.1% (96%-99%) since Nov 2024. Entry flags: primer_site_polymorphic, scope_narrower_than_taxid. 19 chance-pair records excluded (drift.chance_pair_test). |
| `Phlebovirus_L_Sanchez-Seco_2003_round1` | active | 98.1% | 90%-100% | 54 | 96% (216) | 256x high | - | detected share 98.1% (90%-100%) since Nov 2024. |
| `Morbillivirus_P_Barrett_1993_Grosh_F` | active | 98.2% | 98%-99% | 2818 | 98% (2123) | 1x negligible | - | detected share 98.2% (98%-99%) since Nov 2024. Entry flags: amplicon_measured_not_published. Same oligos as Morbillivirus_P_Barrett_1993_MorbF. 181 patent records excluded. |
| `Morbillivirus_P_Barrett_1993_MorbF` | active | 98.2% | 98%-99% | 2818 | 98% (2123) | 1x negligible | - | detected share 98.2% (98%-99%) since Nov 2024. Same oligos as Morbillivirus_P_Barrett_1993_Grosh_F. 181 patent records excluded. |
| `Morbillivirus_canis_H_Muller_2011_Mueller_3F` | active | 98.4% | 95%-99% | 185 | 97% (1693) | 1x negligible | - | detected share 98.4% (95%-99%) since Nov 2024. Entry flags: pairing_is_curator_reading. 61 patent records excluded. |
| `Monkeypox_virus_C3L_Li_2010` | active | 98.4% | 97%-99% | 866 | 98% (466) | 1x negligible | - | detected share 98.4% (97%-99%) since Nov 2024. Entry flags: amplicon_measured_not_published, scope_narrower_than_taxid. 5 patent records excluded. |
| `Adenoviridae_POL_Wellehan_2004_round1` | active | 98.5% | 98%-99% | 1176 | 91% (3783) | 1811939328x severe | - | detected share 98.5% (98%-99%) since Nov 2024. Entry flags: amplicon_multimodal. 160 out-of-scope records excluded. 991 patent records excluded. |
| `Enterovirus_5UTR_VP4_VP2_Wray_2016_round1` | draft | 98.6% | 98%-99% | 1195 | 98% (7533) | 16x moderate | - | detected share 98.6% (98%-99%) since Nov 2024. Entry flags: amplicon_measured_not_published, orientation_inferred. |
| `Astroviridae_RdRp_Atkins_2008_round1` | active | 98.7% | 98%-99% | 682 | 96% (2372) | 32768x severe | - | detected share 98.7% (98%-99%) since Nov 2024. 29 patent records excluded. |
| `Chordopoxvirinae_POL_McAloose_2016` | active | 98.7% | 98%-99% | 5862 | 97% (9695) | 4x negligible | - | detected share 98.7% (98%-99%) since Nov 2024. Entry flags: oligos_from_secondary_source, oligos_modified, pairing_is_curator_reading. 1439 patent records excluded. |
| `Morbillivirus_canis_P_Halecker_2021_Mix7` | active | 98.8% | 94%-100% | 85 | 92% (288) | 16x moderate | - | detected share 98.8% (94%-100%) since Nov 2024. 61 patent records excluded. |
| `Helicobacter_16S_Fox_1998_C98` | active | 99.0% | 95%-100% | 102 | 91% (1049) | 1x negligible | - | detected share 99.0% (95%-100%) since Nov 2024. Entry flags: shares_oligos_with_sibling. 1 patent records excluded. |
| `Filoviridae_L_Zhai_2007_Filo_U12683_A` | active | 99.1% | 95%-100% | 110 | 99% (3817) | 2x negligible | - | detected share 99.1% (95%-100%) since Nov 2024. Entry flags: pairing_is_curator_reading. 85 patent records excluded. |
| `Enterovirus_VP3_VP1_Nix_2006_round1` | active | 99.1% | 98%-99% | 1222 | 96% (8093) | 64x moderate | - | detected share 99.1% (98%-99%) since Nov 2024. Entry flags: amplicon_disagrees_with_paper. 40 out-of-scope records excluded. |
| `Simian_immunodeficiency_virus_pol_Keele_2009_PTS_spol_F1` | active | 99.1% | 97%-100% | 226 | 55% (4988) | 4x negligible | - | detected share 99.1% (97%-100%) since Nov 2024. |
| `Lyssavirus_N_Vazquez-Moron_2006_round2` | active | 99.2% | 99%-99% | 2045 | 98% (11904) | 96x moderate | - | detected share 99.2% (99%-99%) since Nov 2024. 47 patent records excluded. |
| `Simian_immunodeficiency_virus_pol_Clewley_1998_round2` | active | 99.6% | 98%-100% | 226 | 99% (3785) | 576x high | - | detected share 99.6% (98%-100%) since Nov 2024. Entry flags: orientation_inferred. |
| `Alphavirus_nsP4_Sanchez-Seco_2001_round1` | active | 99.7% | 99%-100% | 3780 | 95% (4716) | 512x high | - | detected share 99.7% (99%-100%) since Nov 2024. Entry flags: oligos_modified. 339 patent records excluded. |
| `Batrachochytrium_dendrobatidis_ITS1_5_8S_Annis_2004` | active | 100.0% | 82%-100% | 17 | 88% (163) | 1x negligible | - | detected share 100.0% (82%-100%) since Nov 2024. Entry flags: orientation_inferred. 2 patent records excluded. |
| `Batrachochytrium_dendrobatidis_ITS1_5_8S_Boyle_2004` | active | 100.0% | 82%-100% | 17 | 97% (162) | 1x negligible | - | detected share 100.0% (82%-100%) since Nov 2024. Entry flags: amplicon_measured_not_published. 2 patent records excluded. |
| `Bornaviridae_N_Zimmermann_1994_round1` | active | 100.0% | 98%-100% | 165 | 98% (147) | 1x negligible | - | detected share 100.0% (98%-100%) since Nov 2023 (window widened to 36 months to reach 15 evaluable records). Entry flags: nested_protocol. 1005 out-of-scope records excluded. 12 patent records excluded. |
| `Chlamydia_psittaci_16S_Messmer_1997_round2` | active | 100.0% | 80%-100% | 15 | 100% (147) | 1x negligible | - | detected share 100.0% (80%-100%) since Nov 2024. |
| `Encephalitozoon_18S_Muller_1999` | active | 100.0% | 90%-100% | 33 | 87% (83) | 1x negligible | - | detected share 100.0% (90%-100%) since Nov 2022 (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published. 4 patent records excluded. |
| `Entamoeba_18S_McFarland_2021` | draft | 100.0% | 95%-100% | 80 | 100% (134) | 288x high | - | detected share 100.0% (95%-100%) since Nov 2022 (window widened to 48 months to reach 15 evaluable records). Entry flags: oligos_modified. |
| `Filoviridae_L_Zhai_2007_MOD_FWD` | active | 100.0% | 91%-100% | 40 | 99% (3537) | 288x high | - | detected share 100.0% (91%-100%) since Nov 2024. Entry flags: oligos_modified. 85 patent records excluded. |
| `Henipavirus_nipahense_N_Chua_2000` | active | 100.0% | 86%-100% | 23 | 98% (275) | 1x negligible | - | detected share 100.0% (86%-100%) since Nov 2024. Entry flags: oligos_from_secondary_source, primer_site_polymorphic. 13 patent records excluded. |
| `Henipavirus_nipahense_N_Wacharapluesadee_2007` | active | 100.0% | 85%-100% | 21 | 97% (186) | 1x negligible | - | detected share 100.0% (85%-100%) since Nov 2024. 13 patent records excluded. |
| `Morbillivirus_canis_H_Muller_2011_Mueller_4F` | active | 100.0% | 96%-100% | 86 | 99% (277) | 1x negligible | - | detected share 100.0% (96%-100%) since Nov 2024. Entry flags: pairing_is_curator_reading. 61 patent records excluded. |
| `Mycobacterium_tuberculosis_complex_IS6110_Boniotti_2014` | active | 100.0% | 99%-100% | 274 | 100% (3738) | 1x negligible | - | detected share 100.0% (99%-100%) since Nov 2024. 6 patent records excluded. |
| `Mycoplasmoides_gallisepticum_parE_Kang_2023` | active | 100.0% | 88%-100% | 27 | 100% (68) | 1x negligible | - | detected share 100.0% (88%-100%) since Nov 2023 (window widened to 36 months to reach 15 evaluable records). |
| `Ophidiomyces_ophidiicola_targetD_Haynes_2023` | active | 100.0% | 95%-100% | 81 | - | 1x negligible | - | detected share 100.0% (95%-100%) since Nov 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: chemistry_detail_missing, pairing_is_curator_reading, retrieval_scope_incomplete, thin_evidence. 111 chance-pair records excluded (drift.chance_pair_test). |
| `Orf_virus_RPO147_Zhao_2013` | draft | 100.0% | 88%-100% | 27 | 100% (56) | 1x negligible | - | detected share 100.0% (88%-100%) since Nov 2024. Entry flags: amplicon_measured_not_published, chemistry_detail_missing. 307 out-of-scope records excluded. 51 patent records excluded. 76 chance-pair records excluded (drift.chance_pair_test). |
| `Orthobornavirus_XP_Sigrist_2021_aquatic` | active | 100.0% | 82%-100% | 18 | 100% (21) | 16x moderate | - | detected share 100.0% (82%-100%) since Nov 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: chemistry_detail_missing, oligos_read_from_figure. 1278 out-of-scope records excluded. |
| `Orthobornavirus_XP_Sigrist_2021_psittacine` | active | 100.0% | 90%-100% | 35 | 98% (59) | 64x moderate | - | detected share 100.0% (90%-100%) since Nov 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_read_from_figure. 721 out-of-scope records excluded. |
| `Ranavirus_MCP_Johnson_2008` | active | 100.0% | 95%-100% | 76 | 96% (250) | 1x negligible | - | detected share 100.0% (95%-100%) since Nov 2024. Entry flags: amplicon_disagrees_with_paper, oligos_from_secondary_source. |
| `Salmonella_enterica_invA_Rahn_1992` | active | 100.0% | 93%-100% | 55 | 98% (409) | 1x negligible | - | detected share 100.0% (93%-100%) since Nov 2024. Entry flags: oligos_not_in_cited_paper, orientation_inferred. |
| `Shigella_ipaH_Sethabutr_1993` | active | 100.0% | 91%-100% | 38 | 98% (168) | 1x negligible | - | detected share 100.0% (91%-100%) since Nov 2024. Entry flags: orientation_inferred. |
| `Simian_immunodeficiency_virus_pol_Clewley_1998_round1` | active | 100.0% | 98%-100% | 226 | 83% (4495) | 768x high | - | detected share 100.0% (98%-100%) since Nov 2024. Entry flags: orientation_inferred. |
| `Simian_immunodeficiency_virus_pol_Takehisa_2009_HahnF1` | draft | 100.0% | 98%-100% | 226 | 99% (4991) | 27648x severe | - | detected share 100.0% (98%-100%) since Nov 2024. |
| `Trichomonas_gallinae_18S_Renteria-Solis_2020` | active | 100.0% | 85%-100% | 21 | 100% (46) | 1x negligible | - | detected share 100.0% (85%-100%) since Nov 2022 (window widened to 48 months to reach 15 evaluable records). |
| `Vairimorpha_ceranae_18S_Martin-Hernandez_2007` | active | 100.0% | 88%-100% | 28 | 79% (849) | 1x negligible | - | detected share 100.0% (88%-100%) since Nov 2024. Entry flags: oligos_read_from_figure. |
| `Vibrio_coralliilyticus_vcpA_Wilson_2013_vcpAF` | active | 100.0% | 81%-100% | 16 | 100% (19) | 1x negligible | - | detected share 100.0% (81%-100%) since Nov 2022 (window widened to 48 months to reach 15 evaluable records). Entry flags: amplicon_disagrees_with_paper, oligos_from_secondary_source. |
| `Vibrio_coralliilyticus_vcpA_Wilson_2013_vcpARTF` | active | 100.0% | 81%-100% | 16 | 89% (19) | 1x negligible | - | detected share 100.0% (81%-100%) since Nov 2022 (window widened to 48 months to reach 15 evaluable records). |
| `Yersinia_enterocolitica_yst_Ibrahim_1992` | active | 100.0% | 80%-100% | 15 | 100% (22) | 1x negligible | - | detected share 100.0% (80%-100%) since Nov 2023 (window widened to 36 months to reach 15 evaluable records). Entry flags: amplicon_disagrees_with_paper, oligos_not_in_cited_paper, orientation_inferred. |
| `Yersinia_pseudotuberculosis_inv_Wang_1997` | active | 100.0% | 81%-100% | 16 | 100% (49) | 1x negligible | - | detected share 100.0% (81%-100%) since Nov 2022 (window widened to 48 months to reach 15 evaluable records). Entry flags: orientation_inferred. 2 patent records excluded. |

# Nested protocols

What a lab runs, rather than what a primer pair does. A nested protocol is scored on the records where EVERY round amplifies: round 2's template is round 1's product, not the deposit, so an inner pair that matches a record perfectly yields nothing when the outer reaction has already failed. Each round keeps its own status in the tables above, because a round can be run alone and either product reads on a gel; these rows are the different question of what the published protocol does. A protocol is named for the round it ends on, and a branch is several protocols -- one genus-level first round feeding three species-specific second rounds is three, with three targets. The scope is the intersection of the rounds, so a record only one round claims is out of scope rather than a failure. The threshold and the words are the assay ones.

## Declining (8) — protocols

| protocol | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Adenoviridae_hexon_Casas_2005_round2` | active | 83.3% | 81%-85% | 1389 | 84% (4142) | 8x negligible | unchecked | pooled share 83.3% has low coverage, but lineage Mastadenovirus caesari (3241411) (184 records) detects only 65.2% (58.1%-71.7%), down from 71.1% on 795 earlier records; lineage verdict overrides to declining. 333 patent records excluded. |
| `Coronaviridae_RdRp_Quan_2010_round2` | active | 45.0% | 43%-47% | 1569 | 46% (5177) | 12288x severe | unchecked | pooled share 45.0% has low coverage, but lineage Alphacoronavirus chicagoense (3433756) (171 records) detects only 0.0% (0.0%-2.2%), down from 21.4% on 168 earlier records; lineage verdict overrides to declining. 14 out-of-scope records excluded. |
| `Enterovirus_5UTR_VP4_VP2_Wray_2016_round2` | draft | 52.6% | 50%-55% | 1184 | 84% (7444) | 32x moderate | unchecked | detected share 52.6% (50%-55%) since Nov 2024, upper bound below the 90% threshold; change from baseline -34% to -28%; separately, lineage Enterovirus geswini (3428509) (70 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: amplicon_measured_not_published, orientation_inferred. |
| `Enterovirus_VP3_VP1_Nix_2006_round2` | active | 14.3% | 12%-17% | 909 | 11% (5934) | 16384x severe | unchecked | pooled share 14.3% has low coverage, but lineage Enterovirus betacoxsackie (3428502) (146 records) detects 61.0% (52.9%-68.5%); lineage verdict overrides to declining. Entry flags: amplicon_disagrees_with_paper, amplicon_measured_not_published. |
| `Orthoflavivirus_NS5_Scaramozzino_2001_round2` | active | 24.3% | 23%-25% | 9420 | 33% (24475) | 648x high | unchecked | pooled share 24.3% has low coverage, but lineage Orthoflavivirus usutuense (3048443) (429 records) detects only 0.0% (0.0%-0.9%), down from 12.3% on 592 earlier records; lineage verdict overrides to declining. Entry flags: amplicon_measured_not_published, oligos_from_secondary_source. |
| `Orthoherpesviridae_terminase_Chmielewicz_2001_round2` | active | 72.2% | 67%-77% | 284 | 82% (2303) | 128x moderate | fails: change | detected share 72.2% (67%-77%) since Nov 2024, upper bound below the 90% threshold; change from baseline -16% to -5%; separately, lineage Varicellovirus humanalpha3 (3050294) (54 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: orientation_inferred. 1 out-of-scope records excluded. |
| `Orthoreovirus_RdRp_Landolfi_2010_round2` | active | 18.3% | 15%-23% | 356 | 61% (627) | 147456x severe | holds | detected share 18.3% (15%-23%) since Nov 2024, upper bound below the 90% threshold; change from baseline -48% to -37%. Entry flags: conditions_not_printed, pairing_is_curator_reading. 4 patent records excluded. |
| `Rhabdoviridae_L_Bourhy_2005_round2` | active | 71.7% | 69%-74% | 1263 | 77% (5238) | 36864x severe | unchecked | pooled share 71.7% has low coverage, but lineage Lyssavirus rabies (11292) (945 records) detects 86.9% (84.6%-88.9%), down from 94.9% on 3667 earlier records; lineage verdict overrides to declining. Entry flags: oligos_from_secondary_source. 443 out-of-scope records excluded. |

## Low Coverage (5) — protocols

| protocol | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Astroviridae_RdRp_Chu_2008_round2` | active | 26.2% | 23%-30% | 672 | 42% (2217) | 1536x high | unchecked | detected share 26.2% (23%-30%) since Nov 2024, upper bound below the 90% threshold; change from baseline -19% to -12% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 42%); lineage Mamastrovirus suisencephalomyelitidis (3703181) (35 records) detects only 8.6%, but neither it nor the pooled share ever cleared the threshold, so there is no fall to call a decline. Entry flags: amplicon_measured_not_published, nested_protocol. 12 patent records excluded. |
| `Chlamydia_trachomatis_16S_Messmer_1997_round2` | active | 0.0% | 0%-9% | 39 | 0% (323) | 1x negligible | fails: too_few | detected share 0.0% (0%-9%) since Nov 2024, upper bound below the 90% threshold; change from baseline -1% to +9% (no measurable fall from a baseline of 0%). Entry flags: primer_site_polymorphic, scope_narrower_than_taxid. 1 patent records excluded. |
| `Circoviridae_Rep_Mankertz_2000_round2` | active | 26.9% | 23%-31% | 499 | 34% (6937) | 1536x high | unchecked | detected share 26.9% (23%-31%) since Nov 2024, upper bound below the 90% threshold; change from baseline -11% to -3% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 34%); separately, lineage Circovirus canine (3047721) (36 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: orientation_inferred. 70 patent records excluded. |
| `Paramyxoviridae_L_Tong_2008_round2` | active | 61.9% | 60%-63% | 3958 | 10% (4876) | 384x high | unchecked | detected share 61.9% (60%-63%) since Nov 2024, upper bound below the 90% threshold; change from baseline +50% to +53% (rose from a baseline of 10%); separately, lineage Morbillivirus canis (3052342) (83 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. |
| `Polyomaviridae_VP1_Johne_2005_round2` | active | 0.8% | 0.3%-2% | 642 | 0.1% (1668) | 1536x high | unchecked | detected share 0.8% (0.3%-2%) since Nov 2024, upper bound below the 90% threshold; change from baseline +0.2% to +2% (rose from a baseline of 0.1%); separately, lineage Betapolyomavirus hominis (1891762) (548 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift. Entry flags: amplicon_measured_not_published, nested_protocol. 6 patent records excluded. |

## Insufficient Data (5) — protocols

| protocol | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Chlamydia_pneumoniae_16S_Messmer_1997_round2` | active | 100.0% | 51%-100% | 4 | 100% (9) | 1x negligible | - | 4 evaluable records since Nov 2024, below the minimum of 15; the detected share is 100% (51%-100%), too wide to act on. Entry flags: primer_site_polymorphic, scope_narrower_than_taxid. |
| `Cryptosporidium_18S_Xiao_1999_round2` | active | 100.0% | 78%-100% | 14 | 93% (131) | 1x negligible | - | 14 evaluable records since Nov 2021, below the minimum of 15; the detected share is 100% (78%-100%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: oligos_modified. |
| `Elephant_endotheliotropic_herpesvirus_3_and_4_POL_Latimer_2012_round3` | active | 100.0% | 34%-100% | 2 | 100% (7) | 1x negligible | - | 2 evaluable records since Nov 2024, below the minimum of 15; the detected share is 100% (34%-100%), too wide to act on. |
| `Ferlavirus_HN_Ahne_1999_round2` | active | 66.7% | 30%-90% | 6 | 95% (22) | 1x negligible | - | 6 evaluable records since Nov 2021, below the minimum of 15; the detected share is 67% (30%-90%), too wide to act on (window widened to 60 months to reach 15 evaluable records). Entry flags: amplicon_measured_not_published. |
| `Proboscivirus_POL_Latimer_2012_round2` | active | 50.0% | 25%-75% | 12 | 65% (20) | 1024x high | - | 12 evaluable records since Nov 2021, below the minimum of 15; the detected share is 50% (25%-75%), too wide to act on (window widened to 60 months to reach 15 evaluable records). |

## No Recent Data (2) — protocols

| protocol | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Elephant_endotheliotropic_herpesvirus_5_POL_Latimer_2012_round2` | active | - | - | 0 | 100% (9) | 1x negligible | - | no evaluable records deposited since Nov 2024. |
| `Elephant_endotheliotropic_herpesvirus_5_POL_Latimer_2012_round2B` | active | - | - | 0 | 100% (9) | 1x negligible | - | no evaluable records deposited since Nov 2024. |

## Stable (11) — protocols

| protocol | entry | detected (recent) | 95% CI | evaluable | baseline (n) | degeneracy | duplication | note |
|---|---|---|---|---|---|---|---|---|
| `Adenoviridae_POL_Wellehan_2004_round2` | active | 98.8% | 98%-99% | 1165 | 99% (3464) | 10616832x severe | - | detected share 98.8% (98%-99%) since Nov 2024. Entry flags: amplicon_multimodal. 37 out-of-scope records excluded. 294 patent records excluded. |
| `Alphavirus_nsP4_Sanchez-Seco_2001_round2` | active | 99.0% | 99%-99% | 3771 | 90% (4450) | 256x high | - | detected share 99.0% (99%-99%) since Nov 2024. Entry flags: oligos_modified. 145 patent records excluded. |
| `Astroviridae_RdRp_Atkins_2008_round2` | active | 97.4% | 96%-98% | 681 | 95% (2367) | 131072x severe | - | detected share 97.4% (96%-98%) since Nov 2024. Entry flags: nested_protocol. 12 patent records excluded. |
| `Bocaparvovirus_NS1_Kapoor_2010_round2` | active | 95.4% | 93%-97% | 414 | 68% (1523) | 2048x high | - | detected share 95.4% (93%-97%) since Nov 2024. 4 patent records excluded. |
| `Chlamydia_psittaci_16S_Messmer_1997_round2` | active | 100.0% | 85%-100% | 21 | 100% (91) | 1x negligible | - | detected share 100.0% (85%-100%) since Nov 2021 (window widened to 60 months to reach 15 evaluable records). Entry flags: primer_site_polymorphic, scope_narrower_than_taxid. |
| `Cytomegalovirus_gB_Deckers_2009_round2` | active | 90.6% | 76%-97% | 32 | 96% (521) | 32x moderate | - | detected share 90.6% (76%-97%) since Nov 2024. Entry flags: citation_is_indirect. 36 patent records excluded. |
| `Cytomegalovirus_gB_Prepens_2007_round2` | active | 96.9% | 84%-99% | 32 | 91% (643) | 8192x severe | - | detected share 96.9% (84%-99%) since Nov 2024. Entry flags: amplicon_measured_not_published. 57 patent records excluded. |
| `Mastadenovirus_POL_Roy_2009_round2` | active | 95.0% | 94%-96% | 1070 | 83% (2864) | 1x negligible | - | detected share 95.0% (94%-96%) since Nov 2024. 309 patent records excluded. |
| `Orthohantavirus_S_Mangombi_2021_round2` | draft | 97.7% | 96%-99% | 395 | 98% (3748) | 5184x severe | - | detected share 97.7% (96%-99%) since Nov 2024. Entry flags: nested_protocol. 24 patent records excluded. |
| `Phlebovirus_L_Sanchez-Seco_2003_round2` | active | 96.3% | 87%-99% | 54 | 94% (215) | 8192x severe | - | detected share 96.3% (87%-99%) since Nov 2024. |
| `Simian_immunodeficiency_virus_pol_Clewley_1998_round2` | active | 99.6% | 98%-100% | 226 | 99% (3739) | 576x high | - | detected share 99.6% (98%-100%) since Nov 2024. Entry flags: orientation_inferred. |

## Not scoreable (17)

These assays were screened, and their records still count in the nested,
degeneracy and per-lineage tables, but their entry carries a review item that
means a status would not be a statement about the assay: either an open question
a human has to answer, or a readout this pipeline cannot model. No status is shown
for them, including the one they would otherwise have had.

| assay | entry | why | note |
|---|---|---|---|
| `Bornaviridae_N_Zimmermann_1994_round2` | draft | `oligo_sequence_uncertain` | the printed BornaNestF matches 0 of 1,516 records, differing from every one at the 3'-terminal base; whether the 1994 scan is right has not been settled, and no verdict publishes until it is |
|  |  | `amplicon_size_unresolved` | no product size is declared |
| `Francisella_tularensis_tul4_Long_1993` | draft | `oligo_sequence_uncertain` | the probe is omitted: the OCR of its sequence was not reliable enough to enter |
| `Leptospira_flaB_Hsu_2013` | draft | `not_validated` |  |
| `Lyssavirus_N_Vazquez-Moron_2006_round1` | draft | `not_validated` |  |
| `Morbillivirus_canis_P_Geiselhardt_2022` | draft | `target_scope_unresolved` | also detects PDV (Morbillivirus phocae, txid3052347) while the taxid here is CDV only; decide whether a PDV-scoped entry is wanted |
| `Morbillivirus_canis_P_Halecker_2021_Mix3` | draft | `duplicate_entry_unresolved` | overlaps Morbillivirus_canis_P_Scagliarini_2007: shares CDV3-R, and the forward and probe are degenerate modifications of it; decide whether both entries stay |
| `Mycobacterium_16S_Hermes_2018` | draft | `citation_unresolved` | oligos come from an uncitable source (Nieter, 2016) |
| `Mycobacterium_tuberculosis_complex_IS1081_Hermes_2018` | draft | `citation_unresolved` | oligos come from an uncitable source (anonymous, 2017) |
| `Mycobacterium_tuberculosis_complex_helicase_Hermes_2018` | draft | `citation_unresolved` | oligos come from an uncitable source (anonymous, 2017) |
| `Mycoplasma_16S23S_ITS_Rebelo_2011_16_23_F1` | draft | `oligo_source_unresolved` | the partner primer has no attributed source |
| `Mycoplasma_16S23S_ITS_Rebelo_2011_16_23_F3` | draft | `oligo_source_unresolved` | the partner primer has no attributed source |
| `Mycoplasma_16S_vanKuppeveld_1992` | draft | `do_not_use` |  |
| `Orthobunyavirus_S_Briese_2007_Cac_2_FWD` | draft | `target_scope_unresolved` | the source never states what this assay is meant to cover |
| `Orthobunyavirus_S_Steyn_2020` | draft | `amplicon_size_unresolved` | published 152 bp against a printed 152-304 span that is 153 bp inclusive; to be measured, not argued |
| `Orthoherpesviridae_POL_VanDevanter_1996_round1` | draft | `duplicate_entry_unresolved` | whether the DFA variant and the PREDICT version are one entry or two is unresolved |
| `Orthopoxvirus_ATI_Meyer_1997` | draft | `not_screenable` | identification is by product size plus an XbaI digest, which the screen cannot model |
|  |  | `oligo_source_unresolved` | a Meyer 1994 origin is suspected but not established |
| `Ranavirus_micropterus1_MCP_Li_2025` | active | `not_screenable` | the chemistry is RPA; the penalties are calibrated on PCR |

## Detail for flagged assays

**Duplication check:** 26 of 74 flagged assays still hold when duplicated records are discounted (each distinct binding-site footprint counted once, and the sample size cut to the number of footprints). The note on each assay that did not hold says which test it failed.

### `Simian_immunodeficiency_virus_pol_Keele_2009_PTS_spol_F2`

Simian immunodeficiency virus — pol (Keele 2009, PTS spol F2)  
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
| 2001 | 8 | 16 | 50% |
| 2002 | 6 | 9 | 67% |
| 2003 | 4 | 7 | 57% |
| 2004 | 0 | 29 | 0% |
| 2005 | 0 | 4 | 0% |
| 2006 | 4 | 11 | 36% |
| 2007 | 5 | 6 | 83% |
| 2008 | 2 | 7 | 29% |
| 2009 | 5 | 46 | 11% |
| 2010 | 3 | 22 | 14% |
| 2011 | 6 | 7 | 86% |
| 2012 | 4 | 6 | 67% |
| 2013 | 1 | 660 | 0.2% |
| 2014 | 25 | 54 | 46% |
| 2015 | 6 | 6 | 100% |
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

*trend over deposit year: falling, z = -16.27, two-sided p = 1.53e-59 across 35 years and 3847 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.01, two-sided p = 0.99 across 35 years and 130 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Duplication check:** 224 recent records share 2 distinct footprints (112.0 per footprint), of which 223 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 2 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 2 and 73 independent observations the fall from baseline is -15% to +59%, which no longer excludes zero.

**Denominator:** 3847 of 8252 screened records are evaluable (46.6%); 4405 are not. Every share above is taken over the evaluable ones.

Excluded: 4405 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3467 no_site, 683 chance_anchor, 251 truncated, 4 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 3513 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2948 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 519 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Simian_immunodeficiency_virus_pol_Takehisa_2009_HahnF2`

**Lineage override:** pooled status was low coverage.  
Simian immunodeficiency virus — pol (Takehisa 2009, HahnF2)  
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
| 2002 | 2 | 7 | 29% |
| 2003 | 2 | 10 | 20% |
| 2004 | 0 | 28 | 0% |
| 2005 | 0 | 14 | 0% |
| 2006 | 4 | 20 | 20% |
| 2007 | 5 | 8 | 62% |
| 2008 | 2 | 9 | 22% |
| 2009 | 5 | 1244 | 0.4% |
| 2010 | 1 | 863 | 0.1% |
| 2011 | 4 | 7 | 57% |
| 2012 | 4 | 11 | 36% |
| 2013 | 1 | 39 | 3% |
| 2014 | 0 | 7 | 0% |
| 2015 | 9 | 10 | 90% |
| 2016 | 0 | 87 | 0% |
| 2017 | 169 | 173 | 98% |
| 2018 | 0 | 1 | 0% |
| 2019 | 0 | 384 | 0% |
| 2020 | 0 | 155 | 0% |
| 2021 | 1 | 99 | 1% |
| 2022 | 1 | 3 | 33% |
| 2023 | 0 | 3 | 0% |
| 2024 | 0 | 1854 | 0% |
| 2025 | 0 | 206 | 0% |
| 2026 | 0 | 20 | 0% |

*trend over deposit year: falling, z = -2.54, two-sided p = 0.011 across 36 years and 5299 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.73, two-sided p = 0.462 across 36 years and 202 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 0.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 226 recent records share 3 distinct footprints (75.3 per footprint). This flag does not hold up: only 3 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 3 and 117 independent observations the fall from baseline is -10% to +52%, which no longer excludes zero.

**Denominator:** 5299 of 8252 screened records are evaluable (64.2%); 2953 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 2952 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1454 truncated, 1423 no_site, 74 chance_anchor, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 269 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 6 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1417 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Aparavirus_apisacutum_capsid_Rossi_2024`

Aparavirus apisacutum — capsid protein (Rossi 2024)  
Designed 2024, doi:10.3390/microorganisms12061105  
**Degeneracy:** 4608-fold degenerate (288-fold primers x 16-fold probe); ~12 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1999 | 1 | 1 | 100% |
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

*trend over deposit year: falling, z = -5.67, two-sided p = 1.46e-08 across 20 years and 124 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.47, two-sided p = 0.0135 across 20 years and 39 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Patent records:** 8 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 18 recent records share 8 distinct footprints (2.2 per footprint), of which 1 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 8 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 124 of 983 screened records are evaluable (12.6%); 859 are not. Every share above is taken over the evaluable ones.

Excluded: 859 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 851 no_site, 8 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 2 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 851 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Influenza_A_virus_M_Spackman_2002`

Influenza A virus — M (matrix) (Spackman 2002)  
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
| 2006 | 619 | 1357 | 46% |
| 2007 | 316 | 777 | 41% |
| 2008 | 399 | 626 | 64% |
| 2009 | 740 | 1772 | 42% |
| 2010 | 669 | 2192 | 31% |
| 2011 | 159 | 306 | 52% |
| 2012 | 127 | 537 | 24% |
| 2013 | 262 | 849 | 31% |
| 2014 | 352 | 1216 | 29% |
| 2015 | 445 | 872 | 51% |
| 2016 | 775 | 4246 | 18% |
| 2017 | 1207 | 2055 | 59% |
| 2018 | 1567 | 5180 | 30% |
| 2019 | 918 | 7429 | 12% |
| 2020 | 1570 | 5221 | 30% |
| 2021 | 921 | 2050 | 45% |
| 2022 | 449 | 5435 | 8% |
| 2023 | 316 | 8063 | 4% |
| 2024 | 772 | 10126 | 8% |
| 2025 | 1270 | 16674 | 8% |
| 2026 | 496 | 12487 | 4% |

*trend over deposit year: falling, z = -91.68, two-sided p = 0 across 37 years and 90301 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.51, two-sided p = 0.608 across 37 years and 1959 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 17 lineages: mu = 5.6%, phi = 0.4 (intraclass correlation 0.698); worst lineage after shrinkage H3 at 0.0% (0.0%-0.0%, raw 0.0% on 907); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Duplication check:** 30380 recent records share 158 distinct footprints (192.3 per footprint), of which 39 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 158 independent observations (one per footprint) the interval around the 6% detected share is 4%-11%, and counting each footprint once, 19 of 158 footprints amplify (12%; interval 8%-18%); each is below the 90% threshold, and the fall from baseline (-19% to -9%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 90301 of 184887 screened records are evaluable (48.8%); 94586 are not. Every share above is taken over the evaluable ones.

Excluded: 7 indeterminate, 94579 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 93302 truncated, 1171 no_site, 103 chance_anchor, 3 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 673 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1171 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Monkeypox_virus_N3R_Kulesh_2004`

**Lineage override:** pooled status was low coverage.  
Monkeypox virus — N3R (Kulesh 2004)  
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
| 2026 | 361 | 2601 | 14% |

*trend over deposit year: rising, z = +11.19, two-sided p = 4.7e-29 across 16 years and 12807 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.90, two-sided p = 0.0576 across 16 years and 48 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 26.4%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 5 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 4535 recent records share 6 distinct footprints (755.8 per footprint), of which 2118 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 6 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 6 and 12 independent observations the fall from baseline is -22% to +48%, which no longer excludes zero.

**Denominator:** 12807 of 14206 screened records are evaluable (90.2%); 1399 are not. Every share above is taken over the evaluable ones.

Excluded: 13 indeterminate, 1386 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 747 no_site, 618 no_pair, 21 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 2793 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 746 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Enterovirus_VP3_VP1_Nix_2006_round2`

**Lineage override:** pooled status was low coverage.  
Enterovirus — VP3-VP1 (Nix 2006), nested round 2  
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
| 2012 | 281 | 1952 | 14% |
| 2013 | 327 | 2137 | 15% |
| 2014 | 213 | 2934 | 7% |
| 2015 | 310 | 2530 | 12% |
| 2016 | 138 | 1789 | 8% |
| 2017 | 86 | 2477 | 3% |
| 2018 | 154 | 3027 | 5% |
| 2019 | 700 | 2462 | 28% |
| 2020 | 289 | 1997 | 14% |
| 2021 | 77 | 2701 | 3% |
| 2022 | 164 | 1873 | 9% |
| 2023 | 679 | 2674 | 25% |
| 2024 | 411 | 1931 | 21% |
| 2025 | 407 | 2337 | 17% |
| 2026 | 369 | 2029 | 18% |

*trend over deposit year: rising, z = +9.29, two-sided p = 1.48e-20 across 42 years and 40570 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.14, two-sided p = 0.885 across 42 years and 4896 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 3 lineages: mu = 26.2%, phi = 0.8 (intraclass correlation 0.546); worst lineage after shrinkage Enterovirus alphacoxsackie (3428500) at 0.2% (0.1%-0.5%, raw 0.2% on 1916); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 40 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Enterovirus E11 (3569727) |  | 13 | 13 | 13 | 100% |
| Enterovirus PV1 (3569731) |  | 1 | 1 | 1 | 100% |
| Enterovirus E9 (3569730) |  | 1 | 1 | 2 | 50% |
| Enterovirus E13 (3569728) |  | 0 | 0 | 16 | 0% |
| Enterovirus E6 (3569729) |  | 0 | 0 | 7 | 0% |


**Duplication check:** 4639 recent records share 307 distinct footprints (15.1 per footprint), of which 1430 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 307 and 2141 independent observations the fall from baseline is +1% to +10%, which no longer excludes zero.

**Denominator:** 40570 of 73386 screened records are evaluable (55.3%); 32816 are not. Every share above is taken over the evaluable ones.

Excluded: 32816 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 25019 no_site, 5430 truncated, 2346 chance_anchor, 21 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 16347 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 307 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 24712 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Leucocytozoon_cytb_Hellgren_2004`

**Lineage override:** pooled status was low coverage.  
Leucocytozoon — cytochrome b (Hellgren 2004)  
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
| 2017 | 14 | 33 | 42% |
| 2018 | 18 | 24 | 75% |
| 2019 | 0 | 698 | 0% |
| 2020 | 63 | 67 | 94% |
| 2021 | 0 | 69 | 0% |
| 2022 | 3 | 34 | 9% |
| 2023 | 17 | 31 | 55% |
| 2024 | 45 | 55 | 82% |
| 2025 | 20 | 76 | 26% |
| 2026 | 9 | 37 | 24% |

*trend over deposit year: rising, z = +3.06, two-sided p = 0.00222 across 22 years and 1423 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.73, two-sided p = 0.463 across 22 years and 169 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 34.1%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 114 recent records share 23 distinct footprints (5.0 per footprint), of which 26 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 23 and 106 independent observations the fall from baseline is -5% to +32%, which no longer excludes zero.

**Denominator:** 1423 of 7910 screened records are evaluable (18.0%); 6487 are not. Every share above is taken over the evaluable ones.

Excluded: 6487 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 6297 no_site, 177 truncated, 13 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 1083 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 42 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 6255 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthoflavivirus_NS5_Scaramozzino_2001_round2`

**Lineage override:** pooled status was low coverage.  
Orthoflavivirus — NS5 (Scaramozzino 2001), nested round 2  
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
| 1997 | 28 | 70 | 40% |
| 1998 | 3 | 22 | 14% |
| 1999 | 11 | 24 | 46% |
| 2000 | 11 | 33 | 33% |
| 2001 | 11 | 31 | 35% |
| 2002 | 17 | 32 | 53% |
| 2003 | 23 | 37 | 62% |
| 2004 | 78 | 99 | 79% |
| 2005 | 187 | 240 | 78% |
| 2006 | 82 | 120 | 68% |
| 2007 | 119 | 218 | 55% |
| 2008 | 137 | 1015 | 13% |
| 2009 | 339 | 1331 | 25% |
| 2010 | 292 | 425 | 69% |
| 2011 | 425 | 624 | 68% |
| 2012 | 107 | 328 | 33% |
| 2013 | 170 | 306 | 56% |
| 2014 | 514 | 823 | 62% |
| 2015 | 386 | 571 | 68% |
| 2016 | 673 | 1054 | 64% |
| 2017 | 449 | 1463 | 31% |
| 2018 | 337 | 1118 | 30% |
| 2019 | 207 | 717 | 29% |
| 2020 | 427 | 1836 | 23% |
| 2021 | 1030 | 3363 | 31% |
| 2022 | 453 | 1550 | 29% |
| 2023 | 1153 | 3864 | 30% |
| 2024 | 1591 | 3992 | 40% |
| 2025 | 1646 | 3220 | 51% |
| 2026 | 821 | 5552 | 15% |

*trend over deposit year: falling, z = -20.90, two-sided p = 5.04e-97 across 40 years and 34116 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -3.41, two-sided p = 0.000662 across 40 years and 1505 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 10 lineages: mu = 30.7%, phi = 1.8 (intraclass correlation 0.363); worst lineage after shrinkage Orthoflavivirus zikaense (3048459) at 0.7% (0.0%-3.3%, raw 0.0% on 77); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 1 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Balclutha incisa flavivirus 1 (3140651) |  | 0 | 0 | 0 | 0% |


**Duplication check:** 9444 recent records share 143 distinct footprints (66.0 per footprint), of which 244 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 143 and 316 independent observations the fall from baseline is -15% to +3%, which no longer excludes zero.

**Denominator:** 34116 of 61192 screened records are evaluable (55.8%); 27076 are not. Every share above is taken over the evaluable ones.

Excluded: 16 indeterminate, 27060 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 25495 no_site, 1406 truncated, 159 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 494 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 14281 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 11214 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Monkeypox_virus_SNP183519_Huo_2022`

Monkeypox virus — SNP-typing locus at 183519-183542 of ON563414.2 (Huo 2022)  
Designed 2022, doi:10.1016/j.bsheal.2022.10.005  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 0 | 2 | 0% |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 0 | 2 | 0% |
| 2005 | 0 | 7 | 0% |
| 2007 | 0 | 0 | - |
| 2008 | 0 | 0 | - |
| 2009 | 0 | 0 | - |
| 2010 | 0 | 5 | 0% |
| 2011 | 0 | 2 | 0% |
| 2012 | 0 | 0 | - |
| 2013 | 0 | 1 | 0% |
| 2014 | 0 | 24 | 0% |
| 2015 | 0 | 11 | 0% |
| 2018 | 0 | 1 | 0% |
| 2019 | 0 | 8 | 0% |
| 2020 | 0 | 37 | 0% |
| 2022 | 3259 | 3332 | 98% |
| 2023 | 3087 | 3101 | 100% |
| 2024 | 1379 | 2047 | 67% |
| 2025 | 715 | 1893 | 38% |
| 2026 | 753 | 2737 | 28% |

*trend over deposit year: falling, z = -56.76, two-sided p = 0 across 16 years and 13210 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +1.87, two-sided p = 0.0621 across 16 years and 74 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 34.7%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 5 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 4822 recent records share 17 distinct footprints (283.6 per footprint), of which 45 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 17 independent observations (one per footprint) the interval around the 34% detected share is 17%-58%, and counting each footprint once, 2 of 17 footprints amplify (12%; interval 3%-34%); each is below the 90% threshold, and the fall from baseline (-75% to -25%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 13210 of 14206 screened records are evaluable (93.0%); 996 are not. Every share above is taken over the evaluable ones.

Excluded: 14 indeterminate, 982 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 976 no_site, 5 chance_anchor, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 75 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 424 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 552 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Circoviridae_Rep_Mankertz_2000_round1`

Circoviridae — Rep (Mankertz 2000), nested round 1  
Designed 2000, doi:10.1007/s007050070002  
**Degeneracy:** 1536-fold degenerate (1536-fold primers x 1-fold probe); each member is ~6.5e-04 of the reaction, ~11 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1996 | 1 | 1 | 100% |
| 1997 | 2 | 2 | 100% |
| 1998 | 12 | 15 | 80% |
| 1999 | 9 | 11 | 82% |
| 2000 | 30 | 33 | 91% |
| 2001 | 24 | 28 | 86% |
| 2002 | 31 | 42 | 74% |
| 2003 | 57 | 65 | 88% |
| 2004 | 60 | 70 | 86% |
| 2005 | 53 | 67 | 79% |
| 2006 | 51 | 68 | 75% |
| 2007 | 143 | 166 | 86% |
| 2008 | 132 | 146 | 90% |
| 2009 | 176 | 184 | 96% |
| 2010 | 123 | 131 | 94% |
| 2011 | 216 | 232 | 93% |
| 2012 | 132 | 157 | 84% |
| 2013 | 183 | 217 | 84% |
| 2014 | 253 | 324 | 78% |
| 2015 | 273 | 372 | 73% |
| 2016 | 326 | 406 | 80% |
| 2017 | 255 | 476 | 54% |
| 2018 | 279 | 575 | 49% |
| 2019 | 371 | 786 | 47% |
| 2020 | 152 | 419 | 36% |
| 2021 | 317 | 825 | 38% |
| 2022 | 419 | 732 | 57% |
| 2023 | 525 | 1177 | 45% |
| 2024 | 305 | 993 | 31% |
| 2025 | 150 | 353 | 42% |
| 2026 | 108 | 308 | 35% |

*trend over deposit year: falling, z = -33.40, two-sided p = 1.36e-244 across 31 years and 9381 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -8.96, two-sided p = 3.2e-19 across 31 years and 910 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 3 lineages: mu = 69.4%, phi = 0.3 (intraclass correlation 0.786); worst lineage after shrinkage Circovirus goose (3047842) at 0.3% (0.0%-2.3%, raw 0.0% on 63); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 222 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 678 recent records share 70 distinct footprints (9.7 per footprint), of which 268 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 70 independent observations (one per footprint) the interval around the 39% detected share is 28%-51%, and counting each footprint once, 8 of 70 footprints amplify (11%; interval 6%-21%); each is below the 90% threshold, and the fall from baseline (-29% to -5%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 9381 of 24095 screened records are evaluable (38.9%); 14714 are not. Every share above is taken over the evaluable ones.

Excluded: 6 indeterminate, 14708 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 13539 no_site, 940 truncated, 135 chance_anchor, 94 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 2997 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 13539 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Mycoplasma_16S23S_ITS_Rebelo_2011_Myco16_23S_F`

Mycoplasma — 16S-23S intergenic spacer (Rebelo 2011, Myco16 23S F)  
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
| 2016 | 1 | 13 | 8% |
| 2017 | 4 | 5 | 80% |
| 2018 | 23 | 33 | 70% |
| 2019 | 34 | 91 | 37% |
| 2020 | 16 | 50 | 32% |
| 2021 | 24 | 43 | 56% |
| 2022 | 21 | 46 | 46% |
| 2023 | 9 | 43 | 21% |
| 2024 | 41 | 43 | 95% |
| 2025 | 32 | 106 | 30% |
| 2026 | 22 | 30 | 73% |

*trend over deposit year: falling, z = -3.40, two-sided p = 0.000662 across 23 years and 661 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.99, two-sided p = 0.323 across 23 years and 144 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Per species** (product size names the species here, 354-767 bp, so the share above pools readouts that mean different things; Nov 2024 on, no assessability floor):

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
| Mycoplasma sp. 3686h (3699019) | - | 2 | 2 | 100% |
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

**Duplication check:** 138 recent records share 16 distinct footprints (8.6 per footprint), of which 80 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 16 and 58 independent observations the fall from baseline is -34% to +16%, which no longer excludes zero.

**Denominator:** 661 of 24191 screened records are evaluable (2.7%); 23530 are not. Every share above is taken over the evaluable ones.

Excluded: 23530 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 22553 no_site, 825 truncated, 152 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 316 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 4829 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 17724 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Coronaviridae_RdRp_Watanabe_2010`

**Lineage override:** pooled status was low coverage.  
Coronaviridae — RNA-dependent RNA polymerase (Watanabe 2010)  
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
| 2006 | 54 | 73 | 74% |
| 2007 | 25 | 38 | 66% |
| 2008 | 14 | 28 | 50% |
| 2009 | 51 | 111 | 46% |
| 2010 | 21 | 48 | 44% |
| 2011 | 14 | 86 | 16% |
| 2012 | 38 | 100 | 38% |
| 2013 | 97 | 209 | 46% |
| 2014 | 123 | 333 | 37% |
| 2015 | 304 | 477 | 64% |
| 2016 | 98 | 287 | 34% |
| 2017 | 361 | 656 | 55% |
| 2018 | 203 | 431 | 47% |
| 2019 | 132 | 313 | 42% |
| 2020 | 278 | 459 | 61% |
| 2021 | 190 | 457 | 42% |
| 2022 | 228 | 499 | 46% |
| 2023 | 558 | 1139 | 49% |
| 2024 | 270 | 468 | 58% |
| 2025 | 319 | 970 | 33% |
| 2026 | 313 | 630 | 50% |

*trend over deposit year: rising, z = +1.64, two-sided p = 0.1 across 30 years and 7999 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.26, two-sided p = 0.796 across 30 years and 1001 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 12 lineages: mu = 41.0%, phi = 0.2 (intraclass correlation 0.854); worst lineage after shrinkage Alphacoronavirus porci (3433789) at 0.0% (0.0%-0.2%, raw 0.0% on 306); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Duplication check:** 1749 recent records share 126 distinct footprints (13.9 per footprint), of which 19 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 126 and 302 independent observations the fall from baseline is -16% to +4%, which no longer excludes zero.

**Denominator:** 7999 of 25565 screened records are evaluable (31.3%); 17566 are not. Every share above is taken over the evaluable ones.

Excluded: 2 indeterminate, 17564 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 14531 no_site, 2750 truncated, 283 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 69 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 51 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 14480 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Monkeypox_virus_G2R_Li_2010_G2R_WA_F`

Monkeypox virus — TNF receptor (G2R), inverted terminal repeat (Li 2010, G2R WA F)  
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
| 2010 | 0 | 5 | 0% |
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
| 2026 | 775 | 2808 | 28% |

*trend over deposit year: falling, z = -53.48, two-sided p = 0 across 16 years and 12899 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.09, two-sided p = 0.927 across 16 years and 42 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 41.8%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 5 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 4767 recent records share 8 distinct footprints (595.9 per footprint), of which 31 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 8 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 12899 of 14206 screened records are evaluable (90.8%); 1307 are not. Every share above is taken over the evaluable ones.

Excluded: 10 indeterminate, 1297 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1291 no_site, 3 no_pair, 3 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 69 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 750 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 541 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Monkeypox_virus_F3L_Huo_2022_cladeIIab`

Monkeypox virus — F3L region (positions 46313-46491 of ON563414.2) (Huo 2022, cladeIIab)  
Designed 2022, doi:10.1016/j.bsheal.2022.10.005  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
| 1999 | 0 | 0 | - |
| 2000 | 0 | 0 | - |
| 2001 | 0 | 2 | 0% |
| 2002 | 0 | 0 | - |
| 2003 | 0 | 0 | - |
| 2004 | 1 | 1 | 100% |
| 2005 | 5 | 7 | 71% |
| 2007 | 0 | 0 | - |
| 2008 | 0 | 0 | - |
| 2009 | 0 | 0 | - |
| 2010 | 0 | 3 | 0% |
| 2011 | 0 | 2 | 0% |
| 2012 | 0 | 0 | - |
| 2013 | 0 | 2 | 0% |
| 2014 | 1 | 24 | 4% |
| 2015 | 5 | 11 | 45% |
| 2018 | 3 | 3 | 100% |
| 2019 | 8 | 8 | 100% |
| 2020 | 27 | 37 | 73% |
| 2022 | 3440 | 3446 | 100% |
| 2023 | 3122 | 3132 | 100% |
| 2024 | 1529 | 2099 | 73% |
| 2025 | 1136 | 1887 | 60% |
| 2026 | 793 | 2840 | 28% |

*trend over deposit year: falling, z = -60.25, two-sided p = 0 across 16 years and 13504 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.10, two-sided p = 0.924 across 16 years and 60 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 46.5%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Out of scope:** 3772 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Orthopoxvirus vaccinia (10245) | claimed | 0 | 262 | 285 | 0% |
| taxid 10243 | claimed | 0 | 106 | 119 | 0% |
| taxid 10255 | claimed | 0 | 82 | 82 | 0% |
| taxid 12643 | claimed | 0 | 0 | 12 | 0% |
| taxid 28873 | claimed | 0 | 10 | 12 | 0% |
| taxid 28871 | claimed | 0 | 2 | 2 | 0% |
| taxid 10256 | claimed | 0 | 0 | 0 | 0% |
| taxid 32605 |  | 0 | 16 | 19 | 0% |
| taxid 397342 |  | 0 | 14 | 14 | 0% |
| taxid 467144 |  | 0 | 13 | 13 | 0% |
| _+33 more taxa_ | | | | | |


**Patent records:** 5 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 4919 recent records share 15 distinct footprints (327.9 per footprint), of which 367 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 15 independent observations (one per footprint) the interval around the 43% detected share is 22%-67%, and counting each footprint once, 6 of 15 footprints amplify (40%; interval 20%-64%); each is below the 90% threshold, and the fall from baseline (-71% to -17%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 13504 of 14206 screened records are evaluable (95.1%); 702 are not. Every share above is taken over the evaluable ones.

Excluded: 9 indeterminate, 693 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 693 no_site. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 431 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 691 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Chlamydia_trachomatis_16S_Messmer_1997_round2`

Chlamydia trachomatis — 16S rRNA (Messmer 1997), nested round 2  
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

*trend over deposit year: rising, z = +5.38, two-sided p = 7.26e-08 across 20 years and 362 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +1.38, two-sided p = 0.169 across 20 years and 42 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 46.2%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 1 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 39 recent records share 4 distinct footprints (9.8 per footprint). This flag does not hold up: only 4 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; counting each footprint once, 3 of 4 footprints amplify (75%; interval 30%-95%), which reaches the 90% threshold: the failing records are concentrated on few footprints; with only 4 and 4 independent observations the fall from baseline is -67% to +30%, which no longer excludes zero. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 362 of 378 screened records are evaluable (95.8%); 16 are not. Every share above is taken over the evaluable ones.

Excluded: 16 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 16 no_site. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 9 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthoreovirus_RdRp_Landolfi_2010_round1`

Orthoreovirus — RNA-dependent RNA polymerase (Landolfi 2010), nested round 1  
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
| 2009 | 6 | 6 | 100% |
| 2010 | 7 | 7 | 100% |
| 2011 | 8 | 8 | 100% |
| 2012 | 12 | 12 | 100% |
| 2013 | 10 | 15 | 67% |
| 2014 | 29 | 33 | 88% |
| 2015 | 27 | 32 | 84% |
| 2016 | 20 | 24 | 83% |
| 2017 | 16 | 18 | 89% |
| 2018 | 16 | 33 | 48% |
| 2019 | 20 | 31 | 65% |
| 2020 | 40 | 152 | 26% |
| 2021 | 22 | 35 | 63% |
| 2022 | 44 | 46 | 96% |
| 2023 | 70 | 74 | 95% |
| 2024 | 98 | 99 | 99% |
| 2025 | 134 | 319 | 42% |
| 2026 | 33 | 34 | 97% |

*trend over deposit year: falling, z = -4.45, two-sided p = 8.66e-06 across 23 years and 985 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.35, two-sided p = 0.73 across 23 years and 241 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 2 lineages: mu = 43.1%, phi = 0.0 (intraclass correlation 0.963); worst lineage after shrinkage Orthoreovirus piscis (3431498) at 0.0% (0.0%-0.1%, raw 0.0% on 182); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 52 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 356 recent records share 32 distinct footprints (11.1 per footprint). This flag does not hold up: counting each footprint once, 29 of 32 footprints amplify (91%; interval 76%-97%), which reaches the 90% threshold: the failing records are concentrated on few footprints. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 985 of 14479 screened records are evaluable (6.8%); 13494 are not. Every share above is taken over the evaluable ones.

Excluded: 13494 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 13170 no_site, 265 chance_anchor, 59 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 7610 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 5560 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Monkeypox_virus_F3L_Huo_2022_cladeI`

**Lineage override:** pooled status was low coverage.  
Monkeypox virus — F3L region (positions 46313-46491 of ON563414.2) (Huo 2022, cladeI)  
Designed 2022, doi:10.1016/j.bsheal.2022.10.005  

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
| 2004 | 0 | 1 | 0% |
| 2005 | 2 | 7 | 29% |
| 2007 | 0 | 0 | - |
| 2008 | 0 | 0 | - |
| 2009 | 0 | 0 | - |
| 2010 | 1 | 3 | 33% |
| 2011 | 2 | 2 | 100% |
| 2012 | 0 | 0 | - |
| 2013 | 2 | 2 | 100% |
| 2014 | 23 | 24 | 96% |
| 2015 | 6 | 11 | 55% |
| 2018 | 0 | 3 | 0% |
| 2019 | 0 | 8 | 0% |
| 2020 | 10 | 37 | 27% |
| 2022 | 1 | 3446 | 0% |
| 2023 | 3 | 3132 | 0.1% |
| 2024 | 500 | 2099 | 24% |
| 2025 | 682 | 1886 | 36% |
| 2026 | 1746 | 2840 | 61% |

*trend over deposit year: rising, z = +54.24, two-sided p = 0 across 16 years and 13503 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.12, two-sided p = 0.261 across 16 years and 60 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 53.4%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Out of scope:** 3772 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Orthopoxvirus vaccinia (10245) | claimed | 0 | 283 | 285 | 0% |
| taxid 10243 | claimed | 0 | 113 | 119 | 0% |
| taxid 10255 | claimed | 0 | 82 | 82 | 0% |
| taxid 12643 | claimed | 0 | 12 | 12 | 0% |
| taxid 28873 | claimed | 0 | 10 | 12 | 0% |
| taxid 28871 | claimed | 0 | 2 | 2 | 0% |
| taxid 10256 | claimed | 0 | 0 | 0 | 0% |
| taxid 32605 |  | 0 | 18 | 19 | 0% |
| taxid 397342 |  | 0 | 14 | 14 | 0% |
| taxid 467144 |  | 0 | 13 | 13 | 0% |
| _+33 more taxa_ | | | | | |


**Patent records:** 5 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 4918 recent records share 16 distinct footprints (307.4 per footprint), of which 367 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 16 and 16 independent observations the fall from baseline is +12% to +66%, which no longer excludes zero.

**Denominator:** 13503 of 14206 screened records are evaluable (95.1%); 703 are not. Every share above is taken over the evaluable ones.

Excluded: 10 indeterminate, 693 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 693 no_site. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 431 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 691 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Pseudogymnoascus_destructans_ITS1_Shuey_2014`

Pseudogymnoascus destructans — ITS1 (Shuey 2014)  
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

*trend over deposit year: falling, z = -8.40, two-sided p = 4.58e-17 across 18 years and 457 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.58, two-sided p = 0.01 across 18 years and 40 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Duplication check:** 16 recent records share 4 distinct footprints (4.0 per footprint). This flag does not hold up: only 4 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 4 and 12 independent observations the fall from baseline is -72% to +9%, which no longer excludes zero.

**Denominator:** 457 of 12691 screened records are evaluable (3.6%); 12234 are not. Every share above is taken over the evaluable ones.

Excluded: 12234 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 12226 no_site, 5 chance_anchor, 3 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 3 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 18 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 12208 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Coronaviridae_RdRp_Quan_2010_round1`

**Lineage override:** pooled status was low coverage.  
Coronaviridae — RNA-dependent RNA polymerase (Quan 2010), nested round 1  
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
| 2026 | 337 | 576 | 59% |

*trend over deposit year: falling, z = -8.17, two-sided p = 3.03e-16 across 30 years and 7076 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -4.55, two-sided p = 5.39e-06 across 30 years and 1287 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 12 lineages: mu = 52.6%, phi = 0.6 (intraclass correlation 0.635); worst lineage after shrinkage Alphacoronavirus chicagoense (3433756) at 0.2% (0.0%-1.1%, raw 0.0% on 166); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 262 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Rodent coronavirus PlONCAN (3687427) |  | 10 | 10 | 10 | 100% |
| Rodent coronavirus PmONCAN (3687430) |  | 3 | 3 | 3 | 100% |
| Rodent coronavirus MmONCAN (3687432) |  | 1 | 1 | 1 | 100% |
| Malhaem virus 1 (3456161) |  | 0 | 0 | 0 | 0% |
| Igacovirus sp. (3049965) |  | 0 | 0 | 0 | 0% |
| Betacoronavirus (694002) |  | 0 | 0 | 0 | 0% |
| Alphacoronavirus (693996) |  | 0 | 0 | 0 | 0% |
| Eulipotyphlan coronavirus BbONCAN (3687426) |  | 0 | 0 | 0 | 0% |
| Rodent coronavirus NiONCAN (3687428) |  | 0 | 0 | 0 | 0% |
| Rodent coronavirus CgONCAN (3687429) |  | 0 | 0 | 0 | 0% |
| _+3 more taxa_ | | | | | |


**Duplication check:** 1647 recent records share 201 distinct footprints (8.2 per footprint), of which 24 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 201 and 480 independent observations the fall from baseline is -11% to +5%, which no longer excludes zero.

**Denominator:** 7076 of 25303 screened records are evaluable (28.0%); 18227 are not. Every share above is taken over the evaluable ones.

Excluded: 18227 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 18180 no_site, 31 chance_anchor, 16 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 76 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 18178 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Arenaviridae_S_Lozano_1997_ARS3V`

**Lineage override:** pooled status was low coverage.  
Arenaviridae — S segment (Lozano 1997, ARS3V)  
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
| 2000 | 3 | 4 | 75% |
| 2001 | 2 | 7 | 29% |
| 2002 | 6 | 19 | 32% |
| 2003 | 4 | 5 | 80% |
| 2004 | 10 | 20 | 50% |
| 2005 | 2 | 3 | 67% |
| 2006 | 13 | 15 | 87% |
| 2007 | 3 | 13 | 23% |
| 2008 | 11 | 22 | 50% |
| 2009 | 34 | 51 | 67% |
| 2010 | 12 | 24 | 50% |
| 2011 | 16 | 28 | 57% |
| 2012 | 36 | 45 | 80% |
| 2013 | 7 | 9 | 78% |
| 2014 | 199 | 225 | 88% |
| 2015 | 18 | 23 | 78% |
| 2016 | 16 | 25 | 64% |
| 2017 | 22 | 37 | 59% |
| 2018 | 277 | 443 | 63% |
| 2019 | 54 | 63 | 86% |
| 2020 | 10 | 43 | 23% |
| 2021 | 33 | 39 | 85% |
| 2022 | 39 | 60 | 65% |
| 2023 | 72 | 145 | 50% |
| 2024 | 14 | 23 | 61% |
| 2025 | 22 | 61 | 36% |
| 2026 | 48 | 74 | 65% |

*trend over deposit year: falling, z = -2.17, two-sided p = 0.0298 across 39 years and 1556 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.59, two-sided p = 0.555 across 39 years and 526 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 2 lineages: mu = 58.2%, phi = 8.2 (intraclass correlation 0.109); worst lineage after shrinkage Mammarenavirus machupoense (3052317) at 23.6% (8.3%-43.8%, raw 0.0% on 12); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 473 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| taxid 1672385 |  | 0 | 0 | 7 | 0% |
| taxid 1382279 |  | 0 | 0 | 1 | 0% |
| unidentified Reptarenavirus (1654823) |  | 0 | 0 | 1 | 0% |
| taxid 2764090 |  | 0 | 0 | 0 | 0% |
| Antennavirus trematomi (3426385) |  | 0 | 0 | 0 | 0% |
| taxid 3138838 |  | 0 | 0 | 0 | 0% |
| taxid 2447930 |  | 0 | 0 | 0 | 0% |
| taxid 2461343 |  | 0 | 0 | 0 | 0% |
| taxid 2848326 |  | 0 | 0 | 0 | 0% |
| taxid 2447931 |  | 0 | 0 | 0 | 0% |
| _+57 more taxa_ | | | | | |


**Patent records:** 226 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 137 recent records share 43 distinct footprints (3.2 per footprint). This flag does not hold up: with only 43 and 204 independent observations the fall from baseline is -30% to +2%, which no longer excludes zero.

**Denominator:** 1556 of 5755 screened records are evaluable (27.0%); 4199 are not. Every share above is taken over the evaluable ones.

Excluded: 2 indeterminate, 4197 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3767 no_site, 383 chance_only, 46 chance_anchor, 1 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 3726 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 41 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Enterovirus_5UTR_VP4_VP2_Wray_2016_round2`

Enterovirus — 5' UTR-VP4-VP2 (Wray 2016), nested round 2  
Designed 2016, doi:10.1007/s10393-016-1183-z  
**Degeneracy:** 32-fold degenerate (32-fold primers x 1-fold probe); ~5 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 3 | 3 | 100% |
| 1985 | 2 | 2 | 100% |
| 1987 | 2 | 2 | 100% |
| 1988 | 2 | 2 | 100% |
| 1989 | 2 | 2 | 100% |
| 1992 | 3 | 3 | 100% |
| 1993 | 12 | 12 | 100% |
| 1994 | 6 | 6 | 100% |
| 1995 | 3 | 3 | 100% |
| 1996 | 1 | 1 | 100% |
| 1997 | 0 | 1 | 0% |
| 1998 | 1 | 1 | 100% |
| 1999 | 4 | 5 | 80% |
| 2000 | 16 | 16 | 100% |
| 2001 | 3 | 5 | 60% |
| 2002 | 14 | 18 | 78% |
| 2003 | 56 | 56 | 100% |
| 2004 | 13 | 22 | 59% |
| 2005 | 11 | 12 | 92% |
| 2006 | 24 | 24 | 100% |
| 2007 | 60 | 72 | 83% |
| 2008 | 33 | 42 | 79% |
| 2009 | 166 | 168 | 99% |
| 2010 | 51 | 63 | 81% |
| 2011 | 134 | 153 | 88% |
| 2012 | 76 | 105 | 72% |
| 2013 | 498 | 532 | 94% |
| 2014 | 229 | 280 | 82% |
| 2015 | 491 | 597 | 82% |
| 2016 | 384 | 401 | 96% |
| 2017 | 321 | 363 | 88% |
| 2018 | 138 | 293 | 47% |
| 2019 | 365 | 579 | 63% |
| 2020 | 483 | 575 | 84% |
| 2021 | 1001 | 1098 | 91% |
| 2022 | 789 | 966 | 82% |
| 2023 | 436 | 514 | 85% |
| 2024 | 460 | 518 | 89% |
| 2025 | 424 | 714 | 59% |
| 2026 | 201 | 483 | 42% |

*trend over deposit year: falling, z = -14.93, two-sided p = 2.11e-50 across 40 years and 8712 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -4.43, two-sided p = 9.28e-06 across 40 years and 471 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 5 lineages: mu = 51.5%, phi = 2.0 (intraclass correlation 0.333); worst lineage after shrinkage Enterovirus geswini (3428509) at 1.4% (0.0%-5.2%, raw 0.0% on 70); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Duplication check:** 1203 recent records share 38 distinct footprints (31.7 per footprint), of which 2 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 38 independent observations (one per footprint) the interval around the 52% detected share is 37%-67%, and counting each footprint once, 20 of 38 footprints amplify (53%; interval 37%-68%); each is below the 90% threshold, and the fall from baseline (-48% to -14%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 8712 of 20701 screened records are evaluable (42.1%); 11989 are not. Every share above is taken over the evaluable ones.

Excluded: 11989 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 7169 no_site, 4612 truncated, 191 chance_anchor, 17 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 14 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1550 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 5619 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Influenza_A_virus_M1_Ward_2004`

**Lineage override:** pooled status was low coverage.  
Influenza A virus — M1 (matrix) (Ward 2004)  
Designed 2004, doi:10.1016/S1386-6532(03)00122-7  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 1 | 1 | 100% |
| 1987 | 1 | 1 | 100% |
| 1988 | 1 | 2 | 50% |
| 1989 | 0 | 0 | - |
| 1990 | 1 | 1 | 100% |
| 1992 | 1 | 1 | 100% |
| 1993 | 11 | 12 | 92% |
| 1994 | 2 | 2 | 100% |
| 1997 | 5 | 5 | 100% |
| 1998 | 5 | 5 | 100% |
| 1999 | 37 | 40 | 92% |
| 2000 | 22 | 24 | 92% |
| 2001 | 53 | 56 | 95% |
| 2002 | 30 | 32 | 94% |
| 2003 | 178 | 188 | 95% |
| 2004 | 152 | 172 | 88% |
| 2005 | 780 | 842 | 93% |
| 2006 | 1445 | 1618 | 89% |
| 2007 | 1371 | 1499 | 91% |
| 2008 | 1074 | 1229 | 87% |
| 2009 | 3376 | 3629 | 93% |
| 2010 | 4673 | 5119 | 91% |
| 2011 | 1197 | 1356 | 88% |
| 2012 | 1522 | 1755 | 87% |
| 2013 | 3950 | 4835 | 82% |
| 2014 | 2805 | 3591 | 78% |
| 2015 | 3988 | 5839 | 68% |
| 2016 | 3823 | 6596 | 58% |
| 2017 | 2409 | 3612 | 67% |
| 2018 | 3511 | 6623 | 53% |
| 2019 | 4725 | 11998 | 39% |
| 2020 | 4917 | 7627 | 64% |
| 2021 | 2083 | 3410 | 61% |
| 2022 | 1836 | 8938 | 21% |
| 2023 | 6699 | 14547 | 46% |
| 2024 | 14600 | 23749 | 61% |
| 2025 | 21997 | 36347 | 61% |
| 2026 | 15262 | 28594 | 53% |

*trend over deposit year: falling, z = -80.66, two-sided p = 0 across 37 years and 183895 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -9.94, two-sided p = 2.82e-23 across 37 years and 2791 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 59.2%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 70513 recent records share 347 distinct footprints (203.2 per footprint), of which 12 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 347 and 732 independent observations the fall from baseline is -6% to +7%, which no longer excludes zero.

**Denominator:** 183895 of 184887 screened records are evaluable (99.5%); 992 are not. Every share above is taken over the evaluable ones.

Excluded: 24 indeterminate, 968 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 763 no_site, 203 truncated, 2 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 25 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 763 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthoflavivirus_NS5_Scaramozzino_2001_round1`

**Lineage override:** pooled status was low coverage.  
Orthoflavivirus — NS5 (Scaramozzino 2001), nested round 1  
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
| 1995 | 7 | 11 | 64% |
| 1996 | 2 | 2 | 100% |
| 1997 | 8 | 12 | 67% |
| 1998 | 13 | 22 | 59% |
| 1999 | 13 | 24 | 54% |
| 2000 | 17 | 34 | 50% |
| 2001 | 13 | 31 | 42% |
| 2002 | 24 | 33 | 73% |
| 2003 | 21 | 32 | 66% |
| 2004 | 88 | 99 | 89% |
| 2005 | 190 | 240 | 79% |
| 2006 | 91 | 120 | 76% |
| 2007 | 113 | 211 | 54% |
| 2008 | 216 | 1016 | 21% |
| 2009 | 513 | 1333 | 38% |
| 2010 | 301 | 417 | 72% |
| 2011 | 489 | 614 | 80% |
| 2012 | 151 | 333 | 45% |
| 2013 | 188 | 320 | 59% |
| 2014 | 630 | 815 | 77% |
| 2015 | 358 | 568 | 63% |
| 2016 | 832 | 1052 | 79% |
| 2017 | 771 | 1460 | 53% |
| 2018 | 599 | 1122 | 53% |
| 2019 | 278 | 709 | 39% |
| 2020 | 745 | 1840 | 40% |
| 2021 | 1499 | 3378 | 44% |
| 2022 | 830 | 1549 | 54% |
| 2023 | 2188 | 3904 | 56% |
| 2024 | 2255 | 4006 | 56% |
| 2025 | 2005 | 3226 | 62% |
| 2026 | 3214 | 5592 | 57% |

*trend over deposit year: rising, z = +4.84, two-sided p = 1.28e-06 across 40 years and 34150 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -3.42, two-sided p = 0.000632 across 40 years and 1778 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 10 lineages: mu = 62.3%, phi = 3.7 (intraclass correlation 0.211); worst lineage after shrinkage Orthoflavivirus usutuense (3048443) at 0.5% (0.1%-1.4%, raw 0.0% on 428); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 1 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Balclutha incisa flavivirus 1 (3140651) |  | 0 | 0 | 0 | 0% |


**Duplication check:** 9490 recent records share 194 distinct footprints (48.9 per footprint), of which 315 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 194 and 396 independent observations the fall from baseline is -2% to +15%, which no longer excludes zero.

**Denominator:** 34150 of 61192 screened records are evaluable (55.8%); 27042 are not. Every share above is taken over the evaluable ones.

Excluded: 12 indeterminate, 27030 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 25750 no_site, 1242 truncated, 38 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 640 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1716 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 24034 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Iflavirus_sacbroodi_polyprotein_Rossi_2024`

Iflavirus sacbroodi — polyprotein (Rossi 2024)  
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
| 2026 | 15 | 21 | 71% |

*trend over deposit year: falling, z = -2.43, two-sided p = 0.015 across 24 years and 377 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.59, two-sided p = 0.112 across 24 years and 112 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 60.4%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 1 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 53 recent records share 13 distinct footprints (4.1 per footprint). This flag does not hold up: only 13 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 377 of 918 screened records are evaluable (41.1%); 541 are not. Every share above is taken over the evaluable ones.

Excluded: 541 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 531 no_site, 10 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 1 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 531 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Morbillivirus_canis_N_Elia_2006`

**Lineage override:** pooled status was low coverage.  
Morbillivirus canis — N (nucleoprotein) (Elia 2006)  
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
| 2021 | 21 | 21 | 100% |
| 2022 | 16 | 57 | 28% |
| 2023 | 4 | 21 | 19% |
| 2024 | 12 | 14 | 86% |
| 2025 | 11 | 26 | 42% |
| 2026 | 51 | 77 | 66% |

*trend over deposit year: falling, z = -0.85, two-sided p = 0.393 across 30 years and 659 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.00, two-sided p = 1 across 30 years and 228 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 60.6%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 61 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 104 recent records share 23 distinct footprints (4.5 per footprint). This flag does not hold up: with only 23 and 90 independent observations the fall from baseline is -13% to +29%, which no longer excludes zero.

**Denominator:** 659 of 3952 screened records are evaluable (16.7%); 3293 are not. Every share above is taken over the evaluable ones.

Excluded: 3293 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3282 no_site, 11 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 3282 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Influenza_A_virus_NP_Tsukamoto_2010`

**Lineage override:** pooled status was low coverage.  
Influenza A virus — NP (nucleoprotein) (Tsukamoto 2010)  
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
| 1993 | 75 | 89 | 84% |
| 1994 | 6 | 8 | 75% |
| 1995 | 4 | 4 | 100% |
| 1996 | 0 | 3 | 0% |
| 1997 | 1 | 2 | 50% |
| 1998 | 13 | 17 | 76% |
| 1999 | 26 | 30 | 87% |
| 2000 | 39 | 44 | 89% |
| 2001 | 22 | 32 | 69% |
| 2002 | 41 | 50 | 82% |
| 2003 | 73 | 109 | 67% |
| 2004 | 117 | 130 | 90% |
| 2005 | 194 | 837 | 23% |
| 2006 | 990 | 1947 | 51% |
| 2007 | 632 | 1193 | 53% |
| 2008 | 915 | 1146 | 80% |
| 2009 | 2167 | 2647 | 82% |
| 2010 | 2862 | 3433 | 83% |
| 2011 | 2433 | 3029 | 80% |
| 2012 | 2508 | 3505 | 72% |
| 2013 | 3996 | 4903 | 82% |
| 2014 | 3295 | 4739 | 70% |
| 2015 | 3820 | 5106 | 75% |
| 2016 | 4439 | 7102 | 63% |
| 2017 | 3735 | 7889 | 47% |
| 2018 | 3968 | 6893 | 58% |
| 2019 | 5518 | 11712 | 47% |
| 2020 | 6235 | 7525 | 83% |
| 2021 | 2698 | 3132 | 86% |
| 2022 | 2692 | 8804 | 31% |
| 2023 | 7196 | 13397 | 54% |
| 2024 | 15675 | 23412 | 67% |
| 2025 | 22125 | 35912 | 62% |
| 2026 | 15658 | 28170 | 56% |

*trend over deposit year: falling, z = -31.72, two-sided p = 9.23e-221 across 41 years and 187018 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -5.93, two-sided p = 3.02e-09 across 41 years and 1855 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 60.8%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 69581 recent records share 202 distinct footprints (344.5 per footprint), of which 10 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 202 and 473 independent observations the fall from baseline is -9% to +7%, which no longer excludes zero.

**Denominator:** 187018 of 191543 screened records are evaluable (97.6%); 4525 are not. Every share above is taken over the evaluable ones.

Excluded: 12 indeterminate, 4513 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3315 truncated, 1196 no_site, 2 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 64 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 41 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1155 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Escherichia_coli_malB_Candrian_1991`

**Lineage override:** pooled status was low coverage.  
Escherichia coli — malB promoter region (Candrian 1991)  
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

*trend over deposit year: falling, z = -3.08, two-sided p = 0.00206 across 24 years and 326 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.41, two-sided p = 0.159 across 24 years and 60 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 62.2%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 45 recent records share 5 distinct footprints (9.0 per footprint). This flag does not hold up: only 5 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 5 and 6 independent observations the fall from baseline is -54% to +36%, which no longer excludes zero.

**Denominator:** 326 of 401 screened records are evaluable (81.3%); 75 are not. Every share above is taken over the evaluable ones.

Excluded: 75 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 73 no_site, 2 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 73 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `West_Nile_virus_E_Lanciotti_2001`

West Nile virus — E (envelope) (Lanciotti 2001)  
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
| 2026 | 39 | 412 | 9% |

*trend over deposit year: falling, z = -25.64, two-sided p = 4.85e-145 across 29 years and 7091 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +1.13, two-sided p = 0.259 across 29 years and 376 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 63.9%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 89 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1722 recent records share 38 distinct footprints (45.3 per footprint), of which 4 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 38 independent observations (one per footprint) the interval around the 64% detected share is 48%-77%, and counting each footprint once, 29 of 38 footprints amplify (76%; interval 61%-87%); each is below the 90% threshold, and the fall from baseline (-40% to -7%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 7091 of 9069 screened records are evaluable (78.2%); 1978 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 1977 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1699 no_site, 150 truncated, 128 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 37 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 16 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1683 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Morbillivirus_canis_H_Muller_2011_Mueller_1F`

Morbillivirus canis — H (haemagglutinin) (Müller 2011, Mueller 1F)  
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
| 2026 | 51 | 80 | 64% |

*trend over deposit year: falling, z = -5.58, two-sided p = 2.4e-08 across 33 years and 513 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.46, two-sided p = 0.0139 across 33 years and 171 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 68.1%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 61 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 94 recent records share 25 distinct footprints (3.8 per footprint). Both reductions leave the flag in place: with only 25 independent observations (one per footprint) the interval around the 68% detected share is 48%-83%, and counting each footprint once, 18 of 25 footprints amplify (72%; interval 52%-86%); each is below the 90% threshold, and the fall from baseline (-46% to -8%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 513 of 3952 screened records are evaluable (13.0%); 3439 are not. Every share above is taken over the evaluable ones.

Excluded: 3439 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1846 no_site, 1531 truncated, 62 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 5 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 384 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1462 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Triatovirus_nigereginacellulae_capsid_Rossi_2024`

Triatovirus nigereginacellulae — capsid protein (Rossi 2024)  
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
| 2020 | 56 | 79 | 71% |
| 2021 | 121 | 131 | 92% |
| 2022 | 24 | 43 | 56% |
| 2023 | 92 | 104 | 88% |
| 2024 | 153 | 195 | 78% |
| 2025 | 23 | 40 | 57% |
| 2026 | 35 | 54 | 65% |

*trend over deposit year: falling, z = -2.04, two-sided p = 0.0412 across 25 years and 1229 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -3.72, two-sided p = 0.000201 across 25 years and 193 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 69.2%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 3 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 172 recent records share 25 distinct footprints (6.9 per footprint). This flag does not hold up: with only 25 and 79 independent observations the fall from baseline is -35% to +3%, which no longer excludes zero.

**Denominator:** 1229 of 1615 screened records are evaluable (76.1%); 386 are not. Every share above is taken over the evaluable ones.

Excluded: 3 indeterminate, 383 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 344 no_site, 29 chance_anchor, 10 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 3 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 31 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 313 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthoreovirus_RdRp_Landolfi_2010_round2`

Orthoreovirus — RNA-dependent RNA polymerase (Landolfi 2010), nested round 2  
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
| 2009 | 6 | 6 | 100% |
| 2010 | 5 | 7 | 71% |
| 2011 | 8 | 10 | 80% |
| 2012 | 29 | 29 | 100% |
| 2013 | 15 | 15 | 100% |
| 2014 | 21 | 33 | 64% |
| 2015 | 29 | 32 | 91% |
| 2016 | 19 | 24 | 79% |
| 2017 | 17 | 18 | 94% |
| 2018 | 31 | 33 | 94% |
| 2019 | 27 | 32 | 84% |
| 2020 | 143 | 152 | 94% |
| 2021 | 58 | 60 | 97% |
| 2022 | 39 | 46 | 85% |
| 2023 | 55 | 72 | 76% |
| 2024 | 85 | 99 | 86% |
| 2025 | 219 | 322 | 68% |
| 2026 | 29 | 34 | 85% |

*trend over deposit year: falling, z = -5.02, two-sided p = 5.19e-07 across 24 years and 1032 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.10, two-sided p = 0.0356 across 24 years and 237 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 2 lineages: mu = 67.1%, phi = 0.6 (intraclass correlation 0.622); worst lineage after shrinkage Orthoreovirus 'civet orthoreovirus' (3461089) at 25.3% (0.0%-89.8%, raw 0.0% on 1); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 52 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 359 recent records share 26 distinct footprints (13.8 per footprint). Both reductions leave the flag in place: with only 26 independent observations (one per footprint) the interval around the 70% detected share is 50%-84%, and counting each footprint once, 20 of 26 footprints amplify (77%; interval 58%-89%); each is below the 90% threshold, and the fall from baseline (-38% to -2%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 1032 of 14479 screened records are evaluable (7.1%); 13447 are not. Every share above is taken over the evaluable ones.

Excluded: 13447 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 13154 no_site, 219 chance_anchor, 74 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 3 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 205 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 12949 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Rhabdoviridae_L_Bourhy_2005_round1`

**Lineage override:** pooled status was low coverage.  
Rhabdoviridae — L (polymerase) (Bourhy 2005), nested round 1  
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
| 1997 | 4 | 6 | 67% |
| 1999 | 0 | 10 | 0% |
| 2000 | 4 | 4 | 100% |
| 2001 | 0 | 1 | 0% |
| 2002 | 5 | 7 | 71% |
| 2003 | 2 | 2 | 100% |
| 2004 | 1 | 3 | 33% |
| 2005 | 3 | 8 | 38% |
| 2006 | 2 | 3 | 67% |
| 2007 | 23 | 27 | 85% |
| 2008 | 33 | 42 | 79% |
| 2009 | 14 | 27 | 52% |
| 2010 | 22 | 31 | 71% |
| 2011 | 15 | 22 | 68% |
| 2012 | 197 | 218 | 90% |
| 2013 | 45 | 59 | 76% |
| 2014 | 54 | 98 | 55% |
| 2015 | 259 | 317 | 82% |
| 2016 | 318 | 388 | 82% |
| 2017 | 456 | 569 | 80% |
| 2018 | 253 | 295 | 86% |
| 2019 | 559 | 692 | 81% |
| 2020 | 329 | 495 | 66% |
| 2021 | 98 | 247 | 40% |
| 2022 | 291 | 452 | 64% |
| 2023 | 871 | 961 | 91% |
| 2024 | 704 | 993 | 71% |
| 2025 | 214 | 458 | 47% |
| 2026 | 175 | 319 | 55% |

*trend over deposit year: falling, z = -7.07, two-sided p = 1.58e-12 across 35 years and 6767 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -4.87, two-sided p = 1.13e-06 across 35 years and 1355 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 2 lineages: mu = 85.3%, phi = 298.7 (intraclass correlation 0.003); worst lineage after shrinkage Tahe rhabdovirus 3 (2983976) at 79.7% (75.1%-83.9%, raw 0.0% on 21); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 769 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Dichorhavirus orchidaceae (152177) |  | 8 | 8 | 8 | 100% |
| taxid 2497337 |  | 6 | 6 | 6 | 100% |
| taxid 195059 |  | 4 | 4 | 4 | 100% |
| taxid 11307 |  | 4 | 4 | 4 | 100% |
| taxid 3084645 |  | 3 | 3 | 3 | 100% |
| Betanucleorhabdovirus taraxi (3427245) |  | 2 | 2 | 2 | 100% |
| Betanucleorhabdovirus picridis (3427244) |  | 2 | 2 | 2 | 100% |
| taxid 2950850 |  | 2 | 2 | 2 | 100% |
| taxid 2950883 |  | 2 | 2 | 2 | 100% |
| Asparagales alphanucleorhabdovirus 1 (3479778) |  | 2 | 2 | 2 | 100% |
| _+192 more taxa_ | | | | | |


**Duplication check:** 1309 recent records share 189 distinct footprints (6.9 per footprint), of which 44 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 189 and 525 independent observations the fall from baseline is -12% to +3%, which no longer excludes zero.

**Denominator:** 6767 of 9139 screened records are evaluable (74.0%); 2372 are not. Every share above is taken over the evaluable ones.

Excluded: 9 indeterminate, 2363 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 2102 no_site, 170 truncated, 89 chance_anchor, 2 chance_only. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 139 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 139 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1963 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Haemosporida_cytb_Hellgren_2004_HaemNFI`

Haemosporida — cytochrome b (Hellgren 2004, HaemNFI)  
Designed 2004, doi:10.1645/GE-184R1  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1998 | 4 | 4 | 100% |
| 2000 | 0 | 0 | - |
| 2002 | 52 | 52 | 100% |
| 2003 | 0 | 0 | - |
| 2004 | 5 | 5 | 100% |
| 2005 | 1 | 41 | 2% |
| 2006 | 15 | 15 | 100% |
| 2007 | 3 | 3 | 100% |
| 2008 | 30 | 32 | 94% |
| 2009 | 36 | 41 | 88% |
| 2010 | 73 | 81 | 90% |
| 2011 | 20 | 32 | 62% |
| 2012 | 1 | 7 | 14% |
| 2013 | 8 | 11 | 73% |
| 2014 | 13 | 13 | 100% |
| 2015 | 14 | 24 | 58% |
| 2016 | 11 | 12 | 92% |
| 2017 | 112 | 119 | 94% |
| 2018 | 114 | 117 | 97% |
| 2019 | 11 | 20 | 55% |
| 2020 | 86 | 87 | 99% |
| 2021 | 6 | 6 | 100% |
| 2022 | 73 | 75 | 97% |
| 2023 | 113 | 119 | 95% |
| 2024 | 59 | 68 | 87% |
| 2025 | 125 | 177 | 71% |
| 2026 | 64 | 85 | 75% |

*trend over deposit year: rising, z = +1.70, two-sided p = 0.0884 across 25 years and 1246 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.40, two-sided p = 0.163 across 25 years and 313 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 3 lineages: mu = 68.2%, phi = 1.1 (intraclass correlation 0.488); worst lineage after shrinkage Haemoproteus pallidus (389271) at 10.2% (0.1%-39.0%, raw 0.0% on 6); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 8901 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Hepatocystis sp. TLG-2012 (1266736) |  | 74 | 74 | 74 | 100% |
| Plasmodium floridense (31275) |  | 65 | 65 | 65 | 100% |
| Hepatocystis sp. AA-2012 (1164881) |  | 56 | 56 | 56 | 100% |
| Hepatocystis sp. 1 JS-2013 (1410048) |  | 36 | 36 | 36 | 100% |
| Plasmodium tupinambi (3448513) |  | 29 | 29 | 29 | 100% |
| Haemosporida sp. B LB-2015 (1699100) |  | 27 | 27 | 27 | 100% |
| taxid 864142 |  | 24 | 24 | 24 | 100% |
| Plasmodium sp. BM-2016a (1830315) |  | 24 | 24 | 24 | 100% |
| unidentified Haemosporida (51530) |  | 23 | 23 | 23 | 100% |
| Plasmodiidae sp. (2605378) |  | 22 | 22 | 22 | 100% |
| _+1969 more taxa_ | | | | | |


**Duplication check:** 263 recent records share 41 distinct footprints (6.4 per footprint). Both reductions leave the flag in place: with only 41 independent observations (one per footprint) the interval around the 72% detected share is 57%-84%, and counting each footprint once, 26 of 41 footprints amplify (63%; interval 48%-76%); each is below the 90% threshold, and the fall from baseline (-31% to -1%) still excludes zero. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 1246 of 23152 screened records are evaluable (5.4%); 21906 are not. Every share above is taken over the evaluable ones.

Excluded: 21906 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 20273 no_site, 1204 truncated, 415 chance_anchor, 14 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 2 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 5093 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 15180 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Deformed_wing_virus_B_polyprotein_Rossi_2024`

Deformed wing virus B — polyprotein (Rossi 2024)  
Designed 2024, doi:10.3390/microorganisms12061105  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 2020 | 0 | 0 | - |
| 2022 | 0 | 0 | - |
| 2023 | 41 | 41 | 100% |
| 2024 | 0 | 0 | - |
| 2025 | 9 | 10 | 90% |
| 2026 | 3 | 6 | 50% |

*trend over deposit year: falling, z = -3.94, two-sided p = 8.25e-05 across 3 years and 57 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.27, two-sided p = 0.0232 across 3 years and 17 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Duplication check:** 16 recent records share 8 distinct footprints (2.0 per footprint). This flag does not hold up: only 8 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; with only 8 independent observations (one per footprint) the interval around the 75% detected share is 41%-93%, which no longer rules out the 90% threshold; with only 8 and 7 independent observations the fall from baseline is -59% to +15%, which no longer excludes zero. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 57 of 737 screened records are evaluable (7.7%); 680 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 679 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 670 no_site, 9 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 670 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Papillomaviridae_L1_Forslund_1999`

**Lineage override:** pooled status was low coverage.  
Papillomaviridae — L1 (Forslund 1999)  
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
| 1993 | 50 | 63 | 79% |
| 1994 | 3 | 5 | 60% |
| 1995 | 21 | 58 | 36% |
| 1996 | 5 | 7 | 71% |
| 1997 | 5 | 12 | 42% |
| 1998 | 22 | 27 | 81% |
| 1999 | 3 | 8 | 38% |
| 2000 | 10 | 13 | 77% |
| 2001 | 10 | 11 | 91% |
| 2002 | 16 | 25 | 64% |
| 2003 | 7 | 21 | 33% |
| 2004 | 16 | 22 | 73% |
| 2005 | 38 | 56 | 68% |
| 2006 | 13 | 33 | 39% |
| 2007 | 72 | 96 | 75% |
| 2008 | 133 | 160 | 83% |
| 2009 | 49 | 147 | 33% |
| 2010 | 125 | 142 | 88% |
| 2011 | 606 | 678 | 89% |
| 2012 | 210 | 377 | 56% |
| 2013 | 156 | 190 | 82% |
| 2014 | 323 | 393 | 82% |
| 2015 | 146 | 216 | 68% |
| 2016 | 429 | 909 | 47% |
| 2017 | 438 | 703 | 62% |
| 2018 | 350 | 3266 | 11% |
| 2019 | 174 | 348 | 50% |
| 2020 | 503 | 1500 | 34% |
| 2021 | 2192 | 2329 | 94% |
| 2022 | 412 | 716 | 58% |
| 2023 | 560 | 684 | 82% |
| 2024 | 1152 | 1448 | 80% |
| 2025 | 995 | 1215 | 82% |
| 2026 | 197 | 373 | 53% |

*trend over deposit year: rising, z = +10.43, two-sided p = 1.75e-25 across 43 years and 16275 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -3.42, two-sided p = 0.000616 across 43 years and 1973 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 5 lineages: mu = 77.3%, phi = 0.3 (intraclass correlation 0.791); worst lineage after shrinkage Bovine Dyokappapapillomavirus (3477800) at 3.3% (0.0%-23.6%, raw 0.0% on 6); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 1064 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1591 recent records share 200 distinct footprints (8.0 per footprint), of which 3 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 200 and 863 independent observations the fall from baseline is +12% to +25%, which no longer excludes zero.

**Denominator:** 16275 of 41948 screened records are evaluable (38.8%); 25673 are not. Every share above is taken over the evaluable ones.

Excluded: 57 indeterminate, 25616 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 24135 no_site, 535 chance_only, 525 truncated, 405 chance_anchor, 16 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 59 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 9066 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 15069 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Adenoviridae_hexon_Casas_2005_round1`

**Lineage override:** pooled status was low coverage.  
Adenoviridae — hexon (Casas 2005), nested round 1  
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
| 1990 | 3 | 3 | 100% |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 0 | - |
| 1993 | 11 | 13 | 85% |
| 1994 | 0 | 1 | 0% |
| 1995 | 3 | 5 | 60% |
| 1996 | 0 | 8 | 0% |
| 1997 | 1 | 2 | 50% |
| 1998 | 5 | 6 | 83% |
| 1999 | 10 | 14 | 71% |
| 2000 | 2 | 15 | 13% |
| 2001 | 22 | 27 | 81% |
| 2002 | 7 | 9 | 78% |
| 2003 | 37 | 45 | 82% |
| 2004 | 22 | 29 | 76% |
| 2005 | 99 | 103 | 96% |
| 2006 | 19 | 20 | 95% |
| 2007 | 24 | 44 | 55% |
| 2008 | 110 | 125 | 88% |
| 2009 | 92 | 102 | 90% |
| 2010 | 69 | 92 | 75% |
| 2011 | 64 | 83 | 77% |
| 2012 | 83 | 97 | 86% |
| 2013 | 158 | 195 | 81% |
| 2014 | 73 | 93 | 78% |
| 2015 | 146 | 160 | 91% |
| 2016 | 56 | 165 | 34% |
| 2017 | 149 | 245 | 61% |
| 2018 | 108 | 130 | 83% |
| 2019 | 134 | 250 | 54% |
| 2020 | 459 | 592 | 78% |
| 2021 | 466 | 508 | 92% |
| 2022 | 346 | 462 | 75% |
| 2023 | 492 | 733 | 67% |
| 2024 | 339 | 442 | 77% |
| 2025 | 353 | 542 | 65% |
| 2026 | 736 | 875 | 84% |

*trend over deposit year: falling, z = -0.84, two-sided p = 0.404 across 36 years and 6236 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -4.85, two-sided p = 1.24e-06 across 36 years and 881 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 5 lineages: mu = 88.7%, phi = 1.0 (intraclass correlation 0.498); worst lineage after shrinkage Aviadenovirus hepatitidis (3426530) at 1.8% (0.0%-6.8%, raw 0.0% on 49); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 1043 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1500 recent records share 95 distinct footprints (15.8 per footprint), of which 105 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 95 and 269 independent observations the fall from baseline is -7% to +13%, which no longer excludes zero.

**Denominator:** 6236 of 38024 screened records are evaluable (16.4%); 31788 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 31787 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 24353 no_site, 6190 truncated, 882 chance_anchor, 350 chance_only, 12 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 385 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 13849 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 10504 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Coronaviridae_RdRp_Quan_2010_round2`

**Lineage override:** pooled status was low coverage.  
Coronaviridae — RNA-dependent RNA polymerase (Quan 2010), nested round 2  
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
| 2008 | 18 | 24 | 75% |
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
| 2026 | 427 | 568 | 75% |

*trend over deposit year: rising, z = +16.24, two-sided p = 2.5e-59 across 30 years and 6888 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.71, two-sided p = 0.00675 across 30 years and 707 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 11 lineages: mu = 81.2%, phi = 0.4 (intraclass correlation 0.716); worst lineage after shrinkage Betacoronavirus cameli (3433633) at 0.6% (0.0%-3.4%, raw 0.0% on 58); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 262 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Rodent coronavirus PlONCAN (3687427) |  | 10 | 10 | 10 | 100% |
| Rodent coronavirus PmONCAN (3687430) |  | 3 | 3 | 3 | 100% |
| Rodent coronavirus MmONCAN (3687432) |  | 1 | 1 | 1 | 100% |
| Malhaem virus 1 (3456161) |  | 0 | 0 | 0 | 0% |
| Igacovirus sp. (3049965) |  | 0 | 0 | 0 | 0% |
| Betacoronavirus (694002) |  | 0 | 0 | 0 | 0% |
| Alphacoronavirus (693996) |  | 0 | 0 | 0 | 0% |
| Eulipotyphlan coronavirus BbONCAN (3687426) |  | 0 | 0 | 0 | 0% |
| Rodent coronavirus NiONCAN (3687428) |  | 0 | 0 | 0 | 0% |
| Rodent coronavirus CgONCAN (3687429) |  | 0 | 0 | 0 | 0% |
| _+3 more taxa_ | | | | | |


**Duplication check:** 1575 recent records share 89 distinct footprints (17.7 per footprint), of which 9 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 89 and 160 independent observations the fall from baseline is -1% to +21%, which no longer excludes zero.

**Denominator:** 6888 of 25303 screened records are evaluable (27.2%); 18415 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 18414 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 18022 no_site, 295 chance_only, 68 chance_anchor, 29 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 32 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2340 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 15682 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Influenza_A_virus_HA_H7_Tsukamoto_2010`

**Lineage override:** pooled status was low coverage.  
Influenza A virus — HA (haemagglutinin), H7 (Tsukamoto 2010)  
Designed 2010, doi:10.1128/JCM.01264-10  
**Degeneracy:** 12288-fold degenerate (384-fold primers x 32-fold probe); ~14 cycles of Cq delay at best if it amplifies at all. In-silico detection is close to a tautology here and says little about whether this assay works  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 1 | 0% |
| 1987 | 0 | 1 | 0% |
| 1988 | 2 | 2 | 100% |
| 1989 | 0 | 2 | 0% |
| 1990 | 1 | 1 | 100% |
| 1991 | 0 | 1 | 0% |
| 1994 | 0 | 1 | 0% |
| 1995 | 5 | 6 | 83% |
| 1996 | 3 | 3 | 100% |
| 1998 | 2 | 2 | 100% |
| 1999 | 13 | 13 | 100% |
| 2000 | 23 | 27 | 85% |
| 2001 | 0 | 0 | - |
| 2002 | 0 | 0 | - |
| 2003 | 61 | 66 | 92% |
| 2004 | 23 | 29 | 79% |
| 2005 | 17 | 18 | 94% |
| 2006 | 39 | 47 | 83% |
| 2007 | 109 | 125 | 87% |
| 2008 | 281 | 308 | 91% |
| 2009 | 159 | 170 | 94% |
| 2010 | 79 | 90 | 88% |
| 2011 | 69 | 81 | 85% |
| 2012 | 96 | 102 | 94% |
| 2013 | 141 | 360 | 39% |
| 2014 | 258 | 348 | 74% |
| 2015 | 211 | 859 | 25% |
| 2016 | 99 | 253 | 39% |
| 2017 | 228 | 376 | 61% |
| 2018 | 70 | 254 | 28% |
| 2019 | 89 | 114 | 78% |
| 2020 | 102 | 274 | 37% |
| 2021 | 24 | 163 | 15% |
| 2022 | 41 | 104 | 39% |
| 2023 | 14 | 23 | 61% |
| 2024 | 75 | 90 | 83% |
| 2025 | 48 | 72 | 67% |
| 2026 | 64 | 69 | 93% |

*trend over deposit year: falling, z = -16.49, two-sided p = 4.46e-61 across 36 years and 4455 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.50, two-sided p = 0.135 across 36 years and 412 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 79.3%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 150 recent records share 21 distinct footprints (7.1 per footprint). This flag does not hold up: with only 21 independent observations (one per footprint) the interval around the 79% detected share is 58%-91%, which no longer rules out the 90% threshold; with only 21 and 138 independent observations the fall from baseline is +3% to +40%, which no longer excludes zero. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 4455 of 4652 screened records are evaluable (95.8%); 197 are not. Every share above is taken over the evaluable ones.

Excluded: 2 indeterminate, 195 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 116 truncated, 74 no_site, 5 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 3 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 57 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 17 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthoherpesviridae_terminase_Chmielewicz_2001_round2`

Orthoherpesviridae — terminase (Chmielewicz 2001), nested round 2  
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
| 2026 | 101 | 113 | 89% |

*trend over deposit year: rising, z = +2.96, two-sided p = 0.00311 across 36 years and 3123 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +1.03, two-sided p = 0.301 across 36 years and 432 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 3 lineages: mu = 69.3%, phi = 0.0 (intraclass correlation 1.000); worst lineage after shrinkage Varicellovirus humanalpha3 (3050294) at 0.0% (0.0%-0.0%, raw 0.0% on 54); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 1 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| synthetic construct (32630) |  | 1 | 1 | 1 | 100% |


**Duplication check:** 332 recent records share 29 distinct footprints (11.4 per footprint). This flag does not hold up: with only 29 independent observations (one per footprint) the interval around the 80% detected share is 62%-90%, which no longer rules out the 90% threshold; with only 29 and 106 independent observations the fall from baseline is -31% to +0.1%, which no longer excludes zero. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 3123 of 3812 screened records are evaluable (81.9%); 689 are not. Every share above is taken over the evaluable ones.

Excluded: 4 indeterminate, 685 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 567 no_site, 86 chance_anchor, 30 chance_only, 2 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 423 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 144 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Morbillivirus_canis_P_Scagliarini_2007`

**Lineage override:** pooled status was low coverage.  
Morbillivirus canis — P (phosphoprotein) (Scagliarini 2007)  
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
| 2003 | 25 | 29 | 86% |
| 2004 | 2 | 2 | 100% |
| 2005 | 24 | 28 | 86% |
| 2006 | 5 | 8 | 62% |
| 2007 | 11 | 22 | 50% |
| 2008 | 15 | 16 | 94% |
| 2009 | 25 | 29 | 86% |
| 2010 | 11 | 22 | 50% |
| 2011 | 8 | 10 | 80% |
| 2012 | 23 | 35 | 66% |
| 2013 | 15 | 22 | 68% |
| 2014 | 4 | 16 | 25% |
| 2015 | 13 | 21 | 62% |
| 2016 | 25 | 27 | 93% |
| 2017 | 10 | 11 | 91% |
| 2018 | 14 | 24 | 58% |
| 2019 | 29 | 30 | 97% |
| 2020 | 34 | 50 | 68% |
| 2021 | 4 | 9 | 44% |
| 2022 | 40 | 43 | 93% |
| 2023 | 7 | 14 | 50% |
| 2024 | 14 | 17 | 82% |
| 2025 | 12 | 15 | 80% |
| 2026 | 61 | 76 | 80% |

*trend over deposit year: rising, z = +0.26, two-sided p = 0.796 across 33 years and 602 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.29, two-sided p = 0.022 across 33 years and 171 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 80.4%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 61 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 92 recent records share 19 distinct footprints (4.8 per footprint). This flag does not hold up: with only 19 independent observations (one per footprint) the interval around the 80% detected share is 58%-92%, which no longer rules out the 90% threshold; with only 19 and 55 independent observations the fall from baseline is -18% to +24%, which no longer excludes zero. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 602 of 3952 screened records are evaluable (15.2%); 3350 are not. Every share above is taken over the evaluable ones.

Excluded: 3350 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3343 no_site, 7 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 2 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 3343 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthohantavirus_S_Anthony_2013_round1`

**Lineage override:** pooled status was watch.  
Orthohantavirus — S segment (Anthony 2013), nested round 1  
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
| 2017 | 87 | 95 | 92% |
| 2018 | 271 | 285 | 95% |
| 2019 | 193 | 217 | 89% |
| 2020 | 198 | 203 | 98% |
| 2021 | 657 | 661 | 99% |
| 2022 | 122 | 131 | 93% |
| 2023 | 286 | 293 | 98% |
| 2024 | 242 | 252 | 96% |
| 2025 | 194 | 199 | 97% |
| 2026 | 187 | 232 | 81% |

*trend over deposit year: falling, z = -3.42, two-sided p = 0.000637 across 38 years and 4292 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -4.23, two-sided p = 2.32e-05 across 38 years and 575 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 6 lineages: mu = 89.2%, phi = 3.4 (intraclass correlation 0.227); worst lineage after shrinkage Orthohantavirus luxiense (3052484) at 48.7% (22.6%-75.1%, raw 33.3% on 9); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 83 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 443 recent records share 42 distinct footprints (10.5 per footprint). This flag does not hold up: with only 42 independent observations (one per footprint) the interval around the 88% detected share is 75%-95%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 4292 of 16099 screened records are evaluable (26.7%); 11807 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 11806 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 5460 chance_only, 5131 no_site, 1110 truncated, 105 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 1 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 4918 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 213 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Alphavirus_nsP4_Sanchez-Seco_2001_round2`

**Lineage override:** pooled status was stable.  
Alphavirus — nsP4 (Sánchez-Seco 2001), nested round 2  
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
| 2026 | 3350 | 3380 | 99% |

*trend over deposit year: rising, z = +8.91, two-sided p = 5.3e-19 across 39 years and 8742 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.90, two-sided p = 0.00369 across 39 years and 284 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 2 lineages: mu = 99.6%, phi = 5.0 (intraclass correlation 0.168); worst lineage after shrinkage Alphavirus mayaro (3426306) at 16.5% (5.7%-31.5%, raw 0.0% on 25); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 339 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 3891 recent records share 18 distinct footprints (216.2 per footprint), of which 5 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 18 independent observations (one per footprint) the interval around the 99% detected share is 80%-100%, which no longer rules out the 90% threshold; with only 18 and 54 independent observations the fall from baseline is -14% to +15%, which no longer excludes zero. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 8742 of 17854 screened records are evaluable (49.0%); 9112 are not. Every share above is taken over the evaluable ones.

Excluded: 295 indeterminate, 8817 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 8767 no_site, 31 chance_anchor, 19 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 198 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1034 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7733 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Apicomplexa_23S_Zhu_2000`

Apicomplexa — 23S rRNA (apicoplast) (Zhu 2000)  
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
| 2026 | 0 | 6 | 0% |

*trend over deposit year: not tested (fewer than 3 years with evaluable records, or no variation); by distinct footprint: not tested (fewer than 3 years with footprints, or no variation). Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Duplication check:** 29 recent records share 6 distinct footprints (4.8 per footprint), of which 29 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 6 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 114 of 332 screened records are evaluable (34.3%); 218 are not. Every share above is taken over the evaluable ones.

Excluded: 218 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 200 no_site, 15 chance_anchor, 3 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 113 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 47 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 153 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Avipoxvirus_4b_Baek_2020`

Avipoxvirus — 4b core protein (Baek 2020)  
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

*trend over deposit year: rising, z = +0.57, two-sided p = 0.567 across 26 years and 1083 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +1.44, two-sided p = 0.15 across 26 years and 212 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Patent records:** 7 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 78 recent records share 5 distinct footprints (15.6 per footprint), of which 26 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 5 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 1083 of 1727 screened records are evaluable (62.7%); 644 are not. Every share above is taken over the evaluable ones.

Excluded: 644 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 616 no_site, 18 truncated, 10 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 328 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 12 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 604 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Helicobacter_16S_Conley_2021`

Helicobacter — 16S rRNA (Conley 2021)  
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

*trend over deposit year: not tested (fewer than 3 years with evaluable records, or no variation); by distinct footprint: not tested (fewer than 3 years with footprints, or no variation). Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Patent records:** 1 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 75 recent records share 6 distinct footprints (12.5 per footprint), of which 57 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 6 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 1155 of 3025 screened records are evaluable (38.2%); 1870 are not. Every share above is taken over the evaluable ones.

Excluded: 1870 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1110 no_site, 616 truncated, 141 no_pair, 3 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 360 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1110 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Influenza_A_virus_HA_H3_Shu_2026`

Influenza A virus — HA (haemagglutinin), H3 (Shu 2026)  
Designed 2008, doi:10.1128/jcm.00727-26  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1982 | 0 | 1 | 0% |
| 1983 | 0 | 1 | 0% |
| 1987 | 0 | 3 | 0% |
| 1989 | 0 | 21 | 0% |
| 1990 | 0 | 2 | 0% |
| 1991 | 0 | 1 | 0% |
| 1992 | 0 | 6 | 0% |
| 1993 | 0 | 7 | 0% |
| 1994 | 4 | 18 | 22% |
| 1995 | 2 | 11 | 18% |
| 1996 | 0 | 1 | 0% |
| 1997 | 2 | 6 | 33% |
| 1998 | 0 | 5 | 0% |
| 1999 | 9 | 13 | 69% |
| 2000 | 7 | 13 | 54% |
| 2001 | 41 | 56 | 73% |
| 2002 | 0 | 11 | 0% |
| 2003 | 3 | 10 | 30% |
| 2004 | 116 | 257 | 45% |
| 2005 | 615 | 698 | 88% |
| 2006 | 763 | 865 | 88% |
| 2007 | 711 | 1030 | 69% |
| 2008 | 595 | 1903 | 31% |
| 2009 | 126 | 901 | 14% |
| 2010 | 18 | 636 | 3% |
| 2011 | 176 | 831 | 21% |
| 2012 | 486 | 2030 | 24% |
| 2013 | 262 | 3521 | 7% |
| 2014 | 186 | 2685 | 7% |
| 2015 | 301 | 4232 | 7% |
| 2016 | 202 | 3593 | 6% |
| 2017 | 63 | 5778 | 1% |
| 2018 | 67 | 4334 | 2% |
| 2019 | 29 | 7192 | 0.4% |
| 2020 | 48 | 2134 | 2% |
| 2021 | 10 | 808 | 1% |
| 2022 | 52 | 7281 | 0.7% |
| 2023 | 26 | 6192 | 0.4% |
| 2024 | 80 | 8724 | 0.9% |
| 2025 | 24 | 13412 | 0.2% |
| 2026 | 28 | 12450 | 0.2% |

*trend over deposit year: falling, z = -132.94, two-sided p = 0 across 41 years and 91673 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -12.95, two-sided p = 2.27e-38 across 41 years and 3871 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 0.2%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 26806 recent records share 503 distinct footprints (53.3 per footprint), of which 37 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 503 independent observations (one per footprint) the interval around the 0.2% detected share is 0%-1%, and counting each footprint once, 12 of 503 footprints amplify (2%; interval 1%-4%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 91673 of 108821 screened records are evaluable (84.2%); 17148 are not. Every share above is taken over the evaluable ones.

Excluded: 10 indeterminate, 17138 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 8343 truncated, 6984 no_site, 1773 chance_pair, 38 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 87 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 12 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 6972 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthobunyavirus_M_Briese_2007_BUN_M_IXf`

Orthobunyavirus — M segment (Briese 2007, BUN M IXf)  
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
| 2017 | 13 | 30 | 43% |
| 2018 | 5 | 10 | 50% |
| 2019 | 1 | 27 | 4% |
| 2020 | 2 | 3 | 67% |
| 2021 | 8 | 10 | 80% |
| 2022 | 7 | 12 | 58% |
| 2023 | 3 | 20 | 15% |
| 2024 | 0 | 19 | 0% |
| 2025 | 0 | 104 | 0% |
| 2026 | 1 | 187 | 0.5% |

*trend over deposit year: falling, z = -11.20, two-sided p = 3.87e-29 across 28 years and 558 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.55, two-sided p = 0.0108 across 28 years and 153 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 0.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 296 recent records share 11 distinct footprints (26.9 per footprint), of which 7 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 11 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 558 of 2083 screened records are evaluable (26.8%); 1525 are not. Every share above is taken over the evaluable ones.

Excluded: 1525 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1296 no_site, 179 chance_only, 47 chance_anchor, 2 no_pair, 1 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 27 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 887 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 409 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthopoxvirus_F3L_Huo_2022`

Orthopoxvirus — F3L region (positions 46313-46491 of ON563414.2) (Huo 2022)  
Designed 2022, doi:10.1016/j.bsheal.2022.10.005  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1984 | 0 | 0 | - |
| 1985 | 0 | 0 | - |
| 1986 | 0 | 0 | - |
| 1987 | 0 | 0 | - |
| 1988 | 0 | 0 | - |
| 1989 | 0 | 0 | - |
| 1990 | 0 | 0 | - |
| 1991 | 2 | 2 | 100% |
| 1992 | 0 | 0 | - |
| 1993 | 4 | 4 | 100% |
| 1994 | 1 | 1 | 100% |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 1 | 1 | 100% |
| 1998 | 1 | 1 | 100% |
| 1999 | 3 | 3 | 100% |
| 2000 | 1 | 1 | 100% |
| 2001 | 2 | 4 | 50% |
| 2002 | 5 | 5 | 100% |
| 2003 | 2 | 2 | 100% |
| 2004 | 3 | 4 | 75% |
| 2005 | 5 | 12 | 42% |
| 2006 | 66 | 66 | 100% |
| 2007 | 4 | 4 | 100% |
| 2008 | 1 | 1 | 100% |
| 2009 | 0 | 0 | - |
| 2010 | 0 | 3 | 0% |
| 2011 | 11 | 13 | 85% |
| 2012 | 15 | 16 | 94% |
| 2013 | 31 | 33 | 94% |
| 2014 | 42 | 66 | 64% |
| 2015 | 6 | 17 | 35% |
| 2016 | 2 | 4 | 50% |
| 2017 | 38 | 40 | 95% |
| 2018 | 16 | 21 | 76% |
| 2019 | 24 | 33 | 73% |
| 2020 | 16 | 54 | 30% |
| 2021 | 24 | 24 | 100% |
| 2022 | 15 | 3461 | 0.4% |
| 2023 | 15 | 3147 | 0.5% |
| 2024 | 36 | 2135 | 2% |
| 2025 | 6 | 2215 | 0.3% |
| 2026 | 23 | 3279 | 0.7% |

*trend over deposit year: falling, z = -69.15, two-sided p = 0 across 32 years and 14672 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -5.54, two-sided p = 3.05e-08 across 32 years and 124 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 0.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 1272 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 5686 recent records share 21 distinct footprints (270.8 per footprint), of which 498 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 21 independent observations (one per footprint) the interval around the 0.5% detected share is 0%-16%, and counting each footprint once, 3 of 21 footprints amplify (14%; interval 5%-35%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 14672 of 17579 screened records are evaluable (83.5%); 2907 are not. Every share above is taken over the evaluable ones.

Excluded: 12 indeterminate, 2895 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 2892 no_site, 3 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 564 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 4 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 2888 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Polyomaviridae_VP1_Johne_2005_round1`

Polyomaviridae — VP1 (Johne 2005), nested round 1  
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
| 2019 | 3 | 259 | 1% |
| 2020 | 0 | 43 | 0% |
| 2021 | 0 | 63 | 0% |
| 2022 | 1 | 144 | 0.7% |
| 2023 | 0 | 201 | 0% |
| 2024 | 0 | 360 | 0% |
| 2025 | 0 | 349 | 0% |
| 2026 | 5 | 230 | 2% |

*trend over deposit year: rising, z = +0.56, two-sided p = 0.574 across 37 years and 2365 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.79, two-sided p = 0.427 across 37 years and 425 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 0.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Per species** (product size names the species here, 829-1137 bp, so the share above pools readouts that mean different things; Nov 2024 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Betapolyomavirus hominis (1891762) | - | 0 | 548 | 0% |
| Polyomaviridae sp. (2202645) | - | 5 | 20 | 25% |
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

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Homo sapiens (9606) |  | 0 | 0 | 0 | 0% |
| synthetic construct (32630) |  | 0 | 0 | 0 | 0% |
| Cricetulus griseus (10029) |  | 0 | 0 | 0 | 0% |
| Mirounga angustirostris polyomavirus 1 (3902555) |  | 0 | 0 | 0 | 0% |


**Patent records:** 372 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 650 recent records share 36 distinct footprints (18.1 per footprint), of which 54 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 36 independent observations (one per footprint) the interval around the 0.8% detected share is 0%-11%, and counting each footprint once, 1 of 36 footprints amplify (3%; interval 0.5%-14%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 2365 of 14239 screened records are evaluable (16.6%); 11874 are not. Every share above is taken over the evaluable ones.

Excluded: 11874 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 8492 no_site, 2016 truncated, 1358 chance_anchor, 8 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 299 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 44 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 8448 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Polyomaviridae_VP1_Johne_2005`

Polyomaviridae — VP1 (Johne 2005)  
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
| 2019 | 194 | 544 | 36% |
| 2020 | 33 | 68 | 49% |
| 2021 | 9 | 123 | 7% |
| 2022 | 9 | 191 | 5% |
| 2023 | 28 | 267 | 10% |
| 2024 | 36 | 386 | 9% |
| 2025 | 3 | 436 | 0.7% |
| 2026 | 14 | 479 | 3% |

*trend over deposit year: rising, z = +10.36, two-sided p = 3.66e-25 across 41 years and 6648 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.85, two-sided p = 0.393 across 41 years and 720 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 0.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Out of scope:** 7 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| synthetic construct (32630) |  | 0 | 0 | 2 | 0% |
| Mirounga angustirostris polyomavirus 1 (3902555) |  | 0 | 0 | 2 | 0% |
| Homo sapiens (9606) |  | 0 | 0 | 0 | 0% |
| Cricetulus griseus (10029) |  | 0 | 0 | 0 | 0% |


**Patent records:** 372 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 990 recent records share 46 distinct footprints (21.5 per footprint), of which 35 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 46 independent observations (one per footprint) the interval around the 2% detected share is 0.3%-11%, and counting each footprint once, 9 of 46 footprints amplify (20%; interval 11%-33%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 6648 of 14239 screened records are evaluable (46.7%); 7591 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 7590 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 7157 no_site, 430 truncated, 3 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 179 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7157 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Polyomaviridae_VP1_Johne_2005_round2`

Polyomaviridae — VP1 (Johne 2005), nested round 2  
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
| 2019 | 194 | 544 | 36% |
| 2020 | 33 | 68 | 49% |
| 2021 | 9 | 123 | 7% |
| 2022 | 9 | 191 | 5% |
| 2023 | 28 | 267 | 10% |
| 2024 | 36 | 386 | 9% |
| 2025 | 3 | 436 | 0.7% |
| 2026 | 14 | 479 | 3% |

*trend over deposit year: rising, z = +10.36, two-sided p = 3.66e-25 across 41 years and 6648 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.85, two-sided p = 0.393 across 41 years and 720 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 0.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Out of scope:** 7 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| synthetic construct (32630) |  | 0 | 0 | 2 | 0% |
| Mirounga angustirostris polyomavirus 1 (3902555) |  | 0 | 0 | 2 | 0% |
| Homo sapiens (9606) |  | 0 | 0 | 0 | 0% |
| Cricetulus griseus (10029) |  | 0 | 0 | 0 | 0% |


**Patent records:** 372 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 990 recent records share 46 distinct footprints (21.5 per footprint), of which 35 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 46 independent observations (one per footprint) the interval around the 2% detected share is 0.3%-11%, and counting each footprint once, 9 of 46 footprints amplify (20%; interval 11%-33%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 6648 of 14239 screened records are evaluable (46.7%); 7591 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 7590 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 7157 no_site, 430 truncated, 3 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Counted as failures, NOT excluded: 179 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7157 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Chordopoxvirinae_POL_Bracht_2006`

Chordopoxvirinae — DNA polymerase (Bracht 2006)  
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
| 2002 | 11 | 16 | 69% |
| 2003 | 4 | 8 | 50% |
| 2004 | 3 | 8 | 38% |
| 2005 | 7 | 23 | 30% |
| 2006 | 0 | 19 | 0% |
| 2007 | 0 | 6 | 0% |
| 2008 | 0 | 1 | 0% |
| 2009 | 1 | 1 | 100% |
| 2010 | 0 | 8 | 0% |
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
| 2021 | 18 | 45 | 40% |
| 2022 | 31 | 3491 | 0.9% |
| 2023 | 64 | 3185 | 2% |
| 2024 | 45 | 2152 | 2% |
| 2025 | 98 | 2244 | 4% |
| 2026 | 99 | 3196 | 3% |

*trend over deposit year: falling, z = -11.64, two-sided p = 2.67e-31 across 33 years and 14983 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.69, two-sided p = 0.492 across 33 years and 193 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 2 lineages: mu = 3.4%, phi = 0.0 (intraclass correlation 0.995); worst lineage after shrinkage Orthopoxvirus monkeypox (3431483) at 0.0% (0.0%-0.0%, raw 0.0% on 5377); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 1439 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 5650 recent records share 17 distinct footprints (332.4 per footprint), of which 2 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 17 independent observations (one per footprint) the interval around the 4% detected share is 0.5%-24%, and counting each footprint once, 4 of 17 footprints amplify (24%; interval 10%-47%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 14983 of 28430 screened records are evaluable (52.7%); 13447 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 13446 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 13104 no_site, 242 chance_anchor, 97 truncated, 3 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 16 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 498 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 12606 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Serpentovirinae_PP1b_Uccellini_2014_PythonNido6F`

Serpentovirinae — PP1b (Uccellini 2014, PythonNido6F)  
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

*trend over deposit year: falling, z = -2.61, two-sided p = 0.00913 across 10 years and 60 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.01, two-sided p = 0.315 across 10 years and 42 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Patent records:** 11 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 23 recent records share 14 distinct footprints (1.6 per footprint), of which 4 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 14 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 60 of 279 screened records are evaluable (21.5%); 219 are not. Every share above is taken over the evaluable ones.

Excluded: 219 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 151 no_site, 56 truncated, 12 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 4 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 8 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 143 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Monkeypox_virus_SNP183524_Huo_2022`

Monkeypox virus — SNP-typing locus at 183524-183539 of ON563414.2 (Huo 2022)  
Designed 2022, doi:10.1016/j.bsheal.2022.10.005  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1993 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 0 | 0 | - |
| 1998 | 0 | 0 | - |
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
| 2010 | 0 | 5 | 0% |
| 2011 | 0 | 2 | 0% |
| 2012 | 0 | 0 | - |
| 2013 | 0 | 1 | 0% |
| 2014 | 1 | 24 | 4% |
| 2015 | 5 | 11 | 45% |
| 2018 | 1 | 1 | 100% |
| 2019 | 8 | 8 | 100% |
| 2020 | 27 | 37 | 73% |
| 2022 | 69 | 3332 | 2% |
| 2023 | 8 | 3101 | 0.3% |
| 2024 | 128 | 2046 | 6% |
| 2025 | 406 | 1892 | 21% |
| 2026 | 31 | 2737 | 1% |

*trend over deposit year: rising, z = +3.86, two-sided p = 0.000115 across 16 years and 13208 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.05, two-sided p = 0.292 across 16 years and 70 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 9.1%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 5 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 4821 recent records share 15 distinct footprints (321.4 per footprint), of which 45 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 15 independent observations (one per footprint) the interval around the 9% detected share is 2%-33%, and counting each footprint once, 3 of 15 footprints amplify (20%; interval 7%-45%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 13208 of 14206 screened records are evaluable (93.0%); 998 are not. Every share above is taken over the evaluable ones.

Excluded: 16 indeterminate, 982 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 976 no_site, 5 chance_anchor, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 75 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 424 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 552 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Arenaviridae_S_Lozano_1997_ARS16V`

Arenaviridae — S segment (Lozano 1997, ARS16V)  
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

*trend over deposit year: falling, z = -4.09, two-sided p = 4.23e-05 across 39 years and 1058 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -3.52, two-sided p = 0.000437 across 39 years and 507 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Out of scope:** 473 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| unidentified Reptarenavirus (1654823) |  | 0 | 0 | 25 | 0% |
| taxid 1672385 |  | 0 | 0 | 5 | 0% |
| taxid 2447931 |  | 0 | 0 | 4 | 0% |
| Aurora borealis virus (1672381) |  | 0 | 0 | 2 | 0% |
| S5-like reptarenavirus (1938918) |  | 0 | 0 | 2 | 0% |
| taxid 1223561 |  | 0 | 0 | 2 | 0% |
| taxid 1223562 |  | 0 | 0 | 2 | 0% |
| taxid 2461343 |  | 0 | 0 | 1 | 0% |
| S10-like virus (2301526) |  | 0 | 0 | 1 | 0% |
| S7-like reptarenavirus (2448019) |  | 0 | 0 | 1 | 0% |
| _+57 more taxa_ | | | | | |


**Patent records:** 226 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 69 recent records share 38 distinct footprints (1.8 per footprint), of which 39 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 38 independent observations (one per footprint) the interval around the 13% detected share is 6%-27%, and counting each footprint once, 9 of 38 footprints amplify (24%; interval 13%-39%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 1058 of 5755 screened records are evaluable (18.4%); 4697 are not. Every share above is taken over the evaluable ones.

Excluded: 3 indeterminate, 4694 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 3948 no_site, 367 chance_anchor, 320 truncated, 46 no_pair, 13 chance_only. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 405 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 2572 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1376 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthobunyavirus_L_Briese_2007`

Orthobunyavirus — L segment (Briese 2007)  
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

*trend over deposit year: falling, z = -4.20, two-sided p = 2.63e-05 across 23 years and 192 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.72, two-sided p = 0.00662 across 23 years and 109 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Duplication check:** 23 recent records share 13 distinct footprints (1.8 per footprint), of which 5 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: only 13 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 192 of 2143 screened records are evaluable (9.0%); 1951 are not. Every share above is taken over the evaluable ones.

Excluded: 1951 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1756 no_site, 112 truncated, 75 chance_anchor, 8 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 34 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1753 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 3 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Serpentovirinae_PP1b_Uccellini_2014_PythonNodoF`

Serpentovirinae — PP1b (Uccellini 2014, PythonNodoF)  
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

*trend over deposit year: falling, z = -2.40, two-sided p = 0.0165 across 11 years and 44 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.78, two-sided p = 0.0757 across 11 years and 34 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Patent records:** 11 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 17 recent records share 13 distinct footprints (1.3 per footprint). This flag does not hold up: only 13 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 44 of 279 screened records are evaluable (15.8%); 235 are not. Every share above is taken over the evaluable ones.

Excluded: 235 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 183 no_site, 50 chance_anchor, 2 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 38 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 145 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Apicomplexa_18S_Garner_2006`

Apicomplexa — 18S rRNA (Garner 2006)  
Designed 2006, doi:10.1354/vp.43-3-311  
**Degeneracy:** 128-fold degenerate (128-fold primers x 1-fold probe); ~7 cycles of Cq delay at best  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1989 | 0 | 1 | 0% |
| 1991 | 0 | 0 | - |
| 1992 | 4 | 8 | 50% |
| 1993 | 9 | 16 | 56% |
| 1994 | 8 | 15 | 53% |
| 1995 | 3 | 4 | 75% |
| 1996 | 3 | 6 | 50% |
| 1997 | 17 | 35 | 49% |
| 1998 | 29 | 35 | 83% |
| 1999 | 45 | 64 | 70% |
| 2000 | 4 | 16 | 25% |
| 2001 | 45 | 67 | 67% |
| 2002 | 15 | 32 | 47% |
| 2003 | 24 | 64 | 38% |
| 2004 | 26 | 113 | 23% |
| 2005 | 74 | 185 | 40% |
| 2006 | 32 | 78 | 41% |
| 2007 | 76 | 321 | 24% |
| 2008 | 122 | 399 | 31% |
| 2009 | 42 | 139 | 30% |
| 2010 | 110 | 303 | 36% |
| 2011 | 147 | 268 | 55% |
| 2012 | 144 | 317 | 45% |
| 2013 | 279 | 498 | 56% |
| 2014 | 201 | 495 | 41% |
| 2015 | 239 | 367 | 65% |
| 2016 | 289 | 631 | 46% |
| 2017 | 382 | 698 | 55% |
| 2018 | 326 | 708 | 46% |
| 2019 | 207 | 819 | 25% |
| 2020 | 263 | 697 | 38% |
| 2021 | 152 | 758 | 20% |
| 2022 | 105 | 428 | 25% |
| 2023 | 144 | 803 | 18% |
| 2024 | 241 | 975 | 25% |
| 2025 | 203 | 930 | 22% |
| 2026 | 173 | 548 | 32% |

*trend over deposit year: falling, z = -16.33, two-sided p = 5.99e-60 across 36 years and 11841 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.53, two-sided p = 0.0115 across 36 years and 1640 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 2 lineages: mu = 100.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 1649 recent records share 134 distinct footprints (12.3 per footprint), of which 1208 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 134 independent observations (one per footprint) the interval around the 24% detected share is 18%-32%, and counting each footprint once, 19 of 134 footprints amplify (14%; interval 9%-21%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 11841 of 56519 screened records are evaluable (21.0%); 44678 are not. Every share above is taken over the evaluable ones.

Excluded: 44678 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 30972 no_site, 12840 truncated, 494 no_pair, 372 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 7367 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1443 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 29529 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthobunyavirus_S_Briese_2007_BUNS_5_U_6`

Orthobunyavirus — S segment (Briese 2007, BUNS 5 U 6)  
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
| 2002 | 3 | 9 | 33% |
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
| 2013 | 4 | 8 | 50% |
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

*trend over deposit year: falling, z = -2.68, two-sided p = 0.0074 across 26 years and 181 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.20, two-sided p = 0.228 across 26 years and 118 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Per species** (product size names the species here, 283-1120 bp, so the share above pools readouts that mean different things; Nov 2022 on, no assessability floor):

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

### `Haemosporida_cytb_Hellgren_2004_HaemF`

Haemosporida — cytochrome b (Hellgren 2004, HaemF)  
Designed 2004, doi:10.1645/GE-184R1  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1998 | 3 | 4 | 75% |
| 2000 | 0 | 0 | - |
| 2002 | 24 | 51 | 47% |
| 2003 | 0 | 0 | - |
| 2004 | 3 | 5 | 60% |
| 2005 | 1 | 63 | 2% |
| 2006 | 5 | 26 | 19% |
| 2007 | 0 | 22 | 0% |
| 2008 | 0 | 60 | 0% |
| 2009 | 8 | 38 | 21% |
| 2010 | 32 | 85 | 38% |
| 2011 | 9 | 83 | 11% |
| 2012 | 1 | 29 | 3% |
| 2013 | 9 | 17 | 53% |
| 2014 | 2 | 270 | 0.7% |
| 2015 | 8 | 67 | 12% |
| 2016 | 9 | 40 | 22% |
| 2017 | 119 | 306 | 39% |
| 2018 | 64 | 113 | 57% |
| 2019 | 11 | 54 | 20% |
| 2020 | 5 | 262 | 2% |
| 2021 | 10 | 16 | 62% |
| 2022 | 88 | 96 | 92% |
| 2023 | 37 | 125 | 30% |
| 2024 | 32 | 86 | 37% |
| 2025 | 67 | 201 | 33% |
| 2026 | 17 | 108 | 16% |

*trend over deposit year: rising, z = +5.89, two-sided p = 3.94e-09 across 25 years and 2227 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +6.18, two-sided p = 6.38e-10 across 25 years and 554 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 2 lineages: mu = 54.0%, phi = 0.3 (intraclass correlation 0.777); worst lineage after shrinkage Haemoproteus syrnii (379410) at 0.6% (0.0%-4.8%, raw 0.0% on 27); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 16087 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Hepatocystis sp. SSJ-2010 (903504) |  | 125 | 125 | 125 | 100% |
| Hepatocystis sp. TLG-2012 (1266736) |  | 74 | 74 | 74 | 100% |
| Plasmodium floridense (31275) |  | 65 | 65 | 65 | 100% |
| Plasmodium billcollinsi (720590) |  | 42 | 42 | 42 | 100% |
| Plasmodium blacklocki (nom. inval.) (880536) |  | 35 | 35 | 35 | 100% |
| Plasmodium tupinambi (3448513) |  | 29 | 29 | 29 | 100% |
| Polychromophilus murinus (1147704) |  | 28 | 28 | 28 | 100% |
| taxid 864142 |  | 25 | 25 | 25 | 100% |
| Plasmodiidae sp. (2605378) |  | 22 | 22 | 22 | 100% |
| Polychromophilus sp. (1715677) |  | 19 | 19 | 19 | 100% |
| _+3162 more taxa_ | | | | | |


**Duplication check:** 313 recent records share 36 distinct footprints (8.7 per footprint), of which 134 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 36 independent observations (one per footprint) the interval around the 27% detected share is 15%-43%, and counting each footprint once, 19 of 36 footprints amplify (53%; interval 37%-68%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 2227 of 15966 screened records are evaluable (13.9%); 13739 are not. Every share above is taken over the evaluable ones.

Excluded: 13739 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 12487 no_site, 1232 truncated, 20 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 1190 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 5 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 12482 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Circoviridae_Rep_Mankertz_2000_round2`

Circoviridae — Rep (Mankertz 2000), nested round 2  
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
| 2005 | 42 | 103 | 41% |
| 2006 | 21 | 73 | 29% |
| 2007 | 15 | 171 | 9% |
| 2008 | 40 | 156 | 26% |
| 2009 | 70 | 201 | 35% |
| 2010 | 51 | 180 | 28% |
| 2011 | 100 | 272 | 37% |
| 2012 | 178 | 269 | 66% |
| 2013 | 162 | 257 | 63% |
| 2014 | 269 | 469 | 57% |
| 2015 | 142 | 366 | 39% |
| 2016 | 238 | 401 | 59% |
| 2017 | 312 | 631 | 49% |
| 2018 | 167 | 396 | 42% |
| 2019 | 226 | 520 | 43% |
| 2020 | 57 | 269 | 21% |
| 2021 | 174 | 770 | 23% |
| 2022 | 277 | 722 | 38% |
| 2023 | 503 | 1097 | 46% |
| 2024 | 235 | 1077 | 22% |
| 2025 | 139 | 387 | 36% |
| 2026 | 81 | 329 | 25% |

*trend over deposit year: falling, z = -4.75, two-sided p = 2.05e-06 across 31 years and 9405 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -4.33, two-sided p = 1.48e-05 across 31 years and 1110 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 3 lineages: mu = 50.3%, phi = 2.4 (intraclass correlation 0.290); worst lineage after shrinkage Circovirus pigeon (3050342) at 1.7% (0.1%-5.7%, raw 0.0% on 69); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 222 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 741 recent records share 79 distinct footprints (9.4 per footprint), of which 276 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 79 independent observations (one per footprint) the interval around the 30% detected share is 21%-41%, and counting each footprint once, 18 of 79 footprints amplify (23%; interval 15%-33%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 9405 of 24095 screened records are evaluable (39.0%); 14690 are not. Every share above is taken over the evaluable ones.

Excluded: 14690 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 14121 no_site, 421 truncated, 89 no_pair, 59 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 1703 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 14121 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Plasmodium_18S_Li_1995`

Plasmodium — 18S rRNA (Li 1995)  
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

*trend over deposit year: falling, z = -4.31, two-sided p = 1.6e-05 across 33 years and 734 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.60, two-sided p = 0.547 across 33 years and 92 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Duplication check:** 22 recent records share 2 distinct footprints (11.0 per footprint). This flag does not hold up: only 2 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything; counting each footprint once, 1 of 2 footprints amplify (50%; interval 9%-91%), which reaches the 90% threshold: the failing records are concentrated on few footprints. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 734 of 2712 screened records are evaluable (27.1%); 1978 are not. Every share above is taken over the evaluable ones.

Excluded: 1978 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1426 no_site, 538 truncated, 7 chance_only, 5 no_pair, 2 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 15 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 705 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 721 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Astroviridae_RdRp_Chu_2008_round1`

Astroviridae — RNA-dependent RNA polymerase (Chu 2008), nested round 1  
Designed 2008, doi:10.1128/jvi.00857-08  
**Degeneracy:** 2048-fold degenerate (2048-fold primers x 1-fold probe); each member is ~4.9e-04 of the reaction, ~11 cycles of Cq delay at best, and bench sensitivity is well below in-silico coverage  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1992 | 0 | 0 | - |
| 1993 | 3 | 3 | 100% |
| 1994 | 4 | 4 | 100% |
| 1995 | 0 | 0 | - |
| 1996 | 0 | 0 | - |
| 1997 | 4 | 4 | 100% |
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
| 2011 | 28 | 46 | 61% |
| 2012 | 24 | 53 | 45% |
| 2013 | 23 | 37 | 62% |
| 2014 | 20 | 38 | 53% |
| 2015 | 31 | 62 | 50% |
| 2016 | 77 | 105 | 73% |
| 2017 | 20 | 82 | 24% |
| 2018 | 59 | 100 | 59% |
| 2019 | 84 | 137 | 61% |
| 2020 | 53 | 147 | 36% |
| 2021 | 95 | 199 | 48% |
| 2022 | 153 | 320 | 48% |
| 2023 | 248 | 458 | 54% |
| 2024 | 120 | 221 | 54% |
| 2025 | 122 | 466 | 26% |
| 2026 | 89 | 190 | 47% |

*trend over deposit year: falling, z = -5.45, two-sided p = 4.94e-08 across 29 years and 2925 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.42, two-sided p = 0.0155 across 29 years and 875 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 7 lineages: mu = 29.3%, phi = 0.9 (intraclass correlation 0.530); worst lineage after shrinkage Avastrovirus intestini (3426506) at 1.7% (0.0%-11.6%, raw 0.0% on 14); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Per species** (product size names the species here, 337-477 bp, so the share above pools readouts that mean different things; Nov 2024 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Mamastrovirus sp. (1912147) | - | 18 | 126 | 14% |
| Mamastrovirus suisvulgaris (3703182) | - | 2 | 87 | 2% |
| Porcine astrovirus 2 (1105378) | - | 9 | 48 | 19% |
| Goose astrovirus (1349999) | - | 42 | 45 | 93% |
| Bovine astrovirus (1435485) | - | 15 | 37 | 41% |
| Mamastrovirus suisencephalomyelitidis (3703181) | - | 3 | 35 | 9% |
| Mamastrovirus hominis (3430629) | - | 31 | 31 | 100% |
| Porcine astrovirus 5 (1093928) | - | 17 | 28 | 61% |
| Astroviridae sp. (2585114) | - | 2 | 18 | 11% |
| Human astrovirus (1868658) | - | 18 | 18 | 100% |
| Astroviridae (39733) | - | 12 | 17 | 71% |
| Caprine astrovirus (2870633) | - | 6 | 17 | 35% |
| Avastrovirus intestini (3426506) | - | 0 | 14 | 0% |
| Chicken astrovirus (336959) | - | 2 | 14 | 14% |
| Bat astrovirus (1697918) | - | 7 | 13 | 54% |
| Canine astrovirus (1157338) | - | 3 | 13 | 23% |
| Avastrovirus sp. (2809168) | - | 2 | 12 | 17% |
| Mamastrovirus ovis (3430634) | - | 7 | 11 | 64% |
| Astrovirus sp. (178530) | - | 1 | 7 | 14% |
| Mamastrovirus suisorientalis (3430637) | - | 4 | 7 | 57% |
| Goose astrovirus 2 (2810457) | - | 6 | 6 | 100% |
| Porcine astrovirus 1 (1559735) | - | 1 | 6 | 17% |
| Mamastrovirus (249588) | - | 0 | 4 | 0% |
| Mamastrovirus felis (3430626) | - | 4 | 4 | 100% |
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
| Possum astrovirus (3462434) | - | 1 | 2 | 50% |
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

**Duplication check:** 679 recent records share 105 distinct footprints (6.5 per footprint), of which 2 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 105 independent observations (one per footprint) the interval around the 34% detected share is 26%-44%, and counting each footprint once, 45 of 105 footprints amplify (43%; interval 34%-52%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 2925 of 16713 screened records are evaluable (17.5%); 13788 are not. Every share above is taken over the evaluable ones.

Excluded: 13788 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 11956 no_site, 1326 truncated, 488 chance_anchor, 17 chance_only, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 20 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 4054 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7902 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Chlamydia_16S_Messmer_1997_round1`

Chlamydia — 16S rRNA (Messmer 1997), nested round 1  
Designed 1997, doi:10.1128/jcm.35.8.2043-2046.1997  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 1989 | 0 | 0 | - |
| 1993 | 1 | 1 | 100% |
| 1995 | 2 | 2 | 100% |
| 1996 | 0 | 1 | 0% |
| 1997 | 66 | 77 | 86% |
| 1998 | 0 | 1 | 0% |
| 1999 | 2 | 2 | 100% |
| 2000 | 1 | 2 | 50% |
| 2001 | 0 | 1 | 0% |
| 2002 | 0 | 0 | - |
| 2003 | 9 | 9 | 100% |
| 2004 | 1 | 1 | 100% |
| 2005 | 1 | 22 | 5% |
| 2006 | 2 | 3 | 67% |
| 2007 | 1 | 2 | 50% |
| 2008 | 1 | 3 | 33% |
| 2009 | 2 | 12 | 17% |
| 2010 | 4 | 16 | 25% |
| 2011 | 16 | 21 | 76% |
| 2012 | 10 | 39 | 26% |
| 2013 | 8 | 38 | 21% |
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
| 2025 | 25 | 61 | 41% |
| 2026 | 6 | 19 | 32% |

*trend over deposit year: falling, z = -6.32, two-sided p = 2.62e-10 across 32 years and 814 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.10, two-sided p = 0.036 across 32 years and 127 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 0.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Patent records:** 1 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 85 recent records share 10 distinct footprints (8.5 per footprint). This flag does not hold up: only 10 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 814 of 1667 screened records are evaluable (48.8%); 853 are not. Every share above is taken over the evaluable ones.

Excluded: 853 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 432 truncated, 402 no_site, 13 chance_anchor, 6 chance_only. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 21 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 155 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 247 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Deformed_wing_virus_A_polyprotein_Rossi_2024`

Deformed wing virus A — polyprotein (Rossi 2024)  
Designed 2024, doi:10.3390/microorganisms12061105  

| deposit year | detected | evaluable | share |
|---|---|---|---|
| 2022 | 5 | 6 | 83% |
| 2023 | 28 | 32 | 88% |
| 2024 | 2 | 2 | 100% |
| 2025 | 5 | 21 | 24% |
| 2026 | 18 | 26 | 69% |

*trend over deposit year: falling, z = -2.65, two-sided p = 0.00812 across 5 years and 87 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -2.14, two-sided p = 0.0323 across 5 years and 32 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 1 lineages: mu = 48.9%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 47 recent records share 16 distinct footprints (2.9 per footprint). Both reductions leave the flag in place: with only 16 independent observations (one per footprint) the interval around the 49% detected share is 27%-71%, and counting each footprint once, 4 of 16 footprints amplify (25%; interval 10%-49%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 87 of 245 screened records are evaluable (35.5%); 158 are not. Every share above is taken over the evaluable ones.

Excluded: 158 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 142 no_site, 16 truncated. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match.

Of the `no_site` records, 3 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 139 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthobunyavirus_M_Briese_2007_M3560_F`

Orthobunyavirus — M segment (Briese 2007, M3560 F)  
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
| 2004 | 1 | 5 | 20% |
| 2005 | 0 | 0 | - |
| 2006 | 0 | 0 | - |
| 2007 | 0 | 5 | 0% |
| 2008 | 0 | 0 | - |
| 2009 | 2 | 6 | 33% |
| 2010 | 3 | 4 | 75% |
| 2011 | 0 | 0 | - |
| 2012 | 1 | 2 | 50% |
| 2013 | 4 | 5 | 80% |
| 2014 | 9 | 29 | 31% |
| 2015 | 3 | 20 | 15% |
| 2016 | 7 | 21 | 33% |
| 2017 | 16 | 29 | 55% |
| 2018 | 3 | 13 | 23% |
| 2019 | 5 | 10 | 50% |
| 2020 | 1 | 7 | 14% |
| 2021 | 6 | 11 | 55% |
| 2022 | 2 | 4 | 50% |
| 2023 | 3 | 6 | 50% |
| 2024 | 5 | 9 | 56% |
| 2025 | 1 | 2 | 50% |
| 2026 | 1 | 1 | 100% |

*trend over deposit year: falling, z = -1.62, two-sided p = 0.104 across 29 years and 227 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.63, two-sided p = 0.529 across 29 years and 152 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Per species** (product size names the species here, 201-1090 bp, so the share above pools readouts that mean different things; Nov 2022 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Orthobunyavirus oropoucheense (3052429) | - | 5 | 10 | 50% |
| Orthobunyavirus bunyamweraense (3052381) | - | 2 | 2 | 100% |
| Orthobunyavirus kowanyamaense (3060477) | - | 1 | 2 | 50% |
| Orthobunyavirus manzanillaense (3052416) | - | 1 | 2 | 50% |
| Orthobunyavirus cacheense (3052385) | - | 1 | 1 | 100% |
| Orthobunyavirus lacrosseense (3052409) | - | 1 | 1 | 100% |
| Orthobunyavirus schmallenbergense (3052437) | - | 1 | 1 | 100% |
| Orthobunyavirus trinitiense (3052451) | - | 0 | 1 | 0% |

**Duplication check:** 20 recent records share 14 distinct footprints (1.4 per footprint). This flag does not hold up: only 14 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 227 of 2083 screened records are evaluable (10.9%); 1856 are not. Every share above is taken over the evaluable ones.

Excluded: 1856 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1428 chance_only, 408 no_site, 20 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 408 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 0 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Sarcocystis_18S_5_8S_Kutkiene_2010_ShortITS1R`

Sarcocystis — 18S-ITS1-5.8S rDNA (Kutkienė 2010, ShortITS1R)  
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
| 2017 | 3 | 7 | 43% |
| 2018 | 22 | 31 | 71% |
| 2019 | 0 | 21 | 0% |
| 2020 | 5 | 5 | 100% |
| 2021 | 6 | 6 | 100% |
| 2022 | 0 | 0 | - |
| 2023 | 4 | 4 | 100% |
| 2024 | 7 | 8 | 88% |
| 2025 | 0 | 6 | 0% |
| 2026 | 0 | 0 | - |

*trend over deposit year: rising, z = +2.38, two-sided p = 0.0171 across 16 years and 190 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +2.27, two-sided p = 0.0233 across 16 years and 38 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Per species** (product size names the species here, 225-846 bp, so the share above pools readouts that mean different things; Nov 2022 on, no assessability floor):

| species | product bp | detected | evaluable | share |
|---|---|---|---|---|
| Sarcocystis calchasi (1344799) | 247-248 | 7 | 8 | 88% |
| Sarcocystis arctica (1434935) | 254 | 4 | 4 | 100% |
| Sarcocystis chenggongensis (3475062) | - | 0 | 4 | 0% |
| Sarcocystis medusiformis (1929461) | - | 0 | 2 | 0% |

**Duplication check:** 18 recent records share 5 distinct footprints (3.6 per footprint). This flag does not hold up: only 5 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 190 of 30875 screened records are evaluable (0.6%); 30685 are not. Every share above is taken over the evaluable ones.

Excluded: 30685 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 28571 no_site, 1739 truncated, 287 chance_anchor, 88 chance_only. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Of the `no_site` records, 20657 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 7914 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Paramyxoviridae_L_Tong_2008_round2`

Paramyxoviridae — L (polymerase) (Tong 2008), nested round 2  
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
| 2026 | 1764 | 2312 | 76% |

*trend over deposit year: rising, z = +40.57, two-sided p = 0 across 36 years and 8880 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +1.37, two-sided p = 0.17 across 36 years and 1039 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 6 lineages: mu = 65.1%, phi = 0.2 (intraclass correlation 0.856); worst lineage after shrinkage Respirovirus pneumoniae (3049953) at 0.0% (0.0%-0.2%, raw 0.0% on 550); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 73 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Pyeongtaek Microtus paramyxovirus (3412626) |  | 0 | 0 | 0 | 0% |


**Duplication check:** 3968 recent records share 150 distinct footprints (26.5 per footprint), of which 42 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 150 independent observations (one per footprint) the interval around the 62% detected share is 54%-69%, and counting each footprint once, 10 of 150 footprints amplify (7%; interval 4%-12%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 8880 of 15372 screened records are evaluable (57.8%); 6492 are not. Every share above is taken over the evaluable ones.

Excluded: 11 indeterminate, 6481 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 5909 no_site, 498 chance_anchor, 72 truncated, 2 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 165 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 1604 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 4305 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Avipoxvirus_4b_Farias_2010`

Avipoxvirus — 4b core protein (Farias 2010)  
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
| 2022 | 14 | 17 | 82% |
| 2023 | 28 | 29 | 97% |
| 2024 | 7 | 8 | 88% |
| 2025 | 14 | 15 | 93% |
| 2026 | 1 | 8 | 12% |

*trend over deposit year: falling, z = -0.99, two-sided p = 0.322 across 21 years and 253 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -1.17, two-sided p = 0.241 across 21 years and 57 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

**Patent records:** 7 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 24 recent records share 6 distinct footprints (4.0 per footprint). This flag does not hold up: only 6 distinct footprint(s), fewer than the 15 independent observations the record-level rule needs before it will flag anything.

**Denominator:** 253 of 1727 screened records are evaluable (14.6%); 1474 are not. Every share above is taken over the evaluable ones.

Excluded: 1474 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 1389 no_site, 55 truncated, 30 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 2 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 92 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 1297 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Cryptosporidium_18S_Xiao_1999_round2`

Cryptosporidium — 18S rRNA (Xiao 1999), nested round 2  
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
| 2022 | 46 | 58 | 79% |
| 2023 | 144 | 345 | 42% |
| 2024 | 104 | 139 | 75% |
| 2025 | 99 | 114 | 87% |
| 2026 | 59 | 101 | 58% |

*trend over deposit year: falling, z = -6.51, two-sided p = 7.51e-11 across 32 years and 1662 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -0.94, two-sided p = 0.345 across 32 years and 375 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 2 lineages: mu = 100.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Duplication check:** 224 recent records share 32 distinct footprints (7.0 per footprint), of which 56 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 32 independent observations (one per footprint) the interval around the 71% detected share is 54%-84%, and counting each footprint once, 8 of 32 footprints amplify (25%; interval 13%-42%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 1662 of 15052 screened records are evaluable (11.0%); 13390 are not. Every share above is taken over the evaluable ones.

Excluded: 13390 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 10907 no_site, 2407 truncated, 43 chance_anchor, 33 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 484 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 0 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 10907 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Paramyxoviridae_L_Tong_2008_round1`

Paramyxoviridae — L (polymerase) (Tong 2008), nested round 1  
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
| 2000 | 11 | 19 | 58% |
| 2001 | 8 | 18 | 44% |
| 2002 | 5 | 11 | 45% |
| 2003 | 14 | 23 | 61% |
| 2004 | 13 | 45 | 29% |
| 2005 | 22 | 26 | 85% |
| 2006 | 6 | 17 | 35% |
| 2007 | 8 | 22 | 36% |
| 2008 | 14 | 29 | 48% |
| 2009 | 23 | 66 | 35% |
| 2010 | 14 | 57 | 25% |
| 2011 | 42 | 65 | 65% |
| 2012 | 73 | 156 | 47% |
| 2013 | 38 | 154 | 25% |
| 2014 | 50 | 209 | 24% |
| 2015 | 84 | 147 | 57% |
| 2016 | 43 | 120 | 36% |
| 2017 | 84 | 555 | 15% |
| 2018 | 111 | 519 | 21% |
| 2019 | 111 | 467 | 24% |
| 2020 | 299 | 688 | 43% |
| 2021 | 270 | 709 | 38% |
| 2022 | 368 | 694 | 53% |
| 2023 | 319 | 542 | 59% |
| 2024 | 425 | 1165 | 36% |
| 2025 | 964 | 1780 | 54% |
| 2026 | 2105 | 2429 | 87% |

*trend over deposit year: rising, z = +25.36, two-sided p = 7.05e-142 across 37 years and 10788 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +2.15, two-sided p = 0.0319 across 37 years and 1371 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 9 lineages: mu = 74.6%, phi = 0.1 (intraclass correlation 0.946); worst lineage after shrinkage Respirovirus pneumoniae (3049953) at 0.0% (0.0%-0.1%, raw 0.0% on 548); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Out of scope:** 73 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Pyeongtaek Microtus paramyxovirus (3412626) |  | 6 | 6 | 6 | 100% |


**Duplication check:** 4276 recent records share 187 distinct footprints (22.9 per footprint), of which 69 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 187 independent observations (one per footprint) the interval around the 73% detected share is 66%-79%, and counting each footprint once, 95 of 187 footprints amplify (51%; interval 44%-58%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 10788 of 15372 screened records are evaluable (70.2%); 4584 are not. Every share above is taken over the evaluable ones.

Excluded: 7 indeterminate, 4577 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 4024 no_site, 416 truncated, 137 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 223 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 86 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 3938 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Astroviridae_RdRp_Chu_2008_round2`

Astroviridae — RNA-dependent RNA polymerase (Chu 2008), nested round 2  
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

*trend over deposit year: falling, z = -7.94, two-sided p = 2e-15 across 29 years and 3307 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -4.37, two-sided p = 1.25e-05 across 29 years and 847 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 7 lineages: mu = 79.1%, phi = 1.0 (intraclass correlation 0.489); worst lineage after shrinkage Goose astrovirus (1349999) at 1.8% (0.0%-6.9%, raw 0.0% on 46); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Per species** (product size names the species here, 367-489 bp, so the share above pools readouts that mean different things; Nov 2024 on, no assessability floor):

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
| Mamastrovirus felis (3430626) | - | 4 | 4 | 100% |
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

**Duplication check:** 704 recent records share 101 distinct footprints (7.0 per footprint), of which 2 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). Both reductions leave the flag in place: with only 101 independent observations (one per footprint) the interval around the 78% detected share is 69%-85%, and counting each footprint once, 71 of 101 footprints amplify (70%; interval 61%-78%); each is below the 90% threshold. So the flag does not rest on identical footprints deposited repeatedly.

**Denominator:** 3307 of 16713 screened records are evaluable (19.8%); 13406 are not. Every share above is taken over the evaluable ones.

Excluded: 13406 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 11765 no_site, 935 truncated, 501 chance_anchor, 204 chance_only, 1 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 6 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 4801 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 6964 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Orthoherpesviridae_POL_VanDevanter_1996_round2`

Orthoherpesviridae — DNA polymerase (VanDevanter 1996), nested round 2  
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
| 1994 | 1 | 1 | 100% |
| 1995 | 2 | 4 | 50% |
| 1996 | 0 | 1 | 0% |
| 1997 | 7 | 11 | 64% |
| 1998 | 1 | 6 | 17% |
| 1999 | 2 | 15 | 13% |
| 2000 | 4 | 15 | 27% |
| 2001 | 11 | 20 | 55% |
| 2002 | 7 | 9 | 78% |
| 2003 | 10 | 12 | 83% |
| 2004 | 22 | 41 | 54% |
| 2005 | 18 | 28 | 64% |
| 2006 | 12 | 17 | 71% |
| 2007 | 7 | 17 | 41% |
| 2008 | 9 | 16 | 56% |
| 2009 | 6 | 17 | 35% |
| 2010 | 73 | 76 | 96% |
| 2011 | 74 | 92 | 80% |
| 2012 | 134 | 159 | 84% |
| 2013 | 54 | 67 | 81% |
| 2014 | 75 | 104 | 72% |
| 2015 | 195 | 235 | 83% |
| 2016 | 263 | 279 | 94% |
| 2017 | 182 | 216 | 84% |
| 2018 | 273 | 303 | 90% |
| 2019 | 596 | 611 | 98% |
| 2020 | 66 | 69 | 96% |
| 2021 | 82 | 105 | 78% |
| 2022 | 162 | 231 | 70% |
| 2023 | 239 | 273 | 88% |
| 2024 | 322 | 359 | 90% |
| 2025 | 133 | 165 | 81% |
| 2026 | 100 | 120 | 83% |

*trend over deposit year: rising, z = +8.96, two-sided p = 3.15e-19 across 40 years and 3709 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: rising, z = +0.69, two-sided p = 0.488 across 40 years and 570 footprints. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 3 lineages: mu = 100.0%, lineages no more spread than binomial sampling predicts, so no shrinkage was applied and each posterior is the lineage alone*

**Out of scope:** 2 records excluded (taxid not in scope_taxids).

**Predicted cross-reactivity** (the out-of-scope records above, worst first). A share here is what the assay is predicted to amplify OFF target; for a probe assay a detection implies the probe bound too, because primers with no probe site between them score `fail`. Like every number here it is a prediction from sequence: read a high share as a reason to check the paper's exclusivity panel, not as a finding that the assay cross-reacts. A row marked `claimed` is a taxon the cited paper says this assay does NOT amplify (`target.exclusivity_taxids`), retrieved on purpose to test that claim; the rest are whatever else was in the archives this assay was screened against, which is a coincidence and not a panel.

| off-target taxon | claimed | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|
| Cervid gammaherpesvirus (3683214) |  | 0 | 0 | 0 | 0% |
| synthetic construct (32630) |  | 0 | 0 | 0 | 0% |


**Duplication check:** 356 recent records share 31 distinct footprints (11.5 per footprint), of which 3 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 31 independent observations (one per footprint) the interval around the 83% detected share is 66%-92%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 3709 of 7713 screened records are evaluable (48.1%); 4004 are not. Every share above is taken over the evaluable ones.

Excluded: 1 indeterminate, 4003 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 2274 no_site, 1122 truncated, 343 no_pair, 264 chance_anchor. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 36 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 20 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 2254 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

### `Adenoviridae_hexon_Casas_2005_round2`

Adenoviridae — hexon (Casas 2005), nested round 2  
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
| 1990 | 3 | 4 | 75% |
| 1991 | 0 | 0 | - |
| 1992 | 0 | 1 | 0% |
| 1993 | 11 | 12 | 92% |
| 1994 | 0 | 1 | 0% |
| 1995 | 3 | 3 | 100% |
| 1996 | 2 | 6 | 33% |
| 1997 | 1 | 2 | 50% |
| 1998 | 5 | 7 | 71% |
| 1999 | 13 | 13 | 100% |
| 2000 | 2 | 6 | 33% |
| 2001 | 20 | 23 | 87% |
| 2002 | 7 | 7 | 100% |
| 2003 | 40 | 42 | 95% |
| 2004 | 26 | 29 | 90% |
| 2005 | 100 | 107 | 93% |
| 2006 | 20 | 22 | 91% |
| 2007 | 27 | 34 | 79% |
| 2008 | 115 | 115 | 100% |
| 2009 | 100 | 103 | 97% |
| 2010 | 73 | 93 | 78% |
| 2011 | 69 | 80 | 86% |
| 2012 | 89 | 90 | 99% |
| 2013 | 165 | 168 | 98% |
| 2014 | 80 | 90 | 89% |
| 2015 | 149 | 165 | 90% |
| 2016 | 59 | 93 | 63% |
| 2017 | 151 | 180 | 84% |
| 2018 | 107 | 141 | 76% |
| 2019 | 156 | 189 | 83% |
| 2020 | 559 | 574 | 97% |
| 2021 | 498 | 516 | 97% |
| 2022 | 365 | 415 | 88% |
| 2023 | 583 | 618 | 94% |
| 2024 | 357 | 399 | 89% |
| 2025 | 384 | 483 | 80% |
| 2026 | 790 | 862 | 92% |

*trend over deposit year: rising, z = +0.70, two-sided p = 0.482 across 38 years and 5696 records (Cochran-Armitage; records are not independent, so read the direction and not the certainty); by distinct footprint, each binding-site footprint counted once per year: falling, z = -4.48, two-sided p = 7.51e-06 across 38 years and 698 footprints -- the two disagree on direction, so the by-record trend was carried by duplicated records. Read the by-record figure as an upper bound on the evidence and the by-footprint figure as nearer a lower bound: duplicated deposits inflate the first, sequencing errors in a primer site inflate the second*

*hierarchical fit over 5 lineages: mu = 94.2%, phi = 0.4 (intraclass correlation 0.720); worst lineage after shrinkage Aviadenovirus hepatitidis (3426530) at 0.7% (0.0%-4.3%, raw 0.0% on 49); P(some lineage < 90%) = 1.000 treating lineages as independent given the fit. Reported beside the verdict; not a verdict input (C1 hierarchical, docs/bayesian-scoring-plan.md)*

**Patent records:** 1043 excluded (GenBank patent division; drift.exclude_patent_records).

**Duplication check:** 1429 recent records share 87 distinct footprints (16.4 per footprint), of which 27 records are grouped only by taxon (promoted `diverged` rows, which were never scored and so have no mismatch pattern). This flag does not hold up: with only 87 independent observations (one per footprint) the interval around the 88% detected share is 79%-93%, which no longer rules out the 90% threshold. The failing records may well be real; what this says is that the SHARE failing may reflect how many near-identical records were deposited rather than how much of the population the assay misses.

**Denominator:** 5696 of 38024 screened records are evaluable (15.0%); 32328 are not. Every share above is taken over the evaluable ones.

Excluded: 2 indeterminate, 32326 no_amplicon

Why (the `no_amplicon` rows above; `indeterminate` records carry no reason, so these sum to the `no_amplicon` count and not to the whole excluded total): 21581 no_site, 5260 chance_only, 4830 truncated, 569 chance_anchor, 86 no_pair. `truncated` means the deposit stops before the other primer's site, so it says nothing about the assay; `diverged` means that site is present and does not match. `chance_anchor` means the only site found did not survive the archive-scale test (drift.anchor_fdr), so the record is not evidence either way.

Counted as failures, NOT excluded: 39 diverged. `drift.count_diverged_as_fail` is on, so a record whose primer site is present and does not match is in the denominator above as a failure. These are not part of the excluded counts and must not be added to them.

Of the `no_site` records, 15858 DID have a primer site within `scoring.max_mismatches_searched` and were dropped for failing the credibility bar (`scoring.max_site_evalue`), while 5723 had no site at all. The first group may be drift this assay is not being charged for; the second is most likely records that never held the target.

## Nested protocols (28)

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

**11 of 28** lose coverage this way. A further 1 are labelled as rounds but do not nest, so no conditional coverage is computed for them.

| protocol | round 1 | round 2 alone | run as a nest | records | inner inside outer | round 1 failures (diverged) |
|---|---|---|---|---|---|---|
| `Astroviridae_RdRp_Chu_2008` | 48% | 80% | 38% | 2,901 | yes | 1,508 (20 diverged) |
| `Lyssavirus_N_Vazquez-Moron_2006` (not scoreable) | 59% | 100% | 59% | 13,569 | yes | 5,572 (18 diverged) |
| `Proboscivirus_POL_Latimer_2012` | 62% | 97% | 59% | 32 | yes | 12 (0 diverged) |
| `Orthoreovirus_RdRp_Landolfi_2010` | 63% | 81% | 46% | 987 | yes | 365 (0 diverged) |
| `Coronaviridae_RdRp_Quan_2010` | 57% | 71% | 46% | 6,760 | yes | 2,916 (53 diverged) |
| `Rhabdoviridae_L_Bourhy_2005` | 72% | 89% | 71% | 6,944 | yes | 1,924 (260 diverged) |
| `Polyomaviridae_VP1_Johne_2005` | 0.6% | 11% | 0.3% | 2,316 | yes | 2,303 (289 diverged) |
| `Orthoherpesviridae_terminase_Chmielewicz_2001` | 90% | 90% | 81% | 2,588 | yes | 256 (20 diverged) |
| `Adenoviridae_hexon_Casas_2005` | 85% | 93% | 84% | 5,864 | yes | 865 (37 diverged) |
| `Ferlavirus_HN_Ahne_1999` | 89% | 96% | 89% | 28 | yes | 3 (0 diverged) |
| `Cytomegalovirus_gB_Prepens_2007` | 92% | 98% | 92% | 732 | yes | 56 (2 diverged) |
| `Cryptosporidium_18S_Xiao_1999` | 95% | 98% | 94% | 145 | yes | 7 (2 diverged) |
| `Orthoflavivirus_NS5_Scaramozzino_2001` | 55% | 34% | 30% | 33,895 | yes | 15,225 (441 diverged) |
| `Circoviridae_Rep_Mankertz_2000` | 70% | 36% | 34% | 7,506 | yes | 2,268 (1,166 diverged) |
| `Mastadenovirus_POL_Roy_2009` | 90% | 88% | 86% | 4,243 | yes | 414 (68 diverged) |
| `Alphavirus_nsP4_Sanchez-Seco_2001` | 97% | 96% | 94% | 8,366 | yes | 224 (223 diverged) |
| `Astroviridae_RdRp_Atkins_2008` | 97% | 98% | 96% | 3,060 | yes | 87 (20 diverged) |
| `Phlebovirus_L_Sanchez-Seco_2003` | 97% | 96% | 94% | 269 | yes | 8 (1 diverged) |
| `Orthoherpesviridae_POL_VanDevanter_1996` (not scoreable) | 98% | 86% | 86% | 3,464 | yes | 59 (26 diverged) |
| `Cytomegalovirus_gB_Deckers_2009` | 96% | 95% | 94% | 589 | yes | 23 (0 diverged) |
| `Orthohantavirus_S_Anthony_2013` | 99% | 99% | 98% | 4,167 | yes | 41 (0 diverged) |
| `Enterovirus_VP3_VP1_Nix_2006` | 98% | 12% | not a nest | 6,843 | **no** (53/3,794) | 162 (0 diverged) |
| `Adenoviridae_POL_Wellehan_2004` | 99% | 99% | 99% | 4,960 | yes | 33 (0 diverged) |
| `Paramyxoviridae_L_Tong_2008` | 62% | 33% | 33% | 8,834 | yes | 3,344 (112 diverged) |
| `Enterovirus_5UTR_VP4_VP2_Wray_2016` | 99% | 79% | 79% | 8,628 | yes | 77 (14 diverged) |
| `Bocaparvovirus_NS1_Kapoor_2010` | 74% | 74% | 74% | 1,941 | yes | 511 (504 diverged) |
| `Simian_immunodeficiency_virus_pol_Clewley_1998` | 100% | 99% | 99% | 3,965 | yes | 3 (0 diverged) |
| `Bornaviridae_N_Zimmermann_1994` (not scoreable) | 87% | 0% | 0% | 360 | yes | 46 (42 diverged) |

**`Enterovirus_VP3_VP1_Nix_2006`** — These entries are labelled as rounds of one protocol, but their amplicons do not nest: on 3,794 records scored by both, the inner product lies inside the outer on 53. A nested reaction amplifies the outer product, so these two cannot be running that way - either the round labels are wrong or they are separate assays that share a name. No conditional coverage is reported for them, because conditioning round 2 on a round 1 that does not feed it would invent a number. Curation, not a calculation.

**`Astroviridae_RdRp_Chu_2008`** — Run as published, this nest detects 38.4% of the 2,901 records both rounds can be judged on: round 1 reaches 48.0% and round 2 80.1% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 41.7% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. The rounds share reverse, so their failures are not independent - an escape there takes both.

**`Lyssavirus_N_Vazquez-Moron_2006`** — Run as published, this nest detects 58.9% of the 13,569 records both rounds can be judged on: round 1 reaches 58.9% and round 2 99.7% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 40.8% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. That crosses the 90% threshold: round 2 alone reads as working and the protocol does not.

**`Proboscivirus_POL_Latimer_2012`** — Run as published, this nest detects 59.4% of the 32 records both rounds can be judged on: round 1 reaches 62.5% and round 2 96.9% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 37.5% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. That crosses the 90% threshold: round 2 alone reads as working and the protocol does not. The rounds share reverse, so their failures are not independent - an escape there takes both.

**`Orthoreovirus_RdRp_Landolfi_2010`** — Run as published, this nest detects 45.7% of the 987 records both rounds can be judged on: round 1 reaches 63.0% and round 2 81.3% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 35.6% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. The rounds share forward, so their failures are not independent - an escape there takes both.

**`Coronaviridae_RdRp_Quan_2010`** — Run as published, this nest detects 46.2% of the 6,760 records both rounds can be judged on: round 1 reaches 56.9% and round 2 71.3% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 25.1% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template.

**`Rhabdoviridae_L_Bourhy_2005`** — Run as published, this nest detects 70.9% of the 6,944 records both rounds can be judged on: round 1 reaches 72.3% and round 2 89.4% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 18.5% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. The rounds share reverse, so their failures are not independent - an escape there takes both.

**`Polyomaviridae_VP1_Johne_2005`** — Run as published, this nest detects 0.3% of the 2,316 records both rounds can be judged on: round 1 reaches 0.6% and round 2 10.8% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 10.5% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template.

**`Orthoherpesviridae_terminase_Chmielewicz_2001`** — Run as published, this nest detects 81.3% of the 2,588 records both rounds can be judged on: round 1 reaches 90.1% and round 2 89.9% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 8.6% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template.

**`Adenoviridae_hexon_Casas_2005`** — Run as published, this nest detects 84.5% of the 5,864 records both rounds can be judged on: round 1 reaches 85.2% and round 2 92.9% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 8.4% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. That crosses the 90% threshold: round 2 alone reads as working and the protocol does not. The rounds share reverse, so their failures are not independent - an escape there takes both.

**`Ferlavirus_HN_Ahne_1999`** — Run as published, this nest detects 89.3% of the 28 records both rounds can be judged on: round 1 reaches 89.3% and round 2 96.4% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 7.1% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template. That crosses the 90% threshold: round 2 alone reads as working and the protocol does not.

**`Cytomegalovirus_gB_Prepens_2007`** — Run as published, this nest detects 92.3% of the 732 records both rounds can be judged on: round 1 reaches 92.3% and round 2 98.5% on its own. Round 2's own figure is what it would do as a DIRECT PCR; within the nest 6.1% of that coverage is unreachable, because round 1 escapes on those records and leaves the inner reaction no enriched template.

1 further entries declare a `source.nested_round` and no protocol is assembled from them, because the round they amplify from is not in the registry: `Elephant_endotheliotropic_herpesvirus_6_POL_Latimer_2012_round2`. Each says so with `nested_parent_not_held` and keeps its own standalone status above; what is missing is the other round, not anything about this one. Since 2026-11-01 parentage is declared rather than guessed from the id, so this list is a statement about the registry's contents and no longer about a naming convention.

## Published exclusivity claims, tested

Each of these assays names, in `target.exclusivity_taxids`, a taxon its own paper says
it does NOT amplify, and that taxon is retrieved on purpose so the claim can be screened.
This section exists separately from the per-assay detail above because it must not depend
on the assay's own status: an assay whose neighbour had to be fetched is usually one with
too few records of its own to be flagged, and its claim would then be computed and never
shown.

`evaluable` counts off-target records that yielded a product and so could be judged at
all; `share` is the fraction of those the assay is predicted to amplify. The whole-archive
count is larger and would be the wrong denominator -- most records of a neighbour taxon are
short fragments holding no product for anything, and dividing by them manufactures a
reassuring number. Like every figure here it is a prediction from sequence: a high share
disagrees with the paper's own panel and is worth reading that panel for, not a finding
that the assay cross-reacts in a tube.

| assay | status | claimed taxon | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|---|
| `Monkeypox_virus_F3L_Huo_2022_cladeIIab` | declining | Orthopoxvirus vaccinia (10245) | 0 | 262 | 285 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeIIab` | declining | taxid 10243 | 0 | 106 | 119 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeIIab` | declining | taxid 10255 | 0 | 82 | 82 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeIIab` | declining | taxid 12643 | 0 | 0 | 12 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeIIab` | declining | taxid 28873 | 0 | 10 | 12 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeIIab` | declining | taxid 28871 | 0 | 2 | 2 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeIIab` | declining | taxid 10256 | 0 | 0 | 0 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeI` | declining | Orthopoxvirus vaccinia (10245) | 0 | 283 | 285 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeI` | declining | taxid 10243 | 0 | 113 | 119 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeI` | declining | taxid 10255 | 0 | 82 | 82 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeI` | declining | taxid 12643 | 0 | 12 | 12 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeI` | declining | taxid 28873 | 0 | 10 | 12 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeI` | declining | taxid 28871 | 0 | 2 | 2 | 0% |
| `Monkeypox_virus_F3L_Huo_2022_cladeI` | declining | taxid 10256 | 0 | 0 | 0 | 0% |
| `Parapoxvirus_RPO147_Zhao_2013` | stable | taxid 10279 | 0 | 0 | 54 | 0% |
| `Parapoxvirus_RPO147_Zhao_2013` | stable | taxid 187984 | 0 | 0 | 3 | 0% |
| `Orf_virus_RPO147_Zhao_2013` | stable | taxid 129727 | 0 | 0 | 22 | 0% |
| `Orf_virus_RPO147_Zhao_2013` | stable | taxid 129726 | 0 | 0 | 15 | 0% |
| `Bovine_papular_stomatitis_virus_RPO147_Zhao_2013` | insufficient data | taxid 10258 | 0 | 83 | 85 | 0% |
| `Bovine_papular_stomatitis_virus_RPO147_Zhao_2013` | insufficient data | taxid 129726 | 0 | 1 | 15 | 0% |

## Collection year against deposit year, for assembly-backed assays

The verdicts above date every record by the year it was DEPOSITED. The metadata also carries the year each isolate was COLLECTED, and the two differ by a median of five years on this archive. This table re-dates the same records by collection year and recomputes the recent share the same way, so the two columns differ by the clock and nothing else. It is a lens on how much of a recent fall is a sequencing backlog rather than a change in what circulates; it moves no status. Records without a four-digit collection year are skipped on the collection clock and counted. Nuccore records carry no collection date in their metadata, so this covers assembly records only.

| assay | asm records | with collection year | recent share by deposit year | recent share by collection year | gap |
|---|---|---|---|---|---|
| `Escherichia_coli_LT_Victor_1991` | 325 | 204 | no recent records | no recent records | - |
| `Escherichia_coli_hlyA_Wang_1997` | 325 | 204 | 100.0% of 4 | no recent records | - |
| `Escherichia_coli_malB_Candrian_1991` | 325 | 204 | 56.7% of 60 | 64.0% of 25 | +7.3 points |
| `Leptospira_flaB_Hsu_2013` | 144 | 123 | 100.0% of 38 | 100.0% of 16 | +0.0 points |
| `Leptospira_lipL32_Ahmed_2020` | 144 | 123 | no recent records | no recent records | - |
| `Mycobacterium_16S_Hermes_2018` | 305 | 197 | 100.0% of 57 | 100.0% of 22 | +0.0 points |
| `Mycobacterium_tuberculosis_complex_IS1081_Hermes_2018` | 289 | 197 | 100.0% of 55 | 100.0% of 25 | +0.0 points |
| `Mycobacterium_tuberculosis_complex_IS6110_Boniotti_2014` | 289 | 197 | 100.0% of 54 | 100.0% of 25 | +0.0 points |
| `Mycobacterium_tuberculosis_complex_helicase_Hermes_2018` | 289 | 197 | 100.0% of 57 | 100.0% of 25 | +0.0 points |
| `Salmonella_enterica_invA_Rahn_1992` | 304 | 219 | 100.0% of 60 | 100.0% of 21 | +0.0 points |
| `Shigella_ipaH_Sethabutr_1993` | 173 | 107 | 100.0% of 54 | 100.0% of 18 | +0.0 points |
| `Yersinia_enterocolitica_yst_Ibrahim_1992` | 35 | 23 | 100.0% of 15 | 100.0% of 4 | +0.0 points |
| `Yersinia_pseudotuberculosis_inv_Wang_1997` | 41 | 21 | 100.0% of 16 | 100.0% of 3 | +0.0 points |

## Coverage gaps

These assays cannot be validated against sequence data because the sequence data
does not exist. For wildlife pathogens this is usually the finding, not a caveat.
An assay with no taxid was never searched: that is a registry gap, not a data gap.

| assay | taxon | taxid | evaluable | screened |
|---|---|---|---|---|
| `Batrachochytrium_dendrobatidis_mtDNA_Ghosh_2021_BdCAPE` | Batrachochytrium dendrobatidis | 109871 | 9 | 9491 |
| `Batrachochytrium_dendrobatidis_mtDNA_Ghosh_2021_BdGPL` | Batrachochytrium dendrobatidis | 109871 | 8 | 9491 |
| `Batrachochytrium_salamandrivorans_ITS1_5_8S_Blooi_2013` | Batrachochytrium salamandrivorans | 1357716 | 6 | 12 |
| `Batravirus_terminase_Licheri_2020_european` | Batravirus (formerly Batrachovirus) | 3044671 | 4 | 4 |
| `Batravirus_terminase_Licheri_2020_pan` | Batravirus (formerly Batrachovirus) | 3044671 | 8 | 8 |
| `Eimeria_furonis_18S_Sledge_2011` | Eimeria furonis | 352384 | 5 | 17 |
| `Elephant_endotheliotropic_herpesvirus_5_POL_Latimer_2012_round1` | Elephant endotheliotropic herpesvirus 5 | 548689 | 9 | 20 |
| `Elephant_endotheliotropic_herpesvirus_6_POL_Latimer_2012_round2` | Elephant endotheliotropic herpesvirus 6 | 548689 | 1 | 6 |
| `Intranuclear_coccidium_JW_2004_18S_Alvarez_2013` | Intranuclear coccidium JW-2004 | 293274 | 1 | 2 |
| `Leporid_gammaherpesvirus_5_gB_AbadeDosSantos_2021` | Leporid gammaherpesvirus 5 | 2729004 | 5 | 5 |
| `Orthopoxvirus_G9R_Gallardo-Romero_2011` | Orthopoxvirus | 10242 | 7 | 64 |
| `Sunshinevirus_L_Hyndman_2012_SunshineS1` | Sunshinevirus | 1921703 | 2 | 5 |
| `Sunshinevirus_L_Hyndman_2012_SunshineS2` | Sunshinevirus | 1921703 | 2 | 5 |

## Run timing

Run 2026-11-01 finished success after 49m 32s.

| stage | wall time |
|---|---:|
| workflow | 49m 32s |

134 retrieval groups were screened in this run, 1h 29m 13s of job time in all. The 10 slowest:

| group | archives | wall time | share |
|---|---:|---:|---:|
| `10244/all` | 12 | 12m 34s | 14% |
| `10241/all` | 17 | 7m 22s | 8% |
| `10242/all` | 12 | 7m 13s | 8% |
| `77643/q8c2ce9448f` | 1 | 4m 04s | 5% |
| `1387563/qdb308affab` | 1 | 3m 57s | 4% |
| `11320/q2ebd5918b3` | 21 | 3m 45s | 4% |
| `10241/q059a427e43` | 15 | 3m 21s | 4% |
| `171/q4a36c8adaa` | 6 | 3m 02s | 3% |
| `77643/qa99de05d40` | 1 | 2m 49s | 3% |
| `3044782/q63c5fca5b3` | 19 | 2m 15s | 3% |

Wall time per archive, summed per group, from Snakemake's `benchmark:` files. On macOS this is the only column that exists - `max_rss` and `cpu_time` read `NA` there - so these are elapsed times, not CPU, and a job that spanned a machine sleep would be inflated by it. Only benchmarks written during this run are counted.
