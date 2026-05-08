#!/usr/bin/env python3
"""Q018-F-01: Four-narrative architectural balance — word-count parity test (LOCKED pre-reg).

Tests whether Q 18's four narratives (cave-companions, two gardens, Mūsā-Khaḍir,
Dhū al-Qarnayn) are MORE balanced in verse-count, word-count, and root-token-count
than randomly-placed blocks of the same lengths in a 110-verse surah.

Data sources:
- /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
- /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
"""
import json, re, hashlib, random, os, sys
from collections import Counter

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q018-al-kahf/preregs/Q018-F-01-narrative-balance-prereg.md"
QURAN = f"{PROJECT}/quran-text/quran-no-tashkeel.json"
QAC = f"{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT = f"{PROJECT}/surahs/Q018-al-kahf/csv/Q018-F-01.json"

# Locked block boundaries (from H-NEW-268 + classical N4 endpoint v.101)
BLOCKS = {
    'N1_kahf': (9, 26),
    'N2_gardens': (32, 44),
    'N3_musa_khadir': (60, 82),
    'N4_dhu_qarnayn': (83, 101),
}
SEED = 18001
N_PERM = 10000
ALPHA_BON = 0.05 / 3

# 1. SHA-check pre-reg
sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
print(f"Pre-reg SHA256: {sha}")

# 2. Load Q 18 verses
q = json.load(open(QURAN))
q18 = q[17]
verses = {v['id']: v['text'] for v in q18['verses']}
assert len(verses) == 110

# Strip mushaf marks
MUSHAF_RE = re.compile(r'[۞۩ۚۖۗۛۧۜ]')
def words(text):
    clean = MUSHAF_RE.sub('', text)
    return [w for w in clean.split() if w]

# 3. Per-verse word count
verse_words = {vid: len(words(t)) for vid, t in verses.items()}

# 4. Load QAC roots per verse
verse_roots = {}
with open(QAC) as f:
    for line in f:
        if not line.startswith('(18:'): continue
        m = re.match(r'\(18:(\d+):\d+:\d+\)\s+\S+\s+\S+\s+(.*)', line)
        if not m: continue
        v = int(m.group(1))
        feat = m.group(2)
        rm = re.search(r'ROOT:([^|\s]+)', feat)
        if rm:
            verse_roots.setdefault(v, []).append(rm.group(1))
verse_root_count = {v: len(rs) for v, rs in verse_roots.items()}

# 5. Compute per-block stats
def block_stats(start, end):
    n_verses = end - start + 1
    n_words = sum(verse_words.get(v, 0) for v in range(start, end + 1))
    n_roots = sum(verse_root_count.get(v, 0) for v in range(start, end + 1))
    return n_verses, n_words, n_roots

block_data = {name: block_stats(*span) for name, span in BLOCKS.items()}
print('\nBlock stats:')
for name, (nv, nw, nr) in block_data.items():
    print(f'  {name:18s} verses={nv:3d} words={nw:4d} roots={nr:4d}')

verse_counts = [d[0] for d in block_data.values()]
word_counts = [d[1] for d in block_data.values()]
root_counts = [d[2] for d in block_data.values()]
ratio_v = max(verse_counts) / min(verse_counts)
ratio_w = max(word_counts) / min(word_counts)
ratio_r = max(root_counts) / min(root_counts)
print(f'\nObserved max/min ratios: verses={ratio_v:.4f}, words={ratio_w:.4f}, roots={ratio_r:.4f}')

# 6. Permutation null
# Block lengths from observed
block_lengths = [d[0] for d in block_data.values()]
TOTAL_VERSES = 110
random.seed(SEED)

