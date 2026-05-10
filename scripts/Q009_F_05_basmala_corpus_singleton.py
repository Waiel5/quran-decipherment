#!/usr/bin/env python3
"""
Q009-F-05 — Basmala corpus-singleton verification.

Direction-LOCKED before observation. Pre-reg SHA verified at runtime.

Pre-registered:
  T1a: 113 surahs have basmala canonical opener; T1b: Q 9 is the unique exception.
  T1c: 1 internal basmala occurrence at Q 27:30.
  T1d: total basmala in printed corpus = 114.

Rules-tuple: Hafs-Kufan + orthographic + NFKD-strip for tashkeel-invariant matching.

Seed: 20260509 (no permutation needed; deterministic count).
"""

import hashlib
import json
import os
import re
import sys
import unicodedata

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q009-al-tawba/Q009-F-05-basmala-corpus-singleton-prereg.md"
EXPECTED_SHA = "e3beb6605cd44a6883e01be279a701f9fc1fa08dac6f9e78d4984488220050a7"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q009-al-tawba/csv/Q009-F-05-basmala-corpus-singleton.json"


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH\n  expected: {EXPECTED_SHA}\n  actual:   {actual}\n"
        )
        sys.exit(2)


def strip_diacritics(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def main():
    verify_prereg()

    # --- corpus-1: stored JSON (Hafs verse-numbering) ---
    with open("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json") as f:
        quran = json.load(f)

    # Pattern after NFKD strip: bism allh al-rHmn al-rHym
    bas_pat = re.compile(r"بسم\s*ا?ل?له\s*الرحم[نٰ]\s*الرحيم")

    v1_basmala = []
    v1_not_basmala = []
    internal_hits = []
    for s in quran:
        sid = s["id"]
        v1 = strip_diacritics(s["verses"][0]["text"]).strip()
        if bas_pat.search(v1):
            v1_basmala.append(sid)
        else:
            v1_not_basmala.append(sid)
        for v in s["verses"][1:]:
            txt = strip_diacritics(v["text"])
            if bas_pat.search(txt):
                internal_hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})

    # --- corpus-2: printed convention (simple-txt) ---
    with open("/Users/grey/Downloads/quran/data/alt-text/quran-simple-txt.txt") as f:
        printed = f.read()
    printed_stripped = strip_diacritics(printed)
    printed_count = len(bas_pat.findall(printed_stripped))

    # --- Verdict ---
    stored_ok = (
        v1_basmala == [1]
        and v1_not_basmala == [s["id"] for s in quran if s["id"] != 1]
        and len(internal_hits) == 1
        and internal_hits[0]["surah"] == 27
        and internal_hits[0]["verse"] == 30
    )
    printed_ok = printed_count == 114
    q9_in_not = 9 in v1_not_basmala

    verdict = "VINDICATED-CORPUS-EXACT" if (stored_ok and printed_ok and q9_in_not) else "FALSIFIED"

    result = {
        "finding_id": "Q009-F-05",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260509,
        "rules_tuple": "Hafs-Kufan, no-tashkeel + NFKD-strip, orthographic-tokens",
        "stored_json": {
            "n_v1_basmala": len(v1_basmala),
            "v1_basmala_surahs": v1_basmala,
            "n_v1_not_basmala": len(v1_not_basmala),
            "q9_in_not_basmala": q9_in_not,
            "internal_basmala_hits": internal_hits,
        },
        "printed_corpus": {
            "file": "data/alt-text/quran-simple-txt.txt",
            "total_basmala_count": printed_count,
            "expected": 114,
        },
        "pre_registered_thresholds": {
            "expected_v1_basmala_count": 1,
            "expected_v1_not_basmala_count": 113,
            "expected_internal": 1,
            "expected_internal_locus": "Q27:30",
            "expected_printed_total": 114,
        },
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(json.dumps({k: result[k] for k in ("finding_id", "verdict", "stored_json", "printed_corpus")}, indent=2, ensure_ascii=False))
    print(f"\nResult written to {OUT_PATH}")


if __name__ == "__main__":
    main()
