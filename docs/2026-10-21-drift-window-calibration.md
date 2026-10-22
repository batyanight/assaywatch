# Drift window and minimum, calibrated together (2026-10-21)

ROADMAP carried this as open: "the drift rules interact and are untested.
`recent_window_months: 24` with `min_records_for_drift: 20` is why Bd reads
insufficient data at 100% detected — shorten the window and assays fall below
the minimum, lengthen it and real change is diluted. Validation has to set the
pair together." At (24, 20), **17 of ~49 validation cases were `undecided`**.

This is computed from the existing calls table — drift is a report-time verdict,
not a screen — so the whole sweep needed no rescreen. Each (window, minimum) pair
was scored against `docs/validation-cases.tsv` by `scripts/retrospective.py`.

## The grid

Each cell: agrees / weaker / DISAGREES / undecided, over ~49 cases.

```
  win/min        10            15            20            30
   18mo      16  6 13 14    17  6 11 15    15  6 11 17    13  4 11 21
   24mo *    17  7 11 14    17  7 10 15    15  7 10 17    13  5 10 21
   36mo      17  7 11 14    17  7 10 15    15  7 10 17    13  5 10 21
   48mo      16  9 10 14    16  9  9 15    14  9  9 17    12  7  9 21
   60mo      18  9  8 14    18  9  7 15    16  9  7 17    14  7  7 21
```

`*` = current (24, 20): 15 agree, 7 weaker, 10 DISAGREE, 17 undecided.

The two knobs do **different** things, which is the point of setting them together:

- **`min_records_for_drift` sets `undecided`, not accuracy.** `undecided` depends
  only on the minimum (14 at 10, 15 at 15, 17 at 20, 21 at 30) and is flat across
  every window, because `assess` already auto-widens a thin assay's window to try
  to reach the floor. Lowering the floor decides more cases; it barely touches
  DISAGREES.
- **`recent_window_months` sets accuracy (DISAGREES), not `undecided`.** A longer
  window monotonically *reduces* false calls: at min 15, DISAGREES falls 11 → 10 →
  10 → 9 → 7 as the window goes 18 → 24 → 36 → 48 → 60.

## What the DISAGREES are, and why the window moves them

The 10 DISAGREES at (24, 20) are 7 **false alarms** (a working assay called
`declining`) and 3 **misses** (a failing assay called `stable`: Bd @2017,
INFLUENZA_A Matrix @2010, Pan_hemoparasite @2016 — denominator problems no
threshold fixes).

Going (24, 20) → (60, 15), per case: it **catches 2 slow fails** (Pan_hemoparasite,
Leucocytozoon — coverage erosions only a multi-year window accumulates enough
records to see), **reclassifies 3 false `declining` alarms as `low coverage`** (a
longer baseline reveals the assay was never well-covered, not freshly declining —
a genuine correctness gain in the declining-vs-low-coverage distinction), and
introduces **1 new false alarm** (ENTEROVIRUS VP3_VP1, stable → declining). Net
DISAGREES 10 → 7.

So the window's benefit is real and mechanistic, not dilution of signal.

## What the grid cannot settle

Two thresholds fitted on ~49 cases is easy to overfit, and the validation set has
a structural blind spot. `assess` aggregates the recent window against a
pre-window baseline, so a **60-month "recent" window spans 5 years**: a genuine
recent crash (4 good years, then a collapse in the last year) is averaged toward
"fine" and flagged late. The validation cases are scored for historical *as-of
accuracy*, which rewards a longer window and **cannot see the slow-to-warn cost**.
A drift monitor exists to warn early; that is the half the grid is blind to.

Blast radius confirms the asymmetry: against the current report, **(24, 15) moves
11 of 208 headline statuses; (60, 15) moves 53** — a quarter of the registry.

## Recommendation

**Apply `min_records_for_drift` 20 → 15. Leave `recent_window_months` at 24, and
treat the window as a maintainer decision.**

- *min 20 → 15* is safe and mechanism-backed: 15 records still give a usable Wilson
  interval, it turns 2 `undecided` cases into correct calls (one of them catching
  a real fail, Leucocytozoon @2016), it introduces **zero** new DISAGREES, it has
  no recency cost, and it moves only 11 statuses. This is the calibration the
  ROADMAP asked for, done against known answers.
- *window 24 → 48 or 60* scores better on the validation set (−1 to −3 DISAGREES)
  but reshapes 20–53 statuses and buys that accuracy by making "recent" mean 4–5
  years — a cost the validation set is built not to measure. That trade is the
  maintainer's to make, not a grid minimum's to grab, and it should be made with
  the recency objection in front of it, not behind it.

## The bench panels, for context

The five bench panels are cross-sectional (one gel per type) and do not exercise
the longitudinal window at all, so they neither support nor contradict a window
choice; they are named here only so the record shows they were considered and
found silent on this question. The validation set is the only instrument that
speaks to it, and its limit is stated above.
