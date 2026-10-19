"""Tests for assaywatch.subcluster (Mode C sequence clustering).

Synthetic sequences only -- validation against the real Bd archives (JEL423/
JAM81 must co-cluster; BdCAPE vs BdGPL seeds must separate) happens when the
pipeline can read data/, per docs/2026-10-19-subtaxid-resolution.md decision 3.
These tests pin the mechanism: masking, strand-invariance, the distance
estimator at both extremes, correct grouping/labelling, and determinism.
"""

import random

import pytest

from assaywatch.subcluster import (
    ClusterInfo,
    canonical_kmers,
    cluster,
    cluster_from_config,
    jaccard,
    mash_distance,
    mask_regions,
    sketch,
)


def _revcomp(s: str) -> str:
    return s.translate(str.maketrans("ACGT", "TGCA"))[::-1]


def _rand_seq(n: int, rng: random.Random) -> str:
    return "".join(rng.choice("ACGT") for _ in range(n))


def _mutate(seq: str, rate: float, rng: random.Random) -> str:
    out = list(seq)
    for i in range(len(out)):
        if rng.random() < rate:
            out[i] = rng.choice([b for b in "ACGT" if b != out[i]])
    return "".join(out)


# --- masking ------------------------------------------------------------


def test_mask_regions_blanks_span_plus_buffer_and_clamps():
    seq = "AAAACCCCGGGGTTTT"  # len 16
    # Mask [4,8) with buffer 2 -> [2,10); clamp is a no-op here.
    masked = mask_regions(seq, [(4, 8)], buffer_bp=2)
    assert masked == "AA" + "N" * 8 + "GGTTTT"
    assert len(masked) == len(seq)
    # Buffer running past the ends is clamped, not an error.
    assert mask_regions(seq, [(0, 2)], buffer_bp=100) == "N" * 16
    # No spans -> unchanged.
    assert mask_regions(seq, []) == seq


def test_canonical_kmers_skip_N_and_are_strand_invariant():
    seq = "ACGTACGT"
    km = canonical_kmers(seq, 4)
    # A sequence and its reverse complement share every canonical k-mer.
    assert canonical_kmers(_revcomp(seq), 4) == km
    # An N-masked region contributes no k-mers overlapping the N.
    assert canonical_kmers("ACGTNACGT", 4) == canonical_kmers("ACGT", 4) | canonical_kmers("ACGT", 4)


# --- distance estimator ------------------------------------------------


def test_identical_sequences_distance_zero():
    rng = random.Random(1)
    s = _rand_seq(500, rng)
    a = sketch(s, k=11, sketch_size=200)
    assert jaccard(a, a, 200) == 1.0
    assert mash_distance(1.0, 11) == 0.0


def test_disjoint_sequences_distance_one():
    rng = random.Random(2)
    a = sketch(_rand_seq(500, rng), k=11, sketch_size=200)
    b = sketch(_rand_seq(500, rng), k=11, sketch_size=200)
    j = jaccard(a, b, 200)
    assert j < 0.05  # essentially no shared 11-mers between random 500bp seqs
    assert mash_distance(j, 11) > 0.3


def test_small_mutation_small_distance():
    rng = random.Random(3)
    base = _rand_seq(1000, rng)
    near = _mutate(base, 0.01, rng)  # ~1% divergence
    far = _mutate(base, 0.20, rng)  # ~20% divergence
    d_near = mash_distance(jaccard(sketch(base, 15, 400), sketch(near, 15, 400), 400), 15)
    d_far = mash_distance(jaccard(sketch(base, 15, 400), sketch(far, 15, 400), 400), 15)
    assert d_near < d_far
    assert d_near < 0.05


# --- clustering ---------------------------------------------------------


def _two_lineage_corpus(rng):
    """Two tight lineages (A: 30 records, B: 25) + 2 lone outliers."""
    anc_a = _rand_seq(1500, rng)
    anc_b = _rand_seq(1500, rng)
    records = []
    for i in range(30):
        records.append((f"A{i:03d}.1", _mutate(anc_a, 0.01, rng)))
    for i in range(25):
        records.append((f"B{i:03d}.1", _mutate(anc_b, 0.01, rng)))
    # Two unrelated singletons -> below floor -> unresolved.
    records.append(("Z001.1", _rand_seq(1500, rng)))
    records.append(("Z002.1", _rand_seq(1500, rng)))
    return records


