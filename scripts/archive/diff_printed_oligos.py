#!/usr/bin/env python3
"""Did a change to the oligo reader change what it finds in real papers?

    python scripts/diff_printed_oligos.py --papers papers --old-rev 826a905
    python scripts/diff_printed_oligos.py --papers papers --old-script /path/to/old_verify.py
    python scripts/diff_printed_oligos.py --papers papers --old-rev 50430bb --fail-on-loss

`printed_oligos` in scripts/verify_oligos_against_paper.py decides which runs of
letters in a paper's text count as oligos. Every verdict (`exact`, `absent`,
`no-oligos`) rests on it, and its thresholds were tuned on the 21 open-access
papers a cloud session could reach, not on the 60 PDFs held locally. A threshold
that fixes one primer can drop another, and the only way to know is to run old and
new over the real files. This does that, and nothing else: no registry, no
network, no verdicts.

For each paper it reads the text with each version's OWN `file_text` (so a change
to how PDFs are read is part of what is compared), extracts oligos with each
version's own `printed_oligos`, and reports the sequences LOST (the old version
found them, the new one does not) and GAINED. A revision too old to read `.txt` or
`.xml` files skips them; `--extractor-only` feeds both versions the NEW reading
instead, which isolates a change to `printed_oligos` from a change to how files
are read, and works on any revision. Read the lost list first: a gained
oligo is usually the point of the change, a lost one is how a change quietly breaks
a verdict. An oligo that merely changed because a notation is now read whole, such
as `(N/I)` no longer splitting a primer in two, shows as one lost fragment pair and
one gained primer; that is expected, and visible as such.

`--old-rev` takes any git revision; the old script is read with `git show`, never
checked out, so the working tree is untouched. It runs against the CURRENT
`assaywatch` package, so a revision old enough to import something that no longer
exists will say so.

Exit code is 0 unless `--fail-on-loss` is given: then 1 if something was lost, and 2 if no
paper was compared at all (every file skipped, or an empty folder), since an empty
comparison proves nothing.
"""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

SCRIPT = "scripts/verify_oligos_against_paper.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def old_script_from_git(rev: str, workdir: Path) -> Path:
    """Write `scripts/verify_oligos_against_paper.py` as of `rev` into `workdir`."""
    try:
        out = subprocess.run(
            # `./` makes the path relative to cwd. Without it git resolves it from the
            # repository's top level, which is wrong when this checkout sits inside a
            # larger repository.
            ["git", "show", f"{rev}:./{SCRIPT}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"git could not read {SCRIPT} at {rev!r}: {e.stderr.strip()}") from None
    path = workdir / "old_verify_oligos_against_paper.py"
    path.write_text(out)
    return path


def readable(module, path: Path) -> bool:
    """Can this version of the script read this kind of file? Older ones read PDFs only."""
    return path.suffix.lower() in getattr(module, "PAPER_SUFFIXES", (".pdf",))


def compare(old, new, papers: Path, extractor_only: bool = False) -> list[dict]:
    rows = []
    for path in sorted(p for p in papers.iterdir() if p.is_file()):
        if path.suffix.lower() not in getattr(new, "PAPER_SUFFIXES", (".pdf",)):
            continue
        if not extractor_only and not readable(old, path):
            rows.append({"file": path.name, "skipped": "the old version cannot read this file type"})
            continue
        text = new.file_text(path)
        before = old.printed_oligos(text if extractor_only else old.file_text(path))
        after = new.printed_oligos(text)
        rows.append(
            {
                "file": path.name,
                "old": len(before),
                "new": len(after),
                "lost": sorted(set(before) - set(after)),
                "gained": sorted(set(after) - set(before)),
            }
        )
    return rows


def report(rows: list[dict]) -> int:
    """Print the comparison; return the number of oligos lost."""
    compared = [r for r in rows if "skipped" not in r]
    changed = [r for r in compared if r["lost"] or r["gained"]]
    lost = sum(len(r["lost"]) for r in compared)
    gained = sum(len(r["gained"]) for r in compared)
    print(f"{'paper':<60} {'old':>4} {'new':>4} {'lost':>5} {'gained':>6}")
    for r in rows:
        if "skipped" in r:
            print(f"{r['file'][:60]:<60} skipped: {r['skipped']}")
        elif r["lost"] or r["gained"]:
            print(
                f"{r['file'][:60]:<60} {r['old']:>4} {r['new']:>4} {len(r['lost']):>5} {len(r['gained']):>6}"
            )
    for r in changed:
        print(f"\n{r['file']}")
        for seq in r["lost"]:
            print(f"  - {seq}")
        for seq in r["gained"]:
            print(f"  + {seq}")
    print(
        f"\n{len(compared)} papers compared, {len(compared) - len(changed)} identical, {len(changed)} changed; "
        f"{lost} oligo(s) lost, {gained} gained"
        + (f"; {len(rows) - len(compared)} skipped" if len(rows) != len(compared) else "")
    )
    if lost:
        print("Read the lost ones first: each is a sequence the old reader found and the new one does not.")
    return lost


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--papers", type=Path, default=ROOT / "papers")
    which = ap.add_mutually_exclusive_group(required=True)
    which.add_argument("--old-rev", help="git revision whose reader to compare against")
    which.add_argument("--old-script", type=Path, help="a copy of the old verify_oligos_against_paper.py")
    ap.add_argument("--fail-on-loss", action="store_true", help="exit 1 if any oligo was lost")
    ap.add_argument(
        "--extractor-only",
        action="store_true",
        help="give both versions the NEW file reading, to compare printed_oligos alone",
    )
    args = ap.parse_args(argv)

    if not args.papers.is_dir():
        raise SystemExit(f"{args.papers} is not a directory")
    new = load_module(ROOT / SCRIPT, "_new_verify")
    with tempfile.TemporaryDirectory() as tmp:
        old_path = args.old_script or old_script_from_git(args.old_rev, Path(tmp))
        old = load_module(old_path, "_old_verify")
        rows = compare(old, new, args.papers, args.extractor_only)
    lost = report(rows)
    compared = [r for r in rows if "skipped" not in r]
    if args.fail_on_loss and not compared:
        # Nothing compared is not "nothing lost": an old revision that cannot read the folder's
        # file type, or an empty folder, would otherwise pass a gate vacuously.
        print(
            "--fail-on-loss: no paper was compared, so nothing can be said "
            "(try --extractor-only, or point --papers at files the old version reads)",
            file=sys.stderr,
        )
        return 2
    return 1 if (args.fail_on_loss and lost) else 0


if __name__ == "__main__":
    raise SystemExit(main())
