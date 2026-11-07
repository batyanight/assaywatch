"""The RefSeq twin map: which curated RefSeq records repeat a non-RefSeq record's whole sequence."""

from __future__ import annotations

import gzip
from pathlib import Path

import pytest

from assaywatch import refseq_twins
from assaywatch.calls import key_calls_by_accession


def _archive(path: Path, records: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as fh:
        for rid, seq in records.items():
            fh.write(f">{rid} a title\n{seq}\n")


def _built(tmp_path: Path, **kwargs: int) -> dict[str, frozenset[str]]:
    out = tmp_path / "run" / "refseq-twins.tsv.gz"
    refseq_twins.build(tmp_path / "retrieved", out, **kwargs)
    return refseq_twins.read(out)


def test_a_curated_record_is_paired_with_every_identical_non_refseq_record(tmp_path):
    _archive(
        tmp_path / "retrieved/1/all/2026-01-01.fasta.gz",
        {"NC_1.2": "ACGT", "AY1.1": "ACGT", "KX1.1": "ACGT", "KX2.1": "TTTT"},
    )
    assert _built(tmp_path) == {"NC_1": frozenset({"AY1", "KX1"})}


@pytest.mark.parametrize("prefix", ["NC_", "AC_", "NG_", "NR_", "NW_"])
def test_each_curated_prefix_is_mapped(tmp_path, prefix):
    _archive(tmp_path / "retrieved/1/all/a.fasta.gz", {f"{prefix}1.1": "ACGT", "AY1.1": "ACGT"})
    assert _built(tmp_path) == {f"{prefix}1": frozenset({"AY1"})}


@pytest.mark.parametrize("prefix", ["NZ_", "NM_", "XM_", "XR_"])
def test_other_refseq_prefixes_are_not_mapped(tmp_path, prefix):
    """`NZ_` has its accession rule. `NM_` and `XM_` are transcripts, rarely a copy (130 of 4,244 and 12 of 48,799)."""
    _archive(tmp_path / "retrieved/1/all/a.fasta.gz", {f"{prefix}1.1": "ACGT", "AY1.1": "ACGT"})
    assert _built(tmp_path) == {}


def test_two_refseq_records_are_not_each_others_twin(tmp_path):
    """A twin has to be the deposit that survives, so it can't itself be a RefSeq record."""
    _archive(
        tmp_path / "retrieved/1/all/a.fasta.gz", {"NC_1.1": "ACGT", "NR_1.1": "ACGT", "NZ_CP1.1": "ACGT"}
    )
    assert _built(tmp_path) == {}


def test_a_twin_can_sit_in_another_archive(tmp_path):
    _archive(tmp_path / "retrieved/1/all/a.fasta.gz", {"NC_1.1": "ACGT"})
    _archive(tmp_path / "retrieved/2/q0123456789/b.fasta.gz", {"AY1.1": "ACGT"})
    assert _built(tmp_path) == {"NC_1": frozenset({"AY1"})}


def test_one_accession_cut_differently_in_two_archives_keeps_both_sequences(tmp_path):
    """Window archives hold a cut of the record, so one accession can carry two sequences.
    Either may match, and which one is read last must not decide it."""
    _archive(tmp_path / "retrieved/1/all/a.fasta.gz", {"NC_1.1": "ACGTACGT", "AY1.1": "ACGTACGT"})
    _archive(tmp_path / "retrieved/1/asm/b.fasta.gz", {"NC_1.1": "ACGT"})
    assert _built(tmp_path) == {"NC_1": frozenset({"AY1"})}


def test_case_and_line_wrapping_do_not_separate_twins(tmp_path):
    path = tmp_path / "retrieved/1/all/a.fasta.gz"
    path.parent.mkdir(parents=True)
    with gzip.open(path, "wt") as fh:
        fh.write(">NC_1.1\nACGT\nACGT\n>AY1.1\nacgtacgt\n")
    assert _built(tmp_path) == {"NC_1": frozenset({"AY1"})}


def test_the_file_is_the_same_bytes_whatever_the_worker_count(tmp_path):
    _archive(tmp_path / "retrieved/1/all/a.fasta.gz", {"NC_1.1": "ACGT", "KX1.1": "ACGT"})
    _archive(tmp_path / "retrieved/1/all/b.fasta.gz", {"NC_2.1": "TTTT", "AY1.1": "ACGT", "AY2.1": "TTTT"})
    one, two = tmp_path / "one.tsv.gz", tmp_path / "two.tsv.gz"
    refseq_twins.build(tmp_path / "retrieved", one, workers=1)
    refseq_twins.build(tmp_path / "retrieved", two, workers=2)
    assert one.read_bytes() == two.read_bytes()


def test_an_empty_archive_directory_writes_an_empty_map(tmp_path):
    (tmp_path / "retrieved").mkdir()
    assert _built(tmp_path) == {}


def test_beside_finds_the_map_next_to_the_calls_table(tmp_path):
    _archive(tmp_path / "retrieved/1/all/a.fasta.gz", {"NC_1.1": "ACGT", "AY1.1": "ACGT"})
    refseq_twins.build(tmp_path / "retrieved", tmp_path / "run" / refseq_twins.FILENAME)
    assert refseq_twins.beside(tmp_path / "run" / "calls.tsv.gz") == {"NC_1": frozenset({"AY1"})}


def test_beside_warns_and_returns_none_for_a_run_without_a_map(tmp_path, capsys):
    assert refseq_twins.beside(tmp_path / "calls.tsv.gz") is None
    assert "refseq-twins" in capsys.readouterr().err


def test_a_curated_row_is_dropped_only_when_its_twin_is_in_the_same_assay():
    rows = [
        {"assay_id": "A", "record_id": "NC_1.1", "call": "fail"},
        {"assay_id": "A", "record_id": "AY1.1", "call": "detect"},
        {"assay_id": "B", "record_id": "NC_1.1", "call": "fail"},
        {"assay_id": "C", "record_id": "AY1.1", "call": "detect"},
    ]
    out = key_calls_by_accession(rows, twins={"NC_1": frozenset({"AY1"})})
    assert {(r["assay_id"], r["record_id"]) for r in out} == {("A", "AY1"), ("B", "NC_1"), ("C", "AY1")}


def test_any_one_twin_in_the_assay_is_enough():
    rows = [
        {"assay_id": "A", "record_id": "NC_1.1", "call": "fail"},
        {"assay_id": "A", "record_id": "KX1.1", "call": "detect"},
    ]
    out = key_calls_by_accession(rows, twins={"NC_1": frozenset({"AY1", "KX1"})})
    assert [r["record_id"] for r in out] == ["KX1"]


def test_without_a_map_only_the_nz_rule_applies():
    rows = [
        {"assay_id": "A", "record_id": "NC_1.1", "call": "fail"},
        {"assay_id": "A", "record_id": "AY1.1", "call": "detect"},
        {"assay_id": "A", "record_id": "NZ_CP1.1", "call": "fail"},
        {"assay_id": "A", "record_id": "CP1.1", "call": "detect"},
    ]
    out = key_calls_by_accession(rows)
    assert {r["record_id"] for r in out} == {"NC_1", "AY1", "CP1"}
