# Wave 3: the influenza miss is `reduced`, not a lineage (2026-10-23)

Plan item 3.5: turn on the one `sublineage` resolver that is written and tested — the
title pattern `\((H\d+N\d+)\)` for `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003` —
and re-run tier-2. The validation case (Slomka 2010,
doi:10.1111/j.1750-2659.2010.00149.x) records the M-gene reverse primer carrying
mismatches at about five positions in 2009 pandemic H1N1, amplification efficiency
outside acceptable limits, and the authors concluding it should not be used for H1N1v.
The tool calls the assay `stable` as of 2010-05-30.

## The resolver changes nothing

With and without it, as of 2010-05-30: **97.7% detected of 2,784 recent evaluable
records, `stable`.** Identical.

## Why: the pandemic records are `reduced`, and `reduced` counts as detected

Of 4,651 archive records titled `/2009(H1N1)` and deposited inside that window, the
screen calls **1,295 `reduced`, 14 `fail`, 1 `detect`** (the rest are `truncated` or
`no_site`). Grouping by subtype makes the lineage visible but not failing, because
`drift.py` counts `reduced` as detected — "it amplifies, just later". Per subtype, in
that window:

| subtype in title | n | detect | reduced | fail |
|---|---:|---:|---:|---:|
| H1N1, titled /2009 | 1,310 | 0.1% | **98.9%** | 1.1% |
| H1N1, other years | 193 | 24.4% | 72.0% | 3.6% |
| H3N2 | 145 | 11.0% | 86.2% | 2.8% |
| H5N1 | 162 | 94.4% | 1.9% | 3.7% |
| H5N2 | 126 | 96.8% | 2.4% | 0.8% |
| H7N2 | 79 | 97.5% | 0.0% | 2.5% |

The screen *does* separate pandemic H1N1 from the avian subtypes, exactly as Slomka
describes, and the separation lands on the `detect`/`reduced` boundary rather than on
`reduced`/`fail`. No lineage grouping, and no multiplicity correction, can reach a
failure the call vocabulary has already classified as success.

This is README guess 3 — one penalty table for 161 conventional and 44 probe assays —
with a number on it. For a probe assay "amplifies, just later" is not success: a Cq
shift past the cutoff is a negative result, which is what Slomka measured.

## The counterfactual, measured and NOT shipped

Rewriting `reduced` to `fail` for the 44 probe-chemistry assays only (101,336 rows of
the frozen table) converts the influenza case from miss to catch:

| | current | counterfactual |
|---|---|---|
| documented failures caught | 5/11 = 45% | **6/11 = 55%** (95% CI 28%-79%) |
| caught by `declining` itself | 2/11 | **3/11** |
| PPV of `declining` | 2/9 = 22% | 3/10 = 30% |
| working assays called `declining` | 5/32 | 5/32 (unchanged) |

No `works` case newly disagrees, so it passes the M1 gate. **It is still not shipped**,
for two reasons:

1. **It is a threshold change measured on the 49 cases.** Wave 4 exists to stop exactly
   this. One case moves; the interval on 6/11 (28%-79%) overlaps 5/11 (21%-72%) almost
   entirely.
2. **The blast radius is large and one footprint dominates it.** 9 statuses move,
   including `MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004` from `stable` at 99.9% to `declining`
   at 23.1%. 8,806 of its 8,808 `reduced` calls carry one footprint: a single probe
   mismatch 10 bases from the probe's 3' end, penalty 2.0. Whether that one mismatch
   costs an MGB probe its Cq cutoff is precisely what this pipeline cannot say, and
   `--thermo` is reported but never scored. Reclassifying ~9,000 records on it, to gain
   one validation case, is the trade the conventional override already lost on
   2026-10-19.

## What this is worth

- **The influenza miss now has a mechanism**, and it is in the call vocabulary, not the
  statistics: a probe-chemistry `reduced` is counted as detected.
- **Both of wave 3's documented misses are scoring problems.** Bd: amplicon-level,
  ungapped. Influenza: `reduced` as success for a probe assay. Neither is reachable by
  any lineage, window or denominator setting.
- **It is the second strong argument for per-chemistry calls**, alongside the Usutu case
  (`docs/2026-10-23-wave3-usutu.md`), which pulls the other way: there the conventional
  assay was scored too harshly. Together they say the single table is wrong in both
  directions at once, which is what `scoring.by_chemistry` exists for and what
  `docs/bayesian-scoring-plan.md` C2 would estimate rather than hand-set.
- **For the C2 corpus:** the pandemic-H1N1 footprint is a within-family negative with a
  published efficiency measurement, and the Monkeypox probe footprint is a within-family
  *positive* (no failure reported for it). Both are the scarce kind.

## Not done

`lineage.sublineage` stays `{}`. The resolver works; it has nothing to reveal here while
`reduced` counts as detected, and turning it on would add lineages to every multiplicity
family for no measured gain. Revisit after per-chemistry calls.
