"""
Q045-F-02: hawan-as-god twin construction Q 25:43 ↔ Q 45:23 corpus-singleton-pair.

Pre-reg SHA256: 87889c09fa16dc303700fd47ed9af6886b2c67a8c9554328222afd40ba4d5717
Pre-reg path: surahs/Q045-al-jathiyah/preregs/Q045-F-02-hawan-as-god-twin-prereg.md
Seed: 20260428
"""
import hashlib
import json
import os
import sys
import re

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/preregs/Q045-F-02-hawan-as-god-twin-prereg.md"
EXPECTED_SHA = "87889c09fa16dc303700fd47ed9af6886b2c67a8c9554328222afd40ba4d5717"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/csv/Q045-F-02.json"

QURAN_VARIANTS = {
    "no-tashkeel": "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json",
    "min-tashkeel": "/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json",
}

NEEDLE = "اتخذ إلهه هواه"
PAUSE_MARK_RE = re.compile(r"[ۖۚ۞ۗ]")
COMBINING_MARKS = re.compile(r"[ً-ٰٟۖ-ۭ]")


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")


def find_construction(variant_path):
    with open(variant_path) as f:
        qd = json.load(f)
    hits = []
    for surah in qd:
        for v in surah["verses"]:
            text = COMBINING_MARKS.sub("", v["text"])
            if NEEDLE in text:
                hits.append({
                    "surah": surah["id"],
                    "verse": v["id"],
                    "text": v["text"],
                })
    return hits


def word_count(text):
    cleaned = PAUSE_MARK_RE.sub("", text).strip()
    cleaned = COMBINING_MARKS.sub("", cleaned)
    return len([w for w in cleaned.split() if w])


def main():
    verify_prereg()

    rules_tuple_table = {}
    primary_hits = None
    for variant, path in QURAN_VARIANTS.items():
        hits = find_construction(path)
        rules_tuple_table[variant] = {
            "count": len(hits),
            "verses": [(h["surah"], h["verse"]) for h in hits],
        }
        if variant == "no-tashkeel":
            primary_hits = hits

    expected_set = {(25, 43), (45, 23)}
    observed_set = {(h["surah"], h["verse"]) for h in primary_hits}

    h1_pass = (observed_set == expected_set and len(primary_hits) == 2)
    h1_violation = (len(primary_hits) == 2 and observed_set != expected_set)

    # H1b: word-count ratio
    q25_43 = next((h for h in primary_hits if h["surah"] == 25 and h["verse"] == 43), None)
    q45_23 = next((h for h in primary_hits if h["surah"] == 45 and h["verse"] == 23), None)
    if q25_43 and q45_23:
        wc_25 = word_count(q25_43["text"])
        wc_45 = word_count(q45_23["text"])
        ratio = wc_45 / wc_25 if wc_25 else None
        h1b_pass = ratio is not None and ratio > 1.7
    else:
        wc_25 = wc_45 = ratio = None
        h1b_pass = False

    if h1_pass and h1b_pass:
        verdict = "VINDICATED"
    elif h1_pass and not h1b_pass:
        verdict = "PARTIAL_VINDICATION_H1_ONLY"
    elif h1_violation:
        verdict = "PRECOMMIT_VIOLATION"
    else:
        verdict = "NULL"

    out = {
        "prereg_id": "Q045-F-02",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260428,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "needle": NEEDLE,
        "primary_hits": primary_hits,
        "rules_tuple_stability": rules_tuple_table,
        "H1_pass": h1_pass,
        "H1_violation": h1_violation,
        "Q25_43_word_count_no_tashkeel": wc_25,
        "Q45_23_word_count_no_tashkeel": wc_45,
        "expansion_word_ratio_45_to_25": round(ratio, 4) if ratio else None,
        "expansion_threshold": 1.7,
        "H1b_pass": h1b_pass,
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
