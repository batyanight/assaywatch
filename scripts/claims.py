#!/usr/bin/env python3
"""Every registry count quoted in prose, checked against the registry.

    python scripts/claims.py            # report
    python scripts/claims.py --check    # exit 1 if any quoted count is stale (CI)

WHY. README.md:63-65 explains that counts are printed by the validator "because
the ones written here by hand drifted as the registry grew" -- and then writes
"214 files on 2026-10-14" into prose on the same line. `validate.py` repeats the
lesson, and `score.py` repeats it again, both while quoting 214. The mechanism
was built; the prose was never cut over. On 2026-10-23 the registry held 208
entries and nine different wrong numbers were in circulation across README,
ROADMAP, CONTRIBUTING, config.yaml and score.py.

WHAT IT CHECKS, AND WHAT IT CANNOT. It knows a small set of quantities it can
compute from `registry/` -- the file count, the per-status counts, the per-chemistry
counts, how many carry a probe -- and it finds integers in prose that are
*presented as* one of those. Matching is by the sentence around the number, so it
reports a stale count and a candidate correction rather than editing: a number
can be stale, correct-as-of-a-dated-run, or not a registry count at all, and
only a reader can tell which. A DATED claim ("214 files on 2026-10-14") is
history and legitimate; this flags it only when the date is absent.

It deliberately does not police figures from a RUN -- "59,141 rows moved",
"7.8 GB across 127 groups" -- which cannot be recomputed without the archives and
whose honest fix is a run date beside them, not a check.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.validate import iter_files, load_assay  # noqa: E402

#: Files whose prose is checked. Dated session records under docs/ are history
#: and are left alone; these are the documents a reader is pointed at.
PROSE = ("README.md", "ROADMAP.md", "CONTRIBUTING.md", "config.yaml", "assaywatch/score.py")

#: A quoted count is stale if the sentence around it matches one of these and the
#: number is not the live value. The pattern is deliberately narrow.
PATTERNS = [
    ("total", re.compile(r"(\d{3})\s+(?:registry\s+)?(?:files|entries|assays)\b", re.I)),
    ("total", re.compile(r"\b(?:all|of)\s+(\d{3})\s+assays\b", re.I)),
    ("draft", re.compile(r"(\d{3})\s+(?:of [\d,]+ )?(?:entries|assays)? ?are\s+draft", re.I)),
    ("draft", re.compile(r"(\d{3})\s+draft\b", re.I)),
    ("conventional", re.compile(r"(\d{3})\s+conventional\b", re.I)),
    ("with_probe", re.compile(r"(\d{2,3})\s+probe assays\b", re.I)),
    ("with_probe", re.compile(r"(\d{2,3})\s+carry a probe\b", re.I)),
]

#: Any ISO date on the line marks the claim as history. Deliberately loose: an
#: earlier version wanted "on <date>" or "as of <date>" and flagged two claims
#: that carry a bare "(2026-10-14)", which is a date stamp by any reading. The
#: project's own rule is that "a check that cries wolf gets switched off"
#: (docs/journal/2026-10-05-hallucination-audit.md), and the cost of being loose is that
#: a stale count sharing a line with an unrelated date is missed.
DATED = re.compile(r"\d{4}-\d{2}-\d{2}")


def live_counts() -> dict[str, int]:
    assays = [load_assay(p) for p in iter_files(ROOT / "registry")]
    status = Counter(a.status.value for a in assays)
    chem = Counter(a.chemistry.value for a in assays)
    return {
        "total": len(assays),
        "draft": status["draft"],
        "active": status["active"],
        "deprecated": status["deprecated"],
        "conventional": chem["conventional"],
        "with_probe": sum(1 for a in assays if a.oligos.probe is not None),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if any undated quoted count is stale")
    args = ap.parse_args(argv)

    live = live_counts()
    print("live registry counts: " + ", ".join(f"{k}={v}" for k, v in live.items()))

    stale, dated = [], []
    for name in PROSE:
        path = ROOT / name
        if not path.exists():
            continue
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            for key, pattern in PATTERNS:
                for m in pattern.finditer(line):
                    quoted = int(m.group(1))
                    if quoted == live[key]:
                        continue
                    where = f"{name}:{lineno}"
                    entry = (where, key, quoted, live[key], line.strip()[:96])
                    (dated if DATED.search(line) else stale).append(entry)

    if dated:
        print(f"\n{len(dated)} dated claim(s), left alone (history, not a current count):")
        for where, key, quoted, now, text in dated:
            print(f"  {where:28s} {key}={quoted} (now {now})  {text}")

    if not stale:
        print("\nno undated registry count is stale")
        return 0

    print(f"\n{len(stale)} STALE undated count(s):")
    for where, key, quoted, now, text in stale:
        print(f"  {where:28s} {key}: says {quoted}, registry has {now}")
        print(f"      {text}")
    print(
        "\nFix by giving the number a run date, pointing at `assaywatch validate registry`, or correcting it."
    )
    return 1 if args.check else 0


if __name__ == "__main__":
    raise SystemExit(main())
