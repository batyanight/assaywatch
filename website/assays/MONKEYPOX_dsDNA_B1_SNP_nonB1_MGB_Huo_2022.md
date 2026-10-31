# Development of two multiplex real-time PCR assays for simultaneous detection and differentiation of monkeypox virus IIa, IIb, and I clades and the B.1 lineage

<p class="aw-byline">Huo · Biosafety and Health · 2022</p>

<p class="aw-doi"><a href="https://doi.org/10.1016/j.bsheal.2022.10.005">doi:10.1016/j.bsheal.2022.10.005</a></p>

??? quote "Full citation"
    Huo S, Chen Y, Lu R, Zhang Z, Zhang G, Zhao L, Deng Y, Wu C, Tan W. 2022. Development of two multiplex real-time PCR assays for simultaneous detection and differentiation of monkeypox virus IIa, IIb, and I clades and the B.1 lineage. Biosaf Health 4:392-398

<p class="aw-assay-line"><span class="aw-chip aw-chip-low-coverage">low coverage</span> <span class="aw-id">MONKEYPOX_dsDNA_B1_SNP_nonB1_MGB_Huo_2022</span></p>

**MONKEYPOX virus (dsDNA) — Panel 2 non-B.1 clades MGB probe (Huo 2022)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | SNP-typing locus at 183524-183539 of ON563414.2 |
| Chemistry | mgb |
| Amplicon | 81 bp |
| Registry status | draft |

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGTACACAGACCTCCACCAC` | 20 nt |
| reverse | `AGTAATTGACCTACTGGTCTAGGG` | 24 nt |
| probe | `AGTCCAAAATCCGCCA` | 16 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 437 | 4,838 | 9.0% | 8.3% – 9.9% |
| baseline (everything earlier) | 253 | 8,368 | 3.0% | 2.7% – 3.4% |

Change from baseline, Newcombe interval: **5.1% to 6.9%**. Threshold: **90.0%**.

*detected share 9.0% (8%-10%) since Oct 2024, upper bound below the 90% threshold; change from baseline +5% to +7% (rose from a baseline of 3%); separately, lineage Orthopoxvirus monkeypox (3431483) (4793 records) detects only 9.1% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record rising (p=0.000112, 16 years); by footprint falling (p=0.292); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../limitations.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the threshold. Marker size is the number of records behind each point, because 100%
of three records and 100% of three thousand are not the same claim.

<svg class="aw-chart" viewBox="0 0 720 230" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, 2001 to 2026, against a 90 percent threshold."><rect class="aw-window" x="653.0" y="12.0" width="53.0" height="180.0"><title>the recent window: 24 months from Oct 2024</title></rect><line class="aw-grid" x1="44.0" y1="192.0" x2="706.0" y2="192.0"/><text class="aw-tick aw-tick-y" x="37.0" y="195.5">0</text><line class="aw-grid" x1="44.0" y1="147.0" x2="706.0" y2="147.0"/><text class="aw-tick aw-tick-y" x="37.0" y="150.5">25</text><line class="aw-grid" x1="44.0" y1="102.0" x2="706.0" y2="102.0"/><text class="aw-tick aw-tick-y" x="37.0" y="105.5">50</text><line class="aw-grid" x1="44.0" y1="57.0" x2="706.0" y2="57.0"/><text class="aw-tick aw-tick-y" x="37.0" y="60.5">75</text><line class="aw-grid" x1="44.0" y1="12.0" x2="706.0" y2="12.0"/><text class="aw-tick aw-tick-y" x="37.0" y="15.5">100</text><line class="aw-threshold" x1="44.0" y1="30.0" x2="706.0" y2="30.0"/><text class="aw-threshold-label" x="706.0" y="25.0">90% threshold</text><polyline class="aw-line aw-low-coverage" points="44.0,192.0 123.4,102.0 149.9,63.4 282.3,192.0 308.8,192.0 361.8,192.0 388.2,184.5 414.7,110.2 494.2,12.0 520.6,12.0 547.1,60.6 600.1,188.3 626.6,191.5 653.0,180.7 679.5,153.4 706.0,190.0"/><g class="aw-point aw-low-coverage"><title>2001: 0 of 2 detected (0.0%)</title><circle cx="44.0" cy="192.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>2004: 1 of 2 detected (50.0%)</title><circle cx="123.4" cy="102.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>2005: 5 of 7 detected (71.4%)</title><circle cx="149.9" cy="63.4" r="3.0"/></g><g class="aw-point aw-low-coverage"><title>2010: 0 of 5 detected (0.0%)</title><circle cx="282.3" cy="192.0" r="2.8"/></g><g class="aw-point aw-low-coverage"><title>2011: 0 of 2 detected (0.0%)</title><circle cx="308.8" cy="192.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>2013: 0 of 1 detected (0.0%)</title><circle cx="361.8" cy="192.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>2014: 1 of 24 detected (4.2%)</title><circle cx="388.2" cy="184.5" r="3.8"/></g><g class="aw-point aw-low-coverage"><title>2015: 5 of 11 detected (45.5%)</title><circle cx="414.7" cy="110.2" r="3.3"/></g><g class="aw-point aw-low-coverage"><title>2018: 1 of 1 detected (100.0%)</title><circle cx="494.2" cy="12.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>2019: 8 of 8 detected (100.0%)</title><circle cx="520.6" cy="12.0" r="3.1"/></g><g class="aw-point aw-low-coverage"><title>2020: 27 of 37 detected (73.0%)</title><circle cx="547.1" cy="60.6" r="4.1"/></g><g class="aw-point aw-low-coverage"><title>2022: 69 of 3,332 detected (2.1%)</title><circle cx="600.1" cy="188.3" r="7.0"/></g><g class="aw-point aw-low-coverage"><title>2023: 8 of 3,101 detected (0.3%)</title><circle cx="626.6" cy="191.5" r="7.0"/></g><g class="aw-point aw-low-coverage"><title>2024: 128 of 2,046 detected (6.3%) — recent window</title><circle cx="653.0" cy="180.7" r="6.9"/></g><g class="aw-point aw-low-coverage"><title>2025: 406 of 1,892 detected (21.5%) — recent window</title><circle cx="679.5" cy="153.4" r="6.8"/></g><g class="aw-point aw-low-coverage"><title>2026: 31 of 2,735 detected (1.1%) — recent window</title><circle cx="706.0" cy="190.0" r="7.0"/></g><text class="aw-tick" x="44.0" y="208">2001</text><text class="aw-tick" x="149.9" y="208">2005</text><text class="aw-tick" x="255.8" y="208">2009</text><text class="aw-tick" x="361.8" y="208">2013</text><text class="aw-tick" x="467.7" y="208">2017</text><text class="aw-tick" x="573.6" y="208">2021</text><text class="aw-tick" x="679.5" y="208">2025</text><text class="aw-axis-label" x="375" y="224">deposit year · marker size is the number of records</text></svg>

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

<svg class="aw-track" viewBox="0 0 456 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="68" y="56">forward</text><rect class="aw-zone" x="303.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="44.0" x2="378.0" y2="44.0"/><text class="aw-base" x="85.5" y="57">A</text><text class="aw-base" x="100.5" y="57">G</text><text class="aw-base" x="115.5" y="57">T</text><text class="aw-base" x="130.5" y="57">A</text><text class="aw-base" x="145.5" y="57">C</text><text class="aw-base" x="160.5" y="57">A</text><text class="aw-base" x="175.5" y="57">C</text><text class="aw-base" x="190.5" y="57">A</text><text class="aw-base" x="205.5" y="57">G</text><text class="aw-base" x="220.5" y="57">A</text><text class="aw-base" x="235.5" y="57">C</text><text class="aw-base" x="250.5" y="57">C</text><text class="aw-base" x="265.5" y="57">T</text><text class="aw-base" x="280.5" y="57">C</text><text class="aw-base" x="295.5" y="57">C</text><g class="aw-bar-weak"><title>forward position 5 from the 3&#x27; end, base A
3,242 of 13,131 records differ here (24.7%)
detected when it differs: 0% of 3,242
detected when it does not: 7% of 9,889
substitutions: A&gt;G in 3,242</title><rect x="304.0" y="27.1" width="13.0" height="16.9"/></g><text class="aw-base" x="310.5" y="57">A</text><text class="aw-base" x="325.5" y="57">C</text><text class="aw-base" x="340.5" y="57">C</text><text class="aw-base" x="355.5" y="57">A</text><text class="aw-base" x="370.5" y="57">C</text><text class="aw-tick" x="370.5" y="71">1</text><text class="aw-tick" x="310.5" y="71">5</text><text class="aw-tick" x="235.5" y="71">10</text><text class="aw-tick" x="160.5" y="71">15</text><text class="aw-tick" x="85.5" y="71">20</text><text class="aw-end" x="74" y="57">5′</text><text class="aw-end aw-end-3" x="382" y="57">3′</text><text class="aw-track-label" x="68" y="138">reverse</text><rect class="aw-zone" x="363.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="126.0" x2="438.0" y2="126.0"/><g class="aw-bar-weak"><title>reverse position 24 from the 3&#x27; end, base A
3,242 of 13,131 records differ here (24.7%)
detected when it differs: 0% of 3,242
detected when it does not: 7% of 9,889
substitutions: A&gt;G in 3,241, A&gt;T in 1</title><rect x="79.0" y="109.1" width="13.0" height="16.9"/></g><text class="aw-base" x="85.5" y="139">A</text><text class="aw-base" x="100.5" y="139">G</text><text class="aw-base" x="115.5" y="139">T</text><text class="aw-base" x="130.5" y="139">A</text><text class="aw-base" x="145.5" y="139">A</text><text class="aw-base" x="160.5" y="139">T</text><text class="aw-base" x="175.5" y="139">T</text><text class="aw-base" x="190.5" y="139">G</text><text class="aw-base" x="205.5" y="139">A</text><text class="aw-base" x="220.5" y="139">C</text><text class="aw-base" x="235.5" y="139">C</text><text class="aw-base" x="250.5" y="139">T</text><text class="aw-base" x="265.5" y="139">A</text><text class="aw-base" x="280.5" y="139">C</text><text class="aw-base" x="295.5" y="139">T</text><text class="aw-base" x="310.5" y="139">G</text><text class="aw-base" x="325.5" y="139">G</text><text class="aw-base" x="340.5" y="139">T</text><text class="aw-base" x="355.5" y="139">C</text><text class="aw-base" x="370.5" y="139">T</text><text class="aw-base" x="385.5" y="139">A</text><text class="aw-base" x="400.5" y="139">G</text><text class="aw-base" x="415.5" y="139">G</text><text class="aw-base" x="430.5" y="139">G</text><text class="aw-tick" x="430.5" y="153">1</text><text class="aw-tick" x="370.5" y="153">5</text><text class="aw-tick" x="295.5" y="153">10</text><text class="aw-tick" x="220.5" y="153">15</text><text class="aw-tick" x="145.5" y="153">20</text><text class="aw-tick" x="85.5" y="153">24</text><text class="aw-end" x="74" y="139">5′</text><text class="aw-end aw-end-3" x="442" y="139">3′</text><text class="aw-track-label" x="68" y="220">probe</text><rect class="aw-zone" x="243.0" y="174.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="208.0" x2="318.0" y2="208.0"/><text class="aw-base" x="85.5" y="221">A</text><text class="aw-base" x="100.5" y="221">G</text><text class="aw-base" x="115.5" y="221">T</text><text class="aw-base" x="130.5" y="221">C</text><text class="aw-base" x="145.5" y="221">C</text><text class="aw-base" x="160.5" y="221">A</text><text class="aw-base" x="175.5" y="221">A</text><text class="aw-base" x="190.5" y="221">A</text><text class="aw-base" x="205.5" y="221">A</text><text class="aw-base" x="220.5" y="221">T</text><g class="aw-bar-mid"><title>probe position 6 from the 3&#x27; end, base C
9,197 of 13,131 records differ here (70.0%)
detected when it differs: 0% of 9,197
detected when it does not: 18% of 3,934
substitutions: C&gt;T in 9,197</title><rect x="229.0" y="179.5" width="13.0" height="28.5"/></g><text class="aw-base" x="235.5" y="221">C</text><text class="aw-base" x="250.5" y="221">C</text><text class="aw-base" x="265.5" y="221">G</text><text class="aw-base" x="280.5" y="221">C</text><text class="aw-base" x="295.5" y="221">C</text><text class="aw-base" x="310.5" y="221">A</text><text class="aw-tick" x="310.5" y="235">1</text><text class="aw-tick" x="250.5" y="235">5</text><text class="aw-tick" x="175.5" y="235">10</text><text class="aw-tick" x="100.5" y="235">15</text><text class="aw-tick" x="85.5" y="235">16</text><text class="aw-end" x="74" y="221">5′</text><text class="aw-end aw-end-3" x="322" y="221">3′</text></svg>

## By lineage

Every evaluable record is one lineage, **Orthopoxvirus monkeypox (3431483)** (437 of 4,793 detected, 9.1%, 95% interval 8.3–10.0%), so splitting by lineage adds nothing to the figure above. The split matters where an assay spans several clades: a pooled percentage can look healthy while one lineage fails completely.


## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).

Disclosures on this entry: `amplicon_measured_not_published`, `scope_narrower_than_taxid`.


## What reached the statistics

14,204 records were screened for this assay and **13,206 (93%)** were evaluable, meaning both primers landed in the right orientation and size range. 998 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../limitations.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 976 |
| `chance_anchor` | 5 |
| `no_pair` | 1 |

