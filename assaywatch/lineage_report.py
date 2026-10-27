"""Per-lineage report generation.

Reads the calls table and generates a markdown report showing per-lineage
detection statistics for each assay. Standalone per-lineage report. The verdict-changing logic lives in
assaywatch.drift._lineage_check; this module produces a diagnostic report.

    python -m assaywatch.lineage_report <calls.tsv.gz> --config <config.yaml> --registry <dir> --out <outdir>
"""

import argparse
import csv
import gzip
import sys
from collections import defaultdict
from pathlib import Path

from assaywatch import atomic
from assaywatch.accession import strip_version
from assaywatch.lineage import (
    load_taxa_cache,
    name_lineages_from_taxonomy,
    per_lineage_stats,
    sublineage_resolvers,
    title_assays,
)
from assaywatch.metadata import read_titles
from assaywatch.score import load_config
from assaywatch.taxonomy import taxonomy_from_config

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
            base = strip_version(accession)

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
    resolvers: dict[str, list] | None = None,
) -> str:
    """Render markdown report of per-lineage statistics.

    ``resolvers`` (assay_id -> sub-lineage chain) splits those assays below
    the taxid, exactly as drift's lineage check does; other assays group per taxid.
    """
    lines = [
        "# Per-Lineage Detection Analysis",
        "",
        "Each assay's records are grouped by their NCBI taxonomic lineage.",
        "Statistics show detected share and confidence interval per lineage.",
        f"Lineages below the floor (< {min_records} evaluable records) are omitted.",
        "",
    ]

    for assay_id in sorted(calls_by_assay.keys()):
        calls = calls_by_assay[assay_id]
        stats = per_lineage_stats(
            calls,
            taxa_cache,
            taxid_sidecar,
            min_records=min_records,
            resolvers=resolvers.get(assay_id) if resolvers else None,
        )

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
    ap.add_argument("--registry", type=Path, default=Path("registry"), help="for sub-lineage query taxids")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    lineage_cfg = cfg.get("lineage", {})

    # Load taxa cache, then name what the taxonomy can name. report.py already
    # did this and this module did not, so report.md said "lineage Haemoproteus
    # sp. (191679)" of the same lineage lineage.md called `taxid_191679`. Two
    # labels for one grouping key, in two files a reader is meant to cross-check.
    # No literal default: report.py reads this key with none, and a second home
    # for a PATH is how `lineage.taxid_backfill` came to be declared in
    # config.yaml and read nowhere while two modules hardcoded it.
    taxa_cache_path = lineage_cfg.get("taxa_cache")
    taxa_cache = (
        name_lineages_from_taxonomy(load_taxa_cache(taxa_cache_path), taxonomy_from_config(cfg))
        if taxa_cache_path
        else {}
    )

    # accession -> taxid, keyed unversioned. Two sources, cheapest first:
    # the backfill sidecar (one file, covers records retrieved before the taxid
    # field existed), then any archive metadata that already carries a taxid
    # column. Archives live at <retrieved>/<taxid>/<group>/, so this is rglob.
    taxid_sidecar = {}
    # From config (`lineage.taxid_backfill`), which until 2026-10-21 was declared
    # and read nowhere while this path was hardcoded here and in report.py.
    sidecar_path = Path(lineage_cfg.get("taxid_backfill") or args.retrieved / ".meta.taxid.backfill.tsv.gz")
    if sidecar_path.exists():
        with gzip.open(sidecar_path, "rt") as f:
            next(f, None)
            for line in f:
                acc, _, tx = line.rstrip("\n").partition("\t")
                if tx.isdigit():
                    taxid_sidecar[strip_version(acc)] = int(tx)
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
                    taxid_sidecar[strip_version(parts[ai])] = int(parts[ti])
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
    min_records = lineage_cfg.get("min_records_per_lineage", 30)
    resolvers = None
    if lineage_cfg.get("sublineage"):
        from assaywatch.validate import iter_files, load_assay

        query_taxids = {a.id: a.target.taxid for a in map(load_assay, iter_files(args.registry))}
        # KNOWN ASYMMETRY WITH report.py, recorded 2026-10-26 and deliberately not
        # fixed here. `report.py` builds its resolvers with `cluster_maps=` from
        # `clustermaps.cluster_maps`; this call omits that argument, so a `cluster`
        # chain would defer here and resolve there, and `lineage.md` and `report.md`
        # would disagree about the same assay. Inert today because `config.yaml` ships
        # `lineage.sublineage: {}`, so no chain exists to resolve either way. Not
        # fixed in passing because a `cluster` chain can turn a verdict `declining`
        # (docs/journal/2026-10-19-pan-family-cases.md), so making the two agree is a change
        # to what this report CLAIMS, not a tidy-up, and it needs tier-2 behind it.
        resolvers = sublineage_resolvers(lineage_cfg, query_taxids)
        wanted = title_assays(lineage_cfg)
        titles = read_titles(
            args.retrieved,
            {strip_version(r["record_id"]) for a in wanted for r in calls_by_assay.get(a, [])},
        )
        for a in wanted:
            for r in calls_by_assay.get(a, []):
                r["title"] = titles.get(strip_version(r["record_id"]))
    md = render_lineage_report(
        calls_by_assay, taxa_cache, taxid_sidecar, min_records=min_records, resolvers=resolvers
    )

    # Write output
    args.out.mkdir(parents=True, exist_ok=True)
    report_path = args.out / "lineage.md"
    atomic.write_text(report_path, md)

    print(f"wrote {report_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
