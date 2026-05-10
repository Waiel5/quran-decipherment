#!/usr/bin/env python3
"""H-NEW-1780 — ṣaḥīḥayn vs Sunan hadith-grade distribution across project surahs.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-1780-hadith-grade-distribution.md
SHA-locked. Descriptive ratio computation; no permutation null. Direction-locked:
%sunan-grade ≥ 30% predicts CONFIRMED.
"""

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1780-hadith-grade-distribution.md"
EXPECTED_SHA = "2c93112e6bcf275f348566d0be65cc76b07369ef82ab46c17fe11832e69a78bf"
SURAH_DIR = ROOT / "surahs"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1780.json"
DIRECTION_THRESHOLD = 0.30  # %sunan-grade ≥ 30% predicts CONFIRMED

# Collection classification per pre-reg
SAHIHAYN = {"bukhari", "muslim"}
SUNAN4 = {"tirmidhi", "abu-dawud", "abudawud", "nasai", "ibn-majah", "ibnmajah"}
OTHER_SUNAN = {"malik", "muwatta", "ahmad", "musnad-ahmad", "darimi",
               "bayhaqi", "ibn-hibban", "ibnhibban", "hakim", "mustadrak",
               "ibn-abi-shayba", "ibnabishayba", "musannaf"}

# Citation-extraction regexes
# Patterns target the project's per-surah hadith-corpus citation conventions:
#   "al-Bukhārī #4811", "Bukhārī ḥadīth #5013", "Bukhari 4802", "Bukhari, hadith 1521"
#   "Muslim #1716", "Muslim ḥadīth #942", "Ṣaḥīḥ Muslim #3010"
#   "al-Tirmidhī #2878", "Tirmidhi #578", "al-Tirmidhī *Sunan* #578", "Tirmidhi 3171"
#   "Abū Dāwūd #1402", "Abu Dawud #1402"
#   "al-Nasāʾī K11332", "Nasāʾī #11332"
#   "Ibn Mājah #1057"
#   "Mālik *Muwaṭṭaʾ* #16"
#   "Aḥmad Musnad I.216", "Imām Aḥmad, *Musnad*", "Musnad Aḥmad"
#   "al-Dārimī" (often without number)
#   "al-Bayhaqī *Sunan al-Kubrā*"
#   "Ibn Ḥibbān *Ṣaḥīḥ*"
#   "al-Ḥākim *Mustadrak* I.221"
#   "Ibn Abī Shayba *Muṣannaf* II.13"

# Build collection-detection patterns.  Each pattern returns the collection key.
# Patterns are deliberately conservative: we want the COLLECTION NAME itself,
# not a work-title fragment like "Sunan al-Kubrā" that could refer to either
# Nasāʾī or Bayhaqī.
COLLECTION_PATTERNS = [
    # ṣaḥīḥayn
    (re.compile(r"Bukhārī|Bukhari|al-Bukhārī|al-Bukhari", re.I), "bukhari"),
    (re.compile(r"\bMuslim\b|Sahih Muslim|Ṣaḥīḥ Muslim", re.I), "muslim"),
    # Sunan-4
    (re.compile(r"Tirmidhī|Tirmidhi|al-Tirmidhī|al-Tirmidhi", re.I), "tirmidhi"),
    (re.compile(r"Abū Dāwūd|Abu Dawud|Abū Dawūd|Abū Dāwud", re.I), "abu-dawud"),
    (re.compile(r"Nasāʾī|Nasai|al-Nasāʾī|al-Nasai", re.I), "nasai"),
    (re.compile(r"Ibn Mājah|Ibn Majah", re.I), "ibn-majah"),
    # Other-Sunan
    (re.compile(r"Mālik|\bMalik\b|Muwaṭṭaʾ|Muwaṭṭāʾ|Muwatta|Muwattā", re.I), "malik"),
    (re.compile(r"Aḥmad|\bAhmad\b", re.I), "ahmad"),
    (re.compile(r"Dārimī|Darimi|al-Dārimī|al-Darimi", re.I), "darimi"),
    (re.compile(r"Bayhaqī|Bayhaqi|al-Bayhaqī|al-Bayhaqi", re.I), "bayhaqi"),
    (re.compile(r"Ibn Ḥibbān|Ibn Hibban", re.I), "ibn-hibban"),
    (re.compile(r"Ḥākim|Hakim|al-Ḥākim|al-Hakim|Mustadrak", re.I), "hakim"),
    (re.compile(r"Ibn Abī Shayba|Ibn Abi Shayba|Muṣannaf|Musannaf", re.I), "ibn-abi-shayba"),
]

