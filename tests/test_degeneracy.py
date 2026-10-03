"""Degeneracy accounting: counts molecules, not pairing options, and never scores."""

import pytest
import yaml
from test_score import ASSAYS, CFG, RECORDS, ROOT, screen_record

from assaywatch.degeneracy import assay_degeneracy, tier_for
from assaywatch.iupac import base_state, degeneracy
from assaywatch.schema import Assay


def load(assay_id):
    return Assay.model_validate(yaml.safe_load((ROOT / "registry" / f"{assay_id}.yaml").read_text()))


def test_inosine_is_one_molecule_not_a_degenerate_position():
    """An inosine primer is a single compound; writing it as N inflates it 4-fold per position."""
    as_written = "GCYTCISMIAIIGTTTGIACATT"
    as_stored = as_written.replace("I", "N")
    assert degeneracy(as_written) == 8
    assert degeneracy(as_stored) == 8192


def test_assay_degeneracy_reads_seq_as_written():
    d = assay_degeneracy(load("FILOVIRUS_ssRNA_L_gene_2"))
    assert d.inosine_positions > 0
    rev = next(o for o in d.oligos if o.role == "reverse")
    assert rev.fold == 8  # not 8192
    assert rev.inosine == 5


def test_inosine_pairing_rules():
    """I:C is a real pair, I:A and I:T are wobble pairs, I:G is weak."""
    assert base_state("I", "C") == "match"
    assert base_state("I", "A") == "match"
    assert base_state("I", "T") == "match"
    assert base_state("I", "G") == "unknown"  # poor pair: no evidence either way


def test_total_fold_multiplies_every_oligo_and_components_stay_visible():
    """The headline number is the whole pool; the split says what kind of trouble it is."""
    d = assay_degeneracy(load("DNA_BARCODING_and_internal_con_Carnivore_16S"))
    fwd = next(o for o in d.oligos if o.role == "forward")
    rev = next(o for o in d.oligos if o.role == "reverse")
    probe = next(o for o in d.oligos if o.role == "probe")
    assert d.pair_fold == fwd.fold * rev.fold
    assert d.probe_fold == probe.fold
    assert d.total_fold == d.pair_fold * d.probe_fold == 16


def test_probe_degeneracy_moves_the_tier():
    """A probe-side pool counts: it is reagent that does not participate."""
    d = assay_degeneracy(load("DNA_BARCODING_and_internal_con_Carnivore_16S"))
    assert d.probe_fold == 2
    assert tier_for(d.pair_fold) == "negligible"
    assert tier_for(d.total_fold) == "moderate"
    assert d.tier() == "moderate"


def test_an_assay_without_a_probe_has_probe_fold_one():
    d = assay_degeneracy(load("CHYTRID_Bd_ITS1_5_8S_conventional_Annis_2004"))
    assert d.probe_fold == 1 and d.total_fold == d.pair_fold


def test_expected_cq_delay_is_the_log_of_the_total():
    """log of a product = sum of logs: each oligo's dilution adds its own cycles."""
    d = assay_degeneracy(load("DNA_BARCODING_and_internal_con_Carnivore_16S"))
    assert d.expected_cq_delay == pytest.approx(4.0)  # 16-fold = 4 doublings


def test_tiers_are_ordered_and_configurable():
    assert tier_for(1) == "negligible"
    assert tier_for(64) == "moderate"
    assert tier_for(1024) == "high"
    assert tier_for(10**6) == "severe"
    cfg = {"degeneracy": {"tiers": [[1, "negligible"]]}}
    assert tier_for(2, cfg) == "severe"


def test_degeneracy_never_changes_a_call():
    """The accounting is reported, not scored: swapping the tiers moves no call."""
    row_id = "Pan_mycoplasma_16S_All_Van_1992__fwd_mid_d7"
    assay = ASSAYS["Pan_mycoplasma_16S_All_Van_1992"]
    before = screen_record(assay, row_id, RECORDS[row_id], CFG)
    cfg = dict(CFG)
    cfg["degeneracy"] = {"tiers": [[1, "negligible"]]}
    after = screen_record(assay, row_id, RECORDS[row_id], cfg)
    assert before.call == after.call and before.penalty == after.penalty


def test_note_is_empty_for_clean_assays_and_explicit_for_severe_ones():
    clean = assay_degeneracy(load("CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"))
    assert clean.note(CFG) == ""
    severe = assay_degeneracy(load("ADENOVIRUS_dsDNA_Pan_Polymerase_round1"))
    note = severe.note(CFG)
    assert "tautology" in note
    assert "primers" in note and "probe" in note  # the split is always shown
