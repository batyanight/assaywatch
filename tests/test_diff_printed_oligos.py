"""scripts/diff_printed_oligos.py: compare two versions of the oligo reader over real files.

The tool exists so that a threshold change can be checked against the PDFs held
locally. What has to be true of it: an identical reader reports no change; an
oligo the new reader finds and the old one did not is reported as gained, and one
it no longer finds as lost, with the exit code reflecting loss only when asked;
and a file the old version cannot read is said to be skipped, not silently counted
as identical.
"""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("diff_printed", ROOT / "scripts" / "diff_printed_oligos.py")
dp = importlib.util.module_from_spec(_spec)
sys.modules["diff_printed"] = dp
_spec.loader.exec_module(dp)

FWD, REV = "ACGTACGTACGTAAAAGGGGCC", "TTGGCCAATTGGCCAATTGGAACC"
PAPER = f"Primers (5'-3'): FWD, 5'-{FWD}-3'; REV, 5'-{REV}-3'.\n"
BOGUS = "CCCCCCCCCCCCCCCCCCCC"


@pytest.fixture
def papers(tmp_path):
    d = tmp_path / "papers"
    d.mkdir()
    (d / "10.1000_example.txt").write_text(PAPER)
    return d


def old_script(tmp_path, body: str, suffixes: str = '(".txt", ".pdf")') -> Path:
    path = tmp_path / "old.py"
    path.write_text(
        f"PAPER_SUFFIXES = {suffixes}\n"
        "def file_text(path):\n    return path.read_text()\n"
        f"def printed_oligos(text):\n{body}\n"
    )
    return path


def run(tmp_path, papers, old, capsys, *extra):
    rc = dp.main(["--papers", str(papers), "--old-script", str(old), *extra])
    return rc, capsys.readouterr().out


def test_an_identical_reader_reports_no_change(tmp_path, papers, capsys):
    same = tmp_path / "same.py"
    shutil.copy(ROOT / "scripts" / "verify_oligos_against_paper.py", same)
    rc, out = run(tmp_path, papers, same, capsys, "--fail-on-loss")
    assert rc == 0
    assert "1 papers compared, 1 identical, 0 changed; 0 oligo(s) lost, 0 gained" in out


def test_an_oligo_only_the_new_reader_finds_is_gained_and_is_not_a_failure(tmp_path, papers, capsys):
    old = old_script(tmp_path, f"    return [{FWD!r}]")
    rc, out = run(tmp_path, papers, old, capsys, "--fail-on-loss")
    assert rc == 0
    assert f"  + {REV}" in out and "  - " not in out
    assert "0 oligo(s) lost, 1 gained" in out


def test_an_oligo_the_new_reader_no_longer_finds_is_lost(tmp_path, papers, capsys):
    old = old_script(tmp_path, f"    return [{FWD!r}, {REV!r}, {BOGUS!r}]")
    rc, out = run(tmp_path, papers, old, capsys)
    assert rc == 0, "loss alone must not fail the run unless asked"
    assert f"  - {BOGUS}" in out and "1 oligo(s) lost, 0 gained" in out
    assert "Read the lost ones first" in out
    rc, _ = run(tmp_path, papers, old, capsys, "--fail-on-loss")
    assert rc == 1


def test_a_file_the_old_version_cannot_read_is_skipped_not_called_identical(tmp_path, papers, capsys):
    old = old_script(tmp_path, f"    return [{FWD!r}, {REV!r}]", suffixes='(".pdf",)')
    rc, out = run(tmp_path, papers, old, capsys)
    assert rc == 0
    assert "skipped: the old version cannot read this file type" in out
    assert "0 papers compared" in out and "1 skipped" in out


def test_files_that_are_not_papers_are_ignored(tmp_path, papers, capsys):
    (papers / "notes.md").write_text(PAPER)
    (papers / "scans.pdf").mkdir()  # a directory that merely looks like a paper
    old = old_script(tmp_path, f"    return [{FWD!r}, {REV!r}]")
    _, out = run(tmp_path, papers, old, capsys)
    assert "notes.md" not in out and "1 papers compared" in out


def test_an_unknown_revision_is_named_in_the_error(tmp_path, papers):
    with pytest.raises(SystemExit, match="deadbeefnotarev"):
        dp.main(["--papers", str(papers), "--old-rev", "deadbeefnotarev"])


def test_a_missing_papers_directory_is_an_error(tmp_path):
    with pytest.raises(SystemExit, match="not a directory"):
        dp.main(["--papers", str(tmp_path / "nope"), "--old-script", str(tmp_path / "x.py")])


def test_the_old_reader_is_read_from_git_and_compared(tmp_path, papers, capsys):
    """Against a real revision of this repository: it must load and produce a table.
    What it finds is not asserted, because the working tree may differ from HEAD."""
    try:
        subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        pytest.skip("not a git checkout")
    rc = dp.main(["--papers", str(papers), "--old-rev", "HEAD"])
    out = capsys.readouterr().out
    assert rc == 0 and "1 papers compared" in out


def test_extractor_only_compares_both_versions_on_the_new_reading(tmp_path, papers, capsys):
    """An old version that cannot read the file is skipped by default; with
    --extractor-only it is given the new reading and compared on `printed_oligos`
    alone. Its own `file_text` must not be called at all."""
    old = tmp_path / "old.py"
    old.write_text(
        'PAPER_SUFFIXES = (".pdf",)\n'
        'def file_text(path):\n    raise AssertionError("the old reading must not be used")\n'
        f"def printed_oligos(text):\n    return [{FWD!r}]\n"
    )
    rc, out = run(tmp_path, papers, old, capsys, "--extractor-only")
    assert rc == 0
    assert "skipped" not in out and f"  + {REV}" in out and "1 papers compared" in out
