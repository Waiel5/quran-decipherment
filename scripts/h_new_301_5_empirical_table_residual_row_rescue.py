#!/usr/bin/env python3
"""H-NEW-301.5: empirical-table residual-row rescue over the H-NEW-301 pair family."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import random
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
PREREG_MD = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-301-5-empirical-table-residual-row-rescue-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-301-5.json"

SEED = 20260425
N_PERM = 20000
ALPHA = 0.05

CLUSTER_ORDER = ["ALM", "ALR", "HM", "TSM"]
TARGET_ROWS = ["YS", "N"]

LETTERS = {
    "ا": {"makhraj": 1, "voice": 0, "manner": 3, "emph": 0, "phar": 0,
          "son": 0, "cont": 1, "idhl": 0, "vc": 1, "qalq": 0},
    "ل": {"makhraj": 5, "voice": 1, "manner": 4, "emph": 0, "phar": 0,
          "son": 1, "cont": 1, "idhl": 1, "vc": 0, "qalq": 0},
    "م": {"makhraj": 8, "voice": 1, "manner": 5, "emph": 0, "phar": 0,
          "son": 1, "cont": 1, "idhl": 1, "vc": 0, "qalq": 0},
    "ر": {"makhraj": 5, "voice": 1, "manner": 6, "emph": 0, "phar": 0,
          "son": 1, "cont": 1, "idhl": 1, "vc": 0, "qalq": 0},
    "ك": {"makhraj": 4, "voice": 0, "manner": 1, "emph": 0, "phar": 0,
          "son": 0, "cont": 0, "idhl": 0, "vc": 0, "qalq": 0},
    "ه": {"makhraj": 1, "voice": 0, "manner": 2, "emph": 0, "phar": 1,
          "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
    "ي": {"makhraj": 4, "voice": 1, "manner": 3, "emph": 0, "phar": 0,
          "son": 1, "cont": 1, "idhl": 0, "vc": 1, "qalq": 0},
    "ع": {"makhraj": 2, "voice": 1, "manner": 2, "emph": 0, "phar": 1,
          "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
    "ص": {"makhraj": 6, "voice": 0, "manner": 2, "emph": 1, "phar": 1,
          "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
    "ط": {"makhraj": 6, "voice": 1, "manner": 1, "emph": 1, "phar": 1,
          "son": 0, "cont": 0, "idhl": 0, "vc": 0, "qalq": 1},
    "س": {"makhraj": 6, "voice": 0, "manner": 2, "emph": 0, "phar": 0,
          "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
    "ق": {"makhraj": 3, "voice": 1, "manner": 1, "emph": 0, "phar": 1,
          "son": 0, "cont": 0, "idhl": 0, "vc": 0, "qalq": 1},
    "ن": {"makhraj": 5, "voice": 1, "manner": 5, "emph": 0, "phar": 0,
          "son": 1, "cont": 1, "idhl": 1, "vc": 0, "qalq": 0},
    "ح": {"makhraj": 2, "voice": 0, "manner": 2, "emph": 0, "phar": 1,
          "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
}

MUQ_LETTERS = {
    2: "الم", 3: "الم", 7: "المص", 10: "الر", 11: "الر", 12: "الر",
    13: "المر", 14: "الر", 15: "الر", 19: "كهيعص", 20: "طه",
    26: "طسم", 27: "طس", 28: "طسم", 29: "الم", 30: "الم",
    31: "الم", 32: "الم", 36: "يس", 38: "ص", 40: "حم", 41: "حم",
    42: "حمعسق", 43: "حم", 44: "حم", 45: "حم", 46: "حم",
    50: "ق", 68: "ن",
}

MULTI = {
    "ALM": [2, 3, 29, 30, 31, 32],
    "ALR": [10, 11, 12, 14, 15],
    "HM": [40, 41, 43, 44, 45, 46],
    "TSM": [26, 28],
}

SINGLETONS = {
    "ALMS": 7, "ALMR": 13, "KHYAS": 19, "TH": 20, "TS": 27,
    "YS": 36, "S": 38, "HMASQ": 42, "Q": 50, "N": 68,
}

APRIORI = {
    "ALMS": ["ALM"],
    "ALMR": ["ALM", "ALR"],
    "KHYAS": ["HM", "TSM"],
    "TH": ["TSM"],
    "TS": ["TSM"],
    "YS": ["HM"],
    "S": ["TSM"],
    "HMASQ": ["TSM"],
    "Q": ["HM", "TSM"],
    "N": ["ALM", "ALR"],
}

FEATURE_NAMES = [
    "mean_makhraj", "mean_voice", "mean_manner", "mean_emphatic",
    "mean_pharyngeal", "mean_sonorant", "mean_continuant",
    "mean_idhlaq", "mean_vowel_carrier", "has_qalqala", "letter_count",
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compute_features(letters_str: str) -> list[float]:
    chars = list(letters_str)
    n_chars = len(chars)
    metrics = [LETTERS[ch] for ch in chars]
    return [
        sum(x["makhraj"] for x in metrics) / n_chars,
        sum(x["voice"] for x in metrics) / n_chars,
        sum(x["manner"] for x in metrics) / n_chars,
        sum(x["emph"] for x in metrics) / n_chars,
        sum(x["phar"] for x in metrics) / n_chars,
        sum(x["son"] for x in metrics) / n_chars,
        sum(x["cont"] for x in metrics) / n_chars,
        sum(x["idhl"] for x in metrics) / n_chars,
        sum(x["vc"] for x in metrics) / n_chars,
        1 if any(x["qalq"] for x in metrics) else 0,
        n_chars,
    ]


def zscore_col(values: list[float], reference: list[float]) -> list[float]:
    mu = sum(reference) / len(reference)
    sd = math.sqrt(sum((x - mu) ** 2 for x in reference) / (len(reference) - 1))
    if sd == 0:
        return [0.0 for _ in values]
    return [(v - mu) / sd for v in values]


def pair_label(idx_pair: tuple[int, int]) -> str:
    return " + ".join(FEATURE_NAMES[i] for i in idx_pair)


def build_pair_cache() -> tuple[dict[int, list[float]], list[dict[str, object]]]:
    feats = {surah: compute_features(letters) for surah, letters in MUQ_LETTERS.items()}
    all_surahs = list(feats.keys())
    multi_surahs = [s for members in MULTI.values() for s in members]
    pair_cache = []
    for idx_pair in itertools.combinations(range(len(FEATURE_NAMES)), 2):
        zvecs = {s: [] for s in all_surahs}
        for j in idx_pair:
            ref_vals = [feats[s][j] for s in multi_surahs]
            vals = [feats[s][j] for s in all_surahs]
            z_list = zscore_col(vals, ref_vals)
            for surah, zval in zip(all_surahs, z_list):
                zvecs[surah].append(zval)
        pair_cache.append(
            {
                "idx_pair": idx_pair,
                "pair": [FEATURE_NAMES[i] for i in idx_pair],
                "pair_label": pair_label(idx_pair),
                "zvecs": zvecs,
            }
        )
    return feats, pair_cache


def compute_centroids(
    zvecs: dict[int, list[float]], multi_assignments: dict[str, list[int]]
) -> dict[str, list[float]]:
    return {
        cluster: [
            sum(zvecs[s][k] for s in members) / len(members)
            for k in range(2)
        ]
        for cluster, members in multi_assignments.items()
    }


def compute_distances(
    point: list[float], centroids: dict[str, list[float]]
) -> dict[str, float]:
    return {
        cluster: math.sqrt(
            sum((point[k] - centroid[k]) ** 2 for k in range(2))
        )
        for cluster, centroid in centroids.items()
    }


def nearest_cluster(dists: dict[str, float]) -> str:
    return min(CLUSTER_ORDER, key=lambda cluster: (dists[cluster], cluster))


def evaluate_pair(
    pair_entry: dict[str, object], multi_assignments: dict[str, list[int]]
) -> dict[str, object]:
    zvecs = pair_entry["zvecs"]
    centroids = compute_centroids(zvecs, multi_assignments)
    rescue_count = 0
    positive_margin_sum = 0.0
    total_hits = 0
    per_singleton = []
    target_rows = []

    for singleton, surah in SINGLETONS.items():
        point = zvecs[surah]
        dists = compute_distances(point, centroids)
        nearest = nearest_cluster(dists)
        accepted = APRIORI[singleton]
        match = nearest in accepted
        if match:
            total_hits += 1

        accepted_best = min(dists[c] for c in accepted)
        rejected_best = min(dists[c] for c in CLUSTER_ORDER if c not in accepted)
        margin = rejected_best - accepted_best

        row = {
            "singleton": singleton,
            "surah": surah,
            "nearest_cluster": nearest,
            "accepted_clusters": accepted,
            "match": match,
            "accepted_best_distance": accepted_best,
            "rejected_best_distance": rejected_best,
            "margin": margin,
            "distances_to_centroids": dists,
        }
        per_singleton.append(row)

        if singleton in TARGET_ROWS:
            rescued = margin > 0.0
            if rescued:
                rescue_count += 1
                positive_margin_sum += margin
            target_rows.append(
                {
                    **row,
                    "rescued": rescued,
                }
            )

    return {
        "pair": pair_entry["pair"],
        "pair_label": pair_entry["pair_label"],
        "centroids_z": centroids,
        "rescue_count": rescue_count,
        "positive_margin_sum": positive_margin_sum,
        "total_hits": total_hits,
        "per_singleton": per_singleton,
        "target_rows": target_rows,
    }


def better_targeted(a: dict[str, object], b: dict[str, object]) -> bool:
    if a["rescue_count"] != b["rescue_count"]:
        return a["rescue_count"] > b["rescue_count"]
    if not math.isclose(a["positive_margin_sum"], b["positive_margin_sum"], rel_tol=0, abs_tol=1e-12):
        return a["positive_margin_sum"] > b["positive_margin_sum"]
    return a["pair_label"] < b["pair_label"]


def main() -> None:
    random.seed(SEED)
    prereg_sha = sha256_file(PREREG_MD)
    print("=== H-NEW-301.5 ===")
    print(f"Pre-reg SHA: {prereg_sha}")

    _, pair_cache = build_pair_cache()
    print(f"Testing {len(pair_cache)} pairs")

    observed = [evaluate_pair(entry, MULTI) for entry in pair_cache]
    observed.sort(
        key=lambda row: (
            -int(row["rescue_count"]),
            -float(row["positive_margin_sum"]),
            row["pair_label"],
        )
    )
    best = observed[0]

    print(f"Observed best pair: {best['pair_label']}")
    print(f"Observed targeted rescue: {best['rescue_count']} / 2")
    print(f"Observed positive margin sum: {best['positive_margin_sum']:.12f}")
    print(f"Observed total hits: {best['total_hits']} / 10")

    count_two = sum(1 for row in observed if row["rescue_count"] == 2)
    top_total_hits_among_two = max(
        (row["total_hits"] for row in observed if row["rescue_count"] == 2),
        default=0,
    )
    print(f"Pairs rescuing both targets: {count_two} / {len(observed)}")
    print(f"Highest total hits among 2/2-rescue pairs: {top_total_hits_among_two}")

    multi_list = [s for members in MULTI.values() for s in members]
    sizes = {cluster: len(members) for cluster, members in MULTI.items()}

    ge_targeted = 0
    ge_count_only = 0
    null_best_rescue = []
    null_best_margin = []

    print(f"Running maxT null with n_perm={N_PERM} ...")
    for _ in range(N_PERM):
        shuffled = list(multi_list)
        random.shuffle(shuffled)
        new_multi = {}
        idx = 0
        for cluster in CLUSTER_ORDER:
            size = sizes[cluster]
            new_multi[cluster] = shuffled[idx:idx + size]
            idx += size

        perm_best = None
        perm_max_rescue = -1
        for entry in pair_cache:
            row = evaluate_pair(entry, new_multi)
            if row["rescue_count"] > perm_max_rescue:
                perm_max_rescue = row["rescue_count"]
            if perm_best is None or better_targeted(row, perm_best):
                perm_best = row

        null_best_rescue.append(perm_best["rescue_count"])
        null_best_margin.append(perm_best["positive_margin_sum"])

        if (perm_best["rescue_count"], perm_best["positive_margin_sum"]) >= (
            best["rescue_count"],
            best["positive_margin_sum"],
        ):
            ge_targeted += 1
        if perm_max_rescue >= best["rescue_count"]:
            ge_count_only += 1

    p_maxt = (1 + ge_targeted) / (1 + N_PERM)
    p_count_only = (1 + ge_count_only) / (1 + N_PERM)

    null_sorted_margin = sorted(null_best_margin)
    q95_margin = null_sorted_margin[int(math.ceil(0.95 * N_PERM)) - 1]
    q99_margin = null_sorted_margin[int(math.ceil(0.99 * N_PERM)) - 1]

    if best["rescue_count"] == 2 and p_maxt < ALPHA:
        verdict = "TARGETED-RESIDUAL-RESCUE"
    elif best["rescue_count"] == 2:
        verdict = "DESCRIPTIVE-ONLY"
    else:
        verdict = "NULL"

    print(f"p_maxT: {p_maxt:.12f}")
    print(f"p_count_only: {p_count_only:.12f}")
    print(f"Verdict: {verdict}")

    out = {
        "id": "H-NEW-301.5",
        "title": "Empirical-table residual-row rescue over the 55-pair singleton family",
        "prereg_sha256": prereg_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha": ALPHA,
        "target_rows": TARGET_ROWS,
        "observed_best_pair": best["pair"],
        "observed_best_pair_label": best["pair_label"],
        "observed_rescue_count": best["rescue_count"],
        "observed_positive_margin_sum": best["positive_margin_sum"],
        "observed_total_hits": best["total_hits"],
        "pairs_rescuing_both_targets": count_two,
        "highest_total_hits_among_two_rescue_pairs": top_total_hits_among_two,
        "top10_targeted_pairs": [
            {
                "pair": row["pair"],
                "pair_label": row["pair_label"],
                "rescue_count": row["rescue_count"],
                "positive_margin_sum": row["positive_margin_sum"],
                "total_hits": row["total_hits"],
            }
            for row in observed[:10]
        ],
        "best_pair_target_rows": best["target_rows"],
        "best_pair_per_singleton": best["per_singleton"],
        "best_pair_centroids_z": best["centroids_z"],
        "null_best_rescue_mean": sum(null_best_rescue) / len(null_best_rescue),
        "null_best_rescue_counts": {
            str(k): null_best_rescue.count(k) for k in sorted(set(null_best_rescue))
        },
        "null_best_margin_mean": sum(null_best_margin) / len(null_best_margin),
        "null_best_margin_sd": (
            math.sqrt(
                sum((x - (sum(null_best_margin) / len(null_best_margin))) ** 2 for x in null_best_margin)
                / len(null_best_margin)
            )
        ),
        "null_best_margin_q95": q95_margin,
        "null_best_margin_q99": q99_margin,
        "n_perm_ge_targeted_obs": ge_targeted,
        "n_perm_ge_count_only_obs": ge_count_only,
        "p_maxT": p_maxt,
        "p_count_only": p_count_only,
        "verdict": verdict,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
