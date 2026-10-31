"""Nested protocols: each round scored alone, then round 2 warned about round 1.

The numbers in the docstrings are from the 2026-10-07 records; if a refactor
moves them the refactor is what changed, not the biology.
"""

from types import SimpleNamespace

import pytest

from assaywatch.nested import NestedFamily, assess, families, family_id, unpaired


def _assay(aid, nested_round=None, amplicon_bp=None, fwd="AAAA", rev="TTTT", nested_family=None):
    return SimpleNamespace(
        id=aid,
        source=SimpleNamespace(nested_round=nested_round, nested_family=nested_family),
        amplicon_bp=amplicon_bp,
        oligos=SimpleNamespace(
            forward=SimpleNamespace(matching_seq=fwd),
            reverse=SimpleNamespace(matching_seq=rev),
            probe=None,
        ),
    )


def _row(aid, rid, call, start=None, end=None, exclusion=""):
    return {
        "assay_id": aid,
        "record_id": rid,
        "call": call,
        "exclusion": exclusion,
        "amplicon_start": start,
        "amplicon_end": end,
    }


def test_family_id_strips_any_round_suffix():
    assert family_id("X_round2") == "X"
    assert family_id("X_round2B") == "X"
    assert family_id("X") == "X"
    assert family_id("X_roundabout") == "X_roundabout", "only a numbered suffix is a round"


def test_only_bases_with_more_than_one_round_are_families():
    f = families(["A", "A_round2", "B", "C_round1", "C_round2"])
    assert f == {"A": ["A", "A_round2"], "C": ["C_round1", "C_round2"]}


def test_an_entry_declaring_a_round_with_no_sibling_is_listed_not_guessed():
    """The Chlamydia nest runs one genus round 1 into three species round 2 entries."""
    assays = {
        "CHLAMYDIA_genus_round1": _assay("CHLAMYDIA_genus_round1", "round1"),
        "CHLAMYDIA_psittaci_round2": _assay("CHLAMYDIA_psittaci_round2", "round2"),
        "Z": _assay("Z"),
    }
    assert unpaired(assays) == ["CHLAMYDIA_genus_round1", "CHLAMYDIA_psittaci_round2"]


def test_round_order_comes_from_the_registry_not_the_id():
    """The Landolfi orthoreovirus base id holds round 2, with a `_round1` sibling.

    Taking the base as the outer round inverted that pair, and the containment
    check caught it: 0 of 987 records, where the truth is 987 of 987.
    """
    assays = {
        "ORTHO": _assay("ORTHO", "round2", amplicon_bp=163),
        "ORTHO_round1": _assay("ORTHO_round1", "round1", amplicon_bp=274),
    }
    rows = [_row("ORTHO", "r1", "detect", 100, 261), _row("ORTHO_round1", "r1", "detect", 90, 364)]
    f = assess(assays, rows)["ORTHO"]
    assert (f.outer, f.inner) == ("ORTHO_round1", "ORTHO")
    assert f.containment[("ORTHO_round1", "ORTHO")] == (1, 1)
    assert f.nests is True


def test_round_order_falls_back_to_the_declared_product_size():
    """An outer round is the longer product; that is what nesting means.

    Neither entry declares a round number, which is the real shape of the five
    outer rounds whose `nested_round` mirrors a spreadsheet that recorded none.
    They are in the family because they declare `nested_family`.
    """
    assays = {
        "P": _assay("P", amplicon_bp=200, nested_family="P"),
        "P_round2": _assay("P_round2", amplicon_bp=900, nested_family="P"),
    }
    rows = [_row("P", "r", "detect", 0, 0), _row("P_round2", "r", "detect", 0, 0)]
    assert assess(assays, rows)["P"].outer == "P_round2"


def test_the_nest_detects_only_what_both_rounds_reach():
    """Round 2's own share is a direct PCR; the nest needs round 1 to deliver template."""
    assays = {"L": _assay("L", "round1"), "L_round2": _assay("L_round2", "round2")}
    rows = []
    for i in range(10):
        outer = "detect" if i < 3 else "fail"  # round 1 reaches 3 of 10
        rows += [_row("L", f"r{i}", outer, 0, 100), _row("L_round2", f"r{i}", "detect", 10, 90)]
    f = assess(assays, rows)["L"]
    assert f.records == 10
    assert f.outer_share == 0.3
    assert f.inner_share == 1.0, "round 2 binds every record"
    assert f.nested_share == 0.3, "but the nest only delivers where round 1 did"
    assert f.gap == pytest.approx(0.7)


