"""Schema tests: each rule in schema.py has a case that must pass and one that must fail."""

import copy

import pytest
from pydantic import ValidationError

from assaywatch.review import CAVEAT, OPEN, ReviewFlag
from assaywatch.schema import Assay, Oligo, Status

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


def test_active_does_not_require_submitted_by():
    """Authorship is not evidence about the assay, so it cannot gate `active`.

    Dropped 2026-10-21. Once S7 stopped recorded caveats from blocking `active`,
    this field was the only thing blocking 167 of 208 entries - including all
    four remaining ROADMAP Phase 0 candidates - because the registry was
    bulk-imported by one curator and 207 of 208 leave it null.
    """
    a = Assay.model_validate(variant(submitted_by=None))
    assert a.status is Status.active
    assert a.submitted_by is None


def test_submitted_by_still_validates_when_a_submitter_sets_it():
    """Dropped from the gate, not from the schema: a real submission still records one."""
    assert Assay.model_validate(variant(submitted_by="A Contributor")).submitted_by == "A Contributor"
    with pytest.raises(ValidationError):
        Assay.model_validate(variant(submitted_by=42))


def test_active_still_requires_everything_that_is_about_the_assay():
    """The gate must not have been loosened further than the one field.

    Pinned as a set rather than one case each, so dropping another precondition
    fails here instead of silently widening what `active` promises.
    """
    for change, expected in [
        ({"target.taxid": None}, "target.taxid"),
        ({"citation.doi": None}, "citation.doi"),
        ({"citation.doi_verified": False}, "doi_verified"),
        ({"citation.design_year": None}, "design_year"),
    ]:
        with pytest.raises(ValidationError, match=expected):
            Assay.model_validate(variant(**change))


def test_active_rejects_open_review_flags():
    with pytest.raises(ValidationError, match="open questions"):
        Assay.model_validate(variant(needs_review=[{"flag": "do_not_use"}]))


def test_active_accepts_a_recorded_caveat():
    """A settled, disclosed caveat is not a defect and must not hold an entry at draft.

    This is the half of the rule that the pre-2026-10-21 `needs_review` got
    wrong: it refused any non-empty list, so `nested_protocol` - a permanent
    property of a sound entry - blocked `active` forever.
    """
    a = Assay.model_validate(variant(needs_review=[{"flag": "nested_protocol"}]))
    assert a.status is Status.active
    assert [i.flag for i in a.needs_review] == [ReviewFlag.nested_protocol]
    assert a.open_review == []


def test_active_names_the_open_flag_and_not_the_caveat_beside_it():
    """The message has to say which flag is blocking, or it sends a curator hunting."""
    with pytest.raises(ValidationError) as e:
        Assay.model_validate(
            variant(
                needs_review=[
                    {"flag": "nested_protocol"},
                    {"flag": "citation_unresolved", "note": "no citable source"},
                ]
            )
        )
    assert "citation_unresolved" in str(e.value)
    assert "nested_protocol" not in str(e.value)


def test_a_flag_outside_the_vocabulary_is_refused():
    """The whole point of S7: the field can no longer absorb a new free string."""
    with pytest.raises(ValidationError, match="flag"):
        Assay.model_validate(variant(status="draft", needs_review=[{"flag": "DOI_UNVERIFIED"}]))
    with pytest.raises(ValidationError, match="flag"):
        Assay.model_validate(
            variant(status="draft", needs_review=[{"flag": "SCOPE_HUMMINGBIRD_AVIPOX_CLADE_ONLY"}])
        )


def test_a_bare_string_is_refused():
    """The old shape must fail loudly, not coerce into something plausible."""
    with pytest.raises(ValidationError):
        Assay.model_validate(variant(status="draft", needs_review=["nested_protocol"]))


def test_an_unknown_key_in_a_review_item_is_refused():
    with pytest.raises(ValidationError):
        Assay.model_validate(
            variant(status="draft", needs_review=[{"flag": "nested_protocol", "reason": "x"}])
        )


