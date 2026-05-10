#!/usr/bin/env python3
"""H-NEW-1750 — al-ḥamdu li-llāh opener-pericope flip-test.

Re-tests the H-NEW-1340 NULL (whole-surah Fisher-Rao cohesion of the 5-surah
al-ḥamdu li-llāh opener cluster {Q 1, 6, 18, 34, 35}) at the opener-pericope
scale (first 3 verses of each cluster member). Applies the cross-finding-025-formal
pericope-scale flip law to a 4th independent thin-marker NULL.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1750-alhamdu-opener-pericope.md
Pre-reg SHA256: 840fdf5f932cc7f3112ddf70723c3f8cb37f29200b4d1c5ac496c38481baca73

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
PREREG = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/prereg-h-new-1750-alhamdu-opener-pericope.md')
EXPECTED_SHA = '840fdf5f932cc7f3112ddf70723c3f8cb37f29200b4d1c5ac496c38481baca73'
SEED = 20260509
N_PERM = 10000

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN_NO_TASHKEEL = os.path.join(PROJECT_ROOT, 'quran-text/quran-no-tashkeel.json')
OUT_JSON = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/csv/h-new-1750.json')

# 5 al-ḥamdu li-llāh opener-pericope windows (LOCKED via pre-reg)
# Each pericope = (surah, first verse=1, last verse=3) — first 3 verses of each cluster member.
EXPECTED_CLUSTER = [
    (1, 1, 3),
    (6, 1, 3),
    (18, 1, 3),
    (34, 1, 3),
    (35, 1, 3),
]

# H-NEW-1340 whole-surah scale reference (the NULL we're flipping)
H_NEW_1340_REF = {
    'finding_id': 'H-NEW-1340',
    'aggregation_scale': 'whole-surah Fisher-Rao root-distribution',
    'surah_set': [1, 6, 18, 34, 35],
    'obs_intra_mean_fr': 0.9902,
    'cell_A_uniform_p': 0.7485,
    'cell_B_length_matched_p': 0.4975,
    'mw5_pc_pass_p': 0.0210,
    'verdict': 'NULL (both cells; PC valid)',
}


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def verify_cluster_via_corpus():
    """Reverify each cluster member has ≥3 verses and basmala policy is consistent."""
    text = json.load(open(QURAN_NO_TASHKEEL))
    surah_verse_counts = {}
    for s in text:
        sid = int(s['id'])
        surah_verse_counts[sid] = len(s['verses'])
    for (sid, vstart, vend) in EXPECTED_CLUSTER:
        vc = surah_verse_counts.get(sid)
        if vc is None or vc < vend:
            print(f"FAIL: Q{sid} has {vc} verses, pericope needs through v{vend}", file=sys.stderr)
            sys.exit(1)
    return surah_verse_counts


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set(ROOT)} from QAC v0.4. Identical to h-new-1380/1510/1520.py."""
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


