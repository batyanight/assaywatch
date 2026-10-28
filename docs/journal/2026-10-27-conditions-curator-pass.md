# Reading 64 papers for the protocol the automatic pass could not assign

2026-10-27, late. `--apply --only-sole` took the 292 values a paper states once
(`2026-10-27-conditions-first-pass.md`). It deliberately refused 201 rows: 122 where the
paper prints more than one protocol, and 79 where the entry is one round of a nest. Those
are not noise — they are the papers that describe a panel, a touchdown or a nest, which is
most of a methods literature. This is the reader's pass over them.

`scripts/extract_conditions.py --digest` prints, per paper, the entries that cite it, the
values proposed with the sentence each came from, and **every** protocol-bearing sentence
in the paper. 64 papers, read once each instead of once per entry — 88 entries with an
ambiguous row cite 47 papers, and the nests add 25 more.

**236 values read by hand**, each with the sentence it came from recorded in the committed
proposals table: 87 annealing temperatures, 66 cycle counts, 20 magnesium concentrations,
24 primer and 11 probe concentrations, 18 RT formats, 5 efficiencies, 3 LoDs, and 2
`conditions_not_printed` flags on a paper that genuinely prints no protocol.

## What a reader does that a pattern cannot

Every one of these is an attribution, not an extraction. The number was always right
there; the question was which assay it belongs to.

- **Xiao 1999** prints two programmes: one at 60 °C for the full-length SSU gene it cloned
  and sequenced, one at 55 °C for the nested PCR-RFLP protocol. The registry's two
  Cryptosporidium entries are the nested protocol (1,325 and 819–825 bp, matching their
  stored 1319 and 822), so **55 °C**, with 6 mM Mg²⁺ in the primary step and 3 mM in the
  secondary — a difference the paper states as its only one. `--only-sole` would have
  written 60 for both if they had not been nested rounds.
- **Latimer 2010** splits nine EEHV entries in two with one sentence each: "the redundant
  POL PCR" is the degenerate pan-EEHV assay at 34 cycles, "all other PCR amplification"
  is every virus-specific entry at 45.
- **Zhao 2013** says in its own words that the BPSV assay's "efficiency is reduced
  considerably at 62.5 °C; its annealing temperature is kept at 60 °C". The automatic pass
  had written 62.5, from a sentence about the PCPV assay. That is the single worst kind of
  error available here, and it was in a file.
- **Spackman 2002** anneals the matrix-gene set at 60 °C over 45 cycles and the H7 set at
  58 °C over 40. The entry carried 58. It matters more than most, because that assay is the
  one whose subtype table was measured tonight and the first a thermodynamic read would be
  run on.
- **Annis 2004** names its temperature as the entry's own: "60 °C (the annealing
  temperature for the Bd1a and Bd2a primers)", against 57 °C for the universal ITS5/ITS4
  control. Its magnesium is a specificity result rather than a detail: 0.9 mM is what
  stops the non-*Batrachochytrium* chytrids amplifying, and the paper adopted it for that.
- **Sledge/dao02986** gave a dsDNA poxvirus assay `rt: one_step` and 60 °C, both from
  sentences about other assays in the same multi-assay paper. It is a DNA target amplified
  from DNA extracts: `rt: none`, 45 °C.

## Corrections, counted

Twelve values an earlier pass had written were wrong and are corrected (`how` beginning
`FIX` in the resolution table, applied with `--allow-fix`): the BPSV and matrix-gene
annealing temperatures above, a sequencing programme's 25 cycles read as the lyssavirus
assay's, a probe concentration read from the primer's half of its sentence, a Perkinsea
gradient's low end read as its retained temperature, a reptarenavirus optimisation's
"38 vs. 42 cycles" read as 42 where the protocol repeats 38, a two-stage Nosema programme
read as its first 10 cycles, the HN-gene cycle count taken from the L-gene sentence, and
the pan-herpes 48 °C below.

## A sixth extraction bug, and the one that would have been hardest to notice

**A degree sign the PDF lost becomes the digit 8.** Chmielewicz 1996 renders every one
that way, so "948C" is 94 °C — and a two-digit match inside it is **48**. That is how
`Pan_HERPES_dsDNA_Polymerase` came to carry an annealing temperature of 48 from a paper
that prints 46. Normalised now in `sentences()`, where three digits before a C with the
last of them 8 is a lost degree sign in every paper on disk; 728 °C is not a PCR
temperature. Re-running the whole proposal pass after the fix changed exactly **2 of 644
proposals**, both that entry and its nested round, and recovered 2 the bug had hidden —
whose values are the ones this pass had already read by hand, which is the check worth
having.

The five from the first pass and this one are pinned in `tests/test_extract_conditions.py`,
one test each, with the paper that exposed them.

## What is still not in the registry, and why

- **Touchdown and step-down protocols cannot be written down.** Lan 2010 steps from 65 °C
  down 1 °C per cycle for 15 cycles and then runs 35 at 50; a 1998 SIV nest steps 50 → 35
  and then runs 15 more; Bocavirus runs six high-stringency cycles before its 35. The
  schema has one `annealing_c`, so each of these records the temperature its working cycles
  run at and says so in the resolution note. The honest fix is a `touchdown` block, and
  nothing here argues it is worth one yet.
- **A deliberately varied temperature.** Ahne 1999 says "annealing and RT temperatures
  varied in this study between 40 and 50 °C because all viral isolates did not amplify at
  the higher temperature", and reports results at 40, 45 and 50 for the same primers. No
  single value is that assay's, so its four entries carry cycle counts and no temperature.
- **Three entries whose value I now disbelieve and cannot replace.** `CMV_UL55_gB_Deckers_2009`'s
  magnesium and the three Sigrist orthobornavirus entries' magnesium both came from the
  conventional arm of a paper whose probe assay is the registry entry; the Leptospira flaB
  annealing temperature came from one of three programmes in a MassTag paper and cannot be
  attributed. Removing a value needs a hand edit rather than this tool, which only adds and
  fixes, so they are listed here and in `ROADMAP.md` for the maintainer.
- **Oligo concentrations stay a reader's job**, for the reason the first pass gave: whether
  a number is a stock or a final concentration is a judgement about the reaction. Where a
  paper states its own final concentration — Kuno 1998's "(final concentration, 500 nM)",
  Bohuski 2015's "(final reaction concentration 0.4 µM)" — it is read; where it gives only
  a stock, it is left out.

## After this pass

`conditions` carries a protocol for 119 entries from the automatic pass plus the entries
corrected and extended here. `thermo: true` is arguable for the entries that now carry an
annealing temperature and remains dishonest for the rest, which is the same sentence as
before, with a larger first half.
