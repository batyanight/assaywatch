"""The one door to the assay YAMLs: read, validate, write and edit entries.

Why one module. Before this, `validate.py` parsed entries, `atomic.py` wrote files
safely, `groups.py` said where an assay's archives live, and 48 scripts read
`registry/` on their own: 14 globbed it, 18 called `yaml.safe_load` on it, and the
ones that WROTE an entry each did so differently (`resolve_citations` re-dumped the
whole document, `promote` replaced one line of text). Every one of those was a place
where a rule about the registry could be broken quietly. This module is where the
rules live, and `curate` and every script go through it.

The rules it enforces:
- an entry's `id` is its file name;
- a live entry (one in `registry/`) carries a verified DOI; `pending/` is read with
  `pending=True` and skips that rule;
- a write is atomic: the file is complete or absent, never half-written;
- an edit keeps the file's comments, key order and quoting, and is validated
  BEFORE it lands, so an edit that would break the schema changes nothing.

Reading uses PyYAML (fast, cached). Editing uses ruamel.yaml's round-trip mode,
which is what preserves comments; four entries carry a measurement note that a
whole-document rewrite would have thrown away.
"""

from __future__ import annotations

import hashlib
import io
import os
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from assaywatch.schema import Assay

#: Line width for every YAML this module writes, matching what resolve_citations
#: wrote before it, so a rewrite does not re-wrap the long `reference` strings.
_WIDTH = 120


class RegistryError(ValueError):
    """A registry that cannot be loaded. `problems` lists EVERY bad file, so one
    run of the validator reports them all rather than the first one per run."""

    def __init__(self, problems: list[tuple[Path, str]]) -> None:
        self.problems = problems
        lines = [f"{len(problems)} problem(s):"] + [f"  {p}: {msg}" for p, msg in problems]
        super().__init__("\n".join(lines))


# --- reading --------------------------------------------------------------------


def files(target: Path) -> Iterator[Path]:
    """The entry files under a directory, sorted, or the single file given."""
    target = Path(target)
    if target.is_dir():
        yield from sorted(p for p in target.glob("*.yaml") if p.name != "README.md")
    else:
        yield target


_CACHE: dict[tuple[str, int, int], Assay] = {}


def load_one(path: Path) -> Assay:
    """Parse and validate one entry.

    Parsing 214 YAMLs with PyYAML costs about two seconds and a single process asks for
    the same files several times (a report, a retrospective run and the tests each load
    the registry more than once). The parsed Assay is cached per (path, size, mtime), so
    an edited file is always re-read, and every caller gets its own deep copy: nobody
    can mutate another caller's assay through the cache.
    """
    path = Path(path)
    st = path.stat()
    key = (str(path), st.st_size, st.st_mtime_ns)
    cached = _CACHE.get(key)
    if cached is None:
        cached = _validate(path, yaml.safe_load(path.read_text()))
        _CACHE[key] = cached
    return cached.model_copy(deep=True)


def _validate(path: Path, data: Any) -> Assay:
    if not isinstance(data, dict):
        raise ValueError("top level is not a mapping")
    assay = Assay.model_validate(data)
    if assay.id != path.stem:
        raise ValueError(f"id '{assay.id}' does not match file name '{path.stem}'")
    return assay


def not_live_because(assay: Assay) -> str | None:
    """Why this entry may not sit in `registry/`, or None. The rule is a verified DOI."""
    if assay.citation.doi is None:
        return "no citation.doi; an assay without a published source belongs in pending/"
    if not assay.citation.doi_verified:
        return "citation.doi_verified is false; run scripts/resolve_citations.py, or move it to pending/"
    return None


def load(target: Path, *, pending: bool = False) -> dict[str, Assay]:
    """Every entry under `target`, keyed by id.

    Raises RegistryError naming every file that fails to parse, fails the schema, or
    (unless `pending`) is not allowed to be live.
    """
    out: dict[str, Assay] = {}
    problems: list[tuple[Path, str]] = []
    for path in files(target):
        try:
            assay = load_one(path)
        except (yaml.YAMLError, ValidationError, ValueError) as e:
            problems.append((path, _one_line(e)))
            continue
        why = None if pending else not_live_because(assay)
        if why:
            problems.append((path, why))
            continue
        out[assay.id] = assay
    if problems:
        raise RegistryError(problems)
    return out


def _one_line(e: Exception) -> str:
    text = str(e).strip()
    if isinstance(e, ValidationError):
        first = e.errors()[0]
        loc = ".".join(str(x) for x in first["loc"]) or "<root>"
        text = f"{loc}: {first['msg']}"
    return text.splitlines()[0] if text else type(e).__name__


