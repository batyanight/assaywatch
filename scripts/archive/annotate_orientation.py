#!/usr/bin/env python3
"""Write the archive's answer into each `orientation_inferred` flag's note. Proposes by default.

    python scripts/annotate_orientation.py --measured .tmp/orientation.tsv --run 2026-10-26
    python scripts/annotate_orientation.py --measured ... --run 2026-10-26 --write

WHAT IT DOES. `scripts/check_orientation.py` counts, per flagged entry, how many records
yield a product under the stored orientation. A pair stored the wrong way round faces
outward and yields none anywhere, so a count in the hundreds is the archive confirming
the inference. This takes that table and puts the number where a reader will meet it:
in the flag's own `note`, dated to the run it came from.

WHAT IT DOES NOT DO. It never removes the flag. `orientation_inferred` records
provenance -- the source did not state the orientation -- and that stays true however
many products the archive yields, the way `oligos_modified` stays true. An entry whose
count is below `--min-products` gets a note saying so rather than a reassuring one.

Registry edits go through `--write` only, so a dry run shows every line that would
change first; the validator and the fixture hook then gate the commit as usual. The
note is ONE sentence appended to whatever the flag already says, never a replacement.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FLAG = "orientation_inferred"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--measured", type=Path, required=True, help="check_orientation.py --tsv output")
    ap.add_argument("--run", required=True, help="the run date the counts came from, e.g. 2026-10-26")
    ap.add_argument("--registry", type=Path, default=REPO / "registry")
    ap.add_argument("--min-products", type=int, default=20)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args(argv)

    counts = {
        r["assay_id"]: (int(r["amplicons"]), int(r["no_amplicon"]))
        for r in csv.DictReader(args.measured.open(), delimiter="\t")
    }
    changed = 0
    for path in sorted(args.registry.glob("*.yaml")):
        text = path.read_text()
        aid = path.stem
        if aid not in counts:
            continue
        # Match the flag item and an optional existing note, preserving indentation.
        # Registry files are hand-written YAML; a regex edit keeps every other byte.
        m = re.search(rf"^(?P<ind>\s*)- flag: {FLAG}\n(?:(?P=ind)  note: (?P<note>.*)\n)?", text, flags=re.M)
        if not m:
            print(f"SKIP {aid}: flag listed in the measurement but not found in the file", file=sys.stderr)
            continue
        products, none = counts[aid]
        if f"archive yields {products} products" in (m.group("note") or ""):
            continue
        if products >= args.min_products:
            verdict = f"the archive yields {products} products and {none} none under this orientation ({args.run} run), so the inference stands"
        elif products == 0:
            verdict = f"the archive yields NO products under this orientation ({args.run} run): a wrong orientation or no target in the archive, and this cannot say which"
        else:
            verdict = f"the archive yields only {products} products and {none} none under this orientation ({args.run} run), too few to confirm it"
        old_note = m.group("note")
        new_note = f"{old_note.rstrip('. ')}. {verdict}" if old_note else verdict
        # Quote the note if it contains YAML-sensitive characters; a plain sentence is fine bare.
        if any(ch in new_note for ch in ":#"):
            new_note = "'" + new_note.replace("'", "''") + "'"
        replacement = f"{m.group('ind')}- flag: {FLAG}\n{m.group('ind')}  note: {new_note}\n"
        new_text = text[: m.start()] + replacement + text[m.end() :]
        changed += 1
        print(f"{'WRITE' if args.write else 'would write'} {aid}: {verdict[:90]}...")
        if args.write:
            path.write_text(new_text)
    print(
        f"\n{changed} entries {'updated' if args.write else 'would be updated'}; run the validator before committing."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
