#!/usr/bin/env python3
"""Fail if any registry citation disagrees with Crossref. Nothing here may be written from memory.

    python scripts/check_citations.py              # uses the cached Crossref metadata
    python scripts/check_citations.py --refresh    # re-fetch every DOI first

Why this exists
---------------
On 2026-10-05 a reference was written into three new entries from memory and was
simply wrong: the paper behind doi:10.3390/v13071358 was recorded as Nobach et
al. when Crossref gives Sigrist, Geers, Albini, Rubbenstroth & Wolfrum. It was
caught only because the DOI happened to be checked afterwards. That is luck, not
process, and luck does not scale to 164 entries.

A fabricated citation is worse than a missing one. A missing citation announces
itself; a plausible wrong one is indistinguishable from a right one until
somebody tries to read the paper, and by then it has been copied into a report.
The same applies to sequences, which is what
`scripts/verify_oligos_against_paper.py` is for - this script is its counterpart
for the bibliographic half.

What it checks
--------------
For every entry with a DOI that resolves and a reference string:

- the reference names Crossref's first author, compared with accents folded and
  hyphenation normalised, so Vazquez-Moron and Vázquez-Morón agree;
- the reference or `design_year` is consistent with Crossref's year, allowing a
  one-year gap, because a paper issued online in December and in an issue the
  following January legitimately carries two years.

It deliberately does NOT try to match the whole reference string. Journal
abbreviations and author-list conventions vary too much for that to mean
anything, and a check that cries wolf gets switched off. First author and year
are the two fields that are cheap to verify and catastrophic to invent.

Exit code 1 on any mismatch, so this runs as a pre-commit hook and in CI.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import yaml  # noqa: E402


def fold(s: str) -> str:
    """Lowercase, strip accents, and normalise the several dash characters to '-'.

    Crossref returns 'Vázquez-Morón' and 'Sánchez‐Seco' - the latter with a
    non-breaking hyphen - where a reference typed on an English keyboard has
    'Vazquez-Moron'. Those are the same name and must not be reported as a
    mismatch, or the check becomes noise and gets ignored.
    """
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[‐-―−]", "-", s)
    return s.lower()


def surname_tokens(family: str) -> list[str]:
    """The parts of a surname worth looking for, e.g. 'van Kuppeveld' -> both words."""
    return [t for t in re.split(r"[-\s']+", fold(family)) if len(t) >= 3]


def check(entry: dict, meta: dict) -> list[str]:
    """Problems with one entry's citation against its Crossref record."""
    c = entry.get("citation") or {}
    ref = (c.get("reference") or "") or (c.get("as_written") or "")
    problems = []

    family = meta.get("first_author") or ""
    if family and ref.strip():
        toks = surname_tokens(family)
        # A compound surname only needs one distinctive part present.
        if toks and not any(t in fold(ref) for t in toks):
            problems.append(f"reference does not name Crossref's first author {family!r}: {ref[:110]!r}")
    elif family and not ref.strip():
        problems.append(f"no reference text, though Crossref knows the paper ({family})")

    year = meta.get("year")
    if year:
        years = {int(y) for y in re.findall(r"\b((?:19|20)\d{2})\b", ref)}
        dy = c.get("design_year")
        candidates = years | ({dy} if dy else set())
        # Online-first publication legitimately straddles two years.
        if candidates and not any(abs(y - year) <= 1 for y in candidates):
            problems.append(
                f"no year within 1 of Crossref's {year}; reference/design_year give {sorted(candidates)}"
            )
    return problems


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--cache", type=Path, default=ROOT / "docs" / "papers-index.cache.json")
    ap.add_argument("--refresh", action="store_true", help="rebuild the Crossref cache first")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if args.refresh or not args.cache.exists():
        import subprocess

        # check=True: a failed rebuild must not fall through to judging the
        # registry against the stale cache, which reports new DOIs as unresolvable.
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "papers_index.py"),
                *(["--refresh"] if args.refresh else []),
                "--out",
                str(ROOT / "docs" / "papers-index.md"),
                "--cache",
                str(args.cache),
            ],
            check=True,
        )
    if not args.cache.exists():
        print("no Crossref cache; run scripts/papers_index.py first", file=sys.stderr)
        return 1
    cache = json.loads(args.cache.read_text())

    failures: list[str] = []
    checked = no_doi = unresolved = 0
    for f in sorted(args.registry.glob("*.yaml")):
        d = yaml.safe_load(f.read_text())
        doi = ((d.get("citation") or {}).get("doi") or "").lower()
        if not doi:
            no_doi += 1
            continue
        meta = cache.get(doi)
        if meta is None:
            unresolved += 1
            failures.append(f"{d['id']}: DOI {doi} does not resolve on Crossref")
            continue
        checked += 1
        for p in check(d, meta):
            failures.append(f"{d['id']}: {p}")

    if not args.quiet:
        for line in failures:
            print("FAIL", line)
        print(
            f"{checked} citations checked against Crossref, {len(failures)} problems "
            f"({no_doi} entries have no DOI and cannot be checked this way)"
        )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
