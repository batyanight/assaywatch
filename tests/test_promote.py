"""The promotion worklist: it proposes, and `--apply` changes one line per file."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("promote", ROOT / "scripts" / "promote.py")
promote = importlib.util.module_from_spec(_spec)
sys.modules["promote"] = promote
_spec.loader.exec_module(promote)


def test_listing_writes_nothing(tmp_path, capsys):
    """Only a maintainer sets `active` (CONTRIBUTING.md, CLAUDE.md), so the
    default has to be a worklist."""
    before = {p: p.read_bytes() for p in (ROOT / "registry").glob("*.yaml")}
    assert promote.main(["--tier", "eligible"]) == 0
    out = capsys.readouterr().out
    assert "Proposed only" in out
    assert all(p.read_bytes() == b for p, b in before.items()), "listing must not write"


def test_the_two_tiers_mean_different_things(capsys):
    """`active` is a METADATA gate -- a citation that resolves, a taxon, a design
    year -- and says nothing about whether the oligos are right, which is what
    every call in a screen depends on. The tiers make that choice explicit
    instead of burying it."""
    promote.main([])
    out = capsys.readouterr().out
    assert "meet every mechanical `active` requirement" in out
    assert "carry no oligo doubt" in out
    # and the blockers are counted, so the remainder is a worklist too
    assert "what blocks the rest:" in out


def test_apply_changes_exactly_the_status_line(tmp_path):
    """A YAML round-trip would reformat 100 files and lose the comments that
    carry each entry's reasoning. One line is replaced."""
    import shutil

    reg = tmp_path / "registry"
    shutil.copytree(ROOT / "registry", reg)
    before = {p.name: p.read_text() for p in reg.glob("*.yaml")}
    assert promote.main(["--registry", str(reg), "--tier", "clean", "--apply"]) == 0

    changed = [n for n, t in before.items() if (reg / n).read_text() != t]
    assert changed, "the clean tier should not be empty"
    for name in changed:
        old_lines = before[name].splitlines()
        new_lines = (reg / name).read_text().splitlines()
        diff = [(a, b) for a, b in zip(old_lines, new_lines, strict=True) if a != b]
        assert diff == [("status: draft", "status: active")], f"{name}: {diff}"

    # and the result still validates
    from assaywatch.validate import iter_files, load_assay

    assert len([load_assay(p) for p in iter_files(reg)]) == len(before)
