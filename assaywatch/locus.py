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

WHAT A ROW MEANS. `present` is the verdict of `judge`: identity at or over
`coverage.locus_min_identity`, `coverage.locus_min_covered` of the AMPLICON part of
the winning reference spanned (`amplicon_covered`), and at least
`coverage.locus_min_aligned_bp` reference bases aligned. `covered` is the share of
the whole reference, flanks included, and is reported, not judged. `has_room` is whether the
record runs far enough past the locus on BOTH sides to have held the primer sites.
Coverage counts the record as locus-present only when both are true:

    present  has_room   the record...
    1        1          holds the locus with room for the primers, and they found
                        nothing: a real failure to bind
    1        0          holds the locus and stops before a primer site: a deposit
                        cut short, which never tested the assay
    0        -          does not hold the locus

The second row is why `has_room` exists: a locus can be found in a record that stops
before a primer site, and calling that a failure would blame the assay for a short
deposit.

`FAIL` CALLS ARE CHECKED TOO, AND ONLY REPORTED (a maintainer decision, 2026-11-10).
A `fail` has both primer sites found. In a large archive a few of those are two
primers landing by chance in another gene. For each `fail` the stage asks whether
the stretch the screen called an amplicon is the locus, and writes the answer with
`checked` = `fail`. Coverage reports the count per assay and joins none of it: no
call, cell or drift status changes.

THE REFERENCES. By default WIDE ones (`docs/locus-wide-references.json`): the
amplicon plus up to 100 bp of flank each side, so a 57 bp amplicon still gives the
check something to measure. Each says how many of its bases lie outside the amplicon
at each end, which is how `judge` knows where the primer sites would be. The older
INTERIORS (`docs/locus-references.json`, primer sites trimmed off) are still read.

COST. 43 ms a record on one core with wide references (11,070 records, 2026-11-10);
see `locus_check` for what is aligned. The 2026-11-01 calls hold about 1.8 million
records to check, roughly 22 core-hours: one job per assay on a cluster, which is how
the Snakefile's `locus_check_assay` rule is cut. `--only` and `--limit` make a part
of it runnable on a laptop.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import sys
from collections import defaultdict
from collections.abc import Iterator, Mapping, Sequence
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from assaywatch.fasta import read_fasta
from assaywatch.locus_check import ABSENT, LocusResult, locus_check, rule_from_config
from assaywatch.registry import archive_dir
from assaywatch.registry import load as load_registry
from assaywatch.score import load_config

COLUMNS = (
    "assay_id",
    "record_id",
    "present",
    "has_room",
    "identity",
    "covered",
    "amplicon_covered",
    "flank_left",
    "flank_right",
    "checked",
)
UNJUDGED, FAIL = "unjudged", "fail"  # the two reasons a record is checked: the `checked` column
DIVERGED = "diverged"


def needs_check(row: Mapping[str, Any]) -> bool:
    """Is this a record the screen could not judge? See the module docstring."""
    return row.get("call") == "no_amplicon" and row.get("exclusion") != DIVERGED


@dataclass(frozen=True)
class Reference:
    """One reference amplicon and where the amplicon sits inside it.

    `left` and `right` are how many of the reference's bases lie OUTSIDE the amplicon
    at each end, as the reference is written. A wide reference (the amplicon plus its
    flanks) has them positive, 100 and 100 when the source record had room. An
    interior (the amplicon with its primer sites trimmed off) has them NEGATIVE: the
    amplicon reaches 20 bases beyond each end of the reference.
    """

    seq: str
    left: int
    right: int


def min_aligned_from_config(cfg: Mapping[str, Any]) -> int:
    """`coverage.locus_min_aligned_bp`: the fewest aligned reference bases that count."""
    return int(cfg["coverage"]["locus_min_aligned_bp"])


def amplicon_covered(result: LocusResult, reference: Reference) -> float:
    """The share of the reference's AMPLICON part that the alignment spans.

    A wide reference is flank, amplicon, flank, and its pads say where the amplicon
    starts and stops. On the reverse strand the reference matched reverse-complemented,
    so its right pad comes first. An interior has negative pads (the amplicon reaches
    beyond it): all of it is amplicon, and this is then `result.covered`.
    """
    if result.reference < 0:
        return 0.0
    first, last = (
        (reference.left, reference.right) if result.strand != "-" else (reference.right, reference.left)
    )
    start, end = max(0, first), len(reference.seq) - max(0, last)
    if end <= start:
        return 0.0
    return max(0, min(end, result.ref_end) - max(start, result.ref_start)) / (end - start)


