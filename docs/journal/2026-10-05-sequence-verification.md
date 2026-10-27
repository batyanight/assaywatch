# Sequence verification against the literature, 2026-10-05

55 open-access PDFs arrived in `papers/`. Run:

```bash
python scripts/verify_oligos_against_paper.py --pdf-dir papers --tsv results/oligo-verification-2026-10-05.tsv
```

## Where the registry stands

| verdict | n | meaning |
|---|---|---|
| exact | 65 | found inside an oligo the paper **lists** |
| in-text | 13 | occurs in the paper, but not in any listed oligo |
| near:1 | 1 | one edit from a listed oligo |
| near:2 | 2 | two edits |
| absent | 52 | no listed oligo within four edits |
| no-full-text | 105 | paper not open access and no local PDF |
| no-doi | 106 | nothing to check against |

**65 of 133 checkable oligos agree with their paper (49%).** Before the PDFs
arrived it was 40 of 59. The denominator more than doubled; the agreement rate
did not improve, which is the honest headline.

## Three things the check caught in the tool itself

Worth recording, because each one would have produced a confident wrong answer.

1. **Inosine.** Papers print `I`, the registry stores `N`. Comparing them charged
   an edit per inosine position and reported both PREDICT bocavirus primers as
   one base off when they match exactly. Both sides are now flattened to `N`.
2. **Table extraction glues cells together.** Spackman's forward primer came out
   of the PDF as `...GGTCG` + `M` from the next column, and its probe arrived
   wrapped in `FAM`, `TAMRA` and `AVIAN`. That inflated distances and reported
   candidates the paper never printed. Long candidates are now windowed to the
   stored oligo's length, which both fixes the distance and cleans up the
   reported sequence.
3. **"Appears in the paper" is not "is a primer in the paper".** Papers print
   their target gene. The Yersinia entry's stored forward primer sits inside the
   printed *ystA* sequence, four bases offset from the primer the table actually
   lists - and a plain substring search scored that a perfect match. `exact` now
   requires the match to be inside a listed oligo, and the weaker case is
   reported separately as `in-text`. That reclassification alone moved **12
   oligos out of `exact`**, which is why the agreement rate above is lower than
   the first run's.

## One genuine registry error, and it was not a typo in effect

`Yersinia_enterocolitica_entero_unnamed_Ibrahim_1992`, reverse primer. Ibrahim
et al. 1992 Table 3 prints:

    yst-Pr2a  5'-(30)AATGCTGTCTTCATTTGGAGC(50)-3'
    yst-Pr2b  5'-(92)GCAACATACATCACAGCAATC(72)-3'

The registry stored `GCAACATACATC`**G**`CAGCAATC`, a G where the paper has an A,
nine bases from the 3' end. Corrected.

**What the correction did is the interesting part.** Screened against the 35
*Y. enterocolitica* assemblies both ways, the result inverts: with the stored G,
**13 of 35** records match perfectly and 22 carry a mismatch; with the paper's A,
**22 match** and 13 carry one. The position is genuinely polymorphic in the
target, and the paper's primer sits on the majority allele while the stored
variant sat on the minority one. An `R` there would match all 35, but that is
designing a new primer rather than recording a published one.

**The error was silent to the drift metric.** A single mismatch nine bases from
the 3' end costs exactly 1.0 and `detect_max` is 1.0, so all 35 records read
`detect` either way. The tool cannot catch its own input errors. It was not
harmless though: it spent the whole detect budget, so any second mismatch
anywhere would have tipped a record to `reduced` for a reason that did not exist.

Two discrepancies in that entry are flagged and deliberately **not** "fixed",
because they cannot be settled by reading the table: the stored forward primer
is shifted four bases 3'-ward from `yst-Pr2a` (a 3'-end change, so not
cosmetic), and `amplicon_bp` is 159 where the paper's positions give 63.

## Two modifications now characterised exactly

Both were already flagged as modified; neither said what the modification *was*.

