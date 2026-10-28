"""`scripts/find_retrospective_cases.py` searches the citation graph, not oligo text.

The 2026-10-24 sweep searched Europe PMC for papers that PRINT a registry oligo and
`docs/RESUME-HERE.md` records that seam as spent. This instrument asks instead which
papers CITE an assay's design paper and report it missing things, which reaches the
groups that use a published assay without retyping its primers.

The network is not tested here. What is tested is the part that decides whether a hit
is real, because the API's own filter turned out not to be trustworthy.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location(
    "find_retrospective_cases", REPO / "scripts" / "find_retrospective_cases.py"
)
frc = importlib.util.module_from_spec(spec)
sys.modules["find_retrospective_cases"] = frc
spec.loader.exec_module(frc)


def test_the_phrase_groups_are_failure_weighted_and_disjoint():
    """The scarce case is a documented FAILURE, so the phrases hunt for one.

    The development set holds 32 `works` rows and ONE `fails`+`drift` row against a
    target of five, and the held-out set is spent. A phrase list that returned mostly
    `works` candidates would be answering a question the project does not have.
    """
    assert set(frc.GROUPS) == {"miss", "mismatch", "weakened", "redesign"}
    assert "works" not in frc.GROUPS, "a works-hunting group would swamp the queue"
    # A use-and-report family EXISTS since 2026-10-28, because the only tier-2 candidate
    # found that week had no failure word in it -- Quackenbush 1998 simply ran the
    # pan-herpes nest and reported a product 53% identical to its nearest relatives. It
    # is opt-in for the reason this test exists: by default the queue stays weighted
    # towards the scarce case.
    assert set(frc.OPTIONAL_GROUPS) == {"use"}
    assert frc.groups_for() == frc.GROUPS
    assert set(frc.groups_for(("use",))) == set(frc.GROUPS) | {"use"}
    import pytest as _pytest

    with _pytest.raises(SystemExit):
        frc.groups_for(("nonsense",))
    seen: set[str] = set()
    for phrases in frc.GROUPS.values():
        assert phrases
        for p in phrases:
            assert p == p.lower(), f"{p!r} must be lowercase; matching is done on a lowercased abstract"
            assert p not in seen, f"{p!r} appears in two groups, so the group label would be ambiguous"
            seen.add(p)


def test_a_hit_is_confirmed_only_by_the_abstract_text_itself():
    """The API filter is loose and must not be the filter.

    Measured 2026-10-26: Europe PMC's `ABSTRACT:"..."` does not enforce adjacency. On one
    design paper it took 131 citing papers to 58 and none of the first three returned
    abstracts contained any phrase - it had matched the words separately. So the decision
    is an exact substring check locally, and a hit the abstract does not support is
    dropped rather than recorded.
    """
    assert frc.matched_groups("the assay failed to detect four lineages") == ["miss"]
    assert frc.matched_groups("primer mismatches were found at the 3' end") == ["mismatch"]
    assert frc.matched_groups("") == []
    # The exact words, separately, must NOT confirm: that is the API's mistake.
    assert frc.matched_groups("we detected all of the failed cultures") == []
    assert frc.matched_groups("a broad and sensitive assay for surveillance") == []


def test_matching_is_case_insensitive_because_abstracts_are_not_normalised():
    assert frc.matched_groups("FAILED TO DETECT the variant") == ["miss"]
    assert "false-negative" in frc.matched_phrases("A False-Negative result was obtained")


def test_a_hit_can_carry_more_than_one_group_and_every_phrase_is_reported():
    """The group predicts what kind of case a row could become, so both are recorded."""
    ab = "primer mismatch in the probe region caused reduced sensitivity and failed to detect two isolates"
    # Alphabetical, so "mismatch" sorts before "miss": 'a' < 's'.
    assert sorted(frc.matched_groups(ab)) == ["mismatch", "miss", "weakened"]
    phrases = frc.matched_phrases(ab)
    assert "failed to detect" in phrases
    assert "reduced sensitivity" in phrases


def test_the_script_cannot_write_a_case_file():
    """It proposes, never adds. A case asserts what a paper REPORTED, and that cannot be
    read off an abstract - which the PP-I lead of 2026-10-26 demonstrated: a paper
    reporting a "commonly used primer set" at 15% coverage turned out, on measurement,
    not to be reporting the registry's pair at all.

    Parsed rather than grepped, the same way
    `tests/test_papers.py::test_nothing_writes_a_filename_by_replacing_only_the_slash`
    does it, so the docstring's explanation of the rule is not read as a violation of it.
    """
    import ast

    src = (REPO / "scripts" / "find_retrospective_cases.py").read_text()
    tree = ast.parse(src)
    doc = ast.get_docstring(tree) or ""
    assert "validation-cases.tsv` excludes by rule" in doc, "the docstring must state the rule"
    code = src.replace(doc, "")
    assert "validation-cases" not in code, "no executable line may name a case file"
    assert "Proposes, never adds" in doc
