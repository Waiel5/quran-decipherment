#!/usr/bin/env python3
"""H-NEW-127 — Fisher-Rao fractal extension at verse level (within 5 surahs).

Parent: H-NEW-111 (surah-level Fisher-Rao optimality; PASS-DIRECTED).

Per-surah primary test (Bonferroni-5, α_bon = 0.01):
  L_canon(s) < L_random(s) via 10,000-permutation one-sided lower-tail null,
  for each of the 5 locked surahs: Q 2, Q 7, Q 12, Q 36, Q 55.

Secondary A: L_canon / L_2opt per surah (descriptive).

MW-5 positive control: for Q 55 al-Raḥmān, length-sorted verse order MUST
produce L_length > L_canon. If not, null is broken.

Locked parameters (see pre-reg):
  K_top_roots = 300 (vs H-NEW-111's 500; see pre-reg "garden of forking paths")
  dirichlet_alpha = 0.5 (Jeffreys)
  distance = Fisher-Rao angular = 2·arccos(Σ sqrt(p_i·p_j))
  seed = 20260417 (same as H-NEW-111)
  PERMS = 10,000

Pre-reg SHA-256 emitted to stderr.
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
SEED = 20260417
PERMS = 10000

# Locked parameters
K_TOP = 300
DIRICHLET_ALPHA = 0.5
ALPHA_BON = 0.01
BON_K = 5
LOCKED_SURAHS = [2, 7, 12, 36, 55]
MW5_SURAH = 55  # Q 55 length-sorted control

# Paths
QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-127-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-127.json'

# Pre-reg tamper-evidence
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"K_TOP = {K_TOP}", file=sys.stderr)
print(f"DIRICHLET_ALPHA = {DIRICHLET_ALPHA}", file=sys.stderr)
print(f"ALPHA_BON = {ALPHA_BON} (Bonferroni-{BON_K})", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)
print(f"LOCKED_SURAHS = {LOCKED_SURAHS}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Parse QAC: per-(surah, verse) STEM root tokens
# ---------------------------------------------------------------------------
# QAC location format: (sid:vid:wid:segid)
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_verse_roots = defaultdict(list)  # (sid, vid) -> list of root strings
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
        vid = int(m.group(2))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        root = rm.group(1)
        per_verse_roots[(sid, vid)].append(root)
        global_root_counts[root] += 1

total_tokens = sum(len(v) for v in per_verse_roots.values())
print(f"total STEM root tokens in corpus: {total_tokens}", file=sys.stderr)
print(f"global distinct roots: {len(global_root_counts)}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 2. Select top-K roots GLOBALLY (locked K=300)
# ---------------------------------------------------------------------------
top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {r: i for i, r in enumerate(top_roots)}
topk_cov = sum(global_root_counts[r] for r in top_roots) / total_tokens
print(f"top-K={K_TOP} roots selected", file=sys.stderr)
print(f"  top-5: {top_roots[:5]}", file=sys.stderr)
print(f"  cumulative global coverage: {topk_cov:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 3. Build per-verse distributions for each locked surah
# ---------------------------------------------------------------------------
quran_raw = json.loads(QURAN_JSON.read_text())
verse_counts_per_surah = {}   # sid -> list of verses (each a length-K list)
verse_tokencounts_per_surah = {}  # sid -> list of raw verse token counts (for MW-5)
verse_textlengths_per_surah = {}  # sid -> list of raw char lengths (for MW-5 alt)

for sdata in quran_raw:
    sid = sdata['id']
    if sid not in LOCKED_SURAHS:
        continue
    verses = sdata['verses']
    n_v = len(verses)
    counts_rows = []
    tokct_rows = []
    charlen_rows = []
    for v in verses:
        vid = v['id']
        roots = per_verse_roots.get((sid, vid), [])
        row = [0.0] * K_TOP
        for r in roots:
            idx = top_root_index.get(r)
            if idx is not None:
                row[idx] += 1.0
        counts_rows.append(row)
        tokct_rows.append(len(roots))
        charlen_rows.append(len(v['text']))
    verse_counts_per_surah[sid] = counts_rows
    verse_tokencounts_per_surah[sid] = tokct_rows
    verse_textlengths_per_surah[sid] = charlen_rows
    print(f"  surah {sid}: n_verses={n_v}, mean root tokens/verse = {sum(tokct_rows)/n_v:.2f}",
          file=sys.stderr)

# ---------------------------------------------------------------------------
# 4. Dirichlet smooth + L1 normalize -> prob vectors, then sqrt for Fisher-Rao
# ---------------------------------------------------------------------------
verse_probs_per_surah = {}
verse_sqrtprobs_per_surah = {}
for sid in LOCKED_SURAHS:
    counts_rows = verse_counts_per_surah[sid]
    probs = []
    sqprobs = []
    for row in counts_rows:
        smoothed = [c + DIRICHLET_ALPHA for c in row]
        s = sum(smoothed)
        p = [v / s for v in smoothed]
        probs.append(p)
        sqprobs.append([math.sqrt(x) for x in p])
    verse_probs_per_surah[sid] = probs
    verse_sqrtprobs_per_surah[sid] = sqprobs

# ---------------------------------------------------------------------------
# 5. Fisher-Rao distance builder (per-surah within-verse)
# ---------------------------------------------------------------------------
def build_distance_matrix(sqprobs):
    n = len(sqprobs)
    D = [[0.0] * n for _ in range(n)]
    for i in range(n):
        si = sqprobs[i]
        for j in range(i + 1, n):
            sj = sqprobs[j]
            bc = 0.0
            for k in range(K_TOP):
                bc += si[k] * sj[k]
            if bc > 1.0:
                bc = 1.0
            elif bc < -1.0:
                bc = -1.0
            d = 2.0 * math.acos(bc)
            D[i][j] = d
            D[j][i] = d
    return D

def path_length(D, order):
    L = 0.0
    for i in range(len(order) - 1):
        L += D[order[i]][order[i + 1]]
    return L

def greedy_nn(D, start):
    n = len(D)
    unvisited = set(range(n))
    unvisited.remove(start)
    path = [start]
    cur = start
    while unvisited:
        nxt = min(unvisited, key=lambda v: D[cur][v])
        path.append(nxt)
        unvisited.remove(nxt)
        cur = nxt
    return path

def two_opt(D, path, max_passes=50):
    path = path[:]
    n = len(path)
    improved = True
    passes = 0
    while improved and passes < max_passes:
        improved = False
        passes += 1
        best_delta = 0.0
        best_ij = None
        for i in range(0, n - 2):
            a = path[i]
            b = path[i + 1]
            for j in range(i + 2, n):
                c = path[j]
                d = path[j + 1] if j + 1 < n else None
                if d is None:
                    delta = D[a][c] - D[a][b]
                else:
                    delta = (D[a][c] + D[b][d]) - (D[a][b] + D[c][d])
                if delta < best_delta - 1e-12:
                    best_delta = delta
                    best_ij = (i, j)
        if best_ij is not None:
            i, j = best_ij
            path[i + 1:j + 1] = list(reversed(path[i + 1:j + 1]))
            improved = True
    return path, passes

def q(sorted_list, frac):
    n = len(sorted_list)
    idx = max(0, min(n - 1, int(math.floor(frac * n))))
    return sorted_list[idx]

# ---------------------------------------------------------------------------
# 6. Run per-surah: build D, compute L_canon, run null, 2-opt
# ---------------------------------------------------------------------------
per_surah_results = {}

for sid in LOCKED_SURAHS:
    print(f"\n=== Surah {sid} ===", file=sys.stderr)
    sqprobs = verse_sqrtprobs_per_surah[sid]
    n = len(sqprobs)
    print(f"  n_verses = {n}", file=sys.stderr)

    # Build distance matrix
    D = build_distance_matrix(sqprobs)
    all_d = [D[i][j] for i in range(n) for j in range(i + 1, n)]
    dmean = statistics.mean(all_d)
    dmin = min(all_d)
    dmax = max(all_d)
    print(f"  D stats: min={dmin:.4f}, max={dmax:.4f}, mean={dmean:.4f}", file=sys.stderr)

    # Canonical (mushaf) verse order = 0, 1, 2, ..., n-1
    canon_order = list(range(n))
    L_canon = path_length(D, canon_order)
    print(f"  L_canon = {L_canon:.4f}", file=sys.stderr)

    # Null: 10,000 random permutations (surah-local RNG, seeded deterministically)
    # To ensure reproducibility across surahs, use independent RNG per surah
    # derived from master seed + sid
    rng = random.Random(SEED + sid * 1000003)
    null_L = []
    for p_i in range(PERMS):
        perm = canon_order[:]
        rng.shuffle(perm)
        null_L.append(path_length(D, perm))
    null_L_sorted = sorted(null_L)
    n_le = sum(1 for L in null_L if L <= L_canon)
    p_val = (n_le + 1) / (PERMS + 1)
    null_mean = statistics.mean(null_L)
    null_sd = statistics.stdev(null_L)
    z = (L_canon - null_mean) / null_sd if null_sd > 0 else 0.0
    print(f"  null: mean={null_mean:.4f}, sd={null_sd:.4f}", file=sys.stderr)
    print(f"  null: min={min(null_L):.4f}, q05={q(null_L_sorted, 0.05):.4f}", file=sys.stderr)
    print(f"  z(L_canon) = {z:.4f}", file=sys.stderr)
    print(f"  #{{L_perm ≤ L_canon}} = {n_le}", file=sys.stderr)
    print(f"  p_value (one-sided lower) = {p_val:.6f}  (α_bon = {ALPHA_BON})", file=sys.stderr)
    surah_pass = p_val < ALPHA_BON
    print(f"  PASS: {surah_pass}", file=sys.stderr)

    # 2-opt approximation of TSP (greedy-NN from each start + 2-opt on best)
    # For larger surahs (Q2: 286 verses), this can be slow: 114 greedy starts
    # and then 2-opt on each would be O(n^2) per pass; we do greedy-NN from
    # every start to find the best greedy, then 2-opt that one (H-NEW-111 style).
    greedy_paths = []
    for st in range(n):
        gp = greedy_nn(D, st)
        greedy_paths.append((path_length(D, gp), st, gp))
    greedy_paths.sort(key=lambda x: x[0])
    L_greedy_best = greedy_paths[0][0]
    best_start = greedy_paths[0][1]
    best_gpath = greedy_paths[0][2][:]
    opt_path, npass = two_opt(D, best_gpath)
    L_2opt_best = path_length(D, opt_path)
    print(f"  greedy best: start={best_start}, L={L_greedy_best:.4f}", file=sys.stderr)
    print(f"  2-opt: L={L_2opt_best:.4f} ({npass} passes)", file=sys.stderr)

    # For modest-sized surahs, try 2-opt on top-N greedy starts for tighter bound
    # (keep runtime manageable: only try starts within 1.5x of best greedy)
    top_candidates_to_refine = 20 if n <= 120 else 5
    refined_count = 0
    for L_g, st, gp in greedy_paths[:top_candidates_to_refine]:
        p2, _ = two_opt(D, gp)
        Lp = path_length(D, p2)
        if Lp < L_2opt_best:
            L_2opt_best = Lp
            opt_path = p2[:]
            refined_count += 1
    if refined_count:
        print(f"  additional 2-opt refinements improved best: L={L_2opt_best:.4f}", file=sys.stderr)
    ratio = L_canon / L_2opt_best if L_2opt_best > 0 else float('inf')
    print(f"  L_canon / L_2opt = {ratio:.4f}", file=sys.stderr)

    per_surah_results[sid] = {
        'n_verses': n,
        'L_canon': L_canon,
        'null_mean': null_mean,
        'null_sd': null_sd,
        'null_min': min(null_L),
        'null_max': max(null_L),
        'null_quantiles': {
            'q001': q(null_L_sorted, 0.001),
            'q005': q(null_L_sorted, 0.005),
            'q01':  q(null_L_sorted, 0.01),
            'q025': q(null_L_sorted, 0.025),
            'q05':  q(null_L_sorted, 0.05),
            'q25':  q(null_L_sorted, 0.25),
            'q50':  q(null_L_sorted, 0.50),
            'q75':  q(null_L_sorted, 0.75),
            'q95':  q(null_L_sorted, 0.95),
        },
        'z_score': z,
        'n_perms_le_canon': n_le,
        'p_value_one_sided_lower': p_val,
        'alpha_bon': ALPHA_BON,
        'pass': surah_pass,
        'L_greedy_best': L_greedy_best,
        'L_2opt_best': L_2opt_best,
        'ratio_canon_over_2opt': ratio,
        'D_stats': {
            'min': dmin,
            'max': dmax,
            'mean': dmean,
            'n_pairs': len(all_d),
        },
    }

# ---------------------------------------------------------------------------
# 7. MW-5 positive control on Q 55 (length-sorted ascending)
# ---------------------------------------------------------------------------
print("\n=== MW-5 positive control (Q 55 length-sorted) ===", file=sys.stderr)
mw5_sid = MW5_SURAH
sqprobs_55 = verse_sqrtprobs_per_surah[mw5_sid]
n55 = len(sqprobs_55)
D55 = build_distance_matrix(sqprobs_55)
tokcts_55 = verse_tokencounts_per_surah[mw5_sid]
charlens_55 = verse_textlengths_per_surah[mw5_sid]

# Ascending order by root-token count (break ties by canonical position for stability)
len_order_asc = sorted(range(n55), key=lambda i: (tokcts_55[i], i))
L_lensort_asc = path_length(D55, len_order_asc)
# Also compute char-length-sorted as alt sanity
charlen_order_asc = sorted(range(n55), key=lambda i: (charlens_55[i], i))
L_charlensort_asc = path_length(D55, charlen_order_asc)

L_canon_55 = per_surah_results[mw5_sid]['L_canon']
mw5_token_pass = L_lensort_asc > L_canon_55
mw5_char_pass = L_charlensort_asc > L_canon_55
print(f"  L_canon(55) = {L_canon_55:.4f}", file=sys.stderr)
print(f"  L_lengthsort_asc_TOKENS(55) = {L_lensort_asc:.4f}  (MW-5 token pass: {mw5_token_pass})", file=sys.stderr)
print(f"  L_lengthsort_asc_CHARS(55) = {L_charlensort_asc:.4f}  (MW-5 char pass: {mw5_char_pass})", file=sys.stderr)

# MW-5 OVERALL: require token-sorted version (primary operational definition)
# but report both for transparency
mw5_broken = not mw5_token_pass
if mw5_broken:
    print("  !! MW-5 POSITIVE CONTROL FAILED (token-sort did not exceed canonical) !!",
          file=sys.stderr)
else:
    print("  MW-5 positive control PASSES", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. Family verdict
# ---------------------------------------------------------------------------
n_pass = sum(1 for sid in LOCKED_SURAHS if per_surah_results[sid]['pass'])
print(f"\n=== Family verdict ===", file=sys.stderr)
print(f"  n_pass = {n_pass} of {len(LOCKED_SURAHS)}", file=sys.stderr)
if n_pass >= 3:
    family_verdict = 'STRONG-REPLICATION'
elif n_pass == 0:
    family_verdict = 'NULL-STRONG'
else:
    family_verdict = 'NULL-WEAK'
print(f"  family verdict: {family_verdict}", file=sys.stderr)
if mw5_broken:
    family_verdict = 'INSTRUMENT-BROKEN'
    print(f"  OVERRIDDEN by MW-5 failure: INSTRUMENT-BROKEN", file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. Write JSON
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
    'finding_id': 'h-new-127',
    'title': 'Fisher-Rao fractal extension: verse-level path optimality within 5 surahs',
    'parent_finding': 'h-new-111',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'rules_tuple': '(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf verse order, Hafs-Kufan)',
    'locked_params': {
        'K_top_roots': K_TOP,
        'dirichlet_alpha': DIRICHLET_ALPHA,
        'permutations': PERMS,
        'distance': 'Fisher-Rao angular = 2·arccos(Σ sqrt(p_i·p_j))',
        'length_control': 'L1-normalized probability vectors (MW-1)',
        'bonferroni_k': BON_K,
        'alpha_bon': ALPHA_BON,
        'locked_surahs': LOCKED_SURAHS,
    },
    'corpus_stats': {
        'total_stem_root_tokens': total_tokens,
        'global_distinct_roots': len(global_root_counts),
        'top_K_coverage_fraction': topk_cov,
    },
    'per_surah': {str(sid): per_surah_results[sid] for sid in LOCKED_SURAHS},
    'mw5_positive_control': {
        'surah': mw5_sid,
        'method_primary': 'length-sorted ascending by STEM-root token count',
        'L_canon': L_canon_55,
        'L_length_sorted_token': L_lensort_asc,
        'L_length_sorted_char':  L_charlensort_asc,
        'mw5_token_pass': mw5_token_pass,
        'mw5_char_pass': mw5_char_pass,
        'mw5_broken': mw5_broken,
    },
    'family_verdict': {
        'n_pass': n_pass,
        'n_tests': len(LOCKED_SURAHS),
        'alpha_bon': ALPHA_BON,
        'verdict': family_verdict,
        'pass_criterion': 'n_pass >= 3 of 5 at α_bon = 0.01',
    },
}
summary = round_floats(summary)
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote summary JSON: {OUT_JSON}", file=sys.stderr)

# Final summary to stdout
print("\n" + "=" * 70, file=sys.stderr)
print(f"PER-SURAH (α_bon = {ALPHA_BON}):", file=sys.stderr)
for sid in LOCKED_SURAHS:
    r = per_surah_results[sid]
    flag = 'PASS' if r['pass'] else 'FAIL'
    print(f"  Q {sid:3d} (n={r['n_verses']:3d}): "
          f"L_canon={r['L_canon']:.3f}  null_mean={r['null_mean']:.3f}  "
          f"z={r['z_score']:+.2f}  p={r['p_value_one_sided_lower']:.4f}  "
          f"ratio={r['ratio_canon_over_2opt']:.3f}  [{flag}]", file=sys.stderr)
print(f"MW-5 (Q {mw5_sid} length-sort>canonical): "
      f"tokens {'PASS' if mw5_token_pass else 'FAIL'}, "
      f"chars {'PASS' if mw5_char_pass else 'FAIL'}", file=sys.stderr)
print(f"n_pass = {n_pass} of 5   →   {family_verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)
