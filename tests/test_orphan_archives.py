"""Orphan retrieval archives: on disk, asked for by nobody.

The failure that prompted this: a forced rescreen of every archive on disk died
at DAG construction with `KeyError: (2093, 'q4185828e3e')`, because that
archive's group no longer exists in the registry. Nothing reported it.
"""

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("orph", ROOT / "scripts" / "orphan_archives.py")
orph = importlib.util.module_from_spec(_spec)
sys.modules["orph"] = orph
_spec.loader.exec_module(orph)


def _archive(retrieved: Path, taxid: str, group: str, stem: str, size: int = 10):
    p = retrieved / taxid / group / f"{stem}.fasta.gz"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(b"x" * size)
    return p


def test_archives_are_grouped_by_taxid_and_group(tmp_path):
    _archive(tmp_path, "10241", "all", "2026-10-03")
    _archive(tmp_path, "10241", "all", "2026-10-11")
    _archive(tmp_path, "11118", "qabc", "2026-10-03")
    found = orph.archives_on_disk(tmp_path)
    assert {k: len(v) for k, v in found.items()} == {(10241, "all"): 2, (11118, "qabc"): 1}


def test_non_archive_directories_are_ignored(tmp_path):
    """`data/retrieved/` also holds `runs/` and the manifest, which are not archives."""
    _archive(tmp_path, "runs", "all", "2026-10-03")
    _archive(tmp_path, "10241", "all", "2026-10-03")
    assert list(orph.archives_on_disk(tmp_path)) == [(10241, "all")]


def test_manifest_runs_are_counted_per_group(tmp_path):
    (tmp_path / "manifest.json").write_text(
        json.dumps(
            {
                "runs": [
                    {"taxid": 10241, "group": "all"},
                    {"taxid": 10241, "group": "all"},
                    {"taxid": 11118, "group": "qabc"},
                    {"taxid": 999},  # no group key: the retrieve default is `all`
                    {"group": "all"},  # no taxid: skipped, not fatal
                ]
            }
        )
    )
    assert orph.manifest_runs(tmp_path / "manifest.json") == {
        (10241, "all"): 2,
        (11118, "qabc"): 1,
        (999, "all"): 1,
    }


def test_a_missing_or_broken_manifest_is_not_fatal(tmp_path):
    assert orph.manifest_runs(tmp_path / "nope.json") == {}
    (tmp_path / "manifest.json").write_text("{not json")
    assert orph.manifest_runs(tmp_path / "manifest.json") == {}


@pytest.fixture
def repo(tmp_path):
    """A miniature repo: one live assay, one pending, archives for both plus a stale group."""
    registry, pending, retrieved = tmp_path / "registry", tmp_path / "pending", tmp_path / "retrieved"
    for d in (registry, pending):
        d.mkdir()
    entry = {
        "id": "LIVE",
        "name": "Live assay",
        "target": {"taxid": 10241, "taxon_name": "Orthopoxvirus", "gene": "pol", "genome_type": "dsDNA"},
        "chemistry": "conventional",
        "oligos": {
            "forward": {"name": "F", "seq": "CCTTGATATAATACAGTGTGCCATATGTC"},
            "reverse": {"name": "R", "seq": "AGCCAAGAGATCCGTTGTCAAA"},
        },
        "amplicon_bp": 200,
        "citation": {"doi": "10.3354/dao060141", "design_year": 2004, "doi_verified": True},
        "use_context": ["wildlife"],
        "status": "draft",
    }
    (registry / "LIVE.yaml").write_text(yaml.safe_dump(entry, sort_keys=False))
    waiting = dict(entry, id="WAITING")
    waiting["target"] = dict(entry["target"], taxid=12059)
    (pending / "WAITING.yaml").write_text(yaml.safe_dump(waiting, sort_keys=False))
    _archive(retrieved, "10241", "all", "2026-10-03")  # live
    _archive(retrieved, "12059", "all", "2026-10-03")  # orphaned by the pending move
    _archive(retrieved, "2093", "q4185828e3e", "2026-10-04")  # stale query hash
    (tmp_path / "config.yaml").write_text(yaml.safe_dump({"retrieved_dir": str(retrieved)}))
    return tmp_path


def test_an_orphan_is_reported_and_a_live_group_is_not(repo, capsys):
    rc = orph.main(
        [
            "--registry",
            str(repo / "registry"),
            "--pending",
            str(repo / "pending"),
            "--config",
            str(repo / "config.yaml"),
            "--retrieved",
            str(repo / "retrieved"),
        ]
    )
    out = capsys.readouterr().out
    assert rc == 0
    assert "2 orphan group(s)" in out
    assert "12059/all" in out and "2093/q4185828e3e" in out
    assert "10241/all" not in out, "a live group is not an orphan"


def test_a_pending_entry_explains_its_own_orphan(repo, capsys):
    """The distinction that stops the list reading as rubbish: an assay waiting on
    a DOI comes back, and its archives are the history a baseline needs."""
    orph.main(
        [
            "--registry",
            str(repo / "registry"),
            "--pending",
            str(repo / "pending"),
            "--config",
            str(repo / "config.yaml"),
            "--retrieved",
            str(repo / "retrieved"),
        ]
    )
    out = capsys.readouterr().out
    assert "<- pending: WAITING" in out
    assert "belong to assays in pending/" in out
    # The stale query hash has no such explanation, which is the point of the column.
    stale = next(ln for ln in out.splitlines() if "2093/q4185828e3e" in ln)
    assert "pending" not in stale


def test_the_tsv_lists_every_orphan(repo, tmp_path):
    out_tsv = tmp_path / "orphans.tsv"
    orph.main(
        [
            "--registry",
            str(repo / "registry"),
            "--pending",
            str(repo / "pending"),
            "--config",
            str(repo / "config.yaml"),
            "--retrieved",
            str(repo / "retrieved"),
            "--tsv",
            str(out_tsv),
        ]
    )
    rows = out_tsv.read_text().splitlines()
    assert rows[0].split("\t") == orph.COLS
    assert len(rows) == 3
    assert any("12059" in r and "WAITING" in r for r in rows[1:])


def test_nothing_is_deleted(repo, capsys):
    before = sorted(p.name for p in (repo / "retrieved").rglob("*.fasta.gz"))
    orph.main(
        [
            "--registry",
            str(repo / "registry"),
            "--pending",
            str(repo / "pending"),
            "--config",
            str(repo / "config.yaml"),
            "--retrieved",
            str(repo / "retrieved"),
        ]
    )
    assert sorted(p.name for p in (repo / "retrieved").rglob("*.fasta.gz")) == before
    assert "only reports" in capsys.readouterr().err
