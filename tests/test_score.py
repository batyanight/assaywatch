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
# behaviour is unchanged. See docs/2026-10-20-pipeline-audit.md M1.

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
    budget = screen_record(assay, row["record_id"], rec, _scoring())
    serial = screen_record(assay, row["record_id"], rec, _serial())
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
