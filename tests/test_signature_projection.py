"""`signature.screen_key`: what a cached screen may depend on, and what it may not.

The screen signature used to hash each entry's whole YAML, so a curator's note made the
groups holding that entry stale. Measured 2026-10-28: 192 entries edited in two days of
curation -- `conditions` blocks, five deletions, one reflagging, three provenance notes --
left 312 of 494 cached screens stale, and not one of those edits could change a call.

The projection fixes that, and its risk runs the other way: a field left OUT means an
edit that DOES change a call reuses a stale screen, silently, which is the failure this
whole mechanism exists to prevent. So the field list is pinned against the schema here,
and a new `Assay` field fails this test until someone classifies it.
"""

from __future__ import annotations

import copy
from pathlib import Path

import pytest
import yaml

from assaywatch.schema import Assay
from assaywatch.signature import SCREEN_FIELDS, screen_key

ROOT = Path(__file__).resolve().parents[1]

#: Every `Assay` field the projection deliberately leaves out, with the reason. A field
#: in neither this set nor SCREEN_FIELDS fails `test_every_schema_field_is_classified`,
#: which is the point: classifying is a decision and forgetting is not allowed.
NOT_SCREENED = {
    "id": "the key itself; a rename is a different entry and a different group",
    "name": "display text",
    "citation": "provenance; cannot reach the matcher",
    "use_context": "a filter for readers",
    "submitted_by": "provenance",
    "source": "curator prose, nested_round and nested_family -- read by the nested report, never by a screen",
    "needs_review": "the FLAGS are projected separately; the notes are prose",
    "conditions": "the thermal protocol. `thermo: false` ships, and even with it on "
    "thermo columns are reported and never scored",
    "performance": "the paper's own LoD and efficiency; reported, never scored",
    "panels": "the paper's wet-lab panels; reported, never scored",
}


def _entry() -> dict:
    path = ROOT / "registry" / "BPSV_dsDNA_RPO147_J6R_TaqMan_Zhao_2013.yaml"
    return yaml.safe_load(path.read_text())


def test_every_schema_field_is_classified():
    """A new Assay field is either screen-relevant or deliberately not. Decide, in code."""
    unclassified = set(Assay.model_fields) - set(SCREEN_FIELDS) - set(NOT_SCREENED)
    assert not unclassified, (
        f"new Assay field(s) {sorted(unclassified)}: add to signature.SCREEN_FIELDS if a "
        "screen's result can depend on them, or to NOT_SCREENED here with the reason"
    )


@pytest.mark.parametrize(
    "mutate",
    [
        pytest.param(lambda d: d["source"].update(notes_curator="rewritten"), id="curator note"),
        pytest.param(lambda d: d["conditions"].update(annealing_c=42.0), id="annealing temperature"),
        pytest.param(lambda d: d.update(name="A NEW DISPLAY NAME"), id="display name"),
        pytest.param(lambda d: d["citation"].update(reference="a fuller reference"), id="citation text"),
        pytest.param(lambda d: d["needs_review"][0].update(note="a clearer note"), id="review note"),
        pytest.param(lambda d: d.update(use_context=["public_health"]), id="use context"),
        pytest.param(lambda d: d.update(performance={"lod": "10 copies"}), id="performance block"),
    ],
)
def test_prose_and_protocol_do_not_make_a_screen_stale(mutate):
    before = _entry()
    after = copy.deepcopy(before)
    mutate(after)
    assert after != before, "the mutation did not change the entry; the test proves nothing"
    assert screen_key(after) == screen_key(before)


@pytest.mark.parametrize(
    "mutate",
    [
        pytest.param(
            lambda d: d["oligos"]["forward"].update(seq="ACGTACGTACGTACGTACGT"), id="forward sequence"
        ),
        pytest.param(
            lambda d: d["oligos"]["probe"].update(seq_as_written="ACGTACGTACGTI"), id="seq_as_written"
        ),
        pytest.param(lambda d: d["oligos"]["forward"].update(tail_5prime="GGGG"), id="5' tail"),
        pytest.param(
            lambda d: d["oligos"]["alternates"].append(
                {"name": "alt", "seq": "ACGTACGTACGTACGTACGT", "slot": "forward"}
            ),
            id="alternates",
        ),
        pytest.param(lambda d: d.update(chemistry="conventional"), id="chemistry"),
        pytest.param(lambda d: d.update(amplicon_bp=92), id="amplicon size"),
        pytest.param(lambda d: d["target"].update(taxid=10258), id="target taxid"),
        pytest.param(lambda d: d["target"].update(query="J6R[Gene]"), id="retrieval query"),
        pytest.param(lambda d: d["target"].update(scope_taxids=[129727]), id="scope"),
        pytest.param(lambda d: d["target"].update(exclusivity_taxids=[10258]), id="exclusivity"),
        pytest.param(lambda d: d.update(status="deprecated"), id="status"),
        pytest.param(lambda d: d["needs_review"].append({"flag": "not_screenable"}), id="review FLAG"),
    ],
)
def test_anything_that_can_change_a_call_does_make_a_screen_stale(mutate):
    before = _entry()
    after = copy.deepcopy(before)
    mutate(after)
    assert after != before, "the mutation did not change the entry; the test proves nothing"
    assert screen_key(after) != screen_key(before)


def test_a_null_field_hashes_like_a_missing_one():
    """Adding `conditions: null` to an entry must not rescreen it."""
    before = _entry()
    before.pop("conditions", None)
    after = dict(before, conditions=None, performance=None, panels=None)
    assert screen_key(after) == screen_key(before)


def test_the_key_is_stable_across_key_order():
    before = _entry()
    after = dict(reversed(list(before.items())))
    assert screen_key(after) == screen_key(before)


def test_every_live_entry_projects_without_error():
    """The Snakefile calls this for all 214 entries before anything is screened."""
    keys = {p.stem: screen_key(yaml.safe_load(p.read_text())) for p in (ROOT / "registry").glob("*.yaml")}
    assert len(keys) > 200
    assert all(isinstance(k, bytes) and k for k in keys.values())


def test_the_stale_checker_hashes_what_the_snakefile_hashes():
    """`scripts/stale_screens.py` must answer the pipeline's question, not its own.

    It reimplements the signature so the question "what will the next run rescreen" can
    be asked without starting a run -- which is the tool that was missing when a stopped
    run's progress counter was read as a work queue on 2026-10-28. Two copies of one
    formula drift, so the config keys are pinned against the Snakefile's `_SCREEN_CFG`
    here, and the closure comes from `source_names("screen")` in both.
    """
    import importlib.util
    import re

    spec = importlib.util.spec_from_file_location("stale_screens", ROOT / "scripts" / "stale_screens.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    snakefile = (ROOT / "Snakefile").read_text()
    m = re.search(r"_SCREEN_CFG = \{k: config\.get\(k\) for k in \(([^)]*)\)\}", snakefile)
    assert m, "the Snakefile no longer defines _SCREEN_CFG the way this test reads it"
    keys = tuple(re.findall(r'"([a-z_]+)"', m.group(1)))
    assert keys == mod.SCREEN_CFG_KEYS

    # And the Snakefile hashes the projection, not the file bytes: the whole point.
    assert "screen_key(yaml.safe_load(" in snakefile
    assert "read_bytes())" not in snakefile.split("def screen_signature")[1].split("def ")[0]
