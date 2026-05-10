#!/usr/bin/env python3
"""H-NEW-1510 — pericope-scale flip test for the sajda 15-verse cluster.

Re-tests the H-NEW-1330 NULL (14-surah sajda cluster, whole-surah FR) at the
pericope-scale (each sajda verse ± 2 verses, clipped to surah boundaries),
following the H-NEW-1380 scale-of-aggregation principle (MASTER-FINDINGS-LEDGER §10.51).

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1510-sajda-pericope-replication.md
Pre-reg SHA256: fab8c413105c9867253a49bc09765e3313d22bb6f59688f8a4642048c4d00581

Direction lock: TIGHTER (J_mean > null_mean). Seed 20260509, n_perm=10000.
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import json
import hashlib
import sys
import os
import random
from collections import defaultdict
from itertools import combinations

PROJECT_ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/prereg-h-new-1510-sajda-pericope-replication.md')
EXPECTED_SHA = 'fab8c413105c9867253a49bc09765e3313d22bb6f59688f8a4642048c4d00581'
SEED = 20260509
N_PERM = 10000

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN_JSON = os.path.join(PROJECT_ROOT, 'quran-text/quran-no-tashkeel.json')
OUT_JSON = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/csv/h-new-1510.json')

# 15 sajda verses (classical-Sunnī 14 + Q 22:77 second sajda per Q022-F-06)
# Format: (label, surah, sajda_verse). Window = [v-2..v+2] clipped to [1..n_surah]
SAJDA_VERSES = [
    ('Q 7:206',  7, 206),
    ('Q 13:15', 13,  15),
    ('Q 16:50', 16,  50),
    ('Q 17:109',17, 109),
    ('Q 19:58', 19,  58),
    ('Q 22:18', 22,  18),
    ('Q 22:77', 22,  77),
    ('Q 25:60', 25,  60),
    ('Q 27:26', 27,  26),
    ('Q 32:15', 32,  15),
    ('Q 38:24', 38,  24),
    ('Q 41:38', 41,  38),
    ('Q 53:62', 53,  62),
    ('Q 84:21', 84,  21),
    ('Q 96:19', 96,  19),
]

WINDOW = 2  # ±2 verses

# 14-surah set used by H-NEW-1330 (whole-surah NULL) — retained for cross-scale comparison
H_NEW_1330_SURAHS = [7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96]


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set(ROOT)} from QAC v0.4. Same code path as h-new-1380.py."""
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


