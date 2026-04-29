#!/usr/bin/env python3
"""
H-NEW-232 — OQ-1 singleton nearest-neighbor placement.

Pre-reg: findings/phase-b-hypotheses/h-new-232-oq1-singleton-nearest-neighbor-prereg.md
Parent:  H-NEW-165 (RF LOOCV top-1 = 0.6552, multi-member cluster ceiling)

Re-frames the OQ-1 singleton problem as cross-class nearest-neighbor rather than
LOOCV multi-class classification. Uses the 15-dim LOCKED phonological feature
vector from H-NEW-165, verbatim. Computes Euclidean distance (z-scored w.r.t.
the 19 multi-member-cluster surahs only) from each of 10 singleton surahs to:
  (i) each of 19 multi-member surahs
  (ii) each of 4 cluster centroids (ALM, ALR, HM, TSM).
Reports the nearest of each and a pre-committed "coherence match" against the
a-priori classical-tajwīd profile declared in the pre-reg.

MW-5 cheat control: 1000-permutation null shuffling multi-member labels.

Seed: 20260419.
"""
from __future__ import annotations

import json
from pathlib import Path
from collections import Counter

import numpy as np

SEED = 20260419
N_PERM = 1000

OUTPUT_JSON = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-232.json")

# ---------- canonical muq letter-set assignment (copied verbatim from h-new-165) ----------

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

PER_LETTER_FEATURE_NAMES = [
    "makhraj", "voice", "manner", "emphatic", "pharyngeal",
    "sonorant", "continuant", "idhlaq", "vowel_carrier",
]
QALQALA_LETTERS = {"ق", "ط"}

# 10 singleton letter-sets (all 1-member classes in MUQ_ASSIGNMENTS)
SINGLETON_SETS = {"ALMS", "ALMR", "KHYAS", "TH", "TS", "YS", "S", "HMASQ", "Q", "N"}
# 4 multi-member clusters
MULTI_CLUSTERS = {"ALM", "ALR", "HM", "TSM"}

# Pre-committed a-priori classical-tajwīd accepted-cluster set per singleton.
# Each singleton maps to a set of acceptable clusters.  See pre-reg §Interpretation rules.
APRIORI_ACCEPTED = {
    "ALMS":  {"ALM"},
    "ALMR":  {"ALM", "ALR"},
    "KHYAS": {"HM", "TSM"},
    "TH":    {"TSM"},
    "TS":    {"TSM"},
    "YS":    {"ALR", "ALM"},
    "S":     {"TSM"},
    "HMASQ": {"HM"},
    "Q":     {"HM", "TSM"},
    "N":     {"ALM", "ALR"},
}

# Singleton → surah ID (the one muq surah holding that letter-set)
SINGLETON_SURAH = {
    "ALMS": 7, "ALMR": 13, "KHYAS": 19, "TH": 20, "TS": 27,
    "YS": 36, "S": 38, "HMASQ": 42, "Q": 50, "N": 68,
}

# ---------- feature-matrix builder (verbatim from h-new-165) ----------

def letter_set_features(letter_set_name: str) -> tuple[list[float], list[str]]:
    letters = SET_LETTERS[letter_set_name]
    n = len(letters)
    means = []
    for fname in PER_LETTER_FEATURE_NAMES:
        vals = [LETTER_FEATURES[L][fname] for L in letters]
        means.append(float(np.mean(vals)))
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
    return fv, fn


def build_design_matrix():
    rows, y, surah_ids = [], [], []
    feature_names = None
    for sid in MUQ_SURAHS:
        ls = MUQ_ASSIGNMENTS[sid]
        fv, fn = letter_set_features(ls)
        if feature_names is None:
            feature_names = fn
        rows.append(fv); y.append(ls); surah_ids.append(sid)
    X = np.array(rows, dtype=float)
    return X, np.array(y), feature_names, surah_ids


