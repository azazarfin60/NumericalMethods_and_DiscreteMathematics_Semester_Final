#!/usr/bin/env bash
# Gate V1 · Source freeze · runs every phase.
#
# The nine source files are hashed. If one changed, the answers built from it may
# no longer match the question that was asked. Nothing else proceeds until the
# change is explained and the hash updated by hand.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

echo "=== V1  source freeze ==="
out=$(cd PreviousYearQuestions && sha256sum -c ../scripts/source_manifest.sha256 2>&1)
printf '%s\n' "$out"

if printf '%s\n' "$out" | grep -q 'FAILED'; then
  echo
  echo "V1 RED: a frozen source changed."
  echo "Explain the change, then regenerate scripts/source_manifest.sha256 by hand."
  exit 1
fi

n=$(printf '%s\n' "$out" | grep -c ': OK$')
echo
echo "V1 GREEN: $n of 9 sources unchanged."
[ "$n" -eq 9 ] || { echo "V1 RED: expected 9 sources."; exit 1; }