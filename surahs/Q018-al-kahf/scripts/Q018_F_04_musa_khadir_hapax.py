#!/usr/bin/env python3
"""Q018-F-04: Mūsā-Khaḍir block (N3, vv. 60-82) lexical hapax signature (LOCKED pre-reg).

Tests whether N3's block-internal-hapax count exceeds random 23-verse-span baseline.
"""
import json, re, hashlib, random, os

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q018-al-kahf/preregs/Q018-F-04-musa-khadir-hapax-prereg.md"
QAC = f"{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT = f"{PROJECT}/surahs/Q018-al-kahf/csv/Q018-F-04.json"

SEED = 18004
N_PERM = 10000

sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
print(f"Pre-reg SHA256: {sha}")

# Block boundaries
BLOCKS = {
    'N1_kahf': set(range(9, 27)),
    'N2_gardens': set(range(32, 45)),
    'N3_musa_khadir': set(range(60, 83)),
    'N4_dhu_qarnayn': set(range(83, 102)),
}
ALL_VERSES = set(range(1, 111))
N3 = BLOCKS['N3_musa_khadir']
NON_N3 = ALL_VERSES - N3

# Load Q18 verse roots
verse_roots = {v: set() for v in range(1, 111)}
with open(QAC) as f:
    for line in f:
        if not line.startswith('(18:'): continue
        m = re.match(r'\(18:(\d+):\d+:\d+\)\s+\S+\s+\S+\s+(.*)', line)
        if not m: continue
        v = int(m.group(1))
        feat = m.group(2)
        rm = re.search(r'ROOT:([^|\s]+)', feat)
        if rm:
            verse_roots[v].add(rm.group(1))

# N3-only roots = roots in N3 - roots in everywhere-else-of-Q18
n3_roots = set()
for v in N3:
    n3_roots |= verse_roots[v]
non_n3_roots = set()
for v in NON_N3:
    non_n3_roots |= verse_roots[v]
n3_only = n3_roots - non_n3_roots
print(f'N3 has {len(n3_roots)} distinct roots; {len(non_n3_roots)} in rest of Q 18; N3-only = {len(n3_only)}')
print(f'N3-only roots: {sorted(n3_only)[:30]}')

# Random null: 10000 random samples of 23 verses (any in 1-110), compute roots-only-in-sample
random.seed(SEED)
all_verses_list = list(ALL_VERSES)
null_counts = []
for _ in range(N_PERM):
    sample = set(random.sample(all_verses_list, 23))
    rest = ALL_VERSES - sample
    sample_roots = set()
    rest_roots = set()
    for v in sample:
        sample_roots |= verse_roots[v]
    for v in rest:
        rest_roots |= verse_roots[v]
    only = sample_roots - rest_roots
    null_counts.append(len(only))

null_median = sorted(null_counts)[N_PERM // 2]
null_mean = sum(null_counts) / N_PERM
null_max = max(null_counts)
null_pct95 = sorted(null_counts)[int(0.95 * N_PERM)]
p_value = sum(1 for c in null_counts if c >= len(n3_only)) / N_PERM

print(f'Null distribution: mean={null_mean:.2f}, median={null_median}, p95={null_pct95}, max={null_max}')
print(f'Observed N3-only count: {len(n3_only)}')
print(f'p-value (one-tailed, count >= observed): {p_value:.4f}')

if len(n3_only) < null_median:
    verdict = 'NULL_PRECOMMIT_VIOLATION'
elif p_value < 0.05:
    verdict = 'CONFIRMED'
elif p_value < 0.10:
    verdict = 'DIRECTIONAL'
else:
    verdict = 'NULL'

# Also compute N1, N2, N4 hapax counts for comparative context
def block_hapax(block_set):
    block_roots = set()
    for v in block_set:
        block_roots |= verse_roots[v]
    rest = ALL_VERSES - block_set
    rest_roots = set()
    for v in rest:
        rest_roots |= verse_roots[v]
    return block_roots - rest_roots

n1_only = block_hapax(BLOCKS['N1_kahf'])
n2_only = block_hapax(BLOCKS['N2_gardens'])
n4_only = block_hapax(BLOCKS['N4_dhu_qarnayn'])

result_obj = {
    'finding_id': 'Q018-F-04',
    'pre_reg_sha256': sha,
    'verdict': verdict,
    'n3_only_count': len(n3_only),
    'n3_only_roots': sorted(n3_only),
    'null_mean': null_mean,
    'null_median': null_median,
    'null_p95': null_pct95,
    'null_max': null_max,
    'p_value': p_value,
    'n_perm': N_PERM,
    'seed': SEED,
    'comparator_block_hapax_counts': {
        'N1_kahf_hapax': len(n1_only),
        'N1_kahf_hapax_roots': sorted(n1_only),
        'N2_gardens_hapax': len(n2_only),
        'N2_gardens_hapax_roots': sorted(n2_only),
        'N4_dhu_qarnayn_hapax': len(n4_only),
        'N4_dhu_qarnayn_hapax_roots': sorted(n4_only),
    },
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result_obj, f, indent=2, default=str)
print(f'\nWritten to {OUT}')
