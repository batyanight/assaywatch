"""`assaywatch.registry`: the one door to the assay YAMLs.

The fixture under tests/fixtures/registry/ holds three real entries: a plain live one,
a live one carrying comments and a flow-style range, and a pending one with no DOI.
"""

from pathlib import Path

import pytest
import yaml

from assaywatch import registry
from assaywatch.schema import Assay

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "registry"
PLAIN = FIXTURE / "ABPV_capsid_Rossi_2024.yaml"
COMMENTED = FIXTURE / "Encephalitozoon_Polar_tube_protein_E_cun_Xiao_2001.yaml"
PENDING = FIXTURE / "ENTEROVIRUS_ssRNA_5_UTR_VP4_VP2_round1.yaml"


@pytest.fixture
def live(tmp_path: Path) -> Path:
    """A registry directory holding only the two live fixture entries."""
    d = tmp_path / "registry"
    d.mkdir()
    for src in (PLAIN, COMMENTED):
        (d / src.name).write_text(src.read_text())
    (d / "README.md").write_text("not an entry\n")
    return d


# --- files ---------------------------------------------------------------------


def test_files_lists_the_yamls_of_a_directory_sorted_and_nothing_else(live: Path):
    assert [p.name for p in registry.files(live)] == sorted(p.name for p in (PLAIN, COMMENTED))


def test_files_of_a_single_file_is_that_file():
    assert list(registry.files(PLAIN)) == [PLAIN]


# --- load_one -------------------------------------------------------------------


def test_load_one_parses_and_validates():
    a = registry.load_one(PLAIN)
    assert isinstance(a, Assay)
    assert a.id == PLAIN.stem
    assert a.oligos.probe is not None


def test_load_one_refuses_an_id_that_does_not_match_the_file_name(tmp_path: Path):
    wrong = tmp_path / "SOMETHING_ELSE.yaml"
    wrong.write_text(PLAIN.read_text())
    with pytest.raises(ValueError, match="does not match"):
        registry.load_one(wrong)


def test_each_caller_gets_its_own_copy(tmp_path: Path):
    path = tmp_path / PLAIN.name
    path.write_text(PLAIN.read_text())
    first = registry.load_one(path)
    original = first.target.taxid
    first.target.taxid = original + 1
    assert registry.load_one(path).target.taxid == original


def test_an_edited_file_is_read_again(tmp_path: Path):
    path = tmp_path / PLAIN.name
    text = PLAIN.read_text()
    path.write_text(text)
    before = registry.load_one(path).target.taxid
    path.write_text(text.replace(f"taxid: {before}", f"taxid: {before + 7}", 1))
    assert registry.load_one(path).target.taxid == before + 7


# --- load -----------------------------------------------------------------------


def test_load_keys_every_live_entry_by_id(live: Path):
    assays = registry.load(live)
    assert set(assays) == {PLAIN.stem, COMMENTED.stem}
    assert all(a.id == k for k, a in assays.items())


def test_load_refuses_a_pending_entry_in_the_live_registry(live: Path):
    (live / PENDING.name).write_text(PENDING.read_text())
    with pytest.raises(registry.RegistryError) as e:
        registry.load(live)
    assert [p.name for p, _ in e.value.problems] == [PENDING.name]
    assert "doi" in e.value.problems[0][1]


def test_load_accepts_pending_entries_when_told_to(tmp_path: Path):
    d = tmp_path / "pending"
    d.mkdir()
    (d / PENDING.name).write_text(PENDING.read_text())
    assert set(registry.load(d, pending=True)) == {PENDING.stem}


def test_load_reports_every_bad_file_not_just_the_first(live: Path):
    (live / "AAA_first.yaml").write_text("id: AAA_first\n")
    (live / "ZZZ_last.yaml").write_text("- not a mapping\n")
    with pytest.raises(registry.RegistryError) as e:
        registry.load(live)
    assert [p.name for p, _ in e.value.problems] == ["AAA_first.yaml", "ZZZ_last.yaml"]
    assert "AAA_first.yaml" in str(e.value) and "ZZZ_last.yaml" in str(e.value)


