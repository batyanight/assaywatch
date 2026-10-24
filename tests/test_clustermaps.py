"""The cluster resolver gets its map from the archives (clustermaps.py), 2026-10-24.

`subcluster.py` was built on 2026-10-19 with no consumer. These pin the wiring: with
no `cluster` chain nothing is read; with one, an assay's evaluable records are read
back from its own retrieval group, masked over the amplicon and clustered, and the
labels reach `resolve_sublineage` through `sublineage_resolvers`.
"""

from __future__ import annotations

import gzip
import random

import pytest

from assaywatch.accession import strip_version
from assaywatch.clustermaps import cluster_assays, cluster_maps, search_params
from assaywatch.iupac import reverse_complement
from assaywatch.lineage import resolve_sublineage, sublineage_resolvers
from assaywatch.schema import Assay
from assaywatch.score import load_config

CFG = load_config()

ASSAY = Assay.model_validate(
    {
        "id": "TEST_cluster",
        "name": "Test",
        "target": {"taxid": 109871, "gene": "ITS1", "genome_type": "dsDNA"},
        "chemistry": "conventional",
        "oligos": {
            "forward": {"name": "F", "seq": "CCTTGATATAATACAGTGTGCCATATGTC"},
            "reverse": {"name": "R", "seq": "AGCCAAGAGATCCGTTGTCAAA"},
        },
        "amplicon_bp": 146,
        "citation": {"doi": "10.3354/dao060141", "design_year": 2004, "doi_verified": True},
        "use_context": ["wildlife"],
        "status": "draft",
    }
)

LCFG = {
    "sublineage": {
        "TEST_cluster": {
            "chain": ["cluster"],
            "cluster": {"threshold": 0.05, "min_cluster_records": 5, "buffer_bp": 10},
        }
    }
}


def _lineage(rng: random.Random, n: int, prefix: str) -> list[tuple[str, str]]:
    """n records of one lineage: a shared random backbone carrying the amplicon, each
    copy with ~0.5% substitutions outside it."""
    fwd = ASSAY.oligos.forward.seq
    rev = ASSAY.oligos.reverse.seq
    body = "".join(rng.choice("ACGT") for _ in range(146 - len(fwd) - len(rev)))
    amplicon = fwd + body + reverse_complement(rev)
    left = "".join(rng.choice("ACGT") for _ in range(700))
    right = "".join(rng.choice("ACGT") for _ in range(700))
    backbone = left + amplicon + right
    out = []
    for i in range(n):
        s = list(backbone)
        for _ in range(7):
            j = rng.randrange(len(s))
            if j < len(left) or j >= len(left) + len(amplicon):
                s[j] = rng.choice([b for b in "ACGT" if b != s[j]])
        out.append((f"{prefix}{i:02d}.1", "".join(s)))
    return out


@pytest.fixture
def retrieved(tmp_path):
    rng = random.Random(11)
    group = tmp_path / "109871" / "all"
    group.mkdir(parents=True)
    recs = _lineage(rng, 8, "AAA") + _lineage(rng, 8, "BBB")
    with gzip.open(group / "2026-01-01.fasta.gz", "wt") as fh:
        for rid, seq in recs:
            fh.write(f">{rid} test\n{seq}\n")
    return tmp_path, recs


def test_no_cluster_chain_reads_nothing(tmp_path):
    assert cluster_assays({}) == {}
    assert cluster_assays({"sublineage": {"X": {"chain": ["subtaxid"]}}}) == {}
    # A retrieved dir that does not exist: proof nothing was opened.
    maps, infos = cluster_maps({}, {"TEST_cluster": ASSAY}, [], tmp_path / "nowhere", CFG)
    assert maps == {} and infos == {}


def test_search_params_take_the_widest_search_any_chemistry_uses():
    p = search_params(CFG)
    assert p["max_mm"] >= int(CFG["scoring"]["max_mismatches_searched"])
    assert p["lo_bp"] == CFG["amplicon"]["min_bp"] and p["hi_bp"] == CFG["amplicon"]["max_bp"]
    loose = {**CFG, "scoring": {**CFG["scoring"], "by_chemistry": {"sybr": {"max_pair_evalue": None}}}}
    assert search_params(loose)["max_e"] == float("inf")


def test_two_lineages_become_two_clusters_and_reach_the_resolver(retrieved):
    root, recs = retrieved
    calls = [{"assay_id": "TEST_cluster", "record_id": rid, "call": "detect"} for rid, _ in recs]
    maps, infos = cluster_maps(LCFG, {"TEST_cluster": ASSAY}, calls, root, CFG)
    labels = maps["TEST_cluster"]
    assert len(labels) == 16 and all("." not in k for k in labels), "keyed by unversioned accession"
    a = {labels[strip_version(rid)] for rid, _ in recs if rid.startswith("AAA")}
    b = {labels[strip_version(rid)] for rid, _ in recs if rid.startswith("BBB")}
    assert len(a) == 1 and len(b) == 1 and a != b
    assert {i.label for i in infos["TEST_cluster"]} == a | b
    chains = sublineage_resolvers(LCFG, {"TEST_cluster": 109871}, cluster_maps=maps)
    got = resolve_sublineage(calls[0], 109871, {}, chains["TEST_cluster"])
    assert got == labels[strip_version(calls[0]["record_id"])]
    # Unversioned ids resolve too, and a record the map never saw falls back to the taxid.
    assert resolve_sublineage({"record_id": "AAA00"}, 109871, {}, chains["TEST_cluster"]) == got
    assert resolve_sublineage({"record_id": "ZZZ99.1"}, 109871, {}, chains["TEST_cluster"]) != got


def test_only_evaluable_records_are_clustered(retrieved):
    root, recs = retrieved
    calls = [
        {"assay_id": "TEST_cluster", "record_id": rid, "call": "detect" if i % 2 else "no_amplicon"}
        for i, (rid, _) in enumerate(recs)
    ]
    maps, _ = cluster_maps(LCFG, {"TEST_cluster": ASSAY}, calls, root, CFG)
    assert set(maps["TEST_cluster"]) == {
        strip_version(c["record_id"]) for c in calls if c["call"] == "detect"
    }


def test_the_mask_covers_the_amplicon(retrieved):
    """Decision A: the span handed to the clusterer is the amplicon the screener would
    build, so the binding sites cannot define the lineage."""
    from assaywatch.loci import pair_spans

    _, recs = retrieved
    seq = recs[0][1]
    spans = pair_spans(
        seq,
        [(ASSAY.oligos.forward.matching_seq, ASSAY.oligos.reverse.matching_seq)],
        CFG,
        **search_params(CFG),
    )
    assert len(spans) == 1
    lo, hi = spans[0]
    assert ASSAY.oligos.forward.seq in seq[lo:hi]
    assert reverse_complement(ASSAY.oligos.reverse.seq) in seq[lo:hi]


def test_a_window_archive_is_skipped_with_a_warning(retrieved):
    root, recs = retrieved
    (root / "109871" / "all" / "2026-01-01.windows.tsv.gz").write_bytes(b"")
    calls = [{"assay_id": "TEST_cluster", "record_id": rid, "call": "detect"} for rid, _ in recs]
    with pytest.warns(UserWarning, match="window archive"):
        maps, _ = cluster_maps(LCFG, {"TEST_cluster": ASSAY}, calls, root, CFG)
    assert maps["TEST_cluster"] == {}
