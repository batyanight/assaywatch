# Detection of Francisella tularensis in blood by polymerase chain reaction

<p class="aw-byline">Long · Journal of Clinical Microbiology · 1993</p>

<p class="aw-doi"><a href="https://doi.org/10.1128/jcm.31.1.152-154.1993">doi:10.1128/jcm.31.1.152-154.1993</a></p>

??? quote "Full citation"
    Long, G. W., Oprandy, J. J., Narayanan, R. B., Fortier, A. H., Porter, K. R. & Nacy, C. A. Detection of Francisella tularensis in blood by polymerase chain reaction. Journal of Clinical Microbiology 31, 152-154 (1993).

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">FRANCISELLA_tularensis_tul4_Long_1993</span></p>

**FRANCISELLA TULARENSIS — tul4 (lpnA) 17 kDa lipoprotein (Long 1993)**

| | |
|---|---|
| Target | Francisella tularensis (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=263" title="Francisella tularensis">taxid 263</a>) |
| Gene | tul4 |
| Chemistry | conventional |
| Amplicon | 250 bp |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | Ff393 | `ATGGCGAGTGATACTGCTTG` | 20 nt |
| reverse | Ff642 | `GCATCATCAGAGCCACCTAA` | 20 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`oligo_sequence_uncertain`** — the probe is omitted: the OCR of its sequence was not reliable enough to enter


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
lpnA[Gene] OR tul4[Gene] OR "17 kDa"[Title] OR "complete genome"[Title]
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `oligo_sequence_uncertain`.


## Curation record

Added 2026-10-05 from the paper's own text, read out of the PDF in papers/ rather than transcribed from any secondary list. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-05</b> Added 2026-10-05 from the paper's own text, read out of the PDF in papers/ rather than transcribed from any secondary list. Candidate surfaced by the journal sweep in docs/journal/2026-10-04-literature-audit.md; sequences extracted with scripts/extract_candidate_oligos.py and then checked against real GenBank records before the entry was trusted. Tularemia was absent from the registry. VERIFIED on a tul4-containing contig (NZ_RJDA01000027.1): both primers match with ZERO mismatches and span a 250 bp product. amplicon_bp is measured; the paper states no size. ORIENTATION, which is worth recording because it looked wrong at first. On that contig Ff642 reads on the plus strand and Ff393 only as its reverse complement, i.e. the opposite of the assignment here. That is simply the gene lying on the contig's minus strand: the primer names encode positions 393 and 642 in the tul4 reading frame, so in gene coordinates Ff393 is the forward and Ff642 the reverse, which is how they are stored. The screener accepts either orientation, so the call is unaffected either way.</p><p>THE PAPER'S PROBE IS DELIBERATELY OMITTED. Long et al. detect the product by hybridisation with an oligonucleotide probe, FT443, rather than by fluorescence, so this is a conventional PCR and a probe is not required. More importantly the probe sequence as read from this 1993 scan carries 8 mismatches against the same contig where both primers match perfectly, which means the OCR mangled it. Entering a sequence known to be corrupt would be worse than leaving it out. A clean copy of Table/text would let it be added.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=FRANCISELLA_tularensis_tul4_Long_1993%3A%20&body=Entry%3A%20FRANCISELLA_tularensis_tul4_Long_1993%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/FRANCISELLA_tularensis_tul4_Long_1993/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/FRANCISELLA_tularensis_tul4_Long_1993.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/FRANCISELLA_tularensis_tul4_Long_1993.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

