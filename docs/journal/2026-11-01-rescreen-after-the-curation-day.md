# 2026-11-01 — the rescreen after a day of curation, and what moved

**Finding: one status changed, and it is the one that was predicted.** A full run after
four oligos were removed, two scopes widened, one duplicate deleted and three entries
added. 49m 32s, 625 of 625 steps, exit 0. 202 assays screened against 198 on
2026-10-31; `report_diff results/2026-10-31 results/2026-11-01` reports a single status
change, one entry gone and five new.

| | 2026-10-31 | 2026-11-01 |
|---|---|---|
| stable | 72 | 75 |
| declining | 42 | 42 |
| low coverage | 31 | 32 |
| insufficient data | 30 | 30 |
| no recent data | 18 | 18 |
| watch | 5 | 5 |

## The predicted change, confirmed on real calls

`Haemosporida_cytb_Hellgren_2004_HaemF` **declining -> low coverage**, which is
what adding taxid 31272 to its scope was expected to do and what re-extracting the old
calls had already shown: with 816 records of its own genus back in the denominator the
share is 27.1% of 314 rather than 10.3% of 155, and that is no longer a fall from a
working baseline. Nothing else moved, which is the reassuring part after a day of
registry edits: the removals and the scope change did not quietly reshuffle the report.

## Removing an unpublished primer cost detection and bought more back

`Dependoparvovirus_VP1_Gao_2002_2`, whose two oligos were degenerate
widenings no publication prints until they were replaced by the cited paper's forms:

| | before | after |
|---|---|---|
| detected (recent) | 99.6% of 256 | **91.8% of 256** |
| degeneracy | **6912x severe** | **1x negligible** |
| status | stable | stable |

The 7.8-point fall is the honest cost of a narrower primer and was expected. The
degeneracy collapse was not part of the argument for the change and is the larger
result: the widened pair carried a 6,912-fold degenerate pool, which `config.yaml`
penalises as chance-amplification risk, and the published pair is exact. On both axes
the published sequences make the better entry, so this is not a trade.

## The enterovirus pair splits, and the split is the point

Both entries entered today citing Wray et al. 2016, screened for the first time, sharing
one retrieval group and one window:

| entry | oligos | detected (recent) | section |
|---|---|---|---|
| `..._round1` | `EVRV1` + `EVRV2` | **98.6% of 1,195** | Stable |
| `..._round2` | `EVRV3` + `EVRV2anew` | **52.5% of 1,203** | **Start here** |

Round 1 is Coiras et al. 2004's outer pair with two degenerate positions narrowed by
Wray. Round 2 is Wray's own re-pairing: his `EVRV3` (a narrowed form of Coiras's inner
forward) with `EVRV2anew`, a 19 nt truncation of the OUTER reverse, in place of
Coiras's inner reverse — a pairing Coiras never published, which is why its 660 bp
product is nowhere near his 226 bp nested one.

The like-for-like comparison is the finding: the same records, the same window, 98.6%
against 52.5%. It reads as the cost of a lab-specific variant rather than as drift, and
nothing here distinguishes the two yet. **The experiment that would: enter Coiras's
printed forms as their own entries and screen all four together.** Until that is done,
`round2`'s place in "Start here" should be read as a question about the variant, not as
a verdict on the published assay.

## The rest

- `Orthohantavirus_S_Mangombi_2021_round2`, also new today: **96.5% of 402**, stable.
- `Bornaviridae_N_Zimmermann_1994_round2` published **no verdict**, listed as
  withheld under `oligo_sequence_uncertain`. That is the mechanism working: the printed
  primer matches no known record, and until the 1994 scan is re-read the report declines
  to assert a drift finding it cannot support.
- `Chordopoxvirinae_IMV_Li_2010` and `..._highGC_RNApol_Li_2010` appear in a report
  for the FIRST time, both stable (97.9% and the high-GC sibling). Not a change in the
  assays: their `retrieval_stale` flag was cleared on 2026-10-31 *after* that run was
  generated, so this is the first run able to score them.
- `BORNA_VIRUS_N_gene` is gone from the report, having been merged into its sibling.

## The site

`website/data/run.json` is re-extracted from this run (219 assays, 17 withheld) and the
pages regenerated. Three things reach the site here for the first time: the 16 pages
that replace an empty year chart with a sentence, the 18 rows that say `no recent data`
where they used to say `0`, and the three new entries.

One warning during extraction — `1 taxids not in the taxonomy cache` — is taxid 31272,
added to the haemosporidian scopes today; the cache was rebuilt after the run.
