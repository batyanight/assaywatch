# The Bd miss priced: 297,651 rows are discarded with a credible site, gaps are worth 0.046%, and Bd's own geometry cannot be measured

Phase 1 of the Bd-miss plan. **Measurement only** — no call, verdict, threshold or
config changes, and nothing written to `results/`.

> **THIS DOCUMENT CORRECTS ITSELF, same day.** Its first version reported a Bd probe-site
> table (122 judgeable of 461, 94 failing, 25 indel-explained) and those numbers are
> **WITHDRAWN**. They came from a probe offset that one record in three agreed with. The
> section "the method's limit, and Bd is inside it" explains what went wrong and why the
> corrected answer is that Bd is unmeasurable by this route. The two findings that do not
> depend on an offset — the discarded population and the indel rate — are unchanged.

`docs/2026-10-23-wave3-bd-miss.md` diagnoses the 2017 Bd miss as **two** modelling
choices: scoring only records that hold the whole amplicon, and matching without gaps. It
proposes fixing both together. Phase 1 asks what each is worth separately.

## 1. The ungapped half is worth almost nothing registry-wide

Re-measured with `scripts/indel_check.py` on current data (85,615 sampled calls across
204 assays, seed 1, 300 per assay). **This measurement involves no offset and is not
affected by the correction above.**

| | |
|---|---|
| evaluable records across reported assays | 932,856 |
| sampled calls carrying an indel | 692 |
| estimated `fail` calls an indel would explain | **426, or 0.046% of evaluable** |
| estimated `no_amplicon` rows an indel would turn into an amplicon | 921 |

That reproduces the 2026-10-04 conclusion — "a clean single-base indel explains well
under 1% of evaluable records for every assay but three" — so the verdict that gapped
scoring is not worth building for its own sake still stands.

What the script is good for is registry QA, which is also what 2026-10-04 concluded:

