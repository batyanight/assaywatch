# The drift window and the record minimum, priced together: the window matters and the minimum does not

2026-10-27. `recent_window_months: 24` with `min_records_for_drift: 15` is the pair that
made Bd read "insufficient data" at 100% detected on 17 recent records, and the roadmap
has said since the 2026-10-04 review that the two have to be set together. They never
were. `scripts/window_grid.py` runs the development set under every pair in a grid,
each cell one config overlay on the same cached calls table, nothing rescreened.

    python scripts/window_grid.py --calls results/2026-10-26/calls.tsv.gz

| window (months) | minimum | caught | PPV of `declining` | false alarms | declined to judge |
|---:|---:|---|---|---|---:|
| 12 | 10 | 5/11 | 3/9 | 4/32 | 14 |
| 12 | 15 | 5/11 | 3/9 | 4/32 | 15 |
| 12 | 20 | 5/11 | 3/9 | 4/32 | 16 |
| 12 | 30 | 5/11 | 3/10 | 5/32 | 20 |
| **24** | **15** | **6/11** | **2/9** | **5/32** | **15** |
| 24 | 10 / 20 / 30 | 6/11 | 2/9 | 5/32 | 14 / 16 / 20 |
| 36 | 10 / 15 / 20 / 30 | 6/11 | 2/8 | 4/32 | 14 / 15 / 16 / 20 |

Shipped is 24 / 15, in bold. Every proportion carries the Jeffreys interval in the
script's output; at these counts the interval is the finding.

## What the grid says

**The minimum does not move the matrix between 10 and 20.** Same catches, same PPV, same
alarms in every window; all it changes is how many cases the tool declines to judge
(14, 15, 16). At 30 it declines 20 and, in the 12-month window, adds a false alarm. So
the knob the project has argued about most does one thing on this set: it trades
refusals for nothing. That is also the plan's own prediction about where a hierarchical
layer earns its keep — the refusals, not the flags.

**The window does move it, in both directions.** Twelve months **loses a documented
catch** (5/11), which is the kill criterion for any candidate here, stated per catch
and never netted against the alarm it also drops. Thirty-six months keeps all six
catches and **drops one false alarm** (4/32 against 5/32, PPV 2/8 against 2/9): the
same `declining` set minus one working assay. On this table 36 dominates 24.

## What is not decided

Nothing ships from this. `docs/validation-cases.tsv` is the development set and it is
spent for threshold-setting — at least seven settings have already been accepted or
rejected against its 49 rows, which collapse to about seven independent failure events,
and a one-alarm difference is inside that noise by the file's own account. What this
grid does is name the one cell a held-out read would be worth spending on: **36 / 15**,
the only change that improves a column without costing a catch. Until set 2 holds enough
rows to be read once, 24 / 15 stays, and the roadmap item moves from "the pair is
untested" to "the pair is measured; the candidate is named".

One more thing the table shows that no single number does: the refusal count is set by
the minimum alone, and the catch count by the window alone. They are not, on this
evidence, coupled — the fear that shortening the window would push assays under the
minimum does not materialise at 12 months on this set, because the catches it loses are
lost to dilution of the signal, not to refusals (14 at 12/10 against 14 at 24/10).
