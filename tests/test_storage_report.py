"""The storage report must sort by recoverability, and must never delete.

The obvious reaction to a full disk is to delete the biggest thing, and here
the biggest thing is the one that cannot be re-fetched. These tests pin the
distinction the report exists to make.
"""

import csv
import gzip
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("storage_report", ROOT / "scripts" / "storage_report.py")
storage_report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(storage_report)


def _group(retrieved: Path, taxid: int, group: str, accs, payload=b"x" * 100):
    d = retrieved / str(taxid) / group
    d.mkdir(parents=True, exist_ok=True)
    (d / "2026-10-03.fasta.gz").write_bytes(payload)
    with gzip.open(d / "2026-10-03.meta.tsv.gz", "wt", newline="") as fh:
        w = csv.DictWriter(fh, ["accession", "created", "updated"], delimiter="\t")
        w.writeheader()
        for a in accs:
            w.writerow({"accession": f"{a}.1", "created": "2020-01-01", "updated": "2020-01-01"})


def test_a_group_the_registry_no_longer_asks_for_is_reported_as_orphaned(tmp_path, capsys):
    retrieved = tmp_path / "retrieved"
    # taxid 109871 is Bd, which the real registry does ask for; 999999 is nobody's.
    _group(retrieved, 999999, "all", ["AB1", "AB2"])
    rc = storage_report.main(
        ["--retrieved", str(retrieved), "--registry", str(ROOT / "registry"), "--results", str(tmp_path)]
    )
    out = capsys.readouterr().out
    assert rc == 0
    assert "999999/all" in out
    assert "ORPHANED" in out
    # and the report says what losing it would cost, rather than recommending removal
    assert "Still the only copy" in out


def test_duplication_between_two_groups_of_one_taxon_is_reported(tmp_path, capsys):
    retrieved = tmp_path / "retrieved"
    shared = [f"AB{i}" for i in range(100)]
    _group(retrieved, 999999, "qaaaaaaaaaa", shared, payload=b"x" * 50_000_000)
    _group(retrieved, 999999, "qbbbbbbbbbb", shared + ["ZZ1"], payload=b"x" * 50_000_000)
    storage_report.main(
        ["--retrieved", str(retrieved), "--registry", str(ROOT / "registry"), "--results", str(tmp_path)]
    )
    out = capsys.readouterr().out
    assert "share 100 accessions" in out
    assert "100% of the smaller" in out


def test_the_report_deletes_nothing(tmp_path, capsys):
    """The whole point: it measures, a person decides."""
    retrieved = tmp_path / "retrieved"
    _group(retrieved, 999999, "all", ["AB1"])
    before = sorted(p.relative_to(tmp_path) for p in tmp_path.rglob("*") if p.is_file())
    storage_report.main(
        ["--retrieved", str(retrieved), "--registry", str(ROOT / "registry"), "--results", str(tmp_path)]
    )
    after = sorted(p.relative_to(tmp_path) for p in tmp_path.rglob("*") if p.is_file())
    assert before == after
    assert "Nothing was deleted" in capsys.readouterr().out
