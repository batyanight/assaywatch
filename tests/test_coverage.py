"""The coverage map: which species an assay is predicted to detect, as of today.

Agreed 2026-11-10 (GLOSSARY.md, "Coverage"). Coverage and drift are two summaries of
one calls table and neither imports the other. Every test here builds its calls table
by hand, a few rows at a time: `coverage_map` reads no file and no config, which is
what makes that possible.

The tests are in the order they were written, one step of the plan each.
"""

from __future__ import annotations

import csv
import gzip
from types import SimpleNamespace

import pytest

from assaywatch.coverage import (
    CellState,
    CoverageCell,
    CoverageRule,
    Together,
    coverage_map,
    main,
    recommend,
    render_markdown,
    rule_from_config,
    together_calls,
    together_id,
    trace_passes,
    with_locus,
)
from assaywatch.nested import NestPath
from assaywatch.score import load_config

pytestmark = pytest.mark.fast

RULE = CoverageRule(detect_min_share=0.95, fail_max_share=0.05)

# record -> species taxid. Frog virus 3 and a second ranavirus species stand in.
FV3, EHNV = 10493, 100217
SPECIES = {f"fv3_{i}": FV3 for i in range(20)} | {f"ehnv_{i}": EHNV for i in range(20)}
CLEAN = "|||0|0|0"  # the footprint of a record with no mismatch anywhere


def species_of(record_id):
    return SPECIES.get(record_id)


def scope_of(assay_id, species_taxid):
    """The assay "A" was published for Frog virus 3 and nothing else."""
    return species_taxid == FV3


def row(rec, call="detect", assay="A", exclusion="", footprint=CLEAN, **extra):
    out = {"assay_id": assay, "record_id": rec, "call": call, "exclusion": exclusion, **extra}
    if footprint is not None:
        out["footprint"] = footprint
    return out


def cell(cells, assay="A", species=FV3) -> CoverageCell:
    (got,) = [c for c in cells if c.assay_id == assay and c.species_taxid == species]
    return got


# --- step 1 --------------------------------------------------------------------------


def test_one_detected_record_is_one_cell_predicted_detect():
    cells = coverage_map([row("fv3_0")], species_of, scope_of, RULE)
    assert len(cells) == 1
    c = cells[0]
    assert (c.assay_id, c.species_taxid) == ("A", FV3)
    assert c.state is CellState.predicted_detect
    assert (c.detected, c.locus_present) == (1, 1)  # the cell count, "1/1"


# --- step 2 --------------------------------------------------------------------------


def test_records_that_split_make_the_cell_partial():
    rows = [row(f"fv3_{i}") for i in range(8)] + [row(f"fv3_{i}", "fail") for i in (8, 9)]
    c = cell(coverage_map(rows, species_of, scope_of, RULE))
    assert c.state is CellState.partial
    assert (c.detected, c.locus_present) == (8, 10)


# --- step 3 --------------------------------------------------------------------------


def test_records_that_all_fail_make_the_cell_predicted_fail():
    rows = [row(f"fv3_{i}", "fail") for i in range(4)]
    c = cell(coverage_map(rows, species_of, scope_of, RULE))
    assert c.state is CellState.predicted_fail
    assert (c.detected, c.locus_present) == (0, 4)


# --- step 4 --------------------------------------------------------------------------


def test_each_species_is_its_own_row():
    rows = [row("fv3_0"), row("ehnv_0", "fail")]
    cells = coverage_map(rows, species_of, scope_of, RULE)
    assert {c.species_taxid for c in cells} == {FV3, EHNV}
    assert cell(cells, species=FV3).state is CellState.predicted_detect
    assert cell(cells, species=EHNV).state is CellState.predicted_fail


def test_each_assay_gets_its_own_cell_for_the_same_species():
    rows = [row("fv3_0", assay="A"), row("fv3_0", "fail", assay="B")]
    cells = coverage_map(rows, species_of, scope_of, RULE)
    assert cell(cells, "A").state is CellState.predicted_detect
    assert cell(cells, "B").state is CellState.predicted_fail


