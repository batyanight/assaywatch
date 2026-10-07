"""A window cut from a longer record is scored on the source record's length and composition.

The chance E-value grows with record length, so on its own short length a window can let
through a pair that the whole record called chance_only. The screener reads the source
length and composition from a `<stem>.windows.tsv.gz` sidecar beside the archive.
"""

import csv
import gzip

import yaml
from test_score import ASSAYS, CFG, RECORDS, ROOT

from assaywatch.chance import composition
from assaywatch.match import find_sites
from assaywatch.score import screen_record
from assaywatch.screen import main as screen_main
from assaywatch.screen import sidecar_path

BD = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"
STRICT = {**CFG, "scoring": {**CFG["scoring"], "max_pair_evalue": 0.01}}
# Long enough that a six-and-six pair is indistinguishable from chance (E > 0.01).
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


def test_record_len_decides_the_chance_filter():
    seq = six_and_six()
    own = screen_record(ASSAYS[BD], "w", seq, STRICT)
    assert own.call != "no_amplicon"
    src = screen_record(ASSAYS[BD], "w", seq, STRICT, record_len=SOURCE_LEN).as_row()
    assert src["call"] == "no_amplicon" and src["exclusion"] == "chance_only"


def test_record_len_none_is_the_old_behaviour():
    seq = six_and_six()
    assert screen_record(ASSAYS[BD], "w", seq, STRICT).as_row() == (
        screen_record(ASSAYS[BD], "w", seq, STRICT, record_len=None).as_row()
    )


def _screen(tmp_path, with_sidecar: bool, workers: int) -> dict[str, str]:
    seq = six_and_six()
    fasta = tmp_path / "w.fasta.gz"
    with gzip.open(fasta, "wt") as fh:
        fh.write(f">ACC1.1:1-{len(seq)}\n{seq}\n")
    if with_sidecar:
        comp = ",".join(str(x) for x in composition(seq))
        with gzip.open(sidecar_path(fasta), "wt") as fh:
            fh.write("window_id\taccession\tstart\tend\tsrc_len\tsrc_comp\n")
            fh.write(f"ACC1.1:1-{len(seq)}\tACC1.1\t1\t{len(seq)}\t{SOURCE_LEN}\t{comp}\n")
    cfg = tmp_path / "config.yaml"
    cfg.write_text(yaml.safe_dump(STRICT))
    out = tmp_path / f"calls_{with_sidecar}_{workers}.tsv"
    screen_main(
        [
            str(ROOT / "registry" / f"{BD}.yaml"),
            str(fasta),
            "--config",
            str(cfg),
            "--workers",
            str(workers),
            "-o",
            str(out),
        ]
    )
    return next(csv.DictReader(out.open(), delimiter="\t"))


def test_screen_reads_the_sidecar_serially_and_in_a_pool(tmp_path):
    assert _screen(tmp_path, with_sidecar=False, workers=1)["call"] != "no_amplicon"
    for workers in (1, 2):
        row = _screen(tmp_path, with_sidecar=True, workers=workers)
        assert row["call"] == "no_amplicon" and row["exclusion"] == "chance_only"


def test_sidecar_path_sits_beside_the_archive(tmp_path):
    assert sidecar_path(tmp_path / "2026-10-07.fasta.gz").name == "2026-10-07.windows.tsv.gz"
    assert sidecar_path(tmp_path / "x.fasta").name == "x.windows.tsv.gz"
