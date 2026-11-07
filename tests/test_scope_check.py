"""The release scope verification: the flags, on counts given by hand."""

from __future__ import annotations

import gzip
from datetime import date

from assaywatch.scope_check import Counts, archive_profile, flags_for, scope_lineage_flags, window_start
from assaywatch.taxonomy import Taxonomy


def _counts(**kw) -> Counts:
    base = {
        "query_all": 100,
        "query_window": 10,
        "taxid_window": 12,
        "scope_window": None,
        "archive_accessions": 100,
        "newest_created": "2026-01-01",
    }
    return Counts(**{**base, **kw})


def _flags(c: Counts, query: str | None = None, scoped: bool = False) -> set[str]:
    return {f for f, _ in flags_for(c, query=query, window_from="2024-11-01", scoped=scoped)}


def test_a_healthy_assay_raises_nothing():
    assert _flags(_counts()) == set()


def test_a_query_blind_while_the_taxid_is_not():
    assert "query_sees_nothing" in _flags(_counts(query_window=0, taxid_window=500))


def test_a_quiet_taxon_is_not_a_blind_query():
    assert "query_sees_nothing" not in _flags(_counts(query_window=0, taxid_window=0))


def test_could_not_ask_is_not_zero():
    c = _counts(query_all=None, query_window=None, taxid_window=None)
    assert _flags(c) == set()


def test_taxid_more_than_three_times_the_query():
    assert "taxid_over_query" in _flags(_counts(query_window=10, taxid_window=31))
    assert "taxid_over_query" not in _flags(_counts(query_window=10, taxid_window=30))


def test_archive_more_than_a_tenth_behind_its_query():
    assert "archive_behind_query" in _flags(_counts(archive_accessions=89))
    assert "archive_behind_query" not in _flags(_counts(archive_accessions=90))


def test_newest_deposit_before_the_window():
    assert "archive_stale" in _flags(_counts(newest_created="2021-03-01"))
    assert "archive_stale" in _flags(_counts(newest_created=None))


def test_a_query_naming_a_taxid():
    assert "query_names_taxid" in _flags(_counts(), query="txid123[Organism:exp]")


def test_an_empty_scope_only_counts_when_there_is_a_scope():
    assert "scope_empty" in _flags(_counts(scope_window=0), scoped=True)
    assert "scope_empty" not in _flags(_counts(scope_window=None), scoped=False)


def test_a_scope_taxid_that_gained_a_species_parent():
    """`Orf virus` under `Parapoxvirus orf`: new records file at the parent, outside the scope."""
    tx = Taxonomy(
        parent={10258: 3431389, 3431389: 10257},
        merged={},
        rank={3431389: "species"},
        name={3431389: "P. orf"},
    )
    assert [f for f, _ in scope_lineage_flags([10258], tx)] == ["scope_taxid_gained_parent"]
    assert scope_lineage_flags([10258, 3431389], tx) == []
    assert scope_lineage_flags([10258], None) == []


def test_archive_profile_counts_accessions_once_and_finds_the_newest(tmp_path):
    with gzip.open(tmp_path / "a.meta.tsv.gz", "wt") as fh:
        fh.write("accession\tcreated\nAB1.1\t2020-01-01\nAB1.2\t2021-05-05\nAB2.1\t2019-01-01\n")
    assert archive_profile(tmp_path) == (2, "2021-05-05")
    assert archive_profile(tmp_path / "missing") == (0, None)


def test_window_start_steps_back_whole_months():
    assert window_start(date(2026, 11, 6), 24) == "2024-11-01"
    assert window_start(date(2026, 1, 15), 1) == "2025-12-01"
