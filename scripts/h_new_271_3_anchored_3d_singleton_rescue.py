#!/usr/bin/env python3
"""H-NEW-271.3: anchored 3-D singleton rescue after H-NEW-271.2."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts/h_new_271_muq_minimal_phon_family.py"
PREREG_MD = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-271-3-anchored-3d-singleton-rescue-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-271-3.json"

SEED = 20260419
N_PERM = 1000
ALPHA = 0.05
ANCHOR_PAIR = ("mean_manner", "mean_vowel_carrier")
BASELINE_H232 = 8

SINGLETONS = {
    "ALMS": 7,
    "ALMR": 13,
    "KHYAS": 19,
    "TH": 20,
    "TS": 27,
    "YS": 36,
    "S": 38,
    "HMASQ": 42,
    "Q": 50,
    "N": 68,
}

APRIORI = {
    "ALMS": ["ALM"],
    "ALMR": ["ALM", "ALR"],
    "KHYAS": ["HM", "TSM"],
    "TH": ["TSM"],
    "TS": ["TSM"],
    "YS": ["ALM", "ALR"],
    "S": ["TSM"],
    "HMASQ": ["HM"],
    "Q": ["HM", "TSM"],
    "N": ["ALM", "ALR"],
}


def load_h271_module():
    spec = importlib.util.spec_from_file_location("h_new_271_locked", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load locked H-NEW-271 script")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def split_multi_single(module):
    X_all, y_all, sids_all = module.build_design_matrix()
    feature_names = list(module.FULL_FEATURE_NAMES)
    multi_mask = np.array([label in module.MULTI_MEMBER_CLASSES for label in y_all])
    single_mask = ~multi_mask
    return {
        "X_multi": X_all[multi_mask],
        "y_multi": y_all[multi_mask],
        "sids_multi": [sids_all[i] for i in range(len(sids_all)) if multi_mask[i]],
        "X_single": X_all[single_mask],
        "y_single": y_all[single_mask],
        "sids_single": [sids_all[i] for i in range(len(sids_all)) if single_mask[i]],
        "feature_names": feature_names,
    }


def zscore_against_multi(X_multi: np.ndarray, X_single: np.ndarray):
    mu = X_multi.mean(axis=0)
    sd = X_multi.std(axis=0)
    sd[sd == 0] = 1.0
    return (X_multi - mu) / sd, (X_single - mu) / sd, mu, sd


def triple_label(triple: tuple[str, str, str]) -> str:
    return " + ".join(triple)


def build_triple_cache(module):
    split = split_multi_single(module)
    feature_names = split["feature_names"]
    augment_axes = [
        name for name in module.PHONO_FEATURE_POOL if name not in set(ANCHOR_PAIR)
    ]
    caches = {}
    for axis in augment_axes:
        triple = ANCHOR_PAIR + (axis,)
        idx = [feature_names.index(name) for name in triple]
        Xm_z, Xs_z, mu, sd = zscore_against_multi(
            split["X_multi"][:, idx], split["X_single"][:, idx]
        )
        caches[axis] = {
            "triple": triple,
            "triple_label": triple_label(triple),
            "Xm_z": Xm_z,
            "Xs_z": Xs_z,
            "mu": mu,
            "sd": sd,
        }
    split["caches"] = caches
    split["augment_axes"] = augment_axes
    return split


def nearest_results_for_centroids(
    Xm_z: np.ndarray,
    Xs_z: np.ndarray,
    y_multi: np.ndarray,
    y_single: np.ndarray,
    sids_multi: list[int],
    sids_single: list[int],
    cluster_order: list[str],
):
    centroids = {
        cluster: Xm_z[np.where(y_multi == cluster)[0]].mean(axis=0)
        for cluster in cluster_order
    }

    singleton_results = []
    match_count = 0
    total_nearest_centroid_distance = 0.0
    nearest_agreement_count = 0

    for i, truth in enumerate(y_single.tolist()):
        q = Xs_z[i]
        d_multi = np.linalg.norm(Xm_z - q, axis=1)
        nearest_multi_idx = int(np.argmin(d_multi))
        d_cent = {
            cluster: float(np.linalg.norm(centroids[cluster] - q))
            for cluster in cluster_order
        }
        nearest_centroid_cluster = min(d_cent, key=d_cent.get)
        nearest_multi_cluster = str(y_multi[nearest_multi_idx])
        match = nearest_centroid_cluster in APRIORI[truth]
        if match:
            match_count += 1
        if nearest_centroid_cluster == nearest_multi_cluster:
            nearest_agreement_count += 1
        total_nearest_centroid_distance += d_cent[nearest_centroid_cluster]

        singleton_results.append(
            {
                "singleton": truth,
                "surah": int(sids_single[i]),
                "accepted_clusters": APRIORI[truth],
                "z_triple": [float(value) for value in q.tolist()],
                "nearest_multi_surah": int(sids_multi[nearest_multi_idx]),
                "nearest_multi_cluster": nearest_multi_cluster,
                "nearest_multi_distance": float(d_multi[nearest_multi_idx]),
                "distances_to_centroids": d_cent,
                "nearest_centroid_cluster": nearest_centroid_cluster,
                "nearest_centroid_distance": d_cent[nearest_centroid_cluster],
                "match": match,
            }
        )

    return {
        "centroids_z": {cluster: centroids[cluster].tolist() for cluster in cluster_order},
        "singleton_results": singleton_results,
        "match_count": match_count,
        "match_rate": match_count / len(singleton_results),
        "total_nearest_centroid_distance": total_nearest_centroid_distance,
        "nearest_agreement_count": nearest_agreement_count,
    }


def evaluate_observed_candidates(module):
    payload = build_triple_cache(module)
    cluster_order = sorted(module.MULTI_MEMBER_CLASSES)
    y_multi = payload["y_multi"]
    y_single = payload["y_single"]
    sids_multi = payload["sids_multi"]
    sids_single = payload["sids_single"]

    candidate_results = []
    for axis in payload["augment_axes"]:
        cache = payload["caches"][axis]
        summary = nearest_results_for_centroids(
            cache["Xm_z"],
            cache["Xs_z"],
            y_multi,
            y_single,
            sids_multi,
            sids_single,
            cluster_order,
        )
        candidate_results.append(
            {
                "augmentation_axis": axis,
                "anchor_pair": list(ANCHOR_PAIR),
                "triple": list(cache["triple"]),
                "triple_label": cache["triple_label"],
                "multi_reference_mean": [float(v) for v in cache["mu"].tolist()],
                "multi_reference_sd": [float(v) for v in cache["sd"].tolist()],
                **summary,
            }
        )

    candidate_results.sort(
        key=lambda row: (
            -row["match_count"],
            row["total_nearest_centroid_distance"],
            row["augmentation_axis"],
        )
    )
    return payload, candidate_results


def permuted_match_count(
    Xm_z: np.ndarray,
    Xs_z: np.ndarray,
    y_perm: np.ndarray,
    y_single: np.ndarray,
    cluster_order: list[str],
) -> int:
    centroids = {
        cluster: Xm_z[np.where(y_perm == cluster)[0]].mean(axis=0)
        for cluster in cluster_order
    }
    matches = 0
    for i, truth in enumerate(y_single.tolist()):
        q = Xs_z[i]
        nearest_centroid = min(
            cluster_order,
            key=lambda cluster: float(np.linalg.norm(centroids[cluster] - q)),
        )
        if nearest_centroid in APRIORI[truth]:
            matches += 1
    return matches


def run_maxt_null(module, payload, observed_best_hits: int):
    rng = np.random.default_rng(SEED)
    cluster_order = sorted(module.MULTI_MEMBER_CLASSES)
    y_multi = payload["y_multi"]
    y_single = payload["y_single"]
    caches = payload["caches"]

    ge_count = 0
    null_max_hits = []
    null_per_axis = {axis: [] for axis in payload["augment_axes"]}

    for _ in range(N_PERM):
        y_perm = y_multi.copy()
        rng.shuffle(y_perm)
        perm_counts = {}
        for axis in payload["augment_axes"]:
            cache = caches[axis]
            hits = permuted_match_count(
                cache["Xm_z"], cache["Xs_z"], y_perm, y_single, cluster_order
            )
            perm_counts[axis] = hits
            null_per_axis[axis].append(hits)
        max_hits = max(perm_counts.values())
        null_max_hits.append(max_hits)
        if max_hits >= observed_best_hits:
            ge_count += 1

    null_max_arr = np.array(null_max_hits, dtype=float)
    return {
        "ge_count": ge_count,
        "p_maxT": (1 + ge_count) / (N_PERM + 1),
        "null_max_hits": null_max_arr,
        "null_per_axis": {
            axis: [int(value) for value in values] for axis, values in null_per_axis.items()
        },
    }


def verdict_for(best_hits: int, p_maxT: float) -> str:
    if best_hits > BASELINE_H232 and p_maxT < ALPHA:
        return "SIGNIFICANT-3D-IMPROVEMENT"
    if best_hits >= BASELINE_H232 and p_maxT < ALPHA:
        return "SIGNIFICANT-3D-RESCUE"
    return "NO-MAXT-3D-RESCUE"


def main() -> None:
    module = load_h271_module()
    prereg_sha = hashlib.sha256(PREREG_MD.read_bytes()).hexdigest()

    payload, candidate_results = evaluate_observed_candidates(module)
    best = candidate_results[0]
    null = run_maxt_null(module, payload, best["match_count"])
    p_maxT = float(null["p_maxT"])
    verdict = verdict_for(best["match_count"], p_maxT)

    any_ge_8 = any(row["match_count"] >= BASELINE_H232 for row in candidate_results)
    any_gt_8 = any(row["match_count"] > BASELINE_H232 for row in candidate_results)
    co_best_triples = [
        row["triple"]
        for row in candidate_results
        if row["match_count"] == best["match_count"]
        and np.isclose(
            row["total_nearest_centroid_distance"],
            best["total_nearest_centroid_distance"],
        )
    ]

    out = {
        "id": "H-NEW-271-3",
        "title": "Anchored 3-D singleton rescue after H-NEW-271.2",
        "prereg_sha256": prereg_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha": ALPHA,
        "anchor_pair": list(ANCHOR_PAIR),
        "feature_source": "H-NEW-271 locked deduplicated phonological pool",
        "candidate_augmentations": payload["augment_axes"],
        "candidate_count": len(payload["augment_axes"]),
        "accepted_sets_source": "H-NEW-232 / H-NEW-271.2 verbatim",
        "apriori_sets": APRIORI,
        "singletons": SINGLETONS,
        "comparison_baseline": {
            "h_new_232_hit_bar": BASELINE_H232,
            "h_new_271_2_best_raw_pair": list(ANCHOR_PAIR),
            "h_new_271_2_best_raw_hits": BASELINE_H232,
        },
        "candidate_results": candidate_results,
        "best_triple": best["triple"],
        "best_triple_label": best["triple_label"],
        "best_augmentation_axis": best["augmentation_axis"],
        "best_match_count": best["match_count"],
        "best_match_rate": best["match_rate"],
        "best_total_nearest_centroid_distance": best["total_nearest_centroid_distance"],
        "co_best_triples": co_best_triples,
        "any_triple_reaches_8_of_10": any_ge_8,
        "any_triple_improves_on_8_of_10": any_gt_8,
        "best_minus_h271_2_raw_hits": int(best["match_count"] - BASELINE_H232),
        "null_stats": {
            "familywise_max_mean": float(null["null_max_hits"].mean()),
            "familywise_max_std": float(null["null_max_hits"].std()),
            "familywise_max_q95": float(np.quantile(null["null_max_hits"], 0.95)),
            "familywise_max_q99": float(np.quantile(null["null_max_hits"], 0.99)),
            "familywise_max_max": int(null["null_max_hits"].max()),
            "ge_count": int(null["ge_count"]),
            "p_maxT": p_maxT,
            "per_axis_means": {
                axis: float(np.mean(values))
                for axis, values in null["null_per_axis"].items()
            },
        },
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print("=== H-NEW-271.3 ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Anchor pair: {' + '.join(ANCHOR_PAIR)}")
    print(f"Candidate count: {len(payload['augment_axes'])}")
    print(f"Best triple: {best['triple_label']}")
    print(f"Best hits: {best['match_count']}/10 ({best['match_rate']:.3f})")
    print(f"Any triple >= 8/10: {any_ge_8}")
    print(f"Any triple > 8/10: {any_gt_8}")
    print(f"Corrected p_maxT: {p_maxT:.6f}")
    print(f"Verdict: {verdict}")
    print(f"Wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
