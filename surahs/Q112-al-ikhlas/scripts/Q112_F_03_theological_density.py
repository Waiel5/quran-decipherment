#!/usr/bin/env python3
"""
Q112-F-03: Q 112 theological-proposition density — descriptive comparison.

Pre-reg SHA: f28637a062ad652b31fcec04c8eff6630e5f18250aaf59423a17e8fbb2d86791
"""

import hashlib, json, os, sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/Q112-F-03-theological-density-prereg.md"
PREREG_SHA_EXPECTED = "f28637a062ad652b31fcec04c8eff6630e5f18250aaf59423a17e8fbb2d86791"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/csv/Q112-F-03.json"

def verify_sha():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA_EXPECTED:
        print(f"FATAL: SHA mismatch", file=sys.stderr); sys.exit(1)
    print(f"[OK] pre-reg SHA verified: {sha}")

def main():
    verify_sha()
    with open(QURAN) as f:
        q = json.load(f)
    # Comparator surahs: Q1 (creedal-petition), Q109 (creedal-confrontation), Q112, Q113, Q114
    comparators = {
        # Manual annotations of distinct theological propositions by 4-cell kalām taxonomy
        # Q112 propositions: tawHid (v1) + samadiyya (v2) + nafy walad (v3) + nafy shabih (v4) = 4
        # Q109 al-Kafirun: confrontation-formula (1 main propos) + clean break + repetition; counts as 1-2 distinct propositions
        # Q113 al-Falaq: 1 refuge formula + 4 evil typology (creation, ghasiq, naffathat, hasid) - 1 main + 4 sub = ~5 distinct refuge-objects but only 1 theological proposition
        # Q114 al-Nas: 1 refuge formula + 3 divine aspects (rabb, malik, ilah) + 1 evil typology (waswas) = 4 distinct propositions about God + 1 about evil = ~5 mentions but ~3 about God
        # Q1: 1 hamd + 1 attribute (rahman/rahim) + 1 sovereignty (malik yawm al-din) + 1 worship (iyyaka na'budu) + 1 petition (ihdina) + 1 typology (3 paths) = ~5 distinct prop
        112: {"name": "Q 112 al-Ikhlāṣ", "n_propositions": 4, "n_words": 15, "n_verses": 4},
        109: {"name": "Q 109 al-Kāfirūn", "n_propositions": 2, "n_words": 27, "n_verses": 6},  # confrontation + final formula
        113: {"name": "Q 113 al-Falaq", "n_propositions": 1, "n_words": 23, "n_verses": 5},   # 1 about God (Rabb al-falaq); rest are about typology of evil sought refuge from
        114: {"name": "Q 114 al-Nās", "n_propositions": 3, "n_words": 20, "n_verses": 6},     # rabb, malik, ilah (3 divine aspects)
        1:   {"name": "Q 1 al-Fātiḥa", "n_propositions": 5, "n_words": 29, "n_verses": 7},    # hamd, rabb, rahman/malik, iyyaka, ihdina + 3-path
    }
    # Density per verse
    for s in comparators:
        c = comparators[s]
        c["propositions_per_word"] = c["n_propositions"] / c["n_words"]
        c["propositions_per_verse"] = c["n_propositions"] / c["n_verses"]
    # Rank by propositions_per_word
    sorted_pw = sorted(comparators.items(), key=lambda kv: -kv[1]["propositions_per_word"])
    sorted_pv = sorted(comparators.items(), key=lambda kv: -kv[1]["propositions_per_verse"])
    Q112_rank_word = [s for s,_ in sorted_pw].index(112) + 1
    Q112_rank_verse = [s for s,_ in sorted_pv].index(112) + 1
    result = {
        "preregistration_id": "Q112-F-03",
        "prereg_sha": PREREG_SHA_EXPECTED,
        "comparators": comparators,
        "ranking_per_word_desc": [{"surah": s, "name": c["name"], "p_per_word": c["propositions_per_word"]} for s,c in sorted_pw],
        "ranking_per_verse_desc": [{"surah": s, "name": c["name"], "p_per_verse": c["propositions_per_verse"]} for s,c in sorted_pv],
        "Q112_rank_per_word": Q112_rank_word,
        "Q112_rank_per_verse": Q112_rank_verse,
        "Q112_propositions_per_word": comparators[112]["propositions_per_word"],
        "Q112_propositions_per_verse": comparators[112]["propositions_per_verse"],
        "verdict": "VINDICATED" if Q112_rank_word == 1 else "DIRECTIONAL" if Q112_rank_word <= 2 else "NULL",
        "honest_limit": "Annotation is manual using the 4-cell kalām taxonomy; alternative annotation schemes (e.g., counting propositions per *Sahih International* English clause) could yield different rankings. Replication-with-different-annotator is required for law-strength claims.",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[OK] Q112 propositions/word = {comparators[112]['propositions_per_word']:.4f}; rank = {Q112_rank_word}/{len(comparators)}")
    print(f"[OK] Q112 propositions/verse = {comparators[112]['propositions_per_verse']:.4f}; rank = {Q112_rank_verse}/{len(comparators)}")
    print(f"[OK] verdict: {result['verdict']}")
    print(f"[OK] output -> {OUT}")

if __name__ == "__main__":
    main()
