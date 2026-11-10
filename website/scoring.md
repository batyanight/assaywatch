# Scoring methods

Two separate judgements are made, and they should stay separate.

**Per sequence:** would these oligonucleotides amplify this record? **Per
assay:** given every record and its deposit date, is predicted detection
falling?

The first is a mismatch penalty; the second is a contrast between two time
windows. Neither measures how the assay performs in a reaction. The gap between
a prediction from sequence and a result from a thermocycler applies to
everything below.

---

## Per-sequence call

Each oligonucleotide is searched against every record on both strands,
allowing up to six mismatches. Where forward and reverse sites face each other
at a plausible product size, the mismatches are converted to a penalty and the
penalty to one of five outcomes.

### Penalty table

A mismatch counts for more the closer it is to the 3′ terminus, where the
polymerase extends:

**Primers**, weighted by distance from the 3′ terminus:

| position | window | cost per mismatch |
|---|---|---|
| 3′ end | last 5 nt | 3.0 |
| middle | positions 6–10 from the 3′ end | 1.0 |
| 5′ region | everything else | 0.5 |

**Probes**, judged by how many mismatches they carry. A hydrolysis probe is never
extended. Its 3′ end carries the quencher or the minor-groove binder, and the
polymerase's 5′→3′ exonuclease cleaves it, so its 3′ terminus has no special
status. What matters is whether the duplex survives, and what one mismatch costs
depends on the kind of probe: 4–6 °C of Tm for a standard 20–30 nt probe, up to
15–20 °C for a 12–18 nt MGB probe
([Kutyavin et al. 2000](https://doi.org/10.1093/nar/28.2.655)).

| probe | one mismatch | two or more |
|---|---|---|
| standard hydrolysis probe | `weak`: the call is at best `reduced` | `blocked`: the call is `fail` |
| MGB or LNA probe | `blocked`: the call is `fail` | `blocked` |

Position within the probe is not weighted. These counts rest on the literature
and have not yet been replayed against documented cases.

Forward and reverse primer penalties are summed, and the total sets the call. The
probe is a gate on top: the call is the worse of what the primers earned and what
the probe allows.

<div class="aw-calls" markdown>

| call | rule | counts as |
|---|---|---|
| `detect` | total penalty ≤ 1.0 | detection |
| `reduced` | ≤ 3.0, or a `weak` probe; amplifies, with an expected Ct shift | detection[^1] |
| `fail` | above 3.0; or a mismatch at a primer's terminal 3′ base; or a `blocked` probe; or no probe site within the product | failure |
| `no_amplicon` | no primer pair in the correct orientation and size range | *excluded* |
| `indeterminate` | too many ambiguous record bases beneath an oligonucleotide to score | *excluded* |

</div>

[^1]:
    Except for MGB assays, where a `reduced` call is not counted as detection
    (`drift.reduced_not_detected_for`). The switch covered standard hydrolysis
    probes too from 2026-10-27 to 2026-11-10; they were removed when the probe
    rule above began to separate one probe mismatch (a Ct shift, counted) from
    two (a failure). That removal has not yet been replayed against the
    documented failure the switch was turned on to catch.

The last two categories are excluded on purpose. A record that lacks the
locus, is truncated, or is dense with ambiguity codes tells you about GenBank,
not about the assay. Including them would make a poor sequencing year look the
same as drift.

### Degeneracy

A degenerate base that covers the record's base is scored as a **match**, which is
what it is for. Pool size is reported separately and never counted against an
assay. An ambiguity code in the *record* is likewise never scored as a
mismatch: it is missing information, not evidence of one.

### Product size constraint

A call must fall within 25% of the entry's measured product length. A
1931 bp product is not a 194 bp assay amplifying. The tolerance was measured, not picked: across a complete run, the deviation between observed
and declared length bends near 0.2 and flattens beyond it.

---

## Model assumptions and their limits

One mechanism is well supported. The rest are approximations.

**The mechanism.** A polymerase extends from the primer's 3'-OH, so a mismatch there
sits in the catalytic site, while one near the 5' end costs a little stability
on an oligo with nineteen other matched bases. Weighting by distance from the 3'
end is the right shape, as Kwok et al. 1990
([10.1093/nar/18.4.999](https://doi.org/10.1093/nar/18.4.999)) and Stadhouders
et al. 2010
([10.2353/jmoldx.2010.090035](https://doi.org/10.2353/jmoldx.2010.090035))
show.

**The approximations, in descending order of consequence.**

1. **Mismatch identity is ignored.** Both papers above find that identity
   dominates: at the 3' terminus A:A, A:G, G:A and C:C suppress yield by orders
   of magnitude — over 7 Cq in Stadhouders — while T:G, T:C and T:T are nearly
   free, under 1.5 Cq, since a T:G wobble retains stacking. Failing every
   terminal mismatch is therefore right for about half of them.
2. **Penalties are summed**, but amplification needs forward *and*
   reverse binding, and detection needs the probe as well. These conditions are
   serial. Three trivial mismatches, one per oligonucleotide, score the same as
   one near-terminal mismatch with a large effect.
3. **A single table covers every chemistry** — 153 conventional PCRs and 60
   probe assays. A hundredfold yield loss is a missed Ct in qPCR and often
   still a visible band after 40 cycles of endpoint PCR. Both receive `fail`.
4. **Probe geometry is not modeled.** A minor-groove binder adds
   approximately 15–20 °C of Tm and makes short probes viable, so an MGB probe
   tolerates mismatches that an unmodified oligonucleotide of the same length
   would not.
5. **Mismatch effects are additive**, so two adjacent mismatches, which
   disrupt a contiguous run of base stacking, are under-penalized compared with
   two separated ones.

For an assay near a decision boundary, these are reasons to verify the call
independently instead of accepting it.

---

## Per-assay drift call

Calls are grouped by deposit year, and detection in the recent window is
compared with all earlier records.

### Interval-based flagging

A wildlife assay may have five records across two years. Three failures is
40%, which looks alarming and tells you little: the interval spans
approximately 10% to 70%. Flagging on point estimates would bury real
signal under noise from the very targets the tool exists to serve, the
sparsely sequenced ones.

An assay is therefore flagged only when the **upper** bound of its recent
interval falls below the threshold. The data must be inconsistent with continued function, not merely be compatible with failure.

The interval is Wilson, not the textbook normal approximation, which
misbehaves near 0 and 100%. It can return bounds outside the possible range,
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

The last condition on `declining` is what keeps the term meaningful.
Without it, 14 of 37 assays flagged in an early run were pan-family consensus
PCRs that never covered the organism they were screened against. A fall from
14% to 0% reflects a change in which clades were deposited, not the assay
getting worse.

### Adaptive window

The recent window is 24 months. For an assay with fewer than 15 evaluable
records it grows in annual steps up to a maximum of five years, and each
assay reports the window it used.

Without this, a sparsely sequenced target can only be assessed right after
a burst of deposits. *Batrachochytrium dendrobatidis* ITS records arrive 56 in
one year and four thereafter, so the standard assay read "stable" in 2014 and
"insufficient data" afterward, with no change in the assay. Widening adds only
older records and never removes recent ones.

---

## Estimand

The intervals assume records are independent draws from the population the
assay is used on. Neither condition holds.

**Sequence databases sample sequencing effort, not circulating
diversity.** An outbreak deposits hundreds of near-identical sequences from a
single transmission chain; steady endemic circulation deposits none.

**Deposition is correlated with detection.** A locus is often sequenced
*because* an assay amplified it, and a variant that escapes PCR may never be
deposited. This biases the procedure toward optimism, so `declining` is
strong evidence and `stable` is weak evidence. This asymmetry is the most
important point on this page.

**A single proportion per assay is the wrong summary for most documented
failures.** Published failures are almost always specific to a clade, region or
host. Each assay page therefore carries a per-lineage breakdown where more than
one lineage is represented, and the worst adequately sampled lineage can
override a pooled verdict that would otherwise look reassuring.
