#!/usr/bin/env python3
"""
H-NEW-179 — (α, β)-residual + length features as predictor of muqaṭṭāʿat
letter-set IDENTITY (10-class, 14 labels, 8 singletons).

Pre-reg: findings/phase-b-hypotheses/h-new-179-alpha-beta-predictor-prereg.md

Primary (Bonferroni k=2):
    P1: LOOCV top-1 ≥ 0.50 (baseline H-NEW-88 = 0.414)
    P2: ≥1 singleton letter-set correctly predicted (H-NEW-88 = 0)

Three models:
    (a) 6-feature (α, β, residual, log_length, mean_verse_len, period_medinan)
    (b) 24-feature (6 new + 18 H-NEW-88 structural)
    (c) cheat (MW-5) — adds surah_id as feature, must reach ≥0.52

Classifier: RF (200 est, seed 20260419)
Null: 1000-perm on y, seed 20260419.
"""
from __future__ import annotations

import csv
import json
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np

# Reuse the H-NEW-88 feature-building code
sys.path.insert(0, "/Users/grey/Downloads/quran/scripts")
from h_new_88_letter_set_predictor import (  # noqa: E402
    MUQ_SURAHS, LETTER_SET, LETTER_COUNT, NAME_CLASSES, SURAH_NAME_CLASS,
    PROPHET_NAMED_SURAHS, build_design_matrix as h88_build_design_matrix,
    load_quran, load_revelation, load_asma_names, has_book_ref_in_v1_3,
    divine_name_density, mean_verse_length_chars, strip_punct,
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import LeaveOneOut

# --- locked params ---
SEED = 20260419
N_PERM = 1000

# --- paths ---
ROOT = Path("/Users/grey/Downloads/quran")
ALPHA_BETA_CSV = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-172-per-surah.csv"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-179.json"


# =======================================================================
# Load pre-computed α, β from H-NEW-172 CSV
# =======================================================================
def load_alpha_beta() -> dict[int, dict]:
    """Return {surah_id: {'alpha': float, 'beta': float, 'N': int}} for all
    93 surahs with N ≥ 50."""
    out: dict[int, dict] = {}
    with ALPHA_BETA_CSV.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["surah_id"])
            out[sid] = {
                "alpha": float(row["alpha"]),
                "beta": float(row["beta_h159"]),
                "N": int(row["N"]),
            }
    return out


# =======================================================================
# Fit (α, β) line on 93-surah reference set
# =======================================================================
def fit_alpha_beta_line(ab: dict[int, dict]) -> tuple[float, float]:
    """Fit linear regression α = m*β + c across surahs where both α and β are
    finite (matches H-NEW-178 — some short surahs have NaN β from too-few log-V
    checkpoints).

    Returns (slope m, intercept c)."""
    pairs = []
    for sid in sorted(ab.keys()):
        a = ab[sid]["alpha"]
        b = ab[sid]["beta"]
        if math.isnan(a) or math.isnan(b):
            continue
        pairs.append((b, a))
    n = len(pairs)
    if n < 3:
        raise RuntimeError(f"Too few finite (α, β) pairs: {n}")
    betas = [p[0] for p in pairs]
    alphas = [p[1] for p in pairs]
    mx = sum(betas) / n
    my = sum(alphas) / n
    num = sum((betas[i] - mx) * (alphas[i] - my) for i in range(n))
    den = sum((betas[i] - mx) ** 2 for i in range(n))
    slope = num / den
    intercept = my - slope * mx
    return slope, intercept


def compute_residual(alpha: float, beta: float, slope: float, intercept: float) -> float:
    return alpha - (slope * beta + intercept)


# =======================================================================
# Build design matrices for H-NEW-179
# =======================================================================
def build_new_features_only() -> tuple[np.ndarray, np.ndarray, list[str], list[int]]:
    """6 NEW features only: (alpha, beta, residual, log_length,
    mean_verse_len_chars, period_medinan) per 29 muq surahs."""
    quran = load_quran()
    rev = load_revelation()
    ab = load_alpha_beta()
    slope, intercept = fit_alpha_beta_line(ab)

    rows: list[list[float]] = []
    y: list[str] = []
    surah_ids: list[int] = []
    for sid in MUQ_SURAHS:
        if sid not in ab:
            raise RuntimeError(f"Surah {sid} missing from α/β CSV")
        s = quran[sid]
        r = rev[sid]
        a = ab[sid]["alpha"]
        b = ab[sid]["beta"]
        resid = compute_residual(a, b, slope, intercept)
        log_len = math.log(ab[sid]["N"])
        mvlc = mean_verse_length_chars(s)
        medinan = 1 if r["period"] == "medinan" else 0
        rows.append([a, b, resid, log_len, mvlc, medinan])
        y.append(LETTER_SET[sid])
        surah_ids.append(sid)

    feature_names = [
        "alpha", "beta", "residual", "log_length",
        "mean_verse_length_chars", "period_medinan",
    ]
    X = np.array(rows, dtype=float)
    return X, np.array(y), feature_names, surah_ids


