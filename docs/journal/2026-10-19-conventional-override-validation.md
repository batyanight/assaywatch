# Conventional-PCR scoring override: tier-2 validation

**Date:** 2026-10-19
**Decision:** reverted. `scoring.by_chemistry` is back to `{}` in `config.yaml`.
**Override tested** (committed live in `c15a3b7`, 2026-10-18):

```yaml
by_chemistry:
  conventional:
    terminal_mismatch_fails: false
    primer_3prime_penalty: 2.0
    reduced_max: 5.0
```

## Why it was reverted before testing

`c15a3b7` and `f321201` justified the override with "87 -> 44 assays flagged for
drift, 0 new drift flags, zero regressions". That measures nothing. Loosening the
scoring can only turn `fail` into `reduced`, so it cannot create a flag, and "0 new
flags" holds for any relaxation at all. Fewer flags is the goal only if the flags
removed were false. That is what `docs/validation-cases.tsv` exists to check, and
the `config.yaml` comment above `by_chemistry` requires that check before anything
is filled in. The commit also left 11 tests failing: the hand-worked fixture
expectations in `tests/fixtures/manifest.tsv` (Annis 2004, Van 1992) and
`tests/test_per_chemistry_scoring.py`.

## The test

`scripts/retrospective.py --cases docs/validation-cases.tsv` on two existing call
sets, with the same code, registry and drift thresholds:

- `results/2026-10-17/calls.tsv.gz`: scored **without** the override
- `results/2026-10-18/calls.tsv.gz`: scored **with** it (21:44 run; 133,190 `reduced`
  calls carry penalty > 3.0, which only `reduced_max: 5.0` permits; the 10-17 set has none)

Caveat: the two runs were also one day apart in code (`winning_pair`, timing
instrumentation). Neither change touches scoring, but a rescreen of both configs
on one archive snapshot would be the clean A/B comparison.

## Result

| outcome | without | with |
|---|---:|---:|
| `fails` cases, tool agrees (failures caught) | **5** | **2** |
| `fails` cases, tool disagrees | 3 | 6 |
| `works` cases, tool agrees | 9 | 14 |
| `works` cases, tool disagrees | 5 | 2 |
| `partial` cases, tool agrees | 2 | 1 |
| `partial` cases, tool disagrees | 2 | 3 |
| total disagreements | 10 | 11 |
| undecided | 17 | 17 |

The ten cases that changed:

| assay | as of | expect | without | with |
|---|---|---|---|---|
| Paramyxovirinae L round2 | 2019-02-01 | fails | declining (agrees) | stable (**misses**) |
| Papillomavirus L1 Forslund 1999 | 2011-06-14 | fails | declining (agrees) | stable (**misses**) |
| Pan-hemoparasite cyt b Hellgren 2004 | 2016-12-31 | fails | declining (agrees) | stable (**misses**) |
| Coronavirus RdRp Lan 2010 | 2021-08-27 | partial | low coverage (agrees) | declining (disagrees) |
| CMV gB | 2007-07-20 | works | low coverage (weaker) | stable (agrees) |
| CMV gB Virol | 2007-07-20 | works | low coverage (weaker) | stable (agrees) |
| Paramyxovirinae L Tong round1 | 2024-12-26 | works | declining (disagrees) | stable (agrees) |
| Coronavirus RdRp Lan 2010 | 2020-01-08 | works | declining (disagrees) | stable (agrees) |
| Enterovirus VP3/VP1 round2 | 2018-09-30 | works | declining (disagrees) | stable (agrees) |
| Pan-herpes polymerase | 2018-11-07 | works | watch (agrees) | stable (agrees) |

## Reading

The override is a uniform loosening, and it trades sensitivity for specificity at a
bad rate. It fixes three false alarms on `works` assays and loses three of the five
documented failures the tool was catching. Overall disagreement gets slightly worse
(10 -> 11). For a tool whose job is to flag assays that have stopped working,
missing Forslund and Hellgren costs more than the false alarms it removes.

The false alarms it does fix are real. Paramyxovirinae Tong, Coronavirus Lan, and
Enterovirus round2 are degenerate pan-family primers that the default scoring
penalises like a TaqMan probe. So the direction of the change has support;
applying all three numbers to every conventional assay does not.

## What would be worth testing next

Each is its own tier-2 run against the same cases, one change at a time, so the
effect of each knob is visible:

1. **`terminal_mismatch_fails: false` alone.** This is the one with literature behind
   it (Kwok 1990, Stadhouders 2010, cited in `config.yaml`). The 2026-10-18 VP1
   analysis in `RESUME-HERE.md` found it changes almost nothing on its own, so it
   is the cheapest to check.
2. **`reduced_max` alone, at 4.0 and at 5.0.** This is the knob that moved 133k calls,
   and so the likely cause of the three lost failures.
3. **Penalty by mismatch identity** rather than one number for every terminal
   mismatch, as the config comment describes. That needs code, not a config value.

The fixture expectations in `tests/fixtures/manifest.tsv` encode the default rules
and stay as they are until one of these passes validation.
