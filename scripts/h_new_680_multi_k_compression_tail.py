#!/usr/bin/env python3
"""H-NEW-680: Multi-K compression-tail spectrum.

Mirrors h_new_660_compression_tail_gradient.py methodology, but tests
K ∈ {7, 11, 22}, refines the kink over a broader grid, and applies
Bonferroni-3 within K plus Bonferroni-3 across K.

Pre-reg: findings/phase-b-hypotheses/h-new-680-multi-k-compression-tail-prereg.md
Pre-reg SHA256 (recorded in output JSON): 316642e9ac0839a63f9f3817e048565ca393b944161fa00e0c4d38874a572c46
"""
import hashlib
import json
import random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-680-multi-k-compression-tail-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-680.json"

SEED = 20260434
N_PERMS = 10000
K_VALUES = [7, 11, 22]
KINK_GRID_COARSE = [25, 50, 75]                                        # locked initial grid (matches H-NEW-660)
KINK_GRID_REFINE = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]        # locked refinement grid
ALPHA_BON_WITHIN_K = 0.05 / 3        # 0.01667 — 3 models per K
ALPHA_BON_CROSS_K  = ALPHA_BON_WITHIN_K / 3   # 0.00556 — additional Bonferroni-3 across K


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def mean_pairwise(D, subset):
    pairs = list(combinations(subset, 2))
    return sum(D[a][b] for a, b in pairs) / len(pairs)


def fit_linear(xs, ys):
    n = len(xs)
    mx, my = sum(xs)/n, sum(ys)/n
    num = sum((xs[i]-mx)*(ys[i]-my) for i in range(n))
    den = sum((xs[i]-mx)**2 for i in range(n))
    if abs(den) < 1e-15: return None, None, 0.0, []
    beta = num/den
    alpha = my - beta * mx
    yhat = [alpha + beta*x for x in xs]
    ss_tot = sum((y-my)**2 for y in ys)
    ss_res = sum((ys[i]-yhat[i])**2 for i in range(n))
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2, yhat


def fit_quadratic(xs, ys):
    n = len(xs)
    sx = sum(xs); sx2 = sum(x*x for x in xs); sx3 = sum(x**3 for x in xs); sx4 = sum(x**4 for x in xs)
    sy = sum(ys); sxy = sum(xs[i]*ys[i] for i in range(n)); sx2y = sum(xs[i]**2*ys[i] for i in range(n))
    M = [[n, sx, sx2], [sx, sx2, sx3], [sx2, sx3, sx4]]
    b = [sy, sxy, sx2y]
    A = [row[:] + [b[i]] for i, row in enumerate(M)]
    for col in range(3):
        pivot = max(range(col, 3), key=lambda r: abs(A[r][col]))
        A[col], A[pivot] = A[pivot], A[col]
        piv = A[col][col]
        if abs(piv) < 1e-15: return None, None, None, 0.0, []
        A[col] = [x/piv for x in A[col]]
        for r in range(3):
            if r == col: continue
            factor = A[r][col]
            A[r] = [A[r][k] - factor*A[col][k] for k in range(4)]
    a, bx, c = A[0][3], A[1][3], A[2][3]
    yhat = [a + bx*x + c*x*x for x in xs]
    my = sum(ys)/n
    ss_tot = sum((y-my)**2 for y in ys)
    ss_res = sum((ys[i]-yhat[i])**2 for i in range(n))
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    return a, bx, c, r2, yhat


def fit_two_piece(xs, ys, kink):
    n = len(xs)
    feat = [max(0, x - kink) for x in xs]
    mx, my = sum(feat)/n, sum(ys)/n
    num = sum((feat[i]-mx)*(ys[i]-my) for i in range(n))
    den = sum((feat[i]-mx)**2 for i in range(n))
    if den < 1e-15: return None, None, 0.0, []
    beta = num/den
    alpha = my - beta*mx
    yhat = [alpha + beta*f for f in feat]
    ss_tot = sum((y-my)**2 for y in ys)
    ss_res = sum((ys[i]-yhat[i])**2 for i in range(n))
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2, yhat


