"""Tests for assaywatch.taxonomy (scope_taxids ancestry)."""

import gzip
import json

import pytest

from assaywatch.taxonomy import Taxonomy, load_taxonomy, taxonomy_from_config

# The real shape that broke exact matching: Morbillivirus canis (3052342) with a
# no-rank child (3139435) and a strain (11233), and the species' old taxid 11232
# merged into it. 11229 is the genus.
PARENT = {3052342: 11229, 3139435: 3052342, 11233: 3052342, 11229: 1, 99: 1}
MERGED = {11232: 3052342}


def test_descendants_are_within_a_species_scope():
    tx = Taxonomy(PARENT, MERGED)
    assert tx.within(3139435, {3052342})
    assert tx.within(11233, {3052342})
    assert tx.within(3052342, {3052342})
    assert not tx.within(99, {3052342})  # a sibling of the genus is out
    assert not tx.within(11229, {3052342})  # an ancestor is not inside its child


def test_merges_are_followed_on_both_sides():
    tx = Taxonomy(PARENT, MERGED)
    scope = {tx.canonical(11232)}  # a registry still naming the merged taxid
    assert scope == {3052342}
    assert tx.within(3139435, scope)
    assert tx.within(11232, scope)  # an old record carrying the merged taxid


def test_an_unknown_taxid_matches_only_itself_and_is_recorded():
    tx = Taxonomy(PARENT, MERGED)
    assert tx.within(555, {555})
    assert not tx.within(555, {3052342})
    assert tx.unknown == {555}


def test_round_trip_and_config(tmp_path):
    path = tmp_path / "tree.json.gz"
    with gzip.open(path, "wt") as fh:
        json.dump({"parent": {str(k): v for k, v in PARENT.items()}, "merged": {"11232": 3052342}}, fh)
    tx = load_taxonomy(path)
    assert tx.within(11233, {3052342})
    assert taxonomy_from_config({"drift": {}}) is None
    assert taxonomy_from_config({"drift": {"scope_taxonomy": str(path)}}).within(3139435, {3052342})
    with pytest.raises(FileNotFoundError, match="build_taxonomy_cache"):
        taxonomy_from_config({"drift": {"scope_taxonomy": str(tmp_path / "missing.json.gz")}})


def test_every_registry_scope_taxid_is_in_the_shipped_tree():
    """A scope taxid the tree doesn't know matches only itself, so a typo or a
    deleted taxid would quietly empty the assay. Rebuild the cache if this fails."""
    from pathlib import Path

    from assaywatch.validate import iter_files, load_assay

    root = Path(__file__).resolve().parents[1]
    tx = load_taxonomy(root / "docs" / "taxonomy-cache.json.gz")
    missing = {
        (a.id, t)
        for a in map(load_assay, iter_files(root / "registry"))
        for t in a.target.scope_taxids or []
        if tx.canonical(t) not in tx.parent
    }
    assert not missing, sorted(missing)[:10]


# JC polyomavirus 10632 (no rank) under species 1891763, genus 1891746; 1193974
# "Human enterovirus" (rank species) under "unclassified Enterovirus" 90010.
JC_PARENT = {10632: 1891763, 1891763: 1891746, 1891746: 1, 1193974: 90010, 90010: 12059, 12059: 1}
JC_RANK = {1891763: "species", 1891746: "genus", 1193974: "species", 12059: "genus"}
JC_NAME = {90010: "unclassified Enterovirus", 12059: "Enterovirus", 1193974: "Human enterovirus"}


def test_species_of_rolls_a_no_rank_child_up_and_stops_above_species():
    tx = Taxonomy(JC_PARENT, {}, JC_RANK, JC_NAME)
    assert tx.species_of(10632) == 1891763
    assert tx.species_of(1891763) == 1891763
    assert tx.species_of(1891746) is None  # a genus has no species above it
    assert tx.species_of(555) is None  # unknown taxid


def test_in_unclassified_looks_at_the_taxid_and_its_ancestors():
    tx = Taxonomy(JC_PARENT, {}, JC_RANK, JC_NAME)
    assert tx.in_unclassified(1193974)
    assert not tx.in_unclassified(10632)
    assert not tx.in_unclassified(12059)


def test_load_reads_ranks_and_names_and_tolerates_an_old_cache(tmp_path):
    new, old = tmp_path / "new.json.gz", tmp_path / "old.json.gz"
    with gzip.open(new, "wt") as fh:
        json.dump(
            {"parent": {"10632": 1891763}, "merged": {}, "rank": {"1891763": "species"}, "name": {}}, fh
        )
    with gzip.open(old, "wt") as fh:
        json.dump({"parent": {"10632": 1891763}, "merged": {}}, fh)
    assert load_taxonomy(new).species_of(10632) == 1891763
    assert load_taxonomy(old).rank == {}
