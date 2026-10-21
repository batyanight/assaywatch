#!/usr/bin/env python3
"""Convert the WCS Molecular Lab primer spreadsheet into AssayWatch inputs.

Two outputs:

1. A flat staging table (TSV), one row per oligo, with the sequence cleaned of
   dye/quencher/LNA notation and the orientation, amplicon, citation, control
   and warning flags pulled out of the surrounding cells. This is the thing a
   human curates; nothing here is trusted without review.

2. A directory of draft registry YAML files, one per candidate assay (a block
   of oligos that contains at least one forward and one reverse primer).
   Every draft has ``status: draft`` and null ``taxid``/``doi`` so the schema
   validator rejects it until a human fills those in.

The spreadsheet has no consistent column structure, so the parser does not
trust column positions. For every row it looks for a cell that *is* a
sequence (after stripping modifications) and then classifies the other
cells by what they look like. Assay group and gene are carried forward from
the last row that set them, which is how the spreadsheet's visual layout
(one group label, many oligo rows beneath it) is encoded.

Usage:
    python parse_wcs_primers.py --xlsx Primers.xlsx --out-dir out/

Requires: openpyxl, pyyaml
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml
from openpyxl import load_workbook

# --------------------------------------------------------------------------
# Sequence cleaning
# --------------------------------------------------------------------------

# IUPAC nucleotide codes plus I (inosine, used heavily in PREDICT primers).
IUPAC = set("ACGTURYSWKMBDHVN")
SEQ_ALPHABET = IUPAC | {"I", "+"}  # '+' marks an LNA base in IDT notation

# Dye/quencher tokens that appear glued onto probe sequences. Longest first so
# that e.g. MGBNFQ is removed before MGB would be. Matched case-insensitively.
MOD_TOKENS = [
    "5ATTO647NN",
    "ATTO647NN",
    "ATTO647N",
    "ATTO647",
    "3IABKFQ",
    "3IABRQSP",
    "IABKFQ",
    "IABRQSP",
    "IABRQ",
    "MGBNFQ",
    "MGBNQF",
    "MGB-NFQ",
    "56-FAM",
    "6FAM",
    "5HEX",
    "6HEX",
    "IOWA BLACK",
    "RQ-SP",
    "TAMRA",
    "BHQ1",
    "BHQ2",
    "BHQ",
    "IBRQ",
    "IBFQ",
    "FAM",
    "HEX",
    "CY5",
    "ZEN",
    "TAO",
    "MGB",
    "NFQ",
]
MOD_RE = re.compile("|".join(re.escape(t) for t in MOD_TOKENS), re.IGNORECASE)

REPORTERS = [
    ("FAM", re.compile(r"FAM", re.I)),
    ("HEX", re.compile(r"HEX", re.I)),
    ("Cy5", re.compile(r"CY5", re.I)),
    ("ATTO647N", re.compile(r"ATTO ?647", re.I)),
]
QUENCHERS = [
    ("MGB-NFQ", re.compile(r"MGB", re.I)),
    ("ZEN/IowaBlackFQ", re.compile(r"ZEN", re.I)),
    ("IowaBlackRQ", re.compile(r"IABRQ|IBRQ|RQ-SP", re.I)),
    ("IowaBlackFQ", re.compile(r"IABKFQ|IBFQ|3IABKFQ", re.I)),
    ("TAMRA", re.compile(r"TAMRA", re.I)),
    ("BHQ", re.compile(r"BHQ", re.I)),
]

SEQ_RUN_RE = re.compile(r"[ACGTURYSWKMBDHVNI+]{15,}")


@dataclass
class CleanedSeq:
    seq: str  # uppercase, mods and whitespace removed, LNA '+' removed
    seq_iupac: str  # same but inosine -> N so a strict IUPAC matcher accepts it
    reporter: str
    quencher: str
    lna: bool
    inosine: bool


def clean_sequence(raw: str) -> CleanedSeq | None:
    """Pull a nucleotide sequence out of a spreadsheet cell, or return None.

    Order of operations matters:
      1. strip parentheticals and anything after a note marker ('*', 'Tm='),
         because '(same as above)' or '**** C changed to a Y' would otherwise
         contribute IUPAC-looking letters;
      2. remove dye/quencher tokens as whole words, because '3IABkFQ' is made
         of IUPAC letters and would survive a character filter;
      3. collapse whitespace and dashes (sequences are often typed as
         space-separated triplets, e.g. 'CCT TGA TAT');
      4. take the longest run of sequence characters of length >= 15.
    """
    if raw is None:
        return None
    text = str(raw)
    text = re.sub(r"\([^)]*\)", " ", text)  # (3' Iowa Black...) etc.
    text = re.split(r"\*{2,}|Tm\s*=", text)[0]  # drop trailing notes
    reporter = next((n for n, rx in REPORTERS if rx.search(text)), "")
    quencher = next((n for n, rx in QUENCHERS if rx.search(text)), "")
    text = MOD_RE.sub(" ", text)
    text = re.sub(r"[\s\-/,’'5’3]+", "", text).upper()  # join triplets, drop 5'-/-3'
    runs = SEQ_RUN_RE.findall(text)
    if not runs:
        return None
    run = max(runs, key=len)
    # Guard against plain words that happen to be IUPAC-only (rare but possible):
    # a real oligo is mostly ACGT.
    acgt = sum(run.count(b) for b in "ACGT")
    if acgt / len(run) < 0.5:
        return None
    lna = "+" in run
    seq = run.replace("+", "")
    inosine = "I" in seq
    return CleanedSeq(
        seq=seq,
        seq_iupac=seq.replace("I", "N"),
        reporter=reporter,
        quencher=quencher,
        lna=lna,
        inosine=inosine,
    )


# --------------------------------------------------------------------------
# Cell classification
# --------------------------------------------------------------------------

AMPLICON_RE = re.compile(r"(~?\s*\d{2,4}(?:\s*[-–]\s*\d{2,4})?)\s*(?:bp|b\.p\.)", re.I)
CITATION_RE = re.compile(
    r"et al|\b(19|20)\d{2}\b|doi|protocol|in house|unpublished|developed|journal|\bJ\b\.",
    re.I,
)
CONTROL_RE = re.compile(
    r"\bUC\s?\d|universal control|\bDNA\b|vaccine|plasmid|cDNA|gBlock|from clinical",
    re.I,
)
ROUND_RE = re.compile(r"^\s*Round\s*(\d)", re.I)
GENE_WORDS_RE = re.compile(
    r"gene|rDNA|rRNA|ITS|16S|18S|23S|28S|5\.8S|region|protein|subunit|polymerase|segment|cyto|"
    r"spacer|promoter|RdRp|capsid|hexon|glycoprotein|terminase|NS\d|VP\d|L1|S gene|N gene|P gene|H gene|F gene",
    re.I,
)
REUSE_RE = re.compile(r"same as|same reverse|same forward|same primer", re.I)


def looks_like_gene(text: str) -> bool:
    """Col B is usually a gene, but sometimes a free-text note. Short, or gene-ish words, wins."""
    return len(text) <= 45 or bool(GENE_WORDS_RE.search(text))


# Ordering status is deliberately NOT a flag. "need to order" in the source
# spreadsheet described the lab's stock on one day in 2018, not a property of the
# assay, and the spreadsheet is a starting point rather than the registry's state.
FLAG_PATTERNS = {
    "DO_NOT_USE": re.compile(r"do not use|incorrect|did not work|not recommended", re.I),
    "CROSS_REACTIVE": re.compile(r"x-?react|cross ?react", re.I),
    "UNTESTED": re.compile(r"untested|in development", re.I),
    "MODIFIED_IN_HOUSE": re.compile(
        r"\bmod\b|modified|corrected|adjusted|changed to|in house|in-house|unpublished|designed by", re.I
    ),
    "NESTED": re.compile(r"\bround\s*[12]\b|nested", re.I),
}

# Orientation from the oligo name. Checked in order; first hit wins.
PROBE_RE = re.compile(r"probe|MGB|LNA", re.I)
# Whole-token forms: F, Fwd, FWD1, forward, sense, lf, 1F, 2743s, FP, U12683 (PREDICT 'upper')
FWD_TOKEN_RE = re.compile(r"^(f|fwd|forward|sense|lf|fp|s)\d*$|^\d+f$|^\d{3,}s$|^u\d{3,}$", re.I)
# R, Rev, RVS1, reverse, antisense, as, 1R, 2746-as, RP, 1494c, L13294 (PREDICT 'lower')
REV_TOKEN_RE = re.compile(
    r"^(r|rev|rvs|reverse|antisense|as|rp)\d*$|^\d+r$|^\d{3,}as$|^\d+c$|^l\d{3,}$", re.I
)
# Suffix forms: HaemF, PMP1F, Ziao18SR2, TSCDV-HF, SunshineAS1
# Case matters here: 'Chytr' ends in r but is not a reverse primer. A bare F/R
# suffix must be upper case; lower case only counts when a digit follows (VERTCOIr1).
FWD_SUFFIX_RE = re.compile(r"^[A-Za-z0-9]+(F\d*|f\d+|[Ff][Ww][Dd]\d*|FW\d*)$")
REV_SUFFIX_RE = re.compile(r"^[A-Za-z0-9]+(R\d*|r\d+|[Rr][Vv][Ss]\d*|[Rr][Ee][Vv]\d*)$|^[A-Za-z]{3,}AS\d*$")
# Trailing words that hide the F/R suffix: 2Farctic, Fouter, polRinner, TSADHEXRnew, CDVF5primeUTR
TRAILING_WORD_RE = re.compile(r"(arctic|new|seq|inner|outer|mod|utr|prime)+$", re.I)
# Tokens that end in F/R but are not orientation markers
NOT_ORIENTATION_RE = re.compile(r"^(pcr|qpcr|mgb|nfq|lna|rt|its|for|nr|dr\d*)$", re.I)


def orientation_from_name(name: str, cleaned: CleanedSeq) -> tuple[str, str]:
    """Return (orientation, how_decided). Orientation is forward/reverse/probe/unknown."""
    if cleaned.reporter or cleaned.quencher or PROBE_RE.search(name):
        return "probe", "name_or_dye"
    # "(f) 5934" / "(r) 6597" style annotations are the most reliable signal.
    for tok in re.findall(r"\(([^)]*)\)", name):
        if FWD_TOKEN_RE.match(tok.strip()):
            return "forward", "paren_token"
        if REV_TOKEN_RE.match(tok.strip()):
            return "reverse", "paren_token"
    base = re.sub(r"\([^)]*\)", " ", name)
    tokens = [t for t in re.split(r"[\s_\-/:,*]+", base.strip()) if t]
    for tok in tokens:
        if FWD_TOKEN_RE.match(tok):
            return "forward", "token"
        if REV_TOKEN_RE.match(tok):
            return "reverse", "token"
    for tok in tokens:
        core = TRAILING_WORD_RE.sub("", tok)
        if NOT_ORIENTATION_RE.match(core) or len(core) < 2:
            continue
        if FWD_SUFFIX_RE.match(core):
            return "forward", "suffix"
        if REV_SUFFIX_RE.match(core):
            return "reverse", "suffix"
    return "unknown", "none"


def parse_amplicon(text: str) -> tuple[str, int | None]:
    """Return (raw amplicon text, integer bp or None). Ranges keep the raw text only."""
    m = AMPLICON_RE.search(text)
    if not m:
        return "", None
    raw = m.group(0).strip()
    nums = re.findall(r"\d+", raw)
    bp = int(nums[0]) if len(nums) == 1 else None
    return raw, bp


# --------------------------------------------------------------------------
# Row model
# --------------------------------------------------------------------------


@dataclass
class Oligo:
    row: int
    block_id: int
    assay_group: str
    gene: str
    round: str
    oligo_name: str
    orientation: str
    orientation_source: str
    seq: str
    seq_iupac: str
    seq_len: int
    reporter: str
    quencher: str
    lna: bool
    inosine: bool
    amplicon_raw: str
    amplicon_bp: int | None
    citation: str
    control: str
    flags: str
    raw_seq_cell: str


@dataclass
class Block:
    block_id: int
    assay_group: str
    gene: str
    round: str
    oligos: list[Oligo] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    citations: list[str] = field(default_factory=list)
    controls: list[str] = field(default_factory=list)
    amplicons: list[str] = field(default_factory=list)
    flags: set = field(default_factory=set)


def flags_in(text: str) -> set[str]:
    return {k for k, rx in FLAG_PATTERNS.items() if rx.search(text)}


def parse_sheet(ws) -> list[Block]:
    """Walk the sheet row by row, carrying group/gene/round state forward."""
    blocks: list[Block] = []
    group = gene = rnd = ""
    current: Block | None = None
    block_counter = 0
    seen: dict[tuple[str, str], Oligo] = {}  # (assay_group, normalised name) -> first definition
    pending: dict = {}  # amplicon/citation/control read off a label row, for the next block
    pending_flags: set = set()

    def new_block() -> Block:
        nonlocal block_counter, current, pending, pending_flags
        block_counter += 1
        current = Block(block_counter, group, gene, rnd)
        if "amplicon" in pending:
            current.amplicons.append(pending["amplicon"][0])
        if "citation" in pending:
            current.citations.append(pending["citation"])
        if "control" in pending:
            current.controls.append(pending["control"])
        current.notes.extend(pending.get("notes", []))
        current.flags |= pending_flags
        pending, pending_flags = {}, set()
        blocks.append(current)
        return current

    for row_idx, cells in enumerate(ws.iter_rows(min_row=4), start=4):
        values = [c.value for c in cells]
        strs = [str(v).strip() if v is not None else "" for v in values]
        if not any(strs):
            current = None  # a blank row ends the current block
            continue

        row_text = " | ".join(s for s in strs if s)

        # 1. Find the sequence cell, if any.
        seq_col, cleaned = None, None
        for i, s in enumerate(strs):
            if not s:
                continue
            c = clean_sequence(s)
            if c and (seq_col is None or len(c.seq) > len(cleaned.seq)):
                seq_col, cleaned = i, c

        # 2. Update carried-forward state from non-sequence cells.
        col_a, col_b = strs[0], strs[1] if len(strs) > 1 else ""
        round_hit = next((m for s in strs if (m := ROUND_RE.match(s))), None)
        a_is_note = col_a.startswith(("*", "(")) or bool(FLAG_PATTERNS["DO_NOT_USE"].search(col_a))
        b_is_note = col_b.startswith(("*", "(")) or not looks_like_gene(col_b)
        if col_a and seq_col != 0 and not ROUND_RE.match(col_a) and not a_is_note:
            group = col_a
            gene = col_b if col_b and seq_col != 1 and not b_is_note else ""
            rnd = ""
            current = None
            pending = {}
        elif col_b and seq_col != 1 and not ROUND_RE.match(col_b) and not b_is_note:
            gene = col_b
            rnd = ""
            current = None
            pending = {}
        if (a_is_note and col_a) or (b_is_note and col_b):
            pending_flags |= flags_in(col_a + " " + col_b)
            pending.setdefault("notes", []).append(col_a or col_b)
        if round_hit:
            rnd = f"round{round_hit.group(1)}"
            current = None

        # 3. No sequence. Either this row re-uses an oligo defined earlier in the
        #    same assay group ("ADHEX1R | Same as RVS1", or a bare "ITS4"), or it
        #    is a note; notes are attached to the open block.
        if cleaned is None:
            reuse_name = strs[2] if len(strs) > 2 else ""
            key = (group, re.sub(r"\s+", " ", reuse_name).strip().lower())
            if reuse_name and key in seen and (REUSE_RE.search(row_text) or len(reuse_name) < 15):
                src = seen[key]
                if current is None:
                    new_block()
                assert current is not None
                amplicon_raw, amplicon_bp, citation, control = "", None, "", ""
                for s_ in strs[3:]:
                    if not s_:
                        continue
                    if not amplicon_raw:
                        amplicon_raw, amplicon_bp = parse_amplicon(s_)
                    if not control and CONTROL_RE.search(s_) and len(s_) < 120:
                        control = s_
                    elif not citation and CITATION_RE.search(s_) and len(s_) > 8:
                        citation = s_
                copy = Oligo(
                    **{
                        **asdict(src),
                        "row": row_idx,
                        "block_id": current.block_id,
                        "round": rnd,
                        "amplicon_raw": amplicon_raw,
                        "amplicon_bp": amplicon_bp,
                        "citation": citation,
                        "control": control,
                        "flags": ";".join(
                            sorted(set(src.flags.split(";")) - {""} | {f"REUSED_FROM_ROW_{src.row}"})
                        ),
                    }
                )
                current.oligos.append(copy)
                if amplicon_raw:
                    current.amplicons.append(amplicon_raw)
                if citation:
                    current.citations.append(citation)
                if control:
                    current.controls.append(control)
                continue
            if current is not None and not round_hit:
                current.notes.append(row_text)
                current.flags |= flags_in(row_text)
            elif blocks and not col_a and not col_b and not round_hit:
                blocks[-1].notes.append(row_text)
                blocks[-1].flags |= flags_in(row_text)
            else:
                # A label row with no sequence: its amplicon/citation/control
                # belong to the oligo block that follows it.
                for s_ in strs[2:]:
                    if not s_:
                        continue
                    amp, bp = parse_amplicon(s_)
                    if amp and "amplicon" not in pending:
                        pending["amplicon"] = (amp, bp)
                    elif CONTROL_RE.search(s_) and len(s_) < 120 and "control" not in pending:
                        pending["control"] = s_
                    elif CITATION_RE.search(s_) and len(s_) > 8 and "citation" not in pending:
                        pending["citation"] = s_
            continue

        if current is None:
            new_block()
        assert current is not None

        # 4. Oligo name: the cell to the left, or "NAME, SEQ" inside one cell.
        name = ""
        seq_cell = strs[seq_col]
        if "," in seq_cell and clean_sequence(seq_cell.split(",", 1)[0]) is None:
            name = seq_cell.split(",", 1)[0].strip()
        elif seq_col > 0 and strs[seq_col - 1] and clean_sequence(strs[seq_col - 1]) is None:
            name = strs[seq_col - 1]
        orientation, how = orientation_from_name(name, cleaned)

        # 5. Classify the remaining cells.
        amplicon_raw, amplicon_bp = "", None
        citation, control = "", ""
        for i, s in enumerate(strs):
            if not s or i == seq_col or s == name:
                continue
            if not amplicon_raw:
                amplicon_raw, amplicon_bp = parse_amplicon(s)
            if (
                isinstance(values[i], int)
                and not isinstance(values[i], bool)
                and 80 <= values[i] <= 3000
                and not amplicon_raw
            ):
                amplicon_raw, amplicon_bp = f"{int(values[i])}bp", int(values[i])
            if not control and CONTROL_RE.search(s) and len(s) < 120:
                control = s
            elif not citation and CITATION_RE.search(s) and len(s) > 8:
                citation = s
        # Also read amplicon out of the sequence cell's trailing text (rare).
        if not amplicon_raw:
            amplicon_raw, amplicon_bp = parse_amplicon(seq_cell)

        if not amplicon_raw and current.amplicons and not current.oligos:
            amplicon_raw = current.amplicons[0]
            amplicon_bp = parse_amplicon(amplicon_raw)[1]
        if not citation and current.citations and not current.oligos:
            citation = current.citations[0]
        if not control and current.controls and not current.oligos:
            control = current.controls[0]
        row_flags = flags_in(row_text) | flags_in(group) | flags_in(gene) | current.flags
        oligo = Oligo(
            row=row_idx,
            block_id=current.block_id,
            assay_group=group,
            gene=gene,
            round=rnd,
            oligo_name=name,
            orientation=orientation,
            orientation_source=how,
            seq=cleaned.seq,
            seq_iupac=cleaned.seq_iupac,
            seq_len=len(cleaned.seq),
            reporter=cleaned.reporter,
            quencher=cleaned.quencher,
            lna=cleaned.lna,
            inosine=cleaned.inosine,
            amplicon_raw=amplicon_raw,
            amplicon_bp=amplicon_bp,
            citation=citation,
            control=control,
            flags="",
            raw_seq_cell=seq_cell,
        )
        if len(cleaned.seq) > 60:
            row_flags.add("NOT_AN_OLIGO_LENGTH")  # gBlock or template, not a primer
            oligo.orientation, oligo.orientation_source = "template", "length"
        oligo.flags = ";".join(sorted(row_flags))
        current.oligos.append(oligo)
        seen.setdefault((group, re.sub(r"\s+", " ", name).strip().lower()), oligo)
        current.flags |= row_flags
        if citation:
            current.citations.append(citation)
        if control:
            current.controls.append(control)
        if amplicon_raw:
            current.amplicons.append(amplicon_raw)

    return blocks


def resolve_unknown_orientations(blocks: list[Block]) -> None:
    """Primers whose names carry no F/R marker are paired by order of appearance.

    Within a block, unnamed primers are taken as forward, reverse, forward,
    reverse ... in spreadsheet order, which is how every pair in this sheet is
    laid out. A leftover singleton in a block that already has a forward and a
    reverse primer stays 'unknown' rather than being guessed. This is the only
    inference not read off the spreadsheet, so it is labelled 'position' in
    orientation_source and the curator should check it.
    """
    for b in blocks:
        unknown = [o for o in b.oligos if o.orientation == "unknown"]
        if not unknown:
            continue
        have_f = any(o.orientation == "forward" for o in b.oligos)
        have_r = any(o.orientation == "reverse" for o in b.oligos)
        if len(unknown) % 2 == 1 and have_f and have_r:
            unknown = unknown[:-1]  # leave the odd one out as unknown
        for i, o in enumerate(unknown):
            if len(unknown) == 1:
                o.orientation = "reverse" if have_f and not have_r else "forward"
            else:
                o.orientation = "forward" if i % 2 == 0 else "reverse"
            o.orientation_source = "position"


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------


def slugify(text: str, maxlen: int = 40) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")
    return s[:maxlen].rstrip("_") or "unnamed"


def first_author_year(citation: str) -> tuple[str, int | None]:
    """Best-effort 'Boyle et al, 2004' -> ('Boyle', 2004). Returns ('', None) if unparseable."""
    year = None
    m = re.search(r"\b(19|20)\d{2}\b", citation)
    if m:
        year = int(m.group(0))
    m = re.match(r"\s*([A-Z][A-Za-z'-]+)", citation)
    author = m.group(1) if m else ""
    if author.lower() in {"this", "note", "developed", "modified", "designed", "the", "use", "predict"}:
        author = ""
    return author, year


def block_to_yaml(b: Block, used_ids: Counter) -> dict | None:
    fwd = [o for o in b.oligos if o.orientation == "forward"]
    rev = [o for o in b.oligos if o.orientation == "reverse"]
    probes = [o for o in b.oligos if o.orientation == "probe"]
    if not fwd or not rev:
        return None

    citation = next((c for c in b.citations if c), "")
    author, year = first_author_year(citation)
    chem = "conventional"
    if probes:
        chem = "lna" if probes[0].lna else ("mgb" if "MGB" in probes[0].quencher else "hydrolysis_probe")

    base_id = "_".join(
        p
        for p in [
            slugify(b.assay_group, 30),
            slugify(b.gene, 24),
            author or "",
            str(year) if year else "",
            b.round,
        ]
        if p
    )
    used_ids[base_id] += 1
    assay_id = base_id if used_ids[base_id] == 1 else f"{base_id}_{used_ids[base_id]}"

    def oligo_entry(o: Oligo) -> dict:
        d = {"name": o.oligo_name or None, "seq": o.seq_iupac}
        if o.inosine:
            d["seq_as_written"] = o.seq  # keep the inosine version for the record
        return d

    def probe_entry(o: Oligo) -> dict:
        d = oligo_entry(o)
        d["reporter"] = o.reporter or None
        d["quencher"] = o.quencher or None
        if o.lna:
            d["lna"] = True
        return d

    oligos = {"forward": oligo_entry(fwd[0]), "reverse": oligo_entry(rev[0])}
    if probes:
        oligos["probe"] = probe_entry(probes[0])
    alternates = [oligo_entry(o) for o in fwd[1:] + rev[1:]] + [probe_entry(o) for o in probes[1:]]
    if alternates:
        oligos["alternates"] = alternates

    amplicon_bp = next((o.amplicon_bp for o in b.oligos if o.amplicon_bp), None)
    review = sorted(b.flags)
    if len(fwd) > 1 or len(rev) > 1:
        review.append("MULTIPLE_PRIMERS_IN_BLOCK")
    if any(o.orientation_source == "position" for o in b.oligos):
        review.append("ORIENTATION_INFERRED_BY_POSITION")
    if not year:
        review.append("NO_YEAR")

    return {
        "id": assay_id,
        "name": f"{b.assay_group} — {b.gene}".strip(" —"),
        "target": {"taxid": None, "gene": b.gene or None, "genome_type": None},
        "chemistry": chem,
        "oligos": oligos,
        "amplicon_bp": amplicon_bp,
        "citation": {
            "doi": None,
            "design_year": year,
            "n_sequences_at_design": None,
            "as_written": citation or None,
        },
        "use_context": ["wildlife", "veterinary"],
        "submitted_by": None,
        "status": "draft",
        "source": {
            "spreadsheet": "Primers_for_WCS_Molecular_Lab_updated_021518.xlsx",
            "rows": [o.row for o in b.oligos],
            "positive_control": next((c for c in b.controls if c), None),
            "nested_round": b.round or None,
            "notes": b.notes or None,
        },
        "needs_review": review or None,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--xlsx", required=True, type=Path)
    ap.add_argument("--sheet", default="WCS PRIMER SETS")
    ap.add_argument("--out-dir", required=True, type=Path)
    args = ap.parse_args()

    out = args.out_dir
    (out / "registry_draft").mkdir(parents=True, exist_ok=True)

    ws = load_workbook(args.xlsx, read_only=True, data_only=True)[args.sheet]
    blocks = parse_sheet(ws)
    resolve_unknown_orientations(blocks)

    oligos = [o for b in blocks for o in b.oligos]
    tsv = out / "wcs_primers_staging.tsv"
    with tsv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(asdict(oligos[0]).keys()), delimiter="\t")
        w.writeheader()
        for o in oligos:
            w.writerow(asdict(o))

    used: Counter = Counter()
    n_yaml = 0
    for b in blocks:
        doc = block_to_yaml(b, used)
        if doc is None:
            continue
        with (out / "registry_draft" / f"{doc['id']}.yaml").open("w") as fh:
            yaml.safe_dump(doc, fh, sort_keys=False, allow_unicode=True, width=120)
        n_yaml += 1

    # Summary to stdout so you can sanity-check the run without opening files.
    orient = Counter(o.orientation for o in oligos)
    print(f"blocks: {len(blocks)}  oligos: {len(oligos)}  draft assays: {n_yaml}")
    print(f"orientation: {dict(orient)}")
    print(
        f"probes with reporter: {sum(1 for o in oligos if o.reporter)}  "
        f"LNA: {sum(o.lna for o in oligos)}  inosine: {sum(o.inosine for o in oligos)}"
    )
    print(f"unnamed oligos: {sum(1 for o in oligos if not o.oligo_name)}")
    flag_counts = Counter(f for o in oligos for f in o.flags.split(";") if f)
    print(f"flags: {dict(flag_counts)}")
    print(f"wrote {tsv} and {n_yaml} files in {out / 'registry_draft'}")


if __name__ == "__main__":
    main()
