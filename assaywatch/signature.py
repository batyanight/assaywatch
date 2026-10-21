"""Where a cached screen records what it was produced under.

A convention, not logic, and it lives alone because of who has to share it.
`screen.py` writes the file and `collect.py` reads it, and neither may import
the other:

* `collect` inside `screen`'s import closure would mean every edit to
  collect.py rescreens all 316 archives, because the Snakefile hashes that
  closure into `screen_archive`'s params (see `assaywatch/triggers.py` and
  `_code_hash` in the Snakefile).
* `screen` inside `collect`'s closure would mean every edit to score.py or
  schema.py re-triggers `collect_calls`. Harmless — collecting is cheap — but
  it is noise in the one mechanism the pipeline uses to decide what is stale,
  and that mechanism has already been wrong twice.

So the convention sits here, where both can reach it and neither drags the
other along. Editing this file does rescreen everything, which is correct: it
changes where a screen's signature is kept.

WHY A FILE ON DISK AT ALL. `screen_signature` was already a `screen_archive`
param, and Snakemake reruns a job when a param changes — but only where it
holds a metadata record for that output to compare against. The 2026-10-21 run
found 20 screens of 316 with no such record, written by a different Snakemake
install: the params check had nothing to compare, the changed code hash did not
invalidate them, and they were reused in silence. A file beside the screen is
checkable by `collect` whatever Snakemake remembers.
"""

from __future__ import annotations

from pathlib import Path

#: Appended to a screen's own name, so the result cannot be mistaken for a
#: screen by anything globbing `*.tsv` — `assaywatch/windows.py` does.
SIGNATURE_SUFFIX = ".sig"


def signature_path(calls: Path) -> Path:
    """Where `calls`'s signature lives: `2026-10-03.tsv` -> `2026-10-03.tsv.sig`."""
    return calls.with_name(calls.name + SIGNATURE_SUFFIX)


def stored_signature(calls: Path) -> str | None:
    """What `calls` says it was produced under, or None if it does not say.

    None is the honest answer for every screen written before 2026-10-21, and
    callers must keep it distinct from disagreement: "does not say" and "says
    something else" are different facts and only the second is a defect.
    """
    sig = signature_path(calls)
    if not sig.exists():
        return None
    return sig.read_text().strip() or None
