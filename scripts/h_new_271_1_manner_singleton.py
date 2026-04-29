#!/usr/bin/env python3
"""H-NEW-271.1: 1-D mean_manner singleton propagation follow-up.

This script reuses the locked H-NEW-271 codebook and restricts the singleton
comparison to the single mean_manner axis. The comparison is made against the
H-NEW-232 accepted cluster sets.
"""
from __future__ import annotations

import importlib.util
import json
import math
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts/h_new_271_muq_minimal_phon_family.py"
PREREG_MD = ROOT / "findings/phase-b-hypotheses/h-new-271-1-manner-singleton-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-271-1.json"

SEED = 20260419
N_PERM = 1000
ALPHA_BON = 0.025

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


def mean_manner_for_label(module, label: str) -> float:
    letters = module.SET_LETTERS[label]
    return sum(module.LETTER_FEATURES[ch]["manner"] for ch in letters) / len(letters)


def main() -> None:
    random.seed(SEED)
    module = load_h271_module()
    prereg_sha = __import__("hashlib").sha256(PREREG_MD.read_bytes()).hexdigest()

    raw = {
        sid: mean_manner_for_label(module, label)
        for sid, label in module.MUQ_ASSIGNMENTS.items()
    }

    multi_classes = {
        cname: [sid for sid, label in module.MUQ_ASSIGNMENTS.items() if label == cname]
        for cname in module.MULTI_MEMBER_CLASSES
    }
    multi_ids = [sid for ids in multi_classes.values() for sid in ids]

    mu = sum(raw[sid] for sid in multi_ids) / len(multi_ids)
    sd = math.sqrt(
        sum((raw[sid] - mu) ** 2 for sid in multi_ids) / (len(multi_ids) - 1)
    )
    z = {sid: (value - mu) / sd for sid, value in raw.items()}

    centroids = {
        cname: sum(z[sid] for sid in ids) / len(ids) for cname, ids in multi_classes.items()
    }

    singleton_results = []
    match_count = 0
    for sname, sid in SINGLETONS.items():
        sz = z[sid]
        centroid_dists = {cname: abs(sz - cval) for cname, cval in centroids.items()}
        nearest_cluster = min(centroid_dists, key=centroid_dists.get)

        nearest_surah = min(multi_ids, key=lambda other: abs(sz - z[other]))
        nearest_surah_cluster = module.MUQ_ASSIGNMENTS[nearest_surah]

        match = nearest_cluster in APRIORI[sname]
        if match:
            match_count += 1

        singleton_results.append(
            {
                "singleton": sname,
                "surah": sid,
                "raw_mean_manner": raw[sid],
                "z": sz,
                "nearest_multi_surah": nearest_surah,
                "nearest_multi_cluster": nearest_surah_cluster,
                "nearest_multi_distance": abs(sz - z[nearest_surah]),
                "nearest_cluster": nearest_cluster,
                "nearest_cluster_distance": centroid_dists[nearest_cluster],
                "apriori_accepted": APRIORI[sname],
                "match": match,
            }
        )

    shuffled_pool = list(multi_ids)
    sizes = {cname: len(ids) for cname, ids in multi_classes.items()}
    null_matches = []
    for _ in range(N_PERM):
        shuffled = list(shuffled_pool)
        random.shuffle(shuffled)
        shuffled_classes = {}
        idx = 0
        for cname, size in sizes.items():
            shuffled_classes[cname] = shuffled[idx : idx + size]
            idx += size

        shuffled_centroids = {
            cname: sum(z[sid] for sid in ids) / len(ids)
            for cname, ids in shuffled_classes.items()
        }

        count = 0
        for sname, sid in SINGLETONS.items():
            nearest_cluster = min(
                shuffled_centroids, key=lambda cname: abs(z[sid] - shuffled_centroids[cname])
            )
            if nearest_cluster in APRIORI[sname]:
                count += 1
        null_matches.append(count)

    null_mean = sum(null_matches) / len(null_matches)
    ge_count = sum(1 for value in null_matches if value >= match_count)
    p_perm = ge_count / N_PERM

    cell_a_pass = match_count >= 6 and p_perm < ALPHA_BON
    cell_b_pass = match_count >= 8 and p_perm < ALPHA_BON
    if cell_b_pass:
        verdict = "H-NEW-232-LEVEL-RETAINED"
    elif cell_a_pass:
        verdict = "SUBBASELINE-STRUCTURE-RETAINED"
    else:
        verdict = "MULTI-DIM-REQUIRED-AT-SINGLETONS"

    payload = {
        "id": "H-NEW-271-1",
        "title": "1-D mean_manner singleton propagation follow-up to H-NEW-271",
        "prereg_sha256": prereg_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "feature_source": "H-NEW-271 locked codebook",
        "feature_axis": "mean_manner",
        "controls": {
            "multi_member_count": len(multi_ids),
            "singleton_count": len(SINGLETONS),
        },
        "raw_mean_manner": raw,
        "multi_member_mean": mu,
        "multi_member_sd": sd,
        "cluster_centroids_z": centroids,
        "singleton_results": singleton_results,
        "match_count": match_count,
        "match_rate": match_count / len(SINGLETONS),
        "null_mean": null_mean,
        "ge_count": ge_count,
        "p_perm": p_perm,
        "cell_a_pass": cell_a_pass,
        "cell_b_pass": cell_b_pass,
        "verdict": verdict,
        "apriori_sets": APRIORI,
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("=== H-NEW-271-1 ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Axis: mean_manner")
    print(f"Singleton matches: {match_count}/10")
    print(f"Null mean: {null_mean:.3f}")
    print(f"p_perm: {p_perm:.3f} ({ge_count}/1000)")
    print(f"Verdict: {verdict}")
    print(f"Wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
