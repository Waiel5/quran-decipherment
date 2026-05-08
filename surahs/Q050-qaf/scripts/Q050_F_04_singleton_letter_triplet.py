#!/usr/bin/env python3
"""
Q050-F-04 — Singleton-letter-triplet joint signature.

Test whether the (Q 38, Q 50, Q 68) triplet has a mean pairwise Fisher-Rao
distance LOWER than 95% of N=10000 random 3-surah triplets.

Direction-locked: LOW S (cluster-like).
"""
import hashlib, json, sys, random

PROJECT = '/Users/grey/Downloads/quran'
PREREG_PATH = f'{PROJECT}/surahs/Q050-qaf/preregs/Q050-F-04-singleton-letter-triplet-prereg.md'
EXPECTED_SHA = 'cac90ad5c9e1d4a9454f30ae994f2f9838352e8bb0ca725940a55d7d8a94d8df'

with open(PREREG_PATH, 'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual_sha}')

SEED = 20260507
N_PERM = 10000
N = 114
TRIPLET = (38, 50, 68)

# Load FR distance matrix from h-new-111
with open(f'{PROJECT}/findings/phase-b-hypotheses/csv/h-new-111.json') as f:
    h111 = json.load(f)
ut = h111['D_matrix_upper_triangular']
M = [[0.0] * N for _ in range(N)]
for entry in ut:
    i, j, d = entry
    M[i - 1][j - 1] = d
    M[j - 1][i - 1] = d

def mean_pairwise_FR(triplet_1indexed):
    a, b, c = [t - 1 for t in triplet_1indexed]
    return (M[a][b] + M[a][c] + M[b][c]) / 3.0

S_obs = mean_pairwise_FR(TRIPLET)
print(f'Singleton-letter triplet (Q 38, Q 50, Q 68) mean pairwise FR: {S_obs:.6f}')

rng = random.Random(SEED)
null_S = []
for it in range(N_PERM):
    triplet = rng.sample(range(1, N + 1), 3)
    null_S.append(mean_pairwise_FR(tuple(triplet)))

n_le = sum(1 for s in null_S if s <= S_obs)
p_low = (n_le + 1) / (N_PERM + 1)
n_ge = sum(1 for s in null_S if s >= S_obs)
p_high = (n_ge + 1) / (N_PERM + 1)

null_mean = sum(null_S) / N_PERM
null_sd = (sum((s - null_mean)**2 for s in null_S) / N_PERM) ** 0.5
z = (S_obs - null_mean) / null_sd if null_sd > 0 else None
percentile = (n_le / N_PERM) * 100.0

# Pre-committed direction: LOW S
if p_low < 0.05:
    primary_verdict = 'CONFIRMED'
elif p_low < 0.10:
    primary_verdict = 'DIRECTIONAL'
elif p_high < 0.05:
    primary_verdict = 'PRE-COMMIT-VIOLATION-HIGH-S-NULL'
else:
    primary_verdict = 'NULL'

# Secondary descriptive table
with open(f'{PROJECT}/findings/phase-b-hypotheses/csv/h-new-750.json') as f:
    h750 = json.load(f)
with open(f'{PROJECT}/findings/phase-b-hypotheses/csv/h-new-590.json') as f:
    h590 = json.load(f)
with open(f'{PROJECT}/findings/phase-b-hypotheses/csv/h-new-840.json') as f:
    h840 = json.load(f)

ps750 = {e['surah']: e for e in h750['per_surah']}
ps590 = {e['X']: e for e in h590['all_surahs_results']}
ps840 = {e['surah']: e for e in h840['all_uas']}

descriptive = []
for s in TRIPLET:
    descriptive.append({
        'surah': s,
        'opener_letter': {38: 'ص', 50: 'ق', 68: 'ن'}[s],
        'rev_order': {38: 38, 50: 34, 68: 2}[s],  # Tanzil Egyptian standard
        'noldeke_phase': 'Middle Meccan' if s in (38, 50) else 'Early Meccan',
        'n_verses': ps750[s]['n_verses'],
        'mean_content_distance': round(ps750[s]['mean_content_distance'], 4),
        'sig_A': round(ps750[s]['sig_A'], 4),
        'rank_A': ps750[s]['rank_A'],
        'top_final_letter': ps750[s]['top_final_letter'],
        'top_final_letter_frac': round(ps750[s]['top_final_letter_frac'], 4),
        'rhyme_entropy_nats': round(ps750[s]['rhyme_entropy_nats'], 4),
        'delta_pct_outlier': ps590[s]['delta_pct'],
        'outlier_classification': ps590[s]['classification'],
        'UAS': round(ps840[s]['UAS'], 4),
    })

# Pairwise FR distances within triplet
fr_pair = {}
for i in range(3):
    for j in range(i+1, 3):
        a, b = TRIPLET[i], TRIPLET[j]
        fr_pair[f'FR_Q{a}_Q{b}'] = round(M[a-1][b-1], 4)

output = {
    'finding_id': 'Q050-F-04',
    'prereg_sha256': actual_sha,
    'date_run': '2026-05-07',
    'rules_tuple': '(no-tashkeel, QAC-stem-roots, basmala-not-counted-elsewhere, Hafs-Kufan, mushaf-order, all metrics from H-NEW pipeline as published)',
    'seed': SEED,
    'n_perm': N_PERM,
    'triplet': list(TRIPLET),
    'mean_pairwise_FR_observed': round(S_obs, 6),
    'pairwise_FR_internal': fr_pair,
    'null_mean': round(null_mean, 6),
    'null_sd': round(null_sd, 6),
    'z': round(z, 4) if z is not None else None,
    'percentile_in_null_low_S': round(percentile, 2),
    'p_low_S': round(p_low, 6),
    'p_high_S': round(p_high, 6),
    'primary_verdict': primary_verdict,
    'descriptive_per_surah': descriptive,
}

out_path = f'{PROJECT}/surahs/Q050-qaf/csv/Q050-F-04.json'
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q050-F-04: VERDICT={primary_verdict}')
print(f'  S_obs (low): {S_obs:.6f}')
print(f'  null mean: {null_mean:.6f} ± {null_sd:.6f}')
print(f'  percentile (low-S): {percentile:.2f}')
print(f'  p_low_S: {p_low:.6f}')
print(f'  Output: {out_path}')
