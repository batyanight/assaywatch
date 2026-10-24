# Wave 2: the diverged denominator was the wrong fix, and why (2026-10-23)

Wave 2 of the plan of attack: the two science switches the earlier docs diagnosed as
the unlock (`count_diverged_as_fail`, `exclude_patent_records`), the two definitions
of failure (`nested.py` vs the drift denominator), and publishing precision. All of it
is report-stage, measured on the frozen table with one-line variant configs through
`scripts/retrospective.py --config`.

## 2.1 `count_diverged_as_fail`: tested, killed, and the prediction behind it was wrong

```
summary (diverged on): fails 5 agree / 3 DISAGREE / 3 undecided   (unchanged)
                       works 8 agree / 7 DISAGREE / 6 weaker / 11 undecided   (was 10 / 5)
```

It caught **no new failure** and turned **two working assays `declining`**
(`CMV_UL55_gB_Prepens_2007_round2` @2007, `RANAVIRUS_..._Pallister_2007` @2012). By the
M1 gate — no documented catch lost, no `works` case newly disagreeing — it fails.
`count_diverged_as_fail` stays `false`.

The prediction that motivated it was mine and it was wrong.
`docs/2026-10-23-baseline.md` said that for Bd, counting `diverged` gives
174/238 = 73% and the Mutnale 2018 miss "likely converts to a catch". That pooled every
deposit year together. Measured per year:

| year | detect | fail | diverged | share, excluded | share, counted |
|---|---:|---:|---:|---:|---:|
| 2012 | 56 | 0 | 0 | 100.0% | 100.0% |
| **2014** | 10 | 0 | **55** | 100.0% | **15.4%** |
| 2016 | 15 | 1 | 0 | 93.8% | 93.8% |
| 2024 | 37 | 0 | 2 | 100.0% | 94.9% |

55 of the 63 `diverged` Bd records sit in **2014**, outside every recent window a
validation case or today's report examines. Bd reads 93.8% on 16 records since Mar 2015
(as of 2017-03-31) and 100% on 17 since Oct 2024, identically with the switch on or off.

### And those 55 records are not Bd ITS at all

They are 2014 JAM81 genome-annotation **mRNAs** — *S-methyl-5-thioadenosine
phosphorylase*, *pyrroline-5-carboxylate reductase*, "uncharacterized protein
(BATDEDRAFT_...)". None contains the ITS rDNA locus. Re-finding the anchor in each: 53
of 55 are the reverse primer at **five or six mismatches of 22**, median site E-value
5.1e-3.

The mechanism: `score.classify_exclusion` calls a lone primer site credible when its
**per-record** E-value is under `max_site_evalue: 0.01`. A 22-mer with six mismatches
has E around 0.005 in a 900 bp record. The Bd archive is 9,496 records, 8,386 of
them JAM81 mRNAs, so dozens of chance anchors are expected — 55 is roughly what the
arithmetic gives. It is the same multiplicity error as the lineage rule, one level down:
a threshold set per test, applied across thousands of tests.

Had the switch been on, Bd's 2014 cohort would have read 15.4% detected on the strength
of protein-coding transcripts.

### `diverged` means different things for different assays

Sampling up to 150 `diverged` records from each of the twelve assays that hold 73% of
all 64,230, plus Bd, and re-finding the best anchor:

| assay | anchors at 0-2 mm | at 5-6 mm |
|---|---:|---:|
| `MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004` | 99% | 0% |
| `Leucocytozoon_cyt_c_Hellgren_2004` | 97% | 2% |
| `RETROVIRUS_RNA_polymerase_SIV_Keele_2009` | 90% | 0% |
| `Pan_coccidia_SSU_rDNA_negative_contro_Garner_2006` | 85% | 0% |
| `HANTAVIRUS_ssRNA_S_segment_2` | 49% | 3% |
| `Pan_Plasmodium_sp_and_Haemopro_cytochrome_c` | 41% | 18% |
| `CIRCOVIRUSES_..._Mankertz_2000_round1` | 4% | 31% |
| `POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1` | 1% | 19% |
| `ENTEROVIRUS_ssRNA_VP3_VP1_round2` | 0% | 26% |
| `CIRCOVIRUSES_..._round2` | 2% | 48% |
| `POLYOMAVIRUS_dsDNA_VP1` | 1% | **92%** |
| `CHYTRID_Bd_..._Boyle_2004` | 3% | **94%** |

