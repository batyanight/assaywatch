# LEPTOSPIROSIS_Flagillar_filiment_Prote

<span class="aw-chip aw-chip-none">status withheld</span>

**LEPTOSPIROSIS — flagellar filament protein B (flaB) gene**

| | |
|---|---|
| Target | Leptospira ([taxid 171](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=171)) |
| Gene | flagellar filament protein B (flaB) |
| Chemistry | conventional |
| Amplicon | 120 bp |
| Designed | — |
| Paper | [10.3201/eid1909.130474](https://doi.org/10.3201/eid1909.130474) |
| Registry status | draft |

!!! quote "The paper"
    Hsu M et al. 2013. Emerg Infect Dis 19 (staged molecular analysis; MassTag panel table, Leptospira interrogans flaB Fwd/Rev)

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `GATCATGAAGCAGAGRGCGGATATG` | 25 nt |
| reverse | `CCATATCGGCGTCYCGAATTC` | 21 nt |

!!! warning "No status is reported for this assay"

    Something about this assay means a predicted-detection figure would
    mislead you — a chemistry this scoring does not model, or a readout that
    is not simply amplification. The sequences were still screened and still
    appear in the tables below that do not depend on a verdict. What is
    missing is the verdict, and it is missing on purpose rather than shown
    with a warning attached.

    - **`not_validated`**


## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).

Retrieval query:

```
(flaB[Gene] OR flagellin[Title] OR "flaB"[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `citation_is_indirect`, `oligos_modified`, `not_validated`.

