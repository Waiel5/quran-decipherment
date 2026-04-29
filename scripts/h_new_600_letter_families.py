#!/usr/bin/env python3
"""H-NEW-600/610: Paired letter-family content-cohesion test.

ALM-6 = {Q 2, 3, 29, 30, 31, 32}
ALR-5 = {Q 10, 11, 12, 14, 15}  (Q 13 al-Raʿd is ALMR not ALR — EXCLUDED, see prereg §2.3)

PRIMARY: d̄ percentile in 10000 random-K-subset null, seed 20260430.
MW-5: replication seed 20260431, N_perms 5000.
MW-6: instrument check on locked non-letter-family random-6 set.

Bonferroni k=3, α_bon = 0.01667.
"""
import hashlib
import json
import random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-600-letter-families-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-600.json"

SEED_PRIMARY = 20260430
SEED_MW5 = 20260431
SEED_MW6 = 20260432

N_PERMS_PRIMARY = 10000
N_PERMS_MW5 = 5000
N_PERMS_MW6 = 10000

ALPHA_BON = 0.05 / 3  # 0.01667
GATE_STRICT = 100.0 * (0.05 / 3)   # 1.67 %ile
GATE_DIRECT = 100.0 * (0.05 / 3) * 10  # 16.67 %ile

# Locked letter-family sets (see prereg §2)
ALM_6 = [2, 3, 29, 30, 31, 32]
ALR_5 = [10, 11, 12, 14, 15]
# Q 13 al-Raʿd EXCLUDED — ALMR not ALR (prereg §2.3)

# MW-6 instrument: locked non-letter-family random-6 set (prereg §3.3)
MW6_SET = [5, 9, 17, 25, 33, 47]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    """Load 114-surah symmetric Fisher-Rao distance matrix from H-NEW-111."""
    with open(H_NEW_111) as f:
        d = json.load(f)
    # h-new-111 stores as upper-triangular [i, j, dist] with 0-indexed i,j over surahs 1..114
    mat = [[0.0] * 115 for _ in range(115)]  # 1-indexed convenience, ignore [0]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        # The h-new-111 indexing convention follows h-new-570 script (uses 0..114 indices internally)
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


def run_family(D, name, family, seed_primary, seed_mw5):
    K = len(family)
    rng_p = random.Random(seed_primary)
    rng_m = random.Random(seed_mw5)

    d_obs = mean_pairwise(D, family)
    pct_p = percentile_in_null(D, d_obs, K, N_PERMS_PRIMARY, rng_p)
    pct_m = percentile_in_null(D, d_obs, K, N_PERMS_MW5, rng_m)

    strict = pct_p <= GATE_STRICT
    directional = pct_p <= GATE_DIRECT
    drift = abs(pct_p - pct_m)
    stable = drift <= 3.0

    print(f"\n--- {name} (K={K}) family = {family} ---")
    print(f"  d̄         = {d_obs:.4f}")
    print(f"  PRIMARY   %ile = {pct_p:.2f}%  (seed={seed_primary}, N={N_PERMS_PRIMARY})")
    print(f"  MW-5      %ile = {pct_m:.2f}%  (seed={seed_mw5}, N={N_PERMS_MW5})")
    print(f"  drift = {drift:.2f}pp  stable (≤3pp): {stable}")
    print(f"  STRICT (≤{GATE_STRICT:.2f}%): {strict}")
    print(f"  DIRECT (≤{GATE_DIRECT:.2f}%): {directional}")

    return {
        "name": name,
        "set": family,
        "K": K,
        "d_observed": d_obs,
        "primary": {"seed": seed_primary, "n_perms": N_PERMS_PRIMARY, "percentile": pct_p},
        "mw5": {"seed": seed_mw5, "n_perms": N_PERMS_MW5, "percentile": pct_m},
        "drift_pp": drift,
        "stable_replication": stable,
        "strict_pass": strict,
        "directional_pass": directional,
    }


