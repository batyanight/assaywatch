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
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from assaywatch.credentials import contact_email

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import yaml  # noqa: E402

from assaywatch.papers import doi_stem, held_dois  # noqa: E402

UNPAYWALL = "https://api.unpaywall.org/v2/"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
UA = {"User-Agent": f"assaywatch/0.1 (research tool; {contact_email() or 'unset'})"}
# Some publishers serve a free PDF but refuse an unfamiliar User-Agent with a
# 403 - an anti-bot rule, not a paywall; Inter-Research's Diseases of Aquatic
# Organisms is one. On a 403 the fetch is retried once with a browser string.
# This is only ever applied to files Unpaywall already reports as open, and the
# request rate stays low.
BROWSER_UA = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept": "application/pdf,*/*",
}


def get_json(url: str, timeout: int = 40):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except Exception:  # noqa: BLE001 - a missing record is data, not a crash
        return None


def unpaywall(doi: str, email: str) -> dict:
    d = get_json(f"{UNPAYWALL}{urllib.parse.quote(doi, safe='')}?email={urllib.parse.quote(email)}")
    if not d:
        return {}
    best = d.get("best_oa_location") or {}
    # Prefer a location that actually offers a PDF; best_oa_location sometimes
    # only has a landing page while another location has the file itself.
    pdf = best.get("url_for_pdf")
    if not pdf:
        for loc in d.get("oa_locations") or []:
            if loc.get("url_for_pdf"):
                best, pdf = loc, loc["url_for_pdf"]
                break
    return {
        "is_oa": bool(d.get("is_oa")),
        "oa_status": d.get("oa_status") or "",
        "host_type": best.get("host_type") or "",
        "version": best.get("version") or "",
        "url_pdf": pdf or "",
        "url_landing": best.get("url_for_landing_page") or best.get("url") or "",
        "title": (d.get("title") or "")[:110],
    }


def openalex(doi: str, email: str) -> dict:
    """OpenAlex's view of where a free copy is.

    Worth querying alongside Unpaywall even though both ultimately describe the
    same landscape: they disagree in practice. For doi:10.1177/1040638711416846
    Unpaywall reported no PDF while OpenAlex gave a direct publisher PDF link.
    Two cheap lookups are better than missing a paper.
    """
    d = get_json(
        f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi, safe='')}"
        f"?mailto={urllib.parse.quote(email)}"
    )
    if not d:
        return {}
    loc = d.get("best_oa_location") or {}
    return {
        "is_oa": bool((d.get("open_access") or {}).get("is_oa")),
        "url_pdf": loc.get("pdf_url") or "",
        "version": loc.get("version") or "",
        "host_type": loc.get("source", {}).get("type", "") if isinstance(loc.get("source"), dict) else "",
    }


def pmcid(doi: str) -> str:
    q = urllib.parse.urlencode({"query": f'DOI:"{doi}"', "format": "json", "resultType": "lite"})
    d = get_json(f"{EPMC}/search?{q}")
    for r in ((d or {}).get("resultList") or {}).get("result", []):
        if r.get("pmcid") and r.get("isOpenAccess") == "Y":
            return r["pmcid"]
    return ""


def needed_dois(registry: Path, pdf_dir: Path) -> list[tuple[str, list[str]]]:
    """DOIs cited by the registry for which no local copy of the paper is held.

    "Local copy", not "local PDF": verify_oligos_against_paper reads `.pdf`,
    `.xml` and `.txt`, so a plaintext conversion on disk means the paper does
    not need fetching. The old glob was `*.pdf`, which counted the three `.txt`
    papers as missing on top of the ten its reverse-mapped filenames lost.
    """
    # Forward-mapped, never reverse. Reverse-mapping filenames reported 10 of
    # the 26 "missing" DOIs as missing while their PDFs were in papers/, all of
    # them with parenthesised DOIs; see assaywatch/papers.py.
    all_dois = [
        ((yaml.safe_load(f.read_text()).get("citation") or {}).get("doi") or "")
        for f in sorted(registry.glob("*.yaml"))
    ]
    held = held_dois([d for d in all_dois if d], pdf_dir)
    by_doi: dict[str, list[str]] = {}
    for f in sorted(registry.glob("*.yaml")):
        d = yaml.safe_load(f.read_text())
        doi = ((d.get("citation") or {}).get("doi") or "").lower()
        if doi and doi not in held:
            by_doi.setdefault(doi, []).append(d["id"])
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
                try:
                    blob = b""
                    for headers in (UA, BROWSER_UA):
                        try:
                            req = urllib.request.Request(row["url_pdf"], headers=headers)
                            with urllib.request.urlopen(req, timeout=120) as r:
                                blob = r.read()
                            break
                        except urllib.error.HTTPError as he:
                            if he.code != 403 or headers is BROWSER_UA:
                                raise
                            time.sleep(1.0)
                    # A paywall often answers with an HTML interstitial and a 200.
                    if blob[:5] == b"%PDF-":
                        args.pdf_dir.mkdir(parents=True, exist_ok=True)
                        dest.write_bytes(blob)
                        row["downloaded"] = f"{len(blob) // 1024} KB"
                        got += 1
                    else:
                        row["downloaded"] = "not a PDF"
                except Exception as e:  # noqa: BLE001
                    row["downloaded"] = f"failed: {type(e).__name__}"
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
