# scripts/archive/

One-off analyses whose finding is recorded. Decided 2026-10-29 (ROADMAP, "Architecture"):
a script that answered a question on a date is a record, like a journal entry. Once its
finding is in `ROADMAP.md` or a journal it lives here, untested, and git keeps the exact
version that produced the number. Go back to one when a question reopens; run it from the
repo root (`python scripts/archive/<name>.py --help`), as before.

What stays in `scripts/` is a tool: something the pipeline, CI, pre-commit, the weekly run,
the curation workflow or the roadmap's open work calls.

Their dedicated tests moved to `tests/archive/` and are not collected (`norecursedirs` in
`pyproject.toml`); they passed on 2026-10-29. Two package tests still load `bench_panel.py`
and `holdout.py` from here, because they test package behaviour through them.

| script | what it measured | where the finding is recorded |
|---|---|---|
| `annotate_orientation.py` | Write the archive's answer into each `orientation_inferred` flag's note. | journal/2026-10-19-* (orientation notes); 28 entries annotated |
| `audit_provenance.py` | Audit the registry for provenance problems: does each citation DESIGN its oligos? | journal/2026-10-04-provenance-audit.md, 2026-10-05-verification-handoff.md |
| `c1_intervals.py` | C1, part one: every per-lineage interval in a lineage report, three ways. | journal/2026-10-27-c1-posterior-flag-rule.md |
| `check_primer_provenance.py` | Does the cited paper DESIGN its primers, or did it get them elsewhere? | journal/2026-10-04-provenance-audit.md |
| `compare_thermo.py` | A thermodynamic predictor and the shipped penalty rule on the SAME wet-lab rows. | journal/2026-10-27-thermo-vs-penalty-paired.md, 2026-10-27-tntblast-head-to-head.md |
| `extract_candidate_oligos.py` | Pull candidate oligos out of downloaded papers for curation. | journal/2026-10-05-list2-worklist.md |
| `fit_panel_thresholds.py` | Fit `scoring.engine: serial`'s two thresholds on the bench panels. | journal/2026-10-26-s1-serial-killed.md (S1 killed) |
| `measure_amplicon_lengths.py` | Amplicon length against the assay's declared size. | journal/2026-10-14-amplicon-sizes-measured.md |
| `measure_locus_identity.py` | Is a questionable amplicon the assay's locus at all? | journal/2026-10-25-locus-identity-design.md |
| `measure_site_level.py` | How much evidence the amplicon-level rule discards. | journal/2026-10-26-bd-phase1-site-level-measured.md |
| `orphan_archives.py` | Retrieval archives that no live assay asks for any more. | journal/2026-10-24-orphan-archives.md |
| `rescore.py` | Replay a scoring strategy over a calls table instead of paying for a rescreen. | journal/2026-10-24-scoring-strategy-test-plan.md and the S-ladder journals |
| `retire_merged_taxids.py` | Move an entry off a taxid NCBI has merged away. | journal/2026-10-27-retired-taxids.md |
| `tntblast_arm.py` | Run TNTBLAST over the bench panels and record its melting temperatures. | journal/2026-10-27-tntblast-head-to-head.md |
| `window_grid.py` | The drift window and the record minimum, priced TOGETHER. | journal/2026-10-27-window-minimum-grid.md; ROADMAP (Done) |
| `verify_predict_supplement.py` | Check every PREDICT-panel entry against the supplement its oligos were read from. | journal/2026-10-05-sequence-verification.md (74/74 exact) |
| `build_locus_references.py` | Build each assay's locus reference from the amplicons it detects. | journal/2026-10-25-locus-identity-design.md |
| `diff_printed_oligos.py` | Did a change to the oligo reader change what it finds in real papers? | journal/2026-10-20-scope-curation.md |
| `bench_panel.py` | Score one assay on a bench panel; the mispair behind each 3'-window mismatch. | journal/2026-10-19-fap-bench-panel.md, 2026-10-20-meyer-ati-bench-panel.md; the S-ladder journals (bench accuracy) |
| `holdout.py` | How much of tier-2 performance is the thresholds having seen tier-2. | journal/2026-10-23-wave4-holdout.md, 2026-10-26-c3-intervals-and-holdout-drift.md |
