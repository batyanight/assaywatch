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

> **APPLIED 2026-10-24, with one part of this recommendation struck.** The three entries are
> in `registry/` as `MONKEYPOX_dsDNA_{G2R_generic,G2R_WestAfrican,C3L_CongoBasin}_TaqMan_Li_2010`,
> `status: draft`, DOI Crossref-verified, all nine oligos verified `exact` against the paper's
> own text, and every amplicon measured rather than quoted because the paper states no size
> (90 bp generic, 85 bp WA with a bimodal 82, 100 bp C3L).
> **The `scope_taxids` half of this recommendation cannot be carried out: NCBI Taxonomy has no
> node for either monkeypox clade.** The whole subtree of 10244 is two children, *Callithrix
> jacchus orthopoxvirus* (243803) and Monkeypox virus Zaire-96-I-16 (619591). So both
> clade-specific entries carry `scope_narrower_than_taxid` as the disclosure instead, the way
> AVIPOXVIRUS Baek does. It matters most for C3L, which will read ~8% detection for as long as
> it is unscoped and whose entry says so in terms.
> The predicted drift finding is confirmed and is larger than expected: the GENERIC assay's
> primers are exact in only 20.4% (forward) and 23.0% (reverse) of 13,179 monkeypox genomes
> while its probe is exact in 92.7%.

Add the **Li 2010 G2R trio** (generic + WA + CB) as three entries, taxid 10244 (MPXV) with
`scope_taxids` splitting WA (clade II) and CB (clade I) once their current NCBI nodes are
confirmed. It is the reference standard, it clade-types, its oligos are verifiable, and
watching G2R_WA is the single most informative thing the registry could do about mpox drift.
Optionally add Huo 2022 later for B.1 lineage typing. Source: PubMed; all DOIs above.

## CDC sweep (2026-10-24): two new candidates, both wildlife-relevant and NOT mpox

A PubMed sweep of CDC Poxvirus and Rabies Branch real-time PCR papers (affiliation
"Centers for Disease Control") surfaced two assay-DESIGN papers that fill registry gaps
and fit the wildlife/veterinary scope better than another mpox assay. Source: PubMed.

### A. Gallardo-Romero et al. 2011 — North American orthopoxviruses (STRONG wildlife fit)
- Virol J 8:313, [DOI](https://doi.org/10.1186/1743-422X-8-313), PMC3144017 (open access, so oligos verifiable).
- TaqMan assay on a myristylated protein gene conserved across the NORTH AMERICAN
  orthopoxviruses (Volepox, Skunkpox, Raccoonpox) and distinct from Eurasian OPXV; does not
  cross-react with other orthopox or the wider Chordopoxvirinae. Sensitivity 1-6 fg.
- Why it matters here: the registry has pan-pox consensus and MPXV, but NOTHING specific to
  the North American wild orthopoxviruses -- voles, skunks, raccoons -- which is squarely
  zoo/wildlife diagnostics. Clean, single-assay add.

### B. Zhao et al. 2013 — Parapoxviruses: orf, pseudocowpox, bovine papular stomatitis
- J Virol Methods 194:229-234, [DOI](https://doi.org/10.1016/j.jviromet.2013.08.027); no PMC
  id returned, so likely paywalled -- would need the paper obtained before oligos can be
  verified (NYU proxy).
- TaqMan generic parapoxvirus assay + three species-specific (ORFV, PCPV, BPSV) on the RNA
  polymerase gene. Orf is a common zoonosis of sheep/goats and their handlers; ruminant
  relevance is high for a wildlife/veterinary registry. Splits into 4 entries by probe.

Not assay-design (excluded): the Nigeria 2017-18 outbreak report
([DOI](https://doi.org/10.1016/S1473-3099(19)30294-4)), the GeneXpert commercial eval
([DOI](https://doi.org/10.4269/ajtmh.16-0567), proprietary oligos), the rope-squirrel and
Gambian-pouched-rat reservoir studies, the lab-acquired cowpox case, and the ST-246 antiviral
study -- all use PCR but none publish a new verifiable assay.

### Revised recommendation across the whole sweep
Three clean, in-scope, open-access adds, in priority order: (1) Li 2010 G2R trio (mpox,
clade-typing, watches the known clade-IIb drift); (2) Gallardo-Romero 2011 North American
OPXV (fills a wildlife gap, single assay); (3) Zhao 2013 parapox quartet (orf etc., needs the
paper first). Huo 2022 and Greninger 2022 remain options for mpox lineage/clinical depth.
Still nothing applied.
