# collect

Merges the cached per-archive results into one table for the run.

Each cached screen is checked against a record of the configuration that
produced it. A screen left over from earlier settings is caught here and not
mixed in with current results. The check exists because stale cached screens
once inflated three separate measurements by about two orders of magnitude.

**Output:** `calls.tsv.gz` — 3.0 million rows, about 22 MB compressed;
the only input to every later stage.
