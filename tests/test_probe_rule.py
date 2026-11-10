"""The probe rule: a probe is judged by HOW MANY mismatches it carries, per chemistry.

Decided 2026-11-10. It replaces `probe_center_penalty` / `probe_outer_penalty`, which
weighted a mismatch by which third of the probe it fell in. That rule was blind to
two things that decide what a probe mismatch costs:

* LENGTH. The central third of a 15-mer is 5 nt and of a 30-mer is 10 nt, at one price.
* CHEMISTRY. A standard hydrolysis probe (20-30 nt) loses 4-6 C of Tm to one mismatch
  and usually still reports, late; an MGB probe (12-18 nt) can lose 15-20 C and stops
  (Kutyavin et al. 2000, doi:10.1093/nar/28.2.655). Yao, Nellaker & Karlsson 2006
  (doi:10.1016/j.mcp.2006.03.003) measured both and found the standard probe the more
  tolerant, still giving signal with several mismatches.

Each test below is one step of the plan, in the order it was written.
"""

from __future__ import annotations

import pytest

from assaywatch.drift import reduced_not_detected_ids
from assaywatch.match import Site
from assaywatch.schema import Chemistry
from assaywatch.score import (
    OligoScore,
    ProbeKind,
    ProbeRule,
    decide,
    load_config,
    probe_kind,
    probe_rule_for,
    score_probe,
)

pytestmark = pytest.mark.fast

CFG = load_config()
STANDARD = ProbeRule(ProbeKind.standard, reduced_at=1, fail_at=2)
SHORT = ProbeRule(ProbeKind.short, reduced_at=1, fail_at=1)

PROBE = "CCAAGTGTCAGATGCAAGTCC"  # 21 nt, a plain hydrolysis probe's length


def site_with(*mismatch_positions: int) -> Site:
    """A probe site whose record differs from PROBE at exactly these positions."""
    window = list(PROBE)
    for pos in mismatch_positions:
        window[pos] = "A" if window[pos] != "A" else "C"
    return Site(0, len(PROBE), "+", tuple(mismatch_positions), "".join(window))


def clean_primer() -> OligoScore:
    return OligoScore(0.0, False, (), ())


def primer_with_penalty(penalty: float) -> OligoScore:
    return OligoScore(penalty, False, (10,), (10,))


# --- step 1 --------------------------------------------------------------------------


def test_a_perfectly_matched_standard_probe_is_ok():
    sc = score_probe(site_with(), PROBE, STANDARD)
    assert sc.verdict == "ok"
    assert sc.penalty == 0.0


# --- step 2 --------------------------------------------------------------------------


def test_one_mismatch_in_a_standard_probe_is_weak_wherever_it_sits():
    """Position no longer matters: the count does. Centre, edge and 3' end agree."""
    for pos in (0, 10, len(PROBE) - 1):
        assert score_probe(site_with(pos), PROBE, STANDARD).verdict == "weak", pos


def test_a_weak_probe_on_clean_primers_makes_the_call_reduced():
    ps = score_probe(site_with(10), PROBE, STANDARD)
    call, _, _ = decide(clean_primer(), clean_primer(), ps, CFG)
    assert call == "reduced"


def test_a_reduced_call_counts_as_detected_for_a_standard_hydrolysis_probe():
    """One probe mismatch is a Ct shift, not a miss, so it must stay in the numerator.

    `drift.reduced_not_detected_for` named `hydrolysis_probe` and `mgb` until
    2026-11-10. With it, one probe mismatch read as "this assay does not detect this
    record", which put the CDC H3 assay at the floor from 2016 and hid the drift that
    followed. `mgb` left with it: kept, it would count a long MGB probe's `reduced` as
    not detected and undo the length cut tested below.
    """
    assert reduced_not_detected_ids({"a": "hydrolysis_probe", "b": "mgb"}, CFG) == set()


# --- step 3 --------------------------------------------------------------------------


