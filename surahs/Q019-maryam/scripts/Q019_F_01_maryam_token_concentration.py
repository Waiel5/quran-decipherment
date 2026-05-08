#!/usr/bin/env python3
"""Q019-F-01 — Maryam token-concentration test.

Tests whether Q 19 Maryam ranks 1 in absolute Maryam-token count (Yūsuf-Q12 model)
or rank > 1 (FALSIFICATION direction).

Pre-reg SHA-256: fe028e3ea25ba30d96aec724cf9bd8568d2ba909d67112d9c30b092d85c51fe2
"""
import hashlib, json, os, random, re, sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q019-maryam/preregs/Q019-F-01-maryam-token-concentration-prereg.md'
EXPECTED_SHA = 'fe028e3ea25ba30d96aec724cf9bd8568d2ba909d67112d9c30b092d85c51fe2'
OUT_JSON = ROOT / 'surahs/Q019-maryam/csv/Q019-F-01.json'
SEED = 20260428
N_PERM = 10000

# Verify pre-reg SHA
sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
if sha != EXPECTED_SHA:
    print(f"PRE-REG SHA MISMATCH: got {sha}, expected {EXPECTED_SHA}", file=sys.stderr)
    sys.exit(1)
print(f"pre-reg SHA verified: {sha}", file=sys.stderr)

# Load corpus
with open(ROOT / 'quran-text/quran-no-tashkeel.json') as f:
    quran = json.load(f)

# Count Maryam tokens per surah
per_surah = {}
total = 0
for s in quran:
    cnt = sum(v['text'].count('مريم') for v in s['verses'])
    if cnt > 0:
        per_surah[s['id']] = (s['transliteration'], cnt, len(s['verses']))
        total += cnt

# Rank
ranked = sorted(per_surah.items(), key=lambda x: -x[1][1])
q19_rank = next(i+1 for i, (sid, _) in enumerate(ranked) if sid == 19)

# Permutation null: re-distribute tokens uniformly weighted by surah length
total_words = sum(sum(len(v['text'].split()) for v in s['verses']) for s in quran)
surah_words = {s['id']: sum(len(v['text'].split()) for v in s['verses']) for s in quran}

rng = random.Random(SEED)
null_q19_ranks = []
for _ in range(N_PERM):
    # Multinomial draw of `total` tokens across 114 surahs proportional to length
    counts = {sid: 0 for sid in surah_words}
    for _ in range(total):
        # Sample surah by length-weight
        u = rng.random() * total_words
        cum = 0
        for sid, w in surah_words.items():
            cum += w
            if u <= cum:
                counts[sid] += 1
                break
    sorted_null = sorted(counts.items(), key=lambda x: -x[1])
    null_rank = next(i+1 for i, (sid, _) in enumerate(sorted_null) if sid == 19)
    null_q19_ranks.append(null_rank)

# p-value: probability under null of rank ≤ observed (small rank = high count)
null_le = sum(1 for r in null_q19_ranks if r <= q19_rank) / N_PERM

# Direction-locked (predicted Q 19 rank > 1):
# pass = q19_rank > 1
result = {
    'finding_id': 'Q019-F-01',
    'pre_reg_sha256': sha,
    'seed': SEED,
    'n_perm': N_PERM,
    'rules_tuple': '(no-tashkeel, orthographic, exact-substring مريم, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
    'observed': {
        'q19_rank': q19_rank,
        'q19_count': per_surah[19][1] if 19 in per_surah else 0,
        'q19_share_corpus': per_surah[19][1] / total if 19 in per_surah else 0,
        'corpus_total': total,
        'top_10': [
            {'surah': sid, 'name': info[0], 'count': info[1], 'share': info[1]/total}
            for sid, info in ranked[:10]
        ],
    },
    'null_distribution': {
        'q19_rank_mean': sum(null_q19_ranks) / N_PERM,
        'q19_rank_p05': sorted(null_q19_ranks)[int(0.05*N_PERM)],
        'q19_rank_p95': sorted(null_q19_ranks)[int(0.95*N_PERM)],
        'p_value_le_observed': null_le,
    },
    'comparator_yusuf_q12_concentration': 0.952,
    'verdict': {
        'direction_locked': 'Q 19 rank > 1 (Yūsuf-model FALSIFIED for Q 19)',
        'observed_direction_match': q19_rank > 1,
        'pass': (q19_rank > 1),
        'note': f'Q 19 rank = {q19_rank}; concentration = {per_surah[19][1]/total*100:.1f}% (vs Yūsuf 95.2% in Q 12)',
    },
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f"output: {OUT_JSON}", file=sys.stderr)
print(f"VERDICT: {'PASS' if result['verdict']['pass'] else 'FAIL'} — Q 19 rank = {q19_rank}", file=sys.stderr)
