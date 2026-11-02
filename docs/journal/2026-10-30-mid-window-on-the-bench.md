# The mid-window penalty on the bench panels: measurable, not settleable

2026-10-30. ROADMAP's mid-window item (E1) asked one question of the bench panels: does
any of their 179 rows turn on a single mid-window mismatch? If none did, the penalty would
rest on nothing this project can measure, and `config.yaml` should say so. The question is
answered, and the answer is more useful than either branch the item anticipated.

## Method

No new code. `scripts/price_terminal_mismatch.py` already scores the 179 bench rows under a
config and compares band/no-band against each paper's own result, with sequences cached
under `.tmp/bench-panels/`, so this is offline and competes with nothing. Reused its
`with_override` / `screen_record` / `BAND_CALLS` machinery inline to sweep
`scoring.primer_mid_penalty` over 0.0, 0.5, 1.0 (shipped), 1.5, 2.0, holding everything
else at the shipped config.

## Result

**8 of the 179 rows change their band/no-band prediction across the sweep** (12 if the
sweep is widened to 0.25 and 3.0). So the parameter is load-bearing on the bench, not
invisible to it — the item's "if none does" branch does not apply.

But every one of the 8 sits in a **`fitting`** panel. `docs/bench-panels/panels.tsv`
splits panels into `fitting` (115 rows, a model may be tuned on them) and `control` (64
rows, specificity only, never a fitting set). The lone control panel, Rahn 1992 Salmonella
*invA*, does not move at any penalty value. So the only rows that respond are the rows
reserved for fitting.

Agreement against the bench, all 179 rows:

| `primer_mid_penalty` | agree | FN | FP |
|---|---|---|---|
| 0.0 | 162 | 14 | 3 |
| 0.5 | 162 | 14 | 3 |
| **1.0 (shipped)** | **163** | 15 | 1 |
| 1.5 | 160 | 18 | 1 |
| 2.0 | 158 | 20 | 1 |

## What it settles, and what it does not

It settles the item's literal question: a bench row does turn on the mid-window penalty, so
`config.yaml` should not say the parameter is unmeasurable.

It does not settle the value. Agreement is flat (162–163) from 0.0 to 1.0 and only falls
above it, which rules out the high end but cannot choose between 0.0, 0.5 and the shipped
1.0 — the differences there are within one or two rows, all of them `fitting` rows, so
reading a best value off this table would be tuning on the set reserved for tuning. As
everywhere on these panels the error is FN-dominated (the shipped 1.0 gives 15 FN against 1
FP), which is the same one-sided signal the terminal-mismatch pricing found and is a
property of the panels, not of this parameter.

The honest status for the roadmap: the mid-window penalty rests on `fitting`-panel rows
only, not on nothing; the shipped 1.0 is not contradicted; and a second held-out row
remains the thing that would actually choose the value. 22 of the 23 assays the item flags
over the live run are not monkeypox, so such a row need not reopen the Mills question.
