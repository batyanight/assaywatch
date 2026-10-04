"""scripts/indel_check.py finds a single-base indel in a primer site on either strand."""

import importlib.util
from pathlib import Path

import pytest
from test_score import ASSAYS, CFG, RECORDS

from assaywatch.iupac import reverse_complement

spec = importlib.util.spec_from_file_location(
    "indel_check", Path(__file__).resolve().parents[1] / "scripts" / "indel_check.py"
)
indel_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(indel_check)

BD = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"


def _record_with_reverse_deletion():
    assay = ASSAYS[BD]
    seq = RECORDS[f"{BD}__perfect"]
    rev_site = reverse_complement(assay.oligos.reverse.matching_seq)  # as it reads on the plus strand
    i = seq.index(rev_site)
    k = i + len(rev_site) // 2
    return assay, seq[:k] + seq[k + 1 :]  # drop one base from the middle of the site


@pytest.mark.parametrize("antisense", [False, True])
def test_missing_reverse_primer_with_one_deletion_is_found(antisense):
    assay, seq = _record_with_reverse_deletion()
    if antisense:
        seq = reverse_complement(seq)
    res = indel_check.check_missing(assay, {}, seq, "no_reverse", CFG, max_cost=2)
    assert res is not None and res["oligo"] == "reverse"
    assert res["gapped_cost"] == 1 and len(res["indels_from_3prime"].split(",")) == 1


@pytest.mark.parametrize("antisense", [False, True])
def test_fail_windows_follow_the_sites_on_either_strand(antisense):
    assay = ASSAYS[BD]
    seq = RECORDS[f"{BD}__perfect"]
    if antisense:
        seq = reverse_complement(seq)
    windows = {
        name: (oligo, w, cost)
        for name, oligo, w, cost in indel_check.oligo_windows(assay, {"record_id": "x"}, seq, CFG)
    }
    # A perfect record: every oligo sits in its window with no mismatch.
    assert windows["forward"][2] == 0 and windows["reverse"][2] == 0
