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

And since 2026-10-27, one line per `scope_taxids` entry whose NCBI lineage does NOT
contain the assay's `target.taxid`:

    ESCAPED   a scoped taxon is no longer inside the retrieval root
    MERGED    the registry's taxid is an old id NCBI has merged into a new one;
              retrieval still resolves it, and the entry should carry the new id

MERGED IS WHY THE FIRST RUN OF THE CONTAINMENT CHECK REPORTED 4,113 ESCAPES. 11051
(the flavivirus genus) was merged into 3044782 (*Orthoflavivirus*) and the
herpesvirus family root likewise, so every child's ancestor list carries the NEW
id and the registry's old root was never in it. Containment is therefore tested
against the canonical id of the root, and the merge is reported on its own line.

WHY THAT CHECK EXISTS. A genus-rooted retrieval silently stops fetching an organism
the assay names when taxonomy moves it: *Mycoplasmopsis agassizii* and
*Mycoplasmoides testudinis* both left genus *Mycoplasma*, so an assay whose
`target.taxid` is the genus and whose `scope_taxids` name those species keeps
screening a shrinking archive with no error anywhere. The name check above cannot
see it, because the genus still exists and still has its name. This asks NCBI for
each scoped taxon's ancestor list and refuses when the root is not in it.
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


def fetch_taxa(taxids: list[int], email: str) -> dict[int, tuple[str, str, set[str], set[int], int]]:
    """{taxid: (scientific name, lineage, other names, ancestor taxids, canonical id)} in batches of 100.

    The ancestor set comes from `LineageEx`, which lists every ranked ancestor with
    its TaxId; the taxon's own CANONICAL id is included so that a scope equal to
    the root passes trivially. A merged taxid is keyed under the old id too (see
    the AkaTaxIds loop), and the canonical id says which one NCBI now uses.
    """
    out: dict[int, tuple[str, str, set[str], set[int], int]] = {}
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
            ancestors = {int(t.text) for t in taxon.findall("LineageEx/Taxon/TaxId") if t.text} | {tid}
            out[tid] = (
                taxon.findtext("ScientificName") or "",
                taxon.findtext("Lineage") or "",
                other,
                ancestors,
                tid,
            )
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
    scopes: list[tuple[str, int, int]] = []  # (assay, root taxid, scoped taxid)
    for path in sorted(args.registry.glob("*.yaml")):
        target = (yaml.safe_load(path.read_text()) or {}).get("target") or {}
        entries.append((path.stem, target.get("taxid"), (target.get("taxon_name") or "").strip()))
        if target.get("taxid"):
            scopes += [(path.stem, int(target["taxid"]), int(s)) for s in (target.get("scope_taxids") or [])]

    wanted = {t for _, t, _ in entries if t} | {s for _, _, s in scopes}
    taxa = fetch_taxa(sorted(wanted), args.email)
    bad = 0
    for aid, taxid, name in entries:
        if not taxid:
            status, ncbi = "MISSING", ""
        elif taxid not in taxa:
            status, ncbi = "MISMATCH", "(taxid not found)"
        else:
            sci, lineage, other, _, _ = taxa[taxid]
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

    # A scoped taxon that has left the retrieval root is silently never fetched
    # again. Reported per scope entry, named, so the fix is a registry edit and
    # not a search.
    # Not an error -- esearch resolves a merged id -- but an entry carrying an id
    # NCBI has retired is one taxonomy release away from carrying nothing.
    merged = 0
    for aid, taxid, _ in entries:
        if taxid and taxid in taxa and taxa[taxid][4] != taxid:
            print(f"MERGED\t{aid}\t{taxid}\tnow {taxa[taxid][4]} ({taxa[taxid][0]})")
            merged += 1

    escaped = 0
    for aid, root, scoped in scopes:
        if scoped not in taxa:
            print(f"ESCAPED\t{aid}\t{scoped}\tscope taxid not found at NCBI\troot: {root}")
            escaped += 1
            continue
        sci, _, _, ancestors, _ = taxa[scoped]
        canonical_root = taxa[root][4] if root in taxa else root
        if canonical_root not in ancestors:
            root_name = taxa[root][0] if root in taxa else "?"
            print(f"ESCAPED\t{aid}\t{scoped}\t{sci} is no longer inside {root} ({root_name})")
            escaped += 1
    print(
        f"{bad} mismatched taxids; {merged} merged root taxids; {escaped} scoped taxa outside their retrieval root",
        file=sys.stderr,
    )
    return 1 if bad or escaped else 0


if __name__ == "__main__":
    sys.exit(main())
