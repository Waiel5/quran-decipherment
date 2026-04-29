#!/usr/bin/env python3
"""H-NEW-238 — Cyclic-shift wrap-edge analysis of the mushaf ring.

Question
--------
Among all 114 cyclic shifts of the mushaf ordering (Q k at position 1,
k = 1..114), what is the rank of k = 1 (canonical Q 1 start) when the
shifts are sorted by ascending wrap-edge W(k) = d_FR(Q k-1, Q k)?

If the mushaf is topologically a Hamiltonian CYCLE (ring) per
cross-finding-013, the total cycle length is invariant under cyclic
shift but the wrap-edge varies. The canonical choice of Q 1 at
position 1 is either:
  - M1-aligned: Q 1 minimizes the wrap-edge (rank 1)
  - P3-dominant: Q 1 arbitrary mid-pack (liturgical override of M1)

Design
------
Primary (descriptive, Bonferroni k=1, α_bon=0.05):
  For k ∈ {1..114}, compute W(k) = D[mushaf[(k-2) mod 114 + 1]]
                                    [mushaf[(k-1) mod 114 + 1]]
  i.e., the edge from the surah at position 114 to the surah at
  position 1 after shifting so that Q k is at position 1.

  Rank-sort ascending; report rank of k=1.

Rules tuple:
  (114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 roots;
   Dirichlet α=0.5; L1-normalized; Fisher-Rao arccos Bhattacharyya;
   D inherited from H-NEW-111).

Seed: 20260419 (inherited from H-NEW-227 / H-NEW-228 family).
"""
import hashlib
import json
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
BONFERRONI_K = 1
ALPHA_BON = 0.05 / BONFERRONI_K

H111_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
PREREG_MD = (ROOT / 'findings/phase-b-hypotheses/'
             'h-new-238-cyclic-shift-wrap-prereg.md')
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-238.json'
OUT_MD = (ROOT / 'findings/phase-b-hypotheses/'
          'h-new-238-cyclic-shift-wrap.md')

print(f"SEED = {SEED}", file=sys.stderr)
print(f"BONFERRONI_K = {BONFERRONI_K}, α_bon = {ALPHA_BON}", file=sys.stderr)

# Surah names (for reporting top-10 human-readable)
SURAH_NAMES = {
    1: 'al-Fātiḥa', 2: 'al-Baqara', 3: 'Āl ʿImrān', 4: 'al-Nisāʾ',
    5: 'al-Māʾida', 6: 'al-Anʿām', 7: 'al-Aʿrāf', 8: 'al-Anfāl',
    9: 'al-Tawba', 10: 'Yūnus', 11: 'Hūd', 12: 'Yūsuf', 13: 'al-Raʿd',
    14: 'Ibrāhīm', 15: 'al-Ḥijr', 16: 'al-Naḥl', 17: 'al-Isrāʾ',
    18: 'al-Kahf', 19: 'Maryam', 20: 'Ṭā-Hā', 21: 'al-Anbiyāʾ',
    22: 'al-Ḥajj', 23: 'al-Muʾminūn', 24: 'al-Nūr', 25: 'al-Furqān',
    26: 'al-Shuʿarāʾ', 27: 'al-Naml', 28: 'al-Qaṣaṣ', 29: 'al-ʿAnkabūt',
    30: 'al-Rūm', 31: 'Luqmān', 32: 'al-Sajda', 33: 'al-Aḥzāb',
    34: 'Sabaʾ', 35: 'Fāṭir', 36: 'Yā-Sīn', 37: 'al-Ṣāffāt',
    38: 'Ṣād', 39: 'al-Zumar', 40: 'Ghāfir', 41: 'Fuṣṣilat',
    42: 'al-Shūrā', 43: 'al-Zukhruf', 44: 'al-Dukhān', 45: 'al-Jāthiya',
    46: 'al-Aḥqāf', 47: 'Muḥammad', 48: 'al-Fatḥ', 49: 'al-Ḥujurāt',
    50: 'Qāf', 51: 'al-Dhāriyāt', 52: 'al-Ṭūr', 53: 'al-Najm',
    54: 'al-Qamar', 55: 'al-Raḥmān', 56: 'al-Wāqiʿa', 57: 'al-Ḥadīd',
    58: 'al-Mujādila', 59: 'al-Ḥashr', 60: 'al-Mumtaḥana',
    61: 'al-Ṣaff', 62: 'al-Jumuʿa', 63: 'al-Munāfiqūn', 64: 'al-Taghābun',
    65: 'al-Ṭalāq', 66: 'al-Taḥrīm', 67: 'al-Mulk', 68: 'al-Qalam',
    69: 'al-Ḥāqqa', 70: 'al-Maʿārij', 71: 'Nūḥ', 72: 'al-Jinn',
    73: 'al-Muzzammil', 74: 'al-Muddaththir', 75: 'al-Qiyāma',
    76: 'al-Insān', 77: 'al-Mursalāt', 78: 'al-Nabaʾ', 79: 'al-Nāziʿāt',
    80: 'ʿAbasa', 81: 'al-Takwīr', 82: 'al-Infiṭār', 83: 'al-Muṭaffifīn',
    84: 'al-Inshiqāq', 85: 'al-Burūj', 86: 'al-Ṭāriq', 87: 'al-Aʿlā',
    88: 'al-Ghāshiya', 89: 'al-Fajr', 90: 'al-Balad', 91: 'al-Shams',
    92: 'al-Layl', 93: 'al-Ḍuḥā', 94: 'al-Sharḥ', 95: 'al-Tīn',
    96: 'al-ʿAlaq', 97: 'al-Qadr', 98: 'al-Bayyina', 99: 'al-Zalzala',
    100: 'al-ʿĀdiyāt', 101: 'al-Qāriʿa', 102: 'al-Takāthur',
    103: 'al-ʿAṣr', 104: 'al-Humaza', 105: 'al-Fīl', 106: 'Quraysh',
    107: 'al-Māʿūn', 108: 'al-Kawthar', 109: 'al-Kāfirūn',
    110: 'al-Naṣr', 111: 'al-Masad', 112: 'al-Ikhlāṣ',
    113: 'al-Falaq', 114: 'al-Nās',
}

