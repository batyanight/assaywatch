# Duplex Real-Time PCR for Rapid Simultaneous Detection of Batrachochytrium dendrobatidis and Batrachochytrium salamandrivorans in Amphibian Samples

<p class="aw-byline">Blooi · Journal of Clinical Microbiology · 2013</p>

<p class="aw-doi"><a href="https://doi.org/10.1128/JCM.02313-13">doi:10.1128/JCM.02313-13</a></p>

??? quote "Full citation"
    Blooi M et al. 2013. J Clin Microbiol 51:4173-4177

<p class="aw-assay-line"><span class="aw-chip aw-chip-insufficient-data">insufficient data</span> <span class="aw-id">B_salamandrivorans_Internal_transcribes_spa_Blooi_2013</span></p>

**Batrachochytrium salamandrivorans — ITS real-time PCR STerF/STerR (Blooi 2013)**

| | |
|---|---|
| Target | Batrachochytrium salamandrivorans (<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1357716" title="Batrachochytrium salamandrivorans">taxid 1357716</a>) |
| Gene | ITS1-5.8S rDNA |
| Chemistry | mgb |
| Amplicon | — |
| Registry status | active |

## Oligos

| role | name | sequence (5'→3') | length |
|---|---|---|---|
| forward | STerF | `TGCTCCATCTCCCCCTCTTCA` | 21 nt |
| reverse | STerR | `TGAACGCACATTGCACTCTAC` | 21 nt |
| probe | STerPROBE | `ACAAGAAAATACTATTGATTCTCAAACAGGCA` | 32 nt |

## Verdict

**insufficient data** — too few evaluable records to support an estimate; reported, never flagged

Every value the call was derived from, permitting manual recomputation:

| | detected | evaluable | share | 95% interval |
|---|---|---|---|---|
| recent window (24 months, from Oct 2024) | 0 | 5 | 0.0% | 0.0% – 43.4% |
| baseline (everything earlier) | 1 | 1 | 100.0% | 20.7% – 100.0% |

Change from baseline, Newcombe interval: **-100.0% to -9.5%**. Threshold: **90.0%**.

*5 evaluable records since Oct 2024, below the minimum of 15; the detected share is 0% (0%-43%), too wide to act on*

From the 2026-10-31 run. A status indicates where to direct attention rather than establishing a result; [known limitations](../limitations.md) reports how often these calls are correct.

## Predicted detection by deposit year

The proportion of deposited sequence this assay is predicted to detect, by year of
deposit. The shaded band marks the recent window and the dashed line the threshold.
Marker size encodes the number of records behind each point, since 100% of three
records and 100% of three thousand are not equivalent claims.

<svg class="aw-chart" viewBox="0 0 720 230" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Predicted detection by deposit year, 2013 to 2024, against a 90 percent threshold."><rect class="aw-window" x="706.0" y="12.0" width="0.0" height="180.0"><title>the recent window: 24 months from Oct 2024</title></rect><line class="aw-grid" x1="44.0" y1="183.8" x2="706.0" y2="183.8"/><text class="aw-tick aw-tick-y" x="37.0" y="187.3">0</text><line class="aw-grid" x1="44.0" y1="142.9" x2="706.0" y2="142.9"/><text class="aw-tick aw-tick-y" x="37.0" y="146.4">25</text><line class="aw-grid" x1="44.0" y1="102.0" x2="706.0" y2="102.0"/><text class="aw-tick aw-tick-y" x="37.0" y="105.5">50</text><line class="aw-grid" x1="44.0" y1="61.1" x2="706.0" y2="61.1"/><text class="aw-tick aw-tick-y" x="37.0" y="64.6">75</text><line class="aw-grid" x1="44.0" y1="20.2" x2="706.0" y2="20.2"/><text class="aw-tick aw-tick-y" x="37.0" y="23.7">100</text><line class="aw-threshold" x1="44.0" y1="36.5" x2="706.0" y2="36.5"/><text class="aw-threshold-label" x="706.0" y="31.5">90% threshold</text><polyline class="aw-line aw-insufficient-data" points="44.0,20.2 706.0,183.8"/><g class="aw-point aw-insufficient-data"><title>2013: 1 of 1 detected (100.0%)</title><circle cx="44.0" cy="20.2" r="2.5"/></g><g class="aw-point aw-insufficient-data"><title>2024: 0 of 5 detected (0.0%) — recent window</title><circle cx="706.0" cy="183.8" r="2.8"/></g><text class="aw-tick" x="44.0" y="208">2013</text><text class="aw-tick" x="164.4" y="208">2015</text><text class="aw-tick" x="284.7" y="208">2017</text><text class="aw-tick" x="405.1" y="208">2019</text><text class="aw-tick" x="525.5" y="208">2021</text><text class="aw-tick" x="645.8" y="208">2023</text><text class="aw-axis-label" x="375" y="224">deposit year · marker size is the number of records</text></svg>

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

<svg class="aw-track" viewBox="0 0 602 258" role="img" xmlns="http://www.w3.org/2000/svg" aria-label="Mismatch map: each oligo drawn base by base with a bar showing the share of records differing at that position."><text class="aw-track-label" x="74" y="52">forward</text><text class="aw-track-name" x="74" y="64">STerF</text><rect class="aw-zone" x="344.0" y="10.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="44.0" x2="419.0" y2="44.0"/><text class="aw-base" x="111.5" y="57">T</text><text class="aw-base" x="126.5" y="57">G</text><text class="aw-base" x="141.5" y="57">C</text><text class="aw-base" x="156.5" y="57">T</text><text class="aw-base" x="171.5" y="57">C</text><text class="aw-base" x="186.5" y="57">C</text><text class="aw-base" x="201.5" y="57">A</text><text class="aw-base" x="216.5" y="57">T</text><text class="aw-base" x="231.5" y="57">C</text><text class="aw-base" x="246.5" y="57">T</text><text class="aw-base" x="261.5" y="57">C</text><text class="aw-base" x="276.5" y="57">C</text><text class="aw-base" x="291.5" y="57">C</text><text class="aw-base" x="306.5" y="57">C</text><text class="aw-base" x="321.5" y="57">C</text><text class="aw-base" x="336.5" y="57">T</text><text class="aw-base" x="351.5" y="57">C</text><text class="aw-base" x="366.5" y="57">T</text><text class="aw-base" x="381.5" y="57">T</text><text class="aw-base" x="396.5" y="57">C</text><text class="aw-base" x="411.5" y="57">A</text><text class="aw-tick" x="411.5" y="71">1</text><text class="aw-tick" x="351.5" y="71">5</text><text class="aw-tick" x="276.5" y="71">10</text><text class="aw-tick" x="201.5" y="71">15</text><text class="aw-tick" x="126.5" y="71">20</text><text class="aw-tick" x="111.5" y="71">21</text><text class="aw-end" x="100" y="57">5′</text><text class="aw-end aw-end-3" x="423" y="57">3′</text><text class="aw-track-label" x="74" y="134">reverse</text><text class="aw-track-name" x="74" y="146">STerR</text><rect class="aw-zone" x="344.0" y="92.0" width="75.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="126.0" x2="419.0" y2="126.0"/><text class="aw-base" x="111.5" y="139">T</text><text class="aw-base" x="126.5" y="139">G</text><text class="aw-base" x="141.5" y="139">A</text><text class="aw-base" x="156.5" y="139">A</text><text class="aw-base" x="171.5" y="139">C</text><text class="aw-base" x="186.5" y="139">G</text><text class="aw-base" x="201.5" y="139">C</text><text class="aw-base" x="216.5" y="139">A</text><text class="aw-base" x="231.5" y="139">C</text><text class="aw-base" x="246.5" y="139">A</text><text class="aw-base" x="261.5" y="139">T</text><text class="aw-base" x="276.5" y="139">T</text><text class="aw-base" x="291.5" y="139">G</text><text class="aw-base" x="306.5" y="139">C</text><text class="aw-base" x="321.5" y="139">A</text><text class="aw-base" x="336.5" y="139">C</text><text class="aw-base" x="351.5" y="139">T</text><text class="aw-base" x="366.5" y="139">C</text><text class="aw-base" x="381.5" y="139">T</text><text class="aw-base" x="396.5" y="139">A</text><text class="aw-base" x="411.5" y="139">C</text><text class="aw-tick" x="411.5" y="153">1</text><text class="aw-tick" x="351.5" y="153">5</text><text class="aw-tick" x="276.5" y="153">10</text><text class="aw-tick" x="201.5" y="153">15</text><text class="aw-tick" x="126.5" y="153">20</text><text class="aw-tick" x="111.5" y="153">21</text><text class="aw-end" x="100" y="139">5′</text><text class="aw-end aw-end-3" x="423" y="139">3′</text><text class="aw-track-label" x="74" y="216">probe</text><text class="aw-track-name" x="74" y="228">STerPROBE</text><rect class="aw-zone" x="254.0" y="174.0" width="180.0" height="52.0"/><line class="aw-axis" x1="104.0" y1="208.0" x2="584.0" y2="208.0"/><text class="aw-base" x="111.5" y="221">A</text><text class="aw-base" x="126.5" y="221">C</text><text class="aw-base" x="141.5" y="221">A</text><text class="aw-base" x="156.5" y="221">A</text><text class="aw-base" x="171.5" y="221">G</text><text class="aw-base" x="186.5" y="221">A</text><text class="aw-base" x="201.5" y="221">A</text><text class="aw-base" x="216.5" y="221">A</text><text class="aw-base" x="231.5" y="221">A</text><text class="aw-base" x="246.5" y="221">T</text><text class="aw-base" x="261.5" y="221">A</text><text class="aw-base" x="276.5" y="221">C</text><text class="aw-base" x="291.5" y="221">T</text><text class="aw-base" x="306.5" y="221">A</text><text class="aw-base" x="321.5" y="221">T</text><text class="aw-base" x="336.5" y="221">T</text><text class="aw-base" x="351.5" y="221">G</text><text class="aw-base" x="366.5" y="221">A</text><text class="aw-base" x="381.5" y="221">T</text><text class="aw-base" x="396.5" y="221">T</text><text class="aw-base" x="411.5" y="221">C</text><text class="aw-base" x="426.5" y="221">T</text><text class="aw-base" x="441.5" y="221">C</text><text class="aw-base" x="456.5" y="221">A</text><text class="aw-base" x="471.5" y="221">A</text><text class="aw-base" x="486.5" y="221">A</text><text class="aw-base" x="501.5" y="221">C</text><text class="aw-base" x="516.5" y="221">A</text><text class="aw-base" x="531.5" y="221">G</text><text class="aw-base" x="546.5" y="221">G</text><text class="aw-base" x="561.5" y="221">C</text><text class="aw-base" x="576.5" y="221">A</text><text class="aw-tick" x="576.5" y="235">1</text><text class="aw-tick" x="516.5" y="235">5</text><text class="aw-tick" x="441.5" y="235">10</text><text class="aw-tick" x="366.5" y="235">15</text><text class="aw-tick" x="291.5" y="235">20</text><text class="aw-tick" x="216.5" y="235">25</text><text class="aw-tick" x="141.5" y="235">30</text><text class="aw-tick" x="111.5" y="235">32</text><text class="aw-end" x="100" y="221">5′</text><text class="aw-end aw-end-3" x="588" y="221">3′</text></svg>

## Scope

This entry declares no scope restriction, so every record retrieved for its target taxid counts toward the denominator. Where an assay was designed for a narrower range than its taxid covers, that presents as low coverage rather than drift; see [scope and retrieval](../scoping.md).

Retrieval query:

```
ITS[Title] OR ITS1[Title] OR ITS2[Title] OR "internal transcribed spacer"[Title] OR "5.8S"[Title] OR "ribosomal RNA"[Title] OR rRNA[Title] OR "ribosomal DNA"[Title]
```

A retrieval query is a claim about the population against which the assay is evaluated, and it can cease to be accurate without producing an error; see [scope and retrieval](../scoping.md).

Disclosures on this entry: `oligos_from_secondary_source`.


## Records reaching the statistics

12 records were screened for this assay and **6 (50%)** were evaluable, meaning both primers landed in the right orientation and size range. 6 produced no amplicon at all.

This is material because a record with one diverged primer is scored as a failure while a record with both diverged is excluded from the denominator entirely. The resulting bias is known, measured, and may not be correctable; see [known limitations](../limitations.md).

| why a record was not evaluable | records |
|---|---|
| `no_site` | 5 |
| `truncated` | 1 |


## Curation record

Seed list lists STerR before STerF; 

<details class="aw-curation"><summary>The full note, as the curator wrote it · in the order the curator wrote it, oldest first</summary><p>Seed list lists STerR before STerF; parser assigned by name suffix. Probe fluorophore flagged 'VERIFY' in the seed list.</p><p><b>2026-10-05</b> PROVENANCE SPLIT, found 2026-10-05 by scripts/check_primer_provenance.py and confirmed by reading Blooi et al. 2013's Methods. This entry is a COMPOSITE and the citation covers only part of it:\n - STerF and STerR are NOT Blooi's. The paper says 'The previously described forward primer STerF ... and reverse primer STerR ... were used to detect the 5.8S rRNA gene of B. salamandrivorans (6)'. Its reference (6) is Martel, A., Spitzen-van der Sluijs, A., Blooi, M. et al., 'Batrachochytrium salamandrivorans sp. nov. causes lethal chytridiomycosis in amphibians', PNAS 110, 15325-15329 (2013), doi:10.1073/pnas.1307356110 (verified against Crossref). The scope of these two primers must be read from Martel 2013.\n - The probe IS Blooi's: 'The B. salamandrivorans-specific Cy5-labeled probe STerC ... was developed using Kodon'. Note the paper calls it STerC where this registry stores STerPROBE.\nSo Blooi 2013 contributed the probe and the qPCR, not the primer pair, and oligos_designed_here is False. All three sequences match the paper exactly. The primers target the 5.8S rRNA gene; GenBank KC762295 is the reference the paper names.</p><p><b>2026-10-26</b> AMPLICON MEASURED 2026-10-26 AND DELIBERATELY NOT DECLARED. This entry declares no size, so amplicon.declared_tolerance cannot constrain it and it screens against the global 50-3000 bp window. Measured on results/2026-10-26/calls.tsv.gz: the assay has only 12 rows in the whole retrieval - 6 no_amplicon, 4 fail, 1 reduced, 1 detect - and exactly TWO products, both 161 bp. Two observations are not a declaration, and this entry is status: active, so writing 161 into it would narrow a published assay's screening window on the strength of two records. The number is recorded here instead and the flag says so. It is consistent with the B. salamandrivorans watch item in docs/RESUME-HERE.md, whose five SNU records of 2024-12-06 are 161-165 bp sequenced amplicons, so seven independent observations now sit in 161-165. DECLARE 161 ONCE THE RETRIEVAL IS WIDER: the thin archive is the real problem here, not the missing size - this is one of the assays ROADMAP Phase 0 records as having waited on its rDNA-query data.</p><p>THE FLAG IS NOT SET, AND THAT IS THE SCHEMA'S DECISION RATHER THAN A JUDGEMENT CALL. amplicon_size_unresolved is an OPEN QUESTION, and the validator correctly refuses an open question on an active entry, so setting it here would demote this entry from active. That is a maintainer decision and not a session's, exactly as the CALICIVIRUS Hel1 terminal base was. The measurement above is therefore recorded as a caveat in this note instead. A maintainer who wants the flag should expect active 179 -&gt; 178.</p></details>

## Corrections

If this entry misrepresents the assay, that is a defect and a report is
welcome — particularly from the group that designed it. The sequences,
the product size and the scope are all curated from the paper and can be
wrong.

<div class="aw-contribute" markdown="0">
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/issues/new?title=B_salamandrivorans_Internal_transcribes_spa_Blooi_2013%3A%20&body=Entry%3A%20B_salamandrivorans_Internal_transcribes_spa_Blooi_2013%0APage%3A%20https%3A//batyanight.github.io/assaywatch/assays/B_salamandrivorans_Internal_transcribes_spa_Blooi_2013/%0ARun%3A%202026-10-31%0A%0AWhat%20is%20wrong%2C%20and%20what%20it%20should%20be%3A%0A%0A"><b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry and run. A sentence is enough.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/edit/main/registry/B_salamandrivorans_Internal_transcribes_spa_Blooi_2013.yaml"><b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving offers to open a pull request for you.</span></a>
<a class="aw-cta" href="https://github.com/batyanight/assaywatch/blob/main/registry/B_salamandrivorans_Internal_transcribes_spa_Blooi_2013.yaml"><b>Read the entry</b><span>The file behind this page, with every field and the curator's note.</span></a>
</div>

Contributing an assay is documented in [CONTRIBUTING.md](https://github.com/batyanight/assaywatch/blob/main/CONTRIBUTING.md).

