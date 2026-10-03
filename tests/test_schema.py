"""Schema tests: each rule in schema.py has a case that must pass and one that must fail."""

import copy

import pytest
from pydantic import ValidationError

from assaywatch.schema import Assay

GOOD = {
    "id": "TEST_assay",
    "name": "Test assay",
    "target": {
        "taxid": 109871,
        "taxon_name": "Batrachochytrium dendrobatidis",
        "gene": "ITS1",
        "genome_type": "dsDNA",
    },
    "chemistry": "mgb",
    "oligos": {
        "forward": {"name": "F", "seq": "CCTTGATATAATACAGTGTGCCATATGTC"},
        "reverse": {"name": "R", "seq": "AGCCAAGAGATCCGTTGTCAAA"},
        "probe": {"name": "P", "seq": "CGAGTCGAACAAAAT", "reporter": "FAM", "quencher": "MGB-NFQ"},
    },
    "amplicon_bp": 121,
    "citation": {"doi": "10.3354/dao060141", "design_year": 2004, "doi_verified": True},
    "use_context": ["wildlife"],
    "submitted_by": "tester",
    "status": "active",
}


def variant(**changes):
    d = copy.deepcopy(GOOD)
    for dotted, value in changes.items():
        node = d
        parts = dotted.split(".")
        for p in parts[:-1]:
            node = node[p]
        node[parts[-1]] = value
    return d


def test_good_active_validates():
    a = Assay.model_validate(GOOD)
    assert a.oligos.probe.reporter == "FAM"


def test_draft_may_leave_provenance_null():
    Assay.model_validate(
        variant(
            **{
                "status": "draft",
                "target.taxid": None,
                "citation.doi": None,
                "citation.design_year": None,
                "submitted_by": None,
            }
        )
    )


def test_active_requires_taxid_and_doi():
    with pytest.raises(ValidationError, match="target.taxid"):
        Assay.model_validate(variant(**{"target.taxid": None}))
    with pytest.raises(ValidationError, match="citation.doi"):
        Assay.model_validate(variant(**{"citation.doi": None}))
    with pytest.raises(ValidationError, match="doi_verified"):
        Assay.model_validate(variant(**{"citation.doi_verified": False}))


def test_active_rejects_open_review_flags():
    with pytest.raises(ValidationError, match="needs_review"):
        Assay.model_validate(variant(needs_review=["DOI_UNVERIFIED"]))


@pytest.mark.parametrize(
    "seq,msg",
    [
        ("CGAGTCGAACAAAAI", "non-IUPAC"),  # inosine must be N
        ("CGAGTCGAAC", "length"),  # too short
        ("A" * 41, "length"),  # too long
        ("CGAGTCG AACAAAAT", "non-IUPAC"),  # whitespace
    ],
)
def test_bad_oligo_sequences(seq, msg):
    with pytest.raises(ValidationError, match=msg):
        Assay.model_validate(variant(**{"oligos.forward.seq": seq}))


def test_sequence_is_uppercased():
    a = Assay.model_validate(variant(**{"oligos.forward.seq": "ccttgatataatacagtgtgccatatgtc"}))
    assert a.oligos.forward.seq.isupper()


def test_probe_chemistry_consistency():
    with pytest.raises(ValidationError, match="no probe"):
        d = variant()
        d["oligos"].pop("probe")
        Assay.model_validate(d)
    with pytest.raises(ValidationError, match="primers-only"):
        Assay.model_validate(variant(chemistry="conventional"))


def test_doi_shape():
    with pytest.raises(ValidationError, match="DOI must look like"):
        Assay.model_validate(variant(**{"citation.doi": "https://doi.org/10.3354/dao060141"}))


def test_unknown_key_rejected():
    with pytest.raises(ValidationError, match="Extra inputs"):
        Assay.model_validate(variant(**{"target.taxon_nam": "typo"}))


def test_amplicon_range():
    with pytest.raises(ValidationError):
        Assay.model_validate(variant(amplicon_bp=20))
