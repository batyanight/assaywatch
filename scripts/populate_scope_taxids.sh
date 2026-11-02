#!/usr/bin/env bash
# populate_scope_taxids.sh — look up in-scope taxids for pan-family assays
# and patch their registry YAMLs.
#
# Run from the repo root on the Mac (needs esearch/efetch from Entrez Direct):
#
#   conda activate assaywatch
#   bash scripts/populate_scope_taxids.sh
#
# What it does:
#   1. For each assay, queries NCBI taxonomy for the subtree under its target taxid.
#   2. Filters to species-rank taxids (scope_taxids is exact-match, no ancestry expansion).
#   3. Inserts a scope_taxids line into each YAML's target block.
#   4. Validates the registry afterwards.
#
# CDV Scagliarini is species-level already (taxid 11232), so its scope_taxids
# is just [11232] — included for completeness so drift.py treats it consistently.
#
# Review the output before committing. The script is idempotent: if scope_taxids
# already exists in a YAML, that file is skipped.
#
# Compatible with macOS /bin/bash 3.2 (no associative arrays).

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

# Rate-limit sleep (respects NCBI_API_KEY if set)
SLEEP=0.34
if [[ -n "${NCBI_API_KEY:-}" ]] || [[ -f .secrets/ncbi.key ]]; then
    SLEEP=0.11
fi

# Parallel arrays: FILES[i], TAXIDS[i], LABELS[i]
FILES=(
    "Adenoviridae_POL_Wellehan_2004_round1.yaml"
    "Morbillivirus_canis_P_Scagliarini_2007.yaml"
    "Coronaviridae_RdRp_Quan_2010_round1.yaml"
    "Coronaviridae_RdRp_Quan_2010_round2.yaml"
    "Enterovirus_VP3_VP1_Nix_2006_round2.yaml"
    "Orthoflavivirus_NS5_Scaramozzino_2001_round1.yaml"
    "Orthoflavivirus_NS5_Scaramozzino_2001_round2.yaml"
    "Orthoherpesviridae_POL_VanDevanter_1996_round2.yaml"
    "Paramyxoviridae_L_Tong_2008_round1.yaml"
    "Polyomaviridae_VP1_Johne_2005.yaml"
)
PARENT_TAXIDS=(
    10508   # Adenoviridae
    11232   # Morbillivirus canis (species-level)
    11118   # Coronaviridae
    11118   # Coronaviridae
    12059   # Enterovirus
    11051   # Orthoflavivirus
    11051   # Orthoflavivirus
    10292   # Orthoherpesviridae
    11158   # Paramyxoviridae
    151341  # Polyomaviridae
)
LABELS=(
    "Adenoviridae"
    "Morbillivirus_canis"
    "Coronaviridae"
    "Coronaviridae"
    "Enterovirus"
    "Orthoflavivirus"
    "Orthoflavivirus"
    "Orthoherpesviridae"
    "Paramyxoviridae"
    "Polyomaviridae"
)

# Simple file-based cache so families sharing a taxid hit NCBI once
CACHE_DIR=$(mktemp -d)
trap 'rm -rf "$CACHE_DIR"' EXIT

fetch_species_taxids() {
    local parent_taxid=$1
    local label=$2
    local cache_file="${CACHE_DIR}/${parent_taxid}.txt"

    if [[ -f "$cache_file" ]]; then
        cat "$cache_file"
        return
    fi

    echo "  Querying NCBI taxonomy: txid${parent_taxid}[Subtree] AND species[Rank]..." >&2
    local result
    result=$(esearch -db taxonomy -query "txid${parent_taxid}[Subtree] AND species[Rank]" \
        | efetch -format docsum \
        | xtract -pattern DocumentSummary -element TaxId)
    sleep "$SLEEP"

    if [[ -z "$result" ]]; then
        echo "  WARNING: no species-rank taxids found under ${parent_taxid} (${label})" >&2
        echo "  Falling back to subtree without rank filter..." >&2
        result=$(esearch -db taxonomy -query "txid${parent_taxid}[Subtree]" \
            | efetch -format docsum \
            | xtract -pattern DocumentSummary -element TaxId)
        sleep "$SLEEP"
    fi

    # If still empty, the taxid itself is likely species-level (e.g. CDV 11232).
    # Use it directly so scope filtering works.
    if [[ -z "$result" ]]; then
        echo "  Using parent taxid ${parent_taxid} directly (already species-level)" >&2
        result="$parent_taxid"
    fi

    echo "$result" > "$cache_file"
    echo "$result"
}

patch_yaml() {
    local file=$1
    local taxids_str=$2  # space-separated taxids

    if grep -q 'scope_taxids:' "$file"; then
        echo "  SKIP (scope_taxids already present): $file" >&2
        return
    fi

    if [[ -z "$taxids_str" || "$taxids_str" =~ ^[[:space:]]*$ ]]; then
        echo "  ERROR: no taxids to insert for $file — skipping" >&2
        return 0
    fi

    # Sort numerically, join with ", "
    local yaml_list
    yaml_list=$(echo "$taxids_str" | tr ' ' '\n' | sort -n | tr '\n' ' ' | xargs | sed 's/ /, /g')

    # Use python for reliable YAML-aware insertion.
    # Insert scope_taxids as the last child of the target: block,
    # right before the next top-level key. This avoids splitting
    # multi-line values like folded query strings.
    python3 -c "
import sys
lines = open('$file').readlines()
in_target = False
insert_before = -1
for i, line in enumerate(lines):
    stripped = line.rstrip()
    if stripped == 'target:':
        in_target = True
        continue
    if in_target:
        # First non-indented non-empty line = next top-level key
        if not line.startswith(' ') and stripped:
            insert_before = i
            break
if not in_target:
    print(f'ERROR: no target: block in $file', file=sys.stderr)
    sys.exit(1)
if insert_before == -1:
    insert_before = len(lines)  # target block is last in file
new_line = '  scope_taxids: [$yaml_list]\n'
lines.insert(insert_before, new_line)
open('$file', 'w').writelines(lines)
print(f'  Patched: $file ({len(\"$yaml_list\".split(\",\"))} taxids)')
"
}

echo "=== Populating scope_taxids for ${#FILES[@]} pan-family assays ==="
echo ""

i=0
while [[ $i -lt ${#FILES[@]} ]]; do
    assay_file="${FILES[$i]}"
    parent_taxid="${PARENT_TAXIDS[$i]}"
    label="${LABELS[$i]}"

    echo "[$assay_file] target taxid=${parent_taxid} (${label})"
    taxids=$(fetch_species_taxids "$parent_taxid" "$label")
    n=$(echo "$taxids" | wc -w | tr -d ' ')
    echo "  Found ${n} species-rank taxids"

    patch_yaml "registry/${assay_file}" "$taxids"
    echo ""

    i=$((i + 1))
done

echo "=== Validating registry ==="
python -m assaywatch.validate registry

echo ""
echo "Done. Review the changes with: git diff registry/"
echo "If the taxid counts look right, commit with:"
echo '  git add registry/ && git commit -m "populate scope_taxids for pan-family assays"'
