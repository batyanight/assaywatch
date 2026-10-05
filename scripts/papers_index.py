#!/usr/bin/env python3
"""Keep a committed index of every paper this registry depends on.

    python scripts/papers_index.py --out docs/papers-index.md
    python scripts/papers_index.py --out docs/papers-index.md --refresh

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

CROSSREF = "https://api.crossref.org/works/"
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")


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


def registry_citations() -> dict[str, list[str]]:
    """{doi: [assay ids citing it]} over the whole registry."""
    out: dict[str, list[str]] = defaultdict(list)
    for f in sorted((ROOT / "registry").glob("*.yaml")):
        d = yaml.safe_load(f.read_text())
        doi = (d.get("citation") or {}).get("doi")
        if doi:
            out[doi.lower()].append(d["id"])
    return out


def local_pdfs(pdf_dir: Path) -> dict[str, str]:
    """{doi: filename} for PDFs named after their DOI, as papers/ is."""
    out = {}
    for p in sorted(pdf_dir.glob("*.pdf")):
        stem = p.stem.replace("_", "/")
        if DOI_RE.match(stem):
            out[stem.lower()] = p.name
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "papers-index.md")
    ap.add_argument("--pdf-dir", type=Path, default=ROOT / "papers")
    ap.add_argument("--cache", type=Path, default=ROOT / "docs" / "papers-index.cache.json")
    ap.add_argument("--refresh", action="store_true", help="re-fetch every DOI instead of using the cache")
    args = ap.parse_args(argv)

    cache: dict = {}
    if args.cache.exists() and not args.refresh:
        cache = json.loads(args.cache.read_text())

    cited = registry_citations()
    held = local_pdfs(args.pdf_dir) if args.pdf_dir.exists() else {}
    dois = sorted(set(cited) | set(held))

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
        f"least one registry entry, **{n_held}** held as a PDF in `papers/`.",
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
        "`PDF` means a copy is in `papers/`; blank means the paper still needs to be obtained. "
        "`assays` lists the registry entries that cite it - blank means the paper is held but "
        "nothing has been entered from it yet, which is a to-do rather than an error.",
        "",
        "| year | first author | journal | DOI | PDF | assays | title |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        a = "<br>".join(f"`{x}`" for x in r["assays"])
        pdf = "yes" if r["pdf"] else ""
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
        "See `docs/2026-10-05-papers-needed.md` for the prioritised list of papers not yet "
        "obtained, and `papers/papers-still-needed.md` for links.",
        "",
    ]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(out))
    print(f"wrote {args.out} ({len(rows)} papers, {n_held} held locally, {n_cited} cited)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
