# Scoring methods

Two distinct judgements are made, and they should be kept separate.

**Per sequence:** would these oligonucleotides amplify this record? **Per
assay:** given every record and its deposit date, is predicted detection
falling?

The first is a mismatch penalty; the second a contrast between two time
windows. Neither is a measurement of assay performance in a reaction, and the
distance between a prediction from sequence and a result from a thermocycler
applies to everything below.

---

## Per-sequence call

Each oligonucleotide is searched against every record on both strands,
allowing up to six mismatches. Where forward and reverse sites face each other
at a plausible product size, the mismatches are converted to a penalty and the
penalty to one of five outcomes.

### Penalty table

A mismatch is weighted more heavily nearer the 3′ terminus, the site of
polymerase extension:

| position | window | cost per mismatch |
|---|---|---|
| 3' end | last 5 nt | 3.0 |
| middle | positions 6–10 from the 3' end | 1.0 |
| 5' region | everything else | 0.5 |
| probe centre | — | 2.0 |
| probe ends | — | 1.0 |

Forward, reverse and probe penalties are summed, and the total determines the
call:

| call | rule | in denominator |
|---|---|---|
| `detect` | total ≤ 1.0 | yes, as a detection |
| `reduced` | ≤ 3.0; amplifies with an expected Ct shift | yes, as a detection[^1] |
| `fail` | above 3.0, a mismatch at a primer's terminal 3′ base, or no probe site within the product | yes, as a failure |
| `no_amplicon` | no primer pair in correct orientation and size range | **excluded** |
| `indeterminate` | too many ambiguous record bases beneath an oligonucleotide to score | **excluded** |

[^1]:
    For hydrolysis-probe chemistries this is arguably incorrect, and a switch
    exists. Detection depends on the probe: one binding poorly reports late or
    not at all, whereas a primer binding poorly still generates product.
    Enabling it for probe chemistries raises detection of documented failures
    from 5/11 to 6/11 with no increase in false positives, at the cost of two
    confirmed positives on a published *Leptospira* validation panel. The
    trade-off is not clearly favourable, so the option ships disabled.

The final two categories are excluded deliberately. A record lacking the
locus, truncated, or dense with ambiguity codes is informative about GenBank
rather than about the assay; including them would render a poor sequencing
year indistinguishable from drift.

### Degeneracy

A degenerate base covering the record's base is scored as a **match**, which is
its purpose. Pool size is reported separately and never counted against an
assay. An ambiguity code in the *record* is likewise never scored as a
mismatch: it is missing information, not evidence of one.

### Product size constraint

A call is constrained to the entry's measured product length within 25%. A
1931 bp product is not a 194 bp assay amplifying. The tolerance was measured
rather than selected: across a complete run, deviation between observed and
declared length shows an inflection near 0.2 and flattens beyond it.

---

## Model assumptions and their limits

One well-supported mechanism and several approximations.

