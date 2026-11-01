"""Split a curator note into its dated episodes, newest first.

A curator note is written as a running record: a curator adds to it each time
they check something, and each addition opens with a capitalised headline and a
date -- `OLIGO SOURCE FOUND 2026-10-23`, `SCOPE TRIAGE 2026-10-20, decision
HELD`, `RESOLVED 2026-10-23`. Read top to bottom it is oldest first, which is
the wrong order for someone who wants to know where the entry stands now.

WHAT THE NOTES ACTUALLY LOOK LIKE, measured across the 203 that exist rather
than assumed:

    multi-paragraph                          31 of 203
    contain at least one ISO date           202 of 203
    every paragraph carries a date           31
    contain a back-reference ("above",
      "below", "earlier")                    73

So most notes are ONE paragraph with several dates inside it, and reordering is
only safe where the text does not point at its own layout.

TWO RULES KEEP THIS HONEST.

1. **Nothing is lost.** `episodes` partitions the note: concatenating the
   output, ignoring whitespace, reproduces the input exactly. `split_is_lossless`
   asserts it and the renderer refuses to reorder when it does not hold, so a
   note that defeats the parser is shown whole and unaltered instead.

2. **A note that refers to its own order is never reordered.** 73 notes say
   "the above" or "see below". Moving a paragraph under one of those makes the
   record wrong, which is worse than showing it oldest-first.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

#: An ISO date in the prose. The notes use no other format.
DATE = re.compile(r"\b(20\d\d-\d\d-\d\d)\b")

#: The start of a new episode: a run of capitals opening a sentence, which is
#: how every curator has marked one. Two words minimum, so an acronym mid
#: sentence (`PCR`, `DOI`, `NCBI`) does not split the text.
HEADLINE = re.compile(r"(?:(?<=^)|(?<=[.;?]\s))((?:[A-Z][A-Z0-9'’()/-]*\s+){1,}[A-Z][A-Z0-9'’()/-]*)")

#: Phrases that make a note depend on its own order.
BACK_REFERENCE = re.compile(r"\b(above|below|earlier here|that paragraph|preceding)\b", re.I)


@dataclass(frozen=True)
class Episode:
    """One dated addition to a note. `date` is "" when the text carries none."""

    date: str
    text: str


def _flatten(note: str) -> str:
    return " ".join(note.split())


def episodes(note: str) -> list[Episode]:
    """Partition a note into episodes in the order they were written.

    Paragraph breaks are honoured first; within a paragraph the text is split
    at capitalised headlines. A chunk inherits the date of the first ISO date
    inside it.
    """
    chunks: list[str] = []
    for para in (p for p in re.split(r"\n\s*\n", note) if p.strip()):
        flat = _flatten(para)
        starts = [m.start(1) for m in HEADLINE.finditer(flat)]
        # A headline at position 0 opens the paragraph rather than splitting it.
        starts = [s for s in starts if s > 0]
        bounds = [0, *starts, len(flat)]
        for a, b in zip(bounds, bounds[1:], strict=False):
            piece = flat[a:b].strip()
            if piece:
                chunks.append(piece)
    out = []
    for c in chunks:
        m = DATE.search(c)
        out.append(Episode(date=m.group(1) if m else "", text=c))
    return out


def split_is_lossless(note: str, eps: list[Episode]) -> bool:
    """Does the split reproduce the note, ignoring whitespace?"""
    return "".join(e.text for e in eps).replace(" ", "") == _flatten(note).replace(" ", "")


def reorderable(note: str, eps: list[Episode]) -> bool:
    """May these episodes be shown newest first?

    Only when there is more than one, every one carries a date, the split is
    lossless, and the note never points at its own order.
    """
    return (
        len(eps) > 1
        and all(e.date for e in eps)
        and split_is_lossless(note, eps)
        and not BACK_REFERENCE.search(note)
    )


def newest_first(note: str) -> tuple[list[Episode], bool]:
    """(episodes to display, whether they were reordered).

    Sorting is stable, so two additions made on the same day keep the order the
    curator wrote them in.
    """
    eps = episodes(note)
    if not reorderable(note, eps):
        return eps or [Episode(date="", text=_flatten(note))], False
    return sorted(eps, key=lambda e: e.date, reverse=True), True
