#!/usr/bin/env python3
"""H-NEW-670: Constrained-TSP test — does forcing Q 56/57 adjacency cost ~11% of L_mushaf?

Computes 2-opt-best Hamiltonian PATH on 114 surahs subject to Q a / Q b being adjacent,
for several constraint pairs. Compares constrained-best vs unconstrained-best.
"""
import hashlib
import json
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-670-tsp-hijra-constraint-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-670.json"
SEED = 20260440

L_MUSHAF = 85.759656
L_2OPT_UNCONSTRAINED = 77.466858


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def path_length(D, path):
    return sum(D[path[i]][path[i + 1]] for i in range(len(path) - 1))


def two_opt_path(D, path, n_iter_max=20000):
    """2-opt for OPEN path. Standard reverse-segment moves."""
    best = path[:]
    best_L = path_length(D, best)
    n = len(best)
    improved = True
    iters = 0
    while improved and iters < n_iter_max:
        improved = False
        for i in range(n - 1):
            for k in range(i + 1, n):
                if k - i == 1: continue
                # Reverse path[i+1..k]
                # Old edges: (i, i+1) + (k, k+1) (if exists)
                # New edges: (i, k) + (i+1, k+1)
                a, b = best[i], best[i + 1]
                c = best[k]
                d = best[k + 1] if k + 1 < n else None
                old = D[a][b] + (D[c][d] if d is not None else 0.0)
                new = D[a][c] + (D[b][d] if d is not None else 0.0)
                if new < old - 1e-12:
                    best = best[:i + 1] + best[i + 1:k + 1][::-1] + best[k + 1:]
                    best_L = path_length(D, best)
                    improved = True
                    break
            if improved: break
        iters += 1
    return best, best_L


def two_opt_path_constrained(D, path, force_adj_pair, n_iter_max=20000):
    """2-opt with O(1) constraint check via position tracking.
    Preserves (a, b) adjacency throughout."""
    a_force, b_force = force_adj_pair
    best = path[:]
    best_L = path_length(D, best)
    n = len(best)

    # Verify start
    pos_a = best.index(a_force)
    pos_b = best.index(b_force)
    assert abs(pos_a - pos_b) == 1, f"Start violates constraint: a@{pos_a}, b@{pos_b}"

    improved = True
    iters = 0
    while improved and iters < n_iter_max:
        improved = False
        pos_a = best.index(a_force)
        pos_b = best.index(b_force)
        for i in range(n - 1):
            for k in range(i + 1, n):
                if k - i == 1: continue
                a, b = best[i], best[i + 1]
                c = best[k]
                d = best[k + 1] if k + 1 < n else None
                old = D[a][b] + (D[c][d] if d is not None else 0.0)
                new = D[a][c] + (D[b][d] if d is not None else 0.0)
                if new < old - 1e-12:
                    # Compute new positions of a_force, b_force after reversal of [i+1..k]
                    def new_pos(p):
                        if p < i + 1 or p > k: return p
                        return k + i + 1 - p
                    new_pa, new_pb = new_pos(pos_a), new_pos(pos_b)
                    if abs(new_pa - new_pb) == 1:
                        best = best[:i + 1] + best[i + 1:k + 1][::-1] + best[k + 1:]
                        best_L += new - old
                        pos_a, pos_b = new_pa, new_pb
                        improved = True
                        break
            if improved: break
        iters += 1
    return best, best_L


def random_path_with_adjacency(rng, force_adj_pair, n_surahs=114):
    """Generate random path of 1..n_surahs with force_adj_pair adjacent."""
    a, b = force_adj_pair
    others = [s for s in range(1, n_surahs + 1) if s != a and s != b]
    rng.shuffle(others)
    insert_at = rng.randint(0, len(others))
    return others[:insert_at] + [a, b] + others[insert_at:]


def random_path(rng, n_surahs=114):
    p = list(range(1, n_surahs + 1))
    rng.shuffle(p)
    return p


def best_2opt_unconstrained(D, n_starts=200, base_seed=SEED):
    """Multi-start 2-opt with full-convergence per start."""
    best_L = float("inf")
    best_p = None
    for k in range(n_starts):
        rng = random.Random(base_seed + k)
        p = random_path(rng)
        p, L = two_opt_path(D, p, n_iter_max=2000)
        if L < best_L:
            best_L = L
            best_p = p
    return best_p, best_L


