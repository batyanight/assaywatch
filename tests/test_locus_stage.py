"""The locus stage: run the locus check on the records the screen could not judge.

`assaywatch locus` reads a calls table and the archives, checks only the rows where no
amplicon was found and the screen did not already say why the assay was at fault, and
writes a side file (`locus.tsv.gz`). `assaywatch coverage --locus` joins it. The screen
is not touched, so nothing is rescreened (a maintainer decision, 2026-11-10).
"""

from __future__ import annotations

import csv
import gzip
import json
import random
from types import SimpleNamespace

import pytest

from assaywatch import coverage, locus
from assaywatch.locus import Reference, judge, needs_check, read_locus
from assaywatch.locus_check import locus_check

pytestmark = pytest.mark.fast

FLANK = 20  # the bases trimmed off each end of a reference amplicon: where the primers sit


def dna(n: int, seed: int) -> str:
    rng = random.Random(seed)
    return "".join(rng.choice("ACGT") for _ in range(n))


INTERIOR = dna(160, seed=1)  # a reference amplicon with its primer sites trimmed off
GENOME_L, GENOME_R = dna(400, seed=2), dna(400, seed=3)
REF = Reference(INTERIOR, -FLANK, -FLANK)  # an interior: the amplicon reaches FLANK beyond each end


def substitute(seq: str, share: float, seed: int) -> str:
    rng = random.Random(seed)
    out = list(seq)
    for pos in rng.sample(range(len(seq)), round(share * len(seq))):
        out[pos] = rng.choice([b for b in "ACGT" if b != out[pos]])
    return "".join(out)


# --- which rows are checked --------------------------------------------------------------


@pytest.mark.parametrize(
    ("call", "exclusion", "want"),
    [
        ("no_amplicon", "no_site", True),  # nothing credible for either primer: the case it exists for
        ("no_amplicon", "chance_only", True),
        ("no_amplicon", "no_pair", True),
        ("no_amplicon", "truncated", True),  # the screen's guess; the check and the flank rule decide
        ("no_amplicon", "diverged", False),  # the screen already saw a site that is there and does not fit
        ("detect", "", False),  # both primers found their sites: the locus is there
        ("fail", "", False),
        ("indeterminate", "", False),  # too many undetermined bases: not a question about the locus
    ],
)
def test_only_records_the_screen_could_not_judge_are_checked(call, exclusion, want):
    assert needs_check({"call": call, "exclusion": exclusion}) is want


# --- the flank rule ----------------------------------------------------------------------


def test_the_check_reports_how_much_record_lies_beyond_the_reference():
    got = locus_check("A" * 30 + INTERIOR + "C" * 50, [INTERIOR], 0.7, 0.8)
    assert (got.flank_left, got.flank_right) == (30, 50)


def test_the_flanks_are_reported_in_record_order_on_the_other_strand_too():
    record = "A" * 30 + INTERIOR + "C" * 50
    revcomp = record.translate(str.maketrans("ACGT", "TGCA"))[::-1]
    got = locus_check(revcomp, [INTERIOR], 0.7, 0.8)
    assert (got.flank_left, got.flank_right) == (50, 30)


def test_a_locus_with_room_for_both_primer_sites_is_a_real_failure_to_bind():
    """Present, and the record runs past it on both sides: the primers had their chance."""
    result, has_room = judge(GENOME_L + INTERIOR + GENOME_R, [REF], 0.7, 0.8)
    assert result.present and has_room


def test_a_locus_at_the_very_end_of_a_record_never_tested_the_primers():
    """The reference is the amplicon's INTERIOR, so it can be whole in a record that
    stops before a primer site. Calling that a failure would blame the assay for a
    deposit that was cut short. Present, and no room: it does not count.
    """
    result, has_room = judge(GENOME_L + INTERIOR + "ACGTACGT", [REF], 0.7, 0.8)
    assert result.present
    assert not has_room