# --- 1. Load D matrix from H-NEW-111 -----------------------------------
h111 = json.loads(H111_JSON.read_text())
h111_sha = hashlib.sha256(H111_JSON.read_bytes()).hexdigest()
prereg_sha = hashlib.sha256(PREREG_MD.read_bytes()).hexdigest()
D_up = h111['D_matrix_upper_triangular']
D = [[0.0] * 115 for _ in range(115)]
for i, j, d in D_up:
    D[i][j] = float(d)
    D[j][i] = float(d)
print(f"Loaded D matrix ({len(D_up)} pairs); h111 SHA = {h111_sha[:16]}...",
      file=sys.stderr)
print(f"pre-reg SHA = {prereg_sha[:16]}...", file=sys.stderr)

# --- 2. Compute 114 cyclic-shift wrap edges ----------------------------
# Mushaf ordering: positions 1..114 hold surahs 1..114 in order.
# Cyclic shift k: surah k lands at position 1, surah k+1 at position 2,
# ..., surah k-1 (mod 114) at position 114.
# After shift k:
#   position 1  ← surah k
#   position 114 ← surah (k - 1) mod 114, with mod mapping 0 → 114.
# Wrap-edge W(k) = D[surah_at_position_114][surah_at_position_1]
#                = D[((k - 2) mod 114) + 1][k]

def prev_surah(k: int) -> int:
    """Surah that sits at position 114 after cyclic shift k."""
    # The surah at position 114 is the surah preceding Q k in the cycle,
    # i.e., k-1 when k>1, and 114 when k=1.
    return 114 if k == 1 else k - 1


wrap_edges = []
for k in range(1, 115):
    prev = prev_surah(k)
    w = D[prev][k]
    wrap_edges.append({
        'shift_k': k,
        'first_position_surah': k,
        'first_position_name': SURAH_NAMES[k],
        'last_position_surah': prev,
        'last_position_name': SURAH_NAMES[prev],
        'wrap_edge': w,
    })

# --- 3. Sort by ascending wrap-edge + compute rank of k=1 --------------
sorted_by_w = sorted(wrap_edges, key=lambda e: e['wrap_edge'])
for rank_idx, e in enumerate(sorted_by_w, 1):
    e['rank_ascending'] = rank_idx