# --- step 5 --------------------------------------------------------------------------


def test_an_out_of_scope_species_is_shown_and_labelled_not_dropped():
    """Drift uses scope to shrink its denominator. Coverage uses it only as a label."""
    cells = coverage_map([row("fv3_0"), row("ehnv_0")], species_of, scope_of, RULE)
    assert cell(cells, species=FV3).in_scope is True
    out = cell(cells, species=EHNV)
    assert out.in_scope is False
    assert out.state is CellState.predicted_detect  # "this assay also picks up ..."


def test_a_record_whose_species_is_unknown_is_left_out():
    """No species, no row to put it in. The caller counts these; the map does not guess."""
    cells = coverage_map([row("fv3_0"), row("mystery")], species_of, scope_of, RULE)
    assert [c.species_taxid for c in cells] == [FV3]


# --- step 6 --------------------------------------------------------------------------


def test_a_species_with_no_locus_present_record_is_not_assessable():
    """A deposit that is too short to hold the amplicon never tested the assay."""
    rows = [row(f"ehnv_{i}", "no_amplicon", exclusion="truncated", footprint=None) for i in range(3)]
    c = cell(coverage_map(rows, species_of, scope_of, RULE), species=EHNV)
    assert c.state is CellState.not_assessable
    assert (c.detected, c.locus_present) == (0, 0)


def test_a_diverged_site_counts_as_locus_present_and_not_detected():
    """`diverged` is the screen saying the site is in the deposit and does not match."""
    rows = [row("ehnv_0", "no_amplicon", exclusion="diverged", footprint=None)]
    c = cell(coverage_map(rows, species_of, scope_of, RULE), species=EHNV)
    assert c.state is CellState.predicted_fail
    assert (c.detected, c.locus_present) == (0, 1)


def test_records_that_never_tested_the_assay_stay_out_of_the_cell_count():
    rows = [row("fv3_0"), row("fv3_1", "no_amplicon", exclusion="truncated", footprint=None)]
    rows.append(row("fv3_2", "indeterminate", footprint=None))
    c = cell(coverage_map(rows, species_of, scope_of, RULE))
    assert (c.detected, c.locus_present) == (1, 1)


def test_a_locus_check_result_on_the_row_overrides_the_screens_guess():
    """The seam for the locus check (improvement 3): it writes `locus_present` on a row.

    Today the only evidence that a record holds the locus is that the primers found
    their sites in it. Once a locus check exists, a record where NO primer site was
    found but the locus is there becomes a real failure, and one where the screen
    said `diverged` but the locus is absent stops counting.
    """
    rows = [
        row("ehnv_0", "no_amplicon", exclusion="no_site", footprint=None, locus_present=True),
        row("ehnv_1", "no_amplicon", exclusion="diverged", footprint=None, locus_present=False),
    ]
    c = cell(coverage_map(rows, species_of, scope_of, RULE), species=EHNV)
    assert (c.detected, c.locus_present) == (0, 1)
    assert c.state is CellState.predicted_fail


# --- step 7 --------------------------------------------------------------------------


def test_footprints_count_distinct_mismatch_patterns_behind_the_cell_count():
    """300/300 from two footprints is one outbreak sequenced 300 times."""
    rows = [row(f"fv3_{i}") for i in range(6)]
    rows += [row(f"fv3_{i}", footprint="3||||0|0|0") for i in range(6, 9)]
    c = cell(coverage_map(rows, species_of, scope_of, RULE))
    assert (c.detected, c.locus_present, c.footprints) == (9, 9, 2)


def test_a_row_without_a_footprint_adds_none():
    rows = [row("fv3_0"), row("fv3_1", footprint=None)]
    assert cell(coverage_map(rows, species_of, scope_of, RULE)).footprints == 1


