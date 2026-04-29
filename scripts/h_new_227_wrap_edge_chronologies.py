#!/usr/bin/env python3
"""H-NEW-227 — Wrap-edge comparison across chronologies.

Question
--------
In Fisher-Rao cyclic space (D-matrix from H-NEW-111), is the mushaf
wrap-edge d(Q114, Q1) shorter than the wrap-edge d(last_ordered,
first_ordered) under each classical chronology (Nöldeke, Egyptian-1924,
Bell-1937, Blachère-1947)?

A ṭawāf-like wrap-around is a strong prediction of the mushaf if its
terminal return to Q1 is geodesically tight — specifically tighter than
what we'd see by gluing the last-revealed surah to the first-revealed
surah under a chronology.

Design
------
PRIMARY (descriptive + single one-sided permutation test, k=1, α=0.05)
  H0: d(Q114, Q1) is not smaller than the median wrap-edge under a
      uniform-random null over 10,000 permutations, where wrap-edge =
      d(perm[-1], perm[0]).
  Report: p_mushaf_wrap_vs_null (one-sided lower).

DESCRIPTIVE comparisons (no additional alpha spent; reported as diffs):
  Δ_nold   = d(Q114,Q1) − d(noldeke_last, noldeke_first)
  Δ_egypt  = d(Q114,Q1) − d(egyptian_last, egyptian_first)
  Δ_bell   = d(Q114,Q1) − d(bell_last, bell_first)
  Δ_blach  = d(Q114,Q1) − d(blachere_last, blachere_first)
  Negative Δ ⇒ mushaf wrap-edge is tighter (confirms ṭawāf-like closure
  relative to that chronology).

Bonferroni k=1 per the pre-reg instruction.
Seed 20260419 (reuses H-NEW-212 seed for permutation null comparability).
"""
import csv
import hashlib
import json
import math
import random
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PERMS = 10000
BONFERRONI_K = 1
ALPHA_BON = 0.05 / BONFERRONI_K  # 0.05

H111_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
H212_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-212.json'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-227.json'
OUT_MD = ROOT / 'findings/phase-b-hypotheses/h-new-227-wrap-edge-chronologies.md'

print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)
print(f"BONFERRONI_K = {BONFERRONI_K}, α_bon = {ALPHA_BON}", file=sys.stderr)

# --- 1. Load D matrix from H-NEW-111 -----------------------------------
h111 = json.loads(H111_JSON.read_text())
h111_sha = hashlib.sha256(H111_JSON.read_bytes()).hexdigest()
D_up = h111['D_matrix_upper_triangular']
D = [[0.0] * 115 for _ in range(115)]
for i, j, d in D_up:
    D[i][j] = float(d)
    D[j][i] = float(d)
print(f"Loaded D matrix ({len(D_up)} pairs); h111 SHA = {h111_sha[:16]}...",
      file=sys.stderr)

# --- 2. Load orderings --------------------------------------------------
mushaf_to_egyptian = {}
mushaf_to_noldeke = {}
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        msid = int(row['mushaf_order'])
        mushaf_to_egyptian[msid] = int(row['revelation_order'])
        mushaf_to_noldeke[msid] = int(row['noldeke_order'])

egyptian_order = sorted(range(1, 115), key=lambda sid: mushaf_to_egyptian[sid])
noldeke_order = sorted(range(1, 115), key=lambda sid: mushaf_to_noldeke[sid])

# Reuse Bell / Blachère ranks from H-NEW-212 (verified + pre-reg'd there)
h212 = json.loads(H212_JSON.read_text())
h212_sha = hashlib.sha256(H212_JSON.read_bytes()).hexdigest()

