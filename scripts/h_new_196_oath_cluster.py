#!/usr/bin/env python3
"""H-NEW-196 — Oath-opening surah structural cohesion.

Pre-registered (k=2, α_bon=0.025, seed=20260419):
  H1 (PRIMARY)   — M(oath-21) < M(random-21) under 10,000 perm null
  H2 (SECONDARY) — χ² mode-assignment vs uniform-5 k-means clustering

Reuses H-NEW-111 Fisher-Rao parameterization:
  K_TOP=500 stem roots, Dirichlet α=0.5, L1-normalized, Fisher-Rao metric.
"""
import csv
import hashlib
import json
import math
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PERMS = 10000
K_TOP = 500
DIRICHLET_ALPHA = 0.5
K_MODES = 5

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-196-oath-cluster-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/data/h-new-196.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"SEED = {SEED}  PERMS = {PERMS}  K_TOP = {K_TOP}  K_MODES = {K_MODES}",
      file=sys.stderr)

# H-NEW-85 locked oath-opener set
OATH_21 = [36, 37, 38, 43, 44, 50, 51, 52, 53, 68, 77, 79, 85, 86, 89, 91,
           92, 93, 95, 100, 103]
assert len(set(OATH_21)) == 21

# Task-stated alternate set (sensitivity)
TASK_LIST = [37, 51, 52, 53, 56, 68, 75, 76, 77, 78, 79, 81, 84, 85, 86, 89,
             90, 91, 92, 95, 100, 103]
print(f"task-stated list has {len(TASK_LIST)} items", file=sys.stderr)

# ---------------------------------------------------------------------------
# 0. Cell V — verify oath-list by scanning v1 for wa-qasam pattern
# ---------------------------------------------------------------------------
print("\n=== Cell V — v1 wa-prefix scan ===", file=sys.stderr)
with open(QURAN_JSON, encoding='utf-8') as f:
    quran = json.load(f)
assert len(quran) == 114

WAW_PREFIX = re.compile(r'^(وال|و)')  # "wa-l-" or "wa-"

v1_wa_opener = []  # (sid, v1_text, first_word)
for surah in quran:
    sid = surah['id']
    v1 = surah['verses'][0]['text']
    # Strip common separators (sajdah marks, qalqalah marks etc.)
    # then tokenize
    clean = re.sub(r'[ۚۛۖۗۘۙ]', ' ', v1).split()
    if not clean:
        continue
    # Check first 2 tokens (for cases like ص ۚ والقرآن where muq+waw-oath
    # is all on v1)
    for tok in clean[:2]:
        if tok.startswith('و') and not tok.startswith('والذين') and len(tok) > 1:
            v1_wa_opener.append((sid, tok, v1))
            break

# Also check v2 for muqaṭṭaʿāt surahs where real opener follows
# H-NEW-85 includes Q 36, 38, 43, 44, 50, 68 — all have muq v1, wa-oath v2
muq_surahs = {36, 38, 43, 44, 50, 68, 2, 3, 7, 10, 11, 12, 13, 14, 15, 19,
              20, 26, 27, 28, 29, 30, 31, 32, 40, 41, 42, 45, 46}
v2_wa_after_muq = []
for surah in quran:
    sid = surah['id']
    if sid not in muq_surahs:
        continue
    if len(surah['verses']) < 2:
        continue
    v2 = surah['verses'][1]['text']
    words = v2.split()
    if not words:
        continue
    first = words[0]
    if first.startswith('و') and not first.startswith('والذين'):
        v2_wa_after_muq.append((sid, first, v2))

v1_sids = set(s for s, _, _ in v1_wa_opener)
v2_sids = set(s for s, _, _ in v2_wa_after_muq)
candidate_sids = v1_sids | v2_sids

print(f"v1 wa-opener (raw): {sorted(v1_sids)}", file=sys.stderr)
print(f"v2 wa-opener after muq: {sorted(v2_sids)}", file=sys.stderr)
print(f"candidate set |U| = {len(candidate_sids)}", file=sys.stderr)

oath_in_candidates = sum(1 for s in OATH_21 if s in candidate_sids)
print(f"OATH_21 ∩ candidates = {oath_in_candidates}/21", file=sys.stderr)
missing = [s for s in OATH_21 if s not in candidate_sids]
extras = [s for s in sorted(candidate_sids) if s not in OATH_21]
print(f"OATH_21 missing from scan: {missing}", file=sys.stderr)
print(f"scan extras not in OATH_21: {extras}", file=sys.stderr)

