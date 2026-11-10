"""Wide reference amplicons: the amplicon plus its flanks, for the locus check.

The first references were amplicon INTERIORS (primer sites trimmed off). For a short
amplicon that leaves almost nothing: 17 bases for a 57 bp product. A wide reference is
cut the other way, the amplicon plus up to `flank_bp` either side from the same record,
so even the shortest amplicon gives the aligner a few hundred bases to work with.
"""

from __future__ import annotations

import gzip
import importlib.util
import json
import random
from pathlib import Path

import pytest

from assaywatch.locus import Reference, judge, read_references
from assaywatch.locus_check import locus_check

pytestmark = pytest.mark.fast

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("build_refs", ROOT / "scripts" / "build_locus_references.py")
build_refs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_refs)


def dna(n: int, seed: int) -> str:
    rng = random.Random(seed)
    return "".join(rng.choice("ACGT") for _ in range(n))


def revcomp(seq: str) -> str:
    return seq.translate(str.maketrans("ACGT", "TGCA"))[::-1]


# --- choosing which records to cut references from -----------------------------------------


def source(rid, bp=200, species=1, start=500, length=5000):
    return {
        "record_id": rid,
        "amplicon_bp": bp,
        "species": species,
        "start": start,
        "end": start + bp,
        "length": length,
    }


def test_one_source_is_taken_per_amplicon_length_before_any_length_repeats():
    """A locus whose length varies (a repeat region) needs a reference of each length,
    or the records of the other lengths are not shown to hold the locus."""
    rows = [source(f"a{i}", bp=260) for i in range(50)] + [source("b", bp=276), source("c", bp=308)]
    picked = build_refs.choose_sources(rows, flank_bp=100, limit=3)
    assert sorted(r["amplicon_bp"] for r in picked) == [260, 276, 308]


def test_then_one_per_species_so_the_references_span_the_lineages_the_assay_covers():
    rows = [source(f"a{i}", species=1) for i in range(50)] + [source("b", species=2), source("c", species=3)]
    picked = build_refs.choose_sources(rows, flank_bp=100, limit=3)
    assert sorted(r["species"] for r in picked) == [1, 2, 3]


def test_a_record_with_room_for_both_flanks_is_preferred_to_one_without():
    cramped = source("a_first_by_id", start=10)  # only 10 bases before the amplicon
    roomy = source("z_last_by_id", start=500)
    (picked,) = build_refs.choose_sources([cramped, roomy], flank_bp=100, limit=1)
    assert picked["record_id"] == "z_last_by_id"


def test_the_choice_does_not_depend_on_the_order_the_calls_table_was_read_in():
    rows = [source(f"r{i}", bp=200 + 16 * (i % 3), species=i % 4) for i in range(40)]
    a = build_refs.choose_sources(rows, flank_bp=100, limit=8)
    b = build_refs.choose_sources(rows[::-1], flank_bp=100, limit=8)
    assert [r["record_id"] for r in a] == [r["record_id"] for r in b]


# --- cutting them ---------------------------------------------------------------------------


def test_cut_takes_the_amplicon_and_its_flanks_and_records_how_much_flank_it_got(tmp_path):
    amplicon = dna(60, seed=1)
    full = dna(300, seed=2) + amplicon + dna(300, seed=3)
    short = dna(30, seed=4) + amplicon + dna(300, seed=5)  # the record starts 30 bases before the amplicon
    archive = tmp_path / "retrieved" / "10493" / "all"
    archive.mkdir(parents=True)
    with gzip.open(archive / "2026-11-01.fasta.gz", "wt") as fh:
        fh.write(f">FULL.1 a title\n{full}\n>SHORT.1\n{short}\n>UNWANTED.1\n{dna(500, seed=6)}\n")
    manifest = tmp_path / "manifest.tsv"
    manifest.write_text(
        "archive\tassay_id\trecord_id\tamplicon_start\tamplicon_end\n"
        "10493/all\tA\tFULL.1\t300\t360\n"
        "10493/all\tA\tSHORT.1\t30\t90\n"
        "10493/all\tB\tFULL.1\t300\t360\n"
    )
    out = tmp_path / "wide.json"
    assert (
        build_refs.main(["cut", str(manifest), "--retrieved", str(tmp_path / "retrieved"), "--out", str(out)])
        == 0
    )
    got = json.loads(out.read_text())

    first, second = got["A"]["references"]
    assert (first["from"], first["left"], first["right"]) == ("FULL.1", 100, 100)
    assert first["seq"] == full[200:460]
    assert (second["from"], second["left"], second["right"]) == ("SHORT.1", 30, 100)
    assert second["seq"] == short[0:190]
    assert [r["from"] for r in got["B"]["references"]] == ["FULL.1"]  # one record can serve two assays


