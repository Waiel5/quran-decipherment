#!/usr/bin/env python3
"""H-NEW-450: window-sensitivity of outlier-factor."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-450-window-sensitivity-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-450.json"
SEED = 20260512
N_PERMS = 10000
WINDOWS = [2, 3, 5]
ALPHA_BON = 0.05 / 18

TARGETS = {
    9: ("al-Tawbah", "novel"),
    12: ("Yūsuf", "novel"),
    24: ("al-Nūr", "novel"),
    33: ("al-Aḥzāb", "novel"),
    55: ("al-Raḥmān", "PC"),
    62: ("al-Jumuʿa", "NC"),
}

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

def test_cell(D, k, w, rng):
    block = [n for n in range(k-w, k+w+1) if 1 <= n <= 114]
    block_exc = [n for n in block if n != k]
    d_full = mean_pairwise(D, block)
    d_exc = mean_pairwise(D, block_exc)
    p_full = percentile_in_null(D, d_full, len(block), N_PERMS, rng)
    p_exc = percentile_in_null(D, d_exc, len(block_exc), N_PERMS, rng)
    return {
        "block_full": block, "block_exc": block_exc,
        "n_full": len(block), "n_exc": len(block_exc),
        "d_full": d_full, "d_exc": d_exc,
        "percentile_full": p_full, "percentile_exc": p_exc,
        "delta_pp": p_exc - p_full,
    }

def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-450 (window-sensitivity) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\nα_bon: {ALPHA_BON:.6f}")
    D = load_D()
    rng = random.Random(SEED)

    results = {}
    for k, (name, role) in TARGETS.items():
        print(f"\n--- Q {k} {name} [{role}] ---")
        results[k] = {"name": name, "role": role, "by_window": {}}
        for w in WINDOWS:
            cell = test_cell(D, k, w, rng)
            results[k]["by_window"][w] = cell
            print(f"  w=±{w}: N={cell['n_full']}→{cell['n_exc']}, "
                  f"pct_full={cell['percentile_full']:.2f}%, pct_exc={cell['percentile_exc']:.2f}%, "
                  f"delta={cell['delta_pp']:+.2f}pp")

    # Evaluate H1 criteria
    print(f"\n=== WINDOW-CONSISTENCY VERDICTS ===")
    novel_passes = 0
    pc_passes_all = True
    nc_passes_all = True
    for k, (name, role) in TARGETS.items():
        deltas = [results[k]["by_window"][w]["delta_pp"] for w in WINDOWS]
        if role == "novel":
            all_le_neg15 = all(d <= -15.0 for d in deltas)
            novel_passes += int(all_le_neg15)
            print(f"  Q {k} {name} [{role}]: deltas={[f'{d:+.2f}' for d in deltas]}  PASS(all≤-15)={all_le_neg15}")
        elif role == "PC":
            all_le_neg5 = all(d <= -5.0 for d in deltas)
            pc_passes_all = all_le_neg5
            print(f"  Q {k} {name} [{role}]: deltas={[f'{d:+.2f}' for d in deltas]}  PC-PASS(all≤-5)={all_le_neg5}")
        elif role == "NC":
            all_under_5 = all(abs(d) < 5.0 for d in deltas)
            nc_passes_all = all_under_5
            print(f"  Q {k} {name} [{role}]: deltas={[f'{d:+.2f}' for d in deltas]}  NC-PASS(all|d|<5)={all_under_5}")

    aggregate_h1 = (novel_passes >= 3) and pc_passes_all and nc_passes_all
    print(f"\n=== AGGREGATE ===")
    print(f"Novel window-consistent (≥3/4): {novel_passes}/4")
    print(f"PC pass at all windows: {pc_passes_all}")
    print(f"NC pass at all windows: {nc_passes_all}")
    print(f"Aggregate H1 CONFIRMED: {aggregate_h1}")

    out = {
        "id": "H-NEW-450", "prereg_sha": prereg_sha, "seed": SEED,
        "windows": WINDOWS, "alpha_bon": ALPHA_BON,
        "results": results,
        "novel_window_consistent": novel_passes,
        "pc_pass_all_windows": pc_passes_all,
        "nc_pass_all_windows": nc_passes_all,
        "aggregate_h1_confirmed": aggregate_h1,
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
