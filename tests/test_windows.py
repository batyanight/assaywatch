"""Window archives: a re-screen reproduces the whole-record calls, and the guard refuses what it cannot answer.

A window cut from a longer record is scored on the source record's length and composition,
because the chance E-value grows with record length: on its own short length a window can
let through a pair the whole record called chance_only. The screener reads both from a
`<stem>.windows.tsv.gz` sidecar, and a `manifest.json` beside the archive records the
settings and primers it was cut for.
"""

import csv
import gzip
import json
import random

import pytest
import yaml
from test_score import ASSAYS, CFG, RECORDS, ROOT

from assaywatch.match import find_sites
from assaywatch.score import screen_record
from assaywatch.screen import main as screen_main
from assaywatch.screen import sidecar_path, window_context
from assaywatch.validate import load_assay
from assaywatch.windows import (
    _looser,
    build_group,
    check_against,
    discovery_settings,
    merge_spans,
    pair_signature,
    screened_assays,
)

BD = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
# The threshold is the test's own, not the shipped 0.01, so that a plausible
# record length still flips the call. Scoring now gives `pair_evalue` the window
# it actually accepts — for Bd, 121 bp +/- `declared_tolerance`, so 62 bp rather
# than the global 2951 — which divides every E-value here by about 48. At
# SOURCE_LEN a six-and-six Bd pair scores E = 2.3e-3: chance against this
# threshold, and nowhere near it against the whole record's own 420 bp.
STRICT = {**CFG, "scoring": {**CFG["scoring"], "max_pair_evalue": 0.001}}
# Long enough that a six-and-six pair is indistinguishable from chance.
SOURCE_LEN = 4_000_000_000


def six_and_six() -> str:
    """The Bd amplicon with six mismatches at the 5' end of each primer site."""
    a = ASSAYS[BD]
    rec = list(RECORDS[f"{BD}__perfect"])
    f = find_sites(a.oligos.forward.matching_seq, "".join(rec), 0)[0]
    r = find_sites(a.oligos.reverse.matching_seq, "".join(rec), 0)[0]
    swap = {"A": "C", "C": "G", "G": "T", "T": "A"}
    for i in range(6):
        rec[f.start + i] = swap[rec[f.start + i]]
        rec[r.end - 1 - i] = swap[rec[r.end - 1 - i]]
    return "".join(rec)


# --- the length the chance filter sees ------------------------------------


def test_record_len_decides_the_chance_filter():
    seq = six_and_six()
    assert screen_record(ASSAYS[BD], "w", seq, STRICT).call != "no_amplicon"
    src = screen_record(ASSAYS[BD], "w", seq, STRICT, record_len=SOURCE_LEN).as_row()
    assert src["call"] == "no_amplicon" and src["exclusion"] == "chance_only"


def test_record_len_none_is_the_old_behaviour():
    seq = six_and_six()
    assert screen_record(ASSAYS[BD], "w", seq, STRICT).as_row() == (
        screen_record(ASSAYS[BD], "w", seq, STRICT, record_len=None).as_row()
    )


# --- building ---------------------------------------------------------------


def test_merge_spans_widens_clips_and_merges():
    assert merge_spans([(1000, 1100)], 300, 5000) == [(700, 1400)]
    assert merge_spans([(100, 200)], 300, 5000) == [(0, 500)]
    assert merge_spans([(4900, 4990)], 300, 5000) == [(4600, 5000)]
    assert merge_spans([(1000, 1100), (1500, 1600)], 300, 5000) == [(700, 1900)]
    assert merge_spans([(1000, 1100), (2000, 2100)], 300, 5000) == [(700, 1400), (1700, 2400)]