def test_curation_decision_pending_needs_a_note():
    """A catch-all with no note answers nothing a filter would ask."""
    with pytest.raises(ValidationError, match="requires a note"):
        Assay.model_validate(variant(status="draft", needs_review=[{"flag": "curation_decision_pending"}]))
    with pytest.raises(ValidationError, match="requires a note"):
        Assay.model_validate(
            variant(status="draft", needs_review=[{"flag": "curation_decision_pending", "note": "   "}])
        )
    ok = Assay.model_validate(
        variant(
            status="draft",
            needs_review=[{"flag": "curation_decision_pending", "note": "whether to split by host"}],
        )
    )
    assert ok.needs_review[0].note == "whether to split by host"


def test_a_flag_may_not_repeat():
    """Two items with one flag are two halves of one note, and break any count by flag."""
    with pytest.raises(ValidationError, match="repeats cross_reactive"):
        Assay.model_validate(
            variant(
                status="draft",
                needs_review=[
                    {"flag": "cross_reactive", "note": "detects PDV"},
                    {"flag": "cross_reactive", "note": "detects PPRV"},
                ],
            )
        )


def test_every_flag_is_open_or_a_caveat_and_never_both():
    """OPEN and CAVEAT partition the vocabulary; a flag in neither is silently inert."""
    assert OPEN | CAVEAT == frozenset(ReviewFlag)
    assert not OPEN & CAVEAT


def test_a_note_is_optional_where_the_flag_is_the_whole_finding():
    a = Assay.model_validate(variant(status="draft", needs_review=[{"flag": "cross_reactive"}]))
    assert a.needs_review[0].note is None


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


def test_a_probe_may_be_shorter_than_a_primer():
    """Published MGB probes run 13-14 nt (Haynes 2023 prints several), so the
    probe floor is 12 where a primer's is 15. Refusing them refuses the assay."""
    for seq in ("CGAGTCGAACAAA", "CGAGTCGAACAA"):  # 13 and 12 nt
        a = Assay.model_validate(variant(**{"oligos.probe.seq": seq}))
        assert a.oligos.probe.seq == seq


def test_the_probe_floor_still_catches_a_typo():
    with pytest.raises(ValidationError, match="length 11 outside 12-40"):
        Assay.model_validate(variant(**{"oligos.probe.seq": "CGAGTCGAACA"}))


def test_a_primer_still_needs_fifteen():
    """The lower floor is for probes only: a primer is searched along the whole
    record, where a 14-mer with a mismatch budget chance-matches freely."""
    with pytest.raises(ValidationError, match="outside 15-40 nt for a primer"):
        Assay.model_validate(variant(**{"oligos.forward.seq": "CCTTGATATAATAC"}))
    with pytest.raises(ValidationError, match="outside 15-40 nt for a primer"):
        Assay.model_validate(variant(**{"oligos.reverse.seq": "AGCCAAGAGATCCG"}))


def test_an_alternate_takes_the_floor_of_its_orientation():
    short = "CGAGTCGAACAAA"  # 13 nt
    ok = variant()
    ok["oligos"]["alternates"] = [{"name": "P2", "seq": short, "orientation": "probe"}]
    Assay.model_validate(ok)
    bad = variant()
    bad["oligos"]["alternates"] = [{"name": "F2", "seq": short, "orientation": "forward"}]
    with pytest.raises(ValidationError, match="for a primer"):
        Assay.model_validate(bad)


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


def test_tail_is_left_out_of_matching():
    from assaywatch.schema import Oligo

    o = Oligo(seq="GGATGTCGACATGCACAAGGAAATCC", tail_5prime="ggatgtcgac")
    assert o.matching_seq == "ATGCACAAGGAAATCC"


def test_tail_must_be_the_five_prime_end():
    import pytest
    from pydantic import ValidationError

    from assaywatch.schema import Oligo

    with pytest.raises(ValidationError):
        Oligo(seq="GGATGTCGACATGCACAAGGAAATCC", tail_5prime="GTCGAC")