# Re-hardcode Bell/Blachère ranks (consistency with H-NEW-212)
BELL_RANK = {
    1: 45, 2: 91, 3: 97, 4: 100, 5: 114, 6: 89, 7: 87, 8: 95, 9: 113, 10: 84,
    11: 75, 12: 77, 13: 90, 14: 76, 15: 52, 16: 73, 17: 72, 18: 68, 19: 58,
    20: 55, 21: 65, 22: 107, 23: 64, 24: 105, 25: 66, 26: 56, 27: 67, 28: 79,
    29: 81, 30: 74, 31: 82, 32: 69, 33: 103, 34: 85, 35: 86, 36: 60, 37: 51,
    38: 59, 39: 80, 40: 78, 41: 70, 42: 62, 43: 61, 44: 53, 45: 71, 46: 88,
    47: 96, 48: 108, 49: 112, 50: 54, 51: 48, 52: 22, 53: 30, 54: 49, 55: 28,
    56: 23, 57: 99, 58: 106, 59: 102, 60: 110, 61: 98, 62: 94, 63: 104, 64: 93,
    65: 101, 66: 109, 67: 63, 68: 50, 69: 24, 70: 32, 71: 52, 72: 62, 73: 33,
    74: 2, 75: 27, 76: 34, 77: 25, 78: 26, 79: 20, 80: 17, 81: 15, 82: 15,
    83: 35, 84: 19, 85: 42, 86: 9, 87: 16, 88: 21, 89: 41, 90: 39, 91: 7,
    92: 14, 93: 4, 94: 5, 95: 10, 96: 1, 97: 29, 98: 92, 99: 11, 100: 13,
    101: 12, 102: 31, 103: 6, 104: 38, 105: 40, 106: 3, 107: 8, 108: 37,
    109: 44, 110: 111, 111: 36, 112: 43, 113: 46, 114: 47,
}
BLACHERE_RANK = {
    1: 5, 2: 87, 3: 89, 4: 92, 5: 112, 6: 55, 7: 39, 8: 88, 9: 113, 10: 51,
    11: 52, 12: 53, 13: 96, 14: 72, 15: 54, 16: 70, 17: 50, 18: 69, 19: 44,
    20: 45, 21: 73, 22: 103, 23: 74, 24: 102, 25: 42, 26: 47, 27: 48, 28: 49,
    29: 85, 30: 84, 31: 57, 32: 75, 33: 90, 34: 58, 35: 43, 36: 41, 37: 56,
    38: 38, 39: 59, 40: 60, 41: 61, 42: 53, 43: 63, 44: 64, 45: 65, 46: 66,
    47: 95, 48: 111, 49: 106, 50: 34, 51: 67, 52: 76, 53: 23, 54: 37, 55: 97,
    56: 46, 57: 94, 58: 105, 59: 101, 60: 91, 61: 109, 62: 110, 63: 104,
    64: 108, 65: 99, 66: 107, 67: 77, 68: 2, 69: 78, 70: 79, 71: 71, 72: 40,
    73: 3, 74: 4, 75: 31, 76: 98, 77: 33, 78: 80, 79: 81, 80: 24, 84: 24,
    81: 82, 82: 86, 83: 83, 85: 27, 86: 36, 87: 8, 88: 68, 89: 10, 90: 35,
    91: 26, 92: 9, 93: 11, 94: 12, 95: 28, 96: 1, 97: 25, 98: 100, 99: 93,
    100: 14, 101: 30, 102: 16, 103: 13, 104: 32, 105: 19, 106: 29, 107: 17,
    108: 15, 109: 18, 110: 114, 111: 6, 112: 22, 113: 20, 114: 21,
}
assert len(BELL_RANK) == 114 and len(BLACHERE_RANK) == 114

bell_order = sorted(range(1, 115), key=lambda sid: (BELL_RANK[sid], sid))
blachere_order = sorted(range(1, 115),
                        key=lambda sid: (BLACHERE_RANK[sid], sid))

# --- 3. Mushaf wrap-edge and per-chronology wrap-edges -----------------
orderings = {
    'mushaf': list(range(1, 115)),
    'noldeke_1860': noldeke_order,
    'egyptian_1924': egyptian_order,
    'bell_1937': bell_order,
    'blachere_1947': blachere_order,
}

wrap_edges = {}
for name, order in orderings.items():
    first, last = order[0], order[-1]
    d = D[last][first]
    wrap_edges[name] = {
        'first': first,
        'last': last,
        'wrap_edge': d,
    }
    print(f"  {name:15s}: first=Q{first:>3} last=Q{last:>3} "
          f"d(last,first)={d:.4f}", file=sys.stderr)

d_mushaf_wrap = wrap_edges['mushaf']['wrap_edge']  # d(Q114, Q1)

# --- 4. Permutation null on wrap-edges ---------------------------------
print(f"\nNull: {PERMS} permutation wrap-edges (seed {SEED})...",
      file=sys.stderr)
rng = random.Random(SEED)
base = list(range(1, 115))
null_wraps = []
for p in range(PERMS):
    perm = base[:]
    rng.shuffle(perm)
    null_wraps.append(D[perm[-1]][perm[0]])

null_sorted = sorted(null_wraps)
null_mean = statistics.mean(null_wraps)
null_sd = statistics.stdev(null_wraps)
null_median = statistics.median(null_wraps)

def q(sl, frac):
    n = len(sl)
    idx = max(0, min(n - 1, int(math.floor(frac * n))))
    return sl[idx]

