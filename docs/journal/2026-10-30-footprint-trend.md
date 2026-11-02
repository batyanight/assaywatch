# The trend test counted clones as evidence: 35 of 64 significant declines do not survive counting each footprint once

2026-10-30, built as decided the same evening (`2026-10-30-design-grilled.md` Q4). The
Cochran-Armitage trend over deposit year assumes independent observations. Records are not
independent: one outbreak sequenced five hundred times contributes five hundred identical
rows, and the test reads them as five hundred pieces of evidence. The duplication check
already corrects the recent-window interval for this; the trend had no such correction.

## What was built

A second trend, over distinct footprints per year. `YearStats` gains the set of distinct
`(call, footprint)` classes it saw, `AssayDrift.trend_by_footprint` runs the same
Cochran-Armitage statistic over those counts, and `trend.describe` prints both clauses with
the framing they deserve. Neither feeds the verdict; the house rule is unchanged.

The per-year footprint sets are cleared for the whole assay if any evaluable row lacks a
footprint, the same all-or-nothing rule `_tally_window` already applies to the window
counts: a partial count is a lower bound on distinct footprints, and a trend over lower
bounds is not a trend.

## What it says on the 2026-10-27 run

74 flagged assays carry both trends (2 have too few years with footprints; none has unknown
footprints on this table).

| | by record | by distinct footprint |
|---|---|---|
| observations in total | 710,427 | 39,640 |
| median per assay | 3,880 | 239 |
| assays with p < 0.05 | **64** | **32** |

**35 of the 64 significant by-record trends do not survive**, and the collapses are not
marginal. The median ratio of |z| is 3.3, and the extremes are:

| by record | by footprint |
|---|---|
| z = -91.65, p = 0, n = 90,291 | z = -0.48, p = 0.63, n = 1,953 |
| z = -54.74, p = 0, n = 13,051 | z = +0.20, p = 0.85, n = 59 |
| z = -48.32, p = 0, n = 12,464 | z = +0.21, p = 0.84, n = 41 |
| z = -16.27, p = 1.5e-59, n = 3,847 | z = -0.01, p = 0.99, n = 130 |
| z = +9.63, p = 5.8e-22, n = 40,464 | z = -0.14, p = 0.89, n = 4,894 |

**23 of the 74 disagree on direction**, and the report says so in those rows. A p-value of
exactly 0 on ninety thousand records becoming p = 0.63 on two thousand footprints is the
clearest statement this project has of its own duplication problem: the trend was measuring
how often a sequence was deposited, not how often a target changed.

## How it is meant to be read, and the part that is not a fix

Both figures are printed and neither is the truth. The by-record figure is an **upper bound**
on the evidence, because duplicated deposits are counted as independent. The by-footprint
figure is nearer a **lower bound**, for two reasons recorded in `footprint_signature` and now
in the report's own sentence: a sequencing error in a primer site mints a footprint of its
own, which inflates the count and narrows the interval the unsafe way; and footprints record
positions in the primer sites only, so two genuinely distinct lineages that agree there
collapse into one class. The glossary entry for *trend* carries the same caveat.

No threshold was added and none is implied. Nothing in the screen hash's closure moved, so
the Sunday run is unaffected; the trend is recomputed from the calls table each render.
