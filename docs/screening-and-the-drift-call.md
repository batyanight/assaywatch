# Screening and the drift call: the technical reference

Moved out of `README.md` on 2026-10-31, unchanged, when the README was cut to a
front page. This is the reference version, with every measurement and every
caveat. The website's
[Scoring methods](https://batyanight.github.io/assaywatch/scoring/)
is the same material written for a reader rather than a maintainer; where the two
disagree, this file is the one to fix first, because it carries the numbers.

## Screening

```bash
assaywatch screen registry/CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004.yaml \
    tests/fixtures/records.fasta -o calls.tsv
```

`--workers N` screens one archive across N processes; the output is byte for
byte the same as with one worker (assays in registry order, records in archive
order), and memory stays at a few batches of `--chunk-bp` bases however large
the archive is.

One row per (assay, record) with the call, the total penalty, the amplicon
coordinates, and each oligo's mismatches expressed as distance from its 3' end
(1 = the terminal base). Four calls:

| call | meaning |
|---|---|
| detect | total penalty <= `detect_max` |
| reduced | <= `reduced_max`; amplifies but expect a Ct shift |
| fail | above `reduced_max`, a mismatch at a primer's 3'-terminal base, or no probe site inside the amplicon |
| indeterminate | more than `max_ambiguous_per_oligo` undetermined record bases under an oligo |
| no_amplicon | no primer pair in the right orientation and size range |

`no_amplicon` and `indeterminate` are kept separate from `fail` on purpose: a
partial record, or one full of ambiguity codes, is a sequence-quality problem
rather than an assay problem, and mixing the two would make every rough
GenBank entry look like drift.

**A product has to be the size the assay says it is.** `amplicon.declared_tolerance`
(0.25, on since 2026-10-14) constrains a call to the assay's own `amplicon_bp`,
within a quarter either way, instead of only to the global 50–3000 bp window. A
1931 bp product is not a 194 bp assay amplifying: the extension time, probe
geometry and efficiency belong to something else. The tolerance is measured
rather than chosen — over the 2026-10-07 run, |observed/declared − 1| has a knee
at about 0.2 and flattens past it, so 0.25 keeps 99.3% of the calls that had a
declared size. Applied to that run it would move 59,141 rows out of the
denominator, 54,966 of them `fail`, which is the correction running in the
pessimistic direction: most oversized products were being counted against the
assay. It does mean a mistranscribed `amplicon_bp` now voids an assay's calls instead
of being inert, so `scripts/check_amplicons.py` is the thing to run when an
assay's numbers collapse.

What the filter mostly catches, though, is not a wrong number but **two products
in one entry**. The three assays whose measured product sat furthest from their
declared size each hold a second amplicon in `oligos.alternates` — a nested
secondary pair, or an alternative reverse — and `score.oligo_pools` treats
alternates as interchangeable members of one pool, which is right for a
consensus cocktail and wrong for a second round. Measured over the first 400
records of each archive — 290 for the nidovirus one, which holds no more —
their declared pairs give 1320, 161 and 1695 bp against a declared 1319, 163
and 1694: the stored numbers are right, and it was the alternate's product
being credited to the assay. With the filter on, the out-of-window combination
is `no_amplicon` and the screener falls back to the declared pair. 20 of 214
entries could form a second product this way. The fix is curation — one entry
per round, as the CMV gB and adenovirus polymerase assays already have.

### What the scoring rule assumes about PCR, and where it is wrong

The penalties come from one well-supported fact and several guesses, and it is
worth knowing which is which before reading a call.

**The fact.** A polymerase extends from the primer's 3'-OH, so a mismatch there
sits in the catalytic site, while one near the 5' end costs only a little duplex
stability on an oligo that has 19 other matched bases. Weighting mismatches by
distance from the 3' end is therefore the right shape (Kwok et al. 1990,
[10.1093/nar/18.4.999](https://doi.org/10.1093/nar/18.4.999); Stadhouders et al.
2010, [10.2353/jmoldx.2010.090035](https://doi.org/10.2353/jmoldx.2010.090035)).

**The guesses, in rough order of how much they matter.**

1. *The penalty is blind to which mismatch it is.* Both papers above find
   identity dominates: at the 3' terminus, A:A, A:G, G:A and C:C suppress yield
   by orders of magnitude (>7 Cq in Stadhouders), while T:G, T:C and T:T are
   nearly free (<1.5 Cq) — a T:G wobble still stacks. So
   `terminal_mismatch_fails` is right for about half of terminal mismatches and
   wrong for the rest. The *E. coli* malB result survives this because all 92
   failures are a single A→G at the reverse 3' base, which is in the severe
   class; the rule did not know that when it fired.
2. *Penalties from the three oligos are summed into one budget*, but amplification
   needs forward **and** reverse and detection needs the probe on top. Those are
   serial gates. Three trivial mismatches, one per oligo, land in the same bin as
   one near-lethal 3'-proximal mismatch.
3. *One table serves every chemistry in the registry* -- 155 conventional PCRs and 50
   probe assays on 2026-10-24. A 100-fold yield
   loss is a missed Cq cutoff in qPCR and often still a visible band after 40
   cycles of endpoint PCR. The same `fail` is printed for both.
4. *Probe geometry is length-blind, and MGB-blind.* Of the 50 probe assays here on 2026-10-24,
   20 are MGB (the other 30 are plain hydrolysis probes), and the minor-groove binder
   adds roughly 15–20 °C of Tm and makes short probes viable; such a probe tolerates
   mismatches a bare oligo of the same length would not. `--thermo` computes the real duplex ΔTm and is the better
   guide where it is available.
5. *Mismatches add linearly*, so two adjacent ones — which destroy a contiguous
   run of base stacking — are under-penalised relative to two spread apart.

None of this is hidden in code: every threshold is annotated in `config.yaml`
with its justification or an admission that it has none, and the standing
numbers are in
[docs/journal/2026-10-04-pipeline-review.md](docs/journal/2026-10-04-pipeline-review.md).
Against the 50-case development set, on the 2026-10-31 run, the tool catches **6 of 11**
documented failures and **4 of its 10 `declining` calls** were real failures
(95% CrI 15%-70%), with 4 false alarms in 32 working assays. Of the 11
documented failures, 10 are coverage gaps and **one is drift** — and that one is
caught: Yang 2014 on the influenza A M1 assay of Ward 2004, the only case in the
project where the drift flag itself caught a documented failure. Those figures
are in-sample on roughly seven independent failure events.

The three held-out sets are all spent, and they are worse than the development
set rather than better, which is the honest shape of the thing: set 1 caught 3 of
9 with no false alarms in 17; set 2 caught 2 of 3 but put 4 of 10 working assays
in `declining`; set 3 has two drift rows and caught one.
`scripts/retrospective.py --cases docs/validation-cases.tsv` prints any of them
with intervals. A call is a reason to look, not a result, and
[docs/state-of-the-project.md](docs/state-of-the-project.md) says what the output
is worth in one page.

### Degeneracy is never penalised

Each position of an oligo against a record resolves to one of three states,
not two (`iupac.base_state`):

| state | example | effect |
|---|---|---|
| match | primer `Y`, record `C` or `T` | nothing; this is what degeneracy is for |
| mismatch | primer `A`, record `S` (C or G) | scored by position, as usual |
| unknown | primer `A`, record `R` (A or G), or any record `N` | counted, never charged |

The third state is the one that matters for degenerate assays. Pan-family
primers need degeneracy precisely because they target sparsely and unevenly
sequenced taxa, and those are the records with ambiguity codes in them.
Charging an `R` or an `N` as a mismatch would tax those assays for the
submitter's sequencing quality and would make real drift indistinguishable
from missing information. It would also be wrong at the 3'-terminal base,
where a definite mismatch is fatal but an undetermined base says nothing.

Undetermined positions are reported per oligo (`fwd_ambiguous`,
`rev_ambiguous`, `probe_ambiguous`). Once an oligo's footprint carries more
than `max_ambiguous_per_oligo` of them, too little of the binding site is known
to judge and the record is called `indeterminate`. That cap also stops a run of
Ns elsewhere in a record — which matches every oligo — from being reported as a
clean amplicon.

### Degeneracy is reported instead

Not penalising degeneracy creates the opposite bias: an oligo full of N matches
everything by construction, so a heavily degenerate assay can never be seen to
drift and its `detect` calls approach a tautology. That is a property of the
assay, not of any record, so it is reported alongside the drift numbers rather
than folded into them. Every row of a screen carries `degeneracy_fold` and
`degeneracy_tier` for its assay, and

```bash
assaywatch degeneracy registry --tier severe
```

lists the assays whose in-silico coverage should be read with the most
suspicion. The severe end is the PREDICT pan-family consensus PCRs, which is
expected and is the point of them.

The headline `total_fold` multiplies every oligo, primers and probe, because
all of it is reagent that does not participate in detecting a given template,
and `log2(total_fold)` is reported as `dCq`: a first-order estimate of the Cq
delay, since the log of a product is the sum of the logs. The components stay
visible, because they fail differently. Primer dilution attacks amplification:
annealing is pseudo-first-order in primer concentration, efficiency sits in
the base of the exponential, and a deficit compounds until the reaction does
not take off. Probe dilution attacks only the readout: a hydrolysis probe is
cleaved from the amplicon and is not part of the amplification mechanism, so a
diluted probe reports a smaller share of whatever was made, which is a fixed
offset of about log2(n) cycles. An assay at 4096-fold that is all primers may
not amplify; one that is all probe amplifies fine and reports late. `dCq` is
therefore a lower bound at the high end, not a prediction.

Degeneracy is a concentration effect, not a binding effect: a pool of *n*
oligos contributes roughly 1/*n* of the nominal concentration to any one
template, which costs sensitivity rather than coverage. **Inosine is not
degeneracy.** An inosine-containing primer is one molecule that pairs
promiscuously, which is exactly why designers reach for it, and it pays no
concentration cost. The registry stores inosine as `N` in `seq` to keep that
field strict IUPAC and keeps the original in `seq_as_written`; matching and
degeneracy both read `seq_as_written`, so I pairs with C, A and T, is `unknown`
opposite G (a real but poor pair), and counts as one molecule. Reading the
PREDICT filovirus reverse primer from `seq` instead would call it 8192-fold
degenerate when it is 8-fold: the difference between an unusable assay and a
working one.

### Thermodynamics are reported, not scored

The mismatch penalty is positional. What a mismatch does to binding depends on
which mismatch it is and what surrounds it, so `--thermo` (or `thermo: true` in
config.yaml for the pipeline) adds the primer3 nearest-neighbour Tm of each
oligo on its actual binding site, and its shift from a perfect site:

| column | meaning |
|---|---|
| `fwd_tm`, `rev_tm`, `probe_tm` | duplex Tm (°C) on the record's site |
| `fwd_dtm`, `rev_dtm`, `probe_dtm` | that Tm minus the same oligo's Tm on a perfect site |
| `thermo_min_dtm` | the worst ΔTm across the assay's oligos |
| `thermo_note` | `inosine` when inosine was modelled as the base it faces (an upper bound) |

ΔTm is the column to read: absolute Tm depends on the salt and oligo
concentrations in `thermo_conditions`, which differ between protocols, and the
shift caused by the record's mismatches depends on them much less.

**Why it is reported and not scored, measured rather than asserted** (2026-10-27,
`docs/journal/2026-10-27-tntblast-head-to-head.md`): a ΔTm only means something against
the temperature the reaction ran at, and that is a property of each assay's protocol.
Run thermonucleotideBLAST — the engine PCR_strainer wraps, and so the one this question
is really about — over the 179 labelled wet-lab outcomes in `docs/bench-panels/`, and
with two free parameters fitted on those same rows it reads 64.8% against the penalty
rule's 92.7% as it ships, 58–8 on the discordant rows. Fit a separate cut per panel and
it reads 87.7%, and on the Salmonella specificity panel its separation is total. The
weakness is the single global cut, not the thermodynamics. `conditions.annealing_c`
(2026-10-27) is what would let each assay be judged at its own temperature; until most
entries carry one, a thermodynamic call would be made at a temperature the registry
invented. Degenerate
positions take the record's base when the pool has it (that pool member is the
one that amplifies), and undetermined record bases are modelled as matches, as
in scoring. On the flavivirus archive the median worst ΔTm was −5 °C for
`detect`, −12 °C for `reduced` and −17 °C for `fail`; the extra columns cost
no measurable screening time. Calls are identical with or without `--thermo`.

## Matching

`find_sites(oligo, record, max_mismatches)` returns every ungapped site on
either strand within the mismatch budget. The search is exhaustive by
construction: a 256-entry lookup table per oligo position is applied to the
record as a numpy array, giving the mismatch count at every alignment offset
in L vectorised passes, and only the offsets within budget are revisited to
recover which positions mismatched. A 25 nt oligo against a 30 kb record takes
about 5 ms; one probe-based assay against 1000 records of 1.5 kb takes under a
second.

Undetermined record bases are free when a site is *scored* but count against
the budget when it is *found*: a window of Ns is not evidence of a binding
site, and without this rule every offset in a scaffold gap matched every oligo
perfectly and the pair scoring went cubic (the first live run spent nine hours
on the Bd archive). A site with a few undetermined bases is still found and is
called `indeterminate` if there are too many to judge.

Raising `max_mismatches` can only add sites, never move or remove one, which
`tests/test_match.py` asserts along with equality against a brute-force scan
on random and degenerate sequences. Gaps are not modelled: a binding site with
an indel in it is not a working primer site, and treating it as one would
invent amplicons that do not exist.

## Fixtures

`tests/fixtures/` holds 84 synthetic records built by `tests/make_fixtures.py`:
a perfect amplicon per assay, then copies with substitutions planted at known
distances from each oligo's 3' end, plus an unrelated random record. Two plans edit both ends of one
oligo at once, which the seeded matcher that preceded the current one could
not find at all; three plant ambiguity codes, including at the 3'-terminal
base, to pin down the no-penalty rule. The expected call for every record was worked out by hand
from `config.yaml` before the scorer ran, and `tests/test_score.py` asserts
it. Regenerate with:

```bash
python tests/make_fixtures.py && pytest -q
```

## The drift call

`report.md` renders on GitHub; `report.html` is self-contained (inline SVG, no
CDN, no JavaScript) so it opens from a file:// path in a lab with no
bioinformatician. Both are written under `results/<date>/`, which is gitignored,
so a run's output stays on the machine that produced it --
`docs/example-run-2026-10-26/` is a committed copy of one, and until 2026-10-27
there was none, which made this paragraph a promise about files no reader could
open.

**What goes in the denominator.** Only `detect`, `reduced` and `fail`: records
where both primers landed in the right orientation and size range, so the call
is a statement about the assay. `no_amplicon` and `indeterminate` are counted
and shown but excluded, because a record missing the locus, or truncated, or
full of ambiguity codes says something about GenBank rather than about the
assay. Folding them in would let a bad sequencing year look exactly like drift.
`reduced` counts as detected: it amplifies, just later.

**Why intervals and not just the fraction.** A wildlife assay may have five
records in the last two years. Three failing is 40% detected, which looks
alarming and means nothing — the 95% interval runs from about 10% to 70%.
Flagging on point estimates would bury real signals under noise from exactly
the sparsely sequenced taxa this tool exists to serve. So an assay is flagged
only when the *upper* bound of its recent interval falls below the
threshold: the data must be inconsistent with the assay still working, not
merely consistent with it failing. A flagged assay is then one of two things:

* **declining**: the Newcombe interval for the change from baseline lies wholly
  below zero, the fall is at least `min_decline`, **and** the assay cleared the
  threshold in some earlier year (`drift.require_working_baseline`, on since
  2026-10-14). The share has fallen from a level that worked; that is drift.
  The last condition is what keeps the word honest: without it 14 of the 37
  assays called declining on 2026-10-07 were pan-family consensus PCRs that
  never covered the taxon they are screened against — a fall from 14% to 0% is
  a change in which clades were deposited, not an assay degrading. The test is
  per year, not on the aggregate baseline, which a long decline drags down by
  itself. Those 14 are now **low coverage**, and their note says they are also
  falling.
* **low coverage**: below threshold, but not measurably lower than before (or
  no baseline to compare with). The first full run showed why this needs its
  own name: the gorilla/chimpanzee SIV assay of Takehisa 2009 screened against
  all SIV, or a "turtles only" Mycoplasma assay against the whole genus, sits
  at the same low share in every year. That is an assay used beyond its design,
  not one that has drifted.

**The recent window widens when records are scarce.** It is
`recent_window_months` long, but for an assay with fewer than
`min_records_for_drift` evaluable records in that window it extends a year at a
time, up to `max_window_months`, and the assay reports the window it used.
Without this, an assay for a sparsely sequenced taxon is judgeable only in the
years following a deposition burst: Bd ITS records arrive 56 in 2012 and then
four, so the standard Bd assay read "stable" in 2014 and "insufficient data"
every year after, on no change in the assay. Widening can only add older
records, never drop recent ones. On the 2026-10-04 run, 116 of 141 assays use
the plain 24-month window.

Below `min_records_for_drift` it is reported
as **insufficient data** and never flagged, whatever the fraction looks like;
below threshold with an interval that still covers it, it is **watch**.

The interval is Wilson rather than the textbook normal approximation, which
misbehaves near 0 and 1 — it can return bounds outside [0, 1], and at k = n it
collapses to zero width and claims certainty from a handful of records. The
change from baseline uses the Newcombe hybrid-score interval, which builds a CI
for a difference of proportions out of the two Wilson intervals and keeps that
good behaviour at the extremes, where baselines near 100% live. Both are
closed-form arithmetic, so every figure in the report can be recomputed by hand
from the counts in the per-year table.

**What the fraction estimates, and what it does not.** The intervals above
assume records are independent draws from the population the assay is used on.
Neither half holds:

* *GenBank samples sequencing effort, not circulating diversity.* An outbreak
  deposits hundreds of near-identical sequences from one transmission chain;
  endemic background deposits none. The effective sample size is the number of
  independent lineages, so a Wilson interval computed on record counts is
  narrower than the evidence warrants.
* *Deposition is correlated with detection.* A locus is often sequenced
  *because* an assay amplified it, and a variant that escapes PCR may never be
  deposited. The bias runs toward optimism, which makes `declining` strong
  evidence and `stable` weak evidence. They are not symmetric.
* *One proportion per assay is the wrong estimand for most real failures.*
  Published failures are nearly always lineage-conditional — fails on clade B,
  on the lineage circulating in one region, on the fish ranaviruses the assay
  never claimed. A clade that is 5% of deposits can be 100% of a region's cases,
  and averaging it away is precisely why only 2 of the 11 documented failures in
  `docs/validation-cases.tsv` are caught through the `declining` flag, and why 10
  of those 11 read as coverage gaps rather than as drift. Per-clade fractions are
  the fix, and are only partly built (`lineage.group_at_rank` is species, so a
  genotype below species is still averaged away).

So `detect_fraction_threshold: 0.90` is a judgement about tolerable
surveillance loss, not a property of PCR: an assay missing 1 in 10 targets is
still fine for prevalence and useless for ruling out disease in one animal.

**Joining calls to deposit years** is the one fiddly part. The screen stage
keys on the FASTA record id, which from NCBI carries a version (`AB123456.1`);
the metadata keys on the esummary caption, which does not (`AB123456`). The
join strips the version from both sides, and where several versions of one
accession appear, the latest revision wins rather than both being counted.

**Nested protocols are scored per round, then round 2 is warned about round 1.**
A nested or semi-nested protocol is several entries here, one per round, and each
is screened independently — which is right, because either product can be read on
a gel, so a round whose primers still match is a usable assay on its own. But
round 2's figure answers "would these primers bind this sequence", which is the
question for round 2 run *directly*; run as published its template is round 1's
product, so a record whose outer primers have drifted yields nothing however well
the inner pair matches. The report therefore adds a **Nested protocols** table
giving each round's own share beside the share of records *both* rounds reach.

On the 2026-10-07 records that gap is large for a few families and absent for
most: `LYSSAVIRUSES_ssRNA_Nucleoprotein_gene` reads 99.5% for round 2 alone and
**32.4% run as a nest**, because round 1 escapes on two thirds of the records
round 2 would otherwise reach; `BOCAVIRUS_ssDNA_NS1_gene` and
`Pan_flavivirus_NS5_3` lose essentially nothing. Only round-1 failures that are
the assay's fault count — a `fail`, or a `no_amplicon` labelled `diverged` — on
the same reasoning the drift denominator already uses.

Nothing here changes a status: it is reported beside the per-round rows, as
degeneracy and thermodynamics are. The dependency is one-directional, since round
2 failing leaves round 1's product perfectly readable.

**And the nesting itself is checked**, which nothing did before: on records both
rounds score, does the inner amplicon actually lie inside the outer? Three
families fail that test and get no conditional coverage, because conditioning
round 2 on a round 1 that does not feed it would invent a number. The clearest is
`CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme`, whose two amplicons are **disjoint**
— about 2.7 kb apart in the RdRp gene — so whatever the `_round2` suffix says,
these are two assays rather than two rounds. Round order comes from
`source.nested_round` rather than the id, because the id does not always carry it:
the Landolfi orthoreovirus base entry holds the paper's *second* round, and taking
the base as the outer round inverted that pair until the containment check caught
it.

**Coverage gaps** list assays whose target has fewer than
`min_records_for_coverage` evaluable records. An assay cannot be shown to work
against diversity nobody has sequenced, and for wildlife pathogens that is
usually the finding rather than a caveat.
