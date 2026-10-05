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

Local papers
------------
Most of the papers behind this registry are paywalled, so `--pdf-dir` searches a
local folder as well. It reads `.pdf`, and also `.xml` and `.txt` - a
publisher's JATS deposit and the PubMed Central full text that
`scripts/import_pmc_fulltext.py` writes. Where both a PDF and a text file exist
for one DOI the text file wins, because it is the publisher's own characters
rather than a table pypdf had to rebuild from glyph positions; that is how
Ghosh 2021's primer table became readable at all, having been an image in the
PDF.

A file is matched to an entry by a DOI printed in its text, or failing that by
the cited first author's surname and the design year both appearing on its first
two pages. That second rule is deliberately conservative: a wrong match would
"verify" a sequence against someone else's paper, which is worse than not
checking it, so the surname must appear in the opening pages rather than anywhere
in the references.

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
exact          found inside an oligo the paper LISTS
revcomp        listed as its reverse complement, which is normal for a reverse
               primer and not a defect
in-text        the string occurs in the paper but not in any listed oligo. Papers
               print their target gene, so this can mean the sequence was found
               inside that rather than in the primer table - a weaker result
               than `exact` and worth checking by eye
near:N         not found, but a printed oligo is N edits away. N=1 or 2 is very
               likely a transcription error and the suggestion is the fix
absent         the paper prints oligos, but none within the distance cap of this
               one. Either the sequence lives in a figure or supplement this
               script cannot read, or it is not this paper's at all
no-oligos      the text held for this paper prints NO oligo-like run anywhere, so
               it can neither confirm nor deny a sequence. Not a finding about
               the sequence - a finding about the file. See below
no-full-text   the paper is not open access in PMC and no local PDF matched.
               Needs the PDF - download it and re-run with --pdf-dir
no-doi         nothing to check against

Why `no-oligos` is separate from `absent`
-----------------------------------------
Because conflating them manufactures false findings, and this script found that
out the hard way. `absent` is read as "the paper is in hand and the sequence is
not in it", which is the signal that catches a primer attributed to the wrong
paper. But a paper whose primer table never made it into the text produces
`absent` for every one of its oligos while saying nothing at all about them.

Two ways that happens, both common. A PDF can set its primer table as an image,
so pypdf extracts a page of prose and no sequences. And PubMed Central full text
as served through an MCP tool omits `table-wrap` content: on 2026-10-05 the avian
orthobornavirus paper came back as 31,202 characters of readable body text
containing zero oligo-like runs, and reported all 12 of its stored oligos
`absent`. Every one of those verdicts was an artifact of the extraction.

