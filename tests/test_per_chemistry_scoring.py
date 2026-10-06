"""Tests for per-chemistry scoring overrides.

The point of the mechanism is that one penalty table was being applied to 142
conventional assays and 21 probe-based ones, when conventional PCR tolerates
mismatches far better than a hydrolysis probe does. It ships inert, so the two
things worth testing are:

1. with no overrides, nothing whatsoever changes - not "gives the same answers"
   but takes the identical code path, which is what makes that safe to believe;
2. with overrides, they reach the scoring functions AND a typo cannot pass
   silently, because an override that fails to apply leaves a run looking
   recalibrated when it is not.
"""

from __future__ import annotations

import importlib.util
import random
from pathlib import Path

import pytest
import yaml
from test_score import ASSAYS, RECORDS

from assaywatch.assemblies import extract_loci
from assaywatch.iupac import reverse_complement
from assaywatch.schema import Chemistry
from assaywatch.score import (
    RESOLVED,
    check_chemistry_overrides,
    config_for,
    load_config,
    max_mismatches_searched,
    oligo_pools,
    scoring_for,
    screen_record,
)
from assaywatch.validate import load_assay

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("indel_check", ROOT / "scripts" / "indel_check.py")
indel_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(indel_check)

# A conventional, probe-less assay with fixtures: the chemistry the shipped
# overrides would most plausibly relax.
ANNIS = "CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004"
SWAP = {"A": "C", "C": "A", "G": "T", "T": "G"}  # transversions: never a silent no-op


def write_config(tmp_path, overrides) -> dict:
    """The shipped config with `scoring.by_chemistry` replaced, loaded."""
    cfg = yaml.safe_load((load_config.__globals__["DEFAULT_CONFIG"]).read_text())
    cfg["scoring"]["by_chemistry"] = overrides
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(cfg))
    return load_config(path)


def test_the_shipped_config_overrides_nothing():
    """If this fails, somebody set a threshold by eye. config.yaml says not to
    without a validation run behind it."""
    cfg = load_config()
    assert cfg["scoring"].get("by_chemistry") == {}
    assert RESOLVED not in cfg


def test_without_overrides_every_chemistry_takes_the_identical_path():
    """Not "the same numbers" - the same object.

    Returning cfg itself is what makes "behaviour is unchanged" a fact about the
    code rather than a claim about its output.
    """
    cfg = load_config()
    for chem in Chemistry:
        assert config_for(chem, cfg) is cfg, chem
        assert scoring_for(chem, cfg) is cfg["scoring"], chem


def test_an_override_replaces_only_its_own_key_for_only_its_own_chemistry(tmp_path):
    cfg = write_config(tmp_path, {"conventional": {"terminal_mismatch_fails": False}})

    conv = scoring_for(Chemistry.conventional, cfg)
    assert conv["terminal_mismatch_fails"] is False
    # Every other key is inherited from the base block, not dropped.
    assert conv["primer_3prime_penalty"] == cfg["scoring"]["primer_3prime_penalty"]
    assert conv["detect_max"] == cfg["scoring"]["detect_max"]

    # And no other chemistry moved.
    for chem in (Chemistry.mgb, Chemistry.hydrolysis_probe, Chemistry.rpa):
        assert scoring_for(chem, cfg)["terminal_mismatch_fails"] is True, chem
        assert config_for(chem, cfg) is cfg, chem


def test_an_override_does_not_mutate_the_base_block(tmp_path):
    """The base block is shared by every chemistry that does not override."""
    cfg = write_config(tmp_path, {"mgb": {"probe_center_penalty": 9.0}})
    scoring_for(Chemistry.mgb, cfg)
    assert cfg["scoring"]["probe_center_penalty"] == 2.0


