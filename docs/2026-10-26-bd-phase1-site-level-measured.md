# The Bd miss priced: the amplicon rule discards 297,651 rows, and gapped matching is worth 0.046%

Phase 1 of the Bd-miss plan. **Measurement only** — no call, verdict, threshold or
config changes, and nothing written to `results/`.

`docs/2026-10-23-wave3-bd-miss.md` diagnoses the 2017 Bd miss as **two** modelling
choices: scoring only records that hold the whole amplicon, and matching without gaps.
It proposes fixing both together. Phase 1 asks what each is worth separately, and the
answer is that they are worth wildly different amounts — which changes what Phase 2
should be.

## The ungapped half is worth almost nothing registry-wide

Re-measured with `scripts/indel_check.py` on current data (85,615 sampled calls across
204 assays, seed 1, 300 per assay):

| | |
|---|---|
| evaluable records across reported assays | 932,856 |
| sampled calls carrying an indel | 692 |
| estimated `fail` calls an indel would explain | **426, or 0.046% of evaluable** |
| estimated `no_amplicon` rows an indel would turn into an amplicon | 921 |

That reproduces the 2026-10-04 conclusion — "a clean single-base indel explains well
under 1% of evaluable records for every assay but three" — and so the verdict that
gapped scoring is not worth building for its own sake still stands.

What the script is actually good for is registry QA, which is also what 2026-10-04
concluded. The outliers by share of their own evaluable records:

