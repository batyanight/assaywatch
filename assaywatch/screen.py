"""Screen one or more registry assays against a FASTA and write a TSV of calls.

    python -m assaywatch.screen registry/CHYTRID_Bd_*.yaml records.fasta -o calls.tsv
    python -m assaywatch.screen registry/ records.fasta.gz --config config.yaml

One row per (assay, record). Columns are defined by Call.as_row().

Large archives can be screened across processes with --workers N. Records are
handed out in batches of roughly --chunk-bp bases, and each assay's rows are
spooled to its own temporary file as batches come back, so the output is the
same file, byte for byte, whatever N is: assays in registry order, records in
archive order within each assay.
"""

from __future__ import annotations

import argparse
import csv
import sys
import tempfile
from collections import Counter
from collections.abc import Iterable, Iterator
from itertools import islice
from multiprocessing import Pool
from pathlib import Path
from typing import Any

from assaywatch.degeneracy import assay_degeneracy
from assaywatch.fasta import read_fasta
from assaywatch.score import load_config, screen_record
from assaywatch.validate import iter_files, load_assay

# Set once per worker process by _init_worker, so the assays and config are
# pickled once per worker rather than once per batch.
_STATE: tuple[list, dict[str, Any], list] | None = None


def _init_worker(assays: list, cfg: dict[str, Any]) -> None:
    global _STATE
    # Degeneracy is a property of the assay, not of any record, and it is
    # never scored. It rides along on every row so that a reader of the TSV
    # cannot see a `detect` without seeing how much the pool was diluted.
    degs = [assay_degeneracy(a) for a in assays]
    _STATE = (assays, cfg, [(d.total_fold, d.tier(cfg)) for d in degs])


def _screen_batch(batch: list[tuple[str, str]]) -> list[list[dict[str, Any]]]:
    """Rows for one batch of records, one list per assay in assay order."""
    assert _STATE is not None, "_init_worker was not called"
    assays, cfg, degs = _STATE
    out = []
    for assay, (fold, tier) in zip(assays, degs, strict=False):
        rows = []
        for rid, seq in batch:
            call = screen_record(assay, rid, seq, cfg)
            call.extra["degeneracy_fold"] = fold
            call.extra["degeneracy_tier"] = tier
            rows.append(call.as_row())
        out.append(rows)
    return out


def batches(records: Iterable[tuple[str, str]], target_bp: int) -> Iterator[list[tuple[str, str]]]:
    """Group records into batches of at least `target_bp` bases (the last may be short)."""
    batch, bp = [], 0
    for rec in records:
        batch.append(rec)
        bp += len(rec[1])
        if bp >= target_bp:
            yield batch
            batch, bp = [], 0
    if batch:
        yield batch


def screen_records(
    assays: list,
    records: Iterable[tuple[str, str]],
    cfg: dict[str, Any],
    workers: int = 1,
    chunk_bp: int = 5_000_000,
) -> Iterator[list[list[dict[str, Any]]]]:
    """Yield per-batch results in archive order, serially or from a process pool."""
    if workers <= 1:
        _init_worker(assays, cfg)
        yield from map(_screen_batch, batches(records, chunk_bp))
        return
    # Pool.imap would read the whole archive ahead into its task queue, so batches
    # are fed in windows of a few per worker: memory stays at a handful of
    # batches however large the archive. imap keeps input order within a window,
    # which is what makes the output independent of N.
    it = batches(records, chunk_bp)
    with Pool(workers, initializer=_init_worker, initargs=(assays, cfg)) as pool:
        while window := list(islice(it, 4 * workers)):
            yield from pool.imap(_screen_batch, window)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("assays", type=Path, help="a registry YAML file or a directory of them")
    ap.add_argument("fasta", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=None, help="TSV path (default: stdout)")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument(
        "--only",
        default=None,
        help="comma-separated assay ids to screen; the pipeline uses this to score each "
        "retrieval group only against the assays that asked for it",
    )
    ap.add_argument("--workers", type=int, default=1, help="processes to screen with (default 1)")
    ap.add_argument(
        "--chunk-bp",
        type=int,
        default=5_000_000,
        help="bases per worker batch (default 5,000,000)",
    )
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    assays = [load_assay(p) for p in iter_files(args.assays)]
    if args.only:
        wanted = {a.strip() for a in args.only.split(",") if a.strip()}
        assays = [a for a in assays if a.id in wanted]
        missing = wanted - {a.id for a in assays}
        if missing:
            raise SystemExit(f"--only names assays not in {args.assays}: {sorted(missing)}")

    # One spool file per assay, so rows can be written as batches finish and
    # still come out assay by assay without holding them all in memory.
    spools = [tempfile.TemporaryFile("w+", newline="") for _ in assays]
    fieldnames: list[str] | None = None
    tally: Counter = Counter()
    records = read_fasta(args.fasta)
    for per_assay in screen_records(assays, records, cfg, args.workers, args.chunk_bp):
        for assay, rows, spool in zip(assays, per_assay, spools, strict=False):
            if rows and fieldnames is None:
                fieldnames = list(rows[0])
            w = csv.DictWriter(spool, fieldnames=fieldnames or [], delimiter="\t")
            for row in rows:
                w.writerow(row)
                tally[(assay.id, row["call"])] += 1

    # Write under a temporary name and rename at the end, so the output only
    # exists once it is complete: counting finished files then means something.
    tmp = args.out.with_name(f".{args.out.name}.part") if args.out else None
    out = tmp.open("w", newline="") if tmp else sys.stdout
    if fieldnames is not None:
        csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t").writeheader()
        for spool in spools:
            spool.seek(0)
            while block := spool.read(1 << 20):
                out.write(block)
    for spool in spools:
        spool.close()
    if args.out:
        out.close()
        tmp.replace(args.out)
        for (aid, call), n in sorted(tally.items()):
            print(f"{aid}\t{call}\t{n}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
