# Bayesian methods for scoring: the plan before the code

Status: **design only, 2026-10-23. Nothing implemented.** Written in the shape of
`docs/journal/2026-10-17-estimand-plan.md`, which worked: state the design, make a falsifiable
prediction, and agree the kill-test before writing anything.

References for everything below are in `docs/related-work.md` §5 and §6.

## "Bayesian scoring" is three different projects

They share a toolkit and nothing else. Separating them is most of the work of deciding
what to do.

| | layer | replaces | cost | new deps |
|---|---|---|---|---|
| **C1** | the drift proportion | Wilson / Newcombe / the flag rule | days | none (scipy) |
| **C2** | the per-record call | the additive penalty table | a research project | maybe |
| **C3** | the validation matrix | point sensitivity | a day | none |

Recommended order: **C3 -> C1 conjugate -> C1 hierarchical -> the identity column ->
C2.** C3 is pure honesty and is already partly done (`docs/journal/2026-10-23-baseline.md`).
C1 fixes behaviour that ships today. C2 is the research contribution and is gated on a
data problem, below, that is bigger than the modelling problem.

---

## C1 — Bayesian detection proportions

### What it replaces

`drift.py` computes a Wilson interval on k detects of n evaluable, a Newcombe interval
for the change from baseline, and flags when the Wilson upper bound falls below
`detect_fraction_threshold`. `lineage.py:236` instead uses a Wald interval, which is
the bug wave 1.1 fixes.

### The model

Detection probability θ with a Beta(α₀, β₀) prior gives, after k detects of n,

    θ | k, n  ~  Beta(α₀ + k, β₀ + n − k)

Conjugate: closed form, `scipy.stats.beta`, no sampling, no new dependency (scipy is
already in the `lineage` extra), and **deterministic**, which this project's
reproducibility rule requires.

### Why it is better here specifically

**1. It fixes the extremes at the root instead of patching them.** Measured, on the
cases that actually appear in `results/baseline-2026-10-22/`:

| k/n | Wald (ships today) | Wilson (wave 1.1) | Beta-Jeffreys (C1) |
|---|---|---|---|
| 0/428 (the Usutu row) | (0.00%, 0.00%) | (0.00%, 0.89%) | (0.00%, 0.58%) |
| 0/43 | (0.00%, 0.00%) | (0.00%, 8.20%) | (0.00%, 5.64%) |
| 43/43 | (100.00%, 100.00%) | (91.80%, 100.00%) | (94.36%, 100.00%) |
| 5/5 | (100.00%, 100.00%) | (56.55%, 100.00%) | (62.06%, 99.99%) |
| 50/100 | (40.20%, 59.80%) | (40.38%, 59.62%) | (40.32%, 59.68%) |

Wilson already fixes the zero-width defect, so C1's advantage is not that — it is that
one estimator covers 0/n, n/n and everything between with no special cases, and that
the same object then answers the flag question directly.

**2. The flag becomes a statement a lab can read.** Instead of "the upper bound of the
95% interval is below 0.90", report **P(θ < 0.90 | data)**: the posterior probability
that this assay detects less than 90% of what is being deposited. Measured on real
rows from the frozen table:

| k/n | share | P(θ < 0.90) |
|---|---:|---:|
| 0/428 (Usutu lineage) | 0.0% | 1.0000 |
| 302/345 (a lineage the current rule flags) | 87.8% | **0.9081** |
| 174/238 (Bd, counting `diverged`) | 73.1% | 1.0000 |
| 174/175 (Bd as it ships) | 99.4% | 0.0000 |
| 4/5 (a sparse wildlife assay) | 80.0% | 0.8017 |

The 302/345 row is the interesting one. The current per-lineage rule — a one-sided
binomial p against 0.90 at BH-adjusted α 0.05 — **flags** it. Under a stated posterior
rule of "flag at P > 0.95" it does **not**. That is the `declining`-inflation of §F of
the evaluation, fixed by making the rule explicit rather than by tuning a margin: at
large n, testing significance against a threshold that `README.md:690` itself calls
"a judgement about tolerable surveillance loss, not a property of PCR" manufactures
flags. A posterior probability and a stated cut-off do not.

