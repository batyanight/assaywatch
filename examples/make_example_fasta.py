#!/usr/bin/env python3
"""Build the small FASTA that `examples/README.md` screens, from an assay's own oligos.

    python examples/make_example_fasta.py            # writes examples/bd-example.fasta

WHY THIS IS GENERATED AND NOT DOWNLOADED. The example has to run offline, in a
second, and show each verdict the screener can reach. Real GenBank records give
you whichever verdicts those particular records happen to produce, and fetching
them needs the network and an API key. So these records are SYNTHETIC: each one
is the assay's own amplicon with one defect introduced, and its name says which.
They are not GenBank sequences and must never be treated as evidence about the
assay - that is what `registry/` and a real screen are for.

The assay is CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004, the Boyle 2004
Batrachochytrium dendrobatidis ITS TaqMan assay, read from the registry rather
than copied here so the two cannot drift apart.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.iupac import reverse_complement  # noqa: E402
from assaywatch.validate import load_assay  # noqa: E402

ASSAY = ROOT / "registry" / "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004.yaml"
OUT = Path(__file__).resolve().parent / "bd-example.fasta"

# Filler that carries no primer or probe site of its own. Fixed, not random, so
# the file is byte-identical on every run.
FILLER = "TGACTGCATGACCTAGCATGACTGCATGACCTAGCATGACTGCATGACCTAGCATGACTGCATGACCTAGC"
FLANK = "GTTACCAGTTCAGCATTGACCTAGGTTCAAGGCTAACGTTGACCAGTTCAAGGCTAACGTTGACCAGTTCA"


def amplicon(fwd: str, probe: str, rev: str, want_bp: int) -> str:
    """fwd + filler-carrying-the-probe + reverse-complement(rev), exactly want_bp."""
    middle_bp = want_bp - len(fwd) - len(rev)
    if middle_bp < len(probe):
        raise SystemExit(f"amplicon {want_bp} too short for a {len(probe)} nt probe")
    pre = (middle_bp - len(probe)) // 2
    post = middle_bp - len(probe) - pre
    middle = FILLER[:pre] + probe + FILLER[pre : pre + post]
    seq = fwd + middle + reverse_complement(rev)
    assert len(seq) == want_bp, (len(seq), want_bp)
    return seq


def swap(seq: str, i: int) -> str:
    """Change one base at index i (negative indexes from the 3' end)."""
    i = i % len(seq)
    return seq[:i] + {"A": "C", "C": "A", "G": "T", "T": "G"}[seq[i]] + seq[i + 1 :]


def main() -> int:
    a = load_assay(ASSAY)
    fwd, rev = a.oligos.forward.seq, a.oligos.reverse.seq
    probe = a.oligos.probe.seq
    amp = amplicon(fwd, probe, rev, a.amplicon_bp)

    records: list[tuple[str, str, str]] = [
        ("perfect", FLANK + amp + FLANK, "both primers and the probe match exactly"),
        (
            "fwd_3prime_mismatch",
            FLANK + swap(amp, len(fwd) - 1) + FLANK,
            "one mismatch at the forward primer's 3'-terminal base, the position that stops extension",
        ),
        (
            "fwd_5prime_mismatch",
            FLANK + swap(amp, 0) + FLANK,
            "one mismatch at the forward primer's 5' end, far from the 3' end",
        ),
        (
            "probe_mismatch",
            FLANK + swap(amp, len(fwd) + (a.amplicon_bp - len(fwd) - len(rev) - len(probe)) // 2) + FLANK,
            "primers match; one mismatch inside the probe site",
        ),
        (
            "no_reverse_site",
            FLANK + amp[: -len(rev)] + FILLER[: len(rev)] + FLANK,
            "the reverse primer's site is replaced by filler, so there is no pair",
        ),
        (
            "truncated_inside_amplicon",
            FLANK + amp[: len(amp) // 2],
            "the record ends inside the amplicon, so coverage is the limit, not the primers",
        ),
        (
            "both_primers_mid_mismatch",
            FLANK + swap(swap(amp, len(fwd) - 1 - 6), len(amp) - len(rev) + 6) + FLANK,
            "one mismatch 6-10 nt from the 3' end of EACH primer, the mid window",
        ),
        (
            "probe_centre_mismatch",
            FLANK
            + swap(amp, len(fwd) + (a.amplicon_bp - len(fwd) - len(rev) - len(probe)) // 2 + len(probe) // 2)
            + FLANK,
            "primers match; one mismatch in the probe's central third",
        ),
        ("unrelated", FLANK + FILLER + FLANK + FILLER, "no site for either primer"),
    ]

    with OUT.open("w") as fh:
        for name, seq, why in records:
            fh.write(f">{a.id}__{name} SYNTHETIC - {why}\n")
            for i in range(0, len(seq), 70):
                fh.write(seq[i : i + 70] + "\n")

    print(f"wrote {OUT.relative_to(ROOT)}: {len(records)} synthetic records")
    print(f"  assay      {a.id}")
    print(f"  amplicon   {a.amplicon_bp} bp (fwd {len(fwd)}, probe {len(probe)}, rev {len(rev)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
