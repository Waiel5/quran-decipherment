#!/usr/bin/env python3
"""Scan all 9 hadith books for Q10 / Yūnus / surat-yūnus references.

Heuristics: Arabic match patterns include `سورة يونس`, `يونس بن متى`, `قوم يونس`,
`أولياء الله لا خوف`, plus verse-fragment matches for major Q10 verses (62, 98, 101).
Output JSON: {book: [{id, idInBook, snippet, match_type}]}.
"""
import json, os, re

DB = '/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books'
OUT = '/Users/grey/Downloads/quran/surahs/Q010-yunus/csv/Q010-hadith-scan.json'

BOOKS = ['bukhari', 'muslim', 'abudawud', 'tirmidhi', 'nasai', 'ibnmajah', 'malik', 'ahmed', 'darimi']

# Arabic patterns
PATS = [
    ('SURAT_YUNUS', re.compile(r'سورة\s+يونس|سُورَة\s+يُونُس')),
    ('YUNUS_BIN_MATTA', re.compile(r'يونس\s+بن\s+متى|يُونُس\s+بْن\s+مَتَّى|يُونُسَ\s+بْنِ\s+مَتَّى')),
    ('QAWM_YUNUS', re.compile(r'قوم\s+يونس|قَوْم\s+يُونُس')),
    ('AWLIYA_VERSE', re.compile(r'أولياء\s+الله\s+لا\s+خوف|أَوْلِيَاءَ\s+اللَّهِ\s+لَا\s+خَوْفٌ')),
    ('Q10_98_QARYA', re.compile(r'إلا قوم يونس|إِلَّا قَوْمَ يُونُس')),
    ('Q10_101_UNZURU', re.compile(r'انظروا\s+ماذا\s+في\s+السماوات|انْظُرُوا مَاذَا فِي السَّمَوَات')),
    ('Q10_OPENING_ALR', re.compile(r'الر\s+تلك\s+آيات\s+الكتاب\s+الحكيم|الر تلك آيَات الْكتاب الْحَكِيم')),
    ('YUNUS_ENGLISH', re.compile(r'\bSurat\s+Yunus\b|\bSurah\s+Yunus\b|\bYunus\b', re.IGNORECASE)),
    ('JONAH_ENGLISH', re.compile(r'\bJonah\b|\bson\s+of\s+Matta\b', re.IGNORECASE)),
]

def scan(book):
    fp = os.path.join(DB, book + '.json')
    with open(fp) as f: data = json.load(f)
    hits = []
    for h in data.get('hadiths', []):
        ar = h.get('arabic', '') or ''
        en_raw = h.get('english', '') or ''
        if isinstance(en_raw, dict):
            en = (en_raw.get('text') or '') + ' ' + (en_raw.get('narrator') or '')
        else:
            en = en_raw
        if not isinstance(ar, str): ar = ''
        if not isinstance(en, str): en = ''
        for tag, pat in PATS:
            m = pat.search(ar) or pat.search(en)
            if m:
                # snippet around match (Arabic preferred)
                src = ar if pat.search(ar) else en
                start = max(0, m.start() - 50)
                end = min(len(src), m.end() + 80)
                snippet = src[start:end].replace('\n', ' ')
                hits.append({
                    'id': h.get('id'),
                    'idInBook': h.get('idInBook'),
                    'chapterId': h.get('chapterId'),
                    'bookId': h.get('bookId'),
                    'match': tag,
                    'snippet': snippet,
                })
                break  # one match per hadith
    return hits


def main():
    out = {}
    for b in BOOKS:
        try:
            out[b] = scan(b)
            print(f'{b}: {len(out[b])} hits')
        except FileNotFoundError as e:
            print(f'  MISSING: {b}')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'\nWrote {OUT}')


if __name__ == '__main__':
    main()
