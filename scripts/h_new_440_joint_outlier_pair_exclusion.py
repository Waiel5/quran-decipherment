#!/usr/bin/env python3
"""H-NEW-440: joint Q 55 + Q 56 outlier-pair exclusion — neighborhood-contrast diagnostic."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-440-joint-outlier-pair-exclusion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-440.json"
SEED = 20260511
N_PERMS = 10000
ALPHA_BON = 0.05 / 3

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist; mat[j][i] = dist
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

def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-440 (joint Q55+Q56 exclusion) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\nα_bon: {ALPHA_BON:.5f}")
    D = load_D()
    rng = random.Random(SEED)

    B = [53, 54, 55, 56, 57]
    B_minus_55 = [s for s in B if s != 55]
    B_minus_56 = [s for s in B if s != 56]
    B_minus_both = [s for s in B if s not in (55, 56)]

    # Baseline
    d5 = mean_pairwise(D, B)
    p5 = percentile_in_null(D, d5, 5, N_PERMS, rng)

    # Singletons
    d4_55 = mean_pairwise(D, B_minus_55)
    p4_55 = percentile_in_null(D, d4_55, 4, N_PERMS, rng)
    d4_56 = mean_pairwise(D, B_minus_56)
    p4_56 = percentile_in_null(D, d4_56, 4, N_PERMS, rng)

    # Joint
    d3_both = mean_pairwise(D, B_minus_both)
    p3_both = percentile_in_null(D, d3_both, 3, N_PERMS, rng)

    # Deltas
    delta_55 = p4_55 - p5
    delta_56 = p4_56 - p5
    delta_joint = p3_both - p5
    superadditivity = delta_joint - (delta_55 + delta_56)

    print(f"\nBASE block {B}: d̄={d5:.4f} → percentile {p5:.2f}%")
    print(f"{'':>4} −Q55 → {B_minus_55}: d̄={d4_55:.4f} → pct={p4_55:.2f}%  delta={delta_55:+.2f}pp")
    print(f"{'':>4} −Q56 → {B_minus_56}: d̄={d4_56:.4f} → pct={p4_56:.2f}%  delta={delta_56:+.2f}pp")
    print(f"{'':>4} −{{Q55,Q56}} → {B_minus_both}: d̄={d3_both:.4f} → pct={p3_both:.2f}%  delta={delta_joint:+.2f}pp")
    print(f"\nSuperadditivity = Δ_joint − (Δ_55 + Δ_56) = {superadditivity:+.2f}pp")

    # MW-5: Q 62 singleton removal
    B_q62 = [60, 61, 62, 63, 64]
    B_q62_exc = [s for s in B_q62 if s != 62]
    d5_q62 = mean_pairwise(D, B_q62)
    p5_q62 = percentile_in_null(D, d5_q62, 5, N_PERMS, rng)
    d4_q62 = mean_pairwise(D, B_q62_exc)
    p4_q62 = percentile_in_null(D, d4_q62, 4, N_PERMS, rng)
    delta_q62 = p4_q62 - p5_q62

    print(f"\nMW-5 (Q 62 NC): {B_q62}: pct={p5_q62:.2f}% → −Q62 pct={p4_q62:.2f}%  delta={delta_q62:+.2f}pp")

    # Verdicts
    h1_a = p3_both <= 30.0
    h1_b = superadditivity <= -10.0
    mw5_pass = abs(delta_q62) < 5.0
    pc_q55 = delta_55 <= -5.0
    pc_q56 = delta_56 <= -10.0

    print(f"\n=== VERDICT ===")
    print(f"H1(a) p3_minus_both ≤ 30%ile: {h1_a}  ({p3_both:.2f}%)")
    print(f"H1(b) superadditivity ≤ −10pp: {h1_b}  ({superadditivity:+.2f}pp)")
    print(f"MW-5 |Q62-delta|<5pp: {mw5_pass}  ({delta_q62:+.2f}pp)")
    print(f"Singleton Q55 ≤ −5pp: {pc_q55}  ({delta_55:+.2f}pp)")
    print(f"Singleton Q56 ≤ −10pp: {pc_q56}  ({delta_56:+.2f}pp)")
    h1_confirmed = h1_a and h1_b and mw5_pass
    print(f"\nH1 AGGREGATE CONFIRMED: {h1_confirmed}")

    out = {
        "id": "H-NEW-440", "prereg_sha": prereg_sha, "seed": SEED,
        "baseline_block": B, "baseline_d": d5, "baseline_percentile": p5,
        "singletons": {
            "minus_55": {"d": d4_55, "percentile": p4_55, "delta_pp": delta_55, "pass": pc_q55},
            "minus_56": {"d": d4_56, "percentile": p4_56, "delta_pp": delta_56, "pass": pc_q56},
        },
        "joint_minus_both": {"d": d3_both, "percentile": p3_both, "delta_pp": delta_joint},
        "superadditivity": superadditivity,
        "mw5_q62": {"baseline_pct": p5_q62, "exc_pct": p4_q62, "delta_pp": delta_q62, "pass": mw5_pass},
        "h1_a_pass": h1_a, "h1_b_pass": h1_b, "mw5_pass": mw5_pass,
        "h1_aggregate_confirmed": h1_confirmed,
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
