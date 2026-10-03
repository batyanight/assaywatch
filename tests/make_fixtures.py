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

import csv
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

    gap = 20
    spacer_left = _flank(gap)
    spacer_right = _flank(gap)
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
        "probe": len(lead) + len(fwd) + gap,
        "reverse": len(lead) + len(fwd) + gap + len(probe_site) + gap,
    }
    return seq, offsets


def main() -> None:
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

    with (FIXTURES / "records.fasta").open("w") as fh:
        for rid, seq in records:
            fh.write(f">{rid}\n")
            for i in range(0, len(seq), 70):
                fh.write(seq[i : i + 70] + "\n")

    with (FIXTURES / "manifest.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    print(f"{len(records)} records for {len(FIXTURE_ASSAYS)} assays -> {FIXTURES}")
    print(
        f"thresholds in use: detect<={cfg['scoring']['detect_max']} reduced<={cfg['scoring']['reduced_max']}"
    )


if __name__ == "__main__":
    main()