| assay | evaluable | fails an indel explains | share |
|---|---:|---:|---:|
| `NOSEMA_bombi_SSU_Kato_2020` | 81 | 19 | 23.5% |
| `NOSEMA_ceranae_SSU_Martin-Hernandez_2007` | 876 | 101 | 11.5% |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` | 2,075 | 145 | 7.0% |
| `Cryptosporidium_18SrDNA_Xiao_1999_round2` | 1,178 | 19 | 1.6% |
| `CIRCOVIRUSES_..._Rep_Gene_Mankertz_2000_round2` | 6,458 | 63 | 1.0% |

A consistent same-position indel across a whole record set is an oligo typo, not
biology. `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` is worth singling out: section 6 of
this plan measured the same entry as reaching `detect` **zero** times in 14,537 records,
and a 7% indel share is the second independent signal that something about that entry is
wrong rather than that polyomaviruses have drifted.

`B_salamandrivorans_..._Blooi_2013` reads 16.7% and is noise: that is one record of six
evaluable.

## The amplicon-level half is worth a great deal

Counted exactly from `results/2026-10-26/calls.tsv.gz`, with the classes
`score.classify_exclusion` defines:

| `no_amplicon` class | rows | reachable at site level? |
|---|---:|---|
| `no_site` — nothing credible for either primer | 1,442,931 | **no**, nothing to anchor on |
| `truncated` — the missing site runs off the end of the record | 230,844 | yes |
| `diverged` — the window is in the record and nothing matches | 63,738 | yes |
| `no_pair` — both primers credible, never facing in range | 3,069 | yes |
| `chance_only` — pairs found, none distinguishable from chance | 48,518 | excluded, deliberately |
| **total** | **1,789,100** | **297,651 reachable** |

So **297,651 rows carry at least one credible primer site and are discarded whole** —
10.9% of all 2,724,036 rows and 16.6% of the `no_amplicon` rows. The `truncated` rows
alone span 185 assays.

`chance_only` is excluded on purpose. Those records do have primer sites, but their
pairs are indistinguishable from chance, and admitting them is exactly the error the
2026-10-25 chance-pair work exists to prevent. Counting them would add 48,518 rows whose
sites nobody should trust.

`no_site` is four fifths of the discarded population and is genuinely unreachable, which
is worth stating because it bounds the whole idea: site-level evaluation is not a way to
recover most of what the screen drops. It is a way to recover a specific tenth of it.

## On Bd, the mechanism is now quantified rather than illustrated

`scripts/measure_site_level.py --assay CHYTRID_Bd_...`:

| | records |
|---|---:|
| discarded by the amplicon rule (`truncated` + `diverged` + `no_pair`) | 461 |
| examined | 461 |
| **probe footprint wholly inside the deposit — judgeable** | **122** |
| probe footprint cut by the record start | 295 |
| probe footprint entirely outside the record | 44 |
| **of the 122, would FAIL the probe** | **94** |
| of those 94, explained by an indel at edit cost <= 3 | **25** |

Three things follow.

**The case doc's hand-read sample generalises.** It reports that for 27 of 33
Table S1 records GenBank does not hold the whole probe site; across all 461 discarded
records it is 339 of 461, the same 73%.

**It names three records with a 3'-end deletion; there are 25.** `AB435217`, `JN870747`
and `AB723981` were found by hand. At edit cost <= 3 the same signature appears in 25 of
the 94 site-level failures.

**And the two halves of the diagnosis interact rather than compete.** Gapped matching is
negligible across the registry (0.046%) and material *inside* the population that
site-level evaluation would newly reach (25 of 94, 27%). Neither finding is visible
without the other: measuring gaps registry-wide says "don't build it", and measuring
gaps inside the truncated population says "you will need it once you look there".

## What this says about Phase 2, and it is not what the plan assumed

The plan treats Phase 2 as one change — "site-level coverage with gapped alignment
feeding the verdict". The measurement splits it:

- **Site-level evaluation is the valuable half** and should be specified first, on its
  own, against the 297,651 rows it reaches.
- **Gapped alignment is a dependency of that half, not a peer of it.** It buys 0.046%
  registry-wide, which does not justify it, and ~27% of the new site-level failures on
  Bd, which does. So it should be built *inside* site-level evaluation and not shipped as
  a general scoring change.

**And it cannot be replayed, which is now confirmed rather than predicted.** No
`no_amplicon` row carries any site coordinate: `fwd_site`, `rev_site` and `probe_site`
are empty on all 1,789,100 of them, because there is no winning amplicon to write them
from. The population can be counted from the table; nothing about where its sites sit
can be. So every iteration of a site-level rule costs a full rescreen, exactly as
`scripts/rescore.py`'s replay boundary says a search-layer change must.

That is the main reason to keep Phase 2 stopped. It is a search-layer and estimand
change on the denominator axis, it cannot be priced cheaply, and the denominator axis
produced three failed candidates on 2026-10-25.

## Two open design questions, one of which this run answers

The case doc lists three open questions for the design doc. One is now settled by method
rather than by argument:

> *how to locate a site in a truncated record without the partner primer to anchor it*

The Bd investigation placed the probe using one hand-picked reference record
(`MW147112.1`), which is the single part of its method that could not be reproduced.
`measure_site_level.py` takes the **modal offset over the assay's own detecting
records** instead, so the anchor is the assay's own geometry, and an assay with no record
holding all three sites is skipped and said so rather than anchored on a guess. Four
tests pin that, including that `no_site` must never be counted as reachable — counting it
would inflate the population roughly fivefold.

The two that remain are unchanged and both are real:

- **A lone site needs its own credibility test.** The archive-scale multiplicity problem
  from wave 2 applies with force to a 15-mer probe, and nothing here reports a site-level
  failure *share* for that reason. The 94 above is a count of judgeable failing sites, not
  a coverage figure, and it must not be read as one.
- **How a site-level failure enters a verdict, if at all**, versus being reported beside
  it the way degeneracy and thermodynamics are.

## What was not done

No verdict moved. The Bd `fails` label at 2017-03-31 is unchanged, and the case doc's
caution about it stands: the label is sound but rests on less sequence evidence than its
note implies, and the wet-lab evidence does not by itself separate sequence mismatch from
the nested protocol's greater sensitivity. That is still for the maintainer to weigh.
