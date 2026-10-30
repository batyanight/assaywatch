# Two strict-bar drift cases found — both on assays the registry does not hold

2026-10-30. The drift-case hunt's literature route (Phase 5) produced its first two cases
that clear the strict bar. Neither can become a validation row as things stand, because
neither concerns an assay in `registry/`. This records the finding and frames the decision
that follows; it does not enter anything.

## The strict bar, restated

A `mechanism: drift` case must show the *same lineage changing over time at primer or probe
binding sites* — an alignment, a substitution table, or named substitutions with collection
years. Both papers below do.

## Case 1 — Yang et al. 2014, *J Clin Microbiol* 52:76–82 (`10.1128/JCM.02467-13`)

H1N1pdm09 and H3N2 matrix-gene real-time RT-PCR losing sensitivity to accumulated
primer/probe-binding mismatches. Named substitutions, with years: G238A seen in 11–12
H1N1pdm09 isolates in **2010–2011**, accumulating with C154T (earlier), G225A, T228C through
**2012–2013**; H3N2 gains C153T, C163T, G189T over the same span. Table 1 gives the Ct
shifts; the paper prints its modified degenerate oligos. **Clears the bar.**

**But the assay is Ward et al.'s WHO M-gene assay** (ref 15: Ward CL, Dempsey MH, Ring CJ
et al.), which Yang modifies. The registry's only matrix entry,
`INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003`, is **Spackman 2002** — an avian-origin
M-gene assay, already flagged modified-in-house, with a redesigned reverse primer. Different
assay. Yang's drift observation does not attach to it.

## Case 2 — Shu et al. 2026, *J Clin Microbiol* (`10.1128/jcm.00727-26`)

The FDA-cleared CDC Human Influenza A(H3/H1pdm09) subtyping assay losing sensitivity to
reverse-primer mismatches A21G with T23G/T23C/T23A, redesigned as H3_v2. Year-resolved:
the 3C.2a1b.2a clade emerged **2020** and the mutation reached **96% of globally
circulating viruses by end of 2021** (GISAID, 2020–2023); measurable Ct shift between H3
and H3_v2; Table 1 prints both oligo sets. **Clears the bar.**

**But the registry holds no H3 subtyping assay** (only Tsukamoto 2010 H5/H7/NP and the
Spackman matrix), and the assay's primary source is the **FDA 510(k) diagnostic panel**
(080570, 2008; updated 2020/2024/2025), not a journal article with a Crossref DOI. So even
entering it collides with the rule that every entry cites its own paper through Crossref.

## What this means

The hunt worked: strict-bar drift cases exist in the literature. But a drift case is a
statement about a *registry assay*, and both of these are about assays the registry does
not carry. Turning either into a `mechanism: drift` row is **registry growth** — it needs
the design paper, oligo verification against GenBank, and a verifiable DOI — not a line
added to a case file. That affects published results and is a maintainer's scope decision,
so nothing is entered here.

Of the two, the Ward et al. matrix assay is the tractable one: a citable design paper with
a DOI. The CDC H3 subtyping assay has no DOI'd design paper, which is a harder problem than
reading one more PDF.

The PDFs are in `papers/` (`yang-2014-10.1128_JCM.02467-13.pdf`,
`shu-2026-10.1128_jcm.00727-26.pdf`), both DOIs confirmed via Crossref.
