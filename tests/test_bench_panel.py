"""scripts/bench_panel.py reads a site on either strand and names the mispair facing each primer base."""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "bench_panel", Path(__file__).resolve().parents[1] / "scripts" / "bench_panel.py"
)
bench_panel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bench_panel)


def test_site_window_reverse_strand_reads_as_the_oligo():
    seq = "AAAA" + "GGTCA" + "TTTT"
    assert bench_panel.site_window(seq, "4-9+") == "GGTCA"
    assert bench_panel.site_window(seq, "4-9-") == "TGACC"


def test_mispair_names_template_base_not_record_base():
    # FAP59's 3' end against HPV16 (NC_001526 4901-4922): record C under primer W,
    # 5 nt from the 3' end. The primer faces template G, so the pairs are A:G and T:G.
    oligo = "TAACWGTIGGICAYCCWTATT"
    window = "TTGCAGTTGGACATCCCTATT"
    assert bench_panel.window_mispairs(oligo, window, 5) == [(5, "A:G/T:G")]
    # the two 5' mismatches only appear once the window reaches them
    assert bench_panel.window_mispairs(oligo, window, 20) == [(20, "A:A"), (19, "A:C"), (5, "A:G/T:G")]


def test_read_panel_skips_comments_and_unversions(tmp_path):
    p = tmp_path / "panel.tsv"
    p.write_text("# note\naccession\tlabel\tbench\nNC_001526.4\tHPV16\tband\n")
    assert bench_panel.read_panel(p) == {
        "NC_001526": {"accession": "NC_001526.4", "label": "HPV16", "bench": "band"}
    }
