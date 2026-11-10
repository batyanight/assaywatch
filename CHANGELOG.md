# Changelog

What changed between releases, and what each release's output is worth.
`ROADMAP.md`'s `# Done` section is organised by phase rather than by version and
is the fuller history; this file is the short version a reader needs before
citing a release. `docs/state-of-the-project.md` is the companion page on what
the output is worth.

Dates are the release date. Figures carry the date of the run that produced them,
because none of them can be recomputed without the archives.

## Unreleased

- **New stage: `assaywatch coverage`, the coverage map.** Which species each assay is predicted to
  detect as of today: one cell per (assay, species), `predicted detect`, `partial`, `predicted fail`
  or `not assessable`, always with its count and its number of distinct footprints, in-scope and
  out-of-scope species in separate blocks. A nested protocol gets each round alone and `together`
  under two rules (trace and strict), as a range. Reads the calls
  table and changes no call, no status and nothing in `report.md`. Without a locus file behind it,
  read an absent species as unknown (`ROADMAP.md`, "Coverage map").
- **New stage: `assaywatch locus`.** For the records in which the screen found no primer site, it
  asks whether the assay's target region is there at all (a local, gapped alignment of a reference
  amplicon), and writes `locus.tsv.gz`. `assaywatch coverage --locus` joins it, which turns a blank
  cell into `predicted fail` where the locus is shown present with room for the primers. Without
  `--locus` the coverage map is unchanged. The screen is not touched and nothing is rescreened.
  Its references are the amplicon plus its flanks (`docs/locus-wide-references.json`, 207 assays),
  so short amplicons can be checked too. Both stages are opt-in Snakemake targets
  (`--config locus=true -- coverage_map`) and no part of the weekly run. It has been run on eight
  assays, not on the table: the one finding read by eye holds (the Farias avipox assay on fowlpox,
  pigeonpox and turkeypox), and the second rests on `UNVERIFIED` genomes and is not to be quoted.
- Assay pages open on the primer graph, then the line graph, then the bar graph. Assembly records now
  reach the lineage groups, and a species is no longer split across names by the strains in its titles.
  Fixes from the security and code reviews. No status moved.
- Every assay page shows what was deposited by lineage, with a same-mix line on the detection
  chart and the change split into mix and detection within. Report-only: no status moves. These
  are sequence groups at a fixed cut, and in 17 of 199 assays the largest holds several species,
  which the page says (2026-11-01 run).
- 21 scopes broadened on rereading their papers, 2 more by a host-checked list of 1,269 bird
  lineages, and 3 Uccellini entries narrowed to the one virus they were written for, moving 2 from
  `low coverage` to `insufficient data`. No other status moved.
- Withheld pages show the mismatch map unless the oligo is in doubt or the readout isn't an amplicon.
  Scope sections say what an assay is meant to detect, what it is scored against and where it was
  retrieved from; 66 entries carry the paper's claim.
- Four entries moved to `pending/` because one of their primers is printed in no
  paper: `Sarcocystis_18S_5_8S_Kutkiene_2010_ShortITS1R`, the two
  `Mycoplasma_16S23S_ITS_Rebelo_2011_16_23_*` pairs, and
  `Mycoplasma_16S_vanKuppeveld_1992`. 216 assays are live.
- Assay pages show the measured size range, and the size by species, where the
  product length varies, instead of a dash.

## v0.2.0 — 2026-11-02

