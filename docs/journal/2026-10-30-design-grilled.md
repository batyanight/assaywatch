# Seven design questions, asked one at a time, before the next four builds

2026-10-30, after the four maintainer decisions of the same day
(`2026-10-30-decisions.md`). The approved interface for `drift.window_on` turned out, on
reading the code, to leave real choices open, and two further items (the footprint trend and
the drift-mechanism hunt) had never been designed at all. The maintainer was interviewed one
question at a time. These are the answers, and they are decisions: the builds below do not
reopen them.

| | Question | Decision |
|---|---|---|
| Q1 | Is `window_on: collection` a switch that can change a status, or a lens? | **A lens beside the verdict.** Deposit date stays the verdict's clock. No config switch. The report shows the collection-dated share for asm assays; no status can move. |
| Q2 | Collection dates arrive as full dates, year-month, bare years and junk. Where does a year-only record sit? | **Years, not days, for the whole lens.** Every asm record is re-dated to its collection YEAR and the existing year-granularity `Window` is reused. No invented days. Records without a four-digit year (including ranges) are excluded from the lens and counted. |
| Q3 | Where does the lens live? | **One report-wide section**, present only when asm assays exist: one row per asm assay with recent share by deposit clock, recent share by collection year, the gap in points, and how many records carried a collection year. |
| Q4 | Footprint trend: a column, or a second trend test? | **A second trend**, over distinct footprints per year, printed beside the by-record one. The by-record trend is an upper bound on the evidence (duplication), the by-footprint one nearer a lower bound (sequencing error inflates footprints; clade structure beyond the primer sites is invisible). The report says so in one clause when they disagree. Neither feeds the verdict. Absent, with the reason, when footprints are unknown. |
| Q5 | Where could a documented DRIFT case come from? | **Redesign papers first**: a new phrase family in `find_retrospective_cases.py` over the citation graph already on disk ("redesign", "updated primers", "modified to accommodate", five-plus years after the design paper), pre-registered like the `use` family. Fast-evolving-target literature and EQA reports are second and third. |
| Q6 | The bar for `mechanism: drift`. | **Strict.** The paper must show the SAME lineage changing over time at primer sites: an alignment, a table, or an explicit statement naming the substitutions and the years. "Newer isolates fail, older work" without that is `coverage` or not a row. |
| Q7 | Set 2 put 4 pan-family nests under `declining` against a published `works` about field sensitivity. Change the matrix's rule? | **Add a scope to each row.** A `works` row carries which lineage the paper tested; the matrix scores the tool's verdict for THAT lineage where a per-lineage verdict exists, the pooled one otherwise, and says which it used. Not a blanket relabel. **Disclosed**: this rule was chosen after set 2 was read, so its first honest test is on data not yet collected; applied to set 2 it is a description, not a score. |

## What this changes in the plan

- `drift.window_on` as a config key is **withdrawn**. The item becomes the collection-year
  lens (Q1 to Q3). `assemblies.py` still gains a `collected` column so the lens does not have
  to parse it back out of the title string for new archives; existing archives are read from
  the title.
- The footprint trend is a `trend.py` change plus one report clause (Q4).
- The drift hunt is a phrase family and a pre-registered expectation, then reading (Q5, Q6).
- The matrix gains an optional `scope_taxid` column in the cases files and a per-lineage
  lookup in `scripts/retrospective.py` (Q7). Set 2 may be re-described under it, never
  re-scored as evidence for a threshold.

Order of build: lens, footprint trend, redesign family, scope column, then the 93 `use`
rows re-read. Each its own PR; nothing under the screen hash's closure is touched, so none of
these forces a rescreen, and the S7b run on Sunday is unaffected.