def test_cluster_splits_two_lineages_and_labels_by_size():
    rng = random.Random(10)
    records = _two_lineage_corpus(rng)
    labels, infos = cluster(records, k=15, sketch_size=400, threshold=0.05, min_cluster_records=20)

    # The 30-record lineage is cluster-01, the 25-record one cluster-02.
    a_labels = {labels[f"A{i:03d}.1"] for i in range(30)}
    b_labels = {labels[f"B{i:03d}.1"] for i in range(25)}
    assert a_labels == {"cluster-01"}
    assert b_labels == {"cluster-02"}
    # The two singletons fall into the unresolved bucket, not a clade.
    assert labels["Z001.1"] == "unresolved"
    assert labels["Z002.1"] == "unresolved"

    by_label = {ci.label: ci for ci in infos}
    assert by_label["cluster-01"].n_records == 30
    assert by_label["cluster-02"].n_records == 25
    assert by_label["unresolved"].n_records == 2
    # Representative is the smallest accession in the cluster (stable, BLAST-able).
    assert by_label["cluster-01"].representative == "A000"
    assert isinstance(by_label["cluster-01"], ClusterInfo)


def test_cluster_is_deterministic_under_input_reordering():
    rng = random.Random(10)
    records = _two_lineage_corpus(rng)
    labels1, _ = cluster(records, k=15, sketch_size=400, threshold=0.05, min_cluster_records=20)

    shuffled = records[:]
    random.Random(99).shuffle(shuffled)
    labels2, _ = cluster(shuffled, k=15, sketch_size=400, threshold=0.05, min_cluster_records=20)

    # Same record -> same label regardless of the order it was fed in.
    assert labels1 == labels2


def test_cluster_empty_input():
    assert cluster([], k=15, sketch_size=400) == ({}, [])


def test_masked_footprint_does_not_drive_clustering():
    """Two records identical only inside the (masked) footprint, divergent
    outside, must NOT cluster -- the whole point of masking."""
    rng = random.Random(42)
    shared_site = _rand_seq(60, rng)
    rec1 = shared_site + _rand_seq(800, rng)
    rec2 = shared_site + _rand_seq(800, rng)
    span = [(0, 60)]
    m1 = mask_regions(rec1, span, buffer_bp=0)
    m2 = mask_regions(rec2, span, buffer_bp=0)
    labels, _ = cluster(
        [("R1.1", m1), ("R2.1", m2)], k=15, sketch_size=400, threshold=0.05, min_cluster_records=1
    )
    # With the shared site masked out, only the divergent flanks remain -> two
    # separate clusters, not one.
    assert labels["R1.1"] != labels["R2.1"]


# --- config seam (decision A) ------------------------------------------


def test_cluster_from_config_masks_amplicon_and_clusters():
    """Decision A: caller passes whole-amplicon spans; the shared (masked)
    amplicon must not fuse two records whose flanks diverge."""
    rng = random.Random(7)
    shared_amplicon = _rand_seq(120, rng)  # the 'pair_spans' region, masked away
    # Two records sharing the amplicon but with unrelated flanks either side.
    rec1 = _rand_seq(400, rng) + shared_amplicon + _rand_seq(400, rng)
    rec2 = _rand_seq(400, rng) + shared_amplicon + _rand_seq(400, rng)
    spans = [(400, 520)]  # where the amplicon sits in both
    cfg = {
        "buffer_bp": 10,
        "kmer": 15,
        "sketch_size": 400,
        "threshold": 0.05,
        "min_cluster_records": 1,
        "method": "mash",
    }
    labels, _ = cluster_from_config([("R1.1", rec1, spans), ("R2.1", rec2, spans)], cfg)
    assert labels["R1.1"] != labels["R2.1"]


def test_cluster_from_config_rejects_unknown_method():
    with pytest.raises(ValueError):
        cluster_from_config([], {"method": "blast"})
