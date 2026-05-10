#!/usr/bin/env python3
"""Q035-F-04 — Q 34 -> Q 35 canonical-adjacency transition cost test.

Pre-reg: surahs/Q035-fatir/preregs/Q035-F-04-q34-q35-transition-prereg.md
Pre-reg SHA256: a21dc6694c6202565fb3b00454f4f7829407faf27b010b74b937d7293ab29d75
Rules-tuple: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, mushaf order, Hafs-Kufan)

H1: rank_delta(Q34->Q35) <= 15 / 113 (top-15 smoothest).
H2: cost(Q34->Q35) < median{cost(Q1->Q2), cost(Q5->Q6), cost(Q17->Q18), cost(Q33->Q34), cost(Q35->Q36)}.
H3: 3 of 4 architectural cells match between Q34 and Q35.
Bonferroni k=3, alpha_bon=0.0167.
"""
import json, hashlib, sys, os, statistics

PREREG = '/Users/grey/Downloads/quran/surahs/Q035-fatir/preregs/Q035-F-04-q34-q35-transition-prereg.md'
EXPECTED_SHA = 'a21dc6694c6202565fb3b00454f4f7829407faf27b010b74b937d7293ab29d75'
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
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json') as f:
        d720 = json.load(f)
    pa = d720['per_adjacency']

    pa_sorted = sorted(pa, key=lambda e: e['delta_raw'])
    rank_seam = None
    delta_q34_q35 = None
    for rk, e in enumerate(pa_sorted, 1):
        if e['pair'] == [34, 35]:
            rank_seam = rk
            delta_q34_q35 = e['delta_raw']
            break

    h1_pass = rank_seam is not None and rank_seam <= 15

    # H2: comparison set per prereg: {Q1->Q2, Q5->Q6, Q17->Q18, Q33->Q34, Q35->Q36}
    targets = [[1,2], [5,6], [17,18], [33,34], [35,36]]
    costs = {}
    for e in pa:
        for t in targets:
            if e['pair'] == t:
                costs[tuple(t)] = e['delta_raw']
    cost_values = list(costs.values())
    median_5 = statistics.median(cost_values) if cost_values else None
    h2_pass = (delta_q34_q35 is not None) and (median_5 is not None) and (delta_q34_q35 < median_5)

    # H3: 4 architectural cells
    # Cell A: rhyme-letter match (Q34 top=ن, Q35 top=ر) -> NO
    # Cell B: length-class match (both Late-Meccan; Q34=54 verses, Q35=45 verses; both medium) -> YES
    # Cell C: mean-content-distance similar (Q34=0.9877, Q35~0.971; difference < 0.05) -> YES
    # Cell D: FR-top-5-neighbor reciprocity (is each in the other's top-5?)
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json') as f:
        d111 = json.load(f)
    ut = d111['D_matrix_upper_triangular']
    N = 114
    mat = [[0.0]*N for _ in range(N)]
    for entry in ut:
        i, j, v = entry
        mat[i-1][j-1] = v
        mat[j-1][i-1] = v

    def top_k(s_idx, k=5):
        nbrs = []
        for j in range(N):
            if j == s_idx: continue
            nbrs.append((j+1, mat[s_idx][j]))
        nbrs.sort(key=lambda x: x[1])
        return nbrs[:k]

    top5_q34 = top_k(33, 5)
    top5_q35 = top_k(34, 5)
    q34_in_q35_top5 = any(s == 34 for s, _ in top5_q35)
    q35_in_q34_top5 = any(s == 35 for s, _ in top5_q34)
    cell_D = q34_in_q35_top5 and q35_in_q34_top5  # mutual top-5

    # Cell A: rhyme top-letter
    # Q34 top-final = ن (40.7%); Q35 top = ر (64.4%). Different -> cell A = FALSE
    cell_A = False
    # Cell B: both Late-Meccan, medium-length -> TRUE
    cell_B = True
    # Cell C: mean content distance similar. We compute mean FR per surah.
    mean_q34 = sum(mat[33]) / 113.0
    mean_q35 = sum(mat[34]) / 113.0
    # Note: dividing by 113 includes the self-distance 0, so this is mean across all 114 including self.
    # More accurate: exclude self.
    mean_q34 = sum(mat[33][j] for j in range(N) if j != 33) / 113.0
    mean_q35 = sum(mat[34][j] for j in range(N) if j != 34) / 113.0
    cell_C = abs(mean_q34 - mean_q35) < 0.05

    cells = {'rhyme_letter': cell_A, 'length_class': cell_B, 'mean_content_dist': cell_C, 'fr_top5_reciprocity': cell_D}
    n_cells_pass = sum(cells.values())
    h3_pass = n_cells_pass >= 3

    n_pass = sum([h1_pass, h2_pass, h3_pass])
    if n_pass == 3: verdict = 'CONFIRMED'
    elif n_pass == 2: verdict = 'DIRECTIONAL'
    elif n_pass == 1: verdict = 'DIRECTIONAL-WEAK'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q035-F-04',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, QAC-STEM root tokens, QAC v0.4, mushaf order, Hafs-Kufan)',
        'seed': SEED,
        'alpha_bon': ALPHA_BON,
        'h1_seam_top15': {
            'delta_q34_q35': delta_q34_q35,
            'rank': rank_seam,
            'threshold': 15,
            'pass': h1_pass,
        },
        'h2_opener_median_cost': {
            'comparison_set': [{'pair': list(k), 'delta_raw': v} for k, v in costs.items()],
            'median_5': median_5,
            'delta_q34_q35': delta_q34_q35,
            'pass': h2_pass,
        },
        'h3_architectural_cells': {
            'cells': cells,
            'n_cells_pass': n_cells_pass,
            'q34_top_final_letter': 'ن',
            'q35_top_final_letter': 'ر',
            'mean_q34': mean_q34,
            'mean_q35': mean_q35,
            'fr_top5_q34': [{'surah': s, 'fr': d} for s, d in top5_q34],
            'fr_top5_q35': [{'surah': s, 'fr': d} for s, d in top5_q35],
            'pass': h3_pass,
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'Pre-flight: rank 65/113, NOT top-15; H1 will FAIL. H3 likely passes B+C; cell D depends on top-5 reciprocity (likely false at top-5).',
    }

    print('=== Q035-F-04 Q34->Q35 transition test ===')
    print(f'H1: delta={delta_q34_q35:.4f}, rank={rank_seam}/113, top-15? {h1_pass}')
    print(f'H2: median_5={median_5:.4f}, q34-q35={delta_q34_q35:.4f}; pass={h2_pass}')
    print(f'H3 cells: {cells} -> {n_cells_pass}/4 cells, pass(>=3)? {h3_pass}')
    print(f'\nN pass: {n_pass}/3 -> {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv/Q035-F-04.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