It also makes the pooled rule and the lineage rule **the same rule**, which is the root
of the inconsistency: today one is a CI bound at roughly one-sided α 0.025 and the
other a p-value at BH-adjusted 0.05, and the looser one dominates the headline.

**3. "Insufficient data" stops being a refusal.** 34 of 204 assays read `insufficient
data` and 14 `no recent data`, because below `min_records_for_drift: 15` nothing is
flagged whatever the share. The 4/5 row above shows the alternative: P(θ<0.90) = 0.80,
which is real information, is honestly short of a 0.95 flag, and is strictly more than
silence. **Sparsely sequenced taxa are this project's entire constituency**, so this is
the largest product gain in C1, not a technicality.

**4. The baseline becomes the prior.** The natural prior for the recent window is the
posterior from the earlier years. "Has it fallen?" is then one model with a time term,
or a comparison of two posteriors — which removes both the separate Newcombe machinery
and `drift.py:360`'s `ever_worked` gate, currently a bare point estimate on >= 10
records that decides `declining` versus `low coverage` and moved 14-16 assays.

### The hierarchical layer, which is the real prize

For assay *a* and lineage *l*:

    θ_al ~ Beta(μ_a · φ_a, (1 − μ_a) · φ_a)
    k_al ~ Binomial(n_al, θ_al)

μ_a is the assay's overall detection level; φ_a is a concentration (inverse
overdispersion) parameter. Three separate findings collapse into this one model:

- **Multiplicity, solved by the model rather than bolted onto it.** Lineages with few
  records shrink toward μ_a; lineages with many barely shrink. That is what BH and Holm
  are there to achieve (Gelman, Hill & Yajima 2012). It also fixes the winner's curse
  in `worst_lineage_verdict`: an argmin over 24 noisy estimates is biased low and is
  currently reported with no acknowledgement of that. The posterior answers
  `P(min_l θ_al < threshold)` *and* carries honest uncertainty about **which** lineage
  is worst — which is what the "detects only S%" notes get wrong.
- **Pseudo-replication, estimated instead of asserted.** φ_a *is* the overdispersion
  (Prentice 1986). If a lineage's records are near-identical clones, the observed
  lineage shares are more extreme than binomial sampling allows, φ_a comes out small,
  and every interval widens automatically. That replaces the footprint duplication
  check's present role — computed, found to fail on 39 of 72 flags, and printed anyway
  — with a parameter inside the model. The footprint counts can inform the prior on φ_a
  rather than being a separate report-and-ignore pass.
- **The assessability floor becomes soft.** A 32-record lineage today either clears
  `min_records_per_lineage: 30` and gets a full-confidence interval, or falls below it
  and is invisible. Shrinkage is the right shape for that boundary.

### Deterministic first, sampling only if forced

Fit (μ_a, φ_a) by **empirical Bayes** — moment-matching or marginal maximum likelihood,
then closed-form posteriors (Efron 2004). scipy-only, deterministic, and most of the
benefit. A fully Bayesian treatment of the hyperparameters needs numpyro/pymc/
cmdstanpy, which is a heavy conda addition; keep it behind an opt-in extra if it
happens at all, with the CI job that deliberately omits `lineage` as the precedent for
proving the pipeline still runs without it.

### First experiment, one afternoon, no new dependencies

Recompute every per-lineage interval in `results/baseline-2026-10-22/lineage.md` three
ways — Wald (ships), Wilson (wave 1.1), Beta-Jeffreys — into one comparison table, and
re-run `scripts/retrospective.py --cases` with the flag rule changed to
`P(θ < 0.90) > 0.95`. Report-stage, off the cached calls table, nothing rescreened.
That one table decides whether C1 earns more than wave 1.1 does on its own.

### Prediction

C1-conjugate alone will **not** move the tier-2 matrix much: it changes the extremes and
the wording, and most flagged assays are flagged on large n where Wilson and Beta agree
to within a percentage point (see 50/100 above). The gains are (a) the 302/345 class of
over-flagging, (b) the 48 assays currently refused a verdict, and (c) one estimator
instead of three. **If the matrix is the only thing measured, C1 will look like it did
nothing.** Measure the flag count, the refused count, and the 46%-flagged share too.

