"""`assaywatch curate <entry>`: the curation chain, write-through, stopping at judgement.

The chain runs against fakes: a `Transport` for NCBI, a `Get` for the literature, and
a registry directory and archive built under tmp_path from the fixtures. No network.
"""

import gzip
import json
from pathlib import Path

import pytest
import yaml

from assaywatch import curate, registry
from assaywatch.score import load_config

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "tests" / "fixtures"
BD = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
TAXONOMY_XML = (FIX / "ncbi" / "taxonomy.xml").read_text()


def bd_taxonomy_xml() -> str:
    """The fixture XML with E. cuniculi's record relabelled as the Bd entry's taxon."""
    return TAXONOMY_XML.replace("<TaxId>6035</TaxId>", "<TaxId>109871</TaxId>").replace(
        "Encephalitozoon cuniculi", "Batrachochytrium dendrobatidis"
    )


class Ncbi:
    def __init__(self, *, taxonomy: str | None = None, esearch_ids: list[str] | None = None) -> None:
        self.taxonomy = taxonomy if taxonomy is not None else bd_taxonomy_xml()
        self.esearch_ids = esearch_ids or []
        self.calls: list[tuple[str, dict]] = []

    def __call__(self, endpoint: str, params: dict) -> str:
        self.calls.append((endpoint, params))
        if endpoint == "efetch" and params.get("db") == "taxonomy":
            return self.taxonomy
        if endpoint == "esearch":
            return json.dumps({"esearchresult": {"idlist": self.esearch_ids}})
        raise AssertionError(f"unexpected NCBI call {endpoint} {params}")


class Lit:
    """A `papers.Get` answering by URL substring."""

    def __init__(self, **by: tuple[int, str, str | bytes]) -> None:
        self.by = by
        self.calls: list[str] = []

    def __call__(self, url: str, headers: dict[str, str]) -> tuple[int, str, bytes]:
        self.calls.append(url)
        for needle, (status, ctype, body) in self.by.items():
            if needle in url:
                return status, ctype, body if isinstance(body, bytes) else body.encode()
        return 404, "text/plain", b""


def crossref_for(entry: dict) -> tuple[int, str, str]:
    ref = entry["citation"]["reference"]
    family = ref.split(",")[0].split()[0]
    msg = {
        "message": {
            "DOI": entry["citation"]["doi"],
            "title": ["t"],
            "container-title": ["j"],
            "issued": {"date-parts": [[entry["citation"]["design_year"]]]},
            "author": [{"family": family}],
        }
    }
    return 200, "application/json", json.dumps(msg)


@pytest.fixture
def ws(tmp_path: Path) -> dict:
    """A registry with the Bd entry, its fixture archive, a papers dir and a fetch list."""
    reg = tmp_path / "registry"
    reg.mkdir()
    src = ROOT / "registry" / f"{BD}.yaml"
    (reg / src.name).write_text(src.read_text())
    entry = yaml.safe_load(src.read_text())
    archive_dir = tmp_path / "retrieved" / str(entry["target"]["taxid"]) / "all"
    archive_dir.mkdir(parents=True)
    records = []
    with (FIX / "records.fasta").open() as fh:
        rid, seq = None, []
        for line in fh:
            if line.startswith(">"):
                if rid and rid.startswith(BD):
                    records.append((rid, "".join(seq)))
                rid, seq = line[1:].strip(), []
            else:
                seq.append(line.strip())
        if rid and rid.startswith(BD):
            records.append((rid, "".join(seq)))
    with gzip.open(archive_dir / "2026-10-03.fasta.gz", "wt") as out:
        for rid, s in records:
            out.write(f">{rid}\n{s}\n")
    papers = tmp_path / "papers"
    papers.mkdir()
    return {
        "path": reg / src.name,
        "entry": entry,
        "retrieved": tmp_path / "retrieved",
        "papers": papers,
        "fetch_list": tmp_path / "papers-fetch-list.md",
        "cfg": load_config(ROOT / "config.yaml"),
        "n_records": len(records),
    }


def run(ws: dict, **kw) -> curate.Curation:
    args = dict(
        cfg=ws["cfg"],
        email="me@example.org",
        retrieved=ws["retrieved"],
        paper_dir=ws["papers"],
        fetch_list=ws["fetch_list"],
        transport=Ncbi(),
        get=Lit(crossref=crossref_for(ws["entry"])),
    )
    args.update(kw)
    return curate.curate(ws["path"], **args)


# --- the shape of an answer -----------------------------------------------------


