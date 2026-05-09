#!/usr/bin/env python3
"""Q038-F-07 — Iblīs-narrative 7-pericope root-Jaccard cohesion vs length-matched corpus null.

Pre-reg: surahs/Q038-sad/Q038-F-07-iblis-narrative-cohesion-prereg.md
Pre-reg SHA256: 9778fb03e21170410a7b6041cf3784b3883cb8ddf63355f87cbdc88e023b0d95
Rules-tuple: (no-tashkeel, root-tokens via QAC-v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, hashlib, sys, os, random
from collections import defaultdict
from itertools import combinations

PREREG = '/Users/grey/Downloads/quran/surahs/Q038-sad/Q038-F-07-iblis-narrative-cohesion-prereg.md'
EXPECTED_SHA = '9778fb03e21170410a7b6041cf3784b3883cb8ddf63355f87cbdc88e023b0d95'
SEED = 20260509
N_PERM = 10000

MORPH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'

# Iblīs-narrative pericopes (locked in pre-reg)
PERICOPES = [
    ('Q 2:34',        2, 34, 34),
    ('Q 7:11-25',     7, 11, 25),
    ('Q 15:31-44',   15, 31, 44),
    ('Q 17:61-65',   17, 61, 65),
    ('Q 18:50',      18, 50, 50),
    ('Q 20:115-123', 20, 115, 123),
    ('Q 38:71-85',   38, 71, 85),
]


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
            # parse location like (1:1:1:1) -> surah:verse:word:segment
            loc_clean = loc.strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc_clean.split(':'))
            except ValueError:
                continue
            # find ROOT: in features
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

    # All verse keys (for null draws)
    all_verses = sorted(verse_roots.keys())

    # Observed: 7 pericopes
    obs_root_sets = []
    obs_lengths = []
    for label, s, v0, v1 in PERICOPES:
        rs = pericope_roots(verse_roots, s, v0, v1)
        obs_root_sets.append(rs)
        obs_lengths.append(v1 - v0 + 1)

    obs_J = mean_pairwise_jaccard(obs_root_sets)

    # Null: 10000 draws of 7 length-matched random pericopes from the corpus
    # For each pericope of length L, sample a random verse and take the L consecutive verses from the flat verse index
    null_Js = []
    for _ in range(N_PERM):
        null_sets = []
        for L in obs_lengths:
            # sample start such that L consecutive verses fit
            start = rng.randrange(0, len(all_verses) - L + 1)
            window = all_verses[start:start+L]
            rs = set()
            for vk in window:
                rs |= verse_roots.get(vk, set())
            null_sets.append(rs)
        null_Js.append(mean_pairwise_jaccard(null_sets))

    null_mean = sum(null_Js) / len(null_Js)
    null_std = (sum((x - null_mean)**2 for x in null_Js) / len(null_Js))**0.5
    p_greater = sum(1 for x in null_Js if x >= obs_J) / N_PERM

    direction_match = obs_J > null_mean

    if direction_match and p_greater < 0.05:
        verdict = 'CONFIRMED'
    elif direction_match and p_greater < 0.5:
        verdict = 'DIRECTIONAL'
    elif not direction_match:
        verdict = 'NULL' if obs_J >= null_mean - 0.5 * null_std else 'PRE-COMMIT-VIOLATION'
    else:
        verdict = 'NULL'

    # Per-pericope sizes for transparency
    pericope_summary = []
    for (label, s, v0, v1), rs, L in zip(PERICOPES, obs_root_sets, obs_lengths):
        pericope_summary.append({
            'label': label,
            'surah': s, 'verse_start': v0, 'verse_end': v1,
            'n_verses': L,
            'n_unique_roots': len(rs),
            'sample_roots': sorted(rs)[:15],
        })

    out = {
        'finding_id': 'Q038-F-07',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, root-tokens via QAC-v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'pericopes': pericope_summary,
        'pericope_lengths': obs_lengths,
        'observed_mean_pairwise_jaccard': obs_J,
        'null_mean': null_mean,
        'null_std': null_std,
        'p_greater_perm': p_greater,
        'direction_locked': 'TIGHTER (greater than null mean)',
        'direction_match': direction_match,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q038-sad/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q038-sad/csv/Q038-F-07.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Pericope sizes (verses): {obs_lengths}")
    print(f"Per-pericope unique roots: {[p['n_unique_roots'] for p in pericope_summary]}")
    print(f"Observed mean pairwise root-Jaccard: {obs_J:.6f}")
    print(f"Null mean: {null_mean:.6f}  std: {null_std:.6f}")
    print(f"p_greater (one-tailed perm): {p_greater:.4f}")
    print(f"Direction match (obs > null mean): {direction_match}")
    print(f"Verdict: {verdict}")


if __name__ == '__main__':
    main()
