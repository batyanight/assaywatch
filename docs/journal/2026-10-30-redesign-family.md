# The redesign-paper family, pre-registered and run: two rows, neither a redesign, zero toward a drift case

2026-10-30. Q5 of `2026-10-30-design-grilled.md` decided where a `mechanism: drift` case
could come from: redesign papers first, as a new phrase family in
`scripts/find_retrospective_cases.py` over the citation graph, restricted to citing papers
published five or more years after the design paper. Q6 set the bar: the paper must show
the SAME lineage changing over time at primer sites (an alignment, a table, or named
substitutions with years). This is the build and its first run. The bar was not applied,
because nothing reached it.

## What was built

- `late_redesign`, an opt-in family beside `use` (`--include late_redesign`), so the
  default queue stays failure-weighted. Six phrases: the three Q5 names (`redesign`,
  `updated primers`, `modified to accommodate`) plus `re-design`, `updated probe`,
  `modified to account for`. Nothing broader.
- A clock, `late_enough()`: the label survives only when the citing paper's year is
  `MIN_YEARS_AFTER_DESIGN` (5) or more past `citation.design_year`. An unknown year on
  either side excludes, as the lens's Q2 rule does. The constant lives in the script with
  the phrases it qualifies: it decides what is read, not what any assay is called.
- `admit()`, the per-hit decision, which the other families pass through unchanged; the
  queue gains a `design_year` column.

Pre-registered expectation, written in the script before the run: a short queue, most of
it redesigns for breadth or platform rather than for drift, and zero rows meeting the bar
is legitimate.

## The run

`caffeinate -i python scripts/find_retrospective_cases.py --include late_redesign`, 118
verified design DOIs, 223 rows in `results/retro-candidates-2026-10-30-late-redesign.tsv`
(gitignored run state; the queue is not promoted to `docs/` because it holds no reading
assignment the 2026-10-29 queue did not).

| family | rows |
|---|---|
| miss | 141 |
| weakened | 74 |
| mismatch | 6 |
| redesign (default group) | 3 |
| **late_redesign** | **2** |

The two `late_redesign` rows, in full, because they are the whole result:

| design paper | citing paper | years after | why it matched | what it is |
|---|---|---|---|---|
| Nipah N gene, 10.1126/science.288.5470.1432 (2000) | 10.1016/j.scitotenv.2021.145172 (2021) | 21 | `redesign` | a One Health review of crop-protection practice; the word is landscape redesign |
| Dependovirus VP1 nest, 10.1073/pnas.182412299 (2002) | 10.1038/mt.2011.153 (2011) | 9 | `redesign` | AAV6 shRNA delivery in a muscular dystrophy model; the word is vector redesign |

Neither is a primer redesign. Neither is a reading assignment. **Zero rows toward a drift
case**, which the pre-registration named as a legitimate outcome.

## What the run says

- The bare word `redesign` is the family's loose phrase and both of its hits are off
  target. It stays in the family as registered; a phrase changed after seeing the hits is
  not pre-registered. If the family is run again the expectation should be written down
  first and the two rows above treated as known noise.
- The five default-group counts are higher than on 2026-10-29 (miss 94 -> 141, weakened
  55 -> 74) over the same DOIs: Europe PMC's citation index grew in a day, or returned
  more fully. The 2026-10-29 queue remains the reading record; this run was not read for
  the default families.
- The citation graph cannot produce a drift case by this route. Q5's second and third
  sources, the fast-evolving-target literature and EQA reports, are what is left, and
  neither is a phrase search over citations of a design paper.
