"""Retrieval tests. No network: the transport is a fake returning canned E-utilities XML.

What is worth testing here is not HTTP but the decisions: how the query is
built, when a run is incremental, what the cap does, and whether the archive
and manifest are reproducible.
"""

import gzip
import json
from pathlib import Path

import pytest

from assaywatch.retrieve import (
    RecordMeta,
    RetrievalError,
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
<Item Name="TaxId" Type="Integer">{taxid}</Item>
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
                    taxid=109871 + i,
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
    # Three days of overlap with the previous run, for records NCBI indexes late.
    assert second.mode == "incremental" and second.since == "2026/08/29"
    params = next(p for e, p in fake.calls if e == "esearch")
    assert params["mindate"] == "2026/08/29"
    assert params["maxdate"] == "2026/10/03"  # pinned to the run date
    assert params["datetype"] == "mdat"  # revisions count, not just new deposits


def test_full_flag_ignores_the_manifest(cfg):
    record_run(cfg, retrieve_taxon(109871, cfg, FakeNCBI(5), run_date="2026-09-01"))
    fake = FakeNCBI(5)
    run = retrieve_taxon(109871, cfg, fake, run_date="2026-10-03", full=True)
    assert run.mode == "full"
    params = next(p for e, p in fake.calls if e == "esearch")
    assert params["mindate"] == "1800/01/01" and params["maxdate"] == "2026/10/03"


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


class FlakyNCBI(FakeNCBI):
    """Drops the history handle once, on the first efetch, the way NCBI does under load."""

    def __init__(self, n):
        super().__init__(n)
        self.dropped = False

    def __call__(self, endpoint, params):
        from assaywatch.retrieve import HistoryExpired

        if endpoint == "efetch" and not self.dropped:
            self.dropped = True
            raise HistoryExpired("efetch: Cannot retrieve history data")
        return super().__call__(endpoint, params)


def test_expired_history_handle_is_refreshed_and_the_page_retried(cfg):
    fake = FlakyNCBI(7)
    run = retrieve_taxon(121791, cfg, fake, run_date="2026-10-03")
    assert run.n_fetched == 7
    assert sum(1 for e, _ in fake.calls if e == "esearch") == 2  # the refresh


def test_interrupted_fetch_leaves_no_finished_looking_archive(cfg, tmp_path):
    class Dies(FakeNCBI):
        def __call__(self, endpoint, params):
            if endpoint == "efetch" and int(params["retstart"]) > 0:
                raise RuntimeError("Response ended prematurely")
            return super().__call__(endpoint, params)

    with pytest.raises(RuntimeError):
        retrieve_taxon(10241, cfg, Dies(7), run_date="2026-10-03")
    d = tmp_path / "retrieved" / "10241" / "all"
    assert not (d / "2026-10-03.fasta.gz").exists()
    assert not (d / "2026-10-03.meta.tsv.gz").exists()
    assert not list(d.glob(".*.part"))  # and no partial left to clean up by hand


class BigRecords(FakeNCBI):
    """Every record reports a 200 kb length, like a poxvirus genome."""

    def __call__(self, endpoint, params):
        out = super().__call__(endpoint, params)
        return out.replace('Type="Integer">5', 'Type="Integer">20000') if endpoint == "esummary" else out


def test_efetch_pages_shrink_for_large_records(cfg):
    cfg["retrieve"]["page_size"] = 500
    cfg["retrieve"]["page_target_bytes"] = 2_000_000
    fake = BigRecords(40)
    run = retrieve_taxon(10241, cfg, fake, run_date="2026-10-03")
    fetch_sizes = {int(p["retmax"]) for e, p in fake.calls if e == "efetch"}
    assert fetch_sizes == {10}  # 2 MB / ~200 kb, floored at 10
    assert run.n_fetched == 40 and "pages of 10" in run.note


def test_small_records_keep_the_full_page(cfg):
    fake = FakeNCBI(7)
    run = retrieve_taxon(109871, cfg, fake, run_date="2026-10-03")
    assert run.note == ""
    assert {int(p["retmax"]) for e, p in fake.calls if e == "efetch"} == {3}


def test_a_second_run_on_the_same_day_never_overwrites_the_first(cfg):
    """Regression: an incremental run named by date would replace the morning's full archive."""
    first = retrieve_taxon(109871, cfg, FakeNCBI(7), run_date="2026-10-04")
    second = retrieve_taxon(109871, cfg, FakeNCBI(2), run_date="2026-10-04", full=True)
    assert first.fasta.endswith("2026-10-04.fasta.gz")
    assert second.fasta.endswith("2026-10-04_2.fasta.gz")
    assert gzip.open(first.fasta, "rt").read().count(">") == 7  # untouched


def test_manifest_write_is_atomic(cfg, tmp_path):
    record_run(cfg, retrieve_taxon(109871, cfg, FakeNCBI(3), run_date="2026-10-04"))
    d = tmp_path / "retrieved"
    assert (d / "manifest.json").exists() and not list(d.glob(".manifest.json.part"))


def test_run_record_lists_every_group_including_nothing_new(tmp_path, monkeypatch):
    import assaywatch.retrieve as R

    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(
        f"retrieved_dir: {tmp_path / 'retrieved'}\nretrieve: {{page_size: 50, max_records_per_taxon: 1000}}\n"
    )
    monkeypatch.setattr(R, "http_transport", lambda email, key: FakeNCBI(0))
    record = tmp_path / "runs" / "today.json"
    rc = R.main(
        [
            str(Path(__file__).resolve().parents[1] / "registry"),
            "--email",
            "t@e.org",
            "--config",
            str(cfg_path),
            "--taxid",
            "109871",
            "--run-record",
            str(record),
        ]
    )
    assert rc == 0
    data = json.loads(record.read_text())
    assert [r["taxid"] for r in data["runs"]] == [109871]
    assert data["runs"][0]["note"] == "nothing new"


def test_rebuild_manifest_from_archives(tmp_path, monkeypatch):
    import importlib.util

    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location("rebuild", root / "scripts" / "rebuild_manifest.py")
    rebuild_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rebuild_mod)

    cfg = {
        "retrieved_dir": str(tmp_path / "retrieved"),
        "retrieve": {"page_size": 5, "max_records_per_taxon": 100},
    }
    retrieve_taxon(109871, cfg, FakeNCBI(6), run_date="2026-10-03")
    retrieve_taxon(109871, cfg, FakeNCBI(2), run_date="2026-10-03", full=True)
    (tmp_path / "retrieved" / "109871" / "all" / ".2026-10-04.fasta.gz.part").write_text("x")

    manifest, partials = rebuild_mod.rebuild(cfg, root / "registry")
    runs = sorted(manifest["runs"], key=lambda r: r["fasta"])
    assert [r["n_fetched"] for r in runs] == [6, 2]
    assert [r["mode"] for r in runs] == ["full", "incremental"]
    assert runs[0]["assays"], "assays come from the registry"
    assert len(partials) == 1
    assert last_run_date(manifest, 109871) == "2026/10/03"


