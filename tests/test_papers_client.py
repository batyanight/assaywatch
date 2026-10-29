"""`assaywatch.papers`, the client half: Crossref, open-access routes, full text, storage.

Every network function takes a `Get`, so these tests hand in canned answers and see
every request. The JSON and XML below are cut down from real answers.
"""

import json
from pathlib import Path

from assaywatch import papers

DOI = "10.3390/microorganisms12061105"

CROSSREF = {
    "message": {
        "DOI": DOI,
        "title": ["Selection and Multiplexing of <i>RT-qPCR</i> Tests"],
        "container-title": ["Microorganisms"],
        "volume": "12",
        "issued": {"date-parts": [[2024, 6, 1]]},
        "author": [{"family": "Rossi", "given": "F."}, {"family": "Del Matto"}],
    }
}
UNPAYWALL = {
    "is_oa": True,
    "oa_status": "gold",
    "title": "Selection and Multiplexing",
    "best_oa_location": {
        "host_type": "publisher",
        "version": "publishedVersion",
        "url_for_landing_page": "https://x/l",
    },
    "oa_locations": [
        {"host_type": "repository", "version": "acceptedVersion", "url_for_pdf": "https://x/p.pdf"}
    ],
}
OPENALEX = {
    "open_access": {"is_oa": True},
    "best_oa_location": {
        "pdf_url": "https://o/p.pdf",
        "version": "publishedVersion",
        "source": {"type": "journal"},
    },
}
EPMC_SEARCH = {
    "resultList": {
        "result": [
            {"pmcid": "PMC1", "isOpenAccess": "N", "inPMC": "N"},
            {"pmcid": "PMC2", "isOpenAccess": "Y"},
        ]
    }
}
CONVERTER = {"records": [{"doi": DOI, "pmcid": "PMC9"}]}
FULLTEXT = (
    "<article><front><title-group><article-title>A paper</article-title></title-group></front>"
    "<body><p>Primers were:</p><table-wrap><table><tr><th>Name</th><th>Sequence</th></tr>"
    "<tr><td>APVF</td><td>TTTGTTTCAAAYAARATG</td></tr></table></table-wrap></body></article>"
)
ELSEVIER_ERROR = json.dumps(
    {"service-error": {"status": {"statusCode": "AUTHENTICATION_ERROR", "statusText": "Invalid API Key"}}}
).encode()


class Get:
    """A `papers.Get`: answers by URL substring, records every call."""

    def __init__(self, **by_substring: tuple[int, str, bytes | str]) -> None:
        self.by = by_substring
        self.calls: list[tuple[str, dict[str, str]]] = []

    def __call__(self, url: str, headers: dict[str, str]) -> tuple[int, str, bytes]:
        self.calls.append((url, headers))
        for needle, (status, ctype, body) in self.by.items():
            if needle in url:
                return status, ctype, body if isinstance(body, bytes) else body.encode()
        return 404, "text/plain", b"not here"


def j(obj: object) -> tuple[int, str, str]:
    return 200, "application/json", json.dumps(obj)


# --- Crossref -------------------------------------------------------------------


def test_crossref_parses_title_journal_year_and_authors_and_strips_markup():
    get = Get(crossref=j(CROSSREF))
    c = papers.crossref(DOI, get, email="me@example.org")
    assert c is not None
    assert (c.title, c.journal, c.year, c.volume) == (
        "Selection and Multiplexing of RT-qPCR Tests",
        "Microorganisms",
        2024,
        "12",
    )
    assert c.authors == ("Rossi", "Del Matto") and c.first_author == "Rossi"
    url, headers = get.calls[0]
    assert "api.crossref.org/works/10.3390%2F" in url and "mailto=me%40example.org" in url
    assert "assaywatch" in headers["User-Agent"]


def test_a_doi_crossref_does_not_know_is_none():
    assert papers.crossref("10.1/nope", Get(), email="me@example.org") is None


