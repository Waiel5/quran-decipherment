#!/usr/bin/env python3
"""
Q056-F-05 — Deathbed-hadith verse-citation concentration on Q56:88-94 / 83-96.
SHA-locked pre-reg: 9bae02fa413bb6b3ef9060ea5857dc0ce070a2ac659e6530df62b3d9bee1361a
"""
import json, re, hashlib, os
from collections import Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/preregs/Q056-F-05-deathbed-hadith-concentration-prereg.md'
EXPECTED_SHA = '9bae02fa413bb6b3ef9060ea5857dc0ce070a2ac659e6530df62b3d9bee1361a'
with open(PREREG,'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f'SHA mismatch: {actual}'

# 1) Search 9-book hadiths for Q56-verse citations
books = ['bukhari','muslim','tirmidhi','abudawud','nasai','ibnmajah','malik','ahmed','darimi']
ROOT = '/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books'

# Citation patterns (Arabic + English)
# Looking for "سورة الواقعة آية N" or "[الواقعة: N]" or "(56:N)"
patterns = [
    re.compile(r'سورة الواقعة آية (\d+)'),
    re.compile(r'الواقعة:\s*\[?(\d+)\]?'),
    re.compile(r'\(56[:\s]+(\d+)\)'),
    re.compile(r'al-Waqi[\'`ʿ]ah[^\d]*?(\d+)'),
]

verse_citations = []   # (source, book, idInBook, chapter, verse_num, context, deathbed_flag)
for b in books:
    p = f'{ROOT}/{b}.json'
    with open(p) as f: book = json.load(f)
    for h in book['hadiths']:
        ar = h.get('arabic','') or ''
        en_obj = h.get('english',{}) or {}
        en = (en_obj.get('text','') or '') + ' ' + (en_obj.get('narrator','') or '') if isinstance(en_obj, dict) else en_obj or ''
        text = ar + ' ||| ' + en
        for pat in patterns:
            for m in pat.finditer(text):
                v = int(m.group(1))
                if 1 <= v <= 96:
                    # Check deathbed-context: keywords near match
                    span_start = max(0, m.start()-200)
                    span_end = min(len(text), m.end()+200)
                    context = text[span_start:span_end]
                    deathbed = any(k in context for k in ['موت','وفاة','احتضار','يموت','ميت','المحتضر','death','dying','deathbed','death-bed'])
                    verse_citations.append({'source':'9-book-hadith','book':b,'idInBook':h['idInBook'],
                                            'verse':v,'context_snippet':context[:300], 'deathbed': deathbed})

print(f'9-book hadith Q56 verse-citations: {len(verse_citations)}')
verse_dist = Counter(c['verse'] for c in verse_citations)
print(f'verse distribution: {sorted(verse_dist.items())}')

# 2) Search tafsir Q56 for deathbed-related verse citations
tafs = ['ar-tafsir-al-tabari','ar-tafseer-al-qurtubi','ar-tafsir-ibn-kathir',
        'en-tafsir-maarif-ul-quran','en-tafisr-ibn-kathir','ar-tafsir-al-baghawi',
        'ar-tafsir-al-wasit','en-al-jalalayn']
TAF_ROOT = '/Users/grey/Downloads/quran/data/literature/classical-tafsir/spa5k-tafsir-api'

tafsir_deathbed_verses = []  # which Q56 verses have tafsir-text mentioning death/deathbed
for taf in tafs:
    for vid in range(1, 97):
        p = f'{TAF_ROOT}/{taf}/56/{vid}.json'
        if not os.path.exists(p): continue
        try:
            with open(p) as f: d = json.load(f)
        except: continue
        text = d.get('text','') or ''
        # Deathbed/death-moment keywords
        death_kw = ['موت','احتضار','المحتضر','أحتضر','الحلقوم','يموت','ميت',
                    'death','dying','deathbed','death-bed','death bed',"on his deathbed",'Ibn Mas\'ud','Ibn Masud','Ibn Mas`ud','عبدالله بن مسعود','ابن مسعود']
        # Strong-context: text mentions Ibn Masʿūd OR ḥalqūm OR explicit death
        strong = any(k in text for k in ['Ibn Masud','Ibn Mas\'ud','Ibn Mas`ud','عبدالله بن مسعود','ابن مسعود','الحلقوم','حلقوم','deathbed'])
        if strong:
            tafsir_deathbed_verses.append({'tafsir':taf,'verse':vid,'snippet':text[:200]})

print(f'\nTafsir deathbed-context Q56 verse-citations: {len(tafsir_deathbed_verses)}')
tafsir_verse_dist = Counter(c['verse'] for c in tafsir_deathbed_verses)
print(f'distribution: {sorted(tafsir_verse_dist.items())}')

# Combined density: weight by which verses have deathbed-context tafsir/hadith
combined = Counter()
for c in verse_citations: combined[c['verse']] += 1
for c in tafsir_deathbed_verses: combined[c['verse']] += 1
print(f'\nCombined verse-citation distribution: {sorted(combined.items())}')

# Compute fraction in vv 83-96 (the death-moment-and-thereafter block)
in_block = sum(c for v,c in combined.items() if 83 <= v <= 96)
total = sum(combined.values())
frac = in_block/total if total > 0 else 0.0
print(f'\nVerses 83-96 citations: {in_block}/{total} = {frac:.2%}')

# Same with stricter 88-94 block
in_88_94 = sum(c for v,c in combined.items() if 88 <= v <= 94)
frac_strict = in_88_94/total if total > 0 else 0.0
print(f'Verses 88-94 citations: {in_88_94}/{total} = {frac_strict:.2%}')

verdict = 'VINDICATED' if frac >= 0.50 else 'NULL'
print(f'\nVERDICT: {verdict} (pre-reg: ≥ 50% in vv 83-96)')

result = {
    'test_id': 'Q056-F-05',
    'prereg_sha': EXPECTED_SHA,
    'hadith_citations': verse_citations,
    'hadith_verse_dist': dict(verse_dist),
    'tafsir_deathbed_citations': tafsir_deathbed_verses,
    'tafsir_verse_dist': dict(tafsir_verse_dist),
    'combined_dist': dict(combined),
    'frac_vv_83_96': frac,
    'frac_vv_88_94': frac_strict,
    'in_block_vs_total': f'{in_block}/{total}',
    'verdict': verdict,
}
OUT = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/csv/Q056-F-05.json'
with open(OUT,'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f'Wrote {OUT}')
