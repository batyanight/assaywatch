"""`scripts/rescore.py` replays a scoring strategy over a calls table.

The point of the harness is that it must agree with the screen. So the tests that
matter here are agreement tests: `primer_score`/`probe_score` against
`score.score_primer`/`score.score_probe` on the same mismatch configuration, and the
refusals that keep a search change from being replayed and called a scoring result.
"""

from __future__ import annotations

import csv
import gzip
import importlib.util
import sys
from pathlib import Path

import pytest

from assaywatch.iupac import MISMATCH, base_state
from assaywatch.match import Site, find_sites
from assaywatch.score import load_config, oligo_pools, score_primer, score_probe
from assaywatch.validate import iter_files, load_assay

REPO = Path(__file__).resolve().parents[1]
CFG = load_config()

spec = importlib.util.spec_from_file_location("rescore", REPO / "scripts" / "rescore.py")
rescore = importlib.util.module_from_spec(spec)
# Registered BEFORE exec_module, unlike tests/test_bench_panel.py: rescore.py defines a
# dataclass, and `dataclasses` resolves a field's type through
# `sys.modules[cls.__module__]`, which is None for a module loaded from a spec alone.
sys.modules["rescore"] = rescore
spec.loader.exec_module(rescore)


def _scoring(**overrides):
    return {**CFG, "scoring": {**CFG["scoring"], **overrides}}


# --- the registry invariant the probe length rests on -------------------------


def test_no_probe_pool_holds_oligos_of_differing_lengths():
    """The one thing a replay cannot read off a row is the probe's length.

    A primer needs none: the distance from its 3' end is recorded per mismatch, so
    the position bands can be applied without knowing how long the oligo was.
    `score_probe` divides the oligo into thirds, so it does need the length, and the
    replay takes it from the registry. That is only sound while an assay's probe
    pool is unambiguous. If this ever fails, every probe penalty the harness
    computes for that assay is quietly wrong, and `registry_facts` raises rather
    than guessing.
    """
    offenders = {}
    for path in iter_files(REPO / "registry"):
        assay = load_assay(path)
        lengths = {len(p) for p in oligo_pools(assay)[2]}
        if len(lengths) > 1:
            offenders[assay.id] = sorted(lengths)
    assert offenders == {}, f"probe pools with differing lengths: {offenders}"


# --- agreement with the screen ------------------------------------------------

_OLIGO = "TTGACCGATAGCCAATGATG"
_CASES = [
    ("a 3'-terminal mismatch", "TTGACCGATAGCCAATGATA"),
    ("a 5' mismatch outside every penalty window", "TTAACCGATAGCCAATGATG"),
    ("two mismatches in different bands", "TTAACCGATAGCCAATGATA"),
    ("a clean site", "TTGACCGATAGCCAATGATG"),
]


@pytest.mark.parametrize(("label", "record"), [(c[0], c[1]) for c in _CASES])
@pytest.mark.parametrize("mispair_table", [{}, {"G:T": 0.0}, {"G:T": 0.5}])
def test_primer_score_reproduces_score_primer(label, record, mispair_table):
    """The replay transcribes `score_primer`'s loop; this is what holds it to it.

    Deliberately a transcription and not a call into `score_primer`, because that
    function takes a `Site` and a record sequence, and inventing a window to reach
    it would mean reconstructing bases the calls table does not hold. A
    transcription can drift from its original, so it is pinned across the
    `mispair_penalty` table too - identity acts only inside the 3' window, and a
    replay that applied it everywhere would read as a cheap improvement.
    """
    cfg = _scoring(mispair_penalty=mispair_table)
    site = next(s for s in find_sites(_OLIGO, record, 4) if s.strand == "+")
    want = score_primer(site, _OLIGO, cfg)
    got = rescore.primer_score(rescore.parse_mispairs(",".join(want.mispairs)), len(site.ambiguous), cfg)
    assert got.penalty == want.penalty, label
    assert got.terminal_mismatch == want.terminal_mismatch, label
    assert got.mismatches_from_3prime == want.mismatches_from_3prime, label
    assert got.mispairs == want.mispairs, label


