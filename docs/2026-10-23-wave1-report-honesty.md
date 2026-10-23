# Wave 1: the report now says what its code does (2026-10-23)

Wave 1 of the plan of attack. Every change here is a correctness fix to what the
report **says**, measured against the frozen baseline in
`docs/2026-10-23-baseline.md`. None is a recalibration.

## Measured, baseline -> wave 1

Same frozen calls table (`results/baseline-2026-10-22/calls.tsv.gz`), regenerated with
`python -m assaywatch.report` and `python -m assaywatch.lineage_report`. No rescreen:
every change is inside the report rules' import closure (`Snakefile:217-241`).

| | baseline | wave 1 |
|---|---:|---:|
| zero-width intervals in `report.md` | 3 | **0** |
| zero-width intervals in `lineage.md`, at 0% | 237 | **0** |
| zero-width intervals in `lineage.md`, at 100% | 467 | **0** |
| assays given a status the registry says cannot be one | 19 | **0** |
| flagged assays the duplication check "could not check" | 7 | **0** |
| override notes saying "detects only" of a lineage at or above the pool | 6 | **0** |
| override notes carrying the lineage's own earlier share | 0 | 13 |
| notes running two sentences together | 3 | **0** |
| bare `taxid_` labels in `lineage.md` (of 1,512 rows) | 1,336 | 889 |

**704 of the 1,512 per-lineage intervals were zero-width.** Nearly half the lineage
table claimed certainty, all of it from `lineage.py:236`'s Wald interval. The report
header said "Intervals are Wilson 95%" throughout.

Statuses, scored assays only: **37 declining, 37 low coverage, 13 watch, 32
insufficient data, 14 no recent data, 52 stable**, plus **19 not scoreable** — 204 in
all, as before. The duplication line is now "21 of 74 flagged assays still hold", where
it was "33 of 72 ... (7 could not be checked)": every flag now gets a verdict, and the
ones that had escaped the check were overwhelmingly ones that fail it.

## The tier-2 matrix did not move, and that is the right answer

```
python scripts/retrospective.py --cases docs/validation-cases.tsv \
    --calls results/baseline-2026-10-22/calls.tsv.gz --renames docs/rename-mapping.tsv
```

Identical to the baseline, row for row. Expected, and worth saying why, because it
would be easy to read as "wave 1 did nothing":

- `retrospective.py` goes through `drift.assess`, and nothing in wave 1 changes a
  status there. The lineage **verdict** is a binomial test; the interval never entered
  it. The duplication verdict is documented as never gating a flag. Note text is text.
- The not-scoreable quarantine lives in the report layer, which the harness does not
  read.

So wave 1 changed what a reader is told, not what the tool decides. PPV of `declining`
is still **2/9**. That is the job of waves 2 and 3.

## The Usutu correction

`docs/2026-10-23-baseline.md` first called the `Pan_flavivirus` Usutu alarm "a Wald
artefact, not a finding". Wave 1 showed that half wrong, and the baseline doc now says
so. With Wilson the row reads:

> lineage Orthoflavivirus usutuense (3048443) (428 records) detects only 0.0%
> (0.0%-0.9%), down from 12.0% on 592 earlier records

The interval was the artefact. The alarm is not: the screen finds this assay matching
almost no Usutu record in any period, while the MediLabSecure EQA in
`docs/validation-cases.tsv` records the reference lab detecting Usutu with it. That is a
disagreement between the **scoring** and the **bench**, and it goes to wave 2 and to
`docs/bayesian-scoring-plan.md` C2 as a lead.

## What changed, item by item

**1.1 / 1.2 — one estimator.** `assaywatch/interval.py` is new and holds `Z95`,
`wilson_interval` and `newcombe_difference`, moved out of `drift.py`. They lived above
`lineage.py` in the layering, so the lineage code could not import them and grew its own
Wald interval. Same move, same reason, as `signature.py`. `drift.py` re-exports both, so
`drift.wilson_interval` still works for `figures.py`, the tests and `scripts/`.
`lineage.confidence_interval` now delegates to it. The test that let Wald through
(`upper < 0.1` for 0/100, which zero width passes) is joined by one asserting non-zero
width at both extremes and one pinning the lineage interval to drift's — both written
first, and both failed against the old code.

One numerical fix fell out: `wilson_interval(0, n)` returned a lower bound of ~3.5e-18
rather than 0, a residue of `centre - half`. It now returns the analytic 0 (and 1 at
k = n), which is what statsmodels' reference implementation returns and what
`tests/test_drift.py` holds it to.

