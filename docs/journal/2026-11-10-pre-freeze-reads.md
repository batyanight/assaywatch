# Pre-freeze reads: three curator notes, eleven sizes, the malaria nest, and a scope column that never worked

2026-11-10, on `pre-freeze-registry` off `next-release`. Release plan steps 8 (notes only),
9 and the "Sizes to read" and "nested malaria assay" items. Nothing here runs the pipeline;
every measurement is read off the 2026-11-01 calls.

## The finding that matters most: `scope_taxid` has never been honoured

The 34 drafted `scope_taxid` reads were about to land on a column that does nothing.

`scripts/retrospective.scope_verdict` matches a case row's scope against
`LineageStats.taxid`. That field is parsed in `lineage.per_lineage_stats`, and it was parsed
only out of the bare `taxid_10245` label form. `lineage.name_lineages_from_taxonomy` relabels
almost every lineage to `Name (10245)` *before* the stats are built, so on real data the field
was `None` for every lineage in every run, and every scoped row fell back to the pooled status
with `no per-lineage statistics for taxid N`. That message reads like a fact about the records
and was a fact about a label.

The assumption that made it safe was written down, which is how it was found:
`name_lineages_from_taxonomy`'s docstring said **"Nothing reads `LineageStats.taxid`"**. That
was true when the function was written and stopped being true when the case-row scope was
added on 2026-10-30. One `lineage.taxid_from_lineage_label` now answers for both label forms
and returns None for a resolver's sub-lineage (`H5N1`), which names no taxon.

## The question the roadmap asked: can a genus or subfamily taxid be honoured?

Not before today, and not only for the reason above. `per_lineage_stats` groups records by
the taxon each record is filed at, and GenBank files at species or below. A paper reporting
"gammaherpesviruses of two species" tested a subfamily, which no lineage carries. 9 of the 14
drafted rows with a taxid name a genus or subfamily.

`scope_verdict` now takes an optional `taxonomy` -- the same `drift.scope_taxonomy` cache
`scope_taxids` already uses -- and sums the lineages beneath a named clade, testing them as
one. An exact lineage still wins, being the narrower answer; a clade with no descendant among
the lineages is still skipped rather than scored on an empty sum; and with no taxonomy the old
behaviour stands. `assaywatch/taxonomy.py` says why this is a fix and not a loosening: "exact
matching is the bug this module exists to fix".

## What the 15 rows do to the matrix: nothing, and that is the useful answer

15 of the 34 drafted rows carry a taxid and are applied; 19 stay blank, by the draft's own
rule that a paper naming no single lineage leaves the row pooled. Measured against the
2026-11-01 calls, before and after:

| set | PPV of `declining` | failures caught | change |
|---|---|---|---|
| development | 4/10 = 40% (15-70%) | 7/11 = 64% (35-86%) | none |
| held-out 1 | 1/5 = 20% (2-63%) | 3/9 = 33% (10-65%) | none |
| held-out 2 | 0/4 = 0% (0-44%) | 2/3 = 67% (18-96%) | none |

Four rows now score on a named clade instead of the pooled status, and all four agree with
the pooled verdict, which is why no figure moves:

- Wellehan rounds 1 and 2 @ 2020-04-05, clade 10509 Mastadenovirus, 206 of 206 detected.
- VanDevanter rounds 1 and 2 @ 2023-10-01, clade 10293 Alphaherpesvirinae, 270 of 270 and
  238 of 273 (p = 0.077, so `works` at the 90% threshold, narrowly).

Six applied rows still skip, honestly: the EEHV1 species node 146015 has no lineage of its own
in those assays, and one assay has no lineage statistics at all.

**Pre-existing, found while doing this and not fixed here:** the development set cannot be
scored against the 2026-11-01 calls at all. `Mycoplasma_16S_unpublished` has no rows there and
no rename reaches one, and the script refuses rather than hiding it in the undecided count.
The figures above are with that one row dropped. It resolves at the frozen run or wants a
rename entry.

## The Messmer bench row is NOT applied, deliberately

The draft conditions itself on reopening a decision: a `works` row for
`Chlamydia_16S_Messmer_1997_round1` would score `undecided` at its 1997 `as_of` (about seven
*C. trachomatis* records before that date) and `docs/validation-cases.tsv` is the development
set, FROZEN 2026-10-23. The roadmap's own decisions table says "no validation row" for this
case. Reopening a frozen set is the maintainer's call, so the draft stays in `local/`.

## Three curator notes the papers contradict

- **Lozano 1997, both entries.** The note said the paper "amplified LCM WE, Lassa Nigeria and
  Josiah, Mopeia, Pichinde, Tacaribe, Junin MC2 and XJ, Oliveros and Pampa". That list is
  Fig. 2, a HinfI pattern *calculated* from published sequence for "those arenaviruses for
  which the S RNA sequence is available". ARS1/ARS16V amplified four viruses (Fig. 3a, lanes
  J, L, T and P: Junin MC2, LCM WE, Tacaribe, Pampa); ARS6C/ARS3V amplified three, "the whole
  S RNA of Junin, LCM and Tacaribe virus (not shown)". Pichinde is cultured in section 2.2 and
  is in no amplification figure. The scope decision is unaffected: it was taken from the range
  the paper claims, not the panel it ran.