### Kill-test

C1 dies if the posterior flag rule reproduces the Wilson flag on every assay **and**
loses a documented tier-2 catch — i.e. if it buys nothing but a dependency on priors.
The hierarchical layer dies if the fitted φ_a implies no overdispersion (records really
are independent) or if shrinkage removes a documented catch.

### Both halves were measured on 2026-10-27, and neither kill test fired

Recorded here because this section's predictions can now be checked against numbers
rather than re-argued. `docs/journal/2026-10-27-c1-posterior-flag-rule.md` and
`-c1-second-kill-test.md` hold the detail; the short version:

- **C1-conjugate**: Wilson and Jeffreys disagree on 1 of 1,351 lineage intervals. The
  posterior flag rule (`P(θ < 0.90) > 0.95`) moves 2 of 233 statuses, both `watch` →
  `low coverage` at small n, and leaves tier-2 identical case for case. Exhaustively
  over 15 ≤ n ≤ 400 the two rules disagree on 425 of 69,581 cells and the posterior
  always flags MORE. The prediction above — "if the matrix is the only thing measured,
  C1 will look like it did nothing" — was right, and the 704 zero-width Wald intervals
  it was really about had already been fixed by Wilson on 2026-10-23.
- **The hierarchical layer** (`assaywatch/hierarchical.py`): fitted φ 0.3–11.7 on
  multi-lineage assays, intraclass correlation 0.08–0.78, so the first kill test does
  not fire — the records are nothing like independent, and that is now a parameter
  rather than a prose caveat. Driving the override from the shrunk worst lineage
  (`lineage.verdict_from: posterior`) moves **0 of 240 statuses** and leaves tier-2
  identical, so the second does not fire either. It ships beside the verdict.

Both therefore ship **off**: `drift.flag_rule: wilson`, `lineage.verdict_from: holm`.
What the layer earns is honest numbers for thin lineages — a 0.0% (0.0%–0.0%) lineage
reads 1.3% (0.0%–4.7%) — not a different decision.

### C1b — the floor the hierarchical layer cannot reach, which is where the refusals are

**The defect.** This section claimed above that "the assessability floor becomes soft"
and named "the 48 assays currently refused a verdict" as one of C1's three gains. That
is wrong, and the 2026-10-27 run is what showed it: `min_records_for_drift` is applied
to the **pooled** recent count inside `drift.finalise`, *before* any lineage is looked
at. The hierarchical layer shrinks across lineages, so it cannot reach an assay that
never gets a lineage table at all. 30 assays are refused this way (2026-10-27 run), and
for a 17-record assay there is no lineage to borrow from.

**The model.** Borrow across ASSAYS instead, within one chemistry:

    θ_a ~ Beta(μ_c · φ_c, (1 − μ_c) · φ_c)      for assay a of chemistry c
    k_a ~ Binomial(n_a, θ_a)

μ_c and φ_c fitted by the same moment-matching as `hierarchical.fit_assay`, on the
assays of that chemistry that DO clear the floor; a refused assay then gets a posterior
on its own θ_a, shrunk toward its chemistry's level, and the verdict comes from
`P(θ_a < threshold) > credibility` exactly as `drift.flag_rule: posterior` already
computes it. Nothing new is needed numerically: `hierarchical.py` and
`interval.posterior_below` are both in place, and the change is which units the
Beta-binomial is fitted over.

**Why this is the only route left.** Three alternatives were considered and are worse.
Widening the recent window is already priced (`2026-10-27-window-minimum-grid.md`): 36
months keeps every catch, and widening does not help an assay whose whole archive is 17
records. Lowering the floor was priced on the same grid: between 10 and 20 it only
trades refusals, and at 30 it refuses 20 assays for no gain. And declining to judge
remains defensible — it is what ships — but it is a refusal on the *estimator's*
terms, not the evidence's: a 17-record assay with 2 detections is not weak evidence of
drift, it is reasonable evidence, and a confidence interval simply has no way to say so.

