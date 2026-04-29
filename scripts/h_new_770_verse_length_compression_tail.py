#!/usr/bin/env python3
"""H-NEW-770: Verse-length compression-tail — does verse-length follow the same 1-D law
as H-NEW-660's content-cohesion (R²=0.986)?

For each surah, compute mean letters/verse and mean words/verse (no-tashkeel).
For each consecutive K=15 window starting at s ∈ {1..100}, compute the within-window
mean of per-surah verse-length. Fit linear, quadratic, and two-piece-kink-grid
{25,35,50,65,75}. Permutation null with 10000 surah-shuffles.

Cross-axis: Pearson r(window-verse-length, window-content-d̄_660).
"""
import hashlib
import json
import math
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_NO_TASHKEEL = ROOT / "quran-text/quran-no-tashkeel.json"
H_NEW_660_OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-660.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-770-verse-length-compression-tail-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-770.json"
SEED = 20260446
N_PERMS = 10000
K = 15
KINK_GRID = [25, 35, 50, 65, 75]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_per_surah_verse_lengths():
    """Return two lists indexed 1..114 (index 0 unused) of per-surah mean letters/verse and words/verse.

    Letters: count of all non-whitespace characters in the no-tashkeel text per verse.
    Words: count of whitespace-split tokens per verse.
    """
    with open(QURAN_NO_TASHKEEL) as f:
        data = json.load(f)
    letters_pv = [None] * 115
    words_pv = [None] * 115
    surah_letter_counts = [None] * 115
    surah_word_counts = [None] * 115
    surah_verse_counts = [None] * 115
    for surah in data:
        sid = surah["id"]
        verses = surah["verses"]
        n_verses = len(verses)
        total_letters = 0
        total_words = 0
        for v in verses:
            txt = v["text"]
            # Words = whitespace-split tokens.
            words = txt.split()
            total_words += len(words)
            # Letters = all non-whitespace chars in the no-tashkeel text.
            letters = sum(1 for ch in txt if not ch.isspace())
            total_letters += letters
        letters_pv[sid] = total_letters / n_verses
        words_pv[sid] = total_words / n_verses
        surah_letter_counts[sid] = total_letters
        surah_word_counts[sid] = total_words
        surah_verse_counts[sid] = n_verses
    return letters_pv, words_pv, surah_letter_counts, surah_word_counts, surah_verse_counts


def fit_linear(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return None, None, 0.0, []
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * x for x in xs]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2, yhat


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
            return None, None, None, 0.0, []
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
    return a, bx, c, r2, yhat


