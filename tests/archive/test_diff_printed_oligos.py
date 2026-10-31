"""scripts/archive/diff_printed_oligos.py: compare two versions of the oligo reader over real files.

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

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location(
    "diff_printed", ROOT / "scripts" / "archive" / "diff_printed_oligos.py"
)
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


# ---- after the second review ------------------------------------------------------------


def test_fail_on_loss_does_not_pass_when_nothing_was_compared(tmp_path, papers, capsys):
    """An old revision that cannot read the folder's file type skipped every file and exited
    0 under --fail-on-loss: a gate built on the exit code passed vacuously. It is 2 now, and
    it says why."""
    old = old_script(tmp_path, f"    return [{FWD!r}]", suffixes='(".pdf",)')
    rc, out = run(tmp_path, papers, old, capsys, "--fail-on-loss")
    assert rc == 2 and "0 papers compared" in out
    rc, _ = run(tmp_path, papers, old, capsys)  # without the flag the same run is just a report
    assert rc == 0
    empty = tmp_path / "empty"
    empty.mkdir()
    same = old_script(tmp_path, f"    return [{FWD!r}]")
    assert dp.main(["--papers", str(empty), "--old-script", str(same), "--fail-on-loss"]) == 2


def test_an_old_script_without_paper_suffixes_is_treated_as_pdf_only(tmp_path, papers, capsys):
    """Revisions that predate `PAPER_SUFFIXES` read PDFs only: the default has to say so."""
    path = tmp_path / "old_nosuffix.py"
    path.write_text(
        f"def file_text(path):\n    return path.read_text()\ndef printed_oligos(text):\n    return [{FWD!r}]\n"
    )
    (papers / "scan.pdf").write_bytes(b"%PDF-1.4 not really")
    rc, out = run(tmp_path, papers, path, capsys)
    assert rc == 0
    assert "skipped: the old version cannot read this file type" in out  # the .txt paper
    assert "scan.pdf" not in out or "skipped" not in out.split("scan.pdf")[1].splitlines()[0]


def test_the_old_versions_own_reader_is_used_by_default(tmp_path, papers, capsys):
    """The headline behaviour: each version reads the paper with ITS OWN file_text, so a
    change to how files are read is part of what is compared. The fake old reader appends a
    marker its extractor needs; the paper itself lacks it, so an extractor handed the new
    reading finds nothing and every oligo would read as gained."""
    old = tmp_path / "old_marker.py"
    old.write_text(
        'PAPER_SUFFIXES = (".txt",)\n'
        "def file_text(path):\n"
        '    return path.read_text() + " MARKER"\n'
        "def printed_oligos(text):\n"
        f"    return [{FWD!r}, {REV!r}] if text.endswith(' MARKER') else []\n"
    )
    rc, out = run(tmp_path, papers, old, capsys)
    assert rc == 0 and "0 oligo(s) lost, 0 gained" in out, out
    rc, out = run(tmp_path, papers, old, capsys, "--extractor-only")
    # Given the unmarked (new) reading, the old extractor finds nothing, so both read as GAINED.
    assert "0 oligo(s) lost, 2 gained" in out, out


def test_the_summary_counts_identical_papers_when_some_changed(tmp_path, capsys):
    d = tmp_path / "p"
    d.mkdir()
    (d / "10.1000_same.txt").write_text(PAPER)
    (d / "10.1000_other.txt").write_text(PAPER.replace(FWD, "CCCCGGGGAAAATTTTACGTAC"))
    old = old_script(tmp_path, f"    return [{FWD!r}, {REV!r}]")
    _, out = run(tmp_path, d, old, capsys)
    assert "2 papers compared, 1 identical, 1 changed" in out, out


def test_git_show_is_relative_to_the_checkout_not_the_enclosing_repo(tmp_path, monkeypatch):
    """When this checkout sits inside a larger repository, `REV:path` resolved from the
    repository's top level and the tool died with 'path does not exist'."""
    import subprocess

    nest = tmp_path / "nest"
    proj = nest / "proj"
    (proj / "scripts").mkdir(parents=True)
    (proj / "scripts" / "verify_oligos_against_paper.py").write_text("MARKER = 1\n")
    git = ["git", "-c", "user.name=t", "-c", "user.email=t@t"]
    try:
        subprocess.run([*git, "init", "-q"], cwd=nest, check=True, capture_output=True)
        subprocess.run([*git, "add", "-A"], cwd=nest, check=True, capture_output=True)
        subprocess.run([*git, "commit", "-q", "-m", "x"], cwd=nest, check=True, capture_output=True)
    except (OSError, subprocess.CalledProcessError):
        pytest.skip("git unavailable")
    monkeypatch.setattr(dp, "ROOT", proj)
    work = tmp_path / "work"
    work.mkdir()
    assert dp.old_script_from_git("HEAD", work).read_text() == "MARKER = 1\n"