# Cell V: PASS if ≥19/21 match
cell_v_pass = oath_in_candidates >= 19

# ---------------------------------------------------------------------------
# 1. Parse QAC (reuse H-NEW-111 logic)
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_surah_roots = defaultdict(list)
global_root_counts = Counter()

with open(QAC_FILE, encoding='utf-8') as f:
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

n_surahs = len(per_surah_roots)
assert n_surahs == 114, f"Expected 114, got {n_surahs}"
print(f"\nparsed QAC: 114 surahs, {len(global_root_counts)} distinct roots",
      file=sys.stderr)

top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {r: i for i, r in enumerate(top_roots)}

# ---------------------------------------------------------------------------
# 2. Probability vectors + Fisher-Rao matrix
# ---------------------------------------------------------------------------
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

def fr_distance(i, j):
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

print("\nBuilding 114x114 Fisher-Rao matrix...", file=sys.stderr)
D = [[0.0] * 115 for _ in range(115)]
for i in range(1, 115):
    for j in range(i + 1, 115):
        d = fr_distance(i, j)
        D[i][j] = d
        D[j][i] = d

all_d = [D[i][j] for i in range(1, 115) for j in range(i + 1, 115)]
print(f"  D mean={statistics.mean(all_d):.4f} range=[{min(all_d):.4f}, {max(all_d):.4f}]",
      file=sys.stderr)

# ---------------------------------------------------------------------------
# 3. Cell H1 — mean-pairwise cluster cohesion
# ---------------------------------------------------------------------------
def mean_pairwise(subset):
    s = list(subset)
    n = len(s)
    if n < 2:
        return 0.0
    total = 0.0
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            total += D[s[i]][s[j]]
            count += 1
    return total / count

M_oath = mean_pairwise(OATH_21)
print(f"\nM(OATH_21) = {M_oath:.6f}", file=sys.stderr)

# Permutation null
rng = random.Random(SEED)
all_sids = list(range(1, 115))
null_Ms = []
for p in range(PERMS):
    sample = rng.sample(all_sids, 21)
    null_Ms.append(mean_pairwise(sample))
    if (p + 1) % 2000 == 0:
        print(f"  perm {p+1}/{PERMS}", file=sys.stderr)

null_sorted = sorted(null_Ms)
n_le = sum(1 for x in null_Ms if x <= M_oath)
p_H1 = (n_le + 1) / (PERMS + 1)

def quant(xs, q):
    n = len(xs)
    idx = max(0, min(n - 1, int(math.floor(q * n))))
    return xs[idx]

null_quant = {
    'min': null_sorted[0],
    'q01': quant(null_sorted, 0.01),
    'q025': quant(null_sorted, 0.025),
    'q05': quant(null_sorted, 0.05),
    'q50': quant(null_sorted, 0.50),
    'q95': quant(null_sorted, 0.95),
    'q99': quant(null_sorted, 0.99),
    'max': null_sorted[-1],
    'mean': statistics.mean(null_Ms),
    'sd': statistics.stdev(null_Ms),
}
z_oath = (M_oath - null_quant['mean']) / null_quant['sd']
print(f"  null mean={null_quant['mean']:.6f} sd={null_quant['sd']:.6f}",
      file=sys.stderr)
print(f"  z(M_oath) = {z_oath:.4f}", file=sys.stderr)
print(f"  p_H1 (one-sided lower) = {p_H1:.6f}", file=sys.stderr)

cell_h1_pass = p_H1 < 0.025

# ---------------------------------------------------------------------------
# Sensitivity: task-stated list
# ---------------------------------------------------------------------------
task_valid = [s for s in TASK_LIST if 1 <= s <= 114]
M_task = mean_pairwise(task_valid)
# separate null of size len(task_valid)
rng2 = random.Random(SEED + 1)
null_task = []
for p in range(PERMS):
    sample = rng2.sample(all_sids, len(task_valid))
    null_task.append(mean_pairwise(sample))
