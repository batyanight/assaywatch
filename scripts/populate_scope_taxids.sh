#!/usr/bin/env bash
# populate_scope_taxids.sh — look up in-scope taxids for 12 pan-family assays
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

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

# Rate-limit sleep (respects NCBI_API_KEY if set)
SLEEP=0.34
if [[ -n "${NCBI_API_KEY:-}" ]] || [[ -f .secrets/ncbi.key ]]; then
    SLEEP=0.11
fi

# assay_file → taxid to query subtree, taxon description
declare -A ASSAYS=(
    # Pan-flavivirus NS5 (both rounds) — Orthoflavivirus, taxid 11051
    ["Pan_flavivirus_NS5_3_round1.yaml"]="11051|Orthoflavivirus"
    ["Pan_flavivirus_NS5_3_round2.yaml"]="11051|Orthoflavivirus"
    # Pan-coronavirus Lan (both rounds) — Coronaviridae, taxid 11118
    ["CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_Lan_2010_round1.yaml"]="11118|Coronaviridae"
    ["CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2.yaml"]="11118|Coronaviridae"
    # Pan-herpes Polymerase round2 — Orthoherpesviridae, taxid 10292
    ["Pan_HERPES_dsDNA_Polymerase_round2.yaml"]="10292|Orthoherpesviridae"
    # Adenovirus Pan Polymerase round1 — Adenoviridae, taxid 10508
    ["ADENOVIRUS_dsDNA_Pan_Polymerase_round1.yaml"]="10508|Adenoviridae"
    # Enterovirus VP3_VP1 round2 — Enterovirus, taxid 12059
    ["ENTEROVIRUS_ssRNA_VP3_VP1_round2.yaml"]="12059|Enterovirus"
    # CDV Scagliarini — Morbillivirus canis, taxid 11232 (already species-level)
    ["Canine_distemper_virus_specifi_P_gene_Scagliarini_2007.yaml"]="11232|Morbillivirus_canis"
    # Paramyxovirinae Tong round1 — Paramyxoviridae, taxid 11158
    ["Paramyxovirinae_Polymerase_L_gene_Tong_2008_round1.yaml"]="11158|Paramyxoviridae"
    # Polyomavirus VP1 Johne — Polyomaviridae, taxid 151341
    ["POLYOMAVIRUS_dsDNA_VP1_Johne_2005.yaml"]="151341|Polyomaviridae"
)

# Cache subtree lookups so families sharing a taxid (flavi round1+round2) hit NCBI once
declare -A TAXID_CACHE

fetch_species_taxids() {
    local parent_taxid=$1
    local label=$2

    if [[ -n "${TAXID_CACHE[$parent_taxid]:-}" ]]; then
        echo "${TAXID_CACHE[$parent_taxid]}"
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

    TAXID_CACHE[$parent_taxid]="$result"
    echo "$result"
}

patch_yaml() {
    local file=$1
    local taxids_str=$2  # space-separated taxids

    # Build the YAML list: scope_taxids: [12345, 67890, ...]
    # Sort numerically for stable diffs
    local sorted
    sorted=$(echo "$taxids_str" | tr ' ' '\n' | sort -n | tr '\n' ' ')
    local yaml_list
    yaml_list=$(echo "$sorted" | xargs | sed 's/ /, /g')

    # Insert scope_taxids after the taxon_name or query line in the target block,
    # or after genome_type if neither exists. We insert before the first line that
    # is NOT indented (i.e., the next top-level key after target's children).
    # Strategy: find the last line of the target block and insert after it.

    if grep -q 'scope_taxids:' "$file"; then
        echo "  SKIP (scope_taxids already present): $file" >&2
        return
    fi

    # Use python for reliable YAML-aware insertion
    python3 -c "
import sys
lines = open('$file').readlines()
# Find the target: block
in_target = False
insert_after = -1
for i, line in enumerate(lines):
    stripped = line.rstrip()
    if stripped == 'target:':
        in_target = True
        continue
    if in_target:
        # Still inside target block if line starts with spaces
        if line.startswith('  ') and not line.startswith('   '):
            # This is a direct child of target
            insert_after = i
        elif not line.startswith(' ') and stripped:
            # Left the target block
            break
if insert_after == -1:
    print(f'ERROR: could not find target block in $file', file=sys.stderr)
    sys.exit(1)
# Insert after the last target child
new_line = '  scope_taxids: [$yaml_list]\n'
lines.insert(insert_after + 1, new_line)
open('$file', 'w').writelines(lines)
print(f'  Patched: $file ({len(\"$yaml_list\".split(\",\"))} taxids)')
"
}

echo "=== Populating scope_taxids for 12 pan-family assays ==="
echo ""

for assay_file in $(echo "${!ASSAYS[@]}" | tr ' ' '\n' | sort); do
    info="${ASSAYS[$assay_file]}"
    parent_taxid="${info%%|*}"
    label="${info##*|}"

    echo "[$assay_file] target taxid=${parent_taxid} (${label})"
    taxids=$(fetch_species_taxids "$parent_taxid" "$label")
    n=$(echo "$taxids" | wc -w | tr -d ' ')
    echo "  Found ${n} species-rank taxids"

    patch_yaml "registry/${assay_file}" "$taxids"
    echo ""
done

echo "=== Validating registry ==="
python -m assaywatch.validate registry

echo ""
echo "Done. Review the changes with: git diff registry/"
echo "If the taxid counts look right, commit with:"
echo '  git add registry/ && git commit -m "populate scope_taxids for 12 pan-family assays"'
