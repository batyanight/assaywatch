# Recalibration: lineage estimand vs validation cases

**Date:** 2026-10-18
**Run:** `scripts/retrospective.py --cases docs/validation-cases.tsv`
**Pipeline summary:** 213 assays — 66 stable, 63 declining, 12 watch, 17 low
coverage, 41 insufficient data, 14 no recent data.

## Result

50 validation cases. The tool judged 33 and declined 17 (insufficient data or
no recent data). Of the 33 judged:

| verdict     | count | rate  |
|-------------|------:|------:|
| agrees      |    15 |  45%  |
| weaker      |     4 |  12%  |
| DISAGREES   |    14 |  42%  |

"Weaker" means the tool said low coverage where the literature said works or
partial — not wrong, just a softer call than the paper's.

### True positives (6 of 12 known failures caught)

| assay | as_of | status |
|-------|-------|--------|
| Paramyxovirinae Tong round1 | 2019-02-01 | declining |
| Paramyxovirinae Tong round2 | 2019-02-01 | declining |
| CDV Scagliarini | 2021-07-06 | declining |
| Papillomavirus L1 Forslund | 2011-06-14 | declining |
| Pan-hemoparasite Hellgren | 2016-12-31 | declining |
| Pan-Plasmodium Hellgren | 2016-12-31 | declining |

### False negatives (2): literature says fails, tool says stable

| assay | as_of | status | root cause |
|-------|-------|--------|------------|
| Bd Boyle 2004 | 2017-03-31 | stable | All Bd haplotypes share taxid 109871; per-lineage analysis cannot separate them. Needs sequence-cluster lineages. |
| Influenza A Matrix 2003 | 2010-05-30 | stable | Subtypes share a taxid. Same class of problem. |

Both are the **taxid-resolution ceiling**: the lineage estimand groups by NCBI
taxid, and when functionally distinct lineages share a taxid, the tool cannot
see the within-taxid divergence that causes the failure.

### False positives (8): literature says works, tool says declining

| assay | as_of | root cause |
|-------|-------|------------|
| Pan-flavivirus NS5 round1 | 2017-03-31 | pan-family scope |
| Pan-flavivirus NS5 round2 | 2017-03-31 | pan-family scope |
| Pan-flavivirus NS5 round1 | 2018-05-31 | pan-family scope (partial→declining) |
| Pan-coronavirus Lan round1 | 2020-01-08 | pan-family scope |
| Pan-herpes Polymerase round2 | 2018-11-07 | pan-family scope |
| Adenovirus Pan Polymerase round1 | 2019-04-30 | pan-family scope |
| Enterovirus VP3_VP1 round2 | 2018-09-30 | pan-family scope |
| CDV Scagliarini | 2019-10-31 | lineage variant (one CDV genotype) |
| Paramyxovirinae Tong round1 | 2024-12-26 | pan-family scope |

All but CDV Scagliarini (which appears in both TP and FP at different dates)
are pan-family assays where the tool counts failures from taxa outside the
assay's design scope. The 2026-10-04 investigations documented this pattern
for ranavirus (Santee-Cooper clade fish ranaviruses) and CDV (one recurring
genotype).

### Partial overcalls (4): literature says partial, tool says declining

| assay | as_of |
|-------|-------|
| Pan-coronavirus Lan round1 | 2021-08-27 |
| Pan-coronavirus round2 | 2024-03-29 |
| Pan-flavivirus NS5 round1 | 2018-05-31 |
| Polyomavirus VP1 Johne | 2019-08-29 |

Same pan-family scope issue. The tool sees genus-level gaps as drift.

### Undecided (17): tool declined to judge

12 works, 4 fails, 1 partial. These are assays with too few records in the
recent window. The `min_records_for_drift` threshold controls this: lowering
it would judge more cases but with wider confidence intervals.

## Diagnosis

The lineage estimand did not change the FP/FN picture. The 14 disagreements
break into two structural problems, neither fixable by threshold tuning:

1. **Pan-family scope (12 of 14 disagreements).** The tool's denominator is
   every sequence under the retrieval taxid. For a pan-family assay whose
   published claim covers only a subset of that diversity, failures from
   out-of-scope taxa inflate the decline signal. Fix: a registry-level concept
   of which taxids are "in scope" for each assay, so out-of-scope failures are
   counted but not scored.

2. **Taxid-resolution ceiling (2 of 14 disagreements).** When functionally
   distinct lineages share a taxid (Bd haplotypes, influenza subtypes), the
   per-lineage analysis cannot see the divergence that causes the failure. Fix:
   sequence-cluster lineages — group within a taxid by actual sequence
   similarity at the primer/probe sites.

## Threshold decision

**No change to `config.yaml` thresholds.** The current thresholds correctly
separate the cases where the tool has enough information to judge. The errors
are in what the tool measures, not where it draws the line.

The `min_records_per_lineage` floor of 20 is reasonable: lowering it would not
rescue the 2 FNs (both have enough records, the problem is taxid granularity)
and would add noise from small-sample lineages.

## Next steps (not this session)

1. **Pan-family scope logic** — add an optional `scope_taxids` field to the
   registry schema. When present, only records under those taxids count toward
   the drift denominator. Out-of-scope records are reported separately as
   "cross-reactivity" rather than "drift". This resolves ~12 of the 14
   disagreements.

2. **Sequence-cluster lineages** — for assays where the target species has
   known within-taxid diversity at the primer sites (Bd, influenza), cluster
   the retrieved sequences by primer-site identity and treat each cluster as a
   lineage. This resolves the remaining 2 FNs.

3. **RuntimeWarning in lineage.py:158** — `comb(n, k) * p^k * (1-p)^(n-k)`
   overflows or hits NaN for some lineage with large n_evaluable. Needs a
   log-space computation or scipy.stats.binom_test fallback.