def adj_r2(r2, n, p):
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def best_two_piece_over_grid(starts, d_obs, grid):
    best = None
    for k in grid:
        out = fit_two_piece(starts, d_obs, k)
        if out[2] is None: continue
        if best is None or out[2] > best[3]:
            best = (k, out[0], out[1], out[2])  # (kink, alpha, beta, r2)
    return best


def run_for_K(D, K):
    print(f"\n========================================")
    print(f"   K = {K}")
    print(f"========================================")
    starts = list(range(1, 114 - K + 2))   # s = 1 .. 114-K+1
    d_obs = []
    for s in starts:
        sub = list(range(s, s + K))
        d_obs.append(mean_pairwise(D, sub))
    n = len(starts)
    print(f"  Windows: {n} (start s={starts[0]}..{starts[-1]})")
    print(f"  d̄ range: best={min(d_obs):.4f} at s={starts[d_obs.index(min(d_obs))]}; worst={max(d_obs):.4f} at s={starts[d_obs.index(max(d_obs))]}")

    s_center = [s - (sum(starts) / n) for s in starts]

    # 3 baseline models
    a_lin, b_lin, r2_lin, _ = fit_linear(s_center, d_obs)
    a_q, b_q, c_q, r2_q, _ = fit_quadratic(s_center, d_obs)

    # Coarse two-piece on locked H-NEW-660 grid {25, 50, 75}
    coarse = best_two_piece_over_grid(starts, d_obs, KINK_GRID_COARSE)
    coarse_kink, coarse_alpha, coarse_beta, coarse_r2 = coarse

    # Refined two-piece on extended grid (kink-position confidence)
    refine = best_two_piece_over_grid(starts, d_obs, KINK_GRID_REFINE)
    refine_kink, refine_alpha, refine_beta, refine_r2 = refine

    # Per-grid R² profile (for kink-CI reporting)
    kink_profile = []
    for k in KINK_GRID_REFINE:
        out = fit_two_piece(starts, d_obs, k)
        kink_profile.append({"kink": k, "alpha": out[0], "beta": out[1], "r2": out[2]})

    print(f"  LINEAR     : β={b_lin:+.5f}  R²={r2_lin:.4f}  adjR²={adj_r2(r2_lin, n, 1):.4f}")
    print(f"  QUADRATIC  : R²={r2_q:.4f}  adjR²={adj_r2(r2_q, n, 2):.4f}")
    print(f"  TWO-PIECE  : best kink (coarse {{25,50,75}}) = {coarse_kink}, R²={coarse_r2:.4f}")
    print(f"  TWO-PIECE  : best kink (refine 25..75 by 5) = {refine_kink}, R²={refine_r2:.4f}, β={refine_beta:+.5f}")

    # Choose primary-two-piece using the COARSE grid (mirror H-NEW-660 protocol so cross-K comparison is apples-to-apples).
    # Refined kink is reported separately as the "best fit" for kink-position-CI purposes.
    primary_two_piece = (coarse_kink, coarse_alpha, coarse_beta, coarse_r2)

    primary_choices = [
        ("linear",                              r2_lin, adj_r2(r2_lin, n, 1)),
        ("quadratic",                           r2_q,   adj_r2(r2_q, n, 2)),
        (f"two-piece-kink-{primary_two_piece[0]}", primary_two_piece[3],
                                                adj_r2(primary_two_piece[3], n, 1)),
    ]
    primary = max(primary_choices, key=lambda t: t[2])
    print(f"  PRIMARY (highest adj-R²): {primary[0]}, R²={primary[1]:.4f}, adjR²={primary[2]:.4f}")

    # Permutation null
    print(f"  Running {N_PERMS} permutations...")
    rng = random.Random(SEED + K)   # K-specific seed offset for reproducibility but distinct streams
    null_lin_r2 = []
    null_q_r2 = []
    null_tp_r2_at_primary_kink = []

    for _ in range(N_PERMS):
        perm = list(range(1, 115))
        rng.shuffle(perm)
        d_perm = []
        for s in starts:
            sub = [perm[s - 1 + i] for i in range(K)]
            d_perm.append(mean_pairwise(D, sub))
        _, _, r2_n, _ = fit_linear(s_center, d_perm)
        null_lin_r2.append(r2_n)
        q_n = fit_quadratic(s_center, d_perm)
        null_q_r2.append(q_n[3])
        tp_n = fit_two_piece(starts, d_perm, primary_two_piece[0])
        null_tp_r2_at_primary_kink.append(tp_n[2])

    p_lin = sum(1 for r in null_lin_r2 if r >= r2_lin) / N_PERMS
    p_q   = sum(1 for r in null_q_r2 if r >= r2_q) / N_PERMS
    p_tp  = sum(1 for r in null_tp_r2_at_primary_kink if r >= primary_two_piece[3]) / N_PERMS
    null_lin_mean = sum(null_lin_r2) / N_PERMS
    null_q_mean   = sum(null_q_r2) / N_PERMS
    null_tp_mean  = sum(null_tp_r2_at_primary_kink) / N_PERMS

    print(f"    Linear     R² obs={r2_lin:.4f}  null mean={null_lin_mean:.4f}  p={p_lin:.5f}")
    print(f"    Quadratic  R² obs={r2_q:.4f}  null mean={null_q_mean:.4f}  p={p_q:.5f}")
    print(f"    Two-piece  R² obs={primary_two_piece[3]:.4f}  null mean={null_tp_mean:.4f}  p={p_tp:.5f}")

    # Best/worst windows
    bw_idx = d_obs.index(min(d_obs))
    ww_idx = d_obs.index(max(d_obs))

    return {
        "K": K,
        "n_windows": n,
        "starts": starts,
        "d_observed": d_obs,
        "best_window": {"start_s": starts[bw_idx], "covers": f"Q {starts[bw_idx]}-{starts[bw_idx]+K-1}", "d_bar": d_obs[bw_idx]},
        "worst_window": {"start_s": starts[ww_idx], "covers": f"Q {starts[ww_idx]}-{starts[ww_idx]+K-1}", "d_bar": d_obs[ww_idx]},
        "linear":    {"alpha": a_lin, "beta": b_lin, "r2": r2_lin, "adj_r2": adj_r2(r2_lin, n, 1), "perm_p_r2": p_lin, "null_mean_r2": null_lin_mean},
        "quadratic": {"alpha": a_q, "beta": b_q, "gamma": c_q, "r2": r2_q, "adj_r2": adj_r2(r2_q, n, 2), "perm_p_r2": p_q, "null_mean_r2": null_q_mean},
        "two_piece_coarse": {"kink": coarse_kink, "alpha": coarse_alpha, "beta": coarse_beta, "r2": coarse_r2, "adj_r2": adj_r2(coarse_r2, n, 1), "perm_p_r2": p_tp, "null_mean_r2": null_tp_mean},
        "two_piece_refined": {"kink": refine_kink, "alpha": refine_alpha, "beta": refine_beta, "r2": refine_r2, "adj_r2": adj_r2(refine_r2, n, 1)},
        "kink_profile": kink_profile,
        "primary_model": primary[0],
        "primary_r2": primary[1],
        "primary_adj_r2": primary[2],
        "primary_perm_p_r2": {"linear": p_lin, "quadratic": p_q, f"two-piece-kink-{primary_two_piece[0]}": p_tp}[primary[0]],
    }


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-680 (Multi-K compression-tail spectrum) ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Seed: {SEED}, K values: {K_VALUES}, n_perms per K: {N_PERMS}")
    print(f"α_bon (within-K, 3 models)  = {ALPHA_BON_WITHIN_K:.5f}")
    print(f"α_bon (across-K, additional 3-K) = {ALPHA_BON_CROSS_K:.5f}")

    D = load_D()

    per_K = {}
    for K in K_VALUES:
        per_K[str(K)] = run_for_K(D, K)

    # Cross-K convergence check
    primary_kinks = []
    refined_kinks = []
    for K in K_VALUES:
        primary_model = per_K[str(K)]["primary_model"]
        if primary_model.startswith("two-piece"):
            primary_kinks.append((K, per_K[str(K)]["two_piece_coarse"]["kink"]))
        refined_kinks.append((K, per_K[str(K)]["two_piece_refined"]["kink"]))

    print(f"\n========================================")
    print(f"   CROSS-K CONVERGENCE")
    print(f"========================================")
    print(f"  Coarse-grid kinks (primary): {primary_kinks}")
    print(f"  Refined-grid kinks         : {refined_kinks}")

    # Strict-pass evaluation
    strict_per_K = {}
    for K in K_VALUES:
        rec = per_K[str(K)]
        primary_r2 = rec["primary_r2"]
        primary_p = rec["primary_perm_p_r2"]
        refined_kink = rec["two_piece_refined"]["kink"]
        beta_ref = rec["two_piece_refined"]["beta"]
        passes_within = primary_r2 >= 0.50 and primary_p <= ALPHA_BON_WITHIN_K
        passes_cross  = primary_r2 >= 0.50 and primary_p <= ALPHA_BON_CROSS_K
        kink_in_window = 40 <= refined_kink <= 60
        beta_neg = beta_ref < 0
        strict_per_K[str(K)] = {
            "passes_within_K": passes_within,
            "passes_cross_K":  passes_cross,
            "kink_in_40_60":   kink_in_window,
            "beta_negative":   beta_neg,
            "strict_pass_for_K": passes_cross and kink_in_window and beta_neg,
        }

    all_strict = all(s["strict_pass_for_K"] for s in strict_per_K.values())
    all_directional = all(
        per_K[str(K)]["primary_r2"] >= 0.30
        and per_K[str(K)]["primary_perm_p_r2"] <= 0.05
        and per_K[str(K)]["two_piece_refined"]["beta"] < 0
        and 30 <= per_K[str(K)]["two_piece_refined"]["kink"] <= 70
        for K in K_VALUES
    )

    refined_kink_values = [k for _, k in refined_kinks]
    kink_spread = max(refined_kink_values) - min(refined_kink_values)
    scale_invariant = all_strict and kink_spread <= 20

    if scale_invariant:
        verdict = (f"STRICT PASS (SCALE-INVARIANT) — at every K ∈ {K_VALUES} the two-piece-kink law "
                   f"clears α_cross={ALPHA_BON_CROSS_K:.5f}, refined kinks span {kink_spread} surahs (within ±10 of s=50).")
    elif all_strict:
        verdict = (f"STRICT PASS — all K clear within-K Bonferroni; cross-K kink-spread = {kink_spread} surahs (>20 → not strictly scale-invariant).")
    elif all_directional:
        verdict = (f"DIRECTIONAL — all K supported at α=0.05 with kinks ∈ [30, 70]; refined-kink spread = {kink_spread}.")
    else:
        verdict = (f"PARTIAL/NULL — see per-K table; kink-spread = {kink_spread}.")

    print(f"\n=== VERDICT: {verdict} ===")

    out = {
        "id": "H-NEW-680",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "K_values": K_VALUES,
        "n_perms": N_PERMS,
        "alpha_bon_within_K": ALPHA_BON_WITHIN_K,
        "alpha_bon_cross_K":  ALPHA_BON_CROSS_K,
        "kink_grid_coarse":   KINK_GRID_COARSE,
        "kink_grid_refine":   KINK_GRID_REFINE,
        "per_K": per_K,
        "strict_per_K": strict_per_K,
        "cross_K": {
            "coarse_kinks": primary_kinks,
            "refined_kinks": refined_kinks,
            "refined_kink_spread": kink_spread,
            "all_strict_pass": all_strict,
            "all_directional": all_directional,
            "scale_invariant": scale_invariant,
        },
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
