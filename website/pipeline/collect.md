# collect

Consolidates the cached per-archive results into a single table for the run.

Each cached screen is checked against a record of the configuration that
produced it, so a screen remaining from earlier settings is detected here
rather than being combined with current results. The check exists because
stale cached screens once inflated three separate measurements by
approximately two orders of magnitude.

**Output:** `calls.tsv.gz` — 3.0 million rows, approximately 22 MB compressed;
the sole input to every downstream stage.
