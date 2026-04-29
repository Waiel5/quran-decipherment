"""H-NEW-164: Fourier spectrum of the 114 verse-count integer sequence.

Pre-reg: findings/phase-b-hypotheses/h-new-164-fourier-verse-count-prereg.md

Method (primary, verse-counts):
  1. Load verse counts [total_verses for each of 114 surahs] via loader.
  2. Mean-detrend; compute DFT via numpy.fft.fft.
  3. Power spectrum P[k] = |F[k]|^2, normalized by sum over k=1..57.
  4. Top-5 peaks; null by 10,000 random permutations; p = fraction with
     max(P_norm) >= observed + 1/(N_perm+1).

Secondary (cumulative sum):
  Same pipeline on cum[i] = sum(x[0:i+1]).

MW-5: synthetic sinusoid check.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime

import numpy as np

sys.path.insert(0, "/Users/grey/Downloads/quran/analysis")
from tools.loader import load_quran  # noqa: E402


SEED = 20260419
N_PERM = 10_000
ALPHA_BON = 0.05
BONFERRONI_K = 1

OUT_JSON = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-164.json"


def power_spectrum(x: np.ndarray) -> np.ndarray:
    """Normalized power spectrum P_norm[k] for k=1..57 (Nyquist).

    Mean-detrends so F[0]=0. Returns length-57 vector summing to 1.
    """
    x = np.asarray(x, dtype=float)
    x = x - x.mean()
    F = np.fft.fft(x)
    # k = 1..57 (Nyquist for N=114 is index 57)
    P = np.abs(F[1:58]) ** 2
    tot = P.sum()
    if tot <= 0:
        return np.zeros_like(P)
    return P / tot


def top_k_peaks(pnorm: np.ndarray, k: int = 5):
    """Return list of (k_index, power_fraction) for top-k peaks."""
    idx = np.argsort(pnorm)[::-1][:k]
    # k_index is 1-based (since we sliced [1:58])
    return [(int(i + 1), float(pnorm[i])) for i in idx]


def permutation_null(x: np.ndarray, n_perm: int, seed: int):
    """Return array of max(P_norm[1..57]) over n_perm random permutations."""
    rng = np.random.default_rng(seed)
    x = np.asarray(x, dtype=float)
    n = x.size
    max_peaks = np.empty(n_perm, dtype=float)
    for i in range(n_perm):
        perm = rng.permutation(x)
        pn = power_spectrum(perm)
        max_peaks[i] = pn.max()
    return max_peaks


def p_value(observed: float, null_dist: np.ndarray) -> float:
    """One-tail p = (# null >= observed + 1) / (N + 1)."""
    n = null_dist.size
    return float((np.sum(null_dist >= observed) + 1) / (n + 1))


def run_sequence(name: str, x: np.ndarray, n_perm: int, seed: int):
    pnorm = power_spectrum(x)
    top5 = top_k_peaks(pnorm, 5)
    obs_max = float(pnorm.max())
    null = permutation_null(x, n_perm, seed)
    p = p_value(obs_max, null)
    null_95 = float(np.percentile(null, 95))
    null_99 = float(np.percentile(null, 99))
    null_max = float(null.max())
    return {
        "name": name,
        "length": int(x.size),
        "sum": float(x.sum()),
        "top5_peaks_k_and_power_fraction": top5,
        "observed_max_peak_power_fraction": obs_max,
        "observed_argmax_k": int(np.argmax(pnorm) + 1),
        "null_percentile_95": null_95,
        "null_percentile_99": null_99,
        "null_max": null_max,
        "p_value": p,
        "alpha_bon": ALPHA_BON,
        "bonferroni_k": BONFERRONI_K,
        "reject_null": bool(p < ALPHA_BON),
        "n_perm": n_perm,
    }


def mw5_sinusoid_check():
    """MW-5: synthetic sinusoid must concentrate power at its own f0."""
    f0 = 7
    n = 114
    x = np.sin(2 * np.pi * np.arange(n) * f0 / n)
    pn = power_spectrum(x)
    return {
        "synthetic_f0": f0,
        "P_norm_at_f0": float(pn[f0 - 1]),  # k=1-based; pn index (f0-1)
        "argmax_k": int(np.argmax(pn) + 1),
        "passes_threshold_0p5": bool(pn[f0 - 1] > 0.5),
    }


def main():
    q = load_quran("no-tashkeel")
    assert len(q) == 114, f"expected 114 surahs, got {len(q)}"
    verse_counts = np.array([s.total_verses for s in q], dtype=float)
    assert int(verse_counts.sum()) == 6236, (
        f"expected sum 6236, got {int(verse_counts.sum())}"
    )
    cumsum = np.cumsum(verse_counts)

    mw5 = mw5_sinusoid_check()
    assert mw5["passes_threshold_0p5"], (
        "MW-5 failed; pipeline bug: synthetic sinusoid did not peak at f0"
    )

    primary = run_sequence(
        "verse_counts", verse_counts, N_PERM, SEED
    )
    secondary = run_sequence(
        "cumsum_verse_counts", cumsum, N_PERM, SEED + 1
    )

    result = {
        "id": "h-new-164",
        "title": "Fourier spectrum of 114 verse-count integer sequence",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "seed": SEED,
        "variant": "no-tashkeel",
        "mw_5": mw5,
        "primary": primary,
        "secondary": secondary,
        "prereg": (
            "findings/phase-b-hypotheses/"
            "h-new-164-fourier-verse-count-prereg.md"
        ),
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w") as fh:
        json.dump(result, fh, indent=2, default=float)

    print(json.dumps(result, indent=2, default=float))


if __name__ == "__main__":
    main()
