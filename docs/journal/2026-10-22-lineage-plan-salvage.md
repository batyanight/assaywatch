# Salvaged from the 2026-10-15 lineage plan before closing PR #3 (2026-10-22)

PR #3 (`docs/2026-10-15-lineage-plan`, one commit, docs only) proposed
lineage-conditional verdicts and asked for three decisions. Two days later a
parallel session on the other machine wrote `docs/journal/2026-10-17-estimand-plan.md`
and shipped from that instead: `assaywatch/lineage.py`, `lineage_report.py`, the
`lineage:` config block, Phase 1 reporting (`780df17`) and Phase 2 wiring
(`1d9d964`). The shipped design diverged from the PR deliberately —
Benjamini-Hochberg rather than Bonferroni, a `mechanism` column in
`docs/validation-cases.tsv` rather than the PR's `lineage` column, taxid rolled
up to species rather than the PR's "every node", and no `drift.subgroup` block.
Nothing on main references the PR's doc, and its `docs/RESUME-HERE.md` hunk is
pure staleness now ("last full run 2026-10-15", "catches 1 of 12").

So the PR is closed. Three things in it are **not** recorded anywhere on main,
and this file is where they go so they are not rediscovered from scratch.

## 1. The GenBank-availability ceiling: the honest score may be 9, not 11

**ANSWERED 2026-10-24: it is 11.** KM610046, the fusiform-lineage mitogenome Lotta 2019
draws the HaemR2L mismatch on, was public from 2014-12-24 and the screen calls it `fail`.
`docs/journal/2026-10-24-genbank-ceiling.md`. The paragraphs below are kept as the question as posed.

main's only "ceiling" language is the **taxid-resolution** ceiling
(`docs/journal/2026-10-18-recalibration.md`) — how many cases lineage grouping could
reach given how NCBI labels records. The PR named a different and harder limit:

> "the three *Leucocytozoon* rows may be **uncatchable by any in-silico method**:
> Lotta 2019 found the missed species by whole-mitogenome amplification, and if
> their cyt b sequences were not in GenBank before the 2016-12-31 cutoff, no tool
> screening GenBank could have seen them. Those rows would then be a statement
> about GenBank, and the honest ceiling is 9 of 12, not 12."

Carried over to the current case file, which has **11** `fails` rows, two of them
the Hellgren pair at 2016-12-31 (`Pan_hemoparasite_cytochrome_c_Hellgren_2004`,
`Leucocytozoon_cyt_c_Hellgren_2004`) — the PR's third row has since been dropped
or renamed. If the reading holds, **the ceiling is 9 of 11, and every "N of 11"
figure in the project is being quoted against a denominator that cannot be
reached.** That is checkable with no network: the archives carry deposition
dates, so "are there pre-2016-12-31 records of the fusiform-gametocyte species at
all" is a local query. It was Phase 0's go/no-go and it was never run.

**What this does and does not bear on.** It bounds *lineage-conditional*
recovery — whether the tool can name the specific missed lineage. It does **not**
weaken the pooled coverage call that the M1 revert was measured against: pre-M1
the tool read `Leucocytozoon_cyt_c_Hellgren_2004` @2016-12-31 as `low coverage`
on the records it did have, which is a real catch of a real signal
(`docs/journal/2026-10-22-M1-tier2.md`). The two claims are about different estimands.

## 2. Footprint groups as lineage units (the PR's source B)

main groups only by taxonomy. The PR's second label source is not implemented
anywhere and is the one that needs no external labels:

> "The screen already writes each record's footprint (the mismatch pattern at
> every oligo site, `drift.footprint_signature`). Records that share a
> primer-site variant share a footprint. Grouping by footprint sees a lineage
> defined by the very bases that matter, with no external labels: the *E. coli*
> malB case is one footprint of 92 failures."

Its two stated weaknesses are the useful part, because they are what a taxonomy
grouping does not have to think about:

- a sequencing error is a footprint of its own (the reason equal weighting was
  rejected in review 3.3);
- a record whose sites were not found at all (`no_site`, `diverged`) has **no
  footprint**, so the most divergent lineages — exactly the ones a coverage gap
  is about — are invisible to it. The PR's answer was to report the per-unit
  `no_site`/`diverged` exclusion share alongside each unit, so a unit's
  denominator discloses what it dropped. main's taxonomy grouping has no
  equivalent disclosure.

The PR's own per-case reading of which source could catch which failure (its
table of 12) is worth re-reading before building either: it expected taxonomy
alone to reach 3 or 4 of 12, footprints to add the Bd and influenza shapes, and
clustering to be needed for the rest.

## 3. The open decision: do `partial` rows count as successes?

> **Settled 2026-10-27: yes, scored separately.** A named `partial` gap counts as a
> catch, reported on its own line in `scripts/retrospective.py`'s summary and never
> pooled into the `fails` numerator, which is the paper's main figure. The text below is
> the question as it stood.

Of the three decisions the PR asked for, two were settled on main without
reference to it — intended scope per assay became `scope_taxids` plus
`docs/journal/2026-10-20-scope-curation.md`, and "which ranks count as units" was settled
de facto by `lineage.group_at_rank: species`. The third is still open:

> "**Whether `partial` rows count as successes when the tool names their gap.**
> I'd say yes, and score them separately from `fails` so the two are not mixed."

`scripts/retrospective.py` currently reports `partial` in its own cells
(2 agrees / 2 DISAGREES / 1 weaker / 1 undecided of 6 as of 2026-10-22) and the
headline number quotes `fails` only, which is the "scored separately" half of
that answer but not a decision about whether a named `partial` gap counts as a
catch. It decides what the paper's main figure claims, so it wants settling
before the figure is drawn.
