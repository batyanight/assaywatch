"""Build the synthetic fixture set: records with mismatches at known positions.

    python tests/make_fixtures.py            # writes tests/fixtures/*.fasta + manifest.tsv

This is validation tier 1 from the build plan. The point is that the expected
call for every record is known before the scorer runs, because the record was
constructed by taking a perfect amplicon and editing specific bases.

Construction, per assay in FIXTURE_ASSAYS:

    [random 5' flank] [forward primer] [spacer, with probe site] [revcomp(reverse primer)] [random 3' flank]

Each record then gets zero or more planted edits, each specified as
(oligo, where) so the test can assert both the positions the matcher reports
and the final call. An oligo name ending in `_amb` plants an ambiguity code
instead of a mismatching base, which is how the "degeneracy and undetermined
record bases are not penalised" rule is tested.

Mutations are made with a base that the oligo's IUPAC code genuinely does not
cover, so a degenerate position cannot silently absorb the edit; that is what
`_mismatching_base` checks.

The manifest (tests/fixtures/manifest.tsv) lists record_id, assay_id, the
planted edits and the expected call, and is what test_score.py reads.
"""

from __future__ import annotations

import argparse
import csv
import io
import random
from pathlib import Path

import yaml

from assaywatch.iupac import IUPAC, base_matches, reverse_complement
from assaywatch.schema import Assay
from assaywatch.score import load_config

HERE = Path(__file__).resolve().parent
REGISTRY = HERE.parent / "registry"
FIXTURES = HERE / "fixtures"

# Five assays spanning the chemistries and oligo lengths in the registry.
FIXTURE_ASSAYS = [
    "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004",  # MGB probe, short probe (15 nt)
    "CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004",  # conventional, no probe
    "B_salamandrivorans_Internal_transcribes_spa_Blooi_2013",  # MGB probe, 32 nt probe
    "RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007",  # MGB probe
    "Pan_mycoplasma_16S_All_Van_1992",  # degenerate primers, no probe
]

# (suffix, [(which_oligo, where), ...], expected_call)
# `where` is a distance from the oligo's 3' end (1 = the terminal base) for
# primers, or one of "first" / "center" / "last" for a named position.
PLANS: list[tuple[str, list[tuple[str, int]], str]] = [
    ("perfect", [], "detect"),
    ("fwd_3term", [("forward", 1)], "fail"),  # terminal mismatch rule
    ("rev_3term", [("reverse", 1)], "fail"),
    ("fwd_3prime_d3", [("forward", 3)], "reduced"),  # 3.0, exactly reduced_max
    ("fwd_mid_d7", [("forward", 7)], "detect"),  # 1.0 <= detect_max 1.0
    ("fwd_5prime_d15", [("forward", 15)], "detect"),  # 0.5
    ("fwd_mid_x2", [("forward", 7), ("forward", 9)], "reduced"),  # 2.0
    ("fwd_mid_rev_mid", [("forward", 7), ("reverse", 7)], "reduced"),  # 2.0
    ("fwd_5prime_x3", [("forward", 14), ("forward", 16), ("forward", 18)], "reduced"),  # 1.5
    ("fwd_mid_x4", [("forward", 7), ("forward", 8), ("forward", 9), ("forward", 10)], "fail"),  # 4.0
    ("probe_center", [("probe", "center")], "reduced"),  # 2.0 when a probe exists
    ("probe_outer", [("probe", "first")], "detect"),  # 1.0
    # Both ends of one oligo edited at once. The seeded matcher this replaced
    # took one seed from each end of the oligo, so these records broke every
    # seed and the site vanished: they were miscounted as no_amplicon instead
    # of being scored. They are the regression test for that bug.
    ("fwd_both_ends", [("forward", 1), ("forward", "first")], "fail"),  # 3.0 + 0.5, and terminal
    ("probe_both_ends", [("probe", "first"), ("probe", "last")], "reduced"),  # 1.0 + 1.0
    # Undetermined record bases. These are not mismatches and must cost
    # nothing, even at the 3'-terminal base where a real mismatch is fatal.
    # Past `max_ambiguous_per_oligo` the record is indeterminate, not failed.
    ("rec_ambiguous_3term", [("forward_amb", 1)], "detect"),
    ("rec_ambiguous_x2", [("forward_amb", 1), ("forward_amb", 5)], "detect"),
    ("rec_ambiguous_x3", [("forward_amb", 1), ("forward_amb", 5), ("forward_amb", 9)], "indeterminate"),
]

RNG = random.Random(20261003)  # fixed seed: fixtures must be reproducible


def _ambiguous_base(code: str) -> str:
    """An IUPAC code that overlaps `code` without being covered by it.

    Planting this makes the record's true base undetermined at that position:
    it may or may not match the oligo. The scorer must charge nothing for it.
    """
    for rb, bases in IUPAC.items():
        allowed = set(IUPAC[code.upper()])
        if set(bases) & allowed and not set(bases) <= allowed:
            return rb
    return "N"


