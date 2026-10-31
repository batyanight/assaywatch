"""`scripts/check_archive_recency.py`: the date arithmetic and the sidecar reader.

The script itself is a worklist generator whose value is measured and modest (see its
docstring: four candidates on 2026-10-30, all four fine). What is worth testing is the two
pieces that could be quietly wrong and would corrupt the list: reading the newest deposit
date out of sidecars whose columns differ between files, and the month arithmetic.
"""

from __future__ import annotations

import gzip
import importlib.util
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "check_archive_recency", ROOT / "scripts" / "check_archive_recency.py"
)
assert _spec and _spec.loader
recency = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(recency)


def _sidecar(path: Path, header: list[str], rows: list[list[str]]) -> None:
    with gzip.open(path, "wt") as fh:
        fh.write("\t".join(header) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")


def test_the_newest_date_is_found_across_sidecars_with_different_columns(tmp_path: Path):
    """The influenza matrix group has 19 sidecars and only one carries `taxid`, because the
    schema gained columns partway through. A reader that trusts the first file's header, or
    a fixed column index, silently reads the wrong field or none."""
    _sidecar(tmp_path / "a.meta.tsv.gz", ["uid", "accession", "created"], [["1", "A1", "2019-05-01"]])
    _sidecar(
        tmp_path / "b.meta.tsv.gz",
        ["uid", "accession", "created", "updated", "taxid", "is_patent"],
        [
            ["2", "A2", "2024-11-30", "2024-12-01", "11320", "false"],
            ["3", "A3", "2021-01-01", "", "11320", "false"],
        ],
    )
    newest, n = recency.newest_deposit(tmp_path)
    assert newest == "2024-11-30"
    assert n == 3


def test_a_sidecar_with_no_created_column_still_contributes_its_count(tmp_path: Path):
    """Otherwise an archive of real records reads as empty, which the script would print as
    "never fetched" -- the opposite of the truth."""
    _sidecar(
        tmp_path / "a.meta.tsv.gz", ["uid", "accession", "length"], [["1", "A1", "900"], ["2", "A2", "901"]]
    )
    newest, n = recency.newest_deposit(tmp_path)
    assert newest is None
    assert n == 2


def test_an_empty_directory_reads_as_never_fetched(tmp_path: Path):
    assert recency.newest_deposit(tmp_path) == (None, 0)


def test_month_arithmetic_handles_both_date_spellings_and_year_boundaries():
    """GenBank's `created` arrives as `2024-11-30` and, in older sidecars, `2024/11/30`."""
    now = date(2026, 10, 30)
    assert recency.months_between("2026-10-01", now) == 0
    assert recency.months_between("2026-09-30", now) == 1
    assert recency.months_between("2025-10-31", now) == 12
    assert recency.months_between("2021/11/13", now) == 59
    # a year-only date is treated as January of that year, not as today
    assert recency.months_between("2020", now) == 81  # Jan 2020 -> Oct 2026
