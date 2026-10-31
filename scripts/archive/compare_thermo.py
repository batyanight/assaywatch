#!/usr/bin/env python3
"""Put a thermodynamic predictor and the shipped penalty rule on the SAME wet-lab rows.

    python scripts/compare_thermo.py                      # all panels, cached sequences
    python scripts/compare_thermo.py --tsv out/rows.tsv    # per-record detail

WHY THIS EXISTS. `docs/related-work.md` concedes that PCR_strainer "wraps
thermonucleotideBLAST, so matching is thermodynamic, not a positional penalty
table", and until now the project's answer to "why not just use PCR_strainer?"
was a feature table. No head-to-head against any external tool had ever been
run: none of PCR_strainer, TNTBLAST, openPrimeR or GoPrime appears anywhere in
`assaywatch/`, `scripts/`, `tests/`, the Snakefile or `environment.yml`, and
`results/benchmarks/` holds Snakemake wall-clock rather than accuracy.

WHAT THIS IS NOT. It is not that comparison. TNTBLAST is on bioconda for osx-64
and linux-64 but not osx-arm64, and running the osx-64 build needs Rosetta 2,
which is not installed on this machine and whose installation is a system change
requiring admin rights. So the thermodynamic arm here is primer3's
nearest-neighbour model, which is already a pinned dependency
(`assaywatch/thermo.py`, primer3-py 2.3.1). That is weaker evidence against the
"why not PCR_strainer" question -- a different engine, and not the one a reviewer
will name -- but it is the same EXPERIMENT: a physically grounded predictor and a
hand-set penalty table, on one set of labelled wet-lab outcomes, compared pairwise.

THE DESIGN, and why it is pairwise. `docs/bench-panels/` holds 179 labelled
outcomes over 7 papers, which is far too few for two independent accuracy
estimates to separate: each would carry an interval around 20 points wide. That is
exactly why the in-sample 5/11-vs-6/11 deltas this project has been weighing are
uninformative. McNemar's test looks only at the DISCORDANT pairs -- the rows where
the two predictors disagree -- and asks whether the disagreements fall
asymmetrically, which is answerable at this sample size.

THE ADVANTAGE GIVEN TO THE THERMODYNAMIC ARM, deliberately. Its one free
parameter, the delta-Tm below which it predicts no band, is chosen to MAXIMISE its
accuracy on these same rows. So its score is an in-sample upper bound, while the
penalty rule runs exactly as it ships. The comparison is therefore biased in
favour of thermodynamics, which makes a tie or a loss for it the informative
outcome.

REGISTRATION, which is the known defect in the thermo column. `thermo.duplex_tm`
calls `primer3.calc_heterodimer`, which returns the MOST STABLE structure between
two sequences rather than the in-register duplex. On a heavily mismatched site it
can find a shifted, shorter near-perfect duplex and report an optimistically small
|delta-Tm| -- least trustworthy on exactly the records that matter. This script
measures how often that happens here, from the returned alignment, and reports it
rather than assuming it away.
"""

from __future__ import annotations

import argparse
import csv
import sys
from math import comb
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))

from assaywatch.accession import strip_version  # noqa: E402
from assaywatch.fasta import read_fasta  # noqa: E402
from assaywatch.score import load_config, screen_record  # noqa: E402
from assaywatch.thermo import duplex_tm, resolve  # noqa: E402
from assaywatch.validate import load_assay  # noqa: E402

PANELS = REPO / "docs" / "bench-panels" / "panels.tsv"
CACHE = REPO / ".tmp" / "bench-panels"

#: Predicted band under the shipped rule.
BAND_CALLS = ("detect", "reduced")


