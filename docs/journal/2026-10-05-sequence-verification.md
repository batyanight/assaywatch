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

`Yersinia_enterocolitica_yst_Ibrahim_1992`, reverse primer. Ibrahim
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
name. The published sequence is not substituted in, because the modified oligo is the one in use. Its partner `MycoRev1` is **not in that paper at all**, so
the pair is a composite.

**`AIMatrixF/R`** vs Spackman et al. 2002: the forward has 2 changes, both
widenings. The reverse has **5**, including two fixed-base substitutions
(`C->A`, `A->G`) - a redesign, not a relaxation, which is why the checker reports
it absent from the paper. The probe is unchanged. Read alongside the sibling
entry `(an entry since removed)`: the registry holds at least
two in-house attempts at an influenza matrix assay, one recorded as failing.

## The 52 absent, by assay

Not necessarily errors. The common causes are a primer table set as an image, a
sequence that lives only in a supplement, and oligos that genuinely come from a
different paper than the one cited - which the provenance audit was already
chasing. These are the next thing to work through by eye.

- `Batrachochytrium_dendrobatidis_ITS1_5_8S_Boyle_2004` (3)
- `Cryptosporidium_18S_Xiao_1999_round1` (3)
- `Mastadenovirus_POL_Roy_2009_round2` (2)
- `Mastadenovirus_POL_Roy_2009_round1` (2)
- `Astroviridae_RdRp_Atkins_2008_round1` (2)
- `Astroviridae_RdRp_Atkins_2008_round2` (2)
- `Caliciviridae_capsid_Reid_1999` (2)
- `Cytomegalovirus_gB_Deckers_2009_round1` (2)
- `Cytomegalovirus_gB_Prepens_2007_round1` (2)
- `Cytomegalovirus_gB_Prepens_2007_round2` (2)
- `Cytomegalovirus_gB_Deckers_2009_round2` (2)
- `Filoviridae_L_Zhai_2007_MOD_FWD` (2)
- `Mycoplasmatota_16S_Feldman_2006` (2)
- `Orthobunyavirus_L_Briese_2007` (2)
- `Orthobunyavirus_M_Briese_2007_M3560_F` (2)
- `Orthobunyavirus_M_Briese_2007_BUN_S5_F` (2)
- `Orthobunyavirus_M_Briese_2007_BUN_M_IXf` (2)
- `Orthobunyavirus_S_Briese_2007_BUNS_5_U_6` (2)
- `Orthobunyavirus_S_Briese_2007_Cac_2_FWD` (2)
- `Dependoparvovirus_VP1_Gao_2002_2` (2)

## The 13 in-text

Each needs a human to open the primer table and confirm, since the match may be
inside the printed target sequence.

- `Adenoviridae_POL_Wellehan_2004_round1` Forward, pol- Fouter
- `Adenoviridae_POL_Wellehan_2004_round1` Reverse, pol-Router
- `Adenoviridae_POL_Wellehan_2004_round2` Forward, polFinner
- `Adenoviridae_POL_Wellehan_2004_round2` Reverse, polRinner
- `Astroviridae_RdRp_Atkins_2008_round1` Astr4380F
- `Astroviridae_RdRp_Atkins_2008_round2` Astr4380F
- `Astroviridae_RdRp_Atkins_2008_round2` Astr4722R
- `Coronaviridae_RdRp_Quan_2010_round1` CoV-FWD1 (U630)
- `Coronaviridae_RdRp_Quan_2010_round2` CoV-RVS2(L1107)
- `Orthoflavivirus_NS5_Scaramozzino_2001_round2` FS 778-Zino-hemi-fwd
- `West_Nile_virus_E_Lanciotti_2001` WN-1333
- `West_Nile_virus_E_Lanciotti_2001` WN-1494c
- `Yersinia_enterocolitica_yst_Ibrahim_1992` YE-1
