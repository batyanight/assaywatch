"""The retrospective-candidate identity check.

The one distinction this instrument exists to make is CONFIRMED vs VARIANT: a
citing paper that reprints an assay's primers verbatim tested that assay, and a
paper that prints a one-base-different form did not. Collapsing the two is the
error that let three of the first four hand reads through, so the load-bearing
test below pins that a near miss is never read as a confirmation.

The comparison engine (`verify.check`) has its own tests; these drive the thin
layer on top of it against synthetic paper text, so no network is touched.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_candidate_identity as cci  # noqa: E402

REGISTRY = ROOT / "registry"
ASSAY = "INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003"


def _methods_text(*oligos: str) -> str:
    """A minimal methods paragraph that prints each oligo as a listed primer.

    Enough oligo-like runs that the paper reads as a methods paper rather than one
    with its table lost (MIN_PRINTED_FOR_ABSENT), and set in capitals so
    `printed_oligos` harvests them.
    """
    lines = [f"Primer-{i} 5'-{seq}-3'" for i, seq in enumerate(oligos)]
    return "The assay used the following oligonucleotides. " + " ".join(lines)


def _stored(slot: str) -> str:
    assay = cci.load_assay(REGISTRY / f"{ASSAY}.yaml")
    o = getattr(assay.oligos, slot)
    return (o.seq_as_written or o.seq).replace("I", "N").upper()


# --- classify_oligo: the mapping from verify.check verdicts -------------------


def test_exact_and_revcomp_are_the_only_confirmations():
    assert cci.classify_oligo("exact") == cci.PRESENT_EXACT
    assert cci.classify_oligo("revcomp") == cci.PRESENT_EXACT


def test_near_is_always_a_variant_never_a_confirmation():
    # The load-bearing mapping: any edit distance is a variant.
    for n in (1, 2, 3, 4):
        assert cci.classify_oligo(f"near:{n}") == cci.PRESENT_VARIANT


def test_in_text_is_weak_and_absent_is_not_found():
    assert cci.classify_oligo("in-text") == cci.WEAK
    assert cci.classify_oligo("absent") == cci.NOT_FOUND


# --- assay_identity: the per-assay rule ---------------------------------------


def test_both_primers_verbatim_is_confirmed():
    fwd, rev = _stored("forward"), _stored("reverse")
    text = _methods_text(fwd, rev, _stored("probe"))
    res = cci.check_assay(ASSAY, text, REGISTRY, cap=4)
    assert res["identity"] == "CONFIRMED", res


def test_a_one_base_different_reverse_is_variant_not_confirmed():
    # This is the real Influenza Matrix trap: the stored reverse is a redesign of
    # Spackman's, so a paper reprinting a one-base-off form must read VARIANT.
    fwd, rev = _stored("forward"), _stored("reverse")
    # flip one interior base to a different unambiguous base
    swap = "A" if rev[6] != "A" else "C"
    mutated = rev[:6] + swap + rev[7:]
    assert mutated != rev
    text = _methods_text(fwd, mutated, _stored("probe"))
    res = cci.check_assay(ASSAY, text, REGISTRY, cap=4)
    assert res["identity"] == "VARIANT", res
    assert res["identity"] != "CONFIRMED"


def test_no_oligo_table_is_unconfirmable_not_absent():
    # A paper that cites the assay but prints no oligos cannot decide identity;
    # it must not read as a contradiction.
    text = "We screened samples with the published Spackman matrix assay as cited. " * 40
    res = cci.check_assay(ASSAY, text, REGISTRY, cap=4)
    assert res["identity"] == "UNCONFIRMABLE", res


def test_unreachable_paper_is_unconfirmable():
    # paper_text returns (None, reason) when there is no DOI, no PMC id and no
    # local copy; the caller must treat that as UNCONFIRMABLE, never an error.
    text, src = cci.paper_text(None, None, Path("/nonexistent"))
    assert text is None
    assert "PMC" in src or "copy" in src


# --- assay_identity unit cases, independent of the comparison engine ----------


def test_assay_identity_variant_primer_beats_a_matching_probe():
    results = [
        {"slot": "forward", "category": cci.PRESENT_EXACT},
        {"slot": "reverse", "category": cci.PRESENT_VARIANT},
        {"slot": "probe", "category": cci.PRESENT_EXACT},
    ]
    verdict, _ = cci.assay_identity(results, printed_count=6)
    assert verdict == "VARIANT"


def test_assay_identity_absent_primer_with_a_full_table_points_at_a_different_assay():
    results = [
        {"slot": "forward", "category": cci.PRESENT_EXACT},
        {"slot": "reverse", "category": cci.NOT_FOUND},
    ]
    verdict, reason = cci.assay_identity(results, printed_count=12)
    assert verdict == "UNCONFIRMABLE"
    assert "different assay" in reason
