#!/usr/bin/env bash
# Leak gate. Chain it to the commit:  bash scripts/audit-staged-diff.sh && git commit ...
# Exits non-zero if any flagged term appears OUTSIDE a SHA-locked pre-registration.
#
# Pre-registrations are exempt because they are immutable once run — a prereg records what was
# written before the run and is never corrected, including when it contains something a later
# rule would have excluded. See commit 350.
#
# The pattern is ASSEMBLED from fragments rather than written literally, so this file does not
# match its own search. The first version did, and blocked its own installation.
cd "$(dirname "$0")/.." || exit 1
P="cl""aude|anth""ropic|\bassis""tant\b|scratch""pad|sub""agent"
outside=0
for f in $(git diff --cached --name-only); do
  n=$(git diff --cached -- "$f" | grep -icE "$P")
  [ "$n" = "0" ] && continue
  case "$f" in
    *prereg-*) echo "  exempt (locked prereg): $n hit(s) in $f" ;;
    *)         echo "  *** $n hit(s) in $f"; outside=$((outside+n)) ;;
  esac
done
if [ "$outside" != "0" ]; then
  echo "LEAK GATE: $outside hit(s) outside a locked prereg — ABORTING"; exit 1
fi
echo "LEAK GATE: clean"
