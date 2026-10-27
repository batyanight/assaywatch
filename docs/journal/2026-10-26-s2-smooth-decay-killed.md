# S2 passes its own kill test and destroys four catches nobody thought to name

`positional_weight: exponential`, the second rung of the ladder
(`docs/journal/2026-10-24-scoring-strategy-test-plan.md` Part 1 S2). Pre-registration in
`strategies/s2-smooth-decay.yaml`. **Nothing shipped**; `config.yaml` is untouched, and
in this case it could not have been shipped anyway — see the replay-only limit at the end.

## The headline is a methodological one

S2's pre-registered kill criterion was **"Leucocytozoon @2016-12-31 lost"**, chosen
because that documented failure rests on a G:T mispair at d=2, which is exactly where a
decay curve departs most from the three-band step function. It was the obvious probe.

**It survives.** `Leucocytozoon_cyt_c_Hellgren_2004` at 2016-12-31 reads `low coverage /
agrees` under S2, the same as under S0. S2 passes the test that was written for it.

**And it loses four other documented catches, by name:**

| case | as of | S0 | S2 |
|---|---|---|---|
| `CDV_P_gene_Scagliarini_2007` | 2021-07-06 | `declining` / agrees | `stable` / **DISAGREES** |
| `PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999` | 2011-06-14 | `low coverage` / agrees | `stable` / **DISAGREES** |
| `Paramyxovirinae_..._Tong_2008_round1` | 2019-02-01 | `declining` / agrees | `stable` / **DISAGREES** |
| `Paramyxovirinae_..._round2` | 2019-02-01 | `low coverage` / agrees | `stable` / **DISAGREES** |

The first of those is **the project's only drift ground-truth event.** `CDV_P_gene_Scagliarini_2007`
at 2021-07-06 is the single `fails` + `drift` row in the development set, the one case that
tests the drift flag against a documented drift event rather than against a coverage
failure. S2 turns it `stable`.

So the candidate is killed by the **standing rule** — a candidate that loses a documented
catch is a bad candidate, stated per catch and never netted — and not by its own criterion.
That is worth recording as a lesson about the protocol, not only about this candidate: a
named kill criterion is a probe, and a probe can be insensitive. Four of the five catches
in this set were not named by anyone, and they are where the damage landed. **Future
candidates should pre-register "no documented catch lost" as the criterion and name a
specific case as an additional probe, not as the test.**

## Documented failure detection collapses, and the aggregate hides it completely

```
                                            S0              S2
  declining calls that were failures (PPV)  2/9  = 22%      0/4  = 0%
  documented failures caught                5/11 = 45%      1/11 = 9%
    among the cases it judged at all        5/8  = 62%      1/8  = 12%
  working assays called declining           5/32 = 16%      2/32 = 6%
  works / agrees                            10              16
```

Read the first three lines and S2 is a catastrophe. Read the last two and it is a clear
improvement: false alarms fall by two thirds and agreement on working assays rises from 10
cases to 16.

**Now count total disagreements, as any aggregate score would.** S0 has 3 + 2 + 5 = 10.
S2 has 7 + 2 + 2 = 11. One worse. **An aggregate reads this candidate as neutral while it
has reduced the tool's ability to detect a documented failure from 45% to 9% and taken its
precision to zero.**

That is the clearest demonstration in the ladder so far of why Part 0.4 insists on reading
the matrix cell by cell and why netting is forbidden. The trade S2 makes is sensitivity for
specificity, on a tool whose entire purpose is detecting failure.

## Why: the fitted curve systematically cheapens the 3' window

The constrained best cell is `w0 = 2.5, half_distance = 5.0`. Against the shipped step
function:

| d | step | curve | ratio |
|---|---|---|---|
| 1 | 3.00 | 2.50 | 0.83 |
| 2 | 3.00 | 2.18 | 0.73 |
| 3 | 3.00 | 1.89 | 0.63 |
| 4 | 3.00 | 1.65 | 0.55 |
| 5 | 3.00 | 1.44 | 0.48 |
| 6 | 1.00 | 1.25 | 1.25 |
| 8 | 1.00 | 0.95 | 0.95 |
| 11 | 0.50 | 0.62 | 1.25 |

