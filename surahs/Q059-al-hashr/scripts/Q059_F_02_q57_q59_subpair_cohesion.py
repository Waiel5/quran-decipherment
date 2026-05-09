#!/usr/bin/env python3
"""
Q059-F-02 — Q 57+59 perfect-tense sub-pair cohesion test.

Tests whether the Q 57 / Q 59 sub-pair (within the H-NEW-58c perfect-tense trio Q 57/59/61)
is more cohesive than chance — and specifically whether the sub-pair is even tighter than
the full Q 57/59/61 trio mean.

Operationalization: shared character-prefix (H-NEW-58c metric) + root-overlap Jaccard.

Pre-reg: preregs/Q059-F-02-q57-q59-subpair-cohesion-prereg.md
Authored: Waiel Al-Shujaa, 2026-05-09
"""
import json
import re
import hashlib
import random
from pathlib import Path
from itertools import combinations

ROOT = Path('/Users/grey/Downloads/quran')
OUT = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/csv/Q059-F-02.json')
PREREG = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/preregs/Q059-F-02-q57-q59-subpair-cohesion-prereg.md')
SEED = 20260509

ORNAMENTS = re.compile(r'[ۖ-ۭۚ-۝]')

def clean_text(t):
    t = ORNAMENTS.sub(' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

with open(ROOT / 'quran-text' / 'quran-no-tashkeel.json', 'r') as f:
    q = json.load(f)

# Get full surah words for Q 57, 59, 61, 62, 64
surah_words = {}
surah_text = {}
surah_v1 = {}
for sid in [57, 59, 61, 62, 64]:
    s = q[sid-1]
    all_words = []
    for v in s['verses']:
        t = clean_text(v['text'])
        all_words.extend(t.split())
    surah_words[sid] = all_words
    surah_text[sid] = ' '.join(all_words)
    surah_v1[sid] = clean_text(s['verses'][0]['text'])

# Cell A: shared char-prefix metric (H-NEW-58c) for opening verse
def shared_prefix(s1, s2):
    """Number of chars from start that match exactly."""
    n = 0
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            n += 1
        else:
            break
    return n

print("=== Cell A — Opening-verse shared-char-prefix ===")
all_pairs = list(combinations([57, 59, 61, 62, 64], 2))
prefix_results = {}
for (a, b) in all_pairs:
    p = shared_prefix(surah_v1[a], surah_v1[b])
    prefix_results[f"Q{a}-Q{b}"] = p
    print(f"  Q{a}-Q{b}: {p}")

within_perfect = [prefix_results['Q57-Q59'], prefix_results['Q57-Q61'], prefix_results['Q59-Q61']]
within_imperfect = [prefix_results['Q62-Q64']]
cross_tense = [prefix_results['Q57-Q62'], prefix_results['Q57-Q64'],
               prefix_results['Q59-Q62'], prefix_results['Q59-Q64'],
               prefix_results['Q61-Q62'], prefix_results['Q61-Q64']]

print(f"\nWithin-perfect (Q57/59/61) mean: {sum(within_perfect)/3:.1f} chars")
print(f"Within-imperfect (Q62/64): {within_imperfect[0]} chars")
print(f"Cross-tense mean: {sum(cross_tense)/6:.1f} chars")

# Q 57+59 subpair (perfect)
q57_q59_prefix = prefix_results['Q57-Q59']
q57_q61_prefix = prefix_results['Q57-Q61']
q59_q61_prefix = prefix_results['Q59-Q61']
print(f"\nQ 57+59 subpair: {q57_q59_prefix}")
print(f"Q 57+61 subpair: {q57_q61_prefix}")
print(f"Q 59+61 subpair: {q59_q61_prefix}")
print(f"Subpair test: is Q 57+59 < Q 59+61? {q57_q59_prefix < q59_q61_prefix}")

# Cell B — root-overlap Jaccard between full surahs
# Use simple stem: strip common Arabic clitics + use unique-token signature
# This is a proxy for root-overlap — we use orthographic-token Jaccard
# (more rigorous root extraction would require QAC; this is a coarse proxy)
def token_set(words):
    return set(words)

print("\n=== Cell B — Surah-level token-set Jaccard ===")
jaccard_results = {}
for (a, b) in all_pairs:
    sa = token_set(surah_words[a])
    sb = token_set(surah_words[b])
    inter = len(sa & sb)
    uni = len(sa | sb)
    j = inter / uni if uni > 0 else 0
    jaccard_results[f"Q{a}-Q{b}"] = {'inter': inter, 'union': uni, 'jaccard': j}
    print(f"  Q{a}-Q{b}: |inter|={inter} |union|={uni} J={j:.4f}")

# Cell C — permutation null for Q 57/59 subpair vs random pair from short-Medinan block
# (Q 57-66 = H-NEW-1080's short-Medinan block, 10 surahs)
short_medinan = [57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
short_med_words = {}
short_med_v1 = {}
for sid in short_medinan:
    s = q[sid-1]
    all_words = []
    for v in s['verses']:
        all_words.extend(clean_text(v['text']).split())
    short_med_words[sid] = all_words
    short_med_v1[sid] = clean_text(s['verses'][0]['text'])

# Compute all C(10,2)=45 pair shared-prefixes within short-Medinan
print("\n=== Cell C — All 45 short-Medinan pairwise shared-prefixes ===")
short_med_pairs = list(combinations(short_medinan, 2))
short_med_prefix = []
for (a, b) in short_med_pairs:
    p = shared_prefix(short_med_v1[a], short_med_v1[b])
    short_med_prefix.append({'pair': f"Q{a}-Q{b}", 'prefix': p})

short_med_prefix_sorted = sorted(short_med_prefix, key=lambda x: -x['prefix'])
for entry in short_med_prefix_sorted[:10]:
    print(f"  {entry['pair']}: {entry['prefix']}")

# What rank does Q 57+59 subpair achieve?
ranks = {p['pair']: i+1 for i, p in enumerate(short_med_prefix_sorted)}
print(f"\nQ 57+59 rank in 45 short-Medinan pairs: {ranks['Q57-Q59']}")

# permutation null: how often does a random 5-of-10 subset match the musabbihat 5-prefix-sum?
# Already done in H-NEW-58c at corpus-wide level; here we tighten to short-Medinan
random.seed(SEED)
N_PERM = 10000
musabbihat_5 = [57, 59, 61, 62, 64]
obs_total = sum(prefix_results[f"Q{a}-Q{b}"] for (a, b) in all_pairs)
print(f"\nObserved musabbihat 5-prefix-sum: {obs_total}")

# Sample random 5-subsets from short-Medinan
short_med_set = short_medinan
greater_or_eq = 0
sums_null = []
for _ in range(N_PERM):
    subset = sorted(random.sample(short_med_set, 5))
    pairs = list(combinations(subset, 2))
    s = sum(shared_prefix(short_med_v1[a], short_med_v1[b]) for (a, b) in pairs)
    sums_null.append(s)
    if s >= obs_total:
        greater_or_eq += 1
p_short_med = greater_or_eq / N_PERM
print(f"p (musabbihat-5 prefix-sum >= obs) within short-Medinan random 5-subsets: {p_short_med:.4f}")

# Also sample random 2-subsets within short-Medinan to test Q 57+59 sub-pair
N_PAIR = 10000
random.seed(SEED + 1)
obs_q57_q59 = q57_q59_prefix
greater_eq_pair = 0
for _ in range(N_PAIR):
    a, b = random.sample(short_med_set, 2)
    p = shared_prefix(short_med_v1[a], short_med_v1[b])
    if p >= obs_q57_q59:
        greater_eq_pair += 1
p_pair_short_med = greater_eq_pair / N_PAIR
print(f"p (Q 57+59 prefix={obs_q57_q59} <= random short-Medinan pair) = {p_pair_short_med:.4f}")

# Bond-strength comparison: which is the TIGHTEST sub-pair within Q 57/59/61?
# H-NEW-58c reports: Q 57+59=24, Q 57+61=24, Q 59+61=56
# So Q 59+61 is the tightest sub-pair.
# Q 57+59 is the LOOSER sub-pair within the perfect-tense trio.
tightest_perfect = max(within_perfect)
print(f"\nTightest perfect-trio sub-pair: {tightest_perfect}")
print(f"Q 57+59: {q57_q59_prefix} {'EQUALS' if q57_q59_prefix == tightest_perfect else 'BELOW'} tightest")

prereg_sha = ''
if PREREG.exists():
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()

result = {
    'finding_id': 'Q059-F-02',
    'title': 'Q 57+59 perfect-tense sub-pair cohesion within musabbihat trio',
    'prereg_sha': prereg_sha,
    'seed': SEED,
    'n_perm': N_PERM,
    'rules_tuple': '(no-tashkeel, ornament-stripped, whitespace-tokenized, opening-verse-shared-prefix)',
    'authored_by': 'Waiel Al-Shujaa',
    'date': '2026-05-09',
    'cell_A_opening_prefix_pairs': prefix_results,
    'within_perfect_mean': sum(within_perfect)/3,
    'within_imperfect_value': within_imperfect[0],
    'cross_tense_mean': sum(cross_tense)/6,
    'cell_A_q57_q59_subpair_prefix': q57_q59_prefix,
    'cell_A_q57_q61_subpair_prefix': q57_q61_prefix,
    'cell_A_q59_q61_subpair_prefix': q59_q61_prefix,
    'cell_A_tightest_perfect_subpair_chars': tightest_perfect,
    'cell_A_q57_q59_is_tightest_perfect_subpair': q57_q59_prefix == tightest_perfect,
    'cell_A_q57_q59_is_below_tightest': q57_q59_prefix < tightest_perfect,
    'cell_B_surah_token_jaccard': jaccard_results,
    'cell_C_short_medinan_45_pair_prefix_sorted': short_med_prefix_sorted,
    'cell_C_q57_q59_rank_within_short_medinan_45': ranks['Q57-Q59'],
    'cell_C_q59_q61_rank_within_short_medinan_45': ranks['Q59-Q61'],
    'cell_D_permutation_null_5subset': {
        'observed_musabbihat_5prefix_sum': obs_total,
        'null_mean': sum(sums_null)/N_PERM,
        'p_one_sided_geq': p_short_med,
    },
    'cell_E_pair_null': {
        'observed_q57_q59_prefix': obs_q57_q59,
        'p_one_sided_geq_random_pair_short_medinan': p_pair_short_med,
    },
    'q57_q59_root_overlap_jaccard': jaccard_results['Q57-Q59']['jaccard'],
    'q59_q62_root_overlap_jaccard': jaccard_results['Q59-Q62']['jaccard'],
    'q59_q61_root_overlap_jaccard': jaccard_results['Q59-Q61']['jaccard'],
    'verdict': {
        'overall': 'TIGHTER-THAN-TRIO' if q57_q59_prefix > sum(within_perfect)/3 else 'BELOW-OR-AT-TRIO-MEAN',
        'q57_q59_vs_perfect_trio_mean': 'BELOW' if q57_q59_prefix < sum(within_perfect)/3 else 'AT-OR-ABOVE',
        'tightest_perfect_subpair_identification': 'Q59-Q61' if q59_q61_prefix == tightest_perfect else f'Q{[k for k,v in prefix_results.items() if v == tightest_perfect][0]}',
    }
}

OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(f"\nWrote: {OUT}")
print(f"Verdict: {result['verdict']['overall']}")
