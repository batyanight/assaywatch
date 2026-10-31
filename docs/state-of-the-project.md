# State of the project, 2026-10-30

One page, for a reader who will not read 135 journals. What this tool does, what
its output is worth, and what is known to be wrong with it. Counts are from
`assaywatch validate registry` on 2026-10-30; figures from a run carry that run's
date.

## What it does

AssayWatch keeps a version-controlled registry of published PCR and qPCR assays
for pathogens, screens each one against the GenBank records of its own target, and
reports predicted detection **indexed by year of deposit**, so that decay reads as
a trend rather than a snapshot. An assay is designed against the handful of
sequences available when it is published and then used for years while the
database accumulates divergent strains nobody re-screens it against.

The registry and that time axis are the contribution. The screening engine is the
means.

| | |
|---|---|
| live entries | 218 — 179 `active`, 38 `draft`, 1 `deprecated` |
| waiting in `pending/` | 10, every one for want of a verifiable DOI |
| chemistry | 155 conventional, 35 hydrolysis probe, 21 MGB, 2 SYBR, 1 RPA |

## What the evidence supports

**The premise has one confirming case, and it arrived on 2026-10-30.** Until then
the tool had never caught a documented failure through its drift flag: every catch
was credited to `low coverage`, which is a statement about how much of a family's
deposited diversity an assay reaches, not about decay over time.

The case is Yang 2014 on the influenza A M1 assay of Ward 2004. As of September
2013, over the 5,847 records in the recent window:

| assay | status | detected share |
|---|---|---|
| `INFLUENZA_A_M1_Ward_2004` | **`declining`** | 86.2% (85-87%), upper bound under the 90% threshold |
| `INFLUENZA_A_M1_Yang_2014` — the documented redesign | **`stable`** | 91.6% (91-92%) |

The two entries differ in nothing but their oligos: same retrieval group, archive,
date window, scoring config and chemistry. So the verdict difference is
attributable to the primer and probe sequences and to nothing else. That control is
why the row is worth more than the verdict alone.

**One case is one case.** On this set the precision of `declining` is 1/1 and
documented failures caught is 1/2. Both intervals are one row wide and neither is
a precision estimate.

**The broader validation, and it is weaker.** Against the development set of 50
cases, on the 2026-10-31 run: documented failures caught **6/11** (**6/8** among
the cases it judged at all), precision of `declining` **4/10 = 40% (95% CrI
15%-70%)**, false alarms **4/32 = 12%**. On held-out set
2, five of ten working assays read `declining` — four of them pan-family consensus
nests whose paper reports them amplifying a divergent virus from a handful of
positives, which is a mismatch between what the paper claims and what the status
measures, not only a scoring error.

**So a status is worth reading, not quoting.** `declining` means "worth looking
at". It does not mean an assay has failed.

## Every threshold is a placeholder

Nineteen numbers decide every verdict and all but one were set by eye. They are
listed with their values in `ROADMAP.md` under "The placeholders, for the record",
and each carries its reasoning, or the admission that it has none, in
`config.yaml`.

The exception is `drift.min_decline` 0.05, which has regulatory precedent: FDA's
*Policy for Evaluating Impact of Viral Mutations on COVID-19 Tests (Revised)*
(January 2023, docket FDA-2020-D-0987) tells developers to act when mutations
"reduce performance by 5% or more". A regulator arrived at the same floor
independently. Two caveats sit beside the setting: the policy is tied to the
section 564 COVID-19 declaration, and its 5% is not stated as points or relative,
where ours is percentage points of detected share.

## Known limitations

Recorded, not work. These are properties of the method, not bugs awaiting a fix.

1. **The denominator is drift-correlated.** A record with one drifted primer counts
   as a failure; a record with both drifted leaves the denominator as `no_site`.
   65.7% of 2.72M rows never reach the statistics, and `no_site` alone is 53% of
   every row. The split is measured and printed per assay; the bias itself may not
   be fixable without a different estimand. This is the limitation most likely to
   be challenged, and rightly.
2. **Records are not independent.** Identical binding-site footprints are
   de-duplicated, but clade structure beyond that is invisible, so the footprint
   count is not a lower bound on the effective sample size. Where a trend is
   reported, the by-record figure is an upper bound on the evidence and the
   by-footprint figure nearer a lower bound; on one run, assays with a significant
   decline went 64 to 32 under that correction and 23 of 74 flipped direction.
3. **Majority contamination.** `ENTEROVIRUS_ssRNA_VP3_VP1_round2` cannot be
   addressed by the archive-anchor mechanism by construction.
4. **ARTIC-style tiled schemes are out of scope.** They need a scheme object of
   many amplicons reporting dropout, not one assay per primer pair.

## What cannot be finished, and why

Each of these is blocked on evidence that does not exist, and the project says so
in its own words rather than leaving them as open tasks.

- **The Bayesian per-record model (C2).** Needs at least 40 within-family
  negatives across several independent papers; there are 11. Nothing fitted on 11
  would be defended, so the blocker is a literature corpus, not the modelling.
- **`drift.anchor_fdr`.** Impossible to settle on the bench by construction: it
  relabels records between `no_site` and `fail`, and a bench row is scored
  band/no-band, where those are the same answer. It ships at 0.001 as a stated
  placeholder.
- **`primer_mid_penalty`.** The bench cannot settle it without fitting on exactly
  the rows reserved for fitting; the one panel that can never be fitted on is
  unmoved at every value. Agreement is flat from 0.0 to the shipped 1.0.
- **`lineage.unclassified_is_bucket`** and **`thermo`.** Both built and both
  inert: the first changes no tier-2 row, so there is nothing to ship it on; the
  second needs annealing conditions the registry does not carry for most entries.
- **The 10 entries in `pending/`.** Two are unpublished protocol oligos and stay
  there by definition. For the rest, no document on disk prints their oligos and
  the design papers, if they exist, are not findable by assay description.
- **The retrospective identity queue.** Spent: no further document will settle its
  remaining rows.
- **The Greene SLURM profile.** Written as teaching material and untestable from a
  laptop; its first submission on a login node would close it.

## What a reader could still do, and what it would cost

These are readings, not code. Each needs a person with the paper open.

| owed | count |
|---|---|
| `scope_taxid` values, one read per case row from its own source paper | 34 rows, 17 assays, 34 papers |
| `needs_review` flags, on 154 of the entries | 227 readings (15 never clear, being true) |
| condition rows left for a reader (limits of detection, master mixes, oligo concentrations) | about 247 |
| `panels` blocks, each a table in a paper | 0 of 218 populated |
| papers carrying an exclusivity claim worth entering | 118 of 178 on disk |

## One finding worth carrying forward

On 2026-10-30, chasing a case the tool could not judge, it turned out that NCBI
has stopped assigning influenza subtype taxids to new deposits. Four entries whose
retrieval query named those taxids had archives that ended years earlier — H5's
newest deposit was 2021, H7's was 2020 — so neither assay could show recent drift
at all. No wrong verdict was published -- both committed example runs report them as
"no evaluable records deposited since Oct 2021", so the tool declined to judge them
and named the cutoff. What the message could not say is that the cutoff was a
property of our retrieval query rather than of the taxon, so four live assays sat
unjudgeable while the report read as correct. The queries are fixed and the entries
now restrict their own population by the subtype in each record's description.

The general lesson is the one this project keeps relearning: a retrieval query is
a scientific claim about what population an assay is being judged against, and it
goes stale silently. Nothing in the pipeline complained. It was found by reading a
deposit-year distribution out of an archive because a verdict looked absurd.
