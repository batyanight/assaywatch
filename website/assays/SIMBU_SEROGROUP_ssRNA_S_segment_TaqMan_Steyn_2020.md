# Shuni Virus in Wildlife and Nonequine Domestic Animals, South Africa

<p class="aw-byline">Steyn · Emerging Infectious Diseases · 2020</p>

<p class="aw-doi"><a href="https://doi.org/10.3201/eid2607.190770">doi:10.3201/eid2607.190770</a></p>

??? quote "Full citation"
    Steyn J et al. 2020. Shuni Virus in Wildlife and Nonequine Domestic Animals, South Africa. Emerg Infect Dis 26:1521-1525

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">SIMBU_SEROGROUP_ssRNA_S_segment_TaqMan_Steyn_2020</span></p>

**SIMBU SEROGROUP (ssRNA-) — S segment TaqMan RT-PCR**

| | |
|---|---|
| Target | Orthobunyavirus (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11572">taxid 11572</a>) |
| Gene | S segment |
| Chemistry | hydrolysis_probe |
| Amplicon | 152 bp |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | Ortho(SimbuF152) | `TAGAGTCTTCTTCCTCAAYCAGAAGAAGGCC` | 31 nt |
| reverse | Ortho(SimbuR304) | `GTYAMGGCAMTGTCTGGCACAGGATTTG` | 28 nt |
| probe | Ortho(Simbu-probe252) | `TGGTTAATAACCATTTTCC` | 19 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`amplicon_size_unresolved`** — published 152 bp against a printed 152-304 span that is 153 bp inclusive; to be measured, not argued


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
S[Gene] OR M[Gene] OR "S segment"[Title] OR "M segment"[Title] OR nucleocapsid[Title] OR glycoprotein[Title] OR "complete genome"[Title]
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `scope_narrower_than_taxid`, `amplicon_size_unresolved`.


## Curation record

ADDED 2026-10-25 from the maintainer's Downloads, and VERIFIED THE SAME DAY against its own design paper's appendix. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-25</b> ADDED 2026-10-25 from the maintainer's Downloads, and VERIFIED THE SAME DAY against its own design paper's appendix. All three oligos match character for character. Found via Table 1 of van der Walt M et al. 2023, Identification and Molecular Characterization of Shamonda Virus in an Aborted Goat Fetus in South Africa, Pathogens 12:1100, doi:10.3390/pathogens12091100, held as papers/10.3390_pathogens12091100.pdf, which prints them as the "Simbu Serogroup TaqMan Real-Time RT-PCR Assay" and credits its reference [20] = Steyn 2020. STEYN 2020 IS THE DESIGN PAPER, AND ITS OLIGOS ARE IN THE APPENDIX, NOT THE ARTICLE. The main PDF (papers/10.3201_eid2607.190770.pdf) prints none of the three sequences and none of their names, which looked at first like another citation chain. It is not: the article says it screened samples by a SHUV rRT-PCR and "a newly designed rRT-PCR targeting a conserved area of the S segment of the Simbu serogroup (Appendix)". The appendix is held under the project's .supp convention as papers/10.3201_eid2607.190770.supp.pdf, and its Methods and Validations section prints, verbatim: Ortho(SimbuF152) 5'152 TAGAGTCTTCTTCCTCAAYCAGAAGAAGGCC 3'184 Ortho(SimbuR304) 5'276 GTYAMGGCAMTGTCTGGCACAGGATTTG 3'304 Ortho(Simbu-probe252) 5'252 TGGTTAATAACCATTTTCC 3'270 designed on a conserved S-segment region of SHUV KC510272, positions 152-304. Those are the only three oligo-length runs anywhere in the appendix, so there is nothing else it could be confused with.</p><p>THE NAME-TO-SEQUENCE MAPPING WAS CHECKED TWICE, and the check mattered. pdftotext without -layout interleaves van der Walt's table columns and read that way the forward and reverse are SWAPPED. Two independent confirmations of the order recorded above: van der Walt's own nested S-segment assay prints Ortho(SimbuF141) as CGRTRYYGYTAGAGTCTTCTTCC, whose 3' end TAGAGTCTTCTTCC is the 5' start of F152, which a reverse primer could not be; and Steyn's appendix labels each sequence with its own 5'/3' coordinates, which agree.</p><p>COORDINATE ARITHMETIC, recorded because it is loose in the source and must not be mistaken for a transcription error here. The probe is exact: 252-270 inclusive is 19 and the sequence is 19 nt. The two primers are not: F152 is 31 nt against a printed 152-184 (33), R304 is 28 nt against a printed 276-304 (29). The probe matching exactly argues the extraction is sound and the paper's primer coordinates are a little loose, most likely in the superscripts. Independently, the appendix states 152 bp for a span of 152-304 that is 153 bp inclusive. None of this touches the sequences, which are verbatim; it is why amplicon_bp carries amplicon_size_unresolved and must be MEASURED rather than taken from either number.</p><p><b>2026-10-25</b> RETRIEVAL QUERY matches ORTHOBUNYAVIRUS_ssRNA_S_segment_Cac_Briese_2007 exactly, so this entry joins that archive group rather than forcing a fresh fetch of the genus. It pulls M-segment records into the denominator of an S-segment assay, which is the shape that generates chance pairs - harmless here because this is a probe-bearing assay and drift.chance_pair_test (shipped 2026-10-25) guards exactly that case.</p><p>TAXID IS THE GENUS, DELIBERATELY, AND IS WIDER THAN THE ASSAY. "Simbu serogroup" is not a taxonomic rank. NCBI has Simbu orthobunyavirus 3052441, Shuni orthobunyavirus 3052440 and Shamonda orthobunyavirus 159150 as separate species, so no single species node covers the serogroup and 3052441 would wrongly exclude the Shuni and Shamonda viruses this assay is used to detect. 11572 Orthobunyavirus is the same retrieval taxon the four ORTHOBUNYAVIRUS_*_Briese_2007 entries already use. It is far wider than the serogroup, so this entry carries scope_narrower_than_taxid and would need scope work before it could be screened meaningfully. AMPLICON: 152 is the published figure. The printed span 152-304 is 153 bp inclusive, an off-by-one of the kind this registry resolves by measurement rather than by argument, so nothing is decided here; amplicon_bp must be measured against real records before this goes live and may well disagree with both numbers.</p><p>NOT THE ONLY ASSAY IN THAT PAPER. van der Walt 2023 Table 1 also prints four assays it designed itself ("This study"), all conventional and all with degenerate pooled primers: a Simbu S-segment nested pair (F141/R718, 576 bp; nested FN403/RN695, 291 bp), a Simbu M-segment hemi-nested pair (M2671+/M3476-, 807 bp; nested M2671+/M3110-, 421 bp) and a pan-orthobunyavirus hemi-nested assay (Peri-F1 and others, 513 bp). Those have clean provenance - the paper that designed them is the paper we hold - and are better candidates than this one on that count, but the paper states the primers could only be tested as pools, not individually, which is the pooled_as_one_assay situation and wants a reading of its own before entry. Deliberately left out of this entry rather than guessed at.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=SIMBU_SEROGROUP_ssRNA_S_segment_TaqMan_Steyn_2020%3A%20&body=Entry%3A%20SIMBU_SEROGROUP_ssRNA_S_segment_TaqMan_Steyn_2020%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/SIMBU_SEROGROUP_ssRNA_S_segment_TaqMan_Steyn_2020/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/SIMBU_SEROGROUP_ssRNA_S_segment_TaqMan_Steyn_2020.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/SIMBU_SEROGROUP_ssRNA_S_segment_TaqMan_Steyn_2020.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