def test_reduced_records_are_detected_and_make_the_cell_partial():
    """Detected, with an expected loss of efficiency: amplifies, expect a Ct shift.

    They are in the numerator (the assay does pick the species up) and they keep the
    cell from reading `predicted detect`, which is reserved for a clean match.
    """
    rows = [row(f"fv3_{i}", "reduced") for i in range(5)]
    c = cell(coverage_map(rows, species_of, scope_of, RULE))
    assert (c.detected, c.reduced, c.locus_present) == (5, 5, 5)
    assert c.state is CellState.partial


def test_a_few_reduced_records_do_not_cost_a_cell_its_detect():
    rows = [row(f"fv3_{i}") for i in range(19)] + [row("fv3_19", "reduced")]
    c = cell(coverage_map(rows, species_of, scope_of, RULE))
    assert c.state is CellState.predicted_detect  # 19/20 clean = 95%, the agreed cut
    assert (c.detected, c.reduced) == (20, 1)


def test_the_cuts_are_inclusive_at_both_ends():
    one_in_twenty_detected = [row("fv3_0")] + [row(f"fv3_{i}", "fail") for i in range(1, 20)]
    assert (
        cell(coverage_map(one_in_twenty_detected, species_of, scope_of, RULE)).state
        is CellState.predicted_fail
    )
    two_in_twenty = [row(f"fv3_{i}") for i in (0, 1)] + [row(f"fv3_{i}", "fail") for i in range(2, 20)]
    assert cell(coverage_map(two_in_twenty, species_of, scope_of, RULE)).state is CellState.partial


def test_the_hosts_of_a_cells_records_are_shown_most_common_first():
    """Host is a column, never a row. Blank until retrieval stores GenBank's /host."""
    rows = [row("fv3_0", host="Lithobates sylvaticus"), row("fv3_1", host="Lithobates sylvaticus")]
    rows += [row("fv3_2", host="Terrapene carolina"), row("fv3_3")]
    assert cell(coverage_map(rows, species_of, scope_of, RULE)).hosts == (
        "Lithobates sylvaticus",
        "Terrapene carolina",
    )


def test_cells_come_back_in_a_stable_order():
    rows = [row("ehnv_0", assay="B"), row("ehnv_0"), row("fv3_0"), row("fv3_0", assay="B")]
    cells = coverage_map(rows, species_of, scope_of, RULE)
    # by assay, the in-scope block first, then by species taxid
    assert [(c.assay_id, c.species_taxid) for c in cells] == [
        ("A", FV3),
        ("A", EHNV),
        ("B", FV3),
        ("B", EHNV),
    ]


# --- step 8 --------------------------------------------------------------------------


def _cell(assay, state, detected=10, present=10, species=EHNV):
    return CoverageCell(assay, species, False, state, detected, present, 1, ())


def test_recommend_orders_assays_for_one_species_by_cell_state():
    cells = [
        _cell("fails", CellState.predicted_fail, 0),
        _cell("blank", CellState.not_assessable, 0, 0),
        _cell("works", CellState.predicted_detect),
        _cell("partly", CellState.partial, 6),
        _cell("other_species", CellState.predicted_detect, species=FV3),
    ]
    assert [c.assay_id for c in recommend(cells, EHNV)] == ["works", "partly", "fails", "blank"]


def test_recommend_breaks_a_tie_toward_the_less_degenerate_primer_pool():
    """Degeneracy never changes a cell. It decides between two cells that agree."""
    cells = [
        _cell("consensus_nest", CellState.predicted_detect),
        _cell("specific", CellState.predicted_detect),
    ]
    ranked = recommend(cells, EHNV, degeneracy_of={"consensus_nest": 4096, "specific": 1})
    assert [c.assay_id for c in ranked] == ["specific", "consensus_nest"]


def test_recommend_then_prefers_the_cell_with_more_behind_it():
    cells = [
        _cell("three_records", CellState.predicted_detect, 3, 3),
        _cell("ninety", CellState.predicted_detect, 90, 90),
    ]
    assert [c.assay_id for c in recommend(cells, EHNV)] == ["ninety", "three_records"]


