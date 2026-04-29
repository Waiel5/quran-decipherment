#!/usr/bin/env python3
"""
H-NEW-55 — Multi-axis muqaṭṭaʿāt classifier (LOOCV)

Pre-registered features (locked before training):
  F1: surah length (verse count)
  F2: period_meccan (1 if Meccan, 0 if Medinan)
  F3: noldeke_order
  F4: book_ref_v1_3 (1 if k-t-b or q-r-ʾ form in v1-3)
  F5: prophet_named (conservative list per H-NEW-49.1)
  F6: mushaf_index

Procedure: logistic regression with LOOCV.
Null: 1000-permutation y-shuffle.
PASS: AUC > 0.80 AND perm p < 0.01.
MW-5 sanity: planted-signal control must yield > 0.95 AUC.
Seed: 20260416.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import LeaveOneOut

# ---------- locked constants ----------

SEED = 20260416
N_PERM = 1000

QURAN_JSON = Path("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json")
REVELATION_CSV = Path("/Users/grey/Downloads/quran/data/revelation-order.csv")

OUTPUT_JSON = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-55.json")

# Locked muqaṭṭaʿāt set (29 surahs)
MUQ_SURAHS = frozenset({
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68
})
assert len(MUQ_SURAHS) == 29

# Locked prophet-named set per H-NEW-49.1 (conservative)
PROPHET_NAMED_SURAHS = frozenset({10, 11, 12, 14, 19, 31, 47, 71})
assert len(PROPHET_NAMED_SURAHS) == 8

# Book-reference substring lists per H-NEW-53
KITAB_FORMS = [
    "كتاب", "كتب", "الكتاب", "الكتب",
    "كتابك", "كتابه", "كتابي", "كتابهم", "كتابا",
]
QURAN_FORMS = [
    "قرآن", "القرآن", "قرءان", "القرءان",
    "قرءن", "قرآنا", "قرآنه",
]


# ---------- data loaders ----------

def load_quran() -> dict[int, dict]:
    with QURAN_JSON.open() as f:
        data = json.load(f)
    by_id = {}
    for s in data:
        by_id[int(s["id"])] = s
    assert len(by_id) == 114
    return by_id


def load_revelation() -> dict[int, dict]:
    """Map mushaf_order -> {period, noldeke_order}."""
    by_mushaf = {}
    with REVELATION_CSV.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            m = int(row["mushaf_order"])
            by_mushaf[m] = {
                "period": row["period"].strip().lower(),
                "noldeke_order": int(row["noldeke_order"]),
            }
    assert len(by_mushaf) == 114
    return by_mushaf


def has_book_ref_in_v1_3(surah: dict) -> int:
    """Return 1 if any k-t-b or q-r-ʾ form found in verses 1-3."""
    verses = surah["verses"][:3]
    for v in verses:
        text = v["text"]
        for form in KITAB_FORMS:
            if form in text:
                return 1
        for form in QURAN_FORMS:
            if form in text:
                return 1
    return 0


# ---------- feature matrix ----------

def build_design_matrix() -> tuple[np.ndarray, np.ndarray, list[str]]:
    quran = load_quran()
    rev = load_revelation()

    rows = []
    y = []
    for sid in range(1, 115):
        s = quran[sid]
        r = rev[sid]
        length = int(s["total_verses"])
        period_meccan = 1 if r["period"] == "meccan" else 0
        noldeke = int(r["noldeke_order"])
        bookref = has_book_ref_in_v1_3(s)
        prophet = 1 if sid in PROPHET_NAMED_SURAHS else 0
        mushaf = sid
        rows.append([length, period_meccan, noldeke, bookref, prophet, mushaf])
        y.append(1 if sid in MUQ_SURAHS else 0)

    X = np.array(rows, dtype=float)
    y = np.array(y, dtype=int)
    feature_names = [
        "length",
        "period_meccan",
        "noldeke_order",
        "book_ref_v1_3",
        "prophet_named",
        "mushaf_index",
    ]
    return X, y, feature_names


# ---------- LOOCV ----------

def loocv_predictions(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Returns per-surah hold-out probability of class=1."""
    n = X.shape[0]
    preds = np.zeros(n, dtype=float)
    loo = LeaveOneOut()
    for train_idx, test_idx in loo.split(X):
        X_tr, X_te = X[train_idx], X[test_idx]
        y_tr = y[train_idx]
        # standardize continuous columns (0,2,5) on training fold only
        mu = X_tr.mean(axis=0)
        sd = X_tr.std(axis=0)
        sd[sd == 0] = 1.0
        # only standardize continuous (binary cols stay as-is for interpretability)
        cont_mask = np.array([True, False, True, False, False, True])
        X_tr_s = X_tr.copy()
        X_te_s = X_te.copy()
        X_tr_s[:, cont_mask] = (X_tr[:, cont_mask] - mu[cont_mask]) / sd[cont_mask]
        X_te_s[:, cont_mask] = (X_te[:, cont_mask] - mu[cont_mask]) / sd[cont_mask]
        clf = LogisticRegression(
            C=1.0, solver="liblinear", class_weight="balanced",
            max_iter=1000, random_state=SEED,
        )
        clf.fit(X_tr_s, y_tr)
        preds[test_idx[0]] = clf.predict_proba(X_te_s)[0, 1]
    return preds


