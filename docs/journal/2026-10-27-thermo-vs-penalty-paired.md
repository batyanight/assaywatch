# A thermodynamic predictor beats the penalty rule on the bench panels — and the margin does not survive fixing the register

2026-10-27. The first head-to-head this project has ever run between its scoring
rule and a physically grounded alternative, on the only wet-lab truth it holds.

> **CORRECTED THE SAME DAY, and the correction matters more than the original
> result.** The first run below reported p = 0.0192 with the thermodynamic arm
> computed by `primer3.calc_heterodimer`, which returns the most stable structure
> between two sequences rather than the in-register duplex — the confound this
> write-up named itself, in section 3. `thermo.duplex_tm` was then fixed to score
> the duplex base-for-base (Biopython `MeltingTemp.Tm_NN`, SantaLucia & Hicks
> 2004 with the Allawi/SantaLucia mismatch tables; no alignment search, so no
> register to get wrong), and the comparison was re-run. **The thermodynamic arm
> loses most of its margin: 92.7% against 93.9%, discordance 21-10 instead of
> 20-7, McNemar exact two-sided p = 0.0708.** It still wins more discordant pairs
> than it loses, and at this sample size that is no longer distinguishable from
> chance. So the honest headline is the one in section 1, which the fix does not
> touch: the penalty rule's errors are 23 false negatives against 1 false
> positive. Everything below is the original run; the re-run is at the end.

    python scripts/compare_thermo.py

## What was compared, and what was not

The experiment the review asked for is thermonucleotideBLAST, via PCR_strainer,
because `docs/related-work.md` concedes that PCR_strainer "wraps
thermonucleotideBLAST, so matching is thermodynamic, not a positional penalty
table", and a reviewer will name it in their first paragraph.

**That is not what ran.** `tntblast` is on bioconda for osx-64 and linux-64 but
not osx-arm64. The osx-64 build installs cleanly into an isolated env and then
refuses to execute (`bad CPU type in executable`) because Rosetta 2 is not
installed on this machine, and installing Rosetta is a system-level change
requiring admin rights. So the thermodynamic arm here is **primer3's
nearest-neighbour model**, which is already a pinned dependency
(`assaywatch/thermo.py`, primer3-py 2.3.1) and already computes a per-oligo
delta-Tm on the real binding site -- it simply ships disabled (`thermo: false`).

That is weaker evidence against the "why not PCR_strainer" question: a different
engine, and not the one that will be named. It is the same EXPERIMENT.

## The design

179 labelled outcomes over 7 papers in `docs/bench-panels/`, 122 band and 57
no_band, sequences already cached under `.tmp/bench-panels/` so this needs no
network. Every row is scored twice:

- **the penalty rule exactly as it ships** -- `screen_record`, predicted band when
  the call is `detect` or `reduced`;
- **primer3** -- the minimum delta-Tm across the oligos that found a site,
  predicted band when that is at or above a threshold.

Then **McNemar's exact test** on the discordant pairs: the rows where the two
disagree. Only those carry information about which predictor is better, and that
is what makes 179 paired rows usable where two independent accuracy estimates,
each with an interval around 20 points wide, cannot separate anything. It is also
why the 5-of-11 versus 6-of-11 deltas this project has been weighing are
uninformative -- they are unpaired, on about seven independent failure events.

**The thermodynamic arm was given an unfair advantage, deliberately.** Its one
free parameter, the delta-Tm cutoff, was chosen to maximise its accuracy on these
same rows, so its score is an in-sample upper bound while the penalty rule ran
untuned. A tie or a loss for thermodynamics would therefore have been the
informative outcome. It did not tie.

## The result

| predictor | accuracy | TP | TN | FP | FN |
|---|---:|---:|---:|---:|---:|
| penalty rule, as shipped | 86.6% | 99 | 56 | **1** | **23** |
| primer3, delta-Tm >= -12.1 C | 93.9% | 115 | 53 | 4 | 7 |

