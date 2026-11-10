# Glossary

The project's own vocabulary. Use these words, exactly, in function and variable names,
comments, commit messages and conversation. Definitions are taken from `config.yaml`,
`assaywatch/schema.py` and module docstrings; the location is given where the repo defines
the term precisely. PCR basics are not defined here. Add a term here before inventing a new
word for a concept.

## Registry and assays

**assay** — one registry entry: one published primer set (plus optional probe) with its target, chemistry and citation, stored as one YAML in `registry/` (`schema.py` `Assay`).

**oligo** — any single oligonucleotide of an assay: forward primer, reverse primer, probe or an alternate (`schema.py` `Oligo`).

**primer** — a forward or reverse oligo; scored by its distance from the 3' end.

**probe** — the internal oligo of a `hydrolysis_probe`, `mgb` or `lna` assay; absent in `conventional`, `sybr` and `rpa` assays (`assaywatch validate registry` prints the current split, which is not quoted here because a hand-written count goes stale; `config.yaml scoring:` for how a probe is scored).

**chemistry** — the assay's detection format, one of `conventional`, `sybr`, `hydrolysis_probe`, `mgb`, `lna`, `rpa`; scoring overrides are keyed on it (`schema.py` `Chemistry`, `config.yaml scoring: by_chemistry`).

**amplicon** — the product between the facing forward and reverse sites in a record.

**amplicon_bp** — the amplicon length in bp, measured from where the primers sit on real GenBank records, never copied from the paper (`CLAUDE.md` "Measure, never quote").

**amplicon_bp_range** — `[min, max]` declared for an assay whose product length genuinely varies by species; mutually exclusive with `amplicon_bp` (`schema.py`).

**species_sizes** — measured product length per species, only valid alongside `amplicon_bp_range` (`schema.py` `SpeciesSize`).

**amplicon_disagrees_with_paper** — review flag: the measured amplicon length differs from the published one, and the registry keeps the measured value (`CLAUDE.md`, `review.py`).

**target** — the taxon and gene the assay is for: `taxid`, `taxon_name`, `gene`, `genome_type`, optional `query` (`schema.py` `Target`).

**gene name** — `target.gene`: `symbol (product)`, or a bare name where there is no separate symbol, each virus keeping its own true symbol (influenza NP, paramyxovirus N). Coordinates, accessions and ortholog lists go in `notes_curator`, unless a position is the locus's only identity.

**scope_taxids** — taxa the assay is meant to detect; a record counts toward the drift denominator when its taxid or any ancestor is listed (`schema.py` `Target`, `config.yaml drift: scope_taxonomy`).

**exclusivity** — a published claim that the assay does not amplify certain off-target taxa; those taxa are listed in `target.exclusivity_taxids`, retrieved on purpose, and reported as predicted cross-reactivity, never scored (`schema.py` `Target`).

**citation** — the paper an entry rests on (`schema.py` `Citation`); every live entry cites its own paper.

**doi_verified** — `true` only after `scripts/resolve_citations.py` and `scripts/check_citations.py` have confirmed the DOI against Crossref; a DOI is always entered as `false` first (`CLAUDE.md`).

**status (active, draft, deprecated)** — registry status, the entry's lifecycle; only a maintainer sets `active`, and an entry in `registry/` must also carry `doi_verified: true` (`schema.py` `Status`).

**pending entry** — an assay YAML waiting for a verified DOI; it sits in `pending/`, is never screened, and is checked with `python -m assaywatch.validate pending --pending` (`CLAUDE.md`).

**review flag (needs_review)** — a controlled-vocabulary tag on an entry that can be filtered on, e.g. `oligos_read_from_figure`, `not_screenable`, `thin_evidence`; the specifics of one case go in prose, not the flag (`review.py`).

**nested protocol** — a nested or semi-nested protocol, stored as one entry per round, each screened as an independent assay and then cross-warned (`nested.py`).

**conditions** — the thermal and reagent protocol exactly as the paper prints it (annealing temperature, salts, oligo concentrations, `master_mix`); nothing in it is screened (`schema.py` `Conditions`).

**master mix** — the commercial reaction mix named in the paper, stored as the free-text `Conditions.master_mix` field; keep the term, it is the reagent's name.

**performance** — what the paper measured (LOD, efficiency, R squared, dynamic range); reported, not scored (`schema.py` `Performance`).