def test_two_mismatches_block_a_standard_probe_and_fail_the_call():
    ps = score_probe(site_with(3, 15), PROBE, STANDARD)
    assert ps.verdict == "blocked"
    call, _, _ = decide(clean_primer(), clean_primer(), ps, CFG)
    assert call == "fail"


# --- step 4 --------------------------------------------------------------------------


def test_one_mismatch_blocks_a_short_probe():
    ps = score_probe(site_with(10), PROBE, SHORT)
    assert ps.verdict == "blocked"
    call, _, _ = decide(clean_primer(), clean_primer(), ps, CFG)
    assert call == "fail"


def test_a_perfectly_matched_short_probe_is_ok():
    assert score_probe(site_with(), PROBE, SHORT).verdict == "ok"


# --- step 5 --------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("chemistry", "probe_len", "want"),
    [
        (Chemistry.hydrolysis_probe, 25, STANDARD),
        (Chemistry.mgb, 15, SHORT),
        (Chemistry.lna, 15, SHORT),
    ],
)
def test_the_shipped_config_builds_the_agreed_rule_for_each_probe_chemistry(chemistry, probe_len, want):
    assert probe_rule_for(chemistry, probe_len, CFG) == want


# --- step 5b: the label is not the mechanism --------------------------------------------


def test_an_mgb_probe_is_short_only_up_to_the_length_cut():
    """20 nt is the top of Kutyavin's MGB design range; the registry holds MGB probes to 32."""
    cut = CFG["scoring"]["short_probe_max_nt"]
    assert cut == 20
    assert probe_kind(Chemistry.mgb, cut, CFG) is ProbeKind.short
    assert probe_kind(Chemistry.mgb, cut + 1, CFG) is ProbeKind.standard


def test_a_long_mgb_probe_takes_the_standard_rule():
    """The Blooi 2013 Bsal probe is MGB and 32 nt. One mismatch must not fail it."""
    assert probe_rule_for(Chemistry.mgb, 32, CFG) == STANDARD


def test_a_short_plain_probe_is_still_standard():
    """Being short is not enough either: the short rule is about a stabilised probe.

    The registry has plain hydrolysis probes of 16-19 nt. Whether those tolerate a
    mismatch is its own question and no evidence was gathered on it; they keep the
    standard rule.
    """
    assert probe_kind(Chemistry.hydrolysis_probe, 16, CFG) is ProbeKind.standard


def test_each_probe_in_a_pool_is_judged_at_its_own_length():
    assert probe_rule_for(Chemistry.mgb, 18, CFG).kind is ProbeKind.short
    assert probe_rule_for(Chemistry.mgb, 24, CFG).kind is ProbeKind.standard


def test_the_real_blooi_entry_is_reduced_not_failed_by_one_probe_mismatch():
    row = "Batrachochytrium_salamandrivorans_ITS1_5_8S_Blooi_2013__probe_center"
    fixtures = Path(__file__).parent / "fixtures"
    records = dict(read_fasta(fixtures / "records.fasta"))
    assay = Assay.model_validate(
        yaml.safe_load((ROOT / "registry" / f"{row.split('__')[0]}.yaml").read_text())
    )
    assert str(assay.chemistry) == "mgb"
    assert len(assay.oligos.probe.matching_seq) == 32
    assert screen_record(assay, row, records[row], CFG).call == "reduced"


def test_a_rule_that_fails_before_it_reduces_is_refused():
    with pytest.raises(ValueError, match="fail_at"):
        ProbeRule(ProbeKind.standard, reduced_at=2, fail_at=1)


def test_a_rule_that_reduces_at_zero_mismatches_is_refused():
    with pytest.raises(ValueError, match="reduced_at"):
        ProbeRule(ProbeKind.standard, reduced_at=0, fail_at=1)


# --- the probe is a gate, not part of the primers' budget -------------------------------


