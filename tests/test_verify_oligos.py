"""Tests for the paper-vs-registry oligo check.

The registry's sequences must match the literature, not the lab spreadsheet they
were transcribed from, so this script is the thing that makes that checkable.
Its one real difficulty is telling a printed sequence apart from English text:
every letter of "attach" is an IUPAC code.
"""

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("vo", ROOT / "scripts" / "verify_oligos_against_paper.py")
vo = importlib.util.module_from_spec(_spec)
sys.modules["vo"] = vo
_spec.loader.exec_module(vo)


def test_finds_sequences_printed_in_codon_groups():
    """Grizzle 2003 and Briese 2007 both group their sequences; a plain
    run-of-letters pattern finds nothing in exactly the papers that matter."""
    grizzle = "The forward primer (LMBV288F) sequence was 5'-GCG GCC AAC CAG TTT AAC GCA A-3'"
    assert "GCGGCCAACCAGTTTAACGCAA" in vo.printed_oligos(grizzle)
    # Briese prints degenerate codes in lower case inside an upper-case sequence.
    briese = "BUNS-5-U-6 5'-CGGCGCC AGT AGT GTA CTC CAC 947"
    assert "CGGCGCCAGTAGTGTACTCCAC" in vo.printed_oligos(briese)
    mixed = "M940C-R 5'-CTr GCw GCT CTw AGr CTT TTr TAm CC 936"
    assert "CTRGCWGCTCTWAGRCTTTTRTAMCC" in vo.printed_oligos(mixed)


def test_finds_heavily_degenerate_consensus_primers():
    """Regression for the 0.75-with-inosine composition rule, which dropped them.

    Atkins 2009 prints both of these. Under the old rule they scored 0.73 and
    0.71 against a 0.75 threshold, so neither was extracted, and the registry's
    exact copies of them came back as `in-text` - the verdict that means "this
    string is somewhere in the paper", when in fact the paper lists them as its
    primers. A pan-viral consensus primer is degenerate by design, and this
    registry is mostly pan-viral screening, so these cannot be edge cases.
    """
    atkins = (
        "forward primer Astr4380F (5'-GAYTGGRCNCGNTWYGATGGNACIAT-3') and reverse "
        "primer Astr4722R (5'-ARNCKRTCATCNCCATA-3')"
    )
    printed = vo.printed_oligos(atkins)
    assert "GAYTGGRCNCGNTWYGATGGNACIAT" in printed, printed
    assert "ARNCKRTCATCNCCATA" in printed, printed
    # And the registry's stored form, with N where the paper prints inosine,
    # must now read as an exact match rather than as in-text.
    verdict, _ = vo.check("GAYTGGRCNCGNTWYGATGGNACNAT", atkins, printed, 4)
    assert verdict == "exact", verdict


def test_inosine_is_not_counted_as_an_unambiguous_base():
    """The reason the threshold can be 0.65: `I` is common in English, rare in
    oligos, so counting it scores all-caps prose nearly as high as a primer.

    `INDINGS IN BATS IN THAI` is 0.53 unambiguous with inosine counted and 0.26
    without, which is what puts clear air between it and a real primer.
    """
    assert vo.printed_oligos("FINDINGS IN BATS IN THAILAND") == []
    # An inosine-carrying primer still survives, because inosine sits at a few
    # wobble positions rather than throughout.
    assert "GGNAAYCCMTCWGGICA" in vo.printed_oligos("primer 5'-GGNAAYCCMTCWGGICA-3'")


def test_rejects_all_caps_headings():
    """Regression for the PREDICT final report, where the case test alone
    returned 32 'oligos', all of them headings with the spaces lost.

    These survive a case test because English words are built from IUPAC
    letters; they fail the base-composition test, being about 23% unambiguous
    bases against a real oligo's 90-100%.
    """
    for heading in (
        "FINDINGS IN BATS IN THAILAND",
        "HIGH RISK INTERFACES WITH WILDLIFE",
        "VIRUS DETECTION IN ANIMALS AND HUMANS",
    ):
        assert vo.printed_oligos(heading) == [], heading


def test_lower_case_prose_is_not_an_oligo():
    assert vo.printed_oligos("we attach a cat and a tag to that sample") == []


def test_edit_distance_abandons_past_the_cap():
    """The near-match search runs every stored oligo against every printed one,
    so the distance only has to be exact while it is small."""
    assert vo.edit_distance("ACGTACGTACGT", "ACGTACGTACGT", 4) == 0
    assert vo.edit_distance("ACGTACGTACGT", "ACGTACGTACGA", 4) == 1
    assert vo.edit_distance("ACGTACGTACGT", "ACGTACGTACG", 4) == 1  # a dropped base
    assert vo.edit_distance("ACGT", "TTTTTTTTTTTT", 4) > 4