# After identifying a collection, look for a ḥadīth-number nearby.  This regex finds
# any of: "#1402", "ḥadīth #1402", "hadith 1402", "id 1402", "idInBook 1402", "I.216", "II.13"
HADITH_NUM = re.compile(
    r"(?:#|ḥadīth\s*#?|hadith\s*#?|id(?:InBook)?\s*|nḥadīth\s*)?(\d{1,5})"
)


def classify(coll_key):
    if coll_key in SAHIHAYN:
        return "sahihayn"
    if coll_key in SUNAN4:
        return "sunan4"
    if coll_key in OTHER_SUNAN:
        return "other"
    return None


WINDOW_MAX = 80  # chars: window after collection mention to capture number


def extract_citations(text, surah_id):
    """Walk through text line by line and extract (collection, number) tuples.

    A citation requires:
      1. An explicit collection mention (e.g. "Bukhārī"), AND
      2. A hadith-number / idInBook / chapter-id / roman-numeral volume reference
         within WINDOW_MAX chars after the collection mention, AND
      3. No OTHER collection name appearing between the collection-mention and
         the number (i.e. the number must be unambiguously attributable to the
         nearest preceding collection).

    Vague references (e.g. "al-Bukhārī silent on Q 22") are excluded.
    """
    cites = []
    lines = text.splitlines()
    for ln_idx, line in enumerate(lines):
        # First, detect all collections mentioned in this line.
        detected = []
        for pat, key in COLLECTION_PATTERNS:
            for m in pat.finditer(line):
                detected.append((m.start(), m.end(), key))
        if not detected:
            continue
        # Sort by start position.
        detected.sort()
        # For each detection, try to find a ḥadīth-number within WINDOW_MAX chars
        # after the end of the collection name, BEFORE any next collection mention.
        for i, (start, end, key) in enumerate(detected):
            # Determine the search-window end: min(end + WINDOW_MAX, next_collection_start).
            next_coll_start = detected[i + 1][0] if i + 1 < len(detected) else len(line)
            window_end = min(end + WINDOW_MAX, next_coll_start)
            window = line[end: window_end]

            # Look for a hadith-number indicator and digit-string.
            # Strong indicators: #, ḥadīth #, hadith #, idInBook, global #
            # Weak: "id N", "chapter id N" — these are ambiguous; we accept them
            # because they often anchor real claims (e.g. "Kitāb Sujūd al-Qurʾān = chapter id 17").
            num_match = re.search(
                r"(?:#|ḥadīth\s*#?|hadith\s*#?|idInBook\s*|global\s*#|chapter\s*id\s*)\s*(\d{1,6})",
                window,
                re.I,
            )
            roman_match = re.search(
                r"\b([IVX]{1,4}\.\d{1,4})\b",
                window,
            )
            if num_match:
                cites.append({
                    "surah": surah_id,
                    "collection": key,
                    "grade": classify(key),
                    "identifier": num_match.group(1),
                    "id_type": "number",
                    "line": ln_idx + 1,
                })
            elif roman_match:
                cites.append({
                    "surah": surah_id,
                    "collection": key,
                    "grade": classify(key),
                    "identifier": roman_match.group(1),
                    "id_type": "roman",
                    "line": ln_idx + 1,
                })
            # Otherwise: this is a vague reference. Drop it per pre-reg.
    return cites


def dedupe(cites):
    """Per pre-reg: de-duplicate by (surah, collection, identifier).

    Multiple citations of the same ḥadīth across topical sections of one surah file
    count as one instance per file.
    """
    seen = set()
    out = []
    for c in cites:
        key = (c["surah"], c["collection"], c["identifier"])
        if key in seen:
            continue
        seen.add(key)
        out.append(c)
    return out


