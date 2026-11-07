# 2026-11-06 — RefSeq copies of GenBank records were counted as separate deposits

**Finding: on the 2026-11-01 calls, 8,191 assay-level `NZ_` and GenBank pairs give identical calls, so they
are one deposit counted twice. Collapsing them moves two statuses, and `NC_` copies are a second, wider
class that is measured but not fixed.** The `NZ_` fix is committed on branch `refseq-twins`. The site data
isn't regenerated, so nothing published has changed. The session stopped here on the maintainer's request.

## The `NZ_` fix

`key_calls_by_accession` drops an `NZ_` row when its GenBank source is in the same assay's calls, and keeps
the GenBank row for its original date. `accession.refseq_source` holds the rule. Every verdict and the
composition stage read through that function.

Measured with a site extract to a scratch directory, against `main`. 14 assays change, largest first:

| assay | records removed | recent before | recent after | status |
|---|---|---|---|---|
| MTB IS6110 | 472 of 4,012 | 274/274 | 167/167 | stable, unchanged |
| MTB IS1081 | 377 of 1,451 | 287/287 | 206/206 | no status, unchanged |
| *Mycoplasma* Rebelo Myco16_23S | 196 of 661 | 56/138 | 39/81 | declining, unchanged |
| *Leptospira* lipL32 | 180 of 1,937 | 406/414 | 368/376 | stable, unchanged |
| Messmer round 1 | 124 of 814 | 35/85 | 21/49 | low coverage, unchanged |
| *V. coralliilyticus* vcpA vcpAF | 16 of 35 | 16/16 | 9/9 | **stable to insufficient data** |
| *V. coralliilyticus* vcpA vcpARTF | 16 of 35 | 16/16 | 8/9 | **stable to insufficient data** |

*C. psittaci* recent rises from 15/15 to 19/19. That's expected: with copies gone the 24-month window falls
short of 15 records, so the existing rule widens it to 60 months.

## `NC_` copies: measured, not fixed

An `NC_`, `AC_` or `NG_` number doesn't name its source, so the accession can't show the pair. By whole
sequence within each archive group, 3,614 of 3,708 such records are identical to a non-RefSeq record, for
example `NC_004003` and `AY077835`. These counts are records in archives, not calls. Identical sequence doesn't
strictly prove a RefSeq copy, since a separate deposit can match too.

A simulation of dropping them from the verdicts was started and stopped before it returned; it was rerun the
same evening, below. A fix would need a sequence comparison at report time or a stored map.

## `NC_` copies: the simulation, and one more status

Method: a blake2b digest of each whole sequence across all archives; a row dropped when its `NC_`, `AC_` or
`NG_` record has the same digest as a non-RefSeq record in the same assay's calls; two site extracts to a
scratch directory, on this branch, with and without those rows. That removes 6,529 (assay, record) pairs in 177
assays. **One status moves on top of the `NZ_` fix.**

| assay | recent before | recent after | status |
|---|---|---|---|
| `Orthobunyavirus_S_Briese_2007_BUNS_5_U_6` | 4/15 | 1/10 | **low coverage to insufficient data** |
| `Orthobunyavirus_M_Briese_2007_M3560_F` | 12/20 | 10/15 | low coverage, unchanged |
| `Orthobunyavirus_L_Briese_2007` | 3/23 | 2/19 | low coverage, unchanged |
| `Rhabdoviridae_L_Bourhy_2005_round2` (nest) | 906/1263 | 901/1239 | declining, unchanged |
| `Paramyxoviridae_L_Tong_2008_round2` (nest) | 2449/3958 | 2448/3914 | low coverage, unchanged |

Recent counts change in 25 assays and 6 nests: most of these copies are old. The per-year charts of all 177
weren't compared. Called records with a twin, by prefix: `NC_` 6,401 of 6,577, `AC_` 100 of 127, `NG_` 28 of 28,
`NR_` 489 of 690, `NW_` 432 of 455, `NM_` 130 of 4,244, `XM_` 12 of 48,799, `XR_` 2 of 306. `NR_` and `NW_` weren't in
the simulation.

Decided by the maintainer: fix with a stored map, on whole-sequence identity, published with the release's
frozen run (`ROADMAP.md`, "Release plan").

## The map, built

Adding `NR_` and `NW_` removes 921 more pairs (7,450 in 186 assays) and moves no status: recent counts change
in 3 assays, by one record each. `refseq_twins.build` found 3,285 curated records with a twin over the 9.3 GB
of archives, in 154 s on 6 workers, 0.67 GB in the largest process. An extract through the module equals the
simulation's `run.json` byte for byte, so the two independent routes agree. 1,394,917 accessions were checked.

## Not done

- `website/data` isn't regenerated. The composition rebuild was stopped at assay 69 of 219, and it now waits
  for the frozen run.
- `website/index.md` counts need updating after the extract.

`pytest -m slow` passed on this change on 2026-11-06 (12 tests), with the full suite (2,160), the validator, ruff
and `check_citations`.
