# The influenza sublineage chain works — five subtypes read below 90% inside a 97% pool — and it exposed a defect the probe switch left behind

2026-10-27. `lineage.sublineage` has shipped `{}` since the resolver chain was built,
with the influenza matrix assay written into `config.yaml` as a commented worked example
and never enabled. The roadmap item: the assay is one lineage of 74,861 records reading
stable at 97.1%, while the paper `related-work.md` names as the benchmark found H3N2
carrying a probe-interfering mutation circulating since 2010.

    lineage:
      sublineage:
        INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003:
          chain: [title]
          title: {pattern: '\((H\d+N\d+)\)'}

    python -m assaywatch.lineage_report results/2026-10-26/calls.tsv.gz --config <that> ...

## It works

Record titles in the influenza archive carry the subtype in parentheses —
`Influenza A virus (A/Wisconsin/52/2026(H3N2)) segment 7 ...` — and the title resolver
labels 68,225 of the 74,861 records by it (the 6,636 it cannot label stay under
`Influenza A virus`). **57 subtype lineages** appear in the per-lineage table where there
was one. Those with ≥ 30 evaluable records and a share below the 90% threshold:

| lineage | evaluable | detected | share | 95% CI |
|---|---:|---:|---:|---|
| **H1N2** | 1,917 | 1,383 | **72.1%** | 70.1–74.1% |
| H16N3 | 193 | 152 | 78.8% | 72.5–83.9% |
| H3N1 | 83 | 71 | 85.5% | 76.4–91.5% |
| **H5N1** | 3,214 | 2,814 | **87.6%** | 86.4–88.7% |
| H13N6 | 250 | 219 | 87.6% | 82.9–91.1% |

Against that, H1N1 at 97.3% of 27,725 and H3N2 at **99.4% of 38,771**. So the pooled
97% was averaging a swine-lineage H1N2 at 72% and the H5N1 clade at 88% into the two
human seasonal subtypes that make up 89% of the records. That is the lineage-conditional
estimand doing exactly what its design document said it was for.

**The H3N2 claim is not reproduced here, and that needs saying plainly.** The
benchmark paper found a probe-site mutation in H3N2 from 2010; this archive's H3N2
records read 99.4% detected by this assay. Either the mutation sits where the penalty
rule does not weigh it (the probe's centre vs its ends), or the stored probe is not the
one that paper tested, or the 2010 lineage is a small fraction of 38,771 records most of
which are later. The per-year table for the H3N2 lineage alone would separate those, and
is the next thing to look at. What the chain does reproduce is the *shape* of the
finding — a subtype-specific failure hidden by a pooled share — just not in the subtype
the literature named.

## What it exposed

**The lineage report still counts `reduced` as detected for every assay.**
`lineage.py` line 403: `n_det = sum(1 for c in lineage_calls if c["call"] in ("detect",
"reduced"))`, hard-coded. Since this morning `drift.reduced_not_detected_for:
[hydrolysis_probe, mgb]` makes a `reduced` probe call *not* a detection in the pooled
share — which is why the main report has this very assay at **6.5%** and `declining`,
while the lineage table above has every one of its subtypes between 72% and 100%. Same
run, same calls, two definitions of "detected", and the lineage one feeds
`worst_lineage_verdict`, which can override a pooled status. For the 51 probe-bearing
entries the lineage layer is now reading a different assay from the one the verdict
describes.

This is a defect the probe switch introduced by omission: the switch was wired through
`drift.YearStats.detected_calls` and nothing else. The fix is to thread the same
`detected_calls` into `lineage.py`'s counting — one function, a per-assay argument.

> **Fixed the same evening.** `assaywatch.triggers.source_names("screen")` lists the
> fifteen modules the screen signature hashes, and `lineage.py`, `drift.py` and
> `lineage_report.py` are not among them, so the fix did not have to wait for the run.
> `per_lineage_stats`, `lineages_never_covered` and `lineages_ever_covered` now take
> `detected_calls`; `drift.py` passes its own, and `lineage_report.py` builds the
> per-assay map from the registry's chemistry exactly as `report.py` does. Four tests pin
> that the numerator moves and the denominator does not. The table above was rendered
> BEFORE the fix and is kept as it was, because it is what exposed the defect; the
> subtype shares for this probe assay will read lower once re-rendered.

## Decision

Not enabled. `config.yaml` says an entry here "can turn a verdict into `declining`, so
like any threshold here it goes through tier-2 validation before it is added", and
tier-2 is unchanged by it today (the assay is already `declining` on the pooled share).
The reasons to wait are the two above: the lineage counts it would drive verdicts from
are using the wrong numerator for this chemistry, and the subtype the literature flagged
is not the one the table flags. Enable it after the numerator is fixed, re-read the
table, and then decide on evidence that is internally consistent.
