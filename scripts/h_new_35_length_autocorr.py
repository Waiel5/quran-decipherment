#!/usr/bin/env python3
"""H-NEW-35 — Verse-length autocorrelation as rhythmic-memory signature.

al-Sakkākī Miftāḥ al-ʿUlūm pp. 527-540 on īqāʿ (rhythm): Quranic verse-length
sequences should show positive short-range autocorrelation (ρ(1) > 0)
decaying with lag.

Sub-tests (Bonferroni k=3, α_bon=0.0167):
  (a) Quran ρ(1) z > +2.58 vs phase-shuffle null (within-surah)
  (b) Monotonic decay ρ(1) > ρ(2) > ρ(3) > ρ(4) > ρ(5)
  (c) Quran ρ(1) differs from Bukhari AND Jahiz ρ(1) via Fisher-z |Δ| > 2.58

Rules: (no-tashkeel, hafs-kufan, character-length of cleaned verse).
Null: phase-shuffle within each surah 1000 times, weighted by surah length.
Seed 20260414.
"""

import json
import math
import random
import re
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260414)

AR_LETTER = re.compile(r'[\u0621-\u064A]')


def len_letters(text):
    return sum(1 for ch in text if AR_LETTER.match(ch))


# ---- Load Quran verse-length sequences per surah ----
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())

surahs = {}  # sid -> list of verse lengths
for s in sorted(Q, key=lambda x: x['id']):
    sid = s['id']
    lens = [len_letters(v['text']) for v in s['verses']]
    surahs[sid] = lens

print(f"n surahs: {len(surahs)}", file=sys.stderr)
print(f"sample surah 1 lens: {surahs[1]}", file=sys.stderr)
print(f"sample surah 108 lens: {surahs[108]}", file=sys.stderr)


def pearson_r(x, y):
    n = len(x)
    if n < 2:
        return 0.0
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    vx = sum((xi - mx) ** 2 for xi in x)
    vy = sum((yi - my) ** 2 for yi in y)
    if vx == 0 or vy == 0:
        return 0.0
    return num / math.sqrt(vx * vy)


def autocorr(series, lag):
    if len(series) <= lag:
        return None
    return pearson_r(series[:-lag], series[lag:])


# ---- Per-surah ρ(k) for k=1..5 ----
LAGS = [1, 2, 3, 4, 5]


def surah_rhos(seq, lags):
    out = {}
    for k in lags:
        r = autocorr(seq, k)
        out[k] = r
    return out


def weighted_mean(values, weights):
    num, den = 0.0, 0.0
    for v, w in zip(values, weights):
        if v is None:
            continue
        num += v * w
        den += w
    return num / den if den > 0 else 0.0


# Compute per-surah rhos
per_surah = {}
for sid, lens in surahs.items():
    per_surah[sid] = surah_rhos(lens, LAGS)

# Weighted mean ρ(k) — weighting by (N - k) as variance weight
quran_rhos = {}
for k in LAGS:
    vals = []
    wts = []
    for sid, lens in surahs.items():
        r = per_surah[sid][k]
        if r is None:
            continue
        w = len(lens) - k  # effective sample size for lag k
        vals.append(r)
        wts.append(w)
    quran_rhos[k] = weighted_mean(vals, wts)

print("\nQuran weighted-mean ρ(k):", file=sys.stderr)
for k in LAGS:
    print(f"  ρ({k}) = {quran_rhos[k]:.4f}", file=sys.stderr)

# ---- Phase-shuffle null: 1000 perms per full experiment ----
N_PERM = 1000
print(f"\n=== Phase-shuffle null ({N_PERM} perms) ===", file=sys.stderr)

null_rhos = {k: [] for k in LAGS}
for perm in range(N_PERM):
    shuffled_rhos = {k: [] for k in LAGS}
    shuffled_wts = {k: [] for k in LAGS}
    for sid, lens in surahs.items():
        sh = list(lens)
        random.shuffle(sh)
        rhos = surah_rhos(sh, LAGS)
        for k in LAGS:
            if rhos[k] is None:
                continue
            shuffled_rhos[k].append(rhos[k])
            shuffled_wts[k].append(len(lens) - k)
    for k in LAGS:
        w = weighted_mean(shuffled_rhos[k], shuffled_wts[k])
        null_rhos[k].append(w)
    if (perm + 1) % 100 == 0:
        print(f"  perm {perm+1}/{N_PERM}", file=sys.stderr)

