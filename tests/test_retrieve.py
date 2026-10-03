"""Retrieval tests. No network: the transport is a fake returning canned E-utilities XML.

What is worth testing here is not HTTP but the decisions: how the query is
built, when a run is incremental, what the cap does, and whether the archive
and manifest are reproducible.
"""

import gzip
import json

import pytest

from assaywatch.retrieve import (
    RecordMeta,
    TooManyRecords,
    build_query,
    esearch,
    group_slug,
    last_run_date,
    load_manifest,
    record_run,
    retrieve_taxon,
    targets_from_registry,
)

ESEARCH_XML = """<?xml version="1.0"?>
<eSearchResult><Count>{count}</Count><RetMax>0</RetMax>
<QueryKey>1</QueryKey><WebEnv>MCID_TEST</WebEnv></eSearchResult>"""

SUMMARY_DOC = """<DocSum><Id>{uid}</Id>
<Item Name="Caption" Type="String">{acc}</Item>
<Item Name="Title" Type="String">{title}</Item>
<Item Name="CreateDate" Type="Date">{created}</Item>
<Item Name="UpdateDate" Type="Date">{updated}</Item>
<Item Name="Length" Type="Integer">{length}</Item>
</DocSum>"""


class FakeNCBI:
    """Serves `n` records and records every call made against it."""

    def __init__(self, n: int, start_year: int = 2020):
        self.n = n
        self.start_year = start_year
        self.calls: list[tuple[str, dict]] = []

    def __call__(self, endpoint: str, params: dict) -> str:
        self.calls.append((endpoint, dict(params)))
        if endpoint == "esearch":
            return ESEARCH_XML.format(count=self.n)
        start, retmax = int(params["retstart"]), int(params["retmax"])
        ids = range(start, min(start + retmax, self.n))
        if endpoint == "esummary":
            docs = "".join(
                SUMMARY_DOC.format(
                    uid=1000 + i,
                    acc=f"AB{i:05d}",
                    title=f"Test record {i}",
                    created=f"{self.start_year + i % 3}/02/0{i % 9 + 1}",
                    updated="2026/01/01",
                    length=500 + i,
                )
                for i in ids
            )
            return f"<eSummaryResult>{docs}</eSummaryResult>"
        return "".join(f">AB{i:05d} Test record {i}\nACGTACGTAC\n" for i in ids)


@pytest.fixture
def cfg(tmp_path):
    return {
        "retrieved_dir": str(tmp_path / "retrieved"),
        "retrieve": {"page_size": 3, "min_length": 100, "max_records_per_taxon": 100},
    }


def test_query_expands_down_the_taxonomy_and_applies_filters():
    q = build_query(5758, {"retrieve": {"min_length": 100, "max_length": 20000}})
    assert "txid5758[Organism:exp]" in q  # exp = include child taxa
    assert "100:20000[SLEN]" in q


def test_query_suffix_is_wrapped_so_it_cannot_break_the_and_chain():
    q = build_query(1, {"retrieve": {"query_suffix": 'NOT "whole genome shotgun"[Title]'}})
    assert q.endswith('AND (NOT "whole genome shotgun"[Title])')


def test_first_run_is_full_and_fetches_everything(cfg):
    fake = FakeNCBI(7)
    run = retrieve_taxon(109871, cfg, fake, taxon_name="Bd", run_date="2026-10-03")
    assert run.mode == "full" and run.since is None
    assert run.n_available == 7 and run.n_fetched == 7
    assert gzip.open(run.fasta, "rt").read().count(">") == 7
    meta = gzip.open(run.metadata, "rt").read().splitlines()
    assert meta[0].startswith("uid\taccession") and len(meta) == 8


def test_pages_cover_every_record_without_overlap(cfg):
    fake = FakeNCBI(7)  # page_size 3 -> 3 pages
    retrieve_taxon(109871, cfg, fake, run_date="2026-10-03")
    accessions = [
        line.split()[0]
        for line in gzip.open(f"{cfg['retrieved_dir']}/109871/all/2026-10-03.fasta.gz", "rt")
        if line.startswith(">")
    ]
    assert len(accessions) == len(set(accessions)) == 7


def test_second_run_is_incremental_from_the_manifest(cfg):
    first = retrieve_taxon(109871, cfg, FakeNCBI(5), run_date="2026-09-01")
    record_run(cfg, first)
    assert last_run_date(load_manifest(cfg), 109871) == "2026/09/01"

    fake = FakeNCBI(2)
    second = retrieve_taxon(109871, cfg, fake, run_date="2026-10-03")
    assert second.mode == "incremental" and second.since == "2026/09/01"
    params = next(p for e, p in fake.calls if e == "esearch")
    assert params["mindate"] == "2026/09/01"
    assert params["datetype"] == "mdat"  # revisions count, not just new deposits


