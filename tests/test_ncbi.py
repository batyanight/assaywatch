"""`assaywatch.ncbi`: the one NCBI client (key, pacing, retry, parsers, caches).

Transports take their HTTP function and sleep as parameters, so these tests see every
request and every pause without a network or a real clock. The taxonomy XML fixtures
are real E-utilities answers for 3047346 (ABPV), 6035 (E. cuniculi) and 11232 (an old
CDV taxid NCBI merged into 3052342), captured 2026-10-29 with `efetch`.
"""

import json
from pathlib import Path

import pytest

from assaywatch import ncbi

FIX = Path(__file__).resolve().parent / "fixtures" / "ncbi"
TAXONOMY_XML = (FIX / "taxonomy.xml").read_text()
DOCSUM_XML = (FIX / "taxonomy-docsum.xml").read_text()


class Response:
    def __init__(self, status: int, body: str | bytes = "") -> None:
        self.status_code = status
        self.text = body if isinstance(body, str) else body.decode("utf-8", "replace")
        self.content = body if isinstance(body, bytes) else body.encode()


class Http:
    """Records calls; answers from a queue of Responses (or raises what it is given)."""

    def __init__(self, *answers: Response | Exception) -> None:
        self.answers = list(answers)
        self.calls: list[dict] = []
        self.slept: list[float] = []

    def __call__(self, url: str, **kw: object) -> Response:
        self.calls.append({"url": url, **kw})
        a = self.answers.pop(0)
        if isinstance(a, Exception):
            raise a
        return a

    def sleep(self, s: float) -> None:
        self.slept.append(s)


# --- E-utilities transport ------------------------------------------------------


def test_eutils_sends_email_tool_and_key_and_returns_the_body():
    http = Http(Response(200, "<ok/>"))
    call = ncbi.eutils("me@example.org", "KEY", post=http, sleep=http.sleep)
    assert call("esearch", {"db": "nuccore", "term": "x"}) == "<ok/>"
    sent = http.calls[0]
    assert sent["url"].endswith("/esearch.fcgi")
    assert sent["data"] == {
        "db": "nuccore",
        "term": "x",
        "email": "me@example.org",
        "tool": "assaywatch",
        "api_key": "KEY",
    }


def test_eutils_without_a_key_sends_none_and_paces_at_three_per_second():
    http = Http(Response(200, "a"), Response(200, "b"))
    call = ncbi.eutils("me@example.org", None, post=http, sleep=http.sleep)
    call("efetch", {})
    call("efetch", {})
    assert "api_key" not in http.calls[0]["data"]
    assert http.slept and 0 < http.slept[-1] <= ncbi.INTERVAL_WITHOUT_KEY


def test_eutils_retries_transient_statuses_with_backoff_and_then_succeeds():
    http = Http(Response(429), Response(503), Response(200, "fine"))
    call = ncbi.eutils("me@example.org", "KEY", post=http, sleep=http.sleep)
    assert call("efetch", {}) == "fine"
    assert len(http.calls) == 3
    assert [s for s in http.slept if s >= 1] == [1, 2]


def test_eutils_gives_up_after_five_attempts():
    http = Http(*[Response(500)] * 5)
    call = ncbi.eutils("me@example.org", "KEY", post=http, sleep=http.sleep)
    with pytest.raises(ncbi.NcbiError, match="5 attempts"):
        call("efetch", {})


def test_eutils_reports_an_expired_history_handle_as_its_own_error():
    http = Http(Response(400, "Cannot retrieve History data"))
    call = ncbi.eutils("me@example.org", "KEY", post=http, sleep=http.sleep)
    with pytest.raises(ncbi.HistoryExpired):
        call("efetch", {})


def test_eutils_scrubs_the_key_out_of_an_error_message():
    http = Http(Response(403, "forbidden for api_key=SECRETKEY"))
    call = ncbi.eutils("me@example.org", "SECRETKEY", post=http, sleep=http.sleep)
    with pytest.raises(ncbi.NcbiError) as e:
        call("efetch", {})
    assert "SECRETKEY" not in str(e.value)


# --- Datasets transport ---------------------------------------------------------


def test_datasets_sends_the_key_as_a_header_and_returns_bytes():
    http = Http(Response(200, b"\x1f\x8b"))
    call = ncbi.datasets("KEY", get=http, sleep=http.sleep)
    assert call("genome/accession/GCF_1/download", {"x": 1}, "application/zip") == b"\x1f\x8b"
    sent = http.calls[0]
    assert sent["url"].endswith("/genome/accession/GCF_1/download")
    assert sent["headers"] == {"Accept": "application/zip", "api-key": "KEY"}


def test_datasets_errors_are_ncbi_errors():
    http = Http(Response(404, b"no such genome"))
    call = ncbi.datasets(None, get=http, sleep=http.sleep)
    with pytest.raises(ncbi.NcbiError, match="404"):
        call("genome/x", {}, "application/json")


# --- taxonomy parsing -----------------------------------------------------------