**The cost, stated before anything is built.** This imports an assumption the
within-assay layer did not need: that assays of one chemistry are exchangeable draws
from one distribution. They are not, obviously — a pan-family consensus PCR and a
species-specific probe assay sit in the same `conventional` or `hydrolysis_probe`
bucket and have nothing else in common. So the prior does real work here, where in the
within-assay layer it mostly did not, and an assay with 17 records will be told largely
what its chemistry's other assays say. That is the trade: a verdict with a stated,
borrowed prior, against no verdict at all.

**The kill tests, pre-registered.** C1b dies if either fires:

1. **It changes a verdict that is already judgeable.** Fitted on the clearing assays
   and applied to them, it must reproduce their shipped statuses; a disagreement on an
   assay with hundreds of records means the pooled prior is overwhelming real data.
2. **It manufactures a catch tier-2 cannot confirm.** Of the 30 refused assays, the
   ones it promotes to `declining` must not include a case the literature reports as
   *working*. There are `works` cases among the refusals (Salmonella invA, Shigella
   ipaH, the pan-mycoplasma 16S, Bd), which makes this testable: a false alarm there is
   a kill, not a shrug.

**What it would be worth.** Tier-2 currently declines to judge 15 of its cases and 3 of
its 11 documented failures. Those three are the whole of the difference between "6/11
caught" and "6/8 among the cases it judged at all", and that gap is the strongest thing
anyone can say against this project's central number. C1b is the only mechanism on the
table that could close it rather than explain it.

**Not built.** Design only, 2026-10-27, by the same rule the rest of this plan follows:
a mechanism is written down with its kill criteria first, and measured before it ships.

---

## C2 — A Bayesian amplification model for the per-record call

### What it replaces

`score.py`'s additive penalty: positional weights 3.0 / 1.0 / 0.5 over windows of
5/5/rest, summed across the three oligos, thresholded at `detect_max: 1.0` and
`reduced_max: 3.0`, with `terminal_mismatch_fails: true` as a hard override.
`README.md` lists five things it already knows are wrong with this.

### The model

Model each oligo's probability of binding and extending, then combine them the way the
chemistry does:

    P(detect | record) = P(fwd ok) × P(rev ok) × P(probe reports)

    logit P(oligo ok) = β₀[chemistry] + Σ_j w(d_j) · m(identity_j) + adjacency + covariates

where `d_j` is the mismatch's distance from the 3' end, `identity_j` is the mispair
(A:A, T:G, ...), `w(·)` is a smooth decay rather than three step-function bands, and the
covariates are things the pipeline already computes and refuses to score: oligo length,
MGB versus plain probe, and the primer3 nearest-neighbour ΔTm on the real binding site.

### It answers all five admitted guesses from one structure

| `README.md`'s guess | how the model answers it |
|---|---|
| 1. the penalty is blind to which mismatch it is | `m(identity)` is an estimated coefficient, with a prior from Stadhouders 2010 |
| 2. the three oligos are summed, but they are serial gates | the product form **is** the serial-gate structure; nothing to patch |
| 3. one table serves 161 conventional and 44 probe assays | chemistry as a hierarchical varying intercept and slope, so the 44 probe assays borrow strength from the 161 instead of needing a hand-set second table. This is `by_chemistry` **estimated** rather than invented |
| 4. probe geometry is length- and MGB-blind | covariates |
| 5. mismatches add linearly | adjacency term plus a non-linear link |

It also dissolves the arithmetic coincidence that killed M1. `primer_3prime_penalty:
3.0` happens to equal `reduced_max: 3.0`, so a single mismatch two bases from the 3'
end lands exactly on the class boundary, and `docs/journal/2026-10-22-M1-tier2.md` showed the
whole G:T wobble question was decided by that coincidence rather than by biology
("a multiplier of 0.8 is not a discount"). A fitted continuous model has no such edge.

### Why Bayesian rather than plain logistic regression

Three reasons specific to this dataset, not general advocacy:

