#!/usr/bin/env python3
"""Q035-F-03 — Q 35 v.1 corpus-unique al-mala'ika opener test.

Pre-reg: surahs/Q035-fatir/preregs/Q035-F-03-malaika-opener-prereg.md
Pre-reg SHA256: 633ab39e30121d42cdd5626b49d9805414ffc6580e5fe191de7e6ff3f09d528a
Rules-tuple: (no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, mashriqi)

H1: n_v1_surface = 1 (only Q35's v.1 contains explicit al-mala'ika surface form).
H1b: n_v1_lemma = 1 (only Q35's v.1 contains QAC LEM:malak).
Bonferroni k=2, alpha_bon=0.025.
"""
import json, hashlib, sys, os, re

PREREG = '/Users/grey/Downloads/quran/surahs/Q035-fatir/preregs/Q035-F-03-malaika-opener-prereg.md'
EXPECTED_SHA = '633ab39e30121d42cdd5626b49d9805414ffc6580e5fe191de7e6ff3f09d528a'
SEED = 20260509
ALPHA_BON = 0.05 / 2


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
        qtxt = json.load(f)

    # Surface form: الملائكة or ملائكة
    pat_malaika = re.compile(r'الملائكة|ملائكة')

    matching_surface_v1 = []
    for s_obj in qtxt:
        s = int(s_obj['id'])
        v1 = s_obj['verses'][0]['text']
        if pat_malaika.search(v1):
            matching_surface_v1.append({'surah': s, 'v1_text': v1})

    n_v1_surface = len(matching_surface_v1)
    h1_pass = n_v1_surface == 1 and matching_surface_v1[0]['surah'] == 35

    # Lemma test: scan QAC for LEM:malak at v.1 of each surah
    matching_lemma_v1 = []
    with open('/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt') as f:
        for line in f:
            if 'LEM:malak' not in line:
                continue
            m = re.match(r'^\((\d+):(\d+):', line)
            if m:
                s, v = int(m.group(1)), int(m.group(2))
                if v == 1:
                    matching_lemma_v1.append({'surah': s, 'qac_line': line.strip()[:200]})

    surahs_with_lemma_v1 = sorted(set(e['surah'] for e in matching_lemma_v1))
    n_v1_lemma = len(surahs_with_lemma_v1)
    h1b_pass = n_v1_lemma == 1 and surahs_with_lemma_v1 == [35]

    n_pass = sum([h1_pass, h1b_pass])
    if n_pass == 2: verdict = 'CONFIRMED'
    elif n_pass == 1: verdict = 'DIRECTIONAL'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q035-F-03',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, mashriqi)',
        'seed': SEED,
        'alpha_bon': ALPHA_BON,
        'h1_surface_v1': {
            'n_matching': n_v1_surface,
            'matches': matching_surface_v1,
            'pass': h1_pass,
        },
        'h1b_lemma_v1': {
            'n_matching_surahs': n_v1_lemma,
            'surahs': surahs_with_lemma_v1,
            'lemma_lines': matching_lemma_v1,
            'pass': h1b_pass,
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'Test is deterministic counting. Pre-flight observed only Q35 v.1 has explicit al-malaika.',
    }

    print('=== Q035-F-03 mala\'ika v.1 opener uniqueness ===')
    print(f'H1 surface: n={n_v1_surface}; pass={h1_pass}')
    for m in matching_surface_v1:
        print(f'  Q {m["surah"]}: {m["v1_text"][:120]}...')
    print(f'H1b lemma: n_surahs={n_v1_lemma}; surahs={surahs_with_lemma_v1}; pass={h1b_pass}')
    print(f'\nN pass: {n_pass}/2 -> {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv/Q035-F-03.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
