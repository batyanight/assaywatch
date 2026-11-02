# Every stored amplicon, measured against real records

2026-10-05. `scripts/check_amplicons.py`, run over the whole registry.
Full table: `results/amplicon-audit.tsv` (gitignored, regenerate with the script).

`amplicon_bp` reads like an annotation and is not. It is the only field that says
how far apart the two primers should land, and `score.py` is already written to
reject a product of the wrong length as soon as
`config.yaml: amplicon.declared_tolerance` stops being `null`. On the day that is
turned on, a wrong value here starts throwing away real amplifications.

Most of these numbers were transcribed or quoted from a
paper. Measuring them was prompted by a run of individual corrections earlier the
same day - adenovirus inner 281 against a measured 258, the two pan-adenovirus
rounds 550 and 330 against 556 and 324, enterovirus 992 against 760, CMV 4125 550
against 599, West Nile 161 against 162, AAV 316 against 255 - at which point
checking the rest stopped being optional.

## What came back

155 assays have both a stored `amplicon_bp` and a local archive to measure against.

| | n |
|---|---|
| agrees exactly | 55 |
| within 3 bp | 26 |
| **disagrees by more than 3 bp** | **41** |
| no stored value | 18 |
| fewer than 5 products | 4 |
| no product anywhere | 11 |

**A `DISAGREES` row is not a defect.** Three different things produce one, and
only the first is an error worth fixing:

1. The stored number is wrong.
2. The primers are so degenerate that the measurement itself is unreliable.
3. The assay's target is not what the archive contains.

The third is the subtle one, and the audit found a clean example of it.

## The scope trap, worked

`Helicobacter_16S_Conley_2021` stores 194 bp, the figure Conley et al.
2021 states, and measures 178. That looks like a wrong number and is not.

Screening the entire *Helicobacter* archive for the assay's probe returns **zero**
records with an exact site. The probe sits on a 14 bp insertion the paper says is
unique to *Helicobacter* sp. Grand Cayman Blue Iguana 1, a provisional species
that is not in GenBank's nucleotide records at all. Every product the measurement
found therefore came from some other *Helicobacter* - and 194 minus that 14 bp
insertion is 180, which is exactly the second peak in the measured distribution.

The paper is right about its own organism. The database cannot corroborate it,
because the organism is not in the database. The stored value stays.

Its sibling, a pan-*Helicobacter* entry since removed, was the opposite case: a
pan-*Helicobacter* assay, where the genus archive is the right thing to judge it
against. It measures 162/163/164 across 1,121 of 1,285 products, and its stored
180 matches none of them. Corrected.

**So the question to ask of every `DISAGREES` row is not "is the number wrong"
but "is this archive evidence about this assay".**

## The 13 worth looking at first

Filtered to a primer pool of 64 or less, at least 30 products, and a mode holding
at least 40% of them - which removes the degenerate-primer noise.

| assay | stored | measured | n |
|---|---|---|---|
| `Chordopoxvirinae_POL_unpublished` | 192 | 188 | 13421/13421 |
| `Chordopoxvirinae_POL_McAloose_2016` | 192 | 188 | 13423/13423 |
| `Haemosporida_cytb_Hellgren_2004_HaemF` | 480 | **525** | 4269/4274 |
| `Morbillivirus_canis_H_Muller_2011_Mueller_3F` | 563 | 544 | 1814/1823 |
| `Morbillivirus_canis_H_Muller_2011_Mueller_2F` | 570 | 560 | 1453/1457 |
| pan-*Helicobacter* sibling (since removed) | 180 | 162 | 532/1285 |
| `Leptospira_flaB_Hsu_2013` | 120 | 125 | 774/775 |
| `Helicobacter_16S_Conley_2021` | 194 | 178 | 206/476 |
| `Morbillivirus_canis_H_Muller_2011_Mueller_1F` | 567 | 552 | 431/432 |
| `BORNA_VIRUS_N_gene` | 445 | 441 | 317/317 |
| `Bornaviridae_N_Zimmermann_1994_round1` | 752 | 748 | 314/314 |
| `Leucocytozoon_cytb_Hellgren_2004` | 478 | **524** | 234/235 |
| `Filoviridae_L_Zhai_2007_Filo_U12683_A` | 630 | 634 | 150/150 |

Two of these have been dealt with already, both Helicobacter rows above. The rest
are a worklist, not a verdict.

Reading them:

- **The two haemosporidian entries are the largest discrepancies and the best
  evidenced.** 480 against 525, in 4,269 of 4,274 products, with a
  non-degenerate primer pair. Both are already flagged as composites whose scope
  comes from a different paper than the one cited (the Hellgren/Bensch case), so
  the stored size plausibly belongs to a different primer combination than the one
  stored. Worth settling properly rather than quickly.
- **The four CDV H-gene entries drift 10 to 19 bp short**, consistently, with
  non-degenerate primers and over a thousand products each. These are the
  "muller,2011" entries whose citation is still unresolved, so there is no paper
  to check a stated size against - the measurement is all there is.
- **The repeated 4 bp offsets** - pox twice, Borna twice, filovirus once - look
  like a stated-size convention rather than independent errors, and the pox pair
  is unanimous across 13,000 records. Worth one look at whether the sources count
  the primers in.

## What was deliberately not done

Nothing was written back to `registry/` in bulk. Changing a stored amplicon
belongs in an entry's `notes_curator` next to the evidence for it, which is how
the dozen corrected individually today were handled, and the point of the Conley
example above is that a bulk edit would have introduced an error rather than
removed one.

The 28 lower-confidence rows are not listed here. Several carry primer pools in
the millions - one at 31,850,496 - where a 20-mer finds a site in almost any
record and the resulting "product" means nothing. `python -m assaywatch.degeneracy
registry` is the companion check, and the `pool` column in the TSV repeats it.

## Correction to the numbers above

The counts in this file come from the FIRST run of `check_amplicons.py`, which
picked a taxon's retrieval group arbitrarily. A group is a (taxid, query) pair
and 14 taxa hold more than one - *E. coli* holds four - so some assays were
measured against records retrieved for a different assay's query. That is how
both Wang 1997 entries were reported as giving no product at all, minutes after
`check_submission.py` had amplified them happily; with the group chosen by the
entry's own query they measure 440 bp and agree exactly.

The script now resolves the group with `retrieve.group_slug()` and records which
one it used in a `group` column. **Re-run it before trusting any row here**; the
13-row shortlist and the Helicobacter reasoning are unaffected, because those
taxa hold a single group each.

One further limitation, not a bug: the default 3-mismatch cap is deliberately
conservative and will report `no-product` for consensus assays whose primers
normally sit further off. The four orthobunyavirus rows are the clear case - the
M-segment 5' entry's own notes record 93 evaluable and 8 detected in the
project's 2026-10-04 screen, where this audit finds none. Raise `--max-mm` for
those, and read `no-product` as "not at this stringency" rather than "never".
