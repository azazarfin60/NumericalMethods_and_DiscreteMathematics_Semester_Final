#!/usr/bin/env bash
# Gate V9 · Markdown and writing rules · runs every phase.
#
# Checks only the answer directories. The frozen sources under PreviousYearQuestions/
# and the textbook are out of scope, so their pre-existing defects must not fail
# this gate.
#
# Two passes. The first pass is the authoritative fence-state check, which reads
# the real files because it needs to see inside code fences to document them.
# The second pass runs the section 8 greps against copies with code blanked, since
# a README that shows correct markup would otherwise fail the same greps that
# catch broken markup. That gap is the one the guideline already flags for rule
# 1.1, closed the same way.
#
# Exits 0 when every check passes, 1 otherwise.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

DIRS=(answers_exam_style answers_explanation topicwise_answers_exam_style \
      topicwise_answers_explanation CT_Questions)

TMP=$(mktemp -d) || exit 1
trap 'rm -rf "$TMP"' EXIT

fail=0
note() { printf '\n=== %s ===\n' "$1"; }
bad()  { fail=1; printf 'FAIL: %s\n' "$1"; }

# --- rule 1.1, authoritative, on the real files -------------------------------
note "rule 1.1  \$\$ fence glued to content"
out=$(node scripts/normalize-vault-math.mjs "${DIRS[@]}" 2>&1)
if printf '%s\n' "$out" | grep -q 'defects found : 0'; then
  printf 'clean\n'
else
  printf '%s\n' "$out" | tail -25
  bad "math fence defect in an answer file"
fi

# --- build the code-blanked copies the greps run against -----------------------
mkdir -p "$TMP/stripped"
for d in "${DIRS[@]}"; do
  python3 scripts/strip_code.py "$d" "$TMP/stripped/$d" 2>/dev/null
done
S=("$TMP/stripped/answers_exam_style" "$TMP/stripped/answers_explanation" \
   "$TMP/stripped/topicwise_answers_exam_style" \
   "$TMP/stripped/topicwise_answers_explanation" "$TMP/stripped/CT_Questions")

# --- rule 1.3, odd number of \$\$ in a file ------------------------------------
note "rule 1.3  odd number of \$\$ in a file"
odd=0
while IFS= read -r -d '' f; do
  n=$(grep -o '\$\$' "$f" | wc -l)
  [ $((n % 2)) -ne 0 ] && { printf 'FAIL: %s has %s\n' "${f#"$TMP/stripped/"}" "$n"; odd=1; }
done < <(find "${S[@]}" -name '*.md' -print0)
[ "$odd" -eq 0 ] && printf 'clean\n' || bad "unbalanced \$\$"

# --- rule 1.6, commands KaTeX does not support ---------------------------------
note "rule 1.6  KaTeX-unsupported commands"
if grep -rnP '\\(label|ref|eqref|newcommand|renewcommand|def|href|url|htmlClass|htmlId|htmlStyle)\b' \
     --include='*.md' "${S[@]}"; then
  bad "unsupported command"
else
  printf 'clean\n'
fi

# --- rule 2.3, image path with a space -----------------------------------------
note "rule 2.3  image path with a space"
if grep -rnP '!\[[^\]]*\]\([^)]* [^)]*\)' --include='*.md' "${S[@]}"; then
  bad "image path with a space"
else
  printf 'clean\n'
fi

# --- rule 2.4, empty alt text ---------------------------------------------------
note "rule 2.4  empty alt text"
if grep -rnP '!\[\]\(' --include='*.md' "${S[@]}"; then
  bad "empty alt text"
else
  printf 'clean\n'
fi

# --- rule 5.2, \$\$ fence at column 0 straight after a blockquote line -----------
note "rule 5.2  fence at column 0 after a blockquote line"
h5=0
while IFS= read -r -d '' f; do
  hits=$(awk '/^\$\$/ && prev ~ /^[ \t]*>/ { print FNR } { prev = $0 }' "$f")
  [ -n "$hits" ] && { printf 'FAIL: %s line %s\n' "${f#"$TMP/stripped/"}" "$(echo "$hits" | tr '\n' ' ')"; h5=1; }
done < <(find "${S[@]}" -name '*.md' -print0)
[ "$h5" -eq 0 ] && printf 'clean\n' || bad "fence broke out of its blockquote"

# --- rule 3.2, duplicate heading text inside one file ---------------------------
note "rule 3.2  duplicate heading inside one file"
h3=0
while IFS= read -r -d '' f; do
  hits=$(awk 'FNR==1 { delete seen }
               /^#+ / { if ($0 in seen) print FNR ": " $0; seen[$0]=1 }' "$f")
  [ -n "$hits" ] && { printf 'FAIL: %s %s\n' "${f#"$TMP/stripped/"}" "$(echo "$hits" | tr '\n' ';')"; h3=1; }
done < <(find "${S[@]}" -name '*.md' -print0)
[ "$h3" -eq 0 ] && printf 'clean\n' || bad "duplicate heading"

# --- writing_style.md, no em dash -----------------------------------------------
note "writing_style.md  em dash"
if grep -rn '—' --include='*.md' "${S[@]}"; then
  bad "em dash"
else
  printf 'clean\n'
fi

# --- every image link resolves ---------------------------------------------------
note "images  every link resolves"
missing=0
while IFS= read -r p; do
  found=0
  for d in "${DIRS[@]}"; do
    [ -e "$d/$p" ] && { found=1; break; }
    [ -e "$d/diagrams/$p" ] && { found=1; break; }
  done
  [ "$found" -eq 0 ] && { printf 'FAIL: missing: %s\n' "$p"; missing=1; }
done < <(grep -rhoP '!\[[^\]]*\]\(\K[^)]+' --include='*.md' "${S[@]}" | sort -u)
[ "$missing" -eq 0 ] && printf 'clean\n' || bad "broken image link"

# --- V6, zero invention ----------------------------------------------------------
note "V6  zero invention"
if grep -rniE '\[(Practice|Extra|Similar|Bonus)\]|not from a past paper' "${DIRS[@]}"; then
  bad "invented question inside a past-paper file"
else
  printf 'clean\n'
fi

printf '\n'
if [ "$fail" -eq 0 ]; then
  echo "V9 GREEN"
else
  echo "V9 RED"
fi
exit "$fail"