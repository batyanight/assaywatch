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
