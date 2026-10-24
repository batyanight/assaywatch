# Adjudicating 21 near-misses and 32 absent oligos (2026-10-23)

`docs/2026-10-23-wave5-elsevier-and-oligo-flags.md` left 15 candidate oligo errors
after removing the 4 CDV arctic variants and 2 `Mod` oligos, and noted that the 32
`absent` oligos had never been enumerated. This is that adjudication: every
`near:` and `absent` row read against the paper itself, by eye where the
extraction had failed.

**Nothing was changed on the verifier's say-so.** Four sequences were corrected,
and each rests on the printed table read directly.

## The policy decision: keep both

A published panel often reprints a published primer with the degeneracy widened.
Asked whether the registry should hold the panel's form or the original paper's,
the maintainer's answer was **keep both**: store the form actually run, and record
what it was modified from and where that modification is published.

That is now `Oligo.modified_from` plus `Oligo.modification_doi`, added in the
previous commit for the two `Mod` oligos and applied here to 11 more. The verifier
reads it: an oligo whose `modified_from` the paper prints reads `modified` and
counts as agreeing, rather than as a transcription error against a sequence nobody
claimed. An empty `modification_doi` is itself a finding — the modification is
unpublished and exists only here.

## Four real errors, all of which change calls

| entry | oligo | stored | the paper prints | cause |
|---|---|---|---|---|
| `BORNA_VIRUS_N_gene` | Borna-NF | GCCTTGTGTTTCTAT**GTTTG** | GCCTTGTGTTTCTAT**CTTTC** | Zimmermann 1994's internal pair, read in both the PDF and the publisher XML. The last four bases were wrong **including the 3'-terminal base**, the single most load-bearing position under `terminal_mismatch_fails`. The stored tail is that of the paper's *external* sense primer, which is the likely origin. The sibling round-2 entry already stored the correct form as BornaNestF. |
| `CALICIVIRUS_ssRNA_Helicase_Reid_1999` | Hel1 | GTCCCAGTATTCGGATTTGTCT (22) | GTCCCAGTATTCGGATTTGTCT**GCG** (25) | One mis-split table cell. Reid 1999 Table 2 wraps each 25-mer after a hyphen, and its own nt column says 25. |
| | Hel2 | **GCGA**GCGGGTAGTTCAGT (18) | AGCGGGTAGTTCAGT**CAAGTTCACC** (25) | Hel1's wrapped continuation `GCG` had been prepended to Hel2's first line, so one primer's tail became the next primer's head. |
| `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme` | CoV-RVS3 | CCATCATCASWYR**G**AATCATCATA (24) | PREDICT P-006: CCATCATCASWYRAATCATCATA (23) | A hybrid nobody printed: Watanabe 2010's length with the panel's degeneracy. Europe PMC finds 0 papers with the stored 24-mer and 19 with the panel's 23-mer. |

The calicivirus entry also loses `oligos_designed_here`: Table 2's footnote reads
"Originally described by Neill and Seal (1995)", so Reid is where Hel1/Hel2 are
printed, not where they were designed.

CoV-RVS3's correction is the first case where **the panel, not the registry,
introduced the error** — P-006 drops one base relative to Watanabe, and 19
downstream papers inherited it. Under "keep both" the panel's form is what the
registry stores, with Watanabe's as `modified_from`.

## Thirteen modifications now recorded rather than flagged

`modified_from` added, with `modification_doi` where the modified form is itself
published:

