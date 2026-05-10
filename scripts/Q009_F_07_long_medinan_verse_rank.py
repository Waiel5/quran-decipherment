#!/usr/bin/env python3
"""
Q009-F-07 — Q 9 long-Medinan jurisprudential verse-length signature.

Direction-LOCKED: Q 9 rank by mean words/verse ≤ 10 of 114 ⇒ VINDICATED.

Seed: 20260509 (no permutation needed; deterministic ranking).
Rules-tuple: Hafs-Kufan, no-tashkeel, orthographic-words.
"""

import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q009-al-tawba/Q009-F-07-long-medinan-verse-rank-prereg.md"
EXPECTED_SHA = "c97f9d9d352acf0f83f873a125651ae9e55c59cd1cce3121bd9056e37512168f"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q009-al-tawba/csv/Q009-F-07-long-medinan-verse-rank.json"


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH\n  expected: {EXPECTED_SHA}\n  actual:   {actual}\n"
        )
        sys.exit(2)


def compute_wpv(json_path):
    with open(json_path) as f:
        quran = json.load(f)
    rows = []
    for s in quran:
        total = sum(len(v["text"].split()) for v in s["verses"])
        nv = len(s["verses"])
        rows.append({
            "surah": s["id"],
            "name_translit": s.get("transliteration", ""),
            "type": s.get("type", ""),
            "n_verses": nv,
            "n_words": total,
            "words_per_verse": total / nv,
        })
    rows.sort(key=lambda r: -r["words_per_verse"])
    for i, r in enumerate(rows):
        r["rank_desc"] = i + 1
    return rows


def main():
    verify_prereg()

    rows_no = compute_wpv("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json")
    rows_min = compute_wpv("/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json")
    rows_full = compute_wpv("/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json")

    q9_no = next(r for r in rows_no if r["surah"] == 9)
    q9_min = next(r for r in rows_min if r["surah"] == 9)
    q9_full = next(r for r in rows_full if r["surah"] == 9)

    threshold = 10
    primary_rank = q9_no["rank_desc"]

    if primary_rank <= threshold:
        verdict = "VINDICATED"
    elif primary_rank <= 30:
        verdict = "NULL-DIRECTIONAL"
    else:
        verdict = "FALSIFIED"

    # Top 15 for context
    top15 = [
        {k: r[k] for k in ("rank_desc", "surah", "name_translit", "type", "n_verses", "n_words", "words_per_verse")}
        for r in rows_no[:15]
    ]

    result = {
        "finding_id": "Q009-F-07",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260509,
        "rules_tuple_primary": "no-tashkeel + orthographic + Hafs-Kufan",
        "q9_primary_no_tashkeel": q9_no,
        "q9_replication_min_tashkeel": q9_min,
        "q9_replication_full_tashkeel": q9_full,
        "top15_by_words_per_verse": top15,
        "pre_registered_threshold": {
            "vindicated_if_rank": "<= 10",
            "null_directional_if_rank": "11-30",
            "falsified_if_rank": ">= 31",
        },
        "verdict": verdict,
        "rules_tuple_stability": {
            "rank_no_tashkeel": q9_no["rank_desc"],
            "rank_min_tashkeel": q9_min["rank_desc"],
            "rank_full_tashkeel": q9_full["rank_desc"],
            "stable": q9_no["rank_desc"] == q9_min["rank_desc"] == q9_full["rank_desc"],
        },
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(json.dumps({
        "finding_id": result["finding_id"],
        "verdict": result["verdict"],
        "q9_no_tashkeel": q9_no,
        "rules_tuple_stability": result["rules_tuple_stability"],
    }, indent=2, ensure_ascii=False))
    print(f"\nResult written to {OUT_PATH}")


if __name__ == "__main__":
    main()
