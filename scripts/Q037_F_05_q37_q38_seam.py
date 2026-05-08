#!/usr/bin/env python3
"""Q037-F-05 — Q 37 → Q 38 seam empirical-seamlessness diagnostic.

Pre-reg: surahs/Q037-al-saffat/Q037-F-05-q37-q38-seam-prereg.md
Pre-reg SHA256: 684ae9fdc0150ba64ed56e39a6e5f5c290980097ee6e9f25900320b046fb16cd
Rules-tuple: (no-tashkeel, orthographic-token + QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, re, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q037-al-saffat/Q037-F-05-q37-q38-seam-prereg.md'
EXPECTED_SHA = '684ae9fdc0150ba64ed56e39a6e5f5c290980097ee6e9f25900320b046fb16cd'

PROPHET_NAMES = [
    'آدم', 'نوح', 'إدريس', 'هود', 'صالح', 'إبراهيم', 'لوط',
    'إسماعيل', 'إسحاق', 'يعقوب', 'يوسف', 'شعيب',
    'أيوب', 'موسى', 'هارون', 'داوود', 'سليمان',
    'إلياس', 'اليسع', 'يونس', 'زكريا', 'يحيى', 'عيسى', 'محمد',
]
DHU_KIFL = [r'ذا\s+الكفل', r'ذي\s+الكفل']


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))

    # H1: rank Q 37 → Q 38 in delta_raw ascending
    d720 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json'))
    per_adj = sorted(d720['per_adjacency'], key=lambda x: x['delta_raw'])
    rank_q37_q38 = next((i+1, r) for i,r in enumerate(per_adj) if r['s']==37)
    rank_position = rank_q37_q38[0]
    h1_pass = rank_position <= 5

    smoothest_5 = [(i+1, r['s'], r['pair'], r['delta_raw']) for i,r in enumerate(per_adj[:5])]

    # H2: 4 architectural cells
    d700 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json'))
    rld = {r['surah']: r for r in d700['rhyme']['rhyme_letter_diagnostics']}
    rl_q37 = rld[37]
    rl_q38 = rld[38]

    d750 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json'))
    ps = {r['surah']: r for r in d750['per_surah']}
    mcd_q37 = ps[37]['mean_content_distance']
    mcd_q38 = ps[38]['mean_content_distance']

    d111 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'))
    ut = d111['D_matrix_upper_triangular']
    N = 114
    mat = [[0.0]*N for _ in range(N)]
    for entry in ut:
        i, j, v = entry
        mat[i-1][j-1] = v
        mat[j-1][i-1] = v
    q37_top10 = sorted([(s+1, mat[36][s]) for s in range(N) if s!=36], key=lambda x: x[1])[:10]
    q38_top10 = sorted([(s+1, mat[37][s]) for s in range(N) if s!=37], key=lambda x: x[1])[:10]
    q37_in_q38_top5 = any(sid==37 for sid,_ in q38_top10[:5])
    q38_in_q37_top5 = any(sid==38 for sid,_ in q37_top10[:5])

    # cells
    cell_a_same_rhyme = (rl_q37['top_letter'] == rl_q38['top_letter'])
    n_q37_v = rl_q37['n_verses']  # 182
    n_q38_v = rl_q38['n_verses']  # 88
    # length-class: both mid-Meccan ~80-200 verses
    cell_b_same_length_class = (50 <= n_q37_v <= 200) and (50 <= n_q38_v <= 200)
    cell_c_d_close = abs(mcd_q37 - mcd_q38) <= 0.10
    cell_d_top5_neighbor = q37_in_q38_top5 or q38_in_q37_top5

    cells = [cell_a_same_rhyme, cell_b_same_length_class, cell_c_d_close, cell_d_top5_neighbor]
    n_cells_pass = sum(cells)
    h2_pass = n_cells_pass >= 2

    # H3: shared prophet tokens
    def prophets_in_surah(sid):
        s = next(x for x in quran if x['id']==sid)
        full = ' '.join(v['text'] for v in s['verses'])
        present = set()
        for name in PROPHET_NAMES:
            pat = re.compile(r'(?:^|\s)(?:[لوفبك])*' + re.escape(name) + r'(?=\s|$|[،.])')
            if pat.search(full):
                present.add(name)
        for pat in DHU_KIFL:
            if re.search(pat, full):
                present.add('ذو الكفل')
                break
        return present

    p37 = prophets_in_surah(37)
    p38 = prophets_in_surah(38)
    shared = p37 & p38
    h3_pass = len(shared) >= 3

    # Verdict
    n_pass = sum([h1_pass, h2_pass, h3_pass])
    if n_pass == 3:
        verdict = 'CONFIRMED'
    elif n_pass == 2:
        verdict = 'DIRECTIONAL'
    elif n_pass == 1:
        verdict = 'DIRECTIONAL-WEAK'
    else:
        verdict = 'NULL'
    if rank_position > 50 or len(shared) == 0:
        verdict = 'PRE-COMMIT-VIOLATION'

    out = {
        'finding_id': 'Q037-F-05',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-token + QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'h1_q37_q38_seam': {
            'rank_in_delta_raw_ascending': rank_position,
            'delta_raw': rank_q37_q38[1]['delta_raw'],
            'fraction_residual': rank_q37_q38[1]['fraction_residual'],
            'top_5_smoothest': smoothest_5,
            'h1_pass_top5': h1_pass,
        },
        'h2_architectural_cells': {
            'cell_a_same_top_rhyme_letter': {
                'q37_top': rl_q37['top_letter'], 'q37_frac': rl_q37['frac'],
                'q38_top': rl_q38['top_letter'], 'q38_frac': rl_q38['frac'],
                'pass': cell_a_same_rhyme,
            },
            'cell_b_same_length_class': {
                'q37_n_verses': n_q37_v, 'q38_n_verses': n_q38_v, 'pass': cell_b_same_length_class,
            },
            'cell_c_mean_content_distance_close': {
                'q37_mcd': mcd_q37, 'q38_mcd': mcd_q38, 'delta': abs(mcd_q37-mcd_q38), 'pass': cell_c_d_close,
            },
            'cell_d_top5_FR_neighbor': {
                'q38_in_q37_top10': [(sid, dv) for sid, dv in q37_top10 if sid==38],
                'q37_in_q38_top10': [(sid, dv) for sid, dv in q38_top10 if sid==37],
                'q37_top10_neighbors': q37_top10,
                'q38_top10_neighbors': q38_top10,
                'pass': cell_d_top5_neighbor,
            },
            'n_cells_pass': n_cells_pass,
            'h2_pass': h2_pass,
        },
        'h3_shared_prophets': {
            'prophets_in_q37': sorted(list(p37)),
            'prophets_in_q38': sorted(list(p38)),
            'shared': sorted(list(shared)),
            'h3_pass': h3_pass,
        },
        'verdict': verdict,
        'honest_limits': 'Smoothest-5 ranking depends on H-NEW-720 2-opt heuristic with K=10 starts; cell (a) rhyme-letter likely fails (Q 37=ن, Q 38=ب expected); content seamlessness driven by shared prophet-cycle motif.',
    }

    print('=== Q037-F-05 Q 37 → Q 38 SEAM ===')
    print(f'H1 rank in delta_raw ascending: {rank_position}/113')
    print(f'  delta_raw: {rank_q37_q38[1]["delta_raw"]:.6f}')
    print(f'  fraction_residual: {rank_q37_q38[1]["fraction_residual"]}')
    print(f'  top-5 smoothest:')
    for r in smoothest_5:
        print(f'    rank {r[0]}: pair {r[2]} delta_raw={r[3]:.6f}')
    print(f'\nH2 architectural cells:')
    print(f'  (a) same top-rhyme-letter: q37={rl_q37["top_letter"]}({rl_q37["frac"]:.2f}), q38={rl_q38["top_letter"]}({rl_q38["frac"]:.2f}) → pass={cell_a_same_rhyme}')
    print(f'  (b) same length-class (50-200 v): {cell_b_same_length_class}')
    print(f'  (c) mcd close (|Δ|≤0.10): {mcd_q37:.4f} vs {mcd_q38:.4f} → pass={cell_c_d_close}')
    print(f'  (d) top-5 FR neighbor: pass={cell_d_top5_neighbor}')
    print(f'  n_cells_pass: {n_cells_pass}/4; H2: {h2_pass}')
    print(f'\nH3 shared prophets ({len(shared)}): {sorted(shared)}')
    print(f'  H3: {h3_pass}')
    print(f'\nVerdict: {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv/Q037-F-05.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
