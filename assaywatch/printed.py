"""What a paper PRINTS, and whether a stored oligo is in it.

Pure text functions, moved here from scripts/verify_oligos_against_paper.py so that
`assaywatch curate` and that script judge an oligo against a paper by the same code.
The script keeps the judgement that sits above these (which file claims a DOI, how a
`modified_from` oligo is read, sibling runs); this module answers the one question
underneath: given a paper's text, where is this sequence, and if nowhere, how far is
the nearest thing it prints?

Verdicts from `check`: `exact`, `revcomp`, `in-text`, `near:<edits>`, `absent`.
"""

from __future__ import annotations

import re
from pathlib import Path

from assaywatch.iupac import reverse_complement
from assaywatch.schema import PROBE_MIN

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


# A position a paper writes as "X or inosine" inside a sequence: `(N/I)`, but also
# `(b/i)`, `(r/i)` and `(y/i)` - Deckers 2009 prints all four in one table. Both
# cases, both bracket styles and both orders occur, so any IUPAC letter on either
# side of the slash is matched provided the other side is I.
_IUPAC_NOT_I = "ACGTURYSWKMBDHVNacgturyswkmbdhvn"


NI_POSITION = re.compile(rf"[(\[]\s*(?:[{_IUPAC_NOT_I}]\s*/\s*[Ii]|[Ii]\s*/\s*[{_IUPAC_NOT_I}])\s*[)\]]")


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


def compare(seq: str, text: str, printed: list[str], cap: int) -> tuple[str, str]:
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