# --- not_live_because -----------------------------------------------------------


def test_not_live_because_names_the_missing_doi_or_the_unverified_one():
    assert registry.not_live_because(registry.load_one(PLAIN)) is None
    pending = registry.load_one(PENDING)
    assert "doi" in (registry.not_live_because(pending) or "")


# --- write ----------------------------------------------------------------------


def test_write_round_trips_and_leaves_no_part_file(tmp_path: Path):
    a = registry.load_one(COMMENTED)
    out = tmp_path / COMMENTED.name
    registry.write(a, out)
    assert registry.load_one(out) == a
    assert not list(tmp_path.glob(".*.part"))


def test_write_puts_keys_in_schema_order(tmp_path: Path):
    a = registry.load_one(PLAIN)
    out = tmp_path / PLAIN.name
    registry.write(a, out)
    top = list(yaml.safe_load(out.read_text()))
    assert top == list(Assay.model_fields)


# --- edit -----------------------------------------------------------------------


def test_edit_sets_dotted_keys_and_returns_the_reloaded_entry(tmp_path: Path):
    path = tmp_path / PLAIN.name
    path.write_text(PLAIN.read_text())
    a = registry.edit(path, {"amplicon_bp": 150, "citation.n_sequences_at_design": 44})
    assert (a.amplicon_bp, a.citation.n_sequences_at_design) == (150, 44)
    again = registry.load_one(path)
    assert (again.amplicon_bp, again.citation.n_sequences_at_design) == (150, 44)


def test_edit_keeps_comments_key_order_and_flow_style(tmp_path: Path):
    path = tmp_path / COMMENTED.name
    before = COMMENTED.read_text()
    path.write_text(before)
    registry.edit(path, {"citation.n_sequences_at_design": 99})
    after = path.read_text()
    assert "# Measured by scripts/measure_species_sizes.py" in after
    assert "amplicon_bp_range: [275, 373]" in after
    assert [ln.split(":")[0] for ln in before.splitlines() if ln and ln[0].isalpha()] == [
        ln.split(":")[0] for ln in after.splitlines() if ln and ln[0].isalpha()
    ]
    # Meaning: the one change and nothing else. `null` stays spelled out.
    expected = yaml.safe_load(before)
    expected["citation"]["n_sequences_at_design"] = 99
    assert yaml.safe_load(after) == expected
    assert "amplicon_bp: null" in after


def test_edit_validates_before_writing_and_leaves_the_file_untouched_on_failure(tmp_path: Path):
    path = tmp_path / PLAIN.name
    path.write_text(PLAIN.read_text())
    with pytest.raises(ValueError):
        registry.edit(path, {"oligos.forward.seq": "not a sequence!"})
    assert path.read_text() == PLAIN.read_text()
    assert not list(tmp_path.glob(".*.part"))


def test_edit_refuses_a_key_whose_parent_does_not_exist(tmp_path: Path):
    path = tmp_path / PLAIN.name
    path.write_text(PLAIN.read_text())
    with pytest.raises(KeyError):
        registry.edit(path, {"nowhere.at_all": 1})


# --- archive_dir ----------------------------------------------------------------


def test_archive_dir_is_taxid_then_all_or_a_query_hash(tmp_path: Path):
    a = registry.load_one(PLAIN)
    assert registry.archive_dir(a, tmp_path) == tmp_path / str(a.target.taxid) / "all"
    b = a.model_copy(deep=True)
    b.target.query = "capsid[Title]"
    sub = registry.archive_dir(b, tmp_path)
    assert sub.parent == tmp_path / str(a.target.taxid)
    assert sub.name.startswith("q") and len(sub.name) == 11
    assert registry.archive_dir(b, tmp_path) == sub, "the hash is stable"


# --- the old names keep working -------------------------------------------------


def test_the_old_entry_points_are_the_new_functions():
    from assaywatch import atomic, groups, validate

    assert validate.load_assay is registry.load_one
    assert validate.iter_files is registry.files
    assert validate.not_live_because is registry.not_live_because
    assert atomic.write_text is registry.write_text
    assert groups.group_slug is registry.group_slug