null_quantiles = {
    'min': null_sorted[0],
    'q001': q(null_sorted, 0.001),
    'q01': q(null_sorted, 0.01),
    'q025': q(null_sorted, 0.025),
    'q05': q(null_sorted, 0.05),
    'q25': q(null_sorted, 0.25),
    'q50': null_median,
    'q75': q(null_sorted, 0.75),
    'q95': q(null_sorted, 0.95),
    'max': null_sorted[-1],
    'mean': null_mean,
    'sd': null_sd,
}
print(f"  null mean={null_mean:.4f} sd={null_sd:.4f} median={null_median:.4f}",
      file=sys.stderr)
print(f"  null min={null_sorted[0]:.4f} q05={null_quantiles['q05']:.4f} "
      f"q95={null_quantiles['q95']:.4f}", file=sys.stderr)


def p_lower(val):
    n_le = sum(1 for x in null_wraps if x <= val)
    return (n_le + 1) / (PERMS + 1), n_le


# Primary: mushaf wrap-edge permutation p-value
p_primary, n_le_mushaf = p_lower(d_mushaf_wrap)
z_mushaf = (d_mushaf_wrap - null_mean) / null_sd
print(f"\nPRIMARY: d(Q114,Q1) = {d_mushaf_wrap:.4f}", file=sys.stderr)
print(f"         z = {z_mushaf:+.3f}", file=sys.stderr)
print(f"         p_1sided_lower = {p_primary:.6f}  (α_bon={ALPHA_BON})",
      file=sys.stderr)
print(f"         verdict: {'PASS' if p_primary < ALPHA_BON else 'NULL'}",
      file=sys.stderr)

# Permutation p-values for every chronology's wrap-edge (descriptive)
chrono_wrap_stats = {}
for name, info in wrap_edges.items():
    d = info['wrap_edge']
    p, n_le = p_lower(d)
    z = (d - null_mean) / null_sd
    chrono_wrap_stats[name] = {
        'first': info['first'],
        'last': info['last'],
        'wrap_edge': d,
        'z': z,
        'n_perms_le': n_le,
        'p_one_sided_lower': p,
    }

# --- 5. Head-to-head: mushaf wrap vs each chronology wrap --------------
head_to_head = {}
for name, info in wrap_edges.items():
    if name == 'mushaf':
        continue
    d_chrono = info['wrap_edge']
    delta = d_mushaf_wrap - d_chrono   # negative ⇒ mushaf tighter
    tighter = 'mushaf TIGHTER' if delta < 0 else 'chronology TIGHTER or equal'
    # One-sided sign test-ish descriptive: count perms where the mushaf wrap
    # is tighter than this chronology's wrap.  The chronology wrap is a
    # single scalar so this is just d_chrono vs null quantile of perm wraps.
    head_to_head[name] = {
        'chrono_wrap': d_chrono,
        'mushaf_wrap': d_mushaf_wrap,
        'delta_mushaf_minus_chrono': delta,
        'delta_in_null_sd': delta / null_sd,
        'sign_interpretation': tighter,
    }
    print(f"  Δ({name}): {delta:+.4f} ({delta/null_sd:+.3f} SDs) — {tighter}",
          file=sys.stderr)

# --- 6. Sanity: does mushaf wrap rank as the tightest of the 5? --------
ranked = sorted(wrap_edges.items(), key=lambda kv: kv[1]['wrap_edge'])
print("\nRanked wrap-edges (tightest first):", file=sys.stderr)
for i, (name, info) in enumerate(ranked, 1):
    print(f"  {i}. {name:15s}  d={info['wrap_edge']:.4f}  "
          f"(last=Q{info['last']} → first=Q{info['first']})",
          file=sys.stderr)

mushaf_rank = next(i for i, (n, _) in enumerate(ranked, 1) if n == 'mushaf')

