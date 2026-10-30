"""`assaywatch.calls`: which deposits can still matter to the collection clock.

The collection-year lens re-dates records by collection year. A record whose COLLECTION
year cannot reach any recent window cannot change a number the lens prints, so its
collection date need not be fetched at all -- and fetching it is the expensive part:
714,713 of 1,243,065 records on the 2026-10-27 run fall outside the widest window.

That is a proof rather than an approximation, resting on two facts. The widest window any
assay reaches is `drift.max_window_months`, after every widening. And collection precedes
deposit: measured 2026-10-30 over 59,968 records carrying both, ZERO have a collection
year later than their deposit year. So a record deposited before the cutoff was collected
before it too.
"""

from __future__ import annotations

import gzip
from datetime import date
from pathlib import Path

from assaywatch import calls as C

CFG = {"drift": {"recent_window_months": 24, "max_window_months": 60}}


def test_the_cutoff_is_a_year_and_comes_from_the_widest_window_not_the_base():
    """A YEAR, because the collection clock compares at year granularity.

    `drift.Window.inside` compares `int(iso[:4]) >= edge.year` when the input holds bare
    years, which is what the collection clock passes. So a record collected in January of
    the edge year is recent against an October cutoff. Comparing full dates would drop
    records deposited early in the edge year whose collection year still counts, and the
    whole point of this filter is that it discards nothing the report could see.

    And `max_window_months`, never `recent_window_months`: the per-assay window widens up
    to the maximum when records are scarce, so the base would be the silent wrong answer.
    """
    assert C.earliest_relevant_year(CFG, today=date(2026, 10, 30)) == 2021
    # 24 months would give 2024 -- taking the base window would discard three years of
    # records that a widened window can still reach.
    assert C.earliest_relevant_year({"drift": {"max_window_months": 24}}, date(2026, 10, 30)) == 2024
    # Exact calendar arithmetic, via drift.months_back, not 30.44-day months.
    assert C.earliest_relevant_year(CFG, today=date(2026, 1, 31)) == 2021
    assert C.earliest_relevant_year(CFG, today=date(2026, 2, 1)) == 2021
    # An empty config falls back to the settings model's 60, not to the base window.
    # tests/test_settings.py pins that agreement, and caught 24 here on the first attempt.
    assert C.earliest_relevant_year({}, today=date(2026, 10, 30)) == 2021


def test_a_record_whose_deposit_year_is_unknown_is_kept(tmp_path: Path):
    """Fail open. An undatable deposit cannot be PROVEN irrelevant, so it is fetched.

    97 records in the 2026-10-27 calls table carry no deposit date. Dropping them would
    trade a provable filter for a guess, which is the one thing this filter must not do.
    """
    meta = tmp_path / "7777" / "all"
    meta.mkdir(parents=True)
    with gzip.open(meta / "a.meta.tsv.gz", "wt", newline="") as fh:
        fh.write("accession\tcreated\tupdated\n")
        fh.write("AB000001.1\t2025-06-01\t\n")  # inside
        fh.write("AB000002.1\t2019-01-01\t\n")  # outside
        fh.write("AB000003.1\t2021-02-01\t\n")  # early in the edge year: KEPT
    want = ["AB000001.1", "AB000002.1", "AB000003.1", "AB999999.9"]
    got = C.accessions_worth_dating(tmp_path, want, 2021)
    assert got == ["AB000001.1", "AB000003.1", "AB999999.9"]


def test_keys_come_back_as_the_caller_spelled_them(tmp_path: Path):
    """The archives key on a bare accession; the calls table keys on accession.version."""
    meta = tmp_path / "7777" / "all"
    meta.mkdir(parents=True)
    with gzip.open(meta / "a.meta.tsv.gz", "wt", newline="") as fh:
        fh.write("accession\tcreated\tupdated\n")
        fh.write("AB000001.2\t2025-06-01\t\n")
    assert C.accessions_worth_dating(tmp_path, ["AB000001.2"], 2021) == ["AB000001.2"]
    assert C.accessions_worth_dating(tmp_path, ["AB000001"], 2021) == ["AB000001"]