def main():
    actual_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual_sha != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: expected {EXPECTED_SHA}, got {actual_sha}")
    print(f"SHA verified: {EXPECTED_SHA}")

    # Find all hadith-corpus files
    files = sorted(SURAH_DIR.glob("Q*/04-hadith-corpus.md"))
    print(f"Found {len(files)} per-surah hadith-corpus files")

    all_cites = []
    per_surah_counts = {}
    for f in files:
        # Extract surah id from filename
        sid_match = re.search(r"Q(\d{3})", str(f))
        if not sid_match:
            continue
        sid = int(sid_match.group(1))
        text = f.read_text()
        raw = extract_citations(text, sid)
        # de-dupe within a surah
        deduped = dedupe(raw)
        per_surah_counts[sid] = {
            "raw_hits": len(raw),
            "deduped": len(deduped),
        }
        all_cites.extend(deduped)

    # Tally
    n_total = len(all_cites)
    by_grade = defaultdict(int)
    by_collection = defaultdict(int)
    for c in all_cites:
        by_grade[c["grade"]] += 1
        by_collection[c["collection"]] += 1

    n_sahihayn = by_grade["sahihayn"]
    n_sunan4 = by_grade["sunan4"]
    n_other = by_grade["other"]
    n_unclassified = by_grade[None]

    # Ratios (against classified-total, not n_total — unclassified would only be a
    # bug; we did not expect any with the locked classification scheme)
    n_classified = n_sahihayn + n_sunan4 + n_other
    pct_sahihayn = n_sahihayn / n_classified if n_classified else 0.0
    pct_sunan4 = n_sunan4 / n_classified if n_classified else 0.0
    pct_other = n_other / n_classified if n_classified else 0.0
    pct_sunan_grade = (n_sunan4 + n_other) / n_classified if n_classified else 0.0

    # Per-surah grade breakdown
    per_surah_grades = {}
    for c in all_cites:
        sid = c["surah"]
        if sid not in per_surah_grades:
            per_surah_grades[sid] = {"sahihayn": 0, "sunan4": 0, "other": 0}
        if c["grade"] in per_surah_grades[sid]:
            per_surah_grades[sid][c["grade"]] += 1

    # Direction check
    direction_met = pct_sunan_grade >= DIRECTION_THRESHOLD
    verdict = "DESCRIPTIVE-CONFIRMED" if direction_met else "DESCRIPTIVE-NULL"

    # Top-cited collections by individual book
    coll_counts_sorted = sorted(by_collection.items(), key=lambda x: -x[1])

    # Per-collection breakdown
    col_table = []
    for coll, count in coll_counts_sorted:
        col_table.append({
            "collection": coll,
            "count": count,
            "grade": classify(coll),
            "pct_of_classified": count / n_classified if n_classified else 0.0,
        })

    result = {
        "id": "H-NEW-1780",
        "title": "ṣaḥīḥayn vs Sunan hadith-grade distribution",
        "prereg_sha256": EXPECTED_SHA,
        "n_surah_files_audited": len(files),
        "n_citation_instances_total": n_total,
        "n_citation_instances_classified": n_classified,
        "n_unclassified": n_unclassified,
        "by_grade": {
            "sahihayn": n_sahihayn,
            "sunan4": n_sunan4,
            "other": n_other,
        },
        "pct_by_grade": {
            "sahihayn": pct_sahihayn,
            "sunan4": pct_sunan4,
            "other": pct_other,
            "sunan_grade_combined": pct_sunan_grade,
        },
        "direction_threshold": DIRECTION_THRESHOLD,
        "direction_met": direction_met,
        "verdict": verdict,
        "by_collection": col_table,
        "per_surah_grades": per_surah_grades,
        "per_surah_raw_vs_deduped": per_surah_counts,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False))

    # Print summary
    print()
    print(f"Total surah-files audited: {len(files)}")
    print(f"Total citation-instances (deduped per surah): {n_total}")
    print(f"  ṣaḥīḥayn: {n_sahihayn}  ({100 * pct_sahihayn:.2f}%)")
    print(f"  Sunan-4 : {n_sunan4}  ({100 * pct_sunan4:.2f}%)")
    print(f"  Other   : {n_other}  ({100 * pct_other:.2f}%)")
    print(f"  Sunan-grade combined: {n_sunan4 + n_other}  ({100 * pct_sunan_grade:.2f}%)")
    print(f"Direction threshold: ≥ {100 * DIRECTION_THRESHOLD:.0f}% sunan-grade — {'MET' if direction_met else 'NOT MET'}")
    print(f"Verdict: {verdict}")
    print()
    print("Top collections:")
    for r in col_table[:15]:
        print(f"  {r['collection']:<18} count={r['count']:<4} grade={r['grade']:<10} {100*r['pct_of_classified']:.2f}%")


if __name__ == "__main__":
    main()
