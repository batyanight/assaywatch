"""Write a file so it is either complete or absent, never half-written.

Why this exists as its own module rather than a line in each writer.

Every stage downstream of `collect` wrote its output straight to the path
Snakemake tracks: `report.md`, `report.html`, `site-drift.md`, `site-drift.tsv`,
`lineage.md` and each figure. Snakemake deletes a FAILED job's outputs, which
covers the ordinary case -- but not a whole-process death. A lid closing, a
`kill -9` or a power loss during `write_text` leaves a truncated file with a
fresh mtime, and that is a file `rule all` accepts and `report` inlines: a
half-written `forest.svg` goes into the published HTML, and a half-written
`report.md` is the document a reader opens. `profiles/launchd/README.md` records
a run that spent 1h31m of 1h47m asleep, so the window is not hypothetical.

`shadow: "minimal"` would have been the one-line Snakemake answer and does not
work here: these rules read the registry, which travels as a PARAM and not as a
declared input (see the comment above `_REPORT_PARAMS` in the Snakefile), so a
shadow directory would not contain it. Making the writers atomic gets the same
guarantee without changing what the rules depend on.

`collect.py` already guarded its own upstream inputs this way; nothing guarded
the outputs. `retrieve.write_manifest` and `timing` had it too, each written
after its own incident -- which is the argument for one helper instead of a
fourth hand-rolled copy.
"""

from __future__ import annotations

import os
from pathlib import Path


def write_text(path: Path, text: str) -> None:
    """Write *text* to *path* via a sibling `.part`, then rename.

    The rename is atomic within a filesystem, so a reader sees either the
    previous contents or the complete new ones. The `.part` sits beside the
    target rather than in a temp directory, so the rename never crosses a
    filesystem boundary (which would silently become a copy, reopening the
    window this closes). A leftover `.part` after a crash is inert: every
    consumer looks for the real name, and the next run overwrites it.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.part")
    tmp.write_text(text)
    os.replace(tmp, path)
