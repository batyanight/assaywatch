# Use of Staged Molecular Analysis to Determine Causes of Unexplained Central Nervous System Infections

<p class="aw-byline">Hsu · Emerging Infectious Diseases · 2013</p>

<p class="aw-doi"><a href="https://doi.org/10.3201/eid1909.130474">doi:10.3201/eid1909.130474</a></p>

??? quote "Full citation"
    Hsu M et al. 2013. Emerg Infect Dis 19 (staged molecular analysis; MassTag panel table, Leptospira interrogans flaB Fwd/Rev)

<p class="aw-assay-line"><span class="aw-chip aw-chip-none">status withheld</span> <span class="aw-id">LEPTOSPIROSIS_Flagillar_filiment_Prote</span></p>

**LEPTOSPIROSIS — flagellar filament protein B (flaB) gene**

| | |
|---|---|
| Target | Leptospira (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=171">taxid 171</a>) |
| Gene | flagellar filament protein B (flaB) |
| Chemistry | conventional |
| Amplicon | 120 bp |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | LeptoF | `GATCATGAAGCAGAGRGCGGATATG` | 25 nt |
| reverse | LeptoR | `CCATATCGGCGTCYCGAATTC` | 21 nt |

!!! warning "No status is reported for this assay"

    A property of this entry would render a predicted-detection figure
    misleading: a chemistry this scoring does not model, or a readout other
    than amplification. The sequences were screened and still appear in the
    tables below that do not depend on a verdict. The verdict is withheld
    deliberately, rather than presented with a caveat attached.

    - **`not_validated`**


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
(flaB[Gene] OR flagellin[Title] OR "flaB"[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `citation_is_indirect`, `oligos_modified`, `not_validated`.


## Curation record

SOURCE FOUND 2026-10-21, as the place the oligos are PRINTED and not necessarily designed. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-21</b> SOURCE FOUND 2026-10-21, as the place the oligos are PRINTED and not necessarily designed. LeptoF and LeptoR both appear verbatim in the open-access full text of PMC3810931, inside a MassTag PCR panel table that also lists Streptococcus pneumoniae plysin, Neisseria meningitidis ctrA, Mycobacterium tuberculosis pncA and Toxoplasma gondii B1 - a panel table records what a study ran, not necessarily what it designed. The table labels the target "Leptospira interrogans flaB", which independently corroborates this entry's gene. Flagged printed-not-proven-first-publication, the same treatment as Atkins/PREDICT and Lan/Quan. doi_verified stays false until scripts/resolve_citations.py approves it.</p><p><b>2026-10-24</b> SPELLING FIXED 2026-10-24 in the `name` and `target.gene` fields only: both read "Flagillar filiment Protein B gene", two misspellings of "flagellar filament". The gene is flaB, which the retrieval query already spells correctly, so nothing was ever mis-retrieved - target.gene is free text and is not screened on.</p><p>THE ENTRY ID IS DELIBERATELY NOT RENAMED, even though it carries the same misspelling: docs/validation-cases.tsv keys a scored tier-2 case on this id, and archive directories and several docs reference it, so renaming is a maintainer's change and not a spelling fix.</p><p><b>2026-10-27</b> THE TWO NOTES ABOVE WERE TWO `notes_curator` KEYS IN ONE MAPPING until 2026-10-27, so every loader kept the second and silently discarded the first: the spelling note existed in the file and in no loaded entry. Found by pre-commit's check-yaml, which only sees a file a commit touches, three days after the duplicate landed. The validator could not see it, because pydantic is handed a dict that has already lost the key.</p><p><b>2026-10-28</b> CONDITIONS CORRECTED 2026-10-28: an `annealing_c: 55.0` written by the automatic pass of 2026-10-27 is REMOVED, not replaced. Hsu 2013 prints three programmes -- a 35-cycle PCR annealing at 45 C, a first MassTag PCR of 18 cycles, and a labelling PCR of 49 cycles that starts at 25 C and moves to 55 C -- and nothing in the text attributes one of them to the flaB primer pair this entry carries. Unattributable, so unrecorded.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=LEPTOSPIROSIS_Flagillar_filiment_Prote%3A%20&body=Entry%3A%20LEPTOSPIROSIS_Flagillar_filiment_Prote%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/LEPTOSPIROSIS_Flagillar_filiment_Prote/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/LEPTOSPIROSIS_Flagillar_filiment_Prote.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/LEPTOSPIROSIS_Flagillar_filiment_Prote.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

