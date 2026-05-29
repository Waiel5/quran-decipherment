#!/usr/bin/env python3
"""Q066-F-01 — al-Taḥrīm verbatim verse-twin (Arm A) + antithetical dual-exemplar seal (Arm B).

Pre-reg: surahs/Q066-al-tahrim/Q066-F-01-tahrim-seal-prereg.md
Pre-reg SHA256: 749a186efd3959ab1e0eddfa435f916f8104454bf347a43d9466c1a1705c4d44
Rules-tuple: (no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

Arm A: Q 66:9 is a verbatim full-verse twin (deterministic corpus-rarity).
Arm B: the kafarū→āmanū adjacent exemplar-frame is corpus-exclusive to Q 66:10-11 (B-H1);
       believer-exemplars v11,v12 cohere internally vs the disbeliever exemplar v10 (B-H2);
       seal cohesion vs length-matched permutation null (B-H3, seed 20260509, 10000 perms).
"""
import json
import re
import hashlib
import sys
import os
import random
from collections import defaultdict

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs/Q066-al-tahrim/Q066-F-01-tahrim-seal-prereg.md')
EXPECTED_SHA = '749a186efd3959ab1e0eddfa435f916f8104454bf347a43d9466c1a1705c4d44'
SEED = 20260509
N_PERM = 10000
OUT_PATH = os.path.join(ROOT, 'surahs/Q066-al-tahrim/csv/Q066-F-01.json')

PAUSE = set('۪ۭۖۚۗۛۙۘ۠ۤ۫ۧۦٰۨ۬۞')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)
    print(f"SHA OK: {actual}")


def norm(t):
    return ' '.join(''.join(c for c in t if c not in PAUSE).split())


