# Changelog

What changed between releases, and what each release's output is worth.
`ROADMAP.md`'s `# Done` section is organised by phase rather than by version and
is the fuller history; this file is the short version a reader needs before
citing a release. `docs/state-of-the-project.md` is the companion page on what
the output is worth.

Dates are the release date. Figures carry the date of the run that produced them,
because none of them can be recomputed without the archives.

## v0.1.0 — unreleased

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

**The release run.** `docs/example-run-2026-10-31/` is the run this release
describes, and it is also the confirming rescreen `scoring.mispair_window: 10`
(S7b) owed: because `scoring` is in the screen hash, all 580-odd archives
rescreened. Against the previous run 11 assays changed status, every one of them
an improvement or an unblocking: `stable` 60 -> 72, `watch` 8 -> 5, `low coverage`
34 -> 31, `no recent data` 20 -> 18, `declining` unchanged at 42. S7b's one
pre-registered prediction landed — `MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010`,
held-out set 2's single false alarm, moved `declining -> stable`. The two
Tsukamoto influenza assays moved off `no recent data` for the first time, to
`stable` (H5) and `declining` (H7).

**Licensing.** Code MIT (`LICENSE`); the registry and the derived tables CC BY 4.0
(`LICENSE-registry`).
