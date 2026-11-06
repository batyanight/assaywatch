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

A simulation of dropping them from the verdicts was started and stopped before it returned, so **their effect
on status is unknown**. A fix would need a sequence comparison at report time or a stored map.

## Not done

- `website/data` isn't regenerated. The composition rebuild was stopped at assay 69 of 219, so it restarts
  from nothing.
- `website/index.md` counts need updating after the extract.
- `pytest -m slow` hasn't run on this change, and `calls.py` needs it.
