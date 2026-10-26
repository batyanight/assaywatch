# Testing scoring strategies, Bayesian ones included: the harness before the candidates (2026-10-24)

Status: plan. Nothing here is built. It sits on top of `docs/bayesian-scoring-plan.md`
(what "Bayesian scoring" could mean: C1 proportions, C2 the per-record call, C3 the
validation matrix) and does not repeat it. This document is about the part that doc
left implicit: **how to test any candidate rule fairly and cheaply**, because every
candidate so far has been expensive to try and judged on the same 49 in-sample cases.

## Why a harness first

Three scoring candidates have been tried. All three were decided by tier-2 and two died:

| candidate | cost to try | verdict | where |
|---|---|---|---|
| conventional override (`by_chemistry`) | one full rescreen | lost 3 of 5 catches | `docs/2026-10-19-conventional-override-validation.md` |
| M1 identity-aware 3' penalty | two rescreens | lost 1 catch at d=2; HELD | `docs/2026-10-22-M1-tier2.md` |
| M2 nearest-neighbour ΔG | a probe script | killed at step 0: ranks A:A/A:G backwards | `docs/2026-10-21-M2-step0-killtest.md` |
| `engine: serial` | one replay | ships off, thresholds uncalibrated | `config.yaml` `scoring.engine` |