def best_2opt_with_adjacency(D, force_adj_pair, n_starts=200, base_seed=SEED):
    best_L = float("inf")
    best_p = None
    for k in range(n_starts):
        rng = random.Random(base_seed + k)
        p = random_path_with_adjacency(rng, force_adj_pair)
        p, L = two_opt_path_constrained(D, p, force_adj_pair, n_iter_max=2000)
        if L < best_L:
            best_L = L
            best_p = p
    return best_p, best_L


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-670 (Constrained-TSP / Hijra-adjacency) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\n")

    D = load_D()
    print(f"Anchors (cross-finding-011):")
    print(f"  L_mushaf       = {L_MUSHAF:.4f}")
    print(f"  L_2opt (unc.)  = {L_2OPT_UNCONSTRAINED:.4f}")
    print(f"  Ratio mushaf/2opt = {L_MUSHAF/L_2OPT_UNCONSTRAINED:.4f}")
    print(f"  Residual = {(L_MUSHAF/L_2OPT_UNCONSTRAINED - 1) * 100:.2f}%\n")

    # Sanity: my unconstrained 2-opt should match or beat L_2opt = 77.47
    print("Sanity check: my unconstrained 2-opt (20 random starts)...")
    _, L_unc = best_2opt_unconstrained(D, n_starts=20)
    print(f"  My L_2opt(unconstrained) = {L_unc:.4f}  (cross-finding-011 reports 77.47)")
    # Use the BEST of mine vs cross-finding-011's
    L_2opt_best = min(L_unc, L_2OPT_UNCONSTRAINED)
    print(f"  Using L_2opt = {L_2opt_best:.4f}\n")

    # Constrained tests
    test_pairs = [
        ("Hijra-kink Q56-Q57", (56, 57)),
        ("Q1-Q2 (canonical opener)", (1, 2)),
        ("Q113-Q114 (terminal-pair canonical)", (113, 114)),
        ("Q1-Q113 (random non-canonical)", (1, 113)),
        ("Q50-Q90 (random non-canonical)", (50, 90)),
        ("Q9-Q108 (random non-canonical)", (9, 108)),
    ]

    results = []
    for label, pair in test_pairs:
        print(f"--- Testing constraint: {label} (pair {pair}) ---")
        _, L_constrained = best_2opt_with_adjacency(D, pair, n_starts=50)
        delta = L_constrained - L_2opt_best
        frac_residual_explained = delta / (L_MUSHAF - L_2opt_best) if L_MUSHAF > L_2opt_best else 0
        residual_left = (L_MUSHAF - L_constrained) / L_MUSHAF * 100
        print(f"  L_2opt|{pair} = {L_constrained:.4f}")
        print(f"  Δ = {delta:.4f}")
        print(f"  Fraction-of-residual-explained = {frac_residual_explained:.4f}")
        print(f"  Residual left after constraint  = {residual_left:.2f}%\n")
        results.append({
            "label": label,
            "pair": pair,
            "L_constrained": L_constrained,
            "delta": delta,
            "fraction_residual_explained": frac_residual_explained,
            "residual_left_pct": residual_left,
        })

    # Verdict
    hijra = next(r for r in results if r["pair"] == (56, 57))
    if hijra["fraction_residual_explained"] >= 0.50:
        verdict = "STRONG-PASS — Hijra-kink alone explains ≥50% of TSP-residual"
    elif hijra["fraction_residual_explained"] >= 0.20:
        verdict = "DIRECTIONAL — Hijra-kink explains 20-50% of TSP-residual"
    elif hijra["fraction_residual_explained"] >= 0.05:
        verdict = "MARGINAL — Hijra-kink contributes 5-20% of residual"
    else:
        verdict = "NULL — Hijra-kink does NOT explain TSP-residual; other factors dominate"
    print(f"=== VERDICT: {verdict} ===")
    print(f"  Hijra-kink fraction explained: {hijra['fraction_residual_explained']:.4f}")

    out = {
        "id": "H-NEW-670",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "anchors": {
            "L_mushaf": L_MUSHAF,
            "L_2opt_unconstrained_cf011": L_2OPT_UNCONSTRAINED,
            "L_2opt_unconstrained_my": L_unc,
            "L_2opt_used": L_2opt_best,
        },
        "tests": results,
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
