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
from assaywatch.papers import doi_stem  # noqa: E402

# Prefix for the filename-stem keys in `by_doi`; a DOI can never start with it.
STEM_KEY = "stem:"
from assaywatch.schema import PROBE_MIN  # noqa: E402
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


# The shortest run `printed_oligos` harvests for a PRIMER. A probe may be shorter (see
# schema.PROBE_MIN), so `printed_runs_for` lowers the floor for probes alone.
PRINTED_MIN_LEN = 14

# `absent` says "the paper is in hand and this sequence is not in it", which is
# the signal that catches a primer attributed to the wrong paper. It is only fair
# to say that of a paper that prints enough oligos to be a methods paper at all.
# One oligo-like run cannot be a primer pair, and a text that holds one is a text
# that lost the rest - Quan 2010 came through PMC with only its reverse primer, and
# three perfectly good stored primers read `absent` against it. So below this many
# runs a would-be `absent` becomes `no-oligos`. It is a floor, not a guarantee: a
# paper that prints two unrelated oligos and loses its table still reads `absent`,
# which is why the verdict row carries `paper_oligos`.
MIN_PRINTED_FOR_ABSENT = 2


LOWER_MIN_LEN = 18  # a lowercase run shorter than this is not evidence


def printed_oligos(text: str, min_len: int = PRINTED_MIN_LEN, max_len: int = 60) -> list[str]:
    """Every oligo-like sequence a paper prints, with codon grouping undone.

    Two tests separate sequences from English prose, which is a real problem
    here: every letter of "attach" is an IUPAC code, so prose leaks through a
    naive pattern.

    1. CASE. Papers set sequences in capitals and use lower case only for
       degenerate codes, as Briese 2007 does with `CTr GCw GCT`. At least 60%
       upper case.
    2. BASE COMPOSITION. A real oligo is mostly A, C, G, T and U, with some
       degenerate codes; English is not. A candidate passes if EITHER

         (a) at least 65% of its letters are A, C, G, T or U, inosine NOT
             counted, or
         (b) at least 75% are A, C, G, T, U or I, inosine counted.

    The composition test was added after running this over the 596-page PREDICT
    final report, where the case test alone returned 32 "oligos", every one of
    them an all-capitals heading with the spaces lost: FINDINGS IN BATS became
    `INDINGSINBATS`, HIGH RISK became `HIGHRISKWI`, and one was a person's name.

    WHY TWO RULES. Rule (b) is the original, and it was too strict for heavily
    degenerate primers: Astr4380F (`GAYTGGRCNCGNTWYGATGGNACIAT`) scores 0.73 and
    Astr4722R (`ARNCKRTCATCNCCATA`) 0.71 under it, so neither was extracted from
    Atkins 2009 and the registry's exact copies were reported as the much weaker
    `in-text`. Rule (a) rescues them: inosine is among the commonest letters in
    English and a rare one in oligos, so leaving it out is what gives prose clear
    air (`INDINGS IN BATS IN THAI` is 0.53 with inosine counted and 0.26 without)
    while a degenerate primer, which is mostly real bases, barely moves.

    But (a) alone loses the opposite kind of primer. Replacing (b) with (a) was
    tried first and regressed every inosine-RICH primer: Alpha1R
    (`KYTCYTCIGTRTGYTTIGTICCIGG`), Alpha2R, 222/RVS, NPhlebo1NEG and NPhlebo2POS
    score 0.57-0.64 without inosine and 0.76-0.85 with it, so (a) drops them and
    (b) keeps them. Taking either rule is therefore a superset of the original and
    of the first replacement, so nothing either one extracted can be lost, and the
    only new false positives are those the original already admitted.

    Calibrated against all 357 distinct registry oligos as written (14-60 nt),
    each placed in a one-line methods sentence, rather than only the papers in
    hand: the original rule misses 36, the first replacement 18, this one 13. The
    13 are the most heavily degenerate: between 50% and 65% unambiguous bases (the
    lowest, `GVKWRWANTHDANGTANGGRTTDTYNCC`, is 50%; `ACHBYMTCVTGGTTCMWDCAGG` is 64%,
    only just under the 65% line) and cannot be told from capitalised prose by
    composition, so a paper that prints one is confirmed only by the weaker `in-text`
    search.

    Inosine is matched by `GROUPED_RE` and stays part of the sequence that comes
    back; it is only treated differently in the composition arithmetic.
    """
    out: set[str] = set()
    for m in GROUPED_RE.finditer(text):
        letters = [c for c in m.group(0) if c.isalpha()]
        n = len(letters)
        if not (min_len <= n <= max_len):
            continue
        bases = sum(c.upper() in "ACGTU" for c in letters)
        with_inosine = bases + sum(c.upper() == "I" for c in letters)
        if sum(c.isupper() for c in letters) / n < 0.6:
            # LOWER CASE. The case rule above assumes papers set sequences in
            # capitals, and most do, but Rahn et al. 1992 prints both its invA
            # primers entirely in lower case (`gtgaaattatcgccacgttcgggcaa`), so
            # the reader returned ZERO oligos from a text holding both of them
            # and the entry read `no-oligos`. Measured over papers/ on
            # 2026-10-20: 3 papers and 6 registry oligos are invisible this way.
            #
            # Such a run is admitted only on a much stronger composition test
            # than the capitalised one, because lower case is where the prose is:
            # at least LOWER_MIN_LEN letters and EVERY letter an unambiguous
            # base. An English word of 18+ letters drawn only from a, c, g, t
            # and u does not occur, where capitalised headings with their spaces
            # lost (`INDINGSINBATS`) very much do.
            #
            # Why no degenerate codes are allowed here, where the capitalised
            # rule tolerates 35%: a 90% threshold was tried first and admitted
            # five false oligos from Deckers 2009, whose primer table flattens to
            # `gB-1 a c t g g t g g t t t g g UL33-1/2 g a t a c a t a a t g g t
            # a c a` + `gB-2 ...`, so the NEXT row's primer name glues onto the
            # end of the previous sequence and `gatacataatggtaca` came back as
            # `GATACATAATGGTACAGB`. Every degenerate letter is also a common
            # English letter, so in lower case they are where the glue and the
            # prose are. The cost is that a genuinely degenerate primer printed
            # in lower case still reads only `in-text`.
            if n < LOWER_MIN_LEN or bases < n:
                continue
        elif bases / n < 0.65 and with_inosine / n < 0.75:
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
# first version preferred publisher text over a PDF on the reasoning that
# structured text beats a table pypdf has to rebuild from glyph positions. That is
# true of the text a publisher deposits in full, and not of PMC full text as served
# through an MCP tool, which comes back flattened and often (not always: Prepens
# 2007 and Deckers 2009 kept their primer tables) without its tables - so preferring
# it would let a table-less text file override a PDF whose primer table extracts
# perfectly well. `index_papers` picks between them on what they actually yield
# instead.
PAPER_SUFFIXES = (".pdf", ".xml", ".txt")


