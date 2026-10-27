# The held-out set is spent, and it rejected M1 on the half the development set could not see

**THE HELD-OUT SET HAS NOW BEEN READ. It is spent.** `docs/validation-cases-heldout.tsv`
was consulted once, on 2026-10-26, on the maintainer's instruction, for the one decision it
was reserved for: whether to merge `experiment/2026-10-26-m1-proposed`. No future candidate
can use it. Closing a new one needs new cases.

**Outcome: M1 is REJECTED. Do not merge the branch.**

## What was pre-registered, and where my pre-registration fell short

Before running anything I wrote: *M1 merges only if the held-out set loses no documented
catch.* **By that criterion M1 passes.** Documented failures caught is 4/9 on both tables
and no catch is lost.

**That criterion was narrower than M1's own documented gate, and the narrow version is not
the one that should decide.** `docs/2026-10-21-M1-shipped.md` set the gate when M1 first
shipped, and `docs/2026-10-22-M1-tier2.md` applied it when M1 was reverted: *"caught
failures do not fall **and no works/partial case newly disagrees**."* Two halves. I
pre-registered the first and omitted the second. The gate predates today, it is the
project's, and it is the standard this candidate has already been judged against once, so
it is the standard here.

**M1 passes the first half and fails the second.**

## The result

Three of the 34 held-out cases change:

| | case | as of | shipped | M1 |
|---|---|---|---|---|
| **new disagreement** | `Morbillivirus_including_CDV_P_gene` (`works`) | 2014-03-01 | `low coverage` / weaker | **`declining` / DISAGREES** |
| credit moves | `PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999` (`fails`) | 2022-10-18 | `declining` / agrees | `low coverage` / agrees |
| credit moves | `Pan_HERPES_dsDNA_Polymerase_round2` (`fails`) | 2021-08-05 | `declining` / agrees | `low coverage` / agrees |

Headline figures, held-out set:

| | shipped | M1 |
|---|---|---|
| documented failures caught | 4/9 = 44% | 4/9 = 44% |
| caught by the drift flag itself | 3/9 = 33% | **1/9 = 11%** |
| precision of `declining` | 3/4 = 75% | **1/3 = 33%** |
| working assays called declining | **0/17 = 0%** | **1/17 = 6%** |

So the same four failures are still caught, but two of them are now credited to `low
coverage` rather than to the drift flag, the drift flag's precision falls from 75% to 33%,
and **the shipped rule's perfect false-alarm record on this set, 0 of 17, is broken.**

## The false alarm is real, not an artefact of the replay

This mattered enough to check, because the held-out verdicts were computed from the M1
replay table and the replay is known to be pessimistic — under-crediting M1 is exactly how
a replay could manufacture a false `declining`.

`Morbillivirus_including_CDV_P_gene` was **not** among the 17 assays rescreened for the
earlier confirmation, so it was rescreened now: all 13 archives, 37,522 records, under the
M1 config.

> **0 call disagreements and 0 reason disagreements against the replay**, on all 37,522
> rows. 257 penalty disagreements, all replay-pessimistic again. Since a drift verdict is
> computed from calls and not from penalties, the verdict is the same either way.

The false alarm is M1's, not the harness's.

## The mechanism, and it is a finding about the drift model rather than about M1

| | recent | baseline | change from baseline | status |
|---|---|---|---|---|
| shipped | 64.9% of 37 | 73% | −25% to +6% | `low coverage` |
| M1 | **67.6%** of 37 | — | **−43% to −14%** | **`declining`** |

**M1 makes the recent window BETTER, 64.9% to 67.6%, and that is what turns the assay
`declining`.** It lifts the baseline years by more than it lifts the recent window, so a
change that read as "no measurable fall" becomes a measurable one. The decline is
manufactured by raising the baseline, not by the recent window deteriorating.

That generalises beyond this candidate and is worth stating on its own:

> **A uniform loosening can manufacture a `declining` verdict.** Every candidate on the
> 2026-10-26 ladder that loosened was assumed to cut flags, and the test plan says so
> outright: "a change that only loosens will always cut flags; that is not evidence." That
> is true of *coverage* flags and false of *drift* flags. A loosening that favours the
> baseline over the recent window moves an assay toward `declining`, and nothing in the
> ladder's reasoning anticipated it.

It is also the same failure mode M1 showed in 2026-10-22, when the gate was "violated on
both counts" and the second count was the Paramyxovirinae `works` case at 2024-12-26 going
weaker to DISAGREES. **M1's characteristic defect is manufacturing a false `declining`, and
it is reproducible across two independent case sets four days apart.** What changed is only
that the development set stopped showing it.

## What this says about the development set, which is the real lesson

On the development set today, M1 changes **zero** of 49 rows and rescues 7 bench-panel false
fails at no measured cost. That was a clean result and it was not enough.

- The development set has been read many times and informed several decisions, so a
  candidate that survives it has partly been selected on it.
- The held-out set had never been read, and it found M1's known defect on the first look.
- The defect was never subtle. It is the same one the 2026-10-22 revert recorded. The
  development set simply no longer contains a case that exhibits it, because one assay's
  recent window grew.

**That is what the held-out set was for, and it worked.** It cost one use to find out, which
is the price it was always going to charge.

## Disposition

- **`main` is unchanged** and ships `mispair_penalty: {}`, as it has since 2026-10-22.
- **`experiment/2026-10-26-m1-proposed` is not merged**, and is kept as the record of what
  was proposed and why it was refused. Its config comment now records the rejection.
- **`docs/2026-10-22-M1-tier2.md`'s verdict stands after all**, though not its reasoning:
  the Leucocytozoon incompatibility it named is genuinely gone, and the decision it reached
  is confirmed by a case it never saw. Its "measured and closed" sentence remains superseded
  in its detail and is now right in its conclusion.
- **The held-out set is spent.** `docs/2026-10-24-heldout-candidates.md` records that
  literal oligo search over Europe PMC is exhausted, so new cases need a different
  instrument. That is now a blocker rather than a backlog item.

## What M1 would still need

Not a better number. The 7 bench-panel rescues are real wet-lab evidence and they still
disagree with the field catches, which is the conflict `docs/2026-10-22-M1-tier2.md`
describes as "three bench panels and one documented field catch disagree about the same
wobble". Today it is three bench panels against one documented false alarm instead, on a
different assay.

What would change the answer is a rule that discounts the wobble **without lifting the
baseline relative to the recent window** — which means the discount has to be conditional on
something other than position and identity alone. That is C2's territory, and C2 is gated at
11 within-family negatives against 40.
