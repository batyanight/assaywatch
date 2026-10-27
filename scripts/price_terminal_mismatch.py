#!/usr/bin/env python3
"""Price `terminal_mismatch_fails: false` for conventional PCR on the bench panels.

    python scripts/price_terminal_mismatch.py
    python scripts/price_terminal_mismatch.py --tsv .tmp/terminal/rows.tsv

WHY THIS, AND WHY NOW. `scoring.terminal_mismatch_fails: true` makes a mismatch in
the last base of a primer an automatic `fail` whatever else the oligo does. It is a
qPCR-strength rule applied to a registry that is 155 of 209 conventional PCR
(2026-10-27), and `scoring.by_chemistry` ships empty, so the same rule covers a
hydrolysis probe read by fluorescence and an endpoint PCR read as a band on a gel.
The paired bench comparison of 2026-10-27 then measured what that costs: the shipped
rule makes **23 false negatives against 1 false positive**
(docs/journal/2026-10-27-thermo-vs-penalty-paired.md). An error distribution that
one-sided is a rule that is too strict, not a rule that is noisy.

WHAT MAKES THIS DIFFERENT FROM THE 2026-10-26 MEASUREMENT. That one exempted
conventional chemistry across the whole registry and found 251 calls of 2.7 M moved
and no verdict changed anywhere (docs/journal/2026-10-26-s3-chemistry-switches.md).
That is a statement about how OFTEN the rule is load-bearing in the archive, where a
record carrying a terminal mismatch usually carries others that clear `reduced_max`
on their own. It is not a statement about whether the rule is RIGHT, because the
archive has no answers in it. The bench panels do: 179 rows of published
band/no_band, 122 band and 57 no_band, on assays the registry holds.

NOTHING IS FITTED HERE, which is the point. The switch is one boolean with no free
parameter, so there is no threshold to tune and no in-sample advantage to declare --
unlike the thermodynamic arm of the 2026-10-27 comparison, whose cutoff was chosen on
these same rows. A paired test on these 179 rows is therefore the cleanest evidence
this project can produce about a scoring rule without new wet-lab work.

WHAT IT CANNOT SETTLE. These are 7 papers, not 7 independent measurements of PCR:
rows within a panel share a primer pair, a lab and a gel. Three panels have no
negatives at all, so they cannot punish a loosening. Rahn 1992 is the control -- its
41 negatives are other genera with no target gene, so nothing anchors and no scoring
change can move them. And `by_chemistry` can carry more than this one key; the
commented worked example in config.yaml also drops `primer_3prime_penalty` to 2.0,
which this script prices separately rather than bundling, because two changes at once
make neither legible.
"""

from __future__ import annotations

import argparse
import copy
import csv
import sys
from math import comb
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from assaywatch.accession import strip_version  # noqa: E402
from assaywatch.fasta import read_fasta  # noqa: E402
from assaywatch.score import RESOLVED, load_config, screen_record  # noqa: E402
from assaywatch.validate import load_assay  # noqa: E402

PANELS = REPO / "docs" / "bench-panels" / "panels.tsv"
CACHE = REPO / ".tmp" / "bench-panels"

#: A row is predicted to put a product on a gel.
BAND_CALLS = ("detect", "reduced")

