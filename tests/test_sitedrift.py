"""Tests for assaywatch.sitedrift.

The statistics are checked against hand-computable cases, and the position
convention is pinned down explicitly: getting 3'-vs-5' the wrong way round
would point a redesign at the wrong base while looking perfectly plausible.
"""

import gzip

import pytest

from assaywatch.sitedrift import (
    THREE_PRIME_ZONE,
    PositionStat,
    footprint_groups,
    organism_from_title,
    parse_positions,
    position_stats,
    read_site_calls,
    read_titles,
    render_markdown,
    render_tsv,
)


def row(call, forward=(), reverse=(), probe=(), record_id="A1", assay_id="X"):
    return {
        "assay_id": assay_id,
        "record_id": record_id,
        "call": call,
        "forward": tuple(forward),
        "reverse": tuple(reverse),
        "probe": tuple(probe),
    }


# -- parsing ---------------------------------------------------------------


@pytest.mark.parametrize(
    "cell,expected",
    [("14,6,2", (2, 6, 14)), ("", ()), (None, ()), ("3", (3,)), ("a,2", (2,)), (" 5 , 1 ", (1, 5))],
)
def test_parse_positions(cell, expected):
    assert parse_positions(cell) == expected


# -- the position convention ----------------------------------------------


def test_position_1_is_the_three_prime_terminal_base():
    """`1` must be the LAST base of the written sequence, not the first."""
    seq = "ACGTA"  # 5 nt; position 1 from 3' is the final A
    stats = position_stats([row("fail", forward=[1])] * 5, "forward", seq, min_records=1)
    assert len(stats) == 1
    s = stats[0]
    assert s.pos_3prime == 1
    assert s.pos_5prime == 5
    assert s.base == "A"  # seq[-1]
    assert s.three_prime is True


def test_five_prime_end_maps_to_the_largest_three_prime_index():
    seq = "GCGTA"
    stats = position_stats([row("fail", forward=[5])] * 3, "forward", seq, min_records=1)
    s = stats[0]
    assert (s.pos_3prime, s.pos_5prime, s.base) == (5, 1, "G")
    assert s.three_prime is (5 <= THREE_PRIME_ZONE)


def test_positions_outside_the_oligo_are_ignored():
    """A position longer than the primer is bad data, not a silent extra base."""
    seq = "ACGT"
    assert position_stats([row("fail", forward=[99])] * 5, "forward", seq, min_records=1) == []


# -- the statistics --------------------------------------------------------


def test_detected_shares_split_on_the_position():
    """Hand-computable: 10 mismatching records all fail, 10 clean all detect."""
    rows = [row("fail", forward=[2]) for _ in range(10)] + [row("detect") for _ in range(10)]
    (s,) = position_stats(rows, "forward", "ACGTACGT", min_records=5)
    assert s.n_mismatch == 10
    assert s.detected_with == 0
    assert s.evaluable_with == 10
    assert s.detected_without == 10
    assert s.evaluable_without == 10
    assert s.share_with == 0.0
    assert s.share_without == 1.0
    assert s.gap == 1.0


def test_reduced_counts_as_detected():
    """Matches drift.YearStats.detected, so the two reports cannot disagree."""
    rows = [row("reduced", forward=[3]) for _ in range(6)]
    (s,) = position_stats(rows, "forward", "ACGTACGT", min_records=1)
    assert s.detected_with == 6
    assert s.share_with == 1.0


def test_min_records_suppresses_thin_positions():
    rows = [row("fail", forward=[2]) for _ in range(3)] + [row("detect") for _ in range(50)]
    assert position_stats(rows, "forward", "ACGTACGT", min_records=20) == []
    assert len(position_stats(rows, "forward", "ACGTACGT", min_records=3)) == 1


def test_positions_are_ranked_by_gap_not_frequency():
    """A common but harmless position must rank below a rare damaging one."""
    rows = []
    # position 8: very common, no effect on detection
    rows += [row("detect", forward=[8]) for _ in range(100)]
    # position 2: rarer, always fatal
    rows += [row("fail", forward=[2]) for _ in range(20)]
    rows += [row("detect") for _ in range(100)]
    stats = position_stats(rows, "forward", "ACGTACGT", min_records=10)
    assert stats[0].pos_3prime == 2
    assert stats[0].gap > stats[1].gap


def test_empty_sequence_gives_no_statistics():
    assert position_stats([row("fail", forward=[1])], "forward", "", min_records=1) == []


# -- footprint groups ------------------------------------------------------


def test_footprints_group_identical_patterns():
    rows = [row("fail", forward=[2, 5], reverse=[3], record_id=f"A{i}") for i in range(4)] + [
        row("detect", record_id=f"B{i}") for i in range(6)
    ]
    dates = {f"A{i}": "2025-03-01" for i in range(4)} | {f"B{i}": "2024-01-01" for i in range(6)}
    groups = footprint_groups(rows, dates, {}, top=10)
    assert [g.n for g in groups] == [6, 4]
    clean, failing = groups
    assert clean.clean is True
    assert failing.dominant_call == "fail"
    assert failing.describe() == "fwd 2,5; rev 3"
    assert failing.years == {"2025": 4}