def test_the_room_needed_grows_with_what_the_alignment_left_uncovered():
    """If the alignment stops 10 bases short of the reference's end, the primer site
    is 10 bases further out than the alignment's edge suggests.
    """
    clipped = INTERIOR[:-10]  # the record holds all but the last 10 reference bases
    _, has_room = judge(GENOME_L + clipped + "T" * 25, [REF], 0.7, 0.8)
    assert not has_room  # 25 bases follow, 10 of them are where the reference would be: 15 < 20
    _, has_room = judge(GENOME_L + clipped + "T" * 35, [REF], 0.7, 0.8)
    assert has_room


# --- the stage, end to end ---------------------------------------------------------------

HEADER = ["assay_id", "record_id", "call", "exclusion"]
TAXID, OTHER = 10493, 100217


def _run(tmp_path, monkeypatch):
    """One assay, an archive of four records, and the calls the screen made on them."""
    records = {
        "DETECTED.1": GENOME_L + INTERIOR + GENOME_R,  # scored by the screen: never checked
        "DIVERGED.1": GENOME_L
        + substitute(INTERIOR, 0.2, seed=4)
        + GENOME_R,  # locus there, primers found nothing
        "OTHERGENE.1": dna(900, seed=5),  # a fragment of something else
        "CUTSHORT.1": GENOME_L + INTERIOR + "ACGT",  # locus there, record ends before the primer site
    }
    archive = tmp_path / "retrieved" / str(TAXID) / "all"
    archive.mkdir(parents=True)
    with gzip.open(archive / "2026-11-01.fasta.gz", "wt") as fh:
        for rid, seq in records.items():
            fh.write(f">{rid} some title\n{seq}\n")
    with gzip.open(archive / "2026-11-01.meta.tsv.gz", "wt") as fh:
        fh.write("accession\tcreated\ttaxid\n")
        fh.write(f"DETECTED\t2020-01-01\t{TAXID}\nDIVERGED\t2020-01-01\t{OTHER}\n")
        fh.write(f"OTHERGENE\t2020-01-01\t{OTHER}\nCUTSHORT\t2020-01-01\t{OTHER}\n")
    calls = tmp_path / "calls.tsv.gz"
    rows = [
        ["A", "DETECTED.1", "detect", ""],
        ["A", "DIVERGED.1", "no_amplicon", "no_site"],
        ["A", "OTHERGENE.1", "no_amplicon", "no_site"],
        ["A", "CUTSHORT.1", "no_amplicon", "no_site"],
        ["NOREF", "DIVERGED.1", "no_amplicon", "no_site"],  # an assay with no reference amplicon
    ]
    with gzip.open(calls, "wt", newline="") as fh:
        csv.writer(fh, delimiter="\t", lineterminator="\n").writerows([HEADER, *rows])
    references = tmp_path / "references.json"
    references.write_text(json.dumps({"A": {"from": ["DETECTED"], "interiors": [INTERIOR]}}))

    def assay(aid):
        return SimpleNamespace(
            id=aid,
            target=SimpleNamespace(taxid=TAXID, query=None, scope_taxids=None),
            source=SimpleNamespace(nested_round=None, nested_parent=None, nested_family=None),
        )

    registry = {"A": assay("A"), "NOREF": assay("NOREF")}
    taxonomy = SimpleNamespace(
        species_of=lambda t: t,
        within=lambda t, scope: t in scope,
        canonical=lambda t: t,
        name={TAXID: "Frog virus 3", OTHER: "Epizootic haematopoietic necrosis virus"},
    )
    for module in (locus, coverage):
        monkeypatch.setattr(module, "load_registry", lambda path: registry)
    monkeypatch.setattr(coverage, "taxonomy_from_config", lambda cfg: taxonomy)
    return calls, tmp_path / "retrieved", references