# --- 7. Build summary ---------------------------------------------------
summary = {
    'finding_id': 'h-new-227',
    'title': ('Wrap-edge d(last,first) across chronologies — '
              'does mushaf ṭawāf-like closure beat each chronology?'),
    'pre_reg_note': ('Pre-reg bonferroni_k=1, seed 20260419 as specified in '
                     'task prompt; single primary test = mushaf wrap-edge '
                     'vs permutation null; head-to-head deltas descriptive.'),
    'h_new_111_sha256_source_of_D': h111_sha,
    'h_new_212_sha256_source_of_ranks': h212_sha,
    'seed': SEED,
    'permutations': PERMS,
    'bonferroni_k': BONFERRONI_K,
    'alpha_bon': ALPHA_BON,
    'date': '2026-04-17',
    'rules_tuple': ('(114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 '
                    'roots; Dirichlet α=0.5; L1-normalized; Fisher-Rao arccos '
                    'Bhattacharyya; basmala-counted-only-in-Surah-1; '
                    'D-matrix inherited from H-NEW-111)'),
    'question': ('Is d(Q114, Q1) < d(last_ordered, first_ordered) under each '
                 'of Nöldeke/Egyptian/Bell/Blachère, and is it significantly '
                 'small vs a uniform-random wrap-edge null?'),
    'chronology_wrap_stats': chrono_wrap_stats,
    'null_quantiles': null_quantiles,
    'primary': {
        'metric': 'mushaf wrap-edge d(Q114, Q1)',
        'value': d_mushaf_wrap,
        'z': z_mushaf,
        'n_perms_le': n_le_mushaf,
        'p_one_sided_lower': p_primary,
        'alpha_bon': ALPHA_BON,
        'pass': p_primary < ALPHA_BON,
    },
    'head_to_head_vs_chronologies': head_to_head,
    'leaderboard_tightest_first': [
        {'rank': i + 1, 'name': n,
         'first': info['first'], 'last': info['last'],
         'wrap_edge': info['wrap_edge']}
        for i, (n, info) in enumerate(ranked)
    ],
    'mushaf_rank_among_5': mushaf_rank,
    'verdict_summary': None,  # filled below
}

# Verdict
mushaf_beats_all = all(
    wrap_edges['mushaf']['wrap_edge'] < wrap_edges[n]['wrap_edge']
    for n in ['noldeke_1860', 'egyptian_1924', 'bell_1937', 'blachere_1947']
)
verdict_parts = []
if summary['primary']['pass']:
    verdict_parts.append(
        f"PRIMARY PASS: d(Q114,Q1)={d_mushaf_wrap:.4f} "
        f"p={p_primary:.6f} < α={ALPHA_BON}")
else:
    verdict_parts.append(
        f"PRIMARY NULL: d(Q114,Q1)={d_mushaf_wrap:.4f} "
        f"p={p_primary:.6f} ≥ α={ALPHA_BON}")
verdict_parts.append(
    f"Mushaf wrap tighter than ALL 4 chronologies: {mushaf_beats_all}")
summary['verdict_summary'] = '; '.join(verdict_parts)
summary['mushaf_wrap_tighter_than_all_4_chronologies'] = mushaf_beats_all


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
md.append('id: H-NEW-227')
md.append('title: Wrap-edge d(last,first) across chronologies — mushaf ṭawāf-like closure test')
md.append('phase: B')
md.append('date: 2026-04-17')
md.append(f'seed: {SEED}')
md.append(f'permutations: {PERMS}')
md.append(f'bonferroni_k: {BONFERRONI_K}')
md.append(f'alpha_bon: {ALPHA_BON}')
md.append('rules_tuple: (114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 roots; Dirichlet α=0.5; L1-normalized; Fisher-Rao arccos Bhattacharyya; D from H-NEW-111)')
md.append(f'h_new_111_sha256: {h111_sha}')
md.append(f'h_new_212_sha256: {h212_sha}')
md.append('---')
md.append('')
md.append('# H-NEW-227 — Mushaf wrap-edge vs chronology wrap-edges')
md.append('')
md.append('## Question')
md.append('')
md.append('Does the mushaf "ṭawāf-like" wrap-around d(Q 114 → Q 1) beat the '
         'analogous wrap-edge d(final, initial) under Nöldeke (1860), '
         'Egyptian Standard (1924), Bell (1937), and Blachère (1947)?')
md.append('')
md.append('## Method')
md.append('')
md.append('- Reuse 114×114 Fisher-Rao angular distance matrix **D** from '
         'H-NEW-111 (QAC-STEM top-500 roots, Dirichlet α=0.5, L1-normalized).')
md.append('- For each ordering π, compute wrap-edge = D[π[-1], π[0]].')
md.append('- Null: 10,000 uniform-random permutations; for each, record '
         'D[perm[-1], perm[0]].  Compute one-sided lower-tail permutation '
         'p-value for mushaf wrap.')
md.append('- Bonferroni k=1 per task spec; α=0.05.')
md.append('')
md.append('## Results')
md.append('')
md.append('| Ordering | first | last | wrap-edge d(last,first) | z | p₁ₛ |')
md.append('|---|---:|---:|---:|---:|---:|')
for name in ['mushaf', 'noldeke_1860', 'egyptian_1924', 'bell_1937', 'blachere_1947']:
    s = chrono_wrap_stats[name]
    md.append(f"| {name} | Q{s['first']} | Q{s['last']} | "
              f"{s['wrap_edge']:.4f} | {s['z']:+.3f} | "
              f"{s['p_one_sided_lower']:.4f} |")
