#!/usr/bin/env python3
"""Check every stored oligo against its own paper's text. The literature is the truth.

    python scripts/verify_oligos_against_paper.py --limit 20
    python scripts/verify_oligos_against_paper.py --pdf-dir ~/Downloads
    python scripts/verify_oligos_against_paper.py --tsv results/oligo-verification.tsv
    python scripts/verify_oligos_against_paper.py --assay CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004 -v

Why
---
Most of this registry's entries were seeded from one primer list. That list
was a place to start, not the truth, and it has already been
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
`scripts/import_pmc_fulltext.py` writes.

Where one DOI is held as more than one file, the file NAMED for the DOI (the
filename is the DOI with `/` written as `_`) wins over one that merely prints
it, and between two named files the one that prints MORE oligos wins. No format
is better in itself: a PDF can set its primer table as an image, and PMC text can
come back without its tables or its inline sequences, and which it is varies by
article and cannot be told from the journal. What a file actually yields is the
only comparison worth making. An earlier version preferred text over PDF on the
reasoning that text is the publisher's own characters; that would have let a
table-less text file silently replace a PDF whose table read fine.

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
modified       the oligo records `modified_from`, and the paper prints THAT
               sequence: the stored difference is a recorded modification.
               Counted as agreeing
sibling        would be `near:N`, but the nearest printed run is another oligo of
               the same entry: a lineage variant or alternate measured against
               the primer it was derived from. Not a transcription error, and not
               counted as checkable
no-oligos      the text held for this paper prints fewer than two oligo-like
               runs (MIN_PRINTED_FOR_ABSENT), so it cannot confirm or deny a
               sequence that it does not contain. Not a finding about the
               sequence - a finding about the file. See below
no-full-text   the paper is not open access in PMC and no local PDF matched.
               Needs the PDF - download it and re-run with --pdf-dir
no-doi         nothing to check against

Why `no-oligos` is separate from `absent`
-----------------------------------------
Because conflating them manufactures false findings, and this script found that
out the hard way. `absent` is read as "the paper is in hand and the sequence is
not in it", which is the signal that catches a primer attributed to the wrong
paper. But a text that lost its primer content produces `absent` for every one of
its oligos while saying nothing at all about them.

Three ways that happens. A PDF can set its primer table as an image, so pypdf
extracts a page of prose and no sequences. PubMed Central text can come back
without a table: the avian orthobornavirus paper arrived as 31,202 characters of
readable body text ending its methods in "primers used are presented in" and
nothing, with zero oligo-like runs, and reported all 12 stored oligos `absent`.
And a sequence that sits INLINE can come back empty: the avipox paper's reverse primer
reads "primer 1R ()" in the text, the parenthetical emptied (whether PMC's own XML or the
flattening this text came through lost it is not established; `lost_inline` reads the
empty bracket as the marker either way). Some PMC articles
keep their tables whole (Prepens 2007 and Deckers 2009 both did), so this is not
a rule about PMC; it is why `paper_oligos` is reported on every row.

A would-be `absent` therefore becomes `no-oligos` when the text printed fewer
than MIN_PRINTED_FOR_ABSENT oligos. One run cannot be a primer pair: Quan 2010
came through with only its reverse primer, and three correct stored primers read
`absent` against it. The check still runs first, so a stored sequence that does
occur in the running text is reported `in-text`, not hidden behind `no-oligos`.
The floor is not a guarantee - a paper that prints two unrelated oligos and loses
its table still reads `absent` - and `paper_oligos` is what lets a reader weigh an
`absent` against a paper that printed 2 oligos versus one that printed 40.

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

from assaywatch.credentials import contact_email, ncbi_interval, with_api_key  # noqa: E402
from assaywatch.iupac import reverse_complement  # noqa: E402
from assaywatch.papers import PAPER_SUFFIXES, doi_stem, identity_stem  # noqa: E402

# The text functions live in assaywatch.printed; the `as` form keeps every name
# this module's tests and sibling scripts reach through it.
from assaywatch.printed import GROUPED_RE as GROUPED_RE  # noqa: E402
from assaywatch.printed import LOWER_MIN_LEN as LOWER_MIN_LEN  # noqa: E402
from assaywatch.printed import MIN_PRINTED_FOR_ABSENT as MIN_PRINTED_FOR_ABSENT  # noqa: E402
from assaywatch.printed import NI_POSITION as NI_POSITION  # noqa: E402
from assaywatch.printed import NOISE as NOISE  # noqa: E402
from assaywatch.printed import PRINTED_MIN_LEN as PRINTED_MIN_LEN  # noqa: E402
from assaywatch.printed import align_to_run as align_to_run  # noqa: E402
from assaywatch.printed import compare as check  # noqa: E402
from assaywatch.printed import deinosine as deinosine  # noqa: E402
from assaywatch.printed import edit_distance as edit_distance  # noqa: E402
from assaywatch.printed import file_text as file_text  # noqa: E402
from assaywatch.printed import normalise_notation as normalise_notation  # noqa: E402
from assaywatch.printed import pdf_text as pdf_text  # noqa: E402
from assaywatch.printed import printed_oligos as printed_oligos  # noqa: E402
from assaywatch.printed import printed_runs_for as printed_runs_for  # noqa: E402

# Prefix for the filename-stem keys in `by_doi`; a DOI can never start with it.
STEM_KEY = "stem:"
from assaywatch.validate import iter_files, load_assay  # noqa: E402

CONVERTER = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"


# PAPER_SUFFIXES moved to assaywatch/papers.py on 2026-10-24, so that this reader and
# papers_index agree on which files count as a held paper; the reasoning is there.


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
    claims: dict[str, tuple[bool, int, int]],
    doi: str,
    text: str,
    path: Path,
    n_oligos: int,
    *,
    named: bool,
    offset: int = 0,
) -> None:
    """Let one file take `doi`, if its claim is the stronger one.

    - a file NAMED for the DOI beats one that merely prints it, always, however
      few sequences the named file yields. A filename is a statement that this
      is the paper; a DOI in running text is often a cited reference.
    - between two NAMED claims, more oligos wins. No format is reliably better -
      a PDF can hide its table in an image and PMC full text can lose it - so what
      a file yields is the comparison worth making. Ties keep the incumbent, so
      the result follows `paper_files`' stable order.
    - between two UNNAMED claims, the file that prints the DOI EARLIER wins
      (`offset` is its position in the file's first 4,000 characters). A paper
      prints its own DOI in its header, and a review or erratum that cites the
      paper's DOI does so after its own, so the earlier occurrence is the likelier
      owner. This does not depend on file order, which the first version did: it
      let the first-sorted file keep the DOI, so a review that sorted ahead of the
      paper it reprints took the paper's place. Ties keep the incumbent.

    THE ASYMMETRIES TO KNOW ABOUT: a named file that yields nothing still beats an
    unnamed one that holds the table, which is the price of never trusting a DOI
    printed in running text - if you hold a better copy, name it for the DOI
    (`10.1234_abc.pdf`) and it competes on yield, and `main` reports how many
    files print fewer than two oligos so the case is visible. And "earlier" is a
    heuristic: an erratum that opens "Erratum to doi:A" and then prints its own DOI
    claims A, though it is not A's paper; it does not displace A's own paper, but if
    A's paper is absent it stands in for it.
    """
    current = claims.get(doi)
    if current is not None:
        cur_named, cur_n, cur_offset = current
        if cur_named and (not named or cur_n >= n_oligos):
            return
        if not named and not cur_named and cur_offset <= offset:
            return
    by_doi[doi] = (text, path)
    claims[doi] = (named, n_oligos, offset)


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
    # (named, n_oligos, offset) for whichever file currently holds each DOI, so a later
    # file can be compared against it without re-extracting its sequences.
    claims: dict[str, tuple[bool, int, int]] = {}
    everything: list[tuple[str, Path]] = []
    for path in paper_files(paper_dir):
        # A filename that is the DOI with its slashes swapped for underscores
        # beats anything read out of the text, so it is checked first. This is
        # how the papers/ folder is named. A `.supp` file answers to its
        # article's stem (assaywatch.papers.identity_stem): a supplementary
        # table is evidence about the paper it belongs to, and reading the
        # marker as part of the DOI filed it under one nothing cites.
        stem = identity_stem(path).replace("_", "/")
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
        # The stem itself, for DOIs whose characters the reverse mapping above
        # cannot recover (see assaywatch.papers.doi_stem). Prefixed, so no
        # consumer that walks by_doi can mistake a stem for a DOI - the bare form
        # made extract_candidate_oligos label a file with its own stem. Looked up
        # only via a DOI forward-mapped to the same string, so a stem belonging
        # to no DOI is never reached. `named=True`: a filename IS the identity.
        if identity_stem(path).lower().startswith("10."):
            claim(by_doi, claims, STEM_KEY + identity_stem(path).lower(), text, path, n_oligos, named=True)
        for doi, offset in text_dois(text).items():
            claim(by_doi, claims, doi, text, path, n_oligos, named=False, offset=offset)
    return by_doi, everything


def prints_own_doi(text: str, path: Path) -> bool:
    """True where a file says which paper it is, by filename or by a DOI on page one.

    Such a file is already indexed under that DOI, so it is never a candidate for
    the surname-and-year fallback. The fallback exists for papers that print no
    DOI at all, and a paper that does print one is not evidence about any other.
    """
    named = DOI_IN_TEXT.fullmatch(identity_stem(path).replace("_", "/")) is not None
    return named or DOI_IN_TEXT.search(text[:4000]) is not None


def text_dois(text: str) -> dict[str, int]:
    """{doi: offset of its first occurrence} among the first 4,000 characters of a paper."""
    out: dict[str, int] = {}
    for m in DOI_IN_TEXT.finditer(text[:4000]):
        out.setdefault(m.group(0).rstrip(".,;)").lower(), m.start())
    return out


def local_paper(assay, by_doi, everything) -> tuple[str, Path] | None:
    """The local PDF for this assay, by DOI or by first author plus design year."""
    doi = (assay.citation.doi or "").lower()
    if doi and doi in by_doi:
        return by_doi[doi]
    if doi and STEM_KEY + doi_stem(doi) in by_doi:
        return by_doi[STEM_KEY + doi_stem(doi)]
    ref = (assay.citation.reference or "") or (assay.citation.as_written or "")
    m = re.match(r"\s*([A-Z][A-Za-z'\-]{2,})", ref)
    year = assay.citation.design_year
    if not m or not year:
        return None
    surname = m.group(1)
    for text, path in everything:
        # Without this, any paper that names the author and the year in its first
        # two pages qualifies - an introduction citing "Reid et al. 1999" is
        # enough. That checked the Reid calicivirus, Garner 2006 and Feldman 2006
        # primers against the EEHV and filovirus papers and called them `absent`,
        # and checked Boyle 2004 against Ghosh 2021, which merely cites it.
        if prints_own_doi(text, path):
            continue
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
    q = urllib.parse.urlencode(
        with_api_key({"ids": doi, "format": "json", "tool": "assaywatch", "email": email})
    )
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


def is_probe_slot(slot: str, oligo) -> bool:
    """The `probe` slot, or an alternate declared `orientation: probe`."""
    return slot == "probe" or getattr(oligo, "orientation", None) == "probe"


def name_pattern(name: str) -> re.Pattern | None:
    """A pattern for an oligo's NAME as a paper may print it, or None if too short to search.

    Punctuation in names varies, so the match is loose: `BornaPCA3(+)` in a registry
    may be `BornaPCA3` in print, and `Gd-ITS1-qPCR_F` may carry different dashes.
    Names of 4 or more letters and digits match anywhere, ignoring case. Two and
    three-character names (`1F`, `1R`, `T7`) are real - the avipox assay's primers are
    called that - but short enough to occur inside other words, so they match only
    as a whole token and case-sensitively. A one-character name is not searchable.
    """
    core = re.sub(r"[^A-Za-z0-9]+", "", name)
    if len(core) < 2:
        return None
    loose = r"[^A-Za-z0-9]{0,2}".join(re.escape(c) for c in core)
    if len(core) >= 4:
        return re.compile(loose, re.I)
    return re.compile(rf"(?<![A-Za-z0-9]){loose}(?![A-Za-z0-9])")


def find_name(name: str, text: str) -> list[int]:
    """Where a paper mentions an oligo by name; [] if it does not, or the name is too short."""
    pat = name_pattern(name)
    return [m.start() for m in pat.finditer(text)] if pat else []


EMPTY_BRACKET = re.compile(r"\s*[(\[]\s*[)\]]")


def lost_inline(name: str, text: str) -> bool:
    """Does the text name this oligo and then print an EMPTY bracket where its sequence was?

    `primer 1R ()` is what the avipox paper's reverse primer looks like after PMC's
    extraction: the name survives and the parenthetical holding the sequence is
    emptied. That is a detectable loss marker, and an `absent` verdict beside it is
    a statement about the text, not the primer.
    """
    pat = name_pattern(name)
    if pat is None:
        return False
    return any(EMPTY_BRACKET.match(text, m.end()) for m in pat.finditer(text))


def judge(
    seq: str,
    text: str,
    printed: list[str],
    cap: int,
    name: str | None = None,
    runs: list[str] | None = None,
    siblings: list[tuple[str, str]] | None = None,
) -> tuple[str, str]:
    """(verdict, note) for one oligo against a paper whose text IS held.

    `check` decides what the text says about the sequence. This adds the one
    judgement about the TEXT: whether it printed enough oligos for "absent" to
    mean anything.

    `runs` is the listing to search for THIS oligo, which `printed_runs_for`
    narrows or widens by slot - a probe may be shorter than a primer. The
    `absent` floor below still counts `printed`, every run the text holds,
    because that is a judgement about the file and not about one oligo.

    check() always runs, even for a text that printed nothing, because the stored
    sequence may still occur in the running text and that deserves `in-text`
    rather than being hidden behind `no-oligos`. Only a would-be `absent` is
    reclassified, and it is reclassified as a statement about the FILE: below
    MIN_PRINTED_FOR_ABSENT oligo-like runs the primer table or inline sequences
    were lost, and "not in this paper" cannot be concluded from what is left.
    """
    verdict, note = check(seq, text, printed if runs is None else runs, cap)
    if verdict.startswith("near:") and siblings:
        if hit := nearest_is_sibling(seq, int(verdict[5:]), printed if runs is None else runs, siblings, cap):
            return "sibling", (
                f"the nearest printed run is {hit}, another oligo of this entry, {verdict[5:]} edit(s) "
                "away. A lineage variant or alternate is designed to differ from the primer it was "
                "derived from, so this is not a transcription error; the paper's own table has to "
                "be read by eye for this one"
            )
    if verdict != "absent":
        return verdict, note
    if name and lost_inline(name, text):
        return (
            "no-oligos",
            (
                f"the paper names this oligo ({name}) but the text held prints an EMPTY bracket "
                "where its sequence should be, so the extraction lost it and `absent` would be a "
                "statement about the file, not the primer. Needs the paper's own copy read by eye"
            ),
        )
    if len(printed) < MIN_PRINTED_FOR_ABSENT:
        return (
            "no-oligos",
            (
                f"the text held for this paper prints {len(printed)} oligo-like run(s), "
                "too few for a primer pair, so it cannot confirm or deny this sequence - "
                "the primer table or the inline sequences were lost (an image, or dropped "
                "when the text was extracted). Needs the paper's own table read by eye"
            ),
        )
    return verdict, f"{note}; the paper's text printed {len(printed)} oligo-like run(s)"


def judge_modified(o, verdict: str, note: str, text: str, printed: list[str], cap: int) -> tuple[str, str]:
    """Re-judge a deliberately modified oligo on the sequence the paper should print.

    `modified_from` is the published oligo the stored one was changed from. If the
    paper prints THAT, the entry agrees with its paper about everything it claims,
    and the stored difference is the recorded modification, not an error.
    """
    orig = o.modified_from.replace("I", "N").upper()
    runs = printed_runs_for(is_probe_slot("", o), orig, text, printed)
    v, _ = check(orig, text, runs, cap)
    if v in ("exact", "revcomp"):
        where = f"published in {o.modification_doi}" if o.modification_doi else "no published source"
        return (
            "modified",
            f"the paper prints modified_from {orig} ({v}); the stored form is a recorded modification ({where})",
        )
    return verdict, f"{note}; modified_from {orig} is not printed either ({v})"


def nearest_is_sibling(
    seq: str, d: int, printed: list[str], siblings: list[tuple[str, str]], cap: int
) -> str | None:
    """The name of a same-entry oligo that explains a `near:d`, or None.

    The CDV arctic variants read `near:2` and `near:3` against their own entry's
    Mueller primers, because the nearest printed run to a deliberate variant is
    the primer it was derived from. A sibling explains the near-miss when the
    paper prints it (either strand) and it is no further from `seq` than `d`.
    """
    listed = [deinosine(p) for p in printed]
    for sname, sseq in siblings:
        s = deinosine(sseq)
        rc = reverse_complement(s)
        if s == seq or not any(s in p or rc in p for p in listed):
            continue
        if min(edit_distance(seq, s, cap), edit_distance(seq, rc, cap)) <= d:
            return sname
    return None


def near_listing(near: list[dict]) -> list[str]:
    """Console lines for the `near:N` rows, fewest edits first.

    Sorted by the NUMBER of edits (a text sort puts `near:10` before `near:2`), and the
    whole note is printed: it used to be cut at 70 characters, which removed exactly the
    part that says the paper's run is longer than the stored oligo.
    """
    lines = []
    for r in sorted(near, key=lambda r: (int(r["verdict"][5:]), r["assay_id"], r["oligo_name"])):
        note = r["note"]
        lines.append(f"  {r['assay_id'][:44]:44s} {r['oligo_name'][:16]:16s} {r['verdict']:7s} {note[:70]}")
        if len(note) > 70:
            lines.append(f"  {'':44s} {'':16s} {'':7s} {note[70:]}")
    return lines


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
    ap.add_argument("--email", default=None, help="NCBI asks for one")
    ap.add_argument("--pdf-dir", type=Path, help="also search a folder of papers: .pdf, .xml and .txt files")
    ap.add_argument("--tsv", type=Path)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)
    # Resolved after parsing, so --help works with no address set and the
    # repository carries none. See assaywatch.credentials.contact_email.
    args.email = args.email or contact_email()

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
        # Per FILE: one file can hold several DOIs (its own plus every one it cites in
        # its first 4,000 characters), and counting per DOI reported one thin paper
        # once for each of them.
        holders = {path: text for text, path in by_doi.values()}
        thin = sum(1 for text in holders.values() if len(printed_oligos(text)) < MIN_PRINTED_FOR_ABSENT)
        print(f"indexed {len(everything)} readable papers from {pdf_dir} ({len(holders)} with a DOI)")
        if thin:
            print(
                f"  {thin} print fewer than {MIN_PRINTED_FOR_ABSENT} oligos (a primer table that is an image, or text "
                "whose tables were dropped); their oligos read `no-oligos`. A better copy named "
                "<doi with / as _>.pdf competes for the DOI on what it yields."
            )
        print()

    rows: list[dict] = []
    for n, path in enumerate(paths, 1):
        a = load_assay(path)
        doi = a.citation.doi
        read_from = "predict" if a.source.predict_protocol else ""
        pmcid, text, printed, src = None, None, [], ""
        hit = local_paper(a, by_doi, everything) if everything else None
        if hit:
            text, pdf_path = hit
            src = f"{pdf_path.suffix.lstrip('.').lower()}:{pdf_path.name}"
        if text is None and doi:
            pmcid = pmcid_for(doi, args.email)
            time.sleep(ncbi_interval())
            if pmcid:
                text = paper_text(pmcid)
                time.sleep(ncbi_interval())
                if text:
                    src = f"pmc:{pmcid}"
        if text:
            printed = printed_oligos(text)

        entry_oligos = [
            (slot, o, (o.seq_as_written or o.seq).replace("I", "N").upper()) for slot, o in oligos_of(a)
        ]
        for slot, o, seq in entry_oligos:
            if text is None and not doi:
                verdict, note = "no-doi", "no DOI and no local PDF to check against"
            elif text is None:
                verdict, note = "no-full-text", "not open access in PMC and no local PDF; needs the PDF"
            else:
                runs = printed_runs_for(is_probe_slot(slot, o), seq, text, printed)
                siblings = [(s.name or sl, sq) for sl, s, sq in entry_oligos if sl != slot]
                verdict, note = judge(seq, text, printed, args.cap, o.name, runs=runs, siblings=siblings)
                if o.modified_from and verdict not in ("exact", "revcomp"):
                    verdict, note = judge_modified(o, verdict, note, text, printed, args.cap)
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

    # `near:N` for every N that occurred, not a fixed 1-4: with --cap above 4 the
    # rows for larger N belonged to no bucket and to no denominator, so the
    # percentage was inflated and the counts stopped adding up to the total.
    near_verdicts = sorted(
        {r["verdict"] for r in rows if r["verdict"].startswith("near:")}, key=lambda v: int(v[5:])
    )
    order = [
        "exact",
        "revcomp",
        "modified",
        "in-text",
        *near_verdicts,
        "absent",
        "sibling",
        "no-oligos",
        "no-full-text",
        "no-doi",
    ]
    counts = {k: sum(1 for r in rows if r["verdict"] == k) for k in order}
    print(f"\n{len(rows)} oligos across {len(paths)} entries\n")
    for k in order:
        if counts[k]:
            print(f"  {counts[k]:4d}  {k}")
    # `no-oligos` is not checkable: the file is in hand but too little of it was
    # readable, so counting it would quietly depress the percentage with rows that
    # carry no evidence either way.
    # `sibling` is left out for the same reason: the paper was read, but what it showed
    # is the primer a variant was derived from, which says nothing about the variant.
    checkable = sum(counts[k] for k in order if k not in ("sibling", "no-oligos", "no-full-text", "no-doi"))
    agreeing = counts["exact"] + counts["revcomp"] + counts["modified"]
    if checkable:
        print(
            f"\n  {agreeing} of {checkable} checkable oligos agree with their paper ({100 * agreeing / checkable:.0f}%)"
        )

    near = [r for r in rows if r["verdict"].startswith("near:")]
    if near:
        print("\n### Probable transcription errors, with the paper's own sequence")
        print("\n".join(near_listing(near)))

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
