"""Tests for assaywatch.composition (ROADMAP "Lineage composition over time").

Synthetic windows only. Each test pins one rule of the stage at its interface.
"""

from __future__ import annotations

import random

from assaywatch.composition import sample_windows
from assaywatch.subcluster import Region


def _region(acc: str, seq: str, full: bool = True) -> Region:
    return Region(acc, seq, 5 if full else 2, 5, full)


def _distinct(n: int, prefix: str, seed: int) -> list[Region]:
    rng = random.Random(seed)
    return [_region(f"{prefix}{i}.1", "".join(rng.choice("ACGT") for _ in range(40))) for i in range(n)]


# ---- sample_windows (step 3) ----


def test_everything_distinct_and_full_flanked_is_taken_under_the_cap():
    regions = _distinct(6, "A", 1)
    years = [2001, 2001, 2002, 2002, 2003, 2003]
    assert sorted(sample_windows(regions, years, cap=100)) == list(range(6))


def test_a_short_flank_window_is_never_sampled():
    """Finding 2: short-flank windows are assigned by containment, never sampled,
    or a 100 bp assembly cut would define a lineage by less sequence than the rest."""
    regions = [*_distinct(2, "A", 2), _region("S1.1", "ACGT" * 10, full=False)]
    assert 2 not in sample_windows(regions, [2001, 2001, 2001], cap=100)


def test_identical_windows_count_once_whatever_their_order():
    """A clone deposited twenty times is one lineage member, not twenty."""
    seq = "ACGTTGCAAC" * 4
    regions = [_region(f"D{i}.1", seq) for i in range(5)] + _distinct(1, "U", 3)
    years = [2010] * 6
    chosen = sample_windows(regions, years, cap=100)
    assert sum(r.seq == seq for r in (regions[i] for i in chosen)) == 1
    shuffled = list(reversed(regions))
    again = sample_windows(shuffled, years, cap=100)
    assert {regions[i].record_id for i in chosen} == {shuffled[i].record_id for i in again}


def test_quiet_years_are_filled_before_busy_ones():
    """Round-robin across years: three records from each of two quiet years are
    all taken before a busy year gets its fourth."""
    regions = _distinct(100, "B", 4) + _distinct(3, "Q", 5) + _distinct(3, "R", 6)
    years = [2020] * 100 + [2005] * 3 + [2010] * 3
    chosen = sample_windows(regions, years, cap=9)
    by_year = sorted(years[i] for i in chosen)
    assert by_year == [2005] * 3 + [2010] * 3 + [2020] * 3


def test_a_cap_left_over_by_a_quiet_year_goes_to_the_others():
    regions = _distinct(50, "B", 7) + _distinct(1, "Q", 8)
    years = [2020] * 50 + [2005]
    chosen = sample_windows(regions, years, cap=10)
    assert len(chosen) == 10
    assert sum(years[i] == 2005 for i in chosen) == 1


def test_the_sample_does_not_depend_on_input_order():
    """Stable cluster ids rest on this: the same archive, read in any order, must
    sample the same records, so which ones are chosen inside a year comes from a
    hash of the accession, not from file order."""
    regions = _distinct(40, "C", 9)
    years = [2000 + (i % 4) for i in range(40)]
    first = {regions[i].record_id for i in sample_windows(regions, years, cap=12)}
    order = list(range(40))
    random.Random(10).shuffle(order)
    regions2 = [regions[i] for i in order]
    years2 = [years[i] for i in order]
    second = {regions2[i].record_id for i in sample_windows(regions2, years2, cap=12)}
    assert first == second


def test_the_accession_version_does_not_change_the_choice():
    """`.1` and `.2` of one accession are one record; a version bump must not
    reshuffle which records a year contributes."""
    a = _distinct(20, "V", 11)
    b = [Region(r.record_id.replace(".1", ".2"), r.seq, 5, 5, True) for r in a]
    years = [2015] * 20
    pick = lambda rs: {rs[i].record_id.split(".")[0] for i in sample_windows(rs, years, cap=5)}  # noqa: E731
    assert pick(a) == pick(b)
