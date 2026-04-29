#!/usr/bin/env python3
"""H-NEW-146 — Q 50 al-Qāf mid-mushaf hub investigation.

Pre-registered tests (Bonferroni k=3, α_bon=0.0167, family=h-new-146-q50-hub):

  Cell A — position: Q 50's cluster-network degree rank within Q 40-60.
           PASS if rank ≤ 3/21 at p_perm < 0.0167.
  Cell B — content: Q 50's qrA (qurʾān) root density rank across 114.
           PASS if rank ≤ 10/114 at hypergeometric p < 0.0167.
  Cell C — structural: Q 50's FR distance to {Q 38, Q 68} vs other 28
           muq surahs. 2-sided permutation. PASS if p < 0.0167.

MW-5 positive control: Q 44 (degree 3, non-hub) instead of Q 50; expect
all cells fail.

Seed 20260417. Deterministic.
"""
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
SEED = 20260417
N_PERMS = 10000

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
CF010_JSON = ROOT / 'findings/phase-b-hypotheses/csv/cross-finding-010.json'
H111_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-146-q50-qaf-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-146.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

rng = random.Random(SEED)

# ---------------------------------------------------------------------------
# 1. Quran metadata
# ---------------------------------------------------------------------------
quran = json.loads(QURAN_JSON.read_text())
surah_nverses = {s['id']: len(s['verses']) for s in quran}

# ---------------------------------------------------------------------------
# 2. Cluster-network degrees from cross-finding-010
# ---------------------------------------------------------------------------
cf010 = json.loads(CF010_JSON.read_text())
per_surah_degree = {int(k): v for k, v in cf010['product_A_degree_distribution']['per_surah_degree'].items()}

# ---------------------------------------------------------------------------
# 3. QAC root tokens (for Cell B qrA root density)
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')
per_surah_roots = defaultdict(list)
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
        if 'STEM' not in parts[3]:
            continue
        rm = ROOT_RE.search(parts[3])
        if not rm:
            continue
        per_surah_roots[sid].append(rm.group(1))

def root_count(sid, target_roots):
    return sum(1 for r in per_surah_roots.get(sid, []) if r in target_roots)

def root_density(sid, target_roots):
    return root_count(sid, target_roots) / surah_nverses[sid]

# ---------------------------------------------------------------------------
# 4. H-NEW-111 D-matrix (upper-triangular)
# ---------------------------------------------------------------------------
h111 = json.loads(H111_JSON.read_text())
D_upper = h111['D_matrix_upper_triangular']
D = [[0.0] * 115 for _ in range(115)]
for entry in D_upper:
    i, j, d = int(entry[0]), int(entry[1]), float(entry[2])
    D[i][j] = d
    D[j][i] = d

# Canonical 29 muq surahs
MUQ_SURAHS = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
              31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]
SINGLE_LETTER_MUQ = [38, 50, 68]  # ص, ق, ن

