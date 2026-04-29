#!/usr/bin/env python3
"""
H-NEW-88 — Multi-class predictive model for muqaṭṭaʿāt LETTER-SET (14 classes, 29 surahs).

Pre-reg: findings/phase-b-hypotheses/h-new-88-letter-set-predictor-prereg.md

Locked features:
  F1: length (verse count)
  F2: period_meccan
  F3: noldeke_order
  F4: mushaf_index
  F5: book_ref_v1_3 (per H-NEW-53)
  F6: prophet_named (per H-NEW-49.1)
  F7: name_class one-hot (per H-NEW-49, 9 classes)
  F8: divine_name_density (99-names tokens / total tokens)
  F9: first_content_word_class (5 categories one-hot)
  F10: top-20 root counts (locked from full muqaṭṭaʿāt corpus)
  F11: mean_verse_length_chars
  F12: letter_count_in_set (1–5)

Procedure:
  - Multi-class classifiers: multinomial logistic + random forest
  - LOOCV (29 folds)
  - Permutation null (1000 shuffles)
  - Feature importance (logistic coefs by class, RF permutation imp)
  - Confusion matrix
  - PASS criteria locked
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import LeaveOneOut

# ---------- locked constants ----------

SEED = 20260416
N_PERM = 1000

QURAN_JSON = Path("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json")
REVELATION_CSV = Path("/Users/grey/Downloads/quran/data/revelation-order.csv")
ASMA_TXT = Path("/Users/grey/Downloads/quran/data/asma-al-husna.txt")

OUTPUT_JSON = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-88.json")

# Locked muqaṭṭaʿāt set (29 surahs)
MUQ_SURAHS = sorted(
    {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
     36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
)
assert len(MUQ_SURAHS) == 29

# Locked 14 letter-sets per surah
LETTER_SET = {
    2:  "ALM",     3:  "ALM",
    7:  "ALMS",
    10: "ALR",     11: "ALR",     12: "ALR",     14: "ALR",     15: "ALR",
    13: "ALMR",
    19: "KHYAS",
    20: "TH",
    26: "TSM",     28: "TSM",
    27: "TS",
    29: "ALM",     30: "ALM",     31: "ALM",     32: "ALM",
    36: "YS",
    38: "S",
    40: "HM",      41: "HM",      43: "HM",      44: "HM",      45: "HM",      46: "HM",
    42: "HMASQ",
    50: "Q",
    68: "N",
}
assert len(LETTER_SET) == 29
assert len(set(LETTER_SET.values())) == 14

# Locked prophet-named set per H-NEW-49.1
PROPHET_NAMED_SURAHS = frozenset({10, 11, 12, 14, 19, 31, 47, 71})

# Book-reference substring lists per H-NEW-53
KITAB_FORMS = [
    "كتاب", "كتب", "الكتاب", "الكتب",
    "كتابك", "كتابه", "كتابي", "كتابهم", "كتابا",
]
QURAN_FORMS = [
    "قرآن", "القرآن", "قرءان", "القرءان",
    "قرءن", "قرآنا", "قرآنه",
]

# Locked name-class taxonomy from H-NEW-49 (PROPHET_PERSON, ANIMAL_OBJECT, etc.)
SURAH_NAME_CLASS = {
    1: "REVELATION_RITUAL", 2: "ANIMAL_OBJECT", 3: "PROPHET_PERSON", 4: "SOCIAL_LEGAL",
    5: "ANIMAL_OBJECT", 6: "ANIMAL_OBJECT", 7: "COSMOLOGICAL_NATURAL", 8: "SOCIAL_LEGAL",
    9: "REVELATION_RITUAL", 10: "PROPHET_PERSON", 11: "PROPHET_PERSON", 12: "PROPHET_PERSON",
    13: "COSMOLOGICAL_NATURAL", 14: "PROPHET_PERSON", 15: "COSMOLOGICAL_NATURAL",
    16: "ANIMAL_OBJECT", 17: "REVELATION_RITUAL", 18: "REVELATION_RITUAL",
    19: "PROPHET_PERSON", 20: "MUQATTAAT_LETTER", 21: "PROPHET_PERSON",
    22: "REVELATION_RITUAL", 23: "SOCIAL_LEGAL", 24: "DIVINE_ATTRIBUTE",
    25: "REVELATION_RITUAL", 26: "SOCIAL_LEGAL", 27: "ANIMAL_OBJECT",
    28: "REVELATION_RITUAL", 29: "ANIMAL_OBJECT", 30: "SOCIAL_LEGAL",
    31: "PROPHET_PERSON", 32: "REVELATION_RITUAL", 33: "SOCIAL_LEGAL",
    34: "PROPHET_PERSON", 35: "DIVINE_ATTRIBUTE", 36: "MUQATTAAT_LETTER",
    37: "SOCIAL_LEGAL", 38: "MUQATTAAT_LETTER", 39: "SOCIAL_LEGAL",
    40: "DIVINE_ATTRIBUTE", 41: "REVELATION_RITUAL", 42: "SOCIAL_LEGAL",
    43: "ANIMAL_OBJECT", 44: "COSMOLOGICAL_NATURAL", 45: "EVENT_ESCHATOLOGICAL",
    46: "COSMOLOGICAL_NATURAL", 50: "MUQATTAAT_LETTER", 68: "ANIMAL_OBJECT",
}
NAME_CLASSES = [
    "PROPHET_PERSON", "ANIMAL_OBJECT", "DIVINE_ATTRIBUTE", "COSMOLOGICAL_NATURAL",
    "EVENT_ESCHATOLOGICAL", "SOCIAL_LEGAL", "REVELATION_RITUAL",
    "MUQATTAAT_LETTER", "OTHER_ABSTRACT",
]

# Letter count per set
LETTER_COUNT = {
    "ALM": 3, "ALMS": 4, "ALR": 3, "ALMR": 4, "KHYAS": 5,
    "TH": 2, "TSM": 3, "TS": 2, "YS": 2, "S": 1,
    "HM": 2, "HMASQ": 5, "Q": 1, "N": 1,
}


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


def load_asma_names() -> list[str]:
    """Load 99 names of Allah (Arabic strings, definite-form)."""
    names = []
    with ASMA_TXT.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            names.append(line)
    return names


# ---------- text helpers ----------

ARABIC_LETTERS = set("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")

def strip_punct(s: str) -> str:
    """Keep only Arabic letters + spaces."""
    return "".join(c if (c in ARABIC_LETTERS or c.isspace()) else " " for c in s)


def has_book_ref_in_v1_3(surah: dict) -> int:
    """Return 1 if any k-t-b or q-r-ʾ form found in verses 1-3."""
    verses = surah["verses"][:3]
    for v in verses:
        text = v["text"]
        for form in KITAB_FORMS + QURAN_FORMS:
            if form in text:
                return 1
    return 0


def first_content_word_class(surah: dict, muqs_str_set: set) -> str:
    """Classify the first content word after the muqaṭṭaʿāt opening.
    Categories: 'BOOK_REF', 'OATH', 'ADDRESS', 'NARRATIVE_PARTICLE', 'OTHER'.
    """
    v1 = surah["verses"][0]["text"]
    # Take first ~3 verses if v1 is short (e.g., الم alone)
    candidates = " ".join(v["text"] for v in surah["verses"][:3])
    candidates = strip_punct(candidates)
    words = candidates.split()
    # Skip muqaṭṭaʿāt-only words
    content = []
    for w in words:
        if w in muqs_str_set or len(w) <= 1:
            continue
        # also skip if word IS exactly a single-letter muqaṭṭaʿa (like ص, ق, ن)
        content.append(w)
    if not content:
        return "OTHER"
    first = content[0]
    # BOOK_REF: kitab/quran roots
    book_substr = ["كتب", "كتاب", "قران", "قرءان", "قرآن", "ايات", "آيات"]
    for s in book_substr:
        if s in first:
            return "BOOK_REF"
    # OATH: starts with و (wa = "by") or has قسم
    if first.startswith("و"):
        return "OATH"
    # ADDRESS: pronouns yā / second-person particles
    address = ["يا", "انت", "انتم", "ك"]
    if first in address or first.startswith("يا"):
        return "ADDRESS"
    # NARRATIVE_PARTICLE: قال / قل / تلك / هذه / إذا
    narr = ["قال", "قل", "تلك", "هذه", "هذا", "اذا", "إذا", "حم"]
    if first in narr:
        return "NARRATIVE_PARTICLE"
    return "OTHER"


def divine_name_density(surah: dict, asma_names: list[str]) -> float:
    """Sum of divine-name token occurrences / total tokens in surah."""
    text_all = " ".join(v["text"] for v in surah["verses"])
    text_clean = strip_punct(text_all)
    tokens = text_clean.split()
    n_tokens = len(tokens)
    if n_tokens == 0:
        return 0.0
    # Substring count of each name (with leading whitespace boundaries to avoid partial matches)
    count = 0
    for name in asma_names:
        # Count tokens that exactly match or with definite-article variants
        for t in tokens:
            if t == name or t.endswith(name) or t.startswith(name):
                count += 1
                break  # count name occurrence once per occurrence pass; we handle per-name separately
    # Actually to be principled: substring count in joined text
    count = 0
    for name in asma_names:
        idx = 0
        while True:
            j = text_clean.find(name, idx)
            if j < 0:
                break
            count += 1
            idx = j + len(name)
    return count / n_tokens


def mean_verse_length_chars(surah: dict) -> float:
    lens = [len(strip_punct(v["text"])) for v in surah["verses"]]
    if not lens:
        return 0.0
    return float(np.mean(lens))


def consonant_skeleton(word: str) -> str:
    """Strip definite article and return consonant skeleton (3-5 letters)."""
    # Remove al- prefix
    w = word
    if w.startswith("ال") and len(w) > 4:
        w = w[2:]
    # Remove conjunction wa
    if w.startswith("و") and len(w) > 4:
        w = w[1:]
    # Keep only Arabic consonants, no weak letters in middle
    return w


def extract_root_counts_per_surah(surah: dict, top_roots: list[str]) -> list[int]:
    """For each root in top_roots, count substring occurrences in surah text."""
    text_all = " ".join(v["text"] for v in surah["verses"])
    text_clean = strip_punct(text_all)
    counts = []
    for root in top_roots:
        # count occurrences of root substring (very rough; consonantal skeleton substring)
        c = 0
        idx = 0
        while True:
            j = text_clean.find(root, idx)
            if j < 0:
                break
            c += 1
            idx = j + 1
        counts.append(c)
    return counts


def lock_top_roots_from_muq_corpus(quran: dict, k: int = 20) -> list[str]:
    """Select top-K most frequent 3-character substrings (proxy for roots)
    across all 29 muqaṭṭaʿāt-opened surahs. Locked once, used for all folds.
    """
    skel_counter: Counter = Counter()
    for sid in MUQ_SURAHS:
        s = quran[sid]
        text_all = " ".join(v["text"] for v in s["verses"])
        text_clean = strip_punct(text_all)
        for tok in text_clean.split():
            sk = consonant_skeleton(tok)
            # take 3-char skeleton from middle
            if len(sk) >= 3:
                # all 3-char windows
                for i in range(len(sk) - 2):
                    skel_counter[sk[i:i+3]] += 1
    # Filter: skip purely high-frequency function-letter combos? No — we keep raw and let model decide.
    most_common = [r for r, _ in skel_counter.most_common(k)]
    return most_common


# ---------- feature matrix ----------

def build_design_matrix() -> tuple[np.ndarray, np.ndarray, list[str], list[str], list[int]]:
    quran = load_quran()
    rev = load_revelation()
    asma = load_asma_names()
    top_roots = lock_top_roots_from_muq_corpus(quran, k=20)

    muqs_str_set = {"الم", "المص", "الر", "المر", "كهيعص", "طه", "طسم",
                    "طس", "يس", "ص", "حم", "ق", "ن", "عسق"}

    rows = []
    y_str = []
    surah_ids = []
    for sid in MUQ_SURAHS:
        s = quran[sid]
        r = rev[sid]
        length = int(s["total_verses"])
        period_meccan = 1 if r["period"] == "meccan" else 0
        noldeke = int(r["noldeke_order"])
        mushaf = sid
        bookref = has_book_ref_in_v1_3(s)
        prophet = 1 if sid in PROPHET_NAMED_SURAHS else 0
        # name_class one-hot
        nc = SURAH_NAME_CLASS.get(sid, "OTHER_ABSTRACT")
        nc_oh = [1 if cls == nc else 0 for cls in NAME_CLASSES]
        # divine name density
        dnd = divine_name_density(s, asma)
        # first content word class one-hot
        fcw = first_content_word_class(s, muqs_str_set)
        fcw_classes = ["BOOK_REF", "OATH", "ADDRESS", "NARRATIVE_PARTICLE", "OTHER"]
        fcw_oh = [1 if cls == fcw else 0 for cls in fcw_classes]
        # top-K root counts
        roots = extract_root_counts_per_surah(s, top_roots)
        # mean verse length chars
        mvlc = mean_verse_length_chars(s)
        # letter count in set
        ls = LETTER_SET[sid]
        lc = LETTER_COUNT[ls]

        row = (
            [length, period_meccan, noldeke, mushaf, bookref, prophet]
            + nc_oh
            + [dnd]
            + fcw_oh
            + roots
            + [mvlc, lc]
        )
        rows.append(row)
        y_str.append(ls)
        surah_ids.append(sid)

    feature_names = (
        ["length", "period_meccan", "noldeke_order", "mushaf_index",
         "book_ref_v1_3", "prophet_named"]
        + [f"name_class_{c}" for c in NAME_CLASSES]
        + ["divine_name_density"]
        + [f"first_word_{c}" for c in ["BOOK_REF", "OATH", "ADDRESS", "NARRATIVE_PARTICLE", "OTHER"]]
        + [f"root_top_{r}" for r in top_roots]
        + ["mean_verse_length_chars", "letter_count_in_set"]
    )
    X = np.array(rows, dtype=float)
    return X, np.array(y_str), feature_names, top_roots, surah_ids


# ---------- LOOCV ----------

def loocv(X: np.ndarray, y: np.ndarray, classifier_name: str) -> tuple[np.ndarray, np.ndarray]:
    """Returns (y_pred_top1, y_pred_proba_matrix)."""
    n = X.shape[0]
    # We need to know the global label set
    classes_global = np.array(sorted(set(y.tolist())))
    n_classes = len(classes_global)
    y_pred_top1 = np.empty(n, dtype=object)
    proba_matrix = np.full((n, n_classes), np.nan, dtype=float)

    loo = LeaveOneOut()
    for train_idx, test_idx in loo.split(X):
        X_tr, X_te = X[train_idx], X[test_idx]
        y_tr = y[train_idx]
        # standardize (only continuous numeric cols matter; binary safe to scale too for logistic)
        mu = X_tr.mean(axis=0)
        sd = X_tr.std(axis=0)
        sd[sd == 0] = 1.0
        X_tr_s = (X_tr - mu) / sd
        X_te_s = (X_te - mu) / sd
        # Map classes available in this fold
        if classifier_name == "logistic":
            clf = LogisticRegression(
                C=1.0, solver="lbfgs", max_iter=2000,
                random_state=SEED,
            )
        elif classifier_name == "rf":
            clf = RandomForestClassifier(
                n_estimators=200, random_state=SEED, n_jobs=1,
            )
        else:
            raise ValueError(classifier_name)
        clf.fit(X_tr_s, y_tr)
        local_classes = clf.classes_
        proba = clf.predict_proba(X_te_s)[0]  # shape (n_local,)
        # Map proba into global class index
        for j, cls in enumerate(local_classes):
            gi = int(np.where(classes_global == cls)[0][0])
            proba_matrix[test_idx[0], gi] = proba[j]
        # Top-1 prediction
        top1_idx = int(np.argmax(proba))
        y_pred_top1[test_idx[0]] = local_classes[top1_idx]
    return y_pred_top1, proba_matrix, classes_global


def topk_accuracy(y_true: np.ndarray, proba: np.ndarray,
                  classes_global: np.ndarray, k: int) -> float:
    n = len(y_true)
    correct = 0
    for i in range(n):
        # rank classes by proba descending; NaN treated as -inf
        scores = proba[i].copy()
        scores[np.isnan(scores)] = -np.inf
        topk_idx = np.argsort(scores)[::-1][:k]
        topk_labels = classes_global[topk_idx]
        if y_true[i] in topk_labels:
            correct += 1
    return correct / n


# ---------- permutation null ----------

def permutation_null(X: np.ndarray, y: np.ndarray,
                     observed_acc: float, classifier_name: str,
                     n_perm: int) -> dict:
    rng = np.random.default_rng(SEED)
    perm_accs = []
    ge_count = 0
    for k in range(n_perm):
        y_perm = rng.permutation(y)
        try:
            y_pred, proba, classes_g = loocv(X, y_perm, classifier_name)
            acc = float(accuracy_score(y_perm, y_pred))
        except Exception:
            acc = 1.0 / len(set(y))
        perm_accs.append(acc)
        if acc >= observed_acc:
            ge_count += 1
        if (k + 1) % 100 == 0:
            print(f"  perm {k+1}/{n_perm} acc_so_far_mean={np.mean(perm_accs):.4f} ge_count={ge_count}")
    perm_accs = np.array(perm_accs)
    p = (1 + ge_count) / (n_perm + 1)
    return {
        "n_perm": n_perm,
        "p_value": float(p),
        "perm_acc_mean": float(perm_accs.mean()),
        "perm_acc_std": float(perm_accs.std()),
        "perm_acc_max": float(perm_accs.max()),
        "perm_acc_q95": float(np.quantile(perm_accs, 0.95)),
        "perm_acc_q99": float(np.quantile(perm_accs, 0.99)),
        "ge_count": int(ge_count),
    }


# ---------- main ----------

def main():
    print("Building design matrix...")
    X, y, feature_names, top_roots, surah_ids = build_design_matrix()
    print(f"  X.shape = {X.shape}; n_classes = {len(set(y))}")
    print(f"  Letter-set distribution: {Counter(y)}")
    print(f"  Top roots locked: {top_roots}")

    # baselines
    chance_uniform = 1.0 / len(set(y))
    majority_class = Counter(y).most_common(1)[0][0]
    majority_acc = sum(1 for v in y if v == majority_class) / len(y)
    print(f"  Baseline chance (uniform): {chance_uniform:.4f}")
    print(f"  Baseline majority ({majority_class}): {majority_acc:.4f}")

    results = {}
    for clf_name in ["logistic", "rf"]:
        print(f"\n=== Classifier: {clf_name} ===")
        y_pred, proba, classes_global = loocv(X, y, clf_name)
        acc1 = float(accuracy_score(y, y_pred))
        acc3 = topk_accuracy(y, proba, classes_global, k=3)
        acc5 = topk_accuracy(y, proba, classes_global, k=5)
        print(f"  LOOCV top-1 accuracy: {acc1:.4f}")
        print(f"  LOOCV top-3 accuracy: {acc3:.4f}")
        print(f"  LOOCV top-5 accuracy: {acc5:.4f}")

        # confusion matrix
        labels_sorted = sorted(set(y))
        cm = confusion_matrix(y, y_pred, labels=labels_sorted)
        print(f"  Confusion matrix shape: {cm.shape}")

        # per-set recall
        per_set_recall = {}
        for cls in labels_sorted:
            mask = (y == cls)
            if mask.sum() > 0:
                per_set_recall[cls] = float((y_pred[mask] == cls).sum() / mask.sum())

        # permutation null (only on top-1 acc)
        print(f"  Running permutation null (n={N_PERM})...")
        perm = permutation_null(X, y, acc1, clf_name, N_PERM)
        print(f"  perm acc mean={perm['perm_acc_mean']:.4f}  q95={perm['perm_acc_q95']:.4f}  max={perm['perm_acc_max']:.4f}")
        print(f"  p-value = {perm['p_value']:.4f}  (ge_count={perm['ge_count']}/{N_PERM})")

        # Feature importance from full-data model
        mu = X.mean(axis=0); sd = X.std(axis=0); sd[sd == 0] = 1.0
        Xs = (X - mu) / sd
        if clf_name == "logistic":
            clf_full = LogisticRegression(
                C=1.0, solver="lbfgs", max_iter=2000,
                random_state=SEED,
            )
            clf_full.fit(Xs, y)
            # |coef|.mean over classes per feature
            mean_abs = np.mean(np.abs(clf_full.coef_), axis=0)
            feat_imp = sorted(
                zip(feature_names, mean_abs.tolist()),
                key=lambda kv: kv[1], reverse=True,
            )
        else:
            clf_full = RandomForestClassifier(
                n_estimators=200, random_state=SEED, n_jobs=1,
            )
            clf_full.fit(Xs, y)
            feat_imp = sorted(
                zip(feature_names, clf_full.feature_importances_.tolist()),
                key=lambda kv: kv[1], reverse=True,
            )

        results[clf_name] = {
            "loocv_top1_accuracy": acc1,
            "loocv_top3_accuracy": acc3,
            "loocv_top5_accuracy": acc5,
            "permutation_null": perm,
            "per_set_recall": per_set_recall,
            "confusion_matrix": cm.tolist(),
            "confusion_matrix_labels": labels_sorted,
            "feature_importance_top20": [{"feature": nm, "importance": v} for nm, v in feat_imp[:20]],
            "per_surah_predictions": [
                {
                    "surah": int(surah_ids[i]),
                    "true_set": str(y[i]),
                    "pred_set": str(y_pred[i]),
                    "correct": bool(y[i] == y_pred[i]),
                }
                for i in range(len(y))
            ],
        }

    # Verdict (primary = logistic)
    primary = results["logistic"]
    pass_acc = primary["loocv_top1_accuracy"] >= 0.30
    pass_p = primary["permutation_null"]["p_value"] < 0.05
    strong_acc = primary["loocv_top1_accuracy"] >= 0.50
    strong_p = primary["permutation_null"]["p_value"] < 0.01
    if pass_acc and pass_p and strong_acc and strong_p:
        verdict = "STRONG-PASS"
    elif pass_acc and pass_p:
        verdict = "PASS"
    elif primary["loocv_top1_accuracy"] <= majority_acc or primary["permutation_null"]["p_value"] >= 0.05:
        verdict = "NULL"
    else:
        verdict = "INCONCLUSIVE"
    print(f"\n=== VERDICT (primary=logistic): {verdict} ===")
    print(f"  top-1 acc {primary['loocv_top1_accuracy']:.4f} >= 0.30? {pass_acc}")
    print(f"  perm p {primary['permutation_null']['p_value']:.4f} < 0.05? {pass_p}")

    out = {
        "id": "H-NEW-88",
        "title": "Multi-class predictive model for muqaṭṭaʿāt LETTER-SET",
        "seed": SEED,
        "n_surahs": len(MUQ_SURAHS),
        "n_classes": len(set(y)),
        "n_features": X.shape[1],
        "feature_names": feature_names,
        "top_roots_locked": top_roots,
        "letter_set_distribution": dict(Counter(y)),
        "baseline_uniform_chance": chance_uniform,
        "baseline_majority_class": majority_class,
        "baseline_majority_accuracy": majority_acc,
        "results_by_classifier": results,
        "primary_classifier": "logistic",
        "verdict": verdict,
        "pass_criterion": {
            "top1_acc_gte_0_30": bool(pass_acc),
            "perm_p_lt_0_05": bool(pass_p),
            "strong_top1_gte_0_50": bool(strong_acc),
            "strong_perm_p_lt_0_01": bool(strong_p),
        },
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
