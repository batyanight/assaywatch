# Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens

<p class="aw-byline">Rossi · Microorganisms · 2024</p>

<p class="aw-doi"><a href="https://doi.org/10.3390/microorganisms12061105">doi:10.3390/microorganisms12061105</a></p>

??? quote "Full citation"
    Rossi, F.; Del Matto, I.; Ricchiuti, L.; Marino, L. Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens. Microorganisms 2024, 12, 1105.

<p class="aw-assay-line"><span class="aw-chip aw-chip-declining">declining</span> <span class="aw-id">DWVB_polyprotein_Rossi_2024</span></p>

**DEFORMED WING VIRUS B — polyprotein gene RT-qPCR, MGB probe (Rossi 2024)**

| | |
|---|---|
| Target | Deformed wing virus B ([taxid 2498590](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2498590)) |
| Gene | polyprotein gene |
| Chemistry | mgb |
| Amplicon | 138 bp |
| Registry status | active |

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `TTTATCTTCATTAAAACCGCCA` | 22 nt |
| reverse | `CTCATTAACTGAGTTGTTGTC` | 21 nt |
| probe | `ATCTTTTGAGAGGGATGAGA` | 20 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 12 | 16 | 75.0% | 50.5% – 89.8% |
| baseline (everything earlier) | 41 | 41 | 100.0% | 91.4% – 100.0% |

Change from baseline, Newcombe interval: **-49.5% to -7.9%**. Threshold: **90.0%**.

*detected share 75.0% (51%-90%) since Oct 2024, upper bound below the 90% threshold; change from baseline -49% to -8%*

Trend across deposit years: by record falling (p=8.25e-05, 3 years); by footprint falling (p=0.0232). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the threshold. Marker size is the number of records behind each point, because 100%
of three records and 100% of three thousand are not the same claim.

<svg class="aw-chart" viewBox="0 0 720 230" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, 2023 to 2026, against a 90 percent threshold."><rect class="aw-window" x="485.3" y="12.0" width="220.7" height="180.0"><title>the recent window: 24 months from Oct 2024</title></rect><line class="aw-grid" x1="44.0" y1="192.0" x2="706.0" y2="192.0"/><text class="aw-tick aw-tick-y" x="37.0" y="195.5">0</text><line class="aw-grid" x1="44.0" y1="147.0" x2="706.0" y2="147.0"/><text class="aw-tick aw-tick-y" x="37.0" y="150.5">25</text><line class="aw-grid" x1="44.0" y1="102.0" x2="706.0" y2="102.0"/><text class="aw-tick aw-tick-y" x="37.0" y="105.5">50</text><line class="aw-grid" x1="44.0" y1="57.0" x2="706.0" y2="57.0"/><text class="aw-tick aw-tick-y" x="37.0" y="60.5">75</text><line class="aw-grid" x1="44.0" y1="12.0" x2="706.0" y2="12.0"/><text class="aw-tick aw-tick-y" x="37.0" y="15.5">100</text><line class="aw-threshold" x1="44.0" y1="30.0" x2="706.0" y2="30.0"/><text class="aw-threshold-label" x="706.0" y="25.0">90% threshold</text><polyline class="aw-line aw-declining" points="44.0,12.0 485.3,30.0 706.0,102.0"/><g class="aw-point aw-declining"><title>2023: 41 of 41 detected (100.0%)</title><circle cx="44.0" cy="12.0" r="4.2"/></g><g class="aw-point aw-declining"><title>2025: 9 of 10 detected (90.0%) — recent window</title><circle cx="485.3" cy="30.0" r="3.3"/></g><g class="aw-point aw-declining"><title>2026: 3 of 6 detected (50.0%) — recent window</title><circle cx="706.0" cy="102.0" r="3.0"/></g><text class="aw-tick" x="44.0" y="208">2023</text><text class="aw-tick" x="264.7" y="208">2024</text><text class="aw-tick" x="485.3" y="208">2025</text><text class="aw-tick" x="706.0" y="208">2026</text><text class="aw-axis-label" x="375" y="224">deposit year · marker size is the number of records</text></svg>

## Where the mismatches sit

Each oligo drawn base by base, 5′ to 3′, with the 3′ window shaded — a mismatch
there is the one that fails a reaction. Bar height is the share of records differing
at that position; bar colour is what that costs, measured as the fall in detection
between records that differ there and records that do not:

<span class="aw-key"><span class="aw-key-swatch aw-bar-strong"></span> detection falls 25 points or more</span>
<span class="aw-key"><span class="aw-key-swatch aw-bar-mid"></span> falls 10 to 25</span>
<span class="aw-key"><span class="aw-key-swatch aw-bar-weak"></span> little or no cost — variation the assay tolerates</span>

Hover any bar for the counts. A tall grey bar is a polymorphism; a short red one is a
design problem.

