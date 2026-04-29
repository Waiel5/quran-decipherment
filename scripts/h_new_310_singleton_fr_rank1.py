#!/usr/bin/env python3
"""H-NEW-310: Full-singleton Fisher-Rao rank-1 nearest-neighbor.
Pre-reg: findings/phase-b-hypotheses/h-new-310-singleton-fr-rank1-prereg.md
"""
import hashlib
import json
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG_MD = ROOT / "findings/phase-b-hypotheses/h-new-310-singleton-fr-rank1-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-310.json"

SEED = 20260425
N_PERM = 1000

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


def load_fr_matrix():
    with open(H_NEW_111_JSON) as f:
        d = json.load(f)
    ut = d["D_matrix_upper_triangular"]
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in ut:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def cluster_of(surah_id, clusters):
    for cname, mms in clusters.items():
        if surah_id in mms:
            return cname
    return None  # non-muq or singleton


def rank1_neighbor(pivot, D, n=114):
    dists = [(s, D[pivot][s]) for s in range(1, n + 1) if s != pivot]
    dists.sort(key=lambda x: x[1])
    return dists[0]  # (surah_id, distance)


def main():
    random.seed(SEED)
    prereg_sha = sha256_file(PREREG_MD)
    print(f"=== H-NEW-310 ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Seed: {SEED}, N_perm: {N_PERM}")
    print()

    D = load_fr_matrix()

    # Analysis
    print("Singleton rank-1 FR nearest neighbor:")
    print(f"{'Singleton':<8} {'Q':>3}  {'Apriori':<20} {'Rank-1 surah':>11}  {'d':>7}  {'Cluster':<10} {'Match?'}")
    print("-" * 80)

    results = []
    matches = 0
    for sname, sid in SINGLETONS.items():
        neighbor, dist = rank1_neighbor(sid, D)
        ncluster = cluster_of(neighbor, MULTI_CLUSTERS)
        apriori = APRIORI[sname]
        match = (ncluster in apriori) if ncluster else False
        if match:
            matches += 1
        marker = "✓" if match else "✗"
        results.append({
            "singleton": sname, "surah": sid, "rank1_neighbor": neighbor,
            "rank1_distance": dist, "rank1_cluster": ncluster or "non-muq",
            "apriori_accepted": apriori, "match": match,
        })
        print(f"{sname:<8} {sid:>3}  {str(apriori):<20} {neighbor:>11}  "
              f"{dist:.4f}  {ncluster or 'non-muq':<10} {marker}")

    print(f"\nMatch count: {matches}/10")

    # MW-5 null
    print(f"\nMW-5 null (cluster-label shuffle on 19 multi-members)...")
    multi_list = [s for cname, mms in MULTI_CLUSTERS.items() for s in mms]
    sizes = {c: len(mms) for c, mms in MULTI_CLUSTERS.items()}
    null_matches = []
    for _ in range(N_PERM):
        shuffled = list(multi_list)
        random.shuffle(shuffled)
        new_clusters = {}
        idx = 0
        for c, sz in sizes.items():
            new_clusters[c] = shuffled[idx:idx + sz]
            idx += sz
        nm = 0
        for sname, sid in SINGLETONS.items():
            neighbor, _ = rank1_neighbor(sid, D)
            ncluster = cluster_of(neighbor, new_clusters)
            if ncluster and ncluster in APRIORI[sname]:
                nm += 1
        null_matches.append(nm)

    null_mean = sum(null_matches) / len(null_matches)
    p_perm = sum(1 for v in null_matches if v >= matches) / N_PERM
    print(f"Null mean: {null_mean:.3f}")
    print(f"p(null >= {matches}): {p_perm:.4f}")

    alpha_bon = 0.025
    cell_a = matches >= 5
    cell_b = p_perm < alpha_bon

    if cell_a and cell_b:
        verdict = "CONTENT-CLUSTERS-SINGLETONS-CORRECTLY (strict PASS)"
    elif cell_a:
        verdict = "DIRECTIONAL-PASS-PERMUTATION-MARGINAL"
    else:
        verdict = "NULL"
    print(f"\nCell A (≥5): {'PASS' if cell_a else 'FAIL'}")
    print(f"Cell B (p<α_bon): {'PASS' if cell_b else 'FAIL'}")
    print(f"Verdict: {verdict}")

    out = {
        "id": "H-NEW-310", "prereg_sha": prereg_sha, "seed": SEED,
        "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": alpha_bon,
        "results": results, "match_count": matches,
        "null_mean": null_mean, "p_perm": p_perm,
        "cell_a_pass": cell_a, "cell_b_pass": cell_b,
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
