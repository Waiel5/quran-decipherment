"""H-NEW-43: Corpus-Wide Verse-Length FFT.

Pre-reg: findings/phase-b-hypotheses/h-new-43-verse-length-fft-prereg.md
Rules tuple: (no-tashkeel, orthographic-token, graphemes,
              basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)

Procedure:
  1. Build L: 6,236 verse-lengths (graphemes) in canonical mushaf order.
  2. Subtract per-surah mean (demean each surah-block independently).
  3. Periodogram; retain k in [55, N/2].
  4. Fit AR(1) to L; 10,000 AR(1) surrogates; amplitude null per k.
  5. Top-10 peaks; z-score and one-sided p under AR(1).
  6. Test directed frequencies 1/21, 1/34, 1/57, 1/7, 1/14 with search windows.
  7. Same pipeline on Bukhari / Jahiz / Muallaqat sentence-length sequences
     truncated/padded to 6,236 points.
  8. MW-5 positive-control: inject sinusoid f0=0.01, amp=0.2 sigma.

Seed 20260415. alpha_cell = 1.28e-3 (inner, 13 tests).
"""

from __future__ import annotations

import json
import os
import re
import sys
from typing import Dict, List, Tuple

import numpy as np

sys.path.insert(0, "/Users/grey/Downloads/quran")
from analysis.tools.loader import load_quran
from analysis.tools.tokenize import graphemes, LETTER_RANGES

SEED = 20260415
N_TARGET = 6236
N_SURROGATES = 10_000
K_MIN = 55
ALPHA_CELL = 1.28e-3  # inner (3 directed + 10 undirected)
ALPHA_BON = 0.0167

OUT_JSON = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-43.json"
OUT_PERIODOGRAM = (
    "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-43-periodogram.csv"
)

LETTER_SET = set()
for lo, hi in LETTER_RANGES:
    for cp in range(lo, hi + 1):
        LETTER_SET.add(chr(cp))


def count_graphemes_in_string(s: str) -> int:
    return sum(1 for ch in s if ch in LETTER_SET)


# ---------------------------------------------------------------------------
# Signal construction
# ---------------------------------------------------------------------------


def build_quran_lengths() -> Tuple[np.ndarray, np.ndarray]:
    """Return (lengths_raw, surah_ids) of length 6,236."""
    surahs = load_quran("no-tashkeel")
    lengths: List[int] = []
    surah_ids: List[int] = []
    for s in surahs:
        for v in s.verses:
            lengths.append(graphemes(v.text))
            surah_ids.append(s.id)
    L = np.array(lengths, dtype=float)
    S = np.array(surah_ids, dtype=int)
    assert L.size == N_TARGET, f"got {L.size}, expected {N_TARGET}"
    return L, S


def demean_per_surah(L: np.ndarray, S: np.ndarray) -> np.ndarray:
    out = L.copy()
    for sid in np.unique(S):
        mask = S == sid
        out[mask] = out[mask] - out[mask].mean()
    return out


# ---------------------------------------------------------------------------
# Baseline corpora: sentence-length sequences
# ---------------------------------------------------------------------------

BUKHARI_PATH = "/Users/grey/Downloads/quran/data/baseline-corpora/raw/bukhari.txt"
JAHIZ_PATH = "/Users/grey/Downloads/quran/data/baseline-corpora/raw/jahiz-hayawan.txt"
MUALLAQA_PATHS = [
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-imru-al-qais.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-tarafa.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-zuhayr.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-labid.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-antara.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-amr-bin-kulthum.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-harith.txt",
]

# Arabic sentence boundaries.
SENT_SPLIT_RE = re.compile(r"[\.؟!\?\n]+")


