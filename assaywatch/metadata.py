"""Reading the retrieve stage's record metadata (``*.meta.tsv.gz``) for one purpose.

Kept free of heavy imports, because both the site-drift report (no scipy) and
the sub-lineage title resolver (lineage.py) read titles from it.
"""

from __future__ import annotations

import csv
import gzip
import re
from pathlib import Path

# A patent-division title is the patent itself: "JP 2021522784-A/5: SYNTHETIC
# CHIMERIC VACCINIA VIRUS". esummary's <Extra> carries the authoritative marker
# (`|pat|JP|2021522784|5` against `|gb|` for an ordinary record), and that is what
# retrieve.py records in the `is_patent` column. This pattern is for archives
# fetched before that column existed: on 300 records sampled from the archive
# 2026-10-19, 150 title matches and 150 non-matches, it agreed with <Extra>
# every time.
PATENT_TITLE = re.compile(r"^[A-Z]{2} [\d/]+-[A-Z]\d*/\d+:")


def looks_like_patent(title: str) -> bool:
    """True if the deposit title is a patent citation (GenBank patent division)."""
    return bool(PATENT_TITLE.match(title or ""))


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


def read_patent_accessions(retrieved_dir: Path, accessions: set[str]) -> set[str]:
    """The subset of `accessions` whose records are GenBank patent-division deposits.

    Reads the `is_patent` column written by retrieve.py, falling back to the
    deposit title for archives fetched before that column existed (see
    looks_like_patent above). Unversioned accessions, as read_titles uses.
    """
    out: set[str] = set()
    if not accessions:
        return out
    for meta in sorted(Path(retrieved_dir).rglob("*.meta.tsv.gz")):
        try:
            with gzip.open(meta, "rt", newline="") as fh:
                for row in csv.DictReader(fh, delimiter="\t"):
                    acc = (row.get("accession") or "").split(".")[0]
                    if acc not in accessions:
                        continue
                    flag = row.get("is_patent")
                    if flag == "1" or (flag is None and looks_like_patent(row.get("title") or "")):
                        out.add(acc)
        except (OSError, EOFError, csv.Error):
            continue
    return out
