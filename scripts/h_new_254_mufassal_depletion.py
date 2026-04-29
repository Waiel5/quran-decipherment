#!/usr/bin/env python3
"""H-NEW-254 — Mufaṣṣal divine-name depletion: compositional or length-artifact?

Pre-reg: findings/phase-b-hypotheses/h-new-254-mufassal-depletion-mechanism-prereg.md
Parent: h-new-239 (divine-name-gradient). Seed: 20260419. Bonferroni k=1 (α=0.05).

Primary test: for each mufaṣṣal surah s ∈ {50..114}, compare observed divine-name
density D_s^obs = name_tokens_s / N_s to a length-matched null — Bernoulli(p_corpus)
bootstrap of N_s words, 10000 draws per surah. Stouffer-combine one-tailed per-surah
p-values (observed < null) across the 65 surahs.

MW-5 instrument check: shuffle per-verse divine-name counts across the full 6236-verse
space and re-run the whole protocol. Shuffled-corpus Stouffer Z should be ≈ 0.

Outputs:
- findings/phase-b-hypotheses/csv/h-new-254.json
- findings/phase-b-hypotheses/csv/h-new-254-per-surah.tsv
"""
from __future__ import annotations

import csv
import json
import random
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats as sstats

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
BONFERRONI_K = 1
ALPHA_PER_CELL = 0.05 / BONFERRONI_K
N_BOOT = 10000  # per-surah Bernoulli bootstrap

NAMES_CSV = ROOT / "findings/phase-b-hypotheses/divine-names-by-verse.csv"
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
OUT_DIR = ROOT / "findings/phase-b-hypotheses/csv"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSON = OUT_DIR / "h-new-254.json"
OUT_TSV = OUT_DIR / "h-new-254-per-surah.tsv"

MUFASSAL = list(range(50, 115))  # Q 50..114 (65 surahs)


# -------- data loaders (parity with H-NEW-239) --------

def load_surah_words() -> dict[int, int]:
    with open(QURAN_JSON, encoding="utf-8") as f:
        data = json.load(f)
    out = {}
    for s in data:
        sid = s["id"]
        total = 0
        for v in s["verses"]:
            total += len(v["text"].split())
        out[sid] = total
    return out


def load_all_verse_word_counts() -> list[tuple[int, int, int]]:
    """Return list of (surah, verse, n_words) across the full 6236-verse corpus."""
    out = []
    with open(QURAN_JSON, encoding="utf-8") as f:
        data = json.load(f)
    for s in data:
        for v in s["verses"]:
            out.append((s["id"], v["id"], len(v["text"].split())))
    return out


def load_per_verse_names() -> dict[tuple[int, int], int]:
    counts: dict[tuple[int, int], int] = {}
    with open(NAMES_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["surah"]); vid = int(row["verse"])
            n = int(row["num_names"])
            counts[(sid, vid)] = n
    return counts


def per_surah_name_tokens(per_verse_counts: dict[tuple[int, int], int]) -> dict[int, int]:
    out: dict[int, int] = defaultdict(int)
    for (sid, vid), n in per_verse_counts.items():
        out[sid] += n
    return dict(out)


# -------- main protocol --------

