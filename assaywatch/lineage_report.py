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


def read_calls_with_taxid(calls_path: Path, metadata: dict, taxid_sidecar: dict) -> dict[str, list[dict]]:
    """Read calls table and enrich with taxids from metadata.
    
    Returns dict mapping assay_id -> list of call dicts.
    """
    calls_by_assay = defaultdict(list)
    
    with gzip.open(calls_path, "rt") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            assay_id = row.get("assay_id", "")
            accession = row.get("accession", "")
            
            # Enrich with taxid
            taxid = None
            if accession in metadata:
                taxid = metadata[accession].taxid
            if taxid is None and accession in taxid_sidecar:
                taxid = taxid_sidecar[accession]
            
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
    
    # Load metadata and backfill taxids
    meta_paths = sorted(args.retrieved.glob("*.meta.tsv.gz"))
    metadata = {}
    for meta_path in meta_paths:
        metadata.update(load_record_metadata(
            meta_path,
            taxid_backfill_path=args.retrieved / ".meta.taxid.backfill.tsv.gz",
        ))
    
    # Create taxid sidecar dict from metadata
    taxid_sidecar = {acc: meta.taxid for acc, meta in metadata.items() if meta.taxid}
    
    # Read calls
    calls_by_assay = read_calls_with_taxid(args.calls, metadata, taxid_sidecar)
    
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