def test_a_curation_reports_every_step_in_order(ws: dict):
    c = run(ws)
    assert c.assay_id == BD
    assert [f.step for f in c.findings][:3] == ["schema", "keys", "citation"]
    assert {f.step for f in c.findings} == set(curate.STEPS)
    assert all(f.level in curate.LEVELS for f in c.findings)


def test_an_entry_that_does_not_parse_is_one_finding_and_nothing_runs(ws: dict):
    ws["path"].write_text("id: nope\n")
    c = run(ws)
    assert c.failed and [f.step for f in c.findings] == ["schema"]


# --- the checks that only read --------------------------------------------------


def test_duplicate_keys_fail_and_name_the_line(ws: dict):
    ws["path"].write_text(ws["path"].read_text() + "amplicon_bp: 146\n")
    c = run(ws)
    f = next(f for f in c.findings if f.step == "keys")
    assert f.level == "FAIL" and "amplicon_bp" in f.message


def test_the_taxon_is_checked_against_ncbi(ws: dict):
    c = run(ws)
    f = next(f for f in c.findings if f.step == "taxon")
    assert f.level == "OK" and "Batrachochytrium" in f.message


def test_a_taxon_that_ncbi_names_differently_fails(ws: dict):
    c = run(ws, transport=Ncbi(taxonomy=TAXONOMY_XML.replace("<TaxId>6035</TaxId>", "<TaxId>109871</TaxId>")))
    f = next(f for f in c.findings if f.step == "taxon")
    assert f.level == "FAIL" and "Encephalitozoon" in f.message


def test_the_oligos_amplify_the_fixture_records(ws: dict):
    c = run(ws)
    f = next(f for f in c.findings if f.step == "amplify")
    assert f.level == "OK" and "amplicon" in f.message


def test_offline_skips_the_network_steps_and_says_so(ws: dict):
    ncbi, lit = Ncbi(), Lit()
    c = run(ws, transport=ncbi, get=lit, offline=True)
    assert ncbi.calls == [] and lit.calls == []
    assert {f.step: f.level for f in c.findings if f.step in ("citation", "taxon", "paper")} == {
        "citation": "SKIP",
        "taxon": "SKIP",
        "paper": "SKIP",
    }


# --- write-through ---------------------------------------------------------------


def test_a_matching_doi_is_marked_verified_in_the_file(ws: dict):
    registry.edit(ws["path"], {"status": "draft", "citation.doi_verified": False})
    c = run(ws)
    f = next(f for f in c.findings if f.step == "citation")
    assert f.level == "WROTE" and c.wrote == {"citation.doi_verified": True}
    assert registry.load_one(ws["path"]).citation.doi_verified is True


def test_a_doi_that_does_not_match_the_reference_is_not_verified(ws: dict):
    registry.edit(
        ws["path"],
        {"status": "draft", "citation.doi_verified": False, "citation.reference": "Nobody X. 1990. Nowhere"},
    )
    c = run(ws)
    f = next(f for f in c.findings if f.step == "citation")
    assert f.level == "FAIL" and c.wrote == {}
    assert registry.load_one(ws["path"]).citation.doi_verified is False


def test_a_missing_taxid_is_filled_when_ncbi_gives_exactly_one(ws: dict):
    text = (
        ws["path"]
        .read_text()
        .replace("  taxid: 109871\n", "  taxid: null\n", 1)
        .replace("status: active\n", "status: draft\n", 1)
    )
    ws["path"].write_text(text)
    c = run(ws, transport=Ncbi(esearch_ids=["109871"]))
    assert c.wrote.get("target.taxid") == 109871
    assert registry.load_one(ws["path"]).target.taxid == 109871


def test_an_ambiguous_taxon_name_is_a_question_not_a_write(ws: dict):
    ws["path"].write_text(
        ws["path"]
        .read_text()
        .replace("  taxid: 109871\n", "  taxid: null\n", 1)
        .replace("status: active\n", "status: draft\n", 1)
    )
    c = run(ws, transport=Ncbi(esearch_ids=["1", "2"]))
    f = next(f for f in c.findings if f.step == "taxon")
    assert f.level == "TODO" and "target.taxid" not in c.wrote


def test_an_unset_amplicon_is_measured_and_written(ws: dict):
    ws["path"].write_text(ws["path"].read_text().replace("amplicon_bp: 146\n", "amplicon_bp: null\n", 1))
    c = run(ws)
    f = next(f for f in c.findings if f.step == "amplicon")
    assert f.level == "WROTE" and c.wrote.get("amplicon_bp") == 146
    assert registry.load_one(ws["path"]).amplicon_bp == 146


