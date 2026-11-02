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
| `Enterovirus_5UTR_VP4_VP2_Wray_2016_round2` | 660 | 2,054 | 100% |
| `Morbillivirus_P_Barrett_1993_Grosh_F` | 429 | 1,798 | 100% |
| `Orthoherpesviridae_POL_VanDevanter_1996_round1` | 734 | 1,102 | 100% |
| `Orthoflavivirus_NS5_Scaramozzino_2001_round1` | 263 | 959 | 100% |
| `Helicobacter_16S_Fox_1998_C05` | 1196 | 479 | 100% |
| `(an entry since removed)` | 1989 | 465 | 100% |
| `Plasmodium_18S_Li_1995` | 374 | 382 | 99% |
| `Enterovirus_VP3_VP1_Nix_2006_round2` | 375 | 352 | 100% |
| `Ranavirus_MCP_Pallister_2007` | 57 | 314 | 100% |
| `Polyomaviridae_VP1_Johne_2005_round2` | 271 | 293 | 100% |
| `Simian_immunodeficiency_virus_pol_Takehisa_2009_HahnF2` | 285 | 174 | 100% |
| `(an entry since removed)` | 2013 | 133 | 100% |
| `Encephalitozoon_18S_Muller_1999` | 279 | 45 | 100% |

`RANAVIRUS_…_MCP_Pallister_2007` at 57 bp is not an error: it is an MGB
real-time assay, and a short amplicon is what such an assay is designed around.

## Left unset, and why

| assay | modal | products | within ±25% | reason |
|---|---|---|---|---|
| `Batrachochytrium_salamandrivorans_ITS1_5_8S_Blooi_2013` | 161 | 6 | 100% | only 6 products |
| `Encephalitozoon_cuniculi_PTP_Xiao_2001` | 285 | 20 | 45% | multimodal: one value covers only 45% |
| `Orthopoxvirus_ATI_Meyer_1997` | 1067 | 3,495 | 31% | multimodal: one value covers only 31% |
| `Polyomaviridae_VP1_Johne_2005_round1` | — | 0 | — | no product at 3 mismatches; see below |
| `Mycoplasma_16S23S_ITS_Rebelo_2011_Myco16_23S_F` | 514 | 18 | 100% | only 18 products |
| `Sarcocystis_18S_5_8S_Kutkiene_2010_P_ITSR` | 1087 | 13 | 100% | only 13 products |
| `Sarcocystis_18S_5_8S_Kutkiene_2010_ShortITS1R` | 247 | 11 | 100% | only 11 products |
| `Intranuclear_coccidium_JW_2004_18S_Alvarez_2013` | — | 0 | — | no local archive |

Two of these are the interesting ones. `Orthopoxvirus_ATI_Meyer_1997`
really is multimodal — 1067, 1538 and 1535 bp — and that is the ATI length
polymorphism the assay's RFLP typing exploits, so no single declared size is
correct for it; constraining it would need a per-entry range rather than one
number. `Polyomaviridae_VP1_Johne_2005_round1` gives no product at the
3-mismatch limit this measurement used, but it is not dead.

*Correction, 2026-10-15.* An earlier version of this note said round 1 produces
no amplicon at all. That was the measurement's limit talking: VP1/1r never
matches a record at fewer than 5 mismatches. In the 2026-10-07 screen, which
searches to `max_mismatches_searched` (6), round 1 forms a product in 2,074 of
14,531 records, 80% of them 1,000-1,099 bp, and calls every one `fail` (2,069)
or `reduced` (5), never `detect`. The mismatches are almost all in the 5' half:
the reverse primer's sit 15-24 nt from its 3' end and the forward's 13-21, so
both 3' ends match. Mean penalty is about 1.9 (forward) plus 3.0 (reverse),
against `reduced_max` 3.0. For a broad-spectrum consensus PCR with intact 3'
ends that is a scoring verdict, not an established failure: it is the case
`scoring.by_chemistry` exists for, and conventional-PCR penalties set by tier-2
validation would decide it. Its size stays unset, since 3 mismatches finds no
product to measure.

The other six are simply short of evidence: too few products to measure
against, or no local archive. They stay exempt from the tolerance until there
are more records, which is the honest state rather than a guess.
