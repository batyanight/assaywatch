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
    "ADENOVIRUS_dsDNA_Pan_Polymerase_round1.yaml"
    "Canine_distemper_virus_specifi_P_gene_Scagliarini_2007.yaml"
    "CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_Lan_2010_round1.yaml"
    "CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2.yaml"
    "ENTEROVIRUS_ssRNA_VP3_VP1_round2.yaml"
    "Pan_flavivirus_NS5_3_round1.yaml"
    "Pan_flavivirus_NS5_3_round2.yaml"
    "Pan_HERPES_dsDNA_Polymerase_round2.yaml"
    "Paramyxovirinae_Polymerase_L_gene_Tong_2008_round1.yaml"
    "POLYOMAVIRUS_dsDNA_VP1_Johne_2005.yaml"
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
    result=$(esearch -db taxonomy -term "txid${parent_taxid}[Subtree] AND species[Rank]" \
        | efetch -format docsum \
        | xtract -pattern DocumentSummary -element TaxId)
    sleep "$SLEEP"

    if [[ -z "$result" ]]; then
        echo "  WARNING: no species-rank taxids found under ${parent_taxid} (${label})" >&2
        echo "  Falling back to subtree without rank filter..." >&2
        result=$(esearch -db taxonomy -term "txid${parent_taxid}[Subtree]" \
            | efetch -format docsum \
            | xtract -pattern DocumentSummary -element TaxId)
        sleep "$SLEEP"
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

    # Sort numerically, join with ", "
    local yaml_list
    yaml_list=$(echo "$taxids_str" | tr ' ' '\n' | sort -n | tr '\n' ' ' | xargs | sed 's/ /, /g')

    # Use python for reliable YAML-aware insertion
    python3 -c "
import sys
lines = open('$file').readlines()
in_target = False
insert_after = -1
for i, line in enumerate(lines):
    stripped = line.rstrip()
    if stripped == 'target:':
        in_target = True
        continue
    if in_target:
        if line.startswith('  ') and not line.startswith('   '):
            insert_after = i
        elif not line.startswith(' ') and stripped:
            break
if insert_after == -1:
    print(f'ERROR: could not find target block in $file', file=sys.stderr)
    sys.exit(1)
new_line = '  scope_taxids: [$yaml_list]\n'
lines.insert(insert_after + 1, new_line)
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