| entry | oligo(s) | modified from | published in |
|---|---|---|---|
| `CORONAVIRUS_..._polyme` | CoV-FWD3, CoV-RVS3 | Watanabe 2010 | 10.1038/ncomms9147 (P-006) |
| `CORONAVIRUS_..._polyme_Lan_2010_round1` | CoV-RVS1 | Quan 2010's 33-mer | 10.1038/ncomms9147 (P-005) |
| `Pan_Flavivirus_NS5_gene` | Flavi-FWD | Moureau 2007 PF1S `TGYRTB...` | 10.1038/ncomms9147 (P-009) |
| `Cryptosporidium_18SrDNA_Xiao_1999_round1` | Xiao18SR1 | Xiao 1999's `CCCTAAT...` | 10.1128/aem.66.12.5492-5498.2000 |
| `INFLUENZA_A_..._h_2003` | AIMatrixF, AIMatrixR | Spackman 2002 | 10.3390/v5081964 |
| `ARENAVIRUS_ssRNA_S_gene_2` | ARS7C-MOD | Lozano 1997's ARS7C | 10.1038/ncomms9147 (P-004) |
| `PARVOVIRUS_..._dependovirus_2002` | 19SAAVF, 18asAAVR | Gao 2002's 19s / 18as | — unpublished |
| `Entamoeba_18S_..._SSU_2014` | GEI18SF, GEI18SR | the printed pair | — unpublished |
| `Pan_mycoplasma_16S_All_Van_1992` | GPO-1FMod | van Kuppeveld 1992's GPO-1 | — unpublished |

Two notes were wrong and are corrected. **Xiao18SR1 is not an in-house
correction**: Xiao et al. 2000 prints it as the authors' own published fix
("a correction (change of TAA to ATT) was made ... the corrected primary reverse
primer is 5'-CCCATTTCCTTCGAAACAGGA-3'"), in the very paper an earlier audit said
did not print it. And the influenza reverse is not a registry redesign: both
stored influenza primers appear verbatim in Lindsay et al. 2013, described there
as Spackman's protocol "modified by Runstadler et al."

## Why the 32 `absent` were mostly not errors

Six distinct mechanisms, none of them a defect in the registry:

- **The oligos are only in a figure.** Boyle 2004 (Bd), Pallister 2007
  (ranavirus), Hellgren 2004 (HaemF/HaemR2) and Sigrist 2021 (nine oligos across
  three entries) print their primers as labelled arrows or rows inside an image.
  These will read `absent` forever.
- **Degeneracies written as parenthesised alternatives.** Zhu 2000 prints
  `TTT(C/T)(C/T)G(A/G)TCCTCTCGTACT`, which no oligo-shaped run survives.
- **A cocktail consolidated into one degenerate pair.** Zhai 2007 prints four
  forwards and four reverses; the stored MOD-FWD/MOD-RVS cover all eight with no
  mismatch, and are published in that consolidated form in three later protocols.
- **Glued table text.** Deckers 2009's run came out ending `AGCMVGB` — the
  name column plus the next column's label.
- **Hyphen-wrapped table rows.** Lozano 1997's ARS3V and ARS16V (settled in the
  previous commit) and the calicivirus pair above, which was the one case where
  the wrap had actually corrupted the entry.
- **A comparator primer, not the assay's own.** Sigrist's BornaPCA6 read `near:1`
  against PaBVcon_1401+ from supplementary Table S4, one of the *previously
  published* assays that paper compares itself to.

**Bd, the one `active` assay, was the urgent case** and is clean: all three oligos
match AY598034.1, the accession its figure cites, with a 146 bp product equal to
the stored `amplicon_bp`.

The flagging rule applied, so it is not decided per entry: `oligos_read_from_figure`
goes on an entry whose oligos' only primary source is an image. Bd does not get it,
because the figure names a GenBank accession and the sequences were confirmed
against that accession rather than by eye.

## Three oligos have no source, and two have a different one

- `Pan_mycoplasma_16S_23S_intergenic_space` 16-23-R1 and `..._3` 16-23-F3, and
  `Pan_mycoplasma_16S_All_Van_1992` MycoRev1: not in the cited paper and not in
  Europe PMC full text. `oligo_source_unresolved` is **not** a to-do here; reading
  another paper will not clear it.
