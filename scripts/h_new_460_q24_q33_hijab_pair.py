#!/usr/bin/env python3
"""H-NEW-460: Q 24 ↔ Q 33 ḥijāb-pair content-proximity test."""
import hashlib, json
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-460-q24-q33-hijab-pair-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-460.json"
SEED = 20260513
ALPHA_BON = 0.05 / 4

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist; mat[j][i] = dist
    return mat

def percentile_of(values, target):
    """Fraction of values ≤ target, as percent."""
    below = sum(1 for v in values if v <= target)
    return 100.0 * below / len(values)

def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-460 (Q24↔Q33 ḥijāb-pair) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\nα_bon: {ALPHA_BON:.4f}")
    D = load_D()

    # All pairwise distances (null distribution)
    all_pairs = []
    for i in range(1, 115):
        for j in range(i+1, 115):
            all_pairs.append((i, j, D[i][j]))
    pair_vals = sorted(v for _,_,v in all_pairs)
    n_pairs = len(pair_vals)
    print(f"\nNull: {n_pairs} pairwise FR distances; min={pair_vals[0]:.4f}, median={pair_vals[n_pairs//2]:.4f}, max={pair_vals[-1]:.4f}")
    print(f"  5th pct:  {pair_vals[int(n_pairs*0.05)]:.4f}")
    print(f"  10th pct: {pair_vals[int(n_pairs*0.10)]:.4f}")
    print(f"  20th pct: {pair_vals[int(n_pairs*0.20)]:.4f}")
    print(f"  80th pct: {pair_vals[int(n_pairs*0.80)]:.4f}")

    # PRIMARY: D(Q24, Q33)
    d_24_33 = D[24][33]
    pct_24_33 = percentile_of(pair_vals, d_24_33)
    primary_pass = pct_24_33 <= 10.0
    print(f"\n--- PRIMARY: D(Q24, Q33) ---")
    print(f"  D(24, 33) = {d_24_33:.4f}")
    print(f"  percentile = {pct_24_33:.2f}%")
    print(f"  Pre-commit ≤10%: {primary_pass}")

    # SECONDARY: nearest-neighbor ranks
    # For Q 24: rank all other surahs by distance
    q24_neighbors = sorted([(j, D[24][j]) for j in range(1, 115) if j != 24], key=lambda x: x[1])
    q33_neighbors = sorted([(j, D[33][j]) for j in range(1, 115) if j != 33], key=lambda x: x[1])

    rank_33_in_q24 = next(i+1 for i, (s, _) in enumerate(q24_neighbors) if s == 33)
    rank_24_in_q33 = next(i+1 for i, (s, _) in enumerate(q33_neighbors) if s == 24)
    sec_q24_pass = rank_33_in_q24 <= 28
    sec_q33_pass = rank_24_in_q33 <= 28
    print(f"\n--- SECONDARY: nearest-neighbor ranks ---")
    print(f"  Q 33's rank in Q 24's neighbors: {rank_33_in_q24}/113 (top-25 pass: {sec_q24_pass})")
    print(f"  Q 24's rank in Q 33's neighbors: {rank_24_in_q33}/113 (top-25 pass: {sec_q33_pass})")
    print(f"  Q 24's top 5 nearest: {[(s, f'{d:.3f}') for s,d in q24_neighbors[:5]]}")
    print(f"  Q 33's top 5 nearest: {[(s, f'{d:.3f}') for s,d in q33_neighbors[:5]]}")

    # MW-5: D(Q57, Q64) cohesion control
    d_57_64 = D[57][64]
    pct_57_64 = percentile_of(pair_vals, d_57_64)
    mw5_pass = pct_57_64 <= 20.0
    print(f"\n--- MW-5: D(Q57, Q64) musabbiḥāt cohesion ---")
    print(f"  D(57, 64) = {d_57_64:.4f}, pct = {pct_57_64:.2f}%, pass (≤20%): {mw5_pass}")

    # MW-6: D(Q24, Q112) anti-pair control
    d_24_112 = D[24][112]
    pct_24_112 = percentile_of(pair_vals, d_24_112)
    mw6_pass = pct_24_112 >= 80.0
    print(f"\n--- MW-6: D(Q24, Q112) anti-pair ---")
    print(f"  D(24, 112) = {d_24_112:.4f}, pct = {pct_24_112:.2f}%, pass (≥80%): {mw6_pass}")

    # Aggregate
    aggregate = primary_pass and sec_q24_pass and sec_q33_pass and mw5_pass and mw6_pass
    print(f"\n=== AGGREGATE ===")
    print(f"PRIMARY: {primary_pass}  SEC_Q24: {sec_q24_pass}  SEC_Q33: {sec_q33_pass}")
    print(f"MW-5: {mw5_pass}  MW-6: {mw6_pass}")
    print(f"AGGREGATE H1 CONFIRMED: {aggregate}")

    out = {
        "id": "H-NEW-460", "prereg_sha": prereg_sha, "seed": SEED,
        "alpha_bon": ALPHA_BON,
        "primary": {
            "d_24_33": d_24_33, "percentile": pct_24_33,
            "threshold": 10.0, "pass": primary_pass
        },
        "secondary": {
            "rank_q33_in_q24": rank_33_in_q24, "rank_q24_in_q33": rank_24_in_q33,
            "pass_q24": sec_q24_pass, "pass_q33": sec_q33_pass,
            "q24_top5": [(int(s), float(d)) for s,d in q24_neighbors[:5]],
            "q33_top5": [(int(s), float(d)) for s,d in q33_neighbors[:5]],
        },
        "mw5_q57_q64": {"d": d_57_64, "percentile": pct_57_64, "pass": mw5_pass},
        "mw6_q24_q112": {"d": d_24_112, "percentile": pct_24_112, "pass": mw6_pass},
        "aggregate_h1_confirmed": aggregate,
        "null_thresholds": {
            "5th_pct": pair_vals[int(n_pairs*0.05)],
            "10th_pct": pair_vals[int(n_pairs*0.10)],
            "20th_pct": pair_vals[int(n_pairs*0.20)],
            "50th_pct": pair_vals[int(n_pairs*0.50)],
            "80th_pct": pair_vals[int(n_pairs*0.80)],
        }
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