**panel** — one inclusivity or exclusivity validation panel the paper ran, as counts `n_tested` and `n_detected` (`schema.py` `Panel`).

**use_context** — free-text list of the settings an assay is used in; the intended use that the `drift.detect_fraction_threshold` comment says the right threshold depends on.

## Screening and scoring

**screen** — match every oligo of an assay against every record of an archive and write one call per (assay, record) (`screen.py`).

**call** — the per-record outcome of a screen for one assay, one of `detect`, `reduced`, `fail`, `indeterminate`, `no_amplicon` (`score.py` `Call`).

**detect** — a call: the summed penalty is at most `scoring.detect_max` (`config.yaml scoring:`).

**reduced** — a call: amplifies but with penalty above `detect_max` and at most `reduced_max`; drift counts it as detected unless the assay's chemistry is in `drift.reduced_not_detected_for` (`config.yaml`).

**fail** — a call: both primers land but the penalty exceeds `reduced_max`, or a terminal mismatch fails it (`terminal_mismatch_fails`).

**no_amplicon** — a call: no facing primer pair in the right orientation within the amplicon size range. Kept out of the drift fraction, with one exception: a `no_amplicon` whose exclusion is `diverged` is counted as a failure under `drift.count_diverged_as_fail` (shipped `true`) (`drift.py`, `score.py`).

**indeterminate** — a call: too many undetermined record bases (ambiguity codes, N) under an oligo to score; kept out of the drift fraction (`score.py`).

**detection** — the predicted outcome that a record would amplify, i.e. a `detect` or (unless excluded) `reduced` call; drift's numerator is the detected share.

**not detected** — a `reduced` call counted as not detected for the chemistries in `drift.reduced_not_detected_for` (currently `hydrolysis_probe`, `mgb`), where a reduced probe call stops counting as a find (`config.yaml drift:`).

**evaluable record** — a record in the drift denominator: one with a `detect`, `reduced` or `fail` call, plus a `diverged` `no_amplicon` record under `drift.count_diverged_as_fail`. `indeterminate` and every other `no_amplicon` are not evaluable (`drift.py`). See also **assessable** and **coverage gap**, two further thresholds on the same count.

**exclusion** — the reason a record yielded no amplicon: `no_site`, `truncated`, `diverged`, `no_pair`, or `chance_only` (`score.py classify_exclusion`).

**site** — a binding site: a position in a record where an oligo binds with at most `max_mismatches_searched` mismatches, found on both strands (`match.py`).

**penalty** — the position-weighted mismatch cost of one oligo; forward, reverse and probe penalties are summed into one budget under the shipped `engine: budget` (`config.yaml scoring:`).

**3' window** — the last `primer_3prime_window` (5) nt at a primer's 3' end, penalized by `primer_3prime_penalty` per mismatch (`config.yaml scoring:`).

**mid window** — positions 6 to 10 from the 3' end, penalized by `primer_mid_penalty` per mismatch (`config.yaml scoring:`).

**5' region** — the rest of a primer, penalized by `primer_5prime_penalty` (`config.yaml scoring:`).

**terminal mismatch** — a mismatch at the 3'-most base of a primer; with `terminal_mismatch_fails: true` it makes the call `fail` regardless of identity (`config.yaml scoring:`).

**mismatch** — a position where an oligo base and the record base it faces share no possible base; a degenerate oligo base that includes the record base is a match, and an undetermined record base is **ambiguous**, not a mismatch (`iupac.py base_state`).

**mispair** — the identity of a mismatch (template base : primer base, e.g. `G:T`), as opposed to its position; `mispair_penalty` overrides the cost of named mispairs such as G:T wobble (`config.yaml scoring:`, `score.py`).

**mispair window** — how many bases from the 3' end `mispair_penalty` applies; null means `primer_3prime_window` (`scoring.mispair_window`).

**oligo verdict** — under `engine: serial` only, the per-oligo judgement `ok`, `weak` or `blocked` set by `oligo_ok_max` and `oligo_weak_max` (`score.py oligo_verdict`). The only place "verdict" means something other than a drift status.

**engine (budget, serial)** — how oligo penalties combine: `budget` sums them against `detect_max`/`reduced_max`; `serial` judges each oligo alone and the worst decides (`scoring.engine`).

