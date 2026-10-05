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
