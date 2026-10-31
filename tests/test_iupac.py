from assaywatch.iupac import base_matches, degeneracy, expand, mismatch_positions, reverse_complement


def test_reverse_complement_handles_degenerate_codes():
    assert reverse_complement("ACGT") == "ACGT"
    assert reverse_complement("GAYTTYGCN") == "NGCRAARTC"


def test_degeneracy_and_expand():
    assert degeneracy("ACGT") == 1
    assert degeneracy("RY") == 4
    assert sorted(expand("AR")) == ["AA", "AG"]


def test_expand_refuses_absurd_oligos():
    import pytest

    with pytest.raises(ValueError):
        expand("N" * 10, limit=1000)


def test_base_matches_degenerate_cover():
    assert base_matches("R", "A") and base_matches("R", "G")
    assert not base_matches("R", "C")
    assert base_matches("N", "A")
    assert not base_matches("A", "N")  # unknown target base is never evidence of binding
    assert base_matches("R", "R")  # target degenerate covered by oligo degenerate


def test_mismatch_positions_known_answer():
    oligo = "CAGTGTGCCATATGTCACG"
    target = "CAGTGTGCCATATGTCACG"
    assert mismatch_positions(oligo, target) == []
    target = "CAGTGTGCCATATGTCACT"  # last base (3' terminal) changed
    assert mismatch_positions(oligo, target) == [18]
