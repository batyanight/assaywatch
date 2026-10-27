#!/usr/bin/env python3
"""How much of tier-2 performance is the thresholds having seen tier-2.

    python scripts/holdout.py --calls results/baseline-2026-10-22/calls.tsv.gz

THE PROBLEM THIS MEASURES. `docs/journal/2026-10-23-baseline.md` records that at least
seven `config.yaml` settings were accepted or rejected on their effect on the 49
cases in `docs/validation-cases.tsv`, which collapse to about seven independent
failure events. A matrix reported from those same cases is therefore optimistic
by an unknown amount, and "unknown" is the part this fixes.

WHAT IT DOES. Leave-one-out over a stated selection rule, on the one pair of
settings the project has already swept as a grid
(`docs/journal/2026-10-21-drift-window-calibration.md`): `recent_window_months` x
`min_records_for_drift`. For each case, the rule picks the grid cell that scores
best on the OTHER 48 cases, and that cell is then used to score the held-out
case. The spread between the in-sample best and this estimate is the optimism.

WHY THIS PAIR. Because the selection rule has to be written down to be
cross-validated, and this is where it already is: the ROADMAP says the two must
be set together, the grid is documented, and `min_records_for_drift` 20 -> 15 is
one of the seven tuned decisions. The other six were single judgements with no
sweepable range (`require_working_baseline`, `group_at_rank`, ...), so no
resampling can estimate their optimism; they are listed in the output as
uncosted, which is the honest treatment.

WHAT IT IS NOT. Not a substitute for held-out cases (plan item 4.2). LOO
estimates the optimism of a selection rule applied to THIS sample; it cannot
see a bias shared by every case in it, and
`docs/journal/2026-10-21-drift-window-calibration.md` documents exactly such a bias --
as-of scoring cannot see the cost of warning late, so the grid prefers a long
window for a reason that has nothing to do with being right.

Evidence is loaded once and every grid cell scored in process, so the whole
sweep costs one pass over the calls table.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import importlib.util  # noqa: E402

from assaywatch.interval import wilson_interval  # noqa: E402
from assaywatch.score import load_config  # noqa: E402

_spec = importlib.util.spec_from_file_location("retro", ROOT / "scripts" / "retrospective.py")
retro = importlib.util.module_from_spec(_spec)
sys.modules["retro"] = retro
_spec.loader.exec_module(retro)

#: The sweep, as `docs/journal/2026-10-21-drift-window-calibration.md` ran it.
WINDOWS = (18, 24, 36, 48, 60)
MINIMUMS = (10, 15, 20, 30)

#: Settings tuned on these cases with no sweepable range, so no resampling can
#: price their optimism. Named in the output rather than left implicit.
UNCOSTED = (
    "drift.require_working_baseline",
    "lineage.require_working_baseline",
    "lineage.min_records_per_lineage",
    "lineage.group_at_rank",
    "lineage.unclassified_is_bucket",
    "scoring.mispair_penalty (shipped then reverted)",
)


def objective(verdicts: list[str]) -> int:
    """Lower is better: the disagreement count the documented grid minimised.

    `weaker` is not a disagreement (a pan-family assay detecting most of a genus
    is consistent with a paper that used it on the isolates it had), and
    `undecided` is not either -- the tool declining to judge is a different
    thing from judging wrongly, and counting it here would make the rule prefer
    whatever decides most cases.
    """
    return sum(1 for v in verdicts if v == "DISAGREES")


def score_grid(
    evidence, cfg: dict, cases: list[dict], resolved, scope_map
) -> dict[tuple[int, int], list[str]]:
    """verdict per case, per grid cell."""
    out: dict[tuple[int, int], list[str]] = {}
    for w in WINDOWS:
        for m in MINIMUMS:
            trial = {
                **cfg,
                "drift": {**cfg.get("drift", {}), "recent_window_months": w, "min_records_for_drift": m},
            }
            verdicts = []
            for i, c in enumerate(cases):
                rid, _ = resolved[i]
                if rid is None:
                    verdicts.append("removed")
                    continue
                drifts, _ = retro.status_from_evidence(
                    evidence, trial, date.fromisoformat(c["as_of"]), {rid}, scope_map=scope_map
                )
                a = drifts.get(rid)
                _, v = retro.classify(a.status if a else "no data", c["expect"], c.get("mechanism") or None)
                verdicts.append(v)
            out[(w, m)] = verdicts
            print(f"  ({w:>2}, {m:>2}) done: {objective(verdicts)} disagreements", file=sys.stderr)
    return out


def best_cell(grid: dict[tuple[int, int], list[str]], skip: int | None = None) -> tuple[int, int]:
    """The grid cell with fewest disagreements, ties to the smallest (window, min).

    Ties are broken on the cell, never toward the shipped value: tie-breaking
    toward what ships would import the very preference this is trying to price.
    """

    def score(cell):
        vs = grid[cell]
        if skip is not None:
            vs = [v for j, v in enumerate(vs) if j != skip]
        return (objective(vs), cell)

    return min(grid, key=score)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--calls", type=Path, default=None)
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--cases", type=Path, default=ROOT / "docs" / "validation-cases.tsv")
    ap.add_argument("--renames", type=Path, default=ROOT / "docs" / "rename-mapping.tsv")
    args = ap.parse_args(argv)

    # Shared with retrospective.py, which is where the by-date rule and the bug it
    # replaced are documented: `sorted(...)[-1]` picked `baseline-2026-10-22` over
    # `2026-10-25` because `b` > `2`.
    calls = args.calls or retro.newest_run(ROOT / "results")
    if args.calls is None:
        print(f"scoring {calls.parent.name}/{calls.name}", file=sys.stderr)
    cfg = load_config(args.config)
    scope_map = retro._build_scope_map(args.registry) if args.registry.is_dir() else None
    query_taxids = retro._query_taxids(args.registry) if args.registry.is_dir() else None

    with args.cases.open() as fh:
        cases = list(csv.DictReader((ln for ln in fh if not ln.startswith("#")), delimiter="\t"))
    print(f"{len(cases)} cases from {args.cases.name}", file=sys.stderr)

    # `registry` is passed for the same reason retrospective.py passes it: without
    # it a cluster-based sublineage resolver defers here and not there, so the two
    # scripts would disagree about a lineage. Inert while `lineage.sublineage` is
    # empty, which is exactly when a divergence like this goes unnoticed.
    registry = args.registry if args.registry.is_dir() else None
    evidence = retro.load_evidence(calls, args.retrieved, cfg, query_taxids, registry)
    present = set(evidence.by_assay)
    if args.renames.exists():
        renamed, removed = retro.rename_map(args.renames)
        aliases = retro.id_aliases(renamed)
    else:
        aliases, removed = {}, set()
    resolved: dict[int, tuple[str | None, str]] = {}
    for i, c in enumerate(cases):
        resolved[i] = retro.resolve_assay_id(c["assay_id"], present, aliases, removed)

    print(f"scoring {len(WINDOWS) * len(MINIMUMS)} grid cells", file=sys.stderr)
    grid = score_grid(evidence, cfg, cases, resolved, scope_map)

    shipped = (
        int(cfg["drift"].get("recent_window_months", 24)),
        int(cfg["drift"].get("min_records_for_drift", 20)),
    )
    ins = best_cell(grid)
    scorable = [i for i in range(len(cases)) if grid[ins][i] != "removed"]

    # LOO: pick the cell on the other 48, score the one left out.
    loo, picks = [], Counter()
    for i in scorable:
        cell = best_cell(grid, skip=i)
        picks[cell] += 1
        loo.append(grid[cell][i])

    n = len(scorable)

    def line(label, k):
        lo, hi = wilson_interval(k, n)
        return f"  {label:34s} {k:>2}/{n} = {k / n:4.0%} (95% CI {lo:.0%}-{hi:.0%})"

    print("\n" + "=" * 78)
    print(f"grid: recent_window_months {WINDOWS} x min_records_for_drift {MINIMUMS}")
    print(f"objective: fewest DISAGREES over {n} scorable cases\n")
    print(f"shipped cell {shipped}: {objective(grid[shipped])} disagreements")
    print(f"in-sample best {ins}: {objective(grid[ins])} disagreements")
    print(line("in-sample agreement", sum(1 for v in grid[ins] if v == "agrees")))
    print(line("LEAVE-ONE-OUT agreement", sum(1 for v in loo if v == "agrees")))
    print(line("in-sample disagreement", objective(grid[ins])))
    print(line("LEAVE-ONE-OUT disagreement", sum(1 for v in loo if v == "DISAGREES")))
    opt = objective(grid[ins]) - sum(1 for v in loo if v == "DISAGREES")
    print(f"\n  optimism of the in-sample figure: {opt:+d} disagreements")
    print(f"  cells the rule picked across folds: {dict(picks)}")
    print("\n  uncosted settings, also tuned on these cases, no sweepable range:")
    for s in UNCOSTED:
        print(f"    - {s}")
    print(
        "\n  LOO prices the optimism of a selection rule on THIS sample. It cannot see a\n"
        "  bias every case shares: docs/journal/2026-10-21-drift-window-calibration.md documents\n"
        "  one (as-of scoring cannot see the cost of warning late). Held-out cases, not\n"
        "  resampling, are what answers that."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
