#!/usr/bin/env python3
"""Propose `conditions` / `performance` values from the papers on disk. Proposes by default.

    python scripts/extract_conditions.py --propose .tmp/conditions.tsv
    python scripts/extract_conditions.py --apply .tmp/conditions.tsv          # dry
    python scripts/extract_conditions.py --apply .tmp/conditions.tsv --write

WHY THIS IS A PROPOSAL AND NOT AN IMPORT. The thermal protocol is prose. One paper
writes "45 cycles of 95 C for 5 s and 60 C for 20 s", the next "standard cycling
conditions", the third puts the temperature in a table caption and the touchdown
programme in a footnote. A regex can FIND the sentence that carries a number; only a
reader can say whether 60 C is this assay's annealing step, the annealing step of the
other assay in the same panel, or an extension. So every value here comes out beside
the sentence it came from, and nothing reaches a registry file until a human has read
that sentence and deleted the rows that are wrong.

The heuristics, stated so a reader knows what they are trusting:

  annealing_c   the temperature in 40-80 C CLOSEST TO the word "anneal", within 60
                characters of it -- a protocol sentence holds every temperature the
                run uses, and taking the first one in range read an RT step at 50 C
                as the annealing step of an assay that anneals at 54; failing
                that, the MIDDLE temperature of a three-temperature cycling sentence
                (95 / 55 / 72 is denature / anneal / extend), which is a convention
                and not a fact, so those rows are marked `middle-of-three`.
  cycles        "<n> cycles", two digits, in a cycling sentence.
  rt            one-step / two-step near reverse transcription.
  mg_mm         a number before `mM MgCl`.
  primer_nm     a concentration near "primer"; micromolar is converted, noted.
  probe_nm      the same near "probe".
  master_mix    the sentence naming a commercial mix, quoted whole, since a buffer
                whose composition the vendor does not publish IS its name.
  efficiency_pct, lod   the paper's own figures, from a sentence naming them.

An entry whose paper is on disk and yields no temperature and no cycle count gets a
`conditions_not_printed` proposal instead, which is a finding about the paper and the
reason `thermo: false` ships.

PAPERS ARE NOT COMMITTED (papers/ is gitignored), so this script's output is the
durable record of what was read. Keep the proposal TSV with the journal entry.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from assaywatch.papers import paper_for_doi  # noqa: E402

FIELDS = ("assay_id", "doi", "paper", "block", "field", "value", "how", "sentence")
# Temperatures a PCR protocol uses for something other than annealing.
DENATURE = 80.0
# A sentence is at most this long before it stops being evidence and becomes a page.
MAX_SENTENCE = 400
# What `--apply --only-sole` will write without a reader. The oligo concentrations
# are NOT here, and the reason is measured rather than cautious: of the first four
# proposals read, one was a 0.2 µM final concentration OCR'd as "0n2 µM" and read as
# 2 µM, and one was a 100 µM STOCK whose final concentration the sentence does not
# give. Both are a judgement about what the number is for, which is a reader's job;
# a temperature, a cycle count and a magnesium concentration are not.
SOLE_FIELDS = ("annealing_c", "cycles", "rt", "mg_mm")


def text_of(path: Path) -> str:
    """The paper as plain text. `pdftotext` for a PDF, tags stripped for JATS XML."""
    if path.suffix.lower() == ".pdf":
        try:
            out = subprocess.run(
                ["pdftotext", "-q", str(path), "-"], capture_output=True, text=True, timeout=120
            )
        except (OSError, subprocess.TimeoutExpired) as e:
            print(f"SKIP {path.name}: pdftotext failed ({e})", file=sys.stderr)
            return ""
        return out.stdout
    raw = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() in (".xml", ".html", ".htm"):
        import html

        raw = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    return raw


def sentences(text: str) -> list[str]:
    """Rough sentence split, after collapsing the line breaks a PDF column leaves.

    Rough is the right level: the unit here is "enough context for a human to judge
    the number", and a clause that runs into the next sentence costs nothing while a
    number torn from its sentence costs everything.
    """
    flat = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.;])\s+(?=[A-Z(])", flat)
    return [p.strip() for p in parts if 10 < len(p) < MAX_SENTENCE]


TEMP_RE = re.compile(r"(\d{2}(?:\.\d)?)\s*(?:°|◦|°)?\s*C\b")


def _temps(s: str) -> list[float]:
    return [float(m.group(1)) for m in TEMP_RE.finditer(s)]


#: A quantity immediately before a unit, read whole: `1.5`, `2,0` (a decimal comma)
#: or `1 . 25` (a decimal point the OCR has spaced out). Two 1990s papers on disk
#: print the last form, from which a plain `\d+(?:\.\d+)?` read 25 mM MgCl2 where
#: the paper says 1.25 -- twenty times the value, caught only by the schema's
#: ceiling. The one before it, Deckers 2009's "2,0 mM", a dot-only pattern read as
#: 0 mM, which no range check can catch at all. Both are the same defect: a number
#: must be read from its left edge, never from wherever a pattern happens to bite.
#: A decimal COMMA takes no space around it, where a decimal point may: allowing
#: both forms to be spaced read "[pH 8.81, 2 mM MgCl" as 81.2 mM.
AMOUNT = r"(\d+(?:\s*\.\s*\d+|,\d+)?)\s*"


def _amount_before(s: str, unit: str) -> float | None:
    """The number this sentence gives for `unit`, or None.

    A STATED FINAL CONCENTRATION WINS OVER THE STOCK. Kuno 1998 writes "3 µl of 50
    mM MgCl2 (final concentration, 1.5 mM)": both numbers are about magnesium, one
    is what the reaction contains and the other is what the bottle contains, and
    reading the bottle makes a reaction look 33 times over-magnesiated.
    """
    anchor = re.search(AMOUNT + unit, s, re.I)
    if not anchor:
        return None
    # The window is anchored on THIS unit, so a "final concentration" belonging to
    # some other reagent in the same sentence cannot answer for it.
    tail = s[anchor.end() : anchor.end() + 60]
    if m := re.search(r"final concentration[,:\s]{0,3}" + AMOUNT + r"mM", tail, re.I):
        return float(re.sub(r"\s+", "", m.group(1)).replace(",", "."))
    return float(re.sub(r"\s+", "", anchor.group(1)).replace(",", "."))


def _temp_near_anneal(s: str) -> float | None:
    """The temperature closest to the word "anneal", not the first one in range.

    The first-in-range reading was wrong on the first paper it met: "15 min at 50 C
    for reverse transcription, 2 min of denaturation at 95 C and 50 cycles of
    denaturation at 95 C for 15 s and annealing at 54 C for 30 s" gave 50, the RT
    step. A protocol sentence holds every temperature the run uses, so proximity to
    the word is the only thing that distinguishes them.
    """
    low = s.lower()
    anneal = [m.start() for m in re.finditer(r"anneal", low)]
    if not anneal:
        return None
    # Two shapes where the paper itself says which temperature it is, tried before
    # proximity. Plain distance gets "52 C for 1 min (annealing) and 68 C for 30 s
    # (elongation)" wrong, because the label sits nearer to the elongation
    # temperature than to the one it labels.
    # The parenthesised-label shape is tried FIRST, because "and annealing at 54 C"
    # and "52 C (annealing) and 68 C" both put a number after the word and only the
    # second means the one before it.
    for pat in (
        r"(\d{2}(?:\.\d)?)\s*(?:°|◦|°)?\s*C[^.()]{0,30}?\(\s*anneal",
        r"anneal\w*[^.\d]{0,20}(\d{2}(?:\.\d)?)\s*(?:°|◦|°)?\s*C",
    ):
        if m := re.search(pat, s, re.I):
            t = float(m.group(1))
            if 40 <= t < DENATURE:
                return t
    best: tuple[int, float] | None = None
    for m in TEMP_RE.finditer(s):
        t = float(m.group(1))
        if not 40 <= t < DENATURE:
            continue
        gap = min(abs(m.start() - a) for a in anneal)
        if gap <= 60 and (best is None or gap < best[0]):
            best = (gap, t)
    return best[1] if best else None


def propose_for(text: str) -> list[tuple[str, str, str, str, str]]:
    """[(block, field, value, how, sentence)] for one paper, one row per field.

    EVERY candidate is collected, not the first, because the count is the thing a
    reviewer most needs: a methods paper that prints one programme gives one
    annealing temperature and the attribution is unambiguous, while a paper
    describing a panel, a nested protocol or a touchdown prints several and only a
    reader can say which belongs to this entry. The row's `how` says which case it
    is, and `--apply --only-sole` will take the first kind and leave the second.
    """
    cands: dict[tuple[str, str], list[tuple[str, str, str]]] = {}

    def add(block: str, field: str, value: object, how: str, sentence: str) -> None:
        cands.setdefault((block, field), []).append((str(value), how, sentence))

    for s in sentences(text):
        low = s.lower()
        cycling = "cycle" in low or "cycling" in low or "amplification" in low
        if (near := _temp_near_anneal(s)) is not None:
            add("conditions", "annealing_c", near, "temperature nearest the word anneal", s)
        elif cycling:
            temps = _temps(s)
            if len(temps) >= 3 and temps[0] >= DENATURE and 40 <= temps[1] < DENATURE:
                add("conditions", "annealing_c_middle", temps[1], "middle-of-three", s)
        if m := re.search(r"(\d{2})\s*cycles", low):
            add("conditions", "cycles", int(m.group(1)), "n cycles", s)
        if re.search(r"\b(one|single)[- ]step\b", low) and ("rt" in low or "reverse transcri" in low):
            add("conditions", "rt", "one_step", "one-step near RT", s)
        elif re.search(r"\btwo[- ]step\b", low) and ("rt" in low or "reverse transcri" in low):
            add("conditions", "rt", "two_step", "two-step near RT", s)
        # The lookbehind refuses a number whose decimal point the OCR has spaced
        # out: Rahn 1992 prints "1 . 25 mm MgCl 2", from which the bare pattern
        # read 25 mM -- twenty times the real value, and caught only by the
        # schema's own ceiling.
        if (mg := _amount_before(s, r"mM\s*MgCl")) is not None:
            add("conditions", "mg_mm", mg, "mM MgCl", s)
        for field, word in (("primer_nm", "primer"), ("probe_nm", "probe")):
            if word not in low:
                continue
            if m := re.search(r"(\d+(?:\.\d+)?)\s*nM", s):
                add("conditions", field, float(m.group(1)), f"nM near {word}", s)
            elif m := re.search(r"(\d+(?:\.\d+)?)\s*(?:µ|u|μ)M", s):
                add("conditions", field, float(m.group(1)) * 1000, f"uM near {word}, converted", s)
        if re.search(r"master ?mix|supermix|universal pcr", low):
            add("conditions", "master_mix", "SEE SENTENCE", "names a commercial mix", s)
        if m := re.search(r"efficienc\w*[^.]{0,40}?(\d{2,3}(?:\.\d+)?)\s*%", low):
            add("performance", "efficiency_pct", float(m.group(1)), "efficiency %", s)
        if re.search(r"limit of detection|\blod\b|detection limit", low):
            add("performance", "lod", "SEE SENTENCE", "names an LoD", s)

    # The word "anneal" wins over the convention: a paper that labels its annealing
    # step is not read by position as well.
    if ("conditions", "annealing_c") not in cands:
        mid = cands.pop(("conditions", "annealing_c_middle"), None)
        if mid:
            cands[("conditions", "annealing_c")] = mid
    cands.pop(("conditions", "annealing_c_middle"), None)

    rows: list[tuple[str, str, str, str, str]] = []
    for (block, field), items in cands.items():
        distinct = sorted({v for v, _, _ in items})
        value, how, sentence = items[0]
        if len(distinct) == 1:
            how = f"{how}; sole value in the paper"
        else:
            how = f"{how}; AMBIGUOUS, {len(distinct)} values in the paper: {', '.join(distinct)}"
        rows.append((block, field, value, how, sentence))
    return rows


def entries(registry: Path) -> list[tuple[str, str]]:
    """[(assay_id, doi)] for every entry that cites a DOI."""
    out = []
    for path in sorted(registry.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text()) or {}
        doi = ((doc.get("citation") or {}).get("doi") or "").strip()
        if doi:
            out.append((path.stem, doi))
    return out


def propose(args) -> int:
    rows: list[dict[str, str]] = []
    no_paper = silent = 0
    for aid, doi in entries(args.registry):
        paper = paper_for_doi(doi, args.papers)
        if paper is None:
            no_paper += 1
            continue
        text = text_of(paper)
        if not text.strip():
            no_paper += 1
            continue
        got = propose_for(text)
        has_protocol = any(f in ("annealing_c", "cycles") for _, f, _, _, _ in got)
        if not has_protocol:
            silent += 1
            rows.append(
                {
                    "assay_id": aid,
                    "doi": doi,
                    "paper": paper.name,
                    "block": "needs_review",
                    "field": "conditions_not_printed",
                    "value": "true",
                    "how": "no temperature and no cycle count found",
                    "sentence": "",
                }
            )
        for block, field, value, how, sentence in got:
            rows.append(
                {
                    "assay_id": aid,
                    "doi": doi,
                    "paper": paper.name,
                    "block": block,
                    "field": field,
                    "value": value,
                    "how": how,
                    "sentence": sentence,
                }
            )
    with args.propose.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    assays = len({r["assay_id"] for r in rows})
    print(
        f"{len(rows)} proposals over {assays} entries -> {args.propose}\n"
        f"{no_paper} entries have no readable paper on disk; "
        f"{silent} papers on disk print no protocol this can find.\n"
        "READ THE SENTENCE COLUMN AND DELETE EVERY ROW YOU DO NOT BELIEVE, then "
        "re-run with --apply.",
    )
    return 0


def _block_yaml(block: str, values: dict[str, str]) -> str:
    """`conditions:` / `performance:` as the registry's hand-written YAML."""
    lines = [f"{block}:"]
    for field, value in values.items():
        lines.append(f"  {field}: {value}")
    return "\n".join(lines) + "\n"


