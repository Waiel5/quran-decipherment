#!/usr/bin/env python3
"""Q094-F-01 — al-Sharḥ al-ʿusr/al-yusr reprise (94:5-6) as the corpus's tightest near-verbatim adjacent couplet.

Pre-reg: surahs/Q094-al-sharh/Q094-F-01-usr-yusr-reprise-prereg.md
Pre-reg SHA256: 2dd938018b303e0da9e8a1313d3fe710fe83123913e6aaa705c1975908f71d2a
Rules-tuple: (no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

Arm A: Q 94:5-6 is the UNIQUE adjacent same-surah pair differing by only a single leading ف/و (deterministic).
Arm B: Q 94:5-6 is the GLOBAL minimum-edit-distance adjacent couplet (edit=1, rank 1); 0 exact-verbatim
       adjacencies; tighter than a length-matched permutation null (B-H3, seed 20260509, 10000 perms).
Arm C: definite-al-ʿusr / indefinite-yusran orthographic asymmetry + v5/v6 root-Jaccard = 1.0 (deterministic).
"""
import json
import hashlib
import sys
import os
import random
from collections import defaultdict

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs/Q094-al-sharh/Q094-F-01-usr-yusr-reprise-prereg.md')
EXPECTED_SHA = '2dd938018b303e0da9e8a1313d3fe710fe83123913e6aaa705c1975908f71d2a'
SEED = 20260509
SEED2 = 20260530
N_PERM = 10000
OUT_PATH = os.path.join(ROOT, 'surahs/Q094-al-sharh/csv/Q094-F-01.json')

PAUSE = set('۪ۭۖۚۗۛۙۘ۠ۤ۫ۧۦٰۨ۬۞')
FA = 'ف'
WAW = 'و'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)
    print(f"SHA OK: {actual}")


def norm(t):
    return ' '.join(''.join(c for c in t if c not in PAUSE).split())


def lev(a, b):
    m, n = len(a), len(b)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        cur = [i] + [0] * n
        ai = a[i - 1]
        for j in range(1, n + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ai != b[j - 1]))
        prev = cur
    return prev[n]


