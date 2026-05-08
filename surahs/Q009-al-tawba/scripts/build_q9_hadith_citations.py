#!/usr/bin/env python3
"""Build a Q9 hadith-citation index from ahmedbaset-json.

Strategy: scan English narrator+text for explicit Q9 verse references
(e.g. "Sura 9", "Tawba", "Bara'a", verse keywords like "Tabuk",
"Hypocrites", "the Three who stayed behind", "Hud, has aged me").

Outputs a citations file at data/literature/hadith/Q009-citations.md.
"""
import json
import re
from pathlib import Path

HADITH_DIR = Path('/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books')
OUT_FILE = Path('/Users/grey/Downloads/quran/data/literature/hadith/Q009-citations.md')

BOOK_NAMES = {
    'bukhari': 'Sahih al-Bukhari',
    'muslim': 'Sahih Muslim',
    'tirmidhi': 'Jami al-Tirmidhi',
    'abudawud': 'Sunan Abu Dawud',
    'nasai': 'Sunan al-Nasai',
    'ibnmajah': 'Sunan Ibn Majah',
    'malik': "Muwatta' Malik",
    'ahmed': 'Musnad Ahmad',
    'darimi': 'Sunan al-Darimi',
}

# Search terms (English):
# - explicit surah refs ("Sura 9", "Surat al-Tawba", "Bara'a", "Tauba", etc.)
# - Q9-distinctive content: Tabuk expedition; the three who stayed behind
#   (Ka'b ibn Malik, Hilal ibn Umayya, Murara b. al-Rabi); ila' al-nisa'
#   pertaining to Tabuk; Bara'a proclamation by 'Ali; Q 9:36 four sacred months;
#   Q 9:60 zakat distribution; Q 9:103 charity from wealth; Q 9:128 closing.
# Quote fragments are recognizable English renderings of Q9 verses.

EN_PATTERNS = [
    # Surah-name variants
    (r'\bSurat? al[- ]Tawb', 'name:al-Tawba'),
    (r'\bSurat? Bara\W', 'name:Bara\'a'),
    (r"Sura(t)?(h)? 9\b", 'name:Sura 9'),
    (r'\bAt-?Tawbah\b', 'name:al-Tawba'),
    (r'\bAt-?Tauba\b', 'name:al-Tawba'),
    # Tabuk expedition (the Q9 setting)
    (r'\bTabuk\b', 'tabuk'),
    (r'\bTabouk\b', 'tabuk'),
    # Three who stayed behind
    (r'Ka\'?ab\s+(b\.|bin|ibn)\s*Malik', 'kab-malik'),
    (r'three\s+who\s+(were\s+)?(stayed|remained|left|forsaken)', 'three-stayed'),
    (r"three\s+who\s+had\s+stayed\s+behind", 'three-stayed'),
    # Q9-distinctive verse fragments (English renderings)
    (r'no shelter from Allah except in Him', 'q9-118'),
    (r"no place of refuge from Allah except in Him", 'q9-118'),
    (r'There has come to you a Messenger from amongst yourselves', 'q9-128'),
    (r'a Messenger.{0,30}from yourselves.{0,30}grievous to him', 'q9-128'),
    (r'Hud and its sisters', 'q9-context'),
    (r'(Bara|Bera|Para)at\b', 'name:Bara\'a'),
    (r'\bal[- ]Faadihah\b', 'name:al-Faḍiḥa'),
    # Verse-by-verse English fragments
    (r'four months', 'q9-2-or-36'),
    (r'four (forbidden|sacred) months', 'q9-36'),
    (r"the day of the greatest pilgrimage", 'q9-3'),
    (r'\bjizya\b', 'q9-29'),
    (r'no Verse was revealed for some time after that', 'q9-context'),
    # Verse-fragment proclamation by Ali on Hajj
    (r'(Abu Bakr.+Hajj.+Bara|Bara.+Abu Bakr.+Hajj)', 'q9-3-proclamation'),
    (r"\bAli.+(proclaim|declare|announce).+(Bara|Tawba|repent)", 'q9-3-proclamation'),
    # asbab last revelation
    (r'last (verse|chapter|Sura)', 'last-revealed'),
    (r'last (Aya|Ayah|āyah)', 'last-revealed'),
    # Q9:60 zakat-categories
    (r'(eight categories|categories of zakat|categories of Sadaqa)', 'q9-60'),
]

def main():
    rows = []
    for short, longn in BOOK_NAMES.items():
        path = HADITH_DIR / f'{short}.json'
        if not path.exists():
            continue
        try:
            d = json.loads(path.read_text(encoding='utf-8'))
        except Exception as e:
            print(f'skip {short}: {e}')
            continue
        hadiths = d.get('hadiths') or d.get('hadith') or d
        if not isinstance(hadiths, list):
            continue
        # build chapter id -> name
        chapters = {c['id']: c.get('english', '') if isinstance(c, dict) else '' for c in d.get('chapters', [])}
        for h in hadiths:
            en = h.get('english', {})
            if isinstance(en, dict):
                text = (en.get('narrator', '') + ' ' + en.get('text', ''))
            else:
                text = str(en)
            tags = []
            for pat, tag in EN_PATTERNS:
                if re.search(pat, text, re.IGNORECASE):
                    tags.append(tag)
            if tags:
                ar = h.get('arabic', '')
                idInBook = h.get('idInBook')
                gid = h.get('id')
                ch = h.get('chapterId')
                ch_name = chapters.get(ch, '')
                rows.append({
                    'book_short': short,
                    'book_name': longn,
                    'idInBook': idInBook,
                    'global_id': gid,
                    'chapterId': ch,
                    'chapter': ch_name if isinstance(ch_name, dict) else (ch_name or ''),
                    'tags': sorted(set(tags)),
                    'narrator': en.get('narrator', '') if isinstance(en, dict) else '',
                    'text': en.get('text', '') if isinstance(en, dict) else str(en),
                    'arabic': ar[:600] if isinstance(ar, str) else str(ar)[:600],
                })

    # write Markdown
    counts = {}
    for r in rows:
        counts[r['book_name']] = counts.get(r['book_name'], 0) + 1
    md = []
    md.append(f'# Q 9 al-Tawba — Hadith Citation Index (auto-built)')
    md.append('')
    md.append(f'Source: scan of `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/`')
    md.append(f'')
    md.append(f'Hits per book:')
    md.append(f'')
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        md.append(f'- {k}: {v}')
    md.append(f'')
    md.append(f'Total: {len(rows)}')
    md.append(f'')
    md.append('---')
    md.append('')
    by_book = {}
    for r in rows:
        by_book.setdefault(r['book_name'], []).append(r)
    for book in sorted(by_book.keys()):
        md.append(f'## {book}')
        md.append('')
        for r in by_book[book]:
            md.append(f"### #{r['idInBook']} (global #{r['global_id']}) — {', '.join(r['tags'])}")
            ch = r['chapter']
            if isinstance(ch, dict):
                ch = ch.get('english', '') or ch.get('arabic', '')
            md.append(f"- Chapter: {ch}")
            md.append(f"- Narrator: {r['narrator']}")
            md.append(f"- Text: {r['text'][:1200]}")
            md.append(f"- Arabic (truncated): {r['arabic']}")
            md.append('')
        md.append('---')
        md.append('')
    OUT_FILE.write_text('\n'.join(md), encoding='utf-8')
    print(f'wrote {OUT_FILE}: {len(rows)} hits across {len(by_book)} books')

if __name__ == '__main__':
    main()
