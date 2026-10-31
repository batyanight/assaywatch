"""`target.title_requires`: screening only records whose FASTA description matches.

WHY THIS EXISTS. NCBI stopped assigning influenza subtype taxids to new deposits,
so a query built on them goes blind: the seven H3Nx taxids AND the HA terms
returned ZERO records for 2024-2026 on 2026-10-30, where dropping the subtype
restriction returned 95,155. The consequence was live and unnoticed -- the H5
Tsukamoto archive's newest deposit was 2021 and H7's was 2020, so neither assay
could show recent drift by construction.

The subtype survives in the record's own description, inside the strain name
(`Influenza A virus (A/Wisconsin/52/2026(H3N2)) segment 4 ...`): 62,372 of 67,655
recent records carry it. A bare `H3N2` Entrez term finds 33,737 of them, but only
97.4% are really H3N2 -- the other 862 are H1N1, H10N5 and H3 with no N type,
matched because the subtype is mentioned somewhere in the record. For a
subtype-specific assay an off-subtype record scores as a failure, so leaving them
in the denominator would manufacture a decline. Hence: narrow with the query,
then make it exact here.

Full record: docs/journal/2026-10-30-set3-scored.md.
"""

from __future__ import annotations

from pathlib import Path

from assaywatch.fasta import read_fasta, read_fasta_titled
from assaywatch.screen import title_allows

H3 = "Influenza A virus (A/Wisconsin/52/2026(H3N2)) segment 4 hemagglutinin (HA) gene, complete cds"
H1 = "Influenza A virus (A/Tempe/S330/2023(H1N1)) segment 4 hemagglutinin (HA) gene, complete cds"
BARE = "Influenza A virus A/canine/Madison/5/2015 HA gene for hemagglutinin, complete cds"


def _fasta(tmp_path: Path) -> Path:
    p = tmp_path / "titled.fasta"
    p.write_text(f">AB1.1 {H3}\nACGT\n>AB2.1 {H1}\nACGTA\n>AB3.1 {BARE}\nACGTAA\n")
    return p


class _Target:
    def __init__(self, title_requires=None):
        self.title_requires = title_requires


class _Assay:
    def __init__(self, title_requires=None):
        self.target = _Target(title_requires)


def test_the_titled_reader_yields_the_description_the_plain_one_drops(tmp_path: Path):
    """`read_fasta` keeps its two-value shape; the titled reader adds a third.

    `read_fasta` has about twenty callers that unpack exactly two values, several
    of them `dict(read_fasta(...))`. Widening its return would have broken all of
    them for the benefit of one, so the parser gained a second view instead and
    the old name delegates to it.
    """
    p = _fasta(tmp_path)
    assert list(read_fasta(p)) == [("AB1.1", "ACGT"), ("AB2.1", "ACGTA"), ("AB3.1", "ACGTAA")]
    titled = list(read_fasta_titled(p))
    assert [r[0] for r in titled] == ["AB1.1", "AB2.1", "AB3.1"]
    assert [r[1] for r in titled] == ["ACGT", "ACGTA", "ACGTAA"]
    assert titled[0][2] == H3
    assert titled[2][2] == BARE


def test_a_record_carrying_the_wanted_subtype_is_screened():
    assert title_allows(_Assay(["H3N2"]), H3)


def test_a_record_carrying_a_different_subtype_is_not():
    """The case the whole mechanism exists for: an H1N1 record reaching an H3 assay
    would score as a failure, and enough of them read as drift."""
    assert not title_allows(_Assay(["H3N2"]), H1)


def test_a_record_carrying_no_subtype_at_all_is_not_screened():
    """Excluded, deliberately, and this is the decision most worth stating.

    For an assay restricted to a subtype we cannot know an untyped record is the
    target. Including it would put a record of unknown subtype in the denominator,
    where a specific assay failing on it reads as drift. Excluding it shrinks the
    denominator instead, which is the conservative direction and shows up honestly
    as a wider interval rather than as a decline. 7.8% of recent records are
    untyped this way, so this is not a rounding decision.
    """
    assert not title_allows(_Assay(["H3N2"]), BARE)


def test_an_assay_with_no_requirement_screens_everything():
    """The guard that the other 214 entries did not change. Absent, empty and None
    all mean "screen every record", so only an entry that opts in is filtered."""
    for req in (None, []):
        for desc in (H3, H1, BARE, ""):
            assert title_allows(_Assay(req), desc)


def test_matching_ignores_case_and_accepts_any_of_several():
    """Case-insensitive because the description's case is NCBI's to change, and any
    of several because H5 and H7 each cover the subtypes their seven taxids named."""
    assert title_allows(_Assay(["h3n2"]), H3)
    assert title_allows(_Assay(["H5N1", "H5N8", "H3N2"]), H3)
    assert not title_allows(_Assay(["H5N1", "H5N8"]), H3)


def test_a_record_with_no_description_is_excluded_when_a_requirement_is_set():
    """A header that is only an accession carries no subtype, so it is unknown and
    excluded by the same rule as an untyped strain name."""
    assert not title_allows(_Assay(["H3N2"]), "")
    assert title_allows(_Assay(None), "")


def test_a_subtype_inside_a_strain_identifier_does_not_match():
    """The bug a plain substring had, found by measuring rather than by reading.

    GenBank strain identifiers carry the same letter-digit pairs as subtypes, so
    an H7 assay matching a bare "H7" would take in this H1N1 record -- `BBBH74562`
    contains "H7" -- and score it as a failure. Over 232,161 real influenza
    headers the left boundary removes 50 such collisions for H7, 72 for H5 and 48
    for H3.
    """
    h1_with_h7_in_its_strain_code = (
        "Influenza A virus (A/New Jersey/GKISBBBH74562/2026(H1N1)) segment 4 hemagglutinin (HA) gene"
    )
    assert not title_allows(_Assay(["H7"]), h1_with_h7_in_its_strain_code)
    assert not title_allows(
        _Assay(["H5"]), "Influenza A virus (A/New York/GKISBBBH56238/2026(H3N2)) segment 4"
    )
    assert title_allows(_Assay(["H1"]), h1_with_h7_in_its_strain_code)


def test_both_title_formats_satisfy_the_boundary():
    """The subtype is written two ways and the rule must accept both, which is why
    anchoring on the opening parenthesis was rejected: it missed 28 records of the
    44,627 in the H3 archive, all of them genuinely H3N2."""
    parenthesised = "Influenza A virus (A/Wisconsin/52/2026(H3N2)) segment 4 hemagglutinin (HA) gene"
    after_a_space = "Influenza A virus H3N2 partial Hemagglutinin (HA) gene for Hemagglutinin"
    assert title_allows(_Assay(["H3"]), parenthesised)
    assert title_allows(_Assay(["H3"]), after_a_space)


def test_h3_matches_every_n_type_and_the_untyped_parenthesised_form():
    """`H3` rather than the seven H3Nx subtypes, because the archive also holds
    `(H3Nx)` and bare `(H3)` records, which are H3 and belong in the denominator.
    No right boundary, so "H3" matches "H3N2"."""
    for form in ("(H3N2)", "(H3N8)", "(H3Nx)", "(H3)"):
        assert title_allows(_Assay(["H3"]), f"Influenza A virus (A/x/1/2026{form}) segment 4")
    # and it must not reach a neighbouring subtype
    assert not title_allows(_Assay(["H3"]), "Influenza A virus (A/x/1/2026(H13N2)) segment 4")
