# Research Findings, 2026-10-06 — N. ceranae, Tasman-PCR, DWV Taxid Comparison

## 1. N. ceranae Primers (Martin-Hernández 2007, via Kato 2020)

### Source
- **Cited in**: Kato et al. 2020 Scientific Reports 10:1118, Table 1
- **Original paper**: Martin-Hernández et al. 2007, *Journal of Invertebrate Pathology* 106:98-104
- **Designation**: 218MITOC-FOR/REV (mitochondrial cytochrome oxidase PCR)

### Primer Sequences
```
218MITOC-FOR: 5′-CGGCGACGATGTGATATGAAAATATTAA-3′  (28 nt)
218MITOC-REV: 5′-CCCGGTCATTCTCAAACAAAAAACCG-3′     (26 nt)
```

### Current Issue
Per the Nosema bombi entry verification (2026-10-06):
- **5' end mismatches on GenBank references**:
  - Forward primer: 2 bases mismatch at 5' end
  - Reverse primer: 5 bases mismatch at 5' end
- **GenBank query**: RefSeq XR_002966746.1 and all N. ceranae 16S/18S records
- **Detection rate**: 136 of 152 product-bearing records (90%) called "fail" on 5' end penalties

### Resolution Path
1. **Option A (Preferred)**: Correct sequences to match all GenBank records
   - Measure actual amplicon on reference records
   - Use corrected sequences for registry entry
   
2. **Option B**: Enter as printed in Martin-Hernández 2007 (if discrepancy is publication error)
   - Follow up with Martin-Hernández/Kato to confirm
   - Note discrepancy in source field

3. **Option C**: Flag as "hypothetical" (sequences as published) pending literature clarification
   - Wait for follow-up papers with revised sequences
   - Common practice for microsporidian PCR where literature discrepancies occur

### Status
- **Actionable**: Yes, sequences are now known
- **Next step**: Screen 218MITOC-FOR/REV against full N. ceranae GenBank set and document measured size vs. published

---

## 2. Tasman-PCR (Kwon et al. 2018, Royal Society Open Science)

### Paper Details
- **DOI**: 10.1098/rsos.180870
- **Title**: "Tasman-PCR: a genetic diagnostic assay for Tasmanian devil facial tumour diseases"
- **Authors**: Kwon et al.
- **Publication**: 2018, Royal Society Open Science

### Assay Design
**Triplex PCR** amplifying host cancer-specific structural translocations:

| Target | Product Size | Gene/Region | Specificity |
|--------|--------------|-------------|------------|
| DFT1-A | 231 bp | Interchromosomal translocation Chr2/ChrX | Devil facial tumor clone 1 |
| DFT2-A | 321 bp | Interchromosomal translocation Chr4/Chr5 | Devil facial tumor clone 2 |
| RPL13A | 520 bp | Ribosomal protein L13A | Host genome control |

### Performance
- **Sensitivity**: 96.2% on 344 confirmed DFTD tumors
- **Specificity**: 100% on 804 normal devil DNA (0 false positives)
- **Tested on**: 546 tumors + 804 normal samples from Tasmania, 2003-2016

### Scope Classification
- **Target**: Host genome (cancer cell DNA, not pathogen)
- **Status**: **OUT OF SCOPE for pathogen registry**
- **Reason**: Detects structural variants in devil cancer cells, not pathogenic DNA
- **Decision**: Keep for now (user judgment: "reassess later")

### Note for Registry
If entered, should include scope note:
> "HOST GENOME ASSAY: Detects Tasmanian devil cancer cell-specific structural translocations (DFT1 and DFT2), not a pathogenic target. Included for reference pending registry scope clarification."

### Related Finding
- DFT2 preferentially affects male devils (82% male, p=0.033)
- Two devils identified with both DFT1 and DFT2 co-infection
- DFT2 appears geographically restricted to Channel Peninsula (southeast Tasmania)

### Status
- **Actionable**: Yes, assay details fully documented
- **Decision made**: Keep for future reassessment of scope
- **Next step**: Create draft entries with scope disclaimer or await scope policy decision

---

## 3. DWV-A/-B Taxid Comparison (Variant vs. Species-Level)

### Current Approach (Variant-Node Taxids)
- **DWV-A taxid**: 2951794 (Deformed wing virus A)
- **DWV-B taxid**: 2498590 (Deformed wing virus B)
- **Issue**: ~80% of GenBank DWV records lack A/B variant labels
- **Detection rate**: 68/223 (30.5%) A-labeled records detect; 82/1010 (8.1%) unlabeled

### Recommended Alternative (Species-Level Taxid)
- **Taxid**: 3047792 (Iflavirus aladeformis, the species)
- **Benefit**: Single query captures all labeled + unlabeled DWV records
- **Trade-off**: Broader match, may retrieve distant iflaviruses

### Decision Framework
**Test both approaches:**
1. Keep current DWV-A entry (variant-level: high specificity, low recall)
2. Create alternate DWV-A-species entry (species-level: higher recall, check specificity)
3. Compare detection rates on same GenBank set
4. Choose: species-level if comparable specificity, variant-level if specificity matters more

### Implementation Status
- **DWV-A entry**: Ready to test at both taxid levels
- **Primer sequences** confirmed (DWVAF, DWVAR, DWVAP from Rossi 2024)
- **Next step**: Create species-level variant and run parallel screens to compare

### Rationale for Testing
- Unlabeled DWV records represent ~80% of GenBank deposits
- Current variant approach misses most of the population
- Species-level approach would provide better real-world detection
- Cross-reactivity note: Assay detected B variant signal in A template (per Rossi 2024)

---

## Summary of Actions Taken

| Task | Outcome | Status |
|------|---------|--------|
| Locate Martin-Hernández 2007 paper | Found (via Kato 2020 Table 1) | ✓ Complete |
| Extract N. ceranae 218MITOC primers | Found: 28nt FOR, 26nt REV | ✓ Complete |
| Locate Kwon 2018 Tasman-PCR paper | Found & analyzed | ✓ Complete |
| Extract Tasman-PCR assay design | Triplex PCR documented (DFT1-A, DFT2-A, RPL13A) | ✓ Complete |
| DWV taxid comparison analysis | Two-approach strategy documented | ✓ Ready for testing |

## Files Added to Papers Folder
- `papers/10.1016_j.jip.2007.06.002.pdf` — Martin-Hernández 2007 (N. ceranae PCR)
- `papers/10.1098_rsos.180870.pdf` — Kwon 2018 (Tasman-PCR)

## Recommendations for Next Session

1. **N. ceranae**: Enter draft with 218MITOC primers; screen against GenBank to confirm/correct sequences; flag discrepancy with current GenBank records

2. **Tasman-PCR**: Create 3 draft entries (DFT1-A, DFT2-A, RPL13A) with prominent scope warning; reassess if registry expands to host-genome markers

3. **DWV**: Create species-level variant of DWV-A and perform parallel screening comparison; document which approach (variant or species) better serves the registry's use cases

## Status of Pipeline
- Snakemake retrieval still in progress (network-bound)
- Will complete and rescreen all 212 assays with fixed composition rule
