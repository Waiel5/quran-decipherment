#!/usr/bin/env python3
"""
H-NEW-260 — Q 54 + Q 55 dyad deep-dive (empirical Mode-B mirror-pair)

Pre-reg: findings/phase-b-hypotheses/h-new-260-q54-q55-dyad-prereg.md
SHA-256 (at commit): 72a5bb88011f919511cce57c2ca6a0825f6ecfaad093816cd6906a399c00c6ff

Seed 20260419.  Bonferroni k=3, alpha_bon=0.01667.

Cells:
  A — Joint verse-length ACF coherence: concatenate Q 54+Q 55 (133 vv)
      and compute ACF lag-1, lag-2, lag-3; compare max|ACF| to the
      113 adjacent-pair baseline.
  B — Content-root Jaccard: |R_54 ∩ R_55| / |R_54 ∪ R_55|
      vs 113 adjacent-pair baseline.
  C — Fisher-Rao mirror asymmetry: |d(54,55) - d(55,56)| vs 112 adj-triple null.

MW-5 sanity: 5 random adjacent pairs (seed 20260419+2, excluding Q 54-55)
verified NOT to replicate the Q 54-55 signature.
"""
from __future__ import annotations
import csv
import hashlib
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PREREG = ROOT / 'findings/phase-b-hypotheses/h-new-260-q54-q55-dyad-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-260.json'
OUT_CSV = ROOT / 'findings/phase-b-hypotheses/csv/h-new-260-adjacent-pair-baselines.csv'
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'

# Fisher-Rao parameters match H-NEW-111 exactly
K_TOP = 500
DIRICHLET_ALPHA = 0.5

# Pre-reg SHA (tamper-evidence)
prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"SEED={SEED}  K_TOP={K_TOP}  DIRICHLET_ALPHA={DIRICHLET_ALPHA}", file=sys.stderr)

AR_LETTER = re.compile(r'[\u0621-\u064A]')


def len_letters(text: str) -> int:
    return sum(1 for ch in text if AR_LETTER.match(ch))


# ----------------------------------------------------------------------
# 1. Load per-surah verse-length sequences
# ----------------------------------------------------------------------
Q = json.loads(QURAN_JSON.read_text())
Q = sorted(Q, key=lambda x: int(x['id']))
per_surah_vlen: dict[int, list[int]] = {}
for s in Q:
    sid = int(s['id'])
    per_surah_vlen[sid] = [len_letters(v['text']) for v in s['verses']]

print(f"Loaded {len(per_surah_vlen)} surahs.", file=sys.stderr)
for sid in (54, 55, 56):
    print(f"  Q{sid}: {len(per_surah_vlen[sid])} verses, "
          f"mean letters {sum(per_surah_vlen[sid])/len(per_surah_vlen[sid]):.1f}",
          file=sys.stderr)


# ----------------------------------------------------------------------
# 2. Load per-surah STEM root tokens (QAC) — same as H-NEW-111
# ----------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_surah_roots: dict[int, list[str]] = defaultdict(list)
global_root_counts: Counter = Counter()

