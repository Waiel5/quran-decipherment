#!/usr/bin/env python3
"""
Q023-F-01 — UAS rank verification + UAS top-10 cluster FR-cohesion vs length-matched null.

Pre-reg locked at SHA256 below. Verified at runtime.
"""

import hashlib
import json
import os
import random
import sys
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
PRE_REG = REPO / "surahs/Q023-al-muminun/preregs/Q023-F-01-uas-top10-fr-cluster-prereg.md"
EXPECTED_SHA = "9d16de4b7194c686feaf3f53b4d438504c2d9a1a63fe5f85dbdd59179d3d6834"

H_NEW_111 = REPO / "findings/phase-b-hypotheses/csv/h-new-111.json"
H_NEW_840 = REPO / "findings/phase-b-hypotheses/csv/h-new-840.json"
HAFS_TSV = REPO / "data/hafs-verse-counts.tsv"

OUT = REPO / "surahs/Q023-al-muminun/csv/Q023-F-01.json"

SEED = 20260509
N_PERMS = 10000


def verify_sha():
    actual = hashlib.sha256(PRE_REG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}")
        sys.exit(1)
    print(f"[ok] Pre-reg SHA256 verified: {actual}")


def load_fr_matrix():
    """Return D as a 115-indexed (1..114 inclusive) symmetric dict-of-dicts."""
    with open(H_NEW_111) as f:
        d = json.load(f)
    ut = d["D_matrix_upper_triangular"]
    D = {i: {} for i in range(1, 115)}
    for row in ut:
        i, j, dist = row[0], row[1], row[2]
        D[i][j] = dist
        D[j][i] = dist
    for i in range(1, 115):
        D[i][i] = 0.0
    return D


def load_uas_top10():
    """Read top-10 UAS surahs from h-new-840.json."""
    with open(H_NEW_840) as f:
        d = json.load(f)
    top15 = d["top_15"]
    top10 = [int(x["surah"]) for x in top15[:10]]
    return top10, top15


def load_verse_counts():
    """Return {surah_id: verse_count} from hafs-verse-counts.tsv."""
    vc = {}
    with open(HAFS_TSV) as f:
        for ln in f:
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            parts = ln.split()
            if len(parts) < 2:
                continue
            try:
                s = int(parts[0])
                n = int(parts[1])
                vc[s] = n
            except ValueError:
                continue
    return vc


def mean_pairwise_fr(D, surahs):
    n = len(surahs)
    s = 0.0
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            s += D[surahs[i]][surahs[j]]
            k += 1
    return s / k if k > 0 else float("nan")


def length_matched_pool(vc, target_surahs, exclude, tol=0.20, min_pool=5):
    """For each target surah, return list of corpus surahs within ±tol of its length, excluding `exclude`.

    If pool is smaller than min_pool, progressively expand tol (0.20 -> 0.40 -> 0.60 -> 1.0)."""
    pools = {}
    tols_used = {}
    for s in target_surahs:
        n = vc[s]
        for t in (tol, 0.40, 0.60, 1.0, 2.0):
            lo, hi = n * (1 - t), n * (1 + t)
            pl = [tt for tt in range(1, 115) if tt not in exclude and lo <= vc[tt] <= hi]
            if len(pl) >= min_pool:
                pools[s] = pl
                tols_used[s] = t
                break
        else:
            # fallback: nearest by absolute distance
            sorted_by_diff = sorted([tt for tt in range(1, 115) if tt not in exclude], key=lambda x: abs(vc[x] - n))
            pools[s] = sorted_by_diff[:max(min_pool, 5)]
            tols_used[s] = "nearest-5"
    return pools, tols_used


