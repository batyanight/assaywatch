#!/usr/bin/env python3
"""Check a submitted or existing assay entry before it is trusted.

    python scripts/check_submission.py registry/NEW_ASSAY.yaml --email you@example.org
    python scripts/check_submission.py registry/ --offline      # schema and oligo checks only

Everything that went wrong in this registry's first months was a transcription
or provenance error, not a modelling error: a Sarcocystis primer carried one
extra C and failed on 98% of records; two orthobunyavirus primers carried
non-templated cloning tails and matched nothing at all; three taxids pointed at
the wrong organism, one of them to a genus of moths; five DOIs resolved to
other papers. Each was caught eventually by a different ad-hoc script. This
collects those checks in one place and runs them against a candidate entry, so
a submission is checked before it reaches a report rather than after.

The checks, in increasing cost:

  schema      the entry parses, the oligos are IUPAC and the right length
  tails       no restriction site sitting at an oligo's 5' end (a cloning tail
              does not bind the target, so it must be declared in tail_5prime)
  degeneracy  the primer pool size, and a warning when it is so large that an
              in-silico `detect` means little
  citation    the DOI resolves, and its first author and year match the entry
  taxon       the taxid exists and still means what the entry says it does
  amplify     the decisive one: fetch a sample of real records for this target
              and check the oligos actually find their amplicon in them

The `amplify` check is what catches a mistyped oligo. An assay whose primers
match nothing in their own target taxon is far more likely to be wrong than to
be a real discovery, and that is exactly the signature of both bugs above.

Exit status is 0 when nothing failed, 1 when any check failed. Warnings do not
fail the run: a brand-new pathogen with three deposited sequences will warn on
`amplify` and still be a perfectly good submission.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.credentials import ncbi_interval, with_api_key  # noqa: E402
from assaywatch.degeneracy import assay_degeneracy  # noqa: E402
from assaywatch.fasta import read_fasta  # noqa: E402
from assaywatch.match import find_sites  # noqa: E402
from assaywatch.schema import OLIGO_MAX, OLIGO_MIN  # noqa: E402
from assaywatch.score import load_config, screen_record  # noqa: E402
from assaywatch.validate import iter_files, load_assay  # noqa: E402

# Restriction sites common on cloning primers. A match inside the first few
# bases of an oligo is a strong hint that the printed sequence includes a tail
# that never touches the target: the CDV F-gene primers carry SalI and NotI,
# and the orthobunyavirus terminal primers carry KasI/NarI.
RESTRICTION_SITES = {
    "GAATTC": "EcoRI",
    "GGATCC": "BamHI",
    "AAGCTT": "HindIII",
    "GTCGAC": "SalI",
    "GCGGCCGC": "NotI",
    "GGCGCC": "KasI/NarI",
    "CTCGAG": "XhoI",
    "CCATGG": "NcoI",
    "CATATG": "NdeI",
    "TCTAGA": "XbaI",
    "GGTACC": "KpnI",
    "ACTAGT": "SpeI",
    "GAGCTC": "SacI",
}


class Result:
    """Collected findings, so one entry can report every problem at once."""

    def __init__(self) -> None:
        self.lines: list[tuple[str, str, str]] = []

    def add(self, level: str, check: str, message: str) -> None:
        self.lines.append((level, check, message))

    @property
    def failed(self) -> bool:
        return any(level == "FAIL" for level, _, _ in self.lines)

    def report(self, assay_id: str) -> None:
        print(f"\n== {assay_id}")
        for level, check, message in self.lines:
            print(f"  {level:<4} {check:<11} {message}")
        if not self.failed:
            print("  OK   overall     nothing failed")


def fold(text: str) -> str:
    """Lowercase, strip accents, normalise dashes — for comparing author names."""
    stripped = unicodedata.normalize("NFKD", text)
    plain = "".join(c for c in stripped if not unicodedata.combining(c)).lower()
    return re.sub(r"[‐-―−]", "-", plain)


def oligos_of(assay) -> dict[str, object]:
    """The assay's oligos by role, pool members included, skipping absent ones."""
    out: dict[str, object] = {"forward": assay.oligos.forward, "reverse": assay.oligos.reverse}
    if assay.oligos.probe is not None:
        out["probe"] = assay.oligos.probe
    for i, alt in enumerate(assay.oligos.alternates or []):
        out[f"alternate[{i}] {alt.name or ''}".strip()] = alt
    return out


