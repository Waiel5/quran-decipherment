#!/usr/bin/env python3
"""H-NEW-181 — Per-surah verse-length autocorrelation.

Pre-reg: findings/phase-b-hypotheses/h-new-181-verse-length-acf-prereg.md
Seed 20260419. Bonferroni-2, α_bon=0.025 per leg.

- For each surah with N>=20 verses, compute verse-length (letters) ACF k=1..10,
  PACF k=1..5, Ljung-Box Q(m=10).
- Null: 2000 within-surah phase-shuffle permutations per surah.
- Leg A: Fisher exact 2-sided — top-10 by Q enriched for (muq OR Meccan).
- Leg B: Spearman(Q, H-NEW-163 dispersion) AND Spearman(Q, H-NEW-178 (α,β) residual).
"""
import csv
import hashlib
import json
import math
import random
import re
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
N_PERM = 2000
MIN_N = 20

PREREG = ROOT / 'findings/phase-b-hypotheses/h-new-181-verse-length-acf-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-181.json'
OUT_CSV = ROOT / 'findings/phase-b-hypotheses/csv/h-new-181-per-surah.csv'

prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

AR_LETTER = re.compile(r'[\u0621-\u064A]')


def len_letters(text):
    return sum(1 for ch in text if AR_LETTER.match(ch))


# ---- Load verse-length sequences ----
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
surahs = {}
for s in sorted(Q, key=lambda x: x['id']):
    sid = s['id']
    lens = [len_letters(v['text']) for v in s['verses']]
    surahs[sid] = lens

included = {sid: lens for sid, lens in surahs.items() if len(lens) >= MIN_N}
print(f"Included surahs (N>={MIN_N}): {len(included)} / {len(surahs)}", file=sys.stderr)


# ---- ACF / PACF / Ljung-Box ----
def acf(x, lag):
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n <= lag:
        return float('nan')
    m = x.mean()
    num = np.sum((x[:n - lag] - m) * (x[lag:] - m))
    den = np.sum((x - m) ** 2)
    if den == 0:
        return float('nan')
    return float(num / den)


