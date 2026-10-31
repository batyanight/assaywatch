# How the scoring works

There are two separate judgements here and it helps to keep them apart.

**Per sequence:** would these oligos amplify this record? **Per assay:** given
every record and when each was deposited, is detection falling?

The first is a mismatch penalty. The second compares two time windows. Neither
is a measurement of your assay in a tube, and the gap between a prediction from
sequence and a result from a thermocycler is the main thing to keep in mind
while reading any of it.

---

## Per sequence: the call

Every oligo is searched against every record, both strands, allowing up to six
mismatches. Where a forward and reverse site face each other at a plausible
product size, the mismatches are converted to a penalty, and the penalty to one
of five outcomes.

### The penalty

A mismatch costs more the closer it sits to the 3' end, because that is where
the polymerase extends from:

| position | window | cost per mismatch |
|---|---|---|
| 3' end | last 5 nt | 3.0 |
| middle | positions 6–10 from the 3' end | 1.0 |
| 5' region | everything else | 0.5 |
| probe centre | — | 2.0 |
| probe ends | — | 1.0 |

Forward, reverse and probe penalties are added into a single total, and that
total decides the call:

| call | rule | counted? |
|---|---|---|
| `detect` | total ≤ 1.0 | yes, as detection |
| `reduced` | ≤ 3.0 — amplifies, expect a Ct shift | yes, as detection[^1] |
| `fail` | above 3.0, a mismatch at a primer's final 3' base, or no probe site in the product | yes, as failure |
| `no_amplicon` | no primer pair in the right orientation and size range | **excluded** |
| `indeterminate` | too many ambiguous bases under an oligo to judge | **excluded** |

[^1]:
    For a hydrolysis probe this is arguably wrong, and there is a switch for it.
    Detection *is* the probe: one that binds poorly reports late or not at all,
    whereas a primer that binds poorly still makes product. Turning that on for
    probe chemistries improves the catch rate from 5/11 to 6/11 documented
    failures with no extra false alarms — and costs two genuine positives on a
    published *Leptospira* validation panel. That trade-off is not obviously
    worth making, so it ships off.

The last two are excluded deliberately. A record missing the locus, truncated,
or full of ambiguity codes tells you about GenBank, not about your assay.
Counting them would make a bad sequencing year look exactly like drift.

### Degeneracy is never penalised

A degenerate base covering the record's base is a **match** — that is what
degeneracy is for. Pool size is reported separately and never counted against an
assay. An ambiguity code in the *record* is likewise never scored as a mismatch;
it is missing information, not evidence of one.

### Products have to be the right size

A call is constrained to the entry's measured product length, within 25% either
way. A 1931 bp product is not a 194 bp assay amplifying. That tolerance was
measured rather than chosen: across a full run, the deviation between observed
and declared length has a knee around 0.2 and flattens after it.

---

## Where this model is wrong

One well-supported fact, several approximations. Worth knowing before you read
any call here.