1. **Small n with separation.** If every terminal A:A in the corpus is `no_band`, the
   maximum-likelihood coefficient for that term diverges to −∞. Weakly informative
   priors are the standard fix and this is the textbook case for them (Gelman et al.
   2008).
2. **The literature carries real prior information.** Kwok 1990 and Stadhouders 2010
   measure per-mispair effects quantitatively, in a *different* assay system — so
   using them as prior means on the identity coefficients, rather than as training
   rows, is both the methodologically correct move and the Bayesian one. It also fits
   this project's existing culture exactly: `config.yaml`'s rule is that every number
   carries its justification or an admission that it has none, and **a prior is
   precisely an annotated number with a justification.**
3. **The output has to propagate.** What is wanted per record is a probability with
   uncertainty, which then has to flow into the assay-level proportion. Today the drift
   interval treats every call as known truth — the scoring model's uncertainty never
   reaches the report, which is this pipeline's one unacknowledged overconfidence. A
   posterior predictive propagates it natively.

### How it plugs into the pipeline

Per record you get P(detect) in [0,1] instead of a class. An assay's detected count
over n records is then a sum of independent Bernoullis with different probabilities — a
**Poisson-binomial** — and `chance.py:56-78` **already implements the Poisson-binomial
DP**, for the same reason (each oligo position is a coin with its own probability). So
the expected-detections distribution is computable with code that exists.

Migration path: keep the four-class call by thresholding P(detect), show the model
reproduces or beats the current calls on the bench corpus and on tier-2, and only then
let probabilities into the report.

### The data problem is bigger than the modelling problem

This is the part that decides whether C2 is a project or a wish, and the honest answer
is worse than it first looks.

`docs/bench-panels/` holds **179 labelled wet-lab outcomes, 122 `band` and 57
`no_band`** (recounted 2026-10-27; was 160/108/52 before the Ahmed panel) — a
design paper's own test panel, one genome per type or strain, with an
accession so the mismatch configuration is computable by the existing matcher. That
sounds like a training set. Measured per panel:

| panel | band | no_band |
|---|---:|---:|
| `rahn-1992-salmonella-invA` | 23 | **41** |
| `forslund-1999-fap` | 60 | **10** |
| `ahmed-2020-leptospira` | 14 | **5** |
| `meyer-1997-ati` | 8 | **1** |
| `meyer-1997-ati-strains` | 2 | 0 |
| `rebelo-2011-mycoplasma` | 8 | 0 |
| `barrett-1993-morbillivirus` | 7 | 0 |

**41 of the 57 negatives are Rahn's, and they are other genera** —
*Acinetobacter calcoaceticus*, *Aeromonas hydrophila*, *Bacillus subtilis*,
*Citrobacter freundii*, *Edwardsiella tarda* and so on. That is a **specificity** panel.
A model fitted on it learns "sequence far from the target gives no band", which is a
question `scoring.max_pair_evalue` and `chance.py` already answer, and which has
nothing to do with drift.

The negatives that actually inform a drift model are the **within-family** ones: the 10
Forslund HPV types the pan-papillomavirus consensus PCR failed to amplify (HPV1, 2, 35,
41, 44, 55, 63, 66, 71, 74), Ahmed's 5 same-genus *Leptospira* (*L. inadai*,
*licerasiae*, *wolffii*, *broomii*, *fainei*) and Meyer's raccoonpox. **Sixteen
informative negatives**, of which 15 are threshold-sensitive: Meyer's is gene-absent,
so it has no site to score and cannot bound a threshold.

Sixteen negatives cannot support ten coefficients, however good the priors. So:

> **C2's first task is not modelling. It is building the corpus.**

What to collect, and it is a well-defined literature task: design and evaluation papers
that print a **per-type or per-strain** amplification result for a consensus or
pan-family assay — the shape Forslund 1999 has. Consensus-PCR papers are the richest
seam because they routinely tabulate which types amplified and which did not, and this
registry is full of them (PREDICT panels, pan-herpes, pan-flavivirus, pan-paramyxovirus,
pan-adenovirus). Target: **60+ within-family negatives across >= 10 independent papers**
before fitting anything. `scripts/bench_panel.py` and `docs/bench-panels/*.tsv` already
define the format, so each new panel is a TSV and a header comment recording what was
read and from where.

