# GC Content-Based Pan-Pox Universal PCR Assays for Poxvirus Detection

<p class="aw-byline">Li · Journal of Clinical Microbiology · 2010</p>

<p class="aw-doi"><a href="https://doi.org/10.1128/JCM.01697-09">doi:10.1128/JCM.01697-09</a></p>

??? quote "Full citation"
    Li Y, Meyer H, Zhao H, Damon IK. 2010. GC content-based pan-pox universal PCR assays for poxvirus detection. J Clin Microbiol 48:268-276

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">PANPOX_dsDNA_lowGC_IMV_Li_2010</span></p>

**PAN-POXVIRUS (dsDNA) — low-GC universal PCR (Li 2010)**

| | |
|---|---|
| Target | Chordopoxvirinae (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10241">taxid 10241</a>) |
| Gene | insulin metalloproteinase-like protein to IMV membrane protein |
| Chemistry | conventional |
| Amplicon | 230 bp |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | low-GC-forward | `ACACCAAAAACTCATATAACTTCT` | 24 nt |
| reverse | low-GC-reverse | `CCTATTTTACTCCTTAGTAAATGAT` | 25 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`retrieval_stale`** — the retrieval query changed on 2026-10-17; these numbers predate it


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
(txid10242[Organism:exp] OR txid10260[Organism:exp] OR txid10265[Organism:exp] OR txid10275[Organism:exp] OR txid10282[Organism:exp] OR txid573055[Organism:exp] OR txid2005509[Organism:exp] OR txid2733296[Organism:exp] OR txid2733297[Organism:exp] OR txid2733298[Organism:exp] OR txid2733299[Organism:exp] OR txid2733301[Organism:exp])
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `scope_narrower_than_taxid`, `retrieval_stale`.


## Curation record

Added 2026-10-05 from the paper's own Methods text, read out of the local PDF. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-05</b> Added 2026-10-05 from the paper's own Methods text, read out of the local PDF. Li 2010 publishes two universal PCRs rather than one, because Chordopoxvirinae splits into a low-GC group (around 25-35% GC: Orthopoxvirus, Capripoxvirus, Leporipoxvirus) and a high-GC group (around 62-64%: Parapoxvirus, Molluscipoxvirus, crocodilepox), and no single primer pair covers both. This entry is the low-GC assay; the high-GC one is PANPOX_dsDNA_highGC_RNApol_Li_2010. The forward primer sits in the insulin metalloproteinase-like protein gene and the reverse in the IMV membrane protein gene, so the product spans two adjacent genes.</p><p><b>2026-10-03</b> AMPLICON MEASURED, AND THE PAPER'S FIGURE IS APPROXIMATE: the text says 'about 220 bp'; measured with assaywatch.match against all 28,387 records in the 2026-10-03 Chordopoxvirinae archive (up to 4 mismatches per primer) it gives a product in 13,734 of them and the size is 230 bp in 13,733 of those, 228 in one. amplicon_bp is the measured 230. Both primers are near-invariant where they bind: forward exact in 13,321 and reverse in 13,727 of the 13,734. SCOPE, flagged rather than scored: the hits are monkeypox (11,906 - the archive is dominated by the 2022 outbreak), lumpy skin disease, myxoma, cowpox, variola and vaccinia, which is the low-GC half of the subfamily and exactly what the assay is for. Judged against all of Chordopoxvirinae it will look like 48% coverage; that is the design, not drift, and the same scoping decision the avipox entry is waiting on.</p><p><b>2026-10-17</b> DENOMINATOR SCOPED 2026-10-17, FROM MEASURED GC AND NOT FROM MEMORY. The pair partitions Chordopoxvirinae by GC content, so a share against the whole subfamily was never this assay's coverage - it was the design. NCBI lists 18 genera in the subfamily (an earlier hand-written list had 11 and would have silently dropped 494 records). One record of 100-400 kb was fetched per genus and its GC computed: Sciuripoxvirus 66.7%, Parapoxvirus 64.4%, Molluscipoxvirus 63.5%, Crocodylidpoxvirus 61.9% | Macropopoxvirus 53.9% | Leporipoxvirus 43.2% | Salmonpoxvirus 37.4%, Pteropopoxvirus 33.8%, Orthopoxvirus 33.0%, Mustelpoxvirus 31.3%, Avipoxvirus 30.8%, Centapoxvirus 29.5%, Suipoxvirus 27.4%, Yatapoxvirus 27.0%, Cervidpoxvirus 26.8%, Capripoxvirus 25.9%, Oryzopoxvirus 23.6%, Vespertilionpoxvirus 23.5%. That reproduces the paper's stated ~25-64% span and falls into two clusters with a clear gap. HIGH-GC = the four genera above 60%, which contains the three the earlier screen actually hit (Parapoxvirus, Molluscipoxvirus, crocodilepox) plus Sciuripoxvirus, which sits in the same band and simply had no record in that measurement. LOW-GC = the twelve below 40%. LEPORIPOXVIRUS (43.2%) AND MACROPOPOXVIRUS (53.9%) ARE IN NEITHER QUERY, 783 records: Li 2010 does not say where the crossover between its two pairs sits, and putting them in one denominator could hide a real failure while putting them in the other could invent one. They are excluded and flagged rather than assigned.</p><p><b>2026-10-31</b> THIS CHANGES RETRIEVAL, so this entry's archive and calls are stale until the group is re-retrieved and rescreened. RETRIEVAL_STALE CLEARED 2026-10-31. The flag said the numbers predated the 2026-10-17 query change. They no longer do: this group's archive has been re-fetched under the current query and holds deposits through 2026-10-27, and the verdict on this page comes from the 2026-10-31 run over that archive. The flag was self-dating and its condition is now false, so it is removed rather than carried.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=PANPOX_dsDNA_lowGC_IMV_Li_2010%3A%20&body=Entry%3A%20PANPOX_dsDNA_lowGC_IMV_Li_2010%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/PANPOX_dsDNA_lowGC_IMV_Li_2010/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/PANPOX_dsDNA_lowGC_IMV_Li_2010.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/PANPOX_dsDNA_lowGC_IMV_Li_2010.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

