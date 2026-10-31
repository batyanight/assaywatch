# Development and application of a qPCR-based genotyping assay for Ophidiomyces ophidiicola to investigate the epidemiology of ophidiomycosis

<p class="aw-byline">Haynes · PLOS ONE · 2023</p>

<p class="aw-doi"><a href="https://doi.org/10.1371/journal.pone.0289159">doi:10.1371/journal.pone.0289159</a></p>

??? quote "Full citation"
    Haynes E, Lorch J, Allender MC. Development and application of a qPCR-based genotyping assay for Ophidiomyces ophidiicola to investigate the epidemiology of ophidiomycosis. PLoS ONE e0289159 (published 3 August 2023).

<p class="aw-assay-line"><span class="aw-chip aw-chip-stable">stable</span> <span class="aw-id">OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023</span></p>

**OPHIDIOMYCES OPHIDIICOLA — genotyping-panel target D, lineage-conserved qPCR locus (Haynes 2023)**

| | |
|---|---|
| Target | Ophidiomyces ophidiicola ([taxid 1387563](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1387563)) |
| Gene | target D, unannotated genomic segment shared by all six clades/lineages (position in paper's S1 Table, not in PDF) |
| Chemistry | hydrolysis_probe |
| Amplicon | 57 bp |
| Registry status | active |

## Oligos

| role | sequence (5'→3') | length |
|---|---|---|
| forward | `AGCGTTTTGCCCCAGCTA` | 18 nt |
| reverse | `GCAATGTTGCTCCGCAGTACT` | 21 nt |
| probe | `CTCGACTACGAAATCG` | 16 nt |

## The verdict, and the numbers behind it

**stable** — the recent interval does not fall below the threshold

Everything the call was made from, so you can check it yourself:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 81 | 81 | 100.0% | 95.5% – 100.0% |
| baseline (everything earlier) | 0 | 0 | — | 0.0% – 100.0% |

Change from baseline, Newcombe interval: **-100.0% to 100.0%**. Threshold: **90.0%**.

*detected share 100.0% (95%-100%) since Oct 2021 (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status tells you where to look rather than what is true — [what the output is worth](../what-the-output-is-worth.md) explains how often these calls are right.

## Detection by deposit year

How much of the deposited sequence this assay is predicted to detect, by the year
each record was deposited. The shaded band is the recent window; the dashed line is
the threshold. Marker size is the number of records behind each point, because 100%
of three records and 100% of three thousand are not the same claim.



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

<svg class="aw-track" viewBox="0 0 411 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="68" y="56">forward</text><rect class="aw-zone" x="273.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="44.0" x2="348.0" y2="44.0"/><g class="aw-bar-strong"><title>forward position 18 from the 3&#x27; end, base A
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: A&gt;C in 24</title><rect x="79.0" y="32.0" width="13.0" height="12.0"/></g><text class="aw-base" x="85.5" y="57">A</text><g class="aw-bar-strong"><title>forward position 17 from the 3&#x27; end, base G
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: G&gt;C in 46</title><rect x="94.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="100.5" y="57">G</text><text class="aw-base" x="115.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 15 from the 3&#x27; end, base G
65 of 192 records differ here (33.9%)
detected when it differs: 0% of 65
detected when it does not: 64% of 127
substitutions: G&gt;T in 41, G&gt;A in 24</title><rect x="124.0" y="24.2" width="13.0" height="19.8"/></g><text class="aw-base" x="130.5" y="57">G</text><g class="aw-bar-strong"><title>forward position 14 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;G in 24</title><rect x="139.0" y="32.0" width="13.0" height="12.0"/></g><text class="aw-base" x="145.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 13 from the 3&#x27; end, base T
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: T&gt;G in 46</title><rect x="154.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="160.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 12 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;A in 24</title><rect x="169.0" y="32.0" width="13.0" height="12.0"/></g><text class="aw-base" x="175.5" y="57">T</text><text class="aw-base" x="190.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 10 from the 3&#x27; end, base G
87 of 192 records differ here (45.3%)
detected when it differs: 0% of 87
detected when it does not: 77% of 105
substitutions: G&gt;T in 46, G&gt;C in 41</title><rect x="199.0" y="21.1" width="13.0" height="22.9"/></g><text class="aw-base" x="205.5" y="57">G</text><g class="aw-bar-strong"><title>forward position 9 from the 3&#x27; end, base C
41 of 192 records differ here (21.4%)
detected when it differs: 0% of 41
detected when it does not: 54% of 151
substitutions: C&gt;G in 41</title><rect x="214.0" y="28.3" width="13.0" height="15.7"/></g><text class="aw-base" x="220.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 8 from the 3&#x27; end, base C
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: C&gt;G in 46</title><rect x="229.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="235.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 7 from the 3&#x27; end, base C
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: C&gt;T in 46</title><rect x="244.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="250.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 6 from the 3&#x27; end, base C
65 of 192 records differ here (33.9%)
detected when it differs: 0% of 65
detected when it does not: 64% of 127
substitutions: C&gt;A in 41, C&gt;T in 24</title><rect x="259.0" y="24.2" width="13.0" height="19.8"/></g><text class="aw-base" x="265.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 5 from the 3&#x27; end, base A
65 of 192 records differ here (33.9%)
detected when it differs: 0% of 65
detected when it does not: 64% of 127
substitutions: A&gt;T in 41, A&gt;C in 24</title><rect x="274.0" y="24.2" width="13.0" height="19.8"/></g><text class="aw-base" x="280.5" y="57">A</text><text class="aw-base" x="295.5" y="57">G</text><text class="aw-base" x="310.5" y="57">C</text><text class="aw-base" x="325.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 1 from the 3&#x27; end, base A
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: A&gt;C in 46</title><rect x="334.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="340.5" y="57">A</text><text class="aw-tick" x="340.5" y="71">1</text><text class="aw-tick" x="280.5" y="71">5</text><text class="aw-tick" x="205.5" y="71">10</text><text class="aw-tick" x="130.5" y="71">15</text><text class="aw-tick" x="85.5" y="71">18</text><text class="aw-end" x="74" y="57">5′</text><text class="aw-end aw-end-3" x="352" y="57">3′</text><text class="aw-track-label" x="68" y="138">reverse</text><rect class="aw-zone" x="318.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="126.0" x2="393.0" y2="126.0"/><text class="aw-base" x="85.5" y="139">G</text><text class="aw-base" x="100.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 19 from the 3&#x27; end, base A
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: A&gt;T in 24</title><rect x="109.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="115.5" y="139">A</text><g class="aw-bar-strong"><title>reverse position 18 from the 3&#x27; end, base A
41 of 192 records differ here (21.4%)
detected when it differs: 0% of 41
detected when it does not: 54% of 151
substitutions: A&gt;G in 41</title><rect x="124.0" y="110.3" width="13.0" height="15.7"/></g><text class="aw-base" x="130.5" y="139">A</text><g class="aw-bar-strong"><title>reverse position 17 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;A in 24</title><rect x="139.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="145.5" y="139">T</text><text class="aw-base" x="160.5" y="139">G</text><g class="aw-bar-strong"><title>reverse position 15 from the 3&#x27; end, base T
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: T&gt;A in 46</title><rect x="169.0" y="109.4" width="13.0" height="16.6"/></g><text class="aw-base" x="175.5" y="139">T</text><g class="aw-bar-strong"><title>reverse position 14 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;G in 24</title><rect x="184.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="190.5" y="139">T</text><g class="aw-bar-strong"><title>reverse position 13 from the 3&#x27; end, base G
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: G&gt;A in 46</title><rect x="199.0" y="109.4" width="13.0" height="16.6"/></g><text class="aw-base" x="205.5" y="139">G</text><text class="aw-base" x="220.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 11 from the 3&#x27; end, base T
41 of 192 records differ here (21.4%)
detected when it differs: 0% of 41
detected when it does not: 54% of 151
substitutions: T&gt;C in 41</title><rect x="229.0" y="110.3" width="13.0" height="15.7"/></g><text class="aw-base" x="235.5" y="139">T</text><g class="aw-bar-strong"><title>reverse position 10 from the 3&#x27; end, base C
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: C&gt;A in 46</title><rect x="244.0" y="109.4" width="13.0" height="16.6"/></g><text class="aw-base" x="250.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 9 from the 3&#x27; end, base C
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: C&gt;T in 24</title><rect x="259.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="265.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 8 from the 3&#x27; end, base G
41 of 192 records differ here (21.4%)
detected when it differs: 0% of 41
detected when it does not: 54% of 151
substitutions: G&gt;A in 41</title><rect x="274.0" y="110.3" width="13.0" height="15.7"/></g><text class="aw-base" x="280.5" y="139">G</text><g class="aw-bar-strong"><title>reverse position 7 from the 3&#x27; end, base C
87 of 192 records differ here (45.3%)
detected when it differs: 0% of 87
detected when it does not: 77% of 105
substitutions: C&gt;G in 46, C&gt;A in 41</title><rect x="289.0" y="103.1" width="13.0" height="22.9"/></g><text class="aw-base" x="295.5" y="139">C</text><text class="aw-base" x="310.5" y="139">A</text><g class="aw-bar-strong"><title>reverse position 5 from the 3&#x27; end, base G
87 of 192 records differ here (45.3%)
detected when it differs: 0% of 87
detected when it does not: 77% of 105
substitutions: G&gt;C in 87</title><rect x="319.0" y="103.1" width="13.0" height="22.9"/></g><text class="aw-base" x="325.5" y="139">G</text><g class="aw-bar-strong"><title>reverse position 4 from the 3&#x27; end, base T
87 of 192 records differ here (45.3%)
detected when it differs: 0% of 87
detected when it does not: 77% of 105
substitutions: T&gt;G in 46, T&gt;A in 41</title><rect x="334.0" y="103.1" width="13.0" height="22.9"/></g><text class="aw-base" x="340.5" y="139">T</text><text class="aw-base" x="355.5" y="139">A</text><g class="aw-bar-strong"><title>reverse position 2 from the 3&#x27; end, base C
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: C&gt;A in 24</title><rect x="364.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="370.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 1 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;C in 24</title><rect x="379.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="385.5" y="139">T</text><text class="aw-tick" x="385.5" y="153">1</text><text class="aw-tick" x="325.5" y="153">5</text><text class="aw-tick" x="250.5" y="153">10</text><text class="aw-tick" x="175.5" y="153">15</text><text class="aw-tick" x="100.5" y="153">20</text><text class="aw-tick" x="85.5" y="153">21</text><text class="aw-end" x="74" y="139">5′</text><text class="aw-end aw-end-3" x="397" y="139">3′</text><text class="aw-track-label" x="68" y="220">probe</text><rect class="aw-zone" x="243.0" y="174.0" width="75.0" height="52.0"/><line class="aw-axis" x1="78.0" y1="208.0" x2="318.0" y2="208.0"/><text class="aw-base" x="85.5" y="221">C</text><text class="aw-base" x="100.5" y="221">T</text><text class="aw-base" x="115.5" y="221">C</text><text class="aw-base" x="130.5" y="221">G</text><text class="aw-base" x="145.5" y="221">A</text><text class="aw-base" x="160.5" y="221">C</text><text class="aw-base" x="175.5" y="221">T</text><text class="aw-base" x="190.5" y="221">A</text><text class="aw-base" x="205.5" y="221">C</text><text class="aw-base" x="220.5" y="221">G</text><text class="aw-base" x="235.5" y="221">A</text><text class="aw-base" x="250.5" y="221">A</text><text class="aw-base" x="265.5" y="221">A</text><text class="aw-base" x="280.5" y="221">T</text><text class="aw-base" x="295.5" y="221">C</text><text class="aw-base" x="310.5" y="221">G</text><text class="aw-tick" x="310.5" y="235">1</text><text class="aw-tick" x="250.5" y="235">5</text><text class="aw-tick" x="175.5" y="235">10</text><text class="aw-tick" x="100.5" y="235">15</text><text class="aw-tick" x="85.5" y="235">16</text><text class="aw-end" x="74" y="221">5′</text><text class="aw-end aw-end-3" x="322" y="221">3′</text></svg>

## By lineage

Every evaluable record is one lineage, **Ophidiomyces ophidiicola (1387563)** (81 of 81 detected, 100.0%, 95% interval 95.5–100.0%), so splitting by lineage adds nothing to the figure above. The split matters where an assay spans several clades: a pooled percentage can look healthy while one lineage fails completely.


## Scope — what this assay is judged against

This entry declares no `scope_taxids`, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower set than its taxid covers, that reads as low coverage rather than as drift — see [scoping](../scoping.md).

Retrieval query:

```
"whole genome shotgun"[Title]
```

A retrieval query is a scientific claim about the population the assay is being judged against, and it can go stale silently — see [scoping](../scoping.md).

Disclosures on this entry: `retrieval_scope_incomplete`, `pairing_is_curator_reading`, `chemistry_detail_missing`, `thin_evidence`.


## What reached the statistics

25,593 records were screened for this assay and **81 (0%)** were evaluable, meaning both primers landed in the right orientation and size range. 25,512 produced no amplicon at all.

This matters because a record with one drifted primer counts as a failure while a record with both drifted leaves the denominator entirely. The bias is known, measured and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 25,185 |
| `chance_anchor` | 118 |
| `chance_pair` | 111 |
| `chance_only` | 98 |

