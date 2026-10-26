#!/usr/bin/env python3
"""Fit `scoring.engine: serial`'s two thresholds on the bench panels, leave-one-paper-out.

    python scripts/fit_panel_thresholds.py --out .tmp/fit/serial.json

S1 of `docs/2026-10-24-scoring-strategy-test-plan.md` Part 1. `engine: serial` has
been in the codebase and off since 2026-10-21, and its `oligo_ok_max`/`oligo_weak_max`
are placeholders copied from the budget thresholds `detect_max`/`reduced_max`. They
are the only two numbers the serial engine adds, and the bench panels are the only
type-level truth there is, so this is where they can be fitted rather than guessed.

IT RESCREENS EVERY CELL RATHER THAN REPLAYING ONE. `scripts/rescore.py` would be
quicker, but under `serial` the thresholds enter the choice of WHICH candidate
amplicon wins (`screen_one` ranks by call first), so a replay of a fixed table would
hold the budget engine's winner fixed and price a slightly different rule than the
one that would ship. The panels are 21 MB in total, so exactness is affordable here
in a way it is not over 2.7 M calls. That is the whole reason the replay boundary
names candidate selection as its one approximation.

LEAVE-ONE-PAPER-OUT, NEVER LEAVE-ONE-ROW-OUT. The rows of one panel share a primer
pair, a lab and a gel, so they are not independent draws; a row-wise split lets the
fit see its own test paper. The two Meyer files are ONE paper and are held out
together, which `docs/bench-panels/panels.tsv` records as the `paper` column.

Rahn 1992 is excluded from the fit and reported beside it. Its 41 negatives are
other genera, so they teach "sequence far from the target gives no band", a question
`scoring.max_pair_evalue` already answers; fitting on them would buy specificity
that is not in question and say nothing about drift.

WHAT COUNTS AS CORRECT, stated because it is a choice and not a measurement. A
`band` row is correct when the call is `detect` or `reduced`, i.e. the assay would
put a product on a gel. A `no_band` row is correct when it is `fail` or
`no_amplicon`. Treating `reduced` as a band is the SHIPPED reading, and it is
exactly what S3's probe switch proposes to change for probe chemistry (the influenza
mechanism), so this script holds it fixed and S3 varies it. Changing both at once
would make neither legible.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from assaywatch.accession import strip_version
from assaywatch.fasta import read_fasta
from assaywatch.score import load_config, screen_record
from assaywatch.validate import load_assay

REPO = Path(__file__).resolve().parents[1]

BAND_CALLS = {"detect", "reduced"}
NO_BAND_CALLS = {"fail", "no_amplicon", "indeterminate"}

# The grid. `oligo_ok_max` is a per-oligo "this oligo is fine" bar and
# `oligo_weak_max` a per-oligo "this oligo still works, badly" bar, so both live on
# the same scale as one oligo's penalty: a single 3'-window mismatch costs 3.0, a
# mid one 1.0, a 5' one 0.5. The range runs from "only a clean oligo is ok" to
# "two 3'-window mismatches are still weak rather than blocked".
OK_GRID = (0.5, 1.0, 1.5, 2.0, 3.0)
WEAK_GRID = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)


def read_panel(path: Path) -> dict[str, dict[str, str]]:
    with path.open() as fh:
        body = (line for line in fh if not line.startswith("#"))
        return {strip_version(r["accession"]): r for r in csv.DictReader(body, delimiter="\t")}


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open() as fh:
        body = (line for line in fh if not line.startswith("#"))
        return [r for r in csv.DictReader(body, delimiter="\t") if r.get("panel")]


def load_panel_data(manifest: Path, fasta_cache: Path) -> list[dict[str, Any]]:
    """One entry per panel: its assay, its rows, and the sequences keyed by accession."""
    out = []
    for row in read_manifest(manifest):
        panel_path = REPO / row["panel"]
        fasta = fasta_cache / f"{panel_path.stem}.fasta"
        if not fasta.exists():
            print(f"skipping {panel_path.stem}: no cached sequences at {fasta}", file=sys.stderr)
            continue
        panel = read_panel(panel_path)
        seqs = {rid.split()[0]: s for rid, s in read_fasta(fasta) if strip_version(rid.split()[0]) in panel}
        out.append(
            {
                "name": panel_path.stem,
                "paper": row["paper"],
                "role": row["role"],
                "assay": load_assay(REPO / row["assay"]),
                "panel": panel,
                "seqs": seqs,
            }
        )
    return out


def score_panel(entry: dict[str, Any], cfg: dict[str, Any]) -> dict[str, Any]:
    """One panel under one config: per-row calls and the correct/incorrect tally."""
    rows, tally = [], Counter()
    for acc, seq in entry["seqs"].items():
        call = screen_record(entry["assay"], acc, seq, cfg)
        bench = entry["panel"][strip_version(acc)]["bench"]
        label = entry["panel"][strip_version(acc)]["label"]
        want = BAND_CALLS if bench == "band" else NO_BAND_CALLS
        ok = call.call in want
        rows.append(
            {
                "accession": acc,
                "label": label,
                "bench": bench,
                "call": call.call,
                "penalty": call.penalty,
                "correct": ok,
            }
        )
        tally["correct" if ok else "wrong"] += 1
        tally[f"{bench}/{call.call}"] += 1
    return {"rows": rows, "tally": dict(tally), "correct": tally["correct"], "wrong": tally["wrong"]}


def cfg_for(ok_max: float, weak_max: float, base: dict[str, Any]) -> dict[str, Any]:
    cfg = {
        **base,
        "scoring": {
            **base["scoring"],
            "engine": "serial",
            "oligo_ok_max": ok_max,
            "oligo_weak_max": weak_max,
        },
    }
    return cfg


def cells() -> list[tuple[float, float]]:
    return [(a, b) for a, b in itertools.product(OK_GRID, WEAK_GRID) if b >= a]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--panels", type=Path, default=REPO / "docs" / "bench-panels" / "panels.tsv")
    ap.add_argument("--fasta-cache", type=Path, default=REPO / ".tmp" / "bench-panels")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None, help="write the full result as JSON")
    args = ap.parse_args(argv)

    base = load_config(args.config)
    data = load_panel_data(args.panels, args.fasta_cache)
    fitting = [d for d in data if d["role"] == "fitting"]
    control = [d for d in data if d["role"] != "fitting"]
    papers = sorted({d["paper"] for d in fitting})
    print(f"fitting papers: {', '.join(papers)}")
    print(f"control (never fitted): {', '.join(d['paper'] for d in control)}")
    print(f"grid: {len(cells())} cells, oligo_ok_max x oligo_weak_max with weak >= ok")
    print()

    # The shipped budget rule, as the row every cell is compared against.
    s0 = {d["name"]: score_panel(d, base) for d in data}
    print("S0 (shipped, engine: budget) per panel:")
    for d in data:
        r = s0[d["name"]]
        print(f"  {d['name']:34} {r['correct']:3} correct  {r['wrong']:3} wrong   [{d['role']}]")
    print()

    # The grid is swept over the FITTING panels only. The control panel is 288 MB of
    # Salmonella and other-genera genomes, so screening it 28 times would dominate the
    # run for no gain: it is not a fitting set, and what it has to say is whether the
    # ONE chosen cell starts detecting non-targets. It is therefore scored twice, at S0
    # and at the chosen cell, which is the question it answers.
    scores: dict[tuple[float, float], dict[str, Any]] = {}
    for ok_max, weak_max in cells():
        cfg = cfg_for(ok_max, weak_max, base)
        scores[(ok_max, weak_max)] = {d["name"]: score_panel(d, cfg) for d in fitting}

    def wrong_on(cell: tuple[float, float], papers_wanted: set[str]) -> int:
        per = scores[cell]
        return sum(per[d["name"]]["wrong"] for d in fitting if d["paper"] in papers_wanted)

    def lost_on(cell: tuple[float, float], papers_wanted: set[str]) -> list[str]:
        """Rows S0 scores correctly that this cell does not. Named, never counted away.

        The standing rule of the ladder: a candidate that loses a documented catch is
        a bad candidate, stated per catch and NOT netted against gains. So "fewest
        wrong" is the wrong objective - a cell can buy ten rescued positives with
        seven lost negatives and still read as an improvement, which is exactly what
        the unconstrained best does here. Selection is therefore constrained to cells
        that lose nothing, and the unconstrained best is printed beside it so the
        cost of the constraint is visible rather than hidden.
        """
        out = []
        for d in fitting:
            if d["paper"] not in papers_wanted:
                continue
            was = {r["accession"]: r for r in s0[d["name"]]["rows"]}
            for r in scores[cell][d["name"]]["rows"]:
                if was[r["accession"]]["correct"] and not r["correct"]:
                    out.append(f"{d['name']}:{r['label']} ({r['bench']} -> {r['call']})")
        return out

    def rank(cell: tuple[float, float], papers_wanted: set[str]) -> tuple:
        return (len(lost_on(cell, papers_wanted)), wrong_on(cell, papers_wanted), cell[0], cell[1])

    all_papers = set(papers)
    s0_wrong = sum(s0[d["name"]]["wrong"] for d in fitting)

    unconstrained = sorted(cells(), key=lambda c: (wrong_on(c, all_papers), c[0], c[1]))[0]
    lost_there = lost_on(unconstrained, all_papers)
    print(
        f"UNCONSTRAINED best cell (fewest wrong, netting allowed): {unconstrained} "
        f"-> {wrong_on(unconstrained, all_papers)} wrong against S0's {s0_wrong}"
    )
    print(f"  but it LOSES {len(lost_there)} rows S0 gets right:")
    for name in lost_there:
        print(f"    {name}")
    print("  Netting is forbidden, so this cell is not a candidate however good the total.")
    print()

    # The whole grid, because the interesting result is not the best cell but that
    # NO cell is clean. A table makes that checkable instead of a claim.
    print("the grid (lost = rows S0 gets right that this cell gets wrong):")
    print(f"  {'ok_max':>7} {'weak_max':>9} {'lost':>5} {'wrong':>6}   lost rows")
    for c in cells():
        lost = lost_on(c, all_papers)
        names = ", ".join(n.split(":")[1].split(" ")[0] for n in lost)
        print(f"  {c[0]:7} {c[1]:9} {len(lost):5} {wrong_on(c, all_papers):6}   {names}")
    print()

    best = sorted(cells(), key=lambda c: rank(c, all_papers))[0]
    clean = [c for c in cells() if not lost_on(c, all_papers)]
    print(
        f"CONSTRAINED best cell (loses nothing): oligo_ok_max={best[0]}, "
        f"oligo_weak_max={best[1]} -> {wrong_on(best, all_papers)} wrong against S0's {s0_wrong}"
    )
    print(f"  {len(clean)} of {len(cells())} cells lose nothing")
    if lost_on(best, all_papers):
        print("  WARNING: even the constrained best loses a row; the constraint is unsatisfiable")
    print()

    print("leave-one-paper-out (same constraint, fitted on the other papers only):")
    lopo_wrong, picks = 0, Counter()
    lopo_detail = []
    for held in papers:
        train = all_papers - {held}
        pick = sorted(cells(), key=lambda c: rank(c, train))[0]
        w = wrong_on(pick, {held})
        n = sum(len(scores[pick][d["name"]]["rows"]) for d in fitting if d["paper"] == held)
        lopo_wrong += w
        picks[pick] += 1
        lopo_detail.append({"held_out": held, "picked": list(pick), "wrong": w, "rows": n})
        print(f"  held out {held:16} picked {pick}  ->  {w} wrong of {n} rows")
    total_rows = sum(len(scores[best][d["name"]]["rows"]) for d in fitting)
    print(f"  LOPO total: {lopo_wrong} wrong of {total_rows} rows")
    print(f"  cells picked across folds: {dict(picks)}")
    print()

    print("the control panel, never fitted (a rule must not start detecting non-targets):")
    best_cfg = cfg_for(best[0], best[1], base)
    for d in control:
        scores[best][d["name"]] = score_panel(d, best_cfg)
        print(
            f"  {d['name']}: S0 {s0[d['name']]['wrong']} wrong -> best cell {scores[best][d['name']]['wrong']} wrong"
        )
    print()

    print("per-panel at the in-sample best cell, against S0:")
    for d in data:
        a, b = s0[d["name"]], scores[best][d["name"]]
        print(f"  {d['name']:34} {a['wrong']:3} -> {b['wrong']:3} wrong   [{d['role']}]")

    print()
    print("rows that MOVE at the in-sample best cell (panel truth vs call):")
    for d in data:
        a = {r["accession"]: r for r in s0[d["name"]]["rows"]}
        for r in scores[best][d["name"]]["rows"]:
            was = a[r["accession"]]
            if was["call"] != r["call"]:
                flag = "" if r["correct"] else "   <-- STILL WRONG"
                if was["correct"] and not r["correct"]:
                    flag = "   <-- LOST A CORRECT ROW"
                print(
                    f"  {d['name']:30} {r['label']:34} {r['bench']:8} {was['call']:11} -> {r['call']:11}{flag}"
                )

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(
            json.dumps(
                {
                    "grid": {"ok": OK_GRID, "weak": WEAK_GRID},
                    "s0": {k: v["tally"] for k, v in s0.items()},
                    "in_sample_best": list(best),
                    "in_sample_wrong": wrong_on(best, all_papers),
                    "s0_wrong_on_fitting": s0_wrong,
                    "lopo": {"wrong": lopo_wrong, "rows": total_rows, "folds": lopo_detail},
                    "by_cell": {
                        f"{a},{b}": {k: v["tally"] for k, v in per.items()} for (a, b), per in scores.items()
                    },
                },
                indent=2,
            )
            + "\n"
        )
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