def run_protocol(per_verse_counts, surah_words, label, rng_seed):
    """Compute per-surah observed density, null density (Bernoulli bootstrap), z-scores,
    and Stouffer's combined Z across Q 50-114.

    Returns dict with per-surah and combined results.
    """
    rng = np.random.default_rng(rng_seed)

    # Corpus marginals
    N_total_words = sum(surah_words.values())
    N_total_name_tokens = sum(per_verse_counts.values())
    p_corpus = N_total_name_tokens / N_total_words

    tokens_per_surah = per_surah_name_tokens(per_verse_counts)

    per_surah = []
    per_surah_p_less: list[float] = []
    per_surah_z: list[float] = []

    for sid in MUFASSAL:
        N_s = surah_words[sid]
        obs_tokens = tokens_per_surah.get(sid, 0)
        obs_density = obs_tokens / N_s if N_s > 0 else 0.0

        # Null: simulate N_BOOT draws of N_s Bernoulli(p_corpus)
        # faster: sample total tokens via Binomial(N_s, p_corpus)
        null_tokens = rng.binomial(N_s, p_corpus, size=N_BOOT)
        null_density = null_tokens / N_s

        null_mean = float(null_density.mean())
        null_sd = float(null_density.std(ddof=1))
        z_s = (obs_density - null_mean) / null_sd if null_sd > 0 else 0.0

        # One-tailed p (observed <= null), continuity-corrected
        # P(null_density <= obs_density)
        # Equivalently proportion of null draws at or below observed tokens.
        n_le = int((null_tokens <= obs_tokens).sum())
        # Clamp away from 0/1 for Stouffer inverse Φ
        p_less = (n_le + 0.5) / (N_BOOT + 1.0)
        p_less = min(max(p_less, 1e-6), 1 - 1e-6)

        per_surah.append({
            "surah": sid,
            "N_s": N_s,
            "obs_tokens": obs_tokens,
            "obs_density": obs_density,
            "null_mean_density": null_mean,
            "null_sd_density": null_sd,
            "z": z_s,
            "p_less": p_less,
        })
        per_surah_p_less.append(p_less)
        per_surah_z.append(z_s)

    # Stouffer's Z: convert one-tailed p_less → z via inverse CDF; large-negative z means
    # observed was below null (depletion).
    # Standard Stouffer: z_i = Φ^{-1}(1 − p_i); but we want directional — use
    # z_i = Φ^{-1}(p_less_i) so that small p_less (observed well below null) → large-NEG z.
    z_stouffer_per_surah = [sstats.norm.ppf(p) for p in per_surah_p_less]
    Z_combined = float(np.sum(z_stouffer_per_surah) / np.sqrt(len(z_stouffer_per_surah)))

    # One-tailed p for H1 (less-than):
    p_combined_less = float(sstats.norm.cdf(Z_combined))
    # Two-sided secondary:
    p_combined_two = float(2 * min(p_combined_less, 1 - p_combined_less))

    # Descriptives
    obs_mean_density = float(np.mean([r["obs_density"] for r in per_surah]))
    null_mean_density = float(np.mean([r["null_mean_density"] for r in per_surah]))
    z_stats = {
        "mean": float(np.mean(per_surah_z)),
        "median": float(np.median(per_surah_z)),
        "min": float(np.min(per_surah_z)),
        "max": float(np.max(per_surah_z)),
        "sd": float(np.std(per_surah_z, ddof=1)),
        "frac_negative": float(np.mean(np.array(per_surah_z) < 0)),
        "frac_below_m1": float(np.mean(np.array(per_surah_z) < -1)),
        "frac_below_m2": float(np.mean(np.array(per_surah_z) < -2)),
    }

    return {
        "label": label,
        "p_corpus": p_corpus,
        "N_total_words": N_total_words,
        "N_total_name_tokens": N_total_name_tokens,
        "per_surah": per_surah,
        "obs_mean_density_mufassal": obs_mean_density,
        "null_mean_density_mufassal": null_mean_density,
        "Z_stouffer": Z_combined,
        "p_stouffer_less": p_combined_less,
        "p_stouffer_two": p_combined_two,
        "z_descriptives": z_stats,
        "n_mufassal_surahs": len(per_surah),
    }


# -------- MW-5 shuffle nulls (instrument checks) --------

def shuffle_per_verse_counts(per_verse_counts, seed) -> dict[tuple[int, int], int]:
    """Permute per-verse divine-name counts across the full 6236-verse corpus.
    Under VERSE-shuffle, per-surah tokens reflect verse-count-weighted random
    placement — mufaṣṣal surahs have short verses and thus MORE tokens per
    word than per-word null expects. This is the H-NEW-239 shuffle. Included
    for reproducibility with the parent finding. NOT a per-word instrument
    check (see word_level_shuffle below for the matching null).
    """
    rng = random.Random(seed)
    with open(QURAN_JSON, encoding="utf-8") as f:
        data = json.load(f)
    all_verses = []
    for s in data:
        for v in s["verses"]:
            all_verses.append((s["id"], v["id"]))
    counts_vec = [per_verse_counts.get(k, 0) for k in all_verses]
    rng.shuffle(counts_vec)
    return dict(zip(all_verses, counts_vec))


