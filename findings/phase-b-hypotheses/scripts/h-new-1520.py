#!/usr/bin/env python3
"""H-NEW-1520 — yā-ayyuhā al-nabī prophet-vocative pericope-scale flip test.

Re-tests the H-NEW-1360 NULL (whole-surah Fisher-Rao cohesion of the 6-surah
yā-ayyuhā al-nabī set) at the pericope-window scale. The vocative is a
DISCOURSE marker whose content is the immediate next words — the directive
Allāh issues to the Prophet. Applies the H-NEW-1380 scale-of-aggregation
principle to a NEW NULL.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1520-prophet-vocative-pericope.md
Pre-reg SHA256: 7d4dce4952bb47dfba71fb173230e43032df45ed59f2a56293981920925dbb1e

Direction lock: TIGHTER (J_mean > null_mean). Seed 20260509, n_perm=10000.
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import json
import hashlib
import sys
import os
import random
import re
from collections import defaultdict
from itertools import combinations

PROJECT_ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/prereg-h-new-1520-prophet-vocative-pericope.md')
EXPECTED_SHA = '7d4dce4952bb47dfba71fb173230e43032df45ed59f2a56293981920925dbb1e'
SEED = 20260509
N_PERM = 10000

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN_NO_TASHKEEL = os.path.join(PROJECT_ROOT, 'quran-text/quran-no-tashkeel.json')
OUT_JSON = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/csv/h-new-1520.json')

# 13 yā-ayyuhā al-nabī attestations (LOCKED via pre-reg)
# These are reverified at runtime by regex over no-tashkeel corpus.
EXPECTED_ATTESTATIONS = [
    (8, 64), (8, 65), (8, 70),
    (9, 73),
    (33, 1), (33, 28), (33, 45), (33, 50), (33, 59),
    (60, 12),
    (65, 1),
    (66, 1), (66, 9),
]
VOCATIVE_REGEX = re.compile(r'يا\s*أيها\s*النبي')

# H-NEW-1360 whole-surah scale reference (the NULL we're flipping)
H_NEW_1360_REF = {
    'finding_id': 'H-NEW-1360',
    'aggregation_scale': 'whole-surah Fisher-Rao root-distribution',
    'surah_set': [8, 9, 33, 60, 65, 66],
    'obs_intra_mean_fr': 0.9532,
    'cell_A_uniform_p': 0.5734,
    'cell_B_length_matched_p': 0.5835,
    'mw5_pc_subsample': [69, 97, 101],
    'mw5_pc_p': 0.0445,
    'verdict': 'substantive NULL (PC valid)',
}


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def verify_attestations():
    """Reverify the 13 vocative attestations via regex over no-tashkeel corpus."""
    text = json.load(open(QURAN_NO_TASHKEEL))
    surah_verse_counts = {}
    found = []
    for s in text:
        sid = int(s['id'])
        surah_verse_counts[sid] = len(s['verses'])
        for v in s['verses']:
            if VOCATIVE_REGEX.search(v.get('text', '')):
                found.append((sid, int(v['id'])))
    found.sort()
    if found != EXPECTED_ATTESTATIONS:
        print(f"FAIL: attestation reverify failed.\n  expected={EXPECTED_ATTESTATIONS}\n  found   ={found}", file=sys.stderr)
        sys.exit(1)
    return surah_verse_counts


def build_pericope_windows(surah_verse_counts):
    """Build the 13 pericope-windows with edge-case truncation.

    Each window = (vocative_verse, next_verse, ...) up to 3 verses, but truncated
    if it would extend past the end of the surah (prefer in-surah completion).
    """
    windows = []
    for (sid, vstart) in EXPECTED_ATTESTATIONS:
        max_verse = surah_verse_counts[sid]
        vend = min(vstart + 2, max_verse)  # 3-verse window, in-surah only
        L = vend - vstart + 1
        windows.append({
            'label': f'Q {sid}:{vstart}-{vend}' if vend > vstart else f'Q {sid}:{vstart}',
            'surah': sid,
            'verse_start': vstart,
            'verse_end': vend,
            'length': L,
        })
    return windows


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set(ROOT)} from QAC v0.4. Identical to h-new-1380.py."""
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
    surah_verse_counts = verify_attestations()
    windows = build_pericope_windows(surah_verse_counts)

    rng = random.Random(SEED)
    verse_roots = load_qac_roots_by_verse()
    all_verses = sorted(verse_roots.keys())  # 6,236 flat-indexed verses

    # Observed: 13 pericope-windows
    obs_root_sets = []
    obs_lengths = []
    per_window_summary = []
    for w in windows:
        rs = window_roots(verse_roots, w['surah'], w['verse_start'], w['verse_end'])
        obs_root_sets.append(rs)
        obs_lengths.append(w['length'])
        per_window_summary.append({
            **w,
            'n_unique_roots': len(rs),
        })

    obs_J = mean_pairwise_jaccard(obs_root_sets)

    # Per-pair Jaccard table for transparency (78 pairs)
    pair_table = []
    for (i, j) in combinations(range(len(obs_root_sets)), 2):
        a, b = obs_root_sets[i], obs_root_sets[j]
        u = a | b
        Jij = (len(a & b) / len(u)) if u else 0.0
        pair_table.append({
            'i': windows[i]['label'],
            'j': windows[j]['label'],
            'inter': len(a & b),
            'union': len(u),
            'jaccard': Jij,
        })

    # Permutation null: 10000 draws of 13 length-matched random windows
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
        'FLIP (whole-surah NULL → pericope-window PASS-DIRECTED)'
        if verdict == 'PASS-DIRECTED'
        else (
            'NON-FLIP (both whole-surah and pericope-window NULL/sub-threshold)'
            if verdict in ('NULL', 'DIRECTIONAL')
            else 'PRE-COMMIT-VIOLATION'
        )
    )

    out = {
        'finding_id': 'H-NEW-1520',
        'title': 'yā-ayyuhā al-nabī prophet-vocative pericope-scale flip test',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'aggregation_scale': 'pericope-window (3 verses; truncated to in-surah if at end-of-surah)',
        'vocative_regex': r'يا\s*أيها\s*النبي',
        'n_attestations': len(EXPECTED_ATTESTATIONS),
        'attestations_surahs': sorted(set(s for s, v in EXPECTED_ATTESTATIONS)),
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
            'whole_surah_scale': H_NEW_1360_REF,
            'pericope_window_scale': {
                'finding_id': 'H-NEW-1520',
                'aggregation_scale': 'pericope-window (3 verses, truncated at surah-end)',
                'n_windows': len(windows),
                'J_mean': obs_J,
                'null_mean': null_mean,
                'null_std': null_std,
                'z_score': z,
                'p_greater_perm': p_greater,
                'verdict': verdict,
            },
        },
        'cross_finding_025_corollary': {
            'principle': 'scale-of-aggregation as second methodological axis (formalized by H-NEW-1380)',
            'prior_supporting_pair': 'H-NEW-039 NULL (whole-surah) ↔ H-NEW-1380 PASS (pericope) on Iblīs-narrative set',
            'this_pair': 'H-NEW-1360 NULL (whole-surah) ↔ H-NEW-1520 ? (pericope-window) on yā-ayyuhā al-nabī set',
            'codification_threshold': 'two supporting finding-pairs at cross-finding-025-formal',
            'this_pair_supports_principle': verdict == 'PASS-DIRECTED',
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


if __name__ == '__main__':
    main()
