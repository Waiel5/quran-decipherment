#!/usr/bin/env python3
"""Q029-F-02 — ALM-4 cluster {Q 29, 30, 31, 32} pericope-window root-Jaccard cohesion (first 3 verses).

Pre-reg: surahs/Q029-al-ankabut/preregs/Q029-F-02-alm-4-pericope-cohesion-prereg.md
Pre-reg SHA256: 3d4acccc01e01985bcdbef1b4dcd4dd5c7005878862dbd291a7159c4406994d8
Rules-tuple: (no-tashkeel, root-tokens via QAC-v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import hashlib
import json
import os
import random
import sys
from collections import defaultdict
from itertools import combinations

PREREG = '/Users/grey/Downloads/quran/surahs/Q029-al-ankabut/preregs/Q029-F-02-alm-4-pericope-cohesion-prereg.md'
EXPECTED_SHA = '3d4acccc01e01985bcdbef1b4dcd4dd5c7005878862dbd291a7159c4406994d8'
MORPH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
OUT = '/Users/grey/Downloads/quran/surahs/Q029-al-ankabut/csv/Q029-F-02.json'

SEED = 20260509
N_PERM = 10000
ALPHA = 0.05

# ALM-4 Late-Meccan sub-cluster — locked surface form
PERICOPES = [
    ('Q 29:1-3', 29, 1, 3),
    ('Q 30:1-3', 30, 1, 3),
    ('Q 31:1-3', 31, 1, 3),
    ('Q 32:1-3', 32, 1, 3),
]
PERICOPE_LEN = 3


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set of ROOT strings} from QAC v0.4."""
    verse_roots = defaultdict(set)
    with open(MORPH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            loc_clean = loc.strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc_clean.split(':'))
            except ValueError:
                continue
            for tok in features.split('|'):
                if tok.startswith('ROOT:'):
                    root = tok[len('ROOT:'):]
                    verse_roots[(s, v)].add(root)
                    break
    return dict(verse_roots)


def pericope_roots(verse_roots, surah, vstart, vend):
    out = set()
    for v in range(vstart, vend + 1):
        out |= verse_roots.get((surah, v), set())
    return out


def mean_pairwise_jaccard(root_sets):
    pairs = list(combinations(range(len(root_sets)), 2))
    if not pairs:
        return 0.0
    vals = []
    for i, j in pairs:
        a, b = root_sets[i], root_sets[j]
        if not a and not b:
            vals.append(0.0)
            continue
        u = a | b
        if not u:
            vals.append(0.0)
            continue
        vals.append(len(a & b) / len(u))
    return sum(vals) / len(vals)