def build_combined_features() -> tuple[np.ndarray, np.ndarray, list[str], list[int]]:
    """24 features = 6 new + 18 H-NEW-88 structural (drop roots + first_word).

    H-NEW-88 18 structural:
      length, period_meccan, noldeke_order, mushaf_index, book_ref_v1_3,
      prophet_named (6)
      + name_class one-hot (9)
      + divine_name_density (1)
      + mean_verse_length_chars (1)
      + letter_count_in_set (1)
      = 18

    Note: mean_verse_length_chars appears in both blocks; we include it in the
    H-NEW-88 block (where it is F11) and DROP it from the 6 new features to
    avoid exact duplication. That gives 5 new + 18 = 23. To preserve the
    pre-registered count of 24 features, we ALSO drop period_medinan (since
    period_meccan = 1 - period_medinan in H-NEW-88). Final layout:

      6 NEW: alpha, beta, residual, log_length, mean_verse_length_chars, period_medinan
        - strip duplicates vs H-NEW-88: drop mean_verse_length_chars, period_medinan
        - → 4 unique NEW features (alpha, beta, residual, log_length)
      18 H-NEW-88 structural: as above
      → 22 features total.

    To hit pre-registered 24 cleanly: we KEEP all 6 new features AS-IS
    (including duplicates) and add the 18 H-NEW-88 STRUCTURAL minus the
    2 duplicates (mean_verse_length_chars, period_meccan) = 16.
    Result: 6 + 16 = 22 features. Still undercount.

    Simplest: KEEP all 24 slots (6+18) INCLUDING known duplicates. RF is
    invariant to duplicate features (they split information). We follow
    the pre-reg's stated 24-feature specification literally.
    """
    # 6 new features (all surahs keyed to MUQ_SURAHS)
    X_new, y, new_names, surah_ids = build_new_features_only()

    # 18 H-NEW-88 structural features (rebuild without roots or first_word)
    quran = load_quran()
    rev = load_revelation()
    asma = load_asma_names()

    rows: list[list[float]] = []
    for sid in MUQ_SURAHS:
        s = quran[sid]
        r = rev[sid]
        length = int(s["total_verses"])
        period_meccan = 1 if r["period"] == "meccan" else 0
        noldeke = int(r["noldeke_order"])
        mushaf = sid
        bookref = has_book_ref_in_v1_3(s)
        prophet = 1 if sid in PROPHET_NAMED_SURAHS else 0
        nc = SURAH_NAME_CLASS.get(sid, "OTHER_ABSTRACT")
        nc_oh = [1 if cls == nc else 0 for cls in NAME_CLASSES]
        dnd = divine_name_density(s, asma)
        mvlc = mean_verse_length_chars(s)
        ls = LETTER_SET[sid]
        lc = LETTER_COUNT[ls]
        row = (
            [length, period_meccan, noldeke, mushaf, bookref, prophet]
            + nc_oh
            + [dnd]
            + [mvlc, lc]
        )
        rows.append(row)

    h88_18_names = (
        ["length", "period_meccan", "noldeke_order", "mushaf_index",
         "book_ref_v1_3", "prophet_named"]
        + [f"name_class_{c}" for c in NAME_CLASSES]
        + ["divine_name_density", "mean_verse_length_chars", "letter_count_in_set"]
    )
    assert len(h88_18_names) == 18, f"expected 18, got {len(h88_18_names)}"

    X_h88 = np.array(rows, dtype=float)
    X_combined = np.hstack([X_new, X_h88])
    names_combined = new_names + h88_18_names
    assert X_combined.shape[1] == 24
    return X_combined, y, names_combined, surah_ids


def build_cheat_features() -> tuple[np.ndarray, np.ndarray, list[str], list[int]]:
    """MW-5: combined 24 features + surah_id (as lookup feature)."""
    X, y, names, surah_ids = build_combined_features()
    X_cheat = np.hstack([X, np.array(surah_ids, dtype=float).reshape(-1, 1)])
    return X_cheat, y, names + ["cheat_surah_id"], surah_ids