def fit_full_model(X: np.ndarray, y: np.ndarray):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd[sd == 0] = 1.0
    cont_mask = np.array([True, False, True, False, False, True])
    Xs = X.copy()
    Xs[:, cont_mask] = (X[:, cont_mask] - mu[cont_mask]) / sd[cont_mask]
    clf = LogisticRegression(
        C=1.0, solver="liblinear", class_weight="balanced",
        max_iter=1000, random_state=SEED,
    )
    clf.fit(Xs, y)
    return clf


# ---------- permutation null ----------

def permutation_null(X: np.ndarray, y: np.ndarray, observed_auc: float, n_perm: int) -> dict:
    rng = np.random.default_rng(SEED)
    perm_aucs = []
    ge_count = 0
    for k in range(n_perm):
        y_perm = rng.permutation(y)
        try:
            preds = loocv_predictions(X, y_perm)
            auc = roc_auc_score(y_perm, preds)
        except ValueError:
            auc = 0.5
        perm_aucs.append(auc)
        if auc >= observed_auc:
            ge_count += 1
    perm_aucs = np.array(perm_aucs)
    p = (1 + ge_count) / (n_perm + 1)
    return {
        "n_perm": n_perm,
        "p_value": float(p),
        "perm_auc_mean": float(perm_aucs.mean()),
        "perm_auc_std": float(perm_aucs.std()),
        "perm_auc_max": float(perm_aucs.max()),
        "perm_auc_q95": float(np.quantile(perm_aucs, 0.95)),
        "perm_auc_q99": float(np.quantile(perm_aucs, 0.99)),
        "ge_count": int(ge_count),
    }


# ---------- MW-5 planted signal control ----------

def mw5_control() -> float:
    """Build a 114×6 dataset with 3 informative features and 3 noise.
    Run the SAME LOOCV pipeline. Must produce AUC > 0.95.
    """
    rng = np.random.default_rng(SEED + 1)
    n = 114
    # planted y matches our class distribution
    y = np.zeros(n, dtype=int)
    muq_idx = rng.choice(n, size=29, replace=False)
    y[muq_idx] = 1
    # 3 informative features (correlated with y)
    f1 = y * 2.5 + rng.normal(0, 1, n)  # strong continuous
    f2 = (y == 1).astype(int) ^ (rng.random(n) < 0.10).astype(int)  # binary, 90% match
    f3 = y * 1.8 + rng.normal(0, 1, n)
    # 3 noise
    f4 = rng.normal(0, 1, n)
    f5 = rng.integers(0, 2, n)
    f6 = rng.normal(0, 1, n)
    X = np.column_stack([f1, f2, f3, f4, f5, f6])
    preds = loocv_predictions(X, y)
    return float(roc_auc_score(y, preds))


# ---------- main ----------

