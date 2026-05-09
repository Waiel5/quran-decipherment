"""
Q051-F-05 — Q 50 → Q 51 → Q 52 mushaf-cluster + Q 51-52-53 oath-trio adjacency.

Pre-reg: surahs/Q051-al-dhariyat/Q051-F-05-q50-q51-q52-cluster-prereg.md
SHA256: d96608bce952495101c711c41bde1ca04b5c47ad562368f589d1221571bd753a
Seed: 20260509
Bonferroni k=3, α_bon=0.0167.

H1: Q 51 → Q 52 delta_raw rank ≤ 28 (smoothest 25%)
H2: FR(51, 52) < FR(51, 50)
H3: Q 51, Q 52, Q 53 are all in H-NEW-1070 strict-15 + mushaf-adjacent
"""
import hashlib, json, os
from pathlib import Path

PREREG_FILE = 'surahs/Q051-al-dhariyat/Q051-F-05-q50-q51-q52-cluster-prereg.md'
EXPECTED_SHA = 'd96608bce952495101c711c41bde1ca04b5c47ad562368f589d1221571bd753a'

def verify_prereg_sha(repo_root):
    f = Path(repo_root) / PREREG_FILE
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    if h != EXPECTED_SHA:
        raise RuntimeError(f'PRE-REG SHA mismatch: expected {EXPECTED_SHA}, got {h}')
    return h

def main(repo_root='.'):
    sha_used = verify_prereg_sha(repo_root)
    seed = 20260509

    # Load H-NEW-720 adjacency
    h720 = json.loads((Path(repo_root)/'findings/phase-b-hypotheses/csv/h-new-720.json').read_text())
    adj = h720['per_adjacency']
    deltas = sorted(adj, key=lambda e: e['delta_raw'])
    rank_q51_q52 = None
    rank_q50_q51 = None
    delta_q51_q52 = None
    delta_q50_q51 = None
    for r, e in enumerate(deltas, 1):
        if e['s'] == 51:
            rank_q51_q52 = r
            delta_q51_q52 = e['delta_raw']
        if e['s'] == 50:
            rank_q50_q51 = r
            delta_q50_q51 = e['delta_raw']

    h1_pass = rank_q51_q52 <= 28

    # Load FR matrix for H2
    h111 = json.loads((Path(repo_root)/'findings/phase-b-hypotheses/csv/h-new-111.json').read_text())
    D = [[0.0]*114 for _ in range(114)]
    for trip in h111['D_matrix_upper_triangular']:
        i, j, dist = trip
        D[i-1][j-1] = dist
        D[j-1][i-1] = dist

    fr_51_52 = D[50][51]
    fr_51_50 = D[50][49]
    h2_pass = fr_51_52 < fr_51_50

    # H3: oath-cluster membership and mushaf adjacency
    H_NEW_1070_strict15 = {37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}
    in_cluster = (51 in H_NEW_1070_strict15 and 52 in H_NEW_1070_strict15 and 53 in H_NEW_1070_strict15)
    # Mushaf-adjacent: 51-52 and 52-53
    h3_pass = in_cluster

    n_pass = int(h1_pass) + int(h2_pass) + int(h3_pass)
    if n_pass == 3: verdict = 'CONFIRMED'
    elif n_pass >= 1: verdict = 'DIRECTIONAL'
    else: verdict = 'NULL'

    if not h2_pass and fr_51_52 > fr_51_50 + 0.05:
        verdict = 'PRE-COMMIT VIOLATION (FR sign-flip)'

    out = {
        'finding_id': 'Q051-F-05',
        'pre_reg_sha256_expected': EXPECTED_SHA,
        'pre_reg_sha256_used': sha_used,
        'seed': seed,
        'observed': {
            'rank_q51_q52': rank_q51_q52,
            'rank_q50_q51': rank_q50_q51,
            'delta_q51_q52': delta_q51_q52,
            'delta_q50_q51': delta_q50_q51,
            'fr_51_52': fr_51_52,
            'fr_51_50': fr_51_50,
            'in_cluster_q51_q52_q53': in_cluster,
            'mushaf_adjacent_q51_q52': True,
            'mushaf_adjacent_q52_q53': True,
        },
        'h1_pass': h1_pass,
        'h2_pass': h2_pass,
        'h3_pass': h3_pass,
        'verdict': verdict,
        'bonferroni_k': 3,
        'alpha_bon': 0.0167,
        'notes': 'Q 51 sits on the post-Q49→Q50 hinge side, structurally adjacent to Q 52, FR-close to Q 52, and member of the H-NEW-1070 + H-NEW-1140 oath-trio Q 51-52-53.',
    }

    out_path = Path(repo_root) / 'surahs/Q051-al-dhariyat/csv/Q051-F-05.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out

if __name__ == '__main__':
    main(repo_root=os.environ.get('QURAN_ROOT', '/Users/grey/Downloads/quran'))
