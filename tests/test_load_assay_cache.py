"""`validate.load_assay` caches parsed files; these pin what the cache must not break."""

from pathlib import Path

from assaywatch.validate import load_assay

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "registry" / "ABPV_capsid_Rossi_2024.yaml"


def test_each_caller_gets_its_own_copy(tmp_path):
    path = tmp_path / SOURCE.name
    path.write_text(SOURCE.read_text())
    first = load_assay(path)
    original_taxid = first.target.taxid
    first.target.taxid = original_taxid + 1
    assert load_assay(path).target.taxid == original_taxid


def test_an_edited_file_is_read_again(tmp_path):
    path = tmp_path / SOURCE.name
    text = SOURCE.read_text()
    path.write_text(text)
    before = load_assay(path).target.taxid
    path.write_text(text.replace(f"taxid: {before}", f"taxid: {before + 7}", 1))
    assert load_assay(path).target.taxid == before + 7
