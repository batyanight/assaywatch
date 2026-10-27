# A failing lineage cannot overturn a verdict that never cleared the threshold (2026-10-20)

The open estimand question from `docs/journal/2026-10-19-taxid-artefacts.md`: should a
failing lineage be allowed to override a **pooled `low coverage`** to `declining`?
`declining` claims a fall, and a pooled `low coverage` is the statement that this
assay was never shown to work on this denominator, so there is no fall for the
lineage to be evidence of. **Evidence:** `results/2026-10-17/calls.tsv.gz` with
current IDs, species roll-up and the working-baseline gate on.

## How often this fires, and in which direction

19 lineage overrides fire at 2026-10-17. **17 of them sit on a pooled `low
coverage`**, 2 on a pooled stable/watch (Orthopox ATI, Parvovirus dependovirus),
and none on `insufficient data`.

In **6 of the 17 the "failing" lineage detects at or above the pooled share**. The
override is then flipping `low coverage` to `declining` on the evidence that a
*better than average* slice of the pool sits below an absolute 90% threshold.
Nothing in that is a fall. One case is CDV_H_gene_Mueller_2011_2, where the firing
lineage holds all 189 of 189 recent records at 59.8%, identical to the pooled
59.8%: the override is re-reading the pooled measurement and renaming it.

The tier-2 case is sharper. Enterovirus VP3/VP1 round2 as of 2018-09-30 reads
pooled 10.7% of 2,501 records, and the pooled note says in as many words *"fell
measurably, but never reached the 90% threshold in any earlier year, so this is not
drift"*. The override then fired on taxid 1193974 "Human enterovirus", 33 records
at 0.0% — three records over the per-lineage floor, and precisely the NCBI
reclassification artefact that `docs/journal/2026-10-19-taxid-artefacts.md` identified as
a bucket of untyped coxsackievirus A6. The literature says this assay works.

## The rule, and the four alternatives that lost

