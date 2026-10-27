"""Reading the calls table and the deposit dates: one loader, three consumers.

WHY A MODULE OF ITS OWN. These lived in `report.py`, and `sitedrift.py` and
`scripts/retrospective.py` both imported them from there -- so the module that
renders a document was also the project's calls-table I/O library, and its 1,228
lines were the four jobs its own `ReportModel` layer was introduced to separate.
Same move, same reason, as `interval.py` and `signature.py`.

MEMORY IS THE THING TO KNOW HERE. `read_calls` materialises the whole table as
one small dict per row: 2,688,879 rows on 2026-10-22. An earlier version kept
every column and took 3.6 GB; this one keeps the four or five fields anything
downstream reads and interns the footprint string, which brings it to roughly
1-1.5 GB. That is still the largest resident set in the pipeline, it scales as
assays x records, and three rules load it -- `report`, `site_drift` and
`lineage_analysis` -- two of which Snakemake can co-schedule. All three now
declare `resources: mem_mb` for that reason (Snakefile), because on SLURM a
`resources:` block is the sbatch request and an undeclared job is killed rather
than slowed. Nothing here streams or chunks; a registry twice this size needs
that before it needs anything else.
"""

from __future__ import annotations

import csv
import gzip
from collections import defaultdict
from contextlib import suppress
from pathlib import Path
from typing import Any

from assaywatch.accession import strip_version, version_of
from assaywatch.drift import FOOTPRINT_COLUMNS, FOOTPRINT_REQUIRED, footprint_signature


def _open(path: Path):
    return gzip.open(path, "rt") if str(path).endswith(".gz") else open(path)


def read_calls(path: Path, with_spans: set[str] | None = None) -> list[dict[str, Any]]:
    """The columns the drift statistic needs, one small dict per row.

    Loading every column of a two-million-row calls table as dicts took 3.6 GB;
    nothing downstream reads the other columns. The six mismatch columns are
    folded into ONE interned `footprint` string per row rather than carried as
    six, so the cost is a pointer per row and millions of identical exact-match
    footprints are a single object. A row has no `footprint` key when the columns
    are absent from the table OR the row's own scoring cells are blank (a row from
    an older screen that `collect.concatenate_screens` blank-filled), which
    `drift.assess` reads as "unknown" and not as "all the same".
    """
    with _open(path) as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if header is None:
            return []
        ia, ir, ic = header.index("assay_id"), header.index("record_id"), header.index("call")
        span_idx = (
            [header.index(c) for c in ("amplicon_start", "amplicon_end")]
            if with_spans and all(c in header for c in ("amplicon_start", "amplicon_end"))
            else None
        )
        # `exclusion` says why an unusable record was unusable (score.classify_exclusion).
        ie = header.index("exclusion") if "exclusion" in header else None
        # The best lone site's per-record E-value behind that label, for `apply_anchor_fdr`.
        ian = header.index("anchor_evalue") if "anchor_evalue" in header else None
        # For `apply_chance_pair_test`: the two primer penalties, carried ONLY on a
        # `fail` row whose probe site is absent. That is the only row the test can
        # move, and it is a small minority (26,691 of 132,496 evaluable rows on
        # 2026-10-25), so the memory this costs is bounded by those rows rather than
        # by the whole table - which is the constraint this function exists to respect.
        pp_idx = (
            [header.index(c) for c in ("probe_site", "fwd_penalty", "rev_penalty")]
            if all(c in header for c in ("probe_site", "fwd_penalty", "rev_penalty"))
            else None
        )
        # The footprint is known only where the row's own scoring columns are
        # populated (see drift.FOOTPRINT_REQUIRED). Having the six mismatch
        # columns in the HEADER is not enough: `collect.concatenate_screens` unions
        # the headers of old and new screens and blank-fills the cells an older
        # screen never had, so an older screen's rows arrive with all six columns
        # present and empty - indistinguishable from a clean record unless the
        # scoring cells beside them are checked. All six columns or none: a partial
        # footprint would compare unequal to a full one that agrees with it.
        fp_idx = (
            [header.index(c) for c in FOOTPRINT_COLUMNS]
            if all(c in header for c in (*FOOTPRINT_COLUMNS, *FOOTPRINT_REQUIRED))
            else None
        )
        req_idx = [header.index(c) for c in FOOTPRINT_REQUIRED] if fp_idx is not None else []
        rows = []
        for r in reader:
            if not r:
                continue
            row = {
                "assay_id": r[ia],
                "record_id": r[ir],
                "call": r[ic],
                "exclusion": (r[ie] if ie is not None and ie < len(r) else ""),
            }
            if ian is not None and ian < len(r) and r[ian] != "":
                row["anchor_evalue"] = float(r[ian])
            if pp_idx is not None and row["call"] == "fail" and all(i < len(r) for i in pp_idx):
                ps, fwd, rev = (r[i] for i in pp_idx)
                if ps in ("-", "") and fwd != "" and rev != "":
                    with suppress(ValueError):
                        row["probeless_penalties"] = (float(fwd), float(rev))
            if fp_idx is not None and all(i < len(r) and r[i] != "" for i in req_idx):
                row["footprint"] = footprint_signature(r[i] if i < len(r) else "" for i in fp_idx)
            if span_idx is not None and row["assay_id"] in with_spans:
                a, b = (r[i] if i < len(r) else "" for i in span_idx)
                if a and b:
                    row["amplicon_start"], row["amplicon_end"] = a, b
            rows.append(row)
        return rows


