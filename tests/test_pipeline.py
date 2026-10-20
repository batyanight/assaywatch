"""End-to-end: retrieval writes an archive, screening reads it, offline throughout.

This is the join between the two stages, which unit tests of either one miss:
the FASTA the retriever writes has to be the FASTA the screener can read, gzip
and all, and the record ids have to survive the round trip so a call can be
traced back to an accession.
"""

import gzip

from test_retrieve import ESEARCH_XML, SUMMARY_DOC
from test_score import FIX, RECORDS, ROOT

from assaywatch.fasta import read_fasta
from assaywatch.retrieve import retrieve_taxon
from assaywatch.screen import main as screen_main


class FakeNCBIServingFixtures:
    """An NCBI that returns the synthetic fixture records for the Bd assays."""

    def __init__(self):
        self.records = [(rid, seq) for rid, seq in RECORDS.items() if rid.startswith("CHYTRID_Bd")]

    def __call__(self, endpoint, params):
        if endpoint == "esearch":
            return ESEARCH_XML.format(count=len(self.records))
        start, retmax = int(params["retstart"]), int(params["retmax"])
        page = self.records[start : start + retmax]
        if endpoint == "esummary":
            docs = "".join(
                SUMMARY_DOC.format(
                    uid=i,
                    acc=rid,
                    title=rid,
                    created="2015/06/01",
                    updated="2026/01/01",
                    length=len(seq),
                    taxid=10239,
                )
                for i, (rid, seq) in enumerate(page, start=start)
            )
            return f"<eSummaryResult>{docs}</eSummaryResult>"
        return "".join(f">{rid} fixture\n{seq}\n" for rid, seq in page)


def test_retrieve_then_screen(tmp_path, capsys):
    cfg = {
        "retrieved_dir": str(tmp_path / "retrieved"),
        "retrieve": {"page_size": 5, "max_records_per_taxon": 1000},
    }
    run = retrieve_taxon(109871, cfg, FakeNCBIServingFixtures(), taxon_name="Bd", run_date="2026-10-03")
    assert run.n_fetched == len([r for r in RECORDS if r.startswith("CHYTRID_Bd")])

    # The archive is readable by the screener's own FASTA reader, gzipped.
    fetched = dict(read_fasta(run.fasta))
    assert (
        fetched["CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004__perfect"]
        == (RECORDS["CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004__perfect"])
    )

    out = tmp_path / "calls.tsv"
    screen_main(
        [
            str(ROOT / "registry" / "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004.yaml"),
            str(run.fasta),
            "-o",
            str(out),
        ]
    )
    rows = out.read_text().splitlines()
    assert len(rows) == run.n_fetched + 1
    calls = {r.split("\t")[1]: r.split("\t")[2] for r in rows[1:]}
    assert calls["CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004__perfect"] == "detect"
    assert calls["CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004__fwd_3term"] == "fail"


def test_metadata_rows_line_up_with_the_fasta(tmp_path):
    cfg = {"retrieved_dir": str(tmp_path / "r"), "retrieve": {"page_size": 4, "max_records_per_taxon": 1000}}
    run = retrieve_taxon(109871, cfg, FakeNCBIServingFixtures(), run_date="2026-10-03")
    meta = gzip.open(run.metadata, "rt").read().splitlines()[1:]
    accessions = [line.split("\t")[1] for line in meta]
    ids = [rid for rid, _ in read_fasta(run.fasta)]
    assert accessions == ids


def test_fixture_archive_is_not_left_behind(tmp_path):
    """Sanity: nothing is written into the repo's own data directory by tests."""
    assert not (FIX / "retrieved").exists()
