"""Reading the calls table and the deposit dates: one loader, three consumers.

WHY A MODULE OF ITS OWN. These lived in `report.py`, and `sitedrift.py` and
`scripts/retrospective.py` both imported them from there -- so the module that
renders a document was also the project's calls-table I/O library, and its 1,228
lines were the four jobs its own `ReportModel` layer was introduced to separate.
Same move, same reason, as `interval.py` and `signature.py`.

MEMORY IS THE THING TO KNOW HERE. `read_calls` materialises the whole table as
one small dict per row: 2,688,879 rows on 2026-10-22. An earlier version kept
every column and took 3.6 GB; this one keeps the four or five fields anything
downstream reads and interns the footprint string, which brings it to roughly
1-1.5 GB. That is still the largest resident set in the pipeline, it scales as
assays x records, and three rules load it -- `report`, `site_drift` and
`lineage_analysis` -- two of which Snakemake can co-schedule. All three now
declare `resources: mem_mb` for that reason (Snakefile), because on SLURM a
`resources:` block is the sbatch request and an undeclared job is killed rather
than slowed. Nothing here streams or chunks; a registry twice this size needs
that before it needs anything else.
"""

from __future__ import annotations

import csv
import gzip
from pathlib import Path
from typing import Any

from assaywatch.accession import strip_version, version_of
from assaywatch.drift import FOOTPRINT_COLUMNS, FOOTPRINT_REQUIRED, footprint_signature


def _open(path: Path):
    return gzip.open(path, "rt") if str(path).endswith(".gz") else open(path)


def read_calls(path: Path, with_spans: set[str] | None = None) -> list[dict[str, Any]]:
    """The columns the drift statistic needs, one small dict per row.

    Loading every column of a two-million-row calls table as dicts took 3.6 GB;
    nothing downstream reads the other columns. The six mismatch columns are
    folded into ONE interned `footprint` string per row rather than carried as
    six, so the cost is a pointer per row and millions of identical exact-match
    footprints are a single object. A row has no `footprint` key when the columns
    are absent from the table OR the row's own scoring cells are blank (a row from
    an older screen that `collect.concatenate_screens` blank-filled), which
    `drift.assess` reads as "unknown" and not as "all the same".
    """
    with _open(path) as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return []
        ia, ir, ic = header.index("assay_id"), header.index("record_id"), header.index("call")
        span_idx = (
            [header.index(c) for c in ("amplicon_start", "amplicon_end")]
            if with_spans and all(c in header for c in ("amplicon_start", "amplicon_end"))
            else None
        )
        # `exclusion` says why an unusable record was unusable (score.classify_exclusion).
        ie = header.index("exclusion") if "exclusion" in header else None
        # The footprint is known only where the row's own scoring columns are
        # populated (see drift.FOOTPRINT_REQUIRED). Having the six mismatch
        # columns in the HEADER is not enough: `collect.concatenate_screens` unions
        # the headers of old and new screens and blank-fills the cells an older
        # screen never had, so an older screen's rows arrive with all six columns
        # present and empty - indistinguishable from a clean record unless the
        # scoring cells beside them are checked. All six columns or none: a partial
        # footprint would compare unequal to a full one that agrees with it.
        fp_idx = (
            [header.index(c) for c in FOOTPRINT_COLUMNS]
            if all(c in header for c in (*FOOTPRINT_COLUMNS, *FOOTPRINT_REQUIRED))
            else None
        )
        req_idx = [header.index(c) for c in FOOTPRINT_REQUIRED] if fp_idx is not None else []
        rows = []
        for r in reader:
            if not r:
                continue
            row = {
                "assay_id": r[ia],
                "record_id": r[ir],
                "call": r[ic],
                "exclusion": (r[ie] if ie is not None and ie < len(r) else ""),
            }
            if fp_idx is not None and all(i < len(r) and r[i] != "" for i in req_idx):
                row["footprint"] = footprint_signature(r[i] if i < len(r) else "" for i in fp_idx)
            if span_idx is not None and row["assay_id"] in with_spans:
                a, b = (r[i] if i < len(r) else "" for i in span_idx)
                if a and b:
                    row["amplicon_start"], row["amplicon_end"] = a, b
            rows.append(row)
        return rows


def read_dates(retrieved_dir: Path) -> dict[str, str]:
    """{accession without version: deposit date (YYYY-MM-DD)}, newest revision winning."""
    best: dict[str, tuple[str, str]] = {}
    for meta in sorted(retrieved_dir.rglob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                acc = strip_version(row["accession"])
                created = (row.get("created") or "")[:10]
                if not created[:4].isdigit():
                    continue
                updated = row.get("updated") or ""
                if acc not in best or updated > best[acc][0]:
                    best[acc] = (updated, created)
    return {acc: created for acc, (_, created) in best.items()}


def read_years(retrieved_dir: Path) -> dict[str, int]:
    """{accession without version: deposit year}, newest revision winning."""
    return {acc: int(d[:4]) for acc, d in read_dates(retrieved_dir).items()}


def key_calls_by_accession(calls: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Normalise record ids so they join against the metadata, newest version only.

    Newest means the highest `.N` version, not the last row: the pipeline
    concatenates archives group by group, so an older version can come last.
    """
    seen: dict[tuple[str, str], tuple[int, dict[str, Any]]] = {}
    for row in calls:
        acc = strip_version(row["record_id"])
        v = version_of(row["record_id"])
        key = (row["assay_id"], acc)
        if key not in seen or v >= seen[key][0]:
            seen[key] = (v, {**row, "record_id": acc})
    return [row for _, row in seen.values()]
