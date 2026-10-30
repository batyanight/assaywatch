# The collection-year lens goes live across every assay

2026-10-30. `report.collection_sidecar` is set, so the collection-year lens now covers
every assay a run screens, not the 13 whose archives are genome assemblies. This closes the
build half of the window_on work (the design half closed earlier: the lens is a report
section, not a drift switch — `docs/journal/2026-10-30-design-grilled.md` Q1, and
`drift.window_on` is retired).

## What was set

`report.collection_sidecar: data/collection-dates/collection-dates.tsv` — the file
`scripts/backfill_collection_dates.py --window-only` produced. It is gitignored run state,
so a clone or CI without it falls back to the asm-only lens, which is correct and tested.

The sidecar holds **685,734 settled records: 540,087 with a collection date, 145,549 with
none, 30 NCBI would not serve, 67 not accessions**. The fetch was window-scoped, so it
asked only for records whose collection date could still reach a recent window; across the
whole run that is **534,282 of 1,243,065 records (43%) now carrying a collection year**,
and the 57.5% it skipped are provably outside every window and cannot move a lens number.

## The verification that mattered

The lens must move no verdict — it is a view on the same records, never an input to the
drift call. Rendered the 2026-10-27 run twice, sidecar off then on, and compared the drift
status of all **213 assays: zero changed**. The column is richer; every verdict is
identical. Gate green including `pytest -m slow`, since `config.yaml` is hashed (the
`report:` section is deliberately outside the drift hash, so nothing rescreens).

## What this does not do

It does not re-date the drift verdict. The verdict still runs on deposit date by decision;
collection year sits beside it as a lens on how much of a recent fall is sequencing backlog
rather than a change in what circulates. On the 2026-10-27 run the earlier 13-assay reading
already showed the share barely moves while the recent denominator shrinks; the full
coverage now lets a reader see that per assay rather than for assemblies only.
