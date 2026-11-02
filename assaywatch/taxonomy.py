"""NCBI taxonomy ancestry, offline, so scope_taxids can match descendants.

`scope_taxids` lists the species an assay is meant to detect. GenBank records
are often annotated below species rank: a strain, or since NCBI's move to
binomial virus species names, a no-rank child that keeps the old common name
(3139435 "canine distemper virus" under 3052342 *Morbillivirus canis*). An exact
match drops all of those, which on 2026-10-17 excluded about 90% of in-scope
records in every scoped assay. Scope therefore means "the record's taxid, or any
ancestor of it, is listed".

Lineage grouping uses the same tree for two more things. A record's taxid is
rolled up to its species (`species_of`), so a no-rank child and its species are
one lineage: JC polyomavirus 10632 under 1891763 *Betapolyomavirus secuhominis*
otherwise reads as two, and the species copy looks new to the archive. And a
taxid under an "unclassified ..." node (`in_unclassified`) is a bucket of
untyped records, not a lineage: 1193974 "Human enterovirus" under "unclassified
Enterovirus" held 33 coxsackievirus A6 records in 2018.

The tree is a parent map, ranks, names and a merged-taxid map, built from NCBI by
scripts/build_taxonomy_cache.py and read from a committed file, so reports
never touch the network. Merges matter in both directions: a scope list can name
a taxid NCBI has since merged (11232 -> 3052342), and so can an old record.
"""

from __future__ import annotations

import gzip
import json
from pathlib import Path


class Taxonomy:
    def __init__(
        self,
        parent: dict[int, int],
        merged: dict[int, int],
        rank: dict[int, str] | None = None,
        name: dict[int, str] | None = None,
    ) -> None:
        self.parent = parent
        self.merged = merged
        self.rank = rank or {}  # absent = "no rank"
        self.name = name or {}
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

    def _path_up(self, taxid: int) -> list[int]:
        """The taxid (canonical) then its ancestors, nearest first."""
        path, t = [], self.canonical(taxid)
        while t is not None and t not in path:
            path.append(t)
            p = self.parent.get(t)
            t = None if p == t else p
        return path

    def species_of(self, taxid: int) -> int | None:
        """The nearest taxid at species rank, the taxid itself included; None above species."""
        return next((t for t in self._path_up(taxid) if self.rank.get(t) == "species"), None)

    def in_unclassified(self, taxid: int) -> bool:
        """True if the taxid or an ancestor is one of NCBI's "unclassified ..." nodes."""
        return any(self.name.get(t, "").startswith("unclassified ") for t in self._path_up(taxid))


def load_taxonomy(path: Path | str) -> Taxonomy:
    """Read the cache written by scripts/build_taxonomy_cache.py."""
    with gzip.open(path, "rt") as fh:
        data = json.load(fh)
    parent = {int(k): int(v) for k, v in data["parent"].items()}
    merged = {int(k): int(v) for k, v in data["merged"].items()}
    rank = {int(k): v for k, v in data.get("rank", {}).items()}
    name = {int(k): v for k, v in data.get("name", {}).items()}
    return Taxonomy(parent, merged, rank, name)


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
