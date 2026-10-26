# S1 is dead, and the panels can only fit one of its two thresholds

`engine: serial`, the first rung of the pre-registered ladder
(`docs/2026-10-24-scoring-strategy-test-plan.md` Part 1). Pre-registration in
`strategies/s1-serial.yaml`; its question, prediction and kill criterion are that test
plan's, dated 2026-10-24, not written after the result.

**Killed on its own criterion, twice over and independently.** The criterion is "it loses
a catch at any threshold pair the panels accept", and the standing rule is that a lost
catch is stated per catch and never netted against gains.

- **On the panels: no threshold pair is clean.** All 31 cells of the grid lose at least
  one row the shipped rule gets right. The floor is 2.
- **On tier-2: two documented catches lost, by name.** Both Paramyxovirinae L-gene cases
  at 2019-02-01, where the literature says the assay fails: `..._Tong_2008_round1` goes
  `declining` -> `stable`, and `..._round2` goes `low coverage` -> `stable`. Documented
  failures caught falls 5/11 -> 3/11, and the PPV of `declining` falls 2/9 = 22% -> 1/10 =
  10%.

Nothing was shipped. `config.yaml` is untouched and `engine` is still `budget`.

## What the grid actually says, which is more interesting than the kill

Fitted with `scripts/fit_panel_thresholds.py` over the five fitting papers (Forslund,
Barrett, Meyer, Rebelo, Ahmed), Rahn held out as a specificity control. `lost` counts rows
S0 scores correctly that the cell does not; `wrong` is the cell's total errors.

| `oligo_ok_max` | `oligo_weak_max` | lost | wrong |
|---|---|---|---|
| any of 0.5–1.0 | 1.0 | 17 | 41 |
| any of 0.5–2.0 | 2.0 | 9 | 33 |
| **any of 0.5–3.0** | **3.0** | **2** | **22** |
| any of 0.5–3.0 | 4.0 | 5 | 14 |
| any of 0.5–3.0 | 5.0 | 7 | 15 |
| any of 0.5–3.0 | 6.0 or 7.0 | 7 | 13 |

S0 itself is 24 wrong on the same panels.

**`oligo_ok_max` has no effect on panel accuracy at all.** Every cell sharing a
`oligo_weak_max` scores identically whatever `oligo_ok_max` is. The reason is structural
and not a quirk of this grid: `oligo_ok_max` only separates `detect` from `reduced`, and a
panel's truth is band or no band, so both sides of that line are the same answer. **The
panels can therefore fit only ONE of the two numbers the serial engine adds.** Half of
S1's parameterisation has no type-level evidence behind it, and nothing in the test plan
anticipated that.

**The curve is U-shaped and it bottoms out at the value already shipped.** `reduced_max` is
3.0, and `oligo_weak_max: 3.0` is the best cell on the panels. Tightening below it breaks
true positives — at 2.0 it loses measles, variola, volepox and HPV36 among others, at 1.0
seventeen rows — and loosening above it converts Forslund's genuine negatives into
predicted bands. The panels' verdict on the serial engine is that its best setting is the
number `config.yaml` already holds.

## Why no cell can be clean, structurally

The engine swap changes the comparison from a **sum** to a **max**, and that direction is
fixed. A record whose forward scores 2.0 and reverse 2.0 sums to 4.0 and fails under
`budget`; under `serial` its worst oligo is 2.0, so it is `weak` for any
`oligo_weak_max` >= 2.0 and the call becomes `reduced`. Raising the threshold cannot undo
that, and lowering it far enough to undo it starts blocking oligos that carry one ordinary
mismatch, which is what destroys the true positives at 1.0 and 2.0. So the loosening is a
property of the engine, not of its calibration, and two numbers cannot tune it away.

This matches the test plan's own prediction that S1 "only loosens". What the plan did not
predict is that the loosening lands on the **within-family negatives**, which are the
scarcest evidence this project has.

## The clearest result in the run: Rahn reports zero cost

The control panel is unchanged — **0 wrong at S0 and 0 wrong at the chosen cell** — while
the Forslund panel loses within-family negatives at every setting.

That is the whole argument for marking Rahn `control` and never a fitting set, now
measured rather than argued. Its 41 negatives are other genera, so they ask "does sequence
far from the target give a band", which `scoring.max_pair_evalue` already answers. A fit
that optimised total panel accuracy with Rahn included would have been handed 64 free
correct rows and told, truthfully, that specificity was untouched, while the assay quietly
began calling seven HPV types the design paper could not amplify.

## And the demonstration of why netting is forbidden