The two disagree on 27 of 179 rows. The penalty rule is right and primer3 wrong
on 7; primer3 is right and the penalty rule wrong on 20. **McNemar exact
two-sided p = 0.0192.**

Per panel, errors by each predictor:

| panel | band/no_band | penalty wrong | thermo wrong | role |
|---|---|---:|---:|---|
| `ahmed-2020-leptospira` | 14/5 | 5 | 0 | fitting |
| `barrett-1993-morbillivirus` | 7/0 | 3 | 1 | fitting |
| `forslund-1999-fap` | 60/10 | 15 | 7 | fitting |
| `meyer-1997-ati` | 8/1 | 1 | 2 | fitting |
| `meyer-1997-ati-strains` | 2/0 | 0 | 0 | fitting |
| `rahn-1992-salmonella-invA` | 23/41 | 0 | 0 | control |
| `rebelo-2011-mycoplasma` | 8/0 | 0 | 1 | fitting |

## What this says, in order of confidence

**1. The penalty rule is pessimistic, and the asymmetry is stark: 23 false
negatives against 1 false positive.** It predicts failure where the bench saw a
band, 23 times, and over-predicts success once. This is the bench review's
prediction confirmed on data: `terminal_mismatch_fails: true` is a qPCR-strength
rule applied to a registry that is three-quarters conventional PCR, where a
3'-terminal mismatch on an endpoint reaction read on a gel is frequently still a
visible band. The `ahmed-2020-leptospira` panel is the cleanest case -- its own
header records that the published positives are called `fail` on a single
mismatch at position 1 from the reverse primer's 3' terminus -- and the penalty
rule gets 5 of 19 wrong there while primer3 gets none.

It also means the direction of the project's standing caveat is right: a `fail`
is weak evidence and a `detect` is strong. The 1 false positive is the whole
basis for that, and it survives.

**2. Rahn is a control and behaves like one.** Both predictors get all 64 rows
right, because its 41 negatives are other genera with no target gene at all, so
nothing anchors. Its own panel file says it "CANNOT bound a relaxation of
reduced_max", and this confirms that: it separates nothing. The informative rows
are the 16 within-family negatives, as the Bayesian plan already says.

**3. The comparison is confounded, in primer3's favour, and the confound is a
known bug.** `thermo.duplex_tm` calls `primer3.calc_heterodimer`, which returns
the most stable structure between two sequences rather than the in-register
duplex. **99 of 179 rows are off-register** by this script's own check -- a
majority. An off-register alignment finds a shifted, shorter, near-perfect duplex
and so reports an optimistically SMALL |delta-Tm|, which pushes primer3 toward
predicting a band. The panels are band-heavy, 122 of 179, so an optimistic
predictor is flattered by them. Part of primer3's 20-to-7 advantage may be that
artefact rather than thermodynamics.

So the honest reading is not "replace the engine". It is: **a thermodynamic
predictor, even a mis-registered one with its threshold fitted in-sample, beats
the shipped penalty rule on the only wet-lab rows this project has, and the
penalty rule's errors are almost all in one direction.** Both halves matter.

## What to do next, cheapest first

> *History, as of 2026-10-27. The live list is `ROADMAP.md`, the only to-do file
> in the repository; anything below that is still open was lifted into it.*

1. **Fix the registration before trusting any delta-Tm.** Score the in-register
   duplex rather than primer3's most-stable structure. Until then the thermo
   column is least trustworthy on exactly the records that matter, and this
   comparison cannot be tightened.
2. **Re-run this with the registration fixed.** If primer3's advantage survives,
   it is thermodynamics; if it shrinks, it was the artefact. Either answer is
   worth having and costs one afternoon.
3. **Then attack the 23 false negatives directly**, which is per-chemistry
   scoring: `by_chemistry` ships empty, and `terminal_mismatch_fails: false` for
   `conventional` is the single change this result most supports. It can be
   priced as a replay over the calls table via `scripts/rescore.py`, with these
   179 rows as the arbiter.
