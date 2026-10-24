# Hunting papers for the undocumented PREDICT-panel primers (2026-10-21)

Prompted by two decisions: ordering status is the lab's workflow and does not belong in
the pipeline, and **an oligo's name should come from the paper that published it**, not
from whether it needs ordering. `NEED_TO_ORDER` is gone from the registry, from
the seed-list importer (since removed) and from `scripts/materials_needed.py`; two display names and two
assay ids that carried a truncated `_ne_` from it were cleaned up too.

That left the real question: which of the PREDICT-derived entries have no paper, and can
one be found?

## The panel is in better shape than the audit implied

`docs/2026-10-20-pipeline-audit.md` framed this as "35 entries rest on a supplement that
is not on disk". Measured properly, of **49 PREDICT-derived entries**:

| | |
|---:|---|
| 45 | already carry a DOI |
| 41 | carry a DOI **and** have the paper on disk |
| 4 | had no DOI at all |

So the supplement matters for *transcription provenance* — it is where the sequences were
read from — but it is not the only citation for most of the panel. The hunt was the 4
without a DOI, plus 9 related orphans with no DOI and no reference.

## Method

Europe PMC full-text search on **both** the oligo name and the sequence, each sequence
also searched as its reverse complement (52 searches). A hit was then **confirmed against
the paper itself** — the local PDF where one exists, the open-access full text otherwise,
with whitespace flattened so a sequence broken across lines still matches. A search hit
alone was never treated as a source: the first pass returned papers that merely *use*
these primers, which is the trap.

## Resolved, four entries

All four verified against Crossref by `scripts/resolve_citations.py`.

| entry | source | how it was confirmed |
|---|---|---|
| `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme` | **Watanabe et al. 2010**, Emerg Infect Dis 16:1217-1223, `10.3201/eid1608.100208` | `CoV-FWD3`/`CoV-RVS3` are Watanabe's pan-CoV RdRp pair with 4 degenerate substitutions each, and **every one is an IUPAC superset** of Watanabe's base at that position (checked with `assaywatch.iupac`) |
| `RETROVIRUS_RNA_polymerase_SIV_3` | **Takehisa et al. 2009**, J Virol 83:1635-1648, `10.1128/JVI.02311-08` | all **four** Hahn primers are in the local PDF; `HahnF1`/`HahnR1` here are the outer round of the same nested *pol* assay as the sibling entry's `HahnF2`/`HahnR2` |
| `HANTAVIRUS_ssRNA_S_segment` | **Anthony et al. 2013**, mBio 4:e00598-13, `10.1128/mbio.00598-13` | `UHantaF1`/`UHantaR1` both in the open-access full text (PMC3760253) |
| `LEPTOSPIROSIS_Flagillar_filiment_Prote` | **Hsu et al. 2013**, Emerg Infect Dis 19, `10.3201/eid1909.130474` | `LeptoF`/`LeptoR` verbatim in the open-access full text (PMC3810931), **inside a MassTag panel table** — flagged `CITED_PAPER_IS_WHERE_THE_OLIGOS_ARE_PRINTED_NOT_PROVEN_FIRST_PUBLICATION` |

Two of these were worth the trouble beyond the citation:

- **The coronavirus entry was not a Quan round.** It sits in a group whose siblings cite
  Quan 2010, and the local Quan PDF prints `AAYBTVCCWYTICARBTRGG`,
  `GGCWCCWCCHGGNGARCAATT` and `GGWAWCCCCAYTGYTGWAYRTC` — none of them this pair. It is a
  *third* assay, from a different paper, and the "increased degeneracy" modification is
  the same thing PREDICT did to Bourhy's rhabdovirus primers. The lead came from a search
  hit titled "Comparative Analysis of **Quan and Watanabe** Pan-Coronavirus Assays".
- **The Leptospira primers sit in a panel table**, among *S. pneumoniae* plysin,
  *N. meningitidis* ctrA, *M. tuberculosis* pncA and *T. gondii* B1. A panel table records
  what a study ran, not what it designed, so this is where the oligos are *printed* and
  not necessarily first published — the Atkins/PREDICT and Lan/Quan pattern again. The
  table does independently corroborate the gene as *flaB*.

**One self-caught error worth recording:** the first attempt named the Leptospira first
author as Kuroda, from memory. `resolve_citations.py` refused it — Crossref says **Hsu** —
which is exactly what the "no citation from memory" rule exists to catch.

