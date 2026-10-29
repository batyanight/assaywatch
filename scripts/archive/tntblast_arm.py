#!/usr/bin/env python3
"""Run TNTBLAST over the bench panels and record its melting temperatures. No verdict.

    python scripts/tntblast_arm.py --tsv results/tntblast-bench.tsv
    python scripts/compare_thermo.py --tntblast results/tntblast-bench.tsv

WHY TNTBLAST SPECIFICALLY. `docs/related-work.md` answers "why not just use
PCR_strainer?" with a feature table, and PCR_strainer wraps thermonucleotideBLAST --
so TNTBLAST is the engine a reviewer will name. `scripts/compare_thermo.py` ran the
same experiment against primer3's nearest-neighbour model instead, for one reason:
TNTBLAST is on bioconda for osx-64 and linux-64 but not osx-arm64, and the osx-64
build needs Rosetta 2. Rosetta was installed on 2026-10-27, so the arm the comparison
was built for can finally run (`tntblast` 2.77, osx-64 under Rosetta).

WHAT IT RECORDS, AND WHAT IT DOES NOT DECIDE. TNTBLAST's own thresholds are `-e`
(minimum primer Tm) and `-E` (minimum probe Tm): below them it reports no amplicon at
all. Choosing them here would bake one arbitrary cut into the measurement, so this
runs at a permissive floor and writes out the TEMPERATURES, one row per bench record:
the best amplicon's limiting primer Tm and its probe Tm. `compare_thermo.py` then
sweeps the cut on these same rows and keeps the best, which is the same deliberate
in-sample advantage the primer3 arm is given -- its accuracy is an upper bound while
the penalty rule runs exactly as it ships.

ONE RECORD PER INVOCATION, which is slower and the only honest way. TNTBLAST's
verbose output ends each hit with the target's defline, so a multi-record database
needs that defline parsed back to a record -- and a record that yields NO hit prints
nothing at all, which is indistinguishable from a record that was never searched. A
single-record database makes "no output" mean exactly one thing.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))

from assaywatch.accession import strip_version  # noqa: E402
from assaywatch.fasta import read_fasta  # noqa: E402
from assaywatch.validate import load_assay  # noqa: E402

PANELS = REPO / "docs" / "bench-panels" / "panels.tsv"
CACHE = REPO / ".tmp" / "bench-panels"
FIELDS = ("panel", "assay_id", "role", "record_id", "bench", "n_amplicons", "primer_tm", "probe_tm")
NUM = r"(-?\d+(?:\.\d+)?)"


def read_tsv(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text().splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def parse_blocks(text: str) -> list[tuple[float, float | None]]:
    """[(limiting primer Tm, probe Tm or None)] per reported amplicon.

    The limiting primer is the colder of the two: an amplicon needs both to bind, so
    TNTBLAST's own `-e` applies to the minimum. Blocks are split on the `name =` line
    rather than on the `###` rule, because the rule is also printed around the header.
    """
    out: list[tuple[float, float | None]] = []
    for block in re.split(r"^name = ", text, flags=re.M)[1:]:
        fwd = re.search(rf"^forward primer tm = {NUM}", block, flags=re.M)
        rev = re.search(rf"^reverse primer tm = {NUM}", block, flags=re.M)
        if not (fwd and rev):
            continue
        probe = re.search(rf"^probe tm = {NUM}", block, flags=re.M)
        out.append((min(float(fwd.group(1)), float(rev.group(1))), float(probe.group(1)) if probe else None))
    return out


def oligo_line(assay) -> str:
    """TNTBLAST's assay line: name, forward, reverse, and a probe if there is one."""
    parts = [assay.id, assay.oligos.forward.matching_seq, assay.oligos.reverse.matching_seq]
    if assay.oligos.probe is not None:
        parts.append(assay.oligos.probe.matching_seq)
    return "\t".join(parts) + "\n"


def run_one(binary: str, oligos: Path, record: tuple[str, str], tmp: Path, floor: float, max_len: int):
    """TNTBLAST on one record. Returns its blocks, or None if the binary failed."""
    target = tmp / "target.fasta"
    target.write_text(f">{record[0]}\n{record[1]}\n")
    out = tmp / "out.txt"
    cmd = [
        binary, "-i", str(oligos), "-d", str(target), "-o", str(out),
        "-e", str(floor), "-E", str(floor), "-l", str(max_len), "-M", "F", "-a", "F",
    ]  # fmt: skip
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if proc.returncode != 0:
        print(f"FAILED {record[0]}: {proc.stderr.strip()[:200]}", file=sys.stderr)
        return None
    return parse_blocks(out.read_text() if out.exists() else "")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--panels", type=Path, default=PANELS)
    ap.add_argument("--cache", type=Path, default=CACHE)
    ap.add_argument("--tsv", type=Path, required=True)
    ap.add_argument(
        "--binary",
        default="tntblast",
        help="tntblast on PATH, or the full path inside the osx-64 env "
        "(conda run -n tntblast which tntblast)",
    )
    ap.add_argument(
        "--floor",
        type=float,
        default=20.0,
        help="minimum primer and probe Tm TNTBLAST will report at all (-e/-E). The "
        "comparison sweeps its own cut above this, so the floor only has to be low "
        "enough not to hide a row; 20 C is far below any usable annealing temperature.",
    )
    ap.add_argument("--max-length", type=int, default=5000)
    args = ap.parse_args(argv)

    rows: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for entry in read_tsv(args.panels):
            panel = REPO / entry["panel"]
            fasta = args.cache / (panel.stem + ".fasta")
            if not fasta.exists():
                print(f"skip {panel.stem}: no cached sequences", file=sys.stderr)
                continue
            assay = load_assay(REPO / entry["assay"])
            oligos = tmp / "oligos.txt"
            oligos.write_text(oligo_line(assay))
            seqs = {strip_version(rid): s for rid, s in read_fasta(fasta)}
            for r in read_tsv(panel):
                acc = strip_version(r["accession"])
                seq = seqs.get(acc)
                if seq is None:
                    print(f"skip {acc}: not in {fasta.name}", file=sys.stderr)
                    continue
                blocks = run_one(args.binary, oligos, (acc, seq), tmp, args.floor, args.max_length)
                if blocks is None:
                    return 1
                # The best amplicon is the one with the warmest limiting primer: that
                # is the one TNTBLAST would still report as the cut is raised.
                best = max(blocks, default=None, key=lambda b: b[0])
                rows.append(
                    {
                        "panel": panel.stem,
                        "assay_id": assay.id,
                        "role": entry.get("role", ""),
                        "record_id": acc,
                        "bench": r["bench"],
                        "n_amplicons": len(blocks),
                        "primer_tm": f"{best[0]:.4f}" if best else "",
                        "probe_tm": f"{best[1]:.4f}" if best and best[1] is not None else "",
                    }
                )
                print(
                    f"{panel.stem:34s} {acc:18s} {r['bench']:8s} "
                    f"{len(blocks):3d} amplicons  primer Tm {rows[-1]['primer_tm'] or '-':>8s}"
                    f"  probe Tm {rows[-1]['probe_tm'] or '-':>8s}"
                )

    args.tsv.parent.mkdir(parents=True, exist_ok=True)
    with args.tsv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    found = sum(1 for r in rows if r["n_amplicons"])
    print(f"\n{len(rows)} bench records, {found} with at least one amplicon at the floor -> {args.tsv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
