"""Reading the retrieve stage's record metadata (``*.meta.tsv.gz``) for one purpose.

Kept free of heavy imports, because both the site-drift report (no scipy) and
the sub-lineage title resolver (lineage.py) read titles from it.
"""

from __future__ import annotations

import csv
import gzip
from pathlib import Path


def read_titles(retrieved_dir: Path, accessions: set[str]) -> dict[str, str]:
    """{accession without version: deposit title} for the accessions asked for.

    Only the requested accessions are kept. The metadata is ~20 MB gzipped
    across 272 files and covers every record ever fetched; building the whole
    map would cost hundreds of megabytes to answer a question about a few
    thousand records.
    """
    out: dict[str, str] = {}
    if not accessions:
        return out
    for meta in sorted(Path(retrieved_dir).rglob("*.meta.tsv.gz")):
        try:
            with gzip.open(meta, "rt", newline="") as fh:
                for row in csv.DictReader(fh, delimiter="\t"):
                    acc = (row.get("accession") or "").split(".")[0]
                    if acc in accessions and acc not in out:
                        title = row.get("title") or ""
                        if title:
                            out[acc] = title
        except (OSError, EOFError, csv.Error):
            # A truncated metadata sidecar must not stop the report; the
            # affected records simply have no organism label.
            continue
    return out
