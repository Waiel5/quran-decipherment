"""
Q043-F-02: HM-A → HM-B rhyme-entropy structural break
Pre-reg SHA256: 1bfd78dd11cad0e36d13e9d3c8b68fbf01e408e3b97f2278eb76bebb7274b9de
Pre-reg path: surahs/Q043-al-zukhruf/preregs/Q043-F-02-hma-hmb-entropy-break-prereg.md
Seed: 20260428
"""
import hashlib
import json
import math
import os
import random
import sys
from collections import Counter

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/preregs/Q043-F-02-hma-hmb-entropy-break-prereg.md"
EXPECTED_SHA = "1bfd78dd11cad0e36d13e9d3c8b68fbf01e408e3b97f2278eb76bebb7274b9de"
QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/csv/Q043-F-02.json"
SEED = 20260428
N_PERM = 10000


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")


def shannon_entropy(counts):
    total = sum(counts.values())
    if total == 0:
        return 0.0
    H = 0.0
    for c in counts.values():
        if c > 0:
            p = c / total
            H -= p * math.log2(p)
    return H


def main():
    verify_prereg()

    with open(QURAN_PATH) as f:
        quran = json.load(f)

    # Per-surah list of last-graphemes (no-tashkeel)
    surah_finals = {}  # sid -> list of last chars
    surah_entropies = {}
    for s in quran:
        sid = s["id"]
        finals = []
        for v in s["verses"]:
            t = v["text"].strip()
            if t:
                finals.append(t[-1])
        surah_finals[sid] = finals
        surah_entropies[sid] = shannon_entropy(Counter(finals))

    HM7 = [40, 41, 42, 43, 44, 45, 46]
    HMA = [40, 41, 42]
    H43 = surah_entropies[43]
    H_HMA_min = min(surah_entropies[s] for s in HMA)
    H_HMA_max = max(surah_entropies[s] for s in HMA)
    HM7_ranked = sorted([(s, surah_entropies[s]) for s in HM7], key=lambda x: x[1])

    # Verdict (pre-committed)
    if H43 >= H_HMA_max:
        verdict = "PRECOMMIT_VIOLATION"
    elif H43 >= H_HMA_min:
        verdict = "NULL"
    else:
        # Below HM-A min — at least DIRECTIONAL
        if HM7_ranked[0][0] == 43:
            verdict = "VINDICATED"
        else:
            verdict = "DIRECTIONAL"

    # Permutation null (MW-2 corpus-prior).  Shuffle all verse-final-graphemes
    # corpus-wide, redistribute to per-surah verse-counts, recompute Q 43 entropy.
    rng = random.Random(SEED)
    all_finals = []
    surah_n_verses = {}
    for sid, finals in surah_finals.items():
        all_finals.extend(finals)
        surah_n_verses[sid] = len(finals)

    n_perm_below_observed = 0  # how many permuted-Q43 entropies are <= observed
    perm_q43_ents = []
    for _ in range(N_PERM):
        rng.shuffle(all_finals)
        # Slice for Q43
        # Reconstruct per-surah slices in deterministic surah-id order:
        idx = 0
        for sid in range(1, 115):
            n = surah_n_verses[sid]
            if sid == 43:
                slice_q43 = all_finals[idx:idx + n]
                break
            idx += n
        H43_perm = shannon_entropy(Counter(slice_q43))
        perm_q43_ents.append(H43_perm)
        if H43_perm <= H43:
            n_perm_below_observed += 1

    p_perm = n_perm_below_observed / N_PERM

    out = {
        "prereg_id": "Q043-F-02",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "Q43_entropy": round(H43, 4),
        "HM_A_entropies": {f"Q{s}": round(surah_entropies[s], 4) for s in HMA},
        "HM_A_min": round(H_HMA_min, 4),
        "HM_A_max": round(H_HMA_max, 4),
        "HM_B_entropies": {f"Q{s}": round(surah_entropies[s], 4) for s in [43, 44, 45, 46]},
        "HM7_ranked_by_entropy_low_to_high": [(int(s), round(h, 4)) for s, h in HM7_ranked],
        "delta_H_42_to_43": round(surah_entropies[42] - surah_entropies[43], 4),
        "p_perm_Q43_entropy_le_observed": p_perm,
        "n_perm": N_PERM,
        "direction_predicted": "H(43) < min(H(40..42))",
        "direction_observed": ("matches" if H43 < H_HMA_min else "reversed"),
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
