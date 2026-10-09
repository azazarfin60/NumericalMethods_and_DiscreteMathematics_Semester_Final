#!/usr/bin/env bash
# Gate V2 · Manifest completeness · P0.
#
# Rebuilds the manifest from the frozen sources and checks the totals. A rebuild
# that differs from the committed file means the sources and the manifest have
# drifted apart, which would break every downstream gate.
#
# Checks:
#   202 rows, being 183 paper sub-questions and 19 class-test parts
#   721 paper marks, split 96 96 96 96 97 80 80 80
#   84 subtopics carry a file
#   filelist.txt agrees with the manifest on that set, exactly
#   no unit cross-files against itself
#   every unit id is unique

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

echo "=== V2  manifest completeness ==="
tmp=$(mktemp) || exit 1
cp scripts/answer_manifest.csv "$tmp"
trap 'rm -f "$tmp"' EXIT

if ! python3 scripts/build_manifest.py; then
  echo
  echo "V2 RED: the manifest did not build, or its own checks failed."
  exit 1
fi

if ! cmp -s "$tmp" scripts/answer_manifest.csv; then
  echo
  echo "V2 RED: the rebuild differs from the committed manifest."
  diff <(head -3 "$tmp") <(head -3 scripts/answer_manifest.csv) || true
  exit 1
fi
rm -f "$tmp"; trap - EXIT

python3 - <<'PY'
import collections, csv, os, sys

rows = list(csv.DictReader(open("scripts/answer_manifest.csv", encoding="utf-8")))
fail = []


def check(label, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + label + (("  " + detail) if detail else ""))
    if not ok:
        fail.append(label)


papers = [r for r in rows if r["source"] == "paper"]
cts = [r for r in rows if r["source"] == "class_test"]

check("202 rows", len(rows) == 202, "got %d" % len(rows))
check("183 paper sub-questions", len(papers) == 183, "got %d" % len(papers))
check("19 class-test parts", len(cts) == 19, "got %d" % len(cts))

per = collections.defaultdict(int)
for r in papers:
    per[r["year"]] += int(r["marks_part"])
expect = {"2017": 96, "2018": 96, "2019": 96, "2020": 96,
          "2021": 97, "2022": 80, "2023": 80, "2024": 80}
check("per-paper marks 96 96 96 96 97 80 80 80", dict(per) == expect, str(dict(sorted(per.items()))))
check("721 paper marks", sum(per.values()) == 721, "got %d" % sum(per.values()))

ids = collections.Counter(r["unit_id"] for r in rows)
dupes = [k for k, v in ids.items() if v > 1]
check("every unit id unique", not dupes, ", ".join(dupes[:5]))

self_ref = [r["unit_id"] for r in rows if r["subtopic"] in r["also_subtopics"].split()]
check("no unit cross-files against itself", not self_ref, ", ".join(self_ref[:5]))

blank = [r["unit_id"] for r in rows if not r["subtopic"] or not r["question_text"]]
check("every row has a subtopic and question text", not blank, ", ".join(blank[:5]))

# Class-test parts must never carry an invented per-part mark.
bad_ct = [r["unit_id"] for r in cts if r["marks_part"]]
check("no class-test part carries a per-part mark", not bad_ct, ", ".join(bad_ct[:5]))

listed = {l.split("_")[0] for l in open("scripts/filelist.txt", encoding="utf-8") if l.strip()}
# Written by build_manifest.py from the entry lines themselves, not from the
# manifest's primary-filing column. Ten units are printed a second time in
# another subtopic's block, so NM-3.8, NM-5.6, NM-5.7 and NM-10.4 hold entry
# lines while never being the primary filing. Reading only the primary column
# would call those four fileless and fail the gate spuriously.
used = {l.strip() for l in open("scripts/subtopics_with_file.txt", encoding="utf-8") if l.strip()}
check("84 subtopics carry a file", len(listed) == 84, "got %d" % len(listed))
check("filelist matches the entry-line subtopic set", used == listed,
      "manifest-only %s / filelist-only %s" % (
          sorted(used - listed)[:5], sorted(listed - used)[:5]))

empty = [l for l in open("scripts/filelist_no_file.txt", encoding="utf-8") if l.strip()]
check("21 subtopics carry no file", len(empty) == 21, "got %d" % len(empty))
check("file list and no-file list partition the taxonomy",
      len(listed) + len(empty) == 105, "got %d" % (len(listed) + len(empty)))

sys.exit(1 if fail else 0)
PY
rc=$?

echo
if [ "$rc" -eq 0 ]; then
  echo "V2 GREEN"
else
  echo "V2 RED"
fi
exit "$rc"