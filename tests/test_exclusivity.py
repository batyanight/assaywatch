"""`target.exclusivity_taxids`: a near neighbour the paper excludes is fetched on purpose.

The report has had a predicted-cross-reactivity arm since 2026-10-23, but it could only
report off-target records that happened to be on disk for some other assay. An assay
whose whole claim is that it distinguishes itself from one named neighbour -- BPSV
against orf virus and pseudocowpox virus -- had nothing to be tested against, so its
specificity was a hand screen in a curator note and not a pipeline result.

Three things are pinned here: the schema refuses the two silent mistakes (the target's
own taxid, and a taxid also declared in scope, which would count the same records in
both arms), retrieval emits the neighbour as its own group on the assay's own query, and
the report marks the rows a paper actually claims so a reader can tell a specificity
result from a coincidence.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from assaywatch.report import exclusivity_rows
from assaywatch.retrieve import group_slug, targets_from_registry
from assaywatch.schema import Target

ROOT = Path(__file__).resolve().parents[1]
BPSV = "BPSV_dsDNA_RPO147_J6R_TaqMan_Zhao_2013"
ORF_VIRUS = 10258
PSEUDOCOWPOX = 129726


def test_the_target_itself_cannot_be_claimed_excluded():
    with pytest.raises(ValidationError, match="target taxid"):
        Target(taxid=129727, exclusivity_taxids=[129727])


def test_a_taxid_cannot_be_both_in_scope_and_excluded():
    with pytest.raises(ValidationError, match="both in scope and claimed excluded"):
        Target(taxid=129727, scope_taxids=[10258], exclusivity_taxids=[10258])


def test_duplicates_are_refused():
    with pytest.raises(ValidationError, match="duplicates"):
        Target(taxid=129727, exclusivity_taxids=[10258, 10258])


def test_an_off_target_neighbour_is_accepted():
    t = Target(taxid=129727, exclusivity_taxids=[ORF_VIRUS, PSEUDOCOWPOX])
    assert t.exclusivity_taxids == [ORF_VIRUS, PSEUDOCOWPOX]


def test_the_registry_asks_for_both_bpsv_neighbours():
    """The live registry, not a fixture: the group has to exist for the run to fetch it."""
    groups = targets_from_registry([ROOT / "registry"])
    slug = group_slug(None)  # BPSV has no gene query; whole-taxon fetch
    for taxid in (ORF_VIRUS, PSEUDOCOWPOX):
        assert BPSV in groups[(taxid, slug)]["assays"]
    # And the neighbour's group is NOT named after the assay that asked for it.
    assert groups[(PSEUDOCOWPOX, slug)]["name"] != "Bovine papular stomatitis virus"


def test_a_claimed_row_sorts_first_and_is_marked():
    class FakeDrift:
        detected_calls = ("detect", "reduced")
        out_of_scope_calls = {
            # A heavy cross-reaction nobody claimed anything about...
            999: {"detect": 90, "fail": 10},
            # ...and the claim the paper actually made, on fewer records.
            ORF_VIRUS: {"reduced": 61, "fail": 3},
        }

    rows = exclusivity_rows(FakeDrift(), None, {ORF_VIRUS})
    assert [r[4] for r in rows] == [True, False]
    assert rows[0][0] == "taxid 10258" and rows[0][1] == 61
