#!/usr/bin/env python3
"""H-NEW-173 — Spectral analysis of M1 residual sequence r_i = D[i, i+1].

Pre-reg: findings/phase-b-hypotheses/h-new-173-residual-spectrum-prereg.md
Seed: 20260419. Bonferroni-2 across {spectrum, ACF}.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
N_PERMS = 10_000

H111_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-173-residual-spectrum-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-173.json"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def power_spectrum(x: np.ndarray) -> np.ndarray:
    """Return |rFFT|^2 for each real bin."""
    F = np.fft.rfft(x)
    return (F.real * F.real + F.imag * F.imag)


def acf_biased(x: np.ndarray, max_lag: int) -> np.ndarray:
    N = len(x)
    xc = x - x.mean()
    denom = (xc * xc).sum()
    if denom == 0.0:
        return np.zeros(max_lag + 1)
    rhos = np.empty(max_lag + 1)
    for lag in range(max_lag + 1):
        rhos[lag] = (xc[: N - lag] * xc[lag:]).sum() / denom
    return rhos


def load_residuals() -> np.ndarray:
    with H111_JSON.open() as f:
        d = json.load(f)
    upper = d["D_matrix_upper_triangular"]
    dmap: dict[tuple[int, int], float] = {}
    for row in upper:
        i, j, v = int(row[0]), int(row[1]), float(row[2])
        dmap[(i, j)] = v
    r = np.array([dmap[(i, i + 1)] for i in range(1, 114)], dtype=float)
    assert len(r) == 113
    return r


def run_spectrum_test(r: np.ndarray, rng: np.random.Generator) -> dict:
    N = len(r)
    obs_power = power_spectrum(r)  # length 57 (floor(113/2)+1)
    k_range = np.arange(2, 57)  # scan 2..56

    # Permutation null: batch all perms
    exceed = np.zeros(len(k_range), dtype=np.int64)
    for _ in range(N_PERMS):
        perm = rng.permutation(r)
        pp = power_spectrum(perm)
        exceed += (pp[k_range] >= obs_power[k_range]).astype(np.int64)

    p_raw = (exceed + 1) / (N_PERMS + 1)
    n_k = len(k_range)
    p_bonf = np.minimum(1.0, p_raw * n_k)
    min_idx = int(np.argmin(p_bonf))
    min_p = float(p_bonf[min_idx])
    min_k = int(k_range[min_idx])

    # Top-3 by raw observed power
    order = np.argsort(-obs_power[k_range])
    top3 = []
    for idx in order[:3]:
        k = int(k_range[idx])
        top3.append({
            "k": k,
            "period_T": float(N / k),
            "power": float(obs_power[k]),
            "p_raw": float(p_raw[idx]),
            "p_bonf": float(p_bonf[idx]),
        })

    return {
        "obs_power_by_k": {int(k): float(obs_power[k]) for k in k_range},
        "p_raw_by_k": {int(k_range[i]): float(p_raw[i]) for i in range(n_k)},
        "p_bonf_by_k": {int(k_range[i]): float(p_bonf[i]) for i in range(n_k)},
        "min_p_bonf": min_p,
        "min_p_k": min_k,
        "top3_peaks": top3,
        "n_bins_scanned": n_k,
        "pass_primary_alpha_0p025": bool(min_p < 0.025),
    }


def run_acf_test(r: np.ndarray, rng: np.random.Generator) -> dict:
    N = len(r)
    max_lag = 30
    obs_rho = acf_biased(r, max_lag)
    lags = np.arange(1, max_lag + 1)

    exceed = np.zeros(max_lag, dtype=np.int64)
    abs_obs = np.abs(obs_rho[1:])
    for _ in range(N_PERMS):
        perm = rng.permutation(r)
        pr = acf_biased(perm, max_lag)
        exceed += (np.abs(pr[1:]) >= abs_obs).astype(np.int64)

    p_raw = (exceed + 1) / (N_PERMS + 1)
    p_bonf = np.minimum(1.0, p_raw * max_lag)
    min_idx = int(np.argmin(p_bonf))
    min_p = float(p_bonf[min_idx])
    min_lag = int(lags[min_idx])

    order = np.argsort(-abs_obs)
    top3 = []
    for idx in order[:3]:
        lg = int(lags[idx])
        top3.append({
            "lag": lg,
            "rho": float(obs_rho[lg]),
            "p_raw": float(p_raw[idx]),
            "p_bonf": float(p_bonf[idx]),
        })

    return {
        "obs_acf_lags_1_to_30": {int(lg): float(obs_rho[lg]) for lg in lags},
        "p_raw_by_lag": {int(lags[i]): float(p_raw[i]) for i in range(max_lag)},
        "p_bonf_by_lag": {int(lags[i]): float(p_bonf[i]) for i in range(max_lag)},
        "min_p_bonf": min_p,
        "min_p_lag": min_lag,
        "top3_lags_by_abs_rho": top3,
        "pass_secondary_alpha_0p025": bool(min_p < 0.025),
    }


def mw5_positive_control() -> dict:
    """Synthetic sinusoid with period 11 (k=113/11≈10.27, expect peak k=10)."""
    rng = np.random.default_rng(SEED + 1)
    N = 113
    i = np.arange(1, N + 1)
    synth = 1.0 + 0.2 * np.sin(2 * np.pi * i / 11) + rng.normal(0, 0.05, N)
    pw = power_spectrum(synth)
    k_range = np.arange(2, 57)
    ranked = k_range[np.argsort(-pw[k_range])]
    return {
        "period_embedded": 11,
        "expected_peak_k_approx": 113 / 11,
        "top5_k_by_power": [int(k) for k in ranked[:5]],
        "top5_powers": [float(pw[k]) for k in ranked[:5]],
        "passes_mw5": bool(ranked[0] in (10, 11)),
    }


def main() -> None:
    prereg_hash = sha256(PREREG)
    print(f"prereg SHA-256: {prereg_hash}", file=sys.stderr)
    print(f"SEED = {SEED}", file=sys.stderr)
    print(f"N_PERMS = {N_PERMS}", file=sys.stderr)

    r = load_residuals()
    rbar = float(r.mean())
    rvar = float(r.var())
    print(f"r stats: N={len(r)}, mean={rbar:.4f}, var={rvar:.6f}, min={r.min():.4f}, max={r.max():.4f}", file=sys.stderr)

    rng_spec = np.random.default_rng(SEED)
    rng_acf = np.random.default_rng(SEED + 2)

    print("Running spectrum permutation test (10k perms)...", file=sys.stderr)
    spec = run_spectrum_test(r, rng_spec)
    print(f"  min p_bonf = {spec['min_p_bonf']:.4f} at k={spec['min_p_k']}", file=sys.stderr)
    print(f"  top3: {spec['top3_peaks']}", file=sys.stderr)

    print("Running ACF permutation test (10k perms)...", file=sys.stderr)
    acf = run_acf_test(r, rng_acf)
    print(f"  min p_bonf = {acf['min_p_bonf']:.4f} at lag={acf['min_p_lag']}", file=sys.stderr)
    print(f"  top3: {acf['top3_lags_by_abs_rho']}", file=sys.stderr)

    print("Running MW-5 positive control...", file=sys.stderr)
    mw5 = mw5_positive_control()
    print(f"  top5 k: {mw5['top5_k_by_power']}, passes={mw5['passes_mw5']}", file=sys.stderr)

    alpha_fam = 0.05
    alpha_per = 0.025
    primary_pass = spec["min_p_bonf"] < alpha_per
    secondary_pass = acf["min_p_bonf"] < alpha_per

    out = {
        "finding_id": "h-new-173",
        "title": "Spectral analysis of M1 residual sequence (Fisher-Rao consecutive-pair distances)",
        "pre_reg_sha256": prereg_hash,
        "seed": SEED,
        "n_perms": N_PERMS,
        "bonferroni": {
            "family_size": 2,
            "alpha_family": alpha_fam,
            "alpha_per_test": alpha_per,
        },
        "residual_stats": {
            "N": len(r),
            "mean": rbar,
            "variance": rvar,
            "min": float(r.min()),
            "max": float(r.max()),
            "sequence": r.tolist(),
        },
        "primary_spectrum": spec,
        "secondary_acf": acf,
        "mw5_positive_control": mw5,
        "verdict": {
            "primary_spectrum_pass": primary_pass,
            "secondary_acf_pass": secondary_pass,
            "any_pass": primary_pass or secondary_pass,
            "both_pass": primary_pass and secondary_pass,
            "mw5_pass": mw5["passes_mw5"],
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"Wrote {OUT_JSON}", file=sys.stderr)
    print(f"VERDICT primary={primary_pass}, secondary={secondary_pass}, mw5={mw5['passes_mw5']}", file=sys.stderr)


if __name__ == "__main__":
    main()
