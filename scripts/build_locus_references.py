#!/usr/bin/env python3
"""Build each assay's locus reference from the amplicons it actually detects.

    python scripts/build_locus_references.py --run results/2026-10-25
    python scripts/build_locus_references.py --run results/2026-10-25 --check

The cached artefact behind `assaywatch.locus_identity`: for every assay, a few
amplicon interiors taken from records that `detect`, which is what the test
compares a questionable amplicon against. Written as JSON so it is auditable
rather than a hidden intermediate - anyone can see which records define an
assay's locus, and a wrong one is visible instead of merely acting.

WHY IT READS A RUN'S `calls.tsv.gz` AND NOT `results/screened/`. That directory
keeps the screens of orphan groups, which no live assay retrieves and nothing
rescreens, so their rows carry whatever scoring rules were in force when they
were written - one of them predates `amplicon.declared_tolerance` by eleven days.
Globbing it inflated three measurements about a hundredfold on 2026-10-25
(docs/2026-10-25-stale-orphan-screens.md). `collect_calls` is what the report is
built from, so it is what a reference quoted beside the report must come from.

A reference is only ever taken from a `detect`. A `reduced` record also carries
the locus, but `detect` is the stricter evidence and there is no shortage of it;
an assay with no `detect` at all gets no reference, and the test then declines to
judge that assay rather than inventing a locus from a failure.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from assaywatch.accession import strip_version  # noqa: E402
from assaywatch.locus_identity import TRIM_BP, interior  # noqa: E402

#: How many reference interiors to keep per assay. More is slower at screen time
#: for no measured gain: the detects of one assay are the same locus, so the
#: second reference rarely changes the answer. Five is a hedge against one
#: unrepresentative record, not a sample size.
N_REFERENCES = 5


def read_detects(calls: Path) -> dict[str, list[tuple[str, int, int]]]:
    """{assay_id: [(accession, amplicon_start, amplicon_end)]} for `detect` rows."""
    out: dict[str, list[tuple[str, int, int]]] = defaultdict(list)
    with gzip.open(calls, "rt") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["call"] != "detect":
                continue
            try:
                start, end = int(r["amplicon_start"]), int(r["amplicon_end"])
            except (KeyError, TypeError, ValueError):
                continue
            out[r["assay_id"]].append((strip_version(r["record_id"]), start, end))
    return out


def load_sequences(wanted: set[str], retrieved: Path) -> dict[str, str]:
    """{accession without version: sequence} for the accessions asked for."""
    got: dict[str, str] = {}
    for fasta in sorted(retrieved.rglob("*.fasta.gz")):
        if not wanted - got.keys():
            break
        try:
            fh = gzip.open(fasta, "rt")
        except OSError:
            continue
        with fh:
            acc: str | None = None
            buf: list[str] = []
            for line in fh:
                if line.startswith(">"):
                    if acc in wanted and acc not in got:
                        got[acc] = "".join(buf)
                    acc = strip_version(line[1:].split()[0])
                    buf = []
                else:
                    buf.append(line.strip())
            if acc in wanted and acc not in got:
                got[acc] = "".join(buf)
    return got


def build(calls: Path, retrieved: Path, trim: int = TRIM_BP) -> dict[str, dict]:
    detects = read_detects(calls)
    # Take the first few per assay rather than a random sample, so the artefact is
    # reproducible from the same run without carrying a seed.
    picks = {a: rows[: N_REFERENCES * 4] for a, rows in detects.items()}
    seqs = load_sequences({acc for rows in picks.values() for acc, _, _ in rows}, retrieved)
    out: dict[str, dict] = {}
    for assay, rows in sorted(picks.items()):
        refs: list[str] = []
        used: list[str] = []
        for acc, start, end in rows:
            seq = seqs.get(acc)
            if not seq:
                continue
            lo, hi = (start, end) if start <= end else (end, start)
            it = interior(seq[max(0, lo) : hi], trim)
            if it and it not in refs:
                refs.append(it)
                used.append(acc)
            if len(refs) >= N_REFERENCES:
                break
        if refs:
            out[assay] = {"from": used, "interiors": refs}
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", type=Path, required=True, help="a results/<date> directory holding calls.tsv.gz")
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "locus-references.json")
    ap.add_argument(
        "--check", action="store_true", help="exit 1 if the committed file is not what this would write"
    )
    args = ap.parse_args(argv)

    calls = args.run / "calls.tsv.gz"
    if not calls.exists():
        print(f"no calls table at {calls}", file=sys.stderr)
        return 2
    refs = build(calls, args.retrieved)
    text = json.dumps(refs, indent=1, sort_keys=True) + "\n"
    n_int = sum(len(v["interiors"]) for v in refs.values())
    if args.check:
        if not args.out.exists() or args.out.read_text() != text:
            print(f"{args.out} is stale; regenerate it with --run {args.run}", file=sys.stderr)
            return 1
        print(f"{args.out} is current ({len(refs)} assays, {n_int} interiors)")
        return 0
    args.out.write_text(text)
    print(f"wrote {args.out} ({len(refs)} assays, {n_int} interiors)")
    lengths = sorted(len(i) for v in refs.values() for i in v["interiors"])
    if lengths:
        print(f"  interior lengths {lengths[0]}-{lengths[-1]} bp, median {lengths[len(lengths) // 2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