@pytest.mark.parametrize(
    ("label", "probe", "record"),
    [
        ("a central mismatch", "CCAAGTGTCAGATGC", "CCAAGTGACAGATGC"),
        ("an outer mismatch", "CCAAGTGTCAGATGC", "ACAAGTGTCAGATGC"),
        ("a clean probe", "CCAAGTGTCAGATGC", "CCAAGTGTCAGATGC"),
    ],
)
def test_probe_score_reproduces_score_probe(label, probe, record):
    site = next(s for s in find_sites(probe, record, 4) if s.strand == "+")
    want = score_probe(site, probe, CFG)
    got = rescore.probe_score(
        rescore.parse_mispairs(",".join(want.mispairs)), len(site.ambiguous), len(probe), CFG
    )
    assert got.penalty == want.penalty, label
    assert got.mismatches_from_3prime == want.mismatches_from_3prime, label


def test_primer_score_agrees_on_a_degenerate_oligo_whose_identity_names_no_pair():
    """A degenerate code must keep the full position penalty on both paths.

    `mispair_multiplier` returns 1.0 for a degenerate oligo base, so a `Y:T` entry
    in the table must not discount it. The replay reads the code back out of the
    recorded string, which is the step where an expansion would creep in.
    """
    oligo, window = "TAACWGTIGGICAYCCWTATT", "TTGCAGTTGGACATCCCTATT"
    mm = tuple(i for i, (o, t) in enumerate(zip(oligo, window, strict=True)) if base_state(o, t) == MISMATCH)
    cfg = _scoring(mispair_penalty={"A:G": 0.0, "T:G": 0.0})
    want = score_primer(Site(0, len(oligo), "+", mm, window, ()), oligo, cfg)
    got = rescore.primer_score(rescore.parse_mispairs(",".join(want.mispairs)), 0, cfg)
    assert got.penalty == want.penalty
    assert "W:G@5" in want.mispairs  # the degenerate base, unexpanded


# --- parsing ------------------------------------------------------------------


def test_parse_mispairs_round_trips_what_as_row_wrote():
    assert rescore.parse_mispairs("") == ()
    assert rescore.parse_mispairs("G:T@1") == (("G", "T", 1),)
    assert rescore.parse_mispairs("G:T@18,A:C@2") == (("G", "T", 18), ("A", "C", 2))
    # An undetermined template base is written as N by score_primer's defensive branch.
    assert rescore.parse_mispairs("G:N@3") == (("G", "N", 3),)


# --- the refusals -------------------------------------------------------------


@pytest.mark.parametrize(
    "key",
    [
        "max_mismatches_searched",
        "max_site_evalue",
        "max_pairs_per_record",
        "max_pair_evalue",
        "locus_identity_min",
    ],
)
def test_a_search_or_denominator_knob_is_refused_with_its_reason(key):
    problems = rescore.refuse_unreplayable({key: 1})
    assert len(problems) == 1
    assert key in problems[0]
    assert "rescreen" in problems[0]


def test_max_ambiguous_per_oligo_is_refused_although_it_could_be_replayed():
    """The counts are in the table, so this one is a choice and says so.

    Moving it moves the denominator - how many records are judged at all - which
    Part 0.4 holds fixed across every scoring comparison. Three candidates died on
    the denominator axis on 2026-10-25; it is not an axis to vary by accident.
    """
    (problem,) = rescore.refuse_unreplayable({"max_ambiguous_per_oligo": 4})
    assert "denominator" in problem
    assert "COULD be replayed" in problem


def test_an_unknown_scoring_key_is_refused_rather_than_ignored():
    """A silently ignored override makes a run look recalibrated when it was not."""
    (problem,) = rescore.refuse_unreplayable({"reduced_maxx": 4.0})
    assert "reduced_maxx" in problem


def test_a_search_knob_hidden_inside_a_by_chemistry_override_is_still_refused():
    (problem,) = rescore.refuse_unreplayable({"by_chemistry": {"mgb": {"max_pair_evalue": 0.001}}})
    assert "by_chemistry.mgb.max_pair_evalue" in problem


@pytest.mark.parametrize("key", sorted(rescore.REPLAYABLE_KEYS))
def test_every_replayable_key_is_accepted(key):
    assert rescore.refuse_unreplayable({key: {} if key in {"mispair_penalty", "by_chemistry"} else 1}) == []


def test_the_two_key_sets_partition_the_scoring_block():
    """Neither set may drift from `settings.Scoring`, in either direction.

    A new scoring key that is in neither set would be refused as unknown, which is
    the safe default; this test makes the omission loud instead, so whoever adds one
    has to say which side of the replay boundary it falls on.
    """
    from assaywatch.settings import Scoring

    fields = set(Scoring.model_fields)
    classified = rescore.REPLAYABLE_KEYS | set(rescore.UNREPLAYABLE_KEYS)
    assert fields - classified == set(), "unclassified scoring keys"
    assert classified - fields == set(), "classified keys that no longer exist"
    assert rescore.REPLAYABLE_KEYS & set(rescore.UNREPLAYABLE_KEYS) == set()


