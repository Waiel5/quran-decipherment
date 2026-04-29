#!/usr/bin/env python3
"""H-NEW-690: Causal generative test of the compression-tail law.

Question: if a generative simulator is constrained ONLY by the compression-tail law
(H-NEW-660: two-piece-kink-50 fit with R² ≥ 0.95, β ∈ [-0.015, -0.010]), does it
produce orderings whose FR-TSP-residual matches canonical mushaf's ~11%?

PRE-REG-STANDARD-04. Pre-reg SHA embedded below.
"""
import hashlib
import json
import math
import random
from itertools import combinations
from pathlib import Path
import time

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-690-causal-generative-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-690.json"
EXPECTED_PREREG_SHA = "21d56df2bcf132dd219846ce7152df2e089e876a85dc5b089e8a30257efadfda"

SEED = 20260437
N_STEPS = 10000
N_BURN = 1000
N_SAMPLES = 100
SAMPLE_EVERY = 100  # post-burn-in
K = 15  # window size
KINK = 50
R2_MIN = 0.95
BETA_LO = -0.015
BETA_HI = -0.010
T_MH = 1.0

# Locked from h-new-111.json
L_CANONICAL = 85.759656
L_2OPT = 77.466858
CANONICAL_RESIDUAL = (L_CANONICAL - L_2OPT) / L_2OPT  # ~0.10705


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    """Load FR distance matrix as 115x115 (1-indexed). D[i][j] for surahs i,j ∈ [1,114]."""
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def window_mean(D, surahs):
    """Mean pairwise FR distance over a list of surah IDs."""
    n = len(surahs)
    if n < 2:
        return 0.0
    s = 0.0
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            s += D[surahs[i]][surahs[j]]
            cnt += 1
    return s / cnt


def all_window_means(D, perm):
    """For an ordering perm (list of 114 surah IDs), compute d̄ for windows starting at s=1..100."""
    out = []
    for s in range(1, 101):
        # Window covers positions s..s+K-1 (1-indexed). 0-indexed slice: [s-1 : s-1+K]
        sub = perm[s - 1: s - 1 + K]
        out.append(window_mean(D, sub))
    return out


