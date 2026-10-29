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
from assaywatch.score import RESOLVED, classify, load_config, screen_record

ROOT = Path(__file__).resolve().parents[1]
FIX = Path(__file__).resolve().parent / "fixtures"
CFG = load_config()
# The synthetic MANIFEST fixtures hand-encode the POSITION, COUNT and TERMINAL
# rules, and a planted mismatch at a primer G becomes an incidental G:T wobble -
# so any non-empty scoring.mispair_penalty changes their calls for a reason the
# fixture never meant to test. config.yaml ships the table empty (the G:T/T:G
# value was tried and reverted, docs/journal/2026-10-22-M1-tier2.md), so today this is a
# no-op; it stays explicit so the fixture tests keep testing position, count and
# terminal behaviour whatever a later candidate puts in the table. The mechanism
# itself is pinned by the dedicated identity tests below.
CFG_NO_MISPAIR = {**CFG, "scoring": {**CFG["scoring"], "mispair_penalty": {}}}
# `load_config` caches the per-chemistry resolution INSIDE the dict it returns
# (`score.RESOLVED`), and a shallow copy carries that cache, so `config_for` would
# answer from the shipped table however this copy's `scoring` reads. Found
# 2026-10-27 when the M1 table shipped: three fixture rows planted on a primer G
# read as free wobbles for conventional assays. Same footgun
# scripts/price_terminal_mismatch.py hit the same day; the cache must be dropped.
CFG_NO_MISPAIR.pop(RESOLVED, None)
RECORDS = dict(read_fasta(FIX / "records.fasta"))
MANIFEST = list(csv.DictReader((FIX / "manifest.tsv").open(), delimiter="\t"))
ASSAYS = {
    row["assay_id"]: Assay.model_validate(
        yaml.safe_load((ROOT / "registry" / f"{row['assay_id']}.yaml").read_text())
    )
    for row in MANIFEST
}


