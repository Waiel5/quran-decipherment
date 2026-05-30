#!/usr/bin/env python3
"""Q098-F-01 — al-Bayyina title-density falsification + khayr↔sharr al-bariyya minimal-pair muqābala.

Pre-reg: surahs/Q098-al-bayyina/Q098-F-01-bariyya-antithesis-prereg.md
Pre-reg SHA256: 57eb6828a86fccaecb0a5438ad4acb671a6f8724e16d1669fede67b2d1852b41
Rules-tuple: (no-tashkeel, orthographic-token, QAC v0.4 roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

Arm A: Q 98 al-Bayyina is NOT title-density-rank-1 in byn (raw root + exact البينة form) — direction-locked FALSIFICATION.
Arm B: البرية is a Q 98-exclusive corpus hapax-pair (exactly 2 occurrences, both Q 98).
Arm C: Q 98:6-7 is the corpus-UNIQUE adjacent faith-antithetical verse-pair with a single-substitution
       aligned tail (matched-tail >=3) pivoting on the khayr<->sharr antonym.
Arm D: content-root-Jaccard(v6,v7) vs length-matched permutation null (seed 20260509, 10000 perms).
"""
import json
import re
import hashlib
import sys
import os
import random
from collections import defaultdict, Counter

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs/Q098-al-bayyina/Q098-F-01-bariyya-antithesis-prereg.md')
EXPECTED_SHA = '57eb6828a86fccaecb0a5438ad4acb671a6f8724e16d1669fede67b2d1852b41'
SEED = 20260509
N_PERM = 10000
OUT_PATH = os.path.join(ROOT, 'surahs/Q098-al-bayyina/csv/Q098-F-01.json')

PAUSE = set('۪ۭۖۚۗۛۙۘ۠ۤ۫ۧۦٰۨ۬۞')

# Locked F1 faith-field lexicon (byte-identical to H-NEW-2290/2360)
FAITH_POS = {'Amn'}
FAITH_NEG = {'kfr', 'nfq', 'Srk'}
ANTONYM_PIVOTS = {frozenset(('خير', 'شر'))}


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)
    print(f"SHA OK: {actual}")


def norm_words(t):
    return ''.join(c for c in t if c not in PAUSE).split()


