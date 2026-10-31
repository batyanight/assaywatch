# AssayWatch site drift — 2026-10-27

86 assays with a site breakdown. For each, the oligo positions where records differ from the primer, and the groups of accessions that carry each pattern.

**How to read this.** `pos(3')` counts from the 3' end, where 1 is the 3'-terminal base — the screen's own convention, and the one that matters for extension. `pos(5')` counts from the 5' end, which is how the oligo is written and ordered. `detected|mm` is the detected share among records that mismatch at that position; `detected|clean` is the share among records that do not. The `gap` between them is how much detection that position costs. Positions with fewer than 20 mismatching records are not shown.

**Reading the base columns.** `base` is the oligo's own base there, from the registry entry. `records carry` is what the deposits hold instead, tallied from the scored mismatches, and `order` is the IUPAC code covering both — the base you would order to restore inclusivity. A star on `base` means the screen scored a different base at that position, which happens on a pool assay when the winning alternate differs from the primary oligo; `records carry` then names the primer actually used and `base` does not. `order` is left blank where no single code is honest, rather than widened to `N`. **What this cannot tell you.** The footprint groups below key on positions alone, so two records differing in base at one position are still one group there. Organism names are parsed from deposit titles as a navigation aid, not a taxonomy lookup. And a position associated with failure may be travelling with the real cause elsewhere in the same diverged lineage rather than causing it — the footprint table below each assay is there so that covariation stays visible.

**Which records are counted.** Evaluable records only (`detect`, `reduced`, `fail`), newest version of each accession — the same record set `report.md` uses. But note the time span differs: `report.md` headlines the *recent window*, whereas the position tables below pool **every year**, because a site pattern needs all the records it can get to be characterised. The per-footprint `deposit years` column is where the temporal signal lives: a pattern confined to recent years is emerging drift, one spread evenly across years is long-standing scope mismatch. So a percentage here will not equal the recent-window percentage in `report.md`, and is not meant to.

## AVIPOXVIRUS_dsDNA_4b_core_Baek_2020

Avipoxvirus (taxid 10260) — status **low coverage** — 757 evaluable of 1,734 screened records

- forward: `5'-ACGTCAACTCATGACTGGCAAT-3'` (22 nt)
- reverse: `5'-TCTCATAACTCGAATAAGATCTTGTATCG-3'` (29 nt)
- probe: `5'-AGACGCAGACGCTATA-3'` (16 nt)

**472 of 757 evaluable records (62%) share one mismatch pattern, mostly Fowlpox virus, deposited 1993-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 20 | 3 | `G` | G&rarr;A 751, G&rarr;T 3 | `R` (99.6%) | 754 | 0.0% | 0-1% | 3 | 100.0% | 44-100% | 100.0% |  |
| probe | 7 | 10 | `C` | C&rarr;T 730 | `Y` | 730 | 0.0% | 0-1% | 27 | 11.1% | 4-28% | 11.1% |  |
| forward | 17 | 6 | `A` | A&rarr;T 488 | `W` | 488 | 0.0% | 0-1% | 269 | 1.1% | 0-3% | 1.1% |  |
| reverse | 20 | 10 | `T` | T&rarr;G 481, T&rarr;A 2 | `K` (99.6%) | 483 | 0.0% | 0-1% | 274 | 1.1% | 0-3% | 1.1% |  |
| reverse | 29 | 1 | `T` | T&rarr;C 483 | `Y` | 483 | 0.0% | 0-1% | 274 | 1.1% | 0-3% | 1.1% |  |
| reverse | 11 | 19 | `A` | A&rarr;G 479 | `R` | 479 | 0.0% | 0-1% | 278 | 1.1% | 0-3% | 1.1% |  |
| reverse | 8 | 22 | `T` | T&rarr;C 249 | `Y` | 249 | 0.0% | 0-2% | 508 | 0.6% | 0-2% | 0.6% |  |
| probe | 13 | 4 | `C` | C&rarr;T 234 | `Y` | 234 | 0.0% | 0-2% | 523 | 0.6% | 0-2% | 0.6% |  |
| reverse | 18 | 12 | `G` | G&rarr;T 185 | `K` | 185 | 0.0% | 0-2% | 572 | 0.5% | 0-2% | 0.5% |  |
| reverse | 2 | 28 | `C` | C&rarr;A 48, C&rarr;G 2 | `M` (96.0%) | 50 | 0.0% | 0-7% | 707 | 0.4% | 0-1% | 0.4% | yes |
| reverse | 17 | 13 | `A` | A&rarr;T 24, A&rarr;G 10 | `D` | 34 | 0.0% | 0-10% | 723 | 0.4% | 0-1% | 0.4% |  |
| forward | 14 | 9 | `T` | T&rarr;G 25, T&rarr;A 2, T&rarr;C 1 | `D` (96.4%) | 28 | 0.0% | 0-12% | 729 | 0.4% | 0-1% | 0.4% |  |
| forward | 8 | 15 | `C` | C&rarr;T 27 | `Y` | 27 | 0.0% | 0-12% | 730 | 0.4% | 0-1% | 0.4% |  |
| probe | 10 | 7 | `A` | A&rarr;G 20, A&rarr;T 2 | `D` | 22 | 0.0% | 0-15% | 735 | 0.4% | 0-1% | 0.4% |  |
| forward | 2 | 21 | `A` | A&rarr;G 20, A&rarr;T 1 | `R` (95.2%) | 21 | 0.0% | 0-15% | 736 | 0.4% | 0-1% | 0.4% | yes |
| probe | 4 | 13 | `T` | T&rarr;C 16, T&rarr;A 5 | `H` | 21 | 0.0% | 0-15% | 736 | 0.4% | 0-1% | 0.4% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 17,20; rev 11,20,29; prb 7 | 472 | fail | 2023×33, 2024×20, 2025×14, 2026×20 | Fowlpox virus×352, Avipoxvirus sp.×48, Avipoxvirus fowlpox×16 | `PZ594842`, `PX639487`, `PX639486`, `PX639485`, `PX639484`, `PX639483` (+466) |
| fwd 20; rev 8,18; prb 7,13 | 172 | fail | 2023×25, 2024×26, 2025×7, 2026×5 | Pigeonpox virus×78, Avipoxvirus sp.×32, Avipoxvirus×21 | `PZ043884`, `PZ043883`, `PZ043882`, `PV250209`, `PX219506`, `PV863408` (+166) |
| fwd 20; rev 2,8,17; prb 7,13 | 24 | fail | 2005×1, 2013×9, 2018×13, 2022×1 | Avipoxvirus sp.×12, Avipoxvirus isolate×11, Fowlpox virus×1 | `OM364080`, `MH175296`, `MH175263`, `MH175262`, `MH175242`, `MH175241` (+18) |
| fwd 20; rev 8; prb 7,13 | 23 | fail | 2017×1, 2018×1, 2023×4, 2024×2 | Avipoxvirus isolate×7, Avipoxvirus sp.×6, Avipoxvirus×5 | `PQ497102`, `PP341421`, `OP131515`, `OP131514`, `OP131513`, `OP131512` (+17) |
| fwd 20; rev 8; prb 4,10 | 14 | fail | 2010×1, 2013×8, 2015×1, 2018×4 | Avipoxvirus isolate×7, Avipoxvirus sp.×2, Eagle poxvirus×1 | `MH175238`, `MH175234`, `MG934698`, `KY781924`, `KR733092`, `KC693506` (+8) |
| fwd 2,8,14,20; rev 2; prb 7 | 11 | fail | 2014×3, 2021×1, 2023×1, 2024×6 | Avipoxvirus sp.×8, Avipoxvirus×3 | `PP536639`, `PP536638`, `PP536637`, `PQ109165`, `PQ109164`, `PQ109163` (+5) |
| fwd 2,8,14,20; rev 2,17; prb 7 | 9 | fail | 2013×7, 2018×1, 2026×1 | Avipoxvirus isolate×7, Avipoxvirus sp.×2 | `PZ492933`, `MH175227`, `KC017996`, `KC017995`, `KC017994`, `KC017993` (+3) |
| fwd 17,20; rev 20,29; prb 7 | 3 | fail | 2018×1, 2021×1, 2024×1 | Turkeypox virus×2, Fowlpox virus×1 | `PQ202258`, `MZ889098`, `MF496044` |

## Apicoplast_23S_LSU_Large_subunit_Molecular_2005

Apicomplexa (taxid 5794) — status **low coverage** — 1 evaluable of 329 screened records

- forward: `5'-GCGAAATTCCTGTCGGGTAAGTCC-3'` (24 nt)
- reverse: `5'-TTTYYGRTCCTCTCGTACT-3'` (19 nt)

**1 of 1 evaluable records (100%) share one mismatch pattern, mostly Plasmodium falciparum, deposited 2006, and the group's dominant call is `fail`.**

No single position reaches the reporting threshold: the mismatches are spread thinly rather than concentrated. The footprint table below is the informative view for this assay.

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 2,15,19,22,23,24 | 1 | fail | 2006×1 | Plasmodium falciparum×1 | `DQ642846` |

## Helicobacter_16S_Conley_2021

Helicobacter (taxid 209) — status **low coverage** — 795 evaluable of 3,026 screened records

- forward: `5'-TAGATAACATGCCCTTTAGTCTGGGATAGCCA-3'` (32 nt)
- reverse: `5'-GTGTGTCCGTTCACCCTCTCAGG-3'` (23 nt)
- probe: `5'-CTGGATACTCCCCAAGGGGATACC-3'` (24 nt)

**103 of 795 evaluable records (13%) share one mismatch pattern, mostly Helicobacter cinaedi, deposited 1992-2022, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 29 | 4 | `A` | A&rarr;G 512 | `R` | 512 | 0.0% | 0-1% | 283 | 0.0% | 0-1% | 0.0% |  |
| forward | 27 | 6 | `A` | A&rarr;T 335, A&rarr;G 114, A&rarr;C 4 | `D` (99.1%) | 453 | 0.0% | 0-1% | 342 | 0.0% | 0-1% | 0.0% |  |
| forward | 25 | 8 | `C` | C&rarr;T 397 | `Y` | 397 | 0.0% | 0-1% | 398 | 0.0% | 0-1% | 0.0% |  |
| reverse | 14 | 10 | `T` | T&rarr;A 338, T&rarr;C 19, T&rarr;G 3, +1 more | `H` (98.9%) | 361 | 0.0% | 0-1% | 434 | 0.0% | 0-1% | 0.0% |  |
| forward | 24 | 9 | `A` | A&rarr;G 342, A&rarr;C 1 | `R` (99.7%) | 343 | 0.0% | 0-1% | 452 | 0.0% | 0-1% | 0.0% |  |
| probe | 1 | 24 | `C` | C&rarr;G 232, C&rarr;T 2 | `S` (99.1%) | 234 | 0.0% | 0-2% | 561 | 0.0% | 0-1% | 0.0% | yes |
| probe | 2 | 23 | `C` | C&rarr;A 230, C&rarr;G 4 | `M` (98.3%) | 234 | 0.0% | 0-2% | 561 | 0.0% | 0-1% | 0.0% | yes |
| probe | 12 | 13 | `C` | C&rarr;T 234 | `Y` | 234 | 0.0% | 0-2% | 561 | 0.0% | 0-1% | 0.0% |  |
| probe | 4 | 21 | `T` | T&rarr;A 233 | `W` | 233 | 0.0% | 0-2% | 562 | 0.0% | 0-1% | 0.0% | yes |
| probe | 10 | 15 | `A` | A&rarr;C 227, A&rarr;T 6 | `M` (97.4%) | 233 | 0.0% | 0-2% | 562 | 0.0% | 0-1% | 0.0% |  |
| probe | 5 | 20 | `A` | A&rarr;G 227 | `R` | 227 | 0.0% | 0-2% | 568 | 0.0% | 0-1% | 0.0% | yes |
| forward | 12 | 21 | `C` | C&rarr;T 190, C&rarr;A 2 | `Y` (99.0%) | 192 | 0.0% | 0-2% | 603 | 0.0% | 0-1% | 0.0% |  |
| forward | 18 | 15 | `T` | T&rarr;C 176 | `Y` | 176 | 0.0% | 0-2% | 619 | 0.0% | 0-1% | 0.0% |  |
| forward | 17 | 16 | `T` | T&rarr;A 162 | `W` | 162 | 0.0% | 0-2% | 633 | 0.0% | 0-1% | 0.0% |  |
| forward | 10 | 23 | `G` | G&rarr;A 114 | `R` | 114 | 0.0% | 0-3% | 681 | 0.0% | 0-1% | 0.0% |  |
| forward | 8 | 25 | `G` | G&rarr;A 55 | `R` | 55 | 0.0% | 0-7% | 740 | 0.0% | 0-1% | 0.0% |  |
| forward | 22 | 11 | `G` | G&rarr;A 31, G&rarr;C 1 | `R` (96.9%) | 32 | 0.0% | 0-11% | 763 | 0.0% | 0-1% | 0.0% |  |
| forward | 19 | 14 | `C` | C&rarr;T 20 | `Y` | 20 | 0.0% | 0-16% | 775 | 0.0% | 0-0% | 0.0% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 24,25,27,29; rev 14; prb 1,2,4,5,10,12 | 103 | fail | 2017×2, 2018×1, 2019×3, 2022×2 | Helicobacter cinaedi×41, Helicobacter sp.×37, Helicobacter hepaticus×9 | `OP278857`, `OP278856`, `MK849616`, `MK279513`, `MK279512`, `NR_029182` (+97) |
| fwd 12,27 | 87 | fail | 2018×5, 2021×20, 2022×14, 2024×3 | Helicobacter sp.×51, Helicobacter felis×11, Helicobacter heilmannii×8 | `LC848814`, `LC848813`, `LC848812`, `NR_180203`, `NR_180202`, `NR_180201` (+81) |
| fwd 24,25,27,29; rev 14 | 78 | fail | 2021×1, 2022×3, 2025×11, 2026×2 | Helicobacter pullorum×29, Helicobacter canadensis×19, Helicobacter sp.×11 | `PP929916`, `PP929915`, `PV271819`, `PV185354`, `PV185353`, `PV185352` (+72) |
| fwd 12 | 57 | fail | 2009×1, 2010×10, 2021×5, 2022×8 | Helicobacter sp.×36, Helicobacter heilmannii×11, Helicobacter felis×6 | `OK613988`, `OK606114`, `OK606113`, `OK606111`, `OK606110`, `OK606106` (+51) |
| fwd 17,18,24,25,27,29 | 48 | fail | 2014×1, 2018×1, 2021×17, 2022×1 | Helicobacter sp.×39, Helicobacter pametensis×4, Helicobacter brantae×2 | `NR_181912`, `OL960428`, `OL960423`, `OL960422`, `OL960421`, `OL960420` (+42) |
| fwd 17,18,24,25,27,29; rev 14 | 35 | fail | 2011×3, 2021×21, 2022×1, 2025×1 | Helicobacter sp.×29, Helicobacter anseris×2, Helicobacter suncus×2 | `PV702632`, `NR_181911`, `OL960431`, `OL960430`, `OL960429`, `OL960427` (+29) |
| no mismatches | 26 | fail | 2016×1, 2017×1, 2021×11, 2022×1 | Helicobacter turcicus×12, Helicobacter sp.×8, Helicobacter jaachi×3 | `NR_181839`, `MZ781213`, `MZ781212`, `MZ781211`, `MZ781210`, `MZ781209` (+20) |
| fwd 10 | 24 | fail | 2012×5, 2013×2, 2014×2, 2020×2 | Helicobacter sp.×14, Helicobacter ganmani×8, Helicobacter fennelliae×2 | `MT967897`, `MT967527`, `NR_118766`, `NR_114604`, `NR_024836`, `KJ729586` (+18) |

## POLYOMAVIRUS_dsDNA_PREDICT_VP1_round1

Polyomaviridae (taxid 151341) — status **low coverage** — 2,072 evaluable of 14,537 screened records

- forward: `5'-CCAGACCCAACTARRAATGARAA-3'` (23 nt)
- reverse: `5'-AACAAGAGACACAAATNTTTCCNCC-3'` (25 nt)

**1,301 of 2,072 evaluable records (63%) share one mismatch pattern, mostly Betapolyomavirus hominis, deposited 1982-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 19 | 7 | `A` | A&rarr;G 1,798, A&rarr;T 97 | `D` | 1,895 | 0.0% | 0-0% | 177 | 2.8% | 1-6% | 2.8% |  |
| forward | 15 | 9 | `A` | A&rarr;C 1,288, A&rarr;T 635 | `H` | 1,923 | 0.1% | 0-0% | 149 | 2.0% | 1-6% | 1.9% |  |
| forward | 13 | 11 | `C` | C&rarr;G 1,745, C&rarr;T 44 | `S` (97.5%) | 1,789 | 0.0% | 0-0% | 283 | 1.8% | 1-4% | 1.8% |  |
| forward | 21 | 3 | `A` | A&rarr;T 1,790, A&rarr;G 5, A&rarr;C 1 | `W` (99.7%) | 1,796 | 0.1% | 0-0% | 276 | 1.4% | 1-4% | 1.4% |  |
| forward | 18 | 6 | `C` | C&rarr;T 1,575 | `Y` | 1,575 | 0.0% | 0-0% | 497 | 1.0% | 0-2% | 1.0% |  |
| reverse | 17 | 9 | `A` | A&rarr;T 157, A&rarr;G 16 | `D` | 173 | 0.0% | 0-2% | 1,899 | 0.3% | 0-1% | 0.3% |  |
| forward | 12 | 12 | `T` | T&rarr;C 91, T&rarr;A 76, T&rarr;G 2 | `H` (98.8%) | 169 | 0.0% | 0-2% | 1,903 | 0.3% | 0-1% | 0.3% |  |
| reverse | 21 | 5 | `A` | A&rarr;G 159 | `R` | 159 | 0.0% | 0-2% | 1,913 | 0.3% | 0-1% | 0.3% |  |
| reverse | 16 | 10 | `C` | C&rarr;G 73, C&rarr;A 14, C&rarr;T 2 | `V` (97.8%) | 89 | 0.0% | 0-4% | 1,983 | 0.3% | 0-1% | 0.3% |  |
| forward | 3 | 21 | `R` | R&rarr;C 39, R&rarr;T 30 | hypervariable | 69 | 0.0% | 0-5% | 2,003 | 0.2% | 0-1% | 0.2% | yes |
| reverse | 6 | 20 | `T` | T&rarr;C 43 | `Y` | 43 | 0.0% | 0-8% | 2,029 | 0.2% | 0-1% | 0.2% |  |
| forward | 23 | 1 | `C` | C&rarr;G 34 | `S` | 34 | 0.0% | 0-10% | 2,038 | 0.2% | 0-1% | 0.2% |  |
| reverse | 13 | 13 | `A` | A&rarr;C 26 | `M` | 26 | 0.0% | 0-13% | 2,046 | 0.2% | 0-1% | 0.2% |  |
| reverse | 12 | 14 | `A` | A&rarr;G 24 | `R` | 24 | 0.0% | 0-14% | 2,048 | 0.2% | 0-1% | 0.2% |  |
| reverse | 10 | 16 | `T` | T&rarr;A 21 | `W` | 21 | 0.0% | 0-15% | 2,051 | 0.2% | 0-1% | 0.2% |  |
| reverse | 18 | 8 | `G` | G&rarr;A 1,791, G&rarr;T 9, G&rarr;C 8 | `R` (99.1%) | 1,808 | 0.2% | 0-1% | 264 | 0.4% | 0-2% | 0.2% |  |
| reverse | 23 | 3 | `C` | C&rarr;A 2,046, C&rarr;T 16 | `M` (99.2%) | 2,062 | 0.2% | 0-1% | 10 | 0.0% | 0-28% | -0.2% |  |
| reverse | 24 | 2 | `A` | A&rarr;C 1,733, A&rarr;T 313 | `H` | 2,046 | 0.2% | 0-1% | 26 | 0.0% | 0-13% | -0.2% |  |
| reverse | 20 | 6 | `G` | G&rarr;A 1,942, G&rarr;C 7, G&rarr;T 6 | `R` (99.3%) | 1,955 | 0.3% | 0-1% | 117 | 0.0% | 0-3% | -0.3% |  |
| reverse | 15 | 11 | `A` | A&rarr;C 1,645, A&rarr;T 127, A&rarr;G 12 | `H` (99.3%) | 1,784 | 0.3% | 0-1% | 288 | 0.0% | 0-1% | -0.3% |  |
| forward | 14 | 10 | `A` | A&rarr;G 190, A&rarr;T 125, A&rarr;C 6 | `D` (98.1%) | 321 | 0.9% | 0-3% | 1,751 | 0.1% | 0-0% | -0.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 13,15,18,21; rev 15,18,19,20,23,24 | 1,301 | fail | 2023×141, 2024×278, 2025×248, 2026×139 | Betapolyomavirus hominis×738, Human polyomavirus×346, BK polyomavirus×214 | `PX952589`, `PX952588`, `PX952586`, `PX952582`, `PX952581`, `PX952580` (+1,295) |
| fwd 13,15,21; rev 15,18,19,20,23,24 | 236 | fail | 2023×14, 2024×3, 2025×35, 2026×33 | Betapolyomavirus hominis×112, BK polyomavirus×75, Human polyomavirus×46 | `PX952590`, `PX952587`, `PX952585`, `PX952584`, `PX952583`, `PX952503` (+230) |
| fwd 13,15,18,21; rev 18,19,20,23,24 | 98 | fail | 2022×7, 2023×9, 2024×14, 2025×26 | Betapolyomavirus hominis×46, Human polyomavirus×39, BK polyomavirus×13 | `PX257737`, `PX257736`, `PX257735`, `PX257734`, `PX257723`, `PX257722` (+92) |
| fwd 14,15; rev 17,19,21,23,24 | 83 | fail | 2023×17, 2024×21, 2025×1, 2026×2 | Gammapolyomavirus avis×33, Budgerigar fledgling×26, Aves polyomavirus×20 | `PZ157467`, `PZ157466`, `OR004162`, `OR004161`, `OR004160`, `OR004159` (+77) |
| fwd 13,18,21; rev 15,18,19,20,23,24 | 42 | fail | 2011×1, 2013×3, 2016×1, 2024×1 | Simian virus×33, JP×3, MAG×1 | `BK066515`, `NC_001669`, `HZ469834`, `BD102073`, `DI197544`, `HW249739` (+36) |
| fwd 3,13,15; rev 17,19,20,21,23,24 | 29 | fail | 2019×1, 2023×5, 2025×5, 2026×2 | KI polyomavirus×14, Betapolyomavirus tertihominis×11, Sequence×4 | `PZ246330`, `PZ246329`, `OZ373715`, `OZ373041`, `PX473112`, `PX104348` (+23) |
| fwd 3,12,13,14,18; rev 15,16,20,23,24 | 23 | fail | 2016×1, 2023×1, 2024×2, 2026×5 | MW polyomavirus×15, Deltapolyomavirus decihominis×6, Human polyomavirus×1 | `PZ233419`, `PZ233418`, `PZ233417`, `PZ233416`, `PZ233414`, `PQ335163` (+17) |
| fwd 12,14,15,21; rev 15,16,19,20,23,24 | 9 | fail | 2014×2, 2016×1, 2018×3, 2019×1 | Tupaia glis×4, Raccoon polyomavirus×3, Chlorocebus pygerythrus×2 | `NC_040566`, `NC_025898`, `NC_023845`, `MG721017`, `MG721016`, `MG721015` (+3) |

## RETROVIRUS_RNA_polymerase_SIV_Keele_2009

Simian immunodeficiency virus (taxid 11723) — status **declining** — 334 evaluable of 8,252 screened records

- forward: `5'-GARGACCATGAYAAATATCA-3'` (20 nt)
- reverse: `5'-CAATCCCCCCTTTTCTTTTAAAATTGTG-3'` (28 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 24 | 5 | `C` | C&rarr;T 97 | `Y` | 97 | 22.7% | 15-32% | 237 | 98.7% | 96-100% | 76.1% |  |
| reverse | 18 | 11 | `T` | T&rarr;C 96 | `Y` | 96 | 22.9% | 16-32% | 238 | 98.3% | 96-99% | 75.4% |  |
| reverse | 21 | 8 | `C` | C&rarr;T 95, C&rarr;A 1 | `Y` (99.0%) | 96 | 22.9% | 16-32% | 238 | 98.3% | 96-99% | 75.4% |  |
| forward | 6 | 15 | `A` | A&rarr;G 42 | `R` | 42 | 11.9% | 5-25% | 292 | 86.0% | 82-89% | 74.1% |  |
| reverse | 27 | 2 | `A` | A&rarr;T 111, A&rarr;C 2, A&rarr;G 1 | `W` (97.4%) | 114 | 32.5% | 25-42% | 220 | 99.5% | 97-100% | 67.1% |  |
| forward | 7 | 14 | `A` | A&rarr;G 42, A&rarr;T 7 | `D` | 49 | 22.4% | 13-36% | 285 | 86.0% | 81-90% | 63.5% |  |
| forward | 9 | 12 | `Y` | Y&rarr;A 62, Y&rarr;G 17 | hypervariable | 79 | 38.0% | 28-49% | 255 | 88.6% | 84-92% | 50.7% |  |
| reverse | 17 | 12 | `T` | T&rarr;C 53, T&rarr;G 1 | `Y` (98.1%) | 54 | 40.7% | 29-54% | 280 | 83.6% | 79-87% | 42.8% |  |
| forward | 3 | 18 | `T` | T&rarr;C 68 | `Y` | 68 | 42.6% | 32-54% | 266 | 85.3% | 81-89% | 42.7% | yes |
| forward | 15 | 6 | `C` | C&rarr;A 69, C&rarr;T 50, C&rarr;G 22 | hypervariable | 141 | 52.5% | 44-61% | 193 | 94.3% | 90-97% | 41.8% |  |
| reverse | 3 | 26 | `G` | G&rarr;A 28 | `R` | 28 | 42.9% | 27-61% | 306 | 79.7% | 75-84% | 36.9% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 166 | detect | 2007×5, 2017×155, 2019×1, 2022×1 | Simian immunodeficiency×166 | `ON933805`, `AF382822`, `MN315554`, `KY989753`, `KY989752`, `KY989751` (+160) |
| fwd 9,15 | 13 | reduced | 2010×1, 2011×2, 2015×2, 2021×1 | Simian immunodeficiency×11, SIVcpz proviral×2 | `MW815971`, `EF535993`, `HM803689`, `FJ424871`, `FJ424866`, `FJ424865` (+7) |
| fwd 15; rev 17,18,21,24,27 | 12 | reduced | 2014×12 | Simian immunodeficiency×12 | `KJ467498`, `KJ467497`, `KJ467496`, `KJ467495`, `KJ467493`, `KJ467491` (+6) |
| fwd 3,6,15; rev 17,18,21,24,27 | 10 | fail | 2014×10 | Simian immunodeficiency×10 | `KJ467483`, `KJ467481`, `KJ467480`, `KJ467478`, `KJ467477`, `KJ467476` (+4) |
| fwd 3,9,15 | 8 | reduced | 2008×1, 2012×1, 2013×1, 2015×3 | Simian immunodeficiency×8 | `EF535994`, `DQ373064`, `DQ373063`, `KP861923`, `KP004994`, `KP004989` (+2) |
| rev 3 | 8 | detect | 2017×8 | Simian immunodeficiency×8 | `KY989665`, `KY989664`, `KY989662`, `KY989654`, `KY989638`, `KY989624` (+2) |
| fwd 3,15; rev 17,18,21,24,27 | 7 | reduced | 2014×7 | Simian immunodeficiency×7 | `KJ467494`, `KJ467492`, `KJ467485`, `KJ467484`, `KJ467460`, `KJ467454` (+1) |
| fwd 3,9,15; rev 17,18,21,24,27 | 7 | fail | 2014×7 | Simian immunodeficiency×7 | `KJ467482`, `KJ467475`, `KJ467474`, `KJ467473`, `KJ467472`, `KJ467469` (+1) |

## RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009

Simian immunodeficiency virus (taxid 11723) — status **declining** — 5,030 evaluable of 8,252 screened records

- forward: `5'-AYAAYCCHCAAAGTCAAGGAGTRGT-3'` (25 nt)
- reverse: `5'-GTCCTTTCCAAATDGGRTCTCTGCTGTC-3'` (28 nt)

**2,621 of 5,030 evaluable records (52%) share one mismatch pattern, mostly Simian immunodeficiency, deposited 1990-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 4 | 25 | `T` | T&rarr;C 4,826, T&rarr;G 1, T&rarr;A 1 | `Y` (100.0%) | 4,828 | 0.2% | 0-0% | 202 | 100.0% | 98-100% | 99.8% | yes |
| reverse | 3 | 26 | `G` | G&rarr;T 4,798, G&rarr;A 171, G&rarr;C 16 | `K` (96.2%) | 4,985 | 3.4% | 3-4% | 45 | 93.3% | 82-98% | 89.9% | yes |
| reverse | 16 | 13 | `T` | T&rarr;G 4,783, T&rarr;C 197, T&rarr;A 5 | `K` (95.9%) | 4,985 | 3.5% | 3-4% | 45 | 88.9% | 77-95% | 85.4% |  |
| reverse | 14 | 15 | `G` | G&rarr;T 4,772, G&rarr;C 7, G&rarr;A 1 | `K` (99.8%) | 4,780 | 0.0% | 0-0% | 250 | 84.8% | 80-89% | 84.8% |  |
| reverse | 18 | 11 | `A` | A&rarr;C 4,860, A&rarr;G 8, A&rarr;T 4 | `M` (99.8%) | 4,872 | 3.6% | 3-4% | 158 | 24.7% | 19-32% | 21.1% |  |
| forward | 15 | 11 | `A` | A&rarr;G 3,638 | `R` | 3,638 | 0.1% | 0-0% | 1,392 | 15.0% | 13-17% | 14.9% |  |
| reverse | 24 | 5 | `T` | T&rarr;C 2,765 | `Y` | 2,765 | 0.3% | 0-1% | 2,265 | 9.0% | 8-10% | 8.7% |  |
| forward | 12 | 14 | `T` | T&rarr;C 2,022, T&rarr;A 22 | `Y` (98.9%) | 2,044 | 0.1% | 0-0% | 2,986 | 7.1% | 6-8% | 7.0% |  |
| reverse | 15 | 14 | `D` | D&rarr;C 2,024 | hypervariable | 2,024 | 0.2% | 0-1% | 3,006 | 6.9% | 6-8% | 6.7% |  |
| forward | 9 | 17 | `A` | A&rarr;G 2,812, A&rarr;T 3 | `R` (99.9%) | 2,815 | 1.6% | 1-2% | 2,215 | 7.6% | 7-9% | 6.1% |  |
| forward | 14 | 12 | `A` | A&rarr;T 28, A&rarr;G 7 | `D` | 35 | 0.0% | 0-10% | 4,995 | 4.3% | 4-5% | 4.3% |  |
| forward | 5 | 21 | `G` | G&rarr;T 26, G&rarr;A 7 | `D` | 33 | 0.0% | 0-10% | 4,997 | 4.3% | 4-5% | 4.3% | yes |
| reverse | 6 | 23 | `G` | G&rarr;C 18, G&rarr;T 10 | `B` | 28 | 0.0% | 0-12% | 5,002 | 4.3% | 4-5% | 4.3% |  |
| forward | 13 | 13 | `G` | G&rarr;C 27 | `S` | 27 | 0.0% | 0-12% | 5,003 | 4.3% | 4-5% | 4.3% |  |
| reverse | 27 | 2 | `T` | T&rarr;G 29, T&rarr;A 12, T&rarr;C 3 | hypervariable | 44 | 2.3% | 0-12% | 4,986 | 4.3% | 4-5% | 2.0% |  |
| forward | 4 | 22 | `T` | T&rarr;C 33, T&rarr;G 1, T&rarr;A 1 | `B` (97.1%) | 35 | 5.7% | 2-19% | 4,995 | 4.2% | 4-5% | -1.5% | yes |
| forward | 6 | 20 | `A` | A&rarr;G 30, A&rarr;T 7, A&rarr;C 2 | hypervariable | 39 | 15.4% | 7-30% | 4,991 | 4.1% | 4-5% | -11.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 9,15; rev 3,4,14,16,18,24 | 2,621 | fail | 2023×3, 2024×1735, 2025×203, 2026×20 | Simian immunodeficiency×2614, Simian-Chimpanzee immunodeficiency×5, Simian×2 | `PZ775881`, `PZ775880`, `PZ775879`, `PZ775878`, `PZ775877`, `PZ775876` (+2,615) |
| fwd 12; rev 3,4,14,15,16,18 | 1,087 | fail | 2009×640, 2010×447 | Simian immunodeficiency×1087 | `FJ402541`, `FJ402539`, `FJ402538`, `FJ402537`, `FJ402536`, `FJ402534` (+1,081) |
| fwd 12,15; rev 3,4,14,15,16,18 | 828 | fail | 2010×328, 2012×6, 2016×34, 2017×1 | Simian immunodeficiency×828 | `MF370842`, `AY965480`, `KX089855`, `KX089854`, `KX089853`, `KX089852` (+822) |
| rev 3,16,18 | 128 | detect | 1996×1, 2017×126, 2022×1 | Simian immunodeficiency×128 | `ON933805`, `KY989753`, `KY989752`, `KY989751`, `KY989749`, `KY989748` (+122) |
| fwd 9,15; rev 3,4,14,16,24 | 78 | fail | 2019×3, 2024×75 | Simian immunodeficiency×78 | `PP458484`, `PP458483`, `PP458482`, `PP458481`, `PP458480`, `PP458479` (+72) |
| fwd 9; rev 3,16,18 | 42 | reduced | 2017×42 | Simian immunodeficiency×42 | `KY989750`, `KY989745`, `KY989744`, `KY989743`, `KY989739`, `KY989721` (+36) |
| fwd 9,15; rev 3,4,14,16,24,27 | 23 | fail | 2019×23 | Simian immunodeficiency×23 | `MN442954`, `MN442953`, `MN442952`, `MN442951`, `MN442950`, `MN442949` (+17) |
| no mismatches | 16 | detect | 2011×1, 2013×1, 2015×6, 2021×1 | Simian immunodeficiency×16 | `MW815971`, `AF115393`, `FJ424871`, `FJ424866`, `FJ424865`, `FJ424864` (+10) |

## ORTHOBUNYAVIRUS_ssRNA_M_segment_internal_Briese_2007

Orthobunyavirus (taxid 11572) — status **low coverage** — 531 evaluable of 2,083 screened records

- forward: `5'-TGGGGNYGYGARGARTWYGG-3'` (20 nt)
- reverse: `5'-TTKGTYTTTTGKACATTKCC-3'` (20 nt)

**306 of 531 evaluable records (58%) share one mismatch pattern, mostly Oropouche virus, deposited 2015-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 2 | 19 | `C` | C&rarr;T 330, C&rarr;G 6 | `Y` (98.2%) | 336 | 0.0% | 0-1% | 195 | 48.2% | 41-55% | 48.2% | yes |
| reverse | 7 | 14 | `C` | C&rarr;T 376, C&rarr;A 10, C&rarr;G 4 | `Y` (96.4%) | 390 | 6.7% | 5-10% | 141 | 48.2% | 40-56% | 41.6% |  |
| reverse | 14 | 7 | `T` | T&rarr;C 330, T&rarr;A 16, T&rarr;G 6 | `H` (98.3%) | 352 | 4.0% | 2-7% | 179 | 44.7% | 38-52% | 40.7% |  |
| reverse | 16 | 5 | `T` | T&rarr;A 322, T&rarr;C 28, T&rarr;G 13 | `H` (96.4%) | 363 | 5.8% | 4-9% | 168 | 43.5% | 36-51% | 37.7% |  |
| reverse | 12 | 9 | `T` | T&rarr;G 316, T&rarr;C 84, T&rarr;A 1 | `B` (99.8%) | 401 | 9.2% | 7-12% | 130 | 43.8% | 36-52% | 34.6% |  |
| reverse | 10 | 11 | `G` | G&rarr;T 18, G&rarr;A 8, G&rarr;C 7 | hypervariable | 33 | 0.0% | 0-10% | 498 | 18.9% | 16-23% | 18.9% |  |
| forward | 3 | 18 | `Y` | Y&rarr;G 24, Y&rarr;A 7 | hypervariable | 31 | 0.0% | 0-11% | 500 | 18.8% | 16-22% | 18.8% | yes |
| forward | 4 | 17 | `W` | W&rarr;G 22, W&rarr;C 8 | hypervariable | 30 | 0.0% | 0-11% | 501 | 18.8% | 16-22% | 18.8% | yes |
| reverse | 1 | 20 | `C` | C&rarr;T 14, C&rarr;A 13, C&rarr;G 2 | hypervariable | 29 | 0.0% | 0-12% | 502 | 18.7% | 16-22% | 18.7% | yes |
| forward | 17 | 4 | `G` | G&rarr;A 16, G&rarr;T 12 | `D` | 28 | 0.0% | 0-12% | 503 | 18.7% | 16-22% | 18.7% |  |
| reverse | 19 | 2 | `T` | T&rarr;G 16, T&rarr;A 9, T&rarr;C 1 | `D` (96.2%) | 26 | 0.0% | 0-13% | 505 | 18.6% | 15-22% | 18.6% |  |
| forward | 1 | 20 | `G` | G&rarr;A 13, G&rarr;T 11 | `D` | 24 | 0.0% | 0-14% | 507 | 18.5% | 15-22% | 18.5% | yes |
| reverse | 8 | 13 | `A` | A&rarr;C 8, A&rarr;G 7, A&rarr;T 5 | hypervariable | 20 | 0.0% | 0-16% | 511 | 18.4% | 15-22% | 18.4% |  |
| reverse | 3 | 18 | `K` | K&rarr;A 34, K&rarr;C 27 | hypervariable | 61 | 4.9% | 2-13% | 470 | 19.4% | 16-23% | 14.4% | yes |
| reverse | 6 | 15 | `A` | A&rarr;G 24, A&rarr;T 9, A&rarr;C 4 | hypervariable | 37 | 24.3% | 13-40% | 494 | 17.2% | 14-21% | -7.1% |  |
| reverse | 17 | 4 | `G` | G&rarr;A 70, G&rarr;C 20, G&rarr;T 17 | hypervariable | 107 | 29.0% | 21-38% | 424 | 14.9% | 12-19% | -14.1% |  |
| reverse | 13 | 8 | `T` | T&rarr;C 15, T&rarr;G 14, T&rarr;A 6 | hypervariable | 35 | 37.1% | 23-54% | 496 | 16.3% | 13-20% | -20.8% |  |
| reverse | 5 | 16 | `T` | T&rarr;C 24, T&rarr;G 5 | `B` | 29 | 41.4% | 26-59% | 502 | 16.3% | 13-20% | -25.0% | yes |
| reverse | 9 | 12 | `K` | K&rarr;A 49, K&rarr;C 21 | hypervariable | 70 | 42.9% | 32-55% | 461 | 13.9% | 11-17% | -29.0% |  |
| reverse | 18 | 3 | `K` | K&rarr;A 51, K&rarr;C 28 | hypervariable | 79 | 59.5% | 48-70% | 452 | 10.4% | 8-14% | -49.1% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 2,7,12,14,16 | 306 | fail | 2023×13, 2024×17, 2025×90, 2026×177 | Oropouche virus×229, Orthobunyavirus oropoucheense×77 | `PQ754782`, `PQ754779`, `PQ754776`, `PQ754773`, `PQ754770`, `PQ754764` (+300) |
| no mismatches | 21 | detect | 2014×1, 2018×1, 2021×4, 2026×1 | Cache×15, Orthobunyavirus bunyamweraense×4, Bunyamwera virus×1 | `OP137175`, `MW314031`, `MW314028`, `MW314025`, `MW314022`, `MH166878` (+15) |
| rev 7,12,18 | 16 | reduced | 2015×1, 2016×15 | Anadyr virus×16 | `KT313760`, `KT313757`, `KT313754`, `KT313751`, `KT313748`, `KT313745` (+10) |
| rev 3,7,12 | 10 | fail | 2014×1, 2016×9 | Batai virus×10 | `KT313714`, `KT313711`, `KT313708`, `KT313705`, `KT313702`, `KT313699` (+4) |
| fwd 1,8,10,16,17,18; rev 7,8,16,17,19 | 8 | fail | 2025×8 | Snowshoe hare×8 | `OR641864`, `OR641861`, `OR641853`, `OR641850`, `OR641844`, `OR641841` (+2) |
| rev 9,14,16,17,18 | 8 | reduced | 2015×2, 2018×1, 2020×1, 2021×4 | Keystone virus×8 | `MZ156794`, `MZ156791`, `MZ156788`, `MZ156785`, `MT127622`, `MH016785` (+2) |
| rev 6,7,12 | 8 | reduced | 2006×2, 2022×6 | Ngari virus×6, Batai virus×2 | `MT929321`, `MT929318`, `ON755199`, `ON755198`, `ON755197`, `ON755196` (+2) |
| rev 9,18 | 7 | reduced | 2003×4, 2009×2, 2019×1 | Maguari virus×4, Tensaw virus×3 | `NC_043548`, `FJ943508`, `FJ943506`, `AY286446`, `AY286445`, `AY286444` (+1) |

## ORTHOPOXVIRUS_dsDNA_F3L_region_nonMPXV_TaqMan_Huo_2022

Orthopoxvirus (taxid 10242) — status **low coverage** — 13,788 evaluable of 18,308 screened records

- forward: `5'-ATCCTCTCTCATTGATTTTTCGCGGGA-3'` (27 nt)
- reverse: `5'-TGGAGAAGCGAGAAGTTAATAAAGC-3'` (25 nt)
- probe: `5'-TCGTCGGAGCTGTACACCATAGCAC-3'` (25 nt)

**10,593 of 13,788 evaluable records (77%) share one mismatch pattern, mostly Monkeypox virus, deposited 2004-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 14 | 12 | `G` | G&rarr;A 25 | `R` | 25 | 96.0% | 80-99% | 13,763 | 99.7% | 100-100% | 3.7% |  |
| probe | 17 | 9 | `G` | G&rarr;A 2,587, G&rarr;T 15 | `R` (99.4%) | 2,602 | 99.4% | 99-100% | 11,186 | 99.7% | 100-100% | 0.3% |  |
| probe | 3 | 23 | `C` | C&rarr;T 2,582 | `Y` | 2,582 | 99.5% | 99-100% | 11,206 | 99.7% | 100-100% | 0.2% | yes |
| probe | 11 | 15 | `C` | C&rarr;A 10,607, C&rarr;T 1 | `M` (100.0%) | 10,608 | 99.9% | 100-100% | 3,180 | 99.0% | 99-99% | -0.9% |  |
| probe | 21 | 5 | `C` | C&rarr;T 10,607 | `Y` | 10,607 | 99.9% | 100-100% | 3,181 | 99.0% | 99-99% | -0.9% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| prb 11,21 | 10,593 | reduced | 2023×3122, 2024×1528, 2025×1452, 2026×1004 | Monkeypox virus×10055, Orthopoxvirus monkeypox×536, Mutant×2 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+10,587) |
| prb 3,17 | 2,569 | reduced | 2023×3, 2024×500, 2025×686, 2026×1331 | Monkeypox virus×2533, Orthopoxvirus monkeypox×36 | `OZ555904`, `OZ555901`, `OZ555900`, `OZ555899`, `OZ540336`, `OZ540332` (+2,563) |
| no mismatches | 538 | detect | 2023×10, 2024×48, 2025×23, 2026×101 | Cowpox virus×103, Vaccinia virus×101, Variola virus×82 | `LC948760`, `LC948759`, `LC948758`, `LC948757`, `LC948756`, `LC948755` (+532) |
| rev 14 | 24 | detect | 2020×4, 2023×8, 2025×1, 2026×5 | Orthopoxvirus vaccinia×17, Vaccinia virus×4, Buffalopox virus×2 | `PX423484`, `PX423483`, `PX423482`, `PX423481`, `PX423480`, `PV798393` (+18) |
| prb 17 | 16 | detect | 2014×1, 2018×2, 2021×8, 2026×1 | Ectromelia virus×15, Orthopoxvirus akhmetapox×1 | `PX585983`, `NC_004105`, `OU343159`, `OU343158`, `OU343157`, `OU343156` (+10) |
| rev 5; prb 3,17 | 12 | fail | 2024×11, 2025×1 | Monkeypox virus×12 | `OZ254519`, `PQ221720`, `PQ221719`, `PQ221718`, `PQ221717`, `PQ221716` (+6) |
| rev 18; prb 11,21 | 11 | fail | 2015×1, 2025×2, 2026×8 | Monkeypox virus×8, Orthopoxvirus monkeypox×3 | `PX990728`, `PX782070`, `PX782069`, `PV993194`, `PV993193`, `PX122227` (+5) |
| fwd 6 | 5 | detect | 2011×1, 2015×1, 2017×1, 2018×1 | Cowpox virus×5 | `LT993226`, `LT896722`, `LN864566`, `HQ420897`, `DQ437593` |

## POLYOMAVIRUS_dsDNA_PREDICT_VP1_round2

Polyomaviridae (taxid 151341) — status **low coverage** — 6,443 evaluable of 14,537 screened records

- forward: `5'-ATGAAAATGGGGTTGGCCCNCTNTGYAARG-3'` (30 nt)
- reverse: `5'-CCCTCATAAACCCGAACYTCYTCHACYTG-3'` (29 nt)

**2,144 of 6,443 evaluable records (33%) share one mismatch pattern, mostly JC polyomavirus, deposited 1989-2025, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 16 | 14 | `G` | G&rarr;T 6,030, G&rarr;C 1 | `K` (100.0%) | 6,031 | 2.5% | 2-3% | 412 | 89.8% | 87-92% | 87.3% |  |
| forward | 20 | 11 | `G` | G&rarr;T 5,468, G&rarr;A 419, G&rarr;C 27, +1 more | `D` (99.5%) | 5,915 | 1.9% | 2-2% | 528 | 77.5% | 74-81% | 75.6% |  |
| forward | 25 | 6 | `A` | A&rarr;T 3,143, A&rarr;C 2,238, A&rarr;G 1 | `H` (100.0%) | 5,382 | 0.2% | 0-0% | 1,061 | 48.2% | 45-51% | 48.0% |  |
| forward | 14 | 17 | `C` | C&rarr;G 5,473, C&rarr;A 208, C&rarr;T 69 | `S` (95.2%) | 5,750 | 3.0% | 3-3% | 693 | 50.4% | 47-54% | 47.4% |  |
| reverse | 23 | 7 | `T` | T&rarr;A 5,346, T&rarr;C 1 | `W` (100.0%) | 5,347 | 0.1% | 0-0% | 1,096 | 46.8% | 44-50% | 46.7% |  |
| forward | 24 | 7 | `A` | A&rarr;T 3,138, A&rarr;C 3 | `W` (99.9%) | 3,141 | 0.3% | 0-1% | 3,302 | 15.5% | 14-17% | 15.2% |  |
| forward | 23 | 8 | `T` | T&rarr;G 2,227, T&rarr;C 26, T&rarr;A 11 | `K` (98.4%) | 2,264 | 0.3% | 0-1% | 4,179 | 12.3% | 11-13% | 12.0% |  |
| reverse | 4 | 26 | `C` | C&rarr;T 850 | `Y` | 850 | 0.0% | 0-0% | 5,593 | 9.3% | 9-10% | 9.3% | yes |
| forward | 17 | 14 | `T` | T&rarr;G 2,555, T&rarr;A 141, T&rarr;C 11 | `D` (99.6%) | 2,707 | 3.3% | 3-4% | 3,736 | 11.5% | 11-13% | 8.2% |  |
| reverse | 18 | 12 | `C` | C&rarr;T 3,650, C&rarr;A 111, C&rarr;G 20 | `Y` (96.5%) | 3,781 | 5.1% | 4-6% | 2,662 | 12.4% | 11-14% | 7.3% |  |
| reverse | 27 | 3 | `C` | C&rarr;A 2,304, C&rarr;T 141, C&rarr;G 1 | `H` (100.0%) | 2,446 | 3.6% | 3-4% | 3,997 | 10.8% | 10-12% | 7.2% |  |
| reverse | 21 | 9 | `A` | A&rarr;C 2,519, A&rarr;T 322, A&rarr;G 65 | `H` (97.8%) | 2,906 | 5.4% | 5-6% | 3,537 | 10.3% | 9-11% | 4.8% |  |
| forward | 10 | 21 | `C` | C&rarr;T 192, C&rarr;A 4 | `Y` (98.0%) | 196 | 4.1% | 2-8% | 6,247 | 8.2% | 8-9% | 4.1% |  |
| reverse | 24 | 6 | `A` | A&rarr;G 60, A&rarr;C 6, A&rarr;T 2 | `V` (97.1%) | 68 | 4.4% | 2-12% | 6,375 | 8.1% | 7-9% | 3.7% |  |
| reverse | 29 | 1 | `C` | C&rarr;T 48, C&rarr;A 2, C&rarr;G 1 | `H` (98.0%) | 51 | 7.8% | 3-18% | 6,392 | 8.1% | 7-9% | 0.2% |  |
| reverse | 25 | 5 | `C` | C&rarr;G 150, C&rarr;A 3, C&rarr;T 2 | `S` (96.8%) | 155 | 9.7% | 6-15% | 6,288 | 8.0% | 7-9% | -1.6% |  |
| reverse | 19 | 11 | `C` | C&rarr;T 396, C&rarr;A 1 | `Y` (99.7%) | 397 | 11.1% | 8-15% | 6,046 | 7.9% | 7-9% | -3.2% |  |
| reverse | 15 | 15 | `A` | A&rarr;G 938, A&rarr;C 212, A&rarr;T 155 | hypervariable | 1,305 | 13.4% | 12-15% | 5,138 | 6.7% | 6-7% | -6.7% |  |
| forward | 19 | 12 | `G` | G&rarr;A 76 | `R` | 76 | 15.8% | 9-26% | 6,367 | 8.0% | 7-9% | -7.8% |  |
| forward | 26 | 5 | `A` | A&rarr;G 465, A&rarr;C 33, A&rarr;T 1 | `V` (99.8%) | 499 | 23.2% | 20-27% | 5,944 | 6.8% | 6-7% | -16.4% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 14,20,24,25; rev 16,18,23 | 2,144 | fail | 2022×39, 2023×35, 2024×5, 2025×7 | JC polyomavirus×1562, JC virus×524, Betapolyomavirus secuhominis×26 | `PX312157`, `PX312156`, `PX312155`, `PX312154`, `PX312153`, `PH255745` (+2,138) |
| fwd 14,17,20,23,25; rev 16,21,23,27 | 1,320 | fail | 2023×159, 2024×240, 2025×277, 2026×85 | Betapolyomavirus hominis×784, Human polyomavirus×320, BK polyomavirus×210 | `PX952589`, `PX952588`, `PX952586`, `PX952570`, `PX952566`, `PX952564` (+1,314) |
| fwd 14,17,20,23,25; rev 15,16,21,23,27 | 809 | fail | 2023×18, 2024×51, 2025×102, 2026×268 | Betapolyomavirus hominis×460, BK polyomavirus×223, Human polyomavirus×116 | `PX952590`, `PX952587`, `PX952585`, `PX952584`, `PX952583`, `PX952582` (+803) |
| fwd 14,20,24,25; rev 4,16,18,23 | 737 | fail | 2020×8, 2021×14, 2022×1, 2023×2 | JC polyomavirus×441, JC virus×254, Betapolyomavirus secuhominis×30 | `OQ615759`, `OQ615754`, `OP549863`, `MT375554`, `MT375551`, `MT375550` (+731) |
| fwd 17,20,26; rev 16,18,19,21 | 203 | fail | 2019×13, 2021×2, 2023×6, 2026×3 | Merkel cell×198, Alphapolyomavirus quintihominis×5 | `PZ726174`, `PZ726173`, `PZ726172`, `OQ616757`, `ON023016`, `ON023015` (+197) |
| no mismatches | 175 | detect | 2013×3, 2015×3, 2019×167, 2023×1 | Bat polyomavirus×167, Avian polyomavirus×3, Polyomavirus×2 | `OR420733`, `LC426667`, `LC426666`, `LC426665`, `LC426664`, `LC426663` (+169) |
| fwd 14,20,24,25; rev 16,18,21,23 | 156 | fail | 2019×1, 2021×2, 2022×1, 2023×2 | JC virus×116, JC polyomavirus×40 | `OQ615768`, `OQ615767`, `MT448666`, `MW587998`, `MW587997`, `MK728940` (+150) |
| fwd 14; rev 18,21 | 87 | reduced | 2023×11, 2024×21, 2025×1, 2026×2 | Gammapolyomavirus avis×38, Budgerigar fledgling×25, Aves polyomavirus×20 | `PZ157467`, `PZ157466`, `OR004161`, `OR004160`, `OR004159`, `PV506317` (+81) |

## POLYOMAVIRUS_dsDNA_VP1_Johne_2005

Polyomaviridae (taxid 151341) — status **low coverage** — 6,443 evaluable of 14,537 screened records

- forward: `5'-ATGAAAATGGGGTTGGCCCNCTNTGYAARG-3'` (30 nt)
- reverse: `5'-CCCTCATAAACCCGAACYTCYTCHACYTG-3'` (29 nt)

**2,144 of 6,443 evaluable records (33%) share one mismatch pattern, mostly JC polyomavirus, deposited 1989-2025, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 16 | 14 | `G` | G&rarr;T 6,030, G&rarr;C 1 | `K` (100.0%) | 6,031 | 2.5% | 2-3% | 412 | 89.8% | 87-92% | 87.3% |  |
| forward | 20 | 11 | `G` | G&rarr;T 5,468, G&rarr;A 419, G&rarr;C 27, +1 more | `D` (99.5%) | 5,915 | 1.9% | 2-2% | 528 | 77.5% | 74-81% | 75.6% |  |
| forward | 25 | 6 | `A` | A&rarr;T 3,143, A&rarr;C 2,238, A&rarr;G 1 | `H` (100.0%) | 5,382 | 0.2% | 0-0% | 1,061 | 48.2% | 45-51% | 48.0% |  |
| forward | 14 | 17 | `C` | C&rarr;G 5,473, C&rarr;A 208, C&rarr;T 69 | `S` (95.2%) | 5,750 | 3.0% | 3-3% | 693 | 50.4% | 47-54% | 47.4% |  |
| reverse | 23 | 7 | `T` | T&rarr;A 5,346, T&rarr;C 1 | `W` (100.0%) | 5,347 | 0.1% | 0-0% | 1,096 | 46.8% | 44-50% | 46.7% |  |
| forward | 24 | 7 | `A` | A&rarr;T 3,138, A&rarr;C 3 | `W` (99.9%) | 3,141 | 0.3% | 0-1% | 3,302 | 15.5% | 14-17% | 15.2% |  |
| forward | 23 | 8 | `T` | T&rarr;G 2,227, T&rarr;C 26, T&rarr;A 11 | `K` (98.4%) | 2,264 | 0.3% | 0-1% | 4,179 | 12.3% | 11-13% | 12.0% |  |
| reverse | 4 | 26 | `C` | C&rarr;T 850 | `Y` | 850 | 0.0% | 0-0% | 5,593 | 9.3% | 9-10% | 9.3% | yes |
| forward | 17 | 14 | `T` | T&rarr;G 2,555, T&rarr;A 141, T&rarr;C 11 | `D` (99.6%) | 2,707 | 3.3% | 3-4% | 3,736 | 11.5% | 11-13% | 8.2% |  |
| reverse | 18 | 12 | `C` | C&rarr;T 3,650, C&rarr;A 111, C&rarr;G 20 | `Y` (96.5%) | 3,781 | 5.1% | 4-6% | 2,662 | 12.4% | 11-14% | 7.3% |  |
| reverse | 27 | 3 | `C` | C&rarr;A 2,304, C&rarr;T 141, C&rarr;G 1 | `H` (100.0%) | 2,446 | 3.6% | 3-4% | 3,997 | 10.8% | 10-12% | 7.2% |  |
| reverse | 21 | 9 | `A` | A&rarr;C 2,519, A&rarr;T 322, A&rarr;G 65 | `H` (97.8%) | 2,906 | 5.4% | 5-6% | 3,537 | 10.3% | 9-11% | 4.8% |  |
| forward | 10 | 21 | `C` | C&rarr;T 192, C&rarr;A 4 | `Y` (98.0%) | 196 | 4.1% | 2-8% | 6,247 | 8.2% | 8-9% | 4.1% |  |
| reverse | 24 | 6 | `A` | A&rarr;G 60, A&rarr;C 6, A&rarr;T 2 | `V` (97.1%) | 68 | 4.4% | 2-12% | 6,375 | 8.1% | 7-9% | 3.7% |  |
| reverse | 29 | 1 | `C` | C&rarr;T 48, C&rarr;A 2, C&rarr;G 1 | `H` (98.0%) | 51 | 7.8% | 3-18% | 6,392 | 8.1% | 7-9% | 0.2% |  |
| reverse | 25 | 5 | `C` | C&rarr;G 150, C&rarr;A 3, C&rarr;T 2 | `S` (96.8%) | 155 | 9.7% | 6-15% | 6,288 | 8.0% | 7-9% | -1.6% |  |
| reverse | 19 | 11 | `C` | C&rarr;T 396, C&rarr;A 1 | `Y` (99.7%) | 397 | 11.1% | 8-15% | 6,046 | 7.9% | 7-9% | -3.2% |  |
| reverse | 15 | 15 | `A` | A&rarr;G 938, A&rarr;C 212, A&rarr;T 155 | hypervariable | 1,305 | 13.4% | 12-15% | 5,138 | 6.7% | 6-7% | -6.7% |  |
| forward | 19 | 12 | `G` | G&rarr;A 76 | `R` | 76 | 15.8% | 9-26% | 6,367 | 8.0% | 7-9% | -7.8% |  |
| forward | 26 | 5 | `A` | A&rarr;G 465, A&rarr;C 33, A&rarr;T 1 | `V` (99.8%) | 499 | 23.2% | 20-27% | 5,944 | 6.8% | 6-7% | -16.4% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 14,20,24,25; rev 16,18,23 | 2,144 | fail | 2022×39, 2023×35, 2024×5, 2025×7 | JC polyomavirus×1562, JC virus×524, Betapolyomavirus secuhominis×26 | `PX312157`, `PX312156`, `PX312155`, `PX312154`, `PX312153`, `PH255745` (+2,138) |
| fwd 14,17,20,23,25; rev 16,21,23,27 | 1,320 | fail | 2023×159, 2024×240, 2025×277, 2026×85 | Betapolyomavirus hominis×784, Human polyomavirus×320, BK polyomavirus×210 | `PX952589`, `PX952588`, `PX952586`, `PX952570`, `PX952566`, `PX952564` (+1,314) |
| fwd 14,17,20,23,25; rev 15,16,21,23,27 | 809 | fail | 2023×18, 2024×51, 2025×102, 2026×268 | Betapolyomavirus hominis×460, BK polyomavirus×223, Human polyomavirus×116 | `PX952590`, `PX952587`, `PX952585`, `PX952584`, `PX952583`, `PX952582` (+803) |
| fwd 14,20,24,25; rev 4,16,18,23 | 737 | fail | 2020×8, 2021×14, 2022×1, 2023×2 | JC polyomavirus×441, JC virus×254, Betapolyomavirus secuhominis×30 | `OQ615759`, `OQ615754`, `OP549863`, `MT375554`, `MT375551`, `MT375550` (+731) |
| fwd 17,20,26; rev 16,18,19,21 | 203 | fail | 2019×13, 2021×2, 2023×6, 2026×3 | Merkel cell×198, Alphapolyomavirus quintihominis×5 | `PZ726174`, `PZ726173`, `PZ726172`, `OQ616757`, `ON023016`, `ON023015` (+197) |
| no mismatches | 175 | detect | 2013×3, 2015×3, 2019×167, 2023×1 | Bat polyomavirus×167, Avian polyomavirus×3, Polyomavirus×2 | `OR420733`, `LC426667`, `LC426666`, `LC426665`, `LC426664`, `LC426663` (+169) |
| fwd 14,20,24,25; rev 16,18,21,23 | 156 | fail | 2019×1, 2021×2, 2022×1, 2023×2 | JC virus×116, JC polyomavirus×40 | `OQ615768`, `OQ615767`, `MT448666`, `MW587998`, `MW587997`, `MK728940` (+150) |
| fwd 14; rev 18,21 | 87 | reduced | 2023×11, 2024×21, 2025×1, 2026×2 | Gammapolyomavirus avis×38, Budgerigar fledgling×25, Aves polyomavirus×20 | `PZ157467`, `PZ157466`, `OR004161`, `OR004160`, `OR004159`, `PV506317` (+81) |

## POXVIRUSES_dsDNA_Polymerase

Chordopoxvirinae (taxid 10241) — status **low coverage** — 14,583 evaluable of 29,321 screened records

- forward: `5'-ATACAGAGCTAGTACITTAATAAAAG-3'` (26 nt)
- reverse: `5'-CTATTTTTAAATCCCATTAAACC-3'` (23 nt)

**13,731 of 14,583 evaluable records (94%) share one mismatch pattern, mostly Monkeypox virus, deposited 1991-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 5 | 22 | `A` | A&rarr;C 14,003, A&rarr;T 120 | `M` (99.2%) | 14,123 | 0.0% | 0-0% | 460 | 97.2% | 95-98% | 97.2% | yes |
| forward | 8 | 19 | `A` | A&rarr;C 13,836, A&rarr;G 155, A&rarr;T 125 | `M` (98.0%) | 14,116 | 0.0% | 0-0% | 467 | 95.7% | 93-97% | 95.7% |  |
| forward | 17 | 10 | `T` | T&rarr;G 13,825, T&rarr;C 262, T&rarr;A 13 | `K` (98.0%) | 14,100 | 0.0% | 0-0% | 483 | 92.5% | 90-95% | 92.5% |  |
| forward | 10 | 17 | `T` | T&rarr;A 10,511, T&rarr;G 3,332, T&rarr;C 123 | `D` (99.1%) | 13,966 | 0.0% | 0-0% | 617 | 72.4% | 69-76% | 72.4% |  |
| reverse | 17 | 7 | `T` | T&rarr;C 13,969 | `Y` | 13,969 | 0.0% | 0-0% | 614 | 72.1% | 68-76% | 72.1% |  |
| forward | 23 | 4 | `C` | C&rarr;T 14,024 | `Y` | 14,024 | 0.3% | 0-0% | 559 | 71.4% | 67-75% | 71.0% |  |
| reverse | 4 | 20 | `A` | A&rarr;G 13,848 | `R` | 13,848 | 0.0% | 0-0% | 735 | 60.8% | 57-64% | 60.8% | yes |
| forward | 2 | 25 | `A` | A&rarr;G 13,841 | `R` | 13,841 | 0.0% | 0-0% | 742 | 60.2% | 57-64% | 60.2% | yes |
| reverse | 6 | 18 | `T` | T&rarr;C 13,831, T&rarr;A 8, T&rarr;G 2 | `Y` (99.9%) | 13,841 | 0.0% | 0-0% | 742 | 60.2% | 57-64% | 60.2% |  |
| forward | 20 | 7 | `A` | A&rarr;G 271, A&rarr;T 6 | `R` (97.8%) | 277 | 0.0% | 0-1% | 14,306 | 3.1% | 3-3% | 3.1% |  |
| reverse | 18 | 6 | `T` | T&rarr;C 153, T&rarr;A 119, T&rarr;G 2 | `H` (99.3%) | 274 | 0.0% | 0-1% | 14,309 | 3.1% | 3-3% | 3.1% |  |
| reverse | 21 | 3 | `A` | A&rarr;G 255 | `R` | 255 | 0.0% | 0-1% | 14,328 | 3.1% | 3-3% | 3.1% |  |
| forward | 22 | 5 | `A` | A&rarr;C 155 | `M` | 155 | 0.0% | 0-2% | 14,428 | 3.1% | 3-3% | 3.1% |  |
| reverse | 12 | 12 | `T` | T&rarr;A 12, T&rarr;C 8 | `H` | 20 | 0.0% | 0-16% | 14,563 | 3.1% | 3-3% | 3.1% |  |
| reverse | 15 | 9 | `A` | A&rarr;G 71, A&rarr;T 1 | `R` (98.6%) | 72 | 1.4% | 0-7% | 14,511 | 3.1% | 3-3% | 1.7% |  |
| reverse | 3 | 21 | `A` | A&rarr;C 160, A&rarr;T 116, A&rarr;G 2 | `H` (99.3%) | 278 | 1.4% | 1-4% | 14,305 | 3.1% | 3-3% | 1.7% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 2,5,8,10,17,23; rev 4,6,17 | 13,731 | fail | 2023×3118, 2024×2080, 2025×2140, 2026×2622 | Monkeypox virus×12698, Orthopoxvirus monkeypox×651, Vaccinia virus×91 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+13,725) |
| no mismatches | 394 | detect | 2023×64, 2024×34, 2025×95, 2026×93 | Lumpy skin×335, Cetacean poxvirus×17, Goatpox virus×15 | `PZ620426`, `PZ620425`, `PZ620424`, `PZ620423`, `PZ620422`, `PZ620421` (+388) |
| fwd 5,8,17,20,22; rev 3,18,21 | 146 | fail | 2023×1, 2024×14, 2025×11, 2026×4 | Myxoma virus×145, Leporipoxvirus myxoma×1 | `PZ495198`, `PZ376975`, `PZ376974`, `PX512303`, `PX436186`, `PQ241019` (+140) |
| fwd 5,8,10,17,20,23; rev 15,17,18 | 67 | fail | 2022×19, 2023×1, 2025×1, 2026×6 | Fowlpox virus×56, Avipoxvirus sp.×4, Avipoxvirus isolate×2 | `PW014406`, `PX852200`, `OP046362`, `PX666377`, `PX666376`, `PX666373` (+61) |
| fwd 23 | 44 | detect | 2022×3, 2024×11, 2025×3, 2026×5 | Sheeppox virus×39, Goatpox virus×3, Lumpy skin×2 | `PZ614488`, `PZ541183`, `PZ541182`, `PP843160`, `PV167793`, `PV434148` (+38) |
| fwd 2,5,8,10,17,23; rev 3,4,6,17 | 42 | fail | 2019×8, 2022×1, 2025×1, 2026×14 | Cowpox virus×39, KR×1, JP×1 | `LC948760`, `LC948759`, `LC948758`, `LC948757`, `LC948756`, `LC948755` (+36) |
| fwd 5,8,10,17,20,23; rev 17,18,21 | 35 | fail | 2023×1, 2024×1, 2025×2, 2026×1 | Pigeonpox virus×13, Avipoxvirus isolate×8, Avipoxvirus sp.×6 | `PV250209`, `PX219506`, `PQ155435`, `PP341421`, `ON375849`, `NC_036582` (+29) |
| fwd 2,5,8,10,17,23; rev 3,4,6,17,21 | 33 | fail | 2021×2, 2022×3, 2024×12, 2026×1 | Modified×12, Cowpox virus×10, Orthopoxvirus×4 | `PZ351591`, `OQ822801`, `OQ822800`, `OQ822799`, `OQ822798`, `OQ822797` (+27) |

## Snake_nidovirus_PP1b_Uccellini_2014_2

Serpentovirinae (snake nidoviruses, Tobaniviridae) (taxid 2508240) — status **low coverage** — 56 evaluable of 290 screened records

- forward: `5'-GTGACTACACGAAATGCGACC-3'` (21 nt)
- reverse: `5'-ACGTAGTCTTGCCAGTTCCC-3'` (20 nt)

**10 of 56 evaluable records (18%) share one mismatch pattern, mostly Serpentovirinae sp., deposited 2019-2024, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 11 | 11 | `G` | G&rarr;C 28, G&rarr;A 12, G&rarr;T 9 | hypervariable | 49 | 0.0% | 0-7% | 7 | 85.7% | 49-97% | 85.7% |  |
| reverse | 1 | 20 | `C` | C&rarr;T 41, C&rarr;A 8 | `H` | 49 | 0.0% | 0-7% | 7 | 85.7% | 49-97% | 85.7% | yes |
| reverse | 16 | 5 | `A` | A&rarr;T 22, A&rarr;G 14, A&rarr;C 3 | hypervariable | 39 | 0.0% | 0-9% | 17 | 35.3% | 17-59% | 35.3% |  |
| reverse | 19 | 2 | `C` | C&rarr;T 26, C&rarr;G 7, C&rarr;A 5 | hypervariable | 38 | 0.0% | 0-9% | 18 | 33.3% | 16-56% | 33.3% |  |
| reverse | 7 | 14 | `A` | A&rarr;G 32, A&rarr;T 4 | `D` | 36 | 0.0% | 0-10% | 20 | 30.0% | 15-52% | 30.0% |  |
| forward | 14 | 8 | `C` | C&rarr;T 37 | `Y` | 37 | 2.7% | 0-14% | 19 | 26.3% | 12-49% | 23.6% |  |
| forward | 20 | 2 | `T` | T&rarr;C 21, T&rarr;A 2 | `H` | 23 | 0.0% | 0-14% | 33 | 18.2% | 9-34% | 18.2% |  |
| reverse | 4 | 17 | `T` | T&rarr;A 13, T&rarr;G 8 | `D` | 21 | 0.0% | 0-15% | 35 | 17.1% | 8-33% | 17.1% | yes |
| forward | 5 | 17 | `C` | C&rarr;T 28 | `Y` | 28 | 3.6% | 1-18% | 28 | 17.9% | 8-36% | 14.3% | yes |
| forward | 8 | 14 | `A` | A&rarr;G 22 | `R` | 22 | 4.5% | 1-22% | 34 | 14.7% | 6-30% | 10.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 8,11,14,20; rev 1,7,16,19 | 10 | fail | 2019×4, 2020×2, 2023×1, 2024×3 | Serpentovirinae sp.×7, Morelia viridis×3 | `OR131637`, `OR131628`, `OR131620`, `NC_076657`, `MK182569`, `MK182566` (+4) |
| fwd 5,11,14; rev 1,7,16 | 4 | fail | 2019×2, 2024×2 | Serpentovirinae sp.×4 | `OR131648`, `OR131622`, `MN161563`, `MN161560` |
| fwd 8,11,14,17,20; rev 1,4,7,16,19,20 | 3 | fail | 2025×3 | Serpentovirinae sp.×3 | `PV975822`, `PV975821`, `PV975820` |
| fwd 5,11,14,17; rev 1,7,10,16,19 | 3 | fail | 2019×2, 2023×1 | Serpentovirinae sp.×3 | `MN161561`, `NC_076722`, `MN161562` |
| no mismatches | 3 | detect | 2014×3 | Ball python×3 | `NC_024709`, `KM267236`, `KJ541759` |
| fwd 5,11,14,17; rev 1,7,16 | 2 | fail | 2017×2 | Pregotovirus moreliae×1, Morelia viridis×1 | `MF351889`, `NC_035465` |
| fwd 5,8,11; rev 1,4,13,19 | 2 | fail | 2024×2 | Serpentovirinae sp.×2 | `PP898873`, `PP898865` |
| fwd 2,5,11,17; rev 1,4,13,16,19 | 2 | fail | 2024×2 | Serpentovirinae sp.×2 | `PP898869`, `PP898868` |

## ABPV_capsid_Rossi_2024

Aparavirus apisacutum (acute bee paralysis virus; the paper's name, renamed by ICTV) (taxid 3047346) — status **declining** — 122 evaluable of 990 screened records

- forward: `5'-TTTGTTTCAAAYAARATGTTYATGAAAYC-3'` (29 nt)
- reverse: `5'-BTWGAHACAGTCTCTGGACACAT-3'` (23 nt)
- probe: `5'-TATGGTGGAAAYKCTGARAAYAAT-3'` (24 nt)

**16 of 122 evaluable records (13%) share one mismatch pattern, mostly Acute bee, deposited 2021-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 10 | 15 | `T` | T&rarr;C 16, T&rarr;A 11 | `H` | 27 | 59.3% | 41-75% | 95 | 98.9% | 94-100% | 39.7% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 77 | detect | 2019×1, 2021×16, 2022×5, 2023×3 | Acute bee×77 | `OR513774`, `OR513773`, `OR513772`, `OM744314`, `OM744313`, `OM744312` (+71) |
| prb 10 | 16 | reduced | 2022×6, 2024×1, 2025×5, 2026×2 | Acute bee×14, Aparavirus apisacutum×2 | `PX550093`, `PX550092`, `PV664170`, `PV664164`, `PV664128`, `PV664102` (+10) |
| rev 21 | 7 | detect | 2000×2, 2001×3, 2009×2 | Acute bee×5, Sequence×2 | `NC_002548`, `AF263736`, `AF263733`, `AF263724`, `AF150629`, `HB342184` (+1) |
| rev 12; prb 19,22 | 3 | reduced | 2026×3 | Acute bee×3 | `PX663534`, `PX663533`, `PX663532` |
| fwd 2,21; rev 9,15; prb 7,10,16,19 | 3 | fail | 2025×3 | Acute bee×3 | `PV008149`, `PV008147`, `PV008146` |
| fwd 2,3,21; rev 9,12,15; prb 1,10,16,19 | 3 | fail | 2015×3 | Acute bee×3 | `KP025952`, `KP025951`, `KP025950` |
| fwd 2,3,21; rev 9,15; prb 1,7,10,16,19 | 2 | fail | 2023×1, 2025×1 | Acute bee×2 | `PV008148`, `OP628240` |
| rev 12; prb 10,19 | 1 | fail | 2026×1 | Acute bee×1 | `PX726311` |

## INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003

Influenza A virus (taxid 11320) — status **declining** — 89,624 evaluable of 184,766 screened records

- forward: `5'-ARATGAGTCTTCTRACCGAGGTCG-3'` (24 nt)
- reverse: `5'-TGAAAAGACATCYTCAAGYYTCTG-3'` (24 nt)
- probe: `5'-TCAGGCCCCCTCAAAGCCGA-3'` (20 nt)

**27,815 of 89,624 evaluable records (31%) share one mismatch pattern, mostly Influenza, deposited 2017-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 2 | 23 | `C` | C&rarr;T 981, C&rarr;A 121, C&rarr;G 4 | `H` (99.6%) | 1,106 | 0.3% | 0-1% | 88,518 | 98.4% | 98-99% | 98.2% | yes |
| reverse | 3 | 22 | `C` | C&rarr;T 198, C&rarr;A 2 | `Y` (99.0%) | 200 | 0.0% | 0-2% | 89,424 | 97.4% | 97-98% | 97.4% | yes |
| probe | 14 | 7 | `C` | C&rarr;T 63, C&rarr;A 1 | `Y` (98.4%) | 64 | 10.9% | 5-21% | 89,560 | 97.3% | 97-97% | 86.4% |  |
| probe | 6 | 15 | `A` | A&rarr;G 61 | `R` | 61 | 24.6% | 16-37% | 89,563 | 97.3% | 97-97% | 72.7% |  |
| reverse | 21 | 4 | `A` | A&rarr;G 347, A&rarr;C 1 | `R` (99.7%) | 348 | 30.2% | 26-35% | 89,276 | 97.5% | 97-98% | 67.3% |  |
| reverse | 7 | 18 | `G` | G&rarr;A 317, G&rarr;T 198 | `D` | 515 | 34.6% | 31-39% | 89,109 | 97.6% | 97-98% | 63.0% |  |
| reverse | 2 | 23 | `T` | T&rarr;C 26, T&rarr;A 21, T&rarr;G 1 | `H` (97.9%) | 48 | 52.1% | 38-66% | 89,576 | 97.3% | 97-97% | 45.2% | yes |
| probe | 18 | 3 | `A` | A&rarr;G 2,480, A&rarr;C 396, A&rarr;T 53 | `V` (98.2%) | 2,929 | 63.0% | 61-65% | 86,695 | 98.4% | 98-98% | 35.4% |  |
| reverse | 15 | 10 | `A` | A&rarr;G 197, A&rarr;T 112, A&rarr;C 19 | hypervariable | 328 | 62.5% | 57-68% | 89,296 | 97.4% | 97-97% | 34.9% |  |
| forward | 8 | 17 | `C` | C&rarr;T 696, C&rarr;A 450, C&rarr;G 14 | `H` (98.8%) | 1,160 | 76.7% | 74-79% | 88,464 | 97.5% | 97-98% | 20.8% |  |
| forward | 24 | 1 | `A` | A&rarr;G 26, A&rarr;T 26, A&rarr;C 4 | hypervariable | 56 | 78.6% | 66-87% | 89,568 | 97.2% | 97-97% | 18.7% |  |
| forward | 16 | 9 | `C` | C&rarr;T 27, C&rarr;A 2, C&rarr;G 1 | `H` (96.7%) | 30 | 80.0% | 63-90% | 89,594 | 97.2% | 97-97% | 17.2% |  |
| forward | 9 | 16 | `C` | C&rarr;A 32, C&rarr;G 1 | `M` (97.0%) | 33 | 84.8% | 69-93% | 89,591 | 97.2% | 97-97% | 12.4% |  |
| reverse | 18 | 7 | `G` | G&rarr;A 5,941, G&rarr;C 4,893, G&rarr;T 2,396, +3 more | hypervariable | 13,295 | 89.3% | 89-90% | 76,329 | 98.6% | 99-99% | 9.4% |  |
| forward | 13 | 12 | `C` | C&rarr;T 64, C&rarr;G 4 | `B` | 68 | 89.7% | 80-95% | 89,556 | 97.2% | 97-97% | 7.5% |  |
| forward | 14 | 11 | `T` | T&rarr;C 106, T&rarr;A 6, T&rarr;G 1 | `H` (99.1%) | 113 | 92.0% | 86-96% | 89,511 | 97.2% | 97-97% | 5.2% |  |
| reverse | 14 | 11 | `T` | T&rarr;C 30,231, T&rarr;G 7, T&rarr;A 1 | `Y` (100.0%) | 30,239 | 95.4% | 95-96% | 59,385 | 98.2% | 98-98% | 2.7% |  |
| reverse | 9 | 16 | `A` | A&rarr;C 30,856, A&rarr;T 175, A&rarr;G 149 | `M` (99.0%) | 31,180 | 95.5% | 95-96% | 58,444 | 98.2% | 98-98% | 2.7% |  |
| reverse | 23 | 2 | `G` | G&rarr;A 159 | `R` | 159 | 95.0% | 90-97% | 89,465 | 97.2% | 97-97% | 2.3% |  |
| reverse | 16 | 9 | `C` | C&rarr;T 39, C&rarr;G 1, C&rarr;A 1 | `Y` (95.1%) | 41 | 97.6% | 87-100% | 89,583 | 97.2% | 97-97% | -0.3% |  |
| reverse | 13 | 12 | `C` | C&rarr;T 29,290 | `Y` | 29,290 | 97.7% | 98-98% | 60,334 | 97.0% | 97-97% | -0.7% |  |
| forward | 5 | 20 | `G` | G&rarr;A 58, G&rarr;C 1 | `R` (98.3%) | 59 | 98.3% | 91-100% | 89,565 | 97.2% | 97-97% | -1.1% | yes |
| forward | 11 | 14 | `R` | R&rarr;T 28,839, R&rarr;C 26 | `D` (99.9%) | 28,865 | 99.8% | 100-100% | 60,759 | 96.0% | 96-96% | -3.8% |  |
| forward | 17 | 8 | `T` | T&rarr;C 40,754, T&rarr;A 1 | `Y` (100.0%) | 40,755 | 99.7% | 100-100% | 48,869 | 95.2% | 95-95% | -4.5% |  |
| reverse | 24 | 1 | `T` | T&rarr;A 40,178, T&rarr;C 213, T&rarr;G 37, +1 more | `W` (99.4%) | 40,429 | 99.7% | 100-100% | 49,195 | 95.2% | 95-95% | -4.6% |  |
| reverse | 22 | 3 | `A` | A&rarr;C 89,475, A&rarr;T 15 | `M` (100.0%) | 89,490 | 97.3% | 97-97% | 134 | 45.5% | 37-54% | -51.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 11,17; rev 22,24 | 27,815 | reduced | 2023×3996, 2024×3783, 2025×7200, 2026×6783 | Influenza×27815 | `QB100350`, `QB100344`, `QB100335`, `QB100330`, `QB100323`, `QB100309` (+27,809) |
| rev 9,13,14,22 | 27,223 | reduced | 2023×2652, 2024×4089, 2025×5920, 2026×3276 | Influenza×27222, Mutant×1 | `QB092707`, `QB092691`, `QB092683`, `QB092675`, `QB092661`, `QB092654` (+27,217) |
| fwd 17; rev 22,24 | 10,007 | reduced | 2023×36, 2024×578, 2025×907, 2026×839 | Influenza×10007 | `PZ649423`, `PZ649415`, `PZ649407`, `PZ649399`, `PZ649391`, `PZ649383` (+10,001) |
| rev 18,22 | 8,256 | detect | 2023×104, 2024×330, 2025×853, 2026×272 | Influenza×8256 | `QB024908`, `QB024852`, `QB024830`, `QB024664`, `QB024618`, `QB024599` (+8,250) |
| rev 22 | 5,325 | detect | 2023×195, 2024×387, 2025×379, 2026×210 | Influenza×5325 | `QB075457`, `QB075456`, `QB075455`, `QB075454`, `QB025430`, `QB025423` (+5,319) |
| rev 22; prb 18 | 1,397 | reduced | 2023×380, 2024×359, 2025×236, 2026×280 | Influenza×1397 | `QB023248`, `PZ599872`, `PZ599552`, `PZ599528`, `PZ599488`, `PZ599472` (+1,391) |
| fwd 17; rev 18,22 | 866 | reduced | 2023×9, 2024×71, 2025×199, 2026×65 | Influenza×866 | `QB024143`, `QB024032`, `PZ768257`, `PV717827`, `PV717819`, `PV695182` (+860) |
| rev 9,13,14,18,22 | 588 | reduced | 2023×98, 2024×78, 2025×61, 2026×23 | Influenza×588 | `PZ984804`, `PZ933139`, `PZ932338`, `PZ906781`, `PV825774`, `PV720107` (+582) |

## Pan_Plasmodium_sp_and_Haemopro_cytochrome_c

Haemosporida (taxid 5819) — status **declining** — 6,630 evaluable of 32,039 screened records

- forward: `5'-ATGGTGCTTTCGATATATGCATG-3'` (23 nt)
- reverse: `5'-GCATTATCTGGATGTGATAATGGT-3'` (24 nt)

**1,752 of 6,630 evaluable records (26%) share one mismatch pattern, mostly Plasmodium vivax, deposited 1998-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 13 | 11 | `C` | C&rarr;A 6,545, C&rarr;G 2 | `M` (100.0%) | 6,547 | 25.5% | 24-27% | 83 | 98.8% | 93-100% | 73.3% |  |
| forward | 17 | 7 | `C` | C&rarr;T 6,137, C&rarr;A 4 | `Y` (99.9%) | 6,141 | 21.3% | 20-22% | 489 | 90.4% | 87-93% | 69.1% |  |
| reverse | 1 | 24 | `T` | T&rarr;A 1,907, T&rarr;C 12, T&rarr;G 4 | `W` (99.2%) | 1,923 | 0.1% | 0-0% | 4,707 | 37.2% | 36-39% | 37.1% | yes |
| reverse | 4 | 21 | `T` | T&rarr;A 2,394, T&rarr;C 11, T&rarr;G 1 | `W` (99.5%) | 2,406 | 6.1% | 5-7% | 4,224 | 37.9% | 36-39% | 31.8% | yes |
| forward | 8 | 16 | `T` | T&rarr;C 1,741 | `Y` | 1,741 | 5.7% | 5-7% | 4,889 | 33.7% | 32-35% | 28.0% |  |
| forward | 1 | 23 | `G` | G&rarr;T 292, G&rarr;A 2, G&rarr;C 1 | `K` (99.0%) | 295 | 0.0% | 0-1% | 6,335 | 27.6% | 27-29% | 27.6% | yes |
| forward | 5 | 19 | `G` | G&rarr;A 229, G&rarr;T 4 | `R` (98.3%) | 233 | 0.0% | 0-2% | 6,397 | 27.4% | 26-28% | 27.4% | yes |
| forward | 7 | 17 | `A` | A&rarr;T 137, A&rarr;C 46 | `H` | 183 | 0.0% | 0-2% | 6,447 | 27.1% | 26-28% | 27.1% |  |
| forward | 18 | 6 | `G` | G&rarr;C 495, G&rarr;T 1 | `S` (99.8%) | 496 | 1.6% | 1-3% | 6,134 | 28.4% | 27-30% | 26.8% |  |
| forward | 19 | 5 | `T` | T&rarr;G 492, T&rarr;A 1, T&rarr;C 1 | `K` (99.6%) | 494 | 1.6% | 1-3% | 6,136 | 28.4% | 27-30% | 26.8% |  |
| forward | 16 | 8 | `T` | T&rarr;A 49, T&rarr;C 2, T&rarr;G 1 | `H` (98.1%) | 52 | 0.0% | 0-7% | 6,578 | 26.6% | 26-28% | 26.6% |  |
| reverse | 2 | 23 | `G` | G&rarr;A 35, G&rarr;T 6, G&rarr;C 4 | hypervariable | 45 | 0.0% | 0-8% | 6,585 | 26.6% | 26-28% | 26.6% | yes |
| reverse | 14 | 11 | `G` | G&rarr;A 100, G&rarr;T 10 | `D` | 110 | 0.9% | 0-5% | 6,520 | 26.8% | 26-28% | 25.9% |  |
| reverse | 9 | 16 | `G` | G&rarr;C 49, G&rarr;A 22 | `V` | 71 | 1.4% | 0-8% | 6,559 | 26.7% | 26-28% | 25.3% |  |
| reverse | 16 | 9 | `T` | T&rarr;A 2,526, T&rarr;G 6, T&rarr;C 2 | `W` (99.7%) | 2,534 | 10.9% | 10-12% | 4,096 | 36.0% | 35-37% | 25.1% |  |
| forward | 2 | 22 | `T` | T&rarr;C 1,648, T&rarr;A 1 | `Y` (99.9%) | 1,649 | 9.4% | 8-11% | 4,981 | 32.0% | 31-33% | 22.6% | yes |
| reverse | 24 | 1 | `G` | G&rarr;A 30, G&rarr;T 4, G&rarr;C 2 | hypervariable | 36 | 8.3% | 3-22% | 6,594 | 26.5% | 25-28% | 18.2% |  |
| reverse | 8 | 17 | `A` | A&rarr;C 497 | `M` | 497 | 10.7% | 8-14% | 6,133 | 27.7% | 27-29% | 17.0% |  |
| reverse | 10 | 15 | `T` | T&rarr;A 3,362, T&rarr;G 354 | `D` | 3,716 | 22.1% | 21-23% | 2,914 | 31.9% | 30-34% | 9.8% |  |
| reverse | 23 | 2 | `C` | C&rarr;A 157, C&rarr;G 7, C&rarr;T 2 | `V` (98.8%) | 166 | 17.5% | 12-24% | 6,464 | 26.6% | 26-28% | 9.2% |  |
| reverse | 5 | 20 | `A` | A&rarr;G 73, A&rarr;T 1 | `R` (98.6%) | 74 | 23.0% | 15-34% | 6,556 | 26.4% | 25-28% | 3.5% | yes |
| reverse | 13 | 12 | `A` | A&rarr;G 51, A&rarr;T 1 | `R` (98.1%) | 52 | 32.7% | 22-46% | 6,578 | 26.3% | 25-27% | -6.3% |  |
| reverse | 22 | 3 | `A` | A&rarr;G 163, A&rarr;C 2 | `R` (98.8%) | 165 | 50.3% | 43-58% | 6,465 | 25.8% | 25-27% | -24.5% |  |
| forward | 14 | 10 | `T` | T&rarr;C 668, T&rarr;A 1 | `Y` (99.9%) | 669 | 56.5% | 53-60% | 5,961 | 23.0% | 22-24% | -33.5% |  |
| reverse | 19 | 6 | `A` | A&rarr;G 18, A&rarr;C 3 | `V` | 21 | 76.2% | 55-89% | 6,609 | 26.2% | 25-27% | -50.0% |  |
| forward | 23 | 1 | `A` | A&rarr;T 44, A&rarr;G 23, A&rarr;C 10 | hypervariable | 77 | 80.5% | 70-88% | 6,553 | 25.8% | 25-27% | -54.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 13,17; rev 1,10 | 1,752 | fail | 2023×32, 2024×4, 2025×42, 2026×4 | Plasmodium vivax×1054, Plasmodium sp.×274, Plasmodium cf.×116 | `PZ512988`, `PZ512987`, `LC909092`, `LC909091`, `PQ362418`, `PQ362417` (+1,746) |
| fwd 2,8,13,17; rev 4,16 | 1,394 | fail | 2023×17, 2024×1, 2025×19, 2026×4 | Plasmodium falciparum×1328, Plasmodium sp.×52, Plasmodium praefalciparum×13 | `PZ698056`, `PX684229`, `PX684216`, `PX684208`, `PV806003`, `PV806000` (+1,388) |
| fwd 13,14,17; rev 10 | 280 | reduced | 2018×7, 2019×1, 2022×12, 2025×8 | Hepatocystis sp.×280 | `PQ362391`, `PQ362390`, `PQ362389`, `PQ362388`, `PQ362387`, `PQ362386` (+274) |
| fwd 13,17; rev 10 | 257 | reduced | 2022×38, 2023×4, 2024×6, 2025×34 | Plasmodium ovale×71, Plasmodium sp.×60, Plasmodium cathemerium×44 | `PV948057`, `PV948056`, `PV948055`, `PV948054`, `PV806004`, `PV806001` (+251) |
| fwd 13,17 | 250 | detect | 2023×19, 2024×2, 2025×39, 2026×4 | Plasmodium sp.×142, Plasmodium relictum×31, Plasmodium juxtanucleare×18 | `LC909104`, `PV948515`, `PV948494`, `PV085842`, `PV948052`, `PV948051` (+244) |
| fwd 13,17,18,19; rev 4 | 239 | fail | 2015×54, 2016×42, 2017×3, 2025×6 | Plasmodium sp.×159, Plasmodium gaboni×50, Plasmodium adleri×29 | `PV805989`, `PV805985`, `PV805982`, `PV805948`, `PV805946`, `PV805945` (+233) |
| fwd 13,17,18,19; rev 4,10 | 238 | fail | 2016×16, 2017×28, 2022×169, 2025×6 | Plasmodium gaboni×212, Plasmodium sp.×20, Plasmodium billbrayi×6 | `PV805958`, `PV805950`, `PV805949`, `PV805947`, `PV805932`, `PV805931` (+232) |
| fwd 13,17; rev 8,10,16 | 207 | fail | 2023×28, 2024×3, 2025×47, 2026×12 | Haemoproteus sp.×148, Parahaemoproteus sp.×20, Haemoproteus majoris×6 | `LC909103`, `LC909098`, `LC909097`, `LC909096`, `LC909095`, `LC867943` (+201) |

## MONKEYPOX_dsDNA_B1_SNP_nonB1_MGB_Huo_2022

Monkeypox virus (taxid 10244) — status **low coverage** — 12,701 evaluable of 13,757 screened records

- forward: `5'-AGTACACAGACCTCCACCAC-3'` (20 nt)
- reverse: `5'-AGTAATTGACCTACTGGTCTAGGG-3'` (24 nt)
- probe: `5'-AGTCCAAAATCCGCCA-3'` (16 nt)

**9,187 of 12,701 evaluable records (72%) share one mismatch pattern, mostly Monkeypox virus, deposited 2022-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 24 | 1 | `A` | A&rarr;G 2,813, A&rarr;T 1 | `R` (100.0%) | 2,814 | 0.1% | 0-0% | 9,887 | 99.9% | 100-100% | 99.9% |  |
| forward | 5 | 16 | `A` | A&rarr;G 2,814 | `R` | 2,814 | 0.2% | 0-0% | 9,887 | 99.9% | 100-100% | 99.7% | yes |
| probe | 6 | 11 | `C` | C&rarr;T 9,197 | `Y` | 9,197 | 99.9% | 100-100% | 3,504 | 19.8% | 18-21% | -80.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| prb 6 | 9,187 | reduced | 2023×3084, 2024×1379, 2025×713, 2026×753 | Monkeypox virus×9185, Mutant×2 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+9,181) |
| fwd 5; rev 24 | 2,805 | fail | 2023×3, 2024×511, 2025×765, 2026×1479 | Monkeypox virus×2805 | `OZ555904`, `OZ555901`, `OZ555900`, `OZ555899`, `OZ540336`, `OZ540332` (+2,799) |
| no mismatches | 678 | detect | 2023×8, 2024×125, 2025×405, 2026×29 | Monkeypox virus×678 | `OZ531712`, `OZ531711`, `OZ531706`, `OZ531700`, `OZ501870`, `OZ501843` (+672) |
| rev 20 | 7 | detect | 2005×2, 2020×3, 2022×1, 2025×1 | Monkeypox virus×7 | `PV982292`, `OK573020`, `MT903348`, `MT903347`, `MT903346`, `DQ011157` (+1) |
| fwd 5 | 5 | reduced | 2024×3, 2025×2 | Monkeypox virus×5 | `OZ254422`, `OZ254274`, `PQ221653`, `PQ221590`, `PQ221588` |
| fwd 4; prb 6 | 3 | fail | 2026×3 | Monkeypox virus×3 | `OZ501866`, `OZ501842`, `OZ501830` |
| fwd 7; prb 6 | 2 | reduced | 2023×2 | Monkeypox virus×2 | `OQ468954`, `OQ419051` |
| fwd 6 | 2 | detect | 2024×2 | Monkeypox virus×2 | `PP860032`, `PP860028` |

## ORTHOBUNYAVIRUS_ssRNA_L_segment_Briese_2007

Orthobunyavirus (taxid 11572) — status **low coverage** — 158 evaluable of 2,143 screened records

- forward: `5'-AGTAGTGTACTYCTA-3'` (15 nt)
- reverse: `5'-ACCAKGGTGCTGTMARAGTGAARTCWCCAT-3'` (30 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 11 | 5 | `G` | G&rarr;C 40, G&rarr;A 29, G&rarr;T 1 | `V` (98.6%) | 70 | 0.0% | 0-5% | 88 | 60.2% | 50-70% | 60.2% |  |
| forward | 8 | 8 | `T` | T&rarr;A 43, T&rarr;G 23, T&rarr;C 3 | `D` (95.7%) | 69 | 0.0% | 0-5% | 89 | 59.6% | 49-69% | 59.6% |  |
| forward | 6 | 10 | `C` | C&rarr;A 42, C&rarr;G 13, C&rarr;T 3 | hypervariable | 58 | 0.0% | 0-6% | 100 | 53.0% | 43-62% | 53.0% |  |
| forward | 7 | 9 | `A` | A&rarr;T 23, A&rarr;C 23, A&rarr;G 1 | `H` (97.9%) | 47 | 0.0% | 0-8% | 111 | 47.7% | 39-57% | 47.7% |  |
| forward | 13 | 3 | `T` | T&rarr;C 26, T&rarr;A 10, T&rarr;G 2 | hypervariable | 38 | 0.0% | 0-9% | 120 | 44.2% | 36-53% | 44.2% |  |
| forward | 1 | 15 | `A` | A&rarr;T 21, A&rarr;C 8, A&rarr;G 7 | hypervariable | 36 | 0.0% | 0-10% | 122 | 43.4% | 35-52% | 43.4% | yes |
| forward | 12 | 4 | `A` | A&rarr;G 26, A&rarr;T 6, A&rarr;C 2 | hypervariable | 34 | 0.0% | 0-10% | 124 | 42.7% | 34-52% | 42.7% |  |
| forward | 2 | 14 | `T` | T&rarr;C 20, T&rarr;A 8, T&rarr;G 1 | `H` (96.6%) | 29 | 0.0% | 0-12% | 129 | 41.1% | 33-50% | 41.1% | yes |
| forward | 3 | 13 | `C` | C&rarr;T 24, C&rarr;G 3, C&rarr;A 2 | hypervariable | 29 | 0.0% | 0-12% | 129 | 41.1% | 33-50% | 41.1% | yes |
| forward | 5 | 11 | `T` | T&rarr;C 20, T&rarr;A 15 | `H` | 35 | 2.9% | 1-15% | 123 | 42.3% | 34-51% | 39.4% | yes |
| forward | 4 | 12 | `Y` | Y&rarr;A 18, Y&rarr;G 2 | hypervariable | 20 | 0.0% | 0-16% | 138 | 38.4% | 31-47% | 38.4% | yes |
| reverse | 5 | 26 | `W` | W&rarr;G 22, W&rarr;C 10 | hypervariable | 32 | 18.8% | 9-35% | 126 | 37.3% | 29-46% | 18.6% | yes |
| reverse | 26 | 5 | `K` | K&rarr;A 34, K&rarr;C 3 | hypervariable | 37 | 24.3% | 13-40% | 121 | 36.4% | 28-45% | 12.0% |  |
| reverse | 17 | 14 | `M` | M&rarr;T 51, M&rarr;G 3 | hypervariable | 54 | 27.8% | 18-41% | 104 | 36.5% | 28-46% | 8.8% |  |
| reverse | 11 | 20 | `G` | G&rarr;A 53, G&rarr;C 7 | `V` | 60 | 28.3% | 19-41% | 98 | 36.7% | 28-47% | 8.4% |  |
| reverse | 14 | 17 | `A` | A&rarr;T 51, A&rarr;G 32, A&rarr;C 5 | hypervariable | 88 | 36.4% | 27-47% | 70 | 30.0% | 21-42% | -6.4% |  |
| reverse | 20 | 11 | `T` | T&rarr;A 37, T&rarr;C 16 | `H` | 53 | 39.6% | 28-53% | 105 | 30.5% | 22-40% | -9.1% |  |
| reverse | 23 | 8 | `T` | T&rarr;A 15, T&rarr;C 11, T&rarr;G 9 | hypervariable | 35 | 42.9% | 28-59% | 123 | 30.9% | 23-40% | -12.0% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 2,3,4,8,11,15; rev 14,20 | 9 | fail | 2020×9 | La×9 | `MT294293`, `MT294292`, `MT294291`, `MT294290`, `MT294286`, `MT294285` (+3) |
| rev 14,15,23 | 9 | reduced | 2017×9 | Wolkberg virus×9 | `NC_034633`, `KX470581`, `KX470578`, `KX470569`, `KX470566`, `KX470563` (+3) |
| no mismatches | 9 | detect | 1991×1, 1994×1, 2011×6, 2014×1 | La×7, Bunyamwera virus×1, Batai virus×1 | `NC_001925`, `KJ187038`, `GU206125`, `GU206128`, `GU206134`, `GU206137` (+3) |
| fwd 6,7,8,11,13; rev 26 | 8 | fail | 2016×8 | Anadyr virus×8 | `KT313759`, `KT313756`, `KT313753`, `KT313750`, `KT313747`, `KT313744` (+2) |
| fwd 6,7,8,11,13; rev 2,26 | 7 | fail | 2016×7 | Anadyr virus×7 | `KT313741`, `KT313738`, `KT313735`, `KT313726`, `KT313723`, `KT313720` (+1) |
| fwd 3,6,7,8,11,13; rev 5,14,17,26 | 6 | fail | 2016×6 | Batai virus×6 | `KT313713`, `KT313710`, `KT313707`, `KT313704`, `KT313701`, `KT313698` |
| rev 14,20 | 5 | detect | 2011×5 | La×5 | `GU206131`, `GU206122`, `GU206119`, `GU206113`, `GU206110` |
| fwd 1,6,7,8,11,12 | 4 | fail | 2024×4 | Orthobunyavirus bunyamweraense×4 | `OQ790102`, `OQ790095`, `OQ790094`, `OQ790089` |

## ARENAVIRUS_ssRNA_S_gene

Arenaviridae (taxid 11617) — status **low coverage** — 740 evaluable of 6,454 screened records

- forward: `5'-GGCATWGANCCAAACTGATT-3'` (20 nt)
- reverse: `5'-CGCACCGGGGATCCTAGGC-3'` (19 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 3 | 18 | `A` | A&rarr;G 168, A&rarr;T 9, A&rarr;C 2 | `D` (98.9%) | 179 | 5.0% | 3-9% | 561 | 75.6% | 72-79% | 70.6% | yes |
| reverse | 1 | 19 | `C` | C&rarr;T 45, C&rarr;G 25 | `B` | 70 | 0.0% | 0-5% | 670 | 64.6% | 61-68% | 64.6% | yes |
| reverse | 5 | 15 | `T` | T&rarr;G 45, T&rarr;C 23 | `B` | 68 | 0.0% | 0-5% | 672 | 64.4% | 61-68% | 64.4% | yes |
| reverse | 2 | 18 | `G` | G&rarr;T 46 | `K` | 46 | 0.0% | 0-8% | 694 | 62.4% | 59-66% | 62.4% | yes |
| forward | 5 | 16 | `T` | T&rarr;A 41, T&rarr;G 4 | `D` | 45 | 0.0% | 0-8% | 695 | 62.3% | 59-66% | 62.3% | yes |
| forward | 1 | 20 | `T` | T&rarr;A 33, T&rarr;C 4, T&rarr;G 1 | `H` (97.4%) | 38 | 0.0% | 0-9% | 702 | 61.7% | 58-65% | 61.7% | yes |
| forward | 7 | 14 | `A` | A&rarr;T 34, A&rarr;C 2 | `H` | 36 | 0.0% | 0-10% | 704 | 61.5% | 58-65% | 61.5% |  |
| reverse | 7 | 13 | `C` | C&rarr;T 22, C&rarr;G 3 | `B` | 25 | 0.0% | 0-13% | 715 | 60.6% | 57-64% | 60.6% |  |
| forward | 17 | 4 | `A` | A&rarr;G 48, A&rarr;T 1 | `R` (98.0%) | 49 | 2.0% | 0-11% | 691 | 62.5% | 59-66% | 60.5% |  |
| reverse | 18 | 2 | `G` | G&rarr;C 13, G&rarr;T 6, G&rarr;A 4 | hypervariable | 23 | 13.0% | 5-32% | 717 | 60.0% | 56-63% | 46.9% |  |
| reverse | 19 | 1 | `C` | C&rarr;T 27, C&rarr;A 10, C&rarr;G 9, +1 more | hypervariable | 47 | 31.9% | 20-46% | 693 | 60.3% | 57-64% | 28.4% |  |
| forward | 19 | 2 | `G` | G&rarr;T 115, G&rarr;A 22, G&rarr;C 12 | hypervariable | 149 | 38.9% | 31-47% | 591 | 63.5% | 59-67% | 24.5% |  |
| forward | 6 | 15 | `C` | C&rarr;T 249, C&rarr;G 9, C&rarr;A 3 | `Y` (95.4%) | 261 | 44.8% | 39-51% | 479 | 66.0% | 62-70% | 21.1% |  |
| forward | 18 | 3 | `C` | C&rarr;A 65, C&rarr;T 58, C&rarr;G 30 | hypervariable | 153 | 44.4% | 37-52% | 587 | 62.2% | 58-66% | 17.7% |  |
| forward | 16 | 5 | `T` | T&rarr;C 73, T&rarr;A 46, T&rarr;G 7 | hypervariable | 126 | 45.2% | 37-54% | 614 | 61.2% | 57-65% | 16.0% |  |
| forward | 11 | 10 | `C` | C&rarr;T 95, C&rarr;G 16, C&rarr;A 5 | `B` (95.7%) | 116 | 50.0% | 41-59% | 624 | 60.1% | 56-64% | 10.1% |  |
| forward | 8 | 13 | `A` | A&rarr;T 89, A&rarr;C 10, A&rarr;G 10 | hypervariable | 109 | 51.4% | 42-61% | 631 | 59.7% | 56-64% | 8.4% |  |
| forward | 20 | 1 | `G` | G&rarr;C 85, G&rarr;A 15, G&rarr;T 6 | hypervariable | 106 | 52.8% | 43-62% | 634 | 59.5% | 56-63% | 6.6% |  |
| forward | 9 | 12 | `A` | A&rarr;G 168, A&rarr;C 16 | `V` | 184 | 54.3% | 47-61% | 556 | 59.9% | 56-64% | 5.5% |  |
| forward | 13 | 8 | `A` | A&rarr;T 396, A&rarr;C 90, A&rarr;G 3 | `H` (99.4%) | 489 | 56.9% | 52-61% | 251 | 61.8% | 56-68% | 4.9% |  |
| reverse | 12 | 8 | `G` | G&rarr;T 448, G&rarr;A 142, G&rarr;C 1, +1 more | `D` (99.7%) | 592 | 57.9% | 54-62% | 148 | 60.8% | 53-68% | 2.9% |  |
| forward | 15 | 6 | `W` | W&rarr;G 170, W&rarr;C 28 | hypervariable | 198 | 67.2% | 60-73% | 542 | 55.4% | 51-59% | -11.8% |  |
| reverse | 14 | 6 | `C` | C&rarr;A 530, C&rarr;G 21, C&rarr;T 6, +1 more | `M` (95.0%) | 558 | 63.8% | 60-68% | 182 | 42.3% | 35-50% | -21.5% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 9,13,15; rev 12,14 | 71 | reduced | 2019×3, 2022×5, 2023×6, 2024×3 | Lassa virus×39, Mammarenavirus lassaense×18, Mopeia×11 | `PQ421571`, `PP826288`, `PP826286`, `OM791222`, `OM735988`, `OM735972` (+65) |
| fwd 8,11,13,19,20 | 54 | reduced | 2021×3, 2022×3, 2023×10, 2026×1 | Mammarenavirus lassaense×20, Lassa virus×20, Mopeia×9 | `PX115302`, `MT085097`, `OM791228`, `OM735974`, `OR041684`, `OR041681` (+48) |
| fwd 6,13; rev 12,14 | 51 | reduced | 2023×1, 2024×2, 2025×3, 2026×9 | JP×22, Lymphocytic choriomeningitis×11, Sequence×9 | `QS268543`, `QS268539`, `QS268538`, `QQ887355`, `QQ887351`, `QQ887350` (+45) |
| fwd 16,18; rev 12,14 | 41 | reduced | 2018×3, 2019×1, 2021×2, 2022×1 | Junin virus×28, Mammarenavirus juninense×3, JP×3 | `MZ772913`, `MW227339`, `MW227337`, `MP167664`, `MA420650`, `MA401990` (+35) |
| fwd 6,13,16,17,18; rev 1,2,5,12,14 | 28 | fail | 2015×19, 2017×1, 2018×6, 2022×2 | Unidentified×17, University of×9, S5-like reptarenavirus×2 | `KR870015`, `KR870012`, `OM456554`, `MW091471`, `MH483094`, `MH483083` (+22) |
| fwd 6; rev 12,14 | 27 | reduced | 2017×3, 2018×2, 2024×1, 2026×1 | Pichinde virus×9, Mammarenavirus guanaritoense×3, Machupo virus×2 | `OR844394`, `NC_006447`, `LY512442`, `LZ985362`, `KU746276`, `KU746277` (+21) |
| fwd 15; rev 12,14 | 25 | reduced | 2017×4, 2020×1, 2024×1, 2026×1 | Machupo virus×12, Mammarenavirus machupoense×6, Flexal virus×3 | `PV088375`, `PP967232`, `MT015970`, `NC_010756`, `NC_010757`, `NC_005078` (+19) |
| fwd 13; rev 12,14 | 24 | reduced | 2015×2, 2019×2, 2022×6, 2023×2 | Mammarenavirus lassaense×6, Lassa virus×3, Lymphocytic choriomeningitis×3 | `OM791226`, `OM735984`, `OM735980`, `OM735968`, `AB627952`, `OP775657` (+18) |

## MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004

Monkeypox virus (taxid 10244) — status **declining** — 9,991 evaluable of 13,757 screened records

- forward: `5'-AACAACCGTCCTACAATTAAACAACA-3'` (26 nt)
- reverse: `5'-CGCTATCGAACCATTTTTGTAGTCT-3'` (25 nt)
- probe: `5'-TATAACGGCGAAGAATATACT-3'` (21 nt)

**8,806 of 9,991 evaluable records (88%) share one mismatch pattern, mostly Monkeypox virus, deposited 2015-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 10 | 12 | `A` | A&rarr;C 8,810 | `M` | 8,810 | 100.0% | 100-100% | 1,181 | 99.4% | 99-100% | -0.6% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| prb 10 | 8,806 | reduced | 2023×2600, 2024×1359, 2025×859, 2026×756 | Monkeypox virus×8804, Mutant×2 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+8,800) |
| no mismatches | 1,179 | detect | 2023×2, 2024×486, 2025×277, 2026×339 | Monkeypox virus×1179 | `OZ555904`, `OZ555901`, `OZ555900`, `OZ555899`, `OZ540336`, `OZ540332` (+1,173) |
| fwd 19; rev 2,14,15,19,23,25; prb 9,12,14,15 | 2 | fail | 2010×2 | Modified×2 | `FV537352`, `FV537351` |
| rev 23,24; prb 10 | 1 | reduced | 2024×1 | Monkeypox virus×1 | `PP778666` |
| prb 10,12 | 1 | fail | 2023×1 | Monkeypox virus×1 | `OQ320439` |
| rev 18; prb 10 | 1 | reduced | 2023×1 | Monkeypox virus×1 | `OQ261696` |
| prb 2,3,10 | 1 | fail | 2022×1 | Monkeypox virus×1 | `OP536776` |

## Snake_nidovirus_PP1b_Uccellini_2014_3

Serpentovirinae (snake nidoviruses, Tobaniviridae) (taxid 2508240) — status **low coverage** — 44 evaluable of 290 screened records

- forward: `5'-ACCTGCTACCGATGTCCAAG-3'` (20 nt)
- reverse: `5'-GTCGTTGTTGGCTGAGTGTG-3'` (20 nt)

**5 of 44 evaluable records (11%) share one mismatch pattern, mostly Serpentovirinae sp., deposited 2019-2024, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 18 | 3 | `C` | C&rarr;A 19, C&rarr;G 3, C&rarr;T 3 | hypervariable | 25 | 0.0% | 0-13% | 19 | 63.2% | 41-81% | 63.2% |  |
| reverse | 8 | 13 | `T` | T&rarr;G 19, T&rarr;A 6 | `D` | 25 | 0.0% | 0-13% | 19 | 63.2% | 41-81% | 63.2% |  |
| reverse | 2 | 19 | `T` | T&rarr;G 19, T&rarr;A 3, T&rarr;C 2 | hypervariable | 24 | 0.0% | 0-14% | 20 | 60.0% | 39-78% | 60.0% | yes |
| reverse | 6 | 15 | `A` | A&rarr;T 19, A&rarr;C 2, A&rarr;G 1 | `H` (95.5%) | 22 | 0.0% | 0-15% | 22 | 54.5% | 35-73% | 54.5% |  |
| reverse | 11 | 10 | `G` | G&rarr;A 18, G&rarr;T 6, G&rarr;C 6 | hypervariable | 30 | 23.3% | 12-41% | 14 | 35.7% | 16-61% | 12.4% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 5 | detect | 2014×2, 2018×1, 2019×1, 2026×1 | Ball python×4, Serpentovirinae sp.×1 | `PZ137011`, `MN161571`, `NC_024709`, `MG752895`, `KJ541759` |
| fwd 11,12,18; rev 2,5,6,7,8,11 | 5 | fail | 2019×3, 2024×2 | Serpentovirinae sp.×5 | `OR131628`, `OR131602`, `MN161570`, `MN161569`, `MN161568` |
| rev 11 | 4 | detect | 2017×2, 2019×2 | Serpentovirinae sp.×2, Pregotovirus moreliae×1, Morelia viridis×1 | `MF351889`, `MN161563`, `MN161558`, `NC_035465` |
| fwd 2,6,9,18; rev 2,8,11,16 | 3 | fail | 2025×3 | Serpentovirinae sp.×3 | `PV975822`, `PV975821`, `PV975820` |
| fwd 11,18,19; rev 2,5,6,7,8,11 | 3 | fail | 2020×2, 2023×1 | Morelia viridis×3 | `NC_076657`, `MK182569`, `MK182566` |
| rev 11,20 | 2 | detect | 2024×2 | Serpentovirinae sp.×2 | `OR131648`, `OR131622` |
| fwd 2,18; rev 2,6,7,8 | 2 | fail | 2019×1, 2024×1 | Serpentovirinae sp.×2 | `OR131641`, `MN161559` |
| fwd 3,9,11,15,18; rev 3,4,5,9,11,18 | 2 | fail | 2019×1, 2023×1 | Serpentovirinae sp.×2 | `MN161561`, `NC_076722` |

## ENTEROVIRUS_ssRNA_VP3_VP1_round2

Enterovirus (taxid 12059) — status **declining** — 24,161 evaluable of 73,270 screened records

- forward: `5'-CCAGCACTGACAGCAGYNGARAYNGG-3'` (26 nt)
- reverse: `5'-TACTGGACCACCTGGNGGNAYRWACAT-3'` (27 nt)

**2,813 of 24,161 evaluable records (12%) share one mismatch pattern, mostly Coxsackievirus, deposited 2004-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 26 | 2 | `A` | A&rarr;T 10,078, A&rarr;G 1,061, A&rarr;C 447 | `D` (96.1%) | 11,586 | 0.5% | 0-1% | 12,575 | 41.9% | 41-43% | 41.5% |  |
| forward | 16 | 11 | `C` | C&rarr;A 10,786, C&rarr;G 59, C&rarr;T 1 | `M` (99.4%) | 10,846 | 0.1% | 0-0% | 13,315 | 40.0% | 39-41% | 39.9% |  |
| forward | 17 | 10 | `A` | A&rarr;C 10,154, A&rarr;G 667, A&rarr;T 31 | `V` (99.7%) | 10,852 | 0.2% | 0-0% | 13,309 | 39.9% | 39-41% | 39.7% |  |
| reverse | 25 | 3 | `C` | C&rarr;T 16,583, C&rarr;G 534, C&rarr;A 97 | `Y` (96.3%) | 17,214 | 10.7% | 10-11% | 6,947 | 50.3% | 49-51% | 39.6% |  |
| reverse | 24 | 4 | `T` | T&rarr;C 7,884, T&rarr;G 4,900, T&rarr;A 3,213, +1 more | hypervariable | 15,998 | 8.7% | 8-9% | 8,163 | 48.3% | 47-49% | 39.6% |  |
| reverse | 20 | 8 | `C` | C&rarr;G 14,402, C&rarr;A 30 | `S` (99.8%) | 14,432 | 6.3% | 6-7% | 9,729 | 45.5% | 45-46% | 39.2% |  |
| reverse | 18 | 10 | `A` | A&rarr;C 9,368, A&rarr;T 4,853, A&rarr;G 2,373 | hypervariable | 16,594 | 12.5% | 12-13% | 7,567 | 42.9% | 42-44% | 30.4% |  |
| forward | 18 | 9 | `G` | G&rarr;A 9,080, G&rarr;C 6,167, G&rarr;T 2,209 | hypervariable | 17,456 | 15.5% | 15-16% | 6,705 | 39.1% | 38-40% | 23.5% |  |
| reverse | 19 | 9 | `C` | C&rarr;T 33, C&rarr;A 6, C&rarr;G 1 | `H` (97.5%) | 40 | 0.0% | 0-9% | 24,121 | 22.1% | 22-23% | 22.1% |  |
| forward | 25 | 2 | `C` | C&rarr;A 23, C&rarr;T 2, C&rarr;G 1 | `H` (96.2%) | 26 | 0.0% | 0-13% | 24,135 | 22.1% | 22-23% | 22.1% |  |
| reverse | 7 | 21 | `Y` | Y&rarr;A 99, Y&rarr;G 8 | hypervariable | 107 | 0.9% | 0-5% | 24,054 | 22.2% | 22-23% | 21.2% |  |
| forward | 23 | 4 | `G` | G&rarr;A 337, G&rarr;T 19, G&rarr;C 1 | `D` (99.7%) | 357 | 1.7% | 1-4% | 23,804 | 22.4% | 22-23% | 20.7% |  |
| forward | 12 | 15 | `A` | A&rarr;T 7,015, A&rarr;C 6,527, A&rarr;G 2,669, +1 more | hypervariable | 16,212 | 15.4% | 15-16% | 7,949 | 35.7% | 35-37% | 20.4% |  |
| reverse | 23 | 5 | `G` | G&rarr;A 18, G&rarr;C 15, G&rarr;T 15 | hypervariable | 48 | 2.1% | 0-11% | 24,113 | 22.1% | 22-23% | 20.0% |  |
| forward | 22 | 5 | `C` | C&rarr;T 214, C&rarr;A 62, C&rarr;G 1 | `H` (99.6%) | 277 | 2.9% | 1-6% | 23,884 | 22.3% | 22-23% | 19.4% |  |
| forward | 26 | 1 | `C` | C&rarr;A 54, C&rarr;T 15 | `H` | 69 | 2.9% | 1-10% | 24,092 | 22.1% | 22-23% | 19.2% |  |
| forward | 5 | 22 | `A` | A&rarr;G 19, A&rarr;C 2, A&rarr;T 2 | hypervariable | 23 | 4.3% | 1-21% | 24,138 | 22.1% | 22-23% | 17.7% | yes |
| forward | 11 | 16 | `G` | G&rarr;A 103, G&rarr;C 6, G&rarr;T 2 | `V` (98.2%) | 111 | 6.3% | 3-12% | 24,050 | 22.1% | 22-23% | 15.8% |  |
| forward | 10 | 17 | `Y` | Y&rarr;A 52, Y&rarr;G 39 | hypervariable | 91 | 7.7% | 4-15% | 24,070 | 22.1% | 22-23% | 14.4% |  |
| reverse | 21 | 7 | `A` | A&rarr;G 7,049, A&rarr;T 3,384, A&rarr;C 1,159 | hypervariable | 11,592 | 17.0% | 16-18% | 12,569 | 26.7% | 26-28% | 9.8% |  |
| forward | 21 | 6 | `A` | A&rarr;G 4,792, A&rarr;T 2,435, A&rarr;C 2,261 | hypervariable | 9,488 | 17.8% | 17-19% | 14,673 | 24.8% | 24-26% | 7.1% |  |
| forward | 24 | 3 | `A` | A&rarr;T 3,947, A&rarr;G 2,155, A&rarr;C 2,049, +1 more | hypervariable | 8,152 | 18.2% | 17-19% | 16,009 | 24.0% | 23-25% | 5.8% |  |
| reverse | 22 | 6 | `G` | G&rarr;C 446, G&rarr;A 97, G&rarr;T 53 | hypervariable | 596 | 17.3% | 14-21% | 23,565 | 22.2% | 22-23% | 4.9% |  |
| forward | 20 | 7 | `C` | C&rarr;T 5,965, C&rarr;G 10, C&rarr;A 9 | `Y` (99.7%) | 5,984 | 22.0% | 21-23% | 18,177 | 22.1% | 21-23% | 0.0% |  |
| reverse | 15 | 13 | `T` | T&rarr;A 4,344, T&rarr;G 2,597, T&rarr;C 1,724 | hypervariable | 8,665 | 23.8% | 23-25% | 15,496 | 21.1% | 20-22% | -2.7% |  |
| forward | 15 | 12 | `A` | A&rarr;T 4,397, A&rarr;C 2,907, A&rarr;G 2,678 | hypervariable | 9,982 | 34.7% | 34-36% | 14,179 | 13.1% | 13-14% | -21.6% |  |
| reverse | 27 | 1 | `T` | T&rarr;C 5,360, T&rarr;G 3,359, T&rarr;A 2,082 | hypervariable | 10,801 | 34.4% | 34-35% | 13,360 | 12.1% | 12-13% | -22.4% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 12,16,17,18; rev 18,20,24,25,26 | 2,813 | fail | 2023×103, 2024×17, 2025×117, 2026×205 | Coxsackievirus×2509, Human coxsackievirus×270, Enterovirus×34 | `PV472738`, `PV472736`, `PV472735`, `PV472734`, `PV472732`, `PV472725` (+2,807) |
| fwd 12,16,17,18,21; rev 15,20,24,25,26 | 1,336 | fail | 2023×51, 2024×12, 2025×13, 2026×1 | Enterovirus×966, Human enterovirus×369, Recombinant×1 | `PV872005`, `PV176308`, `PQ868600`, `PQ868598`, `PQ868597`, `PQ868596` (+1,330) |
| fwd 15,18,24; rev 18,20,21,24,25,26 | 800 | fail | 2023×361, 2024×13, 2025×2, 2026×6 | Poliovirus×477, Human poliovirus×300, Human enterovirus×9 | `PZ134350`, `PQ861973`, `PQ861972`, `PQ861971`, `PQ861970`, `PQ861969` (+794) |
| fwd 15,18,24; rev 18,20,27 | 657 | reduced | 2023×155, 2024×61, 2025×12, 2026×28 | Poliovirus×327, Human poliovirus×295, Enterovirus×32 | `PX841384`, `PX460079`, `PX458843`, `PX436184`, `PX436183`, `PX436182` (+651) |
| fwd 12,16,17,18; rev 18,20,21,24,25,26 | 654 | fail | 2023×87, 2024×35, 2025×149, 2026×62 | Coxsackievirus×635, Enterovirus×14, Human coxsackievirus×5 | `PV472742`, `PV472741`, `PV472737`, `PV472707`, `PV472675`, `PV472671` (+648) |
| fwd 12,15; rev 15,25,27 | 634 | reduced | 2023×92, 2024×144, 2025×160, 2026×100 | Echovirus×610, Enterovirus×19, Echovirus isolate×5 | `PZ445305`, `PZ445304`, `PZ445303`, `PX841407`, `PX841406`, `PX841405` (+628) |
| fwd 12,15,20; rev 15,25,27 | 464 | reduced | 2023×48, 2024×45, 2025×1, 2026×1 | Echovirus×439, Human echovirus×22, Enterovirus×3 | `PX841401`, `PV637433`, `PP534811`, `PP534710`, `PP534708`, `PP534705` (+458) |
| fwd 15,18,21,24; rev 18,20,21,27 | 424 | fail | 2013×164, 2014×183, 2016×4, 2024×2 | Human poliovirus×417, Poliovirus×6, Human coxsackievirus×1 | `PQ159226`, `PQ159222`, `EU046227`, `EU046226`, `EU046225`, `EU046224` (+418) |

## Pan_coccidia_SSU_rDNA_negative_contro_Garner_2006

Apicomplexa (taxid 5794) — status **low coverage** — 4,473 evaluable of 56,412 screened records

- forward: `5'-ACYATAAACTATGCCRACTAGA-3'` (22 nt)
- reverse: `5'-CYTCCYTRCRTTARACACGCAA-3'` (22 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 1 | 22 | `A` | A&rarr;G 134, A&rarr;T 48, A&rarr;C 11 | hypervariable | 193 | 0.0% | 0-2% | 4,280 | 97.7% | 97-98% | 97.7% | yes |
| reverse | 1 | 22 | `A` | A&rarr;T 32, A&rarr;C 23, A&rarr;G 16 | hypervariable | 71 | 0.0% | 0-5% | 4,402 | 95.0% | 94-96% | 95.0% | yes |
| forward | 2 | 21 | `G` | G&rarr;A 107, G&rarr;C 25, G&rarr;T 6 | `V` (95.7%) | 138 | 2.9% | 1-7% | 4,335 | 96.3% | 96-97% | 93.4% | yes |
| forward | 3 | 20 | `A` | A&rarr;G 82, A&rarr;T 19, A&rarr;C 9 | hypervariable | 110 | 5.5% | 3-11% | 4,363 | 95.7% | 95-96% | 90.2% | yes |
| forward | 4 | 19 | `T` | T&rarr;C 36, T&rarr;A 8, T&rarr;G 2 | `H` (95.7%) | 46 | 4.3% | 1-15% | 4,427 | 94.4% | 94-95% | 90.0% | yes |
| reverse | 13 | 10 | `R` | R&rarr;C 17, R&rarr;T 7 | hypervariable | 24 | 4.2% | 1-20% | 4,449 | 93.9% | 93-95% | 89.8% |  |
| reverse | 6 | 17 | `A` | A&rarr;T 79, A&rarr;G 37, A&rarr;C 9 | hypervariable | 125 | 9.6% | 6-16% | 4,348 | 95.9% | 95-96% | 86.3% |  |
| forward | 6 | 17 | `A` | A&rarr;T 22, A&rarr;G 1, A&rarr;C 1 | `D` (95.8%) | 24 | 8.3% | 2-26% | 4,449 | 93.9% | 93-95% | 85.6% |  |
| forward | 20 | 3 | `Y` | Y&rarr;A 31 | `H` | 31 | 9.7% | 3-25% | 4,442 | 94.0% | 93-95% | 84.4% |  |
| forward | 21 | 2 | `C` | C&rarr;T 43, C&rarr;A 4, C&rarr;G 1 | `H` (97.9%) | 48 | 10.4% | 5-22% | 4,425 | 94.4% | 94-95% | 83.9% |  |
| forward | 8 | 15 | `C` | C&rarr;T 25, C&rarr;A 2, C&rarr;G 2 | hypervariable | 29 | 10.3% | 4-26% | 4,444 | 94.0% | 93-95% | 83.6% |  |
| reverse | 12 | 11 | `T` | T&rarr;A 93, T&rarr;C 70, T&rarr;G 2 | `H` (98.8%) | 165 | 20.0% | 15-27% | 4,308 | 96.3% | 96-97% | 76.3% |  |
| reverse | 17 | 6 | `Y` | Y&rarr;G 12, Y&rarr;A 10 | hypervariable | 22 | 22.7% | 10-43% | 4,451 | 93.8% | 93-94% | 71.1% |  |
| reverse | 15 | 8 | `R` | R&rarr;T 10, R&rarr;C 10 | hypervariable | 20 | 25.0% | 11-47% | 4,453 | 93.8% | 93-94% | 68.8% |  |
| reverse | 7 | 16 | `C` | C&rarr;T 54, C&rarr;A 31, C&rarr;G 2 | `H` (97.7%) | 87 | 26.4% | 18-37% | 4,386 | 94.8% | 94-95% | 68.3% |  |
| reverse | 2 | 21 | `A` | A&rarr;G 40, A&rarr;C 13 | `V` | 53 | 26.4% | 16-40% | 4,420 | 94.3% | 94-95% | 67.8% | yes |
| reverse | 3 | 20 | `C` | C&rarr;T 26, C&rarr;G 24, C&rarr;A 8 | hypervariable | 58 | 27.6% | 18-40% | 4,415 | 94.3% | 94-95% | 66.7% | yes |
| reverse | 8 | 15 | `A` | A&rarr;G 39, A&rarr;C 12, A&rarr;T 4 | hypervariable | 55 | 29.1% | 19-42% | 4,418 | 94.3% | 94-95% | 65.2% |  |
| forward | 12 | 11 | `A` | A&rarr;G 16, A&rarr;C 3, A&rarr;T 2 | hypervariable | 21 | 38.1% | 21-59% | 4,452 | 93.7% | 93-94% | 55.6% |  |
| forward | 19 | 4 | `A` | A&rarr;G 87, A&rarr;T 8, A&rarr;C 3 | `D` (96.9%) | 98 | 43.9% | 34-54% | 4,375 | 94.6% | 94-95% | 50.7% |  |
| forward | 13 | 10 | `T` | T&rarr;G 61, T&rarr;A 27, T&rarr;C 9 | hypervariable | 97 | 45.4% | 36-55% | 4,376 | 94.5% | 94-95% | 49.2% |  |
| reverse | 14 | 9 | `C` | C&rarr;T 292, C&rarr;G 32, C&rarr;A 31 | hypervariable | 355 | 55.2% | 50-60% | 4,118 | 96.7% | 96-97% | 41.5% |  |
| reverse | 4 | 19 | `G` | G&rarr;A 357, G&rarr;C 36, G&rarr;T 18 | `V` (95.6%) | 411 | 56.4% | 52-61% | 4,062 | 97.2% | 97-98% | 40.7% | yes |
| reverse | 5 | 18 | `C` | C&rarr;T 195, C&rarr;A 18, C&rarr;G 18 | hypervariable | 231 | 55.8% | 49-62% | 4,242 | 95.5% | 95-96% | 39.7% | yes |
| reverse | 9 | 14 | `R` | R&rarr;T 51, R&rarr;C 49 | hypervariable | 100 | 70.0% | 60-78% | 4,373 | 94.0% | 93-95% | 24.0% |  |
| reverse | 10 | 13 | `A` | A&rarr;G 108, A&rarr;C 38, A&rarr;T 10 | hypervariable | 156 | 74.4% | 67-81% | 4,317 | 94.1% | 93-95% | 19.8% |  |
| forward | 10 | 13 | `G` | G&rarr;A 33 | `R` | 33 | 75.8% | 59-87% | 4,440 | 93.6% | 93-94% | 17.8% |  |
| forward | 15 | 8 | `A` | A&rarr;C 31, A&rarr;T 1 | `M` (96.9%) | 32 | 78.1% | 61-89% | 4,441 | 93.6% | 93-94% | 15.4% |  |
| forward | 17 | 6 | `A` | A&rarr;G 31, A&rarr;T 4, A&rarr;C 1 | `D` (97.2%) | 36 | 80.6% | 65-90% | 4,437 | 93.6% | 93-94% | 13.0% |  |
| forward | 18 | 5 | `T` | T&rarr;G 30, T&rarr;A 6 | `D` | 36 | 80.6% | 65-90% | 4,437 | 93.6% | 93-94% | 13.0% |  |
| reverse | 16 | 7 | `T` | T&rarr;C 244, T&rarr;A 5, T&rarr;G 2 | `Y` (97.2%) | 251 | 86.1% | 81-90% | 4,222 | 93.9% | 93-95% | 7.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 3,422 | detect | 2023×106, 2024×193, 2025×172, 2026×143 | Hepatozoon sp.×417, Sarcocystis sp.×228, Sarcocystis cruzi×142 | `PZ661905`, `PZ661859`, `QB043393`, `PZ661788`, `PZ359813`, `PZ359812` (+3,416) |
| rev 16 | 161 | detect | 2023×17, 2024×17, 2025×11, 2026×11 | Hepatozoon canis×114, Hepatozoon sp.×28, Cryptosporidium serpentis×5 | `PZ873231`, `PZ873227`, `PZ873225`, `PZ873209`, `PZ155372`, `PZ155371` (+155) |
| rev 4,5,14 | 121 | reduced | 2023×2, 2024×6, 2025×4, 2026×4 | Cryptosporidium parvum×91, Cryptosporidium sp.×9, Cryptosporidium meleagridis×6 | `PZ944843`, `PZ944842`, `PZ944841`, `PZ621322`, `PQ834959`, `PQ834958` (+115) |
| rev 10 | 88 | detect | 2020×2, 2021×5, 2023×3, 2024×3 | Sarcocystis singaporensis×29, Sarcocystis sp.×15, Sarcocystis zamani×11 | `LC830208`, `OR976521`, `OR976520`, `ON979685`, `ON979684`, `ON972386` (+82) |
| fwd 1,2,3; rev 4,6,12,14 | 58 | fail | 2021×42, 2024×2, 2025×6, 2026×1 | Gregarina sp.×44, Eugregarinorida sp.×4, Gregarina lutescens×2 | `PX830635`, `PV594003`, `PV594002`, `PV594001`, `PV594000`, `PV593999` (+52) |
| rev 9 | 48 | detect | 2021×1, 2022×7, 2024×3, 2025×1 | Sarcocystis bertrami×25, Sarcocystis asinus×6, Sarcocystis fayeri×5 | `LC857068`, `OR680781`, `LC796017`, `LC796016`, `OP626897`, `OM971701` (+42) |
| rev 4,14 | 39 | detect | 2023×1, 2024×10, 2025×7, 2026×2 | Corallicolida sp.×12, Apicomplexa sp.×12, Anthozoaphila gnarlus×8 | `PV426990`, `PX990216`, `PQ863704`, `PQ863701`, `PQ863700`, `PQ863699` (+33) |
| fwd 10,15,17,18,19 | 24 | reduced | 2016×23, 2026×1 | Nematopsis temporariae×24 | `OZ557594`, `KT717659`, `KT717658`, `KT717657`, `KT717656`, `KT717655` (+18) |

## Leucocytozoon_cyt_c_Hellgren_2004

Leucocytozoon (taxid 195944) — status **declining** — 340 evaluable of 7,904 screened records

- forward: `5'-ATGGTGTTTTAGATACTTACATT-3'` (23 nt)
- reverse: `5'-CATTATCTGGATGAGATAATGGIGC-3'` (25 nt)

**38 of 340 evaluable records (11%) share one mismatch pattern, mostly Leucocytozoon sp., deposited 2024-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 1 | 25 | `C` | C&rarr;A 88, C&rarr;T 12, C&rarr;G 2 | `H` (98.0%) | 102 | 0.0% | 0-4% | 238 | 98.7% | 96-100% | 98.7% | yes |
| reverse | 2 | 24 | `G` | G&rarr;A 107 | `R` | 107 | 3.7% | 1-9% | 233 | 99.1% | 97-100% | 95.4% | yes |
| reverse | 16 | 10 | `G` | G&rarr;A 78, G&rarr;T 6 | `D` | 84 | 0.0% | 0-4% | 256 | 91.8% | 88-95% | 91.8% |  |
| reverse | 25 | 1 | `C` | C&rarr;A 84, C&rarr;G 6 | `V` | 90 | 2.2% | 1-8% | 250 | 93.2% | 89-96% | 91.0% |  |
| forward | 16 | 8 | `T` | T&rarr;A 62 | `W` | 62 | 0.0% | 0-6% | 278 | 84.5% | 80-88% | 84.5% |  |
| forward | 5 | 19 | `A` | A&rarr;G 32, A&rarr;T 4 | `D` | 36 | 0.0% | 0-10% | 304 | 77.3% | 72-82% | 77.3% | yes |
| reverse | 24 | 2 | `A` | A&rarr;G 21 | `R` | 21 | 0.0% | 0-15% | 319 | 73.7% | 69-78% | 73.7% |  |
| forward | 14 | 10 | `T` | T&rarr;C 28, T&rarr;A 15 | `H` | 43 | 7.0% | 2-19% | 297 | 78.1% | 73-82% | 71.1% |  |
| forward | 7 | 17 | `T` | T&rarr;A 94, T&rarr;C 45 | `H` | 139 | 28.1% | 21-36% | 201 | 97.5% | 94-99% | 69.5% |  |
| reverse | 11 | 15 | `G` | G&rarr;C 62, G&rarr;A 24 | `V` | 86 | 27.9% | 20-38% | 254 | 83.1% | 78-87% | 55.2% |  |
| reverse | 18 | 8 | `T` | T&rarr;A 95, T&rarr;C 1 | `W` (99.0%) | 96 | 35.4% | 27-45% | 244 | 82.4% | 77-87% | 47.0% |  |
| forward | 17 | 7 | `T` | T&rarr;C 25, T&rarr;A 4 | `H` | 29 | 31.0% | 17-49% | 311 | 72.7% | 67-77% | 41.6% |  |
| forward | 8 | 16 | `C` | C&rarr;T 182 | `Y` | 182 | 52.7% | 46-60% | 158 | 88.0% | 82-92% | 35.2% |  |
| forward | 2 | 22 | `T` | T&rarr;C 31 | `Y` | 31 | 45.2% | 29-62% | 309 | 71.5% | 66-76% | 26.4% | yes |
| reverse | 12 | 14 | `A` | A&rarr;T 79, A&rarr;G 32 | `D` | 111 | 93.7% | 88-97% | 229 | 57.2% | 51-63% | -36.5% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 56 | detect | 2022×3, 2024×44, 2025×5, 2026×1 | Leucocytozoon sp.×56 | `PV948490`, `PV839545`, `LC784022`, `LC784021`, `LC784020`, `LC784019` (+50) |
| fwd 7,8,16; rev 1,2,11,16,18,25 | 38 | fail | 2024×5, 2025×32, 2026×1 | Leucocytozoon sp.×38 | `PV839582`, `PV872129`, `PV872128`, `PV872127`, `PV872126`, `PV872124` (+32) |
| fwd 7,8; rev 12 | 37 | reduced | 2020×23, 2025×13, 2026×1 | Leucocytozoon sp.×37 | `PZ065612`, `PV944119`, `PV944118`, `PV944117`, `PV944116`, `PV944115` (+31) |
| rev 12 | 36 | detect | 2018×7, 2020×8, 2023×8, 2025×1 | Leucocytozoon sp.×32, Leucocytozoon fringillinarum×3, Leucocytozoon gentili×1 | `PQ878335`, `OR901950`, `OR416864`, `OR347665`, `OR347664`, `OR347662` (+30) |
| fwd 8 | 33 | detect | 2018×7, 2020×7, 2023×6, 2026×1 | Leucocytozoon sp.×33 | `PX974372`, `OR901953`, `OR901952`, `OR901951`, `OR416868`, `OR347663` (+27) |
| rev 11,18 | 21 | detect | 2013×2, 2018×1, 2025×1, 2026×2 | Leucocytozoon sp.×21 | `PV948489`, `PV948488`, `PV839546`, `MG428421`, `KF146934`, `KF146933` (+15) |
| fwd 8; rev 12 | 14 | reduced | 2016×1, 2018×1, 2020×12 | Leucocytozoon sp.×14 | `MN459557`, `MN459556`, `MN459544`, `MN459528`, `MN459520`, `MN459516` (+8) |
| fwd 5,7,8,14; rev 1,2,16,18,24,25 | 11 | fail | 2005×11 | Leucocytozoon toddi×11 | `DQ177251`, `DQ177250`, `DQ177249`, `DQ177248`, `DQ177247`, `DQ177246` (+5) |

## Pan_flavivirus_NS5_3_round2

Orthoflavivirus (formerly Flavivirus) (taxid 3044782) — status **declining** — 33,608 evaluable of 61,179 screened records

- forward: `5'-AARGGHAGYMCDGCHATHTGGT-3'` (22 nt)
- reverse: `5'-GTGTCCCAGCCGGCGGTGTCATCAGC-3'` (26 nt)

**3,590 of 33,608 evaluable records (11%) share one mismatch pattern, mostly West, deposited 1989-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 3 | 24 | `A` | A&rarr;T 11,175, A&rarr;G 10,808, A&rarr;C 1,810, +1 more | hypervariable | 23,795 | 5.0% | 5-5% | 9,813 | 98.1% | 98-98% | 93.1% | yes |
| reverse | 18 | 9 | `G` | G&rarr;T 19,774, G&rarr;A 3,756, G&rarr;C 844, +2 more | `D` (96.5%) | 24,376 | 21.0% | 20-21% | 9,232 | 61.9% | 61-63% | 40.9% |  |
| reverse | 9 | 18 | `G` | G&rarr;A 7,264, G&rarr;C 1 | `R` (100.0%) | 7,265 | 5.5% | 5-6% | 26,343 | 39.6% | 39-40% | 34.1% |  |
| forward | 11 | 12 | `D` | D&rarr;C 1,726 | hypervariable | 1,726 | 0.8% | 0-1% | 31,882 | 33.9% | 33-34% | 33.1% |  |
| reverse | 11 | 16 | `G` | G&rarr;A 102 | `R` | 102 | 0.0% | 0-4% | 33,506 | 32.3% | 32-33% | 32.3% |  |
| reverse | 10 | 17 | `T` | T&rarr;C 50, T&rarr;A 4, T&rarr;G 2 | `H` (96.4%) | 56 | 0.0% | 0-6% | 33,552 | 32.3% | 32-33% | 32.3% |  |
| forward | 1 | 22 | `T` | T&rarr;G 36, T&rarr;A 4, T&rarr;C 1 | `D` (97.6%) | 41 | 0.0% | 0-9% | 33,567 | 32.2% | 32-33% | 32.2% | yes |
| forward | 7 | 16 | `A` | A&rarr;C 36, A&rarr;G 1 | `M` (97.3%) | 37 | 0.0% | 0-9% | 33,571 | 32.2% | 32-33% | 32.2% |  |
| forward | 3 | 20 | `G` | G&rarr;C 33, G&rarr;T 3 | `B` | 36 | 0.0% | 0-10% | 33,572 | 32.2% | 32-33% | 32.2% | yes |
| forward | 19 | 4 | `G` | G&rarr;A 42, G&rarr;T 2 | `R` (95.5%) | 44 | 4.5% | 1-15% | 33,564 | 32.2% | 32-33% | 27.7% |  |
| reverse | 6 | 21 | `A` | A&rarr;G 3,687, A&rarr;C 3, A&rarr;T 1 | `R` (99.9%) | 3,691 | 13.9% | 13-15% | 29,917 | 34.5% | 34-35% | 20.6% |  |
| reverse | 24 | 3 | `G` | G&rarr;A 6,586, G&rarr;T 1 | `R` (100.0%) | 6,587 | 17.1% | 16-18% | 27,021 | 35.9% | 35-36% | 18.8% |  |
| forward | 10 | 13 | `G` | G&rarr;A 181, G&rarr;C 39, G&rarr;T 1 | `V` (99.5%) | 221 | 14.5% | 10-20% | 33,387 | 32.3% | 32-33% | 17.8% |  |
| forward | 15 | 8 | `G` | G&rarr;C 148, G&rarr;A 1, G&rarr;T 1 | `S` (98.7%) | 150 | 16.0% | 11-23% | 33,458 | 32.3% | 32-33% | 16.3% |  |
| forward | 16 | 7 | `A` | A&rarr;T 140, A&rarr;G 3 | `W` (97.9%) | 143 | 16.8% | 12-24% | 33,465 | 32.3% | 32-33% | 15.5% |  |
| forward | 17 | 6 | `H` | H&rarr;G 798 | hypervariable | 798 | 18.4% | 16-21% | 32,810 | 32.5% | 32-33% | 14.1% |  |
| forward | 14 | 9 | `Y` | Y&rarr;A 61, Y&rarr;G 53 | hypervariable | 114 | 19.3% | 13-27% | 33,494 | 32.2% | 32-33% | 12.9% |  |
| forward | 9 | 14 | `C` | C&rarr;T 22, C&rarr;G 6, C&rarr;A 1 | `B` (96.6%) | 29 | 20.7% | 10-38% | 33,579 | 32.2% | 32-33% | 11.5% |  |
| forward | 8 | 15 | `H` | H&rarr;G 212 | hypervariable | 212 | 28.8% | 23-35% | 33,396 | 32.2% | 32-33% | 3.4% |  |
| forward | 21 | 2 | `A` | A&rarr;G 83, A&rarr;C 2, A&rarr;T 1 | `R` (96.5%) | 86 | 30.2% | 22-41% | 33,522 | 32.2% | 32-33% | 2.0% |  |
| reverse | 15 | 12 | `G` | G&rarr;T 11,527, G&rarr;A 10,761, G&rarr;C 310, +1 more | `D` (98.6%) | 22,600 | 35.4% | 35-36% | 11,008 | 25.6% | 25-26% | -9.8% |  |
| forward | 12 | 11 | `C` | C&rarr;G 33,556, C&rarr;A 4, C&rarr;T 1, +1 more | `S` (100.0%) | 33,562 | 32.2% | 32-33% | 46 | 17.4% | 9-31% | -14.8% |  |
| reverse | 12 | 15 | `G` | G&rarr;T 22,257, G&rarr;A 2,503, G&rarr;C 2,336, +2 more | hypervariable | 27,098 | 36.5% | 36-37% | 6,510 | 14.1% | 13-15% | -22.4% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 12; rev 12,15 | 3,590 | reduced | 2023×131, 2024×213, 2025×566, 2026×125 | West×2225, Dengue virus×1353, Orthoflavivirus nilense×3 | `PZ754493`, `PZ754492`, `PV834969`, `PV834968`, `PZ675960`, `PZ437308` (+3,584) |
| fwd 12; rev 3,12,18,24 | 3,416 | fail | 2023×445, 2024×429, 2025×149, 2026×48 | Dengue virus×3405, Japanese encephalitis×3, Tick-borne encephalitis×3 | `PZ151992`, `PZ675961`, `PZ454033`, `PZ454032`, `PZ454031`, `PZ454030` (+3,410) |
| fwd 12; rev 3,9,12,18 | 3,285 | fail | 2023×572, 2024×95, 2025×113, 2026×1805 | Dengue virus×2632, dengue virus×650, Tick-borne encephalitis×2 | `PZ859237`, `PZ859236`, `PZ666263`, `PZ666262`, `PZ666261`, `PZ666260` (+3,279) |
| fwd 12; rev 12,15,18 | 3,064 | reduced | 2023×471, 2024×501, 2025×373, 2026×72 | Dengue virus×2991, Orthoflavivirus ilheusense×16, West×14 | `OP595767`, `OZ318959`, `PZ683568`, `PZ683567`, `PZ682609`, `PZ682608` (+3,058) |
| fwd 12; rev 3,15,18 | 2,951 | fail | 2023×362, 2024×479, 2025×300, 2026×820 | Dengue virus×2759, Yellow fever×148, dengue virus×40 | `PZ185676`, `QB001157`, `QB001156`, `QB001155`, `QB001154`, `PZ449417` (+2,945) |
| fwd 12; rev 3,6,12,15,18 | 2,245 | fail | 2023×324, 2024×306, 2025×89, 2026×127 | Dengue virus×2050, Tembusu virus×118, Duck×43 | `OZ319202`, `OZ319158`, `OZ319037`, `OZ318976`, `OZ318972`, `OZ318967` (+2,239) |
| fwd 12; rev 3,9,12,15,18 | 1,989 | fail | 2023×263, 2024×92, 2025×198, 2026×432 | Dengue virus×1921, Murray×48, dengue virus×12 | `PZ520749`, `PV693353`, `PP719138`, `PP719137`, `PP719136`, `PP719135` (+1,983) |
| fwd 12; rev 3,12,15,18 | 1,915 | fail | 2023×176, 2024×307, 2025×126, 2026×37 | Dengue virus×862, Yellow fever×604, Powassan virus×337 | `PZ671926`, `PZ671925`, `PQ197972`, `PQ197971`, `PZ365778`, `PZ324381` (+1,909) |

## ORTHOBUNYAVIRUS_ssRNA_S_segment

Orthobunyavirus (taxid 11572) — status **low coverage** — 181 evaluable of 2,083 screened records

- forward: `5'-AGTAGTGTACTCCAC-3'` (15 nt)
- reverse: `5'-AGTAGTGTGCTCCAC-3'` (15 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 2 | 14 | `A` | A&rarr;T 22, A&rarr;C 17, A&rarr;G 12 | hypervariable | 51 | 0.0% | 0-7% | 130 | 47.7% | 39-56% | 47.7% | yes |
| reverse | 4 | 12 | `C` | C&rarr;A 22, C&rarr;T 18, C&rarr;G 10 | hypervariable | 50 | 0.0% | 0-7% | 131 | 47.3% | 39-56% | 47.3% | yes |
| reverse | 1 | 15 | `C` | C&rarr;A 32, C&rarr;G 8, C&rarr;T 6 | hypervariable | 46 | 0.0% | 0-8% | 135 | 45.9% | 38-54% | 45.9% | yes |
| forward | 1 | 15 | `C` | C&rarr;T 20, C&rarr;A 16, C&rarr;G 5 | hypervariable | 41 | 0.0% | 0-9% | 140 | 44.3% | 36-53% | 44.3% | yes |
| reverse | 2 | 14 | `A` | A&rarr;C 29, A&rarr;T 13, A&rarr;G 5 | hypervariable | 47 | 2.1% | 0-11% | 134 | 45.5% | 37-54% | 43.4% | yes |
| reverse | 3 | 13 | `C` | C&rarr;A 14, C&rarr;G 8 | `V` | 22 | 0.0% | 0-15% | 159 | 39.0% | 32-47% | 39.0% | yes |
| reverse | 6 | 10 | `C` | C&rarr;T 17, C&rarr;G 4, C&rarr;A 1 | `B` (95.5%) | 22 | 0.0% | 0-15% | 159 | 39.0% | 32-47% | 39.0% |  |
| reverse | 9 | 7 | `G` | G&rarr;A 9, G&rarr;T 7, G&rarr;C 6 | hypervariable | 22 | 0.0% | 0-15% | 159 | 39.0% | 32-47% | 39.0% |  |
| reverse | 5 | 11 | `T` | T&rarr;C 22, T&rarr;A 4 | `H` | 26 | 3.8% | 1-19% | 155 | 39.4% | 32-47% | 35.5% | yes |
| reverse | 13 | 3 | `T` | T&rarr;A 10, T&rarr;C 10, T&rarr;G 5 | hypervariable | 25 | 8.0% | 2-25% | 156 | 38.5% | 31-46% | 30.5% |  |
| forward | 11 | 5 | `G` | G&rarr;T 20, G&rarr;C 5, G&rarr;A 4 | hypervariable | 29 | 10.3% | 4-26% | 152 | 38.8% | 31-47% | 28.5% |  |
| reverse | 12 | 4 | `A` | A&rarr;C 13, A&rarr;G 12, A&rarr;T 12 | hypervariable | 37 | 13.5% | 6-28% | 144 | 39.6% | 32-48% | 26.1% |  |
| forward | 15 | 1 | `A` | A&rarr;G 14, A&rarr;T 12, A&rarr;C 5 | hypervariable | 31 | 16.1% | 7-33% | 150 | 38.0% | 31-46% | 21.9% |  |
| reverse | 11 | 5 | `G` | G&rarr;C 29, G&rarr;T 19, G&rarr;A 12 | hypervariable | 60 | 23.3% | 14-35% | 121 | 39.7% | 31-49% | 16.3% |  |
| forward | 7 | 9 | `A` | A&rarr;T 15, A&rarr;G 11, A&rarr;C 1 | `D` (96.3%) | 27 | 22.2% | 11-41% | 154 | 36.4% | 29-44% | 14.1% |  |
| reverse | 14 | 2 | `G` | G&rarr;A 24, G&rarr;T 19, G&rarr;C 6 | hypervariable | 49 | 28.6% | 18-42% | 132 | 36.4% | 29-45% | 7.8% |  |
| reverse | 15 | 1 | `A` | A&rarr;T 17, A&rarr;C 15, A&rarr;G 9 | hypervariable | 41 | 34.1% | 22-49% | 140 | 34.3% | 27-42% | 0.1% |  |
| reverse | 7 | 9 | `G` | G&rarr;A 23, G&rarr;T 22, G&rarr;C 7 | hypervariable | 52 | 34.6% | 23-48% | 129 | 34.1% | 26-43% | -0.5% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 29 | detect | 2018×4, 2019×1, 2020×3, 2023×1 | Melao virus×3, Anopheles×3, Triniti virus×2 | `NC_078269`, `MG792215`, `MN268730`, `MN268727`, `MN268724`, `NC_043698` (+23) |
| fwd 1,2,11,15; rev 4,7,11 | 12 | fail | 2003×1, 2007×7, 2009×3, 2015×1 | Akabane virus×12 | `NC_009895`, `AB968526`, `FJ498801`, `FJ498800`, `FJ498798`, `AB100604` (+6) |
| rev 7,11,14,15 | 9 | reduced | 2014×2, 2016×6, 2023×1 | Oropouche virus×7, Iquitos virus×2 | `OP407854`, `KP795101`, `KP795095`, `KP795089`, `KP795086`, `KP795080` (+3) |
| fwd 7; rev 3,4,5,11,12,14 | 7 | fail | 2012×1, 2015×5, 2020×1 | Schmallenberg virus×6, Orthobunyavirus schmallenbergense×1 | `LC557487`, `KP731870`, `KP731869`, `KP731868`, `KP731867`, `KP731866` (+1) |
| rev 1,2 | 6 | fail | 2013×1, 2014×2, 2019×2, 2021×1 | Facey's×2, Ingwavuma virus×2, Jatobal virus×2 | `NC_055186`, `NC_043590`, `NC_043576`, `KF697141`, `KF697136`, `JQ675601` |
| fwd 7 | 6 | detect | 2004×1, 2010×1, 2011×4 | Oropouche virus×5, Batai virus×1 | `NC_005777`, `HM470138`, `HM470136`, `HM470134`, `HM470133`, `FJ436804` |
| fwd 2; rev 2 | 6 | fail | 2016×1, 2018×5 | Gamboa virus×4, Pueblo×1, Trubanaman virus×1 | `KX900440`, `KX900437`, `KX900434`, `KX900431`, `KX900428`, `KU661981` |
| fwd 7,15; rev 4,6,8,10,11 | 5 | fail | 2016×5 | Shuni virus×3, Orthobunyavirus shuniense×2 | `KT946781`, `KT946779`, `KP900882`, `KP900867`, `KP900860` |

## CIRCOVIRUSES_ssDNA_vertebrate_Rep_Gene_round2

Circoviridae (taxid 39724) — status **low coverage** — 7,772 evaluable of 24,317 screened records

- forward: `5'-GGATAATGARRARTAYTGCAGTAAAGA-3'` (27 nt)
- reverse: `5'-TCKACTCTTSCCACAMCCVGGYGGSCC-3'` (27 nt)

**2,646 of 7,772 evaluable records (34%) share one mismatch pattern, mostly Porcine circovirus, deposited 1997-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 18 | 10 | `S` | S&rarr;A 2,860, S&rarr;T 12 | `V` (99.6%) | 2,872 | 0.7% | 0-1% | 4,900 | 72.9% | 72-74% | 72.3% |  |
| reverse | 24 | 4 | `A` | A&rarr;G 6,006, A&rarr;T 4 | `R` (99.9%) | 6,010 | 32.5% | 31-34% | 1,762 | 92.9% | 92-94% | 60.4% |  |
| forward | 7 | 21 | `G` | G&rarr;C 995, G&rarr;A 13, G&rarr;T 7 | `S` (98.0%) | 1,015 | 0.2% | 0-1% | 6,757 | 53.1% | 52-54% | 52.9% |  |
| forward | 8 | 20 | `A` | A&rarr;T 974, A&rarr;G 34, A&rarr;C 24 | `D` (97.7%) | 1,032 | 0.4% | 0-1% | 6,740 | 53.2% | 52-54% | 52.9% |  |
| reverse | 15 | 13 | `A` | A&rarr;G 994, A&rarr;C 4 | `R` (99.6%) | 998 | 1.4% | 1-2% | 6,774 | 52.8% | 52-54% | 51.4% |  |
| forward | 24 | 4 | `T` | T&rarr;G 5,288, T&rarr;C 1,093, T&rarr;A 26 | `B` (99.6%) | 6,407 | 37.4% | 36-39% | 1,365 | 87.8% | 86-89% | 50.4% |  |
| reverse | 23 | 5 | `C` | C&rarr;G 48, C&rarr;T 4, C&rarr;A 1 | `B` (98.1%) | 53 | 0.0% | 0-7% | 7,719 | 46.5% | 45-48% | 46.5% |  |
| reverse | 5 | 23 | `G` | G&rarr;C 34, G&rarr;A 2, G&rarr;T 2 | hypervariable | 38 | 0.0% | 0-9% | 7,734 | 46.5% | 45-48% | 46.5% | yes |
| forward | 19 | 9 | `A` | A&rarr;G 22, A&rarr;T 3, A&rarr;C 3 | hypervariable | 28 | 0.0% | 0-12% | 7,744 | 46.4% | 45-48% | 46.4% |  |
| reverse | 9 | 19 | `V` | V&rarr;T 27 | hypervariable | 27 | 0.0% | 0-12% | 7,745 | 46.4% | 45-48% | 46.4% |  |
| forward | 1 | 27 | `A` | A&rarr;G 25, A&rarr;T 1 | `R` (96.2%) | 26 | 0.0% | 0-13% | 7,746 | 46.4% | 45-47% | 46.4% | yes |
| reverse | 22 | 6 | `T` | T&rarr;A 17, T&rarr;C 5, T&rarr;G 1 | `H` (95.7%) | 23 | 0.0% | 0-14% | 7,749 | 46.4% | 45-47% | 46.4% |  |
| reverse | 13 | 15 | `A` | A&rarr;T 45, A&rarr;C 28, A&rarr;G 6 | hypervariable | 79 | 1.3% | 0-7% | 7,693 | 46.7% | 46-48% | 45.4% |  |
| reverse | 14 | 14 | `C` | C&rarr;A 29, C&rarr;G 5, C&rarr;T 1 | `V` (97.1%) | 35 | 2.9% | 1-15% | 7,737 | 46.4% | 45-48% | 43.6% |  |
| reverse | 12 | 16 | `M` | M&rarr;T 16, M&rarr;G 10 | hypervariable | 26 | 3.8% | 1-19% | 7,746 | 46.4% | 45-47% | 42.5% |  |
| reverse | 27 | 1 | `T` | T&rarr;A 982, T&rarr;C 220, T&rarr;G 8 | `H` (99.3%) | 1,210 | 11.7% | 10-14% | 6,562 | 52.6% | 51-54% | 40.9% |  |
| forward | 9 | 19 | `C` | C&rarr;T 448, C&rarr;G 2 | `Y` (99.6%) | 450 | 8.2% | 6-11% | 7,322 | 48.6% | 47-50% | 40.3% |  |
| forward | 16 | 12 | `A` | A&rarr;C 17, A&rarr;G 7, A&rarr;T 2 | hypervariable | 26 | 11.5% | 4-29% | 7,746 | 46.3% | 45-47% | 34.8% |  |
| forward | 3 | 25 | `A` | A&rarr;G 188, A&rarr;T 4, A&rarr;C 1 | `R` (97.4%) | 193 | 19.7% | 15-26% | 7,579 | 46.9% | 46-48% | 27.2% | yes |
| forward | 27 | 1 | `G` | G&rarr;T 208, G&rarr;A 114, G&rarr;C 85 | hypervariable | 407 | 23.6% | 20-28% | 7,365 | 47.5% | 46-49% | 23.9% |  |
| forward | 6 | 22 | `T` | T&rarr;C 153, T&rarr;G 27, T&rarr;A 26 | hypervariable | 206 | 28.6% | 23-35% | 7,566 | 46.7% | 46-48% | 18.1% |  |
| forward | 20 | 8 | `G` | G&rarr;A 5,241, G&rarr;C 51 | `R` (99.0%) | 5,292 | 41.4% | 40-43% | 2,480 | 56.6% | 55-59% | 15.2% |  |
| forward | 26 | 2 | `G` | G&rarr;C 5,232, G&rarr;A 2 | `S` (100.0%) | 5,234 | 41.9% | 41-43% | 2,538 | 55.2% | 53-57% | 13.3% |  |
| reverse | 21 | 7 | `C` | C&rarr;T 5,246 | `Y` | 5,246 | 42.5% | 41-44% | 2,526 | 54.0% | 52-56% | 11.6% |  |
| reverse | 26 | 2 | `C` | C&rarr;T 5,424, C&rarr;G 2, C&rarr;A 1 | `Y` (99.9%) | 5,427 | 43.4% | 42-45% | 2,345 | 52.8% | 51-55% | 9.4% |  |
| forward | 15 | 13 | `R` | R&rarr;T 28, R&rarr;C 6 | hypervariable | 34 | 50.0% | 34-66% | 7,738 | 46.2% | 45-47% | -3.8% |  |
| forward | 17 | 11 | `R` | R&rarr;C 43 | `V` | 43 | 60.5% | 46-74% | 7,729 | 46.2% | 45-47% | -14.3% |  |
| forward | 21 | 7 | `T` | T&rarr;C 120 | `Y` | 120 | 68.3% | 60-76% | 7,652 | 45.9% | 45-47% | -22.4% |  |
| reverse | 3 | 25 | `S` | S&rarr;T 648, S&rarr;A 74 | hypervariable | 722 | 79.9% | 77-83% | 7,050 | 42.8% | 42-44% | -37.1% | yes |
| reverse | 6 | 22 | `Y` | Y&rarr;G 215, Y&rarr;A 108 | hypervariable | 323 | 82.7% | 78-86% | 7,449 | 44.7% | 44-46% | -38.0% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 20,24,26; rev 18,21,24,26 | 2,646 | fail | 2023×279, 2024×116, 2025×72, 2026×51 | Porcine circovirus×2373, Porcine circovirus-2×135, Sequence×67 | `PZ351343`, `PZ351340`, `PZ148085`, `PZ148084`, `PZ148083`, `PZ465519` (+2,640) |
| fwd 20,24,26; rev 21,24,26 | 1,635 | reduced | 2023×193, 2024×110, 2025×73, 2026×39 | Porcine circovirus×1532, Porcine circovirus-2×91, JP×5 | `LC946308`, `LC946307`, `PZ351347`, `PZ351346`, `PZ351345`, `PZ351344` (+1,629) |
| fwd 7,8,24; rev 15,24,27 | 500 | fail | 2023×27, 2024×253, 2025×23, 2026×24 | Pigeon circovirus×457, Columbid circovirus×42, Bat associated×1 | `PZ698351`, `PZ400761`, `PZ400760`, `PZ400759`, `PZ400758`, `PZ400757` (+494) |
| fwd 20,24,26; rev 21,26 | 381 | reduced | 2023×70, 2024×21, 2025×11, 2026×15 | Porcine circovirus×376, Porcine circovirus-2×5 | `PZ465520`, `PZ465516`, `PZ465510`, `PZ465507`, `PZ465506`, `PZ465496` (+375) |
| rev 3 | 298 | reduced | 2023×43, 2024×2, 2025×6, 2026×1 | Beak and×298 | `PX634662`, `PX470190`, `PX470188`, `PV683375`, `PV683374`, `PV683373` (+292) |
| no mismatches | 227 | detect | 2023×37, 2024×9, 2025×9, 2026×18 | Beak and×227 | `PZ512370`, `PZ512369`, `PZ512368`, `PZ512366`, `PZ512363`, `PZ512362` (+221) |
| fwd 20,24,26; rev 24,26,27 | 139 | reduced | 2020×2, 2022×7, 2023×4, 2024×2 | Porcine circovirus×74, Sequence×40, JP×10 | `PQ303662`, `PQ303661`, `MZ594656`, `MZ594655`, `MZ594654`, `MZ594653` (+133) |
| rev 6,24 | 120 | reduced | 2018×2, 2020×1, 2023×15, 2024×5 | Beak and×120 | `OR710298`, `OR710292`, `PP792707`, `OR224880`, `OR224872`, `OR729122` (+114) |

## SSU_rRNA_gene_Plasmodium_SSU_rDNA_Grim_2003

Plasmodium (taxid 5820) — status **low coverage** — 719 evaluable of 2,712 screened records

- forward: `5'-GAACGAGATCTTAACCTGC-3'` (19 nt)
- reverse: `5'-TAITGATAAAGATTACCTA-3'` (19 nt)

**335 of 719 evaluable records (47%) share one mismatch pattern, mostly Plasmodium knowlesi, deposited 1996-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 4 | 16 | `C` | C&rarr;A 339 | `M` | 339 | 0.0% | 0-1% | 380 | 89.7% | 86-92% | 89.7% | yes |
| forward | 5 | 15 | `C` | C&rarr;T 337, C&rarr;A 1 | `Y` (99.7%) | 338 | 0.0% | 0-1% | 381 | 89.5% | 86-92% | 89.5% | yes |
| forward | 10 | 10 | `C` | C&rarr;A 337, C&rarr;G 1 | `M` (99.7%) | 338 | 0.0% | 0-1% | 381 | 89.5% | 86-92% | 89.5% |  |
| reverse | 6 | 14 | `T` | T&rarr;A 338 | `W` | 338 | 0.0% | 0-1% | 381 | 89.5% | 86-92% | 89.5% |  |
| reverse | 10 | 10 | `A` | A&rarr;C 337, A&rarr;G 1 | `M` (99.7%) | 338 | 0.0% | 0-1% | 381 | 89.5% | 86-92% | 89.5% |  |
| forward | 1 | 19 | `C` | C&rarr;T 337 | `Y` | 337 | 0.0% | 0-1% | 382 | 89.3% | 86-92% | 89.3% | yes |
| forward | 12 | 8 | `A` | A&rarr;C 335, A&rarr;G 2 | `M` (99.4%) | 337 | 0.0% | 0-1% | 382 | 89.3% | 86-92% | 89.3% |  |
| forward | 16 | 4 | `C` | C&rarr;A 336 | `M` | 336 | 0.0% | 0-1% | 383 | 89.0% | 86-92% | 89.0% |  |
| reverse | 14 | 6 | `A` | A&rarr;T 337, A&rarr;G 1 | `W` (99.7%) | 338 | 0.3% | 0-2% | 381 | 89.2% | 86-92% | 88.9% |  |
| reverse | 9 | 11 | `G` | G&rarr;C 337, G&rarr;T 3 | `S` (99.1%) | 340 | 0.9% | 0-3% | 379 | 89.2% | 86-92% | 88.3% |  |
| reverse | 15 | 5 | `G` | G&rarr;C 336, G&rarr;A 5, G&rarr;T 1 | `S` (98.2%) | 342 | 1.2% | 0-3% | 377 | 89.4% | 86-92% | 88.2% |  |
| reverse | 1 | 19 | `A` | A&rarr;T 24, A&rarr;G 1, A&rarr;C 1 | `D` (96.2%) | 26 | 0.0% | 0-13% | 693 | 49.2% | 45-53% | 49.2% | yes |
| forward | 6 | 14 | `A` | A&rarr;G 20, A&rarr;C 2, A&rarr;T 1 | `V` (95.7%) | 23 | 100.0% | 86-100% | 696 | 45.7% | 42-49% | -54.3% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 1,5,10,12,16; rev 4,6,9,10,14,15 | 335 | fail | 2020×18, 2024×11, 2025×1, 2026×3 | Plasmodium knowlesi×275, Plasmodium malariae×16, Plasmodium sp.×14 | `PZ500255`, `PV123279`, `PV123278`, `PV628049`, `OR139045`, `OR139044` (+329) |
| no mismatches | 297 | detect | 2021×3, 2022×1, 2023×1, 2024×7 | Plasmodium vivax×80, Plasmodium relictum×39, Plasmodium ovale×32 | `9BUU_SA`, `9BUT_SA`, `9BUS_SA`, `9BUQ_SA`, `9BUP_SA`, `8TPU_SA` (+291) |
| rev 1 | 23 | fail | 2017×2, 2019×17, 2020×1, 2022×1 | Plasmodium elongatum×16, Plasmodium berghei×3, Plasmodium chabaudi×2 | `XR_007844653`, `XR_001678646`, `XR_002696559`, `XR_002688199`, `XR_004611894`, `MK650619` (+17) |
| fwd 6 | 20 | detect | 2003×1, 2006×1, 2019×18 | Plasmodium elongatum×18, Plasmodium vivax×1, Plasmodium simiovale×1 | `MK650572`, `MK650566`, `MK650563`, `MK650560`, `MK650559`, `MK650557` (+14) |
| fwd 2,4; rev 5 | 11 | fail | 2019×11 | Plasmodium vaughani×11 | `MK650599`, `MK650598`, `MK650596`, `MK650595`, `MK650591`, `MK650590` (+5) |
| rev 13 | 9 | detect | 2007×2, 2009×2, 2015×1, 2019×2 | Plasmodium sp.×2, Plasmodium malariae×2, Plasmodium cf.×2 | `XR_003699335`, `XR_003699327`, `KT266778`, `AB489196`, `AB489195`, `AB287278` (+3) |
| fwd 6,7 | 2 | reduced | 1999×1, 2019×1 | Plasmodium elongatum×1, Plasmodium relictum×1 | `MK650543`, `AF145395` |
| fwd 11; rev 9 | 2 | reduced | 1998×1, 2018×1 | Plasmodium vivax×2 | `XR_003001229`, `U93235` |

## ASTROVIRUS_RdRp_Chu_2008_round1

Astroviridae (taxid 39733) — status **low coverage** — 2,917 evaluable of 16,742 screened records

- forward: `5'-GARTTYGATTGGRCKCGKTAYGA-3'` (23 nt)
- reverse: `5'-GGYTTKACCCACATNCCRAA-3'` (20 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 4 | 20 | `A` | A&rarr;T 1,657, A&rarr;C 1 | `W` (99.9%) | 1,658 | 19.5% | 18-22% | 1,259 | 79.6% | 77-82% | 60.0% | yes |
| reverse | 13 | 8 | `C` | C&rarr;T 254, C&rarr;A 7, C&rarr;G 6 | `Y` (95.1%) | 267 | 1.1% | 0-3% | 2,650 | 49.9% | 48-52% | 48.8% |  |
| reverse | 14 | 7 | `A` | A&rarr;C 18, A&rarr;T 10, A&rarr;G 1 | `H` (96.6%) | 29 | 0.0% | 0-12% | 2,888 | 45.9% | 44-48% | 45.9% |  |
| reverse | 2 | 19 | `A` | A&rarr;C 18, A&rarr;T 5, A&rarr;G 2 | hypervariable | 25 | 0.0% | 0-13% | 2,892 | 45.9% | 44-48% | 45.9% | yes |
| reverse | 16 | 5 | `T` | T&rarr;A 18, T&rarr;G 6 | `D` | 24 | 0.0% | 0-14% | 2,893 | 45.8% | 44-48% | 45.8% |  |
| reverse | 5 | 16 | `C` | C&rarr;G 20, C&rarr;A 3 | `V` | 23 | 0.0% | 0-14% | 2,894 | 45.8% | 44-48% | 45.8% | yes |
| reverse | 1 | 20 | `A` | A&rarr;G 10, A&rarr;T 7, A&rarr;C 4 | hypervariable | 21 | 0.0% | 0-15% | 2,896 | 45.8% | 44-48% | 45.8% | yes |
| reverse | 12 | 9 | `C` | C&rarr;A 19, C&rarr;T 7, C&rarr;G 1 | `H` (96.3%) | 27 | 3.7% | 1-18% | 2,890 | 45.8% | 44-48% | 42.1% |  |
| forward | 9 | 15 | `K` | K&rarr;C 998, K&rarr;A 690 | hypervariable | 1,688 | 28.1% | 26-30% | 1,229 | 69.3% | 67-72% | 41.2% |  |
| reverse | 11 | 10 | `C` | C&rarr;A 10, C&rarr;G 7, C&rarr;T 4 | hypervariable | 21 | 4.8% | 1-23% | 2,896 | 45.8% | 44-48% | 41.0% |  |
| forward | 6 | 18 | `K*` | K&rarr;C 897, G&rarr;A 243, K&rarr;A 204, +1 more | - | 1,345 | 33.4% | 31-36% | 1,572 | 55.8% | 53-58% | 22.4% |  |
| forward | 11 | 13 | `R` | R&rarr;T 69, R&rarr;C 2 | `D` (97.2%) | 71 | 26.8% | 18-38% | 2,846 | 45.9% | 44-48% | 19.2% |  |
| forward | 20 | 4 | `T` | T&rarr;A 932, T&rarr;C 532, T&rarr;G 49 | `H` (96.8%) | 1,513 | 42.0% | 40-44% | 1,404 | 49.2% | 47-52% | 7.2% |  |
| reverse | 19 | 2 | `G` | G&rarr;T 336, G&rarr;C 54, G&rarr;A 24 | hypervariable | 414 | 42.0% | 37-47% | 2,503 | 46.0% | 44-48% | 4.0% |  |
| reverse | 20 | 1 | `G` | G&rarr;C 229, G&rarr;T 156, G&rarr;A 10 | `B` (97.5%) | 395 | 43.8% | 39-49% | 2,522 | 45.7% | 44-48% | 1.9% |  |
| reverse | 15 | 6 | `K` | K&rarr;A 1,232, K&rarr;C 308 | hypervariable | 1,540 | 47.8% | 45-50% | 1,377 | 42.8% | 40-45% | -4.9% |  |
| forward | 18 | 6 | `Y` | Y&rarr;G 987, Y&rarr;A 41 | `B` (96.0%) | 1,028 | 48.8% | 46-52% | 1,889 | 43.6% | 41-46% | -5.2% |  |
| forward | 15 | 9 | `T` | T&rarr;C 1,663, T&rarr;G 1, T&rarr;S 1 | `Y` (99.9%) | 1,665 | 50.4% | 48-53% | 1,252 | 38.9% | 36-42% | -11.5% |  |
| forward | 19 | 5 | `T` | T&rarr;C 245, T&rarr;G 10, T&rarr;A 10 | `B` (96.2%) | 265 | 92.5% | 89-95% | 2,652 | 40.8% | 39-43% | -51.7% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 15,18,19,20; rev 15 | 235 | reduced | 2023×54, 2024×11, 2025×14, 2026×32 | Goose astrovirus×235 | `PZ562298`, `PZ348388`, `PZ325484`, `PZ195463`, `PZ195462`, `PZ195461` (+229) |
| fwd 6,9,15; rev 15 | 213 | reduced | 2023×43, 2024×20, 2025×23, 2026×9 | Human astrovirus×161, Mamastrovirus×21, JP×8 | `PZ726271`, `PZ447405`, `PZ447404`, `PZ447403`, `PZ447402`, `PZ447401` (+207) |
| fwd 4,6,9; rev 15 | 184 | fail | 2023×46, 2024×11, 2025×41, 2026×5 | Canine astrovirus×57, Bovine astrovirus×43, Porcine astrovirus×37 | `PZ529594`, `PZ529593`, `ON624283`, `ON624282`, `ON624281`, `ON624280` (+178) |
| fwd 4,9,15,20; rev 13 | 168 | fail | 2022×24, 2023×3, 2025×58, 2026×35 | Porcine astrovirus×89, Mamastrovirus×35, Mamastrovirus sp.×29 | `PX848849`, `LC900476`, `LC900475`, `LC900463`, `LC900458`, `LC900442` (+162) |
| fwd 9,15,18,20; rev 19,20 | 98 | fail | 2009×69, 2012×10, 2022×2, 2025×1 | Turkey astrovirus×85, Astrovirus×10, Porcine astrovirus×2 | `PX113252`, `ON792974`, `ON792973`, `DQ381397`, `DQ381395`, `DQ381394` (+92) |
| fwd 4,20 | 87 | reduced | 2022×11, 2023×14, 2024×1, 2025×3 | Avian nephritis×56, Chicken astrovirus×15, Avastrovirus sp.×10 | `OR951013`, `PP871786`, `PV093023`, `PV093022`, `OR220065`, `OR220064` (+81) |
| fwd 4,9,15 | 77 | fail | 2023×4, 2024×3, 2025×27, 2026×10 | Porcine astrovirus×28, Mamastrovirus×14, Mamastrovirus sp.×10 | `PZ660278`, `ON624269`, `PX942056`, `PX942048`, `PX942040`, `PX941828` (+71) |
| fwd 4,6,9,15; rev 15 | 65 | fail | 2023×6, 2024×2, 2025×20, 2026×5 | Murine astrovirus×16, Bovine astrovirus×10, Mamastrovirus sp.×8 | `QB068546`, `PX692893`, `PX692891`, `PX941967`, `PX941894`, `PX221758` (+59) |

## ORTHOBUNYAVIRUS_ssRNA_M_segment

Orthobunyavirus (taxid 11572) — status **low coverage** — 227 evaluable of 2,083 screened records

- forward: `5'-TCNAARGGHTGYGGNAATGT-3'` (20 nt)
- reverse: `5'-AGTAGTGTGCTACC-3'` (14 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 3 | 12 | `A` | A&rarr;C 52, A&rarr;T 4, A&rarr;G 2 | `H` (96.6%) | 58 | 0.0% | 0-6% | 169 | 42.0% | 35-50% | 42.0% | yes |
| forward | 8 | 13 | `G` | G&rarr;T 36, G&rarr;A 23, G&rarr;C 7 | hypervariable | 66 | 1.5% | 0-8% | 161 | 43.5% | 36-51% | 42.0% |  |
| reverse | 1 | 14 | `C` | C&rarr;A 33, C&rarr;T 14, C&rarr;G 7 | hypervariable | 54 | 0.0% | 0-7% | 173 | 41.0% | 34-48% | 41.0% | yes |
| reverse | 6 | 9 | `G` | G&rarr;A 23, G&rarr;T 19, G&rarr;C 6 | hypervariable | 48 | 0.0% | 0-7% | 179 | 39.7% | 33-47% | 39.7% |  |
| forward | 7 | 14 | `G` | G&rarr;T 16, G&rarr;C 16, G&rarr;A 9 | hypervariable | 41 | 0.0% | 0-9% | 186 | 38.2% | 31-45% | 38.2% |  |
| forward | 5 | 16 | `A` | A&rarr;T 17, A&rarr;G 11, A&rarr;C 5 | hypervariable | 33 | 0.0% | 0-10% | 194 | 36.6% | 30-44% | 36.6% | yes |
| reverse | 8 | 7 | `G` | G&rarr;A 16, G&rarr;C 8, G&rarr;T 3 | hypervariable | 27 | 0.0% | 0-12% | 200 | 35.5% | 29-42% | 35.5% |  |
| forward | 10 | 11 | `G` | G&rarr;A 41, G&rarr;T 12, G&rarr;C 6 | hypervariable | 59 | 5.1% | 2-14% | 168 | 40.5% | 33-48% | 35.4% |  |
| reverse | 4 | 11 | `T` | T&rarr;A 11, T&rarr;C 9 | `H` | 20 | 0.0% | 0-16% | 207 | 34.3% | 28-41% | 34.3% | yes |
| forward | 2 | 19 | `G` | G&rarr;A 57, G&rarr;T 15, G&rarr;C 7 | hypervariable | 79 | 11.4% | 6-20% | 148 | 41.9% | 34-50% | 30.5% | yes |
| forward | 1 | 20 | `T` | T&rarr;C 18, T&rarr;A 11, T&rarr;G 6 | hypervariable | 35 | 5.7% | 2-19% | 192 | 35.9% | 29-43% | 30.2% | yes |
| forward | 16 | 5 | `A` | A&rarr;C 14, A&rarr;T 9, A&rarr;G 6 | hypervariable | 29 | 6.9% | 2-22% | 198 | 34.8% | 29-42% | 28.0% |  |
| forward | 19 | 2 | `C` | C&rarr;A 33, C&rarr;G 33, C&rarr;T 27 | hypervariable | 93 | 15.1% | 9-24% | 134 | 42.5% | 34-51% | 27.5% |  |
| forward | 13 | 8 | `G` | G&rarr;T 55, G&rarr;A 28, G&rarr;C 8 | hypervariable | 91 | 16.5% | 10-25% | 136 | 41.2% | 33-50% | 24.7% |  |
| forward | 3 | 18 | `T` | T&rarr;C 26, T&rarr;A 10, T&rarr;G 9 | hypervariable | 45 | 15.6% | 8-29% | 182 | 35.2% | 29-42% | 19.6% | yes |
| forward | 14 | 7 | `G` | G&rarr;T 37, G&rarr;A 23, G&rarr;C 4 | hypervariable | 64 | 21.9% | 14-33% | 163 | 35.0% | 28-43% | 13.1% |  |
| forward | 4 | 17 | `A` | A&rarr;G 21, A&rarr;T 9, A&rarr;C 5 | hypervariable | 35 | 28.6% | 16-45% | 192 | 31.8% | 26-39% | 3.2% | yes |
| reverse | 13 | 2 | `G` | G&rarr;T 28, G&rarr;A 1 | `K` (96.6%) | 29 | 37.9% | 23-56% | 198 | 30.3% | 24-37% | -7.6% |  |
| reverse | 14 | 1 | `A` | A&rarr;T 18, A&rarr;G 15 | `D` | 33 | 39.4% | 25-56% | 194 | 29.9% | 24-37% | -9.5% |  |
| forward | 20 | 1 | `T` | T&rarr;G 33, T&rarr;A 14, T&rarr;C 11 | hypervariable | 58 | 43.1% | 31-56% | 169 | 27.2% | 21-34% | -15.9% |  |
| reverse | 11 | 4 | `A` | A&rarr;T 20, A&rarr;G 1 | `W` (95.2%) | 21 | 47.6% | 28-68% | 206 | 29.6% | 24-36% | -18.0% |  |
| forward | 17 | 4 | `A` | A&rarr;C 80, A&rarr;T 2 | `M` (97.6%) | 82 | 43.9% | 34-55% | 145 | 24.1% | 18-32% | -19.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 2,5,10,14,17,19 | 16 | fail | 2017×1, 2020×1, 2024×3, 2025×1 | Oropouche virus×16 | `PQ801465`, `PP992528`, `PP477317`, `PP477316`, `MN264268`, `MF620128` (+10) |
| no mismatches | 12 | detect | 2002×2, 2015×2, 2018×1, 2020×1 | La×4, Keystone virus×3, Melao virus×2 | `MN264271`, `NC_004109`, `MH016785`, `KT630292`, `KT630289`, `U88057` (+6) |
| fwd 17 | 11 | detect | 2003×4, 2009×2, 2018×1, 2019×1 | Cache×4, Maguari virus×4, Tensaw virus×3 | `NC_043548`, `MH166878`, `AF186243`, `AF186242`, `AF186241`, `FJ943508` (+5) |
| fwd 4,20 | 9 | reduced | 2017×9 | Wolkberg virus×9 | `NC_034631`, `KX470582`, `KX470579`, `KX470570`, `KX470567`, `KX470564` (+3) |
| fwd 17; rev 11,12,13,14 | 9 | reduced | 1999×1, 2000×4, 2001×4 | Cache×9 | `AF234767`, `AF231115`, `AF231114`, `AF231113`, `AF231119`, `AF231118` (+3) |
| fwd 2,17; rev 2,4,8,11,14 | 8 | fail | 2016×8 | Batai virus×8 | `KT313714`, `KT313711`, `KT313708`, `KT313705`, `KT313702`, `KT313699` (+2) |
| fwd 1,2,8,10,13,19; rev 6 | 7 | fail | 2012×1, 2013×3, 2019×2, 2024×1 | Schmallenberg virus×7 | `PP616750`, `NC_043584`, `MF154865`, `KC355458`, `KC355455`, `JX853180` (+1) |
| rev 2,6,8,13 | 6 | fail | 2017×6 | Inkoo virus×4, Khatanga virus×2 | `KT288306`, `KT288297`, `KT288282`, `KT288279`, `KT288276`, `KT288273` |

## Pan_flavivirus_NS5_3_round1

Orthoflavivirus (formerly Flavivirus) (taxid 3044782) — status **declining** — 33,496 evaluable of 61,179 screened records

- forward: `5'-AACATGATGGGRAARAGRGARAA-3'` (23 nt)
- reverse: `5'-GTGTCCCAGCCGGCGGTGTCATCAGC-3'` (26 nt)

**3,491 of 33,496 evaluable records (10%) share one mismatch pattern, mostly Dengue virus, deposited 1992-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 3 | 24 | `A` | A&rarr;T 11,177, A&rarr;G 10,759, A&rarr;C 1,794, +1 more | hypervariable | 23,732 | 21.4% | 21-22% | 9,764 | 94.9% | 94-95% | 73.6% | yes |
| reverse | 9 | 18 | `G` | G&rarr;A 7,332, G&rarr;C 1 | `R` (100.0%) | 7,333 | 4.9% | 4-5% | 26,163 | 53.4% | 53-54% | 48.5% |  |
| reverse | 11 | 16 | `G` | G&rarr;A 154 | `R` | 154 | 0.0% | 0-2% | 33,342 | 43.0% | 42-44% | 43.0% |  |
| reverse | 10 | 17 | `T` | T&rarr;C 105, T&rarr;A 4, T&rarr;G 2 | `H` (98.2%) | 111 | 0.0% | 0-3% | 33,385 | 43.0% | 42-43% | 43.0% |  |
| forward | 18 | 6 | `G` | G&rarr;C 87, G&rarr;A 81, G&rarr;T 12 | hypervariable | 180 | 3.3% | 2-7% | 33,316 | 43.0% | 43-44% | 39.7% |  |
| forward | 19 | 5 | `T` | T&rarr;C 173, T&rarr;A 3, T&rarr;G 3 | `Y` (96.6%) | 179 | 3.4% | 2-7% | 33,317 | 43.0% | 43-44% | 39.7% |  |
| forward | 7 | 17 | `G` | G&rarr;A 226, G&rarr;T 1 | `R` (99.6%) | 227 | 3.5% | 2-7% | 33,269 | 43.1% | 43-44% | 39.6% |  |
| forward | 21 | 3 | `C` | C&rarr;T 1,447, C&rarr;G 2 | `Y` (99.9%) | 1,449 | 6.4% | 5-8% | 32,047 | 44.5% | 44-45% | 38.1% |  |
| reverse | 6 | 21 | `A` | A&rarr;G 3,686, A&rarr;C 6, A&rarr;T 1 | `R` (99.8%) | 3,693 | 10.2% | 9-11% | 29,803 | 46.9% | 46-47% | 36.7% |  |
| reverse | 24 | 3 | `G` | G&rarr;A 6,550, G&rarr;T 2 | `R` (100.0%) | 6,552 | 17.3% | 16-18% | 26,944 | 49.0% | 48-50% | 31.7% |  |
| reverse | 18 | 9 | `G` | G&rarr;T 19,738, G&rarr;A 3,763, G&rarr;C 841, +2 more | `D` (96.5%) | 24,344 | 35.1% | 35-36% | 9,152 | 63.4% | 62-64% | 28.2% |  |
| reverse | 12 | 15 | `G` | G&rarr;T 22,213, G&rarr;A 2,492, G&rarr;C 2,332, +2 more | hypervariable | 27,039 | 38.0% | 37-39% | 6,457 | 63.1% | 62-64% | 25.1% |  |
| forward | 20 | 4 | `A` | A&rarr;C 18, A&rarr;T 4, A&rarr;G 3 | hypervariable | 25 | 32.0% | 17-52% | 33,471 | 42.8% | 42-43% | 10.8% |  |
| forward | 8 | 16 | `A` | A&rarr;C 3,299, A&rarr;T 1, A&rarr;Y 1 | `M` (99.9%) | 3,301 | 38.7% | 37-40% | 30,195 | 43.3% | 43-44% | 4.6% |  |
| forward | 6 | 18 | `R` | R&rarr;T 2,753, R&rarr;C 273 | hypervariable | 3,026 | 40.1% | 38-42% | 30,470 | 43.1% | 43-44% | 3.0% |  |
| reverse | 15 | 12 | `G` | G&rarr;T 11,455, G&rarr;A 10,699, G&rarr;C 311, +1 more | `D` (98.6%) | 22,467 | 52.4% | 52-53% | 11,029 | 23.3% | 23-24% | -29.0% |  |
| forward | 12 | 12 | `R` | R&rarr;C 4,549, R&rarr;T 558, R&rarr;Y 10 | hypervariable | 5,117 | 71.2% | 70-72% | 28,379 | 37.7% | 37-38% | -33.5% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 3,12,18,24 | 3,491 | fail | 2023×445, 2024×406, 2025×157, 2026×48 | Dengue virus×3486, Japanese encephalitis×3, Kedougou virus×1 | `PZ151992`, `PZ675961`, `PZ454033`, `PZ454032`, `PZ454031`, `PZ454030` (+3,485) |
| rev 3,9,12,18 | 3,287 | fail | 2023×570, 2024×91, 2025×118, 2026×1802 | Dengue virus×2630, dengue virus×656, New×1 | `PZ859237`, `PZ859236`, `PZ666263`, `PZ666262`, `PZ666261`, `PZ666260` (+3,281) |
| rev 3,15,18 | 2,922 | reduced | 2023×364, 2024×477, 2025×294, 2026×806 | Dengue virus×2731, Yellow fever×147, dengue virus×37 | `PZ185676`, `QB001157`, `QB001156`, `QB001155`, `QB001154`, `PZ449417` (+2,916) |
| fwd 12; rev 12,15,18 | 2,843 | reduced | 2023×461, 2024×481, 2025×331, 2026×70 | Dengue virus×2833, dengue virus×8, Yellow fever×1 | `OP595767`, `OZ318959`, `PZ683568`, `PZ683567`, `PZ682609`, `PZ682608` (+2,837) |
| rev 12,15 | 2,211 | detect | 2023×16, 2024×2, 2025×326, 2026×20 | West×2204, Orthoflavivirus nilense×3, Japanese encephalitis×2 | `PZ754493`, `PZ754492`, `PZ437308`, `PZ437307`, `PZ437305`, `PZ437304` (+2,205) |
| rev 3,9,12,15,18 | 1,931 | fail | 2023×262, 2024×89, 2025×153, 2026×433 | Dengue virus×1915, dengue virus×12, West×1 | `PV693353`, `PP719138`, `PP719137`, `PP719136`, `PP719135`, `PP719134` (+1,925) |
| rev 3,12,15,18 | 1,642 | fail | 2023×146, 2024×272, 2025×85, 2026×17 | Dengue virus×654, Yellow fever×629, Powassan virus×334 | `PZ671926`, `PZ671925`, `PZ324381`, `PZ521690`, `PZ454037`, `PZ385152` (+1,636) |
| rev 3,6,12,15,18 | 1,480 | fail | 2023×246, 2024×214, 2025×33, 2026×47 | Dengue virus×1480 | `PZ454015`, `PZ454014`, `PZ454013`, `PZ454012`, `PZ454011`, `PZ454008` (+1,474) |

## MONKEYPOX_dsDNA_B1_SNP_lineageB1_TaqMan_Huo_2022

Monkeypox virus (taxid 10244) — status **declining** — 12,703 evaluable of 13,757 screened records

- forward: `5'-AGTACACAGACCTCCACCAC-3'` (20 nt)
- reverse: `5'-AGTAATTGACCTACTGGTCTAGGG-3'` (24 nt)
- probe: `5'-AAACCAGTCCAAAATTCGCCACAA-3'` (24 nt)

**2,805 of 12,703 evaluable records (22%) share one mismatch pattern, mostly Monkeypox virus, deposited 2004-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 5 | 16 | `A` | A&rarr;G 2,815 | `R` | 2,815 | 0.0% | 0-0% | 9,888 | 100.0% | 100-100% | 100.0% | yes |
| reverse | 24 | 1 | `A` | A&rarr;G 2,814, A&rarr;T 1 | `R` (100.0%) | 2,815 | 0.1% | 0-0% | 9,888 | 99.9% | 100-100% | 99.8% |  |
| probe | 9 | 16 | `T` | T&rarr;C 3,502 | `Y` | 3,502 | 19.6% | 18-21% | 9,201 | 100.0% | 100-100% | 80.4% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 9,190 | detect | 2023×3084, 2024×1379, 2025×716, 2026×753 | Monkeypox virus×9188, Mutant×2 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+9,184) |
| fwd 5; rev 24; prb 9 | 2,805 | fail | 2023×3, 2024×511, 2025×765, 2026×1479 | Monkeypox virus×2805 | `OZ555904`, `OZ555901`, `OZ555900`, `OZ555899`, `OZ540336`, `OZ540332` (+2,799) |
| prb 9 | 676 | reduced | 2023×8, 2024×125, 2025×403, 2026×29 | Monkeypox virus×676 | `OZ531712`, `OZ531711`, `OZ531706`, `OZ531700`, `OZ501870`, `OZ501843` (+670) |
| rev 20; prb 9 | 7 | reduced | 2005×2, 2020×3, 2022×1, 2025×1 | Monkeypox virus×7 | `PV982292`, `OK573020`, `MT903348`, `MT903347`, `MT903346`, `DQ011157` (+1) |
| fwd 5; prb 9 | 5 | fail | 2024×3, 2025×2 | Monkeypox virus×5 | `OZ254422`, `OZ254274`, `PQ221653`, `PQ221590`, `PQ221588` |
| fwd 4 | 3 | reduced | 2026×3 | Monkeypox virus×3 | `OZ501866`, `OZ501842`, `OZ501830` |
| fwd 7 | 2 | detect | 2023×2 | Monkeypox virus×2 | `OQ468954`, `OQ419051` |
| fwd 6; prb 9 | 2 | reduced | 2024×2 | Monkeypox virus×2 | `PP860032`, `PP860028` |

## CIRCOVIRUSES_ssDNA_vertebrate_Rep_Gene_Mankertz_2000_round1

Circoviridae (taxid 39724) — status **declining** — 6,454 evaluable of 24,317 screened records

- forward: `5'-GTGTTTCACBCTYAAYAAYCCTWCMGA-3'` (27 nt)
- reverse: `5'-ATCTTCCCCRTSRTAWCCATCCCACCA-3'` (27 nt)

**4,194 of 6,454 evaluable records (65%) share one mismatch pattern, mostly Porcine circovirus, deposited 1997-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 17 | 11 | `C` | C&rarr;A 577, C&rarr;T 252, C&rarr;G 10 | `H` (98.8%) | 839 | 0.2% | 0-1% | 5,615 | 93.1% | 92-94% | 92.8% |  |
| reverse | 22 | 6 | `C` | C&rarr;G 722, C&rarr;T 12, C&rarr;A 1 | `S` (98.2%) | 735 | 0.0% | 0-1% | 5,719 | 91.4% | 91-92% | 91.4% |  |
| forward | 1 | 27 | `A` | A&rarr;C 336, A&rarr;T 265, A&rarr;G 32, +1 more | hypervariable | 634 | 0.0% | 0-1% | 5,820 | 89.8% | 89-91% | 89.8% | yes |
| forward | 2 | 26 | `G` | G&rarr;C 299, G&rarr;T 250, G&rarr;A 32 | hypervariable | 581 | 0.5% | 0-2% | 5,873 | 89.0% | 88-90% | 88.5% | yes |
| reverse | 25 | 3 | `C` | C&rarr;G 291, C&rarr;T 109, C&rarr;A 16 | `B` (96.2%) | 416 | 1.0% | 0-2% | 6,038 | 86.5% | 86-87% | 85.6% |  |
| reverse | 16 | 12 | `S` | S&rarr;T 327, S&rarr;A 31 | hypervariable | 358 | 0.8% | 0-2% | 6,096 | 85.7% | 85-87% | 84.9% |  |
| forward | 7 | 21 | `C` | C&rarr;A 136, C&rarr;G 32, C&rarr;T 10 | hypervariable | 178 | 0.0% | 0-2% | 6,276 | 83.3% | 82-84% | 83.3% |  |
| forward | 27 | 1 | `G` | G&rarr;T 93, G&rarr;C 46, G&rarr;A 3 | `B` (97.9%) | 142 | 0.0% | 0-3% | 6,312 | 82.8% | 82-84% | 82.8% |  |
| forward | 8 | 20 | `C` | C&rarr;T 182, C&rarr;A 2 | `Y` (98.9%) | 184 | 0.5% | 0-3% | 6,270 | 83.4% | 82-84% | 82.8% |  |
| forward | 6 | 22 | `T` | T&rarr;C 123, T&rarr;A 87, T&rarr;G 47 | hypervariable | 257 | 1.9% | 1-4% | 6,197 | 84.3% | 83-85% | 82.3% |  |
| reverse | 17 | 11 | `T` | T&rarr;C 42, T&rarr;G 27, T&rarr;A 8 | hypervariable | 77 | 0.0% | 0-5% | 6,377 | 82.0% | 81-83% | 82.0% |  |
| reverse | 26 | 2 | `T` | T&rarr;C 95, T&rarr;G 50, T&rarr;A 2 | `B` (98.6%) | 147 | 2.0% | 1-6% | 6,307 | 82.8% | 82-84% | 80.8% |  |
| reverse | 20 | 8 | `C` | C&rarr;T 29, C&rarr;G 1 | `Y` (96.7%) | 30 | 3.3% | 1-17% | 6,424 | 81.4% | 80-82% | 78.0% |  |
| reverse | 12 | 16 | `W` | W&rarr;G 513, W&rarr;C 70 | hypervariable | 583 | 11.5% | 9-14% | 5,871 | 87.9% | 87-89% | 76.4% |  |
| reverse | 19 | 9 | `C` | C&rarr;G 21, C&rarr;T 11, C&rarr;A 2 | hypervariable | 34 | 5.9% | 2-19% | 6,420 | 81.4% | 80-82% | 75.5% |  |
| forward | 3 | 25 | `M` | M&rarr;T 309, M&rarr;G 75 | hypervariable | 384 | 10.4% | 8-14% | 6,070 | 85.5% | 85-86% | 75.1% | yes |
| forward | 18 | 10 | `B` | B&rarr;A 42 | hypervariable | 42 | 7.1% | 2-19% | 6,412 | 81.5% | 81-82% | 74.3% |  |
| reverse | 24 | 4 | `T` | T&rarr;C 493, T&rarr;G 213, T&rarr;A 136 | hypervariable | 842 | 17.7% | 15-20% | 5,612 | 90.5% | 90-91% | 72.8% |  |
| forward | 23 | 5 | `T` | T&rarr;C 21, T&rarr;A 2 | `H` | 23 | 8.7% | 2-27% | 6,431 | 81.3% | 80-82% | 72.6% |  |
| reverse | 18 | 10 | `R` | R&rarr;T 24, R&rarr;C 11 | hypervariable | 35 | 14.3% | 6-29% | 6,419 | 81.4% | 80-82% | 67.1% |  |
| reverse | 9 | 19 | `A` | A&rarr;G 148, A&rarr;C 2 | `R` (98.7%) | 150 | 21.3% | 16-29% | 6,304 | 82.4% | 81-83% | 61.1% |  |
| forward | 21 | 7 | `C` | C&rarr;T 181, C&rarr;G 16 | `B` | 197 | 45.7% | 39-53% | 6,257 | 82.1% | 81-83% | 36.4% |  |
| forward | 24 | 4 | `T` | T&rarr;G 5,133, T&rarr;C 584, T&rarr;A 5 | `B` (99.9%) | 5,722 | 83.3% | 82-84% | 732 | 62.8% | 59-66% | -20.5% |  |
| forward | 15 | 13 | `Y` | Y&rarr;G 4,636, Y&rarr;A 25 | `B` (99.5%) | 4,661 | 90.5% | 90-91% | 1,793 | 56.3% | 54-59% | -34.2% |  |
| reverse | 27 | 1 | `A` | A&rarr;T 5,357, A&rarr;C 366, A&rarr;G 36 | `H` (99.4%) | 5,759 | 85.4% | 84-86% | 695 | 44.3% | 41-48% | -41.1% |  |
| forward | 25 | 3 | `G` | G&rarr;T 5,374, G&rarr;C 2 | `K` (100.0%) | 5,376 | 87.9% | 87-89% | 1,078 | 46.5% | 44-49% | -41.5% |  |
| forward | 26 | 2 | `T` | T&rarr;G 5,373, T&rarr;A 1, T&rarr;C 1 | `K` (100.0%) | 5,375 | 87.9% | 87-89% | 1,079 | 46.4% | 43-49% | -41.5% |  |
| reverse | 21 | 7 | `C` | C&rarr;A 4,969, C&rarr;T 279, C&rarr;G 133 | `H` (97.5%) | 5,381 | 88.2% | 87-89% | 1,073 | 45.1% | 42-48% | -43.1% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 15,24,25,26; rev 21,27 | 4,194 | reduced | 2023×450, 2024×194, 2025×127, 2026×93 | Porcine circovirus×3828, Porcine circovirus-2×226, Sequence×65 | `LC946308`, `LC946307`, `PZ351347`, `PZ351346`, `PZ351345`, `PZ351344` (+4,188) |
| fwd 24,25,26; rev 21,27 | 517 | reduced | 2023×60, 2024×39, 2025×18, 2026×14 | Porcine circovirus×428, Sequence×40, Porcine circovirus-2×13 | `PZ465518`, `PZ465511`, `PZ465500`, `PX417657`, `PX417653`, `PX417648` (+511) |
| fwd 15,17,24,25,26; rev 21,27 | 231 | fail | 2023×61, 2024×19, 2025×3, 2026×5 | Porcine circovirus×224, Porcine circovirus-2×6, Sequence×1 | `PZ148083`, `PX874166`, `PX874165`, `PX874163`, `PX874161`, `PX254068` (+225) |
| fwd 1,2,3,17,24; rev 12,22,24,25,27 | 161 | fail | 2023×12, 2024×13, 2025×13, 2026×2 | Canine circovirus×161 | `PZ311403`, `PZ055485`, `PP691214`, `PP691213`, `PP691212`, `PP691209` (+155) |
| fwd 1,2,17,24,25,26; rev 12,16,22,24 | 157 | fail | 2023×1, 2024×4, 2025×26, 2026×16 | Goose circovirus×156, Circovirus sp.×1 | `PZ599977`, `PZ599974`, `PZ599970`, `PZ599966`, `PZ599965`, `PZ599962` (+151) |
| no mismatches | 155 | detect | 2019×5, 2020×1, 2022×3, 2023×1 | Beak and×153, Sequence×2 | `OR729123`, `OK482702`, `OM675057`, `OM675056`, `MK387074`, `MK803407` (+149) |
| fwd 6,7,8,27; rev 16,21,22,24,25,26 | 73 | fail | 2021×22, 2022×25, 2023×14, 2024×3 | Porcine circovirus×72, Circovirus sp.×1 | `PQ043545`, `PP067098`, `PP067097`, `OQ970017`, `OQ970016`, `OQ658351` (+67) |
| rev 24,27 | 62 | detect | 2016×2, 2019×3, 2023×1, 2024×10 | Beak and×62 | `OR424529`, `OR424520`, `OR424513`, `OR424507`, `OQ995104`, `OQ995102` (+56) |

## DWVA_polyprotein_Rossi_2024

Deformed wing virus A (taxid 2951794) — status **low coverage** — 68 evaluable of 223 screened records

- forward: `5'-CTTTGTCTTCATTAAAGCCAC-3'` (21 nt)
- reverse: `5'-CTCATTAACTGTGTCGTTGAT-3'` (21 nt)
- probe: `5'-TGCGTGGAATGCGTCC-3'` (16 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 7 | 15 | `C` | C&rarr;T 23 | `Y` | 23 | 52.2% | 33-71% | 45 | 97.8% | 88-100% | 45.6% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 30 | detect | 2023×23, 2024×1, 2025×4, 2026×2 | Deformed wing×30 | `PX663591`, `PX663590`, `PX309089`, `PV664190`, `PV664186`, `PV239925` (+24) |
| fwd 2,5; rev 4,7 | 6 | fail | 2025×6 | Deformed wing×6 | `LC905098`, `LC905097`, `LC905095`, `LC905093`, `LC905086`, `LC905085` |
| rev 4,7 | 4 | detect | 2025×1, 2026×3 | Deformed wing×4 | `PX663592`, `PX663589`, `PX663587`, `LC905089` |
| fwd 17; prb 3 | 4 | reduced | 2023×4 | Deformed wing×4 | `OR497393`, `OR497381`, `OR497379`, `OR497378` |
| rev 1,4,7,10 | 3 | reduced | 2025×3 | Deformed wing×3 | `LC905094`, `LC905091`, `LC905090` |
| fwd 17 | 3 | detect | 2022×3 | Deformed wing×3 | `MZ867714`, `MZ867712`, `MZ867711` |
| rev 7 | 1 | detect | 2026×1 | Deformed wing×1 | `PX663586` |
| fwd 2,14 | 1 | fail | 2026×1 | Deformed wing×1 | `PX703942` |

## Pan_mycoplasma_16S_23S_intergenic_space_Rebelo_2011

Mycoplasma (taxid 2093) — status **declining** — 345 evaluable of 24,246 screened records

- forward: `5'-ACACCATGGGAGYTGGTAAT-3'` (20 nt)
- reverse: `5'-CTCCWTCGACTTYCAGACCCAAGGCAT-3'` (27 nt)

**193 of 345 evaluable records (56%) share one mismatch pattern, mostly Mycoplasma sp., deposited 2004-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 11 | 17 | `A` | A&rarr;T 20, A&rarr;C 2 | `H` | 22 | 0.0% | 0-15% | 323 | 100.0% | 99-100% | 100.0% |  |
| reverse | 19 | 9 | `A` | A&rarr;C 21, A&rarr;T 3, A&rarr;G 2 | hypervariable | 26 | 23.1% | 11-42% | 319 | 99.4% | 98-100% | 76.3% |  |
| reverse | 14 | 14 | `C` | C&rarr;T 31, C&rarr;A 1 | `Y` (96.9%) | 32 | 43.8% | 28-61% | 313 | 98.7% | 97-100% | 55.0% |  |
| forward | 19 | 2 | `C` | C&rarr;A 73 | `M` | 73 | 76.7% | 66-85% | 272 | 98.2% | 96-99% | 21.4% |  |
| forward | 14 | 7 | `T` | T&rarr;C 25 | `Y` | 25 | 76.0% | 57-89% | 320 | 95.0% | 92-97% | 19.0% |  |
| reverse | 21 | 7 | `C` | C&rarr;A 21 | `M` | 21 | 100.0% | 85-100% | 324 | 93.2% | 90-95% | -6.8% |  |
| reverse | 25 | 3 | `C` | C&rarr;T 345 | `Y` | 345 | 93.6% | 91-96% | 0 | - | 0-100% | - |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 25 | 193 | detect | 2023×2, 2024×41, 2025×22, 2026×14 | Mycoplasma sp.×68, Mycoplasma anserisalpingitidis×25, Mycoplasma milvi×14 | `NZ_CP132191`, `NC_014014`, `NZ_JHWE01000010`, `NZ_CP187940`, `NZ_CM150749`, `NZ_CP040825` (+187) |
| fwd 19; rev 25 | 46 | detect | 2019×7, 2020×2, 2021×13, 2022×5 | Mycoplasma sp.×14, Mycoplasma zalophidermidis×8, Mycoplasma tauri×8 | `NZ_JANSFS010000010`, `NZ_JNJG01000002`, `NZ_CP053096`, `NZ_CP070479`, `NZ_JAIQCB010000010`, `NZ_JAIQBX010000015` (+40) |
| rev 21,25 | 21 | detect | 2010×1, 2020×2, 2021×1, 2022×1 | Mycoplasma phocoeninasale×11, Mycoplasma sp.×10 | `NZ_CP051480`, `NZ_JAFFTE010000007`, `OP373744`, `DQ840488`, `DQ523533`, `DQ523532` (+15) |
| fwd 14; rev 25 | 8 | detect | 2019×4, 2025×4 | Mycoplasma marinum×4, Mycoplasma todarodis×4 | `NZ_CBDBYK010000026`, `NZ_PSZP01000043`, `NZ_PSZO01000002`, `NZ_CBDBYJ010000006`, `CBDBYK010000026`, `CBDBYJ010000006` (+2) |
| fwd 14,19; rev 25 | 7 | reduced | 2004×1, 2022×4, 2026×2 | Mycoplasma sp.×6, Mycoplasma oxoniensis×1 | `NZ_CM165563`, `CM165563`, `NZ_CP102082`, `NZ_CP102081`, `CP102082`, `CP102081` (+1) |
| fwd 6; rev 25 | 7 | reduced | 2014×1, 2025×6 | Mycoplasma sp.×7 | `NZ_JBSQBH010000007`, `NZ_JBSQBF010000007`, `NZ_JBSQBE010000008`, `NZ_JBSQBD010000005`, `NZ_CP196080`, `CP196080` (+1) |
| fwd 7; rev 25 | 6 | reduced | 2005×1, 2009×1, 2017×2, 2019×2 | Mycoplasma testudineum×6 | `NZ_NNCE01000002`, `NZ_SNWN01000010`, `SNWN01000010`, `NNCE01000002`, `FJ666138`, `AY973570` |
| fwd 12,16,17,18,19,20; rev 10,11,14,19,25 | 6 | fail | 2022×4, 2023×2 | Mycoplasma bradburyae×6 | `NZ_JAJHZN010000014`, `NZ_JAJHZO010000008`, `NZ_CP101415`, `NZ_CP101414`, `CP101415`, `CP101414` |

## CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme

Coronaviridae (taxid 11118) — status **declining** — 7,924 evaluable of 25,559 screened records

- forward: `5'-GGTTGGGAYTAYCCHAARTGTGA-3'` (23 nt)
- reverse: `5'-CCATCATCASWYRGAATCATCATA-3'` (24 nt)

**1,420 of 7,924 evaluable records (18%) share one mismatch pattern, mostly Human coronavirus, deposited 1993-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 1 | 24 | `A` | A&rarr;T 2,911, A&rarr;G 943, A&rarr;C 60 | `D` (98.5%) | 3,914 | 0.0% | 0-0% | 4,010 | 92.3% | 91-93% | 92.3% | yes |
| reverse | 2 | 23 | `T` | T&rarr;A 1,037, T&rarr;G 569 | `D` | 1,606 | 3.4% | 3-4% | 6,318 | 57.7% | 57-59% | 54.3% | yes |
| reverse | 4 | 21 | `C` | C&rarr;T 520, C&rarr;A 378, C&rarr;G 152 | hypervariable | 1,050 | 0.8% | 0-1% | 6,874 | 53.8% | 53-55% | 53.0% | yes |
| reverse | 24 | 1 | `C` | C&rarr;G 728, C&rarr;T 2 | `S` (99.7%) | 730 | 5.5% | 4-7% | 7,194 | 50.9% | 50-52% | 45.4% |  |
| reverse | 13 | 12 | `Y` | Y&rarr;A 2,434, Y&rarr;G 446 | hypervariable | 2,880 | 19.9% | 19-21% | 5,044 | 62.0% | 61-63% | 42.1% |  |
| reverse | 8 | 17 | `T` | T&rarr;C 20, T&rarr;A 1 | `Y` (95.2%) | 21 | 9.5% | 3-29% | 7,903 | 46.8% | 46-48% | 37.3% |  |
| reverse | 19 | 6 | `A` | A&rarr;G 623, A&rarr;C 2, A&rarr;T 1 | `R` (99.5%) | 626 | 20.0% | 17-23% | 7,298 | 49.0% | 48-50% | 29.1% |  |
| forward | 3 | 21 | `T` | T&rarr;C 1,639 | `Y` | 1,639 | 28.9% | 27-31% | 6,285 | 51.4% | 50-53% | 22.5% | yes |
| reverse | 10 | 15 | `A` | A&rarr;T 1,668, A&rarr;G 1,271 | `D` | 2,939 | 38.0% | 36-40% | 4,985 | 51.9% | 51-53% | 13.9% |  |
| forward | 9 | 15 | `H` | H&rarr;G 82 | hypervariable | 82 | 40.2% | 30-51% | 7,842 | 46.8% | 46-48% | 6.6% |  |
| reverse | 16 | 9 | `A` | A&rarr;T 389, A&rarr;G 218, A&rarr;C 89, +2 more | hypervariable | 698 | 45.4% | 42-49% | 7,226 | 46.9% | 46-48% | 1.4% |  |
| reverse | 22 | 3 | `A` | A&rarr;G 1,556, A&rarr;T 2 | `R` (99.9%) | 1,558 | 59.3% | 57-62% | 6,366 | 43.7% | 42-45% | -15.7% |  |
| reverse | 11 | 14 | `G` | G&rarr;A 3,694, G&rarr;C 1 | `R` (100.0%) | 3,695 | 56.7% | 55-58% | 4,229 | 38.0% | 37-39% | -18.7% |  |
| forward | 21 | 3 | `T` | T&rarr;A 849, T&rarr;C 337, T&rarr;G 73 | hypervariable | 1,259 | 68.8% | 66-71% | 6,665 | 42.6% | 41-44% | -26.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 11 | 1,420 | detect | 2023×226, 2024×97, 2025×138, 2026×157 | Human coronavirus×816, Bovine coronavirus×251, Porcine hemagglutinating×48 | `QB036323`, `LC918947`, `LC918946`, `LC642814`, `PZ892151`, `OZ540712` (+1,414) |
| fwd 3; rev 1,13 | 1,117 | fail | 2023×47, 2024×49, 2025×204, 2026×71 | Porcine epidemic×1100, UNVERIFIED_ASMBLY:×15, Alphacoronavirus porci×1 | `PZ463692`, `PZ949040`, `PZ433557`, `PZ433556`, `PZ433555`, `PZ433554` (+1,111) |
| rev 1,2,4,10,11 | 789 | fail | 2023×112, 2024×44, 2025×165, 2026×37 | Infectious bronchitis×473, Porcine deltacoronavirus×262, Porcine coronavirus×13 | `PX388002`, `PX388001`, `PX103085`, `PX103084`, `PZ823619`, `PZ426367` (+783) |
| rev 10,22 | 725 | reduced | 2022×17, 2023×25, 2024×14, 2025×12 | Middle×717, Human betacoronavirus×4, Betacoronavirus×2 | `PP086048`, `OR987496`, `OR987495`, `OR987494`, `OR987493`, `OR987492` (+719) |
| rev 1,13,24 | 498 | fail | 2023×47, 2024×10, 2025×11, 2026×29 | SARS coronavirus×268, Sarbecovirus sp.×57, Betacoronavirus sp.×37 | `PV344449`, `PV344448`, `PV344447`, `PV344446`, `PV344445`, `PV344444` (+492) |
| rev 1,13,22 | 291 | fail | 2023×62, 2024×15, 2025×85, 2026×12 | Human coronavirus×283, Unidentified human×4, Human×2 | `PZ673863`, `LC720428`, `LC687402`, `LC687394`, `LC922677`, `LC922676` (+285) |
| fwd 3,21; rev 13 | 239 | detect | 2023×50, 2024×34, 2025×27, 2026×78 | Human coronavirus×236, Mutant×2, Unidentified human×1 | `LC654445`, `LC922646`, `PZ086305`, `PZ086302`, `PZ086301`, `PZ086300` (+233) |
| fwd 21; rev 11 | 185 | detect | 2023×38, 2024×9, 2025×12, 2026×18 | Transmissible gastroenteritis×48, Canine coronavirus×41, Feline coronavirus×21 | `PZ799096`, `LC932283`, `LC932282`, `LC932281`, `LC932280`, `LC932279` (+179) |

## CHLAMYDIA_genus_16S_Messmer_1997_round1

Chlamydia (taxid 810) — status **low coverage** — 794 evaluable of 1,668 screened records

- forward: `5'-ACGGAATAATGACTTCGG-3'` (18 nt)
- reverse: `5'-TACCTGGTACGCTCAATT-3'` (18 nt)

**259 of 794 evaluable records (33%) share one mismatch pattern, mostly Chlamydia sp., deposited 1993-2025, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 8 | 11 | `G` | G&rarr;T 420, G&rarr;A 26, G&rarr;C 19 | `D` (95.9%) | 465 | 0.6% | 0-2% | 329 | 97.9% | 96-99% | 97.2% |  |
| forward | 12 | 7 | `T` | T&rarr;C 449, T&rarr;A 19 | `Y` (95.9%) | 468 | 4.3% | 3-7% | 326 | 93.6% | 90-96% | 89.3% |  |
| forward | 7 | 12 | `A` | A&rarr;G 469, A&rarr;C 12 | `R` (97.5%) | 481 | 7.3% | 5-10% | 313 | 92.7% | 89-95% | 85.4% |  |
| forward | 6 | 13 | `C` | C&rarr;T 379, C&rarr;A 1 | `Y` (99.7%) | 380 | 0.0% | 0-1% | 414 | 78.5% | 74-82% | 78.5% |  |
| forward | 13 | 6 | `A` | A&rarr;G 367 | `R` | 367 | 0.0% | 0-1% | 427 | 76.1% | 72-80% | 76.1% |  |
| forward | 1 | 18 | `G` | G&rarr;A 110, G&rarr;T 11, G&rarr;C 2 | `D` (98.4%) | 123 | 0.0% | 0-3% | 671 | 48.4% | 45-52% | 48.4% | yes |
| forward | 9 | 10 | `T` | T&rarr;A 19, T&rarr;C 7 | `H` | 26 | 0.0% | 0-13% | 768 | 42.3% | 39-46% | 42.3% |  |
| forward | 11 | 8 | `A` | A&rarr;T 19, A&rarr;G 3 | `D` | 22 | 0.0% | 0-15% | 772 | 42.1% | 39-46% | 42.1% |  |
| forward | 17 | 2 | `C` | C&rarr;A 19, C&rarr;T 1 | `M` (95.0%) | 20 | 5.0% | 1-24% | 774 | 41.9% | 38-45% | 36.9% |  |
| reverse | 2 | 17 | `T` | T&rarr;A 793, T&rarr;G 1 | `W` (99.9%) | 794 | 40.9% | 38-44% | 0 | - | 0-100% | - | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 2 | 259 | reduced | 2022×25, 2023×1, 2024×22, 2025×24 | Chlamydia sp.×70, Chlamydia psittaci×62, Chlamydophila psittaci×46 | `NZ_CP067334`, `NZ_CP137902`, `NZ_CP137896`, `NZ_CP158099`, `NZ_CP158101`, `NZ_CP158097` (+253) |
| fwd 6,7,8,12,13; rev 2 | 257 | fail | 2022×2, 2024×10, 2025×14, 2026×2 | Chlamydia trachomatis×252, Chlamydia muridarum×4, JP×1 | `NZ_CP194983`, `CP194983`, `NZ_CP042790`, `NZ_CP042777`, `NZ_CP035763`, `NZ_CP035760` (+251) |
| fwd 1,6,7,8,12,13; rev 2 | 110 | fail | 2017×27, 2021×4, 2024×7, 2025×22 | Chlamydia trachomatis×110 | `NZ_CP020535`, `NZ_CP007131`, `NZ_CP156064`, `NZ_CP156065`, `NZ_CP156063`, `NZ_CP010571` (+104) |
| fwd 7,8,12; rev 2 | 51 | fail | 2018×25, 2020×1, 2021×1, 2026×6 | Chlamydia muridarum×51 | `NZ_CP182491`, `CP182491`, `NZ_CP183464`, `CP183464`, `NZ_CP009608`, `NZ_CP009609` (+45) |
| fwd 7; rev 2 | 34 | reduced | 2013×4, 2017×1, 2020×8, 2021×10 | Chlamydia pecorum×16, Chlamydia sp.×12, Chlamydophila pecorum×6 | `NZ_CP088917`, `NZ_CP080403`, `NZ_CP080401`, `CP088917`, `CP080403`, `CP080401` (+28) |
| fwd 12; rev 2 | 20 | reduced | 2006×1, 2010×1, 2011×1, 2026×6 | Chlamydophila felis×12, Chlamydia felis×8 | `PX368699`, `PX368698`, `PX368697`, `PX368696`, `PX368695`, `PX368694` (+14) |
| fwd 8,9,11,12,16,17; rev 2 | 19 | fail | 2012×7, 2016×3, 2017×2, 2018×1 | Chlamydia gallinacea×10, Chlamydia sp.×8, Chlamydophila sp.×1 | `NZ_CP015840`, `NZ_CP019792`, `NR_136425`, `MF140888`, `CP019792`, `CP015840` (+13) |
| fwd 1,3,4,6,7,8; rev 2 | 10 | fail | 2013×7, 2014×2, 2015×1 | Chlamydia avium×10 | `NZ_CP006571`, `CP006571`, `NR_121781`, `NR_118595`, `KF366260`, `KF366259` (+4) |

## OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023

Ophidiomyces ophidiicola (taxid 1387563) — status **low coverage** — 192 evaluable of 25,593 screened records

- forward: `5'-AGCGTTTTGCCCCAGCTA-3'` (18 nt)
- reverse: `5'-GCAATGTTGCTCCGCAGTACT-3'` (21 nt)
- probe: `5'-CTCGACTACGAAATCG-3'` (16 nt)

**46 of 192 evaluable records (24%) share one mismatch pattern, mostly Ophidiomyces ophidiicola, deposited 2022, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 10 | 9 | `G` | G&rarr;T 46, G&rarr;C 41 | `B` | 87 | 0.0% | 0-4% | 105 | 77.1% | 68-84% | 77.1% |  |
| reverse | 4 | 18 | `T` | T&rarr;G 46, T&rarr;A 41 | `D` | 87 | 0.0% | 0-4% | 105 | 77.1% | 68-84% | 77.1% | yes |
| reverse | 5 | 17 | `G` | G&rarr;C 87 | `S` | 87 | 0.0% | 0-4% | 105 | 77.1% | 68-84% | 77.1% | yes |
| reverse | 7 | 15 | `C` | C&rarr;G 46, C&rarr;A 41 | `V` | 87 | 0.0% | 0-4% | 105 | 77.1% | 68-84% | 77.1% |  |
| forward | 5 | 14 | `A` | A&rarr;T 41, A&rarr;C 24 | `H` | 65 | 0.0% | 0-6% | 127 | 63.8% | 55-72% | 63.8% | yes |
| forward | 6 | 13 | `C` | C&rarr;A 41, C&rarr;T 24 | `H` | 65 | 0.0% | 0-6% | 127 | 63.8% | 55-72% | 63.8% |  |
| forward | 15 | 4 | `G` | G&rarr;T 41, G&rarr;A 24 | `D` | 65 | 0.0% | 0-6% | 127 | 63.8% | 55-72% | 63.8% |  |
| forward | 1 | 18 | `A` | A&rarr;C 46 | `M` | 46 | 0.0% | 0-8% | 146 | 55.5% | 47-63% | 55.5% | yes |
| forward | 7 | 12 | `C` | C&rarr;T 46 | `Y` | 46 | 0.0% | 0-8% | 146 | 55.5% | 47-63% | 55.5% |  |
| forward | 8 | 11 | `C` | C&rarr;G 46 | `S` | 46 | 0.0% | 0-8% | 146 | 55.5% | 47-63% | 55.5% |  |
| forward | 13 | 6 | `T` | T&rarr;G 46 | `K` | 46 | 0.0% | 0-8% | 146 | 55.5% | 47-63% | 55.5% |  |
| forward | 17 | 2 | `G` | G&rarr;C 46 | `S` | 46 | 0.0% | 0-8% | 146 | 55.5% | 47-63% | 55.5% |  |
| reverse | 10 | 12 | `C` | C&rarr;A 46 | `M` | 46 | 0.0% | 0-8% | 146 | 55.5% | 47-63% | 55.5% |  |
| reverse | 13 | 9 | `G` | G&rarr;A 46 | `R` | 46 | 0.0% | 0-8% | 146 | 55.5% | 47-63% | 55.5% |  |
| reverse | 15 | 7 | `T` | T&rarr;A 46 | `W` | 46 | 0.0% | 0-8% | 146 | 55.5% | 47-63% | 55.5% |  |
| forward | 9 | 10 | `C` | C&rarr;G 41 | `S` | 41 | 0.0% | 0-9% | 151 | 53.6% | 46-61% | 53.6% |  |
| reverse | 8 | 14 | `G` | G&rarr;A 41 | `R` | 41 | 0.0% | 0-9% | 151 | 53.6% | 46-61% | 53.6% |  |
| reverse | 11 | 11 | `T` | T&rarr;C 41 | `Y` | 41 | 0.0% | 0-9% | 151 | 53.6% | 46-61% | 53.6% |  |
| reverse | 18 | 4 | `A` | A&rarr;G 41 | `R` | 41 | 0.0% | 0-9% | 151 | 53.6% | 46-61% | 53.6% |  |
| forward | 12 | 7 | `T` | T&rarr;A 24 | `W` | 24 | 0.0% | 0-14% | 168 | 48.2% | 41-56% | 48.2% |  |
| forward | 14 | 5 | `T` | T&rarr;G 24 | `K` | 24 | 0.0% | 0-14% | 168 | 48.2% | 41-56% | 48.2% |  |
| forward | 18 | 1 | `A` | A&rarr;C 24 | `M` | 24 | 0.0% | 0-14% | 168 | 48.2% | 41-56% | 48.2% |  |
| reverse | 1 | 21 | `T` | T&rarr;C 24 | `Y` | 24 | 0.0% | 0-14% | 168 | 48.2% | 41-56% | 48.2% | yes |
| reverse | 2 | 20 | `C` | C&rarr;A 24 | `M` | 24 | 0.0% | 0-14% | 168 | 48.2% | 41-56% | 48.2% | yes |
| reverse | 9 | 13 | `C` | C&rarr;T 24 | `Y` | 24 | 0.0% | 0-14% | 168 | 48.2% | 41-56% | 48.2% |  |
| reverse | 14 | 8 | `T` | T&rarr;G 24 | `K` | 24 | 0.0% | 0-14% | 168 | 48.2% | 41-56% | 48.2% |  |
| reverse | 17 | 5 | `T` | T&rarr;A 24 | `W` | 24 | 0.0% | 0-14% | 168 | 48.2% | 41-56% | 48.2% |  |
| reverse | 19 | 3 | `A` | A&rarr;T 24 | `W` | 24 | 0.0% | 0-14% | 168 | 48.2% | 41-56% | 48.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 81 | detect | 2022×81 | Ophidiomyces ophidiicola×81 | `NW_026054647`, `JALBCJ010000077`, `JALBCK010000011`, `JALBCI010000002`, `JALBCG010000005`, `JALBCH010000003` (+75) |
| fwd 1,7,8,10,13,17; rev 4,5,7,10,13,15 | 46 | fail | 2022×46 | Ophidiomyces ophidiicola×46 | `JALBCJ010000223`, `JALBCI010000085`, `JALBCE010000100`, `JALBCF010000086`, `JALBBY010000430`, `JALBBX010000098` (+40) |
| fwd 5,6,9,10,15; rev 4,5,7,8,11,18 | 41 | fail | 2022×41 | Ophidiomyces ophidiicola×41 | `NW_026054648`, `JALBCH010000013`, `JALBCE010000013`, `JALBBV010000010`, `JALBBX010000168`, `JALBBT010000029` (+35) |
| fwd 5,6,12,14,15,18; rev 1,2,9,14,17,19 | 24 | fail | 2022×24 | Ophidiomyces ophidiicola×24 | `JALBCH010000101`, `JALBCF010000120`, `JALBCD010000100`, `JALBBY010000169`, `JALBBZ010000104`, `JALBBU010000092` (+18) |

## MONKEYPOX_dsDNA_F3L_region_cladeI_TaqMan_Huo_2022

Monkeypox virus (taxid 10244) — status **declining** — 12,624 evaluable of 13,757 screened records

- forward: `5'-ATCCTCTCTCATTGATTTTTCGCGGGA-3'` (27 nt)
- reverse: `5'-TGGAGAAGCGAGAAGTTAATAAAGC-3'` (25 nt)
- probe: `5'-TCGTCGGAACTGTACACCATAGTAC-3'` (25 nt)

**10,057 of 12,624 evaluable records (80%) share one mismatch pattern, mostly Monkeypox virus, deposited 2004-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 3 | 23 | `T` | T&rarr;C 10,068 | `Y` | 10,068 | 0.0% | 0-0% | 2,556 | 99.6% | 99-100% | 99.6% | yes |
| probe | 11 | 15 | `C` | C&rarr;A 10,068 | `M` | 10,068 | 0.0% | 0-0% | 2,556 | 99.6% | 99-100% | 99.6% |  |
| probe | 17 | 9 | `A` | A&rarr;G 10,068 | `R` | 10,068 | 0.0% | 0-0% | 2,556 | 99.6% | 99-100% | 99.6% |  |
| probe | 21 | 5 | `C` | C&rarr;T 10,068 | `Y` | 10,068 | 0.0% | 0-0% | 2,556 | 99.6% | 99-100% | 99.6% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| prb 3,11,17,21 | 10,057 | fail | 2023×3122, 2024×1528, 2025×1134, 2026×786 | Monkeypox virus×10055, Mutant×2 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+10,051) |
| no mismatches | 2,540 | detect | 2023×3, 2024×506, 2025×682, 2026×1300 | Monkeypox virus×2540 | `OZ555904`, `OZ555901`, `OZ555900`, `OZ555899`, `OZ540336`, `OZ540332` (+2,534) |
| rev 5 | 12 | reduced | 2024×11, 2025×1 | Monkeypox virus×12 | `OZ254519`, `PQ221720`, `PQ221719`, `PQ221718`, `PQ221717`, `PQ221716` (+6) |
| rev 18; prb 3,11,17,21 | 8 | fail | 2015×1, 2025×2, 2026×5 | Monkeypox virus×8 | `PV993194`, `PV993193`, `PX122227`, `PX119016`, `PX119015`, `OZ261637` (+2) |
| fwd 2,3,4,6,14; rev 1,17; prb 4,14,19,20,23 | 2 | fail | 2010×2 | Modified×2 | `FV537352`, `FV537351` |
| prb 4,7,8,9,12,13 | 1 | fail | 2025×1 | Monkeypox virus×1 | `OZ254691` |
| fwd 14; prb 3,11,17,21 | 1 | fail | 2024×1 | Monkeypox virus×1 | `PQ218891` |
| prb 3,8,11,17,21 | 1 | fail | 2022×1 | Monkeypox virus×1 | `OP650030` |

## MONKEYPOX_dsDNA_G2R_WestAfrican_TaqMan_Li_2010

Monkeypox virus (taxid 10244) — status **declining** — 12,396 evaluable of 13,757 screened records

- forward: `5'-CACACCGTCTCTTCCACAGA-3'` (20 nt)
- reverse: `5'-GATACAGGTTAATTTCCACATCG-3'` (23 nt)
- probe: `5'-AACCCGTCGTAACCAGCAATACATTT-3'` (26 nt)

No single position reaches the reporting threshold: the mismatches are spread thinly rather than concentrated. The footprint table below is the informative view for this assay.

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 12,388 | detect | 2023×3010, 2024×1847, 2025×1745, 2026×2365 | Monkeypox virus×12386, Mutant×2 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+12,382) |
| fwd 2,14; rev 2,5,7,8,19 | 4 | fail | 2010×4 | Modified×4 | `FV537352`, `FV537351`, `FV537350`, `FV537349` |
| prb 22 | 2 | detect | 2022×2 | Monkeypox virus×2 | `OP890466`, `ON803418` |
| rev 22 | 1 | detect | 2024×1 | Monkeypox virus×1 | `PP533340` |
| fwd 5; rev 16 | 1 | fail | 2004×1 | Callithrix jacchus×1 | `AY298786` |

## CHLAMYDIA_trachomatis_16S_Messmer_1997_round2

Chlamydia trachomatis (taxid 813) — status **declining** — 363 evaluable of 379 screened records

- forward: `5'-GCAATTGTTTCGGCAATTG-3'` (19 nt)
- reverse: `5'-AGCGGGTATTAACCGCCT-3'` (18 nt)

**105 of 363 evaluable records (29%) share one mismatch pattern, mostly Chlamydia trachomatis, deposited 1996-2025, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 5 | 15 | `A` | A&rarr;G 110 | `R` | 110 | 4.5% | 2-10% | 253 | 100.0% | 99-100% | 95.5% | yes |
| forward | 7 | 13 | `G` | G&rarr;A 110 | `R` | 110 | 4.5% | 2-10% | 253 | 100.0% | 99-100% | 95.5% |  |
| reverse | 3 | 16 | `C` | C&rarr;T 156 | `Y` | 156 | 32.7% | 26-40% | 207 | 100.0% | 98-100% | 67.3% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 202 | detect | 2022×2, 2024×2, 2025×6, 2026×2 | Chlamydia trachomatis×202 | `NZ_CP194983`, `CP194983`, `NZ_CP035763`, `NZ_CP035760`, `NZ_CP035761`, `NZ_CP035762` (+196) |
| fwd 5,7; rev 3 | 105 | fail | 2017×27, 2021×4, 2024×7, 2025×20 | Chlamydia trachomatis×105 | `NZ_CP020535`, `NZ_CP007131`, `NZ_CP156064`, `NZ_CP156065`, `NZ_CP156063`, `NZ_CP010571` (+99) |
| rev 3 | 51 | reduced | 2016×7, 2017×6, 2024×8, 2025×8 | Chlamydia trachomatis×50, JP×1 | `NZ_CP156066`, `NZ_CP156067`, `NZ_CP156061`, `NZ_CP156062`, `NZ_CP010569`, `NZ_CP010567` (+45) |
| fwd 5,7 | 5 | reduced | 2005×2, 2013×1, 2025×2 | Chlamydia trachomatis×5 | `NZ_CP166125`, `CP166125`, `CP006945`, `DQ019297`, `DQ019291` |

## MONKEYPOX_dsDNA_F3L_region_cladeIIab_TaqMan_Huo_2022

Monkeypox virus (taxid 10244) — status **declining** — 12,625 evaluable of 13,757 screened records

- forward: `5'-ATCCTCTCTCATTGATTTTTCGCGGGA-3'` (27 nt)
- reverse: `5'-TGGAGAAGCGAGAAGTTAATAAAGC-3'` (25 nt)
- probe: `5'-TCGTTGGAGCTGTAAACCATAGCAC-3'` (25 nt)

**2,533 of 12,625 evaluable records (20%) share one mismatch pattern, mostly Monkeypox virus, deposited 2001-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 3 | 23 | `C` | C&rarr;T 2,546 | `Y` | 2,546 | 0.0% | 0-0% | 10,079 | 99.9% | 100-100% | 99.9% | yes |
| probe | 11 | 15 | `A` | A&rarr;C 2,546 | `M` | 2,546 | 0.0% | 0-0% | 10,079 | 99.9% | 100-100% | 99.9% |  |
| probe | 17 | 9 | `G` | G&rarr;A 2,546 | `R` | 2,546 | 0.0% | 0-0% | 10,079 | 99.9% | 100-100% | 99.9% |  |
| probe | 21 | 5 | `T` | T&rarr;C 2,546 | `Y` | 2,546 | 0.0% | 0-0% | 10,079 | 99.9% | 100-100% | 99.9% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 10,066 | detect | 2023×3122, 2024×1534, 2025×1136, 2026×787 | Monkeypox virus×10064, Mutant×2 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+10,060) |
| prb 3,11,17,21 | 2,533 | fail | 2023×3, 2024×500, 2025×682, 2026×1299 | Monkeypox virus×2533 | `OZ555904`, `OZ555901`, `OZ555900`, `OZ555899`, `OZ540336`, `OZ540332` (+2,527) |
| rev 5; prb 3,11,17,21 | 12 | fail | 2024×11, 2025×1 | Monkeypox virus×12 | `OZ254519`, `PQ221720`, `PQ221719`, `PQ221718`, `PQ221717`, `PQ221716` (+6) |
| rev 18 | 8 | detect | 2015×1, 2025×2, 2026×5 | Monkeypox virus×8 | `PV993194`, `PV993193`, `PX122227`, `PX119016`, `PX119015`, `OZ261637` (+2) |
| fwd 2,3,4,6,14; rev 1,17 | 2 | fail | 2010×2 | Modified×2 | `FV537352`, `FV537351` |
| fwd 14 | 1 | detect | 2024×1 | Monkeypox virus×1 | `PQ218891` |
| prb 8 | 1 | detect | 2022×1 | Monkeypox virus×1 | `OP650030` |
| fwd 6 | 1 | detect | 2022×1 | Monkeypox virus×1 | `OP415222` |

## ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010_round1

Orthoreovirus (taxid 10882) — status **declining** — 989 evaluable of 14,531 screened records

- forward: `5'-GGBTCMACNGCYACYTCBACYGAGCA-3'` (26 nt)
- reverse: `5'-CDATGTCRTAHWYCCANCCRAA-3'` (22 nt)

**337 of 989 evaluable records (34%) share one mismatch pattern, mostly Piscine orthoreovirus, deposited 2013-2025, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 14 | 9 | `T` | T&rarr;A 351 | `W` | 351 | 0.0% | 0-1% | 638 | 97.5% | 96-98% | 97.5% |  |
| reverse | 2 | 21 | `A` | A&rarr;C 350 | `M` | 350 | 0.0% | 0-1% | 639 | 97.3% | 96-98% | 97.3% | yes |
| reverse | 1 | 22 | `A` | A&rarr;T 349 | `W` | 349 | 0.0% | 0-1% | 640 | 97.2% | 96-98% | 97.2% | yes |
| forward | 3 | 24 | `G` | G&rarr;A 609 | `R` | 609 | 41.7% | 38-46% | 380 | 96.8% | 95-98% | 55.1% | yes |
| forward | 21 | 6 | `M` | M&rarr;T 416, M&rarr;G 214 | hypervariable | 630 | 43.2% | 39-47% | 359 | 97.5% | 95-99% | 54.3% |  |
| forward | 6 | 21 | `Y` | Y&rarr;G 489, Y&rarr;A 127 | hypervariable | 616 | 42.5% | 39-46% | 373 | 96.5% | 94-98% | 54.0% |  |
| forward | 9 | 18 | `B` | B&rarr;A 26 | hypervariable | 26 | 80.8% | 62-91% | 963 | 62.4% | 59-65% | -18.4% |  |
| forward | 24 | 3 | `B` | B&rarr;A 109 | hypervariable | 109 | 91.7% | 85-96% | 880 | 59.3% | 56-63% | -32.4% |  |
| reverse | 18 | 5 | `G` | G&rarr;A 148, G&rarr;C 2 | `R` (98.7%) | 150 | 91.3% | 86-95% | 839 | 57.8% | 54-61% | -33.5% |  |
| reverse | 19 | 4 | `T` | T&rarr;C 41, T&rarr;G 1 | `Y` (97.6%) | 42 | 97.6% | 88-100% | 947 | 61.4% | 58-64% | -36.3% |  |
| forward | 15 | 12 | `Y` | Y&rarr;G 267, Y&rarr;A 17 | hypervariable | 284 | 95.4% | 92-97% | 705 | 49.8% | 46-53% | -45.6% |  |
| forward | 12 | 15 | `Y` | Y&rarr;A 172, Y&rarr;G 167 | hypervariable | 339 | 96.5% | 94-98% | 650 | 45.4% | 42-49% | -51.1% |  |
| reverse | 12 | 11 | `H` | H&rarr;G 360 | hypervariable | 360 | 95.6% | 93-97% | 629 | 44.2% | 40-48% | -51.4% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 3,6,21; rev 1,2,14 | 337 | fail | 2019×9, 2020×108, 2021×13, 2025×182 | Piscine orthoreovirus×328, Piscine reovirus×6, Sequence×2 | `PV409545`, `PV409535`, `PV409525`, `PV409515`, `PV409505`, `PV409495` (+331) |
| no mismatches | 118 | detect | 2023×19, 2024×4, 2025×14, 2026×5 | Mammalian orthoreovirus×105, Reovirus serotype×3, JP×2 | `PZ764064`, `QQ447910`, `QQ447907`, `PZ005679`, `PV855983`, `PV818064` (+112) |
| fwd 3,6,12,15,21; rev 12 | 82 | reduced | 2023×4, 2024×1, 2025×56, 2026×5 | Avian orthoreovirus×82 | `PZ525050`, `PX942584`, `PX942574`, `PX942566`, `PX942556`, `PV448237` (+76) |
| fwd 6,12,15,21; rev 12 | 73 | reduced | 2015×1, 2023×11, 2024×10, 2025×44 | Avian orthoreovirus×73 | `PQ068936`, `PQ068926`, `PQ068916`, `PQ068906`, `PQ068896`, `PV406122` (+67) |
| fwd 3,6,12,15; rev 12 | 47 | reduced | 2023×6, 2024×6, 2025×2, 2026×7 | Avian orthoreovirus×45, Duck reovirus×1, Orthoreovirus sp.×1 | `OP313856`, `OP313846`, `OP302733`, `PZ112220`, `PZ112210`, `PZ112190` (+41) |
| fwd 24; rev 18 | 41 | detect | 2024×41 | Mammalian orthoreovirus×41 | `LC818806`, `LC818796`, `LC818786`, `LC818772`, `LC818762`, `LC818752` (+35) |
| fwd 21,24; rev 12 | 36 | reduced | 2022×5, 2023×7, 2024×9, 2025×3 | Duck reovirus×29, Avian orthoreovirus×5, Muscovy duck×2 | `PQ567546`, `PV296163`, `PV296162`, `PQ456204`, `PQ346622`, `PQ346612` (+30) |
| rev 18 | 15 | detect | 2022×2, 2023×1, 2025×2, 2026×1 | Mammalian orthoreovirus×14, Cataraqui virus×1 | `PX871018`, `PV089291`, `PQ768068`, `OP963624`, `OP057385`, `OP037832` (+9) |

## PD_WNS_ITS1_Shuey_2014

Pseudogymnoascus destructans (taxid 655981) — status **declining** — 454 evaluable of 12,691 screened records

- forward: `5'-CTTTGTTTATTACACTTTGTTGCTTT-3'` (26 nt)
- reverse: `5'-CCGTTGTTGAAAGTTTTAACTATTATAT-3'` (28 nt)
- probe: `5'-CTTGCCAGAGGACTAA-3'` (16 nt)

**57 of 454 evaluable records (13%) share one mismatch pattern, mostly Pseudogymnoascus destructans, deposited 2016-2025, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 2 | 15 | `A` | A&rarr;T 66 | `W` | 66 | 95.5% | 87-98% | 388 | 99.7% | 99-100% | 4.3% | yes |
| probe | 3 | 14 | `T` | T&rarr;C 66 | `Y` | 66 | 95.5% | 87-98% | 388 | 99.7% | 99-100% | 4.3% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 375 | detect | 2021×14, 2022×10, 2024×1, 2025×7 | Pseudogymnoascus destructans×242, Geomyces destructans×133 | `PP958286`, `PP958285`, `PP958284`, `PP958283`, `PP958282`, `PP958281` (+369) |
| prb 2,3 | 57 | reduced | 2022×3, 2023×10, 2024×3, 2025×2 | Pseudogymnoascus destructans×57 | `PX393942`, `PV104929`, `PQ741281`, `PP384908`, `PP384903`, `OR653265` (+51) |
| fwd 13 | 7 | detect | 2015×7 | Pseudogymnoascus destructans×7 | `LN871295`, `LN871294`, `LN871293`, `LN871292`, `LN871291`, `LN871288` (+1) |
| fwd 6 | 5 | detect | 2021×5 | Pseudogymnoascus destructans×5 | `LR739063`, `LR739061`, `LR739057`, `LR739055`, `LR739053` |
| prb 2,3,15 | 4 | reduced | 2020×1, 2022×2, 2025×1 | Pseudogymnoascus destructans×4 | `PP794600`, `OP377706`, `OM967389`, `MW031239` |
| fwd 16; prb 2,3,15 | 2 | fail | 2025×2 | Pseudogymnoascus destructans×2 | `PX657289`, `PX657263` |
| fwd 2,3; prb 2,3 | 1 | reduced | 2018×1 | Pseudogymnoascus destructans×1 | `MK182422` |
| fwd 14; prb 2,3 | 1 | reduced | 2017×1 | Pseudogymnoascus destructans×1 | `MG001399` |

## ARENAVIRUS_ssRNA_S_gene_2

Arenaviridae (taxid 11617) — status **declining** — 1,640 evaluable of 6,454 screened records

- forward: `5'-CATGACKMTGAATTYTGTGACA-3'` (22 nt)
- reverse: `5'-ATRTGYCKRTGWGTTGG-3'` (17 nt)

**251 of 1,640 evaluable records (15%) share one mismatch pattern, mostly Lassa virus, deposited 1987-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 2 | 16 | `G` | G&rarr;C 21, G&rarr;T 18, G&rarr;A 11 | hypervariable | 50 | 0.0% | 0-7% | 1,590 | 66.8% | 64-69% | 66.8% | yes |
| reverse | 1 | 17 | `G` | G&rarr;A 20, G&rarr;C 16, G&rarr;T 11 | hypervariable | 47 | 0.0% | 0-8% | 1,593 | 66.7% | 64-69% | 66.7% | yes |
| reverse | 4 | 14 | `T` | T&rarr;C 17, T&rarr;A 15, T&rarr;G 12 | hypervariable | 44 | 0.0% | 0-8% | 1,596 | 66.5% | 64-69% | 66.5% | yes |
| reverse | 5 | 13 | `G` | G&rarr;T 23, G&rarr;A 10, G&rarr;C 7 | hypervariable | 40 | 0.0% | 0-9% | 1,600 | 66.4% | 64-69% | 66.4% | yes |
| reverse | 14 | 4 | `T` | T&rarr;C 15, T&rarr;A 13, T&rarr;G 9 | hypervariable | 37 | 0.0% | 0-9% | 1,603 | 66.3% | 64-69% | 66.3% |  |
| reverse | 8 | 10 | `T` | T&rarr;A 25, T&rarr;G 6 | `D` | 31 | 0.0% | 0-11% | 1,609 | 66.0% | 64-68% | 66.0% |  |
| reverse | 13 | 5 | `G` | G&rarr;C 19, G&rarr;A 11, G&rarr;T 1 | `V` (96.8%) | 31 | 0.0% | 0-11% | 1,609 | 66.0% | 64-68% | 66.0% |  |
| reverse | 7 | 11 | `G` | G&rarr;C 22, G&rarr;T 4, G&rarr;A 4 | hypervariable | 30 | 0.0% | 0-11% | 1,610 | 66.0% | 64-68% | 66.0% |  |
| reverse | 15 | 3 | `R` | R&rarr;C 13, R&rarr;T 9 | hypervariable | 22 | 0.0% | 0-15% | 1,618 | 65.6% | 63-68% | 65.6% |  |
| reverse | 17 | 1 | `A` | A&rarr;C 37, A&rarr;G 14, A&rarr;T 1 | `V` (98.1%) | 52 | 3.8% | 1-13% | 1,588 | 66.8% | 64-69% | 62.9% |  |
| forward | 2 | 21 | `C` | C&rarr;T 370, C&rarr;A 1, C&rarr;G 1 | `Y` (99.5%) | 372 | 17.2% | 14-21% | 1,268 | 78.7% | 76-81% | 61.5% | yes |
| forward | 6 | 17 | `G` | G&rarr;A 10, G&rarr;C 8, G&rarr;T 5 | hypervariable | 23 | 8.7% | 2-27% | 1,617 | 65.6% | 63-68% | 56.9% |  |
| reverse | 10 | 8 | `K` | K&rarr;A 24, K&rarr;C 6 | hypervariable | 30 | 10.0% | 3-26% | 1,610 | 65.8% | 63-68% | 55.8% |  |
| reverse | 11 | 7 | `C` | C&rarr;T 20, C&rarr;G 7, C&rarr;A 4 | hypervariable | 31 | 16.1% | 7-33% | 1,609 | 65.7% | 63-68% | 49.6% |  |
| forward | 19 | 4 | `G` | G&rarr;A 54, G&rarr;T 3, G&rarr;C 1 | `D` (98.3%) | 58 | 17.2% | 10-29% | 1,582 | 66.5% | 64-69% | 49.3% |  |
| reverse | 3 | 15 | `T` | T&rarr;G 178, T&rarr;C 128, T&rarr;A 88 | hypervariable | 394 | 27.7% | 23-32% | 1,246 | 76.5% | 74-79% | 48.8% | yes |
| forward | 20 | 3 | `T` | T&rarr;C 268, T&rarr;G 3, T&rarr;A 2 | `Y` (98.2%) | 273 | 28.6% | 24-34% | 1,367 | 72.0% | 70-74% | 43.4% |  |
| forward | 5 | 18 | `T` | T&rarr;C 76, T&rarr;G 1 | `Y` (98.7%) | 77 | 37.7% | 28-49% | 1,563 | 66.1% | 64-68% | 28.4% | yes |
| reverse | 16 | 2 | `T` | T&rarr;C 392, T&rarr;G 93, T&rarr;A 20 | `B` (96.0%) | 505 | 48.1% | 44-52% | 1,135 | 72.2% | 69-75% | 24.0% |  |
| reverse | 6 | 12 | `W` | W&rarr;G 742, W&rarr;C 16 | `D` (97.9%) | 758 | 55.8% | 52-59% | 882 | 72.4% | 69-75% | 16.6% |  |
| reverse | 12 | 6 | `Y` | Y&rarr;A 41, Y&rarr;G 34 | hypervariable | 75 | 56.0% | 45-67% | 1,565 | 65.2% | 63-67% | 9.2% |  |
| forward | 11 | 12 | `A` | A&rarr;G 852, A&rarr;T 3 | `R` (99.6%) | 855 | 61.4% | 58-65% | 785 | 68.4% | 65-72% | 7.0% |  |
| forward | 14 | 9 | `T` | T&rarr;A 943, T&rarr;G 474, T&rarr;C 31 | `D` (97.9%) | 1,448 | 65.9% | 63-68% | 192 | 56.2% | 49-63% | -9.6% |  |
| forward | 17 | 6 | `C` | C&rarr;T 1,306, C&rarr;G 39, C&rarr;A 8 | `Y` (96.5%) | 1,353 | 67.2% | 65-70% | 287 | 53.3% | 48-59% | -13.9% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 14,17 | 251 | detect | 2023×31, 2024×10, 2025×10, 2026×17 | Lassa virus×77, Mammarenavirus lassaense×76, Mopeia×25 | `QB068539`, `PZ239818`, `QS268539`, `QS268538`, `QQ887351`, `QQ887350` (+245) |
| fwd 11,14,17; rev 6,16 | 170 | reduced | 2014×44, 2018×116, 2019×5, 2023×3 | Mammarenavirus lassaense×123, Lassa virus×46, Lassa mammarenavirus×1 | `OR147793`, `OR147791`, `MH157037`, `OQ791497`, `MK281627`, `MK281625` (+164) |
| fwd 11,14,17 | 109 | reduced | 2023×9, 2024×6, 2025×16, 2026×8 | Mammarenavirus lassaense×38, JP×15, KR×13 | `QB068541`, `PV847665`, `PV847663`, `PV847661`, `PX115307`, `PX115292` (+103) |
| fwd 11,14,17,20; rev 6,16 | 74 | fail | 2014×2, 2018×68, 2023×4 | Mammarenavirus lassaense×70, Lassa mammarenavirus×2, Lassa virus×2 | `OR493501`, `OR493499`, `OQ791510`, `OQ791508`, `MK118030`, `MK118015` (+68) |
| fwd 11,14,17; rev 6 | 71 | reduced | 2021×1, 2022×2, 2023×1, 2026×1 | Mammarenavirus lassaense×36, Lassa virus×32, Lassa mammarenavirus×2 | `PZ239820`, `OR493503`, `OM140829`, `OM140827`, `MZ558311`, `MT193283` (+65) |
| fwd 2,14,17,20; rev 3,6 | 47 | fail | 2014×1, 2018×39, 2021×1, 2023×6 | Mammarenavirus lassaense×41, Lassa mammarenavirus×5, Lassa virus×1 | `OR147792`, `LC388592`, `LC387488`, `LC387484`, `LC387482`, `LC387480` (+41) |
| fwd 2,14,17 | 42 | reduced | 2023×3, 2024×1, 2025×4, 2026×12 | Mammarenavirus lassaense×16, Mammarenavirus choriomeningitidis×8, Morogoro mammarenavirus×7 | `QB068545`, `QB068543`, `QB068542`, `QB068537`, `QB068533`, `QB068530` (+36) |
| fwd 2,11,14; rev 3,6,16 | 41 | fail | 2020×1, 2022×1, 2025×9, 2026×2 | Mammarenavirus machupoense×20, Machupo virus×20, Machupo mammarenavirus×1 | `PV088375`, `PV861685`, `PV861683`, `PV861681`, `PV861679`, `PV861677` (+35) |

## CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_Lan_2010_round1

Coronaviridae (taxid 11118) — status **declining** — 7,008 evaluable of 25,559 screened records

- forward: `5'-CGTTGGIACWAAYBTVCCWYTICARBTRGG-3'` (30 nt)
- reverse: `5'-GGTCATKATAGCRTCAVMASWWGCNACATG-3'` (30 nt)

**908 of 7,008 evaluable records (13%) share one mismatch pattern, mostly Porcine epidemic, deposited 2001-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 28 | 3 | `T` | T&rarr;G 995, T&rarr;C 301 | `B` | 1,296 | 0.7% | 0-1% | 5,712 | 67.3% | 66-69% | 66.6% |  |
| reverse | 14 | 17 | `V` | V&rarr;T 887 | hypervariable | 887 | 0.0% | 0-0% | 6,121 | 62.9% | 62-64% | 62.9% |  |
| forward | 5 | 26 | `B` | B&rarr;A 677 | hypervariable | 677 | 0.0% | 0-1% | 6,331 | 60.9% | 60-62% | 60.9% | yes |
| reverse | 13 | 18 | `M` | M&rarr;T 961 | `H` | 961 | 2.7% | 2-4% | 6,047 | 63.3% | 62-64% | 60.6% |  |
| reverse | 3 | 28 | `A` | A&rarr;G 553 | `R` | 553 | 1.6% | 1-3% | 6,455 | 59.6% | 58-61% | 57.9% | yes |
| reverse | 5 | 26 | `A` | A&rarr;T 255, A&rarr;G 4 | `W` (98.5%) | 259 | 0.0% | 0-1% | 6,749 | 57.1% | 56-58% | 57.1% | yes |
| forward | 3 | 28 | `R` | R&rarr;T 790, R&rarr;C 35 | `D` (95.8%) | 825 | 5.2% | 4-7% | 6,183 | 61.6% | 60-63% | 56.4% | yes |
| reverse | 4 | 27 | `C` | C&rarr;T 23 | `Y` | 23 | 0.0% | 0-14% | 6,985 | 55.2% | 54-56% | 55.2% | yes |
| forward | 21 | 10 | `W` | W&rarr;C 1,082, W&rarr;G 53 | `H` (95.3%) | 1,135 | 12.8% | 11-15% | 5,873 | 63.1% | 62-64% | 50.4% |  |
| reverse | 22 | 9 | `T` | T&rarr;C 470, T&rarr;G 2 | `Y` (99.6%) | 472 | 12.3% | 10-16% | 6,536 | 58.1% | 57-59% | 45.8% |  |
| reverse | 24 | 7 | `K` | K&rarr;A 2,135, K&rarr;C 15 | `D` (99.3%) | 2,150 | 28.3% | 26-30% | 4,858 | 66.8% | 65-68% | 38.5% |  |
| forward | 15 | 16 | `V` | V&rarr;T 1,424 | hypervariable | 1,424 | 27.7% | 25-30% | 5,584 | 61.9% | 61-63% | 34.2% |  |
| reverse | 9 | 22 | `W` | W&rarr;G 701, W&rarr;C 247 | hypervariable | 948 | 27.0% | 24-30% | 6,060 | 59.4% | 58-61% | 32.4% |  |
| reverse | 23 | 8 | `A` | A&rarr;G 141, A&rarr;T 11 | `D` | 152 | 23.7% | 18-31% | 6,856 | 55.7% | 54-57% | 32.0% |  |
| forward | 30 | 1 | `C` | C&rarr;T 2,363, C&rarr;A 957, C&rarr;G 40 | `H` (98.8%) | 3,360 | 40.0% | 38-42% | 3,648 | 68.8% | 67-70% | 28.8% |  |
| reverse | 21 | 10 | `A` | A&rarr;T 1,598, A&rarr;G 1,424, A&rarr;C 21 | `D` (99.3%) | 3,043 | 39.9% | 38-42% | 3,965 | 66.6% | 65-68% | 26.7% |  |
| forward | 29 | 2 | `G` | G&rarr;A 3,235, G&rarr;T 1,010, G&rarr;C 36 | `D` (99.2%) | 4,281 | 44.8% | 43-46% | 2,727 | 71.0% | 69-73% | 26.2% |  |
| reverse | 30 | 1 | `G` | G&rarr;A 4,621, G&rarr;T 1,426, G&rarr;C 747 | hypervariable | 6,794 | 54.6% | 53-56% | 214 | 67.8% | 61-74% | 13.2% |  |
| forward | 12 | 19 | `W` | W&rarr;C 142, W&rarr;G 86 | hypervariable | 228 | 46.5% | 40-53% | 6,780 | 55.3% | 54-56% | 8.8% |  |
| reverse | 15 | 16 | `A` | A&rarr;C 556, A&rarr;T 155, A&rarr;G 97 | hypervariable | 808 | 48.5% | 45-52% | 6,200 | 55.8% | 55-57% | 7.3% |  |
| reverse | 12 | 19 | `A` | A&rarr;T 1,592, A&rarr;G 866, A&rarr;C 43 | `D` (98.3%) | 2,501 | 53.7% | 52-56% | 4,507 | 55.7% | 54-57% | 2.0% |  |
| forward | 27 | 4 | `T` | T&rarr;C 1,844, T&rarr;A 545, T&rarr;G 489 | hypervariable | 2,878 | 61.0% | 59-63% | 4,130 | 50.8% | 49-52% | -10.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 27; rev 21,30 | 908 | reduced | 2023×37, 2024×44, 2025×124, 2026×44 | Porcine epidemic×891, UNVERIFIED_ASMBLY:×13, Bat coronavirus×2 | `PZ463692`, `PZ949040`, `PZ433556`, `PZ433555`, `PZ433554`, `ON944188` (+902) |
| fwd 29; rev 12,30 | 784 | reduced | 2023×152, 2024×57, 2025×68, 2026×92 | Human coronavirus×432, Bovine coronavirus×234, Porcine hemagglutinating×35 | `QB036323`, `LC918947`, `LC918946`, `LC642814`, `PZ892151`, `OZ540711` (+778) |
| fwd 21,28,29,30; rev 13,14,21,30 | 766 | fail | 2023×25, 2024×56, 2025×13, 2026×1 | Middle×757, Human betacoronavirus×4, Betacoronavirus×3 | `PZ397813`, `PX660034`, `PP086048`, `OR987496`, `OR987495`, `OR987494` (+760) |
| fwd 27,30; rev 30 | 442 | reduced | 2023×53, 2024×4, 2025×15, 2026×12 | SARS coronavirus×265, Sarbecovirus sp.×46, Bat×37 | `PV344449`, `PV344448`, `PV344447`, `PV344446`, `PV344441`, `PX775823` (+436) |
| fwd 3,30; rev 3,24,30 | 279 | fail | 2023×51, 2024×44, 2025×30, 2026×100 | Human coronavirus×275, Mutant×4 | `LC654445`, `OZ470519`, `OZ470518`, `LC922646`, `PZ086306`, `PZ086305` (+273) |
| fwd 3,15,27,29; rev 5,9,22,24,30 | 234 | fail | 2023×61, 2024×19, 2025×84, 2026×14 | Human coronavirus×232, Human×2 | `PZ673863`, `LC720428`, `LC895504`, `LC922677`, `LC922676`, `LC922664` (+228) |
| fwd 5,27,28,29; rev 12,21,30 | 217 | fail | 2023×18, 2024×21, 2025×37, 2026×5 | Porcine deltacoronavirus×187, Porcine coronavirus×13, Deltacoronavirus×5 | `PZ823619`, `PZ392699`, `PZ095794`, `PZ144404`, `KR265864`, `KR265863` (+211) |
| fwd 15,29,30; rev 12,15,24,30 | 167 | fail | 2023×35, 2024×6, 2025×22, 2026×4 | Infectious bronchitis×157, Avian coronavirus×9, Yunnan coronavirus×1 | `PX989790`, `PX759540`, `PX662814`, `PX826228`, `PX653459`, `PX474341` (+161) |

## SBV_polyprotein_Rossi_2024

Iflavirus sacbroodi (sacbrood virus; the paper's name, renamed by ICTV) (taxid 3048309) — status **declining** — 365 evaluable of 900 screened records

- forward: `5'-AAYGTCCACTACACCGAAATGT-3'` (22 nt)
- reverse: `5'-TAHGAGGTAATAACTTTTCGCCA-3'` (23 nt)
- probe: `5'-TGATGAGAGTGGACGAAGAATCTGGAATG-3'` (29 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 23 | 7 | `G` | G&rarr;A 40, G&rarr;T 16 | `D` | 56 | 76.8% | 64-86% | 309 | 98.4% | 96-99% | 21.6% |  |
| reverse | 15 | 9 | `A` | A&rarr;T 32, A&rarr;C 2, A&rarr;G 1 | `H` (97.1%) | 35 | 77.1% | 61-88% | 330 | 97.0% | 95-98% | 19.8% |  |
| reverse | 12 | 12 | `A` | A&rarr;T 31, A&rarr;C 2 | `H` | 33 | 84.8% | 69-93% | 332 | 96.1% | 93-98% | 11.2% |  |
| reverse | 16 | 8 | `T` | T&rarr;A 30 | `W` | 30 | 90.0% | 74-97% | 335 | 95.5% | 93-97% | 5.5% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 241 | detect | 2023×10, 2024×20, 2025×10, 2026×5 | Sacbrood virus×237, Iflavirus sacbroodi×3, WO×1 | `QS360128`, `BK064925`, `PV915611`, `PV915609`, `PV915607`, `PX123565` (+235) |
| rev 12,15,16; prb 23 | 23 | reduced | 2023×2, 2024×3, 2025×11, 2026×3 | Sacbrood virus×21, Iflavirus sacbroodi×2 | `PX550091`, `PX550090`, `PV904220`, `PV904219`, `PV904218`, `PV904216` (+17) |
| prb 23 | 16 | detect | 2021×1, 2024×2, 2025×4, 2026×1 | Sacbrood virus×16 | `PX585033`, `PV008158`, `PX123563`, `PV983670`, `PV656429`, `PQ240505` (+10) |
| fwd 11 | 8 | detect | 2018×1, 2019×1, 2024×2, 2025×1 | Sacbrood virus×8 | `PV664095`, `OR496427`, `OR496419`, `MH133356`, `MF623170`, `KY465677` (+2) |
| fwd 5; prb 23 | 7 | fail | 2018×1, 2020×1, 2023×1, 2025×1 | Sacbrood virus×6, Iflavirus sacbroodi×1 | `PX055611`, `OR228143`, `MN732871`, `KX663835`, `JX270800`, `JX270795` (+1) |
| prb 20 | 7 | detect | 2003×1, 2019×1, 2021×5 | Sacbrood virus×7 | `MZ821926`, `MW435735`, `MW435728`, `MW435724`, `MW435684`, `KX786162` (+1) |
| fwd 5 | 6 | reduced | 2017×1, 2020×1, 2023×1, 2024×1 | Sacbrood virus×6 | `PQ376985`, `OR734831`, `MT482477`, `KY465675`, `JQ796782`, `JQ796781` |
| rev 14 | 6 | detect | 2014×1, 2015×2, 2017×3 | Sacbrood virus×6 | `KX668141`, `KX668140`, `KX668139`, `KP296802`, `KJ959613`, `KM884995` |

## CDV_N_gene_Elia_2006

Morbillivirus canis (formerly Canine morbillivirus) (taxid 3052342) — status **declining** — 664 evaluable of 4,013 screened records

- forward: `5'-AGCTAGTTTCATCTTAACTATCAAATT-3'` (27 nt)
- reverse: `5'-TTAACTCTCCAGAAAACTCATGC-3'` (23 nt)
- probe: `5'-ACCCAAGAGCCGGATACATAGTTTCAATGC-3'` (30 nt)

**101 of 664 evaluable records (15%) share one mismatch pattern, mostly Canine distemper, deposited 1999-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 3 | 25 | `A` | A&rarr;G 104, A&rarr;C 1 | `R` (99.0%) | 105 | 2.9% | 1-8% | 559 | 97.3% | 96-98% | 94.5% | yes |
| forward | 14 | 14 | `T` | T&rarr;C 84 | `Y` | 84 | 2.4% | 1-8% | 580 | 94.0% | 92-96% | 91.6% |  |
| reverse | 19 | 5 | `C` | C&rarr;T 93, C&rarr;A 1 | `Y` (98.9%) | 94 | 8.5% | 4-16% | 570 | 94.6% | 92-96% | 86.1% |  |
| forward | 27 | 1 | `A` | A&rarr;G 22 | `R` | 22 | 22.7% | 10-43% | 642 | 84.4% | 81-87% | 61.7% |  |
| probe | 20 | 11 | `C` | C&rarr;T 15, C&rarr;G 6, C&rarr;A 4 | hypervariable | 25 | 40.0% | 23-59% | 639 | 84.0% | 81-87% | 44.0% |  |
| reverse | 13 | 11 | `A` | A&rarr;G 447, A&rarr;T 4 | `R` (99.1%) | 451 | 78.9% | 75-82% | 213 | 89.7% | 85-93% | 10.7% |  |
| forward | 9 | 19 | `T` | T&rarr;C 14, T&rarr;G 14, T&rarr;A 1 | `B` (96.6%) | 29 | 79.3% | 62-90% | 635 | 82.5% | 79-85% | 3.2% |  |
| probe | 23 | 8 | `A` | A&rarr;G 28, A&rarr;C 15, A&rarr;T 1 | `V` (97.7%) | 44 | 84.1% | 71-92% | 620 | 82.3% | 79-85% | -1.8% |  |
| reverse | 16 | 8 | `T` | T&rarr;C 52, T&rarr;A 8 | `H` | 60 | 88.3% | 78-94% | 604 | 81.8% | 79-85% | -6.5% |  |
| forward | 21 | 7 | `T` | T&rarr;C 35 | `Y` | 35 | 91.4% | 78-97% | 629 | 81.9% | 79-85% | -9.6% |  |
| forward | 12 | 16 | `A` | A&rarr;G 71 | `R` | 71 | 93.0% | 85-97% | 593 | 81.1% | 78-84% | -11.8% |  |
| forward | 24 | 4 | `T` | T&rarr;C 14, T&rarr;G 13, T&rarr;A 4 | hypervariable | 31 | 96.8% | 84-99% | 633 | 81.7% | 78-84% | -15.1% |  |
| probe | 26 | 5 | `A` | A&rarr;G 49, A&rarr;T 34 | `D` | 83 | 96.4% | 90-99% | 581 | 80.4% | 77-83% | -16.0% |  |
| reverse | 10 | 14 | `A` | A&rarr;G 21 | `R` | 21 | 100.0% | 85-100% | 643 | 81.8% | 79-85% | -18.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 127 | detect | 2022×5, 2024×2, 2025×2, 2026×14 | Canine distemper×85, Morbillivirus canis×36, Canine morbillivirus×5 | `PV167797`, `PX610320`, `PX610319`, `PX656924`, `PX656923`, `PX656912` (+121) |
| rev 13 | 101 | detect | 2022×2, 2024×1, 2025×1, 2026×2 | Canine distemper×64, Morbillivirus canis×33, Canine morbillivirus×2 | `PX254110`, `PX656925`, `PV645846`, `PQ311664`, `LC338064`, `LC159587` (+95) |
| fwd 3,14; rev 13,19 | 67 | fail | 2023×3, 2024×3, 2025×5, 2026×3 | Canine distemper×27, Morbillivirus canis×16, Canine morbillivirus×10 | `PZ672980`, `PZ270058`, `PQ571709`, `PX404828`, `PX112332`, `PX112331` (+61) |
| rev 13; prb 26 | 64 | reduced | 2020×26, 2022×3, 2023×1, 2025×7 | Morbillivirus canis×36, Canine distemper×24, Canine morbillivirus×4 | `PX112330`, `PX112329`, `PX112328`, `PX112327`, `PX112326`, `PX112325` (+58) |
| rev 13,16 | 30 | detect | 2009×1, 2014×1, 2020×3, 2026×23 | Morbillivirus canis×23, Canine distemper×7 | `PZ812018`, `PZ812017`, `PZ812016`, `PZ812015`, `PZ812014`, `PZ812013` (+24) |
| fwd 12,21; rev 13 | 18 | reduced | 2014×1, 2016×2, 2025×1, 2026×14 | Morbillivirus canis×14, Canine distemper×4 | `PX734755`, `PX734754`, `PX734752`, `PX734751`, `PX734750`, `PX734749` (+12) |
| fwd 3,27 | 17 | fail | 2022×17 | Canine morbillivirus×17 | `OK557797`, `OK557796`, `OK557795`, `OK557794`, `OK557793`, `OK557792` (+11) |
| fwd 24; rev 13 | 16 | detect | 2019×2, 2023×1, 2024×7, 2026×5 | Morbillivirus canis×14, Canine morbillivirus×1, Canine distemper×1 | `PX656921`, `PX656920`, `PX656919`, `PX656915`, `PX656914`, `PP498908` (+10) |

## MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010

Monkeypox virus (taxid 10244) — status **declining** — 12,052 evaluable of 13,757 screened records

- forward: `5'-GGAAAATGTAAAGACAACGAATACAG-3'` (26 nt)
- reverse: `5'-GCTATCACATAATCTGGAAGCGTA-3'` (24 nt)
- probe: `5'-AAGCCGTAATCTATGTTGTCTATCGTGTCC-3'` (30 nt)

**8,947 of 12,052 evaluable records (74%) share one mismatch pattern, mostly Monkeypox virus, deposited 2022-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 21 | 6 | `A` | A&rarr;G 9,571 | `R` | 9,571 | 100.0% | 100-100% | 2,481 | 99.8% | 100-100% | -0.2% |  |
| reverse | 8 | 17 | `G` | G&rarr;A 8,955 | `R` | 8,955 | 100.0% | 100-100% | 3,097 | 99.8% | 100-100% | -0.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 21; rev 8 | 8,947 | reduced | 2023×2911, 2024×1407, 2025×697, 2026×750 | Monkeypox virus×8945, Mutant×2 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+8,941) |
| no mismatches | 2,469 | detect | 2023×3, 2024×253, 2025×691, 2026×1469 | Monkeypox virus×2469 | `OZ555904`, `OZ555901`, `OZ555900`, `OZ555899`, `OZ540336`, `OZ540332` (+2,463) |
| fwd 21 | 612 | detect | 2023×12, 2024×123, 2025×304, 2026×35 | Monkeypox virus×612 | `OZ531712`, `OZ503384`, `OZ503382`, `OZ503378`, `OZ503341`, `OZ503305` (+606) |
| fwd 1,8,14,19,25,26; rev 4,11,17,19,23; prb 4,6,13,16,25,28 | 4 | fail | 2010×4 | Modified×4 | `FV537352`, `FV537351`, `FV537350`, `FV537349` |
| rev 23 | 3 | detect | 2024×1, 2025×2 | Monkeypox virus×3 | `OZ254777`, `OZ254707`, `PQ221504` |
| prb 25 | 3 | detect | 2025×2, 2026×1 | Monkeypox virus×3 | `OZ254341`, `OZ254256`, `OZ573548` |
| fwd 21; rev 8,23 | 3 | reduced | 2023×3 | Monkeypox virus×3 | `OR500076`, `OR500074`, `OR500072` |
| fwd 21; rev 8,9 | 3 | reduced | 2022×3 | Monkeypox virus×3 | `OP752123`, `OP257259`, `OP257250` |

## E_coli_malB_Candrian_1991

Escherichia coli (taxid 562) — status **declining** — 326 evaluable of 401 screened records

- forward: `5'-GACCTCGGTTTAGTTCACAGA-3'` (21 nt)
- reverse: `5'-CACACGCTGACGCTGACCA-3'` (19 nt)

**85 of 326 evaluable records (26%) share one mismatch pattern, mostly Escherichia coli, deposited 2007-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 1 | 19 | `A` | A&rarr;G 92 | `R` | 92 | 0.0% | 0-4% | 234 | 100.0% | 98-100% | 100.0% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 217 | detect | 2023×11, 2024×11, 2025×13, 2026×8 | Escherichia coli×214, synthetic×2, E.coli malB×1 | `GCA_000006665`, `GCA_000013305`, `GCA_000013265`, `GCA_000010245`, `GCA_000014845`, `GCA_000017745` (+211) |
| rev 1 | 85 | fail | 2023×5, 2024×7, 2025×5, 2026×11 | Escherichia coli×85 | `GCA_000017765`, `GCA_000010385`, `GCA_000026265`, `GCA_000091005`, `GCA_000010765`, `GCA_000010745` (+79) |
| rev 16 | 15 | detect | 2020×1, 2022×1, 2023×4, 2025×1 | Escherichia coli×15 | `GCA_000210475`, `GCA_000987875`, `GCA_001900695`, `GCA_002196495`, `GCA_002105735`, `GCA_001971765` (+9) |
| fwd 11; rev 1 | 5 | fail | 2020×1, 2022×1, 2024×1, 2025×1 | Escherichia coli×5 | `GCA_000765435`, `GCA_013888015`, `GCA_022117635`, `GCA_045165505`, `GCA_053102615` |
| rev 1,16 | 2 | fail | 2022×1, 2024×1 | Escherichia coli×2 | `GCA_021397895`, `GCA_045166215` |
| fwd 3 | 1 | reduced | 2002×1 | Escherichia coli×1 | `GCA_000007445` |
| rev 4 | 1 | reduced | 2026×1 | Escherichia coli×1 | `GCA_055814365` |

## INFLUENZA_A_ssRNA_NP_Tsukamoto_2010

Influenza A virus (taxid 11320) — status **declining** — 186,847 evaluable of 191,425 screened records

- forward: `5'-AGRTAYTGGGCYATAAGRAC-3'` (20 nt)
- reverse: `5'-GCATTGTCTCCGAAGAAATAAG-3'` (22 nt)
- probe: `5'-ATCGGGYTCGTYGCCTTTTCGTCY-3'` (24 nt)

**29,965 of 186,847 evaluable records (16%) share one mismatch pattern, mostly Influenza, deposited 2021-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 14 | 11 | `T` | T&rarr;C 55,071, T&rarr;A 45, T&rarr;G 3, +1 more | `Y` (99.9%) | 55,121 | 2.3% | 2-2% | 131,726 | 98.9% | 99-99% | 96.5% |  |
| probe | 1 | 24 | `Y` | Y&rarr;A 31,671, Y&rarr;G 27 | `H` (99.9%) | 31,698 | 3.2% | 3-3% | 155,149 | 84.2% | 84-84% | 81.0% | yes |
| probe | 7 | 18 | `T` | T&rarr;C 65,302, T&rarr;A 6, T&rarr;G 5 | `Y` (100.0%) | 65,313 | 17.8% | 18-18% | 121,534 | 98.7% | 99-99% | 80.9% |  |
| forward | 20 | 1 | `A` | A&rarr;G 65,069, A&rarr;C 548 | `R` (99.2%) | 65,617 | 18.4% | 18-19% | 121,230 | 98.6% | 98-99% | 80.2% |  |
| probe | 13 | 12 | `Y` | Y&rarr;G 1,039, Y&rarr;A 47 | `B` (95.7%) | 1,086 | 10.4% | 9-12% | 185,761 | 70.8% | 71-71% | 60.4% |  |
| reverse | 4 | 19 | `T` | T&rarr;A 33, T&rarr;C 1, T&rarr;G 1 | `H` (97.1%) | 35 | 11.4% | 5-26% | 186,812 | 70.4% | 70-71% | 59.0% | yes |
| reverse | 1 | 22 | `G` | G&rarr;T 65, G&rarr;A 23, G&rarr;C 3 | `D` (96.7%) | 91 | 15.4% | 9-24% | 186,756 | 70.4% | 70-71% | 55.1% | yes |
| reverse | 2 | 21 | `A` | A&rarr;G 542, A&rarr;C 23, A&rarr;T 5 | `R` (95.1%) | 570 | 30.4% | 27-34% | 186,277 | 70.5% | 70-71% | 40.2% | yes |
| probe | 10 | 15 | `C` | C&rarr;T 132, C&rarr;A 2, C&rarr;G 1 | `Y` (97.8%) | 135 | 40.0% | 32-48% | 186,712 | 70.4% | 70-71% | 30.4% |  |
| forward | 18 | 3 | `R` | R&rarr;T 219, R&rarr;C 137 | hypervariable | 356 | 47.5% | 42-53% | 186,491 | 70.5% | 70-71% | 23.0% |  |
| reverse | 7 | 16 | `A` | A&rarr;G 34, A&rarr;T 4 | `D` | 38 | 50.0% | 35-65% | 186,809 | 70.4% | 70-71% | 20.4% |  |
| forward | 17 | 4 | `T` | T&rarr;C 66, T&rarr;A 3, T&rarr;G 1 | `H` (98.6%) | 70 | 51.4% | 40-63% | 186,777 | 70.4% | 70-71% | 19.0% |  |
| forward | 5 | 16 | `A` | A&rarr;C 219, A&rarr;G 4, A&rarr;T 1 | `M` (97.8%) | 224 | 61.2% | 55-67% | 186,623 | 70.4% | 70-71% | 9.3% | yes |
| probe | 15 | 10 | `G` | G&rarr;A 19, G&rarr;C 6, G&rarr;T 1 | `V` (96.2%) | 26 | 61.5% | 43-78% | 186,821 | 70.4% | 70-71% | 8.9% |  |
| reverse | 19 | 4 | `T` | T&rarr;C 510, T&rarr;G 76, T&rarr;A 24 | `B` (96.1%) | 610 | 62.8% | 59-67% | 186,237 | 70.4% | 70-71% | 7.7% |  |
| forward | 9 | 12 | `Y` | Y&rarr;A 2,665, Y&rarr;G 476 | hypervariable | 3,141 | 63.1% | 61-65% | 183,706 | 70.5% | 70-71% | 7.5% |  |
| probe | 19 | 6 | `G` | G&rarr;C 425, G&rarr;A 10, G&rarr;T 8 | `S` (95.9%) | 443 | 63.0% | 58-67% | 186,404 | 70.4% | 70-71% | 7.5% |  |
| reverse | 11 | 12 | `G` | G&rarr;A 1,148, G&rarr;C 7, G&rarr;T 2 | `R` (99.2%) | 1,157 | 69.3% | 67-72% | 185,690 | 70.4% | 70-71% | 1.1% |  |
| reverse | 8 | 15 | `G` | G&rarr;A 108, G&rarr;T 4, G&rarr;C 1 | `R` (95.6%) | 113 | 72.6% | 64-80% | 186,734 | 70.4% | 70-71% | -2.2% |  |
| probe | 16 | 9 | `C` | C&rarr;A 38, C&rarr;T 36, C&rarr;G 3 | `H` (96.1%) | 77 | 74.0% | 63-83% | 186,770 | 70.4% | 70-71% | -3.6% |  |
| reverse | 20 | 3 | `A` | A&rarr;G 358, A&rarr;T 37, A&rarr;C 12 | `D` (97.1%) | 407 | 77.4% | 73-81% | 186,440 | 70.4% | 70-71% | -7.0% |  |
| forward | 19 | 2 | `G` | G&rarr;A 4,930, G&rarr;T 18, G&rarr;C 3 | `R` (99.6%) | 4,951 | 79.1% | 78-80% | 181,896 | 70.2% | 70-70% | -8.9% |  |
| probe | 4 | 21 | `G` | G&rarr;A 541, G&rarr;T 1, G&rarr;C 1 | `R` (99.6%) | 543 | 83.6% | 80-86% | 186,304 | 70.4% | 70-71% | -13.2% | yes |
| reverse | 18 | 5 | `T` | T&rarr;G 22, T&rarr;C 10, T&rarr;A 3 | hypervariable | 35 | 85.7% | 71-94% | 186,812 | 70.4% | 70-71% | -15.3% |  |
| probe | 23 | 2 | `T` | T&rarr;C 362, T&rarr;G 7, T&rarr;A 1 | `Y` (97.8%) | 370 | 86.8% | 83-90% | 186,477 | 70.4% | 70-71% | -16.4% |  |
| forward | 6 | 15 | `A` | A&rarr;T 202, A&rarr;C 176, A&rarr;G 1 | `H` (99.7%) | 379 | 86.8% | 83-90% | 186,468 | 70.4% | 70-71% | -16.4% |  |
| reverse | 21 | 2 | `C` | C&rarr;G 18, C&rarr;T 16, C&rarr;A 5 | hypervariable | 39 | 87.2% | 73-94% | 186,808 | 70.4% | 70-71% | -16.8% |  |
| probe | 9 | 16 | `T` | T&rarr;C 1,637, T&rarr;G 2 | `Y` (99.9%) | 1,639 | 87.6% | 86-89% | 185,208 | 70.3% | 70-70% | -17.3% |  |
| reverse | 14 | 9 | `T` | T&rarr;C 48, T&rarr;A 4 | `H` | 52 | 88.5% | 77-95% | 186,795 | 70.4% | 70-71% | -18.1% |  |
| probe | 17 | 8 | `T` | T&rarr;C 57, T&rarr;G 34, T&rarr;A 10 | hypervariable | 101 | 90.1% | 83-95% | 186,746 | 70.4% | 70-71% | -19.7% |  |
| probe | 22 | 3 | `C` | C&rarr;T 491, C&rarr;A 35, C&rarr;G 5 | `H` (99.1%) | 531 | 93.0% | 91-95% | 186,316 | 70.3% | 70-71% | -22.7% |  |
| reverse | 5 | 18 | `A` | A&rarr;G 1,478, A&rarr;T 5, A&rarr;C 1 | `R` (99.6%) | 1,484 | 93.3% | 92-94% | 185,363 | 70.2% | 70-70% | -23.0% | yes |
| probe | 20 | 5 | `G` | G&rarr;A 46, G&rarr;C 1, G&rarr;T 1 | `R` (95.8%) | 48 | 93.8% | 83-98% | 186,799 | 70.4% | 70-71% | -23.3% |  |
| forward | 4 | 17 | `G` | G&rarr;A 479, G&rarr;T 2 | `R` (99.6%) | 481 | 96.5% | 94-98% | 186,366 | 70.3% | 70-71% | -26.1% | yes |
| probe | 18 | 7 | `Y` | Y&rarr;G 370, Y&rarr;A 67 | hypervariable | 437 | 96.6% | 94-98% | 186,410 | 70.4% | 70-71% | -26.2% |  |
| reverse | 22 | 1 | `G` | G&rarr;T 22, G&rarr;C 6, G&rarr;A 3 | hypervariable | 31 | 96.8% | 84-99% | 186,816 | 70.4% | 70-71% | -26.4% |  |
| reverse | 17 | 6 | `G` | G&rarr;A 401, G&rarr;T 7 | `R` (98.3%) | 408 | 98.8% | 97-99% | 186,439 | 70.4% | 70-71% | -28.4% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 105,255 | detect | 2023×6554, 2024×15059, 2025×21228, 2026×15123 | Influenza×105252, Mutant×2, Influenza virus×1 | `QB115735`, `QB115727`, `QB115720`, `QB115712`, `QB115704`, `QB115696` (+105,249) |
| fwd 20; prb 1,7,14 | 29,965 | fail | 2023×4515, 2024×5601, 2025×8957, 2026×10493 | Influenza×29965 | `QB122958`, `QB122950`, `QB122942`, `QB122934`, `QB122926`, `QB122918` (+29,959) |
| fwd 20; prb 7,14 | 22,201 | fail | 2023×889, 2024×1112, 2025×2248, 2026×1265 | Influenza×22201 | `QB121828`, `PX414946`, `PX414942`, `PX414941`, `PX414940`, `PX414939` (+22,195) |
| fwd 20; prb 7 | 10,979 | reduced | 2023×48, 2024×244, 2025×957, 2026×32 | Influenza×10979 | `PZ647098`, `PZ647019`, `PZ646987`, `PZ645592`, `PZ115402`, `PZ114970` (+10,973) |
| fwd 19 | 2,752 | detect | 2023×23, 2024×159, 2025×233, 2026×91 | Influenza×2752 | `QB056936`, `QB056920`, `QB055424`, `QB004395`, `QB004389`, `QB004365` (+2,746) |
| rev 5 | 1,382 | reduced | 2023×371, 2024×171, 2025×496, 2026×273 | Influenza×1382 | `QB026294`, `QB026286`, `QB026278`, `QB026206`, `QB026070`, `QB026062` (+1,376) |
| prb 9 | 1,164 | reduced | 2020×14, 2023×1, 2025×1, 2026×2 | Influenza×1164 | `PZ576492`, `PZ573169`, `PX671144`, `OQ535154`, `KU976822`, `MW109689` (+1,158) |
| fwd 9 | 1,156 | detect | 2023×27, 2024×58, 2025×102, 2026×23 | Influenza×1156 | `QB026190`, `QB004144`, `QB004122`, `PZ932579`, `PZ932504`, `PQ489902` (+1,150) |

## SARCOCYSTIS_18S_5_8s_rDNA_short_Kutkiene_2010

Sarcocystis (taxid 5812) — status **low coverage** — 190 evaluable of 30,869 screened records

- forward: `5'-ATTGAGTGTTCCGGTGAATTA-3'` (21 nt)
- reverse: `5'-GGGATTCARTKGYYGAAA-3'` (18 nt)

**71 of 190 evaluable records (37%) share one mismatch pattern, mostly Sarcocystis miescheriana, deposited 2015-2025, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 8 | 11 | `K` | K&rarr;C 76, K&rarr;A 3 | `B` (96.2%) | 79 | 3.8% | 1-11% | 111 | 82.9% | 75-89% | 79.1% |  |
| reverse | 16 | 3 | `G` | G&rarr;A 84, G&rarr;C 6, G&rarr;T 1 | `V` (98.9%) | 91 | 11.0% | 6-19% | 99 | 85.9% | 78-91% | 74.9% |  |
| reverse | 15 | 4 | `A` | A&rarr;C 87, A&rarr;T 5, A&rarr;G 3 | `H` (96.8%) | 95 | 12.6% | 7-21% | 95 | 87.4% | 79-93% | 74.7% |  |
| reverse | 14 | 5 | `T` | T&rarr;A 85, T&rarr;C 2, T&rarr;G 2 | `W` (95.5%) | 89 | 13.5% | 8-22% | 101 | 82.2% | 74-88% | 68.7% |  |
| reverse | 18 | 1 | `G` | G&rarr;A 86, G&rarr;C 2 | `R` (97.7%) | 88 | 13.6% | 8-22% | 102 | 81.4% | 73-88% | 67.7% |  |
| reverse | 11 | 8 | `A` | A&rarr;C 85, A&rarr;G 1 | `M` (98.8%) | 86 | 15.1% | 9-24% | 104 | 78.8% | 70-86% | 63.7% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 78 | detect | 2020×5, 2021×6, 2023×4, 2024×6 | Sarcocystis lutrae×33, Sarcocystis lari×12, Sarcocystis halieti×8 | `CAXOTS010000019`, `CAXOTS010000032`, `CAXOTS010000033`, `CAXOTS010000034`, `CAXOTS010000037`, `CAXOTS010000054` (+72) |
| rev 8,11,14,15,16,18 | 71 | fail | 2017×4, 2018×7, 2019×20, 2025×2 | Sarcocystis miescheriana×16, Sarcocystis sinensis×16, Sarcocystis bovini×9 | `PV470858`, `PV470857`, `MH590230`, `MK867470`, `MK867469`, `MK867468` (+65) |
| rev 11,14,15,16,18 | 9 | reduced | 2016×9 | Sarcocystis zamani×9 | `KU244528`, `KU244527`, `KU244526`, `KU244525`, `KU244524`, `KU244523` (+3) |
| rev 2,3,4,5 | 4 | fail | 2025×4 | Sarcocystis chenggongensis×4 | `PX632651`, `PX632650`, `PX632649`, `PX632648` |
| fwd 3,8,9,17,18,21; rev 10,12,13,15,16,17 | 3 | fail | 2000×1, 2002×2 | SnEST4b04b12.y1 cSn×1, SnEST4a46a11.y1 cSn×1, SnEST4a06d08.y1 cSn×1 | `BU086209`, `BM303981`, `BE635461` |
| rev 3,4,9 | 3 | reduced | 2017×3 | Sarcocystis dehongensis×3 | `KY711380`, `KY711379`, `KY711378` |
| rev 8,11,14,15,18 | 3 | reduced | 2015×3 | Sarcocystis sinensis×3 | `KT901180`, `KT901178`, `KT901177` |
| fwd 4; rev 8,11,14,15,16,18 | 2 | fail | 2018×2 | Sarcocystis arieticanis×2 | `MH413044`, `MH413043` |

## Paramyxovirinae_Polymerase_L_gene_round2

Paramyxoviridae (taxid 11158) — status **low coverage** — 8,712 evaluable of 15,440 screened records

- forward: `5'-GTTGCTTCAATGGTTCARGGNGAYAA-3'` (26 nt)
- reverse: `5'-GCTGAAGTTACIGGITCICCDATRTTNC-3'` (28 nt)

**2,276 of 8,712 evaluable records (26%) share one mismatch pattern, mostly Measles virus, deposited 1995-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 24 | 5 | `A` | A&rarr;C 2,264, A&rarr;T 1,877 | `H` | 4,141 | 0.2% | 0-0% | 4,571 | 64.4% | 63-66% | 64.3% |  |
| reverse | 26 | 3 | `T` | T&rarr;A 3,245, T&rarr;G 547, T&rarr;C 171, +1 more | `D` (95.7%) | 3,964 | 1.2% | 1-2% | 4,748 | 61.2% | 60-63% | 59.9% |  |
| reverse | 19 | 10 | `A` | A&rarr;G 1,863, A&rarr;C 1,846 | `V` | 3,709 | 0.1% | 0-0% | 5,003 | 59.0% | 58-60% | 59.0% |  |
| forward | 21 | 6 | `T` | T&rarr;C 2,080, T&rarr;A 1,371, T&rarr;G 156 | `H` (95.7%) | 3,607 | 0.6% | 0-1% | 5,105 | 57.4% | 56-59% | 56.8% |  |
| reverse | 20 | 9 | `T` | T&rarr;C 2,176, T&rarr;G 449, T&rarr;A 218 | hypervariable | 2,843 | 0.5% | 0-1% | 5,869 | 50.1% | 49-51% | 49.7% |  |
| forward | 24 | 3 | `T` | T&rarr;G 1,622, T&rarr;C 527, T&rarr;A 384 | hypervariable | 2,533 | 0.0% | 0-0% | 6,179 | 47.8% | 47-49% | 47.8% |  |
| forward | 20 | 7 | `T` | T&rarr;G 2,290, T&rarr;A 126 | `D` | 2,416 | 0.6% | 0-1% | 6,296 | 46.7% | 45-48% | 46.1% |  |
| forward | 23 | 4 | `G` | G&rarr;A 1,441, G&rarr;T 538 | `D` | 1,979 | 0.0% | 0-0% | 6,733 | 43.9% | 43-45% | 43.9% |  |
| forward | 19 | 8 | `C` | C&rarr;G 1,980 | `S` | 1,980 | 0.1% | 0-0% | 6,732 | 43.9% | 43-45% | 43.7% |  |
| reverse | 22 | 7 | `G` | G&rarr;A 1,955 | `R` | 1,955 | 0.0% | 0-0% | 6,757 | 43.7% | 43-45% | 43.7% |  |
| reverse | 21 | 8 | `T` | T&rarr;C 1,955, T&rarr;A 64 | `Y` (96.8%) | 2,019 | 2.3% | 2-3% | 6,693 | 43.4% | 42-45% | 41.1% |  |
| reverse | 18 | 11 | `C` | C&rarr;A 1,423, C&rarr;T 58, C&rarr;G 9 | `M` (95.5%) | 1,490 | 0.0% | 0-0% | 7,222 | 40.9% | 40-42% | 40.9% |  |
| forward | 22 | 5 | `C` | C&rarr;T 112, C&rarr;G 2 | `Y` (98.2%) | 114 | 0.0% | 0-3% | 8,598 | 34.4% | 33-35% | 34.4% |  |
| forward | 18 | 9 | `A` | A&rarr;C 1,395, A&rarr;G 1,329, A&rarr;T 967, +1 more | hypervariable | 3,692 | 17.9% | 17-19% | 5,020 | 45.7% | 44-47% | 27.8% |  |
| reverse | 25 | 4 | `G` | G&rarr;C 62 | `S` | 62 | 16.1% | 9-27% | 8,650 | 34.0% | 33-35% | 17.9% |  |
| forward | 12 | 15 | `T` | T&rarr;G 3,378, T&rarr;A 1,563, T&rarr;C 1,379 | hypervariable | 6,320 | 36.8% | 36-38% | 2,392 | 26.2% | 24-28% | -10.7% |  |
| reverse | 23 | 6 | `A` | A&rarr;T 4,510, A&rarr;G 685, A&rarr;C 411 | hypervariable | 5,606 | 52.4% | 51-54% | 3,106 | 0.5% | 0-1% | -52.0% |  |
| reverse | 27 | 2 | `C` | C&rarr;A 4,790, C&rarr;T 14 | `M` (99.7%) | 4,804 | 60.2% | 59-62% | 3,908 | 1.6% | 1-2% | -58.7% |  |
| forward | 26 | 1 | `G` | G&rarr;A 4,735 | `R` | 4,735 | 61.1% | 60-62% | 3,977 | 1.5% | 1-2% | -59.6% |  |
| forward | 17 | 10 | `A` | A&rarr;T 3,644, A&rarr;C 723, A&rarr;G 250 | hypervariable | 4,617 | 62.7% | 61-64% | 4,095 | 1.5% | 1-2% | -61.2% |  |
| forward | 15 | 12 | `G` | G&rarr;A 3,842, G&rarr;T 646, G&rarr;C 12 | `D` (99.7%) | 4,500 | 64.2% | 63-66% | 4,212 | 1.6% | 1-2% | -62.6% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 12,15,17,26; rev 23,27 | 2,276 | reduced | 2023×33, 2024×107, 2025×483, 2026×1464 | Measles virus×2223, Measles morbillivirus×33, Morbillivirus hominis×19 | `QB035549`, `QB035548`, `QB035547`, `QB035545`, `QB035544`, `QB035541` (+2,270) |
| fwd 20,23,24; rev 18,19,21,22,24,26 | 1,215 | fail | 2023×53, 2024×237, 2025×430, 2026×74 | Human respirovirus×1092, Human parainfluenza×113, Respirovirus pneumoniae×6 | `PZ892266`, `PZ892265`, `PZ892264`, `PZ892263`, `PZ892262`, `PZ892261` (+1,209) |
| fwd 12,18,19,21; rev 19,20,24,26 | 679 | fail | 2023×25, 2024×34, 2025×77, 2026×27 | Avian paramyxovirus×366, Newcastle disease×159, Pigeon paramyxovirus×79 | `PQ067333`, `PQ067332`, `PZ519057`, `PV958090`, `PZ619957`, `PZ619956` (+673) |
| fwd 15,17,18,26; rev 23,27 | 598 | reduced | 2023×54, 2024×16, 2025×178, 2026×291 | Measles virus×390, Morbillivirus hominis×148, Measles morbillivirus×60 | `QB035546`, `QB035543`, `QB035542`, `PZ891940`, `PZ891939`, `PZ891935` (+592) |
| fwd 12,18,19,21; rev 19,20,23,24,26 | 497 | fail | 2023×27, 2024×22, 2025×53, 2026×14 | Avian paramyxovirus×352, Newcastle disease×72, Avian orthoavulavirus×28 | `PZ339900`, `PZ173234`, `PZ173230`, `PZ338776`, `LC874215`, `LC874214` (+491) |
| fwd 12,15,17,18,26; rev 23,27 | 409 | fail | 2022×98, 2024×13, 2025×9, 2026×119 | Measles virus×399, Measles morbillivirus×4, Morbillivirus hominis×3 | `QB075716`, `QB017949`, `PZ885218`, `PZ891938`, `PZ891937`, `PZ891936` (+403) |
| fwd 12,15,17,18,21,26; rev 23,27 | 249 | fail | 2018×2, 2020×2, 2022×142, 2023×88 | Measles virus×249 | `ON035993`, `ON035992`, `ON035991`, `ON035990`, `ON035989`, `ON035988` (+243) |
| fwd 12,20,21,23,24; rev 19,21,22,24 | 239 | fail | 2023×7, 2024×95, 2025×46, 2026×6 | Human respirovirus×172, Human parainfluenza×61, Respirovirus laryngotracheitidis×5 | `PZ055831`, `PZ244843`, `PZ210092`, `PX731599`, `PX731583`, `PX731580` (+233) |

## FILOVIRUS_ssRNA_L_gene

Filoviridae (taxid 11266) — status **declining** — 3,931 evaluable of 4,686 screened records

- forward: `5'-TATTCTCYCTACAAAAGCATTGGG-3'` (24 nt)
- reverse: `5'-GCTTCTGCGAGTGTTTGGACATT-3'` (23 nt)

**2,246 of 3,931 evaluable records (57%) share one mismatch pattern, mostly Zaire ebolavirus, deposited 2014-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 12 | 12 | `T` | T&rarr;A 86, T&rarr;C 2 | `W` (97.7%) | 88 | 0.0% | 0-4% | 3,843 | 99.7% | 99-100% | 99.7% |  |
| forward | 20 | 5 | `C*` | C&rarr;T 94, T&rarr;C 1 | - | 95 | 9.5% | 5-17% | 3,836 | 99.6% | 99-100% | 90.1% |  |
| reverse | 13 | 11 | `G` | G&rarr;A 86 | `R` | 86 | 10.5% | 6-19% | 3,845 | 99.4% | 99-100% | 88.9% |  |
| forward | 16 | 9 | `C*` | C&rarr;G 77, G&rarr;T 23, G&rarr;A 14, +3 more | - | 123 | 28.5% | 21-37% | 3,808 | 99.7% | 99-100% | 71.2% |  |
| reverse | 15 | 9 | `G*` | A&rarr;T 68, G&rarr;A 23, G&rarr;T 12, +2 more | - | 115 | 28.7% | 21-38% | 3,816 | 99.5% | 99-100% | 70.8% |  |
| forward | 23 | 2 | `A` | A&rarr;G 99, A&rarr;C 11, A&rarr;T 3 | `V` (97.3%) | 113 | 29.2% | 22-38% | 3,818 | 99.4% | 99-100% | 70.2% |  |
| forward | 17 | 8 | `Y*` | C&rarr;A 142, Y&rarr;A 78, T&rarr;A 10, +2 more | - | 239 | 62.8% | 56-69% | 3,692 | 99.7% | 99-100% | 36.9% |  |
| forward | 11 | 14 | `A` | A&rarr;G 32 | `R` | 32 | 78.1% | 61-89% | 3,899 | 97.6% | 97-98% | 19.5% |  |
| forward | 14 | 11 | `A*` | T&rarr;A 2,264, T&rarr;C 158, A&rarr;G 75, +1 more | - | 2,502 | 96.5% | 96-97% | 1,429 | 99.0% | 98-99% | 2.5% |  |
| forward | 8 | 17 | `G` | G&rarr;A 71 | `R` | 71 | 97.2% | 90-99% | 3,860 | 97.4% | 97-98% | 0.3% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 14 | 2,246 | detect | 2019×224, 2021×18, 2023×22, 2026×8 | Zaire ebolavirus×2240, Orthoebolavirus zairense×4, Sequence×1 | `PZ867532`, `PZ867531`, `PZ867530`, `PZ867529`, `OZ538128`, `OZ538127` (+2,240) |
| no mismatches | 1,326 | detect | 2023×12, 2024×76, 2025×15, 2026×15 | Zaire ebolavirus×1071, Ebola virus×107, Sequence×29 | `OZ556707`, `OZ556706`, `OZ556703`, `OZ556702`, `OZ556700`, `OZ556699` (+1,320) |
| fwd 14,17 | 142 | detect | 2021×2, 2022×1, 2023×119, 2025×2 | Sudan ebolavirus×136, Sequence×3, Zaire ebolavirus×2 | `OZ222062`, `PD166168`, `OQ673069`, `OQ673068`, `OQ673066`, `OQ673065` (+136) |
| fwd 14,16,17,20,23; rev 12,13,15 | 68 | fail | 2020×17, 2021×2, 2022×1, 2026×35 | Bundibugyo virus×59, Bundibugyo ebolavirus×7, Sequence×2 | `OZ542751`, `OZ538125`, `OZ538124`, `OZ538122`, `OZ538121`, `OZ538117` (+62) |
| fwd 8 | 44 | detect | 2015×3, 2017×1, 2018×1, 2019×3 | Marburg marburgvirus×31, Lake×5, Mutant×4 | `MK271062`, `MH638315`, `MH638314`, `MG725616`, `KP985768`, `KP117261` (+38) |
| fwd 8,11 | 25 | reduced | 2024×18, 2025×5, 2026×2 | Orthomarburgvirus marburgense×25 | `PZ112889`, `PZ112888`, `PV700541`, `PV700540`, `PV700539`, `PV700538` (+19) |
| fwd 14,16,23; rev 15 | 22 | reduced | 2017×1, 2020×1, 2022×1, 2025×2 | Lake×10, Sequence×4, Marburg marburgvirus×3 | `PD166177`, `PD166176`, `OK572966`, `MT321489`, `NC_024781`, `KU059750` (+16) |
| fwd 14,16,17,20,23; rev 12,15,18 | 7 | fail | 2015×1, 2017×1, 2018×1, 2022×1 | Tai×4, Sequence×2, Cote d'Ivoire×1 | `OK573000`, `MH121167`, `NC_014372`, `MS811583`, `KU182910`, `JA489027` (+1) |

## AVIPOXVIRUS_dsDNA_4b_core_Farias_2010

Avipoxvirus (taxid 10260) — status **low coverage** — 251 evaluable of 1,734 screened records

- forward: `5'-TCCTTGTAAAAGCGATACAGGAA-3'` (23 nt)
- reverse: `5'-CCCCTTAACATGTGCTAACAA-3'` (21 nt)
- probe: `5'-CAGCGTGATGAAGACGCTAA-3'` (20 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 20 | 1 | `C` | C&rarr;T 39 | `Y` | 39 | 0.0% | 0-9% | 212 | 95.8% | 92-98% | 95.8% |  |
| probe | 17 | 4 | `C` | C&rarr;T 43 | `Y` | 43 | 2.3% | 0-12% | 208 | 97.1% | 94-99% | 94.8% |  |
| forward | 11 | 13 | `C` | C&rarr;A 28, C&rarr;T 2, C&rarr;G 1 | `H` (96.8%) | 31 | 0.0% | 0-11% | 220 | 92.3% | 88-95% | 92.3% |  |
| reverse | 9 | 13 | `T` | T&rarr;A 27, T&rarr;C 4 | `H` | 31 | 0.0% | 0-11% | 220 | 92.3% | 88-95% | 92.3% |  |
| forward | 3 | 21 | `G` | G&rarr;A 29 | `R` | 29 | 0.0% | 0-12% | 222 | 91.4% | 87-94% | 91.4% | yes |
| reverse | 3 | 19 | `C` | C&rarr;T 29 | `Y` | 29 | 0.0% | 0-12% | 222 | 91.4% | 87-94% | 91.4% | yes |
| forward | 10 | 14 | `G` | G&rarr;A 28 | `R` | 28 | 0.0% | 0-12% | 223 | 91.0% | 87-94% | 91.0% |  |
| probe | 18 | 3 | `G` | G&rarr;A 27, G&rarr;C 1 | `R` (96.4%) | 28 | 0.0% | 0-12% | 223 | 91.0% | 87-94% | 91.0% |  |
| forward | 2 | 22 | `A` | A&rarr;T 27 | `W` | 27 | 0.0% | 0-12% | 224 | 90.6% | 86-94% | 90.6% | yes |
| forward | 13 | 11 | `A` | A&rarr;G 27 | `R` | 27 | 0.0% | 0-12% | 224 | 90.6% | 86-94% | 90.6% |  |
| reverse | 4 | 18 | `A` | A&rarr;G 27 | `R` | 27 | 0.0% | 0-12% | 224 | 90.6% | 86-94% | 90.6% | yes |
| probe | 2 | 19 | `A` | A&rarr;G 27 | `R` | 27 | 0.0% | 0-12% | 224 | 90.6% | 86-94% | 90.6% | yes |
| probe | 14 | 7 | `G` | G&rarr;A 30 | `R` | 30 | 6.7% | 2-21% | 221 | 91.0% | 86-94% | 84.3% |  |
| reverse | 18 | 4 | `C` | C&rarr;T 50 | `Y` | 50 | 18.0% | 10-31% | 201 | 96.5% | 93-98% | 78.5% |  |
| reverse | 21 | 1 | `C` | C&rarr;T 43 | `Y` | 43 | 20.9% | 11-35% | 208 | 93.3% | 89-96% | 72.3% |  |
| probe | 5 | 16 | `G` | G&rarr;A 21, G&rarr;T 10, G&rarr;C 1 | `D` (96.9%) | 32 | 28.1% | 16-45% | 219 | 88.6% | 84-92% | 60.5% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 185 | detect | 2022×14, 2023×28, 2024×7, 2025×14 | Avipoxvirus isolate×82, Avipoxvirus sp.×51, Avipoxvirus×25 | `PQ790040`, `PQ790039`, `PQ790038`, `PQ790037`, `PQ790036`, `PQ790035` (+179) |
| fwd 2,3,10,11,13; rev 3,4,9,18,21; prb 2,14,17,18,20 | 19 | fail | 2018×1, 2019×1, 2025×1, 2026×5 | Avipoxvirus sp.×7, Avipoxvirus×5, Canarypox virus×4 | `PZ162756`, `PZ162755`, `PZ162754`, `PZ162753`, `PZ162752`, `PV976819` (+13) |
| rev 18,21; prb 5 | 9 | reduced | 2016×6, 2018×2, 2023×1 | Fowlpox virus×8, Avipoxvirus sp.×1 | `ON568588`, `MH175236`, `MH175220`, `LC055563`, `LC055562`, `LC055561` (+3) |
| fwd 2,3,10,11,13; rev 3,4,9,18,21; prb 2,5,14,17,18,20 | 7 | fail | 2006×1, 2013×4, 2022×1, 2026×1 | Avipoxvirus isolate×4, Avipoxvirus sp.×1, Mynahpox virus×1 | `PZ754544`, `MW864265`, `KC018067`, `KC018065`, `KC018064`, `KC018063` (+1) |
| fwd 15; rev 12,18; prb 4,5,8,17,20 | 6 | fail | 2013×5, 2018×1 | Brazilian penguinpox×5, Avipoxvirus sp.×1 | `KC588961`, `KC588958`, `KC588957`, `KC588956`, `KC588955`, `MH175228` |
| rev 18; prb 4,5,8,17,20 | 3 | fail | 2019×2, 2022×1 | Avipoxvirus sp.×3 | `MZ091383`, `MG189368`, `MG189367` |
| fwd 6,7,20; rev 9,12,21; prb 5,17 | 3 | fail | 2013×3 | Avipoxvirus isolate×2, Brazilian penguinpox×1 | `KF516679`, `KC018062`, `KC018061` |
| fwd 21; rev 6; prb 3,11,12,15 | 2 | fail | 2013×1, 2018×1 | Canarypox virus×2 | `MF102272`, `KC193679` |

## West_Nile_Virus_Envelope_glycoprotein_E_Lanciotti_2001

West Nile virus (taxid 11082) — status **declining** — 7,068 evaluable of 9,151 screened records

- forward: `5'-ACCAAGGCAATAGGAAGAACCA-3'` (22 nt)
- reverse: `5'-GTATGAAGGCGCCGCAGGAGTGA-3'` (23 nt)

**1,132 of 7,068 evaluable records (16%) share one mismatch pattern, mostly West, deposited 1993-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 20 | 4 | `T` | T&rarr;A 1,261, T&rarr;G 13, T&rarr;C 7 | `W` (98.4%) | 1,281 | 0.5% | 0-1% | 5,787 | 99.8% | 100-100% | 99.3% |  |
| forward | 11 | 12 | `A` | A&rarr;T 1,179, A&rarr;G 73, A&rarr;C 2 | `D` (99.8%) | 1,254 | 0.6% | 0-1% | 5,814 | 99.3% | 99-99% | 98.7% |  |
| forward | 5 | 18 | `A` | A&rarr;G 1,277 | `R` | 1,277 | 1.1% | 1-2% | 5,791 | 99.6% | 99-100% | 98.5% | yes |
| forward | 7 | 16 | `A` | A&rarr;T 1,163, A&rarr;C 19 | `W` (98.4%) | 1,182 | 0.1% | 0-0% | 5,886 | 98.2% | 98-99% | 98.1% |  |
| reverse | 8 | 16 | `A` | A&rarr;T 1,174, A&rarr;G 116, A&rarr;C 10 | `D` (99.2%) | 1,300 | 2.1% | 1-3% | 5,768 | 99.8% | 100-100% | 97.7% |  |
| reverse | 9 | 15 | `C` | C&rarr;A 1,167, C&rarr;T 1 | `M` (99.9%) | 1,168 | 0.3% | 0-1% | 5,900 | 97.9% | 98-98% | 97.7% |  |
| forward | 3 | 20 | `C` | C&rarr;T 1,161 | `Y` | 1,161 | 0.2% | 0-1% | 5,907 | 97.9% | 97-98% | 97.7% | yes |
| reverse | 17 | 7 | `A` | A&rarr;T 1,176, A&rarr;G 129, A&rarr;C 4 | `D` (99.7%) | 1,309 | 2.8% | 2-4% | 5,759 | 99.8% | 100-100% | 96.9% |  |
| forward | 17 | 6 | `G` | G&rarr;A 1,223, G&rarr;T 4 | `R` (99.7%) | 1,227 | 3.6% | 3-5% | 5,841 | 98.2% | 98-99% | 94.7% |  |
| reverse | 2 | 22 | `G` | G&rarr;T 1,168, G&rarr;A 68 | `D` | 1,236 | 5.2% | 4-7% | 5,832 | 98.0% | 98-98% | 92.9% | yes |
| forward | 12 | 11 | `T` | T&rarr;C 1,622 | `Y` | 1,622 | 21.8% | 20-24% | 5,446 | 99.7% | 99-100% | 77.8% |  |
| forward | 2 | 21 | `C` | C&rarr;T 116, C&rarr;A 4 | `Y` (96.7%) | 120 | 23.3% | 17-32% | 6,948 | 82.8% | 82-84% | 59.5% | yes |
| reverse | 5 | 19 | `A` | A&rarr;G 149, A&rarr;T 6 | `R` (96.1%) | 155 | 32.9% | 26-41% | 6,913 | 82.9% | 82-84% | 50.0% | yes |
| forward | 8 | 15 | `A` | A&rarr;T 14, A&rarr;G 8, A&rarr;C 3 | hypervariable | 25 | 32.0% | 17-52% | 7,043 | 82.0% | 81-83% | 50.0% |  |
| forward | 14 | 9 | `A` | A&rarr;G 34, A&rarr;T 13, A&rarr;C 3 | hypervariable | 50 | 44.0% | 31-58% | 7,018 | 82.1% | 81-83% | 38.1% |  |
| reverse | 14 | 10 | `C` | C&rarr;T 197, C&rarr;A 30, C&rarr;G 3 | `H` (98.7%) | 230 | 47.4% | 41-54% | 6,838 | 83.0% | 82-84% | 35.6% |  |
| reverse | 23 | 1 | `G` | G&rarr;A 35 | `R` | 35 | 68.6% | 52-81% | 7,033 | 81.9% | 81-83% | 13.3% |  |
| reverse | 11 | 13 | `C` | C&rarr;T 88, C&rarr;A 16, C&rarr;G 5 | `H` (95.4%) | 109 | 81.7% | 73-88% | 6,959 | 81.8% | 81-83% | 0.2% |  |
| forward | 22 | 1 | `A` | A&rarr;G 62, A&rarr;T 2 | `R` (96.9%) | 64 | 93.8% | 85-98% | 7,004 | 81.7% | 81-83% | -12.1% |  |
| forward | 21 | 2 | `C` | C&rarr;A 37 | `M` | 37 | 100.0% | 91-100% | 7,031 | 81.7% | 81-83% | -18.3% |  |
| reverse | 21 | 3 | `A` | A&rarr;G 32, A&rarr;T 5 | `D` | 37 | 100.0% | 91-100% | 7,031 | 81.7% | 81-83% | -18.3% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 4,833 | detect | 2023×656, 2024×587, 2025×258, 2026×7 | West×4781, Sequence×31, JP×16 | `PX404496`, `PX404495`, `PX597329`, `PX487095`, `PX487094`, `PQ220320` (+4,827) |
| fwd 3,5,7,11,12,17; rev 2,8,9,17,20 | 1,132 | fail | 2023×142, 2024×87, 2025×230, 2026×356 | West×1132 | `OZ545432`, `OZ545431`, `OZ538033`, `OZ538032`, `OZ538065`, `OZ538062` (+1,126) |
| fwd 12 | 284 | detect | 2023×29, 2024×7, 2025×19, 2026×8 | West×284 | `PX619839`, `PX619838`, `PX619837`, `PX619836`, `PX619835`, `PX619832` (+278) |
| rev 14 | 97 | detect | 2022×1, 2023×24, 2024×1, 2025×3 | West×97 | `OZ310105`, `OZ310074`, `PV126614`, `OZ201664`, `OQ721832`, `OQ721804` (+91) |
| rev 11 | 77 | detect | 2019×10, 2023×5, 2024×46, 2025×1 | West×75, Sequence×2 | `OZ309756`, `PQ005989`, `PQ005988`, `PQ005987`, `PQ005986`, `PQ005985` (+71) |
| fwd 22 | 58 | detect | 2010×2, 2023×22, 2025×25, 2026×9 | West×55, MAG×3 | `PZ437308`, `PZ437306`, `PZ437305`, `PZ266570`, `PZ266569`, `PZ266568` (+52) |
| fwd 2,5,11,12; rev 5,8,14,17,20 | 54 | fail | 2003×2, 2012×1, 2016×28, 2024×2 | Kunjin virus×52, West×2 | `LC802099`, `LC802098`, `KX394411`, `KX394410`, `KX394409`, `KX394408` (+48) |
| rev 2 | 53 | detect | 2023×8, 2024×4, 2025×6, 2026×7 | West×53 | `PZ437307`, `PZ437304`, `PZ266567`, `PZ266563`, `PZ260029`, `PZ260028` (+47) |

## BQCV_capsid_Rossi_2024

Triatovirus nigereginacellulae (black queen cell virus; the paper's name, renamed by ICTV) (taxid 3047684) — status **declining** — 1,208 evaluable of 1,596 screened records

- forward: `5'-GTGCGGGAGATGATATGGA-3'` (19 nt)
- reverse: `5'-CCGTCTGAGATGCATGAATAC-3'` (21 nt)
- probe: `5'-TTTCCATCTTTATCGGTACGC-3'` (21 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 2 | 20 | `G` | G&rarr;A 31, G&rarr;C 8 | `V` | 39 | 0.0% | 0-9% | 1,169 | 90.8% | 89-92% | 90.8% | yes |
| reverse | 3 | 19 | `T` | T&rarr;C 28 | `Y` | 28 | 0.0% | 0-12% | 1,180 | 89.9% | 88-92% | 89.9% | yes |
| reverse | 5 | 17 | `A` | A&rarr;G 40 | `R` | 40 | 5.0% | 1-17% | 1,168 | 90.7% | 89-92% | 85.7% | yes |
| reverse | 14 | 8 | `A` | A&rarr;G 31, A&rarr;T 9 | `D` | 40 | 5.0% | 1-17% | 1,168 | 90.7% | 89-92% | 85.7% |  |
| forward | 12 | 8 | `A` | A&rarr;T 28, A&rarr;C 11, A&rarr;G 3 | hypervariable | 42 | 7.1% | 2-19% | 1,166 | 90.7% | 89-92% | 83.6% |  |
| reverse | 13 | 9 | `G` | G&rarr;A 46, G&rarr;T 2 | `R` (95.8%) | 48 | 20.8% | 12-34% | 1,160 | 90.6% | 89-92% | 69.8% |  |
| probe | 8 | 14 | `C` | C&rarr;T 47, C&rarr;G 2 | `Y` (95.9%) | 49 | 22.4% | 13-36% | 1,159 | 90.6% | 89-92% | 68.1% |  |
| reverse | 2 | 20 | `A` | A&rarr;G 107 | `R` | 107 | 33.6% | 25-43% | 1,101 | 93.1% | 91-94% | 59.5% | yes |
| reverse | 20 | 2 | `C` | C&rarr;T 31, C&rarr;A 31, C&rarr;G 6 | hypervariable | 68 | 32.4% | 22-44% | 1,140 | 91.1% | 89-93% | 58.8% |  |
| forward | 6 | 14 | `T` | T&rarr;C 32 | `Y` | 32 | 31.2% | 18-49% | 1,176 | 89.4% | 87-91% | 58.1% |  |
| reverse | 17 | 5 | `C` | C&rarr;T 181, C&rarr;G 11 | `B` | 192 | 43.8% | 37-51% | 1,016 | 96.2% | 95-97% | 52.4% |  |
| reverse | 8 | 14 | `A` | A&rarr;G 53 | `R` | 53 | 43.4% | 31-57% | 1,155 | 89.9% | 88-91% | 46.5% |  |
| reverse | 11 | 11 | `T` | T&rarr;C 79, T&rarr;A 6 | `H` | 85 | 45.9% | 36-56% | 1,123 | 91.0% | 89-93% | 45.1% |  |
| forward | 18 | 2 | `T` | T&rarr;C 87, T&rarr;A 47, T&rarr;G 1 | `H` (99.3%) | 135 | 48.9% | 41-57% | 1,073 | 92.7% | 91-94% | 43.8% |  |
| forward | 15 | 5 | `G` | G&rarr;A 30, G&rarr;C 1, G&rarr;T 1 | `V` (96.9%) | 32 | 78.1% | 61-89% | 1,176 | 88.1% | 86-90% | 10.0% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 781 | detect | 2023×84, 2024×94, 2025×20, 2026×14 | Black queen×775, Triatovirus nigereginacellulae×2, Sequence×2 | `PZ547512`, `OR700106`, `OR700105`, `QT386057`, `QS360125`, `PX550095` (+775) |
| rev 17 | 61 | detect | 2022×1, 2023×1, 2024×31, 2025×1 | Black queen×61 | `PV904192`, `MT683326`, `MT683325`, `MT683324`, `MT683321`, `MT683317` (+55) |
| rev 2 | 36 | reduced | 2023×3, 2024×1, 2025×1, 2026×7 | Black queen×36 | `PZ682689`, `PZ547513`, `PZ547511`, `PZ547510`, `PX625596`, `PX625595` (+30) |
| fwd 18 | 33 | detect | 2021×13, 2022×1, 2024×3, 2025×2 | Black queen×33 | `PV664203`, `PV664158`, `MT648882`, `MT648876`, `ON648737`, `OR912388` (+27) |
| fwd 12,18; rev 3,11,13,14,17,20; prb 2,8 | 28 | fail | 2011×28 | Black queen×28 | `JN054434`, `JN054433`, `JN054432`, `JN054431`, `JN054430`, `JN054429` (+22) |
| rev 11 | 19 | detect | 2012×1, 2017×1, 2019×4, 2024×9 | Black queen×19 | `MT683333`, `MT683332`, `MT683331`, `MT683329`, `MT683328`, `MT683327` (+13) |
| rev 2,17 | 17 | fail | 2022×2, 2024×1, 2025×5, 2026×1 | Black queen×17 | `PZ682691`, `PV904198`, `PV904194`, `PV904191`, `PV904190`, `PV806692` (+11) |
| fwd 15,18 | 16 | detect | 2015×13, 2026×3 | Black queen×16 | `PX625598`, `PX625592`, `PX625590`, `KP675929`, `KP675928`, `KP675927` (+10) |

## Pan_hemoparasite_cytochrome_c_Hellgren_2004

Haemosporida (taxid 5819) — status **declining** — 6,475 evaluable of 32,039 screened records

- forward: `5'-CATATATTAAGAGAAITATGGAG-3'` (23 nt)
- reverse: `5'-ATAGAAAGATAAGAAATACCATTC-3'` (24 nt)

**1,750 of 6,475 evaluable records (27%) share one mismatch pattern, mostly Plasmodium falciparum, deposited 1993-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 12 | 13 | `G` | G&rarr;A 4,292 | `R` | 4,292 | 9.4% | 9-10% | 2,183 | 90.6% | 89-92% | 81.2% |  |
| forward | 18 | 6 | `A` | A&rarr;T 4,450, A&rarr;C 284, A&rarr;G 86 | `H` (98.2%) | 4,820 | 17.8% | 17-19% | 1,655 | 92.0% | 91-93% | 74.2% |  |
| reverse | 18 | 7 | `A` | A&rarr;T 4,883, A&rarr;G 9, A&rarr;C 6 | `W` (99.7%) | 4,898 | 19.7% | 19-21% | 1,577 | 89.9% | 88-91% | 70.2% |  |
| reverse | 9 | 16 | `A` | A&rarr;G 3,852 | `R` | 3,852 | 11.1% | 10-12% | 2,623 | 74.4% | 73-76% | 63.2% |  |
| reverse | 16 | 9 | `A` | A&rarr;G 6,086, A&rarr;C 121 | `R` (98.1%) | 6,207 | 34.4% | 33-36% | 268 | 91.4% | 87-94% | 57.0% |  |
| reverse | 21 | 4 | `G` | G&rarr;A 5,928 | `R` | 5,928 | 32.0% | 31-33% | 547 | 88.5% | 86-91% | 56.5% |  |
| reverse | 13 | 12 | `A` | A&rarr;G 1,816 | `R` | 1,816 | 3.0% | 2-4% | 4,659 | 49.9% | 48-51% | 46.9% |  |
| forward | 21 | 3 | `T` | T&rarr;C 2,494 | `Y` | 2,494 | 9.3% | 8-10% | 3,981 | 54.0% | 52-56% | 44.7% |  |
| forward | 2 | 22 | `A` | A&rarr;T 141, A&rarr;G 63 | `D` | 204 | 0.0% | 0-2% | 6,271 | 38.0% | 37-39% | 38.0% | yes |
| forward | 22 | 2 | `A` | A&rarr;C 61, A&rarr;T 57, A&rarr;G 1 | `H` (99.2%) | 119 | 0.0% | 0-3% | 6,356 | 37.4% | 36-39% | 37.4% |  |
| forward | 4 | 20 | `G` | G&rarr;A 64 | `R` | 64 | 0.0% | 0-6% | 6,411 | 37.1% | 36-38% | 37.1% | yes |
| forward | 12 | 12 | `A` | A&rarr;G 39 | `R` | 39 | 0.0% | 0-9% | 6,436 | 37.0% | 36-38% | 37.0% |  |
| forward | 23 | 1 | `C` | C&rarr;T 123 | `Y` | 123 | 1.6% | 0-6% | 6,352 | 37.4% | 36-39% | 35.8% |  |
| forward | 10 | 14 | `A` | A&rarr;G 68, A&rarr;T 1 | `R` (98.6%) | 69 | 1.4% | 0-8% | 6,406 | 37.1% | 36-38% | 35.7% |  |
| forward | 5 | 19 | `T` | T&rarr;A 65, T&rarr;C 1 | `W` (98.5%) | 66 | 1.5% | 0-8% | 6,409 | 37.1% | 36-38% | 35.6% | yes |
| forward | 3 | 21 | `G` | G&rarr;T 56, G&rarr;C 8, G&rarr;A 1 | `B` (98.5%) | 65 | 1.5% | 0-8% | 6,410 | 37.1% | 36-38% | 35.6% | yes |
| forward | 6 | 18 | `A` | A&rarr;G 41, A&rarr;C 2 | `R` (95.3%) | 43 | 9.3% | 4-22% | 6,432 | 36.9% | 36-38% | 27.6% |  |
| forward | 9 | 15 | `A` | A&rarr;G 613, A&rarr;T 2 | `R` (99.7%) | 615 | 12.0% | 10-15% | 5,860 | 39.4% | 38-41% | 27.3% |  |
| reverse | 15 | 10 | `T` | T&rarr;C 46 | `Y` | 46 | 23.9% | 14-38% | 6,429 | 36.8% | 36-38% | 12.9% |  |
| forward | 1 | 23 | `G` | G&rarr;A 139, G&rarr;C 59, G&rarr;T 1 | `V` (99.5%) | 199 | 36.2% | 30-43% | 6,276 | 36.8% | 36-38% | 0.6% | yes |
| reverse | 24 | 1 | `A` | A&rarr;G 100 | `R` | 100 | 48.0% | 38-58% | 6,375 | 36.6% | 35-38% | -11.4% |  |
| reverse | 3 | 22 | `T` | T&rarr;C 55, T&rarr;A 1 | `Y` (98.2%) | 56 | 91.1% | 81-96% | 6,419 | 36.3% | 35-37% | -54.8% | yes |
| forward | 17 | 7 | `T` | T&rarr;A 336, T&rarr;C 129, T&rarr;G 13 | `H` (97.3%) | 478 | 90.4% | 87-93% | 5,997 | 32.5% | 31-34% | -57.9% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 18,21; rev 9,12,13,16,18,21 | 1,750 | fail | 2023×17, 2024×1, 2025×37, 2026×4 | Plasmodium falciparum×1334, Plasmodium sp.×210, Plasmodium reichenowi×151 | `PZ698056`, `PX684229`, `PX684216`, `PX684208`, `PV806003`, `PV806000` (+1,744) |
| fwd 18; rev 9,12,16,18,21 | 1,562 | fail | 2023×23, 2024×4, 2025×32, 2026×4 | Plasmodium vivax×1043, Plasmodium sp.×133, Plasmodium cf.×118 | `PZ512988`, `PZ512987`, `LC909092`, `LC909091`, `PQ362418`, `PQ362417` (+1,556) |
| fwd 9,18,21; rev 12,16,18,21 | 484 | fail | 2016×66, 2017×33, 2022×167, 2025×12 | Plasmodium gaboni×260, Plasmodium sp.×181, Plasmodium adleri×30 | `PV805989`, `PV805985`, `PV805982`, `PV805958`, `PV805950`, `PV805949` (+478) |
| fwd 17; rev 16,18,21 | 261 | reduced | 2018×5, 2019×1, 2022×14, 2025×6 | Hepatocystis sp.×260, Leucocytozoon grallariae×1 | `PQ362391`, `PQ362390`, `PQ362387`, `PQ362386`, `PQ362385`, `PQ362384` (+255) |
| rev 16,21 | 228 | detect | 2023×15, 2024×5, 2025×32, 2026×4 | Plasmodium sp.×79, Haemoproteus sp.×30, Unidentified×21 | `PX123976`, `PX123975`, `LC909105`, `PV948515`, `PV948052`, `PV948051` (+222) |
| rev 16 | 171 | detect | 2023×21, 2024×2, 2025×44, 2026×2 | Haemoproteus sp.×113, Haemoproteus belopolskyi×10, Parahaemoproteus sp.×9 | `LC909096`, `LC867943`, `PV944104`, `PV944103`, `PV944102`, `PV944101` (+165) |
| fwd 18; rev 16,21 | 168 | reduced | 2019×30, 2022×2, 2023×3, 2025×30 | Plasmodium sp.×55, Haemosporida sp.×34, Plasmodium tupinambi×29 | `PV948024`, `PQ680073`, `PQ680072`, `PQ680071`, `PQ680070`, `PQ680069` (+162) |
| fwd 18; rev 9,16,18,21 | 141 | reduced | 2018×1, 2019×1, 2023×8, 2025×16 | Plasmodium sp.×108, Plasmodium inui×27, Plasmodium cynomolgi×4 | `PQ362415`, `PQ362414`, `PQ362413`, `PQ362412`, `PQ362411`, `PQ362410` (+135) |

## CDV_H_gene_Mueller_2011_1

Morbillivirus canis (formerly Canine morbillivirus) (taxid 3052342) — status **declining** — 512 evaluable of 4,013 screened records

- forward: `5'-GGGCTCAGGTAGTCCARCAA-3'` (20 nt)
- reverse: `5'-CCTCCGGAGAGTGCTGATAA-3'` (20 nt)

**59 of 512 evaluable records (12%) share one mismatch pattern, mostly Canine distemper, deposited 1997-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 1 | 20 | `A` | A&rarr;G 41 | `R` | 41 | 0.0% | 0-9% | 471 | 98.1% | 96-99% | 98.1% | yes |
| reverse | 3 | 18 | `T` | T&rarr;C 76, T&rarr;A 3 | `Y` (96.2%) | 79 | 53.2% | 42-64% | 433 | 97.0% | 95-98% | 43.8% | yes |
| reverse | 18 | 3 | `T` | T&rarr;C 119, T&rarr;A 4 | `Y` (96.7%) | 123 | 65.9% | 57-74% | 389 | 97.9% | 96-99% | 32.1% |  |
| reverse | 15 | 6 | `G` | G&rarr;A 167, G&rarr;C 38, G&rarr;T 5 | `V` (97.6%) | 210 | 79.0% | 73-84% | 302 | 98.0% | 96-99% | 19.0% |  |
| reverse | 2 | 19 | `A` | A&rarr;G 20 | `R` | 20 | 90.0% | 70-97% | 492 | 90.2% | 87-93% | 0.2% | yes |
| forward | 13 | 8 | `G` | G&rarr;A 64 | `R` | 64 | 90.6% | 81-96% | 448 | 90.2% | 87-93% | -0.4% |  |
| reverse | 16 | 5 | `C` | C&rarr;T 33 | `Y` | 33 | 97.0% | 85-99% | 479 | 89.8% | 87-92% | -7.2% |  |
| reverse | 12 | 9 | `G` | G&rarr;T 35, G&rarr;A 3 | `D` | 38 | 97.4% | 87-100% | 474 | 89.7% | 87-92% | -7.7% |  |
| reverse | 20 | 1 | `C` | C&rarr;G 90, C&rarr;T 6, C&rarr;A 1 | `B` (99.0%) | 97 | 96.9% | 91-99% | 415 | 88.7% | 85-91% | -8.2% |  |
| reverse | 9 | 12 | `T` | T&rarr;G 51 | `K` | 51 | 100.0% | 93-100% | 461 | 89.2% | 86-92% | -10.8% |  |
| reverse | 13 | 8 | `A` | A&rarr;T 55, A&rarr;G 5 | `D` | 60 | 100.0% | 94-100% | 452 | 88.9% | 86-92% | -11.1% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 105 | detect | 2023×2, 2024×1, 2025×1, 2026×12 | Morbillivirus canis×63, Canine distemper×39, Canine morbillivirus×2 | `PV167797`, `PX656924`, `PX656923`, `PX656922`, `PX656920`, `PX656919` (+99) |
| rev 20 | 59 | detect | 2022×1, 2023×2, 2025×2, 2026×1 | Canine distemper×38, Morbillivirus canis×19, Canine morbillivirus×1 | `PZ043805`, `PV778034`, `PV778033`, `OR514514`, `OR514513`, `LC338064` (+53) |
| rev 13,15 | 55 | detect | 2018×55 | Morbillivirus canis×55 | `MF953469`, `MF953468`, `MF953467`, `MF953466`, `MF953465`, `MF953464` (+49) |
| rev 1,3,15,18 | 33 | fail | 2005×1, 2018×5, 2020×3, 2026×24 | Morbillivirus canis×26, Canine distemper×7 | `PZ812018`, `PZ812017`, `PZ812016`, `PZ812015`, `PZ812014`, `PZ812013` (+27) |
| rev 9,12,15,18 | 32 | reduced | 2008×3, 2017×5, 2018×4, 2022×9 | Canine morbillivirus×9, Canine distemper×9, Morbillivirus canis×5 | `D00758`, `OL441602`, `OL441601`, `OL441600`, `OL441599`, `OL441598` (+26) |
| rev 3 | 29 | detect | 2021×1, 2024×4, 2025×2, 2026×14 | Morbillivirus canis×23, Canine distemper×6 | `PX734755`, `PX734753`, `PX734752`, `PX734751`, `PX734750`, `PX734749` (+23) |
| rev 15 | 24 | detect | 2018×1, 2019×3, 2022×4, 2026×7 | Morbillivirus canis×11, Canine distemper×9, Canine morbillivirus×4 | `PX610320`, `PX610319`, `PX789678`, `PX789674`, `OP209189`, `OP209188` (+18) |
| fwd 13; rev 15,16 | 19 | reduced | 2022×19 | Canine morbillivirus×19 | `OK557797`, `OK557796`, `OK557795`, `OK557794`, `OK557793`, `OK557792` (+13) |

## ORTHOREOVIRUS_dsRNA_RNA_polymerase_Landolfi_2010

Orthoreovirus (taxid 10882) — status **declining** — 1,033 evaluable of 14,531 screened records

- forward: `5'-GGBTCMACNGCYACYTCBACYGAGCA-3'` (26 nt)
- reverse: `5'-CCRTCRTCWCCYTGRCAKACRTARTT-3'` (26 nt)

**337 of 1,033 evaluable records (33%) share one mismatch pattern, mostly Piscine orthoreovirus, deposited 2013-2025, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 15 | 12 | `Y` | Y&rarr;G 267, Y&rarr;A 16 | hypervariable | 283 | 37.5% | 32-43% | 750 | 98.8% | 98-99% | 61.3% |  |
| forward | 12 | 15 | `Y` | Y&rarr;A 173, Y&rarr;G 167 | hypervariable | 340 | 46.8% | 42-52% | 693 | 99.3% | 98-100% | 52.5% |  |
| forward | 6 | 21 | `Y` | Y&rarr;G 489, Y&rarr;A 127 | hypervariable | 616 | 70.3% | 67-74% | 417 | 99.3% | 98-100% | 29.0% |  |
| forward | 21 | 6 | `M` | M&rarr;T 417, M&rarr;G 216 | hypervariable | 633 | 71.7% | 68-75% | 400 | 98.2% | 96-99% | 26.5% |  |
| reverse | 9 | 18 | `K` | K&rarr;A 489, K&rarr;C 349 | hypervariable | 838 | 78.8% | 76-81% | 195 | 95.9% | 92-98% | 17.1% |  |
| forward | 9 | 18 | `B` | B&rarr;A 27 | hypervariable | 27 | 66.7% | 48-81% | 1,006 | 82.4% | 80-85% | 15.7% |  |
| reverse | 18 | 9 | `W` | W&rarr;G 35, W&rarr;C 22 | hypervariable | 57 | 80.7% | 69-89% | 976 | 82.1% | 80-84% | 1.4% |  |
| forward | 3 | 24 | `G` | G&rarr;A 610 | `R` | 610 | 82.8% | 80-86% | 423 | 80.9% | 77-84% | -1.9% | yes |
| forward | 24 | 3 | `B` | B&rarr;A 109 | hypervariable | 109 | 92.7% | 86-96% | 924 | 80.7% | 78-83% | -11.9% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 3,6,21; rev 9 | 337 | reduced | 2019×9, 2020×108, 2021×13, 2025×182 | Piscine orthoreovirus×328, Piscine reovirus×6, Sequence×2 | `PV409545`, `PV409535`, `PV409525`, `PV409515`, `PV409505`, `PV409495` (+331) |
| rev 9 | 138 | detect | 2023×19, 2024×6, 2025×15, 2026×3 | Mammalian orthoreovirus×130, Orthoreovirus sp.×2, Cataraqui virus×1 | `PZ764064`, `PZ005679`, `PV855983`, `PX871018`, `PX401510`, `PX244563` (+132) |
| fwd 3,6,12,15,21; rev 9 | 87 | fail | 2023×3, 2024×1, 2025×57, 2026×4 | Avian orthoreovirus×86, Avian reovirus×1 | `PZ525050`, `PX942574`, `PX942566`, `PX942556`, `PV448237`, `PQ069026` (+81) |
| fwd 6,12,15,21; rev 9 | 73 | fail | 2015×2, 2023×11, 2024×9, 2025×44 | Avian orthoreovirus×73 | `PQ068936`, `PQ068926`, `PQ068916`, `PQ068906`, `PQ068896`, `PV406122` (+67) |
| fwd 3,6,12,15; rev 9 | 57 | reduced | 2023×6, 2024×9, 2025×4, 2026×10 | Avian orthoreovirus×56, Duck reovirus×1 | `OP313856`, `OP313846`, `OP302733`, `PZ206355`, `PZ112220`, `PZ112210` (+51) |
| fwd 21,24 | 44 | detect | 2023×7, 2024×11, 2025×3, 2026×3 | Duck reovirus×33, Avian orthoreovirus×5, Goose orthoreovirus×2 | `PZ332856`, `PZ123232`, `PQ567546`, `PZ016822`, `PV296163`, `PV296162` (+38) |
| fwd 24 | 41 | detect | 2024×41 | Mammalian orthoreovirus×41 | `LC818806`, `LC818796`, `LC818786`, `LC818772`, `LC818762`, `LC818752` (+35) |
| no mismatches | 32 | detect | 2022×1, 2023×1, 2025×3, 2026×3 | Mammalian orthoreovirus×24, Reovirus serotype×3, JP×2 | `QQ447910`, `QQ447907`, `PV818064`, `PV804332`, `AF368033`, `PV005835` (+26) |

## RHABDOVIRUS_ssRNA_L_gene_round1

Rhabdoviridae (taxid 11270) — status **declining** — 6,951 evaluable of 9,895 screened records

- forward: `5'-RAAGGYAGRTTTTTYKCDYTRATG-3'` (24 nt)
- reverse: `5'-CCADMCBTTTTGYCKYARRCCTTC-3'` (24 nt)

**720 of 6,951 evaluable records (10%) share one mismatch pattern, mostly Lyssavirus rabies, deposited 2008-2024, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 8 | 17 | `C` | C&rarr;G 277, C&rarr;A 6 | `S` (97.9%) | 283 | 0.0% | 0-1% | 6,668 | 75.3% | 74-76% | 75.3% |  |
| reverse | 16 | 9 | `T` | T&rarr;A 233, T&rarr;C 13, T&rarr;G 1 | `H` (99.6%) | 247 | 0.0% | 0-2% | 6,704 | 74.9% | 74-76% | 74.9% |  |
| reverse | 9 | 16 | `Y` | Y&rarr;G 473, Y&rarr;A 369 | hypervariable | 842 | 6.4% | 5-8% | 6,109 | 81.3% | 80-82% | 74.9% |  |
| forward | 4 | 21 | `R` | R&rarr;C 246, R&rarr;T 126, R&rarr;Y 1 | hypervariable | 373 | 1.6% | 1-3% | 6,578 | 76.2% | 75-77% | 74.6% | yes |
| reverse | 10 | 15 | `K` | K&rarr;A 239 | `D` | 239 | 0.4% | 0-2% | 6,712 | 74.8% | 74-76% | 74.4% |  |
| forward | 15 | 10 | `T` | T&rarr;G 234, T&rarr;A 161, T&rarr;C 28 | hypervariable | 423 | 3.1% | 2-5% | 6,528 | 76.7% | 76-78% | 73.6% |  |
| forward | 3 | 22 | `A` | A&rarr;T 23, A&rarr;C 23 | `H` | 46 | 0.0% | 0-8% | 6,905 | 72.7% | 72-74% | 72.7% | yes |
| forward | 1 | 24 | `G` | G&rarr;A 12, G&rarr;C 8, G&rarr;T 4 | hypervariable | 24 | 0.0% | 0-14% | 6,927 | 72.5% | 71-74% | 72.5% | yes |
| reverse | 17 | 8 | `T` | T&rarr;C 21, T&rarr;A 2 | `H` | 23 | 0.0% | 0-14% | 6,928 | 72.5% | 71-74% | 72.5% |  |
| forward | 14 | 11 | `T` | T&rarr;G 235, T&rarr;A 87 | `D` | 322 | 4.0% | 2-7% | 6,629 | 75.5% | 74-77% | 71.5% |  |
| forward | 9 | 16 | `K` | K&rarr;A 43 | `D` | 43 | 2.3% | 0-12% | 6,908 | 72.7% | 72-74% | 70.3% |  |
| reverse | 7 | 18 | `R` | R&rarr;T 39, R&rarr;C 10 | hypervariable | 49 | 4.1% | 1-14% | 6,902 | 72.7% | 72-74% | 68.6% |  |
| forward | 21 | 4 | `G` | G&rarr;C 183, G&rarr;T 6, G&rarr;A 1 | `S` (96.3%) | 190 | 8.9% | 6-14% | 6,761 | 74.0% | 73-75% | 65.1% |  |
| forward | 24 | 1 | `R` | R&rarr;T 80, R&rarr;C 39 | hypervariable | 119 | 9.2% | 5-16% | 6,832 | 73.3% | 72-74% | 64.1% |  |
| forward | 11 | 14 | `T` | T&rarr;A 33, T&rarr;C 3, T&rarr;G 1 | `H` (97.3%) | 37 | 10.8% | 4-25% | 6,914 | 72.6% | 71-74% | 61.8% |  |
| forward | 6 | 19 | `Y` | Y&rarr;A 20, Y&rarr;G 6 | hypervariable | 26 | 11.5% | 4-29% | 6,925 | 72.5% | 71-74% | 60.9% |  |
| forward | 20 | 5 | `G` | G&rarr;C 395, G&rarr;A 2 | `S` (99.5%) | 397 | 15.4% | 12-19% | 6,554 | 75.7% | 75-77% | 60.3% |  |
| reverse | 21 | 4 | `D` | D&rarr;C 488 | hypervariable | 488 | 18.0% | 15-22% | 6,463 | 76.3% | 75-77% | 58.3% |  |
| reverse | 12 | 13 | `Y` | Y&rarr;A 384, Y&rarr;G 290 | hypervariable | 674 | 22.6% | 20-26% | 6,277 | 77.6% | 77-79% | 55.0% |  |
| forward | 19 | 6 | `Y` | Y&rarr;G 652, Y&rarr;A 650 | hypervariable | 1,302 | 29.8% | 27-32% | 5,649 | 82.0% | 81-83% | 52.2% |  |
| reverse | 19 | 6 | `C` | C&rarr;A 32, C&rarr;T 7, C&rarr;G 3 | hypervariable | 42 | 21.4% | 12-36% | 6,909 | 72.5% | 71-74% | 51.1% |  |
| reverse | 20 | 5 | `M` | M&rarr;G 18, M&rarr;T 17 | hypervariable | 35 | 25.7% | 14-42% | 6,916 | 72.5% | 71-74% | 46.8% |  |
| forward | 16 | 9 | `R` | R&rarr;T 87, R&rarr;C 52 | hypervariable | 139 | 26.6% | 20-35% | 6,812 | 73.2% | 72-74% | 46.5% |  |
| forward | 23 | 2 | `A` | A&rarr;C 467, A&rarr;T 385, A&rarr;G 32 | `H` (96.4%) | 884 | 37.7% | 35-41% | 6,067 | 77.3% | 76-78% | 39.6% |  |
| forward | 13 | 12 | `T` | T&rarr;C 3,065, T&rarr;A 250, T&rarr;G 199 | hypervariable | 3,514 | 53.8% | 52-55% | 3,437 | 91.1% | 90-92% | 37.3% |  |
| reverse | 6 | 19 | `R` | R&rarr;C 1,754, R&rarr;T 1,314, R&rarr;Y 1 | hypervariable | 3,069 | 53.2% | 51-55% | 3,882 | 87.2% | 86-88% | 34.0% |  |
| forward | 22 | 3 | `A` | A&rarr;G 3,396, A&rarr;T 396, A&rarr;C 211 | hypervariable | 4,003 | 67.9% | 66-69% | 2,948 | 78.1% | 77-80% | 10.2% |  |
| forward | 7 | 18 | `D` | D&rarr;C 2,310 | hypervariable | 2,310 | 68.3% | 66-70% | 4,641 | 74.2% | 73-75% | 5.9% |  |
| reverse | 15 | 10 | `T` | T&rarr;C 4,930 | `Y` | 4,930 | 76.5% | 75-78% | 2,021 | 61.8% | 60-64% | -14.7% |  |
| reverse | 3 | 22 | `T` | T&rarr;C 4,915 | `Y` | 4,915 | 83.3% | 82-84% | 2,036 | 45.6% | 43-48% | -37.6% | yes |
| forward | 18 | 7 | `A` | A&rarr;C 4,829, A&rarr;G 3, A&rarr;T 1 | `M` (99.9%) | 4,833 | 85.5% | 84-86% | 2,118 | 42.0% | 40-44% | -43.5% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 18; rev 3,6,15 | 720 | reduced | 2020×38, 2022×58, 2023×3, 2024×11 | Lyssavirus rabies×719, Rabies virus×1 | `PP447332`, `PP447331`, `PP447330`, `PP447329`, `PP447328`, `PP447327` (+714) |
| fwd 13,18,22; rev 3,6,15 | 543 | reduced | 2021×8, 2023×85, 2024×122, 2025×47 | Lyssavirus rabies×457, Rabies virus×56, Rabies lyssavirus×30 | `PV855415`, `PV855414`, `PV855413`, `PV855412`, `PV855411`, `PV855410` (+537) |
| fwd 7,18; rev 3,15 | 524 | reduced | 2022×3, 2023×32, 2024×366, 2025×1 | Lyssavirus rabies×459, Rabies virus×60, Rabies lyssavirus×5 | `MG458304`, `PQ671590`, `OR971675`, `OR971674`, `OR971673`, `OR971672` (+518) |
| fwd 7,18,22; rev 3 | 423 | reduced | 2022×65, 2023×297, 2024×23, 2025×22 | Rabies virus×308, Lyssavirus rabies×111, Rabies lyssavirus×4 | `MG458314`, `PP736759`, `PV606732`, `PV606731`, `PV606730`, `PQ671603` (+417) |
| fwd 18,22; rev 3,15 | 415 | reduced | 2019×116, 2020×158, 2023×16, 2024×37 | Lyssavirus rabies×363, Rabies virus×51, Rabies lyssavirus×1 | `MG458319`, `MG458313`, `OR920350`, `OR920348`, `OR920307`, `OR920295` (+409) |
| fwd 7,13,18,22; rev 3,6,15 | 291 | fail | 2022×2, 2024×135, 2025×136, 2026×2 | Lyssavirus rabies×276, Rabies virus×9, Rabies lyssavirus×6 | `PZ334451`, `PX682069`, `OR045939`, `PV584369`, `PV584368`, `PV584367` (+285) |
| fwd 13,18,22; rev 3,15 | 219 | reduced | 2023×24, 2024×5, 2025×3, 2026×4 | Lyssavirus rabies×178, Rabies virus×30, Rabies lyssavirus×6 | `PV730233`, `OZ470011`, `NC_139265`, `PX789578`, `PV591864`, `MG458317` (+213) |
| fwd 13,18; rev 15 | 217 | reduced | 2021×15, 2022×1, 2023×2, 2026×1 | Rabies virus×164, Rabies lyssavirus×26, Lyssavirus rabies×24 | `PX991851`, `OQ068400`, `OP642459`, `OV696601`, `MT895968`, `MT895967` (+211) |

## Cryptosporidium_18SrDNA_Xiao_1999_round2

Cryptosporidium (taxid 5806) — status **low coverage** — 1,178 evaluable of 14,962 screened records

- forward: `5'-GGAAGGGTTGTATTTATTAGATAAAG-3'` (26 nt)
- reverse: `5'-AAGGAGTAAGGAACAACCTCCA-3'` (22 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 1 | 22 | `A` | A&rarr;C 61, A&rarr;T 4, A&rarr;G 2 | `H` (97.0%) | 67 | 0.0% | 0-5% | 1,111 | 96.7% | 95-98% | 96.7% | yes |
| reverse | 4 | 19 | `T` | T&rarr;C 61, T&rarr;A 2, T&rarr;G 1 | `Y` (95.3%) | 64 | 0.0% | 0-6% | 1,114 | 96.4% | 95-97% | 96.4% | yes |
| reverse | 5 | 18 | `C` | C&rarr;A 54, C&rarr;T 9, C&rarr;G 1 | `H` (98.4%) | 64 | 0.0% | 0-6% | 1,114 | 96.4% | 95-97% | 96.4% | yes |
| reverse | 2 | 21 | `C` | C&rarr;T 53, C&rarr;A 8 | `H` | 61 | 0.0% | 0-6% | 1,117 | 96.2% | 95-97% | 96.2% | yes |
| reverse | 21 | 2 | `A` | A&rarr;G 21, A&rarr;T 4 | `D` | 25 | 48.0% | 30-67% | 1,153 | 92.1% | 90-94% | 44.1% |  |
| reverse | 13 | 10 | `G` | G&rarr;A 15, G&rarr;C 13, G&rarr;T 1 | `V` (96.6%) | 29 | 55.2% | 38-72% | 1,149 | 92.1% | 90-94% | 36.9% |  |
| reverse | 19 | 4 | `G` | G&rarr;A 26, G&rarr;T 2, G&rarr;C 1 | `D` (96.6%) | 29 | 62.1% | 44-77% | 1,149 | 91.9% | 90-93% | 29.8% |  |
| forward | 19 | 8 | `T` | T&rarr;G 36, T&rarr;A 2 | `D` | 38 | 63.2% | 47-77% | 1,140 | 92.1% | 90-94% | 28.9% |  |
| reverse | 22 | 1 | `A` | A&rarr;T 13, A&rarr;G 10 | `D` | 23 | 65.2% | 45-81% | 1,155 | 91.7% | 90-93% | 26.5% |  |
| forward | 14 | 13 | `T` | T&rarr;A 47, T&rarr;G 1 | `W` (97.9%) | 48 | 68.8% | 55-80% | 1,130 | 92.1% | 90-94% | 23.4% |  |
| forward | 24 | 3 | `A` | A&rarr;G 40, A&rarr;T 6, A&rarr;C 1 | `D` (97.9%) | 47 | 70.2% | 56-81% | 1,131 | 92.0% | 90-93% | 21.8% |  |
| forward | 15 | 12 | `A` | A&rarr;G 39, A&rarr;T 24 | `D` | 63 | 74.6% | 63-84% | 1,115 | 92.1% | 90-94% | 17.5% |  |
| forward | 22 | 5 | `G` | G&rarr;A 36, G&rarr;T 2, G&rarr;C 1 | `D` (97.4%) | 39 | 76.9% | 62-87% | 1,139 | 91.7% | 90-93% | 14.7% |  |
| forward | 17 | 10 | `G` | G&rarr;T 80 | `K` | 80 | 81.2% | 71-88% | 1,098 | 91.9% | 90-93% | 10.6% |  |
| forward | 18 | 9 | `T` | T&rarr;G 34, T&rarr;C 2 | `B` | 36 | 83.3% | 68-92% | 1,142 | 91.4% | 90-93% | 8.1% |  |
| forward | 26 | 1 | `G` | G&rarr;A 51, G&rarr;T 18 | `D` | 69 | 85.5% | 75-92% | 1,109 | 91.5% | 90-93% | 6.0% |  |
| forward | 20 | 7 | `G` | G&rarr;T 70, G&rarr;A 6 | `D` | 76 | 86.8% | 77-93% | 1,102 | 91.5% | 90-93% | 4.6% |  |
| forward | 23 | 4 | `A` | A&rarr;G 131, A&rarr;T 2 | `R` (98.5%) | 133 | 87.2% | 80-92% | 1,045 | 91.7% | 90-93% | 4.5% |  |
| forward | 16 | 11 | `T` | T&rarr;G 56, T&rarr;C 1 | `K` (98.2%) | 57 | 87.7% | 77-94% | 1,121 | 91.3% | 90-93% | 3.6% |  |
| forward | 25 | 2 | `G` | G&rarr;A 132, G&rarr;T 2 | `R` (98.5%) | 134 | 89.6% | 83-94% | 1,044 | 91.4% | 90-93% | 1.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 823 | detect | 2023×37, 2024×87, 2025×94, 2026×57 | Cryptosporidium parvum×227, Cryptosporidium sp.×133, Cryptosporidium bovis×82 | `PZ944843`, `PZ944842`, `PZ944841`, `PZ491084`, `PZ459145`, `PZ459144` (+817) |
| rev 1,2,4,5 | 51 | fail | 2009×43, 2017×1, 2024×7 | Cryptosporidium serpentis×34, Cryptosporidium sp.×5, Cryptosporidium saurophilum×5 | `PP124559`, `PP124558`, `PP124556`, `PP101411`, `PP101410`, `PP101409` (+45) |
| fwd 22 | 17 | detect | 2004×1, 2005×3, 2007×3, 2015×1 | Cryptosporidium parvum×6, Cryptosporidium sp.×4, Cryptosporidium meleagridis×3 | `KT151551`, `AF115377`, `AF112576`, `AF112574`, `AF112573`, `AF112572` (+11) |
| fwd 20,23,25 | 16 | reduced | 2019×1, 2021×2, 2022×1, 2023×12 | Cryptosporidium bovis×8, Cryptosporidium andersoni×2, Cryptosporidium scrofarum×1 | `PP023957`, `PP023941`, `PP023939`, `OQ456437`, `OQ456427`, `OP861845` (+10) |
| fwd 18,20,23,25 | 12 | reduced | 2020×2, 2023×9, 2025×1 | Cryptosporidium bovis×7, Cryptosporidium ryanae×2, Cryptosporidium andersoni×1 | `PV740228`, `OP861841`, `OP861783`, `OP861769`, `OP861761`, `OP861749` (+6) |
| rev 13,19 | 10 | detect | 2011×1, 2018×1, 2022×8 | Cryptosporidium scrofarum×7, Cryptosporidium suis×2, Cryptosporidium sp.×1 | `ON149811`, `ON149810`, `ON149809`, `ON149808`, `ON149807`, `ON149806` (+4) |
| fwd 16,17,23,25 | 6 | reduced | 2021×1, 2023×5 | Cryptosporidium ryanae×3, Cryptosporidium bovis×2, Cryptosporidium meleagridis×1 | `PP023955`, `PP023921`, `OR994165`, `OR994164`, `OR994155`, `MT757970` |
| fwd 20,23,24,25,26 | 6 | reduced | 2009×1, 2019×1, 2023×4 | Cryptosporidium ryanae×2, Cryptosporidium bovis×1, Cryptosporidium suis×1 | `PP023915`, `OQ456426`, `OQ361806`, `OP861794`, `MK796076`, `EU717828` |

## Paramyxovirinae_Polymerase_L_gene_Tong_2008_round1

Paramyxoviridae (taxid 11158) — status **low coverage** — 10,566 evaluable of 15,440 screened records

- forward: `5'-GAAGGITATTGTCAIAARNTNTGGAC-3'` (26 nt)
- reverse: `5'-GCTGAAGTTACIGGITCICCDATRTTNC-3'` (28 nt)

**3,542 of 10,566 evaluable records (34%) share one mismatch pattern, mostly Measles virus, deposited 1989-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 19 | 8 | `A` | A&rarr;T 5,200 | `W` | 5,200 | 5.8% | 5-6% | 5,366 | 95.7% | 95-96% | 89.9% |  |
| reverse | 18 | 11 | `C` | C&rarr;A 2,792, C&rarr;G 312, C&rarr;T 71 | `V` (97.8%) | 3,175 | 1.5% | 1-2% | 7,391 | 72.9% | 72-74% | 71.4% |  |
| reverse | 26 | 3 | `T` | T&rarr;A 4,718, T&rarr;G 669, T&rarr;C 184, +1 more | `D` (96.7%) | 5,572 | 20.2% | 19-21% | 4,994 | 86.3% | 85-87% | 66.0% |  |
| forward | 20 | 7 | `T` | T&rarr;C 1,453, T&rarr;G 2, T&rarr;A 1 | `Y` (99.8%) | 1,456 | 0.3% | 0-1% | 9,110 | 59.6% | 59-61% | 59.3% |  |
| reverse | 22 | 7 | `G` | G&rarr;A 3,482, G&rarr;C 204 | `V` | 3,686 | 14.4% | 13-16% | 6,880 | 71.3% | 70-72% | 57.0% |  |
| reverse | 21 | 8 | `T` | T&rarr;C 3,685, T&rarr;A 63 | `Y` (98.3%) | 3,748 | 15.1% | 14-16% | 6,818 | 71.4% | 70-72% | 56.4% |  |
| forward | 18 | 9 | `T` | T&rarr;A 2,629, T&rarr;C 1,127, T&rarr;G 346 | hypervariable | 4,102 | 17.0% | 16-18% | 6,464 | 73.3% | 72-74% | 56.3% |  |
| forward | 24 | 3 | `A` | A&rarr;G 3,444 | `R` | 3,444 | 15.5% | 14-17% | 7,122 | 68.8% | 68-70% | 53.3% |  |
| forward | 16 | 11 | `G` | G&rarr;A 16, G&rarr;C 11 | `V` | 27 | 0.0% | 0-12% | 10,539 | 51.6% | 51-53% | 51.6% |  |
| reverse | 24 | 5 | `A` | A&rarr;C 2,362, A&rarr;T 2,072 | `H` | 4,434 | 22.9% | 22-24% | 6,132 | 72.1% | 71-73% | 49.2% |  |
| reverse | 19 | 10 | `A` | A&rarr;G 1,860, A&rarr;C 1,836 | `V` | 3,696 | 20.2% | 19-22% | 6,870 | 68.2% | 67-69% | 48.0% |  |
| forward | 15 | 12 | `T` | T&rarr;C 2,111, T&rarr;A 14 | `Y` (99.3%) | 2,125 | 15.3% | 14-17% | 8,441 | 60.5% | 59-62% | 45.2% |  |
| forward | 7 | 20 | `T` | T&rarr;C 228 | `Y` | 228 | 8.3% | 5-13% | 10,338 | 52.4% | 51-53% | 44.1% |  |
| reverse | 25 | 4 | `G` | G&rarr;C 63 | `S` | 63 | 17.5% | 10-29% | 10,503 | 51.6% | 51-53% | 34.2% |  |
| reverse | 20 | 9 | `T` | T&rarr;C 2,269, T&rarr;G 485, T&rarr;A 450 | hypervariable | 3,204 | 31.2% | 30-33% | 7,362 | 60.2% | 59-61% | 29.0% |  |
| forward | 17 | 10 | `T` | T&rarr;A 264, T&rarr;C 3 | `W` (98.9%) | 267 | 34.5% | 29-40% | 10,299 | 51.9% | 51-53% | 17.4% |  |
| reverse | 23 | 6 | `A` | A&rarr;T 4,719, A&rarr;C 1,702, A&rarr;G 697 | hypervariable | 7,118 | 63.0% | 62-64% | 3,448 | 27.7% | 26-29% | -35.3% |  |
| reverse | 27 | 2 | `C` | C&rarr;A 4,905, C&rarr;T 14 | `M` (99.7%) | 4,919 | 94.0% | 93-95% | 5,647 | 14.4% | 14-15% | -79.6% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 23,27 | 3,542 | detect | 2023×173, 2024×141, 2025×670, 2026×1879 | Measles virus×3270, Morbillivirus hominis×170, Measles morbillivirus×99 | `QB035549`, `QB035548`, `QB035547`, `QB035546`, `QB035545`, `QB035544` (+3,536) |
| fwd 18,19,24; rev 18,21,22,23,26 | 1,326 | fail | 2022×85, 2023×8, 2024×315, 2026×32 | Mumps virus×1064, Mumps orthorubulavirus×252, Mutant×9 | `PZ015905`, `PZ015904`, `PZ015902`, `PZ803316`, `PZ803315`, `PZ803314` (+1,320) |
| fwd 19; rev 18,19,21,22,24,26 | 1,292 | fail | 2023×55, 2024×269, 2025×453, 2026×73 | Human respirovirus×1161, Human parainfluenza×118, Respirovirus pneumoniae×7 | `PZ892266`, `PZ892264`, `PZ892263`, `PZ892262`, `PZ892261`, `PZ797561` (+1,286) |
| rev 19,21,22,24 | 462 | reduced | 2023×11, 2024×149, 2025×175, 2026×29 | Human respirovirus×395, Human parainfluenza×60, Respirovirus laryngotracheitidis×7 | `PZ892260`, `PZ892259`, `LC817390`, `LC817389`, `LC769222`, `LC720862` (+456) |
| fwd 15,18,19,24; rev 19,20,24,26 | 358 | fail | 2023×13, 2024×27, 2025×53, 2026×16 | Avian paramyxovirus×174, Pigeon paramyxovirus×74, Newcastle disease×68 | `PQ067333`, `PQ067332`, `PV958090`, `PZ339901`, `PZ339899`, `PZ339898` (+352) |
| fwd 15,19,20,24; rev 19,20,23,24 | 230 | fail | 2023×4, 2024×5, 2025×14, 2026×8 | Avian paramyxovirus×170, Newcastle disease×36, Avian orthoavulavirus×24 | `LC888361`, `LC890399`, `PQ519976`, `PQ519975`, `PQ519974`, `MZ408183` (+224) |
| fwd 15,18,19,20,24; rev 19,20,24,26 | 200 | fail | 2023×7, 2024×6, 2025×11, 2026×9 | Avian paramyxovirus×153, Newcastle disease×24, Avian orthoavulavirus×22 | `PZ519057`, `PZ360914`, `PZ360911`, `PZ645901`, `PV455366`, `PV455364` (+194) |
| fwd 18,19,20; rev 18,20,21,22,24 | 200 | fail | 2023×2, 2024×36, 2025×64, 2026×25 | Human orthorubulavirus×190, Human parainfluenza×4, Orthorubulavirus laryngotracheitidis×3 | `PV980074`, `PZ245065`, `PZ245064`, `PZ245063`, `PZ245062`, `PZ245061` (+194) |

## DWVB_polyprotein_Rossi_2024

Deformed wing virus B (taxid 2498590) — status **declining** — 57 evaluable of 737 screened records

- forward: `5'-TTTATCTTCATTAAAACCGCCA-3'` (22 nt)
- reverse: `5'-CTCATTAACTGAGTTGTTGTC-3'` (21 nt)
- probe: `5'-ATCTTTTGAGAGGGATGAGA-3'` (20 nt)

**6 of 57 evaluable records (11%) share one mismatch pattern, mostly Deformed wing, deposited 2023-2025, and the group's dominant call is `detect`.**

No single position reaches the reporting threshold: the mismatches are spread thinly rather than concentrated. The footprint table below is the informative view for this assay.

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 29 | detect | 2023×25, 2025×2, 2026×2 | Deformed wing×29 | `PZ565201`, `PZ565199`, `PV664207`, `PV239926`, `OR497392`, `OR497391` (+23) |
| rev 4 | 6 | detect | 2023×1, 2025×5 | Deformed wing×6 | `PV664191`, `PV664187`, `PV664182`, `PV664176`, `PV664167`, `OR361548` |
| prb 19 | 5 | detect | 2023×5 | Deformed wing×5 | `OR497394`, `OR497384`, `OR497383`, `OR361549`, `OR361543` |
| fwd 16 | 4 | detect | 2023×4 | Deformed wing×4 | `OR497395`, `OR497385`, `OR497382`, `OR497380` |
| fwd 19 | 3 | detect | 2023×3 | Deformed wing×3 | `OR497396`, `OR497387`, `OR497386` |
| rev 16 | 2 | detect | 2025×1, 2026×1 | Deformed wing×2 | `PZ565200`, `PP418870` |
| fwd 4; prb 19 | 2 | detect | 2023×2 | Deformed wing×2 | `OR361539`, `OR361538` |
| fwd 1,4,10,19; rev 4 | 1 | fail | 2026×1 | Deformed wing×1 | `PX663595` |

## ORF_VIRUS_dsDNA_RPO147_J6R_TaqMan_Zhao_2013

Orf virus (taxid 10258) — status **low coverage** — 164 evaluable of 2,514 screened records

- forward: `5'-GAGTTCGAGGAGATGATCTTGA-3'` (22 nt)
- reverse: `5'-GCCGAGGAGCAGGTCA-3'` (16 nt)
- probe: `5'-CTCGATCACGGCGCGCT-3'` (17 nt)

**75 of 164 evaluable records (46%) share one mismatch pattern, mostly Orf virus, deposited 1994-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 1 | 22 | `A` | A&rarr;T 76 | `W` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% | yes |
| forward | 9 | 14 | `T` | T&rarr;A 76 | `W` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% |  |
| forward | 13 | 10 | `G` | G&rarr;A 76 | `R` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% |  |
| forward | 15 | 8 | `A` | A&rarr;C 76 | `M` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% |  |
| forward | 18 | 5 | `T` | T&rarr;C 76 | `Y` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% |  |
| reverse | 4 | 13 | `G` | G&rarr;C 76 | `S` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% | yes |
| reverse | 7 | 10 | `C` | C&rarr;G 76 | `S` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% |  |
| reverse | 9 | 8 | `A` | A&rarr;T 76 | `W` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% |  |
| reverse | 12 | 5 | `A` | A&rarr;T 76 | `W` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% |  |
| reverse | 13 | 4 | `G` | G&rarr;T 76 | `K` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% |  |
| reverse | 16 | 1 | `G` | G&rarr;T 76 | `K` | 76 | 0.0% | 0-5% | 88 | 100.0% | 96-100% | 100.0% |  |
| forward | 7 | 16 | `A` | A&rarr;T 75 | `W` | 75 | 0.0% | 0-5% | 89 | 98.9% | 94-100% | 98.9% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 80 | detect | 2023×10, 2024×12, 2025×16, 2026×11 | Orf virus×74, Mutant×2, Sequence×2 | `PZ685464`, `PZ685463`, `PZ370946`, `PZ497124`, `PZ497123`, `PZ403669` (+74) |
| fwd 1,7,9,13,15,18; rev 4,7,9,12,13,16 | 75 | fail | 2022×10, 2023×5, 2025×8, 2026×1 | Orf virus×74, orf virus×1 | `PZ438997`, `PQ621449`, `PQ621448`, `PQ621447`, `PQ621445`, `PQ621440` (+69) |
| fwd 14 | 4 | detect | 2022×1, 2023×3 | Orf virus×4 | `ON380500`, `ON380499`, `OP562382`, `MW537048` |
| fwd 17 | 3 | detect | 2003×1, 2004×1, 2013×1 | Orf virus×2, Sequence×1 | `NC_005336`, `JB071977`, `AY386264` |
| fwd 11 | 1 | detect | 2025×1 | Orf virus×1 | `PP911590` |
| fwd 1,9,13,15,18; rev 4,7,9,12,13,16 | 1 | fail | 2013×1 | Orf virus×1 | `KF478800` |

## PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999

Papillomaviridae (taxid 151340) — status **declining** — 16,361 evaluable of 43,011 screened records

- forward: `5'-TAACWGTIGGICAYCCWTATT-3'` (21 nt)
- reverse: `5'-CCWATATCWVHCATITCICCATC-3'` (23 nt)

**4,018 of 16,361 evaluable records (25%) share one mismatch pattern, mostly Human papillomavirus, deposited 1993-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 5 | 17 | `W` | W&rarr;C 6,337, W&rarr;G 148 | `H` (97.7%) | 6,485 | 18.6% | 18-20% | 9,876 | 84.5% | 84-85% | 65.9% | yes |
| forward | 19 | 3 | `A` | A&rarr;G 8,354, A&rarr;C 126, A&rarr;T 69 | `R` (97.7%) | 8,549 | 27.3% | 26-28% | 7,812 | 92.4% | 92-93% | 65.2% |  |
| reverse | 3 | 21 | `A` | A&rarr;G 1,329, A&rarr;T 19, A&rarr;S 1 | `R` (98.5%) | 1,349 | 4.2% | 3-5% | 15,012 | 63.2% | 62-64% | 59.1% | yes |
| forward | 13 | 9 | `G` | G&rarr;T 49, G&rarr;C 7, G&rarr;A 3 | hypervariable | 59 | 0.0% | 0-6% | 16,302 | 58.6% | 58-59% | 58.6% |  |
| forward | 12 | 10 | `G` | G&rarr;T 50, G&rarr;C 5, G&rarr;A 3 | hypervariable | 58 | 0.0% | 0-6% | 16,303 | 58.6% | 58-59% | 58.6% |  |
| forward | 6 | 16 | `C` | C&rarr;A 50, C&rarr;T 3 | `H` | 53 | 0.0% | 0-7% | 16,308 | 58.6% | 58-59% | 58.6% |  |
| reverse | 22 | 2 | `C` | C&rarr;A 51, C&rarr;T 2 | `M` (96.2%) | 53 | 0.0% | 0-7% | 16,308 | 58.6% | 58-59% | 58.6% |  |
| forward | 8 | 14 | `Y` | Y&rarr;A 50 | `H` | 50 | 0.0% | 0-7% | 16,311 | 58.6% | 58-59% | 58.6% |  |
| reverse | 4 | 20 | `C` | C&rarr;T 53, C&rarr;A 6, C&rarr;G 1 | `H` (98.3%) | 60 | 1.7% | 0-9% | 16,301 | 58.6% | 58-59% | 56.9% | yes |
| reverse | 12 | 12 | `C` | C&rarr;A 56, C&rarr;T 21, C&rarr;G 3 | `H` (96.2%) | 80 | 2.5% | 1-9% | 16,281 | 58.7% | 58-59% | 56.2% |  |
| reverse | 23 | 1 | `C` | C&rarr;T 56, C&rarr;A 17, C&rarr;G 3 | `H` (96.1%) | 76 | 2.6% | 1-9% | 16,285 | 58.6% | 58-59% | 56.0% |  |
| reverse | 16 | 8 | `C` | C&rarr;A 71, C&rarr;G 35, C&rarr;T 2 | `V` (98.1%) | 108 | 3.7% | 1-9% | 16,253 | 58.7% | 58-59% | 55.0% |  |
| forward | 15 | 7 | `T` | T&rarr;C 22, T&rarr;A 5 | `H` | 27 | 3.7% | 1-18% | 16,334 | 58.5% | 58-59% | 54.8% |  |
| reverse | 13 | 11 | `H` | H&rarr;G 27 | hypervariable | 27 | 3.7% | 1-18% | 16,334 | 58.5% | 58-59% | 54.8% |  |
| reverse | 21 | 3 | `W` | W&rarr;G 849, W&rarr;C 136 | hypervariable | 985 | 10.2% | 8-12% | 15,376 | 61.5% | 61-62% | 51.3% |  |
| reverse | 8 | 16 | `T` | T&rarr;G 19, T&rarr;A 11, T&rarr;C 5 | hypervariable | 35 | 11.4% | 5-26% | 16,326 | 58.5% | 58-59% | 47.0% |  |
| forward | 21 | 1 | `T` | T&rarr;A 51, T&rarr;G 10, T&rarr;C 7 | hypervariable | 68 | 11.8% | 6-22% | 16,293 | 58.6% | 58-59% | 46.8% |  |
| reverse | 5 | 19 | `C` | C&rarr;G 23, C&rarr;A 1, C&rarr;T 1 | `V` (96.0%) | 25 | 12.0% | 4-30% | 16,336 | 58.4% | 58-59% | 46.4% | yes |
| reverse | 10 | 14 | `T` | T&rarr;G 11, T&rarr;A 9 | `D` | 20 | 15.0% | 5-36% | 16,341 | 58.4% | 58-59% | 43.4% |  |
| reverse | 17 | 7 | `T` | T&rarr;G 18, T&rarr;C 3, T&rarr;A 3 | hypervariable | 24 | 16.7% | 7-36% | 16,337 | 58.4% | 58-59% | 41.8% |  |
| forward | 4 | 18 | `T` | T&rarr;C 50, T&rarr;A 14, T&rarr;G 3 | `H` (95.5%) | 67 | 23.9% | 15-35% | 16,294 | 58.5% | 58-59% | 34.6% | yes |
| forward | 2 | 20 | `T` | T&rarr;C 1,901, T&rarr;G 33, T&rarr;A 20 | `Y` (97.3%) | 1,954 | 30.6% | 29-33% | 14,407 | 62.1% | 61-63% | 31.5% | yes |
| reverse | 7 | 17 | `C` | C&rarr;G 86, C&rarr;T 61, C&rarr;A 11 | hypervariable | 158 | 33.5% | 27-41% | 16,203 | 58.6% | 58-59% | 25.1% |  |
| forward | 3 | 19 | `A` | A&rarr;T 425, A&rarr;G 3 | `W` (99.3%) | 428 | 36.0% | 32-41% | 15,933 | 59.0% | 58-60% | 23.0% | yes |
| reverse | 20 | 4 | `A` | A&rarr;G 14,184, A&rarr;T 56, A&rarr;C 2 | `R` (99.6%) | 14,242 | 55.9% | 55-57% | 2,119 | 74.9% | 73-77% | 19.0% |  |
| forward | 20 | 2 | `A` | A&rarr;T 9,235, A&rarr;G 2,269, A&rarr;C 213 | `D` (98.2%) | 11,717 | 53.2% | 52-54% | 4,644 | 71.3% | 70-73% | 18.1% |  |
| forward | 17 | 5 | `W` | W&rarr;C 318, W&rarr;G 136 | hypervariable | 454 | 49.3% | 45-54% | 15,907 | 58.6% | 58-59% | 9.3% |  |
| reverse | 18 | 6 | `A` | A&rarr;G 3,007, A&rarr;T 505, A&rarr;C 103 | `D` (97.2%) | 3,615 | 55.6% | 54-57% | 12,746 | 59.2% | 58-60% | 3.6% |  |
| forward | 1 | 21 | `T` | T&rarr;C 59, T&rarr;A 11, T&rarr;G 1 | `H` (98.6%) | 71 | 54.9% | 43-66% | 16,290 | 58.4% | 58-59% | 3.5% | yes |
| forward | 18 | 4 | `C` | C&rarr;T 445, C&rarr;A 102, C&rarr;G 20 | `H` (96.5%) | 567 | 65.6% | 62-69% | 15,794 | 58.1% | 57-59% | -7.5% |  |
| reverse | 19 | 5 | `T` | T&rarr;C 339, T&rarr;A 74, T&rarr;G 46 | hypervariable | 459 | 68.8% | 64-73% | 15,902 | 58.1% | 57-59% | -10.8% |  |
| forward | 16 | 6 | `G` | G&rarr;A 325, G&rarr;T 320, G&rarr;C 54 | hypervariable | 699 | 78.3% | 75-81% | 15,662 | 57.5% | 57-58% | -20.8% |  |
| reverse | 15 | 9 | `W` | W&rarr;C 2,020, W&rarr;G 85 | `H` (96.0%) | 2,105 | 85.4% | 84-87% | 14,256 | 54.4% | 54-55% | -31.0% |  |
| forward | 10 | 12 | `C` | C&rarr;A 2,880, C&rarr;G 6 | `M` (99.8%) | 2,886 | 91.5% | 90-92% | 13,475 | 51.3% | 50-52% | -40.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 5,19,20; rev 20 | 4,018 | fail | 2023×14, 2024×32, 2025×143, 2026×96 | Human papillomavirus×3963, Sequence×27, JP×16 | `PZ377076`, `PZ377075`, `PZ377074`, `PZ377073`, `PZ377069`, `QQ287240` (+4,012) |
| fwd 20; rev 20 | 2,392 | detect | 2023×87, 2024×217, 2025×1, 2026×4 | Human papillomavirus×2386, Sequence×4, Patent application×2 | `PZ638625`, `PZ638624`, `QW261821`, `QW261799`, `PV012261`, `PQ177836` (+2,386) |
| fwd 2,19; rev 3,18,20 | 1,054 | fail | 2022×7, 2023×17, 2024×145, 2026×3 | Human papillomavirus×1050, Patent application×2, Sequence×2 | `PZ638627`, `QW261823`, `QW261801`, `PP792123`, `PP792122`, `PP792121` (+1,048) |
| fwd 10,19,20; rev 20 | 935 | reduced | 2023×26, 2024×171, 2025×22, 2026×3 | Human papillomavirus×924, JP×4, Sequence×3 | `PZ669445`, `QW261829`, `QW261807`, `PQ720438`, `PQ720434`, `PX463235` (+929) |
| fwd 10; rev 20 | 801 | reduced | 2023×15, 2024×131, 2025×168, 2026×61 | Human papillomavirus×777, JP×8, Sequence×8 | `PZ377083`, `PZ377082`, `PZ377081`, `PZ377079`, `QW261820`, `QW261798` (+795) |
| fwd 10; rev 15,20 | 755 | reduced | 2023×21, 2024×78, 2025×589, 2026×2 | Human papillomavirus×741, Sequence×7, JP×4 | `QW261825`, `QW261803`, `PV419492`, `PV419490`, `PV419489`, `PV419486` (+749) |
| fwd 5,19,20; rev 20,21 | 729 | fail | 2022×60, 2023×12, 2025×10, 2026×2 | Human papillomavirus×729 | `PZ377077`, `PZ628165`, `PX461756`, `PX461754`, `PV051158`, `PV051145` (+723) |
| fwd 5,20; rev 20 | 551 | reduced | 2022×140, 2023×2, 2024×174, 2025×2 | Human papillomavirus×551 | `PV012271`, `PV012260`, `PQ177660`, `PQ177659`, `PQ177658`, `PQ177657` (+545) |

## CDV_P_gene_Scagliarini_2007

Morbillivirus canis (formerly Canine morbillivirus) (taxid 3052342) — status **declining** — 604 evaluable of 4,013 screened records

- forward: `5'-GTCGGTAATCGAGGATTCGAGAG-3'` (23 nt)
- reverse: `5'-GCCGAAAGAATATCCCCAGTTAG-3'` (23 nt)
- probe: `5'-ATCTTCGCCAGAATCCTCAGTGCT-3'` (24 nt)

**226 of 604 evaluable records (37%) share one mismatch pattern, mostly Canine distemper, deposited 1999-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 2 | 22 | `A` | A&rarr;G 75 | `R` | 75 | 0.0% | 0-5% | 529 | 99.1% | 98-100% | 99.1% | yes |
| forward | 16 | 8 | `A` | A&rarr;G 30 | `R` | 30 | 0.0% | 0-11% | 574 | 91.3% | 89-93% | 91.3% |  |
| forward | 1 | 23 | `G` | G&rarr;A 27, G&rarr;C 2 | `V` | 29 | 0.0% | 0-12% | 575 | 91.1% | 89-93% | 91.1% | yes |
| probe | 16 | 9 | `C` | C&rarr;T 20 | `Y` | 20 | 0.0% | 0-16% | 584 | 89.7% | 87-92% | 89.7% |  |
| forward | 8 | 16 | `T` | T&rarr;C 43, T&rarr;G 1 | `Y` (97.7%) | 44 | 27.3% | 16-42% | 560 | 91.4% | 89-93% | 64.2% |  |
| forward | 19 | 5 | `G` | G&rarr;A 40 | `R` | 40 | 32.5% | 20-48% | 564 | 90.6% | 88-93% | 58.1% |  |
| forward | 20 | 4 | `G` | G&rarr;A 499 | `R` | 499 | 85.6% | 82-88% | 105 | 92.4% | 86-96% | 6.8% |  |
| reverse | 20 | 4 | `G` | G&rarr;A 43, G&rarr;T 1 | `R` (97.7%) | 44 | 84.1% | 71-92% | 560 | 87.0% | 84-90% | 2.9% |  |
| forward | 17 | 7 | `A` | A&rarr;G 29 | `R` | 29 | 93.1% | 78-98% | 575 | 86.4% | 83-89% | -6.7% |  |
| probe | 9 | 16 | `C` | C&rarr;T 36 | `Y` | 36 | 94.4% | 82-98% | 568 | 86.3% | 83-89% | -8.2% |  |
| forward | 23 | 1 | `G` | G&rarr;A 38 | `R` | 38 | 100.0% | 91-100% | 566 | 85.9% | 83-88% | -14.1% |  |
| reverse | 23 | 1 | `G` | G&rarr;A 65 | `R` | 65 | 100.0% | 94-100% | 539 | 85.2% | 82-88% | -14.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 20 | 226 | detect | 2023×1, 2024×10, 2025×11, 2026×33 | Canine distemper×110, Morbillivirus canis×109, Canine morbillivirus×7 | `LC945032`, `LC945031`, `LC945030`, `PX656922`, `PX445144`, `PX938971` (+220) |
| no mismatches | 78 | detect | 2019×1, 2020×3, 2022×8, 2024×5 | Canine distemper×36, Morbillivirus canis×17, Canine morbillivirus×8 | `PC304176`, `PC304170`, `OP242376`, `OP242375`, `OP242374`, `LC136921` (+72) |
| fwd 20; rev 23 | 57 | detect | 2016×6, 2017×2, 2019×6, 2020×28 | Canine distemper×29, Morbillivirus canis×28 | `MT932503`, `MT932502`, `MT932501`, `MT932500`, `MT932499`, `MT932493` (+51) |
| fwd 2,20 | 35 | fail | 2020×10, 2022×1, 2023×3, 2026×4 | Morbillivirus canis×20, Canine distemper×12, Canine morbillivirus×3 | `PV167797`, `PX656915`, `PX656914`, `PX656913`, `OR514514`, `OR514513` (+29) |
| fwd 20,23; prb 9 | 31 | reduced | 2011×1, 2012×2, 2013×6, 2014×8 | Morbillivirus canis×31 | `AB490681`, `AB490680`, `AB490679`, `AB490678`, `AB490676`, `AB490674` (+25) |
| fwd 20; rev 20 | 24 | detect | 2020×3, 2022×2, 2025×1, 2026×18 | Morbillivirus canis×22, Canine morbillivirus×2 | `PZ812018`, `PZ812017`, `PZ812016`, `PZ812015`, `PZ812014`, `PZ812013` (+18) |
| fwd 17,20 | 20 | detect | 2022×20 | Canine morbillivirus×20 | `OP209186`, `OK557797`, `OK557796`, `OK557795`, `OK557794`, `OK557793` (+14) |
| fwd 1,2,8,16,19,20; prb 5,16 | 13 | fail | 2018×4, 2020×1, 2023×1, 2024×2 | Canine distemper×11, Morbillivirus canis×2 | `PQ311662`, `PQ311661`, `OR514512`, `MT149210`, `MH496778`, `MH496777` (+7) |

## ADENOVIRUS_dsDNA_Hexon_gene

Adenoviridae (taxid 10508) — status **declining** — 6,188 evaluable of 38,963 screened records

- forward: `5'-CAACACCTAYGASTACATGAA-3'` (21 nt)
- reverse: `5'-KATGGGGTARAGCATGTT-3'` (18 nt)

**736 of 6,188 evaluable records (12%) share one mismatch pattern, mostly Human adenovirus, deposited 1993-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 5 | 14 | `A` | A&rarr;G 276, A&rarr;T 86, A&rarr;C 8 | `D` (97.8%) | 370 | 0.0% | 0-1% | 5,818 | 82.5% | 81-83% | 82.5% | yes |
| reverse | 14 | 5 | `G` | G&rarr;T 216, G&rarr;C 109, G&rarr;A 9 | `B` (97.3%) | 334 | 0.0% | 0-1% | 5,854 | 82.0% | 81-83% | 82.0% |  |
| reverse | 16 | 3 | `T` | T&rarr;C 272, T&rarr;A 103, T&rarr;G 8 | `H` (97.9%) | 383 | 1.3% | 1-3% | 5,805 | 82.6% | 82-84% | 81.3% |  |
| forward | 2 | 20 | `A` | A&rarr;C 166, A&rarr;T 27, A&rarr;G 11 | hypervariable | 204 | 0.0% | 0-2% | 5,984 | 80.2% | 79-81% | 80.2% | yes |
| reverse | 4 | 15 | `T` | T&rarr;C 242, T&rarr;G 19, T&rarr;A 16 | hypervariable | 277 | 1.4% | 1-4% | 5,911 | 81.1% | 80-82% | 79.7% | yes |
| reverse | 1 | 18 | `T` | T&rarr;A 121, T&rarr;C 53, T&rarr;G 37 | hypervariable | 211 | 0.9% | 0-3% | 5,977 | 80.3% | 79-81% | 79.3% | yes |
| reverse | 17 | 2 | `A` | A&rarr;G 100, A&rarr;C 50, A&rarr;T 12 | hypervariable | 162 | 0.6% | 0-3% | 6,026 | 79.6% | 79-81% | 79.0% |  |
| forward | 17 | 5 | `A` | A&rarr;T 408, A&rarr;G 10, A&rarr;C 4 | `W` (96.7%) | 422 | 4.0% | 3-6% | 5,766 | 82.9% | 82-84% | 78.9% |  |
| forward | 8 | 14 | `T` | T&rarr;G 85, T&rarr;A 10, T&rarr;C 7 | hypervariable | 102 | 0.0% | 0-4% | 6,086 | 78.9% | 78-80% | 78.9% |  |
| forward | 1 | 21 | `A` | A&rarr;T 92, A&rarr;C 9 | `H` | 101 | 0.0% | 0-4% | 6,087 | 78.8% | 78-80% | 78.8% | yes |
| reverse | 10 | 9 | `A` | A&rarr;C 134, A&rarr;T 37, A&rarr;G 14 | hypervariable | 185 | 1.1% | 0-4% | 6,003 | 79.9% | 79-81% | 78.8% |  |
| forward | 7 | 15 | `A` | A&rarr;C 74, A&rarr;G 10, A&rarr;T 7 | hypervariable | 91 | 0.0% | 0-4% | 6,097 | 78.7% | 78-80% | 78.7% |  |
| forward | 5 | 17 | `A` | A&rarr;T 78, A&rarr;C 34, A&rarr;G 28 | hypervariable | 140 | 0.7% | 0-4% | 6,048 | 79.3% | 78-80% | 78.6% | yes |
| forward | 19 | 3 | `A` | A&rarr;C 240, A&rarr;G 18, A&rarr;T 14 | hypervariable | 272 | 2.9% | 1-6% | 5,916 | 81.0% | 80-82% | 78.0% |  |
| forward | 14 | 8 | `T` | T&rarr;C 13, T&rarr;A 7, T&rarr;G 4 | hypervariable | 24 | 0.0% | 0-14% | 6,164 | 77.9% | 77-79% | 77.9% |  |
| forward | 4 | 18 | `T` | T&rarr;A 12, T&rarr;G 5, T&rarr;C 5 | hypervariable | 22 | 0.0% | 0-15% | 6,166 | 77.8% | 77-79% | 77.8% | yes |
| reverse | 13 | 6 | `G` | G&rarr;C 137, G&rarr;T 57, G&rarr;A 7 | `B` (96.5%) | 201 | 2.5% | 1-6% | 5,987 | 80.1% | 79-81% | 77.6% |  |
| forward | 6 | 16 | `C` | C&rarr;T 450, C&rarr;A 5 | `Y` (98.9%) | 455 | 6.2% | 4-9% | 5,733 | 83.2% | 82-84% | 77.1% |  |
| reverse | 6 | 13 | `C` | C&rarr;A 86, C&rarr;G 67, C&rarr;T 64 | hypervariable | 217 | 4.1% | 2-8% | 5,971 | 80.2% | 79-81% | 76.1% |  |
| reverse | 2 | 17 | `T` | T&rarr;A 133, T&rarr;C 20, T&rarr;G 10 | hypervariable | 163 | 4.9% | 3-9% | 6,025 | 79.5% | 78-81% | 74.6% | yes |
| reverse | 8 | 11 | `A` | A&rarr;T 38, A&rarr;C 17, A&rarr;G 11 | hypervariable | 66 | 4.5% | 2-13% | 6,122 | 78.3% | 77-79% | 73.8% |  |
| forward | 20 | 2 | `A` | A&rarr;T 77, A&rarr;C 30, A&rarr;G 10 | hypervariable | 117 | 7.7% | 4-14% | 6,071 | 78.9% | 78-80% | 71.2% |  |
| reverse | 7 | 12 | `G` | G&rarr;A 369, G&rarr;T 5, G&rarr;C 1 | `R` (98.4%) | 375 | 13.6% | 10-17% | 5,813 | 81.7% | 81-83% | 68.1% |  |
| reverse | 11 | 8 | `T` | T&rarr;A 40, T&rarr;G 7, T&rarr;C 4 | hypervariable | 51 | 13.7% | 7-26% | 6,137 | 78.1% | 77-79% | 64.4% |  |
| forward | 18 | 4 | `C` | C&rarr;T 607, C&rarr;G 82, C&rarr;A 8 | `B` (98.9%) | 697 | 20.8% | 18-24% | 5,491 | 84.8% | 84-86% | 64.0% |  |
| reverse | 3 | 16 | `G` | G&rarr;A 33, G&rarr;C 16, G&rarr;T 1 | `V` (98.0%) | 50 | 20.0% | 11-33% | 6,138 | 78.0% | 77-79% | 58.0% | yes |
| forward | 15 | 7 | `C` | C&rarr;A 484, C&rarr;T 408, C&rarr;G 27 | `H` (97.1%) | 919 | 31.0% | 28-34% | 5,269 | 85.7% | 85-87% | 54.7% |  |
| forward | 16 | 6 | `C` | C&rarr;G 47, C&rarr;A 27, C&rarr;T 14 | hypervariable | 88 | 25.0% | 17-35% | 6,100 | 78.3% | 77-79% | 53.3% |  |
| forward | 9 | 13 | `S` | S&rarr;T 788, S&rarr;A 67 | hypervariable | 855 | 32.2% | 29-35% | 5,333 | 84.8% | 84-86% | 52.7% |  |
| forward | 3 | 19 | `G` | G&rarr;A 164, G&rarr;C 121, G&rarr;T 20 | hypervariable | 305 | 41.3% | 36-47% | 5,883 | 79.4% | 78-80% | 38.1% | yes |
| forward | 11 | 11 | `G` | G&rarr;A 76, G&rarr;C 74, G&rarr;T 7 | `V` (95.5%) | 157 | 50.3% | 43-58% | 6,031 | 78.3% | 77-79% | 27.9% |  |
| reverse | 15 | 4 | `G` | G&rarr;A 422, G&rarr;C 264, G&rarr;T 99 | hypervariable | 785 | 54.5% | 51-58% | 5,403 | 80.9% | 80-82% | 26.4% |  |
| forward | 10 | 12 | `A` | A&rarr;C 988, A&rarr;T 110, A&rarr;G 66 | hypervariable | 1,164 | 57.9% | 55-61% | 5,024 | 82.1% | 81-83% | 24.2% |  |
| forward | 21 | 1 | `C` | C&rarr;A 1,422, C&rarr;G 741, C&rarr;T 389 | hypervariable | 2,552 | 63.6% | 62-65% | 3,636 | 87.3% | 86-88% | 23.8% |  |
| reverse | 12 | 7 | `G` | G&rarr;A 1,463, G&rarr;C 13, G&rarr;T 4 | `R` (98.9%) | 1,480 | 65.3% | 63-68% | 4,708 | 81.4% | 80-82% | 16.1% |  |
| reverse | 9 | 10 | `R` | R&rarr;T 771, R&rarr;C 556 | hypervariable | 1,327 | 68.8% | 66-71% | 4,861 | 79.9% | 79-81% | 11.1% |  |
| reverse | 18 | 1 | `K` | K&rarr;A 2,132, K&rarr;C 164 | hypervariable | 2,296 | 76.0% | 74-78% | 3,892 | 78.5% | 77-80% | 2.5% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 1,298 | detect | 2023×101, 2024×68, 2025×37, 2026×180 | Human adenovirus×1132, Human mastadenovirus×130, Sequence×12 | `PZ256266`, `PV780771`, `HC191035`, `PX575759`, `PX575745`, `PX575744` (+1,292) |
| rev 18 | 736 | detect | 2023×89, 2024×70, 2025×118, 2026×239 | Human adenovirus×517, Human mastadenovirus×175, KR×13 | `PZ576384`, `PZ576383`, `PZ576382`, `PZ576381`, `PZ576380`, `PZ576379` (+730) |
| rev 9 | 586 | detect | 2023×89, 2024×31, 2025×51, 2026×91 | Human adenovirus×327, Human mastadenovirus×240, KR×4 | `PW424729`, `PZ410989`, `PZ410971`, `PZ410962`, `PZ410938`, `PZ410937` (+580) |
| fwd 10,21; rev 12,18 | 466 | reduced | 2023×47, 2024×53, 2025×43, 2026×97 | Human adenovirus×317, Human mastadenovirus×145, Mastadenovirus×1 | `PX059115`, `PX059114`, `PX059113`, `PX059112`, `PX059111`, `PX059110` (+460) |
| fwd 21; rev 15 | 343 | detect | 2023×75, 2024×14, 2025×18, 2026×27 | Human adenovirus×77, Human mastadenovirus×76, KR×66 | `PW424730`, `QV000696`, `PZ411233`, `PZ411232`, `PZ410841`, `QT662143` (+337) |
| fwd 6,9,15,17,18,21 | 305 | fail | 2023×80, 2024×4, 2025×20, 2026×55 | Human adenovirus×153, Human mastadenovirus×147, Feline adenovirus×2 | `PZ726819`, `PZ411235`, `PZ411229`, `PZ411227`, `PZ411219`, `PZ411205` (+299) |
| fwd 21; rev 12,18 | 186 | reduced | 2023×1, 2024×18, 2025×54, 2026×1 | Human adenovirus×182, Human mastadenovirus×2, MAG×1 | `PX491610`, `PV980178`, `PV980177`, `PV980176`, `PV980175`, `PV980174` (+180) |
| fwd 9 | 168 | detect | 2020×11, 2022×1, 2024×5, 2026×1 | Sequence×79, JP×42, KR×18 | `HC191003`, `CS138464`, `CS138463`, `PU879368`, `PC313249`, `PC313248` (+162) |

## ASTROVIRUS_RdRp_Chu_2008_round2

Astroviridae (taxid 39733) — status **low coverage** — 3,313 evaluable of 16,742 screened records

- forward: `5'-CGKTAYGATGGKACKATHCC-3'` (20 nt)
- reverse: `5'-GGYTTKACCCACATNCCRAA-3'` (20 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 5 | 16 | `A` | A&rarr;T 277, A&rarr;G 30, A&rarr;C 21 | hypervariable | 328 | 0.3% | 0-2% | 2,985 | 86.5% | 85-88% | 86.2% | yes |
| forward | 11 | 10 | `G` | G&rarr;C 28, G&rarr;T 24, G&rarr;A 2 | `B` (96.3%) | 54 | 0.0% | 0-7% | 3,259 | 79.3% | 78-81% | 79.3% |  |
| forward | 7 | 14 | `C` | C&rarr;A 29, C&rarr;G 10, C&rarr;T 7 | hypervariable | 46 | 0.0% | 0-8% | 3,267 | 79.1% | 78-80% | 79.1% |  |
| forward | 1 | 20 | `C` | C&rarr;A 27, C&rarr;T 16 | `H` | 43 | 0.0% | 0-8% | 3,270 | 79.0% | 78-80% | 79.0% | yes |
| reverse | 7 | 14 | `T` | T&rarr;C 31, T&rarr;A 12 | `H` | 43 | 0.0% | 0-8% | 3,270 | 79.0% | 78-80% | 79.0% |  |
| forward | 17 | 4 | `T` | T&rarr;A 29, T&rarr;C 8, T&rarr;G 5 | hypervariable | 42 | 0.0% | 0-8% | 3,271 | 79.0% | 78-80% | 79.0% |  |
| forward | 10 | 11 | `G` | G&rarr;C 27, G&rarr;A 11, G&rarr;T 1 | `V` (97.4%) | 39 | 0.0% | 0-9% | 3,274 | 78.9% | 77-80% | 78.9% |  |
| reverse | 9 | 12 | `C` | C&rarr;T 32, C&rarr;G 1, C&rarr;A 1 | `B` (97.1%) | 34 | 0.0% | 0-10% | 3,279 | 78.8% | 77-80% | 78.8% |  |
| reverse | 1 | 20 | `A` | A&rarr;G 12, A&rarr;C 7, A&rarr;T 5 | hypervariable | 24 | 0.0% | 0-14% | 3,289 | 78.5% | 77-80% | 78.5% | yes |
| forward | 8 | 13 | `A` | A&rarr;T 26, A&rarr;G 5, A&rarr;C 4 | hypervariable | 35 | 2.9% | 1-15% | 3,278 | 78.8% | 77-80% | 75.9% |  |
| reverse | 12 | 9 | `C` | C&rarr;T 43, C&rarr;A 7, C&rarr;G 3 | hypervariable | 53 | 3.8% | 1-13% | 3,260 | 79.2% | 78-81% | 75.4% |  |
| forward | 14 | 7 | `G` | G&rarr;A 31, G&rarr;T 11, G&rarr;C 8 | hypervariable | 50 | 4.0% | 1-13% | 3,263 | 79.1% | 78-80% | 75.1% |  |
| reverse | 14 | 7 | `A` | A&rarr;T 12, A&rarr;C 10, A&rarr;G 2 | hypervariable | 24 | 4.2% | 1-20% | 3,289 | 78.5% | 77-80% | 74.3% |  |
| reverse | 11 | 10 | `C` | C&rarr;T 30, C&rarr;G 6, C&rarr;A 3 | hypervariable | 39 | 5.1% | 1-17% | 3,274 | 78.8% | 77-80% | 73.7% |  |
| forward | 3 | 18 | `H` | H&rarr;G 287 | hypervariable | 287 | 12.2% | 9-16% | 3,026 | 84.2% | 83-85% | 72.0% | yes |
| forward | 19 | 2 | `G` | G&rarr;T 25, G&rarr;A 2, G&rarr;C 2 | hypervariable | 29 | 10.3% | 4-26% | 3,284 | 78.6% | 77-80% | 68.2% |  |
| reverse | 15 | 6 | `K` | K&rarr;A 1,361, K&rarr;C 327 | hypervariable | 1,688 | 66.5% | 64-69% | 1,625 | 89.8% | 88-91% | 23.3% |  |
| forward | 12 | 9 | `T` | T&rarr;C 367, T&rarr;A 28, T&rarr;G 2 | `H` (99.5%) | 397 | 70.8% | 66-75% | 2,916 | 78.9% | 77-80% | 8.2% |  |
| forward | 9 | 12 | `K` | K&rarr;C 924, K&rarr;A 801 | hypervariable | 1,725 | 74.3% | 72-76% | 1,588 | 82.0% | 80-84% | 7.7% |  |
| forward | 6 | 15 | `K` | K&rarr;A 791, K&rarr;C 744 | hypervariable | 1,535 | 76.2% | 74-78% | 1,778 | 79.5% | 78-81% | 3.4% |  |
| reverse | 19 | 2 | `G` | G&rarr;T 353, G&rarr;C 73, G&rarr;A 37 | hypervariable | 463 | 75.4% | 71-79% | 2,850 | 78.4% | 77-80% | 3.0% |  |
| reverse | 20 | 1 | `G` | G&rarr;C 244, G&rarr;T 182, G&rarr;A 9 | `B` (97.9%) | 435 | 76.3% | 72-80% | 2,878 | 78.2% | 77-80% | 1.9% |  |
| forward | 18 | 3 | `K*` | K&rarr;C 927, K&rarr;A 343, G&rarr;A 261, +1 more | - | 1,533 | 78.6% | 76-81% | 1,780 | 77.4% | 75-79% | -1.2% |  |
| reverse | 13 | 8 | `C` | C&rarr;T 259, C&rarr;G 24, C&rarr;A 6 | `B` (97.9%) | 289 | 81.7% | 77-86% | 3,024 | 77.6% | 76-79% | -4.0% |  |
| forward | 16 | 5 | `A` | A&rarr;T 1,835 | `W` | 1,835 | 82.6% | 81-84% | 1,478 | 72.3% | 70-74% | -10.3% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 6,9,16,18; rev 15 | 186 | fail | 2023×38, 2024×10, 2025×26, 2026×10 | Murine astrovirus×29, Bovine astrovirus×19, Chicken astrovirus×19 | `QB068548`, `LC940228`, `ON885951`, `ON624262`, `ON624261`, `ON624258` (+180) |
| fwd 9,18; rev 15 | 166 | reduced | 2023×32, 2024×20, 2025×20, 2026×4 | Human astrovirus×122, Mamastrovirus×15, JP×8 | `PZ726271`, `LC940227`, `LC940226`, `PZ146428`, `PX255447`, `PX255446` (+160) |
| fwd 3,5; rev 15 | 166 | fail | 2023×30, 2024×5, 2025×7, 2026×5 | Goose astrovirus×166 | `PX703600`, `PX703595`, `PX703591`, `PX703590`, `PX489687`, `PX289198` (+160) |
| fwd 9,16,18; rev 15 | 144 | reduced | 2023×30, 2024×2, 2025×12, 2026×1 | Human astrovirus×34, Chicken astrovirus×24, Bovine astrovirus×12 | `ON624274`, `ON624270`, `ON624263`, `PX941959`, `LC900394`, `LC900392` (+138) |
| fwd 6,9,16; rev 13 | 140 | reduced | 2022×21, 2023×3, 2025×42, 2026×38 | Porcine astrovirus×78, Mamastrovirus×29, Mamastrovirus sp.×20 | `PX848849`, `LC900463`, `LC900458`, `LC900438`, `LC900398`, `LC900395` (+134) |
| fwd 16,18; rev 15 | 137 | reduced | 2023×17, 2024×15, 2025×30, 2026×3 | Canine astrovirus×44, Porcine astrovirus×23, Human astrovirus×19 | `PZ529594`, `PZ529593`, `ON624266`, `PX941894`, `PV730103`, `LC900450` (+131) |
| rev 19,20 | 109 | detect | 2008×5, 2009×70, 2012×10, 2014×1 | Turkey astrovirus×108, Avastrovirus×1 | `DQ381377`, `DQ381367`, `DQ381366`, `DQ066578`, `DQ066577`, `DQ066576` (+103) |
| fwd 6,16,18; rev 15 | 94 | reduced | 2022×6, 2023×22, 2025×15, 2026×6 | Astrovirus×18, Bovine astrovirus×16, Human astrovirus×9 | `QB068549`, `PP197223`, `ON885949`, `ON624283`, `ON624282`, `ON624281` (+88) |

## CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2

Coronaviridae (taxid 11118) — status **declining** — 6,864 evaluable of 25,559 screened records

- forward: `5'-GGCWCCWCCHGGNGARCAATT-3'` (21 nt)
- reverse: `5'-GGWAWCCCCAYTGYTGWAYRTC-3'` (22 nt)

**1,788 of 6,864 evaluable records (26%) share one mismatch pattern, mostly Porcine epidemic, deposited 1993-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 3 | 19 | `A` | A&rarr;G 1,701, A&rarr;C 96, A&rarr;T 7 | `V` (99.6%) | 1,804 | 5.7% | 5-7% | 5,060 | 95.2% | 95-96% | 89.5% | yes |
| forward | 5 | 17 | `C` | C&rarr;A 195, C&rarr;T 4 | `M` (98.0%) | 199 | 0.5% | 0-3% | 6,665 | 73.8% | 73-75% | 73.3% | yes |
| reverse | 17 | 6 | `C` | C&rarr;T 26, C&rarr;A 5 | `H` | 31 | 0.0% | 0-11% | 6,833 | 72.0% | 71-73% | 72.0% |  |
| reverse | 10 | 13 | `G` | G&rarr;T 29 | `K` | 29 | 0.0% | 0-12% | 6,835 | 72.0% | 71-73% | 72.0% |  |
| reverse | 11 | 12 | `T` | T&rarr;G 29 | `K` | 29 | 0.0% | 0-12% | 6,835 | 72.0% | 71-73% | 72.0% |  |
| reverse | 8 | 15 | `T` | T&rarr;G 27, T&rarr;C 1 | `K` (96.4%) | 28 | 0.0% | 0-12% | 6,836 | 72.0% | 71-73% | 72.0% |  |
| reverse | 7 | 16 | `G` | G&rarr;C 28 | `S` | 28 | 3.6% | 1-18% | 6,836 | 72.0% | 71-73% | 68.4% |  |
| forward | 20 | 2 | `G` | G&rarr;C 1,754, G&rarr;T 267, G&rarr;A 36 | `B` (98.2%) | 2,057 | 28.8% | 27-31% | 4,807 | 90.0% | 89-91% | 61.2% |  |
| forward | 19 | 3 | `C` | C&rarr;T 53, C&rarr;G 9 | `B` | 62 | 16.1% | 9-27% | 6,802 | 72.2% | 71-73% | 56.1% |  |
| reverse | 6 | 17 | `W` | W&rarr;G 269, W&rarr;C 76 | hypervariable | 345 | 21.4% | 17-26% | 6,519 | 74.4% | 73-75% | 52.9% |  |
| forward | 6 | 16 | `R` | R&rarr;C 581, R&rarr;T 428 | hypervariable | 1,009 | 27.4% | 25-30% | 5,855 | 79.3% | 78-80% | 52.0% |  |
| reverse | 21 | 2 | `G` | G&rarr;A 4,048 | `R` | 4,048 | 56.3% | 55-58% | 2,816 | 93.9% | 93-95% | 37.6% |  |
| reverse | 22 | 1 | `G` | G&rarr;T 4,145, G&rarr;C 1,608, G&rarr;A 1,037 | hypervariable | 6,790 | 71.4% | 70-73% | 74 | 94.6% | 87-98% | 23.2% |  |
| reverse | 18 | 5 | `W` | W&rarr;G 771, W&rarr;C 66 | hypervariable | 837 | 58.5% | 55-62% | 6,027 | 73.5% | 72-75% | 15.0% |  |
| forward | 15 | 7 | `W` | W&rarr;G 111, W&rarr;C 105 | hypervariable | 216 | 61.6% | 55-68% | 6,648 | 72.0% | 71-73% | 10.4% |  |
| forward | 21 | 1 | `G` | G&rarr;A 3,760, G&rarr;T 2,651, G&rarr;C 86, +1 more | `D` (98.7%) | 6,498 | 71.3% | 70-72% | 366 | 79.0% | 74-83% | 7.7% |  |
| forward | 18 | 4 | `W` | W&rarr;C 155, W&rarr;G 77 | hypervariable | 232 | 78.0% | 72-83% | 6,632 | 71.5% | 70-73% | -6.5% |  |
| reverse | 16 | 7 | `C` | C&rarr;T 90, C&rarr;G 5, C&rarr;A 1 | `B` (99.0%) | 96 | 90.6% | 83-95% | 6,768 | 71.4% | 70-72% | -19.2% |  |
| forward | 12 | 10 | `H` | H&rarr;G 302 | hypervariable | 302 | 93.7% | 90-96% | 6,562 | 70.7% | 70-72% | -23.0% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 21; rev 22 | 1,788 | detect | 2023×154, 2024×84, 2025×327, 2026×115 | Porcine epidemic×1110, Infectious bronchitis×526, Avian coronavirus×32 | `PZ799096`, `PZ463692`, `PX388002`, `PX388001`, `PZ949040`, `PZ012300` (+1,782) |
| fwd 21; rev 21,22 | 1,377 | reduced | 2023×267, 2024×126, 2025×121, 2026×218 | Human coronavirus×747, Bovine coronavirus×250, Infectious bronchitis×52 | `QB036323`, `LC918947`, `LC918946`, `LC642814`, `PZ892151`, `OZ540712` (+1,371) |
| fwd 3,20,21; rev 21,22 | 814 | fail | 2023×28, 2024×56, 2025×23, 2026×22 | Middle×769, Bat coronavirus×19, Pika coronavirus×16 | `PZ487753`, `PZ487748`, `PZ487747`, `PZ487746`, `PZ487745`, `PZ487742` (+808) |
| fwd 20,21; rev 21,22 | 357 | reduced | 2023×107, 2024×21, 2025×124, 2026×15 | Human coronavirus×247, Bat coronavirus×42, Bat×37 | `PZ673863`, `LC720428`, `LC687402`, `LC687394`, `LC895504`, `LC922677` (+351) |
| fwd 3,6,20,21; rev 18,21,22 | 273 | fail | 2018×6, 2020×1, 2024×1, 2026×2 | SARS coronavirus×268, Mutant×2, Betacoronavirus sp.×1 | `PV344447`, `PP862722`, `AY278489`, `MT308984`, `NC_004718`, `JX163928` (+267) |
| fwd 21; rev 18,22 | 135 | reduced | 2023×22, 2024×7, 2025×33, 2026×10 | Canine coronavirus×45, Porcine epidemic×26, Feline coronavirus×12 | `PX578493`, `PX578488`, `PP566960`, `OZ453836`, `PX797330`, `MW591993` (+129) |
| fwd 12,21; rev 18,21,22 | 114 | reduced | 2022×5, 2023×14, 2024×10, 2025×3 | Swine acute×56, Feline coronavirus×16, Bat×13 | `PX315754`, `PV652218`, `PV652217`, `PQ577606`, `PQ577605`, `PQ577604` (+108) |
| fwd 3,6,20,21; rev 21,22 | 112 | fail | 2023×24, 2024×2, 2025×2, 2026×26 | Bat coronavirus×32, Sarbecovirus sp.×29, Bat×13 | `PZ487758`, `PZ487757`, `PZ487756`, `PZ487755`, `PZ487754`, `PZ487752` (+106) |

## Pan_HERPES_dsDNA_Terminase_round2

Orthoherpesviridae (formerly Herpesviridae) (taxid 3044472) — status **declining** — 3,122 evaluable of 3,811 screened records

- forward: `5'-GCAAGATCATNTTYRTITCITC-3'` (22 nt)
- reverse: `5'-TGTTGGTCGTRWAIGCIGGRT-3'` (21 nt)

**514 of 3,122 evaluable records (16%) share one mismatch pattern, mostly Human herpesvirus, deposited 1990-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 20 | 2 | `G` | G&rarr;A 447, G&rarr;T 1 | `R` (99.8%) | 448 | 47.1% | 43-52% | 2,674 | 98.3% | 98-99% | 51.2% |  |
| forward | 21 | 2 | `C` | C&rarr;T 443, C&rarr;G 75, C&rarr;A 28 | hypervariable | 546 | 52.2% | 48-56% | 2,576 | 99.2% | 99-99% | 47.0% |  |
| forward | 18 | 5 | `G` | G&rarr;A 563 | `R` | 563 | 53.3% | 49-57% | 2,559 | 99.3% | 99-100% | 46.0% |  |
| reverse | 17 | 5 | `G` | G&rarr;T 629, G&rarr;A 62, G&rarr;C 46 | hypervariable | 737 | 66.5% | 63-70% | 2,385 | 98.5% | 98-99% | 32.0% |  |
| forward | 15 | 8 | `C` | C&rarr;T 1,379, C&rarr;A 285, C&rarr;G 69 | `H` (96.0%) | 1,733 | 84.0% | 82-86% | 1,389 | 99.7% | 99-100% | 15.8% |  |
| reverse | 14 | 8 | `C` | C&rarr;G 1,564, C&rarr;A 209, C&rarr;T 159 | hypervariable | 1,932 | 85.5% | 84-87% | 1,190 | 99.8% | 99-100% | 14.3% |  |
| reverse | 15 | 7 | `T` | T&rarr;C 1,064, T&rarr;A 269 | `H` | 1,333 | 82.8% | 81-85% | 1,789 | 97.0% | 96-98% | 14.2% |  |
| forward | 17 | 6 | `A` | A&rarr;C 217, A&rarr;T 7 | `M` (96.9%) | 224 | 83.9% | 79-88% | 2,898 | 91.5% | 90-92% | 7.6% |  |
| reverse | 16 | 6 | `G` | G&rarr;T 652, G&rarr;C 116, G&rarr;A 8 | `B` (99.0%) | 776 | 93.4% | 91-95% | 2,346 | 90.2% | 89-91% | -3.3% |  |
| forward | 14 | 9 | `A` | A&rarr;T 133, A&rarr;C 11, A&rarr;G 5 | `H` (96.6%) | 149 | 96.6% | 92-99% | 2,973 | 90.7% | 90-92% | -6.0% |  |
| reverse | 21 | 1 | `T` | T&rarr;G 636, T&rarr;C 317, T&rarr;A 174 | hypervariable | 1,127 | 95.7% | 94-97% | 1,995 | 88.3% | 87-90% | -7.5% |  |
| forward | 22 | 1 | `G` | G&rarr;C 1,325 | `S` | 1,325 | 95.5% | 94-96% | 1,797 | 87.6% | 86-89% | -7.8% |  |
| reverse | 12 | 10 | `T` | T&rarr;A 29 | `W` | 29 | 100.0% | 88-100% | 3,093 | 90.9% | 90-92% | -9.1% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 22; rev 14,21 | 514 | reduced | 2023×16, 2024×4, 2025×18, 2026×5 | Human herpesvirus×304, Human betaherpesvirus×184, Mutant×5 | `PZ050671`, `PZ050670`, `PZ050669`, `PZ137009`, `LC846339`, `LC846338` (+508) |
| fwd 15; rev 15 | 482 | detect | 2023×107, 2024×48, 2025×11, 2026×50 | Human alphaherpesvirus×367, Human herpesvirus×99, Mutant×7 | `PZ347688`, `PZ169720`, `PZ169719`, `PZ169718`, `PZ169717`, `PZ169716` (+476) |
| fwd 15,22; rev 14,16 | 431 | reduced | 2020×8, 2024×5, 2025×8, 2026×1 | UNVERIFIED_ASMBLY:×218, Human gammaherpesvirus×173, Human herpesvirus×28 | `PQ428139`, `PQ428134`, `PQ428132`, `PX940912`, `PV231823`, `OR134771` (+425) |
| rev 15 | 290 | detect | 2022×1, 2024×168, 2025×6, 2026×3 | Human alphaherpesvirus×261, Human herpesvirus×24, Chimpanzee alpha-1×2 | `PZ135825`, `PZ135824`, `PZ135823`, `MH790662`, `PX259988`, `PX259987` (+284) |
| fwd 15,18,21; rev 14,15,17,20 | 216 | fail | 2021×9, 2023×9, 2024×5, 2025×53 | Human alphaherpesvirus×112, Human herpesvirus×53, Varicellovirus humanalpha3×51 | `PX436161`, `PV845301`, `PV845300`, `PV845299`, `PV845298`, `PV845297` (+210) |
| fwd 14,15,17,18; rev 14,17 | 125 | reduced | 2023×12, 2024×17, 2025×1, 2026×7 | Gallid alphaherpesvirus×80, Gallid herpesvirus×30, Mutant×15 | `PZ112168`, `PX522223`, `PX496590`, `PX492157`, `PX499072`, `PX499071` (+119) |
| rev 14,17,20,21 | 123 | reduced | 2022×1, 2023×2, 2024×59, 2025×9 | Equid alphaherpesvirus×96, Equid herpesvirus×24, Equine herpesvirus×3 | `PQ630631`, `PQ630630`, `PQ630629`, `PQ630628`, `PQ630627`, `PQ630626` (+117) |
| fwd 21; rev 14,17,21 | 113 | reduced | 2021×13, 2023×29, 2024×8, 2025×8 | Felid alphaherpesvirus×108, Mutant×3, Felid herpesvirus×2 | `PV843457`, `PV209842`, `PQ672601`, `PQ672600`, `PQ672599`, `OR703025` (+107) |

## SARCOCYSTIS_18S_5_8s_rDNA_long_2010

Sarcocystis (taxid 5812) — status **watch** — 169 evaluable of 30,869 screened records

- forward: `5'-ATTGAGTGTTCCGGTGAATTA-3'` (21 nt)
- reverse: `5'-GCCATTTGCGTTCAGAAATC-3'` (20 nt)

No single position reaches the reporting threshold: the mismatches are spread thinly rather than concentrated. The footprint table below is the informative view for this assay.

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 155 | detect | 2020×5, 2021×6, 2024×6, 2025×6 | Sarcocystis lutrae×32, Sarcocystis sinensis×19, Sarcocystis miescheriana×16 | `PX632651`, `PX632650`, `PX632649`, `PX632648`, `PV470858`, `PV470857` (+149) |
| rev 2 | 4 | detect | 2017×3, 2018×1 | Sarcocystis dehongensis×3, Sarcocystis bertrami×1 | `MH025635`, `KY711380`, `KY711379`, `KY711378` |
| fwd 4 | 2 | reduced | 2018×2 | Sarcocystis arieticanis×2 | `MH413044`, `MH413043` |
| fwd 11,12,20; rev 3,8,11 | 1 | fail | 2024×1 | Sarcocystis calchasi×1 | `CAXOTS010000001` |
| fwd 4,5,12,18,20; rev 10,11,18,19 | 1 | fail | 2024×1 | Sarcocystis calchasi×1 | `CAXOTS010000012` |
| fwd 2,3,5,6,8,17; rev 2,13,17,18,19 | 1 | fail | 2023×1 | TSA:×1 | `ICSQ01000001` |
| fwd 1,2,3,11,14; rev 1 | 1 | fail | 2019×1 | Sarcocystis sp.×1 | `MH590233` |
| rev 9,12,13 | 1 | reduced | 2018×1 | Sarcocystis tenella×1 | `MH413042` |

## VIBRIO_coralliilyticus_dnaJ_Pollock_2010

Vibrio coralliilyticus (taxid 190893) — status **watch** — 71 evaluable of 139 screened records

- forward: `5'-CGGTTCGYGGTGTTTCAAAA-3'` (20 nt)
- reverse: `5'-AACCTGACCATGACCGTGACA-3'` (21 nt)
- probe: `5'-CAGTGGCGCGAAG-3'` (13 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| probe | 7 | 7 | `C` | C&rarr;T 21 | `Y` | 21 | 14.3% | 5-35% | 50 | 100.0% | 93-100% | 85.7% |  |
| probe | 10 | 4 | `T` | T&rarr;C 23 | `Y` | 23 | 21.7% | 10-42% | 48 | 100.0% | 93-100% | 78.3% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 44 | detect | 2020×13, 2024×6, 2025×2, 2026×8 | Vibrio coralliilyticus×44 | `NZ_JCBDGT010000041`, `NZ_CM184931`, `CM184931`, `NZ_CP156653`, `NZ_CP156656`, `NZ_JABSNA010000013` (+38) |
| fwd 19; prb 7,10 | 6 | fail | 2017×2, 2020×1, 2024×1, 2026×2 | Vibrio coralliilyticus×6 | `NZ_CM184933`, `CM184933`, `NZ_VTXB01000005`, `NZ_NRQO01000005`, `NZ_JAPVQX010000005`, `NRQO01000005` |
| fwd 19; rev 12; prb 7,10 | 5 | fail | 2015×2, 2020×2, 2026×1 | Vibrio coralliilyticus×5 | `NZ_JCAFVU010000005`, `NZ_CP063051`, `NZ_JXXS01000030`, `CP063051`, `JXXS01000030` |
| rev 6; prb 7,10 | 4 | fail | 2015×1, 2016×1, 2018×1, 2019×1 | Vibrio coralliilyticus×4 | `NZ_LGLS01000002`, `NZ_CP031472`, `CP031472`, `LGLS01000002` |
| prb 7,10 | 3 | reduced | 2020×2, 2021×1 | Vibrio coralliilyticus×3 | `NZ_VTYL01000007`, `NZ_VTYG01000008`, `NZ_JAJENQ010000003` |
| fwd 19 | 2 | detect | 2020×1, 2026×1 | Vibrio coralliilyticus×2 | `NZ_JCBDHA010000577`, `NZ_VTXA01000005` |
| prb 6 | 2 | reduced | 2016×2 | Vibrio coralliilyticus×2 | `NZ_CP016556`, `CP016556` |
| fwd 16,19; rev 12; prb 7,10,13 | 2 | fail | 2023×2 | Vibrio coralliilyticus×2 | `NZ_CP120719`, `CP120719` |

## Pan_HERPES_dsDNA_Polymerase_round2

Orthoherpesviridae (formerly Herpesviridae) (taxid 3044472) — status **low coverage** — 3,671 evaluable of 7,713 screened records

- forward: `5'-TGTAACTCGGTGTAYGGNTTYACNGGNGT-3'` (29 nt)
- reverse: `5'-CACAGAGTCCGTRTCNCCRTADAT-3'` (24 nt)

**864 of 3,671 evaluable records (24%) share one mismatch pattern, mostly Human alphaherpesvirus, deposited 1986-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 19 | 6 | `A` | A&rarr;T 232 | `W` | 232 | 3.4% | 2-7% | 3,439 | 91.5% | 91-92% | 88.1% |  |
| reverse | 20 | 5 | `G` | G&rarr;C 232 | `S` | 232 | 3.4% | 2-7% | 3,439 | 91.5% | 91-92% | 88.1% |  |
| forward | 20 | 10 | `G` | G&rarr;T 157, G&rarr;A 1 | `K` (99.4%) | 158 | 1.9% | 1-5% | 3,513 | 89.7% | 89-91% | 87.8% |  |
| forward | 1 | 29 | `T` | T&rarr;C 59, T&rarr;G 1 | `Y` (98.3%) | 60 | 0.0% | 0-6% | 3,611 | 87.4% | 86-88% | 87.4% | yes |
| forward | 11 | 19 | `T` | T&rarr;G 38 | `K` | 38 | 0.0% | 0-9% | 3,633 | 86.8% | 86-88% | 86.8% |  |
| forward | 7 | 23 | `C` | C&rarr;G 128, C&rarr;A 3 | `S` (97.7%) | 131 | 2.3% | 1-7% | 3,540 | 89.0% | 88-90% | 86.7% |  |
| forward | 8 | 22 | `A` | A&rarr;T 128, A&rarr;C 3, A&rarr;G 2 | `W` (96.2%) | 133 | 3.0% | 1-7% | 3,538 | 89.1% | 88-90% | 86.1% |  |
| reverse | 3 | 22 | `D` | D&rarr;C 38 | hypervariable | 38 | 5.3% | 1-17% | 3,633 | 86.8% | 86-88% | 81.5% | yes |
| reverse | 15 | 10 | `C` | C&rarr;G 513, C&rarr;T 293, C&rarr;A 261 | hypervariable | 1,067 | 60.1% | 57-63% | 2,604 | 96.5% | 96-97% | 36.5% |  |
| forward | 24 | 6 | `C` | C&rarr;T 630 | `Y` | 630 | 61.6% | 58-65% | 3,041 | 91.0% | 90-92% | 29.4% |  |
| forward | 23 | 7 | `T` | T&rarr;G 854 | `K` | 854 | 66.4% | 63-69% | 2,817 | 91.9% | 91-93% | 25.5% |  |
| forward | 18 | 12 | `G` | G&rarr;C 592, G&rarr;T 477, G&rarr;A 474 | hypervariable | 1,543 | 75.0% | 73-77% | 2,128 | 93.9% | 93-95% | 18.9% |  |
| reverse | 18 | 7 | `G` | G&rarr;A 794 | `R` | 794 | 72.8% | 70-76% | 2,877 | 89.6% | 88-91% | 16.8% |  |
| forward | 21 | 9 | `G` | G&rarr;C 1,124, G&rarr;T 300, G&rarr;A 163 | hypervariable | 1,587 | 77.2% | 75-79% | 2,084 | 92.6% | 91-94% | 15.4% |  |
| reverse | 1 | 24 | `T` | T&rarr;C 296 | `Y` | 296 | 74.7% | 69-79% | 3,375 | 86.9% | 86-88% | 12.3% | yes |
| reverse | 24 | 1 | `C` | C&rarr;T 1,143, C&rarr;A 640, C&rarr;G 458 | hypervariable | 2,241 | 85.4% | 84-87% | 1,430 | 86.9% | 85-89% | 1.5% |  |
| forward | 27 | 3 | `T` | T&rarr;C 1,783 | `Y` | 1,783 | 85.4% | 84-87% | 1,888 | 86.5% | 85-88% | 1.1% |  |
| reverse | 22 | 3 | `C` | C&rarr;T 1,410, C&rarr;G 710, C&rarr;A 17 | `B` (99.2%) | 2,137 | 90.6% | 89-92% | 1,534 | 79.4% | 77-81% | -11.2% |  |
| reverse | 21 | 4 | `A` | A&rarr;G 2,116, A&rarr;C 745, A&rarr;T 21 | `V` (99.3%) | 2,882 | 88.4% | 87-90% | 789 | 76.8% | 74-80% | -11.6% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 21,22,24 | 864 | reduced | 2023×129, 2024×49, 2025×15, 2026×47 | Human alphaherpesvirus×603, Human herpesvirus×252, Mutant×6 | `PZ347688`, `PV105598`, `PV105591`, `PV105590`, `PV105585`, `PZ169712` (+858) |
| fwd 18,21,23,27; rev 21,22 | 484 | reduced | 2021×1, 2023×1, 2024×3, 2025×8 | UNVERIFIED_ASMBLY:×230, Human gammaherpesvirus×217, Human herpesvirus×27 | `PQ428139`, `PQ428134`, `OR134772`, `OR134771`, `OR134770`, `OR134769` (+478) |
| fwd 27; rev 21,22,24 | 428 | reduced | 2023×2, 2024×167, 2025×7, 2026×12 | Human alphaherpesvirus×310, Human herpesvirus×105, Macacine alphaherpesvirus×7 | `PX974241`, `PZ135825`, `PZ135824`, `PZ135823`, `PZ169720`, `PZ169719` (+422) |
| fwd 21,24; rev 18 | 314 | reduced | 2023×9, 2024×5, 2025×55, 2026×6 | Human alphaherpesvirus×203, Human herpesvirus×57, Varicellovirus humanalpha3×51 | `PV796772`, `PV796771`, `PV796770`, `PV737807`, `PV737806`, `PV700517` (+308) |
| fwd 18,27; rev 15,21 | 238 | reduced | 2022×1, 2023×1, 2024×58, 2025×22 | Equid herpesvirus×119, Equid alphaherpesvirus×117, Equine herpesvirus×2 | `PQ630631`, `PQ630630`, `PQ630629`, `PQ630628`, `PQ630627`, `PQ630626` (+232) |
| fwd 27; rev 1,21,24 | 180 | reduced | 2023×20, 2024×4, 2025×13, 2026×24 | Suid alphaherpesvirus×76, Bovine alphaherpesvirus×68, Suid herpesvirus×17 | `PQ662995`, `PQ662994`, `PQ662993`, `PQ662992`, `PQ662991`, `PQ662990` (+174) |
| fwd 18,21; rev 15,18,24 | 129 | reduced | 2023×12, 2024×17, 2025×1, 2026×7 | Gallid alphaherpesvirus×80, Gallid herpesvirus×28, Mutant×15 | `PZ112168`, `PX522223`, `PX496590`, `PX492157`, `PX499072`, `PX499071` (+123) |
| fwd 18,21; rev 15,18,21,24 | 113 | reduced | 2021×13, 2023×29, 2024×8, 2025×8 | Felid alphaherpesvirus×108, Mutant×3, Felid herpesvirus×2 | `PV843457`, `PV209842`, `PQ672601`, `PQ672600`, `PQ672599`, `OR703025` (+107) |

## ADENOVIRUS_dsDNA_Polymerase_Primate_speci

Mastadenovirus (taxid 10509) — status **low coverage** — 4,184 evaluable of 30,214 screened records

- forward: `5'-GTGACAAAGAGGCTGTCCGTGTCCCCGTA-3'` (29 nt)
- reverse: `5'-TCACGTGGCCTACACTTACAAGCCAATCAC-3'` (30 nt)

**541 of 4,184 evaluable records (13%) share one mismatch pattern, mostly Human adenovirus, deposited 1985-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 18 | 13 | `C` | C&rarr;T 371 | `Y` | 371 | 0.8% | 0-2% | 3,813 | 88.1% | 87-89% | 87.3% |  |
| forward | 6 | 24 | `C` | C&rarr;T 459, C&rarr;G 394, C&rarr;A 5 | `B` (99.4%) | 858 | 13.9% | 12-16% | 3,326 | 97.5% | 97-98% | 83.6% |  |
| forward | 18 | 12 | `G` | G&rarr;A 229, G&rarr;C 1 | `R` (99.6%) | 230 | 1.7% | 1-4% | 3,954 | 84.9% | 84-86% | 83.2% |  |
| reverse | 3 | 28 | `C` | C&rarr;T 59, C&rarr;A 11 | `H` | 70 | 0.0% | 0-5% | 4,114 | 81.7% | 81-83% | 81.7% | yes |
| reverse | 30 | 1 | `T` | T&rarr;C 64, T&rarr;A 26, T&rarr;G 1 | `H` (98.9%) | 91 | 2.2% | 1-8% | 4,093 | 82.1% | 81-83% | 79.9% |  |
| forward | 25 | 5 | `C` | C&rarr;G 30, C&rarr;A 6, C&rarr;T 2 | hypervariable | 38 | 13.2% | 6-27% | 4,146 | 81.0% | 80-82% | 67.8% |  |
| forward | 19 | 11 | `G` | G&rarr;A 98, G&rarr;T 16, G&rarr;C 1 | `D` (99.1%) | 115 | 14.8% | 9-22% | 4,069 | 82.2% | 81-83% | 67.4% |  |
| reverse | 23 | 8 | `G` | G&rarr;A 1,152, G&rarr;T 19 | `R` (98.4%) | 1,171 | 34.2% | 31-37% | 3,013 | 98.3% | 98-99% | 64.1% |  |
| forward | 9 | 21 | `G` | G&rarr;A 61 | `R` | 61 | 24.6% | 16-37% | 4,123 | 81.2% | 80-82% | 56.6% |  |
| forward | 12 | 18 | `C` | C&rarr;G 730, C&rarr;T 399, C&rarr;A 53 | `B` (95.5%) | 1,182 | 40.3% | 38-43% | 3,002 | 96.1% | 95-97% | 55.9% |  |
| reverse | 12 | 19 | `C` | C&rarr;T 703 | `Y` | 703 | 40.8% | 37-44% | 3,481 | 88.3% | 87-89% | 47.5% |  |
| reverse | 16 | 15 | `C` | C&rarr;A 18, C&rarr;T 10 | `H` | 28 | 35.7% | 21-54% | 4,156 | 80.7% | 79-82% | 44.9% |  |
| reverse | 9 | 22 | `G` | G&rarr;A 1,811 | `R` | 1,811 | 61.4% | 59-64% | 2,373 | 94.8% | 94-96% | 33.4% |  |
| reverse | 21 | 10 | `C` | C&rarr;A 715, C&rarr;T 254, C&rarr;G 6 | `H` (99.4%) | 975 | 62.5% | 59-65% | 3,209 | 85.8% | 85-87% | 23.3% |  |
| forward | 27 | 3 | `G` | G&rarr;A 177, G&rarr;C 42, G&rarr;T 16 | hypervariable | 235 | 74.9% | 69-80% | 3,949 | 80.7% | 79-82% | 5.8% |  |
| forward | 21 | 9 | `G` | G&rarr;A 1,258, G&rarr;C 788, G&rarr;T 12 | `V` (99.4%) | 2,058 | 79.1% | 77-81% | 2,126 | 81.6% | 80-83% | 2.5% |  |
| reverse | 15 | 16 | `T` | T&rarr;C 2,016, T&rarr;A 21, T&rarr;G 10 | `Y` (98.5%) | 2,047 | 82.2% | 80-84% | 2,137 | 78.6% | 77-80% | -3.6% |  |
| reverse | 22 | 9 | `C` | C&rarr;A 327, C&rarr;T 1, C&rarr;G 1 | `M` (99.4%) | 329 | 87.2% | 83-90% | 3,855 | 79.8% | 78-81% | -7.5% |  |
| forward | 24 | 6 | `A` | A&rarr;G 1,136 | `R` | 1,136 | 91.1% | 89-93% | 3,048 | 76.3% | 75-78% | -14.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 1,212 | detect | 2023×72, 2024×139, 2025×124, 2026×311 | Human adenovirus×932, Human mastadenovirus×158, JP×33 | `PZ576384`, `PZ576383`, `PZ576382`, `PZ576381`, `PZ576380`, `PZ576379` (+1,206) |
| fwd 21,24; rev 9,15 | 541 | reduced | 2023×136, 2024×27, 2025×39, 2026×77 | Human adenovirus×190, Human mastadenovirus×159, KR×62 | `PW424730`, `QV000696`, `PZ410862`, `LC879952`, `LC879951`, `LC879947` (+535) |
| fwd 6,12; rev 9,12,18,23 | 334 | fail | 2023×42, 2024×33, 2025×48, 2026×22 | Human adenovirus×213, Human mastadenovirus×117, Mastadenovirus×2 | `PZ683035`, `PZ683031`, `PZ411221`, `PZ411189`, `PZ410871`, `PZ360999` (+328) |
| fwd 12,21; rev 15 | 329 | reduced | 2023×32, 2024×8, 2025×3, 2026×2 | Human adenovirus×241, Human mastadenovirus×76, Sequence×6 | `PV780771`, `PX951443`, `PX121480`, `FJ169625`, `PV359444`, `PQ738617` (+323) |
| fwd 21; rev 15,21,22,23 | 287 | reduced | 2023×17, 2024×23, 2025×68, 2026×5 | Human adenovirus×226, Human mastadenovirus×30, Sequence×10 | `LC945760`, `PX461456`, `PX461455`, `PX491610`, `PV980178`, `PV980177` (+281) |
| fwd 21,24; rev 9,12,15 | 280 | reduced | 2023×75, 2024×7, 2025×35, 2026×32 | Human adenovirus×194, Human mastadenovirus×71, JP×4 | `PW424729`, `PZ726818`, `PZ411237`, `PZ411234`, `PZ411230`, `PZ411229` (+274) |
| rev 21 | 201 | detect | 2023×36, 2024×8, 2025×25, 2026×100 | Human adenovirus×123, Human mastadenovirus×50, JP×9 | `LC882652`, `LC882651`, `LC882650`, `LC882649`, `LC882648`, `LC882647` (+195) |
| fwd 6,12,18,21; rev 9,15,21,23 | 169 | fail | 2022×98, 2023×25, 2024×1, 2026×3 | Human adenovirus×127, Human mastadenovirus×40, Mastadenovirus sp.×2 | `PZ023991`, `PX951442`, `PX905700`, `OQ744647`, `LC791110`, `OQ518334` (+163) |

## Entamoeba_18S_small_subunit_SSU

Entamoeba (taxid 5758) — status **watch** — 214 evaluable of 3,324 screened records

- forward: `5'-CGAACGAGACTKDAWCYTATTWAT-3'` (24 nt)
- reverse: `5'-AATTTCACCTHTWTITTCAATC-3'` (22 nt)

**59 of 214 evaluable records (28%) share one mismatch pattern, mostly Entamoeba bovis, deposited 2010-2023, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 10 | 15 | `W` | W&rarr;G 71 | `D` | 71 | 84.5% | 74-91% | 143 | 100.0% | 97-100% | 15.5% |  |
| reverse | 6 | 17 | `T` | T&rarr;C 71 | `Y` | 71 | 84.5% | 74-91% | 143 | 100.0% | 97-100% | 15.5% |  |
| reverse | 11 | 12 | `T` | T&rarr;C 72, T&rarr;A 1 | `Y` (98.6%) | 73 | 84.9% | 75-91% | 141 | 100.0% | 97-100% | 15.1% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 131 | detect | 2023×9, 2024×2, 2025×8, 2026×1 | Entamoeba polecki×29, Entamoeba gingivalis×14, Entamoeba hartmanni×12 | `PZ193673`, `LC901119`, `PQ389466`, `PQ389467`, `PQ389465`, `PQ389464` (+125) |
| fwd 10; rev 6,11 | 59 | reduced | 2010×8, 2015×1, 2017×3, 2023×47 | Entamoeba bovis×38, Entamoeba sp.×18, Entamoeba cf.×3 | `OM900113`, `OM900112`, `OM900111`, `OM900110`, `OM900109`, `OM900108` (+53) |
| fwd 10; rev 6,9,11 | 11 | fail | 2010×1, 2023×10 | Entamoeba sp.×11 | `OM900095`, `OM900091`, `OM900089`, `OM900080`, `OM900069`, `OM900067` (+5) |
| rev 22 | 7 | detect | 1999×2, 2009×1, 2010×3, 2020×1 | Entamoeba coli×7 | `MN914079`, `AB444953`, `FR686449`, `FR686439`, `FR686364`, `AF149915` (+1) |
| fwd 10; rev 7,11 | 1 | reduced | 2023×1 | Entamoeba sp.×1 | `OM900060` |
| fwd 5,6; rev 4 | 1 | reduced | 2009×1 | Entamoeba muris×1 | `AB445018` |
| rev 10 | 1 | detect | 2010×1 | Entamoeba sp.×1 | `FR686365` |
| fwd 5,6; rev 13,22 | 1 | reduced | 2010×1 | Entamoeba sp.×1 | `FR686360` |

## ADENOVIRUS_dsDNA_Hexon_gene_round2

Adenoviridae (taxid 10508) — status **low coverage** — 6,010 evaluable of 38,963 screened records

- forward: `5'-CCCITTYAACCACCACCG-3'` (18 nt)
- reverse: `5'-KATGGGGTARAGCATGTT-3'` (18 nt)

**978 of 6,010 evaluable records (16%) share one mismatch pattern, mostly Human adenovirus, deposited 1990-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 14 | 5 | `G` | G&rarr;T 239, G&rarr;C 31, G&rarr;A 20 | hypervariable | 290 | 0.3% | 0-2% | 5,720 | 94.6% | 94-95% | 94.3% |  |
| reverse | 5 | 14 | `A` | A&rarr;G 198, A&rarr;T 38, A&rarr;C 3 | `D` (98.7%) | 239 | 0.0% | 0-2% | 5,771 | 93.8% | 93-94% | 93.8% | yes |
| reverse | 4 | 15 | `T` | T&rarr;C 199, T&rarr;G 38, T&rarr;A 13 | hypervariable | 250 | 0.4% | 0-2% | 5,760 | 94.0% | 93-95% | 93.6% | yes |
| reverse | 16 | 3 | `T` | T&rarr;C 256, T&rarr;G 30, T&rarr;A 2 | `B` (99.3%) | 288 | 2.4% | 1-5% | 5,722 | 94.5% | 94-95% | 92.0% |  |
| forward | 11 | 8 | `A` | A&rarr;C 57, A&rarr;T 36, A&rarr;G 12 | hypervariable | 105 | 0.0% | 0-4% | 5,905 | 91.7% | 91-92% | 91.7% |  |
| forward | 14 | 5 | `T` | T&rarr;C 48, T&rarr;G 33, T&rarr;A 8 | hypervariable | 89 | 0.0% | 0-4% | 5,921 | 91.4% | 91-92% | 91.4% |  |
| forward | 16 | 3 | `C` | C&rarr;A 39, C&rarr;T 28, C&rarr;G 8 | hypervariable | 75 | 0.0% | 0-5% | 5,935 | 91.2% | 90-92% | 91.2% |  |
| forward | 8 | 11 | `C` | C&rarr;T 33, C&rarr;A 27, C&rarr;G 12 | hypervariable | 72 | 0.0% | 0-5% | 5,938 | 91.2% | 90-92% | 91.2% |  |
| reverse | 10 | 9 | `A` | A&rarr;T 36, A&rarr;C 23, A&rarr;G 6 | hypervariable | 65 | 0.0% | 0-6% | 5,945 | 91.1% | 90-92% | 91.1% |  |
| forward | 10 | 9 | `A` | A&rarr;G 41, A&rarr;T 14, A&rarr;C 6 | hypervariable | 61 | 0.0% | 0-6% | 5,949 | 91.0% | 90-92% | 91.0% |  |
| forward | 17 | 2 | `C` | C&rarr;G 28, C&rarr;A 11, C&rarr;T 10 | hypervariable | 49 | 0.0% | 0-7% | 5,961 | 90.8% | 90-92% | 90.8% |  |
| forward | 7 | 12 | `A` | A&rarr;T 23, A&rarr;G 19, A&rarr;C 3 | hypervariable | 45 | 0.0% | 0-8% | 5,965 | 90.7% | 90-91% | 90.7% |  |
| forward | 5 | 14 | `C` | C&rarr;A 26, C&rarr;T 8, C&rarr;W 1 | `H` (97.1%) | 35 | 0.0% | 0-10% | 5,975 | 90.6% | 90-91% | 90.6% | yes |
| forward | 4 | 15 | `A` | A&rarr;T 24, A&rarr;C 5, A&rarr;G 2 | hypervariable | 31 | 0.0% | 0-11% | 5,979 | 90.5% | 90-91% | 90.5% | yes |
| reverse | 17 | 2 | `A` | A&rarr;T 45, A&rarr;C 25, A&rarr;G 14 | hypervariable | 84 | 1.2% | 0-6% | 5,926 | 91.3% | 91-92% | 90.1% |  |
| reverse | 13 | 6 | `G` | G&rarr;C 54, G&rarr;T 35, G&rarr;A 17 | hypervariable | 106 | 2.8% | 1-8% | 5,904 | 91.6% | 91-92% | 88.8% |  |
| reverse | 1 | 18 | `T` | T&rarr;A 27, T&rarr;G 24, T&rarr;C 7 | hypervariable | 58 | 3.4% | 1-12% | 5,952 | 90.9% | 90-92% | 87.5% | yes |
| forward | 13 | 6 | `T` | T&rarr;G 37, T&rarr;A 16, T&rarr;C 11 | hypervariable | 64 | 6.2% | 2-15% | 5,946 | 91.0% | 90-92% | 84.7% |  |
| reverse | 8 | 11 | `A` | A&rarr;G 14, A&rarr;T 12, A&rarr;C 4 | hypervariable | 30 | 6.7% | 2-21% | 5,980 | 90.5% | 90-91% | 83.8% |  |
| reverse | 11 | 8 | `T` | T&rarr;A 69, T&rarr;G 17, T&rarr;C 17 | hypervariable | 103 | 11.7% | 7-19% | 5,907 | 91.4% | 91-92% | 79.8% |  |
| reverse | 6 | 13 | `C` | C&rarr;A 51, C&rarr;T 35, C&rarr;G 21 | hypervariable | 107 | 13.1% | 8-21% | 5,903 | 91.5% | 91-92% | 78.4% |  |
| forward | 3 | 16 | `C` | C&rarr;T 87, C&rarr;G 32, C&rarr;A 10 | hypervariable | 129 | 14.7% | 10-22% | 5,881 | 91.7% | 91-92% | 77.0% | yes |
| forward | 1 | 18 | `G` | G&rarr;A 45, G&rarr;T 28, G&rarr;C 6 | hypervariable | 79 | 15.2% | 9-25% | 5,931 | 91.1% | 90-92% | 75.9% | yes |
| reverse | 2 | 17 | `T` | T&rarr;C 29, T&rarr;G 24, T&rarr;A 23 | hypervariable | 76 | 15.8% | 9-26% | 5,934 | 91.0% | 90-92% | 75.2% | yes |
| reverse | 3 | 16 | `G` | G&rarr;A 34, G&rarr;C 11, G&rarr;T 1 | `V` (97.8%) | 46 | 26.1% | 16-40% | 5,964 | 90.6% | 90-91% | 64.5% | yes |
| forward | 2 | 17 | `C` | C&rarr;A 224, C&rarr;T 8, C&rarr;G 3 | `M` (95.3%) | 235 | 36.2% | 30-42% | 5,775 | 92.3% | 92-93% | 56.1% | yes |
| reverse | 15 | 4 | `G` | G&rarr;A 438, G&rarr;C 252, G&rarr;T 106 | hypervariable | 796 | 57.7% | 54-61% | 5,214 | 95.0% | 94-96% | 37.4% |  |
| reverse | 7 | 12 | `G` | G&rarr;A 279, G&rarr;T 12 | `R` (95.9%) | 291 | 70.8% | 65-76% | 5,719 | 91.0% | 90-92% | 20.3% |  |
| forward | 6 | 13 | `C` | C&rarr;T 532, C&rarr;G 26, C&rarr;A 5 | `B` (99.1%) | 563 | 81.9% | 78-85% | 5,447 | 90.9% | 90-92% | 9.0% |  |
| forward | 9 | 10 | `C` | C&rarr;T 681, C&rarr;G 13, C&rarr;A 8 | `Y` (97.0%) | 702 | 85.6% | 83-88% | 5,308 | 90.7% | 90-91% | 5.0% |  |
| reverse | 18 | 1 | `K` | K&rarr;A 2,071, K&rarr;C 161 | hypervariable | 2,232 | 87.2% | 86-89% | 3,778 | 91.7% | 91-93% | 4.5% |  |
| reverse | 9 | 10 | `R` | R&rarr;T 743, R&rarr;C 491 | hypervariable | 1,234 | 87.9% | 86-90% | 4,776 | 90.6% | 90-91% | 2.7% |  |
| reverse | 12 | 7 | `G` | G&rarr;A 1,353, G&rarr;T 6 | `R` (99.6%) | 1,359 | 89.1% | 87-91% | 4,651 | 90.3% | 89-91% | 1.2% |  |
| forward | 18 | 1 | `C` | C&rarr;T 2,820, C&rarr;A 15, C&rarr;G 8 | `Y` (99.2%) | 2,843 | 91.0% | 90-92% | 3,167 | 89.2% | 88-90% | -1.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 18 | 978 | detect | 2023×19, 2024×57, 2025×50, 2026×230 | Human adenovirus×887, Human mastadenovirus×45, Sequence×18 | `PX059042`, `PX059041`, `PX059040`, `PX059039`, `PX059038`, `PX059037` (+972) |
| fwd 18; rev 18 | 717 | detect | 2023×89, 2024×70, 2025×117, 2026×240 | Human adenovirus×496, Human mastadenovirus×174, KR×13 | `PZ576384`, `PZ576383`, `PZ576382`, `PZ576381`, `PZ576380`, `PZ576379` (+711) |
| no mismatches | 711 | detect | 2023×88, 2024×16, 2025×5, 2026×9 | Human adenovirus×357, Human mastadenovirus×138, Sequence×82 | `PV780771`, `HC191035`, `HC191003`, `CS138464`, `CS138463`, `QS054961` (+705) |
| fwd 18; rev 9 | 596 | reduced | 2023×91, 2024×32, 2025×53, 2026×94 | Human adenovirus×328, Human mastadenovirus×246, KR×4 | `PW424729`, `PZ411234`, `PZ410989`, `PZ410971`, `PZ410962`, `PZ410940` (+590) |
| fwd 9; rev 12,18 | 471 | reduced | 2023×47, 2024×53, 2025×44, 2026×97 | Human adenovirus×317, Human mastadenovirus×150, Mastadenovirus×1 | `PX059115`, `PX059114`, `PX059113`, `PX059112`, `PX059111`, `PX059110` (+465) |
| fwd 6 | 394 | detect | 2023×96, 2024×5, 2025×23, 2026×57 | Human adenovirus×221, Human mastadenovirus×150, Sequence×6 | `PZ726819`, `PZ411255`, `PZ411237`, `PZ411235`, `PZ411229`, `PZ411227` (+388) |
| rev 15 | 360 | detect | 2023×76, 2024×14, 2025×19, 2026×33 | Human adenovirus×81, Human mastadenovirus×79, KR×66 | `PW424730`, `QV000696`, `PZ411233`, `PZ411232`, `PZ410841`, `QT662143` (+354) |
| rev 12,18 | 274 | detect | 2023×16, 2024×20, 2025×63, 2026×5 | Human adenovirus×246, Human mastadenovirus×27, Unidentified adenovirus×1 | `LC945760`, `PX461456`, `PX461455`, `PX491610`, `PV980178`, `PV980177` (+268) |

## HANTAVIRUS_ssRNA_S_segment

Orthohantavirus (taxid 1980442) — status **declining** — 4,316 evaluable of 16,179 screened records

- forward: `5'-GWGGVCARACWGCHGAYT-3'` (18 nt)
- reverse: `5'-CCWGGTGTDADYTCHTCWGC-3'` (20 nt)

**1,341 of 4,316 evaluable records (31%) share one mismatch pattern, mostly Orthohantavirus hantanense, deposited 1987-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 1 | 20 | `C` | C&rarr;A 62, C&rarr;T 57, C&rarr;G 1 | `H` (99.2%) | 120 | 0.0% | 0-3% | 4,196 | 98.3% | 98-99% | 98.3% | yes |
| forward | 16 | 3 | `G` | G&rarr;A 55, G&rarr;T 31, G&rarr;C 12 | hypervariable | 98 | 0.0% | 0-4% | 4,218 | 97.8% | 97-98% | 97.8% |  |
| forward | 2 | 17 | `Y` | Y&rarr;G 38, Y&rarr;A 27 | hypervariable | 65 | 0.0% | 0-6% | 4,251 | 97.1% | 97-98% | 97.1% | yes |
| forward | 1 | 18 | `T` | T&rarr;A 25, T&rarr;G 19, T&rarr;C 3 | hypervariable | 47 | 0.0% | 0-8% | 4,269 | 96.7% | 96-97% | 96.7% | yes |
| forward | 7 | 12 | `G` | G&rarr;A 21, G&rarr;C 17, G&rarr;T 9 | hypervariable | 47 | 0.0% | 0-8% | 4,269 | 96.7% | 96-97% | 96.7% |  |
| reverse | 2 | 19 | `G` | G&rarr;A 83, G&rarr;T 6, G&rarr;C 2 | `D` (97.8%) | 91 | 1.1% | 0-6% | 4,225 | 97.6% | 97-98% | 96.5% | yes |
| reverse | 8 | 13 | `T` | T&rarr;C 39, T&rarr;A 1 | `Y` (97.5%) | 40 | 0.0% | 0-9% | 4,276 | 96.5% | 96-97% | 96.5% |  |
| forward | 15 | 4 | `G` | G&rarr;T 52, G&rarr;C 32, G&rarr;A 21 | hypervariable | 105 | 1.9% | 1-7% | 4,211 | 97.9% | 97-98% | 96.0% |  |
| reverse | 13 | 8 | `T` | T&rarr;A 60, T&rarr;C 11, T&rarr;G 6 | hypervariable | 77 | 1.3% | 0-7% | 4,239 | 97.3% | 97-98% | 96.0% |  |
| reverse | 5 | 16 | `T` | T&rarr;G 62, T&rarr;C 7, T&rarr;A 5 | hypervariable | 74 | 1.4% | 0-7% | 4,242 | 97.2% | 97-98% | 95.9% | yes |
| forward | 9 | 10 | `C` | C&rarr;A 52, C&rarr;T 14, C&rarr;G 5 | hypervariable | 71 | 1.4% | 0-8% | 4,245 | 97.2% | 97-98% | 95.8% |  |
| reverse | 19 | 2 | `C` | C&rarr;A 36, C&rarr;T 14, C&rarr;G 8 | hypervariable | 58 | 3.4% | 1-12% | 4,258 | 96.9% | 96-97% | 93.4% |  |
| forward | 6 | 13 | `C` | C&rarr;T 19, C&rarr;G 8, C&rarr;A 5 | hypervariable | 32 | 3.1% | 1-16% | 4,284 | 96.3% | 96-97% | 93.2% |  |
| reverse | 20 | 1 | `C` | C&rarr;T 20, C&rarr;A 2 | `H` | 22 | 4.5% | 1-22% | 4,294 | 96.1% | 95-97% | 91.5% |  |
| forward | 11 | 8 | `R` | R&rarr;T 32, R&rarr;C 7 | hypervariable | 39 | 5.1% | 1-17% | 4,277 | 96.4% | 96-97% | 91.3% |  |
| reverse | 4 | 17 | `C` | C&rarr;T 33, C&rarr;G 2, C&rarr;A 1 | `B` (97.2%) | 36 | 5.6% | 2-18% | 4,280 | 96.4% | 96-97% | 90.8% | yes |
| forward | 13 | 6 | `C` | C&rarr;G 34, C&rarr;A 32, C&rarr;T 16 | hypervariable | 82 | 8.5% | 4-17% | 4,234 | 97.3% | 97-98% | 88.7% |  |
| forward | 12 | 7 | `A` | A&rarr;C 59, A&rarr;G 14, A&rarr;T 13 | hypervariable | 86 | 9.3% | 5-17% | 4,230 | 97.4% | 97-98% | 88.0% |  |
| forward | 4 | 15 | `G` | G&rarr;A 55, G&rarr;C 36, G&rarr;T 34 | hypervariable | 125 | 11.2% | 7-18% | 4,191 | 98.1% | 98-98% | 86.9% | yes |
| forward | 10 | 9 | `A` | A&rarr;T 23, A&rarr;G 15, A&rarr;C 4 | hypervariable | 42 | 16.7% | 8-31% | 4,274 | 96.4% | 96-97% | 79.7% |  |
| forward | 8 | 11 | `W` | W&rarr;C 28, W&rarr;G 27 | hypervariable | 55 | 80.0% | 68-88% | 4,261 | 95.8% | 95-96% | 15.8% |  |
| forward | 18 | 1 | `G` | G&rarr;C 1,565, G&rarr;T 34, G&rarr;A 9 | `S` (97.3%) | 1,608 | 92.7% | 91-94% | 2,708 | 97.3% | 97-98% | 4.7% |  |
| forward | 17 | 2 | `W` | W&rarr;C 208, W&rarr;G 17 | hypervariable | 225 | 94.2% | 90-97% | 4,091 | 95.7% | 95-96% | 1.5% |  |
| forward | 5 | 14 | `H` | H&rarr;G 141 | hypervariable | 141 | 94.3% | 89-97% | 4,175 | 95.6% | 95-96% | 1.3% | yes |
| reverse | 15 | 6 | `T` | T&rarr;A 616, T&rarr;G 304, T&rarr;C 135, +1 more | hypervariable | 1,056 | 97.0% | 96-98% | 3,260 | 95.2% | 94-96% | -1.8% |  |
| reverse | 3 | 18 | `W` | W&rarr;G 248, W&rarr;C 44 | hypervariable | 292 | 97.6% | 95-99% | 4,024 | 95.5% | 95-96% | -2.2% | yes |
| reverse | 12 | 9 | `D` | D&rarr;C 430 | hypervariable | 430 | 97.9% | 96-99% | 3,886 | 95.3% | 95-96% | -2.6% |  |
| reverse | 6 | 15 | `H` | H&rarr;G 64 | hypervariable | 64 | 98.4% | 92-100% | 4,252 | 95.6% | 95-96% | -2.9% |  |
| forward | 14 | 5 | `V` | V&rarr;T 1,209 | hypervariable | 1,209 | 98.8% | 98-99% | 3,107 | 94.4% | 94-95% | -4.4% |  |
| reverse | 18 | 3 | `W` | W&rarr;G 246, W&rarr;C 116 | hypervariable | 362 | 99.7% | 98-100% | 3,954 | 95.2% | 95-96% | -4.5% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 18 | 1,341 | detect | 2023×112, 2024×74, 2025×91, 2026×39 | Orthohantavirus hantanense×293, Orthohantavirus seoulense×208, Hantaan virus×143 | `PX241526`, `PX241525`, `PW070294`, `PZ024107`, `PZ024106`, `PZ024105` (+1,335) |
| no mismatches | 580 | detect | 2023×35, 2024×57, 2025×50, 2026×43 | Orthohantavirus tulaense×105, Juquitiba virus×75, Orthohantavirus puumalaense×63 | `PX069883`, `PX069880`, `PX069875`, `PX069874`, `PX069873`, `PX069871` (+574) |
| fwd 14 | 323 | detect | 2023×10, 2024×16, 2025×13, 2026×3 | Orthohantavirus puumalaense×72, Orthohantavirus chocloense×55, Puumala virus×35 | `PV544289`, `PV544288`, `PV544287`, `PV544286`, `PX445895`, `PP239363` (+317) |
| rev 15 | 309 | detect | 2023×28, 2024×12, 2025×15, 2026×33 | Orthohantavirus andesense×86, Orthohantavirus puumalaense×79, Puumala virus×51 | `PX069882`, `PX069881`, `PX069879`, `PX069877`, `PX069876`, `PX069872` (+303) |
| fwd 14; rev 15 | 247 | detect | 2019×23, 2020×4, 2021×116, 2024×6 | Orthohantavirus puumalaense×186, Puumala virus×38, Orthohantavirus sinnombreense×7 | `OQ999163`, `OQ999146`, `OQ999138`, `OQ999116`, `OQ999113`, `OQ999108` (+241) |
| fwd 14; rev 12,15 | 170 | reduced | 2019×23, 2020×9, 2021×42, 2023×7 | Orthohantavirus puumalaense×137, Puumala virus×33 | `OQ283013`, `OQ283012`, `OQ283011`, `OQ283010`, `OQ283009`, `OQ283008` (+164) |
| fwd 14; rev 18 | 152 | detect | 2023×8, 2024×31, 2025×1, 2026×1 | Orthohantavirus puumalaense×105, Puumala orthohantavirus×40, Puumala virus×7 | `PX026263`, `PQ660168`, `OQ606921`, `OQ606918`, `OR999070`, `OR974366` (+146) |
| fwd 14; rev 3,15 | 141 | reduced | 2016×1, 2017×3, 2020×4, 2021×124 | Orthohantavirus puumalaense×132, Puumala virus×9 | `MT453710`, `MT453677`, `MT453676`, `MT453675`, `MT453674`, `MT453673` (+135) |

## CDV_H_gene_Mueller_2011_2

Morbillivirus canis (formerly Canine morbillivirus) (taxid 3052342) — status **watch** — 1,959 evaluable of 4,013 screened records

- forward: `5'-GCGATACAATTGGGATCAGA-3'` (20 nt)
- reverse: `5'-TGGGTGAGCAACAGGTATCA-3'` (20 nt)

**342 of 1,959 evaluable records (17%) share one mismatch pattern, mostly Canine distemper, deposited 2003-2026, and the group's dominant call is `reduced`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 1 | 20 | `A` | A&rarr;G 76, A&rarr;T 1 | `R` (98.7%) | 77 | 0.0% | 0-5% | 1,882 | 93.7% | 93-95% | 93.7% | yes |
| forward | 4 | 17 | `C` | C&rarr;A 14, C&rarr;T 12 | `H` | 26 | 0.0% | 0-13% | 1,933 | 91.3% | 90-92% | 91.3% | yes |
| reverse | 10 | 11 | `A` | A&rarr;G 38 | `R` | 38 | 2.6% | 0-13% | 1,921 | 91.8% | 90-93% | 89.1% |  |
| forward | 8 | 13 | `G` | G&rarr;A 31 | `R` | 31 | 58.1% | 41-74% | 1,928 | 90.6% | 89-92% | 32.5% |  |
| reverse | 3 | 18 | `T` | T&rarr;C 15, T&rarr;A 4, T&rarr;G 1 | `H` (95.0%) | 20 | 60.0% | 39-78% | 1,939 | 90.4% | 89-92% | 30.4% | yes |
| reverse | 14 | 7 | `A` | A&rarr;G 12, A&rarr;T 8, A&rarr;C 1 | `D` (95.2%) | 21 | 66.7% | 45-83% | 1,938 | 90.3% | 89-92% | 23.6% |  |
| reverse | 12 | 9 | `C` | C&rarr;A 13, C&rarr;T 7, C&rarr;G 1 | `H` (95.2%) | 21 | 76.2% | 55-89% | 1,938 | 90.2% | 89-91% | 14.0% |  |
| forward | 2 | 19 | `G` | G&rarr;A 659, G&rarr;T 2, G&rarr;C 1 | `R` (99.5%) | 662 | 81.3% | 78-84% | 1,297 | 94.5% | 93-96% | 13.3% | yes |
| reverse | 9 | 12 | `C` | C&rarr;T 516, C&rarr;A 3, C&rarr;G 1 | `Y` (99.2%) | 520 | 80.8% | 77-84% | 1,439 | 93.4% | 92-95% | 12.6% |  |
| forward | 12 | 9 | `A` | A&rarr;G 555, A&rarr;C 2 | `R` (99.6%) | 557 | 81.1% | 78-84% | 1,402 | 93.6% | 92-95% | 12.4% |  |
| forward | 6 | 15 | `A` | A&rarr;G 590, A&rarr;C 33 | `V` | 623 | 82.7% | 79-85% | 1,336 | 93.5% | 92-95% | 10.8% |  |
| forward | 19 | 2 | `C` | C&rarr;T 711 | `Y` | 711 | 84.5% | 82-87% | 1,248 | 93.2% | 92-94% | 8.7% |  |
| forward | 10 | 11 | `T` | T&rarr;C 51, T&rarr;G 2 | `Y` (96.2%) | 53 | 84.9% | 73-92% | 1,906 | 90.2% | 89-91% | 5.3% |  |
| forward | 13 | 8 | `A` | A&rarr;T 39, A&rarr;G 10, A&rarr;C 5 | hypervariable | 54 | 87.0% | 76-94% | 1,905 | 90.1% | 89-91% | 3.1% |  |
| reverse | 17 | 4 | `G` | G&rarr;A 233, G&rarr;T 10 | `R` (95.9%) | 243 | 91.8% | 88-95% | 1,716 | 89.8% | 88-91% | -2.0% |  |
| forward | 15 | 6 | `A` | A&rarr;T 81, A&rarr;G 53, A&rarr;C 2 | `D` (98.5%) | 136 | 91.9% | 86-95% | 1,823 | 89.9% | 88-91% | -2.0% |  |
| reverse | 20 | 1 | `T` | T&rarr;C 60, T&rarr;G 9, T&rarr;A 8 | hypervariable | 77 | 92.2% | 84-96% | 1,882 | 90.0% | 89-91% | -2.3% |  |
| reverse | 2 | 19 | `C` | C&rarr;G 130, C&rarr;T 18, C&rarr;A 6 | `B` (96.1%) | 154 | 92.2% | 87-95% | 1,805 | 89.9% | 88-91% | -2.3% | yes |
| reverse | 8 | 13 | `A` | A&rarr;G 40, A&rarr;C 2 | `R` (95.2%) | 42 | 92.9% | 81-98% | 1,917 | 90.0% | 89-91% | -2.9% |  |
| forward | 14 | 7 | `C` | C&rarr;T 48, C&rarr;A 1 | `Y` (98.0%) | 49 | 95.9% | 86-99% | 1,910 | 89.9% | 88-91% | -6.0% |  |
| reverse | 18 | 3 | `G` | G&rarr;A 35, G&rarr;C 1 | `R` (97.2%) | 36 | 97.2% | 86-100% | 1,923 | 89.9% | 88-91% | -7.3% |  |
| reverse | 4 | 17 | `A*` | G&rarr;A 1,632, G&rarr;C 2, A&rarr;T 2 | - | 1,636 | 91.9% | 90-93% | 323 | 80.8% | 76-85% | -11.1% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| fwd 2,6,12,19; rev 4,9 | 342 | reduced | 2023×3, 2024×39, 2025×8, 2026×29 | Canine distemper×228, Morbillivirus canis×99, Canine morbillivirus×15 | `PZ171056`, `PZ845994`, `PZ845993`, `PZ845992`, `PZ845991`, `PZ845990` (+336) |
| rev 4 | 234 | detect | 2023×10, 2024×8, 2025×6, 2026×6 | Canine distemper×107, Morbillivirus canis×63, Canine morbillivirus×57 | `PZ766579`, `PX610320`, `PX610319`, `PX656912`, `PX656911`, `PX656910` (+228) |
| no mismatches | 194 | detect | 2021×3, 2022×4, 2025×1, 2026×38 | Morbillivirus canis×100, Canine distemper×63, Sequence×14 | `PZ812018`, `PZ812017`, `PZ812016`, `PZ812015`, `PZ812014`, `PZ812013` (+188) |
| rev 2,4 | 138 | reduced | 2011×5, 2021×129, 2022×4 | Morbillivirus canis×127, Canine morbillivirus×6, Canine distemper×5 | `MW828751`, `MW828750`, `MW828749`, `MW828748`, `OK667044`, `OK667043` (+132) |
| fwd 19; rev 4 | 109 | detect | 2023×1, 2024×1, 2025×2, 2026×18 | Canine distemper×72, Morbillivirus canis×26, Canine morbillivirus×7 | `PX445144`, `PX938971`, `PX938970`, `PX734755`, `PX734753`, `PX734752` (+103) |
| rev 4,17 | 94 | detect | 2021×7, 2022×2, 2023×43, 2024×1 | Morbillivirus canis×85, Canine morbillivirus×6, Canine distemper×3 | `PP683092`, `OR733215`, `OR733214`, `OR515853`, `OR515852`, `OR515851` (+88) |
| fwd 15; rev 4 | 70 | detect | 2022×8, 2023×10, 2024×3, 2025×1 | Canine distemper×26, Canine morbillivirus×18, Morbillivirus canis×15 | `OR120159`, `PQ625782`, `PQ241502`, `PQ241501`, `AB472691`, `AB472690` (+64) |
| fwd 2,14; rev 4 | 39 | detect | 2020×2, 2023×7, 2024×1, 2025×8 | Morbillivirus canis×39 | `OR880602`, `OR880601`, `OR880600`, `OR880599`, `OR880598`, `PV712681` (+33) |

## RANAVIRUS_dsDNA_variable_intergenic_regi_Pallister_2007

Ranavirus (taxid 10492) — status **watch** — 250 evaluable of 1,466 screened records

- forward: `5'-AGAAATCTTGCGAGACCG-3'` (18 nt)
- reverse: `5'-AACTGTTGGTGATTGCAGC-3'` (19 nt)

**140 of 250 evaluable records (56%) share one mismatch pattern, mostly Santee-Cooper ranavirus, deposited 1994-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 2 | 17 | `C` | C&rarr;G 17, C&rarr;A 4, C&rarr;T 1 | `V` (95.5%) | 22 | 0.0% | 0-15% | 228 | 99.1% | 97-100% | 99.1% | yes |
| reverse | 18 | 2 | `A` | A&rarr;G 17, A&rarr;C 3 | `V` | 20 | 15.0% | 5-36% | 230 | 97.0% | 94-99% | 82.0% |  |
| forward | 1 | 18 | `G` | G&rarr;A 21, G&rarr;C 1 | `R` (95.5%) | 22 | 18.2% | 7-39% | 228 | 97.4% | 94-99% | 79.2% | yes |
| reverse | 17 | 3 | `C` | C&rarr;A 156 | `M` | 156 | 98.7% | 95-100% | 94 | 76.6% | 67-84% | -22.1% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 17 | 140 | detect | 2023×2, 2024×9, 2025×48, 2026×6 | Santee-Cooper ranavirus×47, Frog virus×39, Common midwife×16 | `PZ441287`, `PX692941`, `PX692939`, `PX692938`, `PX692937`, `PX562879` (+134) |
| no mismatches | 63 | detect | 2015×16, 2016×5, 2019×1, 2020×15 | Ambystoma tigrinum×33, Epizootic haematopoietic×18, European sheatfish×3 | `NC_030842`, `NC_028461`, `NC_005832`, `NC_017940`, `MT510743`, `MT510742` (+57) |
| fwd 1,2,6; rev 4,6,8,10,18,19 | 17 | fail | 2023×3, 2024×1, 2025×5, 2026×3 | Largemouth bass×9, Mandarin fish×3, Siniperca chuatsi×2 | `PZ233446`, `PX883867`, `PX879566`, `PV833272`, `PX463212`, `PV191281` (+11) |
| fwd 8; rev 17 | 6 | reduced | 2017×1, 2025×5 | Santee-Cooper ranavirus×5, Rana esculenta×1 | `OQ718185`, `OQ718184`, `OQ718168`, `OQ718167`, `OQ718165`, `MF538628` |
| fwd 12 | 6 | detect | 2019×6 | Ranavirus ambystoma1×6 | `MK580533`, `MK580532`, `MK580531`, `MK580535`, `MK580536`, `MK580534` |
| fwd 1; rev 17 | 4 | detect | 2020×1, 2025×3 | Santee-Cooper ranavirus×3, Tiger frog×1 | `OQ718217`, `OQ718216`, `OQ718204`, `MT512502` |
| rev 18 | 3 | detect | 2019×2, 2023×1 | Lumpfish ranavirus×3 | `NC_075538`, `MH665360`, `MH665358` |
| fwd 5; rev 17 | 2 | reduced | 2018×1, 2026×1 | Frog virus×1, Rana nigromaculata×1 | `PX692940`, `MG791866` |

## RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Johnson_2008

Ranavirus (taxid 10492) — status **watch** — 326 evaluable of 1,466 screened records

- forward: `5'-GACTTGGCCACTTATGAC-3'` (18 nt)
- reverse: `5'-GTCTCTGGAGAAGAAGAA-3'` (18 nt)

**39 of 326 evaluable records (12%) share one mismatch pattern, mostly Largemouth bass, deposited 2011-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 6 | 13 | `G` | G&rarr;A 55, G&rarr;C 1 | `R` (98.2%) | 56 | 0.0% | 0-6% | 270 | 98.9% | 97-100% | 98.9% |  |
| reverse | 10 | 9 | `A` | A&rarr;C 40, A&rarr;T 16 | `H` | 56 | 0.0% | 0-6% | 270 | 98.9% | 97-100% | 98.9% |  |
| forward | 16 | 3 | `C` | C&rarr;T 55, C&rarr;A 3 | `H` | 58 | 1.7% | 0-9% | 268 | 99.3% | 97-100% | 97.5% |  |
| reverse | 11 | 8 | `G` | G&rarr;C 55, G&rarr;A 1 | `S` (98.2%) | 56 | 1.8% | 0-9% | 270 | 98.5% | 96-99% | 96.7% |  |
| forward | 13 | 6 | `G` | G&rarr;C 39, G&rarr;T 2 | `S` (95.1%) | 41 | 0.0% | 0-9% | 285 | 93.7% | 90-96% | 93.7% |  |
| forward | 15 | 4 | `T` | T&rarr;C 39, T&rarr;G 3 | `B` | 42 | 2.4% | 0-12% | 284 | 93.7% | 90-96% | 91.3% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 265 | detect | 2023×4, 2024×9, 2025×57, 2026×10 | Santee-Cooper ranavirus×55, Frog virus×44, Epizootic haematopoietic×18 | `PZ441287`, `PV776865`, `PX692941`, `PX692940`, `PX692939`, `PX692938` (+259) |
| fwd 13,15,16; rev 6,10,11 | 39 | fail | 2023×6, 2024×2, 2025×5, 2026×3 | Largemouth bass×19, Santee-Cooper ranavirus×4, Smallmouth bass×4 | `PZ233446`, `PX883867`, `PX879566`, `PV833272`, `PX463212`, `PV191281` (+33) |
| fwd 4,7,16; rev 6,10,11 | 11 | fail | 2016×5, 2017×1, 2019×1, 2024×1 | Grouper iridovirus×8, Singapore grouper×3 | `PP085414`, `NC_006549`, `MK107821`, `KX284838`, `KX228768`, `KX228767` (+5) |
| fwd 7,10,16; rev 6,10,11 | 4 | fail | 2011×4 | Grouper iridovirus×3, Largemouth bass×1 | `JF264365`, `JF264364`, `JF264361`, `JF264358` |
| fwd 5,14,15,16,17,18 | 2 | fail | 2019×2 | Frog virus×2 | `MK959620`, `MK959619` |
| rev 11 | 1 | detect | 2026×1 | Lithobates grylio×1 | `PZ195142` |
| fwd 4,7,16; rev 6,8,10,11 | 1 | fail | 2022×1 | Singapore grouper×1 | `OM793601` |
| fwd 14,15,16,17,18 | 1 | reduced | 2019×1 | Frog virus×1 | `MK959615` |

## MONKEYPOX_dsDNA_F3L_MGB_Kulesh_2004

Monkeypox virus (taxid 10244) — status **watch** — 12,658 evaluable of 13,757 screened records

- forward: `5'-CTCATTGATTTTTCGCGGGATA-3'` (22 nt)
- reverse: `5'-GACGATACTCCTCCTCGTTGGT-3'` (22 nt)
- probe: `5'-CATCAGAATCTGTAGGCCGT-3'` (20 nt)

**9,935 of 12,658 evaluable records (78%) share one mismatch pattern, mostly Monkeypox virus, deposited 2004-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 7 | 16 | `C` | C&rarr;T 132, C&rarr;A 1 | `Y` (99.2%) | 133 | 100.0% | 97-100% | 12,525 | 99.9% | 100-100% | -0.1% |  |
| reverse | 22 | 1 | `G` | G&rarr;A 10,072 | `R` | 10,072 | 100.0% | 100-100% | 2,586 | 99.5% | 99-100% | -0.5% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 22 | 9,935 | detect | 2023×3121, 2024×1506, 2025×1083, 2026×736 | Monkeypox virus×9932, Mutant×2, Patent application×1 | `OZ561975`, `OZ561965`, `OZ561964`, `OZ561963`, `OZ561962`, `OZ561960` (+9,929) |
| no mismatches | 2,584 | detect | 2023×3, 2024×533, 2025×697, 2026×1303 | Monkeypox virus×2584 | `OZ555904`, `OZ555901`, `OZ555900`, `OZ555899`, `OZ540336`, `OZ540332` (+2,578) |
| rev 7,22 | 132 | reduced | 2023×1, 2024×23, 2025×55, 2026×53 | Monkeypox virus×132 | `PZ760199`, `PZ760198`, `OZ501928`, `OZ501846`, `OZ501915`, `OZ501910` (+126) |
| fwd 7,9,20,22; rev 2,3,6,19,22; prb 3,4,11,17,20 | 2 | fail | 2010×2 | Modified×2 | `FV537350`, `FV537349` |
| rev 22; prb 15 | 1 | reduced | 2025×1 | Monkeypox virus×1 | `OZ330175` |
| fwd 16; rev 22 | 1 | detect | 2024×1 | Monkeypox virus×1 | `PQ218891` |
| fwd 8; rev 22 | 1 | reduced | 2022×1 | Monkeypox virus×1 | `OP415222` |
| rev 7 | 1 | detect | 2015×1 | Monkeypox virus×1 | `KJ642618` |

## RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007

Ranavirus (taxid 10492) — status **watch** — 351 evaluable of 1,466 screened records

- forward: `5'-CTCATCGTTCTGGCCATCAA-3'` (20 nt)
- reverse: `5'-TCCCATCGAGCCGTTCA-3'` (17 nt)
- probe: `5'-CACAACATTATCCGCATC-3'` (18 nt)

**36 of 351 evaluable records (10%) share one mismatch pattern, mostly Largemouth bass, deposited 2011-2026, and the group's dominant call is `fail`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 11 | 10 | `C` | C&rarr;A 37 | `M` | 37 | 0.0% | 0-9% | 314 | 100.0% | 99-100% | 100.0% |  |
| forward | 18 | 3 | `C` | C&rarr;G 37 | `S` | 37 | 0.0% | 0-9% | 314 | 100.0% | 99-100% | 100.0% |  |
| reverse | 17 | 1 | `T` | T&rarr;A 37, T&rarr;G 1 | `W` (97.4%) | 38 | 2.6% | 0-13% | 313 | 100.0% | 99-100% | 97.4% |  |
| forward | 15 | 6 | `C` | C&rarr;G 37, C&rarr;T 2 | `B` | 39 | 5.1% | 1-17% | 312 | 100.0% | 99-100% | 94.9% |  |
| reverse | 11 | 7 | `C` | C&rarr;G 37, C&rarr;T 2 | `B` | 39 | 5.1% | 1-17% | 312 | 100.0% | 99-100% | 94.9% |  |
| forward | 12 | 9 | `T` | T&rarr;C 40 | `Y` | 40 | 7.5% | 3-20% | 311 | 100.0% | 99-100% | 92.5% |  |
| reverse | 8 | 10 | `G` | G&rarr;A 60 | `R` | 60 | 38.3% | 27-51% | 291 | 100.0% | 99-100% | 61.7% |  |
| forward | 17 | 4 | `A` | A&rarr;G 67 | `R` | 67 | 44.8% | 33-57% | 284 | 100.0% | 99-100% | 55.2% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 257 | detect | 2023×2, 2024×9, 2025×54, 2026×12 | Frog virus×55, Santee-Cooper ranavirus×52, Epizootic haematopoietic×19 | `PZ441287`, `PV776865`, `PX692941`, `PX692939`, `PX692938`, `PX692937` (+251) |
| fwd 11,12,15,17,18; rev 8,11,17 | 36 | fail | 2023×5, 2024×2, 2025×4, 2026×3 | Largemouth bass×17, Santee-Cooper ranavirus×4, Smallmouth bass×4 | `PZ233446`, `PX883867`, `PX879566`, `PV833272`, `PV191281`, `PV459226` (+30) |
| fwd 17; rev 8 | 16 | reduced | 2018×12, 2019×3, 2023×1 | Ranavirus sp.×12, Lumpfish ranavirus×4 | `NC_075538`, `MH665360`, `MH665359`, `MH665358`, `MF678523`, `MF678522` (+10) |
| fwd 17 | 14 | detect | 2010×1, 2013×9, 2016×1, 2026×1 | Rana catesbeiana×10, Pike-perch iridovirus×2, Frog virus×1 | `PX692940`, `KX574341`, `KC756964`, `KC756963`, `KC756962`, `KC756961` (+8) |
| fwd 9 | 11 | detect | 2015×2, 2018×1, 2019×6, 2025×1 | Ranavirus ambystoma1×6, Zoo ranavirus×2, Frog virus×1 | `PQ844486`, `MK580533`, `MK580532`, `MK580531`, `MK580535`, `MK580536` (+5) |
| rev 8 | 4 | detect | 2009×2, 2017×2 | Common midwife×1, Pelophylax esculentus×1, Rana esculenta×1 | `MF125270`, `MF538627`, `FJ515796`, `AB474588` |
| fwd 12; rev 8 | 3 | reduced | 2009×1, 2016×2 | Short-finned eel×3 | `KX353311`, `NC_030394`, `FJ358612` |
| fwd 15 | 2 | detect | 2021×1, 2025×1 | Santee-Cooper ranavirus×1, Tiger frog×1 | `OQ718208`, `MW727505` |

## ADENOVIRUS_dsDNA_Polymerase_Primate_speci_Casas_2005

Mastadenovirus (taxid 10509) — status **low coverage** — 4,179 evaluable of 30,214 screened records

- forward: `5'-TGATGCGYTTCTTACCTYTGGTYTCCATGAG-3'` (31 nt)
- reverse: `5'-AGTTYTACATGCTGGGCTCTTACCG-3'` (25 nt)

**1,303 of 4,179 evaluable records (31%) share one mismatch pattern, mostly Human adenovirus, deposited 1985-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 6 | 20 | `T` | T&rarr;C 294, T&rarr;G 1 | `Y` (99.7%) | 295 | 0.0% | 0-1% | 3,884 | 91.2% | 90-92% | 91.2% |  |
| forward | 10 | 22 | `T` | T&rarr;A 208, T&rarr;C 11, T&rarr;G 4 | `H` (98.2%) | 223 | 0.0% | 0-2% | 3,956 | 89.6% | 89-90% | 89.6% |  |
| reverse | 1 | 25 | `G` | G&rarr;T 34, G&rarr;A 32, G&rarr;C 1 | `D` (98.5%) | 67 | 4.5% | 2-12% | 4,112 | 86.1% | 85-87% | 81.6% | yes |
| reverse | 18 | 8 | `C` | C&rarr;T 46 | `Y` | 46 | 6.5% | 2-18% | 4,133 | 85.7% | 85-87% | 79.2% |  |
| forward | 25 | 7 | `G` | G&rarr;T 26 | `K` | 26 | 11.5% | 4-29% | 4,153 | 85.3% | 84-86% | 73.7% |  |
| forward | 24 | 8 | `Y` | Y&rarr;A 33, Y&rarr;G 32 | hypervariable | 65 | 13.8% | 7-24% | 4,114 | 85.9% | 85-87% | 72.1% |  |
| forward | 22 | 10 | `T` | T&rarr;G 58, T&rarr;C 4, T&rarr;A 2 | `B` (96.9%) | 64 | 14.1% | 8-25% | 4,115 | 85.9% | 85-87% | 71.8% |  |
| forward | 3 | 29 | `G` | G&rarr;A 265, G&rarr;C 7, G&rarr;T 5 | `R` (95.7%) | 277 | 20.6% | 16-26% | 3,902 | 89.4% | 88-90% | 68.8% | yes |
| forward | 27 | 5 | `G` | G&rarr;T 28, G&rarr;C 22, G&rarr;A 4 | hypervariable | 54 | 27.8% | 18-41% | 4,125 | 85.6% | 84-87% | 57.8% |  |
| forward | 21 | 11 | `C` | C&rarr;T 15, C&rarr;G 6 | `B` | 21 | 28.6% | 14-50% | 4,158 | 85.1% | 84-86% | 56.5% |  |
| reverse | 24 | 2 | `G` | G&rarr;A 669, G&rarr;T 350, G&rarr;C 13 | `D` (98.7%) | 1,032 | 44.2% | 41-47% | 3,147 | 98.1% | 98-99% | 53.9% |  |
| reverse | 9 | 17 | `C` | C&rarr;T 728, C&rarr;A 327, C&rarr;G 9 | `H` (99.2%) | 1,064 | 45.3% | 42-48% | 3,115 | 98.3% | 98-99% | 53.0% |  |
| forward | 30 | 2 | `G` | G&rarr;A 17, G&rarr;T 4, G&rarr;C 3 | hypervariable | 24 | 37.5% | 21-57% | 4,155 | 85.1% | 84-86% | 47.6% |  |
| forward | 28 | 4 | `T` | T&rarr;G 32, T&rarr;C 12, T&rarr;A 3 | hypervariable | 47 | 38.3% | 26-53% | 4,132 | 85.3% | 84-86% | 47.0% |  |
| forward | 13 | 19 | `T` | T&rarr;G 1,210, T&rarr;C 2, T&rarr;A 1 | `K` (99.8%) | 1,213 | 52.1% | 49-55% | 2,966 | 98.2% | 98-99% | 46.1% |  |
| reverse | 8 | 18 | `T` | T&rarr;G 36, T&rarr;A 27 | `D` | 63 | 52.4% | 40-64% | 4,116 | 85.3% | 84-86% | 32.9% |  |
| forward | 12 | 20 | `G` | G&rarr;C 630, G&rarr;T 108, G&rarr;A 12 | `B` (98.4%) | 750 | 60.9% | 57-64% | 3,429 | 90.0% | 89-91% | 29.1% |  |
| forward | 20 | 12 | `T` | T&rarr;C 33 | `Y` | 33 | 63.6% | 47-78% | 4,146 | 85.0% | 84-86% | 21.3% |  |
| forward | 11 | 21 | `G` | G&rarr;C 48, G&rarr;T 11 | `B` | 59 | 71.2% | 59-81% | 4,120 | 85.0% | 84-86% | 13.8% |  |
| reverse | 14 | 12 | `C` | C&rarr;T 1,758, C&rarr;G 66, C&rarr;A 8 | `Y` (96.0%) | 1,832 | 78.9% | 77-81% | 2,347 | 89.4% | 88-91% | 10.6% |  |
| reverse | 12 | 14 | `G` | G&rarr;A 1,666, G&rarr;T 227, G&rarr;C 5 | `D` (99.7%) | 1,898 | 83.8% | 82-85% | 2,281 | 85.7% | 84-87% | 1.9% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 14 | 1,303 | detect | 2023×104, 2024×120, 2025×149, 2026×411 | Human adenovirus×1035, Human mastadenovirus×166, Sequence×28 | `PZ576384`, `PZ576383`, `PZ576382`, `PZ576381`, `PZ576380`, `PZ576379` (+1,297) |
| rev 12 | 1,148 | detect | 2023×249, 2024×72, 2025×86, 2026×168 | Human adenovirus×598, Human mastadenovirus×326, KR×70 | `PW424729`, `PW424730`, `QV000696`, `PZ726819`, `PZ726818`, `PZ411237` (+1,142) |
| fwd 12,13; rev 24 | 339 | reduced | 2023×34, 2024×3, 2025×3, 2026×2 | Human adenovirus×248, Human mastadenovirus×78, Sequence×7 | `PV780771`, `PX951443`, `PX121480`, `FJ169625`, `PV359444`, `PQ738617` (+333) |
| rev 9,12 | 302 | reduced | 2023×20, 2024×22, 2025×72, 2026×5 | Human adenovirus×234, Human mastadenovirus×32, Sequence×11 | `LC945760`, `PX461456`, `PX461455`, `PX491610`, `PX146757`, `PV980178` (+296) |
| fwd 13; rev 6,9,14,24 | 261 | fail | 2023×35, 2024×21, 2025×23, 2026×23 | Human adenovirus×171, Human mastadenovirus×86, Mastadenovirus×2 | `PZ683035`, `PZ683031`, `PZ411221`, `PZ411189`, `PZ410871`, `PZ360999` (+255) |
| fwd 3,10,12,13; rev 9,12,24 | 176 | fail | 2022×99, 2023×25, 2024×1, 2026×3 | Human adenovirus×134, Human mastadenovirus×40, Mastadenovirus sp.×2 | `PZ023991`, `PX951442`, `PX905700`, `OQ744647`, `LC791110`, `OQ518334` (+170) |
| fwd 13; rev 9,14,24 | 77 | reduced | 2022×23, 2023×6, 2024×12, 2025×26 | Human adenovirus×53, Human mastadenovirus×24 | `PX485693`, `PX453680`, `PX453679`, `PX453678`, `PX453677`, `PX453676` (+71) |
| fwd 12,13; rev 9 | 57 | reduced | 2020×3, 2022×31, 2025×13, 2026×2 | Human adenovirus×42, Human mastadenovirus×12, Mastadenovirus×2 | `PZ683033`, `PZ683032`, `L19443`, `PX485688`, `PX485687`, `PX485686` (+51) |

## Morbillivirus_including_CDV_P_gene

Morbillivirus (taxid 11229) — status **low coverage** — 4,934 evaluable of 37,519 screened records

- forward: `5'-ATGTTTATGATCACAGCGGT-3'` (20 nt)
- reverse: `5'-ATTGGGTTGCACCACTTGTC-3'` (20 nt)

**3,783 of 4,934 evaluable records (77%) share one mismatch pattern, mostly Measles virus, deposited 1988-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 9 | 12 | `C` | C&rarr;G 222, C&rarr;A 45 | `V` | 267 | 0.0% | 0-1% | 4,667 | 99.2% | 99-99% | 99.2% |  |
| forward | 17 | 4 | `T` | T&rarr;G 257, T&rarr;A 7, T&rarr;C 1 | `K` (97.0%) | 265 | 0.4% | 0-2% | 4,669 | 99.1% | 99-99% | 98.7% |  |
| forward | 16 | 5 | `T` | T&rarr;A 263, T&rarr;C 1 | `W` (99.6%) | 264 | 0.4% | 0-2% | 4,670 | 99.1% | 99-99% | 98.7% |  |
| forward | 10 | 11 | `T` | T&rarr;C 266, T&rarr;A 6 | `Y` (97.8%) | 272 | 1.1% | 0-3% | 4,662 | 99.2% | 99-99% | 98.1% |  |
| reverse | 3 | 18 | `G` | G&rarr;A 272, G&rarr;T 1 | `R` (99.6%) | 273 | 2.6% | 1-5% | 4,661 | 99.1% | 99-99% | 96.6% | yes |
| forward | 12 | 9 | `G` | G&rarr;A 19, G&rarr;T 4 | `D` | 23 | 0.0% | 0-14% | 4,911 | 94.2% | 94-95% | 94.2% |  |
| forward | 14 | 7 | `A` | A&rarr;C 283, A&rarr;T 2, A&rarr;G 2 | `M` (98.6%) | 287 | 6.3% | 4-10% | 4,647 | 99.2% | 99-99% | 92.9% |  |
| forward | 2 | 19 | `G` | G&rarr;A 264, G&rarr;T 24 | `D` | 288 | 8.3% | 6-12% | 4,646 | 99.1% | 99-99% | 90.8% | yes |
| forward | 11 | 10 | `A` | A&rarr;G 18, A&rarr;C 3 | `V` | 21 | 4.8% | 1-23% | 4,913 | 94.2% | 93-95% | 89.4% |  |
| reverse | 20 | 1 | `A` | A&rarr;G 206, A&rarr;C 194, A&rarr;T 71 | hypervariable | 471 | 39.9% | 36-44% | 4,463 | 99.5% | 99-100% | 59.6% |  |
| forward | 15 | 6 | `T` | T&rarr;C 41, T&rarr;G 2 | `Y` (95.3%) | 43 | 62.8% | 48-76% | 4,891 | 94.1% | 93-95% | 31.3% |  |
| reverse | 15 | 6 | `G` | G&rarr;A 36 | `R` | 36 | 77.8% | 62-88% | 4,898 | 93.9% | 93-95% | 16.1% |  |
| forward | 4 | 17 | `C` | C&rarr;T 82, C&rarr;G 7 | `B` | 89 | 79.8% | 70-87% | 4,845 | 94.1% | 93-95% | 14.3% | yes |
| forward | 6 | 15 | `A` | A&rarr;G 71, A&rarr;T 71, A&rarr;C 2 | `D` (98.6%) | 144 | 84.7% | 78-90% | 4,790 | 94.1% | 93-95% | 9.3% |  |
| forward | 19 | 2 | `T` | T&rarr;C 27, T&rarr;G 4 | `B` | 31 | 87.1% | 71-95% | 4,903 | 93.8% | 93-94% | 6.7% |  |
| reverse | 18 | 3 | `T` | T&rarr;C 190, T&rarr;G 16, T&rarr;A 1 | `B` (99.5%) | 207 | 87.9% | 83-92% | 4,727 | 94.1% | 93-95% | 6.1% |  |
| reverse | 6 | 15 | `C` | C&rarr;T 406, C&rarr;A 21 | `Y` (95.1%) | 427 | 89.5% | 86-92% | 4,507 | 94.2% | 93-95% | 4.7% |  |
| reverse | 19 | 2 | `T` | T&rarr;C 50, T&rarr;G 4, T&rarr;A 1 | `B` (98.2%) | 55 | 90.9% | 80-96% | 4,879 | 93.8% | 93-94% | 2.9% |  |
| reverse | 4 | 17 | `T` | T&rarr;G 110 | `K` | 110 | 92.7% | 86-96% | 4,824 | 93.8% | 93-94% | 1.1% | yes |
| reverse | 5 | 16 | `T` | T&rarr;C 4,199, T&rarr;G 2 | `Y` (100.0%) | 4,201 | 99.5% | 99-100% | 733 | 61.0% | 57-64% | -38.5% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 5 | 3,783 | detect | 2023×151, 2024×147, 2025×702, 2026×1874 | Measles virus×3484, Morbillivirus hominis×169, Measles morbillivirus×102 | `QB035549`, `QB035548`, `QB035547`, `QB035546`, `QB035545`, `QB035544` (+3,777) |
| fwd 2,9,10,14,16,17; rev 3,20 | 231 | fail | 2023×2, 2024×33, 2025×32, 2026×33 | Morbillivirus caprinae×122, Peste-des-petits-ruminants virus×78, Peste des×27 | `PX459241`, `PX460962`, `PX460961`, `PX460960`, `PZ706560`, `PX685424` (+225) |
| rev 6 | 201 | detect | 2023×6, 2024×4, 2025×7, 2026×62 | Morbillivirus canis×144, Canine distemper×47, Canine morbillivirus×10 | `PX254110`, `PV167797`, `PZ812018`, `PZ812017`, `PZ812016`, `PZ812015` (+195) |
| rev 4,5 | 100 | reduced | 2016×6, 2020×2, 2022×70, 2023×18 | Measles virus×100 | `ON035992`, `ON035991`, `ON035989`, `ON035988`, `ON035986`, `ON035985` (+94) |
| no mismatches | 73 | detect | 2021×1, 2022×8, 2024×2, 2026×1 | Canine distemper×28, Morbillivirus canis×15, Canine morbillivirus×8 | `PX656921`, `PC304176`, `PC304170`, `AB606409`, `AB212727`, `OL441602` (+67) |
| fwd 4; rev 6 | 69 | reduced | 2023×3, 2024×10, 2025×4, 2026×3 | Morbillivirus canis×38, Canine distemper×27, Canine morbillivirus×4 | `PZ168248`, `PZ043805`, `PZ043803`, `PV778034`, `PV778033`, `PV645846` (+63) |
| fwd 6; rev 6,18 | 60 | reduced | 2019×1, 2021×48, 2022×2, 2026×3 | Phocine morbillivirus×51, Phocine distemper×5, Morbillivirus phocae×3 | `PX610323`, `PX610322`, `PX610321`, `MW642078`, `MW642077`, `OK104991` (+54) |
| rev 5,20 | 49 | detect | 2020×38, 2021×4, 2023×7 | Rinderpest morbillivirus×38, Measles virus×11 | `OP951103`, `OP951102`, `OP951101`, `OP951100`, `OP951099`, `OP951098` (+43) |

## Morbillivirus_including_CDV_P_gene_Barrett_2003

Morbillivirus (taxid 11229) — status **low coverage** — 4,934 evaluable of 37,519 screened records

- forward: `5'-ATGTTTATGATCACAGCGGT-3'` (20 nt)
- reverse: `5'-ATTGGGTTGCACCACTTGTC-3'` (20 nt)

**3,783 of 4,934 evaluable records (77%) share one mismatch pattern, mostly Measles virus, deposited 1988-2026, and the group's dominant call is `detect`.**

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| forward | 9 | 12 | `C` | C&rarr;G 222, C&rarr;A 45 | `V` | 267 | 0.0% | 0-1% | 4,667 | 99.2% | 99-99% | 99.2% |  |
| forward | 17 | 4 | `T` | T&rarr;G 257, T&rarr;A 7, T&rarr;C 1 | `K` (97.0%) | 265 | 0.4% | 0-2% | 4,669 | 99.1% | 99-99% | 98.7% |  |
| forward | 16 | 5 | `T` | T&rarr;A 263, T&rarr;C 1 | `W` (99.6%) | 264 | 0.4% | 0-2% | 4,670 | 99.1% | 99-99% | 98.7% |  |
| forward | 10 | 11 | `T` | T&rarr;C 266, T&rarr;A 6 | `Y` (97.8%) | 272 | 1.1% | 0-3% | 4,662 | 99.2% | 99-99% | 98.1% |  |
| reverse | 3 | 18 | `G` | G&rarr;A 272, G&rarr;T 1 | `R` (99.6%) | 273 | 2.6% | 1-5% | 4,661 | 99.1% | 99-99% | 96.6% | yes |
| forward | 12 | 9 | `G` | G&rarr;A 19, G&rarr;T 4 | `D` | 23 | 0.0% | 0-14% | 4,911 | 94.2% | 94-95% | 94.2% |  |
| forward | 14 | 7 | `A` | A&rarr;C 283, A&rarr;T 2, A&rarr;G 2 | `M` (98.6%) | 287 | 6.3% | 4-10% | 4,647 | 99.2% | 99-99% | 92.9% |  |
| forward | 2 | 19 | `G` | G&rarr;A 264, G&rarr;T 24 | `D` | 288 | 8.3% | 6-12% | 4,646 | 99.1% | 99-99% | 90.8% | yes |
| forward | 11 | 10 | `A` | A&rarr;G 18, A&rarr;C 3 | `V` | 21 | 4.8% | 1-23% | 4,913 | 94.2% | 93-95% | 89.4% |  |
| reverse | 20 | 1 | `A` | A&rarr;G 206, A&rarr;C 194, A&rarr;T 71 | hypervariable | 471 | 39.9% | 36-44% | 4,463 | 99.5% | 99-100% | 59.6% |  |
| forward | 15 | 6 | `T` | T&rarr;C 41, T&rarr;G 2 | `Y` (95.3%) | 43 | 62.8% | 48-76% | 4,891 | 94.1% | 93-95% | 31.3% |  |
| reverse | 15 | 6 | `G` | G&rarr;A 36 | `R` | 36 | 77.8% | 62-88% | 4,898 | 93.9% | 93-95% | 16.1% |  |
| forward | 4 | 17 | `C` | C&rarr;T 82, C&rarr;G 7 | `B` | 89 | 79.8% | 70-87% | 4,845 | 94.1% | 93-95% | 14.3% | yes |
| forward | 6 | 15 | `A` | A&rarr;G 71, A&rarr;T 71, A&rarr;C 2 | `D` (98.6%) | 144 | 84.7% | 78-90% | 4,790 | 94.1% | 93-95% | 9.3% |  |
| forward | 19 | 2 | `T` | T&rarr;C 27, T&rarr;G 4 | `B` | 31 | 87.1% | 71-95% | 4,903 | 93.8% | 93-94% | 6.7% |  |
| reverse | 18 | 3 | `T` | T&rarr;C 190, T&rarr;G 16, T&rarr;A 1 | `B` (99.5%) | 207 | 87.9% | 83-92% | 4,727 | 94.1% | 93-95% | 6.1% |  |
| reverse | 6 | 15 | `C` | C&rarr;T 406, C&rarr;A 21 | `Y` (95.1%) | 427 | 89.5% | 86-92% | 4,507 | 94.2% | 93-95% | 4.7% |  |
| reverse | 19 | 2 | `T` | T&rarr;C 50, T&rarr;G 4, T&rarr;A 1 | `B` (98.2%) | 55 | 90.9% | 80-96% | 4,879 | 93.8% | 93-94% | 2.9% |  |
| reverse | 4 | 17 | `T` | T&rarr;G 110 | `K` | 110 | 92.7% | 86-96% | 4,824 | 93.8% | 93-94% | 1.1% | yes |
| reverse | 5 | 16 | `T` | T&rarr;C 4,199, T&rarr;G 2 | `Y` (100.0%) | 4,201 | 99.5% | 99-100% | 733 | 61.0% | 57-64% | -38.5% | yes |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| rev 5 | 3,783 | detect | 2023×151, 2024×147, 2025×702, 2026×1874 | Measles virus×3484, Morbillivirus hominis×169, Measles morbillivirus×102 | `QB035549`, `QB035548`, `QB035547`, `QB035546`, `QB035545`, `QB035544` (+3,777) |
| fwd 2,9,10,14,16,17; rev 3,20 | 231 | fail | 2023×2, 2024×33, 2025×32, 2026×33 | Morbillivirus caprinae×122, Peste-des-petits-ruminants virus×78, Peste des×27 | `PX459241`, `PX460962`, `PX460961`, `PX460960`, `PZ706560`, `PX685424` (+225) |
| rev 6 | 201 | detect | 2023×6, 2024×4, 2025×7, 2026×62 | Morbillivirus canis×144, Canine distemper×47, Canine morbillivirus×10 | `PX254110`, `PV167797`, `PZ812018`, `PZ812017`, `PZ812016`, `PZ812015` (+195) |
| rev 4,5 | 100 | reduced | 2016×6, 2020×2, 2022×70, 2023×18 | Measles virus×100 | `ON035992`, `ON035991`, `ON035989`, `ON035988`, `ON035986`, `ON035985` (+94) |
| no mismatches | 73 | detect | 2021×1, 2022×8, 2024×2, 2026×1 | Canine distemper×28, Morbillivirus canis×15, Canine morbillivirus×8 | `PX656921`, `PC304176`, `PC304170`, `AB606409`, `AB212727`, `OL441602` (+67) |
| fwd 4; rev 6 | 69 | reduced | 2023×3, 2024×10, 2025×4, 2026×3 | Morbillivirus canis×38, Canine distemper×27, Canine morbillivirus×4 | `PZ168248`, `PZ043805`, `PZ043803`, `PV778034`, `PV778033`, `PV645846` (+63) |
| fwd 6; rev 6,18 | 60 | reduced | 2019×1, 2021×48, 2022×2, 2026×3 | Phocine morbillivirus×51, Phocine distemper×5, Morbillivirus phocae×3 | `PX610323`, `PX610322`, `PX610321`, `MW642078`, `MW642077`, `OK104991` (+54) |
| rev 5,20 | 49 | detect | 2020×38, 2021×4, 2023×7 | Rinderpest morbillivirus×38, Measles virus×11 | `OP951103`, `OP951102`, `OP951101`, `OP951100`, `OP951099`, `OP951098` (+43) |

## ALPHAVIRUSES_Togaviridae_ssRNA_NSP4_gene_round2

Alphavirus (taxid 11019) — status **declining** — 8,680 evaluable of 18,181 screened records

- forward: `5'-GIAAYTGYAAYGTIACICARATG-3'` (23 nt)
- reverse: `5'-GCRAAIARIGCIGCIGCYTYIGGICC-3'` (26 nt)

| oligo | pos(3') | pos(5') | base | records carry | order | n mismatching | detected\|mm | 95% CI | n clean | detected\|clean | 95% CI | gap | 3' zone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reverse | 5 | 22 | `G` | G&rarr;C 108, G&rarr;A 10, G&rarr;T 1 | `V` (99.2%) | 119 | 0.0% | 0-3% | 8,561 | 99.6% | 99-100% | 99.6% | yes |
| forward | 6 | 18 | `C` | C&rarr;G 31, C&rarr;T 10 | `B` | 41 | 0.0% | 0-9% | 8,639 | 98.7% | 98-99% | 98.7% |  |
| reverse | 10 | 17 | `C` | C&rarr;T 35, C&rarr;G 1 | `Y` (97.2%) | 36 | 0.0% | 0-10% | 8,644 | 98.6% | 98-99% | 98.6% |  |
| forward | 17 | 7 | `G` | G&rarr;C 31, G&rarr;A 4 | `V` | 35 | 0.0% | 0-10% | 8,645 | 98.6% | 98-99% | 98.6% |  |
| reverse | 2 | 25 | `C` | C&rarr;G 31, C&rarr;T 4 | `B` | 35 | 0.0% | 0-10% | 8,645 | 98.6% | 98-99% | 98.6% | yes |
| forward | 5 | 19 | `A` | A&rarr;G 31 | `R` | 31 | 0.0% | 0-11% | 8,649 | 98.6% | 98-99% | 98.6% | yes |
| forward | 18 | 6 | `T` | T&rarr;C 31 | `Y` | 31 | 0.0% | 0-11% | 8,649 | 98.6% | 98-99% | 98.6% |  |
| reverse | 19 | 8 | `R` | R&rarr;T 31 | `D` | 31 | 0.0% | 0-11% | 8,649 | 98.6% | 98-99% | 98.6% |  |
| reverse | 24 | 3 | `R` | R&rarr;C 30, R&rarr;T 1 | `V` (96.8%) | 31 | 0.0% | 0-11% | 8,649 | 98.6% | 98-99% | 98.6% |  |
| forward | 20 | 4 | `A` | A&rarr;C 32 | `M` | 32 | 3.1% | 1-16% | 8,648 | 98.6% | 98-99% | 95.5% |  |
| reverse | 4 | 23 | `G` | G&rarr;C 152, G&rarr;A 10 | `V` | 162 | 8.0% | 5-13% | 8,518 | 99.9% | 100-100% | 91.9% | yes |
| forward | 2 | 22 | `T` | T&rarr;C 29, T&rarr;G 5 | `B` | 34 | 14.7% | 6-30% | 8,646 | 98.6% | 98-99% | 83.8% | yes |
| reverse | 22 | 5 | `A` | A&rarr;G 479, A&rarr;C 31 | `V` | 510 | 93.7% | 91-96% | 8,170 | 98.5% | 98-99% | 4.8% |  |
| reverse | 25 | 2 | `C` | C&rarr;A 58, C&rarr;T 5 | `H` | 63 | 93.7% | 85-98% | 8,617 | 98.3% | 98-99% | 4.6% |  |
| reverse | 23 | 4 | `A` | A&rarr;T 101 | `W` | 101 | 100.0% | 96-100% | 8,579 | 98.2% | 98-98% | -1.8% |  |

_Both denominators are shown because a large `gap` can rest on a handful of clean records: when almost every record mismatches at a position, the comparison group is tiny and the interval, not the point estimate, is the honest summary. A position mismatching in nearly all records usually means the assay is being screened against a wider group than it was designed for, rather than that the group recently changed._

**Footprint groups** (records sharing one mismatch pattern)

| pattern | records | dominant call | deposit years | organisms (heuristic) | example accessions |
|---|---|---|---|---|---|
| no mismatches | 7,862 | detect | 2023×1221, 2024×424, 2025×491, 2026×3383 | Alphavirus chikungunya×3026, Chikungunya virus×3010, Eastern equine×516 | `PZ710104`, `PZ710103`, `PZ710102`, `PZ710101`, `PZ710100`, `PZ710099` (+7,856) |
| rev 22 | 475 | detect | 2023×27, 2024×6, 2025×1, 2026×1 | Chikungunya virus×475 | `PX404498`, `PX312164`, `OR488125`, `OR488124`, `OR488123`, `OR488122` (+469) |
| rev 4,5 | 107 | fail | 2020×1, 2022×1, 2024×7, 2026×24 | Mayaro virus×103, Tai×2, JP×1 | `PV591951`, `PV591950`, `PV591949`, `PV591948`, `PV591947`, `PV591946` (+101) |
| rev 23 | 100 | detect | 2019×9, 2021×1, 2023×4, 2025×4 | Venezuelan equine×86, Tonate virus×4, Mucambo virus×4 | `PP972019`, `PQ778495`, `PV600894`, `PQ406672`, `OR644808`, `OR644804` (+94) |
| rev 25 | 56 | detect | 2023×4, 2024×2, 2025×1, 2026×1 | Eastern equine×48, Eilat virus×6, Getah virus×1 | `PZ710095`, `LC869669`, `KR260717`, `OP324813`, `OP324812`, `OQ511737` (+50) |
| fwd 2,5,6,17,18,20; rev 2,4,10,19,22,24 | 29 | fail | 2022×7, 2023×3, 2025×13, 2026×4 | Getah virus×29 | `PZ244959`, `PZ179619`, `PQ658766`, `PQ658765`, `PQ658764`, `PQ658763` (+23) |
| rev 4 | 13 | reduced | 2022×1, 2023×4, 2025×2, 2026×3 | Chikungunya virus×9, Alphavirus chikungunya×3, Mwinilunga alphavirus×1 | `PX800868`, `PX800288`, `PX800286`, `PQ841429`, `PV054363`, `OQ775537` (+7) |
| fwd 6,8; rev 4,5,11,14,17,26 | 10 | fail | 2010×10 | Modified×10 | `FV537406`, `FV537405`, `FV537402`, `FV537401`, `FV537271`, `FV537270` (+4) |

