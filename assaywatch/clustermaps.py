"""Cluster maps for the `cluster` sub-lineage resolver (Mode C), wired 2026-10-24.

`assaywatch.subcluster` was built and tested on 2026-10-19 with no consumer:
`lineage.cluster_resolver` took a precomputed ``{record_id: label}`` map and the
pipeline never produced one. This module produces it, from the archives on disk,
for exactly the assays whose `lineage.sublineage` chain names ``cluster``. With the
shipped ``sublineage: {}`` nothing here runs and no archive is read.

What it clusters, and why only that:

- **An assay's evaluable records** (`detect`, `reduced`, `fail`), read back from its
  own retrieval group's archives. The all-pairs step is quadratic
  (`subcluster.cluster`), and records the screen could not judge contribute nothing
  to a per-lineage verdict anyway.
- **Masked over the amplicon span** (design decision A of
  `docs/2026-10-19-subtaxid-resolution.md`): `loci.pair_spans` finds every amplicon
  the screener could build and `subcluster.mask_regions` blanks it, so the lineage is
  defined by sequence the assay does not measure. Cluster on the binding sites and
  every assay shows a failing cluster by construction.
- **Whole-record archives only.** A window archive (`<stem>.windows.tsv.gz` beside the
  FASTA, see `windows.py`) holds only the stretches around sites, i.e. exactly the part
  the mask removes; clustering it would cluster nothing. Such archives are skipped
  with a warning rather than silently producing one giant cluster of Ns.

The primary forward/reverse pair finds the span; a pool's alternates sit on the same
sites within a few bases, so the mask covers them too (`buffer_bp` is for that).
"""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Any

from assaywatch.accession import strip_version
from assaywatch.drift import EVALUABLE
from assaywatch.fasta import read_fasta
from assaywatch.groups import group_slug
from assaywatch.loci import pair_spans
from assaywatch.subcluster import ClusterInfo, cluster_from_config


def cluster_assays(lineage_cfg: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """{assay_id: its `cluster:` block} for every chain that names the cluster resolver."""
    out: dict[str, dict[str, Any]] = {}
    for aid, entry in (lineage_cfg.get("sublineage") or {}).items():
        entry = entry or {}
        if "cluster" in (entry.get("chain") or []):
            out[aid] = entry.get("cluster") or {}
    return out


def search_params(cfg: dict[str, Any]) -> dict[str, Any]:
    """The widest site search any chemistry may use, as `windows.py` derives it.

    The span must cover every amplicon the screener could score, so the search runs
    at the largest mismatch budget and the loosest chance filter among the base
    scoring block and its per-chemistry overrides.
    """
    sc = cfg["scoring"]
    tables = [sc] + [{**sc, **o} for o in (sc.get("by_chemistry") or {}).values() if isinstance(o, dict)]
    evalues = [t.get("max_pair_evalue", 0.01) for t in tables]
    return {
        "max_mm": max(int(t.get("max_mismatches_searched", 6)) for t in tables),
        "max_e": float("inf") if any(e is None for e in evalues) else max(float(e) for e in evalues),
        "lo_bp": int(cfg["amplicon"]["min_bp"]),
        "hi_bp": int(cfg["amplicon"]["max_bp"]),
    }


def _is_window_archive(fasta: Path) -> bool:
    # Same convention as screen.sidecar_path, inlined so this module does not import
    # the screen (and so the screen's trigger closure does not grow).
    return fasta.with_name(fasta.name.removesuffix(".gz").removesuffix(".fasta") + ".windows.tsv.gz").exists()


def cluster_maps(
    lineage_cfg: dict[str, Any],
    assays: dict[str, Any],
    calls: list[dict[str, Any]],
    retrieved: Path,
    cfg: dict[str, Any],
) -> tuple[dict[str, dict[str, str]], dict[str, list[ClusterInfo]]]:
    """({assay_id: {record_id: cluster label}}, {assay_id: cluster infos}) for the cluster assays.

    Empty when no chain names ``cluster``; then no archive is opened. Labels are keyed
    by the unversioned accession, which `lineage.cluster_resolver` reaches from a
    versioned or an unversioned call id.
    """
    wanted = cluster_assays(lineage_cfg)
    if not wanted:
        return {}, {}
    search = search_params(cfg)
    maps: dict[str, dict[str, str]] = {}
    infos: dict[str, list[ClusterInfo]] = {}
    for aid, ccfg in wanted.items():
        assay = assays.get(aid)
        if assay is None or assay.target.taxid is None:
            warnings.warn(
                f"lineage.sublineage names {aid!r} for clustering but it has no registry taxid", stacklevel=2
            )
            maps[aid], infos[aid] = {}, []
            continue
        ids = {
            strip_version(r["record_id"]) for r in calls if r["assay_id"] == aid and r["call"] in EVALUABLE
        }
        pairs = [(assay.oligos.forward.matching_seq, assay.oligos.reverse.matching_seq)]
        group_dir = retrieved / str(assay.target.taxid) / group_slug(assay.target.query)
        records: list[tuple[str, str, list[tuple[int, int]]]] = []
        seen: set[str] = set()
        for fasta in sorted(group_dir.glob("*.fasta.gz")):
            if _is_window_archive(fasta):
                warnings.warn(
                    f"{fasta} is a window archive; clustering needs whole records, skipped", stacklevel=2
                )
                continue
            for rid, seq in read_fasta(fasta):
                base = strip_version(rid)
                if base not in ids or base in seen:
                    continue
                seen.add(base)
                seq = seq.upper()
                # Keyed by the unversioned accession: `lineage.cluster_resolver` looks a
                # call up by its id and then by its stripped id, so this key serves both.
                records.append((base, seq, pair_spans(seq, pairs, cfg, **search)))
        labels, info = cluster_from_config(records, ccfg)
        maps[aid], infos[aid] = labels, info
    return maps, infos
