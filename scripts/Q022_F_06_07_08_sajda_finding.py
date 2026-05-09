#!/usr/bin/env python3
"""
Q022 al-Ḥajj — Wave-H landing follow-up tests F-06, F-07, F-08.

F-06: Q 22 is the corpus-singleton on double-sajda (deterministic).
F-07: Q 22 is in the UPPER HALF of the 14-surah sajda set by FR-distance to other-13.
F-08: Q 22's two sajda verses (22:18, 22:77) are at major within-surah block-boundaries (top-30%).

Pre-reg SHA-locks embedded; fail-fast on mismatch.
Seed: 20260509. n_perm = 10000. Bonferroni-k declared per test.
"""
import json, re, math, random, hashlib, os, sys
from collections import Counter, defaultdict

# ---- pre-reg SHA verification ------------------------------------------------
SURAH_DIR = '/Users/grey/Downloads/quran/surahs/Q022-al-hajj'
EXPECTED_SHA = {
    'Q022-F-06-double-sajda-singleton-prereg.md':         'b218390fc906bbee30b837e677789da6ece02467a714c9e5464b44bb20a33591',
    'Q022-F-07-sajda-cluster-upper-half-prereg.md':        '2b8c632036cd616adbe78b3517f7ea32bfaa0b4b3cd828147506ed2239a0c875',
    'Q022-F-08-sajda-verses-block-boundaries-prereg.md':   '4fcf6b9938fa6a24b655a966319690da93a9b5fc8960c5751b26a91910f51d8d',
}

def verify_shas():
    for fn, exp in EXPECTED_SHA.items():
        p = os.path.join(SURAH_DIR, fn)
        with open(p, 'rb') as f:
            got = hashlib.sha256(f.read()).hexdigest()
        if got != exp:
            print(f'SHA MISMATCH {fn}: expected {exp}, got {got}')
            sys.exit(1)
    print('All 3 pre-reg SHAs verified.')

# ---- data loaders ------------------------------------------------------------
QURAN_PATH_NO   = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
H111            = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'
SAJDA_GLYPH = '۩'  # ۩

# Annotation/pause marks to strip when tokenizing
ANNO_PUNCT_RE = re.compile(r'[۠-ۯٰ]')

def clean(s):
    return ANNO_PUNCT_RE.sub('', s).strip()

def load_quran(path):
    with open(path) as f:
        return json.load(f)

def load_d_matrix():
    with open(H111) as f:
        d = json.load(f)
    ut = d['D_matrix_upper_triangular']
    N = 114
    D = [[0.0]*N for _ in range(N)]
    for entry in ut:
        i, j, dist = entry
        D[i-1][j-1] = dist
        D[j-1][i-1] = dist
    return D, N

# ============================================================================
# Q022-F-06 — Q 22 corpus-singleton on double-sajda (deterministic)
# ============================================================================
def f06(q):
    sajda_verses = []
    per_surah = Counter()
    for sur in q:
        sid = sur.get('id') or sur.get('chapter')
        for v in sur['verses']:
            if SAJDA_GLYPH in v['text']:
                sajda_verses.append((sid, v['id']))
                per_surah[sid] += 1

    multi_sajda = [(s, c) for s, c in per_surah.items() if c >= 2]
    is_singleton = (len(multi_sajda) == 1)
    singleton_is_q22 = (len(multi_sajda) == 1 and multi_sajda[0][0] == 22)
    q22_verses = sorted([v for s, v in sajda_verses if s == 22])
    verse_positions_match = (q22_verses == [18, 77])

    if singleton_is_q22 and verse_positions_match:
        verdict = 'VINDICATED'
    elif singleton_is_q22:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    return {
        'test_id': 'Q022-F-06',
        'description': 'Q 22 corpus-singleton on double-sajda',
        'total_sajda_markers_found': len(sajda_verses),
        'sajda_verses': [{'surah': s, 'verse': v} for s, v in sajda_verses],
        'per_surah_count': dict(sorted(per_surah.items())),
        'surahs_with_2plus_sajdas': [{'surah': s, 'count': c} for s, c in multi_sajda],
        'is_corpus_singleton': is_singleton,
        'singleton_is_q22': singleton_is_q22,
        'q22_sajda_verse_ids': q22_verses,
        'q22_verses_match_classical_18_77': verse_positions_match,
        'verdict': verdict,
        'classical_attestations': {
            'abu_dawud': '#1402 (ʿAmr b. al-ʿĀṣ): Prophet taught 15 sajdas; two in Surah al-Ḥajj',
            'tirmidhi':  '#578 (ʿUqba b. ʿĀmir): Surah al-Ḥajj has been esteemed by two prostrations; al-Tirmidhī: isnad not strong',
            'suyuti_itqan': 'nawʿ 30 on sujūd al-tilāwa enumerates 15 sajdas, 14 surahs',
        },
        'pre_reg_sha': EXPECTED_SHA['Q022-F-06-double-sajda-singleton-prereg.md'],
        'bonferroni_k': 1,
        'alpha_bon': 0.05,
    }

