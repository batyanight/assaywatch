# The Candrian seam, worked: 59 papers, zero held-out rows, one verified oligo

`docs/2026-10-24-heldout-candidates.md` left `E_coli_malB_Candrian_1991` as "the rich seam":
its forward primer returns **59 Europe PMC full texts**, far more than any other registry
oligo, and the doc judged them "mostly prevalence surveys, `works`-shaped rather than
drift-shaped, and a pass of its own". This is that pass.

**The judgement was right and the seam is now closed. Zero of the 59 clear the held-out bar.**
That is the headline, and it is a result rather than a failure to find one: the richest
remaining lead in the held-out search yields nothing, which is information about where the
set's drift shortfall can and cannot be closed.

## What the 59 are

Confirmed the hit count independently (`"GACCTCGGTTTAGTTCACAGA"`, Europe PMC REST, 59 of 59
returned). By publication year: 44 are 2018 or later, and the distribution is dominated by one
genre — **antimicrobial-resistance prevalence surveys**, with E. coli isolated from poultry,
raw milk, retail meat, seafood, well water, migratory birds, pet birds, dairy cattle and
garden soil. The primer appears in them as a species-confirmation step on the way to an AMR
result. That is the `works`-shaped use the earlier doc predicted.

## Why none qualifies

The bar in `docs/validation-cases-heldout.tsv` is a paper, erratum or redesign reporting how an
assay **already in the registry** performed, with `as_of` no later than the sequences its
authors could have seen. A survey that uses the primers and reports a prevalence reports
nothing about the assay. Five titles looked like they might clear it; all five were read.

| # | paper | why not |
|---|---|---|
| 20 | Novel multiplex-PCR test for *E. coli* detection (2024, `10.1128/spectrum.03773-23`) | A **new** assay on `cydA`/`lacY`/`ydiV`, validated in silico over 47,370 genomes. Impressive, and explicitly out of bounds: a new assay's validation against its own panel says nothing about drift in an existing one. |
| 56 | PCR versus hybridization for EHEC virulence genes (2007, `10.3201/eid1308.060428`) | The closest call; see below. |
| 23 | WGS reveals environmental pathogen misidentification (2026, `10.1186/s12917-025-05280-z`) | The misidentification is of *Stutzerimonas stutzeri* by conventional microbiology, not by any registry assay. E. coli is a control. |
| 5 | NRPS genome amplification by rolling circle (2024, `10.3390/ijms25105089`) | E. coli is the **non-target** in a *Pseudomonas* enrichment. The primer hit is incidental. |
| 59 | PCR detection of predominant anaerobic bacteria in feces (1996, `10.1128/aem.62.4.1242-1247.1996`) | Reports titres for its own 16S assays for 12 anaerobes. Nothing about malB. |

A sweep of all 59 titles and abstracts for failure language (`failed`, `false-negative`,
`did not detect`, `no amplification`, `missed`, `mismatch`, `underestimat`, `redesign`, …)
returned 6, and the other four are treatment or organ failure and microbiota
under-quantification, not assay failure.

### The one that came closest, and the two reasons it does not count

Gerber et al. 2007 (`10.3201/eid1308.060428`) compares PCR against DNA-DNA hybridization over
40 EHEC isolates and finds **PCR did not detect 4%–20% of hybridizable plasmid genes** —
`hlyA`, `katP`, `espP`, `toxB`, ORF1, ORF2. A published report of PCR missing true positives
is exactly the shape the held-out set wants, and the registry does hold an `hlyA` assay
(`E_coli_O157_hlyA_Wang_1997`). It still fails, for two independent reasons:

1. **Different `hlyA` assay.** Its primers are `HlyA1F`/`HlyA1R`
   (`GGTGCAGCAGAAAAAGTTGTAG` / `TCTCGCCTGATAGTGTTTGGTA`), a **1551 bp** product credited to
   its reference 13. The registry's entry is Wang 1997's `O157-3`/`O157-4`
   (`GTAGGGAAGCGAACAGAG` / `AAGCTCCGTGTGCCTGAA`), **361 bp**. Nothing connects the two beyond
   the target gene.
2. **It reports no malB result at all.** `malB` occurs in this paper exactly once, in the
   primer table. It is an unreported internal species control — no detection rate, no failure,
   nothing to score.

## What the pass did find: Eco1 is independently transcribed

Worth more than the empty result. Gerber 2007's Table prints

    MalBU   GACCTCGGTTTAGTTCACAGA   MalB promoter (414)   This study

and `MalBU` is **byte-identical to the registry's stored `Eco1` forward**. So the registry's
forward primer now has a second, independent printed source, which matters because
`10.1016/0168-1605(91)90148-I` (Candrian 1991) is paywalled and still on the still-needed
list — the stored sequence has never been checked against its own design paper. One of its two
oligos is now confirmed against a source we hold.

Two cautions attached to that, both of which keep this out of the registry as evidence:

- **The reverse is not confirmed.** Gerber pairs the same forward with `MalBDn`
  (`AGCGCGTAGGACTGAAACACCATA`) for a **414 bp** product, against the registry's `Eco-2`
  (`CACACGCTGACGCTGACCA`) and **585 bp**. This is a redesign sharing a forward, not the
  registry's assay, so it says nothing about `Eco-2` or about `amplicon_bp`.
- **It is attributed to "This study", not to Candrian.** The paper claims the primer as its
  own. Either it is an independent design that landed on the same 21-mer, or the attribution
  is simply wrong. Either way it is a transcription of the same sequence by people who were
  not copying Candrian's table, which is what makes it useful as a check — but it is not a
  citation chain, and Candrian 1991 is still the paper the entry needs.

**Nothing was changed in the registry.** The confirmation is recorded here and the entry's
`needs_review` is untouched: its one flag is `orientation_inferred`, which this does not
address — Gerber's `MalBU` is a forward too, so orientation remains inferred from two sources
that agree with each other.

## What this closes

The seam is spent. `E_coli_malB_Candrian_1991`'s forward was the last unexplored high-yield
oligo in `docs/2026-10-24-heldout-candidates.md`, and the remaining searchable registry oligos
there returned 0 (apicoplast 23S, Yersinia, the Reid capsid) or cannot be searched literally
(the circovirus primers, all degenerate). **Adding held-out rows by literal oligo search over
Europe PMC has reached its limit**; the set stands at 34 rows with its drift shortfall intact,
and closing that gap needs a different instrument than this one — the scoring-strategy plan's
replay harness, or the lab leads in `docs/2026-10-06-lab-leads.md`.
