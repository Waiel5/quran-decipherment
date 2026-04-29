#!/usr/bin/env python3
"""H-NEW-760: 3-axis inverse regression — predict s from (d_content, d_rhyme, d_phoneme)."""
import hashlib
import json
import math
import random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
H_NEW_700 = ROOT / "findings/phase-b-hypotheses/csv/h-new-700.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-760-three-axis-inverse-regression-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-760.json"
SEED = 20260443
N_PERMS = 1000  # smaller; LOOCV is expensive


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


def transpose(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def matmul(A, B):
    n = len(A); p = len(B[0]); m = len(B)
    C = [[0.0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            a = A[i][k]
            if a == 0: continue
            for j in range(p):
                C[i][j] += a * B[k][j]
    return C


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def inverse(M):
    n = len(M)
    A = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(A[r][col]))
        if abs(A[pivot][col]) < 1e-14: raise ValueError("singular")
        A[col], A[pivot] = A[pivot], A[col]
        piv = A[col][col]
        A[col] = [x / piv for x in A[col]]
        for r in range(n):
            if r == col: continue
            factor = A[r][col]
            if factor == 0: continue
            A[r] = [A[r][k] - factor * A[col][k] for k in range(2 * n)]
    return [row[n:] for row in A]


def fit_ols(X, y, ridge_lam=0.0):
    """Adds intercept column."""
    X1 = [[1.0] + row for row in X]
    XT = transpose(X1)
    XTX = matmul(XT, X1)
    if ridge_lam > 0:
        for i in range(1, len(XTX)):
            XTX[i][i] += ridge_lam
    XTy = matvec(XT, y)
    beta = matvec(inverse(XTX), XTy)
    return beta


def predict(beta, X):
    return [beta[0] + sum(beta[i + 1] * row[i] for i in range(len(row))) for row in X]


def r2(y_true, y_pred):
    n = len(y_true)
    m = sum(y_true) / n
    ss_tot = sum((y - m) ** 2 for y in y_true)
    ss_res = sum((y_true[i] - y_pred[i]) ** 2 for i in range(n))
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0


def loocv_r2(X, y, ridge_lam=0.0):
    n = len(X)
    yhat = []
    for i in range(n):
        X_i = X[:i] + X[i+1:]
        y_i = y[:i] + y[i+1:]
        try:
            b = fit_ols(X_i, y_i, ridge_lam)
            yhat.append(predict(b, [X[i]])[0])
        except ValueError:
            yhat.append(float('nan'))
    if any(math.isnan(p) for p in yhat):
        return float('nan'), yhat
    return r2(y, yhat), yhat


def mae(y_true, y_pred):
    return sum(abs(y_true[i] - y_pred[i]) for i in range(len(y_true))) / len(y_true)


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-760 (3-axis inverse regression) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\n")

    # Load data
    D = load_D()
    K = 15
    starts = list(range(1, 101))
    d_content = [mean_pairwise(D, list(range(s, s + K))) for s in starts]
    with open(H_NEW_700) as f:
        h700 = json.load(f)
    d_rhyme = h700["rhyme"]["d_observed"]
    d_phoneme = h700["phoneme"]["d_observed"]

    print(f"Loaded {len(starts)} windows; predictors: d_content, d_rhyme, d_phoneme.\n")

    # Build feature sets for 3 models
    # Model 1: linear
    X_lin = [[d_content[i], d_rhyme[i], d_phoneme[i]] for i in range(len(starts))]
    # Model 2: linear + 3 interactions
    X_int = [X_lin[i] + [
        d_content[i] * d_rhyme[i],
        d_content[i] * d_phoneme[i],
        d_rhyme[i] * d_phoneme[i]
    ] for i in range(len(starts))]
    # Model 3: linear + 3 quadratic
    X_quad = [X_lin[i] + [
        d_content[i] ** 2,
        d_rhyme[i] ** 2,
        d_phoneme[i] ** 2
    ] for i in range(len(starts))]

    y = [float(s) for s in starts]

    # Fit each model
    models = [("linear", X_lin), ("linear+interactions", X_int), ("linear+quadratic", X_quad)]
    results = {}
    for name, X in models:
        beta = fit_ols(X, y)
        yhat_in = predict(beta, X)
        r2_in = r2(y, yhat_in)
        loo_r2, yhat_loo = loocv_r2(X, y, ridge_lam=0.0)
        loo_mae = mae(y, yhat_loo) if not math.isnan(loo_r2) else float('nan')
        in_mae = mae(y, yhat_in)
        print(f"--- Model: {name} ---")
        print(f"  In-sample R² = {r2_in:.4f}, MAE = {in_mae:.2f}")
        print(f"  LOOCV   R² = {loo_r2:.4f}, MAE = {loo_mae:.2f}")
        print(f"  Coefficients (intercept, then features): {[f'{b:+.3f}' for b in beta]}\n")
        results[name] = {
            "beta": beta, "r2_in": r2_in, "loo_r2": loo_r2,
            "in_mae": in_mae, "loo_mae": loo_mae,
            "yhat_in": yhat_in, "yhat_loo": yhat_loo
        }

    # Sign check on linear model
    beta_lin = results["linear"]["beta"]
    sign_content = beta_lin[1] < 0
    sign_rhyme = beta_lin[2] > 0
    sign_phoneme = beta_lin[3] > 0
    print(f"Pre-committed sign check (linear):")
    print(f"  β(d_content) < 0: {sign_content} (β = {beta_lin[1]:+.4f})")
    print(f"  β(d_rhyme) > 0:   {sign_rhyme} (β = {beta_lin[2]:+.4f})")
    print(f"  β(d_phoneme) > 0: {sign_phoneme} (β = {beta_lin[3]:+.4f})")

    # Permutation null on linear model
    print(f"\n--- PERMUTATION NULL ({N_PERMS} perms, linear LOOCV R²) ---")
    rng = random.Random(SEED)
    null_r2s = []
    for _ in range(N_PERMS):
        y_perm = y[:]
        rng.shuffle(y_perm)
        try:
            r2_perm, _ = loocv_r2(X_lin, y_perm, ridge_lam=0.0)
            if not math.isnan(r2_perm):
                null_r2s.append(r2_perm)
        except ValueError:
            pass
    p_emp = sum(1 for r in null_r2s if r >= results["linear"]["loo_r2"]) / len(null_r2s) if null_r2s else 1.0
    print(f"  p(LOOCV R² ≥ observed {results['linear']['loo_r2']:.4f}) = {p_emp:.5f}")

    # Verdict
    alpha_bon = 0.05 / 3
    primary = max(results.values(), key=lambda r: r["loo_r2"] if not math.isnan(r["loo_r2"]) else -1)
    primary_name = [n for n, r in results.items() if r is primary][0]
    print(f"\n=== Primary (highest LOOCV R²): {primary_name}: {primary['loo_r2']:.4f} ===")

    strict = primary["loo_r2"] >= 0.95 and primary["loo_mae"] <= 5 and sign_content and sign_rhyme and sign_phoneme
    directional = primary["loo_r2"] >= 0.85 and primary["loo_mae"] <= 10
    if strict:
        verdict = f"STRICT PASS — primary {primary_name}: LOOCV R²={primary['loo_r2']:.4f}, MAE={primary['loo_mae']:.2f}; all signs correct; perm p={p_emp:.5f}"
    elif directional:
        verdict = f"DIRECTIONAL — primary {primary_name}: LOOCV R²={primary['loo_r2']:.4f}, MAE={primary['loo_mae']:.2f}; perm p={p_emp:.5f}"
    else:
        verdict = f"NULL — primary {primary_name}: LOOCV R²={primary['loo_r2']:.4f}, MAE={primary['loo_mae']:.2f}"
    print(f"\n=== VERDICT: {verdict} ===")
    print(f"  Bonferroni-3 α = {alpha_bon:.5f}")

    out = {
        "id": "H-NEW-760",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "K": K,
        "starts": starts,
        "models": {n: {k: r[k] for k in r if k not in ["yhat_in", "yhat_loo"]} for n, r in results.items()},
        "primary_model": primary_name,
        "primary_loocv_r2": primary["loo_r2"],
        "primary_mae": primary["loo_mae"],
        "linear_signs_correct": sign_content and sign_rhyme and sign_phoneme,
        "linear_perm_p": p_emp,
        "alpha_bon": alpha_bon,
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