def test_an_extra_base_reads_as_a_one_edit_near_match():
    """The Sarcocystis failure mode: one extra C, which then matched almost
    nothing. A verdict of near:1 carries its own correction."""
    paper = "the primer P-ITSF 5'-GGATCACTCGGTTCGAGGTG-3' was used"
    stored = "GGATCACTCCGGTTCGAGGTG"  # one extra C
    verdict, note = vo.check(stored, paper, vo.printed_oligos(paper), 4)
    assert verdict == "near:1", (verdict, note)
    assert "GGATCACTCGGTTCGAGGTG" in note


def test_inosine_matches_the_registry_n():
    """Papers print inosine as I; the registry stores it as N in `seq`.

    The first full run flagged both PREDICT bocavirus primers as near:1 purely
    because of this, so both sides of the comparison must use one alphabet.
    """
    paper = "PANBOV-F1 5'-TAATGCAYCARGAYTGGGTIGANCC-3'"
    stored = "TAATGCAYCARGAYTGGGTNGANCC"  # the registry's N where the paper prints I
    verdict, _ = vo.check(stored, paper, vo.printed_oligos(paper), 4)
    assert verdict == "exact", verdict


def test_a_match_inside_the_printed_gene_is_not_a_primer_match():
    """Papers print their target sequence, so "appears in the paper" is weaker
    than "appears in the primer table".

    Ibrahim 1992 prints the ystA gene, and the registry's stored forward primer
    sits inside it four bases offset from the primer the table actually lists.
    A plain substring search called that a perfect match.
    """
    paper = (
        "TABLE 3 yst-Pr2a 5'-AATGCTGTCTTCATTTGGAGC-3' "
        "FIG 2 ATGAAAAAGATAGTTTTTGTTCTTGTGTTAATGCTGTCTTCATTTGGAGCATTCGGCCAAGAAACAGTTTCAGGG"
    )
    printed = vo.printed_oligos(paper)
    listed, _ = vo.check("AATGCTGTCTTCATTTGGAGC", paper, printed, 4)
    assert listed == "exact", listed
    shifted, note = vo.check("CTGTCTTCATTTGGAGCATTC", paper, printed, 4)
    assert shifted == "in-text", (shifted, note)


def test_a_paper_printing_no_oligos_is_not_evidence_of_absence():
    """`no-oligos` has to be its own verdict, or the tool manufactures findings.

    `absent` is read as "the paper is in hand and this sequence is not in it",
    which is the signal that catches a primer attributed to the wrong paper. A
    paper whose primer table never reached the text - set as an image, or
    dropped with its `table-wrap` when PMC full text was extracted - would
    otherwise produce exactly that verdict for every one of its oligos while
    saying nothing about any of them. On 2026-10-05 that accounted for 44 of 57
    `absent` rows in a single run.
    """
    prose = "We screened samples by real-time PCR as described previously. See Table 1."
    assert vo.printed_oligos(prose) == []


def test_paper_files_prefers_publisher_text_over_a_pdf(tmp_path):
    """Both formats for one DOI: the text file must win.

    It is the publisher's own characters, where the PDF's primer table may be an
    image or a grid pypdf has to rebuild from glyph positions. Ghosh 2021's table
    is readable only this way.
    """
    (tmp_path / "10.1111_1755-0998.13299.pdf").write_bytes(b"%PDF-1.4 not really a pdf")
    (tmp_path / "10.1111_1755-0998.13299.txt").write_text(
        "primer BdAll-F 5'-GCGGCCAACCAGTTTAACGCAA-3' and 5'-ATTGCGCTGGAACCTTGTCAA-3'"
    )
    by_doi, everything = vo.index_papers(tmp_path)
    assert "10.1111/1755-0998.13299" in by_doi
    text, path = by_doi["10.1111/1755-0998.13299"]
    assert path.suffix == ".txt", path
    assert "GCGGCCAACCAGTTTAACGCAA" in vo.printed_oligos(text)


def test_file_text_reads_xml_by_dropping_tags():
    """A publisher JATS deposit must read the same as a fetched fullTextXML."""
    import tempfile

    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "a.xml"
        p.write_text("<article><p>primer 5'-<b>GCGGCCAACCAGTTTAACGCAA</b>-3'</p></article>")
        assert "GCGGCCAACCAGTTTAACGCAA" in vo.printed_oligos(vo.file_text(p))


