#!/usr/bin/env python3
"""Replay a scoring strategy over a calls table instead of paying for a rescreen.

    python scripts/rescore.py --calls results/2026-10-26/calls.tsv.gz \
        --strategy strategies/s0-shipped.yaml --out .tmp/rescore/s0/

Part 0.2 of `docs/2026-10-24-scoring-strategy-test-plan.md`. Scoring is a function
of the mismatch configuration, and the screen already finds that configuration; as
of 2026-10-26 it also writes the whole of it down (`*_mispairs`, commit `1fa4672`).
So a candidate scoring rule no longer costs a ~30-minute rescreen to price - it is
arithmetic over a table, and this script is that arithmetic plus the fixed Part 0.4
report around it.

WHY A REPLAY CAN BE EXACT. `score_primer`'s penalty needs the position penalty
bands, the mispair identity and the distance from the 3' end. The distance is
recorded per mismatch, so a primer needs no sequence and not even its own length.
Only `score_probe` needs a length, for its thirds, and no probe pool in the
registry holds oligos of differing lengths (checked by a test), so that length is
unambiguous. Nothing here re-finds a site or re-reads a record.

THE BOUNDARY, three parts, printed on every run because Part 0.1 requires it:

1. A replay changes how a found site is SCORED. It cannot change which sites are
   FOUND. `max_mismatches_searched`, `max_site_evalue`, `max_pairs_per_record`,
   gapped alignment and the amplicon window decide what the screen looks at, and a
   strategy naming one is refused rather than warned about.
2. Evaluability is frozen. `max_pair_evalue` and `max_ambiguous_per_oligo` decide
   whether a record is judged at all, which is the DENOMINATOR axis - a different
   question, held fixed across every scoring comparison (Part 0.4), and the axis
   that produced three failed candidates on 2026-10-25. `max_ambiguous_per_oligo`
   is refused although the ambiguity counts are in the table and it could be
   replayed, because moving it moves the denominator.
3. CANDIDATE SELECTION IS FROZEN, and this is the one approximation that is not a
   refusal. The screen evaluates every facing primer pair in a record and writes
   only the winner; a scoring change can reorder those candidates, and a replay
   cannot see a candidate that is not in the table. So a replay is exact for the
   amplicon the screen chose and silent about the one it might have chosen
   instead. A strategy that passes its gate here is therefore PRICED, not proven:
   shipping one needs a confirming rescreen, which is cheap once exactly one
   candidate deserves it.

   MEASURED 2026-10-26, and it is small and one-directional. M1 was really
   rescreened over every tier-2 assay whose calls it moves - 514,096 rows across 17
   assays - and compared against the replay of the same strategy: **2 call
   disagreements and 11 penalty disagreements, 0 on the reason**. That is 0.0004% of
   rows. Every one of the 13 runs the same way: the REAL screen finds a better
   candidate than the replay could see, so the replay is PESSIMISTIC and a candidate
   priced here is never flattered by this approximation. Both call disagreements fell
   on one assay whose verdict sits at 97.9% of 755 records against a 90% threshold,
   so neither could move it. Write-up in
   docs/2026-10-26-m1-confirming-rescreen.md.

Determinism: the same table and strategy give the same output byte for byte. The
S0 strategy is the control - it is the shipped config with nothing overridden, and
`--expect-identical` asserts the replay reproduces the input table's own calls. A
no-op replay that merely looks clean is how the first chance-pair test nearly
shipped (it read keys that did not exist and took its `except` branch on every
row), so the control is an assertion and not a glance.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from assaywatch.schema import Chemistry
from assaywatch.score import (
    OligoScore,
    config_for,
    decide,
    mispair_multiplier,
    oligo_pools,
    too_ambiguous,
)
from assaywatch.settings import validated
from assaywatch.validate import iter_files, load_assay

REPO = Path(__file__).resolve().parents[1]

# Scoring keys a replay may change, because every input they read is in the row.
REPLAYABLE_KEYS = frozenset(
    {
        "primer_3prime_window",
        "primer_3prime_penalty",
        "primer_mid_window",
        "primer_mid_penalty",
        "primer_5prime_penalty",
        "mispair_penalty",
        "probe_center_penalty",
        "probe_outer_penalty",
        "detect_max",
        "reduced_max",
        "terminal_mismatch_fails",
        "engine",
        "oligo_ok_max",
        "oligo_weak_max",
        "by_chemistry",
    }
)

# Everything else in the `scoring` block, each with the reason a replay refuses it.
# Stated per key rather than as a list, so a future key is refused by default and
# whoever adds it has to say which side of the boundary it is on.
UNREPLAYABLE_KEYS = {
    "max_mismatches_searched": "search: decides which sites are found at all",
    "max_site_evalue": "search: decides which single sites survive",
    "max_pairs_per_record": "search: decides which candidate pairs are considered",
    "max_pair_evalue": "denominator: decides whether a record is evaluable",
    "max_ambiguous_per_oligo": (
        "denominator: decides whether a record is judged or `indeterminate`. The counts "
        "are in the table, so this COULD be replayed; it is refused because moving it "
        "moves the denominator, which Part 0.4 holds fixed"
    ),
    "locus_identity_min": "search: needs the amplicon interior, which the table does not carry",
    "locus_identity_trim_bp": "search: part of the locus-identity test",
    "locus_identity_min_interior_bp": "search: part of the locus-identity test",
}

# Rows a replay must pass through untouched, and why. Each is an outcome of the
# SEARCH layer wearing a call's clothing.
PASSTHROUGH_CALLS = {
    "no_amplicon": "no primer pair was found; nothing was scored",
    "indeterminate": "too_ambiguous fired, which is a denominator decision held fixed",
}
PROBE_ABSENT_REASON = "no probe site inside amplicon"


@dataclass(frozen=True)
class Strategy:
    """One pre-registered candidate: its name, its overlay and its own kill criterion."""

    name: str
    scoring: dict[str, Any]
    meta: dict[str, Any]
    path: Path
    #: A positional weight curve replacing `score_primer`'s three-band step function,
    #: for the shape Part 0.2 means by "a small Python callable `footprints -> call`
    #: for shapes the config cannot express". `config.yaml` has three bands and two
    #: widths, so a decay cannot be written as an overlay at all.
    #:
    #: REPLAY-ONLY, AND THAT IS A HARDER LIMIT THAN IT SOUNDS. `assaywatch/score.py`
    #: knows only the step function, so a curve priced here cannot be screened with.
    #: Shipping one needs a change to the package AND a rescreen; pricing one does
    #: not, which is the whole point of doing it this way round.
    weight: dict[str, Any] | None = None
    #: Chemistries for which a `reduced` call must NOT count toward the detected
    #: share - S3's probe switch, and the influenza mechanism from wave 3: a
    #: hydrolysis probe that binds badly reports late or not at all, where a primer
    #: that binds badly still makes product.
    #:
    #: `drift.YearStats.detected` is `detect + reduced` in code, with no config key
    #: and no per-chemistry variant, so this cannot be an overlay. It is priced by
    #: REWRITING those rows to `fail` in the replayed table, which is arithmetically
    #: identical for drift: `detected` is `detect + reduced` and `evaluable` is
    #: `detect + reduced + fail`, so moving a row from `reduced` to `fail` takes it
    #: out of the numerator and leaves the denominator alone, which is exactly what
    #: "not detected" means. Shipping it would mean a per-chemistry `detected` in
    #: `drift.py`, not this rewrite.
    reduced_not_detected_for: tuple[str, ...] = ()


def positional_weight(spec: dict[str, Any] | None, d: int, cfg: dict[str, Any]) -> float:
    """The penalty a mismatch `d` bases from the 3' end carries.

    With no spec this IS `score_primer`'s step function, read from the same config
    keys, so an S0 replay goes down one code path and not two.

    `kind: exponential` is `w0 * 2 ** (-(d - 1) / half_distance)`: the weight at the
    3'-terminal base is `w0` and it halves every `half_distance` bases toward the 5'
    end. Motivated by Usutu, where d = 3 is where the step function and the
    literature part company - the step treats d = 1 and d = 5 as identical at 3.0 and
    then drops to 1.0 at d = 6, which is a cliff no measurement supports.
    """
    s = cfg["scoring"]
    if not spec:
        w3, wmid = s["primer_3prime_window"], s["primer_mid_window"]
        if d <= w3:
            return s["primer_3prime_penalty"]
        if d <= w3 + wmid:
            return s["primer_mid_penalty"]
        return s["primer_5prime_penalty"]
    kind = spec.get("kind")
    if kind != "exponential":
        raise SystemExit(f"unknown positional weight kind {kind!r}; only `exponential` is implemented")
    w0 = float(spec["w0"])
    half = float(spec["half_distance"])
    floor = float(spec.get("floor", 0.0))
    return max(floor, w0 * 2.0 ** (-(d - 1) / half))


def load_strategy(path: Path) -> Strategy:
    doc = yaml.safe_load(path.read_text()) or {}
    if "name" not in doc:
        raise SystemExit(f"{path}: a strategy needs a `name`")
    scoring = doc.get("scoring") or {}
    if not isinstance(scoring, dict):
        raise SystemExit(f"{path}: `scoring` must be a mapping of overrides")
    weight = doc.get("positional_weight")
    undetected = tuple(doc.get("reduced_not_detected_for") or ())
    known = {str(c) for c in Chemistry}
    unknown = [c for c in undetected if c not in known]
    if unknown:
        raise SystemExit(f"{path}: unknown chemistry in reduced_not_detected_for: {', '.join(unknown)}")
    meta = {
        k: v
        for k, v in doc.items()
        if k not in {"name", "scoring", "positional_weight", "reduced_not_detected_for"}
    }
    missing = [k for k in ("question", "predicts", "kill") if k not in meta]
    if missing:
        # Part 0.5: pre-register what it changes, what it predicts and what kills it.
        # Enforced rather than asked for, because a candidate without a kill criterion
        # cannot fail, and four of the last five candidates died on theirs.
        raise SystemExit(f"{path}: pre-registration incomplete, missing {', '.join(missing)}")
    return Strategy(doc["name"], scoring, meta, path, weight, undetected)


def refuse_unreplayable(scoring: dict[str, Any]) -> list[str]:
    """Problems with a strategy's overlay, as full sentences. Empty means replayable."""
    problems = []
    for key in scoring:
        if key in UNREPLAYABLE_KEYS:
            problems.append(f"`{key}` cannot be replayed - {UNREPLAYABLE_KEYS[key]}; it needs a rescreen")
        elif key not in REPLAYABLE_KEYS:
            problems.append(
                f"`{key}` is not a known scoring key, or not one a replay has been told how to handle"
            )
    for chem, override in (scoring.get("by_chemistry") or {}).items():
        for key in override or {}:
            if key in UNREPLAYABLE_KEYS:
                problems.append(
                    f"`by_chemistry.{chem}.{key}` cannot be replayed - {UNREPLAYABLE_KEYS[key]}; it needs a rescreen"
                )
            elif key not in REPLAYABLE_KEYS:
                problems.append(f"`by_chemistry.{chem}.{key}` is not a known scoring key")
    return problems


