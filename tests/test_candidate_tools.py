"""Tests for extract_candidate_oligos.py and check_primer_provenance.py.

Both sit on top of the verifier's paper index, and both were changed when the
index learned to read `.txt` and `.xml` as well as PDFs. The review found each
had picked up a flaw from that: one counted a DOI twice when it was held as two
files, the other reported `name-not-found` against text that had lost its tables.
"""

from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


extract = load("extract_candidate_oligos")
prov = load("check_primer_provenance")

F = "GCGGCCAACCAGTTTAACGCAA"
R = "ATTGCGCTGGAACCTTGTCAAG"
RICH = f"Methods. Forward primer 5'-{F}-3' and reverse primer 5'-{R}-3' were used at 0.4 uM."
POOR = "Methods. Samples were screened by PCR as described previously. See Table 1."


def tsv(path: Path) -> list[dict]:
    return list(csv.DictReader(path.open(), delimiter="\t"))


# --- the extractor ----------------------------------------------------------


def test_a_doi_held_as_two_files_is_extracted_once(tmp_path, capsys):
    """It walked every file, so a DOI held as both an .xml and a .txt listed each
    sequence twice and doubled the per-paper count: '4 candidate oligos from 1
    papers' for a paper that prints two primers."""
    d = tmp_path / "papers"
    d.mkdir()
    (d / "10.7777_dup.1.txt").write_text(RICH)
    (d / "10.7777_dup.1.xml").write_text(f"<article><p>{RICH}</p></article>")
    out = tmp_path / "cand.tsv"
    assert extract.main(["--pdf-dir", str(d), "--out", str(out)]) == 0
    rows = tsv(out)
    assert sorted(r["sequence"] for r in rows) == sorted([F, R])
    assert "2 candidate oligos from 1 papers" in capsys.readouterr().out


def test_a_doi_is_not_both_a_candidate_source_and_a_paper_with_no_sequences(tmp_path, capsys):
    """When one file prints the table and its sibling is prose, the DOI used to be
    listed under 'yielded NO readable sequences' as well, telling a curator the
    paper needed eyes when its sibling had already produced the candidates."""
    d = tmp_path / "papers"
    d.mkdir()
    (d / "10.7777_split.2.xml").write_text(f"<article>{POOR}</article>")
    (d / "10.7777_split.2.txt").write_text(RICH)
    out = tmp_path / "cand.tsv"
    extract.main(["--pdf-dir", str(d), "--out", str(out)])
    printed = capsys.readouterr().out
    assert len(tsv(out)) == 2
    assert "yielded NO readable sequences" not in printed, printed


def test_a_paper_whose_every_file_is_prose_is_still_reported_as_needing_eyes(tmp_path, capsys):
    """The case the report exists for must survive de-duplication."""
    d = tmp_path / "papers"
    d.mkdir()
    (d / "10.7777_image.3.txt").write_text(POOR)
    extract.main(["--pdf-dir", str(d), "--out", str(tmp_path / "c.tsv")])
    printed = capsys.readouterr().out
    assert "yielded NO readable sequences" in printed and "10.7777/image.3" in printed


# --- the provenance check ---------------------------------------------------


def _registry(tmp_path):
    reg = tmp_path / "registry"
    reg.mkdir(exist_ok=True)
    src = ROOT / "registry" / "PD_WNS_ITS1_Shuey_2014.yaml"
    (reg / src.name).write_text(src.read_text())
    return reg, yaml.safe_load(src.read_text())


def _verdicts(tmp_path, paper_text) -> dict[str, str]:
    """{oligo name: verdict} from running the provenance check over one paper."""
    reg, _ = _registry(tmp_path)
    papers = tmp_path / "papers"
    papers.mkdir(exist_ok=True)
    (papers / "10.1128_aem.02897-13.txt").write_text(paper_text)
    out = tmp_path / "prov.tsv"
    prov.main(["--registry", str(reg), "--pdf-dir", str(papers), "--tsv", str(out)])
    return {r["oligo_name"]: r["verdict"] for r in tsv(out)}


