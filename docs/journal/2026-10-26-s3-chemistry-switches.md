# S3: the chemistry axis carries signal, on one side only, and the first candidate worth a decision

Part 1 S3 of `docs/journal/2026-10-24-scoring-strategy-test-plan.md`: two hand-set per-chemistry
switches, tested alone and then together. Pre-registration in
`strategies/s3a-probe-reduced-not-detected.yaml`,
`strategies/s3b-conventional-terminal-is-reduced.yaml` and `strategies/s3-both-switches.yaml`.
**Nothing shipped.**

S3 was specified as a probe of the mechanism, not as a candidate to ship: "it is cheap and
tells whether the chemistry axis carries signal before a model is built on it." It
answers that question, and the answer is asymmetric.

## The numbers

| | S0 shipped | S3a probe switch | S3b conventional switch | S3 both |
|---|---|---|---|---|
| documented failures caught | 5/11 = 45% | **6/11 = 55%** | 5/11 = 45% | 6/11 = 55% |
| among the cases it judged | 5/8 = 62% | **6/8 = 75%** | 5/8 = 62% | 6/8 = 75% |
| PPV of `declining` | 2/9 = 22% | **3/10 = 30%** | 2/9 = 22% | 3/10 = 30% |
| working assays called declining | 5/32 = 16% | **5/32 = 16%** | 5/32 = 16% | 5/32 = 16% |
| tier-2 catches lost | — | **0** | 0 | 0 |
| panel rows lost | — | **2** | 0 | 2 |
| calls moved | — | 112,977 | 251 | 113,228 |

Credible intervals, since every one of these spans tens of points: failures caught goes
from (20%, 73%) to (27%, 80%), and among the cases judged from (29%, 88%) to (41%, 94%).
**These deltas are inside the noise of this development set and the intervals say so.** The
case for S3a is the named mechanism and the named case, not the aggregate.

## S3a: the probe switch gains a catch, and costs no false alarms

A `reduced` call does not count toward the detected share for the 51 probe-bearing
entries. The mechanism is wave 3's influenza case: for a hydrolysis probe, detection *is*
the probe, so a probe that binds badly reports late or not at all. A primer that binds
badly still makes product, which is why `reduced` counting as detected is right for a
primer and wrong for a probe.

**It fixes exactly the case it predicted it would.**
`INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` at 2010-05-30 is a documented failure
that the shipped rule calls `stable` — a miss of the kind the tool exists to prevent. Under
S3a it reads `declining / agrees`.

**And it costs nothing in false alarms.** `working assays called declining` is 5/32 = 16%
under both. That is the result that makes S3a different from everything else in the ladder:
S1 and S2 each bought agreement on working assays by destroying failure detection, and this
buys failure detection without paying on the other side. It is the only rung that tightens,
and a tightening candidate's extra flags are evidence rather than the artefact a loosening
always produces.

One other case moves, neutrally: `RANAVIRUS_..._MCP_Pallister_2007` at 2017-07-13 goes
`stable / weaker` to `watch / weaker`.

## S3a's cost, named: two published positives on the one probe panel

**It fails its own pre-registered kill criterion.** That criterion was "any documented
catch lost", and two are:

| panel | row | bench | S0 | S3a |
|---|---|---|---|---|
| ahmed-2020-leptospira | `L_mayottensis` | band | `reduced` | **`fail`** |
| ahmed-2020-leptospira | `L_alexanderi` | band | `reduced` | **`fail`** |

Measured, not reasoned: every other panel is untouched, because every other panel's assay
is `conventional`. Panel errors go 24 to 26 in total, all of it on this one panel, 5 wrong
to 7.

The reading is forced by the switch's own semantics and is not a choice: if a `reduced`
probe call is not a detection, then predicting one where the bench saw a band is a false
negative. There is no offsetting gain available on these panels — the switch can only turn
`reduced` into `fail`, and the Leptospira panel has no `no_band` row scored `reduced` for
it to fix.

**Two things a maintainer should weigh, and I am not weighing them.**

- `L_mayottensis` is solid against the panel's own substitution rule: 28 records, all
  `reduced`. `L_alexanderi` is mixed, 5 `reduced` against 2 `detect`, so its
  representative was chosen by the modal rule and a different rule would have hidden the
  loss.
