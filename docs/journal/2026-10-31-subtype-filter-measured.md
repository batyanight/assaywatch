# The subtype filter measured, and set 3's second row disagrees for a reason worth keeping

2026-10-31, overnight. The shared hemagglutinin archive finished fetching (280,786 of
280,786 records), so the before/after check PR #37 owed can be run, and held-out set 3 can
be scored on both its rows for the first time.

## The filter check: it passes, in every case

The prediction on record was that the detected share should **rise** as off-subtype
records leave the denominator while the record count **falls**, and that a share which
**fell** would mean the filter was excluding genuine target records.

| assay | view | status | share | recent n |
|---|---|---|---|---|
| H5 Tsukamoto | old archive | `no recent data` | — | 0 |
| | new, filter off | **`declining`** | 49.8% | 40,452 |
| | new, filter on | **`stable`** | **96.2%** | 20,923 |
| H7 Tsukamoto | old archive | `no recent data` | — | 0 |
| | new, filter off | `low coverage` | 0.5% | 27,780 |
| | new, filter on | **`declining`** | **80.3%** | 157 |
| CDC H3 (v1) | old archive | `no recent data` | — | 0 |
| | new, filter off | `low coverage` | 0.1% | 41,749 |
| | new, filter on | `low coverage` | 0.2% | 27,309 |
| CDC H3_v2 | old archive | `no recent data` | — | 0 |
| | new, filter off | `stable` | 91.0% | 28,994 |
| | new, filter on | `stable` | **92.2%** | 27,323 |

Share up and count down in all four. **No case where the share falls**, so the filter is
not throwing away target records.

**The H5 row is the one that earns the mechanism.** Without the filter it reads
`declining` at 49.8%, which would be a false alarm manufactured entirely by H1, H7 and
other subtypes scoring as failures against an H5 assay. With the filter it reads `stable`
at 96.2%. So the filter does not merely restore recency — it prevents a fabricated decline
on a live, `active` assay.

And the recency is restored: the shared archive holds 26,649 deposits from 2024, 37,858
from 2025 and 30,647 from 2026, where all four assays previously had **zero** records in
any recent window.

## One screen, not two, and the equivalence was tested rather than assumed

`title_requires` selects records per (assay, record), so the rows a filtered screen writes
are exactly the subset of an unfiltered screen's rows whose record carries the subtype.
Rather than screen 280,786 records twice, the filtered view is derived by subsetting.

Checked on a 297-record slice first: the filter-on screen wrote 376 rows, the filter-off
screen 1,188, and subsetting the latter reproduced the former **exactly** — same
(assay, record) keys, same calls. Equal, not approximately equal. That halved about 45
minutes of screening.

## Held-out set 3, both rows scored

    INFLUENZA_A_M1_Ward_2004          2013-09-06  fails  declining     agrees
    INFLUENZA_A_HA_H3_CDC_Shu_2026    2026-10-27  fails  low coverage  DISAGREES

    declining calls that were documented failures (PPV): 1/1 = 100% (95% CrI 15%-100%)
    documented failures caught: 1/2 = 50% (95% CrI 6%-94%)
    failure cases by mechanism: drift 2
    working assays called declining (false alarms): 0/0

So the drift catch count stands at one of two, and the second row is a **miss**.

## Why the Shu row misses, and it is not what I predicted

My first hypothesis was that the drift finished before the comparison window: A21G emerged
in 2020 and reached 96% of circulating viruses by the end of 2021, so if both windows sit
after that, there is no decline left to see. **Measured, and wrong.** Detected share by
deposit year for the two H3 entries:

| year | CDC H3 (v1) | n | H3_v2 | n |
|---|---|---|---|---|
| 2016 | 5.5% | 3,646 | 81.4% | 3,690 |
| 2017 | 1.1% | 5,832 | 88.0% | 5,942 |
| 2019 | **0.4%** | 7,226 | 90.0% | 7,237 |
| 2022 | 0.7% | 7,295 | 86.1% | 7,296 |
| 2025 | 0.2% | 13,737 | 92.6% | 13,762 |
| 2026 | 0.2% | 12,574 | 92.4% | 12,579 |

The v1 assay reads as non-detecting from **2016 onwards** — years before the mutation Shu
2026 describes. There is no decline because there was never a height.

**That looked like a defect in my own entry, so I aligned the oligos against a 2018-deposited
record (MG856325.1) base by base:**

| oligo | strand | mismatches |
|---|---|---|
| v1 forward | + | 0 |
| **v1 reverse** | − | **0** |
| **v1 probe** | + | **1, at position 13: oligo T against template C** |
| v2 probe | + | 0 |

The transcription is right — Shu Table 1 prints `CAG GAT CAC /ZEN/ATA TGG GSC CTG TCC CAG`
for v1 and `...ATA YGG...` for v2, and position 13 is exactly where v2 widens T to Y. So
the entry is faithful and the finding is real: **one central probe mismatch, present since
at least 2016, is enough to take this assay out of `detect` for every record that carries
it**, because for a hydrolysis probe a `reduced` call is not a detection. The dominant
post-2020 profile adds Shu's reverse-primer hit on top (`rev_pen=3 probe_pen=2` on 34,409
records, total 5 against a `reduced_max` of 3.0), which turns `reduced` into `fail`.

## The limitation this exposes, which is the thing to keep

**A two-window contrast cannot see drift in an assay that already scored as
non-detecting.** The CDC H3 assay was FDA-cleared and in clinical use throughout the years
this archive says it detected 0.4% of H3 records, so in vitro it plainly worked. What the
tool measures is its own scoring rule applied to deposited sequence, and under that rule a
single mid-probe mismatch disqualifies detection — so the assay sat at the floor before the
drift began and the drift could not move it further down.

Two existing roadmap items are the same fact seen from other angles: the probe-chemistry
decision that a `reduced` probe call is not a detection (which this row depends on
entirely), and `primer_mid_penalty: 1.0` equalling `detect_max: 1.0` so that one
mid-window mismatch sits exactly on the band boundary. This is a third witness, and the
first where the consequence is a **missed drift case rather than a false alarm**.

It also means the honest statement about Shu 2026 is narrower than the one I put in set 3's
file: the paper's drift is real and documented, and this tool cannot score it, because the
assay's floor under our rule predates it.

## What was run

One retrieve (280,786 records, group `q1f149635cb`), one screen of 1,123,144 rows with the
filter off, the filtered view derived by subsetting, and `retrospective.py` against the old
archives, the unfiltered view and the filtered view. Not a pipeline run; the four influenza
assays only.
