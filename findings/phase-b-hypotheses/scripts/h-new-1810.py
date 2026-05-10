#!/usr/bin/env python3
"""
H-NEW-1810 — Corpus-wide Arabic letter (grapheme) frequency distribution
+ muqaṭṭāʿat-14 overlap audit against al-Suyūṭī Itqān nawʿ 6.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1810-letter-frequency.md
SHA256 LOCK (computed 2026-05-10):
  b6b4eeac2b8015cf447805c2494070d2042b7af2a71b9157f4580c941b61533f

Rules-tuple: (no-tashkeel, grapheme-count, Hafs-Kūfan, basmala-as-v.1-of-Q1-only)
Seed: 20260509
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import sys
from collections import Counter

PROJECT_ROOT = "/Users/grey/Downloads/quran"
PREREG_PATH = os.path.join(
    PROJECT_ROOT,
    "findings/phase-b-hypotheses/prereg-h-new-1810-letter-frequency.md",
)
EXPECTED_SHA = "b6b4eeac2b8015cf447805c2494070d2042b7af2a71b9157f4580c941b61533f"
CORPUS_PATH = os.path.join(PROJECT_ROOT, "quran-text/quran-no-tashkeel.json")
BASELINE_CSV = os.path.join(PROJECT_ROOT, "data/baseline-corpora/letter-freqs.csv")
OUTPUT_JSON = os.path.join(
    PROJECT_ROOT, "findings/phase-b-hypotheses/csv/h-new-1810.json"
)

# --- 1) SHA verification (fail-fast) ---
def verify_prereg_sha():
    with open(PREREG_PATH, "rb") as f:
        data = f.read()
    actual = hashlib.sha256(data).hexdigest()
    if actual != EXPECTED_SHA:
        print(
            f"FATAL: prereg SHA mismatch.\n  expected {EXPECTED_SHA}\n  actual   {actual}",
            file=sys.stderr,
        )
        sys.exit(1)
    return actual


# --- 2) Letter normalization to canonical 28-letter alphabet ---
# Per pre-reg rules-tuple (locked before run):
# أ/إ/آ → ا; ؤ → و; ئ → ي; ة → ت; ى → ي; standalone ء tracked separately
ALPHABET_28 = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")
NORMALIZE_MAP = {
    "أ": "ا",
    "إ": "ا",
    "آ": "ا",
    "ؤ": "و",
    "ئ": "ي",
    "ة": "ت",
    "ى": "ي",
}
HAMZA_STANDALONE = "ء"  # tracked but not in the 28


def normalize_char(ch: str) -> str | None:
    """Return a canonical 28-letter symbol, 'HAMZA', or None (filter out)."""
    if ch in NORMALIZE_MAP:
        return NORMALIZE_MAP[ch]
    if ch in ALPHABET_28:
        return ch
    if ch == HAMZA_STANDALONE:
        return "HAMZA"
    return None


# --- 3) Count graphemes across corpus ---
def count_corpus():
    with open(CORPUS_PATH, encoding="utf-8") as f:
        corpus = json.load(f)
    counter = Counter()
    raw_codepoint_counter = Counter()
    n_verses = 0
    for surah in corpus:
        for v in surah["verses"]:
            n_verses += 1
            for ch in v["text"]:
                raw_codepoint_counter[ch] += 1
                norm = normalize_char(ch)
                if norm is not None:
                    counter[norm] += 1
    return counter, raw_codepoint_counter, n_verses, len(corpus)


# --- 4) Hypergeometric P(X >= k) for population=28, success=14, sample=14 ---
def comb(n: int, k: int) -> int:
    return math.comb(n, k)


def hypergeom_ge(k_obs: int, N: int = 28, K: int = 14, n: int = 14) -> float:
    """P(X >= k_obs) under hypergeometric(N, K, n)."""
    total = comb(N, n)
    p = 0.0
    for k in range(k_obs, min(K, n) + 1):
        p += comb(K, k) * comb(N - K, n - k) / total
    return p


# --- 5) Main ---
def main():
    actual_sha = verify_prereg_sha()
    print(f"[OK] prereg SHA verified: {actual_sha}")
    print(f"[OK] reading corpus: {CORPUS_PATH}")

    counter, raw_cp, n_verses, n_surahs = count_corpus()
    print(f"[OK] {n_surahs} surahs, {n_verses} verses processed.")

    # 28-letter counts only (exclude HAMZA from base alphabet per pre-reg)
    letter_counts_28 = {l: counter.get(l, 0) for l in ALPHABET_28}
    total_28 = sum(letter_counts_28.values())
    hamza_count = counter.get("HAMZA", 0)

    # Relative frequencies
    rel_freq_28 = {l: letter_counts_28[l] / total_28 for l in ALPHABET_28}

    # Sort descending
    ranked = sorted(rel_freq_28.items(), key=lambda kv: -kv[1])
    top14 = [l for l, _ in ranked[:14]]
    top3 = [l for l, _ in ranked[:3]]

    # The muqaṭṭāʿat 14 (per al-Suyūṭī Itqān nawʿ 6)
    muqattaat_14 = set("الم" + "ص" + "ر" + "ك" + "ه" + "ي" + "ع" + "ط" + "س" + "ح" + "ق" + "ن")
    # Sanity-check the set has 14 distinct letters
    assert len(muqattaat_14) == 14, f"muqaṭṭāʿat set has {len(muqattaat_14)} letters (expected 14)"

    overlap = sorted(muqattaat_14 & set(top14))
    missing_from_top14 = sorted(muqattaat_14 - set(top14))  # muqaṭṭāʿat letters not in top-14
    extra_in_top14 = sorted(set(top14) - muqattaat_14)      # top-14 letters not in muqaṭṭāʿat
    k_overlap = len(overlap)

    # Hypergeometric p (one-tailed, P(X >= k))
    p_hyper = hypergeom_ge(k_overlap, N=28, K=14, n=14)

    # T1: top-3 sum
    top3_sum = sum(rel_freq_28[l] for l in top3)
    t1_pass = top3_sum > 0.25
    t1_direction_ok = top3_sum > (3.0 / 28.0)  # > uniform expectation

    # T2: exact 14/14
    t2_strong_pass = (k_overlap == 14)

    # T3: muqaṭṭāʿat-14 summed frequency
    muq14_sum_freq = sum(rel_freq_28[l] for l in muqattaat_14)
    t3_pass = muq14_sum_freq > 0.50
    t3_direction_ok = muq14_sum_freq > (14.0 / 28.0)  # > uniform expectation

    # ---- Build output ----
    result = {
        "finding_id": "H-NEW-1810",
        "title": "Corpus-wide Arabic letter frequency + muqaṭṭāʿat-14 overlap audit",
        "date_run": "2026-05-10",
        "prereg_sha256": actual_sha,
        "seed": 20260509,
        "rules_tuple": {
            "orthography": "no-tashkeel",
            "letter_definition": "graphemes (28-letter normalized)",
            "basmala_policy": "counted-only-in-surah-1",
            "verse_numbering": "hafs-kufan",
            "normalization": {
                "أ/إ/آ → ا": True,
                "ؤ → و": True,
                "ئ → ي": True,
                "ة → ت": True,
                "ى → ي": True,
                "ء (standalone hamza)": "tracked separately, not in 28",
            },
        },
        "corpus_stats": {
            "n_surahs": n_surahs,
            "n_verses": n_verses,
            "total_28_letter_graphemes": total_28,
            "standalone_hamza_count": hamza_count,
        },
        "letter_counts_28": letter_counts_28,
        "letter_relative_freq_28": {l: round(rel_freq_28[l], 6) for l in ALPHABET_28},
        "ranked_descending": [
            {"rank": i + 1, "letter": l, "count": letter_counts_28[l], "rel_freq": round(rel_freq_28[l], 6)}
            for i, (l, _) in enumerate(ranked)
        ],
        "top3_letters": top3,
        "top14_letters": top14,
        "muqattaat_14_set": sorted(muqattaat_14),
        "muqattaat_14_letters_unicode_order": ["ا","ل","م","ص","ر","ك","ه","ي","ع","ط","س","ح","ق","ن"],
        "overlap_top14_vs_muqattaat14": overlap,
        "k_overlap": k_overlap,
        "muqattaat14_NOT_in_top14": missing_from_top14,
        "top14_NOT_in_muqattaat14": extra_in_top14,
        "hypergeometric_p_X_geq_k": round(p_hyper, 10),
        "tests": {
            "T1_top3_nonuniform": {
                "description": "Top-3 letters' summed relative freq > 0.25 (direction LOCKED HIGH)",
                "top3_sum": round(top3_sum, 6),
                "threshold": 0.25,
                "direction_locked": "HIGH",
                "direction_observed": "HIGH" if t1_direction_ok else "REVERSED",
                "pass": t1_pass,
            },
            "T2_strong_set_equality": {
                "description": "muqaṭṭāʿat-14 set == top-14 by frequency (al-Suyūṭī Itqān nawʿ 6 strong-form)",
                "k_overlap": k_overlap,
                "threshold": 14,
                "pass": t2_strong_pass,
            },
            "T2_weak_hypergeometric": {
                "description": "P(X ≥ k_observed | N=28, K=14, n=14), one-tailed",
                "k_overlap": k_overlap,
                "p_value": round(p_hyper, 10),
                "alpha_bonferroni": 0.0167,
                "pass_directed": p_hyper < 0.0167,
            },
            "T3_muqattaat_sum_freq": {
                "description": "muqaṭṭāʿat-14 summed relative freq > 0.50 (direction LOCKED HIGH)",
                "sum_freq": round(muq14_sum_freq, 6),
                "threshold": 0.50,
                "direction_locked": "HIGH",
                "direction_observed": "HIGH" if t3_direction_ok else "REVERSED",
                "pass": t3_pass,
            },
        },
        "raw_codepoint_top20": [
            {"codepoint": cp, "count": c, "hex": f"U+{ord(cp):04X}"}
            for cp, c in raw_cp.most_common(20)
        ],
    }

    # ---- Cross-corpus context (descriptive, NOT pre-committed) ----
    # Parse the pre-computed baseline-corpora/letter-freqs.csv
    try:
        with open(BASELINE_CSV, encoding="utf-8") as f:
            header = f.readline().rstrip("\n").split(",")
            # header[0] = 'name'; header[1:] = letters
            baseline_rows = {}
            for line in f:
                parts = line.rstrip("\n").split(",")
                name = parts[0]
                freqs = {header[i]: float(parts[i]) for i in range(1, len(header))}
                baseline_rows[name] = freqs
        # For each baseline corpus, normalize codepoints to canonical 28 and rank
        cross_corpus = {}
        for name, freqs in baseline_rows.items():
            norm = Counter()
            for cp, f_val in freqs.items():
                n_cp = normalize_char(cp)
                if n_cp is not None and n_cp != "HAMZA":
                    norm[n_cp] += f_val
            # Re-normalize so they sum to 1
            s = sum(norm.values())
            if s > 0:
                norm_rel = {l: norm.get(l, 0.0) / s for l in ALPHABET_28}
                ranked_n = sorted(norm_rel.items(), key=lambda kv: -kv[1])
                top14_n = [l for l, _ in ranked_n[:14]]
                k_ov_n = len(muqattaat_14 & set(top14_n))
                muq_sum_n = sum(norm_rel[l] for l in muqattaat_14)
                cross_corpus[name] = {
                    "top14": top14_n,
                    "k_overlap_with_muqattaat14": k_ov_n,
                    "muqattaat14_sum_freq": round(muq_sum_n, 6),
                }
        result["cross_corpus_descriptive"] = cross_corpus
    except Exception as e:
        result["cross_corpus_descriptive_error"] = str(e)

    # Write output
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[OK] wrote {OUTPUT_JSON}")

    # ---- Print summary to stdout ----
    print()
    print("=" * 70)
    print(f"H-NEW-1810 SUMMARY")
    print("=" * 70)
    print(f"corpus: {n_surahs} surahs, {n_verses} verses, {total_28} graphemes (28-letter)")
    print(f"standalone hamza ء (not in 28): {hamza_count}")
    print()
    print(f"Top-14 letters by frequency (descending):")
    for i, (l, fr) in enumerate(ranked[:14]):
        in_muq = "✓" if l in muqattaat_14 else "✗"
        print(f"  {i+1:2d}. {l}  {letter_counts_28[l]:6d}  {fr:.4f}  muq:{in_muq}")
    print()
    print(f"Letters 15-28 (descending):")
    for i, (l, fr) in enumerate(ranked[14:]):
        in_muq = "✓" if l in muqattaat_14 else "✗"
        print(f"  {i+15:2d}. {l}  {letter_counts_28[l]:6d}  {fr:.4f}  muq:{in_muq}")
    print()
    print(f"muqaṭṭāʿat-14 ∩ top-14 = {k_overlap}/14")
    print(f"  overlap letters: {' '.join(overlap)}")
    if missing_from_top14:
        print(f"  muqaṭṭāʿat letters NOT in top-14: {' '.join(missing_from_top14)}")
    if extra_in_top14:
        print(f"  top-14 letters NOT in muqaṭṭāʿat-14: {' '.join(extra_in_top14)}")
    print(f"hypergeometric P(X ≥ {k_overlap}) = {p_hyper:.3e}")
    print()
    print(f"T1 top-3 sum = {top3_sum:.4f} (threshold > 0.25) → {'PASS' if t1_pass else 'NULL'}")
    print(f"T2 strong-form k=14/14? → {'PASS' if t2_strong_pass else 'FALSIFIED'}")
    print(f"T2 weak-form hypergeom p={p_hyper:.3e} (α_bon=0.0167) → {'PASS-DIRECTED' if p_hyper < 0.0167 else 'NULL'}")
    print(f"T3 muqaṭṭāʿat-14 sum = {muq14_sum_freq:.4f} (threshold > 0.50) → {'PASS' if t3_pass else 'NULL'}")
    print()


if __name__ == "__main__":
    main()
