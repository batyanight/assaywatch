"""The founding premise, measured -- and kept distinct from the authors' own count."""

from __future__ import annotations

import gzip
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("design_era", ROOT / "scripts" / "design_era.py")
design_era = importlib.util.module_from_spec(_spec)
sys.modules["design_era"] = design_era
_spec.loader.exec_module(design_era)


def _archive(root: Path, taxid: int, group: str, rows: list[tuple[str, str]]) -> None:
    d = root / str(taxid) / group
    d.mkdir(parents=True)
    with gzip.open(d / "2026-01-01.meta.tsv.gz", "wt") as fh:
        fh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
        for acc, created in rows:
            fh.write(f"1\t{acc}\t{created}\t\t500\tt\n")


def test_deposits_are_counted_once_per_accession_across_archives(tmp_path):
    """Archives are per group and a record belongs to every group whose query
    matches it, so the same accession appears more than once. Counting it twice
    would inflate the denominator."""
    _archive(tmp_path, 109871, "all", [("AB1", "2003-01-01"), ("AB2", "2005-01-01")])
    _archive(tmp_path, 109871, "q1234", [("AB1", "2003-01-01"), ("AB3", "2010-01-01")])
    years = design_era.deposits_by_taxon(tmp_path)
    assert sorted(years[109871]) == [2003, 2005, 2010], "AB1 is in two groups and counts once"


def test_undated_and_malformed_rows_are_skipped_not_guessed(tmp_path):
    _archive(tmp_path, 11082, "all", [("A", "2001-01-01"), ("B", ""), ("C", "no date")])
    assert design_era.deposits_by_taxon(tmp_path)[11082] == [2001]


def test_the_two_counts_are_reported_side_by_side_and_never_merged():
    """`citation.n_sequences_at_design` is how many sequences THE AUTHORS aligned,
    which only their paper can say. This script measures how many EXISTED for the
    target taxon. An author who aligned 8 of 42 available is in a different
    position from one who aligned 8 of 8, so the columns stay separate and this
    script fills no registry field.

    Two rows prove the archive is not GenBank: Nosema apis (authors 6, archive 5)
    and Leporid gammaherpesvirus 5 (authors 5, archive 0) report the authors
    aligning MORE than the archive shows existed. That is the documented limit --
    an archive counts what its group's query returned -- disclosing itself.
    """
    import csv

    path = ROOT / "docs" / "design-era.tsv"
    assert path.exists(), "run: python scripts/design_era.py --out docs/design-era.tsv"
    rows = list(csv.DictReader(path.open(), delimiter="\t"))
    assert {"records_before_design", "authors_n_sequences"} <= set(rows[0])

    both = [r for r in rows if r["authors_n_sequences"]]
    assert both, "some entries carry the authors' own count"
    over = [r for r in both if int(r["authors_n_sequences"]) > int(r["records_before_design"])]
    assert over, (
        "no row shows the authors aligning more than the archive holds -- if that "
        "became true, check whether the two quantities have been conflated"
    )
