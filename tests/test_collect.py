"""Gathering cached screens into one calls table.

This logic lived in a Snakefile `run:` block, so none of it could be tested,
including the case it was written for: a screen cached before a column existed
meeting one written after. Plain concatenation would shift the older file's rows
a column sideways and corrupt every call in them, with no error and a report
that looks normal.
"""

from __future__ import annotations

import csv
import gzip
import json
import os
from datetime import UTC, datetime
from pathlib import Path

import pytest

from assaywatch.collect import (
    LINE_END,
    _runtime,
    assays_without_calls,
    concatenate_screens,
    read_header,
    screen_stats,
    stem_order,
    stored_signature,
    unified_columns,
)
from assaywatch.screen import signature_path


def write_screen(path: Path, columns: list[str], rows: list[dict]) -> Path:
    """A cached screen exactly as screen.py writes one: csv.DictWriter, CRLF."""
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, columns, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    return path


def read_table(path: Path) -> list[dict]:
    with gzip.open(path, "rt", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


OLD = ["assay_id", "record_id", "call", "penalty"]
NEW = ["assay_id", "record_id", "call", "penalty", "exclusion", "pair_evalue"]


def test_stems_sort_in_fetch_order_not_text_order():
    """`_10` sorts before `_2` as text. Archives are concatenated oldest first so
    that the newest version of an accession wins, so the wrong order silently
    makes an OLDER version win."""
    names = [
        "2026-10-05.fasta.gz",
        "2026-10-04_10.fasta.gz",
        "2026-10-04.fasta.gz",
        "2026-10-04_2.fasta.gz",
    ]
    assert sorted(names) != [
        "2026-10-04.fasta.gz",
        "2026-10-04_2.fasta.gz",
        "2026-10-04_10.fasta.gz",
        "2026-10-05.fasta.gz",
    ]  # the plain text sort IS wrong
    ordered = sorted((Path(n) for n in names), key=stem_order)
    assert [p.name for p in ordered] == [
        "2026-10-04.fasta.gz",
        "2026-10-04_2.fasta.gz",
        "2026-10-04_10.fasta.gz",
        "2026-10-05.fasta.gz",
    ]


def test_stem_order_reads_screen_files_too():
    """archives() sorts FASTA paths, but the same stems name the screens."""
    assert stem_order(Path("2026-10-04_3.tsv")) == ("2026-10-04", 3)
    assert stem_order(Path("2026-10-04.tsv")) == ("2026-10-04", 1)


def test_consistent_screens_are_copied_through_untouched(tmp_path):
    rows_a = [{"assay_id": "A", "record_id": "R1", "call": "detect", "penalty": "0.0"}]
    rows_b = [{"assay_id": "A", "record_id": "R2", "call": "fail", "penalty": "3.0"}]
    a = write_screen(tmp_path / "a.tsv", OLD, rows_a)
    b = write_screen(tmp_path / "b.tsv", OLD, rows_b)
    out = tmp_path / "calls.tsv.gz"
    assert concatenate_screens([a, b], out) == OLD
    assert read_table(out) == [*rows_a, *rows_b]
    # These rows are already what a csv writer produces, so this checks content and
    # order only. That the copy path really copies, rather than parsing and
    # rewriting, needs rows a csv writer would change: see the next test.
    raw = gzip.open(out, "rb").read()
    assert raw.endswith(a.read_bytes().split(b"\r\n", 1)[1] + b.read_bytes().split(b"\r\n", 1)[1])


def test_the_copy_path_copies_bytes_instead_of_parsing_and_rewriting_rows(tmp_path):
    """The usual case is thousands of screens of millions of rows with identical
    columns, and what makes it cheap is that rows are copied, not parsed. Nothing
    above can tell: every other fixture is written by a csv writer, so parsing and
    rewriting such a row gives back the same bytes.

    A field that arrives quoted when it did not need to be is a row a csv writer
    would not produce: reading it and writing it again drops the quotes. So if the
    quotes survive, the row was copied.
    """
    header = "\t".join(OLD) + LINE_END
    quoted = '"A"\tR1\tdetect\t0.0' + LINE_END
    plain = "A\tR2\tfail\t3.0" + LINE_END
    a, b = tmp_path / "a.tsv", tmp_path / "b.tsv"
    a.write_bytes((header + quoted).encode())
    b.write_bytes((header + plain).encode())
    out = tmp_path / "calls.tsv.gz"
    concatenate_screens([a, b], out)
    assert gzip.open(out, "rb").read() == (header + quoted + plain).encode()
    assert [r["assay_id"] for r in read_table(out)] == ["A", "A"]  # and still parses as the value


def test_the_rewrite_path_normalises_quoting_which_is_why_the_copy_path_matters(tmp_path):
    """The other side of the same fact, so the test above is shown to mean something:
    the same quoted row, sent through the reconciling path, comes out unquoted."""
    quoted = '"A"\tR1\tdetect\t0.0' + LINE_END
    a, b = tmp_path / "a.tsv", tmp_path / "b.tsv"
    a.write_bytes(("\t".join(OLD) + LINE_END + quoted).encode())
    b.write_bytes(
        ("\t".join(NEW) + LINE_END + "A\tR2\tfail\t3.0\t\t" + LINE_END).encode()
    )  # a different schema forces the rewrite
    out = tmp_path / "calls.tsv.gz"
    concatenate_screens([a, b], out)
    assert b'"A"' not in gzip.open(out, "rb").read()


def test_an_old_screen_meeting_a_new_one_keeps_every_value_in_its_own_column(tmp_path):
    """THE CASE THIS CODE EXISTS FOR.

    The failure it prevents is a shift, so the assertion is on specific cells:
    plain concatenation would put the old file's `penalty` value under
    `exclusion`, and the call counts would still add up.
    """
    old = write_screen(
        tmp_path / "old.tsv",
        OLD,
        [{"assay_id": "A", "record_id": "R1", "call": "fail", "penalty": "3.0"}],
    )
    new = write_screen(
        tmp_path / "new.tsv",
        NEW,
        [
            {
                "assay_id": "A",
                "record_id": "R2",
                "call": "no_amplicon",
                "penalty": "",
                "exclusion": "truncated",
                "pair_evalue": "0.5",
            }
        ],
    )
    out = tmp_path / "calls.tsv.gz"
    assert concatenate_screens([old, new], out) == NEW
    r1, r2 = read_table(out)
    assert (r1["call"], r1["penalty"]) == ("fail", "3.0")
    assert r1["exclusion"] == "" and r1["pair_evalue"] == ""  # not guessed
    assert (r2["exclusion"], r2["pair_evalue"]) == ("truncated", "0.5")


def test_the_newer_screen_first_also_reconciles(tmp_path):
    """Archive order is not column order: a new-schema screen can come first."""
    new = write_screen(
        tmp_path / "new.tsv",
        NEW,
        [
            {
                "assay_id": "A",
                "record_id": "R1",
                "call": "detect",
                "penalty": "0.0",
                "exclusion": "",
                "pair_evalue": "1",
            }
        ],
    )
    old = write_screen(
        tmp_path / "old.tsv",
        OLD,
        [{"assay_id": "A", "record_id": "R2", "call": "fail", "penalty": "3.0"}],
    )
    out = tmp_path / "calls.tsv.gz"
    concatenate_screens([new, old], out)
    r1, r2 = read_table(out)
    assert (r1["record_id"], r1["pair_evalue"]) == ("R1", "1")
    assert (r2["record_id"], r2["penalty"], r2["pair_evalue"]) == ("R2", "3.0", "")


def test_the_same_columns_in_a_different_order_land_under_their_names(tmp_path):
    a = write_screen(
        tmp_path / "a.tsv",
        ["call", "assay_id", "record_id"],
        [{"call": "detect", "assay_id": "A", "record_id": "R1"}],
    )
    b = write_screen(
        tmp_path / "b.tsv",
        ["assay_id", "record_id", "call"],
        [{"call": "fail", "assay_id": "B", "record_id": "R2"}],
    )
    out = tmp_path / "calls.tsv.gz"
    concatenate_screens([a, b], out)
    assert read_table(out) == [
        {"call": "detect", "assay_id": "A", "record_id": "R1"},
        {"call": "fail", "assay_id": "B", "record_id": "R2"},
    ]


def test_columns_are_unioned_in_first_seen_order():
    assert unified_columns([["a", "b"], ["b", "c"], ["a", "d", "c"]]) == ["a", "b", "c", "d"]
    assert unified_columns([["a", ""], ["", "b"]]) == ["a", "b"]  # blank names are dropped


def test_a_zero_byte_screen_contributes_nothing_and_misaligns_nothing(tmp_path):
    """An archive with no matching records can leave an empty file."""
    empty = tmp_path / "empty.tsv"
    empty.write_bytes(b"")
    real = write_screen(
        tmp_path / "real.tsv", OLD, [{"assay_id": "A", "record_id": "R1", "call": "detect", "penalty": "0"}]
    )
    out = tmp_path / "calls.tsv.gz"
    assert concatenate_screens([empty, real], out) == OLD
    assert [r["record_id"] for r in read_table(out)] == ["R1"]
    assert read_header(empty) == [""]


def test_a_header_only_screen_is_fine(tmp_path):
    only = write_screen(tmp_path / "h.tsv", NEW, [])
    real = write_screen(
        tmp_path / "r.tsv", OLD, [{"assay_id": "A", "record_id": "R1", "call": "detect", "penalty": "0"}]
    )
    out = tmp_path / "calls.tsv.gz"
    assert concatenate_screens([only, real], out) == NEW
    assert [r["record_id"] for r in read_table(out)] == ["R1"]


def test_a_screen_with_no_final_line_break_is_refused_not_glued(tmp_path):
    """The copying path appends the next file straight after this one. An
    unterminated last row would have the next file's header glued onto it: one
    corrupt row, silently, in the middle of a report's input."""
    cut = write_screen(
        tmp_path / "cut.tsv", OLD, [{"assay_id": "A", "record_id": "R1", "call": "detect", "penalty": "0"}]
    )
    cut.write_bytes(cut.read_bytes().rstrip(b"\r\n"))
    nxt = write_screen(
        tmp_path / "nxt.tsv", OLD, [{"assay_id": "A", "record_id": "R2", "call": "fail", "penalty": "3"}]
    )
    with pytest.raises(ValueError, match="does not end with a line break"):
        concatenate_screens([cut, nxt], tmp_path / "calls.tsv.gz")


def test_the_refusal_names_the_file_and_says_what_to_do(tmp_path):
    cut = write_screen(
        tmp_path / "2026-10-04.tsv",
        OLD,
        [{"assay_id": "A", "record_id": "R1", "call": "detect", "penalty": "0"}],
    )
    cut.write_bytes(cut.read_bytes().rstrip(b"\r\n"))
    with pytest.raises(ValueError) as e:
        concatenate_screens([cut], tmp_path / "calls.tsv.gz")
    assert "2026-10-04.tsv" in str(e.value) and "rerun" in str(e.value)


def test_line_endings_are_consistent_throughout(tmp_path):
    """The old block wrote its header with a bare LF and every row with CRLF, so
    the first line of a calls table disagreed with the rest."""
    old = write_screen(
        tmp_path / "old.tsv", OLD, [{"assay_id": "A", "record_id": "R1", "call": "fail", "penalty": "3"}]
    )
    new = write_screen(
        tmp_path / "new.tsv",
        NEW,
        [
            {
                "assay_id": "A",
                "record_id": "R2",
                "call": "fail",
                "penalty": "3",
                "exclusion": "",
                "pair_evalue": "",
            }
        ],
    )
    out = tmp_path / "calls.tsv.gz"
    concatenate_screens([old, new], out)
    raw = gzip.open(out, "rb").read()
    assert raw.count(b"\n") == raw.count(b"\r\n") == 3  # header + 2 rows, every one CRLF
    assert raw.startswith("\t".join(NEW).encode() + LINE_END.encode())


def test_the_result_is_readable_by_the_report_stage(tmp_path):
    """End to end through the consumer: what report.read_calls makes of a table
    built from a mixed-schema pair."""
    from assaywatch.report import read_calls

    old = write_screen(
        tmp_path / "old.tsv", OLD, [{"assay_id": "A", "record_id": "R1", "call": "fail", "penalty": "3"}]
    )
    new = write_screen(
        tmp_path / "new.tsv",
        NEW,
        [
            {
                "assay_id": "A",
                "record_id": "R2",
                "call": "no_amplicon",
                "penalty": "",
                "exclusion": "truncated",
                "pair_evalue": "",
            }
        ],
    )
    out = tmp_path / "calls.tsv.gz"
    concatenate_screens([old, new], out)
    rows = read_calls(out)
    assert [(r["record_id"], r["call"], r["exclusion"]) for r in rows] == [
        ("R1", "fail", ""),
        ("R2", "no_amplicon", "truncated"),
    ]


# The real history. `exclusion` and `pair_evalue` were inserted BEFORE the
# per-oligo columns, not appended after them, so an older screen's later columns
# sit at different positions than the same columns in a newer one.
REAL_OLD = ["assay_id", "record_id", "call", "probe_site", "fwd_penalty", "rev_penalty", "reason"]
REAL_NEW = [
    "assay_id",
    "record_id",
    "call",
    "probe_site",
    "exclusion",
    "pair_evalue",
    "fwd_penalty",
    "rev_penalty",
    "reason",
]


def test_a_column_inserted_in_the_middle_does_not_shift_the_values_after_it(tmp_path):
    """The case that actually corrupts, as opposed to merely padding.

    Concatenating an older row under the newer header puts `fwd_penalty`'s value
    under `exclusion`, `rev_penalty`'s under `pair_evalue`, and so on to the end
    of the row. Every call survives and the counts add up, so nothing flags it;
    the corruption is in which penalty belongs to which oligo.
    """
    old = write_screen(
        tmp_path / "old.tsv",
        REAL_OLD,
        [
            {
                "assay_id": "A",
                "record_id": "R1",
                "call": "reduced",
                "probe_site": "10-30+",
                "fwd_penalty": "1.5",
                "rev_penalty": "0.5",
                "reason": "",
            }
        ],
    )
    new = write_screen(
        tmp_path / "new.tsv",
        REAL_NEW,
        [
            {
                "assay_id": "A",
                "record_id": "R2",
                "call": "no_amplicon",
                "probe_site": "",
                "exclusion": "diverged",
                "pair_evalue": "0.02",
                "fwd_penalty": "",
                "rev_penalty": "",
                "reason": "",
            }
        ],
    )
    out = tmp_path / "calls.tsv.gz"
    concatenate_screens([old, new], out)
    r1, r2 = read_table(out)
    # Old row: its penalties stay under the penalty columns...
    assert (r1["fwd_penalty"], r1["rev_penalty"]) == ("1.5", "0.5")
    # ...and the columns it never had are empty rather than holding those values.
    assert r1["exclusion"] == "" and r1["pair_evalue"] == ""
    assert r1["probe_site"] == "10-30+"
    assert (r2["exclusion"], r2["pair_evalue"]) == ("diverged", "0.02")


def test_naive_concatenation_would_have_failed_that_test(tmp_path):
    """Pins that the test above is capable of failing, by running the bug.

    Under the newer header, an older row read positionally puts 1.5 where
    `exclusion` belongs.
    """
    old = write_screen(
        tmp_path / "old.tsv",
        REAL_OLD,
        [
            {
                "assay_id": "A",
                "record_id": "R1",
                "call": "reduced",
                "probe_site": "p",
                "fwd_penalty": "1.5",
                "rev_penalty": "0.5",
                "reason": "",
            }
        ],
    )
    row = old.read_bytes().decode().split("\r\n")[1].split("\t")
    shifted = dict(zip(REAL_NEW, row, strict=False))
    assert shifted["exclusion"] == "1.5" and shifted["pair_evalue"] == "0.5"  # the corruption


def test_the_same_screens_collected_at_different_times_give_the_same_bytes(tmp_path, monkeypatch):
    """`gzip.open` stamps the clock into the header, so a regenerated calls table could never
    be compared with the old one by hash. With the timestamp pinned, "unchanged" is a fact
    cmp can check. The clock is made to differ between the two calls, so a writer that reads
    it fails this; sleeping would only make the test slow."""
    import gzip as gzip_module

    a = write_screen(
        tmp_path / "a.tsv", OLD, [{"assay_id": "A", "record_id": "R1", "call": "detect", "penalty": "0"}]
    )
    first, second = tmp_path / "one.tsv.gz", tmp_path / "two.tsv.gz"
    clock = iter([1_000_000_000.0, 2_000_000_000.0, 3_000_000_000.0, 4_000_000_000.0])
    monkeypatch.setattr(gzip_module.time, "time", lambda: next(clock))
    concatenate_screens([a], first)
    concatenate_screens([a], second)
    assert first.read_bytes() == second.read_bytes()
    assert gzip.open(first, "rt", newline="").read().startswith("\t".join(OLD) + LINE_END)
    assert b"one.tsv" not in first.read_bytes()  # and no file name stored in the header either


# The registry guard. results/2026-10-20/calls.tsv.gz held three assay ids the
# registry had renamed, from one cached screen reused without its --only list
# being re-checked, and "208 assays screened" counted them twice.
IDS = ["assay_id", "record_id", "call"]


def test_screens_holding_only_current_ids_collect_as_before(tmp_path):
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    out = tmp_path / "calls.tsv.gz"
    concatenate_screens([a], out, known_ids={"A", "B"})
    assert [r["assay_id"] for r in read_table(out)] == ["A"]


def test_a_stale_id_is_refused_naming_the_file_the_id_and_the_row_count(tmp_path):
    good = write_screen(tmp_path / "good.tsv", IDS, [{"assay_id": "NEW", "record_id": "R1", "call": "pass"}])
    stale = write_screen(
        tmp_path / "stale.tsv",
        IDS,
        [
            {"assay_id": "OLD", "record_id": "R2", "call": "pass"},
            {"assay_id": "OLD", "record_id": "R3", "call": "fail"},
            {"assay_id": "NEW", "record_id": "R4", "call": "pass"},
        ],
    )
    out = tmp_path / "calls.tsv.gz"
    with pytest.raises(ValueError) as err:
        concatenate_screens([good, stale], out, known_ids={"NEW"})
    msg = str(err.value)
    assert str(stale) in msg and "OLD (2 rows)" in msg
    assert str(good) not in msg
    assert "Delete them and rerun" in msg


def test_a_refused_collect_writes_no_calls_table(tmp_path):
    """A half-written table left behind is what a later stage would pick up."""
    stale = write_screen(
        tmp_path / "stale.tsv", IDS, [{"assay_id": "OLD", "record_id": "R1", "call": "pass"}]
    )
    out = tmp_path / "calls.tsv.gz"
    with pytest.raises(ValueError):
        concatenate_screens([stale], out, known_ids={"NEW"})
    assert not out.exists()


def test_a_quoted_line_break_is_not_misread_as_a_row(tmp_path):
    """Per-line splitting would read the continuation 'tail' as an assay id."""
    a = write_screen(
        tmp_path / "a.tsv",
        IDS + ["reason"],
        [{"assay_id": "A", "record_id": "R1", "call": "pass", "reason": "head\ntail"}],
    )
    concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A"})


def test_a_screen_without_an_assay_id_column_is_refused(tmp_path):
    a = write_screen(tmp_path / "a.tsv", ["record_id", "call"], [{"record_id": "R1", "call": "pass"}])
    with pytest.raises(ValueError, match="no assay_id column"):
        concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A"})


def test_zero_byte_and_header_only_screens_pass_the_check(tmp_path):
    empty = tmp_path / "empty.tsv"
    empty.write_bytes(b"")
    header = write_screen(tmp_path / "header.tsv", IDS, [])
    concatenate_screens([empty, header], tmp_path / "calls.tsv.gz", known_ids=set())


def test_without_known_ids_nothing_is_checked(tmp_path):
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "ANY", "record_id": "R1", "call": "pass"}])
    concatenate_screens([a], tmp_path / "calls.tsv.gz")


