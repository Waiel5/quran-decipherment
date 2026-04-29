#!/usr/bin/env python3
"""H-NEW-900: Cross-text architectural comparison.

Tests whether the Quran's compression-tail R²=0.986 (H-NEW-660) and
iʿjāz anti-twin r=-0.86 (H-NEW-730) generalize to other ordered corpora.

Two approaches:
  (A) Bukhari religious-prose: build per-book content + final-letter dists,
      compute Fisher-Rao d̄ over K-windows, fit compression-tail R² + content × rhyme r.
  (B) Shuffled-Quran null: 100 random surah orderings; recompute both
      observables; check Quran is in the extreme tail.

Honest framing: Bukhari's "canonical order" is editorial-thematic, not
the same kind of attested ordering as the Quran's mushaf. Document this caveat.
"""
import hashlib
import json
import math
import random
import re
import unicodedata
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
RAW = ROOT / "data/baseline-corpora/raw"
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
H_NEW_700 = ROOT / "findings/phase-b-hypotheses/csv/h-new-700.json"
H_NEW_660 = ROOT / "findings/phase-b-hypotheses/csv/h-new-660.json"
H_NEW_730 = ROOT / "findings/phase-b-hypotheses/csv/h-new-730.json"
QURAN_TXT = ROOT / "data/alt-text/quran-simple-min-txt-2.txt"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-900.json"

SEED = 20260428
N_SHUFFLES = 100
K_QURAN = 15            # K used in H-NEW-660/730 for Quran
K_BUKHARI = 10          # smaller K because Bukhari has only ~79 books
TOPK_WORDS = 500
DIRICHLET_ALPHA = 0.5

# Quran reference values
QURAN_R2_LIN = 0.7706         # h-new-660 linear primary value used here
QURAN_R2_PRIMARY = 0.9860     # h-new-660 primary (two-piece)
QURAN_RCR = -0.8643           # h-new-730 content × rhyme

# Letter normalization (same as h-new-740)
ARABIC_LETTERS = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")
LETTER_INDEX = {ch: i for i, ch in enumerate(ARABIC_LETTERS)}
VARIANT_MAP = {
    "ى": "ي", "ة": "ه",
    "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا",
    "ؤ": "و", "ئ": "ي",
}
DIACRITICS_RANGES = [
    (0x0610, 0x061A), (0x064B, 0x065F),
    (0x0670, 0x0670), (0x06D6, 0x06DC),
    (0x06DF, 0x06E4), (0x06E7, 0x06E8),
    (0x06EA, 0x06ED),
]
ORNAMENTS = set("ـۛۖۚۗۘۙۜۥۭۧۤ")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def is_diacritic(cp):
    for lo, hi in DIACRITICS_RANGES:
        if lo <= cp <= hi:
            return True
    return False


def strip_diacritics(s):
    return "".join(ch for ch in s if not is_diacritic(ord(ch)) and ch not in ORNAMENTS)


def normalize_letter(ch):
    return VARIANT_MAP.get(ch, ch)


def is_arabic_letter(ch):
    return ("ء" <= ch <= "ي") or ch in "ىةؤئٱآأإ"


def get_final_letter(text):
    cleaned = strip_diacritics(text).strip()
    cleaned = re.sub(r"\s*\([0-9]+\)\s*$", "", cleaned)
    cleaned = re.sub(r"\s+\d+\s*$", "", cleaned)
    cleaned = cleaned.rstrip()
    while cleaned and not is_arabic_letter(cleaned[-1]):
        cleaned = cleaned[:-1]
    if not cleaned:
        return None
    last = normalize_letter(cleaned[-1])
    return last if last in LETTER_INDEX else None


def normalize_word(w):
    w = strip_diacritics(w)
    w = "".join(normalize_letter(ch) for ch in w)
    w = "".join(ch for ch in w if "؀" <= ch <= "ۿ")
    if len(w) < 2:
        return w
    for p in ["ال", "و", "ف", "ب", "ل", "ك"]:
        if w.startswith(p) and len(w) > len(p) + 1:
            w = w[len(p):]
            break
    return w


