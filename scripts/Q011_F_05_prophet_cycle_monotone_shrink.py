#!/usr/bin/env python3
"""Q011-F-05 — Q 11 prophet-cycle monotone shrinkage (within-surah compression).

Pre-reg: surahs/Q011-hud/preregs/Q011-F-05-prophet-cycle-monotone-shrink-prereg.md
Pre-reg SHA256: c4bb22a7adf749c20b043a368fc53293353e5d2c1620f1873767fcb445b758dd
Rules-tuple: (no-tashkeel, verse-count, al-Biqāʿī-anchored-block-bounds,
              7-block-with-coda, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed: 20260507
"""
import json, hashlib, sys, os, random
from itertools import permutations

PREREG = '/Users/grey/Downloads/quran/surahs/Q011-hud/preregs/Q011-F-05-prophet-cycle-monotone-shrink-prereg.md'
EXPECTED_SHA = 'c4bb22a7adf749c20b043a368fc53293353e5d2c1620f1873767fcb445b758dd'
SEED = 20260507
N_PERM = 10000

# Locked block segmentation (verse-counts)
BLOCKS = [
    {'idx': 1, 'prophet': 'Nūḥ',       'lo': 25, 'hi': 49, 'verses': 25},
    {'idx': 2, 'prophet': 'Hūd',       'lo': 50, 'hi': 60, 'verses': 11},
    {'idx': 3, 'prophet': 'Ṣāliḥ',     'lo': 61, 'hi': 68, 'verses':  8},
    {'idx': 4, 'prophet': 'Ibrāhīm+Lūṭ','lo': 69,'hi': 83, 'verses': 15},
    {'idx': 5, 'prophet': 'Shuʿayb',   'lo': 84, 'hi': 95, 'verses': 12},
    {'idx': 6, 'prophet': 'Mūsā',      'lo': 96, 'hi': 99, 'verses':  4},
    {'idx': 7, 'prophet': 'Pedagog-coda','lo':100,'hi':108, 'verses':  9},
]


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def spearman(x, y):
    """Spearman rank correlation (with average-rank tie handling)."""
    def avg_ranks(a):
        sorted_idx = sorted(range(len(a)), key=lambda i: a[i])
        ranks = [0.0]*len(a)
        i = 0
        while i < len(a):
            j = i
            while j+1 < len(a) and a[sorted_idx[j+1]] == a[sorted_idx[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1
            for k in range(i, j+1):
                ranks[sorted_idx[k]] = avg
            i = j + 1
        return ranks
    rx = avg_ranks(x)
    ry = avg_ranks(y)
    n = len(x)
    mean_rx = sum(rx)/n
    mean_ry = sum(ry)/n
    num = sum((rx[i]-mean_rx)*(ry[i]-mean_ry) for i in range(n))
    dx = sum((r-mean_rx)**2 for r in rx) ** 0.5
    dy = sum((r-mean_ry)**2 for r in ry) ** 0.5
    if dx == 0 or dy == 0:
        return 0.0
    return num / (dx * dy)


def main():
    verify_sha()

    # Verify block bounds against canonical text
    with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
        d = json.load(f)
    q11 = next(s for s in d if s['id'] == 11)
    for b in BLOCKS:
        actual = sum(1 for v in q11['verses'] if b['lo'] <= v['id'] <= b['hi'])
        if actual != b['verses']:
            print(f"WARN: block {b['idx']} ({b['prophet']}) expected {b['verses']} but got {actual}", file=sys.stderr)
            b['verses'] = actual

    cycle_idx = [b['idx'] for b in BLOCKS]
    verse_counts = [b['verses'] for b in BLOCKS]

    rho_obs = spearman(cycle_idx, verse_counts)

    # Permutation null: random orderings of verse-counts assigned to indices
    rng = random.Random(SEED)
    n = len(verse_counts)
    le_count = 0
    # 7! = 5040, fewer than 10000 perms, so we can do exact + Monte Carlo blend
    # For honesty, sample N_PERM random perms with replacement
    for _ in range(N_PERM):
        permuted = verse_counts[:]
        rng.shuffle(permuted)
        rho_perm = spearman(cycle_idx, permuted)
        if rho_perm <= rho_obs:
            le_count += 1
    p_lower = (le_count + 1) / (N_PERM + 1)

    # Exact enumeration verification (since 7! = 5040)
    le_exact = 0
    total_exact = 0
    for perm in permutations(verse_counts):
        rho_p = spearman(cycle_idx, list(perm))
        if rho_p <= rho_obs:
            le_exact += 1
        total_exact += 1
    p_lower_exact = le_exact / total_exact

    if rho_obs <= -0.6 and p_lower <= 0.05:
        verdict = 'CONFIRMED'
    elif rho_obs < 0 and p_lower <= 0.15:
        verdict = 'DIRECTIONAL'
    elif rho_obs >= 0 or p_lower > 0.15:
        verdict = 'NULL'
    else:
        verdict = 'NULL'
    if p_lower >= 0.95:
        verdict = 'NULL — pre-commit-violation candidate (rho strongly positive)'

    out = {
        'finding_id': 'Q011-F-05',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, verse-count, al-Biqāʿī-anchored-block-bounds, 7-block-with-coda, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'blocks': BLOCKS,
        'cycle_index': cycle_idx,
        'verse_counts': verse_counts,
        'spearman_rho': rho_obs,
        'p_lower_perm': p_lower,
        'p_lower_exact_enumeration': p_lower_exact,
        'exact_total_permutations': total_exact,
        'verdict': verdict,
    }
    out_dir = '/Users/grey/Downloads/quran/surahs/Q011-hud/csv'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'Q011-F-05.json'), 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Q011-F-05 verdict: {verdict}")
    print(f"  Spearman ρ: {rho_obs:.4f}")
    print(f"  p_lower (perm): {p_lower:.4f}")
    print(f"  p_lower (exact 5040 perms): {p_lower_exact:.4f}")
    print(f"  blocks: {[(b['idx'], b['prophet'], b['verses']) for b in BLOCKS]}")


if __name__ == '__main__':
    main()
