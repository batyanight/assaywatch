"""Tests for assaywatch.subcluster (Mode C sequence clustering).

Synthetic sequences only -- validation against the real Bd archives (JEL423/
JAM81 must co-cluster; BdCAPE vs BdGPL seeds must separate) happens when the
pipeline can read data/, per docs/journal/2026-10-19-subtaxid-resolution.md decision 3.
These tests pin the mechanism: masking, strand-invariance, the distance
estimator at both extremes, correct grouping/labelling, and determinism.
"""

import random

import pytest

from assaywatch.subcluster import (
    OTHER,
    UNPLACED,
    ClusterInfo,
    assign_nearest,
    canonical_kmers,
    cluster,
    cluster_from_config,
    components_at,
    flanked_region,
    jaccard,
    jaccard_matrix,
    kmer_matrix,
    mash_distance,
    mash_distances,
    mask_regions,
    mst_weights,
    sketch,
    widest_gap_cut,
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


# ---- flanked_region: the window composition clusters (ROADMAP step 1) ----
#
# A 30-bp record with an amplicon at [10, 20) is the shape every case below varies.
_REC = "AAAAACCCCCGGGGGTTTTTACGTACGTAC"


def _fr(seq=_REC, amplicon=(10, 20), sites=(), *, flank_bp=5, mask_buffer_bp=0, stop_n_run=10):
    return flanked_region(
        "rec1.1",
        seq,
        amplicon,
        list(sites),
        flank_bp=flank_bp,
        mask_buffer_bp=mask_buffer_bp,
        stop_n_run=stop_n_run,
    )


def test_a_window_is_the_amplicon_plus_both_flanks():
    r = _fr()
    assert r.seq == _REC[5:25]
    assert (r.left_bp, r.right_bp, r.full_flank) == (5, 5, True)
    assert r.record_id == "rec1.1"


def test_a_flank_stops_at_the_end_of_the_record_and_says_so():
    """Assembly cuts carry 100 bp and window archives 300, so a short flank is the
    normal case for them; the flank used is recorded, never padded."""
    r = _fr(amplicon=(2, 10))
    assert r.seq == _REC[0:15]
    assert (r.left_bp, r.right_bp, r.full_flank) == (2, 5, False)
    r = _fr(amplicon=(20, 28))
    assert (r.left_bp, r.right_bp, r.full_flank) == (5, 2, False)


def test_a_run_of_n_ends_a_flank_but_a_short_one_does_not():
    """Scaffolds join contigs with N spacers; sequence beyond one is not adjacent to
    the amplicon. A few N inside real sequence are ambiguity, not a spacer."""
    spacer = "ACGTACGT" + "N" * 10 + "ACGTA" + "CCCCCGGGGG" + "ACGTACGTAC"
    r = _fr(spacer, amplicon=(23, 33), flank_bp=20)
    assert r.left_bp == 5  # stops just after the 10-N run, which is not included
    assert r.seq.startswith("ACGTA")
    short = "ACGTACGTACGT" + "NNN" + "ACGTACCCCCGGGGG" + "ACGTACGTAC"
    r = _fr(short, amplicon=(25, 35), flank_bp=20)
    assert r.left_bp == 20 and "NNN" in r.seq


def test_sites_are_masked_in_window_coordinates_with_their_buffer():
    """Sites arrive in RECORD coordinates and the window starts at the left flank,
    so the mask must shift; the buffer widens each site but never leaves the window."""
    r = _fr(sites=[(10, 13), (17, 20)], mask_buffer_bp=1)
    # window = _REC[5:25] = CCCCC|GGGGGTTTTT|ACGTA; buffered sites [9,14) and [16,21)
    # land at window [4,9) and [11,16)
    assert r.seq == "CCCC" + "NNNNN" + "GT" + "NNNNN" + "CGTA"
    edge = _fr(amplicon=(0, 10), sites=[(0, 3)], mask_buffer_bp=4)
    assert edge.seq.startswith("NNNNNNN") and len(edge.seq) == 15


def test_a_window_is_upper_case_whatever_the_archive_wrote():
    assert _fr(_REC.lower()).seq == _REC[5:25]


@pytest.mark.parametrize("amplicon", [(10, 10), (12, 8), (-1, 5), (25, 31)])
def test_an_amplicon_outside_the_record_is_refused(amplicon):
    with pytest.raises(ValueError, match="amplicon"):
        _fr(amplicon=amplicon)


def test_a_flank_never_ends_in_n():
    """N at a flank's OUTER end -- cut off by the flank limit or the record's end --
    are dropped: a flank padded with ambiguity would read as longer than the sequence
    it holds. N between real flank bases and the amplicon are interior and kept."""
    rec = "NNACG" + "CCCCCGGGGG" + "TTNNN"
    r = _fr(rec, amplicon=(5, 15), flank_bp=5)
    assert (r.left_bp, r.right_bp) == (3, 2)
    assert r.seq == "ACG" + "CCCCCGGGGG" + "TT"
    interior = _fr("ACGNN" + "CCCCCGGGGG" + "TTTTT", amplicon=(5, 15), flank_bp=5)
    assert interior.left_bp == 5 and interior.seq.startswith("ACGNN")


# ---- kmer_matrix / jaccard_matrix / mash_distances: exact and vectorised (step 2) ----
#
# Finding 5: pure-Python sketch comparison costs ~6.5 ms a pair. A composition
# window has far fewer k-mers than `sketch_size`, and below that size the bottom-k
# estimate IS the exact Jaccard index, so an exact sparse-matrix computation gives
# the same number in a fraction of the time. These pin that equality.


def _windows(n=12, length=300, seed=7):
    rng = random.Random(seed)
    base = _rand_seq(length, rng)
    out = []
    for i in range(n):
        s = list(base)
        for _ in range(i * 3):  # increasing divergence from the base
            j = rng.randrange(length)
            s[j] = rng.choice("ACGT")
        out.append("".join(s))
    return out


def test_each_row_holds_exactly_that_window_s_canonical_kmers():
    seqs = _windows()
    m = kmer_matrix(seqs, 15)
    assert m.shape[0] == len(seqs)
    for i, s in enumerate(seqs):
        assert m[i].nnz == len(canonical_kmers(s, 15))


def test_a_window_and_its_reverse_complement_are_one_row():
    s = _windows(1)[0]
    m = kmer_matrix([s, _revcomp(s)], 15)
    assert (m[0] != m[1]).nnz == 0


def test_jaccard_matrix_is_the_exact_set_jaccard():
    seqs = _windows()
    j = jaccard_matrix(kmer_matrix(seqs, 15))
    for a in range(len(seqs)):
        for b in range(len(seqs)):
            ka, kb = canonical_kmers(seqs[a], 15), canonical_kmers(seqs[b], 15)
            assert j[a, b] == pytest.approx(len(ka & kb) / len(ka | kb))


def test_below_sketch_size_it_equals_the_sketch_estimate():
    """The equality finding 5 rests on: with fewer k-mers than `sketch_size`, the
    existing bottom-k `jaccard` and the exact matrix agree to the last digit."""
    seqs, k, size = _windows(), 15, 10_000
    j = jaccard_matrix(kmer_matrix(seqs, k))
    sk = [sketch(s, k, size) for s in seqs]
    for a in range(len(seqs)):
        for b in range(len(seqs)):
            assert j[a, b] == pytest.approx(jaccard(sk[a], sk[b], size))


def test_two_sets_of_rows_compare_as_a_rectangle():
    seqs = _windows()
    m = kmer_matrix(seqs, 15)
    full = jaccard_matrix(m)
    rect = jaccard_matrix(m[:4], m[4:])
    assert rect.shape == (4, len(seqs) - 4)
    assert rect == pytest.approx(full[:4, 4:])


def test_an_all_n_window_shares_nothing_and_is_not_nan():
    m = kmer_matrix(["N" * 50, _windows(1)[0]], 15)
    j = jaccard_matrix(m)
    assert j[0, 0] == 0.0 and j[0, 1] == 0.0


def test_mash_distances_equal_mash_distance_entry_by_entry():
    import numpy as np

    js = np.array([[0.0, 1e-9, 0.1], [0.5, 0.9, 1.0]])
    d = mash_distances(js, 15)
    for (r, c), v in np.ndenumerate(js):
        assert d[r, c] == pytest.approx(mash_distance(float(v), 15))


# ---- widest_gap_cut: where one assay's lineages separate (step 4) ----
#
# Synthetic distance matrices, so each case states its own geometry.


def _clades(sizes, within, between):
    """Block distance matrix: `within` inside a clade, `between[i][j]` across."""
    import numpy as np

    n = sum(sizes)
    d = np.zeros((n, n))
    starts = [sum(sizes[:i]) for i in range(len(sizes))]
    for a, (sa, na) in enumerate(zip(starts, sizes, strict=True)):
        for b, (sb, nb) in enumerate(zip(starts, sizes, strict=True)):
            d[sa : sa + na, sb : sb + nb] = within if a == b else between[a][b]
    np.fill_diagonal(d, 0.0)
    return d


def test_mst_weights_are_the_single_linkage_merge_heights():
    d = _clades([3, 3], 0.004, [[0, 0.1], [0.1, 0]])
    w = sorted(mst_weights(d))
    assert len(w) == 5
    assert w == pytest.approx([0.004] * 4 + [0.1])


def test_a_zero_distance_is_still_an_edge():
    """Two different windows can share every k-mer (distance 0). scipy's MST reads 0
    as 'no edge' and would split them; this one must not."""
    d = _clades([2, 1], 0.0, [[0, 0.2], [0.2, 0]])
    assert sorted(mst_weights(d)) == pytest.approx([0.0, 0.2])


def test_two_clades_are_cut_at_the_middle_of_the_gap_between_them():
    d = _clades([4, 4], 0.004, [[0, 0.1], [0.1, 0]])
    cut = widest_gap_cut(d, lo=0.01, hi=0.15, min_gap=0.01)
    assert cut.reason == "widest gap"
    assert cut.value == pytest.approx((0.01 + 0.1) / 2)
    assert cut.gap == pytest.approx(0.09)


def test_a_gap_is_clipped_to_the_bounds_before_it_is_measured():
    """Clades 30% apart still separate (the gap is clipped at cut_max), and a
    sub-split at 0.8% is below cut_min and is not a lineage boundary."""
    far = _clades([3, 3], 0.004, [[0, 0.3], [0.3, 0]])
    cut = widest_gap_cut(far, lo=0.01, hi=0.15, min_gap=0.01)
    assert cut.value == pytest.approx(0.08)
    tiers = _clades([2, 2, 3], 0.002, [[0, 0.008, 0.2], [0.008, 0, 0.2], [0.2, 0.2, 0]])
    cut = widest_gap_cut(tiers, lo=0.01, hi=0.15, min_gap=0.01)
    assert cut.value == pytest.approx(0.08)


def test_the_space_above_the_largest_edge_is_not_a_gap():
    """Otherwise 'everything above 5%' outbids the real gap below it and two
    groups 5% apart would always merge."""
    d = _clades([3, 3], 0.002, [[0, 0.05], [0.05, 0]])
    cut = widest_gap_cut(d, lo=0.01, hi=0.15, min_gap=0.01)
    assert cut.value == pytest.approx((0.01 + 0.05) / 2)


def test_evenly_spread_distances_have_no_gap_and_make_one_cluster():
    import numpy as np

    pos = np.arange(0, 0.2, 0.005)  # points on a line: MST edges all 0.005
    d = np.abs(pos[:, None] - pos[None, :])
    cut = widest_gap_cut(d, lo=0.01, hi=0.15, min_gap=0.01)
    assert (cut.value, cut.reason) == (None, "no gap in bounds")


def test_everything_tighter_than_cut_min_is_one_cluster():
    d = _clades([5], 0.003, [[0]])
    cut = widest_gap_cut(d, lo=0.01, hi=0.15, min_gap=0.01)
    assert (cut.value, cut.reason) == (None, "no gap in bounds")


def test_one_window_is_too_few_to_cut():
    import numpy as np

    cut = widest_gap_cut(np.zeros((1, 1)), lo=0.01, hi=0.15, min_gap=0.01)
    assert (cut.value, cut.reason) == (None, "too few")


# ---- components_at / assign_nearest (step 5) ----


def _point_mutate(seq: str, n: int, rng: random.Random) -> str:
    s = list(seq)
    for _ in range(n):
        i = rng.randrange(len(s))
        s[i] = rng.choice([b for b in "ACGT" if b != s[i]])
    return "".join(s)


def _two_clade_windows(seed=21, length=1000, per=6):
    """Two clades ~10% apart, members within a clade ~0.3% apart."""
    rng = random.Random(seed)
    root = _rand_seq(length, rng)
    a, b = _point_mutate(root, 50, rng), _point_mutate(root, 50, rng)
    return [_point_mutate(a, 3, rng) for _ in range(per)] + [_point_mutate(b, 3, rng) for _ in range(per)]


def test_components_are_labelled_by_size_largest_first():
    d = _clades([2, 5, 3], 0.002, [[0, 0.1, 0.1], [0.1, 0, 0.1], [0.1, 0.1, 0]])
    labels = components_at(d, 0.05, min_size=1)
    assert labels == [2] * 2 + [0] * 5 + [1] * 3


def test_a_component_below_min_size_is_other():
    d = _clades([4, 1], 0.002, [[0, 0.1], [0.1, 0]])
    assert components_at(d, 0.05, min_size=3) == [0] * 4 + [OTHER]


def test_no_cut_is_one_cluster_and_a_tiny_sample_is_other():
    d = _clades([2, 2], 0.002, [[0, 0.1], [0.1, 0]])
    assert components_at(d, None, min_size=3) == [0] * 4
    assert components_at(d[:2, :2], None, min_size=3) == [OTHER] * 2


def test_equal_sizes_tie_to_the_earlier_sample():
    d = _clades([3, 3], 0.002, [[0, 0.1], [0.1, 0]])
    assert components_at(d, 0.05, min_size=1) == [0] * 3 + [1] * 3


def test_a_record_joins_the_clade_of_its_nearest_sampled_member():
    rng = random.Random(22)
    w = _two_clade_windows()
    ref, labels = w[:3] + w[6:9], [0, 0, 0, 1, 1, 1]
    queries = [_point_mutate(w[4], 2, rng), _point_mutate(w[10], 2, rng)]
    assert assign_nearest(queries, ref, labels, 15, 0.05) == [0, 1]


def test_a_record_beyond_the_cut_from_every_member_is_unplaced():
    rng = random.Random(23)
    w = _two_clade_windows()
    stranger = _rand_seq(1000, rng)
    assert assign_nearest([stranger], w[:6], [0] * 6, 15, 0.05) == [UNPLACED]


def test_a_short_flank_record_is_placed_by_containment():
    """A 300 bp piece of a clade-B window shares few k-mers with a 1,000 bp
    window as a SET (Jaccard ~0.3, distance far past the cut), but nearly all of its
    own k-mers are in it. Containment places it; Jaccard would leave it unplaced."""
    w = _two_clade_windows()
    piece = w[8][350:650]
    ref, labels = w[:3] + w[6:9], [0, 0, 0, 1, 1, 1]
    assert assign_nearest([piece], ref, labels, 15, 0.05) == [UNPLACED]
    assert assign_nearest([piece], ref, labels, 15, 0.05, containment_for={0}) == [1]
