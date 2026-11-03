"""Sequence-homology clustering for sub-taxid lineage resolution (Mode C).

Some biologically distinct lineages share one NCBI taxid and carry no
distinguishing label in their defline -- *Batrachochytrium dendrobatidis*
BdGPL vs BdCAPE is the motivating case (all taxid 109871, zero lineage tokens
in any title). The only remaining signal is sequence homology, so we cluster
the records and hand each cluster to the per-lineage machinery as its own
"lineage". See docs/journal/2026-10-19-subtaxid-resolution.md, decisions 2-4.

The one hard constraint (estimand plan): cluster on sequence **outside the
primer and probe footprints**. Cluster on the binding sites and the lineage is
defined by the very quantity the assay measures -- every assay would then show
a failing cluster by construction. So each record is masked over the regions
the caller passes (see ``mask_regions``) before it is sketched.

Method: bottom-k MinHash sketches and Mash distance, single-linkage. This is
the same estimator the Mash tool uses, implemented in pure Python + numpy so
the pipeline stays reproducible across machines (conda/renv) with no external
binary to install. The all-pairs step is quadratic, so feed it only an assay's
evaluable records; the scaling note in ``cluster`` has the measured cost.

Status (2026-10-26): WIRED. `assaywatch/clustermaps.py` consumed this module on
2026-10-24 and `report.py` builds its sublineage resolvers with those maps, so the
`cluster` chain is reachable from the report. It is still INERT in practice, for a
different reason than when this note first said "no consumer yet": `config.yaml`
ships `lineage.sublineage: {}`, so no assay declares a chain for it to resolve.

Bd, the motivating case, measured out as a denominator problem rather than a lineage
split (see the design doc, Mode C), and that has not changed: 174 of its 175 evaluable
records detect, so no partition respecting `min_records_per_lineage: 30` can fall below
90%, and its real failure sits in the 8,857 `no_site` records.

Everything here is deterministic: a fixed hash (blake2b), deterministic
bottom-k selection, union-find in input order, and a label assignment keyed on
(size, representative accession). The same archive yields the same cluster ids
on every run -- a property a test pins, because an unstable label would make
the drift report diff noisily from run to run.
"""

from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass

from assaywatch.accession import strip_version

_COMPLEMENT = str.maketrans("ACGT", "TGCA")


def mask_regions(seq: str, spans: list[tuple[int, int]], buffer_bp: int = 0) -> str:
    """Return *seq* with every ``(start, end)`` span (0-based half-open),
    extended by ``buffer_bp`` on each side, replaced by ``N``.

    Masking to ``N`` (rather than cutting the regions out and concatenating the
    remainder) matters: concatenation would fuse the two flanks into a junction
    that never existed and manufacture k-mers spanning it. ``N`` is simply
    skipped by ``canonical_kmers``, so the footprint contributes nothing and no
    artificial sequence is created.

    The caller decides what the spans are. Passing ``loci.pair_spans`` output
    masks the whole amplicon (primer-to-primer) and clusters on the outer
    flanks only; passing individual primer/probe site coordinates masks just
    the binding footprints and keeps the inter-primer body. Both are
    non-circular; the module does not assume which.
    """
    if not spans:
        return seq
    chars = list(seq)
    n = len(seq)
    for start, end in spans:
        lo = max(0, start - buffer_bp)
        hi = min(n, end + buffer_bp)
        for i in range(lo, hi):
            chars[i] = "N"
    return "".join(chars)


@dataclass(frozen=True)
class Region:
    """One record's window for composition clustering: flank + amplicon + flank,
    every primer/probe site (plus buffer) masked to ``N``.

    ``left_bp`` / ``right_bp`` are the flank actually used, which is less than asked
    where the record ends or an ``N`` spacer begins; ``full_flank`` says both sides
    reached the requested length. Short-flank windows are assigned by containment and
    never sampled (ROADMAP, "Lineage composition over time", finding 2), so the
    caller needs to know. No reverse complement: ``canonical_kmers`` already counts a
    k-mer and its reverse complement as one, so either strand's window compares.
    """

    record_id: str
    seq: str
    left_bp: int
    right_bp: int
    full_flank: bool


def _flank_extent(seq: str, edge: int, step: int, flank_bp: int, stop_n_run: int) -> int:
    """How many bases a flank keeps, walking outward from the amplicon boundary ``edge``
    (its start for the left flank, its exclusive end for the right) by ``step``
    (-1 left, +1 right), stopping at the record's end or before a run of
    ``stop_n_run`` N. A shorter run of N is ambiguity and is kept."""
    kept = 0
    run = 0
    i = edge - 1 if step < 0 else edge
    while kept + run < flank_bp and 0 <= i < len(seq):
        if seq[i] == "N":
            run += 1
            if run >= stop_n_run:
                return kept
        else:
            kept += run + 1
            run = 0
        i += step
    return kept