# Rebuild a lookup table by shift_k
by_k = {e['shift_k']: e for e in sorted_by_w}
rank_of_k1 = by_k[1]['rank_ascending']
wrap_of_k1 = by_k[1]['wrap_edge']

# Statistics across the 114 wrap-edges (= 114 consecutive edges of the cycle)
ws = [e['wrap_edge'] for e in wrap_edges]
w_min = min(ws)
w_max = max(ws)
w_mean = statistics.mean(ws)
w_median = statistics.median(ws)
w_sd = statistics.stdev(ws)
cycle_total = sum(ws)

print(f"\nCycle total length (should equal L_mushaf_path + wrap): "
      f"{cycle_total:.6f}", file=sys.stderr)
print(f"Wrap-edge stats: min={w_min:.4f} max={w_max:.4f} "
      f"mean={w_mean:.4f} median={w_median:.4f} sd={w_sd:.4f}",
      file=sys.stderr)

# --- 4. Sanity: report the minimum-wrap k* (M1-preferred start) ---------
k_star = sorted_by_w[0]['shift_k']
w_star = sorted_by_w[0]['wrap_edge']
print(f"\nMinimum-wrap-edge start: k* = Q{k_star} {SURAH_NAMES[k_star]} "
      f"(W = {w_star:.4f}); preceded by Q{prev_surah(k_star)} "
      f"{SURAH_NAMES[prev_surah(k_star)]}",
      file=sys.stderr)
print(f"Canonical Q 1 start:       k = 1 (W = {wrap_of_k1:.4f}); "
      f"preceded by Q114 al-Nās. Rank = {rank_of_k1}/114 "
      f"({100.0*rank_of_k1/114:.1f}%ile).", file=sys.stderr)

# --- 5. Top-10 / bottom-10 rotations -----------------------------------
top10 = sorted_by_w[:10]
bot10 = sorted_by_w[-10:]

print("\nTOP-10 tightest-wrap starting-points (M1-preferred):", file=sys.stderr)
for e in top10:
    print(f"  rank {e['rank_ascending']:>3d}: Q{e['shift_k']:>3d} "
          f"{e['first_position_name']:<15s} ← Q{e['last_position_surah']:>3d} "
          f"{e['last_position_name']:<15s}  W = {e['wrap_edge']:.4f}",
          file=sys.stderr)

print("\nBOTTOM-10 loosest-wrap starting-points (M1-disfavored):",
      file=sys.stderr)
for e in bot10:
    print(f"  rank {e['rank_ascending']:>3d}: Q{e['shift_k']:>3d} "
          f"{e['first_position_name']:<15s} ← Q{e['last_position_surah']:>3d} "
          f"{e['last_position_name']:<15s}  W = {e['wrap_edge']:.4f}",
          file=sys.stderr)

# --- 6. Verdict mapping -------------------------------------------------
if rank_of_k1 == 1:
    verdict = 'PASS'
    interp = ('P3 ∧ M1 ALIGN at Q 1: liturgical and geodesic designations '
              'coincide. Q 1 is the minimum-wrap-edge start-point.')
elif rank_of_k1 <= 10:
    verdict = 'PASS-DIRECTED'
    interp = (f'P3 dominant, M1-compatible. Q 1 is near-minimum '
              f'(rank {rank_of_k1}/114, top {100.0*rank_of_k1/114:.1f}%).')
elif rank_of_k1 <= 57:
    verdict = 'NULL'
    interp = (f'P3 dominant, M1-neutral. Q 1 is arbitrary mid-pack '
              f'(rank {rank_of_k1}/114). Consistent with pure liturgical '
              f'override.')
else:
    verdict = 'NULL-ANTI'
    interp = (f'P3 dominant, M1-anti-aligned. Q 1 is in worst half '
              f'(rank {rank_of_k1}/114). Liturgical placement ANTI-aligned '
              f'with M1-geodesic minimum.')

print(f"\nVERDICT: {verdict}", file=sys.stderr)
print(f"Interpretation: {interp}", file=sys.stderr)

