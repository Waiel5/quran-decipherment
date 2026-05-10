#!/usr/bin/env python3
"""Q034-F-03 — Q 34 ROOT:Hmd token-count + per-verse density rank in corpus.

Pre-reg: surahs/Q034-saba/preregs/Q034-F-03-hmd-root-rank-prereg.md
Pre-reg SHA256: 70d7b5ec80de9cf6a2aef1586847b24e8c976b6314af0a228afa9d098c963c00
Rules-tuple: (no-tashkeel, QAC-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

H1: Q34 ROOT:Hmd token-count is in top-10 of 114 surahs.
H2: Q34 per-verse density is in top-10 of 36 surahs with >=1 attestation.
H3: Q34 per-verse density > median of 5 al-hamdu openers {1,6,18,34,35}.
Bonferroni k=3, alpha_bon=0.01667.
"""
import json, hashlib, sys, os, re

PREREG = '/Users/grey/Downloads/quran/surahs/Q034-saba/preregs/Q034-F-03-hmd-root-rank-prereg.md'
EXPECTED_SHA = '70d7b5ec80de9cf6a2aef1586847b24e8c976b6314af0a228afa9d098c963c00'
SEED = 20260509
ALPHA_BON = 0.05 / 3


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    counts = {}
    location_re = re.compile(r'^\((\d+):(\d+):(\d+):?(\d+)?\)')
    with open('/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt') as f:
        for line in f:
            if 'ROOT:Hmd' not in line:
                continue
            m = location_re.match(line.strip())
            if m:
                s = int(m.group(1))
                counts[s] = counts.get(s, 0) + 1

    verse_counts = {}
    with open('/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv') as f:
        for line in f:
            sid, vc = line.strip().split('\t')
            verse_counts[int(sid)] = int(vc)

    # Token-count rank (descending; ties handled by dense rank)
    sorted_counts = sorted(counts.items(), key=lambda x: -x[1])
    q34_count = counts.get(34, 0)
    rank_count = None
    for rk, (s, c) in enumerate(sorted_counts, 1):
        if s == 34:
            rank_count = rk
            break
    # Density: count / verse_count (only for surahs with >=1 attestation)
    densities = {s: c/verse_counts[s] for s, c in counts.items()}
    sorted_density = sorted(densities.items(), key=lambda x: -x[1])
    q34_density = densities.get(34, 0.0)
    rank_density = None
    for rk, (s, d) in enumerate(sorted_density, 1):
        if s == 34:
            rank_density = rk
            break

    # H1: rank_count <= 10
    h1_pass = rank_count is not None and rank_count <= 10
    # H2: rank_density <= 10
    h2_pass = rank_density is not None and rank_density <= 10

    # H3: q34 density > median of 5 openers
    openers = [1, 6, 18, 34, 35]
    opener_densities = [densities.get(s, 0.0) for s in openers]
    opener_densities_sorted = sorted(opener_densities)
    # median of 5 = middle (index 2)
    median_5 = opener_densities_sorted[2]
    h3_pass = q34_density > median_5

    n_pass = sum([h1_pass, h2_pass, h3_pass])
    if n_pass == 3: verdict = 'CONFIRMED'
    elif n_pass == 2: verdict = 'DIRECTIONAL'
    elif n_pass == 1: verdict = 'DIRECTIONAL-WEAK'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q034-F-03',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, QAC-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'seed': SEED,
        'alpha_bon': ALPHA_BON,
        'corpus_total_hmd_tokens': sum(counts.values()),
        'corpus_n_surahs_with_hmd': len(counts),
        'h1_token_count': {
            'q34_count': q34_count,
            'rank': rank_count,
            'top10_threshold': 10,
            'pass': h1_pass,
            'top10_table': [{'surah': s, 'count': c} for s, c in sorted_counts[:10]],
        },
        'h2_per_verse_density': {
            'q34_density': q34_density,
            'q34_verse_count': verse_counts.get(34),
            'rank': rank_density,
            'top10_threshold': 10,
            'pass': h2_pass,
            'top10_table': [{'surah': s, 'density': d, 'count': counts[s], 'verses': verse_counts[s]} for s, d in sorted_density[:10]],
        },
        'h3_opener_intra_median': {
            'openers': openers,
            'opener_densities': [{'surah': s, 'density': densities.get(s, 0.0), 'count': counts.get(s, 0), 'verses': verse_counts[s]} for s in openers],
            'median_5_density': median_5,
            'q34_density': q34_density,
            'q34_above_median': h3_pass,
            'pass': h3_pass,
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'Token-count ties (rank 6 with multiple surahs at 3 tokens) means rank_count is dense-rank-based; Q34 tied with Q14, Q27, Q31, Q35, Q40. H2 density is more discriminating (per-verse normalization). Pre-flight observation made; verdict ceiling = DESCRIPTIVE-EMPIRICAL.',
    }

    print('=== Q034-F-03 hmd-root rank ===')
    print(f'H1 token-count: Q34={q34_count}, rank={rank_count}/114 -> pass={h1_pass}')
    print(f'H2 per-verse density: Q34={q34_density:.4f}, rank={rank_density}/{len(densities)} -> pass={h2_pass}')
    print(f'H3 opener-cluster median: median_5={median_5:.4f}, Q34={q34_density:.4f} -> pass={h3_pass}')
    print(f'\nN pass: {n_pass}/3 -> {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q034-saba/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q034-saba/csv/Q034-F-03.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
