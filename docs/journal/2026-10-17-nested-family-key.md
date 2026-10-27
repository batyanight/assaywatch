# The nested family key was wrong, and it manufactured two findings

2026-10-17. Measured on `results/2026-10-15/calls.tsv.gz`.

## What was wrong

Family membership was the id with any `_roundN` suffix removed. That key fails three ways,
and all three were live in the registry:

1. **An unrelated entry shares the base.** `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme` is a
   440 bp consensus assay with no DOI and no declared round. It shares a base with Lan 2010's
   nested pair, so it was pulled into that family and displaced Lan's real round 1.
2. **`_round2_2` escapes the `$`-anchored suffix.** A second nest on one base can never
   assemble. Two papers' CMV gB nests were crossed by this: Deckers' round 1 (800 bp) was
   paired with Prepens' round 2 (230 bp).
3. **A nest can span unlike ids.** The Chlamydia 16S nest is one genus round 1 feeding three
   species-specific round 2 entries across three taxids. No id base can express it, so all
   four entries sat in the unpaired list.

## What it cost

Two of the three families reported as non-nesting on 2026-10-14 were mis-pairings, not
biology. Containment on the corrected pairings:

| pairing | shared records | inner inside outer |
|---|---|---|
| coronavirus `Lan_2010_round1` x `round2` (one paper) | 6,672 | **6,668 — 99.9%** |
| coronavirus bare 440 bp consensus x `round2` | 6,694 | 0 — 0.0% |
| CMV Prepens `Virol_2007_round1` x `round2` | 726 | **726 — 100%** |
| CMV Deckers `gB` x `round2_2` | 578 | **578 — 100%** |
| CMV `gB` x `round2` (across two papers) | 659 | 0 — 0.0% |
| enterovirus `VP3_VP1` x `round2` (one paper) | 3,808 | 56 — 1.5% |

Those are a direct containment pass over every row carrying both spans, which is the only way
to measure the two wrong pairings, since the families they describe no longer exist.
`nested.assess` counts a narrower denominator — rows that are evidence about the assay for
*both* rounds — and so reports slightly fewer: **6,667 of 6,671** for the coronavirus nest,
726 of 726 and 578 of 578 for the two CMV nests, 56 of 3,760 for the enterovirus pair. The
`assess` figures are the ones the report prints, and the ones used below.

So the claim in the 2026-10-14 report and in `RESUME-HERE.md` — that the coronavirus RdRp
rounds are disjoint and "really two assays" — is **withdrawn**. They are a nest on 6,667 of
the 6,671 records both rounds can be judged on, and a consequential one: run as published it reaches 44.3% where round 2 alone reads 69.5%, a
25-point gap that was invisible while the family was mis-assembled.

Three real nests were missing from the coverage table entirely (coronavirus, both CMV pairs),
and three more never assembled at all because an author/year token sat on one round and not
the other (adenovirus primate polymerase, circovirus Rep, Paramyxovirinae L).

## The fix

`source.nested_family`, an optional declared key that overrides the id base, plus one rule:
given the registry mapping, an entry joins a family only if it **says** it is part of a nest
(`nested_round` or `nested_family`). The id base remains the default, so the 15 families that
were already correct were not touched.

`nested_round` was deliberately NOT written where it was absent. The CMV entry's
`notes_curator` records the convention — that field holds what the spreadsheet said, and the
spreadsheet recorded no round — so membership is declared in `nested_family` instead and round
order falls back to the declared product size, which is correct for all five such entries.

21 entries now declare a family. Families **in the registry** went 23 to 27; of those, the
ones with per-record data in the 2026-10-15 calls went 21 to 24 (the rest have no records
either round can be judged on). Entries declaring a round but landing in no family went 15
to 3. The two family counts are different metrics and are easy to confuse — the registry
count is what `nested.families` returns, the smaller one is what the report can print.

## Before and after

| | 2026-10-14 | 2026-10-17 |
|---|---|---|
| families with per-record data | 21 | **24** |
| failing containment | 3 | **1** |
| entries declaring a round, in no family | 15 | **3** |

Newly reporting conditional coverage (round 1 / round 2 alone / run as a nest):

| family | r1 | r2 | nest |
|---|---|---|---|
| `CORONAVIRUS_..._Lan_2010` | 55.8% | 69.5% | **44.3%** |
| `CIRCOVIRUSES_..._Mankertz_2000` | 68.2% | 33.2% | 31.0% |
| `Paramyxovirinae_..._Tong_2008` | 58.8% | 32.0% | 31.8% |
| `ADENOVIRUS_..._Primate_speci_Casas_2005` | 81.9% | 78.8% | 76.2% |
| `CMV_..._gB_Deckers_2009` | 93.9% | 93.9% | 92.9% |
| `CMV_..._gB_Prepens_2007` | 91.9% | 98.4% | 91.9% |

## Second pass: the containment criterion was wrong too