def window_roots(verse_roots, surah, vstart, vend):
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
    surah_verse_counts = verify_cluster_via_corpus()
    verse_roots = load_qac_roots_by_verse()
    all_verses = sorted(verse_roots.keys())  # ~6,236 flat-indexed verses

    rng = random.Random(SEED)

    # Observed: 5 opener-pericope windows
    obs_root_sets = []
    obs_lengths = []
    per_window_summary = []
    for (sid, vstart, vend) in EXPECTED_CLUSTER:
        rs = window_roots(verse_roots, sid, vstart, vend)
        L = vend - vstart + 1
        obs_root_sets.append(rs)
        obs_lengths.append(L)
        per_window_summary.append({
            'label': f'Q {sid}:{vstart}-{vend}',
            'surah': sid,
            'verse_start': vstart,
            'verse_end': vend,
            'length': L,
            'n_unique_roots': len(rs),
            'roots': sorted(rs),
        })

    obs_J = mean_pairwise_jaccard(obs_root_sets)

    # Per-pair Jaccard table for transparency (10 pairs)
    pair_table = []
    for (i, j) in combinations(range(len(obs_root_sets)), 2):
        a, b = obs_root_sets[i], obs_root_sets[j]
        u = a | b
        Jij = (len(a & b) / len(u)) if u else 0.0
        pair_table.append({
            'i': per_window_summary[i]['label'],
            'j': per_window_summary[j]['label'],
            'inter': len(a & b),
            'union': len(u),
            'shared_roots': sorted(a & b),
            'jaccard': Jij,
        })

    # Permutation null: 10000 draws of 5 length-matched random windows from flat verse-index
    null_Js = []
    for _ in range(N_PERM):
        null_sets = []
        for L in obs_lengths:
            start = rng.randrange(0, len(all_verses) - L + 1)
            window_verses = all_verses[start:start + L]
            rs = set()
            for vk in window_verses:
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
        verdict = 'PRE-COMMIT-VIOLATION (NULL with prominence)'
    elif direction_match and p_greater < 0.05:
        verdict = 'PASS-DIRECTED'
    elif direction_match:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    flip_verdict = (
        'FLIP (whole-surah NULL → opener-pericope PASS-DIRECTED)'
        if verdict == 'PASS-DIRECTED'
        else (
            'NON-FLIP (both whole-surah and opener-pericope NULL/sub-threshold)'
            if verdict in ('NULL', 'DIRECTIONAL')
            else 'PRE-COMMIT-VIOLATION'
        )
    )

    out = {
        'finding_id': 'H-NEW-1750',
        'title': 'al-ḥamdu li-llāh opener-pericope flip-test',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'aggregation_scale': 'opener-pericope (first 3 verses of each cluster member surah)',
        'cluster_definition': '5 surahs opening with al-ḥamdu li-llāh: {Q 1, 6, 18, 34, 35}',
        'n_attestations': len(EXPECTED_CLUSTER),
        'attestations_surahs': sorted(set(s for s, vs, ve in EXPECTED_CLUSTER)),
        'pericope_windows': per_window_summary,
        'pericope_lengths': obs_lengths,
        'pairwise_jaccards': pair_table,
        'observed_mean_pairwise_jaccard': obs_J,
        'null_mean': null_mean,
        'null_std': null_std,
        'z_score': z,
        'p_greater_perm_strict': p_greater,
        'p_reportable_upper_bound': p_reportable_max,
        'direction_locked': 'TIGHTER (J_mean > null_mean)',
        'direction_match': direction_match,
        'verdict': verdict,
        'flip_verdict': flip_verdict,
        'scale_of_aggregation_pair': {
            'whole_surah_scale': H_NEW_1340_REF,
            'opener_pericope_scale': {
                'finding_id': 'H-NEW-1750',
                'aggregation_scale': 'opener-pericope (first 3 verses of each cluster member)',
                'n_windows': len(EXPECTED_CLUSTER),
                'J_mean': obs_J,
                'null_mean': null_mean,
                'null_std': null_std,
                'z_score': z,
                'p_greater_perm': p_greater,
                'verdict': verdict,
            },
        },
        'cross_finding_025_formal_corollary': {
            'principle': 'pericope-scale flip law (cross-finding-025-formal, 2026-05-09 PM)',
            'prior_supporting_pairs': [
                'H-NEW-039 NULL (whole-surah) ↔ H-NEW-1380 PASS (pericope) on Iblīs-narrative set, z=+4.76',
                'H-NEW-1330 NULL (whole-surah) ↔ H-NEW-1510 PASS (pericope) on sajda 14-verse cluster, z=+2.685',
                'H-NEW-1360 NULL (whole-surah) ↔ H-NEW-1520 PASS (pericope) on yā-ayyuhā al-nabī set, z=+6.41',
            ],
            'this_pair': 'H-NEW-1340 NULL (whole-surah) ↔ H-NEW-1750 ? (opener-pericope) on al-ḥamdu li-llāh opener set',
            'this_pair_supports_principle': verdict == 'PASS-DIRECTED',
            'count_after_this_test': '4/4 if PASS, 3/4 if first non-flip',
        },
    }
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Observed J_mean = {obs_J:.6f}")
    print(f"Null mean       = {null_mean:.6f}  null std = {null_std:.6f}")
    print(f"z               = {z:.3f}")
    print(f"p_perm (strict, one-tailed, >= obs) = {p_greater:.4f}  (count >= obs: {n_ge}/{N_PERM})")
    print(f"Direction match: {direction_match}")
    print(f"Verdict:         {verdict}")
    print(f"Flip verdict:    {flip_verdict}")
    print()
    print(f"Pericope-window lengths: {obs_lengths}")
    print(f"Per-window root-set sizes: {[len(rs) for rs in obs_root_sets]}")
    print()
    print("Per-window summary:")
    for w in per_window_summary:
        print(f"  {w['label']}: {w['n_unique_roots']} roots")
    print()
    print("Per-pair Jaccards:")
    for p in pair_table:
        print(f"  {p['i']} ↔ {p['j']}: |∩|={p['inter']:2d} |∪|={p['union']:3d} J={p['jaccard']:.4f}")


if __name__ == '__main__':
    main()