def _tree(tmp_path, cfg):
    """A group with one archive of one long record holding the Bd amplicon twice, screened whole."""
    rng = random.Random(7)
    noise = lambda n: "".join(rng.choice("ACGT") for _ in range(n))  # noqa: E731
    amp = RECORDS[f"{BD}__perfect"]
    whole = noise(20_000) + amp + noise(40_000) + amp + noise(20_000)
    src = tmp_path / "retrieved" / "1" / "qtest"
    scr = tmp_path / "screened" / "1" / "qtest"
    src.mkdir(parents=True)
    scr.mkdir(parents=True)
    with gzip.open(src / "2026-01-01.fasta.gz", "wt") as fh:
        fh.write(f">ACC1.1 test\n{whole}\n")
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg))
    screen_main(
        [
            str(ROOT / "registry" / f"{BD}.yaml"),
            str(src / "2026-01-01.fasta.gz"),
            "--config",
            str(cfg_path),
            "-o",
            str(scr / "2026-01-01.tsv"),
        ]
    )
    return whole, cfg_path


def _build(tmp_path, cfg, buffer=300):
    whole, cfg_path = _tree(tmp_path, cfg)
    assay = load_assay(ROOT / "registry" / f"{BD}.yaml")
    m = build_group(
        1, "qtest", [assay], cfg, tmp_path / "screened", tmp_path / "retrieved", tmp_path / "windows", buffer
    )
    return whole, cfg_path, m, tmp_path / "windows" / "1" / "qtest"


def _screen_windows(dst, cfg_path, workers=1, registry_file=None):
    out = dst.parent / f"calls_{workers}.tsv"
    screen_main(
        [
            str(registry_file or ROOT / "registry" / f"{BD}.yaml"),
            str(dst / "2026-01-01.fasta.gz"),
            "--config",
            str(cfg_path),
            "--workers",
            str(workers),
            "-o",
            str(out),
        ]
    )
    return list(csv.DictReader(out.open(), delimiter="\t"))


def test_windows_reproduce_the_whole_record_row_exactly(tmp_path):
    whole, cfg_path, m, dst = _build(tmp_path, CFG)
    original = list(csv.DictReader((tmp_path / "screened/1/qtest/2026-01-01.tsv").open(), delimiter="\t"))
    assert m["archives"]["2026-01-01"]["windows"] == 2
    assert m["archives"]["2026-01-01"]["window_bp"] < len(whole) / 50
    for workers in (1, 2):
        rows = _screen_windows(dst, cfg_path, workers)
        assert len(rows) == 1 and rows[0]["record_id"] == "ACC1.1"
        # pair_evalue matches only because the source length was used; coordinates are in
        # the joined record, so they are the one thing allowed to differ.
        moved = {"amplicon_start", "amplicon_end", "fwd_site", "rev_site", "probe_site"}
        assert {k: v for k, v in rows[0].items() if k not in moved} == (
            {k: v for k, v in original[0].items() if k not in moved}
        )


def test_sidecar_maps_each_window_back_to_the_source(tmp_path):
    whole, _, _, dst = _build(tmp_path, CFG)
    with gzip.open(sidecar_path(dst / "2026-01-01.fasta.gz"), "rt") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    joined = next(iter(gzip.open(dst / "2026-01-01.fasta.gz", "rt").read().split("\n")[1:2]))
    for r in rows:
        off, n, s, e = int(r["offset"]), int(r["length"]), int(r["src_start"]), int(r["src_end"])
        assert joined[off : off + n] == whole[s - 1 : e]  # 1-based inclusive, as efetch seq_start/seq_stop
        assert int(r["src_len"]) == len(whole)
    assert window_context(dst / "2026-01-01.fasta.gz") == {
        "ACC1.1": (len(whole), tuple(float(x) for x in rows[0]["src_comp"].split(",")))
    }


def test_screened_assays_refuses_a_group_screened_inconsistently(tmp_path):
    for name, aid in (("a.tsv", "X"), ("b.tsv", "Y")):
        (tmp_path / name).write_text(f"assay_id\trecord_id\n{aid}\tr\n")
    with pytest.raises(SystemExit, match="different assays"):
        screened_assays(tmp_path)


# --- the guard --------------------------------------------------------------


def test_looser_treats_none_as_no_limit():
    assert _looser(7, 6, "le") and not _looser(5, 6, "le") and not _looser(6, 6, "le")
    assert _looser(None, 0.01, "le") and not _looser(0.5, None, "le")
    assert _looser(40, 50, "ge") and not _looser(60, 50, "ge")


