#!/usr/bin/env python3
"""Fit `scoring.engine: serial`'s two thresholds on the bench panels, leave-one-paper-out.

    python scripts/fit_panel_thresholds.py --out .tmp/fit/serial.json

S1 of `docs/journal/2026-10-24-scoring-strategy-test-plan.md` Part 1. `engine: serial` has
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
import importlib.util
import itertools
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from assaywatch.accession import strip_version
from assaywatch.fasta import read_fasta
from assaywatch.score import decide, load_config, screen_record
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


# `scripts/rescore.py` holds the replay arithmetic and the positional-weight curve.
# Imported rather than re-implemented: a second copy of `score_primer`'s loop is
# exactly the duplication `assaywatch/accession.py`'s own docstring warns about, and
# the S0 control below exists to prove the two paths agree.
_spec = importlib.util.spec_from_file_location("rescore", REPO / "scripts" / "rescore.py")
rescore = importlib.util.module_from_spec(_spec)
sys.modules["rescore"] = rescore
_spec.loader.exec_module(rescore)


def footprints_of(entry: dict[str, Any], cfg: dict[str, Any]) -> list[dict[str, Any]]:
    """Screen the panel ONCE and keep what a replay needs, so a curve can be swept.

    `assaywatch/score.py` knows only the three-band step function, so a smooth decay
    cannot be screened with at all - it can only be replayed. One screen under the
    shipped config gives the mismatch configuration (which is what scoring is a
    function of) and every curve is then arithmetic over it.

    THE APPROXIMATION THIS BUYS, stated because the threshold fit above deliberately
    avoids it: candidate selection is frozen at the shipped rule's winner, exactly as
    in `scripts/rescore.py`. For these panels that is a small risk - one assay, one
    locus, a handful of records each - but it is not zero, and a curve that survived
    would need a `score.py` change and a real rescreen before it could ship.
    """
    out = []
    for acc, seq in entry["seqs"].items():
        call = screen_record(entry["assay"], acc, seq, cfg)
        row = entry["panel"][strip_version(acc)]
        out.append(
            {
                "accession": acc,
                "label": row["label"],
                "bench": row["bench"],
                "call": call.call,
                "reason": call.reason,
                "fwd": call.forward.mispairs if call.forward else (),
                "rev": call.reverse.mispairs if call.reverse else (),
                "probe": call.probe.mispairs if call.probe else (),
                "fwd_amb": len(call.forward.ambiguous) if call.forward else 0,
                "rev_amb": len(call.reverse.ambiguous) if call.reverse else 0,
                "probe_amb": len(call.probe.ambiguous) if call.probe else 0,
                "has_probe": call.probe is not None,
                "probe_len": len(entry["assay"].oligos.probe.matching_seq)
                if entry["assay"].oligos.probe
                else None,
            }
        )
    return out


def score_panel_replayed(
    footprints: list[dict[str, Any]],
    cfg: dict[str, Any],
    weight: dict[str, Any] | None,
    undetected: tuple[str, ...] = (),
    chemistry: str | None = None,
) -> dict[str, Any]:
    """The same tally as `score_panel`, from a frozen footprint plus a curve.

    `undetected` is S3's probe switch: chemistries for which a `reduced` call is not
    a detection. On a panel that means a `band` row scored `reduced` becomes an
    ERROR, because the paper saw a product and the model now predicts a miss. That
    reading is forced by the switch's own semantics, not a choice: if `reduced` is
    not a detection then predicting it where the bench saw a band is a false
    negative.
    """
    rows, tally = [], Counter()
    for f in footprints:
        if f["call"] in rescore.PASSTHROUGH_CALLS:
            call = f["call"]
            penalty = None
        else:
            fs = rescore.primer_score(rescore.parse_mispairs(",".join(f["fwd"])), f["fwd_amb"], cfg, weight)
            rs = rescore.primer_score(rescore.parse_mispairs(",".join(f["rev"])), f["rev_amb"], cfg, weight)
            ps = None
            if f["has_probe"]:
                ps = rescore.probe_score(
                    rescore.parse_mispairs(",".join(f["probe"])), f["probe_amb"], f["probe_len"] or 0, cfg
                )
            call, _, penalty = decide(fs, rs, ps, cfg)
            if f["reason"].startswith(rescore.PROBE_ABSENT_REASON):
                call = "fail"
            elif call == "reduced" and chemistry is not None and str(chemistry) in undetected:
                call = "fail"
        want = BAND_CALLS if f["bench"] == "band" else NO_BAND_CALLS
        ok = call in want
        rows.append(
            {
                "accession": f["accession"],
                "label": f["label"],
                "bench": f["bench"],
                "call": call,
                "penalty": penalty,
                "correct": ok,
            }
        )
        tally["correct" if ok else "wrong"] += 1
        tally[f"{f['bench']}/{call}"] += 1
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


# S2's grid. `w0` is the weight at the 3'-terminal base and `half_distance` is how
# many bases it takes to halve. The shipped step function is w=3.0 flat to d=5, then
# 1.0 to d=10, then 0.5, so w0 near 3.0 keeps the terminal scale while the decay
# replaces the cliff at d=6 that no measurement supports.
W0_GRID = (2.0, 2.5, 3.0, 3.5, 4.0)
HALF_GRID = (1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0)


def weight_cells() -> list[tuple[float, float]]:
    return list(itertools.product(W0_GRID, HALF_GRID))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--panels", type=Path, default=REPO / "docs" / "bench-panels" / "panels.tsv")
    ap.add_argument("--fasta-cache", type=Path, default=REPO / ".tmp" / "bench-panels")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None, help="write the full result as JSON")
    ap.add_argument(
        "--grid",
        choices=("thresholds", "weight"),
        default="thresholds",
        help="thresholds = S1's oligo_ok_max x oligo_weak_max, by real rescreen per cell. "
        "weight = S2's exponential positional decay, by replay, because score.py knows "
        "only the three-band step function and cannot screen a curve",
    )
    args = ap.parse_args(argv)

    base = load_config(args.config)
    data = load_panel_data(args.panels, args.fasta_cache)
    fitting = [d for d in data if d["role"] == "fitting"]
    control = [d for d in data if d["role"] != "fitting"]
    papers = sorted({d["paper"] for d in fitting})
    grid = cells() if args.grid == "thresholds" else weight_cells()
    print(f"fitting papers: {', '.join(papers)}")
    print(f"control (never fitted): {', '.join(d['paper'] for d in control)}")
    if args.grid == "thresholds":
        print(f"grid: {len(grid)} cells, oligo_ok_max x oligo_weak_max with weak >= ok (rescreened per cell)")
    else:
        print(f"grid: {len(grid)} cells, w0 x half_distance, exponential decay (REPLAYED, not rescreened)")
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
    scores: dict[Any, dict[str, Any]] = {}
    if args.grid == "thresholds":
        for cell in grid:
            scores[cell] = {d["name"]: score_panel(d, cfg_for(cell[0], cell[1], base)) for d in fitting}
    else:
        prints = {d["name"]: footprints_of(d, base) for d in data}
        # The control that the replay path agrees with the screen, before any curve is
        # swept over it. Without this an S2 result would rest on an unverified second
        # implementation of score_primer's loop, which is how the first chance-pair
        # test nearly shipped: a no-op is indistinguishable from a clean pass.
        bad = []
        for d in data:
            got = score_panel_replayed(prints[d["name"]], base, None)
            want = s0[d["name"]]
            a = {r["accession"]: r["call"] for r in want["rows"]}
            b = {r["accession"]: r["call"] for r in got["rows"]}
            bad += [f"{d['name']}:{k} screen={a[k]} replay={b[k]}" for k in a if a[k] != b[k]]
        if bad:
            print("REPLAY CONTROL FAILED - the replay does not reproduce the screen:")
            for x in bad:
                print(f"  {x}")
            return 1
        print(
            f"replay control: the curve-less replay reproduces the screen on all "
            f"{sum(len(v) for v in prints.values())} panel rows."
        )
        print()
        for cell in grid:
            spec = {"kind": "exponential", "w0": cell[0], "half_distance": cell[1]}
            scores[cell] = {d["name"]: score_panel_replayed(prints[d["name"]], base, spec) for d in fitting}

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

    unconstrained = sorted(grid, key=lambda c: (wrong_on(c, all_papers), c[0], c[1]))[0]
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
    a_name, b_name = ("ok_max", "weak_max") if args.grid == "thresholds" else ("w0", "half_dist")
    print(f"  {a_name:>7} {b_name:>9} {'lost':>5} {'wrong':>6}   lost rows")
    for c in grid:
        lost = lost_on(c, all_papers)
        names = ", ".join(n.split(":")[1].split(" ")[0] for n in lost)
        print(f"  {c[0]:7} {c[1]:9} {len(lost):5} {wrong_on(c, all_papers):6}   {names}")
    print()

    best = sorted(grid, key=lambda c: rank(c, all_papers))[0]
    clean = [c for c in grid if not lost_on(c, all_papers)]
    print(
        f"CONSTRAINED best cell (loses nothing): oligo_ok_max={best[0]}, "
        f"oligo_weak_max={best[1]} -> {wrong_on(best, all_papers)} wrong against S0's {s0_wrong}"
    )
    print(f"  {len(clean)} of {len(grid)} cells lose nothing")
    if lost_on(best, all_papers):
        print("  WARNING: even the constrained best loses a row; the constraint is unsatisfiable")
    print()

    print("leave-one-paper-out (same constraint, fitted on the other papers only):")
    lopo_wrong, picks = 0, Counter()
    lopo_detail = []
    for held in papers:
        train = all_papers - {held}
        pick = sorted(grid, key=lambda c: rank(c, train))[0]
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
    for d in control:
        if args.grid == "thresholds":
            scores[best][d["name"]] = score_panel(d, cfg_for(best[0], best[1], base))
        else:
            spec = {"kind": "exponential", "w0": best[0], "half_distance": best[1]}
            scores[best][d["name"]] = score_panel_replayed(prints[d["name"]], base, spec)
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
