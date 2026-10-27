"""Minimal FASTA reader. pyfastx replaces this in Phase 1 once files get large."""

from __future__ import annotations

import gzip
from collections.abc import Iterator
from pathlib import Path


class NotFasta(ValueError):
    """A file that was handed to `read_fasta` and is not FASTA."""


def read_fasta(path: Path) -> Iterator[tuple[str, str]]:
    """Yield (record_id, sequence). record_id is the header up to the first space.

    Raises `NotFasta` when the first non-blank line is not a header. This used to
    be silent: everything before the first '>' was discarded, so an error
    document, an HTML page or a truncated download yielded NO records, and
    `screen.py` then wrote a signed, header-only calls table and exited 0. That
    archive simply vanished from the drift denominator, which reads as an assay
    with less data rather than as a broken input -- the one failure mode the
    exclusion taxonomy cannot label, because the records never reach it.
    """
    opener = gzip.open if str(path).endswith(".gz") else open
    rid, chunks = None, []
    with opener(path, "rt") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith(">"):
                if rid is not None:
                    yield rid, "".join(chunks)
                parts = line[1:].split(None, 1)
                rid, chunks = (parts[0] if parts else ""), []
            elif line:
                if rid is None:
                    # Content before any header: not FASTA, however it got here.
                    raise NotFasta(f"{path}: first non-blank line is not a FASTA header: {line[:120]!r}")
                # Whitespace inside a sequence line is formatting, not sequence.
                chunks.append("".join(line.split()))
    if rid is not None:
        yield rid, "".join(chunks)