def judge(
    record: str,
    references: Sequence[Reference],
    min_identity: float,
    min_covered: float,
    min_aligned_bp: int = 0,
) -> tuple[LocusResult, bool]:
    """Is the locus in the record, and has the record room for both primer sites?

    The best-scoring reference decides (`LocusResult.reference` says which). The
    returned result's `present` is THIS function's verdict, not `locus_check`'s:

        identity          >= min_identity      over the aligned columns
        amplicon covered  >= min_covered       of the AMPLICON part of that reference
        aligned bases     >= min_aligned_bp    of the reference, flanks included

    `locus_check` asks for `min_covered` of the whole reference. With a wide reference
    that demands the flanks too, and a deposit that holds the amplicon and both primer
    sites but begins twenty bases before the forward primer was refused (measured
    2026-11-10: 145 of 1,684 records the screen had detected or called reduced, none
    with the rule here, and 0 of 1,445 unrelated records either way). The flanks are
    there to be aligned, not to be required. The floor on aligned bases is the guard
    for a short amplicon, whose own fifty-odd bases chance could supply.

    The reference's pads also say where the amplicon would sit, and the record HAS
    ROOM when it reaches across that whole stretch. `flank_left` and `flank_right` are
    in the record's order, so when the match is on the reverse strand the reference's
    right pad is on the record's left.
    """
    result = locus_check(record, [r.seq for r in references], min_identity, min_covered)
    if result.reference < 0:
        return ABSENT, False
    ref = references[result.reference]
    present = (
        result.identity >= min_identity
        and amplicon_covered(result, ref) >= min_covered
        and result.ref_end - result.ref_start >= min_aligned_bp
    )
    result = replace(result, present=present)
    pad_left, pad_right = (ref.left, ref.right) if result.strand != "-" else (ref.right, ref.left)
    # The whole reference would start `flank_left` bases into the record, and the
    # amplicon `pad_left` bases after that: so the record must not start later.
    has_room = result.flank_left >= -pad_left and result.flank_right >= -pad_right
    return result, has_room


def read_references(path: Path, min_bp: int = 1, trim_bp: int = 20) -> dict[str, list[Reference]]:
    """assay id -> its reference amplicons, from either kind of reference file.

    The wide kind (`scripts/build_locus_references.py`) lists `references`, each with
    its own pads. The older kind (`docs/locus-references.json`) lists `interiors`,
    amplicons with `trim_bp` bases trimmed off each end, so their pads are minus that.

    A reference shorter than `min_bp` is dropped: a 17-base interior matches by chance
    in almost any record, so it defines nothing. An assay left with none is in the
    result with an empty list, which the stage reports as "reference too short".
    """
    out: dict[str, list[Reference]] = {}
    for aid, entry in json.loads(Path(path).read_text()).items():
        if "references" in entry:
            refs = [Reference(r["seq"], int(r["left"]), int(r["right"])) for r in entry["references"]]
        else:
            refs = [Reference(s, -trim_bp, -trim_bp) for s in entry.get("interiors", [])]
        out[aid] = [r for r in refs if len(r.seq) >= min_bp]
    return out