def _with(cfg, **scoring):
    return {**cfg, "scoring": {**cfg["scoring"], **scoring}}


@pytest.mark.parametrize(
    "change, why",
    [
        (lambda c: _with(c, max_mismatches_searched=7), "max_mismatches_searched"),
        (lambda c: _with(c, max_pair_evalue=None), "max_pair_evalue"),
        (lambda c: {**c, "amplicon": {**c["amplicon"], "max_bp": c["amplicon"]["max_bp"] + 1}}, "max_bp"),
        (lambda c: {**c, "amplicon": {**c["amplicon"], "min_bp": c["amplicon"]["min_bp"] - 1}}, "min_bp"),
    ],
    ids=["mismatch budget up", "chance filter off", "max_bp up", "min_bp down"],
)
def test_guard_refuses_looser_discovery(tmp_path, change, why):
    _, _, m, dst = _build(tmp_path, CFG)
    assert any(why in p for p in check_against(m, change(CFG), [ASSAYS[BD]]))
    loose = tmp_path / "loose.yaml"
    loose.write_text(yaml.safe_dump(change(CFG)))
    with pytest.raises(SystemExit, match="refusing"):
        _screen_windows(dst, loose)


def test_guard_allows_tighter_discovery_and_any_context_change(tmp_path):
    _, _, m, dst = _build(tmp_path, CFG)
    tighter = _with(CFG, max_mismatches_searched=5, primer_3prime_penalty=9.0, detect_max=0.5)
    assert check_against(m, tighter, [ASSAYS[BD]]) == []
    path = tmp_path / "tight.yaml"
    path.write_text(yaml.safe_dump(tighter))
    assert len(_screen_windows(dst, path)) == 1


def test_guard_refuses_an_assay_the_archive_was_not_cut_for(tmp_path):
    _, _, m, _ = _build(tmp_path, CFG)
    other = next(a for aid, a in ASSAYS.items() if aid != BD)
    assert any("not in the archive" in p for p in check_against(m, CFG, [other]))


def test_guard_refuses_edited_primers(tmp_path):
    _, cfg_path, m, dst = _build(tmp_path, CFG)
    doc = yaml.safe_load((ROOT / "registry" / f"{BD}.yaml").read_text())
    doc["oligos"]["forward"]["seq"] = "A" + doc["oligos"]["forward"]["seq"][1:]
    edited = tmp_path / f"{BD}.yaml"
    edited.write_text(yaml.safe_dump(doc))
    assert pair_signature(load_assay(edited)) != m["assays"][BD]
    with pytest.raises(SystemExit, match="primer pools differ"):
        _screen_windows(dst, cfg_path, registry_file=edited)


def test_window_archive_without_manifest_is_refused(tmp_path):
    _, cfg_path, _, dst = _build(tmp_path, CFG)
    (dst / "manifest.json").unlink()
    with pytest.raises(SystemExit, match="manifest.json is missing"):
        _screen_windows(dst, cfg_path)


def test_manifest_records_settings_assays_and_verifiability(tmp_path):
    _, _, m, dst = _build(tmp_path, CFG)
    on_disk = json.loads((dst / "manifest.json").read_text())
    assert on_disk == json.loads(json.dumps(m))
    assert m["buffer_bp"] == 300 and m["verifiable_by_efetch"] is True
    assert m["discovery"] == json.loads(json.dumps(discovery_settings(CFG)))
    assert m["assays"] == {BD: pair_signature(ASSAYS[BD])}


def test_sidecar_path_sits_beside_the_archive(tmp_path):
    assert sidecar_path(tmp_path / "2026-10-07.fasta.gz").name == "2026-10-07.windows.tsv.gz"
    assert sidecar_path(tmp_path / "x.fasta").name == "x.windows.tsv.gz"


