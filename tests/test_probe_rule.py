"""The probe rule: a probe mismatch is priced by the melting temperature it costs.

Decided 2026-11-10, second attempt. The first attempt the same day counted mismatches
(one is `weak`, two are `blocked`, a short stabilised probe is blocked at one). Replayed
against the documented cases it traded one catch for another, and both hinged on ONE
mismatch at position 15 of a standard probe: T:G in the CDC H3 assay, G:A in Ward 2004.
A count cannot tell those apart. What tells them apart is which bases are mispaired and
how long the probe is, and both are what a nearest-neighbour Tm sees.

So the probe is priced by its predicted loss of Tm on the record's site against a
perfect site (`thermo.duplex_tm`: SantaLucia & Hicks 2004, Allawi & SantaLucia
mismatch terms), under the reaction conditions in `config.yaml`:

    loss <  weak_dtm ............ `ok`
    weak_dtm <= loss < block_dtm  `weak`     the call is at best `reduced`
    loss >= block_dtm ........... `blocked`  the call is `fail`
    loss cannot be computed ..... `blocked`  (adjacent mismatches have no measured term)

The numbers in these tests are the model's, computed for the probe below at the
shipped conditions and written down here so that a change in either shows.

ON A BRANCH, UNMERGED (maintainer decision, 2026-11-10). Two things are owed before
it merges: a cut for minor-groove-binder probes, which the nearest-neighbour tables do
not model, and one documented case that neither threshold has seen.
"""

from __future__ import annotations

import pytest

from assaywatch.drift import reduced_not_detected_ids
from assaywatch.match import Site
from assaywatch.score import OligoScore, ProbeRule, decide, load_config, probe_rule, score_probe

pytestmark = pytest.mark.fast

CFG = load_config()
CONDITIONS = CFG["thermo_conditions"]
RULE = ProbeRule(weak_dtm=2.0, block_dtm=5.0)

PROBE = "CCAAGTGTCAGATGCAAGTCC"  # 21 nt, a plain hydrolysis probe's length; Tm 64.0 C here
# What one mismatch at each of these positions costs this probe, in degrees C:
END, NEAR_END, OFF_CENTRE, CENTRE = 0, 1, 15, 10  # 1.9, 8.1, 4.2, 5.8


def site_with(*mismatch_positions: int) -> Site:
    """A probe site whose record differs from PROBE at exactly these positions."""
    window = list(PROBE)
    for pos in mismatch_positions:
        window[pos] = "A" if window[pos] != "A" else "C"
    return Site(0, len(PROBE), "+", tuple(mismatch_positions), "".join(window))


def probe(*mismatch_positions: int) -> OligoScore:
    return score_probe(site_with(*mismatch_positions), PROBE, RULE, CONDITIONS)


def clean_primer() -> OligoScore:
    return OligoScore(0.0, False, (), ())


def primer_with_penalty(penalty: float) -> OligoScore:
    return OligoScore(penalty, False, (10,), (10,))


# --- step 1: no mismatch, no loss ---------------------------------------------------------


def test_a_perfectly_matched_probe_is_ok():
    sc = probe()
    assert sc.verdict == "ok"
    assert sc.penalty == 0.0


# --- step 2: the same count, three verdicts ------------------------------------------------


def test_one_mismatch_is_priced_by_where_it_sits_and_what_it_is():
    """The point of the rule. One mismatch each, and the model's loss decides."""
    assert probe(END).verdict == "ok"  # 1.9 C: the last base of a duplex frays anyway
    assert probe(OFF_CENTRE).verdict == "weak"  # 4.2 C
    assert probe(CENTRE).verdict == "blocked"  # 5.8 C
    assert probe(NEAR_END).verdict == "blocked"  # 8.1 C: one base in is not the end


def test_the_mispair_decides_as_well_as_the_position():
    """Position 15 again, two different record bases. A count would call these the same."""
    costs = {}
    for base in "ACGT":
        if base == PROBE[OFF_CENTRE]:
            continue
        window = PROBE[:OFF_CENTRE] + base + PROBE[OFF_CENTRE + 1 :]
        site = Site(0, len(PROBE), "+", (OFF_CENTRE,), window)
        costs[base] = score_probe(site, PROBE, RULE, CONDITIONS).verdict
    assert len(set(costs.values())) > 1, costs


