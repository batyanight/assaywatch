#!/usr/bin/env python3
"""Cut wide reference amplicons for the locus check: the amplicon plus its flanks.

    python scripts/build_locus_references.py plan results/2026-11-01/calls.tsv.gz --out refs-manifest.tsv
    python scripts/build_locus_references.py cut refs-manifest.tsv --out docs/locus-wide-references.json

WHY. The locus check (`assaywatch/locus_check.py`) looks for an assay's target region in
a record by aligning a reference against it. The first references were amplicon
interiors, which are useless for a short amplicon (17 bases for a 57 bp product) and
blind to a locus whose length varies (one reference length, six product lengths). A
wide reference is the amplicon plus up to `--flank` bases either side, cut from records
the assay DETECTS, one per product length and then one per species.

TWO STEPS, BECAUSE THE ARCHIVES ARE BIG AND LIVE ELSEWHERE.

`plan` reads the calls table and the archive metadata and writes a manifest: which
records to cut, from which archive, and where the amplicon sits in each. It needs the
`assaywatch` package and no sequence.

`cut` reads the manifest and the FASTA archives and writes the references. It uses
ONLY the Python standard library, so it runs anywhere the archives are, including a
machine without the project's environment. It can be stopped and restarted
(`--seconds`): each archive's cut is saved as it finishes.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_FLANK = 100
DEFAULT_LIMIT = 8


def choose_sources(rows: list[dict], flank_bp: int, limit: int) -> list[dict]:
    """Which detected records to cut one assay's references from.

    `rows` are the assay's `detect` records: `record_id`, `amplicon_bp`, `species`,
    `start`, `end`, `length` (the record's, or None when unknown).

    One record per product LENGTH first, commonest length first, because a reference
    of the wrong length cannot cover a locus that carries a different number of
    repeats. Then one per SPECIES not yet represented, commonest first, so the
    references span the lineages the assay covers. Within a group, a record with room
    for both flanks beats one without, and ties go to the lowest record id, so the
    choice is the same however the calls table was ordered.
    """

    def roomy(r: dict) -> bool:
        return r["start"] >= flank_bp and (r["length"] is None or r["length"] - r["end"] >= flank_bp)

    def best(group: list[dict]) -> dict:
        return min(group, key=lambda r: (not roomy(r), r["record_id"]))

    picked: list[dict] = []
    taken: set[str] = set()
    for key in ("amplicon_bp", "species"):
        groups: dict = defaultdict(list)
        for r in rows:
            groups[r[key]].append(r)
        seen = {p[key] for p in picked}
        # commonest group first; the group's own value breaks ties so the order is fixed
        for value, group in sorted(groups.items(), key=lambda kv: (-len(kv[1]), str(kv[0]))):
            if len(picked) >= limit:
                return picked
            if value in seen:
                continue
            choice = best([r for r in group if r["record_id"] not in taken] or group)
            if choice["record_id"] not in taken:
                picked.append(choice)
                taken.add(choice["record_id"])
    return picked


def plan(args: argparse.Namespace) -> int:
    """Write the manifest. Imports the package here so that `cut` never needs it."""
    from assaywatch.accession import strip_version
    from assaywatch.coverage import read_taxids
    from assaywatch.registry import archive_dir
    from assaywatch.registry import load as load_registry
    from assaywatch.score import load_config
    from assaywatch.taxonomy import taxonomy_from_config

    assays = load_registry(args.registry)
    taxonomy = taxonomy_from_config(load_config(args.config))
    # Taxids come from the backfill sidecar as well as the archive metadata (older
    # archives carry no taxid column), which is what `coverage.read_taxids` reads.
    taxid = read_taxids(args.retrieved)
    length: dict[str, int] = {}
    for meta in sorted(args.retrieved.rglob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            header = (fh.readline() or "").rstrip("\n").split("\t")
            if "accession" not in header or "length" not in header:
                continue
            ai, li = header.index("accession"), header.index("length")
            for line in fh:
                parts = line.rstrip("\n").split("\t")
                if len(parts) > max(ai, li) and parts[li].isdigit():
                    length[strip_version(parts[ai])] = int(parts[li])

    detected: dict[str, list[dict]] = defaultdict(list)
    opener = gzip.open if str(args.calls).endswith(".gz") else open
    with opener(args.calls, "rt", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["call"] != "detect" or row["assay_id"] not in assays or not row.get("amplicon_start"):
                continue
            acc = strip_version(row["record_id"])
            t = taxid.get(acc)
            detected[row["assay_id"]].append(
                {
                    "record_id": row["record_id"],
                    "amplicon_bp": int(row["amplicon_end"]) - int(row["amplicon_start"]),
                    "species": (taxonomy.species_of(t) if taxonomy and t else None) or t or 0,
                    "start": int(row["amplicon_start"]),
                    "end": int(row["amplicon_end"]),
                    "length": length.get(acc),
                }
            )

    n = 0
    with open(args.out, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["archive", "assay_id", "record_id", "amplicon_start", "amplicon_end"])
        for assay_id in sorted(detected):
            archive = archive_dir(assays[assay_id], Path(""))
            for r in choose_sources(detected[assay_id], args.flank, args.limit):
                w.writerow([archive.as_posix(), assay_id, r["record_id"], r["start"], r["end"]])
                n += 1
    without = sorted(set(assays) - set(detected))
    print(f"{n} references planned for {len(detected)} assays -> {args.out}", file=sys.stderr)
    print(f"{len(without)} assays have no detected record to cut from", file=sys.stderr)
    return 0


def _fasta(path: Path, wanted: set[str]):
    """(record id, sequence) for the wanted records of one gzipped FASTA; stops when all are found."""
    left = set(wanted)
    rid, chunks = None, []
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith(">"):
                if rid is not None:
                    yield rid, "".join(chunks)
                    left.discard(rid)
                    if not left:
                        return
                head = line[1:].split(None, 1)
                rid = head[0] if head and head[0] in left else None
                chunks = []
            elif rid is not None:
                chunks.append(line.strip())
    if rid is not None:
        yield rid, "".join(chunks)


def cut(args: argparse.Namespace) -> int:
    """Cut every planned reference. Standard library only: see the module docstring."""
    started = time.monotonic()
    by_archive: dict[str, dict[str, list[tuple[str, int, int]]]] = defaultdict(lambda: defaultdict(list))
    order: list[tuple[str, str]] = []  # (assay, record) in manifest order, which is the output order
    with open(args.manifest, newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            by_archive[row["archive"]][row["record_id"]].append(
                (row["assay_id"], int(row["amplicon_start"]), int(row["amplicon_end"]))
            )
            order.append((row["assay_id"], row["record_id"]))

    parts = Path(str(args.out) + ".parts")
    parts.mkdir(parents=True, exist_ok=True)
    pending = 0
    for archive in sorted(by_archive):
        part = parts / (archive.replace("/", "__") + ".json")
        if part.exists():
            continue
        if args.seconds is not None and time.monotonic() - started > args.seconds:
            pending += 1
            continue
        wanted = by_archive[archive]
        found: dict[str, dict] = {}
        remaining = set(wanted)
        for fasta in sorted((args.retrieved / archive).glob("*.fasta.gz")):
            if not remaining:
                break
            for rid, seq in _fasta(fasta, remaining):
                remaining.discard(rid)
                for assay_id, a_start, a_end in wanted[rid]:
                    lo, hi = max(0, a_start - args.flank), min(len(seq), a_end + args.flank)
                    found[f"{assay_id}\t{rid}"] = {
                        "from": rid,
                        "left": a_start - lo,  # reference bases before the amplicon
                        "right": hi - a_end,  # and after it
                        "seq": seq[lo:hi].upper(),
                    }
        part.write_text(json.dumps({"found": found, "missing": sorted(remaining)}))
    if pending:
        print(f"{pending} archives still to cut; run the same command again", file=sys.stderr)
        return 3

    found, missing = {}, []
    for part in sorted(parts.glob("*.json")):
        data = json.loads(part.read_text())
        found.update(data["found"])
        missing += data["missing"]
    out: dict[str, dict] = {}
    for assay_id, rid in order:
        ref = found.get(f"{assay_id}\t{rid}")
        if ref is not None:
            out.setdefault(assay_id, {"flank_bp": args.flank, "references": []})["references"].append(ref)
    args.out.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    lengths = Counter(len(r["seq"]) < 100 for e in out.values() for r in e["references"])
    print(
        f"{sum(len(e['references']) for e in out.values())} references for {len(out)} assays -> {args.out}"
        f" ({lengths[True]} under 100 bp; {len(missing)} planned records not found in the archives)",
        file=sys.stderr,
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="step", required=True)
    p = sub.add_parser("plan", help="choose the source records; needs the assaywatch package")
    p.add_argument("calls", type=Path)
    p.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    p.add_argument("--registry", type=Path, default=Path("registry"))
    p.add_argument("--config", type=Path, default=None)
    p.add_argument("--flank", type=int, default=DEFAULT_FLANK)
    p.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="references per assay")
    p.add_argument("--out", type=Path, required=True)
    p.set_defaults(run=plan)
    c = sub.add_parser("cut", help="cut them from the archives; standard library only")
    c.add_argument("manifest", type=Path)
    c.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    c.add_argument("--flank", type=int, default=DEFAULT_FLANK)
    c.add_argument("--seconds", type=float, default=None, help="stop starting new archives after this long")
    c.add_argument("--out", type=Path, required=True)
    c.set_defaults(run=cut)
    args = ap.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    raise SystemExit(main())