- Both rows come from a panel built on 2026-10-26 with species-level substitutions for
  strains, disclosed in its header. The influenza case it gains is in
  `docs/validation-cases.tsv` and has been there throughout.

So the trade is one documented assay-level failure caught against two documented
type-level positives missed, on the same chemistry, both small and both named. Every other
candidate in this ladder lost catches *and* got worse. This one does not, which is why it
is a decision rather than a rejection — and by the standing rule as written, it is
rejected.

## S3b: inert, and that is the finding

For conventional chemistry a 3'-terminal mismatch alone becomes `reduced` rather than
`fail`. It moves **251 calls** out of 2.7 million and **changes no verdict anywhere**:
every tier-2 figure is identical to S0 to the digit, and every panel is unchanged.

That is a real answer to a question `ROADMAP.md` Phase 2 has carried since 2026-10-23.
`terminal_mismatch_fails` is a qPCR-strength rule applied to 155 conventional entries, and
the roadmap says it "almost certainly inflates `fail` across the conventional majority".
**Measured, it inflates `fail` by 251 records and moves nothing.** The rule is not doing
the damage the roadmap attributes to it.

The reason is the arithmetic the Leptospira panel already predicted before this ran: a
record carrying a terminal mismatch almost always carries others, and the others alone
clear `reduced_max`. The lone-terminal-mismatch case the switch exists for is rare. S3b's
own pre-registration predicted it would not rescue the Leptospira five for exactly that
reason, and it is right, twice over — those penalties are 4 to 11.5 against a bar of 3.0,
and that assay is a hydrolysis probe, which this switch does not touch at all.

> **One caveat on S3b that matters more than its result.** The switch does what its name
> says only because `primer_3prime_penalty` 3.0 **equals** `reduced_max` 3.0, so a lone
> terminal mismatch lands exactly on `reduced` instead of `detect`. That is the same
> coincidence M1 tripped over. Change either number and this candidate silently becomes a
> different one.

## S3 combined: no interaction, as predicted

113,228 calls move, which is exactly 112,977 from S3a plus 251 from S3b, and every tier-2
figure equals S3a's. The two switches are confined to their own chemistries and do not
reach each other. That was the prediction and it is confirmed.

## What this means for the ladder and for C2

**The chemistry axis carries signal on the probe side and no measurable signal on the
conventional terminal-mismatch side.** That is what S3 was built to find out, and it is
directly useful to the Bayesian C2 model, whose whole structure rests on chemistry as a
hierarchical intercept: the probe half of that structure is supported by evidence, and the
conventional terminal-mismatch half is not supported by anything measured here.

Part 3 of the test plan forbids hand-fitting a full `by_chemistry` table if C2 is going to
happen. Nothing here does that: these are two switches, and one of them turned out to do
nothing.

**S4 is now unavailable as specified.** It was "M1 re-tested under S1+S2+S3", on the
reasoning that `primer_3prime_penalty` 3.0 equalling `reduced_max` 3.0 is a coincidence
that disappears under serial gates. S1 and S2 are rejected, so there are no serial gates
and no decay curve to re-test M1 under, and the coincidence is still there — S3b depends on
it. S4 needs re-specifying against `budget` plus S3a, which is a different experiment from
the one written down.

## Method notes

- S3a cannot be an overlay. `drift.YearStats.detected` is `detect + reduced` in code with
  no config key and no per-chemistry variant. It is priced by rewriting those rows to
  `fail`, which is **arithmetically identical** for drift rather than an approximation:
  `detected` is `detect + reduced` and `evaluable` is `detect + reduced + fail`, so moving
  a row from `reduced` to `fail` takes it out of the numerator and leaves the denominator
  alone. Shipping it means a per-chemistry `detected` in `drift.py`.
- The chemistry names in a strategy are checked against the registry's own enum, because a
  typo would switch nothing and the run would read as "the chemistry axis carries no
  signal", which is the opposite of the truth.
- Candidate selection is frozen in the full-table price, as always. S3a does not change any
  penalty, only which call class a row lands in, so for this candidate the approximation is
  narrower than usual: nothing it does can reorder candidate amplicons.