**The mechanism.** A polymerase extends from the primer's 3'-OH, so a mismatch there
sits in the catalytic site, while one near the 5' end costs a little stability
on an oligo with nineteen other matched bases. Weighting by distance from the 3'
end is the right shape — Kwok et al. 1990
([10.1093/nar/18.4.999](https://doi.org/10.1093/nar/18.4.999)) and Stadhouders
et al. 2010
([10.2353/jmoldx.2010.090035](https://doi.org/10.2353/jmoldx.2010.090035)).

**The approximations, in descending order of consequence.**

1. **Mismatch identity is ignored.** Both papers above find identity
   dominates: at the 3' terminus A:A, A:G, G:A and C:C suppress yield by orders
   of magnitude — over 7 Cq in Stadhouders — while T:G, T:C and T:T are nearly
   free, under 1.5 Cq, since a T:G wobble retains stacking. Failing every
   terminal mismatch is therefore correct for approximately half of them.
2. **Penalties are summed**, whereas amplification requires forward *and*
   reverse binding and detection additionally requires the probe. These are
   serial conditions. Three trivial mismatches, one per oligonucleotide, score
   identically to one near-terminal mismatch of large effect.
3. **A single table covers every chemistry** — 155 conventional PCRs and 60
   probe assays. A hundredfold yield loss is a missed Ct in qPCR and frequently
   still a visible band after 40 cycles of endpoint PCR. Both receive `fail`.
4. **Probe geometry is not modelled.** A minor-groove binder adds
   approximately 15–20 °C of Tm and makes short probes viable, so an MGB probe
   tolerates mismatches an unmodified oligonucleotide of equal length would
   not.
5. **Mismatch effects are additive**, so two adjacent mismatches — which
   disrupt a contiguous run of base stacking — are under-penalised relative to
   two separated ones.

For an assay near a decision boundary, these are the grounds for independent
verification rather than acceptance of the call.

---

## Per-assay drift call

Calls are grouped by deposit year, and detection within the recent window is
compared with all earlier records.

### Interval-based flagging

A wildlife assay may have five records across two years. Three failures is
40%, which appears alarming and is uninformative: the interval spans
approximately 10% to 70%. Flagging on point estimates would bury genuine
signal under noise from precisely the sparsely sequenced targets the tool
exists to serve.

An assay is therefore flagged only where the **upper** bound of its recent
interval falls below the threshold. The data must be inconsistent with
continued function, not merely compatible with failure.

The interval is Wilson rather than the textbook normal approximation, which
misbehaves near 0 and 100% — it can return bounds outside the possible range,
and when everything detects it collapses to zero width and claims certainty from
a handful of records. The change from baseline uses the Newcombe interval, built
from two Wilson intervals, which stays sensible where baselines near 100% live.
Both are closed-form, so every number on this site can be checked by hand from
the counts printed beside it.

### Status definitions

| status | rule |
|---|---|
| **declining** | recent interval below 90%, the change interval entirely below zero, a fall of at least 5 points, **and** the assay cleared 90% in some earlier year |
| **low coverage** | below 90% but not measurably lower than before, or with no working baseline |
| **watch** | below 90% with an interval that still spans it |
| **insufficient data** | fewer than 15 evaluable records; reported, never flagged |
| **no recent data** | nothing deposited in the window |
| **stable** | none of the above |

The final condition on `declining` is what preserves the term's meaning.
Without it, 14 of 37 assays flagged in an early run were pan-family consensus
PCRs that never covered the organism they were screened against. A fall from
14% to 0% reflects a change in which clades were deposited, not degradation of
the assay.

### Adaptive window

The recent window is 24 months; for an assay with fewer than 15 evaluable
records it extends in annual increments to a maximum of five years, and each
assay reports the window applied.

Without this, a sparsely sequenced target is assessable only immediately after
a deposition burst. *Batrachochytrium dendrobatidis* ITS records arrive 56 in
one year and four thereafter, so the standard assay read "stable" in 2014 and
"insufficient data" subsequently, on no change in the assay. Widening adds only
older records and never removes recent ones.

---

## Estimand

The intervals assume records are independent draws from the population on which
the assay is used. Neither condition holds.

**Sequence databases sample sequencing effort rather than circulating
diversity.** An outbreak deposits hundreds of near-identical sequences from a
single transmission chain; steady endemic circulation deposits none.

**Deposition is correlated with detection.** A locus is frequently sequenced
*because* an assay amplified it, and a variant escaping PCR may never be
deposited. This biases the procedure toward optimism, making `declining`
strong evidence and `stable` weak evidence. The asymmetry is the most
consequential point on this page.

**A single proportion per assay is the wrong summary for most documented
failures.** Published failures are almost always specific to a clade, region or
host. Each assay page therefore carries a per-lineage breakdown where more than
one lineage is represented, and the worst adequately sampled lineage can
override an otherwise reassuring pooled verdict.
