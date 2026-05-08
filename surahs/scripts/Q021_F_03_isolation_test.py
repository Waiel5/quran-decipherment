#!/usr/bin/env python3
"""Q021-F-03 — True-isolate lexical dispersion: Q 21 mean d to 5 nearest neighbors.

Pre-reg: surahs/Q021-al-anbiya/Q021-F-03-isolation-prereg.md
Pre-reg SHA-256 (locked): 16d48c7847fcb704f6588ce04df6239df227c529b1608616d1ca283bdee27587
Direction (locked): HIGHER (Q 21 above corpus median for mean-d-to-5-nearest).
Bonferroni k=1, α=0.05, seed=20260507.

Pipeline (matches H-NEW-111):
  - QAC v0.4 STEM ROOT counts per surah
  - Top-K=500 root selection (frequency)
  - Dirichlet α=0.5 smoothing
  - L1-normalize to probability vectors
  - Pairwise Fisher-Rao distance
  - Per-surah mean distance to 5 nearest neighbors
"""
import hashlib
import json
import math
import re
import sys
import statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q021-al-anbiya/Q021-F-03-isolation-prereg.md'
EXPECTED_SHA = '16d48c7847fcb704f6588ce04df6239df227c529b1608616d1ca283bdee27587'
QAC = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
OUT = ROOT / 'surahs/Q021-al-anbiya/csv/Q021-F-03.json'

K_TOP = 500
DIRICHLET = 0.5

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: got {sha}, expected {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

LOC = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_surah_roots = defaultdict(list)
global_counts = Counter()
with open(QAC, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip().split('\t')
        if len(parts) < 4:
            continue
        m = LOC.match(parts[0])
        if not m:
            continue
        sid = int(m.group(1))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        root = rm.group(1)
        per_surah_roots[sid].append(root)
        global_counts[root] += 1

# Top-K
top_roots = [r for r, _ in global_counts.most_common(K_TOP)]
top_idx = {r: i for i, r in enumerate(top_roots)}

# Per-surah probability vector
probs = [None] * 115
for s in range(1, 115):
    counts = [0.0] * K_TOP
    for r in per_surah_roots[s]:
        idx = top_idx.get(r)
        if idx is not None:
            counts[idx] += 1.0
    smoothed = [c + DIRICHLET for c in counts]
    total = sum(smoothed)
    probs[s] = [v / total for v in smoothed]


def fisher_rao(p, q):
    s = 0.0
    for a, b in zip(p, q):
        s += math.sqrt(a * b)
    s = max(-1.0, min(1.0, s))
    return 2.0 * math.acos(s)


# Pairwise distances (full 114x114 — needed for per-surah mean-d-to-5-nearest)
dist = [[0.0] * 115 for _ in range(115)]
for i in range(1, 115):
    for j in range(i + 1, 115):
        d = fisher_rao(probs[i], probs[j])
        dist[i][j] = d
        dist[j][i] = d

# Per-surah mean-d-to-5-nearest
mean5 = {}
nearest_lists = {}
for s in range(1, 115):
    others = sorted([(dist[s][t], t) for t in range(1, 115) if t != s])[:5]
    mean5[s] = statistics.mean(d for d, _ in others)
    nearest_lists[s] = [t for _, t in others]

# Q 21 specifically
q21_mean5 = mean5[21]
q21_nearest = nearest_lists[21]

# Rank Q 21 (higher = more isolated)
ranked = sorted(mean5.items(), key=lambda x: -x[1])  # most-isolated first
q21_rank_isolation = next(i for i, (s, _) in enumerate(ranked) if s == 21) + 1
q21_pct = (114 - q21_rank_isolation + 1) / 114 * 100  # higher percentile = more isolated

corpus_median = statistics.median(mean5.values())
corpus_mean = statistics.mean(mean5.values())
above_median = q21_mean5 > corpus_median

# Verdict
if q21_rank_isolation <= 30:
    verdict = 'CONFIRMED'  # top-30 most isolated
elif above_median:
    verdict = 'DIRECTIONAL'
else:
    verdict = 'NULL'
direction_pass = above_median

# Top 15 most-isolated for context
top15 = ranked[:15]
# Bottom 5 (least isolated)
bottom5 = ranked[-5:]

# Also compute Q 21 mean-d to entire corpus and farthest-5
all_d_q21 = sorted([(dist[21][t], t) for t in range(1, 115) if t != 21])
q21_mean_corpus = statistics.mean(d for d, _ in all_d_q21)
q21_farthest_5 = sorted([(dist[21][t], t) for t in range(1, 115) if t != 21], reverse=True)[:5]

# Other true-isolate cluster surahs ranks
isolate_cluster = {16, 21, 22, 23, 25}
isolate_ranks = {}
for s in isolate_cluster:
    rk = next(i for i, (ss, _) in enumerate(ranked) if ss == s) + 1
    isolate_ranks[s] = {'rank': rk, 'mean5': mean5[s]}

result = {
    'test_id': 'Q021-F-03',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'rules_tuple': '(QAC-v0.4-STEM-roots, top-K=500, Dirichlet-α=0.5, L1-normalize, Fisher-Rao, no-tashkeel)',
    'K_TOP': K_TOP,
    'DIRICHLET': DIRICHLET,
    'q21_mean_d_to_5_nearest': q21_mean5,
    'q21_5_nearest_surahs': q21_nearest,
    'q21_5_nearest_with_distance': [{'surah': t, 'd': dist[21][t]} for t in q21_nearest],
    'q21_5_farthest_with_distance': [{'surah': t, 'd': d} for d, t in q21_farthest_5],
    'q21_mean_d_to_corpus': q21_mean_corpus,
    'q21_isolation_rank': q21_rank_isolation,
    'q21_isolation_percentile': q21_pct,
    'corpus_median_mean5': corpus_median,
    'corpus_mean_mean5': corpus_mean,
    'q21_above_corpus_median': above_median,
    'top_15_most_isolated': [{'surah': s, 'mean5': v} for s, v in top15],
    'bottom_5_least_isolated': [{'surah': s, 'mean5': v} for s, v in bottom5],
    'true_isolate_cluster_ranks': isolate_ranks,
    'direction_locked': 'HIGHER (Q21 above corpus median)',
    'direction_pass': direction_pass,
    'bonferroni_k': 1,
    'alpha_bon': 0.05,
    'verdict': verdict
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q021-F-03: Q21 mean-d-to-5-nearest = {q21_mean5:.4f}', file=sys.stderr)
print(f'  isolation rank = {q21_rank_isolation}/114, percentile = {q21_pct:.1f}', file=sys.stderr)
print(f'  corpus median = {corpus_median:.4f}', file=sys.stderr)
print(f'  Q21 5 nearest: {q21_nearest}', file=sys.stderr)
print(f'  verdict: {verdict}', file=sys.stderr)
