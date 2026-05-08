#!/usr/bin/env python3
"""
Q032-F-02 — Q 32 ↔ Q 67 architectural-twin extension on 4 content axes.
Pre-reg SHA verified at runtime; fail-fast on mismatch.
Seed: 20260508. Bonferroni-4.
"""
import json, re, math, random, hashlib, os, sys
from collections import Counter

EXPECTED_SHA = '2f94580c3714cc4f7ce375e5160a1a6185935f4ce75a70fd87285b8f8a58e975'
PREREG_PATH = '/Users/grey/Downloads/quran/surahs/Q032-al-sajda/Q032-F-02-q32-q67-twin-axes-prereg.md'
QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
QURAN_MIN = '/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json'
H750 = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q032-al-sajda/csv/Q032-F-02.json'

ANNO_PUNCT_RE = re.compile(r'[ۣۖۗۘۚۛۜ۠ۡۢۤۥۦۧۨ۩ۭ]')
TASHKEEL_RE = re.compile(r'[ً-ْٰـ]')

def clean(s):
    return ANNO_PUNCT_RE.sub('', s).strip()

def verify_sha():
    with open(PREREG_PATH, 'rb') as f:
        got = hashlib.sha256(f.read()).hexdigest()
    if got != EXPECTED_SHA:
        print(f'SHA MISMATCH: expected {EXPECTED_SHA}, got {got}')
        sys.exit(1)
    print(f'Pre-reg SHA verified: {got}')

def get_words(q, s):
    return ' '.join(clean(v['text']) for v in q[s-1]['verses']).split()

def main():
    verify_sha()
    q = json.load(open(QURAN_PATH))
    h750 = json.load(open(H750))

    sig_q32 = next(e for e in h750['per_surah'] if e['surah']==32)
    sig_q67 = next(e for e in h750['per_surah'] if e['surah']==67)

    # Axis A1 — top final-letter equality
    top_q32 = sig_q32['top_final_letter']
    top_q67 = sig_q67['top_final_letter']
    a1_pass = top_q32 == top_q67

    # Axis A2 — sig_A within 0.5
    siga_q32 = sig_q32['sig_A']
    siga_q67 = sig_q67['sig_A']
    a2_diff = abs(siga_q32 - siga_q67)
    a2_pass = a2_diff < 0.5

    # Axis A3 — length-class
    n_q32 = sig_q32['n_verses']
    n_q67 = sig_q67['n_verses']
    a3_diff = abs(n_q32 - n_q67)
    a3_pass = a3_diff <= 5

    # Axis A4 — divine-name density (top-30 corpus-wide)
    divine_names = [
        'الله', 'الرحمن', 'الرحيم', 'الملك', 'العزيز', 'الحكيم',
        'العليم', 'القدير', 'اللطيف', 'الخبير', 'السميع', 'البصير',
        'رب', 'ربك', 'ربكم', 'ربنا', 'ربهم', 'ربه', 'ربها', 'ربى',
    ]
    div_set = set(divine_names)

    densities = []
    for s in range(1, 115):
        words = get_words(q, s)
        n = len(words) or 1
        cnt = sum(1 for w in words if w in div_set)
        densities.append((s, cnt / n * 100, cnt, n))

    densities_sorted = sorted(densities, key=lambda x: -x[1])
    rank_q32 = next(i+1 for i,(s,r,c,n) in enumerate(densities_sorted) if s==32)
    rank_q67 = next(i+1 for i,(s,r,c,n) in enumerate(densities_sorted) if s==67)
    den_q32 = next(r for s,r,c,n in densities if s==32)
    den_q67 = next(r for s,r,c,n in densities if s==67)
    a4_pass = (rank_q32 <= 30) and (rank_q67 <= 30)

    n_pass = sum([a1_pass, a2_pass, a3_pass, a4_pass])
    verdict = ('VINDICATED' if n_pass == 4
               else 'DIRECTIONAL' if n_pass >= 3
               else 'NULL')

    out = {
        'test_id': 'Q032-F-02',
        'pre_reg_sha': EXPECTED_SHA,
        'seed': 20260508,
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'A1_rhyme': {
            'Q32_top_final': top_q32,
            'Q67_top_final': top_q67,
            'pass': a1_pass,
        },
        'A2_sig_A': {
            'Q32_sig_A': siga_q32,
            'Q67_sig_A': siga_q67,
            'abs_diff': a2_diff,
            'threshold': 0.5,
            'pass': a2_pass,
        },
        'A3_length_class': {
            'Q32_n_verses': n_q32,
            'Q67_n_verses': n_q67,
            'abs_diff': a3_diff,
            'threshold': 5,
            'pass': a3_pass,
        },
        'A4_divine_density': {
            'Q32_density_per_100w': den_q32,
            'Q67_density_per_100w': den_q67,
            'Q32_rank': rank_q32,
            'Q67_rank': rank_q67,
            'threshold': 30,
            'top_5_surahs_by_density': [{'surah': s, 'density': round(r,3), 'count': c, 'words': n} for s,r,c,n in densities_sorted[:5]],
            'pass': a4_pass,
        },
        'axes_passed': n_pass,
        'axes_total': 4,
        'bonferroni_k': 4,
        'alpha_bon': 0.0125,
        'verdict': verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'Q032-F-02 verdict: {verdict} ({n_pass}/4 axes passed)')
    print(f'  A1 rhyme: Q32={top_q32}, Q67={top_q67} -> pass={a1_pass}')
    print(f'  A2 sig_A: Q32={siga_q32:.3f}, Q67={siga_q67:.3f}, diff={a2_diff:.3f} -> pass={a2_pass}')
    print(f'  A3 length: Q32={n_q32}, Q67={n_q67}, diff={a3_diff} -> pass={a3_pass}')
    print(f'  A4 div-density: Q32 rank {rank_q32}, Q67 rank {rank_q67} -> pass={a4_pass}')

if __name__ == '__main__':
    main()