def test_overrides_actually_change_a_call(tmp_path):
    """The mechanism is worthless if the numbers never reach the scorer.

    Scored through the public entry point, because that is the only place
    resolution happens and the risk being tested is that it happens nowhere.

    The transition asserted here is the whole argument for per-chemistry
    scoring in one record. A single 3'-terminal mismatch on a conventional
    assay scores a penalty of 3.0, which is exactly `reduced_max` - so it is
    `reduced` on the numbers, and only `terminal_mismatch_fails` pushes it to
    `fail`. That rule is qPCR-grade, and this assay is endpoint PCR, where the
    lost yield is usually still a band. Relaxing it for conventional chemistry
    alone turns the call back into `reduced` without touching the penalty.

    Both legs are asserted unconditionally and the strict leg is asserted
    first: if the fixture ever stops producing a terminal mismatch, this fails
    loudly instead of passing while testing nothing.
    """
    assay = next(
        a
        for a in (load_assay(p) for p in sorted((ROOT / "registry").glob("*.yaml")))
        if a.chemistry == Chemistry.conventional and a.oligos.probe is None and a.oligos.forward.seq.isalpha()
    )
    fwd = assay.oligos.forward.matching_seq
    rev = assay.oligos.reverse.matching_seq
    # One substitution at the forward primer's 3'-terminal base, nothing else.
    broken = fwd[:-1] + SWAP[fwd[-1]]
    record = "TTTT" + broken + "ACGT" * 30 + reverse_complement(rev) + "TTTT"

    before = screen_record(
        assay, "r1", record, write_config(tmp_path, {})
    )  # explicit: not whatever config.yaml ships
    assert before.call == "fail", (assay.id, before.call, before.penalty)
    assert before.penalty == 3.0, before.penalty

    loose = write_config(tmp_path, {"conventional": {"terminal_mismatch_fails": False}})
    after = screen_record(assay, "r1", record, loose)
    assert after.call == "reduced", (after.call, after.penalty)
    # The penalty is untouched: only the rule that overrode it changed.
    assert after.penalty == before.penalty


def test_a_misspelled_chemistry_is_a_hard_error(tmp_path):
    """The failure this prevents is silent: the run succeeds, the numbers are
    the old ones, and the report looks recalibrated."""
    cfg = yaml.safe_load((load_config.__globals__["DEFAULT_CONFIG"]).read_text())
    cfg["scoring"]["by_chemistry"] = {"conventinoal": {"terminal_mismatch_fails": False}}
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(cfg))
    with pytest.raises(ValueError, match="not a chemistry in the schema"):
        load_config(path)


def test_a_misspelled_scoring_key_is_a_hard_error(tmp_path):
    cfg = yaml.safe_load((load_config.__globals__["DEFAULT_CONFIG"]).read_text())
    cfg["scoring"]["by_chemistry"] = {"conventional": {"primer_3prime_penalties": 2.0}}
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(cfg))
    with pytest.raises(ValueError, match="not a key in `scoring`"):
        load_config(path)


def test_the_checker_reports_every_problem_at_once():
    """A config with three typos should not need three runs to fix."""
    cfg = {
        "scoring": {
            "detect_max": 1.0,
            "by_chemistry": {
                "nonsense": {"detect_max": 2.0},
                "mgb": {"detetc_max": 2.0, "also_wrong": 1},
            },
        }
    }
    problems = check_chemistry_overrides(cfg)
    assert len(problems) == 3, problems
    assert any("nonsense" in p for p in problems)
    assert any("detetc_max" in p for p in problems)
    assert any("also_wrong" in p for p in problems)


def test_a_non_mapping_is_rejected_rather_than_ignored():
    assert check_chemistry_overrides({"scoring": {"by_chemistry": ["conventional"]}})
    assert check_chemistry_overrides({"scoring": {"a": 1, "by_chemistry": {"mgb": 3.0}}})


def test_an_empty_or_null_override_is_allowed():
    """Writing a chemistry down with nothing under it is a legitimate way to
    record "considered, deliberately unchanged"."""
    cfg = {"scoring": {"detect_max": 1.0, "by_chemistry": {"mgb": None, "rpa": {}}}}
    assert check_chemistry_overrides(cfg) == []
    assert scoring_for(Chemistry.mgb, cfg) is cfg["scoring"]
    assert scoring_for(Chemistry.rpa, cfg) is cfg["scoring"]


