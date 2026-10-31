# Wave 5: the report leads with ten assays, and is navigable without a script (2026-10-23)

Plan items 5.6 and 5.7.

## 5.6 The problem

The 2026-10-22 report flagged **93 of 204** assays and sorted every section by ascending
detected share, so what led the page was whichever assay had the lowest number — for
this registry, always a pan-family consensus PCR screened against a whole family. The
stated audience is "a lab with no bioinformatician" (README) and they were given no way
in.

## What was added

A **Start here** section after the headline counts and their caveats, capped at
`report.max_triage_rows` (10). The full status tables are unchanged below it.

The order is **lexicographic over criteria whose direction is individually obvious**, not
a weighted score — a composite would need weights, and numbers set by eye are what
`config.yaml`'s own header warns about:

1. `declining` before `low coverage` — a measured fall from a level that worked is
   actionable; never having covered a clade is a scope question;
2. entries whose **oligos** are not in doubt first;
3. larger shortfall below the threshold first;
4. more evaluable records first;
5. assay id, so the list is stable between runs.

Two exclusions, both the project's own caveats, **neither a status change** — the rows
stay in their tables and are only kept from leading:

- **degeneracy `high` or `severe`** (28 of 74), where "detect calls approach a tautology"
  (README). Folding degeneracy into a verdict would break the convention that it is
  "reported alongside the drift numbers rather than folded into them"; keeping such an
  assay off the front page does not.
- **a flag the duplication check did not confirm** (36 of 74). `_cluster_check` is
  explicit that it "can only withhold the label 'survives'", so it cannot gate a status —
  but "this flag held when duplicated records were discounted" is exactly what makes one
  worth opening first.

Both counts are printed, so a reader sees what was held back and why.

## A flag the plan got backwards, and I repeated

Criterion 2 was first implemented as "carries any recorded caveat". That is wrong, and
wrong in a revealing direction: it ranked `amplicon_measured_not_published` — which means
the product size was **measured on real records instead of quoted from a paper**, this
project's own preferred practice — alongside `oligos_not_in_cited_paper`. Same for
`cross_reactive` (a specificity disclosure about a correct entry) and
`retrieval_scope_incomplete` (about which records were fetched).

`review.OLIGO_DOUBT` now names the nine flags that cast doubt on the sequences a screen
actually depends on, and a test asserts it is a **strict subset** of `CAVEAT` and
excludes the good-practice flags by name. Writing that test caught a second error:
`oligo_source_unresolved` and `oligo_sequence_uncertain` are doubts about oligos but are
`OPEN` questions, so those entries are held out of scoring entirely (wave 1) and can
never reach a list that ranks scored assays.

The effect is visible: `INFLUENZA_A_ssRNA_NP_Tsukamoto_2010` moved up once its only
flag — `retrieval_scope_incomplete` — stopped counting as doubt about its oligos.

## And a correction to the outside evaluation

The evaluation said 6 `declining` rows "carry a note that says 'a coverage gap, not
drift'. The heading and the note contradict each other." **They do not.** The heading is
the pooled verdict and it is sound in each case — `Pan_Plasmodium..._cytochrome_c` is at
10.2% with its upper bound below threshold and a change from baseline of −35% to −21%, a
real fall from a level that worked. The clause describes the worst **lineage**, saying why
the lineage check did not also drive the call. Two estimands in one sentence, not a
contradiction.

So no row was moved. What was wrong was the wording, which left "not drift" ambiguous
about what it described; the note now reads "…**separately**, lineage X … so **that
lineage** is a coverage gap rather than drift".
`docs/journal/2026-10-23-baseline.md` carries the correction.

## 5.7 Navigation, and why not JavaScript

The plan called for an inline-JS filter box. **Deliberately not done**, after measuring
what was actually missing:

- `report.html` is 1 MB with ten `<h2>` headings and **zero anchors**: a reader could not
  jump to a section or be sent to one assay.
- But the status tables are **open** — only the 74 per-assay detail blocks are inside
  `<details>` — so the browser's own find already reaches every assay row. Search was
  not the gap; navigation was.
- README states "no JavaScript" as a property of this file, with a reason ("opens from a
  `file://` path or GitHub Pages in a lab with no bioinformatician"). That is the
  author's documented decision, and the gap can be closed without overriding it.

So: every section heading has an `id`, there is a contents list linking to all of them
with counts, each detail block is `<details id='detail-<assay>'>`, and every assay id in
the triage and status tables links to its own detail. A `<details>` whose fragment is
targeted is opened by the browser, so one link lands a reader inside an assay's year
table with nothing running. A test asserts the anchors exist **and** that `<script>` does
not, so the no-script property is now pinned rather than assumed.

If a filter box is wanted later, that is a one-line change to the same test and a small
inline script — but it should be a deliberate reversal of a documented decision, not a
side effect of adding search nobody had asked for.