md.append('')
md.append(f"Null wrap mean={null_mean:.4f}, sd={null_sd:.4f}, "
         f"median={null_median:.4f}, q05={null_quantiles['q05']:.4f}")
md.append('')
md.append('## Leaderboard (tightest wrap first)')
md.append('')
for i, (name, info) in enumerate(ranked, 1):
    tag = '  ← mushaf' if name == 'mushaf' else ''
    md.append(f"{i}. **{name}** d={info['wrap_edge']:.4f} "
              f"(Q{info['last']} → Q{info['first']}){tag}")
md.append('')
md.append('## Head-to-head Δ (negative ⇒ mushaf is tighter)')
md.append('')
md.append('| Chronology | d(last,first) | Δ = d_mushaf − d_chrono | Δ/SD | Interpretation |')
md.append('|---|---:|---:|---:|---|')
for name in ['noldeke_1860', 'egyptian_1924', 'bell_1937', 'blachere_1947']:
    h = head_to_head[name]
    md.append(f"| {name} | {h['chrono_wrap']:.4f} | "
              f"{h['delta_mushaf_minus_chrono']:+.4f} | "
              f"{h['delta_in_null_sd']:+.3f} | "
              f"{h['sign_interpretation']} |")
md.append('')
md.append('## Verdict')
md.append('')
md.append(f"- PRIMARY (mushaf wrap-edge vs permutation null): "
         f"p₁ₛ = {p_primary:.6f}, α = {ALPHA_BON} → "
         f"**{'PASS' if p_primary < ALPHA_BON else 'NULL'}**")
md.append(f"- Mushaf wrap tighter than ALL 4 chronologies? **{mushaf_beats_all}**")
md.append(f"- Mushaf rank among 5 orderings: **{mushaf_rank}/5**")
md.append('')
md.append('## Interpretation')
md.append('')
md.append('The ṭawāf-like wrap-around is the claim that the mushaf closes a '
         'geodesic loop: its last→first jump is short relative to a random '
         'endpoint pairing *and* relative to what each classical chronology '
         'would produce at its last→first transition.')
md.append('')
md.append('If the mushaf wrap is **tighter than all four chronologies** AND '
         'significantly tight vs the random null, the closure is a feature '
         'of the canonical order specifically, not an artifact of any '
         'reconstructed chronology.')
md.append('')
md.append('## Related findings')
md.append('- H-NEW-111 / H-NEW-212: provide the D matrix and whole-path analyses.')
md.append('- H-NEW-137: Q1 content-closeness to TERMINAL_TRIAD (Primary PASS).')
md.append('- H-NEW-144: cyclic TSP including the mushaf as a loop.')
md.append('- H-NEW-185: ring-Laplacian spectral test.')

OUT_MD.write_text('\n'.join(md))
print(f"Wrote: {OUT_MD}", file=sys.stderr)

# --- 9. Final stdout ----------------------------------------------------
print("\n" + "=" * 72, file=sys.stderr)
print("H-NEW-227 SUMMARY", file=sys.stderr)
print("=" * 72, file=sys.stderr)
print(f"  d(Q114,Q1) mushaf wrap = {d_mushaf_wrap:.4f}", file=sys.stderr)
print(f"  null(mean,sd,median) = ({null_mean:.4f}, {null_sd:.4f}, {null_median:.4f})", file=sys.stderr)
print(f"  p_1sided_lower = {p_primary:.6f}  (α_bon = {ALPHA_BON})  → "
      f"{'PASS' if p_primary < ALPHA_BON else 'NULL'}", file=sys.stderr)
for name in ['noldeke_1860', 'egyptian_1924', 'bell_1937', 'blachere_1947']:
    s = chrono_wrap_stats[name]
    print(f"  {name:15s}: d(Q{s['last']}→Q{s['first']})={s['wrap_edge']:.4f}  "
          f"Δ={head_to_head[name]['delta_mushaf_minus_chrono']:+.4f}",
          file=sys.stderr)
print(f"  mushaf wrap tighter than all 4 chronologies: {mushaf_beats_all}",
      file=sys.stderr)
print(f"  mushaf rank among 5: {mushaf_rank}/5", file=sys.stderr)
print("=" * 72, file=sys.stderr)
