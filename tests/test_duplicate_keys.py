"""`scripts/check_duplicate_keys.py`: a key given twice must not load silently.

`yaml.safe_load` takes last-wins on a duplicate mapping key and says nothing, so an
entry with two `notes_curator` keys validates, screens and reports while carrying only
the second value -- the other is in the file and in no loaded entry. That happened:
LEPTOSPIROSIS_Flagillar_filiment_Prote.yaml held two for three days, and pre-commit's
check-yaml found it only when an unrelated commit touched the file.

The detector is pinned on text rather than on the registry, so the test says what the
tool does even on a day when every registry file is clean.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _module():
    spec = importlib.util.spec_from_file_location(
        "check_duplicate_keys", ROOT / "scripts" / "check_duplicate_keys.py"
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


DUPED = """
id: X
source:
  notes_curator: the first note, which yaml.safe_load throws away
  notes_curator: the second note, which is all pydantic ever sees
"""

CLEAN = """
id: X
source:
  notes_curator: one note
  nested_round: null
"""


def test_a_repeated_key_is_reported_with_its_line():
    dupes = _module().duplicates_in(DUPED)
    assert [k for k, _ in dupes] == ["notes_curator"]
    assert dupes[0][1] == 5


def test_a_clean_file_reports_nothing():
    assert _module().duplicates_in(CLEAN) == []


def test_the_same_key_in_two_different_mappings_is_not_a_duplicate():
    # `note:` under each of two review items is the ordinary case and must stay quiet.
    text = "needs_review:\n- flag: a\n  note: one\n- flag: b\n  note: two\n"
    assert _module().duplicates_in(text) == []


def test_the_live_registry_is_clean():
    mod = _module()
    bad = {
        path.name: mod.duplicates_in(path.read_text())
        for path in sorted((ROOT / "registry").glob("*.yaml"))
        if mod.duplicates_in(path.read_text())
    }
    assert not bad, f"duplicate keys: {bad}"
