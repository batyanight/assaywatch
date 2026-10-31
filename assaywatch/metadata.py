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

# Where assemblies.py puts the BioSample collection date inside the title, for archives
# written before the `collected` column existed (2026-10-30).
COLLECTED_IN_TITLE = re.compile(r"; collected (?P<date>[^;]*)$")
# A collection date is kept only as a YEAR. GenBank and BioSample dates arrive as
# 2010-05-13, 2010-05, 2010, 13-May-2010, May-2010, "missing", "not collected",
# "2010/2011". The lens that reads them works in years (decided 2026-10-30,
# docs/journal/2026-10-30-design-grilled.md Q2): no invented days, and a RANGE is
# undatable to a year rather than taken at its first year.
#
# The day in the day-month-year form is optional because it is optional in the data: the
# nuccore backfill measured the bare month-year spelling at 156 of the first 3,663 dates
# GenBank served, and the first version of this pattern silently dropped every one of them.
_YEAR_ONLY = re.compile(r"^(?:(?:\d{1,2}-)?[A-Za-z]{3}-)?(\d{4})(?:-\d{2}(?:-\d{2})?)?(?:T.*)?$")


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


def collection_year(text: str | None) -> int | None:
    """The four-digit year of a BioSample collection date, or None when it has none.

    Accepts ISO prefixes (2010, 2010-05, 2010-05-13, with or without a time) and the
    day-month-year form (13-May-2010). Anything else -- "missing", "not collected", a
    range such as 2010/2011 -- is None. See `_YEAR_ONLY` for why a range is not a year.
    """
    m = _YEAR_ONLY.match((text or "").strip())
    return int(m.group(1)) if m else None


def read_collection_years(
    retrieved_dir: Path,
    accessions: set[str],
    *,
    sidecar: Path | None = None,
) -> dict[str, int]:
    """{accession as the caller spelled it: collection year}, for the records asked for.

    Two sources, in order. The `sidecar` is what `scripts/backfill_collection_dates.py`
    fetched from the GenBank flatfiles, and it covers every record a run screened, nuccore
    included; the retrieval archives carry a collection date only for `asm` records, which
    is 13 assays of 214. So the sidecar answers first and the archives fill its gaps. A
    sidecar row that settled with no date, or that NCBI would not serve, is an answer and
    not a gap: it is left out of the result like any undatable record, and the archives are
    not consulted for it, because they have nothing to say about a nuccore accession.

    From the archives, reads the `collected` column where it exists and the
    `; collected ...` tail of the title where it does not (archives written before
    2026-10-30). Only records with a four-digit collection year appear; the caller counts
    the rest as undatable.

    Keys are spelled the way the caller asked. An accession matches with or without its
    version, so a caller holding versioned nuccore record ids and one holding bare assembly
    accessions both get keys they can look up directly.
    """
    out: dict[str, int] = {}
    if not accessions:
        return out
    bare = {strip_version(a): a for a in accessions}

    def asked_as(acc: str) -> str | None:
        """The caller's own spelling of `acc`, or None if they did not ask for it."""
        return acc if acc in accessions else bare.get(strip_version(acc))

    answered: set[str] = set()
    if sidecar is not None and Path(sidecar).exists():
        with Path(sidecar).open(newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                key = asked_as((row.get("accession") or "").strip())
                if key is None:
                    continue
                answered.add(key)
                year = collection_year(row.get("collection_date"))
                if year is not None:
                    out[key] = year
    for meta in sorted(Path(retrieved_dir).rglob("asm/*.meta.tsv.gz")):
        try:
            with gzip.open(meta, "rt", newline="") as fh:
                for row in csv.DictReader(fh, delimiter="\t"):
                    key = asked_as(row.get("accession") or "")
                    if key is None or key in out or key in answered:
                        continue
                    acc = key
                    text = row.get("collected")
                    if text is None:
                        m = COLLECTED_IN_TITLE.search(row.get("title") or "")
                        text = m.group("date") if m else ""
                    year = collection_year(text)
                    if year is not None:
                        out[acc] = year
        except (OSError, EOFError, csv.Error):
            continue
    return out