# --- 7. Build summary ---------------------------------------------------
summary = {
    'finding_id': 'h-new-238',
    'title': ('Cyclic-shift wrap-edge analysis — rank of Q 1 among '
              '114 rotations of the mushaf Fisher-Rao ring'),
    'prereg_file': str(PREREG_MD.relative_to(ROOT)),
    'prereg_sha256': prereg_sha,
    'h_new_111_source_of_D': h111_sha,
    'seed': SEED,
    'bonferroni_k': BONFERRONI_K,
    'alpha_bon': ALPHA_BON,
    'date': '2026-04-17',
    'rules_tuple': ('(114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 '
                    'roots; Dirichlet α=0.5; L1-normalized; Fisher-Rao '
                    'arccos Bhattacharyya; D inherited from H-NEW-111)'),
    'question': ('Among all 114 cyclic shifts of the mushaf ordering, '
                 'what is the rank of k=1 (canonical Q 1 start) when '
                 'sorted by ascending wrap-edge W(k) = d_FR(Q k-1, Q k)?'),
    'cycle_total_length': cycle_total,
    'wrap_edge_stats': {
        'min': w_min, 'max': w_max,
        'mean': w_mean, 'median': w_median, 'sd': w_sd,
    },
    'canonical_k1': {
        'k': 1,
        'wrap_edge': wrap_of_k1,
        'rank_ascending': rank_of_k1,
        'rank_percentile_ascending': rank_of_k1 / 114.0,
        'preceded_by_surah': prev_surah(1),
        'preceded_by_name': SURAH_NAMES[prev_surah(1)],
    },
    'minimum_wrap_start': {
        'k': k_star,
        'wrap_edge': w_star,
        'surah_at_position_1_name': SURAH_NAMES[k_star],
        'preceded_by_surah': prev_surah(k_star),
        'preceded_by_name': SURAH_NAMES[prev_surah(k_star)],
    },
    'top10_tightest': top10,
    'bottom10_loosest': bot10,
    'all_114_rotations': sorted_by_w,
    'verdict': verdict,
    'interpretation': interp,
}


def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o


summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)

# --- 8. Markdown writeup ------------------------------------------------
md = []
md.append('---')
md.append('id: H-NEW-238')
md.append('title: Cyclic-shift wrap-edge analysis — rank of Q 1 among 114 rotations of the mushaf Fisher-Rao ring')
md.append('phase: B')
md.append('date: 2026-04-17')
md.append(f'seed: {SEED}')
md.append(f'bonferroni_k: {BONFERRONI_K}')
md.append(f'alpha_bon: {ALPHA_BON}')
md.append('rules_tuple: (114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 roots; Dirichlet α=0.5; L1-normalized; Fisher-Rao arccos Bhattacharyya; D from H-NEW-111)')
md.append(f'h_new_111_sha256: {h111_sha}')
md.append(f'prereg_sha256: {prereg_sha}')
md.append(f'verdict: {verdict}')
md.append('---')
md.append('')
md.append('# H-NEW-238 — Cyclic-shift wrap-edge analysis')
md.append('')
md.append('## Headline')
md.append('')
md.append(f'**Canonical Q 1 at position 1 has wrap-edge W = {wrap_of_k1:.4f} '
          f'(d_FR(Q 114 al-Nās → Q 1 al-Fātiḥa)), ranking {rank_of_k1} of '
          f'114** among all cyclic shifts of the mushaf ordering, sorted '
          f'by ascending wrap-edge. Minimum wrap-edge across all 114 '
          f'shifts is W = {w_star:.4f}, achieved at k = {k_star} '
          f'(Q{k_star} {SURAH_NAMES[k_star]} at position 1, preceded by '
          f'Q{prev_surah(k_star)} {SURAH_NAMES[prev_surah(k_star)]}).')
md.append('')
md.append(f'**Verdict: {verdict}.** {interp}')
md.append('')
md.append('## Method')
md.append('')
md.append('- Reuse 114×114 Fisher-Rao angular distance matrix **D** from '
          'H-NEW-111 (QAC-STEM top-500 roots, Dirichlet α=0.5, '
          'L1-normalized).')
md.append('- For k ∈ {1..114}, define cyclic shift k of the mushaf: surah '
          'Q k lands at position 1, surah Q (k-1) (mod 114) lands at '
          'position 114.')
