"""Tests for assaywatch.sitedrift.

The statistics are checked against hand-computable cases, and the position
convention is pinned down explicitly: getting 3'-vs-5' the wrong way round
would point a redesign at the wrong base while looking perfectly plausible.
"""

import gzip

import pytest

from assaywatch.sitedrift import (
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
    assert s.three_prime is (5 <= s.three_prime_zone)


def test_three_prime_zone_follows_the_scorers_window():
    """The marker must come from `scoring.primer_3prime_window`, not a second constant."""
    seq = "GCGTA"
    rows = [row("fail", forward=[3])] * 3
    wide = position_stats(rows, "forward", seq, min_records=1, three_prime_zone=3)[0]
    narrow = position_stats(rows, "forward", seq, min_records=1, three_prime_zone=2)[0]
    assert (wide.three_prime, narrow.three_prime) == (True, False)


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
    # Asserted on the claims rather than on the word "never", which is what this
    # checked until 2026-10-27: the prose it was guarding had gone stale (it said
    # the substituted base is not recorded, which stopped being true on
    # 2026-10-26) and the proxy word could not notice. Rewritten again the same
    # day, because the base IS now named and the old caveat became the false one.
    assert "records carry" in md and "order" in md
    assert "the base you would order to restore inclusivity" in md
    # The limit that survived: footprint groups still key on positions alone.
    assert "two records differing in base at one position are still one group" in md
    # And the pool caveat is stated rather than silently wrong.
    assert "pool assay when the winning alternate differs" in md
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


# --------------------------------------------------------------------------
# Naming the substituted base (2026-10-27). The direction of the complement is
# the part worth pinning: score.py records the TEMPLATE base, and a redesign
# needs the base the RECORD carries, so getting it backwards would print the
# wrong replacement with full confidence.
# --------------------------------------------------------------------------


def test_parse_mispairs_complements_the_template_back_to_the_record_base():
    from assaywatch.sitedrift import parse_mispairs

    # score.py wrote G:T@7 for an oligo G facing template T. The record itself
    # therefore carries A (the complement of T) in the oligo's own sense.
    assert parse_mispairs("G:T@7") == (("G", "A", 7),)
    assert parse_mispairs("A:C@2,G:A@14") == (("A", "G", 2), ("G", "T", 14))
    assert parse_mispairs("") == () and parse_mispairs(None) == ()
    # Malformed cells are dropped, not guessed at.
    assert parse_mispairs("junk,G:T@,:@5,G:T@7") == (("G", "A", 7),)


def test_substitutions_name_the_replacement_code():
    from assaywatch.sitedrift import PositionStat

    # Oligo G, records carry A: order R.
    p = PositionStat(
        oligo="forward",
        pos_3prime=3,
        pos_5prime=10,
        base="G",
        n_mismatch=754,
        detected_with=0,
        evaluable_with=754,
        detected_without=3,
        evaluable_without=3,
        substitutions=(("G", "A", 749), ("G", "T", 5)),
    )
    # G plus A plus T is D, not R: the replacement has to cover EVERY base seen,
    # or it restores inclusivity for 749 records and not the other 5.
    assert p.replacement == "D"
    assert p.scored_bases == ("G",)
    assert not p.base_disagrees


def test_a_single_substitution_gives_the_two_base_code():
    from assaywatch.sitedrift import PositionStat

    p = PositionStat("forward", 3, 10, "G", 749, 0, 749, 3, 3, substitutions=(("G", "A", 749),))
    assert p.replacement == "R"


def test_a_pool_assay_whose_alternates_differ_refuses_to_name_one_base():
    from assaywatch.sitedrift import PositionStat

    # Two different oligo bases scored at one position: the primary oligo's base
    # is not "the" base, so no single replacement is honest.
    p = PositionStat("forward", 3, 10, "G", 100, 0, 100, 0, 0, substitutions=(("G", "A", 60), ("A", "G", 40)))
    assert p.replacement is None
    assert p.base_disagrees is True
    assert p.scored_bases == ("A", "G")


def test_no_replacement_is_offered_when_the_code_would_be_the_oligos_own_base():
    from assaywatch.sitedrift import PositionStat

    # A record base already covered by a degenerate oligo base is not a redesign.
    p = PositionStat("forward", 3, 10, "R", 10, 0, 10, 0, 0, substitutions=(("R", "A", 10),))
    assert p.replacement is None


def test_an_ambiguous_record_base_gets_no_replacement_rather_than_N():
    from assaywatch.sitedrift import PositionStat

    p = PositionStat("forward", 3, 10, "G", 10, 0, 10, 0, 0, substitutions=(("G", "N", 10),))
    assert p.replacement is None


def test_replacement_share_says_how_much_of_the_drift_the_code_covers():
    """Untested at first, and the one line it covers had a 3-tuple unpacked as a
    pair -- which every other test passed straight over because none of them
    touched this property."""
    from assaywatch.sitedrift import PositionStat

    # 749 A and 5 T. At cover=0.95, A alone clears the bar, so the code is R and
    # it covers 749/754 of the mismatching records, not all of them.
    p = PositionStat(
        "forward", 3, 10, "G", 754, 0, 754, 3, 3, substitutions=(("G", "A", 749), ("G", "T", 5)), cover=0.95
    )
    assert p.replacement == "R"
    assert p.replacement_share is not None
    assert abs(p.replacement_share - 749 / 754) < 1e-9
    assert not p.hypervariable

    # At cover=1.0 the rare T is chased too, so the code widens and covers all.
    q = PositionStat(
        "forward", 3, 10, "G", 754, 0, 754, 3, 3, substitutions=(("G", "A", 749), ("G", "T", 5)), cover=1.0
    )
    assert q.replacement == "D" and q.replacement_share == 1.0


def test_a_position_carrying_every_base_is_hypervariable_not_an_order_for_N():
    from assaywatch.sitedrift import PositionStat

    p = PositionStat(
        "forward",
        3,
        10,
        "G",
        300,
        0,
        300,
        0,
        0,
        substitutions=(("G", "A", 100), ("G", "C", 100), ("G", "T", 100)),
        cover=1.0,
    )
    assert p.hypervariable is True
    # The code is still N in the machine-readable column; the renderer is what
    # refuses to print it as an instruction.
    assert p.replacement == "N"


def test_a_probe_assay_counts_a_mismatched_probe_the_way_the_report_does():
    """The site table and the report must agree about what a detection is.

    `_detected` took a `detected_calls` parameter so `drift.reduced_not_detected_for`
    could narrow it, and no caller ever passed one -- so for all 56 probe assays the
    site table counted a mismatched probe as a detection while the report did not.
    Measured 2026-10-28 on MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010: its two
    commonest variant sites read 99.97% and 99.98% detected in site-drift.tsv against
    the report's 57.9%, and the whole gap was this.
    """
    from assaywatch.sitedrift import position_stats

    # Ten records carrying a mismatch at position 3 from the 3' end: five amplify
    # cleanly, five amplify with a degraded probe.
    rows = [{"call": "detect", "probe": (3,)} for _ in range(5)]
    rows += [{"call": "reduced", "probe": (3,)} for _ in range(5)]
    seq = "ACGTACGTACGT"

    (both,) = position_stats(rows, "probe", seq, min_records=1)
    (strict,) = position_stats(rows, "probe", seq, min_records=1, detected_calls=("detect",))
    assert both.detected_with == 10, "the default still counts `reduced` as a detection"
    assert strict.detected_with == 5, "a probe assay must not count a degraded probe"
    assert both.evaluable_with == strict.evaluable_with == 10