def _mismatching_base(code: str) -> str:
    """A concrete base the IUPAC `code` does not cover."""
    for b in "ACGT":
        if not base_matches(code, b):
            return b
    raise ValueError(f"{code} covers every base; cannot plant a mismatch here")


def _concrete(code: str) -> str:
    """A concrete base the code does cover, for writing a 'perfect' record."""
    return RNG.choice(IUPAC[code.upper()])


def _flank(n: int) -> str:
    return "".join(RNG.choice("ACGT") for _ in range(n))


DEFAULT_GAP = 20  # used when the assay declares no amplicon size
# The probe only has to sit between the primers, not at a comfortable distance:
# `score.screen_one` accepts a probe site anywhere inside the span, so one base
# of clearance is a real geometry. It has to be this small because real qPCR
# amplicons are: Pallister 2007's ranavirus MGB assay makes a 57 bp product from
# a 20 nt forward, an 18 nt probe and a 17 nt reverse, which leaves exactly one
# base either side. At a floor of 5 the builder fell back to DEFAULT_GAP and
# produced a 95 bp record for a 57 bp assay, which `declared_tolerance` then
# correctly refused - every fixture for that assay failed the moment its
# measured size was stored.
MIN_GAP = 1


def _spacers(fwd_len: int, probe_len: int, rev_len: int, declared: int | None) -> tuple[int, int]:
    """Spacer lengths either side of the probe, so the product is `declared` bp.

    Returns the fixed default when the assay declares no size, or when the
    declared size cannot hold the oligos with a gap either side — in which case
    the fixture is deliberately the wrong length and the test will say so,
    rather than the builder quietly producing a product nobody asked for.
    """
    if not declared:
        return DEFAULT_GAP, DEFAULT_GAP
    total = declared - fwd_len - probe_len - rev_len
    if total < 2 * MIN_GAP:
        return DEFAULT_GAP, DEFAULT_GAP
    left = total // 2
    return left, total - left