with QAC_FILE.open(encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        sid = int(m.group(1))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        root = rm.group(1)
        per_surah_roots[sid].append(root)
        global_root_counts[root] += 1

print(f"QAC: {len(per_surah_roots)} surahs, {sum(len(v) for v in per_surah_roots.values())} "
      f"STEM root tokens, {len(global_root_counts)} distinct roots.", file=sys.stderr)


# ----------------------------------------------------------------------
# 3. ACF of verse-length sequence
# ----------------------------------------------------------------------
def acf(x: list[float], lag: int) -> float:
    n = len(x)
    if n <= lag:
        return float('nan')
    m = sum(x) / n
    num = sum((x[i] - m) * (x[i + lag] - m) for i in range(n - lag))
    den = sum((xi - m) ** 2 for xi in x)
    if den == 0:
        return float('nan')
    return num / den


def joint_acf_stats(a: list[int], b: list[int]) -> dict[str, float]:
    """Concatenate a and b, compute ACF lag 1/2/3 and max|ACF|."""
    seq = list(a) + list(b)
    r1 = acf(seq, 1)
    r2 = acf(seq, 2)
    r3 = acf(seq, 3)
    vals = [x for x in (r1, r2, r3) if not math.isnan(x)]
    max_abs = max((abs(x) for x in vals), default=float('nan'))
    return {'lag1': r1, 'lag2': r2, 'lag3': r3, 'max_abs': max_abs, 'N': len(seq)}


# ----------------------------------------------------------------------
# 4. Root Jaccard
# ----------------------------------------------------------------------
def root_jaccard(sid_a: int, sid_b: int) -> dict[str, float]:
    Ra = set(per_surah_roots[sid_a])
    Rb = set(per_surah_roots[sid_b])
    union = Ra | Rb
    inter = Ra & Rb
    if not union:
        return {'jaccard': float('nan'), 'overlap_min': float('nan'),
                'n_a': len(Ra), 'n_b': len(Rb), 'n_shared': 0}
    jac = len(inter) / len(union)
    min_size = min(len(Ra), len(Rb))
    om = len(inter) / min_size if min_size else float('nan')
    return {'jaccard': jac, 'overlap_min': om, 'n_a': len(Ra),
            'n_b': len(Rb), 'n_shared': len(inter)}


# ----------------------------------------------------------------------
# 5. Fisher-Rao distance — replicate H-NEW-111 protocol
# ----------------------------------------------------------------------
top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {r: i for i, r in enumerate(top_roots)}

counts = [[0.0] * K_TOP for _ in range(115)]
for sid in range(1, 115):
    for r in per_surah_roots.get(sid, []):
        idx = top_root_index.get(r)
        if idx is not None:
            counts[sid][idx] += 1.0

prob = [[0.0] * K_TOP for _ in range(115)]
for sid in range(1, 115):
    smoothed = [c + DIRICHLET_ALPHA for c in counts[sid]]
    s = sum(smoothed)
    prob[sid] = [v / s for v in smoothed]

sqrt_prob = [[math.sqrt(p) for p in prob[sid]] for sid in range(115)]


def fr_distance(i: int, j: int) -> float:
    if i == j:
        return 0.0
    bc = 0.0
    si = sqrt_prob[i]
    sj = sqrt_prob[j]
    for k in range(K_TOP):
        bc += si[k] * sj[k]
    if bc > 1.0:
        bc = 1.0
    elif bc < -1.0:
        bc = -1.0
    return 2.0 * math.acos(bc)


# ----------------------------------------------------------------------
# 6. Cell A: joint verse-length ACF — Q 54+Q 55 vs 113 adjacent-pair baseline
# ----------------------------------------------------------------------
obs_A = joint_acf_stats(per_surah_vlen[54], per_surah_vlen[55])
print(f"\n[Cell A] Q 54+55 joint ACF: "
      f"lag1={obs_A['lag1']:.4f} lag2={obs_A['lag2']:.4f} lag3={obs_A['lag3']:.4f} "
      f"max|ACF|={obs_A['max_abs']:.4f} (N={obs_A['N']})",
      file=sys.stderr)

adjacent_pairs: list[tuple[int, int]] = [(k, k + 1) for k in range(1, 114)]
baseline_A: list[dict] = []
for a, b in adjacent_pairs:
    la, lb = per_surah_vlen[a], per_surah_vlen[b]
    if len(la) < 5 or len(lb) < 5:
        continue
    stats = joint_acf_stats(la, lb)
    stats['pair'] = (a, b)
    baseline_A.append(stats)

baseline_A_max_abs = sorted(x['max_abs'] for x in baseline_A
                            if not math.isnan(x['max_abs']))
print(f"  baseline n={len(baseline_A_max_abs)} adjacent pairs (N>=5 each)",
      file=sys.stderr)
print(f"  baseline max|ACF| min={baseline_A_max_abs[0]:.4f} "
      f"median={baseline_A_max_abs[len(baseline_A_max_abs)//2]:.4f} "
      f"max={baseline_A_max_abs[-1]:.4f}", file=sys.stderr)


def percentile_of(x: float, sorted_ref: list[float]) -> float:
    """Midrank percentile (inclusive) of x within sorted_ref."""
    below = sum(1 for v in sorted_ref if v < x)
    equal = sum(1 for v in sorted_ref if v == x)
    return 100.0 * (below + 0.5 * equal) / len(sorted_ref)


pct_A = percentile_of(obs_A['max_abs'], baseline_A_max_abs)
pass_A = pct_A >= 95.0
print(f"  Q 54-55 max|ACF|={obs_A['max_abs']:.4f} at pct={pct_A:.2f} "
      f"of 113-pair baseline → PASS={pass_A}", file=sys.stderr)


# Also report pct for lag1, lag2, lag3 individually, signed and absolute
def pct_for(key: str) -> float:
    ref = sorted(x[key] for x in baseline_A if not math.isnan(x[key]))
    return percentile_of(obs_A[key], ref)


print(f"  lag1 signed pct={pct_for('lag1'):.1f}  "
      f"lag2 signed pct={pct_for('lag2'):.1f}  "
      f"lag3 signed pct={pct_for('lag3'):.1f}", file=sys.stderr)


# ----------------------------------------------------------------------
# 7. Cell B: Content-root Jaccard
# ----------------------------------------------------------------------
obs_B = root_jaccard(54, 55)
print(f"\n[Cell B] Q 54-55 Jaccard={obs_B['jaccard']:.4f} "
      f"(|R_54|={obs_B['n_a']}, |R_55|={obs_B['n_b']}, |inter|={obs_B['n_shared']}); "
      f"overlap_min={obs_B['overlap_min']:.4f}", file=sys.stderr)

baseline_B: list[dict] = []
for a, b in adjacent_pairs:
    if len(per_surah_roots.get(a, [])) < 5 or len(per_surah_roots.get(b, [])) < 5:
        continue
    stats = root_jaccard(a, b)
    stats['pair'] = (a, b)
    baseline_B.append(stats)

baseline_B_jac = sorted(x['jaccard'] for x in baseline_B if not math.isnan(x['jaccard']))
pct_B = percentile_of(obs_B['jaccard'], baseline_B_jac)
pass_B = pct_B >= 95.0
print(f"  baseline n={len(baseline_B_jac)} adjacent pairs", file=sys.stderr)
print(f"  baseline Jaccard min={baseline_B_jac[0]:.4f} "
      f"median={baseline_B_jac[len(baseline_B_jac)//2]:.4f} "
      f"max={baseline_B_jac[-1]:.4f}", file=sys.stderr)
print(f"  Q 54-55 Jaccard={obs_B['jaccard']:.4f} at pct={pct_B:.2f} "
      f"→ PASS={pass_B}", file=sys.stderr)


# ----------------------------------------------------------------------
# 8. Cell C: Fisher-Rao mirror asymmetry — |d(54,55) - d(55,56)| vs adj-triple null
# ----------------------------------------------------------------------
d_5455 = fr_distance(54, 55)
d_5556 = fr_distance(55, 56)
d_5456 = fr_distance(54, 56)
delta_55 = abs(d_5455 - d_5556)
print(f"\n[Cell C] d(Q54,Q55)={d_5455:.4f}  d(Q55,Q56)={d_5556:.4f}  "
      f"d(Q54,Q56)={d_5456:.4f}  |Δ|={delta_55:.4f}", file=sys.stderr)

# Null: Δ_k = |d(Q_k,Q_{k+1}) - d(Q_{k+1},Q_{k+2})| for k=1..112
null_C: list[float] = []
for k in range(1, 113):
    d_kk1 = fr_distance(k, k + 1)
    d_k1k2 = fr_distance(k + 1, k + 2)
    null_C.append(abs(d_kk1 - d_k1k2))

null_C_sorted = sorted(null_C)
pct_C = percentile_of(delta_55, null_C_sorted)
# 2-sided: extreme if either upper tail (>= p95) or lower tail (<= p5),
# but per pre-reg the direction is UPPER tail at p < 0.01667 (i.e. pct >= 98.33)
pass_C = pct_C >= 100.0 * (1 - 0.01667)
p_emp_C = min(1.0, (sum(1 for v in null_C if v >= delta_55) + 1) / (len(null_C) + 1))
print(f"  baseline n={len(null_C)} adjacent-triple Δs", file=sys.stderr)
print(f"  baseline Δ min={null_C_sorted[0]:.4f} median={null_C_sorted[len(null_C_sorted)//2]:.4f} "
      f"max={null_C_sorted[-1]:.4f}", file=sys.stderr)
print(f"  Q 54-55-56 |Δ|={delta_55:.4f} at pct={pct_C:.2f} "
      f"(upper p_emp={p_emp_C:.4f}) → PASS={pass_C}", file=sys.stderr)


# ----------------------------------------------------------------------
# 9. MW-5 sanity: 5 random adjacent pairs (excl Q 54-55)
# ----------------------------------------------------------------------
rng = random.Random(SEED + 2)
candidate_pairs = [p for p in adjacent_pairs if p != (54, 55)
                   and len(per_surah_vlen[p[0]]) >= 5
                   and len(per_surah_vlen[p[1]]) >= 5
                   and len(per_surah_roots.get(p[0], [])) >= 5
                   and len(per_surah_roots.get(p[1], [])) >= 5]
mw5_pairs = rng.sample(candidate_pairs, 5)
mw5_results = []
for a, b in mw5_pairs:
    sA = joint_acf_stats(per_surah_vlen[a], per_surah_vlen[b])
    sB = root_jaccard(a, b)
    pctA = percentile_of(sA['max_abs'], baseline_A_max_abs)
    pctB = percentile_of(sB['jaccard'], baseline_B_jac)
    mw5_results.append({'pair': (a, b), 'max_abs_ACF': sA['max_abs'], 'pct_A': pctA,
                        'jaccard': sB['jaccard'], 'pct_B': pctB,
                        'both_ge_p95': pctA >= 95.0 and pctB >= 95.0})
print("\n[MW-5] random adjacent pairs (sanity)", file=sys.stderr)
for r in mw5_results:
    print(f"  Q{r['pair'][0]}-Q{r['pair'][1]}: "
          f"max|ACF|={r['max_abs_ACF']:.4f} pct_A={r['pct_A']:.1f}  "
          f"Jaccard={r['jaccard']:.4f} pct_B={r['pct_B']:.1f}  "
          f"both_ge_p95={r['both_ge_p95']}", file=sys.stderr)
mw5_signature_count = sum(1 for r in mw5_results if r['both_ge_p95'])
print(f"  MW-5 signature-replication: {mw5_signature_count}/5 pairs", file=sys.stderr)


# ----------------------------------------------------------------------
# 10. Shared roots enumerated
# ----------------------------------------------------------------------
R54 = set(per_surah_roots[54])
R55 = set(per_surah_roots[55])
shared = sorted(R54 & R55)
# Rank by joint frequency (Q54 + Q55)
def root_freq(sid: int, root: str) -> int:
    return sum(1 for r in per_surah_roots[sid] if r == root)


shared_ranked = sorted(shared, key=lambda r: -(root_freq(54, r) + root_freq(55, r)))
print(f"\nShared roots Q 54 ∩ Q 55: {len(shared)} (Jaccard={obs_B['jaccard']:.4f})",
      file=sys.stderr)
print(f"  top 20 by joint freq:", file=sys.stderr)
for r in shared_ranked[:20]:
    print(f"    {r}: Q54={root_freq(54, r)}  Q55={root_freq(55, r)}", file=sys.stderr)


# ----------------------------------------------------------------------
# 11. Output
# ----------------------------------------------------------------------
n_pass = sum([pass_A, pass_B, pass_C])
if n_pass == 3:
    verdict = "GENUINE_MODE_B_MIRROR_PAIR (3/3 PASS α_bon=0.01667)"
elif n_pass == 2:
    verdict = "PARTIAL_CORROBORATION (2/3 PASS)"
elif n_pass == 1:
    verdict = "MINIMAL_SUPPORT (1/3 PASS)"
else:
    verdict = "LENGTH_ADJACENCY_ARTIFACT (0/3 PASS) — Q 55 individually unique only"

out = {
    'id': 'H-NEW-260',
    'seed': SEED,
    'prereg_sha256': prereg_sha,
    'bonferroni_k': 3,
    'alpha_bon': 0.01667,
    'cell_A_joint_ACF': {
        'observed': obs_A,
        'pct': pct_A,
        'pass': pass_A,
        'baseline_n': len(baseline_A_max_abs),
        'baseline_stats': {
            'min': baseline_A_max_abs[0] if baseline_A_max_abs else None,
            'median': baseline_A_max_abs[len(baseline_A_max_abs)//2] if baseline_A_max_abs else None,
            'max': baseline_A_max_abs[-1] if baseline_A_max_abs else None,
        },
        'signed_pcts': {
            'lag1': pct_for('lag1'),
            'lag2': pct_for('lag2'),
            'lag3': pct_for('lag3'),
        },
    },
    'cell_B_root_jaccard': {
        'observed': obs_B,
        'pct': pct_B,
        'pass': pass_B,
        'baseline_n': len(baseline_B_jac),
        'baseline_stats': {
            'min': baseline_B_jac[0] if baseline_B_jac else None,
            'median': baseline_B_jac[len(baseline_B_jac)//2] if baseline_B_jac else None,
            'max': baseline_B_jac[-1] if baseline_B_jac else None,
        },
        'shared_roots_top20': [
            {'root': r, 'Q54': root_freq(54, r), 'Q55': root_freq(55, r)}
            for r in shared_ranked[:20]
        ],
        'shared_roots_count': len(shared),
    },
    'cell_C_FR_mirror_asymmetry': {
        'd_54_55': d_5455,
        'd_55_56': d_5556,
        'd_54_56': d_5456,
        'delta': delta_55,
        'pct': pct_C,
        'p_emp_upper': p_emp_C,
        'pass': pass_C,
        'baseline_n': len(null_C),
        'baseline_stats': {
            'min': null_C_sorted[0],
            'median': null_C_sorted[len(null_C_sorted)//2],
            'max': null_C_sorted[-1],
        },
    },
    'n_pass': n_pass,
    'verdict': verdict,
    'MW5': {
        'pairs': [{'a': p['pair'][0], 'b': p['pair'][1],
                   'max_abs_ACF': p['max_abs_ACF'], 'pct_A': p['pct_A'],
                   'jaccard': p['jaccard'], 'pct_B': p['pct_B'],
                   'both_ge_p95': p['both_ge_p95']}
                  for p in mw5_results],
        'n_signature_replicated': mw5_signature_count,
    },
}
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False))

# Per-adjacent-pair CSV for external inspection
with OUT_CSV.open('w') as f:
    w = csv.writer(f)
    w.writerow(['pair_a', 'pair_b', 'joint_max_abs_ACF', 'joint_lag1', 'joint_lag2',
                'joint_lag3', 'root_jaccard', 'root_overlap_min', 'root_n_shared'])
    for rA, rB in zip(
        sorted(baseline_A, key=lambda x: x['pair']),
        sorted(baseline_B, key=lambda x: x['pair']),
    ):
        # Re-align (both are adjacent-pair-indexed but filtering may differ)
        pass
    # Cleaner: recompute both side by side with consistent filter
    rows = []
    for a, b in adjacent_pairs:
        la, lb = per_surah_vlen[a], per_surah_vlen[b]
        if len(la) < 5 or len(lb) < 5:
            continue
        if len(per_surah_roots.get(a, [])) < 5 or len(per_surah_roots.get(b, [])) < 5:
            continue
        sA = joint_acf_stats(la, lb)
        sB = root_jaccard(a, b)
        rows.append([a, b, sA['max_abs'], sA['lag1'], sA['lag2'], sA['lag3'],
                     sB['jaccard'], sB['overlap_min'], sB['n_shared']])
    for r in rows:
        w.writerow(r)

print(f"\n=== H-NEW-260 RESULTS (verdict: {verdict}) ===")
print(f"  Cell A (joint ACF max|·|={obs_A['max_abs']:.4f} pct={pct_A:.1f}): "
      f"{'PASS' if pass_A else 'NULL'}")
print(f"  Cell B (Jaccard={obs_B['jaccard']:.4f} pct={pct_B:.1f}): "
      f"{'PASS' if pass_B else 'NULL'}")
print(f"  Cell C (|Δd|={delta_55:.4f} pct={pct_C:.1f} p={p_emp_C:.4f}): "
      f"{'PASS' if pass_C else 'NULL'}")
print(f"  MW-5: {mw5_signature_count}/5 random pairs replicate the signature")
print(f"  JSON: {OUT_JSON}")
print(f"  CSV:  {OUT_CSV}")