# --- pre-registration and the scratch rule ------------------------------------


def test_a_strategy_without_a_kill_criterion_is_refused(tmp_path):
    """Part 0.5. A candidate that cannot fail is not a candidate.

    Four of the last five candidates died on their own stated kill criterion, which
    only works if it is written down before the run.
    """
    p = tmp_path / "s.yaml"
    p.write_text("name: half-registered\nquestion: x\npredicts: y\n")
    with pytest.raises(SystemExit) as e:
        rescore.load_strategy(p)
    assert "kill" in str(e.value)


def test_a_fully_registered_strategy_loads(tmp_path):
    p = tmp_path / "s.yaml"
    p.write_text("name: ok\nquestion: q\npredicts: p\nkill: k\nscoring:\n  reduced_max: 4.0\n")
    s = rescore.load_strategy(p)
    assert s.name == "ok"
    assert s.scoring == {"reduced_max": 4.0}


def test_the_shipped_s0_strategy_overrides_nothing():
    """S0 is the control, so an override on it would invalidate the whole ladder."""
    s = rescore.load_strategy(REPO / "strategies" / "s0-shipped.yaml")
    assert s.scoring == {}


def test_a_replay_refuses_to_write_into_results(tmp_path):
    """`results/` is run state the report is built from; a replay is scratch.

    Part 0.2 says "never into results/", and the reason is that a replayed table is
    not a screen: it carries the scoring of a candidate that has not been shipped,
    and anything that globbed `results/*/calls.tsv.gz` would pick it up as a run.
    """
    calls = tmp_path / "calls.tsv.gz"
    with gzip.open(calls, "wt") as fh:
        fh.write("assay_id\trecord_id\tcall\tpenalty\treason\tfwd_mispairs\n")
    with pytest.raises(SystemExit) as e:
        rescore.main(
            [
                "--calls",
                str(calls),
                "--strategy",
                str(REPO / "strategies" / "s0-shipped.yaml"),
                "--out",
                str(REPO / "results" / "should-never-exist"),
            ]
        )
    assert "scratch" in str(e.value)
    assert not (REPO / "results" / "should-never-exist").exists()


def test_a_table_without_the_footprint_columns_is_refused_not_silently_passed(tmp_path):
    """The failure mode this harness exists to avoid, made loud.

    A pre-2026-10-26 calls table has no `*_mispairs`, so every mispair would parse as
    empty, every penalty would come out 0.0 and every row would read `detect`. That
    is a replay that "works" and is entirely fiction.
    """
    calls = tmp_path / "calls.tsv.gz"
    with gzip.open(calls, "wt") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["assay_id", "record_id", "call", "penalty", "reason"])
        w.writerow(["A", "R1", "fail", "3", ""])
    with pytest.raises(SystemExit) as e:
        rescore.replay(calls, tmp_path / "out", {}, CFG)
    assert "fwd_mispairs" in str(e.value)


# --- the forced call a replay must not re-decide ------------------------------


def test_a_probe_absent_fail_keeps_its_forced_call_but_recomputes_its_penalty():
    """Both halves, because getting one right and the other wrong is invisible.

    `screen_one` forces `fail` for an amplicon whose probe has no site, past
    whatever `decide` returned, and keeps that reason. It does NOT force the
    penalty: `Call.penalty` is still `decide`'s scalar, which is the sum under
    `budget` and the worst single oligo under `serial`. An early version of the
    replay returned the row's own penalty here, so under `engine: serial` it
    reported 13.5 where a real rescreen reported 7.5 on 19 rows - with zero call
    disagreements, because the call was already pinned. Found by rescreening one
    archive for real and diffing, not by reading the code.
    """
    facts = {"A": {"chemistry": "hydrolysis_probe", "probe_len": 20}}
    row = {
        "assay_id": "A",
        "record_id": "R1",
        "call": "fail",
        "penalty": "13.5",
        "reason": "no probe site inside amplicon",
        "fwd_mispairs": "G:T@7,C:A@4",
        "rev_mispairs": "C:A@20",
        "probe_mispairs": "",
        "fwd_ambiguous": "0",
        "rev_ambiguous": "0",
        "probe_ambiguous": "",
        "probe_penalty": "",
    }
    call, reason, penalty = rescore.replay_row(row, facts, CFG)
    assert call == "fail"
    assert reason == "no probe site inside amplicon"
    # budget: the sum of both primers, recomputed, not the 13.5 carried in the row.
    # G:T@7 is mid-window (1.0), C:A@4 is 3'-window (3.0), C:A@20 is 5' (0.5).
    assert penalty == "4.5"

    serial, _, serial_penalty = rescore.replay_row(row, facts, _scoring(engine="serial"))
    assert serial == "fail"
    # The worst single oligo is the forward at 4.0, not the 4.5 the two sum to.
    assert serial_penalty == "4", "serial reports the worst single oligo"


