#!/usr/bin/env python3
"""Q003-F-01 — al-sabʿ al-ṭiwāl head-block cohesion.

Pre-reg: surahs/Q003-al-imran/Q003-F-01-tiwal-block-cohesion-prereg.md
Pre-reg SHA256: 40f796b7f07db6196fd397180b449e780382ba154684033fb8ecb2329f80c4d7
Rules-tuple: (no-tashkeel, QAC v0.4 STEM-root, Fisher-Rao, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

Arm A: is block {2,3,4,5} the smoothest contiguous 4-surah block in the muṣḥaf (H-NEW-720 mean internal seam)?
Arm B: is Q3 a COHESION_ANCHOR of its {1-7} window (H-NEW-590 delta_pct < 0)?
Arm C: permutation null (seed 20260509, 10000 perms): observed block-min seam vs random-arrangement min-block.
"""
import json
import hashlib
import sys
import os
import random

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs/Q003-al-imran/Q003-F-01-tiwal-block-cohesion-prereg.md')
EXPECTED_SHA = '40f796b7f07db6196fd397180b449e780382ba154684033fb8ecb2329f80c4d7'
SEED = 20260509
N_PERM = 10000
OUT_PATH = os.path.join(ROOT, 'surahs/Q003-al-imran/csv/Q003-F-01.json')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)
    print(f"SHA OK: {actual}")


def median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def main():
    verify_sha()
    d720 = json.load(open(os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-720.json')))
    d590 = json.load(open(os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-590.json')))

    # seam[s] = delta_raw for the pair s -> s+1, s in 1..113
    seam = {r['s']: r['delta_raw'] for r in d720['per_adjacency']}
    seam_vals = [seam[s] for s in sorted(seam)]
    seam_median = median(seam_vals)

    # ---- ARM A: contiguous 4-surah block mean internal seam ----
    # block starting at surah s covers seams s, s+1, s+2 (three internal joints)
    def block_mean(s, seam_map):
        return (seam_map[s] + seam_map[s + 1] + seam_map[s + 2]) / 3.0

    block_means = {s: block_mean(s, seam) for s in range(1, 112)}  # 111 blocks
    ranked = sorted(block_means.items(), key=lambda kv: kv[1])
    rank_2345 = [i for i, (s, m) in enumerate(ranked, 1) if s == 2][0]
    obs_block_mean = block_means[2]
    A_H1 = (rank_2345 == 1)
    seam_q2q3 = seam[2]
    seam_q3q4 = seam[3]
    A_H2 = (seam_q2q3 <= seam_median) and (seam_q3q4 <= seam_median)
    armA_verdict = 'CONFIRMED' if (A_H1 and A_H2) else 'NULL'

    # ---- ARM B: Q3 cohesion anchor (H-NEW-590) ----
    rec3 = [r for r in d590['all_surahs_results'] if r.get('X') == 3][0]
    delta_pct_3 = rec3['delta_pct']
    class_3 = rec3['classification']
    B_H1 = (delta_pct_3 < 0) and (class_3 == 'COHESION_ANCHOR')
    armB_verdict = 'CONFIRMED' if B_H1 else 'NULL (pre-commit violation)'

    # ---- ARM C: permutation null (max-statistic: min block-mean over random seam arrangements) ----
    rng = random.Random(SEED)
    positions = list(range(1, 114))  # 113 seam positions s=1..113
    null_mins = []
    for _ in range(N_PERM):
        shuffled = seam_vals[:]
        rng.shuffle(shuffled)
        perm_seam = {s: shuffled[i] for i, s in enumerate(positions)}
        mn = min((perm_seam[s] + perm_seam[s + 1] + perm_seam[s + 2]) / 3.0 for s in range(1, 112))
        null_mins.append(mn)
    n_le = sum(1 for x in null_mins if x <= obs_block_mean)
    p_perm = (n_le + 1) / (N_PERM + 1)
    null_mean = sum(null_mins) / len(null_mins)
    null_var = sum((x - null_mean) ** 2 for x in null_mins) / len(null_mins)
    null_std = null_var ** 0.5
    z = (obs_block_mean - null_mean) / null_std if null_std else float('nan')
    C_H1 = (p_perm < 0.05)
    armC_verdict = 'CONFIRMED' if C_H1 else 'NULL'

    out = {
        'test_id': 'Q003-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC v0.4 STEM-root, Fisher-Rao, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'seam_median': seam_median,
        'arm_A': {
            'block_2345_internal_seams': [seam[2], seam[3], seam[4]],
            'block_2345_mean_internal_seam': obs_block_mean,
            'rank_among_111_blocks_ascending': rank_2345,
            'smoothest_6_blocks': [(s, round(m, 6)) for s, m in ranked[:6]],
            'A_H1_rank_is_1': A_H1,
            'seam_Q2Q3': seam_q2q3,
            'seam_Q3Q4': seam_q3q4,
            'A_H2_both_seams_le_median': A_H2,
            'verdict': armA_verdict,
        },
        'arm_B': {
            'delta_pct_X3': delta_pct_3,
            'classification_X3': class_3,
            'window': rec3['window'],
            'd_W': rec3['d_W'],
            'd_W_minus_X': rec3['d_W_minus_X'],
            'B_H1_cohesion_anchor': B_H1,
            'verdict': armB_verdict,
        },
        'arm_C': {
            'obs_block_mean': obs_block_mean,
            'null_min_mean': null_mean,
            'null_min_std': null_std,
            'z': z,
            'p_perm': p_perm,
            'n_le': n_le,
            'alpha': 0.05,
            'C_H1_pass': C_H1,
            'verdict': armC_verdict,
        },
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("\n===== Q003-F-01 RESULTS =====")
    print(f"ARM A: block{{2,3,4,5}} mean_seam={obs_block_mean:.5f} rank={rank_2345}/111 | "
          f"seam_median={seam_median:.5f} Q2Q3={seam_q2q3:.5f} Q3Q4={seam_q3q4:.5f} | "
          f"A-H1={A_H1} A-H2={A_H2} -> {armA_verdict}")
    print(f"ARM B: Q3 delta_pct={delta_pct_3} class={class_3} -> {armB_verdict}")
    print(f"ARM C: obs={obs_block_mean:.5f} null_min_mean={null_mean:.5f} z={z:.3f} "
          f"p_perm={p_perm:.5f} -> {armC_verdict}")
    print(f"\nWrote {OUT_PATH}")


if __name__ == '__main__':
    main()
