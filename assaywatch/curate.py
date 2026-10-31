"""`assaywatch curate <entry>`: run the curation chain on an entry, write what can be
measured or resolved, and print what is left for a human.

The chain, in order, each step one line of the report:

    schema    the entry parses, oligo lengths and undeclared 5' tails, degeneracy
    keys      no YAML key given twice (PyYAML keeps the last and says nothing)
    citation  the DOI resolves at Crossref to the paper the reference names
              -> WRITES citation.doi_verified: true when it does
    taxon     the taxid exists and NCBI's name is the entry's; a missing taxid is
              looked up by name -> WRITES target.taxid when NCBI gives exactly one
    paper     the cited paper is in papers/, or is fetched (Europe PMC, Unpaywall,
              OpenAlex, Elsevier with a key); otherwise it is queued for a human
    oligos    every stored oligo against what the paper prints: exact, revcomp,
              in-text, near:<edits>, absent
    amplicon  the modal product over the local archive -> WRITES amplicon_bp when
              it was unset; a stored value that disagrees is a judgement, not a write
    amplify   the oligos find an amplicon in a sample of the archive's records

Levels: OK, WARN, FAIL (a defect), WROTE (a field filled in), TODO (a judgement
only a curator can make), SKIP (not run: offline, or nothing to run on). `status`
is never touched; only a maintainer sets `active`. Decided 2026-10-29 (ROADMAP,
"Architecture"); the per-step logic came from scripts/check_submission.py,
scripts/check_amplicons.py, scripts/resolve_citations.py and
scripts/verify_oligos_against_paper.py, which this replaces for one entry at a time.
"""

from __future__ import annotations

import argparse
import gzip
import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from assaywatch import ncbi, papers, printed, registry
from assaywatch.collect import stem_order
from assaywatch.credentials import ELSEVIER, ELSEVIER_INSTTOKEN, read_secret
from assaywatch.degeneracy import assay_degeneracy
from assaywatch.fasta import read_fasta
from assaywatch.match import find_sites, modal_amplicon
from assaywatch.schema import OLIGO_MAX, OLIGO_MIN, PROBE_MIN, Assay
from assaywatch.score import load_config, oligo_pools, screen_record

STEPS = ("schema", "keys", "citation", "taxon", "paper", "oligos", "amplicon", "amplify")
LEVELS = ("OK", "WARN", "FAIL", "WROTE", "TODO", "SKIP")

#: A 5' run that is a restriction site and no declared `tail_5prime` is the usual
#: sign of a cloning tail transcribed as if it bound the target.
RESTRICTION_SITES = {
    "GAATTC": "EcoRI",
    "GGATCC": "BamHI",
    "AAGCTT": "HindIII",
    "GTCGAC": "SalI",
    "GCGGCCGC": "NotI",
    "GGCGCC": "KasI/NarI",
    "CTCGAG": "XhoI",
    "CCATGG": "NcoI",
    "CATATG": "NdeI",
    "TCTAGA": "XbaI",
    "GGTACC": "KpnI",
    "ACTAGT": "SpeI",
    "GAGCTC": "SacI",
}
#: Measurement settings, the same scripts/check_amplicons.py audits with.
AMPLICON_MAX_MM = 3
AMPLICON_MAX_LEN = 4000
AMPLICON_MIN_PRODUCTS = 5
AMPLICON_AGREES_WITHIN = 3
#: Edit cap for "near" verdicts against the paper, as the verifier uses.
NEAR_CAP = 3
#: Records longer than this are whole genomes: slow to screen and rarely needed here.
AMPLIFY_MAX_RECORD_BP = 200_000


@dataclass(frozen=True)
class Finding:
    step: str
    level: str
    message: str


@dataclass
class Curation:
    assay_id: str
    path: Path
    findings: list[Finding] = field(default_factory=list)
    wrote: dict[str, Any] = field(default_factory=dict)

    def add(self, step: str, level: str, message: str) -> None:
        assert step in STEPS and level in LEVELS, (step, level)
        self.findings.append(Finding(step, level, message))

    @property
    def failed(self) -> bool:
        return any(f.level == "FAIL" for f in self.findings)

    @property
    def worklist(self) -> list[Finding]:
        """What a human still has to decide or fix."""
        return [f for f in self.findings if f.level in ("TODO", "FAIL")]

    def report(self) -> str:
        lines = [f"== {self.assay_id}"]
        for f in self.findings:
            lines.append(f"  {f.level:<5} {f.step:<9} {f.message}")
        if self.wrote:
            lines.append("  Wrote: " + ", ".join(f"{k} = {v!r}" for k, v in self.wrote.items()))
        if self.worklist:
            lines.append("  Left for a human:")
            lines += [f"    - {f.step}: {f.message}" for f in self.worklist]
        return "\n".join(lines)


