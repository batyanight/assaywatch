# Searching for papers that USE an assay, not ones that complain about it, took the held-out set from 3 rows to 14

2026-10-29. The retrospective queue was declared spent on 2026-10-28: 220 rows, every
PDF in hand, 2 CONFIRMED / 1 VARIANT / 10 UNCONFIRMABLE, and the conclusion that "no
document will settle the remaining rows". That was true of the queue and false of the
method. The queue was **failure-weighted on purpose** — it searched the citation graph
for phrases like *false negative*, *failed to detect*, *primer mismatch* — because a
documented failure is the scarce case. The cost of that choice had never been measured.

`scripts/find_retrospective_cases.py --include use` (the opt-in phrase family added
2026-10-28, kept out of the default queue by its own pre-registered design) searches
instead for a paper that simply **runs** a registry assay and **reports a result**. Over
the same 118 design DOIs:

| | failure-weighted queue | with `use` |
|---|---|---|
| candidate rows | 220 | **248** (93 of them `use`) |
| CONFIRMED (paper, assay) pairs | 2, in three weeks | **13, over 7 papers, in one run** |
| VARIANT | 1 | 3 |
| UNCONFIRMABLE | 10 | 153 |

`check_candidate_identity.py` answers the question that actually blocks a row — did this
paper test *our* oligos — before any reading time is spent, and all 13 read `exact` on
every slot. Then each paper's **results section** was read from the Europe PMC full text,
because the bar is what a paper reported and not what its abstract advertises.

Eleven rows proposed into `docs/validation-cases-heldout-2.tsv`, all awaiting sign-off.

## The one that matters: a mechanistic failure, located at the 3' end, in the paper's own words

Himmel, Harl et al. 2022 (Malar J 21:1) screened 183 accipitriform raptors with the
Hellgren 2004 haemosporidian nest — the same nest whose Leucocytozoon entry is the
documented tier-2 catch M1 nearly cost the project — and says this in its methods:

> The nested PCR assay by [6] does not allow amplification of the CytB in parasites of
> the *L. toddi* group. In particular, the forward primer of the first PCR, HaemNFI,
> shows a two bp mismatch at the 3'-end compared to *L. toddi* group sequences (AG vs
> GC), and the nested reverse primer HaemR2L [...] features a two bp mismatch at the
> 3'-end (GC [complement] vs CT, TT, or AT).

and this in its discussion, about a second clade:

> Both 'nest 2' reverse primers (HaemR2 and HaemR2L) of the standard PCR protocol by [6]
> feature four mismatches in the 3'-region to lineages of this group, which might explain
> the extremely scarce molecular genetic record in other studies.

It then **acted on both**: every sample was screened a second time with a group-specific
protocol, and the paper's own sequences for those clades came from those other primers.

Three rows, one per registry entry whose oligos are named — `fails`, `mechanism:
coverage`. This is the shape the project claims to predict: not a vague "performed
poorly" but mismatches counted at the 3' end of named primers, which is exactly what
`primer_3prime_window` and `terminal_mismatch_fails` are about. **The honest caveat is
recorded with the rows**: the same nest found 80 of 183 birds infected, so the failure is
clade-specific inside a working survey, the same shape as the Paramyxovirinae rows in the
development set.

## The other eight

- **Pan-herpes DPOL (VanDevanter)**, twice over and both `works`: typing EHV-1 and EHV-4
  across equine swabs and blood (Open Vet J 2024, received date in the JATS, so `as_of`
  is exact), and recovering a **novel** gammaherpesvirus from a wild Chilean pudu whose
  polymerase is 78.7% identical to its nearest relative. A pan-family assay amplifying
  something previously unknown is the clearest `works` available.
- **Chu 2008 pan-astrovirus**, both rounds `works`: 10 of 16 buffalo-calf samples in the
  single round, **16 of 16 with the nest**, sequenced to a candidate new species. The
  62.5% is sensitivity, not coverage — the same distinction the Cryptosporidium row in
  this file already turns on.
- **Pan-adenovirus hexon**, both rounds `works`: 4 of 775 DRC rodents, sequences 81–91%
  identical to MAdV-2. The authors' own caveat that the true prevalence "will be higher
  than what was detected" is recorded with the row, since a maintainer could read it as
  a named gap and make these `partial`.
- **Quan pan-coronavirus (`_round2`)**, the only head-to-head in the batch and the one
  `partial`: a ~3,000-animal Cameroon survey ran two pan-CoV protocols on the same
  samples and reports "the Watanabe PCR protocol produced 173 positive results, while
  the Quan PCR protocols produced 64". Ours is the Quan pair, so it found CoV RNA (not
  `fails`) and a second assay found 2.7× more (not `works`).

Two near-misses are recorded as NOT A ROW so they are not chased again. The disc-herniation
study (BMC Musculoskelet Disord 2020) prints all five pan-herpes oligos and found **all
15 samples negative** — but untargeted sequencing of the same samples found no
herpesvirus either, so it is a true negative, and its only statement about our assay is
that the positive controls amplified. And the other coronavirus entry is not ours to
claim even though the paper prints CoV-FWD3/CoV-RVS3: that entry stores the Drexler
modification, not Watanabe's original, so the checker reads it VARIANT and the 173
positives belong to a primer pair the registry does not hold.

## What this changes

Set 2 now has **14 rows: 10 `works`, 3 `fails`, 1 `partial`** — inside its own 15–20
target — and **11 of them have never been scored**, which was the point. The file was
deliberately not run through `scripts/retrospective.py` when the rows were written,
because `--cases` scores every row and that is how its first three rows got spent.

What it does **not** fix is the gap the header named first: still **zero rows with
`mechanism: drift`**. Every documented failure this project has found is a clade the
assay never covered, not a target that moved out from under it. The drift flag — the
thing the pipeline is named for — still rests on about one ground-truth event, and a
`use`-family search cannot fix that, because a paper reporting decay over time is rarer
than one reporting a clade it never reached. 153 UNCONFIRMABLE rows remain and most will
stay that way; the 93 `use` rows that did not reach CONFIRMED are the next cheap read.
