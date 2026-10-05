#!/usr/bin/env python3
"""Turn PubMed Central full-text JSON into the per-DOI text files `papers/` expects.

    python scripts/import_pmc_fulltext.py --json dump1.json dump2.json
    python scripts/import_pmc_fulltext.py --json dump.json --out-dir papers --dry-run

Why this exists
---------------
`papers/` is gitignored, because the PDFs in it are copyrighted. That is the
right call for the repository and an awkward one for any machine that did not
download them: a fresh clone starts with no papers at all, and almost every
remaining verification task reads one.

`scripts/find_open_access.py` is the usual way back - Unpaywall, then OpenAlex,
then a PDF over HTTPS. It needs direct outbound network access to those hosts,
which a locked-down environment may not grant. Where it does not, PubMed Central
is still reachable through an MCP tool that returns the open-access full text as
JSON, and that JSON is what this script consumes. The route differs; the source
does not. PMC's open-access subset is the same corpus Europe PMC's
`fullTextXML` endpoint serves, so a sequence read from a file written here is
read from the publisher's own deposited text.

What it writes
--------------
One UTF-8 text file per article, named for the DOI with slashes written as
underscores - `10.3390_v13081632.txt` - which is exactly the convention
`verify_oligos_against_paper.py --pdf-dir papers` matches on. Title, abstract
and body are concatenated, because a paper sometimes prints a primer in its
abstract and nowhere else.

An article whose `full_text` is empty is REPORTED AND SKIPPED, never written as
an empty or abstract-only file. That distinction matters: an abstract-only file
would be indexed as if the paper were in hand, and every sequence checked
against it would come back `absent` - indistinguishable from "this sequence is
not in this paper", which is the finding the whole verification exists to
surface. A missing file reads honestly as "no full text".

Empty `full_text` is common and not a bug. In the 2026-10-05 import, every
American Society for Microbiology article (J Clin Microbiol, J Virol, Appl
Environ Microbiol) and the one SAGE article came back with an abstract and no
body, while mBio - also ASM, but born open access - came back whole. Publisher
deposit policy, not availability, decides this.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")


def doi_filename(doi: str) -> str:
    """`10.3390/v13081632` -> `10.3390_v13081632.txt`, lowercased.

    Lowercasing matters. PMC echoes a DOI in the publisher's own casing, so the
    same paper arrives as `10.1128/JCM.00192-08` here and is stored in the
    registry as `10.1128/jcm.00192-08`. The verifier lowercases the DOI it reads
    off a filename before comparing, so a mixed-case file would simply never be
    matched to its entry.
    """
    return doi.lower().replace("/", "_") + ".txt"


def articles_in(path: Path) -> list[dict]:
    """Every article record in one JSON dump, or [] if the file is unusable."""
    try:
        blob = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"  cannot read {path.name}: {type(e).__name__}", file=sys.stderr)
        return []
    if isinstance(blob, dict):
        arts = blob.get("articles")
        if isinstance(arts, list):
            return [a for a in arts if isinstance(a, dict)]
        # A single bare article object.
        return [blob] if "identifiers" in blob or "full_text" in blob else []
    if isinstance(blob, list):
        return [a for a in blob if isinstance(a, dict)]
    return []


def document(article: dict) -> str:
    """Title, abstract and body as one block of text.

    The abstract is included because a short methods paper sometimes prints the
    primer pair in it and in no table - and because when the body is missing the
    abstract is at least a record of what the paper claims.
    """
    parts = [
        (article.get("title") or "").strip(),
        (article.get("abstract") or "").strip(),
        (article.get("full_text") or "").strip(),
    ]
    return "\n\n".join(p for p in parts if p) + "\n"


def doi_of(article: dict) -> str:
    """The article's DOI, from either place PMC puts it."""
    ids = article.get("identifiers") or {}
    doi = (ids.get("doi") or article.get("doi") or "").strip()
    return doi if DOI_RE.match(doi) else ""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", type=Path, nargs="+", required=True, help="PMC full-text JSON dumps")
    ap.add_argument("--out-dir", type=Path, default=ROOT / "papers")
    ap.add_argument("--dry-run", action="store_true", help="report without writing")
    ap.add_argument("--overwrite", action="store_true", help="replace files that already exist")
    args = ap.parse_args(argv)

    wrote, skipped_empty, skipped_exists, no_doi = [], [], [], []
    for path in args.json:
        for a in articles_in(path):
            doi = doi_of(a)
            pmcid = (a.get("identifiers") or {}).get("pmcid") or "?"
            if not doi:
                no_doi.append(pmcid)
                continue
            if not (a.get("full_text") or "").strip():
                skipped_empty.append((doi, pmcid))
                continue
            dest = args.out_dir / doi_filename(doi)
            if dest.exists() and not args.overwrite:
                skipped_exists.append(doi)
                continue
            text = document(a)
            if not args.dry_run:
                args.out_dir.mkdir(parents=True, exist_ok=True)
                dest.write_text(text, encoding="utf-8")
            wrote.append((doi, len(text), dest.name))

    for doi, n, name in sorted(wrote):
        print(f"  {'would write' if args.dry_run else 'wrote':11s} {name:48s} {n:7d} chars  {doi}")
    if skipped_exists:
        print(f"\n  {len(skipped_exists)} already present (use --overwrite to replace)")
    if skipped_empty:
        print(f"\n  {len(skipped_empty)} articles carry NO full text and were skipped:")
        for doi, pmcid in sorted(skipped_empty):
            print(f"    {pmcid:12s} {doi}")
        print(
            "    These are in PMC as an abstract only - publisher deposit policy.\n"
            "    They still need the PDF; nothing was written, so the verifier will\n"
            "    keep reporting them as no-full-text rather than as absent sequences."
        )
    if no_doi:
        print(f"\n  {len(no_doi)} articles had no usable DOI: {', '.join(no_doi)}", file=sys.stderr)
    print(f"\n{len(wrote)} papers {'would be ' if args.dry_run else ''}written to {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