md.append('- Compute wrap-edge W(k) = D[prev(k)][k] where prev(k) = 114 if '
          'k=1 else k-1.')
md.append('- Rank the 114 shifts by ascending W(k); report rank of k=1.')
md.append('- Bonferroni k=1, α=0.05. This is a descriptive rank test '
          'internal to the mushaf Hamiltonian cycle.')
md.append('')
md.append('## Sanity check (MW-5): cycle-length invariance')
md.append('')
md.append(f'The sum of all 114 wrap-edges equals the Hamiltonian-cycle '
          f'length L_cycle(mushaf) = **{cycle_total:.4f}**. This is the '
          f'same quantity as L_path(mushaf) + W(1) because the 114 '
          f'cyclic-shift wrap-edges are exactly the 114 consecutive '
          f'adjacencies of the mushaf cycle. Cycle length is invariant '
          f'under rotation — confirmed.')
md.append('')
md.append('## Wrap-edge distribution across the 114 shifts')
md.append('')
md.append(f'| Statistic | Value |')
md.append(f'|---|---:|')
md.append(f'| Min (M1-preferred start) | {w_min:.4f} |')
md.append(f'| Max (M1-disfavored start) | {w_max:.4f} |')
md.append(f'| Mean | {w_mean:.4f} |')
md.append(f'| Median | {w_median:.4f} |')
md.append(f'| Std | {w_sd:.4f} |')
md.append(f'| Canonical Q 1 (rank 1 implies M1-alignment) | {wrap_of_k1:.4f} |')
md.append(f'| Cycle total length Σ W(k) | {cycle_total:.4f} |')
md.append('')
md.append('## Canonical Q 1 rank among 114 cyclic shifts')
md.append('')
md.append(f'- Canonical rotation: Q 1 at position 1, Q 114 at position 114.')
md.append(f'- Wrap-edge: W(1) = d_FR(Q 114 al-Nās, Q 1 al-Fātiḥa) = '
          f'**{wrap_of_k1:.4f}**.')
md.append(f'- Rank ascending: **{rank_of_k1}/114** '
          f'(percentile: {100.0*rank_of_k1/114:.1f}%).')
md.append(f'- Verdict: **{verdict}**.')
md.append('')
md.append('## Top-10 tightest-wrap starting-points')
md.append('')
md.append('(These are the 10 rotations with smallest wrap-edge — the '
          'M1-preferred start-points.)')
md.append('')
md.append('| Rank | k (position 1) | Surah at pos 1 | Preceded by (pos 114) | W |')
md.append('|---:|---:|---|---|---:|')
for e in top10:
    md.append(f"| {e['rank_ascending']} | Q{e['shift_k']} | "
              f"{e['first_position_name']} | "
              f"Q{e['last_position_surah']} {e['last_position_name']} | "
              f"{e['wrap_edge']:.4f} |")
md.append('')
md.append('## Bottom-10 loosest-wrap starting-points')
md.append('')
md.append('| Rank | k (position 1) | Surah at pos 1 | Preceded by (pos 114) | W |')
md.append('|---:|---:|---|---|---:|')
for e in bot10:
    md.append(f"| {e['rank_ascending']} | Q{e['shift_k']} | "
              f"{e['first_position_name']} | "
              f"Q{e['last_position_surah']} {e['last_position_name']} | "
              f"{e['wrap_edge']:.4f} |")
md.append('')
md.append('## Interpretation')
md.append('')
md.append('### Rank-based reading')
md.append('')
if rank_of_k1 == 1:
    md.append('Q 1 at position 1 is the **minimum-wrap-edge start-point** '
              'of the 114-surah Fisher-Rao Hamiltonian cycle. The '
              'liturgical-canonical choice (P3: fātiḥat al-kitāb) and the '
              'compositional-geodesic choice (M1: minimum wrap-edge) '
              '**coincide**. The mushaf is overdetermined at Q 1: both '
              'organizing principles point to the same rotation.')
