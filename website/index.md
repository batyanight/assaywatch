# AssayWatch

**Continuous in-silico re-validation of published PCR and qPCR assays against
newly deposited GenBank sequences.**

A diagnostic assay is designed against the sequences available at the time of
design, then used for years while sequence databases accumulate divergent
strains against which it is never re-checked. Loss of primer match produces a
negative result indistinguishable from true absence of the target. The problem
is acute in wildlife and One Health surveillance, where targets are sparsely
sequenced, assays are transferred between host species and regions, and
contemporary positive controls are rarely available.

AssayWatch maintains a version-controlled registry of 218 published assays,
each cited to its source publication, screens every assay against the GenBank
records of its own target, and reports predicted detection **indexed by year of
deposit**, so that loss of coverage is observable as a trend rather than a
single-point estimate.

[Assay registry](assays/index.md){ .md-button .md-button--primary }
[Known limitations](limitations.md){ .md-button }

---

## Interpretation

A status indicates where to direct attention. It is not a result.

`declining` identifies an assay warranting examination. The precision of that
call has been measured against assays whose field performance was subsequently
published: **4 of 10 `declining` calls corresponded to documented failures**
(40%, 95% credible interval 15–70%). The interval is wide because the number of
published follow-up reports is small.

Nineteen thresholds determine every verdict; all but one were set by inspection
rather than derived. [Validation](validation.md) gives the complete confusion
matrix, including three held-out sets, all of which performed worse than the
set used for tuning.

## Registry status, 2026-10-31 run

| status | assays | definition |
|---|---|---|
| stable | 72 | recent detection does not fall below 90% |
| declining | 42 | below 90% and measurably lower than an earlier baseline that exceeded it |
| low coverage | 31 | below 90% without a measurable decline — applied beyond its design range, or never covering the target |
| insufficient data | 30 | too few evaluable records to support an estimate |
| no recent data | 18 | no deposits within the window |
| watch | 5 | below 90% with an interval that still spans it |
| no status | 19 | entry carries a condition under which a verdict would be misleading; stated per page |

The distinction between `declining` and `low coverage` is material. A pan-family
consensus PCR screened against an entire genus will appear to perform poorly
without having changed, because it never covered that diversity. Only a fall
from a baseline that previously exceeded the threshold constitutes drift.

## Demonstrated case

Prior to October 2026 the drift flag had identified no documented failure; every
detected case was attributable to `low coverage`, which measures breadth rather
than temporal decay.

Scored as of September 2013, using only records deposited before publication of
the report describing the problem:

| assay | status | predicted detection |
|---|---|---|
| [Ward 2004](assays/INFLUENZA_A_M1_Ward_2004.md), influenza A M1 | **declining** | 86.2% of 5,847 records |
| [Yang 2014](assays/INFLUENZA_A_M1_Yang_2014.md), the published redesign | **stable** | 91.6% of the same records |

Yang and colleagues redesigned the Ward assay because it was failing to detect
circulating strains. AssayWatch reaches the same conclusion from sequence alone,
using records predating that publication.

The two registry entries share a retrieval group, archive, date window and
scoring configuration, differing only in oligonucleotide sequence; no other
factor accounts for the difference in verdict. A second drift case in the same
held-out set was **not** detected, for reasons given under
[validation](validation.md).

## Per-assay reporting

Each registry entry has a page presenting:

- **Predicted detection by deposit year**, with the recent window and threshold
  marked, and per-year record counts, since 100% of three records and 100% of
  three thousand are not equivalent claims.
- **Mismatch distribution along each oligonucleotide**, with the 3′ terminal
  window marked. Each position reports detection among records carrying a
  mismatch at that position against records that do not.
- **Per-lineage breakdown**, where more than one lineage is represented.
- **Complete verdict arithmetic**, permitting manual recomputation.
- **Proportion of screened records reaching the statistics**, which is the
  principal known weakness of the method.

## Availability

| | |
|---|---|
| source code, registry, issue tracker | [github.com/batyanight/assaywatch](https://github.com/batyanight/assaywatch) |
| complete run output, readable without installation | [example run](https://github.com/batyanight/assaywatch/blob/main/docs/example-run-2026-10-31/report.md) |
| offline worked example, single assay | [`examples/`](https://github.com/batyanight/assaywatch/blob/main/examples/README.md) |
| all thresholds with their justification | [`config.yaml`](https://github.com/batyanight/assaywatch/blob/main/config.yaml) |
| archived release, citable | [10.5281/zenodo.23841793](https://doi.org/10.5281/zenodo.23841793) |

Code is MIT licensed; the registry and curated tables are CC-BY-4.0.

Corrections to registry entries are welcome. If an entry misrepresents a
published assay, please [open an issue](https://github.com/batyanight/assaywatch/issues).

*Figures throughout carry the date of the run that produced them.*
