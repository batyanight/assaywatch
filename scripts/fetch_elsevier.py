#!/usr/bin/env python3
"""Fetch Elsevier (10.1016/...) PDFs through the Elsevier Article Retrieval API.

Usage (from the repo root):
    python scripts/fetch_elsevier.py --list papers/papers-still-needed-2026-10-24.md
    python scripts/fetch_elsevier.py --doi 10.1016/j.jviromet.2007.05.021 --doi 10.1016/...

Credentials (read, never printed):
    ELSEVIER_API_KEY     required. Env var, or a KEY=VALUE line in ./.env (gitignore it).
    ELSEVIER_INSTTOKEN   optional. Institutional token, only if Elsevier issued you one.

Output:
    papers/<doi_stem>.pdf                one file per DOI that came back as a real PDF
    results/elsevier-fetch.tsv           one row per DOI: doi, http, outcome, detail, path

Filenames go through `assaywatch.papers.doi_stem`, like everything else that writes
into `papers/`. This script used to carry its own `slug()`, a fourth private copy of
the convention that module exists to hold; its output happened to agree because every
reader lowercases, which is what made it worth removing before it stopped agreeing.

Why the API can say no even with a valid key: full text is gated on *entitlement*, which
Elsevier decides per request from (a) the article being open access, (b) the request's IP
being inside a subscribing institution's registered ranges, or (c) an X-ELS-Insttoken.
A plain key from a non-institutional IP gets OA articles and AUTHORIZATION_ERROR on the rest.
The TSV makes that visible per DOI instead of guessing.

This asks for `application/pdf`, so the guard against a metadata-only reply is the
`%PDF` magic number rather than the `<body>` test the XML fetcher needed. The reason
that test exists is worth carrying: Elsevier answers 200 with a
`full-text-retrieval-response` envelope whether or not it contains the article, so the
status line says nothing. Mao, Hedrick & Chinchar 1997 (10.1006/viro.1996.8435, the
pan-ranavirus MCP design paper) came back on 2026-10-24 as 110 KB of metadata,
abstract and references with no body and no sequence anywhere in it, and was saved and
reported as full text. A paper wrongly recorded as held is the expensive kind of error
here - it is what sent a reader after Santee 2003 behind a paywall it is not behind.
Bytes, never the status code.
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from assaywatch.credentials import read_secret
from assaywatch.papers import doi_stem, held_dois

API = "https://api.elsevier.com/content/article/doi/"
# The needed-papers markdown always renders the DOI as [DOI](https://doi.org/DOI).
# Matching that exact shape is safer than a loose DOI regex, because some Elsevier
# DOIs contain parentheses (e.g. 10.1016/s0166-0934(02)00148-9) that a generic
# pattern would cut in half.
LINKED_DOI_RE = re.compile(r"\[(10\.1016/[^\]]+)\]\(https://doi\.org/")
PAUSE_S = 0.5  # stay well under Elsevier's per-second limit


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_credentials() -> tuple[str, str | None]:
    """The API key and optional institutional token. Never echoed, only measured.

    Read through `assaywatch.credentials`, which is where this project keeps
    credentials: an environment variable if set, else `.secrets/<name>`. Going
    through it also means a key file written by Windows PowerShell (UTF-16) or
    Notepad (a UTF-8 byte-order mark) is decoded correctly, or refused with a
    reason by `assaywatch credentials`, rather than being sent with an
    invisible character on the front of it.

    This replaced a loader that read only environment variables and a `./.env`
    file. Measured 2026-10-25: neither variable was set, `.env` held a stale
    `ELSEVIER_API_KEY`, and the real credentials were in `.secrets/elsevier.key`
    and `.secrets/elsevier.insttoken` all along - so the script sent the stale
    key, got `AUTHENTICATION_ERROR: Invalid API Key`, and then reported "no
    ELSEVIER_INSTTOKEN set" about a token sitting on disk. Two wrong answers from
    one wrong source. `.env` is no longer consulted; `python -m
    assaywatch.credentials` is the one place that says what is configured.
    """
    key = read_secret(("ELSEVIER_API_KEY", "elsevier.key"))
    inst = read_secret(("ELSEVIER_INSTTOKEN", "elsevier.insttoken"))
    if not key:
        sys.exit(
            "ELSEVIER_API_KEY not set. Put it in $ELSEVIER_API_KEY or "
            ".secrets/elsevier.key, then check with `assaywatch credentials`."
        )
    return key, inst or None


def dois_from_list(path: Path) -> list[str]:
    seen: list[str] = []
    for m in LINKED_DOI_RE.finditer(path.read_text()):
        doi = m.group(1).strip()
        if doi not in seen:
            seen.append(doi)
    return seen


def fetch_pdf(doi: str, key: str, inst: str | None) -> tuple[int, str, bytes]:
    url = API + quote(doi, safe="/") + "?httpAccept=application/pdf"
    req = urllib.request.Request(
        url,
        headers={
            "X-ELS-APIKey": key,
            "Accept": "application/pdf",
            "User-Agent": "assaywatch-fetch/1.0",
        },
    )
    if inst:
        req.add_header("X-ELS-Insttoken", inst)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read()
    except urllib.error.HTTPError as e:
        # 401/403/404 bodies are JSON with Elsevier's own status code; keep them.
        return e.code, e.headers.get("Content-Type", ""), e.read()
    except urllib.error.URLError as e:
        return 0, "", str(e.reason).encode()


def explain_error(body: bytes) -> str:
    """Pull Elsevier's statusCode/statusText out of an error body, if present."""
    try:
        j = json.loads(body.decode("utf-8", "replace"))
        st = j["service-error"]["status"]
        return f"{st.get('statusCode')}: {st.get('statusText')}"
    except (ValueError, KeyError, TypeError, AttributeError):
        # Not Elsevier's JSON error envelope: a plain-text or HTML body, or JSON
        # shaped differently. Fall back to the first 200 characters of whatever
        # arrived, which is what makes an unexpected reply legible in the TSV.
        txt = body.decode("utf-8", "replace").strip().replace("\t", " ").replace("\n", " ")
        return txt[:200]


