#!/usr/bin/env python3
"""Q021-F-02 — Prophet-order distance: Q 21 vs Q 6 vs {Q 11, Q 26, Q 37}.

Pre-reg: surahs/Q021-al-anbiya/Q021-F-02-prophet-order-distance-prereg.md
Pre-reg SHA-256 (locked): 780454a427c82c582d9d9987251e4a4b9f44c61b861b495b9a01e83d46174fdf
Direction (locked): mean(d(Q21,Q11), d(Q21,Q26), d(Q21,Q37)) < d(Q21,Q6).
Bonferroni k=3, α=0.0167, seed=20260507.
"""
import hashlib
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q021-al-anbiya/Q021-F-02-prophet-order-distance-prereg.md'
EXPECTED_SHA = '780454a427c82c582d9d9987251e4a4b9f44c61b861b495b9a01e83d46174fdf'
QAC = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
OUT = ROOT / 'surahs/Q021-al-anbiya/csv/Q021-F-02.json'
SEED = 20260507
N_PERMS = 10000

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: got {sha}, expected {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

PROPHET_LEMMAS = {
    'A^dam', 'nuwH', '<iboraAhiym', '<isomaAEiyl', '<isoHaAq', 'yaEoquwb', 'yuwsuf',
    'luwT', 'huwd', 'Sa`liH2', '$uEayob', 'muwsaY`', 'ha`ruwn', 'daAwud', 'sulayoma`n',
    '<iloyaAs', '<aloyasaE', 'yuwnus', 'zakariy~aA', 'yaHoyaY`', 'EiysaY`', '<idoriys',
    '>ay~uwb', 'muHam~ad', '>aHomad'
}

LOC = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')

# Build first-occurrence prophet order per surah
per_surah_order = defaultdict(list)
seen = defaultdict(set)
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
        sid, vid, wid = int(m.group(1)), int(m.group(2)), int(m.group(3))
        feat = parts[3]
        if 'POS:PN' not in feat:
            continue
        lm = re.search(r'LEM:([^|]+)', feat)
        if not lm:
            continue
        lem = lm.group(1)
        if lem not in PROPHET_LEMMAS:
            continue
        if lem in seen[sid]:
            continue
        seen[sid].add(lem)
        per_surah_order[sid].append(lem)


def kendall_tau_distance_normalized(order_a, order_b):
    """Distance on the COMMON subset.

    Both orders are list of items (some shared). Restrict each to the common subset
    preserving original order. Then count inversions / max-inversions on the common subset.
    """
    common = set(order_a) & set(order_b)
    if len(common) < 2:
        return None, len(common)
    a = [x for x in order_a if x in common]
    b = [x for x in order_b if x in common]
    # rank of each item in b
    rank_b = {x: i for i, x in enumerate(b)}
    n = len(a)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if rank_b[a[i]] > rank_b[a[j]]:
                inv += 1
    max_inv = n * (n - 1) // 2
    return inv / max_inv, n


# Compute distances
q21 = per_surah_order[21]
q6 = per_surah_order[6]
q11 = per_surah_order[11]
q26 = per_surah_order[26]
q37 = per_surah_order[37]

d_q21_q6, n_a = kendall_tau_distance_normalized(q21, q6)
d_q21_q11, n_b = kendall_tau_distance_normalized(q21, q11)
d_q21_q26, n_c = kendall_tau_distance_normalized(q21, q26)
d_q21_q37, n_d = kendall_tau_distance_normalized(q21, q37)

# Permutation null on Q 21's order
random.seed(SEED)
perm_diffs = []
for _ in range(N_PERMS):
    shuffled = q21.copy()
    random.shuffle(shuffled)
    a = kendall_tau_distance_normalized(shuffled, q6)[0]
    b = kendall_tau_distance_normalized(shuffled, q11)[0]
    c = kendall_tau_distance_normalized(shuffled, q26)[0]
    d = kendall_tau_distance_normalized(shuffled, q37)[0]
    if None in (a, b, c, d):
        continue
    perm_diffs.append((b + c + d) / 3 - a)

# Observed
obs_diff = ((d_q21_q11 + d_q21_q26 + d_q21_q37) / 3) - d_q21_q6
# one-sided p (H1: obs_diff < 0; null = symmetric around ~0)
p_one_sided = sum(1 for x in perm_diffs if x <= obs_diff) / len(perm_diffs)

# Per-cell tests against Q6 baseline
cell_b_pass = (d_q21_q11 < d_q21_q6) if d_q21_q11 is not None else None
cell_c_pass = (d_q21_q26 < d_q21_q6) if d_q21_q26 is not None else None
cell_d_pass = (d_q21_q37 < d_q21_q6) if d_q21_q37 is not None else None
n_cells_pass = sum(1 for x in (cell_b_pass, cell_c_pass, cell_d_pass) if x)

# Verdict
direction_pass = obs_diff < 0
if direction_pass and n_cells_pass >= 2 and p_one_sided <= 0.0167:
    verdict = 'CONFIRMED'
elif direction_pass and (n_cells_pass >= 1 or p_one_sided <= 0.0167):
    verdict = 'DIRECTIONAL'
else:
    verdict = 'NULL'

result = {
    'test_id': 'Q021-F-02',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'seed': SEED,
    'n_perms': N_PERMS,
    'direction_locked': 'mean(d(Q21,Q11), d(Q21,Q26), d(Q21,Q37)) < d(Q21,Q6)',
    'q21_order': q21,
    'q6_order': q6,
    'q11_order': q11,
    'q26_order': q26,
    'q37_order': q37,
    'd_q21_q6': d_q21_q6,
    'common_size_q6': n_a,
    'd_q21_q11': d_q21_q11,
    'common_size_q11': n_b,
    'd_q21_q26': d_q21_q26,
    'common_size_q26': n_c,
    'd_q21_q37': d_q21_q37,
    'common_size_q37': n_d,
    'mean_alt_distance': (d_q21_q11 + d_q21_q26 + d_q21_q37) / 3,
    'observed_diff': obs_diff,
    'permutation_p_one_sided': p_one_sided,
    'cell_b_q11_closer_than_q6': cell_b_pass,
    'cell_c_q26_closer_than_q6': cell_c_pass,
    'cell_d_q37_closer_than_q6': cell_d_pass,
    'n_cells_passing_direction': n_cells_pass,
    'bonferroni_k': 3,
    'alpha_bon': 0.0167,
    'direction_pass': direction_pass,
    'verdict': verdict
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q021-F-02: d(Q21,Q6)={d_q21_q6:.3f}, mean_alt={result["mean_alt_distance"]:.3f}', file=sys.stderr)
print(f'  diff={obs_diff:.3f}, p_perm={p_one_sided:.4f}, cells_pass={n_cells_pass}/3', file=sys.stderr)
print(f'  verdict: {verdict}', file=sys.stderr)