def split_sentences(text: str) -> List[str]:
    # remove lines starting with section-markers like "# "
    cleaned_lines = []
    for ln in text.splitlines():
        stripped = ln.strip()
        if not stripped:
            continue
        # drop markdown-like headings and bracketed citation numbers that are
        # purely structural (e.g. "[1119]") from Bukhari, and title lines
        if stripped.startswith("#"):
            continue
        cleaned_lines.append(ln)
    joined = "\n".join(cleaned_lines)
    # split on punctuation and newlines
    parts = SENT_SPLIT_RE.split(joined)
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        g = count_graphemes_in_string(p)
        if g >= 3:  # drop near-empty fragments
            out.append(g)
    return out


def load_baseline_lengths(path: str) -> List[int]:
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    return split_sentences(text)


def load_muallaqat_verses() -> List[int]:
    """Treat each line (verse) as a unit; concatenate all 7 muallaqat."""
    lengths: List[int] = []
    for p in MUALLAQA_PATHS:
        with open(p, "r", encoding="utf-8") as fh:
            for ln in fh:
                g = count_graphemes_in_string(ln)
                if g >= 3:
                    lengths.append(g)
    return lengths


def to_length_6236(seq: List[int]) -> Tuple[np.ndarray, str]:
    """Truncate or zero-pad to 6,236 points."""
    arr = np.array(seq, dtype=float)
    if arr.size >= N_TARGET:
        return arr[:N_TARGET], f"truncated_from_{arr.size}"
    else:
        # pad by repeating the series (preserves spectral character better
        # than zero-padding) then truncate
        reps = int(np.ceil(N_TARGET / arr.size))
        tiled = np.tile(arr, reps)[:N_TARGET]
        return tiled, f"tiled_from_{arr.size}_reps{reps}"


# ---------------------------------------------------------------------------
# Spectral machinery
# ---------------------------------------------------------------------------


def periodogram(x: np.ndarray) -> np.ndarray:
    """Return |FFT(x)|^2 / N, length N//2+1 (one-sided)."""
    X = np.fft.rfft(x)
    return (np.abs(X) ** 2) / x.size


def fit_ar1(x: np.ndarray) -> Tuple[float, float, np.ndarray]:
    """OLS / Yule-Walker-equivalent AR(1) fit: x_t = phi*x_{t-1} + eps.

    Returns (phi, sigma_eps, residuals).
    """
    xm = x - x.mean()
    num = np.sum(xm[1:] * xm[:-1])
    den = np.sum(xm[:-1] ** 2)
    phi = num / den if den > 0 else 0.0
    phi = max(min(phi, 0.999), -0.999)
    resid = xm[1:] - phi * xm[:-1]
    sigma = float(np.std(resid, ddof=1))
    return float(phi), sigma, resid


def ljung_box(resid: np.ndarray, lag: int = 10, n_params: int = 1) -> Tuple[float, float]:
    """Ljung-Box Q statistic and p-value under chi-squared with (lag-n_params) df.

    Q = n(n+2) * sum_{k=1..h} r_k^2 / (n-k)
    H0: residuals are white noise (AR(p) fit adequate).
    """
    n = resid.size
    rm = resid - resid.mean()
    var = np.sum(rm ** 2) / n
    Q = 0.0
    for k in range(1, lag + 1):
        c_k = np.sum(rm[k:] * rm[:-k]) / n
        r_k = c_k / var if var > 0 else 0.0
        Q += (r_k ** 2) / (n - k)
    Q *= n * (n + 2)
    df = lag - n_params
    try:
        from scipy.stats import chi2  # type: ignore
        p = float(chi2.sf(Q, df))
    except Exception:
        # Wilson-Hilferty chi-square survival approximation (adequate for audit)
        from math import exp, sqrt
        def erf(x):
            a1, a2, a3, a4, a5, p_ = (0.254829592, -0.284496736, 1.421413741,
                                      -1.453152027, 1.061405429, 0.3275911)
            sign = 1 if x >= 0 else -1
            xx = abs(x)
            t = 1.0 / (1.0 + p_ * xx)
            y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * exp(-xx * xx)
            return sign * y
        h = 2.0 / (9.0 * df)
        z = ((Q / df) ** (1.0 / 3.0) - (1.0 - h)) / sqrt(h)
        p = 0.5 * (1.0 - erf(z / sqrt(2.0)))
    return float(Q), float(p)