@pytest.mark.parametrize("call", sorted(rescore.PASSTHROUGH_CALLS))
def test_a_search_layer_outcome_passes_through_untouched(call):
    """`no_amplicon` and `indeterminate` are not threshold decisions.

    No primer pair was found, or `too_ambiguous` fired. Re-deciding either from a
    footprint that was never scored would invent a verdict.
    """
    row = {
        "assay_id": "A",
        "record_id": "R1",
        "call": call,
        "penalty": "",
        "reason": "no forward site within 6 mismatches",
        "fwd_mispairs": "",
    }
    assert rescore.replay_row(row, {"A": {"chemistry": "conventional", "probe_len": None}}, CFG) == (
        call,
        row["reason"],
        "",
    )


# --- the positional weight curve (S2's shape, which config.yaml cannot express) ----


@pytest.mark.parametrize("d", range(1, 16))
def test_no_weight_spec_is_exactly_the_shipped_step_function(d):
    """The default path must BE the step function, not a reimplementation of it.

    An S0 replay has to go down one code path, not two, or the control that licenses
    the whole ladder would be comparing the harness against itself.
    """
    s = CFG["scoring"]
    w3, wmid = s["primer_3prime_window"], s["primer_mid_window"]
    if d <= w3:
        want = s["primer_3prime_penalty"]
    elif d <= w3 + wmid:
        want = s["primer_mid_penalty"]
    else:
        want = s["primer_5prime_penalty"]
    assert rescore.positional_weight(None, d, CFG) == want
    assert rescore.positional_weight({}, d, CFG) == want


def test_the_exponential_curve_halves_every_half_distance():
    spec = {"kind": "exponential", "w0": 3.0, "half_distance": 2.0}
    assert rescore.positional_weight(spec, 1, CFG) == pytest.approx(3.0)
    assert rescore.positional_weight(spec, 3, CFG) == pytest.approx(1.5)
    assert rescore.positional_weight(spec, 5, CFG) == pytest.approx(0.75)
    # A floor, so a long oligo's 5' end does not decay to free.
    floored = {**spec, "floor": 1.0}
    assert rescore.positional_weight(floored, 21, CFG) == pytest.approx(1.0)


def test_an_unknown_weight_kind_is_refused_rather_than_silently_ignored():
    with pytest.raises(SystemExit) as e:
        rescore.positional_weight({"kind": "logistic", "w0": 3.0, "half_distance": 2.0}, 1, CFG)
    assert "logistic" in str(e.value)


def test_a_curve_changes_the_penalty_but_identity_still_acts_only_in_the_3prime_window():
    """The window and the curve answer different questions and must not merge.

    `primer_3prime_window` says where the mispair effect is measurable (Kwok 1990,
    Stadhouders 2010); the curve says how the position penalty decays. A candidate
    that changed both at once would be two candidates.
    """
    cfg = _scoring(mispair_penalty={"G:T": 0.0})
    spec = {"kind": "exponential", "w0": 2.0, "half_distance": 4.0}
    # Inside the window: identity zeroes it, curve or no curve.
    inside = rescore.primer_score(rescore.parse_mispairs("G:T@2"), 0, cfg, spec)
    assert inside.penalty == 0.0
    # Outside: identity does not fire, so the curve alone sets the penalty.
    outside = rescore.primer_score(rescore.parse_mispairs("G:T@9"), 0, cfg, spec)
    assert outside.penalty == pytest.approx(2.0 * 2.0 ** (-8 / 4.0))
    # And the step function would have charged the 5'/mid band instead.
    assert (
        rescore.primer_score(rescore.parse_mispairs("G:T@9"), 0, cfg).penalty
        == CFG["scoring"]["primer_mid_penalty"]
    )


def test_a_strategy_carries_its_weight_spec_and_s2_declares_one():
    s2 = rescore.load_strategy(REPO / "strategies" / "s2-smooth-decay.yaml")
    assert s2.weight is not None
    assert s2.weight["kind"] == "exponential"
    assert s2.scoring == {}, "S2 varies the curve only; a scoring override too would be two candidates"
    # S0 must stay curve-less, or the control stops being a control.
    assert rescore.load_strategy(REPO / "strategies" / "s0-shipped.yaml").weight is None


