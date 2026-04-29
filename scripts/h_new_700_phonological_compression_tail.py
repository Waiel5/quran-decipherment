#!/usr/bin/env python3
"""H-NEW-700: Phonological compression-tail — does rhyme-distribution and phoneme-density
follow the same 2-piece-kink-at-s=50 law as H-NEW-660 content-cohesion?

Rhyme axis: per-surah 28-vector of verse-final-letter frequencies (cosine-distance pairwise).
Phoneme axis: per-surah 4-vector of {emphatic, pharyngeal, sibilant, glottal} proportions.

For each consecutive K=15 window, compute mean pairwise cosine distance.
Regress on window-start position s. Compare to H-NEW-660 content result.
"""
import hashlib
import json
import math
import random
import re
import unicodedata
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_NO_TASH = ROOT / "quran-text/quran-no-tashkeel.json"
QURAN_MIN_TASH = ROOT / "quran-text/quran-min-tashkeel.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-700-phonological-compression-tail-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-700.json"
EXPECTED_PREREG_SHA = "63c0008f5e349129f0ec8421144c34a86bda4077221387cdf0b4ade933204b31"

SEED = 20260435
N_PERMS = 10000
K = 15
KINK_GRID = [25, 35, 50, 65, 75]

# 28-letter Arabic basis for rhyme-distribution
ARABIC_LETTERS = [
    "ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر",
    "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف",
    "ق", "ك", "ل", "م", "ن", "ه", "و", "ي",
]
LETTER_INDEX = {ch: i for i, ch in enumerate(ARABIC_LETTERS)}

# Mapping for variant forms → canonical 28-letter basis
VARIANT_MAP = {
    "ى": "ي",  # alif maqsura → ya
    "ة": "ه",  # ta marbuta → ha (verse-final convention)
    "أ": "ا", "إ": "ا", "آ": "ا",  # hamza-bearing alif → alif
    "ؤ": "و",
    "ئ": "ي",
    "ٱ": "ا",  # alif wasla → alif
}

# Diacritic / ornament codepoints to strip
DIACRITICS_RANGES = [
    (0x0610, 0x061A),
    (0x064B, 0x065F),
    (0x0670, 0x0670),
    (0x06D6, 0x06DC),
    (0x06DF, 0x06E4),
    (0x06E7, 0x06E8),
    (0x06EA, 0x06ED),
]
# Tatweel and pause-marks
ORNAMENTS = set("ـۛۖۚۗۘۙۜۥۭۧۤ")


def is_diacritic(cp):
    for lo, hi in DIACRITICS_RANGES:
        if lo <= cp <= hi:
            return True
    return False


def strip_diacritics_and_ornaments(s):
    out = []
    for ch in s:
        if is_diacritic(ord(ch)):
            continue
        if ch in ORNAMENTS:
            continue
        out.append(ch)
    return "".join(out)


def normalize_letter(ch):
    return VARIANT_MAP.get(ch, ch)


def get_final_letter(text):
    """Get the last canonical Arabic letter of a verse text."""
    cleaned = strip_diacritics_and_ornaments(text).strip()
    # Strip trailing whitespace, punctuation, non-Arabic
    while cleaned and not (("ء" <= cleaned[-1] <= "ي") or cleaned[-1] in "ىةؤئٱآأإ"):
        cleaned = cleaned[:-1]
    if not cleaned:
        return None
    last = cleaned[-1]
    last = normalize_letter(last)
    if last in LETTER_INDEX:
        return last
    return None


