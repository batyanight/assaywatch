#!/usr/bin/env python3
"""The drift window and the record minimum, priced TOGETHER on the development set.

    python scripts/window_grid.py --calls results/2026-10-26/calls.tsv.gz
    python scripts/window_grid.py --calls ... --windows 12,24,36 --minimums 10,15,20,30 --tsv .tmp/grid.tsv

WHY TOGETHER. `recent_window_months: 24` with `min_records_for_drift: 15` is the pair
that made Bd (Boyle 2004) read "insufficient data" at 100% detected on 17 recent
records. Shorten the window and assays fall below the minimum; lengthen it and real
change is diluted into history. Each knob has been argued about alone; neither can be
set alone, because the thing they jointly control is how often the tool declines to
judge at all -- and a declined case is not a miss, so a matrix that only counts
catches cannot see the trade.

WHAT IS MEASURED PER CELL, from `scripts/retrospective.py --cases`: documented
failures caught, the PPV of `declining`, working assays called `declining`, and how
many cases the tool declined to judge. Every proportion carries the Jeffreys interval
that script prints, and at these counts the interval is the finding. Nothing here
chooses a cell: the development set is spent for threshold-setting
(`docs/validation-cases.tsv` header), so this table says what each pair would have
cost and bought, and the choice -- if any -- waits for a held-out read.

Report-stage only. Nothing is rescreened; each cell is a config overlay on the cached
calls table, which is why the whole grid is minutes.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
RETRO = REPO / "scripts" / "retrospective.py"

LINE = {
    "caught": re.compile(r"documented failures caught: (\d+)/(\d+)"),
    "ppv": re.compile(r"\(PPV\): (\d+)/(\d+)"),
    "alarms": re.compile(r"false alarms\): (\d+)/(\d+)"),
    "declined": re.compile(r"(\d+) case\(s\) the tool declined to judge"),
}


def overlay(base: str, window: int, minimum: int) -> str:
    out, n1 = re.subn(r"^  recent_window_months: \d+$", f"  recent_window_months: {window}", base, flags=re.M)
    out, n2 = re.subn(
        r"^  min_records_for_drift: \d+$", f"  min_records_for_drift: {minimum}", out, flags=re.M
    )
    if n1 != 1 or n2 != 1:
        raise SystemExit("config.yaml does not carry exactly one of each key at two-space indent")
    # max_window_months must stay >= the window or Settings refuses the file.
    m = re.search(r"^  max_window_months: (\d+)$", out, flags=re.M)
    if m and int(m.group(1)) < window:
        out = out.replace(m.group(0), f"  max_window_months: {window}")
    return out


def run_cell(calls: Path, cases: Path, cfg_text: str) -> dict[str, str]:
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as fh:
        fh.write(cfg_text)
        path = Path(fh.name)
    try:
        proc = subprocess.run(
            [sys.executable, str(RETRO), "--calls", str(calls), "--cases", str(cases), "--config", str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
    finally:
        path.unlink(missing_ok=True)
    if proc.returncode != 0:
        raise SystemExit(f"retrospective failed:\n{proc.stderr[-2000:]}")
    out: dict[str, str] = {}
    for key, rx in LINE.items():
        m = rx.search(proc.stdout)
        out[key] = "/".join(m.groups()) if m else "-"
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--calls", type=Path, required=True)
    ap.add_argument("--cases", type=Path, default=REPO / "docs" / "validation-cases.tsv")
    ap.add_argument("--config", type=Path, default=REPO / "config.yaml")
    ap.add_argument("--windows", default="12,24,36", help="recent_window_months values")
    ap.add_argument("--minimums", default="10,15,20,30", help="min_records_for_drift values")
    ap.add_argument("--tsv", type=Path, default=None)
    args = ap.parse_args(argv)

    base = args.config.read_text()
    windows = [int(x) for x in args.windows.split(",")]
    minimums = [int(x) for x in args.minimums.split(",")]
    rows = []
    print(f"{'window':>6} {'min':>4}  {'caught':>7} {'PPV':>6} {'alarms':>7} {'declined':>8}")
    for w in windows:
        for m in minimums:
            cell = run_cell(args.calls, args.cases, overlay(base, w, m))
            rows.append({"window_months": w, "min_records": m, **cell})
            print(
                f"{w:>6} {m:>4}  {cell['caught']:>7} {cell['ppv']:>6} {cell['alarms']:>7} {cell['declined']:>8}"
            )
    print()
    print("Each cell is one config overlay on the same cached calls; nothing was rescreened.")
    print("No cell is chosen here: the development set is spent for threshold-setting.")
    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            wtr = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
            wtr.writeheader()
            wtr.writerows(rows)
        print(f"wrote {args.tsv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
