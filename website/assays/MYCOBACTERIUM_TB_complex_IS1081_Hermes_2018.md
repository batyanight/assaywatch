# Differential detection of tuberculous and non-tuberculous mycobacteria by qPCR in lavage fluids of tuberculosis-suspicious white rhinoceros

<p class="aw-byline">Hermes · PLOS ONE · 2018</p>

<p class="aw-doi"><a href="https://doi.org/10.1371/journal.pone.0207365">doi:10.1371/journal.pone.0207365</a></p>

??? quote "Full citation"
    Hermes R, Saragusty J, Moser I, Barth SA, Holtze S, Lecu A, Cracknell J, Williams D, Goeritz F, Hildebrandt TB. 2018. Differential detection of tuberculous and non-tuberculous mycobacteria by qPCR in lavage fluids of tuberculosis-suspicious white rhinoceros. PLoS One 13:e0207365

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018</span></p>

**MYCOBACTERIUM TUBERCULOSIS COMPLEX - IS1081 TaqMan**

| | |
|---|---|
| Target | Mycobacterium tuberculosis complex (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=77643">taxid 77643</a>) |
| Gene | IS1081 |
| Chemistry | hydrolysis_probe |
| Amplicon | 110 bp |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | MTC-IS1081-5F | `CTCTCGACGTTCATCGCCG` | 19 nt |
| reverse | MTC-IS1081-5Rn | `TGGCGGTAGCCGTTGCGC` | 18 nt |
| probe | MTC-IS1081-5FAM | `ATTGGACCGCTCATCGCTGCGTTC` | 24 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`citation_unresolved`** — oligos come from an uncitable source (anonymous, 2017)


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
IS1081[All Fields] NOT "whole genome shotgun"[Title]
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `target_annotation_uncertain`, `citation_unresolved`.


## Curation record

Added 2026-10-05 from the paper's S1 Table, which is a supplementary DOCX rather than anything in the PDF. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-05</b> Added 2026-10-05 from the paper's S1 Table, which is a supplementary DOCX rather than anything in the PDF. This matters, because the entry for this paper in docs/RESUME-HERE.md listed it among the 'image-only primer tables' needing a page rendered and read by eye - that is wrong. The PDF never prints the sequences at all; it says 'Sequences of the used primers and probes are listed in the S1 Table', and PLOS serves that supplement openly at journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0207365.s001&amp;type=supplementary . Reading it needed the cell line breaks preserved: the three oligos of each assay sit in ONE table cell separated by soft breaks, so a plain text dump concatenates them and the boundary between forward and reverse becomes guesswork. A first careless read of this table split the Heli pair as TTGATCAGGTCGACGATGTAGTC / ACCACCGACAAAGCGTC, which is wrong by two bases at each end; the cell breaks give TTGATCAGGTCGACGATGTAG / TCACCACCGACAAAGCGTC. Recorded because that is precisely how a fabricated sequence enters a registry. PROVENANCE: this paper did not design these oligos and does not say who did in a citable way.</p><p><b>2026-10-05</b> S1 Table's own Reference column reads 'Anonymous, 2017' for both MTC assays and 'Nieter, 2016' for the genus 16S assay, neither of which resolves to anything in the reference list; the acknowledgements thank Bernd Hoffmann, Heike Koehler and Petra Moebius 'for the development of the MTC qPCR', which reads as unpublished in-house work at FLI. oligos_designed_here is therefore false and the credited source is recorded verbatim rather than guessed at - the Nobach mistake was inventing a citation that looked right. The fourth assay in that table, IC beta-actin (ACT2-1030-F / ACT-1135-R / ACT-1081-1105-YAK, credited to Toussaint 2007), is a HOST extraction control and is deliberately not entered, for the same reason the tilapia beta-actin pair was left out: screening a host housekeeping gene against a bacterial taxon reports guaranteed non-detection as drift. MEASURED 2026-10-05 against complete mycobacterial chromosomes fetched for the purpose - one Mycobacterium tuberculosis (CM184409.1), one M. avium subsp. hominissuis (NZ_CP199875.1) and one Mycobacterium sp. (CM135953.1). The sample is small because NCBI was being shared with other work at the time and most fetches came back empty; it is enough to fix an amplicon and to show the specificity, and it is NOT enough for a coverage statistic, so no such number is claimed here. This pair gives a 110 bp product in the M. tuberculosis chromosome with both primers and the probe at zero mismatches, and no product in either non-tuberculosis mycobacterium, where the probe is absent altogether. IS1081 is a multi-copy insertion element in the complex, which is why an assay on it is sensitive; note for whoever scores this that copy number means the target is not a single locus. amplicon_bp 110 is measured; the paper states no size.</p><p>CITATION CORRECTED BEFORE THIS ENTRY WAS EVER COMMITTED, and the correction is worth keeping. The reference string was first written from memory as 'Horn F, ... Tuberculosis in rhinoceros - a case report and review of the literature', which is not this paper. scripts/check_submission.py and scripts/resolve_citations.py both rejected it on the spot - 'DOI resolves to Hermes 2018: Differential detection of tuberculous and non-tuberculous mycobacteria, which does not match the entry' - and the reference was replaced with Crossref's record. That gate exists because a reference was once invented here and went unnoticed; this is it working on a live attempt, and it is the reason nothing in this registry should be typed from recollection.</p><p><b>2026-10-07</b> SCREENED 2026-10-07 (counted by call from results/2026-10-07/calls.tsv.gz): 1,467 records, of which 1,179 are gene-level GenBank records from this entry query IS1081[All Fields] NOT "whole genome shotgun"[Title] and 288 are complete-genome assemblies (GCA_ ids) cut to candidate loci by the asm group. Calls: 1,448 detect, 19 no_amplicon. The no_amplicon rows by the exclusion column: chance_only 14, no_site 3, diverged 1, truncated 1. These are counts of calls, not a coverage statistic; the failing and non-amplifying records were not examined.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018%3A%20&body=Entry%3A%20MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/MYCOBACTERIUM_TB_complex_IS1081_Hermes_2018.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