def random_placement():
    """Place 4 non-overlapping blocks of the given lengths in 110 verses, ordered."""
    while True:
        # Sample 4 starts s.t. blocks fit and don't overlap
        # Simpler: use exact ordered placement: gaps g0, g1, g2, g3, g4 with g_i >= 0 and sum(blocks) + sum(gaps) = 110
        # We want a uniform sample over valid placements.
        L = sum(block_lengths)
        slack = TOTAL_VERSES - L  # = 110 - 73 = 37 (or 70 if length 70)
        if slack < 0:
            return None
        # Sample 5 nonneg gaps summing to slack
        # Use stars-and-bars uniform
        breaks = sorted(random.choices(range(slack + 1), k=4))  # not uniform; use proper sampling
        # Proper: choose 4 cuts in slack+5-1 positions
        # Let's just sample gap tuple directly via dirichlet-like approach
        # Easier: random.sample of 4 unique cut points from 0..slack
        # Uniform sample over compositions of slack into 5 parts:
        # cuts = sorted(random.sample(range(slack + 5), 4))
        cuts = sorted(random.sample(range(slack + 4), 4))  # but this gives compositions with non-strict
        gaps = [cuts[0]] + [cuts[i] - cuts[i-1] - 1 for i in range(1, 4)] + [slack + 3 - cuts[-1]]
        # Adjust: standard stars-and-bars with k=5 nonneg parts summing to slack
        # parts = c_i = stars between bars; we need sample of (g0..g4) >= 0 sum = slack
        # use: indices of 4 bars among slack+4 positions
        idx = sorted(random.sample(range(slack + 4), 4))
        # gaps = [idx[0], idx[1]-idx[0]-1, ..., (slack+4-1)-idx[3]]
        # but counts: g0 = idx[0], g_i = idx[i]-idx[i-1]-1 for i=1..3, g4 = (slack+4)-1-idx[3]
        # equivalent stars-and-bars
        g = [idx[0]]
        for i in range(1, 4):
            g.append(idx[i] - idx[i-1] - 1)
        g.append(slack + 4 - 1 - idx[-1])
        # check
        if sum(g) != slack:
            continue
        # block_starts:
        starts = []
        cur = 1 + g[0]
        for i, L_i in enumerate(block_lengths):
            starts.append(cur)
            cur += L_i + g[i+1]
        # sanity: cur - 1 == sum lengths + sum gaps starting from 1, plus gaps_after
        return starts

def block_stats_random(starts):
    counts_v = block_lengths[:]
    counts_w, counts_r = [], []
    for s, L in zip(starts, block_lengths):
        end = s + L - 1
        counts_w.append(sum(verse_words.get(v, 0) for v in range(s, end + 1)))
        counts_r.append(sum(verse_root_count.get(v, 0) for v in range(s, end + 1)))
    return counts_v, counts_w, counts_r

# Run nulls
null_v_ratios = []
null_w_ratios = []
null_r_ratios = []
for _ in range(N_PERM):
    starts = random_placement()
    if starts is None: continue
    cv, cw, cr = block_stats_random(starts)
    null_v_ratios.append(max(cv) / min(cv))
    null_w_ratios.append(max(cw) / min(cw))
    null_r_ratios.append(max(cr) / min(cr) if min(cr) > 0 else float('inf'))

def p_value(observed, null_dist):
    # one-tailed: P(null <= observed)
    return sum(1 for x in null_dist if x <= observed) / len(null_dist)

p_v = p_value(ratio_v, null_v_ratios)
p_w = p_value(ratio_w, null_w_ratios)
p_r = p_value(ratio_r, null_r_ratios)

med_v = sorted(null_v_ratios)[len(null_v_ratios)//2]
med_w = sorted(null_w_ratios)[len(null_w_ratios)//2]
med_r = sorted(null_r_ratios)[len(null_r_ratios)//2]

print(f'\nNull medians: verses={med_v:.4f}, words={med_w:.4f}, roots={med_r:.4f}')
print(f'p-values (one-tailed, observed <= null): verses={p_v:.4f}, words={p_w:.4f}, roots={p_r:.4f}')

def cell_verdict(p, ratio, med):
    if ratio > med:
        return 'NULL_PRECOMMIT_VIOLATION'
    if p < ALPHA_BON:
        return 'CONFIRMED'
    if p < 0.05:
        return 'DIRECTIONAL'
    return 'NULL'

verdict_v = cell_verdict(p_v, ratio_v, med_v)
verdict_w = cell_verdict(p_w, ratio_w, med_w)
verdict_r = cell_verdict(p_r, ratio_r, med_r)

n_confirmed = sum(1 for v in [verdict_v, verdict_w, verdict_r] if v == 'CONFIRMED')
combined = f'CONFIRMED on {n_confirmed}/3 cells'

result = {
    'finding_id': 'Q018-F-01',
    'pre_reg_sha256': sha,
    'verdict': combined,
    'cells': {
        'A_verses': {'observed_ratio': ratio_v, 'null_median': med_v, 'p': p_v, 'verdict': verdict_v},
        'B_words': {'observed_ratio': ratio_w, 'null_median': med_w, 'p': p_w, 'verdict': verdict_w},
        'C_roots': {'observed_ratio': ratio_r, 'null_median': med_r, 'p': p_r, 'verdict': verdict_r},
    },
    'block_data': {n: {'verses': d[0], 'words': d[1], 'roots': d[2]} for n, d in block_data.items()},
    'block_lengths_verses': block_lengths,
    'n_perm': N_PERM,
    'seed': SEED,
    'alpha_bonferroni': ALPHA_BON,
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, default=str)
print('\nResult:', json.dumps(result, indent=2, default=str)[:2000])
print(f'\nWritten to {OUT}')