n_le_task = sum(1 for x in null_task if x <= M_task)
p_task = (n_le_task + 1) / (PERMS + 1)
print(f"\nSENSITIVITY: task-list M={M_task:.6f} p={p_task:.6f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 4. Cell H2 — k-means mode assignment
# ---------------------------------------------------------------------------
# k-means on sqrt_prob (square-root transform = Hellinger embedding)
# sq Euclidean in sqrt-prob space ≈ Hellinger^2 ≈ first-order approx to FR
def l2_sq(a, b):
    s = 0.0
    for k in range(K_TOP):
        d = a[k] - b[k]
        s += d * d
    return s

def mean_vec(vs):
    n = len(vs)
    if n == 0:
        return [0.0] * K_TOP
    out = [0.0] * K_TOP
    for v in vs:
        for k in range(K_TOP):
            out[k] += v[k]
    return [x / n for x in out]

def kmeans(data, k, seed, max_iter=100):
    rng = random.Random(seed)
    n = len(data)
    # k-means++ init
    first = rng.randrange(n)
    centers = [data[first][:]]
    while len(centers) < k:
        # weighted by min distance^2
        d2 = []
        for i in range(n):
            mn = min(l2_sq(data[i], c) for c in centers)
            d2.append(mn)
        tot = sum(d2)
        if tot <= 0:
            # pick random
            centers.append(data[rng.randrange(n)][:])
            continue
        r = rng.random() * tot
        cum = 0.0
        picked = 0
        for i, v in enumerate(d2):
            cum += v
            if cum >= r:
                picked = i
                break
        centers.append(data[picked][:])
    # lloyd iterations
    assign = [0] * n
    for it in range(max_iter):
        new_assign = []
        for i in range(n):
            best_c = 0
            best_d = float('inf')
            for c_i, c in enumerate(centers):
                d = l2_sq(data[i], c)
                if d < best_d:
                    best_d = d
                    best_c = c_i
            new_assign.append(best_c)
        if new_assign == assign and it > 0:
            break
        assign = new_assign
        # update centers
        new_centers = []
        for c_i in range(k):
            members = [data[i] for i in range(n) if assign[i] == c_i]
            if not members:
                # re-init to furthest point
                far_i = max(range(n),
                            key=lambda i: min(l2_sq(data[i], c) for c in centers))
                new_centers.append(data[far_i][:])
            else:
                new_centers.append(mean_vec(members))
        centers = new_centers
    return assign, centers

# Input to k-means: sqrt-prob rows 1..114 (index 0..113)
km_input = [sqrt_prob[sid] for sid in range(1, 115)]
assign, centers = kmeans(km_input, K_MODES, SEED)
# Map sid -> mode
sid_mode = {sid: assign[sid - 1] for sid in range(1, 115)}
mode_counts = Counter(assign)
print(f"\n=== Cell H2 — k-means k={K_MODES} mode counts (all 114) ===",
      file=sys.stderr)
for m in range(K_MODES):
    print(f"  mode {m}: {mode_counts[m]} surahs", file=sys.stderr)

# OATH_21 per mode
oath_mode_counts = Counter(sid_mode[s] for s in OATH_21)
print(f"\n=== OATH_21 distribution per mode ===", file=sys.stderr)
for m in range(K_MODES):
    print(f"  mode {m}: {oath_mode_counts[m]} oath-surahs "
          f"(of {mode_counts[m]} total; rate={oath_mode_counts[m]/max(1,mode_counts[m]):.3f})",
          file=sys.stderr)

# χ² vs expected proportional to mode sizes
# H0: oath-21 distributes proportionally to global mode sizes
expected = {m: 21.0 * mode_counts[m] / 114.0 for m in range(K_MODES)}
chi2 = 0.0
for m in range(K_MODES):
    e = expected[m]
    o = oath_mode_counts[m]
    if e > 0:
        chi2 += (o - e) ** 2 / e
df = K_MODES - 1

# approximate p via permutation rather than relying on chi-sq table
# null: sample 21 without replacement from 114, repeat 10000x
rng3 = random.Random(SEED + 2)
null_chi2 = []
for p in range(PERMS):
    sample = rng3.sample(all_sids, 21)
    c = Counter(sid_mode[s] for s in sample)
    ch = 0.0
    for m in range(K_MODES):
        e = expected[m]
        o = c[m]
        if e > 0:
            ch += (o - e) ** 2 / e
    null_chi2.append(ch)
n_ge_chi2 = sum(1 for x in null_chi2 if x >= chi2)
p_H2 = (n_ge_chi2 + 1) / (PERMS + 1)
print(f"  χ² observed = {chi2:.4f}  df={df}  p_perm = {p_H2:.6f}",
      file=sys.stderr)
cell_h2_pass = p_H2 < 0.025

# ---------------------------------------------------------------------------
# 5. Write results
# ---------------------------------------------------------------------------
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)

