# Validation

Every threshold in this tool was set by inspection rather than derived. The
question that matters is therefore not what the thresholds are, but whether the
verdicts they produce agree with observed performance.

The available reference standard is the literature: assays for which field
performance was subsequently published. If a group reported an assay failing to
detect circulating strains in 2014, would this tool have flagged it in 2013?

---

## Case construction

A case comprises an assay, a date, and a published finding.

The pipeline is re-run as of that date: records deposited on or after the
cutoff are excluded, and the recent window is measured backwards from the
cutoff. No other parameter changes, so the tool is not given access to the
outcome.

The published finding is classified as `works`, `fails` or `partial`. Statuses
map as follows:

| status | classification |
|---|---|
| stable, watch | works |
| declining | fails |
| low coverage | partial |
| insufficient data, no recent data | **undecided** |

`undecided` is tabulated separately rather than counted as an error. An assay
the tool declines to judge is distinct from one it judges incorrectly, and that
distinction is what calibrates the minimum record count.

## Development set: 50 cases

These cases were used to set the thresholds; the figures are therefore
**in-sample** and optimistic. On the 2026-10-31 run:

| measure | result | 95% credible interval |
|---|---|---|
| documented failures detected | **6 of 11** | — |
| of those the tool judged at all | 6 of 8 | — |
| `declining` calls corresponding to documented failures | **4 of 10 (40%)** | 15–70% |
| false positives among working assays | 4 of 32 (12%) | — |

Ten of the eleven documented failures are coverage gaps; one is drift.

!!! warning "Eleven rows are not eleven independent observations"
    Several rows describe the same underlying event reported in different
    publications. The effective denominator is approximately seven independent
    failure events. The intervals, rather than the point estimates, should be
    read.

## Held-out sets

A held-out set is reserved and not consulted while setting any threshold. Three
exist; all have been used.

| set | failures detected | `declining` calls that were real | false positives |
|---|---|---|---|
| development (in-sample) | 6 of 11 | 4 of 10 | 4 of 32 |
| held-out 1 | 3 of 9 | 1 of 5 | 0 of 17 |
| held-out 2 | 2 of 3 | 0 of 4 | 4 of 10 |
| held-out 3 | 1 of 2 | 1 of 1 | 0 of 0 |

Held-out performance below tuned performance is the expected direction, and is
the reason the development figures should not be quoted in isolation.

The weakest result is held-out set 2, in which five of ten working assays were
classified `declining`. Four of the five are pan-family consensus nested PCRs
whose publications report amplification of a divergent virus from a small
number of positives. Those publications claim something narrower than a
whole-genus screen measures; from the user's perspective the calls remain false
positives, and they should be expected on broad consensus assays.

---

## Confirmed detection

Held-out set 3 was constructed because neither of the first two contains a case
demonstrating **drift** in the strict sense — the same lineage changing over
time at the primer binding sites. Most published failures are coverage
problems, which is itself a finding about the field.

Scored as of 2013-09-06, over 5,847 records:

| assay | status | predicted detection |
|---|---|---|
| [`INFLUENZA_A_M1_Ward_2004`](assays/INFLUENZA_A_M1_Ward_2004.md) | **declining** | 86.2% (85–87%) |
| [`INFLUENZA_A_M1_Yang_2014`](assays/INFLUENZA_A_M1_Yang_2014.md), the redesign | **stable** | 91.6% (91–92%) |

Yang and colleagues redesigned the Ward assay because it was failing to detect
circulating influenza. The tool reaches the same conclusion from sequence
alone, on records predating that publication.

The internal control is what gives the case weight: both entries share a
target, archive, date window and every scoring parameter, differing only in
oligonucleotide sequence. No factor other than the primers and probe can
account for one reading `declining` and the other `stable`.

## Confirmed non-detection

The second case in that set was **not** detected, for a reason no threshold
adjustment addresses.

Shu and colleagues documented drift in the CDC H3 assay in 2026. This tool
cannot detect it, because under its own scoring that assay already reads as
non-detecting from 2016 onward — 0.4% in 2019, 0.2% in 2026. A single mismatch
at the center of a hydrolysis probe is sufficient to disqualify detection, and
the assay had reached that floor before the divergence Shu describes began.

Verified against an individual record: the forward primer matches exactly, the
reverse matches exactly, and the probe carries one mismatch at position 13 —
the position at which the redesigned assay substitutes a degenerate base.

A before-and-after contrast cannot detect decline from zero. This is a property
of the approach rather than a tuning problem, and is relevant to any assay this
tool already scores near the floor.

---

## Rejected modifications

Three results are recorded because each terminated a change expected to be an
improvement.

**Uniform loosening of the scoring can generate a false positive.** One
candidate raised the mismatch tolerance across all positions. For one assay it
raised recent detection from 64.9% to 67.6% — an improvement — and that is what
reclassified it as `declining`, because the baseline rose further. The flag
compares two windows, so a uniform improvement can worsen the contrast.

**A pre-registered acceptance criterion can be insensitive.** A smoother
positional decay function satisfied its pre-registered criterion while losing
four documented detections, including the only drift case then available.
Aggregate disagreement counts barely moved, so a summary statistic read the
change as neutral. The fitted curve had discounted the entire 3′ region, where
the signal is concentrated.

**A prior measurement is not permanent evidence.** A later candidate reproduced
an earlier experiment's record-level movements exactly, but the verdict on
which that experiment rested was no longer near its decision boundary, so the
original conclusion no longer followed.

---

## Scope of these results

- **No result here is a laboratory measurement.** Every figure is a prediction
  of oligonucleotide–template match. Predicted amplification is not
  amplification.
- **The cases are not a random sample.** They are assays for which a follow-up
  publication exists, which biases toward assays of sufficient interest to
  re-examine, and plausibly toward those that presented problems.
- **In-sample figures are in-sample.** For performance on an unseen assay, the
  held-out rows are the relevant estimate, and they are few: 53 rows across the
  three sets, carrying **14 documented failures** between them. Every
  proportion quoted from them has a denominator in single figures.
- **Sequence databases do not sample surveillance.** An outbreak deposits
  hundreds of near-identical sequences; endemic circulation deposits none. A
  variant escaping PCR may never be sequenced, which biases the entire
  procedure toward optimism.
