#!/usr/bin/env python3
"""H-NEW-1500 — Christ-narrative pericope-scale flip test for H-NEW-1310 NULL.

9 Christ-narrative pericopes across Q 3, Q 4, Q 5, Q 19 — root-Jaccard cohesion
vs length-matched corpus null. Tests whether the H-NEW-1310 whole-surah NULL
flips to a PASS at pericope scale, replicating the H-NEW-1380 / Q038-F-07
methodological discovery on a different theological set.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1500-christ-pericope-replication.md
Pre-reg SHA256: 74626141b16e345be4ec5feb35b8217b92423afbe0a6432e1d885cb31e95bea7

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
PREREG = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/prereg-h-new-1500-christ-pericope-replication.md')
EXPECTED_SHA = '74626141b16e345be4ec5feb35b8217b92423afbe0a6432e1d885cb31e95bea7'
SEED = 20260509
N_PERM = 10000

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
OUT_JSON = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/csv/h-new-1500.json')

# 9 Christ-narrative pericopes (LOCKED — pre-reg "Locked pericope inventory")
PERICOPES = [
    ('Q 3:33-63',     3,  33,  63),   # Maryam-birth + ʿĪsā-birth + ḥawāriyyīn (L=31)
    ('Q 3:64-89',     3,  64,  89),   # Q 3 polemic against Christological claims (L=26)
    ('Q 4:155-172',   4, 155, 172),   # Jewish-rejection of ʿĪsā + Christological clarifications (L=18)
    ('Q 5:17',        5,  17,  17),   # Allāh ≠ al-Masīḥ ibn Maryam (L=1)
    ('Q 5:46-48',     5,  46,  48),   # Injīl-revelation passage (L=3)
    ('Q 5:72-75',     5,  72,  75),   # Trinitarian rejection (L=4)
    ('Q 5:109-120',   5, 109, 120),   # ḥawāriyyīn-table + ʿĪsā's final response (L=12)
    ('Q 19:16-40',   19,  16,  40),   # Maryam pericope + ʿĪsā cradle-speech (L=25)
    ('Q 19:88-93',   19,  88,  93),   # walad-denial pericope (L=6)
]

# H-NEW-1310 surah-set (whole-surah NULL); retained for cross-scale comparison
H_NEW_1310_SURAHS = [3, 5, 19]
# This pre-reg widens to 4 surahs by including Q 4 (the longest single Christological pericope)
H_NEW_1500_SURAHS = sorted({p[1] for p in PERICOPES})


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set(ROOT)} from QAC v0.4 — instrument-identical to H-NEW-1380."""
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
    all_verses = sorted(verse_roots.keys())

    # Observed: 9 Christ-narrative pericopes
    obs_root_sets = []
    obs_lengths = []
    per_pericope_summary = []
    for label, s, v0, v1 in PERICOPES:
        rs = pericope_roots(verse_roots, s, v0, v1)
        L = v1 - v0 + 1
        obs_root_sets.append(rs)
        obs_lengths.append(L)
        per_pericope_summary.append({
            'label': label,
            'surah': s, 'verse_start': v0, 'verse_end': v1,
            'n_verses': L,
            'n_unique_roots': len(rs),
        })

    obs_J = mean_pairwise_jaccard(obs_root_sets)

    # Per-pair Jaccard table for transparency (36 pairs)
    pair_table = []
    for (i, j) in combinations(range(len(obs_root_sets)), 2):
        a, b = obs_root_sets[i], obs_root_sets[j]
        u = a | b
        Jij = (len(a & b) / len(u)) if u else 0.0
        pair_table.append({
            'i': PERICOPES[i][0],
            'j': PERICOPES[j][0],
            'inter': len(a & b),
            'union': len(u),
            'jaccard': Jij,
        })

    # Permutation null: 10000 draws of 9 length-matched random pericopes
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
    # Strict count of perm-J >= observed
    n_ge = sum(1 for x in null_Js if x >= obs_J)
    p_greater = n_ge / N_PERM
    # 95th-percentile of null (pre-reg cross-check)
    sorted_null = sorted(null_Js)
    p95 = sorted_null[int(0.95 * N_PERM)]
    # Reportable lower bound when n_ge == 0
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
        verdict = 'NULL-AT-PERICOPE-SCALE'

    flip_verdict = (
        'NULL→PASS (Christ-narrative flips at pericope scale, matching Iblīs-narrative)'
        if verdict == 'PASS-DIRECTED'
        else 'NULL holds across scales (Christ-narrative diverges from Iblīs-narrative on scale-of-aggregation axis)'
        if verdict in ('NULL-AT-PERICOPE-SCALE', 'PRE-COMMIT-VIOLATION')
        else 'WEAK (DIRECTIONAL trend but p>=0.05)'
    )

    out = {
        'finding_id': 'H-NEW-1500',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'aggregation_scale': 'pericope (locked verse range)',
        'pericopes': per_pericope_summary,
        'pericope_lengths': obs_lengths,
        'pairwise_jaccards': pair_table,
        'observed_mean_pairwise_jaccard': obs_J,
        'null_mean': null_mean,
        'null_std': null_std,
        'null_p95': p95,
        'z_score': z,
        'p_greater_perm_strict': p_greater,
        'p_reportable_upper_bound': p_reportable_max,
        'direction_locked': 'TIGHTER (J_mean > null_mean)',
        'direction_match': direction_match,
        'verdict': verdict,
        'flip_verdict': flip_verdict,
        'scale_of_aggregation_pair': {
            'whole_surah_scale': {
                'finding': 'H-NEW-1310',
                'set': sorted(H_NEW_1310_SURAHS),
                'verdict': 'NULL (cell A uniform p=0.481; cell B length-matched p=0.187; PC sub-sample p=0.041 — MW-5 PASSED)',
                'note': 'Whole-surah FR root-distribution cohesion of 3 Christ-token surahs',
            },
            'pericope_scale': {
                'finding': 'H-NEW-1500',
                'set_surahs': H_NEW_1500_SURAHS,
                'set_pericopes': [p[0] for p in PERICOPES],
                'verdict': verdict,
                'J_mean': obs_J,
                'null_mean': null_mean,
                'z_score': z,
                'p_greater_perm': p_greater,
                'note': 'Pericope-scale root-Jaccard cohesion of 9 Christ-narrative pericopes',
            },
        },
        'cross_set_comparison_to_h_new_1380': {
            'iblis_narrative': {
                'finding': 'H-NEW-1380 (Iblīs-narrative, 7 pericopes)',
                'J_mean': 0.14561477089814906,
                'null_mean': 0.06503342766937967,
                'z': 4.76,
                'verdict': 'PASS-DIRECTED-REPLICATION',
            },
            'christ_narrative_this_finding': {
                'J_mean': obs_J,
                'null_mean': null_mean,
                'z': z,
                'verdict': verdict,
            },
            'interpretation_template': (
                'If Christ also flips (PASS-DIRECTED): scale-of-aggregation axis is supported by 2 finding-pairs; '
                'cross-finding-025 graduates from PRELIMINARY-SYNTHESIS upon a third confirming pair. '
                'If Christ does NOT flip: scale-of-aggregation axis is thematically conditional, not universal — '
                'the Iblīs-narrative is special, not a generic instance of the principle.'
            ),
        },
    }
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Observed J_mean = {obs_J:.6f}")
    print(f"Null mean = {null_mean:.6f}  null std = {null_std:.6f}")
    print(f"Null p95 = {p95:.6f}")
    print(f"z = {z:.3f}")
    print(f"p_perm (strict, one-tailed, >= obs) = {p_greater:.4f}  (count >= obs: {n_ge}/{N_PERM})")
    print(f"Direction match: {direction_match}")
    print(f"Verdict: {verdict}")
    print(f"Flip verdict: {flip_verdict}")


if __name__ == '__main__':
    main()
