# What the output is worth

If you are deciding how much weight to put on a status, read this page. Counts
describe the registry on 31 October 2026; figures from a run carry that run's
date.

---

## The short answer

**A status tells you where to look. It is not a result.**

`declining` means an assay is worth examining. Against the cases I could test —
assays whose real-world performance was later published — **4 of 10 `declining`
calls were genuine documented failures**, a 40% hit rate with a 95% credible
interval from 15% to 70%.

That interval is wide because there are not many such cases in the literature.
Every headline figure in the validation spans 25 to 50 points, and I would
rather show you that than present a tidy number.

## Every threshold is a judgement

Nineteen numbers decide every verdict here and all but one I set by eye. Each
one is written down with its reasoning, or with an admission that it has none,
in [`config.yaml`](https://github.com/batyanight/assaywatch/blob/main/config.yaml).

The 90% detection threshold is the clearest example. It is a statement about
tolerable surveillance loss, not a property of PCR. An assay missing 1 in 10
targets is still perfectly useful for estimating prevalence and useless for
ruling out disease in an individual animal. The right number depends on what
you are doing, which is why it is visible and arguable rather than buried.

The one exception is the 5-point minimum decline, which has independent
regulatory precedent: FDA's *Policy for Evaluating Impact of Viral Mutations on
COVID-19 Tests (Revised)* (January 2023, docket FDA-2020-D-0987) advises
developers to act when mutations "reduce performance by 5% or more". A regulator
reached the same floor without reference to this work. Two caveats: that policy
is tied to the COVID-19 emergency declaration, and it does not say whether its
5% is absolute or relative, while mine is percentage points.

## Four things this method cannot do

These are properties of the approach, not bugs.

### 1. What gets measured depends on what is being measured

A record where one primer has drifted counts as a failure. A record where both
have drifted produces nothing and drops out of the denominator entirely. Across
one full run, 65.7% of 2.72 million screened records never reached the
statistics. Every assay page shows this split for its own assay.

This is the limitation most worth challenging, and it may not be fixable without
changing what the tool estimates.

### 2. Sequences are not independent samples

Identical primer-site patterns are de-duplicated, but population structure
beyond that is invisible. Confidence intervals computed on record counts are
therefore narrower than the evidence really justifies. Where a trend is
reported, you get it twice — once per record, which overstates the evidence, and
once per distinct binding pattern, which understates it. On one run, assays with
a statistically significant decline dropped from 64 to 32 under that correction,
and 23 of 74 reversed direction.

### 3. A decline cannot be seen in something already at zero

If an assay already scores as non-detecting under this tool's rules, later
genuine drift produces no measurable fall. This is not hypothetical — it is
exactly why one of the two real drift cases I tested against was missed. See
[how it was tested](how-it-was-tested.md).

### 4. Tiled amplicon schemes are out of scope

ARTIC-style schemes need a model of many amplicons reporting dropout, not one
assay per primer pair.

## What is deliberately unfinished

Each of these is blocked on evidence that does not exist, so they are listed
rather than left looking like forgotten work.

- **A per-record statistical model** would need at least 40 documented
  within-family negatives across several independent papers. There are 11.
  Anything fitted on 11 would not be defensible, so the obstacle is the
  literature, not the modelling.
- **Two scoring parameters cannot be settled from the bench evidence available**
  — one because it relabels records in a way a gel cannot distinguish, the other
  because settling it would mean fitting on exactly the data reserved for
  checking.
- **Ten assays are waiting** for a verifiable citation and are never screened or
  published until they have one. Two of them are unpublished protocol oligos and
  will stay there.

## Still owed, and honest about it

These need a person with a paper open, not more code.

| owed | scale |
|---|---|
| design scope read from the source paper, per test case | 34 rows across 17 assays |
| curation flags to clear | 227 readings over 154 entries (2026-10-30); 15 will never clear, being true |
| reaction conditions — limits of detection, master mixes, concentrations | about 247 |
| validation panels, each a table in a paper | 0 of 218 entered |
| papers with a specificity claim worth recording | 118 of 178 on hand |

## How often it actually runs

The schedule is installed on **one laptop**. "Re-screened weekly" describes
tooling in this repository, not a service you can point at. If you need current
numbers for a specific assay, run it yourself or ask.

## What I will stand behind about the registry

- 218 entries, every one citing a paper whose DOI has been confirmed against
  Crossref. An assay without one is not published here.
- Oligo sequences and product sizes are checked against real GenBank records and
  the paper's own table before entry. Where a measured product length disagrees
  with the published one, the entry keeps the **measured** value and says so.
- 19 assays get no status at all, because something about them means a verdict
  would be misleading — a chemistry this scoring does not model, or an outcome
  read from a gel band rather than amplification. Those pages explain the reason
  instead of showing a number with a warning next to it.

If an entry misrepresents your assay, that is a bug and I would like to know.