def count_letters(text):
    """Count canonical Arabic letters per phoneme group + total."""
    cleaned = strip_diacritics_and_ornaments(text)
    emphatic = pharyngeal = sibilant = glottal = total = 0
    for ch in cleaned:
        # Skip non-Arabic-letter codepoints (whitespace, digits, punctuation)
        if not (("ء" <= ch <= "ي") or ch in "ىةؤئٱآأإ"):
            continue
        canonical = normalize_letter(ch)
        # Even hamza U+0621 (ء) is a phoneme — count it for glottal
        total += 1
        # Original ch (not canonical) for some classifications
        if canonical in {"ص", "ض", "ط", "ظ"}:
            emphatic += 1
        if canonical in {"ح", "ع"}:
            pharyngeal += 1
        if canonical in {"س", "ش", "ز", "ص"}:
            sibilant += 1
        if ch == "ء" or canonical == "ه":
            glottal += 1
        # Hamza-bearing alif (أ إ آ) and standalone hamza ء also count for glottal
        if ch in {"أ", "إ", "آ", "ؤ", "ئ"}:
            glottal += 1
    return emphatic, pharyngeal, sibilant, glottal, total


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def cosine_distance(u, v):
    """Cosine distance = 1 - cosine similarity."""
    du = sum(x * x for x in u) ** 0.5
    dv = sum(x * x for x in v) ** 0.5
    if du < 1e-15 or dv < 1e-15:
        return 1.0
    sim = sum(u[i] * v[i] for i in range(len(u))) / (du * dv)
    sim = max(-1.0, min(1.0, sim))
    return 1.0 - sim


def build_distance_matrix(vectors):
    """114-surah cosine distance matrix. vectors[i] for surah i+1 (1-indexed in caller)."""
    n = len(vectors)
    D = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = cosine_distance(vectors[i], vectors[j])
            D[i][j] = d
            D[j][i] = d
    return D


def mean_pairwise(D, indices):
    """Mean pairwise distance over indices (0-indexed)."""
    pairs = list(combinations(indices, 2))
    if not pairs:
        return 0.0
    return sum(D[a][b] for a, b in pairs) / len(pairs)


def fit_linear(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return 0.0, 0.0, 0.0, [my] * n
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * x for x in xs]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0
    return alpha, beta, r2, yhat


def fit_quadratic(xs, ys):
    n = len(xs)
    sx = sum(xs)
    sx2 = sum(x * x for x in xs)
    sx3 = sum(x ** 3 for x in xs)
    sx4 = sum(x ** 4 for x in xs)
    sy = sum(ys)
    sxy = sum(xs[i] * ys[i] for i in range(n))
    sx2y = sum(xs[i] ** 2 * ys[i] for i in range(n))
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
    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0
    return a, bx, c, r2, yhat


