"""Per-lineage detection analysis and verdicts.

Phase 1 of the estimand rebuild: assign records to lineages by NCBI taxid,
group calls by assay + lineage, and compute per-lineage detection shares with
the worst lineage driving the call.

Why lineages matter: a pan-family PCR can detect one clade perfectly and miss
another. Pooling dilutes the miss to a average, which a threshold cannot catch.
Per-lineage analysis asks: what is the worst-case detection among the clades
this assay was asked to detect?

Sub-taxid resolution (estimand "Phase 2", see
docs/2026-10-19-subtaxid-resolution.md): some biologically distinct lineages
collapse into one NCBI taxid. A per-assay *resolver chain* assigns a finer
sub-lineage label from the cheapest sufficient signal — a more specific
per-record taxid, a label parsed from the record title, or a sequence-homology
cluster id — before falling back to the taxid. The chain is opt-in: with
``resolvers=None`` (the default) grouping is exactly the per-taxid behaviour of
Phase 1, so an assay with no sub-lineage config is untouched.
"""

import json
import re
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.stats import binom
from statsmodels.stats.multitest import multipletests

# A resolver maps (call dict, resolved taxid, taxa cache) -> a sub-lineage
# label, or None to defer to the next resolver in the chain.
Resolver = Callable[[dict, "int | None", dict[int, str]], "str | None"]


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


# --- sub-taxid resolver chain -------------------------------------------
# Each factory returns a Resolver. A resolver returns a label or None; the
# chain tries resolvers in order (cheapest/most-reliable first) and the first
# non-None label wins. If every resolver defers, resolve_sublineage falls back
# to the plain taxid label, so an unconfigured assay behaves as in Phase 1.


def subtaxid_resolver(query_taxid: int | None = None) -> Resolver:
    """Group by the record's own taxid when it is finer than the query taxid.

    Mode A in the design doc (e.g. Avipoxvirus: fowlpox 10261 vs canarypox
    10264, both below query 10260). A record sitting at the *parent* query
    taxid carries no sub-lineage signal here, so it returns None to let a
    title or cluster resolver try — this is what keeps the 76% of influenza
    Matrix records stuck at parent 11320 from short-circuiting the title
    resolver.

    Note: "finer than" is approximated as "present and != query_taxid". The
    taxa cache has no ancestry, and in practice a record retrieved under
    txidX[Organism:exp] carries X or a descendant, so a non-parent taxid is a
    genuine sub-taxon. A stray sibling taxid would be grouped on its own,
    which is harmless (it just gets its own row).
    """

    def _resolve(call: dict, taxid: int | None, taxa_cache: dict[int, str]) -> str | None:
        if taxid is None:
            return None
        if query_taxid is not None and taxid == query_taxid:
            return None
        return lineage_for_taxid(taxid, taxa_cache)

    return _resolve


def title_resolver(pattern: str) -> Resolver:
    """Group by a label parsed from the record title.

    Mode B (e.g. influenza subtype ``(H5N1)`` via ``r'\\((H\\d+N\\d+)\\)'``).
    If the pattern has a capture group, group 1 is the label; otherwise the
    whole match is used. No match -> None (defer). A missing title -> None,
    so this is safe before report.py threads titles into the call dicts.
    """

    rx = re.compile(pattern)

    def _resolve(call: dict, taxid: int | None, taxa_cache: dict[int, str]) -> str | None:
        m = rx.search(call.get("title") or "")
        if not m:
            return None
        return m.group(1) if m.groups() else m.group(0)

    return _resolve


def cluster_resolver(cluster_map: dict[str, str]) -> Resolver:
    """Group by a precomputed sequence-homology cluster id.

    Mode C (e.g. Bd BdGPL/BdCAPE). ``cluster_map`` maps record_id (versioned
    or unversioned accession) to a stable cluster label produced by
    assaywatch.subcluster. No entry -> None (defer).
    """

    def _resolve(call: dict, taxid: int | None, taxa_cache: dict[int, str]) -> str | None:
        rid = call.get("record_id", "")
        return cluster_map.get(rid) or cluster_map.get(rid.split(".")[0])

    return _resolve


def build_resolvers(
    assay_cfg: dict,
    *,
    query_taxid: int | None = None,
    cluster_map: dict[str, str] | None = None,
) -> list[Resolver]:
    """Build a resolver chain for one assay from its ``sublineage`` config.

    Config shape (per assay, under the top-level ``sublineage`` block)::

        chain: [subtaxid, title]
        title:   {pattern: '\\((H\\d+N\\d+)\\)'}
        cluster: {...}            # consumed by subcluster, not here

    An empty/absent config yields ``[subtaxid_resolver()]``, which combined
    with the taxid fallback reproduces Phase 1 grouping.
    """
    chain = assay_cfg.get("chain") or ["subtaxid"]
    resolvers: list[Resolver] = []
    for i, name in enumerate(chain):
        if name == "subtaxid":
            if query_taxid is None and i < len(chain) - 1:
                # Without the query taxid, a parent-level record resolves to the
                # parent's own label instead of deferring, so nothing after
                # subtaxid would ever run. Fail rather than silently pool.
                raise ValueError(f"subtaxid before {chain[i + 1]!r} needs the assay's query taxid")
            resolvers.append(subtaxid_resolver(query_taxid))
        elif name == "title":
            pattern = (assay_cfg.get("title") or {}).get("pattern")
            if not pattern:
                raise ValueError(f"title resolver needs a 'pattern' (assay cfg: {assay_cfg!r})")
            resolvers.append(title_resolver(pattern))
        elif name == "cluster":
            resolvers.append(cluster_resolver(cluster_map or {}))
        else:
            raise ValueError(f"unknown sub-lineage resolver {name!r}")
    return resolvers


