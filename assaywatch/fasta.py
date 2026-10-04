"""Minimal FASTA reader. pyfastx replaces this in Phase 1 once files get large."""

from __future__ import annotations

import gzip
from collections.abc import Iterator
from pathlib import Path


def read_fasta(path: Path) -> Iterator[tuple[str, str]]:
    """Yield (record_id, sequence). record_id is the header up to the first space."""
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
                # Whitespace inside a sequence line is formatting, not sequence.
                chunks.append("".join(line.split()))
    if rid is not None:
        yield rid, "".join(chunks)
