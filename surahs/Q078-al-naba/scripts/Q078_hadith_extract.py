#!/usr/bin/env python3
"""
Q078 hadith-citation extractor (descriptive; no pre-reg).

Extracts hadith-text matches against Q 78 verse-text snippets in
`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/*.json`.

Output: csv/hadith-citations.json — descriptive listing of partial-match
hadith with their idInBook identifiers.

Note: this is descriptive (no pre-reg), supporting `04-hadith-corpus.md`
documentation. For SHA-locked tests, see Q078_F_01 through Q078_F_05.

Seed: 20260509 (no random element).
"""

import json
import re
import os
import glob

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
QURAN_PATH = os.path.join(PROJECT_ROOT, 'quran-text', 'quran-no-tashkeel.json')
HADITH_GLOB = os.path.join(PROJECT_ROOT, 'data', 'literature', 'hadith',
                           'ahmedbaset-json', 'db', 'by_book', 'the_9_books',
                           '*.json')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv',
                           'hadith-citations.json')


def normalize_arabic(s):
    """Strip tashkeel + unify hamza-variants + final-yāʾ."""
    s = re.sub(r'[ً-ٰٟـ]', '', s)  # tashkeel + tatweel
    s = re.sub(r'[إأآ]', 'ا', s)
    s = re.sub(r'ى', 'ي', s)
    s = re.sub(r'ة', 'ه', s)
    return s


def main():
    with open(QURAN_PATH) as f:
        quran = json.load(f)
    q78 = next(s for s in quran if s['id'] == 78)

    # Q 78 verse-text snippets (≥3 words for matching)
    snippets = []
    for v in q78['verses']:
        words = v['text'].split()
        for i in range(len(words) - 2):
            snippet = ' '.join(words[i:i+3])
            snippets.append({
                "verse_id": v['id'],
                "snippet": snippet,
                "snippet_normalized": normalize_arabic(snippet),
            })

    # Try to load hadith JSON files; if path doesn't exist, return empty
    hadith_files = sorted(glob.glob(HADITH_GLOB))
    if not hadith_files:
        result = {
            "test_id": "Q078-hadith-extract",
            "snippets_count": len(snippets),
            "hadith_files_found": 0,
            "matches": [],
            "note": "Hadith data path not present at expected location; skip-only mode.",
        }
    else:
        all_matches = []
        seen_ids = set()
        for hf in hadith_files:
            try:
                with open(hf, encoding='utf-8') as f:
                    book_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                continue
            book_name = os.path.basename(hf).replace('.json', '')
            # Try common JSON shapes
            entries = []
            if isinstance(book_data, list):
                entries = book_data
            elif isinstance(book_data, dict):
                if 'hadiths' in book_data:
                    entries = book_data['hadiths']
                elif 'data' in book_data:
                    entries = book_data['data']
            for h in entries[:5000]:  # cap to avoid runtime blowup
                if not isinstance(h, dict):
                    continue
                arabic_text = h.get('arabic') or h.get('matn') or h.get('hadithText') or h.get('text', '')
                if not arabic_text or not isinstance(arabic_text, str):
                    continue
                norm = normalize_arabic(arabic_text)
                for sn in snippets:
                    if sn['snippet_normalized'] in norm:
                        idInBook = h.get('idInBook') or h.get('id') or '?'
                        key = (book_name, idInBook, sn['verse_id'])
                        if key in seen_ids:
                            continue
                        seen_ids.add(key)
                        all_matches.append({
                            "book": book_name,
                            "idInBook": idInBook,
                            "q78_verse": sn['verse_id'],
                            "snippet": sn['snippet'],
                        })
                        if len(all_matches) >= 200:
                            break
                if len(all_matches) >= 200:
                    break
            if len(all_matches) >= 200:
                break

        result = {
            "test_id": "Q078-hadith-extract",
            "snippets_count": len(snippets),
            "hadith_files_found": len(hadith_files),
            "match_count": len(all_matches),
            "matches": all_matches[:50],  # first 50
            "note": "Descriptive partial-match scan; not SHA-locked test.",
        }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Snippets generated: {len(snippets)}")
    print(f"Hadith files found: {result.get('hadith_files_found', 0)}")
    print(f"Match count: {result.get('match_count', 0)}")
    print(f"Output: {OUTPUT_PATH}")


if __name__ == '__main__':
    main()
