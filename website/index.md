# AssayWatch

**Checks published PCR and qPCR assays, in silico, against the sequences GenBank
has received since they were designed.**

An assay is designed against the sequences available at the time, then stays in
use for years while new strains keep being deposited, and nobody goes back to
check it against them. When a primer stops matching, the test comes back
negative, and that looks exactly like the target not being there. This matters
most in wildlife and One Health surveillance, where most targets have few
sequences, assays get moved to new host species and regions, and current positive
controls are hard to come by.

AssayWatch keeps a version-controlled registry of 216 published assays, each cited
to its own paper. It screens each assay against the GenBank records of its target
and reports predicted detection **by year of deposit**, so you can watch coverage
change over time instead of reading one number.

[Assay registry](assays/index.md){ .md-button .md-button--primary }
[Known limitations](limitations.md){ .md-button }

---

## How to read a status

A status tells you where to look. It is not a result.

`declining` means an assay deserves a closer look. That call has been tested
against assays whose field performance was published later: **4 of 10 `declining`
calls matched a documented failure** (40%, 95% credible interval 15–70%). The
interval is wide because few follow-up reports exist.

Nineteen thresholds decide every verdict, and all but one were set by inspection
rather than derived from data. [Validation](validation.md) has the full confusion
matrix, including three held-out sets, all of which did worse than the set used
for tuning.

## Registry status, 2026-11-10 run

| status | assays | definition |
|---|---|---|
| stable | 70 | recent detection does not fall below 90% |
| declining | 41 | below 90% and measurably lower than an earlier baseline that exceeded it |
| low coverage | 27 | below 90% with no measurable decline: used beyond what it was designed for, or it never covered the target |
| insufficient data | 36 | too few evaluable records to estimate anything |
| no recent data | 17 | no deposits within the window |
| watch | 6 | below 90% with an interval that still spans it |
| no status | 18 | a verdict would mislead for this entry; each page says why |

The difference between `declining` and `low coverage` matters. A pan-family
consensus PCR screened against a whole genus will look poor without anything having
changed, because it never covered that diversity. Only a fall from a baseline that
used to clear the threshold counts as drift.

## A case it caught

Until October 2026 the drift flag had not identified a single documented failure.
Every case detected came through `low coverage`, which measures breadth rather than
decay over time.

This one is scored as of September 2013, using only records deposited before the
report describing the problem came out:

| assay | status | predicted detection |
|---|---|---|
| [Ward 2004](assays/Influenza_A_virus_M1_Ward_2004.md), influenza A M1 | **declining** | 86.2% of 5,847 records |
| [Yang 2014](assays/Influenza_A_virus_M1_Yang_2014.md), the published redesign | **stable** | 91.6% of the same records |

Yang and colleagues redesigned the Ward assay because it was missing circulating
strains. AssayWatch reaches the same conclusion from sequence alone, using records
older than their paper.

The two entries share a retrieval group, archive, date window and scoring
configuration. Only the oligo sequences differ, so nothing else can explain the
different verdicts. A second drift case in the same held-out set was **not**
detected; [validation](validation.md) explains why.

## What each assay page shows

- **Predicted detection by deposit year**, with the recent window and threshold
  marked and a record count for each year, because 100% of three records and 100%
  of three thousand are very different claims.
- **Where mismatches fall along each oligo**, with the 3′ window marked. Each
  position compares detection in records with a mismatch there against records
  without one.
- **A breakdown by lineage**, where there is more than one.
- **The full arithmetic behind the verdict**, so you can redo it by hand.
- **The share of screened records that reach the statistics**, which is the
  method's main known weakness.

## Availability

| | |
|---|---|
| source code, registry, issue tracker | [github.com/batyanight/assaywatch](https://github.com/batyanight/assaywatch) |
| complete run output, readable without installation | [example run](https://github.com/batyanight/assaywatch/blob/main/docs/example-run-2026-11-01/report.md) |
| offline worked example, single assay | [`examples/`](https://github.com/batyanight/assaywatch/blob/main/examples/README.md) |
| all thresholds with their justification | [`config.yaml`](https://github.com/batyanight/assaywatch/blob/main/config.yaml) |
| archived release, citable | [10.5281/zenodo.23841793](https://doi.org/10.5281/zenodo.23841793) |

Code is MIT licensed; the registry and curated tables are CC-BY-4.0.

Corrections are welcome. If an entry misrepresents a published assay, please
[open an issue](https://github.com/batyanight/assaywatch/issues).

*Figures throughout carry the date of the run that produced them.*