Do this **alongside wave 4.2** (the held-out tier-2 cases). They are the same literature
sweep at two levels of resolution — assay-level outcomes for tier-2, type-level outcomes
for C2 — and reading each paper once for both is the only sane way to do it.

### The one infrastructure blocker, worth doing early and separately

`scripts/bench_panel.py:9-20` already screens a panel with the real matcher and prints
the **mispair identity** per 3'-window mismatch ("a W opposite template G prints
A:G/T:G"), so the feature extractor is most of the way written — it prints a summary
where it needs to emit a table.

But the calls table stores `fwd_mm_from_3prime` as positions ("14,6,2") and **not the
mispair identity**. Identity-aware scoring at the scale of 2.7 M rows therefore needs a
new column, which means **one rescreen (~26 min)**, since `screen.py` and the `scoring`
block are both in the screen signature (`Snakefile:122`).

Do it once, as infrastructure, independent of whether C2 ever happens. It also unlocks
per-chemistry work (wave 4.5), and it is what M1 would have needed to diagnose its own
failure without a hand forensics pass over 5,499 changed records.

> **DONE 2026-10-26** (`1fa4672`). `Call.as_row` now writes `fwd_mispairs`,
> `rev_mispairs` and `probe_mispairs` as `oligo:template@distance_from_3prime`. Two
> details this section did not anticipate: the identity is recorded for **every**
> mismatch and not only those inside `primer_3prime_window`, because a replay may weight
> identity at a different distance; and a degenerate oligo base records its own code
> (`Y:T@2`) where `bench_panel.py` expands it to `C:T/T:T`, so the two formats agree in
> meaning and not in text. The columns are deliberately kept out of
> `drift.FOOTPRINT_COLUMNS`, which must stay position-only or the duplication analysis
> regroups and published intervals move.

### Kill-test

C2 dies if, under **leave-one-panel-out** cross-validation — leave out a whole paper,
never a row, because rows within a panel are not independent — it does not beat the
current additive rule on the metric this project already cares about: no documented
tier-2 catch lost, and the FAP and Barrett false `fail`s reduced. Those two are the
specific target; they are what M1 was trying to fix and what `config.yaml:75` records
as still standing.

C2 is also **killed before it starts** if the corpus task above stalls below ~40
within-family negatives. Say so now, so that a model fitted on 16 is never defended on
the grounds that the work was already done.

> **The two numbers in this file are a FLOOR and a TARGET, not a disagreement
> (reconciled 2026-10-26).** `docs/journal/2026-10-24-scoring-strategy-test-plan.md` gates S5 at
> "at least 40 within-family negatives across several independent papers", which is the
> ~40 kill floor in the paragraph above, not a different standard. The "60+ across >= 10
> independent papers" in the corpus section is the collection *target*: the count at which
> fitting ten coefficients is reasonable rather than merely not fatal. So 40 is where C2
> stops being dead and 60 is where it starts being defensible, and a corpus of 45 means
> "fit it and report the interval honestly", never "the gate is met". Today the count is
> **11**, so both readings agree C2 is not started.

---

## C3 — Bayesian treatment of the validation matrix

Cheapest item here and the one that most improves the project's honesty. Partly done
already in `docs/journal/2026-10-23-baseline.md`, which records:

| quantity | point | 95% credible interval (Jeffreys) |
|---|---:|---|
| `fails` caught, 5/11 | 45.5% | **(20.0%, 73.0%)** |
| `fails` caught among decided, 5/8 | 62.5% | (29.5%, 88.1%) |
| PPV of `declining`, 2/9 | 22.2% | **(4.9%, 54.4%)** |

Printing those intervals makes the overfitting argument **quantitative instead of
rhetorical**. A PPV whose 95% interval runs from 5% to 54% cannot adjudicate a
"-1 FP, 0 TP" threshold change (`config.yaml:542`), and seven settings have been
accepted or rejected on exactly that kind of delta. The interval says so in one line
where three paragraphs of caveat did not.