So a file that prints no oligos now yields `no-oligos`, and the `paper_oligos`
column records how many oligo-like runs the matched text held. An `absent`
against a paper that printed 2 oligos deserves far less weight than one against
a paper that printed 40, and the column is what makes that visible.

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
    2. BASE COMPOSITION. A real oligo is mostly A, C, G, T and U, with some
       degenerate codes; English is not. At least 65% of the letters must be one
       of those five bases.

    The second test was added after running this over the 596-page PREDICT final
    report, where test 1 alone returned 32 "oligos", every one of them an
    all-capitals heading with the spaces lost: FINDINGS IN BATS became
    `INDINGSINBATS`, HIGH RISK became `HIGHRISKWI`, and one was a person's name.

    INOSINE IS DELIBERATELY NOT COUNTED as an unambiguous base here, and that
    detail is the whole reason the threshold can be as low as 0.65. `I` is one of
    the commonest letters in English and a rare one in oligos, so counting it
    scores prose almost as high as a real primer: `INDINGS IN BATS IN THAI`
    counts 0.53 with inosine included and 0.26 without, while a real primer
    barely moves. Measured over the 21 papers in hand on 2026-10-05:

        all-caps prose, inosine excluded     0.26
        most degenerate real primer found    0.69   (Astr4380F, Atkins 2009)
        typical degenerate consensus primer  0.71 - 0.85
        a non-degenerate primer              1.00

    The earlier rule - 0.75 with inosine counted - sat above two of the real
    primers in that set and silently dropped them. Astr4380F
    (`GAYTGGRCNCGNTWYGATGGNACIAT`, 0.73 under the old rule) and Astr4722R
    (`ARNCKRTCATCNCCATA`, 0.71) are both printed in Atkins 2009 and neither was
    extracted, so the registry's exact copies of them were reported as the much
    weaker `in-text` rather than `exact`. Highly degenerate consensus primers are
    not an edge case for this registry - pan-viral screening is most of what it
    holds - so the test has to pass them.

    Inosine is still matched by `GROUPED_RE` and still part of the sequence that
    comes back; it is only excluded from this one numerator.
    """
    out: set[str] = set()
    for m in GROUPED_RE.finditer(text):
        letters = [c for c in m.group(0) if c.isalpha()]
        if not (min_len <= len(letters) <= max_len):
            continue
        if sum(c.isupper() for c in letters) / len(letters) < 0.6:
            continue
        if sum(c.upper() in "ACGTU" for c in letters) / len(letters) < 0.65:
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


# Every extension `papers/` may hold. A PDF is what a browser download gives;
# `.xml` is a publisher's own JATS deposit, and `.txt` is what
# `scripts/import_pmc_fulltext.py` writes from PubMed Central's open-access
# full text.
#
# No format is better than the others, which took a wrong turn to learn. The
# first version of this preferred publisher text over a PDF on the reasoning
# that structured text beats a table pypdf has to rebuild from glyph positions.
# That is true of the text a publisher deposits in full, and false of PMC full
# text as served through an MCP tool, which omits `table-wrap` entirely - so
# preferring it would let a table-less text file override a PDF whose primer
# table extracts perfectly well. `index_papers` picks between them on what they
# actually yield instead.
PAPER_SUFFIXES = (".pdf", ".xml", ".txt")


# A position a paper writes as the literal string "(N/I)" - "N or inosine" -
# inside a sequence. Both cases and both bracket styles occur in one table of
# one paper, so all four are matched, as is "(I/N)".
NI_POSITION = re.compile(r"[(\[]\s*(?:[Nn]\s*/\s*[Ii]|[Ii]\s*/\s*[Nn])\s*[)\]]")


def normalise_notation(text: str) -> str:
    """Rewrite in-sequence notation that would otherwise split a printed oligo.

    So far one form, and it is not obscure. The Ehlers-lab pan-herpesvirus
    consensus primers - a mainstay of wildlife herpesvirus screening, and the
    source of several entries here - are printed with their ambiguous positions
    spelled out as `(N/I)`, meaning "N or inosine at this base":

        2744s   TTCAAGGAACTCAGYAARAT(N/I)AAYCC
        2745as  CGTTGTCCTC(N/I)CC(N/I)ARYTG(N/I)CC

    Left alone, the brackets and the slash end the run, so `printed_oligos`
    sees fragments instead of primers - `TTCAAGGAACTCAGYAARAT` and nothing
    else - and every stored oligo past the first bracket reports `absent`.
    Prepens 2007 uses the notation 22 times and produced 4 such false verdicts,
    all 4 of which are exact matches to the registry once it is read.

    The substring search in `check` needs this just as much, and for a nastier
    reason: it strips every non-IUPAC character, and N and I are both IUPAC, so
    `(N/I)` silently collapses to the two bases `NI` and shifts the rest of the
    sequence by one. A wrong answer, not a missing one.

    Replacing it with `N` is what the registry already does - `seq` holds strict
    IUPAC, and `deinosine` flattens inosine to N on both sides of every
    comparison anyway - so nothing is lost by resolving it here.
    """
    return NI_POSITION.sub("N", text)


def file_text(path: Path) -> str:
    """All readable text from a paper file, whatever format it is in.

    XML is reduced to text by dropping tags, the same transformation
    `paper_text` applies to a Europe PMC `fullTextXML` response, so a stored
    `.xml` file and a freshly fetched one are read identically.
    """
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return normalise_notation(pdf_text(path))
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    return normalise_notation(re.sub(r"<[^>]+>", " ", raw) if suffix == ".xml" else raw)


def paper_files(paper_dir: Path) -> list[Path]:
    """Every paper file in a folder, grouped by format and sorted by name.

    The order only has to be stable, not meaningful: `index_papers` chooses
    between two files for one DOI on how many oligos each yields, not on which
    came first. Sorting keeps the result independent of filesystem order.
    """
    return [p for suffix in PAPER_SUFFIXES for p in sorted(paper_dir.glob(f"*{suffix}"))]


DOI_IN_TEXT = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")


def claim(
    by_doi: dict[str, tuple[str, Path]],
    claims: dict[str, tuple[bool, int]],
    doi: str,
    text: str,
    path: Path,
    n_oligos: int,
    *,
    named: bool,
) -> None:
    """Let one file take `doi`, if its claim is the stronger one.

    Ranked on (named, n_oligos), in that order of importance:

    - a file NAMED for the DOI beats one that merely prints it, always, however
      few sequences the named file yields. A filename is a statement that this
      is the paper; a DOI in running text is often a cited reference.
    - between two claims of equal standing, more oligos wins. No format is
      reliably better - a PDF can hide its table in an image and PMC full text
      can lose the table altogether - so what a file yields is the only
      comparison worth making.
    - ties keep the incumbent, so the result follows `paper_files`' stable order.
    """
    current = claims.get(doi)
    if current is not None and current >= (named, n_oligos):
        return
    by_doi[doi] = (text, path)
    claims[doi] = (named, n_oligos)


def index_papers(paper_dir: Path) -> tuple[dict[str, tuple[str, Path]], list[tuple[str, Path]]]:
    """({doi: (text, path)}, [(text, path)]) for every readable paper in a folder.

    A file whose name is the DOI with slashes written as underscores is matched
    on that, which is both exact and free. Otherwise the DOI is read out of the
    first few thousand characters. The second list is for the
    surname-and-year fallback, used only when a paper prints no DOI at all -
    common for older journals.

    WHERE TWO FILES CLAIM ONE DOI, the one printing more oligos wins. That is
    the only comparison that means anything here. A PDF can hide its primer
    table in an image, and PMC full text can lose the whole table to the
    extraction, so neither format is reliably the better evidence - but a file
    that yields 40 sequences is self-evidently more use than one yielding none,
    whatever its extension. Picking by format instead, as this first did, let a
    table-less PMC text file silently override a PDF whose table read fine.
    """
    by_doi: dict[str, tuple[str, Path]] = {}
    # (named, n_oligos) for whichever file currently holds each DOI, so a later
    # file can be compared against it without re-extracting its sequences.
    claims: dict[str, tuple[bool, int]] = {}
    everything: list[tuple[str, Path]] = []
    for path in paper_files(paper_dir):
        # A filename that is the DOI with its slashes swapped for underscores
        # beats anything read out of the text, so it is checked first. This is
        # how the papers/ folder is named.
        stem = path.stem.replace("_", "/")
        named_doi = stem.lower() if DOI_IN_TEXT.fullmatch(stem) else None
        text = file_text(path)
        if not text:
            continue
        # A paper describing an assay prints its oligos. Requiring at least two
        # oligo-like runs keeps unrelated PDFs out of the index entirely, which
        # matters when --pdf-dir is pointed at a general Downloads folder that
        # also holds personal documents: those are discarded here rather than
        # indexed, and they can never win the surname-and-year fallback.
        n_oligos = len(printed_oligos(text))
        if n_oligos < 2 and not named_doi:
            # No oligos and no DOI in the filename: not a paper we can use, and
            # keeping it out means a general folder of personal documents is
            # never indexed. A DOI-named file is kept even without readable
            # sequences, so that "the PDF is here but its table is an image"
            # reads differently from "the PDF is missing".
            continue
        everything.append((text, path))

        # How a file claimed a DOI decides who wins, before how much it yields.
        # A filename IS the DOI; a DOI read out of running text may just be a
        # reference this paper cites. So a named file always beats a text match,
        # even when the named file prints nothing - that is what keeps "the PDF
        # is here and its table is an image" distinct from "the PDF is missing".
        # Only between two files of equal standing does the oligo count decide.
        if named_doi:
            claim(by_doi, claims, named_doi, text, path, n_oligos, named=True)
        for d in DOI_IN_TEXT.findall(text[:4000]):
            claim(by_doi, claims, d.rstrip(".,;)").lower(), text, path, n_oligos, named=False)
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
    return normalise_notation(re.sub(r"<[^>]+>", " ", xml))


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


def deinosine(s: str) -> str:
    """Inosine to N, so both sides of a comparison use the same alphabet.

    The registry keeps strict IUPAC in `seq` and the printed form in
    `seq_as_written`, so an inosine is stored as N. Papers print `I`. Comparing
    one against the other charges an edit per inosine position, which is how the
    first run of this script reported the two PREDICT bocavirus primers as
    `near:1` when in fact they match their paper exactly. Both sides get
    flattened to N here instead.
    """
    return s.replace("I", "N")


def check(seq: str, text: str, printed: list[str], cap: int) -> tuple[str, str]:
    """(verdict, note) for one oligo against one paper's text and its oligo runs."""
    rc = reverse_complement(seq)
    # Prefer a match inside a LISTED oligo over a match anywhere in the paper.
    # Papers print their target gene, so a bare substring search says only "this
    # string occurs in this paper". Checking the Yersinia entry found its stored
    # forward primer inside the printed ystA gene sequence, four bases offset
    # from the primer the table actually lists - which a plain substring search
    # scored as a perfect match. `printed` holds standalone oligo-like runs
    # capped at 60 bases, so a gene sequence cannot get in, while a table-mangled
    # primer with a neighbouring cell glued on still contains its own sequence.
    listed = [deinosine(p) for p in printed]
    if any(seq in p for p in listed):
        return "exact", ""
    if any(rc in p for p in listed):
        return "revcomp", "listed as its reverse complement, which is normal for a reverse primer"
    flat = deinosine(NOISE.sub("", text.upper()))
    if seq in flat or rc in flat:
        return "in-text", (
            "occurs in the paper but not in any listed oligo - it may be inside the printed target "
            "sequence rather than being a primer the paper lists. Check the primer table by eye"
        )
    # PDF table extraction glues neighbouring cells onto a sequence: this paper's
    # influenza primer came out as AGATGAGTCTTCTAACCGAGGTCG + "M" from the next
    # column, and its probe arrived wrapped in FAM, TAMRA and AVIAN. Comparing a
    # stored oligo against the whole glued string inflates the distance and
    # reports a candidate that is not what the paper printed. So when a printed
    # candidate is longer than the stored oligo, every window of the stored
    # length is tried and the best window is what gets reported.
    best, best_d = None, cap + 1
    for p in printed:
        pd = deinosine(p)
        for cand in (seq, rc):
            windows = (
                [pd]
                if len(pd) <= len(cand)
                else [pd[i : i + len(cand)] for i in range(len(pd) - len(cand) + 1)]
            )
            for w in windows:
                d = edit_distance(cand, w, cap)
                if d < best_d:
                    best, best_d = w, d
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
    "paper_oligos",
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
        by_doi, everything = index_papers(pdf_dir)
        print(f"indexed {len(everything)} readable papers from {pdf_dir} ({len(by_doi)} with a DOI)\n")

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
            elif not printed:
                # The text is here and prints no sequences at all. Saying
                # "absent" would assert something about the oligo; the only
                # honest statement is about the file.
                verdict, note = (
                    "no-oligos",
                    (
                        "the text held for this paper prints no oligo-like run anywhere, so it cannot "
                        "confirm or deny this sequence - the primer table is an image, or was dropped "
                        "when the full text was extracted. Needs the table read by eye"
                    ),
                )
            else:
                verdict, note = check(seq, text, printed, args.cap)
                if verdict == "absent":
                    note = f"{note}; the paper's text printed {len(printed)} oligo-like run(s)"
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
                    "paper_oligos": len(printed) if text else "",
                    "read_from": read_from,
                }
            )
        if args.verbose:
            vs = [r["verdict"] for r in rows if r["assay_id"] == a.id]
            print(f"[{n}/{len(paths)}] {a.id[:56]:56s} {','.join(vs)}", flush=True)
        elif n % 10 == 0:
            print(f"  ...{n}/{len(paths)}", file=sys.stderr, flush=True)

    order = [
        "exact",
        "revcomp",
        "in-text",
        "near:1",
        "near:2",
        "near:3",
        "near:4",
        "absent",
        "no-oligos",
        "no-full-text",
        "no-doi",
    ]
    counts = {k: sum(1 for r in rows if r["verdict"] == k) for k in order}
    print(f"\n{len(rows)} oligos across {len(paths)} entries\n")
    for k in order:
        if counts[k]:
            print(f"  {counts[k]:4d}  {k}")
    # `no-oligos` is not checkable: the file is in hand but prints no sequences,
    # so counting it would quietly depress the percentage with rows that carry
    # no evidence either way.
    checkable = sum(counts[k] for k in order if k not in ("no-oligos", "no-full-text", "no-doi"))
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