def word_level_shuffle_per_surah_tokens(per_verse_counts, surah_words, seed) -> dict[int, int]:
    """Per-WORD shuffle: distribute the total N_name_tokens across the full
    N_total_words word-token pool uniformly at random. Return per-surah
    token counts under that placement. Under this null, the matching-Bernoulli
    length-matched test SHOULD yield Stouffer Z ≈ 0 (proper instrument check).
    """
    rng = np.random.default_rng(seed)
    N_total_words = sum(surah_words.values())
    N_total_name_tokens = sum(per_verse_counts.values())
    # Draw N_total_name_tokens word-indices uniformly from [0, N_total_words)
    # Assign each to the surah at that global word-index.
    # Build cumulative word-index boundaries per surah.
    surah_ids = sorted(surah_words.keys())
    boundaries = []
    cum = 0
    for sid in surah_ids:
        boundaries.append((cum, cum + surah_words[sid], sid))
        cum += surah_words[sid]
    # Sample N_total_name_tokens positions (with replacement is WRONG — must be
    # without replacement to be a true shuffle; use permutation)
    # Use choice without replacement via random permutation.
    # Memory: 82375 ints = fine.
    all_word_positions = np.arange(N_total_words, dtype=np.int64)
    chosen = rng.choice(all_word_positions, size=N_total_name_tokens, replace=False)
    tokens_per_surah: dict[int, int] = {sid: 0 for sid in surah_ids}
    # Map each chosen position → surah via binary search on boundaries
    starts = np.array([b[0] for b in boundaries])
    for pos in chosen:
        idx = int(np.searchsorted(starts, pos, side="right")) - 1
        sid = boundaries[idx][2]
        tokens_per_surah[sid] += 1
    return tokens_per_surah


def run_protocol_from_per_surah_tokens(tokens_per_surah, surah_words, p_corpus_override,
                                        label, rng_seed, N_total_words, N_total_name_tokens):
    """Variant of run_protocol that accepts a pre-shuffled per-surah token count
    dict directly (used for the word-level shuffle instrument check). Null model
    still uses Bernoulli(p_corpus) at N_s. If the per-surah tokens came from a
    proper per-word shuffle with the same p_corpus, Z should be ≈ 0.
    """
    rng = np.random.default_rng(rng_seed)
    p_corpus = p_corpus_override

    per_surah = []
    per_surah_p_less: list[float] = []
    per_surah_z: list[float] = []

    for sid in MUFASSAL:
        N_s = surah_words[sid]
        obs_tokens = tokens_per_surah.get(sid, 0)
        obs_density = obs_tokens / N_s if N_s > 0 else 0.0

        null_tokens = rng.binomial(N_s, p_corpus, size=N_BOOT)
        null_density = null_tokens / N_s

        null_mean = float(null_density.mean())
        null_sd = float(null_density.std(ddof=1))
        z_s = (obs_density - null_mean) / null_sd if null_sd > 0 else 0.0

        n_le = int((null_tokens <= obs_tokens).sum())
        p_less = (n_le + 0.5) / (N_BOOT + 1.0)
        p_less = min(max(p_less, 1e-6), 1 - 1e-6)

        per_surah.append({
            "surah": sid, "N_s": N_s, "obs_tokens": obs_tokens,
            "obs_density": obs_density, "null_mean_density": null_mean,
            "null_sd_density": null_sd, "z": z_s, "p_less": p_less,
        })
        per_surah_p_less.append(p_less)
        per_surah_z.append(z_s)

    z_stouffer_per_surah = [sstats.norm.ppf(p) for p in per_surah_p_less]
    Z_combined = float(np.sum(z_stouffer_per_surah) / np.sqrt(len(z_stouffer_per_surah)))
    p_combined_less = float(sstats.norm.cdf(Z_combined))
    p_combined_two = float(2 * min(p_combined_less, 1 - p_combined_less))

    obs_mean_density = float(np.mean([r["obs_density"] for r in per_surah]))
    null_mean_density = float(np.mean([r["null_mean_density"] for r in per_surah]))
    z_stats = {
        "mean": float(np.mean(per_surah_z)),
        "median": float(np.median(per_surah_z)),
        "min": float(np.min(per_surah_z)),
        "max": float(np.max(per_surah_z)),
        "sd": float(np.std(per_surah_z, ddof=1)),
        "frac_negative": float(np.mean(np.array(per_surah_z) < 0)),
        "frac_below_m1": float(np.mean(np.array(per_surah_z) < -1)),
        "frac_below_m2": float(np.mean(np.array(per_surah_z) < -2)),
    }
    return {
        "label": label, "p_corpus": p_corpus,
        "N_total_words": N_total_words, "N_total_name_tokens": N_total_name_tokens,
        "per_surah": per_surah,
        "obs_mean_density_mufassal": obs_mean_density,
        "null_mean_density_mufassal": null_mean_density,
        "Z_stouffer": Z_combined,
        "p_stouffer_less": p_combined_less,
        "p_stouffer_two": p_combined_two,
        "z_descriptives": z_stats,
        "n_mufassal_surahs": len(per_surah),
    }


