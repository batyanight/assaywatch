# Development of two multiplex real-time PCR assays for simultaneous detection and differentiation of monkeypox virus IIa, IIb, and I clades and the B.1 lineage

<p class="aw-byline">Huo · Biosafety and Health · 2022</p>

<p class="aw-doi"><a href="https://doi.org/10.1016/j.bsheal.2022.10.005">doi:10.1016/j.bsheal.2022.10.005</a></p>

??? quote "Full citation"
    Huo S, Chen Y, Lu R, Zhang Z, Zhang G, Zhao L, Deng Y, Wu C, Tan W. 2022. Development of two multiplex real-time PCR assays for simultaneous detection and differentiation of monkeypox virus IIa, IIb, and I clades and the B.1 lineage. Biosaf Health 4:392-398

<p class="aw-assay-line"><span class="aw-chip aw-chip-declining">declining</span> <span class="aw-id">MONKEYPOX_dsDNA_F3L_region_cladeI_TaqMan_Huo_2022</span></p>

**MONKEYPOX virus (dsDNA) — Panel 1 clade I probe (Huo 2022)**

| | |
|---|---|
| Target | Monkeypox virus ([taxid 10244](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=10244)) |
| Gene | F3L region (positions 46313-46491 of ON563414.2) |
| Chemistry | hydrolysis_probe |
| Amplicon | 179 bp |
| Registry status | draft |

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `ATCCTCTCTCATTGATTTTTCGCGGGA` | 27 nt |
| reverse | `TGGAGAAGCGAGAAGTTAATAAAGC` | 25 nt |
| probe | `TCGTCGGAACTGTACACCATAGTAC` | 25 nt |

## The verdict, and the numbers behind it

**declining** — below the threshold, measurably lower than a baseline that once cleared it

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 2,429 | 4,935 | 49.2% | 47.8% – 50.6% |
| baseline (everything earlier) | 549 | 8,566 | 6.4% | 5.9% – 6.9% |

Change from baseline, Newcombe interval: **41.3% to 44.3%**. Threshold: **90.0%**.

*pooled share 49.2% has low coverage, but lineage Orthopoxvirus monkeypox (3431483) (4568 records) detects 53.2% (51.7%-54.6%); lineage verdict overrides to declining*

Trend across deposit years: by record rising (p=0, 16 years); by footprint falling (p=0.261); **the two disagree on direction**. Shown for context; it does not feed the verdict.

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../limitations.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the threshold. Marker size is the number of records behind each point, because 100%
of three records and 100% of three thousand are not the same claim.

