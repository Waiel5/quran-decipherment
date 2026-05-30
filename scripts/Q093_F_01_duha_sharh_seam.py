#!/usr/bin/env python3
"""Q093-F-01 — al-Ḍuḥā ↔ al-Sharḥ seam scale-dissociation (Arm A) +
favor→command orphan-recall (Arm B).

Pre-reg: surahs/Q093-al-duha/Q093-F-01-duha-sharh-seam-prereg.md
Pre-reg SHA256: 2e384496b1c2e27463135e579918d91f2dc12028276e82f4dc9f08b81be41eed
Rules-tuple: (no-tashkeel, orthographic-token, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

Arm A: the classically-claimed Q93/Q94 pairing is whole-surah-FR-driven (A-H1 FR top-5; A-H2 TSP seam
       top-15 smoothest) but NOT boundary-pericope-lexical (A-H3 seam root-Jaccard <= corpus mean at
       k=3 AND k=5; A-H4 percentile <= 90th). Direction-locked dissociation.
Arm B: wjd-anaphora over favor-block vv6-8 (B-H1); ytm is the UNIQUE root bridging favor-block (vv6-8)
       and command-block (vv9-11), v6->v9 (B-H2); corpus census of ytm favor->command recall (B-H3).

QAC roots loaded via the H-NEW-2280 convention (first ROOT per segment from the QAC v0.4 morphology
TXT) so the seam-Jaccard reproduces H-NEW-2280's published Q93->Q94 value exactly.
"""
import json
import hashlib
import sys
import os
import random
from collections import defaultdict

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs/Q093-al-duha/Q093-F-01-duha-sharh-seam-prereg.md')
EXPECTED_SHA = '2e384496b1c2e27463135e579918d91f2dc12028276e82f4dc9f08b81be41eed'
SEED = 20260509
N_PERM = 10000
K_VALUES = [3, 5]
N_SURAHS = 114
OUT_PATH = os.path.join(ROOT, 'surahs/Q093-al-duha/csv/Q093-F-01.json')

MORPH = os.path.join(ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN = os.path.join(ROOT, 'quran-text/quran-no-tashkeel.json')
FR_JSON = os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-111.json')
TSP_JSON = os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-720.json')


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)
    print(f"SHA OK: {actual}")


def load_qac_roots_by_verse():
    """{(surah, verse): set(ROOT)} — H-NEW-2280 convention (first ROOT per segment)."""
    verse_roots = defaultdict(set)
    with open(MORPH, 'r', encoding='utf-8') as f:
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
                    verse_roots[(s, v)].add(tok[len('ROOT:'):])
                    break
    return dict(verse_roots)


def jaccard(a, b):
    u = a | b
    return len(a & b) / len(u) if u else 0.0


