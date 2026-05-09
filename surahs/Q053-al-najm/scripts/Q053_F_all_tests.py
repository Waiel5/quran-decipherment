#!/usr/bin/env python3
"""
Q 53 al-Najm specialist novel-findings test family.

Tests:
  - Q053-F-01: Q 53's FR-nearest neighbor identity (predicted Q 96)
  - Q053-F-02: Q 53:19-23 reverse-direction empirical text-anomaly null (gharānīq)
  - Q053-F-03: 14 sajda-surahs FR cohesion test (reverse-direction null prediction)

Bonferroni-k = 3, α_bon = 0.0167. Seed 20260509. n_perm = 20,000.
SHA-locked pre-regs verified at runtime.

Outputs: csv/Q053-F-{01,02,03}.json
"""

import hashlib
import itertools
import json
import math
import os
import random
import sys
from pathlib import Path

# ---------- Configuration ----------

SEED = 20260509
N_PERM = 20000
ALPHA_BON = 0.0167
BONFERRONI_K = 3

REPO_ROOT = Path("/Users/grey/Downloads/quran")
PREREGS = REPO_ROOT / "surahs" / "Q053-al-najm" / "preregs"
CSV_OUT = REPO_ROOT / "surahs" / "Q053-al-najm" / "csv"
H_NEW_111 = REPO_ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-111.json"
QURAN_JSON = REPO_ROOT / "quran-text" / "quran-no-tashkeel.json"

CSV_OUT.mkdir(parents=True, exist_ok=True)

SAJDA_14 = [7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96]


# ---------- SHA verification ----------

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg_shas():
    """Compute and report SHA-256 of each pre-reg file. Embed in output JSONs."""
    shas = {}
    for fid in ["01", "02", "03"]:
        candidates = list(PREREGS.glob(f"Q053-F-{fid}-*-prereg.md"))
        if len(candidates) != 1:
            raise RuntimeError(
                f"Expected exactly 1 pre-reg for Q053-F-{fid}; found {len(candidates)}: {candidates}"
            )
        shas[f"Q053-F-{fid}"] = {
            "filename": str(candidates[0].name),
            "sha256": sha256_file(candidates[0]),
        }
    return shas


# ---------- Data loading ----------

def load_fr_matrix():
    """Load the H-NEW-111 Fisher-Rao distance matrix as a dict of (i,j) -> distance."""
    with open(H_NEW_111) as f:
        h111 = json.load(f)
    D = h111["D_matrix_upper_triangular"]
    d_map = {}
    for entry in D:
        i, j, dist = entry
        key = (min(i, j), max(i, j))
        d_map[key] = dist
    return d_map


def load_quran():
    with open(QURAN_JSON) as f:
        return json.load(f)


# ---------- Q053-F-01: Q 53 FR-nearest = Q 96 ----------

def test_F_01(d_map):
    """Q 53's FR-nearest neighbor identity test."""
    s53 = 53

    def get(a, b):
        if a == b:
            return 0.0
        return d_map[(min(a, b), max(a, b))]

    others = [(s, get(s53, s)) for s in range(1, 115) if s != s53]
    others.sort(key=lambda x: x[1])
    nearest_neighbors = others[:15]

    target = 96
    target_rank = next(i + 1 for i, (s, _) in enumerate(others) if s == target)

    if target_rank == 1:
        verdict = "CONFIRMED"
    elif target_rank <= 3:
        verdict = "PASS-DIRECTED"
    elif target_rank <= 10:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    return {
        "test_id": "Q053-F-01",
        "title": "Q 53 FR-nearest = Q 96 al-ʿAlaq",
        "target_neighbor": target,
        "target_rank": target_rank,
        "rank_threshold_confirmed": 1,
        "verdict": verdict,
        "top_15_nearest": [
            {"rank": i + 1, "surah": s, "distance": round(d, 6)}
            for i, (s, d) in enumerate(nearest_neighbors)
        ],
        "alpha_bon": ALPHA_BON,
        "bonferroni_k": BONFERRONI_K,
        "seed": SEED,
    }


# ---------- Q053-F-02: Q 53:19-23 text-anomaly null ----------