<svg class="aw-chart" viewBox="0 0 720 230" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, 2001 to 2026, against a 90 percent threshold."><rect class="aw-window" x="653.0" y="12.0" width="53.0" height="180.0"><title>the recent window: 24 months from Oct 2024</title></rect><line class="aw-grid" x1="44.0" y1="192.0" x2="706.0" y2="192.0"/><text class="aw-tick aw-tick-y" x="37.0" y="195.5">0</text><line class="aw-grid" x1="44.0" y1="147.0" x2="706.0" y2="147.0"/><text class="aw-tick aw-tick-y" x="37.0" y="150.5">25</text><line class="aw-grid" x1="44.0" y1="102.0" x2="706.0" y2="102.0"/><text class="aw-tick aw-tick-y" x="37.0" y="105.5">50</text><line class="aw-grid" x1="44.0" y1="57.0" x2="706.0" y2="57.0"/><text class="aw-tick aw-tick-y" x="37.0" y="60.5">75</text><line class="aw-grid" x1="44.0" y1="12.0" x2="706.0" y2="12.0"/><text class="aw-tick aw-tick-y" x="37.0" y="15.5">100</text><line class="aw-threshold" x1="44.0" y1="30.0" x2="706.0" y2="30.0"/><text class="aw-threshold-label" x="706.0" y="25.0">90% threshold</text><polyline class="aw-line aw-declining" points="44.0,12.0 123.4,192.0 149.9,140.6 282.3,132.0 308.8,12.0 361.8,12.0 388.2,19.5 414.7,93.8 494.2,192.0 520.6,192.0 547.1,143.4 600.1,191.9 626.6,191.8 653.0,149.1 679.5,126.9 706.0,81.4"/><g class="aw-point aw-declining"><title>2001: 2 of 2 detected (100.0%)</title><circle cx="44.0" cy="12.0" r="2.5"/></g><g class="aw-point aw-declining"><title>2004: 0 of 1 detected (0.0%)</title><circle cx="123.4" cy="192.0" r="2.5"/></g><g class="aw-point aw-declining"><title>2005: 2 of 7 detected (28.6%)</title><circle cx="149.9" cy="140.6" r="3.0"/></g><g class="aw-point aw-declining"><title>2010: 1 of 3 detected (33.3%)</title><circle cx="282.3" cy="132.0" r="2.6"/></g><g class="aw-point aw-declining"><title>2011: 2 of 2 detected (100.0%)</title><circle cx="308.8" cy="12.0" r="2.5"/></g><g class="aw-point aw-declining"><title>2013: 2 of 2 detected (100.0%)</title><circle cx="361.8" cy="12.0" r="2.5"/></g><g class="aw-point aw-declining"><title>2014: 23 of 24 detected (95.8%)</title><circle cx="388.2" cy="19.5" r="3.8"/></g><g class="aw-point aw-declining"><title>2015: 6 of 11 detected (54.5%)</title><circle cx="414.7" cy="93.8" r="3.3"/></g><g class="aw-point aw-declining"><title>2018: 0 of 3 detected (0.0%)</title><circle cx="494.2" cy="192.0" r="2.6"/></g><g class="aw-point aw-declining"><title>2019: 0 of 8 detected (0.0%)</title><circle cx="520.6" cy="192.0" r="3.1"/></g><g class="aw-point aw-declining"><title>2020: 10 of 37 detected (27.0%)</title><circle cx="547.1" cy="143.4" r="4.1"/></g><g class="aw-point aw-declining"><title>2022: 1 of 3,446 detected (0.0%)</title><circle cx="600.1" cy="191.9" r="7.0"/></g><g class="aw-point aw-declining"><title>2023: 3 of 3,132 detected (0.1%)</title><circle cx="626.6" cy="191.8" r="7.0"/></g><g class="aw-point aw-declining"><title>2024: 500 of 2,099 detected (23.8%) — recent window</title><circle cx="653.0" cy="149.1" r="6.9"/></g><g class="aw-point aw-declining"><title>2025: 682 of 1,886 detected (36.2%) — recent window</title><circle cx="679.5" cy="126.9" r="6.8"/></g><g class="aw-point aw-declining"><title>2026: 1,744 of 2,838 detected (61.5%) — recent window</title><circle cx="706.0" cy="81.4" r="7.0"/></g><text class="aw-tick" x="44.0" y="208">2001</text><text class="aw-tick" x="149.9" y="208">2005</text><text class="aw-tick" x="255.8" y="208">2009</text><text class="aw-tick" x="361.8" y="208">2013</text><text class="aw-tick" x="467.7" y="208">2017</text><text class="aw-tick" x="573.6" y="208">2021</text><text class="aw-tick" x="679.5" y="208">2025</text><text class="aw-axis-label" x="375" y="224">deposit year · marker size is the number of records</text></svg>

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

