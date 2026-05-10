#!/usr/bin/env python3
"""H-NEW-1570 — chronology-paired surahs inverse-rank lexical-key principle (corpus-wide).

Formalizes Q068-F-06's observation that Q 96 (rev #1) holds rank-1 by *qlm* density and
Q 68 (rev #2, title-eponymous) holds rank-2 — i.e. the chronology-adjacent pair holds
the title-lexical-key in INVERSE rank order. Tests five chronology-adjacent pairs.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1570-chronology-pair-inverse-rank.md
Pre-reg SHA256: 911bdda399a7abec7da27c32d2231b2ca4a746327881771d20ef94839054a955

Direction lock: ≥3 of 5 pairs show strict inverse-rank (rank_early=1, rank_later=2).
Seed 20260509, n_perm=10000.
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import csv
import hashlib
import json
import os
import random
import sys
from collections import defaultdict

PROJECT_ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/prereg-h-new-1570-chronology-pair-inverse-rank.md')
EXPECTED_SHA = '911bdda399a7abec7da27c32d2231b2ca4a746327881771d20ef94839054a955'

SEED = 20260509
N_PERM = 10000
ALPHA_RAW = 0.05
BONFERRONI_K = 5
ALPHA_BON = ALPHA_RAW / BONFERRONI_K  # 0.01

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
REVELATION = os.path.join(PROJECT_ROOT, 'data/revelation-order.csv')
OUT_JSON = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/csv/h-new-1570.json')

# LOCKED five chronology-adjacent pairs. Each = (early_rev_n, later_rev_n+1, early_mushaf, later_mushaf, root, label).
LOCKED_PAIRS = [
    {'rev_early': 1,  'rev_later': 2,  'early': 96, 'later': 68,  'root': 'qlm', 'label': 'Q96 al-Alaq (rev#1) -> Q68 al-Qalam (rev#2) [qlm]'},
    {'rev_early': 3,  'rev_later': 4,  'early': 73, 'later': 74,  'root': 'dvr', 'label': 'Q73 al-Muzzammil (rev#3) -> Q74 al-Muddaththir (rev#4) [dvr]'},
    {'rev_early': 5,  'rev_later': 6,  'early': 1,  'later': 111, 'root': 'msd', 'label': 'Q1 al-Fatiha (rev#5) -> Q111 al-Masad (rev#6) [msd]'},
    {'rev_early': 7,  'rev_later': 8,  'early': 81, 'later': 87,  'root': 'Elw', 'label': 'Q81 al-Takwir (rev#7) -> Q87 al-Aala (rev#8) [Elw]'},
    {'rev_early': 11, 'rev_later': 12, 'early': 93, 'later': 94,  'root': '$rH', 'label': 'Q93 al-Duha (rev#11) -> Q94 al-Sharh (rev#12) [$rH]'},
]


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def verify_chronology():
    """Reverify the 5 chronology-adjacent pairs against revelation-order.csv."""
    rev_to_mushaf = {}
    with open(REVELATION, encoding='utf-8') as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            rev_to_mushaf[int(row['revelation_order'])] = int(row['mushaf_order'])
    for p in LOCKED_PAIRS:
        e_csv = rev_to_mushaf.get(p['rev_early'])
        l_csv = rev_to_mushaf.get(p['rev_later'])
        if e_csv != p['early'] or l_csv != p['later']:
            print(f"FAIL: chronology reverify mismatch for pair {p['label']}\n"
                  f"  expected (rev#{p['rev_early']}={p['early']}, rev#{p['rev_later']}={p['later']})\n"
                  f"  actual   (rev#{p['rev_early']}={e_csv}, rev#{p['rev_later']}={l_csv})", file=sys.stderr)
            sys.exit(1)


def load_qac_root_counts():
    """Returns:
      surah_total[s] = total QAC root-tokens in surah s
      surah_root[(s,R)] = count of ROOT:R tokens in surah s
    """
    surah_total = defaultdict(int)
    surah_root = defaultdict(int)
    with open(MORPH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            loc_clean = loc.strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc_clean.split(':'))
            except ValueError:
                continue
            root = None
            for tok in features.split('|'):
                if tok.startswith('ROOT:'):
                    root = tok[len('ROOT:'):]
                    break
            if root is None:
                continue
            surah_total[s] += 1
            surah_root[(s, root)] += 1
    return dict(surah_total), dict(surah_root)


def rank_surahs_by_density(root, surah_total, surah_root):
    """Rank all 114 surahs by density of ROOT:root descending.
    Tie-breaking: by raw count desc, then by surah number ascending.
    Returns: dict {surah -> rank (1-indexed)} and dict {surah -> (count, density)}.
    """
    info = {}
    for s in range(1, 115):
        n = surah_total.get(s, 0)
        k = surah_root.get((s, root), 0)
        dens = (k / n * 1000.0) if n > 0 else 0.0
        info[s] = (k, dens)
    # Sort: density desc, count desc, surah asc
    ordered = sorted(range(1, 115), key=lambda s: (-info[s][1], -info[s][0], s))
    rank = {s: i + 1 for i, s in enumerate(ordered)}
    return rank, info, ordered


def check_inverse_rank_strict(rank_early, rank_later, dens_early, dens_later):
    """Strict criterion: rank_early=1, rank_later=2, dens_early > dens_later."""
    return (rank_early == 1 and rank_later == 2 and dens_early > dens_later)


def check_inverse_rank_loose(rank_early, rank_later, dens_early, dens_later):
    """Loose secondary criterion: rank_early < rank_later AND both in top-5 AND dens_early > dens_later."""
    return (rank_early < rank_later and rank_early <= 5 and rank_later <= 5 and dens_early > dens_later)


def main():
    verify_sha()
    verify_chronology()
    surah_total, surah_root = load_qac_root_counts()

    per_pair = []
    n_strict = 0
    n_loose = 0
    for p in LOCKED_PAIRS:
        root = p['root']
        rank, info, ordered = rank_surahs_by_density(root, surah_total, surah_root)
        ce, de = info[p['early']]
        cl, dl = info[p['later']]
        re_ = rank[p['early']]
        rl = rank[p['later']]
        strict = check_inverse_rank_strict(re_, rl, de, dl)
        loose = check_inverse_rank_loose(re_, rl, de, dl)
        if strict:
            n_strict += 1
        if loose:
            n_loose += 1
        # Top-5 of the ranking for transparency
        top5 = [{'surah': s, 'rank': rank[s], 'count': info[s][0], 'density_per1000': info[s][1]} for s in ordered[:5]]
        per_pair.append({
            'pair_label': p['label'],
            'rev_early': p['rev_early'],
            'rev_later': p['rev_later'],
            'early_surah': p['early'],
            'later_surah': p['later'],
            'root': root,
            'corpus_total_tokens_for_root': sum(surah_root.get((s, root), 0) for s in range(1, 115)),
            'early': {'count': ce, 'total_root_tokens': surah_total.get(p['early'], 0), 'density_per1000': de, 'rank': re_},
            'later': {'count': cl, 'total_root_tokens': surah_total.get(p['later'], 0), 'density_per1000': dl, 'rank': rl},
            'inverse_rank_strict': strict,
            'inverse_rank_loose': loose,
            'top5_by_density': top5,
        })

    # Permutation null: for each perm, draw 5 random ordered pairs (a, b) with a != b from {1..114},
    # using the same locked root for each pair. Count satisfaction.
    rng = random.Random(SEED)
    surahs = list(range(1, 115))
    # Pre-compute per-root ranks and density info (these are corpus-wide facts)
    root_to_rank_info = {}
    for p in LOCKED_PAIRS:
        r = p['root']
        if r not in root_to_rank_info:
            rank, info, ordered = rank_surahs_by_density(r, surah_total, surah_root)
            root_to_rank_info[r] = (rank, info)

    null_n_strict = []
    null_n_loose = []
    for _ in range(N_PERM):
        ns = 0
        nl = 0
        for p in LOCKED_PAIRS:
            r = p['root']
            rank, info = root_to_rank_info[r]
            a, b = rng.sample(surahs, 2)
            de = info[a][1]
            dl = info[b][1]
            re_ = rank[a]
            rl = rank[b]
            if check_inverse_rank_strict(re_, rl, de, dl):
                ns += 1
            if check_inverse_rank_loose(re_, rl, de, dl):
                nl += 1
        null_n_strict.append(ns)
        null_n_loose.append(nl)

    p_strict = sum(1 for x in null_n_strict if x >= n_strict) / N_PERM
    p_loose = sum(1 for x in null_n_loose if x >= n_loose) / N_PERM

    direction_match_strict = n_strict >= 3
    pre_commit_violation = (
        n_strict == 0 and
        all(per_pair[i]['later']['rank'] == 1 for i in range(5))
    )

    if pre_commit_violation:
        verdict = 'PRE-COMMIT-VIOLATION (NULL with prominence)'
    elif direction_match_strict and p_strict < ALPHA_BON:
        verdict = 'PASS-DIRECTED'
    elif direction_match_strict:
        verdict = 'DIRECTIONAL'
    elif n_strict == 2:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'H-NEW-1570',
        'title': 'Chronology-paired surahs inverse-rank lexical-key principle (corpus-wide formalization)',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'bonferroni_k': BONFERRONI_K,
        'alpha_raw': ALPHA_RAW,
        'alpha_bon': ALPHA_BON,
        'parent_finding': 'Q068-F-06 (Q 96 rank-1, Q 68 rank-2 by qlm density)',
        'n_pairs_tested': len(LOCKED_PAIRS),
        'per_pair': per_pair,
        'n_strict_inverse_rank_observed': n_strict,
        'n_loose_inverse_rank_observed': n_loose,
        'p_strict_perm': p_strict,
        'p_loose_perm': p_loose,
        'null_strict_mean': sum(null_n_strict) / len(null_n_strict),
        'null_strict_max': max(null_n_strict),
        'null_strict_min': min(null_n_strict),
        'null_loose_mean': sum(null_n_loose) / len(null_n_loose),
        'direction_locked': 'POSITIVE — >= 3 of 5 pairs strict inverse-rank',
        'direction_match_strict': direction_match_strict,
        'verdict': verdict,
        'corpus_principle_status': (
            'Q068-F-06 is the ONLY pair satisfying the strict inverse-rank pattern; '
            'principle is NOT corpus-wide. Q068-F-06 isolated finding.'
            if n_strict <= 1 else
            f'{n_strict}/5 pairs satisfy strict inverse-rank; principle may extend beyond Q068-F-06.'
        ),
    }
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"=== H-NEW-1570 ===")
    for r in per_pair:
        print(f"  {r['pair_label']}")
        print(f"    early Q{r['early_surah']} root={r['root']} count={r['early']['count']} dens={r['early']['density_per1000']:.4f} rank={r['early']['rank']}")
        print(f"    later Q{r['later_surah']} root={r['root']} count={r['later']['count']} dens={r['later']['density_per1000']:.4f} rank={r['later']['rank']}")
        print(f"    inverse_rank_strict={r['inverse_rank_strict']}  inverse_rank_loose={r['inverse_rank_loose']}")
    print(f"\nn_strict_observed = {n_strict}/5   (threshold for PASS: >=3)")
    print(f"n_loose_observed  = {n_loose}/5")
    print(f"perm p (strict, >= obs) = {p_strict:.4f}   alpha_bon = {ALPHA_BON}")
    print(f"perm p (loose, >= obs)  = {p_loose:.4f}")
    print(f"null mean strict        = {sum(null_n_strict)/len(null_n_strict):.4f}")
    print(f"VERDICT: {verdict}")


if __name__ == '__main__':
    main()