# =======================================================================
# LOOCV with RF
# =======================================================================
def loocv_rf(X: np.ndarray, y: np.ndarray,
             seed: int = SEED) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    n = X.shape[0]
    classes_global = np.array(sorted(set(y.tolist())))
    y_pred = np.empty(n, dtype=object)
    proba = np.full((n, len(classes_global)), np.nan, dtype=float)

    loo = LeaveOneOut()
    for train_idx, test_idx in loo.split(X):
        X_tr, X_te = X[train_idx], X[test_idx]
        y_tr = y[train_idx]
        mu = X_tr.mean(axis=0)
        sd = X_tr.std(axis=0)
        sd[sd == 0] = 1.0
        X_tr_s = (X_tr - mu) / sd
        X_te_s = (X_te - mu) / sd
        clf = RandomForestClassifier(
            n_estimators=200, random_state=seed, n_jobs=1,
        )
        clf.fit(X_tr_s, y_tr)
        local_classes = clf.classes_
        p = clf.predict_proba(X_te_s)[0]
        for j, cls in enumerate(local_classes):
            gi = int(np.where(classes_global == cls)[0][0])
            proba[test_idx[0], gi] = p[j]
        top1_idx = int(np.argmax(p))
        y_pred[test_idx[0]] = local_classes[top1_idx]
    return y_pred, proba, classes_global


def topk_accuracy(y_true: np.ndarray, proba: np.ndarray,
                  classes_global: np.ndarray, k: int) -> float:
    n = len(y_true)
    correct = 0
    for i in range(n):
        scores = proba[i].copy()
        scores[np.isnan(scores)] = -np.inf
        topk_idx = np.argsort(scores)[::-1][:k]
        topk_labels = classes_global[topk_idx]
        if y_true[i] in topk_labels:
            correct += 1
    return correct / n


# =======================================================================
# Permutation null
# =======================================================================
def _one_perm(args):
    """Run one permutation for joblib.Parallel.

    args = (X, y, observed_acc, seed_k, perm_k)"""
    X, y, observed_acc, perm_seed = args
    rng = np.random.default_rng(perm_seed)
    y_perm = rng.permutation(y)
    try:
        y_pred, _, _ = loocv_rf(X, y_perm, seed=SEED)
        acc = float(accuracy_score(y_perm, y_pred))
    except Exception:
        acc = 1.0 / len(set(y))
    return acc


def permutation_null(X: np.ndarray, y: np.ndarray,
                     observed_acc: float, n_perm: int, seed: int) -> dict:
    try:
        from joblib import Parallel, delayed
    except ImportError:
        Parallel = None  # type: ignore

    # Pre-generate per-perm seeds from master rng for reproducibility
    master_rng = np.random.default_rng(seed)
    perm_seeds = master_rng.integers(0, 2**31 - 1, size=n_perm).tolist()
    args_list = [(X, y, observed_acc, s) for s in perm_seeds]

    if Parallel is not None:
        # Parallel over perms, each fit single-threaded
        perm_accs = Parallel(n_jobs=-1, verbose=5)(
            delayed(_one_perm)(a) for a in args_list
        )
        perm_accs = list(perm_accs)
    else:
        perm_accs = []
        for i, a in enumerate(args_list):
            perm_accs.append(_one_perm(a))
            if (i + 1) % 100 == 0:
                print(f"    perm {i+1}/{n_perm}  "
                      f"mean={np.mean(perm_accs):.4f}")

    perm_accs_np = np.array(perm_accs)
    ge = int((perm_accs_np >= observed_acc).sum())
    return {
        "n_perm": n_perm,
        "p_value": (1 + ge) / (n_perm + 1),
        "perm_acc_mean": float(perm_accs_np.mean()),
        "perm_acc_std": float(perm_accs_np.std()),
        "perm_acc_max": float(perm_accs_np.max()),
        "perm_acc_q95": float(np.quantile(perm_accs_np, 0.95)),
        "perm_acc_q99": float(np.quantile(perm_accs_np, 0.99)),
        "ge_count": int(ge),
    }


