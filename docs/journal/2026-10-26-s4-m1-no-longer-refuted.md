# S4: M1 is no longer refuted by the measurement that refuted it

Part 1 S4 of `docs/journal/2026-10-24-scoring-strategy-test-plan.md`, re-specified.
Pre-registration in `strategies/s4-m1-alone.yaml` and `strategies/s4-m1-under-s3a.yaml`.
**Nothing shipped**; `mispair_penalty` is still `{}`.

## Re-specified first, and the reason recorded rather than quietly fixed

S4 was written as "M1 re-tested under S1+S2+S3", on the reasoning that
`primer_3prime_penalty` 3.0 equalling `reduced_max` 3.0 is a coincidence that disappears
under serial gates. **S1 and S2 were both rejected earlier today**, so there are no serial
gates and no decay curve, and that coincidence is still there. The only surviving rung is
S3a, so S4 became M1 under `budget` plus S3a. That is a weaker experiment than the one
written down: it cannot test the claim S4 was written to test.

A reference row was added for exactly that reason — `s4-m1-alone`, M1 under the shipped
engine, whose stated purpose was that "a DISAGREEMENT with the 2026-10-22 record would be
the finding, and would mean that decision needs re-taking rather than citing."

That is what happened.

## My prediction was wrong, and it was wrong in the interesting direction

The pre-registration predicted M1 would lose the Leucocytozoon catch again, reasoning that
`Leucocytozoon_cyt_c_Hellgren_2004` is `chemistry: conventional` while S3a only reaches
`hydrolysis_probe` and `mgb`, so the one mechanism that could rescue the catch cannot reach
the assay that needs it. The chemistry check was right — four of the five documented
catches are conventional and only `CDV_P_gene_Scagliarini_2007` is `mgb` — and the
conclusion was wrong, because the catch does not need rescuing.

**M1 alone changes zero rows of the 49-case tier-2 matrix.** Not the Leucocytozoon row, not
any other. Both halves of the gate M1 failed on 2026-10-22 — "caught failures do not fall
and no works/partial case newly disagrees" — pass today, with nothing to spare because
nothing moves at all.

## The record-level effect reproduces exactly; the verdict-level effect has gone

`docs/journal/2026-10-22-M1-tier2.md` recorded 17 Leucocytozoon records changing call:

| transition | 2026-10-22 | today |
|---|---:|---:|
| `fail` -> `detect` | 11 | 11 |
| `fail` -> `reduced` | 4 | 4 |
| `reduced` -> `detect` | 2 | 2 |

and totals detect 153 -> 166, fail 120 -> 105, reduced 67 -> 69, `no_amplicon` 7,564
unchanged. **Every one of those figures reproduces today, exactly.** The scoring change
does precisely what it did four days ago.

What has changed is the verdict's sensitivity to it. At as-of 2016-12-31 the recent window
holds **21 evaluable records**:

| | detected share | 95% interval | status |
|---|---|---|---|
| shipped | 28.6% of 21 | 14%–50% | `low coverage` / agrees |
| M1 | 33.3% of 21 | 17%–55% | `low coverage` / agrees |

M1 moves one record of 21 and the interval's upper bound from 50% to 55%. The threshold is
90%. **The verdict is nowhere near its boundary, so the catch cannot fall.** On 2026-10-22
the same 17 record movements flipped it to `watch`, which requires the upper bound to reach
90% — i.e. a much smaller or differently composed recent window than the 21 records it
holds now.

**Recorded, not chased**, following the precedent of the holdout-optimism note. The
plausible causes are the denominator work of 2026-10-23 to 2026-10-25 — `drift.anchor_fdr`,
the scope curation — and *not* the chance-pair test, which is bounded to probe-bearing
assays while this one is conventional. Nothing here says which, and the figure to cite is
the one above.

## It is not a harness artefact, and this was the case where it might have been

M1 changes penalties, so frozen candidate selection — the replay's one approximation — was
a live concern here in a way it was not for S3a. So the decisive archive was **really
rescreened** under M1, not replayed: taxid 195944, all four of its archives, 7,904 records.

> **Replay versus real rescreen under M1: 0 disagreements on 7,904 records.**

That is the harness's third independent validation, and the first on a strategy that
changes a penalty rather than a threshold or a call class.

## What M1 buys on the panels: seven rescues, nothing lost, no specificity cost