# -------- main --------

def main():
    random.seed(SEED)
    np.random.seed(SEED)

    surah_words = load_surah_words()
    per_verse_counts = load_per_verse_names()

    real_result = run_protocol(
        per_verse_counts, surah_words,
        label="observed", rng_seed=SEED,
    )

    # MW-5a: VERSE-shuffle null (H-NEW-239 style). NOT the proper instrument check
    # (predictably inflates mufaṣṣal density because mufaṣṣal has short verses).
    shuffled_counts = shuffle_per_verse_counts(per_verse_counts, seed=SEED + 1)
    mw5_verse_result = run_protocol(
        shuffled_counts, surah_words,
        label="mw5_verse_shuffled", rng_seed=SEED + 2,
    )

    # MW-5b: WORD-level shuffle — proper instrument check matching the per-word
    # Bernoulli null. Should yield Stouffer Z ≈ 0 by construction.
    N_total_words_real = sum(surah_words.values())
    N_total_name_tokens_real = sum(per_verse_counts.values())
    p_corpus_real = N_total_name_tokens_real / N_total_words_real
    word_shuffled_tokens = word_level_shuffle_per_surah_tokens(
        per_verse_counts, surah_words, seed=SEED + 3,
    )
    mw5_word_result = run_protocol_from_per_surah_tokens(
        word_shuffled_tokens, surah_words,
        p_corpus_override=p_corpus_real,
        label="mw5_word_shuffled", rng_seed=SEED + 4,
        N_total_words=N_total_words_real,
        N_total_name_tokens=N_total_name_tokens_real,
    )

    # Sanity-check set: Q 112, Q 110, Q 85, Q 65, Q 59 top-density per H-NEW-239
    sanity_ids = [112, 110, 85, 65, 59]
    sanity = [
        r for r in real_result["per_surah"] if r["surah"] in sanity_ids
    ]
    # Q 59 is NOT in mufaṣṣal Q 50-114 range... wait, Q 59 IS in Q 50..114. OK.
    # (Q 50-114 includes Q 59.)

    # Bonferroni decision
    def verdict(Z, p):
        if Z <= sstats.norm.ppf(ALPHA_PER_CELL):  # i.e., Z ≤ −1.645 for α=0.05
            return "COMPOSITIONAL_CHOICE"
        elif Z >= -sstats.norm.ppf(ALPHA_PER_CELL):  # Z ≥ +1.645
            return "UNEXPECTED_ENRICHMENT"
        else:
            return "LENGTH_ARTIFACT"

    real_verdict = verdict(real_result["Z_stouffer"], real_result["p_stouffer_less"])
    mw5_verse_verdict = verdict(mw5_verse_result["Z_stouffer"], mw5_verse_result["p_stouffer_less"])
    mw5_word_verdict = verdict(mw5_word_result["Z_stouffer"], mw5_word_result["p_stouffer_less"])

    # Top most-depleted and most-enriched mufaṣṣal surahs by z
    sorted_by_z = sorted(real_result["per_surah"], key=lambda r: r["z"])
    top_depleted = sorted_by_z[:10]
    top_enriched = sorted_by_z[-10:][::-1]

    out = {
        "finding_id": "h-new-254",
        "parent": "h-new-239",
        "seed": SEED,
        "n_boot_per_surah": N_BOOT,
        "bonferroni_k": BONFERRONI_K,
        "alpha_per_cell": ALPHA_PER_CELL,
        "mufassal_range": "Q 50-114",
        "n_mufassal_surahs": len(MUFASSAL),
        "real": real_result,
        "mw5_verse_shuffle_null": mw5_verse_result,
        "mw5_word_shuffle_null": mw5_word_result,
        "decisions": {
            "real_verdict": real_verdict,
            "mw5_verse_verdict": mw5_verse_verdict,
            "mw5_word_verdict": mw5_word_verdict,
        },
        "sanity_top_density_surahs": sanity,
        "top10_depleted_by_z": top_depleted,
        "top10_enriched_by_z": top_enriched,
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    # Per-surah TSV
    with open(OUT_TSV, "w", encoding="utf-8") as f:
        f.write("surah\tN_s\tobs_tokens\tobs_density\tnull_mean_density\tnull_sd_density\tz\tp_less\n")
        for r in real_result["per_surah"]:
            f.write(
                f"{r['surah']}\t{r['N_s']}\t{r['obs_tokens']}\t{r['obs_density']:.6f}"
                f"\t{r['null_mean_density']:.6f}\t{r['null_sd_density']:.6f}"
                f"\t{r['z']:+.4f}\t{r['p_less']:.6f}\n"
            )

    # Console summary
    print("=" * 72)
    print(f"H-NEW-254 mufaṣṣal depletion mechanism — seed {SEED}, Bonf k={BONFERRONI_K}")
    print("=" * 72)
    print(f"Corpus marginal p = N_names / N_words = "
          f"{real_result['N_total_name_tokens']} / {real_result['N_total_words']} "
          f"= {real_result['p_corpus']:.6f}")
    print()
    print(f"Mufaṣṣal Q 50-114 (n={real_result['n_mufassal_surahs']}):")
    print(f"  mean observed density = {real_result['obs_mean_density_mufassal']:.6f}")
    print(f"  mean null density    = {real_result['null_mean_density_mufassal']:.6f}")
    print(f"  Stouffer's Z = {real_result['Z_stouffer']:+.4f}")
    print(f"  one-tailed p_less = {real_result['p_stouffer_less']:.6g}")
    print(f"  two-tailed p_two = {real_result['p_stouffer_two']:.6g}")
    print(f"  VERDICT: {real_verdict}")
    print()
    zd = real_result["z_descriptives"]
    print(f"  Per-surah z: mean={zd['mean']:+.3f} median={zd['median']:+.3f} "
          f"min={zd['min']:+.3f} max={zd['max']:+.3f}")
    print(f"    frac(z<0) = {zd['frac_negative']:.3f}; "
          f"frac(z<-1) = {zd['frac_below_m1']:.3f}; "
          f"frac(z<-2) = {zd['frac_below_m2']:.3f}")
    print()
    print("MW-5a VERSE-shuffle null (H-NEW-239 style; NOT proper per-word check):")
    print(f"  Z'= {mw5_verse_result['Z_stouffer']:+.4f}   p_less={mw5_verse_result['p_stouffer_less']:.4g}"
          f"   verdict={mw5_verse_verdict}")
    print("    (expected POSITIVE because mufaṣṣal has short verses → gets more tokens/word")
    print("     under verse-shuffle than per-word Bernoulli expects; diagnostic, not null-check)")
    print()
    print("MW-5b WORD-LEVEL shuffle (proper per-word instrument check, ≈ 0 by construction):")
    print(f"  Z'= {mw5_word_result['Z_stouffer']:+.4f}   p_less={mw5_word_result['p_stouffer_less']:.4g}"
          f"   verdict={mw5_word_verdict}")
    print()
    print("Sanity — top-density mufaṣṣal surahs (per H-NEW-239 top-10):")
    for r in sanity:
        print(f"  Q{r['surah']:3d}  N={r['N_s']:3d}  obs_d={r['obs_density']:.4f}  "
              f"null_d={r['null_mean_density']:.4f}  z={r['z']:+.3f}")
    print()
    print("Top-10 most-depleted mufaṣṣal surahs (most-negative z):")
    for r in top_depleted:
        print(f"  Q{r['surah']:3d}  N={r['N_s']:4d}  obs_d={r['obs_density']:.4f}  "
              f"null_d={r['null_mean_density']:.4f}  z={r['z']:+.3f}")
    print()
    print("Top-10 most-enriched mufaṣṣal surahs (most-positive z):")
    for r in top_enriched:
        print(f"  Q{r['surah']:3d}  N={r['N_s']:4d}  obs_d={r['obs_density']:.4f}  "
              f"null_d={r['null_mean_density']:.4f}  z={r['z']:+.3f}")
    print()
    print(f"Output JSON: {OUT_JSON}")
    print(f"Per-surah TSV: {OUT_TSV}")


if __name__ == "__main__":
    main()
