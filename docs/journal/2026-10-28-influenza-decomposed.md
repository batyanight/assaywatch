# The influenza matrix assay's 6.5% is three different things, and only one of them is drift

2026-10-28. `lineage.md` could say that H3N2 reads 1.2% of 38,771 records and not whether
that is a fall or has always been so — the question yesterday's sublineage entry raised
and left open. The lineage report now carries a **per-year block** under each lineage below
the threshold (`lineage_report._per_year_blocks`), built with the same `lineage.lineage_of`
the share table uses, from deposit years read in the metadata pass that was already
running. 252 such blocks, 3,652 year rows, no extra I/O.

The first question it answers is the one it was built for, and the answer is flat.

## H3N2 was never detected. Not once, in twenty years

| year | evaluable | detected | share |
|---|---|---|---|
| 2005 | 531 | 6 | 1.1% |
| 2006 | 491 | 8 | 1.6% |
| 2010 | 149 | 7 | 4.7% |
| 2014 | 401 | 26 | 6.5% |
| 2019 | 3,880 | 43 | 1.1% |
| 2022 | 4,193 | 22 | 0.5% |
| 2025 | 8,330 | 6 | 0.1% |
| 2026 | 6,321 | 39 | 0.6% |

So the subtype the literature flags is not a drift case for this assay at all: **its probe
has never matched H3N2 records in the archive**, at any point in the record. `declining`
would be the wrong word for that, and `low coverage` the right one —
`lineage.require_working_baseline` exists for exactly this and is why the H3N2 lineage is
not what drives the verdict.

## What does drive it: three components, measured apart

The verdict is the pooled share, 6.5% of 30,382 recent evaluable records, "change from
baseline −15% to −14%". Splitting every evaluable record by what its GenBank title says
about its subtype:

| year | H3N2/H1N1 | other named subtype | untyped |
|---|---|---|---|
| 2009 | 3.1% of 840 | 88.3% of 787 | 95.0% of 20 |
| 2011 | 11.6% of 146 | 89.7% of 126 | 85.3% of 34 |
| 2017 | 10.5% of 687 | 83.4% of 1,327 | 73.7% of 38 |
| 2018 | 5.0% of 3,514 | 86.5% of 1,519 | 57.4% of 136 |
| 2019 | 2.0% of 5,970 | 61.7% of 1,157 | 28.2% of 298 |
| 2022 | 0.7% of 4,459 | 48.4% of 820 | 13.5% of 155 |
| 2023 | 0.5% of 6,515 | 32.1% of 779 | 4.1% of 763 |
| 2025 | 0.2% of 14,348 | 56.2% of 2,200 | 5.4% of 111 |
| 2026 | 0.5% of 9,187 | 39.4% of 1,131 | **0.1% of 4,729** |

Three effects, and they pull in the same direction for different reasons:

1. **A twenty-year coverage gap.** H3N2 and H1N1 are never detected, and they went from a
   quarter to a half of deposits in 2008–2015 to **86% of them in 2024–2025**. That alone
   drags the pooled share down without anything about the assay changing — the
   "denominator is drift-correlated" caveat this project already records, in its sharpest
   form yet.
2. **A real fall in the subtypes it did detect.** The other named subtypes read 88–90% in
   2009–2011 and 83–87% in 2017–2018, then **61.7% (2019), 48.4% (2022), 32.1% (2023),
   56.2% (2025), 39.4% (2026)**. That is drift, in the records this assay works on, and it
   is invisible in the pooled number because the pooled number is dominated by subtypes it
   never worked on.
3. **A recent flood of records the title pattern could not read.** 2026 alone holds
   **4,729 evaluable records whose title names no subtype *to this pattern*, detected at
   0.1%**, against 111 in 2025 and 136 in 2018. That one is not a third effect: see below.
   It is effect 1 again, hidden behind a regex.

## The third effect was my own regex

The decomposition above says 4,729 records in one year carry no subtype, and the obvious
next move is a resolver that reads the subtype out of the sequence. Measuring the bucket
first (`<scratchpad>/untyped.py`) killed that plan before it was written. All 4,729 are
<1.2 kb M-segment records, 4,657 of them score `reduced`, and **3,857 carry a subtype right
there in the title**:

| what the parenthetical says | records |
|---|---|
| `H1pdm09` | 2,220 |
| `H3` | 1,607 |
| `HxNx`, `H3Nx`, `H1`, `H1N2v`, `HxN2`, `HxN8`, `H5`, `H1Nx`, `HxN1` | 30 |
| nothing | 872 |

The shipped pattern was `\((H\d+N\d+)\)` — both numbers required. GenBank prints
`A/New York/26/2026(H3)` when the N is untyped and `A/Hawaii/1/2026(H1pdm09)` for the 2009
pandemic H1N1 lineage, and neither matches. So there was no new phenomenon in 2026, only a
convention this project could not read.

Broadened to `\((H\d+(?:N\d+v?|Nx|pdm\d+)?|Hx(?:N\d+|Nx)?)\)` and shipped, after both gates
`config.yaml` requires of a sublineage change: tier-2 identical case for case on the
development set (6/11 caught, PPV 4/10, 4/32 false alarms, 2/6 partial gaps) and
`report_diff` against `results/2026-10-27` printing **No assay changed status** — 0 of 193.

What it changes is the one thing it was meant to:

| | narrow | broadened |
|---|---|---|
| H1pdm09 | — | 0 of 2,220 (0.0%) |
| H3 | — | 5 of 1,745 (0.3%) |
| H1 / HxN2 / H3Nx | — | 0 of 115, 2 of 56, 1 of 52 |
| residual *Alphainfluenzavirus influenzae* | 638 of 6,853 (**9.3%**) | 594 of 2,571 (**23.1%**) |

Both tables above are renders off `results/2026-10-27/calls.tsv.gz` with the two configs;
neither the dated run directory nor `docs/example-run-2026-10-27/` was rewritten, because
each is a record of what ran that day beside its own `config.effective.yaml` and the pattern
was not in it. Sunday's run is the first whose artefacts carry the broadened pattern.

4,188 records move out of the residual carrying 8 detections between them, which is effect 1
exactly: `H1pdm09` is pandemic H1N1 and `H3` is H3N2 with the N left off, the two subtypes
the probe has never matched. They were sitting in the unlabelled bucket halving its
apparent share. The records that genuinely carry no subtype are detected at 23.1%, not
9.3% — the pattern was not just missing labels, it was corrupting the one row that is
supposed to mean "unknown".

## Why this matters beyond one assay

The 2026-10-04 review's complaint was that "one population proportion per assay cannot see
a lineage-conditional failure". This is the same complaint from the other side: one
population proportion cannot tell a **coverage gap** from **drift**, and for this assay both
are present at once in a single number that reads "6.5%, down 15 points". The third thing it
looked like it could not tell apart — a metadata artefact — turned out not to exist.

What the per-year block buys is the ability to say which. It is report-only, costs nothing,
and changes no verdict — the honest place for a decomposition that the estimand cannot
carry.

**What it argues for next**: the per-year rows make `drift.window_on` (deposit against
collection date) measurable per lineage rather than per assay, which is the other half of
asking when a fall happened. The sequence-based subtype resolver is **not** on that list any
more, and the reason is the point of this entry — the 872 records that carry no label at all
do not justify a classifier, and the 3,857 that do never needed one.
