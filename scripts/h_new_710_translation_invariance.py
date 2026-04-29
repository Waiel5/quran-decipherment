#!/usr/bin/env python3
"""H-NEW-710: Translation-invariance of compression-tail.

Apply H-NEW-660 protocol to ENGLISH (Sahih International) instead of Arabic FR-roots:
- Top-200 stem cosine distance per surah.
- K=15 windows; linear, quadratic, two-piece (kink-grid {25,35,50,65,75}).
- Permutation null, Bonferroni-3, α_bon = 0.01667.
- Compare English R² to Arabic R²=0.986.

Pre-reg SHA-256 embedded; verified at runtime.
"""

import hashlib
import json
import math
import random
import re
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
TRANSLATION = ROOT / "data/translations/en.sahih.txt-2.txt"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-710-translation-invariance-prereg.md"
PREREG_SHA_EXPECTED = "3cbd690c791a6f38e79ee24ec439a6a51c81451505d326b962639085d83c80a1"
H660_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-660.json"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-710.json"
SEED = 20260436
N_PERMS = 10000
K = 15
TOP_K_VOCAB = 200
KINK_GRID = [25, 35, 50, 65, 75]

STOPWORDS = set("""the a an of in to and or but is are was were be been being have has had do does did will would
can could should may might shall must that this these those who whom whose which what when where why how
with from by at on for as it its he him his she her hers they them their theirs we us our ours you your yours
i me my mine all any some no not so then than also too only just very more most much many indeed yet now into
upon unto""".split())

# Porter-light suffixes — apply LONGEST first; only if remaining stem ≥ 3 chars
SUFFIXES = ["tion", "sion", "ment", "ness", "ity", "ing", "est", "ed", "es", "ly", "er", "s"]
# Sort by length descending for longest-match
SUFFIXES.sort(key=len, reverse=True)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def stem(token):
    """Lowercase + strip non-alpha + Porter-light suffix strip."""
    for suf in SUFFIXES:
        if token.endswith(suf) and len(token) - len(suf) >= 3:
            return token[: -len(suf)]
    return token


def tokenize(text):
    """Strip [bracket] interpolations, lowercase, strip non-alpha, tokenize, stopwords, stem, len ≥ 3."""
    # Strip [...] interpolations (translator's notes/clarifications)
    text = re.sub(r"\[[^\]]*\]", " ", text)
    text = text.lower()
    text = re.sub(r"[^a-z]+", " ", text)
    tokens = text.split()
    out = []
    for t in tokens:
        if t in STOPWORDS:
            continue
        s = stem(t)
        if len(s) < 3:
            continue
        if s in STOPWORDS:
            continue
        out.append(s)
    return out


def load_translation():
    """Return dict surah_num -> list of stems (concatenated across all verses)."""
    surah_tokens = {i: [] for i in range(1, 115)}
    with open(TRANSLATION, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|", 2)
            if len(parts) != 3:
                continue
            try:
                surah = int(parts[0])
            except ValueError:
                continue
            if surah < 1 or surah > 114:
                continue
            text = parts[2]
            surah_tokens[surah].extend(tokenize(text))
    return surah_tokens


def build_top_vocab(surah_tokens, K=TOP_K_VOCAB):
    """Top-K stems by total corpus frequency."""
    total = Counter()
    for s in range(1, 115):
        total.update(surah_tokens[s])
    top = [w for w, _ in total.most_common(K)]
    return top


def vectorize(surah_tokens, vocab):
    """Return dict surah_num -> count vector over vocab."""
    idx = {w: i for i, w in enumerate(vocab)}
    vecs = {}
    for s in range(1, 115):
        v = [0.0] * len(vocab)
        for tok in surah_tokens[s]:
            if tok in idx:
                v[idx[tok]] += 1.0
        vecs[s] = v
    return vecs


def cosine_dist(u, v):
    """1 - cos(u, v). Returns 1.0 if either zero-vector."""
    nu = math.sqrt(sum(x * x for x in u))
    nv = math.sqrt(sum(x * x for x in v))
    if nu == 0 or nv == 0:
        return 1.0
    dot = sum(u[i] * v[i] for i in range(len(u)))
    cos = dot / (nu * nv)
    cos = max(-1.0, min(1.0, cos))
    return 1.0 - cos


def build_distance_matrix(vecs):
    """114x114 cosine-distance matrix; D[i][j] = D[j][i], D[i][i]=0. Indexed 1..114 in mat[1..114][1..114]."""
    D = [[0.0] * 115 for _ in range(115)]
    for i in range(1, 115):
        for j in range(i + 1, 115):
            d = cosine_dist(vecs[i], vecs[j])
            D[i][j] = d
            D[j][i] = d
    return D


def mean_pairwise(D, subset):
    pairs = list(combinations(subset, 2))
    return sum(D[a][b] for a, b in pairs) / len(pairs)


def fit_linear(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return 0.0, 0.0, 0.0, ys[:]
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * x for x in xs]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
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
            return None, None, None, 0, []
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
        return 0.0, 0.0, 0.0, ys[:]
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * f for f in feat]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2, yhat


