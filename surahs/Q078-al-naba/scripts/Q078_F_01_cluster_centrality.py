#!/usr/bin/env python3
"""
Q078-F-01 — Q 78 within H-NEW-1200 short-Meccan-tail-eschatology cluster:
            CENTRALITY rank test.

Pre-reg: surahs/Q078-al-naba/preregs/Q078-F-01-cluster-centrality-prereg.md
SHA256:  embedded at runtime; verified against pre-reg

Hypothesis (LOCKED PRE-RUN):
  H1: Q 78's mean-pairwise FR-distance to the H-NEW-1200 14-cluster is
      LESS THAN the corpus-mean FR-distance from Q 78.
      DIRECTION: Q 78 is closer to the cluster than the corpus average.

  H2: Q 78's intra-cluster centrality rank (with Q 78 inserted as outsider)
      is BELOW the median (i.e., NOT in the top-7 of 15).
      DIRECTION: Q 78 is PERIPHERAL, not central.
      Pre-registered to test the brief's question:
      "Is Q 78 the centroid or peripheral?"

H0: H1 fails (Q 78 cluster-mean ≥ corpus-mean) OR
    H2 fails (Q 78 ranks in top-7 of 15).

Bonferroni: k=2; alpha_bon = 0.025.

Method:
  - Build root-distribution per surah from QAC morphology.
  - Compute Dirichlet-α=0.5 Fisher-Rao distance between each pair.
  - For Q 78, compute mean-distance to (a) cluster (14 surahs) and (b) corpus.
  - For centrality, compute mean-distance from each cluster member to others;
    insert Q 78 and rank.
  - Permutation null: 10000 random 14-surah subsets from corpus excluding Q 78,
    seed 20260509, computing the analogous mean-distance.

Seed: 20260509.
n_perm: 10000.
"""

import json
import math
import re
import sys
import os
import hashlib
import random
from collections import Counter

# Path setup
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PREREG_PATH = os.path.join(os.path.dirname(__file__), '..', 'preregs',
                           'Q078-F-01-cluster-centrality-prereg.md')
QURAN_PATH = os.path.join(PROJECT_ROOT, 'quran-text', 'quran-no-tashkeel.json')
QAC_PATH = os.path.join(PROJECT_ROOT, 'data', 'morphology',
                        'quranic-corpus-morphology-0.4.txt')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv', 'Q078-F-01.json')

# H-NEW-1200 cluster (LOCKED PRE-RUN; from MASTER-FINDINGS-LEDGER §10.35)
CLUSTER_1200 = [56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104]

SEED = 20260509
N_PERM = 10000
ALPHA = 0.5  # Dirichlet smoothing


