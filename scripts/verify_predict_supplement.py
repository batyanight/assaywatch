#!/usr/bin/env python3
"""Check every PREDICT-panel entry against the supplement its oligos were read from.

    python scripts/verify_predict_supplement.py
    python scripts/verify_predict_supplement.py --tsv docs/predict-supplement-verification.tsv

Why
---
Each entry with `source.predict_protocol` cites its DESIGN paper (Lozano 1997 for
P-003, and so on), and `verify_oligos_against_paper.py` checks it against that
paper. But the oligos were transcribed from the PREDICT protocol book, Anthony et
al. 2015, Nat Commun 6:8147, Supplementary Methods (doi 10.1038/ncomms9147,
CC-BY 4.0), and the book modifies some of them (P-004's `ARS7C-Mod`). So the
book is what the stored sequences must match, and until 2026-10-21 it was not
on disk: 35 entries were waiting on it.

The book's layout, per protocol: a `P-0xx <Family>` heading, then a PRIMERS
block where each oligo is `NAME-SEQ` or `NAME;SEQ` and a `ROUND n` label sits
between a round's two primers (sometimes as `ROUND` with the number on the next
line). The text is read with `pdftotext -layout`, which keeps that geometry.

What is checked, per entry: each stored oligo occurs in its protocol's section
(exact, after uppercasing; inosine compared as written), which round it sits in,
whether that agrees with `source.nested_round`, and the section's amplicon size
for that round against `amplicon_bp`. A miss reports the nearest oligo in the
section and its Hamming distance when the lengths agree. Nothing is written to
the registry; the output is a table to act on.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

from assaywatch.validate import iter_files, load_assay

SUPPLEMENT = Path("papers/10.1038_ncomms9147.supp.pdf")

# A section heading on its own line: `P-003 Arenaviruses`. The summary table's
# rows also start with `P-0xx` but carry more columns, so a heading is a line
# with nothing after the family name.
HEADING = re.compile(r"^P-(\d{3}) [A-Za-z][A-Za-z .'-]*$")
# IUPAC plus I (inosine), 14+ letters, not glued to other letters on either side.
SEQ = re.compile(r"(?<![A-Za-z])([ACGTURYKMSWBDHVNI]{14,})(?![a-z])")
# `ROUND 1`, or bare `ROUND` with the number on a later line; the digit must not
# run on, or `ROUND   68C for 15 sec` reads as round 6.
ROUND = re.compile(r"\bROUND\b(?:\s{1,2}(\d)(?!\d))?")
AMPLICON = re.compile(r"(~?\d{2,4}(?:\s*-\s*\d{2,4})?)\s*bp")


def supplement_text(pdf: Path) -> list[str]:
    out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True)
    return out.stdout.splitlines()


def sections(lines: list[str]) -> dict[str, list[str]]:
    """Protocol id -> its lines, from its heading to the next heading."""
    out: dict[str, list[str]] = {}
    current = None
    for line in lines:
        m = HEADING.match(line.strip())
        if m:
            current = f"P-{m.group(1)}"
            out[current] = []
        elif current:
            out[current].append(line)
    return out


def parse_section(lines: list[str]) -> list[dict]:
    """Oligos in a section, each with its round and that round's amplicon size.

    A round's first primer sits on its `ROUND` label's line or up to two lines
    above it (the layout varies by protocol), so each label after the first
    opens a block at the closest oligo line within that reach, or at the label
    itself. Every oligo takes its block's round and the block's AMPLICON cell.
    Two earlier rules misassigned: nearest-label line distance (Alpha2F, two
    lines above its label) and splitting on each round's `95C 5 min` (absent
    where a round reads "Same protocol for both rounds"). A semi-nested
    protocol prints its shared primer once, in round 1's block.
    """
    # A primer row is a sequence, or a reused primer written `Astr4380F Same as for first round`.
    oligo_lines = [
        i for i, line in enumerate(lines) if SEQ.search(line[:60]) or re.search(r"\bSame\b", line[:50])
    ]
    labels = []  # (line index, round)
    for i, line in enumerate(lines):
        if not (m := ROUND.search(line)):
            continue
        rnd = m.group(1)
        # `ROUND` with its number alone in the left margin a line or two down;
        # not just any leading digit, or `96C for 5 sec` reads as round 9.
        for nxt in lines[i + 1 : i + 3] if rnd is None else []:
            if d := re.match(r"\s{0,6}(\d)(\s|$)", nxt):
                rnd = d.group(1)
                break
        labels.append((i, int(rnd) if rnd else None))
    if not labels:
        labels = [(0, 1)]
    starts = [0]
    for i, _ in labels[1:]:
        above = [j for j in oligo_lines if i - 2 <= j <= i]
        starts.append(above[-1] if above else i)
    out = []
    for (_, rnd), start, end in zip(labels, starts, starts[1:] + [len(lines)], strict=True):
        block = lines[start:end]
        amp = next((m.group(1).replace(" ", "") for line in block if (m := AMPLICON.search(line[60:]))), None)
        for line in block:
            # Only the PRIMERS column: the protocol text can hold long capitals.
            for m in SEQ.finditer(line[:60]):
                name = re.split(r"\s{2,}", line[: m.start()].strip())[-1].rstrip("-;: ").strip()
                out.append({"name": name, "seq": m.group(1), "round": rnd or 1, "amplicon": amp})
    return out


def hamming(a: str, b: str) -> int | None:
    return sum(x != y for x, y in zip(a, b, strict=True)) if len(a) == len(b) else None


def check(assay, section: list[dict]) -> list[dict]:
    rows = []
    want_round = assay.source.nested_round
    want_n = int(re.sub(r"\D", "", want_round) or 0) or None if want_round else None
    # The product an entry makes is its own round's, not the block its shared primer is printed in.
    round_amp: dict[int, str] = {}
    for o in section:
        if o["amplicon"]:
            round_amp.setdefault(o["round"], o["amplicon"])
    for role in ("forward", "reverse", "probe"):
        oligo = getattr(assay.oligos, role, None)
        if oligo is None:
            continue
        stored = (oligo.seq_as_written or oligo.seq).upper()
        # A primer printed in more than one round (P-016 reprints PVO3) is taken from the entry's own round.
        hits = sorted((o for o in section if o["seq"].upper() == stored), key=lambda o: o["round"] != want_n)
        row = {
            "assay_id": assay.id,
            "protocol": assay.source.predict_protocol,
            "role": role,
            "stored_name": oligo.name or "",
            "stored_seq": stored,
            "book_name": "",
            "book_seq": "",
            "verdict": "",
            "book_round": "",
            "entry_round": want_round or "",
            "book_amplicon": "",
            "amplicon_bp": assay.amplicon_bp if assay.amplicon_bp is not None else "",
        }
        if hits:
            h = hits[0]
            row.update(
                verdict="exact",
                book_name=h["name"],
                book_seq=h["seq"],
                book_round=h["round"] or "",
                book_amplicon=round_amp.get(want_n or h["round"], ""),
            )
        else:
            scored = [(hamming(stored, o["seq"].upper()), o) for o in section]
            same_len = sorted((d, o["seq"]) for d, o in scored if d is not None)
            if same_len:
                d, seq = same_len[0]
                o = next(o for o in section if o["seq"] == seq)
                row.update(
                    verdict=f"differs ({d} of {len(stored)})",
                    book_name=o["name"],
                    book_seq=seq,
                    book_round=o["round"] or "",
                    book_amplicon=o["amplicon"] or "",
                )
            else:
                row["verdict"] = "absent"
        rows.append(row)
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument("--supplement", type=Path, default=SUPPLEMENT)
    ap.add_argument("--tsv", type=Path, help="write every row here")
    args = ap.parse_args(argv)
    if not args.supplement.exists():
        sys.exit(
            f"{args.supplement} not found. It is CC-BY: Nat Commun 6:8147, Supplementary Information "
            "(41467_2015_BFncomms9147_MOESM1131_ESM.pdf on nature.com)."
        )
    book = {pid: parse_section(lines) for pid, lines in sections(supplement_text(args.supplement)).items()}
    rows = []
    for path in sorted(iter_files(args.registry)):
        assay = load_assay(path)
        pid = assay.source.predict_protocol if assay.source else None
        if not pid:
            continue
        if pid not in book:
            rows.append({"assay_id": assay.id, "protocol": pid, "verdict": "protocol not in supplement"})
            continue
        rows += check(assay, book[pid])
    cols = list(dict.fromkeys(k for r in rows for k in r))
    w = csv.DictWriter(
        open(args.tsv, "w", newline="") if args.tsv else sys.stdout, cols, delimiter="\t", restval=""
    )
    w.writeheader()
    w.writerows(rows)
    if args.tsv:
        verdicts: dict[str, int] = {}
        for r in rows:
            verdicts[r["verdict"].split(" (")[0]] = verdicts.get(r["verdict"].split(" (")[0], 0) + 1
        print(
            f"{len(book)} protocols parsed, {len({r['assay_id'] for r in rows})} entries, {len(rows)} oligos:",
            verdicts,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