- **EcoLT-1/EcoLT-2** are printed in Wang et al. 1997
  (10.1046/j.1365-2672.1997.00300.x) Table 2, with these names, both sequences and
  the 117 bp this entry stores. Victor 1991, the cited paper, prints different LT
  primers (LT51/LT31) and names no EcoLT. Wang's own Reference column credits
  Victor; its newly designed assays instead read "This study".
- **PVOnstF** is printed in Wray et al. 2016 Table 1
  (10.1007/s10393-016-1183-z), paired with PVO3 as this same hemi-nested assay —
  and that table's citation column for the pair reads "Unpublished".

**Both are left cited as they were, and flagged.** Repointing the DOI would also
make each id's `Victor_1991` / `Bourhy` attribution wrong, which is a rename with
`docs/rename-mapping.tsv` consequences, and the precedent set for `Nipah_N_gene_2`
and `POXVIRUSES_dsDNA_Polymerase_short_2` was to keep the upstream citation and
flag the indirectness. A maintainer decision.

## One non-oligo removed from screening

`Entamoeba_18S_small_subunit_SSU_2014` held a second GEI18SR under `alternates`,
the form the paper prints verbatim — which is the *target strand* at the reverse
primer's site, not the oligo. Against AF149905 both printed strings lie on the
sense strand (1308 and 1799, a 511 bp product inside the paper's stated 450-535),
so the primary reverse slot is the correct molecule and the alternate was a
non-oligo being screened as a primer. Removed. The entry is `deprecated`, so
nothing downstream changes.

## The numbers

| | 2026-10-22 | after wave 5 | now |
|---|---|---|---|
| checkable oligos agreeing | 393 / 466 (84%) | 395 / 460 (86%) | **413 / 462 (89%)** |
| `near:` | 21 | 13 | **5**, all documented artefacts |
| `absent` | 31 | 32 | **24**, all documented |
| `sibling` | — | 6 | 4 |
| `modified` | — | 2 | 13 |

Current output: `results/oligo-verification-2026-10-23.tsv` and its `.log`.

## A correction to the previous commit

That commit said the astrovirus alternates are in neither Atkins 2009 nor the
PREDICT book. The first half holds; the second does not. The book has a **second**
astrovirus protocol, **P-002**, whose REFERENCE line reads "Chu, D.K.W. et al
(2008)" and which prints all five oligos at ~436 bp (round 1) and ~421 bp
(round 2). So they are published twice over, and the old entry's error was the
protocol number: P-001 is Atkins' three primers, P-002 is this assay. Both new
entries now carry `predict_protocol: P-002`, and the book's sizes agree with the
measured medians (437 and 410).

## A rescreen is owed, and it is small

Any edit to a registry YAML invalidates the signature of the groups holding that
assay, so every entry touched here will rescreen. Only four groups can produce
**different calls**:

| group | assays | why |
|---|---|---|
| `178830/all` | 3 | Borna-NF's 3' base changed |
| `11974/all` | 1 | both calicivirus primers lengthened to 25 nt |
| `11118/q4d4730ef3b` | 3 | CoV-RVS3 one base shorter |
| `39733/all` | 4 | the two new Chu entries |

Not run here. The calicivirus entry's declared 360 bp should be re-measured
against Reid's printed 357 at the same time, and Borna's every past call was made
with the wrong 3' end.

## Still open

- The **20 `in-text`** rows: the sequence occurs in the paper but not in any
  listed oligo, so it may have been found inside a printed target sequence rather
  than a primer table. A weaker class than `near:`, never enumerated.
- The **E_coli / rhabdovirus re-citation** decision above.
- `ORTHOBORNAVIRUS_XP_aquatic_Sigrist_2021` stores its reporter as "Alexa 647N"
  while Figure 2C labels the probe A647N, the conventional short form of Atto
  647N; Alexa Fluor dyes carry no N suffix. Not screened, not changed, recorded.