For some assays the label is real partner-site divergence; for others it is mostly
chance. No single setting of a global switch can be right for both.

### A fix I tried and reverted

The obvious repair is to require the anchor to be a site the assay could prime from —
`classify(score_primer(site)) != "fail"`, reusing `reduced_max` and
`terminal_mismatch_fails`, no new number. Tested on sampled records it relabelled the
right things: Bd 54 of 63 to `no_site`, Orthoreovirus 98%, Polyomavirus VP1 72%, while
Monkeypox, Phlebovirus, Alphavirus and Leucocytozoon kept 91-100%.

But **SIV Keele lost 99%**, despite 90% of its anchors sitting at 0-2 mismatches. Its
anchors are the forward primer at two mismatches, one 3'-proximal: penalty 3.5, a
`fail`. A 2-mismatch 20-mer in a 9 kb genome is not chance — these are real SIV records
on which the assay genuinely fails, exactly what `diverged` exists to catch. The rule
used "could the assay prime here?" as a proxy for "is the locus here?", and the two come
apart precisely when the assay fails on its real target. Reverted; nothing shipped.

**The right axis is the anchor's chance of arising across the whole archive**, not per
record: an archive-scale E-value (the per-record E times the number of records the query
returned, or an FDR over them). That needs a threshold and the archive size plumbed into
the screen, and it changes the screen signature, so it needs a rescreen and a tier-2
re-run. It goes to wave 3 as a new item. Until then the switch stays off.

## 2.2 Two definitions of failure: kept apart, now visible

`nested.py` counts `diverged` as a round-1 failure; the drift denominator does not.
Measured on the frozen table, switching the nested table to the drift definition moves
**11 of 26 families** by 2 points or more, in a direction that is wrong for some of
them:

| family | round 1, counted -> not | nest, counted -> not | round-1 anchors at 0-2 mm |
|---|---|---|---:|
| `BOCAVIRUS_ssDNA_NS1_gene` | 68.3% -> 99.5% | 68.3% -> 99.5% | 26% |
| `PHLEBOVIRUS_ssRNA_L_segment` | 82.1% -> 94.0% | 75.2% -> 86.5% | 97% |
| `CIRCOVIRUSES_..._Mankertz_` | 68.2% -> 90.7% | 31.0% -> 41.2% | 4% |
| `ALPHAVIRUSES_..._NSP4_gene` | 97.1% -> 99.8% | 94.1% -> 98.5% | 96% |
| `ORTHOREOVIRUS_..._Landolfi_2010` | 32.9% -> 37.7% | 25.8% -> 29.6% | 10% (60% at 5-6) |

Phlebovirus and Alphavirus are counted correctly today — dropping `diverged` would
overstate their nests. Orthoreovirus is chance-dominated. So `nested.py` keeps counting
it, because that is right where the label is right, and the two definitions stay
different on purpose: tier-2 rejected `diverged` in the drift denominator, and nothing
has tested it in the nested one.

What changed is that the reader can now see it. `NestedFamily.outer_diverged` counts
round-1 failures that rest only on the label, and the nested table has a column for it
in both reports. On the frozen table: Lyssavirus's round-1 loss rests on 30 of 9,081;
Circovirus Mankertz's on 1,276 of 2,419; Polyomavirus PREDICT VP1's on 1,004 of 3,029.
Where most of a loss rests on it, the section prose says to read it as an upper bound.

## 2.3 `exclude_patent_records`: on, without tier-2 approval, deliberately

Tier-2 is unchanged row for row with it on. In the report, **5 statuses move, in both
directions**, and **92 assays lose patent records**:

| assay | status | detected (recent) |
|---|---|---|
| `PARVOVIRUS_ssDNA_VP1_gene_dependovirus` | declining -> low coverage | 80.1% -> 43.8% |
| `PARVOVIRUS_ssDNA_VP1_gene_pan_parvo` | declining -> low coverage | 92.4% -> 76.2% |
| `ARENAVIRUS_ssRNA_S_gene_2` | declining -> low coverage | 43.5% -> 31.2% |
| `ARENAVIRUS_ssRNA_S_gene` | low coverage -> declining | 52.9% -> 32.3% |
| `CMV_UL55_gB_Deckers_2009` | watch -> stable | 89.7% -> 96.4% |