def merged_config(strategy: Strategy, base: Path | None) -> dict[str, Any]:
    """The shipped config with the strategy's `scoring` overlay applied and validated.

    Validated through `assaywatch.settings`, the same gate the pipeline uses, so a
    misspelled key or an out-of-order threshold pair is an error here rather than a
    silently ignored override that makes a run look recalibrated when it was not.
    """
    raw = yaml.safe_load((base or REPO / "config.yaml").read_text())
    scoring = {**raw["scoring"]}
    for key, value in strategy.scoring.items():
        if key == "by_chemistry":
            merged = {**(scoring.get("by_chemistry") or {})}
            for chem, override in (value or {}).items():
                merged[chem] = {**(merged.get(chem) or {}), **(override or {})}
            scoring["by_chemistry"] = merged
        else:
            scoring[key] = value
    raw["scoring"] = scoring
    cfg = validated(raw)
    resolved = {}
    for chem in Chemistry:
        from assaywatch.score import scoring_for

        block = scoring_for(chem, cfg)
        if block is not cfg.get("scoring"):
            resolved[str(chem)] = {**cfg, "scoring": block}
    if resolved:
        from assaywatch.score import RESOLVED

        cfg[RESOLVED] = resolved
    return cfg


def registry_facts(registry: Path) -> dict[str, dict[str, Any]]:
    """Per assay: its chemistry, and its probe's length where it has one.

    The probe length is the one thing a replay cannot read off a row, and it is
    unambiguous: no probe pool in the registry holds oligos of differing lengths
    (`tests/test_rescore.py` pins that, because an assay that broke it would make
    every probe penalty in this script quietly wrong for that assay).
    """
    facts = {}
    for path in iter_files(registry):
        assay = load_assay(path)
        _, _, probes = oligo_pools(assay)
        lengths = {len(p) for p in probes}
        if len(lengths) > 1:
            raise SystemExit(
                f"{assay.id}: probe pool holds lengths {sorted(lengths)}, so a replay cannot know "
                "which probe was scored. The row would need the winning probe's name."
            )
        facts[assay.id] = {
            "chemistry": assay.chemistry,
            "probe_len": lengths.pop() if lengths else None,
        }
    return facts


