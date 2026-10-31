# Handoff: DFA correction, and five bugs in the oligo checker

Written 2026-10-05 ~04:50 UTC from a Cowork session working read-mostly over the
desktop bridge, while a parallel Claude Code session had the repo open. Written as
a file because the two sessions cannot message each other.

## State of the working tree when this was written

One uncommitted change, made on Batya's explicit instruction:

- `registry/Pan_HERPES_dsDNA_Polymerase.yaml` — `HV-DFA` truncated from
  `GAYTTYGCNAGYYTNTAYCCR` (21 nt) to VanDevanter's printed `GAYTTYGCNAGYYTNTAYCC`
  (20 nt). `citation.oligos_designed_here: true` added. Full rationale in that
  entry's `source.notes_curator`. `needs_review` gains
  `DFA_VARIANT_VS_PREDICT_UNRESOLVED`.

Gates run after the edit: `assaywatch.validate registry` -> 151 valid, 0 problems.
`pytest -q` -> 744 passed, 2 skipped. Degeneracy pool for the assay halves,
131072 -> 65536, tier unchanged (`severe`).

Not done, and it should be: the entry has not been re-screened both ways, so the
effect of the correction on predicted detection is unmeasured. The 3' `R` excluded
C and T at the position that governs extension, so it charged a terminal mismatch
to every record with a pyrimidine there. For a family as divergent as
Herpesviridae that plausibly suppressed detection broadly. Do not read a coverage
number for this assay until it is re-screened.

Open provenance question: `citation.as_written` is `PREDICT Protocols`, so the
sequence came through PREDICT, not from the paper. If the PREDICT protocol prints
DFA with the `R`, this entry should hold the 21-mer and declare the modification
the way `Pan_mycoplasma_16S_All_Van_1992` records `GPO-1FMod` — the registry records the oligo as used. That document is not in `papers/`.

## The verification run's numbers are not trustworthy yet

`results/oligo-verification-2026-10-05.tsv` reports 65 of 133 agreeing (49%).
That rate is an undercount: the checker is wrong more often than the registry is.
Five distinct defects, in rough order of how many verdicts they move.

### 1. The paper-matching fallback matches the wrong paper (19 of the 52 `absent`)

`local_paper()` falls through from DOI lookup to a scan for first-author surname
plus design year in the first ~9000 characters. A paper that *cites* another paper
matches it. Confirmed wrong pairings in this run:

| assay | cited DOI | PDF actually used |
|---|---|---|
| `CHYTRID_Bd_..._Boyle_2004` (3 oligos) | 10.3354/dao060141 | Ghosh 2020, `10.1111_1755-0998.13299.pdf` |
| 6x `ORTHOBUNYAVIRUS_*` (12) | 10.1007/s00705-007-1069-z | Zhai filovirus, `10.1128_Jcm.01893-06.pdf` |
| `MYCOPLASMA_16S_Turtles_only_Feldman_2006` (2) | 10.7589/0090-3558-42.2.279 | same filovirus PDF |
| `CALICIVIRUS_ssRNA_Capsid` (2) | 10.1016/S0166-0934(99)00088-9 | Latimer elephant herpes, `10.1016_j.vetmic.2010.05.042.pdf` |
| `Pan_coccidia_SSU_rDNA_..._Garner_2006` (2) | 10.1354/vp.43-3-311 | same elephant herpes PDF |

Every `absent` for these is meaningless. Fix: never fall back past the DOI, or
require the surname-plus-year hit to come with a DOI that is absent from the PDF
rather than present-and-different. Detection of the bug is cheap and belongs in
the tool: compare `checked_against`'s filename stem to the slugged DOI and refuse
the pairing when they differ.

### 2. Inosine printed as a parenthesised notation (8 oligos)

`deinosine()` maps a bare `I` to `N`, which handles papers that print `I` inline.
Prepens 2007 Table 3 prints `(N/I)` — and lowercase `[n/i]` in the adjacent block.
All four CM-gB oligos (`2743s`, `2744s`, `2745as`, `2746as`) match the registry
exactly once that notation collapses, and were reported `absent`.

### 3. Oligos broken across a line or column break (5+ oligos)

Pre-2000 two-column PDFs hyphenate sequences across lines. VanDevanter prints DFA
as `GAYT` / `TYGCNAGYYTNTAYCC-39` on consecutive lines, so the scanner sees two
fragments and neither contains the stored oligo — hence `absent` on what is a
one-base difference. Same cause for the four adenovirus pan-polymerase oligos
reported `in-text`: Wellehan's `polRouter` splits as `...RTABARNG` / `MRTT`.
Fix: dehyphenate-and-rejoin the extracted text before scanning. Until it lands,
`absent` on an old PDF means "not found", not "not in the paper".

### 4. `in-text` is often a false alarm from running-text primer lists

Papers that list primers in Methods prose rather than a table produce `in-text`
for oligos that are genuinely the paper's. Verified exact, by eye, against the
printed sequence: all four adenovirus pan-polymerase oligos, `Astr4380F`,
`Astr4722R`, `CoV-FWD1`, `CoV-RVS2`, `FS 778-Zino-hemi-fwd`, `WN-1333`,
`WN-1494c`. The `printed` oligo-run extractor needs to pick up sequences
introduced by `primer <name> (5'-...-3')` in prose, not only table cells.

### 5. Verified wrong citations, not sequence errors

These survive all four fixes above and are registry problems, not tool problems:

- `ASTROVIRUS_*` `AstroFWD1`-`AstroFWD4` are **not in the cited paper**. That
  paper lists `Astr4380F`, `Astr4574F`, `Astr4811F/R`, `Astr5159F`, `Astr5819R`,
  `Astr4722R`. The four `AstroFWD` oligos come from somewhere else.
- `CoV-RVS1(L1150)`: paper prints `...GCNACNACATG`, registry has `...GCNACATG` —
  registry is 3 nt short at the 3' end. Real discrepancy, in the worst place.
- `FILOVIRUS_ssRNA_L_gene_2` `MOD-FWD`/`MOD-RVS` are degenerate consensus
  collapses of Zhai 2007's four discrete primer sets (`Greene-Filo-U12683-A..D` /
  `L13294-A..D`). A legitimate modification, but it is undeclared; characterise it
  the way `GPO-1FMod` is.
- `CMV_..._gB` `4007-s/as` and `4125-s/as` are not in Prepens 2007 at all.
- `RETROVIRUS_RNA_polymerase_SIV` `PTS-pol-*` (4) and
  `CRYPTOSPORIDIA_..._2000` `Ziao18S*` (3) find nothing resembling a match in
  their cited papers. Provenance question, not a base to correct.

## Suggested order

1. Fix defects 1-3 and re-run; they are mechanical and they move the headline.
2. Re-run before touching any registry YAML — several `absent` entries will
   resolve themselves and editing first risks "correcting" a correct sequence.
3. Then work the residue in section 5 as provenance, with
   `scripts/audit_provenance.py`.
4. Re-screen `Pan_HERPES_dsDNA_Polymerase` both ways to quantify the DFA change.