def test_a_table_less_text_file_does_not_override_a_working_pdf(tmp_path):
    """Regression for the first version of the multi-format index.

    It preferred publisher text over a PDF on the reasoning that structured text
    beats a table pypdf rebuilt from glyph positions. True of a full publisher
    deposit, false of PMC full text served without its `table-wrap` content - so
    merging PMC texts into a papers/ folder of good PDFs would have silently
    replaced readable primer tables with files holding no sequences at all.
    Whichever file yields more oligos wins now.
    """
    doi = "10.1234_test.1"
    rich = "primer F 5'-GCGGCCAACCAGTTTAACGCAA-3' primer R 5'-ATTGCGCTGGAACCTTGTCAA-3'"
    (tmp_path / f"{doi}.txt").write_text("We screened by PCR as described. See Table 1.")
    (tmp_path / f"{doi}.xml").write_text(f"<article><p>{rich}</p></article>")
    by_doi, _ = vo.index_papers(tmp_path)
    text, path = by_doi["10.1234/test.1"]
    assert path.suffix == ".xml", path
    assert len(vo.printed_oligos(text)) == 2


def test_a_doi_named_file_beats_a_doi_merely_cited_elsewhere(tmp_path):
    """Standing comes before yield, or an image-table paper loses its own DOI.

    A filename is a statement that this IS the paper. A DOI in running text is
    often just a reference. So the named file wins even printing nothing, which
    is what keeps "the PDF is here and its table is an image" distinct from
    "the PDF is missing".
    """
    (tmp_path / "10.5555_mine.9.txt").write_text("Our assay is described in Table 2.")
    (tmp_path / "someone-else.txt").write_text(
        "We cite 10.5555/mine.9 and print 5'-GCGGCCAACCAGTTTAACGCAA-3' "
        "and 5'-ATTGCGCTGGAACCTTGTCAA-3' of our own."
    )
    by_doi, _ = vo.index_papers(tmp_path)
    _, path = by_doi["10.5555/mine.9"]
    assert path.name == "10.5555_mine.9.txt", path


def test_reads_the_n_or_inosine_notation_as_n():
    """Prepens 2007 and the other Ehlers-lab consensus-primer papers spell an
    ambiguous position out as `(N/I)` - "N or inosine" - inside the sequence.

    The brackets and slash end the run, so without normalisation `printed_oligos`
    returns a fragment and every stored oligo past the first bracket reports
    `absent`. That produced 4 false verdicts on one paper, all 4 of them exact
    matches to the registry once the notation is read.
    """
    paper = "2744s 1 TTCAAGGAACTCAGYAARAT(N/I)AAYCC 250"
    printed = vo.printed_oligos(vo.normalise_notation(paper))
    assert "TTCAAGGAACTCAGYAARATNAAYCC" in printed, printed
    verdict, _ = vo.check("TTCAAGGAACTCAGYAARATNAAYCC", vo.normalise_notation(paper), printed, 4)
    assert verdict == "exact", verdict


def test_the_notation_survives_both_cases_and_bracket_styles():
    """One table in one paper used `(N/I)` and `[n/i]`, so both must work."""
    for token in ("(N/I)", "[n/i]", "(n/i)", "[N/I]", "(I/N)"):
        got = vo.normalise_notation(f"CGTTGTCCTC{token}CCNARYTGNCC")
        assert got == "CGTTGTCCTCNCCNARYTGNCC", (token, got)


def test_any_base_or_inosine_reads_as_n():
    """Deckers 2009 prints `(b/i)` and `(r/i)` beside `(n/i)`. Read only as
    `(N/I)`, its 4125s came out `absent` and 4125as `near:3`, both exact once
    read - the same false verdict the `(N/I)` fix removed, one letter over.
    """
    paper = "4125s 2 GCGGACTCGGTGAT(b/i)TC(n/i)TGGGA 550 4125as GCTGACGGGTTGATCTTGCT(r/i)AG"
    text = vo.normalise_notation(paper)
    printed = vo.printed_oligos(text)
    for stored in ("GCGGACTCGGTGATNTCNTGGGA", "GCTGACGGGTTGATCTTGCTNAG"):
        verdict, _ = vo.check(stored, text, printed, 4)
        assert verdict == "exact", (stored, verdict, printed)


def test_the_notation_is_not_silently_collapsed_to_two_bases():
    """The dangerous half: `check`'s substring search strips every non-IUPAC
    character, and N and I are BOTH IUPAC, so an unnormalised `(N/I)` becomes
    the two bases `NI` and shifts the rest of the sequence by one. That is a
    wrong answer rather than a missing one, which is why the normalisation has
    to happen before the text reaches either search.
    """
    raw = "primer 5'-CGTTGTCCTC(N/I)CCNARYTGNCC-3'"
    assert "NI" in vo.NOISE.sub("", raw.upper())
    assert "NI" not in vo.NOISE.sub("", vo.normalise_notation(raw).upper())
