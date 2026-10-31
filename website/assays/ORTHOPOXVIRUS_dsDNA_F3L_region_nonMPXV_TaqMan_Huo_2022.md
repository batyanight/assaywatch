# Development of two multiplex real-time PCR assays for simultaneous detection and differentiation of monkeypox virus IIa, IIb, and I clades and the B.1 lineage

<p class="aw-byline">Huo · Biosafety and Health · 2022</p>

<p class="aw-doi"><a href="https://doi.org/10.1016/j.bsheal.2022.10.005">doi:10.1016/j.bsheal.2022.10.005</a></p>

??? quote "Full citation"
    Huo S, Chen Y, Lu R, Zhang Z, Zhang G, Zhao L, Deng Y, Wu C, Tan W. 2022. Development of two multiplex real-time PCR assays for simultaneous detection and differentiation of monkeypox virus IIa, IIb, and I clades and the B.1 lineage. Biosaf Health 4:392-398

<p class="aw-assay-line"><span class="aw-chip aw-chip-low-coverage">low coverage</span> <span class="aw-id">ORTHOPOXVIRUS_dsDNA_F3L_region_nonMPXV_TaqMan_Huo_2022</span></p>

**ORTHOPOXVIRUS (dsDNA) — Panel 1 other-orthopoxvirus probe (Huo 2022)**

