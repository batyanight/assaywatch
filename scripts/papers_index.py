#!/usr/bin/env python3
"""Keep a committed index of every paper this registry depends on.

    python scripts/papers_index.py --out docs/papers-index.md
    python scripts/papers_index.py --out docs/papers-index.md --refresh
    python scripts/papers_index.py --check          # pre-commit: is the committed index current?

The PDFs live in `papers/`, which is gitignored because the files are
copyrighted. That means the one durable record of WHICH papers this project
rests on has to be a text document in the repository, or the knowledge of what
has been read lives only on one laptop.

So this writes a Markdown index: every DOI the registry cites, plus every PDF
held locally, with year, journal, title, first author, and which registry
entries depend on it. Metadata comes from Crossref and is cached in
`docs/papers-index.cache.json`, which IS committed - so the index can be rebuilt
with no network, and so a change in what Crossref returns shows up as a diff
rather than silently.

`--refresh` re-fetches everything instead of using the cache. Worth doing
occasionally: a DOI that stops resolving, or starts resolving to a different
paper, is exactly the failure this project has hit before.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import yaml  # noqa: E402

from assaywatch.papers import PAPER_SUFFIXES, SUPPLEMENT_SUFFIX, doi_stem  # noqa: E402

CROSSREF = "https://api.crossref.org/works/"


def crossref(doi: str) -> dict | None:
    """Title, journal, year and authors for a DOI, or None if it does not resolve."""
    try:
        url = CROSSREF + urllib.parse.quote(doi, safe="")
        with urllib.request.urlopen(url, timeout=45) as r:
            m = json.loads(r.read().decode())["message"]
    except Exception:  # noqa: BLE001 - a dead DOI is data, not a crash
        return None
    # Crossref embeds italics as tags in titles; strip them so the index is plain text.
    title = re.sub(r"<[^>]+>", "", (m.get("title") or [""])[0])
    title = re.sub(r"\s+", " ", title).strip()
    dates = (m.get("issued") or {}).get("date-parts") or [[None]]
    authors = [a.get("family", "") for a in (m.get("author") or []) if a.get("family")]
    return {
        "title": title,
        "journal": (m.get("container-title") or [""])[0],
        "year": dates[0][0],
        "volume": m.get("volume") or "",
        "first_author": authors[0] if authors else "",
        "n_authors": len(authors),
    }


# Sources the registry depends on that no single entry CITES, so
# `registry_citations` cannot see them and a PDF named after one is reported
# unmatched. Each entry here needs a reason, because the alternative - letting
# any unmatched filename invent a DOI - is the bug local_pdfs exists to prevent.
SHARED_SOURCES = {
    # 37 entries' oligos were transcribed from this book's Supplementary Methods
    # and verified against it (scripts/verify_predict_supplement.py, 74/74 exact).
    # Each cites its own design paper, as it should, so nothing cites the book.
    "10.1038/ncomms9147": "PREDICT consensus-PCR protocol book (Anthony et al. 2015)",
}


def registry_citations() -> dict[str, list[str]]:
    """{doi: [assay ids citing it]} over the whole registry."""
    out: dict[str, list[str]] = defaultdict(list)
    for f in sorted((ROOT / "registry").glob("*.yaml")):
        d = yaml.safe_load(f.read_text())
        doi = (d.get("citation") or {}).get("doi")
        if doi:
            out[doi.lower()].append(d["id"])
    return out


def local_pdfs(pdf_dir: Path, known_dois: set[str]) -> tuple[dict[str, str], int]:
    """({doi: filename(s)} for DOIs whose full text is held, count of files matched to none).

    Every extension in `PAPER_SUFFIXES` counts, not just `.pdf`. Until 2026-10-24
    this globbed `*.pdf` alone while `verify_oligos_against_paper` read `.pdf`,
    `.xml` and `.txt`, so the two readers of `papers/` disagreed about what a held
    paper is and the index reported sixteen papers it holds as never obtained -
    four cited entries held as PMC `.txt` and twelve as publisher `.xml`. The
    constant is shared from `assaywatch/papers.py` for exactly the reason
    SUPPLEMENT_SUFFIX is.

    A `<stem>.supp.<ext>` counts for the same DOI as `<stem>.<ext>` and is recorded
    under the DOI with its real filename, so the index says which of the two is
    on disk.

    Forward-mapped from each known DOI, because a filename stem cannot be turned
    back into a DOI (see assaywatch/papers.py). This used to reverse-map every
    stem and treat the result as a DOI, which invented ten DOIs out of the ten
    parenthesised ones in papers/ - `10.1016/0890-8508/92/90002-f` and friends -
    and, since a DOI that does not resolve is cached too, wrote all ten into
    docs/papers-index.cache.json as permanent nulls.

    The unmatched count is returned rather than swallowed: a PDF whose DOI is not
    in the registry or the cache can no longer be discovered by name, and that is
    a real loss of capability, so it has to be visible. Name such a file after a
    DOI the registry cites, or add the entry.
    """
    stems: dict[str, list[str]] = {}
    if pdf_dir.is_dir():
        for suffix in PAPER_SUFFIXES:
            for p in sorted(pdf_dir.glob(f"*{suffix}")):
                stems.setdefault(p.stem.lower(), []).append(p.name)
    out, claimed = {}, set()
    for doi in known_dois:
        # Two stem spellings, kept for files written before 2026-10-24. doi_stem
        # replaces `/`, `(`, `)`, `<` and `>` with `_`, which is what a browser
        # download was saved as; three fetchers (Elsevier, Europe PMC,
        # find_open_access) replaced only the slash, so eleven publisher JATS
        # deposits sat on disk as `10.1016_s0016-5085(98)70589-x.xml` and matched
        # nothing. On 2026-10-24 all three fetchers moved to `doi_stem` and the
        # eleven files were renamed, so nothing writes the slash-only spelling any
        # more; this variant stays only so a `papers/` copied from an older
        # checkout still indexes. `verify_oligos_against_paper` compares the
        # canonical stem alone and now reaches those files too - re-run on
        # 2026-10-24, 479 rows, zero verdict changes, because a JATS deposit also
        # prints its own DOI and was being found by that weaker route.
        # A LIST, not a set: set iteration order varies between runs, which made the
        # `held` column print "pdf, xml" or "xml, pdf" at random and the --check hook
        # flake. Canonical stem first, so a PDF is named before a publisher deposit.
        # The slash-only spelling on purpose: see the paragraph above.
        slash_only = doi.strip().lower().replace("/", "_")
        variants = [doi_stem(doi)] + ([slash_only] if slash_only != doi_stem(doi) else [])
        names = list(
            dict.fromkeys(
                n for stem in variants for n in stems.get(stem, []) + stems.get(stem + SUPPLEMENT_SUFFIX, [])
            )
        )
        if names:
            out[doi.strip().lower()] = ", ".join(names)
            claimed.update(names)
    return out, len({n for names in stems.values() for n in names} - claimed)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "papers-index.md")
    ap.add_argument("--pdf-dir", type=Path, default=ROOT / "papers")
    ap.add_argument("--cache", type=Path, default=ROOT / "docs" / "papers-index.cache.json")
    ap.add_argument("--refresh", action="store_true", help="re-fetch every DOI instead of using the cache")
    ap.add_argument(
        "--check",
        action="store_true",
        help="write nothing; exit 1 if --out is not what this run would write (for the pre-commit hook)",
    )
    args = ap.parse_args(argv)

    # Loaded even under --refresh: other scripts cache DOIs this one never
    # visits (List 2 candidates, the literature scan), and starting from an empty
    # dict silently dropped 102 of them. --refresh re-fetches only what it indexes.
    cache: dict = {}
    if args.cache.exists():
        cache = json.loads(args.cache.read_text())

    cited = registry_citations()
    # The cache's own keys count as known DOIs: they are what earlier runs
    # resolved, which is how a paper on disk for a DOI the registry does not cite
    # stays in the index.
    held, unmatched = local_pdfs(args.pdf_dir, set(cited) | set(cache) | set(SHARED_SOURCES))
    if unmatched:
        print(
            f"{unmatched} file(s) in {args.pdf_dir} match no DOI in the registry or the cache "
            "and are not indexed; see local_pdfs",
            file=sys.stderr,
        )
    dois = sorted(set(cited) | set(held) | set(SHARED_SOURCES))

    fetched = 0
    for doi in dois:
        if doi in cache and not args.refresh:
            continue
        meta = crossref(doi)
        cache[doi] = meta  # None is cached too: a DOI that does not resolve is worth remembering
        fetched += 1
        time.sleep(0.2)
        if meta is None:
            print(f"  DOI DOES NOT RESOLVE: {doi}", file=sys.stderr)
    if fetched:
        args.cache.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")
        print(f"fetched {fetched} records into {args.cache.name}")

    rows = []
    for doi in dois:
        m = cache.get(doi) or {}
        rows.append(
            {
                "doi": doi,
                "year": m.get("year") or "",
                "journal": m.get("journal") or "",
                "title": m.get("title") or "(DOI did not resolve)",
                "author": m.get("first_author") or "",
                "pdf": held.get(doi, ""),
                "assays": cited.get(doi, []),
                "shared": SHARED_SOURCES.get(doi, ""),
            }
        )
    rows.sort(key=lambda r: (-(r["year"] or 0), r["author"]))

    n_held = sum(1 for r in rows if r["pdf"])
    n_cited = sum(1 for r in rows if r["assays"])
    unresolved = [r for r in rows if r["title"].startswith("(DOI did not")]

    out = [
        "# Papers this registry depends on",
        "",
        f"Generated by `scripts/papers_index.py`. {len(rows)} papers: **{n_cited}** cited by at "
        f"least one registry entry, **{n_held}** held in `papers/` as full text "
        f"({', '.join(PAPER_SUFFIXES)}).",
        "",
        "`papers/` is gitignored because the PDFs are copyrighted, so this file is the durable "
        "record of what the project has actually read. Metadata is Crossref's, cached in "
        "`papers-index.cache.json` so the index rebuilds offline and so a DOI that changes what it "
        "resolves to shows up as a diff.",
        "",
        "Regenerate after adding an entry or a PDF:",
        "",
        "```bash",
        "python scripts/papers_index.py --out docs/papers-index.md",
        "```",
        "",
        "`held` says which format is in `papers/` and whether it is the article or its "
        "supplement; blank means the paper still needs to be obtained. A `.xml` is a "
        "publisher JATS deposit and a `.txt` is PMC open-access full text; neither is worse "
        "than a PDF, and all three are read by `verify_oligos_against_paper`. "
        "`assays` lists the registry entries that cite it - blank means the paper is held but "
        "nothing has been entered from it yet, which is a to-do rather than an error.",
        "",
        "| year | first author | journal | DOI | held | assays | title |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        # A shared source has no citing entry, so the column says what it is instead.
        a = "<br>".join(f"`{x}`" for x in r["assays"]) or (f"_{r['shared']}_" if r["shared"] else "")
        # Which file is held, not just whether one is: an article, its supplement, or both.
        held_names = r["pdf"].split(", ") if r["pdf"] else []
        kinds = []
        for n in held_names:
            ext = Path(n).suffix.lstrip(".")
            kinds.append(f"{ext} suppl" if SUPPLEMENT_SUFFIX + Path(n).suffix in n else ext)
        pdf = ", ".join(dict.fromkeys(kinds))
        out.append(
            f"| {r['year']} | {r['author']} | {r['journal'][:38]} | "
            f"[{r['doi']}](https://doi.org/{r['doi']}) | {pdf} | {a} | {r['title'][:96]} |"
        )
    if unresolved:
        out += ["", "## DOIs that did not resolve", ""]
        out += [
            f"- `{r['doi']}`" + (f" (cited by {', '.join(r['assays'])})" if r["assays"] else "")
            for r in unresolved
        ]
        out += [
            "",
            "A DOI that stops resolving is worth chasing: five entries in this registry once "
            "carried DOIs pointing at the wrong paper.",
        ]
    out += [
        "",
        "## Papers still wanted",
        "",
        "See `docs/journal/2026-10-05-papers-needed.md` for the prioritised list of papers not yet "
        "obtained, and `papers/papers-still-needed.md` for links.",
        "",
    ]

    text = "\n".join(out)
    summary = f"{len(rows)} papers, {n_held} held locally, {n_cited} cited"

    if args.check:
        current = args.out.read_text() if args.out.exists() else ""
        if current == text:
            return 0
        print(
            f"{args.out.relative_to(ROOT) if args.out.is_relative_to(ROOT) else args.out} is stale "
            f"({summary} now). Regenerate it and include it in this commit:\n"
            f"    python scripts/papers_index.py --out {args.out}",
            file=sys.stderr,
        )
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text)
    print(f"wrote {args.out} ({summary})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