#: The label a lone anchor gets when it does not survive the archive-scale test.
CHANCE_ANCHOR = "chance_anchor"
#: Exclusion labels that rest on exactly one credible primer site.
LONE_ANCHOR_LABELS = frozenset({"diverged", "truncated", "no_pair"})


def apply_anchor_fdr(rows: list[dict[str, Any]], cfg: dict[str, Any]) -> dict[str, int]:
    """Relabel lone anchors that do not survive an archive-scale test. Off unless `drift.anchor_fdr` is set.

    `score.classify_exclusion` calls a lone primer site credible when its PER-RECORD
    E-value is under `scoring.max_site_evalue`. That threshold is set per test and
    applied across thousands of records, so an archive produces chance anchors in
    proportion to its size: 55 of Bd's 63 `diverged` records are 2014 JAM81 mRNAs
    with no ITS locus, anchored by the reverse primer at five or six mismatches
    (docs/journal/2026-10-23-wave2-diverged-and-patent.md). A `diverged` label there asserts
    the assay fails on a record that never held its target.

    Why Benjamini-Hochberg over the assay's rows and not "E times the record
    count": the product cannot tell a real failure set from a chance one. SIV Keele
    has real two-mismatch anchors on 90% of 8,252 records (E about 3e-5 each, so
    E x N is 0.25 and would fail a 0.05 cut) while Bd's chance anchors are 55 at
    5e-3 in 9,496 (E x N 47). Step-up BH separates them: thousands of small p's
    raise the threshold for each other and all pass; 55 at 5e-3 ranked among 9,000
    tests face k/m x q of about 2.5e-3 and fail. Rows that recorded no E count as
    p = 1. A per-record E is treated as a p-value, which it approximates for
    E << 1 (P(at least one) ~ E).

    THE FAMILY is `drift.anchor_fdr_family`, and the default changed on
    2026-10-27 after the first attempt at it was refuted by these tests.

    `tested` (default): rows where the test was actually PERFORMED -- a lone
    anchor was found and its E-value recorded -- whatever the exclusion label.
    `lone_anchor`: only the labels this function can relabel. `all_no_amplicon`:
    those plus every `no_site` row, which is what shipped before.

    `no_site` does not mean "no site": it means no CREDIBLE site, one having been
    found and failed `scoring.max_site_evalue`. Of 1,442,931 such rows on
    2026-10-26, 357,923 recorded an E-value and 1,085,008 did not, so the label
    mixes a test that failed to reject -- which a multiple-comparisons family
    must count, since counting the comparisons made is the point -- with a record
    where no hypothesis was tested at all. The latter enters as p = 1, can never
    be rejected or relabelled, and only enlarges m; and because the bar is
    k/m x q, a larger m TIGHTENS it for the rows that can move, so more real
    anchors are relabelled as chance.

    Measured by replaying results/2026-10-26 at q = 0.001: all_no_amplicon
    relabels 36,184 rows across 153 assays, `tested` 26,875 across 146, and
    `lone_anchor` 23,985 across 143. The 9,309 between the old default and
    `tested` moved purely on anchor-less padding, which scales with archive size.

    `lone_anchor` was the recommendation until these tests ran: it drops the
    357,923 genuine tests as well, loosening the bar until real chance anchors
    escape. `test_bd_shaped_chance_anchors_are_relabelled_and_the_real_deposits_are_not`
    is exactly that case -- Bd's 8,900 mRNA records anchored weakly at E 0.5 --
    and under `lone_anchor` m falls to 447 and all 55 chance anchors pass as
    real. The project's own worked example stopped being caught, which is how the
    recommendation was found to be wrong before it shipped.

    Only `diverged`, `truncated` and `no_pair` can move, to `chance_anchor`; a row
    with no recorded E (an older screen) is never relabelled, because unknown is
    not the same as chance. Returns {assay_id: rows relabelled}. Mutates `rows`.
    """
    q = (cfg.get("drift") or {}).get("anchor_fdr")
    if q is None:
        return {}
    q = float(q)
    if not 0 < q < 1:
        raise ValueError(f"drift.anchor_fdr must be between 0 and 1, got {q}")
    family = str((cfg.get("drift") or {}).get("anchor_fdr_family", "tested"))
    if family not in ("tested", "lone_anchor", "all_no_amplicon"):
        raise ValueError(
            f"drift.anchor_fdr_family must be tested, lone_anchor or all_no_amplicon, got {family!r}"
        )
    labels = LONE_ANCHOR_LABELS if family == "lone_anchor" else LONE_ANCHOR_LABELS | {"no_site"}
    by_assay: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        if r.get("call") != "no_amplicon" or (r.get("exclusion") or "") not in labels:
            continue
        # `tested` additionally requires that a test was actually PERFORMED on
        # this record: an anchor was found and its E-value recorded. A row with no
        # anchor at all had no hypothesis to test, so it is not a member of the
        # family; a row whose anchor was poor IS one, and belongs in m.
        if family == "tested" and "anchor_evalue" not in r:
            continue
        by_assay[r["assay_id"]].append(r)
    moved: dict[str, int] = {}
    for aid, rs in by_assay.items():
        m = len(rs)
        ps = sorted(min(1.0, float(r["anchor_evalue"])) if "anchor_evalue" in r else 1.0 for r in rs)
        # Step-up: the largest rank k with p_(k) <= k/m * q; everything at or below
        # p_(k) is rejected, so tied p-values share one fate.
        cut = -1.0
        for rank, p in enumerate(ps, 1):
            if p <= rank / m * q:
                cut = p
        for r in rs:
            if (r.get("exclusion") or "") not in LONE_ANCHOR_LABELS or "anchor_evalue" not in r:
                continue
            if min(1.0, float(r["anchor_evalue"])) > cut:
                r["exclusion"] = CHANCE_ANCHOR
                moved[aid] = moved.get(aid, 0) + 1
    return moved


