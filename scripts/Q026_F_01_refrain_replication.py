#!/usr/bin/env python3
"""
Q026-F-01 brief-spec replication (T1): verify corpus-EXACT count = 8 and
exact verse positions for the closing-refrain pair (R1 + R2) in Q 26.

This is a re-run / replication of the F-01 finding under a fresh script
written for the 2026-05-09 brief. The original Q026_F_all.py established
the result; this script re-derives it independently for audit purposes.

Outputs JSON to surahs/Q026-al-shuara/csv/Q026-T1-refrain-replication.json
"""

import json
import os
import sys

BASE = "/Users/grey/Downloads/quran"
OUT = os.path.join(BASE, "surahs/Q026-al-shuara/csv/Q026-T1-refrain-replication.json")

# Refrain phrases (no-tashkeel)
R1 = "أكثرهم مؤمنين"  # 'most of them were not believers' fragment
R2 = "وإن ربك لهو العزيز الرحيم"  # closing chorus


def main():
    with open(os.path.join(BASE, "quran-text/quran-no-tashkeel.json"), encoding="utf-8") as f:
        corpus = json.load(f)

    r1_corpus = []  # list of (surah_id, verse_id)
    r2_corpus = []
    for surah in corpus:
        sid = surah["id"]
        for v in surah["verses"]:
            text = v["text"]
            if R1 in text:
                r1_corpus.append((sid, v["id"]))
            if R2 in text:
                r2_corpus.append((sid, v["id"]))

    r1_in_q26 = [vid for (sid, vid) in r1_corpus if sid == 26]
    r2_in_q26 = [vid for (sid, vid) in r2_corpus if sid == 26]
    r1_outside_q26 = [(sid, vid) for (sid, vid) in r1_corpus if sid != 26]
    r2_outside_q26 = [(sid, vid) for (sid, vid) in r2_corpus if sid != 26]

    result = {
        "test_id": "Q026-T1-refrain-replication",
        "R1_phrase": R1,
        "R2_phrase": R2,
        "R1_corpus_total": len(r1_corpus),
        "R2_corpus_total": len(r2_corpus),
        "R1_in_Q26_positions": r1_in_q26,
        "R2_in_Q26_positions": r2_in_q26,
        "R1_outside_Q26": r1_outside_q26,
        "R2_outside_Q26": r2_outside_q26,
        "R1_count_in_Q26": len(r1_in_q26),
        "R2_count_in_Q26": len(r2_in_q26),
        "corpus_exact_8": (len(r1_corpus) == 8 and len(r2_corpus) == 8
                          and len(r1_outside_q26) == 0 and len(r2_outside_q26) == 0),
        "expected_positions_R1": [8, 67, 103, 121, 139, 158, 174, 190],
        "expected_positions_R2": [9, 68, 104, 122, 140, 159, 175, 191],
        "positions_match_R1": (r1_in_q26 == [8, 67, 103, 121, 139, 158, 174, 190]),
        "positions_match_R2": (r2_in_q26 == [9, 68, 104, 122, 140, 159, 175, 191]),
        "verdict": None,
    }

    if (result["corpus_exact_8"]
        and result["positions_match_R1"]
        and result["positions_match_R2"]):
        result["verdict"] = "CONFIRMED-REPLICATION: R1+R2 paired refrain is corpus-EXACT 8/8 in Q 26, exact positions as predicted."
    else:
        result["verdict"] = "DEVIATION from F-01 replication; see fields."

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps({k: v for k, v in result.items()
                       if k not in ("R1_outside_Q26", "R2_outside_Q26")},
                      ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
