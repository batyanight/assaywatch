# Preparing two influenza assays so their drift cases have somewhere to land

2026-10-30, following the maintainer's "pursue both" on the two strict-bar drift cases
(`docs/journal/2026-10-30-two-strict-bar-drift-cases.md`). Each case needs its assay in
the registry first. This records how far each got and what each still needs. Nothing is
entered into `registry/` or `pending/` here — entering an assay affects published results
and goes through the curate chain under review.

## Ward matrix assay — in hand, ready to build

Yang 2014's drift observation is about the influenza A M1 assay of **Ward et al. 2004,
*J Clin Virol* 29:179–188, `10.1016/S1386-6532(03)00122-7`** (DOI confirmed via Crossref).
The paper is **open access** (PMC7128145, Elsevier COVID collection) and is saved to
`papers/ward-2004-10.1016_S1386-6532(03)00122-7.pmc.xml`.

Oligos read verbatim from the paper's text (the 104 bp M1 assay, not the separate RT
primer, and not the influenza B pair):

| role | sequence (5′→3′) | nt |
|---|---|---|
| forward (senseA) | `AAGACCAATCCTGTCACCTCTGA` | 23 |
| reverse (antisenseA) | `CAAAGCGTCTACGCTGCAGTCC` | 22 |
| probe (FAM/TAMRA) | `TTTGTGTTCACGCTCACCGT` | 20 |

Paper states a 104 bp product in the M1 gene; target is influenza A (taxid 11320).

**Still owed before it is live**, all on the curate path:
- `assaywatch curate` to verify the DOI through Crossref and set `doi_verified: true`.
- Oligos verified present in real GenBank M-segment records, and `amplicon_bp` MEASURED
  from where the primers sit (the paper's 104 bp is a claim; the registry takes the
  measured value and discloses any disagreement).
- Confirm it is distinct from the existing `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003`
  (Spackman 2002) — it is: different primers, different design paper.
- Then Yang 2014 becomes its `mechanism: drift` case: C154T/G225A/T228C/G238A accumulating
  in the H1N1pdm09 primer-binding regions across 2010–2013.

## CDC H3 subtyping assay — blocked on a citation ruling

Shu 2026's drift observation is about the FDA-cleared **CDC Human Influenza A(H3/H1pdm09)
Subtyping assay**. Crossref has **no journal paper** for the original assay; its formal
source is the FDA 510(k) panel (080570, 2008; refreshed 2020/2024/2025). Shu 2026 Table 1
prints the H3 (v1) and H3_v2 oligos, so the sequences are obtainable, but the registry's
rule is that every entry cites its own paper through Crossref, and an FDA 510(k) has no
Crossref DOI.

**Decision owed from the maintainer**: may an assay be entered citing an FDA 510(k) panel
(or citing Shu 2026 itself, which prints the oligos and has a DOI), or is a DOI'd design
paper required — in which case this assay cannot be entered and Shu 2026's drift case
cannot land? Until that is settled, the H3 assay is not built.
