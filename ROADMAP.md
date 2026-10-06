# Roadmap

Scope for v0.1 is frozen in the build plan; new ideas go here, not into the sprint.

## Phase 0 (current)
- [x] repo, environment.yml, pre-commit, CI
- [x] YAML schema (pydantic) and validator
- [x] registry imported from the WCS spreadsheet (138 pathogen assays; 38 host/barcoding/universal primers excluded as out of scope)
- [ ] 5 assays promoted to `active`: Bd (Boyle 2004) done 2026-10-04 (stable, 100% of 54 recent);
      Bsal (Blooi 2013) and Oo ITS2 (Bohuski 2015) await their rDNA-query data; ranavirus MCP
      (Pallister 2007) and CDV P (Scagliarini 2007) were "watch" at ~88%
- [x] run `scripts/resolve_citations.py` once (2026-10-04): 64 DOIs verified, 21 taxids filled;
      5 BAD DOIs left for review. `scripts/check_taxids.py` found and fixed 3 wrong taxids
- [ ] name, license (MIT code / CC-BY registry), IP question asked in writing

## Phase 1: core pipeline
- [x] `match`: exhaustive vectorised search, both strands, held to brute force in tests
- [x] `score`: position-weighted penalty from config.yaml, five-way call per record
- [x] three-state base comparison: degeneracy and undetermined record bases cost nothing
- [x] inosine handled as a single promiscuous molecule, not as N
- [x] degeneracy accounting reported next to the drift signal, never scored
- [x] `screen` CLI: assays x FASTA -> TSV of calls
- [x] synthetic fixture set with hand-derived expected calls (61 records, 5 assays)
- [x] `retrieve`: Entrez esearch/esummary/efetch per taxid, mdat-filtered, gzip archive + manifest
- [x] wire the stages into a Snakefile with a checkpoint; SLURM profile
- [x] first live NCBI dry run (2026-10-03): 28 taxa fetchable whole, 19 needed gene-targeted queries
- [x] first live fetch (2026-10-03): 25 taxa, ~470k records, 1.1 GB; fixed dropped connections on genome-sized pages and expired history handles
- [x] gene-targeted retrieval groups; per-group screening
- [x] dry-run the gene-targeted groups; WGS contigs excluded for bacteria; influenza opted in
- [x] first full pipeline run (2026-10-03/04): N-gaps in scaffolds made pairing cubic; fixed
- [x] manifest is state, not a Snakemake output (it was being deleted each run); atomic writes;
      archives never overwritten; `scripts/rebuild_manifest.py`
- [x] cumulative reports from cached per-archive screens
- [x] screen large archives across cores (`screen --workers`, byte-identical output); biggest archives first
- [x] `drift`: Wilson / Newcombe intervals, minimum-evidence guard, evaluable denominator
- [x] assembly-level retrieval for bacterial targets (`asm` groups, NCBI Datasets): N complete
      genomes per release year, cut to credible amplicon windows
- [x] screen amplicons on both strands (minus-strand targets were never found)
- [x] `pair_evalue` per amplicon (chance.py); scoring guard available, off by default
- [x] `scoring.max_pair_evalue: 0.01`; flagged assays split into declining / low coverage (2026-10-04)
- [x] check the two suspected oligo typos (Sarcocystis long rev, Circovirus Mankertz fwd) against
      the papers (2026-10-04, `docs/2026-10-04-first-run-review.md` "Follow-up"). Sarcocystis
      P-ITSR WAS a typo, an extra C from the spreadsheet, and is corrected (98% failing -> 96%
      detected). Circovirus #174 is NOT a typo: the paper prints the extra T, so the registry
      keeps the published sequence. Both flags cleared
- [x] optional thermodynamic columns (`screen --thermo`, primer3-py): per-oligo Tm and ΔTm, never scored
- [x] `report`: markdown + self-contained HTML, per-year tables, coverage-gap table,
      degeneracy note beside the coverage trend
- [x] indel check (`scripts/indel_check.py`, 2026-10-04): across 69k sampled fail / one-primer
      no_amplicon calls, a clean single-base indel explains well under 1% of evaluable records
      for every assay but three. Gapped scoring (parasail) is not worth building. The three
      outliers are consistent same-position indels across all records, i.e. registry oligo
      typos, which makes the script a registry QA tool

## Review

`docs/2026-10-04-pipeline-review.md` reviews the pipeline stage by stage from a
software and a methods angle, and ranks what is open. The short version: the
estimand is wrong (one population proportion per assay cannot see a
lineage-conditional failure, which is why validation catches 1 of 12), the
denominator conditions on the outcome, records are not independent so the
intervals are too narrow, and declared amplicon sizes are not enforced.

