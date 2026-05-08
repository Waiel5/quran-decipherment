#!/usr/bin/env python3
"""Q016-F-05 — Chrono-vs-mushaf displacement vs true-isolate status.

Pre-reg: surahs/Q016-al-nahl/Q016-F-05-chrono-displacement-isolate-prereg.md
SHA256: 2fe13979bb7c46734e96b25405b0488e74f817fd5041bd728ee7e86a5f0edb50
Seed: 20260507
"""
import json, hashlib, sys, os, random, csv
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q016-al-nahl/Q016-F-05-chrono-displacement-isolate-prereg.md'
EXPECTED_SHA = '2fe13979bb7c46734e96b25405b0488e74f817fd5041bd728ee7e86a5f0edb50'
SEED = 20260507
N_PERM = 10000
ALPHA_BON = 0.025

REV_ORDER_CSV = '/Users/grey/Downloads/quran/data/revelation-order.csv'
ISOLATES = {16, 21, 22, 23, 25}


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def load_chrono():
    """Returns dict mushaf_pos -> {tanzil_rank, noldeke_rank}."""
    by_mushaf = {}
    with open(REV_ORDER_CSV) as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                m = int(row['mushaf_order'])
                t = int(row['revelation_order'])
                n = int(row['noldeke_order'])
                by_mushaf[m] = {'tanzil': t, 'noldeke': n}
            except (ValueError, KeyError):
                pass
    return by_mushaf


def spearman(x, y):
    """Compute Spearman ρ between two equal-length lists."""
    n = len(x)
    rx = rank(x)
    ry = rank(y)
    mean_rx = sum(rx) / n
    mean_ry = sum(ry) / n
    num = sum((rx[i]-mean_rx)*(ry[i]-mean_ry) for i in range(n))
    den_x = (sum((rx[i]-mean_rx)**2 for i in range(n)))**0.5
    den_y = (sum((ry[i]-mean_ry)**2 for i in range(n)))**0.5
    if den_x == 0 or den_y == 0: return 0
    return num / (den_x * den_y)


def rank(values):
    """Average-rank handling ties."""
    n = len(values)
    indexed = sorted(range(n), key=lambda i: values[i])
    ranks = [0]*n
    i = 0
    while i < n:
        j = i
        while j+1 < n and values[indexed[j+1]] == values[indexed[i]]:
            j += 1
        avg = (i + j + 2) / 2  # 1-based avg
        for k in range(i, j+1):
            ranks[indexed[k]] = avg
        i = j + 1
    return ranks


