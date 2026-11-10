# 2026-11-10 — The remaining 60 papers reread: two duplicates withheld, one nest withdrawn, three primer pairs restored to print

**Finding: on the 2026-11-01 calls two statuses move, both to withheld as duplicates, and one nest verdict disappears;
nothing else moves and no recent denominator changes.** Three entries had stored primers shorter than, or shifted
from, what their papers print. 93 entries got a `citation.claim`; the two Keele rows still wait on a source. This
closes step 6b of the v0.3.0 plan and, with `docs/journal/2026-11-06-scope-reread-negative-verdicts.md` and
`2026-11-04-scope-reread.md`, the scope report the roadmap asked for: every live entry's paper has now been reread.

Method as before. Subagents read in batches (`local/release-work-2026-11-06/batch5.md` to `batch9b.md`), every
claim quote was machine-checked against the paper text (95 of 95), and separate subagents verified each reported
discrepancy against the paper and the measured products before anything was applied (`verified-5-8.md`,
`verified-9.md`). Of 79 items, 9 were overstated and 2 wrong, so that step kept earning its cost: the Yang
influenza narrowing was the reverse of what the paper says, and the batch's "Ibrahim could move a status" did not
hold once the printed primer was checked against every product.

| entry | status | why |
|---|---|---|
| `Dependoparvovirus_VP1_Gao_2002_2` | `stable` to withheld, draft | identical to `_1` in oligos, taxid and size; `duplicate_entry_unresolved` until one is retired |
| `Morbillivirus_P_Barrett_1993_MorbF` | `stable` to withheld, draft | the same pair as `Grosh_F` under other names; the same flag |
| `Orthohantavirus_S_Mangombi_2021_round2` | nest verdict gone; own status unchanged | Mangombi runs UHantaF2/R2 as one conventional PCR; the nest with Anthony round 1 was geometric |

- **Primers restored to print.** `Salmonella_enterica_invA_Rahn_1992` held the 3' 19 nt of the printed 26-mer and
  22-mer under invented names; `Shigella_ipaH_Sethabutr_1993` held both primers cut at both ends;
  `Yersinia_enterocolitica_yst_Ibrahim_1992` held the forward shifted 4 nt along the gene. On the measured products
  the restored bases match in 407 of 455 (Rahn, the rest 1-2 mismatches far from the 3' end), add a mismatch in 2 of
  202 (Sethabutr) and are exact in 37 of 37 (Ibrahim, giving the paper's 163 bp). No call changes class on that
  evidence; the rescreen at the frozen run decides. Grizzle's query now excludes by NOT clause the three viruses its
  note wrongly said it left out.
- **Chemistry.** Bohuski's two probes and Blooi's are hydrolysis probes (FAM/BHQ-1 and Cy5), not MGB; Zhao's three
  are FAM/BHQ1. Li 2025 is RPA at 39 C, not 40 cycles.
- **Sizes, by measurement.** McFarland 489 (572 matched no product), Deckers 599 and 803, Atkins round 1 413, Kapoor
  298 and 294, Vazquez-Moron 374 and 260, McAloose 188, Sanchez-Seco 554 and 245, Hsu 125, Lorch 81, Rahn 285,
  Ibrahim 163. Atkins round 2 keeps 342 because the modal 329 would drop two real products from the window.
- **Disclosed, not retargeted.** The paper tested less than the entry covers for Wang (O157:H7 only), Roy (primates),
  Zhai (2006's filoviruses), Pallister (Australian and European ranaviruses), Atkins (one cheetah astrovirus):
  `scope_wider_than_paper_tested` on each. Renteria-Solis amplified Tritrichomonas foetus and Ibrahim two Y.
  kristensenii strains: `cross_reactive`.
- **Not applied, the maintainer's.** Widening Clewley to HIV-1 and HIV-2 (122,714 recent HIV-1 records against 226
  SIV) and Muller to E. bieneusi (736, outside Encephalitozoon), each a retrieval move; testing Pallister's narrower
  scope; excluding raccoonpox from Meyer (0 recent records); retiring one of each duplicate pair. All on the roadmap's
  post-release list.
- **The Chlamydia 16S share.** The query returned 27.6% of *Chlamydia*'s 2020 deposits and 0.4% of 2023's (14 of
  3,742) while the genus's deposits grew from 568 to 3,742 (measured 2026-11-03 on `pdat`). The query is title-based
  under a genus that increasingly deposits genomes, so that assay's verdict is partly a fact about its query. The
  Chlamydia assemblies were tested and not added (`next-run-prep`): they would double count 379 of 493 genomes.

Page descriptions for all 95 entries are drafted in the batch claims files for step 10; `citation.description` is
not yet a schema field on `next-release`. `website/data/run.json` is re-extracted from the 2026-11-01 calls so the
site data describes this registry; it publishes only at step 15.
