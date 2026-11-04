"""Per-year record counts for the retrieval-coverage series (ROADMAP composition step 17).

What the panel's coverage band rests on: how many records a query returns per deposit
year, against how many the target taxon holds. One counter, two consumers -- the panel
and the release scope verification (decision 2026-11-02) -- so the counts and their cache
live in `retrieve`, which owns NCBI access.

No network here: a fake transport records the queries and returns the counts.
"""

from __future__ import annotations

import gzip
import json
from datetime import date

import pytest

from assaywatch.retrieve import year_counts


class FakeTransport:
    """Counts whatever is asked, recording the calls. `counts` is keyed by (term, year)."""

    def __init__(self, counts: dict[tuple[str, int], int] | None = None, fail: bool = False) -> None:
        self.counts = counts or {}
        self.calls: list[dict[str, str]] = []
        self.fail = fail

    def __call__(self, endpoint: str, params: dict[str, object]) -> str:
        if self.fail:
            raise OSError("no network")
        self.calls.append({k: str(v) for k, v in params.items()})
        year = int(str(params["mindate"])[:4])
        n = self.counts.get((str(params["term"]), year), 0)
        return f"<eSearchResult><Count>{n}</Count></eSearchResult>"


def test_a_year_is_counted_by_its_own_date_range():
    t = FakeTransport({("txid810[Organism:exp]", 2024): 7, ("txid810[Organism:exp]", 2025): 9})
    got = year_counts(t, "txid810[Organism:exp]", [2024, 2025], "pdat")
    assert got == {2024: 7, 2025: 9}
    assert [(c["mindate"], c["maxdate"], c["datetype"]) for c in t.calls] == [
        ("2024/01/01", "2024/12/31", "pdat"),
        ("2025/01/01", "2025/12/31", "pdat"),
    ]
    assert all(c["retmax"] == "0" for c in t.calls), "a count must not fetch records"


def test_the_counts_are_cached_so_a_second_run_asks_nothing(tmp_path):
    cache = tmp_path / ".year-counts.json.gz"
    t = FakeTransport({("q", 2020): 4})
    kw = {"cache": cache, "today": date(2026, 11, 3)}
    assert year_counts(t, "q", [2020], "pdat", **kw) == {2020: 4}
    again = FakeTransport({("q", 2020): 999})
    assert year_counts(again, "q", [2020], "pdat", **kw) == {2020: 4}
    assert again.calls == [], "a cached year was asked again"


def test_the_last_years_are_re_counted_because_deposits_arrive_late(tmp_path):
    """A year's count is not final when the year is: records are deposited and
    re-annotated for a long time afterwards, so the recent tail is refreshed."""
    cache = tmp_path / ".year-counts.json.gz"
    cold = FakeTransport({("q", 2023): 1, ("q", 2024): 2, ("q", 2025): 3})
    year_counts(cold, "q", [2023, 2024, 2025], "pdat", cache=cache, today=date(2025, 6, 1))
    t = FakeTransport({("q", 2023): 11, ("q", 2024): 22, ("q", 2025): 33})
    # "the last two years" is a fact about now: in mid-2025 that is 2024 and 2025
    got = year_counts(
        t, "q", [2023, 2024, 2025], "pdat", cache=cache, refresh_years=2, today=date(2025, 6, 1)
    )
    assert got == {2023: 1, 2024: 22, 2025: 33}
    assert [int(c["mindate"][:4]) for c in t.calls] == [2024, 2025]


def test_a_refresh_of_zero_years_trusts_the_cache_entirely(tmp_path):
    cache = tmp_path / ".year-counts.json.gz"
    year_counts(FakeTransport({("q", 2025): 5}), "q", [2025], "pdat", cache=cache)
    t = FakeTransport({("q", 2025): 50})
    assert year_counts(t, "q", [2025], "pdat", cache=cache, refresh_years=0) == {2025: 5}
    assert t.calls == []


def test_offline_falls_back_to_the_cache_rather_than_failing_the_run(tmp_path):
    """The stage is report-only and runs in a pipeline that must not stop because NCBI is
    unreachable: a coverage series the reader is told is stale beats no report."""
    cache = tmp_path / ".year-counts.json.gz"
    year_counts(FakeTransport({("q", 2024): 8}), "q", [2024], "pdat", cache=cache)
    assert year_counts(FakeTransport(fail=True), "q", [2024], "pdat", cache=cache, refresh_years=5) == {
        2024: 8
    }


def test_offline_with_nothing_cached_says_so_rather_than_counting_zero():
    """Zero records and "we could not ask" are different facts, and a band drawn from the
    first when the second is true invents a retrieval gap."""
    assert year_counts(FakeTransport(fail=True), "q", [2024], "pdat") == {}


def test_two_queries_do_not_share_a_cache_entry(tmp_path):
    cache = tmp_path / ".year-counts.json.gz"
    t = FakeTransport({("a", 2020): 1, ("b", 2020): 2})
    kw = {"cache": cache, "today": date(2026, 11, 3)}
    assert year_counts(t, "a", [2020], "pdat", **kw) == {2020: 1}
    assert year_counts(t, "b", [2020], "pdat", **kw) == {2020: 2}
    assert year_counts(FakeTransport(), "a", [2020], "pdat", **kw) == {2020: 1}


def test_the_datetype_is_part_of_the_key(tmp_path):
    """`pdat` is when a record was published and `mdat` when it last changed; a count
    under one is not a count under the other, and the archive dates by `created`."""
    cache = tmp_path / ".year-counts.json.gz"
    kw = {"cache": cache, "today": date(2026, 11, 3)}
    t = FakeTransport({("q", 2020): 3})
    assert year_counts(t, "q", [2020], "pdat", **kw) == {2020: 3}
    t2 = FakeTransport({("q", 2020): 4})
    assert year_counts(t2, "q", [2020], "mdat", **kw) == {2020: 4}
    assert len(t2.calls) == 1, "the mdat count read the pdat cache entry"


def test_the_cache_is_readable_json_so_a_bad_entry_can_be_found_by_hand(tmp_path):
    cache = tmp_path / ".year-counts.json.gz"
    year_counts(FakeTransport({("q", 2025): 3}), "q", [2025], "pdat", cache=cache)
    with gzip.open(cache, "rt") as fh:
        data = json.load(fh)
    assert any("q" in key for key in data), data


def test_a_corrupt_cache_is_a_cold_cache_and_not_a_crash(tmp_path):
    cache = tmp_path / ".year-counts.json.gz"
    cache.write_bytes(b"not gzip")
    t = FakeTransport({("q", 2025): 3})
    assert year_counts(t, "q", [2025], "pdat", cache=cache) == {2025: 3}
    assert len(t.calls) == 1


def test_no_year_asks_nothing():
    t = FakeTransport()
    assert year_counts(t, "q", [], "pdat") == {}
    assert t.calls == []


@pytest.mark.parametrize("bad", [1899, 3001])
def test_a_year_outside_the_plausible_range_is_refused(bad):
    """A nonsense year would silently count the whole database: esearch takes the range
    it is given."""
    with pytest.raises(ValueError, match="year"):
        year_counts(FakeTransport(), "q", [bad], "pdat")