# --- using them -----------------------------------------------------------------------------

AMPLICON = dna(60, seed=10)
L, R = dna(100, seed=11), dna(100, seed=12)
WIDE = Reference(L + AMPLICON + R, left=100, right=100)


def test_both_kinds_of_reference_file_are_read(tmp_path):
    wide = tmp_path / "wide.json"
    wide.write_text(
        json.dumps({"A": {"references": [{"from": "X.1", "left": 100, "right": 90, "seq": "ACGT" * 60}]}})
    )
    assert read_references(wide, min_bp=100, trim_bp=20) == {"A": [Reference("ACGT" * 60, 100, 90)]}
    interiors = tmp_path / "interiors.json"
    interiors.write_text(json.dumps({"A": {"interiors": ["ACGT" * 30, "ACGT"]}}))
    # an interior is the amplicon LESS 20 bases each side, so its pads are minus 20
    assert read_references(interiors, min_bp=100, trim_bp=20) == {"A": [Reference("ACGT" * 30, -20, -20)]}


def test_a_short_amplicon_can_now_be_checked():
    """60 bp of amplicon is too little to define a locus. 260 bp with its flanks is not."""
    record = dna(400, seed=13) + L + AMPLICON + R + dna(400, seed=14)
    result, has_room = judge(record, [WIDE], 0.6, 0.8)
    assert result.present and has_room


def test_with_a_wide_reference_room_means_the_record_reaches_across_the_amplicon():
    """The flanks may run off the end of the record. The amplicon may not."""
    whole_amplicon = L[40:] + AMPLICON + R  # 40 bases of the left flank are missing
    result, has_room = judge(whole_amplicon + dna(300, seed=15), [WIDE], 0.6, 0.8)
    assert result.present and has_room
    cut_into = AMPLICON[25:] + R + dna(400, seed=16)  # the record starts inside the amplicon
    result, has_room = judge(cut_into, [WIDE], 0.0, 0.0)
    assert not has_room


def test_room_is_judged_in_the_references_own_direction_on_the_other_strand():
    """Uneven pads: 100 bases of flank before the amplicon and 20 after. On the reverse
    strand the 20 is on the record's LEFT."""
    uneven = Reference(L + AMPLICON + R[:20], left=100, right=20)
    record = dna(300, seed=17) + L + AMPLICON  # ends exactly where the amplicon ends
    assert locus_check(revcomp(record), [uneven.seq], 0.6, 0.8).strand == "-"
    for rec in (record, revcomp(record)):
        result, has_room = judge(rec, [uneven], 0.6, 0.8)
        assert result.present and has_room, result
    shy = record[:-5]  # five bases short of the amplicon's end
    for rec in (shy, revcomp(shy)):
        assert not judge(rec, [uneven], 0.0, 0.0)[1]


def test_the_best_reference_decides_and_its_own_pads_are_the_ones_used():
    other = Reference(dna(260, seed=18), left=0, right=0)
    record = dna(400, seed=13) + L + AMPLICON + R + dna(400, seed=14)
    result, has_room = judge(record, [other, WIDE], 0.6, 0.8)
    assert result.present and has_room
