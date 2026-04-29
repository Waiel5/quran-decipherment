#!/usr/bin/env python3
"""H-NEW-187 — Per-surah Lempel-Ziv-76 complexity vs H-NEW-15 gzip + correlations.

Pre-reg: findings/phase-b-hypotheses/h-new-187-lempel-ziv-prereg.md
Seed: 20260419, Bonferroni k=2.

Primary tests:
  P1: Spearman ρ(LZ_norm, gzip_ratio) ≥ +0.7 with p < 0.025.
  P2: Mann-Whitney U(Quran LZ_norm, Bukhārī matched-chunk LZ_norm) p < 0.025.

Secondary: Spearman(LZ_norm, β), Spearman(LZ_norm, α), Spearman(LZ_norm, dispersion),
           Muq vs non-muq Welch t, MW-5 synthetic.
"""
from __future__ import annotations

import csv
import gzip
import json
import math
import random
import re
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
CORPUS = ROOT / "quran-text" / "quran-no-tashkeel.json"
BUKHARI = ROOT / "data" / "baseline-corpora" / "raw" / "bukhari-noquran.txt"
OUT_DIR = ROOT / "findings" / "phase-b-hypotheses"
OUT_CSV = OUT_DIR / "csv" / "h-new-187-per-surah.csv"
OUT_JSON = OUT_DIR / "csv" / "h-new-187.json"

SEED = 20260419
random.seed(SEED)

# ---------- LZ76 (standard Lempel-Ziv 1976 complexity) ----------

def lz76_complexity(s: str) -> int:
    """Standard LZ76 phrase count. Each new parsed phrase is the shortest
    substring not seen in the prefix-plus-current-character history.
    """
    n = len(s)
    if n == 0:
        return 0
    i = 0  # end of current "dictionary" region
    c = 1  # phrase count
    k = 1  # current phrase length
    l = 1  # start of new phrase under exploration
    k_max = 1
    stop = False
    while not stop:
        if s[i + k - 1] != s[l + k - 1]:
            if k > k_max:
                k_max = k
            i += 1
            if i == l:
                c += 1
                l += k_max
                if l + 1 > n:
                    stop = True
                else:
                    i = 0
                    k = 1
                    k_max = 1
            else:
                k = 1
        else:
            k += 1
            if l + k > n:
                c += 1
                stop = True
    return c


def lz_metrics(s: str) -> dict:
    n = max(len(s), 1)
    c = lz76_complexity(s)
    return {
        "length": len(s),
        "lz_count": c,
        "lz_norm_simple": c / n,                       # phrases per char
        "lz_norm_log": c * math.log2(max(n, 2)) / n,   # standard LZ76 norm
    }


# ---------- Stat helpers (pure Python) ----------

def spearman_rho(x: list[float], y: list[float]) -> tuple[float, float]:
    """Spearman rho and two-sided p-value approximation (t-distribution, df=n-2)."""
    n = len(x)
    assert n == len(y) and n >= 3
    rx = rank(x)
    ry = rank(y)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    denx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    deny = math.sqrt(sum((a - my) ** 2 for a in ry))
    rho = num / (denx * deny) if denx * deny > 0 else 0.0
    # t-statistic approximation; p from Student-t CDF
    if abs(rho) >= 1.0:
        p = 0.0
    else:
        t = rho * math.sqrt((n - 2) / max(1 - rho * rho, 1e-18))
        p = 2 * (1 - student_t_cdf(abs(t), n - 2))
    return rho, p


def rank(xs: list[float]) -> list[float]:
    """Average ranks (1-based), handle ties."""
    paired = sorted(enumerate(xs), key=lambda p: p[1])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(paired):
        j = i
        while j + 1 < len(paired) and paired[j + 1][1] == paired[i][1]:
            j += 1
        avg = (i + j) / 2.0 + 1  # 1-based average
        for k in range(i, j + 1):
            ranks[paired[k][0]] = avg
        i = j + 1
    return ranks


