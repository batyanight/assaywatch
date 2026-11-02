"""`conditions` / `performance` / `panels`: the protocol the registry never carried.

Counted 2026-10-27: annealing or cycling appears in 7 of 214 entries, LoD or efficiency
in 23, master mix or Mg2+ in 2, and one-step versus two-step RT in none -- all of it in
curator prose. That is why `thermo: false` must ship, because a mismatch costing 6 °C of
Tm is irrelevant at an annealing temperature of 50 and fatal at 62, and the schema could
not say which.

These blocks are added empty, the way `by_chemistry` was: the shape is fixed and
validated before 164 papers are read into it. What is pinned here is that the shape
refuses the mistakes a bulk populate pass would otherwise commit silently -- a
temperature that is not a temperature, a panel detecting more than it tested, an
efficiency that is a fraction where the field is a percentage.
"""

from __future__ import annotations

import pytest
import yaml
from pydantic import ValidationError

from assaywatch.review import OPEN, ReviewFlag
from assaywatch.schema import Assay, Conditions, Panel, Performance, RTFormat

MINIMAL = {
    "id": "TEST_assay",
    "name": "Test assay",
    "target": {"taxid": 1234},
    "chemistry": "hydrolysis_probe",
    "oligos": {
        "forward": {"name": "f", "seq": "ACGTACGTACGTACGT"},
        "reverse": {"name": "r", "seq": "TGCATGCATGCATGCA"},
        "probe": {"name": "p", "seq": "ACGTACGTACGTA"},
    },
    "citation": {"doi": "10.1016/j.jviromet.2013.08.027"},
}


def test_a_protocol_round_trips_through_yaml():
    entry = dict(
        MINIMAL,
        conditions={
            "annealing_c": 60.0,
            "annealing_seconds": 20,
            "cycles": 45,
            "rt": "none",
            "master_mix": "TaqMan Universal PCR Master Mix",
        },
        performance={"lod": "1-7 copies of viral genome per reaction", "efficiency_pct": 98.5},
        panels=[{"name": "exclusivity", "n_tested": 12, "n_detected": 0, "taxids": [10258, 129726]}],
    )
    a = Assay.model_validate(yaml.safe_load(yaml.safe_dump(entry)))
    assert a.conditions and a.conditions.annealing_c == 60.0
    assert a.conditions.rt is RTFormat.none
    assert a.performance and a.performance.efficiency_pct == 98.5
    assert a.panels and a.panels[0].n_detected == 0


def test_absent_is_the_default_and_stays_absent():
    a = Assay.model_validate(MINIMAL)
    assert a.conditions is None and a.performance is None and a.panels is None


def test_a_typo_in_a_block_fails_loudly():
    with pytest.raises(ValidationError):
        Assay.model_validate(dict(MINIMAL, conditions={"anneal_c": 60}))


def test_an_impossible_temperature_or_cycle_count_is_refused():
    with pytest.raises(ValidationError):
        Conditions(annealing_c=600)  # a Celsius/Fahrenheit or decimal-point slip
    with pytest.raises(ValidationError):
        Conditions(cycles=0)
    with pytest.raises(ValidationError):
        Conditions(denature_c=60)  # denaturation below 80 C is a mislabelled step


def test_an_efficiency_given_as_a_fraction_is_refused():
    # 0.985 is the same measurement in the other unit, and silently reading it as
    # 0.985% would make a working assay look broken.
    with pytest.raises(ValidationError):
        Performance(efficiency_pct=0.985)


def test_a_panel_cannot_detect_more_than_it_tested():
    with pytest.raises(ValidationError, match="n_detected"):
        Panel(name="inclusivity", n_tested=10, n_detected=11)


def test_conditions_not_printed_is_a_recorded_caveat_not_an_open_question():
    # The paper not printing a protocol is a permanent fact about the paper, so it
    # must not block `active` the way an unanswered curation question does.
    assert ReviewFlag.conditions_not_printed not in OPEN