Shipped: **when the pooled verdict is not stable or watch, a failing lineage may
override it only if that lineage itself cleared the threshold in an earlier
measured year.** This is the rule the project already settled at the pooled level
(`lineage.require_working_baseline`, "a fall from a baseline that never cleared it
is not drift") applied to the denominator the override actually claims. A lineage
new to the archive cannot carry it: it has no history to have fallen from. It is
gated on the same config flag, because it is the same rule, and `lineage.py` gained
`lineages_ever_covered` — the positive counterpart of `lineages_never_covered`, and
deliberately not its complement, since a lineage with no measured year belongs to
neither set.

Tier-2 against `docs/validation-cases.tsv`, all candidates measured:

> **Re-verified 2026-10-20** (`docs/journal/2026-10-20-tier2-rename-resolution.md`). The
> shipped row below re-measures exactly, 4/11 and 10, on `results/2026-10-20/`.
> Do not try to reproduce it on a calls table older than the assay-ID renames
> without a current `scripts/retrospective.py`: the version that shipped before
> that date scored a case whose id had been renamed as `no data`, which reads as
> `undecided`, and on `results/2026-10-17/` that silently hid 13 of the 49 cases
> — including **CDV_P_gene_Scagliarini_2007 2021-07-06, the only catch any
> override candidate can move**. A re-measurement under that bug reads 3/11 and
> 9, makes the three candidates rejected below look free, and would revert this
> rule on evidence that had disappeared. `retrospective.py` now refuses to print
> a matrix when a case id matches nothing.

| | failures caught | disagreements | current assays moved |
|---|---:|---:|---:|
| before | 4/11 | 12 | — |
| **shipped: lineage must have worked** | **4/11** | **10** | **2** |
| never override a weak pooled at all | 3/11 | 7 | 17 |
| override but don't call it declining | 3/11 | 7 | 17 |
| lineage share must be ≤ pooled | 3/11 | 12 | 6 |
| lineage share must be < pooled | 4/11 | 11 | 5 |
| both gates (worked **and** < pooled) | 4/11 | 9 | 7 |
| measure the fall on the lineage itself | 3/11 | 9 | 11 |

Two rows move under the shipped rule, both improvements, nothing lost: Enterovirus
round2 2018-09-30 (`works`: declining/DISAGREES → low coverage/weaker) and
Coronavirus RdRp round2 2024-03-29 (`partial`: declining/DISAGREES → low
coverage/agrees). Current statuses: 2 of 201 move, both `declining` →
`low coverage` with the gap named — Pan_mycoplasma_16S_All_Van_1992 and
PAPILLOMAVIRUS L1 Forslund 1999.

**Why the more principled candidates lost.** Refusing the override outright, or
keeping it under a different status name, both answer the question correctly in
principle and both **drop the CDV_P_gene_Scagliarini_2007 2021 catch** — the one
case in the set documented as real drift on its own target. By the project's own
rule, a candidate that loses a documented catch is a bad candidate.

Checked case by case on 2026-10-20, and it is narrower than it reads: of the four
`fails` the tool catches, **CDV_P 2021 is the only one that comes from an
override at all**. Paramyxovirinae L round1 (pooled 18.5% of 1,056), round2
(4.5% of 755) and Forslund L1 (79.3% of 715) are all caught by the pooled
verdict with `lineage_override` false, so no override candidate can move them.
The whole comparison above therefore turns on a single case, whose `mechanism` is
`drift` — so its `low coverage` earns no coverage excusal in `classify()` and the
catch is lost outright, not downgraded. And that case is itself an above-pooled
override: the firing lineage holds all 83 records at exactly the pooled 80.7%.
The one case justifying the rule is an instance of the pattern point 2 below
wants to gate out.

The most instructive loss is the one that makes the override measure a fall, with
the same Newcombe bound and `min_decline` the pooled test uses. It also loses
CDV_P, and the reason matters: that lineage is the whole pool, and it goes 82.2%
baseline → 78.7% recent, a fall of 3.5%, under the 5% `min_decline`. **The one
documented drift catch the override rescues is rescued precisely because the
override does not measure a fall.** That inconsistency is currently load-bearing.

"Report it as something other than `declining`" turns out to be numerically
identical to refusing the override, and it cannot be fixed by inventing a status:
`scripts/retrospective.py` maps any unrecognised status to `undecided`, which would
convert the coverage-mechanism catches (Forslund, Hellgren, Kolesnik) from `agrees`
into non-catches. A new status word costs catches through the scoring rubric rather
than through the science, so `classify()` would have to be extended first.

## What this rests on, and what is still missing

1. **One case separates the shipped rule from refusing the override entirely.**
   CDV_P 2021 is the only validation case where a lineage that used to work is now
   failing under a pooled `low coverage`, and its fall is 3.5% — below the
   project's own `min_decline`. A second such case is what would turn this from
   defensible into demonstrated.
2. **Adding the "< pooled share" gate would be better** (9 disagreements, same
   4/11) and is the only candidate that stops an above-pooled lineage driving
   `declining`. Not shipped: its extra gain rests on a single row, and the `<`
   versus `≤` boundary was fixed by one case where the lineage share equals the
   pooled share to the digit. A threshold whose sign is set by one row is what the
   top of `config.yaml` warns against. Cases for the above-pooled pattern — 6 of
   the 17 — are what would approve it.
3. **`scope_taxids` from the design papers** would shrink the 17 directly rather
   than adjudicate them. Several fire on a lineage outside the assay's stated
   range: *Papillomaviridae* sp. for Forslund's cutaneous set, *Mycoplasma ovis*
   for a 1992 pan-mycoplasma 16S set. Curation removes the case before any
   estimand rule has to decide it.
4. **The reclassification artefact is still unfixed.** The new rule suppresses
   1193974 here, but incidentally: the next minted taxid with ≥30 records and no
   earlier year reproduces the enterovirus bug.
5. **CDV_H_gene_Mueller_2011_2 stays `declining` under every candidate tested**,
   on a lineage that is the entire pool at the pooled share. The existing
   whole-pool rule would catch it but is gated on the assay never having worked,
   and CDV_H worked earlier. No validation case covers it; flagged, not fixed.
