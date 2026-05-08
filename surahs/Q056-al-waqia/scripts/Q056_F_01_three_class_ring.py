#!/usr/bin/env python3
"""
Q056-F-01 — 3-class RING ARCHITECTURE test.
SHA-locked pre-reg: f5583581e6b14d2fa19a87fc278463ae2f4f47ab36cbb1fd7dd4cfb51cd6882c
Seed: 20260507; n_perm: 10000; bonferroni_k: 3; alpha_bon: 0.01667
"""
import json, random, hashlib, sys, os, re
from collections import Counter

PREREG_PATH = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/preregs/Q056-F-01-three-class-ring-prereg.md'
EXPECTED_SHA = 'f5583581e6b14d2fa19a87fc278463ae2f4f47ab36cbb1fd7dd4cfb51cd6882c'

with open(PREREG_PATH,'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
assert actual_sha == EXPECTED_SHA, f'PRE-REG SHA MISMATCH: {actual_sha} != {EXPECTED_SHA}'

SEED = 20260507
N_PERM = 10000
random.seed(SEED)

with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
    q = json.load(f)
q56 = q[55]

def tokens_of(verses_range):
    """verses_range is (start, end) inclusive 1-indexed."""
    s, e = verses_range
    toks = []
    for v in q56['verses']:
        if s <= v['id'] <= e:
            toks.extend(v['text'].split())
    return toks

# Block A: full 3-class
A1 = tokens_of((10,26))   # Sābiqūn
A2 = tokens_of((27,40))   # Yamīn
A3 = tokens_of((41,56))   # Shimāl

# Block B: death-moment
B1 = tokens_of((88,89))   # muqarrabīn
B2 = tokens_of((90,91))   # yamīn
B3 = tokens_of((92,94))   # mukadhdhibīn / ḍāllīn

print(f'A1 (Sābiqūn 10-26): {len(A1)} tokens')
print(f'A2 (Yamīn 27-40): {len(A2)} tokens')
print(f'A3 (Shimāl 41-56): {len(A3)} tokens')
print(f'B1 (muqarrabīn 88-89): {len(B1)} tokens; sample: {B1}')
print(f'B2 (yamīn 90-91): {len(B2)} tokens; sample: {B2}')
print(f'B3 (mukadhdhibīn 92-94): {len(B3)} tokens; sample: {B3}')

def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb: return 0.0
    return len(sa & sb) / len(sa | sb)

# Observed correspondence Jaccards
J11 = jaccard(A1, B1)
J22 = jaccard(A2, B2)
J33 = jaccard(A3, B3)
print(f'\nObserved correspondence Jaccards:')
print(f'  J(A1, B1) = {J11:.4f}')
print(f'  J(A2, B2) = {J22:.4f}')
print(f'  J(A3, B3) = {J33:.4f}')

# Cross (non-corresponding) Jaccards
J12 = jaccard(A1, B2); J13 = jaccard(A1, B3)
J21 = jaccard(A2, B1); J23 = jaccard(A2, B3)
J31 = jaccard(A3, B1); J32 = jaccard(A3, B2)
print(f'\nCross Jaccards (non-corresponding):')
print(f'  J(A1,B2)={J12:.4f}  J(A1,B3)={J13:.4f}')
print(f'  J(A2,B1)={J21:.4f}  J(A2,B3)={J23:.4f}')
print(f'  J(A3,B1)={J31:.4f}  J(A3,B2)={J32:.4f}')
print(f'\nMean cross J: {(J12+J13+J21+J23+J31+J32)/6:.4f}')

# Permutation test: for each of 3 corresponding pairs, randomize which
# A-block tokens are assigned to which size-matched chunk and recompute J.
# More principled: token-shuffle permutation of A-blocks: pool all A tokens, reshuffle to A1/A2/A3
# preserving sizes; compute J(Ai_shuffled, Bi).
A_pool = A1 + A2 + A3
nA1, nA2, nA3 = len(A1), len(A2), len(A3)

null_J11 = []; null_J22 = []; null_J33 = []
for _ in range(N_PERM):
    pool = A_pool[:]
    random.shuffle(pool)
    nA1_perm = pool[:nA1]
    nA2_perm = pool[nA1:nA1+nA2]
    nA3_perm = pool[nA1+nA2:]
    null_J11.append(jaccard(nA1_perm, B1))
    null_J22.append(jaccard(nA2_perm, B2))
    null_J33.append(jaccard(nA3_perm, B3))

def p_one_sided(obs, null):
    return sum(1 for x in null if x >= obs) / len(null)

p11 = p_one_sided(J11, null_J11)
p22 = p_one_sided(J22, null_J22)
p33 = p_one_sided(J33, null_J33)

print(f'\nPermutation test (N={N_PERM}, seed={SEED}):')
print(f'  Cell F-01.a J(A1,B1)={J11:.4f}  null mean={sum(null_J11)/len(null_J11):.4f}  p_one_sided={p11:.4f}')
print(f'  Cell F-01.b J(A2,B2)={J22:.4f}  null mean={sum(null_J22)/len(null_J22):.4f}  p_one_sided={p22:.4f}')
print(f'  Cell F-01.c J(A3,B3)={J33:.4f}  null mean={sum(null_J33)/len(null_J33):.4f}  p_one_sided={p33:.4f}')

ALPHA_BON = 0.05/3
n_pass = sum(1 for p in [p11,p22,p33] if p < ALPHA_BON)
print(f'\nBonferroni-3 α = {ALPHA_BON:.5f}')
print(f'Cells passing: {n_pass}/3')
verdict = 'VINDICATED-RING' if n_pass >= 2 else ('PARTIAL' if n_pass==1 else 'NULL')
print(f'VERDICT: {verdict}')

# Show shared tokens for inspection
print('\nShared tokens per corresponding cell:')
for label, A, B in [('A1∩B1',A1,B1),('A2∩B2',A2,B2),('A3∩B3',A3,B3)]:
    shared = set(A) & set(B)
    print(f'  {label}: {sorted(shared)}')

result = {
    'test_id': 'Q056-F-01',
    'prereg_sha': EXPECTED_SHA,
    'seed': SEED, 'n_perm': N_PERM,
    'bonferroni_k': 3, 'alpha_bon': ALPHA_BON,
    'A1_tokens': len(A1), 'A2_tokens': len(A2), 'A3_tokens': len(A3),
    'B1_tokens': len(B1), 'B2_tokens': len(B2), 'B3_tokens': len(B3),
    'J11': J11, 'J22': J22, 'J33': J33,
    'cross_J': {'J12':J12,'J13':J13,'J21':J21,'J23':J23,'J31':J31,'J32':J32},
    'cross_J_mean': (J12+J13+J21+J23+J31+J32)/6,
    'null_means': {'J11_null_mean': sum(null_J11)/len(null_J11),
                   'J22_null_mean': sum(null_J22)/len(null_J22),
                   'J33_null_mean': sum(null_J33)/len(null_J33)},
    'p_one_sided': {'F01a': p11, 'F01b': p22, 'F01c': p33},
    'shared_tokens': {
        'A1_B1_shared': sorted(set(A1)&set(B1)),
        'A2_B2_shared': sorted(set(A2)&set(B2)),
        'A3_B3_shared': sorted(set(A3)&set(B3)),
    },
    'cells_passing_bon': n_pass,
    'verdict': verdict,
}

OUT = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/csv/Q056-F-01.json'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT,'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f'\nWrote {OUT}')