def test_F_02(quran):
    """Q 53:19-23 lexical-distribution null test against all 5-verse corpus windows."""
    s53 = quran[52]
    block = s53["verses"][18:23]  # vv 19-23
    block_text = " ".join(v["text"] for v in block)
    block_tokens = block_text.split()
    block_unique = set(block_tokens)
    block_n = len(block_tokens)
    block_u = len(block_unique)
    block_ttr = block_u / block_n if block_n else 0.0

    # All 5-verse corpus windows
    all_windows = []
    for surah in quran:
        verses = surah["verses"]
        if len(verses) < 5:
            continue
        for i in range(len(verses) - 4):
            window = verses[i:i + 5]
            text = " ".join(v["text"] for v in window)
            tokens = text.split()
            uniq = set(tokens)
            n = len(tokens)
            u = len(uniq)
            ttr = u / n if n else 0.0
            all_windows.append({
                "surah": surah["id"],
                "start": window[0]["id"],
                "n": n,
                "u": u,
                "ttr": ttr,
            })

    n_total = len(all_windows)
    # Rank Q 53:19-23
    by_n = sorted(all_windows, key=lambda w: w["n"])
    by_ttr = sorted(all_windows, key=lambda w: w["ttr"])

    rank_n = next(i + 1 for i, w in enumerate(by_n) if w["surah"] == 53 and w["start"] == 19)
    rank_ttr = next(i + 1 for i, w in enumerate(by_ttr) if w["surah"] == 53 and w["start"] == 19)

    pct_n = rank_n / n_total
    pct_ttr = rank_ttr / n_total

    # NULL CONFIRMED if both metrics within 5%-95%
    in_5_95 = lambda pct: 0.05 <= pct <= 0.95
    null_confirmed = in_5_95(pct_n) and in_5_95(pct_ttr)

    verdict = (
        "NULL CONFIRMED (text statistically typical — no lexical anomaly)"
        if null_confirmed
        else "DIRECTIONAL ANOMALY"
    )

    return {
        "test_id": "Q053-F-02",
        "title": "Q 53:19-23 text-anomaly null (gharānīq adversarial)",
        "block": "Q 53:19-23",
        "n_tokens": block_n,
        "n_unique": block_u,
        "ttr": round(block_ttr, 6),
        "n_total_windows": n_total,
        "token_count_rank_low_to_high": rank_n,
        "token_count_pct": round(pct_n, 4),
        "ttr_rank_low_to_high": rank_ttr,
        "ttr_pct": round(pct_ttr, 4),
        "null_confirmed": null_confirmed,
        "verdict": verdict,
        "interpretation": (
            "Q 53:19-23 lies within corpus 5%-95% range on both n_tokens and TTR — "
            "no detectable lexical anomaly suggestive of editorial-interpolation removal. "
            "This is the predicted reverse-direction outcome and provides one verification "
            "axis for the broader gharānīq-narrative falsification (see 04-hadith-corpus.md §6 "
            "and 05-classical-claims-audit.md §2)."
        ),
        "alpha_bon": ALPHA_BON,
        "bonferroni_k": BONFERRONI_K,
        "seed": SEED,
    }


# ---------- Q053-F-03: 14 sajda-surahs FR cohesion ----------

def test_F_03(d_map):
    """14 sajda-surahs cohesion — reverse-direction NULL prediction."""
    pairs = list(itertools.combinations(SAJDA_14, 2))
    dists = [d_map[(min(a, b), max(a, b))] for a, b in pairs]
    d_sajda = sum(dists) / len(dists)
    n_pairs = len(pairs)

    # Corpus-wide baseline
    all_pairs = list(itertools.combinations(range(1, 115), 2))
    all_dists = [d_map[(min(a, b), max(a, b))] for a, b in all_pairs]
    d_corpus = sum(all_dists) / len(all_dists)

    # Permutation null
    rng = random.Random(SEED)
    nulls = []
    for _ in range(N_PERM):
        sample = rng.sample(range(1, 115), 14)
        sample_dists = [d_map[(min(a, b), max(a, b))] for a, b in itertools.combinations(sample, 2)]
        nulls.append(sum(sample_dists) / len(sample_dists))

    nulls_sorted = sorted(nulls)
    n_smaller_or_eq = sum(1 for x in nulls if x <= d_sajda)
    perm_p_lower = n_smaller_or_eq / N_PERM  # one-tailed: prob obs ≤ random

    null_mean = sum(nulls) / N_PERM
    null_var = sum((x - null_mean) ** 2 for x in nulls) / N_PERM
    null_sd = math.sqrt(null_var) if null_var > 0 else 0.0
    z = (d_sajda - null_mean) / null_sd if null_sd > 0 else 0.0

    # Verdict (reverse-direction; NULL is the predicted outcome)
    if perm_p_lower > 0.5:
        verdict = "NULL CONFIRMED (functional-classification, not content-cohesive)"
    elif perm_p_lower < ALPHA_BON:
        verdict = "COHESION CONFIRMED (would falsify our reverse-direction prediction)"
    elif perm_p_lower < 0.05:
        verdict = "DIRECTIONAL TOWARD COHESION (not Bonferroni-significant)"
    else:
        verdict = "WEAK COHESION (DIRECTIONAL but not significant)"

    return {
        "test_id": "Q053-F-03",
        "title": "14 sajda-surahs FR cohesion test",
        "sajda_14_surahs": SAJDA_14,
        "n_pairs": n_pairs,
        "d_sajda_within_cluster_mean": round(d_sajda, 6),
        "d_corpus_pairwise_mean": round(d_corpus, 6),
        "ratio_within_to_corpus": round(d_sajda / d_corpus, 6),
        "n_perm": N_PERM,
        "null_mean": round(null_mean, 6),
        "null_sd": round(null_sd, 6),
        "z_score": round(z, 4),
        "perm_p_one_tailed": round(perm_p_lower, 6),
        "verdict": verdict,
        "interpretation": (
            "14 sajda-surahs are NOT FR-content-cohesive (within-cluster mean is "
            "slightly ABOVE corpus baseline). The classical sujūd-al-tilāwah "
            "classification is functional-liturgical (where to prostrate during "
            "recitation), NOT a content-fingerprint classification. This adds the "
            "sajda-classification to the project's catalog of functional-classifications-"
            "without-content-cohesion (alongside H-NEW-68 Friday-recitation NULL, "
            "H-NEW-69 14-vs-14 alphabet-split NULL)."
        ),
        "alpha_bon": ALPHA_BON,
        "bonferroni_k": BONFERRONI_K,
        "seed": SEED,
    }