def parse_mispairs(cell: str) -> tuple[tuple[str, str, int], ...]:
    """`"G:T@1,A:C@19"` -> ((oligo base, template base, distance from the 3' end), ...)."""
    if not cell:
        return ()
    out = []
    for item in cell.split(","):
        pair, _, distance = item.partition("@")
        oligo_base, _, template = pair.partition(":")
        out.append((oligo_base, template, int(distance)))
    return tuple(out)


def primer_score(
    mispairs: tuple[tuple[str, str, int], ...],
    n_ambiguous: int,
    cfg: dict[str, Any],
    weight: dict[str, Any] | None = None,
) -> OligoScore:
    """`score_primer` with the row's recorded footprint standing in for the record.

    Deliberately a transcription of `score_primer`'s loop rather than a call into
    it: that function takes a `Site` and a sequence, and inventing a fake window to
    reach it would mean reconstructing bases the table does not hold. The two must
    agree exactly, which is what the S0 control measures over every row.
    """
    s = cfg["scoring"]
    w3 = s["primer_3prime_window"]
    table = s.get("mispair_penalty") or {}
    penalty, terminal = 0.0, False
    for oligo_base, template, d in mispairs:
        base = positional_weight(weight, d, cfg)
        # Identity still acts only within the 3' window even under a smooth curve.
        # The window and the curve answer different questions - where the mispair
        # effect is measurable, and how the position penalty decays - and merging
        # them would change two things in one candidate.
        mult = mispair_multiplier(oligo_base, template, table) if d <= w3 else 1.0
        penalty += base * mult
        if d == 1 and mult != 0:
            terminal = True
    distances = tuple(d for _, _, d in mispairs)
    return OligoScore(
        penalty,
        terminal,
        (),  # 5'-based positions are not in the table and nothing downstream reads them
        distances,
        tuple(range(n_ambiguous)),  # only the COUNT is recorded; too_ambiguous reads the length
        tuple(f"{o}:{t}@{d}" for o, t, d in mispairs),
    )