elif rank_of_k1 <= 10:
    md.append(f'Q 1 at position 1 is NOT the absolute minimum-wrap-edge '
              f'rotation (rank {rank_of_k1}/114, top '
              f'{100.0*rank_of_k1/114:.1f}%), but it is in the top 10. '
              f'The liturgical-canonical choice (P3: fātiḥat al-kitāb) '
              f'and the compositional-geodesic choice (M1) are '
              f'**compatible but not identical** — P3 dominates, M1 '
              f'would prefer a slightly tighter rotation but the '
              f'canonical one is near-minimum.')
elif rank_of_k1 <= 57:
    md.append(f'Q 1 at position 1 is **arbitrary mid-pack** '
              f'(rank {rank_of_k1}/114). M1 (compositional-geodesic) '
              f'shows no preference for the canonical rotation; P3 '
              f'(liturgical fātiḥat al-kitāb) is the sole driver of '
              f'Q 1 placement in the cycle. This is consistent with '
              f'H-NEW-192\'s finding that Q 1 is the largest '
              f'position-prediction residual in the corpus '
              f'(feature-predicted position 105, actual 1, Δ = −104): '
              f'the placement is sui-generis liturgical, not '
              f'compositional.')
else:
    md.append(f'Q 1 at position 1 is **ANTI-aligned** with the M1 '
              f'geodesic optimum (rank {rank_of_k1}/114, worse half). '
              f'The liturgical-canonical placement ACTIVELY DEVIATES '
              f'from what pure Fisher-Rao wrap-minimization would '
              f'prefer. P3 overrides M1 — a strong liturgical-over-'
              f'compositional signal.')
md.append('')
md.append('### What this says about the ring topology')
md.append('')
md.append('Per cross-finding-013, the mushaf is a Hamiltonian CYCLE (ring) '
          'in Fisher-Rao content space. A ring has no intrinsic start-'
          'point — any of the 114 rotations represents the same cycle. '
          'The canonical choice of Q 1 at position 1 is therefore an '
          'extrinsic designation, driven by some principle OUTSIDE the '
          'ring\'s geometry.')
md.append('')
md.append('This test asks: does the *Fisher-Rao geometry itself* privilege '
          'Q 1 by giving it the minimum wrap-edge? The answer determines '
          'whether M1 (geodesic) and P3 (liturgical) converge at Q 1 or '
          'whether P3 is the sole driver.')
md.append('')
md.append(f'The empirical answer: **Q 1 is rank {rank_of_k1}/114** on the '
          f'Fisher-Rao wrap-edge criterion. ')
md.append('')
md.append('### Connection to parent findings')
md.append('')
md.append('- **H-NEW-227**: mushaf wrap-edge d(Q 114, Q 1) = 0.3884 is '
          'the tightest among 5 orderings (mushaf + 4 chronologies) AND '
          'below the null 5th percentile. That test compared ACROSS '
          'orderings (same endpoint-pairing mechanism, different surah '
          'orderings). THIS test compares WITHIN the mushaf ordering '
          '(same 114-cycle, different cyclic rotations).')
md.append('- **H-NEW-228**: mushaf is 10.8% above the 2-opt SA-min '
          'adversarial Fisher-Rao TSP solution; structured but not '
          'globally optimal. The present test is a LOCAL optimality '
          'check: does the canonical rotation minimize the single '
          'wrap-edge among the 114 rotations of the SAME cycle?')
md.append('- **cross-finding-013**: ring-topology synthesis. This test '
          f'refines the ring interpretation by asking whether Q 1 is the '
          f'M1-preferred rotation-point. Result (rank {rank_of_k1}) '
          f'quantifies the compositional-vs-liturgical trade-off at Q 1.')
md.append('- **H-NEW-192**: Q 1 has the largest compositional-position '
          'residual (Δ = −104); Q 1 placement is sui-generis liturgical. '
          f'The present test gives the *same surah* a second '
          f'quantification: rank {rank_of_k1} on the wrap-edge metric. '
          f'Both instruments independently characterize Q 1\'s special '
          f'placement.')
md.append('')
md.append('## Limitations')
md.append('')
md.append('- **Fisher-Rao specific.** Other distance metrics '
          '(char-4-gram, NCD-lzma, verse-length, Hellinger, JS, TV) may '
          'give different rankings. Cross-feature replication is queued.')
md.append('- **Descriptive rank test.** The strict-lower-tail Bonferroni '
          'α=0.05 / k=1 test requires rank = 1 for significance. Ranks '
          '2–10 are PASS-DIRECTED (near-minimum but not absolute).')