def fit_two_piece(xs, ys, kink):
    n = len(xs)
    feat = [max(0, x - kink) for x in xs]
    mx, my = sum(feat) / n, sum(ys) / n
    num = sum((feat[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((feat[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return None, None, 0.0, []
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * f for f in feat]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2, yhat


def adj_r2(r2, n, p):
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if dx < 1e-15 or dy < 1e-15:
        return 0.0
    return num / (dx * dy)


def windowed_means(per_surah_vec, starts, K):
    """For each start s, take per_surah_vec[s..s+K-1] (1-indexed) and return mean."""
    out = []
    for s in starts:
        window_vals = [per_surah_vec[s + i] for i in range(K)]
        out.append(sum(window_vals) / len(window_vals))
    return out


def fit_all_three(starts, ys):
    """Return dict of three model fits + chosen primary by adj-R²."""
    s_center = [s - 50.5 for s in starts]
    a_lin, b_lin, r2_lin, _ = fit_linear(s_center, ys)
    q = fit_quadratic(s_center, ys)
    a_q, b_q, c_q, r2_q, _ = q

    best_kink = None
    best_r2_tp = -1
    best_a_tp = None
    best_b_tp = None
    for kink in KINK_GRID:
        a_tp, b_tp, r2_tp, _ = fit_two_piece(starts, ys, kink)
        if r2_tp > best_r2_tp:
            best_r2_tp = r2_tp
            best_kink = kink
            best_a_tp = a_tp
            best_b_tp = b_tp

    n = len(starts)
    fits = {
        "linear": {"alpha": a_lin, "beta": b_lin, "r2": r2_lin, "adj_r2": adj_r2(r2_lin, n, 1)},
        "quadratic": {"alpha": a_q, "beta": b_q, "gamma": c_q, "r2": r2_q, "adj_r2": adj_r2(r2_q, n, 2)},
        "two_piece": {"kink": best_kink, "alpha": best_a_tp, "beta": best_b_tp, "r2": best_r2_tp, "adj_r2": adj_r2(best_r2_tp, n, 1)},
    }
    primary_choices = [
        ("linear", fits["linear"]["r2"], fits["linear"]["adj_r2"]),
        ("quadratic", fits["quadratic"]["r2"], fits["quadratic"]["adj_r2"]),
        ("two_piece", fits["two_piece"]["r2"], fits["two_piece"]["adj_r2"]),
    ]
    primary = max(primary_choices, key=lambda t: t[2])
    fits["primary_model"] = primary[0]
    fits["primary_r2"] = primary[1]
    fits["primary_adj_r2"] = primary[2]
    fits["best_kink"] = best_kink
    return fits, b_lin


def run_metric(label, per_surah, starts, content_d, alpha_bon):
    print(f"\n========== METRIC: {label} ==========")
    print(f"  per-surah head (s=1..5): {[round(per_surah[i], 2) for i in range(1, 6)]}")
    print(f"  per-surah tail (s=110..114): {[round(per_surah[i], 2) for i in range(110, 115)]}")
    obs = windowed_means(per_surah, starts, K)
    print(f"  window range: {min(obs):.3f} (min) to {max(obs):.3f} (max)")
    fits, b_lin = fit_all_three(starts, obs)
    print(f"  Linear:    α={fits['linear']['alpha']:.3f}, β={fits['linear']['beta']:+.4f}, R²={fits['linear']['r2']:.4f}")
    print(f"  Quadratic: α={fits['quadratic']['alpha']:.3f}, β={fits['quadratic']['beta']:+.4f}, γ={fits['quadratic']['gamma']:+.5f}, R²={fits['quadratic']['r2']:.4f}")
    print(f"  Two-piece: kink={fits['best_kink']}, α={fits['two_piece']['alpha']:.3f}, β={fits['two_piece']['beta']:+.4f}, R²={fits['two_piece']['r2']:.4f}")
    print(f"  PRIMARY: {fits['primary_model']}, R²={fits['primary_r2']:.4f}, adjR²={fits['primary_adj_r2']:.4f}")

    # Permutation null
    rng = random.Random(SEED)
    null_r2 = {"linear": [], "quadratic": [], "two_piece": []}
    for _ in range(N_PERMS):
        perm = list(range(1, 115))
        rng.shuffle(perm)
        # Permuted per-surah vector: position p maps to original surah perm[p-1]
        permuted = [None] * 115
        for p in range(1, 115):
            permuted[p] = per_surah[perm[p - 1]]
        obs_perm = windowed_means(permuted, starts, K)
        s_center = [s - 50.5 for s in starts]
        _, _, r2_lin_n, _ = fit_linear(s_center, obs_perm)
        q_n = fit_quadratic(s_center, obs_perm)
        r2_q_n = q_n[3] if q_n[1] is not None else 0.0
        # Two-piece: best over grid
        best_tp = -1
        for kink in KINK_GRID:
            _, _, r2_tp_n, _ = fit_two_piece(starts, obs_perm, kink)
            if r2_tp_n > best_tp:
                best_tp = r2_tp_n
        null_r2["linear"].append(r2_lin_n)
        null_r2["quadratic"].append(r2_q_n)
        null_r2["two_piece"].append(best_tp)

    p_lin = sum(1 for r in null_r2["linear"] if r >= fits["linear"]["r2"]) / N_PERMS
    p_q = sum(1 for r in null_r2["quadratic"] if r >= fits["quadratic"]["r2"]) / N_PERMS
    p_tp = sum(1 for r in null_r2["two_piece"] if r >= fits["two_piece"]["r2"]) / N_PERMS
    print(f"  Perm p (linear R²): {p_lin:.5f}")
    print(f"  Perm p (quadratic R²): {p_q:.5f}")
    print(f"  Perm p (two-piece R², best-kink-in-grid): {p_tp:.5f}")
    fits["linear"]["perm_p_r2"] = p_lin
    fits["quadratic"]["perm_p_r2"] = p_q
    fits["two_piece"]["perm_p_r2"] = p_tp

    p_primary = {"linear": p_lin, "quadratic": p_q, "two_piece": p_tp}[fits["primary_model"]]
    fits["primary_perm_p"] = p_primary

    # Verdict
    strict = fits["primary_r2"] >= 0.50 and p_primary <= alpha_bon and b_lin < 0
    directional = fits["primary_r2"] >= 0.30 and p_primary <= 0.05 and b_lin < 0
    if strict:
        verdict = f"STRICT PASS — primary={fits['primary_model']}, R²={fits['primary_r2']:.4f}, β_lin={b_lin:+.5f}, p={p_primary:.5f}"
    elif directional:
        verdict = f"DIRECTIONAL — primary={fits['primary_model']}, R²={fits['primary_r2']:.4f}, β_lin={b_lin:+.5f}, p={p_primary:.5f}"
    else:
        verdict = f"NULL — primary={fits['primary_model']}, R²={fits['primary_r2']:.4f}, β_lin={b_lin:+.5f}, p={p_primary:.5f}"
    print(f"  VERDICT: {verdict}")
    fits["verdict"] = verdict

    # Pearson r against H-NEW-660 content-d̄
    r = pearson(obs, content_d)
    print(f"  Pearson r(window-{label}, window-content-d̄_660) = {r:+.4f}")
    fits["pearson_r_vs_content_d"] = r
    fits["window_obs"] = obs
    fits["null_r2_summary"] = {
        "linear_mean": sum(null_r2["linear"]) / N_PERMS,
        "quadratic_mean": sum(null_r2["quadratic"]) / N_PERMS,
        "two_piece_mean": sum(null_r2["two_piece"]) / N_PERMS,
        "linear_p99": sorted(null_r2["linear"])[int(0.99 * N_PERMS)],
        "two_piece_p99": sorted(null_r2["two_piece"])[int(0.99 * N_PERMS)],
    }
    return fits, b_lin


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-770 (Verse-length compression-tail) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\n")

    letters_pv, words_pv, sl, sw, sv = load_per_surah_verse_lengths()
    print(f"Loaded {sum(1 for x in letters_pv if x is not None)} surahs.")
    print(f"  Total letters across mushaf: {sum(x for x in sl if x is not None)}")
    print(f"  Total words across mushaf: {sum(x for x in sw if x is not None)}")
    print(f"  Total verses across mushaf: {sum(x for x in sv if x is not None)}")
    print(f"  Q1 letters/verse: {letters_pv[1]:.2f}, words/verse: {words_pv[1]:.2f}")
    print(f"  Q2 letters/verse: {letters_pv[2]:.2f}, words/verse: {words_pv[2]:.2f}")
    print(f"  Q108 letters/verse: {letters_pv[108]:.2f}, words/verse: {words_pv[108]:.2f}")
    print(f"  Q114 letters/verse: {letters_pv[114]:.2f}, words/verse: {words_pv[114]:.2f}")

    # Load H-NEW-660 content-d̄ for cross-correlation
    with open(H_NEW_660_OUT) as f:
        d660 = json.load(f)
    content_d = d660["d_observed"]
    starts = d660["starts"]
    assert starts == list(range(1, 101)), "Starts must match H-NEW-660 windowing."

    alpha_bon = 0.05 / 6  # 6 tests = 3 models × 2 metrics

    fits_letters, b_lin_letters = run_metric("letters_per_verse", letters_pv, starts, content_d, alpha_bon)
    fits_words, b_lin_words = run_metric("words_per_verse", words_pv, starts, content_d, alpha_bon)

    out = {
        "id": "H-NEW-770",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "K": K,
        "kink_grid": KINK_GRID,
        "alpha_bon": alpha_bon,
        "starts": starts,
        "per_surah_letters_per_verse": [letters_pv[i] for i in range(115)],
        "per_surah_words_per_verse": [words_pv[i] for i in range(115)],
        "metric_letters_per_verse": fits_letters,
        "metric_words_per_verse": fits_words,
        "h_new_660_d_observed": content_d,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")
    print(f"\n=== SUMMARY ===")
    print(f"  letters/verse PRIMARY: {fits_letters['primary_model']}, R²={fits_letters['primary_r2']:.4f}, p={fits_letters['primary_perm_p']:.5f}")
    print(f"  words/verse  PRIMARY: {fits_words['primary_model']}, R²={fits_words['primary_r2']:.4f}, p={fits_words['primary_perm_p']:.5f}")
    print(f"  Pearson r letters vs content-d̄: {fits_letters['pearson_r_vs_content_d']:+.4f}")
    print(f"  Pearson r words   vs content-d̄: {fits_words['pearson_r_vs_content_d']:+.4f}")
    print(f"  α_bon (6 tests) = {alpha_bon:.5f}")


if __name__ == "__main__":
    main()
