#!/usr/bin/env python3
"""H-NEW-183 — Predict Nöldeke rank from per-surah compositional features.

Pre-reg: findings/phase-b-hypotheses/h-new-183-chronology-predictor-prereg.md

Pipeline
--------
  1. Assemble 12-feature matrix X (114 x 12) from H-NEW-123 (per-surah β/K),
     H-NEW-125 (per-surah 15 axes), H-NEW-168 (per-surah dispersion),
     with NaN-imputation to feature median.
  2. Target y = Nöldeke rank (from data/revelation-order.csv).
  3. Ridge full, Ridge length-only baseline, RF full — LOOCV.
  4. Permutation null for Ridge full: 500 perms of y, seed 20260419.
  5. 80/20 holdout MW-5 split (seed 20260419) for Ridge full.
  6. Emit JSON.

Writes findings/phase-b-hypotheses/csv/h-new-183.json.
"""
from __future__ import annotations

import csv
import json
import math
import random
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold, LeaveOneOut, train_test_split
from sklearn.preprocessing import StandardScaler

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
N_PERM = 500


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_noldeke_rank() -> Dict[int, int]:
    """surah_id -> noldeke_order (1..114)."""
    path = ROOT / "data" / "revelation-order.csv"
    out: Dict[int, int] = {}
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                mushaf = int(row["mushaf_order"])
                nold = int(row["noldeke_order"])
            except (ValueError, KeyError):
                continue
            out[mushaf] = nold
    return out


def load_heap() -> Dict[int, Dict]:
    """surah_id -> {N, beta, K}."""
    path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-123.json"
    d = json.load(path.open())
    out: Dict[int, Dict] = {}
    for row in d["per_surah_full"]:
        sid = int(row["surah_id"])
        out[sid] = {
            "N": row["N"],
            "beta": row["beta"],
            "K": row["K"],
        }
    return out


def load_h125() -> Dict[int, Dict]:
    """surah_id -> dict of axis values."""
    path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-125.json"
    d = json.load(path.open())
    out: Dict[int, Dict] = {}
    for sid_str, rec in d["per_surah_axis_values"].items():
        sid = int(sid_str)
        out[sid] = rec["axis_values"]
    return out


def load_dispersion() -> Dict[int, float]:
    """surah_id -> dispersion."""
    path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-168-per-surah-dispersion.csv"
    out: Dict[int, float] = {}
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                sid = int(row["sid"])
                disp = float(row["dispersion"])
            except (ValueError, KeyError):
                continue
            out[sid] = disp
    return out


# ---------------------------------------------------------------------------
# Feature matrix
# ---------------------------------------------------------------------------
FEATURE_NAMES = [
    "alpha",            # proxy: log(K)
    "beta",
    "alpha_minus_beta",
    "log_length",
    "mean_verse_len",
    "allah_density",
    "qul_density",
    "book_ref_density",
    "loanword_density",
    "eschat_density",
    "dispersion",
    "muq_cardinality",
]


def _safe_log(x: float) -> float:
    if x is None or (isinstance(x, float) and (math.isnan(x) or x <= 0)):
        return float("nan")
    return math.log(x)


def build_feature_matrix() -> Tuple[np.ndarray, np.ndarray, List[int], List[str]]:
    heap = load_heap()
    h125 = load_h125()
    disp = load_dispersion()
    noldeke = load_noldeke_rank()

    sids = sorted(noldeke.keys())
    X_rows = []
    y = []
    for sid in sids:
        h = heap.get(sid, {})
        a = h125.get(sid, {})
        beta = h.get("beta", float("nan"))
        K = h.get("K", float("nan"))
        N = h.get("N", float("nan"))
        log_K = _safe_log(K)
        log_N = _safe_log(N)
        beta_v = beta if beta is not None else float("nan")
        if beta_v is None:
            beta_v = float("nan")
        alpha_proxy = log_K
        alpha_minus_beta = (
            alpha_proxy - beta_v
            if not (math.isnan(alpha_proxy) or (isinstance(beta_v, float) and math.isnan(beta_v)))
            else float("nan")
        )
        row = [
            alpha_proxy,
            beta_v if beta_v is not None else float("nan"),
            alpha_minus_beta,
            log_N,
            a.get("mean_verse_length", float("nan")),
            a.get("allah_density", float("nan")),
            a.get("qul_density", float("nan")),
            a.get("book_reference_density", float("nan")),
            a.get("loanword_density", float("nan")),
            a.get("eschatological_density", float("nan")),
            disp.get(sid, float("nan")),
            a.get("muq_cardinality", float("nan")),
        ]
        X_rows.append(row)
        y.append(noldeke[sid])

    X = np.array(X_rows, dtype=float)
    y_arr = np.array(y, dtype=float)
    return X, y_arr, sids, FEATURE_NAMES