def build_record(assay: Assay, edits: list[tuple[str, object]]) -> tuple[str, dict[str, int]]:
    """Return (sequence, {oligo: offset}) with the given edits planted.

    Offsets are the plus-strand start of each oligo's binding site, which the
    test uses to check the matcher found the right place.
    """
    fwd = assay.oligos.forward.seq
    rev = assay.oligos.reverse.seq
    probe = assay.oligos.probe.seq if assay.oligos.probe else None

    fwd_site = [_concrete(b) for b in fwd]
    # The reverse primer anneals to the plus strand's complement, so the plus
    # strand carries the reverse complement of the reverse primer.
    rev_site = [_concrete(b) for b in reverse_complement(rev)]
    probe_site = [_concrete(b) for b in probe] if probe else []

    def index_in(oligo: str, where: object) -> int:
        """Translate a plan's `where` into a 0-based index from the oligo's 5' end."""
        named = {"first": 0, "center": len(oligo) // 2, "last": len(oligo) - 1}
        if isinstance(where, str) and where in named:
            return named[where]
        return len(oligo) - int(where)  # distance 1 -> the 3'-terminal base

    for which, where in edits:
        edit = _ambiguous_base if which.endswith("_amb") else _mismatching_base
        which = which.removesuffix("_amb")
        if which == "forward":
            i = index_in(fwd, where)
            fwd_site[i] = edit(fwd[i])
        elif which == "reverse":
            j = index_in(rev, where)  # index in the primer, 5'->3'
            # position j of the primer corresponds to plus-strand index len-1-j
            k = len(rev) - 1 - j
            rev_site[k] = edit(reverse_complement(rev)[k])
        elif which == "probe":
            if not probe:
                raise ValueError("probe edit requested for an assay with no probe")
            i = index_in(probe, where)
            probe_site[i] = edit(probe[i])
        else:
            raise ValueError(which)

    # Spacers are sized so the built product matches the assay's own declared
    # amplicon_bp, because `amplicon.declared_tolerance` constrains a call to
    # that size. Built at a fixed 20 nt instead, the Annis 2004 fixtures came
    # out at 79 bp against a declared 300 and every one of them scored
    # no_amplicon the moment the tolerance was switched on. An assay with no
    # declared size, or one whose declared size leaves no room for the oligos,
    # keeps the fixed spacing.
    left_gap, right_gap = _spacers(len(fwd), len(probe_site), len(rev), assay.amplicon_bp)
    spacer_left = _flank(left_gap)
    spacer_right = _flank(right_gap)
    lead = _flank(60)

    parts = [
        lead,
        "".join(fwd_site),
        spacer_left,
        "".join(probe_site),
        spacer_right,
        "".join(rev_site),
        _flank(60),
    ]
    seq = "".join(parts)
    offsets = {
        "forward": len(lead),
        "probe": len(lead) + len(fwd) + left_gap,
        "reverse": len(lead) + len(fwd) + left_gap + len(probe_site) + right_gap,
    }
    return seq, offsets


def main(argv: list[str] | None = None) -> int:
    """Regenerate the golden fixtures, or with `--check` verify they are current.

    WHY `--check` EXISTS. This script reads LIVE inputs -- `registry/*.yaml` and
    `config.yaml` via `load_config` -- and overwrites `tests/fixtures/`. The RNG
    is seeded, so regeneration is deterministic, but the inputs are not frozen.
    That makes the failure asymmetric and the dangerous direction silent:

      * change a THRESHOLD and the hand-derived `expected_call` values in `PLANS`
        go stale, `tests/test_score.py` fails loudly, and someone notices;
      * change an OLIGO in one of the five fixture assays and regeneration
        rebuilds all 84 records around the new sequence, every expectation still
        matches, and a scoring regression introduced the same day is absorbed
        into the golden file.

    The committed fixtures were generated 2026-10-15; `registry/` and
    `config.yaml` have both changed since. Nothing compared them until now. The
    pattern is `scripts/papers_index.py --check`, which is a pre-commit hook for
    exactly this reason after that index went stale twice.
    """
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--check",
        action="store_true",
        help="do not write; fail if the committed fixtures differ from a fresh generation",
    )
    args = ap.parse_args(argv)
    FIXTURES.mkdir(exist_ok=True)
    cfg = load_config()
    rows = []
    records: list[tuple[str, str]] = []

    for assay_id in FIXTURE_ASSAYS:
        assay = Assay.model_validate(yaml.safe_load((REGISTRY / f"{assay_id}.yaml").read_text()))
        has_probe = assay.oligos.probe is not None
        for suffix, edits, expected in PLANS:
            if any(w.startswith("probe") for w, _ in edits) and not has_probe:
                continue
            seq, offsets = build_record(assay, edits)
            rid = f"{assay_id}__{suffix}"
            records.append((rid, seq))
            rows.append(
                {
                    "record_id": rid,
                    "assay_id": assay_id,
                    "edits": ";".join(f"{w}:{v}" for w, v in edits) or "none",
                    "expected_call": expected,
                    "fwd_offset": offsets["forward"],
                    "rev_offset": offsets["reverse"],
                    "length": len(seq),
                }
            )

    # A record with no amplicon at all: random sequence of the same length.
    for assay_id in FIXTURE_ASSAYS:
        rid = f"{assay_id}__unrelated"
        records.append((rid, _flank(400)))
        rows.append(
            {
                "record_id": rid,
                "assay_id": assay_id,
                "edits": "none",
                "expected_call": "no_amplicon",
                "fwd_offset": "",
                "rev_offset": "",
                "length": 400,
            }
        )

    fasta = io.StringIO()
    for rid, seq in records:
        fasta.write(f">{rid}\n")
        for i in range(0, len(seq), 70):
            fasta.write(seq[i : i + 70] + "\n")

    manifest = io.StringIO()
    # csv.DictWriter's default lineterminator is CRLF, and the committed manifest has
    # CRLF, because the original wrote through `open(newline="")`. Keep it: changing it
    # here would rewrite all 85 lines and report every fixture stale for no reason.
    w = csv.DictWriter(manifest, fieldnames=list(rows[0]), delimiter="\t")
    w.writeheader()
    w.writerows(rows)

    # BYTES, not text, on both sides. csv.DictWriter's default lineterminator is
    # CRLF and the manifest keeps it (the pipeline's own TSVs do too, pinned by
    # tests/test_collect.py), but `Path.read_text()` performs universal-newline
    # translation on READ, turning that CRLF back into LF -- so a text comparison
    # reported every fixture stale immediately after regenerating them.
    want = {
        "records.fasta": fasta.getvalue().encode(),
        "manifest.tsv": manifest.getvalue().encode(),
    }
    if args.check:
        stale = [
            name
            for name, blob in want.items()
            if not (FIXTURES / name).exists() or (FIXTURES / name).read_bytes() != blob
        ]
        if stale:
            raise SystemExit(
                f"fixtures are stale: {', '.join(stale)} differ from a fresh generation "
                "off the current registry/ and config.yaml.\n"
                "Regenerate and READ THE DIFF -- an oligo change rebuilds every record "
                "silently, so a scoring regression can hide in it:\n"
                "    python tests/make_fixtures.py && pytest -q"
            )
        print(f"fixtures match a fresh generation ({len(records)} records)")
        return 0
    for name, blob in want.items():
        (FIXTURES / name).write_bytes(blob)

    print(f"{len(records)} records for {len(FIXTURE_ASSAYS)} assays -> {FIXTURES}")
    print(
        f"thresholds in use: detect<={cfg['scoring']['detect_max']} reduced<={cfg['scoring']['reduced_max']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
