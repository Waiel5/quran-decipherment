#!/usr/bin/env python3
"""
Q068-F-03 — singleton-letter cluster (Q 38 + Q 50 + Q 68) joint test on
WORD-LENGTH (Mann-Whitney U) and ROOT-RARITY (mean QAC Zipf-rank, perm null).
Coordinates with Q050-F-04 (axis-disjoint).
"""
import hashlib, json, math, os, random, re, sys
from collections import Counter, defaultdict

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f'{PROJECT}/surahs/Q068-al-qalam/preregs/Q068-F-03-singleton-cluster-wordlength-rootrarity-prereg.md'
EXPECTED_SHA = 'ce90bfc4654b5ce31d469248358d5c3c327c00f05d8a10af9725dda6e59b23e2'

with open(PREREG, 'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}')

SEED = 20260507
N_PERM = 10000
SINGLETONS = [38, 50, 68]
BONFERRONI_K = 2
ALPHA_BON = 0.05 / BONFERRONI_K

# --- Axis A: word-length distribution ---
ARABIC_LETTER = re.compile(r'[ء-ي]')
def norm_letters(s):
    s = s.replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    return ''.join(ARABIC_LETTER.findall(s))

with open(f'{PROJECT}/quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    quran = json.load(f)

singleton_word_lens = []
rest_word_lens = []
for s_idx, s in enumerate(quran):
    s_id = s_idx + 1
    for v in s['verses']:
        txt = v if isinstance(v, str) else v.get('text', '')
        for w in txt.split():
            wn = norm_letters(w)
            if not wn: continue
            (singleton_word_lens if s_id in SINGLETONS else rest_word_lens).append(len(wn))

# Mann-Whitney U (asymptotic)
def mannwhitney_u(x, y):
    """Returns (U_x, p_two_sided_normal_approx)."""
    nx = len(x); ny = len(y)
    combined = [(v, 0) for v in x] + [(v, 1) for v in y]
    combined.sort(key=lambda t: t[0])
    # Assign ranks with tie-correction
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j+1 < len(combined) and combined[j+1][0] == combined[i][0]:
            j += 1
        avg_rank = (i + j + 2) / 2.0  # 1-indexed
        for k in range(i, j+1):
            ranks[k] = avg_rank
        i = j + 1
    # sum of ranks for x
    R_x = sum(r for r,(_,grp) in zip(ranks, combined) if grp == 0)
    U_x = R_x - nx * (nx + 1) / 2.0
    U_y = nx * ny - U_x
    U = min(U_x, U_y)
    mu = nx * ny / 2.0
    # Tie correction for sigma
    tie_counts = Counter(v for v,_ in combined)
    T = sum(t**3 - t for t in tie_counts.values())
    nN = nx + ny
    sigma_sq = nx * ny / 12.0 * ((nN + 1) - T / (nN * (nN - 1)))
    sigma = math.sqrt(sigma_sq) if sigma_sq > 0 else 1.0
    z = (U_x - mu) / sigma  # signed: positive => x > y
    # two-sided
    from math import erf, sqrt
    p_two = 2 * (1 - 0.5 * (1 + erf(abs(z) / sqrt(2))))
    return {'U_singleton': U_x, 'U_rest': U_y, 'z': z, 'p_two_sided': p_two,
            'mean_singleton': sum(x)/len(x), 'mean_rest': sum(y)/len(y),
            'median_singleton': sorted(x)[len(x)//2], 'median_rest': sorted(y)[len(y)//2],
            'n_singleton': nx, 'n_rest': ny}

axis_A = mannwhitney_u(singleton_word_lens, rest_word_lens)

# --- Axis B: mean Zipf-rank of QAC roots ---
roots_per_surah = defaultdict(list)  # surah -> list of root tokens
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
                roots_per_surah[surah].append(rt)
                total_per_root[rt] += 1
                break

# Zipf rank: 1 = most common, ties broken by alphabetical
sorted_roots = sorted(total_per_root.items(), key=lambda x: (-x[1], x[0]))
zipf_rank = {r: i+1 for i, (r, _) in enumerate(sorted_roots)}

def mean_zipf(surah_list):
    tokens = []
    for s in surah_list:
        tokens.extend(roots_per_surah[s])
    if not tokens: return None
    return sum(zipf_rank.get(r, len(zipf_rank)+1) for r in tokens) / len(tokens)

singleton_mean_zipf = mean_zipf(SINGLETONS)
rest_mean_zipf = mean_zipf([s for s in range(1, 115) if s not in SINGLETONS])

# Permutation: shuffle surah-labels to a random size-3 cluster
all_surahs = list(range(1, 115))
rng = random.Random(SEED)
observed_diff = abs(singleton_mean_zipf - rest_mean_zipf)
ge_count = 0
sample_diffs = []
for _ in range(N_PERM):
    sample = rng.sample(all_surahs, 3)
    s_mean = mean_zipf(sample)
    r_mean = mean_zipf([s for s in all_surahs if s not in sample])
    diff = abs(s_mean - r_mean)
    sample_diffs.append(s_mean - r_mean)
    if diff >= observed_diff:
        ge_count += 1
p_axis_B = ge_count / N_PERM

# Verdict per axis
def cell_verdict(p):
    if p < ALPHA_BON: return 'VINDICATED'
    if p < 0.05: return 'DIRECTIONAL'
    return 'NULL'

axis_A_verdict = cell_verdict(axis_A['p_two_sided'])
axis_B_verdict = cell_verdict(p_axis_B)

passes = sum(1 for v in [axis_A_verdict, axis_B_verdict] if v == 'VINDICATED')
if passes == 2:
    joint = 'CLUSTER-DISTINCT-2-AXIS'
elif passes == 1:
    joint = 'CLUSTER-DISTINCT-1-AXIS'
else:
    joint = 'CLUSTER-NULL on word-length and root-rarity (singleton-architecture, if any, must be on Q050-F-04 axes)'

output = {
    'finding_id': 'Q068-F-03',
    'prereg_sha256': actual,
    'date_run': '2026-05-07',
    'seed': SEED,
    'n_perm': N_PERM,
    'singletons': SINGLETONS,
    'rules_tuple': '(no-tashkeel, QAC-stem-roots for axis B; orthographic-token graphemes for axis A; basmala-counted-only-in-Q1, Hafs-Kufan)',
    'axis_A_word_length': axis_A,
    'axis_A_verdict': axis_A_verdict,
    'axis_B_root_rarity_zipf': {
        'singleton_mean_zipf': singleton_mean_zipf,
        'rest_mean_zipf': rest_mean_zipf,
        'observed_abs_diff': observed_diff,
        'observed_signed_diff_singleton_minus_rest': singleton_mean_zipf - rest_mean_zipf,
        'p_value_perm_two_sided': p_axis_B,
        'distinct_roots_total': len(zipf_rank),
        'singleton_signed_diff_percentile': sum(1 for d in sample_diffs if d < (singleton_mean_zipf - rest_mean_zipf)) / N_PERM * 100,
    },
    'axis_B_verdict': axis_B_verdict,
    'alpha_raw': 0.05,
    'alpha_bonferroni_2': ALPHA_BON,
    'joint_verdict': joint,
    'coordination_with_Q050_F_04': 'AXIS-DISJOINT pre-registration; no Bonferroni overlap. Q050-F-04 covers FR-distance / sig_A / outlier; Q068-F-03 covers word-length / root-rarity.',
}

out_path = f'{PROJECT}/surahs/Q068-al-qalam/csv/Q068-F-03.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q068-F-03: JOINT VERDICT={joint}')
print(f'  Axis A (word-length, MW-U): mean_singleton={axis_A["mean_singleton"]:.3f} '
      f'mean_rest={axis_A["mean_rest"]:.3f} z={axis_A["z"]:.3f} p={axis_A["p_two_sided"]:.4f} '
      f'verdict={axis_A_verdict}')
print(f'  Axis B (root-rarity, mean Zipf-rank): singleton={singleton_mean_zipf:.2f} '
      f'rest={rest_mean_zipf:.2f} diff={singleton_mean_zipf - rest_mean_zipf:+.2f} '
      f'p_perm={p_axis_B:.4f} verdict={axis_B_verdict}')
print(f'  Output: {out_path}')