def _stage(tmp_path, calls, retrieved, references):
    out = tmp_path / "locus.tsv.gz"
    args = [str(calls), "--retrieved", str(retrieved), "--references", str(references), "--out", str(out)]
    assert locus.main(args) == 0
    with gzip.open(out, "rt", newline="") as fh:
        return out, {(r["assay_id"], r["record_id"]): r for r in csv.DictReader(fh, delimiter="\t")}


def test_the_stage_checks_the_unjudged_records_and_writes_what_it_found(tmp_path, monkeypatch):
    out, got = _stage(tmp_path, *_run(tmp_path, monkeypatch))

    assert set(got) == {("A", "DIVERGED.1"), ("A", "OTHERGENE.1"), ("A", "CUTSHORT.1")}
    diverged = got[("A", "DIVERGED.1")]
    assert (diverged["present"], diverged["has_room"]) == ("1", "1")
    assert 0.75 <= float(diverged["identity"]) <= 0.90
    assert got[("A", "OTHERGENE.1")]["present"] == "0"
    assert (got[("A", "CUTSHORT.1")]["present"], got[("A", "CUTSHORT.1")]["has_room"]) == ("1", "0")

    # what coverage reads: locus present AND room for the primers -> True, anything else False
    assert read_locus(out) == {"A": {"DIVERGED.1": True, "OTHERGENE.1": False, "CUTSHORT.1": False}}


def test_an_assay_with_no_reference_amplicon_is_left_alone(tmp_path, monkeypatch):
    """Nothing defines its locus, so its records stay unjudged instead of being guessed at."""
    _, got = _stage(tmp_path, *_run(tmp_path, monkeypatch))
    assert not any(assay == "NOREF" for assay, _ in got)


def test_a_reference_too_short_to_mean_anything_is_not_used(tmp_path):
    """A 17-base interior (a 57 bp amplicon, trimmed) matches by chance almost anywhere."""
    path = tmp_path / "references.json"
    path.write_text(
        json.dumps({"SHORT": {"interiors": ["ACGTACGTACGTACGTA"]}, "A": {"interiors": [INTERIOR, "ACGT"]}})
    )
    assert locus.read_references(path, min_bp=100) == {"SHORT": [], "A": [REF]}


def test_the_stage_can_be_limited_to_named_assays(tmp_path, monkeypatch):
    calls, retrieved, references = _run(tmp_path, monkeypatch)
    out = tmp_path / "locus.tsv.gz"
    base = [str(calls), "--retrieved", str(retrieved), "--references", str(references), "--out", str(out)]
    assert locus.main([*base, "--only", "NOREF"]) == 0
    assert read_locus(out) == {}


def test_coverage_turns_a_blank_into_a_failure_when_the_locus_is_shown_present(tmp_path, monkeypatch):
    """The point of the whole thing. Without the locus file the other species has no
    record shown to hold the locus: `not assessable`. With it, one record is shown to
    hold the locus with room for both primers and none was amplified: `predicted fail`,
    1 of the 3 records counted, the other-gene fragment and the cut-short deposit not.
    """
    calls, retrieved, references = _run(tmp_path, monkeypatch)
    side, _ = _stage(tmp_path, calls, retrieved, references)

    def cells(*extra):
        out = tmp_path / f"cov{len(extra)}"
        assert coverage.main([str(calls), "--retrieved", str(retrieved), "--out", str(out), *extra]) == 0
        with open(out / "coverage.tsv", newline="") as fh:
            return {(r["assay_id"], int(r["species_taxid"])): r for r in csv.DictReader(fh, delimiter="\t")}

    before, after = cells(), cells("--locus", str(side))
    assert before[("A", OTHER)]["state"] == "not assessable"
    assert after[("A", OTHER)]["state"] == "predicted fail"
    assert (after[("A", OTHER)]["detected"], after[("A", OTHER)]["locus_present"]) == ("0", "1")
    assert after[("A", TAXID)] == before[("A", TAXID)]  # a record the screen scored is never touched