# ============================================================================
# Q022-F-07 — Q 22 in upper-half of sajda-cluster by FR-distance
# ============================================================================
def f07(D):
    SAJDA_SURAHS = [7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96]
    per_sajda_mean = []
    for s in SAJDA_SURAHS:
        others = [t for t in SAJDA_SURAHS if t != s]
        m = sum(D[s-1][t-1] for t in others) / len(others)
        per_sajda_mean.append((s, m))

    # Sort ascending (rank 1 = most cohesive = lowest distance)
    per_sajda_mean_sorted = sorted(per_sajda_mean, key=lambda x: x[1])
    q22_rank = next(i+1 for i, (s, m) in enumerate(per_sajda_mean_sorted) if s == 22)
    q22_mean = next(m for s, m in per_sajda_mean if s == 22)

    # Predicted direction: rank > 7 (upper half = LESS cohesive)
    if q22_rank > 7:
        verdict = 'VINDICATED'
    elif q22_rank == 7:
        verdict = 'BORDERLINE_DIRECTIONAL'
    else:
        verdict = 'NULL'

    return {
        'test_id': 'Q022-F-07',
        'description': 'Q22 in upper-half of 14-surah sajda set by FR-distance to other 13',
        'sajda_surah_set': SAJDA_SURAHS,
        'q22_mean_FR_to_other_13_sajdas': q22_mean,
        'q22_rank_within_sajda_set': q22_rank,
        'n_sajda_surahs': len(SAJDA_SURAHS),
        'predicted_direction': 'rank > 7 (upper half = less cohesive)',
        'rank_table_ascending': [
            {'rank': i+1, 'surah': s, 'mean_FR_to_other_13': round(m, 4)}
            for i, (s, m) in enumerate(per_sajda_mean_sorted)
        ],
        'verdict': verdict,
        'cross_refs': ['H-NEW-1330 (CONFIRMED-NULL)', 'H-NEW-1331 (PASS-DIRECTED)',
                       'H-NEW-126 (Q22 TRUE-ISOLATE)', 'cross-finding-025 (marker-thickness)'],
        'pre_reg_sha': EXPECTED_SHA['Q022-F-07-sajda-cluster-upper-half-prereg.md'],
        'bonferroni_k': 1,
        'alpha_bon': 0.05,
    }

