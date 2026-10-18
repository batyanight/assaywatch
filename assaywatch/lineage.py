"""Per-lineage detection analysis and verdicts.

Phase 1 of the estimand rebuild: assign records to lineages by NCBI taxid,
group calls by assay + lineage, and compute per-lineage detection shares with
the worst lineage driving the call.

Why lineages matter: a pan-family PCR can detect one clade perfectly and miss
another. Pooling dilutes the miss to a average, which a threshold cannot catch.
Per-lineage analysis asks: what is the worst-case detection among the clades
this assay was asked to detect?
"""

from dataclasses import dataclass
from typing import Any
from pathlib import Path
import json
import gzip
import csv
from collections import defaultdict

import numpy as np
from scipy.special import comb
from statsmodels.stats.multitest import multipletests


@dataclass
class LineageStats:
    """Detection statistics for one assay + lineage combination."""

    assay_id: str
    lineage_name: str  # taxid, or "unresolved"
    taxid: int | None
    n_evaluable: int
    n_detected: int
    share: float  # n_detected / n_evaluable
    ci_lower: float
    ci_upper: float


def load_taxa_cache(cache_file: Path | str) -> dict[int, str]:
    """Load taxid -> name mapping from docs/taxa-cache.json."""
    try:
        with open(cache_file) as f:
            data = json.load(f)
        return {int(k): v for k, v in data.get("taxa", {}).items()}
    except FileNotFoundError:
        return {}


def lineage_for_taxid(taxid: int | None, taxa_cache: dict[int, str]) -> str:
    """Resolve a record's taxid to a lineage name."""
    if taxid is None:
        return "unresolved"
    return taxa_cache.get(taxid, f"taxid_{taxid}")


def confidence_interval_wald(n_success: int, n_total: int, z: float = 1.96) -> tuple[float, float]:
    """Wald (asymptotic normal) confidence interval for a binomial proportion."""
    if n_total == 0:
        return (0.0, 1.0)
    p = n_success / n_total
    se = np.sqrt(p * (1 - p) / n_total)
    return (max(0, p - z * se), min(1, p + z * se))


def per_lineage_stats(
    calls: list[dict],
    taxa_cache: dict[int, str],
    taxid_sidecar: dict[str, int],
    min_records: int = 20,
) -> list[LineageStats]:
    """Compute per-lineage detection stats for one assay's calls.
    
    Args:
        calls: List of call dicts, each with keys 'record_id', 'call', 'taxid' (optional)
        taxa_cache: taxid -> lineage name mapping
        taxid_sidecar: accession -> taxid mapping for backfilled records
        min_records: minimum evaluable records per lineage for assessability
    
    Returns:
        List of LineageStats, sorted by share ascending (worst first for call determination).
    """
    evaluable_calls = [c for c in calls if c["call"] in ("detect", "reduced", "fail")]
    
    # Group by lineage (derived from record's taxid)
    by_lineage = defaultdict(list)
    for call in evaluable_calls:
        taxid = call.get("taxid")
        # If no taxid in the call, look it up via accession
        if taxid is None and "accession" in call and taxid_sidecar:
            # Extract accession from record_id if needed
            parts = call["record_id"].split(".")
            accession = parts[0] if parts else call.get("accession", "")
            taxid = taxid_sidecar.get(accession)
        
        lineage = lineage_for_taxid(taxid, taxa_cache)
        by_lineage[lineage].append(call)
    
    results = []
    for lineage, lineage_calls in sorted(by_lineage.items()):
        n_eval = len(lineage_calls)
        if n_eval < min_records:
            continue  # Below floor; will be reported as "below floor" row
        
        n_det = sum(1 for c in lineage_calls if c["call"] in ("detect", "reduced"))
        share = n_det / n_eval if n_eval > 0 else 0
        ci_lower, ci_upper = confidence_interval_wald(n_det, n_eval)
        
        # Extract taxid from lineage name if present
        taxid_val = None
        if lineage.startswith("taxid_"):
            try:
                taxid_val = int(lineage.split("_")[1])
            except (IndexError, ValueError):
                pass
        
        results.append(
            LineageStats(
                assay_id="",  # Filled by caller
                lineage_name=lineage,
                taxid=taxid_val,
                n_evaluable=n_eval,
                n_detected=n_det,
                share=share,
                ci_lower=ci_lower,
                ci_upper=ci_upper,
            )
        )
    
    # Sort by share (ascending) so worst lineage comes first
    return sorted(results, key=lambda x: x.share)


def worst_lineage_verdict(lineage_stats: list[LineageStats], threshold: float) -> str | None:
    """Determine verdict from worst assessable lineage.
    
    Apply Benjamini-Hochberg correction across lineages before thresholding.
    Returns None if no lineages are assessable.
    """
    if not lineage_stats:
        return None
    
    # Collect p-values (one-sided test: is share significantly below threshold?)
    # H0: share >= threshold
    # H1: share < threshold
    # For a binomial, p = P(X <= observed | n, p=threshold)
    p_values = []
    for stat in lineage_stats:
        # Use cumulative binomial: P(X <= n_detected | n_evaluable, threshold)
        # This is a one-sided test lower tail
        p = sum(
            comb(stat.n_evaluable, k) * (threshold ** k) * ((1 - threshold) ** (stat.n_evaluable - k))
            for k in range(stat.n_detected + 1)
        )
        p_values.append(p)
    
    # Benjamini-Hochberg FDR control
    if p_values:
        reject, corrected_p, _, _ = multipletests(p_values, method="fdr_bh")
        # The worst lineage is lineage_stats[0] (lowest share)
        if reject[0]:
            return "failing"  # Worst lineage significantly below threshold
    
    # If worst lineage is not failing, the assay passes
    return "detecting"
