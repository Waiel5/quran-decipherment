#!/usr/bin/env python3
"""
H-NEW-165.2 — Phonological codebook sensitivity sweep for the OQ-1 muq predictor.

Pre-reg:
  findings/phase-b-hypotheses/h-new-165-2-codebook-sensitivity-prereg.md

Parents:
  H-NEW-165
  H-NEW-232

This is a bounded sensitivity sweep over 4 locked codebooks:
  - baseline_h165_locked
  - watson_modern_voice
  - strict_pharyngeal_split
  - holes_glottal_ha_ayn
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
ALPHA_BON = 0.025
HNEW88_BASELINE = 0.4138
PRIMARY_THRESHOLD = 0.50
PRIMARY_PRESERVED_THRESHOLD = 18 / 29
BASELINE_EXPECTED_TOP1 = 19 / 29
BASELINE_EXPECTED_SINGLETON_MATCHES = 8

OUTPUT_JSON = Path(
    "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-165-2.json"
)

# ---------- canonical muq letter-set assignment (copied from H-NEW-165/232) ----------

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
MUQ_LETTERS = sorted(set().union(*SET_LETTERS.values()))
assert len(MUQ_LETTERS) == 14

TASK_SINGLETONS_8 = {"S", "Q", "N", "TH", "YS", "TS", "KHYAS", "HMASQ"}
SINGLETON_SETS_10 = {"ALMS", "ALMR", "KHYAS", "TH", "TS", "YS", "S", "HMASQ", "Q", "N"}
MULTI_CLUSTERS = {"ALM", "ALR", "HM", "TSM"}

APRIORI_ACCEPTED = {
    "ALMS": {"ALM"},
    "ALMR": {"ALM", "ALR"},
    "KHYAS": {"HM", "TSM"},
    "TH": {"TSM"},
    "TS": {"TSM"},
    "YS": {"ALR", "ALM"},
    "S": {"TSM"},
    "HMASQ": {"HM"},
    "Q": {"HM", "TSM"},
    "N": {"ALM", "ALR"},
}

# ---------- locked phonological ingredients ----------

BASE_MAKHRAJ = {
    "ا": 8,
    "ل": 3,
    "م": 1,
    "ر": 3,
    "ص": 3,
    "ك": 5,
    "ه": 8,
    "ي": 4,
    "ع": 7,
    "ط": 3,
    "س": 3,
    "ح": 7,
    "ن": 3,
    "ق": 6,
}

MANNER = {
    "ا": 0,
    "ل": 4,
    "م": 5,
    "ر": 6,
    "ص": 2,
    "ك": 1,
    "ه": 2,
    "ي": 3,
    "ع": 2,
    "ط": 1,
    "س": 2,
    "ح": 2,
    "ن": 5,
    "ق": 1,
}

CLASSICAL_VOICED = {"ا", "ل", "م", "ر", "ي", "ع", "ط", "ن"}
WATSON_MODERN_VOICED = {"ا", "ل", "م", "ر", "ي", "ع", "ن"}

EMPHATIC_SET = {"ص", "ط", "ق"}
PHARYNGEAL_HYBRID_SET = {"ص", "ط", "ق", "ع", "ح"}
PHARYNGEAL_STRICT_SET = {"ع", "ح"}
SONORANT_SET = {"ا", "ل", "م", "ر", "ي", "ن"}
STOP_SET = {"ك", "ط", "ق"}
IDHLAQ_SET = {"ر", "م", "ن", "ل"}
VOWEL_CARRIER_SET = {"ا", "ي"}
QALQALA_SET = {"ق", "ط"}

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

CODEBOOK_SPECS = [
    {
        "id": "baseline_h165_locked",
        "label": "Baseline locked H-165 codebook",
        "voice_set": CLASSICAL_VOICED,
        "pharyngeal_set": PHARYNGEAL_HYBRID_SET,
        "makhraj_overrides": {},
    },
    {
        "id": "watson_modern_voice",
        "label": "Watson-style modern voice recode",
        "voice_set": WATSON_MODERN_VOICED,
        "pharyngeal_set": PHARYNGEAL_HYBRID_SET,
        "makhraj_overrides": {},
    },
    {
        "id": "strict_pharyngeal_split",
        "label": "Strict throat-only pharyngeal recode",
        "voice_set": CLASSICAL_VOICED,
        "pharyngeal_set": PHARYNGEAL_STRICT_SET,
        "makhraj_overrides": {},
    },
    {
        "id": "holes_glottal_ha_ayn",
        "label": "Holes-style ha/ayn glottal makhraj recode",
        "voice_set": CLASSICAL_VOICED,
        "pharyngeal_set": PHARYNGEAL_HYBRID_SET,
        "makhraj_overrides": {"ح": 8, "ع": 8},
    },
]


def build_letter_features(spec: dict) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for letter in MUQ_LETTERS:
        makhraj = spec["makhraj_overrides"].get(letter, BASE_MAKHRAJ[letter])
        out[letter] = {
            "makhraj": float(makhraj),
            "voice": float(1 if letter in spec["voice_set"] else 0),
            "manner": float(MANNER[letter]),
            "emphatic": float(1 if letter in EMPHATIC_SET else 0),
            "pharyngeal": float(1 if letter in spec["pharyngeal_set"] else 0),
            "sonorant": float(1 if letter in SONORANT_SET else 0),
            "continuant": float(0 if letter in STOP_SET else 1),
            "idhlaq": float(1 if letter in IDHLAQ_SET else 0),
            "vowel_carrier": float(1 if letter in VOWEL_CARRIER_SET else 0),
        }
    return out


def letter_set_features(letter_set_name: str, letter_features: dict[str, dict[str, float]]) -> tuple[list[float], list[str]]:
    letters = SET_LETTERS[letter_set_name]
    n = len(letters)

    means: list[float] = []
    for fname in PER_LETTER_FEATURE_NAMES:
        vals = [letter_features[L][fname] for L in letters]
        means.append(float(np.mean(vals)))

    letter_count = float(n)
    frac_emphatic = float(sum(letter_features[L]["emphatic"] for L in letters) / n)
    frac_pharyngeal = float(sum(letter_features[L]["pharyngeal"] for L in letters) / n)
    frac_sonorant = float(sum(letter_features[L]["sonorant"] for L in letters) / n)
    frac_idhlaq = float(sum(letter_features[L]["idhlaq"] for L in letters) / n)
    has_qalqala = float(1 if any(L in QALQALA_SET for L in letters) else 0)

    fv = means + [
        letter_count,
        frac_emphatic,
        frac_pharyngeal,
        frac_sonorant,
        frac_idhlaq,
        has_qalqala,
    ]
    fn = [f"mean_{f}" for f in PER_LETTER_FEATURE_NAMES] + [
        "letter_count",
        "frac_emphatic",
        "frac_pharyngeal",
        "frac_sonorant",
        "frac_idhlaq",
        "has_qalqala",
    ]
    assert len(fv) == 15
    return fv, fn


def build_design_matrix(letter_features: dict[str, dict[str, float]]) -> tuple[np.ndarray, np.ndarray, list[str], list[int]]:
    rows = []
    y = []
    surah_ids = []
    feature_names = None
    for sid in MUQ_SURAHS:
        label = MUQ_ASSIGNMENTS[sid]
        fv, fn = letter_set_features(label, letter_features)
        if feature_names is None:
            feature_names = fn
        rows.append(fv)
        y.append(label)
        surah_ids.append(sid)
    X = np.array(rows, dtype=float)
    return X, np.array(y), feature_names, surah_ids


def loocv(X, y, clf_factory, k_top=(1, 3, 5)):
    n = X.shape[0]
    preds = np.empty(n, dtype=object)
    topk_correct = {k: 0 for k in k_top}
    classes_global = np.array(sorted(set(y.tolist())))

    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        X_tr = X[mask]
        y_tr = y[mask]
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
            top1_idx = int(np.argmax(probs))
            preds[i] = classes_local[top1_idx]
            ranked = sorted(zip(classes_local, probs), key=lambda kv: -kv[1])
            ranked_classes = [cls for cls, _ in ranked]
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
    return preds, acc, classes_global


def per_class_recall(y, preds) -> dict[str, float]:
    recall = {}
    for cls in sorted(set(y.tolist())):
        idx = np.where(y == cls)[0]
        recall[cls] = float(sum(preds[i] == cls for i in idx) / len(idx))
    return recall


def per_singleton_result(y, preds, surah_ids) -> tuple[dict[str, dict[str, object]], int]:
    per_sing: dict[str, dict[str, object]] = {}
    hits = 0
    for i, sid in enumerate(surah_ids):
        if y[i] in TASK_SINGLETONS_8:
            correct = bool(y[i] == preds[i])
            per_sing[str(sid)] = {
                "true": str(y[i]),
                "pred": str(preds[i]),
                "correct": correct,
            }
            if correct:
                hits += 1
    return per_sing, hits


def permutation_null(X, y, clf_factory, observed_top1, surah_ids, n_perm=N_PERM, seed=SEED) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    null_top1 = []
    ge_count = 0
    singleton_hit_ge1 = 0

    for _ in range(n_perm):
        y_sh = y.copy()
        rng.shuffle(y_sh)
        try:
            preds_sh, acc_sh, _ = loocv(X, y_sh, clf_factory, k_top=(1,))
            top1 = acc_sh["top1"]
            n_sing = 0
            for i, _sid in enumerate(surah_ids):
                if y_sh[i] in TASK_SINGLETONS_8 and preds_sh[i] == y_sh[i]:
                    n_sing += 1
        except Exception:
            top1 = 1.0 / len(set(y))
            n_sing = 0
        null_top1.append(top1)
        if top1 >= observed_top1:
            ge_count += 1
        if n_sing >= 1:
            singleton_hit_ge1 += 1

    null_top1_arr = np.array(null_top1)
    return {
        "n_perm": int(n_perm),
        "observed_top1": float(observed_top1),
        "p_value_primary": float((1 + ge_count) / (n_perm + 1)),
        "p_value_singleton_hit": float((1 + singleton_hit_ge1) / (n_perm + 1)),
        "null_mean": float(null_top1_arr.mean()),
        "null_std": float(null_top1_arr.std()),
        "null_q95": float(np.quantile(null_top1_arr, 0.95)),
        "null_q99": float(np.quantile(null_top1_arr, 0.99)),
        "null_max": float(null_top1_arr.max()),
        "ge_count": int(ge_count),
        "singleton_hit_ge1_count": int(singleton_hit_ge1),
    }


def compute_nearest_centroids(X_all, y_all, surah_ids) -> tuple[list[dict[str, object]], dict[str, list[float]]]:
    multi_mask = np.array([y in MULTI_CLUSTERS for y in y_all])
    single_mask = ~multi_mask

    X_multi = X_all[multi_mask]
    y_multi = y_all[multi_mask]
    sids_multi = [surah_ids[i] for i in range(len(surah_ids)) if multi_mask[i]]

    X_single = X_all[single_mask]
    y_single = y_all[single_mask]
    sids_single = [surah_ids[i] for i in range(len(surah_ids)) if single_mask[i]]

    mu = X_multi.mean(axis=0)
    sd = X_multi.std(axis=0)
    sd[sd == 0] = 1.0
    Xm_z = (X_multi - mu) / sd
    Xs_z = (X_single - mu) / sd

    clusters = sorted(MULTI_CLUSTERS)
    centroids: dict[str, np.ndarray] = {}
    for cls in clusters:
        idx = [i for i, value in enumerate(y_multi) if value == cls]
        centroids[cls] = Xm_z[idx].mean(axis=0)

    out_rows: list[dict[str, object]] = []
    for i in range(X_single.shape[0]):
        q = Xs_z[i]
        d_multi = np.linalg.norm(Xm_z - q, axis=1)
        nearest_idx = int(np.argmin(d_multi))
        d_cent = {cls: float(np.linalg.norm(centroids[cls] - q)) for cls in clusters}
        nearest_centroid = min(d_cent.items(), key=lambda kv: kv[1])[0]
        out_rows.append(
            {
                "surah": int(sids_single[i]),
                "truth_set": str(y_single[i]),
                "nearest_multi_surah": int(sids_multi[nearest_idx]),
                "nearest_multi_cluster": str(y_multi[nearest_idx]),
                "nearest_centroid_cluster": nearest_centroid,
                "nearest_centroid_distance": float(d_cent[nearest_centroid]),
                "distances_to_centroids": d_cent,
                "accepted_clusters": sorted(APRIORI_ACCEPTED[str(y_single[i])]),
                "match": bool(nearest_centroid in APRIORI_ACCEPTED[str(y_single[i])]),
            }
        )

    centroids_out = {cls: centroids[cls].round(8).tolist() for cls in clusters}
    return out_rows, centroids_out


def singleton_permutation_null(X_all, y_all, seed=SEED, n_perm=N_PERM) -> dict[str, float]:
    multi_mask = np.array([y in MULTI_CLUSTERS for y in y_all])
    single_mask = ~multi_mask

    X_multi = X_all[multi_mask]
    y_multi = y_all[multi_mask]
    X_single = X_all[single_mask]
    y_single = y_all[single_mask]

    mu = X_multi.mean(axis=0)
    sd = X_multi.std(axis=0)
    sd[sd == 0] = 1.0
    Xm_z = (X_multi - mu) / sd
    Xs_z = (X_single - mu) / sd

    rng = np.random.default_rng(seed)
    match_counts = []
    ge_count = 0

    observed_rows, _ = compute_nearest_centroids(X_all, y_all, MUQ_SURAHS)
    observed_matches = sum(1 for row in observed_rows if row["match"])

    for _ in range(n_perm):
        y_sh = y_multi.copy()
        rng.shuffle(y_sh)
        centroids: dict[str, np.ndarray] = {}
        for cls in sorted(MULTI_CLUSTERS):
            idx = [i for i, value in enumerate(y_sh) if value == cls]
            centroids[cls] = Xm_z[idx].mean(axis=0)

        matches = 0
        for i in range(X_single.shape[0]):
            q = Xs_z[i]
            d_cent = {cls: float(np.linalg.norm(centroids[cls] - q)) for cls in centroids}
            nearest_centroid = min(d_cent.items(), key=lambda kv: kv[1])[0]
            if nearest_centroid in APRIORI_ACCEPTED[str(y_single[i])]:
                matches += 1
        match_counts.append(matches)
        if matches >= observed_matches:
            ge_count += 1

    match_arr = np.array(match_counts)
    return {
        "observed_matches": int(observed_matches),
        "p_value": float((1 + ge_count) / (n_perm + 1)),
        "null_mean": float(match_arr.mean()),
        "null_std": float(match_arr.std()),
        "null_q95": float(np.quantile(match_arr, 0.95)),
        "null_q99": float(np.quantile(match_arr, 0.99)),
        "null_max": int(match_arr.max()),
        "ge_count": int(ge_count),
    }


def evaluate_variant(spec: dict) -> dict[str, object]:
    print(f"\n=== Variant: {spec['id']} ===", flush=True)
    letter_features = build_letter_features(spec)
    X, y, feature_names, surah_ids = build_design_matrix(letter_features)

    preds_cheat, acc_cheat, _ = loocv(
        np.array(surah_ids, dtype=float).reshape(-1, 1),
        y,
        lambda: RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1),
        k_top=(1, 3, 5),
    )
    mw5_top1 = acc_cheat["top1"]
    _ = preds_cheat

    clf_defs = {
        "rf": lambda: RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1),
        "logistic": lambda: LogisticRegression(C=1.0, solver="lbfgs", max_iter=2000, random_state=SEED),
    }
    classifier_results: dict[str, object] = {}

    for clf_name, clf_factory in clf_defs.items():
        preds, acc, _classes = loocv(X, y, clf_factory, k_top=(1, 3, 5))
        per_sing, n_sing_hits = per_singleton_result(y, preds, surah_ids)
        result_row: dict[str, object] = {
            "top1": float(acc["top1"]),
            "top3": float(acc["top3"]),
            "top5": float(acc["top5"]),
            "per_class_recall": per_class_recall(y, preds),
            "singleton_task_hits": int(n_sing_hits),
            "singleton_task_results": per_sing,
        }
        if clf_name == "rf":
            result_row["permutation_null"] = permutation_null(
                X, y, clf_factory, acc["top1"], surah_ids, n_perm=N_PERM, seed=SEED
            )
        classifier_results[clf_name] = result_row

    singleton_rows, centroids = compute_nearest_centroids(X, y, surah_ids)
    singleton_null = singleton_permutation_null(X, y, seed=SEED, n_perm=N_PERM)
    singleton_matches = sum(1 for row in singleton_rows if row["match"])

    rf_top1 = float(classifier_results["rf"]["top1"])
    rf_perm_p = float(classifier_results["rf"]["permutation_null"]["p_value_primary"])
    primary_retained = (rf_top1 > PRIMARY_THRESHOLD) and (rf_perm_p < ALPHA_BON)
    primary_preserved = primary_retained and (rf_top1 >= PRIMARY_PRESERVED_THRESHOLD)
    collapsed_below_h88 = (rf_top1 <= HNEW88_BASELINE) or (rf_perm_p >= 0.05)
    singleton_retained = (singleton_matches >= 7) and (singleton_null["p_value"] < ALPHA_BON)
    singleton_degraded = (singleton_matches <= 6) or (singleton_null["p_value"] >= 0.05)

    if primary_preserved and singleton_retained:
        verdict = "PRESERVED-BOTH"
    elif primary_preserved:
        verdict = "PRESERVED-PRIMARY-ONLY"
    elif primary_retained:
        verdict = "DEGRADED-BUT-RETAINS-PRIMARY"
    else:
        verdict = "DEGRADED"

    print(
        f"  RF top1={rf_top1:.4f} p={rf_perm_p:.4f} "
        f"singleton_matches={singleton_matches}/10 p={singleton_null['p_value']:.4f} "
        f"verdict={verdict}",
        flush=True,
    )

    return {
        "id": spec["id"],
        "label": spec["label"],
        "codebook_spec": {
            "voice_set": sorted(spec["voice_set"]),
            "pharyngeal_set": sorted(spec["pharyngeal_set"]),
            "makhraj_overrides": spec["makhraj_overrides"],
        },
        "feature_names": feature_names,
        "letter_features": letter_features,
        "mw5_cheat_surah_id_top1": float(mw5_top1),
        "classifier_results": classifier_results,
        "singleton_geometry": {
            "matches": int(singleton_matches),
            "rows": singleton_rows,
            "centroids": centroids,
            "permutation_null": singleton_null,
        },
        "variant_flags": {
            "primary_retained": bool(primary_retained),
            "primary_preserved": bool(primary_preserved),
            "collapsed_below_h88": bool(collapsed_below_h88),
            "singleton_retained": bool(singleton_retained),
            "singleton_degraded": bool(singleton_degraded),
        },
        "variant_verdict": verdict,
    }


def main() -> None:
    print("=== H-NEW-165.2 Codebook Sensitivity Sweep ===", flush=True)
    print(f"Seed: {SEED}", flush=True)

    variants = [evaluate_variant(spec) for spec in CODEBOOK_SPECS]
    variant_map = {variant["id"]: variant for variant in variants}

    baseline = variant_map["baseline_h165_locked"]
    baseline_reproduction_pass = (
        abs(baseline["classifier_results"]["rf"]["top1"] - BASELINE_EXPECTED_TOP1) < 1e-12
        and baseline["singleton_geometry"]["matches"] == BASELINE_EXPECTED_SINGLETON_MATCHES
    )

    perturbed = [variant for variant in variants if variant["id"] != "baseline_h165_locked"]
    n_primary_retained = sum(1 for variant in perturbed if variant["variant_flags"]["primary_retained"])
    n_primary_preserved = sum(1 for variant in perturbed if variant["variant_flags"]["primary_preserved"])
    n_singleton_retained = sum(1 for variant in perturbed if variant["variant_flags"]["singleton_retained"])
    any_collapsed_below_h88 = any(
        variant["variant_flags"]["collapsed_below_h88"] for variant in perturbed
    )

    if not baseline_reproduction_pass:
        overall_verdict = "NULL-BROKEN-PIPELINE"
    elif n_primary_retained == 3 and n_singleton_retained >= 2:
        overall_verdict = "ROBUST"
    elif n_primary_retained == 3:
        overall_verdict = "ROBUST-PRIMARY-EDGE-SENSITIVE"
    elif n_primary_retained in {1, 2}:
        overall_verdict = "MIXED"
    else:
        overall_verdict = "FRAGILE"

    out = {
        "id": "H-NEW-165.2",
        "title": "Phonological codebook sensitivity sweep for the OQ-1 muq predictor",
        "seed": SEED,
        "n_perm": N_PERM,
        "parents": ["H-NEW-165", "H-NEW-232"],
        "baseline_reference": {
            "h_new_165_rf_top1": BASELINE_EXPECTED_TOP1,
            "h_new_232_singleton_matches": BASELINE_EXPECTED_SINGLETON_MATCHES,
            "h_new_88_top1": HNEW88_BASELINE,
        },
        "thresholds": {
            "alpha_bon": ALPHA_BON,
            "primary_threshold": PRIMARY_THRESHOLD,
            "primary_preserved_threshold": PRIMARY_PRESERVED_THRESHOLD,
            "singleton_threshold_matches": 7,
        },
        "codebook_specs": [
            {
                "id": spec["id"],
                "label": spec["label"],
                "voice_set": sorted(spec["voice_set"]),
                "pharyngeal_set": sorted(spec["pharyngeal_set"]),
                "makhraj_overrides": spec["makhraj_overrides"],
            }
            for spec in CODEBOOK_SPECS
        ],
        "variants": variants,
        "summary": {
            "baseline_reproduction_pass": bool(baseline_reproduction_pass),
            "n_perturbed_variants": 3,
            "n_primary_retained": int(n_primary_retained),
            "n_primary_preserved": int(n_primary_preserved),
            "n_singleton_retained": int(n_singleton_retained),
            "any_collapsed_below_h88": bool(any_collapsed_below_h88),
            "overall_verdict": overall_verdict,
        },
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False))

    print("\n=== SUMMARY ===", flush=True)
    print(f"baseline reproduction pass: {baseline_reproduction_pass}", flush=True)
    print(f"primary retained in perturbed variants: {n_primary_retained}/3", flush=True)
    print(f"primary preserved in perturbed variants: {n_primary_preserved}/3", flush=True)
    print(f"singleton retained in perturbed variants: {n_singleton_retained}/3", flush=True)
    print(f"overall verdict: {overall_verdict}", flush=True)
    print(f"wrote {OUTPUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