- **Li 2010 IMV.** The note said "Li 2010 does not say where the crossover between its two
  pairs sits". For Leporipoxvirus it does: Table 1 files myxoma Lausanne (43.6%) and rabbit
  fibroma Kasza (39.5%) under its own heading "Low GC", the low-GC primers were "selected based
  on the genome sequence alignment results obtained with strains of low-GC content poxviruses
  (Table 1)", the validation panel carried both, and both amplified. Table 1's high-GC side is
  three taxa only (Molluscipoxvirus, Parapoxvirus, crocodilepox), so nothing competes for it.
  Macropopoxvirus keeps the old wording: it is in no part of Table 1. The query change is a new
  retrieval group and stays on `next-run-prep`.

## The nested malaria assay: `Plasmodium_18S_Li_1995` is not a nest

Read page by page. One 30-cycle round, the cDNA primed with the antisense primer and amplified
once. Table I's eleven oligos are one pair plus probes: 841/844 (this entry), 842 (genus,
internal), 741 and 743 (*P. vivax* A- and S-gene), and 933-936 (four species), every one of the
last nine used on Southern transfers of the one gel, never as primers. 566/570 is genuinely
outside 841/844 on the gene, which is what made the question reasonable, but the paper uses it
as an ALTERNATIVE for cloning: "For the purpose of species identification and taxonomy,
however, shorter regions of sequence are sufficient. The genus-conserved primer pair 841-844
was selected for the work described here." `nested_family` and `nested_round` stay null.

Two findings for the maintainer, both needing a rescreen and so not acted on:

1. **An unstored probe.** Oligo 842, `TAACACAAGGAAGTTTAAGGC`, genus-conserved and between the
   primers: the pair "includes an internal genus-conserved sequence located between V7 and V8
   which can serve to confirm the identification of the sequence as Plasmodium-related". Same
   shape as the Francisella tul4 FT443 item.
2. **The product length varies by design.** 719 products over 59 lengths, 280-466 bp, median
   374 (the stored scalar), mode 284. The pair was chosen because it "covers the two most
   variable regions (V7 and V8)". `amplicon_bp_range` may be the right shape; it changes which
   records are evaluable, so the scalar stands. The flags are corrected either way: the paper
   does publish "about 400 bp", so `amplicon_measured_not_published` was wrong and is now
   `amplicon_disagrees_with_paper` plus `amplicon_multimodal`.

## Eleven sizes, one rule, ten settled

`amplicon_bp` takes the measured mode where one dominates and the measured median where none
does; the flag says whether the CITED paper publishes a size; and a value only moves where the
new +/-25% window still admits every product measured, so a correction cannot silently delete
calls.

| entry | stored | now | measured | paper |
|---|---|---|---|---|
| Mueller 1F | 567 | **552** | 552 in 511 of 512 | no size printed |
| Mueller 2F | 570 | **560** | 560 in 1,949 of 1,959 | no size printed |
| Mueller 3F | 563 | **544** | 544 in 1,872 of 1,885 | no size printed |
| Bourhy round 1 | 460 | **462** | 462 in 5,044 of 7,027 | "a 456-462 nucleotide region" |
| Bourhy round 2 | 260 | **249** | 249 in 5,023 of 7,165 | none for this pair |
| Garner | 350 | **391** | mode 391 of 4,475, median 394 | "approximately 350-basepair" |
| Tsukamoto H5 | 261 | **258** | 258 in 29,731 of 35,830 | 249 (Table 1) |
| Spackman | 100 | **101** | 101 in all 92,224 | no size printed |
| Briese L | 630 | **584** | median 584 of 158, mode 505 | positions, not sizes |
| Briese BUN_S5_F | 961 | **948** | mode 948 of 87, median 950 | positions, not sizes |
| Briese BUN_M_IXf | 335 | *unchanged* | mode 283 of 531, truncated | positions, not sizes |

Three of these need a word.

- **Bourhy round 1 gets no disagreement flag**, because 462 is inside the range the paper
  prints. The stored 460 was the single figure protocol P-016 carries.
- **Bourhy round 2 drops three products** of 7,165, at 314 bp (two) and 317 bp (one), all three
  already `fail`, so they read `no_amplicon` after the frozen run. That is the one call move in
  the table and it is deliberate. The paper publishes no size for this pair: it does not print
  PVOnstF at all, and its own internal PVO5/PVO6 pair, which "amplified a 317 nucleotide
  region", is a sequencing pair this entry does not use.
- **Briese L takes the median 584, not the modal 505** the verifier's table noted. A 505
  declaration would window 379-631 bp and drop the 641 and 642 bp products that are measured
  and real; 584 windows 438-730 and admits all 158.

**Briese BUN_M_IXf could not be settled.** Its products run 251-417 bp against a 251-418 bp
window -- hard against both edges -- so the window is clipping a pan-genus segment continuum by
an unknown amount, and the modal 283 is measured through the very constraint in question. Its
`M3560_F` and `BUNS_5_U_6` siblings carry `amplicon_bp_range` for exactly this reason and were
settled on 2026-10-21 by rescreening with the size window opened. This one needs the same.
`amplicon_bp` stays 335 and the entry now carries `amplicon_multimodal` saying so.

## Gates

`pytest` 2,206 passed, `pytest -m slow` 12 passed, `assaywatch validate registry` 216 valid /
0 problems, `ruff check`, `ruff format --check`, `check_citations` 216 / 0 problems,
`claims.py --check`.
