# Known limitations

Reference for assessing how much weight a status will bear. Registry counts
describe 2026-10-31; figures derived from a run carry that run's date.

---

## Summary

A status indicates where to direct attention; it is not a result.

Measured against assays whose field performance was subsequently published,
**4 of 10 `declining` calls corresponded to documented failures** — 40%, with a
95% credible interval of 15% to 70%. Every headline figure in the validation
spans 25 to 50 percentage points, reflecting the small number of published
follow-up reports available.

## Threshold provenance

Nineteen numeric thresholds determine every verdict. All but one were set by
inspection rather than derived from data. Each is documented at its definition
in [`config.yaml`](https://github.com/batyanight/assaywatch/blob/main/config.yaml),
together with its justification or an explicit statement that none exists.

The 90% detection threshold is the clearest instance. It expresses a judgement
about tolerable surveillance loss rather than a property of PCR: an assay
missing 1 in 10 targets remains adequate for prevalence estimation and
inadequate for excluding infection in an individual animal. The appropriate
value depends on application, which is why it is stated explicitly rather than
embedded in code.

The exception is the 5-percentage-point minimum decline, which has independent
regulatory precedent. FDA's *Policy for Evaluating Impact of Viral Mutations on
COVID-19 Tests (Revised)* (January 2023, docket FDA-2020-D-0987) advises
developers to act where mutations "reduce performance by 5% or more". Two
qualifications apply: the policy is tied to the COVID-19 emergency declaration,
and it does not specify whether its 5% is absolute or relative, whereas the
threshold used here is in percentage points.

## Methodological limitations

### Censoring is correlated with the quantity being estimated

A record in which one primer has diverged is scored as a failure. A record in
which both have diverged yields no product and is excluded from the denominator
entirely. Across one complete run, 65.7% of 2.72 million screened records did
not reach the statistics. Each assay page reports this proportion for its own
assay.

This is the limitation most open to challenge. It may not be correctable
without changing the estimand.

### Records are not independent observations

Identical primer-site patterns are de-duplicated, but population structure
beyond that is not observable. Confidence intervals computed on record counts
are therefore narrower than the evidence supports. Where a trend is reported it
is given twice: by record, which overstates the evidence, and by distinct
binding-site pattern, which understates it. Under that correction, assays with
a statistically significant decline fell from 64 to 32 in one run, and 23 of 74
reversed direction.

### A two-window contrast cannot detect decline from a floor

Where an assay already scores as non-detecting under the applied rules,
subsequent divergence produces no measurable fall. This is not hypothetical: it
accounts for one of the two genuine drift cases in the held-out material being
missed. See [validation](validation.md).

### Tiled amplicon schemes are out of scope

ARTIC-style schemes require a model of multiple amplicons reporting dropout
rather than one assay per primer pair.

## Work blocked on unavailable evidence

Listed so that these are not mistaken for outstanding tasks.

- **A per-record statistical model** would require at least 40 documented
  within-family negatives across several independent publications; 11 are
  available. A model fitted on 11 would not be defensible, so the constraint is
  the literature rather than the method.
- **Two scoring parameters cannot be resolved from available bench evidence**:
  one relabels records in a manner a gel cannot distinguish; the other could
  only be fitted on the data reserved for evaluating it.
- **Ten assays await a verifiable citation** and are neither screened nor
  published until one exists. Two are unpublished protocol oligonucleotides and
  will remain so.

## Outstanding curation

These require assessment of source publications rather than further
development.

| outstanding | scale |
|---|---|
| design scope read from the source publication, per validation case | 34 rows across 17 assays |
| curation flags requiring resolution | 227 readings across 154 entries (2026-10-30); 15 will not clear, being accurate |
| reaction conditions — limits of detection, master mixes, concentrations | approximately 247 |
| validation panels, each a table in a publication | 0 of 218 entered |
| publications with a specificity claim worth recording | 118 of 178 held |

## Execution frequency

The schedule is installed on a single workstation. "Re-screened weekly"
describes tooling in this repository, not a hosted service. Current figures for
a specific assay require either a local run or a request.

## Registry assurances

- 218 entries, each citing a publication whose DOI has been confirmed against
  Crossref. An assay without one is not published here.
- Oligonucleotide sequences and product sizes are verified against GenBank
  records and the source publication's own table before entry. Where a measured
  product length disagrees with the published value, the entry retains the
  measured value and records the discrepancy.
- 19 assays carry no status, because a property of the entry would render a
  verdict misleading — a chemistry the scoring does not model, or a readout
  other than amplification. Those pages state the reason in place of a figure.

Reports of entries that misrepresent a published assay are welcome.
