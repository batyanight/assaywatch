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


def test_pdb_chain_ids_join_to_their_metadata():
    from assaywatch.report import strip_version

    assert strip_version("pdb|29WD|T") == strip_version("29WD_T") == "29WD_T"
    assert strip_version("AB123.2") == "AB123"


def test_newest_version_wins_whatever_the_row_order():
    from assaywatch.report import key_calls_by_accession

    rows = [
        {"assay_id": "A", "record_id": "AB1.2", "call": "fail"},
        {"assay_id": "A", "record_id": "AB1.1", "call": "detect"},
    ]
    assert [r["call"] for r in key_calls_by_accession(rows)] == ["fail"]


def test_recent_window_is_exactly_the_configured_months():
    from datetime import date

    from assaywatch.drift import assess, recent_cutoff

    cfg = {"drift": {"recent_window_months": 24, "min_records_for_drift": 1}}
    assert recent_cutoff(cfg, date(2026, 10, 4)) == date(2024, 10, 4)
    calls = [{"assay_id": "A", "record_id": r, "call": "detect"} for r in ("old", "new")]
    a = assess(calls, {"old": "2024-03-01", "new": "2024-11-01"}, cfg, today=date(2026, 10, 4))["A"]
    assert (a.recent_evaluable, a.baseline_evaluable) == (1, 1)


def test_assay_with_only_undated_records_still_appears():
    from assaywatch.drift import assess

    calls = [{"assay_id": "A", "record_id": f"r{i}", "call": "detect"} for i in range(5)]
    a = assess(calls, {}, {"drift": {}})["A"]
    assert a.status == "no recent data" and a.skipped_undated == 5


def test_markdown_cells_escape_pipes():
    from assaywatch.report import md

    assert md("BAD|ID") == "BAD\\|ID"


def test_small_bounds_are_not_rounded_to_zero():
    from assaywatch.drift import pct

    assert pct(0.0019) == "0.2%" and pct(0.0) == "0%" and pct(-0.001, signed=True) == "-0.1%"
    assert pct(-0.004, signed=True) != "-0%" and pct(-0.0004, signed=True) == "0%"


def _screen(*args):
    import subprocess
    import sys

    from test_score import ROOT

    return subprocess.run(
        [sys.executable, "-m", "assaywatch.screen", str(ROOT / "registry"), *args],
        capture_output=True,
        text=True,
    )


def test_empty_fasta_still_gets_a_header(tmp_path):
    empty = tmp_path / "empty.fa"
    empty.write_text("")
    out = tmp_path / "calls.tsv"
    assert _screen(str(empty), "--only", BD, "-o", str(out)).returncode == 0
    assert out.read_text().startswith("assay_id\trecord_id\tcall")


def test_bad_arguments_fail_before_screening(tmp_path):
    from test_score import FIX

    fa = str(FIX / "records.fasta")
    assert "names no assays" in _screen(fa, "--only", " , ").stderr
    assert "does not exist" in _screen(fa, "--only", BD, "-o", str(tmp_path / "nope" / "x.tsv")).stderr
    assert "at least 1" in _screen(fa, "--workers", "0").stderr


def test_a_second_retrieval_is_refused_while_one_holds_the_lock(tmp_path):
    import subprocess
    import sys

    from assaywatch.retrieve import acquire_lock

    cfg = {"retrieved_dir": str(tmp_path / "retrieved")}
    held = acquire_lock(cfg)
    try:
        # flock is per open file, so a second process is the honest test.
        code = (
            "import sys; from assaywatch.retrieve import acquire_lock; "
            f"acquire_lock({{'retrieved_dir': {cfg['retrieved_dir']!r}}})"
        )
        proc = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
        assert proc.returncode != 0 and "another retrieval is running" in proc.stderr
    finally:
        held.close()
    proc = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert proc.returncode == 0  # released when the holder closes or exits


