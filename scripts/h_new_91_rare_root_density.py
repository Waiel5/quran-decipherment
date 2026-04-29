#!/usr/bin/env python3
"""H-NEW-91 — Rare-root concentration per surah.

Pre-registered tests (Bonferroni k=5, α_bon=0.01):
  T1 — heterogeneity vs uniform-vocabulary null (Σ z² permutation)
  T2 — length confound (Spearman ρ vs log N_s; partial vs genre)
  T3 — Q 26 al-Shuʿarāʾ rank claim (one-sided pre-committed: bottom-15)
  T4 — H-NEW-23 hapax-final cross-reference (Spearman ρ)
  T5 — genre clustering (permutation ANOVA)

Seed 20260415.
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
SEED = 20260415
PERMS = 10000
random.seed(SEED)

# ---- Paths ----
QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
ROOT_STATS_CSV = ROOT / 'data/morphology/root-stats.csv'
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
HAPAX_CSV = ROOT / 'findings/phase-b-hypotheses/hapaxes-full-list.csv'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-91-rare-root-density-prereg.md'
OUT_PER_SURAH = ROOT / 'findings/phase-b-hypotheses/csv/h-new-91-per-surah.csv'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-91.json'

# ---- Pre-reg hash (tamper-evidence) ----
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

# ---- Load global root counts (truth) ----
root_global_count = {}
with open(ROOT_STATS_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        root_global_count[row['root']] = int(row['total_occurrences'])
print(f"global roots: {len(root_global_count)}", file=sys.stderr)

# ---- Parse QAC: per-token (sid, vid, wid, root) for STEM segments ----
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_surah_tokens = defaultdict(list)  # sid -> list of root strings
verse_tokens = defaultdict(list)  # (sid, vid) -> list of (wid, root)

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
        sid, vid, wid, seg = (int(m.group(i)) for i in range(1, 5))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        root = rm.group(1)
        per_surah_tokens[sid].append(root)
        verse_tokens[(sid, vid)].append((wid, root))

print(f"tokens with root (STEM): {sum(len(v) for v in per_surah_tokens.values())}", file=sys.stderr)
print(f"surahs with at least 1 root token: {len(per_surah_tokens)}", file=sys.stderr)

# Sanity: rebuild global root counts from QAC tokens to double-check consistency
qac_global = Counter()
for sid in per_surah_tokens:
    qac_global.update(per_surah_tokens[sid])
print(f"QAC-rebuilt global root types: {len(qac_global)}", file=sys.stderr)

# Cross-check: report disagreements (should be tiny / zero)
mismatches = 0
for r, c in qac_global.items():
    rs_c = root_global_count.get(r, 0)
    if rs_c != c:
        mismatches += 1
print(f"root-stats vs QAC-STEM-rebuilt mismatches: {mismatches}", file=sys.stderr)
# Use QAC-rebuilt counts for internal consistency (so per-surah numerators
# and global denominators are computed under the SAME rule):
ROOT_F = dict(qac_global)
TOTAL_TOKENS = sum(ROOT_F.values())
print(f"total root-bearing STEM tokens: {TOTAL_TOKENS}", file=sys.stderr)

# Distribution of f for global sampling null
roots_sorted = sorted(ROOT_F.items(), key=lambda kv: -kv[1])
sample_pool = []  # list with each root repeated f times
for r, c in roots_sorted:
    sample_pool.extend([r] * c)
print(f"sample pool size: {len(sample_pool)}", file=sys.stderr)

# ---- Load surah names + Meccan/Medinan ----
import json as _json
quran = _json.loads(QURAN_JSON.read_text())
surah_meta = {}
for s in quran:
    surah_meta[s['id']] = {
        'name_tl': s.get('transliteration', ''),
        'name_ar': s.get('name', ''),
        'type': s.get('type', '').lower(),
        'n_verses': len(s.get('verses', [])),
    }

# ---- Genre coding (LOCKED, copied from H-NEW-23) ----
def genre_for(sid: int) -> str:
    if sid in {1, 87, 94, 112, 113, 114}:
        return 'hymn'
    if 78 <= sid <= 114:
        return 'eschatological'
    if sid in {2, 3, 4, 5, 24, 33, 58, 60, 65, 66}:
        return 'legal'
    if sid in {8, 9, 47, 48, 49, 59}:
        return 'polemic'
    if sid in {12, 18, 19, 20, 28}:
        return 'narrative'
    # default
    if surah_meta[sid]['type'] == 'meccan':
        return 'narrative'
    return 'narrative'  # remaining Medinan default

# ---- Per-surah metrics ----
def metrics_for_surah(roots_list, root_f, common_thresh=100, rare_thresh=5):
    n = len(roots_list)
    if n == 0:
        return None
    fs = [root_f.get(r, 0) for r in roots_list]
    # Replace 0 with 1 to avoid log(0); shouldn't happen given QAC filter
    safe_fs = [f if f > 0 else 1 for f in fs]
    mean_f = sum(fs) / n
    geom_mean_f = math.exp(sum(math.log(f) for f in safe_fs) / n)
    median_f = statistics.median(fs)
    rare5 = sum(1 for f in fs if f <= rare_thresh) / n
    hapax = sum(1 for f in fs if f == 1) / n
    common100 = sum(1 for f in fs if f >= common_thresh) / n
    return {
        'n_root_tokens': n,
        'n_distinct_roots': len(set(roots_list)),
        'mean_freq': mean_f,
        'geom_mean_freq': geom_mean_f,
        'median_freq': median_f,
        'rare_density_5': rare5,
        'hapax_density': hapax,
        'common_only_density': common100,
    }

per_surah = {}
for sid in sorted(per_surah_tokens):
    m = metrics_for_surah(per_surah_tokens[sid], ROOT_F)
    m['sid'] = sid
    m['name_tl'] = surah_meta[sid]['name_tl']
    m['type'] = surah_meta[sid]['type']
    m['genre'] = genre_for(sid)
    per_surah[sid] = m

# Sanity print
print(f"surahs ranked: {len(per_surah)}", file=sys.stderr)

# ---- Spearman ----
def rankdata(xs):
    """Average ranks for ties (1-based)."""
    n = len(xs)
    indexed = sorted(range(n), key=lambda i: xs[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and xs[indexed[j+1]] == xs[indexed[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            ranks[indexed[k]] = avg
        i = j + 1
    return ranks

def spearman_rho(xs, ys):
    rx = rankdata(xs)
    ry = rankdata(ys)
    return pearson_r(rx, ry)

def pearson_r(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    sx = math.sqrt(sum((xs[i] - mx) ** 2 for i in range(n)))
    sy = math.sqrt(sum((ys[i] - my) ** 2 for i in range(n)))
    if sx == 0 or sy == 0:
        return 0.0
    return cov / (sx * sy)

# ---- TEST 1: Heterogeneity vs uniform null ----
# For each surah, compute observed geom_mean_freq.
# Build empirical null: per-surah, draw N_s tokens with replacement from sample_pool;
# repeat 10,000 times across all surahs jointly (one global permutation: shuffle
# the sequence of root labels across all token positions and re-aggregate by surah).
print("\n[T1] Heterogeneity test...", file=sys.stderr)
sids = sorted(per_surah.keys())
obs_gm = {sid: per_surah[sid]['geom_mean_freq'] for sid in sids}

# Quick: for each surah, MC null mean+sd of geom_mean_freq under random draws of N_s
mc_iters = 1000  # per-surah; 1000 × 114 = 114k draws; cheap
random.seed(SEED)
log_pool = [math.log(ROOT_F[r]) for r in sample_pool]  # precompute logs
# To draw uniformly from the global token distribution (proportional to f), draw
# from sample_pool (each root listed f times). Cheap: random.choices.
per_surah_null = {}
for sid in sids:
    n = per_surah[sid]['n_root_tokens']
    gms = []
    for _ in range(mc_iters):
        sample = random.choices(log_pool, k=n)
        gms.append(math.exp(sum(sample) / n))
    mean_null = statistics.mean(gms)
    sd_null = statistics.stdev(gms) if len(gms) > 1 else 0.0
    z = (obs_gm[sid] - mean_null) / sd_null if sd_null > 0 else 0.0
    per_surah_null[sid] = {
        'mc_mean': mean_null,
        'mc_sd': sd_null,
        'z': z,
    }
    per_surah[sid]['null_z'] = z

# Aggregate Σ z²
sum_z2_obs = sum(per_surah_null[sid]['z'] ** 2 for sid in sids)
print(f"  Σz² observed: {sum_z2_obs:.2f}", file=sys.stderr)

# Permutation: 10,000 global shuffles, each draws fresh per-surah tokens
# from a global root-shuffle (preserves per-surah N_s, breaks per-surah composition)
# Build the full token list in mushaf order
all_tokens = []
surah_index_for_token = []
for sid in sids:
    for r in per_surah_tokens[sid]:
        all_tokens.append(r)
        surah_index_for_token.append(sid)

null_sumz2 = []
random.seed(SEED + 1)
print(f"  permutations: {PERMS}", file=sys.stderr)
for p in range(PERMS):
    perm = all_tokens[:]
    random.shuffle(perm)
    # Compute per-surah geom_mean_freq under this perm
    per_surah_perm = defaultdict(list)
    for i, r in enumerate(perm):
        per_surah_perm[surah_index_for_token[i]].append(r)
    sz2 = 0.0
    for sid in sids:
        roots_p = per_surah_perm[sid]
        n = len(roots_p)
        if n == 0:
            continue
        gm_p = math.exp(sum(math.log(ROOT_F[r]) for r in roots_p) / n)
        z_p = (gm_p - per_surah_null[sid]['mc_mean']) / per_surah_null[sid]['mc_sd'] if per_surah_null[sid]['mc_sd'] > 0 else 0
        sz2 += z_p ** 2
    null_sumz2.append(sz2)
    if (p + 1) % 1000 == 0:
        print(f"    perm {p+1}/{PERMS}", file=sys.stderr)

n_ge = sum(1 for v in null_sumz2 if v >= sum_z2_obs)
p_t1 = (n_ge + 1) / (PERMS + 1)
print(f"  permutation p (Σz² ≥ obs): {p_t1:.4f}", file=sys.stderr)

t1 = {
    'observed_sum_z2': sum_z2_obs,
    'null_mean_sum_z2': statistics.mean(null_sumz2),
    'null_sd_sum_z2': statistics.stdev(null_sumz2),
    'n_perm_ge_obs': n_ge,
    'p_perm': p_t1,
    'pass': p_t1 < 0.01,
}

# ---- TEST 2: Length confound (Spearman) ----
print("\n[T2] Length confound...", file=sys.stderr)
log_n = {sid: math.log(per_surah[sid]['n_root_tokens']) for sid in sids}
gm_list = [per_surah[sid]['geom_mean_freq'] for sid in sids]
ln_list = [log_n[sid] for sid in sids]
rho_len = spearman_rho(gm_list, ln_list)
print(f"  Spearman ρ(geom_mean_freq, log N_s) = {rho_len:.4f}", file=sys.stderr)

# Length-residualized rank: 5 quintile bins, within-bin rank
def quintile_residualize(metric_dict, length_dict):
    """Returns dict sid -> within-bin rank of metric, after binning by length."""
    sorted_by_len = sorted(length_dict.keys(), key=lambda s: length_dict[s])
    nb = 5
    per_bin = len(sorted_by_len) // nb
    bin_for = {}
    for i, sid in enumerate(sorted_by_len):
        b = min(i // per_bin, nb - 1)
        bin_for[sid] = b
    bin_members = defaultdict(list)
    for sid, b in bin_for.items():
        bin_members[b].append(sid)
    resid_rank = {}
    for b, mems in bin_members.items():
        mems_sorted = sorted(mems, key=lambda s: metric_dict[s])
        for r, sid in enumerate(mems_sorted):
            resid_rank[sid] = r + 1
    return resid_rank, bin_for

resid_rank_gm, bin_of = quintile_residualize({s: per_surah[s]['geom_mean_freq'] for s in sids}, log_n)
resid_rank_rare5, _ = quintile_residualize({s: per_surah[s]['rare_density_5'] for s in sids}, log_n)
resid_rank_hapax, _ = quintile_residualize({s: per_surah[s]['hapax_density'] for s in sids}, log_n)

for sid in sids:
    per_surah[sid]['log_n'] = log_n[sid]
    per_surah[sid]['length_quintile'] = bin_of[sid]
    per_surah[sid]['gm_resid_rank_in_quintile'] = resid_rank_gm[sid]
    per_surah[sid]['rare5_resid_rank_in_quintile'] = resid_rank_rare5[sid]
    per_surah[sid]['hapax_resid_rank_in_quintile'] = resid_rank_hapax[sid]

t2 = {
    'spearman_rho_geom_mean_freq_vs_log_N': rho_len,
    'length_confounded': abs(rho_len) > 0.5,
}

# ---- TEST 3: Q 26 al-Shuʿarāʾ ----
print("\n[T3] Q 26 al-Shuʿarāʾ rank claim...", file=sys.stderr)
sids_by_gm = sorted(sids, key=lambda s: per_surah[s]['geom_mean_freq'])  # ascending = lowest mean = most rare
rank_q26 = sids_by_gm.index(26) + 1
n_total = len(sids_by_gm)

# Length-residualized: Q26's resid_rank within its quintile + which quintile
q26_quintile = bin_of[26]
q26_resid_rank = resid_rank_gm[26]
quintile_size = sum(1 for s in sids if bin_of[s] == q26_quintile)

# Verdict on raw rank
if rank_q26 <= 15:
    verdict_q26 = 'PASS (Q26 in bottom-15 by geom_mean_freq)'
elif rank_q26 <= 30:
    verdict_q26 = 'PARTIAL (Q26 in bottom-30)'
elif rank_q26 > n_total / 2:
    verdict_q26 = 'FAIL (Q26 above median)'
else:
    verdict_q26 = 'FAIL (Q26 in middle bin)'

t3 = {
    'q26_geom_mean_freq': per_surah[26]['geom_mean_freq'],
    'q26_n_root_tokens': per_surah[26]['n_root_tokens'],
    'q26_rank_ascending': rank_q26,  # 1 = most rare
    'q26_total_surahs': n_total,
    'q26_length_quintile': q26_quintile,
    'q26_resid_rank_in_quintile': q26_resid_rank,
    'q26_quintile_size': quintile_size,
    'verdict_raw': verdict_q26,
    'pass': rank_q26 <= 15,
}
print(f"  Q26 rank ascending: {rank_q26}/{n_total}; verdict: {verdict_q26}", file=sys.stderr)

# ---- TEST 4: Cross-reference with H-NEW-23 hapax-final ----
print("\n[T4] H-NEW-23 hapax-final cross-reference...", file=sys.stderr)
# Load hapax catalog (verse-final flag per hapax)
per_surah_hapax_total = defaultdict(int)
per_surah_hapax_final = defaultdict(int)
with open(HAPAX_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['type'] != 'root-hapax':
            continue
        sid = int(row['surah'])
        per_surah_hapax_total[sid] += 1
        if int(row['verse_final']) == 1:
            per_surah_hapax_final[sid] += 1

# Per-surah hapax-final-rate (only surahs with ≥ 1 hapax)
hapax_final_rate = {}
for sid in sids:
    h = per_surah_hapax_total[sid]
    hf = per_surah_hapax_final[sid]
    if h > 0:
        hapax_final_rate[sid] = hf / h
    else:
        hapax_final_rate[sid] = None

# Spearman: correlate rare_density_5 rank vs hapax-final-rate (excluding None)
sids_with_hapax = [s for s in sids if hapax_final_rate[s] is not None]
print(f"  surahs with ≥1 hapax: {len(sids_with_hapax)}", file=sys.stderr)
rare5_xs = [per_surah[s]['rare_density_5'] for s in sids_with_hapax]
hf_ys = [hapax_final_rate[s] for s in sids_with_hapax]
rho_t4 = spearman_rho(rare5_xs, hf_ys)
# Permutation p (two-sided)
random.seed(SEED + 2)
n_xc = len(sids_with_hapax)
null_rhos = []
for _ in range(PERMS):
    shuffled = hf_ys[:]
    random.shuffle(shuffled)
    null_rhos.append(spearman_rho(rare5_xs, shuffled))
n_extreme = sum(1 for r in null_rhos if abs(r) >= abs(rho_t4))
p_t4 = (n_extreme + 1) / (PERMS + 1)
print(f"  Spearman ρ(rare_density_5, hapax-final-rate) = {rho_t4:.4f}; p_perm={p_t4:.4f}", file=sys.stderr)
t4 = {
    'spearman_rho_rare5_vs_hapax_final_rate': rho_t4,
    'n_surahs_with_hapax': n_xc,
    'p_perm_two_sided': p_t4,
    'pass': p_t4 < 0.01 and abs(rho_t4) > 0.30,
}

# ---- TEST 5: Genre clustering (permutation ANOVA) ----
print("\n[T5] Genre ANOVA...", file=sys.stderr)
def perm_anova_F(values_by_group):
    """Returns F = between-group var / within-group var (one-way ANOVA F)."""
    all_vals = []
    grand_mean_components = []
    for g, vs in values_by_group.items():
        for v in vs:
            all_vals.append(v)
            grand_mean_components.append(v)
    grand_mean = sum(all_vals) / len(all_vals)
    ss_between = sum(len(vs) * (sum(vs) / len(vs) - grand_mean) ** 2 for vs in values_by_group.values() if len(vs) > 0)
    ss_within = sum(sum((v - sum(vs) / len(vs)) ** 2 for v in vs) for vs in values_by_group.values() if len(vs) > 0)
    df_b = len(values_by_group) - 1
    df_w = len(all_vals) - len(values_by_group)
    if df_b == 0 or df_w == 0 or ss_within == 0:
        return float('inf') if ss_between > 0 else 0.0
    return (ss_between / df_b) / (ss_within / df_w)

# For both metrics: geom_mean_freq and rare_density_5
def run_perm_anova(metric_key):
    obs_grouped = defaultdict(list)
    for sid in sids:
        obs_grouped[per_surah[sid]['genre']].append(per_surah[sid][metric_key])
    F_obs = perm_anova_F(obs_grouped)
    # Permutation: shuffle genre labels
    sid_genres = [per_surah[s]['genre'] for s in sids]
    sid_metric = [per_surah[s][metric_key] for s in sids]
    null_Fs = []
    random.seed(SEED + 3)
    for _ in range(PERMS):
        gen = sid_genres[:]
        random.shuffle(gen)
        grouped = defaultdict(list)
        for i, s in enumerate(sids):
            grouped[gen[i]].append(sid_metric[i])
        null_Fs.append(perm_anova_F(grouped))
    n_extreme = sum(1 for F in null_Fs if F >= F_obs)
    p = (n_extreme + 1) / (PERMS + 1)
    means_per_genre = {g: statistics.mean(vs) for g, vs in obs_grouped.items()}
    n_per_genre = {g: len(vs) for g, vs in obs_grouped.items()}
    return {
        'F_obs': F_obs,
        'p_perm': p,
        'means_per_genre': means_per_genre,
        'n_per_genre': n_per_genre,
        'pass': p < 0.01,
    }

t5_gm = run_perm_anova('geom_mean_freq')
t5_rare5 = run_perm_anova('rare_density_5')
print(f"  geom_mean_freq: F={t5_gm['F_obs']:.2f} p={t5_gm['p_perm']:.4f}", file=sys.stderr)
print(f"  rare_density_5: F={t5_rare5['F_obs']:.2f} p={t5_rare5['p_perm']:.4f}", file=sys.stderr)
t5 = {
    'geom_mean_freq': t5_gm,
    'rare_density_5': t5_rare5,
    'pass': t5_gm['pass'] or t5_rare5['pass'],
}

# ---- Bonferroni composite ----
n_pass = sum([t1['pass'], False, t3['pass'], t4['pass'], t5['pass']])
# Note: T2 is descriptive/diagnostic; not a pass/fail at α level
if n_pass == 0:
    composite = 'NULL'
elif n_pass == 1:
    composite = 'WEAK-EXPLORATORY'
elif n_pass <= 3:
    composite = 'PARTIAL-PASS'
else:
    composite = 'STRONG-PASS'

# ---- Top-15 / Bottom-15 ----
sorted_by_gm = sorted(sids, key=lambda s: per_surah[s]['geom_mean_freq'])
top15_rare = sorted_by_gm[:15]  # lowest geom_mean = most rare-vocab
top15_common = sorted_by_gm[-15:][::-1]  # highest geom_mean = most common-vocab

# Length-residualized: rank by within-quintile rank average across all 5 quintiles
# Simpler: report per-quintile lowest 3
top_per_quintile = {}
for q in range(5):
    in_q = [s for s in sids if bin_of[s] == q]
    in_q_sorted = sorted(in_q, key=lambda s: per_surah[s]['geom_mean_freq'])
    top_per_quintile[q] = {
        'n_in_quintile': len(in_q),
        'log_n_min': min(log_n[s] for s in in_q),
        'log_n_max': max(log_n[s] for s in in_q),
        'most_rare': [{'sid': s, 'name': surah_meta[s]['name_tl'], 'geom_mean_freq': per_surah[s]['geom_mean_freq']} for s in in_q_sorted[:3]],
        'most_common': [{'sid': s, 'name': surah_meta[s]['name_tl'], 'geom_mean_freq': per_surah[s]['geom_mean_freq']} for s in in_q_sorted[-3:][::-1]],
    }

# ---- Write per-surah CSV ----
fieldnames = ['sid', 'name_tl', 'type', 'genre', 'n_root_tokens', 'n_distinct_roots',
              'mean_freq', 'geom_mean_freq', 'median_freq', 'rare_density_5',
              'hapax_density', 'common_only_density', 'null_z', 'log_n',
              'length_quintile', 'gm_resid_rank_in_quintile',
              'rare5_resid_rank_in_quintile', 'hapax_resid_rank_in_quintile']
with open(OUT_PER_SURAH, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for sid in sids:
        row = {k: per_surah[sid].get(k, '') for k in fieldnames}
        w.writerow(row)
print(f"\nWrote per-surah CSV: {OUT_PER_SURAH}", file=sys.stderr)

# ---- Write summary JSON ----
def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o

summary = {
    'finding_id': 'h-new-91',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'rules_tuple': '(no-tashkeel, STEM-root tokens, QAC-roots v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)',
    'date': '2026-04-15',
    'n_surahs_ranked': len(sids),
    'n_global_roots': len(ROOT_F),
    'total_root_tokens': TOTAL_TOKENS,
    'tests': {
        'T1_heterogeneity': t1,
        'T2_length_confound': t2,
        'T3_q26_al_shuara': t3,
        'T4_hapax_final_xref': t4,
        'T5_genre_anova': t5,
    },
    'composite_verdict': composite,
    'n_tests_pass': n_pass,
    'top15_rare_root_density': [
        {'sid': s, 'name': surah_meta[s]['name_tl'], 'genre': per_surah[s]['genre'],
         'geom_mean_freq': per_surah[s]['geom_mean_freq'],
         'rare_density_5': per_surah[s]['rare_density_5'],
         'hapax_density': per_surah[s]['hapax_density'],
         'n_root_tokens': per_surah[s]['n_root_tokens'],
         'length_quintile': per_surah[s]['length_quintile'],
         'null_z': per_surah[s]['null_z']} for s in top15_rare],
    'top15_common_only': [
        {'sid': s, 'name': surah_meta[s]['name_tl'], 'genre': per_surah[s]['genre'],
         'geom_mean_freq': per_surah[s]['geom_mean_freq'],
         'common_only_density': per_surah[s]['common_only_density'],
         'n_root_tokens': per_surah[s]['n_root_tokens'],
         'length_quintile': per_surah[s]['length_quintile'],
         'null_z': per_surah[s]['null_z']} for s in top15_common],
    'top_per_length_quintile': top_per_quintile,
}
summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"Wrote summary JSON: {OUT_JSON}", file=sys.stderr)
print(f"\nComposite verdict: {composite} ({n_pass}/4 tests pass at α_bon=0.01)", file=sys.stderr)