# --- step 9: nested rows ----------------------------------------------------------------

PATH = NestPath(nest_id="N_round2", family="N", rounds=("N_round1", "N_round2"), shared_oligos=())
FREE = frozenset({"G:T", "T:G"})  # the mispairs config.yaml prices at zero


def r1(rec, call="detect", exclusion="", fwd_mm="", fwd_mispairs="", **extra):
    return row(
        rec,
        call,
        assay="N_round1",
        exclusion=exclusion,
        fwd_mm_from_3prime=fwd_mm,
        rev_mm_from_3prime="",
        fwd_mispairs=fwd_mispairs,
        rev_mispairs="",
        **extra,
    )


def by_assay(rows):
    out: dict = {}
    for r in rows:
        out.setdefault(r["assay_id"], {})[r["record_id"]] = r
    return out


def together(round1_rows, round2_rows, rule=Together.trace):
    return list(together_calls(PATH, by_assay([*round1_rows, *round2_rows]), FREE, rule))


def test_together_is_round_twos_call_when_round_one_works():
    (t,) = together([r1("fv3_0")], [row("fv3_0", assay="N_round2")])
    assert t["assay_id"] == together_id("N_round2", Together.trace) == "N_round2@together-trace"
    assert t["call"] == "detect"


def test_the_strict_rule_needs_round_one_detected_in_its_own_right():
    """The other end of the range: the same record the trace rule lets through."""
    mid_primer = r1("fv3_0", "fail", fwd_mm="12,9,7", fwd_mispairs="C:A@12,A:C@9,G:A@7")
    (t,) = together([mid_primer], [row("fv3_0", assay="N_round2")], Together.strict)
    assert t["assay_id"] == "N_round2@together-strict"
    assert t["call"] == "fail"
    (ok,) = together([r1("fv3_0", "reduced")], [row("fv3_0", assay="N_round2")], Together.strict)
    assert ok["call"] == "detect"


def test_the_two_together_rows_share_one_denominator():
    rounds = [r1("fv3_0"), r1("fv3_1", "fail", fwd_mm="9", fwd_mispairs="C:A@9"), r1("fv3_2", "no_amplicon")]
    rounds += [row(f"fv3_{i}", assay="N_round2") for i in range(3)]
    trace, strict = together(rounds, []), together(rounds, [], Together.strict)
    assert [t["record_id"] for t in trace] == [t["record_id"] for t in strict] == ["fv3_0", "fv3_1"]
    assert [t["call"] for t in trace] == ["detect", "detect"]
    assert [t["call"] for t in strict] == ["detect", "fail"]


def test_round_one_only_has_to_make_a_trace_of_product():
    """The trace rule. Round 1 scored `fail` on penalty alone still feeds round 2.

    A nest's first round runs at a forgiving anneal for many cycles and only has to
    hand round 2 a trace. A rule tuned on single-round PCR overstates its failure.
    """
    mid_primer = r1("fv3_0", "fail", fwd_mm="12,9,7", fwd_mispairs="C:A@12,A:C@9,G:A@7")
    assert trace_passes(mid_primer, FREE)
    (t,) = together([mid_primer], [row("fv3_0", assay="N_round2")])
    assert t["call"] == "detect"


def test_a_three_prime_terminal_mismatch_in_round_one_fails_the_protocol():
    blocked = r1("fv3_0", "fail", fwd_mm="1", fwd_mispairs="C:A@1")
    assert not trace_passes(blocked, FREE)
    (t,) = together([blocked], [row("fv3_0", assay="N_round2")])
    assert t["call"] == "fail"


def test_a_terminal_mispair_the_config_prices_at_zero_does_not_block():
    wobble = r1("fv3_0", "fail", fwd_mm="12,9,7,1", fwd_mispairs="C:A@12,A:C@9,G:A@7,G:T@1")
    assert trace_passes(wobble, FREE)