def load_surah_lengths():
    """Returns {surah_id: n_verses} from canonical quran-text JSON."""
    data = json.load(open(QURAN_JSON))
    return {s['id']: s['total_verses'] for s in data}


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
    surah_lengths = load_surah_lengths()
    all_verses = sorted(verse_roots.keys())

    # Build the 15 sajda pericopes with ±2 window clipped to surah boundaries
    obs_root_sets = []
    obs_lengths = []
    per_pericope_summary = []
    for label, s, sv in SAJDA_VERSES:
        n = surah_lengths[s]
        v0 = max(1, sv - WINDOW)
        v1 = min(n, sv + WINDOW)
        rs = pericope_roots(verse_roots, s, v0, v1)
        L = v1 - v0 + 1
        obs_root_sets.append(rs)
        obs_lengths.append(L)
        per_pericope_summary.append({
            'label': label,
            'surah': s,
            'sajda_verse': sv,
            'window_start': v0,
            'window_end': v1,
            'n_verses': L,
            'n_unique_roots': len(rs),
            'surah_total_verses': n,
            'clipped': (v0 != sv - WINDOW) or (v1 != sv + WINDOW),
        })

    obs_J = mean_pairwise_jaccard(obs_root_sets)

    # Per-pair Jaccard table for transparency (105 pairs)
    pair_table = []
    for (i, j) in combinations(range(len(obs_root_sets)), 2):
        a, b = obs_root_sets[i], obs_root_sets[j]
        u = a | b
        Jij = (len(a & b) / len(u)) if u else 0.0
        pair_table.append({
            'i': SAJDA_VERSES[i][0],
            'j': SAJDA_VERSES[j][0],
            'inter': len(a & b),
            'union': len(u),
            'jaccard': Jij,
        })

    # Permutation null: 10000 draws of 15 length-matched random pericopes
    null_Js = []
    for _ in range(N_PERM):
        null_sets = []
        for L in obs_lengths:
            start = rng.randrange(0, len(all_verses) - L + 1)
            window = all_verses[start:start + L]
            rs = set()
            for vk in window:
                rs |= verse_roots.get(vk, set())
            null_sets.append(rs)
        null_Js.append(mean_pairwise_jaccard(null_sets))

    null_mean = sum(null_Js) / len(null_Js)
    null_std = (sum((x - null_mean) ** 2 for x in null_Js) / len(null_Js)) ** 0.5
    z = (obs_J - null_mean) / null_std if null_std > 0 else float('nan')
    n_ge = sum(1 for x in null_Js if x >= obs_J)
    p_greater = n_ge / N_PERM
    p_reportable_max = 1.0 / N_PERM if n_ge == 0 else p_greater

    direction_match = obs_J > null_mean
    pre_commit_violation = obs_J < null_mean

    if pre_commit_violation:
        verdict = 'PRE-COMMIT-VIOLATION'
    elif direction_match and p_greater < 0.05:
        verdict = 'PASS-DIRECTED'
    elif direction_match:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    # Top-5 tightest pairs for narrative reporting
    sorted_pairs = sorted(pair_table, key=lambda r: -r['jaccard'])
    top5 = sorted_pairs[:5]
    bot5 = sorted_pairs[-5:]

    out = {
        'finding_id': 'H-NEW-1510',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'aggregation_scale': 'pericope (sajda verse ± 2 verses, clipped to surah boundaries)',
        'window_halfwidth': WINDOW,
        'edge_clipping_policy': 'clip-at-surah-boundary; no cross-surah bleed',
        'pericopes': per_pericope_summary,
        'pericope_lengths': obs_lengths,
        'n_pericopes': len(obs_root_sets),
        'n_pairs': len(pair_table),
        'pairwise_jaccards': pair_table,
        'top5_tightest_pairs': top5,
        'bottom5_loosest_pairs': bot5,
        'observed_mean_pairwise_jaccard': obs_J,
        'null_mean': null_mean,
        'null_std': null_std,
        'z_score': z,
        'p_greater_perm_strict': p_greater,
        'p_reportable_upper_bound': p_reportable_max,
        'direction_locked': 'TIGHTER (J_mean > null_mean)',
        'direction_match': direction_match,
        'verdict': verdict,
        'scale_of_aggregation_pair': {
            'whole_surah_scale': {
                'finding': 'H-NEW-1330',
                'set_size': len(H_NEW_1330_SURAHS),
                'set': sorted(H_NEW_1330_SURAHS),
                'verdict': 'NULL',
                'cell_A_p': 0.571,
                'cell_B_p_length_matched': 0.110,
                'mw5_pc_p': 0.00020,
                'note': 'Whole-surah FR root-distribution cohesion of 14 sajda-token surahs',
            },
            'pericope_scale': {
                'finding': 'H-NEW-1510 (this run)',
                'set_size': len(SAJDA_VERSES),
                'set': [p[0] for p in SAJDA_VERSES],
                'verdict': verdict,
                'J_mean': obs_J,
                'null_mean': null_mean,
                'null_std': null_std,
                'z_score': z,
                'p_greater_perm': p_greater,
                'note': 'Pericope-scale root-Jaccard cohesion of 15 sajda-verse pericopes (±2 clipped)',
            },
            'scale_flip_verdict': (
                'FLIP-CONFIRMED (whole-surah NULL → pericope PASS-DIRECTED)' if verdict == 'PASS-DIRECTED'
                else 'NO-FLIP (NULL at both scales)' if verdict in ('NULL', 'DIRECTIONAL')
                else 'PRE-COMMIT-VIOLATION (sajda-pericopes are MORE DISPERSED than random)'
            ),
        },
    }
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"H-NEW-1510 — sajda 15-verse pericope-scale flip test")
    print(f"Pericope lengths: {obs_lengths}  (sum={sum(obs_lengths)} verses, {len(pair_table)} pairs)")
    print(f"Observed J_mean = {obs_J:.6f}")
    print(f"Null mean = {null_mean:.6f}  null std = {null_std:.6f}")
    print(f"z = {z:.3f}")
    print(f"p_perm (strict, one-tailed, >= obs) = {p_greater:.4f}  (count >= obs: {n_ge}/{N_PERM})")
    print(f"Direction match: {direction_match}")
    print(f"Verdict: {verdict}")
    print(f"Scale-flip verdict: {out['scale_of_aggregation_pair']['scale_flip_verdict']}")


if __name__ == '__main__':
    main()