## Phase 2 (next milestone): validation sets the thresholds

**Every number in `config.yaml` is a placeholder set by eye.** Nothing in the
reports is calibrated against a known answer, so the statuses should be read as
"worth looking at", not as measurements. Tier-2 validation is what turns them
into measurements, and it is also the paper's main figure.

- [ ] **Tier 2: retrospective validation.** Assemble a set of assays with
      published follow-up — a paper, erratum or redesign that reported the assay
      failing on particular lineages, or reported it still working — and ask
      whether AssayWatch flags what the literature found, using only records
      deposited before that paper. That gives a confusion matrix, and the
      thresholds become whatever optimises it rather than whatever looked
      sensible.
- [ ] **Per-chemistry scoring.** One penalty table is applied to every assay,
      but 128 of 138 are conventional or consensus PCR and 10 are probe-based.
      Conventional PCR tolerates mismatches far better than a hydrolysis probe,
      and `terminal_mismatch_fails: true` is a qPCR-strength rule, so the
      consensus assays are probably scored too harshly — which would inflate
      `fail` and so the flagged counts. Fix shape: a scoring block per
      chemistry, with the conventional numbers set by tier-2 validation.
- [x] the recent window now widens per assay (`max_window_months`, 60) when the
      standard window holds too few records, which is what made Bd unjudgeable;
      `scripts/retrospective.py` recomputes any past date's verdict, so the
      window and the minimum can be calibrated together against real cases
- [x] **Duplication check** (2026-10-05, review 3.3, partial). Each assay now also reports how many
      distinct binding-site footprints sit behind its recent window, the interval at that many
      independent draws, and for a flagged assay whether the flag survives it. Reported beside a
      verdict and never into one: a test pins that statuses and intervals are identical with and
      without footprints. This removes the duplication it can SEE (identical footprints); clade
      structure beyond that is still unaddressed, so it is not a lower bound on the effective
      sample size. The review's "weight each distinct haplotype equally" was rejected: one
      sequencing error in a primer site is a unique failing footprint, so a healthy assay would
      read as mostly failing. Corrected 2026-10-06 after two adversarial reviews: a flag now
      needs at least `min_records_for_drift` distinct footprints to be reported as surviving
      (it had reassured at every count below that, up to 19), must also stay below the
      threshold when each distinct footprint is counted once (the sample-size reduction alone
      cannot see one clone carrying the failures), and records with no footprint information
      make the count unknown instead of counting as one real footprint.
- [ ] **The drift rules interact and are untested.** `recent_window_months: 24`
      with `min_records_for_drift: 20` is why Bd (Boyle 2004) reads "insufficient
      data" at 100% detected on 17 recent records: shorten the window and assays
      fall below the minimum, lengthen it and real change is diluted. Validation
      has to set the pair together, not each alone.

The placeholders, for the record: `scoring` (3'/mid/5' primer penalties 3.0 /
1.0 / 0.5 over windows of 5, probe centre/outer 2.0 / 1.0, `detect_max` 1.0,
`reduced_max` 3.0, `terminal_mismatch_fails` true, `max_ambiguous_per_oligo` 2,
`max_mismatches_searched` 6, `max_pair_evalue` 0.01); `drift`
(`detect_fraction_threshold` 0.90, `recent_window_months` 24,
`min_records_for_drift` 20, `min_records_for_coverage` 10, `min_decline` 0.05);
`degeneracy.tiers` (8 / 128 / 4096); `assemblies.per_year` 20.

## Later
- SLURM executor profile for Greene
- contributor template, two-week review promise
- registry coverage: audit the PREDICT consensus-PCR panel for gaps, and add
  assays in current wildlife-lab use that PREDICT never covered (fungal,
  bacterial and parasitic targets especially). Sequences only from a source
  that can be read and cited, never transcribed from a secondary list
- genus-level taxids can stop containing an assay's target species when it is
  reclassified (Mycoplasmopsis agassizii, Mycoplasmoides testudinis left genus
  Mycoplasma). `check_taxids.py` cannot see this; it needs a check that each
  assay's named target organisms are still inside its retrieval root
- ARTIC-style tiled schemes (out of scope 2026-10-04): would need a scheme
  object of many amplicons reporting dropout, not one assay per pair, and
  quick-lab/primerschemes is CC BY-SA 4.0, which the registry licence would
  have to accommodate
