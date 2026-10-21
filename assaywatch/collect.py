"""Gather the cached per-archive screens into one calls table.

This was a `run:` block inside the Snakefile, which meant none of it could be
imported and none of it was tested - including the part that exists for the one
case where it matters. It lives here so it can be.

The case: a cached screen written before a column was added, meeting one written
after (`exclusion`, `pair_evalue`, the `--thermo` columns, and the footprint
columns that `drift.py` reads have each arrived this way). Cached screens are
kept on purpose, since a week's run should screen only the archives that are new,
so old and new schemas meet in every cumulative report. Plain concatenation would
shift the older file's rows a column sideways and quietly corrupt every call in
them. Rows are therefore written by column NAME.

The second case: a cached screen holding assay ids the registry no longer has.
`results/2026-10-20/calls.tsv.gz` carried three, beside their renamed
counterparts, because one archive's screen from 2026-10-18 was reused without
its `--only` list being re-checked (Snakemake's metadata for it came from a
different install). Every count downstream inherited them: "208 assays screened"
double-counted three. Snakemake's invalidation is the wrong place to rely on, so
the collector checks every id against the assays the run screens, and refuses
rather than drops: a stale screen's rows are missing for the assay's NEW id too,
so dropping the orphans would quietly leave that archive out of the renamed
assay's numbers.
"""

from __future__ import annotations

import csv
import gzip
import io
from collections import Counter
from collections.abc import Collection, Sequence
from pathlib import Path

# What csv.DictWriter writes by default, and so what every cached screen uses.
# Stated rather than inherited, because the reconciling path writes rows through
# a csv writer and the copying path copies bytes, and the two have to agree.
LINE_END = "\r\n"


def stem_order(path: Path) -> tuple[str, int]:
    """`2026-10-04` < `2026-10-04_2` < `2026-10-04_10`: archive names in fetch order.

    A second fetch on the same day gets a `_2`, `_3` suffix, so the stems sort as
    text in the wrong order (`_10` before `_2`). Order matters because archives
    are concatenated oldest first, so that the newest version of an accession is
    the one that survives deduplication downstream.
    """
    stem = path.name.split(".")[0]
    day, _, n = stem.partition("_")
    return (day, int(n or 1))


def _check_terminated(path: Path) -> None:
    """Refuse a screen whose last row has no line ending.

    The copying path appends the next file straight after this one, so an
    unterminated final row would have the next file's header glued onto it:
    one corrupt row, silently, in the middle of a report's input. The
    reconciling path is no better, since a row cut short mid-field reads as a
    valid row with its remaining columns empty. Neither is something to repair -
    a screen that stopped mid-write is unreliable throughout - so this names the
    file and says what to do.
    """
    if path.stat().st_size == 0:
        return
    with open(path, "rb") as fh:
        fh.seek(-1, 2)
        if fh.read(1) not in (b"\n", b"\r"):
            raise ValueError(
                f"{path} does not end with a line break, so its last row may be cut short. "
                f"Delete it and rerun to screen that archive again."
            )


def read_header(path: Path) -> list[str]:
    """A screen's column names; empty for a zero-byte file."""
    with open(path) as fh:
        return next(fh, "").rstrip("\r\n").split("\t")


def orphan_ids(path: Path, known_ids: Collection[str]) -> Counter[str]:
    """Rows per assay_id in one screen whose id is not in `known_ids`.

    Parsed with the csv module rather than split per line, so a quoted field
    holding a line break cannot be misread as a row. A screen with no
    `assay_id` column cannot be checked and is refused the same way.
    """
    known = frozenset(known_ids)
    with open(path, newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return Counter()
        if "assay_id" not in header:
            raise ValueError(
                f"{path} has no assay_id column, so its rows cannot be checked against the registry."
            )
        i = header.index("assay_id")
        return Counter(row[i] for row in reader if row and row[i] not in known)


def check_assay_ids(paths: Sequence[Path], known_ids: Collection[str]) -> None:
    """Refuse screens holding assay ids outside `known_ids`, naming each file and id.

    Raises before anything is written, so a refused collect leaves no calls
    table behind for a later stage to pick up.
    """
    found = {path: c for path in paths if (c := orphan_ids(path, known_ids))}
    if not found:
        return
    lines = [
        f"  {path}: " + ", ".join(f"{aid} ({n} rows)" for aid, n in sorted(c.items()))
        for path, c in found.items()
    ]
    raise ValueError(
        f"{len(found)} cached screen(s) hold assay ids that are not current registry assays "
        f"(renamed, removed or deprecated):\n"
        + "\n".join(lines)
        + "\nThese screens are stale. Delete them and rerun to screen those archives again; "
        "dropping the rows instead would leave the archives out of the current assays' numbers."
    )


def unified_columns(headers: Sequence[Sequence[str]]) -> list[str]:
    """Every column seen, in the order first met.

    First-seen order keeps the columns of the oldest screen where they were,
    with each later-added column appended, so a table built from consistent
    inputs has exactly the header they share.
    """
    columns: list[str] = []
    for h in headers:
        columns += [c for c in h if c and c not in columns]
    return columns


def concatenate_screens(
    paths: Sequence[Path], out_path: Path, known_ids: Collection[str] | None = None
) -> list[str]:
    """Write one gzipped calls table from many cached screens; return its columns.

    `paths` are taken in the order given and written in that order - the caller
    passes them oldest first, which is what lets the newest version of an
    accession win downstream.

    When every screen has the same columns in the same order, which is nearly
    always, rows are copied through untouched. Otherwise they are rewritten by
    column name, and a column a screen never had is left empty rather than
    guessed.

    With `known_ids`, every row's assay_id must be one of them (see
    `check_assay_ids`); the pipeline always passes it. None skips the check,
    for callers that are not collecting a run.
    """
    paths = [Path(p) for p in paths]
    for path in paths:
        _check_terminated(path)
    if known_ids is not None:
        check_assay_ids(paths, known_ids)
    headers = [read_header(path) for path in paths]
    columns = unified_columns(headers)
    # mtime=0 and no stored file name: the same screens give the same BYTES whenever they are
    # collected, which `gzip.open` does not (it stamps the clock into the header). That makes
    # "the output is unchanged" a checkable fact with cmp or a hash, instead of one that only
    # holds after decompressing.
    with (
        open(out_path, "wb") as raw,
        gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as gz,
        io.TextIOWrapper(gz, encoding="utf-8", newline="") as out,
    ):
        out.write("\t".join(columns) + LINE_END)
        for path, header in zip(paths, headers, strict=True):
            with open(path, newline="") as fh:
                next(fh, None)
                if header == columns:
                    out.writelines(fh)  # the usual case: same columns, copy as is
                else:
                    w = csv.DictWriter(out, columns, delimiter="\t", restval="", lineterminator=LINE_END)
                    w.writerows(csv.DictReader(fh, fieldnames=header, delimiter="\t"))
    return columns