def check_oligos(assay, res: Result) -> None:
    """Length, alphabet and undeclared 5' tails. No network needed."""
    for role, oligo in oligos_of(assay).items():
        seq = oligo.matching_seq
        if not OLIGO_MIN <= len(seq) <= OLIGO_MAX:
            res.add(
                "FAIL", "schema", f"{role} binding part is {len(seq)} nt, outside {OLIGO_MIN}-{OLIGO_MAX}"
            )
        # Only the first 12 bases are examined: a restriction site in the middle
        # of a primer is ordinary sequence, not a tail.
        head = seq[:12]
        if oligo.tail_5prime is None:
            for site, name in RESTRICTION_SITES.items():
                if site in head:
                    res.add(
                        "WARN",
                        "tails",
                        f"{role} starts with a {name} site ({site}) and declares no tail_5prime; "
                        "if those bases do not bind the target they must be declared, or the assay "
                        "will appear to match nothing",
                    )
                    break
    deg = assay_degeneracy(assay)
    tier = deg.tier()
    level = "WARN" if deg.total_fold > 4096 else "OK"
    res.add(level, "degeneracy", f"{deg.total_fold}x pool ({tier})")


def check_citation(assay, res: Result, email: str) -> None:
    """Does the DOI resolve, and to the paper the entry names?"""
    import requests

    doi = assay.citation.doi
    if not doi:
        res.add("WARN", "citation", "no DOI; a primer with no traceable source cannot be checked")
        return
    try:
        r = requests.get(f"https://api.crossref.org/works/{doi}", params={"mailto": email}, timeout=30)
        if r.status_code == 404:
            res.add("FAIL", "citation", f"DOI {doi} does not resolve")
            return
        r.raise_for_status()
        msg = r.json()["message"]
    except Exception as e:  # noqa: BLE001 - a network problem is not the entry's fault
        res.add("WARN", "citation", f"could not reach Crossref ({type(e).__name__})")
        return
    authors = msg.get("author") or []
    family = (authors[0].get("family") or "") if authors else ""
    year = None
    for key in ("published-print", "published-online", "issued", "created"):
        parts = msg.get(key, {}).get("date-parts", [[None]])[0]
        if parts and parts[0]:
            year = parts[0]
            break
    ref = assay.citation.reference or assay.citation.as_written or ""
    named = fold(family) in fold(ref) if (family and ref) else None
    want = assay.citation.design_year
    year_ok = want is None or year is None or abs(year - want) <= 1
    title = (msg.get("title") or [""])[0][:60]
    if named is False or not year_ok:
        res.add(
            "FAIL", "citation", f"DOI resolves to {family} {year}: {title!r}, which does not match the entry"
        )
    else:
        res.add("OK", "citation", f"{family} {year}: {title!r}")


def check_taxon(assay, res: Result, email: str) -> None:
    """Does the taxid exist, and does it still mean what the entry says?"""
    import xml.etree.ElementTree as ET

    import requests

    taxid = assay.target.taxid
    if taxid is None:
        res.add("WARN", "taxon", "no taxid, so this assay is never screened against anything")
        return
    try:
        r = requests.get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
            params=with_api_key({"db": "taxonomy", "id": str(taxid), "email": email, "tool": "assaywatch"}),
            timeout=60,
        )
        r.raise_for_status()
        taxa = ET.fromstring(r.text).findall("Taxon")
    except Exception as e:  # noqa: BLE001
        res.add("WARN", "taxon", f"could not reach NCBI Taxonomy ({type(e).__name__})")
        return
    finally:
        # One request per assay, so checking many submissions in a loop was
        # unpaced: past 3 a second NCBI answers 429, which the handler above
        # reports as a WARN about reachability, not about rate.
        time.sleep(ncbi_interval())
    if not taxa:
        res.add("FAIL", "taxon", f"taxid {taxid} not found in NCBI Taxonomy")
        return
    sci = taxa[0].findtext("ScientificName") or ""
    lineage = taxa[0].findtext("Lineage") or ""
    others = {(el.text or "").strip().lower() for el in taxa[0].findall("OtherNames/*") if el.text}
    want = (assay.target.taxon_name or "").split(" (")[0].strip().lower()
    if not want:
        res.add("WARN", "taxon", f"taxid {taxid} is {sci}, but the entry names no taxon")
    elif want in (sci.lower(), *others) or want in lineage.lower() or sci.lower() in want:
        res.add("OK", "taxon", f"taxid {taxid} = {sci}")
    else:
        res.add(
            "FAIL",
            "taxon",
            f"taxid {taxid} is {sci}, but the entry says {assay.target.taxon_name!r}",
        )


