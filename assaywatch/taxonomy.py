"""NCBI taxonomy ancestry, offline, so scope_taxids can match descendants.

`scope_taxids` lists the species an assay is meant to detect. GenBank records
are often annotated below species rank: a strain, or since NCBI's move to
binomial virus species names, a no-rank child that keeps the old common name
(3139435 "canine distemper virus" under 3052342 *Morbillivirus canis*). An exact
match drops all of those, which on 2026-10-17 excluded about 90% of in-scope
records in every scoped assay. Scope therefore means "the record's taxid, or any
ancestor of it, is listed".

The tree is a parent map plus a merged-taxid map, built from NCBI by
scripts/build_taxonomy_cache.py and read from a committed file, so reports
never touch the network. Merges matter in both directions: a scope list can name
a taxid NCBI has since merged (11232 -> 3052342), and so can an old record.
"""

from __future__ import annotations

import gzip
import json
from pathlib import Path


class Taxonomy:
    def __init__(self, parent: dict[int, int], merged: dict[int, int]) -> None:
        self.parent = parent
        self.merged = merged
        self._ancestors: dict[int, frozenset[int]] = {}
        self.unknown: set[int] = set()  # taxids asked about that the cache does not hold

    def canonical(self, taxid: int) -> int:
        """Follow merges to the taxid NCBI uses now."""
        seen = set()
        while taxid in self.merged and taxid not in seen:
            seen.add(taxid)
            taxid = self.merged[taxid]
        return taxid

    def ancestors(self, taxid: int) -> frozenset[int]:
        """The taxid itself (canonical) and every ancestor up to the root."""
        taxid = self.canonical(taxid)
        got = self._ancestors.get(taxid)
        if got is not None:
            return got
        if taxid not in self.parent:
            self.unknown.add(taxid)
        chain, t = [], taxid
        while t not in self._ancestors and t not in chain:
            chain.append(t)
            p = self.parent.get(t)
            if p is None or p == t:
                break
            t = p
        tail = self._ancestors.get(t, frozenset())
        for node in reversed(chain):
            tail = tail | {node}
            self._ancestors[node] = tail
        return self._ancestors[taxid]

    def within(self, taxid: int, scope: set[int]) -> bool:
        """True if `taxid` or an ancestor is in `scope` (already canonical)."""
        return not self.ancestors(taxid).isdisjoint(scope)


def load_taxonomy(path: Path | str) -> Taxonomy:
    """Read the cache written by scripts/build_taxonomy_cache.py."""
    with gzip.open(path, "rt") as fh:
        data = json.load(fh)
    parent = {int(k): int(v) for k, v in data["parent"].items()}
    merged = {int(k): int(v) for k, v in data["merged"].items()}
    return Taxonomy(parent, merged)


def taxonomy_from_config(cfg: dict) -> Taxonomy | None:
    """The cache named by ``drift.scope_taxonomy``, or None when no path is set.

    A path that is set but missing is an error, not a quiet fall back to exact
    matching: exact matching is the bug this module exists to fix.
    """
    path = (cfg.get("drift") or {}).get("scope_taxonomy")
    if not path:
        return None
    if not Path(path).exists():
        raise FileNotFoundError(
            f"drift.scope_taxonomy is {path!r} but the file is missing; "
            "build it with `python scripts/build_taxonomy_cache.py`"
        )
    return load_taxonomy(path)