<svg class="aw-track" viewBox="0 0 426 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="68" y="56">forward</text><rect class="aw-zone" x="333.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="44.0" x2="408.0" y2="44.0"/><text class="aw-base" x="85.5" y="57">T</text><text class="aw-base" x="100.5" y="57">T</text><text class="aw-base" x="115.5" y="57">T</text><text class="aw-base" x="130.5" y="57">A</text><text class="aw-base" x="145.5" y="57">T</text><text class="aw-base" x="160.5" y="57">C</text><text class="aw-base" x="175.5" y="57">T</text><text class="aw-base" x="190.5" y="57">T</text><text class="aw-base" x="205.5" y="57">C</text><text class="aw-base" x="220.5" y="57">A</text><text class="aw-base" x="235.5" y="57">T</text><text class="aw-base" x="250.5" y="57">T</text><text class="aw-base" x="265.5" y="57">A</text><text class="aw-base" x="280.5" y="57">A</text><text class="aw-base" x="295.5" y="57">A</text><text class="aw-base" x="310.5" y="57">A</text><text class="aw-base" x="325.5" y="57">C</text><text class="aw-base" x="340.5" y="57">C</text><text class="aw-base" x="355.5" y="57">G</text><text class="aw-base" x="370.5" y="57">C</text><text class="aw-base" x="385.5" y="57">C</text><text class="aw-base" x="400.5" y="57">A</text><text class="aw-tick" x="400.5" y="71">1</text><text class="aw-tick" x="340.5" y="71">5</text><text class="aw-tick" x="265.5" y="71">10</text><text class="aw-tick" x="190.5" y="71">15</text><text class="aw-tick" x="115.5" y="71">20</text><text class="aw-tick" x="85.5" y="71">22</text><text class="aw-end" x="74" y="57">5′</text><text class="aw-end aw-end-3" x="412" y="57">3′</text><text class="aw-track-label" x="68" y="138">reverse</text><rect class="aw-zone" x="318.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="126.0" x2="393.0" y2="126.0"/><text class="aw-base" x="85.5" y="139">C</text><text class="aw-base" x="100.5" y="139">T</text><text class="aw-base" x="115.5" y="139">C</text><text class="aw-base" x="130.5" y="139">A</text><text class="aw-base" x="145.5" y="139">T</text><text class="aw-base" x="160.5" y="139">T</text><text class="aw-base" x="175.5" y="139">A</text><text class="aw-base" x="190.5" y="139">A</text><text class="aw-base" x="205.5" y="139">C</text><text class="aw-base" x="220.5" y="139">T</text><text class="aw-base" x="235.5" y="139">G</text><text class="aw-base" x="250.5" y="139">A</text><text class="aw-base" x="265.5" y="139">G</text><text class="aw-base" x="280.5" y="139">T</text><text class="aw-base" x="295.5" y="139">T</text><text class="aw-base" x="310.5" y="139">G</text><text class="aw-base" x="325.5" y="139">T</text><text class="aw-base" x="340.5" y="139">T</text><text class="aw-base" x="355.5" y="139">G</text><text class="aw-base" x="370.5" y="139">T</text><text class="aw-base" x="385.5" y="139">C</text><text class="aw-tick" x="385.5" y="153">1</text><text class="aw-tick" x="325.5" y="153">5</text><text class="aw-tick" x="250.5" y="153">10</text><text class="aw-tick" x="175.5" y="153">15</text><text class="aw-tick" x="100.5" y="153">20</text><text class="aw-tick" x="85.5" y="153">21</text><text class="aw-end" x="74" y="139">5′</text><text class="aw-end aw-end-3" x="397" y="139">3′</text><text class="aw-track-label" x="68" y="220">probe</text><rect class="aw-zone" x="303.0" y="174.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="208.0" x2="378.0" y2="208.0"/><text class="aw-base" x="85.5" y="221">A</text><text class="aw-base" x="100.5" y="221">T</text><text class="aw-base" x="115.5" y="221">C</text><text class="aw-base" x="130.5" y="221">T</text><text class="aw-base" x="145.5" y="221">T</text><text class="aw-base" x="160.5" y="221">T</text><text class="aw-base" x="175.5" y="221">T</text><text class="aw-base" x="190.5" y="221">G</text><text class="aw-base" x="205.5" y="221">A</text><text class="aw-base" x="220.5" y="221">G</text><text class="aw-base" x="235.5" y="221">A</text><text class="aw-base" x="250.5" y="221">G</text><text class="aw-base" x="265.5" y="221">G</text><text class="aw-base" x="280.5" y="221">G</text><text class="aw-base" x="295.5" y="221">A</text><text class="aw-base" x="310.5" y="221">T</text><text class="aw-base" x="325.5" y="221">G</text><text class="aw-base" x="340.5" y="221">A</text><text class="aw-base" x="355.5" y="221">G</text><text class="aw-base" x="370.5" y="221">A</text><text class="aw-tick" x="370.5" y="235">1</text><text class="aw-tick" x="310.5" y="235">5</text><text class="aw-tick" x="235.5" y="235">10</text><text class="aw-tick" x="160.5" y="235">15</text><text class="aw-tick" x="85.5" y="235">20</text><text class="aw-end" x="74" y="221">5′</text><text class="aw-end aw-end-3" x="382" y="221">3′</text></svg>

## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).

Disclosures on this entry: `oligos_from_secondary_source`, `scope_narrower_than_taxid`.


## What reached the statistics

737 records were screened for this assay and **57 (8%)** were evaluable, meaning both primers landed in the right orientation and size range. 680 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 670 |
| `truncated` | 9 |

