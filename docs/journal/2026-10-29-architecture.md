# The architecture day: the code moved to fit the engineering principles (2026-10-29)

One session, eleven PRs, every step green on the full gate (default and slow test
suites, the registry validator, the citation check, ruff). The plan and every decision
are in `ROADMAP.md` under "Architecture"; the vocabulary is `GLOSSARY.md`. This is the
record of what each step found that the plan did not expect.

## What changed

- **Glossary.** 98 terms. Seven the scan could not define (tier-2, ground truth,
  evaluable vs assessable, undecided, the C-numbers vs the S-ladder, the retrospective
  families, lineage Modes A/B/C) were all answerable from the repo's own files.
- **Reproducibility.** Two scripts hardcoded the author's laptop path. Of four constants
  the plan wanted in config, only two moved: `THREE_PRIME_ZONE` was a second copy of
  `scoring.primer_3prime_window`, so the site table's 3' marker could have disagreed
  with the scorer; it now reads that key. The master sheet is the assay sheet.
- **Test tiers.** Default `pytest` 168 s -> 43 s; `pytest -m fast` is 235 tests in 5 s.
  Most of the saving was one cache: `load_assay` re-parsed all 214 YAMLs for every
  caller, and a retrospective test paid two seconds each time.
- **Type hints** enforced for the package (29 functions annotated).
- **`registry.py`**: the one door to the entries. `edit()` keeps comments, key order and
  quoting through ruamel.yaml's round-trip mode; four entries carry measurement notes a
  whole-document rewrite would have thrown away.
- **`assaywatch <stage>`**: one command, each stage keeps its parser; 42 call sites.
- **`ncbi.py`**: both transports with injectable HTTP and sleep, one `TaxonRecord` for
  the five parsers that existed, the only writer of the two taxonomy caches. Found: a
  key handed directly to a transport was never scrubbed from its error messages.
  Importing it from `lineage.py` put `credentials.py` into every report rerun; the
  trigger test caught it and the taxa-name reader stayed where it was.
- **`papers.py`**: the literature client six scripts each carried, and `obtain(doi)`,
  the chain curate runs (local file, open full text if longer than an abstract, a free
  PDF, Elsevier with a key, else queue the DOI for a human).
- **`assaywatch curate <entry>`**: eight steps, write-through for `doi_verified`, a
  missing taxid and an unset `amplicon_bp`; TODO for judgement; `status` never touched.
  `printed.py` holds the paper-text functions the verifier script now imports.
- **Scripts.** 34 live scripts run on the modules; `check_submission` is a shim over
  `curate --dry-run`. Twenty one-off analyses moved to `scripts/archive/` with an index
  of what each measured and where the finding is recorded; their tests sit in
  `tests/archive/`, kept and not collected.

## Judgement calls, recorded

- `bench_panel` and `holdout` are archived although the open scoring test plan quotes
  their numbers; two package tests still load them from the archive.
- Five scripts stayed live by judgement, not by the caller rule: the roadmap's open work
  or the resume point names them.
- `5g` (one section list behind the two report renderers) was verified and not done:
  the renderers share no code and the HTML one carries widgets Markdown cannot.
- The two report renderers, the package layout (no stage subpackages) and the Snakefile's
  eight rules are unchanged.

## What this day could not do

- GitHub Actions ran nothing all day: every run, including the morning's, reports that
  the account's Actions billing has failed. The gate ran locally on every commit.
- `conda-lock.yml` was regenerated at the end of the day for the one new dependency
  (`ruamel.yaml`), with `conda-lock` installed into the env for it.