| panel | S0 wrong | M1 wrong | M1 + S3a wrong | M1 rescues |
|---|---:|---:|---:|---|
| forslund-1999-fap | 15 | **10** | 10 | HPV67, HPV40, HPV72, HPV29, HPV15 |
| barrett-1993-morbillivirus | 3 | **1** | 1 | dolphin_morbillivirus, rinderpest_KabeteO |
| meyer-1997-ati | 1 | 1 | 1 | — |
| rebelo-2011-mycoplasma | 0 | 0 | 0 | — |
| ahmed-2020-leptospira | 5 | 5 | **7** | — |
| rahn-1992-salmonella-invA (control) | 0 | **0** | 0 | — |
| **total** | **24** | **17** | **19** | |

**M1 loses no panel row anywhere**, and the Rahn control is unchanged at 0 wrong, which
reproduces the 2026-10-21 finding of zero specificity cost.

One difference from the record worth naming: `docs/journal/2026-10-21-M1-identity-aware-penalty.md`
reported Barrett's 3 of 3 false fails rescued, and today it is **2 of 3**.
`PPRV_Nigeria75_1` stays `fail` under M1 where it was rescued then. So the panel benefit is
7 rows, not 8.

The two rows M1+S3a loses are S3a's, not M1's — `L_mayottensis` and `L_alexanderi` on the
probe panel, documented in `docs/journal/2026-10-26-s3-chemistry-switches.md`.

## S4 combined, and the independence it shows

M1 under S3a changes exactly two tier-2 rows, and both are S3a's: the influenza Matrix-gene
gain at 2010-05-30 and the neutral `RANAVIRUS_..._MCP_Pallister_2007` move at 2017-07-13.
Documented failures caught is 6/11 = 55% against S0's 5/11 = 45%, PPV 3/10 = 30% against
2/9 = 22%, false alarms unchanged at 5/32 = 16%, catches lost 0.

So **M1 and S3a are independent**: M1 contributes the panel rescues and no tier-2 movement,
S3a contributes the tier-2 catch and no panel rescue. Together, panels go 24 to 19 and
failures caught 45% to 55%.

## What this does and does not establish

**It does not establish that M1 is right.** The tier-2 set has 49 cases that collapse to
about seven independent failure events, and its headline intervals span tens of points.
"M1 changes zero rows" is a strong statement about a weak instrument. M1 is **no longer
refuted by the evidence that refuted it**, which is a different and smaller claim than
being supported by evidence.

**What it does establish is that a closed decision rests on a measurement that no longer
reproduces.** `docs/journal/2026-10-22-M1-tier2.md` concludes that "the G:T/T:G discount and the
Leucocytozoon catch are incompatible under the `budget` engine at any value worth having.
This is not a tuning problem to come back to with a better number; it is measured and
closed." The incompatibility was real when measured and is not visible today. That
conclusion should be marked as superseded rather than cited, and whether `mispair_penalty`
is re-taken is a maintainer's decision.

Two things to weigh, and I am not weighing them:

- The seven panel rescues are type-level wet-lab evidence from two independent papers, and
  the conflict `docs/journal/2026-10-22-M1-tier2.md` describes as "three bench panels and one
  documented field catch disagree about the same wobble" now has nothing on the field-catch
  side of it.
- The reason it has nothing on that side is that one assay's recent window grew, not that
  any new evidence arrived about the wobble. A decision re-taken on that basis is a decision
  resting on a denominator change, and the denominator is the layer this project has
  repeatedly found to be its weakest.

## Where the ladder ends

Four rungs, all measured, none shipped.

| | verdict | tier-2 catches lost | panels (24 at S0) |
|---|---|---|---|
| S1 serial engine | **rejected** | 2 | no clean cell exists |
| S2 smooth decay | **rejected** | 4, incl. the only drift ground truth | no clean cell exists |
| S3a probe switch | **maintainer decision** | 0 | 26 (loses 2) |
| S3b conventional terminal | **inert** | 0 | 24 (no change) |
| S4 = M1 | **maintainer decision** | 0 | 17 (rescues 7) |
| S4 = M1 + S3a | **maintainer decision** | 0 | 19 |

S5 stays gated: it needs at least 40 within-family bench negatives and there are 11.

The two candidates worth a decision are the two that do not loosen uniformly. Both failed
candidates failed by loosening, and both died on the same ten Forslund negatives — which
remain the binding constraint on this whole axis, and a corpus problem rather than a
modelling one.