def test_a_stored_amplicon_that_disagrees_is_a_judgement_not_a_write(ws: dict):
    ws["path"].write_text(ws["path"].read_text().replace("amplicon_bp: 146\n", "amplicon_bp: 180\n", 1))
    c = run(ws)
    f = next(f for f in c.findings if f.step == "amplicon")
    assert f.level == "TODO" and "146" in f.message and "180" in f.message
    assert "amplicon_bp" not in c.wrote and registry.load_one(ws["path"]).amplicon_bp == 180


def test_dry_run_reports_what_it_would_write_and_writes_nothing(ws: dict):
    registry.edit(ws["path"], {"status": "draft", "citation.doi_verified": False})
    before = ws["path"].read_text()
    c = run(ws, write=False)
    assert c.wrote == {"citation.doi_verified": True}
    assert ws["path"].read_text() == before


def test_status_is_never_touched(ws: dict):
    ws["path"].write_text(ws["path"].read_text().replace("status: active\n", "status: draft\n", 1))
    c = run(ws)
    assert "status" not in c.wrote and registry.load_one(ws["path"]).status.value == "draft"


# --- the paper -------------------------------------------------------------------


def test_the_paper_is_fetched_and_every_oligo_judged_against_it(ws: dict):
    e = ws["entry"]["oligos"]
    text = (
        "x" * 7000
        + f"<table><tr><td>F</td><td>{e['forward']['seq']}</td></tr><tr><td>R</td><td>{e['reverse']['seq']}</td></tr></table>"
    )
    lit = Lit(
        crossref=crossref_for(ws["entry"]),
        idconv=(200, "application/json", json.dumps({"records": [{"pmcid": "PMC77"}]})),
        fullTextXML=(200, "application/xml", f"<article>{text}</article>"),
    )
    c = run(ws, get=lit)
    paper = next(f for f in c.findings if f.step == "paper")
    assert paper.level == "OK" and "europepmc:PMC77" in paper.message
    oligos = [f for f in c.findings if f.step == "oligos"]
    assert {f.message.split(" ")[0]: f.level for f in oligos} == {
        "forward": "OK",
        "reverse": "OK",
        "probe": "TODO",
    }
    assert list(ws["papers"].glob("*.txt"))


def test_a_paper_nobody_can_fetch_is_queued_and_the_oligos_wait(ws: dict):
    c = run(ws)
    paper = next(f for f in c.findings if f.step == "paper")
    assert paper.level == "TODO" and "queued" in paper.message
    assert ws["entry"]["citation"]["doi"] in ws["fetch_list"].read_text()
    assert all(f.level == "SKIP" for f in c.findings if f.step == "oligos")


# --- what is left for a human -------------------------------------------------


def test_the_worklist_is_the_todo_and_fail_findings(ws: dict):
    ws["path"].write_text(ws["path"].read_text().replace("amplicon_bp: 146\n", "amplicon_bp: 180\n", 1))
    c = run(ws)
    assert c.worklist and all(f.level in ("TODO", "FAIL") for f in c.worklist)
    assert any(f.step == "amplicon" for f in c.worklist)


def test_the_report_is_readable_and_names_the_writes(ws: dict, capsys):
    ws["path"].write_text(ws["path"].read_text().replace("amplicon_bp: 146\n", "amplicon_bp: null\n", 1))
    c = run(ws)
    print(c.report())
    out = capsys.readouterr().out
    assert BD in out and "WROTE" in out and "amplicon_bp" in out and "Left for a human" in out


# --- the command -------------------------------------------------------------


def test_main_runs_offline_on_a_directory_and_exits_nonzero_on_a_failure(ws: dict, capsys):
    ws["path"].write_text(ws["path"].read_text() + "amplicon_bp: 146\n")  # a duplicate key
    rc = curate.main(
        [
            str(ws["path"].parent),
            "--offline",
            "--retrieved",
            str(ws["retrieved"]),
            "--papers",
            str(ws["papers"]),
            "--fetch-list",
            str(ws["fetch_list"]),
        ]
    )
    assert rc == 1
    assert "FAIL" in capsys.readouterr().out


def test_main_needs_an_email_unless_offline(ws: dict):
    with pytest.raises(SystemExit):
        curate.main([str(ws["path"])])


def test_curate_is_a_stage_of_the_cli():
    from assaywatch.cli import STAGES

    assert STAGES["curate"][0] == "assaywatch.curate"