# A position a paper writes as "X or inosine" inside a sequence: `(N/I)`, but also
# `(b/i)`, `(r/i)` and `(y/i)` - Deckers 2009 prints all four in one table. Both
# cases, both bracket styles and both orders occur, so any IUPAC letter on either
# side of the slash is matched provided the other side is I.
_IUPAC_NOT_I = "ACGTURYSWKMBDHVNacgturyswkmbdhvn"
NI_POSITION = re.compile(rf"[(\[]\s*(?:[{_IUPAC_NOT_I}]\s*/\s*[Ii]|[Ii]\s*/\s*[{_IUPAC_NOT_I}])\s*[)\]]")


def normalise_notation(text: str) -> str:
    """Rewrite in-sequence notation that would otherwise split a printed oligo.

    One family of forms, and it is not obscure. The Ehlers-lab pan-herpesvirus
    consensus primers - a mainstay of wildlife herpesvirus screening, and the
    source of several entries here - are printed with their ambiguous positions
    spelled out as `(N/I)`, meaning "N or inosine at this base", and other positions
    as `(b/i)`, `(r/i)` or `(y/i)`, "B, R or Y, or inosine":

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

    The same holds for any other base before the slash - `(b/i)`, `(r/i)` - as
    Deckers 2009 prints them: the paper offers that base or inosine, and the
    registry stores such a position as N.

    Replacing it with `N` is what the registry already does - `seq` holds strict
    IUPAC, and `deinosine` flattens inosine to N on both sides of every
    comparison anyway - and it is the faithful reading of "B or inosine": inosine
    pairs with any base, so the union of the two is N. So nothing is lost by
    resolving every form to N here.
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
        # The stem itself, for DOIs whose characters the reverse mapping above
        # cannot recover (see assaywatch.papers.doi_stem). Prefixed, so no
        # consumer that walks by_doi can mistake a stem for a DOI - the bare form
        # made extract_candidate_oligos label a file with its own stem. Looked up
        # only via a DOI forward-mapped to the same string, so a stem belonging
        # to no DOI is never reached. `named=True`: a filename IS the identity.
        if path.stem.lower().startswith("10."):
            claim(by_doi, claims, STEM_KEY + path.stem.lower(), text, path, n_oligos, named=True)
        for doi, offset in text_dois(text).items():
            claim(by_doi, claims, doi, text, path, n_oligos, named=False, offset=offset)
    return by_doi, everything


def prints_own_doi(text: str, path: Path) -> bool:
    """True where a file says which paper it is, by filename or by a DOI on page one.

    Such a file is already indexed under that DOI, so it is never a candidate for
    the surname-and-year fallback. The fallback exists for papers that print no
    DOI at all, and a paper that does print one is not evidence about any other.
    """
    named = DOI_IN_TEXT.fullmatch(path.stem.replace("_", "/")) is not None
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


def printed_runs_for(is_probe: bool, seq: str, text: str, printed: list[str]) -> list[str]:
    """The printed runs to compare ONE stored oligo against.

    Probes are judged separately from primers. Published MGB probes run 13-14 nt,
    below the 14-nt floor the harvest uses so that short English runs stay out, so
    a probe printed alone in a primer table was never extracted and could not
    reach `exact`; it fell to `in-text`, "check by eye", however clearly the paper
    printed it. A short probe is therefore harvested at the probe floor. A primer
    never is: the lower floor admits more prose-shaped runs, and a primer is not
    allowed to be that short anyway.
    """
    if is_probe and len(seq) < PRINTED_MIN_LEN:
        return printed_oligos(text, min_len=PROBE_MIN)
    return printed


def is_probe_slot(slot: str, oligo) -> bool:
    """The `probe` slot, or an alternate declared `orientation: probe`."""
    return slot == "probe" or getattr(oligo, "orientation", None) == "probe"


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
    best, best_printed, best_cand, best_d = None, None, None, cap + 1
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
                    best, best_printed, best_cand, best_d = w, pd, cand, d
    if best is not None and best_d <= cap:
        if len(best_printed) > len(best):
            # The paper's run is LONGER than the stored oligo, and a bare window
            # would present a truncated fragment as "the paper's own sequence" -
            # Quan 2010 prints a 33-mer, the stored 30-mer lacks three bases, and
            # the window alone dropped the last three of the paper's. But a longer
            # run is just as often a SHORT oligo with table text glued on (a primer
            # name's last letters, a column label), and quoting it whole would invite
            # extending the stored sequence by those letters. So the note aligns the
            # stored sequence to the run end to end and says where the extra bases
            # are: at the ends they may be glue, inside the run they are real.
            edits, five, three, inside = align_to_run(best_cand, best_printed)
            where = []
            if five:
                where.append(f"{five} extra base(s) at the run's 5' end")
            if three:
                where.append(f"{three} extra base(s) at its 3' end")
            if inside:
                where.append(f"{inside} base(s) inside it that the stored sequence lacks")
            return (
                f"near:{best_d}",
                f"paper prints {best_printed} ({len(best_printed)} nt; the stored oligo is {len(seq)}). "
                f"Aligned end to end the stored sequence is {edits} edit(s) from it"
                + (f", with {'; '.join(where)}" if where else "")
                + ". Bases at the ends of a printed run can be table text glued on by the extraction, "
                "so only a difference inside the run is evidence the stored sequence is wrong",
            )
        return f"near:{best_d}", f"paper prints {best} ({best_d} edit(s) away)"
    return "absent", "no printed oligo within the distance cap"


def align_to_run(cand: str, run: str) -> tuple[int, int, int, int]:
    """Align `cand` end to end against `run`, whose two ends are free.

    Returns (edits, bases of `run` before the aligned stretch, bases after it,
    bases of `run` inside the stretch that `cand` has no partner for). Unit costs,
    by plain character equality, like `edit_distance`. Lengths here are at most
    60, so the table is small.
    """
    n, m = len(cand), len(run)
    inf = n + m + 1
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1):
        dp[0][j] = 0  # the aligned stretch may start anywhere in the run
    for i in range(1, n + 1):
        dp[i][0] = i
        for j in range(1, m + 1):
            dp[i][j] = min(
                dp[i - 1][j - 1] + (cand[i - 1] != run[j - 1]),
                dp[i - 1][j] + 1,  # a base of cand with no partner in the run
                dp[i][j - 1] + 1,  # a base of the run with no partner in cand
            )
    end = min(range(m + 1), key=lambda j: (dp[n][j], -j))
    i, j, inside = n, end, 0
    while i > 0:
        if j > 0 and dp[i][j] == dp[i - 1][j - 1] + (cand[i - 1] != run[j - 1]):
            i, j = i - 1, j - 1
        elif dp[i][j] == dp[i - 1][j] + 1:
            i -= 1
        else:
            inside += 1
            j -= 1
    return dp[n][end], j, m - end, inside


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
        read_from = (
            "spreadsheet" if a.source.spreadsheet else ("predict" if a.source.predict_protocol else "")
        )
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

        for slot, o in oligos_of(a):
            seq = (o.seq_as_written or o.seq).replace("I", "N").upper()
            if text is None and not doi:
                verdict, note = "no-doi", "no DOI and no local PDF to check against"
            elif text is None:
                verdict, note = "no-full-text", "not open access in PMC and no local PDF; needs the PDF"
            else:
                runs = printed_runs_for(is_probe_slot(slot, o), seq, text, printed)
                verdict, note = judge(seq, text, printed, args.cap, o.name, runs=runs)
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
    order = ["exact", "revcomp", "in-text", *near_verdicts, "absent", "no-oligos", "no-full-text", "no-doi"]
    counts = {k: sum(1 for r in rows if r["verdict"] == k) for k in order}
    print(f"\n{len(rows)} oligos across {len(paths)} entries\n")
    for k in order:
        if counts[k]:
            print(f"  {counts[k]:4d}  {k}")
    # `no-oligos` is not checkable: the file is in hand but too little of it was
    # readable, so counting it would quietly depress the percentage with rows that
    # carry no evidence either way.
    checkable = sum(counts[k] for k in order if k not in ("no-oligos", "no-full-text", "no-doi"))
    agreeing = counts["exact"] + counts["revcomp"]
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