def main():
    verify_sha()
    text = json.load(open(QURAN))
    lengths = {int(s['id']): len(s['verses']) for s in text}
    verse_roots = load_qac_roots_by_verse()

    # ---------- ARM A ----------
    # A-H1: Q94 rank in Q93's FR list
    fr = json.load(open(FR_JSON))
    tri = fr['D_matrix_upper_triangular']
    d93 = {}
    for i, j, dd in tri:
        if i == 93:
            d93[j] = dd
        elif j == 93:
            d93[i] = dd
    fr_ranked = sorted(d93.items(), key=lambda x: x[1])
    fr_ids = [s for s, _ in fr_ranked]
    q94_fr_rank = fr_ids.index(94) + 1
    q94_fr_dist = d93[94]
    q92_fr_rank = fr_ids.index(92) + 1
    mean_fr_93 = sum(d93.values()) / len(d93)
    A_H1 = (q94_fr_rank <= 5)

    # A-H2: Q93->Q94 TSP seam ascending-rank
    tsp = json.load(open(TSP_JSON))
    pa = tsp['per_adjacency']
    order = sorted(pa, key=lambda x: x['delta_raw'])
    seam_rank = {e['s']: r for r, e in enumerate(order, 1)}
    q93_seam = next(e for e in pa if e['s'] == 93)
    q93_seam_rank = seam_rank[93]
    A_H2 = (q93_seam_rank <= 15)

    # A-H3 / A-H4: boundary-pericope seam Jaccard at k=3, k=5 (H-NEW-2280 method)
    def pericope_last(sid, k):
        kk = min(k, lengths[sid])
        out = set()
        for v in range(lengths[sid] - kk + 1, lengths[sid] + 1):
            out |= verse_roots.get((sid, v), set())
        return out

    def pericope_first(sid, k):
        kk = min(k, lengths[sid])
        out = set()
        for v in range(1, kk + 1):
            out |= verse_roots.get((sid, v), set())
        return out

    seam_results = {}
    for k in K_VALUES:
        last_roots = {sid: pericope_last(sid, k) for sid in range(1, N_SURAHS + 1)}
        first_roots = {sid: pericope_first(sid, k) for sid in range(1, N_SURAHS + 1)}
        # observed 113 seams
        obs = []
        for N in range(1, N_SURAHS):
            obs.append((N, jaccard(last_roots[N], first_roots[N + 1])))
        corpus_mean = sum(j for _, j in obs) / len(obs)
        j_9394 = jaccard(last_roots[93], first_roots[94])
        # percentile of Q93->Q94 among real seams
        n_le = sum(1 for _, j in obs if j <= j_9394)
        pct_rank = 100.0 * n_le / len(obs)
        # H-NEW-2280 null (random non-adjacent pairing)
        rng = random.Random(SEED)
        all_ids = list(range(1, N_SURAHS + 1))
        null_means = []
        for _ in range(N_PERM):
            vals = []
            for _draw in range(N_SURAHS - 1):
                a = rng.choice(all_ids)
                while True:
                    b = rng.choice(all_ids)
                    if b != a and b != a + 1:
                        break
                vals.append(jaccard(last_roots[a], first_roots[b]))
            null_means.append(sum(vals) / len(vals))
        nm = sum(null_means) / len(null_means)
        seam_results[f'k{k}'] = {
            'k': k,
            'j_Q93_Q94': j_9394,
            'shared_roots_seam': sorted(last_roots[93] & first_roots[94]),
            'n_last_roots_Q93': len(last_roots[93]),
            'n_first_roots_Q94': len(first_roots[94]),
            'corpus_mean_seam_J': corpus_mean,
            'null_mean_seam_J': nm,
            'Q93Q94_percentile_among_real_seams': pct_rank,
            'A_H3_le_corpus_mean': (j_9394 <= corpus_mean),
        }
    A_H3 = seam_results['k3']['A_H3_le_corpus_mean'] and seam_results['k5']['A_H3_le_corpus_mean']
    A_H4 = (seam_results['k3']['Q93Q94_percentile_among_real_seams'] <= 90.0)

    a_pass = sum([A_H1, A_H2, A_H3, A_H4])
    # pre-commit violation: whole-surah claims reversed, OR boundary lexis STRONG (A-H3 reversed)
    a_violation = (not A_H1) or (not A_H2) or (
        (seam_results['k3']['j_Q93_Q94'] > seam_results['k3']['corpus_mean_seam_J']) and
        (seam_results['k5']['j_Q93_Q94'] > seam_results['k5']['corpus_mean_seam_J']))
    if a_violation:
        armA_verdict = 'NULL (pre-commit violation)'
    elif a_pass == 4:
        armA_verdict = 'CONFIRMED (scale-dissociation)'
    elif a_pass == 3:
        armA_verdict = 'DIRECTIONAL'
    else:
        armA_verdict = 'NULL'

    # ---------- ARM B ----------
    # B-H1: wjd over favor block vv6-8 only
    wjd_verses = [v for v in range(1, lengths[93] + 1) if 'wjd' in verse_roots.get((93, v), set())]
    B_H1 = (wjd_verses == [6, 7, 8])

    favor_block = set()
    for v in (6, 7, 8):
        favor_block |= verse_roots.get((93, v), set())
    command_block = set()
    for v in (9, 10, 11):
        command_block |= verse_roots.get((93, v), set())
    bridge = sorted(favor_block & command_block)
    B_H2 = (len(bridge) == 1 and bridge[0] == 'ytm')

    # B-H3: corpus census — surahs where ytm appears in >=2 verses AND at least one is an imperative
    # (operationalized deterministically: count surahs where ytm root appears in >=2 distinct verses).
    ytm_by_surah = defaultdict(list)
    for (s, v), roots in verse_roots.items():
        if 'ytm' in roots:
            ytm_by_surah[s].append(v)
    ytm_multi = {s: sorted(vs) for s, vs in ytm_by_surah.items() if len(set(vs)) >= 2}
    ytm_total_surahs = len(ytm_by_surah)
    # specifically: ytm in adjacent-or-same favor/command pattern within Q93 = v6 and v9
    q93_ytm_verses = sorted(set(ytm_by_surah.get(93, [])))

    armB_verdict = 'CONFIRMED' if (B_H1 and B_H2) else 'NULL'

    out = {
        'test_id': 'Q093-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'arm_A': {
            'A_H1_Q94_FR_rank': q94_fr_rank,
            'A_H1_Q94_FR_dist': q94_fr_dist,
            'A_H1_pass_top5': A_H1,
            'Q92_FR_rank': q92_fr_rank,
            'Q93_mean_FR': mean_fr_93,
            'A_H2_Q93Q94_TSP_seam_delta_raw': q93_seam['delta_raw'],
            'A_H2_Q93Q94_TSP_ascending_rank': q93_seam_rank,
            'A_H2_pass_top15_smoothest': A_H2,
            'seam_jaccard_by_k': seam_results,
            'A_H3_seam_le_corpus_mean_both_k': A_H3,
            'A_H4_percentile_le_90_k3': A_H4,
            'A_passes': a_pass,
            'pre_commit_violation': a_violation,
            'verdict': armA_verdict,
        },
        'arm_B': {
            'B_H1_wjd_verses': wjd_verses,
            'B_H1_pass': B_H1,
            'favor_block_roots_vv6_8': sorted(favor_block),
            'command_block_roots_vv9_11': sorted(command_block),
            'bridge_roots': bridge,
            'B_H2_unique_bridge_is_ytm': B_H2,
            'B_H3_ytm_total_surahs': ytm_total_surahs,
            'B_H3_ytm_multi_verse_surahs': ytm_multi,
            'B_H3_Q93_ytm_verses': q93_ytm_verses,
            'verdict': armB_verdict,
        },
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("\n===== Q093-F-01 RESULTS =====")
    print(f"ARM A: A-H1 Q94 FR rank={q94_fr_rank} (dist {q94_fr_dist:.4f}) top5={A_H1} | Q92 rank={q92_fr_rank}")
    print(f"       A-H2 Q93->Q94 TSP delta_raw={q93_seam['delta_raw']:.5f} asc-rank={q93_seam_rank}/113 top15={A_H2}")
    for k in K_VALUES:
        r = seam_results[f'k{k}']
        print(f"       A-H3 k={k}: J(Q93->Q94)={r['j_Q93_Q94']:.4f} vs corpus_mean={r['corpus_mean_seam_J']:.4f} "
              f"null={r['null_mean_seam_J']:.4f} pct={r['Q93Q94_percentile_among_real_seams']:.1f} le_mean={r['A_H3_le_corpus_mean']}")
    print(f"       A-H3(both k)={A_H3}  A-H4(pct<=90)={A_H4}  -> ARM A {armA_verdict} ({a_pass}/4)")
    print(f"ARM B: B-H1 wjd verses={wjd_verses} (=[6,7,8]?) {B_H1}")
    print(f"       B-H2 favor∩command bridge={bridge} (=ytm only?) {B_H2}")
    print(f"       B-H3 ytm total surahs={ytm_total_surahs}; multi-verse-ytm surahs={list(ytm_multi.keys())}; Q93 ytm verses={q93_ytm_verses}")
    print(f"       -> ARM B {armB_verdict}")
    print(f"\nWrote {OUT_PATH}")


if __name__ == '__main__':
    main()