def test_a_context_change_that_moves_the_best_pair_to_another_copy_is_reproduced(tmp_path):
    """Two copies of the amplicon, each one mismatch off in a different place. The default
    weights prefer copy A; heavier 5' weights prefer copy B. The windows must hold B too."""
    a = ASSAYS[BD]
    amp = RECORDS[f"{BD}__perfect"]
    f = find_sites(a.oligos.forward.matching_seq, amp, 0)[0]
    swap = {"A": "C", "C": "G", "G": "T", "T": "A"}

    def mismatch(at: int) -> str:
        s = list(amp)
        s[f.start + at] = swap[s[f.start + at]]
        return "".join(s)

    flen = len(a.oligos.forward.matching_seq)
    copy_a = mismatch(0)  # forward 5'-most base: the 5' penalty
    copy_b = mismatch(flen - 1 - 7)  # 8th base from the 3' end: the mid-window penalty
    rng = random.Random(11)
    noise = lambda n: "".join(rng.choice("ACGT") for _ in range(n))  # noqa: E731
    whole = noise(15_000) + copy_a + noise(30_000) + copy_b + noise(15_000)
    b_start = 15_000 + len(copy_a) + 30_000

    src = tmp_path / "retrieved" / "1" / "qtest"
    scr = tmp_path / "screened" / "1" / "qtest"
    src.mkdir(parents=True)
    scr.mkdir(parents=True)
    with gzip.open(src / "2026-01-01.fasta.gz", "wt") as fh:
        fh.write(f">ACC2.1\n{whole}\n")
    base = tmp_path / "base.yaml"
    base.write_text(yaml.safe_dump(CFG))
    registry_file = str(ROOT / "registry" / f"{BD}.yaml")
    screen_main(
        [
            registry_file,
            str(src / "2026-01-01.fasta.gz"),
            "--config",
            str(base),
            "-o",
            str(scr / "2026-01-01.tsv"),
        ]
    )
    m = build_group(
        1,
        "qtest",
        [load_assay(ROOT / "registry" / f"{BD}.yaml")],
        CFG,
        tmp_path / "screened",
        tmp_path / "retrieved",
        tmp_path / "windows",
        300,
    )
    assert m["archives"]["2026-01-01"]["windows"] == 2

    heavy = _with(CFG, primer_5prime_penalty=2.0)
    assert check_against(m, heavy, [ASSAYS[BD]]) == []
    hp = tmp_path / "heavy.yaml"
    hp.write_text(yaml.safe_dump(heavy))
    whole_out, win_out = tmp_path / "whole.tsv", tmp_path / "win.tsv"
    screen_main([registry_file, str(src / "2026-01-01.fasta.gz"), "--config", str(hp), "-o", str(whole_out)])
    dst = tmp_path / "windows" / "1" / "qtest"
    screen_main([registry_file, str(dst / "2026-01-01.fasta.gz"), "--config", str(hp), "-o", str(win_out)])
    w_row = next(csv.DictReader(whole_out.open(), delimiter="\t"))
    v_row = next(csv.DictReader(win_out.open(), delimiter="\t"))
    assert int(w_row["amplicon_start"]) >= b_start, (
        "the heavier 5' weight should move the best pair to copy B"
    )
    moved = {"amplicon_start", "amplicon_end", "fwd_site", "rev_site", "probe_site"}
    assert {k: v for k, v in v_row.items() if k not in moved} == {
        k: v for k, v in w_row.items() if k not in moved
    }
    # and the window row's coordinates map back to copy B through the sidecar
    with gzip.open(sidecar_path(dst / "2026-01-01.fasta.gz"), "rt") as fh:
        side = list(csv.DictReader(fh, delimiter="\t"))
    start = int(v_row["amplicon_start"])
    win = next(r for r in side if int(r["offset"]) <= start < int(r["offset"]) + int(r["length"]))
    assert int(win["src_start"]) - 1 + (start - int(win["offset"])) == int(w_row["amplicon_start"])


def test_parallel_build_is_byte_identical(tmp_path):
    _tree(tmp_path, CFG)
    assay = load_assay(ROOT / "registry" / f"{BD}.yaml")
    outs = []
    for workers in (1, 2):
        out = tmp_path / f"w{workers}"
        build_group(
            1, "qtest", [assay], CFG, tmp_path / "screened", tmp_path / "retrieved", out, 300, workers
        )
        d = out / "1" / "qtest"
        outs.append([gzip.open(d / n).read() for n in ("2026-01-01.fasta.gz", "2026-01-01.windows.tsv.gz")])
    assert outs[0] == outs[1]