def impute_median(X: np.ndarray, medians: np.ndarray | None = None) -> Tuple[np.ndarray, np.ndarray]:
    X2 = X.copy()
    if medians is None:
        medians = np.nanmedian(X2, axis=0)
    inds = np.where(np.isnan(X2))
    X2[inds] = np.take(medians, inds[1])
    return X2, medians


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------
def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    ss_res = float(np.sum((y_true - y_pred) ** 2))
    ss_tot = float(np.sum((y_true - y_true.mean()) ** 2))
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))


def spearman_rho(a: np.ndarray, b: np.ndarray) -> float:
    from scipy.stats import spearmanr

    rho, _ = spearmanr(a, b)
    return float(rho)


# ---------------------------------------------------------------------------
# LOOCV
# ---------------------------------------------------------------------------
def loocv_ridge(X: np.ndarray, y: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    n = X.shape[0]
    preds = np.zeros(n, dtype=float)
    loo = LeaveOneOut()
    for train_idx, test_idx in loo.split(X):
        X_train = X[train_idx]
        X_test = X[test_idx]
        y_train = y[train_idx]
        # Impute missing on training-only medians, apply to test
        X_train_i, meds = impute_median(X_train)
        X_test_i, _ = impute_median(X_test, medians=meds)
        scaler = StandardScaler().fit(X_train_i)
        X_train_s = scaler.transform(X_train_i)
        X_test_s = scaler.transform(X_test_i)
        model = Ridge(alpha=alpha, random_state=SEED)
        model.fit(X_train_s, y_train)
        preds[test_idx] = model.predict(X_test_s)
    return preds


def loocv_rf(X: np.ndarray, y: np.ndarray, n_estimators: int = 500) -> np.ndarray:
    n = X.shape[0]
    preds = np.zeros(n, dtype=float)
    loo = LeaveOneOut()
    for train_idx, test_idx in loo.split(X):
        X_train_i, meds = impute_median(X[train_idx])
        X_test_i, _ = impute_median(X[test_idx], medians=meds)
        model = RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=None,
            random_state=SEED,
            n_jobs=1,
        )
        model.fit(X_train_i, y[train_idx])
        preds[test_idx] = model.predict(X_test_i)
    return preds


# ---------------------------------------------------------------------------
# Permutation null (Ridge full)
# ---------------------------------------------------------------------------
def permutation_null_ridge(X: np.ndarray, y: np.ndarray, n_perm: int = N_PERM,
                           seed: int = SEED) -> Dict:
    rng = np.random.default_rng(seed)
    null_r2 = np.zeros(n_perm, dtype=float)
    for k in range(n_perm):
        y_perm = y[rng.permutation(len(y))]
        preds = loocv_ridge(X, y_perm)
        null_r2[k] = r2_score(y_perm, preds)
    return {
        "null_r2_mean": float(null_r2.mean()),
        "null_r2_std": float(null_r2.std(ddof=0)),
        "null_r2_95": float(np.percentile(null_r2, 95)),
        "null_r2_975": float(np.percentile(null_r2, 97.5)),
        "null_r2_max": float(null_r2.max()),
        "null_r2_samples": null_r2.tolist(),
    }