def test_a_name_missing_from_a_text_that_lost_its_tables_is_not_name_not_found(tmp_path):
    """`name-not-found` means 'this paper never uses that name, so the oligo may
    not be from it'. Said of a text that printed one oligo-like run, it is a fact
    about the text: 33 of 51 such rows over the PMC texts were papers like this."""
    got = _verdicts(tmp_path, f"The reverse primer was 5'-{R}-3'. Other primers are in Table 1.")
    assert set(got.values()) == {"no-oligos"}, got
    assert len(got) == 3  # forward, reverse and probe were all judged


def test_a_name_missing_from_a_methods_paper_is_still_name_not_found(tmp_path):
    """The signal survives where it means something: the text printed enough
    oligos to be a methods paper and still never mentions the stored names."""
    got = _verdicts(tmp_path, RICH + " Primer set 5'-CCTTGGTTAAGGCCTTGGAACCTT-3' was also used.")
    assert set(got.values()) == {"name-not-found"}, got


def test_a_name_that_is_found_is_judged_on_its_sentence_not_on_the_floor(tmp_path):
    """A thin text that DOES contain a stored name still gets the ordinary
    analysis for THAT oligo, while the oligos whose names are absent from the same
    text are the ones the floor reclassifies."""
    _, d = _registry(tmp_path)
    fwd, rev = d["oligos"]["forward"]["name"], d["oligos"]["reverse"]["name"]
    got = _verdicts(tmp_path, f"We designed {fwd} in this study. Remaining primers are in Table 1.")
    assert got[fwd] == "claimed-here", got  # found: judged on its sentence
    assert got[rev] == "no-oligos", got  # absent from a thin text: the floor


# ==========================================================================
# Added after the second review
# ==========================================================================


def test_a_paper_that_cites_another_doi_first_is_not_dropped(tmp_path, capsys):
    """The one-file-per-DOI rule skipped any file whose FIRST printed DOI was held by a
    different file. An erratum, or any paper that cites a DOI before printing its own,
    lost its candidates without a trace: not in the output, not in the 'no readable
    sequences' list, and `--doi <its own DOI>` found nothing."""
    d = tmp_path / "papers"
    d.mkdir()
    (d / "a_paper.txt").write_text("doi:10.1111/aaa.1 " + RICH)
    other_f, other_r = "TTCAAGGAACTCAGTAAGATCAACC", "CCTTGGTTAAGGCCTTGGAACCTTGG"
    (d / "b_erratum.txt").write_text(
        f"Erratum to doi:10.1111/aaa.1 . This article doi:10.2222/bbb.2 . Forward 5'-{other_f}-3' reverse 5'-{other_r}-3'."
    )
    out = tmp_path / "cand.tsv"
    assert extract.main(["--pdf-dir", str(d), "--all", "--out", str(out)]) == 0
    by_file = {}
    for r in tsv(out):
        by_file.setdefault(r["pdf"], []).append(r["doi"])
    assert set(by_file) == {"a_paper.txt", "b_erratum.txt"}, by_file
    assert set(by_file["b_erratum.txt"]) == {"10.2222/bbb.2"}, (
        "labelled with its own DOI, not the one it cites"
    )
    # and it is findable by its own DOI
    only = tmp_path / "only.tsv"
    extract.main(["--pdf-dir", str(d), "--all", "--doi", "10.2222/bbb.2", "--out", str(only)])
    assert {r["pdf"] for r in tsv(only)} == {"b_erratum.txt"}


def test_a_sibling_file_that_prints_something_the_winner_does_not_is_kept_and_noted(tmp_path, capsys):
    """Copies of one paper are skipped; two files that merely share a DOI are not. A file
    NAMED for the DOI holds it even when it prints nothing (a PDF whose table is an image),
    and an unnamed download citing the same DOI with a readable table is not a copy of it:
    both are listed, and the output says they share the DOI."""
    d = tmp_path / "papers"
    d.mkdir()
    (d / "10.7777_both.4.txt").write_text(POOR)  # named, so it holds the DOI, and yields nothing
    (d / "downloaded.txt").write_text("doi:10.7777/both.4 " + RICH)
    out = tmp_path / "cand.tsv"
    extract.main(["--pdf-dir", str(d), "--out", str(out)])
    printed = capsys.readouterr().out
    assert {r["pdf"] for r in tsv(out)} == {"downloaded.txt"}
    assert sorted(r["sequence"] for r in tsv(out)) == sorted([F, R])
    assert "downloaded.txt and 10.7777_both.4.txt both claim 10.7777/both.4" in printed, printed


