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
    SCOPED    the name is not the taxid's, but the retrieval `query` pins
              `txid<N>[Organism:exp]` terms inside that taxid and one of them
              IS the organism the name says -- a deliberate narrowing
    MISMATCH  neither: the taxid points at something else
    MISSING   no taxid set (resolve_citations.py can fill these)

SCOPED EXISTS BECAUSE EIGHT ENTRIES WERE READING AS WRONG SINCE 2026-10-04. Seven
Latimer 2010 EEHV entries sit on genus *Proboscivirus* (548689) and the Grizzle 2003
LMBV entry on genus *Ranavirus* (10492), each narrowed to its own species by explicit
organism taxids in the query -- the house pattern for an assay whose species has no
usable retrieval root of its own. The name check could only say the genus is not
called "Elephant endotheliotropic herpesvirus 5", so a deliberate design and a wrong
taxid printed the same line. This reads the query, checks that every organism taxid in
it descends from the entry's own taxid, and asks whether one of them carries the stored
name; only then is the narrowing confirmed. A query that pins a taxon OUTSIDE the root
still reports MISMATCH, because that is the Mycoplasma failure in a second disguise.

And since 2026-10-27, one line per `scope_taxids` entry whose NCBI lineage does NOT
contain the assay's `target.taxid`:

    ESCAPED   a scoped taxon is no longer inside the retrieval root
    EXCL_INSIDE   a taxon the paper claims the assay excludes sits INSIDE the
              assay's own target subtree, so its records leave the drift
              denominator. Legal and sometimes right; never silent
    EXCL_UNKNOWN  a claimed-excluded taxid NCBI does not know
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
import re
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


def narrowed_to(
    name: str,
    root: int,
    pinned: list[int],
    taxa: dict[int, tuple[str, str, set[str], set[int], int]],
) -> str:
    """The pinned organism this entry's `taxon_name` names, or "" if none does.

    Two conditions, both required. Every taxid the query pins must descend from the
    entry's own taxid, or the query is reaching outside the retrieval root and the
    MISMATCH stands. And one of them must carry the stored name: equal to NCBI's
    scientific name, one of its synonyms, or either string inside the other -- the
    last case is what lets "Elephant endotheliotropic herpesvirus 3 and 4" match the
    two taxa it names, since the registry entry covers a pair of species on one
    primer pair and NCBI has no name for the pair.
    """
    if not name or not pinned or any(p not in taxa for p in pinned):
        return ""
    canonical_root = taxa[root][4] if root in taxa else root
    if any(canonical_root not in taxa[p][3] for p in pinned):
        return ""
    for p in pinned:
        sci, _, other, _, _ = taxa[p]
        low = sci.lower()
        if name == low or name in other or low in name or name in low:
            return f"{sci} ({p})"
    return ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, required=True)
    ap.add_argument("--email", required=True)
    ap.add_argument("--quiet", action="store_true", help="only print lines that are not OK")
    args = ap.parse_args()

    entries = []
    scopes: list[tuple[str, int, int]] = []  # (assay, root taxid, scoped taxid)
    excl: list[tuple[str, int, int]] = []  # (assay, root taxid, claimed-excluded taxid)
    for path in sorted(args.registry.glob("*.yaml")):
        target = (yaml.safe_load(path.read_text()) or {}).get("target") or {}
        pinned = [int(m) for m in re.findall(r"txid(\d+)\[Organism", target.get("query") or "")]
        entries.append((path.stem, target.get("taxid"), (target.get("taxon_name") or "").strip(), pinned))
        if target.get("taxid"):
            scopes += [(path.stem, int(target["taxid"]), int(s)) for s in (target.get("scope_taxids") or [])]
            excl += [
                (path.stem, int(target["taxid"]), int(e)) for e in (target.get("exclusivity_taxids") or [])
            ]

    wanted = (
        {t for _, t, _, _ in entries if t}
        | {s for _, _, s in scopes}
        | {e for _, _, e in excl}
        | {p for _, _, _, pinned in entries for p in pinned}
    )
    taxa = fetch_taxa(sorted(wanted), args.email)
    bad = 0
    for aid, taxid, name, pinned in entries:
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
                scoped_to = narrowed_to(first, taxid, pinned, taxa)
                if scoped_to:
                    status, ncbi = "SCOPED", f"{sci} narrowed by query to {scoped_to}"
        bad += status == "MISMATCH"
        if status != "OK" or not args.quiet:
            print(f"{status}\t{aid}\t{taxid or '-'}\tregistry: {name}\tncbi: {ncbi}")

    # A scoped taxon that has left the retrieval root is silently never fetched
    # again. Reported per scope entry, named, so the fix is a registry edit and
    # not a search.
    # Not an error -- esearch resolves a merged id -- but an entry carrying an id
    # NCBI has retired is one taxonomy release away from carrying nothing.
    merged = 0
    for aid, taxid, _, _ in entries:
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
    # An exclusivity taxon is checked and REPORTED, never refused, and the two
    # shapes mean different things. Outside the target's subtree is the ordinary
    # case: a near neighbour the paper says the assay does not amplify. Inside it is
    # legitimate too -- Zhao 2013's generic parapoxvirus assay claims not to detect
    # seal parapoxvirus, which is a species of the genus the assay targets -- but it
    # takes those records out of the assay's own drift denominator, so it is worth
    # naming on its own line rather than passing in silence. The schema cannot do
    # this check: it has no taxonomy.
    inside = unknown = 0
    for aid, root, claimed in excl:
        if claimed not in taxa:
            print(f"EXCL_UNKNOWN\t{aid}\t{claimed}\tclaimed-excluded taxid not found at NCBI")
            unknown += 1
            continue
        sci, _, _, ancestors, _ = taxa[claimed]
        canonical_root = taxa[root][4] if root in taxa else root
        if canonical_root in ancestors:
            root_name = taxa[root][0] if root in taxa else "?"
            print(
                f"EXCL_INSIDE\t{aid}\t{claimed}\t{sci} is INSIDE {root} ({root_name}): its records "
                "leave this assay's own denominator"
            )
            inside += 1
    print(
        f"{bad} mismatched taxids; {merged} merged root taxids; "
        f"{escaped} scoped taxa outside their retrieval root; "
        f"{inside} claimed exclusions inside their own target, {unknown} unknown",
        file=sys.stderr,
    )
    return 1 if bad or escaped or unknown else 0


if __name__ == "__main__":
    sys.exit(main())
