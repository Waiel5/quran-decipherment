#!/usr/bin/env python3
"""Q073-F-05 — Q 73:20 "the long verse" corpus-rank distinction within Early-Meccan / non-muq surahs.

Pre-reg: surahs/Q073-al-muzzammil/Q073-F-05-long-verse-rank-prereg.md
Pre-reg SHA256: 5938f7820ed051c8c805206469264f18fd80234ebdbab3f8d69b2ce58f8d3b0b
Rules-tuple: (no-tashkeel, whitespace tokenization, basmala-counted-only-in-Q1, Hafs-Kufan)
"""
import json, hashlib, sys, os, csv

PREREG = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/Q073-F-05-long-verse-rank-prereg.md'
EXPECTED_SHA = '5938f7820ed051c8c805206469264f18fd80234ebdbab3f8d69b2ce58f8d3b0b'

QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
NOLDEKE_CSV = '/Users/grey/Downloads/quran/data/revelation-order.csv'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/csv/Q073-F-05.json'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()

    quran = json.load(open(QURAN_PATH))

    # Build verse list with word counts
    verses = []
    for s in quran:
        for v in s['verses']:
            wc = len(v['text'].split())
            cc = len(v['text'])
            verses.append({'sid': s['id'], 'aid': v['id'], 'text': v['text'], 'word_count': wc, 'char_count': cc})

    # Sort by word_count descending
    verses_sorted = sorted(verses, key=lambda x: -x['word_count'])
    rank_map = {(v['sid'], v['aid']): i+1 for i, v in enumerate(verses_sorted)}

    # Q 73:20
    q73_20 = next(v for v in verses if v['sid']==73 and v['aid']==20)
    corpus_rank = rank_map[(73, 20)]
    h1a_pass = (corpus_rank <= 25)

    # Top-25 corpus
    top25 = [{'sid': v['sid'], 'aid': v['aid'], 'word_count': v['word_count'], 'char_count': v['char_count'], 'rank': rank_map[(v['sid'], v['aid'])]} for v in verses_sorted[:25]]

    # === Early-Meccan filter ===
    early_meccan_surahs = set()
    with open(NOLDEKE_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('noldeke_phase', '').strip().lower() == 'early meccan':
                early_meccan_surahs.add(int(row['mushaf_order']))

    em_verses = [v for v in verses if v['sid'] in early_meccan_surahs]
    em_sorted = sorted(em_verses, key=lambda x: -x['word_count'])
    em_rank = next((i+1 for i, v in enumerate(em_sorted) if v['sid']==73 and v['aid']==20), None)
    h1b_pass = (em_rank == 1)

    em_top10 = [{'sid': v['sid'], 'aid': v['aid'], 'word_count': v['word_count']} for v in em_sorted[:10]]

    # === Verdict ===
    n_pass = (1 if h1a_pass else 0) + (1 if h1b_pass else 0)
    if n_pass == 2:
        verdict = "CONFIRMED"
    elif n_pass == 1:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    # Pre-commit-violation check: verse below median?
    median_wc = sorted([v['word_count'] for v in verses])[len(verses)//2]
    if q73_20['word_count'] < median_wc:
        verdict = "PRE-COMMIT-VIOLATION (below median word-count — direction-reversed)"

    out = {
        "test_id": "Q073-F-05",
        "prereg_sha": EXPECTED_SHA,
        "Q73_20_word_count": q73_20['word_count'],
        "Q73_20_char_count": q73_20['char_count'],
        "corpus_total_verses": len(verses),
        "corpus_rank_descending": corpus_rank,
        "h1a_top25_pass": h1a_pass,
        "early_meccan_surah_count": len(early_meccan_surahs),
        "early_meccan_verse_count": len(em_verses),
        "early_meccan_rank": em_rank,
        "h1b_em_max_pass": h1b_pass,
        "top25_corpus": top25,
        "top10_early_meccan": em_top10,
        "median_word_count_corpus": median_wc,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Verdict: {verdict}")
    print(f"  Q 73:20 word_count = {q73_20['word_count']}, char_count = {q73_20['char_count']}")
    print(f"  H1a: corpus_rank = {corpus_rank} / {len(verses)}; pass top-25 = {h1a_pass}")
    print(f"  H1b: early-meccan rank = {em_rank} / {len(em_verses)} verses; pass max-1 = {h1b_pass}")
    print(f"  Top-5 corpus: {[(t['sid'], t['aid'], t['word_count']) for t in top25[:5]]}")
    print(f"  Top-5 early-Meccan: {[(t['sid'], t['aid'], t['word_count']) for t in em_top10[:5]]}")
    print(f"Written to: {OUT_PATH}")


if __name__ == '__main__':
    main()