# =======================================================================
# Main
# =======================================================================
def describe_singletons(y: np.ndarray, y_pred: np.ndarray,
                        surah_ids: list[int]) -> dict:
    """Identify which of the 8 singleton letter-sets were correctly predicted."""
    counts = Counter(y.tolist())
    singletons = [cls for cls, n in counts.items() if n == 1]
    # Sanity: H-NEW-88 had 8 singletons + TSM (n=2)
    hits = []
    misses = []
    for i in range(len(y)):
        if y[i] in singletons:
            (hits if y[i] == y_pred[i] else misses).append({
                "surah_id": int(surah_ids[i]),
                "true_set": str(y[i]),
                "pred_set": str(y_pred[i]),
            })
    return {
        "singletons": singletons,
        "n_singletons": len(singletons),
        "singleton_hits": hits,
        "singleton_hits_count": len(hits),
        "singleton_misses": misses,
    }


def run_model(X: np.ndarray, y: np.ndarray,
              feature_names: list[str], surah_ids: list[int],
              model_tag: str, do_perm: bool) -> dict:
    print(f"\n=== Model: {model_tag}  (X.shape={X.shape}) ===")
    y_pred, proba, classes_global = loocv_rf(X, y, seed=SEED)
    acc1 = float(accuracy_score(y, y_pred))
    acc3 = topk_accuracy(y, proba, classes_global, k=3)
    acc5 = topk_accuracy(y, proba, classes_global, k=5)
    print(f"  LOOCV top-1: {acc1:.4f}  top-3: {acc3:.4f}  top-5: {acc5:.4f}")

    # per-set recall
    labels_sorted = sorted(set(y))
    per_set_recall = {}
    for cls in labels_sorted:
        mask = (y == cls)
        if mask.sum() > 0:
            per_set_recall[cls] = float((y_pred[mask] == cls).sum() / mask.sum())

    # singleton diagnostic
    singleton_info = describe_singletons(y, y_pred, surah_ids)
    print(f"  Singleton hits: {singleton_info['singleton_hits_count']}/"
          f"{singleton_info['n_singletons']}: "
          f"{[h['true_set'] for h in singleton_info['singleton_hits']]}")

    # per-surah predictions
    per_surah = [
        {"surah_id": int(surah_ids[i]),
         "true_set": str(y[i]),
         "pred_set": str(y_pred[i]),
         "correct": bool(y[i] == y_pred[i])}
        for i in range(len(y))
    ]

    # feature importance from full-data model
    mu = X.mean(axis=0); sd = X.std(axis=0); sd[sd == 0] = 1.0
    Xs = (X - mu) / sd
    clf_full = RandomForestClassifier(
        n_estimators=200, random_state=SEED, n_jobs=1,
    )
    clf_full.fit(Xs, y)
    feat_imp = sorted(
        zip(feature_names, clf_full.feature_importances_.tolist()),
        key=lambda kv: kv[1], reverse=True,
    )
    print("  Top-8 features:")
    for nm, v in feat_imp[:8]:
        print(f"    {nm:32s}  {v:.4f}")

    result = {
        "model_tag": model_tag,
        "n_features": X.shape[1],
        "feature_names": feature_names,
        "loocv_top1": acc1,
        "loocv_top3": acc3,
        "loocv_top5": acc5,
        "per_set_recall": per_set_recall,
        "singleton_info": singleton_info,
        "per_surah_predictions": per_surah,
        "feature_importance_top20": [
            {"feature": nm, "importance": v} for nm, v in feat_imp[:20]
        ],
    }

    if do_perm:
        print(f"  Running permutation null (n={N_PERM})...")
        perm = permutation_null(X, y, acc1, N_PERM, SEED)
        print(f"  perm mean={perm['perm_acc_mean']:.4f}  "
              f"q95={perm['perm_acc_q95']:.4f}  max={perm['perm_acc_max']:.4f}")
        print(f"  p = {perm['p_value']:.4f}")
        result["permutation_null"] = perm

    return result


