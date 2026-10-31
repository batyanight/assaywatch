# M1: identity-aware 3'-window penalty, mechanism in and measured, shipped off (2026-10-21)

The first proposal from `docs/journal/2026-10-20-pipeline-audit.md`. The scorer weights a
mismatch by its distance from the 3' end but is blind to which bases mispair, and
Kwok et al. 1990 (doi:10.1093/nar/18.4.999) and Stadhouders et al. 2010
(doi:10.2353/jmoldx.2010.090035) both find the 3'-region effect is dominated by
identity: A:G, G:A, C:C (~100-fold) and A:A (~20-fold) suppress yield, while T:G,
G:T, T:C and T:T are nearly free, a wobble still stacking.

## What was built

`scoring.mispair_penalty`, a table of `"{primer base}:{template base}" -> multiplier`
read by `score.score_primer` (`assaywatch/score.py`). At each definite mismatch the
position penalty is multiplied by the table value for the mispair that forms; the
template base is the complement of the record base, since `Site.window` reads the
record in the oligo's own orientation (`score.mispair_multiplier`). Only unambiguous
A/C/G/T mispairs are looked up — a degenerate primer base or an ambiguity code in the
record names no single mispair and keeps the full penalty. A multiplier of 0 also
exempts a 3'-terminal mismatch from `terminal_mismatch_fails`, or the discount would
be defeated at the one position it matters most.

**Shipped empty**, exactly like `by_chemistry: {}`. An empty table returns 1.0 for
every mispair, so the default output is byte-identical to the code before M1 — the
whole 1298-test suite passes unchanged, and six new tests in `tests/test_score.py`
pin the mechanism (empty = position penalty + terminal set; a zeroed mispair = no
penalty + terminal exempt; a partial multiplier scales but keeps terminal; an
unlisted mispair unaffected; degenerate/ambiguous skipped; per-chemistry override
validates). It is also a recognised `by_chemistry` key for free, because
`check_chemistry_overrides` derives its key set from the base scoring block.

## Measured candidate: discount the G:T/T:G wobble to 0

Scored all five bench panels under the current config and under
`mispair_penalty: {"G:T": 0.0, "T:G": 0.0}` (`scripts/bench_panel.py --config`):

| panel | assay | current | G:T/T:G = 0 | change |
|---|---|---|---|---|
| Forslund FAP | `PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999` | 14 band-`fail` | **9** | 5 false fails rescued (detect 25 -> 30) |
| Barrett | `Morbillivirus_including_CDV_P_gene_Barrett_2003` | 3 band-`fail` | **0** | all 3 rescued (detect 2 -> 4) |
| Meyer ATI | `ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997` | 1 band-`fail` | 1 | unchanged — skunkpox has no 3'-window mismatch |
| Rebelo | `Pan_mycoplasma_16S_23S_intergenic_space_Rebelo_2011` | 0 fails | 0 | unchanged — no G:T anywhere |
| Rahn | `Salmonella_invA_Rahn_1992` | 3 no_band-`fail` | 3 | **unchanged — zero specificity cost** |

This is exactly what the audit predicted from the panels and from Kwok. **Eight
documented false fails rescued** (5 FAP + 3 Barrett), and **zero** of Rahn's 41 bench
negatives moved toward a false detect — the three chance pairings stay `fail` (one
drops 13.5 -> 12 from an out-of-3'-window G:T but stays an order of magnitude above
`reduced_max`). Meyer and Rebelo are untouched, which is the right null: neither has a
G:T mispair in play, so a correct mechanism must leave them alone.

## What remains before the value can ship

**The tier-2 gate requires a full re-screen, and has not run.** `retrospective.py`
reads the pre-scored `call` column from `calls.tsv.gz`; scoring happens at screen
time, so the candidate's effect on the 50 validation cases cannot be measured without
re-screening every archive under the candidate config (the `screen` pass, ~25 min, not
retrieval). Per the project's own rule — a candidate that loses a documented catch is
a bad candidate — `mispair_penalty` stays `{}` until that run shows no documented
catch is lost. The bench panels are necessary evidence that the mechanism is right and
G:T is the correct first knob; they are not the whole gate.

To ship it:

1. Re-screen under `mispair_penalty: {"G:T": 0.0, "T:G": 0.0}`
   (`caffeinate -i snakemake --cores 4 --config email=...` with the candidate in
   `config.yaml`, or a scratch config).
2. `python scripts/retrospective.py --cases docs/validation-cases.tsv` against the new
   calls table; confirm caught failures do not fall and no `works`/`partial` case
   newly disagrees.
3. If clean, set the value in `config.yaml` with the tier-2 numbers in the comment,
   the way `docs/journal/2026-10-19-conventional-override-validation.md` documents for the
   reverted conventional override.

One mispair at a time after that — the next candidates with literature behind them are
the strong suppressors (A:G, G:A, C:C, A:A), which would be penalty *increases*, not
discounts, and need their own panels.
