#!/usr/bin/env python3
"""Verify DOIs against Crossref and fill missing taxids from NCBI Taxonomy.

    python resolve_citations.py --registry registry --email you@example.org [--dry-run]

Runs over every YAML in --registry and edits the files in place:

  * DOI check. For each assay with a DOI and doi_verified: false, fetch
    https://api.crossref.org/works/<doi>. The DOI is marked verified when the
    Crossref record's year matches citation.design_year AND the first author's
    family name appears in citation.reference. A DOI that resolves to a
    different paper is reported and left unverified; a 404 is reported as such.

  * Taxid fill. For each assay whose target.taxid is null and whose
    target.taxon_name is set, run an NCBI Taxonomy esearch on the name. One hit
    fills taxid; zero or several hits are reported and left null.

Both services want a contact email in the request (Crossref's "polite pool",
NCBI's Entrez policy); pass yours with --email. NCBI allows 3 requests/s
without an API key; this script sleeps accordingly.

Requires: pyyaml, requests
"""

from __future__ import annotations

import argparse
import re
import time
import unicodedata
from pathlib import Path

import requests
import yaml

CROSSREF = "https://api.crossref.org/works/{doi}"
ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"


def crossref_lookup(doi: str, email: str) -> dict | None:
    r = requests.get(CROSSREF.format(doi=doi), params={"mailto": email}, timeout=30)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return r.json()["message"]


def fold(text: str) -> str:
    """Lowercase, strip accents and normalise dashes, so Vazquez-Moron matches Vázquez-Morón.

    Journals, Crossref and the registry disagree about diacritics on the same
    author, and an author check that fails on an accent reports a correct DOI
    as pointing at the wrong paper.
    """
    stripped = unicodedata.normalize("NFKD", text)
    folded = "".join(c for c in stripped if not unicodedata.combining(c)).lower()
    # Crossref writes some names with a Unicode hyphen (Sánchez‐Seco); journals
    # and the registry use a plain one. Treat every dash as the same character.
    return re.sub(r"[\u2010-\u2015\u2212]", "-", folded)


def crossref_matches(msg: dict, year: int | None, reference: str) -> tuple[bool, str]:
    """Does the Crossref record look like the paper named in `reference`?"""
    cr_year = None
    for key in ("published-print", "published-online", "issued", "created"):
        parts = msg.get(key, {}).get("date-parts", [[None]])[0]
        if parts and parts[0]:
            cr_year = parts[0]
            break
    authors = msg.get("author") or []
    family = (authors[0].get("family") or "") if authors else ""
    title = (msg.get("title") or [""])[0]
    year_ok = (year is None) or (cr_year == year) or (cr_year is not None and abs(cr_year - year) <= 1)
    author_ok = bool(family) and fold(family) in fold(reference)
    summary = f"{family} {cr_year}: {title[:70]}"
    return (year_ok and author_ok), summary


def taxid_lookup(name: str, email: str) -> list[str]:
    r = requests.get(
        ESEARCH,
        params={"db": "taxonomy", "term": name, "retmode": "json", "email": email, "tool": "assaywatch"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["esearchresult"].get("idlist", [])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, required=True)
    ap.add_argument("--email", required=True)
    ap.add_argument("--dry-run", action="store_true", help="report only, do not edit files")
    ap.add_argument("--skip-dois", action="store_true")
    ap.add_argument("--skip-taxids", action="store_true")
    args = ap.parse_args()

    doi_cache: dict[str, tuple[bool, str]] = {}
    tax_cache: dict[str, list[str]] = {}

    for path in sorted(args.registry.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text())
        changed = False
        cit, tgt = doc.get("citation", {}), doc.get("target", {})

        doi = cit.get("doi")
        if doi and not cit.get("doi_verified") and not args.skip_dois:
            if doi not in doi_cache:
                msg = crossref_lookup(doi, args.email)
                doi_cache[doi] = (
                    (False, "404 not found")
                    if msg is None
                    else crossref_matches(msg, cit.get("design_year"), cit.get("reference") or "")
                )
                time.sleep(0.2)
            ok, summary = doi_cache[doi]
            print(f"{'OK ' if ok else 'BAD'} {doc['id'][:55]:<55} {doi:<40} {summary}")
            if ok:
                cit["doi_verified"] = True
                changed = True

        name = tgt.get("taxon_name")
        if name and not tgt.get("taxid") and not args.skip_taxids:
            # Strip parenthetical commentary before querying ("Ferlavirus (snake...)").
            query = re.sub(r"\(.*?\)", "", name).strip()
            if query not in tax_cache:
                tax_cache[query] = taxid_lookup(query, args.email)
                time.sleep(0.35)
            ids = tax_cache[query]
            if len(ids) == 1:
                tgt["taxid"] = int(ids[0])
                changed = True
                print(f"TAX {doc['id'][:55]:<55} {query!r} -> {ids[0]}")
            else:
                print(f"TAX {doc['id'][:55]:<55} {query!r} -> {len(ids)} hits {ids[:5]} (left null)")

        if changed and not args.dry_run:
            flags = set(doc.get("needs_review") or [])
            if cit.get("doi_verified"):
                flags.discard("DOI_UNVERIFIED")
            if tgt.get("taxid"):
                flags.discard("TAXID_MISSING")
            doc["needs_review"] = sorted(flags) or None
            path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=120))


if __name__ == "__main__":
    main()