# --- S3's probe switch: a `reduced` probe call is not a detection ------------------


def _probe_row(call="reduced", **over):
    row = {
        "assay_id": "A",
        "record_id": "R1",
        "call": call,
        "penalty": "2",
        "reason": "",
        "fwd_mispairs": "",
        "rev_mispairs": "",
        "probe_mispairs": "G:T@8",
        "fwd_ambiguous": "0",
        "rev_ambiguous": "0",
        "probe_ambiguous": "0",
        "probe_penalty": "2",
    }
    return {**row, **over}


def test_the_probe_switch_rewrites_reduced_to_fail_only_for_the_named_chemistries():
    """Priced as a rewrite because `drift.YearStats.detected` has no config key.

    `detected` is `detect + reduced` and `evaluable` is `detect + reduced + fail`, so
    moving a row from `reduced` to `fail` takes it out of the numerator and leaves the
    denominator alone. That is exactly what "not detected" means, which is why the
    rewrite is arithmetically identical to a per-chemistry `detected` rather than an
    approximation of one.
    """
    probe = {"A": {"chemistry": "hydrolysis_probe", "probe_len": 20}}
    conv = {"A": {"chemistry": "conventional", "probe_len": None}}

    call, reason, _ = rescore.replay_row(_probe_row(), probe, CFG, None, ("hydrolysis_probe", "mgb"))
    assert call == "fail"
    assert "reduced is not detected" in reason

    # A chemistry the switch does not name is untouched.
    assert rescore.replay_row(_probe_row(), probe, CFG, None, ("mgb",))[0] == "reduced"
    # And with no switch at all, nothing moves.
    assert rescore.replay_row(_probe_row(), probe, CFG)[0] == "reduced"
    # The switch cannot reach a conventional assay even when named, because that
    # assay's chemistry is not in the list. A conventional row carries no probe, so
    # its `reduced` comes from the primers: one mid-window mismatch on each, 1.0 + 1.0.
    conventional = _probe_row(fwd_mispairs="G:T@7", rev_mispairs="G:T@7", probe_mispairs="", probe_penalty="")
    assert rescore.replay_row(conventional, conv, CFG, None, ("hydrolysis_probe",)) == ("reduced", "", "2")


def test_the_probe_switch_leaves_detect_and_fail_alone():
    """It must move exactly one call class, or it is two candidates."""
    probe = {"A": {"chemistry": "hydrolysis_probe", "probe_len": 20}}
    for call, mispairs in (("detect", ""), ("fail", "G:T@8,G:T@9,G:T@10")):
        row = _probe_row(call=call, probe_mispairs=mispairs)
        got = rescore.replay_row(row, probe, CFG, None, ("hydrolysis_probe",))[0]
        assert got != "reduced"
        assert (
            "reduced is not detected"
            not in rescore.replay_row(row, probe, CFG, None, ("hydrolysis_probe",))[1]
        )


def test_a_strategy_naming_an_unknown_chemistry_is_refused(tmp_path):
    """The chemistry names are checked against the registry's own enum.

    A typo would silently switch nothing and the run would read as "the chemistry axis
    carries no signal", which is the opposite of the truth.
    """
    p = tmp_path / "s.yaml"
    p.write_text("name: x\nquestion: q\npredicts: p\nkill: k\nreduced_not_detected_for: [hydrolysis_prob]\n")
    with pytest.raises(SystemExit) as e:
        rescore.load_strategy(p)
    assert "hydrolysis_prob" in str(e.value)


def test_the_s3_strategies_on_disk_are_what_their_names_claim():
    s3a = rescore.load_strategy(REPO / "strategies" / "s3a-probe-reduced-not-detected.yaml")
    s3b = rescore.load_strategy(REPO / "strategies" / "s3b-conventional-terminal-is-reduced.yaml")
    both = rescore.load_strategy(REPO / "strategies" / "s3-both-switches.yaml")
    # One switch each, so "test each alone, then together" means what it says.
    assert s3a.reduced_not_detected_for == ("hydrolysis_probe", "mgb")
    assert s3a.scoring == {}
    assert s3b.reduced_not_detected_for == ()
    assert s3b.scoring == {"by_chemistry": {"conventional": {"terminal_mismatch_fails": False}}}
    # And the combination is exactly the union, not a third thing.
    assert both.reduced_not_detected_for == s3a.reduced_not_detected_for
    assert both.scoring == s3b.scoring
