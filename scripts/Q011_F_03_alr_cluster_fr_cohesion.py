#!/usr/bin/env python3
"""Q011-F-03 — Q 11 FR-distance pull-in to ALR-siblings vs length-matched non-ALR.

Pre-reg: surahs/Q011-hud/preregs/Q011-F-03-alr-cluster-fr-cohesion-prereg.md
Pre-reg SHA256: 4c69a83734cce6db3ea07eff20907820643a06fbac9a35011cc2465f9e6a4b45
Rules-tuple: (no-tashkeel, FR-distance from h-new-111,
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed: 20260507
"""
import json, hashlib, sys, os, random

PREREG = '/Users/grey/Downloads/quran/surahs/Q011-hud/preregs/Q011-F-03-alr-cluster-fr-cohesion-prereg.md'
EXPECTED_SHA = '4c69a83734cce6db3ea07eff20907820643a06fbac9a35011cc2465f9e6a4b45'
SEED = 20260507
N_PERM = 10000


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def reconstruct_fr_matrix(path):
    with open(path) as f:
        d = json.load(f)
    ut = d['D_matrix_upper_triangular']
    M = [[0.0]*114 for _ in range(114)]
    for entry in ut:
        i, j, v = entry
        # Convert to 0-indexed
        i0 = int(i) - 1; j0 = int(j) - 1
        M[i0][j0] = float(v)
        M[j0][i0] = float(v)
    return M


def main():
    verify_sha()
    M = reconstruct_fr_matrix('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json')
    q11 = 11

    # Verse counts for length-matching
    with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
        quran = json.load(f)
    n_verses = {s['id']: len(s['verses']) for s in quran}
    n_q11 = n_verses[q11]

    alr_siblings = [10, 12, 14, 15]  # Q 11's ALR-strict siblings
    excluded = {10, 11, 12, 13, 14, 15}  # ALR + ALMR cluster

    candidates = [s for s in range(1, 115) if s not in excluded]
    candidates_sorted = sorted(candidates, key=lambda s: abs(n_verses[s] - n_q11))
    length_matched = candidates_sorted[:20]

    # FR distances from Q 11 to each
    def fr(s):
        return M[q11-1][s-1]

    d_alr = [fr(s) for s in alr_siblings]
    d_lm = [fr(s) for s in length_matched]
    mean_alr = sum(d_alr) / len(d_alr)
    mean_lm = sum(d_lm) / len(d_lm)
    T_obs = mean_alr - mean_lm  # Negative = ALR closer (direction-matched)

    # Permutation null: random partitions
    rng = random.Random(SEED)
    pool = alr_siblings + length_matched  # 24 surahs
    pool_d = [fr(s) for s in pool]
    n_alr = len(alr_siblings)
    le_count = 0
    perms = []
    for _ in range(N_PERM):
        idx = list(range(len(pool)))
        rng.shuffle(idx)
        fake_alr = [pool_d[i] for i in idx[:n_alr]]
        fake_lm = [pool_d[i] for i in idx[n_alr:]]
        T_perm = sum(fake_alr)/n_alr - sum(fake_lm)/len(fake_lm)
        perms.append(T_perm)
        if T_perm <= T_obs:
            le_count += 1
    p_lower = (le_count + 1) / (N_PERM + 1)

    if T_obs < 0 and p_lower <= 0.05:
        verdict = 'CONFIRMED'
    elif T_obs < 0 and p_lower <= 0.10:
        verdict = 'DIRECTIONAL'
    elif T_obs >= 0 or p_lower > 0.10:
        verdict = 'NULL'
    else:
        verdict = 'NULL'
    if p_lower >= 0.95:
        verdict = 'NULL — pre-commit-violation candidate (T strongly positive)'

    out = {
        'finding_id': 'Q011-F-03',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, FR-distance from h-new-111, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'alr_siblings': alr_siblings,
        'length_matched_non_alr': length_matched,
        'q11_to_alr_distances': dict(zip(alr_siblings, d_alr)),
        'q11_to_length_matched_distances': dict(zip(length_matched, d_lm)),
        'mean_alr': mean_alr,
        'mean_length_matched': mean_lm,
        'T_obs': T_obs,
        'p_lower': p_lower,
        'verdict': verdict,
    }
    out_dir = '/Users/grey/Downloads/quran/surahs/Q011-hud/csv'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'Q011-F-03.json'), 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Q011-F-03 verdict: {verdict}")
    print(f"  mean ALR FR: {mean_alr:.4f}")
    print(f"  mean length-matched non-ALR FR: {mean_lm:.4f}")
    print(f"  T_obs: {T_obs:.4f}")
    print(f"  p_lower: {p_lower:.4f}")


if __name__ == '__main__':
    main()
