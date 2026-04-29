"""Q043-F-01: Q 43-Q 44 verbatim-identical first-two-verse opening uniqueness."""
import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/preregs/Q043-F-01-q43q44-twin-opening-prereg.md"
EXPECTED_SHA = "6d4d362785f083bd9ff5f1cee533afc0cfa30f55e198031ab3718d10eff331d2"
QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/csv/Q043-F-01.json"

def main():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha}")

    with open(QURAN_PATH) as f:
        quran = json.load(f)

    twin_pairs = []
    for i in range(len(quran) - 1):
        s_a = quran[i]
        s_b = quran[i + 1]
        if len(s_a["verses"]) < 2 or len(s_b["verses"]) < 2:
            continue
        a1 = s_a["verses"][0]["text"].strip()
        a2 = s_a["verses"][1]["text"].strip()
        b1 = s_b["verses"][0]["text"].strip()
        b2 = s_b["verses"][1]["text"].strip()
        if a1 == b1 and a2 == b2:
            twin_pairs.append({
                "pair": [s_a["id"], s_b["id"]],
                "v1": a1,
                "v2": a2,
            })

    expected = [[43, 44]]
    observed = [p["pair"] for p in twin_pairs]
    verdict = "VINDICATED" if observed == expected else "NULL_OR_DISCREPANCY"

    out = {
        "prereg_id": "Q043-F-01",
        "prereg_sha": EXPECTED_SHA,
        "n_adjacent_pairs_examined": 113,
        "twin_pairs": twin_pairs,
        "expected_pairs": expected,
        "observed_pairs": observed,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