def test_citation_matches_wants_the_first_author_in_the_reference_and_a_year_within_one():
    c = papers.parse_crossref(CROSSREF["message"])
    ok, summary = papers.citation_matches(c, 2023, "Rossi F, Del Matto I. 2024. Microorganisms 12:1105")
    assert ok and summary.startswith("Rossi 2024")
    assert not papers.citation_matches(c, 2024, "Smith J. 2024")[0]
    assert not papers.citation_matches(c, 2020, "Rossi F. 2020")[0]


def test_citation_problems_is_what_check_citations_reports():
    c = papers.parse_crossref(CROSSREF["message"])
    assert papers.citation_problems(c, {"reference": "Rossi F. 2024", "design_year": 2024}) == []
    probs = papers.citation_problems(c, {"reference": "Smith J. 2019", "design_year": 2019})
    assert len(probs) == 2 and "first author" in probs[0] and "year" in probs[1]
    assert papers.citation_problems(c, {"reference": "", "design_year": None}) == [
        "no reference text, though Crossref knows the paper (Rossi)"
    ]


def test_the_index_cache_round_trips_in_its_committed_shape(tmp_path: Path):
    path = tmp_path / "papers-index.cache.json"
    c = papers.parse_crossref(CROSSREF["message"])
    papers.save_index_cache(path, {DOI: c, "10.1/dead": None})
    raw = json.loads(path.read_text())
    assert raw[DOI]["first_author"] == "Rossi" and raw[DOI]["n_authors"] == 2 and raw["10.1/dead"] is None
    assert raw[DOI]["authors"] == ["Rossi", "Del Matto"]
    back = papers.load_index_cache(path)
    assert back[DOI] == c and back["10.1/dead"] is None


# --- where a free copy is -------------------------------------------------------


def test_unpaywall_prefers_a_location_that_has_the_pdf():
    oa = papers.unpaywall(DOI, Get(unpaywall=j(UNPAYWALL)), email="me@example.org")
    assert oa is not None and oa.is_oa and oa.url_pdf == "https://x/p.pdf" and oa.host_type == "repository"
    assert oa.source == "unpaywall" and oa.oa_status == "gold"


def test_openalex_is_asked_too_because_the_two_disagree():
    oa = papers.openalex(DOI, Get(openalex=j(OPENALEX)), email="me@example.org")
    assert oa is not None and oa.url_pdf == "https://o/p.pdf" and oa.source == "openalex"


def test_pmcid_tries_ncbis_converter_then_europe_pmc_open_access_only():
    get = Get(idconv=j(CONVERTER))
    assert papers.pmcid_for(DOI, get, email="me@example.org") == "PMC9"
    get = Get(europepmc=j(EPMC_SEARCH))
    assert papers.pmcid_for(DOI, get, email="me@example.org") == "PMC2"
    assert papers.pmcid_for(DOI, Get(), email="me@example.org") is None


# --- full text ------------------------------------------------------------------


def test_fulltext_keeps_tables_legible_and_rejects_a_non_article():
    get = Get(fullTextXML=(200, "application/xml", FULLTEXT))
    text = papers.europepmc_fulltext("PMC2", get)
    assert text is not None
    assert "APVF | TTTGTTTCAAAYAARATG" in text
    assert papers.europepmc_fulltext("PMC3", Get(fullTextXML=(200, "text/html", "<html>no</html>"))) is None


def test_elsevier_sends_key_and_token_and_explains_its_errors():
    get = Get(**{"api.elsevier.com": (401, "application/json", ELSEVIER_ERROR)})
    status, _ctype, body = papers.elsevier_pdf(DOI, get, key="K" * 10, inst_token="T" * 10)
    assert status == 401 and papers.elsevier_error(body) == "AUTHENTICATION_ERROR: Invalid API Key"
    _, headers = get.calls[0]
    assert headers["X-ELS-APIKey"] == "K" * 10 and headers["X-ELS-Insttoken"] == "T" * 10


