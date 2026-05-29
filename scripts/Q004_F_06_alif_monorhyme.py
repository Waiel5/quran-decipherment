#!/usr/bin/env python3
"""Q004-F-06 — the al-Nisāʾ alif-monorhyme anomaly.

(Test numbered F-06 because Q004-F-01..F-05 are taken by a prior 2026-05-07 pre-registered set
 — legal-density, vocabulary-saturation, fraction-coherence, q4:1-q39:6 twin, marriage-khutba.)

Pre-reg: surahs/Q004-al-nisa/Q004-F-06-alif-monorhyme-prereg.md
Pre-reg SHA256: 47eec58b703727e0acddd9b61bb60dac36b610d3850ebdcb08292e99af55cec6
Rules-tuple: (min-tashkeel rhyme final-letter, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

Arm A: among al-sabʿ al-ṭiwāl {2,3,4,5,6,7,9}, is Q4 the UNIQUE alif-dominant surah (others nūn)?
Arm B: is Q4's sig_A in the bottom-3 of 114 AND z_rhyme_entropy < 0 (structural-iʿjāz minimum)?
Arm C: length-stratified null (n_verses>=100, seed 20260509, 10000 perms): is Q4's frac an upper-tail extreme?
"""
import json
import hashlib
import sys
import os
import random

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs/Q004-al-nisa/Q004-F-06-alif-monorhyme-prereg.md')
EXPECTED_SHA = '47eec58b703727e0acddd9b61bb60dac36b610d3850ebdcb08292e99af55cec6'
SEED = 20260509
N_PERM = 10000
OUT_PATH = os.path.join(ROOT, 'surahs/Q004-al-nisa/csv/Q004-F-06.json')

ALIF = 'ا'
NUN = 'ن'
TIWAL = [2, 3, 4, 5, 6, 7, 9]
TIWAL_ALT = [2, 3, 4, 5, 6, 7, 8]  # alt roster taking Q8 (anfal) as 7th instead of Q9


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)
    print(f"SHA OK: {actual}")


def main():
    verify_sha()
    d700 = json.load(open(os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-700.json')))
    d750 = json.load(open(os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-750.json')))

    rld = {r['surah']: r for r in d700['rhyme']['rhyme_letter_diagnostics']}
    per750 = {r['surah']: r for r in d750['per_surah']}

    # ---- ARM A: Q4 unique alif in al-sabʿ al-ṭiwāl ----
    tiwal_letters = {s: rld[s]['top_letter'] for s in TIWAL}
    alif_members = [s for s in TIWAL if tiwal_letters[s] == ALIF]
    A_H1 = (alif_members == [4])
    others_all_nun = all(tiwal_letters[s] == NUN for s in TIWAL if s != 4)
    armA_verdict = 'CONFIRMED' if (A_H1 and others_all_nun) else 'NULL'
    # robustness: alt roster
    tiwal_alt_letters = {s: rld[s]['top_letter'] for s in TIWAL_ALT}
    alif_alt = [s for s in TIWAL_ALT if tiwal_alt_letters[s] == ALIF]

    # ---- ARM B: sig_A bottom-3 + low rhyme entropy ----
    sigA_desc = sorted(per750.values(), key=lambda r: -r['sig_A'])
    sigA_rank_4 = [i for i, r in enumerate(sigA_desc, 1) if r['surah'] == 4][0]
    z_rhyme_4 = per750[4]['z_rhyme_entropy']
    rhyme_entropy_4 = per750[4]['rhyme_entropy_nats']
    B_H1 = (sigA_rank_4 >= 112) and (z_rhyme_4 < 0)
    armB_verdict = 'CONFIRMED' if B_H1 else 'NULL'

    # ---- ARM C: length-stratified frac null (n_verses >= 100, excluding Q4) ----
    pool = [r['frac'] for s, r in rld.items() if r['n_verses'] >= 100 and s != 4]
    frac_4 = rld[4]['frac']
    rng = random.Random(SEED)
    draws = [rng.choice(pool) for _ in range(N_PERM)]
    n_ge = sum(1 for x in draws if x >= frac_4)
    p_perm = (n_ge + 1) / (N_PERM + 1)
    null_mean = sum(draws) / len(draws)
    null_var = sum((x - null_mean) ** 2 for x in draws) / len(draws)
    null_std = null_var ** 0.5
    z = (frac_4 - null_mean) / null_std if null_std else float('nan')
    C_H1 = (p_perm < 0.05)
    # pre-committed honest-limit: how many long surahs exceed Q4?
    long_exceeding = sorted([(s, r['frac']) for s, r in rld.items()
                             if r['n_verses'] >= 100 and r['frac'] > frac_4],
                            key=lambda kv: -kv[1])
    armC_verdict = 'CONFIRMED' if C_H1 else 'NULL/DIRECTIONAL (notable-not-extreme)'

    out = {
        'test_id': 'Q004-F-06',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(min-tashkeel rhyme, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'arm_A': {
            'tiwal_roster': TIWAL,
            'tiwal_dominant_letters': tiwal_letters,
            'alif_members': alif_members,
            'A_H1_Q4_unique_alif': A_H1,
            'others_all_nun': others_all_nun,
            'alt_roster': TIWAL_ALT,
            'alt_roster_letters': tiwal_alt_letters,
            'alt_roster_alif_members': alif_alt,
            'verdict': armA_verdict,
        },
        'arm_B': {
            'sig_A_Q4': per750[4]['sig_A'],
            'sig_A_rank_desc': sigA_rank_4,
            'rhyme_entropy_nats_Q4': rhyme_entropy_4,
            'z_rhyme_entropy_Q4': z_rhyme_4,
            'B_H1_pass': B_H1,
            'verdict': armB_verdict,
        },
        'arm_C': {
            'frac_Q4': frac_4,
            'top_letter_Q4': rld[4]['top_letter'],
            'n_verses_Q4': rld[4]['n_verses'],
            'pool_size': len(pool),
            'null_mean': null_mean,
            'null_std': null_std,
            'z': z,
            'p_perm': p_perm,
            'n_ge': n_ge,
            'alpha': 0.05,
            'long_surahs_exceeding_Q4': long_exceeding,
            'C_H1_pass': C_H1,
            'verdict': armC_verdict,
        },
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("\n===== Q004-F-06 RESULTS =====")
    print(f"ARM A: tiwal letters={tiwal_letters} alif_members={alif_members} -> {armA_verdict}")
    print(f"ARM B: sig_A(Q4)={per750[4]['sig_A']:.4f} rank={sigA_rank_4}/114 "
          f"z_rhyme_entropy={z_rhyme_4:.4f} -> {armB_verdict}")
    print(f"ARM C: frac(Q4)={frac_4:.4f} ({rld[4]['n_verses']}v) null_mean={null_mean:.4f} "
          f"z={z:.3f} p_perm={p_perm:.5f} -> {armC_verdict}")
    print(f"       long surahs exceeding Q4: {long_exceeding}")
    print(f"\nWrote {OUT_PATH}")


if __name__ == '__main__':
    main()
