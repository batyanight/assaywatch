"""Every `docs/...` path this repository mentions in prose actually exists.

WHY. Before the journals were filed under `docs/journal/` on 2026-10-27, 427
references of the form "docs/" plus a dated filename were spread over prose, code
comments, strategy files and 38 registry curator notes. A move is only safe if
something checks the pointers afterwards, and a pointer rots the same way
whether a file moved, was renamed, or never landed: on 2026-10-27, three
references were already stale and one of them was simply a wrong directory
prefix in a docstring.

WHAT IT CANNOT CATCH. A link that resolves to the wrong file, and a relative
link inside a docs/ file (those are checked for docs/INDEX.md by
test_config_keys.py). This checks the repo-root form only, which is the one that
appears in code comments and registry notes.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

#: Where prose lives. `data/`, `results/` and `.snakemake/` are run state.
SEARCHED = (
    "*.md",
    "*.yaml",
    "*.yml",
    "Snakefile",
    "config.yaml",
    "docs/**/*.md",
    "docs/**/*.tsv",
    "scripts/*.py",
    "assaywatch/*.py",
    "tests/*.py",
    "registry/*.yaml",
    "pending/*.yaml",
    "strategies/*.yaml",
    "papers/*.md",
)

REFERENCE = re.compile(r"docs/[A-Za-z0-9._/-]+\.(?:md|tsv)")

#: Paths that are referenced on purpose and are not in this repository. Each one
#: needs a reason, because the cheap way to green this test is to add a line here.
EXPECTED_ABSENT = {
    # Written on an experiment branch that was never merged; both mentions say so.
    "docs/2026-10-24-anchor-pair-counterfactual.md",
    # A regenerated worksheet from the 2026-10-20 audit, never committed. The two
    # mentions are dated journals describing what that day's run produced.
    "docs/materials-needed.tsv",
}


def test_every_docs_reference_resolves():
    missing: dict[str, list[str]] = {}
    for pattern in SEARCHED:
        for path in sorted(ROOT.glob(pattern)):
            if not path.is_file():
                continue
            try:
                text = path.read_text()
            except (UnicodeDecodeError, OSError):  # pragma: no cover - binary stray
                continue
            for ref in sorted(set(REFERENCE.findall(text))):
                if ref in EXPECTED_ABSENT or (ROOT / ref).exists():
                    continue
                missing.setdefault(ref, []).append(str(path.relative_to(ROOT)))
    assert not missing, "references to docs/ files that do not exist: " + "; ".join(
        f"{ref} (from {', '.join(src[:3])})" for ref, src in sorted(missing.items())
    )