Each cost 25-30 minutes of screening per variant, so each was tried once, as one bundle
of numbers, and judged on the development set. That is why the override's verdict
("direction right, all three numbers at once wrong") could not be refined, and why M1
could not be re-tested jointly with the serial engine when its own write-up said the
two were entangled ("the G:T discount and this catch are incompatible **under the
`budget` engine**"). A Bayesian model multiplies the number of variants to try by a
hundred. Without a harness it cannot be tested at all.

The one fact that makes a harness possible: **scoring is a function of the mismatch
configuration, and the screen already finds that configuration.** What the screen does
not do is write it down completely. It stores positions (`fwd_mm_from_3prime` =
"14,6,2") and not identities (A:G at 2). Store the whole footprint once, and every
candidate rule is a replay over the calls table in seconds instead of a rescreen.

## Part 0: the harness

### 0.1 One rescreen that writes the footprint

Per oligo, per row, a `*_mispairs` column: the aligned mismatches as
`primer:template@distance_from_3prime`, e.g. `A:G@2,T:C@14`, plus the ambiguity
positions already counted. `scripts/bench_panel.py` already derives exactly this for a
panel (it prints "a W opposite template G prints A:G/T:G"); the work is to emit it
from `score.score_primer` into `Call.as_row`. Also: oligo length, probe type (MGB or
hydrolysis) and chemistry come from the registry at replay time, not the row.

This is the `bayesian-scoring-plan.md` "one infrastructure blocker", generalised:
it serves identity-aware scoring, per-chemistry scoring, smooth position weights and
C2 alike. One rescreen (~12 min at the current granularity, measured tonight).

**The boundary this does not cross.** A replay can change how a found site is *scored*.
It cannot change which sites are *found*: `max_mismatches_searched`, gapped alignment
(the Bd probe case, `docs/2026-10-23-wave3-bd-miss.md`), the chance-pair filter and
the amplicon size window are search settings and still need a rescreen. State that in
the harness output so nobody replays a search change and calls it scoring.

### 0.2 `scripts/rescore.py`

    python scripts/rescore.py --calls results/baseline-2026-10-22/calls.tsv.gz \
        --strategy strategies/serial-calibrated.yaml --out <scratch>/serial/

Reads the footprint columns, applies one strategy, writes a calls table and a sidecar
naming the strategy and its parameters, into a scratch directory and never into
`results/`. A strategy is either a `scoring:` overlay on `config.yaml` (every knob that
exists today) or a small Python callable `footprints -> call` for shapes the config
cannot express (a smooth decay, a fitted model). Then, in the same run, it calls the
things that already exist:

- `scripts/retrospective.py --cases docs/validation-cases.tsv --calls <new table>`
- `scripts/holdout.py --calls <new table>` (the optimism estimate)
- `scripts/bench_panel.py` over every `docs/bench-panels/*.tsv`, per type
- `scripts/report_diff.py` against the baseline table: how many calls moved, which way

One command, one strategy, one folder of numbers. Determinism: the same table and
strategy give the same folder byte for byte.

### 0.3 The evaluation sets, frozen before any fitting

| set | what it measures | role |
|---|---|---|
| bench panels, within-family rows only (`docs/bench-panels/`: Forslund 60 band / 10 no band, Meyer 8/1, Barrett 7/0, Rebelo 8/0) | per-type: did this mismatch configuration give a band | the only type-level truth; **fitting data** for any model |
| Rahn 1992 (23 band / 41 no band, other genera) | specificity only | control that a rule does not start detecting non-targets; never a fitting set for drift |
| `docs/validation-cases.tsv`, 49 cases, ~7 independent failure events | assay-level: does the status agree with published follow-up | **development set**: selection and sanity, in-sample, reported with Jeffreys intervals (C3) |
| `docs/validation-cases-heldout.tsv` | the same, unseen | **read once**, by the maintainer, when a strategy is proposed for shipping. Not before. |
| the three wave-3 mechanism cases: Bd (amplicon-level, ungapped), Usutu (flat 3' window on a conventional primer), influenza (probe `reduced` counted as detected) | does the candidate fix the named mechanism | probes, not scores: each is one case and already in the development set |
| `results/baseline-2026-10-22/` | every call under the shipped rule | the diff reference; every candidate is reported as moves from here |

Two existing rules travel with the sets. **A candidate that loses a documented catch
is a bad candidate** (the M1 decision), stated per catch, not netted against gains.
And **a change that only loosens will always cut flags**; that is not evidence
(`docs/2026-10-19-conventional-override-validation.md`).

### 0.4 What gets reported for every candidate, always the same table

1. Bench panels: band/no-band accuracy per panel, **leave-one-panel-out** when the
   candidate has fitted parameters (leave out a whole paper, never a row: the rows of
   one panel share a primer pair and a lab, so they are not independent, and a
   row-wise split would let the model see its own test paper).
2. Tier-2: the 2x3 matrix with Jeffreys 95% intervals (C3), plus the three counts the
   matrix hides: flags, assays refused a verdict, moved calls.
3. The two-directions check: the Usutu class (conventional scored too harshly) and the
   influenza class (probe scored too leniently) in the same table, because a rule can
   fix one by making the other worse and the aggregate will not show it.
4. Hold the denominator fixed. `count_diverged_as_fail`, patent exclusion, scope and the
   anchor test (tonight's `drift.anchor_fdr`) are denominator choices, a different axis.
   Every scoring comparison runs on the same denominator settings, stated in the output.

### 0.5 Protocol

Pre-register each candidate here before running it: what it changes, the predicted
effect on each set, and what result kills it. Change one thing per run. The development
set selects among candidates; the held-out set is read once at the end. The repo's
determinism rule applies to models too: closed-form or MAP/empirical-Bayes fits, fixed
seeds and iteration counts where sampling is unavoidable, and a committed parameter
file so the report rebuilds without refitting.

## Part 1: the ladder of candidates, cheapest first

Each is one `rescore.py` run once Part 0 exists. The order is by how much each one
teaches about the next.

**S0. The shipped budget rule.** The reference row of every table.

**S1. `engine: serial`, calibrated.** Exists, ships off, `oligo_ok_max`/`oligo_weak_max`
are placeholders copied from the budget thresholds. Fit the two thresholds on the
bench panels (LOPO), then tier-2. Prediction: it only loosens (every measured move was
fail->reduced or reduced->detect), so flags fall; the influenza probe case gets worse
until S3; the FAP false fails do not move, because they rest on identity, not summing.
Kill: loses a catch at any threshold pair the panels accept.

**S2. A smooth positional weight.** Replace the 5/5/rest step function with a decay
`w(d)`, one or two parameters (an exponential with a half-distance is enough to start).
Motivated by Usutu: d = 3 is where the step function and the literature part company.
Fit on the panels. Prediction: FAP and Usutu improve; nothing with a terminal mismatch
changes. Kill: Leucocytozoon @2016 (G:T at d = 2) lost.

**S3. Per-chemistry decisions, hand-set, as a mechanism probe.** Two switches, not a
table: for probe chemistry, `reduced` is not detected (the influenza mechanism); for
conventional chemistry, a terminal mismatch alone is `reduced` not `fail` (the
calicivirus Hel1 and Usutu mechanism). Test each alone, then together. This is
deliberately the frequentist version of what C2 would estimate; it is cheap and tells
whether the chemistry axis carries signal before a model is built on it. Kill: either
switch loses a catch.

**S4. Identity-aware 3' penalty (M1) re-tested under S1+S2+S3.** M1 is HELD by the
maintainer and this does not ship it. It re-asks M1's own open question: its write-up
says the lost catch and the G:T discount are incompatible under the budget engine
because `primer_3prime_penalty` 3.0 equals `reduced_max` 3.0; under serial gates and a
smooth decay that coincidence is gone. Prediction: FAP 12 of 14 and Barrett 3 of 3
false fails clear; whether Leucocytozoon @2016 survives decides it. Kill: it does not.

**S5. C2, the Bayesian per-record model.** As designed in `bayesian-scoring-plan.md`:
`P(detect) = P(fwd ok) x P(rev ok) x P(probe reports)`, each a logistic model over
identity, a smooth position term, adjacency and length, with chemistry as a
hierarchical intercept so the 43 probe assays borrow strength from the 154
conventional ones. Priors on the identity coefficients from Kwok 1990 and Stadhouders
2010, stated beside the numbers the way every `config.yaml` threshold already is.
Fit by MAP or empirical Bayes in scipy first; a sampler only if the posterior is
visibly non-Gaussian, behind an opt-in extra. Output per record is a probability;
migration thresholds it back to the four classes so S5 sits in the same table as
S0-S4. Aggregation to an assay is a Poisson-binomial, which `chance.py` already
implements.

**Gate before S5, from the existing plan and not negotiable:** at least 40
within-family negatives across several independent papers (today: 11). The corpus
sweep is the same literature pass as the held-out case collection, one read per paper
for both. Below 40, S5 is not fitted and nothing fitted on 11 is defended.

> **The 40 here and the "60+ across >= 10 papers" in `docs/bayesian-scoring-plan.md`
> are the same standard read at two points (reconciled 2026-10-26).** 40 is that
> file's kill floor, below which C2 is dead before it starts; 60 is its collection
> target, the count at which fitting ten coefficients is reasonable rather than merely
> not fatal. Neither number has moved and neither overrides the other. A corpus of 45
> means "fit it and report the interval honestly", not "the gate is met".

**Kill for S5:** under LOPO it does not beat the best of S1-S4 on the panels, or it
loses a catch on the development set, or its fitted identity coefficients contradict
Kwok's order (the M2 failure, which is the test that would have caught it).

**New evidence found 2026-10-24, and it is the right shape for this gate.** The scope
audit turned up three lab-confirmed POSITIVES that the current model scores `fail` on a
single 3'-terminal mismatch, all in one assay and all from the design paper's own panel:
`LEPTOSPIRA_lipL32_Ahmed_2020` against *L. kmetyi* (0 detected of 13 records),
*L. adleri* (0 of 4) and *L. gomenensis* (0 of 8). Ahmed et al. 2020 Table 1 marks all
three "Pathogenic" and scores each `+` in the lab. Every failing record carries the
reverse primer mismatched at position 1 from its 3' terminus and nothing else material,
while *L. interrogans* (578 records), *L. borgpetersenii* (209), *L. santarosai* (59),
*L. weilii* (47), *L. noguchii* (36) and *L. kirschneri* (35) match at penalty 0 with no
mismatch anywhere. *L. wolffii* is a built-in control: the paper scores it `-` and the
screen fails it too.

Three cautions on using it. It is **one** assay and one paper, so it is three correlated
points, not three independent ones. It is the assay's **own** panel, so it cannot enter
`docs/validation-cases.tsv`, which excludes exactly that — but the bar for the S5 bench
corpus is different from the bar for a tier-2 validation case, and this clears the former.
And it is a *positive* the model calls negative, i.e. a false negative of the scoring rule,
whereas the 40-case gate above counts within-family **negatives**; it belongs on the other
side of the ledger and does not count toward that 40. Its real use is as a direct probe of
`terminal_mismatch_fails` and of `by_chemistry`: this is a hydrolysis-probe assay, where a
terminal primer mismatch is far more tolerable than the shipped rule assumes. The
CALICIVIRUS Helicase entry's 3'-terminal G/C mismatch is the same mechanism on a
conventional PCR, which makes the pair of them a two-chemistry test of the same knob.
Evidence: `docs/2026-10-24-scope-audit.md`, item 10.

## Part 1b: C1 is a separate axis, and it is free

C1 (Beta posterior on the detection proportion, `P(θ < 0.90 | data)` as the flag rule,
hierarchical shrinkage across lineages) is not a scoring strategy. It changes how calls
are aggregated, it is report-time, and it needs no rescreen and no harness beyond
`retrospective.py --config`. The one-afternoon experiment in the Bayesian doc stands:
recompute every per-lineage interval three ways and re-run tier-2 under the posterior
rule. Do it independently of S1-S5 and hold it fixed while scoring candidates run, or
the two axes will be confounded in every table.

## Part 2: order and effort

1. **Harness** (Part 0): the footprint columns and one rescreen; `rescore.py`; the
   frozen sets with C3 intervals in the output. About a week of evenings; the rescreen
   is 12 minutes.
2. **S1, S2, S3**: an afternoon each once the harness exists. These are also the
   first real use of the bench panels as fitting data.
3. **S4**: an afternoon, result goes to the maintainer with the M1 hold still in force.
4. **Corpus sweep** (shared with held-out collection): weeks, in parallel with 2-3.
5. **S5** when the gate is met. Then the held-out set, read once.
6. **C1** any time, independently.

## Part 3: what not to do

- Do not fit anything on the 49 cases and report the matrix as the result. Fit on
  panels, select on the development set with intervals, confirm on held-out once.
- Do not change a search parameter inside a "scoring" run. The harness refuses it.
- Do not hand-fit a full `by_chemistry` table if S5 is going to happen. S3's two
  switches are a probe of the mechanism, not a second penalty table.
- Do not let a sampler into the pipeline path. Deterministic fits, committed parameters.
- Do not net gains against a lost catch. Each documented catch is reported by name.

## Jargon, since this is the statistics the project is learning

- **Leave-one-panel-out (LOPO):** cross-validation where the unit held out is a whole
  paper's panel. Rows from one paper share a primer pair, a lab and a protocol, so they
  are not independent draws; holding out single rows would let the model see its own
  test set through its siblings and report an optimistic score.
- **Pre-registration:** writing the prediction and the kill criterion down before the
  run, so a result cannot be re-interpreted as a success after the fact.
- **Empirical Bayes / MAP:** fitting the model's hyperparameters from the data and then
  using closed-form posteriors (or the posterior mode) instead of sampling. Same
  answer to first order, fully deterministic, no new dependency.
- **Shrinkage:** in a hierarchical model, a lineage with few records is pulled toward
  the assay's overall level, and one with many records is barely moved. It is what
  multiple-testing corrections approximate from the outside.
- **Poisson-binomial:** the distribution of a sum of independent yes/no outcomes that
  each have their own probability. An assay's expected detections over records with
  different P(detect) is one.
