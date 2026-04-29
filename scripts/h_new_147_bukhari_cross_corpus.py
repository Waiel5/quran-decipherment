#!/usr/bin/env python3
"""H-NEW-145 — Bukhārī cross-corpus Fisher-Rao near-optimality test.

Tests whether the Quran's mushaf-ordering near-optimality (L/L_2opt = 1.107)
is corpus-specific or generalizes to another coherent Arabic religious corpus.

Pre-reg: findings/phase-b-hypotheses/h-new-145-prereg.md
Seed: 20260420

Light-stemming applied to BOTH corpora (apples-to-apples).
"""

from __future__ import annotations

import json
import math
import random
import re
from collections import Counter
from pathlib import Path

SEED = 20260420
PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
BUKHARI_TXT = PROJECT_ROOT / "data/baseline-corpora/raw/bukhari-noquran.txt"
QURAN_JSON = PROJECT_ROOT / "quran-text/quran-no-tashkeel.json"
OUTPUT = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-145.json"

N_RESTARTS = 10
N_PERMS = 10_000
K_ROOTS = 500
DIRICHLET_ALPHA = 0.5

# Light stemmer: strip common prefixes and suffixes (Larkey-like)
STRIP_PREFIXES = ["ال", "وال", "بال", "فال", "كال", "لل", "و", "ف", "ل", "ب", "ك", "س"]
STRIP_SUFFIXES = ["ون", "ين", "ان", "ات", "ها", "هم", "هن", "كم", "كن", "نا", "تم", "تن", "ة", "ه", "ي", "ا", "ت", "ن"]


def light_stem(token: str) -> str:
    t = token
    # Skip very short tokens
    if len(t) < 3:
        return t
    # Try each prefix (longest first for greedy matching)
    for p in sorted(STRIP_PREFIXES, key=lambda x: -len(x)):
        if len(t) > len(p) + 2 and t.startswith(p):
            t = t[len(p):]
            break
    # Try each suffix
    for s in sorted(STRIP_SUFFIXES, key=lambda x: -len(x)):
        if len(t) > len(s) + 2 and t.endswith(s):
            t = t[:-len(s)]
            break
    return t


def load_bukhari_segments() -> list[list[str]]:
    """Split Bukhārī at 'باب' markers; return tokens per segment."""
    with BUKHARI_TXT.open(encoding="utf-8") as f:
        text = f.read()
    # Strip non-letter punctuation/diacritics
    text = re.sub(r"[\u06D6-\u06DF\u0610-\u061A\u0615-\u061A\u064B-\u065F\u0670]+", "", text)
    segments = re.split(r"\bباب\b", text)
    seg_tokens = [s.split() for s in segments if s.strip()]
    # Sort by token count descending, take top 114
    seg_tokens.sort(key=len, reverse=True)
    return seg_tokens[:114]


def load_quran_surahs() -> list[list[str]]:
    """Return tokens per surah (114 surahs)."""
    with QURAN_JSON.open() as f:
        data = json.load(f)
    surahs_toks = []
    for s in data:
        toks: list[str] = []
        for v in s["verses"]:
            text = re.sub(r"[\u06D6-\u06DF\u0610-\u061A\u0615-\u061A\u064B-\u065F\u0670]+", "", v["text"])
            toks.extend(text.split())
        surahs_toks.append(toks)
    return surahs_toks  # Indexed 0..113, surah 1..114 in canonical order


def build_distribution_matrix(corpus_tokens: list[list[str]], k_top: int = K_ROOTS) -> list[list[float]]:
    """Given list of token-lists per segment, return L1-normalized distribution matrix.

    Applies light-stemming, selects top-K global roots.
    """
    stemmed = [[light_stem(t) for t in segs] for segs in corpus_tokens]
    global_freq: Counter[str] = Counter()
    for segs in stemmed:
        global_freq.update(segs)
    top_k = [root for root, _ in global_freq.most_common(k_top)]
    top_k_index = {r: i for i, r in enumerate(top_k)}

    n_segments = len(stemmed)
    mat = [[DIRICHLET_ALPHA] * k_top for _ in range(n_segments)]
    for i, segs in enumerate(stemmed):
        for t in segs:
            if t in top_k_index:
                mat[i][top_k_index[t]] += 1
    # L1-normalize
    for i in range(n_segments):
        s = sum(mat[i])
        if s > 0:
            mat[i] = [x / s for x in mat[i]]
    return mat


