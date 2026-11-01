# Natural M-segment reassortment in Potosi and Main Drain viruses: implications for the evolution of orthobunyaviruses

<p class="aw-byline">Briese · Archives of Virology · 2007</p>

<p class="aw-doi"><a href="https://doi.org/10.1007/s00705-007-1069-z">doi:10.1007/s00705-007-1069-z</a></p>

??? quote "Full citation"
    Briese, T., Kapoor, V. & Lipkin, W. I. Natural M-segment reassortment in Potosi and Main Drain viruses: implications for the evolution of orthobunyaviruses. Archives of Virology 152, 2237-2247 (2007).

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">ORTHOBUNYAVIRUS_ssRNA_S_segment_Cac_Briese_2007</span></p>

**ORTHOBUNYAVIRUS (ssRNA) — S segment, Cac-2/Cac-7 (Briese 2007)**

| | |
|---|---|
| Target | Orthobunyavirus (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11572">taxid 11572</a>) |
| Gene | S segment |
| Chemistry | conventional |
| Amplicon | 471 bp |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | Cac-2-FWD | `DCTTAACYTTGGRGGCTGGA` | 20 nt |
| reverse | Cac-7-REV | `CTVACRTTDGYYTTCTTCCA` | 20 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`target_scope_unresolved`** — the source never states what this assay is meant to cover


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
S[Gene] OR M[Gene] OR "S segment"[Title] OR "M segment"[Title] OR nucleocapsid[Title] OR glycoprotein[Title] OR "complete genome"[Title]
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `target_scope_unresolved`.


## Curation record

Added 2026-10-04 from Briese et al. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-04</b> Added 2026-10-04 from Briese et al. 2007 Table 1 (doi:10.1007/s00705-007-1069-z), read from the paper itself rather than from any secondary list. The table gives each primer's sequence and the genome position of its 3'-terminal base, numbered on the Bunyamwera virus prototype 1943 reference (D00353 = S, M11852 = M, X14383 = L). Degenerate positions are printed as lower-case IUPAC codes and are transcribed here in upper case; sequences are printed in triplets, which is how each primer's length was checked. Non-authentic (cloning-tail) bases are marked in the table by a distinct italic font, and NONE of the primers in this entry carries one except where tail_5prime is set below. amplicon_bp is COMPUTED, not quoted: the paper gives 3' positions, not product sizes, so the product is taken as the span from the forward primer's 5' base to the reverse primer's 5' base using the printed 3' positions and the primer lengths. Cac-2-FWD is 20 nt with its 3' base at 290, so it binds 271-290; Cac-7-REV is 20 nt with its 3' base at 722, so it binds 722-741; the product is 271-741 = 471 bp. The arithmetic is corroborated by the primer names, which encode their own positions (BUNS-3-L947 at 947, BUNL650R at 601-630). Treat the size as approximate: it is exact only on the Bunyamwera reference, and these are consensus primers meant for a whole serogroup. SCOPE. The paper designed these from an alignment of 'orthobunyaviruses of the CE and BUN serogroups and Guaroa virus', so the claim is the California encephalitis and Bunyamwera serogroups, not the whole genus. The registry target is genus Orthobunyavirus (~18 serogroups), so a low detected share here is very likely scope rather than drift. Screening the two assays already in the registry on 2026-10-04 showed the pattern plainly: strong on the design serogroups (Cache Valley 14/15, Maguari 4/5) and near-zero on Simbu-serogroup viruses (Oropouche 0/24, Akabane 0/7, Schmallenberg 0/7, Manzanilla 0/4). Left unscoped pending the registry-wide decision on lineage scoping. This is the second of the two S-segment pairs in Table 1 and the only one run at 52 C, the highest annealing temperature in the paper, which suggests it is the more specific of the two. The paper never says what 'Cac' stands for and cites its reference [8] for the consensus primer panel, so the intended target is not stated: Cache Valley virus is the obvious reading given the paper's subject, but that is an inference and is flagged rather than recorded as fact. Screened on 2026-10-04 against the existing orthobunyavirus archive: 73 evaluable of 2,056, 40 detected (55%). What it detects supports the stated design scope and is better evidence than the guess about the name: Batai 8/8, Cache Valley 4/4, Guaroa 4/4 (the paper names Guaroa explicitly as one of the inputs to its design alignment), Ilesha 3/3, Germiston, Bunyamwera, Sororoca - Bunyamwera serogroup throughout.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=ORTHOBUNYAVIRUS_ssRNA_S_segment_Cac_Briese_2007%3A%20&body=Entry%3A%20ORTHOBUNYAVIRUS_ssRNA_S_segment_Cac_Briese_2007%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/ORTHOBUNYAVIRUS_ssRNA_S_segment_Cac_Briese_2007/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/ORTHOBUNYAVIRUS_ssRNA_S_segment_Cac_Briese_2007.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/ORTHOBUNYAVIRUS_ssRNA_S_segment_Cac_Briese_2007.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