def test_a_weak_probe_does_not_add_to_the_primer_penalty():
    """Primers at exactly `detect_max` plus a weak probe is `reduced`, not `fail`.

    Under the old rule the probe's penalty joined the primers' sum, so a probe defect
    (which costs signal) traded against a primer defect (which costs amplification).
    They are different mechanisms: the primers decide whether there is product, and
    the probe decides whether the product is seen. The call is the worse of the two.
    """
    at_detect_max = primer_with_penalty(CFG["scoring"]["detect_max"])
    ps = score_probe(site_with(10), PROBE, STANDARD)
    call, _, _ = decide(at_detect_max, clean_primer(), ps, CFG)
    assert call == "reduced"


def test_an_ok_probe_cannot_rescue_failing_primers():
    over = primer_with_penalty(CFG["scoring"]["reduced_max"] + 1)
    ps = score_probe(site_with(), PROBE, STANDARD)
    call, _, _ = decide(over, clean_primer(), ps, CFG)
    assert call == "fail"


def test_the_serial_engine_reads_the_probe_verdict_too():
    serial = {**CFG, "scoring": {**CFG["scoring"], "engine": "serial"}}
    ps = score_probe(site_with(3, 15), PROBE, STANDARD)
    call, reason, _ = decide(clean_primer(), clean_primer(), ps, serial)
    assert call == "fail"
    assert "probe blocked" in reason


def test_the_best_probe_site_is_still_the_one_with_fewest_mismatches():
    """`screen_one` picks a probe site by `min(penalty)`; the penalty is the count."""
    one = score_probe(site_with(10), PROBE, STANDARD)
    two = score_probe(site_with(3, 15), PROBE, STANDARD)
    assert one.penalty < two.penalty


# --- end to end, through the screen, on a real standard-probe entry ---------------------

from pathlib import Path  # noqa: E402

import yaml  # noqa: E402

from assaywatch.fasta import read_fasta  # noqa: E402
from assaywatch.iupac import expand, reverse_complement  # noqa: E402
from assaywatch.schema import Assay  # noqa: E402
from assaywatch.score import screen_record  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
STANDARD_ENTRY = "Avipoxvirus_4b_Farias_2010"  # chemistry: hydrolysis_probe


def _record_with_probe_mismatches(n: int) -> tuple[Assay, str]:
    """A record the entry's primers match exactly, its probe site edited at `n` places."""
    assay = Assay.model_validate(yaml.safe_load((ROOT / "registry" / f"{STANDARD_ENTRY}.yaml").read_text()))
    assert str(assay.chemistry) == "hydrolysis_probe"
    # `expand(...)[0]` picks one concrete sequence where an oligo is degenerate.
    fwd = expand(assay.oligos.forward.matching_seq)[0]
    rev = expand(assay.oligos.reverse.matching_seq)[0]
    probe = list(expand(assay.oligos.probe.matching_seq)[0])
    for pos in (len(probe) // 2, 2)[:n]:
        probe[pos] = "A" if probe[pos] != "A" else "C"
    inner = assay.amplicon_bp - len(fwd) - len(rev) - len(probe)
    left, right = "ACGT" * (inner // 8 + 1), "TGCA" * (inner // 8 + 1)
    left, right = left[: inner // 2], right[: inner - inner // 2]
    flank = "GATTACA" * 20
    return assay, flank + fwd + left + "".join(probe) + right + reverse_complement(rev) + flank


@pytest.mark.parametrize(("n_mismatches", "want"), [(0, "detect"), (1, "reduced"), (2, "fail")])
def test_a_standard_probe_entry_screens_to_the_agreed_call(n_mismatches, want):
    assay, record = _record_with_probe_mismatches(n_mismatches)
    call = screen_record(assay, "rec", record, CFG)
    assert call.call == want, call.reason
    assert call.forward.penalty == 0 and call.reverse.penalty == 0, (
        "the primers are clean; the probe alone decided"
    )