def test_no_round_one_site_fails_the_protocol():
    no_site = r1("fv3_0", "no_amplicon", exclusion="diverged", footprint=None)
    (t,) = together([no_site], [row("fv3_0", assay="N_round2")])
    assert t["call"] == "fail"


def test_a_round_one_fail_with_no_mismatch_columns_is_read_strictly():
    """An older screen's row cannot say WHY it failed, so the trace rule cannot excuse it."""
    old = row("fv3_0", "fail", assay="N_round1")
    assert not trace_passes(old, FREE)


def test_a_record_round_one_was_never_tested_on_is_not_a_together_row():
    truncated = r1("fv3_0", "no_amplicon", exclusion="truncated", footprint=None)
    assert together([truncated], [row("fv3_0", assay="N_round2")]) == []


def test_a_round_one_record_the_locus_stage_shows_to_be_a_real_failure_fails_the_protocol():
    """Round 1 found no primer site, and the screen could not say why, so the record
    was left out of both `together` rows. The locus stage says the locus is there with
    room for the primers: now it is round 1's failure, and the protocol's.
    """
    unjudged = r1("fv3_0", "no_amplicon", exclusion="no_site", footprint=None)
    assert together([unjudged], [row("fv3_0", assay="N_round2")]) == []
    judged = with_locus(dict(unjudged), {"fv3_0": True})
    assert (judged["locus_present"], judged["exclusion"]) == (True, "diverged")
    for rule in Together:
        (t,) = together([judged], [row("fv3_0", assay="N_round2")], rule)
        assert t["call"] == "fail"


def test_a_record_the_locus_stage_did_not_check_or_found_empty_is_left_as_it_was():
    unjudged = r1("fv3_0", "no_amplicon", exclusion="no_site", footprint=None)
    assert with_locus(dict(unjudged), None) == unjudged
    assert with_locus(dict(unjudged), {"other": True}) == unjudged
    absent = with_locus(dict(unjudged), {"fv3_0": False})
    assert (absent["locus_present"], absent["exclusion"]) == (False, "no_site")
    assert together([absent], [row("fv3_0", assay="N_round2")]) == []


def test_round_two_failing_fails_the_protocol_whatever_round_one_did():
    (t,) = together([r1("fv3_0")], [row("fv3_0", "fail", assay="N_round2")])
    assert t["call"] == "fail"


def test_a_nested_protocol_gets_its_rounds_alone_and_together_under_both_rules():
    """Round 1 alone, round 2 alone, and together twice: the published protocol as a
    range, and both fallbacks.

    Here round 1 has a 3'-terminal mismatch on this species and round 2 matches. So
    the protocol as published fails, and round 2 run directly on the sample works:
    exactly the "round 1 isn't picking it up, run round 2 alone" reading.
    """
    rounds = [r1("ehnv_0", "fail", fwd_mm="1", fwd_mispairs="C:A@1"), row("ehnv_0", assay="N_round2")]
    rows = [*rounds, *(t for how in Together for t in together_calls(PATH, by_assay(rounds), FREE, how))]
    cells = coverage_map(rows, species_of, scope_of, RULE)
    assert [c.assay_id for c in cells] == [
        "N_round1",
        "N_round2",
        "N_round2@together-strict",
        "N_round2@together-trace",
    ]
    assert cell(cells, "N_round2@together-trace", EHNV).state is CellState.predicted_fail
    assert cell(cells, "N_round2@together-strict", EHNV).state is CellState.predicted_fail
    assert cell(cells, "N_round1", EHNV).state is CellState.predicted_fail
    assert cell(cells, "N_round2", EHNV).state is CellState.predicted_detect


# --- the rule itself --------------------------------------------------------------------


def test_the_shipped_config_carries_the_agreed_cuts():
    assert rule_from_config(load_config()) == RULE


