# How it was tested

Every threshold in this tool I set by eye. That is true of most in-silico primer
checkers, and it is usually where the documentation stops.

So the question worth answering is not what the thresholds are, but whether the
verdicts they produce agree with reality. The only reality available is the
literature: assays whose real-world performance somebody published a follow-up
about. If a group reported an assay missing circulating strains in 2014, would
this tool have flagged it in 2013?

---

## How a test case works

One case is an assay, a date, and what a paper found.

The tool is re-run as of that date: records deposited on or after the cutoff are
dropped, and the recent window is measured backwards from the cutoff. Nothing
else changes, so the tool is never shown the answer.

The paper's finding becomes `works`, `fails` or `partial`. The tool's status
maps on like this:

| status | reads as |
|---|---|
| stable, watch | works |
| declining | fails |
| low coverage | partial |
| insufficient data, no recent data | **undecided** |

`undecided` is counted separately rather than as a wrong answer. An assay the
tool declines to judge is not the same as one it judges badly, and keeping them
apart is what tells me whether the minimum record count is set sensibly.

## The main set: 50 cases

These are the cases I tuned the thresholds against, so the figures below are
**in-sample** and flatter the tool. On the run of 31 October 2026:

| | result | 95% credible interval |
|---|---|---|
| documented failures caught | **6 of 11** | — |
| …of those it judged at all | 6 of 8 | — |
| `declining` calls that were real failures | **4 of 10 — 40%** | 15% – 70% |
| false alarms among working assays | 4 of 32 — 12% | — |

Ten of those eleven documented failures are coverage gaps; one is drift.

!!! warning "Eleven rows is not eleven independent results"
    Several rows describe the same underlying event reported by different
    papers. Treat the real denominator as about seven independent failure
    events, and read the intervals rather than the point estimates — they span
    25 to 50 points, which is what a corpus this size supports.

## Held-out sets: all three scored worse

A held-out set is one I reserved and did not consult while setting any
threshold. Three exist and all three have now been used.

| set | failures caught | `declining` calls that were real | false alarms |
|---|---|---|---|
| main set (in-sample) | 6 of 11 | 4 of 10 | 4 of 32 |
| held-out 1 | 3 of 9 | 1 of 5 | 0 of 17 |
| held-out 2 | 2 of 3 | 0 of 4 | 4 of 10 |
| held-out 3 | 1 of 2 | 1 of 1 | 0 of 0 |

Held-out performance being worse than tuned performance is the expected
direction, and it is the reason the headline figures above should not be quoted
on their own.

**The worst result is held-out set 2**, which put five of ten working assays in
`declining`. Four of those five are pan-family consensus nested PCRs whose
papers report them amplifying a divergent virus from a handful of positives.
Their papers are claiming something narrower than what a whole-genus screen
measures — but from your point of view they are still false alarms, and you
should expect them on broad consensus assays.

---

## The case that worked, and why the control matters

Held-out set 3 exists because neither of the first two contains a case that
demonstrates **drift** in the strict sense: the same lineage changing over time
at the primer sites. Most published failures are coverage problems, which is
itself a finding about this field.

Scored as of 6 September 2013, over 5,847 records:

| assay | status | detected |
|---|---|---|
| [`INFLUENZA_A_M1_Ward_2004`](assays/INFLUENZA_A_M1_Ward_2004.md) | **declining** | 86.2% (85–87%) |
| [`INFLUENZA_A_M1_Yang_2014`](assays/INFLUENZA_A_M1_Yang_2014.md), the redesign | **stable** | 91.6% (91–92%) |

Yang's group redesigned Ward's assay because it was missing circulating
influenza. The tool agrees, from sequence alone, on records deposited before
their paper appeared.

The control is what makes this more than an anecdote: both entries share a
target, an archive, a date window and every setting. They differ only in their
oligo sequences. Nothing but the primers and probe can account for one reading
`declining` and the other `stable`.

## The case that failed, which is more useful

The second case in that set is a **miss**, for a reason no threshold adjustment
can repair.

Shu and colleagues documented drift in the CDC H3 assay in 2026. This tool
cannot detect it, because under its own scoring that assay already reads as
non-detecting from 2016 onward — 0.4% in 2019, 0.2% in 2026. A single mismatch
in the middle of a hydrolysis probe is enough to disqualify detection, and the
assay had already hit that floor before the drift Shu describes began.

Checked against one record directly: the forward primer matches perfectly, the
reverse matches perfectly, and the probe carries one mismatch at position 13 —
exactly where the redesigned version widens that base to a degenerate code.

**A before-and-after comparison cannot detect a decline in something already at
zero.** That is a limit of the approach rather than a tuning problem, and it is
worth knowing if your assay is one this tool already scores near the floor.

---

## Things that looked like improvements and were not

Three results worth sharing, because each one killed a change I expected to
ship.

**Loosening the scoring can create a false alarm.** One candidate raised the
mismatch tolerance across the board. For one assay it lifted recent detection
from 64.9% to 67.6% — an improvement — and that is precisely what flipped it to
`declining`, because the baseline rose further. The flag compares two windows,
so making everything better can make the comparison worse.

**A pass criterion you chose in advance can still be blind.** A smoother
positional decay curve passed the test I had pre-registered for it and quietly
lost four documented catches, including the only drift case the project had at
the time. Totals barely moved, so a summary statistic read it as harmless. The
fitted curve had discounted the whole 3' region, which is where the signal
lives.

**An old measurement is not permanent evidence.** A later candidate reproduced
an earlier experiment's record-level movements exactly, but the verdict that
experiment had rested on was no longer near its decision boundary, so the
original conclusion no longer followed.

---

## What none of this tests

- **Nothing here is a wet-lab result.** Every figure is a prediction about
  whether oligos match sequence. Predicted amplification is not amplification.
- **The cases are not a random sample.** They are assays somebody thought worth
  publishing a follow-up about, which skews toward assays interesting enough to
  re-examine — probably toward ones that had problems.
- **In-sample is in-sample.** For the number you would get on an assay I have
  never seen, read the held-out rows. There are only 14 of them.
- **Sequence databases are not surveillance.** An outbreak deposits hundreds of
  near-identical sequences; endemic circulation deposits none. A variant that
  escapes PCR may never be sequenced at all, which biases everything here toward
  optimism.