Remaining C3 work:

- **Treat `undecided` as missing data, not as a dropped row.** 3 of 11 `fails` and 11 of
  32 `works` are undecided — 15 of 49 cases. Modelling the probability that a case is
  *decidable* alongside the probability it is *correctly called* is cleaner than
  reporting four cells and comparing one.
- **Make threshold selection a decision problem with a stated loss.**
  expected loss = (cost of a missed drift) × P(miss) + (cost of a false alarm) ×
  P(false alarm). The project already has the instinct without the formalism:
  `docs/journal/2026-10-21-drift-window-calibration.md:58-90` overruled its own grid optimum
  *because the loss function was wrong* — as-of scoring cannot see the slow-to-warn
  cost. Writing the loss down would have made that argument formal rather than
  narrative, and it is the same move that would settle `detect_fraction_threshold: 0.90`.
- **Put the credible intervals in `config.yaml`'s header and the report**, beside the
  point estimates, so nobody reads 5 of 11 as a measurement.

**No kill-test.** C3 reports uncertainty that already exists; there is no version of it
that makes the project less honest.

---

## Interaction with the main plan

**Read this before doing wave 3.1-3.3.**

- **3.1 (BH -> Holm): do it.** One line, and C1-hierarchical is months away. It is a
  stopgap and should be labelled one in the commit message.
- **3.3 (non-inferiority margin): skip it, defer to C1.** Partial pooling addresses the
  same over-flagging better, and the 302/345 row above shows a stated posterior cut-off
  does the job without a new tunable. Tuning a margin on the 49-case set is exactly the
  pattern wave 4 exists to stop.
- **Wave 4.5 (per-chemistry scoring): C2 subsumes it.** `by_chemistry` hand-set per
  chemistry is the frequentist version of a varying intercept. If C2 is going to happen,
  do not hand-fit two tables first.

## Risks, stated up front

| risk | mitigation |
|---|---|
| **Priors become the thing a reviewer attacks.** | Every prior gets a one-line citation or an explicit "weakly informative, chosen to be conservative", in `config.yaml` beside the number, exactly as the thresholds do now. This project's culture is unusually well-suited to defending priors; it has been annotating numbers since day one. |
| **Determinism.** The repo pins that the same archive gives the same answer every run (`subcluster.py`: "an unstable label would make the drift report diff noisily from run to run"). MCMC does not. | Prefer conjugate updates and empirical Bayes, which are deterministic. Where sampling is unavoidable: fixed seed, fixed iteration count, and a committed posterior summary so the report rebuilds without re-sampling. |
| **Dependencies.** C1-conjugate and empirical Bayes need only scipy. Hierarchical MCMC needs numpyro/pymc/cmdstanpy. | Keep sampling behind an opt-in extra and keep the closed-form path as the one the pipeline uses. The CI job that omits `lineage` is the pattern to copy. |
| **Scope.** C2 could absorb the whole winter. | C3 and C1 are weeks and ship value immediately. C2 is gated on the corpus task, which is explicitly a literature sweep shared with wave 4.2, and on a kill-test agreed here rather than later. |
| **Replacing a rule that is understood with a model that is not.** | Both C1 and C2 keep the existing output shape during migration — threshold the posterior, threshold P(detect) — so every change is diffable against `results/baseline-2026-10-22/`. Never ship a Bayesian layer without that diff. |

## What C2 would mean for the project's standing

Worth saying plainly. GoPrime (`docs/related-work.md` §1) already fits a linear model of
real-time PCR performance from sequence, for one virus. A hierarchically fitted,
identity-aware, chemistry-varying amplification model, calibrated on published
per-type bench panels and validated against documented assay failures, applied to a
curated registry of wildlife assays, is a larger and more defensible contribution than
the registry alone — and it converts this project's most criticised component,
penalties set by eye, into its strongest.

It is also what would let the report say

> P(this assay detects the circulating lineage) = 0.62 (0.48-0.75)

instead of `declining`, which is the difference between a number a lab lead can act on
and a word they have to interpret.
