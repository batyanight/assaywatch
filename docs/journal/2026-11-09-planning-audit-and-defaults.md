# The planning documents audited, and five stale defaults the fallback test could not see (2026-11-09)

Asked for: an audit of `ROADMAP.md`, `docs/RESUME-HERE.md` and the project's structure, then action on the
structural findings. Branch `roadmap-audit`, off `next-release`.

## What the planning documents had drifted on

Four items sat twice in the roadmap (page narrative, per-assay cuts, species synonyms, the rereads), and two of
the older copies were still open after merged PRs had finished them. The resume point called `scope-reread-fixes`
an open PR a day after PR #13 merged it. Document counts were stale in four files and one journal was unindexed.
Step 12 named one conflicting file where there are three. PR #14 targets `main` against the plan's merge rule.
All corrected in the first commit on this branch; PR #14 is left for the maintainer.

## The worktree was testing the wrong package

`pytest` in `../assaywatch-pages` imported `assaywatch` from the editable install, which points at the main
checkout, so `page-narrative`'s own tests failed against another branch's code. `pythonpath = ["."]` in
`pyproject.toml` pins each checkout to itself. Every gate run from a worktree before this tested the main checkout.

## Five defaults had drifted from config.yaml, in the unsafe direction, and the pin could not see them

`settings.py` pins every `cfg.get("key", literal)` to the model by a grep over the AST. A dataclass field or
keyword default that mirrors a key under another name is the same hazard and was invisible to it:
`AssayDrift.min_records` said 20 (config 15), `AssayDrift.min_decline` 0.0 (config 0.05, the value the settings
docstring itself calls the unsafe one), `per_lineage_stats` and `render_lineage_report` `min_records` 20 (config
30), and `sitedrift.analyse_assay` `cover` 1.0 (config 0.95). None was reachable in a run, since every stage
builds these through `from_config`; all were reachable from a test or a script that builds the object bare.
`tests/test_settings.py::test_every_dataclass_and_signature_default_matches_the_model` now holds an alias table
of 28 mirrors, and the five read the model (`Drift().min_decline` and so on, the idiom `lineage_report` already
used for `thin_of_best`). The default suite and the slow tests pass unchanged, so no test had leaned on a stale value.

## One archive scan instead of four

`lineage_report`, `composition_build` and `report` each walked `*.meta.tsv.gz` with their own header-index loop;
`metadata.py` had the same loop twice more. `metadata.read_column(retrieved, column, wanted=None, *, files=None)`
is now the one reader: bare accession keys, archives without the column skipped, first value wins (as
`read_titles` always did; the two taxid loops were last-wins, which differs only where one accession carries two
taxids in two archives, and none does). `lineage_report` now reads `created` and `taxid` in two passes where it
read both in one; the rule is a diagnostic and the second pass is seconds. `lineage.read_taxid_backfill`'s header
check stays as it is, since it is a guard and not a read.

## Left as proposals on the roadmap (Architecture, step 6)

The per-lineage concept spread over `lineage`, `lineage_report` and `drift._lineage_check`; `report.py` at 3,000
lines; three `pct` helpers with different dashes and rounding; `gapped.py` with no caller in the package.
