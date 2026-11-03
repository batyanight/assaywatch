"""How each assay's record mix changes over time, and what that does to its graph.

ROADMAP "Lineage composition over time" (designed and grilled 2026-11-02). An assay's
per-year detection share can move because detection WITHIN lineages changed (drift)
or because the MIX of lineages being sequenced changed. This stage separates the two,
using sequence clusters as lineages: composition windows (`subcluster.flanked_region`)
are sampled across deposit years, clustered at a per-assay cut, and every record is
assigned to its nearest sampled member.

REPORT-ONLY. Nothing here moves a status; like the trend, collection-year and
hierarchical lenses, it is printed beside the verdict.

Built in steps; the entry point `build` arrives at step 12. Until then this module
holds the stage's internals, each tested at its own boundary.
"""

from __future__ import annotations

import hashlib
from collections import defaultdict
from collections.abc import Sequence

from assaywatch.accession import strip_version
from assaywatch.subcluster import Region


def _order_key(record_id: str) -> tuple[bytes, str]:
    """Deterministic, input-order-free rank of a record: a hash of its accession
    WITHOUT version, so `.1` and `.2` of one record rank the same; the accession
    breaks the (vanishingly rare) hash tie."""
    acc = strip_version(record_id)
    return hashlib.blake2b(acc.encode(), digest_size=8).digest(), acc


def sample_windows(regions: Sequence[Region], years: Sequence[int], cap: int) -> list[int]:
    """Indices of the windows to cluster: at most `cap`, spread across deposit years.

    Rules, each pinned by a test in tests/test_composition.py:

    - Only full-flank windows are sampled (finding 2); short ones are assigned later.
    - Identical windows count once, keeping the lowest-ranked record: a clone deposited
      twenty times is one member of its lineage, not twenty.
    - ROUND-ROBIN across years, one window per year per pass, years in chronological
      order within a pass. A busy year therefore cannot crowd out a quiet one, which is
      the point: a lineage seen only in a quiet year must still be clustered.
    - Within a year, records are taken in `_order_key` order, so the same archive read
      in any order samples the same records.

    Returned in (year, rank) order.
    """
    if len(regions) != len(years):
        raise ValueError(f"{len(regions)} regions but {len(years)} years")
    best: dict[str, int] = {}
    for i, r in enumerate(regions):
        if not r.full_flank:
            continue
        j = best.get(r.seq)
        if j is None or _order_key(r.record_id) < _order_key(regions[j].record_id):
            best[r.seq] = i
    per_year: dict[int, list[int]] = defaultdict(list)
    for i in best.values():
        per_year[years[i]].append(i)
    queues = {y: sorted(ix, key=lambda i: _order_key(regions[i].record_id)) for y, ix in per_year.items()}
    chosen: list[int] = []
    depth = 0
    while len(chosen) < cap:
        took = False
        for y in sorted(queues):
            if depth < len(queues[y]) and len(chosen) < cap:
                chosen.append(queues[y][depth])
                took = True
        if not took:
            break
        depth += 1
    rank = {i: (years[i], _order_key(regions[i].record_id)) for i in chosen}
    return sorted(chosen, key=rank.__getitem__)
