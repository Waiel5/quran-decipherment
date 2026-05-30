#!/usr/bin/env python3
"""H-NEW-2430 — Eponymous-surah cycle-centrality law.

For every figure with BOTH a dedicated eponymous surah AND a recurring
multi-surah narrative cycle (Nūḥ Q71, Ibrāhīm Q14, Hūd Q11, Maryam Q19,
Yūnus Q10), compute the eponymous surah's mean-pairwise root-Jaccard
CENTRALITY RANK within its cycle. Generalises Q071-F-01 (Nūḥ peripheral,
rank 5/6) + Q020-F-06 (Ṭā-Hā = Mūsā hub, the non-eponymous core carrier) to
a corpus-wide law, extending H-NEW-1820 (title-density independence).

Direction LOCKED: eponymous surahs are NOT systematically the cycle centroid —
median eponymous centrality-rank > 1 (≤ 2 of 5 rank-1). Reversal (median==1 and
rank-null p<0.05) is a pre-commit violation, published with full prominence.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2430-eponymous-cycle-centrality.md
Pre-reg SHA-256: 67a689a5382cac196f7bec9cbdb19c31f3a226db864dcbe2b680e045fe09019e
Seed 20260509, n_perm=10000. Arm B Bonferroni across k=5 cycles: α = 0.05/5 = 0.01.
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, verse-union pericope,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import json
import hashlib
import sys
import os
import random
from collections import defaultdict
from itertools import combinations

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'findings/phase-b-hypotheses/prereg-h-new-2430-eponymous-cycle-centrality.md')
EXPECTED_SHA = '67a689a5382cac196f7bec9cbdb19c31f3a226db864dcbe2b680e045fe09019e'
SEED = 20260509
N_PERM = 10000
BONFERRONI_K = 5  # five eponymous cycles, Arm B family
ALPHA_BON = 0.05 / BONFERRONI_K  # 0.01

MORPH = os.path.join(ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN = os.path.join(ROOT, 'quran-text/quran-no-tashkeel.json')
OUT = os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-2430.json')

# Each cycle: list of (label, surah, v0, v1); 'eponymous' is the ◆ label.
# Boundaries verified on disk (verify_boundaries) and against the markers below.
CYCLES = {
    'NUH': {
        'eponymous': 'Q 71:1-28',
        'eponymous_surah': 71,
        'marker': ['نوح', 'نوحا'],
        'pericopes': [
            ('Q 7:59-64',     7,  59,  64),
            ('Q 11:25-49',   11,  25,  49),
            ('Q 23:23-30',   23,  23,  30),
            ('Q 26:105-122', 26, 105, 122),
            ('Q 54:9-17',    54,   9,  17),
            ('Q 71:1-28',    71,   1,  28),
        ],
        'core_episode_carrier': False,  # Q71 develops daʿwa/idol material, not the ark/flood core
    },
    'IBRAHIM': {
        'eponymous': 'Q 14:35-41',
        'eponymous_surah': 14,
        'marker': ['إبراهيم', 'ابراهيم'],
        'pericopes': [
            ('Q 6:74-83',     6,  74,  83),
            ('Q 14:35-41',   14,  35,  41),
            ('Q 19:41-50',   19,  41,  50),
            ('Q 21:51-70',   21,  51,  70),
            ('Q 26:69-104',  26,  69, 104),
            ('Q 37:83-113',  37,  83, 113),
        ],
        'core_episode_carrier': False,  # Q14 carries only the Mecca-duʿāʾ, a distinct episode
    },
    'HUD': {
        'eponymous': 'Q 11:50-60',
        'eponymous_surah': 11,
        'marker': ['هود', 'هودا', 'عاد', 'عادا'],
        'pericopes': [
            ('Q 7:65-72',     7,  65,  72),
            ('Q 11:50-60',   11,  50,  60),
            ('Q 26:123-140', 26, 123, 140),
            ('Q 46:21-26',   46,  21,  26),
            ('Q 54:18-21',   54,  18,  21),
        ],
        'core_episode_carrier': True,  # Q11 carries the fullest Hūd→ʿĀd episode
    },
    'MARYAM': {
        'eponymous': 'Q 19:16-34',
        'eponymous_surah': 19,
        # Maryam cycle markers: the name مريم/عيسى OR the canonical referential
        # nafkh-rūḥ formula by which Q 21:91 alludes to her ("...فنفخنا فيها/فيه من
        # روحنا...وابنها") — Q 21:91 is a LOCKED cycle member in pre-reg §2.4 (the
        # ʿĪsā-sign allusion). This widening keeps the locked inventory intact.
        'marker': ['مريم', 'عيسى', 'روحنا', 'وابنها'],
        'pericopes': [
            ('Q 3:35-47',     3,  35,  47),
            ('Q 19:16-34',   19,  16,  34),
            ('Q 21:91',      21,  91,  91),
            ('Q 23:50',      23,  50,  50),
            ('Q 66:12',      66,  12,  12),
        ],
        'core_episode_carrier': True,  # Q19 carries the fullest nativity episode
    },
    'YUNUS': {
        'eponymous': 'Q 10:98',
        'eponymous_surah': 10,
        'marker': ['يونس', 'النون', 'الحوت', 'حوت'],
        'pericopes': [
            ('Q 10:98',      10,  98,  98),
            ('Q 21:87-88',   21,  87,  88),
            ('Q 37:139-148', 37, 139, 148),
            ('Q 68:48-50',   68,  48,  50),
        ],
        'core_episode_carrier': False,  # Q10 is a 1-verse allusion (qawm Yūnus), not the fish episode
    },
}

# MŪSĀ documented control — no eponymous surah, so NO data point. Reproduces
# Q020-F-06 hub-strengths as an MW-5 sanity assertion only.
MUSA_CONTROL = [
    ('Q 20:9-36',  20,  9, 36),
    ('Q 27:7-14',  27,  7, 14),
    ('Q 28:29-35', 28, 29, 35),
    ('Q 79:15-26', 79, 15, 26),
]
MUSA_Q20_HUB_STORED = 0.234  # from surahs/Q020-ta-ha/csv/Q020-F-06.json (rounded)

# MW-5: Nūḥ centrality must reproduce Q071-F-01 (rank 5/6, centroid Q 7:59-64).
NUH_Q71_RANK_STORED = 5
NUH_CENTROID_STORED = 'Q 7:59-64'


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: pre-reg SHA mismatch.\n  expected {EXPECTED_SHA}\n  actual   {actual}",
              file=sys.stderr)
        sys.exit(1)
    print(f"Pre-reg SHA-256 OK: {actual}")


def load_qac_roots_by_verse():
    vr = defaultdict(set)
    with open(MORPH, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0].strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc.split(':'))
            except ValueError:
                continue
            for tok in parts[3].split('|'):
                if tok.startswith('ROOT:'):
                    vr[(s, v)].add(tok[len('ROOT:'):])
                    break
    return dict(vr)


def pericope_roots(vr, s, v0, v1):
    out = set()
    for v in range(v0, v1 + 1):
        out |= vr.get((s, v), set())
    return out


def jac(a, b):
    u = a | b
    return len(a & b) / len(u) if u else 0.0


def window_roots(vr, all_verses, start, L):
    out = set()
    for vk in all_verses[start:start + L]:
        out |= vr.get(vk, set())
    return out


def verify_boundaries(text_sidx):
    """Each pericope range must exist and contain its figure-marker in no-tashkeel."""
    failures = []
    for cyc, d in CYCLES.items():
        verses = {int(v['id']): v['text'] for v in text_sidx[d['eponymous_surah']]['verses']} \
            if d['eponymous_surah'] in text_sidx else {}
        for label, s, v0, v1 in d['pericopes']:
            if s not in text_sidx:
                failures.append(f'{cyc} {label}: surah {s} missing')
                continue
            sv = {int(v['id']): v['text'] for v in text_sidx[s]['verses']}
            for v in range(v0, v1 + 1):
                if v not in sv:
                    failures.append(f'{cyc} {label}: verse {v} missing')
            joined = ' '.join(sv.get(v, '') for v in range(v0, v1 + 1))
            if not any(m in joined for m in d['marker']):
                failures.append(f'{cyc} {label}: no figure-marker {d["marker"]} found')
    if failures:
        print('FATAL: boundary verification failed:', file=sys.stderr)
        for fa in failures:
            print('  ' + fa, file=sys.stderr)
        sys.exit(1)
    print('Pericope boundaries + figure-markers OK for all 5 eponymous cycles.')


def centrality_rank(vr, pericopes, target_label):
    rs = {label: pericope_roots(vr, s, v0, v1) for label, s, v0, v1 in pericopes}
    labels = [p[0] for p in pericopes]
    J = {}
    for i, j in combinations(labels, 2):
        v = jac(rs[i], rs[j])
        J[(i, j)] = v
        J[(j, i)] = v
    cent = {a: sum(J[(a, b)] for b in labels if b != a) / (len(labels) - 1) for a in labels}
    ranked = sorted(labels, key=lambda a: -cent[a])
    table = [{'pericope': a, 'mean_jaccard': cent[a], 'rank': ranked.index(a) + 1} for a in labels]
    table.sort(key=lambda r: r['rank'])
    return rs, cent, ranked, table, cent[target_label], ranked.index(target_label) + 1


def run_cycle(cyc, d, vr, all_verses, rng):
    pers = d['pericopes']
    epl = d['eponymous']
    rs, cent, ranked, table, epl_cent, epl_rank = centrality_rank(vr, pers, epl)
    n = len(pers)
    centroid = ranked[0]

    # Arm A label
    if epl_rank == 1:
        armA = 'CENTROID'
    elif epl_rank == 2:
        armA = 'NEAR-CENTROID'
    else:
        armA = 'PERIPHERAL'

    # Arm B: length-matched random-anchor swap null for the eponymous pericope
    epl_tuple = next(p for p in pers if p[0] == epl)
    L = epl_tuple[3] - epl_tuple[2] + 1
    others = [p[0] for p in pers if p[0] != epl]
    other_sets = [rs[a] for a in others]
    max_start = len(all_verses) - L
    null_c = []
    for _ in range(N_PERM):
        start = rng.randrange(0, max_start + 1)
        w = window_roots(vr, all_verses, start, L)
        null_c.append(sum(jac(w, o) for o in other_sets) / len(other_sets))
    nm = sum(null_c) / N_PERM
    ns = (sum((x - nm) ** 2 for x in null_c) / N_PERM) ** 0.5
    z = (epl_cent - nm) / ns if ns > 0 else float('nan')
    n_ge = sum(1 for x in null_c if x >= epl_cent)
    p_perm = n_ge / N_PERM
    p95 = sorted(null_c)[int(0.95 * N_PERM)]
    if z <= 0:
        armB = 'NULL'
    elif p_perm <= ALPHA_BON:
        armB = 'PASS'
    elif p_perm <= 0.05:
        armB = 'DIRECTIONAL'
    else:
        armB = 'NULL'

    return {
        'cycle': cyc,
        'eponymous_pericope': epl,
        'eponymous_surah': d['eponymous_surah'],
        'core_episode_carrier': d['core_episode_carrier'],
        'n_pericopes': n,
        'centrality_table': table,
        'centroid_pericope': centroid,
        'centroid_mean_jaccard': cent[centroid],
        'eponymous_rank': epl_rank,
        'eponymous_mean_jaccard': epl_cent,
        'arm_A_label': armA,
        'arm_B_anchor_swap': {
            'L_matched': L,
            'eponymous_observed_centrality': epl_cent,
            'null_mean': nm,
            'null_std': ns,
            'null_p95': p95,
            'z': z,
            'p_perm_one_sided_greater': p_perm,
            'n_perm_ge_obs': n_ge,
            'alpha_bon': ALPHA_BON,
            'verdict': armB,
        },
    }


def musa_control(vr):
    rs = {label: pericope_roots(vr, s, v0, v1) for label, s, v0, v1 in MUSA_CONTROL}
    labels = [p[0] for p in MUSA_CONTROL]
    hub = {a: sum(jac(rs[a], rs[b]) for b in labels if b != a) / (len(labels) - 1) for a in labels}
    ranked = sorted(labels, key=lambda a: -hub[a])
    return {
        'note': 'No eponymous Sūrat Mūsā — control only, no data point. Q 20 = non-eponymous core-episode hub (Q020-F-06).',
        'hub_strength': {a: hub[a] for a in labels},
        'hub_rank_descending': ranked,
        'q20_hub_strength': hub['Q 20:9-36'],
    }


def main():
    verify_sha()
    text = json.load(open(QURAN))
    sidx = {int(s['id']): s for s in text}
    verify_boundaries(sidx)

    vr = load_qac_roots_by_verse()
    all_verses = sorted(vr.keys())
    rng = random.Random(SEED)

    results = {}
    for cyc in ('NUH', 'IBRAHIM', 'HUD', 'MARYAM', 'YUNUS'):
        results[cyc] = run_cycle(cyc, CYCLES[cyc], vr, all_verses, rng)

    # ---- MW-5 replication assertions ----
    assert results['NUH']['eponymous_rank'] == NUH_Q71_RANK_STORED, \
        f"MW-5 FAIL: Nūḥ Q71 rank {results['NUH']['eponymous_rank']} != stored {NUH_Q71_RANK_STORED}"
    assert results['NUH']['centroid_pericope'] == NUH_CENTROID_STORED, \
        f"MW-5 FAIL: Nūḥ centroid {results['NUH']['centroid_pericope']} != {NUH_CENTROID_STORED}"
    musa = musa_control(vr)
    assert abs(musa['q20_hub_strength'] - MUSA_Q20_HUB_STORED) < 0.01, \
        f"MW-5 FAIL: Mūsā Q20 hub {musa['q20_hub_strength']:.4f} != stored ~{MUSA_Q20_HUB_STORED}"
    print("MW-5 replication OK: Nūḥ rank 5/6 + centroid Q7:59-64; Mūsā Q20 hub reproduces Q020-F-06.")

    # ---- Arm C: cross-cycle rank law ----
    ranks = [results[c]['eponymous_rank'] for c in ('NUH', 'IBRAHIM', 'HUD', 'MARYAM', 'YUNUS')]
    sizes = [results[c]['n_pericopes'] for c in ('NUH', 'IBRAHIM', 'HUD', 'MARYAM', 'YUNUS')]
    n_rank1 = sum(1 for r in ranks if r == 1)

    def median(xs):
        s = sorted(xs)
        m = len(s)
        return s[m // 2] if m % 2 else (s[m // 2 - 1] + s[m // 2]) / 2

    obs_median = median(ranks)

    # uniform-rank null: each eponymous rank ~ Uniform{1..n_i}
    crng = random.Random(SEED)
    null_medians = []
    null_n_rank1 = []
    for _ in range(N_PERM):
        draw = [crng.randint(1, sz) for sz in sizes]
        null_medians.append(median(draw))
        null_n_rank1.append(sum(1 for r in draw if r == 1))
    nm_med = sum(null_medians) / N_PERM
    # one-sided p that eponymous ranks are BETTER (smaller) than chance
    p_median_le = (sum(1 for x in null_medians if x <= obs_median) + 1) / (N_PERM + 1)
    p_rank1_ge = (sum(1 for x in null_n_rank1 if x >= n_rank1) + 1) / (N_PERM + 1)

    # H1 = eponymy != centrality: median > 1 (and <= 2 of 5 rank-1)
    h1_holds = (obs_median > 1) and (n_rank1 <= 2)
    reversal = (obs_median == 1) and (p_rank1_ge < 0.05)
    if reversal:
        arm_c_verdict = 'REVERSAL — eponymy ⇒ centrality (PRE-COMMIT VIOLATION, full prominence)'
    elif h1_holds:
        arm_c_verdict = 'H1 CONFIRMED — eponymy ≠ centrality (median rank > 1)'
    elif obs_median == 1:
        arm_c_verdict = 'DIRECTIONAL-REVERSAL — median==1 but rank-null p>=0.05 (inconclusive at N, MW-7 cap)'
    else:
        arm_c_verdict = f'PARTIAL — median {obs_median}, {n_rank1}/5 rank-1'

    # core-carrier refinement (MW-7 capped descriptive)
    carrier_ranks = {c: (results[c]['eponymous_rank'], results[c]['core_episode_carrier'])
                     for c in ('NUH', 'IBRAHIM', 'HUD', 'MARYAM', 'YUNUS')}

    out = {
        'finding_id': 'H-NEW-2430',
        'title': 'Eponymous-surah cycle-centrality law',
        'prereg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k_armB': BONFERRONI_K,
        'alpha_bon_armB': ALPHA_BON,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'extends': 'H-NEW-1820 + H-NEW-2260 + Q071-F-01 + Q020-F-06',
        'direction_locked': 'eponymy != centrality — median eponymous rank > 1 (<= 2 of 5 rank-1)',
        'degenerate_excluded': {
            'YUSUF_Q12': 'no recurring multi-surah cycle (story confined to Q12)',
            'MUHAMMAD_Q47': 'no narrated multi-surah prophet-story cycle',
        },
        'musa_control': musa,
        'cycles': results,
        'arm_C_cross_cycle_law': {
            'eponymous_ranks': dict(zip(('NUH', 'IBRAHIM', 'HUD', 'MARYAM', 'YUNUS'), ranks)),
            'cycle_sizes': dict(zip(('NUH', 'IBRAHIM', 'HUD', 'MARYAM', 'YUNUS'), sizes)),
            'observed_median_rank': obs_median,
            'n_rank1_of_5': n_rank1,
            'uniform_rank_null_mean_median': nm_med,
            'p_median_le_chance': p_median_le,
            'p_n_rank1_ge_chance': p_rank1_ge,
            'h1_eponymy_neq_centrality_holds': h1_holds,
            'reversal_eponymy_implies_centrality': reversal,
            'verdict': arm_c_verdict,
        },
        'core_episode_carrier_refinement_MW7': {
            'per_cycle_(rank,is_core_carrier)': carrier_ranks,
            'note': 'Pre-committed mechanism: core-episode carriers rank high, variant/allusive eponyms rank low. Descriptive, MW-7-capped.',
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    # ---- console report ----
    print(f"\nArm B Bonferroni α = 0.05/{BONFERRONI_K} = {ALPHA_BON}\n")
    for cyc in ('NUH', 'IBRAHIM', 'HUD', 'MARYAM', 'YUNUS'):
        r = results[cyc]
        b = r['arm_B_anchor_swap']
        print(f"=== {cyc} — eponymous {r['eponymous_pericope']} (core-carrier={r['core_episode_carrier']}) ===")
        for row in r['centrality_table']:
            mark = '  <-- EPONYMOUS' if row['pericope'] == r['eponymous_pericope'] else ''
            print(f"  rank {row['rank']}  {row['pericope']:14s} mean_J={row['mean_jaccard']:.5f}{mark}")
        print(f"  centroid = {r['centroid_pericope']}; eponymous rank = {r['eponymous_rank']}/{r['n_pericopes']} -> Arm A {r['arm_A_label']}")
        print(f"  Arm B: obs={b['eponymous_observed_centrality']:.5f} null_mean={b['null_mean']:.5f} "
              f"z={b['z']:+.3f} p_perm={b['p_perm_one_sided_greater']:.4f} -> {b['verdict']}\n")
    c = out['arm_C_cross_cycle_law']
    print(f"=== Arm C — cross-cycle law ===")
    print(f"  eponymous ranks: {c['eponymous_ranks']}")
    print(f"  cycle sizes:     {c['cycle_sizes']}")
    print(f"  observed median rank = {c['observed_median_rank']} (uniform-null mean median {c['uniform_rank_null_mean_median']:.3f})")
    print(f"  rank-1 count = {c['n_rank1_of_5']}/5")
    print(f"  p(median <= chance) = {c['p_median_le_chance']:.4f}   p(#rank1 >= chance) = {c['p_n_rank1_ge_chance']:.4f}")
    print(f"  VERDICT: {c['verdict']}")
    print(f"\nMūsā control (non-eponymous core hub): Q20 hub-rank in {musa['hub_rank_descending']}")
    print(f"Result written to {OUT}")


if __name__ == '__main__':
    main()
