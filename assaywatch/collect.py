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

The third case, and why `write_provenance` exists: a calls table could not say
what produced it. `results/2026-10-18/calls.tsv.gz` was screened under a scoring
override that was reverted the next day, and the only way anyone established
that was to notice a commit landing three minutes after the run finished. The
sidecar records it mechanically instead.

What the sidecar deliberately does NOT claim is one set of settings for the
table. A calls table is a mosaic: cached screens are kept on purpose, so a run
mixes archives screened today with archives screened three weeks ago under
whatever the config said then, and a single "produced under" line would be
false for most of the rows. What is knowable from here is per-archive - when
each screen was written, how many rows it contributed, which assays it covers -
plus the signature the pipeline expects for it NOW. A screen whose mtime
predates a settings change is exactly the shape of the 2026-10-18 bug, and the
spread of those mtimes is the number that makes it visible.
"""

from __future__ import annotations

import csv
import gzip
import io
import json
from collections import Counter
from collections.abc import Collection, Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
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


@dataclass(frozen=True)
class ScreenStats:
    """What one parse of a cached screen yields: its rows, assays and orphans.

    One pass serves both consumers - the assay-id guard below and the
    provenance sidecar - because parsing all 311 screens costs about 5 seconds
    and doing it twice is 5 seconds for nothing.
    """

    rows: int
    assays: frozenset[str]
    orphans: Counter[str]


def screen_stats(path: Path, known_ids: Collection[str] | None = None) -> ScreenStats:
    """Row count, assay ids and non-registry ids in one screen.

    Parsed with the csv module rather than split per line, so a quoted field
    holding a line break cannot be misread as a row - `reason` can hold one. A
    screen with no `assay_id` column cannot be checked and is refused.
    """
    known = frozenset(known_ids) if known_ids is not None else None
    with open(path, newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return ScreenStats(0, frozenset(), Counter())
        if "assay_id" not in header:
            raise ValueError(
                f"{path} has no assay_id column, so its rows cannot be checked against the registry."
            )
        i = header.index("assay_id")
        seen: Counter[str] = Counter()
        rows = 0
        for row in reader:
            if not row:
                continue
            rows += 1
            seen[row[i]] += 1
    orphans = Counter({a: n for a, n in seen.items() if a not in known}) if known is not None else Counter()
    return ScreenStats(rows, frozenset(seen), orphans)


def orphan_ids(path: Path, known_ids: Collection[str]) -> Counter[str]:
    """Rows per assay_id in one screen whose id is not in `known_ids`."""
    return screen_stats(path, known_ids).orphans


def check_assay_ids(paths: Sequence[Path], known_ids: Collection[str]) -> None:
    """Refuse screens holding assay ids outside `known_ids`, naming each file and id.

    Raises before anything is written, so a refused collect leaves no calls
    table behind for a later stage to pick up.
    """
    _raise_for_orphans({path: c for path in paths if (c := orphan_ids(path, known_ids))})


def _raise_for_orphans(found: Mapping[Path, Counter[str]]) -> None:
    """The refusal message for `check_assay_ids`, shared with the single-parse path."""
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


def _stamp(ts: float) -> str:
    """A timestamp in LOCAL time with its offset: `2026-10-20T21:53:17-04:00`.

    Unambiguous, and in the same frame as the run dates these are read against.
    In UTC the 2026-10-20 run's screens read `2026-10-21T01:53`, which invites
    exactly the wrong comparison when the question is which run wrote a screen.
    """
    return datetime.fromtimestamp(ts, UTC).astimezone().isoformat(timespec="seconds")


def write_provenance(
    paths: Sequence[Path],
    out_path: Path,
    *,
    run_date: str = "",
    expected_signatures: Mapping[str, str] | None = None,
    stats: Mapping[Path, ScreenStats] | None = None,
    extra: Mapping[str, object] | None = None,
) -> dict:
    """Write `<calls stem>.provenance.json` beside the calls table; return its content.

    `expected_signatures` maps an archive's `<taxid>/<group>` to the signature
    the pipeline expects for it now (the Snakefile's `screen_signature`). It is
    what SHOULD have produced that screen, not what did: a cached screen carries
    no record of its own settings, which is the gap this file makes visible
    rather than closes. `stats` passes in the counts already parsed by the
    assay-id guard, so nothing is read twice.
    """
    screens = []
    for path in paths:
        st = path.stat()
        key = "/".join(path.parts[-3:-1])  # <taxid>/<group>
        s = (stats or {}).get(path) or screen_stats(path)
        screens.append(
            {
                "path": str(path),
                "group": key,
                "screened_at": _stamp(st.st_mtime),
                "bytes": st.st_size,
                "rows": s.rows,
                "assays": len(s.assays),
                "expected_signature": (expected_signatures or {}).get(key, ""),
            }
        )
    written = sorted(s["screened_at"] for s in screens)
    doc = {
        "calls_table": out_path.name,
        "run_date": run_date,
        "collected_at": _stamp(datetime.now(UTC).timestamp()),
        "screens": len(screens),
        "rows": sum(s["rows"] for s in screens),
        # The forensic number: how far apart the oldest and newest screen in this
        # table were written. A wide span is not an error - caching is the point -
        # but it is what says the table cannot have one set of settings.
        "screened_first": written[0] if written else "",
        "screened_last": written[-1] if written else "",
        **dict(extra or {}),
        "note": (
            "expected_signature is what this pipeline expects for the group NOW. A cached "
            "screen records no signature of its own, so a screen written before a settings "
            "change still reads as expected here; its screened_at is the evidence."
        ),
        "screen_inventory": screens,
    }
    sidecar = out_path.with_name(out_path.name.split(".")[0] + ".provenance.json")
    sidecar.write_text(json.dumps(doc, indent=1, sort_keys=False) + "\n")
    return doc


def concatenate_screens(
    paths: Sequence[Path],
    out_path: Path,
    known_ids: Collection[str] | None = None,
    provenance: Mapping[str, object] | None = None,
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

    `provenance` (any mapping, passed to `write_provenance` as keyword
    arguments) also writes the sidecar, reusing the guard's single parse rather
    than reading every screen a second time.
    """
    paths = [Path(p) for p in paths]
    for path in paths:
        _check_terminated(path)
    stats: dict[Path, ScreenStats] = {}
    if known_ids is not None or provenance is not None:
        stats = {path: screen_stats(path, known_ids) for path in paths}
    if known_ids is not None:
        _raise_for_orphans({p: s.orphans for p, s in stats.items() if s.orphans})
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
    if provenance is not None:
        # After the table, so a sidecar never describes a table that failed to write.
        write_provenance(paths, Path(out_path), stats=stats, **provenance)
    return columns
