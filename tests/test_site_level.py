"""`scripts/measure_site_level.py` locates a probe site without its amplicon.

Phase 1 of the Bd-miss plan measures how much evidence the amplicon-level rule
discards. The only real logic in it is the offset method: place the probe by its
measured distance from whichever primer IS credible, because a truncated deposit has
no second primer to anchor on. That is the step `docs/2026-10-23-wave3-bd-miss.md`
names as the first open design question, so it is the step worth pinning.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from assaywatch.score import load_config

REPO = Path(__file__).resolve().parents[1]
CFG = load_config()

spec = importlib.util.spec_from_file_location(
    "measure_site_level", REPO / "scripts" / "measure_site_level.py"
)
msl = importlib.util.module_from_spec(spec)
sys.modules["measure_site_level"] = msl
spec.loader.exec_module(msl)


class _Oligo:
    def __init__(self, seq):
        self.matching_seq = seq


class _Oligos:
    def __init__(self, f, r, p):
        self.forward, self.reverse, self.probe = _Oligo(f), _Oligo(r), _Oligo(p)


class _Target:
    def __init__(self, taxid, query=None):
        self.taxid, self.query = taxid, query


class _Assay:
    def __init__(self, f, r, p, taxid=1, query=None):
        self.oligos = _Oligos(f, r, p)
        self.target = _Target(taxid, query)
        self.id = "TEST"


FWD = "GACTTGGCCACTTATGACAA"
PROBE = "CCAAGTGTCAGATGC"
REV = "GTCTCTGGAGAAGAAGAATT"


def _record(before=40, mid=30, after=50):
    """A synthetic full amplicon: forward, probe, reverse-complement of the reverse."""
    from assaywatch.iupac import reverse_complement

    filler = "ACTGGTCA" * 20
    return (
        filler[:before] + FWD + filler[:mid] + PROBE + filler[:mid] + reverse_complement(REV) + filler[:after]
    )


def test_the_probe_offset_is_measured_from_the_assay_s_own_records():
    """The offset must come from the data, not from a hand-picked reference.

    The Bd investigation placed the probe using one reference record (MW147112.1),
    which is the one part of its method that nobody else could reproduce. Taking the
    modal offset over the assay's own detecting records makes it reproducible.
    """
    rec = _record()
    assay = _Assay(FWD, REV, PROBE)
    offsets = msl.probe_offsets(assay, {"R1": rec, "R2": rec}, CFG)
    assert offsets, "no record yielded an offset, so the method found nothing to anchor on"
    assert len(set(offsets)) == 1, "identical records must give identical offsets"
    # The probe sits upstream of the reverse site, so the offset is negative.
    assert offsets[0] < 0
    # And it reconstructs the probe's true position from the reverse site alone.
    from assaywatch.match import find_sites

    rev_site = next(s for s in find_sites(REV, rec, 0))
    probe_site = next(s for s in find_sites(PROBE, rec, 0))
    assert rev_site.start + offsets[0] == probe_site.start


def test_an_assay_whose_records_never_hold_all_three_sites_yields_no_offset():
    """Then the assay is skipped and said so, rather than anchored on a guess."""
    truncated = _record()[60:]  # starts after the forward primer
    assay = _Assay(FWD, REV, PROBE)
    assert msl.probe_offsets(assay, {"R1": truncated}, CFG) == []


def test_only_the_exclusion_classes_that_carry_a_credible_site_are_counted():
    """`no_site` is unreachable and must not be counted as discarded evidence.

    `score.classify_exclusion` defines the classes: `no_site` means nothing credible
    matched for either primer, so site-level evaluation has nothing to anchor on,
    while `truncated`, `diverged` and `no_pair` each have at least one credible primer
    site. Counting `no_site` would inflate the reachable population roughly fivefold -
    it is 1,442,931 of the 1,789,100 `no_amplicon` rows.
    """
    assert set(msl.REACHABLE) == {"truncated", "diverged", "no_pair"}
    assert "no_site" not in msl.REACHABLE
    assert "chance_only" not in msl.REACHABLE


def test_the_archive_path_follows_the_retrieval_group_slug():
    """A wrong slug reads an empty directory and reports zero discarded evidence."""
    from assaywatch.groups import group_slug

    assay = _Assay(FWD, REV, PROBE, taxid=109871, query="internal transcribed spacer")
    paths = msl.archives_for(assay, REPO / "data" / "retrieved")
    expected = REPO / "data" / "retrieved" / "109871" / group_slug(assay.target.query)
    assert all(p.parent == expected for p in paths)


def test_the_offset_is_sampled_strided_and_not_from_the_head_of_the_archive():
    """Archives are accession-ordered, so their head is never representative.

    This is not a refinement. Sampling the first 200 records made `probe_offsets`
    return nothing for the twelve assays with the LARGEST discarded populations - the
    influenza Matrix gene's 93,966 rows among them - so the measurement silently
    excluded the cases that mattered most while reporting "no record holds all three
    sites" about archives holding thousands of them. The registry's own LEPTOSPIRA
    entry note records paying for the same mistake.

    Built as a positive control: every full amplicon sits beyond the sampling limit,
    so only a strided pass can reach one.
    """
    full = _record()
    truncated = _record()[60:]
    seqs = {f"T{i}": truncated for i in range(600)}
    seqs["FULL"] = full  # last, i.e. far past a head-only limit of 200
    assay = _Assay(FWD, REV, PROBE)
    assert msl.probe_offsets(assay, seqs, CFG, limit=200), (
        "a head-only sample misses the one informative record and reports the assay unmeasurable"
    )