def read_tsv(path: Path) -> list[dict[str, str]]:
    """Rows of a bench panel or the panel index, skipping `#` commentary."""
    lines = [ln for ln in path.read_text().splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def primer3_off_register(oligo: str, site: str) -> bool:
    """Would primer3 have scored this pair out of register? The OLD defect, measured.

    Kept after `thermo.duplex_tm` was fixed, because the fix is only worth
    believing if the thing it removed is still counted: this is what the
    2026-10-27 run reported as 99 of 179 rows. `calc_heterodimer` returns the most
    stable structure between two sequences, so if the paired run in its ascii
    structure is shorter than the oligo it found a shifted or truncated duplex and
    its Tm was not the in-register one. Conservative: anything unparseable counts
    as out of register rather than quietly passing.
    """
    import primer3

    from assaywatch.iupac import reverse_complement

    o, t, _ = resolve(oligo, site)
    try:
        r = primer3.calc_heterodimer(o, reverse_complement(t), output_structure=True)
    except (OSError, ValueError, RuntimeError):
        return True
    if not r.structure_found:
        return True
    paired = max(
        (len(ln.split("\t", 1)[1].strip()) for ln in r.ascii_structure_lines if "\t" in ln),
        default=0,
    )
    return paired < len(o)


def score_record(assay: Any, rid: str, seq: str, cfg: dict[str, Any]) -> dict[str, Any]:
    """One record under both predictors."""
    call = screen_record(assay, rid, seq, cfg)
    oligos = {
        "forward": assay.oligos.forward.matching_seq,
        "reverse": assay.oligos.reverse.matching_seq,
    }
    if assay.oligos.probe is not None:
        oligos["probe"] = assay.oligos.probe.matching_seq

    dtms: list[float] = []
    off_register = 0
    unpriced = 0
    for key, site in (call.extra.get("sites") or {}).items():
        if key not in oligos or site is None:
            continue
        tm, perfect, _ = duplex_tm(oligos[key], site.window, cfg)
        if tm is None:
            # Adjacent mismatches have no measured nearest-neighbour term, so the
            # model withholds the number rather than scoring the step as free.
            unpriced += 1
            continue
        dtms.append(tm - perfect)
        if primer3_off_register(oligos[key], site.window):
            off_register += 1
    return {
        "record_id": rid,
        "call": call.call,
        "penalty_band": call.call in BAND_CALLS,
        "min_dtm": min(dtms) if dtms else None,
        "n_sites": len(dtms),
        "off_register": off_register,
        "unpriced": unpriced,
    }


def mcnemar_exact(b: int, c: int) -> float:
    """Two-sided exact McNemar p-value on the discordant counts.

    Only the DISCORDANT pairs carry information: b rows where predictor A is
    right and B wrong, c the reverse. Under the null they split 50/50, so this is
    an exact two-sided binomial test on b of b+c. The concordant rows -- both
    right or both wrong -- say nothing about which predictor is better, which is
    what makes 179 paired rows usable where two separate accuracy estimates are
    not.
    """
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    tail = sum(comb(n, i) for i in range(k + 1)) / 2**n
    return min(1.0, 2 * tail)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--panels", type=Path, default=PANELS)
    ap.add_argument("--cache", type=Path, default=CACHE)
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--tsv", type=Path, default=None, help="per-record detail")
    ap.add_argument(
        "--tntblast",
        type=Path,
        default=None,
        help="scripts/tntblast_arm.py output: adds TNTBLAST as a third arm on the same rows",
    )
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    rows: list[dict[str, Any]] = []

    for entry in read_tsv(args.panels):
        panel = REPO / entry["panel"]
        assay_path = REPO / entry["assay"]
        fasta = args.cache / (panel.stem + ".fasta")
        if not fasta.exists():
            print(f"skip {panel.stem}: no cached sequences at {fasta}", file=sys.stderr)
            continue
        assay = load_assay(assay_path)
        seqs = {strip_version(rid): s for rid, s in read_fasta(fasta)}
        for r in read_tsv(panel):
            acc = strip_version(r["accession"])
            seq = seqs.get(acc)
            if seq is None:
                print(f"skip {acc}: not in {fasta.name}", file=sys.stderr)
                continue
            out = score_record(assay, acc, seq, cfg)
            out |= {
                "panel": panel.stem,
                "assay_id": assay.id,
                "role": entry.get("role", ""),
                "label": r.get("label", ""),
                "bench_band": r["bench"] == "band",
            }
            rows.append(out)

    if not rows:
        print("no rows scored", file=sys.stderr)
        return 1

    truth = [r["bench_band"] for r in rows]
    pen = [r["penalty_band"] for r in rows]

    # The thermodynamic arm, at the threshold that suits it best on these rows.
    scored = [r for r in rows if r["min_dtm"] is not None]
    best = None
    for i in range(-400, 51):
        cut = i / 10.0
        pred = [(r["min_dtm"] is not None and r["min_dtm"] >= cut) for r in rows]
        acc = sum(p == t for p, t in zip(pred, truth, strict=True))
        if best is None or acc > best[0]:
            best = (acc, cut, pred)
    assert best is not None
    _, cut, thermo = best

    # The TNTBLAST arm, read from scripts/tntblast_arm.py and given the same one free
    # parameter as primer3's: one Tm cut, fitted on these same rows. The cut applies to
    # the LIMITING oligo of the best amplicon -- the colder of the two primers, or the
    # probe where there is one -- because an amplicon reported by a probe assay needs
    # all three to bind, which is what TNTBLAST's own -e/-E pair expresses.
    tnt_pred: list[bool] | None = None
    tnt_cuts: tuple[float, float] = (0.0, 0.0)
    tnt_missing = 0
    if args.tntblast:
        tnt: dict[tuple[str, str], tuple[float, float | None] | None] = {}
        for r in read_tsv(args.tntblast):
            key = (r["panel"], r["record_id"])
            if not r["n_amplicons"] or int(r["n_amplicons"]) == 0 or not r["primer_tm"]:
                tnt[key] = None  # no amplicon at any cut
                continue
            tnt[key] = (float(r["primer_tm"]), float(r["probe_tm"]) if r["probe_tm"] else None)
        pairs = [tnt.get((r["panel"], r["record_id"])) for r in rows]
        tnt_missing = sum(1 for r in rows if (r["panel"], r["record_id"]) not in tnt)
        # TWO free parameters, deliberately -- its own -e and -E, each fitted on these
        # same rows. One cut on the limiting oligo would be the tidier comparison and
        # the objection would be that TNTBLAST was handed one knob where it ships with
        # two, so it gets both, and its accuracy is that much further an upper bound.
        best_t = None
        for i in range(0, 161):
            ecut = i / 2.0
            for j in range(0, 161):
                pcut = j / 2.0
                pred = [(x is not None and x[0] >= ecut and (x[1] is None or x[1] >= pcut)) for x in pairs]
                acc = sum(p == t for p, t in zip(pred, truth, strict=True))
                if best_t is None or acc > best_t[0]:
                    best_t = (acc, (ecut, pcut), pred)
        assert best_t is not None
        _, tnt_cuts, tnt_pred = best_t

        # And the same fit PER PANEL, which is the interesting number: an annealing
        # temperature is a property of an assay, not of a method, so a single global
        # cut asks TNTBLAST to be right about seven protocols at once. This is an
        # oracle -- each panel keeps its own best pair -- so it is an upper bound on
        # what per-assay conditions could buy a thermodynamic predictor.
        tnt_oracle = []
        for panel_name in sorted({r["panel"] for r in rows}):
            idx = [i for i, r in enumerate(rows) if r["panel"] == panel_name]
            sub_truth = [truth[i] for i in idx]
            sub_pairs = [pairs[i] for i in idx]
            bestp = None
            for i in range(0, 161):
                ecut = i / 2.0
                for j in range(0, 161):
                    pcut = j / 2.0
                    pred = [
                        (x is not None and x[0] >= ecut and (x[1] is None or x[1] >= pcut)) for x in sub_pairs
                    ]
                    acc = sum(p == t for p, t in zip(pred, sub_truth, strict=True))
                    if bestp is None or acc > bestp[0]:
                        bestp = (acc, (ecut, pcut), len(idx))
            assert bestp is not None
            tnt_oracle.append((panel_name, *bestp))

    def table(pred):
        tp = sum(p and t for p, t in zip(pred, truth, strict=True))
        tn = sum((not p) and (not t) for p, t in zip(pred, truth, strict=True))
        fp = sum(p and (not t) for p, t in zip(pred, truth, strict=True))
        fn = sum((not p) and t for p, t in zip(pred, truth, strict=True))
        return tp, tn, fp, fn

    print(f"rows scored: {len(rows)}   with a thermo site: {len(scored)}")
    print(f"bench outcomes: {sum(truth)} band, {len(truth) - sum(truth)} no_band")
    print(f"sites the NN tables cannot price (adjacent mismatches): {sum(r['unpriced'] for r in rows)}")
    print(
        f"of the priced sites, how many primer3 would have mis-registered: {sum(r['off_register'] for r in rows)}"
    )
    print()
    arms = [("penalty rule (as shipped)", pen), (f"primer3 dTm >= {cut:g} C", thermo)]
    if tnt_pred is not None:
        arms.append((f"tntblast -e {tnt_cuts[0]:g} -E {tnt_cuts[1]:g}", tnt_pred))
        if tnt_missing:
            print(f"WARNING {tnt_missing} rows have no tntblast row and count as no amplicon")
    for name, pred in arms:
        tp, tn, fp, fn = table(pred)
        acc = (tp + tn) / len(truth)
        print(f"{name:28s}  acc {acc:6.1%}   TP {tp:3d}  TN {tn:3d}  FP {fp:3d}  FN {fn:3d}")

    def pairwise(name_a: str, a: list[bool], name_b: str, b_pred: list[bool]) -> None:
        differ = sum(x != y for x, y in zip(a, b_pred, strict=True))
        a_right = sum((x == t) and (y != t) for x, y, t in zip(a, b_pred, truth, strict=True))
        b_right = sum((y == t) and (x != t) for x, y, t in zip(a, b_pred, truth, strict=True))
        print()
        print(f"{name_a} against {name_b}: predictions differ on {differ} rows")
        print(f"  {name_a} right / {name_b} wrong: {a_right}")
        print(f"  {name_b} right / {name_a} wrong: {b_right}")
        print(f"  McNemar exact two-sided p = {mcnemar_exact(a_right, b_right):.4f}")

    pairwise("penalty", pen, "primer3", thermo)
    if tnt_pred is not None:
        pairwise("penalty", pen, "tntblast", tnt_pred)
        pairwise("primer3", thermo, "tntblast", tnt_pred)
    print()
    print("Per panel (bench band/no_band, then each predictor's errors):")
    for panel in sorted({r["panel"] for r in rows}):
        sub = [r for r in rows if r["panel"] == panel]
        st = [r["bench_band"] for r in sub]
        ep = sum(r["penalty_band"] != r["bench_band"] for r in sub)
        et = sum(((r["min_dtm"] is not None and r["min_dtm"] >= cut) != r["bench_band"]) for r in sub)
        role = sub[0]["role"]
        print(
            f"  {panel:34s} {sum(st):3d}/{len(st) - sum(st):<3d}  "
            f"penalty {ep:3d} wrong   thermo {et:3d} wrong   ({role})"
        )
    if tnt_pred is not None:
        right = sum(a for _, a, _, _ in tnt_oracle)
        print()
        print(
            f"tntblast with a SEPARATE cut fitted per panel (an oracle): "
            f"{right}/{len(truth)} = {right / len(truth):.1%}"
        )
        for panel_name, acc, (ecut, pcut), n in tnt_oracle:
            print(f"  {panel_name:34s} {acc:3d}/{n:<3d}  -e {ecut:g} -E {pcut:g}")
    print()
    print("The thermodynamic arm's threshold was fitted on these same rows, so its")
    print("accuracy is an in-sample upper bound; the penalty rule ran as it ships.")
    print("primer3 is a model, not ground truth. The bench labels are the arbiter.")

    if args.tsv:
        cols = [
            "panel",
            "assay_id",
            "role",
            "record_id",
            "label",
            "bench_band",
            "call",
            "penalty_band",
            "min_dtm",
            "n_sites",
            "off_register",
            "unpriced",
        ]
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {args.tsv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
