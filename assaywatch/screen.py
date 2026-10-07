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
import gzip
import sys
import tempfile
from collections import Counter, deque
from collections.abc import Iterable, Iterator
from itertools import islice
from multiprocessing import Pool
from pathlib import Path
from typing import Any

from assaywatch.chance import composition
from assaywatch.degeneracy import assay_degeneracy
from assaywatch.fasta import read_fasta
from assaywatch.score import Call, load_config, screen_record
from assaywatch.thermo import COLUMNS as THERMO_COLUMNS
from assaywatch.thermo import annotate
from assaywatch.validate import iter_files, load_assay

# Set once per worker process by _init_worker, so the assays and config are
# pickled once per worker rather than once per batch.
_STATE: tuple[list, dict[str, Any], list, bool, dict[str, tuple[int, tuple]]] | None = None


def _init_worker(
    assays: list,
    cfg: dict[str, Any],
    thermo: bool = False,
    context: dict[str, tuple[int, tuple]] | None = None,
) -> None:
    global _STATE
    # Degeneracy is a property of the assay, not of any record, and it is
    # never scored. It rides along on every row so that a reader of the TSV
    # cannot see a `detect` without seeing how much the pool was diluted.
    degs = [assay_degeneracy(a) for a in assays]
    _STATE = (assays, cfg, [(d.total_fold, d.tier(cfg)) for d in degs], thermo, context or {})


def _screen_batch(batch: list[tuple[str, str]]) -> list[list[dict[str, Any]]]:
    """Rows for one batch of records, one list per assay in assay order."""
    assert _STATE is not None, "_init_worker was not called"
    assays, cfg, degs, thermo, context = _STATE
    # Base composition is per record, not per assay: count each record once. A window cut
    # from a longer record is scored on that record's length and composition (from its
    # sidecar), because the chance E-values depend on both: on the window's own, a pair
    # the whole record called chance_only can pass the filter.
    srcs = [context.get(rid) for rid, _ in batch]
    comps = [src[1] if src else composition(seq) for (_, seq), src in zip(batch, srcs, strict=True)]
    specs = []
    for assay in assays:
        oligos = {"forward": assay.oligos.forward.matching_seq, "reverse": assay.oligos.reverse.matching_seq}
        if assay.oligos.probe is not None:
            oligos["probe"] = assay.oligos.probe.matching_seq
        specs.append(oligos)
    # Record-outer, so every assay sees a record back to back and find_sites'
    # per-record preparation (and any oligo two assays share) is reused.
    out: list[list[dict[str, Any]]] = [[] for _ in assays]
    for (rid, seq), comp, src in zip(batch, comps, srcs, strict=True):
        for assay, (fold, tier), oligos, rows in zip(assays, degs, specs, out, strict=True):
            call = screen_record(assay, rid, seq, cfg, comp, record_len=src[0] if src else None)
            call.extra["degeneracy_fold"] = fold
            call.extra["degeneracy_tier"] = tier
            if thermo:
                # The winning pool members, falling back to the primary oligos.
                call.extra["thermo"] = annotate(call, call.extra.get("oligos") or oligos, cfg)
            rows.append(call.as_row())
    return out


def sidecar_path(fasta: Path) -> Path:
    """`<stem>.windows.tsv.gz` beside `<stem>.fasta[.gz]`."""
    return fasta.with_name(fasta.name.removesuffix(".gz").removesuffix(".fasta") + ".windows.tsv.gz")


