#!/usr/bin/env python3
"""Merge curation.yaml onto the parser's draft registry files.

    python apply_curation.py --drafts out/registry_draft --curation curation.yaml --out registry

For each draft:
  1. the first `targets` entry whose regex matches "<assay_group> — <gene>"
     (the draft's `name`) fills target.taxon_name / taxid / genome_type and use_context;
  2. the first `citations` entry whose regex matches citation.as_written fills
     doi / design_year / doi_verified / reference;
  3. `assays[<id>]` is deep-merged last: mappings merge key by key, lists and
     scalars replace.

Nothing in the draft is deleted; curation only adds or overrides. The output
file keeps `status: draft` unless the override sets it. A completeness table
is printed so you can see what still needs a human.

Requires: pyyaml
"""

from __future__ import annotations

import argparse
import copy
import re
from pathlib import Path

import yaml


def deep_merge(base: dict, override: dict) -> dict:
    """Return base with override merged in: dicts recurse, everything else replaces."""
    out = copy.deepcopy(base)
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def first_match(rules: list[dict], text: str, key: str = "match") -> dict | None:
    for r in rules:
        if re.search(r[key], text, re.I):
            return r
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--drafts", type=Path, required=True)
    ap.add_argument("--curation", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    cur = yaml.safe_load(args.curation.read_text())
    targets, citations, assays = cur.get("targets", []), cur.get("citations", []), cur.get("assays", {})
    args.out.mkdir(parents=True, exist_ok=True)

    rows = []
    unused_overrides = set(assays)
    for path in sorted(args.drafts.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text())

        t = first_match(targets, doc.get("name", ""))
        if t:
            doc["target"] = deep_merge(
                doc["target"],
                {"taxon_name": t["taxon_name"], "taxid": t["taxid"], "genome_type": t["genome_type"]},
            )
            doc["use_context"] = list(t.get("use_context", doc.get("use_context", [])))

        c = first_match(citations, doc["citation"].get("as_written") or "")
        if c:
            doc["citation"] = deep_merge(
                doc["citation"],
                {
                    "doi": c["doi"],
                    "design_year": c["design_year"] or doc["citation"].get("design_year"),
                    "doi_verified": c["doi_verified"],
                    "reference": c.get("reference"),
                },
            )

        if doc["id"] in assays:
            doc = deep_merge(doc, assays[doc["id"]])
            unused_overrides.discard(doc["id"])

        doc.setdefault("citation", {}).setdefault("doi_verified", False)

        # Recompute the review flags against the curated state.
        flags = set(doc.get("needs_review") or [])
        if doc["citation"].get("design_year"):
            flags.discard("NO_YEAR")
        if "oligos" in assays.get(doc["id"], {}):
            flags.discard("ORIENTATION_INFERRED_BY_POSITION")
        if not doc["citation"].get("doi"):
            flags.add("DOI_MISSING")
        elif not doc["citation"].get("doi_verified"):
            flags.add("DOI_UNVERIFIED")
        if not doc["target"].get("taxid"):
            flags.add("TAXID_MISSING")
        doc["needs_review"] = sorted(flags) or None

        (args.out / path.name).write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=120))

        rows.append(
            (
                doc["id"],
                "Y" if doc["target"].get("taxid") else ("name" if doc["target"].get("taxon_name") else "-"),
                "Y"
                if doc["citation"].get("doi") and doc["citation"].get("doi_verified")
                else ("unv" if doc["citation"].get("doi") else "-"),
                "Y" if doc["citation"].get("design_year") else "-",
                doc.get("status", "draft"),
            )
        )

    w = max(len(r[0]) for r in rows)
    print(f"{'assay id':<{w}}  taxid  doi  year  status")
    for r in rows:
        print(f"{r[0]:<{w}}  {r[1]:<5}  {r[2]:<3}  {r[3]:<4}  {r[4]}")
    n = len(rows)
    print(
        f"\n{n} assays: taxid {sum(r[1] == 'Y' for r in rows)} filled / {sum(r[1] == 'name' for r in rows)} name-only; "
        f"doi {sum(r[2] == 'Y' for r in rows)} verified / {sum(r[2] == 'unv' for r in rows)} unverified / "
        f"{sum(r[2] == '-' for r in rows)} missing; year {sum(r[3] == 'Y' for r in rows)}"
    )
    if unused_overrides:
        print("WARNING: overrides with no matching draft id:", sorted(unused_overrides))


if __name__ == "__main__":
    main()