# Compute z for each lag
null_stats = {}
for k in LAGS:
    vals = null_rhos[k]
    m = statistics.mean(vals)
    sd = statistics.stdev(vals) if len(vals) > 1 else 0
    obs = quran_rhos[k]
    z = (obs - m) / sd if sd > 0 else 0
    p_emp = sum(1 for x in vals if x >= obs) / len(vals)  # upper tail
    null_stats[k] = {
        'null_mean': m, 'null_sd': sd, 'observed': obs, 'z': z, 'p_empirical': p_emp,
    }
    print(f"lag {k}: obs={obs:.4f}, null μ={m:.4f}±{sd:.4f}, z={z:+.3f}, p_emp={p_emp:.4f}",
          file=sys.stderr)

# ---- Sub-test (a): ρ(1) z > +2.58 ----
z_a = null_stats[1]['z']
a_pass = z_a > 2.58
print(f"\nSub-(a) ρ(1) z = {z_a:+.3f} > 2.58? {'PASS' if a_pass else 'FAIL'}", file=sys.stderr)

# ---- Sub-test (b): monotonic decay ρ(1) > ρ(2) > ρ(3) > ρ(4) > ρ(5) ----
rho_seq = [quran_rhos[k] for k in LAGS]
strictly_monotone = all(rho_seq[i] > rho_seq[i+1] for i in range(len(rho_seq)-1))
partially_monotone = rho_seq[0] > rho_seq[-1]
b_pass_strict = strictly_monotone
b_pass_loose = partially_monotone
print(f"Sub-(b) strict decay ρ(1)>ρ(2)>ρ(3)>ρ(4)>ρ(5): {b_pass_strict}", file=sys.stderr)
print(f"       loose decay ρ(1) > ρ(5): {b_pass_loose}", file=sys.stderr)

# ---- Sub-test (c): Quran vs Bukhari/Jahiz sentence-length ----
# Extract sentence-length sequences from each baseline corpus.
# Use period/full-stop as sentence boundary since Arabic prose uses these.
print("\n=== Baseline sentence-length autocorrelations ===", file=sys.stderr)

def sentence_lens_from_text(text, hadith_split=False):
    """Extract sentence-length sequences. For hadith corpora without punctuation,
    split on 'ḥaddathanā' markers which delimit separate hadith reports."""
    if hadith_split:
        # Split Bukhari on ḥaddathanā / ʾakhbaranā / qāla markers as
        # hadith-report boundaries
        parts = re.split(r'حدثنا|أخبرنا|وحدثنا|وأخبرنا', text)
    else:
        parts = re.split(r'[.!?؟۔\n]+|\s{2,}', text)
    lens = []
    for s in parts:
        L = len_letters(s)
        if L > 0:
            lens.append(L)
    return lens


bukhari_path = ROOT / 'data/baseline-corpora/raw/bukhari-noquran.txt'
jahiz_path = ROOT / 'data/baseline-corpora/raw/jahiz-hayawan.txt'

bukhari_sents = sentence_lens_from_text(
    bukhari_path.read_text(encoding='utf-8', errors='replace'), hadith_split=True)
jahiz_sents = sentence_lens_from_text(
    jahiz_path.read_text(encoding='utf-8', errors='replace'))

print(f"bukhari sentences: {len(bukhari_sents)}, mean len: {statistics.mean(bukhari_sents):.1f}",
      file=sys.stderr)
print(f"jahiz sentences: {len(jahiz_sents)}, mean len: {statistics.mean(jahiz_sents):.1f}",
      file=sys.stderr)

