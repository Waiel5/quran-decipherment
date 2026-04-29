#!/usr/bin/env python3
"""H-NEW-420: novel-outlier block-exclusion validation (Q 9, 12, 24, 33)."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-420-novel-outlier-exclusion-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-420.json"
SEED = 20260509
N_PERMS = 10000

SURAH_NAMES = {9: "al-Tawbah", 12: "Yūsuf", 24: "al-Nūr", 33: "al-Aḥzāb",
               55: "al-Raḥmān"}

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
    """Fraction of random N-subsets of {1..114} with d̄ <= observed."""
    all_surahs = list(range(1, 115))
    below = 0
    for _ in range(n_perms):
        sub = rng.sample(all_surahs, size)
        if mean_pairwise(D, sub) <= observed:
            below += 1
    return 100.0 * below / n_perms

def test_outlier(D, k, rng):
    block = [n for n in [k-2, k-1, k, k+1, k+2] if 1 <= n <= 114]
    block_exc = [n for n in block if n != k]
    d_full = mean_pairwise(D, block)
    d_exc = mean_pairwise(D, block_exc)
    p_full = percentile_in_null(D, d_full, len(block), N_PERMS, rng)
    p_exc = percentile_in_null(D, d_exc, len(block_exc), N_PERMS, rng)
    return {
        "surah": k, "name": SURAH_NAMES[k],
        "block_full": block, "block_exc": block_exc,
        "d_full": d_full, "d_exc": d_exc,
        "percentile_full": p_full, "percentile_exc": p_exc,
        "delta_pp": p_exc - p_full,
        "confirmed_outlier": (p_exc - p_full) >= 15.0,
    }

def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-420 ===\nPre-reg SHA: {prereg_sha}\nSeed: {SEED}")
    D = load_D()
    rng = random.Random(SEED)

    candidates = [9, 12, 24, 33]
    results = []
    for k in candidates:
        print(f"\n--- Q {k} {SURAH_NAMES[k]} ---")
        r = test_outlier(D, k, rng)
        results.append(r)
        print(f"  block_full: {r['block_full']}  d̄={r['d_full']:.4f}  pct={r['percentile_full']:.2f}%")
        print(f"  block_exc:  {r['block_exc']}  d̄={r['d_exc']:.4f}  pct={r['percentile_exc']:.2f}%")
        print(f"  delta_pp = {r['delta_pp']:+.2f} {'CONFIRM-OUTLIER' if r['confirmed_outlier'] else 'NULL (below +15pp)'}")

    n_confirmed = sum(1 for r in results if r["confirmed_outlier"])
    print(f"\n=== SUMMARY ===\nConfirmed: {n_confirmed}/4")
    print(f"H1 (generalize ≥3/4): {'SUPPORTED' if n_confirmed >= 3 else 'REJECTED'}")

    # MW-5 positive control: Q 55 rerun
    print(f"\n--- Positive control: Q 55 (H-NEW-390 reported +32.6pp) ---")
    q55 = test_outlier(D, 55, rng)
    print(f"  delta_pp = {q55['delta_pp']:+.2f}")
    pc_ok = q55["delta_pp"] >= 15.0
    print(f"  PC-status: {'PASS' if pc_ok else 'FAIL'}")

    out = {
        "id": "H-NEW-420",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "n_permutations": N_PERMS,
        "results": results,
        "positive_control_q55": q55,
        "n_confirmed": n_confirmed,
        "h1_supported": n_confirmed >= 3,
        "pc_pass": pc_ok,
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
