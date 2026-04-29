#!/usr/bin/env python3
"""H-NEW-321: Q 1 ↔ Q 27 Basmala-echo content-axis test."""
import hashlib
import json
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-321-q1-q27-basmala-echo-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-321.json"

SEED = 20260428
N_PERM = 1000

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def load_D():
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat

def rank_of_target(pivot, target, D):
    dists = sorted([(s, D[pivot][s]) for s in range(1, 115) if s != pivot],
                   key=lambda x: x[1])
    for rank, (s, _) in enumerate(dists, 1):
        if s == target:
            return rank, _
    return None, None

def main():
    random.seed(SEED)
    print(f"=== H-NEW-321 ===")
    print(f"Pre-reg SHA: {sha(PREREG)}")
    D = load_D()

    # Cell A: rank(Q 27 | Q 1)
    r27_from_1, d_1_27 = rank_of_target(1, 27, D)
    print(f"\nCell A — rank of Q 27 among Q 1's 113 neighbors:")
    print(f"  rank = {r27_from_1}/113, d(Q1, Q27) = {d_1_27:.4f}")
    pct_A = r27_from_1 / 113.0 * 100
    print(f"  percentile = {pct_A:.1f}%")

    # Cell B: rank(Q 1 | Q 27)
    r1_from_27, d_27_1 = rank_of_target(27, 1, D)
    print(f"\nCell B — rank of Q 1 among Q 27's 113 neighbors:")
    print(f"  rank = {r1_from_27}/113, d(Q27, Q1) = {d_27_1:.4f}")
    pct_B = r1_from_27 / 113.0 * 100
    print(f"  percentile = {pct_B:.1f}%")

    # MW-5 positive control: rank(Q 113 | Q 114) and rank(Q 114 | Q 113)
    r113_from_114, _ = rank_of_target(114, 113, D)
    r114_from_113, _ = rank_of_target(113, 114, D)
    print(f"\nMW-5 positive control (muʿawwidhatān):")
    print(f"  rank(Q 113 | Q 114) = {r113_from_114}/113")
    print(f"  rank(Q 114 | Q 113) = {r114_from_113}/113")
    mw5_pass = r113_from_114 <= 11 or r114_from_113 <= 11

    # Null: for each permutation draw, pick a random pivot (not 1 or 27) and random target
    null_ranks = []
    non_pivot = [s for s in range(1, 115) if s not in (1, 27)]
    for _ in range(N_PERM):
        p = random.choice(non_pivot)
        t = random.choice([s for s in range(1, 115) if s != p])
        r, _ = rank_of_target(p, t, D)
        null_ranks.append(r)
    null_mean_rank = sum(null_ranks) / len(null_ranks)

    # p(rank <= observed)
    p_A = sum(1 for r in null_ranks if r <= r27_from_1) / N_PERM
    p_B = sum(1 for r in null_ranks if r <= r1_from_27) / N_PERM

    print(f"\nNull rank distribution: mean = {null_mean_rank:.2f}")
    print(f"p(null_rank ≤ {r27_from_1}) = {p_A:.4f}")
    print(f"p(null_rank ≤ {r1_from_27}) = {p_B:.4f}")

    alpha_bon = 0.025
    cell_a = r27_from_1 <= 11
    cell_b = r1_from_27 <= 11

    if cell_a and cell_b:
        verdict = "BASMALA-ECHO-MANIFESTS"
    elif cell_a:
        verdict = "ASYMMETRIC-ECHO (1→27 but not 27→1)"
    elif cell_b:
        verdict = "REVERSE-ASYMMETRIC-ECHO (27→1 but not 1→27)"
    else:
        verdict = "NULL — Basmala echo is phrase-specific, not content-clustering"
    print(f"\nCell A (rank ≤ 11): {'PASS' if cell_a else 'FAIL'}")
    print(f"Cell B (rank ≤ 11): {'PASS' if cell_b else 'FAIL'}")
    print(f"MW-5 (muʿawwidhatān rank ≤ 11): {'PASS' if mw5_pass else 'FAIL'}")
    print(f"Verdict: {verdict}")

    out = {
        "id": "H-NEW-321", "prereg_sha": sha(PREREG), "seed": SEED,
        "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": alpha_bon,
        "cell_A": {"rank_27_given_1": r27_from_1, "d_Q1_Q27": d_1_27,
                   "pct": pct_A, "p_null": p_A, "pass": cell_a},
        "cell_B": {"rank_1_given_27": r1_from_27, "d_Q27_Q1": d_27_1,
                   "pct": pct_B, "p_null": p_B, "pass": cell_b},
        "mw5_positive_control": {
            "rank_113_given_114": r113_from_114,
            "rank_114_given_113": r114_from_113,
            "pass": mw5_pass},
        "null_mean_rank": null_mean_rank,
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {OUT_JSON}")

if __name__ == "__main__":
    main()
