# Your assay was designed against the sequences that existed then

A PCR assay is built against whatever was in GenBank on the day someone designed
it. Then it gets used for years, and the database fills with strains nobody
re-checks it against.

Nothing warns you when the primers stop matching. The reaction comes back
negative, and a negative looks identical whether the pathogen was absent or your
primers missed it. For wildlife and One Health work this matters more than
usual: the targets are sparsely sequenced, assays are borrowed across species
and continents, and there is rarely a positive control for the strain actually
circulating.

**AssayWatch re-checks published assays against newly deposited sequence and
reports predicted detection by the year each record was deposited**, so decay
shows up as a trend instead of a snapshot. It covers 218 published assays, each
one cited to the paper it came from, screened against the GenBank records of its
own target.

[Browse every assay](assays/index.md){ .md-button .md-button--primary }
[What the output is worth](what-the-output-is-worth.md){ .md-button }

---

## Before you trust anything here

**A status tells you where to look. It is not a result.**

`declining` means this assay is worth your attention, not that it has failed. I
can tell you how often that call is right, because I tested it against assays
whose real-world performance was later published: **4 of 10 `declining` calls
were genuine documented failures**, with a 95% credible interval from 15% to
70%.

That interval is wide because the evidence base is small, and I would rather
show you the width than round it away. Nineteen thresholds decide every verdict
here and all but one of them I set by eye.

[How it was tested](how-it-was-tested.md) has the full confusion matrix,
including three held-out sets that all scored worse than the set I tuned on.

## What a run looks like

On the 2026-10-31 run, 217 of the 218 assays were screened (one is retired):

| status | assays | what it means |
|---|---|---|
| stable | 72 | recent detection does not fall below 90% |
| declining | 42 | below 90% **and** measurably lower than it used to be |
| low coverage | 31 | below 90%, but not falling — used beyond its design, or never covered this target |
| insufficient data | 30 | too few records to say anything |
| no recent data | 18 | nothing deposited lately |
| watch | 5 | below 90%, but the uncertainty still spans it |
| no status | 19 | these entries have a problem that makes a verdict meaningless; each page says which |

The split between `declining` and `low coverage` took the longest to get right,
and it is the one worth understanding. A pan-family consensus PCR screened
against an entire genus will look terrible without having changed at all — it
was never covering that diversity. That is `low coverage`. An assay that used to
clear 90% and no longer does is `declining`. Only the second is drift.

## One case where it demonstrably worked

Until October 2026 this tool had never caught a documented failure through its
drift flag — every catch came through `low coverage`, which is a statement about
breadth rather than decay.

Then this one. Scored as of September 2013, using only records deposited before
the paper that reported the problem:

| assay | status | detected |
|---|---|---|
| [Ward 2004](assays/INFLUENZA_A_M1_Ward_2004.md), influenza A M1 | **declining** | 86.2% of 5,847 records |
| [Yang 2014](assays/INFLUENZA_A_M1_Yang_2014.md), the published redesign | **stable** | 91.6% of the same records |

Yang's group redesigned Ward's assay because it was missing circulating strains.
This tool reaches the same conclusion from sequence alone, on records that
predate their paper.

What makes it worth something is the control. Both entries use the same target,
the same archive, the same date window, the same settings. They differ only in
their primer and probe sequences, so nothing else can explain the different
verdicts.

One case is one case. The second drift case I tested it against is a **miss**,
and [the reason](how-it-was-tested.md) tells you more about the method's limits
than the catch does.

## What you get for each assay

Every entry has its own page showing:

- **Detection by deposit year** — with the recent window and the 90% line drawn,
  and record counts underneath, because 100% of three records and 100% of three
  thousand are not the same claim.
- **Where the mismatches sit** on each primer and probe, 3' end on the right.
  Hover any position for the number that matters: detection among records that
  mismatch there versus records that do not.
- **A per-lineage breakdown**, because a pooled percentage hides the clade you
  actually care about.
- **The full arithmetic** behind the verdict, so you can check it by hand.
- **How many records reached the statistics at all**, which is the honest weak
  point of the method.

## Using it on your own assays

Everything is open. The registry is one file per assay, the code is MIT, and a
worked example screens a single assay offline in about a second.

| | |
|---|---|
| code, registry, issues | [github.com/batyanight/assaywatch](https://github.com/batyanight/assaywatch) |
| a full run, readable without installing anything | [example run](https://github.com/batyanight/assaywatch/blob/main/docs/example-run-2026-10-31/report.md) |
| screen one assay offline | [`examples/`](https://github.com/batyanight/assaywatch/blob/main/examples/README.md) |
| every threshold and why it is what it is | [`config.yaml`](https://github.com/batyanight/assaywatch/blob/main/config.yaml) |
| cite this | [10.5281/zenodo.23841793](https://doi.org/10.5281/zenodo.23841793) |

Corrections are welcome, especially to the registry. If an entry misrepresents
your assay, [open an issue](https://github.com/batyanight/assaywatch/issues) —
that is a bug, and it is the kind I most want to hear about.

*Figures throughout this site come from the run dated beside them.*
