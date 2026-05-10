#!/usr/bin/env python3
"""H-NEW-1760 — Ḥawāmīm 7-surah opener-pericope (first 3 verses) root-Jaccard
cohesion flip-test (H-NEW-1395 NULL → ?).

Re-tests the H-NEW-1395 NULL (whole-surah Fisher-Rao cohesion of the 7-surah
ḥawāmīm cluster {Q 40-46}) at the opener-pericope scale (each surah's first 3
verses). The HM marker is concentrated at the opener; the next 2 verses are
the surah's thematic preamble (per al-Suyūṭī al-Itqān nawʿ 8 on tarjamat
al-sūra). Applies the cross-finding-025-formal scale-of-aggregation pericope-
flip law (3/3 prior flips confirmed) to a 4th, structurally different marker
class (orthographic-opener).

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1760-hawamim-opener-pericope.md
Pre-reg SHA256: 160adb78a338a95248e4f2ab29f67412baeaa6daa5e2351aad7ac42ccd8d0eea

Direction lock: TIGHTER (J_mean > null_mean). Seed 20260509, n_perm=10000.
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi).
"""
import json
import hashlib
import sys
import os
import random
from collections import defaultdict
from itertools import combinations

PROJECT_ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(
    PROJECT_ROOT,
    'findings/phase-b-hypotheses/prereg-h-new-1760-hawamim-opener-pericope.md',
)
EXPECTED_SHA = '160adb78a338a95248e4f2ab29f67412baeaa6daa5e2351aad7ac42ccd8d0eea'
SEED = 20260509
N_PERM = 10000

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN_NO_TASHKEEL = os.path.join(PROJECT_ROOT, 'quran-text/quran-no-tashkeel.json')
OUT_JSON = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/csv/h-new-1760.json')

# 7 ḥawāmīm surahs (corpus-EXACT)
HAWAMIM_SURAHS = [40, 41, 42, 43, 44, 45, 46]
HM_GLYPH = 'حم'

# Opener-pericope window = first 3 verses (v1, v2, v3) for ALL 7 surahs.
# For Q 42 this is HM + ʿSQ + 1 content verse; for the other 6 it is HM + 2
# content verses. Per pre-reg, the rule is uniformly vv 1-3 across all 7.
PERICOPE_WINDOW = (1, 3)

# H-NEW-1395 whole-surah scale reference (the NULL we're flipping)
H_NEW_1395_REF = {
    'finding_id': 'H-NEW-1395',
    'aggregation_scale': 'whole-surah Fisher-Rao root-distribution',
    'surah_set': HAWAMIM_SURAHS,
    'obs_intra_mean_fr': 0.8672,
    'cell_A_uniform_p': 0.2086,
    'cell_B_length_matched_p': 0.0514,
    'mw5_pc_p': 0.0414,
    'verdict': 'NULL (PC valid; both cells miss Bonferroni α=0.025)',
}


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(
            f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}",
            file=sys.stderr,
        )
        sys.exit(1)


def verify_hm_openers():
    """Reverify that v1 == 'حم' across all 7 ḥawāmīm surahs."""
    text = json.load(open(QURAN_NO_TASHKEEL))
    surah_verse_counts = {}
    by_id = {}
    for s in text:
        sid = int(s['id'])
        surah_verse_counts[sid] = len(s['verses'])
        by_id[sid] = s
    failures = []
    for sid in HAWAMIM_SURAHS:
        if sid not in by_id:
            failures.append(f'Q {sid}: surah not found in corpus')
            continue
        v1 = by_id[sid]['verses'][0]
        v1_text = v1.get('text', '').strip()
        if v1_text != HM_GLYPH:
            failures.append(f'Q {sid}: v1 == {v1_text!r}, expected {HM_GLYPH!r}')
    if failures:
        print('FAIL: HM-opener reverification failed:', file=sys.stderr)
        for f in failures:
            print(f'  {f}', file=sys.stderr)
        sys.exit(1)
    return surah_verse_counts, by_id


