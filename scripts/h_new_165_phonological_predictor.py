#!/usr/bin/env python3
"""
H-NEW-165 — Classical-Arabic phonological-feature predictor for muqaṭṭaʿāt letter-set.

Pre-reg: findings/phase-b-hypotheses/h-new-165-phonological-predictor-prereg.md
Parent baselines:
  H-NEW-88   (content features, RF LOOCV top-1 = 0.4138, perm p = 0.002)
  H-NEW-96   (92-feature content extension NULL, top-1 = 0.379)
  H-NEW-96.2 (14-feature rhyme NULL, top-1 = 0.310)

OQ-1 attack: phonological-axis predictor. Encode each muq letter with classical
tajwīd features (makhraj, ṣifa, tafkhīm, idhlāq) and predict letter-set identity
for 29 muq surahs under LOOCV.

Seed: 20260419.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

SEED = 20260419
N_PERM = 1000

OUTPUT_JSON = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-165.json")

# ---------- canonical muq letter-set assignment (29 surahs, 14 distinct sets) ----------

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
assert len(set(MUQ_ASSIGNMENTS.values())) == 14

# Each letter-set decomposed into its Arabic letters (canonical spellings)
SET_LETTERS = {
    "ALM":   ["ا", "ل", "م"],
    "ALMS":  ["ا", "ل", "م", "ص"],
    "ALR":   ["ا", "ل", "ر"],
    "ALMR":  ["ا", "ل", "م", "ر"],
    "KHYAS": ["ك", "ه", "ي", "ع", "ص"],
    "TH":    ["ط", "ه"],
    "TSM":   ["ط", "س", "م"],
    "TS":    ["ط", "س"],
    "YS":    ["ي", "س"],
    "S":     ["ص"],
    "HM":    ["ح", "م"],
    "HMASQ": ["ح", "م", "ع", "س", "ق"],
    "Q":     ["ق"],
    "N":     ["ن"],
}
assert set(SET_LETTERS.keys()) == set(MUQ_ASSIGNMENTS.values())

# The 14 distinct muq letters
MUQ_LETTERS = sorted(set().union(*SET_LETTERS.values()))
# Must have 14 letters per project-level constant
assert len(MUQ_LETTERS) == 14, f"Expected 14 muq letters, got {len(MUQ_LETTERS)}: {MUQ_LETTERS}"

# 8-task-spec singleton letter-sets (OQ-1 target for secondary)
TASK_SINGLETONS_8 = {"S", "Q", "N", "TH", "YS", "TS", "KHYAS", "HMASQ"}

# ---------- classical tajwīd phonological feature codebook (LOCKED) ----------
#
# Features per letter (9-dim per-letter table):
#   makhraj   ∈ {1..8} — al-Khalīl 8-tier back-to-front ordinal
#                 1=labial, 2=labio-dental, 3=alveolar/dental, 4=palatal,
#                 5=velar, 6=uvular, 7=pharyngeal, 8=glottal
#   voice     ∈ {0=hams/voiceless, 1=jahr/voiced}  (classical majhūra table)
#   manner    ∈ {0=vowel/carrier, 1=stop, 2=fricative, 3=glide, 4=lateral,
#                5=nasal, 6=trill}
#   emphatic  ∈ {0,1}  — 7 ḥurūf al-tafkhīm = {خ, ص, ض, ط, ظ, غ, ق}
#   pharyngeal ∈ {0,1} — mustaʿliya ∪ pharyngeals: {خ, ص, ض, ط, ظ, غ, ق, ع, ح}
#   sonorant  ∈ {0,1}  — {ا, ل, م, ر, ي, ن, و}
#   continuant ∈ {0,1} — opposed to stops; stops = {ك, ط, ق, ب, د, ت, ء, ج}
#   idhlāq    ∈ {0,1}  — al-Khalīl 6 fluent letters = {ف, ر, م, ن, ل, ب}
#   vowel_carrier ∈ {0,1} — weak letters {ا, ي, و}

LETTER_FEATURES = {
    "ا": {"makhraj": 8, "voice": 1, "manner": 0, "emphatic": 0, "pharyngeal": 0, "sonorant": 1, "continuant": 1, "idhlaq": 0, "vowel_carrier": 1},
    "ل": {"makhraj": 3, "voice": 1, "manner": 4, "emphatic": 0, "pharyngeal": 0, "sonorant": 1, "continuant": 1, "idhlaq": 1, "vowel_carrier": 0},
    "م": {"makhraj": 1, "voice": 1, "manner": 5, "emphatic": 0, "pharyngeal": 0, "sonorant": 1, "continuant": 1, "idhlaq": 1, "vowel_carrier": 0},
    "ر": {"makhraj": 3, "voice": 1, "manner": 6, "emphatic": 0, "pharyngeal": 0, "sonorant": 1, "continuant": 1, "idhlaq": 1, "vowel_carrier": 0},
    "ص": {"makhraj": 3, "voice": 0, "manner": 2, "emphatic": 1, "pharyngeal": 1, "sonorant": 0, "continuant": 1, "idhlaq": 0, "vowel_carrier": 0},
    "ك": {"makhraj": 5, "voice": 0, "manner": 1, "emphatic": 0, "pharyngeal": 0, "sonorant": 0, "continuant": 0, "idhlaq": 0, "vowel_carrier": 0},
    "ه": {"makhraj": 8, "voice": 0, "manner": 2, "emphatic": 0, "pharyngeal": 0, "sonorant": 0, "continuant": 1, "idhlaq": 0, "vowel_carrier": 0},
    "ي": {"makhraj": 4, "voice": 1, "manner": 3, "emphatic": 0, "pharyngeal": 0, "sonorant": 1, "continuant": 1, "idhlaq": 0, "vowel_carrier": 1},
    "ع": {"makhraj": 7, "voice": 1, "manner": 2, "emphatic": 0, "pharyngeal": 1, "sonorant": 0, "continuant": 1, "idhlaq": 0, "vowel_carrier": 0},
    "ط": {"makhraj": 3, "voice": 1, "manner": 1, "emphatic": 1, "pharyngeal": 1, "sonorant": 0, "continuant": 0, "idhlaq": 0, "vowel_carrier": 0},
    "س": {"makhraj": 3, "voice": 0, "manner": 2, "emphatic": 0, "pharyngeal": 0, "sonorant": 0, "continuant": 1, "idhlaq": 0, "vowel_carrier": 0},
    "ح": {"makhraj": 7, "voice": 0, "manner": 2, "emphatic": 0, "pharyngeal": 1, "sonorant": 0, "continuant": 1, "idhlaq": 0, "vowel_carrier": 0},
    "ن": {"makhraj": 3, "voice": 1, "manner": 5, "emphatic": 0, "pharyngeal": 0, "sonorant": 1, "continuant": 1, "idhlaq": 1, "vowel_carrier": 0},
    "ق": {"makhraj": 6, "voice": 0, "manner": 1, "emphatic": 1, "pharyngeal": 1, "sonorant": 0, "continuant": 0, "idhlaq": 0, "vowel_carrier": 0},
}
# Sanity: every muq letter has features defined
for L in MUQ_LETTERS:
    assert L in LETTER_FEATURES, f"Missing feature row for {L}"

PER_LETTER_FEATURE_NAMES = [
    "makhraj", "voice", "manner", "emphatic", "pharyngeal",
    "sonorant", "continuant", "idhlaq", "vowel_carrier",
]

# Qalqala letters (classical bouncing stops): {ق, ط, ب, ج, د}
# In muq alphabet: {ق, ط}
QALQALA_LETTERS = {"ق", "ط"}

# ---------- feature-matrix builder ----------

def letter_set_features(letter_set_name: str) -> tuple[list[float], list[str]]:
    """Given letter-set name (e.g. 'ALM'), return feature vector and names."""
    letters = SET_LETTERS[letter_set_name]
    n = len(letters)

    # Per-letter means (9 features)
    means = []
    for fname in PER_LETTER_FEATURE_NAMES:
        vals = [LETTER_FEATURES[L][fname] for L in letters]
        means.append(float(np.mean(vals)))

    # Aggregate features
    letter_count = float(n)

    frac_emphatic = float(sum(LETTER_FEATURES[L]["emphatic"] for L in letters) / n)
    frac_pharyngeal = float(sum(LETTER_FEATURES[L]["pharyngeal"] for L in letters) / n)
    frac_sonorant = float(sum(LETTER_FEATURES[L]["sonorant"] for L in letters) / n)
    frac_idhlaq = float(sum(LETTER_FEATURES[L]["idhlaq"] for L in letters) / n)
    has_qalqala = float(1 if any(L in QALQALA_LETTERS for L in letters) else 0)

    fv = means + [letter_count, frac_emphatic, frac_pharyngeal,
                  frac_sonorant, frac_idhlaq, has_qalqala]
    fn = (
        [f"mean_{f}" for f in PER_LETTER_FEATURE_NAMES]
        + ["letter_count", "frac_emphatic", "frac_pharyngeal",
           "frac_sonorant", "frac_idhlaq", "has_qalqala"]
    )
    assert len(fv) == 15
    assert len(fn) == 15
    return fv, fn


def build_design_matrix() -> tuple[np.ndarray, np.ndarray, list[str], list[int]]:
    rows = []
    y = []
    surah_ids = []
    feature_names = None
    for sid in MUQ_SURAHS:
        ls = MUQ_ASSIGNMENTS[sid]
        fv, fn = letter_set_features(ls)
        if feature_names is None:
            feature_names = fn
        rows.append(fv)
        y.append(ls)
        surah_ids.append(sid)
    X = np.array(rows, dtype=float)
    return X, np.array(y), feature_names, surah_ids


# ---------- LOOCV ----------

def loocv(X, y, clf_factory, k_top=(1, 3, 5)):
    n = X.shape[0]
    preds = np.empty(n, dtype=object)
    topk_correct = {k: 0 for k in k_top}
    classes_global = np.array(sorted(set(y.tolist())))
    proba_matrix = np.full((n, len(classes_global)), np.nan, dtype=float)

    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        X_tr, y_tr = X[mask], y[mask]
        X_te = X[i : i + 1]
        mu = X_tr.mean(axis=0)
        sd = X_tr.std(axis=0)
        sd[sd == 0] = 1.0
        X_tr_s = (X_tr - mu) / sd
        X_te_s = (X_te - mu) / sd

        clf = clf_factory()
        clf.fit(X_tr_s, y_tr)
        try:
            probs = clf.predict_proba(X_te_s)[0]
            classes_local = list(clf.classes_)
            # Top-1
            top1_idx = int(np.argmax(probs))
            preds[i] = classes_local[top1_idx]
            # Record proba
            for j, cls in enumerate(classes_local):
                gi = int(np.where(classes_global == cls)[0][0])
                proba_matrix[i, gi] = probs[j]
            # Top-k
            ranked = sorted(zip(classes_local, probs), key=lambda kv: -kv[1])
            ranked_classes = [c for c, _ in ranked]
            for k in k_top:
                if y[i] in ranked_classes[:k]:
                    topk_correct[k] += 1
        except Exception:
            pred = clf.predict(X_te_s)[0]
            preds[i] = pred
            if y[i] == pred:
                for k in k_top:
                    topk_correct[k] += 1
    acc = {f"top{k}": topk_correct[k] / n for k in k_top}
    return preds, acc, proba_matrix, classes_global


def per_class_recall(y, preds):
    recall = {}
    for c in sorted(set(y.tolist())):
        idx = np.where(y == c)[0]
        if len(idx) == 0:
            continue
        recall[c] = float(sum(preds[i] == c for i in idx) / len(idx))
    return recall


def per_singleton_result(y, preds, surah_ids):
    per_sing = {}
    hits = 0
    for i, sid in enumerate(surah_ids):
        if y[i] in TASK_SINGLETONS_8:
            correct = bool(y[i] == preds[i])
            per_sing[str(sid)] = {"true": str(y[i]), "pred": str(preds[i]), "correct": correct}
            if correct:
                hits += 1
    return per_sing, hits


def permutation_null(X, y, clf_factory, observed_top1, surah_ids, n_perm=N_PERM, seed=SEED):
    rng = np.random.default_rng(seed)
    null_top1 = []
    ge_count = 0
    singleton_hit_ge1 = 0
    for p in range(n_perm):
        y_sh = y.copy()
        rng.shuffle(y_sh)
        try:
            preds_sh, acc_sh, _, _ = loocv(X, y_sh, clf_factory, k_top=(1,))
            t1 = acc_sh["top1"]
            n_sing = 0
            for i, sid in enumerate(surah_ids):
                if y_sh[i] in TASK_SINGLETONS_8 and preds_sh[i] == y_sh[i]:
                    n_sing += 1
        except Exception:
            t1 = 1.0 / len(set(y))
            n_sing = 0
        null_top1.append(t1)
        if t1 >= observed_top1:
            ge_count += 1
        if n_sing >= 1:
            singleton_hit_ge1 += 1
        if (p + 1) % 100 == 0:
            print(f"  perm {p+1}/{n_perm} mean={np.mean(null_top1):.4f} ge={ge_count} sing_ge1={singleton_hit_ge1}", flush=True)
    null_top1 = np.array(null_top1)
    p_top1 = (1 + ge_count) / (n_perm + 1)
    p_sing = (1 + singleton_hit_ge1) / (n_perm + 1)
    return {
        "n_perm": n_perm,
        "observed_top1": float(observed_top1),
        "p_value_primary": float(p_top1),
        "p_value_singleton_hit": float(p_sing),
        "null_mean": float(null_top1.mean()),
        "null_std": float(null_top1.std()),
        "null_q95": float(np.quantile(null_top1, 0.95)),
        "null_q99": float(np.quantile(null_top1, 0.99)),
        "null_max": float(null_top1.max()),
        "ge_count": int(ge_count),
        "singleton_hit_ge1_count": int(singleton_hit_ge1),
    }


# ---------- main ----------

def main() -> None:
    print("=== H-NEW-165 Classical-Arabic Phonological Predictor ===", flush=True)
    print(f"Seed: {SEED}", flush=True)
    X, y, feature_names, surah_ids = build_design_matrix()
    print(f"X shape: {X.shape}; feature_names = {feature_names}", flush=True)
    print(f"y distribution: {Counter(y.tolist())}", flush=True)

    n_classes = len(set(y.tolist()))
    chance_uniform = 1.0 / n_classes
    majority_class = Counter(y.tolist()).most_common(1)[0][0]
    majority_acc = sum(1 for v in y if v == majority_class) / len(y)
    print(f"chance_uniform = {chance_uniform:.4f}; majority ({majority_class}) = {majority_acc:.4f}", flush=True)

    # Print the design matrix for transparency
    print("\n--- Design matrix (29 rows × 15 features) ---", flush=True)
    for i, sid in enumerate(surah_ids):
        print(f"  Q{sid:>3} {y[i]:<6} {X[i].round(3).tolist()}", flush=True)

    # --- MW-5 positive control ---
    print("\n=== MW-5 positive control (cheat_surah_id) ===", flush=True)
    X_cheat = np.array(surah_ids, dtype=float).reshape(-1, 1)
    preds_cheat, acc_cheat, _, _ = loocv(
        X_cheat, y,
        lambda: RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1),
        k_top=(1, 3, 5),
    )
    mw5_top1 = acc_cheat["top1"]
    print(f"  MW-5 cheat_surah_id RF LOOCV top-1 = {mw5_top1:.4f}", flush=True)
    print(f"  H-NEW-96 structural ceiling = 0.517; expecting ~0.45-0.55", flush=True)

    # Structural multi-member ceiling
    multi_member_ceiling = sum(1 for v in y if Counter(y.tolist())[v] >= 2) / len(y)
    print(f"  structural_multi_member_ceiling = {multi_member_ceiling:.4f}", flush=True)

    results = {}
    for clf_name, clf_factory in [
        ("rf", lambda: RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1)),
        ("logistic", lambda: LogisticRegression(C=1.0, solver="lbfgs", max_iter=2000, random_state=SEED)),
    ]:
        print(f"\n=== {clf_name.upper()} LOOCV ===", flush=True)
        preds, acc, proba, classes_global = loocv(X, y, clf_factory, k_top=(1, 3, 5))
        top1 = acc["top1"]
        print(f"  top-1 = {top1:.4f}  top-3 = {acc['top3']:.4f}  top-5 = {acc['top5']:.4f}", flush=True)
        pcr = per_class_recall(y, preds)
        print(f"  per-class recall: {pcr}", flush=True)
        per_sing, n_sing_hits = per_singleton_result(y, preds, surah_ids)
        print(f"  singleton hits: {n_sing_hits}/8", flush=True)
        print(f"  per-singleton detail:", flush=True)
        for sid_str, detail in per_sing.items():
            print(f"    Q{sid_str:>3} true={detail['true']:<6} pred={detail['pred']:<6} correct={detail['correct']}", flush=True)

        # Permutation null
        if clf_name == "rf":
            print(f"  Running permutation null (n={N_PERM})…", flush=True)
            perm = permutation_null(X, y, clf_factory, top1, surah_ids, n_perm=N_PERM)
            print(f"  perm null mean={perm['null_mean']:.4f} q95={perm['null_q95']:.4f} max={perm['null_max']:.4f}", flush=True)
            print(f"  p_primary = {perm['p_value_primary']:.4f}", flush=True)
            print(f"  p_singleton_hit = {perm['p_value_singleton_hit']:.4f}", flush=True)
        else:
            perm = None

        # Feature importance (full-data fit)
        mu = X.mean(axis=0); sd = X.std(axis=0); sd[sd == 0] = 1.0
        Xs = (X - mu) / sd
        if clf_name == "logistic":
            clf_full = LogisticRegression(C=1.0, solver="lbfgs", max_iter=2000, random_state=SEED)
            clf_full.fit(Xs, y)
            mean_abs = np.mean(np.abs(clf_full.coef_), axis=0)
            feat_imp = sorted(zip(feature_names, mean_abs.tolist()), key=lambda kv: -kv[1])
        else:
            clf_full = RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1)
            clf_full.fit(Xs, y)
            feat_imp = sorted(zip(feature_names, clf_full.feature_importances_.tolist()), key=lambda kv: -kv[1])

        results[clf_name] = {
            "loocv_top1": top1,
            "loocv_top3": acc["top3"],
            "loocv_top5": acc["top5"],
            "per_class_recall": pcr,
            "per_singleton_results": per_sing,
            "n_singleton_hits": n_sing_hits,
            "permutation_null": perm,
            "feature_importance": [{"feature": nm, "importance": v} for nm, v in feat_imp],
            "per_surah_predictions": [
                {
                    "surah": int(surah_ids[i]),
                    "true_set": str(y[i]),
                    "pred_set": str(preds[i]),
                    "correct": bool(y[i] == preds[i]),
                }
                for i in range(len(y))
            ],
        }

    # --- Verdict ---
    rf = results["rf"]
    top1 = rf["loocv_top1"]
    p_prim = rf["permutation_null"]["p_value_primary"]
    n_sing = rf["n_singleton_hits"]
    HNEW88_BASELINE = 0.4138
    PRIMARY_THRESHOLD = 0.50
    ALPHA_BON = 0.025

    pass_primary = (top1 > PRIMARY_THRESHOLD) and (p_prim < ALPHA_BON)
    pass_secondary = n_sing >= 1
    pass_weak = (top1 > HNEW88_BASELINE) and (p_prim < 0.05)

    if pass_primary and pass_secondary:
        verdict = "JOINT-PASS"
    elif pass_primary:
        verdict = "PASS-PRIMARY"
    elif pass_secondary:
        verdict = "PASS-SECONDARY"
    elif pass_weak:
        verdict = "PASS-WEAK"
    else:
        verdict = "NULL"

    pipeline_ok = mw5_top1 >= 0.45
    if not pipeline_ok:
        verdict = "NULL-BROKEN-PIPELINE"

    print(f"\n=== VERDICT: {verdict} ===", flush=True)
    print(f"  RF top-1 = {top1:.4f} (H-NEW-88 baseline = {HNEW88_BASELINE}; primary threshold = {PRIMARY_THRESHOLD})", flush=True)
    print(f"  perm p = {p_prim:.4f} (alpha_bon = {ALPHA_BON})", flush=True)
    print(f"  singleton hits = {n_sing}/8 (OQ-1 progress = {pass_secondary})", flush=True)
    print(f"  MW-5 = {mw5_top1:.4f} (pipeline_ok = {pipeline_ok})", flush=True)

    out = {
        "id": "H-NEW-165",
        "title": "Classical-Arabic phonological-feature predictor for muqaṭṭaʿāt letter-set",
        "seed": SEED,
        "parent_baseline": "H-NEW-88",
        "parent_baseline_top1": HNEW88_BASELINE,
        "parent_null_1": "H-NEW-96",
        "parent_null_2": "H-NEW-96.2",
        "n_surahs": len(MUQ_SURAHS),
        "n_classes": n_classes,
        "n_features": X.shape[1],
        "feature_names": feature_names,
        "muq_letters": MUQ_LETTERS,
        "set_letters": SET_LETTERS,
        "letter_features_codebook": LETTER_FEATURES,
        "muq_assignments": {str(k): v for k, v in MUQ_ASSIGNMENTS.items()},
        "letter_set_distribution": dict(Counter(y.tolist())),
        "baseline_uniform_chance": chance_uniform,
        "baseline_majority_class": str(majority_class),
        "baseline_majority_accuracy": majority_acc,
        "mw5_positive_control_top1": mw5_top1,
        "structural_multi_member_ceiling": multi_member_ceiling,
        "results_by_classifier": results,
        "verdict": verdict,
        "verdict_criteria": {
            "primary_threshold": f"top-1 > {PRIMARY_THRESHOLD} AND perm p < {ALPHA_BON}",
            "secondary_threshold": ">= 1 of 8 singletons correctly predicted",
            "pass_weak_threshold": f"top-1 > {HNEW88_BASELINE} AND perm p < 0.05 (uncorrected)",
            "pass_primary_met": bool(pass_primary),
            "pass_secondary_met": bool(pass_secondary),
            "pass_weak_met": bool(pass_weak),
            "pipeline_ok": bool(pipeline_ok),
        },
        "bonferroni_family": "h-new-165-phonological-predictor",
        "bonferroni_k": 2,
        "alpha_bon": ALPHA_BON,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUTPUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