# Compute ρ(1) on full baseline sequences (treated as one long series)
baseline_rhos = {}
for name, seq in [('bukhari', bukhari_sents), ('jahiz', jahiz_sents)]:
    row = {}
    for k in LAGS:
        r = autocorr(seq, k)
        row[k] = r if r is not None else float('nan')
    baseline_rhos[name] = row
    formatted = [f"{row[k]:.4f}" if not math.isnan(row[k]) else "NaN" for k in LAGS]
    print(f"{name} n={len(seq)} ρ(1..5): {formatted}", file=sys.stderr)


# Fisher z-transform and differential test
def fisher_z(r):
    if abs(r) >= 1:
        r = 0.999 * (1 if r > 0 else -1)
    return 0.5 * math.log((1 + r) / (1 - r))


def fisher_z_diff(r1, n1, r2, n2):
    z1, z2 = fisher_z(r1), fisher_z(r2)
    se = math.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))
    z_diff = (z1 - z2) / se
    return z_diff


# N for Quran = sum of verse pairs = sum(len-k) for k=1
N_quran_pairs = sum(len(lens) - 1 for lens in surahs.values() if len(lens) > 1)
N_bukhari = len(bukhari_sents) - 1
N_jahiz = len(jahiz_sents) - 1

z_diff_bukhari = fisher_z_diff(quran_rhos[1], N_quran_pairs,
                                baseline_rhos['bukhari'][1], N_bukhari)
z_diff_jahiz = fisher_z_diff(quran_rhos[1], N_quran_pairs,
                              baseline_rhos['jahiz'][1], N_jahiz)

print(f"\nFisher z-diff Quran vs Bukhari ρ(1): {z_diff_bukhari:+.3f}", file=sys.stderr)
print(f"Fisher z-diff Quran vs Jahiz ρ(1): {z_diff_jahiz:+.3f}", file=sys.stderr)

c_pass = abs(z_diff_bukhari) > 2.58 and abs(z_diff_jahiz) > 2.58
print(f"Sub-(c) |Δ| > 2.58 vs BOTH: {c_pass}", file=sys.stderr)

# ---- Verdict ----
joint_strict = a_pass and b_pass_strict and c_pass
joint_loose = a_pass and b_pass_loose and c_pass
print(f"\n=== Verdicts ===", file=sys.stderr)
print(f"(a) ρ(1) z>+2.58: {'PASS' if a_pass else 'FAIL'} (z={z_a:+.3f})", file=sys.stderr)
print(f"(b) strict decay: {'PASS' if b_pass_strict else 'FAIL'}", file=sys.stderr)
print(f"(b) loose decay ρ(1)>ρ(5): {'PASS' if b_pass_loose else 'FAIL'}", file=sys.stderr)
print(f"(c) differ from both baselines: {'PASS' if c_pass else 'FAIL'}", file=sys.stderr)
print(f"Joint strict: {'PASS' if joint_strict else 'FAIL'}", file=sys.stderr)
print(f"Joint loose: {'PASS' if joint_loose else 'FAIL'}", file=sys.stderr)

out = {
    'seed': 20260414,
    'hypothesis': 'H-NEW-35 verse-length autocorrelation — al-Sakkākī īqāʿ',
    'rules_tuple': 'no-tashkeel, hafs-kufan, character-length-cleaned',
    'lags': LAGS,
    'quran_weighted_mean_rho': quran_rhos,
    'null_stats_per_lag': null_stats,
    'baseline_rhos': baseline_rhos,
    'N_quran_pairs': N_quran_pairs,
    'N_bukhari_sentences': len(bukhari_sents),
    'N_jahiz_sentences': len(jahiz_sents),
    'bukhari_mean_sent_len': statistics.mean(bukhari_sents),
    'jahiz_mean_sent_len': statistics.mean(jahiz_sents),
    'fisher_z_diff_vs_bukhari_rho1': z_diff_bukhari,
    'fisher_z_diff_vs_jahiz_rho1': z_diff_jahiz,
    'sub_a_pass': a_pass,
    'sub_b_strict_pass': b_pass_strict,
    'sub_b_loose_pass': b_pass_loose,
    'sub_c_pass': c_pass,
    'joint_strict_pass': joint_strict,
    'joint_loose_pass': joint_loose,
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-35.json'
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