# The provenance sidecar (R2). A calls table could not say what produced it:
# establishing that results/2026-10-18/ ran under a since-reverted scoring
# override took noticing a commit that landed three minutes after the run
# finished. These tests pin what the sidecar does record, and what it refuses
# to claim.
def _prov(tmp_path: Path) -> dict:
    return json.loads((tmp_path / "calls.provenance.json").read_text())


def test_no_sidecar_is_written_unless_provenance_is_asked_for(tmp_path):
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A"})
    assert not (tmp_path / "calls.provenance.json").exists()


def test_the_sidecar_lands_beside_the_calls_table_and_names_it(tmp_path):
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    concatenate_screens(
        [a], tmp_path / "calls.tsv.gz", known_ids={"A"}, provenance={"run_date": "2026-10-21"}
    )
    doc = _prov(tmp_path)
    assert doc["calls_table"] == "calls.tsv.gz"
    assert doc["run_date"] == "2026-10-21"


def test_every_screen_is_inventoried_with_its_rows_and_assays(tmp_path):
    a = write_screen(
        tmp_path / "a.tsv",
        IDS,
        [
            {"assay_id": "A", "record_id": "R1", "call": "pass"},
            {"assay_id": "B", "record_id": "R2", "call": "fail"},
        ],
    )
    b = write_screen(tmp_path / "b.tsv", IDS, [{"assay_id": "A", "record_id": "R3", "call": "pass"}])
    concatenate_screens([a, b], tmp_path / "calls.tsv.gz", known_ids={"A", "B"}, provenance={})
    doc = _prov(tmp_path)
    assert doc["screens"] == 2
    assert doc["rows"] == 3  # and that is the row count of the table itself
    assert [s["rows"] for s in doc["screen_inventory"]] == [2, 1]
    assert [s["assays"] for s in doc["screen_inventory"]] == [2, 1]
    assert [Path(s["path"]).name for s in doc["screen_inventory"]] == ["a.tsv", "b.tsv"]