def main():
    verify_sha()
    D = load_fr_matrix()
    top10, top15_full = load_uas_top10()
    vc = load_verse_counts()
    print(f"[info] UAS top-10 surahs (rank-order): {top10}")
    print(f"[info] Q 23 UAS rank: {next((x['rank'] for x in top15_full if x['surah'] == 23), None)}")

    # Observed mean pairwise FR
    T_obs = mean_pairwise_fr(D, top10)
    print(f"[info] T_obs (mean pairwise FR within top-10): {T_obs:.6f}")

    # NULL 1: length-matched random subsets
    rng = random.Random(SEED)
    excluded = set(top10)
    pools, tols_used = length_matched_pool(vc, top10, exclude=excluded, tol=0.20)
    for s, pl in pools.items():
        print(f"[info] Q {s}: verse-count {vc[s]}, length-matched pool size {len(pl)}, tol={tols_used[s]}")

    null_lm = []
    failed = 0
    for _ in range(N_PERMS):
        sample = []
        seen = set()
        for s in top10:
            pl = pools[s]
            choices = [x for x in pl if x not in seen]
            if not choices:
                failed += 1
                break
            x = rng.choice(choices)
            sample.append(x)
            seen.add(x)
        if len(sample) == len(top10):
            null_lm.append(mean_pairwise_fr(D, sample))
    print(f"[info] length-matched null: {len(null_lm)} valid (failed {failed})")

    # NULL 2: strict random
    rng2 = random.Random(SEED + 1)
    null_rand = []
    all_surahs = list(range(1, 115))
    for _ in range(N_PERMS):
        sample = rng2.sample(all_surahs, len(top10))
        null_rand.append(mean_pairwise_fr(D, sample))

    def lower_tail_p(obs, null):
        k = sum(1 for v in null if v <= obs)
        return (k + 1) / (len(null) + 1)

    p_lm = lower_tail_p(T_obs, null_lm)
    p_rand = lower_tail_p(T_obs, null_rand)
    med_lm = sorted(null_lm)[len(null_lm) // 2]
    med_rand = sorted(null_rand)[len(null_rand) // 2]

    # MW-5 replication at higher seed
    rng3 = random.Random(SEED + 1000)
    null_rep = []
    for _ in range(N_PERMS):
        sample = []
        seen = set()
        for s in top10:
            pl = pools[s]
            choices = [x for x in pl if x not in seen]
            if not choices:
                break
            sample.append(rng3.choice(choices))
            seen.add(sample[-1])
        if len(sample) == len(top10):
            null_rep.append(mean_pairwise_fr(D, sample))
    p_rep = lower_tail_p(T_obs, null_rep)

    result = {
        "finding_id": "Q023-F-01",
        "pre_reg_sha256": EXPECTED_SHA,
        "seed": SEED,
        "n_perms": N_PERMS,
        "top10_surahs": top10,
        "uas_top15_rank_of_Q23": next((x["rank"] for x in top15_full if x["surah"] == 23), None),
        "T_obs": T_obs,
        "length_matched_null": {
            "n_valid": len(null_lm),
            "median": med_lm,
            "mean": sum(null_lm) / len(null_lm),
            "min": min(null_lm),
            "max": max(null_lm),
            "p_lower_tail": p_lm,
            "tols_used": tols_used,
        },
        "strict_random_null": {
            "n": N_PERMS,
            "median": med_rand,
            "mean": sum(null_rand) / N_PERMS,
            "p_lower_tail": p_rand,
        },
        "replication_seed_higher": {
            "seed": SEED + 1000,
            "n_valid": len(null_rep),
            "p_lower_tail": p_rep,
        },
        "verdict": (
            "PASS-DIRECTED" if p_lm <= 0.05 and T_obs < med_lm
            else "PRE-COMMIT-VIOLATION-NULL" if T_obs > med_lm
            else "NULL"
        ),
        "direction_observed": "OPPOSITE-OF-PRE-REG" if T_obs > med_lm else "AS-PRE-REG",
        "narrative": (
            "Top-10 UAS surahs are FR-DISPERSED (T_obs above null median); the "
            "pre-registered cohesion direction is violated. UAS top-10 is a "
            "multi-axis cluster, not a root-distribution cluster."
            if T_obs > med_lm else
            "Top-10 UAS surahs are FR-cohesive in the pre-registered direction."
        ),
        "bonferroni_family_alpha": 0.05 / 3,
        "verdict_bonferroni": (
            "PASS-DIRECTED-BONF" if p_lm <= 0.05/3 and T_obs < med_lm else "NOT-PASS-BONF"
        ),
        "rules_tuple": "(no-tashkeel, QAC-stem-roots, FR-K500-Dirichlet-0.5, Hafs-Kufan)",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))
    print(f"\n[ok] wrote {OUT}")


if __name__ == "__main__":
    main()
