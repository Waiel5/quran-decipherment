#!/usr/bin/env python3
"""Q021-F-04 — Q 21:30-33 cosmological-cluster cohesion test.

Pre-reg: surahs/Q021-al-anbiya/Q021-F-04-cosmological-cluster-prereg.md
Pre-reg SHA-256 (locked): 849143dd5a63399a9deb1f1782ae90fa7ba340267d8b0276f5389e4d9ce1c4cc
Direction (locked): HIGHER (vv. 30-33 mean pairwise cohesion > permutation null).
Bonferroni k=1, α=0.05, seed=20260507.
"""
import hashlib
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q021-al-anbiya/Q021-F-04-cosmological-cluster-prereg.md'
EXPECTED_SHA = '849143dd5a63399a9deb1f1782ae90fa7ba340267d8b0276f5389e4d9ce1c4cc'
QAC = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
OUT = ROOT / 'surahs/Q021-al-anbiya/csv/Q021-F-04.json'
SEED = 20260507
N_PERMS = 10000

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: got {sha}, expected {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

# Build per-Q21-verse root multiset from QAC
LOC = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_verse_roots = defaultdict(list)  # vid -> list of roots
all_roots = set()
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
        if sid != 21:
            continue
        vid = int(m.group(2))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        root = rm.group(1)
        per_verse_roots[vid].append(root)
        all_roots.add(root)

n_verses = max(per_verse_roots.keys())
print(f'Q21 verses with roots: {len(per_verse_roots)}, max vid={n_verses}', file=sys.stderr)

# Verse vectors (count) over the all_roots vocabulary
roots_list = sorted(all_roots)
root_idx = {r: i for i, r in enumerate(roots_list)}

verse_vec = {}
for v in per_verse_roots:
    counter = Counter(per_verse_roots[v])
    vec = [0] * len(roots_list)
    for r, c in counter.items():
        vec[root_idx[r]] = c
    verse_vec[v] = vec


def cosine(a, b):
    num = sum(x * y for x, y in zip(a, b))
    da = math.sqrt(sum(x * x for x in a))
    db = math.sqrt(sum(x * x for x in b))
    if da == 0 or db == 0:
        return 0.0
    return num / (da * db)


def mean_pairwise_cosine(verses):
    """Mean pairwise cosine sim over a list of verse ids (size 4)."""
    sims = []
    for i in range(len(verses)):
        for j in range(i + 1, len(verses)):
            v1 = verse_vec.get(verses[i])
            v2 = verse_vec.get(verses[j])
            if v1 is None or v2 is None:
                continue
            sims.append(cosine(v1, v2))
    if not sims:
        return 0.0
    return sum(sims) / len(sims)


# Observed: vv. 30-33
target_block = [30, 31, 32, 33]
observed = mean_pairwise_cosine(target_block)
print(f'observed mean pairwise cosine (vv. 30-33) = {observed:.4f}', file=sys.stderr)

# Permutation null A: random contiguous 4-verse blocks
random.seed(SEED)
contig_null = []
all_verses = sorted(per_verse_roots.keys())
max_start = max(all_verses) - 3
for _ in range(N_PERMS):
    start = random.randint(min(all_verses), max_start)
    block = [v for v in (start, start + 1, start + 2, start + 3) if v in verse_vec]
    if len(block) < 4:
        continue
    contig_null.append(mean_pairwise_cosine(block))

p_contig = sum(1 for x in contig_null if x >= observed) / len(contig_null)

# Permutation null B: random non-contiguous 4-verse samples
non_contig_null = []
for _ in range(N_PERMS):
    block = random.sample(all_verses, 4)
    non_contig_null.append(mean_pairwise_cosine(block))

p_non_contig = sum(1 for x in non_contig_null if x >= observed) / len(non_contig_null)

# Verdict
if p_contig <= 0.05 and p_non_contig <= 0.05:
    verdict = 'CONFIRMED'
elif (p_contig <= 0.10) or (p_non_contig <= 0.05):
    verdict = 'DIRECTIONAL'
else:
    verdict = 'NULL'

# Sanity: which roots dominate the cluster?
cluster_roots = Counter()
for v in target_block:
    if v in per_verse_roots:
        cluster_roots.update(per_verse_roots[v])

result = {
    'test_id': 'Q021-F-04',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'seed': SEED,
    'n_perms': N_PERMS,
    'target_block_verses': target_block,
    'observed_mean_pairwise_cosine': observed,
    'contig_null_mean': sum(contig_null) / len(contig_null) if contig_null else None,
    'contig_null_median': sorted(contig_null)[len(contig_null) // 2] if contig_null else None,
    'p_one_sided_contig': p_contig,
    'non_contig_null_mean': sum(non_contig_null) / len(non_contig_null) if non_contig_null else None,
    'non_contig_null_median': sorted(non_contig_null)[len(non_contig_null) // 2] if non_contig_null else None,
    'p_one_sided_non_contig': p_non_contig,
    'cluster_top_roots': cluster_roots.most_common(15),
    'direction_locked': 'HIGHER (vv. 30-33 cohesion > null)',
    'direction_pass': observed > (sum(contig_null) / len(contig_null) if contig_null else 0),
    'bonferroni_k': 1,
    'alpha_bon': 0.05,
    'verdict': verdict
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q021-F-04: observed = {observed:.4f}', file=sys.stderr)
print(f'  p_contig = {p_contig:.4f}, p_non_contig = {p_non_contig:.4f}', file=sys.stderr)
print(f'  verdict: {verdict}', file=sys.stderr)
