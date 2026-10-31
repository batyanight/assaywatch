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

**Validation, stated plainly.** Against the 50-case development set (2026-10-27
run): documented failures caught 6/11, precision of `declining` 3/9 = 33% (95%
CrI 10%-65%), false alarms 4/32. Three held-out sets have been read and spent.
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
show recent drift by construction, and their verdicts in every earlier report
rested on data that old. Fixed: those entries now share a broad hemagglutinin
query and restrict their own population by the subtype stated in each record's
description (`target.title_requires`).

**Reproducibility.** `examples/` screens one assay offline in under a second and
documents its expected output verbatim; that is the one result a stranger can
reproduce from a clone. The GenBank archives are about 9 GB and are not
recoverable on request, because retrieval is incremental on modification date, so
they are not distributed. Two committed example runs under `docs/` are outputs for
reading, not inputs for regenerating.

**Licensing.** Code MIT (`LICENSE`); the registry and the derived tables CC BY 4.0
(`LICENSE-registry`).
