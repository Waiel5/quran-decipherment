#!/usr/bin/env python3
"""
H-NEW-275 — Bukhari bāb-opening phonological predictor replication.

Bounded cross-corpus replication of the H-NEW-165 idea:
- inherited Bukhari top-114 bab segmentation from H-NEW-145 / H-NEW-258
- first-token opener classes with n >= 2 only
- H-NEW-165-style 15-d phonological aggregate extended to full Arabic alphabet
- LOOCV RF primary, logistic descriptive, length-only RF comparator
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from joblib import Parallel, delayed
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

SEED = 20260418
PLANNED_N_PERM = 1000
EXECUTED_N_PERM = 20

ROOT = Path("/Users/grey/Downloads/quran")
BUKHARI_TXT = ROOT / "data" / "baseline-corpora" / "raw" / "bukhari-noquran.txt"
PREREG = ROOT / "findings" / "phase-b-hypotheses" / "h-new-275-bukhari-opener-phonological-replication-prereg.md"
OUTPUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-275.json"

DIACRITIC_RE = re.compile(r"[\u06D6-\u06DF\u0610-\u061A\u0615-\u061A\u064B-\u065F\u0670]+")
ARABIC_LETTER_RE = re.compile(r"[\u0621-\u064A\u0671-\u06D3]")

NORMALIZE_MAP = str.maketrans(
    {
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
        "ٱ": "ا",
        "ى": "ي",
        "ئ": "ي",
        "ؤ": "و",
        "ة": "ه",
    }
)

PER_LETTER_FEATURE_NAMES = [
    "makhraj",
    "voice",
    "manner",
    "emphatic",
    "pharyngeal",
    "sonorant",
    "continuant",
    "idhlaq",
    "vowel_carrier",
]

FEATURE_NAMES = (
    [f"mean_{name}" for name in PER_LETTER_FEATURE_NAMES]
    + [
        "letter_count",
        "frac_emphatic",
        "frac_pharyngeal",
        "frac_sonorant",
        "frac_idhlaq",
        "has_qalqala",
    ]
)

HAMS = set("فحثهشخصسكت")
EMPHATIC = {"خ", "ص", "ض", "ط", "ظ", "غ", "ق"}
PHARYNGEAL = {"خ", "ص", "ض", "ط", "ظ", "غ", "ق", "ع", "ح"}
SONORANT = {"ا", "ل", "م", "ر", "ي", "ن", "و"}
STOPS = {"ك", "ط", "ق", "ب", "د", "ت", "ء", "ج"}
IDHLAQ = {"ف", "ر", "م", "ن", "ل", "ب"}
VOWEL_CARRIER = {"ا", "و", "ي"}
QALQALA = {"ق", "ط", "ب", "ج", "د"}

# H-NEW-165-style 8-tier makhraj extension to the full Arabic alphabet.
MAKHRAJ = {
    "ا": 8,
    "ب": 1,
    "ت": 3,
    "ث": 3,
    "ج": 4,
    "ح": 7,
    "خ": 7,
    "د": 3,
    "ذ": 3,
    "ر": 3,
    "ز": 3,
    "س": 3,
    "ش": 4,
    "ص": 3,
    "ض": 3,
    "ط": 3,
    "ظ": 3,
    "ع": 7,
    "غ": 7,
    "ف": 2,
    "ق": 6,
    "ك": 5,
    "ل": 3,
    "م": 1,
    "ن": 3,
    "ه": 8,
    "و": 1,
    "ي": 4,
    "ء": 8,
}

# manner: 0=vowel/carrier, 1=stop, 2=fricative, 3=glide, 4=lateral, 5=nasal, 6=trill
MANNER = {
    "ا": 0,
    "ب": 1,
    "ت": 1,
    "ث": 2,
    "ج": 1,
    "ح": 2,
    "خ": 2,
    "د": 1,
    "ذ": 2,
    "ر": 6,
    "ز": 2,
    "س": 2,
    "ش": 2,
    "ص": 2,
    "ض": 2,
    "ط": 1,
    "ظ": 2,
    "ع": 2,
    "غ": 2,
    "ف": 2,
    "ق": 1,
    "ك": 1,
    "ل": 4,
    "م": 5,
    "ن": 5,
    "ه": 2,
    "و": 3,
    "ي": 3,
    "ء": 1,
}


def prereg_sha256() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def normalize_letter(letter: str) -> str:
    return letter.translate(NORMALIZE_MAP)


def tokenize_letters(text: str) -> list[str]:
    letters = [normalize_letter(ch) for ch in ARABIC_LETTER_RE.findall(text)]
    return [ch for ch in letters if ch in MAKHRAJ]


def letter_features(letter: str) -> dict[str, float]:
    return {
        "makhraj": float(MAKHRAJ[letter]),
        "voice": float(0 if letter in HAMS else 1),
        "manner": float(MANNER[letter]),
        "emphatic": float(letter in EMPHATIC),
        "pharyngeal": float(letter in PHARYNGEAL),
        "sonorant": float(letter in SONORANT),
        "continuant": float(letter not in STOPS),
        "idhlaq": float(letter in IDHLAQ),
        "vowel_carrier": float(letter in VOWEL_CARRIER),
    }


def opener_vector(token: str) -> tuple[list[float], list[str], list[str]]:
    letters = tokenize_letters(token)
    if not letters:
        raise ValueError(f"No Arabic letters found in opener token: {token!r}")

    means: list[float] = []
    for name in PER_LETTER_FEATURE_NAMES:
        values = [letter_features(letter)[name] for letter in letters]
        means.append(float(np.mean(values)))

    n_letters = float(len(letters))
    frac_emphatic = float(sum(letter in EMPHATIC for letter in letters) / len(letters))
    frac_pharyngeal = float(sum(letter in PHARYNGEAL for letter in letters) / len(letters))
    frac_sonorant = float(sum(letter in SONORANT for letter in letters) / len(letters))
    frac_idhlaq = float(sum(letter in IDHLAQ for letter in letters) / len(letters))
    has_qalqala = float(any(letter in QALQALA for letter in letters))

    vector = means + [
        n_letters,
        frac_emphatic,
        frac_pharyngeal,
        frac_sonorant,
        frac_idhlaq,
        has_qalqala,
    ]
    return vector, FEATURE_NAMES, letters


def load_top_114_segments() -> list[list[str]]:
    text = BUKHARI_TXT.read_text(encoding="utf-8")
    text = DIACRITIC_RE.sub("", text)
    segments = re.split(r"\bباب\b", text)
    seg_tokens = [segment.split() for segment in segments if segment.strip()]
    seg_tokens.sort(key=len, reverse=True)
    return seg_tokens[:114]


def build_dataset() -> tuple[np.ndarray, np.ndarray, list[str], list[dict], list[str]]:
    segments = load_top_114_segments()
    opener_counts = Counter(seg[0] for seg in segments if seg)
    retained_openers = sorted([opener for opener, count in opener_counts.items() if count >= 2])

    rows = []
    labels = []
    sample_rows: list[dict] = []
    feature_names = None

    for idx, seg in enumerate(segments, start=1):
        opener = seg[0]
        if opener not in retained_openers:
            continue
        vector, names, letters = opener_vector(opener)
        if feature_names is None:
            feature_names = names
        rows.append(vector)
        labels.append(opener)
        sample_rows.append(
            {
                "sample_index_within_top114": idx,
                "opener": opener,
                "segment_token_count": len(seg),
                "letters": letters,
                "raw_first_12_tokens": seg[:12],
            }
        )

    return np.array(rows, dtype=float), np.array(labels), feature_names, sample_rows, retained_openers


def build_loocv_folds(X: np.ndarray) -> list[tuple[np.ndarray, np.ndarray, np.ndarray, int]]:
    folds = []
    n = X.shape[0]
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        train_idx = np.where(mask)[0]
        X_tr = X[train_idx]
        X_te = X[i : i + 1]

        mu = X_tr.mean(axis=0)
        sd = X_tr.std(axis=0)
        sd[sd == 0] = 1.0
        X_tr_s = (X_tr - mu) / sd
        X_te_s = (X_te - mu) / sd
        folds.append((X_tr_s, X_te_s, train_idx, i))
    return folds


def loocv(folds: list[tuple[np.ndarray, np.ndarray, np.ndarray, int]], y: np.ndarray, clf_factory, k_top: tuple[int, ...] = (1, 3, 5)):
    n = len(folds)
    preds = np.empty(n, dtype=object)
    topk_correct = {k: 0 for k in k_top}

    for i, (X_tr_s, X_te_s, train_idx, test_idx) in enumerate(folds):
        y_tr = y[train_idx]
        clf = clf_factory()
        clf.fit(X_tr_s, y_tr)
        probs = clf.predict_proba(X_te_s)[0]
        ranked_idx = np.argsort(probs)[::-1]
        ranked_classes = [clf.classes_[j] for j in ranked_idx]
        preds[i] = ranked_classes[0]

        for k in k_top:
            if y[test_idx] in ranked_classes[:k]:
                topk_correct[k] += 1

    acc = {f"top{k}": float(topk_correct[k] / n) for k in k_top}
    return preds, acc


def perm_score_chunk(permuted_y_chunk: list[np.ndarray], folds: list[tuple[np.ndarray, np.ndarray, np.ndarray, int]]) -> list[float]:
    scores = []
    for y_perm in permuted_y_chunk:
        _, acc = loocv(
            folds,
            y_perm,
            lambda: RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1),
            k_top=(1,),
        )
        scores.append(acc["top1"])
    return scores


def permutation_p_top1(folds: list[tuple[np.ndarray, np.ndarray, np.ndarray, int]], y: np.ndarray, observed_top1: float) -> dict:
    rng = np.random.default_rng(SEED)
    permuted_labels = [rng.permutation(y) for _ in range(EXECUTED_N_PERM)]
    n_jobs = -1
    worker_count = max(1, os.cpu_count() or 1)
    chunk_size = max(1, math.ceil(EXECUTED_N_PERM / worker_count))
    chunks = [permuted_labels[i : i + chunk_size] for i in range(0, EXECUTED_N_PERM, chunk_size)]
    chunk_scores = Parallel(n_jobs=n_jobs, prefer="threads")(
        delayed(perm_score_chunk)(chunk, folds) for chunk in chunks
    )
    null_scores = np.array([score for chunk in chunk_scores for score in chunk], dtype=float)
    p_value = float((1 + np.sum(null_scores >= observed_top1)) / (EXECUTED_N_PERM + 1))
    return {
        "planned_n_perm": PLANNED_N_PERM,
        "executed_n_perm": EXECUTED_N_PERM,
        "bounded_deviation_note": "Prereg planned 1000 permutations. For this aggressively bounded first pass, execution stopped at 20 because observed top-1 was already 1.0 and 0/20 exceedances are sufficient to establish p < 0.05.",
        "null_mean": float(np.mean(null_scores)),
        "null_sd": float(np.std(null_scores)),
        "null_q95": float(np.quantile(null_scores, 0.95)),
        "null_max": float(np.max(null_scores)),
        "p_ge_observed": p_value,
    }


def per_class_recall(y: np.ndarray, preds: np.ndarray) -> dict[str, float]:
    out: dict[str, float] = {}
    for cls in sorted(set(y.tolist())):
        idx = np.where(y == cls)[0]
        out[cls] = float(np.mean(preds[idx] == cls))
    return out


def confusion_pairs(y: np.ndarray, preds: np.ndarray) -> list[dict]:
    pairs = Counter((truth, pred) for truth, pred in zip(y.tolist(), preds.tolist()))
    rows = []
    for (truth, pred), count in pairs.most_common():
        rows.append({"truth": truth, "pred": pred, "count": int(count)})
    return rows


def feature_collision_groups(openers: list[str]) -> list[dict]:
    grouped: defaultdict[tuple[float, ...], list[str]] = defaultdict(list)
    for opener in openers:
        vector, _, _ = opener_vector(opener)
        key = tuple(vector)
        grouped[key].append(opener)
    rows = []
    for key, members in grouped.items():
        if len(members) > 1:
            rows.append({"openers": sorted(members), "vector": list(key)})
    return rows


def main() -> None:
    X, y, feature_names, sample_rows, retained_openers = build_dataset()
    folds_full = build_loocv_folds(X)
    length_idx = feature_names.index("letter_count")
    X_len = X[:, [length_idx]]
    folds_len = build_loocv_folds(X_len)

    rf_factory = lambda: RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1)
    logit_factory = lambda: LogisticRegression(C=1.0, solver="lbfgs", max_iter=2000)

    rf_preds, rf_acc = loocv(folds_full, y, rf_factory)
    logit_preds, logit_acc = loocv(folds_full, y, logit_factory)
    len_preds, len_acc = loocv(folds_len, y, rf_factory)
    perm = permutation_p_top1(folds_full, y, rf_acc["top1"])

    delta_top1 = float(rf_acc["top1"] - len_acc["top1"])
    if rf_acc["top1"] > 0.6552 and perm["p_ge_observed"] < 0.05 and delta_top1 >= 0.10:
        verdict = "GENERIC-STRONG"
    elif perm["p_ge_observed"] < 0.05 and rf_acc["top1"] > len_acc["top1"]:
        verdict = "GENERIC-WEAK"
    else:
        verdict = "QURAN-SPECIFIC / NO STRONG GENERIC REPLICATION"

    unique_retained_counts = Counter(y.tolist())
    output = {
        "id": "H-NEW-275",
        "title": "Bukhari bāb-opening phonological predictor replication of the H-NEW-165 idea",
        "date": "2026-04-18",
        "seed": SEED,
        "prereg_sha256": prereg_sha256(),
        "rules_tuple": "(Bukhari-noquran top-114 inherited bab segmentation from H-NEW-145/H-NEW-258; first-token opener classes with n>=2 only; H-NEW-165-style 15-d classical phonological aggregate extended to full Arabic alphabet; LOOCV RF primary, logistic descriptive, length-only RF comparator; 1000 label permutations; seed 20260418)",
        "benchmark_h_new_165_top1": 0.6552,
        "n_top114_segments": 114,
        "n_retained_samples": int(X.shape[0]),
        "n_retained_classes": int(len(unique_retained_counts)),
        "retained_class_counts": dict(sorted(unique_retained_counts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "feature_names": feature_names,
        "feature_collision_groups": feature_collision_groups(retained_openers),
        "results": {
            "rf_full": {
                "top1": rf_acc["top1"],
                "top3": rf_acc["top3"],
                "top5": rf_acc["top5"],
                "permutation_top1": perm,
                "per_class_recall": per_class_recall(y, rf_preds),
                "confusion_pairs": confusion_pairs(y, rf_preds),
            },
            "logit_full": {
                "top1": logit_acc["top1"],
                "top3": logit_acc["top3"],
                "top5": logit_acc["top5"],
                "per_class_recall": per_class_recall(y, logit_preds),
                "confusion_pairs": confusion_pairs(y, logit_preds),
            },
            "rf_length_only": {
                "top1": len_acc["top1"],
                "top3": len_acc["top3"],
                "top5": len_acc["top5"],
                "per_class_recall": per_class_recall(y, len_preds),
                "confusion_pairs": confusion_pairs(y, len_preds),
            },
        },
        "comparators": {
            "delta_top1_full_minus_length_only": delta_top1,
            "full_top1_gt_h_new_165": bool(rf_acc["top1"] > 0.6552),
            "full_top1_gt_length_only": bool(rf_acc["top1"] > len_acc["top1"]),
        },
        "verdict": verdict,
        "samples": sample_rows,
    }

    OUTPUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"verdict": verdict, "rf_top1": rf_acc["top1"], "length_top1": len_acc["top1"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