def test_the_row_total_matches_the_table_it_describes(tmp_path):
    rows = [{"assay_id": "A", "record_id": f"R{i}", "call": "pass"} for i in range(17)]
    a = write_screen(tmp_path / "a.tsv", IDS, rows)
    out = tmp_path / "calls.tsv.gz"
    concatenate_screens([a], out, known_ids={"A"}, provenance={})
    assert _prov(tmp_path)["rows"] == len(read_table(out)) == 17


def test_a_quoted_line_break_is_counted_as_one_row_not_two(tmp_path):
    """Why the count is parsed rather than taken from newlines."""
    a = write_screen(
        tmp_path / "a.tsv",
        [*IDS, "reason"],
        [{"assay_id": "A", "record_id": "R1", "call": "fail", "reason": "head\ntail"}],
    )
    concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A"}, provenance={})
    assert _prov(tmp_path)["rows"] == 1


def test_the_span_of_screening_times_is_recorded(tmp_path):
    """The forensic number: a table whose screens were written weeks apart cannot
    have one set of settings, and this is what says so."""
    old = write_screen(tmp_path / "old.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    new = write_screen(tmp_path / "new.tsv", IDS, [{"assay_id": "A", "record_id": "R2", "call": "pass"}])
    then = datetime(2026, 10, 4, 18, 30, tzinfo=UTC).timestamp()
    now = datetime(2026, 10, 20, 21, 53, tzinfo=UTC).timestamp()
    os.utime(old, (then, then))
    os.utime(new, (now, now))
    concatenate_screens([old, new], tmp_path / "calls.tsv.gz", known_ids={"A"}, provenance={})
    doc = _prov(tmp_path)
    assert doc["screened_first"] < doc["screened_last"]
    assert doc["screened_first"].startswith("2026-10-0")
    inventory = {Path(s["path"]).name: s["screened_at"] for s in doc["screen_inventory"]}
    assert inventory["old.tsv"] == doc["screened_first"]
    assert inventory["new.tsv"] == doc["screened_last"]


def test_the_timestamps_carry_an_offset_so_they_cannot_be_read_in_the_wrong_zone(tmp_path):
    """In UTC the 2026-10-20 run's screens read 2026-10-21T01:53, which invites
    exactly the wrong comparison when the question is which run wrote a screen."""
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A"}, provenance={})
    doc = _prov(tmp_path)
    for stamp in (doc["collected_at"], doc["screened_first"], doc["screen_inventory"][0]["screened_at"]):
        assert datetime.fromisoformat(stamp).utcoffset() is not None


def test_the_expected_signature_is_recorded_per_group(tmp_path):
    screens = tmp_path / "results" / "screened" / "10292" / "qb41"
    screens.mkdir(parents=True)
    a = write_screen(screens / "2026-10-03.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    concatenate_screens(
        [a],
        tmp_path / "calls.tsv.gz",
        known_ids={"A"},
        expected_signatures={"10292/qb41": "abc123"},
        provenance={},
    )
    entry = _prov(tmp_path)["screen_inventory"][0]
    assert entry["group"] == "10292/qb41"
    assert entry["expected_signature"] == "abc123"


def test_a_group_with_no_signature_given_records_an_empty_one_not_a_wrong_one(tmp_path):
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    concatenate_screens(
        [a], tmp_path / "calls.tsv.gz", known_ids={"A"}, expected_signatures={}, provenance={}
    )
    assert _prov(tmp_path)["screen_inventory"][0]["expected_signature"] == ""


def test_the_sidecar_says_the_signature_is_what_is_expected_now_not_what_ran(tmp_path):
    """The claim it must not make. A cached screen carries no record of its own
    settings - that gap is the 2026-10-18 bug, and this file makes it visible
    rather than closing it."""
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A"}, provenance={})
    note = _prov(tmp_path)["note"]
    assert "NOW" in note and "screened_at is the evidence" in note


def test_extra_fields_are_passed_through(tmp_path):
    """The Snakefile's hashes and git commit, which collect.py cannot compute."""
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    concatenate_screens(
        [a],
        tmp_path / "calls.tsv.gz",
        known_ids={"A"},
        provenance={"extra": {"screen_code_and_config_sha1": "deadbeef", "git_commit": "abc1234 (dirty)"}},
    )
    doc = _prov(tmp_path)
    assert doc["screen_code_and_config_sha1"] == "deadbeef"
    assert doc["git_commit"] == "abc1234 (dirty)"


def test_a_refused_collect_writes_no_sidecar_either(tmp_path):
    stale = write_screen(
        tmp_path / "stale.tsv", IDS, [{"assay_id": "OLD", "record_id": "R1", "call": "pass"}]
    )
    with pytest.raises(ValueError):
        concatenate_screens([stale], tmp_path / "calls.tsv.gz", known_ids={"NEW"}, provenance={})
    assert not (tmp_path / "calls.provenance.json").exists()


def test_the_screens_are_parsed_once_for_the_guard_and_the_sidecar(tmp_path, monkeypatch):
    """Both need the same parse; 311 screens take about 5 seconds to read."""
    import assaywatch.collect as collect

    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    b = write_screen(tmp_path / "b.tsv", IDS, [{"assay_id": "A", "record_id": "R2", "call": "pass"}])
    calls = []
    real = collect.screen_stats
    monkeypatch.setattr(collect, "screen_stats", lambda p, k=None: (calls.append(p), real(p, k))[1])
    collect.concatenate_screens([a, b], tmp_path / "calls.tsv.gz", known_ids={"A"}, provenance={})
    assert calls == [a, b]


# --- A screen that says what it was produced under ---------------------------
# Added 2026-10-21. `screen_signature` was already a `screen_archive` param, so
# Snakemake reran a job when it changed — but only where it holds a metadata
# record for the output to compare against. The full run that day found 20
# screens of 316 with no such record (written by a different Snakemake install):
# the params check had nothing to compare, the changed code hash did not
# invalidate them, and they were silently reused. The signature is now written
# beside the screen, where `collect` can check it whatever Snakemake remembers.


def _sign(path: Path, signature: str) -> Path:
    """What `screen.py --signature` leaves beside a screen."""
    sig = signature_path(path)
    sig.write_text(signature + "\n")
    return sig


def test_a_screen_can_say_what_it_was_produced_under():
    assert signature_path(Path("results/screened/10292/all/2026-10-03.tsv")).name == ("2026-10-03.tsv.sig")
    # Must not look like a screen to anything globbing *.tsv (assaywatch/windows.py does).
    assert not signature_path(Path("a/2026-10-03.tsv")).match("*.tsv")


def test_stored_signature_reads_it_back_and_says_none_when_absent(tmp_path):
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    assert stored_signature(a) is None
    _sign(a, "sig-abc")
    assert stored_signature(a) == "sig-abc"
    # An empty file says nothing, which is None rather than "".
    signature_path(a).write_text("\n")
    assert stored_signature(a) is None


def test_a_screen_whose_signature_disagrees_is_refused(tmp_path):
    screens = tmp_path / "results" / "screened" / "10292" / "qb41"
    screens.mkdir(parents=True)
    a = write_screen(screens / "2026-10-03.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    _sign(a, "the-old-settings")
    with pytest.raises(ValueError, match="no longer uses"):
        concatenate_screens(
            [a],
            tmp_path / "calls.tsv.gz",
            known_ids={"A"},
            expected_signatures={"10292/qb41": "the-new-settings"},
        )
    # Refused, not quietly dropped: no calls table may exist.
    assert not (tmp_path / "calls.tsv.gz").exists()


def test_a_matching_signature_passes_and_is_recorded_as_verified(tmp_path):
    screens = tmp_path / "results" / "screened" / "10292" / "qb41"
    screens.mkdir(parents=True)
    a = write_screen(screens / "2026-10-03.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    _sign(a, "sig-xyz")
    concatenate_screens(
        [a],
        tmp_path / "calls.tsv.gz",
        known_ids={"A"},
        expected_signatures={"10292/qb41": "sig-xyz"},
        provenance={},
    )
    entry = _prov(tmp_path)["screen_inventory"][0]
    assert entry["stored_signature"] == "sig-xyz"
    assert entry["signature_verified"] is True


def test_a_screen_storing_no_signature_is_unverifiable_not_wrong(tmp_path, capsys):
    """null, not False. Every screen written before 2026-10-21 stores nothing, and
    "does not say" is a different fact from "says something else" - only the
    second is a defect, and refusing the first would have failed this run on 20
    screens that turned out to hold correct calls."""
    screens = tmp_path / "results" / "screened" / "10292" / "qb41"
    screens.mkdir(parents=True)
    a = write_screen(screens / "2026-10-03.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    concatenate_screens(
        [a],
        tmp_path / "calls.tsv.gz",
        known_ids={"A"},
        expected_signatures={"10292/qb41": "sig-xyz"},
        provenance={},
    )
    entry = _prov(tmp_path)["screen_inventory"][0]
    assert entry["stored_signature"] is None
    assert entry["signature_verified"] is None
    # And it has to be said out loud, or an unverifiable screen is invisible again.
    assert "store no signature" in capsys.readouterr().err


def test_no_expected_signatures_skips_the_check_entirely(tmp_path):
    """For callers that are not collecting a run; the pipeline always passes them."""
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    _sign(a, "anything-at-all")
    concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A"})
    assert (tmp_path / "calls.tsv.gz").exists()


# --- The mirror of the orphan guard: a screened assay with no rows ------------


def test_an_assay_that_produced_no_rows_is_named_but_does_not_fail_the_run(tmp_path, capsys):
    """`Helicobacter_Pan_Helicobacter_16S_short_Fox_1998` on 2026-10-21: no
    `target.query`, so its group is all 843,447 Helicobacter records, over
    retrieval's cap. Retrieval skipped it and said so; nothing downstream did."""
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    cols = concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A", "B", "C"})
    assert cols  # the run completed
    err = capsys.readouterr().err
    assert "2 screened assay(s) produced no rows" in err
    assert "B, C" in err


def test_nothing_is_said_when_every_assay_produced_rows(tmp_path, capsys):
    a = write_screen(
        tmp_path / "a.tsv",
        IDS,
        [
            {"assay_id": "A", "record_id": "R1", "call": "pass"},
            {"assay_id": "B", "record_id": "R2", "call": "fail"},
        ],
    )
    concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A", "B"})
    assert "produced no rows" not in capsys.readouterr().err


def test_assays_without_calls_is_the_complement_of_what_was_seen(tmp_path):
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    b = write_screen(tmp_path / "b.tsv", IDS, [{"assay_id": "B", "record_id": "R2", "call": "pass"}])
    stats = {a: screen_stats(a, {"A", "B", "C"}), b: screen_stats(b, {"A", "B", "C"})}
    assert assays_without_calls(stats, {"A", "B", "C"}) == ["C"]
    assert assays_without_calls(stats, {"A", "B"}) == []
    # It spans every screen, not just one: A and B each appear in only one.
    assert assays_without_calls({a: stats[a]}, {"A", "B"}) == ["B"]


# --- collected_under: the environment that assembled the table (R1b) ---------
# R2 recorded the code (git_commit, the code hash) but not the interpreter and
# libraries; a numpy or primer3 version can change a number. `collected_under`
# closes that for the common same-day run, honestly labelled for a mixed table.


def test_runtime_names_the_interpreter_and_the_packages_that_move_numbers():
    rt = _runtime()
    assert rt["python"] and rt["platform"]
    pkgs = rt["packages"]
    # numpy and pydantic are core, always present.
    assert pkgs["numpy"] and pkgs["pydantic"]
    # Every package that can change a call or number is named, present or null.
    for p in ("assaywatch", "scipy", "statsmodels", "primer3-py", "snakemake"):
        assert p in pkgs


def test_runtime_records_null_for_an_absent_package_rather_than_raising(monkeypatch):
    """The sidecar must never fail a run; an absent optional package is null."""
    import assaywatch.collect as c

    monkeypatch.setattr(c, "_RUNTIME_PACKAGES", ("numpy", "a-package-that-is-not-installed-xyz"))
    rt = c._runtime()
    assert rt["packages"]["numpy"]
    assert rt["packages"]["a-package-that-is-not-installed-xyz"] is None


def test_the_sidecar_carries_collected_under(tmp_path):
    a = write_screen(tmp_path / "a.tsv", IDS, [{"assay_id": "A", "record_id": "R1", "call": "pass"}])
    concatenate_screens([a], tmp_path / "calls.tsv.gz", known_ids={"A"}, provenance={})
    under = _prov(tmp_path)["collected_under"]
    assert under["python"] and "numpy" in under["packages"]