def student_t_cdf(t: float, df: int) -> float:
    """Approximate two-sided t-distribution CDF at t (t>=0)."""
    # Abramowitz & Stegun 26.7.8 approximation via incomplete-beta
    x = df / (df + t * t)
    return 1 - 0.5 * regularized_beta(x, df / 2.0, 0.5)


def regularized_beta(x: float, a: float, b: float) -> float:
    """Regularized incomplete beta function via continued fraction."""
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    lbeta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    front = math.exp(a * math.log(x) + b * math.log(1 - x) - lbeta) / a
    if x < (a + 1) / (a + b + 2):
        return front * betacf(a, b, x)
    return 1 - front * betacf(b, a, 1 - x) * a / b if False else 1 - regularized_beta_complement(x, a, b)


def regularized_beta_complement(x: float, a: float, b: float) -> float:
    # Symmetry: I(x; a, b) = 1 - I(1-x; b, a)
    lbeta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    front = math.exp(b * math.log(1 - x) + a * math.log(x) - lbeta) / b
    return front * betacf(b, a, 1 - x)


def betacf(a: float, b: float, x: float) -> float:
    """Continued fraction for incomplete beta. Numerical Recipes."""
    MAXIT = 200
    EPS = 3e-15
    FPMIN = 1e-300
    qab = a + b
    qap = a + 1
    qam = a - 1
    c = 1.0
    d = 1 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1 / d
        delta = d * c
        h *= delta
        if abs(delta - 1) < EPS:
            break
    return h


def welch_t(x: list[float], y: list[float]) -> tuple[float, float]:
    nx, ny = len(x), len(y)
    mx, my = sum(x) / nx, sum(y) / ny
    vx = sum((a - mx) ** 2 for a in x) / (nx - 1) if nx > 1 else 0.0
    vy = sum((a - my) ** 2 for a in y) / (ny - 1) if ny > 1 else 0.0
    se = math.sqrt(vx / nx + vy / ny) if vx + vy > 0 else 1e-18
    t = (mx - my) / se
    # Welch-Satterthwaite df
    num = (vx / nx + vy / ny) ** 2
    den = (vx / nx) ** 2 / max(nx - 1, 1) + (vy / ny) ** 2 / max(ny - 1, 1)
    df = num / den if den > 0 else 1
    p = 2 * (1 - student_t_cdf(abs(t), int(round(df))))
    return t, p


def mannwhitney_u(x: list[float], y: list[float]) -> tuple[float, float]:
    """Mann-Whitney U; normal approximation two-sided p."""
    nx, ny = len(x), len(y)
    combined = [(v, 0) for v in x] + [(v, 1) for v in y]
    ranks = rank([v for v, _ in combined])
    rx = sum(r for r, (_, g) in zip(ranks, combined) if g == 0)
    ux = rx - nx * (nx + 1) / 2
    mu = nx * ny / 2
    sigma = math.sqrt(nx * ny * (nx + ny + 1) / 12)
    z = (ux - mu) / sigma if sigma > 0 else 0.0
    # two-sided via normal approximation
    p = 2 * (1 - norm_cdf(abs(z)))
    return ux, p


