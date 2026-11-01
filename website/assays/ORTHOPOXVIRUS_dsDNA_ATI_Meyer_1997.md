# Gene for A-type inclusion body protein is useful for a polymerase chain reaction assay to differentiate orthopoxviruses

<p class="aw-byline">Meyer · Journal of Virological Methods · 1997</p>

<p class="aw-doi"><a href="https://doi.org/10.1016/S0166-0934(96)02155-6">doi:10.1016/S0166-0934(96)02155-6</a></p>

??? quote "Full citation"
    Meyer H, Ropp SL, Esposito JJ. Gene for A-type inclusion body protein is useful for a polymerase chain reaction assay to differentiate orthopoxviruses. J Virol Methods 64:217-221 (1997).

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997</span></p>

**ORTHOPOXVIRUS (dsDNA) — A-type inclusion body (ATI) gene consensus PCR, species by amplicon size (Meyer 1997)**

| | |
|---|---|
| Target | Orthopoxvirus (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10242" title="Orthopoxvirus">taxid 10242</a>) |
| Gene | ATI (A-type inclusion body protein) |
| Chemistry | conventional |
| Amplicon | — |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | ATI-up-1 | `AATACAAGGAGGATCT` | 16 nt |
| reverse | ATI-low-1 | `CTTAACTTTTTCTTTCTC` | 18 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`not_screenable`** — identification is by product size plus an XbaI digest, which the screen cannot model
    - **`oligo_source_unresolved`** — a Meyer 1994 origin is suspected but not established


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `amplicon_multimodal`, `not_screenable`, `oligo_source_unresolved`.


## Curation record

Added 2026-10-06. WHAT THE PAPER IS (the index had no title): Meyer H, Ropp SL, Esposito JJ, J Virol Methods 64:217-221 (1997), accepted 25 Oct 1996, 'Gene for A-type inclusion body protein is useful for a polymerase chain reaction assay to differentiate orthopoxviruses'. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-06</b> Added 2026-10-06.</p><p>WHAT THE PAPER IS (the index had no title): Meyer H, Ropp SL, Esposito JJ, J Virol Methods 64:217-221 (1997), accepted 25 Oct 1996, 'Gene for A-type inclusion body protein is useful for a polymerase chain reaction assay to differentiate orthopoxviruses'. DOI: the paper prints its PII as S0166-0934(96)02155-6, which is DOI 10.1016/S0166-0934(96)02155-6; doi_verified stays false for the resolver. READ: papers/10.1016_s0166-0934_96_02155-6.pdf is a scan with an OCR text layer. The page carrying the primers (page 3) was rendered at 200 dpi and read by eye: ATI-up-1 5'-AATACAAGGAGGATCT-3' (16 nt) and ATI-low-1 5'-CTTAACTTTTTCTTTCTC-3' (18 nt). The cycling is 25 cycles with 40 °C annealing, a low-stringency consensus pair; oligos_designed_here is null (the paper extends Meyer et al. 1994 but does not say the oligos were first published there).</p><p>DIFFERENTIATION ASSAY: one consensus pair across the genus, with product LENGTH (and an XbaI digest) identifying the species.</p><p><b>2026-10-19</b> MEASURED AMPLICON SIZES BY SPECIES: now the structured `species_sizes` field above, remeasured 2026-10-19 from the whole archive with patent records excluded. The hand measurement this replaces (2026-10-06) read: volepox 542 bp; skunkpox 551 bp; ectromelia 1220 bp; camelpox 879 bp; variola 1576–1583 bp; monkeypox 1067 bp (clade I) or 1533–1545 bp (clade IIb, mode 1538 bp); vaccinia 1594–1606 bp; cowpox 1673 bp. The remeasurement agrees except that it adds bands the hand pass missed (vaccinia 1547 and 1671, cowpox 1598–1601 and 1505, akhmetapox 1505, taterapox 1628) and drops skunkpox, whose records score fail.</p><p><b>2026-10-20</b> APPROXIMATE RANGE: 540–1700 bp. The paper's stated sizes differed by 1–32 bp from measured values for several species. RESOLVED 2026-10-20 as gel sizing, not isolate difference: the four well-matched species sit within 3 bp, and the three outliers (monkeypox 1500, volepox 510, skunkpox 530) are all round numbers read low against non-round measurements (1535–1545, 542, 551). For volepox and skunkpox the records scored are Meyer's own isolates (volepox CA, skunkpox WA/1978, the only genomes of either species in GenBank), which excludes isolate difference for those two. Monkeypox is partly a strain question: no Copenhagen genome exists, and his Copenhagen is a non-Zairian isolate, so clade IIb is the band to compare. See docs/journal/2026-10-20-meyer-ati-bench-panel.md. Measured on: every GenBank Orthopoxvirus (txid10242) genome 100–400 kb (542 non-monkeypox records), plus 162 monkeypox strided every 80th, plus 155 ATI-titled records. Non-monkeypox genomes: 410 detect, 79 reduced, 48 fail, 5 no_amplicon (75.6% detect among spanning). Monkeypox: 157 detect of 162 (96.9%). Why non-detects in monkeypox and variola: consensus pair has obligate mismatches in some lineages; pipeline rules score them as reduced or fail.</p><p>NO REGISTRY OVERLAP: no 15 nt window of either primer occurs in existing poxvirus entries. SCOPE: genus-wide; interpret results by species, not by genus-wide share.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997%3A%20&body=Entry%3A%20ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