| | |
|---|---|
| Target | Orthopoxvirus ([taxid 10242](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10242)) |
| Gene | F3L region (positions 46313-46491 of ON563414.2) |
| Chemistry | hydrolysis_probe |
| Amplicon | 179 bp |
| Registry status | draft |

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATCCTCTCTCATTGATTTTTCGCGGGA` | 27 nt |
| reverse | `TGGAGAAGCGAGAAGTTAATAAAGC` | 25 nt |
| probe | `TCGTCGGAGCTGTACACCATAGCAC` | 25 nt |

## The verdict, and the numbers behind it

**low coverage** — below the threshold, but not measurably lower than before — an assay used beyond its design, or one that never covered this taxon

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 29 | 5,703 | 0.5% | 0.4% – 0.7% |
| baseline (everything earlier) | 392 | 8,967 | 4.4% | 4.0% – 4.8% |

Change from baseline, Newcombe interval: **-4.3% to -3.4%**. Threshold: **90.0%**.

*detected share 0.5% (0.4%-0.7%) since Oct 2024, upper bound below the 90% threshold; change from baseline -4% to -3% (fell less than the 5% that counts as declining, from a baseline of 4%); separately, lineage Orthopoxvirus monkeypox (3431483) (5175 records) detects only 0.0% and was below the threshold in every earlier year measured, so that lineage is a coverage gap rather than drift*

Trend across deposit years: by record falling (p=0, 32 years); by footprint falling (p=3.05e-08). Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the threshold. Marker size is the number of records behind each point, because 100%
of three records and 100% of three thousand are not the same claim.

<svg class="aw-chart" viewBox="0 0 720 230" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, 1991 to 2026, against a 90 percent threshold."><rect class="aw-window" x="668.2" y="12.0" width="37.8" height="180.0"><title>the recent window: 24 months from Oct 2024</title></rect><line class="aw-grid" x1="44.0" y1="192.0" x2="706.0" y2="192.0"/><text class="aw-tick aw-tick-y" x="37.0" y="195.5">0</text><line class="aw-grid" x1="44.0" y1="147.0" x2="706.0" y2="147.0"/><text class="aw-tick aw-tick-y" x="37.0" y="150.5">25</text><line class="aw-grid" x1="44.0" y1="102.0" x2="706.0" y2="102.0"/><text class="aw-tick aw-tick-y" x="37.0" y="105.5">50</text><line class="aw-grid" x1="44.0" y1="57.0" x2="706.0" y2="57.0"/><text class="aw-tick aw-tick-y" x="37.0" y="60.5">75</text><line class="aw-grid" x1="44.0" y1="12.0" x2="706.0" y2="12.0"/><text class="aw-tick aw-tick-y" x="37.0" y="15.5">100</text><line class="aw-threshold" x1="44.0" y1="30.0" x2="706.0" y2="30.0"/><text class="aw-threshold-label" x="706.0" y="25.0">90% threshold</text><polyline class="aw-line aw-low-coverage" points="44.0,12.0 81.8,12.0 100.7,12.0 157.5,12.0 176.4,12.0 195.3,12.0 214.2,12.0 233.1,102.0 252.1,12.0 271.0,12.0 289.9,57.0 308.8,117.0 327.7,12.0 346.6,12.0 365.5,12.0 403.4,192.0 422.3,39.7 441.2,23.2 460.1,22.9 479.0,77.5 497.9,128.5 516.9,102.0 535.8,21.0 554.7,54.9 573.6,61.1 592.5,138.7 611.4,12.0 630.3,191.2 649.3,191.1 668.2,189.0 687.1,191.5 706.0,190.7"/><g class="aw-point aw-low-coverage"><title>1991: 2 of 2 detected (100.0%)</title><circle cx="44.0" cy="12.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>1993: 4 of 4 detected (100.0%)</title><circle cx="81.8" cy="12.0" r="2.7"/></g><g class="aw-point aw-low-coverage"><title>1994: 1 of 1 detected (100.0%)</title><circle cx="100.7" cy="12.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>1997: 1 of 1 detected (100.0%)</title><circle cx="157.5" cy="12.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>1998: 1 of 1 detected (100.0%)</title><circle cx="176.4" cy="12.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>1999: 3 of 3 detected (100.0%)</title><circle cx="195.3" cy="12.0" r="2.6"/></g><g class="aw-point aw-low-coverage"><title>2000: 1 of 1 detected (100.0%)</title><circle cx="214.2" cy="12.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>2001: 2 of 4 detected (50.0%)</title><circle cx="233.1" cy="102.0" r="2.7"/></g><g class="aw-point aw-low-coverage"><title>2002: 5 of 5 detected (100.0%)</title><circle cx="252.1" cy="12.0" r="2.8"/></g><g class="aw-point aw-low-coverage"><title>2003: 2 of 2 detected (100.0%)</title><circle cx="271.0" cy="12.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>2004: 3 of 4 detected (75.0%)</title><circle cx="289.9" cy="57.0" r="2.7"/></g><g class="aw-point aw-low-coverage"><title>2005: 5 of 12 detected (41.7%)</title><circle cx="308.8" cy="117.0" r="3.4"/></g><g class="aw-point aw-low-coverage"><title>2006: 66 of 66 detected (100.0%)</title><circle cx="327.7" cy="12.0" r="4.5"/></g><g class="aw-point aw-low-coverage"><title>2007: 4 of 4 detected (100.0%)</title><circle cx="346.6" cy="12.0" r="2.7"/></g><g class="aw-point aw-low-coverage"><title>2008: 1 of 1 detected (100.0%)</title><circle cx="365.5" cy="12.0" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>2010: 0 of 3 detected (0.0%)</title><circle cx="403.4" cy="192.0" r="2.6"/></g><g class="aw-point aw-low-coverage"><title>2011: 11 of 13 detected (84.6%)</title><circle cx="422.3" cy="39.7" r="3.4"/></g><g class="aw-point aw-low-coverage"><title>2012: 15 of 16 detected (93.8%)</title><circle cx="441.2" cy="23.2" r="3.6"/></g><g class="aw-point aw-low-coverage"><title>2013: 31 of 33 detected (93.9%)</title><circle cx="460.1" cy="22.9" r="4.1"/></g><g class="aw-point aw-low-coverage"><title>2014: 42 of 66 detected (63.6%)</title><circle cx="479.0" cy="77.5" r="4.5"/></g><g class="aw-point aw-low-coverage"><title>2015: 6 of 17 detected (35.3%)</title><circle cx="497.9" cy="128.5" r="3.6"/></g><g class="aw-point aw-low-coverage"><title>2016: 2 of 4 detected (50.0%)</title><circle cx="516.9" cy="102.0" r="2.7"/></g><g class="aw-point aw-low-coverage"><title>2017: 38 of 40 detected (95.0%)</title><circle cx="535.8" cy="21.0" r="4.2"/></g><g class="aw-point aw-low-coverage"><title>2018: 16 of 21 detected (76.2%)</title><circle cx="554.7" cy="54.9" r="3.7"/></g><g class="aw-point aw-low-coverage"><title>2019: 24 of 33 detected (72.7%)</title><circle cx="573.6" cy="61.1" r="4.1"/></g><g class="aw-point aw-low-coverage"><title>2020: 16 of 54 detected (29.6%)</title><circle cx="592.5" cy="138.7" r="4.4"/></g><g class="aw-point aw-low-coverage"><title>2021: 24 of 24 detected (100.0%)</title><circle cx="611.4" cy="12.0" r="3.8"/></g><g class="aw-point aw-low-coverage"><title>2022: 15 of 3,461 detected (0.4%)</title><circle cx="630.3" cy="191.2" r="7.0"/></g><g class="aw-point aw-low-coverage"><title>2023: 15 of 3,147 detected (0.5%)</title><circle cx="649.3" cy="191.1" r="7.0"/></g><g class="aw-point aw-low-coverage"><title>2024: 36 of 2,135 detected (1.7%) — recent window</title><circle cx="668.2" cy="189.0" r="6.9"/></g><g class="aw-point aw-low-coverage"><title>2025: 6 of 2,215 detected (0.3%) — recent window</title><circle cx="687.1" cy="191.5" r="7.0"/></g><g class="aw-point aw-low-coverage"><title>2026: 23 of 3,277 detected (0.7%) — recent window</title><circle cx="706.0" cy="190.7" r="7.0"/></g><text class="aw-tick" x="44.0" y="208">1991</text><text class="aw-tick" x="138.6" y="208">1996</text><text class="aw-tick" x="233.1" y="208">2001</text><text class="aw-tick" x="327.7" y="208">2006</text><text class="aw-tick" x="422.3" y="208">2011</text><text class="aw-tick" x="516.9" y="208">2016</text><text class="aw-tick" x="611.4" y="208">2021</text><text class="aw-tick" x="706.0" y="208">2026</text><text class="aw-axis-label" x="375" y="224">deposit year · marker size is the number of records</text></svg>

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

<svg class="aw-track" viewBox="0 0 501 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="68" y="56">forward</text><rect class="aw-zone" x="408.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="44.0" x2="483.0" y2="44.0"/><text class="aw-base" x="85.5" y="57">A</text><text class="aw-base" x="100.5" y="57">T</text><text class="aw-base" x="115.5" y="57">C</text><text class="aw-base" x="130.5" y="57">C</text><text class="aw-base" x="145.5" y="57">T</text><text class="aw-base" x="160.5" y="57">C</text><text class="aw-base" x="175.5" y="57">T</text><text class="aw-base" x="190.5" y="57">C</text><text class="aw-base" x="205.5" y="57">T</text><text class="aw-base" x="220.5" y="57">C</text><text class="aw-base" x="235.5" y="57">A</text><text class="aw-base" x="250.5" y="57">T</text><text class="aw-base" x="265.5" y="57">T</text><text class="aw-base" x="280.5" y="57">G</text><text class="aw-base" x="295.5" y="57">A</text><text class="aw-base" x="310.5" y="57">T</text><text class="aw-base" x="325.5" y="57">T</text><text class="aw-base" x="340.5" y="57">T</text><text class="aw-base" x="355.5" y="57">T</text><text class="aw-base" x="370.5" y="57">T</text><text class="aw-base" x="385.5" y="57">C</text><text class="aw-base" x="400.5" y="57">G</text><text class="aw-base" x="415.5" y="57">C</text><text class="aw-base" x="430.5" y="57">G</text><text class="aw-base" x="445.5" y="57">G</text><text class="aw-base" x="460.5" y="57">G</text><text class="aw-base" x="475.5" y="57">A</text><text class="aw-tick" x="475.5" y="71">1</text><text class="aw-tick" x="415.5" y="71">5</text><text class="aw-tick" x="340.5" y="71">10</text><text class="aw-tick" x="265.5" y="71">15</text><text class="aw-tick" x="190.5" y="71">20</text><text class="aw-tick" x="115.5" y="71">25</text><text class="aw-tick" x="85.5" y="71">27</text><text class="aw-end" x="74" y="57">5′</text><text class="aw-end aw-end-3" x="487" y="57">3′</text><text class="aw-track-label" x="68" y="138">reverse</text><rect class="aw-zone" x="378.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="126.0" x2="453.0" y2="126.0"/><text class="aw-base" x="85.5" y="139">T</text><text class="aw-base" x="100.5" y="139">G</text><text class="aw-base" x="115.5" y="139">G</text><text class="aw-base" x="130.5" y="139">A</text><text class="aw-base" x="145.5" y="139">G</text><text class="aw-base" x="160.5" y="139">A</text><text class="aw-base" x="175.5" y="139">A</text><text class="aw-base" x="190.5" y="139">G</text><text class="aw-base" x="205.5" y="139">C</text><text class="aw-base" x="220.5" y="139">G</text><text class="aw-base" x="235.5" y="139">A</text><g class="aw-bar-weak"><title>reverse position 14 from the 3&#x27; end, base G
25 of 14,265 records differ here (0.2%)
detected when it differs: 96% of 25
detected when it does not: 4% of 14,240
substitutions: G&gt;A in 25</title><rect x="244.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="250.5" y="139">G</text><text class="aw-base" x="265.5" y="139">A</text><text class="aw-base" x="280.5" y="139">A</text><text class="aw-base" x="295.5" y="139">G</text><text class="aw-base" x="310.5" y="139">T</text><text class="aw-base" x="325.5" y="139">T</text><text class="aw-base" x="340.5" y="139">A</text><text class="aw-base" x="355.5" y="139">A</text><text class="aw-base" x="370.5" y="139">T</text><text class="aw-base" x="385.5" y="139">A</text><text class="aw-base" x="400.5" y="139">A</text><text class="aw-base" x="415.5" y="139">A</text><text class="aw-base" x="430.5" y="139">G</text><text class="aw-base" x="445.5" y="139">C</text><text class="aw-tick" x="445.5" y="153">1</text><text class="aw-tick" x="385.5" y="153">5</text><text class="aw-tick" x="310.5" y="153">10</text><text class="aw-tick" x="235.5" y="153">15</text><text class="aw-tick" x="160.5" y="153">20</text><text class="aw-tick" x="85.5" y="153">25</text><text class="aw-end" x="74" y="139">5′</text><text class="aw-end aw-end-3" x="457" y="139">3′</text><text class="aw-track-label" x="68" y="220">probe</text><rect class="aw-zone" x="378.0" y="174.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="208.0" x2="453.0" y2="208.0"/><text class="aw-base" x="85.5" y="221">T</text><text class="aw-base" x="100.5" y="221">C</text><text class="aw-base" x="115.5" y="221">G</text><text class="aw-base" x="130.5" y="221">T</text><g class="aw-bar-mid"><title>probe position 21 from the 3&#x27; end, base C
10,615 of 14,265 records differ here (74.4%)
detected when it differs: 0% of 10,615
detected when it does not: 16% of 3,650
substitutions: C&gt;T in 10,615</title><rect x="139.0" y="178.7" width="13.0" height="29.3"/></g><text class="aw-base" x="145.5" y="221">C</text><text class="aw-base" x="160.5" y="221">G</text><text class="aw-base" x="175.5" y="221">G</text><text class="aw-base" x="190.5" y="221">A</text><g class="aw-bar-weak"><title>probe position 17 from the 3&#x27; end, base G
3,071 of 14,265 records differ here (21.5%)
detected when it differs: 1% of 3,071
detected when it does not: 5% of 11,194
substitutions: G&gt;A in 3,056, G&gt;T in 15</title><rect x="199.0" y="192.2" width="13.0" height="15.8"/></g><text class="aw-base" x="205.5" y="221">G</text><text class="aw-base" x="220.5" y="221">C</text><text class="aw-base" x="235.5" y="221">T</text><text class="aw-base" x="250.5" y="221">G</text><text class="aw-base" x="265.5" y="221">T</text><text class="aw-base" x="280.5" y="221">A</text><g class="aw-bar-mid"><title>probe position 11 from the 3&#x27; end, base C
10,616 of 14,265 records differ here (74.4%)
detected when it differs: 0% of 10,616
detected when it does not: 16% of 3,649
substitutions: C&gt;A in 10,615, C&gt;T in 1</title><rect x="289.0" y="178.7" width="13.0" height="29.3"/></g><text class="aw-base" x="295.5" y="221">C</text><text class="aw-base" x="310.5" y="221">A</text><text class="aw-base" x="325.5" y="221">C</text><text class="aw-base" x="340.5" y="221">C</text><text class="aw-base" x="355.5" y="221">A</text><text class="aw-base" x="370.5" y="221">T</text><text class="aw-base" x="385.5" y="221">A</text><text class="aw-base" x="400.5" y="221">G</text><g class="aw-bar-weak"><title>probe position 3 from the 3&#x27; end, base C
3,051 of 14,265 records differ here (21.4%)
detected when it differs: 0% of 3,051
detected when it does not: 5% of 11,214
substitutions: C&gt;T in 3,051</title><rect x="409.0" y="192.3" width="13.0" height="15.7"/></g><text class="aw-base" x="415.5" y="221">C</text><text class="aw-base" x="430.5" y="221">A</text><text class="aw-base" x="445.5" y="221">C</text><text class="aw-tick" x="445.5" y="235">1</text><text class="aw-tick" x="385.5" y="235">5</text><text class="aw-tick" x="310.5" y="235">10</text><text class="aw-tick" x="235.5" y="235">15</text><text class="aw-tick" x="160.5" y="235">20</text><text class="aw-tick" x="85.5" y="235">25</text><text class="aw-end" x="74" y="221">5′</text><text class="aw-end aw-end-3" x="457" y="221">3′</text></svg>

## By lineage

Every evaluable record is one lineage, **Orthopoxvirus monkeypox (3431483)** (0 of 5,175 detected, 0.0%, 95% interval 0.0–0.1%), so splitting by lineage adds nothing to the figure above. The split matters where an assay spans several clades: a pooled percentage can look healthy while one lineage fails completely.


## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).

Disclosures on this entry: `amplicon_measured_not_published`.


## What reached the statistics

17,577 records were screened for this assay and **14,670 (83%)** were evaluable, meaning both primers landed in the right orientation and size range. 2,907 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 2,892 |
| `chance_anchor` | 3 |