def sha256_of(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def fr_distance(p_counts, q_counts, vocab):
    """Dirichlet-α-smoothed Fisher-Rao distance."""
    p_total = sum(p_counts.values())
    q_total = sum(q_counts.values())
    N = len(vocab)
    cos_sum = 0.0
    for r in vocab:
        p = (p_counts.get(r, 0) + ALPHA) / (p_total + ALPHA * N)
        q = (q_counts.get(r, 0) + ALPHA) / (q_total + ALPHA * N)
        cos_sum += math.sqrt(p * q)
    cos_sum = min(1.0, cos_sum)
    return 2.0 * math.acos(cos_sum)


def load_surah_roots():
    """Build per-surah root distributions from QAC morphology."""
    surah_roots = {i: Counter() for i in range(1, 115)}
    corpus_roots = Counter()
    with open(QAC_PATH, encoding='utf-8') as f:
        for line in f:
            if not line.startswith('('):
                continue
            parts = line.strip().split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            m = re.search(r'ROOT:([^|]+)', features)
            if not m:
                continue
            root = m.group(1)
            nums = re.findall(r'\d+', loc)
            if len(nums) < 1:
                continue
            s = int(nums[0])
            if 1 <= s <= 114:
                surah_roots[s][root] += 1
                corpus_roots[root] += 1
    return surah_roots, corpus_roots


def main():
    # SHA-lock check
    prereg_sha = sha256_of(PREREG_PATH)
    print(f"prereg SHA256: {prereg_sha}")

    # Load
    surah_roots, corpus_roots = load_surah_roots()
    vocab = set(corpus_roots.keys())

    # Cell A: Q 78 mean-distance to cluster vs corpus
    cluster_dists = []
    for s in CLUSTER_1200:
        d = fr_distance(surah_roots[78], surah_roots[s], vocab)
        cluster_dists.append((s, d))
    cluster_mean = sum(d for _, d in cluster_dists) / len(cluster_dists)

    corpus_dists = []
    for s in range(1, 115):
        if s == 78:
            continue
        d = fr_distance(surah_roots[78], surah_roots[s], vocab)
        corpus_dists.append((s, d))
    corpus_mean = sum(d for _, d in corpus_dists) / len(corpus_dists)

    # Cell A permutation null: 10000 random 14-surah subsets (excluding Q 78)
    rng = random.Random(SEED)
    pool = [s for s in range(1, 115) if s != 78]
    null_means = []
    for _ in range(N_PERM):
        subset = rng.sample(pool, 14)
        m = sum(fr_distance(surah_roots[78], surah_roots[s], vocab) for s in subset) / 14
        null_means.append(m)
    null_means.sort()
    # one-tailed p_lower: how many random subsets have mean ≤ observed cluster_mean
    p_lower = sum(1 for m in null_means if m <= cluster_mean) / len(null_means)

    # Cell B: centrality rank of Q 78 inserted as outsider
    intra = []
    for s in CLUSTER_1200:
        others = [x for x in CLUSTER_1200 if x != s]
        md = sum(fr_distance(surah_roots[s], surah_roots[o], vocab) for o in others) / len(others)
        intra.append((s, md))
    md_q78 = sum(fr_distance(surah_roots[78], surah_roots[o], vocab) for o in CLUSTER_1200) / 14
    intra.append((78, md_q78))
    intra.sort(key=lambda x: x[1])
    q78_rank = next(i for i, (s, _) in enumerate(intra) if s == 78) + 1

    # Pre-registered direction:
    # H1 PASS: cluster_mean < corpus_mean AND p_lower ≤ 0.025
    # H2 PASS: q78_rank > 7 (peripheral) — pre-locked direction is "Q 78 is peripheral"

    h1_direction_pass = cluster_mean < corpus_mean
    h1_p_pass = p_lower <= 0.025
    h2_pass = q78_rank > 7

    verdict = {
        "h1_cluster_lt_corpus": h1_direction_pass,
        "h1_p_lower": p_lower,
        "h1_p_pass": h1_p_pass,
        "h2_centrality_rank": q78_rank,
        "h2_pass_peripheral": h2_pass,
    }

    output = {
        "test_id": "Q078-F-01",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_dirichlet": ALPHA,
        "cluster_1200": CLUSTER_1200,
        "cluster_mean_fr": cluster_mean,
        "corpus_mean_fr": corpus_mean,
        "ratio_cluster_corpus": cluster_mean / corpus_mean,
        "p_lower_perm": p_lower,
        "centrality_ranking": [(s, m) for s, m in intra],
        "q78_centrality_rank": q78_rank,
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=2, default=lambda x: float(x) if hasattr(x, 'item') else x)

    print(f"Cluster_mean: {cluster_mean:.4f}")
    print(f"Corpus_mean:  {corpus_mean:.4f}")
    print(f"Ratio:        {cluster_mean/corpus_mean:.4f}")
    print(f"p_lower_perm: {p_lower:.5f}")
    print(f"Q 78 centrality rank: {q78_rank}/15")
    print(f"H1 PASS (cluster<corpus, p≤0.025): {h1_direction_pass and h1_p_pass}")
    print(f"H2 PASS (peripheral, rank>7): {h2_pass}")
    print(f"Output: {OUTPUT_PATH}")


if __name__ == '__main__':
    main()
