# Development and application of a qPCR-based genotyping assay for Ophidiomyces ophidiicola to investigate the epidemiology of ophidiomycosis

<p class="aw-byline">Haynes · PLOS ONE · 2023</p>

<p class="aw-doi"><a href="https://doi.org/10.1371/journal.pone.0289159">doi:10.1371/journal.pone.0289159</a></p>

??? quote "Full citation"
    Haynes E, Lorch J, Allender MC. Development and application of a qPCR-based genotyping assay for Ophidiomyces ophidiicola to investigate the epidemiology of ophidiomycosis. PLoS ONE e0289159 (published 3 August 2023).

<p class="aw-assay-line"><span class="aw-chip aw-chip-stable">stable</span> <span class="aw-id">OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023</span></p>

**OPHIDIOMYCES OPHIDIICOLA — genotyping-panel target D, lineage-conserved qPCR locus (Haynes 2023)**

| | |
|---|---|
| Target | Ophidiomyces ophidiicola (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1387563" title="Ophidiomyces ophidiicola">taxid 1387563</a>) |
| Gene | target D, unannotated genomic segment shared by all six clades/lineages (position in paper's S1 Table, not in PDF) |
| Chemistry | hydrolysis_probe |
| Amplicon | 57 bp |
| Registry status | active |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | D-forward | `AGCGTTTTGCCCCAGCTA` | 18 nt |
| reverse | D-reverse | `GCAATGTTGCTCCGCAGTACT` | 21 nt |
| probe | D-probe | `CTCGACTACGAAATCG` | 16 nt |

## Verdict

**stable** — the recent interval does not fall below the threshold

Every value the call was derived from, permitting manual recomputation:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (60 months, from Oct 2021) | 81 | 81 | 100.0% | 95.5% – 100.0% |
| baseline (everything earlier) | 0 | 0 | — | 0.0% – 100.0% |

Change from baseline, Newcombe interval: **-100.0% to 100.0%**. Threshold: **90.0%**.

*detected share 100.0% (95%-100%) since Oct 2021 (window widened to 60 months to reach 15 evaluable records)*

From the 2026-10-31 run. A status indicates where to direct attention rather than establishing a result; [known limitations](../limitations.md) reports how often these calls are correct.

## Predicted detection by deposit year

The proportion of deposited sequence this assay is predicted to detect, by year of
deposit. The shaded band marks the recent window and the dashed line the threshold.
Marker size encodes the number of records behind each point, since 100% of three
records and 100% of three thousand are not equivalent claims.

<svg class="aw-chart" viewBox="0 0 720 230" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, 2022 to 2022, against a 90 percent threshold."><rect class="aw-window" x="375.0" y="12.0" width="331.0" height="180.0"><title>the recent window: 60 months from Oct 2021</title></rect><line class="aw-grid" x1="44.0" y1="183.8" x2="706.0" y2="183.8"/><text class="aw-tick aw-tick-y" x="37.0" y="187.3">0</text><line class="aw-grid" x1="44.0" y1="142.9" x2="706.0" y2="142.9"/><text class="aw-tick aw-tick-y" x="37.0" y="146.4">25</text><line class="aw-grid" x1="44.0" y1="102.0" x2="706.0" y2="102.0"/><text class="aw-tick aw-tick-y" x="37.0" y="105.5">50</text><line class="aw-grid" x1="44.0" y1="61.1" x2="706.0" y2="61.1"/><text class="aw-tick aw-tick-y" x="37.0" y="64.6">75</text><line class="aw-grid" x1="44.0" y1="20.2" x2="706.0" y2="20.2"/><text class="aw-tick aw-tick-y" x="37.0" y="23.7">100</text><line class="aw-threshold" x1="44.0" y1="36.5" x2="706.0" y2="36.5"/><text class="aw-threshold-label" x="706.0" y="31.5">90% threshold</text><g class="aw-point aw-stable"><title>2022: 81 of 81 detected (100.0%) — recent window</title><circle cx="375.0" cy="20.2" r="4.7"/></g><text class="aw-tick" x="375.0" y="208">2022</text><text class="aw-axis-label" x="375" y="224">one year holds every evaluable record</text></svg>

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

<svg class="aw-track" viewBox="0 0 437 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="74" y="52">forward</text><text class="aw-track-name" x="74" y="64">D-forward</text><rect class="aw-zone" x="299.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="44.0" x2="374.0" y2="44.0"/><g class="aw-bar-strong"><title>forward position 18 from the 3&#x27; end, base A
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: A&gt;C in 24
outside the 3′ window</title><rect x="105.0" y="32.0" width="13.0" height="12.0"/></g><text class="aw-base" x="111.5" y="57">A</text><g class="aw-bar-strong"><title>forward position 17 from the 3&#x27; end, base G
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: G&gt;C in 46
outside the 3′ window</title><rect x="120.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="126.5" y="57">G</text><text class="aw-base" x="141.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 15 from the 3&#x27; end, base G
65 of 192 records differ here (33.9%)
detected when it differs: 0% of 65
detected when it does not: 64% of 127
substitutions: G&gt;T in 41, G&gt;A in 24
outside the 3′ window</title><rect x="150.0" y="24.2" width="13.0" height="19.8"/></g><text class="aw-base" x="156.5" y="57">G</text><g class="aw-bar-strong"><title>forward position 14 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;G in 24
outside the 3′ window</title><rect x="165.0" y="32.0" width="13.0" height="12.0"/></g><text class="aw-base" x="171.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 13 from the 3&#x27; end, base T
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: T&gt;G in 46
outside the 3′ window</title><rect x="180.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="186.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 12 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;A in 24
outside the 3′ window</title><rect x="195.0" y="32.0" width="13.0" height="12.0"/></g><text class="aw-base" x="201.5" y="57">T</text><text class="aw-base" x="216.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 10 from the 3&#x27; end, base G
87 of 192 records differ here (45.3%)
detected when it differs: 0% of 87
detected when it does not: 77% of 105
substitutions: G&gt;T in 46, G&gt;C in 41
outside the 3′ window</title><rect x="225.0" y="21.1" width="13.0" height="22.9"/></g><text class="aw-base" x="231.5" y="57">G</text><g class="aw-bar-strong"><title>forward position 9 from the 3&#x27; end, base C
41 of 192 records differ here (21.4%)
detected when it differs: 0% of 41
detected when it does not: 54% of 151
substitutions: C&gt;G in 41
outside the 3′ window</title><rect x="240.0" y="28.3" width="13.0" height="15.7"/></g><text class="aw-base" x="246.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 8 from the 3&#x27; end, base C
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: C&gt;G in 46
outside the 3′ window</title><rect x="255.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="261.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 7 from the 3&#x27; end, base C
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: C&gt;T in 46
outside the 3′ window</title><rect x="270.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="276.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 6 from the 3&#x27; end, base C
65 of 192 records differ here (33.9%)
detected when it differs: 0% of 65
detected when it does not: 64% of 127
substitutions: C&gt;A in 41, C&gt;T in 24
outside the 3′ window</title><rect x="285.0" y="24.2" width="13.0" height="19.8"/></g><text class="aw-base" x="291.5" y="57">C</text><g class="aw-bar-strong"><title>forward position 5 from the 3&#x27; end, base A
65 of 192 records differ here (33.9%)
detected when it differs: 0% of 65
detected when it does not: 64% of 127
substitutions: A&gt;T in 41, A&gt;C in 24
inside the 3′ window</title><rect x="300.0" y="24.2" width="13.0" height="19.8"/></g><text class="aw-base" x="306.5" y="57">A</text><text class="aw-base" x="321.5" y="57">G</text><text class="aw-base" x="336.5" y="57">C</text><text class="aw-base" x="351.5" y="57">T</text><g class="aw-bar-strong"><title>forward position 1 from the 3&#x27; end, base A
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: A&gt;C in 46
inside the 3′ window</title><rect x="360.0" y="27.4" width="13.0" height="16.6"/></g><text class="aw-base" x="366.5" y="57">A</text><text class="aw-tick" x="366.5" y="71">1</text><text class="aw-tick" x="306.5" y="71">5</text><text class="aw-tick" x="231.5" y="71">10</text><text class="aw-tick" x="156.5" y="71">15</text><text class="aw-tick" x="111.5" y="71">18</text><text class="aw-end" x="100" y="57">5′</text><text class="aw-end aw-end-3" x="378" y="57">3′</text><text class="aw-track-label" x="74" y="134">reverse</text><text class="aw-track-name" x="74" y="146">D-reverse</text><rect class="aw-zone" x="344.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="126.0" x2="419.0" y2="126.0"/><text class="aw-base" x="111.5" y="139">G</text><text class="aw-base" x="126.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 19 from the 3&#x27; end, base A
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: A&gt;T in 24
outside the 3′ window</title><rect x="135.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="141.5" y="139">A</text><g class="aw-bar-strong"><title>reverse position 18 from the 3&#x27; end, base A
41 of 192 records differ here (21.4%)
detected when it differs: 0% of 41
detected when it does not: 54% of 151
substitutions: A&gt;G in 41
outside the 3′ window</title><rect x="150.0" y="110.3" width="13.0" height="15.7"/></g><text class="aw-base" x="156.5" y="139">A</text><g class="aw-bar-strong"><title>reverse position 17 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;A in 24
outside the 3′ window</title><rect x="165.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="171.5" y="139">T</text><text class="aw-base" x="186.5" y="139">G</text><g class="aw-bar-strong"><title>reverse position 15 from the 3&#x27; end, base T
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: T&gt;A in 46
outside the 3′ window</title><rect x="195.0" y="109.4" width="13.0" height="16.6"/></g><text class="aw-base" x="201.5" y="139">T</text><g class="aw-bar-strong"><title>reverse position 14 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;G in 24
outside the 3′ window</title><rect x="210.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="216.5" y="139">T</text><g class="aw-bar-strong"><title>reverse position 13 from the 3&#x27; end, base G
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: G&gt;A in 46
outside the 3′ window</title><rect x="225.0" y="109.4" width="13.0" height="16.6"/></g><text class="aw-base" x="231.5" y="139">G</text><text class="aw-base" x="246.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 11 from the 3&#x27; end, base T
41 of 192 records differ here (21.4%)
detected when it differs: 0% of 41
detected when it does not: 54% of 151
substitutions: T&gt;C in 41
outside the 3′ window</title><rect x="255.0" y="110.3" width="13.0" height="15.7"/></g><text class="aw-base" x="261.5" y="139">T</text><g class="aw-bar-strong"><title>reverse position 10 from the 3&#x27; end, base C
46 of 192 records differ here (24.0%)
detected when it differs: 0% of 46
detected when it does not: 55% of 146
substitutions: C&gt;A in 46
outside the 3′ window</title><rect x="270.0" y="109.4" width="13.0" height="16.6"/></g><text class="aw-base" x="276.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 9 from the 3&#x27; end, base C
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: C&gt;T in 24
outside the 3′ window</title><rect x="285.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="291.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 8 from the 3&#x27; end, base G
41 of 192 records differ here (21.4%)
detected when it differs: 0% of 41
detected when it does not: 54% of 151
substitutions: G&gt;A in 41
outside the 3′ window</title><rect x="300.0" y="110.3" width="13.0" height="15.7"/></g><text class="aw-base" x="306.5" y="139">G</text><g class="aw-bar-strong"><title>reverse position 7 from the 3&#x27; end, base C
87 of 192 records differ here (45.3%)
detected when it differs: 0% of 87
detected when it does not: 77% of 105
substitutions: C&gt;G in 46, C&gt;A in 41
outside the 3′ window</title><rect x="315.0" y="103.1" width="13.0" height="22.9"/></g><text class="aw-base" x="321.5" y="139">C</text><text class="aw-base" x="336.5" y="139">A</text><g class="aw-bar-strong"><title>reverse position 5 from the 3&#x27; end, base G
87 of 192 records differ here (45.3%)
detected when it differs: 0% of 87
detected when it does not: 77% of 105
substitutions: G&gt;C in 87
inside the 3′ window</title><rect x="345.0" y="103.1" width="13.0" height="22.9"/></g><text class="aw-base" x="351.5" y="139">G</text><g class="aw-bar-strong"><title>reverse position 4 from the 3&#x27; end, base T
87 of 192 records differ here (45.3%)
detected when it differs: 0% of 87
detected when it does not: 77% of 105
substitutions: T&gt;G in 46, T&gt;A in 41
inside the 3′ window</title><rect x="360.0" y="103.1" width="13.0" height="22.9"/></g><text class="aw-base" x="366.5" y="139">T</text><text class="aw-base" x="381.5" y="139">A</text><g class="aw-bar-strong"><title>reverse position 2 from the 3&#x27; end, base C
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: C&gt;A in 24
inside the 3′ window</title><rect x="390.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="396.5" y="139">C</text><g class="aw-bar-strong"><title>reverse position 1 from the 3&#x27; end, base T
24 of 192 records differ here (12.5%)
detected when it differs: 0% of 24
detected when it does not: 48% of 168
substitutions: T&gt;C in 24
inside the 3′ window</title><rect x="405.0" y="114.0" width="13.0" height="12.0"/></g><text class="aw-base" x="411.5" y="139">T</text><text class="aw-tick" x="411.5" y="153">1</text><text class="aw-tick" x="351.5" y="153">5</text><text class="aw-tick" x="276.5" y="153">10</text><text class="aw-tick" x="201.5" y="153">15</text><text class="aw-tick" x="126.5" y="153">20</text><text class="aw-tick" x="111.5" y="153">21</text><text class="aw-end" x="100" y="139">5′</text><text class="aw-end aw-end-3" x="423" y="139">3′</text><text class="aw-track-label" x="74" y="216">probe</text><text class="aw-track-name" x="74" y="228">D-probe</text><rect class="aw-zone" x="179.0" y="174.0" width="90.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="208.0" x2="344.0" y2="208.0"/><text class="aw-base" x="111.5" y="221">C</text><text class="aw-base" x="126.5" y="221">T</text><text class="aw-base" x="141.5" y="221">C</text><text class="aw-base" x="156.5" y="221">G</text><text class="aw-base" x="171.5" y="221">A</text><text class="aw-base" x="186.5" y="221">C</text><text class="aw-base" x="201.5" y="221">T</text><text class="aw-base" x="216.5" y="221">A</text><text class="aw-base" x="231.5" y="221">C</text><text class="aw-base" x="246.5" y="221">G</text><text class="aw-base" x="261.5" y="221">A</text><text class="aw-base" x="276.5" y="221">A</text><text class="aw-base" x="291.5" y="221">A</text><text class="aw-base" x="306.5" y="221">T</text><text class="aw-base" x="321.5" y="221">C</text><text class="aw-base" x="336.5" y="221">G</text><text class="aw-tick" x="336.5" y="235">1</text><text class="aw-tick" x="276.5" y="235">5</text><text class="aw-tick" x="201.5" y="235">10</text><text class="aw-tick" x="126.5" y="235">15</text><text class="aw-tick" x="111.5" y="235">16</text><text class="aw-end" x="100" y="221">5′</text><text class="aw-end aw-end-3" x="348" y="221">3′</text></svg>

## By lineage

Every evaluable record is one lineage, **Ophidiomyces ophidiicola (1387563)** (81 of 81 detected, 100.0%, 95% interval 95.5–100.0%), so splitting by lineage adds nothing to the figure above. The split matters where an assay spans several clades: a pooled percentage can look healthy while one lineage fails completely.


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
"whole genome shotgun"[Title]
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `retrieval_scope_incomplete`, `pairing_is_curator_reading`, `chemistry_detail_missing`, `thin_evidence`.


## Records reaching the statistics

25,593 records were screened for this assay and **81 (0%)** were evaluable, meaning both primers landed in the right orientation and size range. 25,512 produced no amplicon at all.

This is material because a record with one diverged primer is scored as a failure while a record with both diverged is excluded from the denominator entirely. The resulting bias is known, measured, and may not be correctable; see [known limitations](../limitations.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 25,185 |
| `chance_anchor` | 118 |
| `chance_pair` | 111 |
| `chance_only` | 98 |


## Curation record

Added 2026-10-06 from the paper's own Table 2 (papers/10.1371_journal.pone.0289159.pdf, page 4). 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-06</b> Added 2026-10-06 from the paper's own Table 2 (papers/10.1371_journal.pone.0289159.pdf, page 4). The page was rendered at 200 dpi and Table 2 and Table 1 were read by eye; the text layer agrees with the image for all 33 sequences.</p><p>WHAT THE PAPER IS: an 11-locus GENOTYPING PANEL, not a detection assay. Eleven primer-probe sets (targets A-K) were designed on genomic segments (29 areas from a Mauve alignment of six O. ophidiicola genomes) that are shared by only some clades and clonal lineages, so that the pattern of which sets amplify assigns an isolate to a lineage (its Table 1). The paper detected positives with a different, earlier O. ophidiicola assay (its ref 38) and used this panel only afterwards; the other fungal assays it ran were specificity controls for the panel.</p><p>THE QUESTION PUT TO THIS ENTRY (is the probe allele-specific, does it belong with the Lorch 2023 pair): neither. The probes are not allele-specific, and the registry's Lorch 2023 entry (PARANANNIZZIOPSIS_ITS_Lorch_2023, a Paranannizziopsis ITS assay) is unrelated.</p><p><b>2026-10-06</b> WHY ONLY TARGET D IS ENTERED: by Table 1 the other ten targets are absent from some lineages by design (A, C, E-K and B each fail to amplify in a different subset), so entered as presence/absence assays they would report built-in 'fail' that is lineage typing working as intended. Target D is the one set the paper shows in every one of the six lineages. D is therefore the only member that is meaningful as a presence/absence marker for the species, which is this curator's reading of Table 1 and not a claim the paper makes: the paper does not offer D as a detection assay and gives no specificity data for D alone. READ: D forward AGCGTTTTGCCCCAGCTA (18), reverse GCAATGTTGCTCCGCAGTACT (21), probe CTCGACTACGAAATCG (16). The paper does not state the probe reporter, quencher or whether it is MGB ('hydrolysis-based Taqman'), so reporter and quencher are null. The target's genomic position and any gene annotation are in the paper's S1 Table, which is not in the PDF, so gene is a placeholder. The paper gives no per-target amplicon size, only a 50-100 bp design window. MEASURED: all six design genomes of Table 1 plus nine more strided from the 81 GenBank O. ophidiicola isolate assemblies (every 7th by accession; 15 isolates, about 18% of those deposited; every scaffold of each isolate fetched, 127 MB of FASTA for the six and 192 MB for the nine; fetched 2026-10-06). In 14 of the 15 assemblies D gives one product of exactly 57 bp with zero mismatches in forward, reverse and probe and the probe inside the product. The fifteenth, NWHC 44736-89, is the clonal lineage IIA isolate, and Table 1's own footnote says D is not found in the IIA genome assembly but is present in the SRA reads; the screener agrees (only chance pairings 1-2.8 kb apart with penalties of 3.5 or more, no real site), so the species-wide share against assemblies will read one lineage short for an assembly reason and not a primer reason. amplicon_bp 57 is measured and invariant (the paper states none).</p><p>CHECK OF THE WHOLE TABLE: screening all 11 sets against the six design genomes reproduces the paper's Table 1 presence/absence pattern in 65 of 66 cells (the one exception is D in IIA, above). That is strong evidence that the transcription of sets A-K is right, and it assigns the genomes to lineages: NWHC 45707-83 is clade I, 44736-89 is IIA, 44736-83 is IID, 44781-25 is IIE, 27466-1 is IIF, UAMH 6688 is clade III. Products are 56-63 bp for every set.</p><p>THE OTHER TEN SETS ARE NOT ENTERED, and three cannot be under the current schema: B's forward primer is 14 nt, E's probe 13 nt and H's probe 14 nt, below the 15 nt floor (assaywatch/schema.py OLIGO_MIN); the probes are probably MGB, for which 13-14 nt is normal. Set B was therefore tested outside the screener by exact matching: it gives a 57 bp product with the probe in the five lineages Table 1 says carry it and none in clade III.</p><p>SPECIFICITY IS NOT TESTED: GenBank holds no Paranannizziopsis or other close-relative nuclear genome (the only Paranannizziopsis records are short; none is 100 kb or more), so cross-reactivity with relatives could not be measured here. SCOPE: needs_review is set because this is a panel member used as a species marker on this curator's reading, and a maintainer may prefer to drop the file.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023%3A%20&body=Entry%3A%20OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