# --- storing and queueing -------------------------------------------------------


def test_stored_files_take_the_doi_stem_and_are_whole_or_absent(tmp_path: Path):
    p = papers.store(DOI, "text", tmp_path, kind="txt")
    assert p == tmp_path / "10.3390_microorganisms12061105.txt" and p.read_text() == "text"
    q = papers.store(DOI, b"%PDF-1.4", tmp_path, kind="pdf")
    assert q.suffix == ".pdf" and q.read_bytes() == b"%PDF-1.4"
    assert not list(tmp_path.glob(".*.part"))


def test_queueing_for_a_human_appends_once_per_doi(tmp_path: Path):
    fl = tmp_path / "papers-fetch-list.md"
    fl.write_text("# Fetch list\n\nprose\n")
    papers.queue_for_human(DOI, "paywalled, no Elsevier key", fl)
    papers.queue_for_human(DOI, "again", fl)
    papers.queue_for_human("10.1/x", "other", fl)
    text = fl.read_text()
    assert text.startswith("# Fetch list\n\nprose\n")
    assert text.count(f"https://doi.org/{DOI}") == 1 and "10.1/x" in text
    assert papers.queued(fl) == {DOI, "10.1/x"}


# --- obtain: the chain curate runs ---------------------------------------------


def test_obtain_prefers_a_local_file_and_touches_no_network(tmp_path: Path):
    (tmp_path / "10.3390_microorganisms12061105.pdf").write_bytes(b"%PDF")
    get = Get()
    path, how = papers.obtain(DOI, tmp_path, get, email="me@example.org", fetch_list=tmp_path / "fl.md")
    assert path == tmp_path / "10.3390_microorganisms12061105.pdf" and how == "local"
    assert get.calls == []


def test_obtain_takes_europe_pmc_full_text_when_it_is_long_enough(tmp_path: Path):
    long = FULLTEXT.replace("Primers were:", "x" * 7000)
    get = Get(idconv=j(CONVERTER), fullTextXML=(200, "application/xml", long))
    path, how = papers.obtain(DOI, tmp_path, get, email="me@example.org", fetch_list=tmp_path / "fl.md")
    assert path is not None and path.suffix == ".txt" and how == "europepmc:PMC9"
    assert "APVF | TTTGTTTCAAAYAARATG" in path.read_text()


def test_obtain_rejects_an_abstract_length_deposit_and_tries_the_pdf_routes(tmp_path: Path):
    get = Get(
        idconv=j(CONVERTER),
        fullTextXML=(200, "application/xml", FULLTEXT),
        unpaywall=j(UNPAYWALL),
        **{"x/p.pdf": (200, "application/pdf", b"%PDF-1.5 body")},
    )
    path, how = papers.obtain(DOI, tmp_path, get, email="me@example.org", fetch_list=tmp_path / "fl.md")
    assert path is not None and path.suffix == ".pdf" and how == "unpaywall"
    assert path.read_bytes().startswith(b"%PDF")


def test_obtain_queues_for_a_human_when_every_route_fails(tmp_path: Path):
    fl = tmp_path / "fl.md"
    path, how = papers.obtain("10.1016/j.x.2020.1", tmp_path, Get(), email="me@example.org", fetch_list=fl)
    assert path is None and "queued" in how
    assert papers.queued(fl) == {"10.1016/j.x.2020.1"}


def test_obtain_uses_elsevier_for_an_elsevier_doi_when_a_key_is_present(tmp_path: Path):
    get = Get(**{"api.elsevier.com": (200, "application/pdf", b"%PDF-1.7 els")})
    path, how = papers.obtain(
        "10.1016/j.x.2020.1",
        tmp_path,
        get,
        email="me@example.org",
        fetch_list=tmp_path / "fl.md",
        elsevier=("K" * 10, None),
    )
    assert path is not None and how == "elsevier" and path.read_bytes().startswith(b"%PDF")
