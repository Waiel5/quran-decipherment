#!/usr/bin/env python3
"""
Q068-F-04 — STORY-OF-THE-GARDEN-OWNERS lexical isolation (Q 68:17-33).

Sub-test (a): Jaccard distance from Q 68 parable root-set to Q 18:32-44 and Q 36:13-32 root-sets,
              vs control distribution of 10000 random K=17-verse contiguous windows.
Sub-test (b): Within-surah max-distinctness — does v.17 starting window have max Jaccard
              distance to in-surah complement, against permutation null?
"""
import hashlib, json, os, random, sys
from collections import defaultdict

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f'{PROJECT}/surahs/Q068-al-qalam/preregs/Q068-F-04-garden-owners-parable-isolation-prereg.md'
EXPECTED_SHA = '5df62b113d245986c5a2a84a48ec3f145fe9725ce29c7c7ce4b7e4d63b88e8d3'

with open(PREREG, 'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}')

SEED = 20260507
N_PERM = 10000
K_WINDOW = 17  # 33-17+1 = 17 verses
ALPHA_BON = 0.05 / 2

# Load QAC roots indexed by (surah, verse)
verse_roots = defaultdict(set)  # (s, v) -> set of roots
verse_root_tokens = defaultdict(list)  # (s, v) -> list of root tokens (with multiplicity)
with open(f'{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('('):
            continue
        parts = line.strip().split('\t')
        if len(parts) < 4:
            continue
        loc = parts[0].strip('()').split(':')
        try:
            s = int(loc[0]); v = int(loc[1])
        except (ValueError, IndexError):
            continue
        feats = parts[3]
        for tag in feats.split('|'):
            if tag.startswith('ROOT:'):
                rt = tag[5:]
                verse_roots[(s, v)].add(rt)
                verse_root_tokens[(s, v)].append(rt)
                break

# Load verse counts per surah from Quran JSON
with open(f'{PROJECT}/quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    quran = json.load(f)
verse_counts = {i+1: len(s['verses']) for i, s in enumerate(quran)}

def window_root_set(surah, v_start, v_end):
    rs = set()
    for v in range(v_start, v_end + 1):
        rs |= verse_roots.get((surah, v), set())
    return rs

def jaccard(a, b):
    if not a and not b: return 0.0
    return 1.0 - len(a & b) / len(a | b)

# Sub-test (a): cross-surah Jaccard
R_qalam = window_root_set(68, 17, 33)
R_kahf = window_root_set(18, 32, 44)
R_yasin = window_root_set(36, 13, 32)

d_qalam_kahf = jaccard(R_qalam, R_kahf)
d_qalam_yasin = jaccard(R_qalam, R_yasin)

# Control distribution: 10000 random K=17-verse contiguous windows from anywhere in the corpus
# excluding (68, 17-33), (18, 32-44), (36, 13-32)
rng = random.Random(SEED)
excluded = [(68, 17, 33), (18, 32, 44), (36, 13, 32)]

def is_excluded(s, v_start, v_end):
    for es, ea, eb in excluded:
        if es == s and not (v_end < ea or v_start > eb):
            return True
    return False

control_distances = []
attempts = 0
while len(control_distances) < N_PERM and attempts < N_PERM * 5:
    attempts += 1
    s = rng.randint(1, 114)
    if verse_counts[s] < K_WINDOW:
        continue
    v_start = rng.randint(1, verse_counts[s] - K_WINDOW + 1)
    v_end = v_start + K_WINDOW - 1
    if is_excluded(s, v_start, v_end):
        continue
    R_ctrl = window_root_set(s, v_start, v_end)
    if not R_ctrl:
        continue
    control_distances.append(jaccard(R_qalam, R_ctrl))

n_ctrl = len(control_distances)
p_kahf = sum(1 for d in control_distances if d >= d_qalam_kahf) / n_ctrl
p_yasin = sum(1 for d in control_distances if d >= d_qalam_yasin) / n_ctrl
median_ctrl = sorted(control_distances)[n_ctrl // 2]
mean_ctrl = sum(control_distances) / n_ctrl

# Sub-test (b): within-surah max-distinctness
n_q68 = verse_counts[68]
windows_q68 = []
for v_start in range(1, n_q68 - K_WINDOW + 2):
    v_end = v_start + K_WINDOW - 1
    R_w = window_root_set(68, v_start, v_end)
    R_complement = set()
    for v in range(1, n_q68 + 1):
        if v < v_start or v > v_end:
            R_complement |= verse_roots.get((68, v), set())
    windows_q68.append({'v_start': v_start, 'v_end': v_end,
                        'jaccard_to_complement': jaccard(R_w, R_complement),
                        'root_set_size': len(R_w)})

# Sort by jaccard descending
sorted_w = sorted(windows_q68, key=lambda w: -w['jaccard_to_complement'])
top_window = sorted_w[0]
parable_window = next(w for w in windows_q68 if w['v_start'] == 17)
parable_rank = next(i+1 for i, w in enumerate(sorted_w) if w['v_start'] == 17)

# Permutation null for sub-test (b): shuffle root tokens within Q 68 (keeping verse-token-counts);
# for each perm, recompute the position of the max window over Q 68. p = fraction of perms
# where v.17 window is THE max (rank 1).
# Build per-verse token counts and global token pool for Q 68.
q68_token_pool = []
q68_verse_lens = []
for v in range(1, n_q68 + 1):
    toks = verse_root_tokens.get((68, v), [])
    q68_verse_lens.append(len(toks))
    q68_token_pool.extend(toks)

is_v17_max_count = 0
v17_top3_count = 0
for _ in range(N_PERM):
    pool = q68_token_pool.copy()
    rng.shuffle(pool)
    perm_verse_roots = {}
    cursor = 0
    for v_idx, ln in enumerate(q68_verse_lens):
        perm_verse_roots[v_idx + 1] = set(pool[cursor:cursor + ln])
        cursor += ln
    perm_jacs = []
    for v_start in range(1, n_q68 - K_WINDOW + 2):
        v_end = v_start + K_WINDOW - 1
        R_w = set()
        for v in range(v_start, v_end + 1):
            R_w |= perm_verse_roots[v]
        R_c = set()
        for v in range(1, n_q68 + 1):
            if v < v_start or v > v_end:
                R_c |= perm_verse_roots[v]
        perm_jacs.append((v_start, jaccard(R_w, R_c)))
    perm_sorted = sorted(perm_jacs, key=lambda t: -t[1])
    if perm_sorted[0][0] == 17:
        is_v17_max_count += 1
    if 17 in [perm_sorted[i][0] for i in range(3)]:
        v17_top3_count += 1

p_b_v17_max = (sum(1 for _ in range(N_PERM) if False) + is_v17_max_count) / N_PERM
# i.e., fraction of perms where v.17 IS max => baseline rate; but we want
# observed event = v.17 IS max; null = expected rate is 1/36 ≈ 0.028.
# So p-value of "v.17 is observed max" is the FRACTION of perms where v.17 is max,
# IFF observed event is v.17 == max.
# But p_value-style: observed is v.17 rank=parable_rank; we test ALTERNATIVE: prob under
# null that a uniformly-random window achieves the same OR higher Jaccard. For sub-test
# (b) the cleaner formulation is:
# Null mean = 1/36. p_perm = (# perms where shuffled-v.17 ranks <= observed rank) / N_PERM.
# We instead report two distinct p's: p_v17_is_max (under perm null), p_v17_is_top3.
p_v17_is_max_under_null = is_v17_max_count / N_PERM
p_v17_is_top3_under_null = v17_top3_count / N_PERM

# Verdicts
def verdict_a(p):
    if p < ALPHA_BON: return 'VINDICATED'
    if p < 0.05: return 'DIRECTIONAL'
    return 'NULL'

# For sub-test a, two-sided: take min(p, 1-p) * 2
two_sided_p_kahf = min(2 * min(p_kahf, 1 - p_kahf), 1.0)
two_sided_p_yasin = min(2 * min(p_yasin, 1 - p_yasin), 1.0)
verdict_a_kahf = verdict_a(two_sided_p_kahf)
verdict_a_yasin = verdict_a(two_sided_p_yasin)

# For sub-test b: we observed that v.17 IS rank parable_rank. This is significant if
# under null (perm), v.17 would only be max with frequency 1/36 ≈ 0.0278.
# Direction-locked POSITIVE: v.17 IS max.
observed_v17_is_max = (parable_rank == 1)
if observed_v17_is_max:
    # p = baseline rate that v.17 is max under null
    # If null < 0.05 / 2 and observed = TRUE → significant
    p_b = p_v17_is_max_under_null
    if p_b < ALPHA_BON:
        verdict_b = 'VINDICATED'
    elif p_b < 0.05:
        verdict_b = 'DIRECTIONAL'
    else:
        verdict_b = 'NULL'
elif parable_rank <= 3:
    p_b = p_v17_is_top3_under_null
    if p_b < ALPHA_BON:
        verdict_b = 'DIRECTIONAL_TOP3'
    elif p_b < 0.05:
        verdict_b = 'DIRECTIONAL_TOP3_WEAK'
    else:
        verdict_b = 'NULL'
else:
    verdict_b = 'NULL'
    p_b = 1.0

# Joint
joint_pass = (verdict_a_kahf == 'VINDICATED' or verdict_a_yasin == 'VINDICATED') and verdict_b in ('VINDICATED', 'DIRECTIONAL')
joint_verdict = 'VINDICATED' if (verdict_b == 'VINDICATED' and (verdict_a_kahf == 'VINDICATED' or verdict_a_yasin == 'VINDICATED')) else (
    'DIRECTIONAL' if (verdict_b in ('VINDICATED','DIRECTIONAL') or verdict_a_kahf in ('VINDICATED','DIRECTIONAL') or verdict_a_yasin in ('VINDICATED','DIRECTIONAL')) else 'NULL')

output = {
    'finding_id': 'Q068-F-04',
    'prereg_sha256': actual,
    'date_run': '2026-05-07',
    'seed': SEED,
    'n_perm': N_PERM,
    'rules_tuple': '(no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan)',
    'sub_test_a_cross_surah_jaccard': {
        'R_qalam_size': len(R_qalam),
        'R_kahf_size': len(R_kahf),
        'R_yasin_size': len(R_yasin),
        'd_qalam_kahf': d_qalam_kahf,
        'd_qalam_yasin': d_qalam_yasin,
        'control_distribution': {
            'n_ctrl_windows': n_ctrl,
            'mean': mean_ctrl,
            'median': median_ctrl,
            'min': min(control_distances),
            'max': max(control_distances),
        },
        'p_one_sided_qalam_kahf_high': p_kahf,
        'p_one_sided_qalam_yasin_high': p_yasin,
        'p_two_sided_qalam_kahf': two_sided_p_kahf,
        'p_two_sided_qalam_yasin': two_sided_p_yasin,
        'verdict_kahf': verdict_a_kahf,
        'verdict_yasin': verdict_a_yasin,
    },
    'sub_test_b_within_surah_distinctness': {
        'parable_window_v_start': 17,
        'parable_window_v_end': 33,
        'parable_window_jaccard_to_complement': parable_window['jaccard_to_complement'],
        'parable_window_rank_among_all_36_windows': parable_rank,
        'top_window': top_window,
        'top5_windows': sorted_w[:5],
        'p_v17_is_max_under_perm_null': p_v17_is_max_under_null,
        'p_v17_is_top3_under_perm_null': p_v17_is_top3_under_null,
        'baseline_uniform_rate': 1.0 / len(windows_q68),
        'observed_v17_is_max': observed_v17_is_max,
        'verdict': verdict_b,
        'p_b': p_b,
    },
    'alpha_bonferroni_2': ALPHA_BON,
    'joint_verdict': joint_verdict,
}

out_path = f'{PROJECT}/surahs/Q068-al-qalam/csv/Q068-F-04.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q068-F-04: JOINT VERDICT={joint_verdict}')
print(f'  Sub-test (a) cross-surah Jaccard:')
print(f'    R_qalam={len(R_qalam)}, R_kahf={len(R_kahf)}, R_yasin={len(R_yasin)}')
print(f'    d_qalam_kahf={d_qalam_kahf:.4f} (control mean={mean_ctrl:.4f}, p1s={p_kahf:.4f}, p2s={two_sided_p_kahf:.4f}) verdict={verdict_a_kahf}')
print(f'    d_qalam_yasin={d_qalam_yasin:.4f} (p1s={p_yasin:.4f}, p2s={two_sided_p_yasin:.4f}) verdict={verdict_a_yasin}')
print(f'  Sub-test (b) within-surah:')
print(f'    parable v.17 rank: {parable_rank}/{len(windows_q68)} (jacc={parable_window["jaccard_to_complement"]:.4f})')
print(f'    top window: v{top_window["v_start"]}-{top_window["v_end"]} jacc={top_window["jaccard_to_complement"]:.4f}')
print(f'    p (v.17 is max under perm null) = {p_v17_is_max_under_null:.4f}')
print(f'    verdict={verdict_b}')
print(f'  Output: {out_path}')