def test_resolution_is_precomputed_once_for_overridden_chemistries(tmp_path):
    """Resolution happens per record, so it must not allocate per record."""
    cfg = write_config(tmp_path, {"conventional": {"detect_max": 2.0}})
    assert RESOLVED in cfg
    assert set(cfg[RESOLVED]) == {"conventional"}
    first = config_for(Chemistry.conventional, cfg)
    assert config_for(Chemistry.conventional, cfg) is first
    assert first["scoring"]["detect_max"] == 2.0
    assert first["amplicon"] == cfg["amplicon"]  # the rest of the config survives


def test_a_hand_built_config_without_precomputation_still_resolves():
    """Tests and scripts build config dicts by hand; they must not silently get
    the base numbers."""
    cfg = {"scoring": {"detect_max": 1.0, "by_chemistry": {"mgb": {"detect_max": 5.0}}}}
    assert RESOLVED not in cfg
    assert config_for(Chemistry.mgb, cfg)["scoring"]["detect_max"] == 5.0
    assert config_for(Chemistry.conventional, cfg) is cfg


# --------------------------------------------------------------------------
# Every consumer of the scoring block has to see the override, not only
# `screen_one`. Three of them read `cfg["scoring"]` themselves, and each was
# found by checking whether it did.
# --------------------------------------------------------------------------


def _random_dna(n, seed):
    rng = random.Random(seed)
    return "".join(rng.choice("ACGT") for _ in range(n))


def test_max_mismatches_searched_is_the_largest_budget_any_chemistry_may_use():
    assert max_mismatches_searched({"scoring": {}}) == 6  # the default, as in screen_one
    assert max_mismatches_searched({"scoring": {"max_mismatches_searched": 5}}) == 5
    assert max_mismatches_searched({"scoring": {"max_mismatches_searched": 5, "by_chemistry": None}}) == 5

    # The largest override is LAST, so a version that looked only at the first one or two
    # (or the last) overrides would not find it by luck of dict order.
    raised = {
        "scoring": {
            "max_mismatches_searched": 5,
            "by_chemistry": {
                "mgb": {"detect_max": 2.0},  # an override that says nothing about the budget
                "rpa": None,
                "hydrolysis_probe": {"max_mismatches_searched": 7},
                "conventional": {"max_mismatches_searched": 9},
            },
        }
    }
    assert max_mismatches_searched(raised) == 9
    reordered = {
        "scoring": {
            **raised["scoring"],
            "by_chemistry": dict(reversed(raised["scoring"]["by_chemistry"].items())),
        }
    }
    assert max_mismatches_searched(reordered) == 9


def test_an_override_below_the_base_never_lowers_the_search_budget():
    """Chemistries with no override still search at the base budget, and the
    pre-cut serves all of them."""
    cfg = {"scoring": {"max_mismatches_searched": 6, "by_chemistry": {"mgb": {"max_mismatches_searched": 4}}}}
    assert max_mismatches_searched(cfg) == 6


def _annis_site_with_forward_mismatches(n):
    """Annis's amplicon with `n` transversions spread over the forward primer.

    Seven or eight is one or two over the shipped budget of six, so only a run whose
    override raises the budget can see the site at all.
    """
    assay = ASSAYS[ANNIS]
    fwd = assay.oligos.forward.matching_seq
    perfect = RECORDS[f"{ANNIS}__perfect"]
    i = perfect.index(fwd)
    site = list(perfect)
    offsets = list(range(0, len(fwd) - 2, 2))[:n]
    assert len(offsets) == n
    for offset in offsets:
        site[i + offset] = SWAP[site[i + offset]]
    return assay, "".join(site)


def _genome_around(site, pairs, strict):
    """A small genome holding `site` whose flanks have no chance window at the shipped budget.

    A random flank can hold a site within six mismatches that faces the real reverse site
    and keeps a window of its own, which would make the "the shipped budget cannot see
    this" leg fail for a reason that has nothing to do with the code. Flanks are searched
    for ones that do not (the seeds were once hard-coded and happened to work).
    """
    for seed in range(1, 60):
        contig = [("c1", _random_dna(1500, seed) + site + _random_dna(1500, seed + 1000))]
        if extract_loci(contig, pairs, strict)[1] == 0:
            return contig
    raise AssertionError("no flank without a chance window in 59 tries")