def adj_r2(r2, n, p):
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def main():
    prereg_sha = sha(PREREG)
    if prereg_sha != PREREG_SHA_EXPECTED:
        raise RuntimeError(f"Pre-reg SHA mismatch! Expected {PREREG_SHA_EXPECTED}, got {prereg_sha}")
    print(f"=== H-NEW-710 (Translation-invariance of compression-tail) ===")
    print(f"Pre-reg SHA: {prereg_sha} (verified)\nSeed: {SEED}\n")

    # Load Arabic baseline R² for comparison
    with open(H660_JSON) as f:
        h660 = json.load(f)
    arabic_r2_lin = h660["linear"]["r2"]
    arabic_r2_q = h660["quadratic"]["r2"]
    arabic_r2_tp = h660["two_piece"]["r2"]
    arabic_kink = h660["two_piece"]["kink"]
    arabic_primary = h660["primary_model"]
    arabic_primary_r2 = h660["primary_r2"]
    print(f"Arabic baseline (H-NEW-660): primary={arabic_primary}, R²={arabic_primary_r2:.4f}")
    print(f"  linear R²={arabic_r2_lin:.4f}, quad R²={arabic_r2_q:.4f}, two-piece(kink={arabic_kink}) R²={arabic_r2_tp:.4f}\n")

    # Load translation
    print(f"Loading {TRANSLATION.name}...")
    surah_tokens = load_translation()
    token_counts = {s: len(surah_tokens[s]) for s in range(1, 115)}
    total_tokens = sum(token_counts.values())
    print(f"  Total stem-tokens after stemming: {total_tokens}")
    print(f"  Tokens per surah: min={min(token_counts.values())} (Q{min(token_counts, key=token_counts.get)}), "
          f"max={max(token_counts.values())} (Q{max(token_counts, key=token_counts.get)}), "
          f"mean={total_tokens/114:.0f}")

    # Build vocab
    vocab = build_top_vocab(surah_tokens, TOP_K_VOCAB)
    print(f"\nTop-{TOP_K_VOCAB} vocab built. Top 20 stems: {vocab[:20]}")

    # Vectorize
    vecs = vectorize(surah_tokens, vocab)

    # Build distance matrix
    print(f"\nComputing 114x114 cosine-distance matrix on top-{TOP_K_VOCAB} stem vectors...")
    D = build_distance_matrix(vecs)

    # Compute K=15 windows
    starts = list(range(1, 101))  # 100 windows
    d_obs = []
    for s in starts:
        sub = list(range(s, s + K))
        d_obs.append(mean_pairwise(D, sub))
    print(f"\nComputed {len(d_obs)} consecutive K={K} windows.")
    best_idx = d_obs.index(min(d_obs))
    worst_idx = d_obs.index(max(d_obs))
    print(f"  d̄ range (English-stem-cosine): {min(d_obs):.4f} (best, s={starts[best_idx]}, "
          f"covers Q{starts[best_idx]}-{starts[best_idx]+K-1}) to "
          f"{max(d_obs):.4f} (worst, s={starts[worst_idx]}, covers Q{starts[worst_idx]}-{starts[worst_idx]+K-1})")
    print(f"  Compression ratio (worst/best): {max(d_obs)/min(d_obs):.2f}x")

    # Center s
    s_center = [s - 50.5 for s in starts]

    # Fit 3 models
    a_lin, b_lin, r2_lin, _ = fit_linear(s_center, d_obs)
    print(f"\n--- LINEAR MODEL (English) ---")
    print(f"  d̄_en = {a_lin:.4f} + ({b_lin:+.5f}) · (s - 50.5)")
    print(f"  R² = {r2_lin:.4f}, adjR² = {adj_r2(r2_lin, len(d_obs), 1):.4f}")

    q = fit_quadratic(s_center, d_obs)
    a_q, b_q, c_q, r2_q, _ = q
    print(f"\n--- QUADRATIC MODEL (English) ---")
    print(f"  d̄_en = {a_q:.4f} + ({b_q:+.5f}) · s + ({c_q:+.6f}) · s²")
    print(f"  R² = {r2_q:.4f}, adjR² = {adj_r2(r2_q, len(d_obs), 2):.4f}")

    # Two-piece kink grid (locked: {25, 35, 50, 65, 75})
    best_kink = None
    best_r2 = -1
    best_two_piece = None
    kink_results = {}
    for kink in KINK_GRID:
        out = fit_two_piece(starts, d_obs, kink)
        kink_results[kink] = {"alpha": out[0], "beta": out[1], "r2": out[2]}
        if out[2] > best_r2:
            best_r2 = out[2]
            best_kink = kink
            best_two_piece = out
    a_tp, b_tp, r2_tp, _ = best_two_piece
    print(f"\n--- TWO-PIECE LINEAR (English; kink-grid {KINK_GRID}, best at s={best_kink}) ---")
    for k in KINK_GRID:
        kr = kink_results[k]
        marker = " ← BEST" if k == best_kink else ""
        print(f"    kink={k}: R²={kr['r2']:.4f}{marker}")
    print(f"  d̄_en = {a_tp:.4f} + ({b_tp:+.5f}) · max(0, s - {best_kink})")
    print(f"  R² = {r2_tp:.4f}, adjR² = {adj_r2(r2_tp, len(d_obs), 1):.4f}")

    # Pick primary by adjusted R²
    primary_choices = [
        ("linear", r2_lin, adj_r2(r2_lin, len(d_obs), 1), a_lin, b_lin, None),
        ("quadratic", r2_q, adj_r2(r2_q, len(d_obs), 2), a_q, b_q, c_q),
        (f"two-piece-kink-{best_kink}", r2_tp, adj_r2(r2_tp, len(d_obs), 1), a_tp, b_tp, None),
    ]
    primary = max(primary_choices, key=lambda t: t[2])
    print(f"\nPRIMARY (highest adj-R²): {primary[0]}, R²={primary[1]:.4f}, adjR²={primary[2]:.4f}")

    # Permutation null
    print(f"\n--- PERMUTATION NULL ({N_PERMS} perms; shuffle 114 surahs) ---")
    rng = random.Random(SEED)
    null_betas_lin = []
    null_r2_lin = []
    null_r2_q = []
    null_r2_tp = []
    for _ in range(N_PERMS):
        perm = list(range(1, 115))
        rng.shuffle(perm)
        d_perm = []
        for s in starts:
            sub = [perm[s - 1 + i] for i in range(K)]
            d_perm.append(mean_pairwise(D, sub))
        _, b_n, r2_n, _ = fit_linear(s_center, d_perm)
        null_betas_lin.append(b_n)
        null_r2_lin.append(r2_n)
        q_n = fit_quadratic(s_center, d_perm)
        if q_n[1] is not None:
            null_r2_q.append(q_n[3])
        tp_n = fit_two_piece(starts, d_perm, best_kink)
        null_r2_tp.append(tp_n[2])

    p_lin_slope = sum(1 for b in null_betas_lin if b <= b_lin) / len(null_betas_lin)
    p_lin_r2 = sum(1 for r in null_r2_lin if r >= r2_lin) / len(null_r2_lin)
    p_q_r2 = sum(1 for r in null_r2_q if r >= r2_q) / len(null_r2_q)
    p_tp_r2 = sum(1 for r in null_r2_tp if r >= r2_tp) / len(null_r2_tp)

    null_mean_lin = sum(null_r2_lin) / len(null_r2_lin)
    null_mean_q = sum(null_r2_q) / len(null_r2_q)
    null_mean_tp = sum(null_r2_tp) / len(null_r2_tp)

    print(f"  Linear β observed = {b_lin:+.5f}; p(β ≤ obs) = {p_lin_slope:.5f}")
    print(f"  Linear R² observed = {r2_lin:.4f} (null mean = {null_mean_lin:.4f}); p(R² ≥ obs) = {p_lin_r2:.5f}")
    print(f"  Quadratic R² observed = {r2_q:.4f} (null mean = {null_mean_q:.4f}); p(R² ≥ obs) = {p_q_r2:.5f}")
    print(f"  Two-piece R² observed = {r2_tp:.4f} (null mean = {null_mean_tp:.4f}); p(R² ≥ obs) = {p_tp_r2:.5f}")

    # Verdicts
    alpha_bon = 0.05 / 3
    p_primary = {
        "linear": p_lin_r2,
        "quadratic": p_q_r2,
        f"two-piece-kink-{best_kink}": p_tp_r2,
    }[primary[0]]

    primary_r2 = primary[1]
    primary_beta = primary[4]  # linear or two-piece beta; for quadratic, this is the b coefficient
    direction_ok = (primary_beta < 0) if primary[0] != "quadratic" else (b_lin < 0)

    # PRE-REG-STANDARD-04 formal pass/fail
    if primary_r2 >= 0.50 and p_primary <= alpha_bon and direction_ok:
        formal_verdict = f"STRICT PASS — translation-invariance confirmed; primary={primary[0]}, R²={primary_r2:.4f}, p={p_primary:.5f}"
    elif primary_r2 >= 0.30 and p_primary <= 0.05 and direction_ok:
        formal_verdict = f"DIRECTIONAL — partial translation-invariance; primary={primary[0]}, R²={primary_r2:.4f}, p={p_primary:.5f}"
    else:
        formal_verdict = f"NULL — translation-invariance not supported; primary={primary[0]}, R²={primary_r2:.4f}, p={p_primary:.5f}"

    # INTERPRETIVE thresholds (locked in pre-reg §7)
    interp_kink_ok = isinstance(best_kink, int) and 40 <= best_kink <= 60
    if primary_r2 >= 0.70 and primary[0].startswith("two-piece") and interp_kink_ok:
        interpretive = "STRONG translation-invariant — compression-tail is STRUCTURAL (deep semantic-architectural law)"
    elif 0.30 <= primary_r2 < 0.70:
        interpretive = "PARTIAL invariance — some content-axis bleed; the law is partly structural, partly Arabic-specific"
    elif primary_r2 < 0.30:
        interpretive = "NULL on translation-invariance — compression-tail is Arabic-syntax-specific (FR-roots-system tied)"
    else:
        # R² ≥ 0.70 but kink not in [40,60] OR primary not two-piece
        interpretive = f"PARTIAL+ — high R² ({primary_r2:.4f}) but interpretive criteria not fully met (primary={primary[0]}, kink={best_kink})"

    print(f"\n=== FORMAL VERDICT: {formal_verdict} ===")
    print(f"=== INTERPRETIVE: {interpretive} ===")
    print(f"  Bonferroni-3 α = {alpha_bon:.5f}")
    print(f"\nArabic primary R²={arabic_primary_r2:.4f} vs English primary R²={primary_r2:.4f}")
    print(f"  R² ratio (English/Arabic): {primary_r2/arabic_primary_r2:.3f}")

    # Match best/worst windows to Arabic
    arabic_d = h660["d_observed"]
    arabic_starts = h660["starts"]
    arabic_best_idx = arabic_d.index(min(arabic_d))
    arabic_worst_idx = arabic_d.index(max(arabic_d))
    print(f"\n--- Best/worst windows comparison ---")
    print(f"  Arabic best: s={arabic_starts[arabic_best_idx]} (Q{arabic_starts[arabic_best_idx]}-{arabic_starts[arabic_best_idx]+K-1}), d̄={arabic_d[arabic_best_idx]:.4f}")
    print(f"  English best: s={starts[best_idx]} (Q{starts[best_idx]}-{starts[best_idx]+K-1}), d̄={d_obs[best_idx]:.4f}")
    print(f"  Arabic worst: s={arabic_starts[arabic_worst_idx]} (Q{arabic_starts[arabic_worst_idx]}-{arabic_starts[arabic_worst_idx]+K-1}), d̄={arabic_d[arabic_worst_idx]:.4f}")
    print(f"  English worst: s={starts[worst_idx]} (Q{starts[worst_idx]}-{starts[worst_idx]+K-1}), d̄={d_obs[worst_idx]:.4f}")

    # Spearman correlation between Arabic and English window curves
    def spearman(a, b):
        n = len(a)
        ra = [r for r, _ in sorted(enumerate(a), key=lambda x: x[1])]
        rank_a = [0] * n
        for rank, idx in enumerate(sorted(range(n), key=lambda i: a[i])):
            rank_a[idx] = rank
        rank_b = [0] * n
        for rank, idx in enumerate(sorted(range(n), key=lambda i: b[i])):
            rank_b[idx] = rank
        m_a = sum(rank_a) / n
        m_b = sum(rank_b) / n
        num = sum((rank_a[i] - m_a) * (rank_b[i] - m_b) for i in range(n))
        da = math.sqrt(sum((rank_a[i] - m_a) ** 2 for i in range(n)))
        db = math.sqrt(sum((rank_b[i] - m_b) ** 2 for i in range(n)))
        return num / (da * db) if da > 0 and db > 0 else 0.0

    pearson_num = sum((arabic_d[i] - sum(arabic_d) / len(arabic_d)) * (d_obs[i] - sum(d_obs) / len(d_obs)) for i in range(len(d_obs)))
    pearson_da = math.sqrt(sum((x - sum(arabic_d) / len(arabic_d)) ** 2 for x in arabic_d))
    pearson_db = math.sqrt(sum((x - sum(d_obs) / len(d_obs)) ** 2 for x in d_obs))
    pearson = pearson_num / (pearson_da * pearson_db) if pearson_da > 0 and pearson_db > 0 else 0.0
    spear = spearman(arabic_d, d_obs)
    print(f"\n  Pearson r(Arabic_d̄, English_d̄) over 100 windows: {pearson:.4f}")
    print(f"  Spearman ρ(Arabic_d̄, English_d̄) over 100 windows: {spear:.4f}")

    out = {
        "id": "H-NEW-710",
        "prereg_sha": prereg_sha,
        "prereg_sha_expected": PREREG_SHA_EXPECTED,
        "prereg_verified": prereg_sha == PREREG_SHA_EXPECTED,
        "seed": SEED,
        "K": K,
        "translation_source": str(TRANSLATION.name),
        "stemmer": "porter-light + stopwords + lowercase + alpha-only",
        "top_K_vocab": TOP_K_VOCAB,
        "vocab_top20": vocab[:20],
        "kink_grid": KINK_GRID,
        "starts": starts,
        "d_observed_english": d_obs,
        "linear": {"alpha": a_lin, "beta": b_lin, "r2": r2_lin, "perm_p_slope": p_lin_slope, "perm_p_r2": p_lin_r2, "null_mean_r2": null_mean_lin},
        "quadratic": {"alpha": a_q, "beta": b_q, "gamma": c_q, "r2": r2_q, "perm_p_r2": p_q_r2, "null_mean_r2": null_mean_q},
        "two_piece": {"kink": best_kink, "alpha": a_tp, "beta": b_tp, "r2": r2_tp, "perm_p_r2": p_tp_r2, "null_mean_r2": null_mean_tp, "kink_grid_results": kink_results},
        "primary_model": primary[0],
        "primary_r2": primary_r2,
        "primary_adj_r2": primary[2],
        "primary_perm_p": p_primary,
        "alpha_bon": alpha_bon,
        "formal_verdict": formal_verdict,
        "interpretive_verdict": interpretive,
        "arabic_baseline": {
            "primary_model": arabic_primary,
            "primary_r2": arabic_primary_r2,
            "linear_r2": arabic_r2_lin,
            "quadratic_r2": arabic_r2_q,
            "two_piece_r2": arabic_r2_tp,
            "two_piece_kink": arabic_kink,
        },
        "english_vs_arabic": {
            "primary_r2_ratio_en_over_ar": primary_r2 / arabic_primary_r2 if arabic_primary_r2 else None,
            "pearson_r_d_curves": pearson,
            "spearman_rho_d_curves": spear,
        },
        "best_worst_windows": {
            "english_best": {"start": starts[best_idx], "covers": [starts[best_idx], starts[best_idx] + K - 1], "d": d_obs[best_idx]},
            "english_worst": {"start": starts[worst_idx], "covers": [starts[worst_idx], starts[worst_idx] + K - 1], "d": d_obs[worst_idx]},
            "arabic_best": {"start": arabic_starts[arabic_best_idx], "covers": [arabic_starts[arabic_best_idx], arabic_starts[arabic_best_idx] + K - 1], "d": arabic_d[arabic_best_idx]},
            "arabic_worst": {"start": arabic_starts[arabic_worst_idx], "covers": [arabic_starts[arabic_worst_idx], arabic_starts[arabic_worst_idx] + K - 1], "d": arabic_d[arabic_worst_idx]},
        },
        "token_counts_per_surah": token_counts,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