def check_amplifies(assay, res: Result, cfg: dict, retrieved: Path, limit: int) -> None:
    """Do the oligos find their amplicon in real records for this target?

    Uses archives already on disk rather than fetching: a submission is checked
    against the same data the report will use, and the check costs nothing. If
    the target has no archive yet, that is reported rather than guessed at.

    Records are sampled ACROSS the archive, not from the front of it. Taking the
    first N looked fine until it was run over the whole registry, where it failed
    eleven entries that do amplify — the Sarcocystis assay corrected this week
    has 155 detections among thirty thousand records and none in the first 150.
    An archive is ordered by accession, which groups submissions by study, so the
    head of the file is never a representative sample.
    """
    from assaywatch.retrieve import group_slug

    if assay.target.taxid is None:
        return
    group = retrieved / str(assay.target.taxid) / group_slug(assay.target.query)
    archives = sorted(group.glob("*.fasta.gz"))
    if not archives:
        res.add(
            "WARN",
            "amplify",
            f"no archive at {group.relative_to(ROOT) if group.is_relative_to(ROOT) else group}; "
            "run retrieval for this target before trusting the oligos",
        )
        return
    archive = archives[-1]

    # Row count from the metadata beside the archive, so the stride can spread the
    # sample over the whole file. Without it, fall back to taking what comes.
    meta = archive.with_name(archive.name.replace(".fasta.gz", ".meta.tsv.gz"))
    total = 0
    if meta.exists():
        import gzip

        with gzip.open(meta, "rt") as fh:
            total = max(0, sum(1 for _ in fh) - 1)
    step = max(1, total // limit) if total > limit else 1

    calls: dict[str, int] = {}
    best: dict[str, int] = {}
    seen = 0
    for i, (rid, seq) in enumerate(read_fasta(archive)):
        if i % step:  # stride across the archive
            continue
        if len(seq) > 200_000:  # whole genomes are slow and rarely needed here
            continue
        call = screen_record(assay, rid, seq, cfg)
        calls[call.call] = calls.get(call.call, 0) + 1
        # Track each oligo's best match too, so "no amplicon" can be explained.
        for role, oligo in oligos_of(assay).items():
            k = min((s.n_mismatches for s in find_sites(oligo.matching_seq, seq, 8)), default=None)
            if k is not None:
                best[role] = min(best.get(role, 99), k)
        seen += 1
        if seen >= limit:
            break

    amplified = sum(calls.get(k, 0) for k in ("detect", "reduced", "fail"))
    summary = ", ".join(f"{n} {k}" for k, n in sorted(calls.items(), key=lambda kv: -kv[1]))
    if amplified:
        res.add("OK", "amplify", f"{amplified} of {seen} sampled records give an amplicon ({summary})")
        return
    detail = ", ".join(f"{r}: best {k}" for r, k in sorted(best.items())) or "no oligo matched at all"
    # A perfectly matching oligo that never yields an amplicon is a different
    # problem from an oligo that matches nothing: the first points at orientation,
    # amplicon_bp or a sample that happens to miss the locus, the second at a
    # mistyped or tailed sequence. Only the second is worth failing a submission.
    if any(k <= 1 for k in best.values()):
        res.add(
            "WARN",
            "amplify",
            f"no amplicon in {seen} sampled records, but an oligo matches closely ({detail} mismatches). "
            "Check the orientation, amplicon_bp, and whether this target's records carry the locus at all",
        )
    else:
        res.add(
            "FAIL",
            "amplify",
            f"no amplicon in {seen} sampled records of {assay.target.taxon_name}, and no oligo matches "
            f"well ({detail} mismatches). A primer that matches nothing in its own target taxon is "
            "usually mistyped, reverse-complemented, or carries an undeclared 5' tail",
        )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", type=Path, help="a registry YAML file, or a directory of them")
    ap.add_argument("--email", default=None, help="contact address; Crossref and NCBI both ask for one")
    ap.add_argument("--offline", action="store_true", help="skip the DOI and taxonomy checks")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--sample", type=int, default=400, help="records to screen for the amplify check")
    args = ap.parse_args(argv)
    if not args.offline and not args.email:
        ap.error("--email is required unless --offline is given")

    cfg = load_config(args.config)
    failed = 0
    for target in args.paths:
        for path in iter_files(target):
            res = Result()
            try:
                assay = load_assay(path)
            except Exception as e:  # noqa: BLE001 - a malformed entry is the first thing to report
                print(f"\n== {path.name}\n  FAIL schema      {e}")
                failed += 1
                continue
            res.add("OK", "schema", f"parses as {assay.chemistry.value}, status {assay.status.value}")
            check_oligos(assay, res)
            if not args.offline:
                check_citation(assay, res, args.email)
                check_taxon(assay, res, args.email)
            check_amplifies(assay, res, cfg, args.retrieved, args.sample)
            res.report(assay.id)
            failed += res.failed
    print(f"\n{failed} entr{'y' if failed == 1 else 'ies'} with at least one failure")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
