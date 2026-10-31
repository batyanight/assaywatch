# The lone-anchor test at archive scale: built, measured, shipping OFF (2026-10-24)

Wave 2's named next item (`docs/journal/2026-10-23-wave2-diverged-and-patent.md`, "New items"):
an archive-scale anchor test in `classify_exclusion`, then a rescreen, then a tier-2
re-run. This is that item.

## The defect, restated

`score.classify_exclusion` calls a lone primer site credible when its **per-record**
E-value is under `scoring.max_site_evalue: 0.01`. A 22-mer six mismatches off has E of
about 5e-3 in a 900 bp record, which passes. An archive is thousands of records, so
chance anchors arrive in proportion to its size, and a `diverged` label on one asserts
the assay failed on a record that never held its target. Wave 2 measured it: 55 of Bd's
63 `diverged` records are 2014 JAM81 genome-annotation mRNAs with no ITS locus.

The per-record threshold is not wrong. The axis is: a threshold set per test, applied
across thousands of tests.

## Why Benjamini-Hochberg and not E x record count

The obvious correction is to multiply the per-record E by the number of records the
archive holds. It does not work, and the reason is the case that killed wave 2's first
repair attempt. `RETROVIRUS_RNA_polymerase_SIV_Keele_2009` has real anchors - the
forward primer at two mismatches - on thousands of records of an 8,252-record archive.
Each is about 3e-5, so E x N is around 0.25 and a 0.05 cut would discard the lot, which
are genuine SIV records the assay genuinely fails on. Bd's chance anchors are 55 at
5e-3 in 9,496 records, product 47. A product rule cannot separate 0.25 from 47 in the
right direction.

Step-up BH over the assay's own `no_amplicon` rows can: thousands of small p-values
raise the acceptance threshold for each other and all pass, while a handful of weak
ones ranked among thousands of tests face a threshold of k/m x q and fail. A per-record
E-value is treated as a p-value, which it approximates while E << 1.

## What shipped

- Every `no_amplicon` row now carries `anchor_evalue`, the best lone site's per-record
  E-value, written by `classify_exclusion` (which returns it as a third value) through
  `Call.as_row`. This is the only part that needed a rescreen, because `score.py` is in
  the screen signature's closure.
- `calls.apply_anchor_fdr(rows, cfg)` runs the BH step-up per assay when
  `drift.anchor_fdr` is set, and relabels a `diverged`, `truncated` or `no_pair` anchor
  that does not survive as **`chance_anchor`**. A distinct label rather than `no_site`
  on purpose: it is counted and named in the report's own exclusion breakdown,
  `nested.py` correctly does not read it as a round-1 escape, and
  `count_diverged_as_fail` correctly no longer sees it as `diverged`.
- It is called at the three places that read a calls table - `report.build`,
  `sitedrift`, `scripts/retrospective.py` - so the documents cannot disagree, which is
  the fault `report.assess_as_reported` was written to close.
- A row that recorded no E-value is **never** relabelled. An older screen's `diverged`
  is unknown, and unknown is not chance.
- `drift.anchor_fdr` ships `null`. The label set is unchanged in every shipped run.

Being report-time is the point: the knob costs no rescreen, so tier-2 can price it, and
every future threshold for it is a replay rather than a 12-minute run.

## The rescreen

Full run, `results/2026-10-24/`, **380 of 380 steps, 35m 50s, exit 0**. Retrieval
fetched 3,061 new records, so there are now 392 screens against 356. Verified: with the
new column removed, **all 335 rescreened screens are byte-for-byte what they were
before** (sha256, taken before and after). The 21 orphan archives carry no column
because no live assay asks for them, which is `scripts/orphan_archives.py`'s finding and
not a fault here. One archive was also rescreened with the pre-change code exported
from `e134e92` and diffed column by column: 54 of 54 rows identical.

## What the test does, measured

The discrimination is visible in the anchor E-values themselves, before any threshold
(`diverged` rows only, 2026-10-24 table):