Archived at Zenodo: [10.5281/zenodo.23891547](https://doi.org/10.5281/zenodo.23891547)
(this version), under the same concept DOI as v0.1.0.

- **Assay ids, names and genes rebuilt on one scheme**,
  `<Taxon>_<gene>_<FirstAuthor>_<Year>[_qualifier][_roundN]`, from each entry's
  own taxon, gene and citation. Every id changed, and with it every site URL. Four
  ids that named an author other than the cited paper's are corrected. Gene
  fields name the locus only, in American spelling. See
  `docs/journal/2026-11-02-one-id-scheme.md`.
- **Gene corrected** on the three Hellgren et al. 2004 entries: cytochrome b,
  as the paper states, not cytochrome c.
- `citation.as_written` removed from the schema; `citation.reference` is the
  citation.
- The validator refuses an entry whose text names a source list.
- **Protocol pages** measure each round on the protocol's own records, scope and
  recent window, so a round's figure and the protocol's are directly comparable.
  This showed the Messmer genus round 1 detecting 0 of 39 recent *C. trachomatis*
  records (open in `ROADMAP.md`).
- The `cross_reactive` flag is no longer printed on the site.
- The repository history restarts at one commit; `docs/journal/` is the record.

**What the output is worth.** No scoring rule, threshold or verdict changed. The
2026-11-01 run, remapped to the new ids, gives the same statuses as before the
rename; `docs/example-run-2026-11-01/` is that run.

## v0.1.0 — 2026-10-31

Archived at Zenodo: [10.5281/zenodo.23841794](https://doi.org/10.5281/zenodo.23841794)
(this version) under the concept DOI
[10.5281/zenodo.23841793](https://doi.org/10.5281/zenodo.23841793), which always
resolves to the newest release and is what `CITATION.cff` carries.

The first release. Nothing was tagged before it, so everything here is "new" in
the sense that nothing was ever published; what follows is what the artifact is
rather than what changed.

**What it is.** A version-controlled registry of 218 published PCR and qPCR
pathogen assays, a screening engine that predicts detection per (assay, GenBank
record), and a pipeline that reports predicted detection indexed by year of
deposit so that decay reads as a trend. The registry and that time axis are the
contribution; the engine is the means.

**What its output is worth.** A status is worth reading, not quoting. `declining`
means "worth looking at", not "this assay has failed". Nineteen thresholds decide
every verdict and all but one were set by eye; the exception, `drift.min_decline`
0.05, has independent regulatory precedent. See `docs/state-of-the-project.md`.

**The premise has one confirming case.** On 2026-10-30 the tool caught its first
documented failure through the drift flag itself rather than through `low
coverage`: the influenza A M1 assay of Ward 2004 reads `declining` as of
2013-09-06, agreeing with Yang 2014, while the degenerate redesign Yang built to
fix it reads `stable` on the same records. The two entries differ in nothing but
their oligos, which is what makes the row worth more than the verdict.

**Validation, stated plainly.** Against the 50-case development set on the
2026-10-31 release run: documented failures caught **6/11**, precision of
`declining` **4/10 = 40% (95% CrI 15%-70%)**, false alarms 4/32. Of the 11
documented failures 10 are coverage gaps and one is drift, and that one is caught.
All three held-out sets are spent and all three are worse than the development
set: set 1 caught 3/9 with 0 false alarms in 17, set 2 caught 2/3 but put 4 of 10
working assays in `declining`, set 3 caught 1 of its 2 drift rows. Three held-out sets have been read and spent.
Held-out set 2 put five of ten working assays in `declining`, four of them
pan-family consensus nests — a mismatch between what their papers claim and what
the status measures, not only a scoring error.

**Known limitations** are in `ROADMAP.md` and summarised in the state-of-the-project
page. The one most likely to be challenged: the denominator is drift-correlated,
65.7% of 2.72M rows never reach the statistics, and that bias may not be fixable
without a different estimand.

**One defect found while preparing this release, worth naming because it was
live.** NCBI has stopped assigning influenza subtype taxids to new deposits, so
four entries whose retrieval query named those taxids had archives that ended
years earlier — H5's newest deposit was 2021, H7's was 2020. Neither assay could
show recent drift by construction. No wrong verdict was published: both committed
example runs report these assays as "no evaluable records deposited since Oct
2021", so the tool declined to judge them and named the cutoff. The defect is that
the message reads as a fact about the taxon when it was a fact about the query, so
four live assays sat unjudgeable while the report looked correct. Fixed: those
entries now share a broad hemagglutinin
query and restrict their own population by the subtype stated in each record's
description (`target.title_requires`).

**Reproducibility.** `examples/` screens one assay offline in under a second and
documents its expected output verbatim; that is the one result a stranger can
reproduce from a clone. The GenBank archives are about 9 GB and are not
recoverable on request, because retrieval is incremental on modification date, so
they are not distributed. Two committed example runs under `docs/` are outputs for
reading, not inputs for regenerating.

**History.** This repository begins at a single commit. It was recreated from a clean
tree on 2026-10-31, before this release, because the development history contained an
institutional name that should not be in a published artifact; the tree had been clean
of it since 2026-10-23. The history is retained privately. `docs/ai-involvement.md`
carries the co-authorship figures read from it, and
`docs/journal/2026-10-31-repository-recreated.md` records what was measured and kept.

**The release run.** The 2026-10-31 run is the one this release describes (its
committed copy is in the Zenodo archive; the repository now carries the 2026-11-01
run as `docs/example-run-2026-11-01/`), and it is also the confirming rescreen `scoring.mispair_window: 10`
(S7b) owed: because `scoring` is in the screen hash, all 580-odd archives
rescreened. Against the previous run 11 assays changed status, every one of them
an improvement or an unblocking: `stable` 60 -> 72, `watch` 8 -> 5, `low coverage`
34 -> 31, `no recent data` 20 -> 18, `declining` unchanged at 42. S7b's one
pre-registered prediction landed — `Monkeypox_virus_G2R_Li_2010_G2R_G_F`,
held-out set 2's single false alarm, moved `declining -> stable`. The two
Tsukamoto influenza assays moved off `no recent data` for the first time, to
`stable` (H5) and `declining` (H7).

**Licensing.** Code MIT (`LICENSE`); the registry and the derived tables CC BY 4.0
(`LICENSE-registry`).