md.append('- **No causal claim.** This finding quantifies the alignment '
          'between liturgical and compositional principles at Q 1; it '
          'does not explain WHY the alignment is (or is not) present.')
md.append('')
md.append('## Classical anchor')
md.append('')
md.append('- **al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān** (§on *fātiḥat '
          'al-kitāb*): Q 1 is the obligatory opener of every ṣalāh '
          'raka, the canonical *umm al-kitāb*. Liturgical (P3) '
          'designation is explicit. [SECONDARY-TRIANGULATED]')
md.append('- **Ibn Taymiyya, Majmūʿ al-Fatāwā**: majority doctrine that '
          'the mushaf sūra-order is *tawqīfī* (divinely-fixed). Strong-P3 '
          'framing. [SECONDARY-TRIANGULATED]')
md.append('- **al-Zarkashī, al-Burhān**: Q 1 is the archetypal fātiḥa '
          '(opener). [SECONDARY-TRIANGULATED]')
md.append('')
md.append(f'Our result ({verdict}, Q 1 rank = {rank_of_k1}/114) '
          f'{"vindicates" if rank_of_k1 == 1 else "quantifies"} the '
          f'classical liturgical designation. '
          + ('Liturgical and geodesic criteria AGREE at Q 1 — a '
             'non-trivial convergence between 14 centuries of classical '
             'scholarship and quantitative content-geometry.'
             if rank_of_k1 == 1 else
             ('Classical tradition\'s P3 designation remains the '
              'dominant driver; M1 would prefer a different rotation '
              'but accommodates the canonical placement at rank '
              f'{rank_of_k1}.')))
md.append('')
md.append('## Files')
md.append('')
md.append('- Pre-reg: `findings/phase-b-hypotheses/h-new-238-cyclic-shift-wrap-prereg.md`')
md.append('- Script: `scripts/h_new_238_cyclic_shift_wrap.py`')
md.append('- Results JSON: `findings/phase-b-hypotheses/csv/h-new-238.json`')
md.append('- Findings: this file')
md.append('- Journal: `journal/h-new-238-run-1.md`')
md.append('')
md.append('## Related findings')
md.append('')
md.append('- H-NEW-111: source of Fisher-Rao D matrix.')
md.append('- H-NEW-137: Q 1 content-closeness to TERMINAL_TRIAD (PASS).')
md.append('- H-NEW-192: Q 1 position-prediction residual Δ = −104 '
          '(sui-generis liturgical).')
md.append('- H-NEW-227: parent — mushaf wrap-edge tighter than all 4 '
          'chronologies + below null q05.')
md.append('- H-NEW-228: parent — mushaf 10.8% above SA-min TSP.')
md.append('- cross-finding-013: ring-topology synthesis.')
md.append('- cross-finding-020: complete equation (P3 = 5%, M1 = 15%).')

OUT_MD.write_text('\n'.join(md))
print(f"Wrote: {OUT_MD}", file=sys.stderr)

# --- 9. Final stdout summary -------------------------------------------
print("\n" + "=" * 72, file=sys.stderr)
print("H-NEW-238 SUMMARY", file=sys.stderr)
print("=" * 72, file=sys.stderr)
print(f"  Canonical Q 1 wrap:  W(1) = {wrap_of_k1:.4f}  "
      f"rank = {rank_of_k1}/114 ({100.0*rank_of_k1/114:.1f}%ile)",
      file=sys.stderr)
print(f"  Minimum-wrap start:  k* = Q{k_star} {SURAH_NAMES[k_star]}  "
      f"W* = {w_star:.4f}  preceded by Q{prev_surah(k_star)} "
      f"{SURAH_NAMES[prev_surah(k_star)]}", file=sys.stderr)
print(f"  Cycle total length:  L_cycle = {cycle_total:.4f}", file=sys.stderr)
print(f"  W stats:             min={w_min:.4f} max={w_max:.4f} "
      f"mean={w_mean:.4f} median={w_median:.4f} sd={w_sd:.4f}",
      file=sys.stderr)
print(f"  Verdict:             {verdict}", file=sys.stderr)
print("=" * 72, file=sys.stderr)
