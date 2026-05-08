#!/usr/bin/env python3
"""Q044-F-01: dukhān-bracket lexical hapax-pair test.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q044-al-dukhan/preregs/Q044-F-01-dukhan-bracket-prereg.md
Pre-reg SHA256 (locked): 8efd2b13c3c2714e11ec8c856b80647f89df649bbbcc2cd5c042e0b033bc30b8
"""

import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/preregs/Q044-F-01-dukhan-bracket-prereg.md"
PREREG_SHA_EXPECTED = "8efd2b13c3c2714e11ec8c856b80647f89df649bbbcc2cd5c042e0b033bc30b8"

OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-01.json"
QURAN_NO_TASHKEEL = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
QURAN_MIN_TASHKEEL = "/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def find_dukhan(json_path, target="دخان"):
    data = json.load(open(json_path))
    hits = []
    for s in data:
        for v in s["verses"]:
            if target in v["text"]:
                hits.append({"surah": s["id"], "verse": v["id"], "text": v["text"]})
    return hits


def main():
    actual = sha256_of(PREREG_PATH)
    if actual != PREREG_SHA_EXPECTED:
        print(f"FAIL: pre-reg SHA mismatch.\n  expected: {PREREG_SHA_EXPECTED}\n  actual:   {actual}", file=sys.stderr)
        sys.exit(1)
    print(f"Pre-reg SHA verified: {actual}")

    # Primary run on no-tashkeel
    hits_nt = find_dukhan(QURAN_NO_TASHKEEL)
    print(f"\n=== no-tashkeel ===\n  {len(hits_nt)} verses contain `دخان`:")
    for h in hits_nt:
        print(f"    Q{h['surah']}:{h['verse']}: {h['text']}")

    # Replication on min-tashkeel
    hits_mt = find_dukhan(QURAN_MIN_TASHKEEL)
    print(f"\n=== min-tashkeel (replication) ===\n  {len(hits_mt)} verses contain `دخان`:")
    for h in hits_mt:
        print(f"    Q{h['surah']}:{h['verse']}: {h['text']}")

    # Verdict
    surahs_hit = sorted({h["surah"] for h in hits_nt})
    HM7 = {40, 41, 42, 43, 44, 45, 46}
    in_hm7 = all(s in HM7 for s in surahs_hit)
    count = len(hits_nt)
    if count == 2 and in_hm7 and set(surahs_hit) == {41, 44}:
        verdict = "VINDICATED"
    elif count == 2:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL / FALSIFIED"

    out = {
        "finding_id": "Q044-F-01",
        "title": "Q 41:11 + Q 44:10 are the corpus's only two attestations of the noun dukhān",
        "prereg_sha": actual,
        "prereg_sha_expected": PREREG_SHA_EXPECTED,
        "primary_run": {
            "tashkeel_level": "no-tashkeel",
            "source": QURAN_NO_TASHKEEL,
            "match_count": count,
            "hits": hits_nt,
            "surahs_hit": surahs_hit,
        },
        "replication_run": {
            "tashkeel_level": "min-tashkeel",
            "source": QURAN_MIN_TASHKEEL,
            "match_count": len(hits_mt),
            "hits": hits_mt,
        },
        "verdict": verdict,
        "in_HM7_only": in_hm7,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    json.dump(out, open(OUT_PATH, "w"), indent=2, ensure_ascii=False)
    print(f"\nVERDICT: {verdict}")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