#: The candidates, each a `scoring.by_chemistry.conventional` block. Priced one at a
#: time: the terminal-mismatch rule alone is the change the 23 false negatives argue
#: for, and the penalty drop is the worked example config.yaml already writes out.
#: Every arm names its thresholds absolutely, because the SHIPPED baseline moved on
#: 2026-10-27: `primer_3prime_penalty` for conventional is now 2.0, so `revert_3.0`
#: is what reproduces the pre-ship comparison and `shipped` is no longer the strict
#: rule. Read `revert_3.0` against the others to see the original measurement.
CANDIDATES: dict[str, dict[str, Any]] = {
    "revert_3.0": {"primer_3prime_penalty": 3.0},
    "terminal_only": {"primer_3prime_penalty": 3.0, "terminal_mismatch_fails": False},
    "penalty_2.5": {"primer_3prime_penalty": 2.5},
    "penalty_2.0": {"primer_3prime_penalty": 2.0},
    "penalty_2.0_no_terminal": {"primer_3prime_penalty": 2.0, "terminal_mismatch_fails": False},
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    """Rows of a bench panel or the panel index, skipping `#` commentary."""
    lines = [ln for ln in path.read_text().splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def with_override(cfg: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """`cfg` with one `scoring.by_chemistry.conventional` block applied.

    A deep copy, because `score.config_for` caches the merged block on the dict it is
    handed and a shared mutable would leak one arm's thresholds into the other.

    THE CACHE MUST ALSO BE DROPPED, and this was a real bug until the shipped config
    carried an override of its own. `load_config` precomputes `_config_by_chemistry`
    whenever `by_chemistry` is non-empty, a deep copy copies it, and `config_for`
    then answers from it -- so every arm would have scored with the SHIPPED
    conventional penalty and all the arms would have agreed, which looks exactly
    like a clean null result. Popping it forces each arm to resolve its own.
    """
    out = copy.deepcopy(cfg)
    out.pop(RESOLVED, None)
    scoring = out.setdefault("scoring", {})
    scoring["by_chemistry"] = {"conventional": dict(override)}
    return out


def mcnemar_exact(b: int, c: int) -> float:
    """Two-sided exact McNemar p-value on the discordant counts.

    Only the discordant pairs carry information: b rows where the shipped rule is
    right and the candidate wrong, c the reverse. Under the null they split 50/50, so
    this is an exact two-sided binomial test on b of b+c.
    """
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    tail = sum(comb(n, i) for i in range(k + 1)) / 2**n
    return min(1.0, 2 * tail)


def table(pred: list[bool], truth: list[bool]) -> tuple[int, int, int, int]:
    tp = sum(p and t for p, t in zip(pred, truth, strict=True))
    tn = sum((not p) and (not t) for p, t in zip(pred, truth, strict=True))
    fp = sum(p and (not t) for p, t in zip(pred, truth, strict=True))
    fn = sum((not p) and t for p, t in zip(pred, truth, strict=True))
    return tp, tn, fp, fn


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--panels", type=Path, default=PANELS)
    ap.add_argument("--cache", type=Path, default=CACHE)
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--tsv", type=Path, default=None, help="per-record detail")
    args = ap.parse_args(argv)

    base = load_config(args.config)
    arms = {"shipped": base} | {name: with_override(base, ov) for name, ov in CANDIDATES.items()}

    rows: list[dict[str, Any]] = []
    for entry in read_tsv(args.panels):
        panel = REPO / entry["panel"]
        assay = load_assay(REPO / entry["assay"])
        fasta = args.cache / (panel.stem + ".fasta")
        if not fasta.exists():
            print(f"skip {panel.stem}: no cached sequences at {fasta}", file=sys.stderr)
            continue
        seqs = {strip_version(rid): s for rid, s in read_fasta(fasta)}
        for r in read_tsv(panel):
            acc = strip_version(r["accession"])
            seq = seqs.get(acc)
            if seq is None:
                print(f"skip {acc}: not in {fasta.name}", file=sys.stderr)
                continue
            row: dict[str, Any] = {
                "panel": panel.stem,
                "assay_id": assay.id,
                "chemistry": assay.chemistry.value,
                "role": entry.get("role", ""),
                "record_id": acc,
                "label": r.get("label", ""),
                "bench_band": r["bench"] == "band",
            }
            for name, cfg in arms.items():
                call = screen_record(assay, acc, seq, cfg)
                row[f"call_{name}"] = call.call
                row[f"band_{name}"] = call.call in BAND_CALLS
            rows.append(row)

    if not rows:
        print("no rows scored", file=sys.stderr)
        return 1

    truth = [r["bench_band"] for r in rows]
    conv = sum(r["chemistry"] == "conventional" for r in rows)
    print(f"rows scored: {len(rows)}   conventional: {conv}   other chemistry: {len(rows) - conv}")
    print(f"bench outcomes: {sum(truth)} band, {len(truth) - sum(truth)} no_band")
    print()

    for name in arms:
        pred = [r[f"band_{name}"] for r in rows]
        tp, tn, fp, fn = table(pred, truth)
        print(
            f"{name:22s} acc {(tp + tn) / len(truth):6.1%}   TP {tp:3d}  TN {tn:3d}  FP {fp:3d}  FN {fn:3d}"
        )
    print()

    ship = [r["band_shipped"] for r in rows]
    for name in CANDIDATES:
        cand = [r[f"band_{name}"] for r in rows]
        moved = sum(a != b for a, b in zip(ship, cand, strict=True))
        b = sum((a == t) and (c != t) for a, c, t in zip(ship, cand, truth, strict=True))
        c = sum((c == t) and (a != t) for a, c, t in zip(ship, cand, truth, strict=True))
        print(f"{name}: {moved} of {len(rows)} predictions move")
        print(f"  shipped right / candidate wrong: {b}")
        print(f"  candidate right / shipped wrong: {c}")
        print(f"  McNemar exact two-sided p = {mcnemar_exact(b, c):.4f}")
        per_panel: dict[str, tuple[int, int]] = {}
        for r in rows:
            if r["band_shipped"] == r[f"band_{name}"]:
                continue
            right = r[f"band_{name}"] == r["bench_band"]
            w, x = per_panel.get(r["panel"], (0, 0))
            per_panel[r["panel"]] = (w + int(right), x + int(not right))
        for panel, (gained, lost) in sorted(per_panel.items()):
            print(f"    {panel:34s} {gained:3d} fixed, {lost:3d} broken")
        print()

    # A loosening can only turn a predicted no_band into a band, so it can only
    # fix false negatives and only break false positives. That makes a band-heavy
    # panel set structurally generous to it, and it is why the negatives are
    # counted separately here: Rahn's 41 are other genera where nothing anchors and
    # no scoring change can touch them, so the only rows that can punish a
    # loosening are the 16 negatives in the other panels.
    informative = [r for r in rows if not r["bench_band"] and r["panel"] != "rahn-1992-salmonella-invA"]
    print(f"negatives that can punish a loosening (non-Rahn no_band rows): {len(informative)}")
    for name in CANDIDATES:
        broke = sum(r[f"band_{name}"] and not r["band_shipped"] for r in informative)
        print(f"  {name:22s} newly predicts a band on {broke} of them")
    print()

    print("No parameter is fitted here: each candidate is a fixed config block, so")
    print("these accuracies are not in-sample upper bounds. The rows are 7 papers,")
    print("not 7 independent measurements of PCR, and three panels have no negatives.")

    if args.tsv:
        cols = list(rows[0])
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {args.tsv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
