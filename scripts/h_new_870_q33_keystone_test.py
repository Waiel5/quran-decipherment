#!/usr/bin/env python3
"""H-NEW-870: Q 33 al-Aḥzāb architectural-keystone test.

Question: Does the compression-tail law (H-NEW-660, R²=0.986) survive removal of Q 33?

Test design:
- Baseline: H-NEW-660 reproduction on 114-surah mushaf, K=15 windows starting at s=1..100.
- Counterfactual: REMOVE Q 33 from the mushaf, re-index the surviving 113 surahs as
  positions 1..113, recompute K=15 windows starting at s=1..99 (=> 99 windows).
- Re-fit linear, quadratic, and two-piece (kink ∈ {25, 50, 75}) models.
- Compare two-piece R² with vs without Q 33.
  * If R² drops by ≥5pp ⇒ Q 33 is a structural keystone (load-bearing).
  * If R² drops by <2pp ⇒ Q 33 is a high-magnitude outlier that does NOT carry the law.
  * Intermediate: partial keystone.

Also report: top 5 surahs whose removal most damages the law (sensitivity sweep), so
Q 33's role is contextualized against the rest of the corpus.

This script is INDEPENDENT of any rules-tuple choice — it operates on the H-NEW-111
distance matrix as-loaded.

Seed: 20260470
"""
import hashlib
import json
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-870.json"
SEED = 20260470  # for any future stochastic step
K = 15
N_SURAHS = 114


# ---------- distance matrix loader (1..114 indexed; row/col 0 unused) ----------
def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D() -> list:
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0] * (N_SURAHS + 1) for _ in range(N_SURAHS + 1)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def mean_pairwise(D, subset):
    pairs = list(combinations(subset, 2))
    if not pairs:
        return 0.0
    return sum(D[a][b] for a, b in pairs) / len(pairs)


# ---------- model fitters ----------
def fit_linear(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return None, None, 0.0
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * x for x in xs]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2


def fit_quadratic(xs, ys):
    n = len(xs)
    sx = sum(xs); sx2 = sum(x * x for x in xs); sx3 = sum(x ** 3 for x in xs); sx4 = sum(x ** 4 for x in xs)
    sy = sum(ys); sxy = sum(xs[i] * ys[i] for i in range(n)); sx2y = sum(xs[i] ** 2 * ys[i] for i in range(n))
    M = [[n, sx, sx2], [sx, sx2, sx3], [sx2, sx3, sx4]]
    b = [sy, sxy, sx2y]
    A = [row[:] + [b[i]] for i, row in enumerate(M)]
    for col in range(3):
        pivot = max(range(col, 3), key=lambda r: abs(A[r][col]))
        A[col], A[pivot] = A[pivot], A[col]
        piv = A[col][col]
        if abs(piv) < 1e-15:
            return None, None, None, 0.0
        A[col] = [x / piv for x in A[col]]
        for r in range(3):
            if r == col:
                continue
            factor = A[r][col]
            A[r] = [A[r][k] - factor * A[col][k] for k in range(4)]
    a, bx, c = A[0][3], A[1][3], A[2][3]
    yhat = [a + bx * x + c * x * x for x in xs]
    my = sum(ys) / n
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return a, bx, c, r2


