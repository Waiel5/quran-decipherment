#!/usr/bin/env python3
"""H-NEW-720: Full canonical-adjacency residual-cost map.

Sweeps all 113 canonical adjacencies (Q s, Q s+1), s ∈ {1,...,113}.
For each pair, runs constrained 2-opt with 50 random starts and records
Δ_s = L_2opt|s,s+1 − L_2opt (anchor: 77.466858).

Pre-reg: h-new-720-canonical-adjacency-cost-prereg.md
"""
import hashlib
import json
import random
import time
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-720-canonical-adjacency-cost-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-720.json"
SEED = 20260441

L_MUSHAF = 85.759656
L_2OPT_UNCONSTRAINED = 77.466858  # cross-finding-011 anchor
RESIDUAL = L_MUSHAF - L_2OPT_UNCONSTRAINED  # 8.292798

N_STARTS = 50
N_ITER_MAX = 2000


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


def two_opt_path_constrained(D, path, force_adj_pair, n_iter_max=N_ITER_MAX):
    """2-opt with O(1) constraint check via position tracking.
    Preserves (a, b) adjacency throughout."""
    a_force, b_force = force_adj_pair
    best = path[:]
    best_L = path_length(D, best)
    n = len(best)

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
    a, b = force_adj_pair
    others = [s for s in range(1, n_surahs + 1) if s != a and s != b]
    rng.shuffle(others)
    insert_at = rng.randint(0, len(others))
    return others[:insert_at] + [a, b] + others[insert_at:]


