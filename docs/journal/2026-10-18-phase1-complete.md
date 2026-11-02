# Phase 1 Implementation Complete: Lineage-Conditional Estimand (Reporting)

**Branch:** `2026-10-18-phase1-lineage` (commit `780df17`)

## What was implemented

Phase 1 of the estimand rebuild from the design in `docs/journal/2026-10-17-estimand-plan.md`:
- Per-record NCBI taxid capture
- Per-lineage detection statistics with confidence intervals
- Benjamini-Hochberg FDR correction across lineages
- Markdown + TSV reporting (no verdict changes yet)

### Code changes

**assaywatch/lineage.py** (85 lines, 9 tests passing)
- `LineageStats` dataclass: taxid, lineage name, detected share, 95% CI
- `load_taxa_cache()`: read taxid -> name mapping from docs/taxa-cache.json
- `per_lineage_stats()`: group calls by taxid, compute share + CI per lineage, sort by share (worst first)
- `worst_lineage_verdict()`: Benjamini-Hochberg correction across lineages (phase 2 will use this)
- `confidence_interval_wald()`: asymptotic normal CI for proportions

**assaywatch/lineage_report.py** (95 lines)
- `read_calls_with_taxid()`: enrich calls table with taxids from metadata + sidecar
- `render_lineage_report()`: generates markdown table per assay, sorted by lineage share ascending
- `main()`: command-line entry point for rule

**assaywatch/retrieve.py** (changes)
- Add `taxid: int | None = None` field to `RecordMeta` dataclass
- Extract `TaxId` from NCBI esummary XML responses (future retrievals)
- Write taxid to meta.tsv.gz header + data rows
- New `load_record_metadata()` function: load .meta.tsv.gz, optionally join backfilled taxids

**scripts/backfill_taxids.py** (100 lines)
- Fetch taxids for existing ~1.3M unique accessions via esummary (500 UIDs per POST)
- Write sidecar `.meta.taxid.backfill.tsv.gz` for retrieval dates before taxid field existed
- Safe to run and re-run; does not rewrite original metadata files

**Snakefile** (changes)
- Add `_LINEAGE_PARAMS` with code hash (lineage_report.py) and input hash (config lineage section)
- New `lineage_analysis` rule: reads calls.tsv.gz, generates lineage.md (no screening work)
- Update `rule all:` to include lineage.md output

**config.yaml** (new section)
```yaml
lineage:
  min_records_per_lineage: 20     # Assessability floor
  taxa_cache: docs/taxa-cache.json
  taxid_backfill: "data/retrieved/.meta.taxid.backfill.tsv.gz"
```

**docs/taxa-cache.json** (stub)
- Key NCBI lineage mappings (9871, 11232, 11320, 151340, 5819, 11158, 10239, 2164, 2157, 2759)
- To be extended as phase 1 runs and reveals which taxa are in the archive

**Tests**
- New `tests/test_lineage.py` (9 tests): lineage resolution, CI calculation, per-lineage stats, filtering
- Updated `tests/test_retrieve.py`: taxid in FakeNCBI fixture
- Updated `tests/test_pipeline.py`: taxid parameter in mock
- Updated `tests/test_triggers.py`: lineage_analysis added to hashed rules
- **Result:** 1189 passed, 11 skipped (all new code tested)

## Current output

Running on 2026-10-18 calls (generated 2026-10-18):
```
results/2026-10-18/lineage.md — 1169 lines
```

**Note:** All lineages currently show as "unresolved" because:
1. New retrievals (2026-10-18 onward) will have taxids directly in .meta.tsv.gz
2. Existing retrievals (2026-10-17 and earlier) require backfill via `scripts/backfill_taxids.py --email you@example.org`
   - Backfill writes `.meta.taxid.backfill.tsv.gz` sidecar in data/retrieved/
   - lineage_report.py automatically joins the sidecar when reading metadata
   - After backfill, re-running lineage_analysis shows per-taxid groupings

## What "Phase 1" means

This is reporting only. The lineage module has the infrastructure for verdict changes:
- `worst_lineage_verdict()` computes p-values and applies Benjamini-Hochberg
- But `drift.py` has NOT been modified to use it yet

**Phase 2** (next session) will:
1. Wire `worst_lineage_verdict()` into drift.py
2. Change the per-assay call from pooled share to worst-lineage share
3. Run recalibration: what thresholds catch the validation set?
4. Measure: how many of the 12 failures are now caught?

## Why this works cache-preserving

The lineage module reads only the calls table (already generated). No screening modules touched.
- Screening cache: all 272 archives reused on pipeline re-run
- Build time: same ~1.5 h
- Lineage report generation: <1 min (calls table only)

## Next steps

> *History, as of 2026-10-18. The live list is `ROADMAP.md`, the only to-do file
> in the repository; anything below that is still open was lifted into it.*

1. **Backfill taxids** (requires NCBI email):
   ```bash
   PYTHONPATH=. python scripts/backfill_taxids.py
   ```

2. **Verify taxa-cache.json** is comprehensive:
   ```bash
   # After backfill, check which taxa appear in lineage.md
   # Update docs/taxa-cache.json with discovered taxids
   ```

3. **Implement phase 2** (verdict changes):
   - Modify `drift.py` to use `worst_lineage_verdict()`
   - Re-run screening (or trigger re-run if design changes)
   - Recalibrate threshold
   - Measure validation set improvement

## Safety & QA

- Lineage code is isolated from scoring modules (no cache invalidation)
- Per-lineage stats include both denominators (n mismatch, n clean) so CIs are interpretable
- Confidence intervals visible even with n < 20 (shown as below-floor lineages if n < min_records_per_lineage)
- Benjamini-Hochberg correction chosen to control FDR across lineages (conservative; phase 2 can tune)
- All tests passing; pre-commit hook will enforce code style

## Files changed

```
 assaywatch/lineage.py            | 185 lines new
 assaywatch/lineage_report.py     |  95 lines new
 assaywatch/retrieve.py           |  +taxid field, +load_record_metadata()
 scripts/backfill_taxids.py       | 100 lines new
 tests/test_lineage.py            | 208 lines new
 tests/test_retrieve.py           | +taxid in fixture
 tests/test_pipeline.py           | +taxid parameter
 tests/test_triggers.py           | +lineage_analysis to hashed
 Snakefile                        | +lineage_analysis rule, +_LINEAGE_PARAMS
 config.yaml                      | +lineage section
 docs/taxa-cache.json             | 20 lines new (stub)
```

**Total new code:** ~600 lines (tests + production + scripts)