def fisher_rao(p: list[float], q: list[float]) -> float:
    # D_FR = 2 * arccos(Σ sqrt(p_k q_k))
    s = 0.0
    for pk, qk in zip(p, q):
        s += math.sqrt(pk * qk)
    s = max(-1.0, min(1.0, s))  # clip for numerical stability
    return 2.0 * math.acos(s)


def build_distance_matrix(dist_mat: list[list[float]]) -> list[list[float]]:
    n = len(dist_mat)
    D = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = fisher_rao(dist_mat[i], dist_mat[j])
            D[i][j] = d
            D[j][i] = d
    return D


def path_length(tour: list[int], D: list[list[float]]) -> float:
    return sum(D[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))


def two_opt_path(tour: list[int], D: list[list[float]], patience: int = 100) -> tuple[list[int], float]:
    best = list(tour)
    n = len(best)
    best_length = path_length(best, D)
    iters_no_improve = 0
    while iters_no_improve < patience:
        improved = False
        for i in range(n - 1):
            for j in range(i + 2, n):
                if j == n - 1 and i == 0:
                    continue  # avoid degenerate case
                if j + 1 > n - 1:
                    # edge (j, j+1) doesn't exist for path; this is fine for path 2-opt
                    # we reverse best[i+1..j]
                    a, b = best[i], best[i + 1]
                    c = best[j]
                    delta = D[a][c] - D[a][b]
                    # For path, we don't have the closing edge; we only affect a-b and c-(j+1) if exists
                    if j + 1 < n:
                        d = best[j + 1]
                        delta = (D[a][c] + D[b][d]) - (D[a][b] + D[c][d])
                    if delta < -1e-10:
                        best[i + 1:j + 1] = best[i + 1:j + 1][::-1]
                        best_length += delta
                        improved = True
                else:
                    a, b = best[i], best[i + 1]
                    c, d = best[j], best[j + 1]
                    delta = (D[a][c] + D[b][d]) - (D[a][b] + D[c][d])
                    if delta < -1e-10:
                        best[i + 1:j + 1] = best[i + 1:j + 1][::-1]
                        best_length += delta
                        improved = True
        iters_no_improve = 0 if improved else iters_no_improve + 1
    return best, best_length


def run_analysis(label: str, corpus_tokens: list[list[str]], seed: int) -> dict:
    print(f"\n{'=' * 70}")
    print(f"{label}")
    print(f"{'=' * 70}")

    dist_mat = build_distribution_matrix(corpus_tokens, K_ROOTS)
    D = build_distance_matrix(dist_mat)
    n = len(D)

    canonical = list(range(n))
    L_canonical = path_length(canonical, D)
    print(f"L_canonical (canonical-order path): {L_canonical:.4f}")

    # 2-opt with restarts
    best_length = float("inf")
    for r in range(N_RESTARTS):
        rng = random.Random(seed + r)
        if r == 0:
            init = list(range(n))
        else:
            init = list(range(n))
            rng.shuffle(init)
        _, refined_len = two_opt_path(init, D)
        if refined_len < best_length:
            best_length = refined_len
    L_2opt = best_length
    R = L_canonical / L_2opt
    print(f"L_2opt (best of {N_RESTARTS} restarts): {L_2opt:.4f}")
    print(f"R = L_canonical / L_2opt = {R:.4f}")

    # Permutation null
    rng = random.Random(seed + 100)
    perm_lengths = []
    for _ in range(N_PERMS):
        perm = list(range(n))
        rng.shuffle(perm)
        perm_lengths.append(path_length(perm, D))
    null_mean = sum(perm_lengths) / N_PERMS
    null_sd = math.sqrt(sum((x - null_mean) ** 2 for x in perm_lengths) / N_PERMS)
    n_le = sum(1 for x in perm_lengths if x <= L_canonical)
    p_one_sided = (n_le + 1) / (N_PERMS + 1)
    z = (L_canonical - null_mean) / null_sd if null_sd > 0 else 0.0
    print(f"Null mean: {null_mean:.3f} ± {null_sd:.3f}")
    print(f"z = {z:+.3f}, p_one_sided_lower = {p_one_sided:.5f}")

    return {
        "label": label,
        "n_segments": n,
        "L_canonical": L_canonical,
        "L_2opt": L_2opt,
        "R": R,
        "null_mean": null_mean,
        "null_sd": null_sd,
        "z_score": z,
        "p_one_sided_lower": p_one_sided,
    }


