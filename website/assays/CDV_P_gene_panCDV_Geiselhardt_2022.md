# Development and Validation of a Pan-Genotypic Real-Time Quantitative Reverse Transcription-PCR Assay To Detect Canine Distemper Virus and Phocine Distemper Virus in Domestic Animals and Wildlife

<p class="aw-byline">Geiselhardt · Journal of Clinical Microbiology · 2022</p>

<p class="aw-doi"><a href="https://doi.org/10.1128/jcm.02505-21">doi:10.1128/jcm.02505-21</a></p>

??? quote "Full citation"
    Geiselhardt F, Peters M, Jo WK, Schadenhofer A, Puff C, Baumgärtner W, Kydyrmanov A, Kuiken T, Piewbang C, Techangamsuwan S, Osterhaus ADME, Beineke A, Ludlow M. Development and Validation of a Pan-Genotypic Real-Time Quantitative Reverse Transcription-PCR Assay To Detect Canine Distemper Virus and Phocine Distemper Virus in Domestic Animals and Wildlife. J Clin Microbiol 2022;60(5).

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">CDV_P_gene_panCDV_Geiselhardt_2022</span></p>

**CANINE DISTEMPER VIRUS — P gene pan-genotypic TaqMan RT-qPCR (Geiselhardt 2022)**

| | |
|---|---|
| Target | Morbillivirus canis (formerly Canine morbillivirus) (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052342" title="Morbillivirus canis">taxid 3052342</a>) |
| Gene | P |
| Chemistry | hydrolysis_probe |
| Amplicon | 160 bp |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | panCDV-F | `GGTGAAGAGGTTAAGGGAATC` | 21 nt |
| reverse | panCDV-PDV-R | `ATCCCCAGTTAGATGAAGC` | 19 nt |
| probe | panCDV-PDV-probe | `TCCYTCGGAATAATCTTCGC` | 20 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`target_scope_unresolved`** — also detects PDV (Morbillivirus phocae, txid3052347) while the taxid here is CDV only; decide whether a PDV-scoped entry is wanted


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `target_scope_unresolved`.


## Curation record

Added 2026-10-06 from the paper's own Table 2 (papers/10.1128_jcm.02505-21.pdf). 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-06</b> Added 2026-10-06 from the paper's own Table 2 (papers/10.1128_jcm.02505-21.pdf). The table page was rendered at 220 dpi and read by eye as well as extracted as text; the two agree base for base. ROLES: panCDV-F (no wobble) is the assay's forward primer and panCDV-PDV-F (R at position 7) is the variant made to also cover phocine distemper virus; the paper found no Cq difference between them, so the second is stored as an alternate (screening gives identical results with either alone). panCDV-PDV-R is the reverse primer. panCDV-PDV-probe (FAM, BHQ1, Y at position 4) is the probe, written reverse-sense in the paper. The paper designed all of these (94 CDV and PDV genome sequences aligned in MEGA7/MAFFT). EXCLUDED: EGFP-1-F, EGFP-2-R and EGFP-HEX (heterologous EGFP internal control from Hoffmann 2006, not a CDV target; note this paper's EGFP-1-F is 17 nt GACCACTACCAGAACAC against 20 nt GACCACTACCAGCAGAACAC in the Halecker 2021 table, probably a typo here, irrelevant because it is excluded); the CDV-Th and CDV-S443 H-gene ORF primers in Methods (restriction-site tailed cloning primers used to sequence strains, not a detection assay); and CDV4.1-F/CDV3-R/CD3.1-FAMas and CDV-1808-F/CDV-1903-R/CDV-1842-FAM, which the paper uses as comparators and which are Halecker et al. 2021 assays, entered as CDV_P_gene_Mix3_Halecker_2021 and CDV_P_gene_Mix7_Halecker_2021. VERIFIED against the paper's design accession MN267060.1 (strain S460/15, Europe-1, complete genome): forward site at 2149-2169, probe at 2267-2286 (minus strand), reverse site at 2290-2308, exactly as the text states, giving the stated 160 bp. Retrieval: the archive is every GenBank nuccore record under txid11232 (Morbillivirus canis; 4,063 records on 2026-10-06), fetched whole rather than strided because the total is small. 'Spanning' below means the record holds the whole primer-to-primer window, judged by the screen producing a product or, for records with none, by a BLAST of the MN267060.1 window covering both ends. MEASURED: 398 records span the amplicon and all 398 give exactly 160 bp with the probe site present (unimodal): 387 detect, 8 reduced, 3 fail, so 97.2% detect and 99.2% detect+reduced among spanning records; 299 of the 398 are complete or partial genomes. The other 3,665 give no_amplicon: 3,430 carry no primer site at all (H, F, N, M, L gene records that do not cover the P region), 231 are truncated, and 184 of the truncated ones are P-gene fragments that begin 4 nt inside the forward primer site (deposited primer-trimmed), so the site cannot be tested; 4 are labelled diverged (three H or N-gene records without the P region, and MT932497.1, a near-complete genome with a run of Ns across the reverse site, so untestable). That is coverage, not primer failure. amplicon_bp 160 is both the paper's figure and the measured one. CROSS-CHECKS against the paper's own claims: the Asia-4 Thai genomes MH496772-MH496775 match this assay at penalty 0-0.5, while on MH496772-MH496774 CDV-Mix 3 (forward, probe) and CDV-Mix 7 (reverse, probe) carry mismatches and fail or are reduced, which is the paper's stated reason for adding Asia-4. Screening 116 Phocine morbillivirus records (txid3052347, a separate taxon, not in this entry's archive): 59 span the amplicon and all 59 detect at 160 bp with the probe, matching the paper's PDV claim. SCOPE: taxid is CDV only; the assay is designed to detect PDV as well, which the CDV archive does not measure. America-3, America-5 and Asia-3 have no P-gene sequence in GenBank to test (the paper says so too). Sensitivity (LOD) figures are the paper's and were not checked here.</p><p><b>2026-10-27</b> TAXID RETIRED 2026-10-27: NCBI has merged 11232 into 3052342 (Morbillivirus canis), so this entry now carries the canonical id. Retrieval resolved the old id and nothing had noticed, which is the point -- an entry on a retired id is one taxonomy release from an empty archive. data/retrieved/11232/ moved to data/retrieved/3052342/ and the manifest was rebuilt in the same commit, so no archive was re-fetched. Found by scripts/check_taxids.py's containment check; see docs/journal/2026-10-27-retired-taxids.md.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=CDV_P_gene_panCDV_Geiselhardt_2022%3A%20&body=Entry%3A%20CDV_P_gene_panCDV_Geiselhardt_2022%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/CDV_P_gene_panCDV_Geiselhardt_2022/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/CDV_P_gene_panCDV_Geiselhardt_2022.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/CDV_P_gene_panCDV_Geiselhardt_2022.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