A mismatch 5 bases from the 3' end costs **less than half** what it costs today, and d=3
and d=4 lose a third to a half. Beyond the window the curve is slightly harsher, which
buys nothing because those positions were already cheap.

So the fit did not smooth the cliff at d=6 so much as **discount the whole 3' window**,
and the 3' window is where drift signal lives: a primer site that is drifting accumulates
mismatches near the 3' end, which is why the step function weights it heavily in the first
place. Halving that is why four coverage and drift catches go `stable`.

This also falsifies S2's own prediction. It predicted "nothing carrying a 3'-terminal
mismatch changes, because at d=1 the curve is w0 and the step is `primer_3prime_penalty`,
and both are near 3.0". At the fitted cell w0 is 2.5, not 3.0, and the real movement is not
at d=1 at all — it is at d=2 to d=5, which the prediction did not consider.

## The panels say the same thing S1's did

Fitted with `scripts/fit_panel_thresholds.py --grid weight`: **0 of 35 cells lose nothing.**
The floor is 4 lost rows, at `(2.5, 5.0)`, and all four are Forslund no_band rows — HPV55,
HPV2, HPV44 and HPV74. The unconstrained best, `(2.5, 2.0)`, takes 24 wrong to 12 by losing
six of them.

**The Forslund negatives are now the binding constraint on this whole axis**, for the second
candidate running. Ten rows, in one paper, are what stands between every loosening candidate
and acceptance, and `docs/bayesian-scoring-plan.md` already identifies those same ten as the
only informative within-family negatives in the corpus against a gate of 40. That is a
corpus problem, and it is plan step 7.

The Rahn control is 0 wrong at S0 and 0 wrong at the chosen cell, again seeing nothing.

Leave-one-paper-out: 17 wrong of 115 rows, picking `{(2.5, 5.0): 4, (2.0, 1.0): 1}`.

## Method notes

- **The replay path was controlled before it was used.** `score_panel_replayed` with no
  curve reproduces the real screen's call on **all 179 panel rows**. Without that control
  an S2 result would rest on an unverified second implementation of `score_primer`'s loop,
  which is the failure mode that nearly shipped the first chance-pair test.
- **S2 is REPLAY-ONLY, and that is a harder limit than it sounds.** `config.yaml` has
  three bands and two widths, so a curve cannot be written as an overlay; and
  `assaywatch/score.py` knows only the step function, so a curve cannot be *screened* with
  either. `scripts/rescore.py` implements it for pricing. Shipping one would need a change
  to the package and a full rescreen. Pricing it first is the right order, and it saved
  exactly that work here.
- Candidate selection is frozen in both the panel fit and the full-table price, so the
  tier-2 figures are a price and not a proof. The four lost catches are status changes
  driven by many records each, not by one amplicon's choice, so the kill stands.
- The full-table replay moved 137,827 calls: 87,143 fail -> reduced, 42,920 reduced ->
  detect, 3,536 detect -> reduced, 2,951 fail -> detect, 1,277 reduced -> fail. The small
  reverse flows come from the curve being harsher just past the window.

## Where the ladder stands

S1 and S2 are both rejected, and both died on the same two things: Forslund's ten
within-family negatives on the panels, and documented failure catches on tier-2. Neither
was a close call.

S3 (two hand-set per-chemistry switches) is next and is a different shape — it is the one
rung that does not loosen uniformly, since one of its switches makes probe assays *stricter*
by not counting `reduced` as detected. That matters now: both failed candidates failed by
loosening, so a candidate that tightens somewhere is the one with a chance.

S4 was specified as "M1 re-tested under S1+S2+S3". S1 and S2 are gone, so that stack no
longer exists and S4 needs re-specifying against `budget` plus whatever survives of S3.
