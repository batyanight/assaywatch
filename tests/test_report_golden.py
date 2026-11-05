"""The report's rendered output, byte for byte, over the fixture registry.

WHY THIS EXISTS. ROADMAP "Lineage composition over time" step 10 moves the record set the
per-year graph is built from out of `report.assess_as_reported` and `drift.assess` into
shared code, so the composition panel and the graph cannot disagree about which records
exist (decision A, 2026-11-02). That is a refactor of the path that decides published
verdicts, and the only honest guard for such a change is that every byte it renders is
unchanged. Committed BEFORE the refactor, for exactly that reason.

It keeps its value afterwards: any change to the report's surface -- a column, a word, a
rounding -- fails here and has to be acknowledged by regenerating the file.

REGENERATE, having read the diff and meant it:

    UPDATE_GOLDEN=1 pytest tests/test_report_golden.py

and commit the new fixture with the change that moved it.
"""

from __future__ import annotations

import gzip
import os
from datetime import date
from pathlib import Path

import pytest
import yaml

from assaywatch.report import build

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"
GOLDEN_MD = FIXTURES / "report-golden.md"
GOLDEN_HTML = FIXTURES / "report-golden.html"

#: The three fixture entries, with a deposit history each that exercises a different
#: verdict: Encephalitozoon declines sharply, Aparavirus holds, and the Enterovirus round
#: has too few records to judge. Fixed years and calls, so the render is deterministic.
_HISTORY = {
    "Encephalitozoon_cuniculi_PTP_Xiao_2001": (
        [(2018, "detect")] * 20 + [(2025, "detect")] * 6 + [(2025, "fail")] * 24
    ),
    "Aparavirus_apisacutum_capsid_Rossi_2024": (
        [(2019, "detect")] * 18 + [(2025, "detect")] * 17 + [(2025, "reduced")] * 3
    ),
    "Enterovirus_5UTR_VP4_VP2_Wray_2016_round1": [(2024, "detect")] * 3 + [(2025, "no_amplicon")] * 2,
}


def _inputs(tmp_path: Path) -> tuple[Path, Path]:
    """Fixture calls and archive metadata on disk; returns (calls path, retrieved dir)."""
    retrieved = tmp_path / "retrieved"
    rows = [("assay_id", "record_id", "call")]
    meta: dict[int, list[tuple[str, ...]]] = {}
    n = 0
    for assay_id, history in _HISTORY.items():
        taxid = yaml.safe_load((FIXTURES / "registry" / f"{assay_id}.yaml").read_text())["target"]["taxid"]
        for year, call in history:
            acc = f"AB{n:05d}"
            n += 1
            rows.append((assay_id, f"{acc}.1", call))
            meta.setdefault(int(taxid), []).append(
                (str(n), acc, f"{year}-03-01", f"{year}-03-01", "500", f"Fixture organism {year} clone {n}")
            )
    for taxid, lines in meta.items():
        group = retrieved / str(taxid)
        group.mkdir(parents=True, exist_ok=True)
        with gzip.open(group / "2026-10-03.meta.tsv.gz", "wt") as fh:
            fh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
            for line in lines:
                fh.write("\t".join(line) + "\n")
    calls_path = tmp_path / "2026-11-01" / "calls.tsv"
    calls_path.parent.mkdir(parents=True)
    calls_path.write_text("\n".join("\t".join(r) for r in rows) + "\n")
    return calls_path, retrieved


def _render(tmp_path: Path) -> tuple[str, str]:
    calls_path, retrieved = _inputs(tmp_path)
    cfg = yaml.safe_load((ROOT / "config.yaml").read_text())
    # `lineage.taxid_backfill` names a gitignored file under data/retrieved. Left alone, the
    # render depended on whether this machine held it: the lineage sections appear only when
    # the map has entries, so the fixture passed locally and failed in CI on 2026-11-04.
    backfill = tmp_path / "backfill.tsv.gz"
    with gzip.open(backfill, "wt") as fh:
        fh.write("accession\ttaxid\nZZ99999\t9\n")
    cfg["lineage"]["taxid_backfill"] = str(backfill)
    md, page, _drifts, _nests = build(
        calls_path,
        FIXTURES / "registry",
        retrieved,
        cfg,
        run_date="2026-11-01",
        today=date(2026, 11, 1),
    )
    return md, page


def test_the_report_renders_the_same_bytes_as_the_committed_fixture(tmp_path):
    md, page = _render(tmp_path)
    if os.environ.get("UPDATE_GOLDEN"):
        GOLDEN_MD.write_text(md)
        GOLDEN_HTML.write_text(page)
        pytest.skip("golden fixtures rewritten")
    hint = "\n\nRead the diff; if it is meant, UPDATE_GOLDEN=1 pytest tests/test_report_golden.py"
    assert md == GOLDEN_MD.read_text(), "report.md changed" + hint
    assert page == GOLDEN_HTML.read_text(), "report.html changed" + hint


def test_the_render_does_not_depend_on_where_it_ran(tmp_path):
    """Two renders in different directories must agree, or the fixture above would pin a
    path. The run is deterministic otherwise: `today` and `run_date` are fixed, and
    nothing in the report reads the clock."""
    first = _render(tmp_path / "one")
    second = _render(tmp_path / "two")
    assert first == second