@pytest.mark.parametrize(("detect_min", "fail_max"), [(0.5, 0.5), (0.2, 0.6), (1.2, 0.05), (0.95, -0.1)])
def test_a_rule_whose_cuts_cross_or_leave_the_unit_interval_is_refused(detect_min, fail_max):
    with pytest.raises(ValueError, match="share"):
        CoverageRule(detect_min_share=detect_min, fail_max_share=fail_max)


# --- step 10: the report, end to end on a tiny calls table ------------------------------

HEADER = [
    "assay_id",
    "record_id",
    "call",
    "exclusion",
    "fwd_penalty",
    "fwd_mm_from_3prime",
    "fwd_ambiguous",
    "rev_penalty",
    "rev_mm_from_3prime",
    "rev_ambiguous",
    "probe_mm_from_3prime",
    "probe_ambiguous",
    "fwd_mispairs",
    "rev_mispairs",
    "degeneracy_fold",
    "degeneracy_tier",
]


def _write_run(tmp_path, monkeypatch):
    """A registry of one assay, three records of two species, and a taxonomy for them."""
    calls = tmp_path / "calls.tsv.gz"
    rows = [
        ["A", "AB000001.1", "detect", "", "0", "", "0", "0", "", "0", "", "", "", "", "4", "negligible"],
        ["A", "AB000002.1", "detect", "", "0", "", "0", "0", "", "0", "", "", "", "", "4", "negligible"],
        ["A", "AB000003.1", "fail", "", "9", "1", "0", "0", "", "0", "", "", "C:A@1", "", "4", "negligible"],
        # screened once, since moved out of the registry: no declared scope, so no row
        ["GONE", "AB000001.1", "detect", "", "0", "", "0", "0", "", "0", "", "", "", "", "1", "negligible"],
    ]
    with gzip.open(calls, "wt", newline="") as fh:
        csv.writer(fh, delimiter="\t", lineterminator="\n").writerows([HEADER, *rows])
    retrieved = tmp_path / "retrieved" / "10493" / "g"
    retrieved.mkdir(parents=True)
    with gzip.open(retrieved / "records.meta.tsv.gz", "wt") as fh:
        fh.write("accession\tcreated\ttaxid\n")
        # 654924 is a strain under Frog virus 3: it must roll up to the species row.
        fh.write(f"AB000001\t2020-01-01\t{FV3}\nAB000002\t2021-01-01\t654924\nAB000003\t2022-01-01\t{EHNV}\n")
    taxonomy = SimpleNamespace(
        species_of=lambda t: {FV3: FV3, 654924: FV3, EHNV: EHNV}.get(t),
        within=lambda t, scope: t in scope,
        canonical=lambda t: t,
        name={FV3: "Frog virus 3", EHNV: "Epizootic haematopoietic necrosis virus"},
    )
    assay = SimpleNamespace(
        id="A",
        target=SimpleNamespace(taxid=FV3, scope_taxids=None),
        source=SimpleNamespace(nested_round=None, nested_parent=None, nested_family=None),
    )
    monkeypatch.setattr("assaywatch.coverage.taxonomy_from_config", lambda cfg: taxonomy)
    monkeypatch.setattr("assaywatch.coverage.load_registry", lambda path: {"A": assay})
    return calls, tmp_path / "retrieved"


def test_the_coverage_stage_writes_a_table_and_a_report(tmp_path, monkeypatch):
    calls, retrieved = _write_run(tmp_path, monkeypatch)
    out = tmp_path / "out"
    assert main([str(calls), "--retrieved", str(retrieved), "--out", str(out)]) == 0

    with open(out / "coverage.tsv", newline="") as fh:
        table = list(csv.DictReader(fh, delimiter="\t"))
    got = {int(r["species_taxid"]): r for r in table}
    assert got[FV3]["state"] == "predicted detect"
    assert (got[FV3]["detected"], got[FV3]["locus_present"], got[FV3]["in_scope"]) == ("2", "2", "yes")
    assert got[EHNV]["state"] == "predicted fail"
    assert got[EHNV]["in_scope"] == "no"
    assert got[EHNV]["species"] == "Epizootic haematopoietic necrosis virus"

    assert {r["assay_id"] for r in table} == {"A"}

    report = (out / "coverage.md").read_text()
    assert "`GONE`" in report and "registry does not hold" in report
    assert "Frog virus 3" in report
    assert "2/2" in report and "0/1" in report  # no cell is printed without its count
    assert "Out of scope" in report
    # the asymmetry is in the wording: a detect says the oligos match, not that the reaction works
    assert "no mismatch that would block" in report