#: The label a probe-less amplicon gets when its primers are too poor to be a real placement.
CHANCE_PAIR = "chance_pair"


def apply_chance_pair_test(
    rows: list[dict[str, Any]], cfg: dict[str, Any], probe_bars: dict[str, float]
) -> dict[str, int]:
    """Relabel `fail` rows that are a chance PAIR, not an amplicon. Off unless `drift.chance_pair_test`.

    `apply_anchor_fdr` above guards the case where ONE primer anchored by chance,
    and its docstring states the problem exactly: "a `diverged` label there
    asserts the assay fails on a record that never held its target". When BOTH
    primers anchor by chance and happen to face each other in range, the record
    gets an amplicon instead, so it becomes EVALUABLE and never enters that
    test's family. It then scores `fail`, because the probe has nowhere to bind
    in a locus that is not there. Measured 2026-10-25 over 134 groups: 26,691
    such rows in 6 probe-bearing assays, and
    `OPHIDIOMYCES_ophidiicola_targetD_Haynes_2023` published 42.2% where every
    record that actually carries targetD detects - 81 detect, 111 chance pairs,
    no genuine failure at all (docs/journal/2026-10-25-chance-pairs-invent-denominators.md).

    **Why not an E-value test, of either kind.** `pair_evalue` cannot do this
    job. It scales with amplicon length, search space AND match quality, so a
    real site that is merely divergent necessarily scores weak - which is the
    record a drift registry most needs to count. Within
    `RANAVIRUS_..._MCP_Pallister_2007` the detects sit at 2.4e-16 and the
    GENUINE fails at 5.6e-7..2.2e-5, an eight-order gap that looks exactly like
    Orf's chance pairs at 4.1e-5..8.4e-4. Lowering `max_pair_evalue` discards
    the real ranavirus failures; Benjamini-Hochberg over pairs rejects them too,
    being assay-relative, because they are a small weak minority among strong
    rows just as the chance pairs are. Both were tried and withdrawn the same
    day.

    **What does separate them is the probe.** It binds inside the amplicon, at
    the target locus, so its presence tests "is the locus here?" independently
    of how well the primers matched. The test is therefore conjunctive, and both
    halves are load-bearing:

    - probe site ABSENT, and
    - BOTH primers above `scoring.oligo_weak_max` - the bar at which one oligo
      alone is `blocked`, so neither primer is a working placement.

    `read_calls` carries `probeless_penalties` on exactly the rows that satisfy
    the first half, so the absent probe site is already established by a row
    having that key at all; this function decides the second half. Rows from a
    screen with no penalty columns never get the key, and unknown is not chance.

    Dropping the primer half would break the finding this exists to protect:
    `MONKEYPOX_dsDNA_G2R_WestAfrican_TaqMan_Li_2010` fails 2,688 records that are
    probe-less with `fwd_penalty` 0 and `rev_penalty` 0 - conserved primers that
    genuinely amplify clade I, and a clade-II probe that genuinely does not bind
    it. Real amplification, real failure, must count. Dropping the probe half
    leaves penalties alone, which marks ~4,900 rows in the two LYSSAVIRUS
    nucleoprotein entries that are plausibly real coverage failures.

    `probe_bars` maps each probe-bearing assay to ITS OWN `oligo_weak_max`, and
    both halves of that matter. Membership is passed rather than inferred from
    the rows, because an assay whose probe never binds anywhere would otherwise
    look probe-less and have its every failure explained away. And the bar is
    passed per assay rather than read from `cfg["scoring"]`, because
    `scoring.by_chemistry` can override it: the screener resolves per chemistry
    through `score.config_for`, and this test reading the base block instead
    would mean one thing by "blocked" in the screen and another here. The table
    ships empty today, so nothing diverges yet - but populating it is the whole
    point of ROADMAP Phase 2, and the first `mgb` or `hydrolysis_probe` override
    would have desynchronised a live test silently. Caller resolves; see
    `report.build`.

    Conventional and SYBR assays have no probe and so no locus-presence test;
    they are out of scope here, and the general case was attempted and rejected
    (`docs/journal/2026-10-25-locus-identity-design.md`).

    Returns {assay_id: rows relabelled}. Mutates `rows`.
    """
    if not (cfg.get("drift") or {}).get("chance_pair_test"):
        return {}
    moved: dict[str, int] = {}
    for r in rows:
        if r.get("call") != "fail":
            continue
        bar = probe_bars.get(r["assay_id"])
        if bar is None:
            continue
        pen = r.get("probeless_penalties")
        if pen is None:
            # Either the probe site was present, or the screen carried no penalty
            # columns. Unknown is not chance.
            continue
        fwd, rev = pen
        if fwd > bar and rev > bar:
            r["call"] = "no_amplicon"
            r["exclusion"] = CHANCE_PAIR
            moved[r["assay_id"]] = moved.get(r["assay_id"], 0) + 1
    return moved