| assay | diverged | E <= 1e-4 | 1e-4 to 1e-3 | E > 1e-3 |
|---|---:|---:|---:|---:|
| `MONKEYPOX_dsDNA_N3R_MGB_Kulesh_2004` | 1,654 | 1,654 | 0 | 0 |
| `Leucocytozoon_cyt_c_Hellgren_2004` | 1,089 | 1,076 | 5 | 8 |
| `Pan_coccidia_SSU_rDNA_..._Garner_2006` | 7,484 | 7,282 | 86 | 116 |
| `RETROVIRUS_RNA_polymerase_SIV_Keele_2009` | 3,927 | 130 | 3,389 | 408 |
| `ENTEROVIRUS_ssRNA_VP3_VP1_round2` | 18,561 | 12,513 | 3,935 | 2,113 |
| `ORTHOREOVIRUS_..._Landolfi_2010_round1` | 229 | 0 | 21 | 208 |
| `CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004` | 63 | 2 | 5 | **56** |

That is wave 2's anchor table recovered from a different direction, and it is the first
time the E-values behind those labels have been on disk at all.

Relabelling, over 2,516,998 rows holding 286,788 lone-anchor rows and 57,542 `diverged`:

| | q = 0.05 | q = 0.01 |
|---|---:|---:|
| rows relabelled `chance_anchor` | 7,206 (2.5% of lone anchors) | 13,693 |
| assays affected | 75 | 127 |
| of those, `diverged` -> `chance_anchor` | 2,794 | 5,465 |
| Bd `diverged` relabelled, of 63 | **50** | 59 |
| SIV Keele `diverged` relabelled, of 3,927 | **0** | 19 |
| Monkeypox N3R, of 1,654 | **0** | 0 |
| Leucocytozoon Hellgren, of 1,089 | **0** | 8 |
| Orthoreovirus Landolfi round1, of 229 | **228** | 229 |

A smaller q relabels **more**, not less, and that is the right direction: rejecting the
null here means "this lone site is real", so a stricter bar for calling a site real
leaves more sites unexplained.

At q = 0.05 the test does what it was built to do. It removes 50 of Bd's 56 weak anchors
and essentially all of Orthoreovirus's - the two chance-dominated cases wave 2 named -
and touches nothing in Monkeypox, Leucocytozoon, Pan-coccidia or SIV Keele, including
the Leucocytozoon catch that the M1 revert turned on.

## The limitation, which is structural and should not be papered over

**BH is a relative criterion, so it is weakest exactly where contamination is the
majority.** `ENTEROVIRUS_ssRNA_VP3_VP1_round2` holds 2,113 `diverged` rows with E above
1e-3, and at q = 0.05 not one of them moves. The arithmetic: with m = 24,097 tests, a
weak anchor ranked near the top of the sort faces k/m x q approaching 0.05, which is
five times **looser** than the per-record 0.01 it already passed. A family dominated by
strong anchors raises the bar for its own weak members.

So this is not a uniformly stricter rule, and it must not be described as one. It is a
rule that catches a minority of chance anchors inside a population of real ones, which
is Bd's shape and the shape wave 2 was looking at. Where the chance anchors are most of
the family, the right instrument is a per-record E-value tightened for the archive's
size, or a credibility test that does not rank sites against each other at all. Neither
is built, and the second is where I would look next.

Three smaller things worth knowing. Most relabelling lands on `truncated` and `no_pair`
rows, which were already outside the drift denominator - at q = 0.05, 2,794 of 7,206
moved rows are `diverged`, so about 60% of the change is invisible to any verdict.
Wave 2's Polyomavirus VP1 prediction is not reproduced, because the entry it measured
(`POLYOMAVIRUS_dsDNA_VP1`) is now in `pending/` and is not screened; the surviving
PREDICT and Johne entries move nothing at q = 0.05. And the two `Morbillivirus_..._P_gene`
entries move 510 rows each, identically, because they store the same oligo pair.

## Tier-2, on the same calls table, six configurations

The knob is report-time, so this is six replays of `scripts/retrospective.py` over
`results/2026-10-24/calls.tsv.gz`, no rescreen. `diverged` means
`count_diverged_as_fail: true`, which is what wave 2 wanted the anchor test for.

