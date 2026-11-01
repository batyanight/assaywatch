"""Cross-link the glossary: a term named inside another term's definition
becomes a link to it.

The glossary defines 101 terms and they refer to one another constantly --
`detect` is defined in terms of `penalty`, which is defined in terms of the
`3' window`. Reading it meant scrolling back and forth.

THE WHOLE DIFFICULTY IS RESTRAINT. The terms include `call`, `site`, `fail`,
`flag`, `probe`, `drift` and `status`, which occur in nearly every definition.
Linking every occurrence would underline most of the page and make the links
worthless. Four rules keep it useful:

1. **First occurrence only**, per definition. The second mention of `penalty` in
   the same paragraph is the same idea; one link is an offer, five is noise.
2. **Never inside code.** `screen.py`, `detect_max` and `status: active` are
   identifiers, not prose references, and a link inside one is wrong.
3. **Never to itself.** A definition naming its own term is the subject, not a
   cross-reference.
4. **Longest alias wins**, so `Wilson / Newcombe interval` is matched before
   `interval`, and `review flag` before `flag`.

Linking is by word boundary and is case-insensitive, but the linked text keeps
the spelling the author used: `Drift` at the start of a sentence stays
capitalised.
"""

from __future__ import annotations

import re

#: `**term** — definition`, the glossary's one structural convention. The dash is
#: an em dash; a term line that used a hyphen would not be a definition here.
TERM_LINE = re.compile(r"^\*\*(?P<term>[^*]+)\*\*\s+(?P<sep>—|-)\s+(?P<body>.*)$")

#: Code spans, which linking must leave alone.
CODE_SPAN = re.compile(r"`[^`]*`")

#: An existing link's text, so a term inside one is not wrapped twice.
MD_LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")

#: Aliases shorter than this are not linked. Two-character tokens like `C1` and
#: `S0` appear inside identifiers and accession numbers far more often than they
#: appear as references, and the false positives cost more than the links gain.
MIN_ALIAS = 3


def slug(term: str) -> str:
    """A stable anchor id for a term."""
    base = term.split("(")[0].strip()
    base = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")
    return f"term-{base}" if base else "term"


def aliases(term: str) -> list[str]:
    """The spellings of `term` worth matching in other definitions.

    `status (active, draft, deprecated)` is referred to as `status`; the
    parenthetical lists its values rather than naming alternatives. But
    `Wilson / Newcombe interval` and `evaluable / assessable / coverage gap` are
    genuinely several terms sharing one definition, so each side of a slash is
    its own alias.
    """
    head = term.split("(")[0].strip()
    parts = [p.strip() for p in head.split("/")] if "/" in head else [head]
    out = []
    for p in parts:
        if len(p) >= MIN_ALIAS and p not in out:
            out.append(p)
    return out


def _protected(text: str) -> list[tuple[int, int]]:
    """Spans that must not be linked into: code, and existing links."""
    return [m.span() for m in CODE_SPAN.finditer(text)] + [m.span() for m in MD_LINK.finditer(text)]


def link_body(body: str, index: dict[str, str], own: set[str]) -> str:
    """Link the first mention of each other term in one definition's body."""
    used: set[str] = set()
    # Longest first, so `review flag` is matched before `flag`.
    for alias in sorted(index, key=len, reverse=True):
        if alias in own or alias in used:
            continue
        pattern = re.compile(r"(?<![\w-])" + re.escape(alias) + r"(?![\w-])", re.IGNORECASE)
        spans = _protected(body)
        for m in pattern.finditer(body):
            if any(a <= m.start() < b for a, b in spans):
                continue
            # The matched text, not the alias: keep the author's capitalisation.
            body = f"{body[: m.start()]}[{m.group(0)}](#{index[alias]}){body[m.end() :]}"
            used.add(alias)
            break
    return body


def crosslink(markdown: str) -> tuple[str, int, list[str]]:
    """(glossary with anchors and cross-links, links added, ambiguous aliases).

    An alias defined by two different entries is NOT linked. `status` is the
    real case: the registry lifecycle (`active`, `draft`, `deprecated`) and the
    per-assay drift verdict are different concepts sharing a word, and a link
    would silently send a reader to whichever was defined first. Both still get
    their own anchor, so either can be linked to by hand; what is refused is
    guessing which one a sentence meant.
    """
    lines = markdown.split("\n")
    terms: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = TERM_LINE.match(line)
        if m:
            terms.append((i, m.group("term")))

    # Anchors must be unique even where two entries share a word, or the second
    # is unreachable and the first silently absorbs every link meant for it.
    anchors: dict[int, str] = {}
    seen: dict[str, int] = {}
    for i, term in terms:
        base = slug(term)
        seen[base] = seen.get(base, 0) + 1
        anchors[i] = base if seen[base] == 1 else f"{base}-{seen[base]}"

    defined: dict[str, list[str]] = {}
    own_by_line: dict[int, set[str]] = {}
    for i, term in terms:
        mine = set()
        for alias in aliases(term):
            defined.setdefault(alias, []).append(anchors[i])
            mine.add(alias)
        own_by_line[i] = mine

    ambiguous = sorted(a for a, v in defined.items() if len(v) > 1)
    index = {a: v[0] for a, v in defined.items() if len(v) == 1}

    added = 0
    for i, term in terms:
        m = TERM_LINE.match(lines[i])
        assert m is not None
        linked = link_body(m.group("body"), index, own_by_line.get(i, set()))
        added += linked.count("](#term-") - m.group("body").count("](#term-")
        # `attr_list` turns the trailing brace into an id on the bold run, which
        # makes `#term-penalty` a working target without promoting every term to
        # a heading and putting 101 entries into the table of contents.
        lines[i] = f"**{term}**{{: #{anchors[i]} }} {m.group('sep')} {linked}"
    return "\n".join(lines), added, ambiguous
