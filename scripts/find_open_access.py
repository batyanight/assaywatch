#!/usr/bin/env python3
"""Find legally open copies of the papers this registry still needs, and fetch them.

    python scripts/find_open_access.py                      # report only
    python scripts/find_open_access.py --download           # fetch what is openly available
    python scripts/find_open_access.py --doi 10.1128/jcm.01264-10 -v

Most of this registry's sequences cannot be checked because the paper is behind
a paywall. A surprising share of those papers nonetheless have a legal free copy
somewhere: the publisher opened it later, or the authors deposited the accepted
manuscript in an institutional repository or on a preprint server. Those copies
are findable programmatically, so there is no need to go anywhere dubious for
them.

Sources, in the order tried:

1. **Unpaywall** (`api.unpaywall.org`), which indexes publisher OA, PubMed
   Central, and author self-archived repository and preprint copies. It is built
   for exactly this question and reports which version a link is - published,
   accepted or submitted - which matters here, because a *submitted* preprint
   may carry different primer sequences from the final paper.
2. **Europe PMC**, for a PMCID, which gives machine-readable full text rather
   than a PDF and is what `verify_oligos_against_paper.py` prefers.

Deliberately not used: sites that host publisher PDFs uploaded in breach of the
author agreement. Beyond the legal question, they are a poor foundation for a
reproducible pipeline - the copy can vanish, and there is no version label, so
you cannot tell an accepted manuscript from the published paper. Where no legal
copy exists, the honest answer is the NYU library link, which
`papers/papers-still-needed.md` already carries.

`--download` saves only files Unpaywall reports as open, named by DOI so that
`verify_oligos_against_paper.py --pdf-dir papers` picks them up automatically.

A VERSION WARNING worth heeding: a `submittedVersion` is the preprint. For a
methods paper the primer table usually survives review unchanged, but not
always, so anything read from a preprint should say so in `notes_curator`.
"""

from __future__ import annotations

import argparse
import csv
import sys
import time
from dataclasses import asdict
from pathlib import Path

from assaywatch.credentials import contact_email

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch import papers, registry  # noqa: E402
from assaywatch.papers import doi_stem, held_dois  # noqa: E402

_GET = papers.http(timeout=40)


def unpaywall(doi: str, email: str) -> dict:
    oa = papers.unpaywall(doi, _GET, email=email)
    return asdict(oa) if oa else {}


def openalex(doi: str, email: str) -> dict:
    oa = papers.openalex(doi, _GET, email=email)
    return asdict(oa) if oa else {}


def pmcid(doi: str) -> str:
    return papers.pmcid_for(doi, _GET, email=contact_email() or "") or ""


def needed_dois(registry_dir: Path, pdf_dir: Path) -> list[tuple[str, list[str]]]:
    """DOIs cited by the registry for which no local copy of the paper is held.

    "Local copy", not "local PDF": verify_oligos_against_paper reads `.pdf`,
    `.xml` and `.txt`, so a plaintext conversion on disk means the paper does
    not need fetching. The old glob was `*.pdf`, which counted the three `.txt`
    papers as missing on top of the ten its reverse-mapped filenames lost.
    """
    # Forward-mapped, never reverse. Reverse-mapping filenames reported 10 of
    # the 26 "missing" DOIs as missing while their PDFs were in papers/, all of
    # them with parenthesised DOIs; see assaywatch/papers.py.
    assays = list(registry.load(registry_dir).values())
    held = held_dois([a.citation.doi for a in assays if a.citation.doi], pdf_dir)
    by_doi: dict[str, list[str]] = {}
    for a in assays:
        doi = (a.citation.doi or "").lower()
        if doi and doi not in held:
            by_doi.setdefault(doi, []).append(a.id)
    return sorted(by_doi.items())


COLS = [
    "doi",
    "is_oa",
    "oa_status",
    "host_type",
    "version",
    "pmcid",
    "url_pdf",
    "url_landing",
    "downloaded",
    "assays",
    "title",
]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--pdf-dir", type=Path, default=ROOT / "papers")
    ap.add_argument("--doi", action="append", help="check these DOIs instead of the registry's")
    ap.add_argument("--email", default=None, help="Unpaywall requires one")
    ap.add_argument("--download", action="store_true", help="fetch the PDFs that are openly available")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "open-access-lookup.tsv")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)
    # Resolved after parsing, so --help works with no address set and the
    # repository carries none. See assaywatch.credentials.contact_email.
    args.email = args.email or contact_email()

    if args.doi:
        targets = [(d.lower(), []) for d in args.doi]
    else:
        targets = needed_dois(args.registry, args.pdf_dir)
    print(f"{len(targets)} DOIs with no local PDF\n")

    rows, got = [], 0
    for doi, assays in targets:
        u = unpaywall(doi, args.email)
        time.sleep(0.15)
        # Fall back to OpenAlex when Unpaywall finds no PDF: they disagree often
        # enough that the second lookup is worth its 0.15 s.
        if not u.get("url_pdf"):
            oa = openalex(doi, args.email)
            time.sleep(0.15)
            if oa.get("url_pdf"):
                u["url_pdf"] = oa["url_pdf"]
                u["is_oa"] = u.get("is_oa") or oa.get("is_oa")
                u["version"] = u.get("version") or oa.get("version")
                u["oa_status"] = u.get("oa_status") or "openalex"
        pid = pmcid(doi) if not u.get("url_pdf") else ""
        time.sleep(0.15)
        row = {
            "doi": doi,
            "is_oa": "yes" if u.get("is_oa") else "",
            "oa_status": u.get("oa_status", ""),
            "host_type": u.get("host_type", ""),
            "version": u.get("version", ""),
            "pmcid": pid,
            "url_pdf": u.get("url_pdf", ""),
            "url_landing": u.get("url_landing", ""),
            "downloaded": "",
            "assays": "; ".join(assays),
            "title": u.get("title", ""),
        }
        if args.download and row["url_pdf"]:
            dest = args.pdf_dir / (doi_stem(doi) + ".pdf")
            if dest.exists():
                row["downloaded"] = "already"
            else:
                # A paywall often answers with an HTML interstitial and a 200;
                # download_pdf returns None for anything that is not a PDF.
                blob = papers.download_pdf(row["url_pdf"], _GET, args.email or "")
                if blob:
                    args.pdf_dir.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(blob)
                    row["downloaded"] = f"{len(blob) // 1024} KB"
                    got += 1
                else:
                    row["downloaded"] = "not a PDF"
                time.sleep(0.5)
        rows.append(row)
        if args.verbose:
            print(f"  {doi:44s} oa={row['oa_status']:8s} {row['version']:18s} {row['downloaded']}")

    oa = [r for r in rows if r["is_oa"]]
    pdfs = [r for r in rows if r["url_pdf"]]
    pmcs = [r for r in rows if r["pmcid"]]
    sub = [r for r in oa if r["version"] == "submittedVersion"]
    print(f"\n  {len(oa)} of {len(rows)} have a legal open copy")
    print(f"  {len(pdfs)} offer a direct PDF, {len(pmcs)} more have open full text in PMC")
    print(f"  {len(sub)} of the open copies are SUBMITTED versions (preprints) - a primer table")
    print("     read from one must say so, since it may differ from the published paper")
    if args.download:
        print(f"\n  downloaded {got} new PDFs into {args.pdf_dir}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, COLS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {args.out}")
    print(
        "\nNothing open was found for the rest; use the NYU links in papers/papers-still-needed.md.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