<svg class="aw-track" viewBox="0 0 501 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="68" y="56">forward</text><rect class="aw-zone" x="408.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="44.0" x2="483.0" y2="44.0"/><text class="aw-base" x="85.5" y="57">A</text><text class="aw-base" x="100.5" y="57">T</text><text class="aw-base" x="115.5" y="57">C</text><text class="aw-base" x="130.5" y="57">C</text><text class="aw-base" x="145.5" y="57">T</text><text class="aw-base" x="160.5" y="57">C</text><text class="aw-base" x="175.5" y="57">T</text><text class="aw-base" x="190.5" y="57">C</text><text class="aw-base" x="205.5" y="57">T</text><text class="aw-base" x="220.5" y="57">C</text><text class="aw-base" x="235.5" y="57">A</text><text class="aw-base" x="250.5" y="57">T</text><text class="aw-base" x="265.5" y="57">T</text><text class="aw-base" x="280.5" y="57">G</text><text class="aw-base" x="295.5" y="57">A</text><text class="aw-base" x="310.5" y="57">T</text><text class="aw-base" x="325.5" y="57">T</text><text class="aw-base" x="340.5" y="57">T</text><text class="aw-base" x="355.5" y="57">T</text><text class="aw-base" x="370.5" y="57">T</text><text class="aw-base" x="385.5" y="57">C</text><text class="aw-base" x="400.5" y="57">G</text><text class="aw-base" x="415.5" y="57">C</text><text class="aw-base" x="430.5" y="57">G</text><text class="aw-base" x="445.5" y="57">G</text><text class="aw-base" x="460.5" y="57">G</text><text class="aw-base" x="475.5" y="57">A</text><text class="aw-tick" x="475.5" y="71">1</text><text class="aw-tick" x="415.5" y="71">5</text><text class="aw-tick" x="340.5" y="71">10</text><text class="aw-tick" x="265.5" y="71">15</text><text class="aw-tick" x="190.5" y="71">20</text><text class="aw-tick" x="115.5" y="71">25</text><text class="aw-tick" x="85.5" y="71">27</text><text class="aw-end" x="74" y="57">5′</text><text class="aw-end aw-end-3" x="487" y="57">3′</text><text class="aw-track-label" x="68" y="138">reverse</text><rect class="aw-zone" x="378.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="126.0" x2="453.0" y2="126.0"/><text class="aw-base" x="85.5" y="139">T</text><text class="aw-base" x="100.5" y="139">G</text><text class="aw-base" x="115.5" y="139">G</text><text class="aw-base" x="130.5" y="139">A</text><text class="aw-base" x="145.5" y="139">G</text><text class="aw-base" x="160.5" y="139">A</text><text class="aw-base" x="175.5" y="139">A</text><text class="aw-base" x="190.5" y="139">G</text><text class="aw-base" x="205.5" y="139">C</text><text class="aw-base" x="220.5" y="139">G</text><text class="aw-base" x="235.5" y="139">A</text><g class="aw-bar-mid"><title>reverse position 14 from the 3&#x27; end, base G
25 of 13,647 records differ here (0.2%)
detected when it differs: 0% of 25
detected when it does not: 22% of 13,622
substitutions: G&gt;A in 25</title><rect x="244.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="250.5" y="139">G</text><text class="aw-base" x="265.5" y="139">A</text><text class="aw-base" x="280.5" y="139">A</text><text class="aw-base" x="295.5" y="139">G</text><text class="aw-base" x="310.5" y="139">T</text><text class="aw-base" x="325.5" y="139">T</text><text class="aw-base" x="340.5" y="139">A</text><text class="aw-base" x="355.5" y="139">A</text><text class="aw-base" x="370.5" y="139">T</text><text class="aw-base" x="385.5" y="139">A</text><text class="aw-base" x="400.5" y="139">A</text><text class="aw-base" x="415.5" y="139">A</text><text class="aw-base" x="430.5" y="139">G</text><text class="aw-base" x="445.5" y="139">C</text><text class="aw-tick" x="445.5" y="153">1</text><text class="aw-tick" x="385.5" y="153">5</text><text class="aw-tick" x="310.5" y="153">10</text><text class="aw-tick" x="235.5" y="153">15</text><text class="aw-tick" x="160.5" y="153">20</text><text class="aw-tick" x="85.5" y="153">25</text><text class="aw-end" x="74" y="139">5′</text><text class="aw-end aw-end-3" x="457" y="139">3′</text><text class="aw-track-label" x="68" y="220">probe</text><rect class="aw-zone" x="378.0" y="174.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="208.0" x2="453.0" y2="208.0"/><text class="aw-base" x="85.5" y="221">T</text><text class="aw-base" x="100.5" y="221">C</text><text class="aw-base" x="115.5" y="221">G</text><text class="aw-base" x="130.5" y="221">T</text><g class="aw-bar-strong"><title>probe position 21 from the 3&#x27; end, base C
10,070 of 13,647 records differ here (73.8%)
detected when it differs: 0% of 10,070
detected when it does not: 83% of 3,577
substitutions: C&gt;T in 10,070</title><rect x="139.0" y="178.8" width="13.0" height="29.2"/></g><text class="aw-base" x="145.5" y="221">C</text><text class="aw-base" x="160.5" y="221">G</text><text class="aw-base" x="175.5" y="221">G</text><text class="aw-base" x="190.5" y="221">A</text><g class="aw-bar-strong"><title>probe position 17 from the 3&#x27; end, base A
10,643 of 13,647 records differ here (78.0%)
detected when it differs: 0% of 10,643
detected when it does not: 99% of 3,004
substitutions: A&gt;G in 10,628, A&gt;T in 15</title><rect x="199.0" y="178.0" width="13.0" height="30.0"/></g><text class="aw-base" x="205.5" y="221">A</text><text class="aw-base" x="220.5" y="221">C</text><text class="aw-base" x="235.5" y="221">T</text><text class="aw-base" x="250.5" y="221">G</text><text class="aw-base" x="265.5" y="221">T</text><text class="aw-base" x="280.5" y="221">A</text><g class="aw-bar-strong"><title>probe position 11 from the 3&#x27; end, base C
10,071 of 13,647 records differ here (73.8%)
detected when it differs: 0% of 10,071
detected when it does not: 83% of 3,576
substitutions: C&gt;A in 10,070, C&gt;T in 1</title><rect x="289.0" y="178.8" width="13.0" height="29.2"/></g><text class="aw-base" x="295.5" y="221">C</text><text class="aw-base" x="310.5" y="221">A</text><text class="aw-base" x="325.5" y="221">C</text><text class="aw-base" x="340.5" y="221">C</text><text class="aw-base" x="355.5" y="221">A</text><text class="aw-base" x="370.5" y="221">T</text><text class="aw-base" x="385.5" y="221">A</text><text class="aw-base" x="400.5" y="221">G</text><g class="aw-bar-strong"><title>probe position 3 from the 3&#x27; end, base T
10,647 of 13,647 records differ here (78.0%)
detected when it differs: 0% of 10,647
detected when it does not: 99% of 3,000
substitutions: T&gt;C in 10,647</title><rect x="409.0" y="178.0" width="13.0" height="30.0"/></g><text class="aw-base" x="415.5" y="221">T</text><text class="aw-base" x="430.5" y="221">A</text><text class="aw-base" x="445.5" y="221">C</text><text class="aw-tick" x="445.5" y="235">1</text><text class="aw-tick" x="385.5" y="235">5</text><text class="aw-tick" x="310.5" y="235">10</text><text class="aw-tick" x="235.5" y="235">15</text><text class="aw-tick" x="160.5" y="235">20</text><text class="aw-tick" x="85.5" y="235">25</text><text class="aw-end" x="74" y="221">5′</text><text class="aw-end aw-end-3" x="457" y="221">3′</text></svg>

## By lineage

Every evaluable record is one lineage, **Orthopoxvirus monkeypox (3431483)** (2,429 of 4,568 detected, 53.2%, 95% interval 51.7–54.6%), so splitting by lineage adds nothing to the figure above. The split matters where an assay spans several clades: a pooled percentage can look healthy while one lineage fails completely.


## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).

3,772 screened records fell outside the declared scope.

The paper claims this assay does **not** amplify 7 other taxa. Those are retrieved on purpose and reported as predicted cross-reactivity; they are never scored.

Disclosures on this entry: `amplicon_measured_not_published`, `scope_narrower_than_taxid`.


## What reached the statistics

14,204 records were screened for this assay and **13,501 (95%)** were evaluable, meaning both primers landed in the right orientation and size range. 703 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../limitations.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 693 |

