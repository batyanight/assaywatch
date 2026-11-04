# Validation

Every threshold in this tool was set by inspection, not derived. So the thresholds
themselves matter less than one question: do the verdicts they produce agree with
how the assays performed?

The reference standard is the literature: assays whose field performance was
published later. If a group reported in 2014 that an assay failed to detect
circulating strains, would this tool have flagged it in 2013?

---

## Case construction

A case is an assay, a date, and a published finding.

The pipeline is re-run as of that date. Records deposited on or after the cutoff
are left out, and the recent window is counted back from the cutoff. No other
parameter changes, so the tool never sees the outcome.

The published finding is classified as `works`, `fails` or `partial`. Statuses
map to those classes like this:

| status | classification |
|---|---|
| stable, watch | works |
| declining | fails |
| low coverage | partial |
| insufficient data, no recent data | **undecided** |

`undecided` is tabulated separately and not counted as an error. An assay the
tool declines to judge is not the same as one it judges wrongly, and that
difference is what sets the minimum record count.

## Development set: 50 cases

These cases were used to set the thresholds, so the figures are **in-sample**
and optimistic. On the 2026-10-31 run:

| measure | result | 95% credible interval |
|---|---|---|
| documented failures detected | **6 of 11** | — |
| of those the tool judged at all | 6 of 8 | — |
| `declining` calls that matched documented failures | **4 of 10 (40%)** | 15–70% |
| false positives among working assays | 4 of 32 (12%) | — |

Ten of the eleven documented failures are coverage gaps; one is drift.

!!! warning "Eleven rows are not eleven independent observations"
    Several rows describe the same event reported in different publications.
    The effective denominator is about seven independent failure events. Read
    the intervals, not the point estimates.

## Held-out sets

A held-out set is kept aside and not looked at while setting any threshold.
There are three, and all have been used.

| set | failures detected | `declining` calls that were real | false positives |
|---|---|---|---|
| development (in-sample) | 6 of 11 | 4 of 10 | 4 of 32 |
| held-out 1 | 3 of 9 | 1 of 5 | 0 of 17 |
| held-out 2 | 2 of 3 | 0 of 4 | 4 of 10 |
| held-out 3 | 1 of 2 | 1 of 1 | 0 of 0 |

Held-out performance below tuned performance is what you would expect. It is why
the development figures should not be quoted on their own.

The weakest result is held-out set 2, where five of ten working assays were
classified `declining`. Four of the five are pan-family consensus nested PCRs.
Their publications report amplifying a divergent virus from a small number of
positives, which is a narrower claim than a whole-genus screen tests. To a user
these calls are still false positives, and broad consensus assays should be
expected to produce them.

---

## Confirmed detection

Held-out set 3 was built because neither of the first two has a case showing
**drift** in the strict sense: the same lineage changing over time at the primer
binding sites. Most published failures are coverage problems, which is itself a
finding about the field.

Scored as of 2013-09-06, over 5,847 records:

| assay | status | predicted detection |
|---|---|---|
| [`Influenza_A_virus_M1_Ward_2004`](assays/Influenza_A_virus_M1_Ward_2004.md) | **declining** | 86.2% (85–87%) |
| [`Influenza_A_virus_M1_Yang_2014`](assays/Influenza_A_virus_M1_Yang_2014.md), the redesign | **stable** | 91.6% (91–92%) |

Yang and colleagues redesigned the Ward assay because it was failing to detect
circulating influenza. The tool reaches the same conclusion from sequence alone,
using records that predate that publication.

The internal control is what makes the case convincing. Both entries share a
target, archive, date window and every scoring parameter, and differ only in
oligonucleotide sequence. Nothing but the primers and probe can explain why one
reads `declining` and the other `stable`.

## Confirmed non-detection

The second case in that set was **not** detected, and no threshold adjustment
would fix that.

Shu and colleagues documented drift in the CDC H3 assay in 2026. This tool cannot
see it, because under its own scoring that assay already reads as non-detecting
from 2016 onward: 0.4% in 2019, 0.2% in 2026. A single mismatch at the center of
a hydrolysis probe is enough to rule out detection, and the assay had hit that
floor before the divergence Shu describes began.

Checked against one record: the forward primer matches exactly, the reverse
matches exactly, and the probe has one mismatch at position 13, the position
where the redesigned assay uses a degenerate base.

A before-and-after contrast cannot detect a decline from zero. This comes from
the approach itself and is not a tuning problem. It applies to any assay this
tool already scores near the floor.

---

## Rejected modifications

Three results are recorded because each ended a change that was expected to be an
improvement.

**Loosening the scoring everywhere can create a false positive.** One candidate
raised the mismatch tolerance at all positions. For one assay it raised recent
detection from 64.9% to 67.6%, which is an improvement, and that is what
reclassified it as `declining`, because the baseline rose even further. The flag
compares two windows, so an improvement across the board can make the contrast
worse.

**A pre-registered acceptance criterion can miss a real loss.** A smoother
positional decay function met its pre-registered criterion while losing four
documented detections, including the only drift case available at the time.
Aggregate disagreement counts barely moved, so the summary statistic called the
change neutral. The fitted curve had discounted the whole 3′ region, where the
signal is concentrated.

**An earlier measurement does not stay valid forever.** A later candidate
reproduced an earlier experiment's record-level movements exactly. But the
verdict that experiment rested on was no longer near its decision boundary, so
the original conclusion no longer followed.

---

## Scope of these results

- **No result here is a laboratory measurement.** Every figure is a prediction
  of oligonucleotide–template match. Predicted amplification is not
  amplification.
- **The cases are not a random sample.** They are assays that have a follow-up
  publication. That favors assays interesting enough to re-examine, and
  plausibly those that had problems.
- **In-sample figures are in-sample.** For an unseen assay, the held-out rows are
  the relevant estimate, and there are few of them: 53 rows across the three
  sets, with **14 documented failures** between them. Every proportion quoted
  from them has a denominator in single figures.
- **Sequence databases do not sample surveillance.** An outbreak deposits
  hundreds of near-identical sequences; endemic circulation deposits none. A
  variant that escapes PCR may never be sequenced, which biases the whole
  procedure toward optimism.