def page_count(pdf: bytes) -> int | None:
    """Pages in this PDF, or None if it cannot be counted.

    The guard behind `first-page-only`. Measured 2026-10-25: this API answered
    200 with a real, well-formed PDF containing **only the article's first page**
    for four of five titles tried - `Veterinary Parasitology 178 (2011) 208-216`
    and `J Virol Methods 195 (2014) 100-105` both arrived as one page, 1.1 MB and
    850 KB respectively, so neither size nor status nor the `%PDF` magic number
    distinguishes them from the real thing. Mao 1997 came through complete at 9
    pages, so it is per-title and not a blanket entitlement limit.

    Saving those under a canonical `doi_stem` name is the error this project
    calls the expensive one: a paper recorded as held that does not contain its
    own primer table, which stops anyone looking for it again. Counting pages is
    the cheapest test that catches it.

    Uses pypdf, which is the `pdf` extra (see docs/installation.md). Without it
    this returns None and the caller saves as before rather than refusing on an
    unmeasured guess.
    """
    try:
        import io

        from pypdf import PdfReader
    except ImportError:
        return None
    try:
        return len(PdfReader(io.BytesIO(pdf)).pages)
    except Exception:  # noqa: BLE001 - any malformed PDF means "cannot count"
        return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", type=Path, help="papers-still-needed markdown to pull 10.1016 DOIs from")
    ap.add_argument("--doi", action="append", default=[], help="explicit DOI (repeatable)")
    ap.add_argument("--pdf-dir", type=Path, default=repo_root() / "papers")
    ap.add_argument("--log", type=Path, default=repo_root() / "results" / "elsevier-fetch.tsv")
    ap.add_argument("--force", action="store_true", help="re-download even if the file exists")
    ap.add_argument(
        "--allow-single-page",
        action="store_true",
        help="keep a one-page reply (for a genuinely one-page article; see page_count)",
    )
    args = ap.parse_args()

    dois = list(args.doi)
    if args.list:
        dois += [d for d in dois_from_list(args.list) if d not in dois]
    if not dois:
        sys.exit("No DOIs: pass --list <markdown> and/or --doi <doi>.")

    key, inst = load_credentials()
    args.pdf_dir.mkdir(parents=True, exist_ok=True)
    args.log.parent.mkdir(parents=True, exist_ok=True)
    new_log = not args.log.exists()

    counts = {"saved": 0, "skipped": 0, "first-page-only": 0, "not-entitled": 0, "error": 0}
    # Forward-mapped through held_dois, never `stem.replace("_", "/")`, and over any
    # extension: eleven of these papers are held as Elsevier `.xml` deposits, and a
    # PDF-only check would re-fetch every one of them over the API.
    held = held_dois(dois, args.pdf_dir)
    with args.log.open("a") as log:
        if new_log:
            log.write("doi\thttp\toutcome\tdetail\tpath\n")
        for i, doi in enumerate(dois, 1):
            out = args.pdf_dir / f"{doi_stem(doi)}.pdf"
            already = doi.strip().lower() in held and not args.force
            # A truncated or HTML-bodied `.pdf` left by an earlier run is not a held paper.
            if already and out.exists() and out.read_bytes()[:4] != b"%PDF":
                already = False
            if already:
                outcome, http, detail = "skipped", "-", "already held"
                counts["skipped"] += 1
            else:
                http, ctype, body = fetch_pdf(doi, key, inst)
                # Trust the bytes, not the status line: a 200 that isn't a PDF is still a miss.
                if http == 200 and body[:4] == b"%PDF":
                    pages = page_count(body)
                    if pages == 1 and not args.allow_single_page:
                        # A first-page-only reply. Not saved: see page_count.
                        outcome = "first-page-only"
                        detail = (
                            f"{len(body)} bytes, 1 page - not the article; --allow-single-page to keep it"
                        )
                        counts["first-page-only"] += 1
                    else:
                        out.write_bytes(body)
                        outcome = "saved"
                        detail = f"{len(body)} bytes" + (f", {pages} pages" if pages else "")
                        counts["saved"] += 1
                elif http in (401, 403):
                    outcome, detail = "not-entitled", explain_error(body)
                    counts["not-entitled"] += 1
                else:
                    outcome = "error"
                    detail = f"content-type={ctype or '?'}; {explain_error(body)}"
                    counts["error"] += 1
                time.sleep(PAUSE_S)
            print(f"[{i:2d}/{len(dois)}] {outcome:13s} {doi}  {detail}")
            log.write(f"{doi}\t{http}\t{outcome}\t{detail}\t{out if outcome == 'saved' else ''}\n")
            log.flush()

    print("\n" + "  ".join(f"{k}={v}" for k, v in counts.items()))
    if counts["not-entitled"]:
        # Say which of the two situations it is, rather than assuming the token is
        # missing: an insttoken IS configured here, so "no token" was the wrong
        # diagnosis and sent the reader after the wrong fix.
        if inst:
            print(
                "not-entitled WITH an insttoken configured: the token or key may be "
                "wrong or expired, or it does not cover this title. Check what is set "
                "with `assaywatch credentials`, and the per-DOI statusText "
                "in the log for which it is."
            )
        else:
            print(
                "not-entitled with no ELSEVIER_INSTTOKEN set: this IP is not recognised as NYU's.\n"
                "Re-run from an NYU-registered network / VPN, or ask the library for an insttoken."
            )


if __name__ == "__main__":
    main()