def declared_spacer(assay, fwd_len: int | None = None, rev_len: int | None = None, filler="ACGT") -> str:
    """Filler that puts a hand-built record's product at the assay's declared size.

    `amplicon.declared_tolerance` constrains a call to the assay's own
    `amplicon_bp`, so a record built with an arbitrary spacer is `no_amplicon`
    however good the primer sites planted in it are — the test would then pass
    or fail on its spacer rather than on what it means to test. Lengths may be
    given explicitly for a pool member that is not the stored oligo. An assay
    with no declared size keeps the old fixed spacing.
    """
    f = fwd_len if fwd_len is not None else len(assay.oligos.forward.matching_seq)
    r = rev_len if rev_len is not None else len(assay.oligos.reverse.matching_seq)
    n = (assay.amplicon_bp - f - r) if assay.amplicon_bp else 120
    if n < 10:
        n = 120
    return (filler * (n // len(filler) + 1))[:n]


@pytest.mark.parametrize("row", MANIFEST, ids=[r["record_id"] for r in MANIFEST])
def test_expected_call(row):
    assay = ASSAYS[row["assay_id"]]
    call = screen_record(assay, row["record_id"], RECORDS[row["record_id"]], CFG_NO_MISPAIR)
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


def test_screen_only_restricts_to_named_assays(tmp_path):
    out = tmp_path / "calls.tsv"
    subprocess.run(
        [
            sys.executable,
            "-m",
            "assaywatch.screen",
            str(ROOT / "registry"),
            str(FIX / "records.fasta"),
            "--only",
            "CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004",
            "-o",
            str(out),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assays = {line.split("\t")[0] for line in out.read_text().splitlines()[1:]}
    assert assays == {"CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004"}


def test_screen_only_rejects_unknown_ids():
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "assaywatch.screen",
            str(ROOT / "registry"),
            str(FIX / "records.fasta"),
            "--only",
            "NOT_AN_ASSAY",
        ],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0 and "NOT_AN_ASSAY" in proc.stderr


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


def test_scaffold_gaps_do_not_blow_up_or_fake_an_amplicon():
    """Regression for the nine-hour Bd run: a long N-gap must be fast and must not score."""
    import time

    assay = ASSAYS["CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"]
    rec = RECORDS["CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004__perfect"]  # no Boyle site in it
    t = time.perf_counter()
    call = screen_record(assay, "gap", rec + "N" * 50_000 + rec, CFG)
    assert time.perf_counter() - t < 2.0
    assert call.call == "no_amplicon"


def test_real_site_is_found_next_to_a_scaffold_gap():
    assay = ASSAYS["CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"]
    rec = RECORDS["CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004__perfect"]
    assert screen_record(assay, "gap", "N" * 20_000 + rec + "N" * 20_000, CFG).call == "detect"


def test_screen_output_appears_only_when_complete(tmp_path):
    out = tmp_path / "calls.tsv"
    subprocess.run(
        [
            sys.executable,
            "-m",
            "assaywatch.screen",
            str(ROOT / "registry"),
            str(FIX / "records.fasta"),
            "--only",
            "CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004",
            "-o",
            str(out),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert out.exists() and not list(tmp_path.glob(".*.part"))


def _screen_cli(out, *extra):
    subprocess.run(
        [
            sys.executable,
            "-m",
            "assaywatch.screen",
            str(ROOT / "registry"),
            str(FIX / "records.fasta"),
            "--only",
            ",".join(sorted(ASSAYS)),
            "-o",
            str(out),
            *extra,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return out.read_bytes()


def test_screen_workers_do_not_change_the_output(tmp_path):
    """Parallel screening is an implementation detail: same bytes for any worker count or batch size."""
    serial = _screen_cli(tmp_path / "serial.tsv")
    # A tiny batch size forces many batches, so ordering across workers is exercised.
    parallel = _screen_cli(tmp_path / "parallel.tsv", "--workers", "3", "--chunk-bp", "2000")
    assert parallel == serial
    assert serial.count(b"\n") == len(RECORDS) * len(ASSAYS) + 1


def test_batches_cover_every_record_in_order():
    from assaywatch.screen import batches

    recs = [(f"r{i}", "A" * (i + 1)) for i in range(20)]
    got = list(batches(recs, 30))
    assert [r for b in got for r in b] == recs
    assert all(sum(len(s) for _, s in b) >= 30 for b in got[:-1])


@pytest.mark.parametrize("row", MANIFEST, ids=[r["record_id"] for r in MANIFEST])
def test_call_does_not_depend_on_record_orientation(row):
    """A record read antisense, or a minus-strand gene in a genome, is the same target."""
    assay = ASSAYS[row["assay_id"]]
    seq = RECORDS[row["record_id"]]
    fwd = screen_record(assay, row["record_id"], seq, CFG)
    rev = screen_record(assay, row["record_id"], reverse_complement(seq), CFG)
    assert (rev.call, rev.penalty, rev.amplicon_bp) == (fwd.call, fwd.penalty, fwd.amplicon_bp)
    if fwd.amplicon_start is not None:
        # Same bases, mirrored coordinates.
        assert rev.amplicon_start == len(seq) - fwd.amplicon_end


# --- M1: identity-aware 3'-window penalty (scoring.mispair_penalty) -----------
# Added 2026-10-21. These pin the mechanism, not a shipped value: config.yaml
# ships mispair_penalty: {} and every other test above asserts the empty-table
# behaviour is unchanged. See docs/journal/2026-10-20-pipeline-audit.md M1.

from assaywatch.match import find_sites as _find_sites  # noqa: E402
from assaywatch.score import mispair_multiplier, score_primer  # noqa: E402


def _primer_site(oligo: str, record: str):
    """The plus-strand Site for `oligo` in `record`, with its real `window`."""
    return next(s for s in _find_sites(oligo, record, 4) if s.strand == "+")


def _scoring(**overrides):
    """The real scoring block with mispair_penalty (and anything else) overridden."""
    return {**CFG, "scoring": {**CFG["scoring"], **overrides}}


# A terminal mismatch where primer G faces record A, i.e. a G:T wobble on the
# template strand. find_sites confirmed window[19] == 'A', COMPLEMENT -> 'T'.
_OLIGO = "TTGACCGATAGCCAATGATG"
_REC_TERMINAL_GT = "TTGACCGATAGCCAATGATA"


def test_mispair_multiplier_only_fires_on_definite_acgt_and_an_empty_table_is_one():
    assert mispair_multiplier("G", "T", {}) == 1.0  # empty table: byte-identical
    assert mispair_multiplier("G", "T", {"G:T": 0.0}) == 0.0
    assert mispair_multiplier("G", "T", {"A:C": 0.0}) == 1.0  # a different mispair
    assert mispair_multiplier("Y", "T", {"G:T": 0.0}) == 1.0  # degenerate primer base
    assert mispair_multiplier("G", "N", {"G:T": 0.0}) == 1.0  # ambiguous template base


def test_empty_mispair_table_scores_the_position_penalty_and_sets_terminal():
    site = _primer_site(_OLIGO, _REC_TERMINAL_GT)
    sc = score_primer(site, _OLIGO, _scoring(mispair_penalty={}))
    assert sc.penalty == CFG["scoring"]["primer_3prime_penalty"]  # one 3'-window mismatch
    assert sc.terminal_mismatch is True


def test_a_zeroed_mispair_drops_the_penalty_and_exempts_the_terminal_fail():
    site = _primer_site(_OLIGO, _REC_TERMINAL_GT)
    sc = score_primer(site, _OLIGO, _scoring(mispair_penalty={"G:T": 0.0}))
    assert sc.penalty == 0.0
    # A mispair declared free must also not trip terminal_mismatch_fails, or the
    # discount would be defeated at the one position it matters most.
    assert sc.terminal_mismatch is False


# The same G:T wobble moved OUT of the 3' window: identity must NOT fire there.
# Kwok's effect is 3'-specific; discounting internal G:T across whole record sets
# masked three real coverage drops in tier-2 (docs/journal/2026-10-22-M1-tier2.md).
_REC_5PRIME_GT = "TTAACCGATAGCCAATGATG"  # primer G at pos 2 (d=18) faces record A -> G:T


def test_a_zeroed_mispair_outside_the_3prime_window_is_not_discounted():
    site = _primer_site(_OLIGO, _REC_5PRIME_GT)
    assert site.mismatches == (2,)  # one mismatch, 18 nt from the 3' end
    sc = score_primer(site, _OLIGO, _scoring(mispair_penalty={"G:T": 0.0}))
    # Beyond the 3' window position alone decides: the full 5'-region penalty, undiscounted.
    assert sc.penalty == CFG["scoring"]["primer_5prime_penalty"]
    assert sc.terminal_mismatch is False


# The same wobble in the MID window (d=10), which is the class S7b is about: the
# Mills/G2R false alarm rests on a G:T at reverse position 8, costing a full
# primer_mid_penalty while the table already calls that mispair free at d<=5.
_REC_MID_GT = "TTGACCGATAACCAATGATG"  # primer G at pos 10 (d=10) faces record A -> G:T


def test_mispair_window_decides_how_far_identity_reaches_and_defaults_to_the_3prime_window():
    site = _primer_site(_OLIGO, _REC_MID_GT)
    assert site.mismatches == (10,)  # one mismatch, 10 nt from the 3' end: mid window
    table = {"G:T": 0.0}
    mid = CFG["scoring"]["primer_mid_penalty"]

    # Null (what ships): identity acts only within primer_3prime_window, so a mid
    # mismatch keeps its full position penalty however the table reads.
    assert score_primer(site, _OLIGO, _scoring(mispair_penalty=table)).penalty == mid
    assert score_primer(site, _OLIGO, _scoring(mispair_penalty=table, mispair_window=None)).penalty == mid
    # The S7b candidate: 10 bases reaches the mid window, and the wobble goes free.
    assert score_primer(site, _OLIGO, _scoring(mispair_penalty=table, mispair_window=10)).penalty == 0.0
    # Narrowing below the window turns identity off entirely, including at the
    # terminus, where it also stops exempting terminal_mismatch_fails.
    terminal = _primer_site(_OLIGO, _REC_TERMINAL_GT)
    sc = score_primer(terminal, _OLIGO, _scoring(mispair_penalty=table, mispair_window=0))
    assert sc.penalty == CFG["scoring"]["primer_3prime_penalty"]
    assert sc.terminal_mismatch is True


def test_the_shipped_config_leaves_identity_scoped_to_the_3prime_window():
    """`mispair_window` ships null, so M1's scope is unchanged until S7b is priced."""
    assert CFG["scoring"]["mispair_window"] is None


def test_a_partial_multiplier_scales_the_penalty_but_keeps_the_terminal_flag():
    site = _primer_site(_OLIGO, _REC_TERMINAL_GT)
    sc = score_primer(site, _OLIGO, _scoring(mispair_penalty={"G:T": 0.5}))
    assert sc.penalty == CFG["scoring"]["primer_3prime_penalty"] * 0.5
    assert sc.terminal_mismatch is True  # not zeroed, so still a terminal mismatch


def test_an_unlisted_mispair_is_unaffected_by_a_nonempty_table():
    site = _primer_site(_OLIGO, _REC_TERMINAL_GT)  # this mispair is G:T
    sc = score_primer(site, _OLIGO, _scoring(mispair_penalty={"A:C": 0.0}))
    assert sc.penalty == CFG["scoring"]["primer_3prime_penalty"]
    assert sc.terminal_mismatch is True


def test_mispair_penalty_is_a_recognised_per_chemistry_override_key():
    from assaywatch.score import check_chemistry_overrides

    ok = _scoring(by_chemistry={"conventional": {"mispair_penalty": {"G:T": 0.0}}})
    assert check_chemistry_overrides(ok) == []
    # A misspelling must be rejected loudly, not silently ignored, or a run would
    # look recalibrated when it was not.
    bad = _scoring(by_chemistry={"conventional": {"mispair_pentalty": {"G:T": 0.0}}})
    assert any("mispair_pentalty" in p for p in check_chemistry_overrides(bad))


# --- Per-oligo verdicts: scoring.engine = budget | serial ---------------------
# Added 2026-10-21. config.yaml ships `engine: budget`, so every test above
# asserts the summed-budget behaviour and this block asserts the alternative.
# What motivated it is a measurement, not a preference: on
# results/2026-10-20/calls.tsv.gz the terminal-identity rule drives 1,618 of
# 269,789 fails (0.60%) while 213,398 (79.1%) sit in 3.01-6.0 just above the
# `reduced_max` cut, and judging the same penalties per oligo moves 182,185 of
# the 912,111 calls `decide` makes. The shared budget, not identity-blindness,
# decides most of the call set. `budget` reproduces every one of those 912,111
# stored calls when replayed through `decide`, which is what says this split is
# faithful on real data and not only on the fixtures.

from assaywatch.score import OligoScore, combine, decide, oligo_verdict  # noqa: E402


def _serial(**overrides):
    return _scoring(engine="serial", **overrides)


def _os(penalty: float, *, terminal: bool = False, ambiguous=()):
    """An OligoScore carrying just what the verdict functions read."""
    return OligoScore(penalty, terminal, (), (), ambiguous)


def test_oligo_verdict_bands():
    cfg = _serial()  # oligo_ok_max 1.0, oligo_weak_max 3.0
    assert oligo_verdict(_os(0.0), cfg) == "ok"
    assert oligo_verdict(_os(1.0), cfg) == "ok"
    assert oligo_verdict(_os(1.01), cfg) == "weak"
    assert oligo_verdict(_os(3.0), cfg) == "weak"
    assert oligo_verdict(_os(3.01), cfg) == "blocked"


def test_a_terminal_mismatch_blocks_the_oligo_that_carries_it():
    """Same outcome as the budget engine's global `terminal`, with the oligo named."""
    cfg = _serial()
    assert oligo_verdict(_os(0.0, terminal=True), cfg) == "blocked"
    off = _serial(terminal_mismatch_fails=False)
    assert oligo_verdict(_os(0.0, terminal=True), off) == "ok"


def test_combine_is_a_serial_gate_not_a_budget():
    cfg = _serial()
    assert combine({"forward": "ok", "reverse": "ok"}, cfg) == ("detect", "")
    assert combine({"forward": "ok", "reverse": "weak"}, cfg) == ("reduced", "reverse weak")
    assert combine({"forward": "blocked", "reverse": "weak"}, cfg) == ("fail", "forward blocked")
    # A blocked oligo fails the call however well the others match: PCR needs
    # the forward AND the reverse primer.
    assert combine({"forward": "ok", "reverse": "ok", "probe": "blocked"}, cfg) == (
        "fail",
        "probe blocked",
    )


def test_combine_reports_every_oligo_at_the_deciding_level():
    cfg = _serial()
    assert combine({"forward": "weak", "reverse": "weak", "probe": "ok"}, cfg) == (
        "reduced",
        "forward, reverse weak",
    )
    assert combine({"forward": "blocked", "reverse": "blocked"}, cfg) == (
        "fail",
        "forward, reverse blocked",
    )


def test_the_reason_names_roles_in_assay_order_not_dict_order():
    """A reason string ends up in a TSV column, so it must not depend on insertion order."""
    cfg = _serial()
    forwards_first = {"forward": "weak", "probe": "weak"}
    probe_first = {"probe": "weak", "forward": "weak"}
    assert combine(forwards_first, cfg) == combine(probe_first, cfg) == ("reduced", "forward, probe weak")


def test_the_engines_disagree_exactly_where_the_measurement_says_they_do():
    """Three trivial mismatches, one per oligo: the defect `classify` documents.

    Summed they are 3.0, which is `reduced_max`, so budget calls `reduced`.
    Judged per oligo each is 1.0, which is `oligo_ok_max`, so serial calls
    `detect`. This single case is the shape of 87,119 of the 182,185 measured
    moves.
    """
    fs, rs, ps = _os(1.0), _os(1.0), _os(1.0)
    budget_call, budget_reason, budget_scalar = decide(fs, rs, ps, _scoring())
    serial_call, serial_reason, serial_scalar = decide(fs, rs, ps, _serial())
    assert (budget_call, budget_reason, budget_scalar) == ("reduced", "", 3.0)
    assert (serial_call, serial_reason, serial_scalar) == ("detect", "", 1.0)


def test_one_lethal_mismatch_fails_under_both_but_for_different_reasons():
    fs, rs = _os(4.5), _os(0.0)
    assert decide(fs, rs, None, _scoring())[0] == "fail"  # 4.5 > reduced_max
    assert decide(fs, rs, None, _serial())[:2] == ("fail", "forward blocked")


def test_the_scalar_is_the_sum_under_budget_and_the_worst_oligo_under_serial():
    """`Call.penalty` and the candidate tie-break both read this number."""
    fs, rs, ps = _os(0.5), _os(2.0), _os(1.0)
    assert decide(fs, rs, ps, _scoring())[2] == 3.5
    assert decide(fs, rs, ps, _serial())[2] == 2.0
    # With no probe, the worst is still the worst and the sum is still the sum.
    assert decide(fs, rs, None, _scoring())[2] == 2.5
    assert decide(fs, rs, None, _serial())[2] == 2.0


def test_an_unset_engine_is_the_budget_engine():
    """The shipped default must survive a config that predates the key entirely."""
    cfg = {**CFG, "scoring": {k: v for k, v in CFG["scoring"].items() if k != "engine"}}
    fs, rs = _os(1.0), _os(1.0)
    assert decide(fs, rs, None, cfg) == decide(fs, rs, None, _scoring())
    assert decide(fs, rs, None, cfg)[0] == "reduced"


def test_an_unknown_engine_name_does_not_silently_become_serial():
    """A typo must leave the shipped behaviour in place, not pick the new path."""
    fs, rs = _os(1.0), _os(1.0)
    assert decide(fs, rs, None, _scoring(engine="seriaI"))[0] == "reduced"


def test_config_ships_the_budget_engine():
    """If this fails, a shipped run has changed its calls. That is a maintainer decision."""
    assert CFG["scoring"]["engine"] == "budget"


def test_serial_runs_end_to_end_on_a_real_fixture_record():
    """The verdict path has to work through screen_record, not just in isolation."""
    row = next(r for r in MANIFEST if r["expected_call"] == "reduced")
    assay = ASSAYS[row["assay_id"]]
    rec = RECORDS[row["record_id"]]
    # Identity-agnostic fixture: score with the discount off (see CFG_NO_MISPAIR).
    budget = screen_record(assay, row["record_id"], rec, _scoring(mispair_penalty={}))
    serial = screen_record(assay, row["record_id"], rec, _serial(mispair_penalty={}))
    assert budget.call == "reduced"
    # Same record, same penalties; only the combination differs. Whatever serial
    # says, it must be a real bucket and its penalty must be <= the sum.
    assert serial.call in {"detect", "reduced", "fail", "indeterminate", "no_amplicon"}
    assert serial.penalty <= budget.penalty


def test_decide_actually_hands_the_probe_to_the_verdicts():
    """Through `decide`, not `combine`: a blocked probe must fail the call.

    Caught by mutation testing. Dropping the probe from `decide`'s verdicts
    passed every test above, because they all exercised `combine` directly with
    a probe already in the dict - so they proved the gate works and never that
    anything asks it about the probe. Same trap as the S7 and S9 tests: when a
    refactor extracts a gate, test the effect through the caller.
    """
    clean, blocked_probe = _os(0.0), _os(9.0)
    assert decide(clean, clean, blocked_probe, _serial())[:2] == ("fail", "probe blocked")
    # And a weak probe must reach the call too, not just a blocked one.
    assert decide(clean, clean, _os(2.0), _serial())[:2] == ("reduced", "probe weak")
    # Without a probe the same primers are a clean detect, so the two cases
    # above cannot be passing for some reason unrelated to the probe.
    assert decide(clean, clean, None, _serial())[:2] == ("detect", "")


def test_decide_passes_each_primer_under_its_own_role_name():
    """A blocked forward must not be reported as a blocked reverse."""
    clean = _os(0.0)
    assert decide(_os(9.0), clean, None, _serial())[1] == "forward blocked"
    assert decide(clean, _os(9.0), None, _serial())[1] == "reverse blocked"


def test_the_weak_reason_is_also_in_assay_order():
    """Both branches of `combine` order by ROLES; the blocked one was covered above."""
    cfg = _serial()
    assert combine({"probe": "weak", "reverse": "weak", "forward": "weak"}, cfg) == (
        "reduced",
        "forward, reverse, probe weak",
    )
    assert combine({"probe": "blocked", "forward": "blocked"}, cfg) == (
        "fail",
        "forward, probe blocked",
    )


# --- The declared size reaches both readers (declared_ends) -------------------
# Added 2026-10-21. `screen_one` derived the declared window inline and handled
# `amplicon_bp_range` correctly; `classify_exclusion` was handed
# `assay.amplicon_bp` alone, so a range-declaring assay passed None and fell
# through to `amplicon.max_bp` — judging truncated-versus-diverged against
# 3000 bp instead of its own ceiling. ORTHOPOXVIRUS ATI is affected today and
# every entry converted from a scalar would have been.

import copy  # noqa: E402

from assaywatch.score import declared_ends  # noqa: E402


def _assay_with(**changes):
    """A valid assay with the amplicon fields overridden."""
    d = {**copy.deepcopy(GOOD_SCORE_ASSAY), **changes}
    return Assay.model_validate(d)


GOOD_SCORE_ASSAY = {
    "id": "TEST_declared",
    "name": "Test",
    "target": {"taxid": 109871, "gene": "ITS1", "genome_type": "dsDNA"},
    "chemistry": "conventional",
    "oligos": {
        "forward": {"name": "F", "seq": "CCTTGATATAATACAGTGTGCCATATGTC"},
        "reverse": {"name": "R", "seq": "AGCCAAGAGATCCGTTGTCAAA"},
    },
    "amplicon_bp": 121,
    "citation": {"doi": "10.3354/dao060141", "design_year": 2004, "doi_verified": True},
    "use_context": ["wildlife"],
    "status": "draft",
}


def test_a_scalar_becomes_both_ends():
    assert declared_ends(_assay_with(amplicon_bp=121)) == [121, 121]


def test_a_range_gives_its_own_ends_not_the_global_ceiling():
    """The bug: a range assay used to hand `None` on to classify_exclusion."""
    a = _assay_with(amplicon_bp=None, amplicon_bp_range=[540, 1700])
    assert declared_ends(a) == [540, 1700]
    # The upper end is what classify_exclusion needs, and it must be the
    # assay's own 1700 rather than amplicon.max_bp's 3000.
    assert declared_ends(a)[1] == 1700


def test_an_assay_declaring_no_size_declares_nothing():
    """None is the honest answer, and the caller falls back to the global window."""
    assert declared_ends(_assay_with(amplicon_bp=None)) is None


def test_classify_exclusion_reads_a_span_not_a_registry_field():
    """Pinned by signature: the parameter is the declared upper end.

    If someone passes `assay.amplicon_bp` here again, a range assay silently
    reverts to the 3000 bp geometry, which is exactly the defect this closed.
    """
    import inspect

    from assaywatch.score import classify_exclusion

    params = list(inspect.signature(classify_exclusion).parameters)
    assert "amplicon_span" in params
    assert "amplicon_bp" not in params


def test_the_declared_UPPER_end_is_what_reaches_classify_exclusion():
    """Through `screen_one`, because the parameter name alone proves nothing.

    Caught by mutation testing: feeding `declared[0]` instead of `declared[1]`
    passed every other test here, since a scalar assay has lo == hi and cannot
    tell them apart. Only a range assay can, which is the whole point.

    `classify_exclusion` reaches `span` bp from the credible anchor and calls the
    record `truncated` when that window runs off the end, `diverged` when it sits
    inside. With a [540, 1700] range and a 1000 bp record anchored at 0:
    1700 overruns the record (truncated), 540 does not (diverged). So the label
    reports which end was passed.
    """
    a = _assay_with(amplicon_bp=None, amplicon_bp_range=[540, 1700])
    fwd = a.oligos.forward.seq
    # The forward primer at position 0, then filler that cannot match the
    # reverse primer (or its complement) within max_mismatches_searched.
    rec = fwd + "G" * (1000 - len(fwd))
    call = screen_record(a, "R_truncated", rec, CFG)
    assert call.call == "no_amplicon"
    assert call.extra["exclusion"] == "truncated", (
        f"got {call.extra['exclusion']!r}: `diverged` means the LOWER end of the range was "
        "passed to classify_exclusion, so a range assay's geometry is judged at 540 bp "
        "instead of its real 1700 bp ceiling"
    )
    assert "reverse primer's window" in call.reason


def test_the_span_is_the_assay_ceiling_not_the_global_one():
    """The other side of the bracket, also from mutation testing.

    The 1000 bp case above cannot tell 1700 from `amplicon.max_bp`'s 3000, since
    both overrun it. A 2000 bp record can: the assay's own 1700 bp window fits
    inside the record and reads `diverged`, while 3000 would overrun it and read
    `truncated`. So the two cases together pin the span to the declared upper
    end - not the lower end, and not the global ceiling.
    """
    a = _assay_with(amplicon_bp=None, amplicon_bp_range=[540, 1700])
    fwd = a.oligos.forward.seq
    rec = fwd + "G" * (2000 - len(fwd))
    call = screen_record(a, "R_diverged", rec, CFG)
    assert call.call == "no_amplicon"
    assert call.extra["exclusion"] == "diverged", (
        f"got {call.extra['exclusion']!r}: `truncated` on a 2000 bp record means the span came "
        "from amplicon.max_bp (3000) rather than this assay's declared 1700 bp ceiling"
    )


# --- The mispair footprint columns (Part 0.1 of the scoring-strategy test plan) -
# Added 2026-10-26. The screen already finds the mismatch configuration; until now
# it wrote down WHERE each mismatch sat and threw away WHAT it was, which is why
# every scoring candidate so far cost a full ~30-minute rescreen to price. These
# pin the recorded identity so a candidate can be REPLAYED over a calls table.
# They assert a FORMAT and a completeness rule, never a scoring value: every test
# above still asserts the penalties, and nothing here changes one.

from assaywatch.drift import FOOTPRINT_COLUMNS, footprint_signature  # noqa: E402
from assaywatch.score import Call, score_probe  # noqa: E402

_REC_DEGENERATE = "TTGACCGATAGCCAATGAAG"  # faces the Y in _OLIGO_DEGENERATE
_OLIGO_DEGENERATE = "TTGACCGATAGCCAATGAYG"
_REC_AMBIGUOUS = "TTAACCGATAGCCAATGATN"  # one definite mismatch, one undetermined base


def test_a_mispair_records_oligo_base_template_base_and_distance_from_the_3prime_end():
    site = _primer_site(_OLIGO, _REC_TERMINAL_GT)
    sc = score_primer(site, _OLIGO, _scoring())
    # Primer G at the 3'-terminal base faces record A, so the TEMPLATE base is T:
    # a G:T wobble, 1 nt from the 3' end. The template base, not the record base,
    # because that is the pair that forms and the key `mispair_multiplier` reads.
    assert sc.mispairs == ("G:T@1",)
    assert sc.mismatches_from_3prime == (1,)


def test_mispairs_are_recorded_outside_the_3prime_window_where_identity_does_not_act():
    """The emission is deliberately wider than the scoring rule that reads it.

    `mispair_multiplier` fires only within `primer_3prime_window`, and
    `test_a_zeroed_mispair_outside_the_3prime_window_is_not_discounted` pins that.
    Recording is not scoring: a replay may weight identity at a different distance,
    and it cannot invent an identity that was never written down.
    """
    site = _primer_site(_OLIGO, _REC_5PRIME_GT)
    sc = score_primer(site, _OLIGO, _scoring())
    assert sc.mispairs == ("G:T@18",)  # 18 nt out, far beyond the 5 nt window
    assert sc.penalty == CFG["scoring"]["primer_5prime_penalty"]  # unchanged by recording


def test_an_undetermined_record_base_is_counted_as_ambiguous_and_names_no_mispair():
    """An ambiguity code names no single pair, so it must not invent one.

    This is `mispair_multiplier`'s own rule, carried into the recording: a record
    N opposite a primer base could be any of four pairs, and writing one down
    would let a replay discount a mismatch that was never observed.
    """
    site = _primer_site(_OLIGO, _REC_AMBIGUOUS)
    sc = score_primer(site, _OLIGO, _scoring())
    assert sc.ambiguous == (19,)  # the record's N
    assert sc.mispairs == ("G:T@18",)  # the definite mismatch only, not two entries
    assert len(sc.mispairs) == len(sc.mismatches_from_3prime)


def test_a_degenerate_oligo_base_records_its_own_code_rather_than_an_expansion():
    """`Y:T@2`, not `C:T@2/T:T@2`.

    A degenerate primer base is a mixture of oligos, so no single mispair formed;
    `mispair_multiplier` returns 1.0 for exactly this reason. Recording the code
    keeps the row faithful to what was there and leaves the expansion to a replay
    that wants one. `scripts/bench_panel.py::window_mispairs` makes the opposite
    choice for a human-readable panel, which is why the two formats differ.
    """
    site = _primer_site(_OLIGO_DEGENERATE, _REC_DEGENERATE)
    sc = score_primer(site, _OLIGO_DEGENERATE, _scoring())
    assert sc.mispairs == ("Y:T@2",)
    assert mispair_multiplier("Y", "T", {"C:T": 0.0, "T:T": 0.0}) == 1.0


def test_a_probes_mispair_distance_is_also_measured_from_its_3prime_end():
    """One format across all three oligos, even though it means less on a probe.

    `score_probe`'s whole premise is that a probe has no 3' asymmetry, so the
    distance is carried for uniformity rather than for scoring. It took the oligo
    LENGTH until 2026-10-26 and now takes the oligo itself, which is the only
    reason it can name a base at all.
    """
    probe = "CCAAGTGTCAGATGC"
    site = _primer_site(probe, "CCAAGTGACAGATGC")
    sc = score_probe(site, probe, CFG)
    assert sc.mispairs == ("T:T@8",)  # position 7 of 15, i.e. 8 from the 3' end
    assert sc.mismatches_from_3prime == (8,)
    assert sc.penalty == CFG["scoring"]["probe_center_penalty"]  # unchanged
    assert sc.terminal_mismatch is False  # a probe never sets it


def test_the_recorded_mispairs_agree_with_what_bench_panel_derives_for_the_same_site():
    """Same mismatch, same template base, same distance - compared as meaning, not as text.

    `scripts/bench_panel.py` has derived this information since the FAP panel, in
    a different format: position-keyed, slash-joined, and expanding a degenerate
    oligo base into its alternatives. A string comparison would fail on the format
    and tell us nothing. The case is FAP59 against HPV16 (NC_001526 4901-4922),
    the same fixture `tests/test_bench_panel.py` uses, so a drift in either
    derivation shows up here.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "bench_panel", Path(__file__).resolve().parents[1] / "scripts" / "bench_panel.py"
    )
    bench_panel = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bench_panel)

    from assaywatch.iupac import IUPAC, MISMATCH, base_state
    from assaywatch.match import Site

    oligo, window = "TAACWGTIGGICAYCCWTATT", "TTGCAGTTGGACATCCCTATT"
    mm = tuple(i for i, (o, t) in enumerate(zip(oligo, window, strict=True)) if base_state(o, t) == MISMATCH)
    sc = score_primer(Site(0, len(oligo), "+", mm, window, ()), oligo, _scoring())

    # Whole oligo, so the comparison covers the mismatches outside the 3' window too.
    expected = bench_panel.window_mispairs(oligo, window, len(oligo))
    assert [p.split("@")[1] for p in sc.mispairs] == [str(d) for d, _ in expected]
    for recorded, (_, derived) in zip(sc.mispairs, expected, strict=True):
        pair, _, _ = recorded.partition("@")
        oligo_base, _, template = pair.partition(":")
        # bench_panel expands the oligo code; score.py keeps it. Agreement means the
        # expansion of what score.py recorded IS what bench_panel printed.
        assert {f"{b}:{template}" for b in IUPAC[oligo_base]} == set(derived.split("/"))


def test_the_mispair_columns_are_written_and_are_empty_for_a_clean_or_unscored_oligo():
    row = Call(
        "A",
        "R1",
        "reduced",
        forward=OligoScore(3.0, True, (19,), (1,), (), ("G:T@1",)),
        reverse=OligoScore(0.0, False, (), (), (), ()),
    ).as_row()
    assert row["fwd_mispairs"] == "G:T@1"
    assert row["rev_mispairs"] == ""  # scored and clean
    assert row["probe_mispairs"] == ""  # no probe on this assay
    # Comma-joined, the same shape as the positions column beside it.
    multi = Call(
        "A", "R2", "fail", forward=OligoScore(3.5, True, (2, 19), (18, 1), (), ("G:T@18", "G:T@1"))
    ).as_row()
    assert multi["fwd_mispairs"] == "G:T@18,G:T@1"
    assert multi["fwd_mm_from_3prime"] == "18,1"


def test_adding_identity_columns_leaves_the_footprint_signature_untouched():
    """The duplication analysis must not regroup, or published intervals move.

    `drift.footprint_signature` records positions and NOT bases on purpose: two
    records differing only in which base sits at a mismatched position merge, which
    makes footprints fewer and the interval wider - the safe direction. The new
    columns are additive and read only by a replay, so neither the column tuple nor
    a signature built from it may change. Making the footprint identity-aware is a
    separate decision.
    """
    assert "fwd_mispairs" not in FOOTPRINT_COLUMNS
    assert not any("mispair" in c for c in FOOTPRINT_COLUMNS)

    same_position_different_base = [
        Call("A", "R1", "fail", forward=OligoScore(3.0, True, (19,), (1,), (), ("G:T@1",))).as_row(),
        Call("A", "R2", "fail", forward=OligoScore(3.0, True, (19,), (1,), (), ("G:A@1",))).as_row(),
    ]
    signatures = {footprint_signature(r[c] for c in FOOTPRINT_COLUMNS) for r in same_position_different_base}
    assert len(signatures) == 1, "a different base at the same position must still merge"
