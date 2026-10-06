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
from pathlib import Path

import pytest

from assaywatch.collect import (
    LINE_END,
    concatenate_screens,
    read_header,
    stem_order,
    unified_columns,
)


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
