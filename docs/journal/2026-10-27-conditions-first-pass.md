# The registry now knows what temperature 119 of its assays ran at

2026-10-27, night. `conditions` / `performance` / `panels` went in empty earlier this
evening, the way `by_chemistry` did: the shape validated before anything was read into
it. This is the first populate pass, from the 164 PDFs and 14 XML deposits in `papers/`.

## Before

Counted 2026-10-27, over 214 entries: annealing or cycling in **7**, LoD or efficiency
in 23, master mix or Mg²⁺ in 2, one-step against two-step RT in **none** — and all of it
in curator prose, where nothing can read it. That is a primer registry, and it is the
reason `thermo: false` ships: a mismatch costing 6 °C of Tm is irrelevant at an
annealing temperature of 50 and fatal at 62.

## After

`scripts/extract_conditions.py --propose` reads each paper, finds the sentence carrying
a number, and emits one row per field per entry **with that sentence quoted beside it**.
644 proposals over 211 entries; 3 entries have no readable paper on disk and 34 papers
on disk print no protocol this script can find (those get a `conditions_not_printed`
proposal, which is a finding about the paper, not a gap in the reading).

`--apply --only-sole --write` then took the subset that needs no judgement:

- the field is one of `annealing_c`, `cycles`, `rt`, `mg_mm`;
- the paper states that value **once** (a paper printing two annealing temperatures is
  describing two protocols and only a reader can say which is this entry's);
- the annealing temperature comes from the paper's **own label**, not from the
  convention that the middle of three temperatures is the annealing step;
- the entry is not a nested round, because the rounds of a nest share a paper and
  almost never share a programme.

**119 entries, 292 values.** Annealing temperatures run 40–62.5 °C, median 54;
magnesium 1.25–6 mM, median 2.0; 84 cycle counts; 14 RT formats, where the schema
previously had none. 270 rows were left for a reader (an LoD and a master mix are
quoted prose, and the oligo concentrations are below), 122 are ambiguous, 79 are nested
rounds. The full proposal table, including every row NOT applied and the sentence each
came from, is committed as `docs/2026-10-27-conditions-proposals.tsv` — `papers/` is
gitignored, so that file is the durable record of what was read, and re-running
`--apply --only-sole` against it reproduces exactly these 119 entries.

## Five extraction bugs, each found by looking at the numbers

Worth recording, because every one of them produced a plausible value and four of the
five would have passed any range check:

1. **The first temperature in range is not the annealing temperature.** Rossi 2024: "15
   min at 50 °C for reverse transcription … and annealing at 54 °C" was read as 50.
   Now the temperature nearest the word, within 60 characters.
2. **The label is sometimes nearer the wrong number.** "52 °C for 1 min (annealing) and
   68 °C for 30 s (elongation)" put "anneal" closer to 68 than to 52, so the
   parenthesised-label shape is matched before proximity is tried.
3. **A spaced-out decimal point.** Rahn 1992 prints "1 . 25 mm MgCl 2", from which a
   plain pattern read **25 mM** — twenty times the value, and the only one of the five
   that something caught, because `Conditions.mg_mm` has a ceiling of 20.
4. **A decimal comma.** Deckers 2009 prints "2,0 mM MgCl2", read as **0 mM**. No range
   check can see that: zero magnesium is a number.
5. **The stock is not the final concentration.** Kuno 1998: "3 µl of 50 mM MgCl2 (final
   concentration, 1.5 mM)" was read as 50. A stated final concentration now wins, but
   only within 60 characters of the unit it belongs to — anchoring it on the sentence
   instead picked up "final concentration: 10 mM Tris" from a digestion buffer.

Bugs 3 and 5 are why **the oligo concentrations are not applied at all**. Of the first
four read, one was a 0.2 µM final concentration OCR'd as "0n2 µM" and one a 100 µM
*stock* whose final concentration the sentence never gives. Which number a
concentration is for is a judgement about the reaction, not a pattern.

## What this does not do

It does not turn `thermo` on. It makes `thermo: true` *arguable* for 47 entries that now
carry an annealing temperature, against 7 before, and the honest reading of the other
167 is that a ΔTm cannot be interpreted for them at all. It also does not touch
`panels`, which is a table in each paper and a read of its own.