# ---------------------------------------------------------------------------
# 5. Cells A/B/C (parametrized to support MW-5 control)
# ---------------------------------------------------------------------------
def run_cells_for_target(target_sid):
    """Run all three cells for target_sid (Q 50 or MW-5 Q 44)."""
    out = {}

    # --- Cell A: degree rank within Q 40-60
    q40_60 = list(range(40, 61))
    degs = [(s, per_surah_degree.get(s, 0)) for s in q40_60]
    degs_sorted = sorted(degs, key=lambda x: -x[1])
    rank_A = next(i + 1 for i, (s, d) in enumerate(degs_sorted) if s == target_sid)
    # Permutation null: shuffle degrees across Q 40-60, compute rank distribution
    null_ranks = []
    raw_degs = [d for _, d in degs]
    for _ in range(N_PERMS):
        shuffled = raw_degs[:]
        rng.shuffle(shuffled)
        # After shuffling, where does target land? Target is index of target in q40_60.
        target_idx = q40_60.index(target_sid)
        target_d = shuffled[target_idx]
        # Rank under this shuffle: sort desc, find position
        sorted_d = sorted(shuffled, reverse=True)
        rank = sorted_d.index(target_d) + 1  # tie → first occurrence rank
        null_ranks.append(rank)
    p_A = sum(1 for r in null_ranks if r <= rank_A) / N_PERMS  # 1-sided lower-tail (smaller rank = better)
    out['cell_A'] = {
        'target_sid': target_sid,
        'degree': per_surah_degree.get(target_sid, 0),
        'q40_60_degrees': dict(degs),
        'rank_within_q40_60': rank_A,
        'threshold_rank': 3,
        'p_perm_one_sided': p_A,
        'alpha_bon': 0.0167,
        'pass': rank_A <= 3 and p_A < 0.0167,
    }

    # --- Cell B: qrA root density rank across 114
    qrA_densities = {s: root_density(s, ['qrA']) for s in range(1, 115)}
    sorted_qrA = sorted(qrA_densities.items(), key=lambda x: -x[1])
    rank_B = next(i + 1 for i, (s, d) in enumerate(sorted_qrA) if s == target_sid)
    # Null: hypergeometric-style — probability that a random surah is in top-10
    # Exact: P(rank ≤ 10) = 10/114
    p_B_exact = 10 / 114  # under uniform null
    out['cell_B'] = {
        'target_sid': target_sid,
        'qrA_density': qrA_densities[target_sid],
        'qrA_count': root_count(target_sid, ['qrA']),
        'rank_among_114': rank_B,
        'threshold_rank': 10,
        'p_uniform': p_B_exact,
        'top10_surahs_by_qrA_density': sorted_qrA[:10],
        'alpha_bon': 0.0167,
        'pass': rank_B <= 10,  # p under uniform null = 0.088 > 0.0167;
        # REQUIRE stronger: rank ≤ 2 (p=2/114=0.0175 still slightly above α_bon)
        # Tighter: rank = 1 (p=1/114=0.0088 < 0.0167 ✓)
        # Update rule pre-run: PASS at rank ≤ 1 (single-test tight);
        # keep rank ≤ 10 as descriptive; declare p vs uniform.
    }
    # Tighten decision: rank-1 is the only rank that survives α_bon=0.0167 under uniform null.
    out['cell_B']['pass_strict_rank_1'] = rank_B == 1
    out['cell_B']['pass_declared'] = rank_B <= 10 and (rank_B / 114.0) < 0.0167
    # Per pre-reg: "rank ≤ 10 at p < 0.0167" — p_uniform for rank≤10 = 10/114 = 0.088 > 0.0167.
    # So strictly PASS requires rank such that rank/114 < 0.0167 → rank ≤ 1.
    # Call this out explicitly:
    out['cell_B']['pass'] = (rank_B / 114.0) < 0.0167

    # --- Cell C: FR distance to {Q 38, Q 68} vs other 28 muq surahs
    other_muq = [s for s in MUQ_SURAHS if s != target_sid]
    single_letter_others = [s for s in SINGLE_LETTER_MUQ if s != target_sid]
    non_single_letter_muq = [s for s in other_muq if s not in single_letter_others]

    dist_to_singles = [D[target_sid][s] for s in single_letter_others]
    dist_to_non_singles = [D[target_sid][s] for s in non_single_letter_muq]

    mean_dist_singles = statistics.mean(dist_to_singles)
    mean_dist_non_singles = statistics.mean(dist_to_non_singles)
    diff_observed = mean_dist_singles - mean_dist_non_singles

    # Permutation null: shuffle muq surah labels, randomly pick 2 as "singles", recompute diff
    null_diffs = []
    for _ in range(N_PERMS):
        shuffled_muq = other_muq[:]
        rng.shuffle(shuffled_muq)
        null_singles = shuffled_muq[:len(single_letter_others)]
        null_non_singles = shuffled_muq[len(single_letter_others):]
        d_s = statistics.mean(D[target_sid][s] for s in null_singles)
        d_ns = statistics.mean(D[target_sid][s] for s in null_non_singles)
        null_diffs.append(d_s - d_ns)

    # 2-sided p
    abs_obs = abs(diff_observed)
    p_C_two_sided = sum(1 for d in null_diffs if abs(d) >= abs_obs) / N_PERMS
    out['cell_C'] = {
        'target_sid': target_sid,
        'single_letter_muq_others': single_letter_others,
        'dist_to_singles': dict(zip(single_letter_others, dist_to_singles)),
        'mean_dist_to_singles': mean_dist_singles,
        'mean_dist_to_other_muq': mean_dist_non_singles,
        'diff_observed': diff_observed,
        'null_diff_mean': statistics.mean(null_diffs),
        'null_diff_sd': statistics.stdev(null_diffs),
        'p_perm_two_sided': p_C_two_sided,
        'alpha_bon': 0.0167,
        'pass': p_C_two_sided < 0.0167,
    }

    return out

# ---------------------------------------------------------------------------
# 6. Main target = Q 50
# ---------------------------------------------------------------------------
print("\n[Q 50 — main target] Running all 3 cells...", file=sys.stderr)
q50_results = run_cells_for_target(50)
for cell_name in ['cell_A', 'cell_B', 'cell_C']:
    c = q50_results[cell_name]
    print(f"\n{cell_name}: {c}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. MW-5 positive control = Q 44 (degree 3, non-hub)
# ---------------------------------------------------------------------------
print("\n[MW-5 control — Q 44 (non-hub)] Running all 3 cells...", file=sys.stderr)
q44_results = run_cells_for_target(44)
for cell_name in ['cell_A', 'cell_B', 'cell_C']:
    c = q44_results[cell_name]
    print(f"\n{cell_name} (Q 44): pass={c.get('pass', False)}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. Final verdict
# ---------------------------------------------------------------------------
q50_pass_count = sum(1 for cn in ['cell_A', 'cell_B', 'cell_C'] if q50_results[cn].get('pass', False))
q44_pass_count = sum(1 for cn in ['cell_A', 'cell_B', 'cell_C'] if q44_results[cn].get('pass', False))
mw5_pass = q44_pass_count == 0

if not mw5_pass:
    final = "INSTRUMENT-BROKEN — Q 44 non-hub control spuriously passes some cell"
elif q50_pass_count == 3:
    final = "FULL-HUB-EXPLANATION — position + content + structural together explain Q 50's hub"
elif q50_pass_count == 2:
    final = "PARTIAL-EXPLANATION — two factors contribute; one dimension null"
elif q50_pass_count == 1:
    final = "WEAK-HUB — single factor dominates"
else:
    final = "UNEXPLAINED — none of the three tested factors survive at α_bon"

print("\n" + "=" * 70, file=sys.stderr)
print(f"Q 50 cells passed: {q50_pass_count}/3", file=sys.stderr)
print(f"Q 44 (MW-5) cells passed: {q44_pass_count}/3 ({'OK' if mw5_pass else 'NOT OK'})", file=sys.stderr)
print(f"FINAL: {final}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. Write JSON
# ---------------------------------------------------------------------------
summary = {
    'finding_id': 'h-new-146',
    'title': 'Q 50 al-Qāf mid-mushaf hub investigation',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'bonferroni': {'k': 3, 'alpha_bon': 0.0167, 'family': 'h-new-146-q50-hub'},
    'q50_main': q50_results,
    'q44_mw5_control': q44_results,
    'mw5_pass': mw5_pass,
    'q50_cells_passed_of_3': q50_pass_count,
    'final_verdict': final,
}
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
