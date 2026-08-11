#!/usr/bin/env bash
# Standing check: which FRONTIER-MAP section-B items already have a finding on disk?
# Run this BEFORE dispatching any lane. One second beats three lanes.
cd "$(dirname "$0")/.." || exit 1
echo "frontier items with a finding already on disk:"
for n in $(seq 1 20); do
  hits=$(grep -rl "frontier_item: F-$n\b" findings/ 2>/dev/null | grep -v 'prereg' | head -3)
  [ -n "$hits" ] && { echo "  F-$n:"; echo "$hits" | sed 's|^|    |'; }
done
echo
echo "(absence here is NOT proof an item is open — a finding may answer an item without carrying the tag.)"
