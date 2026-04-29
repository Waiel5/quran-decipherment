#!/usr/bin/env python3
"""H-NEW-301: minimal 2-feature subset for singleton 8/10 match.
Pre-reg: findings/phase-b-hypotheses/h-new-301-minimal-2feature-singleton-prereg.md
"""
import hashlib
import itertools
import json
import math
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG_MD = ROOT / "findings/phase-b-hypotheses/h-new-301-minimal-2feature-singleton-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-301.json"

SEED = 20260424
N_PERM = 1000

# Tajwīd codebook — reused from H-NEW-165/271 baseline
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
    "ALMS": ["ALM"], "ALMR": ["ALM", "ALR"], "KHYAS": ["HM", "TSM"],
    "TH": ["TSM"], "TS": ["TSM"], "YS": ["ALM", "ALR"],
    "S": ["TSM"], "HMASQ": ["HM"], "Q": ["HM", "TSM"],
    "N": ["ALM", "ALR"],
}

FEATURE_NAMES = [
    "mean_makhraj", "mean_voice", "mean_manner", "mean_emphatic",
    "mean_pharyngeal", "mean_sonorant", "mean_continuant",
    "mean_idhlaq", "mean_vowel_carrier", "has_qalqala", "letter_count",
]


def sha256_file(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def compute_features(letters_str):
    lst = list(letters_str)
    n = len(lst)
    ms = [LETTERS[L] for L in lst]
    return [
        sum(x["makhraj"] for x in ms) / n,
        sum(x["voice"] for x in ms) / n,
        sum(x["manner"] for x in ms) / n,
        sum(x["emph"] for x in ms) / n,
        sum(x["phar"] for x in ms) / n,
        sum(x["son"] for x in ms) / n,
        sum(x["cont"] for x in ms) / n,
        sum(x["idhl"] for x in ms) / n,
        sum(x["vc"] for x in ms) / n,
        1 if any(x["qalq"] for x in ms) else 0,
        n,  # letter_count
    ]


def zscore_col(vals, ref):
    mu = sum(ref) / len(ref)
    sd = math.sqrt(sum((x - mu) ** 2 for x in ref) / (len(ref) - 1))
    if sd == 0:
        return [0.0 for _ in vals], mu, sd
    return [(v - mu) / sd for v in vals], mu, sd


def score_pair(feats, idx_pair, multi, singletons, apriori):
    """Compute singleton match count for a given feature pair index tuple."""
    # Extract 2-D z-scored vectors per surah
    all_surahs = list(feats.keys())
    multi_surahs = [s for cname, mms in multi.items() for s in mms]
    zvecs = {s: [] for s in all_surahs}
    for j in idx_pair:
        ref_vals = [feats[s][j] for s in multi_surahs]
        vals = [feats[s][j] for s in all_surahs]
        z_list, _, _ = zscore_col(vals, ref_vals)
        for s, z in zip(all_surahs, z_list):
            zvecs[s].append(z)

    # Cluster centroids
    centroids = {c: [sum(zvecs[s][k] for s in mms) / len(mms) for k in range(2)]
                 for c, mms in multi.items()}

    # Singleton nearest
    matches = 0
    results = []
    for sname, sid in singletons.items():
        sz = zvecs[sid]
        dists = {c: math.sqrt(sum((sz[k] - cv[k]) ** 2 for k in range(2)))
                 for c, cv in centroids.items()}
        nearest = min(dists, key=dists.get)
        match = nearest in apriori[sname]
        if match:
            matches += 1
        results.append({"singleton": sname, "nearest": nearest, "match": match})
    return matches, results


def main():
    random.seed(SEED)
    prereg_sha = sha256_file(PREREG_MD)
    print(f"=== H-NEW-301 ===")
    print(f"Pre-reg SHA: {prereg_sha}")

    # Compute features for all 29 muq surahs
    feats = {s: compute_features(letters) for s, letters in MUQ_LETTERS.items()}

    # Enumerate all C(11, 2) = 55 pairs
    n_feats = len(FEATURE_NAMES)
    all_pairs = list(itertools.combinations(range(n_feats), 2))
    print(f"Testing {len(all_pairs)} pairs")

    # Score each pair
    pair_results = []
    for idx_pair in all_pairs:
        matches, per_sing = score_pair(feats, idx_pair, MULTI, SINGLETONS, APRIORI)
        name_pair = [FEATURE_NAMES[i] for i in idx_pair]
        pair_results.append({"pair": name_pair, "matches": matches,
                              "per_singleton": per_sing})
    pair_results.sort(key=lambda x: -x["matches"])

    max_matches = pair_results[0]["matches"]
    best_pairs = [r for r in pair_results if r["matches"] == max_matches]
    print(f"\nMax matches: {max_matches}")
    print(f"N pairs at max: {len(best_pairs)}")
    for r in best_pairs[:10]:
        print(f"  {r['pair']}: {r['matches']}/10")

    # Top 10 pairs
    print(f"\nTop 10 pairs (by match count):")
    for r in pair_results[:10]:
        print(f"  {r['pair']}: {r['matches']}/10")

    # Distribution of match counts
    from collections import Counter
    count_dist = Counter(r["matches"] for r in pair_results)
    print(f"\nMatch count distribution: {dict(sorted(count_dist.items()))}")

    # MW-5 maxT permutation
    print(f"\nMaxT permutation (n_perm={N_PERM})...")
    multi_list = [s for cname, mms in MULTI.items() for s in mms]
    sizes = {c: len(mms) for c, mms in MULTI.items()}

    null_max_matches = []
    for perm_i in range(N_PERM):
        shuffled = list(multi_list)
        random.shuffle(shuffled)
        new_multi = {}
        idx = 0
        for c, sz_c in sizes.items():
            new_multi[c] = shuffled[idx:idx + sz_c]
            idx += sz_c
        # For each pair, compute match count under shuffled labels
        pair_match_null = []
        for idx_pair in all_pairs:
            matches_null, _ = score_pair(feats, idx_pair, new_multi,
                                          SINGLETONS, APRIORI)
            pair_match_null.append(matches_null)
        null_max_matches.append(max(pair_match_null))

    null_mean = sum(null_max_matches) / len(null_max_matches)
    p_max = sum(1 for v in null_max_matches if v >= max_matches) / N_PERM
    print(f"Null max-matches mean: {null_mean:.3f}")
    print(f"p(max_null ≥ observed_max): {p_max:.4f}")

    alpha_bon = 0.025
    cell_a = max_matches >= 8
    cell_b = p_max < alpha_bon
    if cell_a and cell_b:
        verdict = "MINIMAL-2D-SUFFICIENT"
    elif cell_a:
        verdict = "MARGINAL (pair exists but permutation-suggestive)"
    else:
        verdict = "MULTI-DIM-GT-2-REQUIRED"
    print(f"\nVerdict: {verdict}")

    out = {
        "id": "H-NEW-301", "prereg_sha": prereg_sha, "seed": SEED,
        "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": alpha_bon,
        "max_matches": max_matches, "n_best_pairs": len(best_pairs),
        "best_pairs": [r["pair"] for r in best_pairs],
        "top20_pairs": [{"pair": r["pair"], "matches": r["matches"]}
                        for r in pair_results[:20]],
        "match_distribution": dict(sorted(count_dist.items())),
        "null_mean_max": null_mean, "p_maxT": p_max,
        "cell_a_pass": cell_a, "cell_b_pass": cell_b, "verdict": verdict,
        "best_pair_per_singleton": best_pairs[0]["per_singleton"]
            if best_pairs else None,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