def main():
    print("H-NEW-179 — (α, β)-residual predictor for letter-set IDENTITY")
    print(f"Seed: {SEED}")
    print()

    # Build feature matrices
    print("[Build] 6-new-feature matrix...")
    X6, y, names6, surah_ids = build_new_features_only()
    print(f"  shape = {X6.shape}, labels = {Counter(y.tolist())}")

    print("[Build] 24-feature combined matrix...")
    X24, _, names24, _ = build_combined_features()
    print(f"  shape = {X24.shape}")

    print("[Build] 25-feature cheat (MW-5) matrix...")
    Xcheat, _, names_cheat, _ = build_cheat_features()
    print(f"  shape = {Xcheat.shape}")

    # Baselines
    chance = 1.0 / len(set(y))
    maj_class = Counter(y.tolist()).most_common(1)[0][0]
    maj_acc = sum(1 for v in y if v == maj_class) / len(y)
    print(f"\n  Baseline chance (1/{len(set(y))}): {chance:.4f}")
    print(f"  Baseline majority ({maj_class}): {maj_acc:.4f}")
    print(f"  Baseline H-NEW-88 RF top-1: 0.4138")
    print(f"  Structural ceiling: 0.6552")

    results = {}

    # -- MW-5 cheat (validate pipeline) --
    print("\n" + "=" * 70)
    print("MW-5: cheat_surah_id validation (must reach >= 0.52)")
    print("=" * 70)
    res_cheat = run_model(Xcheat, y, names_cheat, surah_ids,
                          "cheat_mw5", do_perm=False)
    mw5_pass = res_cheat["loocv_top1"] >= 0.52
    print(f"  MW-5 top-1 = {res_cheat['loocv_top1']:.4f}; PASS? {mw5_pass}")
    results["mw5"] = res_cheat
    results["mw5_pass"] = mw5_pass

    # -- 6-feature only (descriptive secondary) --
    print("\n" + "=" * 70)
    print("6-feature model (α, β, residual, log_length, mvlc, medinan)")
    print("=" * 70)
    res6 = run_model(X6, y, names6, surah_ids, "six_new_features",
                     do_perm=True)
    results["six_feature"] = res6

    # -- 24-feature combined (PRIMARY) --
    print("\n" + "=" * 70)
    print("24-feature combined (PRIMARY)")
    print("=" * 70)
    res24 = run_model(X24, y, names24, surah_ids, "combined_24",
                      do_perm=True)
    results["combined_24"] = res24

    # -- Verdict --
    primary = res24
    acc_primary = primary["loocv_top1"]
    singleton_hits = primary["singleton_info"]["singleton_hits_count"]
    perm_p = primary["permutation_null"]["p_value"]

    p1_pass = acc_primary >= 0.50
    p2_pass = singleton_hits >= 1
    alpha_bon = 0.05 / 2
    p1_sig = perm_p < alpha_bon

    if p1_pass and p1_sig and p2_pass:
        verdict = "FULL-PASS (OQ-1 first positive since project inception)"
    elif p1_pass and p1_sig:
        verdict = "P1-ONLY (primary accuracy; no singleton hit)"
    elif p2_pass:
        verdict = "P2-ONLY (singleton hit but primary <0.50)"
    elif acc_primary <= maj_acc or perm_p >= 0.05:
        verdict = "NULL"
    else:
        verdict = "INCONCLUSIVE"

    print("\n" + "=" * 70)
    print(f"VERDICT: {verdict}")
    print("=" * 70)
    print(f"  Primary 24-feature top-1: {acc_primary:.4f}  "
          f"(threshold 0.50) pass={p1_pass}")
    print(f"  Perm p: {perm_p:.4f}  (α_bon={alpha_bon}) pass={p1_sig}")
    print(f"  Singleton hits: {singleton_hits}  (threshold 1) pass={p2_pass}")
    print(f"  Baseline H-NEW-88: 0.4138")
    print(f"  Δ over baseline: {acc_primary - 0.4138:+.4f}")

    out = {
        "id": "H-NEW-179",
        "title": "(α, β)-residual + length predictor for letter-set IDENTITY",
        "seed": SEED,
        "n_surahs": len(MUQ_SURAHS),
        "n_classes": len(set(y.tolist())),
        "baseline_uniform_chance": chance,
        "baseline_majority_acc": maj_acc,
        "baseline_h_new_88_rf_top1": 0.4138,
        "structural_ceiling": 0.6552,
        "primary_threshold": 0.50,
        "secondary_threshold_singletons": 1,
        "bonferroni_k": 2,
        "alpha_family": 0.05,
        "alpha_bon": alpha_bon,
        "letter_set_distribution": dict(Counter(y.tolist())),
        "results": results,
        "verdict": verdict,
        "pass_cells": {
            "p1_primary_acc_gte_0_50": bool(p1_pass),
            "p1_perm_p_lt_alpha_bon": bool(p1_sig),
            "p2_singleton_hits_gte_1": bool(p2_pass),
        },
        "deltas_vs_baseline": {
            "combined_24_minus_h88": acc_primary - 0.4138,
            "six_feature_minus_h88": res6["loocv_top1"] - 0.4138,
        },
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
