#!/usr/bin/env python3
"""H-NEW-580: 5-Factor Cohesion Regression with out-of-sample subset prediction.

Stage 1: Fit OLS + Ridge on the 12 training subsets from cross-finding-024 §3.
Stage 2: Predict %ile for 6 NEW pre-registered subsets, observe true %ile,
         report r_pred, MAE, and permutation null.
"""
import hashlib
import json
import math
import random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-580-five-factor-regression-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-580.json"
SEED = 20260428
N_PERMS = 10000
N_PERMS_NULL_REGR = 10000

# Training data — 12 subsets from cross-finding-024 §3 (see prereg §2).
# Format: (label, %ile_observed, [block, register, chrono, formula, no_outlier])
TRAIN = [
    ("Q107-114",         0.0,  [1, 1, 1, 0, 1]),
    ("Q98-114",          0.0,  [1, 1, 1, 0, 1]),
    ("Q57-66",           4.8,  [1, 1, 1, 0, 1]),
    ("Q67-77",           7.1,  [1, 1, 1, 0, 1]),
    ("musab-block5",     8.1,  [1, 1, 1, 1, 1]),
    ("Q2-9-tiwal",      17.3,  [1, 0, 0, 0, 1]),
    ("HM-5/6",          21.0,  [1, 0, 1, 1, 1]),
    ("Q50-56-noQ55",    37.5,  [1, 0, 1, 0, 1]),
    ("Q50-66-mufTiwal", 50.1,  [1, 0, 0, 0, 0]),
    ("Q50-56-Meccan",   70.1,  [1, 0, 1, 0, 0]),
    ("hamidat",         75.0,  [0, 0, 0, 1, 1]),
    ("Q1+Q27",          81.0,  [0, 0, 0, 0, 1]),
]

# Out-of-sample subsets — factor-labels committed in prereg §3.
# Format: (label, surah_indices, [block, register, chrono, formula, no_outlier])
OOS = [
    ("Q78-89",      list(range(78, 90)),                           [1, 1, 1, 0, 1]),
    ("Q86-92",      list(range(86, 93)),                           [1, 1, 1, 0, 1]),
    ("Q93-99",      list(range(93, 100)),                          [1, 1, 1, 0, 1]),
    ("Q51-54",      [51, 52, 53, 54],                              [1, 0, 1, 0, 1]),
    ("Q7-15",       [7, 8, 9, 10, 11, 12, 13, 14, 15],             [1, 0, 0, 1, 1]),
    ("Q30-39",      list(range(30, 40)),                           [1, 0, 0, 0, 0]),
]

FACTOR_NAMES = ["block_adj", "register_homog", "chrono_homog", "formula_share", "no_outlier"]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def mean_pairwise(D, subset):
    xs = list(subset)
    vals = [D[a][b] for a, b in combinations(xs, 2)]
    return sum(vals) / len(vals) if vals else 0.0


def percentile_in_null(D, observed, size, n_perms, rng):
    all_surahs = list(range(1, 115))
    below = 0
    for _ in range(n_perms):
        sub = rng.sample(all_surahs, size)
        if mean_pairwise(D, sub) <= observed:
            below += 1
    return 100.0 * below / n_perms