def flanked_region(
    record_id: str,
    seq: str,
    amplicon: tuple[int, int],
    sites: list[tuple[int, int]],
    *,
    flank_bp: int,
    mask_buffer_bp: int,
    stop_n_run: int,
) -> Region:
    """The window ``composition`` clusters, cut from one record.

    ``amplicon`` and ``sites`` are 0-based half-open spans in RECORD coordinates (the
    convention of ``match.pair_spans``); the sites are shifted into window
    coordinates before masking. Each flank extends up to ``flank_bp`` and stops at
    the record's end or just before a run of ``stop_n_run`` N, because an assembly
    spacer means the sequence beyond it is not adjacent to the amplicon. N of a
    shorter run at a flank's OUTER end are dropped, so a flank never ends in N there;
    N between flank bases and the amplicon are interior ambiguity and kept.
    """
    start, end = amplicon
    if not 0 <= start < end <= len(seq):
        raise ValueError(f"{record_id}: amplicon {amplicon} is not inside a {len(seq)} bp record")
    s = seq.upper()
    left = _flank_extent(s, start, -1, flank_bp, stop_n_run)
    right = _flank_extent(s, end, +1, flank_bp, stop_n_run)
    lo, hi = start - left, end + right
    window = mask_regions(s[lo:hi], [(a - lo, b - lo) for a, b in sites], mask_buffer_bp)
    return Region(record_id, window, left, right, left == flank_bp and right == flank_bp)


def canonical_kmers(seq: str, k: int) -> set[str]:
    """Canonical k-mers of *seq*: the lexicographically smaller of each k-mer
    and its reverse complement.

    Canonicalising collapses the two strands onto one representation, so a
    record and its reverse complement sketch identically -- GenBank deposits
    either strand and we do not want that to split a lineage. Any k-mer
    containing a non-ACGT character (``N`` from masking, or an ambiguity code)
    is skipped, which is how the masked footprint drops out.
    """
    seq = seq.upper()
    out: set[str] = set()
    for i in range(len(seq) - k + 1):
        kmer = seq[i : i + k]
        if not set(kmer) <= {"A", "C", "G", "T"}:
            continue
        rc = kmer.translate(_COMPLEMENT)[::-1]
        out.add(kmer if kmer <= rc else rc)
    return out


def _hash(kmer: str) -> int:
    """Deterministic 64-bit hash of a k-mer (no RNG, stable across runs)."""
    return int.from_bytes(hashlib.blake2b(kmer.encode(), digest_size=8).digest(), "big")


def sketch(seq: str, k: int, sketch_size: int) -> tuple[int, ...]:
    """Bottom-k MinHash sketch: the ``sketch_size`` smallest distinct k-mer
    hashes, sorted ascending.

    A set's bottom-s hashes are a uniform random sample of its k-mers (the hash
    randomises order), so two sets that share many k-mers share many of their
    smallest hashes. That is what lets ``jaccard`` estimate overlap from the
    tiny sketches instead of the full k-mer sets. A sequence with fewer than
    ``sketch_size`` distinct k-mers yields a shorter sketch, which the
    estimator handles.
    """
    hashes = sorted(_hash(km) for km in canonical_kmers(seq, k))
    return tuple(hashes[:sketch_size])


def jaccard(sketch_a: tuple[int, ...], sketch_b: tuple[int, ...], sketch_size: int) -> float:
    """Estimate the Jaccard index of two sketches (Mash bottom-sketch method).

    Merge the two bottom-s sketches, take the s smallest hashes of that union,
    and count how many of those lie in *both* sketches. That fraction estimates
    |A∩B| / |A∪B| -- because the bottom-s of the union is a uniform sample of
    A∪B, and a sampled hash is in both sketches exactly when its k-mer is in
    both sets.
    """
    if not sketch_a or not sketch_b:
        return 0.0
    set_a, set_b = set(sketch_a), set(sketch_b)
    merged = sorted(set_a | set_b)[:sketch_size]
    if not merged:
        return 0.0
    shared = sum(1 for h in merged if h in set_a and h in set_b)
    return shared / len(merged)


def mash_distance(j: float, k: int) -> float:
    """Mash distance from a Jaccard estimate: ``-ln(2j/(1+j)) / k``.

    This converts the shared-k-mer fraction into an estimate of the per-base
    mutation rate between the two sequences (derived under a Poisson model of
    independent substitutions), which is why it reads as a genetic distance and
    is comparable across records of different length. ``j = 0`` (no shared
    k-mers) maps to the maximum distance 1.0.
    """
    if j <= 0.0:
        return 1.0
    d = -math.log(2 * j / (1 + j)) / k
    return max(0.0, d)


