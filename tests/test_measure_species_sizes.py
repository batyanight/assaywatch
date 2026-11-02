"""Tests for scripts/measure_species_sizes.py.

The script had none; added 2026-10-21 with the `amplicon_bp_range` suggestion,
whose rule is a maintainer decision and so has to be pinned: the range is the
ENVELOPE of every kept band — the lowest low and the highest high, each end
taken separately — plus a fixed cushion on each end for an indel in a strain not
yet deposited. The measured value is what the registry takes (config.yaml
`amplicon:`); `declared_tolerance` adds its margin on top at screen time.
"""

from __future__ import annotations

import importlib.util
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location("mss", ROOT / "scripts" / "measure_species_sizes.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mss = _load()


def test_the_range_is_the_envelope_of_both_species_each_end_separately():
    """The maintainer's example: A 300-450, B 350-500 -> 300-500, then cushion."""
    assert mss.suggested_range([(300, 450), (350, 500)], cushion=0) == (300, 500)
    assert mss.suggested_range([(300, 450), (350, 500)], cushion=10) == (290, 510)


def test_a_species_wholly_inside_another_does_not_narrow_the_range():
    """The widest low and widest high win even when they come from different bands."""
    # B (350-500) is not contained, but C (380-420) is inside A entirely.
    assert mss.suggested_range([(300, 450), (350, 500), (380, 420)], cushion=0) == (300, 500)


def test_the_outermost_ends_can_come_from_different_bands():
    """Lowest low from one species, highest high from another — not one band's span."""
    assert mss.suggested_range([(540, 1545), (1067, 1067), (879, 879), (1505, 1673)], cushion=10) == (
        530,
        1683,
    )


def test_the_cushion_is_added_to_each_end_not_the_centre():
    lo, hi = mss.suggested_range([(1000, 1000)], cushion=25)
    assert (lo, hi) == (975, 1025)


def test_the_range_is_clamped_to_the_schema_bounds():
    """A cushion must never push the range outside what amplicon_range_is_sane accepts."""
    lo, hi = mss.suggested_range([(60, 2990)], cushion=100)
    assert lo == mss.AMPLICON_MIN  # 60 - 100 would be -40
    assert hi == mss.AMPLICON_MAX  # 2990 + 100 would be 3090
    assert lo >= mss.AMPLICON_MIN and hi <= mss.AMPLICON_MAX


def test_a_single_band_still_yields_a_range():
    assert mss.suggested_range([(146, 151)], cushion=10) == (136, 161)


# --- clusters: the per-species banding the envelope is built on, also untested ---


def test_clusters_splits_on_a_gap_bigger_than_the_threshold():
    """Two lengths 20 bp apart with gap 12 are two bands; 10 bp apart are one."""
    far = mss.clusters(Counter({100: 5, 120: 5}), gap=12, min_records=1, min_share=0.0)
    assert [(lo, hi) for lo, hi, _, _ in far] == [(100, 100), (120, 120)]
    near = mss.clusters(Counter({100: 5, 110: 5}), gap=12, min_records=1, min_share=0.0)
    assert [(lo, hi) for lo, hi, _, _ in near] == [(100, 110)]


def test_clusters_drops_a_length_below_either_floor():
    """A one-off length in a well-sequenced species is trimmed by min_share."""
    sizes = Counter({200: 98, 1000: 1, 201: 1})  # 1000 is 1% of 100
    cs = mss.clusters(sizes, gap=12, min_records=1, min_share=0.02)
    lengths = sorted(bp for _, _, _, g in cs for bp in g)
    assert 1000 not in lengths  # below 2%
    assert 200 in lengths


def test_clusters_biggest_band_first():
    cs = mss.clusters(Counter({100: 2, 500: 50}), gap=12, min_records=1, min_share=0.0)
    assert cs[0][0] == 500  # the 50-record band leads