def main():
    # Step 0: MW-5 control
    print("Running MW-5 planted-signal control...")
    mw5_auc = mw5_control()
    print(f"  MW-5 AUC = {mw5_auc:.4f} (must be > 0.95)")
    if mw5_auc <= 0.95:
        print("MW-5 FAILED — pipeline is broken.")
        sys.exit(1)

    # Step 1: build design matrix
    print("\nBuilding design matrix...")
    X, y, feature_names = build_design_matrix()
    print(f"  X.shape = {X.shape}; n_muq = {y.sum()}; n_non_muq = {(y == 0).sum()}")

    # Step 2: per-surah feature audit
    audit = {}
    for col, name in enumerate(feature_names):
        audit[name] = {
            "mean": float(X[:, col].mean()),
            "min": float(X[:, col].min()),
            "max": float(X[:, col].max()),
            "muq_mean": float(X[y == 1, col].mean()),
            "non_muq_mean": float(X[y == 0, col].mean()),
        }
    print("\nFeature audit:")
    for k, v in audit.items():
        print(f"  {k}: muq_mean={v['muq_mean']:.3f}  non_muq_mean={v['non_muq_mean']:.3f}")

    # Step 3: LOOCV
    print("\nRunning LOOCV...")
    preds = loocv_predictions(X, y)
    auc = float(roc_auc_score(y, preds))
    yhat = (preds >= 0.5).astype(int)
    acc = float(accuracy_score(y, yhat))
    pr_muq, rc_muq, f1_muq, _ = precision_recall_fscore_support(
        y, yhat, average="binary", pos_label=1, zero_division=0
    )
    pr_non, rc_non, f1_non, _ = precision_recall_fscore_support(
        y, yhat, average="binary", pos_label=0, zero_division=0
    )
    print(f"  AUC = {auc:.4f}")
    print(f"  Accuracy @ 0.5 = {acc:.4f}")
    print(f"  Muq precision={pr_muq:.3f} recall={rc_muq:.3f} f1={f1_muq:.3f}")
    print(f"  Non-muq precision={pr_non:.3f} recall={rc_non:.3f} f1={f1_non:.3f}")

    # Step 4: feature importance from full-data model
    full_clf = fit_full_model(X, y)
    coefs = full_clf.coef_[0]
    intercept = float(full_clf.intercept_[0])
    feat_imp = sorted(
        zip(feature_names, coefs.tolist()),
        key=lambda kv: abs(kv[1]),
        reverse=True,
    )
    print("\nFeature coefficients (full-data model, standardized continuous):")
    for nm, c in feat_imp:
        print(f"  {nm}: {c:+.4f}")
    print(f"  intercept: {intercept:+.4f}")

    # Step 5: permutation null
    print(f"\nRunning permutation null (n={N_PERM})...")
    perm = permutation_null(X, y, auc, N_PERM)
    print(f"  perm AUC mean={perm['perm_auc_mean']:.4f}  std={perm['perm_auc_std']:.4f}")
    print(f"  perm AUC q95={perm['perm_auc_q95']:.4f}  q99={perm['perm_auc_q99']:.4f}  max={perm['perm_auc_max']:.4f}")
    print(f"  p-value = {perm['p_value']:.5f}  (ge_count={perm['ge_count']}/{N_PERM})")

    # Step 6: verdict
    pass_auc = auc > 0.80
    pass_p = perm["p_value"] < 0.01
    pass_mw5 = mw5_auc > 0.95
    overall_pass = pass_auc and pass_p and pass_mw5
    strong = auc > 0.90
    if overall_pass and strong:
        verdict = "STRONG-PASS"
    elif overall_pass:
        verdict = "PASS"
    else:
        verdict = "FAIL"
    print(f"\nVERDICT: {verdict}")
    print(f"  AUC > 0.80? {pass_auc}")
    print(f"  perm p < 0.01? {pass_p}")
    print(f"  MW-5 > 0.95? {pass_mw5}")

    # Step 7: per-surah predictions
    per_surah = []
    for i in range(114):
        per_surah.append({
            "surah": i + 1,
            "y": int(y[i]),
            "y_hat": int(yhat[i]),
            "p_muq": float(preds[i]),
            "length": float(X[i, 0]),
            "period_meccan": int(X[i, 1]),
            "noldeke_order": int(X[i, 2]),
            "book_ref_v1_3": int(X[i, 3]),
            "prophet_named": int(X[i, 4]),
            "mushaf_index": int(X[i, 5]),
        })

    # Step 8: write JSON
    out = {
        "id": "H-NEW-55",
        "title": "Multi-axis muqaṭṭaʿāt classifier (LOOCV)",
        "seed": SEED,
        "n": int(X.shape[0]),
        "n_muq": int(y.sum()),
        "n_non_muq": int((y == 0).sum()),
        "feature_names": feature_names,
        "mw5_control_auc": mw5_auc,
        "auc": auc,
        "accuracy_at_0_5": acc,
        "muq_precision": float(pr_muq),
        "muq_recall": float(rc_muq),
        "muq_f1": float(f1_muq),
        "non_muq_precision": float(pr_non),
        "non_muq_recall": float(rc_non),
        "non_muq_f1": float(f1_non),
        "full_model_coefficients": {nm: float(c) for nm, c in zip(feature_names, coefs)},
        "full_model_intercept": intercept,
        "feature_importance_ranked": [{"feature": nm, "coef": c} for nm, c in feat_imp],
        "feature_audit": audit,
        "permutation_null": perm,
        "pass_criterion": {
            "auc_gt_0_80": bool(pass_auc),
            "perm_p_lt_0_01": bool(pass_p),
            "mw5_gt_0_95": bool(pass_mw5),
            "overall_pass": bool(overall_pass),
            "strong_pass": bool(strong and overall_pass),
        },
        "verdict": verdict,
        "per_surah_predictions": per_surah,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