def best_2opt_with_adjacency(D, force_adj_pair, n_starts=N_STARTS, base_seed=SEED):
    best_L = float("inf")
    best_p = None
    for k in range(n_starts):
        rng = random.Random(base_seed + k * 1000 + force_adj_pair[0])
        p = random_path_with_adjacency(rng, force_adj_pair)
        p, L = two_opt_path_constrained(D, p, force_adj_pair, n_iter_max=N_ITER_MAX)
        if L < best_L:
            best_L = L
            best_p = p
    return best_p, best_L


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-720 (Full canonical-adjacency residual-cost map) ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Seed: {SEED}")
    print(f"Starts/pair: {N_STARTS}, max-iter: {N_ITER_MAX}\n")

    D = load_D()
    print(f"Anchors:")
    print(f"  L_mushaf       = {L_MUSHAF:.6f}")
    print(f"  L_2opt (anc.)  = {L_2OPT_UNCONSTRAINED:.6f}")
    print(f"  Residual       = {RESIDUAL:.6f} length-units ({RESIDUAL/L_MUSHAF*100:.2f}%)\n")

    results = []
    t_start = time.time()
    for s in range(1, 114):
        pair = (s, s + 1)
        t0 = time.time()
        _, L_constrained = best_2opt_with_adjacency(D, pair)
        delta = L_constrained - L_2OPT_UNCONSTRAINED
        # Floor at 0 — negative deltas are 2-opt noise, report magnitude separately
        delta_floored = max(0.0, delta)
        frac = delta_floored / RESIDUAL
        elapsed = time.time() - t0
        total_elapsed = time.time() - t_start
        results.append({
            "s": s,
            "pair": [s, s + 1],
            "L_constrained": L_constrained,
            "delta_raw": delta,
            "delta": delta_floored,
            "fraction_residual": frac,
            "elapsed_sec": elapsed,
        })
        print(f"  s={s:3d} (Q{s}-Q{s+1}): L={L_constrained:.4f}  Δ={delta:+.4f}  frac={frac:.4f}  ({elapsed:.1f}s, total {total_elapsed:.0f}s)")

    # Sort by Δ
    sorted_by_delta = sorted(results, key=lambda r: r["delta"], reverse=True)
    top10 = sorted_by_delta[:10]
    bot10 = sorted_by_delta[-10:][::-1]  # ascending: cheapest first

    # Cumulative stats
    deltas = [r["delta"] for r in results]
    raw_deltas = [r["delta_raw"] for r in results]
    sum_delta = sum(deltas)
    mean_delta = sum_delta / len(deltas)
    sorted_d = sorted(deltas)
    median_delta = sorted_d[len(sorted_d) // 2]
    max_delta = max(deltas)
    min_raw = min(raw_deltas)
    var = sum((d - mean_delta) ** 2 for d in deltas) / len(deltas)
    std_delta = var ** 0.5

    # Structural findings
    top3_sum = sum(r["delta"] for r in sorted_by_delta[:3])
    finding_a_threshold = 0.25 * RESIDUAL
    finding_a = top3_sum >= finding_a_threshold

    bot30_sum = sum(r["delta"] for r in sorted_by_delta[-30:])
    finding_b_threshold = 0.05 * RESIDUAL
    finding_b = bot30_sum <= finding_b_threshold

    # Near-Hijra cluster: s ∈ [50, 66] -> 17 pairs (Q50-Q51 through Q66-Q67)
    near_hijra = [r for r in results if 50 <= r["s"] <= 66]
    near_hijra_sum = sum(r["delta"] for r in near_hijra)
    finding_c_threshold = 0.15 * RESIDUAL
    finding_c = near_hijra_sum >= finding_c_threshold

    print(f"\n=== TOP-10 most-expensive ===")
    for r in top10:
        print(f"  Q{r['pair'][0]}-Q{r['pair'][1]}: Δ={r['delta']:.4f}  frac={r['fraction_residual']:.4f}")

    print(f"\n=== BOTTOM-10 least-expensive ===")
    for r in bot10:
        print(f"  Q{r['pair'][0]}-Q{r['pair'][1]}: Δ={r['delta']:.4f}  frac={r['fraction_residual']:.4f}")

    print(f"\n=== Cumulative stats ===")
    print(f"  Σ Δ_s (113 pairs)  = {sum_delta:.4f}")
    print(f"  L_mushaf − L_2opt = {RESIDUAL:.4f}")
    print(f"  Σ Δ / residual    = {sum_delta/RESIDUAL:.4f} (sub-additive if <1, super-additive if >1)")
    print(f"  mean Δ            = {mean_delta:.4f}")
    print(f"  median Δ          = {median_delta:.4f}")
    print(f"  std Δ             = {std_delta:.4f}")
    print(f"  max Δ             = {max_delta:.4f}")
    print(f"  min raw Δ         = {min_raw:.4f}  (negative = 2-opt noise)")

    print(f"\n=== Structural findings ===")
    print(f"  FINDING-A (top-3 ≥ 25% residual): top3_sum={top3_sum:.4f}, threshold={finding_a_threshold:.4f} → {'PASS' if finding_a else 'FAIL'}")
    print(f"  FINDING-B (bot-30 ≤ 5% residual): bot30_sum={bot30_sum:.4f}, threshold={finding_b_threshold:.4f} → {'PASS' if finding_b else 'FAIL'}")
    print(f"  FINDING-C (Q50-Q66 cluster ≥ 15% residual): cluster_sum={near_hijra_sum:.4f}, threshold={finding_c_threshold:.4f} → {'PASS' if finding_c else 'FAIL'}")

    out = {
        "id": "H-NEW-720",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "n_starts": N_STARTS,
        "n_iter_max": N_ITER_MAX,
        "anchors": {
            "L_mushaf": L_MUSHAF,
            "L_2opt_unconstrained": L_2OPT_UNCONSTRAINED,
            "residual": RESIDUAL,
        },
        "per_adjacency": results,
        "top10_expensive": top10,
        "bottom10_cheap": bot10,
        "cumulative_stats": {
            "sum_delta": sum_delta,
            "mean_delta": mean_delta,
            "median_delta": median_delta,
            "std_delta": std_delta,
            "max_delta": max_delta,
            "min_raw_delta": min_raw,
            "ratio_sum_to_residual": sum_delta / RESIDUAL,
        },
        "structural_findings": {
            "finding_a_top3_25pct": {
                "top3_sum": top3_sum,
                "threshold": finding_a_threshold,
                "verdict": "PASS" if finding_a else "FAIL",
            },
            "finding_b_bot30_5pct": {
                "bot30_sum": bot30_sum,
                "threshold": finding_b_threshold,
                "verdict": "PASS" if finding_b else "FAIL",
            },
            "finding_c_near_hijra_15pct": {
                "cluster_range_s": [50, 66],
                "cluster_sum": near_hijra_sum,
                "threshold": finding_c_threshold,
                "verdict": "PASS" if finding_c else "FAIL",
            },
        },
        "total_walltime_sec": time.time() - t_start,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")
    print(f"Total walltime: {time.time() - t_start:.1f}s")


if __name__ == "__main__":
    main()
