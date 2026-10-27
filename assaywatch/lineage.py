"""Per-lineage detection analysis and verdicts.

Phase 1 of the estimand rebuild: assign records to lineages by NCBI taxid,
group calls by assay + lineage, and compute per-lineage detection shares with
the worst lineage driving the call.

Why lineages matter: a pan-family PCR can detect one clade perfectly and miss
another. Pooling dilutes the miss to a average, which a threshold cannot catch.
Per-lineage analysis asks: what is the worst-case detection among the clades
this assay was asked to detect?

Sub-taxid resolution (estimand "Phase 2", see
docs/journal/2026-10-19-subtaxid-resolution.md): some biologically distinct lineages
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

from assaywatch.accession import strip_version
from assaywatch.interval import wilson_interval

# scipy and statsmodels are imported inside worst_lineage_verdict, the only
# function that needs them, so that the pipeline rules which merely read
# titles or group records keep working without them. At module scope they
# broke the snakemake CI job, which installs neither (48a21b2).

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


#: Which calls count as a detection when a caller does not say. The same default as
#: `drift.DETECTED_CALLS`, and the same reason it is a PARAMETER everywhere below:
#: since 2026-10-27 `drift.reduced_not_detected_for` makes a `reduced` probe call not a
#: detection for probe chemistries, and this module used to hard-code the old answer.
#: For the 51 probe-bearing entries that put the lineage table -- and
#: `worst_lineage_verdict`, which can override a pooled status -- on a different
#: numerator from the verdict beside it: the influenza matrix assay read 6.5% pooled
#: and 72-100% per subtype from the same calls. Callers pass the assay's own
#: `detected_calls`; the default exists for tests and for primer-only assays.
DETECTED_DEFAULT: tuple[str, ...] = ("detect", "reduced")


def load_taxa_cache(cache_file: Path | str) -> dict[int, str]:
    """Load taxid -> name mapping from docs/taxa-cache.json."""
    try:
        with open(cache_file) as f:
            data = json.load(f)
        return {int(k): v for k, v in data.get("taxa", {}).items()}
    except FileNotFoundError:
        return {}


def name_lineages_from_taxonomy(taxa_cache: dict[int, str], taxonomy) -> dict[int, str]:
    """`taxa_cache` with a "Name (taxid)" label added for every species the tree names.

    docs/taxa-cache.json holds ten hand-entered names, so almost every lineage
    label was `taxid_10245` — unreadable in a note and in the per-species table.
    The taxonomy cache names 23,593 species, which is the same information for
    free. An entry already in `taxa_cache` wins, so a hand-written label is
    never overwritten. The taxid stays in the label: it is what a reader needs
    to look the lineage up.

    The label is only ever displayed or used as a grouping key, both of which
    one name per taxid satisfies. Nothing reads `LineageStats.taxid`, which a
    named label leaves unset.
    """
    if taxonomy is None:
        return taxa_cache
    out = dict(taxa_cache)
    for taxid, name in taxonomy.name.items():
        if taxid not in out and not name.startswith("unclassified "):
            out[taxid] = f"{name} ({taxid})"
    return out


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
        return cluster_map.get(rid) or cluster_map.get(strip_version(rid))

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


def sublineage_resolvers(
    lineage_cfg: dict,
    query_taxids: dict[str, int],
    cluster_maps: dict[str, dict[str, str]] | None = None,
) -> dict[str, list[Resolver]]:
    """Resolver chains for every assay named under ``lineage.sublineage``.

    ``query_taxids`` is assay_id -> the registry's ``target.taxid``. An assay
    with no entry is absent from the result, and its callers pass
    ``resolvers=None``, i.e. Phase 1 per-taxid grouping. ``cluster_maps`` is
    assay_id -> {record_id: label} from `clustermaps.cluster_maps`, consumed by
    a chain that names ``cluster``; absent, that resolver defers on every record.
    """
    entries = lineage_cfg.get("sublineage") or {}
    return {
        aid: build_resolvers(
            e or {}, query_taxid=query_taxids.get(aid), cluster_map=(cluster_maps or {}).get(aid)
        )
        for aid, e in entries.items()
    }


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


def confidence_interval(n_success: int, n_total: int) -> tuple[float, float]:
    """95% interval for a lineage's detected share. Wilson, as the pooled share uses.

    This was a Wald interval of its own, because the estimators lived in
    `drift.py` and nothing below that module could import them. The cost was not
    academic: Wald collapses to zero width at k = 0 and k = n, so the shipped
    2026-10-22 report offered "lineage Orthoflavivirus usutuense (428 records)
    detects only 0.0% (0.0%-0.0%)" as the evidence for a `declining` call -- on
    an assay the MediLabSecure EQA in docs/validation-cases.tsv records detecting
    Usutu. Six rows of `lineage.md` read [0.00%, 0.00%] for the same reason.
    Meanwhile the report header said "Intervals are Wilson 95%", which was true
    of the pooled numbers and false of every one of these.

    A per-lineage detected share is the same measurement as the pooled one on a
    better-chosen denominator, so it gets the same estimator. It now lives in
    `interval.py`, below both callers, rather than being copied into the second
    one; the reasoning for Wilson over Wald is there.
    """
    return wilson_interval(n_success, n_total)


def lineage_of(
    call: dict,
    taxa_cache: dict[int, str],
    taxid_sidecar: dict[str, int],
    resolvers: list[Resolver] | None = None,
) -> str:
    """The lineage label one call is grouped under: its taxid, then the resolver chain."""
    taxid = call.get("taxid")
    # If no taxid in the call, look it up via accession
    if taxid is None and "accession" in call and taxid_sidecar:
        # The sidecar is keyed on the unversioned accession, which is what the
        # record_id has to be reduced to; `str.split` never returns an empty
        # list, so the old `parts[0] if parts else ...` fallback was dead.
        taxid = taxid_sidecar.get(strip_version(call["record_id"]))
    if resolvers is None:
        return lineage_for_taxid(taxid, taxa_cache)
    return resolve_sublineage(call, taxid, taxa_cache, resolvers)


def lineages_never_covered(
    baseline_calls: list[dict],
    taxa_cache: dict[int, str],
    taxid_sidecar: dict[str, int],
    threshold: float,
    min_records_for_year: int,
    resolvers: list[Resolver] | None = None,
    detected_calls: tuple[str, ...] = DETECTED_DEFAULT,
) -> set[str]:
    """Lineages measured before the recent window that never cleared `threshold`.

    The per-lineage form of AssayDrift.ever_worked, and per year for the same
    reason: an aggregate baseline is diluted by the decline itself. Each call
    needs a ``year``. A lineage is *measured* in a year with at least
    `min_records_for_year` evaluable records, and *never covered* if it was
    measured in some year and reached the threshold in none.

    A lineage with no measured year is not in the set. That is the case the
    tool exists for -- a lineage new to the archive that the assay misses
    (2009 pandemic H1N1 against the 2003 Matrix assay) -- and it must still be
    able to drive ``declining``.
    """
    measured, worked = _measured_and_working(
        baseline_calls, taxa_cache, taxid_sidecar, threshold, min_records_for_year, resolvers, detected_calls
    )
    return measured - worked


def lineages_ever_covered(
    baseline_calls: list[dict],
    taxa_cache: dict[int, str],
    taxid_sidecar: dict[str, int],
    threshold: float,
    min_records_for_year: int,
    resolvers: list[Resolver] | None = None,
    detected_calls: tuple[str, ...] = DETECTED_DEFAULT,
) -> set[str]:
    """Lineages that cleared `threshold` in some measured year before the recent window.

    The positive counterpart of `lineages_never_covered`, and not its complement:
    a lineage with no measured earlier year is in neither set. Which one a caller
    wants depends on what it has to prove. To excuse a failing lineage you must
    show it never worked, so a new lineage is not excused. To let a failing
    lineage overturn a pooled verdict that itself never cleared the threshold,
    you must show the lineage did work, so a new lineage cannot carry that claim
    either. See AssayDrift._lineage_check.
    """
    _, worked = _measured_and_working(
        baseline_calls, taxa_cache, taxid_sidecar, threshold, min_records_for_year, resolvers, detected_calls
    )
    return worked


def _measured_and_working(
    baseline_calls: list[dict],
    taxa_cache: dict[int, str],
    taxid_sidecar: dict[str, int],
    threshold: float,
    min_records_for_year: int,
    resolvers: list[Resolver] | None = None,
    detected_calls: tuple[str, ...] = DETECTED_DEFAULT,
) -> tuple[set[str], set[str]]:
    """(lineages with a measured year, lineages that cleared `threshold` in one).

    One pass for both questions. A lineage is *measured* in a year holding at
    least `min_records_for_year` evaluable records.
    """
    counts: dict[tuple[str, int], list[int]] = defaultdict(lambda: [0, 0])
    for call in baseline_calls:
        if call["call"] not in ("detect", "reduced", "fail"):
            continue
        c = counts[(lineage_of(call, taxa_cache, taxid_sidecar, resolvers), call["year"])]
        c[0] += call["call"] in detected_calls
        c[1] += 1
    measured, worked = set(), set()
    for (lin, _), (det, n) in counts.items():
        if n >= min_records_for_year:
            measured.add(lin)
            if det / n >= threshold:
                worked.add(lin)
    return measured, worked


def per_lineage_stats(
    calls: list[dict],
    taxa_cache: dict[int, str],
    taxid_sidecar: dict[str, int],
    min_records: int = 20,
    resolvers: list[Resolver] | None = None,
    detected_calls: tuple[str, ...] = DETECTED_DEFAULT,
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
        by_lineage[lineage_of(call, taxa_cache, taxid_sidecar, resolvers)].append(call)

    results = []
    for lineage, lineage_calls in sorted(by_lineage.items()):
        n_eval = len(lineage_calls)
        if n_eval < min_records:
            continue  # Below floor; will be reported as "below floor" row

        n_det = sum(1 for c in lineage_calls if c["call"] in detected_calls)
        share = n_det / n_eval if n_eval > 0 else 0
        ci_lower, ci_upper = confidence_interval(n_det, n_eval)

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
    lineage_stats: list[LineageStats],
    threshold: float,
    method: str = "holm",
    alpha: float = 0.05,
) -> tuple[str | None, int | None]:
    """Determine verdict from per-lineage analysis.

    Apply the *method* multiple-testing correction across lineages -- Holm by
    default, and see the comment below for why it is not Benjamini-Hochberg. If
    *any* lineage is significantly below *threshold*, the assay is failing.

    Returns
    -------
    (verdict, worst_rejected_idx)
        verdict : "failing" | "detecting" | None (no assessable lineages)
        worst_rejected_idx : index into *lineage_stats* of the rejected lineage
            with the lowest share, or None when verdict is not "failing".
    """
    if not lineage_stats:
        return None, None

    try:
        from scipy.stats import binom
        from statsmodels.stats.multitest import multipletests
    except ImportError as e:
        raise SystemExit(
            "the per-lineage verdict needs scipy and statsmodels, which are the "
            "`lineage` extra:\n    pip install -e '.[lineage]'   (or conda env "
            "create -f environment.yml)\n"
            "They are optional on purpose -- grouping records, reading titles and the "
            "diagnostic lineage report all work without them, and CI runs one job "
            f"without them to prove it. But anything that computes a verdict needs them. ({e})"
        ) from e

    # Collect p-values (one-sided test: is share significantly below threshold?)
    # H0: share >= threshold
    # H1: share < threshold
    # For a binomial, p = P(X <= observed | n, p=threshold)
    # binom.cdf, not a sum of comb(n, k) * p**k * q**(n-k): above n ~ 1030,
    # comb overflows to inf while p**k underflows to 0, every term is nan, and a
    # nan p-value is never rejected -- so a large lineage could never fail.
    p_values = [float(binom.cdf(stat.n_detected, stat.n_evaluable, threshold)) for stat in lineage_stats]

    # Multiple-testing control across this assay's lineages. Family-wise by
    # default (Holm); `method` decides.
    if p_values:
        # `method` and `alpha` come from `lineage.multiple_testing` and
        # `lineage.alpha` in config.yaml. They were `"fdr_bh"` and statsmodels'
        # default 0.05, hardcoded, against the rule that no such number lives in
        # code -- and BH was the wrong family: the decision below is "ANY rejected
        # lineage fails the assay", and FDR controls the expected share of false
        # rejections among rejections, not the probability of at least one, which
        # is the event that decides the status. That needs FWER control (Holm 1979).
        reject, corrected_p, _, _ = multipletests(p_values, alpha=alpha, method=method)
        if any(reject):
            # Among rejected lineages, pick the one with the lowest share
            worst_idx = min(
                (i for i, r in enumerate(reject) if r),
                key=lambda i: lineage_stats[i].share,
            )
            return "failing", worst_idx

    return "detecting", None
