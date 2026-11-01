# Design and performance testing of quantitative real time PCR assays for influenza A and B viral load measurement

<p class="aw-byline">Ward · Journal of Clinical Virology · 2004</p>

<p class="aw-doi"><a href="https://doi.org/10.1016/S1386-6532(03)00122-7">doi:10.1016/S1386-6532(03)00122-7</a></p>

??? quote "Full citation"
    Ward CL et al. 2004. J Clin Virol 29:179-188

<p class="aw-assay-line"><span class="aw-chip aw-chip-declining">declining</span> <span class="aw-id">INFLUENZA_A_M1_Ward_2004</span></p>

**Influenza A virus — M1 gene real-time RT-PCR (Ward 2004)**

| | |
|---|---|
| Target | Influenza A virus (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11320">taxid 11320</a>) |
| Gene | M1 (matrix) |
| Chemistry | hydrolysis_probe |
| Amplicon | 95 bp |
| Registry status | draft |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | senseA | `AAGACCAATCCTGTCACCTCTGA` | 23 nt |
| reverse | antisenseA | `CAAAGCGTCTACGCTGCAGTCC` | 22 nt |
| probe | influenza A probe | `TTTGTGTTCACGCTCACCGT` | 20 nt |

## Verdict

**declining** — below the threshold, and measurably lower than a baseline that previously exceeded it

Every value the call was derived from, permitting manual recomputation:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 41,798 | 70,578 | 59.2% | 58.9% – 59.6% |
| baseline (everything earlier) | 66,714 | 113,283 | 58.9% | 58.6% – 59.2% |

Change from baseline, Newcombe interval: **-0.1% to 0.8%**. Threshold: **90.0%**.

*pooled share 59.2% has low coverage, but lineage Alphainfluenzavirus influenzae (2955291) (70566 records) detects 59.2% (58.9%-59.6%); lineage verdict overrides to declining*

Trend across deposit years: by record falling (p < 1e-300, 37 years); by footprint falling (p = 3.26e-23). Reported for context; it is not an input to the verdict.

From the 2026-10-31 run. A status indicates where to direct attention rather than establishing a result; [known limitations](../limitations.md) reports how often these calls are correct.

## Predicted detection by deposit year

The proportion of deposited sequence this assay is predicted to detect, by year of
deposit. The shaded band marks the recent window and the dashed line the threshold.
Marker size encodes the number of records behind each point, since 100% of three
records and 100% of three thousand are not equivalent claims.

<svg class="aw-chart" viewBox="0 0 720 230" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, 1982 to 2026, against a 90 percent threshold."><rect class="aw-window" x="675.9" y="12.0" width="30.1" height="180.0"><title>the recent window: 24 months from Oct 2024</title></rect><line class="aw-grid" x1="44.0" y1="183.8" x2="706.0" y2="183.8"/><text class="aw-tick aw-tick-y" x="37.0" y="187.3">0</text><line class="aw-grid" x1="44.0" y1="142.9" x2="706.0" y2="142.9"/><text class="aw-tick aw-tick-y" x="37.0" y="146.4">25</text><line class="aw-grid" x1="44.0" y1="102.0" x2="706.0" y2="102.0"/><text class="aw-tick aw-tick-y" x="37.0" y="105.5">50</text><line class="aw-grid" x1="44.0" y1="61.1" x2="706.0" y2="61.1"/><text class="aw-tick aw-tick-y" x="37.0" y="64.6">75</text><line class="aw-grid" x1="44.0" y1="20.2" x2="706.0" y2="20.2"/><text class="aw-tick aw-tick-y" x="37.0" y="23.7">100</text><line class="aw-threshold" x1="44.0" y1="36.5" x2="706.0" y2="36.5"/><text class="aw-threshold-label" x="706.0" y="31.5">90% threshold</text><polyline class="aw-line aw-declining" points="44.0,20.2 119.2,20.2 134.3,102.0 164.4,20.2 194.5,20.2 209.5,33.8 224.5,20.2 269.7,20.2 284.7,20.2 299.8,32.5 314.8,33.8 329.9,28.9 344.9,30.4 360.0,28.9 375.0,39.2 390.0,32.2 405.1,37.7 420.1,34.2 435.2,40.8 450.2,31.6 465.3,34.4 480.3,39.4 495.4,41.9 510.4,50.1 525.5,56.0 540.5,72.1 555.5,89.0 570.6,74.7 585.6,97.1 600.7,119.4 615.7,78.3 630.8,83.9 645.8,150.2 660.9,108.5 675.9,83.2 691.0,84.8 706.0,96.6"/><g class="aw-point aw-declining"><title>1982: 1 of 1 detected (100.0%)</title><circle cx="44.0" cy="20.2" r="2.5"/></g><g class="aw-point aw-declining"><title>1987: 1 of 1 detected (100.0%)</title><circle cx="119.2" cy="20.2" r="2.5"/></g><g class="aw-point aw-declining"><title>1988: 1 of 2 detected (50.0%)</title><circle cx="134.3" cy="102.0" r="2.5"/></g><g class="aw-point aw-declining"><title>1990: 1 of 1 detected (100.0%)</title><circle cx="164.4" cy="20.2" r="2.5"/></g><g class="aw-point aw-declining"><title>1992: 1 of 1 detected (100.0%)</title><circle cx="194.5" cy="20.2" r="2.5"/></g><g class="aw-point aw-declining"><title>1993: 11 of 12 detected (91.7%)</title><circle cx="209.5" cy="33.8" r="3.4"/></g><g class="aw-point aw-declining"><title>1994: 2 of 2 detected (100.0%)</title><circle cx="224.5" cy="20.2" r="2.5"/></g><g class="aw-point aw-declining"><title>1997: 5 of 5 detected (100.0%)</title><circle cx="269.7" cy="20.2" r="2.8"/></g><g class="aw-point aw-declining"><title>1998: 5 of 5 detected (100.0%)</title><circle cx="284.7" cy="20.2" r="2.8"/></g><g class="aw-point aw-declining"><title>1999: 37 of 40 detected (92.5%)</title><circle cx="299.8" cy="32.5" r="4.2"/></g><g class="aw-point aw-declining"><title>2000: 22 of 24 detected (91.7%)</title><circle cx="314.8" cy="33.8" r="3.8"/></g><g class="aw-point aw-declining"><title>2001: 53 of 56 detected (94.6%)</title><circle cx="329.9" cy="28.9" r="4.4"/></g><g class="aw-point aw-declining"><title>2002: 30 of 32 detected (93.8%)</title><circle cx="344.9" cy="30.4" r="4.0"/></g><g class="aw-point aw-declining"><title>2003: 178 of 188 detected (94.7%)</title><circle cx="360.0" cy="28.9" r="5.2"/></g><g class="aw-point aw-declining"><title>2004: 152 of 172 detected (88.4%)</title><circle cx="375.0" cy="39.2" r="5.2"/></g><g class="aw-point aw-declining"><title>2005: 780 of 842 detected (92.6%)</title><circle cx="390.0" cy="32.2" r="6.3"/></g><g class="aw-point aw-declining"><title>2006: 1,445 of 1,618 detected (89.3%)</title><circle cx="405.1" cy="37.7" r="6.7"/></g><g class="aw-point aw-declining"><title>2007: 1,371 of 1,499 detected (91.5%)</title><circle cx="420.1" cy="34.2" r="6.7"/></g><g class="aw-point aw-declining"><title>2008: 1,074 of 1,229 detected (87.4%)</title><circle cx="435.2" cy="40.8" r="6.5"/></g><g class="aw-point aw-declining"><title>2009: 3,376 of 3,629 detected (93.0%)</title><circle cx="450.2" cy="31.6" r="7.0"/></g><g class="aw-point aw-declining"><title>2010: 4,673 of 5,119 detected (91.3%)</title><circle cx="465.3" cy="34.4" r="7.0"/></g><g class="aw-point aw-declining"><title>2011: 1,197 of 1,356 detected (88.3%)</title><circle cx="480.3" cy="39.4" r="6.6"/></g><g class="aw-point aw-declining"><title>2012: 1,522 of 1,755 detected (86.7%)</title><circle cx="495.4" cy="41.9" r="6.8"/></g><g class="aw-point aw-declining"><title>2013: 3,950 of 4,835 detected (81.7%)</title><circle cx="510.4" cy="50.1" r="7.0"/></g><g class="aw-point aw-declining"><title>2014: 2,805 of 3,591 detected (78.1%)</title><circle cx="525.5" cy="56.0" r="7.0"/></g><g class="aw-point aw-declining"><title>2015: 3,988 of 5,839 detected (68.3%)</title><circle cx="540.5" cy="72.1" r="7.0"/></g><g class="aw-point aw-declining"><title>2016: 3,823 of 6,596 detected (58.0%)</title><circle cx="555.5" cy="89.0" r="7.0"/></g><g class="aw-point aw-declining"><title>2017: 2,409 of 3,612 detected (66.7%)</title><circle cx="570.6" cy="74.7" r="7.0"/></g><g class="aw-point aw-declining"><title>2018: 3,511 of 6,623 detected (53.0%)</title><circle cx="585.6" cy="97.1" r="7.0"/></g><g class="aw-point aw-declining"><title>2019: 4,725 of 11,998 detected (39.4%)</title><circle cx="600.7" cy="119.4" r="7.0"/></g><g class="aw-point aw-declining"><title>2020: 4,917 of 7,627 detected (64.5%)</title><circle cx="615.7" cy="78.3" r="7.0"/></g><g class="aw-point aw-declining"><title>2021: 2,083 of 3,410 detected (61.1%)</title><circle cx="630.8" cy="83.9" r="7.0"/></g><g class="aw-point aw-declining"><title>2022: 1,836 of 8,938 detected (20.5%)</title><circle cx="645.8" cy="150.2" r="7.0"/></g><g class="aw-point aw-declining"><title>2023: 6,699 of 14,547 detected (46.1%)</title><circle cx="660.9" cy="108.5" r="7.0"/></g><g class="aw-point aw-declining"><title>2024: 14,600 of 23,749 detected (61.5%) — recent window</title><circle cx="675.9" cy="83.2" r="7.0"/></g><g class="aw-point aw-declining"><title>2025: 21,997 of 36,347 detected (60.5%) — recent window</title><circle cx="691.0" cy="84.8" r="7.0"/></g><g class="aw-point aw-declining"><title>2026: 15,231 of 28,560 detected (53.3%) — recent window</title><circle cx="706.0" cy="96.6" r="7.0"/></g><text class="aw-tick" x="44.0" y="208">1982</text><text class="aw-tick" x="134.3" y="208">1988</text><text class="aw-tick" x="224.5" y="208">1994</text><text class="aw-tick" x="314.8" y="208">2000</text><text class="aw-tick" x="405.1" y="208">2006</text><text class="aw-tick" x="495.4" y="208">2012</text><text class="aw-tick" x="585.6" y="208">2018</text><text class="aw-tick" x="675.9" y="208">2024</text><text class="aw-axis-label" x="375" y="224">deposit year · marker size is the number of records</text></svg>

## Mismatch distribution

Each oligonucleotide drawn base by base, 5′ to 3′. The shaded region is the one the
scoring penalizes more heavily, and it differs by oligonucleotide: for a primer the
3′ window, where a mismatch sits in the polymerase’s catalytic site; for a probe the
central third, since a hydrolysis probe is never extended — its 3′ end carries the
quencher and it is cleaved by exonuclease activity, so what matters is duplex
stability. Bar height is the proportion of records differing at that position; bar
color is the consequence, measured as the fall in detection between records
differing there and those not:

<span class="aw-key"><span class="aw-key-swatch aw-bar-strong"></span> detection falls by 25 points or more</span>
<span class="aw-key"><span class="aw-key-swatch aw-bar-mid"></span> falls 10 to 25</span>
<span class="aw-key"><span class="aw-key-swatch aw-bar-weak"></span> little or no effect — variation the assay tolerates</span>

Counts are available on hover. A tall gray bar indicates a tolerated polymorphism; a
short red bar indicates a position of consequence.

<svg class="aw-track" viewBox="0 0 467 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="74" y="52">forward</text><text class="aw-track-name" x="74" y="64">senseA</text><rect class="aw-zone" x="374.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="44.0" x2="449.0" y2="44.0"/><g class="aw-bar-strong"><title>forward position 23 from the 3&#x27; end, base A
25 of 183,836 records differ here (0.0%)
detected when it differs: 28% of 25
detected when it does not: 59% of 183,811
substitutions: A&gt;G in 16, A&gt;C in 7, A&gt;T in 2
outside the 3′ window</title><rect x="105.0" y="42.5" width="13.0" height="1.5"/></g><text class="aw-base" x="111.5" y="57">A</text><g class="aw-bar-strong"><title>forward position 22 from the 3&#x27; end, base A
127 of 183,836 records differ here (0.1%)
detected when it differs: 10% of 127
detected when it does not: 59% of 183,709
substitutions: A&gt;C in 122, A&gt;G in 5
outside the 3′ window</title><rect x="120.0" y="42.5" width="13.0" height="1.5"/></g><text class="aw-base" x="126.5" y="57">A</text><text class="aw-base" x="141.5" y="57">G</text><g class="aw-bar-mid"><title>forward position 20 from the 3&#x27; end, base A
757 of 183,836 records differ here (0.4%)
detected when it differs: 39% of 757
detected when it does not: 59% of 183,079
substitutions: A&gt;G in 754, A&gt;C in 2, A&gt;T in 1
outside the 3′ window</title><rect x="150.0" y="41.8" width="13.0" height="2.2"/></g><text class="aw-base" x="156.5" y="57">A</text><text class="aw-base" x="171.5" y="57">C</text><text class="aw-base" x="186.5" y="57">C</text><g class="aw-bar-weak"><title>forward position 17 from the 3&#x27; end, base A
1,742 of 183,836 records differ here (0.9%)
detected when it differs: 57% of 1,742
detected when it does not: 59% of 182,094
substitutions: A&gt;G in 1,533, A&gt;T in 196, A&gt;C in 13
outside the 3′ window</title><rect x="195.0" y="40.7" width="13.0" height="3.3"/></g><text class="aw-base" x="201.5" y="57">A</text><text class="aw-base" x="216.5" y="57">A</text><text class="aw-base" x="231.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 14 from the 3&#x27; end, base C
62,744 of 183,836 records differ here (34.1%)
detected when it differs: 6% of 62,744
detected when it does not: 86% of 121,092
substitutions: C&gt;T in 62,594, C&gt;A in 149, C&gt;G in 1
outside the 3′ window</title><rect x="240.0" y="24.1" width="13.0" height="19.9"/></g><text class="aw-base" x="246.5" y="57">C</text><g class="aw-bar-weak"><title>forward position 13 from the 3&#x27; end, base C
60,700 of 183,836 records differ here (33.0%)
detected when it differs: 84% of 60,700
detected when it does not: 47% of 123,136
substitutions: C&gt;T in 60,695, C&gt;A in 3, C&gt;G in 2
outside the 3′ window</title><rect x="255.0" y="24.5" width="13.0" height="19.5"/></g><text class="aw-base" x="261.5" y="57">C</text><text class="aw-base" x="276.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 11 from the 3&#x27; end, base G
55 of 183,836 records differ here (0.0%)
detected when it differs: 31% of 55
detected when it does not: 59% of 183,781
substitutions: G&gt;A in 50, G&gt;T in 5
outside the 3′ window</title><rect x="285.0" y="42.5" width="13.0" height="1.5"/></g><text class="aw-base" x="291.5" y="57">G</text><text class="aw-base" x="306.5" y="57">T</text><text class="aw-base" x="321.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 8 from the 3&#x27; end, base A
165 of 183,836 records differ here (0.1%)
detected when it differs: 9% of 165
detected when it does not: 59% of 183,671
substitutions: A&gt;G in 152, A&gt;C in 7, A&gt;T in 6
outside the 3′ window</title><rect x="330.0" y="42.5" width="13.0" height="1.5"/></g><text class="aw-base" x="336.5" y="57">A</text><g class="aw-bar-strong"><title>forward position 7 from the 3&#x27; end, base C
1,481 of 183,836 records differ here (0.8%)
detected when it differs: 0% of 1,481
detected when it does not: 60% of 182,355
substitutions: C&gt;T in 1,478, C&gt;A in 2, C&gt;G in 1
outside the 3′ window</title><rect x="345.0" y="40.9" width="13.0" height="3.1"/></g><text class="aw-base" x="351.5" y="57">C</text><text class="aw-base" x="366.5" y="57">C</text><g class="aw-bar-weak"><title>forward position 5 from the 3&#x27; end, base T
464 of 183,836 records differ here (0.3%)
detected when it differs: 53% of 464
detected when it does not: 59% of 183,372
substitutions: T&gt;C in 360, T&gt;A in 95, T&gt;G in 9
inside the 3′ window</title><rect x="375.0" y="42.3" width="13.0" height="1.7"/></g><text class="aw-base" x="381.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 4 from the 3&#x27; end, base C
58,685 of 183,836 records differ here (31.9%)
detected when it differs: 0% of 58,685
detected when it does not: 87% of 125,151
substitutions: C&gt;T in 58,247, C&gt;A in 437, C&gt;G in 1
inside the 3′ window</title><rect x="390.0" y="24.8" width="13.0" height="19.2"/></g><text class="aw-base" x="396.5" y="57">C</text><text class="aw-base" x="411.5" y="57">T</text><g class="aw-bar-weak"><title>forward position 2 from the 3&#x27; end, base G
2,041 of 183,836 records differ here (1.1%)
detected when it differs: 56% of 2,041
detected when it does not: 59% of 181,795
substitutions: G&gt;A in 1,984, G&gt;T in 52, G&gt;C in 5
inside the 3′ window</title><rect x="420.0" y="40.4" width="13.0" height="3.6"/></g><text class="aw-base" x="426.5" y="57">G</text><g class="aw-bar-strong"><title>forward position 1 from the 3&#x27; end, base A
41 of 183,836 records differ here (0.0%)
detected when it differs: 0% of 41
detected when it does not: 59% of 183,795
substitutions: A&gt;G in 28, A&gt;T in 12, A&gt;C in 1
inside the 3′ window</title><rect x="435.0" y="42.5" width="13.0" height="1.5"/></g><text class="aw-base" x="441.5" y="57">A</text><text class="aw-tick" x="441.5" y="71">1</text><text class="aw-tick" x="381.5" y="71">5</text><text class="aw-tick" x="306.5" y="71">10</text><text class="aw-tick" x="231.5" y="71">15</text><text class="aw-tick" x="156.5" y="71">20</text><text class="aw-tick" x="111.5" y="71">23</text><text class="aw-end" x="100" y="57">5′</text><text class="aw-end aw-end-3" x="453" y="57">3′</text><text class="aw-track-label" x="74" y="134">reverse</text><text class="aw-track-name" x="74" y="146">antisenseA</text><rect class="aw-zone" x="359.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="126.0" x2="434.0" y2="126.0"/><g class="aw-bar-weak"><title>reverse position 22 from the 3&#x27; end, base C
37,893 of 183,836 records differ here (20.6%)
detected when it differs: 96% of 37,893
detected when it does not: 49% of 145,943
substitutions: C&gt;T in 37,890, C&gt;A in 3
outside the 3′ window</title><rect x="105.0" y="110.6" width="13.0" height="15.4"/></g><text class="aw-base" x="111.5" y="139">C</text><g class="aw-bar-weak"><title>reverse position 21 from the 3&#x27; end, base A
1,633 of 183,836 records differ here (0.9%)
detected when it differs: 56% of 1,633
detected when it does not: 59% of 182,203
substitutions: A&gt;G in 1,628, A&gt;T in 4, A&gt;C in 1
outside the 3′ window</title><rect x="120.0" y="122.8" width="13.0" height="3.2"/></g><text class="aw-base" x="126.5" y="139">A</text><text class="aw-base" x="141.5" y="139">A</text><text class="aw-base" x="156.5" y="139">A</text><g class="aw-bar-weak"><title>reverse position 18 from the 3&#x27; end, base G
15,015 of 183,836 records differ here (8.2%)
detected when it differs: 62% of 15,015
detected when it does not: 59% of 168,821
substitutions: G&gt;A in 6,947, G&gt;C in 5,391, G&gt;T in 2,510
outside the 3′ window</title><rect x="165.0" y="116.3" width="13.0" height="9.7"/></g><text class="aw-base" x="171.5" y="139">G</text><g class="aw-bar-mid"><title>reverse position 17 from the 3&#x27; end, base C
26 of 183,836 records differ here (0.0%)
detected when it differs: 35% of 26
detected when it does not: 59% of 183,810
substitutions: C&gt;T in 17, C&gt;A in 6, C&gt;G in 3
outside the 3′ window</title><rect x="180.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="186.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 16 from the 3&#x27; end, base G
98 of 183,836 records differ here (0.1%)
detected when it differs: 7% of 98
detected when it does not: 59% of 183,738
substitutions: G&gt;T in 96, G&gt;C in 2
outside the 3′ window</title><rect x="195.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="201.5" y="139">G</text><g class="aw-bar-strong"><title>reverse position 15 from the 3&#x27; end, base T
332 of 183,836 records differ here (0.2%)
detected when it differs: 9% of 332
detected when it does not: 59% of 183,504
substitutions: T&gt;C in 332
outside the 3′ window</title><rect x="210.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="216.5" y="139">T</text><g class="aw-bar-weak"><title>reverse position 14 from the 3&#x27; end, base C
40 of 183,836 records differ here (0.0%)
detected when it differs: 60% of 40
detected when it does not: 59% of 183,796
substitutions: C&gt;T in 22, C&gt;A in 13, C&gt;G in 5
outside the 3′ window</title><rect x="225.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="231.5" y="139">C</text><g class="aw-bar-weak"><title>reverse position 13 from the 3&#x27; end, base T
23 of 183,836 records differ here (0.0%)
detected when it differs: 74% of 23
detected when it does not: 59% of 183,813
substitutions: T&gt;G in 23
outside the 3′ window</title><rect x="240.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="246.5" y="139">T</text><g class="aw-bar-strong"><title>reverse position 12 from the 3&#x27; end, base A
111 of 183,836 records differ here (0.1%)
detected when it differs: 27% of 111
detected when it does not: 59% of 183,725
substitutions: A&gt;G in 108, A&gt;C in 2, A&gt;T in 1
outside the 3′ window</title><rect x="255.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="261.5" y="139">A</text><g class="aw-bar-weak"><title>reverse position 11 from the 3&#x27; end, base C
24 of 183,836 records differ here (0.0%)
detected when it differs: 88% of 24
detected when it does not: 59% of 183,812
substitutions: C&gt;A in 21, C&gt;T in 3
outside the 3′ window</title><rect x="270.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="276.5" y="139">C</text><text class="aw-base" x="291.5" y="139">G</text><g class="aw-bar-strong"><title>reverse position 9 from the 3&#x27; end, base C
1,641 of 183,836 records differ here (0.9%)
detected when it differs: 12% of 1,641
detected when it does not: 59% of 182,195
substitutions: C&gt;T in 1,633, C&gt;A in 8
outside the 3′ window</title><rect x="300.0" y="122.8" width="13.0" height="3.2"/></g><text class="aw-base" x="306.5" y="139">C</text><g class="aw-bar-weak"><title>reverse position 8 from the 3&#x27; end, base T
32 of 183,836 records differ here (0.0%)
detected when it differs: 88% of 32
detected when it does not: 59% of 183,804
substitutions: T&gt;A in 28, T&gt;G in 2, T&gt;C in 2
outside the 3′ window</title><rect x="315.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="321.5" y="139">T</text><text class="aw-base" x="336.5" y="139">G</text><g class="aw-bar-strong"><title>reverse position 6 from the 3&#x27; end, base C
458 of 183,836 records differ here (0.2%)
detected when it differs: 17% of 458
detected when it does not: 59% of 183,378
substitutions: C&gt;A in 356, C&gt;T in 99, C&gt;G in 3
outside the 3′ window</title><rect x="345.0" y="124.3" width="13.0" height="1.7"/></g><text class="aw-base" x="351.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 5 from the 3&#x27; end, base A
29 of 183,836 records differ here (0.0%)
detected when it differs: 0% of 29
detected when it does not: 59% of 183,807
substitutions: A&gt;T in 16, A&gt;G in 10, A&gt;C in 3
inside the 3′ window</title><rect x="360.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="366.5" y="139">A</text><text class="aw-base" x="381.5" y="139">G</text><g class="aw-bar-weak"><title>reverse position 3 from the 3&#x27; end, base T
104 of 183,836 records differ here (0.1%)
detected when it differs: 64% of 104
detected when it does not: 59% of 183,732
substitutions: T&gt;C in 90, T&gt;G in 13, T&gt;A in 1
inside the 3′ window</title><rect x="390.0" y="124.5" width="13.0" height="1.5"/></g><text class="aw-base" x="396.5" y="139">T</text><text class="aw-base" x="411.5" y="139">C</text><text class="aw-base" x="426.5" y="139">C</text><text class="aw-tick" x="426.5" y="153">1</text><text class="aw-tick" x="366.5" y="153">5</text><text class="aw-tick" x="291.5" y="153">10</text><text class="aw-tick" x="216.5" y="153">15</text><text class="aw-tick" x="141.5" y="153">20</text><text class="aw-tick" x="111.5" y="153">22</text><text class="aw-end" x="100" y="139">5′</text><text class="aw-end aw-end-3" x="438" y="139">3′</text><text class="aw-track-label" x="74" y="216">probe</text><text class="aw-track-name" x="74" y="228">influenza A probe</text><rect class="aw-zone" x="194.0" y="174.0" width="120.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="208.0" x2="404.0" y2="208.0"/><g class="aw-bar-weak"><title>probe position 20 from the 3&#x27; end, base T
89 of 183,836 records differ here (0.0%)
detected when it differs: 55% of 89
detected when it does not: 59% of 183,747
substitutions: T&gt;G in 47, T&gt;C in 42
outside the central third</title><rect x="105.0" y="206.5" width="13.0" height="1.5"/></g><text class="aw-base" x="111.5" y="221">T</text><text class="aw-base" x="126.5" y="221">T</text><g class="aw-bar-mid"><title>probe position 18 from the 3&#x27; end, base T
2,145 of 183,836 records differ here (1.2%)
detected when it differs: 38% of 2,145
detected when it does not: 59% of 181,691
substitutions: T&gt;C in 2,049, T&gt;A in 85, T&gt;G in 11
outside the central third</title><rect x="135.0" y="204.3" width="13.0" height="3.7"/></g><text class="aw-base" x="141.5" y="221">T</text><g class="aw-bar-strong"><title>probe position 17 from the 3&#x27; end, base G
515 of 183,836 records differ here (0.3%)
detected when it differs: 1% of 515
detected when it does not: 59% of 183,321
substitutions: G&gt;A in 509, G&gt;T in 6
outside the central third</title><rect x="150.0" y="206.2" width="13.0" height="1.8"/></g><text class="aw-base" x="156.5" y="221">G</text><text class="aw-base" x="171.5" y="221">T</text><g class="aw-bar-strong"><title>probe position 15 from the 3&#x27; end, base G
65,336 of 183,836 records differ here (35.5%)
detected when it differs: 5% of 65,336
detected when it does not: 89% of 118,500
substitutions: G&gt;T in 58,925, G&gt;A in 6,355, G&gt;C in 56
outside the central third</title><rect x="180.0" y="187.7" width="13.0" height="20.3"/></g><text class="aw-base" x="186.5" y="221">G</text><text class="aw-base" x="201.5" y="221">T</text><g class="aw-bar-strong"><title>probe position 13 from the 3&#x27; end, base T
29 of 183,836 records differ here (0.0%)
detected when it differs: 0% of 29
detected when it does not: 59% of 183,807
substitutions: T&gt;A in 24, T&gt;C in 4, T&gt;G in 1
in the central third</title><rect x="210.0" y="206.5" width="13.0" height="1.5"/></g><text class="aw-base" x="216.5" y="221">T</text><g class="aw-bar-strong"><title>probe position 12 from the 3&#x27; end, base C
4,255 of 183,836 records differ here (2.3%)
detected when it differs: 0% of 4,255
detected when it does not: 60% of 179,581
substitutions: C&gt;T in 4,254, C&gt;A in 1
in the central third</title><rect x="225.0" y="202.8" width="13.0" height="5.2"/></g><text class="aw-base" x="231.5" y="221">C</text><g class="aw-bar-strong"><title>probe position 11 from the 3&#x27; end, base A
20 of 183,836 records differ here (0.0%)
detected when it differs: 0% of 20
detected when it does not: 59% of 183,816
substitutions: A&gt;C in 9, A&gt;G in 6, A&gt;T in 5
in the central third</title><rect x="240.0" y="206.5" width="13.0" height="1.5"/></g><text class="aw-base" x="246.5" y="221">A</text><text class="aw-base" x="261.5" y="221">C</text><g class="aw-bar-strong"><title>probe position 9 from the 3&#x27; end, base G
402 of 183,836 records differ here (0.2%)
detected when it differs: 0% of 402
detected when it does not: 59% of 183,434
substitutions: G&gt;A in 399, G&gt;T in 3
in the central third</title><rect x="270.0" y="206.4" width="13.0" height="1.6"/></g><text class="aw-base" x="276.5" y="221">G</text><text class="aw-base" x="291.5" y="221">C</text><text class="aw-base" x="306.5" y="221">T</text><text class="aw-base" x="321.5" y="221">C</text><text class="aw-base" x="336.5" y="221">A</text><text class="aw-base" x="351.5" y="221">C</text><g class="aw-bar-strong"><title>probe position 3 from the 3&#x27; end, base C
240 of 183,836 records differ here (0.1%)
detected when it differs: 11% of 240
detected when it does not: 59% of 183,596
substitutions: C&gt;T in 201, C&gt;A in 37, C&gt;G in 2
outside the central third</title><rect x="360.0" y="206.5" width="13.0" height="1.5"/></g><text class="aw-base" x="366.5" y="221">C</text><text class="aw-base" x="381.5" y="221">G</text><text class="aw-base" x="396.5" y="221">T</text><text class="aw-tick" x="396.5" y="235">1</text><text class="aw-tick" x="336.5" y="235">5</text><text class="aw-tick" x="261.5" y="235">10</text><text class="aw-tick" x="186.5" y="235">15</text><text class="aw-tick" x="111.5" y="235">20</text><text class="aw-end" x="100" y="221">5′</text><text class="aw-end aw-end-3" x="408" y="221">3′</text></svg>

## By lineage

Every evaluable record is one lineage, **Alphainfluenzavirus influenzae (2955291)** (41,798 of 70,566 detected, 59.2%, 95% interval 58.9–59.6%), so splitting by lineage adds nothing to the figure above. The split matters where an assay spans several clades: a pooled percentage can look healthy while one lineage fails completely.


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
"segment 7"[Title] OR ("matrix protein"[Title] AND M[Gene])
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `amplicon_disagrees_with_paper`.


## Records reaching the statistics

184,853 records were screened for this assay and **183,861 (99%)** were evaluable, meaning both primers landed in the right orientation and size range. 992 produced no amplicon at all.

This is material because a record with one diverged primer is scored as a failure while a record with both diverged is excluded from the denominator entirely. The resulting bias is known, measured, and may not be correctable; see [known limitations](../limitations.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 763 |
| `truncated` | 203 |
| `chance_anchor` | 2 |


## Curation record

ENTERED 2026-10-30 so that Yang 2014's documented drift observation has a registry assay to attach to (docs/journal/2026-10-30-two-strict-bar-drift-cases.md). 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-30</b> ENTERED 2026-10-30 so that Yang 2014's documented drift observation has a registry assay to attach to (docs/journal/2026-10-30-two-strict-bar-drift-cases.md). Oligos read verbatim from the paper's own section 2.3.2, which prints them in spaced triplets ("5'AAG ACC AAT CCT GTC ACC TCT GA 3'"); the spacing is the reason a first pass over the PMC XML found no sequences at all. Open-access copy held as papers/ward-2004-10.1016_S1386-6532(03)00122-7.pmc.xml (PMC7128145, Elsevier COVID collection). The paper designed its oligos from an alignment of 20 influenza A and 20 influenza B matrix sequences, which is what n_sequences_at_design records.</p><p>AMPLICON MEASURED AT 95 bp, NOT THE PUBLISHED 104. Measured over the first 4,000 records of this entry's own archive (data/retrieved/11320/q2ebd5918b3): both primers bind within 2 mismatches in 3,975 of them and every single one of those 3,975 gives 95 bp, with the probe binding in 3,968. The forward sits at +143, the probe at +183 and the reverse at +216 on PZ777374.2. There is no second mode. The registry takes the measured value and discloses the difference; see config.yaml under amplicon: for why.</p><p>ORIENTATION IS THE PAPER'S, AND IT IS THE FUNCTIONAL ONE. antisenseA as printed binds the MINUS strand, which is what a working reverse primer does, and the registry's existing matrix entry (Spackman) stores its reverse the same way. This is recorded because Yang 2014 prints the same primer on the opposite strand; see that entry.</p><p>DISTINCT FROM INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003 (Spackman 2002), which is the registry's other matrix assay: different design paper, different primers (no sequence is shared), different target region within the segment, and MGB rather than FAM/TAMRA chemistry. The two are siblings on the same locus and the same retrieval group, not duplicates. The design paper also prints an influenza B matrix assay (senseB / antisenseB and a VIC probe) which is NOT entered here: it is a different target taxon and a separate curation. Recorded so that a later reader knows it was seen and left. The paper's own discussion states the thesis this project is built on: "This highlights the need for regular reviews of any primer or probe sequences used diagnostically or for quantification of viruses that are subject to genetic drift." rt is two_step: the protocol amplifies 2 ul of separately made cDNA. Conditions are the paper's: 1x Universal Master Mix, 900 nM each primer, 225 nM probe, UNG 50 C for 2 min, activation 95 C for 10 min, then 40 cycles of 15 s at 95 C and 1 min at 60 C.</p><p><b>2026-10-30</b> CROSSREF AGREED 2026-10-30, AND doi_verified IS HELD FALSE ANYWAY, DELIBERATELY. `assaywatch curate` resolved this DOI and matched it to the entry (Ward 2004, "Design and performance testing of quantitative real time PCR assays for influenza A and B viral load measurement") and wrote doi_verified: true. It was then set back to false by hand, because "live" in this repository means a verified DOI and nothing else: registry.not_live_because looks at the DOI alone and ignores status, so an entry in pending/ carrying a verified DOI reads as LIVE while sitting in the directory for things that are not, and tests/test_schema.py::test_nothing_in_pending_is_live_and_nothing_in_registry_is_pending fails on exactly that. The maintainer asked for these entries to wait in pending/ for sign-off, and that is incompatible with the flag being true, so the flag waits too. No information is lost: the resolution is recorded here and `assaywatch curate` re-sets the flag in one command at promotion.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=INFLUENZA_A_M1_Ward_2004%3A%20&body=Entry%3A%20INFLUENZA_A_M1_Ward_2004%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/INFLUENZA_A_M1_Ward_2004/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/INFLUENZA_A_M1_Ward_2004.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/INFLUENZA_A_M1_Ward_2004.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

