#!/usr/bin/env python3
"""
Q067-F-04 — m-l-k stem lexical concentration test.
Tests whether Q67 al-Mulk over-concentrates the QAC mlk root family.
Pre-registered direction: POSITIVE (over-concentration). NULL = falsifies
the name-tracks-vocabulary hypothesis at the corpus level.
"""
import hashlib, json, math, os, sys
from collections import Counter, defaultdict

PROJECT = '/Users/grey/Downloads/quran'
PREREG_PATH = f'{PROJECT}/surahs/Q067-al-mulk/preregs/Q067-F-04-mulk-stem-density-prereg.md'
EXPECTED_SHA = '2611e9cc5ed19fab87f1c4cec0eaf5db245b9e963db5dbe35f951e18cdb76fd1'

with open(PREREG_PATH, 'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual_sha}')

# Build per-surah root distribution from QAC v0.4
roots_per_surah = defaultdict(Counter)
total_per_root = Counter()

with open(f'{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('('):
            continue
        parts = line.strip().split('\t')
        if len(parts) < 4:
            continue
        loc = parts[0].strip('()').split(':')
        try:
            surah = int(loc[0])
        except (ValueError, IndexError):
            continue
        feats = parts[3]
        for tag in feats.split('|'):
            if tag.startswith('ROOT:'):
                rt = tag[5:]
                roots_per_surah[surah][rt] += 1
                total_per_root[rt] += 1
                break

target_root = 'mlk'

corpus_total_tokens = sum(total_per_root.values())
corpus_mlk = total_per_root.get(target_root, 0)
q67_total_tokens = sum(roots_per_surah[67].values())
q67_mlk = roots_per_surah[67].get(target_root, 0)

# Hypergeometric test
def lcomb(n, r):
    if r < 0 or r > n:
        return float('-inf')
    return math.lgamma(n+1) - math.lgamma(r+1) - math.lgamma(n-r+1)

def hg_pmf(N, K, n, i):
    return math.exp(lcomb(K, i) + lcomb(N-K, n-i) - lcomb(N, n))

N = corpus_total_tokens
K = corpus_mlk
n = q67_total_tokens
k = q67_mlk

expected = (n * K) / N

p_ge = 0.0
upper = min(K, n)
for i in range(k, upper + 1):
    p_ge += hg_pmf(N, K, n, i)

alpha_bon = 0.05 / 114
passes_raw = p_ge < 0.05
passes_bon = p_ge < alpha_bon

# Per-surah ranking by raw count and density
all_counts = []
for s in range(1, 115):
    n_tok = sum(roots_per_surah[s].values())
    cnt = roots_per_surah[s].get(target_root, 0)
    density = (cnt / n_tok * 1000) if n_tok else 0.0
    all_counts.append({'surah': s, 'mlk_count': cnt, 'total_tokens': n_tok, 'density_per_1000': density})

sorted_by_count = sorted(all_counts, key=lambda x: -x['mlk_count'])
sorted_by_density = sorted(all_counts, key=lambda x: -x['density_per_1000'])

q67_rank_count = next(i+1 for i, e in enumerate(sorted_by_count) if e['surah'] == 67)
q67_rank_density = next(i+1 for i, e in enumerate(sorted_by_density) if e['surah'] == 67)

# Verdict
if passes_bon:
    verdict = 'VINDICATED'
    interpretation = f'Q67 mlk-stem over-concentration significant at Bonferroni-corrected α (p={p_ge:.4e} < {alpha_bon:.4e}). Name-tracks-vocabulary holds for Q67.'
elif passes_raw:
    verdict = 'DIRECTIONAL'
    interpretation = f'Q67 mlk-stem over-concentration significant at raw α=0.05 (p={p_ge:.4e}) but not Bonferroni-corrected.'
elif k <= expected:
    verdict = 'NULL'
    interpretation = (
        f'Q67 has only {k} mlk-stem tokens (expected {expected:.2f}); P(X≥{k})={p_ge:.4f}. '
        f'The "name-tracks-vocabulary" hypothesis is FALSIFIED for Q67. '
        f'Q67 is named *al-Mulk* by the OPENING-WORD CONVENTION, not by lexical-density. '
        f'In contrast, Q24 al-Nūr passes the analogous test for light-cluster at p<10⁻⁶ (Q024-F-01). '
        f'The corpus-wide name-tracks-vocabulary generalization is RULES-TUPLE-FRAGILE: works for Q24, fails for Q67.'
    )
else:
    verdict = 'NULL_DIRECTIONAL'
    interpretation = f'Q67 mlk-stem count ({k}) exceeds expected ({expected:.2f}) but not at significance (p={p_ge:.4f}).'

output = {
    'finding_id': 'Q067-F-04',
    'prereg_sha256': actual_sha,
    'date_run': '2026-04-28',
    'rules_tuple': '(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan)',
    'target_root': target_root,
    'corpus_total_root_tokens': N,
    'corpus_mlk_total': K,
    'q67_total_root_tokens': n,
    'q67_mlk_observed': k,
    'q67_mlk_expected_under_uniform': expected,
    'p_value_hypergeometric_X_ge_observed': p_ge,
    'alpha_raw': 0.05,
    'alpha_bonferroni_for_114_surahs': alpha_bon,
    'passes_raw_alpha': passes_raw,
    'passes_bonferroni': passes_bon,
    'q67_rank_by_raw_count': q67_rank_count,
    'q67_rank_by_density': q67_rank_density,
    'q67_density_per_1000': (k / n * 1000) if n else 0.0,
    'top10_by_raw_count': sorted_by_count[:10],
    'top10_by_density': sorted_by_density[:10],
    'verdict': verdict,
    'interpretation': interpretation,
    'cross_reference_to_Q024_F_01': 'Q24 al-Nūr passes light-cluster Bonferroni at p<10⁻⁶ (light root family of 16 roots vs Q67 single mlk root)',
}

out_path = f'{PROJECT}/surahs/Q067-al-mulk/csv/Q067-F-04.json'
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q067-F-04: VERDICT={verdict}')
print(f'  Q67 mlk count: {k} (expected {expected:.2f})')
print(f'  P(X >= {k}) = {p_ge:.4e}')
print(f'  Bonferroni α = {alpha_bon:.4e}')
print(f'  Q67 rank by raw count: {q67_rank_count}/114')
print(f'  Q67 rank by density: {q67_rank_density}/114')
print(f'  Verdict: {interpretation}')
print(f'  Output: {out_path}')
