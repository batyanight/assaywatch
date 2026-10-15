# Measured amplicon sizes for entries that declared none

2026-10-14. Thirteen entries gained an `amplicon_bp` measured from the archives
rather than quoted from a paper, and eight did not. Each of the thirteen carries
`AMPLICON_BP_MEASURED_NOT_PUBLISHED` in `needs_review`, because a measured size
is weaker evidence than a published one and should be replaced if the figure
turns up.

## Why these entries needed one at all

`amplicon.declared_tolerance` (0.25, on since 2026-10-14) constrains a call to
the assay's own declared product size. An entry that declares none is exempt,
and the exemption is not harmless — in the 2026-10-07 rescreen the undeclared
entries carried **25.7% of their detect/reduced calls on products over 1500 bp,
against 0.57% for entries that declare a size**. They were the last place a
long chance product could still be credited to an assay.

## The criterion

Not "is there a dominant mode" — that asks the wrong question. The stored value
has to work as a *gate*, so the test is whether a single number with ±25% round
it accepts the products the assay really makes:

* at least **20 products** measured over every archive of the entry's own
  retrieval group (`scripts/check_amplicons.py`, 3 mismatches), and
* at least **95% of all products** within ±25% of the modal length.

Both are properties of the distribution, so an entry that fails either was left
unset rather than given a number that would start rejecting real amplifications.

## Filled in

| assay | measured bp | products | within ±25% |
|---|---|---|---|
| `ENTEROVIRUS_ssRNA_5_UTR_VP4_VP2_round2` | 660 | 2,054 | 100% |
| `Morbillivirus_including_CDV_P_gene` | 429 | 1,798 | 100% |
| `Pan_HERPES_dsDNA_Polymerase` | 734 | 1,102 | 100% |
| `Pan_flavivirus_NS5_3_round1` | 263 | 959 | 100% |
| `Helicobacter_Pan_Helicobacter_16S_Jim_Fox_1998` | 1196 | 479 | 100% |
| `Canine_distemper_virus_specifi_F_gene_need_to_order_2` | 1989 | 465 | 100% |
| `SSU_rRNA_gene_Plasmodium_SSU_rDNA_Grim_2003` | 374 | 382 | 99% |
| `ENTEROVIRUS_ssRNA_VP3_VP1_round2` | 375 | 352 | 100% |
| `RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007` | 57 | 314 | 100% |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round2` | 271 | 293 | 100% |
| `RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009` | 285 | 174 | 100% |
| `Canine_distemper_virus_specifi_F_gene_need_to_order` | 2013 | 133 | 100% |
| `Encephalitozoon_18S_General_Encephalitoz_Muller_1999` | 279 | 45 | 100% |

`RANAVIRUS_…_MCP_Pallister_2007` at 57 bp is not an error: it is an MGB
real-time assay, and a short amplicon is what such an assay is designed around.

## Left unset, and why

| assay | modal | products | within ±25% | reason |
|---|---|---|---|---|
| `B_salamandrivorans_Internal_transcribes_spa_Blooi_2013` | 161 | 6 | 100% | only 6 products |
| `Encephalitozoon_Polar_tube_protein_E_cun_Xiao_2001` | 285 | 20 | 45% | multimodal: one value covers only 45% |
| `ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997` | 1067 | 3,495 | 31% | multimodal: one value covers only 31% |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` | — | 0 | — | no product in its own archive |
| `Pan_mycoplasma_16S_23S_intergenic_space_Rebelo_2011` | 514 | 18 | 100% | only 18 products |
| `SARCOCYSTIS_18S_5_8s_rDNA_long_2010` | 1087 | 13 | 100% | only 13 products |
| `SARCOCYSTIS_18S_5_8s_rDNA_short_Kutkiene_2010` | 247 | 11 | 100% | only 11 products |
| `Tortoise_intranuclear_coccidia_18SrDNA` | — | 0 | — | no local archive |

Two of these are the interesting ones. `ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997`
really is multimodal — 1067, 1538 and 1535 bp — and that is the ATI length
polymorphism the assay's RFLP typing exploits, so no single declared size is
correct for it; constraining it would need a per-entry range rather than one
number. `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` produces **no amplicon at all**
in its own archive, which is a finding about the entry rather than a missing
measurement, and worth its own look.

The other six are simply short of evidence: too few products to measure
against, or no local archive. They stay exempt from the tolerance until there
are more records, which is the honest state rather than a guess.
