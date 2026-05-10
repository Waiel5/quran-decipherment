#!/usr/bin/env python3
"""Q035-F-02 — Q 35:32 3-fold hierarchy {zalim li-nafsih, muqtasid, sabiq bi-l-khayrat} corpus-uniqueness test.

Pre-reg: surahs/Q035-fatir/preregs/Q035-F-02-3fold-hierarchy-prereg.md
Pre-reg SHA256: 6bde59963d13dd2b766d3ee52f0849f4af64a20ef94602abf8845fe5fc8790fa
Rules-tuple: (no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

H1a: N_verse = 1 (only Q 35:32 contains all three terms).
H1b: N_surah = 1 (only Q 35 contains all three terms across its verses).
Bonferroni k=2, alpha_bon=0.025.
"""
import json, hashlib, sys, os, re

PREREG = '/Users/grey/Downloads/quran/surahs/Q035-fatir/preregs/Q035-F-02-3fold-hierarchy-prereg.md'
EXPECTED_SHA = '6bde59963d13dd2b766d3ee52f0849f4af64a20ef94602abf8845fe5fc8790fa'
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
    # qtxt is list of dicts with keys {id, name, ..., verses: [{id, text}, ...]}

    pat_zalim = re.compile(r'ظالم')
    pat_nafsih = re.compile(r'نفسه|لنفسه')
    pat_muqtasid = re.compile(r'مقتصد')
    pat_sabiq = re.compile(r'سابق')
    pat_khayrat = re.compile(r'الخيرات|خيرات')

    verses_with_all_three = []
    surahs_with_all_three = {}

    for s_obj in qtxt:
        s = int(s_obj['id'])
        verses = s_obj['verses']
        surah_terms = {'zalim_nafsih': [], 'muqtasid': [], 'sabiq_khayrat': []}
        for v_obj in verses:
            v = int(v_obj['id'])
            text = v_obj['text']
            t1 = bool(pat_zalim.search(text) and pat_nafsih.search(text))
            t2 = bool(pat_muqtasid.search(text))
            t3 = bool(pat_sabiq.search(text) and pat_khayrat.search(text))
            if t1 and t2 and t3:
                verses_with_all_three.append({'surah': s, 'verse': v, 'text': text})
            if t1: surah_terms['zalim_nafsih'].append(v)
            if t2: surah_terms['muqtasid'].append(v)
            if t3: surah_terms['sabiq_khayrat'].append(v)
        if surah_terms['zalim_nafsih'] and surah_terms['muqtasid'] and surah_terms['sabiq_khayrat']:
            surahs_with_all_three[s] = surah_terms

    n_verse = len(verses_with_all_three)
    n_surah = len(surahs_with_all_three)
    h1a_pass = n_verse == 1
    h1b_pass = n_surah == 1

    n_pass = sum([h1a_pass, h1b_pass])
    if n_pass == 2: verdict = 'CONFIRMED'
    elif n_pass == 1: verdict = 'DIRECTIONAL'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q035-F-02',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'seed': SEED,
        'alpha_bon': ALPHA_BON,
        'h1a_verse_uniqueness': {
            'n_verses_with_all_three': n_verse,
            'verses': verses_with_all_three,
            'pass': h1a_pass,
        },
        'h1b_surah_uniqueness': {
            'n_surahs_with_all_three': n_surah,
            'surahs': {str(s): t for s, t in surahs_with_all_three.items()},
            'pass': h1b_pass,
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'Pre-flight observed Q 35:32 is the SOLE verse with all 3 terms. PASS-DIRECTED status pre-locked given empirical-anchor disclosure. Result deterministic.',
    }

    print('=== Q035-F-02 3-fold hierarchy uniqueness ===')
    print(f'H1a: verses with all 3 terms = {n_verse}')
    for v in verses_with_all_three:
        print(f'  Q {v["surah"]}:{v["verse"]} -> {v["text"][:100]}...')
    print(f'   pass={h1a_pass}')
    print(f'H1b: surahs with all 3 terms = {n_surah}')
    for s in surahs_with_all_three:
        print(f'  Q {s}')
    print(f'   pass={h1b_pass}')
    print(f'\nN pass: {n_pass}/2 -> {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv/Q035-F-02.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