def main():
    verify_sha()
    quran = json.load(open(os.path.join(ROOT, 'quran-text/quran-no-tashkeel.json')))
    root_index = json.load(open(os.path.join(ROOT, 'data/morphology/root-index.json')))

    nverses = {s['id']: len(s['verses']) for s in quran}
    bypos = {}  # (s,v) -> [words]
    for s in quran:
        for v in s['verses']:
            bypos[(s['id'], v['id'])] = norm_words(v['text'])

    verse_roots = defaultdict(set)
    for rt, atts in root_index.items():
        for a in atts:
            verse_roots[(int(a[0]), int(a[1]))].add(rt)

    def jac(a, b):
        ra, rb = verse_roots[a], verse_roots[b]
        u = len(ra | rb)
        return len(ra & rb) / u if u else 0.0

    # ================= ARM A — title-density-EXACT falsification =================
    byn = root_index['byn']
    byn_count = Counter(int(a[0]) for a in byn)
    byn_rank_order = sorted(byn_count.items(), key=lambda x: (-x[1], x[0]))
    raw_rank = next(i for i, (s, n) in enumerate(byn_rank_order, 1) if s == 98)
    q98_byn_raw = byn_count.get(98, 0)
    A_H1 = raw_rank > 1  # NOT rank-1

    # exact eponymous surface form البينة / بينة
    bayyina_surf = Counter()
    for (s, v), ws in bypos.items():
        for w in ws:
            if w in ('البينة', 'بينة'):
                bayyina_surf[s] += 1
    surf_rank_order = sorted(bayyina_surf.items(), key=lambda x: (-x[1], x[0]))
    q98_surf = bayyina_surf.get(98, 0)
    n_ge_q98 = sum(1 for s, n in bayyina_surf.items() if s != 98 and n >= q98_surf)
    A_H2 = n_ge_q98 >= 1  # at least one other surah ties/beats Q98 -> not strict rank-1
    armA_falsified = A_H1 and A_H2
    armA_verdict = 'title-density-EXACT FALSIFIED' if armA_falsified else 'title-density-EXACT CONFIRMED'

    # normalized density context
    byn_density = {s: byn_count[s] / nverses[s] for s in byn_count}
    dens_rank = next(i for i, (s, d) in enumerate(
        sorted(byn_density.items(), key=lambda x: (-x[1], x[0])), 1) if s == 98)

    # ================= ARM B — al-bariyya corpus hapax-pair =================
    bariyya_pos = []
    for (s, v), ws in bypos.items():
        for w in ws:
            if w in ('البرية', 'برية'):
                bariyya_pos.append((s, v))
    bariyya_pos = sorted(set(bariyya_pos))
    B_H1 = len(bariyya_pos) == 2
    B_H2 = set(bariyya_pos) == {(98, 6), (98, 7)}
    armB_verdict = 'CONFIRMED' if (B_H1 and B_H2) else 'NULL'

    # ================= ARM C — minimal-pair muqābala census =================
    def single_sub_aligned_tail(a, b):
        """Return (matched_tail, n_subs, pivot_frozenset) reading from the END,
        allowing exactly one positional mismatch (the pivot)."""
        wa = bypos[a][::-1]
        wb = bypos[b][::-1]
        matched = 0
        subs = 0
        pivot = None
        for x, y in zip(wa, wb):
            if x == y:
                matched += 1
            else:
                if subs == 0:
                    subs = 1
                    pivot = frozenset((x, y))
                else:
                    break
        return matched, subs, pivot

    antithetical_pairs = []   # all adjacent faith-antithetical pairs
    minimal_antonym = []      # those meeting Arm C criteria
    for s in quran:
        vs = s['verses']
        for i in range(len(vs) - 1):
            k1 = (s['id'], vs[i]['id'])
            k2 = (s['id'], vs[i + 1]['id'])
            r1, r2 = verse_roots[k1], verse_roots[k2]
            anti = ((r1 & FAITH_POS) and (r2 & FAITH_NEG)) or ((r2 & FAITH_POS) and (r1 & FAITH_NEG))
            if not anti:
                continue
            m, subs, piv = single_sub_aligned_tail(k1, k2)
            antithetical_pairs.append((k1, k2, m, subs, list(piv) if piv else None))
            if subs == 1 and m >= 3 and piv in ANTONYM_PIVOTS:
                minimal_antonym.append((k1, k2, m, list(piv)))

    C_count = len(minimal_antonym)
    C_unique_is_q98 = (C_count == 1 and minimal_antonym[0][0] == (98, 6)
                       and minimal_antonym[0][1] == (98, 7))
    C_H1 = C_unique_is_q98
    if C_H1:
        armC_verdict = 'CONFIRMED'
    elif C_count == 0:
        armC_verdict = 'NULL'
    else:
        armC_verdict = 'NULL (pre-commit violation — a different/extra pair matched)'

    # ================= ARM D — content-disjointness vs null =================
    j_67 = jac((98, 6), (98, 7))
    n6 = len(verse_roots[(98, 6)])
    n7 = len(verse_roots[(98, 7)])
    pool = [(s, v) for (s, v) in verse_roots.keys()
            if verse_roots[(s, v)] and (s, v) not in {(98, 6), (98, 7)}]
    pool_a = [p for p in pool if abs(len(verse_roots[p]) - n6) <= 2]
    pool_b = [p for p in pool if abs(len(verse_roots[p]) - n7) <= 2]
    rng = random.Random(SEED)
    null_js = []
    for _ in range(N_PERM):
        a = rng.choice(pool_a)
        b = rng.choice(pool_b)
        while b == a:
            b = rng.choice(pool_b)
        null_js.append(jac(a, b))
    null_mean = sum(null_js) / len(null_js)
    null_var = sum((x - null_mean) ** 2 for x in null_js) / len(null_js)
    null_std = null_var ** 0.5
    z = (j_67 - null_mean) / null_std if null_std else float('nan')
    n_le = sum(1 for x in null_js if x <= j_67)
    p_lower = (n_le + 1) / (N_PERM + 1)
    alpha = 0.05
    if j_67 > null_mean:
        armD_verdict = 'NULL (pre-commit violation — content OVERLAP, replicates H-NEW-2360 jadal law)'
    elif j_67 < null_mean and p_lower < alpha:
        armD_verdict = 'CONFIRMED (disjoint muqabala)'
    else:
        armD_verdict = 'DIRECTIONAL'

    out = {
        'test_id': 'Q098-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, QAC v0.4 roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'arm_A_title_density': {
            'q98_byn_raw_count': q98_byn_raw,
            'q98_byn_raw_rank': raw_rank,
            'n_surahs_with_byn': len(byn_count),
            'byn_top5': byn_rank_order[:5],
            'A_H1_not_rank1_raw': A_H1,
            'q98_bayyina_surface_count': q98_surf,
            'bayyina_surface_top': surf_rank_order[:8],
            'n_surahs_ge_q98_surface': n_ge_q98,
            'A_H2_not_rank1_surface': A_H2,
            'byn_normalized_density_rank': dens_rank,
            'verdict': armA_verdict,
        },
        'arm_B_bariyya_hapax': {
            'bariyya_positions': bariyya_pos,
            'n_occurrences': len(bariyya_pos),
            'B_H1_count_is_2': B_H1,
            'B_H2_both_in_q98_6_7': B_H2,
            'verdict': armB_verdict,
        },
        'arm_C_minimal_muqabala': {
            'n_adjacent_faith_antithetical_pairs': len(antithetical_pairs),
            'minimal_antonym_pairs': minimal_antonym,
            'C_count': C_count,
            'C_H1_unique_q98_6_7': C_H1,
            'top_matched_tail_examples': sorted(
                [p for p in antithetical_pairs if p[3] == 1 and p[2] >= 2],
                key=lambda x: -x[2])[:8],
            'q98_6_7_record': next((p for p in antithetical_pairs if p[0] == (98, 6)), None),
            'verdict': armC_verdict,
        },
        'arm_D_disjointness': {
            'j_v6_v7': j_67,
            'v6_roots': sorted(verse_roots[(98, 6)]),
            'v7_roots': sorted(verse_roots[(98, 7)]),
            'shared_roots': sorted(verse_roots[(98, 6)] & verse_roots[(98, 7)]),
            'null_mean': null_mean,
            'null_std': null_std,
            'z': z,
            'p_lower': p_lower,
            'n_le': n_le,
            'alpha': alpha,
            'pool_a_size': len(pool_a),
            'pool_b_size': len(pool_b),
            'verdict': armD_verdict,
        },
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("\n===== Q098-F-01 RESULTS =====")
    print(f"ARM A: byn raw rank={raw_rank} (count {q98_byn_raw}); surface البينة count={q98_surf}, "
          f"#surahs>=Q98={n_ge_q98}; norm-density rank={dens_rank} -> {armA_verdict}")
    print(f"ARM B: البرية positions={bariyya_pos} (n={len(bariyya_pos)}) -> {armB_verdict}")
    print(f"ARM C: n adj faith-antithetical={len(antithetical_pairs)}; "
          f"minimal-antonym pairs={minimal_antonym} -> {armC_verdict}")
    print(f"ARM D: J(v6,v7)={j_67:.4f} null_mean={null_mean:.4f} z={z:.3f} p_lower={p_lower:.5f} "
          f"shared_roots={sorted(verse_roots[(98,6)] & verse_roots[(98,7)])} -> {armD_verdict}")
    print(f"\nWrote {OUT_PATH}")


if __name__ == '__main__':
    main()