def probe_score(
    mispairs: tuple[tuple[str, str, int], ...], n_ambiguous: int, probe_len: int, cfg: dict[str, Any]
) -> OligoScore:
    """`score_probe` with the row's footprint. The thirds need the length; nothing else does."""
    s = cfg["scoring"]
    lo, hi = probe_len / 3, 2 * probe_len / 3
    penalty = 0.0
    for _, _, d in mispairs:
        pos = probe_len - d
        penalty += s["probe_center_penalty"] if lo <= pos < hi else s["probe_outer_penalty"]
    return OligoScore(
        penalty,
        False,
        (),
        tuple(d for _, _, d in mispairs),
        tuple(range(n_ambiguous)),
        tuple(f"{o}:{t}@{d}" for o, t, d in mispairs),
    )


def _int(cell: str) -> int:
    return int(cell) if cell else 0


def replay_row(
    row: dict[str, str],
    facts: dict[str, dict[str, Any]],
    cfg: dict[str, Any],
    weight: dict[str, Any] | None = None,
    undetected: tuple[str, ...] = (),
) -> tuple[str, str, str]:
    """One row's (call, reason, penalty cell) under the strategy.

    Returns the row's own values unchanged for anything the search layer decided.
    """
    call = row["call"]
    if call in PASSTHROUGH_CALLS:
        return call, row["reason"], row["penalty"]

    assay = facts.get(row["assay_id"])
    if assay is None:
        return call, row["reason"], row["penalty"]
    chem_cfg = config_for(assay["chemistry"], cfg)

    # The primers amplify and the probe has no site: a fail on its own terms,
    # decided by where the sites are and not by any threshold, so `screen_one`
    # forces the call past whatever `decide` said. It does NOT force the penalty:
    # `Call.penalty` is still `decide`'s scalar, which under `engine: serial` is the
    # worst single oligo and under `budget` the sum. Returning the row's own penalty
    # here was wrong, and it is the kind of wrong that hides: the call is already
    # pinned to `fail`, so no call moved and only the scalar disagreed. Measured
    # against a real `engine: serial` rescreen of one archive on 2026-10-26, which
    # is how it was found - 19 of 266 scored rows, 0 call disagreements.
    probe_absent = row.get("reason", "").startswith(PROBE_ABSENT_REASON)

    fs = primer_score(
        parse_mispairs(row.get("fwd_mispairs", "")), _int(row.get("fwd_ambiguous", "")), chem_cfg, weight
    )
    rs = primer_score(
        parse_mispairs(row.get("rev_mispairs", "")), _int(row.get("rev_ambiguous", "")), chem_cfg, weight
    )
    ps = None
    if row.get("probe_penalty", "") != "":
        ps = probe_score(
            parse_mispairs(row.get("probe_mispairs", "")),
            _int(row.get("probe_ambiguous", "")),
            assay["probe_len"] or 0,
            chem_cfg,
        )

    new_call, reason, total = decide(fs, rs, ps, chem_cfg)
    if too_ambiguous([o for o in (fs, rs, ps) if o is not None], chem_cfg):
        # Unreachable while max_ambiguous_per_oligo is refused, and kept so that the
        # ordering in `screen_one` is reproduced rather than assumed if it is allowed.
        return "indeterminate", row["reason"], row["penalty"]
    if probe_absent:
        # Same order as `screen_one`: the forced call and the kept reason, but the
        # recomputed scalar.
        return "fail", row["reason"], f"{total:g}"
    if new_call == "reduced" and str(assay["chemistry"]) in undetected:
        # S3's probe switch, priced as a rewrite; see Strategy.reduced_not_detected_for.
        return "fail", f"{reason}; reduced is not detected for this chemistry".strip("; "), f"{total:g}"
    return new_call, reason, f"{total:g}"


