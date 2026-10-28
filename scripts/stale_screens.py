#!/usr/bin/env python3
"""Which cached screens are stale, and which entry made them so. Reads only; never writes.

    python scripts/stale_screens.py
    python scripts/stale_screens.py --verbose     # one line per stale screen

WHY THIS EXISTS. A screen is reused when its signature still matches, and that
signature is computed in the Snakefile -- so the only way to ask "what will the next run
rescreen, and why" was to start a run and read what Snakemake printed. That is a bad way
to find out: on 2026-10-28 a re-render was read as a full 357-archive rescreen because
the post-checkpoint DAG counts every screen job in its denominator, and the four jobs
that actually had stale signatures were indistinguishable from 352 that did not. A
registry edit costing one group's rescreen and one costing the project's are very
different facts about the day's work, and neither should need a kill signal to establish.

WHAT MAKES A SCREEN STALE, which is the whole of the signature:

  * the SCREENING CODE -- screen.py and its import closure, from
    `assaywatch.triggers.source_names("screen")`;
  * the SCORING CONFIG -- config.yaml's `scoring`, `amplicon`, `degeneracy` and
    `thermo_conditions` blocks;
  * the YAML OF THE GROUP'S OWN ASSAYS, and no others.

The third is why a note edit is cheap: it rescreens the groups that hold that entry, not
the registry. The first two are why a scoring change is not. This script says which of
the three moved, because the remedy differs: a code or config change means the whole
project is stale and that is correct, while a registry change should name a handful of
groups and anything larger is a bug in the signature.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

import yaml  # noqa: E402

from assaywatch.retrieve import targets_from_registry  # noqa: E402
from assaywatch.signature import screen_key, stored_signature  # noqa: E402
from assaywatch.triggers import source_names  # noqa: E402

#: The config blocks the Snakefile hashes into the screen signature. Kept in step with
#: `_SCREEN_CFG` there; the test pins that the two agree.
SCREEN_CFG_KEYS = ("scoring", "amplicon", "degeneracy", "thermo_conditions")


def code_hash(cfg: dict, registry: Path, package: Path) -> str:
    """The Snakefile's `_code_hash`: the screening closure plus the scoring config."""
    names = source_names("screen")
    blob = b"".join((package / f).read_bytes() for f in names)
    screen_cfg = {k: cfg.get(k) for k in SCREEN_CFG_KEYS}
    return hashlib.sha1(blob + json.dumps(screen_cfg, sort_keys=True, default=str).encode()).hexdigest()


def group_signature(base: str, assays: list[str], registry: Path) -> str:
    """The Snakefile's `screen_signature`, for one group.

    Hashes each entry's SCREEN-RELEVANT fields (`signature.screen_key`), which is what
    the Snakefile hashes since 2026-10-28 -- so a curator's note no longer makes a
    screen stale, and this script agrees with the pipeline about which ones are.
    """
    h = hashlib.sha1(base.encode())
    for aid in sorted(assays):
        h.update(screen_key(yaml.safe_load((registry / f"{aid}.yaml").read_text())))
    return h.hexdigest()[:16]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=REPO / "registry")
    ap.add_argument("--screened", type=Path, default=REPO / "results" / "screened")
    ap.add_argument("--config", type=Path, default=REPO / "config.yaml")
    ap.add_argument("--verbose", action="store_true", help="one line per stale screen")
    args = ap.parse_args(argv)

    cfg = yaml.safe_load(args.config.read_text()) or {}
    base = code_hash(cfg, args.registry, REPO / "assaywatch")
    groups = targets_from_registry([args.registry], cfg)

    fresh = stale = unsigned = orphan = 0
    by_group: Counter[str] = Counter()
    for (taxid, group), info in sorted(groups.items()):
        want = group_signature(base, info["assays"], args.registry)
        d = args.screened / str(taxid) / group
        for calls in sorted(d.glob("*.tsv")) if d.is_dir() else []:
            got = stored_signature(calls)
            if got is None:
                unsigned += 1
                if args.verbose:
                    print(f"UNSIGNED  {calls.relative_to(args.screened)}")
            elif got == want:
                fresh += 1
            else:
                stale += 1
                by_group[f"{taxid}/{group}"] += 1
                if args.verbose:
                    print(f"STALE     {calls.relative_to(args.screened)}  {got} -> {want}")
    # A screen for a group the registry no longer asks for is not stale; it is
    # unreachable, and `scripts/orphan_archives.py` is where that question lives.
    want_dirs = {args.screened / str(t) / g for t, g in groups}
    for d in sorted(p for p in args.screened.glob("*/*") if p.is_dir()):
        if d not in want_dirs:
            orphan += len(list(d.glob("*.tsv")))

    print(f"{fresh} fresh, {stale} stale, {unsigned} unsigned, {orphan} outside any current group")
    if by_group:
        print("\nstale by group, which names the entries that caused it:")
        for key, n in by_group.most_common(20):
            taxid, group = key.split("/", 1)
            assays = sorted(groups[(int(taxid), group)]["assays"])
            print(
                f"  {key:28s} {n:3d} archive(s)  {', '.join(assays[:4])}{' ...' if len(assays) > 4 else ''}"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
