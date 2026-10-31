# The held-out false alarm has one cause, and 23 assays share it

2026-10-28. Held-out set 2 says the monkeypox G2R generic assay `works` — Mills 2022
validated it on 2022 outbreak clinical specimens across many sample types — and the
shipped config calls it `declining`. That was the one false alarm in three held-out rows.
This traces it, and the trace generalises further than the row does.

**Nothing here changes a threshold.** The lead came from held-out data, and the file's rule
is that no `config.yaml` value may be changed because of it. What follows is a
measurement and a question for the bench panels, which are development data and may be
spent.

## The chain, from verdict to single base

The report's line for the assay: pooled 57.9% of 4,328 recent evaluable records, with the
*Orthopoxvirus monkeypox* lineage at 60.2% of 4,163, and the lineage override turning a
pooled `low coverage` into `declining`.

Where the missing 40% goes, from the calls table (12,000 MPXV records in all):

| call | records |
|---|---|
| `reduced` | 8,954 |
| `detect` | 4,537 |
| `no_amplicon` | 1,984 |
| `fail` | 8 |
| `indeterminate` | 11 |

And the site table, once it was fixed to count detections the way the report does (below):

| oligo | position from 3′ | substitution | records | detected with | detected without |
|---|---|---|---|---|---|
| reverse | **8** | G>A ×8,955 | 8,955 | **0.0%** | 99.8% |
| forward | **21** | A>G ×9,571 | 9,571 | 6.4% | 99.8% |

Of the 8,955 records carrying the reverse variant, **8,947 score `reduced`**, every one
with a reverse penalty of exactly 1.0 and the mispair recorded as `G:T@8`.

So the chain is:

1. the 2022-era MPXV records carry a **G:T wobble at position 8** of the reverse primer,
   and an A>G at position 21 of the forward;
2. position 8 is in the **mid window**, where the penalty is 1.0, and position 21 is in
   the 5′ window at 0.5 — **1.5 in total, which crosses `detect_max: 1.0`**, so the call
   is `reduced`;
3. **M1's mispair discount does not reach it.** `scoring.mispair_penalty` prices G:T at
   0.0, but `score.penalty_for` applies identity only inside the 3′ window — a measured
   decision of 2026-10-22, because applying it everywhere erased internal wobbles across
   whole record sets and cost three documented tier-2 catches;
4. the assay is a hydrolysis probe, so `drift.reduced_not_detected_for` makes `reduced`
   not a detection — detection *is* the probe;
5. 57.9% detected, below the threshold, with a working baseline → `declining`.

Every step is a decision this project made deliberately and recorded. Together they say a
primer carrying one internal G:T wobble and one 5′-window substitution detects nothing,
and the wet lab says otherwise. The config's own comment on `mispair_penalty` quotes Kwok
1990 and Stadhouders 2010 to the effect that a T:G wobble "is nearly free — a T:G wobble
still stacks".

## It is not one assay

Over the 1,291 reported positions in the run's site table, **69 sites across 23 assays**
are the same shape: a mismatch outside the 3′ window, carried by at least 200 records,
where records carrying it are detected under 20% and records without it over 80%. By
status: **36 of those sites sit on `low coverage` assays and 33 on `declining` ones.**

The largest few:

| assay | oligo | pos | records | with | without |
|---|---|---|---|---|---|
| `INFLUENZA_A_ssRNA_NP_Tsukamoto_2010` | forward | 20 | 65,617 | 0.9% | 93.7% |
| `POXVIRUSES_dsDNA_Polymerase` | forward | 8 | 14,116 | 0.0% | 95.7% |
| `MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010` | forward | 21 | 9,571 | 6.4% | 99.8% |
| `POLYOMAVIRUS_dsDNA_VP1_Johne_2005` | reverse | 16 | 6,031 | 2.5% | 89.8% |
| `RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009` | reverse | 14 | 4,780 | 0.0% | 84.8% |

These are not all wobbles — A>C, A>T and T>A appear as often as G>A — so the general
statement is not about identity. It is about **arithmetic**: `primer_mid_penalty: 1.0`
equals `detect_max: 1.0`, so a single mid-window mismatch sits exactly on the
detect/reduced boundary and a second mismatch anywhere pushes past it. That is the same
threshold coincidence the roadmap already records for `primer_3prime_penalty: 3.0` against
`reduced_max: 3.0`, one band down.

## What would settle it, and what would not

**Not this row.** Using Mills to move `primer_mid_penalty`, `detect_max` or the window
would turn held-out data into a second development set, which is the one thing the file
forbids.

**The bench panels can be spent on it**, and that is the pre-registered way: 179 labelled
band/no-band outcomes, of which the question is whether any row turns on a single
mid-window mismatch. If none does, the panels cannot price this and the honest answer is
that the mid-window penalty rests on nothing measurable here — which is what
`config.yaml` would then have to say. The ladder in
`docs/journal/2026-10-24-scoring-strategy-test-plan.md` is where a candidate belongs, with
its kill criterion written first.

**A second held-out row would settle it properly**, and the cheapest source is now the
use-and-report search: a paper that simply uses one of these 23 assays and reports a
result is scoreable, and 22 of them are not monkeypox.

## The site table was lying, in the same way `lineage.py` was

`sitedrift.position_stats` counted a detection as `detect` or `reduced`, hard-coded. Its
`_detected` helper took a `detected_calls` parameter for exactly this reason — its
docstring says so, and names `drift.reduced_not_detected_for` — and **no caller ever
passed one**. So for all 56 probe assays the site table reported the primers' health and
called it detection, while the report next to it did not. On this assay the two commonest
variant sites read **99.97% and 99.98% detected** before the fix and **0.0% and 6.4%**
after.

That is the third place this defect has been found since the probe switch shipped
(`lineage.py` on 2026-10-27, the BPSV hand screen earlier today), which is itself the
finding: a default argument that no caller supplies is not a default, it is a second
definition of a project's central term.