def fit_two_piece(xs, ys, kink):
    n = len(xs)
    feat = [max(0, x - kink) for x in xs]
    mx, my = sum(feat) / n, sum(ys) / n
    num = sum((feat[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((feat[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return None, None, 0.0
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * f for f in feat]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2


# ---------- compression-tail computation given an ordered surah list ----------
def compression_tail(D, surah_list, K=15):
    """Return list of (window_start, d_bar) for all consecutive K-windows over surah_list."""
    n = len(surah_list)
    n_windows = n - K + 1
    starts = list(range(1, n_windows + 1))
    d_obs = []
    for s in starts:
        sub = surah_list[s - 1: s - 1 + K]
        d_obs.append(mean_pairwise(D, sub))
    return starts, d_obs


def fit_all_models(starts, d_obs):
    s_center = [s - (sum(starts) / len(starts)) for s in starts]
    a_lin, b_lin, r2_lin = fit_linear(s_center, d_obs)
    a_q, b_q, c_q, r2_q = fit_quadratic(s_center, d_obs)
    best_r2 = -1
    best_kink = None
    best_two = None
    for kink in [25, 50, 75]:
        out = fit_two_piece(starts, d_obs, kink)
        if out[2] > best_r2:
            best_r2 = out[2]
            best_kink = kink
            best_two = out
    return {
        "linear": {"alpha": a_lin, "beta": b_lin, "r2": r2_lin},
        "quadratic": {"alpha": a_q, "beta": b_q, "gamma": c_q, "r2": r2_q},
        "two_piece": {"kink": best_kink, "alpha": best_two[0], "beta": best_two[1], "r2": best_two[2]},
        "primary_r2": max(r2_lin, r2_q, best_two[2]),
        "primary_model": max(
            [("linear", r2_lin), ("quadratic", r2_q), (f"two_piece_kink_{best_kink}", best_two[2])],
            key=lambda t: t[1],
        )[0],
    }


def main():
    print("=" * 64)
    print("H-NEW-870 — Q 33 al-Aḥzāb architectural-keystone test")
    print("=" * 64)
    print(f"Seed: {SEED}; K={K}")
    print(f"H-NEW-111 SHA: {sha(H_NEW_111)}")

    D = load_D()
    full_mushaf = list(range(1, N_SURAHS + 1))

    # ---------- 1. Baseline (114 surahs, replicates H-NEW-660) ----------
    print("\n--- BASELINE (114 surahs, all canonical positions) ---")
    starts_b, d_b = compression_tail(D, full_mushaf, K)
    base = fit_all_models(starts_b, d_b)
    print(f"Linear     R² = {base['linear']['r2']:.4f}, β = {base['linear']['beta']:+.5f}")
    print(f"Quadratic  R² = {base['quadratic']['r2']:.4f}")
    print(f"Two-piece  R² = {base['two_piece']['r2']:.4f}, kink at s={base['two_piece']['kink']}")
    print(f"Primary    : {base['primary_model']} (R² = {base['primary_r2']:.4f})")

    # ---------- 2. Counterfactual: remove Q 33 ----------
    print("\n--- COUNTERFACTUAL (113 surahs, Q 33 al-Aḥzāb removed) ---")
    no33 = [s for s in full_mushaf if s != 33]
    starts_c, d_c = compression_tail(D, no33, K)
    cf = fit_all_models(starts_c, d_c)
    print(f"Linear     R² = {cf['linear']['r2']:.4f}, β = {cf['linear']['beta']:+.5f}")
    print(f"Quadratic  R² = {cf['quadratic']['r2']:.4f}")
    print(f"Two-piece  R² = {cf['two_piece']['r2']:.4f}, kink at s={cf['two_piece']['kink']}")
    print(f"Primary    : {cf['primary_model']} (R² = {cf['primary_r2']:.4f})")

    # ---------- 3. Sensitivity sweep: remove each surah, measure two-piece R² damage ----------
    print("\n--- SENSITIVITY SWEEP (remove each of 114 surahs, measure two-piece R²) ---")
    base_two_r2 = base["two_piece"]["r2"]
    sweep = []
    for x in range(1, N_SURAHS + 1):
        sublist = [s for s in full_mushaf if s != x]
        s_x, d_x = compression_tail(D, sublist, K)
        m = fit_all_models(s_x, d_x)
        delta = base_two_r2 - m["two_piece"]["r2"]
        sweep.append({
            "removed_surah": x,
            "two_piece_r2": m["two_piece"]["r2"],
            "delta_r2_vs_base": delta,
            "primary_r2": m["primary_r2"],
            "primary_model": m["primary_model"],
        })
    sweep_sorted = sorted(sweep, key=lambda r: -r["delta_r2_vs_base"])

    print("\nTop-10 keystones (largest two-piece R² drop when removed):")
    for r in sweep_sorted[:10]:
        print(f"  Q {r['removed_surah']:>3}  ΔR² = {r['delta_r2_vs_base']:+.4f}  "
              f"(after-removal R² = {r['two_piece_r2']:.4f})")

    print("\nBottom-10 anti-keystones (smallest/negative R² drop = removal IMPROVES fit):")
    for r in sweep_sorted[-10:]:
        print(f"  Q {r['removed_surah']:>3}  ΔR² = {r['delta_r2_vs_base']:+.4f}  "
              f"(after-removal R² = {r['two_piece_r2']:.4f})")

    # Q 33 specifically
    q33_entry = next(r for r in sweep if r["removed_surah"] == 33)
    q33_rank = next(i + 1 for i, r in enumerate(sweep_sorted) if r["removed_surah"] == 33)
    print(f"\n*** Q 33 specifically: ΔR² = {q33_entry['delta_r2_vs_base']:+.4f}, "
          f"rank {q33_rank} of 114 by R²-damage ***")

    # ---------- 4. Verdict ----------
    drop = base_two_r2 - cf["two_piece"]["r2"]
    if drop >= 0.05:
        verdict = (f"STRUCTURAL KEYSTONE — removing Q 33 drops two-piece R² by "
                   f"{drop:.4f} (≥0.05). The compression-tail law is partly LOAD-BEARING on Q 33.")
    elif drop >= 0.02:
        verdict = (f"PARTIAL KEYSTONE — removing Q 33 drops two-piece R² by "
                   f"{drop:.4f} (between 0.02 and 0.05). Q 33 contributes but is not solely "
                   f"load-bearing.")
    elif drop >= -0.005:
        verdict = (f"NOT A KEYSTONE — removing Q 33 changes two-piece R² by only "
                   f"{drop:+.4f}. Q 33 is a HIGH-MAGNITUDE OUTLIER but the law is robust without it.")
    else:
        verdict = (f"ANTI-KEYSTONE — removing Q 33 IMPROVES the fit by {-drop:+.4f}. "
                   f"Q 33 is local noise relative to the global compression-tail law.")
    print(f"\n=== VERDICT: {verdict} ===")

    # ---------- 5. Where does Q 33 sit relative to the K=15 windows that contain it? ----------
    # Q 33 appears in windows starting at s=19..33 in the 114-version (need s ≤ 33 and s+K-1 ≥ 33)
    print("\n--- Q 33 IS A MEMBER OF WHICH BASELINE K=15 WINDOWS? ---")
    print("(window-start s, d̄_with_Q33, d̄_without_Q33 [as 14-surah mean])")
    for s in range(max(1, 33 - K + 1), min(101, 33) + 1):
        sub_with = list(range(s, s + K))
        if 33 not in sub_with:
            continue
        d_with = mean_pairwise(D, sub_with)
        sub_without = [x for x in sub_with if x != 33]
        d_without = mean_pairwise(D, sub_without)
        print(f"  s={s:>3}  window={sub_with[0]}-{sub_with[-1]}  "
              f"d̄_with={d_with:.4f}  d̄_without={d_without:.4f}  Δ={d_with - d_without:+.4f}")

    # ---------- 6. Write JSON ----------
    out = {
        "id": "H-NEW-870",
        "title": "Q 33 al-Aḥzāb architectural-keystone test",
        "seed": SEED,
        "K": K,
        "h_new_111_sha": sha(H_NEW_111),
        "baseline_full_mushaf": {
            "n_surahs": N_SURAHS,
            "n_windows": len(starts_b),
            "linear": base["linear"],
            "quadratic": base["quadratic"],
            "two_piece": base["two_piece"],
            "primary_model": base["primary_model"],
            "primary_r2": base["primary_r2"],
        },
        "counterfactual_no_q33": {
            "n_surahs": 113,
            "n_windows": len(starts_c),
            "linear": cf["linear"],
            "quadratic": cf["quadratic"],
            "two_piece": cf["two_piece"],
            "primary_model": cf["primary_model"],
            "primary_r2": cf["primary_r2"],
        },
        "two_piece_r2_drop_with_q33_removed": drop,
        "sensitivity_sweep": sweep,
        "top_10_keystones": sweep_sorted[:10],
        "bottom_10_anti_keystones": sweep_sorted[-10:],
        "q33_keystone_rank": q33_rank,
        "q33_two_piece_r2_drop": q33_entry["delta_r2_vs_base"],
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
