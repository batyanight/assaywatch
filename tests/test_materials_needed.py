"""Tests for scripts/materials_needed.py, the list of gaps only a person can close.

This file exists because of S7. `needs_review` used to carry `DOI_MISSING`,
`NO_YEAR` and `TAXID_MISSING`, and this script read them to raise a row. Those
flags are gone - they restated fields on the same entry and went stale - so the
script derives the gap from the field instead. Nothing covered that logic, which
meant the replacement for the dropped flags could stop working and the only list
that tells a curator what to chase would quietly get shorter.
"""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest

from assaywatch.schema import Assay

ROOT = Path(__file__).resolve().parents[1]


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


mn = _load("materials_needed")

DOC = {
    "id": "TEST_assay",
    "name": "Test assay",
    "target": {"taxid": 109871, "taxon_name": "Batrachochytrium dendrobatidis", "gene": "ITS1"},
    "chemistry": "conventional",
    "oligos": {
        "forward": {"name": "F", "seq": "CCTTGATATAATACAGTGTGCCATATGTC"},
        "reverse": {"name": "R", "seq": "AGCCAAGAGATCCGTTGTCAAA"},
    },
    "amplicon_bp": 121,
    "citation": {"doi": "10.3354/dao060141", "design_year": 2004, "doi_verified": True},
    "use_context": ["wildlife"],
    "status": "draft",
    "source": {"notes_curator": None},
    "needs_review": None,
}


def doc(**changes) -> dict:
    d = copy.deepcopy(DOC)
    for dotted, value in changes.items():
        node = d
        parts = dotted.split(".")
        for p in parts[:-1]:
            node = node[p]
        node[parts[-1]] = value
    return d


def buckets(d: dict, *, papers: Path, verdicts=()) -> list[str]:
    """The buckets this one entry lands in, which is the script's whole output shape."""
    return [r["bucket"] for r in mn.rows_for(Assay.model_validate(d), d, list(verdicts), papers)]


@pytest.fixture
def papers(tmp_path) -> Path:
    """A papers/ holding the entry's own PDF, so `paper-pdf` is not the answer."""
    (tmp_path / "10.3354_dao060141.pdf").write_bytes(b"%PDF-1.4\n")
    return tmp_path


def test_a_complete_entry_needs_nothing(papers):
    assert buckets(doc(), papers=papers) == []


def test_a_missing_design_year_is_derived_not_flagged(papers):
    """The gap comes from `citation.design_year`, never from a stored flag.

    Two of the 18 entries that carried NO_YEAR had `design_year: 2011` on the
    same document: the year had been supplied and nobody cleared the flag.
    Asking the field cannot drift out of step with the field.
    """
    assert buckets(doc(**{"citation.design_year": None}), papers=papers) == ["year"]
    # And it is not reachable by writing the old flag back in.
    assert "year" not in buckets(
        doc(needs_review=[{"flag": "curation_decision_pending", "note": "no year"}]), papers=papers
    )


def test_a_missing_taxid_is_derived_and_names_the_taxon(papers):
    rows = mn.rows_for(Assay.model_validate(d := doc(**{"target.taxid": None})), d, [], papers)
    assert [r["bucket"] for r in rows] == ["taxid"]
    assert "Batrachochytrium dendrobatidis" in rows[0]["what_is_needed"]


def test_both_gaps_appear_separately(papers):
    """One row per gap per assay is the file's contract; two gaps are two rows."""
    assert sorted(buckets(doc(**{"citation.design_year": None, "target.taxid": None}), papers=papers)) == [
        "taxid",
        "year",
    ]


def test_a_missing_doi_is_covered_by_the_citation_buckets(papers):
    """DOI_MISSING needed no replacement: the citation buckets already asked.

    The bucket depends on what the entry *does* have, which is why a flag could
    never have carried it: a reference string naming PREDICT, a reference naming
    the lab, and nothing at all are three different requests of three different
    people.
    """
    assert buckets(
        doc(**{"citation.doi": None, "citation.reference": "PREDICT protocol P-001"}), papers=papers
    ) == ["citation"]
    assert buckets(
        doc(**{"citation.doi": None, "citation.reference": "WCS lab, unpublished"}), papers=papers
    ) == ["lab-record"]
    assert buckets(
        doc(**{"citation.doi": None, "citation.reference": "Smith 2009, J Virol"}), papers=papers
    ) == ["citation"]
    assert buckets(doc(**{"citation.doi": None}), papers=papers) == ["provenance"]


def test_a_figure_flag_asks_for_the_figure(papers):
    assert buckets(doc(needs_review=[{"flag": "oligos_read_from_figure"}]), papers=papers) == ["figure"]


def test_an_uncertain_sequence_also_asks_for_the_figure(papers):
    """Widened at S7, on purpose.

    The old filter named three strings, two of which became
    `oligos_read_from_figure`. The third, `PROBE_OMITTED_OCR_UNRELIABLE`, became
    `oligo_sequence_uncertain` along with a length discrepancy read by OCR - and
    a legible copy of the page is exactly what settles both.
    """
    assert buckets(doc(needs_review=[{"flag": "oligo_sequence_uncertain"}]), papers=papers) == ["figure"]


def test_one_figure_row_even_with_both_flags(papers):
    d = doc(needs_review=[{"flag": "oligos_read_from_figure"}, {"flag": "oligo_sequence_uncertain"}])
    assert buckets(d, papers=papers) == ["figure"]


def test_do_not_use_asks_for_a_decision_and_not_validated_does_not(papers):
    """The two are different requests, and only one of them is destructive.

    `do_not_use` means the source said so and someone must decide whether the
    entry survives. `not_validated` means nobody has run it, which is a reason
    to run it, not to delete it.
    """
    assert buckets(doc(needs_review=[{"flag": "do_not_use"}]), papers=papers) == ["decision"]
    assert buckets(doc(needs_review=[{"flag": "not_validated"}]), papers=papers) == []


def test_a_caveat_flag_asks_for_nothing(papers):
    """A recorded caveat is settled; this list is for what is still open."""
    for flag in ("nested_protocol", "oligos_modified", "cross_reactive", "amplicon_multimodal"):
        assert buckets(doc(needs_review=[{"flag": flag}]), papers=papers) == [], flag


def test_a_doi_with_no_pdf_asks_for_the_pdf(tmp_path):
    assert buckets(doc(), papers=tmp_path) == ["paper-pdf"]


def test_the_predict_supplement_bucket_only_appears_without_the_file(papers):
    d = doc(**{"source.notes_curator": f"Oligos from {mn.PREDICT_SUPPLEMENT}"})
    assert buckets(d, papers=papers) == ["predict-supplement"]
    (papers / mn.PREDICT_SUPPLEMENT_FILE).write_bytes(b"%PDF-1.4\n")
    assert buckets(d, papers=papers) == []