@pytest.mark.parametrize("mismatches", [7, 8])
def test_the_assembly_precut_keeps_a_site_exactly_at_the_override_budget(tmp_path, mismatches):
    """`extract_loci` has no assay and so no chemistry; it runs once per genome and has to
    search at the widest budget any chemistry will use. Searching at the base budget cut a
    window out of the genome that `screen_record` would have scored under the override -
    the cut genome then reported `no_amplicon` for a site the whole genome screens as a call.

    Tested at the budget exactly (a site needing `mismatches` kept at a budget of
    `mismatches`, dropped at one less), so a pre-cut that is one short passes nothing.
    """
    assay, site = _annis_site_with_forward_mismatches(mismatches)
    pairs = [(assay.oligos.forward.matching_seq, assay.oligos.reverse.matching_seq)]
    strict = write_config(tmp_path, {})
    contig = _genome_around(site, pairs, strict)
    exactly = write_config(tmp_path, {"conventional": {"max_mismatches_searched": mismatches}})
    one_short = write_config(tmp_path, {"conventional": {"max_mismatches_searched": mismatches - 1}})

    assert screen_record(assay, "g", contig[0][1], strict).call == "no_amplicon"
    assert extract_loci(contig, pairs, one_short)[1] == 0
    cut, n = extract_loci(contig, pairs, exactly)
    assert n == 1
    whole = screen_record(assay, "g", contig[0][1], exactly)
    assert whole.call != "no_amplicon", "the fixture no longer produces a site the override scores"
    scored_cut = screen_record(assay, "g", cut, exactly)
    assert (scored_cut.call, scored_cut.penalty, scored_cut.amplicon_bp) == (
        whole.call,
        whole.penalty,
        whole.amplicon_bp,
    )


def test_the_precut_uses_the_widest_budget_of_any_chemistry_not_just_the_assays_own(tmp_path):
    """The pre-cut sees primer pairs, not assays, so a budget raised for ANOTHER chemistry
    still has to keep the window: the genome is cut once for all of them. (Screening then
    applies each assay's own budget, so a window kept for a different chemistry is harmless.)"""
    assay, site = _annis_site_with_forward_mismatches(8)
    pairs = [(assay.oligos.forward.matching_seq, assay.oligos.reverse.matching_seq)]
    contig = _genome_around(site, pairs, write_config(tmp_path, {}))
    only_probes = write_config(tmp_path, {"hydrolysis_probe": {"max_mismatches_searched": 8}})
    assert extract_loci(contig, pairs, only_probes)[1] == 1


def _annis_record_failing_on_a_deleted_forward_base_and_a_terminal_reverse_mismatch():
    """Forward primer with one deleted base, reverse primer with a 3'-terminal
    transversion. Ungapped it is `fail` under any rules (penalty 4.5). With the
    deletion forgiven it is a single terminal mismatch, penalty 3.0: rescued only
    where a terminal mismatch does not fail on its own."""
    assay = ASSAYS[ANNIS]
    rec = RECORDS[f"{ANNIS}__perfect"]
    fi = rec.index(assay.oligos.forward.matching_seq)
    rec = rec[: fi + 2] + rec[fi + 3 :]
    ri = rec.index(reverse_complement(assay.oligos.reverse.matching_seq))
    return assay, rec[:ri] + SWAP[rec[ri]] + rec[ri + 1 :]


def test_indel_check_fail_is_judged_under_the_chemistrys_own_rules(tmp_path):
    """Rows come from `Call.as_row()`, as they do from the screened archives, so the
    columns indel_check reads are the columns the screener writes."""
    assay, rec = _annis_record_failing_on_a_deleted_forward_base_and_a_terminal_reverse_mismatch()
    relaxed = write_config(tmp_path, {"conventional": {"terminal_mismatch_fails": False}})
    # An explicit empty override block, not the shipped config: the day the documented
    # candidate override is enabled in config.yaml these tests must still mean what they say.
    strict_cfg = write_config(tmp_path, {})

    rows = {}
    for label, cfg in (("strict", strict_cfg), ("loose", relaxed)):
        call = screen_record(assay, "r", rec, cfg)
        # A fail under both, so the rescue question is live under both.
        assert (call.call, call.penalty) == ("fail", 4.5), label
        rows[label] = call.as_row()

    strict = indel_check.check_fail(assay, rows["strict"], rec, strict_cfg)
    loose = indel_check.check_fail(assay, rows["loose"], rec, relaxed)
    assert strict["penalty_without_indels"] == loose["penalty_without_indels"] == 3.0
    assert strict["rescued_if_indel_forgiven"] is False
    assert loose["rescued_if_indel_forgiven"] is True