# --- helpers -----------------------------------------------------------------


def oligos_of(assay: Assay) -> dict[str, Any]:
    """The assay's oligos by role, pool members included, skipping absent ones."""
    out: dict[str, Any] = {"forward": assay.oligos.forward, "reverse": assay.oligos.reverse}
    if assay.oligos.probe is not None:
        out["probe"] = assay.oligos.probe
    for i, alt in enumerate(assay.oligos.alternates or []):
        out[f"alternate[{i}] {alt.name or ''}".strip()] = alt
    return out


def _is_probe(role: str, oligo: Any) -> bool:
    return role == "probe" or getattr(oligo, "orientation", None) == "probe"


def archives_for(assay: Assay, retrieved: Path) -> list[Path]:
    """Every FASTA archive of this assay's own retrieval group, oldest first; falling
    back to `all` and `asm` under the taxid, then to any group there."""
    if assay.target.taxid is None:
        return []
    base = Path(retrieved) / str(assay.target.taxid)
    own = registry.archive_dir(assay, retrieved)
    for d in (own, base / "all", base / "asm"):
        hits = sorted(d.glob("*.fasta.gz"), key=stem_order)
        if hits:
            return hits
    hits = sorted(base.glob("*/*.fasta.gz"))
    if hits:
        group = hits[0].parent
        return sorted(group.glob("*.fasta.gz"), key=stem_order)
    return []


def _records(paths: Iterable[Path]) -> Iterator[tuple[str, str]]:
    for p in paths:
        yield from read_fasta(p)


def _elsevier_credentials() -> tuple[str, str | None] | None:
    key = read_secret(ELSEVIER)
    return (key, read_secret(ELSEVIER_INSTTOKEN) or None) if key else None


# --- the chain -------------------------------------------------------------------


