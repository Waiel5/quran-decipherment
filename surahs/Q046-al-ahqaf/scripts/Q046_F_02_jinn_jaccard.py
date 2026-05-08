#!/usr/bin/env python3
"""
Q046-F-02 — Q 46:29-32 ↔ Q 72 root-Jaccard with permutation null.

Pre-reg SHA: 9a9b63f5469d9a96006115c7ad96b38161652eaa40b5db3105a022adf04c022a
"""
import json, hashlib, re, random, sys

PREREG = '/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/preregs/Q046-F-02-jinn-listening-jaccard-prereg.md'
EXPECTED_SHA = '9a9b63f5469d9a96006115c7ad96b38161652eaa40b5db3105a022adf04c022a'
OUT = '/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/csv/Q046-F-02.json'
SEED = 20260428
N_PERM = 10000

actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA} got {actual}')

mph = open('/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt').read()

# Build (surah, verse) -> set of roots
verse_roots = {}
for line in mph.split('\n'):
    m = re.match(r'\((\d+):(\d+):\d+:\d+\)', line)
    if not m:
        continue
    s, v = int(m.group(1)), int(m.group(2))
    rm = re.search(r'ROOT:(\S+?)(?:\||$)', line)
    if rm:
        verse_roots.setdefault((s, v), set()).add(rm.group(1))

def union_roots(verses_iter):
    out = set()
    for k in verses_iter:
        out |= verse_roots.get(k, set())
    return out

# Q 46:29-32 root set
q46_2932 = union_roots([(46, v) for v in [29, 30, 31, 32]])

# Q 72 root set
q72_verses = [v for (s, v) in verse_roots.keys() if s == 72]
q72 = union_roots([(72, v) for v in q72_verses])

inter = q46_2932 & q72
union = q46_2932 | q72
observed_jacc = len(inter) / len(union)

# Permutation null: random 4-contiguous-verse windows from Q 46 (excluding [29,30,31,32])
n_q46 = max(v for (s, v) in verse_roots.keys() if s == 46)  # 35
rng = random.Random(SEED)
null_jaccs = []
attempts = 0
while len(null_jaccs) < N_PERM and attempts < N_PERM * 4:
    start = rng.randint(1, n_q46 - 3)
    window = list(range(start, start + 4))
    attempts += 1
    # Exclude window that overlaps [29,30,31,32]
    if any(v in window for v in [29, 30, 31, 32]):
        continue
    sample_roots = union_roots([(46, v) for v in window])
    if not sample_roots:
        continue
    null_inter = sample_roots & q72
    null_union = sample_roots | q72
    if not null_union:
        continue
    null_jaccs.append(len(null_inter) / len(null_union))

null_jaccs.sort()
n_null = len(null_jaccs)
n_ge = sum(1 for v in null_jaccs if v >= observed_jacc)
p_perm = n_ge / n_null
median_null = null_jaccs[n_null // 2]
mean_null = sum(null_jaccs) / n_null

direction_match = observed_jacc > median_null

if direction_match and p_perm < 0.05:
    verdict = 'VINDICATED'
elif direction_match:
    verdict = 'DIRECTIONAL'
else:
    verdict = 'NULL with pre-commit violation'

# Top shared roots
shared_root_list = sorted(inter)

result = {
    'finding_id': 'Q046-F-02',
    'prereg_sha_expected': EXPECTED_SHA,
    'prereg_sha_actual': actual,
    'sha_match': True,
    'seed': SEED,
    'n_perm': n_null,
    'q46_2932_root_count': len(q46_2932),
    'q72_root_count': len(q72),
    'intersection_count': len(inter),
    'union_count': len(union),
    'observed_jaccard': observed_jacc,
    'null_mean_jaccard': mean_null,
    'null_median_jaccard': median_null,
    'p_perm_one_sided': p_perm,
    'direction_match': direction_match,
    'verdict': verdict,
    'shared_roots': shared_root_list,
    'rules_tuple': '(no-tashkeel, QAC-stem-root, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
}

import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print(f'WROTE {OUT}')
print(f'Observed Jaccard: {observed_jacc:.4f}')
print(f'Null median: {median_null:.4f}; null mean: {mean_null:.4f}')
print(f'p_perm: {p_perm:.4f}')
print(f'Verdict: {verdict}')
