#!/usr/bin/env python3
"""Check every stored oligo against its own paper's text. The literature is the truth.

    python scripts/verify_oligos_against_paper.py --limit 20
    python scripts/verify_oligos_against_paper.py --pdf-dir ~/Downloads
    python scripts/verify_oligos_against_paper.py --tsv results/oligo-verification.tsv
    python scripts/verify_oligos_against_paper.py --assay CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004 -v

Why
---
138 of this registry's 151 entries were transcribed from one lab spreadsheet.
That spreadsheet was a place to start, not the truth, and it has already been
caught in: a Sarcocystis primer carrying one extra C that then failed on 98% of
records; two orthobunyavirus primers with undeclared cloning tails that matched
nothing; three taxids naming the wrong organism, one of them a genus of moths;
five DOIs resolving to other papers; an amplicon of 500 bp where the paper and
our own measurement both say 531; and an oligo named `Ziao18SF1` for a paper by
Xiao. A sequence is the one thing in an entry that cannot be checked by reading
the entry, so it has to be checked against the source.

Local PDFs
----------
Most of the papers behind this registry are paywalled, so `--pdf-dir` searches a
folder of downloaded PDFs as well. A PDF is matched to an entry by a DOI printed
in its text, or failing that by the cited first author's surname and the design
year both appearing on its first two pages. That second rule is deliberately
conservative: a wrong match would "verify" a sequence against someone else's
paper, which is worse than not checking it, so the surname must appear in the
opening pages rather than anywhere in the references.

What this does
--------------
For each entry with a DOI: resolve the DOI to a PMC id, fetch the open-access
full text, and look for each stored oligo in it. Papers print reverse primers in
either orientation and break sequences with spaces, hyphens and codon groups, so
the comparison is done on a normalised copy of the text and tries both the
sequence and its reverse complement.

When a sequence is NOT found, the script does not stop at "absent". It extracts
every oligo-like run from the paper and reports the closest one by edit
distance. That is the part that earns the runtime: a stored sequence that is one
base from something printed in the paper is a transcription error with the
correction attached, which is exactly the Sarcocystis failure mode.

Verdicts
--------
exact          found verbatim in the full text
revcomp        found as its reverse complement, which is normal for a reverse
               primer and not a defect
near:N         not found, but a printed oligo is N edits away. N=1 or 2 is very
               likely a transcription error and the suggestion is the fix
absent         no printed oligo within the distance cap. Either the sequences
               live in a figure or a supplement this script cannot read, or the
               stored sequence is not this paper's at all
no-full-text   the paper is not open access in PMC and no local PDF matched.
               Needs the PDF - download it and re-run with --pdf-dir
no-doi         nothing to check against

Nothing is written to registry/. A row is an instruction to go and look.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.iupac import reverse_complement  # noqa: E402
from assaywatch.validate import iter_files, load_assay  # noqa: E402

CONVERTER = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
# Papers print sequences in groups - "GCG GCC AAC CAG TTT AAC GCA A" in Grizzle
# 2003, "CTr GCw GCT CTw" in Briese 2007 - so a plain run-of-letters regex finds
# nothing in exactly the papers that matter. This matches letter groups joined by
# spaces, hyphens or apostrophes, and the groups are stitched back together
# afterwards.
GROUPED_RE = re.compile(r"(?:[ACGTURYSWKMBDHVNIacgturyswkmbdhvni]{1,}[\s'\u2019-]{0,2}){2,}")
# Characters a paper uses to make a sequence readable, all of which must go
# before comparison: codon spacing, hyphens, 5'/3' marks, zero-width joiners.
NOISE = re.compile(r"[^ACGTURYSWKMBDHVNI]+")


def printed_oligos(text: str, min_len: int = 14, max_len: int = 60) -> list[str]:
    """Every oligo-like sequence a paper prints, with codon grouping undone.

    Two tests separate sequences from English prose, which is a real problem
    here: every letter of "attach" is an IUPAC code, so prose leaks through a
    naive pattern.

    1. CASE. Papers set sequences in capitals and use lower case only for
       degenerate codes, as Briese 2007 does with `CTr GCw GCT`. At least 60%
       upper case.
    2. BASE COMPOSITION. A real oligo is almost all A, C, G, T and U, with a few
       degenerate codes; English is not. At least 75% of the letters must be
       unambiguous bases.

    The second test was added after running this over the 596-page PREDICT final
    report, where test 1 alone returned 32 "oligos", every one of them an
    all-capitals heading with the spaces lost: FINDINGS IN BATS became
    `INDINGSINBATS`, HIGH RISK became `HIGHRISKWI`, and one was a person's name.
    Those letters are only 23% unambiguous bases against a real oligo's 90-100%,
    so the composition test removes all 32 and keeps every true sequence in the
    papers checked so far.
    """
    out: set[str] = set()
    for m in GROUPED_RE.finditer(text):
        letters = [c for c in m.group(0) if c.isalpha()]
        if not (min_len <= len(letters) <= max_len):
            continue
        if sum(c.isupper() for c in letters) / len(letters) < 0.6:
            continue
        if sum(c.upper() in "ACGTU" for c in letters) / len(letters) < 0.75:
            continue
        out.add("".join(letters).upper())
    return sorted(out)


def pdf_text(path: Path) -> str:
    """All text from a PDF, or "" if it cannot be read. Needs pypdf."""
    try:
        import logging

        import pypdf

        # pypdf warns per font about missing fontTools on scanned or old PDFs;
        # it does not affect the extracted text and it drowns the report.
        logging.getLogger("pypdf").setLevel(logging.ERROR)
        return " ".join((pg.extract_text() or "") for pg in pypdf.PdfReader(str(path)).pages)
    except Exception:  # noqa: BLE001 - a corrupt download must not end the run
        return ""


DOI_IN_TEXT = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")


def index_pdfs(pdf_dir: Path) -> tuple[dict[str, tuple[str, Path]], list[tuple[str, Path]]]:
    """({doi: (text, path)}, [(text, path)]) for every readable PDF in a folder.

    The second list is for the surname-and-year fallback, used only when a
    paper prints no DOI - which is common for older journals.
    """
    by_doi: dict[str, tuple[str, Path]] = {}
    everything: list[tuple[str, Path]] = []
    for path in sorted(pdf_dir.glob("*.pdf")):
        text = pdf_text(path)
        if not text:
            continue
        # A paper describing an assay prints its oligos. Requiring at least two
        # oligo-like runs keeps unrelated PDFs out of the index entirely, which
        # matters when --pdf-dir is pointed at a general Downloads folder that
        # also holds personal documents: those are discarded here rather than
        # indexed, and they can never win the surname-and-year fallback.
        if len(printed_oligos(text)) < 2:
            continue
        everything.append((text, path))
        for d in DOI_IN_TEXT.findall(text[:4000]):
            by_doi.setdefault(d.rstrip(".,;)").lower(), (text, path))
    return by_doi, everything


def local_paper(assay, by_doi, everything) -> tuple[str, Path] | None:
    """The local PDF for this assay, by DOI or by first author plus design year."""
    doi = (assay.citation.doi or "").lower()
    if doi and doi in by_doi:
        return by_doi[doi]
    ref = (assay.citation.reference or "") or (assay.citation.as_written or "")
    m = re.match(r"\s*([A-Z][A-Za-z'\-]{2,})", ref)
    year = assay.citation.design_year
    if not m or not year:
        return None
    surname = m.group(1)
    for text, path in everything:
        head = text[:9000]  # roughly the first two pages: title, authors, methods start
        if surname in head and str(year) in head:
            return text, path
    return None


def get(url: str, timeout: int = 60) -> str | None:
    """One HTTP GET returning text, or None on any failure. Never raises."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:  # noqa: BLE001 - one dead paper must not end the run
        return None