def test_full_flag_ignores_the_manifest(cfg):
    record_run(cfg, retrieve_taxon(109871, cfg, FakeNCBI(5), run_date="2026-09-01"))
    fake = FakeNCBI(5)
    run = retrieve_taxon(109871, cfg, fake, run_date="2026-10-03", full=True)
    assert run.mode == "full"
    assert "mindate" not in next(p for e, p in fake.calls if e == "esearch")


def test_oversized_taxon_is_refused_with_an_actionable_message(cfg):
    with pytest.raises(TooManyRecords, match="large_taxa_allowed"):
        retrieve_taxon(11320, cfg, FakeNCBI(500_000), taxon_name="Influenza A")


def test_oversized_taxon_can_be_opted_in(cfg):
    cfg["retrieve"]["large_taxa_allowed"] = [11320]
    run = retrieve_taxon(11320, cfg, FakeNCBI(120), run_date="2026-10-03")
    assert run.n_fetched == 120


def test_empty_result_writes_no_files(cfg, tmp_path):
    run = retrieve_taxon(109871, cfg, FakeNCBI(0), run_date="2026-10-03")
    assert run.n_fetched == 0 and run.fasta is None and run.note == "nothing new"
    assert not (tmp_path / "retrieved" / "109871").exists()


def test_assays_with_a_query_form_their_own_group_and_archive(cfg):
    """`invA[Gene]` and the bare taxon must not share a manifest history or a directory."""
    fake = FakeNCBI(4)
    whole = retrieve_taxon(28901, cfg, fake, run_date="2026-10-03")
    gene = retrieve_taxon(28901, cfg, fake, run_date="2026-10-03", assay_query="invA[Gene]")
    assert whole.group == "all" and gene.group.startswith("q")
    assert whole.fasta != gene.fasta
    assert "/28901/all/" in whole.fasta and f"/28901/{gene.group}/" in gene.fasta
    assert "(invA[Gene])" in gene.query and "(invA[Gene])" not in whole.query
    assert group_slug("invA[Gene]") == group_slug("  invA[Gene] ")  # whitespace does not split groups


def test_incremental_history_is_per_group(cfg):
    record_run(cfg, retrieve_taxon(28901, cfg, FakeNCBI(3), run_date="2026-09-01", assay_query="invA[Gene]"))
    bare = retrieve_taxon(28901, cfg, FakeNCBI(3), run_date="2026-10-03")
    assert bare.mode == "full"  # the bare taxon has never been fetched
    gene = retrieve_taxon(28901, cfg, FakeNCBI(3), run_date="2026-10-03", assay_query="invA[Gene]")
    assert gene.mode == "incremental"


def test_dry_run_reports_counts_and_writes_nothing(cfg, tmp_path):
    run = retrieve_taxon(109871, cfg, FakeNCBI(9), run_date="2026-10-03", dry_run=True)
    assert run.n_available == 9 and run.n_fetched == 0 and run.note == "dry run"
    assert not (tmp_path / "retrieved" / "109871").exists()


def test_manifest_is_a_replayable_record_of_what_was_asked(cfg):
    run = retrieve_taxon(109871, cfg, FakeNCBI(4), taxon_name="Bd", run_date="2026-10-03")
    record_run(cfg, run)
    entry = json.loads(open(f"{cfg['retrieved_dir']}/manifest.json").read())["runs"][0]
    assert entry["query"].startswith("txid109871")
    assert entry["run_date"] == "2026-10-03" and entry["n_fetched"] == 4
    assert entry["fasta"].endswith("2026-10-03.fasta.gz")


def test_metadata_carries_the_deposit_year_the_drift_trend_needs(cfg):
    run = retrieve_taxon(109871, cfg, FakeNCBI(3, start_year=2019), run_date="2026-10-03")
    rows = gzip.open(run.metadata, "rt").read().splitlines()[1:]
    years = {row.split("\t")[2][:4] for row in rows}
    assert years == {"2019", "2020", "2021"}


def test_record_meta_year_is_robust_to_a_missing_date():
    assert RecordMeta("1", "AB1", "2014-05-01", "", 100, "t").year == 2014
    assert RecordMeta("1", "AB1", "", "", 100, "t").year is None


def test_esearch_raises_on_an_entrez_error():
    def broken(endpoint, params):
        return "<eSearchResult><ERROR>Invalid term</ERROR></eSearchResult>"

    with pytest.raises(Exception, match="Invalid term"):
        esearch(broken, "txid0[Organism:exp]", None)


def test_registry_targets_skip_deprecated_and_untaxed_assays():
    from pathlib import Path

    targets = targets_from_registry([Path(__file__).resolve().parents[1] / "registry"])
    assert (109871, "all") in targets  # Bd, no per-assay query
    assert all(isinstance(t, int) and isinstance(g, str) for t, g in targets)
    assert targets[(109871, "all")]["assays"], "a group should carry the assays that need it"