def compute_nearest(X_multi, y_multi, sids_multi, X_single, y_single, sids_single):
    """Z-score using multi-member stats only, compute centroids & distances."""
    mu = X_multi.mean(axis=0)
    sd = X_multi.std(axis=0); sd[sd == 0] = 1.0
    Xm_z = (X_multi - mu) / sd
    Xs_z = (X_single - mu) / sd

    clusters = sorted(MULTI_CLUSTERS)
    centroids = {}
    for c in clusters:
        idx = [i for i, v in enumerate(y_multi) if v == c]
        centroids[c] = Xm_z[idx].mean(axis=0)

    out_per_singleton = []
    for i in range(X_single.shape[0]):
        q = Xs_z[i]
        # distances to each multi-member surah
        d_multi = np.linalg.norm(Xm_z - q, axis=1)
        nearest_idx = int(np.argmin(d_multi))
        # distances to 4 centroids
        d_cent = {c: float(np.linalg.norm(centroids[c] - q)) for c in clusters}
        nearest_cent = min(d_cent.items(), key=lambda kv: kv[1])[0]
        out_per_singleton.append({
            "surah": int(sids_single[i]),
            "truth_set": str(y_single[i]),
            "nearest_multi_surah": int(sids_multi[nearest_idx]),
            "nearest_multi_cluster": str(y_multi[nearest_idx]),
            "nearest_multi_distance": float(d_multi[nearest_idx]),
            "distances_to_centroids": d_cent,
            "nearest_centroid_cluster": nearest_cent,
            "nearest_centroid_distance": d_cent[nearest_cent],
        })
    return out_per_singleton, centroids, clusters


def coherence_rate(out_per_singleton) -> tuple[int, int]:
    matches = 0
    for r in out_per_singleton:
        accepted = APRIORI_ACCEPTED[r["truth_set"]]
        if r["nearest_centroid_cluster"] in accepted:
            matches += 1
    return matches, len(out_per_singleton)


# ---------- permutation null (MW-5 cheat control) ----------

def shuffled_match_rate(X_multi, y_multi, X_single, y_single, rng, clusters_required=MULTI_CLUSTERS):
    """Shuffle the 19 multi-member labels, recompute centroids + nearest-centroid match-rate."""
    y_sh = y_multi.copy()
    rng.shuffle(y_sh)
    # Ensure all 4 clusters still present after shuffle (they always will be, since we
    # just permute the EXISTING label vector with fixed multiset of ALM/ALR/HM/TSM)
    mu = X_multi.mean(axis=0)
    sd = X_multi.std(axis=0); sd[sd == 0] = 1.0
    Xm_z = (X_multi - mu) / sd
    Xs_z = (X_single - mu) / sd
    centroids = {}
    for c in sorted(clusters_required):
        idx = [i for i, v in enumerate(y_sh) if v == c]
        if not idx:
            # shouldn't happen — shuffle preserves labels — but safety:
            return None
        centroids[c] = Xm_z[idx].mean(axis=0)
    matches = 0
    for i in range(X_single.shape[0]):
        q = Xs_z[i]
        d_cent = {c: float(np.linalg.norm(centroids[c] - q)) for c in centroids}
        nearest_cent = min(d_cent.items(), key=lambda kv: kv[1])[0]
        if nearest_cent in APRIORI_ACCEPTED[str(y_single[i])]:
            matches += 1
    return matches