def fisher_rao(p, q):
    bc = sum(math.sqrt(p[i] * q[i]) for i in range(len(p)))
    bc = max(-1.0, min(1.0, bc))
    return 2.0 * math.acos(bc)


def cosine_distance(u, v):
    du = math.sqrt(sum(x * x for x in u))
    dv = math.sqrt(sum(x * x for x in v))
    if du < 1e-15 or dv < 1e-15:
        return 1.0
    sim = sum(u[i] * v[i] for i in range(len(u))) / (du * dv)
    sim = max(-1.0, min(1.0, sim))
    return 1.0 - sim


def build_dist_matrix(vectors, metric_fn):
    n = len(vectors)
    D = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = metric_fn(vectors[i], vectors[j])
            D[i][j] = d
            D[j][i] = d
    return D


def mean_pairwise(D, idxs):
    pairs = list(combinations(idxs, 2))
    if not pairs:
        return 0.0
    return sum(D[a][b] for a, b in pairs) / len(pairs)


def fit_linear(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return 0.0, 0.0, 0.0
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * x for x in xs]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2


def fit_quadratic(xs, ys):
    n = len(xs)
    sx = sum(xs); sx2 = sum(x*x for x in xs); sx3 = sum(x**3 for x in xs); sx4 = sum(x**4 for x in xs)
    sy = sum(ys); sxy = sum(xs[i]*ys[i] for i in range(n)); sx2y = sum(xs[i]**2*ys[i] for i in range(n))
    M = [[n, sx, sx2], [sx, sx2, sx3], [sx2, sx3, sx4]]
    b = [sy, sxy, sx2y]
    A = [row[:] + [b[i]] for i, row in enumerate(M)]
    for col in range(3):
        pivot = max(range(col, 3), key=lambda r: abs(A[r][col]))
        A[col], A[pivot] = A[pivot], A[col]
        piv = A[col][col]
        if abs(piv) < 1e-15:
            return 0.0, 0.0, 0.0, 0.0
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
        return 0.0, 0.0, 0.0
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * f for f in feat]
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((ys[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2


def best_compression_r2(d_window):
    """Return max R² over linear, quadratic, and best two-piece kink (matching H-NEW-660 logic)."""
    n = len(d_window)
    xs = list(range(n))
    xs_centered = [x - (n - 1) / 2.0 for x in xs]
    _, _, r2_lin = fit_linear(xs_centered, d_window)
    _, _, _, r2_q = fit_quadratic(xs_centered, d_window)
    best_tp = 0.0
    best_kink = 0
    for kink in range(max(1, n // 5), n - max(1, n // 5)):
        _, _, r2_tp = fit_two_piece(xs, d_window, kink)
        if r2_tp > best_tp:
            best_tp = r2_tp
            best_kink = kink
    return {
        "linear_r2": r2_lin,
        "quadratic_r2": r2_q,
        "two_piece_r2": best_tp,
        "two_piece_kink": best_kink,
        "max_r2": max(r2_lin, r2_q, best_tp),
    }


def pearson_r(x, y):
    n = len(x)
    if n < 2:
        return 0.0
    mx, my = sum(x) / n, sum(y) / n
    num = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    dx = math.sqrt(sum((x[i] - mx) ** 2 for i in range(n)))
    dy = math.sqrt(sum((y[i] - my) ** 2 for i in range(n)))
    return num / (dx * dy) if dx > 1e-15 and dy > 1e-15 else 0.0


# ============================================================
# (A) BUKHARI ANALYSIS
# ============================================================

def parse_bukhari(path):
    """Parse Bukhari: split on '# صحيح البخاري/<book>' headers.
    Each book becomes one section. Returns list of (book_label, [hadith_text])."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    parts = re.split(r"(?m)^# صحيح البخاري/(.+)$", text)
    # parts = [preamble, label1, body1, label2, body2, ...]
    books = []
    for i in range(1, len(parts), 2):
        label = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        # Remove chapter sub-headers (باب ...) but keep their text
        # Extract individual ḥadīth: lines with [number] markers
        # We'll simply use the entire book text for content; for "final letter" use end-of-ḥadīth (line endings before the next [N])
        books.append((label, body))
    return books


def bukhari_book_content_vec(body, word_index):
    arabic_word_re = re.compile(r"[؀-ۿ]+")
    # Strip [N] markers
    body_clean = re.sub(r"\[\d+\]", " ", body)
    c = Counter()
    for w in arabic_word_re.findall(body_clean):
        nw = normalize_word(w)
        if nw and len(nw) >= 2:
            c[nw] += 1
    vec = [0.0] * len(word_index)
    for w, n in c.items():
        if w in word_index:
            vec[word_index[w]] += n
    smoothed = [v + DIRICHLET_ALPHA for v in vec]
    s = sum(smoothed)
    return [v / s for v in smoothed], c


def bukhari_book_rhyme_vec(body):
    """Per-book final-letter distribution. We treat each ḥadīth (text between [N] markers
    or each natural full sentence) as a 'unit' whose final letter we record.
    More robust: use the last Arabic letter of each ḥadīth block."""
    # Split body on hadith markers [N]
    chunks = re.split(r"\[\d+\]", body)
    finals = []
    for ch in chunks:
        ch = ch.strip()
        if not ch:
            continue
        # Use last Arabic letter
        f = get_final_letter(ch)
        if f is not None:
            finals.append(f)
    v = [0] * 28
    for ch in finals:
        v[LETTER_INDEX[ch]] += 1
    n = sum(v)
    if n > 0:
        return [x / n for x in v], len(finals)
    return [1.0 / 28] * 28, 0


def analyze_bukhari():
    print("\n" + "=" * 60)
    print("(A) BUKHARI ANALYSIS")
    print("=" * 60)
    books = parse_bukhari(RAW / "bukhari.txt")
    # Sort by label for canonical ordering (alphabetical) — alternative we could use file order which is editorial
    print(f"Parsed {len(books)} books from Bukhari.")

    # Use file order (matches printed editions)
    print(f"Using file-order (matches printed Bukhari editions).")

    # Build vocabulary across all books
    all_word_counts = Counter()
    all_book_counters = []
    arabic_word_re = re.compile(r"[؀-ۿ]+")
    for label, body in books:
        body_clean = re.sub(r"\[\d+\]", " ", body)
        c = Counter()
        for w in arabic_word_re.findall(body_clean):
            nw = normalize_word(w)
            if nw and len(nw) >= 2:
                c[nw] += 1
        all_word_counts.update(c)
        all_book_counters.append(c)
    top_words = [w for w, _ in all_word_counts.most_common(TOPK_WORDS)]
    word_index = {w: i for i, w in enumerate(top_words)}
    print(f"Bukhari vocab size: {len(all_word_counts)} unique normalized; top-{TOPK_WORDS} retained.")
    print(f"Top-5 words: {top_words[:5]}")

    # Per-book content + rhyme vectors
    content_vecs = []
    rhyme_vecs = []
    n_finals = []
    n_words = []
    book_labels = []
    for (label, body), c in zip(books, all_book_counters):
        # content vec
        vec = [0.0] * TOPK_WORDS
        for w, n in c.items():
            if w in word_index:
                vec[word_index[w]] += n
        smoothed = [v + DIRICHLET_ALPHA for v in vec]
        s = sum(smoothed)
        content_vecs.append([v / s for v in smoothed])
        n_words.append(sum(c.values()))
        # rhyme vec
        rvec, nf = bukhari_book_rhyme_vec(body)
        rhyme_vecs.append(rvec)
        n_finals.append(nf)
        book_labels.append(label)

    print(f"Mean ḥadīth-units per book: {sum(n_finals)/len(n_finals):.1f}, total: {sum(n_finals)}")
    print(f"Mean words per book: {sum(n_words)/len(n_words):.0f}")

    # Distance matrices
    print(f"Computing Fisher-Rao distance matrices (content + rhyme)...")
    D_content = build_dist_matrix(content_vecs, fisher_rao)
    D_rhyme = build_dist_matrix(rhyme_vecs, fisher_rao)

    n = len(books)
    K = K_BUKHARI
    n_windows = n - K + 1
    print(f"K={K} windows: {n_windows}")
    if n_windows < 20:
        print("INSUFFICIENT WINDOWS")
        return None

    d_content = []
    d_rhyme = []
    for s in range(n_windows):
        idxs = list(range(s, s + K))
        d_content.append(mean_pairwise(D_content, idxs))
        d_rhyme.append(mean_pairwise(D_rhyme, idxs))

    # Compression-tail
    comp = best_compression_r2(d_content)
    print(f"\nBukhari compression-tail (content):")
    print(f"  linear R² = {comp['linear_r2']:.4f}")
    print(f"  quadratic R² = {comp['quadratic_r2']:.4f}")
    print(f"  two-piece R² (kink={comp['two_piece_kink']}) = {comp['two_piece_r2']:.4f}")
    print(f"  MAX R² = {comp['max_r2']:.4f}")
    print(f"  -- Quran's primary R² = {QURAN_R2_PRIMARY:.4f} --")

    # iʿjāz anti-twin
    r_cr = pearson_r(d_content, d_rhyme)
    print(f"\nBukhari iʿjāz anti-twin r(content × rhyme) = {r_cr:+.4f}")
    print(f"  -- Quran's r = {QURAN_RCR:+.4f} --")

    return {
        "n_books": n,
        "K": K,
        "n_windows": n_windows,
        "vocab_size": len(all_word_counts),
        "n_finals_total": sum(n_finals),
        "compression_tail": comp,
        "anti_twin_r": r_cr,
        "d_content": d_content,
        "d_rhyme": d_rhyme,
        "book_labels": book_labels,
    }


# ============================================================
# (B) SHUFFLED-QURAN NULL
# ============================================================

def load_quran_D():
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def load_quran_rhyme_per_window():
    """We don't have per-surah rhyme distance matrix; load h-new-700 d_rhyme array
    which is per-window for canonical ordering. For shuffled-Quran null we need
    per-surah rhyme vectors instead.

    Strategy: read h-new-700 source data — it computed rhyme distance matrix
    over surah-level vectors. If h-new-700 stores R matrix, use it; otherwise
    rebuild per-surah final-letter vectors from quran-simple-clean."""
    # First try to load D_rhyme_matrix from h-new-700.json
    with open(H_NEW_700) as f:
        h700 = json.load(f)
    # h700 stores d_observed (window-level) but we need surah-level matrix.
    # Look for per-surah data:
    keys = list(h700.keys())
    return h700, keys


def build_quran_rhyme_matrix():
    """Build per-surah final-letter distribution matrix from quran-simple-clean,
    then compute Fisher-Rao distance matrix over 114 surahs."""
    surah_finals = {i: Counter() for i in range(1, 115)}
    with open(QURAN_TXT, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Format: surah|verse|text
            parts = line.split("|")
            if len(parts) < 3:
                continue
            try:
                s = int(parts[0])
                v = int(parts[1])
            except ValueError:
                continue
            text = parts[2]
            ch = get_final_letter(text)
            if ch is not None:
                surah_finals[s][ch] += 1
    # Build vectors
    vecs = [None] * 115  # 1-indexed
    for s in range(1, 115):
        v = [0] * 28
        for ch, n in surah_finals[s].items():
            v[LETTER_INDEX[ch]] += n
        total = sum(v)
        if total > 0:
            vecs[s] = [x / total for x in v]
        else:
            vecs[s] = [1.0 / 28] * 28
    # Distance matrix
    D = [[0.0] * 115 for _ in range(115)]
    for i in range(1, 115):
        for j in range(i + 1, 115):
            d = fisher_rao(vecs[i], vecs[j])
            D[i][j] = d
            D[j][i] = d
    return D, vecs


def shuffled_quran_null(D_content, D_rhyme, n_shuffles=N_SHUFFLES, seed=SEED):
    """For each shuffle: pick random perm of 1..114, compute K-window d̄_content,
    fit best compression R²; compute K-window d̄_rhyme; compute r_cr.
    Return distributions + observed values from canonical mushaf order."""
    print("\n" + "=" * 60)
    print("(B) SHUFFLED-QURAN NULL (100 shuffles)")
    print("=" * 60)
    K = K_QURAN
    starts = list(range(1, 101))  # match h-new-660: 100 windows of K=15 covering Q 1..114
    rng = random.Random(seed)

    # Canonical (observed) values
    d_content_obs = []
    d_rhyme_obs = []
    for s in starts:
        sub = list(range(s, s + K))
        d_content_obs.append(mean_pairwise(D_content, sub))
        d_rhyme_obs.append(mean_pairwise(D_rhyme, sub))
    comp_obs = best_compression_r2(d_content_obs)
    r_cr_obs = pearson_r(d_content_obs, d_rhyme_obs)
    print(f"Observed (canonical mushaf):")
    print(f"  Compression-tail max R² = {comp_obs['max_r2']:.4f}")
    print(f"  Anti-twin r = {r_cr_obs:+.4f}")

    # Shuffled distribution
    null_r2 = []
    null_rcr = []
    for it in range(n_shuffles):
        perm = list(range(1, 115))
        rng.shuffle(perm)
        d_c = []
        d_r = []
        for s in starts:
            sub = [perm[s - 1 + i] for i in range(K)]
            d_c.append(mean_pairwise(D_content, sub))
            d_r.append(mean_pairwise(D_rhyme, sub))
        comp = best_compression_r2(d_c)
        null_r2.append(comp["max_r2"])
        null_rcr.append(pearson_r(d_c, d_r))
        if (it + 1) % 25 == 0:
            print(f"  shuffle {it+1}/{n_shuffles}: R²={comp['max_r2']:.4f}, r={null_rcr[-1]:+.4f}")

    # Empirical p-values
    p_r2 = sum(1 for x in null_r2 if x >= comp_obs["max_r2"]) / n_shuffles
    p_rcr = sum(1 for x in null_rcr if x <= r_cr_obs) / n_shuffles
    print(f"\nNull distribution (R² max under shuffle):")
    print(f"  mean = {sum(null_r2)/n_shuffles:.4f}, max = {max(null_r2):.4f}, min = {min(null_r2):.4f}")
    print(f"  Quran obs R² = {comp_obs['max_r2']:.4f}, p(null ≥ obs) = {p_r2:.4f}")
    print(f"\nNull distribution (anti-twin r under shuffle):")
    print(f"  mean = {sum(null_rcr)/n_shuffles:+.4f}, min = {min(null_rcr):+.4f}, max = {max(null_rcr):+.4f}")
    print(f"  Quran obs r = {r_cr_obs:+.4f}, p(null ≤ obs) = {p_rcr:.4f}")

    return {
        "n_shuffles": n_shuffles,
        "K": K,
        "n_windows": len(starts),
        "observed_max_r2": comp_obs["max_r2"],
        "observed_compression": comp_obs,
        "observed_r_cr": r_cr_obs,
        "null_r2_distribution": null_r2,
        "null_r_cr_distribution": null_rcr,
        "null_r2_mean": sum(null_r2) / n_shuffles,
        "null_r2_max": max(null_r2),
        "null_r2_min": min(null_r2),
        "null_r_cr_mean": sum(null_rcr) / n_shuffles,
        "null_r_cr_min": min(null_rcr),
        "null_r_cr_max": max(null_rcr),
        "p_r2_empirical": p_r2,
        "p_r_cr_empirical": p_rcr,
    }


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("H-NEW-900: Cross-text architectural comparison")
    print("=" * 60)
    print(f"Seed: {SEED}")
    print(f"Quran reference: compression R²={QURAN_R2_PRIMARY:.4f}, anti-twin r={QURAN_RCR:+.4f}")

    results = {
        "id": "H-NEW-900",
        "seed": SEED,
        "quran_reference": {
            "compression_r2_primary": QURAN_R2_PRIMARY,
            "compression_r2_linear": QURAN_R2_LIN,
            "anti_twin_r": QURAN_RCR,
            "K": K_QURAN,
        },
        "available_corpora": {
            "religious_prose": ["bukhari.txt"],
            "religious_prose_unsuitable_for_section_analysis": [
                "sira-ibn-hisham.txt (no clear section markers)",
                "jahiz-hayawan.txt (no clear book/chapter markers in extract)",
            ],
            "absent_data_gaps": [
                "Tao Te Ching (81 chapters) — not on disk",
                "Psalms (150 chapters) — not on disk",
                "Mahabharata — not on disk",
                "Sefer Tehillim (Hebrew Psalms) — not on disk",
            ],
        },
    }

    # (A) Bukhari
    bukhari_res = analyze_bukhari()
    results["bukhari"] = bukhari_res

    # (B) Shuffled-Quran null
    print("\nLoading Quran content distance matrix (h-new-111)...")
    D_content = load_quran_D()
    print("Building Quran per-surah rhyme distance matrix...")
    D_rhyme, _ = build_quran_rhyme_matrix()
    shuffle_res = shuffled_quran_null(D_content, D_rhyme)
    results["shuffled_quran_null"] = shuffle_res

    # ============================================================
    # SUMMARY
    # ============================================================
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Quran  : R²={QURAN_R2_PRIMARY:.4f}, r={QURAN_RCR:+.4f}")
    if bukhari_res:
        print(f"Bukhari: R²={bukhari_res['compression_tail']['max_r2']:.4f}, "
              f"r={bukhari_res['anti_twin_r']:+.4f}")
    print(f"Shuffled-Quran null: R²-max={shuffle_res['null_r2_max']:.4f} (mean {shuffle_res['null_r2_mean']:.4f}); "
          f"r-min={shuffle_res['null_r_cr_min']:+.4f} (mean {shuffle_res['null_r_cr_mean']:+.4f})")
    print(f"  p(null ≥ Quran R²): {shuffle_res['p_r2_empirical']:.4f}")
    print(f"  p(null ≤ Quran r ): {shuffle_res['p_r_cr_empirical']:.4f}")

    # Verdict
    bukhari_distinct_r2 = bukhari_res and bukhari_res["compression_tail"]["max_r2"] < 0.85
    bukhari_distinct_r = bukhari_res and bukhari_res["anti_twin_r"] > -0.5
    shuffle_distinct_r2 = shuffle_res["p_r2_empirical"] <= 0.05
    shuffle_distinct_r = shuffle_res["p_r_cr_empirical"] <= 0.05

    verdict_lines = []
    if bukhari_distinct_r2 and bukhari_distinct_r:
        verdict_lines.append("Bukhari shows neither compression-tail R²>0.95 nor anti-twin r<-0.5 → Quran's signature is DISTINCT from Bukhari.")
    elif bukhari_res:
        verdict_lines.append(f"Bukhari R²={bukhari_res['compression_tail']['max_r2']:.4f}, r={bukhari_res['anti_twin_r']:+.4f} — partial overlap; not fully distinctive vs Bukhari.")
    if shuffle_distinct_r2:
        verdict_lines.append(f"Shuffled-Quran null: Quran's R² is in extreme upper tail (p={shuffle_res['p_r2_empirical']:.4f}).")
    if shuffle_distinct_r:
        verdict_lines.append(f"Shuffled-Quran null: Quran's r is in extreme lower tail (p={shuffle_res['p_r_cr_empirical']:.4f}).")
    verdict = " ".join(verdict_lines)
    results["verdict"] = verdict
    print(f"\nVERDICT: {verdict}")

    # Save
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