def test_indel_check_ignores_an_override_for_another_chemistry(tmp_path):
    assay, rec = _annis_record_failing_on_a_deleted_forward_base_and_a_terminal_reverse_mismatch()
    other = write_config(tmp_path, {"mgb": {"terminal_mismatch_fails": False}})
    row = screen_record(assay, "r", rec, other).as_row()
    assert indel_check.check_fail(assay, row, rec, other)["rescued_if_indel_forgiven"] is False


def _annis_reverse_with_deleted_base(seq_from_3prime_end):
    """The Annis amplicon with one base deleted from the reverse primer's site,
    `seq_from_3prime_end` bases in from the primer's 3' end."""
    assay = ASSAYS[ANNIS]
    rec = RECORDS[f"{ANNIS}__perfect"]
    ri = rec.index(reverse_complement(assay.oligos.reverse.matching_seq))
    k = ri + seq_from_3prime_end
    return assay, rec[:k] + rec[k + 1 :]


def test_indel_check_missing_labels_the_indel_with_the_chemistrys_3prime_window(tmp_path):
    """The deletion lies 4 bases from the 3' end: inside the shipped 5-base window,
    outside a 2-base one set for conventional PCR."""
    assay, rec = _annis_reverse_with_deleted_base(2)
    narrow = write_config(tmp_path, {"conventional": {"primer_3prime_window": 2}})

    strict_cfg = write_config(tmp_path, {})
    base = indel_check.check_missing(assay, {}, rec, "no_reverse", strict_cfg, max_cost=2)
    over = indel_check.check_missing(assay, {}, rec, "no_reverse", narrow, max_cost=2)
    assert base is not None and over is not None
    assert base["indels_from_3prime"] == over["indels_from_3prime"] == "4"
    assert base["indel_in_3prime_window"] is True
    assert over["indel_in_3prime_window"] is False


def test_indel_check_missing_finds_its_partner_within_the_chemistrys_budget(tmp_path):
    """The partner search was hard-coded to six mismatches, so a partner the
    screen had matched at seven under a raised budget was invisible to it."""
    assay, rec = _annis_site_with_forward_mismatches(7)
    ri = rec.index(reverse_complement(assay.oligos.reverse.matching_seq))
    rec = rec[: ri + 2] + rec[ri + 3 :]
    wide = write_config(tmp_path, {"conventional": {"max_mismatches_searched": 8}})

    assert (
        indel_check.check_missing(assay, {}, rec, "no_reverse", write_config(tmp_path, {}), max_cost=2)
        is None
    )
    found = indel_check.check_missing(assay, {}, rec, "no_reverse", wide, max_cost=2)
    assert found is not None and found["oligo"] == "reverse"


