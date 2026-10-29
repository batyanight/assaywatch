#!/usr/bin/env python
"""Fetch open-access full text from Europe PMC for papers `papers/` does not hold.

    python scripts/fetch_europepmc_fulltext.py --registry registry --pdf-dir papers
    python scripts/fetch_europepmc_fulltext.py --doi 10.4269/ajtmh.2011.11-0248 -v

Why this exists alongside the other two
---------------------------------------
`scripts/find_open_access.py` looks for a PDF, which is what you want when there
is one; it found legal copies for 17 of 46 missing papers and could download only
3, because publishers that mark a paper "bronze" open access still answer a
scripted request with a 401 or an HTML paywall page.

`scripts/import_pmc_fulltext.py` reads PubMed Central full text that an MCP tool
has already returned as JSON, which is the route a locked-down cloud session has.

This is the third route and the one a machine with ordinary outbound network
should try first: Europe PMC's REST service, which serves the same open-access
corpus as machine-readable XML, with no key and no negotiation.

**It carries tables.** The 2026-10-05 cloud session concluded that "PMC omits
table content - the body text arrives, `table-wrap` does not", and that is true
of the JSON the MCP tool returns. It is not true of Europe PMC's `fullTextXML`,
which includes `<table-wrap>` in full. That matters more than anything else here,
because the primer table is the thing being looked for: reading Deckers 2009's
Table 1 out of this endpoint is what identified the real source of four CMV gB
primers that had been misattributed for two days.

So a paper that this script recovers may well yield its primers where the same
paper recovered through the JSON route yielded nothing. Where both are available,
prefer this one.

What it writes
--------------
One UTF-8 text file per article, named for the DOI with slashes as underscores -
`10.4269_ajtmh.2011.11-0248.txt` - the convention
`verify_oligos_against_paper.py --pdf-dir papers` already matches on. Title,
abstract, body and every table are concatenated. Table cells are joined with
` | ` and rows with newlines, because a primer and its name sit in adjacent cells
and gluing them together is what makes an extracted sequence unreadable.

Nothing is overwritten: a PDF in hand is better evidence than a text rendering,
and a file already present is left alone unless --overwrite says otherwise.

This writes into a gitignored directory and fetches only open-access content.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from assaywatch.credentials import contact_email
from assaywatch.papers import doi_stem

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from assaywatch import papers, registry  # noqa: E402

_GET = papers.http(timeout=120)


def held(pdf_dir: Path, doi: str) -> str | None:
    """Any file in pdf_dir already standing for this DOI."""
    p = papers.paper_for_doi(doi, pdf_dir)
    return p.name if p else None


def registry_dois(registry_dir: Path) -> dict[str, list[str]]:
    """{doi: [assay ids]} over every entry that cites one."""
    out: dict[str, list[str]] = {}
    for a in registry.load(registry_dir).values():
        if a.citation.doi:
            out.setdefault(a.citation.doi.strip(), []).append(a.id)
    return out


def pmcid_for(doi: str) -> str | None:
    return papers.pmcid_for(doi, _GET, email=contact_email() or "")


# `flatten` is papers.flatten_xml; the name stays for check_candidate_identity.
flatten = papers.flatten_xml


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--pdf-dir", type=Path, default=ROOT / "papers")
    ap.add_argument("--doi", action="append", default=[], help="fetch only these DOIs")
    ap.add_argument("--overwrite", action="store_true", help="replace a text file already present")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    args.pdf_dir.mkdir(parents=True, exist_ok=True)
    wanted = {d: ["(--doi)"] for d in args.doi} if args.doi else registry_dois(args.registry)

    missing = {}
    for doi, assays in sorted(wanted.items()):
        have = held(args.pdf_dir, doi)
        if have and not (args.overwrite and have.lower().endswith(".txt")):
            if args.verbose:
                print(f"  held   {doi}  ({have})")
            continue
        missing[doi] = assays

    print(f"{len(missing)} of {len(wanted)} cited papers have no local copy")
    got = no_pmc = empty = 0
    for doi, assays in sorted(missing.items()):
        pmcid = pmcid_for(doi)
        time.sleep(0.3)
        if not pmcid:
            no_pmc += 1
            if args.verbose:
                print(f"  no open PMC copy   {doi}")
            continue
        text = papers.europepmc_fulltext(pmcid, _GET, email=contact_email() or "")
        time.sleep(0.3)
        if text is None:
            print(f"  fetch failed       {doi}  {pmcid}")
            continue
        # An abstract-only deposit comes back a few thousand characters long and
        # is not worth writing: it cannot confirm or deny a primer, and a file
        # present stops find_open_access.py looking for the real thing.
        if len(text) < papers.FULLTEXT_MIN_CHARS:
            empty += 1
            if args.verbose:
                print(f"  abstract only      {doi}  {pmcid}  ({len(text)} chars)")
            continue
        out = args.pdf_dir / f"{doi_stem(doi)}.txt"
        if args.dry_run:
            print(f"  would write        {out.name}  ({len(text)} chars, {pmcid})")
        else:
            out.write_text(text, encoding="utf-8")
            print(f"  wrote              {out.name}  ({len(text)} chars, {pmcid})  {', '.join(assays)[:60]}")
        got += 1

    print(f"\n  {got} recovered, {no_pmc} with no open PMC copy, {empty} abstract-only")
    if empty:
        print("  (abstract-only deposits are not written: they cannot confirm a sequence)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