| assay | evaluable | fails an indel explains | share |
|---|---:|---:|---:|
| `NOSEMA_bombi_SSU_Kato_2020` | 81 | 19 | 23.5% |
| `NOSEMA_ceranae_SSU_Martin-Hernandez_2007` | 876 | 101 | 11.5% |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` | 2,075 | 145 | 7.0% |
| `Cryptosporidium_18SrDNA_Xiao_1999_round2` | 1,178 | 19 | 1.6% |
| `CIRCOVIRUSES_..._Rep_Gene_Mankertz_2000_round2` | 6,458 | 63 | 1.0% |

A consistent same-position indel across a whole record set is an oligo typo, not biology.
`POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` is worth singling out: section 6 of this plan
measured the same entry as reaching `detect` **zero** times in 14,537 records, and a 7%
indel share is a second independent signal that the entry is wrong rather than that
polyomaviruses have drifted. `B_salamandrivorans_..._Blooi_2013` reads 16.7% and is
noise: one record of six evaluable.

## 2. The amplicon-level half discards a tenth of the table

Counted exactly from `results/2026-10-26/calls.tsv.gz`, using the classes
`score.classify_exclusion` defines. **No offset is involved here either.**

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

`chance_only` is excluded on purpose: those records do have primer sites, but their pairs
are indistinguishable from chance, and admitting them is the error the 2026-10-25
chance-pair work exists to prevent.

`no_site` is four fifths of the discarded population and genuinely unreachable, which
bounds the whole idea. Site-level evaluation is not a way to recover most of what the
screen drops. It is a way to reach a specific tenth of it.

## 3. The method's limit, and Bd is inside it

To judge a probe in a record that lacks a primer, the probe has to be *placed* without
its amplicon. The Bd investigation did that with one hand-picked reference record
(`MW147112.1`). `scripts/measure_site_level.py` tried to make that reproducible by taking
the modal probe-to-reverse-primer offset over the assay's own records. **Two bugs in that
idea produced the withdrawn numbers, and the second one is not fixable for Bd.**

**Bug one: the offsets were pooled across orientations.** A record deposited in the
reverse orientation mirrors every site, so the probe sits at a negative offset from the
reverse primer in one orientation and a positive one in the other. Bd's ITS deposits come
in both. Pooling them mixed **+93 with −95**, and the "mode" of mutually contradictory
numbers placed the probe nowhere near its real position. Nothing then matched there, so
every record counted as failing, and a gapped alignment against the wrong window invented
an indel rate. Offsets are now keyed by the anchor's strand.

**How it was caught**, because it would otherwise have shipped: the first cross-assay run
reported `USUTU_ssRNA_NS1_realtime_Jost_2011` as **42 of 42 probe failures explained by an
indel**, which is too clean to be real. A hand check of the same records found the probe
at gapped alignment **cost 0** — present and perfect. The Usutu figure was never
published; it is recorded here because it is what exposed the Bd figures beside it.

**Bug two, and the real limit: an offset needs full-amplicon records, and Bd has three.**
Of Bd's 9,493 archived records, exactly **three** hold a clean forward site, reverse site
and probe site together, and they disagree: +93, −95, −84. One observation per value.
`usable_offsets` now requires at least 5 concordant observations and a 60% majority, so
**Bd is reported as unmeasurable** rather than measured wrongly.

That is not a defect to work around. It is the same fact as the case itself: Bd's probe
site cannot be located from Bd's own deposits because almost every Bd deposit is
truncated. **The assay that motivated site-level evaluation is the assay whose geometry
this approach cannot calibrate**, which is exactly why the case doc needed a hand-picked
reference, and it means the case doc's three hand-read records remain the only sequence
evidence of the Bd probe-site deletion. The count is three, not 25.

A sound Bd measurement needs a different anchor — the declared amplicon geometry plus the
reverse site, or a curated full-length reference recorded as such — and that is a design
decision for Phase 2, not a measurement this session can make.

## 4. What this says about Phase 2

- **Site-level evaluation is the valuable half.** 297,651 rows reachable, measured
  exactly, and that number does not depend on any of the above going right.
- **Gapped alignment is not a peer of it.** 0.046% registry-wide does not justify it as a
  general scoring change. Whether it earns its place *inside* site-level evaluation is now
  an open question rather than a measured one, because the measurement that suggested it
  did (25 of 94 on Bd) is withdrawn.
- **Placing a lone probe is a harder sub-problem than the case doc implies**, and it is
  the first thing Phase 2 has to solve. The case doc lists it as an open design question;
  this session established that the obvious answer does not work for the motivating assay.
- **It cannot be replayed, confirmed rather than predicted.** No `no_amplicon` row carries
  any site coordinate: `fwd_site`, `rev_site` and `probe_site` are empty on all 1,789,100
  of them, because there is no winning amplicon to write them from. So every iteration of
  a site-level rule costs a full rescreen, exactly as `scripts/rescore.py`'s replay
  boundary says a search-layer change must.

Phase 2 stays stopped, and the reasons are now measured: it is a search-layer and estimand
change on the denominator axis, it cannot be priced cheaply, and the denominator axis
produced three failed candidates on 2026-10-25.

## 5. Two open design questions, and one that got harder

The case doc lists three open questions. The first was *how to locate a site in a
truncated record without the partner primer to anchor it* — and this session's answer is
that the assay's own geometry cannot supply it where it is most needed. That question is
now **harder, not settled**, and is the critical path for Phase 2.

The other two are unchanged and both real:

- **A lone site needs its own credibility test.** The archive-scale multiplicity problem
  from wave 2 applies with force to a 15-mer probe, so nothing here reports a site-level
  failure *share*, and the per-assay counts below are counts of judgeable failing sites,
  never coverage figures.
- **How a site-level failure enters a verdict, if at all**, versus being reported beside it
  the way degeneracy and thermodynamics are.

## 6. What was not done

No verdict moved. The Bd `fails` label at 2017-03-31 is unchanged, and the case doc's
caution about it stands and is now stronger: the label is sound but rests on three records
of sequence evidence, and the wet-lab evidence does not by itself separate sequence
mismatch from the nested protocol's greater sensitivity. That is for the maintainer to
weigh.