def test_recommend_on_the_command_line_rolls_a_strain_up_to_its_species_row(tmp_path, monkeypatch, capsys):
    calls, retrieved = _write_run(tmp_path, monkeypatch)
    main([str(calls), "--retrieved", str(retrieved), "--out", str(tmp_path / "out"), "--recommend", "654924"])
    printed = capsys.readouterr().out
    assert "Frog virus 3" in printed
    assert "predicted detect" in printed and "2/2" in printed


def test_not_assessable_cells_are_summed_in_the_report_and_listed_in_the_table():
    """A blank has no count to print, and a pan-family archive holds thousands of them."""
    cells = [
        CoverageCell("A", FV3, True, CellState.predicted_detect, 2, 2, 1, ()),
        CoverageCell("A", EHNV, False, CellState.not_assessable, 0, 0, 0, ()),
        CoverageCell("A", 999, False, CellState.not_assessable, 0, 0, 0, ()),
    ]
    report = render_markdown(cells, lambda t: f"taxon {t}", lambda a: "", {}, [])
    assert "taxon 10493" in report and "2/2" in report
    assert "taxon 999" not in report
    assert "2 more species `not assessable`" in report  # summed, not listed


def test_coverage_does_not_load_the_drift_module():
    """Coverage and drift are two summaries of one calls table, and neither is built
    on the other. The footprint both read is defined with the table (`calls.py`), so
    importing coverage must not pull in the drift statistic at all. A fresh
    interpreter, because this test session has long since imported everything.
    """
    import subprocess
    import sys

    code = "import sys, assaywatch.coverage; print('assaywatch.drift' in sys.modules)"
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    assert out.stdout.strip() == "False"


# --- UNVERIFIED records get a row of their own (maintainer decision, 2026-11-10) -----------
#
# GenBank puts UNVERIFIED at the front of a title when it could not confirm the
# sequence or its annotation. The record keeps the organism its submitter gave it. On
# the 2026-11-01 calls, 55 such genomes titled Santee-Cooper ranavirus, with a major
# capsid gene 75% identical to that species' references, took an assay from 28/28 to
# 28/83 on the species. The primers do fail on them. Whether they are the species is
# what GenBank declines to say, so they are counted, beside the species and not in it.


def test_unverified_records_are_counted_beside_the_species_not_in_it():
    doubtful = {f"fv3_{i}" for i in range(3, 8)}
    rows = [row(f"fv3_{i}") for i in range(3)] + [
        row(r, call="fail", footprint="1|||0|0|0") for r in doubtful
    ]
    cells = coverage_map(rows, species_of, scope_of, RULE, unverified=doubtful.__contains__)
    (species,) = [c for c in cells if not c.unverified]
    (beside,) = [c for c in cells if c.unverified]
    assert (species.species_taxid, species.count, species.state) == (FV3, "3/3", CellState.predicted_detect)
    assert (beside.species_taxid, beside.count, beside.state) == (FV3, "0/5", CellState.predicted_fail)
    assert beside.in_scope == species.in_scope  # the same species as far as scope goes
    assert cells.index(species) < cells.index(beside)  # the species row first


def test_without_being_told_which_records_are_unverified_nothing_changes():
    rows = [row(f"fv3_{i}") for i in range(3)] + [row("fv3_3", call="fail")]
    (only,) = coverage_map(rows, species_of, scope_of, RULE)
    assert (only.count, only.unverified) == ("3/4", False)


