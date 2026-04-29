#!/usr/bin/env python3
"""H-NEW-660: Compression-tail gradient — linear regression of d̄(K=15-window) vs mushaf-position."""
import hashlib
import json
import math
import random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-660-compression-tail-gradient-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-660.json"
SEED = 20260433
N_PERMS = 10000
K = 15


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def mean_pairwise(D, subset):
    return sum(D[a][b] for a, b in combinations(subset, 2)) / max(1, len(list(combinations(subset, 2))))


def fit_linear(xs, ys):
    n = len(xs)
    mx, my = sum(xs)/n, sum(ys)/n
    num = sum((xs[i]-mx)*(ys[i]-my) for i in range(n))
    den = sum((xs[i]-mx)**2 for i in range(n))
    beta = num/den
    alpha = my - beta * mx
    yhat = [alpha + beta*x for x in xs]
    ss_tot = sum((y-my)**2 for y in ys)
    ss_res = sum((ys[i]-yhat[i])**2 for i in range(n))
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2, yhat


def fit_quadratic(xs, ys):
    """y = a + b*x + c*x^2 via OLS."""
    n = len(xs)
    sx = sum(xs); sx2 = sum(x*x for x in xs); sx3 = sum(x**3 for x in xs); sx4 = sum(x**4 for x in xs)
    sy = sum(ys); sxy = sum(xs[i]*ys[i] for i in range(n)); sx2y = sum(xs[i]**2*ys[i] for i in range(n))
    # Normal equations: [[n,sx,sx2],[sx,sx2,sx3],[sx2,sx3,sx4]] β = [sy,sxy,sx2y]
    M = [[n, sx, sx2], [sx, sx2, sx3], [sx2, sx3, sx4]]
    b = [sy, sxy, sx2y]
    # Gauss elimination
    A = [row[:] + [b[i]] for i, row in enumerate(M)]
    for col in range(3):
        pivot = max(range(col, 3), key=lambda r: abs(A[r][col]))
        A[col], A[pivot] = A[pivot], A[col]
        piv = A[col][col]
        if abs(piv) < 1e-15: return None, None, None, 0, []
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
    """y = a + b * max(0, x - kink). Hinge model."""
    n = len(xs)
    feat = [max(0, x - kink) for x in xs]
    mx, my = sum(feat)/n, sum(ys)/n
    num = sum((feat[i]-mx)*(ys[i]-my) for i in range(n))
    den = sum((feat[i]-mx)**2 for i in range(n))
    if den < 1e-15: return None, None, 0, []
    beta = num/den
    alpha = my - beta*mx
    yhat = [alpha + beta*f for f in feat]
    ss_tot = sum((y-my)**2 for y in ys)
    ss_res = sum((ys[i]-yhat[i])**2 for i in range(n))
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2, yhat


