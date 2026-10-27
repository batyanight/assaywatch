"""The archive-scale anchor test (calls.apply_anchor_fdr), 2026-10-24.

`score.classify_exclusion` judges a lone primer site by a per-record E-value, and an
archive of thousands of records clears that bar by chance in proportion to its size
(docs/2026-10-23-wave2-diverged-and-patent.md; docs/2026-10-24-archive-anchor.md).
These pin the report-time correction: off is a no-op, Bd-shaped chance anchors are
relabelled, SIV-shaped real ones are not, ties share a fate, and rows that never
recorded an E are left alone.
"""

from __future__ import annotations

import csv
import gzip

import pytest

from assaywatch.calls import CHANCE_ANCHOR, apply_anchor_fdr, read_calls

ON = {"drift": {"anchor_fdr": 0.05}}


def _row(aid, rid, call="no_amplicon", exclusion="", e=None):
    r = {"assay_id": aid, "record_id": rid, "call": call, "exclusion": exclusion}
    if e is not None:
        r["anchor_evalue"] = e
    return r


def _bd_like():
    """8,900 records with no credible site, 392 truncated real deposits, 55 chance anchors."""
    rows = [_row("Bd", f"mrna{i}", exclusion="no_site", e=0.5) for i in range(8900)]
    rows += [_row("Bd", f"its{i}", exclusion="truncated", e=1e-10) for i in range(392)]
    rows += [_row("Bd", f"chance{i}", exclusion="diverged", e=5e-3) for i in range(55)]
    return rows


def test_off_by_default_changes_nothing_and_reports_nothing():
    rows = _bd_like()
    before = [dict(r) for r in rows]
    assert apply_anchor_fdr(rows, {"drift": {}}) == {}
    assert apply_anchor_fdr(rows, {}) == {}
    assert rows == before


def test_bd_shaped_chance_anchors_are_relabelled_and_the_real_deposits_are_not():
    """55 anchors at E 5e-3 ranked after 392 at 1e-10 among 9,347 tests: 447/9347 x 0.05 is
    2.4e-3, below 5e-3, so BH rejects the 392 and not the 55."""
    rows = _bd_like()
    moved = apply_anchor_fdr(rows, ON)
    assert moved == {"Bd": 55}
    labels = {r["record_id"]: r["exclusion"] for r in rows}
    assert all(labels[f"chance{i}"] == CHANCE_ANCHOR for i in range(55))
    assert all(labels[f"its{i}"] == "truncated" for i in range(392))
    assert all(labels[f"mrna{i}"] == "no_site" for i in range(8900))


def test_siv_shaped_real_anchors_all_survive():
    """7,000 two-mismatch anchors at E 3e-5 among 8,000 tests: the step-up threshold at
    rank 7,000 is 0.044, so every one passes. `E x N` would have given 0.21 and failed them,
    which is why the test is BH and not a product."""
    rows = [_row("SIV", f"real{i}", exclusion="diverged", e=3e-5) for i in range(7000)]
    rows += [_row("SIV", f"none{i}", exclusion="no_site", e=0.3) for i in range(1000)]
    assert apply_anchor_fdr(rows, ON) == {}
    assert all(r["exclusion"] != CHANCE_ANCHOR for r in rows)


def test_the_product_rule_would_have_got_siv_wrong():
    """The arithmetic the docstring relies on, pinned so the reasoning cannot drift."""
    assert 3e-5 * 7000 > 0.05  # E x N fails them
    assert 3e-5 <= 7000 / 8000 * 0.05  # BH passes them


def test_only_lone_anchor_labels_can_move():
    rows = [
        _row("A", "r1", call="detect"),
        _row("A", "r2", call="fail"),
        _row("A", "r3", exclusion="no_site", e=0.5),
        _row("A", "r4", exclusion="chance_only", e=0.5),
        _row("A", "r5", exclusion="windowed"),
        _row("A", "r6", exclusion="diverged", e=0.009),
    ]
    rows += [_row("A", f"pad{i}", exclusion="no_site", e=1.0) for i in range(200)]
    before = {r["record_id"]: r["exclusion"] for r in rows}
    moved = apply_anchor_fdr(rows, ON)
    assert moved == {"A": 1}
    after = {r["record_id"]: r["exclusion"] for r in rows}
    assert after["r6"] == CHANCE_ANCHOR
    assert all(after[k] == before[k] for k in before if k != "r6")


def test_a_row_that_recorded_no_evalue_is_never_relabelled():
    """An older screen's `diverged` carries no E. Unknown is not chance."""
    rows = [_row("A", "old", exclusion="diverged")]
    rows += [_row("A", f"pad{i}", exclusion="no_site", e=1.0) for i in range(500)]
    assert apply_anchor_fdr(rows, ON) == {}
    assert rows[0]["exclusion"] == "diverged"