def pacf_durbin_levinson(x, max_lag):
    """PACF via Durbin-Levinson; returns array[max_lag] where index k-1 is pacf(k)."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    r = np.array([acf(x, k) for k in range(max_lag + 1)])  # r[0]=1
    r[0] = 1.0
    phi = np.zeros((max_lag + 1, max_lag + 1))
    pacf = np.zeros(max_lag + 1)
    for k in range(1, max_lag + 1):
        if k == 1:
            phi[1, 1] = r[1]
        else:
            num = r[k] - sum(phi[k - 1, j] * r[k - j] for j in range(1, k))
            den = 1 - sum(phi[k - 1, j] * r[j] for j in range(1, k))
            if den == 0:
                phi[k, k] = float('nan')
            else:
                phi[k, k] = num / den
            for j in range(1, k):
                phi[k, j] = phi[k - 1, j] - phi[k, k] * phi[k - 1, k - j]
        pacf[k] = phi[k, k]
    return pacf[1:]  # pacf(1..max_lag)


def ljung_box_Q(x, m=10):
    n = len(x)
    q = 0.0
    for k in range(1, m + 1):
        rk = acf(x, k)
        if not np.isnan(rk):
            q += rk * rk / max(n - k, 1)
    q *= n * (n + 2)
    return q


# ---- Per-surah compute ----
rng = random.Random(SEED)
np.random.seed(SEED)

rows = []
for sid in sorted(included):
    lens = included[sid]
    N = len(lens)
    acf_obs = [acf(lens, k) for k in range(1, 11)]
    pacf_obs = list(pacf_durbin_levinson(lens, 5))
    q_obs = ljung_box_Q(lens, m=10)
    # permutation null on Q
    q_null = []
    for p in range(N_PERM):
        sh = lens[:]
        rng.shuffle(sh)
        q_null.append(ljung_box_Q(sh, m=10))
    q_null_arr = np.array(q_null)
    p_perm = (1 + int(np.sum(q_null_arr >= q_obs))) / (1 + N_PERM)
    # chi2 asymptotic
    p_chi2 = float(1.0 - stats.chi2.cdf(q_obs, df=10))
    max_abs_acf = max((abs(r) for r in acf_obs if not math.isnan(r)), default=float('nan'))
    max_abs_acf_lag = int(1 + int(np.argmax([abs(r) if not math.isnan(r) else -1 for r in acf_obs])))
    rows.append({
        'sid': sid, 'N': N,
        'acf': acf_obs, 'pacf': pacf_obs,
        'Q_LB': q_obs, 'p_LB_chi2': p_chi2, 'p_LB_perm': p_perm,
        'max_abs_acf': max_abs_acf, 'max_abs_acf_lag': max_abs_acf_lag,
        'null_mean_Q': float(q_null_arr.mean()),
        'null_sd_Q': float(q_null_arr.std(ddof=1)),
        'z_Q': float((q_obs - q_null_arr.mean()) / q_null_arr.std(ddof=1)) if q_null_arr.std(ddof=1) > 0 else 0.0,
    })
    if sid % 20 == 0 or sid == 1:
        print(f"  sid={sid:3d} N={N:3d} Q={q_obs:.2f} p_perm={p_perm:.4f} z={rows[-1]['z_Q']:+.2f}", file=sys.stderr)

# Rank
rows.sort(key=lambda r: -r['Q_LB'])
for rank, row in enumerate(rows, start=1):
    row['rank_by_Q'] = rank

# ---- Classifications ----
MUQ = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29,
       30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}

period = {}
name_ar = {}
with open(ROOT / 'data/revelation-order.csv', encoding='utf-8') as f:
    r = csv.DictReader(f)
    for rec in r:
        sid = int(rec['mushaf_order'])
        period[sid] = rec['period']
        name_ar[sid] = rec['surah_name_ar']

for row in rows:
    row['is_muq'] = int(row['sid'] in MUQ)
    row['period'] = period.get(row['sid'], '')
    row['is_meccan'] = int(period.get(row['sid'], '') == 'Meccan')
    row['muq_or_meccan'] = int(row['is_muq'] or row['is_meccan'])
    row['name_ar'] = name_ar.get(row['sid'], '')

# ---- Top/bottom-10 ----
top10 = rows[:10]
bot10 = rows[-10:]

print(f"\n=== Top-10 by Ljung-Box Q ===", file=sys.stderr)
for r in top10:
    print(f"  Q{r['sid']:3d} N={r['N']:3d} Q={r['Q_LB']:7.2f} p_perm={r['p_LB_perm']:.4f} "
          f"acf1={r['acf'][0]:+.3f} muq={r['is_muq']} mec={r['is_meccan']} ({r['name_ar']})",
          file=sys.stderr)

print(f"\n=== Bottom-10 by Ljung-Box Q ===", file=sys.stderr)
for r in bot10:
    print(f"  Q{r['sid']:3d} N={r['N']:3d} Q={r['Q_LB']:7.2f} p_perm={r['p_LB_perm']:.4f} "
          f"acf1={r['acf'][0]:+.3f} muq={r['is_muq']} mec={r['is_meccan']} ({r['name_ar']})",
          file=sys.stderr)

# ---- Leg A: Fisher exact top-10 vs rest × muq-or-Meccan vs not ----
k_top_hit = sum(r['muq_or_meccan'] for r in top10)
k_top_miss = 10 - k_top_hit
k_rest_hit = sum(r['muq_or_meccan'] for r in rows[10:])
k_rest_miss = (len(rows) - 10) - k_rest_hit
table = [[k_top_hit, k_top_miss], [k_rest_hit, k_rest_miss]]
odds, p_fisher = stats.fisher_exact(table, alternative='two-sided')
baseline_rate = (k_top_hit + k_rest_hit) / len(rows)
print(f"\nLeg A — top-10 muq-or-Meccan hits: {k_top_hit}/10 vs baseline {baseline_rate:.3f}",
      file=sys.stderr)
print(f"  2×2: {table}", file=sys.stderr)
print(f"  Fisher OR={odds:.3f}, p={p_fisher:.4f}", file=sys.stderr)
leg_a_pass = p_fisher < 0.025

# ---- Leg B: Spearman vs dispersion + α/β residual ----
disp_by_sid = {}
with open(ROOT / 'findings/phase-b-hypotheses/csv/h-new-168-per-surah-dispersion.csv',
          encoding='utf-8') as f:
    r = csv.DictReader(f)
    for rec in r:
        disp_by_sid[int(rec['sid'])] = float(rec['dispersion'])

ab_by_sid = {}
with open(ROOT / 'findings/phase-b-hypotheses/csv/h-new-172-per-surah.csv', encoding='utf-8') as f:
    r = csv.DictReader(f)
    for rec in r:
        sid = int(rec['surah_id'])
        try:
            a = float(rec['alpha'])
            b = float(rec['beta_h159'])
        except (ValueError, TypeError):
            continue
        if math.isnan(a) or math.isnan(b):
            continue
        # residual from α = -3.526 β + 3.689
        pred = -3.526 * b + 3.689
        resid = a - pred
        ab_by_sid[sid] = {'alpha': a, 'beta': b, 'resid': resid}

# Leg-B axis 1: Q vs dispersion (restrict to overlap)
q_vals_d, d_vals = [], []
for row in rows:
    if row['sid'] in disp_by_sid:
        q_vals_d.append(row['Q_LB'])
        d_vals.append(disp_by_sid[row['sid']])
rho_d, p_d = stats.spearmanr(q_vals_d, d_vals)

# Leg-B axis 2: Q vs |α/β residual|
q_vals_r, r_vals = [], []
for row in rows:
    if row['sid'] in ab_by_sid and not math.isnan(ab_by_sid[row['sid']]['resid']):
        q_vals_r.append(row['Q_LB'])
        r_vals.append(abs(ab_by_sid[row['sid']]['resid']))
if len(q_vals_r) >= 3:
    rho_r, p_r = stats.spearmanr(q_vals_r, r_vals)
    rho_r = float(rho_r); p_r = float(p_r)
else:
    rho_r, p_r = float('nan'), float('nan')

# Bonferroni-within-leg-B (2 axes): effective α = 0.0125
p_candidates = [(p_d, 'dispersion'), (p_r, 'ab_residual')]
p_candidates = [(p, a) for p, a in p_candidates if not math.isnan(p)]
p_best, leg_b_best_axis = min(p_candidates, key=lambda x: x[0]) if p_candidates else (float('nan'), 'none')
leg_b_pass = (not math.isnan(p_best)) and p_best < 0.0125  # bonferroni-within
# Alternative: leg-B overall α = 0.025 any axis Bonferroni-adjusted
# p_best_adj = min(2 * p_best, 1.0)  # treat axes as multiple tests at α_leg=0.025

print(f"\nLeg B axis 1 (Q vs dispersion n={len(q_vals_d)}): ρ={rho_d:+.3f}, p={p_d:.4f}",
      file=sys.stderr)
print(f"Leg B axis 2 (Q vs |α/β resid| n={len(q_vals_r)}): ρ={rho_r:+.3f}, p={p_r:.4f}",
      file=sys.stderr)
print(f"Leg B best axis: {leg_b_best_axis}, p_best={p_best:.4f} (α_bon-within=0.0125)",
      file=sys.stderr)
print(f"Leg B pass: {leg_b_pass}", file=sys.stderr)

# Bonferroni-2 overall
joint_pass = leg_a_pass and leg_b_pass
verdict = (
    'PASS' if joint_pass else
    'PARTIAL-A' if leg_a_pass else
    'PARTIAL-B' if leg_b_pass else
    'NULL'
)
print(f"\n=== Verdict ===  Leg A={leg_a_pass} Leg B={leg_b_pass} → {verdict}", file=sys.stderr)

# ---- Write CSV ----
with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['rank_by_Q', 'sid', 'name_ar', 'N', 'Q_LB', 'z_Q', 'p_LB_perm', 'p_LB_chi2',
                'acf_1', 'acf_2', 'acf_3', 'acf_4', 'acf_5', 'acf_6', 'acf_7', 'acf_8',
                'acf_9', 'acf_10', 'pacf_1', 'pacf_2', 'pacf_3', 'pacf_4', 'pacf_5',
                'max_abs_acf', 'max_abs_acf_lag', 'is_muq', 'period', 'muq_or_meccan'])
    for row in rows:
        w.writerow([row['rank_by_Q'], row['sid'], row['name_ar'], row['N'],
                    f"{row['Q_LB']:.4f}", f"{row['z_Q']:.4f}",
                    f"{row['p_LB_perm']:.6f}", f"{row['p_LB_chi2']:.6f}",
                    *[f"{v:.4f}" if not math.isnan(v) else 'NaN' for v in row['acf']],
                    *[f"{v:.4f}" if not math.isnan(v) else 'NaN' for v in row['pacf']],
                    f"{row['max_abs_acf']:.4f}", row['max_abs_acf_lag'],
                    row['is_muq'], row['period'], row['muq_or_meccan']])

# ---- Write JSON ----
out = {
    'id': 'H-NEW-181',
    'seed': SEED,
    'prereg_sha256': prereg_sha,
    'rules_tuple': '(no-tashkeel; hafs-kufan; letter-count per verse; N>=20; N_PERM=2000)',
    'n_included': len(rows),
    'bonferroni_k': 2,
    'alpha_bon_per_leg': 0.025,
    'top10': [{'rank': r['rank_by_Q'], 'sid': r['sid'], 'name_ar': r['name_ar'],
               'N': r['N'], 'Q_LB': r['Q_LB'], 'p_LB_perm': r['p_LB_perm'],
               'p_LB_chi2': r['p_LB_chi2'], 'z_Q': r['z_Q'],
               'acf_1_5': r['acf'][:5], 'pacf_1_5': r['pacf'],
               'is_muq': r['is_muq'], 'period': r['period']} for r in top10],
    'bottom10': [{'rank': r['rank_by_Q'], 'sid': r['sid'], 'name_ar': r['name_ar'],
                  'N': r['N'], 'Q_LB': r['Q_LB'], 'p_LB_perm': r['p_LB_perm'],
                  'p_LB_chi2': r['p_LB_chi2'], 'z_Q': r['z_Q'],
                  'acf_1': r['acf'][0], 'is_muq': r['is_muq'], 'period': r['period']}
                 for r in bot10],
    'leg_A_fisher': {
        'top10_muq_or_meccan_hits': k_top_hit,
        'baseline_rate': baseline_rate,
        'table_2x2': table,
        'odds_ratio': odds,
        'p_fisher_2sided': p_fisher,
        'pass_at_alpha_0.025': leg_a_pass,
    },
    'leg_B_spearman': {
        'axis1_Q_vs_dispersion': {'n': len(q_vals_d), 'rho': rho_d, 'p': p_d},
        'axis2_Q_vs_ab_residual': {'n': len(q_vals_r), 'rho': rho_r, 'p': p_r},
        'best_axis': leg_b_best_axis,
        'p_best': p_best,
        'alpha_bon_within_leg': 0.0125,
        'pass': leg_b_pass,
    },
    'verdict': verdict,
}
OUT_JSON.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {OUT_JSON}", file=sys.stderr)
print(f"saved: {OUT_CSV}", file=sys.stderr)
