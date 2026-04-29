#!/usr/bin/env python3
"""H-NEW-208 — Verse-position within-surah structural analysis.

Pre-reg: findings/phase-b-hypotheses/h-new-208-verse-position-structural-prereg.md

Tests (Bonferroni k=3, α_bon = 0.01667, two-tailed):
  T1 Kruskal-Wallis verse-length across {FIRST, Q1, MID, Q3, LAST}
  T2 Kruskal-Wallis divine-name count across same 5 bands
  T3 Mann-Whitney U MID vs non-MID on verse-length

Secondary:
  S1 Per-surah MIDPOINT z-score (verse-length, num_names)
  S2 Spearman ρ(position, verse-length) global
  S3 Sensitivity: drop Q1-Q9 and surahs with V<20

Seed: 20260419.
"""
import csv
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
random.seed(SEED)

# ------------------------------------------------------------------
# Normalization (matches methodology §8 letter-count conventions)
# ------------------------------------------------------------------
# Combining/tashkeel/recitation marks to strip for grapheme count
STRIP_RE = re.compile(r'[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]')
# Whitespace and non-letter punctuation
NONLETTER_RE = re.compile(r'[\s\u060C\u061B\u061F\u06D4\u06DD\u06DE\u06DF\u200C\u200D\u200E\u200F\u00B7]+')

def letter_count(text: str) -> int:
    t = STRIP_RE.sub('', text)
    t = NONLETTER_RE.sub('', t)
    return len(t)

# ------------------------------------------------------------------
# Load corpus
# ------------------------------------------------------------------
with open(ROOT / 'quran-text' / 'quran-no-tashkeel.json', encoding='utf-8') as f:
    RAW = json.load(f)

# Build verse-level dataframe analogue
VERSES = []  # list of dicts
for s in RAW:
    V = s['total_verses']
    for v in s['verses']:
        pos = (v['id'] - 0.5) / V
        VERSES.append({
            'surah': s['id'],
            'verse': v['id'],
            'V': V,
            'pos': pos,
            'text': v['text'],
            'len': letter_count(v['text']),
        })

assert len(VERSES) == 6236, f"verse count mismatch: {len(VERSES)}"

# ------------------------------------------------------------------
# Divine-name count per verse
# ------------------------------------------------------------------
DNAMES = defaultdict(int)
with open(ROOT / 'findings' / 'phase-b-hypotheses' / 'divine-names-by-verse.csv', encoding='utf-8') as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        key = (int(row['surah']), int(row['verse']))
        DNAMES[key] = int(row['num_names'])

for v in VERSES:
    v['num_names'] = DNAMES.get((v['surah'], v['verse']), 0)

# ------------------------------------------------------------------
# Banding
# ------------------------------------------------------------------
def band_verses(V: int):
    """Return dict band->v_id following locked rule. None if V<5."""
    if V < 5:
        return None
    def pick(p):
        # nearest v_id to p*V + 0.5 in 1..V
        vid = int(round(p * V + 0.5))
        return max(1, min(V, vid))
    return {
        'FIRST': 1,
        'Q1': pick(0.25),
        'MID': pick(0.50),
        'Q3': pick(0.75),
        'LAST': V,
    }

# Build band samples (one verse per surah per band)
BANDS = ['FIRST', 'Q1', 'MID', 'Q3', 'LAST']
band_len = {b: [] for b in BANDS}
band_names = {b: [] for b in BANDS}
band_surahs_used = 0
midpoint_record = []  # list of (surah, v, V, len, names)

for s in RAW:
    V = s['total_verses']
    bv = band_verses(V)
    if bv is None:
        continue
    band_surahs_used += 1
    # Fast lookup for this surah
    v_index = {v['id']: v for v in s['verses']}
    for b, vid in bv.items():
        text = v_index[vid]['text']
        L = letter_count(text)
        N = DNAMES.get((s['id'], vid), 0)
        band_len[b].append(L)
        band_names[b].append(N)
        if b == 'MID':
            midpoint_record.append({
                'surah': s['id'],
                'v': vid,
                'V': V,
                'len': L,
                'names': N,
                'name': s['transliteration'],
            })

# ------------------------------------------------------------------
# Stats helpers (pure stdlib)
# ------------------------------------------------------------------
def mean(xs): return sum(xs) / len(xs) if xs else 0.0
def var(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1) if len(xs) > 1 else 0.0
def std(xs): return math.sqrt(var(xs))

