"""
Q041-F-01: *istiqāma* twin-verse uniqueness test.

Pre-reg SHA256: 3ba8abe8acd2ac04e9a3aa37755e1c33206d8c0553997904cb955646674964f6
Pre-reg path: surahs/Q041-fussilat/preregs/Q041-F-01-istiqama-twin-prereg.md
"""
import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q041-fussilat/preregs/Q041-F-01-istiqama-twin-prereg.md"
EXPECTED_SHA = "3ba8abe8acd2ac04e9a3aa37755e1c33206d8c0553997904cb955646674964f6"
QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q041-fussilat/csv/Q041-F-01.json"

def verify():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")

def main():
    verify()
    with open(QURAN_PATH) as f:
        quran = json.load(f)
    target = "قالوا ربنا الله ثم استقاموا"
    hits = []
    for surah in quran:
        sid = surah["id"]
        for v in surah["verses"]:
            if target in v["text"]:
                hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})

    expected_pattern = [(41, 30), (46, 13)]
    observed_pattern = [(h["surah"], h["verse"]) for h in hits]

    if observed_pattern == expected_pattern:
        verdict = "VINDICATED"
    else:
        verdict = "NULL_OR_DISCREPANCY"

    out = {
        "prereg_id": "Q041-F-01",
        "prereg_sha": EXPECTED_SHA,
        "search_string": target,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "n_attestations": len(hits),
        "attestations": hits,
        "expected_pattern": expected_pattern,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