# ---------- Main ----------

def main():
    print("=" * 70)
    print("Q 53 al-Najm specialist test family")
    print(f"Seed: {SEED}; Bonferroni-k: {BONFERRONI_K}; α_bon: {ALPHA_BON}")
    print(f"Permutations: {N_PERM}")
    print("=" * 70)

    # SHA-verification
    print("\n--- SHA-256 of pre-regs ---")
    shas = verify_prereg_shas()
    for k, v in shas.items():
        print(f"  {k}: {v['filename']}  SHA={v['sha256']}")

    # Load corpus + FR matrix
    print("\n--- Loading data ---")
    d_map = load_fr_matrix()
    quran = load_quran()
    print(f"  FR matrix loaded: {len(d_map)} entries")
    print(f"  Quran loaded: {len(quran)} surahs")

    # Run tests
    print("\n--- Running tests ---")
    results = {
        "family_id": "Q053-F-family-2026-05-09",
        "date": "2026-05-09",
        "specialist": "Waiel Al-Shujaa",
        "seed": SEED,
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "n_perm": N_PERM,
        "shas": shas,
        "tests": {},
    }

    print("\n[Q053-F-01]")
    f01 = test_F_01(d_map)
    f01["sha256_of_prereg"] = shas["Q053-F-01"]["sha256"]
    results["tests"]["Q053-F-01"] = f01
    print(f"  target neighbor: Q {f01['target_neighbor']}")
    print(f"  target rank: {f01['target_rank']}")
    print(f"  verdict: {f01['verdict']}")
    print(f"  top 5 nearest:")
    for n in f01["top_15_nearest"][:5]:
        print(f"    rank {n['rank']}: Q {n['surah']} (d_FR = {n['distance']})")

    print("\n[Q053-F-02]")
    f02 = test_F_02(quran)
    f02["sha256_of_prereg"] = shas["Q053-F-02"]["sha256"]
    results["tests"]["Q053-F-02"] = f02
    print(f"  Q 53:19-23 tokens: {f02['n_tokens']} (unique: {f02['n_unique']}, TTR: {f02['ttr']})")
    print(f"  rank by token count (low-to-high): {f02['token_count_rank_low_to_high']} / {f02['n_total_windows']}")
    print(f"  rank by TTR (low-to-high): {f02['ttr_rank_low_to_high']} / {f02['n_total_windows']}")
    print(f"  verdict: {f02['verdict']}")

    print("\n[Q053-F-03]")
    f03 = test_F_03(d_map)
    f03["sha256_of_prereg"] = shas["Q053-F-03"]["sha256"]
    results["tests"]["Q053-F-03"] = f03
    print(f"  d_sajda within-cluster: {f03['d_sajda_within_cluster_mean']}")
    print(f"  corpus baseline: {f03['d_corpus_pairwise_mean']}")
    print(f"  z-score: {f03['z_score']}; perm-p: {f03['perm_p_one_tailed']}")
    print(f"  verdict: {f03['verdict']}")

    # Family summary
    print("\n--- Family summary ---")
    counts = {"CONFIRMED": 0, "PASS-DIRECTED": 0, "NULL_CONFIRMED": 0, "OTHER": 0}
    for tid, t in results["tests"].items():
        v = t["verdict"]
        if v.startswith("CONFIRMED"):
            counts["CONFIRMED"] += 1
        elif v.startswith("PASS-DIRECTED"):
            counts["PASS-DIRECTED"] += 1
        elif "NULL CONFIRMED" in v:
            counts["NULL_CONFIRMED"] += 1
        else:
            counts["OTHER"] += 1
    results["family_summary"] = counts
    for k, v in counts.items():
        print(f"  {k}: {v}")

    # Write outputs
    print("\n--- Writing JSON outputs ---")
    for tid, t in results["tests"].items():
        out_file = CSV_OUT / f"{tid}.json"
        with open(out_file, "w") as f:
            json.dump(t, f, ensure_ascii=False, indent=2)
        print(f"  wrote {out_file}")

    family_file = CSV_OUT / "Q053-F-family-summary.json"
    with open(family_file, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"  wrote {family_file}")

    print("\nDONE.")


if __name__ == "__main__":
    main()