def simulate_ar1(phi: float, sigma: float, n: int, rng: np.random.Generator) -> np.ndarray:
    eps = rng.normal(0.0, sigma, size=n)
    x = np.empty(n)
    x[0] = eps[0] / max(np.sqrt(1 - phi * phi), 1e-9)
    for i in range(1, n):
        x[i] = phi * x[i - 1] + eps[i]
    return x


def ar1_null_distribution(
    phi: float,
    sigma: float,
    n: int,
    k_lo: int,
    k_hi: int,
    n_surrogates: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Return surrogate periodogram matrix of shape (n_surrogates, k_hi-k_lo+1)."""
    n_bins = k_hi - k_lo + 1
    null = np.empty((n_surrogates, n_bins))
    for i in range(n_surrogates):
        surr = simulate_ar1(phi, sigma, n, rng)
        p = periodogram(surr)
        null[i, :] = p[k_lo : k_hi + 1]
    return null


# ---------------------------------------------------------------------------
# Peak detection and significance
# ---------------------------------------------------------------------------


def find_top_peaks(amps: np.ndarray, k_lo: int, K: int = 10) -> List[int]:
    """Return top-K peak indices (in absolute-k terms).

    A peak is a local maximum in the retained range, ranked by amplitude.
    """
    idx_local = []
    n = amps.size
    for i in range(1, n - 1):
        if amps[i] > amps[i - 1] and amps[i] > amps[i + 1]:
            idx_local.append(i)
    if not idx_local:
        idx_local = list(range(n))
    idx_local.sort(key=lambda i: amps[i], reverse=True)
    top = idx_local[:K]
    return [i + k_lo for i in top]


def score_peak(
    amp: float, null_col: np.ndarray
) -> Tuple[float, float]:
    """Return (z, one-sided p) for amp vs null distribution at this bin."""
    mu = null_col.mean()
    sd = null_col.std(ddof=1)
    z = (amp - mu) / sd if sd > 0 else 0.0
    # empirical one-sided p
    p_emp = float(np.mean(null_col >= amp))
    # tail correction for p=0
    if p_emp == 0.0:
        p_emp = 1.0 / (null_col.size + 1)
    return float(z), p_emp


def p_with_search_window(
    amp: float, null_mat: np.ndarray, col_lo: int, col_hi: int
) -> Tuple[float, float, int]:
    """Max-in-window null for directed-frequency search."""
    window_max = null_mat[:, col_lo : col_hi + 1].max(axis=1)
    mu = window_max.mean()
    sd = window_max.std(ddof=1)
    z = (amp - mu) / sd if sd > 0 else 0.0
    p_emp = float(np.mean(window_max >= amp))
    if p_emp == 0.0:
        p_emp = 1.0 / (window_max.size + 1)
    width = col_hi - col_lo + 1
    return float(z), p_emp, width


# ---------------------------------------------------------------------------
# Directed frequencies
# ---------------------------------------------------------------------------


def frequency_to_k(freq: float, n: int) -> int:
    """FFT bin closest to freq (cycles/verse). k/N = freq."""
    return int(round(freq * n))


DIRECTED_FREQS = [
    ("f_sevenths_1/7", 1.0 / 7),
    ("f_sevenths_1/14", 1.0 / 14),
    ("f_fibonacci_1/21", 1.0 / 21),
    ("f_fibonacci_1/34", 1.0 / 34),
    ("f_mushaf_bipartition_1/57", 1.0 / 57),
]


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------


def analyze_signal(
    L_raw: np.ndarray,
    label: str,
    rng: np.random.Generator,
    demean_blocks: np.ndarray = None,
) -> Dict:
    """Full pipeline on a single 6,236-point signal."""
    n = L_raw.size
    if demean_blocks is not None:
        L = demean_per_surah(L_raw, demean_blocks)
    else:
        L = L_raw - L_raw.mean()

    amps_full = periodogram(L)
    k_hi = n // 2
    amps = amps_full[K_MIN : k_hi + 1]
    # absolute-k axis: K_MIN..k_hi

    # AR(1) null
    phi, sigma, resid = fit_ar1(L)
    lb_Q, lb_p = ljung_box(resid, lag=10, n_params=1)
    null_mat = ar1_null_distribution(
        phi, sigma, n, K_MIN, k_hi, N_SURROGATES, rng
    )
    null_mean = null_mat.mean(axis=0)
    null_std = null_mat.std(axis=0, ddof=1)
    null_99 = np.percentile(null_mat, 99, axis=0)

    # Top-10 peaks (undirected)
    top_k_abs = find_top_peaks(amps, K_MIN, K=10)
    top_rows = []
    for k in top_k_abs:
        col = k - K_MIN
        amp = amps[col]
        z, p = score_peak(amp, null_mat[:, col])
        top_rows.append(
            {
                "k": int(k),
                "period_verses": float(n / k),
                "freq_cyc_per_verse": float(k / n),
                "amplitude": float(amp),
                "null_mean": float(null_mean[col]),
                "null_std": float(null_std[col]),
                "z": float(z),
                "p_one_sided": float(p),
                "significant_at_alpha_cell": bool(p < ALPHA_CELL),
            }
        )

    # Directed-frequency cells with search window
    # Bonferroni across top-10 peaks for undirected in the same family;
    # we use max-of-window null for directed, per pre-reg.
    directed_rows = []
    for name, f0 in DIRECTED_FREQS:
        k0 = frequency_to_k(f0, n)
        # search window: +/- 10% of k0, minimum +/- 3 bins
        halfwidth = max(3, int(round(0.10 * k0)))
        kw_lo = max(K_MIN, k0 - halfwidth)
        kw_hi = min(k_hi, k0 + halfwidth)
        col_lo = kw_lo - K_MIN
        col_hi = kw_hi - K_MIN
        # argmax amplitude in window
        win_amps = amps[col_lo : col_hi + 1]
        local_argmax = int(np.argmax(win_amps))
        k_star = kw_lo + local_argmax
        amp_star = float(win_amps[local_argmax])
        z_w, p_w, width = p_with_search_window(
            amp_star, null_mat, col_lo, col_hi
        )
        directed_rows.append(
            {
                "name": name,
                "target_freq": float(f0),
                "target_k": int(k0),
                "window_k_lo": int(kw_lo),
                "window_k_hi": int(kw_hi),
                "window_width_bins": int(width),
                "k_argmax": int(k_star),
                "period_verses": float(n / k_star),
                "amplitude": amp_star,
                "z_vs_window_max_null": float(z_w),
                "p_window_corrected": float(p_w),
                "significant_at_alpha_cell": bool(p_w < ALPHA_CELL),
            }
        )

    # AR(1) parameters
    return {
        "label": label,
        "N": int(n),
        "k_min": int(K_MIN),
        "k_max": int(k_hi),
        "ar1_phi": float(phi),
        "ar1_sigma_eps": float(sigma),
        "ljung_box_Q_lag10": float(lb_Q),
        "ljung_box_p_lag10": float(lb_p),
        "ljung_box_pass_p_gt_0p05": bool(lb_p > 0.05),
        "signal_mean": float(L_raw.mean()),
        "signal_std": float(L_raw.std(ddof=1)),
        "top10_peaks_undirected": top_rows,
        "directed_frequencies": directed_rows,
        "_null_mat_shape": list(null_mat.shape),
        "_k_min": int(K_MIN),
        "_null_99": null_99.tolist(),
        "_amps": amps.tolist(),
    }


def positive_control(rng: np.random.Generator, phi: float, sigma: float) -> Dict:
    """MW-5 positive control: inject sinusoid at f0=0.01, amp=0.2 sigma_L."""
    n = N_TARGET
    f0 = 0.01
    k0 = frequency_to_k(f0, n)
    noise = simulate_ar1(phi, sigma, n, rng)
    sig_std = noise.std(ddof=1)
    t = np.arange(n)
    signal = 0.2 * sig_std * np.sin(2 * np.pi * f0 * t + rng.uniform(0, 2 * np.pi))
    x = noise + signal
    # Reuse pipeline
    amps_full = periodogram(x)
    k_hi = n // 2
    amps = amps_full[K_MIN : k_hi + 1]
    col = k0 - K_MIN
    # null
    null_col = np.empty(N_SURROGATES)
    for i in range(N_SURROGATES):
        surr = simulate_ar1(phi, sigma, n, rng)
        null_col[i] = periodogram(surr)[k0]
    z, p = score_peak(amps[col], null_col)
    detected = p < ALPHA_CELL
    return {
        "injected_freq": f0,
        "injected_k": int(k0),
        "injected_amp_fraction_of_sigma": 0.2,
        "observed_amplitude": float(amps[col]),
        "null_mean": float(null_col.mean()),
        "null_std": float(null_col.std(ddof=1)),
        "z": float(z),
        "p_one_sided": float(p),
        "alpha_cell": ALPHA_CELL,
        "detected": bool(detected),
        "status": "PASS" if detected else "FAIL_PIPELINE_BROKEN",
    }


def save_periodogram_csv(result: Dict) -> None:
    amps = result["_amps"]
    null_99 = result["_null_99"]
    k_min = result["_k_min"]
    with open(OUT_PERIODOGRAM, "w", encoding="utf-8") as fh:
        fh.write("k,amplitude,null_99th_percentile\n")
        for i, (a, n99) in enumerate(zip(amps, null_99)):
            fh.write(f"{k_min + i},{a},{n99}\n")


def main() -> None:
    rng = np.random.default_rng(SEED)

    print("Building Quran verse-length signal...", flush=True)
    L_quran, S_quran = build_quran_lengths()
    print(
        f"  N={L_quran.size} mean={L_quran.mean():.2f} std={L_quran.std():.2f}",
        flush=True,
    )

    print("Analyzing Quran (primary, per-surah demean, AR(1) null, 10k surr)...", flush=True)
    quran_result = analyze_signal(L_quran, "quran", rng, demean_blocks=S_quran)
    # save periodogram immediately (only for Quran)
    save_periodogram_csv(quran_result)

    print("Loading baselines...", flush=True)
    bukhari_seq = load_baseline_lengths(BUKHARI_PATH)
    jahiz_seq = load_baseline_lengths(JAHIZ_PATH)
    muallaqa_seq = load_muallaqat_verses()
    print(
        f"  bukhari n={len(bukhari_seq)} jahiz n={len(jahiz_seq)} muallaqa n={len(muallaqa_seq)}",
        flush=True,
    )

    bukhari_L, bukhari_note = to_length_6236(bukhari_seq)
    jahiz_L, jahiz_note = to_length_6236(jahiz_seq)
    muallaqa_L, muallaqa_note = to_length_6236(muallaqa_seq)

    print("Analyzing Bukhari...", flush=True)
    # For baselines we do global-mean demean (no natural "surah" block)
    bukhari_result = analyze_signal(bukhari_L, "bukhari", rng)
    print("Analyzing Jahiz...", flush=True)
    jahiz_result = analyze_signal(jahiz_L, "jahiz", rng)
    print("Analyzing Muallaqat...", flush=True)
    muallaqa_result = analyze_signal(muallaqa_L, "muallaqat", rng)

    print("Running MW-5 positive control...", flush=True)
    pos_ctrl = positive_control(
        rng, phi=quran_result["ar1_phi"], sigma=quran_result["ar1_sigma_eps"]
    )
    print(f"  positive control: {pos_ctrl['status']} z={pos_ctrl['z']:.2f}", flush=True)

    # Assemble verdict
    q_top = quran_result["top10_peaks_undirected"]
    q_dir = quran_result["directed_frequencies"]
    sig_directed = [r for r in q_dir if r["significant_at_alpha_cell"]]
    sig_undirected = [r for r in q_top if r["significant_at_alpha_cell"]]

    baseline_max_amps = [
        max(r["amplitude"] for r in bukhari_result["top10_peaks_undirected"]),
        max(r["amplitude"] for r in jahiz_result["top10_peaks_undirected"]),
        max(r["amplitude"] for r in muallaqa_result["top10_peaks_undirected"]),
    ]
    quran_max_amp = max(r["amplitude"] for r in q_top)
    quran_exceeds_baselines = quran_max_amp > max(baseline_max_amps)

    # Verdict logic per pre-reg (with amendment 43-B: Ljung-Box gate)
    ljung_ok = quran_result["ljung_box_pass_p_gt_0p05"]
    if not pos_ctrl["detected"]:
        verdict = "NULL-BROKEN"
        verdict_reason = "positive-control failed"
    elif not ljung_ok:
        verdict = "NULL-BROKEN"
        verdict_reason = (
            f"AR(1) Ljung-Box lag-10 p={quran_result['ljung_box_p_lag10']:.3e} "
            f"<= 0.05; AR(1) null disqualified per amendment 43-B"
        )
    elif len(sig_directed) >= 1:
        verdict = "DIRECTED-PASS"
        verdict_reason = f"{len(sig_directed)} directed hits at alpha_cell=1.28e-3"
    elif len(sig_undirected) >= 3 and quran_exceeds_baselines:
        verdict = "EXPLORATORY-PASS"
        verdict_reason = (
            f"{len(sig_undirected)} undirected peaks at alpha_cell=1.28e-3 "
            f"AND Quran max amp > baseline max"
        )
    else:
        verdict = "NULL"
        verdict_reason = (
            f"{len(sig_directed)} directed / {len(sig_undirected)} undirected "
            f"peaks at alpha_cell=1.28e-3; exceeds_baseline={quran_exceeds_baselines}"
        )

    # Strip internal helper arrays before writing
    for r in [quran_result, bukhari_result, jahiz_result, muallaqa_result]:
        for k in ("_null_99", "_amps", "_null_mat_shape", "_k_min"):
            r.pop(k, None)

    summary = {
        "test_id": "H-NEW-43",
        "seed": SEED,
        "n_surrogates": N_SURROGATES,
        "k_min": K_MIN,
        "alpha_cell_inner": ALPHA_CELL,
        "alpha_bon_outer": ALPHA_BON,
        "rules_tuple": [
            "no-tashkeel",
            "orthographic-token",
            "graphemes",
            "basmala-counted-only-in-surah-1",
            "hafs-kufan",
            "mashriqi",
        ],
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "amendments_applied": [
            "43-A: inner k=13, alpha_cell=1.28e-3 (locked, already in script)",
            "43-B: AR(1) Ljung-Box lag-10 gate; p<=0.05 => NULL-BROKEN",
        ],
        "positive_control": pos_ctrl,
        "quran": quran_result,
        "baselines": {
            "bukhari": {"note": bukhari_note, **bukhari_result},
            "jahiz": {"note": jahiz_note, **jahiz_result},
            "muallaqat": {"note": muallaqa_note, **muallaqa_result},
        },
        "baseline_max_peak_amplitudes": {
            "bukhari": baseline_max_amps[0],
            "jahiz": baseline_max_amps[1],
            "muallaqat": baseline_max_amps[2],
        },
        "quran_max_peak_amplitude": quran_max_amp,
        "quran_exceeds_baseline_max": quran_exceeds_baselines,
        "n_significant_directed": len(sig_directed),
        "n_significant_undirected_top10": len(sig_undirected),
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, ensure_ascii=False)

    print(f"\nVerdict: {verdict}")
    print(f"Significant directed: {len(sig_directed)}")
    print(f"Significant undirected top-10: {len(sig_undirected)}")
    print(f"Quran max amp: {quran_max_amp:.3f}; baselines: {baseline_max_amps}")
    print(f"\nWrote: {OUT_JSON}")
    print(f"Wrote: {OUT_PERIODOGRAM}")


if __name__ == "__main__":
    main()
