#!/bin/sh
# Standing integrity check: every embedded EXPECTED_PREREG_SHA must match its pre-registration.
# A pre-registration's value is that it is fixed before the data is seen; a lock a later edit
# can invalidate is not a lock. Run this after ANY bulk edit.
# Established 2026-08-08 after commit b76ec401f (a 702-file propagation) broke FOUR locks at once.
cd "$(dirname "$0")/.." || exit 2
broken=0; checked=0
for s in findings/phase-b-hypotheses/scripts/h-new-*.py; do
  lit=$(grep -oE 'EXPECTED_PREREG_SHA[^"]*"?[a-f0-9]{64}' "$s" 2>/dev/null | grep -oE '[a-f0-9]{64}' | head -1)
  [ -z "$lit" ] && continue
  n=$(basename "$s" .py)
  pr=$(ls findings/phase-b-hypotheses/prereg-"$n"-*.md 2>/dev/null | head -1)
  [ -z "$pr" ] && continue
  checked=$((checked+1))
  cur=$(shasum -a 256 "$pr" | cut -d' ' -f1)
  if [ "$lit" != "$cur" ]; then
    broken=$((broken+1))
    echo "BROKEN  $n"
    echo "        script expects $lit"
    echo "        prereg is      $cur"
  fi
done
echo "checked $checked pre-registration locks; $broken broken"
[ "$broken" -eq 0 ] || exit 1