def main():
    verify_sha()
    rng = random.Random(SEED)

    verse_roots = load_qac_roots_by_verse()

    # All verse keys (sorted by (surah, verse) -> flat index)
    all_verses = sorted(verse_roots.keys())
    # Map flat index -> verse key for null-draw windows
    # We need contiguous 3-verse windows; respect surah boundaries by skipping any window that crosses surah boundary.
    # Approach: enumerate all valid 3-verse contiguous windows within a single surah.
    by_surah = defaultdict(list)
    for (s, v) in all_verses:
        by_surah[s].append(v)
    for s in by_surah:
        by_surah[s].sort()

    # Build list of valid (surah, vstart) for length-3 windows
    candidate_starts = []
    blocked = {(29, 1), (30, 1), (31, 1), (32, 1)}
    for s, verses in by_surah.items():
        # ensure sequential 1..N
        for i in range(len(verses) - PERICOPE_LEN + 1):
            v0 = verses[i]
            # require v0..v0+L-1 all present and contiguous
            if all((s, v0 + k) in verse_roots or (s, v0 + k) == (s, v0 + k) for k in range(PERICOPE_LEN)):
                # contiguous check: verses[i+k] == v0 + k
                ok = True
                for k in range(PERICOPE_LEN):
                    if i + k >= len(verses) or verses[i + k] != v0 + k:
                        ok = False
                        break
                if not ok:
                    continue
                if (s, v0) in blocked:
                    continue
                candidate_starts.append((s, v0))

    # Observed pericopes
    obs_root_sets = []
    for label, s, v0, v1 in PERICOPES:
        obs_root_sets.append(pericope_roots(verse_roots, s, v0, v1))

    obs_J = mean_pairwise_jaccard(obs_root_sets)
    obs_sizes = [len(rs) for rs in obs_root_sets]

    # Per-pair observed values
    obs_pairs = []
    labels = [p[0] for p in PERICOPES]
    for i, j in combinations(range(len(PERICOPES)), 2):
        a, b = obs_root_sets[i], obs_root_sets[j]
        u = a | b
        jij = (len(a & b) / len(u)) if u else 0.0
        obs_pairs.append({
            'pair': f'{labels[i]} ↔ {labels[j]}',
            'jaccard': jij,
            'intersection_size': len(a & b),
            'union_size': len(u),
            'intersection_roots': sorted(a & b),
        })

    # Null distribution: 10,000 draws of 4 length-matched (length=3) random pericopes
    null_Js = []
    for _ in range(N_PERM):
        sample = rng.sample(candidate_starts, len(PERICOPES))
        null_sets = []
        for (s, v0) in sample:
            null_sets.append(pericope_roots(verse_roots, s, v0, v0 + PERICOPE_LEN - 1))
        null_Js.append(mean_pairwise_jaccard(null_sets))

    null_mean = sum(null_Js) / len(null_Js)
    null_std = (sum((x - null_mean) ** 2 for x in null_Js) / len(null_Js)) ** 0.5
    null_max = max(null_Js)
    null_min = min(null_Js)
    p_greater = sum(1 for x in null_Js if x >= obs_J) / N_PERM
    z = (obs_J - null_mean) / null_std if null_std > 0 else 0.0
    pct = sum(1 for x in null_Js if x < obs_J) / N_PERM

    direction_match = obs_J > null_mean

    if direction_match and p_greater <= ALPHA:
        verdict = 'PASS-DIRECTED'
    elif direction_match and p_greater <= 0.5:
        verdict = 'DIRECTIONAL'
    elif direction_match:
        verdict = 'NULL'
    else:
        if obs_J < null_mean - 0.5 * null_std:
            verdict = 'PRE-COMMIT-VIOLATION'
        else:
            verdict = 'NULL'

    out = {
        'finding_id': 'Q029-F-02',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'alpha': ALPHA,
        'rules_tuple': '(no-tashkeel, root-tokens via QAC-v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'pericopes': [{'label': p[0], 'surah': p[1], 'v_start': p[2], 'v_end': p[3],
                       'n_roots': len(rs), 'roots': sorted(rs)}
                      for p, rs in zip(PERICOPES, obs_root_sets)],
        'pericope_root_sizes': obs_sizes,
        'observed_mean_pairwise_jaccard': obs_J,
        'observed_pair_jaccards': obs_pairs,
        'null_mean': null_mean,
        'null_std': null_std,
        'null_min': null_min,
        'null_max': null_max,
        'p_one_sided_ge_perm': p_greater,
        'z_score': z,
        'percentile_of_obs': pct,
        'n_candidate_windows': len(candidate_starts),
        'direction_locked': 'TIGHTER (J_mean > null mean)',
        'direction_match': direction_match,
        'verdict': verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q029-F-02 results:")
    print(f"  Pericopes (root-counts): {dict(zip([p[0] for p in PERICOPES], obs_sizes))}")
    print(f"  Observed mean pairwise root-Jaccard: {obs_J:.6f}")
    print(f"  Null mean: {null_mean:.6f}  std: {null_std:.6f}  (n={N_PERM})")
    print(f"  p_greater (one-tailed perm): {p_greater:.4f};  z={z:.3f};  pct={pct:.4f}")
    print(f"  Direction match: {direction_match}")
    print(f"  Verdict: {verdict}")
    print(f"  Per-pair Jaccards:")
    for p in obs_pairs:
        print(f"    {p['pair']:30s}  J={p['jaccard']:.4f}  |A∩B|={p['intersection_size']:3d}  |A∪B|={p['union_size']:3d}")
    print(f"Written: {OUT}")


if __name__ == '__main__':
    main()
