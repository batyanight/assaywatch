#!/usr/bin/env python3
"""Fetch Elsevier full text over the official API, for the papers this registry still needs.

    python scripts/fetch_elsevier.py                 # every outstanding Elsevier DOI
    python scripts/fetch_elsevier.py --doi 10.1016/j.vetmic.2012.07.030 -v

Elsevier is the largest single block of unreadable papers here: 12 of the 33
outstanding, carrying 42 of the 106 oligos that cannot currently be checked
against their source. Their publisher site blocks automated browsers outright
(error CPE00001 on the User-Agent), but Elsevier also runs a documented API for
exactly this purpose, so that is the route.

The key
-------
Read from `.secrets/elsevier.key` or `$ELSEVIER_API_KEY`, both gitignored. It is
never printed, never logged, and never written into an output file - only its
length is ever reported, and only to confirm it loaded. Get one free at
<https://dev.elsevier.com> with an institutional account.

Entitlement, and what was actually wrong here
--------------------------------------------
Full text is a SEPARATE entitlement from being able to read ScienceDirect, and a
valid key does not imply it. Tested 2026-10-05 with a real key, on and off the
NYU VPN:

    /content/search/scopus      200, real results   -> the key is fine
    /content/article/doi/...    403 AUTHENTICATION_ERROR
                                "Requestor configuration settings insufficient
                                 for access to this resource."

That message means the key's account is not configured for full-text retrieval.
It is not an IP problem, so the VPN does not help. The remedy is an Elsevier
INSTITUTIONAL TOKEN, issued to the institution for text and data mining and sent
as the `X-ELS-Insttoken` header; it also works off-network. Ask the NYU library
for one, referencing the ScienceDirect Article Retrieval API.

Put it in `.secrets/elsevier.insttoken` or `$ELSEVIER_INSTTOKEN` and this script
will send it automatically.

Without entitlement the API can also answer 200 with a metadata-only envelope -
the same reply you get with no key at all - which is why this script checks for
an actual body rather than trusting the status code.

Output
------
Full text is saved to `papers/` as `<doi with slashes as underscores>.xml`, so
`verify_oligos_against_paper.py --pdf-dir papers` picks it up beside the PDFs.
XML is better than a PDF here: no layout to fight, no table cells glued onto
sequences, and the primer tables come through as text.
"""

from __future__ import annotations

import argparse
import csv
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import yaml  # noqa: E402

from assaywatch.credentials import contact_email, read_secret, read_secret_file  # noqa: E402

API = "https://api.elsevier.com/content/article/doi/"
ELSEVIER_PREFIXES = ("10.1016", "10.1006", "10.1053", "10.1054")


def load_secret(explicit: Path | None, env_var: str, default_name: str) -> str:
    """A credential, from a file or the environment. Never echoed, only measured.

    Read by `assaywatch.credentials`, so a key file from Windows PowerShell (UTF-16)
    or Notepad (a UTF-8 byte-order mark) is read correctly, or refused with a reason
    by `python -m assaywatch.credentials`, instead of crashing here or sending a key
    with an invisible character on the front of it.
    """
    if explicit and explicit.exists():
        return read_secret_file(explicit)
    return read_secret((env_var, default_name))


def has_body(xml: str) -> bool:
    """Does this response actually contain the article, or only its metadata?

    Elsevier answers 200 with a `full-text-retrieval-response` envelope either
    way, so the status code says nothing. The article body arrives as
    `originalText` or a `<xocs:doc>`/`<ce:sections>` block; a metadata-only
    reply has neither and is a few hundred bytes.
    """
    return ("originalText" in xml or "<xocs:doc" in xml or "ce:section" in xml) and len(xml) > 8000