def read_dates(retrieved_dir: Path) -> dict[str, str]:
    """{accession without version: deposit date (YYYY-MM-DD)}, newest revision winning."""
    best: dict[str, tuple[str, str]] = {}
    for meta in sorted(retrieved_dir.rglob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                acc = strip_version(row["accession"])
                created = (row.get("created") or "")[:10]
                if not created[:4].isdigit():
                    continue
                updated = row.get("updated") or ""
                if acc not in best or updated > best[acc][0]:
                    best[acc] = (updated, created)
    return {acc: created for acc, (_, created) in best.items()}


def read_years(retrieved_dir: Path) -> dict[str, int]:
    """{accession without version: deposit year}, newest revision winning."""
    return {acc: int(d[:4]) for acc, d in read_dates(retrieved_dir).items()}


def key_calls_by_accession(calls: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Normalise record ids so they join against the metadata, newest version only.

    Newest means the highest `.N` version, not the last row: the pipeline
    concatenates archives group by group, so an older version can come last.
    """
    seen: dict[tuple[str, str], tuple[int, dict[str, Any]]] = {}
    for row in calls:
        acc = strip_version(row["record_id"])
        v = version_of(row["record_id"])
        key = (row["assay_id"], acc)
        if key not in seen or v >= seen[key][0]:
            seen[key] = (v, {**row, "record_id": acc})
    return [row for _, row in seen.values()]
