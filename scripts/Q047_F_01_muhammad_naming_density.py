#!/usr/bin/env python3
"""
Q047-F-01 — Muhammad-naming density: Q 47 in {Q 3, Q 33, Q 47, Q 48}.
Pre-reg SHA verified at runtime; fail-fast on mismatch.
Seed: 20260508. Bonferroni-1.
"""
import json, re, hashlib, os, sys

EXPECTED_SHA = '3fe40cf8cb8e8f0505f54904db7edc710c511f5abe19565cb1d4afb9ca1c62c1'
PREREG_PATH = '/Users/grey/Downloads/quran/surahs/Q047-muhammad/Q047-F-01-muhammad-naming-density-prereg.md'
QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q047-muhammad/csv/Q047-F-01.json'

ANNO_PUNCT_RE = re.compile(r'[ۣۖۗۘۚۛۜ۠ۡۢۤۥۦۧۨ۩ۭ]')

def clean(s):
    return ANNO_PUNCT_RE.sub('', s).strip()

def verify_sha():
    with open(PREREG_PATH, 'rb') as f:
        got = hashlib.sha256(f.read()).hexdigest()
    if got != EXPECTED_SHA:
        print(f'SHA MISMATCH: expected {EXPECTED_SHA}, got {got}')
        sys.exit(1)
    print(f'Pre-reg SHA verified: {got}')

def main():
    verify_sha()
    q = json.load(open(QURAN_PATH))

    target_surahs = [3, 33, 47, 48]
    muhd_re = re.compile(r'\bمحمد\b')
    ahmd_re = re.compile(r'\bأحمد\b')

    surah_words = []
    surah_muhammad = []
    surah_ahmad = []
    for s in range(1, 115):
        words_str = ' '.join(clean(v['text']) for v in q[s-1]['verses'])
        words = words_str.split()
        n_words = len(words)
        n_mhd = len(muhd_re.findall(words_str))
        n_ahd = len(ahmd_re.findall(words_str))
        surah_words.append(n_words)
        surah_muhammad.append(n_mhd)
        surah_ahmad.append(n_ahd)

    # Per-1000-word density for Muhammad-named surahs
    densities = {}
    for s in target_surahs:
        n = surah_words[s-1]
        m = surah_muhammad[s-1]
        densities[s] = {
            'word_count': n,
            'muhammad_count': m,
            'density_per_1000w': (m / n * 1000) if n else 0,
        }

    sorted_dens = sorted(densities.items(), key=lambda x: -x[1]['density_per_1000w'])
    rank_47 = next(i+1 for i,(s,_) in enumerate(sorted_dens) if s == 47)

    den_47 = densities[47]['density_per_1000w']
    others = [densities[s]['density_per_1000w'] for s in target_surahs if s != 47]
    strict_top1 = all(den_47 > o for o in others)

    if strict_top1:
        verdict = 'VINDICATED'
    elif rank_47 <= 2:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    # Surahs with Muhammad/Ahmad mention totals
    all_named_surahs = []
    for s in range(1, 115):
        if surah_muhammad[s-1] or surah_ahmad[s-1]:
            all_named_surahs.append({
                'surah': s,
                'muhammad': surah_muhammad[s-1],
                'ahmad': surah_ahmad[s-1],
                'words': surah_words[s-1],
            })

    out = {
        'test_id': 'Q047-F-01',
        'pre_reg_sha': EXPECTED_SHA,
        'seed': 20260508,
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'corpus_total_muhammad_mentions': sum(surah_muhammad),
        'corpus_total_ahmad_mentions': sum(surah_ahmad),
        'all_named_surahs': all_named_surahs,
        'target_surahs_densities': densities,
        'sorted_by_density': [{'surah': s, **d} for s,d in sorted_dens],
        'Q47_rank_in_4set': rank_47,
        'Q47_strict_top1': strict_top1,
        'verdict': verdict,
        'bonferroni_k': 1,
        'alpha_bon': 0.05,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'Q047-F-01 verdict: {verdict}')
    print(f'  Q47 density: {den_47:.4f} per-1000-words')
    print(f'  Q47 rank in 4-set: {rank_47}/4')
    print(f'  Densities sorted: {[(s, round(d["density_per_1000w"],4)) for s,d in sorted_dens]}')
    print(f'  Total Muhammad in corpus: {sum(surah_muhammad)} (predicted 4)')
    print(f'  Total Ahmad in corpus: {sum(surah_ahmad)} (predicted 1)')

if __name__ == '__main__':
    main()
