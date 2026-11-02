# Deposit date is not collection date: a quarter of assembly records arrive ten or more years late

2026-10-27. The drift window is defined on deposit date, because that is what every
nuccore record carries. The roadmap item: `collection_date` is already retrieved for
`asm` groups and then unused, so a 2025 deposit of 1990s isolates enters the recent
window as current diversity. Before building anything, measure how often that happens.

    python -I <scratch>/collection_dates.py data/retrieved

Over every assembly-group metadata file on disk, deduplicated by accession, reading the
`collected <date>` token `assemblies.py` writes into each title and comparing its year
with the `created` (deposit) year:

| | |
|---|---|
| assembly records | 1,447 |
| with a collection year | 1,001 (69.2%); 444 `missing`, 2 `Unknown` |
| deposit year − collection year, median | **5** |
| mean | 9.8 |
| deposited ≥ 2 years after collection | 871 of 1,001 (87.0%) |
| ≥ 5 years | 529 (52.8%) |
| **≥ 10 years** | **259 (25.9%)** |
| ≥ 20 years | 98 (9.8%) |
| collection after deposit (bad data) | 0 |

**Not immaterial.** The item's step one was "measure; if small, close it". A quarter of
dated assembly records were collected ten or more years before they were deposited, and
one in ten twenty or more. For a bacterial target whose archive is built from complete
genomes, "recent deposits" is to a measurable degree a sequencing-backlog signal and
not a circulating-diversity signal, and a 24-month window on deposit date windows the
wrong thing for those records.

## What this does and does not reach

**It reaches the `asm` groups only.** 1,447 records against 2.72M calls in a run; the
assembly groups are the bacterial complete-genome retrievals, cut to amplicon windows.
Every nuccore record — the other 99.9% of the table — carries no collection date in
the metadata this pipeline keeps, because `retrieve.py` reads `esummary` fields and
collection date is a source-feature qualifier (`/collection_date`) on the GenBank record
itself. Getting it for nuccore means a second fetch (`efetch -format gb` or the
`biosample` route) per record, and a re-fetch of every archive, which is the cost that
has kept it out.

**So the honest shape of the fix has two steps and this entry authorises neither.**

1. For `asm` records: carry `collection_date` as a metadata column (it is already
   parsed; it is only written into the title string), and let `drift` window on it
   where present — a config switch, `drift.window_on: deposit | collection`, default
   `deposit`, with this measurement in its comment. Records without a collection date
   fall back to deposit date and are counted so the report can say how many.
2. For nuccore records: a retrieval change plus a re-fetch, to be priced before it is
   built. Until then a mixed window (collection for 0.1% of records, deposit for the
   rest) would be a different kind of wrong, and step 1 has to say so in the report.

The roadmap item moves from "measure" to "build step 1, price step 2", with these
numbers behind it.
