"""Per-lineage report generation.

Reads the calls table and generates a markdown report showing per-lineage
detection statistics for each assay. This is phase 1 output (reporting only;
verdict changes come in phase 2).

    python -m assaywatch.lineage_report <calls.tsv.gz> --config <config.yaml> --out <outdir>
"""

import argparse
import sys
from pathlib import Path
import gzip
import csv
from collections import defaultdict

from assaywatch.lineage import (
    load_taxa_cache,
    per_lineage_stats,
    LineageStats,
)
from assaywatch.retrieve import load_record_metadata
from assaywatch.score import load_config


# Below this share of call rows carrying a taxid, the join is assumed broken.
MIN_RESOLVED_SHARE = 0.5


def read_calls_with_taxid(calls_path: Path, metadata: dict, taxid_sidecar: dict) -> dict[str, list[dict]]:
    """Read calls table and enrich with taxids from metadata.
    
    Returns dict mapping assay_id -> list of call dicts.
    """
    calls_by_assay = defaultdict(list)
    
    with gzip.open(calls_path, "rt") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            assay_id = row.get("assay_id", "")
            # The calls table identifies a record by `record_id` and carries the
            # VERSIONED accession (AB027157.1), while the metadata and the taxid
            # backfill sidecar are keyed UNVERSIONED (AB027157). Match on both.
            accession = row.get("record_id") or row.get("accession", "")
            base = accession.split(".")[0]

            taxid = None
            for key in (accession, base):
                meta = metadata.get(key)
                if meta is not None and meta.taxid is not None:
                    taxid = meta.taxid
                    break
                if key in taxid_sidecar:
                    taxid = taxid_sidecar[key]
                    break
            
            call_row = dict(row)
            call_row["taxid"] = taxid
            calls_by_assay[assay_id].append(call_row)
    
    return dict(calls_by_assay)


def render_lineage_report(
    calls_by_assay: dict[str, list[dict]],
    taxa_cache: dict[int, str],
    taxid_sidecar: dict,
    min_records: int = 20,
) -> str:
    """Render markdown report of per-lineage statistics."""
    lines = [
        "# Per-Lineage Detection Analysis",
        "",
        "Each assay's records are grouped by their NCBI taxonomic lineage.",
        "Statistics show detected share and confidence interval per lineage.",
        "Lineages below the floor (< {} evaluable records) are omitted.".format(min_records),
        "",
    ]
    
    for assay_id in sorted(calls_by_assay.keys()):
        calls = calls_by_assay[assay_id]
        stats = per_lineage_stats(calls, taxa_cache, taxid_sidecar, min_records=min_records)
        
        if not stats:
            continue
        
        lines.append(f"## {assay_id}")
        lines.append("")
        
        # Table header
        lines.append("| Lineage | N Evaluable | N Detected | Share | 95% CI |")
        lines.append("|---|---|---|---|---|")
        
        for stat in stats:
            ci_str = f"[{stat.ci_lower:.2%}, {stat.ci_upper:.2%}]"
            lines.append(
                f"| {stat.lineage_name} | {stat.n_evaluable} | {stat.n_detected} | "
                f"{stat.share:.1%} | {ci_str} |"
            )
        
        lines.append("")
    
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("calls", type=Path, help="Calls table (TSV.GZ)")
    ap.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    ap.add_argument("--config", type=Path, default=Path("config.yaml"))
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)
    
    cfg = load_config(args.config)
    lineage_cfg = cfg.get("lineage", {})
    
    # Load taxa cache
    taxa_cache_path = lineage_cfg.get("taxa_cache", "docs/taxa-cache.json")
    taxa_cache = load_taxa_cache(taxa_cache_path)
    
    # accession -> taxid, keyed unversioned. Two sources, cheapest first:
    # the backfill sidecar (one file, covers records retrieved before the taxid
    # field existed), then any archive metadata that already carries a taxid
    # column. Archives live at <retrieved>/<taxid>/<group>/, so this is rglob.
    taxid_sidecar = {}
    sidecar_path = args.retrieved / ".meta.taxid.backfill.tsv.gz"
    if sidecar_path.exists():
        with gzip.open(sidecar_path, "rt") as f:
            next(f, None)
            for line in f:
                acc, _, tx = line.rstrip("\n").partition("\t")
                if tx.isdigit():
                    taxid_sidecar[acc.split(".")[0]] = int(tx)
    print(f"{len(taxid_sidecar)} taxids from {sidecar_path.name}", file=sys.stderr)

    n_from_meta = 0
    for meta_path in sorted(args.retrieved.rglob("*.meta.tsv.gz")):
        with gzip.open(meta_path, "rt") as f:
            header = (f.readline() or "").rstrip("\n").split("\t")
            if "taxid" not in header or "accession" not in header:
                continue  # pre-taxid archive; the sidecar covers it
            ai, ti = header.index("accession"), header.index("taxid")
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) > max(ai, ti) and parts[ti].isdigit():
                    taxid_sidecar[parts[ai].split(".")[0]] = int(parts[ti])
                    n_from_meta += 1
    print(f"{n_from_meta} taxids from archive metadata", file=sys.stderr)

    metadata = {}
    
    # Read calls
    calls_by_assay = read_calls_with_taxid(args.calls, metadata, taxid_sidecar)

    # A silently broken join (wrong column, versioned vs unversioned accessions)
    # yields a report of nothing but "unresolved", which looks like a finding
    # about the data rather than a bug. Refuse to write that.
    n_rows = sum(len(v) for v in calls_by_assay.values())
    n_taxid = sum(1 for v in calls_by_assay.values() for r in v if r["taxid"] is not None)
    share = n_taxid / n_rows if n_rows else 0.0
    print(f"taxid resolved for {n_taxid}/{n_rows} call rows ({share:.1%})", file=sys.stderr)
    if n_rows and share < MIN_RESOLVED_SHARE:
        print(
            f"error: only {share:.1%} of call rows resolved to a taxid "
            f"(expected >= {MIN_RESOLVED_SHARE:.0%}). The accession join is probably "
            f"broken, or the backfill sidecar is missing. Not writing lineage.md.",
            file=sys.stderr,
        )
        return 1

    # Render report
    min_records = lineage_cfg.get("min_records_per_lineage", 20)
    md = render_lineage_report(calls_by_assay, taxa_cache, taxid_sidecar, min_records=min_records)
    
    # Write output
    args.out.mkdir(parents=True, exist_ok=True)
    report_path = args.out / "lineage.md"
    report_path.write_text(md)
    
    print(f"wrote {report_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
