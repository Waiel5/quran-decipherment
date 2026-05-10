#!/usr/bin/env python3
"""
Q043-F-06 — *tabāraka alladhī* corpus 5-locus distribution map.
Pre-reg SHA256: 52407393b4f9373229dff0e00ac76d53e615307c8827a0bab14c913d29351e02
Seed: 20260509.
Direction: exact 5 attestations at exactly {Q 25:1, Q 25:10, Q 25:61, Q 43:85, Q 67:1}.
"""
import hashlib
import json
import os
import sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/preregs/Q043-F-06-tabaraka-alladhi-corpus-distribution-prereg.md"
EXPECTED_SHA = "52407393b4f9373229dff0e00ac76d53e615307c8827a0bab14c913d29351e02"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/csv/Q043-F-06.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
    print(f"[OK] Pre-reg SHA verified.")

def main():
    verify()
    quran = json.load(open(QURAN))
    target = "تبارك الذي"
    hits = []
    for s in quran:
        sid = s["id"]
        for v in s["verses"]:
            if target in v["text"]:
                hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})
    observed_loci = [(h["surah"], h["verse"]) for h in hits]
    expected_loci = [(25, 1), (25, 10), (25, 61), (43, 85), (67, 1)]
    if sorted(observed_loci) == sorted(expected_loci):
        verdict = "VINDICATED"
    else:
        verdict = "NULL_OR_DISCREPANCY"
    out = {
        "prereg_id": "Q043-F-06",
        "prereg_sha": EXPECTED_SHA,
        "search_string": target,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "n_attestations": len(hits),
        "expected_n": 5,
        "attestations": hits,
        "observed_loci": observed_loci,
        "expected_loci": expected_loci,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
