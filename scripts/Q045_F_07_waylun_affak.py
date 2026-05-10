#!/usr/bin/env python3
"""
Q045-F-07 — *waylun li-kulli affāk* corpus-uniqueness at Q 45:7.
Pre-reg SHA256: bdd6f1c9de4ea1d673f9fb1534722b1ce095953f20e54ed23c2d3d89faf7b031
Seed: 20260509.
"""
import hashlib
import json
import os
import sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/preregs/Q045-F-07-waylun-affak-phrase-prereg.md"
EXPECTED_SHA = "bdd6f1c9de4ea1d673f9fb1534722b1ce095953f20e54ed23c2d3d89faf7b031"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/csv/Q045-F-07.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
    print(f"[OK] Pre-reg SHA verified.")

def search(quran, needle):
    hits = []
    for s in quran:
        sid = s["id"]
        for v in s["verses"]:
            if needle in v["text"]:
                hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})
    return hits

def main():
    verify()
    quran = json.load(open(QURAN))
    p1 = "ويل لكل أفاك"
    p2 = "أفاك أثيم"
    waylun_lakull = "ويل لكل"
    affak = "أفاك"
    hits_p1 = search(quran, p1)
    hits_p2 = search(quran, p2)
    hits_waylun = search(quran, waylun_lakull)
    hits_affak = search(quran, affak)
    p1_unique_q45_7 = (len(hits_p1) == 1 and (hits_p1[0]["surah"], hits_p1[0]["verse"]) == (45, 7))
    p2_unique_q45_7 = (len(hits_p2) == 1 and (hits_p2[0]["surah"], hits_p2[0]["verse"]) == (45, 7))
    if p1_unique_q45_7 and p2_unique_q45_7:
        verdict = "VINDICATED — both phrases corpus-singleton at Q 45:7"
    elif p1_unique_q45_7 or p2_unique_q45_7:
        verdict = "PARTIAL"
    else:
        verdict = "NULL_OR_DISCREPANCY"
    out = {
        "prereg_id": "Q045-F-07",
        "prereg_sha": EXPECTED_SHA,
        "primary_phrase": p1,
        "primary_hits": hits_p1,
        "primary_unique_q45_7": p1_unique_q45_7,
        "secondary_phrase": p2,
        "secondary_hits": hits_p2,
        "secondary_unique_q45_7": p2_unique_q45_7,
        "waylun_lakull_total_hits": len(hits_waylun),
        "waylun_lakull_loci": [(h["surah"], h["verse"]) for h in hits_waylun],
        "affak_total_hits": len(hits_affak),
        "affak_loci": [(h["surah"], h["verse"]) for h in hits_affak],
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
