# Wave 5: the memory hazard, and two things deliberately not done (2026-10-23)

Plan items 5.16 and 5.17.

## Done

**`assaywatch/calls.py`.** `read_calls`, `read_dates`, `read_years` and
`key_calls_by_accession` moved out of `report.py`, which was the project's calls-table
I/O library as well as its renderer — `sitedrift.py` and `scripts/retrospective.py` both
imported them from there. `report.py` re-exports them, where six test files and both
callers already look. 1,834 lines → 1,738 + 130. Same move, same reason, as
`interval.py` and `signature.py`.

**Memory declared where it is actually spent.** `read_calls` materialises 2,688,879 rows
as one dict each, roughly 1–1.5 GB resident after the interning its docstring describes
(an earlier version kept every column and took 3.6 GB). **Three** rules load it —
`report`, `site_drift`, `lineage_analysis` — and only `screen_archive` and `figures`
declared any resources at all. Snakemake can co-schedule `report` and `site_drift` under
`--cores`, so two 1.5 GB resident sets could land together; on SLURM, where `resources:`
becomes the sbatch request, an undeclared job is killed rather than slowed. All three now
declare `mem_mb=3000`, sized at measured peak plus headroom, since the table scales as
assays × records.

**Worker-init contracts are no longer `assert`.** `screen._screen_batch` and
`windows._cut_batch` asserted their `Pool` initialiser had run. `python -O` strips
asserts, and the resulting `AttributeError` on `None` surfaces inside a multiprocessing
worker, which is the hardest place to trace a failure. Both raise `RuntimeError` now.

**`drift.py` raises `ValueError`, not `SystemExit`.** Four sites. It has four importers
and no `__main__`, so exiting the process over a config value was a library deciding
something only its caller can — `score.load_config` already does this correctly. Five
test expectations updated. The rule, now applied consistently across the package: a bad
**value** is a `ValueError`; a missing **environment** (no config file, no optional
dependency) is a `SystemExit` whose message is instructions.

**The `lineage` extra now fails with instructions.** Without scipy and statsmodels,
`worst_lineage_verdict` raised a bare `ImportError` from an inner import. It now names
the extra and the install command, and says why the dependency is optional.

**`prune .claude` in `MANIFEST.in`.** `.claude/settings.json` is committed and hardcodes
one machine's miniforge path; it was shipping in the sdist.

**CI matrix over OS and Python.** `requires-python` says `>=3.11` and only 3.12 was ever
run; the primary development machine is macOS arm64, which nothing tested — and README
notes primer3-py cannot be pip-built there, so the platform most likely to break was the
one never checked. Now `{ubuntu-latest, macos-latest} × {3.11, 3.12}`.

**Neither new axis has ever been executed.** The source parses clean under
`ast.parse(..., feature_version=(3, 11))` with no 3.12-only stdlib, which is evidence and
not proof: a dependency or a runtime behaviour could still differ. The first run may be
red, and that is the matrix doing its job — the same argument the Snakemake job's own
comment makes for having removed `continue-on-error`.

## Not done, deliberately

**The `assemblies.py` ↔ `retrieve.py` circular import stays.** `assemblies.py` imports
`TaxonRun`, `archive_stem`, `last_run_date` and `load_manifest` from `retrieve.py`;
`retrieve.py` imports `AssemblyError`, `datasets_transport` and `retrieve_assemblies`
back. Both are inside function bodies, so only Python's laziness prevents an
`ImportError`. The audit called it the one structural defect worth fixing, and it is —
but not in this session:

- the seven symbols to move include **`write_manifest`**, the atomic writer for the
  retrieval manifest. That manifest is the state that makes 8.6 GB of archives
  interpretable, and the archives are not reproducible on request (retrieval is
  incremental by `mdat`);
- I cannot exercise the live retrieval path — that means fetching from NCBI, which is not
  something to start unprompted — so the test suite's canned responses would be the only
  check on a change to manifest I/O;
- the defect is currently **harmless**: zero functional impact, no bug reported, purely
  structural.

Refactoring irreplaceable-state code that cannot be tested end to end, for cleanliness,
is a bad trade. The extraction is mapped so it is mechanical for someone who can run a
retrieval afterwards:

> New module `assaywatch/archive.py` takes, in this order, `TaxonRun` (with its
> `@dataclass` decorator — a plain `ast` lineno excludes decorators, which is the first
> way to get this wrong), `manifest_path`, `load_manifest`, `last_run_date`,
> `write_manifest`, `record_run`, `archive_stem`. ~55 lines. Their only dependencies on
> `retrieve.py` internals are `manifest_path` and `write_manifest`, which come along, so
> the new module imports nothing from either caller. Then both import from it, one
> direction, and `retrieve.py` re-exports the names for `scripts/rebuild_manifest.py`.
> Verify with `pytest -q tests/test_retrieve.py` **and one live `--dry-run` retrieval**
> before trusting it.

**`logging` is still absent.** 38 `print()` calls across 12 modules, zero
`import logging` in the package — for a pipeline whose documented failure mode is a
multi-hour stall. The plan listed it among "smaller" items and it is not: it is a wide
diff across every module, it changes what every CLI writes to stdout, and several of
those modules write TSVs to stdout where a stray log line would corrupt the output. It
needs its own pass, deciding per module what is data and what is diagnostics.
`assaywatch/timing.py` (501 lines of heartbeat and progress reporting) exists partly
because this gap was worked around rather than closed.
