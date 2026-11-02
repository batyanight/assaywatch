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

The Crossref rule is assaywatch.papers.citation_matches; the lookup is assaywatch.ncbi.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch import ncbi, papers, registry  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, required=True)
    ap.add_argument("--email", required=True)
    ap.add_argument("--dry-run", action="store_true", help="report only, do not edit files")
    ap.add_argument("--skip-dois", action="store_true")
    ap.add_argument("--skip-taxids", action="store_true")
    args = ap.parse_args()
    get = papers.http()
    transport = ncbi.eutils(args.email, ncbi.api_key())
    doi_cache: dict[str, tuple[bool, str]] = {}
    tax_cache: dict[str, list[int]] = {}
    for path in registry.files(args.registry):
        assay = registry.load_one(path)
        changes: dict[str, object] = {}
        doi = assay.citation.doi
        if doi and not assay.citation.doi_verified and not args.skip_dois:
            if doi not in doi_cache:
                cit = papers.crossref(doi, get, email=args.email)
                doi_cache[doi] = (
                    (False, "404 not found")
                    if cit is None
                    else papers.citation_matches(
                        cit, assay.citation.design_year, assay.citation.reference or ""
                    )
                )
                time.sleep(0.2)
            ok, summary = doi_cache[doi]
            print(f"{'OK ' if ok else 'BAD'} {assay.id[:55]:<55} {doi:<40} {summary}")
            if ok:
                changes["citation.doi_verified"] = True
        name = assay.target.taxon_name
        if name and not assay.target.taxid and not args.skip_taxids:
            # Strip parenthetical commentary before querying ("Ferlavirus (snake...)").
            query = re.sub(r"\(.*?\)", "", name).strip()
            if query not in tax_cache:
                tax_cache[query] = ncbi.taxids_named(query, transport)
            ids = tax_cache[query]
            if len(ids) == 1:
                changes["target.taxid"] = ids[0]
                print(f"TAX {assay.id[:55]:<55} {query!r} -> {ids[0]}")
            else:
                print(f"TAX {assay.id[:55]:<55} {query!r} -> {len(ids)} hits {ids[:5]} (left null)")
        if changes and not args.dry_run:
            # `needs_review` is not touched: consumers derive the citation and taxid
            # flags from the fields (see assaywatch.review). registry.edit keeps the
            # file's comments and key order, which a whole-document re-dump did not.
            registry.edit(path, changes)


if __name__ == "__main__":
    main()
