#!/usr/bin/env python3
"""
Q068-F-01 — Writing-vocabulary density test.

Hypothesis: the muqaṭṭaʿ-letter ن at Q 68:1 is functionally glossed
by *wa-l-qalam* (Ibn ʿAbbās). Q 68 should over-concentrate
QAC writing-vocabulary roots {qlm, sTr, ktb, sjl, rqm, lwH}.

Pre-registered direction: POSITIVE on per-root (Bonferroni-6) and joint-family.
"""
import hashlib, json, math, os, sys
from collections import Counter, defaultdict

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f'{PROJECT}/surahs/Q068-al-qalam/preregs/Q068-F-01-writing-vocabulary-density-prereg.md'
EXPECTED_SHA = '052e5de244595cb30a79f54eab0a45eda2261fdcbee759bdb28e4e63c61a738e'

with open(PREREG, 'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}')

TARGET_SURAH = 68
ROOT_FAMILY = ['qlm', 'sTr', 'ktb', 'sjl', 'rqm', 'lwH']
BONFERRONI_K = 6
ALPHA_BON = 0.05 / BONFERRONI_K

# Build per-surah root distribution from QAC v0.4
roots_per_surah = defaultdict(Counter)
total_per_root = Counter()
target_locs = defaultdict(list)  # for diagnostics

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
                if rt in ROOT_FAMILY and surah == TARGET_SURAH:
                    target_locs[rt].append((parts[0], parts[1]))
                break

N = sum(total_per_root.values())
n_q68 = sum(roots_per_surah[TARGET_SURAH].values())

# Hypergeometric helpers
def lcomb(n, r):
    if r < 0 or r > n: return float('-inf')
    return math.lgamma(n+1) - math.lgamma(r+1) - math.lgamma(n-r+1)

def hg_p_ge(N, K, n, k):
    if k <= 0: return 1.0
    p = 0.0
    for i in range(k, min(K, n) + 1):
        lp = lcomb(K, i) + lcomb(N-K, n-i) - lcomb(N, n)
        p += math.exp(lp)
    return p

# Per-root tests (Bonferroni-6)
per_root_results = {}
combined_K = 0
combined_k = 0
for r in ROOT_FAMILY:
    K = total_per_root.get(r, 0)
    k = roots_per_surah[TARGET_SURAH].get(r, 0)
    expected = (n_q68 * K) / N if N else 0.0
    p = hg_p_ge(N, K, n_q68, k) if K > 0 else 1.0
    per_root_results[r] = {
        'corpus_K': K,
        'q68_k': k,
        'expected_under_uniform': expected,
        'observed_over_expected': (k / expected) if expected > 0 else None,
        'p_value_X_ge_k': p,
        'passes_raw_alpha_0.05': p < 0.05,
        'passes_bonferroni_alpha': p < ALPHA_BON,
    }
    combined_K += K
    combined_k += k

# Joint family test (single combined cell)
joint_p = hg_p_ge(N, combined_K, n_q68, combined_k) if combined_K > 0 else 1.0
joint_expected = (n_q68 * combined_K) / N

# Verdict
any_pass_bon = any(r['passes_bonferroni_alpha'] for r in per_root_results.values())
any_pass_raw = any(r['passes_raw_alpha_0.05'] for r in per_root_results.values())
joint_pass_raw = joint_p < 0.05
direction_reversed = combined_k < joint_expected

if direction_reversed:
    verdict = 'NULL_DIRECTION_REVERSED'
    interp = (f'Q 68 has only {combined_k} writing-vocab tokens vs expected {joint_expected:.2f} '
              f'(direction reversed). Pre-commit violation, published as NULL.')
elif any_pass_bon and joint_pass_raw:
    verdict = 'VINDICATED'
    interp = (f'At least one root passes Bonferroni-6 α={ALPHA_BON:.4f}, AND joint p={joint_p:.4f} < 0.05. '
              f"Ibn ʿAbbās's CONTENT-BEACON gloss of ن empirically supported.")
elif any_pass_raw or joint_pass_raw:
    verdict = 'DIRECTIONAL'
    interp = (f'Raw α passed but Bonferroni-6 not met. joint p={joint_p:.4f}, '
              f'any-root-raw-pass={any_pass_raw}.')
else:
    verdict = 'NULL'
    interp = (f'No root passes raw α=0.05; joint p={joint_p:.4f} ≥ 0.05. '
              f'CONTENT-BEACON hypothesis NOT supported on QAC roots {ROOT_FAMILY}.')

# Compute Q68 RANK by per-density of writing-family combined
all_density = []
for s in range(1, 115):
    n_s = sum(roots_per_surah[s].values())
    k_s = sum(roots_per_surah[s].get(r, 0) for r in ROOT_FAMILY)
    if n_s > 0:
        all_density.append((s, k_s / n_s * 1000, k_s, n_s))
sorted_density = sorted(all_density, key=lambda x: -x[1])
q68_rank_density = next(i+1 for i, e in enumerate(sorted_density) if e[0] == TARGET_SURAH)

output = {
    'finding_id': 'Q068-F-01',
    'prereg_sha256': actual,
    'date_run': '2026-05-07',
    'rules_tuple': '(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan)',
    'target_surah': TARGET_SURAH,
    'root_family': ROOT_FAMILY,
    'corpus_total_root_tokens': N,
    'q68_total_root_tokens': n_q68,
    'per_root_results': per_root_results,
    'joint_family_K': combined_K,
    'joint_family_k': combined_k,
    'joint_family_expected_under_uniform': joint_expected,
    'joint_family_p_value': joint_p,
    'q68_writing_density_per_1000': (combined_k / n_q68 * 1000) if n_q68 else 0.0,
    'q68_rank_by_writing_density_per_1000': q68_rank_density,
    'top10_surahs_by_writing_density': [
        {'surah': s, 'density_per_1000': d, 'k': k, 'n': n} for s,d,k,n in sorted_density[:10]
    ],
    'q68_writing_token_locations': dict(target_locs),
    'alpha_raw': 0.05,
    'alpha_bonferroni_6': ALPHA_BON,
    'verdict': verdict,
    'interpretation': interp,
}

out_path = f'{PROJECT}/surahs/Q068-al-qalam/csv/Q068-F-01.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q068-F-01: VERDICT={verdict}')
print(f'  Q 68 total root-tokens: {n_q68}')
print(f'  Combined writing-family k={combined_k}, expected={joint_expected:.2f}, joint p={joint_p:.4f}')
print(f'  Q 68 rank by writing-density per 1000: {q68_rank_density}/114')
print(f'  Per-root:')
for r, res in per_root_results.items():
    print(f"    {r}: k={res['q68_k']} exp={res['expected_under_uniform']:.3f} p={res['p_value_X_ge_k']:.4f} bon-pass={res['passes_bonferroni_alpha']}")
print(f'  Output: {out_path}')