def test_taxon_records_parse_name_rank_common_name_and_lineage():
    records = ncbi.parse_taxon_records(TAXONOMY_XML)
    cun = records[6035]
    assert cun.scientific_name == "Encephalitozoon cuniculi"
    assert cun.rank == "species"
    assert cun.lineage[0] == (131567, "cellular root", "cellular organisms")
    assert cun.lineage[-1][2] == "Encephalitozoon"
    assert cun.lineage_tail == ("Unikaryonidae", "Encephalitozoon")
    assert 131567 in cun.ancestors and 6035 in cun.ancestors


def test_a_merged_taxid_is_keyed_under_the_old_id_and_says_where_it_went():
    records = ncbi.parse_taxon_records(TAXONOMY_XML)
    assert 11232 in records and records[11232].taxid == 3052342
    assert 11232 in records[3052342].aka_taxids


def test_other_names_are_lowercased_for_matching():
    records = ncbi.parse_taxon_records(TAXONOMY_XML)
    names = records[6035].other_names
    assert "encephalitozoon cunuculi" in names  # NCBI's recorded misspelling, as a DispName
    assert all(n == n.lower() for n in names)


def test_merged_ids_come_from_the_docsum_aka_field():
    assert ncbi.parse_merged(DOCSUM_XML) == {11232: 3052342}


def test_taxon_records_batches_the_request():
    seen: list[str] = []

    def transport(endpoint: str, params: dict) -> str:
        seen.append(params["id"])
        return TAXONOMY_XML

    ncbi.taxon_records(list(range(1, 251)), transport, batch=100)
    assert [len(s.split(",")) for s in seen] == [100, 100, 50]


def test_taxids_of_uids_reads_esummary():
    xml = """<eSummaryResult><DocSum><Id>7</Id><Item Name="TaxId" Type="Integer">6035</Item></DocSum>
    <DocSum><Id>8</Id></DocSum></eSummaryResult>"""
    out = ncbi.taxids_of_uids(["7", "8"], lambda e, p: xml)
    assert out == {"7": 6035}


# --- the taxonomy tree the scope test reads -------------------------------------


def test_taxonomy_tree_is_built_from_the_lineages_and_merges():
    records = ncbi.parse_taxon_records(TAXONOMY_XML)
    tree = ncbi.taxonomy_tree(records, merged={11232: 3052342})
    assert tree.canonical(11232) == 3052342
    assert 131567 in tree.ancestors(6035)
    assert tree.rank.get(6035) == "species"
    assert tree.name[6035] == "Encephalitozoon cuniculi"


def test_the_tree_round_trips_through_the_cache_file(tmp_path: Path):
    from assaywatch.taxonomy import load_taxonomy

    records = ncbi.parse_taxon_records(TAXONOMY_XML)
    path = tmp_path / "taxonomy-cache.json.gz"
    ncbi.save_taxonomy_cache(path, records, merged={11232: 3052342}, n_requested=3, missing=[])
    tree = load_taxonomy(path)
    assert tree.canonical(11232) == 3052342 and tree.rank[6035] == "species"


# --- the two JSON caches, one writer --------------------------------------------


def test_taxon_records_cache_round_trips_the_fields_the_sheet_needs(tmp_path: Path):
    records = ncbi.parse_taxon_records(TAXONOMY_XML)
    path = tmp_path / "taxon-records.cache.json"
    ncbi.save_taxon_records_cache(path, records)
    back = ncbi.load_taxon_records_cache(path)
    assert back[6035] == {
        "scientific_name": "Encephalitozoon cuniculi",
        "common_name": "",
        "rank": "species",
        "lineage_tail": ["Unikaryonidae", "Encephalitozoon"],
    }
    assert list(json.loads(path.read_text())) == sorted(json.loads(path.read_text()))


def test_taxon_records_cache_merges_into_what_is_there(tmp_path: Path):
    path = tmp_path / "taxon-records.cache.json"
    path.write_text(
        json.dumps(
            {"1": {"scientific_name": "root", "common_name": "", "rank": "no rank", "lineage_tail": []}}
        )
    )
    ncbi.save_taxon_records_cache(path, ncbi.parse_taxon_records(TAXONOMY_XML))
    assert {1, 6035} <= set(ncbi.load_taxon_records_cache(path))


def test_taxa_names_cache_keeps_the_shape_the_lineage_analysis_reads(tmp_path: Path):
    path = tmp_path / "taxa-cache.json"
    ncbi.save_taxa_names(path, {6035: "Encephalitozoon cuniculi"})
    raw = json.loads(path.read_text())
    assert set(raw) == {"description", "taxa"} and raw["taxa"] == {"6035": "Encephalitozoon cuniculi"}
    assert ncbi.load_taxa_names(path) == {6035: "Encephalitozoon cuniculi"}


def test_the_lineage_module_reads_taxa_names_through_ncbi():
    from assaywatch import lineage

    assert lineage.load_taxa_cache is ncbi.load_taxa_names