def main():
    verify_sha()
    chrono = load_chrono()

    surahs = sorted(chrono.keys())
    disp_tanzil = [abs(chrono[s]['tanzil'] - s) for s in surahs]
    disp_noldeke = [abs(chrono[s]['noldeke'] - s) for s in surahs]
    is_iso = [1 if s in ISOLATES else 0 for s in surahs]

    # Q16 + sister-isolate displacements
    print('Q16 displacement (Tanzil):', abs(chrono[16]['tanzil'] - 16))
    print('Q16 displacement (Nöldeke):', abs(chrono[16]['noldeke'] - 16))
    iso_tanzil = [(s, abs(chrono[s]['tanzil']-s)) for s in ISOLATES]
    iso_noldeke = [(s, abs(chrono[s]['noldeke']-s)) for s in ISOLATES]
    print('All 5 isolates Tanzil:', iso_tanzil, '  mean=', sum(d for _, d in iso_tanzil)/5)
    print('All 5 isolates Nöldeke:', iso_noldeke, '  mean=', sum(d for _, d in iso_noldeke)/5)
    non_iso_disp_tanzil = [d for s, d in zip(surahs, disp_tanzil) if s not in ISOLATES]
    non_iso_disp_noldeke = [d for s, d in zip(surahs, disp_noldeke) if s not in ISOLATES]
    print('Non-isolate mean displacement (Tanzil):', sum(non_iso_disp_tanzil)/len(non_iso_disp_tanzil))
    print('Non-isolate mean displacement (Nöldeke):', sum(non_iso_disp_noldeke)/len(non_iso_disp_noldeke))

    # Spearman
    rho_t = spearman(disp_tanzil, is_iso)
    rho_n = spearman(disp_noldeke, is_iso)
    print(f'Spearman ρ (Tanzil disp × is_isolate): {rho_t:.4f}')
    print(f'Spearman ρ (Nöldeke disp × is_isolate): {rho_n:.4f}')

    # Permutation null: random 5-of-114 isolate assignments; compute ρ; empirical p = fraction ≥ observed
    rng = random.Random(SEED)
    n_ge_t = 0
    n_ge_n = 0
    for _ in range(N_PERM):
        sample = set(rng.sample(surahs, 5))
        is_perm = [1 if s in sample else 0 for s in surahs]
        rho_perm_t = spearman(disp_tanzil, is_perm)
        rho_perm_n = spearman(disp_noldeke, is_perm)
        if rho_perm_t >= rho_t: n_ge_t += 1
        if rho_perm_n >= rho_n: n_ge_n += 1
    p_t = (n_ge_t + 1) / (N_PERM + 1)
    p_n = (n_ge_n + 1) / (N_PERM + 1)

    # MW-5 / MW-6: positive controls
    # Replace isolates with terminal qiṣār {110,111,112,113,114} (rev-early, mushaf-late → high disp)
    sample_terminal = {110, 111, 112, 113, 114}
    is_terminal = [1 if s in sample_terminal else 0 for s in surahs]
    rho_term_t = spearman(disp_tanzil, is_terminal)
    # Should be POSITIVE (high disp)
    # Replace isolates with head ṭiwāl {1,2,3,4,5} → mostly low disp (Q1=mushaf 1, rev 5; Q2=mushaf 2, rev 87 etc — mixed)
    sample_head = {1, 2, 3, 4, 5}
    is_head = [1 if s in sample_head else 0 for s in surahs]
    rho_head_t = spearman(disp_tanzil, is_head)

    a_reject = (rho_t > 0 and p_t <= ALPHA_BON)
    b_reject = (rho_n > 0 and p_n <= ALPHA_BON)
    if a_reject and b_reject:
        verdict = 'CONFIRMED'
    elif a_reject or b_reject:
        verdict = 'DIRECTIONAL'
    elif rho_t < 0 and rho_n < 0:
        verdict = 'PRE_COMMIT_VIOLATION'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q016-F-05',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(Hafs-Kufan, mushaf-position, Tanzil/Nöldeke chronologies)',
        'isolates': sorted(ISOLATES),
        'isolate_displacements_tanzil': iso_tanzil,
        'isolate_displacements_noldeke': iso_noldeke,
        'isolate_mean_disp_tanzil': sum(d for _,d in iso_tanzil)/5,
        'isolate_mean_disp_noldeke': sum(d for _,d in iso_noldeke)/5,
        'non_isolate_mean_disp_tanzil': sum(non_iso_disp_tanzil)/len(non_iso_disp_tanzil),
        'non_isolate_mean_disp_noldeke': sum(non_iso_disp_noldeke)/len(non_iso_disp_noldeke),
        'spearman_rho_tanzil': rho_t,
        'spearman_rho_noldeke': rho_n,
        'p_perm_tanzil': p_t,
        'p_perm_noldeke': p_n,
        'mw5_terminal_qisar_rho_tanzil': rho_term_t,
        'mw5_head_tiwal_rho_tanzil': rho_head_t,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv/Q016-F-05.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\np_perm Tanzil = {p_t:.4f}, p_perm Nöldeke = {p_n:.4f}")
    print(f"MW-5 terminal-qisar control rho={rho_term_t:.4f} (should be HIGH POSITIVE)")
    print(f"MW-5 head-tiwal control rho={rho_head_t:.4f} (should be NEGATIVE/near-zero)")
    print(f"VERDICT: {verdict}")


if __name__ == '__main__':
    main()
