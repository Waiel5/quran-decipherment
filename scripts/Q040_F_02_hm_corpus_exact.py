#!/usr/bin/env python3
"""Q040-F-02 — HM corpus-EXACT 7-surah identity verification."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q040-ghafir/preregs/Q040-F-02-hm-corpus-exact-prereg.md"
EXPECTED_SHA = "2932348c71e35d72103fc8ffe12ac0dafecaa70cf303e450801952a1d65b5b45"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "surahs/Q040-ghafir/csv/Q040-F-02.json"
EXPECTED_HM = {40, 41, 42, 43, 44, 45, 46}


def main():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: {actual}")

    text = json.loads(QURAN.read_text())
    hm_set = []
    first_verses = {}
    for e in text:
        s = int(e["id"])
        v1 = e["verses"][0]["text"].strip()
        first_verses[s] = v1
        if v1 == "حم":
            hm_set.append(s)

    hm_set_s = set(hm_set)
    match_exact = hm_set_s == EXPECTED_HM

    if match_exact:
        verdict = "VINDICATED (corpus-EXACT HM=Q40-46)"
    elif hm_set_s.issubset(EXPECTED_HM):
        verdict = "RULES-TUPLE-FRAGILE (subset)"
    else:
        verdict = "DEFINITIONAL ANOMALY"

    out = {
        "id": "Q040-F-02",
        "title": "HM-opener corpus-EXACT 7-surah identity",
        "prereg_sha": EXPECTED_SHA,
        "hm_set_found": sorted(hm_set),
        "hm_set_expected": sorted(EXPECTED_HM),
        "match_exact": match_exact,
        "first_verses_hm_block": {s: first_verses[s] for s in sorted(EXPECTED_HM)},
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Q040-F-02: {verdict}")
    print(f"  HM-opener surahs: {sorted(hm_set)}")


if __name__ == "__main__":
    main()
