#!/usr/bin/env python3
"""
cross-finding-028 — Liturgical-recitation surah-pair ↔ FR-near-pair hypothesis.

Pre-reg: /Users/grey/Downloads/quran/findings/cross-finding/cross-finding-028-prereg.md
SHA-locked: 8606f9e1b76144fe4b6db39cd16118ea640728f48bd0bb1be8050c53a5dd7c96

H1: Mean FR distance of pre-committed canonical liturgical-pair set is LOWER
    than corpus mean (0.9235), one-sided permutation test, 10000 perms, seed 20260507.
H2: Holds even when each pair is matched to length-matched random pairs.
H3 (FALSIFIER): If pair-set mean >= 0.9235, hypothesis REVERSED -> NULL.

Direction LOCKED: LOW.
Bonferroni k=2 (primary + length-control); alpha_bon = 0.025.
Per-pair descriptive Bonferroni: k=6, alpha=0.0083.

Inherits rules-tuple from H-NEW-111: (no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""

import json
import hashlib
import random
import os
import sys
from collections import defaultdict

# --- SHA-lock verification ---
PREREG_PATH = '/Users/grey/Downloads/quran/findings/cross-finding/cross-finding-028-prereg.md'
EXPECTED_PREREG_SHA = '8606f9e1b76144fe4b6db39cd16118ea640728f48bd0bb1be8050c53a5dd7c96'

with open(PREREG_PATH, 'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_PREREG_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH:\n  expected {EXPECTED_PREREG_SHA}\n  got      {actual_sha}\nFAIL-FAST per PRE-REG-STANDARD-04.')
print(f'[ok] Pre-reg SHA verified: {actual_sha}')

# --- Locked params ---
SEED = 20260507
N_PERMS = 10000
CORPUS_MEAN_FR = 0.923487  # from h-new-111.json distance_matrix_stats.mean
CORPUS_MEDIAN_FR = 0.956707
ALPHA_BON_PRIMARY = 0.025  # 0.05 / 2 (primary + length-control)
ALPHA_BON_PER_PAIR = 0.05 / 6

# Pre-committed VERIFIED pair set (after on-disk hadith verification, see prereg §2):
VERIFIED_PAIRS = [
    ('P1', 50, 54, 'Eid prayer (muslim#1949, tirmidhi#534, abudawud#1155)'),
    ('P2', 32, 76, 'Fajr-Friday (bukhari#870, bukhari#1037, muslim#1926/1927)'),
    ('P3', 87, 88, 'Eid + Jumuʿa (muslim#1920, tirmidhi#533, abudawud#1123/1126)'),
    ('P4', 109, 112, 'Maghrib/Fajr-sunnah/ṭawāf (tirmidhi#870, ibnmajah#883/900)'),
    ('P5', 113, 114, 'Muʿawwidhatān (bukhari#4809/4810/5526, nasai#5441)'),
    ('P6', 32, 67, 'Pre-sleep al-Munjiya (tirmidhi#2975) — replaces prompt Q36/Q67 per specialist override'),
]

# Cluster sub-test: 3-surah muʿawwidhāt cluster
CLUSTER = [112, 113, 114]
CLUSTER_HADITH = 'bukhari#4810, bukhari#5526'

# --- Load FR matrix ---
FR_PATH = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'
with open(FR_PATH) as f:
    fr_data = json.load(f)
print(f'[ok] FR matrix loaded from {FR_PATH}')
print(f'     pre_reg_sha256 (h-new-111) = {fr_data["pre_reg_sha256"]}')

# Build symmetric distance dict
D = defaultdict(dict)
for triple in fr_data['D_matrix_upper_triangular']:
    a, b, d = triple
    a, b = int(a), int(b)
    D[a][b] = d
    D[b][a] = d

print(f'     n_pairs in matrix = {fr_data["distance_matrix_stats"]["n_pairs"]}')
print(f'     corpus mean FR    = {fr_data["distance_matrix_stats"]["mean"]}')
print(f'     corpus median FR  = {fr_data["distance_matrix_stats"]["median"]}')

# --- Load verse counts for length-control ---
HAFS_PATH = '/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv'
verse_counts = {}
with open(HAFS_PATH) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or line.lower().startswith('surah'):
            continue
        parts = line.split('\t') if '\t' in line else line.split()
        if len(parts) >= 2:
            try:
                s = int(parts[0])
                v = int(parts[1])
                verse_counts[s] = v
            except ValueError:
                continue
if len(verse_counts) != 114:
    # Fallback: derive from quran-no-tashkeel.json
    with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
        q = json.load(f)
    if isinstance(q, dict) and 'data' in q:
        q = q['data']
    if isinstance(q, list):
        verse_counts = {}
        for surah in q:
            sid = int(surah.get('id', surah.get('number', 0)))
            verses = surah.get('verses', surah.get('ayahs', []))
            verse_counts[sid] = len(verses)
print(f'[ok] verse counts loaded for {len(verse_counts)} surahs')

# --- 1. PRIMARY: pair-set mean FR ---
print('\n--- PRIMARY: pair-set mean FR vs random-pair perm null ---')
pair_FRs = []
for label, a, b, ctx in VERIFIED_PAIRS:
    d = D[a][b]
    pair_FRs.append((label, a, b, d, ctx))
    print(f'  {label}: FR(Q{a}, Q{b}) = {d:.4f}   ({ctx})')
observed_mean = sum(p[3] for p in pair_FRs) / len(pair_FRs)
observed_median = sorted(p[3] for p in pair_FRs)[len(pair_FRs) // 2]
print(f'\n  Observed pair-set MEAN   = {observed_mean:.4f}')
print(f'  Observed pair-set MEDIAN = {observed_median:.4f}')
print(f'  Corpus     mean          = {CORPUS_MEAN_FR:.4f}')
print(f'  Corpus     median        = {CORPUS_MEDIAN_FR:.4f}')

# Build pool of all pairs EXCLUDING verified pairs
verified_pair_set = set()
for _, a, b, _, _ in pair_FRs:
    verified_pair_set.add((min(a, b), max(a, b)))

pool_pairs = []
for a in range(1, 115):
    for b in range(a + 1, 115):
        if (a, b) not in verified_pair_set:
            pool_pairs.append((a, b, D[a][b]))
print(f'  pool size (excl verified): {len(pool_pairs)}')

# 2. Permutation null: 10000 random samples of N=6 pairs from pool, take mean
rng = random.Random(SEED)
N = len(pair_FRs)
perm_means = []
for _ in range(N_PERMS):
    samp = rng.sample(pool_pairs, N)
    perm_means.append(sum(p[2] for p in samp) / N)
perm_means_sorted = sorted(perm_means)
n_le = sum(1 for m in perm_means if m <= observed_mean)
p_low = (n_le + 1) / (N_PERMS + 1)
perm_mean_of_means = sum(perm_means) / N_PERMS
perm_min = min(perm_means)
perm_max = max(perm_means)

print(f'\n  perm null (N={N_PERMS}, sample-size-{N} pairs from pool):')
print(f'    mean of perm-means = {perm_mean_of_means:.4f}')
print(f'    [min, max]         = [{perm_min:.4f}, {perm_max:.4f}]')
print(f'    p_low (one-sided, observed_mean <= perm_mean) = {p_low:.5f}')
print(f'  Bonferroni alpha (k=2): {ALPHA_BON_PRIMARY}')
primary_pass = (observed_mean < CORPUS_MEAN_FR) and (p_low <= ALPHA_BON_PRIMARY)
primary_directional = (observed_mean < CORPUS_MEAN_FR) and (p_low <= 0.05)
print(f'  primary verdict: {"CONFIRMED at alpha_bon" if primary_pass else ("DIRECTIONAL (raw p<=0.05)" if primary_directional else "DIRECTIONAL-WEAK or NULL")}')

# --- 3. PER-PAIR descriptive: each pair's percentile under random-pair null ---
print('\n--- PER-PAIR DESCRIPTIVE TABLE (Bonferroni k=6, alpha=0.0083) ---')
all_pool_d = [p[2] for p in pool_pairs]
per_pair_results = []
for label, a, b, d, ctx in pair_FRs:
    n_le_pair = sum(1 for x in all_pool_d if x <= d)
    pctl = 100.0 * n_le_pair / len(all_pool_d)
    p_pair = (n_le_pair + 1) / (len(all_pool_d) + 1)
    sig_marker = ''
    if p_pair <= ALPHA_BON_PER_PAIR:
        sig_marker = '** (Bonferroni-pass)'
    elif p_pair <= 0.05:
        sig_marker = '* (raw <= 0.05)'
    print(f'  {label} Q{a}-Q{b}: FR={d:.4f}, percentile={pctl:.2f}, p_one_sided={p_pair:.4f} {sig_marker}')
    per_pair_results.append({
        'label': label,
        'surah_a': a,
        'surah_b': b,
        'fr': d,
        'percentile_in_pool': pctl,
        'p_one_sided': p_pair,
        'context': ctx,
    })

# --- 4. LENGTH-CONTROL (H2) ---
print('\n--- LENGTH-CONTROL (H2): each pair matched to length-matched random pairs ---')
TOL = 0.10
length_diffs = []
length_match_details = []
for label, a, b, d, ctx in pair_FRs:
    target_C = verse_counts[a] + verse_counts[b]
    lo = target_C * (1 - TOL)
    hi = target_C * (1 + TOL)
    matched = []
    for (x, y, dxy) in pool_pairs:
        Cxy = verse_counts[x] + verse_counts[y]
        if lo <= Cxy <= hi:
            matched.append(dxy)
    if len(matched) < 5:
        # Widen tolerance
        for tol_w in (0.20, 0.30):
            lo = target_C * (1 - tol_w)
            hi = target_C * (1 + tol_w)
            matched = [dxy for (x, y, dxy) in pool_pairs if lo <= verse_counts[x] + verse_counts[y] <= hi]
            if len(matched) >= 50:
                break
    matched_mean = sum(matched) / len(matched)
    diff = d - matched_mean  # negative = pair is FR-closer than length-matched
    length_diffs.append(diff)
    length_match_details.append({
        'label': label,
        'surah_a': a,
        'surah_b': b,
        'pair_fr': d,
        'combined_verses': target_C,
        'n_length_matched_random': len(matched),
        'length_matched_mean_fr': matched_mean,
        'fr_minus_length_matched_mean': diff,
    })
    print(f'  {label} Q{a}-Q{b}: pair FR={d:.4f}, length-matched-pool ({len(matched)} pairs) mean FR={matched_mean:.4f}, diff={diff:+.4f}')

mean_diff = sum(length_diffs) / len(length_diffs)
print(f'\n  Mean (pair_FR - length_matched_mean_FR) = {mean_diff:+.4f}')
# permutation null on the mean-diff statistic: shuffle which "pair" gets which "length-matched-pool" assignment?
# Use a sign-test on the per-pair difference
n_below = sum(1 for x in length_diffs if x < 0)
n_above = sum(1 for x in length_diffs if x > 0)
# Two-tailed binomial (sign test) under H0: equal probability of +/- sign
# For one-sided LOW: probability that >= n_below of N had negative sign under p=0.5
from math import comb
N_diff = len(length_diffs)
sign_p_one_sided = sum(comb(N_diff, k) * (0.5 ** N_diff) for k in range(n_below, N_diff + 1))
print(f'  Sign test: {n_below} of {N_diff} pairs are FR-closer than their length-matched controls')
print(f'  one-sided binomial p (LOW direction): {sign_p_one_sided:.4f}')

# Permutation null on length-controlled mean-diff
length_perm_diffs = []
for _ in range(N_PERMS):
    perm_diffs = []
    for ld in length_match_details:
        target_C = ld['combined_verses']
        lo = target_C * (1 - TOL)
        hi = target_C * (1 + TOL)
        # take a random matched pair instead of the verified pair
        matched_pool = [dxy for (x, y, dxy) in pool_pairs if lo <= verse_counts[x] + verse_counts[y] <= hi]
        if len(matched_pool) < 5:
            for tol_w in (0.20, 0.30):
                lo = target_C * (1 - tol_w)
                hi = target_C * (1 + tol_w)
                matched_pool = [dxy for (x, y, dxy) in pool_pairs if lo <= verse_counts[x] + verse_counts[y] <= hi]
                if len(matched_pool) >= 50:
                    break
        random_pair_fr = rng.choice(matched_pool)
        random_pair_pool_mean = sum(matched_pool) / len(matched_pool)
        perm_diffs.append(random_pair_fr - random_pair_pool_mean)
    length_perm_diffs.append(sum(perm_diffs) / len(perm_diffs))

n_le_lc = sum(1 for m in length_perm_diffs if m <= mean_diff)
p_low_lc = (n_le_lc + 1) / (N_PERMS + 1)
print(f'  permutation null (10000) on length-controlled mean-diff: p_low = {p_low_lc:.5f}')
length_pass = (mean_diff < 0) and (p_low_lc <= ALPHA_BON_PRIMARY)
length_directional = (mean_diff < 0) and (p_low_lc <= 0.05)
print(f'  length-control verdict: {"PASS at alpha_bon" if length_pass else ("DIRECTIONAL (raw p<=0.05)" if length_directional else "DIRECTIONAL-WEAK or NULL")}')

# --- 5. CLUSTER sub-test: muʿawwidhāt 3-cluster ---
print('\n--- CLUSTER SUB-TEST: muʿawwidhāt (Q 112, Q 113, Q 114) ---')
cluster_pairs = [(CLUSTER[i], CLUSTER[j]) for i in range(len(CLUSTER)) for j in range(i + 1, len(CLUSTER))]
cluster_pair_d = [D[a][b] for a, b in cluster_pairs]
cluster_mean = sum(cluster_pair_d) / len(cluster_pair_d)
print(f'  cluster pairs: {cluster_pairs}')
print(f'  cluster pair FRs: {[round(x,4) for x in cluster_pair_d]}')
print(f'  cluster mean pairwise FR = {cluster_mean:.4f}')

# Permutation null: 10000 random 3-surah triplets
all_surahs = list(range(1, 115))
cluster_set = set(CLUSTER)
cluster_perm_means = []
for _ in range(N_PERMS):
    triple = rng.sample(all_surahs, 3)
    while set(triple) == cluster_set:
        triple = rng.sample(all_surahs, 3)
    pairs_t = [(triple[0], triple[1]), (triple[0], triple[2]), (triple[1], triple[2])]
    m = sum(D[a][b] for a, b in pairs_t) / 3
    cluster_perm_means.append(m)
n_le_c = sum(1 for m in cluster_perm_means if m <= cluster_mean)
p_low_c = (n_le_c + 1) / (N_PERMS + 1)
print(f'  perm null (10000 random triplets): p_low = {p_low_c:.5f}')

# --- 6. Save JSON ---
out = {
    'finding_id': 'cross-finding-028',
    'title': 'Liturgical-recitation surah-pair ↔ FR-near-pair hypothesis',
    'pre_reg_sha256': EXPECTED_PREREG_SHA,
    'date': '2026-05-07',
    'seed': SEED,
    'n_perms': N_PERMS,
    'corpus_mean_fr': CORPUS_MEAN_FR,
    'corpus_median_fr': CORPUS_MEDIAN_FR,
    'rules_tuple': '(no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi) — inherited from H-NEW-111',
    'fr_source': FR_PATH,
    'fr_source_pre_reg_sha256': fr_data['pre_reg_sha256'],
    'verified_pairs': [
        {'label': p[0], 'surah_a': p[1], 'surah_b': p[2], 'fr': p[3], 'context': p[4]}
        for p in pair_FRs
    ],
    'data_gaps_dropped': [
        {'pair': 'Q97/Q30', 'reason': 'NOT FOUND in 9-book canonical content-search'},
        {'pair': 'Q17/Q23', 'reason': 'NOT FOUND in 9-book canonical content-search'},
        {'pair': 'Q18/Q32', 'reason': 'NOT FOUND in 9-book content-search as joint single-night practice'},
    ],
    'specialist_override': {
        'replaced': 'Q36/Q67 (prompt)',
        'with': 'Q32/Q67',
        'evidence': 'tirmidhi#2975 — Prophet would not sleep until reciting Alif Lam Mim Tanzil (Q32) AND Tabarak Alladhi Biyadihil-Mulk (Q67)',
        'q36_q67_note': 'Q36 alone (death-recitation) and Q67 alone (al-Mānīʿa grave-protection) are well-attested but NOT as a single coupled pair-recitation in 9-book content-search',
    },
    'primary_aggregate_test': {
        'n_pairs': N,
        'observed_mean_fr': observed_mean,
        'observed_median_fr': observed_median,
        'corpus_mean_fr': CORPUS_MEAN_FR,
        'perm_mean_of_means': perm_mean_of_means,
        'perm_min': perm_min,
        'perm_max': perm_max,
        'p_low_one_sided': p_low,
        'alpha_bon': ALPHA_BON_PRIMARY,
        'verdict': 'CONFIRMED' if primary_pass else ('DIRECTIONAL' if primary_directional else 'NULL/DIRECTIONAL-WEAK'),
    },
    'per_pair_descriptive': per_pair_results,
    'length_control_test': {
        'tolerance_combined_verses': TOL,
        'mean_diff_pair_minus_length_matched': mean_diff,
        'sign_test_n_below': n_below,
        'sign_test_n_above': n_above,
        'sign_test_p_one_sided': sign_p_one_sided,
        'perm_null_p_low': p_low_lc,
        'verdict': 'PASS' if length_pass else ('DIRECTIONAL' if length_directional else 'NULL/DIRECTIONAL-WEAK'),
        'pair_details': length_match_details,
    },
    'cluster_sub_test_muawwidhat': {
        'cluster': CLUSTER,
        'hadith': CLUSTER_HADITH,
        'cluster_pair_fr': cluster_pair_d,
        'cluster_mean_pairwise_fr': cluster_mean,
        'perm_null_n': N_PERMS,
        'p_low_one_sided': p_low_c,
    },
    'bonferroni_family': 'cross-finding-028-liturgical-pair-FR',
    'bonferroni_k': 2,
    'bonferroni_alpha': ALPHA_BON_PRIMARY,
}

OUT_PATH = '/Users/grey/Downloads/quran/findings/cross-finding/csv/cross-finding-028.json'
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print(f'\n[ok] JSON written: {OUT_PATH}')

# --- 7. Final summary ---
print('\n=== FINAL VERDICT SUMMARY ===')
print(f'  Aggregate primary  : observed_mean={observed_mean:.4f} vs corpus={CORPUS_MEAN_FR:.4f}; p_low={p_low:.5f}; alpha_bon={ALPHA_BON_PRIMARY}')
print(f'    -> {"CONFIRMED" if primary_pass else ("DIRECTIONAL (raw)" if primary_directional else "NULL/DIRECTIONAL-WEAK")}')
print(f'  Length-controlled  : mean_diff={mean_diff:+.4f}; sign_p={sign_p_one_sided:.4f}; perm_p={p_low_lc:.5f}')
print(f'    -> {"PASS at alpha_bon" if length_pass else ("DIRECTIONAL (raw)" if length_directional else "NULL/DIRECTIONAL-WEAK")}')
print(f'  Cluster muawwidhat : mean_pairwise={cluster_mean:.4f}; p_low={p_low_c:.5f}')
print('\nFinal H1 verdict (direction-locked LOW + Bonferroni alpha=0.025):')
if observed_mean >= CORPUS_MEAN_FR:
    print('  >>> NULL with REVERSED DIRECTION — pair-set mean ABOVE corpus mean. H3 falsifier triggered.')
elif primary_pass and length_pass:
    print('  >>> CONFIRMED at alpha_bon=0.025 on BOTH primary aggregate AND length-control.')
elif primary_directional and length_directional:
    print('  >>> DIRECTIONAL (raw p<=0.05) on both primary and length-control; NOT at Bonferroni alpha.')
else:
    print('  >>> DIRECTIONAL-WEAK or NULL on at least one of primary/length-control.')