def pmcid_for(doi: str, email: str) -> str | None:
    """PMC id for a DOI, via NCBI's converter then Europe PMC as a fallback."""
    q = urllib.parse.urlencode({"ids": doi, "format": "json", "tool": "assaywatch", "email": email})
    body = get(f"{CONVERTER}?{q}")
    if body:
        try:
            for rec in json.loads(body).get("records", []):
                if rec.get("pmcid"):
                    return rec["pmcid"]
        except json.JSONDecodeError:
            pass
    # Europe PMC indexes some records NCBI's converter misses.
    q = urllib.parse.urlencode({"query": f'DOI:"{doi}"', "format": "json", "resultType": "lite"})
    body = get(f"{EPMC}/search?{q}")
    if body:
        try:
            for r in json.loads(body).get("resultList", {}).get("result", []):
                if r.get("pmcid") and r.get("isOpenAccess") == "Y":
                    return r["pmcid"]
        except json.JSONDecodeError:
            pass
    return None


def paper_text(pmcid: str) -> str | None:
    """Tag-stripped open-access full text, or None if it is not available."""
    xml = get(f"{EPMC}/{pmcid}/fullTextXML", timeout=90)
    if not xml or "<article" not in xml:
        return None
    return re.sub(r"<[^>]+>", " ", xml)


def edit_distance(a: str, b: str, cap: int) -> int:
    """Levenshtein distance, abandoned once it is known to exceed `cap`.

    The cap matters: this runs over every oligo-like run in a paper for every
    stored oligo, and the answer is only interesting when it is small.
    """
    if abs(len(a) - len(b)) > cap:
        return cap + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        if min(cur) > cap:
            return cap + 1
        prev = cur
    return prev[-1]


def check(seq: str, text: str, printed: list[str], cap: int) -> tuple[str, str]:
    """(verdict, note) for one oligo against one paper's text and its oligo runs."""
    flat = NOISE.sub("", text.upper())
    rc = reverse_complement(seq)
    if seq in flat:
        return "exact", ""
    if rc in flat:
        return "revcomp", "found as its reverse complement, which is normal for a reverse primer"
    best, best_d = None, cap + 1
    for p in printed:
        for cand in (seq, rc):
            d = edit_distance(cand, p, cap)
            if d < best_d:
                best, best_d = p, d
    if best is not None and best_d <= cap:
        return f"near:{best_d}", f"paper prints {best} ({best_d} edit(s) away)"
    return "absent", "no printed oligo within the distance cap"


