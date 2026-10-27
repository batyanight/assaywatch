# Phase 2 Handoff: Lineage-Conditional Verdict Wiring

**Date:** 2026-10-18  
**Branch:** main (uncommitted — changes in working tree)

## What was done

Phase 2 of the lineage-conditional estimand: wired `worst_lineage_verdict()` from
`assaywatch/lineage.py` into `drift.py` so that an assay's pooled "stable" or "watch"
status is overridden to "declining" when its worst assessable lineage is significantly
below the detection threshold (one-sided binomial test with Benjamini-Hochberg FDR
correction across lineages).

### Files changed (uncommitted)

**assaywatch/drift.py** — the main work:
- Added imports: `LineageStats`, `per_lineage_stats`, `worst_lineage_verdict` from lineage module
- Added 6 fields to `AssayDrift` dataclass: `lineage_stats`, `lineage_verdict`,
  `lineage_coverage`, `lineage_override`, `status_pooled` (all default None/False)
- New `_lineage_check()` method (~50 lines): runs per-lineage analysis after `finalise()`,
  overrides status when worst lineage is failing but pooled says stable/watch
- Modified `assess()`: new optional params `taxids: dict[str,int]|None` and
  `taxa_cache: dict[int,str]|None`; collects raw rows per assay; calls `_lineage_check()`
  after finalise when taxids are provided

**assaywatch/report.py** — `build()` function:
- Loads taxid sidecar + archive metadata → builds accession→taxid mapping
- Loads taxa_cache from config path
- Passes both to `drift.assess()`

**tests/test_drift.py** — 6 new tests:
- `test_lineage_override_stable_to_declining` — pooled stable, worst lineage failing → declining
- `test_lineage_no_override_when_all_detecting` — all lineages fine → stays stable
- `test_lineage_no_override_when_already_declining` — already declining → no override
- `test_lineage_below_floor_ignored` — lineages < min_records excluded from stats
- `test_lineage_fields_absent_without_taxids` — no taxid data → fields stay None
- `test_lineage_coverage_fraction` — coverage = assessable records / total evaluable

### Test results

1199 passed, 11 skipped. Ruff clean on changed files. Pre-existing lint issues
in lineage.py, lineage_report.py, backfill_taxids.py, timing.py, test_lineage.py
(from phase 1) are untouched.

## What remains

1. **Report rendering** — add lineage-override indicator to the drift table in
   `render_markdown()` and `render_html()` (both in report.py). When `a.lineage_override`
   is True, show that the status was overridden from `a.status_pooled`. Could be a simple
   note column or a parenthetical.

2. **Commit and push** — all changes are in the working tree, not committed.

3. **Backfill taxids** — the pipeline needs `scripts/backfill_taxids.py` to have been run
   on the local machine (requires NCBI network access). Without backfill, all lineages show
   as "unresolved" and no overrides happen.

4. **Recalibrate** — step 6 of the estimand plan. Run the pipeline with taxid data and
   measure how many of the 12 documented failures are now caught. Adjust thresholds in
   config.yaml if needed.

## Design decisions (settled)

- Override is ONE-DIRECTION only: pooled stable/watch → declining. Never upgrades.
- The `status not in ("declining", "low coverage")` guard means a pooled-declining assay
  is not touched by the lineage check.
- `lineage_coverage` measures what fraction of recent evaluable records sit in assessable
  lineages (those with ≥ min_records_per_lineage). Low coverage means the lineage verdict
  is weak.
- taxids dict is keyed by unversioned accession (from sidecar); the assess() code tries
  both versioned and unversioned lookups.
