#!/usr/bin/env python3
"""Q041-F-04 — 6-day creation pericope cluster cohesion on root-Jaccard.

Pre-reg: surahs/Q041-fussilat/preregs/Q041-F-04-creation-7days-pericope-prereg.md
Pre-reg SHA256: ea3a180a6f9ba2259f2c6cfee8587f06672d707cddc9785a936693cae9078604
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, pericope-bag union, Jaccard similarity, length-matched permutation null, Hafs-Kufan, Mashriqi)
"""
import json
import re
import hashlib
import sys
import os
import random
from itertools import combinations

PREREG = '/Users/grey/Downloads/quran/surahs/Q041-fussilat/preregs/Q041-F-04-creation-7days-pericope-prereg.md'
EXPECTED_SHA = 'ea3a180a6f9ba2259f2c6cfee8587f06672d707cddc9785a936693cae9078604'
SEED = 20260509
N_PERM = 10000
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q041-fussilat/csv/Q041-F-04.json'
QAC_PATH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'

# Pericopes: list of (label, list of (surah, verse) keys)
PERICOPES = [
    ('Q7:54', [(7, 54)]),
    ('Q10:3', [(10, 3)]),
    ('Q11:7', [(11, 7)]),
    ('Q25:59', [(25, 59)]),
    ('Q32:4', [(32, 4)]),
    ('Q41:9-12', [(41, 9), (41, 10), (41, 11), (41, 12)]),
    ('Q50:38', [(50, 38)]),
    ('Q57:4', [(57, 4)]),
]


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def parse_qac():
    """Parse QAC v0.4 morphology file into a (s,v) -> {root_set} mapping."""
    verse_roots = {}
    root_pat = re.compile(r'ROOT:([^|]+)')
    key_pat = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)')
    with open(QAC_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            m = key_pat.match(line)
            if not m:
                continue
            s, v, w, seg = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
            rm = root_pat.search(line)
            if rm:
                root = rm.group(1).strip()
                verse_roots.setdefault((s, v), set()).add(root)
    return verse_roots


def pericope_bag(verse_keys, verse_roots):
    bag = set()
    for k in verse_keys:
        if k in verse_roots:
            bag.update(verse_roots[k])
    return bag


def jaccard(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


def mean_pairwise_jaccard(bags):
    pairs = list(combinations(range(len(bags)), 2))
    if not pairs:
        return 0.0
    return sum(jaccard(bags[i], bags[j]) for i, j in pairs) / len(pairs)


def all_valid_anchors(quran, span_len):
    """Get all (surah, verse_start_idx) where a contiguous span of span_len verses fits."""
    anchors = []
    for s in quran:
        nv = len(s['verses'])
        for i in range(nv - span_len + 1):
            anchors.append((s['id'], s['verses'][i]['id']))
    return anchors


def main():
    verify_sha()
    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    verse_roots = parse_qac()

    # Observed pericope bags + mean pairwise Jaccard
    bags = []
    bag_info = []
    for label, keys in PERICOPES:
        bag = pericope_bag(keys, verse_roots)
        bags.append(bag)
        bag_info.append({
            'label': label,
            'verses': [list(k) for k in keys],
            'n_unique_roots': len(bag),
            'sample_roots': sorted(bag)[:15],
        })

    observed_mean = mean_pairwise_jaccard(bags)

    # 28-pair Jaccard matrix
    pair_jaccards = []
    for i, j in combinations(range(len(bags)), 2):
        pair_jaccards.append({
            'pair': [PERICOPES[i][0], PERICOPES[j][0]],
            'jaccard': jaccard(bags[i], bags[j]),
            'intersection_size': len(bags[i] & bags[j]),
            'union_size': len(bags[i] | bags[j]),
        })

    # Permutation null: sample length-matched random spans
    pericope_lengths = [len(keys) for _, keys in PERICOPES]
    # For each pericope-length, get all valid anchors
    anchors_by_len = {L: all_valid_anchors(quran, L) for L in set(pericope_lengths)}

    # Build a (surah, verse) -> root mapping function for spans
    # For each anchor (sid, start_v) and length L, span = [(sid, start_v + i) for i in range(L)]
    # But verses are sequential; need to use surah verse indices
    surah_verses_by_id = {s['id']: [v['id'] for v in s['verses']] for s in quran}

    def span_bag(sid, start_v, L):
        vs = surah_verses_by_id[sid]
        try:
            idx = vs.index(start_v)
        except ValueError:
            return set()
        span_keys = [(sid, vs[idx + i]) for i in range(L) if idx + i < len(vs)]
        bag = set()
        for k in span_keys:
            if k in verse_roots:
                bag.update(verse_roots[k])
        return bag

    random.seed(SEED)
    null_means = []
    n_ge_observed = 0
    for _ in range(N_PERM):
        sampled_bags = []
        for L in pericope_lengths:
            sid, start_v = random.choice(anchors_by_len[L])
            sampled_bags.append(span_bag(sid, start_v, L))
        m = mean_pairwise_jaccard(sampled_bags)
        null_means.append(m)
        if m >= observed_mean:
            n_ge_observed += 1

    p_value = (n_ge_observed + 1) / (N_PERM + 1)

    # Direction lock check
    null_mean = sum(null_means) / len(null_means)
    direction_match = (observed_mean > null_mean)

    # Verdict
    if p_value <= 0.05 and direction_match:
        verdict = 'VINDICATED'
    elif p_value <= 0.10 and direction_match:
        verdict = 'DIRECTIONAL'
    elif not direction_match:
        verdict = 'NULL-PRE-COMMIT-VIOLATION'
    else:
        verdict = 'NULL'

    # Distribution summary
    null_sorted = sorted(null_means)
    null_pct = {
        'min': null_sorted[0],
        'p5': null_sorted[int(0.05 * len(null_sorted))],
        'p25': null_sorted[int(0.25 * len(null_sorted))],
        'p50': null_sorted[int(0.50 * len(null_sorted))],
        'p75': null_sorted[int(0.75 * len(null_sorted))],
        'p95': null_sorted[int(0.95 * len(null_sorted))],
        'p99': null_sorted[int(0.99 * len(null_sorted))],
        'max': null_sorted[-1],
        'mean': null_mean,
    }

    out = {
        'finding_id': 'Q041-F-04',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, pericope-bag union, Jaccard similarity, length-matched permutation null, Hafs-Kufan, Mashriqi)',
        'pericopes': bag_info,
        'observed_mean_pairwise_jaccard': observed_mean,
        'pair_jaccard_matrix': pair_jaccards,
        'null_distribution_summary': null_pct,
        'n_perms_ge_observed': n_ge_observed,
        'p_value': p_value,
        'direction_pre_committed': 'observed > null mean',
        'direction_match': direction_match,
        'observed_minus_null_mean': observed_mean - null_mean,
        'verdict': verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q041-F-04 verdict: {verdict}")
    print(f"  Observed mean pairwise Jaccard: {observed_mean:.4f}")
    print(f"  Null mean: {null_mean:.4f}")
    print(f"  Δ (observed - null): {observed_mean - null_mean:+.4f}")
    print(f"  p-value: {p_value:.6f} (n_ge_observed = {n_ge_observed}/{N_PERM})")
    print(f"  Direction match: {direction_match}")
    for p in pair_jaccards:
        print(f"    {p['pair'][0]} ↔ {p['pair'][1]}: J = {p['jaccard']:.4f}  (|∩|={p['intersection_size']}, |∪|={p['union_size']})")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