**1.3 — the report reads `needs_review`.** It read it nowhere. An assay with an OPEN
review question, `not_screenable` or `do_not_use` now goes to a **Not scoreable**
section with its flag and note, and gets no status — including the one it would have
had, following the convention the nested table already set. 19 held out, among them the
three the audit named: `LMBV_dsDNA_MCP_RPA_Li_2025` (was Stable, 100.0% on an RPA assay),
`ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997` (was Declining on a digest readout) and
`Pan_mycoplasma_16S_All_Van_1992` (was Low Coverage, carrying `do_not_use`). Recorded
caveats are deliberately not held out — 149 of 208 entries carry one — and are printed
in the note column instead as `Entry flags: ...`.

Held-out rounds still appear in the nested table, since those shares are coverage and
not a verdict, but are now marked `(not scoreable)` there too. Making that work exposed a
second decider: the HTML nested table read `ReportModel.nested_rows` while the markdown
one rebuilt its own, so a fact added to the model reached one report and not the other.
`nested_section` now takes the model's rows.

**1.4 — decided at the report, not the screen.** A `not_screenable` entry is still
screened. Its calls feed the nested, degeneracy and per-lineage tables, and the call
table stays a complete record of what was run. What it never gets is a status, and a
test asserts that.

**1.6 — the duplication check sees overridden flags.** `_cluster_check` ran inside
`finalise()`, before `_lineage_check` could change the status, so every lineage override
had been asked the question while it still read `stable`. The verdict half is now
`_cluster_verdict`, idempotent, and re-run after the lineage check.

**1.7 — the duplication verdict is in the row.** A `duplication` column: `holds`,
`fails: <tests>`, or `unchecked`. Of the 37 declining rows: 11 hold, and 15 fail on the
change interval alone.

**1.8 — the override note is a true sentence.** It prints the firing lineage's own
earlier share ("down from 12.0% on 592 earlier records"), and "only" is used only when
the lineage is actually below the pool.

**1.9 — the draft line.** "A draft entry has been checked for structure and valid IUPAC
oligos only — not for a verified citation, taxid or submitter" was false for 173 of the
205 drafts. It now says `draft` is a maintainer sign-off and counts how many drafts
already meet every mechanical requirement, through a new `Assay.missing_for_active` that
the validator itself now uses, so the report cannot describe a different rule from the
one enforced.

**1.10 — text.** Note fragments are terminated where they are joined. `lineage.md`
resolves taxids through `name_lineages_from_taxonomy`, as `report.md` already did.

## Two deliberate departures from the plan

**1.5: the header was rewritten; the override was not made to pass the pooled tests.**
The plan recommended the second. On reading `_lineage_check` that turns out to be wrong
as stated: requiring the **pooled** upper bound to fall below the threshold would stop a
lineage ever flagging a healthy pool, which is the entire purpose of measuring per
lineage. The defensible version applies the equivalent tests to the **lineage's own**
numbers — its recent interval, its own Newcombe change interval, its own
`min_decline`. That changes statuses, so it belongs in wave 3 where it can be measured
against tier-2, not in a wave whose rule is "change what is said, not what is decided".
Meanwhile the header now says what the code does: Wilson throughout, a pooled flag
needs the pooled upper bound below threshold, a lineage can flag a pool that clears it,
the lineage rule is a looser binomial test BH-adjusted within the assay, and nothing
controls error across assays.

**1.7: a column, not a separate section.** The plan offered moving the failing flags
out of Declining. `_cluster_check`'s own docstring rules that out: the footprint
reduction "is never used to flag or to clear anything", because a sequencing error in a
primer site is a footprint of its own. Moving rows would make the check a gate it is
documented not to be. Showing the verdict beside the flag is the honest version.

## Still open from wave 1's territory

- **889 lineages are still `taxid_<n>`.** `name_lineages_from_taxonomy` names only what
  the taxonomy cache holds. The rest need `scripts/build_taxonomy_cache.py` rerun or an
  NCBI lookup — a data task.
- The 6 `declining` rows whose note ends "a coverage gap, not drift", and the 12
  degeneracy-severe assays leading the report, are wave 5.6 (triage), not wave 1.
  Neither is a wrong status: the first are sound pooled calls whose note describes a
  LINEAGE (see the correction in `docs/2026-10-23-baseline.md`), and degeneracy is
  reported beside a verdict and never folded into one, by the convention README states.
  Both are reasons an assay should not LEAD the report, which is a triage question.