def test_a_weak_probe_on_clean_primers_makes_the_call_reduced():
    call, _, _ = decide(clean_primer(), clean_primer(), probe(OFF_CENTRE), CFG)
    assert call == "reduced"


def test_a_blocked_probe_fails_the_call():
    call, reason, _ = decide(clean_primer(), clean_primer(), probe(CENTRE), CFG)
    assert call == "fail"
    assert "probe blocked" in reason


def test_a_reduced_call_counts_as_detected_for_a_hydrolysis_probe():
    """A weak probe is a Ct shift, not a miss, so it stays in the numerator.

    `drift.reduced_not_detected_for` named `hydrolysis_probe` and `mgb` until
    2026-11-10. With it, one probe mismatch read as "this assay does not detect this
    record", which put the CDC H3 assay at the floor from 2016 and hid the drift that
    followed.
    """
    assert reduced_not_detected_ids({"a": "hydrolysis_probe", "b": "mgb"}, CFG) == set()


# --- step 3: losses add up, and what cannot be priced is not waved through ------------------


def test_two_mismatches_that_are_each_mild_block_together():
    assert probe(END).verdict == "ok" and probe(OFF_CENTRE).verdict == "weak"
    assert probe(END, OFF_CENTRE).verdict == "blocked"  # 1.9 + 4.2, and the model gives 6 or more


def test_adjacent_mismatches_cannot_be_priced_and_are_blocked():
    """The tables hold a mismatch flanked by matches. Two in a row have no measured
    term, `duplex_tm` returns None rather than an optimistic number, and a probe with
    two adjacent mismatches is not one to give the benefit of the doubt."""
    assert probe(10, 11).verdict == "blocked"


def test_the_thresholds_are_inclusive():
    """A loss of exactly `weak_dtm` is weak, and of exactly `block_dtm` is blocked."""
    assert RULE.verdict(1.99) == "ok"
    assert RULE.verdict(2.0) == "weak"
    assert RULE.verdict(4.99) == "weak"
    assert RULE.verdict(5.0) == "blocked"
    assert RULE.verdict(None) == "blocked"


# --- step 4: length is in the model, so no length cut is needed -----------------------------


def test_a_short_probe_loses_more_to_the_same_mismatch_than_a_long_one():
    """Why the count rule needed a length cut and this one does not."""
    short = "CAAGTGTCAGATGC"  # 14 nt
    long = "GATTACA" + short + "GATTACA" + "CCGTA"  # 33 nt, the same 14 bases in the middle

    def loss(oligo: str, pos: int) -> float:
        from assaywatch.thermo import duplex_tm

        window = oligo[:pos] + ("A" if oligo[pos] != "A" else "C") + oligo[pos + 1 :]
        tm, perfect, _ = duplex_tm(oligo, window, CFG)
        return perfect - tm

    assert loss(short, 7) > loss(long, 14) + 2.0  # the same base, the same mispair


# --- step 5: the rule comes from config, whole ----------------------------------------------


def test_the_shipped_config_builds_the_agreed_rule():
    assert probe_rule(CFG) == RULE


def test_a_rule_that_blocks_before_it_weakens_is_refused():
    with pytest.raises(ValueError, match="block_dtm"):
        ProbeRule(weak_dtm=5.0, block_dtm=2.0)


def test_a_rule_that_calls_no_loss_weak_is_refused():
    with pytest.raises(ValueError, match="weak_dtm"):
        ProbeRule(weak_dtm=0.0, block_dtm=5.0)


def test_setting_the_two_equal_removes_the_weak_band():
    rule = ProbeRule(weak_dtm=3.0, block_dtm=3.0)
    assert rule.verdict(2.9) == "ok" and rule.verdict(3.0) == "blocked"


# --- the probe is a gate, not part of the primers' budget -------------------------------


