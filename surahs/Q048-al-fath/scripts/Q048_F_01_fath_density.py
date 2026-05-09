#!/usr/bin/env python3
"""
Q048-F-01 — Q 48 al-Fatḥ *fatḥ*-root density test.

Pre-reg: ../preregs/Q048-F-01-fath-root-density-prereg.md
SHA-locked: 263b58105397cb13f1ec36ad5faeac1f7603c21fc10ba57a0027b37c5696f511
Seed: 20260509

Hypothesis (locked direction): Q 48 has a corpus-EXACT *fatḥ*-root density
significantly above corpus baseline, controlling for length.
"""
import json
import hashlib
import os
import sys
from math import comb
import random
from collections import defaultdict

PRE_REG_PATH = os.path.join(os.path.dirname(__file__), '..', 'preregs',
                            'Q048-F-01-fath-root-density-prereg.md')
EXPECTED_SHA = "263b58105397cb13f1ec36ad5faeac1f7603c21fc10ba57a0027b37c5696f511"
SEED = 20260509
N_PERM = 10000

QAC_PATH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv', 'Q048-F-01.json')


def verify_prereg_sha():
    with open(PRE_REG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        print(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {sha}", file=sys.stderr)
        sys.exit(1)
    return sha


def load_qac_root_tokens():
    """Return (per_surah_root_counts, per_surah_total) where per_surah_root_counts[s][root] is count.
    A token counts toward per_surah_total iff it has a ROOT: feature."""
    per_surah_root_counts = defaultdict(lambda: defaultdict(int))
    per_surah_total = defaultdict(int)
    with open(QAC_PATH) as f:
        for ln in f:
            if ln.startswith('#') or not ln.strip() or ln.startswith('LOCATION'):
                continue
            parts = ln.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            loc, form, tag, features = parts[0], parts[1], parts[2], parts[3]
            if 'ROOT:' not in features:
                continue
            surah = int(loc.strip('()').split(':')[0])
            root = features.split('ROOT:')[1].split('|')[0]
            per_surah_root_counts[surah][root] += 1
            per_surah_total[surah] += 1
    return per_surah_root_counts, per_surah_total


def hypergeometric_pvalue(N, K, n, k):
    """P(X >= k | hypergeometric(N, K, n))."""
    if k > min(n, K):
        return 0.0
    p = 0.0
    for i in range(k, min(n, K) + 1):
        p += comb(K, i) * comb(N - K, n - i) / comb(N, n)
    return p


def permutation_test(N, K, n, k, n_perm, seed):
    """Empirical permutation: distribute K successes uniformly over N positions; sample n positions; count >= k."""
    rng = random.Random(seed)
    cnt = 0
    for _ in range(n_perm):
        # Hypergeometric draw via random sampling without replacement
        # Equivalent: choose K success-positions from N, then check overlap with n sample-positions
        # More efficient: generate sample of n positions, compute overlap with success-set
        # We'll do: randomly choose n positions (the "Q48 slot"); count how many of K successes fall there
        sample_set = set(rng.sample(range(N), n))
        successes_in_sample = sum(1 for j in rng.sample(range(N), K) if j in sample_set)
        # Above is wrong - rewrite:
        break

    # Cleaner: just compute the empirical hypergeometric via sampling.
    cnt = 0
    for _ in range(n_perm):
        # Randomly pick K positions from N; count overlap with first-n positions (or any fixed n positions; symmetric)
        chosen = set(rng.sample(range(N), K))
        # overlap with positions 0..n-1
        overlap = sum(1 for x in chosen if x < n)
        if overlap >= k:
            cnt += 1
    return (cnt + 1) / (n_perm + 1)  # add-1 smoothing


def main():
    sha = verify_prereg_sha()
    print(f"Pre-reg SHA verified: {sha}")

    rng = random.Random(SEED)

    per_root, per_total = load_qac_root_tokens()

    # Total corpus
    total_tokens = sum(per_total.values())
    total_ftH = sum(per_root[s].get('ftH', 0) for s in per_root)

    # Q 48
    q48_tokens = per_total[48]
    q48_ftH = per_root[48].get('ftH', 0)

    # Hypergeometric
    p_hyp = hypergeometric_pvalue(total_tokens, total_ftH, q48_tokens, q48_ftH)

    # Permutation
    p_perm = permutation_test(total_tokens, total_ftH, q48_tokens, q48_ftH, N_PERM, SEED)

    # Per-surah density rank (length-controlled, ≥ 100 root-tokens)
    surah_data = []
    for s in range(1, 115):
        tk = per_total.get(s, 0)
        if tk >= 100:
            ftH = per_root[s].get('ftH', 0)
            surah_data.append({'surah': s, 'ftH': ftH, 'tokens': tk, 'density': ftH / tk})

    sorted_density = sorted(surah_data, key=lambda x: -x['density'])
    rank_density = next(i + 1 for i, x in enumerate(sorted_density) if x['surah'] == 48)
    n_eligible = len(sorted_density)

    # All-surah rank by absolute count
    all_surah = []
    for s in range(1, 115):
        ftH = per_root[s].get('ftH', 0)
        all_surah.append({'surah': s, 'ftH': ftH})
    all_sorted = sorted(all_surah, key=lambda x: -x['ftH'])
    rank_count = next(i + 1 for i, x in enumerate(all_sorted) if x['surah'] == 48)

    # Expected under uniform corpus rate
    expected = q48_tokens * (total_ftH / total_tokens)
    enrichment = q48_ftH / expected if expected else float('inf')

    # Verdict
    primary_pass = (p_hyp <= 0.05 and rank_density <= 3)
    directional_pass = (p_hyp <= 0.05 or rank_density <= 3)
    if primary_pass:
        verdict = "PASS-DIRECTED"  # post-hoc-cap per HANDOFF/04-DISCIPLINE
    elif directional_pass:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    result = {
        "test_id": "Q048-F-01",
        "H_NEW": "H-NEW-1260",
        "title": "Q 48 al-Fatḥ — corpus-EXACT *fatḥ* root-density signature",
        "pre_reg_sha": sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, QAC-v0.4-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "alpha_bon": 0.05,
        "bonferroni_k": 1,
        "corpus_stats": {
            "total_root_tagged_tokens": total_tokens,
            "total_ftH_tokens": total_ftH,
            "corpus_ftH_rate": total_ftH / total_tokens,
        },
        "q48_stats": {
            "q48_root_tagged_tokens": q48_tokens,
            "q48_ftH_tokens": q48_ftH,
            "q48_ftH_density": q48_ftH / q48_tokens,
            "expected_under_corpus_rate": expected,
            "enrichment_factor": enrichment,
        },
        "rank_density_length_controlled": {
            "rank": rank_density,
            "of_total": n_eligible,
            "filter": ">=100 root-tagged tokens",
            "top_5": sorted_density[:5],
        },
        "rank_count_all_surahs": rank_count,
        "p_hypergeometric": p_hyp,
        "p_permutation": p_perm,
        "primary_pass": primary_pass,
        "directional_pass": directional_pass,
        "verdict": verdict,
        "verdict_ceiling": "PASS-DIRECTED",
        "honest_limits": [
            "Brief stated 5 fatḥ occurrences; on-disk QAC v0.4 returns 4 root-tokens / 3 verses. Corrected count used here.",
            "Q 48 is NAMED for this root, so the test is in some sense tautological. Empirical contribution = quantifying the magnitude.",
            "Test is post-hoc-noticed; verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION on a distinct dimension.",
            "Replication candidate: orthographic substring فتح count (different operationalization).",
        ],
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Result written to {OUT_PATH}")
    print(f"Verdict: {verdict}")
    print(f"  Q48 ftH tokens: {q48_ftH} (corpus: {total_ftH}; corpus_rate: {total_ftH/total_tokens:.6f})")
    print(f"  enrichment: {enrichment:.2f}x")
    print(f"  hypergeometric p: {p_hyp:.6e}")
    print(f"  permutation p: {p_perm:.6e}")
    print(f"  density rank (length-controlled): {rank_density}/{n_eligible}")
    print(f"  count rank (all 114): {rank_count}/114")


if __name__ == "__main__":
    main()
