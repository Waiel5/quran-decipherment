#!/usr/bin/env python3
"""H-NEW-195 — Per-surah letter-bigram entropy and Quran vs Bukhārī comparison.

Per-surah H(L2|L1). Top/bottom-5 by raw and length-residualized entropy.
Quran vs Bukhārī (top-114 longest bab-segments). Spearman correlations with
H-NEW-163 dispersion, H-NEW-178 (α,β), muqaṭṭaʿāt, Nöldeke.

Pre-reg: findings/phase-b-hypotheses/h-new-195-entropy-per-surah-prereg.md
Seed: 20260419, Bonferroni k=2 (α_bon=0.025 each).
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
PREREG_FILE = ROOT / "findings/phase-b-hypotheses/h-new-195-entropy-per-surah-prereg.md"
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
BUKHARI_TXT = ROOT / "data/baseline-corpora/raw/bukhari-noquran.txt"
H172_CSV = ROOT / "findings/phase-b-hypotheses/csv/h-new-172-per-surah.csv"
NOLDEKE_CSV = ROOT / "data/revelation-order.csv"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-195.json"
OUT_CSV = ROOT / "findings/phase-b-hypotheses/csv/h-new-195-per-surah.csv"
OUT_BUK_CSV = ROOT / "findings/phase-b-hypotheses/csv/h-new-195-bukhari-per-segment.csv"

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"SEED={SEED}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Normalization: strip tashkeel, pause marks; keep only U+0621..U+064A
# ---------------------------------------------------------------------------
PAUSE_TASHKEEL_RE = re.compile(r"[\u06D6-\u06DF\u0610-\u061A\u064B-\u065F\u0670]")
AR_LETTER_RE = re.compile(r"[\u0621-\u064A]")

def clean_letters(text: str) -> str:
    text = PAUSE_TASHKEEL_RE.sub("", text)
    return "".join(AR_LETTER_RE.findall(text))

# ---------------------------------------------------------------------------
# Entropy helpers
# ---------------------------------------------------------------------------
LOG2 = math.log(2.0)

def entropy_from_counts(counts_iter) -> float:
    total = 0
    counts = list(counts_iter)
    total = sum(counts)
    if total == 0:
        return 0.0
    H = 0.0
    for c in counts:
        if c > 0:
            p = c / total
            H -= p * math.log(p) / LOG2
    return H

def bigram_and_unigram_H(text: str) -> tuple[float, float, float, int, int]:
    """Return (H_unigram, H_joint_bigram, H_cond = H_joint-H_unigram, N_letters, N_bigrams)."""
    N = len(text)
    if N < 2:
        return 0.0, 0.0, 0.0, N, 0
    # Bigrams over adjacent letters (cross-verse since text is concatenated)
    bigrams = Counter()
    for i in range(N - 1):
        bigrams[(text[i], text[i + 1])] += 1
    # L1 marginal (first letter of each bigram) — matches H(L1,L2)-H(L1) convention
    left_counts = Counter()
    for (a, _), c in bigrams.items():
        left_counts[a] += c
    H_unigram = entropy_from_counts(left_counts.values())
    H_joint = entropy_from_counts(bigrams.values())
    H_cond = H_joint - H_unigram
    return H_unigram, H_joint, H_cond, N, sum(bigrams.values())

# ---------------------------------------------------------------------------
# Load Quran
# ---------------------------------------------------------------------------
with open(QURAN_JSON, encoding="utf-8") as f:
    quran = json.load(f)
quran = sorted(quran, key=lambda s: s["id"])
assert len(quran) == 114

per_surah = {}  # sid -> dict
for s in quran:
    sid = s["id"]
    concat = " ".join(v["text"] for v in s["verses"])
    letters = clean_letters(concat)
    Hu, Hj, Hc, Nlet, Nbi = bigram_and_unigram_H(letters)
    per_surah[sid] = {
        "sid": sid,
        "name": s["transliteration"],
        "type": s["type"],
        "n_verses": s["total_verses"],
        "n_letters": Nlet,
        "n_bigrams": Nbi,
        "H_unigram": Hu,
        "H_joint": Hj,
        "H_cond": Hc,
        "letters": letters,  # kept for MW-5 shuffle
    }

print(f"114 surahs processed. Total letters: {sum(d['n_letters'] for d in per_surah.values())}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Load Bukhārī, split at باب, top-114 by letter count
# ---------------------------------------------------------------------------
buk_raw = BUKHARI_TXT.read_text(encoding="utf-8", errors="replace")
buk_clean_text = PAUSE_TASHKEEL_RE.sub("", buk_raw)  # strip tashkeel/pause before splitting
buk_segs = re.split(r"\bباب\b", buk_clean_text)
# Clean each to letters only
buk_letter_segs = []
for seg in buk_segs:
    letters = "".join(AR_LETTER_RE.findall(seg))
    if len(letters) >= 2:
        buk_letter_segs.append(letters)
# Sort by letter count desc, take top 114
buk_letter_segs.sort(key=len, reverse=True)
buk_top114 = buk_letter_segs[:114]
print(f"Bukhārī bab-segments: {len(buk_letter_segs)} total, top-114 range "
      f"[{len(buk_top114[-1])}..{len(buk_top114[0])}] letters", file=sys.stderr)

buk_records = []
for i, seg in enumerate(buk_top114):
    Hu, Hj, Hc, Nlet, Nbi = bigram_and_unigram_H(seg)
    buk_records.append({
        "rank": i + 1,
        "n_letters": Nlet,
        "n_bigrams": Nbi,
        "H_unigram": Hu,
        "H_joint": Hj,
        "H_cond": Hc,
    })

# ---------------------------------------------------------------------------
# Length-controlled residual: OLS H_cond ~ log10(n_bigrams)
# ---------------------------------------------------------------------------
def ols_residuals(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    slope = sxy / sxx if sxx > 0 else 0.0
    intercept = my - slope * mx
    resids = [y - (intercept + slope * x) for x, y in zip(xs, ys)]
    # R^2
    syy = sum((y - my) ** 2 for y in ys)
    r2 = 1.0 - sum(r * r for r in resids) / syy if syy > 0 else 0.0
    return slope, intercept, resids, r2

sids_ordered = sorted(per_surah.keys())
log_nbi = [math.log10(per_surah[sid]["n_bigrams"]) for sid in sids_ordered]
H_cond_list = [per_surah[sid]["H_cond"] for sid in sids_ordered]
slope, intercept, resids, r2 = ols_residuals(log_nbi, H_cond_list)
for sid, r in zip(sids_ordered, resids):
    per_surah[sid]["log_nbigrams"] = math.log10(per_surah[sid]["n_bigrams"])
    per_surah[sid]["residual_H_cond"] = r
print(f"OLS H_cond ~ log10(N_bigrams): slope={slope:.4f} intercept={intercept:.4f} R^2={r2:.4f}",
      file=sys.stderr)

# ---------------------------------------------------------------------------
# Top/bottom-5
# ---------------------------------------------------------------------------
sids_by_Hcond = sorted(sids_ordered, key=lambda s: per_surah[s]["H_cond"])
bot5_raw = sids_by_Hcond[:5]  # lowest H_cond = most predictable
top5_raw = sids_by_Hcond[-5:][::-1]  # highest H_cond = most surprising

sids_by_resid = sorted(sids_ordered, key=lambda s: per_surah[s]["residual_H_cond"])
bot5_resid = sids_by_resid[:5]
top5_resid = sids_by_resid[-5:][::-1]

def fmt_surah_list(sids):
    return [
        {
            "sid": s,
            "name": per_surah[s]["name"],
            "H_cond": per_surah[s]["H_cond"],
            "residual": per_surah[s]["residual_H_cond"],
            "n_letters": per_surah[s]["n_letters"],
        }
        for s in sids
    ]

# ---------------------------------------------------------------------------
# Quran vs Bukhārī comparison: Welch t and Mann-Whitney U
# ---------------------------------------------------------------------------
q_Hcond = [per_surah[s]["H_cond"] for s in sids_ordered]
b_Hcond = [r["H_cond"] for r in buk_records]

def welch_t(a, b):
    na, nb = len(a), len(b)
    ma, mb = statistics.mean(a), statistics.mean(b)
    va = statistics.variance(a) if na > 1 else 0.0
    vb = statistics.variance(b) if nb > 1 else 0.0
    se = math.sqrt(va / na + vb / nb)
    t = (ma - mb) / se if se > 0 else 0.0
    # Welch-Satterthwaite df
    if va > 0 or vb > 0:
        df = (va / na + vb / nb) ** 2 / ((va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1))
    else:
        df = na + nb - 2
    return t, df, ma, mb

def t_to_p_twosided(t, df):
    """Two-sided p-value via regularized incomplete beta. Pure-python impl."""
    # p = I_x(df/2, 1/2) where x = df/(df + t^2)
    x = df / (df + t * t)
    return incbeta(df / 2.0, 0.5, x)

def incbeta(a, b, x):
    """Regularized incomplete beta I_x(a,b). From Numerical Recipes betai."""
    if x <= 0.0: return 0.0
    if x >= 1.0: return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    bt = math.exp(lbeta + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * betacf(a, b, x) / a
    else:
        return 1.0 - bt * betacf(b, a, 1.0 - x) / b

def betacf(a, b, x):
    MAX_IT = 200
    EPS = 3e-16
    FPMIN = 1e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN: d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAX_IT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS:
            return h
    return h

t_stat, df, ma, mb = welch_t(q_Hcond, b_Hcond)
p_welch = t_to_p_twosided(t_stat, df)

def mann_whitney_u(a, b):
    """Two-sample MWU (two-sided). Returns U, p via normal approximation with tie-correction."""
    na, nb = len(a), len(b)
    combined = [(v, 0) for v in a] + [(v, 1) for v in b]
    combined.sort(key=lambda x: x[0])
    # Assign ranks (midranks for ties)
    ranks = [0.0] * (na + nb)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        midrank = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[k] = midrank
        i = j + 1
    R1 = sum(r for r, (_, g) in zip(ranks, combined) if g == 0)
    U1 = R1 - na * (na + 1) / 2.0
    U2 = na * nb - U1
    U = min(U1, U2)
    # Normal approx with tie correction
    # tie correction
    from collections import Counter
    vals = [v for v, _ in combined]
    tie_counts = Counter(vals)
    T = sum(t**3 - t for t in tie_counts.values() if t > 1)
    N = na + nb
    mu = na * nb / 2.0
    sigma2 = na * nb / 12.0 * ((N + 1) - T / (N * (N - 1)))
    sigma = math.sqrt(sigma2) if sigma2 > 0 else 1.0
    z = (U1 - mu) / sigma
    # two-sided normal p
    p = math.erfc(abs(z) / math.sqrt(2.0))
    return U1, U2, z, p

U1, U2, z_mwu, p_mwu = mann_whitney_u(q_Hcond, b_Hcond)

# Paired Wilcoxon by length-sorted pairing (MW-1 length-control)
q_sorted_by_n = sorted(sids_ordered, key=lambda s: per_surah[s]["n_letters"], reverse=True)
q_Hcond_sorted = [per_surah[s]["H_cond"] for s in q_sorted_by_n]
# buk_records already sorted by length desc
b_Hcond_sorted = [r["H_cond"] for r in buk_records]
diffs = [q - b for q, b in zip(q_Hcond_sorted, b_Hcond_sorted)]

def wilcoxon_signed_rank(diffs):
    """Two-sided Wilcoxon signed-rank test with normal approx."""
    nz = [d for d in diffs if d != 0]
    n = len(nz)
    abs_sorted = sorted(nz, key=lambda d: abs(d))
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and abs(abs_sorted[j + 1]) == abs(abs_sorted[i]):
            j += 1
        midrank = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[k] = midrank
        i = j + 1
    Wp = sum(r for r, d in zip(ranks, abs_sorted) if d > 0)
    Wn = sum(r for r, d in zip(ranks, abs_sorted) if d < 0)
    W = min(Wp, Wn)
    mu = n * (n + 1) / 4.0
    sigma2 = n * (n + 1) * (2 * n + 1) / 24.0
    # tie correction
    from collections import Counter
    cnt = Counter(abs(d) for d in nz)
    T = sum(t**3 - t for t in cnt.values() if t > 1) / 48.0
    sigma2 -= T
    sigma = math.sqrt(sigma2) if sigma2 > 0 else 1.0
    z = (Wp - mu) / sigma
    p = math.erfc(abs(z) / math.sqrt(2.0))
    return Wp, Wn, z, p

Wp, Wn, z_wil, p_wil = wilcoxon_signed_rank(diffs)

print(f"\nQuran mean H_cond = {ma:.4f}  Bukhārī mean = {mb:.4f}", file=sys.stderr)
print(f"Welch t = {t_stat:.4f}  df = {df:.1f}  p (two-sided) = {p_welch:.6f}", file=sys.stderr)
print(f"MWU z = {z_mwu:.4f}  p (two-sided) = {p_mwu:.6f}", file=sys.stderr)
print(f"Paired Wilcoxon (length-sorted): z = {z_wil:.4f}  p = {p_wil:.6f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Load covariates from h-new-172-per-surah.csv and Nöldeke
# ---------------------------------------------------------------------------
covariates = {}  # sid -> {alpha, beta, dispersion, is_muq}
with open(H172_CSV, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sid = int(row["surah_id"])
        covariates[sid] = {
            "alpha": float(row["alpha"]),
            "beta": float(row["beta_h159"]),
            "dispersion": float(row["dispersion_h163"]),
            "is_muq": int(row["is_muq"]),
        }

noldeke = {}
with open(NOLDEKE_CSV, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sid = int(row["mushaf_order"])
        noldeke[sid] = int(row["noldeke_order"])

# ---------------------------------------------------------------------------
# Spearman correlations
# ---------------------------------------------------------------------------
def spearman(xs, ys):
    n = len(xs)
    rx = rankdata(xs)
    ry = rankdata(ys)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    dy = math.sqrt(sum((b - my) ** 2 for b in ry))
    rho = num / (dx * dy) if dx > 0 and dy > 0 else 0.0
    # t-approx for large n
    if abs(rho) >= 1.0 or n < 3:
        p = 0.0 if abs(rho) >= 1.0 else 1.0
    else:
        t = rho * math.sqrt((n - 2) / (1 - rho * rho))
        p = t_to_p_twosided(t, n - 2)
    return rho, p, n

def rankdata(arr):
    sorted_idx = sorted(range(len(arr)), key=lambda i: arr[i])
    ranks = [0.0] * len(arr)
    i = 0
    while i < len(arr):
        j = i
        while j + 1 < len(arr) and arr[sorted_idx[j + 1]] == arr[sorted_idx[i]]:
            j += 1
        midrank = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[sorted_idx[k]] = midrank
        i = j + 1
    return ranks

# Align subset: only surahs that appear in covariates (≥50 tokens per H-NEW-178)
common_sids = sorted(set(covariates.keys()) & set(sids_ordered))

# Correlation 1: residual_H_cond vs dispersion (H-NEW-163)
x_disp = [covariates[s]["dispersion"] for s in common_sids]
y_resid = [per_surah[s]["residual_H_cond"] for s in common_sids]
rho_disp, p_disp, _ = spearman(x_disp, y_resid)

# Correlation 2: residual vs α
x_alpha = [covariates[s]["alpha"] for s in common_sids]
rho_alpha, p_alpha, _ = spearman(x_alpha, y_resid)

# Correlation 3: residual vs β
x_beta = [covariates[s]["beta"] for s in common_sids]
rho_beta, p_beta, _ = spearman(x_beta, y_resid)

# Correlation 4: residual vs Nöldeke order
nold_sids = sorted(set(noldeke.keys()) & set(common_sids))
x_nold = [noldeke[s] for s in nold_sids]
y_nold_resid = [per_surah[s]["residual_H_cond"] for s in nold_sids]
rho_nold, p_nold, _ = spearman(x_nold, y_nold_resid)

# Correlation 5 (MWU): muq vs non-muq residual
muq_res = [per_surah[s]["residual_H_cond"] for s in common_sids if covariates[s]["is_muq"] == 1]
nonmuq_res = [per_surah[s]["residual_H_cond"] for s in common_sids if covariates[s]["is_muq"] == 0]
U1_m, U2_m, z_muq, p_muq = mann_whitney_u(muq_res, nonmuq_res)
mean_muq = statistics.mean(muq_res)
mean_nonmuq = statistics.mean(nonmuq_res)

correlations = {
    "dispersion_h163": {"rho": rho_disp, "p": p_disp, "n": len(common_sids)},
    "alpha_h172": {"rho": rho_alpha, "p": p_alpha, "n": len(common_sids)},
    "beta_h159": {"rho": rho_beta, "p": p_beta, "n": len(common_sids)},
    "noldeke": {"rho": rho_nold, "p": p_nold, "n": len(nold_sids)},
    "muq_vs_nonmuq": {
        "mean_muq_residual": mean_muq,
        "mean_nonmuq_residual": mean_nonmuq,
        "n_muq": len(muq_res),
        "n_nonmuq": len(nonmuq_res),
        "mwu_z": z_muq,
        "p": p_muq,
    },
}
print(f"\nCorrelations (residual H_cond vs):", file=sys.stderr)
print(f"  dispersion_h163: ρ={rho_disp:+.4f}  p={p_disp:.4f}", file=sys.stderr)
print(f"  alpha_h172:      ρ={rho_alpha:+.4f}  p={p_alpha:.4f}", file=sys.stderr)
print(f"  beta_h159:       ρ={rho_beta:+.4f}  p={p_beta:.4f}", file=sys.stderr)
print(f"  noldeke:         ρ={rho_nold:+.4f}  p={p_nold:.4f}", file=sys.stderr)
print(f"  muq vs nonmuq:   Δ={mean_muq - mean_nonmuq:+.4f}  MWU z={z_muq:+.3f}  p={p_muq:.4f}",
      file=sys.stderr)

# Strongest correlate = max |ρ| among continuous, or muq effect size if larger |z|
corr_strengths = [
    ("dispersion_h163", abs(rho_disp)),
    ("alpha_h172", abs(rho_alpha)),
    ("beta_h159", abs(rho_beta)),
    ("noldeke", abs(rho_nold)),
]
corr_strengths.sort(key=lambda x: -x[1])
strongest = corr_strengths[0]
print(f"\nStrongest continuous correlate: {strongest[0]} |ρ|={strongest[1]:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# MW-5: shuffled Quran control
# ---------------------------------------------------------------------------
rng = random.Random(SEED)
shuf_H_cond = []
for sid in sids_ordered:
    letters = list(per_surah[sid]["letters"])
    rng.shuffle(letters)
    _, _, Hc_shuf, _, _ = bigram_and_unigram_H("".join(letters))
    shuf_H_cond.append(Hc_shuf)
mean_shuf = statistics.mean(shuf_H_cond)
mean_q = statistics.mean(q_Hcond)
mw5_delta = mean_shuf - mean_q
mw5_pass = mw5_delta >= 0.1
print(f"\nMW-5: mean shuffled H_cond = {mean_shuf:.4f}, unshuffled = {mean_q:.4f}, Δ = {mw5_delta:+.4f} bits ({'PASS' if mw5_pass else 'FAIL'})",
      file=sys.stderr)

# ---------------------------------------------------------------------------
# Decisions (Bonferroni k=2, α_bon=0.025)
# ---------------------------------------------------------------------------
primary_pass = p_welch < 0.025
secondary_pass = p_muq < 0.025
if mw5_pass and primary_pass and secondary_pass:
    verdict = "PASS"
elif not mw5_pass:
    verdict = "INSTRUMENT-BROKEN"
elif primary_pass or secondary_pass:
    verdict = "PARTIAL"
else:
    verdict = "NULL"

# ---------------------------------------------------------------------------
# Write per-surah CSV
# ---------------------------------------------------------------------------
with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow([
        "sid", "name", "type", "n_verses", "n_letters", "n_bigrams",
        "H_unigram", "H_joint", "H_cond", "residual_H_cond",
    ])
    for sid in sids_ordered:
        d = per_surah[sid]
        w.writerow([
            d["sid"], d["name"], d["type"], d["n_verses"],
            d["n_letters"], d["n_bigrams"],
            f"{d['H_unigram']:.6f}", f"{d['H_joint']:.6f}",
            f"{d['H_cond']:.6f}", f"{d['residual_H_cond']:.6f}",
        ])
print(f"\nWrote {OUT_CSV}", file=sys.stderr)

with open(OUT_BUK_CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["rank", "n_letters", "n_bigrams", "H_unigram", "H_joint", "H_cond"])
    for r in buk_records:
        w.writerow([r["rank"], r["n_letters"], r["n_bigrams"],
                    f"{r['H_unigram']:.6f}", f"{r['H_joint']:.6f}", f"{r['H_cond']:.6f}"])
print(f"Wrote {OUT_BUK_CSV}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Assemble summary
# ---------------------------------------------------------------------------
def rf(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: rf(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [rf(v, n) for v in o]
    return o

summary = {
    "finding_id": "h-new-195",
    "title": "Per-surah letter-bigram entropy — Quran vs Bukhārī, muq-residual, correlates",
    "pre_reg_sha256": prereg_sha,
    "seed": SEED,
    "date": "2026-04-17",
    "rules_tuple": "(no-tashkeel, raw Arabic letters U+0621..U+064A, cross-verse bigrams, Hafs-Kūfan, Bukhārī top-114 longest bab-segments)",
    "bonferroni_k": 2,
    "alpha_bonferroni": 0.025,
    "corpus_stats": {
        "quran_n_letters": sum(d["n_letters"] for d in per_surah.values()),
        "quran_mean_H_cond": mean_q,
        "quran_sd_H_cond": statistics.stdev(q_Hcond),
        "quran_min_H_cond": min(q_Hcond),
        "quran_max_H_cond": max(q_Hcond),
        "bukhari_n_segments_total": len(buk_letter_segs),
        "bukhari_n_segments_used": 114,
        "bukhari_min_seg_letters": len(buk_top114[-1]),
        "bukhari_max_seg_letters": len(buk_top114[0]),
        "bukhari_mean_H_cond": mb,
        "bukhari_sd_H_cond": statistics.stdev(b_Hcond),
    },
    "length_regression": {
        "slope": slope,
        "intercept": intercept,
        "r2": r2,
        "formula": "H_cond = intercept + slope * log10(N_bigrams)",
    },
    "top5_lowest_H_cond_raw": fmt_surah_list(bot5_raw),
    "top5_highest_H_cond_raw": fmt_surah_list(top5_raw),
    "top5_lowest_residual": fmt_surah_list(bot5_resid),
    "top5_highest_residual": fmt_surah_list(top5_resid),
    "primary_quran_vs_bukhari": {
        "quran_mean": ma,
        "bukhari_mean": mb,
        "delta": ma - mb,
        "welch_t": t_stat,
        "welch_df": df,
        "p_welch_twosided": p_welch,
        "pass_alpha_bon_025": primary_pass,
        "mwu_z": z_mwu,
        "p_mwu_twosided": p_mwu,
        "paired_wilcoxon_z_length_sorted": z_wil,
        "p_paired_wilcoxon_twosided": p_wil,
    },
    "secondary_muq_vs_nonmuq_residual": {
        "mean_muq": mean_muq,
        "mean_nonmuq": mean_nonmuq,
        "delta": mean_muq - mean_nonmuq,
        "n_muq": len(muq_res),
        "n_nonmuq": len(nonmuq_res),
        "mwu_z": z_muq,
        "p_mwu_twosided": p_muq,
        "pass_alpha_bon_025": secondary_pass,
    },
    "descriptive_correlations": correlations,
    "strongest_continuous_correlate": {
        "covariate": strongest[0],
        "abs_rho": strongest[1],
    },
    "mw5_shuffle_control": {
        "mean_shuffled_H_cond": mean_shuf,
        "mean_unshuffled_H_cond": mean_q,
        "delta_shuf_minus_unshuf": mw5_delta,
        "threshold_bits": 0.1,
        "pass": mw5_pass,
    },
    "verdict": verdict,
}

summary = rf(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote {OUT_JSON}", file=sys.stderr)

print("\n" + "=" * 70, file=sys.stderr)
print(f"PRIMARY Quran vs Bukhārī: Δ={ma-mb:+.4f} bits, Welch p={p_welch:.6f}  "
      f"({'PASS' if primary_pass else 'FAIL'})", file=sys.stderr)
print(f"SECONDARY muq vs non-muq residual: Δ={mean_muq-mean_nonmuq:+.4f}, MWU p={p_muq:.6f}  "
      f"({'PASS' if secondary_pass else 'FAIL'})", file=sys.stderr)
print(f"MW-5 shuffle control: {'PASS' if mw5_pass else 'FAIL'} (Δ={mw5_delta:+.4f} bits)", file=sys.stderr)
print(f"VERDICT: {verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)