def test_a_weak_probe_does_not_add_to_the_primer_penalty():
    """Primers at exactly `detect_max` plus a weak probe is `reduced`, not `fail`.

    Under the old rule the probe's penalty joined the primers' sum, so a probe defect
    (which costs signal) traded against a primer defect (which costs amplification).
    They are different mechanisms: the primers decide whether there is product, and
    the probe decides whether the product is seen. The call is the worse of the two.
    """
    at_detect_max = primer_with_penalty(CFG["scoring"]["detect_max"])
    ps = probe(OFF_CENTRE)
    call, _, _ = decide(at_detect_max, clean_primer(), ps, CFG)
    assert call == "reduced"


def test_an_ok_probe_cannot_rescue_failing_primers():
    over = primer_with_penalty(CFG["scoring"]["reduced_max"] + 1)
    ps = probe()
    call, _, _ = decide(over, clean_primer(), ps, CFG)
    assert call == "fail"


def test_the_serial_engine_reads_the_probe_verdict_too():
    serial = {**CFG, "scoring": {**CFG["scoring"], "engine": "serial"}}
    ps = probe(CENTRE)
    call, reason, _ = decide(clean_primer(), clean_primer(), ps, serial)
    assert call == "fail"
    assert "probe blocked" in reason


def test_the_best_probe_site_is_still_the_one_with_fewest_mismatches():
    """`screen_one` picks a probe site by `min(penalty)`; the penalty is still the count."""
    one = probe(CENTRE)
    two = probe(3, 15)
    assert one.penalty < two.penalty


# --- end to end, through the screen, on a real hydrolysis-probe entry ------------------------

from pathlib import Path  # noqa: E402

import yaml  # noqa: E402

from assaywatch.iupac import expand, reverse_complement  # noqa: E402
from assaywatch.schema import Assay  # noqa: E402
from assaywatch.score import screen_record  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
ENTRY = "Avipoxvirus_4b_Farias_2010"  # chemistry: hydrolysis_probe; probe CAGCGTGATGAAGACGCTAA


def _record_with_probe_mismatch_at(*positions: int) -> tuple[Assay, str]:
    """A record the entry's primers match exactly, its probe site edited at `positions`."""
    assay = Assay.model_validate(yaml.safe_load((ROOT / "registry" / f"{ENTRY}.yaml").read_text()))
    assert str(assay.chemistry) == "hydrolysis_probe"
    # `expand(...)[0]` picks one concrete sequence where an oligo is degenerate.
    fwd = expand(assay.oligos.forward.matching_seq)[0]
    rev = expand(assay.oligos.reverse.matching_seq)[0]
    site = list(expand(assay.oligos.probe.matching_seq)[0])
    assert "".join(site) == "CAGCGTGATGAAGACGCTAA", "the losses below were computed for this probe"
    for pos in positions:
        site[pos] = "A" if site[pos] != "A" else "C"
    inner = assay.amplicon_bp - len(fwd) - len(rev) - len(site)
    left, right = "ACGT" * (inner // 8 + 1), "TGCA" * (inner // 8 + 1)
    left, right = left[: inner // 2], right[: inner - inner // 2]
    flank = "GATTACA" * 20
    return assay, flank + fwd + left + "".join(site) + right + reverse_complement(rev) + flank


@pytest.mark.parametrize(
    ("positions", "want"),
    [
        ((), "detect"),
        ((0,), "detect"),  # 1.3 C lost
        ((10,), "reduced"),  # 3.4 C
        ((3,), "fail"),  # 9.7 C
        ((0, 13), "reduced"),  # 1.3 and 1.8 apart: each ok alone, weak together
    ],
)
def test_a_hydrolysis_probe_entry_screens_to_the_call_its_tm_loss_gives(positions, want):
    assay, record = _record_with_probe_mismatch_at(*positions)
    call = screen_record(assay, "rec", record, CFG)
    assert call.call == want, call.reason
    assert call.forward.penalty == 0 and call.reverse.penalty == 0, (
        "the primers are clean; the probe alone decided"
    )
