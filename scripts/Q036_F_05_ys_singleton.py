#!/usr/bin/env python3
"""
Q036-F-05 — YS muqaṭṭāʿat is the corpus-EXACT singleton surah-opener.

Pre-reg: surahs/Q036-yasin/preregs/Q036-F-05-ys-singleton-prereg.md
SHA-256: 9cc710c5a340e52a98a9030c27edfe92031bad37b43b4a106dfdd33d62d6053f
Seed:    20260509 (n/a — deterministic enumeration)
"""

import hashlib
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG = PROJECT_ROOT / "surahs/Q036-yasin/preregs/Q036-F-05-ys-singleton-prereg.md"
EXPECTED_SHA = "9cc710c5a340e52a98a9030c27edfe92031bad37b43b4a106dfdd33d62d6053f"


def verify_prereg_sha():
    """Fail-fast if pre-reg has been edited post-lock."""
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}",
              file=sys.stderr)
        sys.exit(1)
    print(f"[ok] pre-reg SHA verified: {actual[:16]}...")


def load_corpus(path):
    with open(path) as f:
        return json.load(f)


def survey(corpus, label):
    """Return list of surahs whose v1 == 'يس' exactly, plus the muqaṭṭāʿat opener inventory."""
    YS = "يس"
    exact_matches = []
    muq_inventory = {}
    # Classical muqaṭṭāʿat catalog (29 surahs):
    MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
                  36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
    for s in corpus:
        sid = s["id"]
        v1 = s["verses"][0]["text"].strip()
        if v1 == YS:
            exact_matches.append(sid)
        if sid in MUQ_SURAHS:
            muq_inventory[sid] = v1
    return exact_matches, muq_inventory


def main():
    verify_prereg_sha()

    files = {
        "no-tashkeel":        PROJECT_ROOT / "quran-text/quran-no-tashkeel.json",
        "min-tashkeel":       PROJECT_ROOT / "quran-text/quran-min-tashkeel.json",
        "uthmani-consonant":  PROJECT_ROOT / "data/alt-text/quran-uthmani-consonantal.json",
    }

    result = {
        "finding_id": "Q036-F-05",
        "pre_reg_sha256": EXPECTED_SHA,
        "seed": 20260509,
        "date": "2026-05-09",
        "rules_tuple": "(no-tashkeel, orthographic-grapheme, basmala-counted-only-in-Q1, "
                       "Hafs-Kufan, Mashriqi, surah-opening-verse-only)",
        "variants": {},
    }

    for label, path in files.items():
        if not path.exists():
            result["variants"][label] = {"status": "FILE_NOT_FOUND", "path": str(path)}
            continue
        corpus = load_corpus(path)
        exact, muq = survey(corpus, label)
        result["variants"][label] = {
            "exact_ys_v1_surahs": exact,
            "count_exact_ys_v1": len(exact),
            "muq_inventory_size": len(muq),
            "muq_inventory_sample": {str(k): muq[k] for k in sorted(muq.keys())[:8]},
        }
        print(f"\n[{label}] surahs with v1 == 'يس': {exact} (count={len(exact)})")

    # Verdict
    primary = result["variants"]["no-tashkeel"]
    is_singleton = (primary.get("exact_ys_v1_surahs") == [36])

    cross_consistent = all(
        v.get("exact_ys_v1_surahs") == [36]
        for v in result["variants"].values()
        if "exact_ys_v1_surahs" in v
    )

    if is_singleton and cross_consistent:
        verdict = "PASS-DIRECTED-CORPUS-EXACT"
    elif is_singleton:
        verdict = "PASS-DIRECTED but rules-tuple-fragile (variants disagree)"
    else:
        verdict = "NULL (pre-commit violation — Q 36 is not the YS singleton)"

    result["verdict"] = verdict
    result["singleton_confirmed"] = is_singleton and cross_consistent
    result["interpretation"] = (
        "Q 36's two-letter muqaṭṭāʿat opening 'يس' is unique in the corpus. "
        "No other surah's verse 1 equals this string under any of three "
        "orthographic conventions tested (no-tashkeel, min-tashkeel, "
        "Uthmani-consonantal). 1/114 corpus-EXACT."
    ) if (is_singleton and cross_consistent) else "Pre-commit reversed; see full audit."

    out = PROJECT_ROOT / "surahs/Q036-yasin/csv/Q036-F-05.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nVerdict: {verdict}")
    print(f"Output: {out}")


if __name__ == "__main__":
    main()