## Needs more information — eight entries, for Batya to go over

No paper could be confirmed for these. Each row says what was searched and what came
back, so none of it has to be redone.

| entry | oligos | what the search found |
|---|---|---|
| `HANTAVIRUS_ssRNA_S_segment_2` | `UHantaF3`/`UHantaR3` | **nothing at all** — no hit on either name or sequence, and both absent from Anthony 2013's main text |
| `HANTAVIRUS_ssRNA_S_segment_round2` | `UHantaF2`/`UHantaR2` | only a *user*: Blasdell 2021, PLOS ONE `10.1371/journal.pone.0248244`. Absent from Anthony 2013's main text |
| `HANTAVIRUS_ssRNA_S_segment_round2_2` | `UHantaF4`/`UHantaR3` | **nothing at all** |
| `Nipah_N_gene` | `NP1F`/`NP1R` | nothing for either sequence; the name hits are noise (`NP1F` matched a physics DOI) |
| `Nipah_N_gene_2` | `NP2F`/`NP2R` | **both sequences** hit Wong et al. 2003, *A Golden Hamster Model for Human Acute Nipah Virus Infection*, Am J Pathol, `10.1016/S0002-9440(10)63569-9`. **Unconfirmed** — PMC returned an empty body for PMC1892425, so the full text could not be checked. The entry currently cites Chua 2000 Science, so this is a possible mis-citation worth resolving |
| `ENTEROVIRUS_ssRNA_5_UTR_VP4_VP2_round1` | `EVRV1`/`EVRV2` | only users: Bai 2016 EcoHealth `10.1007/s10393-016-1183-z` (a PREDICT-adjacent *Desmodus* survey) plus several rhinovirus papers. `EVRV` suggests an enterovirus/rhinovirus consensus set |
| `ENTEROVIRUS_ssRNA_5_UTR_VP4_VP2_round2` | `EVRV3`/`EVRV2a-new` | same users; `-new` in the name suggests an in-house revision |
| `Pan_mycoplasma_16S_23S_intergenic_space_2` | `16-23-F2`/`16-23-R2` | **nothing** on either sequence; the name hits are noise |

### The single most useful thing to supply

**The Anthony et al. 2015 PREDICT supplement** (Nat Commun 6:8147, Supplementary Methods,
CC-BY) — and, newly, **the Anthony et al. 2013 mBio supplement** (PMC3760253). The 2013
main text carries `UHantaF1`/`R1` but none of the nested or alternate rounds, which is
exactly the pattern of a nested set whose inner primers live in a supplementary table.
Three of the nine unresolved entries are UHanta rounds, so one supplement plausibly
closes them.

### RESOLVED since: the TINC qPCR, and what it says about the method

`Tortoise_intranuclear_coccidia_18SrDNA` returned **nothing** on all three sequences and
both primer names in either orientation. Batya supplied the PDF the same day, and it is
the design paper: **Alvarez et al. 2013**, *Development of a quantitative PCR for rapid
and sensitive diagnosis of an intranuclear coccidian parasite in Testudines (TINC)*,
Vet Parasitol 193:66-70, `10.1016/j.vetpar.2012.11.029`. All three oligos verified
verbatim; the names in the registry are the paper's own.

**That is the method's limit, stated plainly: a no-hit is not evidence an assay is
unpublished.** *Veterinary Parasitology* is Elsevier and not in the open-access full-text
index this search reads, so no number of queries would ever have found it. Every
remaining "nothing at all" row below should be read as "not in the OA index", and the
only way to close one is a human with a PDF.

Reading the paper also forced two corrections nothing else would have caught: the probe
carries a **Black Hole Quencher**, not a minor-groove binder, so `chemistry` moved from
`mgb` to `hydrolysis_probe` and `quencher` from `MGB-NFQ` to `BHQ`. No call changes today
(`by_chemistry: {}`), but the chemistry field is what a per-chemistry calibration would
key on, and the registry's chemistry counts are printed in every run.

### One that may not have a paper at all

`Pan_mycoplasma_16S_23S_intergenic_space_2` returned nothing on either name or sequence,
in either orientation. Given the TINC result, that is most likely a paywalled or
non-indexed journal rather than an unpublished assay — but it could be either, and only a
PDF or a lab note settles it.
