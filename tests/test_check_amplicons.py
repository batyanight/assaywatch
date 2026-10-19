"""The amplicon audit must see the assay the screener sees.

It read `oligos.forward` against `oligos.reverse` and nothing else, while
screening pools `oligos.alternates` in with them (`score.oligo_pools`) and takes
the best product over the cross product. The two were measuring different
assays, and the audit agreed with itself: three entries it called correct were
being scored by the pipeline on a different product entirely.
"""

import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_amplicons", ROOT / "scripts" / "check_amplicons.py")
check_amplicons = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_amplicons)

ANNIS = "CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004"
PREDICT_POOL = "Cryptosporidium_18SrDNA_Xiao_1999_round1"


def _doc(assay_id):
    return yaml.safe_load((ROOT / "registry" / f"{assay_id}.yaml").read_text())


def test_an_entry_with_no_alternates_has_exactly_the_declared_pair():
    pairs = check_amplicons.pairs_of(_doc(ANNIS))
    assert len(pairs) == 1
    label, fwd, rev = pairs[0]
    assert label == "declared"
    assert (fwd, rev) == (
        _doc(ANNIS)["oligos"]["forward"]["seq"],
        _doc(ANNIS)["oligos"]["reverse"]["seq"],
    )


def test_every_pool_combination_is_measured_declared_pair_first():
    """A 2x2 pool gives four combinations, the declared pair first.

    Built in the test rather than read from a registry entry: the entry this
    first used (the Cryptosporidium nested pair) was split into one entry per
    round on 2026-10-14, which is exactly the curation this script exists to
    prompt - a test that depends on an entry's alternates breaks when the
    curation it argues for happens.
    """
    doc = _doc(ANNIS)
    doc["oligos"]["alternates"] = [
        {"name": "alt-fwd", "seq": "GGAAGGGTTGTATTTATTAGATAAAG", "orientation": "forward"},
        {"name": "alt-rev", "seq": "AAGGAGTAAGGAACAACCTCCA", "orientation": "reverse"},
    ]
    pairs = check_amplicons.pairs_of(doc)
    assert len(pairs) == 4
    assert pairs[0] == (
        "declared",
        doc["oligos"]["forward"]["seq"],
        doc["oligos"]["reverse"]["seq"],
    )
    assert [p[0] for p in pairs[1:]] == ["fwd[0]xrev[1]", "fwd[1]xrev[0]", "fwd[1]xrev[1]"]
    assert ("fwd[1]xrev[1]", "GGAAGGGTTGTATTTATTAGATAAAG", "AAGGAGTAAGGAACAACCTCCA") in pairs


def test_a_split_nested_entry_no_longer_pools_its_rounds():
    """After the 2026-10-14 split, each Cryptosporidium round carries one pair.

    The point of the split: while both pairs sat in one entry, the secondary
    pair's 822 bp product was credited to an assay declaring 1319 bp.
    """
    base = "Cryptosporidium_18SrDNA_Xiao_1999"
    assert len(check_amplicons.pairs_of(_doc(f"{base}_round1"))) == 1
    assert len(check_amplicons.pairs_of(_doc(f"{base}_round2"))) == 1
    assert _doc(f"{base}_round1")["amplicon_bp"] == 1319
    assert _doc(f"{base}_round2")["amplicon_bp"] == 822


def test_sequences_come_from_the_schema_so_inosine_is_one_base_not_n():
    """`seq` writes inosine as N; the screener matches on `seq_as_written` via matching_seq.

    Reading `seq` here searched with a four-fold degenerate base where screening
    uses a single promiscuous one, so the audit's product counts were not the
    screener's on any inosine-containing assay.
    """
    inosine = [
        p
        for p in sorted((ROOT / "registry").glob("*.yaml"))
        if "I"
        in ((yaml.safe_load(p.read_text()).get("oligos") or {}).get("forward") or {}).get(
            "seq_as_written", ""
        )
    ]
    if not inosine:
        pytest.skip("no inosine-containing forward primer in the registry")
    doc = yaml.safe_load(inosine[0].read_text())
    label, fwd, _ = check_amplicons.pairs_of(doc)[0]
    assert fwd == doc["oligos"]["forward"]["seq_as_written"]
    assert fwd != doc["oligos"]["forward"]["seq"]


# --- the group is every archive, not the newest one -------------------------


def _archive(path: Path, records):
    import gzip

    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as fh:
        for rid, seq in records:
            fh.write(f">{rid}\n{seq}\n")


def test_every_archive_of_the_group_is_measured_oldest_first(tmp_path, monkeypatch):
    """Retrieval is incremental, so the newest file is not the group.

    Measuring only the newest archive had quietly emptied this script: by
    2026-10-14, 105 of its 155 measurements had moved or fallen to no product at
    all, because a small incremental archive had become the newest one.
    """
    monkeypatch.setattr(check_amplicons, "ROOT", tmp_path)
    base = tmp_path / "data" / "retrieved" / "42" / "all"
    for stem in ("2026-10-03", "2026-10-04", "2026-10-04_2", "2026-10-04_10"):
        _archive(base / f"{stem}.fasta.gz", [("AB1.1", "ACGT")])
    paths, group = check_amplicons.archives_for(42, None)
    assert group == "all"
    assert [p.name.split(".")[0] for p in paths] == [
        "2026-10-03",
        "2026-10-04",
        "2026-10-04_2",
        "2026-10-04_10",
    ], "_10 must sort after _2, as the pipeline's stem_order does"


def test_a_revised_accession_is_measured_once(tmp_path, monkeypatch):
    """The same accession in two archives is one record, the later version winning."""
    monkeypatch.setattr(check_amplicons, "ROOT", tmp_path)
    fwd, rev = "ACGTACGTACGTACGTAC", "TTGCATGCATGCATGCAT"
    from assaywatch.iupac import reverse_complement

    product = fwd + "A" * 80 + reverse_complement(rev)
    base = tmp_path / "data" / "retrieved" / "42" / "all"
    _archive(base / "2026-10-03.fasta.gz", [("AB1.1", product), ("AB2.1", product)])
    _archive(base / "2026-10-04.fasta.gz", [("AB1.2", product)])  # a revision of AB1
    paths, _ = check_amplicons.archives_for(42, None)
    n_records, n_products, lengths = check_amplicons.measure(paths, fwd, rev, 3, 4000, None)
    assert n_records == 2, "AB1 appears twice and is one record"
    assert n_products == 2
    assert lengths.most_common(1)[0][0] == len(product)