def main() -> None:
    print("=== H-NEW-232 OQ-1 Singleton Nearest-Neighbor ===", flush=True)
    print(f"Seed: {SEED}", flush=True)

    X_all, y_all, feature_names, sids_all = build_design_matrix()

    multi_mask = np.array([y in MULTI_CLUSTERS for y in y_all])
    single_mask = ~multi_mask

    X_multi = X_all[multi_mask]; y_multi = y_all[multi_mask]; sids_multi = [sids_all[i] for i in range(len(sids_all)) if multi_mask[i]]
    X_single = X_all[single_mask]; y_single = y_all[single_mask]; sids_single = [sids_all[i] for i in range(len(sids_all)) if single_mask[i]]

    print(f"multi-member: n={len(y_multi)} ({Counter(y_multi.tolist())})", flush=True)
    print(f"singleton: n={len(y_single)} ({Counter(y_single.tolist())})", flush=True)
    assert len(y_multi) == 19
    assert len(y_single) == 10

    # --- primary: nearest-neighbor computation ---
    out_per_singleton, centroids, clusters = compute_nearest(
        X_multi, y_multi, sids_multi, X_single, y_single, sids_single
    )

    print("\n--- Singleton nearest-neighbor table ---", flush=True)
    print(f"{'Sing':<6} {'Q':<5} {'NearMulti':<5} {'NearCluster':<6} {'NearCent':<6}  {'APrior':<20} {'Match'}", flush=True)
    match_list = []
    for r in out_per_singleton:
        accepted = APRIORI_ACCEPTED[r["truth_set"]]
        is_match = r["nearest_centroid_cluster"] in accepted
        match_list.append(is_match)
        print(
            f"{r['truth_set']:<6} Q{r['surah']:<4} Q{r['nearest_multi_surah']:<4} "
            f"{r['nearest_multi_cluster']:<6} {r['nearest_centroid_cluster']:<6}  "
            f"{str(sorted(accepted)):<20} {'YES' if is_match else 'NO'}",
            flush=True,
        )

    matches, total = coherence_rate(out_per_singleton)
    match_rate = matches / total
    print(f"\nObserved coherence: {matches}/{total} = {match_rate:.3f}", flush=True)

    # --- MW-5 shuffled-label null ---
    print(f"\nRunning MW-5 permutation null (n={N_PERM})…", flush=True)
    rng = np.random.default_rng(SEED)
    null_matches = []
    ge_count = 0
    for p in range(N_PERM):
        m = shuffled_match_rate(X_multi, y_multi.copy(), X_single, y_single, rng)
        if m is None:
            continue
        null_matches.append(m)
        if m >= matches:
            ge_count += 1
        if (p + 1) % 250 == 0:
            print(f"  perm {p+1}/{N_PERM} mean={np.mean(null_matches):.3f} ge={ge_count}", flush=True)
    null_arr = np.array(null_matches)
    p_value = (1 + ge_count) / (len(null_arr) + 1)
    print(f"  null mean = {null_arr.mean():.3f}  std = {null_arr.std():.3f}  max = {int(null_arr.max())}", flush=True)
    print(f"  p = (1+{ge_count}) / ({len(null_arr)}+1) = {p_value:.4f}", flush=True)

    # --- Verdict per pre-reg decision rule ---
    PRIMARY_THRESHOLD = 7
    WEAK_THRESHOLD_LO = 5
    WEAK_THRESHOLD_HI = 6
    ALPHA_BON = 0.025
    ALPHA_WEAK = 0.05

    pass_primary = (matches >= PRIMARY_THRESHOLD) and (p_value < ALPHA_BON)
    pass_weak = (WEAK_THRESHOLD_LO <= matches <= WEAK_THRESHOLD_HI) and (p_value < ALPHA_WEAK)

    if pass_primary:
        verdict = "PASS-COHERENT"
    elif pass_weak:
        verdict = "PASS-WEAK"
    else:
        verdict = "NULL"

    print(f"\n=== VERDICT: {verdict} ===", flush=True)
    print(f"  matches = {matches}/{total} (primary threshold ≥ {PRIMARY_THRESHOLD})", flush=True)
    print(f"  p = {p_value:.4f} (α_bon = {ALPHA_BON})", flush=True)

    # --- Persist JSON ---
    out = {
        "id": "H-NEW-232",
        "title": "OQ-1 singleton nearest-neighbor placement — phonological interpretation of 10 singleton letter-sets",
        "seed": SEED,
        "parent": "H-NEW-165",
        "n_multi_member_surahs": int(X_multi.shape[0]),
        "n_singletons": int(X_single.shape[0]),
        "feature_names": feature_names,
        "centroids_z": {c: centroids[c].tolist() for c in centroids},
        "apriori_accepted_clusters": {k: sorted(list(v)) for k, v in APRIORI_ACCEPTED.items()},
        "per_singleton_results": out_per_singleton,
        "observed_matches": matches,
        "observed_match_rate": match_rate,
        "null_stats": {
            "n_perm": int(len(null_arr)),
            "null_mean_matches": float(null_arr.mean()),
            "null_std_matches": float(null_arr.std()),
            "null_max_matches": int(null_arr.max()),
            "null_q95_matches": float(np.quantile(null_arr, 0.95)),
            "null_q99_matches": float(np.quantile(null_arr, 0.99)),
            "ge_count": int(ge_count),
            "p_value": float(p_value),
        },
        "verdict": verdict,
        "verdict_criteria": {
            "primary_threshold_matches": PRIMARY_THRESHOLD,
            "primary_threshold_p": ALPHA_BON,
            "weak_threshold_matches_range": [WEAK_THRESHOLD_LO, WEAK_THRESHOLD_HI],
            "weak_threshold_p": ALPHA_WEAK,
        },
        "bonferroni_family": "h-new-232-oq1-singleton",
        "bonferroni_k": 2,
        "alpha_bon": ALPHA_BON,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUTPUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
