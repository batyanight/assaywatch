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
