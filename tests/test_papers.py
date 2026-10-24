"""The papers/ filename convention: forward only, and injective on the real data."""

import ast
from pathlib import Path

from assaywatch.papers import doi_stem, held_dois, identity_stem, paper_for_doi
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


def test_identity_stem_strips_the_supplement_marker_only():
    """A supplement names its article; nothing else about a stem changes."""
    article = "10.1371_journal.pone.0207365"
    assert identity_stem(Path(article + ".supp.pdf")) == article
    assert identity_stem(Path(article + ".pdf")) == article
    # `.supp` inside the DOI itself is not the marker: only a trailing one is.
    assert identity_stem(Path("10.1234_supp.1.pdf")) == "10.1234_supp.1"


def test_nothing_writes_a_filename_by_replacing_only_the_slash():
    """Every writer into `papers/` forward-maps through `doi_stem`, parentheses included.

    `doi.replace("/", "_")` looks like the convention and is not: it leaves `(`
    and `)` alone, so an Elsevier DOI lands as
    `10.1016_s0016-5085(98)70589-x.xml`, a name no reader forward-mapping a DOI
    can produce. Three fetchers did this until 2026-10-24 and eleven publisher
    JATS deposits on disk had to be renamed. This is the control that keeps the
    fourth from being written.

    Parsed rather than grepped, so the paragraph in `assaywatch/papers.py` that
    explains the mistake is not itself a hit. One reader is allowed to build the
    old spelling on purpose, to index a `papers/` copied from an older checkout;
    it says so with the marker below.
    """
    marker = "slash-only spelling on purpose"
    root = Path(__file__).resolve().parent.parent
    bad = []
    for d in ("scripts", "assaywatch"):
        for path in sorted((root / d).rglob("*.py")):
            src = path.read_text(errors="replace")
            lines = src.splitlines()
            try:
                tree = ast.parse(src)
            except SyntaxError:  # pragma: no cover - nothing in the tree is unparseable
                continue
            for node in ast.walk(tree):
                if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
                    continue
                if node.func.attr != "replace":
                    continue
                args = [a.value for a in node.args if isinstance(a, ast.Constant)]
                if args[:2] != ["/", "_"]:
                    continue
                line = lines[node.lineno - 1]
                if marker in line or (node.lineno > 1 and marker in lines[node.lineno - 2]):
                    continue
                bad.append(f"{path.relative_to(root)}:{node.lineno}: {line.strip()}")
    assert not bad, "forward-map through assaywatch.papers.doi_stem instead:\n" + "\n".join(bad)


def test_nothing_reads_a_doi_back_out_of_a_filename():
    """Nothing reverse-maps a stem with `.replace("_", "/")`, the mapping that is not injective.

    Three characters map onto `_`, so the inverse invents DOIs: the module
    docstring lists five call sites that did it and what each one cost. A sixth
    survived in `fetch_elsevier.outstanding`, which built its "already held" set
    that way and so reported all eleven parenthesised Elsevier papers as
    missing, ready to re-fetch over the API. It hid for as long as it did
    because those files were stored under the slash-only spelling, where the
    reverse mapping happened to come out right; renaming them to the canonical
    stem on 2026-10-24 is what exposed it. Use `held_dois` or `paper_for_doi`.

    `verify_oligos_against_paper` is the one exemption: it reverse-maps to
    recognise a DOI-shaped filename, then files the result under a prefixed
    stem key rather than treating it as a DOI, and says so where it does it.
    """
    marker = "reverse-maps on purpose"
    root = Path(__file__).resolve().parent.parent
    exempt = {"verify_oligos_against_paper.py"}
    bad = []
    for d in ("scripts", "assaywatch"):
        for path in sorted((root / d).rglob("*.py")):
            if path.name in exempt:
                continue
            src = path.read_text(errors="replace")
            lines = src.splitlines()
            try:
                tree = ast.parse(src)
            except SyntaxError:  # pragma: no cover - nothing in the tree is unparseable
                continue
            for node in ast.walk(tree):
                if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
                    continue
                if node.func.attr != "replace":
                    continue
                args = [a.value for a in node.args if isinstance(a, ast.Constant)]
                if args[:2] != ["_", "/"]:
                    continue
                line = lines[node.lineno - 1]
                if marker in line or (node.lineno > 1 and marker in lines[node.lineno - 2]):
                    continue
                bad.append(f"{path.relative_to(root)}:{node.lineno}: {line.strip()}")
    assert not bad, "a filename stem is not a DOI; use held_dois/paper_for_doi:\n" + "\n".join(bad)