def to_check(
    calls: Path, only: set[str] | None
) -> tuple[dict[str, set[str]], dict[str, dict[str, tuple[int, int]]]]:
    """What the stage has to look at, from one pass over the calls table.

    First, assay id -> the unjudged record ids (`needs_check`). Second, assay id ->
    record id -> (amplicon start, amplicon end) for every `fail` call whose row says
    where the screen placed the amplicon; a table without those columns gives none.
    """
    opener = gzip.open if str(calls).endswith(".gz") else open
    blank: dict[str, set[str]] = defaultdict(set)
    fails: dict[str, dict[str, tuple[int, int]]] = defaultdict(dict)
    with opener(calls, "rt", newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return {}, {}
        ia, ir, ic = header.index("assay_id"), header.index("record_id"), header.index("call")
        ie = header.index("exclusion") if "exclusion" in header else None
        span = (
            (header.index("amplicon_start"), header.index("amplicon_end"))
            if "amplicon_start" in header and "amplicon_end" in header
            else None
        )
        for r in reader:
            if not r or (only is not None and r[ia] not in only):
                continue
            if r[ic] == FAIL:
                if span and len(r) > max(span) and r[span[0]].isdigit() and r[span[1]].isdigit():
                    fails[r[ia]][r[ir]] = (int(r[span[0]]), int(r[span[1]]))
                continue
            row = {"call": r[ic], "exclusion": r[ie] if ie is not None and ie < len(r) else ""}
            if needs_check(row):
                blank[r[ia]].add(r[ir])
    return dict(blank), dict(fails)


def unjudged(calls: Path, only: set[str] | None) -> dict[str, set[str]]:
    """assay id -> the record ids that need a locus check, from the calls table."""
    return to_check(calls, only)[0]


def read_locus(path: Path) -> dict[str, dict[str, bool]]:
    """assay id -> record id -> is the locus present WITH room for the primers?

    This is what coverage joins. A record absent from the file was not checked, and
    coverage falls back to the screen's own evidence for it. So does a `fail` call the
    stage checked (`read_fail_checks`): those rows are reported and join nothing.
    """
    out: dict[str, dict[str, bool]] = defaultdict(dict)
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r.get("checked") == FAIL:
                continue
            out[r["assay_id"]][r["record_id"]] = r["present"] == "1" and r["has_room"] == "1"
    return dict(out)


def read_fail_checks(path: Path) -> dict[str, tuple[int, int]]:
    """assay id -> (`fail` calls checked, how many of them are NOT the locus).

    A `fail` whose amplicon is not the locus is the screen placing two primers in some
    other sequence, by chance. A file from before `fail` calls were checked gives {}.
    """
    out: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r.get("checked") == FAIL:
                out[r["assay_id"]][0] += 1
                out[r["assay_id"]][1] += r["present"] != "1"
    return {a: (n, absent) for a, (n, absent) in out.items()}


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
    ap.add_argument("--references", type=Path, default=Path("docs/locus-wide-references.json"))
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--out", type=Path, required=True, help="the side file to write (locus.tsv.gz)")
    ap.add_argument("--only", action="append", metavar="ASSAY", help="limit to this assay id; repeatable")
    ap.add_argument("--limit", type=int, metavar="N", help="check at most N records per assay")
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    min_identity, min_covered = rule_from_config(cfg)
    min_aligned = min_aligned_from_config(cfg)
    assays = load_registry(args.registry)
    flank_bp = int(cfg["scoring"]["locus_identity_trim_bp"])
    references = read_references(args.references, int(cfg["coverage"]["locus_min_reference_bp"]), flank_bp)
    todo, fails = to_check(args.calls, set(args.only) if args.only else None)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    n_checked = n_present = n_room = n_fail = n_chance = 0
    skipped: dict[str, str] = {}
    with gzip.open(args.out, "wt", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(COLUMNS)
        for assay_id in sorted(set(todo) | set(fails)):
            if assay_id not in assays:
                skipped[assay_id] = "not in the registry"
                continue
            refs = references.get(assay_id)
            if not refs:
                skipped[assay_id] = "no reference amplicon" if refs is None else "reference too short"
                continue
            blank, placed = todo.get(assay_id, set()), fails.get(assay_id, {})
            # A `fail` call is checked where the screen placed its amplicon, with as much
            # record either side as the longest reference could need.
            reach = max(len(r.seq) for r in refs)
            done = 0
            for rid, seq in _records(archive_dir(assays[assay_id], args.retrieved), blank | set(placed)):
                if args.limit is not None and done >= args.limit:
                    break
                if rid in placed:
                    start, end = placed[rid]
                    seq, why = seq[max(0, start - reach) : end + reach], FAIL
                else:
                    why = UNJUDGED
                result, has_room = judge(seq, refs, min_identity, min_covered, min_aligned)
                w.writerow(
                    [
                        assay_id,
                        rid,
                        int(result.present),
                        int(has_room),
                        f"{result.identity:.3f}",
                        f"{result.covered:.3f}",
                        f"{amplicon_covered(result, refs[result.reference]):.3f}",  # 0 when absent
                        result.flank_left,
                        result.flank_right,
                        why,
                    ]
                )
                done += 1
                if why == FAIL:
                    n_fail += 1
                    n_chance += not result.present
                else:
                    n_checked += 1
                    n_present += result.present
                    n_room += result.present and has_room
    print(
        f"{n_checked} records checked: {n_present} hold the locus, {n_room} of those with room for both "
        f"primer sites -> {args.out}",
        file=sys.stderr,
    )
    print(
        f"{n_fail} `fail` calls checked where the screen placed the amplicon: {n_chance} are not the locus",
        file=sys.stderr,
    )
    for assay_id, why in sorted(skipped.items()):
        n = len(todo.get(assay_id, ())) + len(fails.get(assay_id, ()))
        print(f"  left alone, {why}: {assay_id} ({n} records)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
