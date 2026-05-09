#!/usr/bin/env python3
"""Q054-F-02 — Q 54 vs Q 26 prophet-cycle compression test.

Pre-reg: surahs/Q054-al-qamar/preregs/Q054-F-02-prophet-cycle-compression-prereg.md
SHA256:  b604bdb40233c539da7b0569ca14b732d6a18972b78e2e43cf4f404f1d8fc389
Seed:    20260509  | n_perm: 10000  | Bonferroni-2 α_bon = 0.025
"""
from __future__ import annotations
import hashlib
import json
import random
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/preregs/Q054-F-02-prophet-cycle-compression-prereg.md"
EXPECTED_SHA = "b604bdb40233c539da7b0569ca14b732d6a18972b78e2e43cf4f404f1d8fc389"
QURAN_PATH = PROJECT_ROOT / "quran-text/quran-no-tashkeel.json"
OUTPUT_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/csv/Q054-F-02.json"

SEED = 20260509
N_PERM = 10000


def verify_prereg() -> str:
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  observed: {sha}")
    return sha


def main() -> None:
    sha = verify_prereg()
    print(f"[Q054-F-02] pre-reg SHA verified: {sha[:16]}…")

    with open(QURAN_PATH) as f:
        corpus = json.load(f)

    q54 = corpus[53]
    q26 = corpus[25]
    verses_q54 = q54["verses"]
    verses_q26 = q26["verses"]

    pericopes_q54 = [
        ("Nūḥ", 9, 17),
        ("ʿĀd", 18, 22),
        ("Thamūd", 23, 32),
        ("Lūṭ", 33, 40),
        ("āl-Firʿawn", 41, 42),
    ]
    pericopes_q26 = [
        ("Mūsā", 10, 68),
        ("Ibrāhīm", 69, 104),
        ("Nūḥ", 105, 122),
        ("Hūd", 123, 140),
        ("Ṣāliḥ", 141, 159),
        ("Lūṭ", 160, 175),
        ("Shuʿayb", 176, 191),
    ]

    def get_pericope_stats(verses, pericopes):
        out = []
        for name, lo, hi in pericopes:
            n_v = hi - lo + 1
            n_w = sum(len(verses[i - 1]["text"].split()) for i in range(lo, hi + 1))
            out.append({"name": name, "lo": lo, "hi": hi, "verses": n_v, "words": n_w})
        return out

    q54_stats = get_pericope_stats(verses_q54, pericopes_q54)
    q26_stats = get_pericope_stats(verses_q26, pericopes_q26)
    mean_v_q54 = sum(p["verses"] for p in q54_stats) / len(q54_stats)
    mean_w_q54 = sum(p["words"] for p in q54_stats) / len(q54_stats)
    mean_v_q26 = sum(p["verses"] for p in q26_stats) / len(q26_stats)
    mean_w_q26 = sum(p["words"] for p in q26_stats) / len(q26_stats)
    ratio_v = mean_v_q26 / mean_v_q54
    ratio_w = mean_w_q26 / mean_w_q54
    h2a_pass = ratio_v >= 2.0
    h2b_pass = ratio_w >= 2.0

    print(f"  H2a verses: Q54 mean = {mean_v_q54:.2f}; Q26 mean = {mean_v_q26:.2f}; ratio = {ratio_v:.3f}; pass (≥2): {h2a_pass}")
    print(f"  H2b words:  Q54 mean = {mean_w_q54:.2f}; Q26 mean = {mean_w_q26:.2f}; ratio = {ratio_w:.3f}; pass (≥2): {h2b_pass}")

    # Permutation null: random partition of pericope-region into pericope-count contiguous blocks
    def partition_random(total_verses, n_blocks, rng):
        if n_blocks == 1:
            return [total_verses]
        # generate n_blocks-1 cut points in 1..total_verses-1
        cuts = sorted(rng.sample(range(1, total_verses), n_blocks - 1))
        sizes = [cuts[0]] + [cuts[i + 1] - cuts[i] for i in range(len(cuts) - 1)] + [total_verses - cuts[-1]]
        return sizes

    # Q54 pericope-region: vv 9-42 (34 verses), 5 blocks
    # Q26 pericope-region: vv 10-191 (182 verses), 7 blocks
    q54_total_v = sum(p["verses"] for p in q54_stats)
    q26_total_v = sum(p["verses"] for p in q26_stats)
    # also compute words in pericope-region for each surah
    q54_words_in_region = [len(verses_q54[i - 1]["text"].split()) for i in range(9, 43)]  # vv 9-42
    q26_words_in_region = [len(verses_q26[i - 1]["text"].split()) for i in range(10, 192)]  # vv 10-191

    rng = random.Random(SEED)
    n_ge_obs_v = 0
    n_ge_obs_w = 0
    for _ in range(N_PERM):
        sizes_q54 = partition_random(q54_total_v, 5, rng)
        sizes_q26 = partition_random(q26_total_v, 7, rng)
        # Compute mean verses per block under null
        mv54 = sum(sizes_q54) / 5
        mv26 = sum(sizes_q26) / 7
        # Compute mean words per block under null (use the actual words-in-region split by random sizes)
        cuts_q54 = []
        cur = 0
        for s in sizes_q54[:-1]:
            cur += s
            cuts_q54.append(cur)
        block_words_q54 = []
        prev = 0
        for c in cuts_q54 + [q54_total_v]:
            block_words_q54.append(sum(q54_words_in_region[prev:c]))
            prev = c
        mw54 = sum(block_words_q54) / 5
        cuts_q26 = []
        cur = 0
        for s in sizes_q26[:-1]:
            cur += s
            cuts_q26.append(cur)
        block_words_q26 = []
        prev = 0
        for c in cuts_q26 + [q26_total_v]:
            block_words_q26.append(sum(q26_words_in_region[prev:c]))
            prev = c
        mw26 = sum(block_words_q26) / 7
        if (mv26 / mv54 if mv54 > 0 else 0) >= ratio_v:
            n_ge_obs_v += 1
        if (mw26 / mw54 if mw54 > 0 else 0) >= ratio_w:
            n_ge_obs_w += 1
    perm_p_v = n_ge_obs_v / N_PERM
    perm_p_w = n_ge_obs_w / N_PERM
    print(f"  H2a perm-p (random partition): {perm_p_v:.5f}")
    print(f"  H2b perm-p (random partition): {perm_p_w:.5f}")

    # Aggregate
    n_passed = sum([h2a_pass, h2b_pass])
    if n_passed == 2:
        verdict = "CONFIRMED"
    elif n_passed == 1:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"
    if ratio_v < 1.0 or ratio_w < 1.0:
        verdict = "PRE-COMMIT VIOLATION"
    print(f"  Aggregate: {n_passed}/2 passed → {verdict}")

    output = {
        "test_id": "Q054-F-02",
        "title": "Q 54 vs Q 26 prophet-cycle compression",
        "prereg_sha256": sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "Q54_pericopes": q54_stats,
        "Q26_pericopes": q26_stats,
        "Q54_mean_verses_per_pericope": mean_v_q54,
        "Q54_mean_words_per_pericope": mean_w_q54,
        "Q26_mean_verses_per_pericope": mean_v_q26,
        "Q26_mean_words_per_pericope": mean_w_q26,
        "compression_ratio_verses": ratio_v,
        "compression_ratio_words": ratio_w,
        "perm_p_verses": perm_p_v,
        "perm_p_words": perm_p_w,
        "H2a": {"ratio": ratio_v, "threshold": 2.0, "pass": h2a_pass},
        "H2b": {"ratio": ratio_w, "threshold": 2.0, "pass": h2b_pass},
        "aggregate": {"n_passed": n_passed, "verdict": verdict},
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
