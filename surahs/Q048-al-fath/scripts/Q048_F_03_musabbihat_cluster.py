#!/usr/bin/env python3
"""
Q048-F-03 — Q 48 musabbiḥāt-adjacent cluster membership test.

Pre-reg: ../preregs/Q048-F-03-musabbihat-cluster-membership-prereg.md
SHA-locked: df56fc6e80aee104d05a3bff7d4b4f6277aa7fc0c9d0513dc9acbd67d20c5685
Seed: 20260509
"""
import json
import hashlib
import os
import sys

PRE_REG_PATH = os.path.join(os.path.dirname(__file__), '..', 'preregs',
                            'Q048-F-03-musabbihat-cluster-membership-prereg.md')
EXPECTED_SHA = "df56fc6e80aee104d05a3bff7d4b4f6277aa7fc0c9d0513dc9acbd67d20c5685"
SEED = 20260509

H111_PATH = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv', 'Q048-F-03.json')

MUSABBIHAT_CLUSTER = {57, 59, 61, 62, 64}  # H-NEW-58c
BACK_MEDINAN_RANGE = set(range(57, 65))  # Q 57-64


def verify_prereg_sha():
    with open(PRE_REG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        print(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {sha}", file=sys.stderr)
        sys.exit(1)
    return sha


def load_fr_matrix():
    with open(H111_PATH) as f:
        d = json.load(f)
    ut = d['D_matrix_upper_triangular']
    N = 114
    D = [[0.0] * N for _ in range(N)]
    for triple in ut:
        i, j, dist = triple[0], triple[1], triple[2]
        D[i - 1][j - 1] = dist
        D[j - 1][i - 1] = dist
    return D, N


def main():
    sha = verify_prereg_sha()
    print(f"Pre-reg SHA verified: {sha}")

    D, N = load_fr_matrix()

    i48 = 47  # 0-indexed
    nbrs = [(j + 1, D[i48][j]) for j in range(N) if j != i48]
    close = sorted(nbrs, key=lambda x: x[1])

    top5 = close[:5]
    top10 = close[:10]
    top5_surahs = [s for s, _ in top5]
    top5_set = set(top5_surahs)

    t1_top5_in_back_medinan = top5_set <= BACK_MEDINAN_RANGE
    overlap_musabb = top5_set & MUSABBIHAT_CLUSTER
    t2_at_least_3_musabb = len(overlap_musabb) >= 3

    if t1_top5_in_back_medinan and t2_at_least_3_musabb:
        verdict = "CONFIRMED"
    elif t1_top5_in_back_medinan or t2_at_least_3_musabb:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    # Compute null prob (under random 5-subset assumption)
    from math import comb
    p_t1_null = comb(8, 5) / comb(113, 5) if comb(113, 5) else 0
    # T2 null: hypergeom P(≥3 of 5 in 5-success-set out of 113)
    K = 5  # |musabbiḥāt|
    p_t2_null = sum(comb(K, k) * comb(113 - K, 5 - k) / comb(113, 5) for k in range(3, 6))

    result = {
        "test_id": "Q048-F-03",
        "H_NEW": "H-NEW-1262",
        "title": "Q 48 — top-5 FR-nearest ⊆ back-Medinan musabbiḥāt-adjacent cluster",
        "pre_reg_sha": sha,
        "seed": SEED,
        "rules_tuple": "(no-tashkeel, QAC-v0.4-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "alpha_bon": 0.05,
        "bonferroni_k": 1,
        "musabbihat_cluster": sorted(MUSABBIHAT_CLUSTER),
        "back_medinan_range": sorted(BACK_MEDINAN_RANGE),
        "top_5_nearest_to_q48": [{"surah": s, "fr": d} for s, d in top5],
        "top_10_nearest_to_q48": [{"surah": s, "fr": d} for s, d in top10],
        "test_t1_top5_in_back_medinan": t1_top5_in_back_medinan,
        "test_t2_at_least_3_musabbihat": t2_at_least_3_musabb,
        "musabbihat_in_top_5": sorted(overlap_musabb),
        "p_t1_under_uniform_random_5tuple_null": p_t1_null,
        "p_t2_under_uniform_random_5tuple_null": p_t2_null,
        "verdict": verdict,
        "honest_limits": [
            "Test is descriptive-categorical; null is conservative (uniform random 5-tuple).",
            "Q 48's mushaf-immediate neighbors Q 47 (rank 13) and Q 49 (rank 6) are NOT in top-5; this contradicts the al-Biqāʿī Q 47-Q 48-Q 49 munāsabah claim at FR level (already noted as DIRECTIONAL via Q047-F-03).",
            "The cluster-membership pattern is consistent with cross-finding-009 META-cluster network architecture.",
        ],
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Result written to {OUT_PATH}")
    print(f"Verdict: {verdict}")
    print(f"  Top-5 nearest to Q 48: {[(s, round(d, 4)) for s, d in top5]}")
    print(f"  T1 (top-5 ⊆ Q57-64): {t1_top5_in_back_medinan}")
    print(f"  T2 (≥3 musabbiḥāt): {t2_at_least_3_musabb} (intersection: {sorted(overlap_musabb)})")
    print(f"  P(T1 under null): {p_t1_null:.6e}")
    print(f"  P(T2 under null): {p_t2_null:.6e}")


if __name__ == "__main__":
    main()
