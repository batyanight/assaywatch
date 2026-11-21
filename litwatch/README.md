# litwatch

> Parked here on the `litwatch-scaffold` branch until the private `litwatch`
> repo exists. Not part of AssayWatch; do not merge into `main`.

Literature Watch: a weekly digest of new papers in three streams
(AssayWatch leads, infectious disease phylodynamics, the AI frontier).
The design lives in the "Literature Watch — PRD" doc.

## Status

Ticket 1 (fetch and deduplicate), first slice only:

- `dedup.py` — `same_doi(a, b)`: two DOIs that differ only in letter case
  are the same paper.
- `tests/test_dedup.py` — the tests for it.

Not built yet: `streams.yml`, `fetch.py`, the rest of `dedup.py`
(preprint vs published version, arXiv versions, `seen.tsv`, AssayWatch DOIs).

## Run the tests

From this `litwatch/` folder, on any machine with Python 3:

```bash
python3 -m unittest discover -s tests -v
```

No environment or packages are needed; the scripts use the standard library only.
