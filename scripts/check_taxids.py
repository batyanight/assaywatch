#!/usr/bin/env python3
"""Check every registry taxid against NCBI Taxonomy. Report only; never edits.

    python scripts/check_taxids.py --registry registry --email you@example.org

resolve_citations.py fills taxids that are missing but trusts the ones already
set. A wrong one is silent and expensive: the first full run fetched 19 moth
COI barcodes as "Batrachochytrium salamandrivorans" (taxid 1430836) and the
Bsal assay was reported as a coverage gap. This asks NCBI for the scientific
name and lineage of each taxid and prints one line per assay:

    OK        the NCBI name equals target.taxon_name
    RENAMED   taxon_name is one of NCBI's other names for the taxid (ICTV's
              binomial renaming made most virus species names synonyms)
    RANK      the names differ but taxon_name appears in the taxid's lineage
              or the other way round (usually a species vs genus choice)
    MISMATCH  neither: the taxid points at something else
    MISSING   no taxid set (resolve_citations.py can fill these)
"""

from __future__ import annotations

import argparse
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.credentials import ncbi_interval, scrub, with_api_key  # noqa: E402

EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch_taxa(taxids: list[int], email: str) -> dict[int, tuple[str, str, set[str]]]:
    """{taxid: (scientific name, lineage, other names)} in batches of 100."""
    out: dict[int, tuple[str, str, set[str]]] = {}
    for i in range(0, len(taxids), 100):
        batch = taxids[i : i + 100]
        try:
            r = requests.get(
                EFETCH,
                params=with_api_key(
                    {"db": "taxonomy", "id": ",".join(map(str, batch)), "email": email, "tool": "assaywatch"}
                ),
                timeout=60,
            )
            r.raise_for_status()
        except requests.RequestException as e:
            # requests puts the full URL in its message, and with a key set the
            # URL carries `api_key=...`. `from None` also drops the chained
            # original, whose traceback would print the same URL.
            raise SystemExit(f"NCBI taxonomy request failed: {scrub(e)}") from None
        for taxon in ET.fromstring(r.text).findall("Taxon"):
            tid = int(taxon.findtext("TaxId"))
            other = {
                (el.text or "").strip().lower()
                for el in taxon.findall("OtherNames/*")
                if el.tag != "Name" and el.text
            }
            other |= {
                (el.findtext("DispName") or "").strip().lower() for el in taxon.findall("OtherNames/Name")
            }
            out[tid] = (taxon.findtext("ScientificName") or "", taxon.findtext("Lineage") or "", other)
            # A merged taxid comes back under its new id; keep the old one too.
            for akas in taxon.findall("AkaTaxIds/TaxId"):
                out[int(akas.text)] = out[tid]
        time.sleep(ncbi_interval())
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, required=True)
    ap.add_argument("--email", required=True)
    ap.add_argument("--quiet", action="store_true", help="only print lines that are not OK")
    args = ap.parse_args()

    entries = []
    for path in sorted(args.registry.glob("*.yaml")):
        target = (yaml.safe_load(path.read_text()) or {}).get("target") or {}
        entries.append((path.stem, target.get("taxid"), (target.get("taxon_name") or "").strip()))

    taxa = fetch_taxa(sorted({t for _, t, _ in entries if t}), args.email)
    bad = 0
    for aid, taxid, name in entries:
        if not taxid:
            status, ncbi = "MISSING", ""
        elif taxid not in taxa:
            status, ncbi = "MISMATCH", "(taxid not found)"
        else:
            sci, lineage, other = taxa[taxid]
            ncbi = sci
            first = name.split(" (")[0].strip().lower()
            if first == sci.lower():
                status = "OK"
            elif first in other:
                status = "RENAMED"
            elif first and (first in lineage.lower() or sci.lower() in first):
                status = "RANK"
            else:
                status = "MISMATCH"
        bad += status == "MISMATCH"
        if status != "OK" or not args.quiet:
            print(f"{status}\t{aid}\t{taxid or '-'}\tregistry: {name}\tncbi: {ncbi}")
    print(f"{bad} mismatched taxids", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