def oligos_of(assay):
    """Every oligo on an assay with the slot it sits in."""
    out = []
    for slot in ("forward", "reverse", "probe"):
        o = getattr(assay.oligos, slot, None)
        if o is not None:
            out.append((slot, o))
    for i, o in enumerate(assay.oligos.alternates or []):
        out.append((f"alt{i}", o))
    return out


COLS = [
    "assay_id",
    "slot",
    "oligo_name",
    "verdict",
    "note",
    "stored_seq",
    "doi",
    "checked_against",
    "read_from",
]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--assay", action="append", help="limit to these ids; repeatable")
    ap.add_argument("--limit", type=int, help="stop after this many entries, for a quick look")
    ap.add_argument("--cap", type=int, default=4, help="largest edit distance worth reporting")
    ap.add_argument("--email", default="nightb02@nyu.edu", help="NCBI asks for one")
    ap.add_argument("--pdf-dir", type=Path, help="also search downloaded PDFs in this folder")
    ap.add_argument("--tsv", type=Path)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    paths = list(iter_files(args.registry))
    if args.assay:
        want = set(args.assay)
        paths = [p for p in paths if p.stem in want]
    if args.limit:
        paths = paths[: args.limit]

    by_doi, everything = ({}, [])
    if args.pdf_dir:
        pdf_dir = args.pdf_dir.expanduser()
        by_doi, everything = index_pdfs(pdf_dir)
        print(f"indexed {len(everything)} readable PDFs from {pdf_dir} ({len(by_doi)} with a DOI)\n")

    rows: list[dict] = []
    for n, path in enumerate(paths, 1):
        a = load_assay(path)
        doi = a.citation.doi
        read_from = (
            "spreadsheet" if a.source.spreadsheet else ("predict" if a.source.predict_protocol else "")
        )
        pmcid, text, printed, src = None, None, [], ""
        hit = local_paper(a, by_doi, everything) if everything else None
        if hit:
            text, pdf_path = hit
            src = f"pdf:{pdf_path.name}"
        if text is None and doi:
            pmcid = pmcid_for(doi, args.email)
            time.sleep(0.34)  # NCBI's 3/sec without an API key
            if pmcid:
                text = paper_text(pmcid)
                time.sleep(0.34)
                if text:
                    src = f"pmc:{pmcid}"
        if text:
            printed = printed_oligos(text)

        for slot, o in oligos_of(a):
            seq = (o.seq_as_written or o.seq).replace("I", "N").upper()
            if text is None and not doi:
                verdict, note = "no-doi", "no DOI and no local PDF to check against"
            elif text is None:
                verdict, note = "no-full-text", "not open access in PMC and no local PDF; needs the PDF"
            else:
                verdict, note = check(seq, text, printed, args.cap)
            rows.append(
                {
                    "assay_id": a.id,
                    "slot": slot,
                    "oligo_name": o.name or "",
                    "verdict": verdict,
                    "note": note,
                    "stored_seq": seq,
                    "doi": doi or "",
                    "checked_against": src or "",
                    "read_from": read_from,
                }
            )
        if args.verbose:
            vs = [r["verdict"] for r in rows if r["assay_id"] == a.id]
            print(f"[{n}/{len(paths)}] {a.id[:56]:56s} {','.join(vs)}", flush=True)
        elif n % 10 == 0:
            print(f"  ...{n}/{len(paths)}", file=sys.stderr, flush=True)

    order = ["exact", "revcomp", "near:1", "near:2", "near:3", "near:4", "absent", "no-full-text", "no-doi"]
    counts = {k: sum(1 for r in rows if r["verdict"] == k) for k in order}
    print(f"\n{len(rows)} oligos across {len(paths)} entries\n")
    for k in order:
        if counts[k]:
            print(f"  {counts[k]:4d}  {k}")
    checkable = sum(counts[k] for k in order if k not in ("no-full-text", "no-doi"))
    agreeing = counts["exact"] + counts["revcomp"]
    if checkable:
        print(
            f"\n  {agreeing} of {checkable} checkable oligos agree with their paper ({100 * agreeing / checkable:.0f}%)"
        )

    near = [r for r in rows if r["verdict"].startswith("near:")]
    if near:
        print("\n### Probable transcription errors, with the paper's own sequence")
        for r in sorted(near, key=lambda r: r["verdict"]):
            print(f"  {r['assay_id'][:44]:44s} {r['oligo_name'][:16]:16s} {r['verdict']:7s} {r['note'][:70]}")

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="") as fh:
            w = csv.DictWriter(fh, COLS, delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {len(rows)} rows to {args.tsv}")

    print(
        "\nNothing in registry/ was changed. Where the paper and the registry disagree, "
        "the paper wins: correct the sequence, and if the stored one was a deliberate lab "
        "modification record it as such rather than as the published assay.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