def test_tied_pvalues_share_one_fate():
    """Two anchors at the same E are rejected together or kept together, whatever
    their position in the sort."""
    rows = [_row("A", f"t{i}", exclusion="diverged", e=1e-4) for i in range(2)]
    rows += [_row("A", f"pad{i}", exclusion="no_site", e=1.0) for i in range(2000)]
    # rank 1: 1/2002 x 0.05 = 2.5e-5 < 1e-4 (not rejected alone); rank 2: 5.0e-5 < 1e-4.
    # So neither passes and both are relabelled; the point is that the answer is the
    # same for both rows.
    apply_anchor_fdr(rows, ON)
    fates = {rows[0]["exclusion"], rows[1]["exclusion"]}
    assert len(fates) == 1


def test_families_are_per_assay():
    """One assay's thousands of real anchors must not rescue another assay's chance ones."""
    rows = [_row("SIV", f"real{i}", exclusion="diverged", e=3e-5) for i in range(7000)]
    rows += _bd_like()
    moved = apply_anchor_fdr(rows, ON)
    assert moved == {"Bd": 55}


def test_a_bad_q_is_refused():
    import pytest

    for q in (0, 1, 1.5, -0.1):
        with pytest.raises(ValueError):
            apply_anchor_fdr(_bd_like(), {"drift": {"anchor_fdr": q}})


def test_read_calls_carries_the_anchor_evalue(tmp_path):
    """The column is read as a float where present and absent where blank, so an
    older table (no column) and a mixed table (blank-filled by collect) both work."""
    p = tmp_path / "calls.tsv.gz"
    header = ["assay_id", "record_id", "call", "exclusion", "anchor_evalue", "reason"]
    with gzip.open(p, "wt", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(header)
        w.writerow(["A", "r1", "no_amplicon", "diverged", "0.0051", "x"])
        w.writerow(["A", "r2", "no_amplicon", "diverged", "", "x"])
        w.writerow(["A", "r3", "detect", "", "", ""])
    rows = {r["record_id"]: r for r in read_calls(p)}
    assert rows["r1"]["anchor_evalue"] == 0.0051
    assert "anchor_evalue" not in rows["r2"]
    assert "anchor_evalue" not in rows["r3"]
    old = tmp_path / "old.tsv"
    old.write_text("assay_id\trecord_id\tcall\texclusion\nA\tr1\tno_amplicon\tdiverged\n")
    assert "anchor_evalue" not in read_calls(old)[0]


# --------------------------------------------------------------------------
# The family, 2026-10-27. `lone_anchor` was recommended and then refuted by
# test_bd_shaped_chance_anchors_... above: it drops the weakly-anchored rows,
# which loosens the bar until the chance anchors this test exists to catch pass
# as real. These pin all three behaviours so the refutation cannot be undone by
# a later tidy-up.
# --------------------------------------------------------------------------


def _fam(name):
    return {"drift": {"anchor_fdr": 0.05, "anchor_fdr_family": name}}


def test_lone_anchor_family_loses_the_bd_catch_which_is_why_it_is_not_the_default():
    """Documenting the wrong answer, so nobody re-adopts it.

    Dropping the 8,900 weakly-anchored rows takes m from 9,347 to 447, the bar at
    the last rank becomes 0.05, and 5e-3 clears it -- so all 55 chance anchors
    are called real and nothing is relabelled.
    """
    rows = _bd_like()
    assert apply_anchor_fdr(rows, _fam("lone_anchor")) == {}
    assert all(r["exclusion"] != CHANCE_ANCHOR for r in rows)


def test_tested_family_keeps_the_bd_catch():
    """Every Bd fixture row recorded an E-value, so all of them were tests."""
    rows = _bd_like()
    assert apply_anchor_fdr(rows, _fam("tested")) == {"Bd": 55}


def test_a_row_with_no_anchor_is_not_a_member_of_the_tested_family():
    """The whole point of the change: no anchor means no hypothesis was tested.

    Such a row enters as p = 1 under `all_no_amplicon`, can never be rejected or
    relabelled, and only enlarges m -- tightening the bar for the rows that can
    move. Here 2,000 of them drag the bar down far enough to relabel the one
    genuine anchor; under `tested` they are not counted and it survives.
    """
    real = [_row("A", "anchor", exclusion="diverged", e=1e-3)]
    padding = [_row("A", f"nosite{i}", exclusion="no_site") for i in range(2000)]

    rows = [dict(r) for r in real + padding]
    assert apply_anchor_fdr(rows, _fam("all_no_amplicon")) == {"A": 1}

    rows = [dict(r) for r in real + padding]
    assert apply_anchor_fdr(rows, _fam("tested")) == {}


def test_a_weakly_anchored_no_site_row_IS_a_member_of_the_tested_family():
    """`no_site` means no CREDIBLE site, not no site. A weak anchor is a test
    that failed to reject, and a family must count it."""
    rows = [_row("A", "anchor", exclusion="diverged", e=1e-3)]
    rows += [_row("A", f"weak{i}", exclusion="no_site", e=0.4) for i in range(2000)]
    # Counted, so the bar is tight and the lone real anchor is relabelled --
    # the same answer `all_no_amplicon` gives, reached for the right reason.
    assert apply_anchor_fdr(rows, _fam("tested")) == {"A": 1}


def test_an_unknown_family_is_refused_rather_than_silently_defaulted():
    with pytest.raises(ValueError, match="anchor_fdr_family"):
        apply_anchor_fdr(_bd_like(), _fam("whatever"))
