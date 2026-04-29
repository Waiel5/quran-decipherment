#!/usr/bin/env python3
"""H-NEW-300: mean_manner alone (1-D) singleton nearest-neighbor test.
Pre-reg: findings/phase-b-hypotheses/h-new-300-manner-only-singleton-prereg.md
Seed: 20260423
"""
import hashlib
import json
import math
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG_MD = ROOT / "findings/phase-b-hypotheses/h-new-300-manner-only-singleton-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-300.json"

SEED = 20260423
N_PERM = 1000

LETTERS = {
    "ا": 3, "ل": 4, "م": 5, "ر": 6, "ك": 1, "ه": 2, "ي": 3,
    "ع": 2, "ص": 2, "ط": 1, "س": 2, "ق": 1, "ن": 5, "ح": 2,
}
# manner ordinal: stop=1, fricative=2, glide=3, lateral=4, nasal=5, trill=6

MUQ_LETTERS = {
    2: "الم", 3: "الم", 7: "المص", 10: "الر", 11: "الر", 12: "الر",
    13: "المر", 14: "الر", 15: "الر", 19: "كهيعص", 20: "طه",
    26: "طسم", 27: "طس", 28: "طسم", 29: "الم", 30: "الم",
    31: "الم", 32: "الم", 36: "يس", 38: "ص", 40: "حم", 41: "حم",
    42: "حمعسق", 43: "حم", 44: "حم", 45: "حم", 46: "حم",
    50: "ق", 68: "ن",
}

MULTI_CLUSTERS = {
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


def sha256_file(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def mean_manner(letters_str):
    lst = list(letters_str)
    return sum(LETTERS[l] for l in lst) / len(lst)


def main():
    random.seed(SEED)
    prereg_sha = sha256_file(PREREG_MD)
    print("=" * 60)
    print("H-NEW-300: 1-D mean_manner singleton nearest-neighbor")
    print("=" * 60)
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Seed: {SEED}")

    # Step 1: compute raw mean_manner per surah
    raw = {s: mean_manner(letters) for s, letters in MUQ_LETTERS.items()}
    print("\nRaw mean_manner per muq surah:")
    for cname, members in MULTI_CLUSTERS.items():
        vals = [raw[s] for s in members]
        print(f"  {cname}: surahs {members}")
        print(f"    manner values: {vals}")
        print(f"    mean: {sum(vals)/len(vals):.3f}")

    # Step 2: z-score against 19 multi-members
    multi_vals = [raw[s] for cname, mms in MULTI_CLUSTERS.items() for s in mms]
    mu = sum(multi_vals) / len(multi_vals)
    sd = math.sqrt(sum((x - mu) ** 2 for x in multi_vals) / (len(multi_vals) - 1))
    print(f"\nMulti-member mean: {mu:.4f}, sd: {sd:.4f}")
    z = {s: (v - mu) / sd for s, v in raw.items()}

    # Step 3: compute cluster centroids in z-space (scalar)
    centroids = {}
    for cname, members in MULTI_CLUSTERS.items():
        centroids[cname] = sum(z[s] for s in members) / len(members)
    print(f"\nCluster centroids (z-scored mean_manner):")
    for c, val in centroids.items():
        print(f"  {c}: {val:+.4f}")

    # Step 4: singleton nearest-cluster
    print("\nSingleton assignments:")
    results = []
    matches = 0
    for sname, sid in SINGLETONS.items():
        sz = z[sid]
        dists = {c: abs(sz - cz) for c, cz in centroids.items()}
        nearest = min(dists, key=dists.get)
        match = nearest in APRIORI[sname]
        if match:
            matches += 1
        results.append({
            "singleton": sname, "surah": sid, "z": sz,
            "dists": dists, "nearest": nearest,
            "apriori_accepted": APRIORI[sname], "match": match,
        })
        star = "✓" if match else "✗"
        print(f"  {sname} (Q {sid:3d}, z={sz:+.3f}): nearest={nearest}, "
              f"apriori={APRIORI[sname]} {star}")

    print(f"\nMatch count: {matches}/10")

    # Step 5: MW-5 null — shuffle cluster labels
    multi_list = [s for cname, mms in MULTI_CLUSTERS.items() for s in mms]
    sizes = {c: len(mms) for c, mms in MULTI_CLUSTERS.items()}
    null_matches = []
    for _ in range(N_PERM):
        shuffled = list(multi_list)
        random.shuffle(shuffled)
        new_clusters = {}
        idx = 0
        for c, sz_c in sizes.items():
            new_clusters[c] = shuffled[idx:idx + sz_c]
            idx += sz_c
        new_centroids = {c: sum(z[s] for s in members) / len(members)
                         for c, members in new_clusters.items()}
        nm = 0
        for sname, sid in SINGLETONS.items():
            dists = {c: abs(z[sid] - cz) for c, cz in new_centroids.items()}
            nearest = min(dists, key=dists.get)
            if nearest in APRIORI[sname]:
                nm += 1
        null_matches.append(nm)
    null_mean = sum(null_matches) / len(null_matches)
    p_perm = sum(1 for v in null_matches if v >= matches) / N_PERM

    print(f"\nMW-5 null:")
    print(f"  Null mean: {null_mean:.3f}")
    print(f"  p(null >= observed): {p_perm:.4f}")

    alpha_bon = 0.025
    # Decision rules
    cell_a = matches >= 7 and p_perm < alpha_bon
    cell_b = matches >= 8
    if cell_a and cell_b:
        verdict = "MAXIMAL-PARSIMONY-SINGULARLY-SUFFICIENT"
    elif cell_a and not cell_b:
        verdict = "PASS-ROBUST-WITH-1-SINGLETON-LOSS"
    else:
        verdict = "MULTI-DIM-REQUIRED-AT-SINGLETONS"

    print(f"\nVerdict: {verdict}")

    out = {
        "id": "H-NEW-300", "prereg_sha": prereg_sha, "seed": SEED,
        "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": alpha_bon,
        "raw_manner": raw, "cluster_centroids_z": centroids,
        "mu_multi": mu, "sd_multi": sd,
        "singleton_results": results,
        "match_count": matches, "null_mean": null_mean,
        "p_perm": p_perm, "cell_a_pass": cell_a, "cell_b_pass": cell_b,
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
