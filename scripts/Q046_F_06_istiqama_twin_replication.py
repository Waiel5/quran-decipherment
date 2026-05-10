#!/usr/bin/env python3
"""
Q046-F-06 — *istiqāma* twin replication of Q041-F-01 from Q 46 direction.
Pre-reg SHA256: 9b8684fb24fe3ba48aee2cdcecd946797a9c754e9c3cfd4e6512c79818679e07
Seed: 20260509.
"""
import hashlib
import json
import os
import sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/preregs/Q046-F-06-istiqama-twin-replication-prereg.md"
EXPECTED_SHA = "9b8684fb24fe3ba48aee2cdcecd946797a9c754e9c3cfd4e6512c79818679e07"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/csv/Q046-F-06.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
    print(f"[OK] Pre-reg SHA verified.")

def main():
    verify()
    quran = json.load(open(QURAN))
    target = "قالوا ربنا الله ثم استقاموا"
    hits = []
    for s in quran:
        sid = s["id"]
        for v in s["verses"]:
            if target in v["text"]:
                hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})
    observed = [(h["surah"], h["verse"]) for h in hits]
    expected = [(41, 30), (46, 13)]
    if sorted(observed) == sorted(expected):
        verdict = "VINDICATED — replicates Q041-F-01 from Q 46 direction"
        replicates = True
    else:
        verdict = "NULL_OR_DISCREPANCY"
        replicates = False
    out = {
        "prereg_id": "Q046-F-06",
        "prereg_sha": EXPECTED_SHA,
        "search_string": target,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "n_attestations": len(hits),
        "attestations": hits,
        "expected_pattern": expected,
        "observed_pattern": observed,
        "replicates_Q041_F_01": replicates,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