The dependovirus rows are the clearest case: 6,845 patent records, overwhelmingly
engineered AAV capsid libraries that the assay detects, were holding its share at 80%.

It was held off for a week because "no validation case names an affected assay", while
the orthopox ATI flag it fixes had been checked by hand and called a false positive. A
49-case set with ~7 independent failure events cannot adjudicate most denominator
questions. The rule now, recorded beside the setting in `config.yaml`: **where the
mechanism argument is sound and tier-2 is silent, ship with the evidence recorded; where
tier-2 contradicts, do not.** `count_diverged_as_fail` is the second case,
`exclude_patent_records` the first.

Turning it on exposed a latent crash: `sitedrift.py` called `assess()` without the
patent set, which `assess` refuses when the option is on. Fixed, and
`tests/test_drift.py::test_every_caller_of_assess_passes_the_patent_set` now checks
every call site in `assaywatch/` and `scripts/` by AST; it flags `sitedrift.py:578` on
the old code.

Live-config statuses: **35 declining, 39 low coverage, 12 watch, 32 insufficient data,
14 no recent data, 53 stable, 19 not scoreable.**

## 2.4 / 2.5 Precision, published

`scripts/retrospective.py` now prints, after the cell counts, the numbers a reader of a
flag needs, each with a Wilson interval:

```
precision:
  declining calls that were documented failures (PPV): 2/9 = 22% (95% CI 6%-55%)
  documented failures caught: 5/11 = 45% (95% CI 21%-72%)
    credited to: low coverage 3, declining 2
    caught by the drift flag itself (declining): 2/11 = 18% (95% CI 5%-48%)
  failure cases by mechanism: coverage 10, drift 1
  working assays called declining (false alarms): 5/32 = 16% (95% CI 7%-32%)
```

`config.yaml`'s header and README now carry the same, labelled in-sample. The header
used to say validation showed the thresholds "far too conservative". The false-alarm
rate says otherwise: the tool is wrong in both directions.

## Where wave 2 leaves the science

PPV is still 2/9. Neither diagnosed switch moved it, and for a reason the earlier docs
did not have: the three documented misses are not denominator problems in the recent
window. Bd's is invisible because its failing records are old, mislabelled, or both; the
genuine Asian ITS haplotypes Mutnale 2018 describes have not been located in the archive
at all yet. That is the next lead, alongside the Usutu scoring-versus-bench
disagreement.

## New items

- ~~**Wave 3, before any re-test of `count_diverged_as_fail`:** an archive-scale anchor
  test in `classify_exclusion`; rescreen; tier-2 re-run.~~ **DONE 2026-10-24**,
  `docs/2026-10-24-archive-anchor.md`: BH over each assay's `no_amplicon` rows rather
  than E x record count (the product cannot tell SIV Keele's real anchors from Bd's
  chance ones), shipping off as `drift.anchor_fdr`. Bd loses 50 of 63 `diverged`, SIV
  Keele and Monkeypox lose none. Tier-2 is silent on it alone; paired with
  `count_diverged_as_fail` at q = 0.01 it removes both false alarms that switch caused.
- **Find Mutnale 2018's haplotypes in the Bd archive** and see what call they get. If
  they are `no_site` (both primers past six mismatches) or `truncated`, the miss is a
  retrieval or search-budget problem, not a denominator one.
- **`site-drift.md` and `report.md` disagree about which assays are failing.**
  `sitedrift.py` says statuses "come from the same assessment the main report uses, so
  the two documents cannot disagree", but it calls `assess()` without taxids, scope,
  resolvers or taxonomy, so it runs no lineage check and no scope filter, and it ignores
  the not-scoreable quarantine. On the live config it covers 87 assays against the
  report's 74 flagged: 17 the report does not flag (some of them Not scoreable) and 4 it
  does that site-drift omits (lineage overrides). Fixed in the next commit: both
  now go through `report.assess_as_reported`, and site-drift covers exactly the
  report's Declining + Low Coverage + Watch set (74 + 12 = 86).
