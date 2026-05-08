#!/usr/bin/env python3
"""Q021-F-05 — Q 21 + Q 22 true-isolate joint adjacency test.

Pre-reg: surahs/Q021-al-anbiya/Q021-F-05-true-isolate-adjacency-prereg.md
Pre-reg SHA-256 (locked): 303446650a70ae0dbad6e03200139e8a421a29dd7ee13cd6e5753a124511ad66
Cell A direction (locked): rank of d(Q21,Q22) within 10 within-cluster pairs is LOW
                           (top-half = "structural-coherence").
Cell B direction (locked): rank of TSP-cost in H-NEW-720 is HIGH (above median = "expensive boundary"),
                           pre-observed at rank 16 / 113.
Bonferroni k=2, α=0.025, seed=20260507.
"""
import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q021-al-anbiya/Q021-F-05-true-isolate-adjacency-prereg.md'
EXPECTED_SHA = '303446650a70ae0dbad6e03200139e8a421a29dd7ee13cd6e5753a124511ad66'
QAC = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
H720 = ROOT / 'findings/phase-b-hypotheses/csv/h-new-720.json'
OUT = ROOT / 'surahs/Q021-al-anbiya/csv/Q021-F-05.json'

K_TOP = 500
DIRICHLET = 0.5

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: got {sha}, expected {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

# --- FR-distance pipeline (matches Q021-F-03 / H-NEW-111) ---
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

top_roots = [r for r, _ in global_counts.most_common(K_TOP)]
top_idx = {r: i for i, r in enumerate(top_roots)}

probs = {}
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


# Within-cluster pairwise distances {Q 16, 21, 22, 23, 25}
cluster = [16, 21, 22, 23, 25]
within_pairs = []
for i in range(len(cluster)):
    for j in range(i + 1, len(cluster)):
        a, b = cluster[i], cluster[j]
        d = fisher_rao(probs[a], probs[b])
        within_pairs.append({'pair': [a, b], 'd': d})

# Sort by distance ascending (low rank = nearer pair)
within_sorted = sorted(within_pairs, key=lambda x: x['d'])
for i, p in enumerate(within_sorted):
    p['rank_within_cluster'] = i + 1

# Find Q 21–Q 22 rank within cluster
q21_q22 = next(p for p in within_pairs if set(p['pair']) == {21, 22})
q21_q22_rank = next(p['rank_within_cluster'] for p in within_sorted if set(p['pair']) == {21, 22})

# Cell A: rank ≤ 5 (top-half nearer pairs of 10 — pre-committed direction "LOW")
cell_a_pass = q21_q22_rank <= 5
cell_a_strong = q21_q22_rank == 1  # strongest possible: most-similar pair in cluster

# Cell B: TSP-cost rank from H-NEW-720
with open(H720) as f:
    h720 = json.load(f)
adj = h720['per_adjacency']
adj_ranked = sorted(adj, key=lambda x: -x['fraction_residual'])
q21_q22_tsp_rank = next(i for i, r in enumerate(adj_ranked) if r['pair'] == [21, 22]) + 1
q21_q22_tsp_frac = next(r['fraction_residual'] for r in adj if r['pair'] == [21, 22])
cell_b_pass = q21_q22_tsp_rank < 57  # above median (rank 1=highest cost = ABOVE median)

# Joint interpretation
if cell_a_pass and not cell_b_pass:
    joint = 'STRUCTURAL-COHERENCE'
elif cell_a_pass and cell_b_pass:
    joint = 'INCOHERENT'
elif (not cell_a_pass) and cell_b_pass:
    joint = 'NEAR-NEIGHBOR-BUT-NOT-CLUSTER'
else:
    joint = 'INDEPENDENT'

# Verdict per Bonferroni-2 cells (note: cell B is post-hoc-observed before pre-reg lock per
# disclosure §2 of pre-reg; treated under MW-7 single-test α=0.05 cap, no Bonferroni penalty)
if cell_a_strong and cell_b_pass:
    verdict = 'CONFIRMED-INCOHERENT'  # Most-similar pair in cluster + costly boundary = surprising
elif cell_a_pass:
    verdict = 'DIRECTIONAL-' + joint
else:
    verdict = 'NULL-' + joint

result = {
    'test_id': 'Q021-F-05',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'within_cluster_pairs_sorted': within_sorted,
    'q21_q22_within_cluster_d': q21_q22['d'],
    'q21_q22_within_cluster_rank': q21_q22_rank,
    'q21_q22_within_cluster_n_pairs': 10,
    'cell_a_locked_direction': 'LOW (rank ≤ 5 of 10 within-cluster pairs)',
    'cell_a_pass': cell_a_pass,
    'cell_a_strong_top1': cell_a_strong,
    'q21_q22_tsp_fraction_residual': q21_q22_tsp_frac,
    'q21_q22_tsp_rank_in_h720': q21_q22_tsp_rank,
    'cell_b_locked_direction': 'HIGH-COST (rank < 57 of 113)',
    'cell_b_pass': cell_b_pass,
    'cell_b_pre_observed': True,  # disclosed in pre-reg §2
    'joint_interpretation': joint,
    'bonferroni_k': 2,
    'alpha_bon': 0.025,
    'verdict': verdict,
    'honest_limits': [
        '5-surah within-cluster sample (10 pairs) is small; significance not established by perm null on 10 pairs.',
        'Cell B was already-observed before pre-reg lock; MW-7 caps at α=0.05 single-test, no Bonferroni penalty applied.',
        'STRUCTURAL coherence operationalized as FR + TSP only; rhyme / register / munāsabah-tafsir not jointly tested.',
    ]
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q021-F-05: d(Q21,Q22) = {q21_q22["d"]:.4f}, within-cluster rank {q21_q22_rank}/10', file=sys.stderr)
print(f'  TSP rank {q21_q22_tsp_rank}/113 (frac_residual={q21_q22_tsp_frac:.4f})', file=sys.stderr)
print(f'  joint interpretation: {joint}', file=sys.stderr)
print(f'  verdict: {verdict}', file=sys.stderr)
