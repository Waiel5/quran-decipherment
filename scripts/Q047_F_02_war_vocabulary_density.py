#!/usr/bin/env python3
"""
Q047-F-02 — War-vocabulary density: Q 47 corpus rank.
Pre-reg SHA verified at runtime; fail-fast on mismatch.
Seed: 20260508. Bonferroni-1.
"""
import json, re, hashlib, os, sys
from collections import defaultdict

EXPECTED_SHA = '4b259d1b8a650a08cabe64ae47246ea498ecb49f23179263e18331925f76358e'
PREREG_PATH = '/Users/grey/Downloads/quran/surahs/Q047-muhammad/Q047-F-02-war-vocabulary-density-prereg.md'
QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q047-muhammad/csv/Q047-F-02.json'

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

    war_categories = {
        'qitāl': ['قتل', 'قتال', 'قاتل', 'قاتلوا', 'قتلوا', 'يقاتل', 'يقاتلون', 'يقتل', 'القتال',
                   'قاتلتموهم', 'قاتلوهم', 'قتلتم', 'قاتلوكم', 'يقاتلونكم', 'فقاتلوا', 'فقتلوا', 'مقتل', 'قتلى'],
        'jihād': ['جهاد', 'جاهد', 'جاهدوا', 'يجاهد', 'يجاهدون', 'مجاهد', 'مجاهدون', 'المجاهدين', 'جاهدا',
                  'جاهدوهم', 'مجاهدا', 'الجهاد'],
        'riqāb': ['رقاب', 'الرقاب', 'رقابكم', 'رقبة'],
        'asr': ['أسر', 'أسرى', 'أسارى', 'أسر', 'الأسرى'],
        'fidāʾ': ['فدا', 'فداء', 'فدية', 'فدوا', 'فديناه'],
        'ḥarb': ['حرب', 'الحرب'],
        'kuffār_combatant': ['كفار', 'الكفار', 'كفروا', 'الذين كفروا'],  # Note: "الذين كفروا" is bigram; handle separately
        'wathāq': ['وثاق', 'الوثاق'],
        'darb_riqāb': ['ضرب', 'فضرب', 'اضربوا', 'فاضربوا'],  # the "strike" verb
    }

    # Flatten unigram set; bigrams handled via substring
    unigram_set = set()
    bigrams = []
    for cat, alts in war_categories.items():
        for w in alts:
            if ' ' in w:
                bigrams.append(w)
            else:
                unigram_set.add(w)

    # For each surah compute density
    per_surah = []
    for s in range(1, 115):
        full_text = ' '.join(clean(v['text']) for v in q[s-1]['verses'])
        words = full_text.split()
        n = len(words) or 1
        unigram_hits = sum(1 for w in words if w in unigram_set)
        bigram_hits = sum(full_text.count(b) for b in bigrams)
        total = unigram_hits + bigram_hits
        rate = total / n * 100
        per_surah.append({
            'surah': s,
            'words': n,
            'unigram_hits': unigram_hits,
            'bigram_hits': bigram_hits,
            'total': total,
            'rate_per_100w': rate,
        })

    sorted_desc = sorted(per_surah, key=lambda x: -x['rate_per_100w'])
    rank_47 = next(i+1 for i,e in enumerate(sorted_desc) if e['surah']==47)

    if rank_47 <= 3:
        verdict = 'VINDICATED'
    elif rank_47 <= 5:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'test_id': 'Q047-F-02',
        'pre_reg_sha': EXPECTED_SHA,
        'seed': 20260508,
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'war_categories': list(war_categories.keys()),
        'Q47_record': next(e for e in per_surah if e['surah']==47),
        'Q47_rank': rank_47,
        'top_10_war_density': [{'surah': e['surah'], 'rate_per_100w': round(e['rate_per_100w'],3),
                                'total_hits': e['total'], 'words': e['words']} for e in sorted_desc[:10]],
        'verdict': verdict,
        'bonferroni_k': 1,
        'alpha_bon': 0.05,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'Q047-F-02 verdict: {verdict}')
    print(f'  Q47 war-vocabulary rate: {next(e for e in per_surah if e["surah"]==47)["rate_per_100w"]:.3f} per-100-words')
    print(f'  Q47 rank: {rank_47}/114')
    print(f'  Top 5: {[(e["surah"], round(e["rate_per_100w"],2)) for e in sorted_desc[:5]]}')

if __name__ == '__main__':
    main()
