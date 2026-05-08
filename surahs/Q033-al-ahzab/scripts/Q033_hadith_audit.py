#!/usr/bin/env python3
"""
Q033 hadith citation audit (Claim #1, #5).

Per-collection scan of all 9 canonical books:
  - Bukhārī, Muslim, Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik (Muwaṭṭaʾ), Aḥmad, Dārimī

We count hadith records that explicitly cite Q 33 (or "al-Aḥzāb") and compare
to citation density of comparable surahs (Q 1, Q 2, Q 36, Q 55, Q 67, Q 112).

Two detection methods:
  A. Surah-name regex: الأحزاب
  B. Verse-quote regex: distinctive phrases unique to Q 33 (خاتم النبيين, ḥijāb verses,
     amāna verse, ṣalawāt verse).
"""

import json
import os
import re
import sys
from collections import defaultdict

BASE = "/Users/grey/Downloads/quran"
HADITH_DIR = os.path.join(BASE, "data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books")

BOOKS = {
    "bukhari": "bukhari.json",
    "muslim": "muslim.json",
    "tirmidhi": "tirmidhi.json",
    "abudawud": "abudawud.json",
    "nasai": "nasai.json",
    "ibnmajah": "ibnmajah.json",
    "malik": "malik.json",
    "ahmad": "ahmed.json",
    "darimi": "darimi.json",
}

# Surah-name-based detection (Arabic)
SURAH_NAMES = {
    1: r"الفاتحة|أم الكتاب|السبع المثاني|فاتحة الكتاب",
    2: r"البقرة",
    33: r"الأحزاب",
    36: r"يس|يٰس",
    55: r"الرحمن|الرحمٰن",
    67: r"الملك|تبارك",
    112: r"الإخلاص|قل هو الله أحد|قل هو اللَّه أحد",
}

# Distinctive phrases unique to Q 33
Q33_DISTINCTIVE_AR = [
    r"خاتم النبيين",      # Q 33:40
    r"الأحزاب",            # surah name
    r"يا أيها النبي اتق الله",  # Q 33:1 opening
    r"إن الله وملائكته يصلون",  # Q 33:56
    r"عرضنا الأمانة",      # Q 33:72
    r"ما جعل الله لرجل من قلبين",  # Q 33:4
]

def normalize(text):
    if not text:
        return ""
    # remove tashkeel + tatweel
    text = re.sub(r"[ً-ٰٟۖ-ۭـ]", "", text)
    return text


def scan_book(path):
    d = json.load(open(path, encoding="utf-8"))
    return d["hadiths"], d["metadata"]


def count_citations(hadiths, surah_pattern, distinctive_patterns=None):
    """Count hadiths matching surah_pattern in arabic text or any distinctive phrase."""
    n_name_only = 0
    n_distinctive = 0
    n_either = 0
    matched_ids = []
    for h in hadiths:
        ar = normalize(h.get("arabic", ""))
        match_name = bool(re.search(surah_pattern, ar)) if surah_pattern else False
        match_distinct = False
        if distinctive_patterns:
            for p in distinctive_patterns:
                if re.search(p, ar):
                    match_distinct = True
                    break
        if match_name:
            n_name_only += 1
        if match_distinct:
            n_distinctive += 1
        if match_name or match_distinct:
            n_either += 1
            matched_ids.append(h.get("idInBook"))
    return {
        "n_name_only": n_name_only,
        "n_distinctive": n_distinctive,
        "n_either": n_either,
        "matched_idInBook_first20": matched_ids[:20],
    }


def main():
    out = {}
    for book_key, fname in BOOKS.items():
        path = os.path.join(HADITH_DIR, fname)
        try:
            hadiths, meta = scan_book(path)
        except Exception as e:
            out[book_key] = {"error": str(e)}
            continue
        n_total = len(hadiths)
        per_surah = {}
        for sid in [1, 2, 33, 36, 55, 67, 112]:
            distinct = Q33_DISTINCTIVE_AR if sid == 33 else None
            per_surah[sid] = count_citations(hadiths, SURAH_NAMES[sid], distinct)
            per_surah[sid]["density_per_1000"] = per_surah[sid]["n_either"] / n_total * 1000
        out[book_key] = {
            "n_total_hadiths": n_total,
            "per_surah": per_surah,
        }
    return out


if __name__ == "__main__":
    out = main()
    json.dump(out, open(os.path.join(BASE, "surahs/Q033-al-ahzab/csv/Q033-hadith-audit.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    # human-readable summary
    print(f"{'Book':<10} {'Total':>6}  Q33-name  Q33-distinct  Q33-either  Q1  Q2  Q36  Q55  Q67  Q112")
    for book_key, data in out.items():
        if "error" in data:
            print(f"{book_key:<10} ERROR: {data['error']}")
            continue
        ps = data["per_surah"]
        print(f"{book_key:<10} {data['n_total_hadiths']:>6}  {ps[33]['n_name_only']:>8}  {ps[33]['n_distinctive']:>12}  {ps[33]['n_either']:>10}  {ps[1]['n_either']:>2}  {ps[2]['n_either']:>2}  {ps[36]['n_either']:>3}  {ps[55]['n_either']:>3}  {ps[67]['n_either']:>3}  {ps[112]['n_either']:>4}")

    # Total Q33 vs Q2 vs Q36 etc across all 9 collections
    totals = defaultdict(int)
    n_total_all = 0
    for book_key, data in out.items():
        if "error" in data:
            continue
        n_total_all += data["n_total_hadiths"]
        for sid, ps in data["per_surah"].items():
            totals[sid] += ps["n_either"]
    print()
    print(f"TOTAL across 9 books (n={n_total_all} hadiths):")
    for sid in [1, 2, 33, 36, 55, 67, 112]:
        print(f"  Q{sid}: {totals[sid]} citations  (density={totals[sid]/n_total_all*1000:.2f}/1000)")