# Identify dominant oath mode
dominant_oath_mode = max(oath_mode_counts, key=oath_mode_counts.get)
dominant_rate = oath_mode_counts[dominant_oath_mode] / 21

# Per-mode exemplars (up to 5 per mode)
mode_surahs = defaultdict(list)
for sid, m in sid_mode.items():
    mode_surahs[m].append(sid)

results = {
    'finding_id': 'h-new-196-oath-cluster',
    'prereg_sha256': prereg_sha,
    'seed': SEED,
    'perms': PERMS,
    'k_top_roots': K_TOP,
    'k_modes': K_MODES,
    'dirichlet_alpha': DIRICHLET_ALPHA,
    'oath_21_locked': OATH_21,
    'cell_v': {
        'v1_wa_opener_sids': sorted(v1_sids),
        'v2_wa_after_muq_sids': sorted(v2_sids),
        'candidate_set': sorted(candidate_sids),
        'oath_21_in_candidates': oath_in_candidates,
        'oath_21_missing_from_scan': missing,
        'scan_extras_not_in_oath_21': extras,
        'verdict': 'PASS' if cell_v_pass else 'NULL',
    },
    'cell_h1': {
        'M_oath': M_oath,
        'null_stats': null_quant,
        'z_oath': z_oath,
        'p_H1_one_sided_lower': p_H1,
        'verdict': 'PASS' if cell_h1_pass else 'NULL',
        'alpha_bon': 0.025,
    },
    'cell_h1_sensitivity_task_list': {
        'task_list': task_valid,
        'n': len(task_valid),
        'M_task': M_task,
        'p_task': p_task,
    },
    'cell_h2': {
        'mode_counts_all': dict(mode_counts),
        'oath_mode_counts': dict(oath_mode_counts),
        'expected_by_mode': expected,
        'chi2': chi2,
        'df': df,
        'p_H2_perm': p_H2,
        'verdict': 'PASS' if cell_h2_pass else 'NULL',
        'dominant_oath_mode': dominant_oath_mode,
        'dominant_oath_mode_count': oath_mode_counts[dominant_oath_mode],
        'dominant_oath_mode_rate': dominant_rate,
        'dominant_mode_total_size': mode_counts[dominant_oath_mode],
        'dominant_mode_members': sorted(mode_surahs[dominant_oath_mode]),
        'alpha_bon': 0.025,
    },
    'sid_mode_assignments': sid_mode,
    'oath_per_sid_mode': {s: sid_mode[s] for s in OATH_21},
    'bonferroni_k': 2,
    'summary_verdict': {
        'cell_v': 'PASS' if cell_v_pass else 'NULL',
        'cell_h1': 'PASS' if cell_h1_pass else 'NULL',
        'cell_h2': 'PASS' if cell_h2_pass else 'NULL',
    },
}
with open(OUT_JSON, 'w') as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nWrote {OUT_JSON}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. Stdout summary
# ---------------------------------------------------------------------------
print("")
print("=" * 60)
print("H-NEW-196 SUMMARY")
print("=" * 60)
print(f"Cell V: oath_21_in_candidates = {oath_in_candidates}/21 "
      f"→ {'PASS' if cell_v_pass else 'NULL'}")
print(f"Cell H1: M_oath={M_oath:.6f} vs null mean={null_quant['mean']:.6f}  "
      f"z={z_oath:.3f}  p={p_H1:.6f}  "
      f"→ {'PASS' if cell_h1_pass else 'NULL'}")
print(f"  Sensitivity task-list (n={len(task_valid)}): "
      f"M={M_task:.6f} p={p_task:.6f}")
print(f"Cell H2: χ²={chi2:.3f}  p={p_H2:.6f}  "
      f"dominant_mode={dominant_oath_mode} "
      f"({oath_mode_counts[dominant_oath_mode]}/21 oath surahs, "
      f"of {mode_counts[dominant_oath_mode]} total in mode)  "
      f"→ {'PASS' if cell_h2_pass else 'NULL'}")
print(f"Bonferroni k=2, α_bon=0.025")