def main():
    prereg_sha = sha(PREREG)
    print("=== H-NEW-600/610 — Paired letter-family content-cohesion ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Bonferroni k=3, α_bon = {ALPHA_BON:.5f}")
    print(f"Gates: STRICT ≤ {GATE_STRICT:.2f}%ile; DIRECTIONAL ≤ {GATE_DIRECT:.2f}%ile")
    assert len(ALM_6) == 6 and len(ALR_5) == 5 and len(MW6_SET) == 6
    # Verify Q 13 not in ALR_5
    assert 13 not in ALR_5, "Q 13 al-Raʿd must be EXCLUDED from ALR-5 (it is ALMR)"
    # Verify MW6 disjoint from any muqaṭṭaʿāt set
    muq29 = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
             36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
    assert set(MW6_SET).isdisjoint(muq29), "MW-6 must be non-muqaṭṭaʿāt"

    D = load_D()

    alm = run_family(D, "ALM-6", ALM_6, SEED_PRIMARY, SEED_MW5)
    alr = run_family(D, "ALR-5", ALR_5, SEED_PRIMARY, SEED_MW5)

    # MW-6 instrument check: random-6 non-letter-family set vs random-6 null
    rng_mw6 = random.Random(SEED_MW6)
    d_mw6 = mean_pairwise(D, MW6_SET)
    pct_mw6 = percentile_in_null(D, d_mw6, 6, N_PERMS_MW6, rng_mw6)
    mw6_null_typical = 25.0 <= pct_mw6 <= 75.0
    print(f"\n--- MW-6 instrument: {MW6_SET} (K=6, non-muq) ---")
    print(f"  d̄ = {d_mw6:.4f}")
    print(f"  %ile = {pct_mw6:.2f}%  (seed={SEED_MW6}, N={N_PERMS_MW6})")
    print(f"  null-typical [25,75]: {mw6_null_typical}")

    # Joint-pattern test: ≥1 of 2 PRIMARY families ≤ 16.67% DIRECTIONAL
    joint_directional = alm["directional_pass"] or alr["directional_pass"]
    # Joint STRICT: ≥1 of 2 ≤ 1.67%
    joint_strict = alm["strict_pass"] or alr["strict_pass"]

    # Aggregate H1: at least one family STRICT AND second family DIRECTIONAL
    aggr_h1 = ((alm["strict_pass"] and alr["directional_pass"]) or
               (alr["strict_pass"] and alm["directional_pass"]))
    # NULL = both > directional
    aggr_null = (not alm["directional_pass"]) and (not alr["directional_pass"])

    print(f"\n=== JOINT / AGGREGATE ===")
    print(f"  Joint STRICT (≥1 ≤ {GATE_STRICT:.2f}%): {joint_strict}")
    print(f"  Joint DIRECT (≥1 ≤ {GATE_DIRECT:.2f}%): {joint_directional}")
    print(f"  AGGREGATE H1 (al-Biqāʿī family-munāsaba): {aggr_h1}")
    print(f"  AGGREGATE NULL (H-NEW-570 generalization): {aggr_null}")

    out = {
        "id": "H-NEW-600",
        "title": "Paired letter-family content-cohesion: ALM-6 + ALR-5",
        "prereg_path": str(PREREG),
        "prereg_sha256": prereg_sha,
        "date": "2026-04-28",
        "bonferroni_k": 3,
        "alpha_bon": ALPHA_BON,
        "gates": {"strict_pct": GATE_STRICT, "directional_pct": GATE_DIRECT},
        "alm_6": alm,
        "alr_5": alr,
        "mw6_instrument": {
            "set": MW6_SET,
            "K": 6,
            "d_observed": d_mw6,
            "seed": SEED_MW6,
            "n_perms": N_PERMS_MW6,
            "percentile": pct_mw6,
            "null_typical_[25,75]": mw6_null_typical,
        },
        "joint": {
            "strict_pass": joint_strict,
            "directional_pass": joint_directional,
            "aggregate_h1_biqai": aggr_h1,
            "aggregate_null_h570_generalization": aggr_null,
        },
        "notes": {
            "q13_excluded_from_alr": "Q 13 al-Raʿd is ALMR (المر) not ALR (الر); see prereg §2.3",
            "alm_classical_anchor": "al-Biqāʿī Naẓm al-Durar; al-Suyūṭī Itqān nawʿ 40; al-Rāzī Mafātīḥ vol.2",
            "alr_classical_anchor": "al-Biqāʿī Naẓm al-Durar (qiṣaṣ-family); al-Rāzī Mafātīḥ vol.17; H-NEW-97 ALR-PROPHET_PERSON p_mc=0.0059",
        },
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