def test_degeneracy_tsv_is_a_real_table():
    import csv
    import io
    import subprocess
    import sys

    from test_score import ROOT

    out = subprocess.run(
        [sys.executable, "-m", "assaywatch.degeneracy", str(ROOT / "registry"), "--tsv"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    rows = list(csv.DictReader(io.StringIO(out), delimiter="\t"))
    assert rows and set(rows[0]) == {
        "assay_id",
        "total_fold",
        "primer_fold",
        "probe_fold",
        "expected_cq_delay",
        "inosine_positions",
        "tier",
    }
    assert all(r["total_fold"].isdigit() for r in rows)
    bad = subprocess.run(
        [sys.executable, "-m", "assaywatch.degeneracy", str(ROOT / "registry"), "--tier", "nonsense"],
        capture_output=True,
        text=True,
    )
    assert bad.returncode != 0 and "must be one of" in bad.stderr


def test_a_pool_member_can_carry_the_call():
    """Consensus protocols run several primers per role; any of them amplifying is a detection."""
    import random
    from pathlib import Path

    from assaywatch.score import oligo_pools, screen_one
    from assaywatch.validate import load_assay

    root = Path(__file__).resolve().parents[1]
    assay = load_assay(root / "registry" / "FILOVIRUS_ssRNA_L_gene.yaml")
    fwd, rev, _ = oligo_pools(assay)
    assert len(fwd) >= 4 and len(rev) >= 4, "this assay is a 4x4 primer pool"
    rng = random.Random(11)

    def noise(n):
        return "".join(rng.choice("ACGT") for _ in range(n))

    # A record carrying only the last pool member of each role.
    rec = noise(300) + fwd[-1] + noise(200) + reverse_complement(rev[-1]) + noise(300)
    assert screen_one(assay, "x", rec, CFG).call == "no_amplicon"  # the declared pair alone
    pooled = screen_record(assay, "x", rec, CFG)
    assert pooled.call == "detect"
    assert fwd[-1] in pooled.extra["pool"] and rev[-1] in pooled.extra["pool"]


def test_exclusion_tells_a_truncated_deposit_from_a_diverged_site():
    """The reason a record is unusable is not incidental: one is about the deposit, one about the assay."""
    import random
    from pathlib import Path

    from assaywatch.validate import load_assay

    root = Path(__file__).resolve().parents[1]
    assay = load_assay(root / "registry" / "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004.yaml")
    rev = assay.oligos.reverse.matching_seq
    rng = random.Random(5)

    def noise(n):
        return "".join(rng.choice("ACGT") for _ in range(n))

    # The reverse site sits on the minus strand, so the forward primer belongs at
    # LOWER coordinates. Only 20 bases there: the deposit stops short.
    short = noise(20) + reverse_complement(rev) + noise(400)
    call = screen_record(assay, "short", short, CFG)
    assert call.call == "no_amplicon" and call.as_row()["exclusion"] == "truncated"

    # Same site with ample room on that side, and nothing resembling the forward primer.
    roomy = noise(900) + reverse_complement(rev) + noise(400)
    assert screen_record(assay, "roomy", roomy, CFG).as_row()["exclusion"] == "diverged"

    # Neither primer anywhere.
    assert screen_record(assay, "none", noise(600), CFG).as_row()["exclusion"] == "no_site"


def test_thermo_survives_a_primer_pool_of_mixed_lengths():
    """A pool member of a different length than the primary oligo used to crash the screen."""
    import subprocess
    import sys
    from pathlib import Path

    from test_score import FIX

    from assaywatch.score import oligo_pools
    from assaywatch.validate import load_assay

    root = Path(__file__).resolve().parents[1]
    assay = load_assay(root / "registry" / "Pan_HERPES_dsDNA_Polymerase.yaml")
    fwd, _, _ = oligo_pools(assay)
    assert len({len(x) for x in fwd}) > 1, "this assay should have a mixed-length forward pool"
    out = subprocess.run(
        [
            sys.executable,
            "-m",
            "assaywatch.screen",
            str(root / "registry"),
            str(FIX / "records.fasta"),
            "--only",
            assay.id,
            "--thermo",
        ],
        capture_output=True,
        text=True,
    )
    assert out.returncode == 0, out.stderr[-400:]


def test_every_probe_pool_member_is_searched():
    """Only the first member used to be searched, while the docstring claimed otherwise."""
    import random
    from pathlib import Path

    from assaywatch.score import screen_one
    from assaywatch.validate import load_assay

    root = Path(__file__).resolve().parents[1]
    assay = load_assay(root / "registry" / "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004.yaml")
    fwd = assay.oligos.forward.matching_seq
    rev = assay.oligos.reverse.matching_seq
    real_probe = assay.oligos.probe.matching_seq
    rng = random.Random(17)
    decoy = "".join(rng.choice("ACGT") for _ in range(len(real_probe)))
    # A record carrying only the SECOND probe member of the pool.
    rec = fwd + "AC" * 10 + real_probe + "GT" * 10 + reverse_complement(rev)
    # Primary probe is the decoy, so a single-probe search finds nothing.
    assert screen_one(assay, "x", rec, CFG, None, fwd, rev, [decoy]).reason == "no probe site inside amplicon"
    # With both members in the pool the real one must be found.
    assert screen_one(assay, "x", rec, CFG, None, fwd, rev, [decoy, real_probe]).call in ("detect", "reduced")
