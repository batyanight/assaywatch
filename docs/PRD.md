# AssayWatch: product requirements (retroactive, 2026-11-06)

Records decisions already made; it adds none. Written from the repository's committed state, then reviewed with
the maintainer. **Tags:** `[C]` = checked against code, config, Snakefile or `assaywatch validate registry`
output. `[I]` = taken from README/ROADMAP/docs prose and not re-checked. **No tag = confirmed by the maintainer
on 2026-11-06.** Counts are from the validator that day; ROADMAP is the only to-do list.

## 1. Problem and research question
- Published PCR/qPCR assays are designed against the sequences available at the time, then used for years while
  GenBank accumulates strains nobody re-screens them against. A failed reaction reads as "pathogen absent". [I]
- Question: does the share of an assay's target records that its oligos still match fall over time, by deposit
  year, and which lineages are escaping? The answer tells labs how useful a test still is.
- Contribution: the curated, citation-verified registry and the deposit-year axis. The screening engine is the
  means. [I]

## 2. Intended users and use cases
- Primary user: a diagnostic or surveillance lab deciding whether to trust, or redesign, a published assay.
- Also: the maintainer (sole curator), outside contributors (`CONTRIBUTING.md`), and readers of the site and of
  `report.md` / `site-drift.md` (which base to order at a drifted primer position). [I]

## 3. Inputs
- **Registry:** one YAML per assay in `registry/`, validated by `schema.py`, unknown keys rejected. 216 entries:
  177 `active`, 38 `draft`, 1 `deprecated`; 153 conventional, 39 hydrolysis_probe, 21 mgb, 2 sybr, 1 rpa;
  60 with a probe. [C]
- **`draft`** = data incomplete or not yet reviewed by the maintainer. Drafts are screened and shown, labelled as
  such. `active` = reviewed, set only by the maintainer. [C: validator] Pending entries (no verified DOI) sit in
  `pending/` and are never screened. [C]
- **GenBank records**, fetched from NCBI per retrieval group (taxid + optional query), archived, incremental;
  bacterial targets can use sampled genome assemblies. [C]
- **Citations:** Crossref approves DOIs; Unpaywall/OpenAlex/Europe PMC supply papers. [I]
- **Config:** `config.yaml`; every threshold carries its justification or the admission there is none. [C]
- **Evidence:** `docs/validation-cases*.tsv` (development set + 3 held-out), `docs/bench-panels/`. [C]

## 4. Outputs
- Per run, `results/<date>/` (gitignored): `calls.tsv.gz`, `report.md/.html`, `site-drift.md/.tsv`, `lineage.md`,
  `degeneracy.tsv`, `figures/`; also RefSeq-twin map, retrieval coverage, composition. [C: Snakefile]
- Per-assay status: `stable`, `watch`, `declining`, `low coverage`, `insufficient data`, `no recent data` (and
  internal `no data`); some entries get none (`not_screenable`, `do_not_use`). [C: `drift.py`, `review.py`]
- Static site (`website/`), deployed by `site.yml` from `main`. Shows the latest run; not a live feed. [C]

## 5. Core workflow
`validate` -> `retrieve` (checkpoint) -> `screen_archive` (cached per archive) -> `collect_calls` ->
`refseq_twins` -> `report` (drift inside) -> `site_drift`, `lineage_analysis`, `degeneracy_table`, `figures`,
`composition`. [C]
- `match.py` finds sites on both strands; `score.py` sums position-weighted mismatch penalties into a call
  (detect / reduced / fail / indeterminate / no_amplicon). [C]
- **Why a positional penalty table, not thermodynamics:** different scoring rules were tested (the S-ladder) to be
  as accurate or as reasonable as possible; the table won against the bench and retrospective sets. Thresholds
  are still set by hand, so "best" is relative to those sets, not derived. `thermo.py` is reported, never scored,
  shipped off. [C: config]
- **Why deposit date:** it exists for every record, cannot be revised, and is what GenBank surveillance can see at
  a given time. Collection year is a lens only; it moves no status. [C: GLOSSARY]
- `drift.py`: recent window vs pooled baseline, Wilson/Newcombe intervals, detected-share threshold 0.90, minimum
  decline 0.05. [C: config keys]
- **Lineage override (shipped, experimental):** one lineage significantly below threshold after Holm correction
  replaces the assay's verdict. It does change published statuses. "Experimental" means its accuracy is
  unmeasured. [C: `lineage_analysis`, architecture doc]

## 6. Validation
- **Gate:** `pytest -q`, `assaywatch validate registry`, ruff, `check_citations.py`; `pytest -m slow` for
  Snakefile changes. 90 test files, tiny fixtures. [C]