def test_a_round_one_failure_that_is_the_deposits_fault_is_not_counted():
    """`truncated` says something about GenBank, not about the assay - as in the denominator."""
    assays = {"T": _assay("T", "round1"), "T_round2": _assay("T_round2", "round2")}
    rows = [
        _row("T", "keep", "fail", 0, 100),
        _row("T_round2", "keep", "detect", 10, 90),
        _row("T", "drop", "no_amplicon", exclusion="truncated"),
        _row("T_round2", "drop", "detect", 10, 90),
    ]
    f = assess(assays, rows)["T"]
    assert f.records == 1, "the truncated record is not evidence about round 1"


def test_a_diverged_site_does_count_as_a_round_one_escape():
    assays = {"D": _assay("D", "round1"), "D_round2": _assay("D_round2", "round2")}
    rows = [
        _row("D", "r", "no_amplicon", exclusion="diverged"),
        _row("D_round2", "r", "detect", 10, 90),
    ]
    f = assess(assays, rows)["D"]
    assert f.records == 1 and f.outer_detected == 0 and f.nested_share == 0.0


def test_no_warning_when_the_amplicons_do_not_nest():
    """The coronavirus pair's amplicons are 2.7 kb apart, so conditioning would invent a number."""
    assays = {"C": _assay("C", "round1"), "C_round2": _assay("C_round2", "round2")}
    rows = []
    for i in range(30):
        rows += [
            _row("C", f"r{i}", "detect" if i < 10 else "fail", 14142, 14582),
            _row("C_round2", f"r{i}", "detect", 17306, 17635),
        ]
    f = assess(assays, rows)["C"]
    assert f.nests is False
    assert f.gap > 0.5, "the gap is large, and still must not be reported as a warning"
    assert f.warns(0.90) is False
    assert "do not nest" in f.note(0.90)


def test_the_warning_fires_on_a_verdict_flip():
    """Round 2 alone clears the threshold and the nest does not: the lyssavirus shape."""
    f = NestedFamily(
        "F",
        ["a", "b"],
        outer="a",
        inner="b",
        records=100,
        outer_detected=33,
        inner_detected=99,
        both_detected=33,
        containment={("a", "b"): (100, 100)},
    )
    assert f.warns(0.90)
    note = f.note(0.90)
    assert "DIRECT PCR" in note and "crosses the 90% threshold" in note


def test_a_shared_oligo_is_named_because_the_rounds_are_not_independent():
    """A semi-nested pair sharing a primer fails both rounds at once when it escapes."""
    assays = {
        "S": _assay("S", "round1", fwd="GGGG", rev="CCCC"),
        "S_round2": _assay("S_round2", "round2", fwd="GGGG", rev="TTTT"),
    }
    rows = []
    for i in range(30):
        rows += [
            _row("S", f"r{i}", "detect" if i < 10 else "fail", 0, 300),
            _row("S_round2", f"r{i}", "detect", 50, 200),
        ]
    f = assess(assays, rows)["S"]
    assert f.shared_oligos == ("forward",)
    assert "share forward" in f.note(0.90)


def test_the_module_cannot_fold_into_a_verdict():
    """Reported beside a status, never into one - as degeneracy and thermo are.

    Structural rather than a text search: `assess` is not given the statuses, and
    a family carries no status field, so there is no path by which this could
    change a call. A later refactor that wants to fold it in has to change the
    signature, which is the point at which somebody should object.
    """
    import dataclasses
    import inspect

    from assaywatch import nested

    assert "statuses" not in inspect.signature(nested.assess).parameters
    fields = {f.name for f in dataclasses.fields(nested.NestedFamily)}
    assert not fields & {"status", "statuses", "call"}


def test_an_entry_sharing_a_base_but_declaring_no_nest_stays_out_of_the_family():
    """The fault that produced a false finding, pinned.

    A 440 bp coronavirus consensus entry shares an id base with Lan 2010's
    nested pair. Grouping by base alone pulled it in, displaced Lan's real
    round 1, and made the pair read as DISJOINT - reported on 2026-10-14 as
    "two assays, not two rounds". Pair Lan's own rounds and they nest on 6,667
    of the 6,671 records both rounds can be judged on.
    """
    assays = {
        "C": _assay("C", amplicon_bp=440),  # unrelated, declares no nest
        "C_Lan_round1": _assay("C_Lan_round1", "round1", 532, nested_family="C_Lan"),
        "C_round2": _assay("C_round2", "round2", 328, nested_family="C_Lan"),
    }
    fams = families(assays)
    assert fams == {"C_Lan": ["C_Lan_round1", "C_round2"]}, "the consensus entry is not a round"