def test_an_error_document_in_a_200_response_is_not_archived(cfg, tmp_path):
    class Errors(FakeNCBI):
        def __call__(self, endpoint, params):
            if endpoint == "efetch" and int(params["retstart"]) > 0:
                return "<eFetchResult><ERROR>Something went wrong</ERROR></eFetchResult>"
            return super().__call__(endpoint, params)

    with pytest.raises(RetrievalError):
        retrieve_taxon(10241, cfg, Errors(7), run_date="2026-10-03")
    d = tmp_path / "retrieved" / "10241" / "all"
    assert not list(d.glob("*.fasta.gz")) and not list(d.glob(".*.part"))


def test_esummary_error_is_raised_not_ignored(cfg):
    class Errors(FakeNCBI):
        def __call__(self, endpoint, params):
            if endpoint == "esummary":
                return "<eSummaryResult><ERROR>Invalid uid</ERROR></eSummaryResult>"
            return super().__call__(endpoint, params)

    with pytest.raises(RetrievalError):
        retrieve_taxon(10241, cfg, Errors(3), run_date="2026-10-03")


# --------------------------------------------------------------------------
# A truncated fetch must be distinguishable from a complete one (2026-10-27).
#
# Before these, an empty efetch page returned 0 records without raising, the
# shortfall was recorded as a note indistinguishable from the legitimate
# WGS-master case, and the run went into the manifest with today's date -- after
# which the incremental cursor asked only for records modified since, so the
# dropped records could never be fetched by any later run.
# --------------------------------------------------------------------------


def test_empty_efetch_page_raises_rather_than_counting_zero(cfg, tmp_path):
    class EmptyPage(FakeNCBI):
        def __call__(self, endpoint, params):
            if endpoint == "efetch" and int(params["retstart"]) > 0:
                return ""
            return super().__call__(endpoint, params)

    with pytest.raises(RetrievalError, match="empty page"):
        retrieve_taxon(10241, cfg, EmptyPage(7), run_date="2026-10-03")
    # And nothing that looks like an archive is left behind.
    d = tmp_path / "retrieved" / "10241" / "all"
    assert not list(d.glob("*.fasta.gz")) and not list(d.glob(".*.part"))