def test_tailed_oligo_may_bind_over_14_nt():
    """BUN-S3-R (Briese 2007 Table 1) is a 6 nt cloning tail plus 14 nt that bind.

    A published primer sits one base below the untailed oligo floor, so the
    floor for a declared tail's binding part is 14, not 15. Guards against
    someone 'tidying' OLIGO_MIN_BINDING back up and silently rejecting the
    orthobunyavirus assays.
    """
    o = Oligo(name="BUN-S3-R", seq="CGCGCCAGTAGTGTGCTACC", tail_5prime="CGCGCC")
    assert o.tail_5prime == "CGCGCC"
    assert len(o.seq) - len(o.tail_5prime) == 14
    with pytest.raises(ValidationError, match="below the 14 nt floor"):
        Oligo(name="too-short", seq="CGCGCCAGTAGTGTGCTAC", tail_5prime="CGCGCC")


def test_query_may_not_begin_with_not():
    """A leading NOT is silently inverted by Entrez once build_query parenthesises it.

    Measured 2026-10-04: `txid562[Organism:exp] AND (NOT ribosomal[Title])` returns
    16,733 records, exactly the same as `AND (ribosomal[Title])`. Scoping an assay
    that way hands it the records it was meant to exclude, with no error.
    """
    from assaywatch.schema import Target

    with pytest.raises(ValidationError, match="starts with NOT"):
        Target(taxid=10492, query="NOT (txid3432136[Organism:exp])")
    with pytest.raises(ValidationError, match="starts with NOT"):
        Target(taxid=10492, query="  (NOT txid3432136[Organism:exp])")
    # Anchored form: the NOT has a left operand, so Entrez applies it.
    t = Target(taxid=10492, query="txid10492[Organism:exp] NOT (txid3432136[Organism:exp])")
    assert t.query.startswith("txid10492")
    # A mid-query NOT is correct and must keep working: fourteen registry entries use it.
    Target(taxid=209, query='(16S[Title]) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]')


def test_oligos_designed_here_is_nullable_and_defaults_to_unknown():
    """The field that keeps 'read the sequences from' apart from 'designed them'.

    Conflating those scoped the ranavirus MCP assay away from the fish
    ranaviruses on 2026-10-04, because its citation was a box-turtle study while
    its oligos are Mao et al. 1997's pan-ranavirus pair. The default must be
    None, not True: an unexamined entry has to read as unknown rather than as
    vouched for.
    """
    from assaywatch.schema import Citation

    assert Citation().oligos_designed_here is None
    assert Citation(oligos_designed_here=False).oligos_designed_here is False
    assert Citation(oligos_designed_here=True).oligos_designed_here is True


def test_a_declared_range_replaces_the_scalar_size_and_never_joins_it():
    """ORTHOPOXVIRUS ATI reads species off product LENGTH, 540-1700 bp.

    A scalar cannot gate that, and before `amplicon_bp_range` it was the one
    entry `declared_tolerance` left unconstrained.
    """
    ok = Assay.model_validate(variant(amplicon_bp=None, amplicon_bp_range=[540, 1700]))
    assert ok.amplicon_bp_range == [540, 1700]
    with pytest.raises(ValidationError, match="not both"):
        Assay.model_validate(variant(amplicon_bp=800, amplicon_bp_range=[540, 1700]))
    with pytest.raises(ValidationError, match="ascend"):
        Assay.model_validate(variant(amplicon_bp=None, amplicon_bp_range=[1700, 540]))
    with pytest.raises(ValidationError):
        Assay.model_validate(variant(amplicon_bp=None, amplicon_bp_range=[540, 99999]))


def _ati_kwargs(**over):
    """The shape of an assay that identifies the species by product length."""
    base = dict(
        id="ORTHOPOX_ATI_test",
        name="ATI test",
        target={"taxid": 10242, "gene": "ATI", "genome_type": "dsDNA", "taxon_name": "Orthopoxvirus"},
        chemistry="conventional",
        oligos={"forward": {"seq": "AATACAAGGAGGATCT"}, "reverse": {"seq": "CTTAACTTTTTCTTTCTC"}},
        amplicon_bp_range=[540, 1700],
        citation={"doi": "10.1016/S0166-0934(96)02155-6"},
    )
    base.update(over)
    return base


