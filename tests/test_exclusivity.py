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


def test_a_claimed_neighbour_never_counts_toward_the_denominator():
    """The defect the 2026-10-27 run found, with the real numbers behind it.

    The scope filter only runs for an assay that declares `scope_taxids`, and the first
    entry to carry `exclusivity_taxids` declared none. So its two neighbour archives --
    retrieved for its specificity claim -- were counted IN its own drift denominator,
    and it moved from `insufficient data` to `low coverage`: the pipeline read orf virus
    records as evidence that a BPSV assay still detects BPSV. An exclusion is out of
    scope whatever else the entry says.
    """
    from assaywatch.drift import assess
    from assaywatch.taxonomy import Taxonomy

    # 129727 BPSV (the target), 10258 orf virus (claimed excluded). Flat tree: each
    # taxon is its own parent, which is all `within` needs for a declared taxid.
    taxonomy = Taxonomy(parent={129727: None, 10258: None}, rank={}, name={}, merged={})
    rows = [{"assay_id": "A", "record_id": f"own{i}", "call": "detect", "species": ""} for i in range(40)] + [
        {"assay_id": "A", "record_id": f"orf{i}", "call": "fail", "species": ""} for i in range(40)
    ]
    years = {r["record_id"]: "2026-01-01" for r in rows}
    taxids = {f"own{i}": 129727 for i in range(40)} | {f"orf{i}": 10258 for i in range(40)}
    cfg = {"drift": {}, "scoring": {}, "lineage": {}}

    without = assess(rows, years, cfg, taxids=taxids, taxonomy=taxonomy)["A"]
    with_claim = assess(rows, years, cfg, taxids=taxids, taxonomy=taxonomy, exclude_map={"A": {10258}})["A"]

    # Unguarded, the neighbour halves the detected share and doubles the denominator.
    assert without.out_of_scope == 0
    assert with_claim.out_of_scope == 40
    assert with_claim.recent_evaluable == without.recent_evaluable - 40
    assert with_claim.recent_fraction == 1.0 and without.recent_fraction == 0.5
    # And the records are kept as the specificity evidence they were fetched to be.
    assert with_claim.out_of_scope_calls[10258]["fail"] == 40


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