def test_two_nests_on_one_base_are_kept_apart():
    """`_round2_2` escapes the `_roundN` suffix, so only a declared family joins it.

    Two papers' CMV gB nests sit on one id base. By base alone, Deckers' round 1
    paired with Prepens' round 2 - different assays, 0 of 659 records contained.
    Declared apart, both nest perfectly (726/726 and 578/578).
    """
    assays = {
        "gB": _assay("gB", amplicon_bp=800, nested_family="gB_Deckers"),
        "gB_round2_2": _assay("gB_round2_2", "round2", 550, nested_family="gB_Deckers"),
        "gB_V_round1": _assay("gB_V_round1", "round1", 320, nested_family="gB_Prepens"),
        "gB_round2": _assay("gB_round2", "round2", 230, nested_family="gB_Prepens"),
    }
    assert families(assays) == {
        "gB_Deckers": ["gB", "gB_round2_2"],
        "gB_Prepens": ["gB_V_round1", "gB_round2"],
    }


def test_a_declared_family_can_span_unlike_ids():
    """The Chlamydia nest: one genus round 1 feeding three species round 2 entries.

    Four ids on three taxids. No id base can express it, which is why the key
    is declared rather than inferred.
    """
    ids = ["CH_genus_round1", "CH_pneumoniae_round2", "CH_psittaci_round2", "CH_trachomatis_round2"]
    assays = {i: _assay(i, "round1" if "genus" in i else "round2", nested_family="CH") for i in ids}
    assert families(assays) == {"CH": sorted(ids)}


def test_a_bare_list_of_ids_still_groups_by_base():
    """The fallback path: with no assays to ask, the id base is all there is."""
    assert families(["A", "A_round2", "B"]) == {"A": ["A", "A_round2"]}


def test_containment_asks_where_the_inner_primers_extend_from():
    """A shared site with a longer inner primer is still a nest.

    The enterovirus VP3/VP1 rounds share their reverse site; round 2's primer
    is 8 nt longer at its 5' end, so its amplicon ends exactly 8 bp past round
    1's on 3,722 of 3,808 records while priming from the identical base. The
    span test called that disjoint. What has to sit inside the outer product is
    the 3' end each inner primer extends from.
    """
    assays = {
        "E": _assay("E", "round1", 760, nested_family="E"),
        "E_round2": _assay("E_round2", "round2", 375, nested_family="E"),
    }
    outer = _row("E", "r", "detect", 2144, 2904)
    inner = _row("E_round2", "r", "detect", 2537, 2912)
    inner["fwd_site"], inner["rev_site"] = "2537-2563+", "2885-2912-"
    f = assess(assays, [outer, inner])["E"]
    assert f.containment[("E", "E_round2")] == (1, 1), "3' ends 2563 and 2885 are inside 2144-2904"
    assert f.nests is True


def test_containment_falls_back_to_the_span_when_no_sites_were_written():
    """Older calls have no site columns; the span test is all there is."""
    assays = {
        "E": _assay("E", "round1", 760, nested_family="E"),
        "E_round2": _assay("E_round2", "round2", 375, nested_family="E"),
    }
    rows = [_row("E", "r", "detect", 2144, 2904), _row("E_round2", "r", "detect", 2537, 2912)]
    f = assess(assays, rows)["E"]
    assert f.containment[("E", "E_round2")] == (0, 1), "the inner span overhangs by 8 bp"


def test_a_primer_reaching_outside_the_outer_product_is_not_contained():
    """The check still has to fail a pair that genuinely does not nest."""
    assays = {
        "D": _assay("D", "round1", 500, nested_family="D"),
        "D_round2": _assay("D_round2", "round2", 300, nested_family="D"),
    }
    outer = _row("D", "r", "detect", 1000, 1500)
    inner = _row("D_round2", "r", "detect", 4000, 4300)
    inner["fwd_site"], inner["rev_site"] = "4000-4020+", "4280-4300-"
    assert assess(assays, [outer, inner])["D"].nests is False


def test_round_one_failures_resting_on_the_diverged_label_are_counted_apart():
    """`diverged` counts as a round-1 failure, and stays counted, because it is
    the right reading where the label is right. But on 2026-10-23 round-1 anchors
    ran from 97% near-perfect (Phlebovirus L) to 60% chance-grade (Orthoreovirus
    Landolfi), so a reader needs to see how much of a nest loss rests on it."""
    from assaywatch.nested import NestedFamily, assess

    class Src:
        def __init__(self, r):
            self.nested_round, self.nested_family = r, "F"

    class A:
        def __init__(self, r):
            self.source, self.oligos = Src(r), None

    assays = {"F": A("round1"), "F_round2": A("round2")}
    calls = []
    for i, (oc, ox) in enumerate(
        [("detect", ""), ("fail", ""), ("no_amplicon", "diverged"), ("no_amplicon", "diverged")]
    ):
        calls += [
            {"assay_id": "F", "record_id": f"R{i}", "call": oc, "exclusion": ox},
            {"assay_id": "F_round2", "record_id": f"R{i}", "call": "detect", "exclusion": ""},
        ]
    fam = assess(assays, calls)["F"]
    assert isinstance(fam, NestedFamily)
    assert fam.records == 4
    assert fam.records - fam.outer_detected == 3
    assert fam.outer_diverged == 2