def fit_two_piece(d_obs, kink=KINK):
    """y = a + b * max(0, x - kink). x = window-start s ∈ {1..100}."""
    n = len(d_obs)
    xs = list(range(1, n + 1))
    feat = [max(0, x - kink) for x in xs]
    mx = sum(feat) / n
    my = sum(d_obs) / n
    num = sum((feat[i] - mx) * (d_obs[i] - my) for i in range(n))
    den = sum((feat[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return None, None, 0.0
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * f for f in feat]
    ss_tot = sum((y - my) ** 2 for y in d_obs)
    ss_res = sum((d_obs[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2


def constraint_ok(r2, beta):
    return (r2 >= R2_MIN) and (BETA_LO <= beta <= BETA_HI)


def fr_tour_length(D, perm):
    """Sum of consecutive FR distances along the ordering perm."""
    L = 0.0
    for i in range(len(perm) - 1):
        L += D[perm[i]][perm[i + 1]]
    return L


def constraint_distance(r2, beta):
    """Distance to feasibility (for warm-up). 0 if feasible."""
    r2_gap = max(0.0, R2_MIN - r2)
    if BETA_LO <= beta <= BETA_HI:
        beta_gap = 0.0
    else:
        beta_gap = min(abs(beta - BETA_LO), abs(beta - BETA_HI))
    # Weight R² gap more heavily
    return 10.0 * r2_gap + beta_gap


def evaluate(D, perm):
    d_obs = all_window_means(D, perm)
    alpha, beta, r2 = fit_two_piece(d_obs)
    L = fr_tour_length(D, perm)
    return alpha, beta, r2, L


def run_chain(D, rng, max_steps=10000, n_burn=1000, n_samples=100, sample_every=100):
    n = 114
    # Step 1: warm-up — find a feasible starting permutation.
    # Start: random; try greedy descent on constraint_distance for up to 5000 proposals.
    perm = list(range(1, 115))
    rng.shuffle(perm)
    alpha, beta, r2, L = evaluate(D, perm)
    cd = constraint_distance(r2, beta)

    warmup_log = {"start_r2": r2, "start_beta": beta, "start_cd": cd, "start_L": L}

    feasible = (cd == 0.0)
    warmup_attempts = 0
    max_warmup = 5000

    while not feasible and warmup_attempts < max_warmup:
        i, j = rng.sample(range(n), 2)
        perm2 = perm[:]
        perm2[i], perm2[j] = perm2[j], perm2[i]
        alpha2, beta2, r2_2, L2 = evaluate(D, perm2)
        cd2 = constraint_distance(r2_2, beta2)
        if cd2 < cd:  # greedy descent on infeasibility
            perm = perm2
            r2, beta, L, cd = r2_2, beta2, L2, cd2
            if cd == 0.0:
                feasible = True
        warmup_attempts += 1

    warmup_log["warmup_attempts"] = warmup_attempts
    warmup_log["warmup_feasible"] = feasible

    if not feasible:
        # Fallback: start from canonical (which satisfies constraint by H-NEW-660 result).
        perm = list(range(1, 115))
        alpha, beta, r2, L = evaluate(D, perm)
        cd = constraint_distance(r2, beta)
        warmup_log["used_canonical_fallback"] = True
        warmup_log["canonical_r2"] = r2
        warmup_log["canonical_beta"] = beta
        warmup_log["canonical_L"] = L
        if cd != 0.0:
            print(f"WARNING: even canonical does not satisfy constraint! r2={r2}, beta={beta}")
    else:
        warmup_log["used_canonical_fallback"] = False

    # Step 2: MH chain. Burn-in n_burn steps, then sample.
    samples = []
    accepts_total = 0
    proposals_total = 0
    accepts_constraint_ok = 0
    proposals_constraint_ok = 0

    sample_indices = []
    next_sample_step = n_burn + sample_every

    for step in range(1, max_steps + 1):
        i, j = rng.sample(range(n), 2)
        perm2 = perm[:]
        perm2[i], perm2[j] = perm2[j], perm2[i]
        alpha2, beta2, r2_2, L2 = evaluate(D, perm2)

        proposals_total += 1
        if constraint_ok(r2_2, beta2):
            proposals_constraint_ok += 1
            # MH step on FR-tour-length
            dL = L2 - L
            if dL <= 0 or rng.random() < math.exp(-dL / T_MH):
                perm = perm2
                r2, beta, L = r2_2, beta2, L2
                accepts_total += 1
                accepts_constraint_ok += 1

        if step >= next_sample_step and len(samples) < n_samples:
            samples.append({
                "step": step,
                "perm": perm[:],
                "r2": r2,
                "beta": beta,
                "L": L,
                "residual": (L - L_2OPT) / L_2OPT,
            })
            sample_indices.append(step)
            next_sample_step += sample_every

    return {
        "warmup": warmup_log,
        "n_steps": max_steps,
        "n_burn": n_burn,
        "n_samples_collected": len(samples),
        "proposals_total": proposals_total,
        "accepts_total": accepts_total,
        "proposals_constraint_ok": proposals_constraint_ok,
        "accepts_constraint_ok": accepts_constraint_ok,
        "samples": samples,
        "sample_indices": sample_indices,
    }


def percentile(sorted_vals, p):
    """Linear interpolation percentile (p in [0,100])."""
    if not sorted_vals:
        return None
    n = len(sorted_vals)
    if n == 1:
        return sorted_vals[0]
    k = (p / 100.0) * (n - 1)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_vals[int(k)]
    return sorted_vals[f] + (k - f) * (sorted_vals[c] - sorted_vals[f])


def main():
    t0 = time.time()
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-690 (Causal generative test of compression-tail law) ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Expected:    {EXPECTED_PREREG_SHA}")
    if prereg_sha != EXPECTED_PREREG_SHA:
        print("WARNING: pre-reg SHA mismatch — pre-reg has been edited since lock.")
    print(f"Seed: {SEED}\n")

    print("Loading FR distance matrix from H-NEW-111...")
    D = load_D()

    # Sanity check: re-evaluate canonical
    canonical = list(range(1, 115))
    alpha_c, beta_c, r2_c, L_c = evaluate(D, canonical)
    print(f"Sanity: canonical → R²={r2_c:.4f}, β={beta_c:+.5f}, L={L_c:.4f}")
    print(f"  Expected: R²≈0.9860, β≈-0.01237, L=85.7597")
    print(f"  Constraint OK: {constraint_ok(r2_c, beta_c)}")

    rng = random.Random(SEED)
    print(f"\nRunning chain: {N_STEPS} steps, burn-in {N_BURN}, sample every {SAMPLE_EVERY}...")
    chain_result = run_chain(D, rng, N_STEPS, N_BURN, N_SAMPLES, SAMPLE_EVERY)
    elapsed = time.time() - t0
    print(f"\nChain done in {elapsed:.1f}s")
    print(f"  Warmup: {chain_result['warmup']}")
    print(f"  Proposals: {chain_result['proposals_total']}, accepts: {chain_result['accepts_total']}")
    print(f"  Constraint-feasible proposals: {chain_result['proposals_constraint_ok']} ({100*chain_result['proposals_constraint_ok']/max(1,chain_result['proposals_total']):.2f}%)")
    print(f"  Samples collected: {chain_result['n_samples_collected']}")

    samples = chain_result["samples"]
    if not samples:
        print("ERROR: no samples collected. Aborting.")
        return

    residuals = sorted([s["residual"] for s in samples])
    Ls = sorted([s["L"] for s in samples])

    median_residual = percentile(residuals, 50)
    p25 = percentile(residuals, 25)
    p75 = percentile(residuals, 75)
    p10 = percentile(residuals, 10)
    p90 = percentile(residuals, 90)

    # Pass-threshold counts (residual ≤ X)
    n_le_115 = sum(1 for r in residuals if r <= 0.115)
    n_le_120 = sum(1 for r in residuals if r <= 0.120)
    n_le_130 = sum(1 for r in residuals if r <= 0.130)
    n = len(residuals)
    pct_le_115 = n_le_115 / n
    pct_le_120 = n_le_120 / n
    pct_le_130 = n_le_130 / n

    # Canonical percentile within ensemble (residual basis)
    n_le_canonical = sum(1 for r in residuals if r <= CANONICAL_RESIDUAL)
    canonical_percentile = 100.0 * n_le_canonical / n

    # Verdict
    if pct_le_115 >= 0.50:
        verdict = "STRONG GENERATIVE"
    elif pct_le_120 >= 0.25:
        verdict = "DIRECTIONAL"
    elif pct_le_130 < 0.10:
        verdict = "NULL"
    else:
        verdict = "AMBIGUOUS"

    summary = {
        "n_samples": n,
        "median_residual": median_residual,
        "p10_residual": p10,
        "p25_residual": p25,
        "p75_residual": p75,
        "p90_residual": p90,
        "min_residual": residuals[0],
        "max_residual": residuals[-1],
        "median_L": percentile(Ls, 50),
        "min_L": Ls[0],
        "max_L": Ls[-1],
        "pct_residual_le_0.115": pct_le_115,
        "pct_residual_le_0.120": pct_le_120,
        "pct_residual_le_0.130": pct_le_130,
        "canonical_residual": CANONICAL_RESIDUAL,
        "canonical_L": L_CANONICAL,
        "L_2opt": L_2OPT,
        "canonical_percentile_in_ensemble": canonical_percentile,
        "verdict": verdict,
    }

    print(f"\n--- HEADLINE ---")
    print(f"Median residual: {median_residual:.4f} ({median_residual*100:.2f}%)")
    print(f"P25-P75: {p25:.4f} – {p75:.4f}  ({p25*100:.2f}% – {p75*100:.2f}%)")
    print(f"Min/Max: {residuals[0]:.4f} / {residuals[-1]:.4f}")
    print(f"Canonical residual: {CANONICAL_RESIDUAL:.4f} ({CANONICAL_RESIDUAL*100:.2f}%)")
    print(f"% of ensemble at residual ≤ 11.5%: {pct_le_115*100:.1f}%")
    print(f"% of ensemble at residual ≤ 12.0%: {pct_le_120*100:.1f}%")
    print(f"% of ensemble at residual ≤ 13.0%: {pct_le_130*100:.1f}%")
    print(f"Canonical's percentile in ensemble: {canonical_percentile:.1f}%")
    print(f"VERDICT: {verdict}")

    # Histogram bins (10 bins)
    if residuals:
        rmin, rmax = residuals[0], residuals[-1]
        if rmax > rmin:
            bins = 10
            step = (rmax - rmin) / bins
            edges = [rmin + i * step for i in range(bins + 1)]
            counts = [0] * bins
            for r in residuals:
                idx = min(int((r - rmin) / step), bins - 1)
                counts[idx] += 1
            histogram = {"edges": edges, "counts": counts}
        else:
            histogram = {"edges": [rmin, rmax], "counts": [len(residuals)]}
    else:
        histogram = {"edges": [], "counts": []}

    # Compress samples for JSON (don't save the full perm of all 100 — store first 5 + summary stats)
    sample_records_full = chain_result["samples"]
    sample_records_compact = [
        {
            "step": s["step"],
            "r2": s["r2"],
            "beta": s["beta"],
            "L": s["L"],
            "residual": s["residual"],
        }
        for s in sample_records_full
    ]
    # Save first 5 full perms for traceability
    first5_full = [
        {"step": s["step"], "perm": s["perm"], "r2": s["r2"], "beta": s["beta"], "L": s["L"], "residual": s["residual"]}
        for s in sample_records_full[:5]
    ]

    out = {
        "id": "H-NEW-690",
        "title": "Causal generative test of the compression-tail law",
        "prereg_sha": prereg_sha,
        "expected_prereg_sha": EXPECTED_PREREG_SHA,
        "prereg_sha_match": prereg_sha == EXPECTED_PREREG_SHA,
        "seed": SEED,
        "date": "2026-04-28",
        "elapsed_seconds": elapsed,
        "locked_params": {
            "n_steps": N_STEPS,
            "n_burn": N_BURN,
            "n_samples": N_SAMPLES,
            "sample_every": SAMPLE_EVERY,
            "K": K,
            "kink": KINK,
            "r2_min": R2_MIN,
            "beta_range": [BETA_LO, BETA_HI],
            "T_MH": T_MH,
        },
        "canonical_check": {
            "r2": r2_c,
            "beta": beta_c,
            "L": L_c,
            "constraint_ok": constraint_ok(r2_c, beta_c),
        },
        "chain": {
            "warmup": chain_result["warmup"],
            "proposals_total": chain_result["proposals_total"],
            "accepts_total": chain_result["accepts_total"],
            "proposals_constraint_ok": chain_result["proposals_constraint_ok"],
            "accepts_constraint_ok": chain_result["accepts_constraint_ok"],
            "n_samples_collected": chain_result["n_samples_collected"],
        },
        "summary": summary,
        "histogram_residuals": histogram,
        "samples_compact": sample_records_compact,
        "first5_full_perms": first5_full,
        "verdict": verdict,
        "bonferroni_k": 3,
        "alpha_bon": 0.0167,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved: {OUT_JSON}")


if __name__ == "__main__":
    main()
