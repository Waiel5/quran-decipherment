#!/usr/bin/env python3
"""H-NEW-228 — Simulated annealing for MINIMUM conditional-entropy surah ordering.

Parent: h-new-171 (H_mushaf = 50.15 bits; H_null_mean = 82.92 bits; greedy-NN = 20.92).

Cost: H_hat(s_{i+1} | s_i) under rank-exp kernel, computed identically to h-new-171.
SA proposal: 2-opt segment reversal (length uniform [2, 30]).
Schedule: geometric, T_0=5.0 bits → T_f=0.001 bits over 500_000 steps.
Starts: mushaf, Nöldeke, random. Seeds: SEED+0/1/2. Master SEED = 20260419.

Descriptive quantities:
    H_min_SA = min over 3 runs of final-best H
    gap_fraction = (H_mushaf - H_min_SA) / (H_null_mean - H_min_SA)

Gating: did SA beat H_mushaf from all 3 starts? (α_bon=0.05, k=1)
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
K_TOP = 100
DIRICHLET_ALPHA = 0.5

SA_STEPS = 500_000
T_0 = 5.0
T_FINAL = 0.001
SEG_MIN = 2
SEG_MAX = 30

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-228-sa-min-entropy-ordering-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-228.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"K_TOP={K_TOP} SA_STEPS={SA_STEPS} T_0={T_0} T_FINAL={T_FINAL} SEED={SEED}",
      file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Parse QAC (same as h-new-171)
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

assert len(per_surah_roots) == 114
total_tokens = sum(len(v) for v in per_surah_roots.values())
top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {r: i for i, r in enumerate(top_roots)}

# ---------------------------------------------------------------------------
# 2. Probability vectors, Fisher-Rao distance, rank matrix, cond-logp
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
    if bc > 1.0: bc = 1.0
    elif bc < -1.0: bc = -1.0
    return 2.0 * math.acos(bc)

print("Building 114x114 Fisher-Rao distance matrix...", file=sys.stderr)
D = [[0.0] * 115 for _ in range(115)]
for i in range(1, 115):
    for j in range(i + 1, 115):
        d = fr_distance(i, j)
        D[i][j] = d
        D[j][i] = d

print("Computing rank matrix...", file=sys.stderr)
rank_of = [[0] * 115 for _ in range(115)]
for i in range(1, 115):
    others = [(j, D[i][j]) for j in range(1, 115) if j != i]
    others.sort(key=lambda t: t[1])
    for pos, (j, _) in enumerate(others, start=1):
        rank_of[i][j] = pos

log2 = math.log(2.0)
cond_logp = [[0.0] * 115 for _ in range(115)]  # log2 p_hat(j | i)
for i in range(1, 115):
    raw = [math.exp(-rank_of[i][j]) if j != i else 0.0 for j in range(115)]
    Z = sum(raw)
    for j in range(1, 115):
        if j == i:
            continue
        p = raw[j] / Z
        cond_logp[i][j] = math.log(p) / log2

# ---------------------------------------------------------------------------
# 3. Metrics
# ---------------------------------------------------------------------------
def cond_entropy_sum(order):
    """Return SUM of -log2 p terms (undivided) over order[i]->order[i+1]."""
    s = 0.0
    n = len(order) - 1
    for i in range(n):
        s -= cond_logp[order[i]][order[i + 1]]
    return s

def cond_entropy(order):
    n = len(order) - 1
    return cond_entropy_sum(order) / n

# ---------------------------------------------------------------------------
# 4. Reference values
# ---------------------------------------------------------------------------
mushaf_order = list(range(1, 115))
H_mushaf = cond_entropy(mushaf_order)
print(f"\nH_mushaf = {H_mushaf:.4f} bits", file=sys.stderr)

mushaf_to_noldeke = {}
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        mushaf_to_noldeke[int(row['mushaf_order'])] = int(row['noldeke_order'])
noldeke_order_list = sorted(range(1, 115), key=lambda sid: mushaf_to_noldeke[sid])
H_noldeke = cond_entropy(noldeke_order_list)
print(f"H_noldeke = {H_noldeke:.4f} bits", file=sys.stderr)

# Random-start permutation (seeded from master SEED so it's reproducible)
rng_master = random.Random(SEED)
random_start_order = list(range(1, 115))
rng_master.shuffle(random_start_order)
H_random_start = cond_entropy(random_start_order)
print(f"H_random_start = {H_random_start:.4f} bits", file=sys.stderr)

# H_null_mean from h-new-171 (hard-coded reference; was 82.92 bits)
# We also recompute a quick null mean from 1000 random perms for sanity.
rng_null = random.Random(SEED + 999)
quick_null_H = []
for _ in range(1000):
    p = list(range(1, 115))
    rng_null.shuffle(p)
    quick_null_H.append(cond_entropy(p))
H_null_mean_quick = statistics.mean(quick_null_H)
H_null_sd_quick = statistics.stdev(quick_null_H)
print(f"H_null (1000 perms, quick sanity): mean={H_null_mean_quick:.4f} sd={H_null_sd_quick:.4f}",
      file=sys.stderr)

# ---------------------------------------------------------------------------
# 5. SA core
# ---------------------------------------------------------------------------
def sa_run(start_order, run_seed, label):
    """2-opt SA on conditional entropy. Returns (best_order, history)."""
    rng = random.Random(run_seed)
    order = list(start_order)
    # cost tracked as SUM of -log2 p_hat; divide by n-1 only when reporting
    cur_sum = cond_entropy_sum(order)
    best_sum = cur_sum
    best_order = list(order)
    beta = (T_FINAL / T_0) ** (1.0 / SA_STEPS)
    T = T_0
    n = len(order)
    n_minus_1 = n - 1  # divisor for H

    accepts = 0
    accepts_uphill = 0
    proposals = 0

    history = []  # (step, T, cur_H, best_H)
    history_stride = max(1, SA_STEPS // 200)

    for step in range(SA_STEPS):
        # Proposal: 2-opt segment reversal
        seg_len = rng.randint(SEG_MIN, SEG_MAX)
        i = rng.randint(0, n - seg_len)
        j = i + seg_len - 1  # inclusive endpoints of segment to reverse
        # Delta-cost: changes occur at edges (i-1, i), (j, j+1) before and
        # (i-1, j), (i, j+1) after, and the internal reversed edges change
        # direction. Because our kernel cond_logp[a][b] != cond_logp[b][a]
        # in general, internal edges DO change cost under reversal.
        # So we evaluate the swap cost by direct diff on the affected region.

        # Collect pre-cost of all edges touching [i-1 .. j+1]
        pre_edges_sum = 0.0
        # edge (i-1, i): exists iff i >= 1
        if i >= 1:
            pre_edges_sum += -cond_logp[order[i-1]][order[i]]
        # internal edges within [i..j]: (i,i+1)..(j-1,j)
        for k in range(i, j):
            pre_edges_sum += -cond_logp[order[k]][order[k+1]]
        # edge (j, j+1): exists iff j <= n-2
        if j <= n - 2:
            pre_edges_sum += -cond_logp[order[j]][order[j+1]]

        # Apply reversal temporarily
        order[i:j+1] = order[i:j+1][::-1]

        post_edges_sum = 0.0
        if i >= 1:
            post_edges_sum += -cond_logp[order[i-1]][order[i]]
        for k in range(i, j):
            post_edges_sum += -cond_logp[order[k]][order[k+1]]
        if j <= n - 2:
            post_edges_sum += -cond_logp[order[j]][order[j+1]]

        delta_sum = post_edges_sum - pre_edges_sum
        # Convert to delta-H (per-step H)
        delta_H = delta_sum / n_minus_1
        proposals += 1

        accept = False
        if delta_H <= 0:
            accept = True
        else:
            if rng.random() < math.exp(-delta_H / T):
                accept = True
                accepts_uphill += 1

        if accept:
            cur_sum += delta_sum
            accepts += 1
            if cur_sum < best_sum:
                best_sum = cur_sum
                best_order = list(order)
        else:
            # revert
            order[i:j+1] = order[i:j+1][::-1]

        T *= beta

        if step % history_stride == 0 or step == SA_STEPS - 1:
            history.append((step, T, cur_sum / n_minus_1, best_sum / n_minus_1))

    print(f"  [{label}] done. best_H = {best_sum/n_minus_1:.4f} bits, "
          f"accepts = {accepts}/{proposals} ({100*accepts/proposals:.1f}%), "
          f"uphill accepts = {accepts_uphill}",
          file=sys.stderr)
    return best_order, best_sum / n_minus_1, history, accepts, accepts_uphill, proposals

# ---------------------------------------------------------------------------
# 6. Run 3 SA trajectories
# ---------------------------------------------------------------------------
runs = []
starts = [
    ("mushaf",   mushaf_order,        SEED + 0),
    ("noldeke",  noldeke_order_list,  SEED + 1),
    ("random",   random_start_order,  SEED + 2),
]
for label, start, run_seed in starts:
    print(f"\nSA run: start={label}, seed={run_seed}", file=sys.stderr)
    print(f"  H_start = {cond_entropy(start):.4f} bits", file=sys.stderr)
    best_order, best_H, history, accepts, uphill, proposals = sa_run(start, run_seed, label)
    runs.append({
        'start_label': label,
        'run_seed': run_seed,
        'H_start': cond_entropy(start),
        'best_H': best_H,
        'best_order': best_order,
        'history': history,
        'accepts': accepts,
        'uphill_accepts': uphill,
        'proposals': proposals,
        'beat_mushaf': best_H < H_mushaf,
    })

H_min_SA = min(r['best_H'] for r in runs)
H_max_SA = max(r['best_H'] for r in runs)
H_spread = H_max_SA - H_min_SA
all_beat_mushaf = all(r['beat_mushaf'] for r in runs)

# p_emp: (# runs with best_H >= H_mushaf + 1) / (n_runs + 1)  -- placeholder
# Proper gating: did all 3 runs produce H < H_mushaf?
n_beat = sum(1 for r in runs if r['beat_mushaf'])

# Gap fraction: how much of the way from SA-min to null-mean is the mushaf?
H_null_mean_ref = 82.92  # from h-new-171
gap_fraction = (H_mushaf - H_min_SA) / (H_null_mean_ref - H_min_SA)
if gap_fraction < 0.10:
    gap_category = 'near-optimum'
elif gap_fraction < 0.50:
    gap_category = 'structured-not-optimal'
else:
    gap_category = 'modestly-structured'

print(f"\nH_min_SA across 3 runs = {H_min_SA:.4f} bits", file=sys.stderr)
print(f"H_max_SA across 3 runs = {H_max_SA:.4f} bits", file=sys.stderr)
print(f"spread = {H_spread:.4f} bits (< 0.5 ⇒ plausibly-global plateau)", file=sys.stderr)
print(f"mushaf H = {H_mushaf:.4f};  gap_fraction = {gap_fraction:.4f} [{gap_category}]",
      file=sys.stderr)
print(f"{n_beat}/3 runs beat H_mushaf", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. Write results JSON
# ---------------------------------------------------------------------------
def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o

summary = {
    'finding_id': 'h-new-228',
    'title': 'SA for MINIMUM conditional-entropy surah ordering',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'rules_tuple': '(no-tashkeel, QAC-STEM roots, top-K=100, Dirichlet α=0.5, L1-norm, Fisher-Rao, rank-exp kernel)',
    'locked_params': {
        'K_top_roots': K_TOP,
        'dirichlet_alpha': DIRICHLET_ALPHA,
        'sa_steps': SA_STEPS,
        'T_0': T_0,
        'T_final': T_FINAL,
        'segment_length_range': [SEG_MIN, SEG_MAX],
        'proposal': '2-opt segment reversal',
        'acceptance': 'Metropolis',
    },
    'reference_values': {
        'H_mushaf': H_mushaf,
        'H_noldeke': H_noldeke,
        'H_null_mean_h171': H_null_mean_ref,
        'H_null_mean_quick1000': H_null_mean_quick,
        'H_null_sd_quick1000': H_null_sd_quick,
        'H_random_start': H_random_start,
    },
    'sa_runs': [
        {
            'start_label': r['start_label'],
            'run_seed': r['run_seed'],
            'H_start': r['H_start'],
            'best_H': r['best_H'],
            'accepts': r['accepts'],
            'uphill_accepts': r['uphill_accepts'],
            'proposals': r['proposals'],
            'beat_mushaf': r['beat_mushaf'],
            'best_order': r['best_order'],
            'history_stride': r['history'][1][0] if len(r['history']) > 1 else 0,
            'history': [
                {'step': h[0], 'T': h[1], 'cur_H': h[2], 'best_H': h[3]}
                for h in r['history']
            ],
        }
        for r in runs
    ],
    'summary_stats': {
        'H_min_SA': H_min_SA,
        'H_max_SA': H_max_SA,
        'H_spread_SA': H_spread,
        'n_runs_beat_mushaf': n_beat,
        'all_runs_beat_mushaf': all_beat_mushaf,
        'gap_fraction': gap_fraction,
        'gap_category': gap_category,
    },
    'verdict': (
        'PASS' if all_beat_mushaf else 'NULL'
    ),
    'verdict_note': (
        f'{n_beat}/3 SA runs found orderings with H < H_mushaf = {H_mushaf:.4f} bits. '
        f'SA lower bound on min H = {H_min_SA:.4f} bits. '
        f'gap_fraction (mushaf ↔ SA-min vs null-mean) = {gap_fraction:.4f} '
        f'({gap_category}).'
    ),
}

summary = round_floats(summary)
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote {OUT_JSON}", file=sys.stderr)

print("\n" + "=" * 70, file=sys.stderr)
print(f"H_mushaf        = {H_mushaf:.4f} bits", file=sys.stderr)
print(f"H_noldeke       = {H_noldeke:.4f} bits", file=sys.stderr)
for r in runs:
    print(f"SA start={r['start_label']:<8s} best_H = {r['best_H']:.4f} bits "
          f"({'< H_mushaf' if r['beat_mushaf'] else '≥ H_mushaf'})", file=sys.stderr)
print(f"H_min_SA        = {H_min_SA:.4f} bits  (upper bound on true min)", file=sys.stderr)
print(f"gap_fraction    = {gap_fraction:.4f}   [{gap_category}]", file=sys.stderr)
print(f"VERDICT         = {summary['verdict']}", file=sys.stderr)
print("=" * 70, file=sys.stderr)