**The fact.** A polymerase extends from the primer's 3'-OH, so a mismatch there
sits in the catalytic site, while one near the 5' end costs a little stability
on an oligo with nineteen other matched bases. Weighting by distance from the 3'
end is the right shape — Kwok et al. 1990
([10.1093/nar/18.4.999](https://doi.org/10.1093/nar/18.4.999)) and Stadhouders
et al. 2010
([10.2353/jmoldx.2010.090035](https://doi.org/10.2353/jmoldx.2010.090035)).

**The approximations, worst first.**

1. **It ignores which mismatch it is.** Both papers above find identity
   dominates: at the 3' terminus A:A, A:G, G:A and C:C suppress yield by orders
   of magnitude — over 7 Cq in Stadhouders — while T:G, T:C and T:T are nearly
   free, under 1.5 Cq, because a T:G wobble still stacks. Failing every terminal
   mismatch is right for roughly half of them and wrong for the rest.
2. **Penalties are summed into one total**, but amplification needs forward
   *and* reverse, and detection needs the probe as well. Those are serial gates.
   Three trivial mismatches, one per oligo, land in the same bin as one
   near-lethal mismatch next to the 3' end.
3. **One table covers every chemistry** — 155 conventional PCRs and 60 probe
   assays. A hundredfold yield loss is a missed Ct in qPCR and often still a
   visible band after 40 cycles of endpoint PCR. Both get the same `fail`.
4. **Probe geometry is ignored.** A minor-groove binder adds roughly 15–20 °C of
   Tm and makes short probes viable, so an MGB probe tolerates mismatches a bare
   oligo of the same length would not.
5. **Mismatches add linearly**, so two adjacent ones — which destroy a run of
   base stacking — are under-penalised next to two spread apart.

If your assay sits near a boundary, these are the reasons to check it yourself
rather than take the call at face value.

---

## Per assay: the drift call

Calls are grouped by the year each record was deposited, and detection in the
recent window is compared with everything earlier.

### Why intervals rather than percentages

A wildlife assay might have five records in two years. Three failing is 40%,
which looks alarming and means nothing — the interval runs from roughly 10% to
70%. Flagging on point estimates would bury real signal under noise from exactly
the sparsely sequenced targets this is meant to serve.

So an assay is flagged only when the **upper** bound of its recent interval
falls below the threshold. The data have to be inconsistent with the assay still
working, not merely compatible with it failing.

The interval is Wilson rather than the textbook normal approximation, which
misbehaves near 0 and 100% — it can return bounds outside the possible range,
and when everything detects it collapses to zero width and claims certainty from
a handful of records. The change from baseline uses the Newcombe interval, built
from two Wilson intervals, which stays sensible where baselines near 100% live.
Both are closed-form, so every number on this site can be checked by hand from
the counts printed beside it.

### The statuses

| status | rule |
|---|---|
| **declining** | recent interval below 90%, the change interval entirely below zero, a fall of at least 5 points, **and** the assay cleared 90% in some earlier year |
| **low coverage** | below 90% but not measurably lower than before, or with no working baseline |
| **watch** | below 90% with an interval that still spans it |
| **insufficient data** | fewer than 15 evaluable records; reported, never flagged |
| **no recent data** | nothing deposited in the window |
| **stable** | none of the above |

That final condition on `declining` is what keeps the word meaningful. Without
it, 14 of 37 assays flagged in an early run were pan-family consensus PCRs that
never covered the organism they were screened against. A fall from 14% to 0% is
a change in which clades got deposited, not an assay degrading.

### The window widens when sequences are scarce

The recent window is 24 months, but for an assay with fewer than 15 evaluable
records it extends a year at a time up to five years, and the assay reports the
window it used.

Without that, a sparsely sequenced target is only judgeable right after a burst
of deposits. *Batrachochytrium dendrobatidis* ITS records arrive 56 in one year
and then four, so the standard assay read "stable" in 2014 and "insufficient
data" ever after — on no change whatsoever in the assay. Widening only ever adds
older records; it never drops recent ones.

---

## What the percentage really estimates

The intervals assume records are independent draws from the population your
assay is used on. Neither half of that is true.

**Sequence databases sample effort, not circulating diversity.** An outbreak
deposits hundreds of near-identical sequences from one transmission chain;
steady endemic circulation deposits none.

**Deposition is correlated with detection.** A locus often gets sequenced
*because* an assay amplified it, and a variant that escapes PCR may never be
deposited at all. This biases everything toward optimism, which makes
`declining` strong evidence and `stable` weak evidence. They are not symmetric,
and that asymmetry is probably the single most important thing to carry away
from this page.

**One percentage per assay is the wrong summary for most real failures.**
Published misses are nearly always specific to a clade, a region or a host. That
is why every assay page carries a per-lineage breakdown where one exists, and
why the worst well-sampled lineage can override an otherwise reassuring pooled
verdict.
