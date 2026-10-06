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
read from the publisher's own deposited text - but NOT necessarily all of it.
The JSON carries the article as flattened text, and what survives varies by
article: Prepens 2007 and Deckers 2009 came through with their primer tables,
while other papers lost a table, or lost sequences printed inline (the avipox
paper's reverse primer reads `primer 1R ()`). A file written here can therefore
look complete and still lack the primers; `verify_oligos_against_paper.py`
reports how many oligo-like runs it found (`paper_oligos`) so that shows.

What it writes
--------------
One UTF-8 text file per article, named for the DOI with slashes written as
underscores - `10.3390_v13081632.txt` - which is exactly the convention
`verify_oligos_against_paper.py --pdf-dir papers` matches on. Title, abstract
and body are concatenated, because a paper sometimes prints a primer in its
abstract and nowhere else.

The convention is one-way. The verifier recovers the DOI by turning every `_`
back into `/` and requiring its own DOI pattern to match the result, so a DOI with
an underscore, or with a character outside that pattern (the old Wiley SICI DOIs
contain `<` and `>`), cannot round-trip and would never be matched to its registry
entry. None of the registry's DOIs does (tests/test_import_pmc.py fails if one is
added), and this script says so instead of writing a file nothing would find.

An article whose `full_text` is empty is REPORTED AND SKIPPED, never written as
an empty or abstract-only file. That distinction matters: an abstract-only file
would be indexed as if the paper were in hand, and every sequence checked
against it would come back `absent` - indistinguishable from "this sequence is
not in this paper", which is the finding the whole verification exists to
surface. A missing file reads honestly as "no full text".

Empty `full_text` is common and not a bug. In the 2026-10-05 import 23 of the 44
articles that had a PMC id came back as an abstract and no body: 21 from the
American Society for Microbiology (J Clin Microbiol, J Virol, Appl Environ
Microbiol), one from PNAS and one from SAGE, while mBio - also ASM, but born open
access - came back whole. The deposit policy of the journal decides it, not the
publisher and not whether the paper is open access; the full list is
docs/2026-10-05-pmc-abstract-only.tsv.
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


def articles_in(path: Path) -> list[dict] | None:
    """Every article record in one JSON dump; None if the file is unusable.

    None, not [], so a corrupt file is not mistaken for a dump that simply held
    no articles: `main` has to be able to say it could not read an input, and
    exit non-zero for it.
    """
    try:
        blob = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"  cannot read {path.name}: {type(e).__name__}", file=sys.stderr)
        return None
    if isinstance(blob, dict):
        arts = blob.get("articles")
        if isinstance(arts, list):
            return [a for a in arts if isinstance(a, dict)]
        # A single bare article object.
        if looks_like_article(blob):
            return [blob]
    elif isinstance(blob, list):
        # A bare list of articles. A list of something else - a tool-result wrapper
        # such as [{"type": "text", "text": "..."}] - is not one.
        arts = [a for a in blob if isinstance(a, dict)]
        if not blob or any(looks_like_article(a) for a in arts):
            return [a for a in arts if looks_like_article(a)]
    # Valid JSON that is not an article dump: an error object, a string, null, a wrapped
    # tool result. Reporting "0 papers written" and exiting 0 for it read exactly like a
    # clean empty run, and a driving script could not tell the two apart.
    print(f"  {path.name} is valid JSON but not a PubMed Central article dump", file=sys.stderr)
    return None


def looks_like_article(obj: dict) -> bool:
    """Does this object carry any of the fields an article record has?"""
    return any(k in obj for k in ("identifiers", "full_text", "doi", "title", "abstract"))


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


def round_trips(doi: str) -> bool:
    """Would `verify_oligos_against_paper` recover this DOI from the file's name?

    It turns every `_` back into `/` and requires its own DOI pattern to match the
    whole result. An underscore in the DOI breaks the first step; a character outside
    the pattern (`<` and `>` in the old Wiley SICI DOIs) breaks the second.
    """
    stem = doi_filename(doi)[: -len(".txt")].replace("_", "/")
    return stem == doi.lower() and _vo().DOI_IN_TEXT.fullmatch(stem) is not None


def _vo():
    """The verifier module, loaded once, so the importer cannot drift from its pattern."""
    global _VO
    if _VO is None:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "_vo", ROOT / "scripts" / "verify_oligos_against_paper.py"
        )
        _VO = importlib.util.module_from_spec(spec)
        sys.modules.setdefault("_vo", _VO)
        spec.loader.exec_module(_VO)
    return _VO


_VO = None


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

    wrote, skipped_empty, skipped_exists, no_doi, unreadable, bad_name = [], [], [], [], [], []
    for path in args.json:
        articles = articles_in(path)
        if articles is None:
            unreadable.append(path.name)
            continue
        for a in articles:
            doi = doi_of(a)
            pmcid = (a.get("identifiers") or {}).get("pmcid") or "?"
            if not doi:
                no_doi.append(pmcid)
                continue
            if not round_trips(doi):
                # Cannot round-trip through the filename convention: the verifier
                # turns every `_` back into `/` and then requires the whole thing to
                # match its DOI pattern, so the file would never be matched by name.
                bad_name.append(doi)
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
    if bad_name:
        print(
            f"\n  {len(bad_name)} DOIs cannot round-trip through the filename convention (an underscore, "
            f"or a character the verifier's DOI pattern does not accept), so nothing was written for: "
            f"{', '.join(bad_name)}",
            file=sys.stderr,
        )
    if unreadable:
        print(
            f"\n  {len(unreadable)} input file(s) could not be read: {', '.join(unreadable)}", file=sys.stderr
        )
    print(f"\n{len(wrote)} papers {'would be ' if args.dry_run else ''}written to {args.out_dir}")
    # Non-zero when an input could not be read, or a DOI could not be named: both
    # mean the papers/ folder is missing something the caller asked for, which a
    # clean exit status would have hidden.
    return 1 if (unreadable or bad_name) else 0


if __name__ == "__main__":
    raise SystemExit(main())
