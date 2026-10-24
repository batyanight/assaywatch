# Candidate modern mpox qPCR assays to add (literature pass, 2026-10-24)

The registry's only MPXV-specific assays are `MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004` and
`..._F3L_MGB_Kulesh_2004` (both `10.1038/labinvest.3700143`, design_year 2004). On the
2026-10-24 run the N3R entry reads 58.3% with `count_diverged_as_fail` on, and 2223 of its
2377 diverged records are 2022-or-later: the clade IIb outbreak against a 2004 probe. This
is a candidate shortlist for a MODERN assay to ADD and watch (not replace — the old entry
stays, that is the point of the registry).

Nothing here is applied. Adding any entry is the full process: paper → Crossref-verified DOI
→ every oligo verified against the paper's own text → taxid → scope. Source metadata below is
from PubMed; verify independently before entry.

## Ranked candidates

### 1. Li et al. 2010 — the CDC G2R/C3L reference standard (TOP PICK)
- J Virol Methods 169:223-227, [DOI](https://doi.org/10.1016/j.jviromet.2010.07.012), PMC9628942 (open access).
- Three TaqMan assays, FAM/BHQ1, splits into three registry entries the way the registry
  already splits multiplex assays by probe:
  - **G2R_G (MPXV generic)**, TNF-receptor gene: F `GGAAAATGTAAAGACAACGAATACAG`,
    R `GCTATCACATAATCTGGAAGCGTA`, P `AAGCCGTAATCTATGTTGTCTATCGTGTCC`.
  - **G2R_WA (West African / clade II specific)**: F `CACACCGTCTCTTCCACAGA`,
    R `GATACAGGTTAATTTCCACATCG`, P `AACCCGTCGTAACCAGCAATACATTT` (anneal 62 degC per paper).
  - **C3L (Congo Basin / clade I specific)**: F `TGTCTACCTGGATACAGAAAGCAA`,
    R `GGCATCTCCGTTTAATACATTGAT`, P `CCCATATATGCTAAATGTACCGGTACCGGA`.
- Why top: global reference standard; clade-types (increasingly needed with clade I
  spreading since Dec 2023); sequences printed in open-access full text, so verifiable.
- HIGH-VALUE SIDE EFFECT: G2R sits in the ITR and is exactly the locus where some 2022 clade
  IIb/B.1 genomes carry a deletion causing documented false negatives. Screening G2R_WA
  against the archive would directly surface that drift -- the registry watching a known
  real-world assay-failure mode. design_year would be 2010.
- Caveat: pre-2022 design, so "current" only in the sense of being the still-dominant
  reference; the generic worked through 2022, the WA/clade-II one is the one with the known
  deletion vulnerability.

### 2. Huo, Tan et al. 2022 — designed ON 2022 clade IIb/B.1 genomes
- Biosaf Health 4:392-398, [DOI](https://doi.org/10.1016/j.bsheal.2022.10.005), PMC9633113 (open access).
- Two multiplex panels differentiating MPXV IIa, IIb, clade I, and the 2022 B.1 lineage;
  primers/probes designed on 138 poxvirus genomes. The most 2022-outbreak-specific design.
- Oligos not yet extracted here; full text is OA, so verifiable. Candidate if lineage-level
  (B.1) typing is wanted, not just clade.

### 3. Mills, Greninger et al. 2022 — clinically validated during the outbreak
- J Clin Virol 159:105373, [DOI](https://doi.org/10.1016/j.jcv.2022.105373), PMC9783225 (open access).
- F3L and G2R MPXV-specific + E9L pan-orthopox, validated on 2022 clinical samples across
  many specimen types. Note G2R outperformed F3L by ~0.4 Ct (two ITR copies).
- Overlaps the registry's existing F3L target name (different primer set from Kulesh).

### 4. Li et al. 2006 — E9L-NVAR + B6R (for completeness, NOT recommended as the add)
- J Clin Virol 36:194-203, [DOI](https://doi.org/10.1016/j.jcv.2006.03.012), PMC9628957.
- The original CDC pair; E9L-NVAR is pan-non-variola-orthopox, B6R is MPXV envelope. Older,
  not clade-typing, and the pan-pox niche is already covered in the registry.

## Not candidates
- NeuMoDx / Qiagen RUO assay (eval: [DOI](https://doi.org/10.1128/jcm.00028-24)) and the
  Chinese EQA of commercial kits ([DOI](https://doi.org/10.1007/s10096-024-04865-0)):
  proprietary oligos, not printed, so unverifiable -- fail the registry's measure-never-quote
  rule.

## Recommendation
Add the **Li 2010 G2R trio** (generic + WA + CB) as three entries, taxid 10244 (MPXV) with
`scope_taxids` splitting WA (clade II) and CB (clade I) once their current NCBI nodes are
confirmed. It is the reference standard, it clade-types, its oligos are verifiable, and
watching G2R_WA is the single most informative thing the registry could do about mpox drift.
Optionally add Huo 2022 later for B.1 lineage typing. Source: PubMed; all DOIs above.