def norm_cdf(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


# ---------- Load Quran ----------

with open(CORPUS, encoding="utf-8") as f:
    quran = json.load(f)

surah_texts: dict[int, str] = {}
surah_meta: dict[int, dict] = {}
for s in quran:
    sid = s["id"]
    full = " ".join(v["text"] for v in s["verses"])
    full = re.sub(r"\s+", " ", full).strip()
    surah_texts[sid] = full
    surah_meta[sid] = {"name": s["transliteration"], "type": s["type"], "n_verses": s["total_verses"]}

# ---------- Per-surah LZ + gzip ----------

print(f"[H-NEW-187] Computing LZ76 + gzip for 114 surahs...", file=sys.stderr)
per_surah: list[dict] = []
for sid in range(1, 115):
    t = surah_texts[sid]
    lz = lz_metrics(t)
    raw = t.encode("utf-8")
    gz = gzip.compress(raw, compresslevel=9)
    per_surah.append({
        "surah": sid,
        "name": surah_meta[sid]["name"],
        "type": surah_meta[sid]["type"],
        "n_verses": surah_meta[sid]["n_verses"],
        "n_chars": lz["length"],
        "lz_count": lz["lz_count"],
        "lz_norm_simple": lz["lz_norm_simple"],
        "lz_norm_log": lz["lz_norm_log"],
        "gzip_ratio": len(gz) / max(len(raw), 1),
    })

# ---------- Join with existing per-surah metrics ----------

# Heap β: we need to compute or find file. Try file first.
heap_path = OUT_DIR / "csv" / "h-new-159-heap-per-surah.csv"
heap_by_sid: dict[int, float] = {}
if heap_path.exists():
    with open(heap_path) as f:
        for row in csv.DictReader(f):
            try:
                heap_by_sid[int(row.get("sid") or row.get("surah"))] = float(row.get("beta") or row.get("heap_beta"))
            except Exception:
                pass

# If heap file doesn't exist, compute Heap β per surah inline (log-log regression on cumulative
# distinct-tokens vs tokens)
if not heap_by_sid:
    print(f"[H-NEW-187] Computing Heap β per surah inline...", file=sys.stderr)
    PUNCT = re.compile(r"[^\u0600-\u06FF\s]")
    for sid in range(1, 115):
        t = PUNCT.sub(" ", surah_texts[sid])
        toks = t.split()
        if len(toks) < 20:
            continue
        seen = set()
        xs, ys = [], []
        for i, tok in enumerate(toks, 1):
            seen.add(tok)
            if i >= 5 and (i % max(1, len(toks) // 20) == 0 or i == len(toks)):
                xs.append(math.log(i))
                ys.append(math.log(len(seen)))
        if len(xs) < 3:
            continue
        mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
        num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
        den = sum((a - mx) ** 2 for a in xs)
        beta = num / den if den > 0 else float("nan")
        heap_by_sid[sid] = beta

# Zipf α
zipf_by_sid: dict[int, float] = {}
zf = OUT_DIR / "csv" / "zipf-per-surah.csv"
if zf.exists():
    with open(zf) as f:
        for row in csv.DictReader(f):
            if row.get("zipf_alpha") and row.get("status") == "ok":
                zipf_by_sid[int(row["mushaf_order"])] = float(row["zipf_alpha"])

# Dispersion (rank-based — higher rank_by_dispersion in file, where rank=1 means most dispersed)
disp_by_sid: dict[int, float] = {}
df = OUT_DIR / "csv" / "h-new-168-per-surah-dispersion.csv"
if df.exists():
    with open(df) as f:
        for row in csv.DictReader(f):
            disp_by_sid[int(row["sid"])] = float(row["dispersion"])

# Attach to per_surah rows
for m in per_surah:
    m["heap_beta"] = heap_by_sid.get(m["surah"], float("nan"))
    m["zipf_alpha"] = zipf_by_sid.get(m["surah"], float("nan"))
    m["dispersion"] = disp_by_sid.get(m["surah"], float("nan"))
    m["is_muq"] = 1 if m["surah"] in {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68} else 0

# ---------- P1: Correlations ----------

def pair(metric_key: str) -> tuple[list[float], list[float]]:
    xs, ys = [], []
    for m in per_surah:
        if not math.isnan(m[metric_key]):
            xs.append(m["lz_norm_simple"])
            ys.append(m[metric_key])
    return xs, ys

corr = {}
for key in ("gzip_ratio", "heap_beta", "zipf_alpha", "dispersion"):
    xs, ys = pair(key)
    if len(xs) >= 3:
        rho, p = spearman_rho(xs, ys)
        corr[key] = {"n": len(xs), "rho": rho, "p": p}
    else:
        corr[key] = {"n": len(xs), "rho": None, "p": None}

# ---------- P2: Quran vs Bukhārī length-matched chunks ----------

print(f"[H-NEW-187] Loading Bukhārī + computing matched chunks...", file=sys.stderr)
with open(BUKHARI, encoding="utf-8") as f:
    bukhari_raw = f.read()
# Normalize whitespace consistent with surah texts
bukhari_norm = re.sub(r"\s+", " ", bukhari_raw).strip()
B_LEN = len(bukhari_norm)

# Length-matched sampling: seed 20260419, for each surah draw contiguous chunk same length
rng = random.Random(SEED)
bukhari_lz_list: list[float] = []
bukhari_rows = []
for m in per_surah:
    L = m["n_chars"]
    if L >= B_LEN:
        # Truncate to Bukhārī length
        chunk = bukhari_norm[:L]
    else:
        start = rng.randint(0, B_LEN - L)
        chunk = bukhari_norm[start:start + L]
    lm = lz_metrics(chunk)
    bukhari_lz_list.append(lm["lz_norm_simple"])
    bukhari_rows.append({"surah": m["surah"], "n_chars": L, "lz_norm_simple": lm["lz_norm_simple"]})

quran_lz_list = [m["lz_norm_simple"] for m in per_surah]
mw_u, mw_p = mannwhitney_u(quran_lz_list, bukhari_lz_list)

# ---------- Secondary: Muq vs non-muq ----------

muq_lz = [m["lz_norm_simple"] for m in per_surah if m["is_muq"]]
nm_lz = [m["lz_norm_simple"] for m in per_surah if not m["is_muq"]]
muq_t, muq_p = welch_t(muq_lz, nm_lz)

# ---------- MW-5 sanity check ----------

# Random string
ALPH = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"  # 28 Arabic letters
rng2 = random.Random(SEED)
rand_str = "".join(rng2.choice(ALPH) for _ in range(10000))
# Repeating pattern
rep_str = ("ابت" * (10000 // 3 + 1))[:10000]

rand_lz = lz_metrics(rand_str)
rep_lz = lz_metrics(rep_str)

# ---------- Decision ----------

ALPHA_BON = 0.025
p1_pass = (corr["gzip_ratio"]["rho"] is not None and
           corr["gzip_ratio"]["rho"] >= 0.7 and
           corr["gzip_ratio"]["p"] < ALPHA_BON)
p2_pass = mw_p < ALPHA_BON
mw5_pass = rand_lz["lz_norm_simple"] >= 10 * rep_lz["lz_norm_simple"]

# ---------- Save CSV ----------

OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
fields = ["surah", "name", "type", "n_verses", "n_chars",
          "lz_count", "lz_norm_simple", "lz_norm_log", "gzip_ratio",
          "heap_beta", "zipf_alpha", "dispersion", "is_muq"]
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for m in per_surah:
        w.writerow({k: m[k] for k in fields})

# ---------- Save JSON ----------

results = {
    "id": "H-NEW-187",
    "seed": SEED,
    "bonferroni_k_primary": 2,
    "alpha_bon_primary": ALPHA_BON,
    "n_surahs": 114,
    "correlations_with_lz_norm_simple": corr,
    "quran_vs_bukhari": {
        "n_quran": len(quran_lz_list),
        "n_bukhari_matched": len(bukhari_lz_list),
        "quran_mean": sum(quran_lz_list) / len(quran_lz_list),
        "bukhari_mean": sum(bukhari_lz_list) / len(bukhari_lz_list),
        "mann_whitney_u": mw_u,
        "p_two_sided": mw_p,
    },
    "muq_vs_nonmuq": {
        "n_muq": len(muq_lz),
        "n_nonmuq": len(nm_lz),
        "muq_mean": sum(muq_lz) / len(muq_lz),
        "nonmuq_mean": sum(nm_lz) / len(nm_lz),
        "welch_t": muq_t,
        "p": muq_p,
    },
    "mw5_sanity": {
        "random_lz_norm_simple": rand_lz["lz_norm_simple"],
        "repeating_lz_norm_simple": rep_lz["lz_norm_simple"],
        "ratio": rand_lz["lz_norm_simple"] / max(rep_lz["lz_norm_simple"], 1e-18),
        "pass": mw5_pass,
    },
    "decision": {
        "p1_pass": p1_pass,
        "p2_pass": p2_pass,
        "mw5_pass": mw5_pass,
    },
    "top10_lowest_lz_norm": [
        {"surah": m["surah"], "name": m["name"], "type": m["type"],
         "lz_norm_simple": m["lz_norm_simple"], "gzip_ratio": m["gzip_ratio"],
         "n_chars": m["n_chars"]}
        for m in sorted(per_surah, key=lambda x: x["lz_norm_simple"])[:10]
    ],
    "top10_highest_lz_norm": [
        {"surah": m["surah"], "name": m["name"], "type": m["type"],
         "lz_norm_simple": m["lz_norm_simple"], "gzip_ratio": m["gzip_ratio"],
         "n_chars": m["n_chars"]}
        for m in sorted(per_surah, key=lambda x: -x["lz_norm_simple"])[:10]
    ],
}

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# ---------- Print summary ----------

print("\n=== H-NEW-187 — LEMPEL-ZIV COMPLEXITY PER SURAH ===")
print(f"Seed: {SEED}, Bonferroni k=2, α_primary={ALPHA_BON}")
print()
print("--- CORRELATIONS (Spearman ρ) — LZ_norm_simple vs ... ---")
for k, v in corr.items():
    if v["rho"] is None:
        print(f"  vs {k:<12}: insufficient data (n={v['n']})")
    else:
        mark = " *BON" if v["p"] < ALPHA_BON else ""
        print(f"  vs {k:<12}: ρ={v['rho']:+.4f}  p={v['p']:.4e}  n={v['n']}{mark}")
print()
print("--- P1: LZ vs gzip ---")
print(f"  PASS? {p1_pass}  (requires ρ>=+0.7 AND p<{ALPHA_BON})")
print()
print("--- P2: Quran vs Bukhārī matched chunks ---")
print(f"  Quran   mean LZ_norm: {results['quran_vs_bukhari']['quran_mean']:.6f}")
print(f"  Bukhārī mean LZ_norm: {results['quran_vs_bukhari']['bukhari_mean']:.6f}")
print(f"  Mann-Whitney U = {mw_u:.1f}, p = {mw_p:.4e}")
print(f"  PASS? {p2_pass}")
print()
print("--- MW-5 sanity ---")
print(f"  Random  LZ_norm: {rand_lz['lz_norm_simple']:.4f}")
print(f"  Repeat  LZ_norm: {rep_lz['lz_norm_simple']:.4f}")
print(f"  Ratio = {rand_lz['lz_norm_simple']/max(rep_lz['lz_norm_simple'],1e-18):.1f}×  PASS? {mw5_pass}")
print()
print("--- Muq vs non-muq ---")
print(f"  Muq   mean LZ_norm: {results['muq_vs_nonmuq']['muq_mean']:.6f}  (n={len(muq_lz)})")
print(f"  NonMq mean LZ_norm: {results['muq_vs_nonmuq']['nonmuq_mean']:.6f}  (n={len(nm_lz)})")
print(f"  Welch t = {muq_t:+.3f}, p = {muq_p:.4e}")
print()
print("--- TOP 10 LOWEST LZ_norm (most compressible / repetitive) ---")
for m in sorted(per_surah, key=lambda x: x["lz_norm_simple"])[:10]:
    print(f"  Q{m['surah']:>3} {m['name']:<20} {m['type']:<8} "
          f"LZ={m['lz_norm_simple']:.4f}  gzip={m['gzip_ratio']:.4f}  chars={m['n_chars']}")
print()
print("--- TOP 10 HIGHEST LZ_norm (most complex / least repetitive) ---")
for m in sorted(per_surah, key=lambda x: -x["lz_norm_simple"])[:10]:
    print(f"  Q{m['surah']:>3} {m['name']:<20} {m['type']:<8} "
          f"LZ={m['lz_norm_simple']:.4f}  gzip={m['gzip_ratio']:.4f}  chars={m['n_chars']}")
print()
print(f"CSV:  {OUT_CSV}")
print(f"JSON: {OUT_JSON}")