def test_a_recommendation_is_made_from_verified_records():
    """Otherwise the doubtful row would be offered as a second verdict on the species."""
    doubtful = {"fv3_5", "fv3_6"}
    rows = [row(f"fv3_{i}") for i in range(3)] + [row(r, call="fail") for r in doubtful]
    cells = coverage_map(rows, species_of, scope_of, RULE, unverified=doubtful.__contains__)
    assert [c.count for c in recommend(cells, FV3)] == ["3/3"]


def test_unverified_is_read_from_the_front_of_the_title(tmp_path):
    from assaywatch.coverage import read_unverified

    d = tmp_path / "1" / "g"
    d.mkdir(parents=True)
    with gzip.open(d / "a.meta.tsv.gz", "wt") as fh:
        fh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
        fh.write(
            "1\tAA000001\t2020-01-01\t2020-01-01\t500\tUNVERIFIED: Some virus isolate X, complete genome\n"
        )
        fh.write("2\tAA000002\t2020-01-01\t2020-01-01\t500\tUNVERIFIED_ORG: Some virus isolate Y\n")
        fh.write("3\tAA000003\t2020-01-01\t2020-01-01\t500\tUNVERIFIED_ASMBLY: Some virus isolate Z\n")
        fh.write(
            "4\tAA000004\t2020-01-01\t2020-01-01\t500\tSome virus, previously unverified, complete genome\n"
        )
    with gzip.open(d / "old.meta.tsv.gz", "wt") as fh:  # an archive written before titles were kept
        fh.write("accession\tcreated\ttaxid\nAA000005\t2020-01-01\t1\n")
    assert read_unverified(tmp_path) == {"AA000001", "AA000002", "AA000003"}


def test_the_stage_gives_unverified_records_their_own_row(tmp_path, monkeypatch):
    calls, retrieved = _write_run(tmp_path, monkeypatch)
    with gzip.open(retrieved / "10493" / "g" / "titles.meta.tsv.gz", "wt") as fh:
        fh.write("accession\ttitle\n")
        fh.write("AB000001\tFrog virus 3 isolate 1, complete genome\n")
        fh.write("AB000002\tUNVERIFIED: Frog virus 3 isolate 2, complete genome\n")
    out = tmp_path / "out"
    assert main([str(calls), "--retrieved", str(retrieved), "--out", str(out)]) == 0
    with open(out / "coverage.tsv", newline="") as fh:
        fv3 = [r for r in csv.DictReader(fh, delimiter="\t") if int(r["species_taxid"]) == FV3]
    assert sorted((r["unverified"], r["detected"], r["locus_present"]) for r in fv3) == [
        ("no", "1", "1"),
        ("yes", "1", "1"),
    ]
    report = (out / "coverage.md").read_text()
    assert "Frog virus 3 (10493), UNVERIFIED records" in report
    assert (
        "1 record" in report and "UNVERIFIED" in report.split("## How to read a cell")[0]
    )  # the header counts them


# --- an out-of-scope failure is specificity (maintainer decision, 2026-11-10) ----------------


def test_the_out_of_scope_block_says_what_a_failure_there_means():
    """A 16S assay finds a 16S gene in every bacterium in its archive and amplifies
    none of them. Out of scope that is the assay not cross-reacting, and the block says
    so in words; the state keeps its one name."""
    cells = [
        CoverageCell("A", FV3, True, CellState.predicted_fail, 0, 9, 1, ()),
        CoverageCell("A", EHNV, False, CellState.predicted_fail, 0, 7, 1, ()),
    ]
    report = render_markdown(cells, lambda t: f"taxon {t}", lambda a: "", {}, [])
    inside, outside = report.split("**Out of scope**")
    assert "not to cross-react" in outside and "`predicted fail`" in outside
    assert "cross-react" not in inside.split("**In scope**")[1]
