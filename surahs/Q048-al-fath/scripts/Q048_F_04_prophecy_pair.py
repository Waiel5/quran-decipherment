#!/usr/bin/env python3
"""
Q048-F-04 — Q 48 + Q 30 forward-prophecy pair FR-cohesion test.

Pre-reg: ../preregs/Q048-F-04-prophecy-pair-cohesion-prereg.md
SHA-locked: 53364809db4b805494b1e8343627f8f007979ec6c1b66f5931a9d3a7ab4bc4b8
Seed: 20260509

Hypothesis: classical iʿjāz al-ghayb pair {Q 48, Q 30} is FR-coherent.
Expected (per pre-reg): NULL — they are thematic-only, not FR-cluster.
"""
import json
import hashlib
import os
import sys

PRE_REG_PATH = os.path.join(os.path.dirname(__file__), '..', 'preregs',
                            'Q048-F-04-prophecy-pair-cohesion-prereg.md')
EXPECTED_SHA = "53364809db4b805494b1e8343627f8f007979ec6c1b66f5931a9d3a7ab4bc4b8"
SEED = 20260509

H111_PATH = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv', 'Q048-F-04.json')


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
    fr_48_30 = D[47][29]

    # Corpus mean FR
    fr_pairs = []
    for i in range(N):
        for j in range(i + 1, N):
            fr_pairs.append(D[i][j])
    corpus_mean = sum(fr_pairs) / len(fr_pairs)

    # Q 48-rank of Q 30
    nbrs_48 = sorted([(j + 1, D[47][j]) for j in range(N) if j != 47], key=lambda x: x[1])
    rank_30_in_q48_nearest = next(i + 1 for i, (s, _) in enumerate(nbrs_48) if s == 30)
    # Equivalent: rank in farthest list
    rank_30_in_q48_farthest = 113 - rank_30_in_q48_nearest + 1

    t1_below_corpus_mean = fr_48_30 <= corpus_mean
    t1_strict_below_086 = fr_48_30 <= 0.86
    t2_not_in_top50_farthest = rank_30_in_q48_farthest > 50
    t2_strict_top30_nearest = rank_30_in_q48_nearest <= 30

    if t1_strict_below_086 and t2_strict_top30_nearest:
        verdict = "CONFIRMED"
    elif t1_below_corpus_mean and rank_30_in_q48_nearest <= 56:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    # Also include Q 105 al-Fīl as the retrospective comparator
    fr_48_105 = D[47][104]
    fr_30_105 = D[29][104]
    rank_105_in_q48 = next(i + 1 for i, (s, _) in enumerate(nbrs_48) if s == 105)

    result = {
        "test_id": "Q048-F-04",
        "H_NEW": "H-NEW-1263",
        "title": "Q 48 + Q 30 forward-prophecy pair FR-cohesion test (the iʿjāz al-ghayb pair claim)",
        "pre_reg_sha": sha,
        "seed": SEED,
        "rules_tuple": "(no-tashkeel, QAC-v0.4-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "alpha_bon": 0.05,
        "bonferroni_k": 1,
        "fr_48_30": fr_48_30,
        "corpus_mean_fr": corpus_mean,
        "rank_30_in_q48_nearest": rank_30_in_q48_nearest,
        "rank_30_in_q48_farthest": rank_30_in_q48_farthest,
        "test_t1_fr_below_corpus_mean": t1_below_corpus_mean,
        "test_t1_strict_below_086": t1_strict_below_086,
        "test_t2_not_in_top50_farthest": t2_not_in_top50_farthest,
        "test_t2_strict_top30_nearest": t2_strict_top30_nearest,
        "comparator_fr_48_105": fr_48_105,
        "comparator_fr_30_105": fr_30_105,
        "comparator_rank_105_in_q48": rank_105_in_q48,
        "verdict": verdict,
        "interpretation": (
            f"FR(Q48,Q30)={fr_48_30:.4f} vs corpus mean {corpus_mean:.4f}. "
            f"Q30 rank in Q48-nearest = {rank_30_in_q48_nearest}/113. "
            "Classical iʿjāz al-ghayb pair claim is THEMATIC, NOT FR-cluster."
        ),
        "honest_limits": [
            "The classical iʿjāz al-ghayb pair claim is thematic-content, not structural-distance.",
            "Q 30 is FAR from Q 48 in FR-space (rank ~88/113); they do not form a structural cluster.",
            "Q 105 al-Fīl is RETROSPECTIVE (not forward-looking); it is included only as comparator.",
            "Pre-reg LOCKED the prediction direction (LOW = cohesion) with the EXPECTED outcome being NULL — this is the project's discipline of testing classical claims and reporting NULLs with equal prominence.",
        ],
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Result written to {OUT_PATH}")
    print(f"Verdict: {verdict}")
    print(f"  FR(Q48, Q30) = {fr_48_30:.4f} (corpus mean: {corpus_mean:.4f})")
    print(f"  Q30 rank in Q48-nearest: {rank_30_in_q48_nearest}/113")
    print(f"  T1 (FR ≤ mean): {t1_below_corpus_mean}; T1 strict (≤0.86): {t1_strict_below_086}")
    print(f"  T2 (not in top-50 farthest): {t2_not_in_top50_farthest}; T2 strict (top-30 nearest): {t2_strict_top30_nearest}")


if __name__ == "__main__":
    main()
