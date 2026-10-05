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

import pytest
import yaml

from assaywatch.schema import Chemistry
from assaywatch.score import (
    RESOLVED,
    check_chemistry_overrides,
    config_for,
    load_config,
    scoring_for,
)


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
    import pathlib

    from assaywatch.iupac import reverse_complement
    from assaywatch.score import screen_record
    from assaywatch.validate import load_assay

    assay = next(
        a
        for a in (load_assay(p) for p in sorted(pathlib.Path("registry").glob("*.yaml")))
        if a.chemistry == Chemistry.conventional and a.oligos.probe is None and a.oligos.forward.seq.isalpha()
    )
    fwd = assay.oligos.forward.matching_seq
    rev = assay.oligos.reverse.matching_seq
    # One substitution at the forward primer's 3'-terminal base, nothing else.
    swap = {"A": "C", "C": "A", "G": "T", "T": "G"}
    broken = fwd[:-1] + swap[fwd[-1]]
    record = "TTTT" + broken + "ACGT" * 30 + reverse_complement(rev) + "TTTT"

    before = screen_record(assay, "r1", record, load_config())
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