def test_tied_copies_resolve_the_same_way_whether_or_not_the_pair_cap_bites():
    """The reported copy among tied candidates must not depend on unrelated pairs elsewhere."""
    from assaywatch.iupac import reverse_complement

    amp = RECORDS[f"{BD}__perfect"]
    rng = random.Random(5)
    noise = lambda n: "".join(rng.choice("ACGT") for _ in range(n))  # noqa: E731
    # minus-strand copy first, plus-strand copy second
    rec = noise(2_000) + reverse_complement(amp) + noise(5_000) + amp + noise(2_000)
    capped = screen_record(ASSAYS[BD], "r", rec, _with(CFG, max_pairs_per_record=1)).as_row()
    uncapped = screen_record(ASSAYS[BD], "r", rec, CFG).as_row()
    assert capped["call"] == uncapped["call"] == "detect"
    assert capped["amplicon_start"] == uncapped["amplicon_start"]


RV = "RANAVIRUS_dsDNA_Major_capsid_protein_MCP_Pallister_2007"


def test_a_no_amplicon_row_from_windows_says_windowed_not_a_guessed_reason(tmp_path):
    """A group of two assays; the record holds only the Bd amplicon. The ranavirus row is
    no_amplicon in both screens, but only the whole record can say why."""
    import shutil

    reg = tmp_path / "reg"
    reg.mkdir()
    for aid in (BD, RV):
        shutil.copy(ROOT / "registry" / f"{aid}.yaml", reg / f"{aid}.yaml")
    whole, cfg_path = _tree(tmp_path, CFG)
    # re-screen the whole record with both assays, so the group's screen names both
    scr = tmp_path / "screened" / "1" / "qtest" / "2026-01-01.tsv"
    src = tmp_path / "retrieved" / "1" / "qtest" / "2026-01-01.fasta.gz"
    screen_main([str(reg), str(src), "--config", str(cfg_path), "-o", str(scr)])
    assays = [load_assay(reg / f"{a}.yaml") for a in (BD, RV)]
    build_group(1, "qtest", assays, CFG, tmp_path / "screened", tmp_path / "retrieved", tmp_path / "w", 300)
    out = tmp_path / "win.tsv"
    win = tmp_path / "w" / "1" / "qtest" / "2026-01-01.fasta.gz"
    screen_main([str(reg), str(win), "--config", str(cfg_path), "-o", str(out)])
    rows = {r["assay_id"]: r for r in csv.DictReader(out.open(), delimiter="\t")}
    whole_rows = {r["assay_id"]: r for r in csv.DictReader(scr.open(), delimiter="\t")}
    assert rows[BD]["call"] == whole_rows[BD]["call"] == "detect"
    assert rows[RV]["call"] == whole_rows[RV]["call"] == "no_amplicon"
    assert whole_rows[RV]["exclusion"] not in ("", "windowed")
    assert rows[RV]["exclusion"] == "windowed" and "whole record" in rows[RV]["reason"]


def test_drift_refuses_count_diverged_on_windowed_rows():
    from assaywatch.drift import assess

    rows = [
        {"assay_id": "A", "record_id": "r1", "call": "detect", "exclusion": ""},
        {"assay_id": "A", "record_id": "r2", "call": "no_amplicon", "exclusion": "windowed"},
    ]
    years = {"r1": 2024, "r2": 2024}
    # `patent=set()`: the shipped setting excludes patent records since 2026-10-23,
    # and `assess` refuses to run that setting without the set. None of these rows is
    # a patent record, so an empty set is the truth here.
    assess(rows, years, CFG, patent=set())  # the shipped setting: fine
    on = {**CFG, "drift": {**CFG.get("drift", {}), "count_diverged_as_fail": True}}
    with pytest.raises(ValueError, match="window archive"):
        assess(rows, years, on, patent=set())