class _DSU:
    """Union-find for single-linkage connected components."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[max(ra, rb)] = min(ra, rb)


@dataclass(frozen=True)
class ClusterInfo:
    """A named cluster, for the report a human reads."""

    label: str  # "cluster-01", or "unresolved" for the below-floor bucket
    n_records: int
    representative: str  # smallest accession in the cluster, for a curator to BLAST


def _base_accession(record_id: str) -> str:
    return strip_version(record_id)


def cluster(
    records: list[tuple[str, str]],
    *,
    k: int = 21,
    sketch_size: int = 10000,
    threshold: float = 0.05,
    min_cluster_records: int = 20,
) -> tuple[dict[str, str], list[ClusterInfo]]:
    """Single-linkage cluster already-masked records by Mash distance.

    Args:
        records: ``(record_id, masked_seq)`` pairs. Mask with ``mask_regions``
            before calling -- this function does not mask.
        k, sketch_size: MinHash parameters.
        threshold: records within this Mash distance are linked (single
            linkage; transitive).
        min_cluster_records: a connected component smaller than this is not a
            clade. Its records are labelled ``unresolved`` -- the estimand's
            junk-drawer convention (never judged as a lineage). The per-lineage
            floor downstream still applies on top of this.

    Returns:
        ``(labels, infos)`` where ``labels`` maps record_id -> cluster label
        and ``infos`` lists each named cluster (and the unresolved bucket if
        non-empty), ordered as the labels were assigned.

    Determinism: components are labelled ``cluster-NN`` by descending record
    count, ties broken by the smallest representative accession, so the mapping
    is identical on re-run and independent of input order.

    Scaling: the pairwise step is O(n^2 * sketch_size). Measured 2026-10-19,
    one ``jaccard`` call at sketch_size 10000 takes about 6.5 ms. That is about
    81 h for all 9,496 Bd records, and about 1.5 min for the 173 that are
    evaluable for the Boyle assay. Pass evaluable records only. Past a few
    thousand, replace the double loop with an LSH index over the sketches
    (banding) or shell out to ``mash dist``; the sketch/distance functions above
    are unchanged by that swap.
    """
    n = len(records)
    if n == 0:
        return {}, []

    sketches = [sketch(seq, k, sketch_size) for _, seq in records]

    dsu = _DSU(n)
    for i in range(n):
        for j_idx in range(i + 1, n):
            jac = jaccard(sketches[i], sketches[j_idx], sketch_size)
            if mash_distance(jac, k) <= threshold:
                dsu.union(i, j_idx)

    # Gather components -> member record indices.
    comps: dict[int, list[int]] = {}
    for idx in range(n):
        comps.setdefault(dsu.find(idx), []).append(idx)

    def representative(member_idxs: list[int]) -> str:
        return min(_base_accession(records[m][0]) for m in member_idxs)

    # Separate real clades from the below-floor bucket.
    clades = [m for m in comps.values() if len(m) >= min_cluster_records]
    below = [m for m in comps.values() if len(m) < min_cluster_records]

    # Deterministic order: larger first, then smaller representative accession.
    clades.sort(key=lambda m: (-len(m), representative(m)))

    labels: dict[str, str] = {}
    infos: list[ClusterInfo] = []
    for i, members in enumerate(clades, start=1):
        label = f"cluster-{i:02d}"
        for m in members:
            labels[records[m][0]] = label
        infos.append(ClusterInfo(label, len(members), representative(members)))

    below_members = [m for group in below for m in group]
    if below_members:
        for m in below_members:
            labels[records[m][0]] = "unresolved"
        infos.append(ClusterInfo("unresolved", len(below_members), representative(below_members)))

    return labels, infos


def cluster_from_config(
    records_with_spans: list[tuple[str, str, list[tuple[int, int]]]],
    cfg: dict,
) -> tuple[dict[str, str], list[ClusterInfo]]:
    """Mask and cluster from a ``cluster:`` config block (design decision A).

    This is the seam the pipeline wiring plugs into. The caller supplies, per
    record, ``(record_id, full_sequence, spans)`` where ``spans`` is the output
    of ``loci.pair_spans`` for this assay -- i.e. the whole amplicon span,
    primer to primer. Decision A masks that entire span (plus ``buffer_bp``),
    so clustering runs on the outer flanks only and cannot see the binding
    sites. The module stays agnostic about what the spans are; "A" lives in the
    caller's choice to pass ``pair_spans`` here.

    Config keys (with defaults): ``buffer_bp`` (0), ``kmer`` (21),
    ``sketch_size`` (10000), ``threshold`` (0.05), ``min_cluster_records``
    (20), ``method`` ("mash"). ``method`` is validated so a typo fails loudly
    rather than silently doing the wrong thing.
    """
    method = cfg.get("method", "mash")
    if method != "mash":
        raise ValueError(f"unsupported cluster method {method!r}; only 'mash' is implemented")
    buffer_bp = int(cfg.get("buffer_bp", 0))
    masked = [
        (record_id, mask_regions(seq, spans, buffer_bp)) for record_id, seq, spans in records_with_spans
    ]
    return cluster(
        masked,
        k=int(cfg.get("kmer", 21)),
        sketch_size=int(cfg.get("sketch_size", 10000)),
        threshold=float(cfg.get("threshold", 0.05)),
        min_cluster_records=int(cfg.get("min_cluster_records", 20)),
    )
