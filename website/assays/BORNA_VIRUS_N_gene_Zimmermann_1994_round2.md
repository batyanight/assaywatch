# Detection of Borna disease virus RNA in naturally infected animals by a nested polymerase chain reaction

<p class="aw-byline">Zimmermann · Journal of Virological Methods · 1994</p>

<p class="aw-doi"><a href="https://doi.org/10.1016/0166-0934(94)90098-1">doi:10.1016/0166-0934(94)90098-1</a></p>

??? quote "Full citation"
    Zimmermann W et al. 1994. J Virol Methods 46:133-143

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">BORNA_VIRUS_N_gene_Zimmermann_1994_round2</span></p>

**BORNA VIRUS — N gene (nested)**

| | |
|---|---|
| Target | Bornaviridae (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=178830">taxid 178830</a>) |
| Gene | N gene |
| Chemistry | conventional |
| Amplicon | — |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | BornaNestF | `GCCTTGTGTTTCTATCTTTC` | 20 nt |
| reverse | BornaNestR | `ATTCTTTACCTGGGGACTCA` | 20 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`amplicon_size_unresolved`** — no product size is declared


## Scope

This entry declares **`scope_taxids`**: <a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1714619" title="Orthobornavirus bornaense">1714619</a>, <a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=12455" title="Borna disease virus">12455</a>. A record counts toward the denominator when its taxid, or any ancestor, is in that set. Records outside it are screened and reported but kept out of the statistics.

<a class="aw-download" href="BORNA_VIRUS_N_gene_Zimmermann_1994_round2.scope.txt" download>Download 2 taxids as a text file</a>

1,005 screened records fell outside the declared scope.

Disclosures on this entry: `oligos_not_in_cited_paper`, `amplicon_size_unresolved`, `orientation_inferred`.


## Curation record

Added 2026-10-19 from candidate oligo extraction (papers/10.1016_0166-0934_94_90098-1.pdf). 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-19</b> Added 2026-10-19 from candidate oligo extraction (papers/10.1016_0166-0934_94_90098-1.pdf). Internal (nested) primers from Zimmermann et al. 1994. The external (round 1) primers are in registry as BORNA_VIRUS_N_gene_Zimmermann_1994. The paper labels these as "Internal (nested) primers: antisense 5'-ATTCTTTACCTGGGGACTCA-3' sense 5'-GCCTTGTGTTTCTATCTTTC-3'". Forward/reverse assignment follows the sense/antisense labels in the paper. AMPLICON_BP: not set; nested product size must be measured against GenBank records (it is internal to the 752 bp external product).</p><p><b>2026-10-23</b> THIS ENTRY CANNOT DETECT, found 2026-10-23 and NOT fixed here. BornaNestF is stored as GCCTTGTGTTTCTATCTTTC, which is what Zimmermann 1994 prints for its internal sense primer - and measured over all 1,516 records of the Orthobornavirus archive, that sequence has an exact site in NONE of them. The template following the shared 15-mer GCCTTGTGTTTCTAT reads GTTTG in 260 records, GCTTG in 42 and GTCTG in 1. So the printed form differs from every known record at two positions including the 3'-terminal base, which `terminal_mismatch_fails` makes fatal on its own, and this entry will read 0 percent detected for reasons that have nothing to do with drift. The sibling BORNA_VIRUS_N_gene stores GCCTTGTGTTTCTATGTTTG, the 260-record form; that entry was briefly changed to the printed sequence on 2026-10-23 and reverted when its detected share fell from 67.5 percent to 0.0. Aligning this entry with the measured form would mean storing a sequence the paper does not print, which is a maintainer decision and the same one the sibling records, so it is flagged rather than applied. SCOPED 2026-10-24 to scope_taxids [1714619, 12455]. taxid 178830 is the whole Bornaviridae family, while Zimmermann et al. 1994 is a Borna disease virus assay: its title is "Detection of Borna disease virus RNA in naturally infected animals by nested PCR". Both taxids are needed and the second is the trap: 1714619 is Orthobornavirus bornaense (rank species, under Bornaviridae &gt; Orthobornavirus), but 12455 "Borna disease virus" sits under Bornaviridae &gt; UNCLASSIFIED Bornaviridae, not under the genus, so a scope list built from the genus node alone silently drops 49 genuine BoDV-1 deposits. Both taxids verified live with efetch -db taxonomy on 2026-10-24. Measured over the WHOLE 2026-10-24 calls table, which is neither the report's recent window nor patent-filtered: of 1,519 screened records 1,003 are a known taxid outside the scope, 513 are inside it and 3 carry no taxid, so about two thirds of the denominator was a different virus - carbovirus, cultervirus and the parrot, serin and estrildid orthobornaviruses. Note that drift.py's filter drops only a KNOWN out-of-scope taxid, so the 3 unknowns stay in. Scoping does NOT rescue this entry: inside the scope it reads 0 detected of 318 assessable records, because the printed BornaNestF mismatches every known record at its 3'-terminal base, as recorded above. The scope fix removes a confound here; it does not change the verdict.</p><p><b>2026-10-26</b> AMPLICON RE-MEASURED 2026-10-26, AND THE FINDING IS THAT THERE IS NOTHING TO MEASURE FROM. On results/2026-10-26/calls.tsv.gz this entry reads 1,151 no_amplicon and 369 fail, with ZERO detect and ZERO reduced. It never once amplifies, so its 369 failures have no product of its own to be anchored against and no size can be derived without inventing one. That is why amplicon_size_unresolved stays and no number is written here. Worth stating plainly for whoever reads the 369 failures: they are not evidence of drift, because an assay that has never succeeded in this archive has no baseline to decline from.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=BORNA_VIRUS_N_gene_Zimmermann_1994_round2%3A%20&body=Entry%3A%20BORNA_VIRUS_N_gene_Zimmermann_1994_round2%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/BORNA_VIRUS_N_gene_Zimmermann_1994_round2/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/BORNA_VIRUS_N_gene_Zimmermann_1994_round2.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/BORNA_VIRUS_N_gene_Zimmermann_1994_round2.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

