"""Tests for the `needs_review` controlled vocabulary and the registry's use of it.

Two kinds of test here. The first few check the vocabulary's own invariants. The
rest are guards against the exact drift S7 undid: free strings, singleton flags,
and flags that restate a field on the same entry. Those three are what made the
field unfilterable, and nothing in the schema stops them coming back - only a
test counting what is actually in `registry/` does.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from collections import Counter
from pathlib import Path

import pytest
import yaml

from assaywatch.review import CAVEAT, NOTE_REQUIRED, OPEN, ReviewFlag
from assaywatch.validate import iter_files, load_assay

REGISTRY = Path(__file__).resolve().parents[1] / "registry"

# Flags whose names were in the field before 2026-10-21 and restated a field on
# the same document. Each had instances that were already wrong at migration.
DERIVABLE = {
    "DOI_MISSING": "citation.doi",
    "DOI_UNVERIFIED": "citation.doi_verified",
    "NO_YEAR": "citation.design_year",
    "TAXID_MISSING": "target.taxid",
}


@pytest.fixture(scope="module")
def entries():
    return [(p, load_assay(p), yaml.safe_load(p.read_text())) for p in sorted(iter_files(REGISTRY))]


def test_open_and_caveat_partition_the_vocabulary():
    assert OPEN | CAVEAT == frozenset(ReviewFlag)
    assert not OPEN & CAVEAT
    assert OPEN and CAVEAT  # neither side is empty, or the split says nothing


def test_note_required_flags_are_real_flags():
    assert NOTE_REQUIRED <= frozenset(ReviewFlag)


def test_flag_values_are_lower_snake_case():
    """SCREAMING_SNAKE is how the old free strings looked; keep the shapes distinguishable."""
    for flag in ReviewFlag:
        assert re.fullmatch(r"[a-z][a-z0-9_]*", flag.value), flag
        assert flag.name == flag.value


def test_the_catch_all_demands_a_note():
    """`curation_decision_pending` is the pressure valve; bare, it is a shrug."""
    assert ReviewFlag.curation_decision_pending in NOTE_REQUIRED
    assert ReviewFlag.curation_decision_pending in OPEN


def test_no_registry_entry_carries_a_derivable_flag(entries):
    """A flag that restates a field cannot be kept in step, so none may exist.

    At migration 6 of 39 instances of these four were already contradicting
    their own entry: four said DOI_MISSING beside a verified DOI, two said
    NO_YEAR beside `design_year: 2011`. The flags are gone; this keeps them gone
    whatever name someone reaches for next.
    """
    names = {f.lower() for f in DERIVABLE}
    offenders = [
        (p.name, i.flag.value)
        for p, a, _ in entries
        for i in a.needs_review or []
        if i.flag.value.lower() in names
    ]
    assert offenders == []


def test_the_field_is_not_mostly_singletons(entries):
    """What broke the old field was not one rare flag; it was a tail of them.

    Before S7 it held 98 distinct strings over 243 instances and 69 of those
    strings occurred exactly once - a list where two thirds of the values are
    unique cannot be filtered, counted or audited, which is the only reason to
    have one. After it: 30 flags over 198 items, 1 singleton
    (`chemistry_detail_missing`, a category that will recur across the 44
    probe-bearing entries). A quarter is well clear of both numbers, so this
    fails on a returning tail and not on a genuinely rare category.
    """
    counts = Counter(i.flag for _, a, _ in entries for i in a.needs_review or [])
    singletons = sorted(f.value for f, n in counts.items() if n == 1)
    assert len(singletons) <= len(counts) / 4, (
        f"{len(singletons)} of {len(counts)} flags in use occur once; a one-off is a note, "
        f"not a category: {singletons}"
    )


def test_the_registry_does_not_lean_on_the_catch_all(entries):
    """If `curation_decision_pending` is common, the vocabulary is missing a category.

    It was unused at migration: all 198 items across 146 entries fell into one of
    the 30 named flags. That is the evidence the categories match the registry,
    and the threshold is set low so the evidence has to stay true.
    """
    n = sum(
        1
        for _, a, _ in entries
        for i in a.needs_review or []
        if i.flag is ReviewFlag.curation_decision_pending
    )
    assert n <= 5, f"{n} entries fall back on curation_decision_pending; name the category instead"


def test_every_registry_item_parses_as_a_structured_item(entries):
    """The YAML on disk is `{flag, note}`, not a bare string.

    `load_assay` would already fail on a bare string, so this checks the raw
    document rather than the model: it is the shape of the files that matters to
    anyone reading them with `rg` or `yq`.
    """
    for path, _, doc in entries:
        for item in doc.get("needs_review") or []:
            assert isinstance(item, dict), f"{path.name}: {item!r}"
            assert set(item) <= {"flag", "note"}, f"{path.name}: {sorted(item)}"
            assert item["flag"] in {f.value for f in ReviewFlag}, f"{path.name}: {item['flag']}"


def test_notes_are_one_line_of_prose(entries):
    """A `note` is a line beside a flag in a filtered list; the long record is notes_curator."""
    for path, a, _ in entries:
        for i in a.needs_review or []:
            if i.note is None:
                continue
            assert "\n" not in i.note, f"{path.name}: {i.flag.value} note has a newline"
            assert len(i.note) <= 400, f"{path.name}: {i.flag.value} note is {len(i.note)} chars"


def test_open_questions_are_the_minority_they_should_be(entries):
    """The split has to actually split something.

    146 of 208 entries were blocked from `active` by the old all-or-nothing gate;
    21 carry a genuine open question. If every flagged entry were open again, the
    vocabulary would have gained nothing.
    """
    flagged = [a for _, a, _ in entries if a.needs_review]
    with_open = [a for a in flagged if a.open_review]
    assert flagged, "the registry has review flags; this test is measuring nothing"
    assert len(with_open) < len(flagged) / 2


# --- the two bootstrap scripts, whose output has to be the new shape ---------
#
# `parse_wcs_primers.py` builds the drafts and `apply_curation.py` merges
# curation onto them, so both write `needs_review` before the validator ever
# sees it. Neither can be run end to end here (the source spreadsheet is a local
# one-off), but the flag logic in each is pure and is where the S7 edit landed.


def _load_script(name: str):
    spec = importlib.util.spec_from_file_location(name, REGISTRY.parent / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_the_parser_emits_items_the_schema_accepts():
    parse = _load_script("parse_wcs_primers")
    items = parse.review_items(
        {"DO_NOT_USE", "NESTED", "NOT_AN_OLIGO_LENGTH"},
        many_primers=True,
        orientation_by_position=True,
    )
    flags = [i["flag"] for i in items]
    assert flags == [
        ReviewFlag.do_not_use.value,
        ReviewFlag.nested_protocol.value,
        ReviewFlag.pairing_is_curator_reading.value,
        ReviewFlag.orientation_inferred.value,
    ]
    # NOT_AN_OLIGO_LENGTH is a mark about one spreadsheet row, not a review
    # flag, and must not leak into the registry's vocabulary.
    assert "NOT_AN_OLIGO_LENGTH" not in str(items)
    for item in items:
        assert set(item) <= {"flag", "note"}


def test_the_parser_no_longer_emits_a_flag_for_a_missing_year():
    """It used to append NO_YEAR, which `citation.design_year` already says."""
    parse = _load_script("parse_wcs_primers")
    items = parse.review_items(set(), many_primers=False, orientation_by_position=False)
    assert items == []
    assert not any(k.lower() in {f.lower() for f in DERIVABLE} for k in parse.CELL_MARK_TO_FLAG)


def test_every_cell_mark_the_parser_knows_maps_to_the_right_flag():
    """Pinned pair by pair, because the mapping *is* the content of that table.

    `UNTESTED -> do_not_use` would pass any test that only checked the flags
    were real: both exist, both are open. But `do_not_use` raises a
    keep-or-delete row in materials-needed.tsv and `not_validated` does not, so
    the mismapping would manufacture deletion decisions for assays whose only
    sin is that nobody has run them.
    """
    parse = _load_script("parse_wcs_primers")
    assert parse.CELL_MARK_TO_FLAG == {
        "DO_NOT_USE": ReviewFlag.do_not_use,
        "CROSS_REACTIVE": ReviewFlag.cross_reactive,
        "UNTESTED": ReviewFlag.not_validated,
        "MODIFIED_IN_HOUSE": ReviewFlag.oligos_modified,
        "NESTED": ReviewFlag.nested_protocol,
    }
    # Every marker the sheet-reader can raise has a home here, so a new pattern
    # cannot be added upstream and then silently dropped on the way in.
    assert set(parse.CELL_MARK_TO_FLAG) == set(parse.FLAG_PATTERNS)