def test_a_pooled_assay_is_screened_under_the_override_for_the_member_that_wins(tmp_path):
    """Pooling is a loop around the same scoring path, so the resolved scoring block has to
    reach every member of the cross product. Here the record carries the ALTERNATE forward
    primer exactly and the stored forward is the worse match, so the winner is the second
    pair: a loop that resolved the override only for the first pair would score the winner
    under the base rules and read `fail` where the override says `reduced`."""
    d = yaml.safe_load((ROOT / "registry" / f"{ANNIS}.yaml").read_text())
    fwd = d["oligos"]["forward"]["seq"]
    alt = fwd  # the record will carry this one exactly
    worse = fwd[:3] + SWAP[fwd[3]] + fwd[4:9] + SWAP[fwd[9]] + fwd[10:15] + SWAP[fwd[15]] + fwd[16:]
    d["oligos"]["forward"]["seq"] = worse  # the stored (first) forward is the worse match for the record
    d["oligos"]["alternates"] = [{"name": "alt-fwd", "seq": alt, "orientation": "forward"}]
    path = tmp_path / f"{ANNIS}.yaml"
    path.write_text(yaml.safe_dump(d))
    pooled = load_assay(path)
    assert [len(p) for p in oligo_pools(pooled)] == [2, 1, 0]

    rev_site = reverse_complement(pooled.oligos.reverse.matching_seq)
    record = (
        "TTTT" + alt + "ACGT" * 30 + SWAP[rev_site[0]] + rev_site[1:] + "TTTT"
    )  # reverse 3'-terminal mismatch
    strict = screen_record(pooled, "r", record, write_config(tmp_path, {}))
    loose = screen_record(
        pooled, "r", record, write_config(tmp_path, {"conventional": {"terminal_mismatch_fails": False}})
    )
    assert alt in strict.extra["pool"] and alt in loose.extra["pool"], (
        "the second pool member must be the winner"
    )
    assert worse not in strict.extra["pool"]
    assert (strict.call, loose.call) == ("fail", "reduced"), (strict.call, loose.call, strict.penalty)
    assert strict.penalty == loose.penalty == 3.0


def test_indel_check_resolves_the_chemistry_of_the_assay_it_is_given(tmp_path):
    """Every other consumer test uses a conventional assay with a conventional override, so
    resolving for a hard-coded 'conventional' passed them all. This one is an MGB assay with
    a DIFFERENT override for each chemistry, and only the MGB one may apply."""
    bd = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
    assay = ASSAYS[bd]
    assert assay.chemistry == Chemistry.mgb
    seq = RECORDS[f"{bd}__perfect"]
    site = reverse_complement(assay.oligos.reverse.matching_seq)
    k = seq.index(site) + len(site) // 2
    rec = seq[:k] + seq[k + 1 :]  # one deleted base, 12 bases in from the reverse primer's 3' end

    both = write_config(
        tmp_path,
        {"mgb": {"primer_3prime_window": 15}, "conventional": {"primer_3prime_window": 2}},
    )
    only_conventional = write_config(tmp_path, {"conventional": {"primer_3prime_window": 15}})
    base = write_config(tmp_path, {})
    labelled = {
        name: indel_check.check_missing(assay, {}, rec, "no_reverse", cfg, max_cost=2)[
            "indel_in_3prime_window"
        ]
        for name, cfg in (("both", both), ("only_conventional", only_conventional), ("base", base))
    }
    assert labelled == {"both": True, "only_conventional": False, "base": False}, labelled


def test_indel_check_fail_resolves_the_chemistry_of_the_assay_it_is_given(tmp_path):
    """The `check_fail` counterpart of the test above, on an MGB assay: a forward primer
    with a deleted base (rescuable) and a 3'-terminal reverse mismatch, which an override
    for MGB may forgive and an override for conventional PCR may not."""
    bd = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
    assay = ASSAYS[bd]
    rec = RECORDS[f"{bd}__perfect"]
    fi = rec.index(assay.oligos.forward.matching_seq)
    rec = rec[: fi + 6] + rec[fi + 7 :]
    ri = rec.index(reverse_complement(assay.oligos.reverse.matching_seq))
    rec = rec[:ri] + SWAP[rec[ri]] + rec[ri + 1 :]

    verdicts = {}
    for name, overrides in (
        ("strict", {}),
        ("mgb_relaxed", {"mgb": {"terminal_mismatch_fails": False}}),
        ("only_conventional_relaxed", {"conventional": {"terminal_mismatch_fails": False}}),
    ):
        cfg = write_config(tmp_path, overrides)
        call = screen_record(assay, "r", rec, cfg)
        assert call.call == "fail", (name, call.call, call.penalty)  # a fail under every config
        verdicts[name] = indel_check.check_fail(assay, call.as_row(), rec, cfg)["rescued_if_indel_forgiven"]
    assert verdicts == {"strict": False, "mgb_relaxed": True, "only_conventional_relaxed": False}, verdicts
