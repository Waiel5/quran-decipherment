#!/usr/bin/env python3
"""H-NEW-590: Outlier-strength spectrum — convert cross-finding-024 Factor 5 from binary to continuous.

For each candidate surah X, compute Δ%ile(X) = %ile(W) − %ile(W\X) where W is a 7-surah
window centered on X (edge-clipped at corpus boundaries). Larger Δ = stronger outlier.

Replication target: Q 55 Δ ≥ 25 (H-NEW-390 reproduces +32.6pp at NEAR-window).
Supporting target: corpus-wide Spearman bootstrap rank-stability ≥ 0.95.
"""
import hashlib
import itertools
import json
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-590-outlier-spectrum-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-590.json"

PREREG_SHA_EXPECTED = "0c75ee51c5689799989088ff9b3902c8614fa3ec967144d7530f7920f753efae"

SEED = 20260429
N_PERM = 10000
N_BOOTSTRAP = 200  # for Spearman rank stability

CANDIDATES = [1, 9, 18, 55, 62, 112]
N_SURAHS = 114


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D() -> list:
    """Returns 115x115 symmetric distance matrix indexed 1..114 (row/col 0 unused)."""
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0] * (N_SURAHS + 1) for _ in range(N_SURAHS + 1)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def mean_pw(s, D) -> float:
    pairs = list(itertools.combinations(s, 2))
    return sum(D[a][b] for a, b in pairs) / len(pairs) if pairs else 0.0


def window_for(X: int, half: int = 3) -> list:
    """Centered window. Edge-clip: keep total size constant at 2*half+1 by sliding inward."""
    size = 2 * half + 1
    lo = X - half
    hi = X + half
    if lo < 1:
        lo = 1
        hi = lo + size - 1
    if hi > N_SURAHS:
        hi = N_SURAHS
        lo = hi - size + 1
    return list(range(lo, hi + 1))


def percentile_against_null(d_obs: float, nulls: list) -> float:
    """%ile = fraction of nulls with null value ≤ d_obs (so larger d_obs ⇒ higher %ile)."""
    return 100.0 * sum(1 for x in nulls if x <= d_obs) / len(nulls)


def compute_delta(X: int, D, nulls_size7: list, nulls_size6: list) -> dict:
    W = window_for(X)
    W_minus = [s for s in W if s != X]
    d_W = mean_pw(W, D)
    d_minus = mean_pw(W_minus, D)
    pct_W = percentile_against_null(d_W, nulls_size7)
    pct_minus = percentile_against_null(d_minus, nulls_size6)
    delta = pct_W - pct_minus
    # descriptive p (one-sided: probability under null of d ≥ d_W, treating outlier-direction)
    p_greater_W = sum(1 for x in nulls_size7 if x >= d_W) / len(nulls_size7)
    return {
        "X": X,
        "window": W,
        "window_minus_X": W_minus,
        "d_W": d_W,
        "d_W_minus_X": d_minus,
        "pct_W": pct_W,
        "pct_W_minus_X": pct_minus,
        "delta_pct": delta,
        "p_greater_W": p_greater_W,
    }


def classify(delta: float) -> str:
    if delta >= 25:
        return "STRONG_OUTLIER"
    if delta >= 10:
        return "MODERATE_OUTLIER"
    if delta > 0:
        return "WEAK_OUTLIER"
    if delta > -5:
        return "NULL"
    if delta > -10:
        return "WEAK_ANCHOR"
    return "COHESION_ANCHOR"


def spearman(a: list, b: list) -> float:
    n = len(a)
    if n != len(b) or n < 2:
        return float("nan")
    ra = rank(a)
    rb = rank(b)
    mean_a = sum(ra) / n
    mean_b = sum(rb) / n
    num = sum((ra[i] - mean_a) * (rb[i] - mean_b) for i in range(n))
    den_a = sum((ra[i] - mean_a) ** 2 for i in range(n)) ** 0.5
    den_b = sum((rb[i] - mean_b) ** 2 for i in range(n)) ** 0.5
    if den_a == 0 or den_b == 0:
        return float("nan")
    return num / (den_a * den_b)