| config | failures caught | PPV of `declining` | false alarms on `works` | undecided |
|---|---:|---:|---:|---:|
| shipped | 5/11 | 2/9 | 5/32 | 15 |
| `anchor_fdr: 0.05` | 5/11 | 2/9 | 5/32 | 15 |
| `anchor_fdr: 0.01` | 5/11 | 2/9 | 5/32 | 15 |
| `count_diverged_as_fail` alone | 5/11 | **2/11** | **7/32** | 15 |
| `count_diverged_as_fail` + 0.05 | 5/11 | 2/10 | 6/32 | 15 |
| `count_diverged_as_fail` + 0.01 | 5/11 | 2/9 | 5/32 | 15 |

**Not one case verdict changes under the anchor test alone.** Tier-2 is silent on it,
in both directions, at both thresholds: the same 5 of 11 caught, the same 15 undecided,
the same 49 rows. By the rule written beside `exclude_patent_records` - ship on a sound
mechanism where tier-2 is silent, never where tier-2 contradicts - that makes this
shippable. It stays off anyway, because the measurement below is the more interesting
result and it is the maintainer's call which of the two knobs to spend it on.

**What the test is actually for is repairing `count_diverged_as_fail`.** That switch
alone moves three rows, and they are the rows wave 2 named: it turns two working assays
`declining`, so the `declining` flag's precision falls from 2 of 9 to 2 of 11 and false
alarms rise from 5 to 7 of 32.

| row | shipped | `count_diverged` alone | + `anchor_fdr: 0.05` | + `anchor_fdr: 0.01` |
|---|---|---|---|---|
| `CMV_UL55_gB_Prepens_2007_round2` @2007-07-20 (works) | stable, agrees | **declining, DISAGREES** | **declining, DISAGREES** | stable, agrees |
| `RANAVIRUS_..._MCP_Pallister` @2012-09-30 (works) | watch, agrees | **declining, DISAGREES** | watch, agrees | watch, agrees |
| `RANAVIRUS_..._MCP_Pallister` @2017-07-13 (partial) | stable, weaker | watch, weaker | stable, weaker | stable, weaker |

The anchor test at q = 0.05 repairs the Ranavirus rows and leaves the CMV one broken; at
**q = 0.01 the matrix is identical to shipped, row for row, while `diverged` records are
being counted as failures.** So the two switches together do what wave 2 hoped
`count_diverged_as_fail` alone would do, at no measured cost on the development set -
and that is also the one place in this measurement where 0.05 and 0.01 can be told
apart.

Read that with the set's own limits in mind. Those 49 cases collapse to about seven
independent failure events, the PPV's 95% interval runs from 6% to 55%
(`docs/journal/2026-10-23-baseline.md`), and a two-false-alarm delta sits well inside it. This
is "no measured harm", not "a measured gain".

### Why Bd stays a miss either way, which is the point

Bd's `no_amplicon` rows are **8,857 `no_site`, 398 `truncated`, 63 `diverged`**, against
174 `detect` and 1 `fail`. Counting `diverged` as failure pools to 174/238 = 73.1%, well
under the threshold - wave 2's observation that the switch would flag Bd on the strength
of protein-coding transcripts. With the anchor test at q = 0.05 removing 50 of those 63,
the pool becomes 174/188 = 92.6%, back above it. (Pooled arithmetic over all years; the
verdict uses the recent window, so these are not the numbers in the report.)

So the anchor test does **not** rescue the Bd validation case. It removes the false route
by which `count_diverged_as_fail` would have appeared to catch it. Bd's real failure
lives in the 8,857 `no_site` records, outside the evaluable set entirely, which is what
`docs/journal/2026-10-23-wave3-bd-miss.md` concluded and what no denominator switch can reach.

## What is still open

> *History, as of 2026-10-24. The live list is `ROADMAP.md`, the only to-do file
> in the repository; anything below that is still open was lifted into it.*

- **Deciding the threshold.** 0.05 and 0.01 differ by a factor of two in rows moved
  (7,206 against 13,693). Tier-2 separates them only in the paired configuration above,
  on one row, which is thin evidence for a threshold. If the knob is ever turned on, the
  choice wants the bench panels or the held-out set.
- **The majority-contamination case** above (`ENTEROVIRUS_ssRNA_VP3_VP1_round2`), which
  this mechanism cannot address by construction.
- **The two switches as a pair.** `count_diverged_as_fail: true` with
  `anchor_fdr: 0.01` is the configuration this measurement actually recommends, and it
  is a denominator change, so it is a maintainer's decision and not made here.
