"""Reading the retrieve stage's record metadata (``*.meta.tsv.gz``) for one purpose.

Kept free of heavy imports, because both the site-drift report (no scipy) and
the sub-lineage title resolver (lineage.py) read titles from it.
"""

from __future__ import annotations

import csv
import gzip
import re
from pathlib import Path

from assaywatch.accession import strip_version

# esummary's <Extra> carries the authoritative patent-division marker
# (`|pat|JP|2021522784|5` against `|gb|` for an ordinary record), and that is what
# retrieve.py records in the `is_patent` column. The patterns below are the
# fallback for archives fetched before that column existed. Two title forms name
# the patent: the citation as the whole title ("JP 2021522784-A/5: SYNTHETIC
# CHIMERIC VACCINIA VIRUS") and the citation after a fixed phrase ("Patent
# application sequence for WO 2026009883-A/7").
#
# MEASURED COVERAGE, archive of 1,530,526 records, 2026-10-20. Patent records
# whose title names the patent: 21,769 of the first form, 152 of the second. A
# third class carries no patent marker in the title at all, only the invention
# name ("Modified Microbial Nucleic Acid", "RESEQUENCING PATHOGEN MICROARRAY"):
# 517 archived records sit under accession prefixes that carry known patents and
# have such titles, and all 114 of a random sample of them came back `|pat|` from
# esummary. So the title fallback misses roughly 3% of patent records and no
# pattern can fix that class — only the column can. A one-off `is_patent`
# backfill sidecar, as data/retrieved/.meta.taxid.backfill.tsv.gz already does
# for taxids, is the clean fix; until then read_patent_accessions undercounts on
# pre-column archives, never over-counts (checked against <Extra> on 300
# records: 150 title matches all `|pat|`, 150 non-matches none).
PATENT_TITLE = re.compile(r"^(?:[A-Z]{2} [\d/]+-[A-Z]\d*/\d+:|Patent application sequence for )")


def looks_like_patent(title: str) -> bool:
    """True if the deposit title names a patent (GenBank patent division).

    Only as good as the title: see the measured coverage above, and prefer the
    `is_patent` column, which comes from GenBank's own division marker.
    """
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
                    acc = strip_version(row.get("accession") or "")
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
                    acc = strip_version(row.get("accession") or "")
                    if acc not in accessions:
                        continue
                    flag = row.get("is_patent")
                    if flag == "1" or (flag is None and looks_like_patent(row.get("title") or "")):
                        out.add(acc)
        except (OSError, EOFError, csv.Error):
            continue
    return out
