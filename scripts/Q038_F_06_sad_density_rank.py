#!/usr/bin/env python3
"""Q038-F-06 — ص-letter density rank for Q 38 among 60-100-verse surahs (mid-length band).

Pre-reg: surahs/Q038-sad/Q038-F-06-sad-density-rank-prereg.md
Pre-reg SHA256: 06dd2010ce39314f07404cb5cb53cb9d22f5135a9566265df8a63f580735fa48
Rules-tuple: (no-tashkeel, character-graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q038-sad/Q038-F-06-sad-density-rank-prereg.md'
EXPECTED_SHA = '06dd2010ce39314f07404cb5cb53cb9d22f5135a9566265df8a63f580735fa48'
SEED = 20260509

MUQ_TOKENS = set(['الم', 'الر', 'المر', 'المص', 'كهيعص', 'طه', 'طسم', 'طس', 'يس',
                  'حم', 'عسق', 'ص', 'ق', 'ن'])
NON_LETTERS = set('۞۩ۭۚۖۗۘۙۜۤ ')


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def strip_muq_body(verses):
    txts = []
    for i, v in enumerate(verses):
        text = v['text']
        for sep in '۞۩ۭۚۖۗۘۙۜۤ':
            text = text.replace(sep, ' ')
        toks = text.split()
        if i == 0 and toks and toks[0] in MUQ_TOKENS:
            toks = toks[1:]
        txts.append(' '.join(toks))
    body = ' '.join(txts)
    return ''.join(ch for ch in body if ch not in NON_LETTERS)


def main():
    verify_sha()

    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    LETTER = 'ص'

    rows = []
    for s in quran:
        n_verses = len(s['verses'])
        body = strip_muq_body(s['verses'])
        n_body = len(body)
        cnt = body.count(LETTER)
        rate = cnt / n_body if n_body else 0.0
        rows.append({
            'surah': s['id'],
            'name': s.get('transliteration', ''),
            'n_verses': n_verses,
            'n_body_letters': n_body,
            'count_sad': cnt,
            'rate_sad': rate,
        })

    # Mid-length band [60, 100]
    band = [r for r in rows if 60 <= r['n_verses'] <= 100]
    band_sorted = sorted(band, key=lambda r: (-r['rate_sad'], -r['count_sad']))

    rank_q38 = next(i+1 for i, r in enumerate(band_sorted) if r['surah'] == 38)
    q38_row = next(r for r in band if r['surah'] == 38)
    band_size = len(band)

    # Significance under a permutation null: degenerate for fixed surah-rates;
    # report rank-based exceedance probability under uniform random selection.
    p_naive = rank_q38 / band_size

    # Full-corpus rank as well
    all_sorted = sorted(rows, key=lambda r: (-r['rate_sad'], -r['count_sad']))
    full_rank_q38 = next(i+1 for i, r in enumerate(all_sorted) if r['surah'] == 38)

    if rank_q38 == 1:
        verdict = 'CONFIRMED'
    elif rank_q38 <= 3:
        verdict = 'DIRECTIONAL'
    elif rank_q38 > band_size / 2:
        verdict = 'PRE-COMMIT-VIOLATION'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q038-F-06',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': '(no-tashkeel, character-graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'letter': LETTER,
        'band_definition': '60 <= n_verses <= 100',
        'band_size': band_size,
        'q38': q38_row,
        'rank_q38_in_band': rank_q38,
        'rank_q38_full_corpus': full_rank_q38,
        'p_naive_uniform_band': p_naive,
        'band_top10': [{'surah': r['surah'], 'name': r['name'], 'n_verses': r['n_verses'],
                        'rate_sad_pct': r['rate_sad']*100, 'count_sad': r['count_sad']}
                       for r in band_sorted[:10]],
        'verdict': verdict,
    }

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q038-sad/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q038-sad/csv/Q038-F-06.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Band [60,100] size: {band_size}")
    print(f"Q 38 ص-density: {q38_row['rate_sad']*100:.3f}% ({q38_row['count_sad']} ص / {q38_row['n_body_letters']} letters)")
    print(f"Q 38 rank in band: {rank_q38}/{band_size}")
    print(f"Q 38 rank in full corpus: {full_rank_q38}/114")
    print(f"\nBand top-10 by ص-density:")
    for i, r in enumerate(band_sorted[:10]):
        marker = ' <-- Q 38' if r['surah'] == 38 else ''
        print(f"  {i+1:2d}. Q {r['surah']:3d} {r['name']:<20s} n_v={r['n_verses']:3d} rate={r['rate_sad']*100:.3f}% (cnt={r['count_sad']}){marker}")
    print(f"\nVerdict: {verdict}")


if __name__ == '__main__':
    main()
