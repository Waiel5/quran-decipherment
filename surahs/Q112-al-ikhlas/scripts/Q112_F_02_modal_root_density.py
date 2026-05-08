#!/usr/bin/env python3
"""
Q112-F-02: Q 112 modal-root-density mechanism test.

Pre-reg SHA: 4d553d5a684cc28d934e37652b27a7f27732698a5ccff48019c3a91a3171d772
Pre-reg path: /Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/Q112-F-02-modal-root-density-prereg.md
"""

import hashlib, json, os, re, sys
from collections import Counter

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/Q112-F-02-modal-root-density-prereg.md"
PREREG_SHA_EXPECTED = "4d553d5a684cc28d934e37652b27a7f27732698a5ccff48019c3a91a3171d772"
MORPH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT = "/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/csv/Q112-F-02.json"

def verify_sha():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA_EXPECTED:
        print(f"FATAL: pre-reg SHA mismatch", file=sys.stderr); sys.exit(1)
    print(f"[OK] pre-reg SHA verified: {sha}")

def main():
    verify_sha()
    per_surah_roots = {s: [] for s in range(1, 115)}
    with open(MORPH) as f:
        for line in f:
            m = re.match(r'^\((\d+):(\d+):(\d+):(\d+)\)', line)
            if not m: continue
            s = int(m.group(1))
            rm = re.search(r'ROOT:(\w+)', line)
            if rm:
                per_surah_roots[s].append(rm.group(1))
    # corpus root frequency
    all_roots = []
    for s, rs in per_surah_roots.items():
        all_roots.extend(rs)
    corpus_freq = Counter(all_roots)
    sorted_roots = [r for r, _ in corpus_freq.most_common()]
    top20 = set(sorted_roots[:20])
    top50 = set(sorted_roots[:50])
    # per-surah fractions
    fractions_20 = {}
    fractions_50 = {}
    for s, rs in per_surah_roots.items():
        if not rs:
            fractions_20[s] = 0.0
            fractions_50[s] = 0.0
            continue
        fractions_20[s] = sum(1 for r in rs if r in top20) / len(rs)
        fractions_50[s] = sum(1 for r in rs if r in top50) / len(rs)
    # rank Q112
    sorted_20 = sorted(range(1,115), key=lambda s: -fractions_20[s])  # desc
    sorted_50 = sorted(range(1,115), key=lambda s: -fractions_50[s])
    rank20 = sorted_20.index(112) + 1
    rank50 = sorted_50.index(112) + 1
    corpus_mean_20 = sum(fractions_20.values()) / 114
    corpus_mean_50 = sum(fractions_50.values()) / 114
    # Build result
    result = {
        "preregistration_id": "Q112-F-02",
        "prereg_sha": PREREG_SHA_EXPECTED,
        "seed": 20260428,
        "Q112_n_root_tokens": len(per_surah_roots[112]),
        "Q112_root_tokens": per_surah_roots[112],
        "Q112_fraction_in_top20": fractions_20[112],
        "Q112_fraction_in_top50": fractions_50[112],
        "corpus_mean_fraction_in_top20": corpus_mean_20,
        "corpus_mean_fraction_in_top50": corpus_mean_50,
        "Q112_rank_top20_fraction": rank20,
        "Q112_rank_top50_fraction": rank50,
        "top_20_roots": sorted_roots[:20],
        "Q112_top20_roots_used": [r for r in per_surah_roots[112] if r in top20],
        "Q112_non_top20_roots": [r for r in per_surah_roots[112] if r not in top20],
        "verdict_pass_strict_top20": rank20 <= 11,
        "verdict_pass_loose_top20": rank20 <= 20,
        "verdict_pass_strict_top50": rank50 <= 11,
        "alpha_bon": 0.0125,
        "p_under_uniform_null_top20": rank20 / 114,
        "p_under_uniform_null_top50": rank50 / 114,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[OK] Q112 fraction_in_top20 = {fractions_20[112]:.4f}; corpus mean = {corpus_mean_20:.4f}")
    print(f"[OK] Q112 fraction_in_top50 = {fractions_50[112]:.4f}; corpus mean = {corpus_mean_50:.4f}")
    print(f"[OK] Q112 rank top20 = {rank20}/114 (strict <=11: {rank20<=11})")
    print(f"[OK] Q112 rank top50 = {rank50}/114")
    print(f"[OK] output -> {OUT}")

if __name__ == "__main__":
    main()