**`GPO-1FMod`** vs van Kuppeveld et al. 1992's `GPO-1`: one change, position 4,
`C -> Y`. A fixed C widened to C/T - a deliberate broadening, consistent with the
name. The published sequence is not substituted in, because the modified oligo
is what the lab runs. Its partner `MycoRev1` is **not in that paper at all**, so
the pair is a composite.

**`AIMatrixF/R`** vs Spackman et al. 2002: the forward has 2 changes, both
widenings. The reverse has **5**, including two fixed-base substitutions
(`C->A`, `A->G`) - a redesign, not a relaxation, which is why the checker reports
it absent from the paper. The probe is unchanged. Read alongside the sibling
entry `INFLUENZA_A_ssRNA_Matrix_gene_DID_NOT_WORK`: the registry holds at least
two in-house attempts at an influenza matrix assay, one recorded as failing.

## The 52 absent, by assay

Not necessarily errors. The common causes are a primer table set as an image, a
sequence that lives only in a supplement, and oligos that genuinely come from a
different paper than the one cited - which the provenance audit was already
chasing. These are the next thing to work through by eye.

- `CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004` (3)
- `CRYPTOSPORIDIA_Need_to_order_18SrDNA_Identification_2000` (3)
- `ADENOVIRUS_dsDNA_Polymerase_Primate_speci` (2)
- `ADENOVIRUS_dsDNA_Polymerase_Primate_speci_Casas_2005` (2)
- `ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round1` (2)
- `ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2` (2)
- `CALICIVIRUS_ssRNA_Capsid` (2)
- `CMV_specific_HERPES_UL55_Glycoprotein_B_gB` (2)
- `CMV_specific_HERPES_UL55_Glycoprotein_B_gB_Virol_2007_round1` (2)
- `CMV_specific_HERPES_UL55_Glycoprotein_B_gB_round2` (2)
- `CMV_specific_HERPES_UL55_Glycoprotein_B_gB_round2_2` (2)
- `FILOVIRUS_ssRNA_L_gene_2` (2)
- `MYCOPLASMA_16S_Turtles_only_Feldman_2006` (2)
- `ORTHOBUNYAVIRUS_ssRNA_L_segment_Briese_2007` (2)
- `ORTHOBUNYAVIRUS_ssRNA_M_segment` (2)
- `ORTHOBUNYAVIRUS_ssRNA_M_segment_5prime_Briese_2007` (2)
- `ORTHOBUNYAVIRUS_ssRNA_M_segment_internal_Briese_2007` (2)
- `ORTHOBUNYAVIRUS_ssRNA_S_segment` (2)
- `ORTHOBUNYAVIRUS_ssRNA_S_segment_Cac_Briese_2007` (2)
- `PARVOVIRUS_ssDNA_VP1_gene_dependovirus_2002` (2)

## The 13 in-text

Each needs a human to open the primer table and confirm, since the match may be
inside the printed target sequence.

- `ADENOVIRUS_dsDNA_Pan_Polymerase_round1` Forward, pol- Fouter
- `ADENOVIRUS_dsDNA_Pan_Polymerase_round1` Reverse, pol-Router
- `ADENOVIRUS_dsDNA_Pan_Polymerase_round2` Forward, polFinner
- `ADENOVIRUS_dsDNA_Pan_Polymerase_round2` Reverse, polRinner
- `ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round1` Astr4380F
- `ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2` Astr4380F
- `ASTROVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2` Astr4722R
- `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_Lan_2010_round1` CoV-FWD1 (U630)
- `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2` CoV-RVS2(L1107)
- `Pan_flavivirus_NS5_3_round2` FS 778-Zino-hemi-fwd
- `West_Nile_Virus_Envelope_glycoprotein_E_Lanciotti_2001` WN-1333
- `West_Nile_Virus_Envelope_glycoprotein_E_Lanciotti_2001` WN-1494c
- `Yersinia_enterocolitica_entero_unnamed_Ibrahim_1992` YE-1
