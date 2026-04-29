#!/usr/bin/env python3
"""
H-NEW-271 — minimal phonological family test for the muq cluster ceiling.

This is a tightly scoped follow-up to H-NEW-165 / H-NEW-165.2.
It asks whether the full 15-column phonological codebook is materially
over-specified or whether a genuinely multi-feature combination is required.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np
from joblib import Parallel, delayed
from sklearn.ensemble import RandomForestClassifier

SEED = 20260419
N_PERM = 1000
ALPHA_BON = 0.025
CEILING_TOP1 = 19 / 29
OUTER_JOBS = min(4, os.cpu_count() or 1)
PERM_BATCH_SIZE = 20

OUTPUT_JSON = Path(
    "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-271.json"
)

MUQ_ASSIGNMENTS = {
    2: "ALM",
    3: "ALM",
    29: "ALM",
    30: "ALM",
    31: "ALM",
    32: "ALM",
    7: "ALMS",
    10: "ALR",
    11: "ALR",
    12: "ALR",
    14: "ALR",
    15: "ALR",
    13: "ALMR",
    19: "KHYAS",
    20: "TH",
    26: "TSM",
    28: "TSM",
    27: "TS",
    36: "YS",
    38: "S",
    40: "HM",
    41: "HM",
    43: "HM",
    44: "HM",
    45: "HM",
    46: "HM",
    42: "HMASQ",
    50: "Q",
    68: "N",
}
MUQ_SURAHS = sorted(MUQ_ASSIGNMENTS.keys())
assert len(MUQ_SURAHS) == 29

SET_LETTERS = {
    "ALM": ["ا", "ل", "م"],
    "ALMS": ["ا", "ل", "م", "ص"],
    "ALR": ["ا", "ل", "ر"],
    "ALMR": ["ا", "ل", "م", "ر"],
    "KHYAS": ["ك", "ه", "ي", "ع", "ص"],
    "TH": ["ط", "ه"],
    "TSM": ["ط", "س", "م"],
    "TS": ["ط", "س"],
    "YS": ["ي", "س"],
    "S": ["ص"],
    "HM": ["ح", "م"],
    "HMASQ": ["ح", "م", "ع", "س", "ق"],
    "Q": ["ق"],
    "N": ["ن"],
}
assert set(SET_LETTERS) == set(MUQ_ASSIGNMENTS.values())

MUQ_LETTERS = sorted(set().union(*SET_LETTERS.values()))
assert len(MUQ_LETTERS) == 14

MULTI_MEMBER_CLASSES = ("ALM", "ALR", "HM", "TSM")

LETTER_FEATURES = {
    "ا": {
        "makhraj": 8,
        "voice": 1,
        "manner": 0,
        "emphatic": 0,
        "pharyngeal": 0,
        "sonorant": 1,
        "continuant": 1,
        "idhlaq": 0,
        "vowel_carrier": 1,
    },
    "ل": {
        "makhraj": 3,
        "voice": 1,
        "manner": 4,
        "emphatic": 0,
        "pharyngeal": 0,
        "sonorant": 1,
        "continuant": 1,
        "idhlaq": 1,
        "vowel_carrier": 0,
    },
    "م": {
        "makhraj": 1,
        "voice": 1,
        "manner": 5,
        "emphatic": 0,
        "pharyngeal": 0,
        "sonorant": 1,
        "continuant": 1,
        "idhlaq": 1,
        "vowel_carrier": 0,
    },
    "ر": {
        "makhraj": 3,
        "voice": 1,
        "manner": 6,
        "emphatic": 0,
        "pharyngeal": 0,
        "sonorant": 1,
        "continuant": 1,
        "idhlaq": 1,
        "vowel_carrier": 0,
    },
    "ص": {
        "makhraj": 3,
        "voice": 0,
        "manner": 2,
        "emphatic": 1,
        "pharyngeal": 1,
        "sonorant": 0,
        "continuant": 1,
        "idhlaq": 0,
        "vowel_carrier": 0,
    },
    "ك": {
        "makhraj": 5,
        "voice": 0,
        "manner": 1,
        "emphatic": 0,
        "pharyngeal": 0,
        "sonorant": 0,
        "continuant": 0,
        "idhlaq": 0,
        "vowel_carrier": 0,
    },
    "ه": {
        "makhraj": 8,
        "voice": 0,
        "manner": 2,
        "emphatic": 0,
        "pharyngeal": 0,
        "sonorant": 0,
        "continuant": 1,
        "idhlaq": 0,
        "vowel_carrier": 0,
    },
    "ي": {
        "makhraj": 4,
        "voice": 1,
        "manner": 3,
        "emphatic": 0,
        "pharyngeal": 0,
        "sonorant": 1,
        "continuant": 1,
        "idhlaq": 0,
        "vowel_carrier": 1,
    },
    "ع": {
        "makhraj": 7,
        "voice": 1,
        "manner": 2,
        "emphatic": 0,
        "pharyngeal": 1,
        "sonorant": 0,
        "continuant": 1,
        "idhlaq": 0,
        "vowel_carrier": 0,
    },
    "ط": {
        "makhraj": 3,
        "voice": 1,
        "manner": 1,
        "emphatic": 1,
        "pharyngeal": 1,
        "sonorant": 0,
        "continuant": 0,
        "idhlaq": 0,
        "vowel_carrier": 0,
    },
    "س": {
        "makhraj": 3,
        "voice": 0,
        "manner": 2,
        "emphatic": 0,
        "pharyngeal": 0,
        "sonorant": 0,
        "continuant": 1,
        "idhlaq": 0,
        "vowel_carrier": 0,
    },
    "ح": {
        "makhraj": 7,
        "voice": 0,
        "manner": 2,
        "emphatic": 0,
        "pharyngeal": 1,
        "sonorant": 0,
        "continuant": 1,
        "idhlaq": 0,
        "vowel_carrier": 0,
    },
    "ن": {
        "makhraj": 3,
        "voice": 1,
        "manner": 5,
        "emphatic": 0,
        "pharyngeal": 0,
        "sonorant": 1,
        "continuant": 1,
        "idhlaq": 1,
        "vowel_carrier": 0,
    },
    "ق": {
        "makhraj": 6,
        "voice": 0,
        "manner": 1,
        "emphatic": 1,
        "pharyngeal": 1,
        "sonorant": 0,
        "continuant": 0,
        "idhlaq": 0,
        "vowel_carrier": 0,
    },
}

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
QALQALA_LETTERS = {"ق", "ط"}

FULL_FEATURE_NAMES = [
    "mean_makhraj",
    "mean_voice",
    "mean_manner",
    "mean_emphatic",
    "mean_pharyngeal",
    "mean_sonorant",
    "mean_continuant",
    "mean_idhlaq",
    "mean_vowel_carrier",
    "letter_count",
    "frac_emphatic",
    "frac_pharyngeal",
    "frac_sonorant",
    "frac_idhlaq",
    "has_qalqala",
]
PHONO_FEATURE_POOL = [
    "mean_makhraj",
    "mean_voice",
    "mean_manner",
    "mean_emphatic",
    "mean_pharyngeal",
    "mean_sonorant",
    "mean_continuant",
    "mean_idhlaq",
    "mean_vowel_carrier",
    "has_qalqala",
]
DUPLICATE_MAP = {
    "frac_emphatic": "mean_emphatic",
    "frac_pharyngeal": "mean_pharyngeal",
    "frac_sonorant": "mean_sonorant",
    "frac_idhlaq": "mean_idhlaq",
}


def rf_factory() -> RandomForestClassifier:
    return RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1)


def letter_set_features(letter_set_name: str) -> tuple[list[float], list[str]]:
    letters = SET_LETTERS[letter_set_name]
    n = len(letters)

    means = []
    for fname in PER_LETTER_FEATURE_NAMES:
        vals = [LETTER_FEATURES[letter][fname] for letter in letters]
        means.append(float(np.mean(vals)))

    letter_count = float(n)
    frac_emphatic = float(
        sum(LETTER_FEATURES[letter]["emphatic"] for letter in letters) / n
    )
    frac_pharyngeal = float(
        sum(LETTER_FEATURES[letter]["pharyngeal"] for letter in letters) / n
    )
    frac_sonorant = float(
        sum(LETTER_FEATURES[letter]["sonorant"] for letter in letters) / n
    )
    frac_idhlaq = float(sum(LETTER_FEATURES[letter]["idhlaq"] for letter in letters) / n)
    has_qalqala = float(any(letter in QALQALA_LETTERS for letter in letters))

    values = means + [
        letter_count,
        frac_emphatic,
        frac_pharyngeal,
        frac_sonorant,
        frac_idhlaq,
        has_qalqala,
    ]
    assert len(values) == len(FULL_FEATURE_NAMES)
    return values, FULL_FEATURE_NAMES


def build_design_matrix() -> tuple[np.ndarray, np.ndarray, list[int]]:
    rows = []
    labels = []
    surah_ids = []
    for surah_id in MUQ_SURAHS:
        label = MUQ_ASSIGNMENTS[surah_id]
        row, _ = letter_set_features(label)
        rows.append(row)
        labels.append(label)
        surah_ids.append(surah_id)
    return np.array(rows, dtype=float), np.array(labels), surah_ids


def standardize_train_test(
    X_tr: np.ndarray, X_te: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    mu = X_tr.mean(axis=0)
    sd = X_tr.std(axis=0)
    sd[sd == 0] = 1.0
    return (X_tr - mu) / sd, (X_te - mu) / sd


def loocv_preds(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    n = X.shape[0]
    preds = np.empty(n, dtype=object)
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        X_tr_s, X_te_s = standardize_train_test(X[mask], X[i : i + 1])

        clf = rf_factory()
        clf.fit(X_tr_s, y[mask])
        preds[i] = clf.predict(X_te_s)[0]
    return preds


def loocv_reaches_threshold(
    X: np.ndarray, y: np.ndarray, target_n_correct: int
) -> bool:
    n = X.shape[0]
    max_errors = n - target_n_correct
    errors = 0

    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        X_tr_s, X_te_s = standardize_train_test(X[mask], X[i : i + 1])

        clf = rf_factory()
        clf.fit(X_tr_s, y[mask])
        pred = clf.predict(X_te_s)[0]
        if pred != y[i]:
            errors += 1
            if errors > max_errors:
                return False

    return True


def top1_from_preds(y: np.ndarray, preds: np.ndarray) -> float:
    return float(np.mean(preds == y))


def per_class_recall(y: np.ndarray, preds: np.ndarray) -> dict[str, float]:
    out: dict[str, float] = {}
    for cls in sorted(set(y.tolist())):
        idx = np.where(y == cls)[0]
        out[cls] = float(np.mean(preds[idx] == y[idx]))
    return out


def ceiling_recovered(y: np.ndarray, preds: np.ndarray) -> bool:
    top1 = top1_from_preds(y, preds)
    if not np.isclose(top1, CEILING_TOP1):
        return False
    recall = per_class_recall(y, preds)
    return all(np.isclose(recall[cls], 1.0) for cls in MULTI_MEMBER_CLASSES)


def evaluate_subset(
    X_all: np.ndarray,
    y: np.ndarray,
    feature_names: list[str],
    subset_names: tuple[str, ...],
) -> dict:
    idx = [feature_names.index(name) for name in subset_names]
    preds = loocv_preds(X_all[:, idx], y)
    top1 = top1_from_preds(y, preds)
    recall = per_class_recall(y, preds)
    return {
        "subset": list(subset_names),
        "top1": top1,
        "n_correct": int(round(top1 * len(y))),
        "ceiling_recovered": ceiling_recovered(y, preds),
        "multi_member_recall": {cls: recall[cls] for cls in MULTI_MEMBER_CLASSES},
    }


def evaluate_single_axis_arm(
    X_all: np.ndarray,
    y: np.ndarray,
    feature_names: list[str],
    pool_names: list[str],
    anchor_names: list[str],
) -> tuple[dict, list[tuple[str, ...]]]:
    subsets = [tuple(anchor_names + [name]) for name in pool_names]
    results = [evaluate_subset(X_all, y, feature_names, subset) for subset in subsets]
    best_top1 = max(result["top1"] for result in results)
    best_subsets = sorted(
        [result["subset"] for result in results if np.isclose(result["top1"], best_top1)]
    )
    ceiling_subsets = sorted(
        [result["subset"] for result in results if result["ceiling_recovered"]]
    )
    return {
        "anchor_names": anchor_names,
        "pool_names": pool_names,
        "n_candidates": len(results),
        "results": results,
        "best_top1": best_top1,
        "best_n_correct": int(round(best_top1 * len(y))),
        "best_subsets": best_subsets,
        "n_ceiling_subsets": len(ceiling_subsets),
        "ceiling_subsets": ceiling_subsets,
        "canonical_winner": ceiling_subsets[0] if ceiling_subsets else best_subsets[0],
    }, subsets


def rf_loocv_top1_only(X: np.ndarray, y: np.ndarray) -> float:
    preds = loocv_preds(X, y)
    return top1_from_preds(y, preds)


def cheat_surah_id_top1(y: np.ndarray, surah_ids: list[int]) -> float:
    X = np.array(surah_ids, dtype=float).reshape(-1, 1)
    return rf_loocv_top1_only(X, y)


def build_perm_indices(n: int, n_perm: int, seed: int) -> list[np.ndarray]:
    rng = np.random.default_rng(seed)
    return [rng.permutation(n) for _ in range(n_perm)]


def batched(items: list[np.ndarray], batch_size: int) -> list[list[np.ndarray]]:
    return [items[i : i + batch_size] for i in range(0, len(items), batch_size)]


def arm_maxT_batch(
    perm_batch: list[np.ndarray],
    X_all: np.ndarray,
    y: np.ndarray,
    subset_indices: list[list[int]],
    target_n_correct: int,
) -> dict:
    ge_count = 0
    for perm_idx in perm_batch:
        y_perm = y[perm_idx]
        arm_hit = False
        for idx in subset_indices:
            if loocv_reaches_threshold(X_all[:, idx], y_perm, target_n_correct):
                ge_count += 1
                arm_hit = True
                break
        if arm_hit:
            continue
    return {
        "executed_n_perm": len(perm_batch),
        "ge_count": ge_count,
    }


def run_arm_batches(
    batch_args: list[tuple[list[np.ndarray], np.ndarray, np.ndarray, list[list[int]], int]]
) -> tuple[list[dict], str]:
    try:
        results = Parallel(n_jobs=OUTER_JOBS, backend="loky")(
            delayed(arm_maxT_batch)(*args) for args in batch_args
        )
        return results, "loky_processes"
    except PermissionError:
        results = Parallel(n_jobs=OUTER_JOBS, prefer="threads")(
            delayed(arm_maxT_batch)(*args) for args in batch_args
        )
        return results, "thread_fallback"


def arm_maxT_p(
    X_all: np.ndarray,
    y: np.ndarray,
    feature_names: list[str],
    candidate_subsets: list[tuple[str, ...]],
    observed_max_n_correct: int,
) -> dict:
    subset_indices = [
        [feature_names.index(name) for name in subset] for subset in candidate_subsets
    ]
    perm_indices = build_perm_indices(len(y), N_PERM, SEED)
    perm_batches = batched(perm_indices, PERM_BATCH_SIZE)
    batch_args = [
        (
            perm_batch,
            X_all,
            y,
            subset_indices,
            observed_max_n_correct,
        )
        for perm_batch in perm_batches
    ]
    batch_results, backend_used = run_arm_batches(batch_args)

    ge_count = int(sum(result["ge_count"] for result in batch_results))
    executed_n_perm = int(sum(result["executed_n_perm"] for result in batch_results))
    assert executed_n_perm == N_PERM

    return {
        "inference_mode": "armwise_maxT",
        "observed_max_n_correct": observed_max_n_correct,
        "observed_max_top1": float(observed_max_n_correct / len(y)),
        "n_perm": N_PERM,
        "ge_count": ge_count,
        "p_arm": float((1 + ge_count) / (N_PERM + 1)),
        "outer_jobs": OUTER_JOBS,
        "perm_batch_size": PERM_BATCH_SIZE,
        "candidate_count": len(candidate_subsets),
        "parallel_backend_used": backend_used,
    }


def verdict_from_searches(
    full15_ok: bool,
    mw5_ok: bool,
    phon_arm: dict,
    phon_maxT: dict | None,
    aug_arm: dict,
    aug_maxT: dict | None,
) -> str:
    if not full15_ok:
        return "NULL-BROKEN-BASELINE"
    if not mw5_ok:
        return "NULL-BROKEN-MW5"

    phon_pass = (
        phon_arm["n_ceiling_subsets"] > 0
        and phon_maxT is not None
        and phon_maxT["p_arm"] < ALPHA_BON
    )
    aug_pass = (
        aug_arm["n_ceiling_subsets"] > 0
        and aug_maxT is not None
        and aug_maxT["p_arm"] < ALPHA_BON
    )

    if phon_pass:
        return "SINGLE-PHON-FEATURE-SUFFICIENT"
    if aug_pass:
        return "SINGLE-AUGMENT-SUFFICIENT"
    return "MULTI-FEATURE-REQUIRED"


def main() -> None:
    X_full, y, surah_ids = build_design_matrix()
    feature_names = FULL_FEATURE_NAMES

    print("Running controls...")
    full15 = evaluate_subset(X_full, y, feature_names, tuple(FULL_FEATURE_NAMES))
    letter_count_only = evaluate_subset(X_full, y, feature_names, ("letter_count",))
    mw5_top1 = cheat_surah_id_top1(y, surah_ids)

    full15_ok = full15["ceiling_recovered"]
    mw5_ok = mw5_top1 >= 0.45

    print("Searching phon-only arm...")
    phon_arm, phon_subsets = evaluate_single_axis_arm(
        X_full, y, feature_names, PHONO_FEATURE_POOL, []
    )

    print("Searching letter_count-augmented arm...")
    aug_arm, aug_subsets = evaluate_single_axis_arm(
        X_full, y, feature_names, PHONO_FEATURE_POOL, ["letter_count"]
    )

    phon_maxT = None
    if phon_arm["n_ceiling_subsets"] > 0:
        print("Running arm-wise maxT for phon-only arm...")
        phon_maxT = arm_maxT_p(
            X_full,
            y,
            feature_names,
            phon_subsets,
            phon_arm["best_n_correct"],
        )

    aug_maxT = None
    if aug_arm["n_ceiling_subsets"] > 0:
        print("Running arm-wise maxT for letter_count-augmented arm...")
        aug_maxT = arm_maxT_p(
            X_full,
            y,
            feature_names,
            aug_subsets,
            aug_arm["best_n_correct"],
        )

    verdict = verdict_from_searches(
        full15_ok=full15_ok,
        mw5_ok=mw5_ok,
        phon_arm=phon_arm,
        phon_maxT=phon_maxT,
        aug_arm=aug_arm,
        aug_maxT=aug_maxT,
    )

    payload = {
        "id": "H-NEW-271",
        "title": "Minimal phonological family test for the muq cluster ceiling",
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "ceiling_top1": CEILING_TOP1,
        "outer_jobs": OUTER_JOBS,
        "perm_batch_size": PERM_BATCH_SIZE,
        "feature_space": {
            "full_feature_names": FULL_FEATURE_NAMES,
            "phon_feature_pool": PHONO_FEATURE_POOL,
            "duplicate_map": DUPLICATE_MAP,
        },
        "controls": {
            "full15": full15,
            "letter_count_only": letter_count_only,
            "mw5_cheat_surah_id_top1": mw5_top1,
            "baseline_reproduction_pass": full15_ok,
            "mw5_pass": mw5_ok,
        },
        "phon_only_arm": {
            **phon_arm,
            "maxT_permutation": phon_maxT,
            "pass": bool(
                phon_arm["n_ceiling_subsets"] > 0
                and phon_maxT is not None
                and phon_maxT["p_arm"] < ALPHA_BON
            ),
        },
        "lettercount_augmented_arm": {
            **aug_arm,
            "maxT_permutation": aug_maxT,
            "pass": bool(
                aug_arm["n_ceiling_subsets"] > 0
                and aug_maxT is not None
                and aug_maxT["p_arm"] < ALPHA_BON
            ),
        },
        "summary": {
            "overall_verdict": verdict,
        },
    }

    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Verdict: {verdict}")


if __name__ == "__main__":
    main()
