#!/usr/bin/env python3
"""Which drafts could be `active`, and what each would still be asserting.

    python scripts/promote.py                      # the whole picture
    python scripts/promote.py --tier clean         # only entries with no oligo doubt
    python scripts/promote.py --apply --tier clean # set status: active on those

PROPOSES BY DEFAULT. `--apply` is the only path that writes, and `CONTRIBUTING.md`
and `CLAUDE.md` both say only a maintainer sets `active`, so this is a worklist
rather than a decision.

THE PROBLEM IT MAKES VISIBLE. 205 of 208 entries are `draft` and 1 is `active`,
and every report header tells the reader a draft's numbers are provisional --
i.e. the report disclaims 99.5% of itself. But 173 of those drafts already carry
a Crossref-verified DOI, a taxid and a design year with no open review question:
everything `Assay.missing_for_active` asks. They are drafts because nobody has
run a promotion pass, which is a fact about the maintainer's queue, not about the
entry.

WHAT `active` DOES AND DOES NOT ASSERT, which is the decision this script exists
to inform. The gate is about METADATA: a citation that resolves, a taxon to
retrieve, a year to date a baseline from, no unresolved question. It says nothing
about whether the OLIGOS are right -- and the oligos are what every call in a
screen depends on. Of the 173 eligible drafts, 73 carry a flag in
`review.OLIGO_DOUBT` (`orientation_inferred`, `oligos_modified`,
`oligos_from_secondary_source`, `oligos_not_in_cited_paper`, ...), and only 87 of
384 oligos registry-wide are confirmed against their source paper
(docs/2026-10-05-hallucination-audit.md). So:

    --tier clean      173 eligible MINUS the 73 with oligo doubt = 100 entries
    --tier eligible   all 173, i.e. `active` means exactly what the validator checks

Neither is wrong; they mean different things, and the report's wording should
match whichever is chosen. `clean` is the stricter reading and the one this
script defaults to listing first.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.review import OLIGO_DOUBT  # noqa: E402
from assaywatch.schema import Status  # noqa: E402
from assaywatch.validate import iter_files, load_assay  # noqa: E402


def oligo_doubts(assay) -> list[str]:
    """The flags on this entry that cast doubt on its oligos."""
    return sorted(i.flag.value for i in (assay.needs_review or []) if i.flag in OLIGO_DOUBT)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument(
        "--tier",
        choices=("clean", "eligible"),
        default=None,
        help="clean: no oligo doubt. eligible: everything the validator's gate accepts.",
    )
    ap.add_argument("--apply", action="store_true", help="write status: active (needs --tier)")
    args = ap.parse_args(argv)

    assays = {a.id: (a, p) for p in iter_files(args.registry) for a in [load_assay(p)]}
    drafts = {i: (a, p) for i, (a, p) in assays.items() if a.status is Status.draft}
    eligible = {i: (a, p) for i, (a, p) in drafts.items() if not a.missing_for_active}
    clean = {i: (a, p) for i, (a, p) in eligible.items() if not oligo_doubts(a)}

    by_status = Counter(a.status.value for a, _ in assays.values())
    print(f"{len(assays)} entries: " + ", ".join(f"{n} {s}" for s, n in sorted(by_status.items())))
    print(f"{len(eligible)} drafts meet every mechanical `active` requirement")
    print(f"{len(clean)} of those also carry no oligo doubt\n")

    blocked = Counter(m.split(" (")[0] for a, _ in drafts.values() for m in a.missing_for_active)
    if blocked:
        print("what blocks the rest:")
        for what, n in blocked.most_common():
            print(f"  {n:3d}  {what}")
        print()

    if args.tier is None:
        doubt_counts = Counter(f for a, _ in eligible.values() for f in oligo_doubts(a))
        print("oligo doubt among the eligible (an entry can carry more than one):")
        for flag, n in doubt_counts.most_common():
            print(f"  {n:3d}  {flag}")
        print("\nRe-run with --tier clean or --tier eligible to list ids; add --apply to write.")
        return 0

    chosen = clean if args.tier == "clean" else eligible
    print(f"--tier {args.tier}: {len(chosen)} entries")
    for i, (a, _) in sorted(chosen.items()):
        doubts = oligo_doubts(a)
        print(f"  {i[:60]:62s} {'' if not doubts else '(' + ', '.join(doubts) + ')'}")

    if not args.apply:
        print(f"\nProposed only. Add --apply to set status: active on these {len(chosen)}.")
        return 0

    # Minimal edit: rewrite the one `status:` line, so comments, key order and
    # formatting survive. Round-tripping YAML would reformat 100 files.
    changed = 0
    for i, (_, path) in sorted(chosen.items()):
        text = path.read_text()
        if "\nstatus: draft\n" not in text:
            print(f"  SKIPPED {i}: no top-level `status: draft` line to replace", file=sys.stderr)
            continue
        path.write_text(text.replace("\nstatus: draft\n", "\nstatus: active\n", 1))
        changed += 1
    print(f"\nset status: active on {changed} entries. Now run:")
    print("  python -m assaywatch.validate registry && pytest -q")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