def replay(
    calls: Path,
    out_dir: Path,
    facts: dict[str, dict[str, Any]],
    cfg: dict[str, Any],
    weight: dict[str, Any] | None = None,
    undetected: tuple[str, ...] = (),
) -> dict[str, Any]:
    """Write the restored calls table and return what moved."""
    out_dir.mkdir(parents=True, exist_ok=True)
    moved: Counter[str] = Counter()
    totals: Counter[str] = Counter()
    disagreements = 0
    with gzip.open(calls, "rt") as fh, gzip.open(out_dir / "calls.tsv.gz", "wt", newline="") as out:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames is None:
            raise SystemExit(f"{calls}: no header")
        if "fwd_mispairs" not in reader.fieldnames:
            raise SystemExit(
                f"{calls} carries no `fwd_mispairs` column, so it predates the footprint columns "
                "(commit 1fa4672) and cannot be replayed. Rescreen, or name a newer table."
            )
        writer = csv.DictWriter(out, fieldnames=reader.fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in reader:
            was = row["call"]
            call, reason, penalty = replay_row(row, facts, cfg, weight, undetected)
            totals[call] += 1
            if call != was:
                moved[f"{was} -> {call}"] += 1
                disagreements += 1
            row["call"], row["reason"], row["penalty"] = call, reason, penalty
            writer.writerow(row)
    return {"moved": dict(moved), "calls": dict(totals), "n_moved": disagreements}


def panel_rows(manifest: Path) -> list[dict[str, str]]:
    with manifest.open() as fh:
        body = (line for line in fh if not line.startswith("#"))
        return [r for r in csv.DictReader(body, delimiter="\t") if r.get("panel")]


def panel_fasta(panel: Path, cache: Path) -> Path | None:
    """The panel's sequences, fetched once through EDirect and cached.

    Cached because a harness that re-fetches 70 accessions per candidate is neither
    deterministic nor polite. Keep efetch's stderr out of the log: on a failed query
    it prints the request URL, API key included.
    """
    cache.mkdir(parents=True, exist_ok=True)
    target = cache / f"{panel.stem}.fasta"
    if target.exists() and target.stat().st_size:
        return target
    accessions = []
    with panel.open() as fh:
        body = (line for line in fh if not line.startswith("#"))
        for row in csv.DictReader(body, delimiter="\t"):
            acc = (row.get("accession") or "").strip()
            if acc:
                accessions.append(acc)
    if not accessions:
        return None
    proc = subprocess.run(
        ["efetch", "-db", "nuccore", "-format", "fasta", "-id", ",".join(accessions)],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        return None
    target.write_text(proc.stdout)
    return target


def run_panels(manifest: Path, cfg_path: Path, cache: Path) -> list[dict[str, Any]]:
    """`bench_panel.py` per panel, which is what Part 0.4's first row asks for."""
    out = []
    for row in panel_rows(manifest):
        panel = REPO / row["panel"]
        fasta = panel_fasta(panel, cache)
        if fasta is None:
            out.append(
                {"panel": panel.stem, "paper": row["paper"], "role": row["role"], "error": "no sequences"}
            )
            continue
        proc = subprocess.run(
            [
                sys.executable,
                str(REPO / "scripts" / "bench_panel.py"),
                "--panel",
                str(panel),
                "--assay",
                str(REPO / row["assay"]),
                "--fasta",
                str(fasta),
                "--config",
                str(cfg_path),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        out.append(
            {
                "panel": panel.stem,
                "paper": row["paper"],
                "role": row["role"],
                "stdout": proc.stdout,
                "returncode": proc.returncode,
                "stderr": proc.stderr[-2000:] if proc.returncode else "",
            }
        )
    return out


def run_script(name: str, args: list[str]) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(REPO / "scripts" / name), *args], capture_output=True, text=True, check=False
    )
    return {"stdout": proc.stdout, "returncode": proc.returncode, "stderr": proc.stderr[-2000:]}


BOUNDARY = """\
REPLAY BOUNDARY (docs/2026-10-24-scoring-strategy-test-plan.md Part 0.1)
  A replay changes how a found site is SCORED, never which sites are FOUND.
  Refused here, because they need a rescreen: max_mismatches_searched,
  max_site_evalue, max_pairs_per_record, gapped alignment, the amplicon window.
  Held fixed as the DENOMINATOR axis: max_pair_evalue, max_ambiguous_per_oligo,
  count_diverged_as_fail, patent exclusion, scope, drift.anchor_fdr.
  NOT a refusal, and the one real approximation: candidate selection is frozen.
  The table holds only the amplicon the screen chose per record, so a strategy
  that would make a different candidate win cannot be seen here. Measured on
  2026-10-26 over 514,096 really-rescreened rows: 2 call and 11 penalty
  disagreements, 0.0004%, and ALL of them pessimistic - the real screen finds a
  better candidate than the replay can. A strategy priced by replay is PRICED,
  NOT PROVEN; shipping one needs a confirming rescreen.\
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument(
        "--calls", type=Path, required=True, help="a calls.tsv.gz carrying the *_mispairs columns"
    )
    ap.add_argument("--strategy", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True, help="a SCRATCH directory; never results/")
    ap.add_argument("--registry", type=Path, default=REPO / "registry")
    ap.add_argument("--config", type=Path, default=None, help="base config the overlay applies to")
    ap.add_argument("--cases", type=Path, default=REPO / "docs" / "validation-cases.tsv")
    ap.add_argument("--panels", type=Path, default=REPO / "docs" / "bench-panels" / "panels.tsv")
    ap.add_argument("--retrieved", type=Path, default=REPO / "data" / "retrieved")
    ap.add_argument("--baseline", type=Path, default=REPO / "results" / "baseline-2026-10-22")
    ap.add_argument(
        "--fasta-cache",
        type=Path,
        default=REPO / ".tmp" / "bench-panels",
        help="where panel sequences are cached",
    )
    ap.add_argument(
        "--expect-identical",
        action="store_true",
        help="assert the replay reproduces the input table's own calls (the S0 control)",
    )
    ap.add_argument(
        "--skip-downstream", action="store_true", help="replay only; no tier-2, holdout or panels"
    )
    args = ap.parse_args(argv)

    resolved_out = args.out.resolve()
    if (REPO / "results").resolve() in resolved_out.parents or resolved_out == (REPO / "results").resolve():
        raise SystemExit(f"{args.out} is under results/; a replay writes to scratch only")

    strategy = load_strategy(args.strategy)
    problems = refuse_unreplayable(strategy.scoring)
    if problems:
        print(f"REFUSED: {strategy.path}", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 2

    cfg = merged_config(strategy, args.config)
    facts = registry_facts(args.registry)
    args.out.mkdir(parents=True, exist_ok=True)

    # The exact scoring block the replay used, written beside the table so a number
    # can never be quoted without the settings that produced it.
    effective = {k: cfg["scoring"][k] for k in sorted(REPLAYABLE_KEYS) if k in cfg["scoring"]}
    cfg_path = args.out / "config-used.yaml"
    full = yaml.safe_load((args.config or REPO / "config.yaml").read_text())
    full["scoring"] = {k: v for k, v in cfg["scoring"].items()}
    cfg_path.write_text(yaml.safe_dump(full, sort_keys=False))

    print(BOUNDARY)
    print()
    print(f"strategy: {strategy.name}  ({strategy.path})")
    for key in ("question", "predicts", "kill"):
        print(f"  {key}: {' '.join(str(strategy.meta[key]).split())}")
    print(f"  overrides: {json.dumps(strategy.scoring, sort_keys=True)}")
    print(f"calls in:  {args.calls}")
    print(f"out:       {args.out}")
    print()

    result = replay(args.calls, args.out, facts, cfg, strategy.weight, strategy.reduced_not_detected_for)
    print(f"replayed {sum(result['calls'].values())} rows; {result['n_moved']} calls moved")
    for move, n in sorted(result["moved"].items(), key=lambda x: -x[1]):
        print(f"  {move}: {n}")
    if not result["moved"]:
        print("  (none)")

    if args.expect_identical and result["n_moved"]:
        print(
            f"\nFAILED --expect-identical: {result['n_moved']} calls moved under a strategy that "
            "should change nothing. The replay does not reproduce the screen.",
            file=sys.stderr,
        )
        return 1
    if args.expect_identical:
        print("\n--expect-identical: the replay reproduces every call in the input table.")

    summary: dict[str, Any] = {
        "strategy": strategy.name,
        "strategy_path": str(strategy.path),
        "pre_registration": strategy.meta,
        "overrides": strategy.scoring,
        "effective_scoring": effective,
        "calls_in": str(args.calls),
        "replay": result,
        "boundary": BOUNDARY,
    }

    if not args.skip_downstream:
        new_calls = args.out / "calls.tsv.gz"
        print("\n--- tier-2 (development set, Jeffreys intervals) ---")
        tier2 = run_script(
            "retrospective.py",
            [
                "--cases",
                str(args.cases),
                "--calls",
                str(new_calls),
                "--registry",
                str(args.registry),
                "--retrieved",
                str(args.retrieved),
                "--config",
                str(cfg_path),
            ],
        )
        print(tier2["stdout"] or tier2["stderr"])
        print("--- leave-one-out optimism ---")
        hold = run_script(
            "holdout.py",
            [
                "--calls",
                str(new_calls),
                "--registry",
                str(args.registry),
                "--retrieved",
                str(args.retrieved),
                "--cases",
                str(args.cases),
                "--config",
                str(cfg_path),
            ],
        )
        print(hold["stdout"] or hold["stderr"])
        print("--- bench panels (per panel; leave-one-panel-out is per PAPER) ---")
        panels = run_panels(args.panels, cfg_path, args.fasta_cache)
        for p in panels:
            head = f"[{p['role']}] {p['panel']} (paper {p['paper']})"
            print(head)
            print(p.get("stdout") or f"  ERROR: {p.get('error') or p.get('stderr')}")
        summary["tier2"] = tier2
        summary["holdout"] = hold
        summary["panels"] = panels

    (args.out / "summary.json").write_text(json.dumps(summary, indent=2, default=str) + "\n")
    print(f"\nwrote {args.out / 'calls.tsv.gz'}, {cfg_path.name} and summary.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
