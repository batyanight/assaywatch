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

    The rest of the header is dropped here and kept by `read_fasta_titled`. This
    name keeps its two-value shape because about twenty call sites unpack exactly
    two values, several of them `dict(read_fasta(...))`.
    """
    for rid, seq, _ in read_fasta_titled(path):
        yield rid, seq


def read_fasta_titled(path: Path) -> Iterator[tuple[str, str, str]]:
    """Yield (record_id, sequence, description): the header's first word, the
    sequence, and the remainder of the header with surrounding space stripped.

    The description is where a GenBank record says what it actually is, and for
    some taxa it is the only place. NCBI stopped assigning influenza subtype
    taxids to new deposits, so `Influenza A virus (A/Wisconsin/52/2026(H3N2))
    segment 4 ...` is the one statement that this record is H3N2 -- the taxid is
    the parent species and no Entrez field indexes the parenthesised form
    precisely. `target.title_requires` reads this to keep a subtype assay's
    denominator to its own subtype; see assaywatch.screen.title_allows.

    The description is "" for a header that is only an identifier, which
    `title_allows` treats as unknown rather than as matching.
    """
    opener = gzip.open if str(path).endswith(".gz") else open
    rid, desc, chunks = None, "", []
    with opener(path, "rt") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith(">"):
                if rid is not None:
                    yield rid, "".join(chunks), desc
                parts = line[1:].split(None, 1)
                rid = parts[0] if parts else ""
                desc = parts[1].strip() if len(parts) > 1 else ""
                chunks = []
            elif line:
                if rid is None:
                    # Content before any header: not FASTA, however it got here.
                    raise NotFasta(f"{path}: first non-blank line is not a FASTA header: {line[:120]!r}")
                # Whitespace inside a sequence line is formatting, not sequence.
                chunks.append("".join(line.split()))
    if rid is not None:
        yield rid, "".join(chunks), desc
