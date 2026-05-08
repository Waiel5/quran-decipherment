#!/usr/bin/env python3
"""Q016-F-01 — Niʿmah-catalog vocabulary saturation in Q 16.

Pre-reg: surahs/Q016-al-nahl/Q016-F-01-nimah-catalog-saturation-prereg.md
SHA256: 1604d9a5e68bb4e23fd76e644717f61f3160f3d7effdcdb0aec5d4704cb96e24
Rules-tuple: (no-tashkeel, orthographic-token, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed: 20260507
"""
import json, re, hashlib, sys, os, random

PREREG = '/Users/grey/Downloads/quran/surahs/Q016-al-nahl/Q016-F-01-nimah-catalog-saturation-prereg.md'
EXPECTED_SHA = '1604d9a5e68bb4e23fd76e644717f61f3160f3d7effdcdb0aec5d4704cb96e24'
SEED = 20260507
N_PERM = 10000


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()

    # Niʿmah-catalog marker set (3 components)
    A_mercy = [r'نعمة', r'نعم', r'نعمت', r'نعمه', r'رحمة', r'رحمه', r'النعمة', r'بنعمت']
    B_verbs = [
        r'سخر', r'سخرنا', r'يسخر', r'سخره', r'سخرها',
        r'أنزل', r'أنزلنا', r'انزل', r'انزلنا', r'نزلنا', r'ينزل',
        r'أنبت', r'أنبتنا', r'ينبت', r'انبت', r'انبتنا',
        r'جعل', r'جعلنا', r'يجعل',
        r'أخرج', r'أخرجنا', r'يخرج', r'اخرج', r'اخرجنا',
    ]
    C_objects = [
        r'الأنعام', r'أنعام', r'الانعام', r'انعام',
        r'الماء', r'ماء',
        r'البحر', r'بحر', r'البحار', r'بحرين', r'البحرين',
        r'الأنهار', r'انهار', r'أنهار', r'الانهار',
        r'الجبال', r'جبال', r'جبل',
        r'الشجر', r'شجر', r'الأشجار', r'أشجار', r'شجرة',
        r'الثمرات', r'ثمرات', r'الثمر', r'ثمر',
        r'السماء', r'سماء', r'السماوات', r'سماوات', r'السموات',
        r'الشمس', r'شمس',
        r'القمر', r'قمر',
        r'النجوم', r'نجوم', r'نجم',
        r'الليل', r'ليل',
        r'النهار', r'نهار',
        r'اللبن', r'لبن', r'اللبنا',
        r'العسل', r'عسل',
        r'الزرع', r'زرع', r'زروع',
        r'الفلك', r'فلك',
    ]

    pat_A = re.compile(r'\b(' + '|'.join(A_mercy) + r')\b')
    pat_B = re.compile(r'\b(' + '|'.join(B_verbs) + r')\b')
    pat_C = re.compile(r'\b(' + '|'.join(C_objects) + r')\b')
    pat_all = re.compile(r'\b(' + '|'.join(A_mercy + B_verbs + C_objects) + r')\b')

    d = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    results = []
    all_tokens = []  # (token, surah)
    for s in d:
        verses = s['verses']
        text_full = ' '.join(v['text'] for v in verses)
        tokens = text_full.split()
        n_words = len(tokens)
        n_a = len(pat_A.findall(text_full))
        n_b = len(pat_B.findall(text_full))
        n_c = len(pat_C.findall(text_full))
        n_total = len(pat_all.findall(text_full))
        results.append({
            'surah': s['id'], 'name': s['transliteration'], 'n_verses': len(verses),
            'n_tokens': n_words,
            'n_A_mercy': n_a, 'n_B_verbs': n_b, 'n_C_objects': n_c,
            'n_total': n_total,
            'nimah_density_per_100tok': 100.0 * n_total / n_words if n_words else 0,
            'A_density_per_100tok': 100.0 * n_a / n_words if n_words else 0,
            'B_density_per_100tok': 100.0 * n_b / n_words if n_words else 0,
            'C_density_per_100tok': 100.0 * n_c / n_words if n_words else 0,
        })
        for t in tokens:
            all_tokens.append((t, s['id']))

    # Q16 rank
    by_total = sorted(results, key=lambda x: -x['nimah_density_per_100tok'])
    rank_total = next(i for i,r in enumerate(by_total,1) if r['surah']==16)
    by_A = sorted(results, key=lambda x: -x['A_density_per_100tok'])
    rank_A = next(i for i,r in enumerate(by_A,1) if r['surah']==16)
    by_B = sorted(results, key=lambda x: -x['B_density_per_100tok'])
    rank_B = next(i for i,r in enumerate(by_B,1) if r['surah']==16)
    by_C = sorted(results, key=lambda x: -x['C_density_per_100tok'])
    rank_C = next(i for i,r in enumerate(by_C,1) if r['surah']==16)

    q16 = next(r for r in results if r['surah']==16)
    q16_density = q16['nimah_density_per_100tok']
    q16_n_tokens = q16['n_tokens']

    # Permutation null: random-resample q16_n_tokens tokens from corpus (not stratified by surah)
    random.seed(SEED)
    corpus_tokens = [t for t, _ in all_tokens]
    n_ge = 0
    for _ in range(N_PERM):
        sample = random.sample(corpus_tokens, q16_n_tokens)
        text_sample = ' '.join(sample)
        n_match = len(pat_all.findall(text_sample))
        density = 100.0 * n_match / q16_n_tokens
        if density >= q16_density:
            n_ge += 1
    p_perm = (n_ge + 1) / (N_PERM + 1)

    # MW-5 / MW-6 controls
    q14 = next(r for r in results if r['surah']==14)
    rank_q14 = next(i for i,r in enumerate(by_total,1) if r['surah']==14)
    q12 = next(r for r in results if r['surah']==12)
    rank_q12 = next(i for i,r in enumerate(by_total,1) if r['surah']==12)
    mw5 = {'q14_rank': rank_q14, 'q14_density': q14['nimah_density_per_100tok'], 'pass_top15': rank_q14 <= 15}
    mw6 = {'q12_rank': rank_q12, 'q12_density': q12['nimah_density_per_100tok'], 'pass_bottom_half': rank_q12 > 57}

    verdict = 'PASS-DIRECTED-CONFIRMED' if rank_total <= 3 and p_perm <= 0.0167 else (
              'DIRECTIONAL' if rank_total <= 10 and p_perm <= 0.05 else
              'PRE_COMMIT_VIOLATION' if rank_total >= 86 else 'NULL')

    out = {
        'finding_id': 'Q016-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'q16': q16,
        'q16_rank_total': rank_total,
        'q16_rank_A': rank_A,
        'q16_rank_B': rank_B,
        'q16_rank_C': rank_C,
        'top10': by_total[:10],
        'p_perm_total_density': p_perm,
        'mw5_q14_positive_control': mw5,
        'mw6_q12_negative_control': mw6,
        'verdict': verdict,
        'success_threshold': {'rank_le': 3, 'alpha_bon': 0.0167},
        'all_results': results,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv/Q016-F-01.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Q016-F-01: rank_total={rank_total}/114, density={q16_density:.3f}, p_perm={p_perm:.4f}")
    print(f"  rank_A={rank_A}, rank_B={rank_B}, rank_C={rank_C}")
    print(f"  Q14 (MW-5 positive control) rank: {rank_q14} ({'PASS' if rank_q14<=15 else 'FAIL'})")
    print(f"  Q12 (MW-6 negative control) rank: {rank_q12} ({'PASS' if rank_q12>57 else 'FAIL'})")
    print(f"  VERDICT: {verdict}")


if __name__ == '__main__':
    main()