def adj_r2(r2, n, p):
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-660 (Compression-tail gradient) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\n")

    D = load_D()
    starts = list(range(1, 100))  # start positions 1..99 → window covers 1..15..99..113. With K=15, max start is 100 (cover Q 100-114).
    starts = list(range(1, 101))  # 100 windows
    d_obs = []
    for s in starts:
        sub = list(range(s, s + K))
        d_obs.append(mean_pairwise(D, sub))

    print(f"Computed {len(d_obs)} consecutive K={K} windows.")
    print(f"  d̄ range: {min(d_obs):.4f} (best) to {max(d_obs):.4f} (worst)")
    print(f"  Best window: starts at s={starts[d_obs.index(min(d_obs))]}, covers Q {starts[d_obs.index(min(d_obs))]}-{starts[d_obs.index(min(d_obs))]+K-1}")
    print(f"  Worst window: starts at s={starts[d_obs.index(max(d_obs))]}, covers Q {starts[d_obs.index(max(d_obs))]}-{starts[d_obs.index(max(d_obs))]+K-1}")

    # Center s
    s_center = [s - 50.5 for s in starts]

    # Fit 3 models
    a_lin, b_lin, r2_lin, _ = fit_linear(s_center, d_obs)
    print(f"\n--- LINEAR MODEL ---")
    print(f"  d̄ = {a_lin:.4f} + ({b_lin:+.5f}) · (s - 50.5)")
    print(f"  R² = {r2_lin:.4f}, adjR² = {adj_r2(r2_lin, len(d_obs), 1):.4f}")

    q = fit_quadratic(s_center, d_obs)
    a_q, b_q, c_q, r2_q, _ = q
    print(f"\n--- QUADRATIC MODEL ---")
    print(f"  d̄ = {a_q:.4f} + ({b_q:+.5f}) · s + ({c_q:+.6f}) · s²")
    print(f"  R² = {r2_q:.4f}, adjR² = {adj_r2(r2_q, len(d_obs), 2):.4f}")

    # Try kinks at 25, 50, 75 (in original s coordinates)
    best_kink = None
    best_r2 = -1
    for kink in [25, 50, 75]:
        out = fit_two_piece(starts, d_obs, kink)
        if out[2] > best_r2:
            best_r2 = out[2]
            best_kink = kink
            best_two_piece = out
    a_tp, b_tp, r2_tp, _ = best_two_piece
    print(f"\n--- TWO-PIECE LINEAR (best kink at s={best_kink}) ---")
    print(f"  d̄ = {a_tp:.4f} + ({b_tp:+.5f}) · max(0, s - {best_kink})")
    print(f"  R² = {r2_tp:.4f}, adjR² = {adj_r2(r2_tp, len(d_obs), 1):.4f}")

    # Pick primary model by adjusted R²
    primary_choices = [
        ("linear", r2_lin, adj_r2(r2_lin, len(d_obs), 1)),
        ("quadratic", r2_q, adj_r2(r2_q, len(d_obs), 2)),
        (f"two-piece-kink-{best_kink}", r2_tp, adj_r2(r2_tp, len(d_obs), 1)),
    ]
    primary = max(primary_choices, key=lambda t: t[2])
    print(f"\nPRIMARY (highest adj-R²): {primary[0]}, R²={primary[1]:.4f}, adjR²={primary[2]:.4f}")

    # Permutation null on primary
    print(f"\n--- PERMUTATION NULL on slope ({N_PERMS} perms; shuffle 114 surahs) ---")
    rng = random.Random(SEED)
    null_betas = []
    null_r2s = []
    null_betas_q = []  # quadratic
    null_betas_tp = []  # two-piece
    for _ in range(N_PERMS):
        perm = list(range(1, 115))
        rng.shuffle(perm)
        # New mushaf: position p maps to surah perm[p-1]
        d_perm = []
        for s in starts:
            sub = [perm[s - 1 + i] for i in range(K)]
            d_perm.append(mean_pairwise(D, sub))
        # Linear
        _, b_n, r2_n, _ = fit_linear(s_center, d_perm)
        null_betas.append(b_n)
        null_r2s.append(r2_n)
        # Quadratic
        q_n = fit_quadratic(s_center, d_perm)
        if q_n[1] is not None:
            null_betas_q.append(q_n[3])  # r2
        # Two-piece
        tp_n = fit_two_piece(starts, d_perm, best_kink)
        null_betas_tp.append(tp_n[2])  # r2

    # Empirical p-values
    p_lin_slope = sum(1 for b in null_betas if b <= b_lin) / len(null_betas)  # one-sided (β < 0 expected)
    p_lin_r2 = sum(1 for r in null_r2s if r >= r2_lin) / len(null_r2s)
    p_q_r2 = sum(1 for r in null_betas_q if r >= r2_q) / len(null_betas_q)
    p_tp_r2 = sum(1 for r in null_betas_tp if r >= r2_tp) / len(null_betas_tp)
    print(f"  Linear β observed = {b_lin:+.5f}; p(β ≤ obs) = {p_lin_slope:.5f}")
    print(f"  Linear R² observed = {r2_lin:.4f}; p(R² ≥ obs) = {p_lin_r2:.5f}")
    print(f"  Quadratic R² observed = {r2_q:.4f}; p(R² ≥ obs) = {p_q_r2:.5f}")
    print(f"  Two-piece R² observed = {r2_tp:.4f}; p(R² ≥ obs) = {p_tp_r2:.5f}")

    # Verdict
    alpha_bon = 0.05 / 3
    p_primary = {"linear": p_lin_r2, "quadratic": p_q_r2, f"two-piece-kink-{best_kink}": p_tp_r2}[primary[0]]
    strict = primary[1] >= 0.50 and p_primary <= alpha_bon and b_lin < 0
    directional = primary[1] >= 0.30 and p_primary <= 0.05 and b_lin < 0
    if strict:
        verdict = f"STRICT PASS — gradient quantitatively confirmed; primary={primary[0]}, R²={primary[1]:.4f}, β_lin={b_lin:+.5f}, p={p_primary:.5f}"
    elif directional:
        verdict = f"DIRECTIONAL — gradient supported; primary={primary[0]}, R²={primary[1]:.4f}, β_lin={b_lin:+.5f}, p={p_primary:.5f}"
    else:
        verdict = f"NULL — primary={primary[0]}, R²={primary[1]:.4f}, β_lin={b_lin:+.5f}, p={p_primary:.5f}"
    print(f"\n=== VERDICT: {verdict} ===")
    print(f"  Bonferroni-3 α = {alpha_bon:.5f}")

    out = {
        "id": "H-NEW-660",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "K": K,
        "starts": starts,
        "d_observed": d_obs,
        "linear": {"alpha": a_lin, "beta": b_lin, "r2": r2_lin, "perm_p_slope": p_lin_slope, "perm_p_r2": p_lin_r2},
        "quadratic": {"alpha": a_q, "beta": b_q, "gamma": c_q, "r2": r2_q, "perm_p_r2": p_q_r2},
        "two_piece": {"kink": best_kink, "alpha": a_tp, "beta": b_tp, "r2": r2_tp, "perm_p_r2": p_tp_r2},
        "primary_model": primary[0],
        "primary_r2": primary[1],
        "primary_adj_r2": primary[2],
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