def curate(
    path: Path,
    *,
    cfg: dict[str, Any],
    email: str,
    retrieved: Path,
    paper_dir: Path,
    fetch_list: Path,
    transport: ncbi.Transport | None = None,
    get: papers.Get | None = None,
    offline: bool = False,
    write: bool = True,
    sample: int = 400,
) -> Curation:
    """Run the chain on one entry. `transport` and `get` default to the real NCBI and
    HTTP clients; tests pass fakes. `write=False` reports what it would write."""
    path = Path(path)
    c = Curation(path.stem, path)
    try:
        assay = registry.load_one(path)
    except Exception as e:  # noqa: BLE001 - a malformed entry is the first thing to report
        c.add("schema", "FAIL", registry._one_line(e))
        return c

    def set_field(dotted: str, value: Any) -> Assay:
        c.wrote[dotted] = value
        if write:
            return registry.edit(path, {dotted: value})
        return assay

    # schema: parses, oligo lengths, undeclared tails, degeneracy
    problems: list[tuple[str, str]] = []
    for role, oligo in oligos_of(assay).items():
        seq = oligo.matching_seq
        floor = PROBE_MIN if _is_probe(role, oligo) else OLIGO_MIN
        if not floor <= len(seq) <= OLIGO_MAX:
            problems.append(("FAIL", f"{role} binding part is {len(seq)} nt, outside {floor}-{OLIGO_MAX}"))
        if oligo.tail_5prime is None:
            head = seq[:12]
            for site, name in RESTRICTION_SITES.items():
                if site in head:
                    problems.append(
                        (
                            "WARN",
                            f"{role} starts with a {name} site ({site}) and declares no tail_5prime; "
                            "if those bases do not bind the target they must be declared",
                        )
                    )
                    break
    deg = assay_degeneracy(assay)
    pool = f"{deg.total_fold}x pool ({deg.tier(cfg)})"
    level = "WARN" if deg.total_fold > 4096 else "OK"
    c.add("schema", level, f"parses as {assay.chemistry.value}, status {assay.status.value}; {pool}")
    for lvl, msg in problems:
        c.add("schema", lvl, msg)

    # keys
    dupes = registry.duplicate_keys(path.read_text())
    if dupes:
        c.add("keys", "FAIL", "key given twice: " + ", ".join(f"{k} (line {ln})" for k, ln in dupes))
    else:
        c.add("keys", "OK", "no key given twice")

    if not offline:
        transport = transport or ncbi.eutils(email, ncbi.api_key())
        get = get or papers.http()

    # citation
    doi = assay.citation.doi
    if offline:
        c.add("citation", "SKIP", "offline")
    elif not doi:
        c.add("citation", "WARN", "no DOI; a primer with no traceable source cannot be checked")
    else:
        cit = papers.crossref(doi, get, email=email)
        if cit is None:
            c.add("citation", "FAIL", f"DOI {doi} does not resolve at Crossref")
        else:
            ref = assay.citation.reference or assay.citation.as_written or ""
            ok, summary = papers.citation_matches(cit, assay.citation.design_year, ref)
            if not ok:
                c.add("citation", "FAIL", f"DOI resolves to {summary}, which does not match the entry")
            elif assay.citation.doi_verified:
                c.add("citation", "OK", summary)
            else:
                assay = set_field("citation.doi_verified", True)
                c.add("citation", "WROTE", f"citation.doi_verified: true ({summary})")

    # taxon
    if offline:
        c.add("taxon", "SKIP", "offline")
    elif assay.target.taxid is None:
        name = (assay.target.taxon_name or "").split(" (")[0].strip()
        if not name:
            c.add(
                "taxon",
                "WARN",
                "no taxid and no taxon_name, so this assay is never screened against anything",
            )
        else:
            ids = ncbi.taxids_named(name, transport)
            if len(ids) == 1:
                assay = set_field("target.taxid", ids[0])
                c.add("taxon", "WROTE", f"target.taxid: {ids[0]} (NCBI's one hit for {name!r})")
            else:
                c.add(
                    "taxon",
                    "TODO",
                    f"{name!r} gives {len(ids)} NCBI taxonomy hits {ids[:5]}; set target.taxid by hand",
                )
    else:
        taxid = assay.target.taxid
        rec = ncbi.taxon_records([taxid], transport).get(taxid)
        want = (assay.target.taxon_name or "").split(" (")[0].strip().lower()
        if rec is None:
            c.add("taxon", "FAIL", f"taxid {taxid} not found in NCBI Taxonomy")
        elif not want:
            c.add("taxon", "WARN", f"taxid {taxid} is {rec.scientific_name}, but the entry names no taxon")
        elif (
            want in (rec.scientific_name.lower(), *rec.other_names)
            or want in rec.lineage_text.lower()
            or rec.scientific_name.lower() in want
        ):
            c.add("taxon", "OK", f"taxid {taxid} = {rec.scientific_name}")
        else:
            c.add(
                "taxon",
                "FAIL",
                f"taxid {taxid} is {rec.scientific_name}, but the entry says {assay.target.taxon_name!r}",
            )

    # paper and oligos
    paper: Path | None = None
    if offline:
        paper = papers.paper_for_doi(doi, paper_dir) if doi and Path(paper_dir).is_dir() else None
        c.add("paper", "SKIP", f"offline; {'using ' + paper.name if paper else 'no local copy'}")
    elif not doi:
        c.add("paper", "SKIP", "no DOI to fetch by")
    else:
        paper, how = papers.obtain(
            doi,
            paper_dir,
            get,
            email=email,
            fetch_list=fetch_list,
            elsevier=_elsevier_credentials(),
            api_key=ncbi.api_key(),
        )
        if paper is None:
            c.add("paper", "TODO", how)
        else:
            c.add("paper", "OK", f"{how}: {paper.name}")
    if paper is None:
        c.add("oligos", "SKIP", "no paper to read")
    else:
        text = printed.file_text(paper)
        runs = printed.printed_oligos(text)
        for role, oligo in oligos_of(assay).items():
            seq = oligo.matching_seq
            candidates = printed.printed_runs_for(_is_probe(role, oligo), seq, text, runs)
            verdict, note = printed.compare(seq, text, candidates, NEAR_CAP)
            level = "OK" if verdict in ("exact", "revcomp") else "WARN" if verdict == "in-text" else "TODO"
            c.add("oligos", level, f"{role} {verdict}" + (f": {note}" if note else ""))

    # amplicon
    archives = archives_for(assay, retrieved)
    if not archives:
        c.add("amplicon", "SKIP", "no archive for this target yet; run retrieval first")
        c.add("amplify", "SKIP", "no archive for this target yet; run retrieval first")
        return c
    fwd, rev, _probes = oligo_pools(assay)
    n_records, n_products, lengths = modal_amplicon(
        _records(archives), fwd[0], rev[0], max_mm=AMPLICON_MAX_MM, max_len=AMPLICON_MAX_LEN
    )
    stored = assay.amplicon_bp
    if n_products < AMPLICON_MIN_PRODUCTS:
        c.add(
            "amplicon",
            "WARN",
            f"only {n_products} of {n_records} archive records give a product; too few to measure",
        )
    else:
        modal, modal_n = lengths.most_common(1)[0]
        spread = ", ".join(f"{bp} bp x{n}" for bp, n in lengths.most_common(3))
        if stored is None and assay.amplicon_bp_range:
            c.add(
                "amplicon", "OK", f"measured {spread}; the entry declares a range {assay.amplicon_bp_range}"
            )
        elif stored is None:
            assay = set_field("amplicon_bp", modal)
            c.add("amplicon", "WROTE", f"amplicon_bp: {modal} ({modal_n} of {n_products} products; {spread})")
        elif abs(stored - modal) <= AMPLICON_AGREES_WITHIN:
            c.add(
                "amplicon",
                "OK",
                f"stored {stored} bp, measured {modal} bp ({modal_n} of {n_products} products)",
            )
        else:
            c.add(
                "amplicon",
                "TODO",
                f"stored {stored} bp but the archive measures {modal} bp in {modal_n} of {n_products} "
                f"products ({spread}); the measurement wins once a curator confirms, with the difference "
                "disclosed (amplicon_disagrees_with_paper)",
            )

    # amplify: a sample across the newest archive
    archive = archives[-1]
    meta = archive.with_name(archive.name.replace(".fasta.gz", ".meta.tsv.gz"))
    total = 0
    if meta.exists():
        with gzip.open(meta, "rt") as fh:
            total = max(0, sum(1 for _ in fh) - 1)
    step = max(1, total // sample) if total > sample else 1
    calls: dict[str, int] = {}
    best: dict[str, int] = {}
    seen = 0
    for i, (rid, seq) in enumerate(read_fasta(archive)):
        if i % step or len(seq) > AMPLIFY_MAX_RECORD_BP:
            continue
        call = screen_record(assay, rid, seq, cfg)
        calls[call.call] = calls.get(call.call, 0) + 1
        for role, oligo in oligos_of(assay).items():
            k = min((s.n_mismatches for s in find_sites(oligo.matching_seq, seq, 8)), default=None)
            if k is not None:
                best[role] = min(best.get(role, 99), k)
        seen += 1
        if seen >= sample:
            break
    amplified = sum(calls.get(k, 0) for k in ("detect", "reduced", "fail"))
    summary = ", ".join(f"{n} {k}" for k, n in sorted(calls.items(), key=lambda kv: -kv[1]))
    if amplified:
        c.add("amplify", "OK", f"{amplified} of {seen} sampled records give an amplicon ({summary})")
    else:
        detail = ", ".join(f"{r}: best {k}" for r, k in sorted(best.items())) or "no oligo matched at all"
        if any(k <= 1 for k in best.values()):
            c.add(
                "amplify",
                "WARN",
                f"no amplicon in {seen} sampled records, but an oligo matches closely ({detail} mismatches); "
                "check the orientation, amplicon_bp, and whether this target's records carry the locus",
            )
        else:
            c.add(
                "amplify",
                "FAIL",
                f"no amplicon in {seen} sampled records, and no oligo matches well ({detail} mismatches); "
                "a primer that matches nothing in its own target is usually mistyped, reverse-complemented, "
                "or carries an undeclared 5' tail",
            )
    return c


# --- the command ---------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="assaywatch curate", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("paths", nargs="+", type=Path, help="an entry YAML, or a directory of them")
    ap.add_argument("--email", default=None, help="contact address; Crossref and NCBI both ask for one")
    ap.add_argument("--offline", action="store_true", help="skip the citation, taxon and paper steps")
    ap.add_argument("--dry-run", action="store_true", help="report what would be written; write nothing")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    ap.add_argument("--papers", type=Path, default=Path("papers"))
    ap.add_argument("--fetch-list", type=Path, default=Path("papers/papers-fetch-list.md"))
    ap.add_argument("--sample", type=int, default=400, help="records to screen for the amplify step")
    args = ap.parse_args(argv)
    if not args.offline and not args.email:
        ap.error("--email is required unless --offline is given")
    cfg = load_config(args.config)
    failed = 0
    for target in args.paths:
        for path in registry.files(target):
            c = curate(
                path,
                cfg=cfg,
                email=args.email or "",
                retrieved=args.retrieved,
                paper_dir=args.papers,
                fetch_list=args.fetch_list,
                offline=args.offline,
                write=not args.dry_run,
                sample=args.sample,
            )
            print(c.report())
            print()
            failed += c.failed
    print(f"{failed} entr{'y' if failed == 1 else 'ies'} with at least one failure", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