def test_species_sizes_allow_several_bands_for_one_species():
    a = Assay(
        **_ati_kwargs(
            species_sizes=[
                {"taxid": 3431483, "bp": [1535, 1545], "n_records": 9113, "note": "clade IIb"},
                {"taxid": 3431483, "bp": [1067, 1067], "n_records": 1981, "note": "clade I"},
            ]
        )
    )
    assert [s.bp for s in a.species_sizes] == [[1535, 1545], [1067, 1067]]


def test_species_sizes_need_the_declared_range():
    """Without amplicon_bp_range the assay is not claiming its length varies by species."""
    kwargs = _ati_kwargs(species_sizes=[{"taxid": 10245, "bp": [1587, 1615], "n_records": 130}])
    del kwargs["amplicon_bp_range"]
    kwargs["amplicon_bp"] = 1600
    with pytest.raises(ValidationError, match="species_sizes needs amplicon_bp_range"):
        Assay(**kwargs)


def test_a_band_outside_the_declared_range_is_rejected():
    with pytest.raises(ValidationError, match="outside amplicon_bp_range"):
        Assay(**_ati_kwargs(species_sizes=[{"taxid": 10245, "bp": [1587, 1900], "n_records": 2}]))


def test_a_band_must_ascend():
    with pytest.raises(ValidationError, match="must ascend"):
        Assay(**_ati_kwargs(species_sizes=[{"taxid": 10245, "bp": [1615, 1587], "n_records": 2}]))


def test_the_committed_json_schema_matches_the_models():
    """`schema.py`'s docstring has promised `Assay.model_json_schema()` as
    documentation for contributors since it was written, and nothing emitted it,
    so the registry's only machine-readable contract lived in Python source. A
    reuser of registry/*.yaml outside Python had to read pydantic or 208 files.
    Committed now, and checked here so it cannot drift from the models."""
    import json
    from pathlib import Path

    from assaywatch.schema import Assay

    root = Path(__file__).resolve().parents[1]
    committed = root / "registry" / "schema.json"
    assert committed.exists(), "run: python -m assaywatch.validate --emit-schema registry/schema.json"
    on_disk = json.loads(committed.read_text())
    live = Assay.model_json_schema()
    assert on_disk["properties"].keys() == live["properties"].keys()
    assert on_disk["$comment"].startswith("Generated from assaywatch.schema")
    # and the licence pointer, since this file is the data's published contract
    assert "LICENSE-registry" in on_disk["$comment"]


# --- only a verified DOI goes live ----------------------------------------


def _write_entry(dir_, **changes):
    import yaml

    d = variant(**changes)
    d["status"] = "draft"
    (dir_ / f"{d['id']}.yaml").write_text(yaml.safe_dump(d, sort_keys=False))


@pytest.mark.parametrize(
    "changes",
    [{"citation.doi_verified": False}, {"citation.doi": None, "citation.doi_verified": False}],
    ids=["unverified", "no-doi"],
)
def test_the_registry_refuses_an_entry_without_a_verified_doi(tmp_path, changes):
    from assaywatch.validate import main

    _write_entry(tmp_path, **changes)
    assert main([str(tmp_path), "--quiet"]) == 1
    # pending/ holds exactly these, against the same schema.
    assert main([str(tmp_path), "--quiet", "--pending"]) == 0


def test_a_verified_doi_is_live(tmp_path):
    from assaywatch.validate import main

    _write_entry(tmp_path)
    assert main([str(tmp_path), "--quiet"]) == 0


def test_the_seed_list_fields_cannot_come_back():
    for field in ("spreadsheet", "rows", "positive_control"):
        with pytest.raises(ValidationError):
            Assay.model_validate(variant(**{"source": {field: "x"}}))


def test_nothing_in_pending_is_live_and_nothing_in_registry_is_pending():
    from pathlib import Path

    from assaywatch.validate import iter_files, load_assay, not_live_because

    root = Path(__file__).resolve().parents[1]
    assert all(not_live_because(load_assay(p)) is None for p in iter_files(root / "registry"))
    assert all(not_live_because(load_assay(p)) for p in iter_files(root / "pending"))