# ---------------------------------------------------------------------------
# 80/20 holdout
# ---------------------------------------------------------------------------
def holdout_8020(X: np.ndarray, y: np.ndarray, alpha: float = 1.0, seed: int = SEED) -> Dict:
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=seed)
    X_tr_i, meds = impute_median(X_tr)
    X_te_i, _ = impute_median(X_te, medians=meds)
    scaler = StandardScaler().fit(X_tr_i)
    X_tr_s = scaler.transform(X_tr_i)
    X_te_s = scaler.transform(X_te_i)
    model = Ridge(alpha=alpha, random_state=seed)
    model.fit(X_tr_s, y_tr)
    preds = model.predict(X_te_s)
    return {
        "n_train": int(len(y_tr)),
        "n_test": int(len(y_te)),
        "r2_test": r2_score(y_te, preds),
        "mae_test": mae(y_te, preds),
        "spearman_test": spearman_rho(y_te, preds),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    np.random.seed(SEED)
    random.seed(SEED)

    X_full, y, sids, names = build_feature_matrix()
    X_length_only = X_full[:, [names.index("log_length")]]

    # Descriptive: fraction missing
    missing = np.isnan(X_full).sum(axis=0).tolist()

    # Model A: Ridge full
    preds_A = loocv_ridge(X_full, y)
    r2_A = r2_score(y, preds_A)
    mae_A = mae(y, preds_A)
    rho_A = spearman_rho(y, preds_A)

    # Model B: Ridge length-only
    preds_B = loocv_ridge(X_length_only, y)
    r2_B = r2_score(y, preds_B)
    mae_B = mae(y, preds_B)
    rho_B = spearman_rho(y, preds_B)

    # Model C: RF full
    preds_C = loocv_rf(X_full, y)
    r2_C = r2_score(y, preds_C)
    mae_C = mae(y, preds_C)
    rho_C = spearman_rho(y, preds_C)

    # Feature importances via single-fit RF on full data (training-median imputation)
    X_imp, _ = impute_median(X_full)
    rf_full = RandomForestRegressor(
        n_estimators=500, max_depth=None, random_state=SEED, n_jobs=1
    )
    rf_full.fit(X_imp, y)
    rf_imp = rf_full.feature_importances_.tolist()
    # Ridge coefficients on scaled features (full fit)
    scaler_full = StandardScaler().fit(X_imp)
    X_imp_s = scaler_full.transform(X_imp)
    ridge_full = Ridge(alpha=1.0, random_state=SEED).fit(X_imp_s, y)
    ridge_coefs = ridge_full.coef_.tolist()

    # Permutation feature importance on ridge (fit+score on full data)
    perm_res = permutation_importance(
        ridge_full, X_imp_s, y, n_repeats=30, random_state=SEED, scoring="r2"
    )
    ridge_perm_imp = perm_res.importances_mean.tolist()

    # Permutation null for Ridge full
    null = permutation_null_ridge(X_full, y, n_perm=N_PERM, seed=SEED)
    # One-sided p: P(null R2 >= observed)
    null_samples = np.array(null["null_r2_samples"], dtype=float)
    p_perm = float((np.sum(null_samples >= r2_A) + 1) / (len(null_samples) + 1))

    # 80/20 holdout (MW-5)
    holdout = holdout_8020(X_full, y, alpha=1.0, seed=SEED)

    # Pre-reg tests
    # H1: R2_full > R2_baseline AND p_perm < 0.025
    H1 = bool(r2_A > r2_B and p_perm < 0.025)
    # H2: MAE < 15
    H2 = bool(mae_A < 15.0)

    # Per-surah predictions (full model)
    per_surah_preds = [
        {
            "surah_id": int(sids[i]),
            "noldeke_rank": int(y[i]),
            "pred_full": float(preds_A[i]),
            "pred_length_only": float(preds_B[i]),
            "pred_rf": float(preds_C[i]),
            "residual_full": float(y[i] - preds_A[i]),
        }
        for i in range(len(sids))
    ]

    out = {
        "id": "H-NEW-183",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_family": "h-new-183-chronology-predictor",
        "bonferroni_k": 2,
        "alpha_fam": 0.05,
        "alpha_test": 0.025,
        "n_surahs": int(len(sids)),
        "feature_names": names,
        "feature_n_missing_before_impute": missing,
        "model_A_ridge_full": {
            "r2_loocv": r2_A,
            "mae_loocv": mae_A,
            "spearman_loocv": rho_A,
            "ridge_alpha": 1.0,
        },
        "model_B_ridge_length_only": {
            "r2_loocv": r2_B,
            "mae_loocv": mae_B,
            "spearman_loocv": rho_B,
            "features": ["log_length"],
        },
        "model_C_rf_full": {
            "r2_loocv": r2_C,
            "mae_loocv": mae_C,
            "spearman_loocv": rho_C,
            "n_estimators": 500,
        },
        "ridge_full_fit_coefs_on_scaled": dict(zip(names, ridge_coefs)),
        "ridge_perm_importance_full": dict(zip(names, ridge_perm_imp)),
        "rf_full_feature_importance": dict(zip(names, rf_imp)),
        "permutation_null_ridge_full": {
            "n_perm": N_PERM,
            "null_r2_mean": null["null_r2_mean"],
            "null_r2_std": null["null_r2_std"],
            "null_r2_95": null["null_r2_95"],
            "null_r2_975": null["null_r2_975"],
            "null_r2_max": null["null_r2_max"],
            "p_one_sided": p_perm,
        },
        "mw5_holdout_8020": holdout,
        "H1_full_beats_baseline_and_p_lt_0p025": H1,
        "H2_mae_lt_15": H2,
        "verdict": (
            "CHRONOLOGY-QUANTITATIVE" if (H1 and H2)
            else "PARTIAL" if H1
            else "LENGTH-DRIVEN" if H2
            else "NULL"
        ),
        "per_surah_predictions": per_surah_preds,
    }

    out_path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-183.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))
    print(f"Wrote {out_path}")
    print("Verdict:", out["verdict"])
    print(f"Ridge full: R2={r2_A:.4f}  MAE={mae_A:.2f}  rho={rho_A:.3f}")
    print(f"Ridge length-only: R2={r2_B:.4f}  MAE={mae_B:.2f}  rho={rho_B:.3f}")
    print(f"RF full: R2={r2_C:.4f}  MAE={mae_C:.2f}  rho={rho_C:.3f}")
    print(f"Perm null: mean={null['null_r2_mean']:.4f} 97.5%={null['null_r2_975']:.4f} "
          f"p_obs={p_perm:.4g}")
    print(f"H1={H1}  H2={H2}")
    print(f"MW-5 holdout: R2_test={holdout['r2_test']:.4f} MAE_test={holdout['mae_test']:.2f}")


if __name__ == "__main__":
    main()
