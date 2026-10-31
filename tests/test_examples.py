"""The offline worked example still works, and still produces what its README says.

WHY THIS EXISTS. `examples/` is the one result a stranger can reproduce from a
clone: no network, no NCBI key, no Snakemake, about a second. Nothing tested it,
and it had been broken since the Bd assay's `amplicon_bp` was corrected from 121
to 146 by measurement (commit 9ea1a1e). `make_example_fasta.py` sliced a 70 nt
filler constant for the 95 nt middle that 146 bp needs, got 70 back, and died on
its own length assertion. The assertion is the only reason it failed loudly rather
than writing a short amplicon.

So the failure mode was: the registry improves, and the front-door example stops
working, and the suite says nothing. Found 2026-10-30 by running the release
plan's "stranger test" by hand. This test is that check, automated.
"""

from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "examples" / "README.md"


def _documented_tally() -> dict[str, int]:
    """The per-call counts the README prints in its expected-output block."""
    rows = re.findall(
        r"^CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004\t(\w+)\t(\d+)$",
        README.read_text(),
        re.MULTILINE,
    )
    assert rows, "examples/README.md no longer shows a per-call tally to check against"
    return {call: int(n) for call, n in rows}


def test_the_example_generator_runs_and_matches_the_registry(tmp_path: Path):
    """It builds its records from the assay's own oligos, so it has to agree with
    whatever `amplicon_bp` the registry now holds."""
    r = subprocess.run(
        [sys.executable, str(ROOT / "examples" / "make_example_fasta.py")],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert r.returncode == 0, f"examples/make_example_fasta.py failed:\n{r.stdout}\n{r.stderr}"
    fasta = ROOT / "examples" / "bd-example.fasta"
    assert fasta.exists()
    headers = [ln for ln in fasta.read_text().splitlines() if ln.startswith(">")]
    assert len(headers) == 9, f"expected 9 synthetic records, got {len(headers)}"


def test_screening_the_example_gives_what_its_readme_documents(tmp_path: Path):
    """The README states the verdict counts verbatim, and a reader checks their
    install against them. If scoring changes, this fails and both move together."""
    subprocess.run(
        [sys.executable, str(ROOT / "examples" / "make_example_fasta.py")],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=True,
    )
    out = tmp_path / "calls.tsv"
    r = subprocess.run(
        [
            sys.executable,
            "-m",
            "assaywatch.screen",
            "registry/CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004.yaml",
            "examples/bd-example.fasta",
            "-o",
            str(out),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert r.returncode == 0, f"screening the example failed:\n{r.stdout}\n{r.stderr}"
    rows = out.read_text().splitlines()
    header = rows[0].split("\t")
    call_at = header.index("call")
    got = Counter(line.split("\t")[call_at] for line in rows[1:])
    assert dict(got) == _documented_tally(), (
        f"examples/README.md documents {_documented_tally()} but the screen produced {dict(got)}; "
        "update both together"
    )