def fit_two_piece(xs_orig, ys, kink):
    """y = a + b * max(0, x - kink). xs_orig = original (uncentered) starts."""
    n = len(xs_orig)
    feat = [max(0.0, x - kink) for x in xs_orig]
    mx = sum(feat) / n
    my = sum(ys) / n
    num = sum((feat[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((feat[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return None, None, 0.0, [my] * n
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * f for f in feat]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0
    return alpha, beta, r2, yhat


def adj_r2(r2, n, p):
    if n - p - 1 <= 0:
        return r2
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def best_two_piece_over_grid(xs_orig, ys, grid):
    best = None
    best_r2 = -1.0
    for kink in grid:
        out = fit_two_piece(xs_orig, ys, kink)
        if out[2] > best_r2:
            best_r2 = out[2]
            best = (kink, *out)
    return best  # (kink, alpha, beta, r2, yhat)


def fit_all_models(starts, d_obs):
    s_centered = [s - 50.5 for s in starts]
    a_lin, b_lin, r2_lin, _ = fit_linear(s_centered, d_obs)
    q = fit_quadratic(s_centered, d_obs)
    a_q, b_q, c_q, r2_q, _ = q
    bp = best_two_piece_over_grid(starts, d_obs, KINK_GRID)
    kink, a_tp, b_tp, r2_tp, _ = bp
    return {
        "linear": {"alpha": a_lin, "beta": b_lin, "r2": r2_lin, "adj_r2": adj_r2(r2_lin, len(d_obs), 1)},
        "quadratic": {"alpha": a_q, "beta": b_q, "gamma": c_q, "r2": r2_q, "adj_r2": adj_r2(r2_q, len(d_obs), 2)},
        "two_piece": {"kink": kink, "alpha": a_tp, "beta": b_tp, "r2": r2_tp, "adj_r2": adj_r2(r2_tp, len(d_obs), 1)},
    }


def pick_primary(models):
    candidates = [
        ("linear", models["linear"]["r2"], models["linear"]["adj_r2"]),
        ("quadratic", models["quadratic"]["r2"], models["quadratic"]["adj_r2"]),
        (f"two-piece-kink-{models['two_piece']['kink']}", models["two_piece"]["r2"], models["two_piece"]["adj_r2"]),
    ]
    return max(candidates, key=lambda t: t[2])


def run_axis(name, vectors, starts):
    """Run full analysis for one axis. Returns dict of results."""
    print(f"\n=== AXIS: {name} ===")
    D = build_distance_matrix(vectors)
    d_obs = []
    for s in starts:
        sub = list(range(s - 1, s - 1 + K))  # 0-indexed
        d_obs.append(mean_pairwise(D, sub))

    print(f"  d̄ range: {min(d_obs):.4f} (best) to {max(d_obs):.4f} (worst)")
    best_idx = d_obs.index(min(d_obs))
    worst_idx = d_obs.index(max(d_obs))
    print(f"  Best window: starts at s={starts[best_idx]}, covers Q {starts[best_idx]}-{starts[best_idx]+K-1}, d̄={d_obs[best_idx]:.4f}")
    print(f"  Worst window: starts at s={starts[worst_idx]}, covers Q {starts[worst_idx]}-{starts[worst_idx]+K-1}, d̄={d_obs[worst_idx]:.4f}")

    models = fit_all_models(starts, d_obs)
    primary = pick_primary(models)
    print(f"  Linear:   R²={models['linear']['r2']:.4f}, adjR²={models['linear']['adj_r2']:.4f}, β={models['linear']['beta']:+.5f}")
    print(f"  Quadratic: R²={models['quadratic']['r2']:.4f}, adjR²={models['quadratic']['adj_r2']:.4f}")
    print(f"  Two-piece (kink={models['two_piece']['kink']}): R²={models['two_piece']['r2']:.4f}, adjR²={models['two_piece']['adj_r2']:.4f}, β={models['two_piece']['beta']:+.5f}")
    print(f"  PRIMARY: {primary[0]}, R²={primary[1]:.4f}, adjR²={primary[2]:.4f}")

    return {
        "axis": name,
        "d_observed": d_obs,
        "best_window": {"start": starts[best_idx], "d_bar": d_obs[best_idx]},
        "worst_window": {"start": starts[worst_idx], "d_bar": d_obs[worst_idx]},
        "models": models,
        "primary_model": primary[0],
        "primary_r2": primary[1],
        "primary_adj_r2": primary[2],
        "D": D,
    }


def permute_and_refit(vectors, starts, n_perms, seed):
    """Permute the 114 surahs, recompute d_obs and refit all models. Returns null R² distributions."""
    rng = random.Random(seed)
    n_surahs = len(vectors)
    null_r2_lin = []
    null_r2_q = []
    null_r2_tp = []
    null_beta_lin = []
    null_beta_tp = []
    null_kinks_tp = []
    s_centered = [s - 50.5 for s in starts]

    # Pre-compute D for the canonical order; permutation is over indices into the surah set
    # Actually: we need to permute the ASSIGNMENT of surahs to mushaf positions. So:
    # build D once on original vectors, then for each perm shuffle which-surah-goes-to-which-position.
    D = build_distance_matrix(vectors)

    for _ in range(n_perms):
        perm = list(range(n_surahs))
        rng.shuffle(perm)
        d_perm = []
        for s in starts:
            sub = [perm[s - 1 + i] for i in range(K)]
            d_perm.append(mean_pairwise(D, sub))
        # Linear
        _, b_lin_n, r2_lin_n, _ = fit_linear(s_centered, d_perm)
        null_r2_lin.append(r2_lin_n)
        null_beta_lin.append(b_lin_n)
        # Quadratic
        q_n = fit_quadratic(s_centered, d_perm)
        if q_n[3] is not None:
            null_r2_q.append(q_n[3])
        # Two-piece (best-grid kink)
        bp_n = best_two_piece_over_grid(starts, d_perm, KINK_GRID)
        null_r2_tp.append(bp_n[3])
        null_beta_tp.append(bp_n[2])
        null_kinks_tp.append(bp_n[0])

    return {
        "null_r2_lin": null_r2_lin,
        "null_r2_q": null_r2_q,
        "null_r2_tp": null_r2_tp,
        "null_beta_lin": null_beta_lin,
        "null_beta_tp": null_beta_tp,
        "null_kinks_tp": null_kinks_tp,
    }


def empirical_p(observed, null_dist, side="upper"):
    if side == "upper":
        return sum(1 for v in null_dist if v >= observed) / max(1, len(null_dist))
    return sum(1 for v in null_dist if v <= observed) / max(1, len(null_dist))


def verdict_for_axis(axis_results, p_primary, p_lin_beta, kink_used):
    r2 = axis_results["primary_r2"]
    beta_lin = axis_results["models"]["linear"]["beta"]
    alpha_bon = 0.05 / 3
    # PASS-EXTENDS-LAW
    extends = (r2 >= 0.50 and p_primary <= alpha_bon and beta_lin < 0 and 40 <= kink_used <= 60)
    directional = (r2 >= 0.30 and p_primary <= 0.05 and beta_lin < 0)
    content_invariance = (r2 < 0.30)
    if extends:
        return f"PASS-EXTENDS-LAW (R²={r2:.4f}, p={p_primary:.5f}, β_lin={beta_lin:+.5f}, kink={kink_used})"
    elif directional:
        return f"DIRECTIONAL-EXTENDS (R²={r2:.4f}, p={p_primary:.5f}, β_lin={beta_lin:+.5f})"
    elif content_invariance:
        return f"PASS-CONFIRMS-CONTENT-INVARIANCE (R²={r2:.4f}, gradient is content-axis-specific)"
    else:
        return f"INTERMEDIATE (R²={r2:.4f}, p={p_primary:.5f}, β_lin={beta_lin:+.5f})"


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-700 (Phonological compression-tail) ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Expected:    {EXPECTED_PREREG_SHA}")
    if prereg_sha != EXPECTED_PREREG_SHA:
        print(f"!!! WARNING: prereg SHA mismatch — recompute and update EXPECTED_PREREG_SHA")
    print(f"Seed: {SEED}\nK: {K}\nKink grid: {KINK_GRID}\n")

    # Load Quran texts
    with open(QURAN_NO_TASH) as f:
        quran_no = json.load(f)
    with open(QURAN_MIN_TASH) as f:
        quran_min = json.load(f)

    # Build per-surah feature vectors
    rhyme_vectors = []  # 114 × 28
    phoneme_vectors = []  # 114 × 4
    rhyme_letter_diagnostics = []  # for top-rhyme-letter per surah
    final_letters_per_surah = []  # list of lists of last-letter chars per verse, per surah

    for s_idx in range(114):
        sn = quran_min[s_idx]
        sn_no = quran_no[s_idx]
        assert sn["id"] == s_idx + 1
        # Rhyme: from min-tashkeel, final letter of each verse
        finals = []
        for v in sn["verses"]:
            ch = get_final_letter(v["text"])
            if ch is not None:
                finals.append(ch)
        final_letters_per_surah.append(finals)
        # Build 28-vector
        vec_r = [0] * 28
        for ch in finals:
            vec_r[LETTER_INDEX[ch]] += 1
        n_finals = sum(vec_r)
        if n_finals > 0:
            vec_r_norm = [v / n_finals for v in vec_r]
        else:
            vec_r_norm = [0.0] * 28
        rhyme_vectors.append(vec_r_norm)
        # Top rhyme-letter
        if n_finals > 0:
            top_idx = max(range(28), key=lambda i: vec_r[i])
            rhyme_letter_diagnostics.append({"surah": s_idx + 1, "top_letter": ARABIC_LETTERS[top_idx], "frac": vec_r[top_idx] / n_finals, "n_verses": n_finals})
        else:
            rhyme_letter_diagnostics.append({"surah": s_idx + 1, "top_letter": None, "frac": 0.0, "n_verses": 0})

        # Phoneme: from no-tashkeel, count letter classes across all verses concatenated
        all_text = " ".join(v["text"] for v in sn_no["verses"])
        emph, phar, sib, glot, total = count_letters(all_text)
        if total > 0:
            phoneme_vectors.append([emph / total, phar / total, sib / total, glot / total])
        else:
            phoneme_vectors.append([0.0, 0.0, 0.0, 0.0])

    print(f"Built {len(rhyme_vectors)} rhyme-vectors (28-dim) and {len(phoneme_vectors)} phoneme-vectors (4-dim).")
    # Diagnostic — top rhyme-letters for first/last 5 surahs
    print("\nTop rhyme-letter diagnostics (first 5 + last 5 surahs):")
    for d in rhyme_letter_diagnostics[:5] + rhyme_letter_diagnostics[-5:]:
        print(f"  Surah {d['surah']:3d}: top='{d['top_letter']}' frac={d['frac']:.3f} (n_verses={d['n_verses']})")

    starts = list(range(1, 101))  # 100 windows of K=15 starting at 1..100

    # --- AXIS 1: RHYME ---
    rhyme_results = run_axis("RHYME", rhyme_vectors, starts)

    # --- AXIS 2: PHONEME ---
    phoneme_results = run_axis("PHONEME", phoneme_vectors, starts)

    # --- PERMUTATION NULL ---
    print(f"\n=== Permutation null ({N_PERMS} perms) ===")
    print("RHYME axis...")
    rhyme_null = permute_and_refit(rhyme_vectors, starts, N_PERMS, SEED)
    print("PHONEME axis...")
    phoneme_null = permute_and_refit(phoneme_vectors, starts, N_PERMS + 1, SEED + 1)

    # Empirical p-values
    def axis_p_values(results, null):
        models = results["models"]
        return {
            "linear": {
                "p_r2": empirical_p(models["linear"]["r2"], null["null_r2_lin"]),
                "p_beta": empirical_p(models["linear"]["beta"], null["null_beta_lin"], side="lower"),
            },
            "quadratic": {
                "p_r2": empirical_p(models["quadratic"]["r2"], null["null_r2_q"]),
            },
            "two_piece": {
                "p_r2": empirical_p(models["two_piece"]["r2"], null["null_r2_tp"]),
                "p_beta": empirical_p(models["two_piece"]["beta"], null["null_beta_tp"], side="lower"),
                "kink": models["two_piece"]["kink"],
            },
        }

    rhyme_pvals = axis_p_values(rhyme_results, rhyme_null)
    phoneme_pvals = axis_p_values(phoneme_results, phoneme_null)

    print("\nRHYME axis p-values:")
    print(f"  Linear:    R²={rhyme_results['models']['linear']['r2']:.4f}, p_R²={rhyme_pvals['linear']['p_r2']:.5f}, p_β={rhyme_pvals['linear']['p_beta']:.5f}")
    print(f"  Quadratic: R²={rhyme_results['models']['quadratic']['r2']:.4f}, p_R²={rhyme_pvals['quadratic']['p_r2']:.5f}")
    print(f"  Two-piece (kink={rhyme_pvals['two_piece']['kink']}): R²={rhyme_results['models']['two_piece']['r2']:.4f}, p_R²={rhyme_pvals['two_piece']['p_r2']:.5f}")

    print("\nPHONEME axis p-values:")
    print(f"  Linear:    R²={phoneme_results['models']['linear']['r2']:.4f}, p_R²={phoneme_pvals['linear']['p_r2']:.5f}, p_β={phoneme_pvals['linear']['p_beta']:.5f}")
    print(f"  Quadratic: R²={phoneme_results['models']['quadratic']['r2']:.4f}, p_R²={phoneme_pvals['quadratic']['p_r2']:.5f}")
    print(f"  Two-piece (kink={phoneme_pvals['two_piece']['kink']}): R²={phoneme_results['models']['two_piece']['r2']:.4f}, p_R²={phoneme_pvals['two_piece']['p_r2']:.5f}")

    # --- VERDICTS ---
    def primary_p(results, pvals):
        m = results["primary_model"]
        if m == "linear":
            return pvals["linear"]["p_r2"]
        if m == "quadratic":
            return pvals["quadratic"]["p_r2"]
        return pvals["two_piece"]["p_r2"]

    rhyme_p_primary = primary_p(rhyme_results, rhyme_pvals)
    phoneme_p_primary = primary_p(phoneme_results, phoneme_pvals)
    rhyme_kink = rhyme_results["models"]["two_piece"]["kink"]
    phoneme_kink = phoneme_results["models"]["two_piece"]["kink"]

    rhyme_verdict = verdict_for_axis(rhyme_results, rhyme_p_primary, rhyme_pvals["linear"]["p_beta"], rhyme_kink)
    phoneme_verdict = verdict_for_axis(phoneme_results, phoneme_p_primary, phoneme_pvals["linear"]["p_beta"], phoneme_kink)

    print(f"\n=== AXIS VERDICTS ===")
    print(f"RHYME:   {rhyme_verdict}")
    print(f"PHONEME: {phoneme_verdict}")

    # Combined verdict
    if "PASS-EXTENDS-LAW" in rhyme_verdict and "PASS-EXTENDS-LAW" in phoneme_verdict:
        combined = "UNIVERSAL-LAW (compression-tail extends to BOTH rhyme and phoneme axes)"
    elif "CONTENT-INVARIANCE" in rhyme_verdict and "CONTENT-INVARIANCE" in phoneme_verdict:
        combined = "CONTENT-SPECIFIC (compression-tail does NOT extend to phonological axes)"
    elif "PASS-EXTENDS-LAW" in rhyme_verdict or "DIRECTIONAL-EXTENDS" in rhyme_verdict:
        if "CONTENT-INVARIANCE" in phoneme_verdict:
            combined = "RHYME-ONLY-EXTENDS (rhyme follows compression-tail; phoneme is content-invariant)"
        else:
            combined = "MIXED (rhyme extends partially, phoneme intermediate)"
    elif "PASS-EXTENDS-LAW" in phoneme_verdict or "DIRECTIONAL-EXTENDS" in phoneme_verdict:
        combined = "PHONEME-ONLY-EXTENDS (phoneme follows compression-tail; rhyme is content-invariant)"
    else:
        combined = "INTERMEDIATE (neither axis cleanly passes; gradient is partially shared but weak)"

    print(f"\n=== COMBINED VERDICT: {combined} ===")
    print(f"\nVS H-NEW-660 content R²=0.9860 with kink at s=50, slope=-0.01237.")
    print(f"  RHYME R²={rhyme_results['primary_r2']:.4f}, kink={rhyme_kink}, β_lin={rhyme_results['models']['linear']['beta']:+.5f}")
    print(f"  PHONEME R²={phoneme_results['primary_r2']:.4f}, kink={phoneme_kink}, β_lin={phoneme_results['models']['linear']['beta']:+.5f}")

    # Drop the heavy D matrices from JSON output (just keep the 114 diagonal as flat for brevity)
    # but emit a summary that allows downstream re-fits.

    out = {
        "id": "H-NEW-700",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "K": K,
        "kink_grid": KINK_GRID,
        "n_perms": N_PERMS,
        "starts": starts,
        "rhyme": {
            "d_observed": rhyme_results["d_observed"],
            "best_window": rhyme_results["best_window"],
            "worst_window": rhyme_results["worst_window"],
            "models": rhyme_results["models"],
            "p_values": rhyme_pvals,
            "primary_model": rhyme_results["primary_model"],
            "primary_r2": rhyme_results["primary_r2"],
            "primary_adj_r2": rhyme_results["primary_adj_r2"],
            "primary_p": rhyme_p_primary,
            "verdict": rhyme_verdict,
            "rhyme_letter_diagnostics": rhyme_letter_diagnostics,
        },
        "phoneme": {
            "d_observed": phoneme_results["d_observed"],
            "best_window": phoneme_results["best_window"],
            "worst_window": phoneme_results["worst_window"],
            "models": phoneme_results["models"],
            "p_values": phoneme_pvals,
            "primary_model": phoneme_results["primary_model"],
            "primary_r2": phoneme_results["primary_r2"],
            "primary_adj_r2": phoneme_results["primary_adj_r2"],
            "primary_p": phoneme_p_primary,
            "verdict": phoneme_verdict,
            "phoneme_vectors": phoneme_vectors,
        },
        "combined_verdict": combined,
        "comparison_to_h_new_660": {
            "content_r2": 0.9860,
            "content_kink": 50,
            "content_beta": -0.01237,
            "rhyme_r2": rhyme_results["primary_r2"],
            "rhyme_kink": rhyme_kink,
            "rhyme_beta_lin": rhyme_results["models"]["linear"]["beta"],
            "phoneme_r2": phoneme_results["primary_r2"],
            "phoneme_kink": phoneme_kink,
            "phoneme_beta_lin": phoneme_results["models"]["linear"]["beta"],
        },
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
