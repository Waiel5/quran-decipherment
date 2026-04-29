"""
Q045-F-01: Q 45:18 *sharīʿa* noun-singleton corpus uniqueness.

Pre-reg SHA256: b13a44a3444b921a8ada51b5f9e4267e3e0b71e5ead4140e687621f009802a88
Pre-reg path: surahs/Q045-al-jathiyah/preregs/Q045-F-01-shariah-singleton-prereg.md
Seed: 20260428
"""
import hashlib
import json
import os
import sys
import re

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/preregs/Q045-F-01-shariah-singleton-prereg.md"
EXPECTED_SHA = "b13a44a3444b921a8ada51b5f9e4267e3e0b71e5ead4140e687621f009802a88"
QAC_PATH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/csv/Q045-F-01.json"

QURAN_VARIANTS = {
    "no-tashkeel": "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json",
    "min-tashkeel": "/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json",
    "full-tashkeel": "/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json",
}

TARGET_NOUN_VARIANTS = {
    "no-tashkeel": "شريعة",
    "min-tashkeel": "شريعة",
    # full-tashkeel may have diacritics intra-word; we strip combining marks before search
    "full-tashkeel": "شريعة",
}

COMBINING_MARKS = re.compile(r"[ً-ٰٟۖ-ۭ]")


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")


def search_singleton(variant_path, needle):
    with open(variant_path) as f:
        qd = json.load(f)
    hits = []
    for surah in qd:
        for v in surah["verses"]:
            text = COMBINING_MARKS.sub("", v["text"])
            if needle in text:
                hits.append({
                    "surah": surah["id"],
                    "verse": v["id"],
                    "text": v["text"],
                })
    return hits


def root_family_inventory(variant_path):
    """All verses where substring 'شرع' appears under no-tashkeel."""
    with open(variant_path) as f:
        qd = json.load(f)
    family = []
    for surah in qd:
        for v in surah["verses"]:
            text = COMBINING_MARKS.sub("", v["text"])
            if "شرع" in text:
                family.append({
                    "surah": surah["id"],
                    "verse": v["id"],
                    "text": v["text"],
                })
    return family


def qac_root_audit():
    """Locate every QAC token whose ROOT == '$rE' (Buckwalter for ش-ر-ع)."""
    target = "$rE"
    out = []
    with open(QAC_PATH) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0]
            form = parts[1]
            tag = parts[2]
            features = parts[3]
            m = re.match(r"\((\d+):(\d+):(\d+):(\d+)\)", loc)
            if not m:
                continue
            surah, verse = int(m.group(1)), int(m.group(2))
            root_match = re.search(r"ROOT:([^|]+)", features)
            if root_match and root_match.group(1) == target:
                out.append({
                    "surah": surah,
                    "verse": verse,
                    "form": form,
                    "tag": tag,
                    "features": features,
                })
    return out


def main():
    verify_prereg()

    # Primary test: substring search across all 3 tashkeel variants
    rules_tuple_table = {}
    for variant, path in QURAN_VARIANTS.items():
        needle = TARGET_NOUN_VARIANTS[variant]
        hits = search_singleton(path, needle)
        rules_tuple_table[variant] = {
            "count": len(hits),
            "verses": [(h["surah"], h["verse"]) for h in hits],
        }

    # Use no-tashkeel as primary
    primary_hits = search_singleton(QURAN_VARIANTS["no-tashkeel"], TARGET_NOUN_VARIANTS["no-tashkeel"])

    # H1b: full root-family inventory
    family = root_family_inventory(QURAN_VARIANTS["no-tashkeel"])

    # QAC root-level audit for ش-ر-ع
    qac_root_hits = qac_root_audit()

    # Verdict
    expected = (45, 18)
    direction_ok = (len(primary_hits) == 1 and (primary_hits[0]["surah"], primary_hits[0]["verse"]) == expected)
    if direction_ok:
        verdict = "VINDICATED"
    elif len(primary_hits) == 1:
        verdict = "PRECOMMIT_VIOLATION"
    else:
        verdict = "NULL"

    out = {
        "prereg_id": "Q045-F-01",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260428,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "primary_test": {
            "needle": "شريعة",
            "hit_count": len(primary_hits),
            "hits": primary_hits,
            "verdict": verdict,
        },
        "rules_tuple_stability": rules_tuple_table,
        "root_family_inventory": {
            "needle_substring": "شرع",
            "hit_count": len(family),
            "hits": family,
        },
        "qac_root_audit": {
            "target_root_buckwalter": "$rE",
            "hit_count": len(qac_root_hits),
            "hits": qac_root_hits,
        },
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