def build_opener_pericopes(surah_verse_counts):
    """Build the 7 opener-pericopes (uniform vv 1-3 across all 7 surahs)."""
    v_start, v_end = PERICOPE_WINDOW
    L = v_end - v_start + 1
    windows = []
    for sid in HAWAMIM_SURAHS:
        max_verse = surah_verse_counts[sid]
        if max_verse < v_end:
            print(
                f'FAIL: Q {sid} has only {max_verse} verses; cannot take vv {v_start}-{v_end}',
                file=sys.stderr,
            )
            sys.exit(1)
        windows.append({
            'label': f'Q {sid}:{v_start}-{v_end}',
            'surah': sid,
            'verse_start': v_start,
            'verse_end': v_end,
            'length': L,
        })
    return windows


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set(ROOT)} from QAC v0.4.

    Identical to h-new-1380.py / h-new-1510.py / h-new-1520.py: takes the
    first ROOT-tagged feature per morphological segment.
    """
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
    surah_verse_counts, _ = verify_hm_openers()
    windows = build_opener_pericopes(surah_verse_counts)

    rng = random.Random(SEED)
    verse_roots = load_qac_roots_by_verse()
    all_verses = sorted(verse_roots.keys())  # 6,236 flat-indexed verses

    # Observed: 7 opener-pericopes (each vv 1-3)
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
            'roots_sample': sorted(rs)[:30],  # first 30 for transparency
        })

    obs_J = mean_pairwise_jaccard(obs_root_sets)

    # Per-pair Jaccard table for transparency (21 pairs)
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
            'shared_roots': sorted(a & b),
            'jaccard': Jij,
        })

    # Permutation null: 10000 draws of 7 length-3 random windows
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
        'finding_id': 'H-NEW-1760',
        'title': 'Ḥawāmīm 7-surah opener-pericope (first 3 verses) root-Jaccard cohesion flip-test',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'aggregation_scale': 'opener-pericope (first 3 verses; uniform vv 1-3 across all 7 ḥawāmīm)',
        'q42_treatment': 'uniformly vv 1-3 — HM + ʿSQ + 1 content verse for Q 42; HM + 2 content verses for the other 6 surahs',
        'cluster_surahs': HAWAMIM_SURAHS,
        'n_pericopes': len(windows),
        'opener_pericopes': per_window_summary,
        'pericope_lengths': obs_lengths,
        'pairwise_jaccards': pair_table,
        'observed_mean_pairwise_jaccard': obs_J,
        'null_mean': null_mean,
        'null_std': null_std,
        'z_score': z,
        'p_greater_perm_strict': p_greater,
        'p_reportable_upper_bound': p_reportable_max,
        'n_perm_ge_obs': n_ge,
        'direction_locked': 'TIGHTER (J_mean > null_mean)',
        'direction_match': direction_match,
        'verdict': verdict,
        'flip_verdict': flip_verdict,
        'scale_of_aggregation_pair': {
            'whole_surah_scale': H_NEW_1395_REF,
            'opener_pericope_scale': {
                'finding_id': 'H-NEW-1760',
                'aggregation_scale': 'opener-pericope (vv 1-3 uniform across 7 surahs)',
                'n_windows': len(windows),
                'J_mean': obs_J,
                'null_mean': null_mean,
                'null_std': null_std,
                'z_score': z,
                'p_greater_perm': p_greater,
                'verdict': verdict,
            },
        },
        'cross_finding_025_formal_corollary': {
            'principle': 'scale-of-aggregation pericope-flip law (corpus-wide, 3/3 prior flips confirmed at cross-finding-025-formal)',
            'prior_supporting_pairs': [
                'H-NEW-039 NULL ↔ H-NEW-1380 PASS (z=+4.76) — Iblīs-narrative',
                'H-NEW-1330 NULL ↔ H-NEW-1510 PASS (z=+2.685) — sajda 15-verse',
                'H-NEW-1360 NULL ↔ H-NEW-1520 PASS (z=+6.41) — yā-ayyuhā al-nabī',
            ],
            'this_pair': 'H-NEW-1395 NULL (whole-surah) ↔ H-NEW-1760 ? (opener-pericope) on ḥawāmīm 7-surah orthographic-opener cluster',
            'this_pair_supports_principle': verdict == 'PASS-DIRECTED',
            'novelty': 'first orthographic-opener marker class tested at pericope scale (3 prior pairs are narrative / liturgical / discourse classes)',
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
    print(f"Opener-pericope lengths: {obs_lengths}")
    print(f"Per-pericope root-set sizes: {[len(rs) for rs in obs_root_sets]}")


if __name__ == '__main__':
    main()