def main():
    verify_sha()
    quran = json.load(open(os.path.join(ROOT, 'quran-text/quran-no-tashkeel.json')))
    root_index = json.load(open(os.path.join(ROOT, 'data/morphology/root-index.json')))

    # --- build verse list ---
    verses = []  # (surah, verse, norm_text, n_words)
    for s in quran:
        for v in s['verses']:
            nt = norm(v['text'])
            verses.append((s['id'], v['id'], nt, len(nt.split())))

    # --- per-verse root sets from QAC ---
    verse_roots = defaultdict(set)  # (s,v) -> {roots}
    for root, atts in root_index.items():
        for a in atts:
            verse_roots[(int(a[0]), int(a[1]))].add(root)

    def jac(a, b):
        ra, rb = verse_roots[a], verse_roots[b]
        if not ra and not rb:
            return 0.0
        inter = len(ra & rb)
        union = len(ra | rb)
        return inter / union if union else 0.0

    # ============ ARM A — verbatim full-verse twins (>=10 tokens) ============
    groups = defaultdict(list)
    for s, v, nt, nw in verses:
        if nw >= 10:
            groups[nt].append((s, v))
    twin_groups = {t: locs for t, locs in groups.items() if len(locs) > 1}

    q669_text = next(nt for s, v, nt, nw in verses if s == 66 and v == 9)
    q669_partners = [loc for loc in groups[q669_text] if loc != (66, 9)]

    A_H1 = (len(q669_partners) == 1 and q669_partners[0] == (9, 73))
    A_H2 = (len(twin_groups) <= 20)
    armA_verdict = 'CONFIRMED' if (A_H1 and A_H2) else 'NULL'

    # supporting context: surface-collision baseline
    n_long = sum(1 for s, v, nt, nw in verses if nw >= 10)
    n_long_pairs = n_long * (n_long - 1) // 2
    n_verbatim_pairs = sum(len(locs) * (len(locs) - 1) // 2 for locs in twin_groups.values())
    obs_collision_rate = n_verbatim_pairs / n_long_pairs if n_long_pairs else 0.0

    # ============ ARM B — antithetical dual-exemplar seal ============
    # B-H1: count adjacent (next-verse) kafarū-exemplar -> āmanū-exemplar frame pairs corpus-wide
    kafaru_re = re.compile(r'ضرب\s+الله\s+مثلا\s+للذين\s+كفروا')
    amanu_re = re.compile(r'ضرب\s+الله\s+مثلا\s+للذين\s+آمنوا')
    by_pos = {(s, v): nt for s, v, nt, nw in verses}
    kafaru_pos = [(s, v) for s, v, nt, nw in verses if kafaru_re.search(nt)]
    amanu_pos = [(s, v) for s, v, nt, nw in verses if amanu_re.search(nt)]
    adjacent_antithetical = []
    for (s, v) in kafaru_pos:
        # immediately following verse in same surah opens with āmanū-frame?
        if (s, v + 1) in by_pos and amanu_re.search(by_pos[(s, v + 1)]):
            adjacent_antithetical.append(((s, v), (s, v + 1)))
    B_H1 = (len(adjacent_antithetical) == 1 and adjacent_antithetical[0] == ((66, 10), (66, 11)))

    # B-H2: believer-exemplars (v11,v12) cohere vs disbeliever-exemplar (v10)
    j_11_12 = jac((66, 11), (66, 12))
    j_10_11 = jac((66, 10), (66, 11))
    j_10_12 = jac((66, 10), (66, 12))
    B_H2 = (j_11_12 > j_10_11) and (j_11_12 > j_10_12)

    # frame-root bias documentation
    frame_roots = {'Drb', 'mvl'}  # ḍ-r-b, m-th-l (QAC convention) — check actual membership
    v10_frame = verse_roots[(66, 10)]
    v11_frame = verse_roots[(66, 11)]
    v12_frame = verse_roots[(66, 12)]

    # B-H3: seal believer-pair cohesion vs length-matched random-pair null
    n11 = len(verse_roots[(66, 11)])
    n12 = len(verse_roots[(66, 12)])
    # candidate pool: all corpus verses with >=1 root, excluding the seal triad
    pool = [(s, v) for (s, v) in verse_roots.keys()
            if verse_roots[(s, v)] and (s, v) not in {(66, 10), (66, 11), (66, 12)}]
    pool_a = [p for p in pool if abs(len(verse_roots[p]) - n11) <= 3]
    pool_b = [p for p in pool if abs(len(verse_roots[p]) - n12) <= 3]

    rng = random.Random(SEED)
    null_js = []
    for _ in range(N_PERM):
        a = rng.choice(pool_a)
        b = rng.choice(pool_b)
        while b == a:
            b = rng.choice(pool_b)
        null_js.append(jac(a, b))
    n_ge = sum(1 for x in null_js if x >= j_11_12)
    p_perm = (n_ge + 1) / (N_PERM + 1)
    null_mean = sum(null_js) / len(null_js)
    null_var = sum((x - null_mean) ** 2 for x in null_js) / len(null_js)
    null_std = null_var ** 0.5
    z = (j_11_12 - null_mean) / null_std if null_std else float('nan')
    alpha = 0.05
    B_H3 = (j_11_12 > null_mean) and (p_perm < alpha)

    # --- Arm B verdict ---
    b_passes = sum([B_H1, B_H2, B_H3])
    direction_violation = (j_11_12 < j_10_11) or (j_11_12 < j_10_12) or (j_11_12 < null_mean)
    if direction_violation:
        armB_verdict = 'NULL (pre-commit violation)'
    elif b_passes == 3:
        armB_verdict = 'CONFIRMED'
    elif b_passes == 2:
        armB_verdict = 'DIRECTIONAL'
    else:
        armB_verdict = 'NULL'

    out = {
        'test_id': 'Q066-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, QAC v0.4 roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'arm_A': {
            'q66_9_text': q669_text,
            'q66_9_verbatim_partners': q669_partners,
            'A_H1_partner_is_Q9_73': A_H1,
            'n_verbatim_twin_groups_ge10tok': len(twin_groups),
            'A_H2_count_le_20': A_H2,
            'twin_group_locations': sorted([sorted(locs) for locs in twin_groups.values()]),
            'n_long_verses_ge10tok': n_long,
            'n_long_verse_pairs': n_long_pairs,
            'n_verbatim_pairs': n_verbatim_pairs,
            'observed_verbatim_collision_rate': obs_collision_rate,
            'verdict': armA_verdict,
        },
        'arm_B': {
            'kafaru_frame_positions': kafaru_pos,
            'amanu_frame_positions': amanu_pos,
            'adjacent_antithetical_pairs': adjacent_antithetical,
            'B_H1_corpus_exclusive_to_Q66': B_H1,
            'j_11_12': j_11_12,
            'j_10_11': j_10_11,
            'j_10_12': j_10_12,
            'B_H2_believer_pair_tighter': B_H2,
            'frame_root_bias_note': {
                'v10_n_roots': len(v10_frame),
                'v11_n_roots': len(v11_frame),
                'v12_n_roots': len(v12_frame),
                'shared_v10_v11': sorted(v10_frame & v11_frame),
                'shared_v11_v12': sorted(v11_frame & v12_frame),
            },
            'B_H3_perm': {
                'j_11_12': j_11_12,
                'null_mean': null_mean,
                'null_std': null_std,
                'z': z,
                'p_perm': p_perm,
                'n_ge': n_ge,
                'alpha': alpha,
                'pool_a_size': len(pool_a),
                'pool_b_size': len(pool_b),
                'pass': B_H3,
            },
            'B_passes': b_passes,
            'direction_violation': direction_violation,
            'verdict': armB_verdict,
        },
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("\n===== Q066-F-01 RESULTS =====")
    print(f"ARM A: Q66:9 partners={q669_partners} | A-H1={A_H1} | groups={len(twin_groups)} A-H2={A_H2} -> {armA_verdict}")
    print(f"ARM B: B-H1 adj-antithetical pairs={adjacent_antithetical} -> {B_H1}")
    print(f"       J(11,12)={j_11_12:.4f}  J(10,11)={j_10_11:.4f}  J(10,12)={j_10_12:.4f} | B-H2={B_H2}")
    print(f"       B-H3 null_mean={null_mean:.4f} z={z:.3f} p_perm={p_perm:.5f} | B-H3={B_H3}")
    print(f"       ARM B -> {armB_verdict}  (passes {b_passes}/3)")
    print(f"\nWrote {OUT_PATH}")


if __name__ == '__main__':
    main()
