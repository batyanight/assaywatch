"""The papers/ filename convention: forward only, and injective on the real data."""

from pathlib import Path

from assaywatch.papers import doi_stem, held_dois, paper_for_doi
from assaywatch.validate import iter_files, load_assay

REGISTRY = Path(__file__).resolve().parent.parent / "registry"


def test_the_convention_maps_slash_and_brackets_and_lowercases():
    assert doi_stem("10.3390/v13081632") == "10.3390_v13081632"
    assert doi_stem("10.1016/S0166-0934(96)02155-6") == "10.1016_s0166-0934_96_02155-6"
    assert doi_stem("10.1016/0890-8508(92)90002-F") == "10.1016_0890-8508_92_90002-f"
    assert doi_stem("  10.1128/JCM.00192-08 ") == "10.1128_jcm.00192-08"


def test_a_stem_cannot_be_reversed_which_is_why_nothing_tries():
    """`/`, `(` and `)` all become `_`, and a round trip cannot tell them apart:
    reversing `_` to `/` and forward-mapping again returns the same stem, so the
    wrong DOI looks as valid as the right one. This is the ambiguity that filed
    twenty entries' papers under DOIs nothing asks for and wrote ten fabricated
    DOIs into docs/papers-index.cache.json."""
    stem = doi_stem("10.1016/0890-8508(92)90002-F")
    wrong = stem.replace("_", "/")
    assert wrong == "10.1016/0890-8508/92/90002-f"
    assert doi_stem(wrong) == stem  # the round trip "succeeds" on the wrong DOI


def test_every_registry_doi_maps_to_its_own_stem():
    """Injective on the real data, which is what makes forward-only lookup sound."""
    dois = {
        a.citation.doi.lower() for a in map(load_assay, iter_files(REGISTRY)) if a.citation and a.citation.doi
    }
    stems: dict[str, str] = {}
    for d in dois:
        s = doi_stem(d)
        assert s not in stems, f"{d} and {stems[s]} share the stem {s}"
        stems[s] = d


def test_paper_for_doi_finds_a_file_of_any_extension(tmp_path):
    (tmp_path / "10.1016_0890-8508_92_90002-f.pdf").write_text("x")
    (tmp_path / "10.3390_v13081632.txt").write_text("x")
    assert paper_for_doi("10.1016/0890-8508(92)90002-F", tmp_path).suffix == ".pdf"
    assert paper_for_doi("10.3390/v13081632", tmp_path).suffix == ".txt"
    # a PDF-only caller does not get the .txt
    assert paper_for_doi("10.3390/v13081632", tmp_path, (".pdf",)) is None
    assert paper_for_doi("10.9999/absent.1", tmp_path) is None
    assert paper_for_doi("", tmp_path) is None


def test_held_dois_is_forward_mapped_not_reverse(tmp_path):
    (tmp_path / "10.1016_s0168-1702_97_01458-5.pdf").write_text("x")
    asked = ["10.1016/S0168-1702(97)01458-5", "10.9999/absent.1"]
    assert held_dois(asked, tmp_path) == {"10.1016/s0168-1702(97)01458-5"}
    assert held_dois(asked, tmp_path / "nope") == set()