def main():
    verify_sha()
    quran = json.load(open(os.path.join(ROOT, 'quran-text/quran-no-tashkeel.json')))
    root_index = json.load(open(os.path.join(ROOT, 'data/morphology/root-index.json')))

    # --- build verse list in canonical order ---
    V = []  # (surah, verse, norm_text)
    for s in quran:
        for v in s['verses']:
            V.append((s['id'], v['id'], norm(v['text'])))

    # per-verse root sets
    verse_roots = defaultdict(set)
    for r, atts in root_index.items():
        for a in atts:
            verse_roots[(int(a[0]), int(a[1]))].add(r)

    # ============ ARM A — single-connective near-verbatim adjacency ============
    # A-H1: token-level. adjacent same-surah pair, equal token count, exactly one differing token,
    #       that token being the other token with a single leading ف/و prepended (or removed).
    a_h1_hits = []
    for i in range(len(V) - 1):
        s, a, ta = V[i]
        s2, b, tb = V[i + 1]
        if s != s2:
            continue
        wa, wb = ta.split(), tb.split()
        if len(wa) != len(wb) or len(wa) < 2:
            continue
        diffs = [k for k in range(len(wa)) if wa[k] != wb[k]]
        if len(diffs) != 1:
            continue
        k = diffs[0]
        x, y = wa[k], wb[k]
        if (x == FA + y or y == FA + x or x == WAW + y or y == WAW + x):
            a_h1_hits.append([s, a, b, x, y])
    A_H1 = (len(a_h1_hits) == 1 and a_h1_hits[0][0] == 94 and a_h1_hits[0][1] == 5 and a_h1_hits[0][2] == 6)

    # A-H2: whole-string. B == A with a single leading ف/و char removed (or vice versa).
    a_h2_hits = []
    for i in range(len(V) - 1):
        s, a, ta = V[i]
        s2, b, tb = V[i + 1]
        if s != s2 or len(ta) < 6:
            continue
        if (ta == FA + tb or tb == FA + ta or ta == WAW + tb or tb == WAW + ta):
            a_h2_hits.append([s, a, b])
    A_H2 = (len(a_h2_hits) == 1 and a_h2_hits[0] == [94, 5, 6])
    armA_verdict = 'CONFIRMED' if (A_H1 and A_H2) else 'NULL'

    # ============ ARM B — global minimum edit-distance adjacent couplet ============
    SUB = 3  # substantive: >=3 word-tokens each
    pairs = []  # (edit, s, a, b, la, lb)
    exact_adjacent = 0
    for i in range(len(V) - 1):
        s, a, ta = V[i]
        s2, b, tb = V[i + 1]
        if s != s2:
            continue
        ca, cb = ta.replace(' ', ''), tb.replace(' ', '')
        if ta == tb and len(ta.split()) >= 2:
            exact_adjacent += 1
        if len(ta.split()) < SUB or len(tb.split()) < SUB:
            continue
        d = lev(ca, cb)
        pairs.append((d, s, a, b, len(ca), len(cb)))
    pairs.sort(key=lambda p: p[0])
    min_edit = pairs[0][0]
    rank1 = [p for p in pairs if p[0] == min_edit]
    B_H1 = (min_edit == 1 and len(rank1) == 1 and rank1[0][1] == 94 and rank1[0][2] == 5 and rank1[0][3] == 6)
    B_H2 = (exact_adjacent == 0)

    # B-H3: permutation null. v5 = (94,5), v6 = (94,6).
    t5 = next(t for s, v, t in V if s == 94 and v == 5).replace(' ', '')
    t6 = next(t for s, v, t in V if s == 94 and v == 6).replace(' ', '')
    obs_edit = lev(t5, t6)
    L5, L6 = len(t5), len(t6)
    all_strings = [t.replace(' ', '') for s, v, t in V]
    pool_a = [x for x in all_strings if abs(len(x) - L5) <= 3]
    pool_b = [x for x in all_strings if abs(len(x) - L6) <= 3]

    def run_null(seed):
        rng = random.Random(seed)
        n_le = 0
        edits = []
        for _ in range(N_PERM):
            x = rng.choice(pool_a)
            y = rng.choice(pool_b)
            while y == x:
                y = rng.choice(pool_b)
            d = lev(x, y)
            edits.append(d)
            if d <= obs_edit:
                n_le += 1
        p = (n_le + 1) / (N_PERM + 1)
        mean = sum(edits) / len(edits)
        return n_le, p, mean

    n_le, p_perm, null_mean = run_null(SEED)
    n_le2, p_perm2, null_mean2 = run_null(SEED2)
    alpha = 0.05
    # direction lock: observed TIGHTER (obs_edit < null_mean) AND p < alpha
    B_H3 = (obs_edit < null_mean) and (p_perm < alpha)
    direction_violation_B = (not B_H1) or (obs_edit >= null_mean)

    b_passes = sum([B_H1, B_H2, B_H3])
    if direction_violation_B and not B_H1:
        armB_verdict = 'NULL (pre-commit violation)'
    elif b_passes == 3:
        armB_verdict = 'CONFIRMED'
    elif b_passes == 2:
        armB_verdict = 'DIRECTIONAL'
    else:
        armB_verdict = 'NULL'

    # ============ ARM C — definite/indefinite asymmetry ============
    w5 = next(t for s, v, t in V if s == 94 and v == 5).split()
    w6 = next(t for s, v, t in V if s == 94 and v == 6).split()
    usr_def_v5 = 'العسر' in w5
    usr_def_v6 = 'العسر' in w6
    yusr_indef_v5 = 'يسرا' in w5
    yusr_indef_v6 = 'يسرا' in w6
    r5 = verse_roots[(94, 5)]
    r6 = verse_roots[(94, 6)]
    jac_56 = len(r5 & r6) / len(r5 | r6) if (r5 | r6) else 0.0
    C_H1 = (usr_def_v5 and usr_def_v6 and yusr_indef_v5 and yusr_indef_v6 and jac_56 == 1.0)
    armC_verdict = 'CONFIRMED' if C_H1 else 'NULL'

    out = {
        'test_id': 'Q094-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'seed_replication': SEED2,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, QAC v0.4 roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'arm_A': {
            'A_H1_token_single_connective_hits': a_h1_hits,
            'A_H1_unique_Q94_5_6': A_H1,
            'A_H2_wholestring_hits': a_h2_hits,
            'A_H2_unique_Q94_5_6': A_H2,
            'verdict': armA_verdict,
        },
        'arm_B': {
            'n_substantive_adjacent_pairs': len(pairs),
            'min_edit_distance': min_edit,
            'rank1_pairs': [[p[1], p[2], p[3]] for p in rank1],
            'B_H1_Q94_5_6_unique_rank1_edit1': B_H1,
            'exact_verbatim_adjacent_count': exact_adjacent,
            'B_H2_zero_exact_adjacent': B_H2,
            'top12_smallest_edit': [{'edit': p[0], 'pair': f"Q{p[1]}:{p[2]}-{p[3]}", 'len': [p[4], p[5]]} for p in pairs[:12]],
            'B_H3_perm': {
                'obs_edit': obs_edit,
                'null_mean_edit_seed1': null_mean,
                'n_le_seed1': n_le,
                'p_perm_seed1': p_perm,
                'null_mean_edit_seed2': null_mean2,
                'n_le_seed2': n_le2,
                'p_perm_seed2': p_perm2,
                'alpha': alpha,
                'pool_a_size': len(pool_a),
                'pool_b_size': len(pool_b),
                'pass': B_H3,
            },
            'B_passes': b_passes,
            'verdict': armB_verdict,
        },
        'arm_C': {
            'usr_definite_v5': usr_def_v5,
            'usr_definite_v6': usr_def_v6,
            'yusr_indefinite_v5': yusr_indef_v5,
            'yusr_indefinite_v6': yusr_indef_v6,
            'v5_roots': sorted(r5),
            'v6_roots': sorted(r6),
            'root_jaccard_v5_v6': jac_56,
            'C_H1_orthographic_asymmetry': C_H1,
            'verdict': armC_verdict,
        },
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("\n===== Q094-F-01 RESULTS =====")
    print(f"ARM A: single-connective hits={a_h1_hits} | A-H1={A_H1} | whole-string={a_h2_hits} A-H2={A_H2} -> {armA_verdict}")
    print(f"ARM B: min_edit={min_edit} rank1={[(p[1],p[2],p[3]) for p in rank1]} B-H1={B_H1}")
    print(f"       exact-verbatim-adjacent={exact_adjacent} B-H2={B_H2}")
    print(f"       B-H3 obs_edit={obs_edit} null_mean={null_mean:.3f} n_le={n_le} p_perm={p_perm:.5f} (seed2 p={p_perm2:.5f}) B-H3={B_H3}")
    print(f"       ARM B -> {armB_verdict} (passes {b_passes}/3)")
    print(f"ARM C: usr-def(v5,v6)=({usr_def_v5},{usr_def_v6}) yusr-indef(v5,v6)=({yusr_indef_v5},{yusr_indef_v6}) jac56={jac_56} -> {armC_verdict}")
    print(f"\nWrote {OUT_PATH}")


if __name__ == '__main__':
    main()
