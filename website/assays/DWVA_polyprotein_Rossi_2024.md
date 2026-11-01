# Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens

<p class="aw-byline">Rossi · Microorganisms · 2024</p>

<p class="aw-doi"><a href="https://doi.org/10.3390/microorganisms12061105">doi:10.3390/microorganisms12061105</a></p>

??? quote "Full citation"
    Rossi, F.; Del Matto, I.; Ricchiuti, L.; Marino, L. Selection and Multiplexing of Reverse Transcription–Quantitative PCR Tests Targeting Relevant Honeybee Viral Pathogens. Microorganisms 2024, 12, 1105.

<p class="aw-assay-line"><span class="aw-chip aw-chip-low-coverage">low coverage</span> <span class="aw-id">DWVA_polyprotein_Rossi_2024</span></p>

**DEFORMED WING VIRUS A — polyprotein gene RT-qPCR, MGB probe (Rossi 2024)**

| | |
|---|---|
| Target | Deformed wing virus A (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2951794">taxid 2951794</a>) |
| Gene | polyprotein gene |
| Chemistry | mgb |
| Amplicon | 139 bp |
| Registry status | active |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | DWVAF | `CTTTGTCTTCATTAAAGCCAC` | 21 nt |
| reverse | DWVAR | `CTCATTAACTGTGTCGTTGAT` | 21 nt |
| probe | DWVAP | `TGCGTGGAATGCGTCC` | 16 nt |

## Verdict

**low coverage** — below the threshold without a measurable decline — applied beyond its design range, or never covering this taxon

Every value the call was derived from, permitting manual recomputation:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 23 | 47 | 48.9% | 35.3% – 62.8% |
| baseline (everything earlier) | 35 | 40 | 87.5% | 73.9% – 94.5% |

Change from baseline, Newcombe interval: **-53.9% to -19.2%**. Threshold: **90.0%**.

*detected share 48.9% (35%-63%) since Oct 2024, upper bound below the 90% threshold; change from baseline -54% to -19% (fell measurably, but never reached the 90% threshold in any earlier year, so this is not drift — it fell from a baseline of 88%)*

Trend across deposit years: by record falling (p = 0.00812, 5 years); by footprint falling (p = 0.0323). Reported for context; it is not an input to the verdict.

From the 2026-10-31 run. A status indicates where to direct attention rather than establishing a result; [known limitations](../limitations.md) reports how often these calls are correct.

## Predicted detection by deposit year

The proportion of deposited sequence this assay is predicted to detect, by year of
deposit. The shaded band marks the recent window and the dashed line the threshold.
Marker size encodes the number of records behind each point, since 100% of three
records and 100% of three thousand are not equivalent claims.

<svg class="aw-chart" viewBox="0 0 720 230" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, 2022 to 2026, against a 90 percent threshold."><rect class="aw-window" x="375.0" y="12.0" width="331.0" height="180.0"><title>the recent window: 24 months from Oct 2024</title></rect><line class="aw-grid" x1="44.0" y1="183.8" x2="706.0" y2="183.8"/><text class="aw-tick aw-tick-y" x="37.0" y="187.3">0</text><line class="aw-grid" x1="44.0" y1="142.9" x2="706.0" y2="142.9"/><text class="aw-tick aw-tick-y" x="37.0" y="146.4">25</text><line class="aw-grid" x1="44.0" y1="102.0" x2="706.0" y2="102.0"/><text class="aw-tick aw-tick-y" x="37.0" y="105.5">50</text><line class="aw-grid" x1="44.0" y1="61.1" x2="706.0" y2="61.1"/><text class="aw-tick aw-tick-y" x="37.0" y="64.6">75</text><line class="aw-grid" x1="44.0" y1="20.2" x2="706.0" y2="20.2"/><text class="aw-tick aw-tick-y" x="37.0" y="23.7">100</text><line class="aw-threshold" x1="44.0" y1="36.5" x2="706.0" y2="36.5"/><text class="aw-threshold-label" x="706.0" y="31.5">90% threshold</text><polyline class="aw-line aw-low-coverage" points="44.0,47.5 209.5,40.6 375.0,20.2 540.5,144.9 706.0,70.5"/><g class="aw-point aw-low-coverage"><title>2022: 5 of 6 detected (83.3%)</title><circle cx="44.0" cy="47.5" r="3.0"/></g><g class="aw-point aw-low-coverage"><title>2023: 28 of 32 detected (87.5%)</title><circle cx="209.5" cy="40.6" r="4.0"/></g><g class="aw-point aw-low-coverage"><title>2024: 2 of 2 detected (100.0%) — recent window</title><circle cx="375.0" cy="20.2" r="2.5"/></g><g class="aw-point aw-low-coverage"><title>2025: 5 of 21 detected (23.8%) — recent window</title><circle cx="540.5" cy="144.9" r="3.7"/></g><g class="aw-point aw-low-coverage"><title>2026: 18 of 26 detected (69.2%) — recent window</title><circle cx="706.0" cy="70.5" r="3.9"/></g><text class="aw-tick" x="44.0" y="208">2022</text><text class="aw-tick" x="209.5" y="208">2023</text><text class="aw-tick" x="375.0" y="208">2024</text><text class="aw-tick" x="540.5" y="208">2025</text><text class="aw-tick" x="706.0" y="208">2026</text><text class="aw-axis-label" x="375" y="224">deposit year · marker size is the number of records</text></svg>

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

<svg class="aw-track" viewBox="0 0 437 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="74" y="52">forward</text><text class="aw-track-name" x="74" y="64">DWVAF</text><rect class="aw-zone" x="344.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="44.0" x2="419.0" y2="44.0"/><text class="aw-base" x="111.5" y="57">C</text><text class="aw-base" x="126.5" y="57">T</text><text class="aw-base" x="141.5" y="57">T</text><text class="aw-base" x="156.5" y="57">T</text><text class="aw-base" x="171.5" y="57">G</text><text class="aw-base" x="186.5" y="57">T</text><text class="aw-base" x="201.5" y="57">C</text><text class="aw-base" x="216.5" y="57">T</text><text class="aw-base" x="231.5" y="57">T</text><text class="aw-base" x="246.5" y="57">C</text><text class="aw-base" x="261.5" y="57">A</text><text class="aw-base" x="276.5" y="57">T</text><text class="aw-base" x="291.5" y="57">T</text><text class="aw-base" x="306.5" y="57">A</text><text class="aw-base" x="321.5" y="57">A</text><text class="aw-base" x="336.5" y="57">A</text><text class="aw-base" x="351.5" y="57">G</text><text class="aw-base" x="366.5" y="57">C</text><text class="aw-base" x="381.5" y="57">C</text><text class="aw-base" x="396.5" y="57">A</text><text class="aw-base" x="411.5" y="57">C</text><text class="aw-tick" x="411.5" y="71">1</text><text class="aw-tick" x="351.5" y="71">5</text><text class="aw-tick" x="276.5" y="71">10</text><text class="aw-tick" x="201.5" y="71">15</text><text class="aw-tick" x="126.5" y="71">20</text><text class="aw-tick" x="111.5" y="71">21</text><text class="aw-end" x="100" y="57">5′</text><text class="aw-end aw-end-3" x="423" y="57">3′</text><text class="aw-track-label" x="74" y="134">reverse</text><text class="aw-track-name" x="74" y="146">DWVAR</text><rect class="aw-zone" x="344.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="126.0" x2="419.0" y2="126.0"/><text class="aw-base" x="111.5" y="139">C</text><text class="aw-base" x="126.5" y="139">T</text><text class="aw-base" x="141.5" y="139">C</text><text class="aw-base" x="156.5" y="139">A</text><text class="aw-base" x="171.5" y="139">T</text><text class="aw-base" x="186.5" y="139">T</text><text class="aw-base" x="201.5" y="139">A</text><text class="aw-base" x="216.5" y="139">A</text><text class="aw-base" x="231.5" y="139">C</text><text class="aw-base" x="246.5" y="139">T</text><text class="aw-base" x="261.5" y="139">G</text><text class="aw-base" x="276.5" y="139">T</text><text class="aw-base" x="291.5" y="139">G</text><text class="aw-base" x="306.5" y="139">T</text><g class="aw-bar-strong"><title>reverse position 7 from the 3&#x27; end, base C
29 of 87 records differ here (33.3%)
detected when it differs: 21% of 29
detected when it does not: 90% of 58
substitutions: C&gt;T in 29
outside the 3′ window</title><rect x="315.0" y="106.4" width="13.0" height="19.6"/></g><text class="aw-base" x="321.5" y="139">C</text><text class="aw-base" x="336.5" y="139">G</text><text class="aw-base" x="351.5" y="139">T</text><g class="aw-bar-strong"><title>reverse position 4 from the 3&#x27; end, base T
25 of 87 records differ here (28.7%)
detected when it differs: 16% of 25
detected when it does not: 87% of 62
substitutions: T&gt;C in 25
inside the 3′ window</title><rect x="360.0" y="107.8" width="13.0" height="18.2"/></g><text class="aw-base" x="366.5" y="139">T</text><text class="aw-base" x="381.5" y="139">G</text><text class="aw-base" x="396.5" y="139">A</text><text class="aw-base" x="411.5" y="139">T</text><text class="aw-tick" x="411.5" y="153">1</text><text class="aw-tick" x="351.5" y="153">5</text><text class="aw-tick" x="276.5" y="153">10</text><text class="aw-tick" x="201.5" y="153">15</text><text class="aw-tick" x="126.5" y="153">20</text><text class="aw-tick" x="111.5" y="153">21</text><text class="aw-end" x="100" y="139">5′</text><text class="aw-end aw-end-3" x="423" y="139">3′</text><text class="aw-track-label" x="74" y="216">probe</text><text class="aw-track-name" x="74" y="228">DWVAP</text><rect class="aw-zone" x="179.0" y="174.0" width="90.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="208.0" x2="344.0" y2="208.0"/><text class="aw-base" x="111.5" y="221">T</text><text class="aw-base" x="126.5" y="221">G</text><text class="aw-base" x="141.5" y="221">C</text><text class="aw-base" x="156.5" y="221">G</text><text class="aw-base" x="171.5" y="221">T</text><text class="aw-base" x="186.5" y="221">G</text><text class="aw-base" x="201.5" y="221">G</text><text class="aw-base" x="216.5" y="221">A</text><text class="aw-base" x="231.5" y="221">A</text><text class="aw-base" x="246.5" y="221">T</text><text class="aw-base" x="261.5" y="221">G</text><text class="aw-base" x="276.5" y="221">C</text><text class="aw-base" x="291.5" y="221">G</text><text class="aw-base" x="306.5" y="221">T</text><text class="aw-base" x="321.5" y="221">C</text><text class="aw-base" x="336.5" y="221">C</text><text class="aw-tick" x="336.5" y="235">1</text><text class="aw-tick" x="276.5" y="235">5</text><text class="aw-tick" x="201.5" y="235">10</text><text class="aw-tick" x="126.5" y="235">15</text><text class="aw-tick" x="111.5" y="235">16</text><text class="aw-end" x="100" y="221">5′</text><text class="aw-end aw-end-3" x="348" y="221">3′</text></svg>

## By lineage

Every evaluable record is one lineage, **Iflavirus aladeformis (3047792)** (23 of 47 detected, 48.9%, 95% interval 35.3–62.8%), so splitting by lineage adds nothing to the figure above. The split matters where an assay spans several clades: a pooled percentage can look healthy while one lineage fails completely.


## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `oligos_from_secondary_source`, `scope_narrower_than_taxid`.


## Records reaching the statistics

245 records were screened for this assay and **87 (36%)** were evaluable, meaning both primers landed in the right orientation and size range. 158 produced no amplicon at all.

This is material because a record with one diverged primer is scored as a failure while a record with both diverged is excluded from the denominator entirely. The resulting bias is known, measured, and may not be correctable; see [known limitations](../limitations.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 142 |
| `truncated` | 16 |


## Curation record

Oligos read from Table 1 of the paper (PDF page 5): the text layer and the page rendered at 200 dpi and read by eye agree. 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p><b>2026-10-06</b> Oligos read from Table 1 of the paper (PDF page 5): the text layer and the page rendered at 200 dpi and read by eye agree. The paper's Tenebrio molitor RNA extraction control oligos (TeneF/TeneR/TeneP, taken from Koppel et al. per the paper) are an exogenous control, not honeybee virus targets, and are deliberately excluded from all six honeybee virus entries made from this paper; its synthetic RNA calibrators carry no oligos. The paper tests the six assays singly and as duplexes (ABPV/BQCV, DWVA/DWVB, CBPV/SBV; also BQCV/DWVA and ABPV/DWVB); each virus is its own entry here. One-step RT-qPCR, 50 C 15 min RT, 95 C 2 min, 50 cycles of 95 C 15 s / 54 C 30 s, 0.2 uM each primer and probe. Screened with assaywatch.screen on 2026-10-06 against GenBank records fetched by esearch/efetch the same day. 'Spanning' below means a record that gives a product, or that the tool labels diverged or chance-only, or that the tool labels no_site but whose sequence still carries the cited reference amplicon region (an 11-mer chain covering at least 80% of it); records the tool labels truncated (they end inside a primer window) are not counted as spanning. DESIGN: MIXED. The paper states the reverse primers for both DWV variants are the same as Kevill et al. (ref 38), while the forward primers and probes were newly designed for each variant (Table 1 'This study [38]'; alignment of 110 sequences). DWVAR is therefore Kevill's oligo, DWVAF and DWVAP are this paper's. Kevill's paper was not available locally; oligos_designed_here left null and flagged. VERIFIED against the cited accession OR497397.1 (Deformed wing virus A isolate 9-2-G_A polyprotein gene, partial cds, 10,124 nt): DWVAF 8636-8656, probe DWVAP 8720-8735, DWVAR 8754-8774, all 0 mismatches; product 139 bp = the paper's span 8636-8774 exactly. MEASURED. The taxon is the NCBI node 'Deformed wing virus A' (txid2951794). Because most DWV records carry no A/B label, the assay was screened against 1,970 records: ALL 223 records labelled A (txid2951794), ALL 737 labelled B (txid2498590), and a 1,200-record strided sample (every ~5th id) of the 6,052 records of the species Iflavirus aladeformis (txid3047792), de-duplicated. Product length is 139 bp in 278 of 281 products (140 bp twice, 142 bp once), probe site present in 281 of 281, so amplicon_bp 139 is measured and equals the paper's.</p><p>RESULT BY LABEL, among records that span the site (A-labelled 68 of 223, B-labelled 58 of 737, unlabelled records 155 of 1,010; the rest are partial deposits too short or ending inside a primer window): A-labelled: detect 39, reduced 7, fail 22 -&gt; detect 57.4%, detect+reduced 67.6%. B-labelled: detect 2, fail 56. Unlabelled: detect 82, reduced 12, fail 60, indeterminate 1. All 281 spanning records together: detect 123 (43.8%), detect+reduced 142 (50.5%). The A-labelled fails are mostly a reverse-primer penalty (DWVAR mismatches within 4 nt of its 3' end). SCOPE / READ THIS: the variants are the same ICTV species and about 89% identical, and the paper found by experiment that each test also gives signal from the other variant's template (an apparent cross-reaction it says was not foreseen from its BLASTN check). In silico the tool scores the B-labelled records as fail for this assay (primer penalty above its limit), which is not the same as no signal in the wet lab. About 80% of DWV records carry no A/B label, so a variant-node taxid retrieves only the labelled minority; whether to scope by label or by species is a lead decision (flag VARIANT_SCOPE). Kakugo virus is matched by this test per the paper.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=DWVA_polyprotein_Rossi_2024%3A%20&body=Entry%3A%20DWVA_polyprotein_Rossi_2024%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/DWVA_polyprotein_Rossi_2024/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/DWVA_polyprotein_Rossi_2024.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/DWVA_polyprotein_Rossi_2024.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