def sublineage_resolvers(lineage_cfg: dict, query_taxids: dict[str, int]) -> dict[str, list[Resolver]]:
    """Resolver chains for every assay named under ``lineage.sublineage``.

    ``query_taxids`` is assay_id -> the registry's ``target.taxid``. An assay
    with no entry is absent from the result, and its callers pass
    ``resolvers=None``, i.e. Phase 1 per-taxid grouping.
    """
    entries = lineage_cfg.get("sublineage") or {}
    return {aid: build_resolvers(e or {}, query_taxid=query_taxids.get(aid)) for aid, e in entries.items()}


def title_assays(lineage_cfg: dict) -> set[str]:
    """Assays whose chain parses titles, so only their records' titles are read."""
    entries = lineage_cfg.get("sublineage") or {}
    return {aid for aid, e in entries.items() if "title" in ((e or {}).get("chain") or [])}


def resolve_sublineage(
    call: dict,
    taxid: int | None,
    taxa_cache: dict[int, str],
    resolvers: list[Resolver],
) -> str:
    """Run the resolver chain; first non-None label wins, else the taxid label."""
    for resolver in resolvers:
        label = resolver(call, taxid, taxa_cache)
        if label is not None:
            return label
    return lineage_for_taxid(taxid, taxa_cache)


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
    resolvers: list[Resolver] | None = None,
) -> list[LineageStats]:
    """Compute per-lineage detection stats for one assay's calls.

    Args:
        calls: List of call dicts, each with keys 'record_id', 'call', and
            optionally 'taxid', 'accession', 'title'.
        taxa_cache: taxid -> lineage name mapping
        taxid_sidecar: accession -> taxid mapping for backfilled records
        min_records: minimum evaluable records per lineage for assessability
        resolvers: optional sub-taxid resolver chain. When None, records are
            grouped by taxid exactly as in Phase 1. When provided, each
            record's group is resolve_sublineage(...), which may split a
            taxid into finer sub-lineages (subtype, cluster) or fall back to
            the taxid label.

    Returns:
        List of LineageStats, sorted by share ascending (worst first for call determination).
    """
    evaluable_calls = [c for c in calls if c["call"] in ("detect", "reduced", "fail")]

    # Group by lineage (derived from record's taxid, then the resolver chain).
    by_lineage = defaultdict(list)
    for call in evaluable_calls:
        taxid = call.get("taxid")
        # If no taxid in the call, look it up via accession
        if taxid is None and "accession" in call and taxid_sidecar:
            # Extract accession from record_id if needed
            parts = call["record_id"].split(".")
            accession = parts[0] if parts else call.get("accession", "")
            taxid = taxid_sidecar.get(accession)

        if resolvers is None:
            lineage = lineage_for_taxid(taxid, taxa_cache)
        else:
            lineage = resolve_sublineage(call, taxid, taxa_cache, resolvers)
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


def worst_lineage_verdict(
    lineage_stats: list[LineageStats], threshold: float
) -> tuple[str | None, int | None]:
    """Determine verdict from per-lineage analysis.

    Apply Benjamini-Hochberg correction across lineages.  If *any* lineage is
    significantly below *threshold*, the assay is failing.

    Returns
    -------
    (verdict, worst_rejected_idx)
        verdict : "failing" | "detecting" | None (no assessable lineages)
        worst_rejected_idx : index into *lineage_stats* of the rejected lineage
            with the lowest share, or None when verdict is not "failing".
    """
    if not lineage_stats:
        return None, None

    # Collect p-values (one-sided test: is share significantly below threshold?)
    # H0: share >= threshold
    # H1: share < threshold
    # For a binomial, p = P(X <= observed | n, p=threshold)
    # binom.cdf, not a sum of comb(n, k) * p**k * q**(n-k): above n ~ 1030,
    # comb overflows to inf while p**k underflows to 0, every term is nan, and a
    # nan p-value is never rejected -- so a large lineage could never fail.
    p_values = [float(binom.cdf(stat.n_detected, stat.n_evaluable, threshold)) for stat in lineage_stats]

    # Benjamini-Hochberg FDR control
    if p_values:
        reject, corrected_p, _, _ = multipletests(p_values, method="fdr_bh")
        if any(reject):
            # Among rejected lineages, pick the one with the lowest share
            worst_idx = min(
                (i for i, r in enumerate(reject) if r),
                key=lambda i: lineage_stats[i].share,
            )
            return "failing", worst_idx

    return "detecting", None