The enterovirus pair was the one survivor of the family-key fix, and it was not curation
either. Its two rounds **share their reverse site**; round 2's primer is 27 nt against round
1's 19, longer at the 5' end. A primer whose 5' tail hangs off the template still primes -
only the 3' end has to anneal - so round 2's amplicon ends exactly 8 bp past round 1's while
extending from the identical base. Measured: `inner_end - outer_end` is **+8 on 3,722 of 3,808
records**, matching 27 - 19 exactly.

So containment now asks where the inner primers **extend from**, not where their amplicon
would end: both inner primers' 3' ends must lie inside the outer product, read from the
`fwd_site`/`rev_site` columns the screener already writes (`2885-2912-`, so the 3' end is the
low coordinate on the minus strand). Calls written before those columns existed fall back to
the old span test.

### Result on the 2026-10-15 calls

**All 26 families with per-record data nest. Nothing fails containment.** The three-families-
fail claim is gone in its entirety: two were mis-paired, one was mis-measured.

The enterovirus pair reads 3,732 of 3,760. The two Hantavirus nests, declared this session,
enter the table for the first time:

| family | r1 | r2 | nest | contained |
|---|---|---|---|---|
| `HANTAVIRUS_..._nest_A` (250 / 236) | 91.0% | 97.9% | 89.9% | 4,165/4,167 |
| `HANTAVIRUS_..._nest_B` (532 / 417) | 17.8% | 44.8% | **17.6%** | 2,488/2,495 |

Nest B is worth a look: round 2 alone reads 44.8% and the protocol delivers 17.6%, a 27-point
gap of the lyssavirus kind.

This should be read with some suspicion of itself. A check that now passes everything is
weaker evidence than one that fails sometimes, and the honest summary is that containment has
never yet caught a real protocol error - it has caught two bookkeeping faults and one error in
its own criterion. It still fails a pair whose inner primers land outside the outer product,
and a test pins that.

## Decisions taken 2026-10-17

- **Containment** judged on inner primers' 3' ends (above).
- **Hantavirus**: two nests declared, A = 250 + 236 and B = 532 + 417, flagged
  `NESTED_FAMILY_FROM_GEOMETRY` on all four entries. These carry no DOI; B's two entries share
  their reverse primer outright, which is what ties the pair, and A's forwards are the same
  site offset by two bases. Both outer rounds contain `_round2` geometrically, so geometry
  alone does not separate them - if a source turns up, check A first.
- **`PROBOSCIVIRUS_POL_Latimer_2010_EEHV6_round2`**: kept, with its existing
  `SINGLE_SPANNING_RECORD` flag. 6 calls and 1 spanning record in the 2026-10-15 run says how
  little EEHV6 is deposited, not that the assay is bad. Its round 1 is still absent from the
  registry, so it stays on the unpaired list for the right reason.
- **ORTHOPOXVIRUS ATI**: `amplicon_bp_range: [540, 1700]` added, a new optional schema field
  mutually exclusive with the scalar `amplicon_bp`, with `declared_tolerance` applied outward
  from each end (so 405-2125 bp at 0.25, against the global 50-3000). **Note the range is
  540-1700, not the 1067/1535/1538 carried in earlier notes** - those are the monkeypox clade
  modes only. The entry's own measurements span volepox 542 bp to cowpox 1673 bp.

## What still needs a curator

1. **`PROBOSCIVIRUS_POL_Latimer_2010_EEHV6_round2` has no round 1 in the registry.** Kept
   (above), but completing the nest means reading the EEHV6 round 1 primers out of Latimer
   2010, which needs the paper. The other three EEHV families all carry their round 1.
2. **The Hantavirus assignment has no source.** Declared from geometry and a shared primer and
   flagged as such. The 250 bp outer with a 236 bp inner is the part to check first.
3. **Round order for the five outer rounds that declare no `nested_round`** rests on the
   declared product size, not on a protocol. It is right in all five cases by containment, but
   it is an inference.

## Verification

`python -m assaywatch.validate registry` reports 217 valid, 0 problems. Suite **1126 passed,
11 skipped**; ruff check and format clean. Eight tests pin the new behaviour: the two
mis-pairing modes, a declared family spanning unlike ids, the id-base fallback, containment on
primer 3' ends, its span fallback, a genuinely non-nesting pair still failing, and the
amplicon range's mutual exclusion with the scalar size.

**The report has not been regenerated, and one assay does need a rescreen.** The nested
numbers above come from re-running `nested.assess` over the existing 2026-10-15 calls: the
family key and the containment criterion change grouping and measurement, not scoring, so
those need only a re-render.

`ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997` is the exception. Giving it
`amplicon_bp_range: [540, 1700]` narrows its accepted product window from the global
50-3000 bp to 405-2125 bp, which is a scoring change, so **its calls are stale until it is
rescreened**. Nothing else in this work touches a call. Until then
`results/2026-10-15/report.md` also still carries the old nested table and the withdrawn
coronavirus sentence.