def main() -> None:
    print("Loading Bukhārī 114 longest bab-segments...")
    bukhari_segs = load_bukhari_segments()
    print(f"Loaded {len(bukhari_segs)} segments, total tokens: {sum(len(s) for s in bukhari_segs):,}")

    print("\nLoading Quran 114 surahs...")
    quran_surahs = load_quran_surahs()
    print(f"Loaded {len(quran_surahs)} surahs, total tokens: {sum(len(s) for s in quran_surahs):,}")

    # Bukhārī analysis
    bukhari = run_analysis("BUKHĀRĪ (114 longest bab-segments, light-stemmed)", bukhari_segs, SEED)
    # Quran analysis with SAME light-stemming (apples-to-apples)
    quran = run_analysis("QURAN (114 surahs, light-stemmed — MW-5 apples-to-apples)", quran_surahs, SEED + 50)

    # MW-5: compare Quran light-stem to QAC benchmark 1.107
    quran_qac_ratio = 1.107
    quran_lightstem_ratio = quran["R"]
    mw5_diff = abs(quran_lightstem_ratio - quran_qac_ratio)
    mw5_pass = mw5_diff < 0.15
    print(f"\n{'=' * 70}")
    print("MW-5: Quran QAC vs light-stem")
    print(f"{'=' * 70}")
    print(f"Quran QAC ratio (cross-finding-011): {quran_qac_ratio:.4f}")
    print(f"Quran light-stem ratio (this run): {quran_lightstem_ratio:.4f}")
    print(f"Difference: {mw5_diff:.4f} (< 0.15 threshold: {mw5_pass})")

    # Primary comparison
    r_bukhari = bukhari["R"]
    r_quran = quran_lightstem_ratio
    diff = r_bukhari - r_quran
    if r_bukhari > 1.3 and diff > 0.15:
        primary_verdict = "CORPUS-SPECIFIC PASS — Bukhārī is NOT near-optimal; Quranic finding exceptional"
    elif r_bukhari < 1.2 and diff < 0.05:
        primary_verdict = "GENRE-GENERAL PASS — Bukhārī is ALSO near-optimal; Quranic finding generalizes"
    else:
        primary_verdict = f"INTERMEDIATE (r_bukhari={r_bukhari:.3f}, r_quran={r_quran:.3f}, diff={diff:.3f})"

    output = {
        "finding_id": "h-new-145",
        "title": "Bukhārī cross-corpus Fisher-Rao near-optimality test",
        "seed": SEED,
        "quran_qac_reference": {
            "source": "cross-finding-011",
            "R_qac": quran_qac_ratio,
        },
        "mw5": {
            "quran_lightstem_R": quran_lightstem_ratio,
            "difference_from_qac": mw5_diff,
            "pass": mw5_pass,
            "note": "Light-stemmer is a noisier root-extractor than QAC-annotated roots.",
        },
        "quran_lightstem": quran,
        "bukhari": bukhari,
        "primary_comparison": {
            "R_bukhari": r_bukhari,
            "R_quran_lightstem_apples_to_apples": r_quran,
            "R_bukhari_minus_R_quran_lightstem": diff,
            "verdict": primary_verdict,
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n{'=' * 70}")
    print("PRIMARY VERDICT")
    print(f"{'=' * 70}")
    print(primary_verdict)
    print(f"\nR_bukhari (canonical bab-order): {r_bukhari:.4f}")
    print(f"R_quran (light-stemmed, apples-to-apples): {r_quran:.4f}")
    print(f"R_quran (QAC, reference): 1.1070")
    print(f"Difference Bukhārī - Quran (both light-stem): {diff:.4f}")
    print(f"\nOutput: {OUTPUT}")


if __name__ == "__main__":
    main()