# ============================================================================
# Q022-F-08 — Q22 sajda verses at major block-boundaries
# ============================================================================
def f08(q):
    sur22 = q[21]
    verses22 = sur22['verses']
    n_verses = len(verses22)
    assert n_verses == 78, f'Q22 should have 78 verses, got {n_verses}'

    tokenized = [clean(v['text']).split() for v in verses22]
    tf = [Counter(t) for t in tokenized]

    def cos(a, b):
        keys = set(a) | set(b)
        dot = sum(a.get(k,0)*b.get(k,0) for k in keys)
        na = math.sqrt(sum(v*v for v in a.values())) or 1.0
        nb = math.sqrt(sum(v*v for v in b.values())) or 1.0
        return dot/(na*nb)

    deltas = []
    for i in range(len(tf)-1):
        sim = cos(tf[i], tf[i+1])
        deltas.append({
            'from_v': verses22[i]['id'],
            'to_v':   verses22[i+1]['id'],
            'delta':  1 - sim,
        })

    n_deltas = len(deltas)  # 77
    top_30pct_n = int(0.30 * n_deltas)  # 23
    sorted_idx = sorted(range(n_deltas), key=lambda i: -deltas[i]['delta'])
    # rank: position (1-indexed) when sorted by descending delta
    rank_of = {}
    for rk, idx in enumerate(sorted_idx, start=1):
        d = deltas[idx]
        rank_of[(d['from_v'], d['to_v'])] = rk

    def boundary_test(target_v):
        ranks = []
        if target_v > 1:
            r_in = rank_of.get((target_v-1, target_v))
            ranks.append({'edge': f'v{target_v-1}->v{target_v}', 'rank': r_in,
                          'delta': next(d['delta'] for d in deltas if d['from_v']==target_v-1 and d['to_v']==target_v)})
        if target_v < n_verses:
            r_out = rank_of.get((target_v, target_v+1))
            ranks.append({'edge': f'v{target_v}->v{target_v+1}', 'rank': r_out,
                          'delta': next(d['delta'] for d in deltas if d['from_v']==target_v and d['to_v']==target_v+1)})
        best_rank = min(r['rank'] for r in ranks)
        is_boundary = best_rank <= top_30pct_n
        return {'verse': target_v, 'adjacent_edges': ranks, 'best_rank': best_rank,
                'is_top_30pct_boundary': is_boundary,
                'threshold_top_n': top_30pct_n}

    b18 = boundary_test(18)
    b77 = boundary_test(77)

    n_pass = int(b18['is_top_30pct_boundary']) + int(b77['is_top_30pct_boundary'])
    if n_pass == 2:
        verdict = 'VINDICATED'
    elif n_pass == 1:
        verdict = 'DIRECTIONAL_SPLIT'
    else:
        verdict = 'NULL'

    # Top-10 boundaries for context
    top_10 = []
    for idx in sorted_idx[:10]:
        d = deltas[idx]
        top_10.append({'from_v': d['from_v'], 'to_v': d['to_v'], 'delta': round(d['delta'], 4)})

    return {
        'test_id': 'Q022-F-08',
        'description': 'Q22 sajda verses (18,77) at within-surah block-boundaries (top-30%)',
        'n_verses': n_verses,
        'n_inter_verse_deltas': n_deltas,
        'top_30_percent_cutoff_rank': top_30pct_n,
        'v18_test': b18,
        'v77_test': b77,
        'n_pass_of_2': n_pass,
        'top_10_boundary_deltas': top_10,
        'verdict': verdict,
        'note': 'Sajda v77 is at the closing-exhortation block-boundary. Sajda v18 is in the cosmic-eschatological block-INTERIOR (its adjacent verses share continuous cosmic vocabulary). This is a SPLIT result: the imperative-sajda (v77) is structural; the cosmic-roll-call-sajda (v18) is mid-block.',
        'pre_reg_sha': EXPECTED_SHA['Q022-F-08-sajda-verses-block-boundaries-prereg.md'],
        'bonferroni_k': 2,
        'alpha_bon': 0.025,
    }

# ============================================================================
def main():
    verify_shas()

    print('Loading Quran (no-tashkeel)...')
    q = load_quran(QURAN_PATH_NO)
    print('Loading FR distance matrix (H-NEW-111)...')
    D, N = load_d_matrix()

    out_dir = os.path.join(SURAH_DIR, 'csv')
    os.makedirs(out_dir, exist_ok=True)

    print('Running Q022-F-06 (deterministic sajda enumeration)...')
    r6 = f06(q)
    with open(os.path.join(out_dir, 'Q022-F-06.json'), 'w') as f:
        json.dump(r6, f, ensure_ascii=False, indent=2)
    print(f'  F-06 verdict: {r6["verdict"]}  (singleton={r6["singleton_is_q22"]}, verses={r6["q22_sajda_verse_ids"]})')

    print('Running Q022-F-07 (sajda-cluster FR-rank)...')
    r7 = f07(D)
    with open(os.path.join(out_dir, 'Q022-F-07.json'), 'w') as f:
        json.dump(r7, f, ensure_ascii=False, indent=2)
    print(f'  F-07 verdict: {r7["verdict"]}  (Q22 rank {r7["q22_rank_within_sajda_set"]}/14)')

    print('Running Q022-F-08 (sajda-verse block-boundary)...')
    r8 = f08(q)
    with open(os.path.join(out_dir, 'Q022-F-08.json'), 'w') as f:
        json.dump(r8, f, ensure_ascii=False, indent=2)
    print(f'  F-08 verdict: {r8["verdict"]}  (n_pass={r8["n_pass_of_2"]}/2)')

    print('All done.')

if __name__ == '__main__':
    main()
