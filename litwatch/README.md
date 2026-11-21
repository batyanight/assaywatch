# litwatch

> Parked here on the `litwatch-scaffold` branch until the private `litwatch`
> repo exists. Not part of AssayWatch; do not merge into `main`.

Literature Watch: a weekly digest of new papers in three streams
(AssayWatch leads, infectious disease phylodynamics, the AI frontier).

## Where the PRD is

The design is the "Literature Watch — PRD" doc, a private Claude artifact
(only its owner can open the link):
<https://claude.ai/artifact/1A4PVgjGWbm7cxssakgvH3>

It is deliberately not copied into this public repo. The build plan there has
six tickets; this folder is the first slice of ticket 1.

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