The unconstrained best cell, chosen by "fewest wrong" exactly as a normal fit would,
is `(0.5, 6.0)`: **24 wrong -> 13 wrong**, a 46% reduction, which reads as a clear win.
It gets there by rescuing positives and **losing seven of Forslund's ten informative
negatives** — HPV55, 2, 41, 44, 74, 66 and 35, every one a type the paper reports the
consensus PCR failed to amplify.

Those ten rows are the same ten that `docs/bayesian-scoring-plan.md` identifies as the
only informative within-family negatives in the whole corpus, against a gate of 40. A
candidate that spends seven of them to improve an aggregate is not an improvement, and the
aggregate cannot show it.

## The prediction was half right, and the half that failed is worth recording

S1 was expected to clear "the best-evidenced false positive in the registry":
`RANAVIRUS_..._MCP_Johnson_2008` fails LMBV genomes on distal mismatches summing to 4.0
against `reduced_max` 3.0, while Grizzle's Fig. 1 is a gel of those primers amplifying
LMBV.

**At the record level it works, exactly as designed.** 43 of that assay's 59 `fail`
records move to `reduced`, their worst-oligo penalty reading 2.5 where the sum read 4.0.
The mechanism does what the structural argument said it would.

**At the tier-2 level it changes nothing, because the case cannot see it.** That case is
`insufficient data / undecided` under S0 and under S1, and so are both `LMBV_dsDNA_MCP_Grizzle_2003`
rows (`no recent data`). The false positive is real and the validation set cannot price it.

So "S1 should clear the best-evidenced false positive" is **true of the records and false
of the case**, and the test plan's wording conflates the two. The honest version: the
serial engine is the right model of a false positive this corpus cannot measure.

## What S1 did buy, for the record

Six tier-2 cases improved: the three CMV UL55 gB cases at 2007-07-20,
`Pan_HERPES_dsDNA_Polymerase_round2` at 2018-11-07, `Paramyxovirinae_..._Tong_2008_round1`
at 2024-12-26, and `RANAVIRUS_..._MCP_Pallister_2007` at 2012-09-30 — mostly `low
coverage/weaker` becoming `stable/agrees`. Two new false alarms appeared:
`ENTEROVIRUS_ssRNA_VP3_VP1_round2` at 2018-09-30 and `POLYOMAVIRUS_dsDNA_VP1_Johne_2005`
at 2019-08-29 both become `declining` against a literature `works` and `partial`.

Net +6 and -4 on agreement, which is precisely the netting the rule forbids, and the
headline figures fall in both directions anyway.

The replayed table also shows the fitted cell is not purely loosening: of 132,266 moved
calls, **94,146 are fail -> reduced and 38,120 are detect -> reduced**, because
`oligo_ok_max: 0.5` is tighter per oligo than `detect_max: 1.0`. Everything collapses
toward one bin, which is another reason the panels cannot see `oligo_ok_max`: it is doing
work that only shows up in a column the panels do not have.

## Method notes

- **Rescreened per cell, not replayed.** Under `serial` the thresholds enter the choice of
  which candidate amplicon wins, so a replay over a fixed table would hold the budget
  engine's winner fixed and price a slightly different rule. The panels are 21 MB, so
  exactness is affordable; over 2.7 M calls it is not, which is why
  `scripts/rescore.py` names frozen candidate selection as its one approximation.
- **Leave-one-paper-out, never leave-one-row-out.** 16 wrong of 115 rows, picking
  `{(0.5, 3.0): 4, (0.5, 6.0): 1}`. The two Meyer files are one paper and are held out
  together.
- **The tier-2 figures come from a replay** (`scripts/rescore.py`), so candidate selection
  is frozen there. That weakens the tier-2 numbers as a price but not as a kill: the two
  lost catches are status changes driven by many records each, not by one amplicon's
  choice, and S1 is already dead on the panels, which were rescreened.
- `reduced` counts as a band throughout. That is the shipped reading and it is exactly
  what S3's probe switch proposes to change, so it is held fixed here; varying both at
  once would make neither legible.

## What this means for the rest of the ladder

S2 (a smooth positional decay) and S4 (M1 re-tested) were both to be measured **under
S1**, on the reasoning that `primer_3prime_penalty` 3.0 equalling `reduced_max` 3.0 is a
coincidence that disappears under serial gates. That stack is no longer available: S1 is
rejected, so S2 and S4 must be re-specified against `budget`, or S1 must be revisited with
something other than two thresholds — a per-chemistry `oligo_weak_max` is the obvious
candidate, and it is S3's territory.

The Forslund negatives are now the binding constraint on this whole axis. Every loosening
candidate will meet them, and there are ten.