def test_whitespace_only_efetch_page_also_raises(cfg):
    class Blank(FakeNCBI):
        def __call__(self, endpoint, params):
            if endpoint == "efetch" and int(params["retstart"]) > 0:
                return "\n\n   \n"
            return super().__call__(endpoint, params)

    with pytest.raises(RetrievalError, match="empty page"):
        retrieve_taxon(10241, cfg, Blank(7), run_date="2026-10-03")


def test_large_shortfall_is_refused_and_leaves_no_manifest_entry(cfg, tmp_path):
    """One page answers with a single record instead of its full three."""

    class Thin(FakeNCBI):
        def __call__(self, endpoint, params):
            if endpoint == "efetch" and int(params["retstart"]) == 0:
                return ">AB00000 Test record 0\nACGTACGTAC\n"
            return super().__call__(endpoint, params)

    # allowance floor 0 and fraction 0, so any shortfall is unexplained
    cfg["retrieve"]["min_shortfall_allowance"] = 0
    cfg["retrieve"]["max_unexplained_shortfall"] = 0.0
    with pytest.raises(RetrievalError, match="shortfall"):
        retrieve_taxon(10241, cfg, Thin(7), run_date="2026-10-03")
    d = tmp_path / "retrieved" / "10241" / "all"
    assert not list(d.glob("*.fasta.gz")) and not list(d.glob(".*.part"))
    assert load_manifest(cfg) == {"runs": []}


def test_small_shortfall_within_allowance_is_recorded_with_a_note(cfg):
    """The legitimate WGS-master case still passes, and says how short it was."""

    class Thin(FakeNCBI):
        def __call__(self, endpoint, params):
            if endpoint == "efetch" and int(params["retstart"]) == 0:
                return ">AB00000 Test record 0\nACGTACGTAC\n"
            return super().__call__(endpoint, params)

    cfg["retrieve"]["min_shortfall_allowance"] = 20  # the default floor
    run = retrieve_taxon(10241, cfg, Thin(7), run_date="2026-10-03")
    assert run.n_fetched == 5  # 7 summaries, one page short by 2
    assert "summaries without sequence" in run.note
    assert "page shortfall 2" in run.note


# --------------------------------------------------------------------------
# The incremental cursor must not outlive the query it was built from.
# --------------------------------------------------------------------------


def test_changed_length_filter_forces_a_full_fetch(cfg):
    """The group slug hashes the assay query only, so it cannot see this change."""
    record_run(cfg, retrieve_taxon(109871, cfg, FakeNCBI(5), run_date="2026-09-01"))
    assert last_run_date(load_manifest(cfg), 109871) == "2026/09/01"

    cfg["retrieve"]["min_length"] = 50  # widened: older short records now qualify
    fake = FakeNCBI(5)
    second = retrieve_taxon(109871, cfg, fake, run_date="2026-10-03")
    assert second.mode == "full" and second.since is None
    params = next(p for e, p in fake.calls if e == "esearch")
    # The whole point: no lower date bound, so nothing older is skipped. `until`
    # is always pinned to the run date, so mindate is present but unbounded.
    assert params["mindate"] == "1800/01/01"
    assert "50:100000000[SLEN]" in params["term"]  # fetched under the NEW filter


def test_unchanged_query_still_goes_incremental(cfg):
    record_run(cfg, retrieve_taxon(109871, cfg, FakeNCBI(5), run_date="2026-09-01"))
    second = retrieve_taxon(109871, cfg, FakeNCBI(2), run_date="2026-10-03")
    assert second.mode == "incremental" and second.since == "2026/08/29"


def test_last_run_date_filters_on_the_recorded_query(cfg):
    record_run(cfg, retrieve_taxon(109871, cfg, FakeNCBI(5), run_date="2026-09-01"))
    manifest = load_manifest(cfg)
    recorded = manifest["runs"][0]["query"]
    assert last_run_date(manifest, 109871, query=recorded) == "2026/09/01"
    assert last_run_date(manifest, 109871, query="txid109871[Organism:exp] AND other") is None
    # Without a query the cursor is unconditional, which is what `asm` groups use.
    assert last_run_date(manifest, 109871) == "2026/09/01"