4. **The TNTBLAST comparison is still owed**, and is now a smaller job: either
   install Rosetta 2 (a system change, needs a human), build TNTBLAST from source
   for arm64, or run it on a linux-64 box or the cluster. This script's structure
   takes a second predictor without modification.

## Caveats stated once

primer3 is a model, not ground truth; the bench labels are the arbiter. The
threshold is in-sample. 138 of 179 rows had a thermo site at all, so 41 rows
contribute to the penalty arm and not to the thermodynamic one, and are counted
as no-band for it. Three of the seven panels have no negatives at all. One panel
is 400 dpi OCR of an image-only scan, and one carries three documented
species-for-strain label substitutions. These are 7 papers, not 7 independent
measurements of PCR.

---

# The re-run, in register

Same day, same rows, same penalty arm. `thermo.duplex_tm` no longer searches for
a structure: `MeltingTemp.Tm_NN` walks the two strands position by position and
sums the nearest-neighbour terms, using the internal- and terminal-mismatch
tables where a pair is not Watson-Crick. The register is therefore exact by
construction rather than by luck.

    python scripts/compare_thermo.py

| predictor | accuracy | TP | TN | FP | FN |
|---|---:|---:|---:|---:|---:|
| penalty rule, as shipped | 86.6% | 99 | 56 | **1** | **23** |
| in-register NN, ΔTm >= -16.7 C | 92.7% | 117 | 49 | 8 | 5 |
| *(primer3 most-stable, the first run)* | *93.9%* | *115* | *53* | *4* | *7* |

The two now disagree on 31 rows: the penalty rule is right and the thermodynamic
arm wrong on 10, the reverse on 21. **McNemar exact two-sided p = 0.0708.**

**What the fix removed.** The engine change cost the thermodynamic arm 1.2 points
of accuracy and tripled the number of discordant pairs it loses, from 7 to 10. Of
the sites it can price, **71 would have been mis-registered by
`calc_heterodimer`** — so the first run's advantage was, in part, an optimistic
ΔTm on exactly the mismatched sites that decide the comparison, flattered by a
band-heavy panel. That was the confound this write-up predicted, and it was worth
about half the margin.

**What it costs in coverage.** The mismatch parameters are published for a
mismatch FLANKED BY MATCHES, so two ADJACENT mismatches have no measured term.
**32 sites cannot be priced at all** and the model now withholds the number
instead of scoring the unknown step as free — Biopython will drop it silently if
asked, and dropping it overstates stability on the most mismatched sites, which
is the same optimism in the same place as the bug being fixed. Those rows carry
`thermo_note: nn_unsupported`. Net effect on the comparison: 137 rows have a
thermo site where 138 did.

**What survives, and what does not.**

- *Does not survive:* "a thermodynamic predictor beats the penalty rule,
  p = 0.019". At p = 0.07, with the threshold still fitted in-sample and the
  thermodynamic arm therefore still flattered, these 179 rows do not separate the
  two engines. A reviewer asking "why not a thermodynamic matcher?" cannot be
  answered with this experiment, in either direction.
- *Survives untouched:* the penalty rule makes **23 false negatives against 1
  false positive**. That is a property of the penalty arm alone, which never
  changed, and it remains the strongest single argument in the repository for
  per-chemistry scoring. It also keeps the direction of the standing caveat
  right: a `fail` is weak evidence and a `detect` is strong.
- *Survives:* Rahn behaves like a control under both engines (the in-register arm
  gets 1 of its 64 rows wrong, against 0 before), and the Leptospira panel is
  still where the penalty rule loses most — 5 of 19 wrong, against 3 for
  thermodynamics.

**And one thing is now cheap that was not.** The thermo column can be believed on
the records that matter, so the next question — does `terminal_mismatch_fails:
false` for `conventional` fix those 23 false negatives — can be priced against a
ΔTm that is not lying about where the mismatches sit.