# --- Linear algebra utilities (no numpy) ---
def transpose(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def matmul(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    assert cols_A == rows_B
    C = [[0.0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for k in range(cols_A):
            a = A[i][k]
            if a == 0:
                continue
            for j in range(cols_B):
                C[i][j] += a * B[k][j]
    return C


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def inverse(M):
    """Gauss-Jordan inverse for small square matrix."""
    n = len(M)
    A = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        # find pivot
        pivot = max(range(col, n), key=lambda r: abs(A[r][col]))
        if abs(A[pivot][col]) < 1e-12:
            raise ValueError(f"Singular matrix at column {col}")
        A[col], A[pivot] = A[pivot], A[col]
        piv = A[col][col]
        A[col] = [x / piv for x in A[col]]
        for r in range(n):
            if r == col:
                continue
            factor = A[r][col]
            if factor == 0:
                continue
            A[r] = [A[r][k] - factor * A[col][k] for k in range(2 * n)]
    return [row[n:] for row in A]


def fit_ols(X, y):
    """β = (X'X)^-1 X'y. Adds intercept column."""
    n = len(X)
    X1 = [[1.0] + row for row in X]
    XT = transpose(X1)
    XTX = matmul(XT, X1)
    XTy = matvec(XT, y)
    beta = matvec(inverse(XTX), XTy)
    return beta  # [intercept, β1...β5]


def fit_ridge(X, y, lam=1.0):
    n = len(X)
    p = len(X[0])
    X1 = [[1.0] + row for row in X]
    XT = transpose(X1)
    XTX = matmul(XT, X1)
    # Add ridge penalty (NOT on intercept)
    for i in range(1, p + 1):
        XTX[i][i] += lam
    XTy = matvec(XT, y)
    beta = matvec(inverse(XTX), XTy)
    return beta


def predict(beta, X):
    return [beta[0] + sum(beta[i + 1] * row[i] for i in range(len(row))) for row in X]


def r2_score(y_true, y_pred):
    n = len(y_true)
    mean_y = sum(y_true) / n
    ss_tot = sum((y - mean_y) ** 2 for y in y_true)
    ss_res = sum((y_true[i] - y_pred[i]) ** 2 for i in range(n))
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0


def pearson_r(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    num = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    dx = math.sqrt(sum((x[i] - mx) ** 2 for i in range(n)))
    dy = math.sqrt(sum((y[i] - my) ** 2 for i in range(n)))
    return num / (dx * dy) if dx > 0 and dy > 0 else 0.0


def mae(y_true, y_pred):
    return sum(abs(y_true[i] - y_pred[i]) for i in range(len(y_true))) / len(y_true)


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-580 (5-Factor Cohesion Regression) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\n")

    # Stage 1: Fit on training-12
    X_train = [row[2] for row in TRAIN]
    y_train = [row[1] for row in TRAIN]
    labels_train = [row[0] for row in TRAIN]

    beta_ols = fit_ols(X_train, y_train)
    beta_ridge = fit_ridge(X_train, y_train, lam=1.0)
    yhat_ols_train = predict(beta_ols, X_train)
    yhat_ridge_train = predict(beta_ridge, X_train)
    r2_ols_train = r2_score(y_train, yhat_ols_train)
    r2_ridge_train = r2_score(y_train, yhat_ridge_train)

    print("--- Stage-1 (in-sample) ---")
    print(f"  OLS    R² = {r2_ols_train:.4f}")
    print(f"  Ridge  R² = {r2_ridge_train:.4f}")
    print(f"  OLS β: intercept={beta_ols[0]:.2f}, " +
          ", ".join(f"{n}={beta_ols[i+1]:.2f}" for i, n in enumerate(FACTOR_NAMES)))
    print(f"  Ridge β: intercept={beta_ridge[0]:.2f}, " +
          ", ".join(f"{n}={beta_ridge[i+1]:.2f}" for i, n in enumerate(FACTOR_NAMES)))

    # Sign check
    ols_signs_correct = all(beta_ols[i + 1] < 0 for i in range(5))
    ridge_signs_correct = all(beta_ridge[i + 1] < 0 for i in range(5))
    print(f"  All OLS βs negative (pre-committed): {ols_signs_correct}")
    print(f"  All Ridge βs negative (pre-committed): {ridge_signs_correct}")

    # LOOCV (informational)
    loo_pred_ols = []
    loo_pred_ridge = []
    for i in range(len(TRAIN)):
        X_loo = [X_train[j] for j in range(len(TRAIN)) if j != i]
        y_loo = [y_train[j] for j in range(len(TRAIN)) if j != i]
        try:
            b_o = fit_ols(X_loo, y_loo)
            loo_pred_ols.append(predict(b_o, [X_train[i]])[0])
        except ValueError:
            loo_pred_ols.append(float("nan"))
        b_r = fit_ridge(X_loo, y_loo, lam=1.0)
        loo_pred_ridge.append(predict(b_r, [X_train[i]])[0])
    loo_r2_ols = r2_score(y_train, loo_pred_ols) if not any(math.isnan(p) for p in loo_pred_ols) else None
    loo_r2_ridge = r2_score(y_train, loo_pred_ridge)
    print(f"  LOOCV  R² (OLS):   {loo_r2_ols}")
    print(f"  LOOCV  R² (Ridge): {loo_r2_ridge:.4f}")

    # Stage 2: Compute observed %iles for OOS subsets
    print("\n--- Stage-2 (out-of-sample) ---")
    print("Computing observed %iles for 6 OOS subsets...")
    D = load_D()
    oos_observed = []
    for label, surahs, _ in OOS:
        rng = random.Random(SEED + hash(label) % 100000)
        d = mean_pairwise(D, surahs)
        pct = percentile_in_null(D, d, len(surahs), N_PERMS, rng)
        oos_observed.append(pct)
        print(f"  {label} (N={len(surahs)}): d̄={d:.4f}, %ile={pct:.2f}")

    X_oos = [row[2] for row in OOS]
    yhat_oos_ols = predict(beta_ols, X_oos)
    yhat_oos_ridge = predict(beta_ridge, X_oos)

    print("\n  Predictions (OLS / Ridge / observed):")
    for i, (label, _, _) in enumerate(OOS):
        print(f"    {label}: OLS={yhat_oos_ols[i]:.1f}, Ridge={yhat_oos_ridge[i]:.1f}, observed={oos_observed[i]:.2f}")

    r_pred_ols = pearson_r(yhat_oos_ols, oos_observed)
    r_pred_ridge = pearson_r(yhat_oos_ridge, oos_observed)
    mae_pred_ols = mae(oos_observed, yhat_oos_ols)
    mae_pred_ridge = mae(oos_observed, yhat_oos_ridge)
    print(f"\n  OOS Pearson r (OLS):   {r_pred_ols:.4f}")
    print(f"  OOS Pearson r (Ridge): {r_pred_ridge:.4f}")
    print(f"  OOS MAE (OLS):         {mae_pred_ols:.2f}")
    print(f"  OOS MAE (Ridge):       {mae_pred_ridge:.2f}")

    # Permutation null: shuffle training %iles, refit, predict OOS
    print(f"\n--- Permutation null ({N_PERMS_NULL_REGR} perms) ---")
    rng_null = random.Random(SEED)
    null_r_ols = []
    null_r_ridge = []
    for _ in range(N_PERMS_NULL_REGR):
        y_perm = y_train[:]
        rng_null.shuffle(y_perm)
        try:
            b_o = fit_ols(X_train, y_perm)
            yhat_o = predict(b_o, X_oos)
            null_r_ols.append(pearson_r(yhat_o, oos_observed))
        except ValueError:
            pass
        b_r = fit_ridge(X_train, y_perm, lam=1.0)
        yhat_r = predict(b_r, X_oos)
        null_r_ridge.append(pearson_r(yhat_r, oos_observed))

    p_ols = sum(1 for r in null_r_ols if r >= r_pred_ols) / len(null_r_ols)
    p_ridge = sum(1 for r in null_r_ridge if r >= r_pred_ridge) / len(null_r_ridge)
    print(f"  OLS   permutation p = {p_ols:.5f} (Bonferroni α=0.025)")
    print(f"  Ridge permutation p = {p_ridge:.5f} (Bonferroni α=0.025)")

    # Verdict (PRE-REG-STANDARD-04 §5)
    strict = (r_pred_ridge >= 0.70 and mae_pred_ridge <= 25 and ridge_signs_correct
              and r_pred_ols >= 0.70 and mae_pred_ols <= 25 and ols_signs_correct)
    directional = (r_pred_ridge >= 0.50 and mae_pred_ridge <= 35
                   and r_pred_ols >= 0.50 and mae_pred_ols <= 35)
    if strict:
        verdict = "STRICT PASS"
    elif directional:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"
    print(f"\n=== VERDICT: {verdict} ===")

    out = {
        "id": "H-NEW-580",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "stage1": {
            "labels": labels_train,
            "y_train": y_train,
            "X_train": X_train,
            "ols": {
                "beta": beta_ols,
                "yhat_train": yhat_ols_train,
                "r2_train": r2_ols_train,
                "all_signs_negative": ols_signs_correct,
                "loo_r2": loo_r2_ols,
            },
            "ridge_lam_1": {
                "beta": beta_ridge,
                "yhat_train": yhat_ridge_train,
                "r2_train": r2_ridge_train,
                "all_signs_negative": ridge_signs_correct,
                "loo_r2": loo_r2_ridge,
            },
        },
        "stage2_oos": {
            "labels": [r[0] for r in OOS],
            "subsets": [r[1] for r in OOS],
            "X_oos": X_oos,
            "y_oos_observed": oos_observed,
            "yhat_oos_ols": yhat_oos_ols,
            "yhat_oos_ridge": yhat_oos_ridge,
            "r_pred_ols": r_pred_ols,
            "r_pred_ridge": r_pred_ridge,
            "mae_pred_ols": mae_pred_ols,
            "mae_pred_ridge": mae_pred_ridge,
            "perm_p_ols": p_ols,
            "perm_p_ridge": p_ridge,
            "alpha_bon": 0.05 / 2,
        },
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
