# A New Molecular Detection System for Canine Distemper Virus Based on a Double-Check Strategy

<p class="aw-byline">Halecker · Viruses · 2021</p>

<p class="aw-doi"><a href="https://doi.org/10.3390/v13081632">doi:10.3390/v13081632</a></p>

??? quote "Full citation"
    Halecker S, Bock S, Beer M, Hoffmann B. A New Molecular Detection System for Canine Distemper Virus Based on a Double-Check Strategy. Viruses 2021;13:1632.

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">CDV_P_gene_Mix3_Halecker_2021</span></p>

**CANINE DISTEMPER VIRUS — P gene TaqMan RT-qPCR CDV-Mix 3, degenerate update of Scagliarini 2007 (Halecker 2021)**

| | |
|---|---|
| Target | Morbillivirus canis (formerly Canine morbillivirus) (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052342" title="Morbillivirus canis">taxid 3052342</a>) |
| Gene | P |
| Chemistry | hydrolysis_probe |
| Amplicon | 116 bp |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | CDV4.1-F | `CTGTCRGTAATCGAGRATTCGA` | 22 nt |
| reverse | CDV3-R | `GCCGAAAGAATATCCCCAGTTAG` | 23 nt |
| probe | CD3.1-FAMas | `ATCTTCGCCAGARTCYTCAGTGCT` | 24 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`duplicate_entry_unresolved`** — overlaps CDV_P_gene_Scagliarini_2007: shares CDV3-R, and the forward and probe are degenerate modifications of it; decide whether both entries stay


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `duplicate_entry_unresolved`.


## Curation record

Added 2026-10-06 from the paper's own Table 1 (papers/10.3390_v13081632.pdf), rendered at 220 dpi and read by eye as well as extracted as text; 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-06</b> Added 2026-10-06 from the paper's own Table 1 (papers/10.3390_v13081632.pdf), rendered at 220 dpi and read by eye as well as extracted as text; both agree, and the same three sequences are printed in Table 2 of Geiselhardt et al. 2022 (10.1128/jcm.02505-21) as 'CDV-Mix 3, Halecker et al.'. PROVENANCE: this is the Scagliarini et al. 2007 P-gene assay (10.1007/s11259-007-0020-9, registry entry CDV_P_gene_Scagliarini_2007) 'decisively adapted' to newer genotypes. CDV3-R is byte-identical to Scagliarini's CDVR3. The forward (CDV4.1-F, degenerate, starts 2 nt upstream of CDVF4, hence 116 bp instead of 114) and the probe (CD3.1-FAMas, degenerate at positions 13 and 16, FAM/BHQ1, antisense) are Halecker's modifications, so oligos_designed_here is true for the modified pair but the shared reverse primer means the two registry entries overlap. EXCLUDED from this paper's Table 1: the ELIA-Mix (Elia 2006, entered separately as CDV_N_gene_Elia_2006), CDV-Mix 7 (entered separately), and the EGFP-Mix 2-HEX and beta-Actin-Mix 2-HEX internal controls (heterologous and host-gene controls, not CDV targets). VERIFIED on MN267060.1 (S460/15, Europe-1): forward at 2204-2225, reverse site 2297-2319, probe 2251-2274 (minus strand): a 116 bp product, the paper's figure. Retrieval: the archive is every GenBank nuccore record under txid11232 (Morbillivirus canis; 4,063 records on 2026-10-06), fetched whole rather than strided because the total is small. 'Spanning' below means the record holds the whole primer-to-primer window, judged by the screen producing a product or, for records with none, by a BLAST of the MN267060.1 window covering both ends. MEASURED: 605 records span the amplicon and all 605 give exactly 116 bp with the probe present: 536 detect, 25 reduced, 44 fail (88.6% detect, 92.7% detect+reduced); 299 are genomes. The other 3,458 give no_amplicon (3,446 with no primer site: records that do not cover the P region; 11 truncated; 1 labelled diverged, MT932497.1, whose reverse site lies under a run of Ns). For comparison, the existing Scagliarini 2007 entry screened on the same archive gives 604 spanning records at 114 bp, 435 detect, 78 reduced, 91 fail (72.0% detect), and its CDVF4 mismatches at position 4 in 499 of 604 records, which is the weak spot this modification repairs. Halecker's ROC/LOD/diagnostic-sensitivity (98.9%) figures are the paper's and were not checked. Screened against 116 PDV records (txid3052347) all 72 spanning records fail, consistent with the paper's report that PDV is not detected. SCOPE: CDV-wide, one of two P-gene assays the paper pairs as a 'double check'; the paper's panel was mostly European lineages and the authors say the other lineages are untested.</p><p><b>2026-10-27</b> TAXID RETIRED 2026-10-27: NCBI has merged 11232 into 3052342 (Morbillivirus canis), so this entry now carries the canonical id. Retrieval resolved the old id and nothing had noticed, which is the point -- an entry on a retired id is one taxonomy release from an empty archive. data/retrieved/11232/ moved to data/retrieved/3052342/ and the manifest was rebuilt in the same commit, so no archive was re-fetched. Found by scripts/check_taxids.py's containment check; see docs/journal/2026-10-27-retired-taxids.md.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=CDV_P_gene_Mix3_Halecker_2021%3A%20&body=Entry%3A%20CDV_P_gene_Mix3_Halecker_2021%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/CDV_P_gene_Mix3_Halecker_2021/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/CDV_P_gene_Mix3_Halecker_2021.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/CDV_P_gene_Mix3_Halecker_2021.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