**degeneracy** — the pool size of a degenerate oligo (product of its ambiguity-code multiplicities); reported with `tiers` negligible, moderate, high, never penalized (`degeneracy.py`, `config.yaml degeneracy:`).

**degenerate base** — an IUPAC ambiguity code written in an oligo, synthesised as a mixture; inosine is kept in `seq_as_written` (`iupac.py`, `schema.py`).

**ambiguous (record base)** — a record position whose true base is undetermined (an IUPAC code or N in the record); the code also writes "undetermined" for the same thing; reported separately and never scored as a mismatch (`match.py`).

**chance pair** — a forward and reverse site that face each other in amplicon range by chance in a long record, with nothing to do with the target (`chance.py`).

**E-value (site, pair)** — expected number of such sites or pairs by chance in a record of that length and composition; `max_site_evalue` and `max_pair_evalue` set the credibility cut (`chance.py`, `config.yaml scoring:`).

**locus identity** — whether an amplicon's interior resembles the interiors of the amplicons the assay actually works on, the chemistry-independent form of the probe-site test; shipped off (`locus_identity_min: null`) (`locus_identity.py`, `config.yaml scoring:`).

**thermo** — optional nearest-neighbor duplex Tm and delta Tm columns per oligo; shown, never scored, shipped `thermo: false` (`thermo.py`, `config.yaml`).

**footprint** — one record's mismatch pattern for an assay (positions from the 3' end and ambiguity counts per oligo), interned to a single string; millions of records share a few thousand footprints (`drift.py FOOTPRINT_COLUMNS`, `calls.py`).

**strategy** — a pre-registered candidate scoring change, one YAML in `strategies/` overriding `config.yaml` values and carrying its own kill criterion, replayed against frozen sets.

**S-ladder (S0, S3b, S7, ...)** — the numbered ladder of candidate scoring strategies; `S0` is the shipped rule, names are reserved in `docs/journal/2026-10-24-scoring-strategy-test-plan.md` (S5 is C2, the gated Bayesian per-record model) (`ROADMAP.md`).

## Drift and verdicts

**drift** — a fall over time in the share of GenBank records for a taxon in which an assay's oligos still match; not the same as loss of infections detected (`config.yaml` "WHAT DRIFT IS AND IS NOT").

**baseline** — the pooled earlier records an assay's recent window is contrasted with (`drift.py`).

