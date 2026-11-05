# Development and Validation of a Pan-Genotypic Real-Time Quantitative Reverse Transcription-PCR Assay To Detect Canine Distemper Virus and Phocine Distemper Virus in Domestic Animals and Wildlife

<p class="aw-byline">Geiselhardt and 12 others · Journal of Clinical Microbiology · 2022</p>

<p class="aw-doi"><a href="https://doi.org/10.1128/jcm.02505-21">doi:10.1128/jcm.02505-21</a></p>

??? quote "Full citation"
    Geiselhardt F, Peters M, Jo WK, Schadenhofer A, Puff C, Baumgärtner W, Kydyrmanov A, Kuiken T, Piewbang C, Techangamsuwan S, Osterhaus ADME, Beineke A, Ludlow M. Development and Validation of a Pan-Genotypic Real-Time Quantitative Reverse Transcription-PCR Assay To Detect Canine Distemper Virus and Phocine Distemper Virus in Domestic Animals and Wildlife. J Clin Microbiol 2022;60(5).

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">Morbillivirus_canis_P_Geiselhardt_2022</span></p>

**Morbillivirus canis — P (phosphoprotein) (Geiselhardt 2022)**

| | |
|---|---|
| Target | Morbillivirus canis (formerly Canine morbillivirus) (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3052342" title="Morbillivirus canis">taxid 3052342</a>) |
| Gene | P (phosphoprotein) |
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

    Something about this entry would make a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld on
    purpose, rather than shown with a caveat attached.

    - **`target_scope_unresolved`** — also detects PDV (Morbillivirus phocae, txid3052347) while the taxid here is CDV only; decide whether a PDV-scoped entry is wanted

This map shows where records differ from the oligos as entered. No status is given, for
the reason above, so it is not a verdict.
Some of these records may be taxa the assay isn't aimed at.

## Mismatch distribution

Each oligo drawn base by base, 5′ to 3′. The shaded region is the one the scoring
penalizes more heavily, and it depends on the oligo. For a primer it is the 3′ window,
where a mismatch sits in the polymerase’s catalytic site. For a probe it is the central
third: a hydrolysis probe is never extended, its 3′ end carries the quencher and it is
cleaved by exonuclease activity, so what matters is duplex stability. Bar height is the
share of records that differ at that position. Bar color is what that costs, measured
as the fall in detection between records that differ there and records that do not:

<span class="aw-key"><span class="aw-key-swatch aw-bar-strong"></span> detection falls by 25 points or more</span>
<span class="aw-key"><span class="aw-key-swatch aw-bar-mid"></span> falls 10 to 25</span>
<span class="aw-key"><span class="aw-key-swatch aw-bar-weak"></span> little or no effect: variation the assay tolerates</span>

Hover for counts. A tall gray bar is a polymorphism the assay tolerates; a short red
bar is a position that matters.

<svg class="aw-track" viewBox="0 0 468 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="105" y="52">forward</text><text class="aw-track-name" x="105" y="64">panCDV-F</text><rect class="aw-zone" x="375.4" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="135.4" y1="44.0" x2="450.4" y2="44.0"/><text class="aw-base" x="142.9" y="57">G</text><text class="aw-base" x="157.9" y="57">G</text><text class="aw-base" x="172.9" y="57">T</text><text class="aw-base" x="187.9" y="57">G</text><text class="aw-base" x="202.9" y="57">A</text><text class="aw-base" x="217.9" y="57">A</text><text class="aw-base" x="232.9" y="57">G</text><text class="aw-base" x="247.9" y="57">A</text><text class="aw-base" x="262.9" y="57">G</text><text class="aw-base" x="277.9" y="57">G</text><text class="aw-base" x="292.9" y="57">T</text><text class="aw-base" x="307.9" y="57">T</text><text class="aw-base" x="322.9" y="57">A</text><text class="aw-base" x="337.9" y="57">A</text><text class="aw-base" x="352.9" y="57">G</text><text class="aw-base" x="367.9" y="57">G</text><text class="aw-base" x="382.9" y="57">G</text><text class="aw-base" x="397.9" y="57">A</text><text class="aw-base" x="412.9" y="57">A</text><text class="aw-base" x="427.9" y="57">T</text><text class="aw-base" x="442.9" y="57">C</text><text class="aw-tick" x="442.9" y="71">1</text><text class="aw-tick" x="382.9" y="71">5</text><text class="aw-tick" x="307.9" y="71">10</text><text class="aw-tick" x="232.9" y="71">15</text><text class="aw-tick" x="157.9" y="71">20</text><text class="aw-tick" x="142.9" y="71">21</text><text class="aw-end" x="131" y="57">5′</text><text class="aw-end aw-end-3" x="454" y="57">3′</text><text class="aw-track-label" x="105" y="134">reverse</text><text class="aw-track-name" x="105" y="146">panCDV-PDV-R</text><rect class="aw-zone" x="345.4" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="135.4" y1="126.0" x2="420.4" y2="126.0"/><text class="aw-base" x="142.9" y="139">A</text><text class="aw-base" x="157.9" y="139">T</text><text class="aw-base" x="172.9" y="139">C</text><text class="aw-base" x="187.9" y="139">C</text><text class="aw-base" x="202.9" y="139">C</text><text class="aw-base" x="217.9" y="139">C</text><text class="aw-base" x="232.9" y="139">A</text><text class="aw-base" x="247.9" y="139">G</text><text class="aw-base" x="262.9" y="139">T</text><text class="aw-base" x="277.9" y="139">T</text><text class="aw-base" x="292.9" y="139">A</text><text class="aw-base" x="307.9" y="139">G</text><text class="aw-base" x="322.9" y="139">A</text><text class="aw-base" x="337.9" y="139">T</text><text class="aw-base" x="352.9" y="139">G</text><text class="aw-base" x="367.9" y="139">A</text><text class="aw-base" x="382.9" y="139">A</text><text class="aw-base" x="397.9" y="139">G</text><text class="aw-base" x="412.9" y="139">C</text><text class="aw-tick" x="412.9" y="153">1</text><text class="aw-tick" x="352.9" y="153">5</text><text class="aw-tick" x="277.9" y="153">10</text><text class="aw-tick" x="202.9" y="153">15</text><text class="aw-tick" x="142.9" y="153">19</text><text class="aw-end" x="131" y="139">5′</text><text class="aw-end aw-end-3" x="424" y="139">3′</text><text class="aw-track-label" x="105" y="216">probe</text><text class="aw-track-name" x="105" y="228">panCDV-PDV-probe</text><rect class="aw-zone" x="225.4" y="174.0" width="120.0" height="52.0"/><line class="aw-axis" x1="135.4" y1="208.0" x2="435.4" y2="208.0"/><text class="aw-base" x="142.9" y="221">T</text><text class="aw-base" x="157.9" y="221">C</text><text class="aw-base" x="172.9" y="221">C</text><text class="aw-base" x="187.9" y="221">Y</text><text class="aw-base" x="202.9" y="221">T</text><text class="aw-base" x="217.9" y="221">C</text><text class="aw-base" x="232.9" y="221">G</text><text class="aw-base" x="247.9" y="221">G</text><text class="aw-base" x="262.9" y="221">A</text><text class="aw-base" x="277.9" y="221">A</text><text class="aw-base" x="292.9" y="221">T</text><text class="aw-base" x="307.9" y="221">A</text><text class="aw-base" x="322.9" y="221">A</text><text class="aw-base" x="337.9" y="221">T</text><text class="aw-base" x="352.9" y="221">C</text><text class="aw-base" x="367.9" y="221">T</text><text class="aw-base" x="382.9" y="221">T</text><text class="aw-base" x="397.9" y="221">C</text><text class="aw-base" x="412.9" y="221">G</text><text class="aw-base" x="427.9" y="221">C</text><text class="aw-tick" x="427.9" y="235">1</text><text class="aw-tick" x="367.9" y="235">5</text><text class="aw-tick" x="292.9" y="235">10</text><text class="aw-tick" x="217.9" y="235">15</text><text class="aw-tick" x="142.9" y="235">20</text><text class="aw-end" x="131" y="221">5′</text><text class="aw-end aw-end-3" x="439" y="221">3′</text></svg>
<p class="aw-empty">No position carried a mismatch in enough records to report. 11 of the 395 records in the recent and baseline windows were not detected. Their mismatches are either spread too thinly to report at any one position, or the record has no site for an oligo (for example no probe site inside the amplicon), which leaves no position to draw.</p>


## Scope

**Scored against:** every record retrieved.  
**Retrieved from:** Morbillivirus canis (formerly Canine morbillivirus) (taxid 3052342), every record.

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `target_scope_unresolved`.


## Curation record

Added 2026-10-06 from the paper's own Table 2 (papers/10.1128_jcm.02505-21.pdf). 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-06</b> Added 2026-10-06 from the paper's own Table 2 (papers/10.1128_jcm.02505-21.pdf). The table page was rendered at 220 dpi and read by eye as well as extracted as text; the two agree base for base. ROLES: panCDV-F (no wobble) is the assay's forward primer and panCDV-PDV-F (R at position 7) is the variant made to also cover phocine distemper virus; the paper found no Cq difference between them, so the second is stored as an alternate (screening gives identical results with either alone). panCDV-PDV-R is the reverse primer. panCDV-PDV-probe (FAM, BHQ1, Y at position 4) is the probe, written reverse-sense in the paper. The paper designed all of these (94 CDV and PDV genome sequences aligned in MEGA7/MAFFT). EXCLUDED: EGFP-1-F, EGFP-2-R and EGFP-HEX (heterologous EGFP internal control from Hoffmann 2006, not a CDV target; note this paper's EGFP-1-F is 17 nt GACCACTACCAGAACAC against 20 nt GACCACTACCAGCAGAACAC in the Halecker 2021 table, probably a typo here, irrelevant because it is excluded); the CDV-Th and CDV-S443 H-gene ORF primers in Methods (restriction-site tailed cloning primers used to sequence strains, not a detection assay); and CDV4.1-F/CDV3-R/CD3.1-FAMas and CDV-1808-F/CDV-1903-R/CDV-1842-FAM, which the paper uses as comparators and which are Halecker et al. 2021 assays, entered as Morbillivirus_canis_P_Halecker_2021_Mix3 and Morbillivirus_canis_P_Halecker_2021_Mix7. VERIFIED against the paper's design accession MN267060.1 (strain S460/15, Europe-1, complete genome): forward site at 2149-2169, probe at 2267-2286 (minus strand), reverse site at 2290-2308, exactly as the text states, giving the stated 160 bp. Retrieval: the archive is every GenBank nuccore record under txid11232 (Morbillivirus canis; 4,063 records on 2026-10-06), fetched whole rather than strided because the total is small. 'Spanning' below means the record holds the whole primer-to-primer window, judged by the screen producing a product or, for records with none, by a BLAST of the MN267060.1 window covering both ends. MEASURED: 398 records span the amplicon and all 398 give exactly 160 bp with the probe site present (unimodal): 387 detect, 8 reduced, 3 fail, so 97.2% detect and 99.2% detect+reduced among spanning records; 299 of the 398 are complete or partial genomes. The other 3,665 give no_amplicon: 3,430 carry no primer site at all (H, F, N, M, L gene records that do not cover the P region), 231 are truncated, and 184 of the truncated ones are P-gene fragments that begin 4 nt inside the forward primer site (deposited primer-trimmed), so the site cannot be tested; 4 are labelled diverged (three H or N-gene records without the P region, and MT932497.1, a near-complete genome with a run of Ns across the reverse site, so untestable). That is coverage, not primer failure. amplicon_bp 160 is both the paper's figure and the measured one. CROSS-CHECKS against the paper's own claims: the Asia-4 Thai genomes MH496772-MH496775 match this assay at penalty 0-0.5, while on MH496772-MH496774 CDV-Mix 3 (forward, probe) and CDV-Mix 7 (reverse, probe) carry mismatches and fail or are reduced, which is the paper's stated reason for adding Asia-4. Screening 116 Phocine morbillivirus records (txid3052347, a separate taxon, not in this entry's archive): 59 span the amplicon and all 59 detect at 160 bp with the probe, matching the paper's PDV claim. SCOPE: taxid is CDV only; the assay is designed to detect PDV as well, which the CDV archive does not measure. America-3, America-5 and Asia-3 have no P-gene sequence in GenBank to test (the paper says so too). Sensitivity (LOD) figures are the paper's and were not checked here.</p><p><b>2026-10-27</b> TAXID RETIRED 2026-10-27: NCBI has merged 11232 into 3052342 (Morbillivirus canis), so this entry now carries the canonical id. Retrieval resolved the old id and nothing had noticed, which is the point -- an entry on a retired id is one taxonomy release from an empty archive. data/retrieved/11232/ moved to data/retrieved/3052342/ and the manifest was rebuilt in the same commit, so no archive was re-fetched. Found by scripts/check_taxids.py's containment check; see docs/journal/2026-10-27-retired-taxids.md.</p></details>

## Corrections

If this entry misrepresents the assay, that is a bug and a report is welcome,
especially from the group that designed it. The sequences, the product size and
the scope are all curated from the paper and can be wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=Morbillivirus_canis_P_Geiselhardt_2022%3A%20&body=Entry%3A%20Morbillivirus_canis_P_Geiselhardt_2022%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/Morbillivirus_canis_P_Geiselhardt_2022/%0ARun%3A%202026-11-01%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/Morbillivirus_canis_P_Geiselhardt_2022.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/Morbillivirus_canis_P_Geiselhardt_2022.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

