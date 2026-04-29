#!/usr/bin/env python3
"""
H-NEW-96.2 — Rhyme-feature predictor for muqaṭṭaʿāt letter-set identity.

Pre-registered in:
  findings/phase-b-hypotheses/h-new-96-2-rhyme-predictor-prereg.md

Goal: test whether the 14-dim rhyme one-hot vector (per muq-letter: is letter L
in top-3 verse-final letters of surah s) predicts the surah's letter-set
identity at LOOCV top-1 > 0.414 (H-NEW-88 baseline).

Primary classifier: RandomForest. Secondary: Logistic. Both LOOCV, 1000 perms.

Data anchor: H-NEW-139 top-3 rhyme table (29 surahs). Sanity-checked before
training.

Seed: 20260417 (same as H-NEW-96 parent).
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

SEED = 20260417
np.random.seed(SEED)

QURAN_JSON = Path("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json")
OUTPUT_JSON = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-96-2.json")

# --- Muqaṭṭaʿāt canonical assignments (29 surahs, 14 letter-sets) ---
MUQ_ASSIGNMENTS = {
    2: "ALM", 3: "ALM", 29: "ALM", 30: "ALM", 31: "ALM", 32: "ALM",
    7: "ALMS",
    10: "ALR", 11: "ALR", 12: "ALR", 14: "ALR", 15: "ALR",
    13: "ALMR",
    19: "KHYAS",
    20: "TH",
    26: "TSM", 28: "TSM",
    27: "TS",
    36: "YS",
    38: "S",
    40: "HM", 41: "HM", 43: "HM", 44: "HM", 45: "HM", 46: "HM",
    42: "HMASQ",
    50: "Q",
    68: "N",
}
MUQ_SURAHS = sorted(MUQ_ASSIGNMENTS.keys())
assert len(MUQ_SURAHS) == 29

# --- Canonical muq letter vocabulary (14 distinct letters across all muq sets) ---
MUQ_LETTERS = ["ا", "ل", "م", "ر", "ص", "ك", "ه", "ي", "ع", "ط", "س", "ح", "ن", "ق"]
assert len(MUQ_LETTERS) == 14

# --- H-NEW-139 published top-3 rhyme table (canonical expectation; used for sanity-check) ---
# Per finding file (29 surahs, each: top-3 verse-final letters excl. v1)
HNEW139_EXPECTED_TOP3 = {
    2: {"ن", "م", "ر"},
    3: {"ن", "م", "ر"},
    7: {"ن", "م", "ل"},
    10: {"ن", "م", "ل"},
    11: {"ن", "د", "ب"},
    12: {"ن", "م", "ر"},
    13: {"ب", "ر", "ل"},
    14: {"ر", "د", "م"},
    15: {"ن", "م", "ل"},
    19: {"ا", "ن", "م"},
    20: {"ى", "ا", "ي"},
    26: {"ن", "م", "ل"},
    27: {"ن", "م", "۩"},
    28: {"ن", "م", "ل"},
    29: {"ن", "م", "ر"},
    30: {"ن", "م", "ر"},
    31: {"ر", "م", "ن"},
    32: {"ن", "م", "۩"},
    36: {"ن", "م"},  # only 2 dominant
    38: {"ب", "ن", "ر"},
    40: {"ن", "ب", "ر"},
    41: {"ن", "م", "د"},
    42: {"ر", "م", "ن"},
    43: {"ن", "م", "ل"},
    44: {"ن", "م"},
    45: {"ن", "م"},
    46: {"ن", "م", "ر"},
    50: {"د", "ب", "ج"},
    68: {"ن", "م"},
}


def extract_top3_rhyme(surah_verses: list[dict], exclude_v1: bool = True) -> set[str]:
    """Extract top-3 verse-final letters of a surah, excluding v1 if muq-opened."""
    finals: list[str] = []
    for v in surah_verses:
        if exclude_v1 and v["id"] == 1:
            continue
        text = v["text"].strip()
        if not text:
            continue
        # Skip trailing punctuation if any; take last character
        last_char = text[-1]
        finals.append(last_char)
    if not finals:
        return set()
    counts = Counter(finals)
    # Top-3 by count (ties broken by alphabetical order for determinism)
    sorted_letters = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    top3 = {letter for letter, _ in sorted_letters[:3]}
    return top3


def build_rhyme_features(quran: list[dict]) -> tuple[np.ndarray, dict[int, set[str]]]:
    """Build 29 × 14 rhyme one-hot matrix. Returns (X, observed_top3_per_surah)."""
    X = np.zeros((len(MUQ_SURAHS), len(MUQ_LETTERS)), dtype=np.int8)
    observed = {}
    for i, sid in enumerate(MUQ_SURAHS):
        surah = quran[sid - 1]
        assert surah["id"] == sid
        top3 = extract_top3_rhyme(surah["verses"], exclude_v1=True)
        observed[sid] = top3
        for j, letter in enumerate(MUQ_LETTERS):
            X[i, j] = 1 if letter in top3 else 0
    return X, observed


def loocv(X: np.ndarray, y: np.ndarray, clf_factory, k_top: list[int] = [1, 3, 5]):
    n = X.shape[0]
    preds = np.empty(n, dtype=object)
    topk_correct = {k: 0 for k in k_top}
    topk_probs = []
    classes_sorted = sorted(set(y.tolist()))
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        X_train, y_train = X[mask], y[mask]
        X_test = X[i : i + 1]
        mu = X_train.mean(axis=0)
        sd = X_train.std(axis=0)
        sd[sd == 0] = 1.0
        X_train_s = (X_train - mu) / sd
        X_test_s = (X_test - mu) / sd
        clf = clf_factory()
        clf.fit(X_train_s, y_train)
        pred = clf.predict(X_test_s)[0]
        preds[i] = pred
        # Top-K via predict_proba
        try:
            probs = clf.predict_proba(X_test_s)[0]
            classes_local = list(clf.classes_)
            ranked = sorted(zip(classes_local, probs), key=lambda kv: -kv[1])
            ranked_classes = [c for c, _ in ranked]
            for k in k_top:
                if y[i] in ranked_classes[:k]:
                    topk_correct[k] += 1
        except Exception:
            if y[i] == pred:
                for k in k_top:
                    topk_correct[k] += 1
    acc = {f"top{k}": topk_correct[k] / n for k in k_top}
    return preds, acc


def per_class_recall(y: np.ndarray, preds: np.ndarray) -> dict[str, float]:
    recall = {}
    classes = sorted(set(y.tolist()))
    for c in classes:
        idx = np.where(y == c)[0]
        if len(idx) == 0:
            continue
        correct = sum(preds[i] == c for i in idx)
        recall[c] = correct / len(idx)
    return recall


def per_singleton_result(y: np.ndarray, preds: np.ndarray) -> tuple[dict, int]:
    singleton_labels = ["S", "Q", "N", "TH", "YS", "TS", "KHYAS", "HMASQ"]
    per_sing = {}
    hits = 0
    for i, sid in enumerate(MUQ_SURAHS):
        if y[i] in singleton_labels:
            correct = y[i] == preds[i]
            per_sing[str(sid)] = {"true": str(y[i]), "pred": str(preds[i]), "correct": bool(correct)}
            if correct:
                hits += 1
    return per_sing, hits


def permutation_null(X: np.ndarray, y: np.ndarray, clf_factory, n_perm: int = 1000, seed: int = SEED):
    rng = np.random.default_rng(seed)
    null_top1 = []
    for p in range(n_perm):
        y_sh = y.copy()
        rng.shuffle(y_sh)
        preds_sh, acc_sh = loocv(X, y_sh, clf_factory, k_top=[1])
        null_top1.append(acc_sh["top1"])
        if (p + 1) % 100 == 0:
            print(f"  perm {p+1}/{n_perm}", flush=True)
    null_top1 = np.array(null_top1)
    return null_top1


def main() -> None:
    print("H-NEW-96.2 RHYME predictor — loading data …", flush=True)
    with QURAN_JSON.open() as f:
        quran = json.load(f)

    print("Building rhyme features (29 × 14) …", flush=True)
    X, observed_top3 = build_rhyme_features(quran)

    # Sanity-check vs H-NEW-139 published table
    print("Sanity-check: observed top-3 vs H-NEW-139 published table …", flush=True)
    mismatches = 0
    for sid in MUQ_SURAHS:
        obs = observed_top3[sid]
        exp = HNEW139_EXPECTED_TOP3.get(sid, set())
        # Note: we only care about the intersection with MUQ_LETTERS for feature purposes;
        # but sanity-check the raw top-3 match count.
        shared = obs & exp
        if len(shared) < 1 and exp:
            mismatches += 1
            print(f"  MISMATCH Q{sid}: observed={obs}, expected={exp}")
    print(f"  {29 - mismatches}/29 surahs have ≥1 shared top-3 letter with H-NEW-139 table", flush=True)

    y_labels = [MUQ_ASSIGNMENTS[s] for s in MUQ_SURAHS]
    y = np.array(y_labels)
    classes_sorted = sorted(set(y_labels))
    n_classes = len(classes_sorted)
    print(f"y classes: {classes_sorted}", flush=True)
    print(f"X shape: {X.shape}  y shape: {y.shape}  n_classes={n_classes}", flush=True)

    # Baselines
    counter_y = Counter(y_labels)
    majority_class = counter_y.most_common(1)[0][0]
    majority_acc = counter_y[majority_class] / len(y_labels)
    chance_uniform = 1.0 / n_classes
    print(f"Baseline uniform: {chance_uniform:.4f}  majority ({majority_class}): {majority_acc:.4f}", flush=True)

    # --- MW-5 positive control: cheat_surah_id ---
    print("MW-5 positive control (cheat_surah_id alone) …", flush=True)
    X_cheat = np.array(MUQ_SURAHS, dtype=float).reshape(-1, 1)
    preds_cheat, acc_cheat = loocv(
        X_cheat, y,
        lambda: RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1),
        k_top=[1, 3, 5],
    )
    print(f"  MW-5 top-1 (cheat) = {acc_cheat['top1']:.4f}", flush=True)

    results = {}
    for clf_name, clf_factory in [
        ("rf", lambda: RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1)),
        ("logistic", lambda: LogisticRegression(C=1.0, solver="lbfgs", max_iter=2000, random_state=SEED)),
    ]:
        print(f"\n=== {clf_name.upper()} LOOCV ===", flush=True)
        preds, acc = loocv(X, y, clf_factory, k_top=[1, 3, 5])
        print(f"  top-1={acc['top1']:.4f}  top-3={acc['top3']:.4f}  top-5={acc['top5']:.4f}", flush=True)
        pcr = per_class_recall(y, preds)
        print(f"  per-class recall: {pcr}", flush=True)
        per_sing, n_sing_hits = per_singleton_result(y, preds)
        print(f"  singleton hits: {n_sing_hits}/8", flush=True)

        print(f"  Permutation null (1000 perms) …", flush=True)
        null_top1 = permutation_null(X, y, clf_factory, n_perm=1000, seed=SEED)
        observed_top1 = acc["top1"]
        p_perm = float((null_top1 >= observed_top1).sum() + 1) / (len(null_top1) + 1)
        print(f"  perm null mean={null_top1.mean():.4f} q95={np.quantile(null_top1, 0.95):.4f} max={null_top1.max():.4f}", flush=True)
        print(f"  p (≥ obs) = {p_perm:.4f}", flush=True)

        # Feature importance from full-data model
        mu = X.mean(axis=0)
        sd = X.std(axis=0)
        sd[sd == 0] = 1.0
        Xs = (X - mu) / sd
        if clf_name == "logistic":
            clf_full = LogisticRegression(C=1.0, solver="lbfgs", max_iter=2000, random_state=SEED)
            clf_full.fit(Xs, y)
            mean_abs = np.mean(np.abs(clf_full.coef_), axis=0)
            feat_imp = sorted(zip(MUQ_LETTERS, mean_abs.tolist()), key=lambda kv: -kv[1])
        else:
            clf_full = RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1)
            clf_full.fit(Xs, y)
            feat_imp = sorted(zip(MUQ_LETTERS, clf_full.feature_importances_.tolist()), key=lambda kv: -kv[1])

        results[clf_name] = {
            "loocv_top1": acc["top1"],
            "loocv_top3": acc["top3"],
            "loocv_top5": acc["top5"],
            "per_class_recall": pcr,
            "per_singleton_results": per_sing,
            "n_singleton_hits": n_sing_hits,
            "permutation_null": {
                "observed_top1": observed_top1,
                "null_mean": float(null_top1.mean()),
                "null_std": float(null_top1.std()),
                "null_q95": float(np.quantile(null_top1, 0.95)),
                "null_max": float(null_top1.max()),
                "n_perm": 1000,
                "p_value": p_perm,
            },
            "feature_importance": [{"letter": L, "importance": v} for L, v in feat_imp],
            "per_surah_predictions": [
                {
                    "surah": int(MUQ_SURAHS[i]),
                    "true_set": str(y[i]),
                    "pred_set": str(preds[i]),
                    "correct": bool(y[i] == preds[i]),
                }
                for i in range(len(y))
            ],
        }

    # Verdict
    rf = results["rf"]
    top1 = rf["loocv_top1"]
    p_prim = rf["permutation_null"]["p_value"]
    n_sing = rf["n_singleton_hits"]
    hnew88_baseline = 0.4138

    pass_primary = (top1 > hnew88_baseline) and (p_prim < 0.025)
    pass_strong = (top1 > 0.50) and (p_prim < 0.025)
    oq1_progress = n_sing >= 1

    if pass_strong and oq1_progress:
        verdict = "JOINT-PASS"
    elif pass_strong:
        verdict = "PASS-STRONG"
    elif pass_primary:
        verdict = "PASS"
    else:
        verdict = "NULL"

    print(f"\n=== VERDICT: {verdict} ===", flush=True)
    print(f"  top-1 = {top1:.4f} (H-NEW-88 baseline = 0.4138)", flush=True)
    print(f"  perm p = {p_prim:.4f}", flush=True)
    print(f"  singleton hits = {n_sing}/8 (OQ-1 progress = {oq1_progress})", flush=True)

    out = {
        "id": "H-NEW-96.2",
        "title": "Rhyme-feature predictor for muqaṭṭaʿāt letter-set identity",
        "seed": SEED,
        "parent_baseline": "H-NEW-88",
        "parent_baseline_top1": hnew88_baseline,
        "parent_extension_null": "H-NEW-96",
        "data_anchor": "H-NEW-139",
        "n_surahs": len(MUQ_SURAHS),
        "n_classes": n_classes,
        "n_features": X.shape[1],
        "muq_letters": MUQ_LETTERS,
        "muq_assignments": {str(k): v for k, v in MUQ_ASSIGNMENTS.items()},
        "observed_top3_per_surah": {str(k): sorted(list(v)) for k, v in observed_top3.items()},
        "hnew139_sanity_mismatches": mismatches,
        "mw5_positive_control_top1": acc_cheat["top1"],
        "baseline_uniform_chance": chance_uniform,
        "baseline_majority_class": str(majority_class),
        "baseline_majority_accuracy": majority_acc,
        "results_by_classifier": results,
        "verdict": verdict,
        "verdict_criteria": {
            "pass_primary_threshold": f"top-1 > {hnew88_baseline} AND perm p < 0.025",
            "pass_strong_threshold": "top-1 > 0.50 AND perm p < 0.025",
            "oq1_progress_threshold": ">= 1 of 8 singletons correctly predicted",
            "pass_primary_met": bool(pass_primary),
            "pass_strong_met": bool(pass_strong),
            "oq1_progress_met": bool(oq1_progress),
        },
        "bonferroni_family": "h-new-96-2-rhyme-predictor",
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUTPUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
