#!/usr/bin/env python3
"""H-NEW-901: ḥawāmīm-7 cluster cohesion test.

HM-7 = {Q 40, 41, 42, 43, 44, 45, 46}, K=7
Direction-locked one-sided permutation:
  H1: d̄(HM-7) percentile ≤ 5%  ⇒ CONFIRMED
  5 < %ile ≤ 16.67  ⇒ DIRECTIONAL
  16.67 < %ile ≤ 95  ⇒ NULL
  %ile > 95  ⇒ FALSIFIED (pre-commit anti-cohesion)

PRIMARY: 10000 random-7 null draws, seed 20260428.
Secondary diagnostics: HM-A {40,41,42}, HM-B {43,44,45,46} percentiles
(NOT in Bonferroni family — descriptive only).

Rules-tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import hashlib
import json
import random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-901-hm7-cohesion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-901-hm7-cohesion.json"

EXPECTED_SHA = "af7a1c1094f7d7e68e4d47660cc514648306ddbeb002f5dbbb471c82881b7ca0"

SEED = 20260428
N_PERMS = 10000

# Locked clusters
HM_7 = [40, 41, 42, 43, 44, 45, 46]
HM_A = [40, 41, 42]
HM_B = [43, 44, 45, 46]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    """Load symmetric Fisher-Rao distance matrix from H-NEW-111 upper-triangular list."""
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]  # 1-indexed
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def mean_pairwise(D, subset):
    xs = list(subset)
    vals = [D[a][b] for a, b in combinations(xs, 2)]
    return sum(vals) / len(vals) if vals else 0.0


def percentile_in_null(D, observed, size, n_perms, rng):
    all_surahs = list(range(1, 115))
    below = 0
    for _ in range(n_perms):
        sub = rng.sample(all_surahs, size)
        if mean_pairwise(D, sub) <= observed:
            below += 1
    return 100.0 * below / n_perms


def verdict_from_pct(p):
    if p <= 5.0:
        return "CONFIRMED"
    if p <= 16.67:
        return "DIRECTIONAL"
    if p <= 95.0:
        return "NULL"
    return "FALSIFIED"


def main():
    actual_sha = sha(PREREG)
    print("=== H-NEW-901 — ḥawāmīm-7 cluster cohesion test ===")
    print(f"Pre-reg path: {PREREG}")
    print(f"Pre-reg SHA (computed): {actual_sha}")
    print(f"Pre-reg SHA (expected): {EXPECTED_SHA}")
    if actual_sha != EXPECTED_SHA:
        raise SystemExit(f"FATAL: pre-reg SHA mismatch — pre-commit violation. "
                         f"Got {actual_sha}, expected {EXPECTED_SHA}.")
    print("Pre-reg SHA verified OK.")

    print(f"Seed: {SEED}; N_perms: {N_PERMS}")

    D = load_D()

    # PRIMARY: HM-7 cohesion test
    rng_p = random.Random(SEED)
    d_obs_hm7 = mean_pairwise(D, HM_7)
    pct_hm7 = percentile_in_null(D, d_obs_hm7, 7, N_PERMS, rng_p)
    verdict_hm7 = verdict_from_pct(pct_hm7)
    print(f"\n--- PRIMARY: HM-7 = {HM_7} (K=7) ---")
    print(f"  d̄ = {d_obs_hm7:.6f}")
    print(f"  PRIMARY %ile = {pct_hm7:.2f}%   (seed={SEED}, N={N_PERMS})")
    print(f"  VERDICT: {verdict_hm7}")

    # Secondary diagnostics: HM-A and HM-B with separate seed-streams
    rng_a = random.Random(SEED + 1)
    d_obs_a = mean_pairwise(D, HM_A)
    pct_a = percentile_in_null(D, d_obs_a, 3, N_PERMS, rng_a)

    rng_b = random.Random(SEED + 2)
    d_obs_b = mean_pairwise(D, HM_B)
    pct_b = percentile_in_null(D, d_obs_b, 4, N_PERMS, rng_b)

    print(f"\n--- SECONDARY: HM-A = {HM_A} (K=3) ---")
    print(f"  d̄ = {d_obs_a:.6f}; %ile = {pct_a:.2f}%")
    print(f"\n--- SECONDARY: HM-B = {HM_B} (K=4) ---")
    print(f"  d̄ = {d_obs_b:.6f}; %ile = {pct_b:.2f}%")

    # Within vs between sub-block mean FR distance
    pairs_within_a = list(combinations(HM_A, 2))
    pairs_within_b = list(combinations(HM_B, 2))
    pairs_between = [(a, b) for a in HM_A for b in HM_B]

    d_within_a = sum(D[i][j] for i, j in pairs_within_a) / len(pairs_within_a)
    d_within_b = sum(D[i][j] for i, j in pairs_within_b) / len(pairs_within_b)
    d_between = sum(D[i][j] for i, j in pairs_between) / len(pairs_between)

    print(f"\n--- HM-A vs HM-B sub-block comparison (descriptive) ---")
    print(f"  d̄_within_HM-A = {d_within_a:.6f}  (n_pairs={len(pairs_within_a)})")
    print(f"  d̄_within_HM-B = {d_within_b:.6f}  (n_pairs={len(pairs_within_b)})")
    print(f"  d̄_between_HM-AB = {d_between:.6f}  (n_pairs={len(pairs_between)})")
    print(f"  HM-A more cohesive than HM-B: {d_within_a < d_within_b}")
    print(f"  Between > within (bifurcation signal): "
          f"{d_between > max(d_within_a, d_within_b)}")

    # All pairwise within HM-7
    pairs_hm7 = list(combinations(HM_7, 2))
    pairwise_hm7 = [(a, b, D[a][b]) for a, b in pairs_hm7]

    out = {
        "id": "H-NEW-901",
        "title": "ḥawāmīm-7 cluster cohesion test",
        "prereg_path": str(PREREG),
        "prereg_sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA,
        "sha_verified": (actual_sha == EXPECTED_SHA),
        "seed": SEED,
        "n_perms": N_PERMS,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, "
                       "basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi); "
                       "Fisher-Rao distance matrix from H-NEW-111 / QAC-STEM root tokens / "
                       "QAC v0.4 / K_top_roots=500 / Dirichlet alpha=0.5",
        "primary": {
            "set": HM_7,
            "K": 7,
            "d_observed": d_obs_hm7,
            "percentile": pct_hm7,
            "verdict": verdict_hm7,
            "gates": {
                "confirmed_pct": 5.0,
                "directional_pct": 16.67,
                "falsified_pct": 95.0,
            },
        },
        "secondary_hm_a": {
            "set": HM_A,
            "K": 3,
            "d_observed": d_obs_a,
            "percentile": pct_a,
            "diagnostic_only": True,
        },
        "secondary_hm_b": {
            "set": HM_B,
            "K": 4,
            "d_observed": d_obs_b,
            "percentile": pct_b,
            "diagnostic_only": True,
        },
        "sub_block_comparison": {
            "d_within_hm_a": d_within_a,
            "d_within_hm_b": d_within_b,
            "d_between_hm_ab": d_between,
            "hm_a_more_cohesive_than_hm_b": d_within_a < d_within_b,
            "between_exceeds_within_max": d_between > max(d_within_a, d_within_b),
        },
        "pairwise_hm7": [{"a": a, "b": b, "d": d} for a, b, d in pairwise_hm7],
        "notes": {
            "classical_anchor": "Ibn ʿAbbās al-ḥawāmīm dībāj al-Qurʾān (al-Suyūṭī Itqān nawʿ 17)",
            "h_new_570_priors": "HM-7 reported at 20.90%ile in MW-5 sub-test of H-NEW-570",
            "h_new_600_double_null": "ALM-6 NULL @ 43.15%, ALR-5 NULL @ 56.25%",
        },
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
