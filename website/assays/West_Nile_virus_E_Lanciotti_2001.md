# Nucleic Acid Sequence-Based Amplification Assays for Rapid Detection of West Nile and St. Louis Encephalitis Viruses

<p class="aw-byline">Lanciotti and Kerst · Journal of Clinical Microbiology · 2001</p>

<p class="aw-doi"><a href="https://doi.org/10.1128/JCM.39.12.4506-4513.2001">doi:10.1128/JCM.39.12.4506-4513.2001</a></p>

??? quote "Full citation"
    Lanciotti RS, Kerst AJ. 2001. J Clin Microbiol 39:4506-4513

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">West_Nile_virus_E_Lanciotti_2001</span></p>

**West Nile virus — E (envelope) (Lanciotti 2001)**

| | |
|---|---|
| Target | West Nile virus (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11082">taxid 11082</a>) |
| Gene | E (envelope) |
| Chemistry | conventional |
| Amplicon | 162 bp |
| Registry status | active |
| Verdict | — |

!!! warning "No status is reported for this assay"

    Something about this entry would make a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld on
    purpose, rather than shown with a caveat attached.

    - **`not_screenable`** — the stored pair is NASBA, isothermal at 41 C with T7 transcription; the penalties are calibrated on PCR


## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | WN-1333 | `ACCAAGGCAATAGGAAGAACCA` | 22 nt |
| reverse | WN-1494c | `GTATGAAGGCGCCGCAGGAGTGA` | 23 nt |


## Scope

**Meant to detect:** West Nile virus, envelope gene, as a NASBA primer pair.  
**Scored against:** every record retrieved.  
**Retrieved from:** West Nile virus (taxid 11082), every record.

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `oligos_modified`, `not_screenable`.


## Curation record

id corrected 2026-10-04: it misspelled Lanciotti as 'Lancotti'. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-04</b> id corrected 2026-10-04: it misspelled Lanciotti as 'Lancotti'. Crossref confirms the author. THE in-text VERDICT IS EXPLAINED, 2026-10-05, and the explanation characterises the modification this entry was already flagged for. The 2026-10-04 audit listed WN-1333 and WN-1494c among the rows needing a human to open the primer table; this is that reading. Lanciotti and Kerst 2001 Table 1 lists them under 'WN virus-specific NASBA assay primers and probes', and prints each with a NON-TEMPLATED 5' TAIL in lower case: WN 1333 at genome positions 1333-1354 as gatgcaaggtcgcatatgag-ACCAAGGCAATAGGAAGAACCA, and WN1494c at 1494-1472 as aattctaatacgactcactatagggagaagg-GTATGAAGGCGCCGCAGGAGTGA, whose tail is the T7 promoter that NASBA needs in order to transcribe. The registry stores only the upper-case target-binding cores. That is why the verifier reports in-text rather than exact - the sequence is in the paper but is not the whole of any listed oligo - and it is the right verdict rather than a problem to fix.</p><p>THE SEQUENCES ARE DELIBERATELY NOT CHANGED. The registry's convention elsewhere, in the orthobunyavirus and CDV cloning-primer entries, is to store the full published oligo and name the prefix in tail_5prime, which keeps matching on the binding part. That convention is not applied here because dropping the NASBA tails is not a transcription slip: chemistry is recorded as conventional, these two are run as an ordinary RT-PCR, and a T7 promoter has no business in that reaction. The stored form is the oligo as ordered, which is the same reasoning that keeps GPO-1FMod as stored. MODIFIED_IN_HOUSE stays, now with the modification described instead of merely asserted.</p><p><b>2026-10-03</b> AMPLICON MEASURED AND CORRECTED: against all 9,125 records of the 2026-10-03 West Nile archive the pair gives a product in 5,785 and it is 162 bp in every single one - no spread at all - which is also exactly what Lanciotti's own table states for this pair, and what its printed positions give (1333 to 1494 inclusive). amplicon_bp was 161 and is now 162.</p><p><b>2026-11-06</b> COVERAGE IS HEALTHY, worth recording beside the drift findings elsewhere today: the forward primer is exact in 5,190 of the 5,785 and the reverse in 5,349, so this twenty-five-year-old assay still sits on the consensus of its target. CORRECTED 2026-11-06: the paper runs these two only as NASBA primers, isothermal at 41 C (Table 1); its RT-PCR and TaqMan use a different, earlier set (ref 10), and the 45 cycles were that assay's. So the earlier 'ordinary RT-PCR' reading is unsupported, and the status is withheld because the penalties are calibrated on PCR.</p></details>

## Corrections

If this entry misrepresents the assay, that is a bug and a report is welcome,
especially from the group that designed it. The sequences, the product size and
the scope are all curated from the paper and can be wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=West_Nile_virus_E_Lanciotti_2001%3A%20&body=Entry%3A%20West_Nile_virus_E_Lanciotti_2001%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/West_Nile_virus_E_Lanciotti_2001/%0ARun%3A%202026-11-01%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/West_Nile_virus_E_Lanciotti_2001.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/West_Nile_virus_E_Lanciotti_2001.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

