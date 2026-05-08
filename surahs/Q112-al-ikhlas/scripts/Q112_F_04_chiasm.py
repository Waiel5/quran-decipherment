#!/usr/bin/env python3
"""
Q112-F-04: Q 112 aḥad-bookend chiasm — rules-tuple-stable across 3 tashkeel variants.

Pre-reg SHA: 5eede724edc02c62dcc2299deae23fd0a5c8bd8daa4ad5850ffe12e383c28acf
"""

import hashlib, json, os, sys
import unicodedata

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/Q112-F-04-chiasm-prereg.md"
PREREG_SHA_EXPECTED = "5eede724edc02c62dcc2299deae23fd0a5c8bd8daa4ad5850ffe12e383c28acf"
OUT = "/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/csv/Q112-F-04.json"

VARIANTS = [
    ("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json", "no-tashkeel"),
    ("/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json", "min-tashkeel"),
    ("/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json", "full-tashkeel"),
]

def verify_sha():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA_EXPECTED:
        print(f"FATAL: SHA mismatch", file=sys.stderr); sys.exit(1)
    print(f"[OK] pre-reg SHA verified: {sha}")

def strip_diacritics(s):
    """Remove Arabic diacritics + tatweel + extended-Arabic combining marks across all 3 tashkeel variants."""
    # Strip combining marks (tashkeel) by Unicode category
    s = "".join(c for c in s if not unicodedata.combining(c))
    # Strip Arabic-specific tashkeel ranges and presentation-form marks not always categorized as combining
    # Common: 0x0610-0x061A, 0x064B-0x065F, 0x0670, 0x06D6-0x06ED
    keep = []
    for c in s:
        cp = ord(c)
        if (0x0610 <= cp <= 0x061A) or (0x064B <= cp <= 0x065F) or cp == 0x0670 or (0x06D6 <= cp <= 0x06ED) or cp == 0x0640:
            continue
        keep.append(c)
    s = "".join(keep)
    # Normalize alif variants: 0x0671 (alif wasla), 0x0622 (alif madda) -> 0x0627 (alif), 0x0623 (alif hamza above) -> alif
    s = s.replace("ٱ", "ا").replace("آ", "ا").replace("أ", "ا").replace("إ", "ا")
    return s

def main():
    verify_sha()
    per_variant = {}
    for path, label in VARIANTS:
        with open(path) as f:
            data = json.load(f)
        s = data[111]  # Q112
        verses = s["verses"]
        # last word of each verse
        last_words = []
        for v in verses:
            text = v["text"].strip()
            words = text.split()
            last_words.append(words[-1] if words else "")
        last_words_stripped = [strip_diacritics(w).strip() for w in last_words]
        per_variant[label] = {
            "raw": last_words,
            "stripped_diacritics": last_words_stripped,
        }
    # Cross-variant comparison
    no_tash = per_variant["no-tashkeel"]["stripped_diacritics"]
    # Check identity v1==v4
    v1_eq_v4 = no_tash[0] == no_tash[3]
    # Across all variants, do the diacritic-stripped tokens match?
    consistent = all(per_variant[v]["stripped_diacritics"] == no_tash for v in per_variant)
    # Final letters
    final_letters = [w[-1] if w else "" for w in no_tash]
    # All end in dāl?
    all_dal = all(c == "د" for c in final_letters)
    result = {
        "preregistration_id": "Q112-F-04",
        "prereg_sha": PREREG_SHA_EXPECTED,
        "per_variant": per_variant,
        "v1_v4_identical": v1_eq_v4,
        "v2_token": no_tash[1],
        "v3_token": no_tash[2],
        "final_letters": final_letters,
        "all_verses_end_in_dal": all_dal,
        "rules_tuple_stable_across_3_variants": consistent,
        "verdict": "VINDICATED-RULES-TUPLE-STABLE" if (v1_eq_v4 and all_dal and consistent) else "DIRECTIONAL" if (v1_eq_v4 and all_dal) else "NULL",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[OK] v1=v4 identical (no-tash): {v1_eq_v4}")
    print(f"[OK] v1 token: {no_tash[0]}; v4 token: {no_tash[3]}")
    print(f"[OK] All verses end in د: {all_dal}")
    print(f"[OK] Rules-tuple stable across 3 variants: {consistent}")
    print(f"[OK] verdict: {result['verdict']}")
    print(f"[OK] output -> {OUT}")

if __name__ == "__main__":
    main()
