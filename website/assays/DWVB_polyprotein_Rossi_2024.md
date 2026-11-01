# Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens

<p class="aw-byline">Rossi · Microorganisms · 2024</p>

<p class="aw-doi"><a href="https://doi.org/10.3390/microorganisms12061105">doi:10.3390/microorganisms12061105</a></p>

??? quote "Full citation"
    Rossi, F.; Del Matto, I.; Ricchiuti, L.; Marino, L. Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens. Microorganisms 2024, 12, 1105.

<p class="aw-assay-line"><span class="aw-chip aw-chip-declining">declining</span> <span class="aw-id">DWVB_polyprotein_Rossi_2024</span></p>

**DEFORMED WING VIRUS B — polyprotein gene RT-qPCR, MGB probe (Rossi 2024)**

| | |
|---|---|
| Target | Deformed wing virus B (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2498590">taxid 2498590</a>) |
| Gene | polyprotein gene |
| Chemistry | mgb |
| Amplicon | 138 bp |
| Registry status | active |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | DWVBF | `TTTATCTTCATTAAAACCGCCA` | 22 nt |
| reverse | DWVBR | `CTCATTAACTGAGTTGTTGTC` | 21 nt |
| probe | DWVBP | `ATCTTTTGAGAGGGATGAGA` | 20 nt |

## Verdict

**declining** — below the threshold, and measurably lower than a baseline that previously exceeded it

Every value the call was derived from, permitting manual recomputation:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 12 | 16 | 75.0% | 50.5% – 89.8% |
| baseline (everything earlier) | 41 | 41 | 100.0% | 91.4% – 100.0% |

Change from baseline, Newcombe interval: **-49.5% to -7.9%**. Threshold: **90.0%**.

*detected share 75.0% (51%-90%) since Oct 2024, upper bound below the 90% threshold; change from baseline -49% to -8%*

Trend across deposit years: by record falling (p = 8.25e-05, 3 years); by footprint falling (p = 0.0232). Reported for context; it is not an input to the verdict.

From the 2026-10-31 run. A status indicates where to direct attention rather than establishing a result; [known limitations](../limitations.md) reports how often these calls are correct.

## Predicted detection by deposit year

The proportion of deposited sequence this assay is predicted to detect, by year of
deposit. The shaded band marks the recent window and the dashed line the threshold.
Marker size encodes the number of records behind each point, since 100% of three
records and 100% of three thousand are not equivalent claims.

<svg class="aw-chart" viewBox="0 0 720 230" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, 2023 to 2026, against a 90 percent threshold."><rect class="aw-window" x="485.3" y="12.0" width="220.7" height="180.0"><title>the recent window: 24 months from Oct 2024</title></rect><line class="aw-grid" x1="44.0" y1="183.8" x2="706.0" y2="183.8"/><text class="aw-tick aw-tick-y" x="37.0" y="187.3">0</text><line class="aw-grid" x1="44.0" y1="142.9" x2="706.0" y2="142.9"/><text class="aw-tick aw-tick-y" x="37.0" y="146.4">25</text><line class="aw-grid" x1="44.0" y1="102.0" x2="706.0" y2="102.0"/><text class="aw-tick aw-tick-y" x="37.0" y="105.5">50</text><line class="aw-grid" x1="44.0" y1="61.1" x2="706.0" y2="61.1"/><text class="aw-tick aw-tick-y" x="37.0" y="64.6">75</text><line class="aw-grid" x1="44.0" y1="20.2" x2="706.0" y2="20.2"/><text class="aw-tick aw-tick-y" x="37.0" y="23.7">100</text><line class="aw-threshold" x1="44.0" y1="36.5" x2="706.0" y2="36.5"/><text class="aw-threshold-label" x="706.0" y="31.5">90% threshold</text><polyline class="aw-line aw-declining" points="44.0,20.2 485.3,36.5 706.0,102.0"/><g class="aw-point aw-declining"><title>2023: 41 of 41 detected (100.0%)</title><circle cx="44.0" cy="20.2" r="4.2"/></g><g class="aw-point aw-declining"><title>2025: 9 of 10 detected (90.0%) — recent window</title><circle cx="485.3" cy="36.5" r="3.3"/></g><g class="aw-point aw-declining"><title>2026: 3 of 6 detected (50.0%) — recent window</title><circle cx="706.0" cy="102.0" r="3.0"/></g><text class="aw-tick" x="44.0" y="208">2023</text><text class="aw-tick" x="264.7" y="208">2024</text><text class="aw-tick" x="485.3" y="208">2025</text><text class="aw-tick" x="706.0" y="208">2026</text><text class="aw-axis-label" x="375" y="224">deposit year · marker size is the number of records</text></svg>

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

<svg class="aw-track" viewBox="0 0 452 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="74" y="52">forward</text><text class="aw-track-name" x="74" y="64">DWVBF</text><rect class="aw-zone" x="359.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="44.0" x2="434.0" y2="44.0"/><text class="aw-base" x="111.5" y="57">T</text><text class="aw-base" x="126.5" y="57">T</text><text class="aw-base" x="141.5" y="57">T</text><text class="aw-base" x="156.5" y="57">A</text><text class="aw-base" x="171.5" y="57">T</text><text class="aw-base" x="186.5" y="57">C</text><text class="aw-base" x="201.5" y="57">T</text><text class="aw-base" x="216.5" y="57">T</text><text class="aw-base" x="231.5" y="57">C</text><text class="aw-base" x="246.5" y="57">A</text><text class="aw-base" x="261.5" y="57">T</text><text class="aw-base" x="276.5" y="57">T</text><text class="aw-base" x="291.5" y="57">A</text><text class="aw-base" x="306.5" y="57">A</text><text class="aw-base" x="321.5" y="57">A</text><text class="aw-base" x="336.5" y="57">A</text><text class="aw-base" x="351.5" y="57">C</text><text class="aw-base" x="366.5" y="57">C</text><text class="aw-base" x="381.5" y="57">G</text><text class="aw-base" x="396.5" y="57">C</text><text class="aw-base" x="411.5" y="57">C</text><text class="aw-base" x="426.5" y="57">A</text><text class="aw-tick" x="426.5" y="71">1</text><text class="aw-tick" x="366.5" y="71">5</text><text class="aw-tick" x="291.5" y="71">10</text><text class="aw-tick" x="216.5" y="71">15</text><text class="aw-tick" x="141.5" y="71">20</text><text class="aw-tick" x="111.5" y="71">22</text><text class="aw-end" x="100" y="57">5′</text><text class="aw-end aw-end-3" x="438" y="57">3′</text><text class="aw-track-label" x="74" y="134">reverse</text><text class="aw-track-name" x="74" y="146">DWVBR</text><rect class="aw-zone" x="344.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="126.0" x2="419.0" y2="126.0"/><text class="aw-base" x="111.5" y="139">C</text><text class="aw-base" x="126.5" y="139">T</text><text class="aw-base" x="141.5" y="139">C</text><text class="aw-base" x="156.5" y="139">A</text><text class="aw-base" x="171.5" y="139">T</text><text class="aw-base" x="186.5" y="139">T</text><text class="aw-base" x="201.5" y="139">A</text><text class="aw-base" x="216.5" y="139">A</text><text class="aw-base" x="231.5" y="139">C</text><text class="aw-base" x="246.5" y="139">T</text><text class="aw-base" x="261.5" y="139">G</text><text class="aw-base" x="276.5" y="139">A</text><text class="aw-base" x="291.5" y="139">G</text><text class="aw-base" x="306.5" y="139">T</text><text class="aw-base" x="321.5" y="139">T</text><text class="aw-base" x="336.5" y="139">G</text><text class="aw-base" x="351.5" y="139">T</text><text class="aw-base" x="366.5" y="139">T</text><text class="aw-base" x="381.5" y="139">G</text><text class="aw-base" x="396.5" y="139">T</text><text class="aw-base" x="411.5" y="139">C</text><text class="aw-tick" x="411.5" y="153">1</text><text class="aw-tick" x="351.5" y="153">5</text><text class="aw-tick" x="276.5" y="153">10</text><text class="aw-tick" x="201.5" y="153">15</text><text class="aw-tick" x="126.5" y="153">20</text><text class="aw-tick" x="111.5" y="153">21</text><text class="aw-end" x="100" y="139">5′</text><text class="aw-end aw-end-3" x="423" y="139">3′</text><text class="aw-track-label" x="74" y="216">probe</text><text class="aw-track-name" x="74" y="228">DWVBP</text><rect class="aw-zone" x="194.0" y="174.0" width="120.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="208.0" x2="404.0" y2="208.0"/><text class="aw-base" x="111.5" y="221">A</text><text class="aw-base" x="126.5" y="221">T</text><text class="aw-base" x="141.5" y="221">C</text><text class="aw-base" x="156.5" y="221">T</text><text class="aw-base" x="171.5" y="221">T</text><text class="aw-base" x="186.5" y="221">T</text><text class="aw-base" x="201.5" y="221">T</text><text class="aw-base" x="216.5" y="221">G</text><text class="aw-base" x="231.5" y="221">A</text><text class="aw-base" x="246.5" y="221">G</text><text class="aw-base" x="261.5" y="221">A</text><text class="aw-base" x="276.5" y="221">G</text><text class="aw-base" x="291.5" y="221">G</text><text class="aw-base" x="306.5" y="221">G</text><text class="aw-base" x="321.5" y="221">A</text><text class="aw-base" x="336.5" y="221">T</text><text class="aw-base" x="351.5" y="221">G</text><text class="aw-base" x="366.5" y="221">A</text><text class="aw-base" x="381.5" y="221">G</text><text class="aw-base" x="396.5" y="221">A</text><text class="aw-tick" x="396.5" y="235">1</text><text class="aw-tick" x="336.5" y="235">5</text><text class="aw-tick" x="261.5" y="235">10</text><text class="aw-tick" x="186.5" y="235">15</text><text class="aw-tick" x="111.5" y="235">20</text><text class="aw-end" x="100" y="221">5′</text><text class="aw-end aw-end-3" x="408" y="221">3′</text></svg>

## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `oligos_from_secondary_source`, `scope_narrower_than_taxid`.


## Records reaching the statistics

737 records were screened for this assay and **57 (8%)** were evaluable, meaning both primers landed in the right orientation and size range. 680 produced no amplicon at all.

This is material because a record with one diverged primer is scored as a failure while a record with both diverged is excluded from the denominator entirely. The resulting bias is known, measured, and may not be correctable; see [known limitations](../limitations.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 670 |
| `truncated` | 9 |


## Curation record

Oligos read from Table 1 of the paper (PDF page 5): the text layer and the page rendered at 200 dpi and read by eye agree. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-06</b> Oligos read from Table 1 of the paper (PDF page 5): the text layer and the page rendered at 200 dpi and read by eye agree. The paper's Tenebrio molitor RNA extraction control oligos (TeneF/TeneR/TeneP, taken from Koppel et al. per the paper) are an exogenous control, not honeybee virus targets, and are deliberately excluded from all six honeybee virus entries made from this paper; its synthetic RNA calibrators carry no oligos. The paper tests the six assays singly and as duplexes (ABPV/BQCV, DWVA/DWVB, CBPV/SBV; also BQCV/DWVA and ABPV/DWVB); each virus is its own entry here. One-step RT-qPCR, 50 C 15 min RT, 95 C 2 min, 50 cycles of 95 C 15 s / 54 C 30 s, 0.2 uM each primer and probe. Screened with assaywatch.screen on 2026-10-06 against GenBank records fetched by esearch/efetch the same day. 'Spanning' below means a record that gives a product, or that the tool labels diverged or chance-only, or that the tool labels no_site but whose sequence still carries the cited reference amplicon region (an 11-mer chain covering at least 80% of it); records the tool labels truncated (they end inside a primer window) are not counted as spanning. DESIGN: MIXED, as for DWVA: DWVBR is Kevill et al.'s reverse primer (ref 38), DWVBF and DWVBP are new in this paper (alignment of 46 sequences). Kevill's paper not available locally; oligos_designed_here left null and flagged. VERIFIED against the cited accession OR497394.1 (Deformed wing virus B isolate 6-H_B DWV polyprotein gene, complete cds, 10,102 nt): DWVBF 8615-8636 and DWVBR 8732-8752 with 0 mismatches, product 138 bp = the paper's span 8615-8752 exactly. The probe DWVBP sits at 8692-8711 with 1 mismatch at its second base from the 5' end (T in the oligo, C in this record): a 5'-end mismatch against the paper's own cited record, not a transcription slip (rendered table agrees with the text). MEASURED on the same 1,970-record set as DWVA (all 223 A-labelled, all 737 B-labelled, strided species sample): 281 products, 138 bp in 277 (139 twice, 141 once, and one 1,788 bp chance pair in an A-labelled record), so amplicon_bp 138 is measured and equals the paper's. Probe site present in 203 of 281 products: all 58 B-labelled products, but only 28 of 68 A-labelled and 117 of 155 unlabelled, i.e. the probe is what discriminates.</p><p>RESULT BY LABEL, among records that span the site: B-labelled 58 of 737: detect 43, reduced 8, fail 6, indeterminate 1 -&gt; detect 74.1%, detect+reduced 87.9%. A-labelled 68 of 223: detect 0, fail 68. Unlabelled 157 of 1,010: detect 35, reduced 1, fail 118, indeterminate 1, no_amplicon 2. All 283 spanning records together: detect 78 (27.6%), detect+reduced 87 (30.7%). SCOPE: as for DWVA. DWV-B and DWV-A are one ICTV species; the paper found apparent cross-signal in both directions by experiment (it reports Ct differences of about 8 and 4 cycles), so use the in-silico 'fail' on the other variant as a hint, not a verdict. The 'Varroa destructor virus 1' records (txid232800, 118 records) are the older name for DWV-B and are not retrieved by the B node; flag VARIANT_SCOPE for the lead.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=DWVB_polyprotein_Rossi_2024%3A%20&body=Entry%3A%20DWVB_polyprotein_Rossi_2024%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/DWVB_polyprotein_Rossi_2024/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/DWVB_polyprotein_Rossi_2024.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/DWVB_polyprotein_Rossi_2024.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

