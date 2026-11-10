"""The locus stage: check the records the screen could not judge, and write what it found.

    assaywatch locus results/2026-11-01/calls.tsv.gz --out results/2026-11-01/locus.tsv.gz
    assaywatch locus CALLS --out locus.tsv.gz --only Ranavirus_MCP_Pallister_2007
    assaywatch coverage CALLS --locus results/2026-11-01/locus.tsv.gz --out results/2026-11-01

WHY A STAGE OF ITS OWN (a maintainer decision, 2026-11-10). The screen has the
sequence in hand and could have run the locus check itself, but changing the screen
changes its signature and forces every archive to be rescreened. This stage reads the
calls table the screen already wrote, opens the archives for just the records that
need it, and writes a side file. Coverage joins the side file. Nothing upstream moves.

WHICH RECORDS. Only a `no_amplicon` the screen did not label `diverged`: no primer
site was found, and the screen cannot say whether the gene is there. A record the
screen scored (`detect`, `reduced`, `fail`) had both primer sites found, so the locus
is there. A `diverged` record had a site that is present and does not fit, which is
already a failure of the assay.

WHAT A ROW MEANS. `present` is the locus check's verdict. `has_room` is whether the
record runs far enough past the locus on BOTH sides to have held the primer sites.
Coverage counts the record as locus-present only when both are true:

    present  has_room   the record...
    1        1          holds the locus with room for the primers, and they found
                        nothing: a real failure to bind
    1        0          holds the locus and stops before a primer site: a deposit
                        cut short, which never tested the assay
    0        -          does not hold the locus

The second row is why `has_room` exists. The reference amplicons are INTERIORS: the
amplicon with `scoring.locus_identity_trim_bp` bases trimmed off each end, so the
primer sites cannot flatter the match (and so an indel in a primer site cannot hide
the locus). An interior can therefore be whole in a record that ends before the
primer site, and calling that a failure would blame the assay for a short deposit.

COST. One alignment per reference and strand per record; see `locus_check`. The
2026-11-01 calls hold about 1.8 million records to check, which is a cluster-sized
job without a k-mer seed. `--only` and `--limit` make a part of it runnable on a laptop.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import sys
from collections import defaultdict
from collections.abc import Iterator, Mapping, Sequence
from pathlib import Path
from typing import Any

from assaywatch.fasta import read_fasta
from assaywatch.locus_check import LocusResult, locus_check, rule_from_config
from assaywatch.registry import archive_dir
from assaywatch.registry import load as load_registry
from assaywatch.score import load_config

COLUMNS = ("assay_id", "record_id", "present", "has_room", "identity", "covered", "flank_left", "flank_right")
DIVERGED = "diverged"


def needs_check(row: Mapping[str, Any]) -> bool:
    """Is this a record the screen could not judge? See the module docstring."""
    return row.get("call") == "no_amplicon" and row.get("exclusion") != DIVERGED


def judge(
    record: str,
    references: Sequence[str],
    min_identity: float,
    min_covered: float,
    flank_bp: int,
) -> tuple[LocusResult, bool]:
    """The locus check, plus whether the record has room for both primer sites.

    `flank_bp` is how far beyond each end of a reference the primer sites reach: the
    bases that were trimmed off the amplicon to make the reference. The record must
    run at least that far past where the WHOLE reference would sit, on both sides.
    """
    result = locus_check(record, references, min_identity, min_covered)
    has_room = result.flank_left >= flank_bp and result.flank_right >= flank_bp
    return result, has_room


def read_references(path: Path, min_bp: int = 1) -> dict[str, list[str]]:
    """assay id -> reference amplicons (interiors), from `docs/locus-references.json`.

    A reference shorter than `min_bp` is dropped: a 17-base interior matches by chance
    in almost any record, so it defines nothing. An assay left with none is in the
    result with an empty list, which the stage reports as "reference too short".
    """
    data = json.loads(Path(path).read_text())
    return {aid: [s for s in entry.get("interiors", []) if len(s) >= min_bp] for aid, entry in data.items()}


def unjudged(calls: Path, only: set[str] | None) -> dict[str, set[str]]:
    """assay id -> the record ids that need a locus check, from the calls table."""
    opener = gzip.open if str(calls).endswith(".gz") else open
    out: dict[str, set[str]] = defaultdict(set)
    with opener(calls, "rt", newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return {}
        ia, ir, ic = header.index("assay_id"), header.index("record_id"), header.index("call")
        ie = header.index("exclusion") if "exclusion" in header else None
        for r in reader:
            if not r or (only is not None and r[ia] not in only):
                continue
            row = {"call": r[ic], "exclusion": r[ie] if ie is not None and ie < len(r) else ""}
            if needs_check(row):
                out[r[ia]].add(r[ir])
    return dict(out)


def read_locus(path: Path) -> dict[str, dict[str, bool]]:
    """assay id -> record id -> is the locus present WITH room for the primers?

    This is what coverage joins. A record absent from the file was not checked, and
    coverage falls back to the screen's own evidence for it.
    """
    out: dict[str, dict[str, bool]] = defaultdict(dict)
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            out[r["assay_id"]][r["record_id"]] = r["present"] == "1" and r["has_room"] == "1"
    return dict(out)


def _records(archive: Path, wanted: set[str]) -> Iterator[tuple[str, str]]:
    """(record id, sequence) for the wanted records in one archive directory, each once."""
    seen: set[str] = set()
    for fasta in sorted(archive.glob("*.fasta.gz")):
        for rid, seq in read_fasta(fasta):
            if rid in wanted and rid not in seen:
                seen.add(rid)
                yield rid, seq


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="assaywatch locus", description=__doc__.split("\n\n")[0])
    ap.add_argument("calls", type=Path, help="calls table (TSV or TSV.GZ)")
    ap.add_argument("--retrieved", type=Path, default=Path("data/retrieved"), help="the archives")
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument("--references", type=Path, default=Path("docs/locus-references.json"))
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--out", type=Path, required=True, help="the side file to write (locus.tsv.gz)")
    ap.add_argument("--only", action="append", metavar="ASSAY", help="limit to this assay id; repeatable")
    ap.add_argument("--limit", type=int, metavar="N", help="check at most N records per assay")
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    min_identity, min_covered = rule_from_config(cfg)
    flank_bp = int(cfg["scoring"]["locus_identity_trim_bp"])
    assays = load_registry(args.registry)
    references = read_references(args.references, int(cfg["coverage"]["locus_min_reference_bp"]))
    todo = unjudged(args.calls, set(args.only) if args.only else None)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    n_checked = n_present = n_room = 0
    skipped: dict[str, str] = {}
    with gzip.open(args.out, "wt", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(COLUMNS)
        for assay_id in sorted(todo):
            if assay_id not in assays:
                skipped[assay_id] = "not in the registry"
                continue
            refs = references.get(assay_id)
            if not refs:
                skipped[assay_id] = "no reference amplicon" if refs is None else "reference too short"
                continue
            done = 0
            for rid, seq in _records(archive_dir(assays[assay_id], args.retrieved), todo[assay_id]):
                if args.limit is not None and done >= args.limit:
                    break
                result, has_room = judge(seq, refs, min_identity, min_covered, flank_bp)
                w.writerow(
                    [
                        assay_id,
                        rid,
                        int(result.present),
                        int(has_room),
                        f"{result.identity:.3f}",
                        f"{result.covered:.3f}",
                        result.flank_left,
                        result.flank_right,
                    ]
                )
                done += 1
                n_present += result.present
                n_room += result.present and has_room
            n_checked += done
    print(
        f"{n_checked} records checked: {n_present} hold the locus, {n_room} of those with room for both "
        f"primer sites -> {args.out}",
        file=sys.stderr,
    )
    for assay_id, why in sorted(skipped.items()):
        print(f"  left alone, {why}: {assay_id} ({len(todo[assay_id])} records)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
