#!/usr/bin/env python3
"""
Q055-F-03 — Cosmic-vocabulary density audit.

Hypothesis: Q 55 is the corpus's most "cosmic" surah (per classical
'creation-as-mercy' theme). Cosmic-token set: samāʾ (sky), arḍ (earth),
shams (sun), qamar (moon), najm (star), baḥr (sea).

Direction-locked: Q 55 ranks corpus-top-3 in cosmic-density per 100 words.
Method: count word-stem matches for each lemma's surface forms in
no-tashkeel; density = matches / total_words * 100.
Bonferroni: family of 6 lemmas → α = 0.05/6 = 0.0083.
"""
import json, os, re, unicodedata, statistics
from collections import Counter

ROOT = '/Users/grey/Downloads/quran'
OUT = os.path.join(ROOT, 'surahs/Q055-al-rahman/csv/Q055-F-03.json')


def strip_diacritics(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def normalize_alif(s):
    s = re.sub(r'[إأآٱ]', 'ا', s)
    s = re.sub(r'ءا', 'ا', s)
    s = re.sub(r'ى', 'ي', s)
    return s


# Cosmic vocabulary: surface forms (in no-tashkeel) for each lemma
# We match word-as-substring (with prefix tolerance for ال, و, ف, ب, ل)
COSMIC = {
    'samaa': [r'سما', r'سماو'],            # سماء، السماء، سماوات
    'ard':   [r'ارض'],                       # ارض، الارض
    'shams': [r'شمس'],                       # شمس، الشمس
    'qamar': [r'قمر'],                       # قمر، القمر
    'najm':  [r'نجم'],                       # نجم، النجوم، نجوم
    'bahr':  [r'بحر', r'بحري'],              # بحر، البحر، البحرين، بحران
}


def normalize_text(text):
    n = strip_diacritics(text)
    return normalize_alif(n)


def count_cosmic(text):
    n = normalize_text(text)
    tokens = n.split()
    counts = {k: 0 for k in COSMIC}
    for t in tokens:
        # strip leading conjunctive prefixes then article (iteratively)
        stripped = t
        # remove و / ف / ب / ل prefix once
        m = re.match(r'^(و|ف|ب|ل|ك)', stripped)
        if m:
            stripped = stripped[len(m.group(1)):]
        # remove ال article
        if stripped.startswith('ال'):
            stripped = stripped[2:]
        for lemma, patterns in COSMIC.items():
            for p in patterns:
                if stripped.startswith(p) and len(stripped) <= len(p) + 4:
                    counts[lemma] += 1
                    break
            else:
                continue
            break
    return counts, len(tokens)


def main():
    print("=== Q055-F-03: Cosmic vocabulary density ===\n")
    out = {'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, Hafs-Kufan)',
           'cosmic_tokens': list(COSMIC.keys())}

    path = os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')
    with open(path) as f:
        data = json.load(f)

    rows = []
    for s in data:
        all_text = ' '.join(v['text'] for v in s['verses'])
        counts, words = count_cosmic(all_text)
        total = sum(counts.values())
        rows.append({
            'surah': s['id'],
            'name': s['name'],
            'words': words,
            'verses': s['total_verses'],
            **{f'{k}_count': v for k, v in counts.items()},
            'cosmic_total': total,
            'cosmic_density_per_100w': 100 * total / max(1, words),
        })

    # Sort by cosmic density
    by_density = sorted(rows, key=lambda r: -r['cosmic_density_per_100w'])
    print(f"{'Rank':>4} | {'Surah':>5} | {'Words':>5} | {'samāʾ':>5} | {'arḍ':>4} | {'shams':>5} | {'qamar':>5} | {'najm':>4} | {'baḥr':>4} | {'Total':>5} | {'/100w':>6}")
    for r, info in enumerate(by_density[:20], 1):
        print(f"{r:>4} | Q{info['surah']:03d} | {info['words']:>5} | {info['samaa_count']:>5} | {info['ard_count']:>4} | {info['shams_count']:>5} | {info['qamar_count']:>5} | {info['najm_count']:>4} | {info['bahr_count']:>4} | {info['cosmic_total']:>5} | {info['cosmic_density_per_100w']:>6.2f}")

    q55_rank = next(i+1 for i, x in enumerate(by_density) if x['surah']==55)
    q55 = next(r for r in rows if r['surah']==55)
    print(f"\nQ 55 cosmic-density rank: {q55_rank}/114")
    print(f"Q 55 cosmic counts: {[(k, q55[f'{k}_count']) for k in COSMIC]}")
    print(f"Q 55 cosmic density: {q55['cosmic_density_per_100w']:.2f}/100words")

    densities = [r['cosmic_density_per_100w'] for r in rows]
    print(f"\nCorpus mean: {statistics.mean(densities):.2f}, median: {statistics.median(densities):.2f}, max: {max(densities):.2f}")

    out['top10_by_density'] = by_density[:10]
    out['q55_metrics'] = q55
    out['q55_rank'] = q55_rank
    out['corpus_mean_density'] = statistics.mean(densities)
    out['corpus_median_density'] = statistics.median(densities)
    out['corpus_max_density'] = max(densities)

    if q55_rank == 1:
        out['verdict'] = 'CONFIRMED — Q 55 corpus-#1 in cosmic-vocabulary density'
    elif q55_rank <= 3:
        out['verdict'] = f'CONFIRMED — Q 55 in top-3 (rank={q55_rank})'
    elif q55_rank <= 10:
        out['verdict'] = f'DIRECTIONAL — Q 55 top-10 (rank={q55_rank})'
    else:
        out['verdict'] = f'NULL — Q 55 rank {q55_rank}/114'

    print(f"\nVerdict: {out['verdict']}")

    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Wrote: {OUT}")


if __name__ == '__main__':
    main()