- **Registry correctness:** oligos checked against the cited paper, `amplicon_bp` measured on real records, DOI
  approved only by Crossref. [C: validator; rest I]
- **Retrospective validation (tier-2):** re-run as of a date before a paper reported a failure; classify
  works/fails/partial; undecided statuses tabulated apart. Development set (50 cases, in-sample): 6/11 failures
  caught, `declining` precision 4/10, false alarms 4/32; held-out sets scored worse. One confirming drift case
  (influenza A M1, Ward 2004 vs Yang 2014). [I: quoted, not recomputed]
- **Bench panels:** per-strain wet-lab results used to compare scoring changes. [I]
- **"Done" for a release:** no accuracy bar exists. The frozen run passes the gate, composition cells sum to the
  graph (0 mismatches), and every status move is explained. Statuses ship as "worth looking at" with measured
  precision beside them.

## 7. Goals
- Pathogen assays with a published paper and a Crossref-verified DOI, wildlife and One-Health and human
  clinical alike. [C: validator]
- Screen every live entry (`active` and `draft`) by deposit year; track escaping lineages.
- Scheduled weekly runs. The pause (ROADMAP "Operations") is temporary and ends at v0.3.0 step 15.
- Disclose caveats under the controlled `needs_review` vocabulary. [C]
- Reproducibility: pinned environment, conda-lock, config-driven paths. [C]
- Further sequence sources beyond GenBank (MalAvi, PR2/SILVA, UNITE, GISAID), deferred. Admission test: a source
  must add sequences GenBank lacks; MalAvi was looked at and mostly duplicated GenBank. GISAID needs a licence
  check first.

## 8. Non-goals
- Host barcoding, eDNA, host-ID, internal-control and kingdom-level universal primers. [C: CLAUDE.md]
- ARTIC-style tiled schemes. [I]
- Scoring degeneracy or thermodynamics (reported only). [C]
- Naming any lab or list as an assay source. [C]
- Treating `declining` as proof an assay has failed. [I]

## 9. Open requirements
Per ROADMAP "Release plan: v0.3.0". [I]
- Blockers: query fixes, `assaywatch scope-check`, rule memory declarations, reread of papers behind
  `declining`/`low coverage`, frozen run, publish `next-release` -> `main`, tag v0.3.0.
- Droppable: C1b lens, pathotype assembly filter, validation reads, assay page narrative, synonyms and cuts.
- Post-release: Bayesian per-record model (needs 40 negatives, has 11), non-GenBank sources, `panels`,
  `exclusivity_taxids`, Greene SLURM profile.
- New from this review: validation figures for the lineage override (none exist).

## 10. Glossary (full: `GLOSSARY.md`)
| Term | Meaning here | Clash and preferred use in new writing |
|---|---|---|
| assay | one registry entry: primer pair (+probe), target, citation [C] | none |
| target | `Target` block: taxid, taxon, gene, query [C] | `scope_taxids` narrows it; say "scope" for that |
| call | per-record outcome of screening [C] | none |
| mismatch | oligo/record base difference, scored by position and mispair [C] | none |
| drift | fall over time in the matched share | not a synonym for `declining` (a status) |
| status | per-assay verdict [C] | GLOSSARY lists 5; code has 6 + `no data` |
| flag | drift flag (Wilson/posterior) vs review flag (`needs_review`) [C] | write "drift flag" / "review flag" |
| evaluable | a record with a `detect`, `reduced` or `fail` call | drop the second GLOSSARY sense ("both primers anchored") |
| validate | schema check only | DOI check = "verify"; tier-2 = "retrospective validation" |
| tier-2 | retrospective validation | there is no tier-1; use "retrospective validation" |
| lineage | records grouped by taxid at species rank [C] | composition also says species, cluster, stratum |
| live | in `registry/` with a verified DOI [C] | includes `draft` |

## Open questions
1. Reconcile counts: README 218 (217 screened), validator 216, composition 215; `active` 177 vs 179 in
   `state-of-the-project.md`; docs counts (reference docs, journals) differ across README, INDEX, CLAUDE.md.
2. README says the lineage layer is "only partly built, not yet a contribution"; the code and this PRD say it is
   shipped. README wording needs a decision.
3. README "Layout" is stale (about 19 of 55 modules; "Phase 1").
4. Whether the PRD's preferred terms get written into `GLOSSARY.md` (no code renames either way).
5. The uncommitted edits on `backfill-guard` (`lineage.py`, `report.py`, `config.yaml`) were not read, so the
   lineage and report descriptions may change.