def test_footprints_are_capped_to_top_n():
    rows = [row("fail", forward=[i], record_id=f"R{i}") for i in range(30)]
    assert len(footprint_groups(rows, {}, {}, top=5)) == 5


def test_footprint_organisms_use_titles_when_present():
    rows = [row("fail", forward=[2], record_id="A1"), row("fail", forward=[2], record_id="A2")]
    titles = {"A1": "Leptospira interrogans strain X gene", "A2": "Leptospira interrogans isolate Y"}
    (g,) = footprint_groups(rows, {}, titles, top=5)
    assert g.organisms["Leptospira interrogans"] == 2


# -- titles ----------------------------------------------------------------


@pytest.mark.parametrize(
    "title,expected",
    [
        ("Leptospira interrogans strain X lipL32 gene", "Leptospira interrogans"),
        ("Uncultured Leptospira sp. clone ICARNEH gene, partial cds", "Leptospira sp."),
        ("UNVERIFIED: Canine distemper virus isolate", "Canine distemper"),
        ("", "unknown"),
    ],
)
def test_organism_from_title(title, expected):
    assert organism_from_title(title) == expected


def test_read_titles_keeps_only_requested_accessions(tmp_path):
    meta = tmp_path / "g" / "2026-01-01.meta.tsv.gz"
    meta.parent.mkdir(parents=True)
    with gzip.open(meta, "wt", newline="") as fh:
        fh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
        fh.write("1\tAB1.2\t2026-01-01\t2026-01-01\t100\tWanted organism gene\n")
        fh.write("2\tZZ9.1\t2026-01-01\t2026-01-01\t100\tUnwanted organism gene\n")
    got = read_titles(tmp_path, {"AB1"})
    assert got == {"AB1": "Wanted organism gene"}


def test_read_titles_with_no_accessions_reads_nothing(tmp_path):
    assert read_titles(tmp_path, set()) == {}


# -- reading the calls table ----------------------------------------------


def test_read_site_calls_filters_and_parses(tmp_path):
    path = tmp_path / "calls.tsv.gz"
    with gzip.open(path, "wt", newline="") as fh:
        fh.write("assay_id\trecord_id\tcall\tfwd_mm_from_3prime\trev_mm_from_3prime\tprobe_mm_from_3prime\n")
        fh.write("KEEP\tA1.1\tfail\t2,5\t3\t\n")
        fh.write("DROP\tB1.1\tdetect\t\t\t\n")
    rows = read_site_calls(path, {"KEEP"})
    assert len(rows) == 1
    assert rows[0]["forward"] == (2, 5)
    assert rows[0]["reverse"] == (3,)
    assert rows[0]["probe"] == ()


def test_read_site_calls_tolerates_a_missing_probe_column(tmp_path):
    path = tmp_path / "calls.tsv"
    path.write_text("assay_id\trecord_id\tcall\tfwd_mm_from_3prime\nKEEP\tA1.1\tfail\t2\n")
    (r,) = read_site_calls(path, {"KEEP"})
    assert r["forward"] == (2,) and r["probe"] == ()


def test_read_site_calls_rejects_a_table_without_the_key_columns(tmp_path):
    path = tmp_path / "bad.tsv"
    path.write_text("a\tb\n1\t2\n")
    with pytest.raises(ValueError):
        read_site_calls(path, {"KEEP"})


def test_read_site_calls_on_an_empty_file(tmp_path):
    path = tmp_path / "empty.tsv"
    path.write_text("")
    assert read_site_calls(path, {"X"}) == []


# -- rendering -------------------------------------------------------------


def _sites():
    from assaywatch.sitedrift import AssaySites, FootprintGroup

    return AssaySites(
        assay_id="DEMO",
        taxon="Demo virus",
        taxid=123,
        status="declining",
        oligo_seqs={"forward": "ACGTACGT"},
        positions=[
            PositionStat("forward", 2, 7, "G", 10, 0, 10, 90, 90),
        ],
        footprints=[FootprintGroup(positions={"forward": (2,)}, n=10)],
        n_evaluable=100,
        n_rows=120,
    )


def test_markdown_states_both_conventions_and_the_limits():
    md = render_markdown([_sites()], "2026-10-17", min_records=20)
    assert "pos(3')" in md and "pos(5')" in md
    # The report must carry its own caveats, not rely on the reader knowing them.
    assert "never" in md and "base" in md
    assert "DEMO" in md and "taxid 123" in md


def test_tsv_has_one_row_per_position_plus_header():
    tsv = render_tsv([_sites()]).strip().splitlines()
    assert len(tsv) == 2
    assert tsv[0].split("\t")[0] == "assay_id"
    assert tsv[1].split("\t")[:2] == ["DEMO", "declining"]


def test_assay_with_no_evaluable_records_renders_without_crashing():
    from assaywatch.sitedrift import AssaySites

    empty = AssaySites("E", "T", None, "low coverage", {"forward": "ACGT"}, [], [], 0, 0)
    md = render_markdown([empty], "2026-10-17", min_records=20)
    assert "No evaluable records" in md