**deposit date** — the day a record first appeared in GenBank (`created` in the metadata; esummary `CreateDate`, or an assembly's `release_date`); the clock every verdict, window and trend runs on (`calls.read_dates`).

**collection date** — the day the isolate behind a record was collected, as BioSample gives it (a full date, a year-month, a bare year, a range or "missing"); carried for assembly records only, in the `collected` metadata column and, for older archives, in the title (`assemblies.py`, `metadata.collection_year`).

**collection-year lens** — the report section that re-dates each record by its collection YEAR and recomputes the recent share beside the deposit-clock one; a lens on sequencing backlog that moves no status (`report.collection_lens_rows`; decided 2026-10-30, `docs/journal/2026-10-30-design-grilled.md` Q1-Q3). Assembly records only until `report.collection_sidecar` names the file `scripts/backfill_collection_dates.py` fetched; then every record.

**recent window** — the latest `recent_window_months` (24) of deposit dates, widened a year at a time up to `max_window_months` (60) when records are scarce (`config.yaml drift:`).

**status (drift)** — the per-assay drift verdict: `declining`, `low coverage`, `watch`, `insufficient data`, `no recent data`, `stable`, plus `no data` (`drift.py` `STATUS_ORDER`, `NO_DATA`; `docs/screening-and-the-drift-call.md` "The drift call"). Not the registry **status (active, draft, deprecated)**; say "drift status" or "registry status" wherever both could be meant.

**declining** — status: recent share is below `detect_fraction_threshold`, the fall is at least `min_decline` with a Newcombe interval wholly below zero, and the assay cleared the threshold in some earlier year (`drift.require_working_baseline`) (`docs/screening-and-the-drift-call.md`, `config.yaml drift:`).

**low coverage** — drift status: below threshold but not measurably lower than before, or never working; an assay used beyond its design, or one that was always poor (`docs/screening-and-the-drift-call.md`). A pooled, over-time statement about one assay; not a cell of the **coverage map**, which is per species and has no time axis.

**watch** — drift status: below threshold with an interval that still covers it (`docs/screening-and-the-drift-call.md`).

**insufficient data** — status: fewer than `min_records_for_drift` evaluable records; reported, never flagged (`config.yaml drift:`).

**flag** — in drift, an assay whose recent upper Wilson bound falls below the threshold (`flag_rule: wilson`) or whose posterior probability of being below it exceeds `flag_posterior_credibility` (`posterior`). Not a review flag.

**detect_fraction_threshold** — share below which an assay is called failing, 0.90; a judgement about tolerable surveillance loss (`config.yaml drift:`).

**lineage** — a group of records of one assay's target defined by NCBI taxid (grouped at `group_at_rank: species`), so a miss on one clade is not averaged away (`lineage.py`, `config.yaml lineage:`).

**sublineage** — a finer split within one taxid, resolved from titles or by sequence-homology clustering (`cluster`, Mode C) where the taxid carries no label (`subcluster.py`, `clustermaps.py`, `config.yaml lineage: sublineage`).

**lineage-conditional verdict** — the assay-level verdict overridden when any one lineage is significantly below threshold after Holm correction (`lineage.multiple_testing`), so the worst lineage drives the call (`lineage.py`, `config.yaml lineage:`).

**site drift** — which oligo positions are failing and in which footprint groups of accessions, for assays the main report calls declining (`sitedrift.py`).

**trend** — a Cochran-Armitage test for a monotone slide in the detected share by deposit year, reported beside the verdict, never folded into it (`trend.py`, `config.yaml drift: trend_min_years`). Printed twice since 2026-10-30: by record (an upper bound on the evidence, since duplicated deposits count as independent) and **by footprint** (each distinct footprint counted once per year; nearer a lower bound, since a sequencing error in a primer site mints a footprint). When they disagree on direction the report says so.

**hierarchical layer (C1)** — Beta-binomial partial pooling of an assay's lineages; reported, never a verdict unless `verdict_from: posterior` (`hierarchical.py`).

**Wilson / Newcombe interval** — Wilson score interval for a proportion; Newcombe hybrid-score interval for a difference of two, built from the two Wilson intervals (`interval.py`, `drift.py`).

## Coverage

Agreed 2026-11-10. Coverage and drift are two separate summaries of the same calls table
and neither depends on the other; coverage is the primary product. Built the same day as
`assaywatch coverage` (`coverage.py`): the map, the cell states, recommendations and the
nested rows. The **locus check** runs as its own stage (`assaywatch locus`) on the
records the screen could not judge, and coverage joins its side file. NOT built yet,
and marked below: **widened retrieval** and the **host column**'s data.

**coverage** — which species an assay is predicted to detect as of today, including species outside what its paper claimed. A snapshot with no time axis. Bench vocabulary would say "in-silico inclusivity"; this project says coverage.

**coverage map** — the assay x species table: one **coverage row** per species, one **coverage cell** per (assay, species).

**coverage row** — one NCBI species taxid. Host never defines a row. A row is split by **sublineage** only where one taxid is known to hide distinct lineages (Bd, influenza A subtypes).

**host column** — the hosts named in a row's records (the GenBank `/host` qualifier, shown as written, most common first). Displayed, never used to group or score. "Fish ranavirus" is something a reader concludes from this column; the tool does not claim it. Empty on real runs until retrieval stores `/host`.

**in-scope row / out-of-scope row** — a row whose taxid is, or is not, under the assay's `scope_taxids` (or its `target.taxid` where no scope is declared). Both are screened and shown, in separate blocks. Drift uses scope to shrink its denominator; coverage uses it only as a label.

**widened retrieval** — a retrieval group fetched above the assay's own target (typically the family) so out-of-scope species are in the archive at all. A per-assay retrieval setting. Not built: a species has a row today only if its records were already in the assay's archive.

**coverage cell** — the predicted outcome for one assay on one species, one of `predicted detect`, `partial`, `predicted fail`, `not assessable`, always printed with its **cell count**. No minimum record count hides a cell.

**cell count** — detected records over locus-present records for the cell, e.g. `8/10`. The reader judges a `3/3` and a `300/300` differently; the tool does not hide either.

**predicted detect** — cell state: the records carry no mismatch that would block the reaction. Worded that way on purpose. It says the oligos match; it does not say the reaction works.

**partial** — cell state: either the records split between detected and not, or they are detected with an expected loss of efficiency (e.g. one mismatch under a standard hydrolysis probe: amplifies, expect a Ct shift). Not the per-record call `reduced`, which is one input to it. In numbers (`config.yaml`, `coverage:`): more than `fail_max_share` detected and less than `detect_min_share` cleanly detected.

**cleanly detected** — a record called `detect`. "Detected" in a cell count also includes `reduced`; `predicted detect` is judged on the cleanly detected share alone, so a species whose records are all `reduced` reads `partial` with a full count.

**predicted fail** — cell state: the locus is present and the oligos are predicted not to amplify it. A stronger claim than `predicted detect`, because a 3' terminal mismatch or a missing site is good evidence from sequence alone.

**not assessable** — cell state: no record of that species is shown to contain the locus, so the assay was never tested by the data. Not a failure. Distinct from **assessable** (a drift lineage with enough evaluable records).

**locus check** — the test, independent of the primers, of whether a record contains the assay's target region: a local, gapped alignment of a reference amplicon against the record, both strands (`locus_check.locus_check`). The locus is present when the aligned stretch reaches `coverage.locus_min_identity` and spans `coverage.locus_min_covered` of the reference. Decides between `predicted fail` and "does not count" when no primer site is found. Not `locus_identity`, which judges an amplicon the primers DID find.

**locus stage** — `assaywatch locus` (`locus.py`): runs the locus check on every **unjudged record**, and on every `fail` call at the amplicon the screen placed (a **fail check**), and writes the **locus file**. Separate from the screen on purpose, so adding it rescreened nothing.

**unjudged record** — a `no_amplicon` the screen did not label `diverged`: no primer site was found and the screen cannot say whether the gene is there. The only records the locus stage checks.

**locus file** — `locus.tsv.gz`, the locus stage's output: one row per (assay, record checked) with `present`, `has_room`, `identity`, `covered`, `amplicon_covered` and `checked` (`unjudged` or `fail`). `assaywatch coverage --locus` joins the `unjudged` rows and reports the `fail` ones.

**has room** — a record reaches across the whole amplicon, primer sites included, as placed by the winning reference (`locus.judge`). Coverage counts a checked record as locus-present only when it is `present` AND has room; present without room is a deposit cut short, which never tested the assay. With **wide references** the two nearly always agree; with interiors a reference could be whole in a record that stopped before a primer site.

**seed** — in the locus check, a short exact word (7 bases) shared by a reference and a record. In a record too long to align whole, the diagonals where seeds pile up pick the stretches that are aligned; in a short one, seeds pick which of the assay's references are aligned at all. A heuristic: a locus sharing too few words with every reference is missed.

**identity (locus check)** — of the aligned columns, the share that match. High over a sliver for unrelated DNA, which is why it is never read without **covered**.

**covered (locus check)** — the share of the whole reference, flanks included, that the alignment spans. Reported; since 2026-11-10 it is **amplicon covered** that is judged.

**amplicon covered** — the share of the AMPLICON part of the winning reference that the alignment spans (`locus.amplicon_covered`). The locus is present at `coverage.locus_min_covered` of it, with identity at `coverage.locus_min_identity` and at least `coverage.locus_min_aligned_bp` reference bases aligned. A wide reference's flanks are there to be aligned, not required: a deposit that holds the amplicon and stops twenty bases beyond it has the locus.

**fail check** — the locus check run on a `fail` call, at the stretch the screen called an amplicon. A `fail` that is not the locus is two primers landing by chance in other sequence, or a product whose length no reference covers. Reported per assay in `coverage.md`; it changes no call and no cell.

**UNVERIFIED row** — the coverage cell holding a species' records whose GenBank title begins `UNVERIFIED` (GenBank could not confirm the sequence or its annotation, the organism name included). Counted beside the species row, never in it, and left out of a **recommendation** (`coverage.read_unverified`).

**locus present** — a record shown to hold the assay's target region; only these enter a cell count. Until the locus check exists the only evidence is the screen's own: both primers found a site (a `detect`, `reduced` or `fail` call) or the screen labelled the record `diverged`. So a distant species in which neither primer lands is invisible to the map.

**reference amplicon** — a stretch cut from a record the assay detects, used as the query of the locus check. One shorter than `coverage.locus_min_reference_bp` is not used.

**wide reference** — a reference amplicon cut as the amplicon plus up to 100 bp of flank each side, so that a 57 bp amplicon still gives the locus check something to measure. One per product length, then per species, up to 8 an assay (`docs/locus-wide-references.json`, built by `scripts/build_locus_references.py`). What the locus stage reads by default.

**interior** — an amplicon with its primer sites trimmed off (`docs/locus-references.json`). Built for **locus identity**; the locus stage still reads the format, and no longer uses it by default.

**recommendation** — for one species, the assays ordered by coverage cell, ties broken toward the less degenerate primer pool. A ranking, not a verdict.

**degeneracy annotation** — the degeneracy tier shown on an assay's rows. It never changes a call or a cell; it breaks ties in a recommendation.

**nested rows** — the rows a nested or semi-nested protocol gets in the coverage map: **together** (shown twice, see **together (trace rule) / together (strict)**), **round 1 alone**, **round 2 alone**. The two "alone" rows are the rounds' own registry entries; only the `together` rows are computed, under the ids `<last round's id>@together-trace` and `@together-strict`.

**together** — nested row: the protocol as published, round 1 then round 2. Round 2 is scored on the normal rule, round 1 on one of two rules, and the cell is the worse of the two rounds.

**together (trace rule) / together (strict)** — the two `together` rows, shown side by side since 2026-11-10 because how much round 1 has to do is not measured. Trace: round 1 passes unless the **trace rule** fails it. Strict: round 1 must itself be called `detect` or `reduced` (what `nested.nest_calls` reads). They share one set of records. Read the pair as a range; where they agree the protocol's cell is not in doubt.

**round 1 alone / round 2 alone** — nested rows: that round's primer pair on raw template, scored on the normal rule because it carries the whole reaction. Round 2 alone is the fallback when round 1 misses a species.

**trace rule** — the looser scoring of round 1 inside a `together` row: round 1 only has to make a trace of product, so it fails only on a 3' terminal mismatch (one the scoring config does not price at zero) or no site (`coverage.trace_passes`). Agreed in outline 2026-11-10 and not measured. It is permissive: on the 2026-11-01 calls it lets nearly every scored round-1 record through, so a trace-rule `together` row reads close to round 2 alone, and the strict row is shown beside it.

## Pipeline and runs

**retrieve** — fetch nucleotide records for a retrieval group from NCBI and archive them, incrementally (`retrieve.py`).

**retrieval group** — a (taxid, `target.query`) pair; assays sharing both share one archive, on disk at `data/retrieved/<taxid>/<slug>/` (`retrieve.py`, `groups.py`).

**archive** — the gzipped FASTA plus `*.meta.tsv.gz` for one retrieval group, keeping whole records so rescreening at any setting is free (`windows.py`, `retrieve.py`).

**assembly (`asm` group)** — a retrieval group of sampled bacterial genome assemblies (`assemblies.taxa`, `per_year`) cut down to the loci the oligos could build an amplicon in, used where gene-level deposits stopped (`assemblies.py`).

**window archive** — an archive cut down to a `buffer_bp` window around the sites a screen found, for distribution (`windows.py`).

**composition window** — one record's amplicon plus up to `flank_bp` of flank each side, every primer/probe site masked to N, cut by `subcluster.flanked_region` and returned as a `Region` with the flank actually used. What composition clusters; not a window archive, which is cut around sites for distribution and keeps them.

**title token** — a word a cluster's record titles carry and the other clusters' do not, shown in the composition panel's tooltip: what the cluster's name leaves out (`composition.title_tokens`). Record qualifiers (`strain`, `isolate`, `clone`) are never tokens.

**same-mix line** — an assay's per-year detected share recomputed on the whole period's lineage mix, by direct standardisation (`composition.same_mix_series`). Drawn beside the observed line: where the two diverge, the mix of lineages being deposited moved rather than detection within them.

**mix part / within part** — the two numbers Kitagawa's decomposition splits a change in detected share into: how much the lineage mix moved, and how much detection moved within the lineages (`composition.split_change`). They add to the change exactly. A lineage deposited in only one of the two periods has no within part, so its whole effect is mix.

**new since design** — of a species under an assay's target taxon: first deposited in this assay's archive after the year its paper designed it (`composition.species_years`), so the designers could not have had it. Unset where the entry carries no `citation.design_year`.

**diverged stratum** — in the composition panel, the records whose primers both landed past the mismatch budget: they have no amplicon and so no composition window, and are drawn and counted as a lineage of their own rather than placed by guesswork (`composition.DIVERGED`). Under `drift.count_diverged_as_fail` they are in the denominator, which is why the panel must show them.

**manifest** — the retrieve stage's run state: per-group last-run dates and counts, kept as state not as a Snakemake output (`retrieve.py`, `timing.py`).

**run record** — what `retrieve` returns for one fetched group (`TaxonRun`), written to the manifest (`retrieve.py`).

**screen signature** — the record, written beside a cached screen, of what it was produced under, so `collect` can detect a stale screen whatever Snakemake remembers (`signature.py`).

**rescreen** — re-run `screen_archive` over the archives after a scoring or code change; the shipped scoring hash forces one (`config.yaml scoring:`, `signature.py`).

**collect** — gather the cached per-archive screens into one calls table, `calls.tsv.gz` (`collect.py`).

**calls table** — `results/<date>/calls.tsv.gz`, one row per (assay, record) (`calls.py`).

**taxa cache** — `docs/taxa-cache.json`, the lineage analysis's taxid-to-name map (`config.yaml lineage.taxa_cache`); not the taxon records.

**taxon record** — an entry in `docs/taxon-records.cache.json`: NCBI scientific name, common name and rank for a taxid, used by the assay sheet (`docs/assay-sheet.md`).

**pipeline stages** — Snakefile rules `validate`, `retrieve`, `screen_archive`, `collect_calls`, `report`, `site_drift`, `lineage_analysis`, `degeneracy_table`, `figures`; `all` requests the outputs (`Snakefile`).

## Evidence and curation

**retrospective case** — a row in `docs/validation-cases*.tsv`: a published follow-up where an assay worked or failed, with its mechanism (`coverage` or `drift`); the evidence the thresholds are checked against (`config.yaml` header).

**development set** — `docs/validation-cases.tsv`, the cases thresholds were tuned against, so figures on it are in-sample (`docs/INDEX.md`).

**held-out set** — validation cases reserved for one decision and not consulted for any threshold; `validation-cases-heldout.tsv` is spent, `-heldout-2.tsv` is current (`docs/INDEX.md`).

**bench panel** — a per-strain wet-lab result table read from a paper into `docs/bench-panels/*.tsv`, used as sensitivity and specificity evidence for scoring changes (`docs/INDEX.md`, `config.yaml scoring:`).

**design era** — how much sequence existed when an assay was designed versus now (`records_before_design`, `records_now`, fold increase), from `scripts/design_era.py` into `docs/design-era.tsv` (`docs/INDEX.md`).

**predict protocol** — `source.predict_protocol`, the `P-0nn` protocol under which an entry's oligos were extracted (`schema.py` `Source`).

## Resolved from the repo on 2026-10-29

**tier-2 (validation)** — retrospective validation: assays with published follow-up (a paper, erratum or redesign reporting the assay failing or still working on particular lineages), asked whether AssayWatch flags what the literature found using only records deposited before that paper; scored as a confusion matrix with Jeffreys intervals by `scripts/retrospective.py` (`ROADMAP.md` "Tier 2: retrospective validation"). No tier-1 is named anywhere; the word survives from the original plan's numbering.

**ground truth** — a documented outcome for an (assay, lineage) pair from a tier-2 case or a bench panel row; a flag with "no ground truth either way" is one no paper or panel has judged (`config.yaml scoring:`).

**evaluable / assessable / coverage gap** — three thresholds on one count. A record is *evaluable* as defined under **evaluable record** above. A lineage is *assessable* when it has at least `lineage.min_records_per_lineage` evaluable records. A *coverage gap* is an assay-level shortfall below `drift.min_records_for_coverage`. Same denominator, three places it is tested.

**undecided** — the set of drift statuses that are not a verdict: `insufficient data`, `no recent data`, `no data` (`scripts/retrospective.py UNDECIDED`). `drift.py STATUS_ORDER` carries the first two and `NO_DATA` the third; the report grays all three. `no recent data` means nothing new was deposited in the window; `insufficient data` means too few evaluable records; `no data` means no archive at all.

**C1 / C2 / C3** — the three layers of `docs/bayesian-scoring-plan.md`: C1 the drift proportion (replaces Wilson/Newcombe and the flag rule), C2 the per-record call (replaces the additive penalty table), C3 the validation matrix intervals (replaces point sensitivity). The **S ladder** (`docs/journal/2026-10-24-scoring-strategy-test-plan.md`, S0 baseline, S3b, S7, S7b…) is a sequence of candidate *scoring rules* inside C2's territory, each pre-registered with kill criteria. C-numbers name what is modeled; S-numbers name one tested change to the penalty rule.

**retrospective families** — the phrase families that `scripts/find_retrospective_cases.py` uses to find citing papers (`docs/journal/2026-10-26-retrospective-case-search.md`): `miss`, a paper reporting the assay missing samples (the scarce `fails` kind, or a clinical sensitivity report); `weakened`, reduced or partial detection; `mismatch`, a paper locating primer mismatches against a lineage (the best route to a `drift` case); `redesign`, a group redesigning the assay, which usually says why; `use`, opt-in, a paper that simply uses the assay and so may test our oligos on new material (`docs/journal/2026-10-29-use-family-cases.md`); `late_redesign`, opt-in and pre-registered, a redesign published five or more years after the design paper, the first source tried for a `drift` case (`docs/journal/2026-10-30-redesign-family.md`).

**lineage Modes A, B, C** — the three ways a record is assigned to a sublineage (`assaywatch/lineage.py` docstrings). Mode A: by taxid, when NCBI already distinguishes the sublineages below the query taxon (Avipoxvirus: fowlpox vs canarypox). Mode B: by a title token regex (influenza subtype `(H5N1)`). Mode C: by a sequence cluster label from `assaywatch/subcluster.py` (Bd BdGPL vs BdCAPE). Each returns None to defer to the next.

## Words with more than one meaning

Each of these is one word doing several jobs. Qualify it every time.

**status** — registry status (`active`, `draft`, `deprecated`) or drift status (`declining`, `stable`, ...).

**flag** — a review flag (`needs_review`) or a drift flag (the rule that puts an assay below threshold).

**verdict** — a drift status, or under the serial engine an oligo verdict (`ok`, `weak`, `blocked`).

**coverage** — four things: the coverage map (this glossary's "Coverage" section); the drift status `low coverage`; a coverage gap (too few records, `drift.min_records_for_coverage`); and how completely an archive was retrieved (`retrieve.py`, `composition.coverage_*`). Unqualified, it means the coverage map.

**site** — a binding site (`match.py`, `sitedrift.py`), or the project website (`site.py`, `site_render.py`, `site_svg.py`).

**window** — 3' window, mid window, mispair window (positions on a primer); recent window (deposit dates); window archive and composition window (stretches of a record).

**target** — the assay's taxon and gene. The sequence being searched is a **record**, and the base a primer faces is the **template** base; neither is "the target".

**tier** — a degeneracy tier (`negligible`, `moderate`, `high`) or tier-2 validation.

**panel** — a `Panel` in the registry schema (the paper's own inclusivity counts), a bench panel (`docs/bench-panels/`), or a panel of the website dashboard.

**assessable** — a drift lineage with enough evaluable records; `not assessable` is a coverage cell with no locus-present record.

**round** — a nested round (round 1, round 2), or the arithmetic `round()` in code.

**exclusion / exclusivity** — an exclusion is why a record yielded no amplicon; exclusivity is a paper's claim about off-target taxa.

## Words not to use

**hit** — not a project term. An oligo matching a record is a **site**; an assay's outcome on a record is a **call**; a record returned by a search is a **record**.

**alert** — not a project term. An assay-level statement is a **drift status** or a **coverage cell**; the rule behind a drift status is a **flag**.

**strain** — not a unit this project groups by. Say **species** (a coverage row), **lineage** or **sublineage**. `strain` survives only as a GenBank record qualifier.

**clade, stratum** — say **lineage** or **sublineage**. The one exception is **diverged stratum**, defined above.

**product** — say **amplicon**.

**undetermined (record base)** — say **ambiguous**.

**inclusivity** — say **coverage**, except when naming a paper's own inclusivity panel.

**drift (for a species the assay never detected)** — that is a `predicted fail` coverage cell or a `low coverage` drift status. Drift is a fall over time.