# --- writing --------------------------------------------------------------------


def write_text(path: Path, text: str) -> None:
    """Write *text* to *path* via a sibling `.part`, then rename, so a reader sees
    either the previous contents or the complete new ones, never a truncated file.

    Snakemake deletes a FAILED job's outputs, but not those of a process that died
    outright (lid closed, `kill -9`, power loss), and a truncated `report.md` with a
    fresh mtime is a file `rule all` accepts. The `.part` sits beside the target so
    the rename never crosses a filesystem (which would silently become a copy). A
    leftover `.part` after a crash is inert: every consumer looks for the real name.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.part")
    tmp.write_text(text)
    os.replace(tmp, path)


def write(assay: Assay, path: Path) -> None:
    """Write a whole entry, keys in schema order, atomically.

    This is for a NEW entry. For a change to an existing file use `edit`, which keeps
    the file's comments; this rewrite would drop them.
    """
    path = Path(path)
    if assay.id != path.stem:
        raise ValueError(f"id '{assay.id}' does not match file name '{path.stem}'")
    doc = assay.model_dump(mode="json")
    write_text(path, yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=_WIDTH))


def edit(path: Path, changes: dict[str, Any]) -> Assay:
    """Set dotted keys in an existing entry, keep everything else, validate, then write.

        edit(path, {"citation.doi_verified": True, "amplicon_bp": 143})

    Each key names an existing parent mapping (KeyError otherwise, so a typo cannot
    grow a new branch the schema would then reject less clearly). The edited document
    is validated as an Assay BEFORE anything is written; on failure the file is
    untouched. Returns the entry as reloaded from disk.
    """
    from ruamel.yaml import YAML

    path = Path(path)
    rt = YAML(typ="rt")
    rt.preserve_quotes = True
    # Fold at the width entries are written at, so an edit does not widen the file: at an
    # effectively infinite width one edit re-emitted an already-folded curator note as a
    # single multi-thousand-character line and the diff was the whole note. Also write
    # `null` the way every entry already spells it rather than ruamel's default blank.
    rt.width = _WIDTH
    rt.representer.add_representer(
        type(None), lambda r, _: r.represent_scalar("tag:yaml.org,2002:null", "null")
    )
    doc = rt.load(path.read_text())
    for dotted, value in changes.items():
        *parents, leaf = dotted.split(".")
        node = doc
        for p in parents:
            if not isinstance(node, dict) or p not in node:
                raise KeyError(f"{dotted}: no mapping '{p}' in {path.name}")
            node = node[p]
        if not isinstance(node, dict):
            raise KeyError(f"{dotted}: parent is not a mapping in {path.name}")
        node[leaf] = value
    buf = io.StringIO()
    rt.dump(doc, buf)
    text = buf.getvalue()
    _validate(path, yaml.safe_load(text))
    write_text(path, text)
    return load_one(path)


# --- where an entry's archives live --------------------------------------------


def group_slug(assay_query: str | None) -> str:
    """Directory name for a retrieval group under its taxid: `all`, or a query hash."""
    if not assay_query:
        return "all"
    return "q" + hashlib.sha1(assay_query.strip().encode()).hexdigest()[:10]


def archive_dir(assay: Assay, retrieved: Path) -> Path:
    """`data/retrieved/<taxid>/<slug>/`: where this assay's sequence archives sit."""
    return Path(retrieved) / str(assay.target.taxid) / group_slug(assay.target.query)


# --- duplicate keys -------------------------------------------------------------
# PyYAML keeps the LAST of two equal keys and says nothing, which twice made the
# validator, the screen and the report all look at a subset of an entry. The
# pre-commit hook and `curate` both ask this.


class _DupeFinder(yaml.SafeLoader):
    def __init__(self, stream: str) -> None:
        super().__init__(stream)
        self.duplicates: list[tuple[str, int]] = []

    def construct_mapping(self, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
        seen: set[object] = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in seen:
                self.duplicates.append((str(key), key_node.start_mark.line + 1))
            seen.add(key)
        return super().construct_mapping(node, deep=deep)


_DupeFinder.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _DupeFinder.construct_mapping)


def duplicate_keys(text: str) -> list[tuple[str, int]]:
    """[(key, line)] for every mapping key given twice in one YAML document."""
    loader = _DupeFinder(text)
    try:
        loader.get_single_data()
        return loader.duplicates
    finally:
        loader.dispose()
