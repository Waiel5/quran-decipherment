#!/usr/bin/env python3
"""Q019-F-03 — al-Raḥmān refrain density test.

Tests whether Q 19 has the highest absolute count of al-Raḥmān (الرحمن) tokens
in the corpus body (basmala excluded), and whether Q 19's density rank
exceeds Q 55 al-Raḥmān (the surah named al-Raḥmān).

Pre-reg SHA-256: d356279301bca3f6d484bfd94aa9ea12a7b8a69fca8448aa53e5746e2f6025fe
"""
import hashlib, json, os, random, sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q019-maryam/preregs/Q019-F-03-rahman-refrain-density-prereg.md'
EXPECTED_SHA = 'd356279301bca3f6d484bfd94aa9ea12a7b8a69fca8448aa53e5746e2f6025fe'
OUT_JSON = ROOT / 'surahs/Q019-maryam/csv/Q019-F-03.json'
SEED = 20260428
N_PERM = 10000

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
if sha != EXPECTED_SHA:
    print(f"PRE-REG SHA MISMATCH: got {sha}, expected {EXPECTED_SHA}", file=sys.stderr)
    sys.exit(1)
print(f"pre-reg SHA verified: {sha}", file=sys.stderr)

with open(ROOT / 'quran-text/quran-no-tashkeel.json') as f:
    quran = json.load(f)

# Per-surah al-Raḥmān count (body only — basmala-excluded for non-Q1)
# Note: the JSON loader returns text without basmala in the body except Q1 v.1
per_surah = {}
total = 0
for s in quran:
    cnt = sum(v['text'].count('الرحمن') for v in s['verses'])
    n_verses = len(s['verses'])
    per_surah[s['id']] = (s['transliteration'], cnt, n_verses, cnt/n_verses if n_verses else 0)
    total += cnt

# Rank by absolute count
ranked_abs = sorted(per_surah.items(), key=lambda x: -x[1][1])
q19_rank_abs = next(i+1 for i, (sid, _) in enumerate(ranked_abs) if sid == 19)

# Rank by density (per verse) — surahs with ≥ 30 verses for fair comparison
filtered = [(sid, info) for sid, info in per_surah.items() if info[2] >= 30]
ranked_dens = sorted(filtered, key=lambda x: -x[1][3])
q19_rank_dens = next((i+1 for i, (sid, _) in enumerate(ranked_dens) if sid == 19), None)

q55 = per_surah.get(55, ('Ar-Rahman', 0, 78, 0))

# Permutation null: redistribute total tokens by surah length
total_words = sum(sum(len(v['text'].split()) for v in s['verses']) for s in quran)
surah_words = {s['id']: sum(len(v['text'].split()) for v in s['verses']) for s in quran}
rng = random.Random(SEED)

null_q19_ranks_abs = []
for _ in range(N_PERM):
    counts = {sid: 0 for sid in surah_words}
    for _ in range(total):
        u = rng.random() * total_words
        cum = 0
        for sid, w in surah_words.items():
            cum += w
            if u <= cum:
                counts[sid] += 1
                break
    sorted_null = sorted(counts.items(), key=lambda x: -x[1])
    null_rank = next(i+1 for i, (sid, _) in enumerate(sorted_null) if sid == 19)
    null_q19_ranks_abs.append(null_rank)

null_le_abs = sum(1 for r in null_q19_ranks_abs if r <= q19_rank_abs) / N_PERM

result = {
    'finding_id': 'Q019-F-03',
    'pre_reg_sha256': sha,
    'seed': SEED,
    'n_perm': N_PERM,
    'rules_tuple': '(no-tashkeel, orthographic, exact-substring الرحمن, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
    'observed': {
        'q19_count_abs': per_surah[19][1],
        'q19_rank_abs': q19_rank_abs,
        'q19_density_per_verse': per_surah[19][3],
        'q19_rank_density_among_30plus_verse': q19_rank_dens,
        'corpus_total': total,
        'top_10_abs': [
            {'surah': sid, 'name': info[0], 'count': info[1], 'n_verses': info[2], 'density': info[3]}
            for sid, info in ranked_abs[:10]
        ],
        'q55_alrahman_count': q55[1],
        'q55_alrahman_density': q55[3],
        'top_10_density_among_30plus': [
            {'surah': sid, 'name': info[0], 'count': info[1], 'n_verses': info[2], 'density': info[3]}
            for sid, info in ranked_dens[:10]
        ],
    },
    'null_distribution': {
        'q19_rank_mean': sum(null_q19_ranks_abs) / N_PERM,
        'q19_rank_p05': sorted(null_q19_ranks_abs)[int(0.05*N_PERM)],
        'p_value_le_observed_rank': null_le_abs,
    },
    'verdict': {
        'direction_locked': 'Q 19 rank = 1 absolute count, p < 0.0125',
        'pass_h1': q19_rank_abs == 1 and null_le_abs < 0.0125,
        'pass_h2_q19_gt_q55': per_surah[19][1] > q55[1],
        'note': (f'Q 19 abs count = {per_surah[19][1]} (rank {q19_rank_abs}); '
                 f'Q 55 = {q55[1]}; classical-vs-empirical inversion: '
                 f"{'CONFIRMED' if per_surah[19][1] > q55[1] else 'NOT-CONFIRMED'}"),
    },
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f"output: {OUT_JSON}", file=sys.stderr)
print(f"VERDICT: H1={'PASS' if result['verdict']['pass_h1'] else 'FAIL'}, H2={'PASS' if result['verdict']['pass_h2_q19_gt_q55'] else 'FAIL'}", file=sys.stderr)
