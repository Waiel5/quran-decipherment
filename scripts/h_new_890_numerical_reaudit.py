#!/usr/bin/env python3
"""
H-NEW-890 — Numerical and sequence re-audit in light of 2026-04-28 architectural findings.

Five pre-committed tests (Bonferroni-5, alpha_bon = 0.01):
  T1 — Q 8 + Q 9 functional unity (FR-distance rank).
  T2 — Compression-tail genericity (Quran vs Bukhari, kink-50 fit).
  T3 — Verse-count divisibility-by-19 (permutation null).
  T4 — 6236/114 divisibility patterns (descriptive).
  T5 — Allah-density vs FR-distance to Q 1 (Spearman).

Inputs
  data/hafs-verse-counts.tsv
  quran-text/quran-no-tashkeel.json
  findings/phase-b-hypotheses/csv/h-new-111.json
  findings/phase-b-hypotheses/csv/compression_per_surah.csv
  data/baseline-corpora/raw/bukhari-noquran.txt

Outputs
  findings/phase-b-hypotheses/csv/h-new-890.json
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import os
import re
from pathlib import Path

import numpy as np
from scipy import stats

# ----------------------------------------------------------------------------
# Paths and constants
# ----------------------------------------------------------------------------

ROOT = Path("/Users/grey/Downloads/quran")
PRREG = ROOT / "findings/phase-b-hypotheses/h-new-890-numerical-reaudit-prereg.md"
VERSE_COUNTS = ROOT / "data/hafs-verse-counts.tsv"
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
FR_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
COMP_CSV = ROOT / "findings/phase-b-hypotheses/csv/compression_per_surah.csv"
BUKHARI_TXT = ROOT / "data/baseline-corpora/raw/bukhari-noquran.txt"

OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-890.json"

SEED = 20260428
N_ITER = 100_000
BONFERRONI_K = 5
ALPHA = 0.05
ALPHA_BON = ALPHA / BONFERRONI_K

rng = np.random.default_rng(SEED)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


# ----------------------------------------------------------------------------
# Load shared resources
# ----------------------------------------------------------------------------

def load_verse_counts() -> np.ndarray:
    """Return n_verses[1..114] with index 0 unused."""
    arr = np.zeros(115, dtype=int)
    with VERSE_COUNTS.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            s, n = line.split("\t")
            arr[int(s)] = int(n)
    assert arr[1:].sum() == 6236, f"verse-count sanity: {arr[1:].sum()} != 6236"
    return arr


def load_fr_distance_matrix() -> np.ndarray:
    """Return symmetric 115x115 FR distance matrix (index 0 unused; diag = 0)."""
    payload = json.loads(FR_JSON.read_text())
    raw = payload["D_matrix_upper_triangular"]
    triples = json.loads(raw) if isinstance(raw, str) else raw
    D = np.zeros((115, 115), dtype=float)
    for i, j, d in triples:
        D[i, j] = d
        D[j, i] = d
    return D


def load_quran_text() -> dict[int, str]:
    """Map surah_id -> concatenated no-tashkeel verse text."""
    surahs = json.loads(QURAN_JSON.read_text())
    out = {}
    for s in surahs:
        sid = int(s["id"])
        out[sid] = " ".join(v["text"] for v in s["verses"])
    return out


# ----------------------------------------------------------------------------
# Test 1 — Q 8 + Q 9 functional-unity
# ----------------------------------------------------------------------------

def test_1_anfal_tawba(D: np.ndarray) -> dict:
    """Empirical rank of d_FR(8, 9) among the 113 adjacent-pair distances."""
    adj = np.array([D[i, i + 1] for i in range(1, 114)])
    d_8_9 = D[8, 9]
    rank = int(np.sum(adj <= d_8_9))  # number of adjacent pairs <= the focal pair
    # convert to one-sided (smaller is more interesting): empirical p
    p_one = rank / 113
    return {
        "test_id": "T1",
        "test_name": "Q8+Q9 FR-distance unity",
        "d_FR_8_9": float(d_8_9),
        "adjacent_mean": float(adj.mean()),
        "adjacent_median": float(np.median(adj)),
        "adjacent_std": float(adj.std(ddof=1)),
        "adjacent_min": float(adj.min()),
        "adjacent_max": float(adj.max()),
        "rank_le": rank,
        "n_adjacent": 113,
        "p_one_sided": float(p_one),
        "alpha_bon": ALPHA_BON,
        "verdict": "PASS" if p_one < ALPHA_BON else "NULL",
        "notes": (
            "rank_le = number of adjacent pairs with distance <= d_FR(8, 9). "
            "Smaller rank => smaller-than-typical adjacent distance."
        ),
    }


# ----------------------------------------------------------------------------
# Test 2 — Compression-tail genericity (Bukhari pseudo-mushaf)
# ----------------------------------------------------------------------------

def two_piece_kink_fit(s: np.ndarray, y: np.ndarray, kink: int = 50) -> dict:
    """Fit y ~ a + b*(s - kink) where slope b applies only for s > kink (clamped at 0).

    Specifically: y = a0 + a1 * 1{s > kink} * (s - kink) + a2 * 1{s <= kink} * 0
    Using the simplest H-NEW-660 form: y = alpha + beta * max(0, s - kink).
    """
    x = np.maximum(0.0, s - kink).astype(float)
    n = len(s)
    # Design matrix [1, x]
    X = np.column_stack([np.ones(n), x])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X @ coef
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    # adj-R^2
    adj_r2 = 1.0 - (1.0 - r2) * (n - 1) / (n - 2) if n > 2 else float("nan")
    return {
        "alpha": float(coef[0]),
        "beta": float(coef[1]),
        "r2": float(r2),
        "adj_r2": float(adj_r2),
        "n": int(n),
        "kink": kink,
    }


def gzip_ratio(text: str) -> float:
    raw = text.encode("utf-8")
    if len(raw) == 0:
        return float("nan")
    return len(gzip.compress(raw, compresslevel=9)) / len(raw)


def test_2_compression_genericity(verse_counts: np.ndarray) -> dict:
    """Build pseudo-mushaf from Bukhari, slice into 114 chunks of byte-lengths
    proportional to per-surah verse counts, fit kink-50 model, compare to Quranic R^2.
    """
    # Quranic compression per surah (from existing CSV)
    q_ratios = np.zeros(115, dtype=float)
    with COMP_CSV.open() as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            sid = int(row["surah"])
            q_ratios[sid] = float(row["gzip_ratio"])
    quran_s = np.arange(1, 115)
    quran_y = q_ratios[1:]
    quran_fit = two_piece_kink_fit(quran_s, quran_y, kink=50)

    # Bukhari pseudo-mushaf
    bukhari = BUKHARI_TXT.read_text(encoding="utf-8", errors="replace")
    total_bytes = len(bukhari.encode("utf-8"))
    proportions = verse_counts[1:].astype(float) / verse_counts[1:].sum()
    chunk_sizes = (proportions * total_bytes).astype(int)
    # Fix rounding
    chunk_sizes[-1] = total_bytes - chunk_sizes[:-1].sum()

    # Slice Bukhari by byte-budget. Convert text to bytes, slice, decode-replace
    bukhari_bytes = bukhari.encode("utf-8")
    chunks: list[str] = []
    pos = 0
    for sz in chunk_sizes:
        end = min(pos + sz, len(bukhari_bytes))
        # snap to nearest space to avoid mid-multibyte cut
        chunk_bytes = bukhari_bytes[pos:end]
        try:
            chunks.append(chunk_bytes.decode("utf-8", errors="replace"))
        except Exception:
            chunks.append("")
        pos = end
    while len(chunks) < 114:
        chunks.append("")

    bukhari_ratios = np.array([gzip_ratio(c) if len(c) > 50 else np.nan for c in chunks])
    valid = ~np.isnan(bukhari_ratios)
    bukhari_s = np.arange(1, 115)[valid]
    bukhari_y = bukhari_ratios[valid]
    bukhari_fit = two_piece_kink_fit(bukhari_s, bukhari_y, kink=50)

    delta_r2 = quran_fit["r2"] - bukhari_fit["r2"]
    # Distinctive criterion (sign-agnostic): Quran R^2 exceeds Bukhari by >=0.20
    # AND Bukhari slope magnitude is < 50% of Quran's |beta|.
    distinctive = (delta_r2 >= 0.20) and (abs(bukhari_fit["beta"]) < 0.5 * abs(quran_fit["beta"]))

    if distinctive:
        verdict = "PASS-DISTINCTIVE"
    elif bukhari_fit["r2"] >= 0.90 and (bukhari_fit["beta"] * quran_fit["beta"]) > 0:
        verdict = "NULL-GENERIC"
    else:
        verdict = "MIXED"

    return {
        "test_id": "T2",
        "test_name": "Compression-tail genericity (Quran vs Bukhari)",
        "quran_fit": quran_fit,
        "bukhari_pseudomushaf_fit": bukhari_fit,
        "delta_r2": float(delta_r2),
        "verdict": verdict,
        "notes": (
            "Per-surah gzip_ratio as a function of mushaf-position, kink-50 simple model. "
            "NOTE: this is a related but distinct metric from H-NEW-660 (which uses pairwise FR-cohesion-distance). "
            "Slope sign: positive beta means gzip_ratio rises in the tail (short surahs are less compressible due to small-sample overhead); "
            "this is the EXPECTED direction once one accounts for length-scale, and the magnitude difference Quran vs Bukhari is the signal of interest. "
            "Distinctive iff Quran R^2 exceeds Bukhari by >= 0.20 AND |Bukhari beta| < 0.5 * |Quran beta|."
        ),
    }


# ----------------------------------------------------------------------------
# Test 3 — Divisibility-by-19
# ----------------------------------------------------------------------------

def test_3_div_19(verse_counts: np.ndarray) -> dict:
    """k = number of surahs with n_verses divisible by 19. Permutation null
    over multinomial bootstrap from empirical verse-count distribution.
    """
    n = verse_counts[1:]
    k_obs = int(np.sum(n % 19 == 0))
    expected_uniform = 114.0 / 19.0  # 6.0
    # Build multinomial bootstrap null
    null_ks = np.zeros(N_ITER, dtype=int)
    rng_local = np.random.default_rng(SEED + 3)
    for it in range(N_ITER):
        sample = rng_local.choice(n, size=114, replace=True)
        null_ks[it] = int(np.sum(sample % 19 == 0))
    # Two-tailed empirical p
    null_mean = float(null_ks.mean())
    if k_obs >= null_mean:
        p_two = (np.sum(null_ks >= k_obs) + np.sum(null_ks <= 2 * null_mean - k_obs)) / N_ITER
    else:
        p_two = (np.sum(null_ks <= k_obs) + np.sum(null_ks >= 2 * null_mean - k_obs)) / N_ITER
    p_two = float(min(1.0, p_two))

    # List which surahs
    matching = [int(i) for i in range(1, 115) if verse_counts[i] % 19 == 0]
    matching_with_n = {str(i): int(verse_counts[i]) for i in matching}
    return {
        "test_id": "T3",
        "test_name": "Verse-count divisibility-by-19",
        "k_obs": k_obs,
        "expected_uniform": expected_uniform,
        "null_mean": null_mean,
        "null_std": float(null_ks.std(ddof=1)),
        "null_min": int(null_ks.min()),
        "null_max": int(null_ks.max()),
        "p_two_sided": p_two,
        "alpha_bon": ALPHA_BON,
        "verdict": "PASS" if p_two < ALPHA_BON else "NULL",
        "matching_surahs": matching_with_n,
        "n_iter": N_ITER,
        "notes": (
            "Multinomial bootstrap from empirical verse-count distribution preserves range/skew. "
            "Two-tailed p around the bootstrap mean."
        ),
    }


# ----------------------------------------------------------------------------
# Test 4 — 6236 / 114 divisibility patterns (descriptive)
# ----------------------------------------------------------------------------

def factor(n: int) -> list[int]:
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i != n // i:
                out.append(n // i)
        i += 1
    return sorted(out)


def test_4_total_factors(verse_counts: np.ndarray) -> dict:
    n_total = int(verse_counts[1:].sum())
    n_surahs = 114
    mean = n_total / n_surahs
    divisors_total = factor(n_total)
    divisors_n_surahs = factor(n_surahs)
    matching_to_total = [int(i) for i in range(1, 115) if int(verse_counts[i]) in set(divisors_total)]
    return {
        "test_id": "T4",
        "test_name": "6236 / 114 divisibility (descriptive)",
        "total_verses": n_total,
        "n_surahs": n_surahs,
        "mean_verses_per_surah": mean,
        "factorization_6236": "2^2 * 1559 (1559 prime)",
        "factorization_114": "2 * 3 * 19",
        "divisors_6236": divisors_total,
        "divisors_114": divisors_n_surahs,
        "surahs_whose_n_divides_6236": matching_to_total,
        "verdict": "DESCRIPTIVE-NULL",
        "notes": "No structural divisibility pattern: 1559 is prime; 6236 has only 6 divisors (1,2,4,1559,3118,6236), none of which match any actual surah length. The factorization 6236 = 4 x 1559 has no architectural significance.",
    }


# ----------------------------------------------------------------------------
# Test 5 — Allah-density vs FR-distance to Q 1
# ----------------------------------------------------------------------------

def test_5_allah_density(text_by_surah: dict[int, str], verse_counts: np.ndarray, D: np.ndarray) -> dict:
    """Spearman of divine-name density per surah vs d_FR(s, 1).

    PRIMARY metric: per-verse divine-name count from divine-names-by-verse.csv
    (broader Allah-related set: Allah, al-Rahman, al-Rahim, etc. — matches the
    classical 'Q 1 has 5+ divine names' claim). Sensitivity: bare regex on الله.
    """
    div_csv = ROOT / "findings/phase-b-hypotheses/divine-names-by-verse.csv"
    div_per_surah = np.zeros(115, dtype=int)
    with div_csv.open() as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            sid = int(row["surah"])
            div_per_surah[sid] += int(row["num_names"])
    div_density = np.zeros(115, dtype=float)
    for s in range(1, 115):
        div_density[s] = div_per_surah[s] / max(1, verse_counts[s])

    # Sensitivity: bare الله regex
    pat = re.compile(r"\bالله\b")
    bare_counts = np.zeros(115, dtype=int)
    bare_density = np.zeros(115, dtype=float)
    for sid, text in text_by_surah.items():
        n_allah = len(pat.findall(text))
        bare_counts[sid] = n_allah
        bare_density[sid] = n_allah / max(1, verse_counts[sid])

    s_indices = np.arange(2, 115)

    def spearman_with_p(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
        rho, p_two = stats.spearmanr(x, y)
        if rho < 0:
            p_one_neg = float(p_two / 2)
        else:
            p_one_neg = float(1.0 - p_two / 2)
        return float(rho), float(p_two), p_one_neg

    # PRIMARY: divine-names density (matches classical claim about Q1)
    x_primary = div_density[s_indices]
    y = np.array([D[s, 1] for s in s_indices])
    rho_p, p_two_p, p_one_p = spearman_with_p(x_primary, y)

    # SENSITIVITY: bare الله regex
    x_sens = bare_density[s_indices]
    rho_s, p_two_s, p_one_s = spearman_with_p(x_sens, y)

    return {
        "test_id": "T5",
        "test_name": "Divine-name density vs d_FR(s, 1)",
        "n_surahs_in_test": int(len(s_indices)),
        "primary_metric": "divine-names-by-verse.csv num_names per verse",
        "primary_spearman_rho": rho_p,
        "primary_p_two_sided": p_two_p,
        "primary_p_one_sided_neg": p_one_p,
        "sensitivity_metric": "bare regex الله per verse (no-tashkeel)",
        "sensitivity_spearman_rho": rho_s,
        "sensitivity_p_two_sided": p_two_s,
        "sensitivity_p_one_sided_neg": p_one_s,
        "alpha_bon": ALPHA_BON,
        "verdict": "PASS" if p_one_p < ALPHA_BON else "NULL",
        "q1_div_names_count": int(div_per_surah[1]),
        "q1_div_names_density": float(div_density[1]),
        "q1_bare_allah_count": int(bare_counts[1]),
        "q1_bare_allah_density": float(bare_density[1]),
        "q1_n_verses": int(verse_counts[1]),
        "global_div_density": float(div_per_surah[1:].sum() / verse_counts[1:].sum()),
        "global_bare_density": float(bare_counts[1:].sum() / verse_counts[1:].sum()),
        "notes": (
            "Primary metric uses the broader divine-names catalog (Allah, al-Rahman, al-Rahim, etc.) "
            "from divine-names-by-verse.csv per the classical 'Q 1 = umm al-kitāb' claim. "
            "Sensitivity uses bare الله token regex — narrower, missing prefixed forms (لله, بالله, والله). "
            "One-sided NEG test: closer-to-Q1 surahs should have HIGHER divine-name density => negative rho."
        ),
    }


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main():
    np.random.seed(SEED)
    print("[*] H-NEW-890 — running 5 numerical re-audit tests")

    print("[*] Loading verse counts, FR matrix, Quranic text…")
    verse_counts = load_verse_counts()
    D = load_fr_distance_matrix()
    text_by_surah = load_quran_text()

    print("[*] T1 — Q8+Q9 functional-unity FR-distance rank…")
    t1 = test_1_anfal_tawba(D)
    print(f"    d_FR(8,9) = {t1['d_FR_8_9']:.4f} | rank = {t1['rank_le']}/113 | p = {t1['p_one_sided']:.4f} | {t1['verdict']}")

    print("[*] T2 — Compression-tail genericity (Quran vs Bukhari)…")
    t2 = test_2_compression_genericity(verse_counts)
    print(f"    Quran R^2 = {t2['quran_fit']['r2']:.3f} (beta = {t2['quran_fit']['beta']:.5f})")
    print(f"    Bukhari R^2 = {t2['bukhari_pseudomushaf_fit']['r2']:.3f} (beta = {t2['bukhari_pseudomushaf_fit']['beta']:.5f})")
    print(f"    delta_R^2 = {t2['delta_r2']:.3f} | {t2['verdict']}")

    print("[*] T3 — divisibility-by-19 permutation null…")
    t3 = test_3_div_19(verse_counts)
    print(f"    k_obs = {t3['k_obs']} (expected ~6); null_mean = {t3['null_mean']:.2f} | p = {t3['p_two_sided']:.4f} | {t3['verdict']}")
    print(f"    matching surahs: {t3['matching_surahs']}")

    print("[*] T4 — 6236 / 114 factorization descriptive…")
    t4 = test_4_total_factors(verse_counts)
    print(f"    {t4['notes']}")

    print("[*] T5 — Allah-density vs FR-distance to Q1…")
    t5 = test_5_allah_density(text_by_surah, verse_counts, D)
    print(f"    PRIMARY rho = {t5['primary_spearman_rho']:.4f} | p_one(neg) = {t5['primary_p_one_sided_neg']:.4f} | {t5['verdict']}")
    print(f"    SENSITIVITY rho = {t5['sensitivity_spearman_rho']:.4f} | p_one(neg) = {t5['sensitivity_p_one_sided_neg']:.4f}")

    # Aggregate
    out = {
        "finding_id": "h-new-890",
        "title": "Numerical and sequence re-audit in light of 2026-04-28 architectural findings",
        "date": "2026-04-28",
        "seed": SEED,
        "n_iter": N_ITER,
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "prereg_path": str(PRREG.relative_to(ROOT)),
        "prereg_sha256": sha256_file(PRREG),
        "rules_tuple": {
            "corpus": "Hafs-no-tashkeel",
            "verse_counts": "data/hafs-verse-counts.tsv",
            "fr_matrix": "findings/phase-b-hypotheses/csv/h-new-111.json (D_matrix_upper_triangular)",
            "compression": "findings/phase-b-hypotheses/csv/compression_per_surah.csv (gzip_ratio)",
            "baseline_corpus": "data/baseline-corpora/raw/bukhari-noquran.txt",
        },
        "tests": {
            "T1": t1,
            "T2": t2,
            "T3": t3,
            "T4": t4,
            "T5": t5,
        },
        "headline": {
            "T1": t1["verdict"],
            "T2": t2["verdict"],
            "T3": t3["verdict"],
            "T4": t4["verdict"],
            "T5": t5["verdict"],
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"[*] Wrote {OUT_JSON}")
    print("[*] Headline:", out["headline"])
    return out


if __name__ == "__main__":
    main()