def outstanding(registry: Path, pdf_dir: Path) -> list[str]:
    """Elsevier DOIs cited by the registry with nothing readable held locally."""
    held = {p.stem.replace("_", "/").lower() for p in pdf_dir.glob("*")} if pdf_dir.exists() else set()
    out = []
    for f in sorted(registry.glob("*.yaml")):
        d = yaml.safe_load(f.read_text())
        doi = ((d.get("citation") or {}).get("doi") or "").lower()
        if doi.startswith(ELSEVIER_PREFIXES) and doi not in held and doi not in out:
            out.append(doi)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--pdf-dir", type=Path, default=ROOT / "papers")
    ap.add_argument("--key-file", type=Path, default=None)
    ap.add_argument(
        "--insttoken-file",
        type=Path,
        default=None,
        help="Elsevier institutional token; unlocks full text off-network",
    )
    ap.add_argument("--doi", action="append")
    ap.add_argument("--tsv", type=Path, default=ROOT / "results" / "elsevier-fetch.tsv")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    key = load_secret(args.key_file, "ELSEVIER_API_KEY", "elsevier.key")
    insttoken = load_secret(args.insttoken_file, "ELSEVIER_INSTTOKEN", "elsevier.insttoken")
    if not key:
        print(
            "No API key. Put one in .secrets/elsevier.key or $ELSEVIER_API_KEY "
            "(see .secrets/README.md); free at https://dev.elsevier.com",
            file=sys.stderr,
        )
        return 1
    # Only the length, never the value.
    print(
        f"key loaded ({len(key)} chars)"
        + (
            f", institutional token loaded ({len(insttoken)} chars)"
            if insttoken
            else ", no institutional token"
        )
    )

    dois = [d.lower() for d in args.doi] if args.doi else outstanding(args.registry, args.pdf_dir)
    print(f"{len(dois)} Elsevier DOIs to fetch\n")

    rows, got = [], 0
    for doi in dois:
        status, note, size = "", "", 0
        try:
            req = urllib.request.Request(
                API + doi,
                headers={
                    "X-ELS-APIKey": key,
                    **({"X-ELS-Insttoken": insttoken} if insttoken else {}),
                    "Accept": "text/xml",
                    "User-Agent": f"assaywatch/0.1 (research; {contact_email() or 'unset'})",
                },
            )
            with urllib.request.urlopen(req, timeout=90) as r:
                xml = r.read().decode("utf-8", "replace")
            size = len(xml)
            if has_body(xml):
                dest = args.pdf_dir / (doi.replace("/", "_") + ".xml")
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(xml)
                status, got = "full-text", got + 1
                note = f"{size // 1024} KB"
            else:
                status = "metadata-only"
                note = "no entitlement from this network, or not in the full-text corpus"
        except urllib.error.HTTPError as e:
            status, note = (
                f"HTTP {e.code}",
                {
                    401: "key rejected",
                    403: (
                        "no full-text entitlement - the key is valid but its account is not "
                        "configured for it; an institutional token is what fixes this"
                    ),
                    404: "not in the Elsevier full-text corpus",
                    429: "rate limited - slow down",
                }.get(e.code, e.reason),
            )
        except Exception as e:  # noqa: BLE001
            status, note = "error", type(e).__name__
        rows.append({"doi": doi, "status": status, "bytes": size, "note": note})
        if args.verbose or status != "full-text":
            print(f"  {status:14s} {doi:42s} {note}")
        time.sleep(0.8)  # Elsevier's weekly quota is generous, its rate limit is not

    print(f"\n  {got} of {len(dois)} full texts saved to {args.pdf_dir}")
    if got:
        print("  re-run: python scripts/verify_oligos_against_paper.py --pdf-dir papers")
    if any(r["status"] == "metadata-only" for r in rows):
        print(
            "\n  'metadata-only' means the API answered but withheld the body. Check you are on "
            "the NYU network or VPN - entitlement is by institution, not by key."
        )
    args.tsv.parent.mkdir(parents=True, exist_ok=True)
    with args.tsv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, ["doi", "status", "bytes", "note"], delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