def rank_with_ties(values):
    """Return ranks (1-indexed, avg for ties), and sum of tie-correction term."""
    idx = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    tie_sum = 0.0
    i = 0
    while i < len(idx):
        j = i
        while j + 1 < len(idx) and values[idx[j + 1]] == values[idx[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0  # average rank
        t = j - i + 1
        if t > 1:
            tie_sum += t ** 3 - t
        for k in range(i, j + 1):
            ranks[idx[k]] = avg
        i = j + 1
    return ranks, tie_sum

def kruskal_wallis(groups):
    """H stat, df, p (chi-sq approx)."""
    pooled = []
    labels = []
    for gi, g in enumerate(groups):
        for x in g:
            pooled.append(x)
            labels.append(gi)
    N = len(pooled)
    ranks, tie_sum = rank_with_ties(pooled)
    R = defaultdict(float)
    n = defaultdict(int)
    for lbl, r in zip(labels, ranks):
        R[lbl] += r
        n[lbl] += 1
    H = 12.0 / (N * (N + 1)) * sum(R[g] ** 2 / n[g] for g in R) - 3 * (N + 1)
    # tie correction
    if tie_sum > 0:
        C = 1.0 - tie_sum / (N ** 3 - N)
        if C > 0:
            H = H / C
    df = len(groups) - 1
    # chi-sq survival function via Wilson-Hilferty or series; use regularized gamma
    p = chi2_sf(H, df)
    return H, df, p

def chi2_sf(x, k):
    """Upper-tail chi-square survival function for integer df."""
    if x <= 0:
        return 1.0
    # Use regularized incomplete gamma Q(k/2, x/2)
    return regularized_gamma_q(k / 2.0, x / 2.0)

def regularized_gamma_q(a, x):
    if x < 0 or a <= 0:
        return 1.0
    if x < a + 1:
        return 1.0 - regularized_gamma_p_series(a, x)
    return regularized_gamma_q_cf(a, x)

def regularized_gamma_p_series(a, x):
    # series
    term = 1.0 / a
    total = term
    for n in range(1, 500):
        term *= x / (a + n)
        total += term
        if abs(term) < abs(total) * 1e-14:
            break
    return total * math.exp(-x + a * math.log(x) - math.lgamma(a))

def regularized_gamma_q_cf(a, x):
    # Lentz's method
    tiny = 1e-300
    b = x + 1 - a
    c = 1.0 / tiny
    d = 1.0 / b
    h = d
    for i in range(1, 500):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-14:
            break
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h

def mann_whitney_u(a, b):
    """Two-sample Mann-Whitney U with normal approximation (two-tailed)."""
    na, nb = len(a), len(b)
    pooled = list(a) + list(b)
    ranks, tie_sum = rank_with_ties(pooled)
    Ra = sum(ranks[:na])
    U1 = Ra - na * (na + 1) / 2.0
    U2 = na * nb - U1
    U = min(U1, U2)
    N = na + nb
    mu = na * nb / 2.0
    # tie-corrected sigma
    sigma = math.sqrt(na * nb * (N + 1) / 12.0 * (1 - tie_sum / (N ** 3 - N)) if tie_sum else na * nb * (N + 1) / 12.0)
    if sigma == 0:
        return U1, 1.0, 0.0
    z = (U1 - mu) / sigma
    # two-tailed
    p = 2 * (1 - norm_cdf(abs(z)))
    # rank-biserial r
    r = 1 - (2 * U) / (na * nb)
    return U1, p, r

def norm_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

def spearman_rho(x, y):
    rx, _ = rank_with_ties(x)
    ry, _ = rank_with_ties(y)
    n = len(x)
    mx, my = mean(rx), mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    if den == 0:
        return 0.0, 1.0
    rho = num / den
    # approximate t-based p
    if n <= 2 or abs(rho) >= 1:
        return rho, 0.0
    t = rho * math.sqrt((n - 2) / (1 - rho ** 2))
    # 2-sided p via student-t → normal approx for large n
    p = 2 * (1 - norm_cdf(abs(t)))
    return rho, p

# ------------------------------------------------------------------
# T1, T2, T3
# ------------------------------------------------------------------
print(f"H-NEW-208 — Verse-position structural analysis")
print(f"Seed: {SEED}")
print(f"Surahs banded (V>=5): {band_surahs_used}")
print(f"Bonferroni k=3, α_bon = 0.01667")
print()

# T1
groups_len = [band_len[b] for b in BANDS]
H1, df1, p1 = kruskal_wallis(groups_len)
print(f"T1 Kruskal-Wallis verse-length across 5 bands:")
for b in BANDS:
    xs = band_len[b]
    print(f"    {b:<6s} n={len(xs):3d}  mean={mean(xs):6.1f}  median={sorted(xs)[len(xs)//2]:4d}  sd={std(xs):5.1f}")
print(f"  H = {H1:.4f}  df = {df1}  p = {p1:.4e}   PASS={p1 < 0.01667}")
print()

# T2
groups_names = [band_names[b] for b in BANDS]
H2, df2, p2 = kruskal_wallis(groups_names)
print(f"T2 Kruskal-Wallis divine-name count across 5 bands:")
for b in BANDS:
    xs = band_names[b]
    print(f"    {b:<6s} n={len(xs):3d}  mean={mean(xs):5.3f}  sum={sum(xs):3d}")
print(f"  H = {H2:.4f}  df = {df2}  p = {p2:.4e}   PASS={p2 < 0.01667}")
print()

# T3
mid = band_len['MID']
non_mid = band_len['FIRST'] + band_len['Q1'] + band_len['Q3'] + band_len['LAST']
U, p3, rbis = mann_whitney_u(mid, non_mid)
print(f"T3 Mann-Whitney U: MID vs non-MID verse-length")
print(f"  MID mean {mean(mid):.1f}   non-MID mean {mean(non_mid):.1f}")
print(f"  U = {U:.1f}  p = {p3:.4e}  rank-biserial r = {rbis:+.4f}")
print(f"  PASS = {p3 < 0.01667 and abs(rbis) >= 0.10}")
print()

# ------------------------------------------------------------------
# S1 Per-surah MIDPOINT anomaly
# ------------------------------------------------------------------
print("S1 Per-surah MIDPOINT anomaly (|z| on verse-length OR num_names >= 2σ):")
anomalies = []
for s in RAW:
    V = s['total_verses']
    if V < 5:
        continue
    bv = band_verses(V)
    mid_v = bv['MID']
    lens = [letter_count(v['text']) for v in s['verses']]
    ns = [DNAMES.get((s['id'], v['id']), 0) for v in s['verses']]
    mu_l, sd_l = mean(lens), std(lens)
    mu_n, sd_n = mean(ns), std(ns)
    mid_L = lens[mid_v - 1]
    mid_N = ns[mid_v - 1]
    z_l = (mid_L - mu_l) / sd_l if sd_l > 0 else 0.0
    z_n = (mid_N - mu_n) / sd_n if sd_n > 0 else 0.0
    if abs(z_l) >= 2.0 or abs(z_n) >= 2.0:
        anomalies.append({
            'surah': s['id'],
            'name': s['transliteration'],
            'V': V,
            'mid_v': mid_v,
            'mid_len': mid_L,
            'z_len': z_l,
            'mid_names': mid_N,
            'z_names': z_n,
        })

anomalies.sort(key=lambda a: -max(abs(a['z_len']), abs(a['z_names'])))
print(f"  n_anomalous_surahs = {len(anomalies)}")
for a in anomalies:
    print(f"    Q{a['surah']:3d} {a['name']:<18s} V={a['V']:3d} mid=v{a['mid_v']:3d}"
          f"  len={a['mid_len']:3d} (z={a['z_len']:+.2f})  names={a['mid_names']} (z={a['z_names']:+.2f})")

# Explicit check on Q18
print()
print("Explicit Q18 al-Kahf check (H-NEW-90 prior):")
for s in RAW:
    if s['id'] != 18:
        continue
    V = s['total_verses']
    bv = band_verses(V)
    print(f"  Q18 V={V}, bands = {bv}")
    lens18 = [letter_count(v['text']) for v in s['verses']]
    n18 = [DNAMES.get((18, v['id']), 0) for v in s['verses']]
    mu_l, sd_l = mean(lens18), std(lens18)
    mu_n, sd_n = mean(n18), std(n18)
    # Also check v50 per H-NEW-90
    print(f"  Q18:50 len={lens18[49]} (z={((lens18[49]-mu_l)/sd_l):+.2f})  "
          f"names={n18[49]} (z={((n18[49]-mu_n)/sd_n if sd_n>0 else 0):+.2f})")
    mid_v = bv['MID']
    print(f"  Q18:{mid_v} (banded MID) len={lens18[mid_v-1]} (z={((lens18[mid_v-1]-mu_l)/sd_l):+.2f})")

print()
# ------------------------------------------------------------------
# S2 Global Spearman position vs verse-length
# ------------------------------------------------------------------
positions = [v['pos'] for v in VERSES]
lengths = [v['len'] for v in VERSES]
rho, p_rho = spearman_rho(positions, lengths)
print(f"S2 Spearman ρ(position, verse-length) all 6236 verses:")
print(f"  ρ = {rho:+.4f}  p = {p_rho:.4e}")

# Also by surah (distribution of per-surah ρ)
per_s_rho = []
for s in RAW:
    if s['total_verses'] < 5:
        continue
    ps = [(v['id'] - 0.5) / s['total_verses'] for v in s['verses']]
    ls = [letter_count(v['text']) for v in s['verses']]
    r, _ = spearman_rho(ps, ls)
    per_s_rho.append((s['id'], r))
mean_r = mean([r for _, r in per_s_rho])
frac_pos = sum(1 for _, r in per_s_rho if r > 0) / len(per_s_rho)
print(f"  per-surah mean ρ = {mean_r:+.4f}  fraction ρ>0: {frac_pos:.3f}")

print()
# ------------------------------------------------------------------
# S3 Sensitivity
# ------------------------------------------------------------------
print("S3 Sensitivity: drop Q1-Q9 and surahs with V<20")
# Rebuild bands with filter
band_len_s3 = {b: [] for b in BANDS}
for s in RAW:
    if s['id'] <= 9:
        continue
    if s['total_verses'] < 20:
        continue
    bv = band_verses(s['total_verses'])
    v_index = {v['id']: v for v in s['verses']}
    for b, vid in bv.items():
        band_len_s3[b].append(letter_count(v_index[vid]['text']))
H1b, _, p1b = kruskal_wallis([band_len_s3[b] for b in BANDS])
mid_s3 = band_len_s3['MID']
non_s3 = band_len_s3['FIRST'] + band_len_s3['Q1'] + band_len_s3['Q3'] + band_len_s3['LAST']
U_s3, p3_s3, r_s3 = mann_whitney_u(mid_s3, non_s3)
print(f"  n_surahs in S3 = {len(band_len_s3['FIRST'])}")
print(f"  T1' p = {p1b:.4e}   T3' p = {p3_s3:.4e}  r = {r_s3:+.4f}")

print()
# ------------------------------------------------------------------
# Summary
# ------------------------------------------------------------------
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"T1 verse-length band-effect          : p={p1:.2e}  {'PASS' if p1 < 0.01667 else 'FAIL'}")
print(f"T2 divine-name band-effect           : p={p2:.2e}  {'PASS' if p2 < 0.01667 else 'FAIL'}")
print(f"T3 MIDPOINT distinguishable (length) : p={p3:.2e}  r={rbis:+.3f}  {'PASS' if (p3 < 0.01667 and abs(rbis) >= 0.10) else 'FAIL'}")
print(f"S1 anomalous MIDPOINT surahs         : {len(anomalies)} / {band_surahs_used}")
print(f"S2 global Spearman ρ(pos, len)       : {rho:+.4f}  (p={p_rho:.2e})")
print(f"S3 T1' p={p1b:.2e}  T3' p={p3_s3:.2e}")

# Write outputs
OUT = ROOT / 'findings' / 'phase-b-hypotheses'
ANAL_OUT = OUT / 'analysis'
ANAL_OUT.mkdir(exist_ok=True)

# Dump band data
with open(ANAL_OUT / 'h-new-208-band-data.csv', 'w', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['band', 'surah', 'verse', 'V', 'len', 'num_names'])
    for s in RAW:
        V = s['total_verses']
        bv = band_verses(V)
        if bv is None:
            continue
        v_index = {v['id']: v for v in s['verses']}
        for b, vid in bv.items():
            text = v_index[vid]['text']
            w.writerow([b, s['id'], vid, V, letter_count(text), DNAMES.get((s['id'], vid), 0)])

# Dump anomalies
with open(ANAL_OUT / 'h-new-208-midpoint-anomalies.csv', 'w', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['surah', 'name', 'V', 'mid_v', 'mid_len', 'z_len', 'mid_names', 'z_names'])
    for a in anomalies:
        w.writerow([a['surah'], a['name'], a['V'], a['mid_v'], a['mid_len'], f"{a['z_len']:.3f}",
                    a['mid_names'], f"{a['z_names']:.3f}"])

print()
print(f"Outputs written:")
print(f"  {ANAL_OUT / 'h-new-208-band-data.csv'}")
print(f"  {ANAL_OUT / 'h-new-208-midpoint-anomalies.csv'}")
