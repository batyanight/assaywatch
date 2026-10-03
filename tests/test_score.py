"""Scoring tests against the synthetic fixture set (validation tier 1).

Every expected call in tests/fixtures/manifest.tsv was worked out by hand from
the rules in config.yaml before the scorer ran. Regenerate the fixtures with
`python tests/make_fixtures.py` if the assays or plans change.
"""

import csv
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from assaywatch.fasta import read_fasta
from assaywatch.iupac import reverse_complement
from assaywatch.match import find_sites
from assaywatch.schema import Assay
from assaywatch.score import classify, load_config, screen_record

ROOT = Path(__file__).resolve().parents[1]
FIX = Path(__file__).resolve().parent / "fixtures"
CFG = load_config()
RECORDS = dict(read_fasta(FIX / "records.fasta"))
MANIFEST = list(csv.DictReader((FIX / "manifest.tsv").open(), delimiter="\t"))
ASSAYS = {
    row["assay_id"]: Assay.model_validate(
        yaml.safe_load((ROOT / "registry" / f"{row['assay_id']}.yaml").read_text())
    )
    for row in MANIFEST
}


@pytest.mark.parametrize("row", MANIFEST, ids=[r["record_id"] for r in MANIFEST])
def test_expected_call(row):
    assay = ASSAYS[row["assay_id"]]
    call = screen_record(assay, row["record_id"], RECORDS[row["record_id"]], CFG)
    assert call.call == row["expected_call"], (
        f"{row['record_id']}: edits {row['edits']} scored {call.penalty} -> {call.call}, "
        f"expected {row['expected_call']} ({call.reason})"
    )


@pytest.mark.parametrize(
    "row", [r for r in MANIFEST if r["fwd_offset"]], ids=[r["record_id"] for r in MANIFEST if r["fwd_offset"]]
)
def test_amplicon_coordinates_match_construction(row):
    """The matcher must find the primers where make_fixtures.py put them."""
    assay = ASSAYS[row["assay_id"]]
    call = screen_record(assay, row["record_id"], RECORDS[row["record_id"]], CFG)
    assert call.amplicon_start == int(row["fwd_offset"])
    assert call.amplicon_end == int(row["rev_offset"]) + len(assay.oligos.reverse.seq)


def test_mismatch_distance_is_reported_from_the_3_prime_end():
    row = next(r for r in MANIFEST if r["edits"] == "forward:7")
    assay = ASSAYS[row["assay_id"]]
    call = screen_record(assay, row["record_id"], RECORDS[row["record_id"]], CFG)
    assert call.forward.mismatches_from_3prime == (7,)


def test_reverse_primer_site_is_on_the_minus_strand():
    """A reverse primer matches the record's reverse complement, not the record."""
    assay = ASSAYS["CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"]
    seq = RECORDS["CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004__perfect"]
    rev = assay.oligos.reverse.seq
    sites = find_sites(rev, seq)
    assert [s.strand for s in sites] == ["-"]
    assert reverse_complement(seq[sites[0].start : sites[0].end]) == rev


def test_unrelated_record_gives_no_amplicon_not_fail():
    """Sequence-coverage problems must stay distinguishable from assay problems."""
    row = next(r for r in MANIFEST if r["record_id"].endswith("__unrelated"))
    assay = ASSAYS[row["assay_id"]]
    call = screen_record(assay, row["record_id"], RECORDS[row["record_id"]], CFG)
    assert call.call == "no_amplicon" and call.penalty is None


def test_degenerate_position_covering_the_target_is_not_a_mismatch():
    """A Y in the primer must not be charged for a C or a T in the record."""
    assay = ASSAYS["Pan_mycoplasma_16S_All_Van_1992"]
    fwd = assay.oligos.forward.seq
    assert "Y" in fwd
    i = fwd.index("Y")
    for base in "CT":
        window = [b if b in "ACGT" else "A" for b in fwd]  # concretise the rest
        window[i] = base
        sites = find_sites(fwd, "".join(window))
        assert sites and sites[0].n_mismatches == 0


def test_undetermined_record_bases_carry_no_penalty():
    """Ambiguity codes in the record are counted, never charged."""
    row = next(r for r in MANIFEST if r["record_id"].endswith("__rec_ambiguous_x2"))
    assay = ASSAYS[row["assay_id"]]
    call = screen_record(assay, row["record_id"], RECORDS[row["record_id"]], CFG)
    assert call.call == "detect"
    assert call.penalty == 0
    assert len(call.forward.ambiguous) == 2


def test_ambiguity_at_the_terminal_base_does_not_trigger_the_terminal_fail():
    """A real 3'-terminal mismatch is fatal; an undetermined base there is not."""
    row = next(r for r in MANIFEST if r["record_id"].endswith("__rec_ambiguous_3term"))
    assay = ASSAYS[row["assay_id"]]
    call = screen_record(assay, row["record_id"], RECORDS[row["record_id"]], CFG)
    assert call.call == "detect" and not call.forward.terminal_mismatch


def test_too_much_ambiguity_is_indeterminate_not_fail():
    """A poorly determined record is a data problem, kept out of the drift numbers."""
    row = next(r for r in MANIFEST if r["record_id"].endswith("__rec_ambiguous_x3"))
    assay = ASSAYS[row["assay_id"]]
    call = screen_record(assay, row["record_id"], RECORDS[row["record_id"]], CFG)
    assert call.call == "indeterminate"
    assert "undetermined" in call.reason


def test_ambiguity_cap_comes_from_config():
    cfg = load_config()
    cfg["scoring"]["max_ambiguous_per_oligo"] = 1
    row = next(r for r in MANIFEST if r["record_id"].endswith("__rec_ambiguous_x2"))
    assay = ASSAYS[row["assay_id"]]
    assert screen_record(assay, row["record_id"], RECORDS[row["record_id"]], cfg).call == "indeterminate"
    cfg["scoring"]["max_ambiguous_per_oligo"] = None
    assert screen_record(assay, row["record_id"], RECORDS[row["record_id"]], cfg).call == "detect"


def test_an_n_run_elsewhere_cannot_masquerade_as_a_clean_amplicon():
    """A stretch of Ns matches every oligo; it must not outrank a real site."""
    assay = ASSAYS["CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004"]
    real = RECORDS["CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004__fwd_mid_x4"]
    call = screen_record(assay, "n_run", real + "N" * 400, CFG)
    assert call.call == "fail"  # the genuine failing site, not the N block


def test_classify_boundaries():
    assert classify(1.0, False, CFG) == "detect"
    assert classify(1.01, False, CFG) == "reduced"
    assert classify(3.0, False, CFG) == "reduced"
    assert classify(3.01, False, CFG) == "fail"
    assert classify(0.0, True, CFG) == "fail"  # terminal mismatch overrides a zero total


def test_thresholds_come_from_config_not_code():
    cfg = load_config()
    cfg["scoring"]["detect_max"] = 0.0
    assert classify(0.5, False, cfg) == "reduced"


def test_screen_cli_runs():
    out = subprocess.run(
        [
            sys.executable,
            "-m",
            "assaywatch.screen",
            str(ROOT / "registry" / "CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004.yaml"),
            str(FIX / "records.fasta"),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    lines = out.stdout.strip().splitlines()
    assert lines[0].startswith("assay_id\trecord_id\tcall")
    assert len(lines) == len(RECORDS) + 1
