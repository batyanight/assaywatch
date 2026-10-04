"""Regressions for the 2026-10-04 audit: each test failed (or crashed) before its fix."""

import random

import pytest
from test_score import ASSAYS, CFG, RECORDS

from assaywatch.fasta import read_fasta
from assaywatch.iupac import expand, reverse_complement
from assaywatch.match import find_sites
from assaywatch.score import screen_record

BD = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"


def rnd(n, seed):
    rng = random.Random(seed)
    return "".join(rng.choice("ACGT") for _ in range(n))


@pytest.mark.parametrize("junk", ["-", "*", "X", " ", "1", "."])
def test_non_iupac_characters_do_not_crash_and_count_as_mismatches(junk):
    a = ASSAYS[BD]
    rec = RECORDS[f"{BD}__perfect"]
    assert screen_record(a, "x", rec + junk * 3 + "ACGT", CFG).call == "detect"
    fwd = a.oligos.forward.matching_seq
    broken = fwd[:5] + junk + fwd[6:]
    site = [s for s in find_sites(fwd, "AAAA" + broken + "AAAA", 6) if s.strand == "+"][0]
    assert 5 in site.mismatches


def test_reverse_complement_keeps_unknown_characters_and_lowercase():
    assert reverse_complement("acgT-N*") == "*N-ACGT"


def test_fasta_blank_header_and_spaced_sequence(tmp_path):
    p = tmp_path / "x.fa"
    p.write_text(">\nAC GT\n>r2 desc\nAC\tGT\n")
    assert list(read_fasta(p)) == [("", "ACGT"), ("r2", "ACGT")]


def test_probe_site_inside_amplicon_is_found_however_many_copies_lie_elsewhere():
    a = ASSAYS[BD]
    probe = a.oligos.probe.matching_seq
    decoys = "".join(probe + rnd(40, i) for i in range(80))  # 80 perfect probe copies, no primers
    rec = decoys + rnd(500, 99) + RECORDS[f"{BD}__perfect"]
    assert screen_record(a, "x", rec, CFG).call == "detect"


def test_true_site_is_not_lost_among_many_chance_sites_in_a_genome():
    a = ASSAYS[BD]
    cfg = {**CFG, "scoring": {**CFG["scoring"], "max_pair_evalue": None}}
    genome = rnd(1_500_000, 5)
    rec = genome[:700_000] + RECORDS[f"{BD}__perfect"] + genome[700_000:]
    call = screen_record(a, "g", rec, cfg)
    assert call.call == "detect" and 699_000 < call.amplicon_start < 702_000


def test_probe_less_pair_does_not_outrank_a_real_amplicon_with_its_probe():
    a = ASSAYS[BD]
    fwd, rev = a.oligos.forward.matching_seq, a.oligos.reverse.matching_seq
    no_probe = fwd + rnd(70, 1) + reverse_complement(rev)  # clean primers, no probe
    # A real amplicon whose forward primer has a 3'-terminal mismatch: a fail with the probe present.
    real = RECORDS[f"{BD}__perfect"]
    i = real.index(fwd) + len(fwd) - 1
    real = real[:i] + ("A" if real[i] != "A" else "C") + real[i + 1 :]
    call = screen_record(a, "x", no_probe + rnd(4000, 2) + real, CFG)
    assert call.call == "fail" and call.reason != "no probe site inside amplicon"


def test_seq_as_written_must_be_seq_with_inosine():
    from pydantic import ValidationError

    from assaywatch.schema import Oligo

    assert Oligo(seq="ACGTNACGTACGTACG", seq_as_written="ACGTIACGTACGTACG").matching_seq == "ACGTIACGTACGTACG"
    with pytest.raises(ValidationError):
        Oligo(seq="ACGTNACGTACGTACG", seq_as_written="ACG")


def test_degeneracy_ignores_the_tail():
    from assaywatch.degeneracy import matching_sequence
    from assaywatch.schema import Oligo

    o = Oligo(seq="NNNNNACGTACGTACGTACG", tail_5prime="NNNNN")
    assert matching_sequence(o) == "ACGTACGTACGTACG"


def test_expand_limit_counts_inosine_expansions():
    with pytest.raises(ValueError):
        expand("I" * 10, limit=4096)


def test_thermo_inosine_opposite_u_is_modelled_as_t():
    pytest.importorskip("primer3")
    from assaywatch.thermo import resolve

    o, t, ino = resolve("GACIT", "GACUT")
    assert ino and o == "GACTT" and t == "GACTT"
    o, t, _ = resolve("GACGT", "GA-GT")  # a gap is a mismatch, not a perfect pair
    assert o[2] != t[2]
