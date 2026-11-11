"""Which curated RefSeq records repeat a non-RefSeq record: the map `calls.key_calls_by_accession` reads.

An `NZ_` accession names its source, so `accession.refseq_source` can pair it. An `NC_`,
`AC_`, `NG_`, `NR_` or `NW_` number names nothing, so the pair has to come from the
sequences: a record is a twin when its whole sequence equals the curated record's.

Identical sequence doesn't strictly prove a copy, since a separate deposit can match too,
and the file keeps every match rather than choosing one. Measured on the 2026-11-01 calls:
7,450 (assay, record) pairs in 186 assays, moving one status beyond the `NZ_` fix
(`docs/journal/2026-11-06-refseq-twins.md`). `NM_` and `XM_` are left out because their
records are rarely a copy: 130 of 4,244 and 12 of 48,799 calls have a twin.

The map is global and the pairing per assay: a row is dropped only when a twin is in the
same assay's calls, which is `key_calls_by_accession`'s job and not this file's.

    assaywatch refseq-twins data/retrieved --out results/<date>/refseq-twins.tsv.gz
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import re
import sys
from collections import defaultdict
from collections.abc import Mapping
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from assaywatch.accession import strip_version
from assaywatch.fasta import read_fasta

FILENAME = "refseq-twins.tsv.gz"

_CURATED = re.compile(r"^(?:NC|AC|NG|NR|NW)_")
#: Any RefSeq number, curated or not. A twin has to be the deposit that survives, so it can't be one of these.
_REFSEQ = re.compile(r"^[A-Z]{2}_")
_HEADER = "refseq_accession\ttwins\n"


def _digests(path: Path) -> list[tuple[str, bytes]]:
    """(version-less accession, digest of the whole sequence) for one archive file."""
    return [
        (strip_version(rid), hashlib.blake2b(seq.upper().encode(), digest_size=12).digest())
        for rid, seq in read_fasta(path)
    ]


def build(retrieved: Path, out: Path, *, workers: int = 1) -> None:
    """Write the map from every archive under `retrieved`. The bytes don't depend on `workers`."""
    files = sorted(retrieved.rglob("*.fasta.gz"))
    curated: dict[bytes, set[str]] = defaultdict(set)
    others: dict[bytes, set[str]] = defaultdict(set)

    def add(pairs: list[tuple[str, bytes]]) -> None:
        for acc, digest in pairs:
            if _CURATED.match(acc):
                curated[digest].add(acc)
            elif not _REFSEQ.match(acc):
                others[digest].add(acc)

    if workers > 1:
        with ProcessPoolExecutor(workers) as pool:
            for pairs in pool.map(_digests, files, chunksize=4):
                add(pairs)
    else:
        for path in files:
            add(_digests(path))

    twins: dict[str, set[str]] = defaultdict(set)
    for digest, accessions in curated.items():
        for acc in accessions:
            twins[acc] |= others.get(digest, set())

    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(out.name + ".tmp")
    # mtime=0, so a rebuild over the same archives is byte-identical.
    with open(tmp, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, filename="") as gz:
        gz.write(_HEADER.encode())
        for acc in sorted(twins):
            if twins[acc]:
                gz.write(f"{acc}\t{','.join(sorted(twins[acc]))}\n".encode())
    tmp.replace(out)


def read(path: Path) -> dict[str, frozenset[str]]:
    """RefSeq accession -> the identical non-RefSeq accessions."""
    with gzip.open(path, "rt") as fh:
        next(fh, None)
        return {
            acc: frozenset(twins.split(",")) for acc, twins in (line.rstrip("\n").split("\t") for line in fh)
        }


def beside(calls_path: Path) -> Mapping[str, frozenset[str]] | None:
    """The map of the run a calls table belongs to, or None with a warning for a run that has none."""
    path = calls_path.parent / FILENAME
    if not path.exists():
        print(
            f"WARNING: no {FILENAME} beside {calls_path}: curated RefSeq copies count as deposits",
            file=sys.stderr,
        )
        return None
    return read(path)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("retrieved", type=Path, help="the archive root, data/retrieved")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--workers", type=int, default=1)
    args = ap.parse_args(argv)
    build(args.retrieved, args.out, workers=args.workers)
    print(f"{args.out}: {len(read(args.out)):,} curated RefSeq records with a twin", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