def test_a_copy_that_adds_nothing_is_skipped_and_counted(tmp_path, capsys):
    d = tmp_path / "papers"
    d.mkdir()
    (d / "10.7777_copy.5.txt").write_text(RICH)
    (d / "downloaded.txt").write_text("doi:10.7777/copy.5 " + RICH)
    out = tmp_path / "cand.tsv"
    extract.main(["--pdf-dir", str(d), "--out", str(out)])
    printed = capsys.readouterr().out
    assert {r["pdf"] for r in tsv(out)} == {"10.7777_copy.5.txt"}
    assert "1 files skipped as copies" in printed, printed


def test_doi_of_prefers_the_doi_a_file_holds_that_it_prints_first(tmp_path):
    text = "Erratum to doi:10.1111/aaa.1 . This article doi:10.2222/bbb.2 ."
    path = tmp_path / "x.txt"
    assert extract.doi_of(path, text, ["10.2222/bbb.2"]) == "10.2222/bbb.2"
    assert extract.doi_of(path, text, None) == "10.1111/aaa.1"  # holds nothing: earliest printed
    assert extract.doi_of(path, "no doi here", None) == ""
    assert extract.doi_of(tmp_path / "10.5555_named.9.txt", text, ["10.2222/bbb.2"]) == "10.5555/named.9"


# --- provenance: short names ------------------------------------------------------


AVIPOX = (
    "Primer 1F (5'-TCC TTG TAA AAG CGA TAC AGG AA-3') and primer 1R () produce a 234 bp fragment within "
    "which lies the Pox1 probe (5'-CAG CGT GAT GAA GAC GCT AA-3'). The real-time PCR assays contained "
    "0.4 uM primer 1F, 0.4 uM primer 1R and 0.4 uM Pox1 probe."
)


def test_a_two_character_name_is_found_when_the_paper_uses_it(tmp_path):
    """`find_name` returned [] for any name under four characters, so the avipox
    entry's `1F` and `1R` read `name-not-found` ('the oligo may not be from this paper')
    against a paper whose Methods use both, twice."""
    reg = tmp_path / "registry"
    reg.mkdir()
    src = ROOT / "registry" / "AVIPOXVIRUS_dsDNA_4b_core_Farias_2010.yaml"
    (reg / src.name).write_text(src.read_text())
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "10.1371_journal.pone.0010745.txt").write_text(AVIPOX)
    out = tmp_path / "prov.tsv"
    prov.main(["--registry", str(reg), "--pdf-dir", str(papers), "--tsv", str(out)])
    got = {r["oligo_name"]: r for r in tsv(out)}
    assert got["1F"]["verdict"] != "name-not-found" and got["1R"]["verdict"] != "name-not-found", got
    assert "short name" in got["1F"]["evidence"] or got["1F"]["verdict"] == "no-signal"


def test_a_one_character_name_is_reported_as_too_short_not_as_missing(tmp_path):
    reg = tmp_path / "registry"
    reg.mkdir()
    src = ROOT / "registry" / "PD_WNS_ITS1_Shuey_2014.yaml"
    d = yaml.safe_load(src.read_text())
    d["oligos"]["forward"]["name"] = "F"
    (reg / src.name).write_text(yaml.safe_dump(d))
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "10.1128_aem.02897-13.txt").write_text(RICH)
    out = tmp_path / "prov.tsv"
    prov.main(["--registry", str(reg), "--pdf-dir", str(papers), "--tsv", str(out)])
    got = {r["slot"]: r["verdict"] for r in tsv(out)}
    assert got["forward"] == "name-too-short", got