def rank(values: list) -> list:
    indexed = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(values):
        j = i
        while j + 1 < len(values) and values[indexed[j + 1]] == values[indexed[i]]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[indexed[k]] = avg_rank
        i = j + 1
    return ranks


def main():
    print("=" * 64)
    print("H-NEW-590 — Outlier-strength spectrum")
    print("=" * 64)

    actual_sha = sha(PREREG)
    print(f"Pre-reg path: {PREREG}")
    print(f"Pre-reg SHA: {actual_sha}")
    print(f"Expected:    {PREREG_SHA_EXPECTED}")
    if actual_sha != PREREG_SHA_EXPECTED:
        print("WARNING: pre-reg SHA mismatch — pre-reg may have been edited after locking.")
    else:
        print("Pre-reg SHA verified.")

    print(f"\nSeed: {SEED}; N_PERM: {N_PERM}")
    D = load_D()

    # Build shared null distributions for size 7 and size 6
    print("\nBuilding null distributions (10000 each for size 7 and size 6)...")
    rng = random.Random(SEED)
    surahs = list(range(1, N_SURAHS + 1))
    nulls_size7 = []
    nulls_size6 = []
    for _ in range(N_PERM):
        nulls_size7.append(mean_pw(rng.sample(surahs, 7), D))
        nulls_size6.append(mean_pw(rng.sample(surahs, 6), D))
    print(f"  null_size7 mean={sum(nulls_size7)/N_PERM:.4f}; "
          f"null_size6 mean={sum(nulls_size6)/N_PERM:.4f}")

    # Per-candidate Δ
    print("\n--- 6 PRE-REGISTERED CANDIDATES ---")
    candidate_results = []
    for X in CANDIDATES:
        r = compute_delta(X, D, nulls_size7, nulls_size6)
        r["classification"] = classify(r["delta_pct"])
        candidate_results.append(r)
        print(f"\nQ {X:>3}  W={r['window']}")
        print(f"       d̄(W)={r['d_W']:.4f} at {r['pct_W']:.2f}%ile (null-7)")
        print(f"       d̄(W\\X)={r['d_W_minus_X']:.4f} at {r['pct_W_minus_X']:.2f}%ile (null-6)")
        print(f"       Δ%ile={r['delta_pct']:+.2f}pp  → {r['classification']}")

    # PRIMARY pre-committed test: Q 55 Δ ≥ 25
    q55 = next(r for r in candidate_results if r["X"] == 55)
    q55_replication = q55["delta_pct"] >= 25.0
    print(f"\nPRIMARY PRE-COMMIT: Q 55 Δ ≥ 25 — Δ={q55['delta_pct']:+.2f}pp → "
          f"{'CONFIRMED' if q55_replication else 'FAILED'}")

    # Corpus-wide Δ ranking
    print("\n--- CORPUS-WIDE Δ RANKING (descriptive) ---")
    all_results = []
    for X in range(1, N_SURAHS + 1):
        r = compute_delta(X, D, nulls_size7, nulls_size6)
        r["classification"] = classify(r["delta_pct"])
        all_results.append(r)

    sorted_by_delta = sorted(all_results, key=lambda r: -r["delta_pct"])
    print("\nTop 10 outliers (largest +Δ):")
    for r in sorted_by_delta[:10]:
        print(f"  Q {r['X']:>3}  Δ={r['delta_pct']:+6.2f}pp  ({r['classification']})  W={r['window']}")
    print("\nBottom 10 cohesion-anchors (smallest/most-negative Δ):")
    for r in sorted_by_delta[-10:]:
        print(f"  Q {r['X']:>3}  Δ={r['delta_pct']:+6.2f}pp  ({r['classification']})  W={r['window']}")

    # Spearman bootstrap rank stability
    # Resample null distributions with different sub-seeds; recompute Δ vector; Spearman correlate
    print(f"\n--- SPEARMAN BOOTSTRAP RANK STABILITY (N={N_BOOTSTRAP}) ---")
    base_deltas = [r["delta_pct"] for r in all_results]
    spearmans = []
    for b in range(N_BOOTSTRAP):
        sub_seed = SEED + 1 + b
        sub_rng = random.Random(sub_seed)
        sub_nulls7 = [mean_pw(sub_rng.sample(surahs, 7), D) for _ in range(N_PERM)]
        sub_nulls6 = [mean_pw(sub_rng.sample(surahs, 6), D) for _ in range(N_PERM)]
        sub_deltas = []
        for X in range(1, N_SURAHS + 1):
            W = window_for(X)
            W_minus = [s for s in W if s != X]
            pct_W = percentile_against_null(mean_pw(W, D), sub_nulls7)
            pct_minus = percentile_against_null(mean_pw(W_minus, D), sub_nulls6)
            sub_deltas.append(pct_W - pct_minus)
        spearmans.append(spearman(base_deltas, sub_deltas))
        if (b + 1) % 50 == 0:
            print(f"  bootstrap {b+1}/{N_BOOTSTRAP}: ρ={spearmans[-1]:.4f}")
    spearman_mean = sum(spearmans) / len(spearmans)
    spearman_min = min(spearmans)
    spearman_lt_0_95 = sum(1 for s in spearmans if s < 0.95) / len(spearmans)
    print(f"\nSpearman bootstrap: mean ρ = {spearman_mean:.4f}; min = {spearman_min:.4f}")
    print(f"Fraction of bootstraps with ρ < 0.95: {spearman_lt_0_95:.4f}")
    rank_stability_pass = spearman_mean >= 0.95

    # Verdict aggregation
    if q55_replication and rank_stability_pass:
        verdict = "REPLICATION CONFIRMED + RANK STABILITY SUPPORTING"
    elif q55_replication:
        verdict = f"REPLICATION CONFIRMED; rank stability marginal (ρ̄={spearman_mean:.3f})"
    elif rank_stability_pass:
        verdict = f"REPLICATION FAILED (Q55 Δ={q55['delta_pct']:+.2f}); rank stability supporting"
    else:
        verdict = (f"REPLICATION FAILED (Q55 Δ={q55['delta_pct']:+.2f}); "
                   f"rank stability marginal (ρ̄={spearman_mean:.3f})")
    print(f"\nVerdict: {verdict}")

    # Write JSON
    out = {
        "id": "H-NEW-590",
        "title": "Outlier-strength spectrum — Factor 5 binary→continuous",
        "prereg_sha": actual_sha,
        "prereg_sha_expected": PREREG_SHA_EXPECTED,
        "seed": SEED,
        "n_perm": N_PERM,
        "n_bootstrap": N_BOOTSTRAP,
        "bonferroni_k": 6,
        "alpha_bon": 0.0083,
        "candidates": CANDIDATES,
        "candidate_results": candidate_results,
        "q55_replication_pass": q55_replication,
        "q55_delta_pct": q55["delta_pct"],
        "all_surahs_results": all_results,
        "top_10_outliers": [
            {"X": r["X"], "delta_pct": r["delta_pct"], "classification": r["classification"]}
            for r in sorted_by_delta[:10]
        ],
        "bottom_10_anchors": [
            {"X": r["X"], "delta_pct": r["delta_pct"], "classification": r["classification"]}
            for r in sorted_by_delta[-10:]
        ],
        "spearman_bootstrap": {
            "n": N_BOOTSTRAP,
            "mean": spearman_mean,
            "min": spearman_min,
            "frac_below_0_95": spearman_lt_0_95,
            "pass": rank_stability_pass,
        },
        "verdict": verdict,
        "null_size7_mean": sum(nulls_size7) / N_PERM,
        "null_size6_mean": sum(nulls_size6) / N_PERM,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
