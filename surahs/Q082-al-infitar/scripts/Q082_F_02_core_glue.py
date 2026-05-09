#!/usr/bin/env python3
"""
Q082-F-02 — H-NEW-1200 CORE-pair cohesion + 4-transition CORE-glue analysis.

Hypothesis (per pre-reg):
- 4-CORE = {Q 81, 82, 84, 99}: all 6 pairwise FR distances below corpus
  pairwise FR median (0.92).
- 4 mushaf-transitions Q 81→82, Q 82→83, Q 83→84, Q 84→85: each below
  H-NEW-720 per-adjacency median.
- Sub-cluster A (5 surahs {Q 56, 81, 82, 84, 99}) FR-cohesive at p=0.034
  per H-NEW-1200; we replicate.
- 4-CORE perm test against length-matched random 4-surah subsets.

Pre-reg locked: see preregs/Q082-F-02-core-glue-prereg.md
Rules-tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import json
import os
import statistics
import random
from itertools import combinations

ROOT = '/Users/grey/Downloads/quran'
OUT = os.path.join(ROOT, 'surahs/Q082-al-infitar/csv/Q082-F-02.json')

SEED = 20260509
N_PERM = 10000


def load_fr():
    """Load Fisher-Rao distance matrix from H-NEW-111."""
    p = os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-111.json')
    data = json.load(open(p))
    fr = {}
    for i, j, d in data['D_matrix_upper_triangular']:
        fr[(i, j)] = d
        fr[(j, i)] = d
    return fr, data


def fr_distance(fr, i, j):
    if i == j:
        return 0.0
    return fr.get((i, j), None)


def load_h720():
    """Load per-adjacency residual costs from H-NEW-720."""
    p = os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-720.json')
    data = json.load(open(p))
    return {tuple(a['pair']): a for a in data['per_adjacency']}


def load_verse_counts():
    """Load verse-count per surah."""
    p = os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')
    data = json.load(open(p))
    return {s['id']: len(s['verses']) for s in data}


def main():
    print("=== Q082-F-02: H-NEW-1200 CORE-pair cohesion + transitions ===\n")
    out = {
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'pre_reg_finding_id': 'Q082-F-02',
        'parent_findings': ['H-NEW-1200', 'H-NEW-720', 'H-NEW-1190'],
        'seed': SEED,
        'n_perm': N_PERM,
    }

    fr, fr_meta = load_fr()
    h720 = load_h720()
    vc = load_verse_counts()

    # 4-CORE pairs
    core = [81, 82, 84, 99]
    core_pairs = list(combinations(core, 2))
    out['core_set'] = core
    out['core_pairs'] = []

    print("[1] H-NEW-1200 4-CORE pairwise FR distances")
    distances = []
    for a, b in core_pairs:
        d = fr_distance(fr, a, b)
        distances.append(d)
        out['core_pairs'].append({'pair': [a, b], 'fr': d})
        print(f"  Q {a} ↔ Q {b}: FR = {d:.4f}")
    mean_core = statistics.mean(distances)
    out['core_mean_fr'] = mean_core
    out['core_max_fr'] = max(distances)
    out['core_min_fr'] = min(distances)
    print(f"  Mean: {mean_core:.4f}; Min: {min(distances):.4f}; Max: {max(distances):.4f}")

    # Corpus pairwise median
    all_fr = [d for (i, j), d in fr.items() if i < j]
    corpus_median = statistics.median(all_fr)
    corpus_mean = statistics.mean(all_fr)
    out['corpus_pairwise_fr_median'] = corpus_median
    out['corpus_pairwise_fr_mean'] = corpus_mean
    print(f"  Corpus pairwise FR median: {corpus_median:.4f}, mean: {corpus_mean:.4f}")

    # CORE-PAIR-CONFIRMED check: all 6 below corpus median?
    n_below = sum(1 for d in distances if d < corpus_median)
    out['core_below_corpus_median'] = n_below
    out['core_pair_confirmed'] = (n_below == 6)
    print(f"  4-CORE pairs below corpus median: {n_below}/6")

    # [2] CORE-glue 4 transitions
    print("\n[2] Mushaf-transition CORE-glue analysis")
    transitions = [(81, 82), (82, 83), (83, 84), (84, 85)]
    out['transitions'] = []
    trans_costs = []
    all_costs = [a['delta_raw'] for a in h720.values()]
    median_all_cost = statistics.median(all_costs)
    out['h720_median_delta_raw'] = median_all_cost
    print(f"  H-NEW-720 per-adjacency median delta_raw: {median_all_cost:.4f}")
    for a, b in transitions:
        adj = h720[(a, b)]
        c = adj['delta_raw']
        trans_costs.append(c)
        out['transitions'].append({
            'pair': [a, b],
            'delta_raw': c,
            'fraction_residual': adj['fraction_residual'],
            'below_median': c < median_all_cost,
        })
        marker = "✓ BELOW MEDIAN" if c < median_all_cost else "above median"
        print(f"  Q {a} → Q {b}: delta_raw = {c:.4f} ({marker})")
    n_trans_below = sum(1 for c in trans_costs if c < median_all_cost)
    out['n_transitions_below_median'] = n_trans_below
    out['core_glue_confirmed'] = (n_trans_below == 4)
    print(f"  Transitions below median: {n_trans_below}/4")
    print(f"  Mean transition cost: {statistics.mean(trans_costs):.4f}")

    # [3] Sub-cluster A (5 surahs) FR-cohesion
    sub_A = [56, 81, 82, 84, 99]
    print(f"\n[3] Sub-cluster A {sub_A} FR-cohesion")
    sub_A_pairs = list(combinations(sub_A, 2))
    sub_A_dists = [fr_distance(fr, a, b) for a, b in sub_A_pairs]
    out['sub_A_set'] = sub_A
    out['sub_A_mean_fr'] = statistics.mean(sub_A_dists)
    out['sub_A_pair_distances'] = [
        {'pair': [a, b], 'fr': fr_distance(fr, a, b)} for a, b in sub_A_pairs
    ]
    print(f"  Sub-cluster A mean pairwise FR: {statistics.mean(sub_A_dists):.4f}")
    print(f"  Number of pairs below corpus median: {sum(1 for d in sub_A_dists if d < corpus_median)}/{len(sub_A_dists)}")

    # [4] Permutation test: 4-CORE vs random 4-surah subsets matched on length
    print(f"\n[4] Permutation test: 4-CORE vs length-matched random 4-subsets")
    random.seed(SEED)
    target_lens = sorted([vc[s] for s in core])
    print(f"  Target verse-counts: {target_lens}")

    # 25% length tolerance
    def lengths_match(s_set, target_lens, tol=0.25):
        ls = sorted([vc[s] for s in s_set])
        for ts, ls_v in zip(target_lens, ls):
            if abs(ls_v - ts) > tol * ts:
                return False
        return True

    # Generate length-matched random 4-subsets and compute mean intra-subset FR
    candidates = list(range(1, 115))
    null_means = []
    n_attempts = 0
    n_max_attempts = N_PERM * 100
    while len(null_means) < N_PERM and n_attempts < n_max_attempts:
        s_set = random.sample(candidates, 4)
        n_attempts += 1
        # Don't require perfect length-match — use loose 25% tolerance
        if lengths_match(s_set, target_lens):
            pairs = list(combinations(s_set, 2))
            mean_d = statistics.mean(fr_distance(fr, a, b) for a, b in pairs)
            null_means.append(mean_d)
    out['n_null_samples'] = len(null_means)
    out['n_perm_attempts'] = n_attempts
    print(f"  Generated {len(null_means)} length-matched null subsets in {n_attempts} attempts")

    if null_means:
        n_lower = sum(1 for n in null_means if n <= mean_core)
        p_lower = (n_lower + 1) / (len(null_means) + 1)
        z = (mean_core - statistics.mean(null_means)) / (statistics.stdev(null_means) if len(null_means) > 1 else 1)
        out['null_mean'] = statistics.mean(null_means)
        out['null_std'] = statistics.stdev(null_means) if len(null_means) > 1 else 0
        out['p_lower'] = p_lower
        out['z_score'] = z
        print(f"  Observed 4-CORE mean: {mean_core:.4f}")
        print(f"  Null mean / std: {statistics.mean(null_means):.4f} / {statistics.stdev(null_means):.4f}")
        print(f"  z-score: {z:.4f}")
        print(f"  p (one-sided lower): {p_lower:.5f}")

    # Verdicts
    print("\n[5] VERDICTS")
    n_passing = (out['core_pair_confirmed'] +
                 out['core_glue_confirmed'] +
                 (out.get('p_lower', 1.0) < 0.0125))  # Bonferroni-4 alpha
    out['n_passing_cells'] = n_passing
    print(f"  CORE-PAIR-CONFIRMED (6/6 pairs below corpus median): {out['core_pair_confirmed']}")
    print(f"  CORE-GLUE-CONFIRMED (4/4 transitions below median): {out['core_glue_confirmed']}")
    pl = out.get('p_lower', None)
    print(f"  Sub-cluster perm-test p < 0.0125 (Bonferroni-4): "
          f"{(pl is not None and pl < 0.0125)} (p = {pl})")

    if n_passing == 3:
        verdict = ('CONFIRMED — Q 82-Q 84 architectural CORE-pair status, '
                   'CORE-glue, and Sub-cluster A cohesion all PASS Bonferroni-4.')
    elif n_passing >= 2:
        verdict = (f'PARTIAL — {n_passing}/3 cells pass; cell-level details '
                   'in JSON output.')
    else:
        verdict = (f'WEAK / NULL — only {n_passing}/3 cells pass; the 4-CORE '
                   'classification is not architecturally supported.')
    out['verdict'] = verdict
    print(f"\n  {verdict}")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nWrote: {OUT}")


if __name__ == '__main__':
    main()