def window_context(fasta: Path) -> dict[str, tuple[int, tuple]] | None:
    """{window id: (source record length, source composition)} for a window archive, else None."""
    side = sidecar_path(fasta)
    if not side.exists():
        return None
    with gzip.open(side, "rt") as fh:
        return {
            r["window_id"]: (int(r["src_len"]), tuple(float(x) for x in r["src_comp"].split(",")))
            for r in csv.DictReader(fh, delimiter="\t")
        }


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
    thermo: bool = False,
    context: dict[str, tuple[int, tuple]] | None = None,
) -> Iterator[list[list[dict[str, Any]]]]:
    """Yield per-batch results in archive order, serially or from a process pool."""
    if workers <= 1:
        _init_worker(assays, cfg, thermo, context)
        yield from map(_screen_batch, batches(records, chunk_bp))
        return
    # Why not Pool.imap: it drains the whole iterable into the task queue up
    # front, so a 775 MB archive would be read into memory before any screening
    # finished. A bounded queue of batches in flight, results taken in submission
    # order:
    # memory stays at a few batches per worker however large the archive, the
    # output is independent of N, and a slow batch (one huge genome) holds up
    # only the results behind it, not the workers, which keep taking new batches.
    it = batches(records, chunk_bp)
    in_flight: deque = deque()
    with Pool(workers, initializer=_init_worker, initargs=(assays, cfg, thermo, context)) as pool:
        for batch in islice(it, 3 * workers):
            in_flight.append(pool.apply_async(_screen_batch, (batch,)))
        while in_flight:
            result = in_flight.popleft().get()  # re-raises a worker's exception here
            nxt = next(it, None)
            if nxt is not None:
                in_flight.append(pool.apply_async(_screen_batch, (nxt,)))
            yield result


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
    ap.add_argument(
        "--thermo",
        action="store_true",
        help="add duplex Tm columns per oligo (needs primer3-py; see assaywatch/thermo.py)",
    )
    args = ap.parse_args(argv)
    if args.workers < 1:
        ap.error("--workers must be at least 1")
    if args.chunk_bp < 1:
        ap.error("--chunk-bp must be positive")
    # Fail now, not after hours of screening, if the output cannot be written.
    if args.out and not args.out.parent.is_dir():
        ap.error(f"output directory {args.out.parent} does not exist")
    if not args.fasta.exists():
        ap.error(f"{args.fasta} does not exist")

    cfg = load_config(args.config)
    assays = [load_assay(p) for p in iter_files(args.assays)]
    if args.only is not None:
        wanted = {a.strip() for a in args.only.split(",") if a.strip()}
        if not wanted:
            ap.error("--only names no assays")
        assays = [a for a in assays if a.id in wanted]
        missing = wanted - {a.id for a in assays}
        if missing:
            raise SystemExit(f"--only names assays not in {args.assays}: {sorted(missing)}")
    if not assays:
        ap.error(f"no assays found in {args.assays}")

    # One spool file per assay. The output must be grouped by assay, but batches
    # come back in record order carrying rows for every assay at once, so rows are
    # written to a per-assay temporary file as they arrive and the spools are
    # concatenated at the end. The alternative — buffering until the archive is
    # done — would hold millions of rows in memory for a large archive.
    spools = [tempfile.TemporaryFile("w+", newline="") for _ in assays]
    # The columns are fixed by Call.as_row, so the header is known up front and
    # an archive with no records still produces a valid, header-only TSV.
    template = Call("", "", "no_amplicon")
    if args.thermo:
        template.extra["thermo"] = dict.fromkeys(THERMO_COLUMNS, "")
    fieldnames = list(template.as_row())
    writers = [csv.DictWriter(sp, fieldnames=fieldnames, delimiter="\t") for sp in spools]
    tally: Counter = Counter()
    context = window_context(args.fasta)
    records = read_fasta(args.fasta)
    for per_assay in screen_records(assays, records, cfg, args.workers, args.chunk_bp, args.thermo, context):
        for assay, rows, w in zip(assays, per_assay, writers, strict=True):
            w.writerows(rows)
            for row in rows:
                tally[(assay.id, row["call"])] += 1

    # Write under a temporary name and rename at the end, so the output only
    # exists once it is complete: counting finished files then means something.
    tmp = args.out.with_name(f".{args.out.name}.part") if args.out else None
    out = tmp.open("w", newline="") if tmp else sys.stdout
    csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t").writeheader()
    for spool in spools:
        spool.seek(0)
        while block := spool.read(1 << 20):
            out.write(block)
        spool.close()
    if args.out:
        out.close()
        tmp.replace(args.out)
    else:
        out.flush()
    # The per-call summary goes to stderr in either mode, so it never mixes with TSV on stdout.
    for (aid, call), n in sorted(tally.items()):
        print(f"{aid}\t{call}\t{n}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
