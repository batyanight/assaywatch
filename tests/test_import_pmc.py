"""Tests for the PMC full-text importer.

It rebuilds `papers/` on a machine that holds none of the PDFs, and everything
downstream reads what it writes, so the failures worth pinning are the quiet
ones: an abstract-only file indexed as though the paper were in hand, a file
named so the verifier can never find it, and a corrupt input that exits clean.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


imp = load("import_pmc_fulltext")
vo = load("verify_oligos_against_paper")

BODY = (
    "Methods. Forward primer F1 (5'-GCGGCCAACCAGTTTAACGCAA-3') and reverse R1 (5'-ATTGCGCTGGAACCTTGTCAAG-3')."
)


def article(doi="10.1234/test.1", body=BODY, pmcid="PMC1", **extra):
    return {
        "identifiers": {"pmcid": pmcid, "pmid": "1", "doi": doi},
        "title": "A paper",
        "abstract": "An abstract.",
        "full_text": body,
        **extra,
    }


def dump(path: Path, payload) -> Path:
    path.write_text(json.dumps(payload))
    return path


def run(tmp_path, *payloads, extra=()):
    files = [dump(tmp_path / f"d{i}.json", p) for i, p in enumerate(payloads)]
    out = tmp_path / "papers"
    rc = imp.main(["--json", *map(str, files), "--out-dir", str(out), *extra])
    return rc, out


def test_writes_one_file_named_for_the_doi_and_the_verifier_can_find_it(tmp_path):
    """The round trip that matters: what the importer writes, index_papers reads
    back under the same DOI."""
    rc, out = run(tmp_path, {"articles": [article("10.1128/JCM.00192-08")]})
    assert rc == 0
    assert [p.name for p in out.glob("*")] == ["10.1128_jcm.00192-08.txt"]  # lowercased
    by_doi, _ = vo.index_papers(out)
    assert "10.1128/jcm.00192-08" in by_doi
    assert len(vo.printed_oligos(by_doi["10.1128/jcm.00192-08"][0])) == 2


@pytest.mark.parametrize(
    "payload",
    [
        {"articles": [article()]},  # the tool's usual shape
        [article()],  # a bare list
        article(),  # a single article object
    ],
    ids=["articles-key", "bare-list", "single-object"],
)
def test_accepts_every_shape_the_dump_arrives_in(tmp_path, payload):
    rc, out = run(tmp_path, payload)
    assert rc == 0 and len(list(out.glob("*.txt"))) == 1


def test_a_doi_at_the_top_level_is_found_when_identifiers_is_absent(tmp_path):
    a = article()
    del a["identifiers"]
    a["doi"] = "10.9999/top.level"
    rc, out = run(tmp_path, [a])
    assert [p.name for p in out.glob("*")] == ["10.9999_top.level.txt"]


def test_title_abstract_and_body_all_land_in_the_file(tmp_path):
    """A short methods paper sometimes prints its primers in the abstract only."""
    rc, out = run(tmp_path, [article()])
    text = next(out.glob("*.txt")).read_text()
    assert "A paper" in text and "An abstract." in text and "GCGGCCAACC" in text


def test_an_article_with_no_body_is_reported_and_never_written(tmp_path, capsys):
    """An abstract-only file would be indexed as if the paper were in hand, and
    every sequence checked against it would read `absent` - indistinguishable from
    "this sequence is not in this paper", the finding verification exists to find."""
    rc, out = run(tmp_path, [article("10.1128/jcm.1", body=""), article("10.1128/jcm.2", body="   \n ")])
    assert rc == 0
    assert not out.exists() or list(out.glob("*")) == []
    printed = capsys.readouterr().out
    assert "2 articles carry NO full text" in printed and "10.1128/jcm.1" in printed


def test_an_article_without_a_usable_doi_is_counted_not_crashed_on(tmp_path, capsys):
    bad = article(doi="not-a-doi")
    none = article()
    none["identifiers"] = {"pmcid": "PMC9"}
    rc, out = run(tmp_path, [bad, none, article("10.1234/ok.1")])
    assert rc == 0
    assert [p.name for p in out.glob("*")] == ["10.1234_ok.1.txt"]
    assert "2 articles had no usable DOI" in capsys.readouterr().err


def test_an_existing_file_is_kept_unless_asked_to_overwrite(tmp_path):
    rc, out = run(tmp_path, [article(body=BODY)])
    f = next(out.glob("*.txt"))
    f.write_text("hand-edited\n")
    run(tmp_path, [article(body=BODY + " changed")])
    assert f.read_text() == "hand-edited\n"
    run(tmp_path, [article(body=BODY + " changed")], extra=["--overwrite"])
    assert "changed" in f.read_text()


def test_dry_run_writes_nothing(tmp_path, capsys):
    rc, out = run(tmp_path, [article()], extra=["--dry-run"])
    assert rc == 0 and not out.exists()
    assert "would write" in capsys.readouterr().out


def test_a_corrupt_input_is_named_and_exits_non_zero(tmp_path, capsys):
    """It used to print '0 papers written' and exit 0, so a script driving it
    could not tell a clean empty run from a failed one."""
    bad = tmp_path / "corrupt.json"
    bad.write_text("{ not json")
    rc = imp.main(["--json", str(bad), "--out-dir", str(tmp_path / "papers")])
    assert rc == 1
    err = capsys.readouterr().err
    assert "corrupt.json" in err and "could not be read" in err


def test_one_corrupt_input_does_not_stop_the_good_ones(tmp_path):
    bad = tmp_path / "corrupt.json"
    bad.write_text("{ not json")
    good = dump(tmp_path / "good.json", [article()])
    rc = imp.main(["--json", str(bad), str(good), "--out-dir", str(tmp_path / "papers")])
    assert rc == 1  # reported...
    assert len(list((tmp_path / "papers").glob("*.txt"))) == 1  # ...but not abandoned


def test_an_empty_dump_is_not_an_error(tmp_path):
    """No articles is a legitimate result and must stay distinguishable from
    an unreadable file."""
    rc, out = run(tmp_path, {"articles": []})
    assert rc == 0


def test_a_doi_containing_an_underscore_is_refused_because_it_cannot_round_trip(tmp_path, capsys):
    """The verifier turns every `_` back into `/`, so `10.1000/abc_def` would be
    written as 10.1000_abc_def.txt and read back as 10.1000/abc/def: a file that
    nothing could ever match to its entry."""
    rc, out = run(tmp_path, [article("10.1000/abc_def")])
    assert rc == 1
    assert not out.exists() or list(out.glob("*")) == []
    assert "underscore" in capsys.readouterr().err


def test_no_registry_doi_contains_an_underscore():
    """The guard behind the refusal above: if a DOI with an underscore is ever
    added to the registry, its paper could not be filed or found by name."""
    bad = []
    for f in sorted((ROOT / "registry").glob("*.yaml")):
        doi = ((yaml.safe_load(f.read_text()).get("citation") or {}).get("doi") or "").strip()
        if "_" in doi:
            bad.append((f.stem, doi))
    assert bad == [], f"DOIs the papers/ naming convention cannot round-trip: {bad}"


def test_doi_filename_lowercases_and_replaces_every_slash():
    assert imp.doi_filename("10.1093/INFDIS/167.2.458") == "10.1093_infdis_167.2.458.txt"