def apply_rows(args) -> int:
    rows = list(csv.DictReader(args.apply.open(), delimiter="\t"))
    by_assay: dict[str, list[dict[str, str]]] = {}
    skipped = {"reader": 0, "ambiguous": 0, "nested": 0}
    for r in rows:
        if r.get("value", "").strip() in ("", "SEE SENTENCE"):
            skipped["reader"] += 1  # a value only a reader can write; left to them
            continue
        # `middle-of-three` is a convention (95 / 55 / 72 is denature / anneal /
        # extend), not the paper's own label, so it is a reading and goes to the
        # curator rather than into a file unread.
        if args.only_sole and ("AMBIGUOUS" in r.get("how", "") or "middle-of-three" in r.get("how", "")):
            skipped["ambiguous"] += 1
            continue
        # A nested protocol's rounds share a paper and almost never share a
        # programme, and nothing here can tell which round a sentence describes.
        if args.only_sole and re.search(r"_round\d", r["assay_id"]):
            skipped["nested"] += 1
            continue
        if args.only_sole and r["field"] not in SOLE_FIELDS:
            skipped["reader"] += 1
            continue
        by_assay.setdefault(r["assay_id"], []).append(r)

    changed = 0
    for aid, items in sorted(by_assay.items()):
        path = args.registry / f"{aid}.yaml"
        if not path.exists():
            print(f"SKIP {aid}: no such entry", file=sys.stderr)
            continue
        text = path.read_text()
        new_text = text
        for block in ("conditions", "performance"):
            values = {r["field"]: r["value"] for r in items if r["block"] == block}
            if not values:
                continue
            if re.search(rf"^{block}:", new_text, flags=re.M):
                print(f"SKIP {aid}: {block} already present; edit it by hand", file=sys.stderr)
                continue
            # Inserted before `use_context:`, which every entry carries, so the
            # file keeps its hand-written order and every other byte.
            anchor = re.search(r"^use_context:", new_text, flags=re.M)
            if not anchor:
                print(f"SKIP {aid}: no use_context anchor", file=sys.stderr)
                continue
            new_text = new_text[: anchor.start()] + _block_yaml(block, values) + new_text[anchor.start() :]
        if new_text != text:
            changed += 1
            fields = ", ".join(sorted(f"{r['block']}.{r['field']}" for r in items))
            print(f"{'WRITE' if args.write else 'would write'} {aid}: {fields}")
            if args.write:
                path.write_text(new_text)
    print(
        f"\n{changed} entries {'updated' if args.write else 'would be updated'}; "
        f"skipped {skipped['reader']} rows only a reader can fill, "
        f"{skipped['ambiguous']} ambiguous, {skipped['nested']} nested rounds. "
        "Quote the paper's own sentence in notes_curator for every value kept, then "
        "run the validator before committing."
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=REPO / "registry")
    ap.add_argument("--papers", type=Path, default=REPO / "papers")
    ap.add_argument("--propose", type=Path, help="write a proposal TSV here")
    ap.add_argument("--apply", type=Path, help="a reviewed proposal TSV to apply")
    ap.add_argument("--write", action="store_true", help="with --apply: actually edit the registry")
    ap.add_argument(
        "--only-sole",
        action="store_true",
        help="with --apply: take only values the paper states once, and no nested round",
    )
    args = ap.parse_args(argv)
    if bool(args.propose) == bool(args.apply):
        ap.error("give exactly one of --propose or --apply")
    return propose(args) if args.propose else apply_rows(args)


if __name__ == "__main__":
    sys.exit(main())
