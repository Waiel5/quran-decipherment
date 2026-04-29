#!/usr/bin/env python3
"""H-NEW-172 — Per-surah Zipf law exponent α: Quran vs Bukhārī bab segments.

Complement to H-NEW-123/H-NEW-159 (Heap's-law β). Zipf's law is the
rank-frequency counterpart: f(r) ~ r^(-α). We fit α per-surah (all 114
surahs; min-token threshold 50) and per-Bukhārī bab-segment (114 longest
babs from H-NEW-147 segmentation).

Rules tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)

Pre-registered, Bonferroni k=3 at family alpha=0.05:
  P1 (primary) : mean α_Quran differs from mean α_Bukhārī (Welch's t)
  P2 (primary) : variance α_Quran differs from variance α_Bukhārī
                 (Levene-style absolute-deviation-from-median test)
  S1 (secondary): α_s correlates (Spearman) with at least one of:
                 muq-status, Meccan/Medinan, log-length, H-NEW-163 dispersion
                 (sub-Bonferroni within the 4 axes)

MW-5 (method working): synthetic Zipfian corpus with α_true=1.0
generated via inverse-sampling; fitted α should be within ±0.1 of 1.0.

Seed: 20260419
"""
from __future__ import annotations

import json
import math
import random
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path("/Users/grey/Downloads/quran")
sys.path.insert(0, str(ROOT))

from analysis.tools.loader import load_quran  # noqa: E402

SEED = 20260419
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-172.json"
OUT_CSV = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-172-per-surah.csv"
OUT_BAB_CSV = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-172-per-bab.csv"

BUKHARI_TXT = ROOT / "data" / "baseline-corpora" / "raw" / "bukhari-noquran.txt"
REVELATION_CSV = ROOT / "data" / "revelation-order.csv"

# ---------------------------------------------------------------------------
# Tokenization (same rules as H-NEW-123)
# ---------------------------------------------------------------------------
ARABIC_LETTERS = set()
for cp in range(0x0621, 0x064B):
    ARABIC_LETTERS.add(chr(cp))
for cp in range(0x0671, 0x06D4):
    ARABIC_LETTERS.add(chr(cp))

REC_MARKS = set(chr(c) for c in range(0x06D6, 0x06EE))
TASHKEEL = set(chr(c) for c in range(0x064B, 0x0660))
TASHKEEL |= {chr(0x0670), chr(0x0640)}


def normalize(s: str) -> str:
    out = []
    for ch in s:
        if ch in TASHKEEL or ch in REC_MARKS:
            continue
        if ch in ARABIC_LETTERS:
            out.append(ch)
        else:
            out.append(" ")
    s = "".join(out)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def tokenize(s: str) -> List[str]:
    return [t for t in normalize(s).split() if t]


# ---------------------------------------------------------------------------
# Zipf α fit: f(r) = K * r^(-α). log f vs log r OLS slope = -α.
# ---------------------------------------------------------------------------
def fit_zipf_alpha(tokens: List[str]) -> Tuple[float, float, int, int, int]:
    """Return (alpha, r2, N_tokens, V_types, n_fit_points)."""
    if not tokens:
        return float("nan"), float("nan"), 0, 0, 0
    freqs = Counter(tokens)
    sorted_counts = sorted(freqs.values(), reverse=True)
    # Exclude hapax tail that breaks log-log fit power-law;
    # convention: fit on ranks where f >= 2 (drop hapaxes)
    # This keeps the fit on the heavy head + middle.
    xs, ys = [], []
    for r, f in enumerate(sorted_counts, start=1):
        if f < 2:
            break
        xs.append(math.log(r))
        ys.append(math.log(f))
    n = len(xs)
    if n < 3:
        # fallback: include hapaxes if too few non-hapax ranks
        xs = [math.log(r) for r, _ in enumerate(sorted_counts, start=1)]
        ys = [math.log(f) for _, f in enumerate(sorted_counts)]
        n = len(xs)
        if n < 3:
            return float("nan"), float("nan"), len(tokens), len(freqs), n
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    slope = num / den if den > 0 else float("nan")
    alpha = -slope if not math.isnan(slope) else float("nan")
    # R²
    intercept = my - slope * mx if not math.isnan(slope) else float("nan")
    if math.isnan(slope):
        r2 = float("nan")
    else:
        ss_tot = sum((y - my) ** 2 for y in ys)
        ss_res = sum((ys[i] - (slope * xs[i] + intercept)) ** 2 for i in range(n))
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return alpha, r2, len(tokens), len(freqs), n


# ---------------------------------------------------------------------------
# MW-5: synthetic Zipfian positive control
# ---------------------------------------------------------------------------
def mw5_synthetic_zipf(alpha_true: float = 1.0, N: int = 10000, V: int = 1000,
                       seed: int = SEED) -> Tuple[float, float]:
    """Generate ~N tokens via inverse-CDF sampling from a Zipf(α_true) distribution
    on V types, fit α, return (alpha_hat, r2)."""
    rng = random.Random(seed)
    # Weights ∝ r^(-α), r=1..V
    weights = [1.0 / (r ** alpha_true) for r in range(1, V + 1)]
    total = sum(weights)
    cum = []
    s = 0.0
    for w in weights:
        s += w / total
        cum.append(s)
    toks: List[str] = []
    for _ in range(N):
        u = rng.random()
        # binary search
        lo, hi = 0, V - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if cum[mid] < u:
                lo = mid + 1
            else:
                hi = mid
        toks.append(f"w{lo + 1}")
    alpha_hat, r2, _, _, _ = fit_zipf_alpha(toks)
    return alpha_hat, r2


# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------
MUQATTAAT_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
                    31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}


def load_quran_by_surah() -> Dict[int, List[str]]:
    surahs = load_quran("no-tashkeel")
    out: Dict[int, List[str]] = {}
    for s in surahs:
        toks: List[str] = []
        for v in sorted(s.verses, key=lambda x: x.id):
            toks.extend(tokenize(v.text))
        out[s.id] = toks
    return out


def load_bukhari_babs() -> List[List[str]]:
    """Split Bukhārī at 'باب' markers, take 114 longest segments (H-NEW-147 method)."""
    text = BUKHARI_TXT.read_text(encoding="utf-8", errors="replace")
    # Strip diacritics/marks same way as Quran normalization
    text = "".join(ch for ch in text if ch not in TASHKEEL and ch not in REC_MARKS)
    segments = re.split(r"\bباب\b", text)
    seg_tokens = [tokenize(s) for s in segments if s.strip()]
    seg_tokens = [t for t in seg_tokens if len(t) >= 50]
    seg_tokens.sort(key=len, reverse=True)
    return seg_tokens[:114]


def load_revelation_periods() -> Dict[int, str]:
    """Return {surah_id: 'Meccan' or 'Medinan'}."""
    out: Dict[int, str] = {}
    with REVELATION_CSV.open(encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        mi = header.index("mushaf_order")
        pi = header.index("period")
        for line in f:
            parts = line.strip().split(",")
            if len(parts) > max(mi, pi):
                try:
                    sid = int(parts[mi])
                    out[sid] = parts[pi]
                except ValueError:
                    continue
    return out


# ---------------------------------------------------------------------------
# Dispersion: compute stem-dispersion per surah (H-NEW-163-like, rough stemmer)
# ---------------------------------------------------------------------------
STRIP_PREFIXES = ["ال", "وال", "بال", "فال", "كال", "لل", "و", "ف", "ل", "ب", "ك", "س"]
STRIP_SUFFIXES = ["ون", "ين", "ان", "ات", "ها", "هم", "هن", "كم", "كن", "نا", "تم",
                  "تن", "ة", "ه", "ي", "ا", "ت", "ن"]


def light_stem(token: str) -> str:
    t = token
    if len(t) < 3:
        return t
    for p in sorted(STRIP_PREFIXES, key=lambda x: -len(x)):
        if len(t) > len(p) + 2 and t.startswith(p):
            t = t[len(p):]
            break
    for s in sorted(STRIP_SUFFIXES, key=lambda x: -len(x)):
        if len(t) > len(s) + 2 and t.endswith(s):
            t = t[:-len(s)]
            break
    return t


def compute_dispersion(by_surah: Dict[int, List[str]]) -> Dict[int, float]:
    """For each surah, fraction of OTHER 113 surahs containing each of its stems,
    averaged across its stems."""
    stems_by_surah = {sid: set(light_stem(t) for t in toks) for sid, toks in by_surah.items()}
    all_sids = sorted(stems_by_surah.keys())
    out: Dict[int, float] = {}
    for sid in all_sids:
        stems = stems_by_surah[sid]
        if not stems:
            out[sid] = float("nan")
            continue
        scores = []
        others = [o for o in all_sids if o != sid]
        for st in stems:
            cnt = sum(1 for o in others if st in stems_by_surah[o])
            scores.append(cnt / len(others))
        out[sid] = sum(scores) / len(scores) if scores else float("nan")
    return out


# ---------------------------------------------------------------------------
# Statistics (no scipy)
# ---------------------------------------------------------------------------
def mean_var(xs: List[float]) -> Tuple[float, float]:
    n = len(xs)
    if n == 0:
        return float("nan"), float("nan")
    m = sum(xs) / n
    v = sum((x - m) ** 2 for x in xs) / (n - 1) if n > 1 else float("nan")
    return m, v


def welch_t(a: List[float], b: List[float]) -> Tuple[float, float, float]:
    """Return (t-stat, df, p-value two-sided). p approximated via normal CDF for df>30."""
    ma, va = mean_var(a)
    mb, vb = mean_var(b)
    na, nb = len(a), len(b)
    se = math.sqrt(va / na + vb / nb)
    t = (ma - mb) / se if se > 0 else float("nan")
    df = (va / na + vb / nb) ** 2 / ((va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1))
    # Large-df normal approx
    z = abs(t)
    p = 2 * (1 - _phi(z))
    return t, df, p


def _phi(z: float) -> float:
    """Standard normal CDF via erf."""
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def levene_median(a: List[float], b: List[float]) -> Tuple[float, float]:
    """Brown-Forsythe (Levene with median): test equality of variances.
    Returns (F-stat, p-value). Large-sample approx via F-distribution."""
    def med(xs):
        xs_s = sorted(xs)
        n = len(xs_s)
        return (xs_s[n // 2] if n % 2 == 1 else 0.5 * (xs_s[n // 2 - 1] + xs_s[n // 2]))

    med_a = med(a)
    med_b = med(b)
    z_a = [abs(x - med_a) for x in a]
    z_b = [abs(x - med_b) for x in b]
    # Welch's t on |deviations| → use that p
    t, df, p = welch_t(z_a, z_b)
    return t, p


def spearman_rho(xs: List[float], ys: List[float]) -> Tuple[float, float]:
    """Rank-correlation; p from t-approximation. NaN-pairs dropped."""
    pairs = [(x, y) for x, y in zip(xs, ys) if not (math.isnan(x) or math.isnan(y))]
    n = len(pairs)
    if n < 4:
        return float("nan"), float("nan")

    def ranks(vs):
        sv = sorted(enumerate(vs), key=lambda p: p[1])
        rks = [0.0] * len(vs)
        i = 0
        while i < len(sv):
            j = i
            while j + 1 < len(sv) and sv[j + 1][1] == sv[i][1]:
                j += 1
            avg = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                rks[sv[k][0]] = avg
            i = j + 1
        return rks

    xr = ranks([p[0] for p in pairs])
    yr = ranks([p[1] for p in pairs])
    mx = sum(xr) / n
    my = sum(yr) / n
    num = sum((xr[i] - mx) * (yr[i] - my) for i in range(n))
    den_x = math.sqrt(sum((r - mx) ** 2 for r in xr))
    den_y = math.sqrt(sum((r - my) ** 2 for r in yr))
    if den_x == 0 or den_y == 0:
        return float("nan"), float("nan")
    rho = num / (den_x * den_y)
    # t-approx
    t = rho * math.sqrt((n - 2) / max(1e-12, 1 - rho * rho)) if abs(rho) < 1 else float("inf")
    z = abs(t)
    p = 2 * (1 - _phi(z))
    return rho, p


def point_biserial(binary: List[int], cont: List[float]) -> Tuple[float, float]:
    """Point-biserial for binary predictor (0/1). Equivalent to Welch's t effect."""
    a = [cont[i] for i in range(len(binary)) if binary[i] == 1 and not math.isnan(cont[i])]
    b = [cont[i] for i in range(len(binary)) if binary[i] == 0 and not math.isnan(cont[i])]
    if len(a) < 3 or len(b) < 3:
        return float("nan"), float("nan")
    t, df, p = welch_t(a, b)
    # Cohen's d
    ma, va = mean_var(a)
    mb, vb = mean_var(b)
    pooled_sd = math.sqrt((va + vb) / 2)
    d = (ma - mb) / pooled_sd if pooled_sd > 0 else float("nan")
    return d, p


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 70)
    print("H-NEW-172 — Per-chapter Zipf α: Quran vs Bukhārī")
    print("=" * 70)
    print(f"Seed: {SEED}")

    # MW-5
    print("\n[MW-5] Synthetic Zipfian corpus, α_true=1.0 ...")
    alpha_hat, r2_syn = mw5_synthetic_zipf(alpha_true=1.0, N=10000, V=1000, seed=SEED)
    mw5_pass = abs(alpha_hat - 1.0) < 0.1
    print(f"  α_hat = {alpha_hat:.4f} (r² = {r2_syn:.4f}) — MW-5 pass: {mw5_pass}")

    # Also check α=0.8 and α=1.3
    alpha_hat_08, _ = mw5_synthetic_zipf(alpha_true=0.8, N=10000, V=1000, seed=SEED + 1)
    alpha_hat_13, _ = mw5_synthetic_zipf(alpha_true=1.3, N=10000, V=1000, seed=SEED + 2)
    print(f"  (aux) α_true=0.8 → α_hat={alpha_hat_08:.4f}")
    print(f"  (aux) α_true=1.3 → α_hat={alpha_hat_13:.4f}")

    # Load corpora
    print("\n[Load] Quran 114 surahs ...")
    q_by_surah = load_quran_by_surah()
    print(f"  Loaded {len(q_by_surah)} surahs")

    print("[Load] Bukhārī 114 longest bab-segments ...")
    bukh_babs = load_bukhari_babs()
    print(f"  Loaded {len(bukh_babs)} bab-segments "
          f"(total tokens: {sum(len(b) for b in bukh_babs):,})")

    print("[Load] Revelation periods ...")
    periods = load_revelation_periods()
    print(f"  Loaded periods for {len(periods)} surahs")

    # Per-surah Zipf α
    print("\n[Fit] Per-surah α ...")
    surah_rows = []
    for sid in sorted(q_by_surah.keys()):
        toks = q_by_surah[sid]
        if len(toks) < 50:
            continue  # skip too-short
        alpha, r2, N, V, n_pts = fit_zipf_alpha(toks)
        surah_rows.append({
            "surah_id": sid,
            "N": N,
            "V": V,
            "alpha": alpha,
            "r2": r2,
            "n_fit_points": n_pts,
            "is_muq": sid in MUQATTAAT_SURAHS,
            "period": periods.get(sid, "Unknown"),
        })
    print(f"  {len(surah_rows)} surahs with N≥50")
    alphas_q = [r["alpha"] for r in surah_rows if not math.isnan(r["alpha"])]
    mean_q, var_q = mean_var(alphas_q)
    print(f"  mean α_Quran = {mean_q:.4f}, SD = {math.sqrt(var_q):.4f}, "
          f"range = [{min(alphas_q):.3f}, {max(alphas_q):.3f}]")

    # Per-bab Zipf α
    print("\n[Fit] Per-bab α ...")
    bab_rows = []
    for i, toks in enumerate(bukh_babs, start=1):
        alpha, r2, N, V, n_pts = fit_zipf_alpha(toks)
        bab_rows.append({
            "bab_id": i,
            "N": N,
            "V": V,
            "alpha": alpha,
            "r2": r2,
            "n_fit_points": n_pts,
        })
    alphas_b = [r["alpha"] for r in bab_rows if not math.isnan(r["alpha"])]
    mean_b, var_b = mean_var(alphas_b)
    print(f"  {len(bab_rows)} bab-segments")
    print(f"  mean α_Bukhārī = {mean_b:.4f}, SD = {math.sqrt(var_b):.4f}, "
          f"range = [{min(alphas_b):.3f}, {max(alphas_b):.3f}]")

    # --- Primary P1: Welch's t on means ---
    print("\n[Primary P1] Welch's t — mean α Quran vs Bukhārī ...")
    t_stat, df, p_means = welch_t(alphas_q, alphas_b)
    print(f"  t = {t_stat:+.4f}, df ≈ {df:.1f}, p = {p_means:.4e}")

    # --- Primary P2: Levene(Brown-Forsythe) on variance ---
    print("\n[Primary P2] Brown-Forsythe on variances ...")
    t_lev, p_vars = levene_median(alphas_q, alphas_b)
    print(f"  |dev| t-stat = {t_lev:+.4f}, p = {p_vars:.4e}")

    # Bonferroni-3
    alpha_bon_primary = 0.05 / 3
    print(f"\n[Bonferroni] α_family = 0.05, k=3 → α_bon = {alpha_bon_primary:.4f}")
    p1_pass = p_means < alpha_bon_primary
    p2_pass = p_vars < alpha_bon_primary
    print(f"  P1 (means differ):   p={p_means:.4e}  pass={p1_pass}")
    print(f"  P2 (variances differ): p={p_vars:.4e}  pass={p2_pass}")

    # --- Secondary S1: correlate α_s with 4 axes ---
    print("\n[Secondary S1] Correlates of α_s ...")
    # Dispersion (H-NEW-163 style, all 114)
    print("  Computing H-NEW-163-style dispersion for all surahs ...")
    dispersion = compute_dispersion(q_by_surah)

    # Build aligned vectors
    sids = [r["surah_id"] for r in surah_rows]
    alphas_vec = [r["alpha"] for r in surah_rows]
    is_muq_vec = [1 if r["is_muq"] else 0 for r in surah_rows]
    is_medinan = [1 if r["period"] == "Medinan" else 0 for r in surah_rows]
    logN_vec = [math.log(r["N"]) for r in surah_rows]
    disp_vec = [dispersion.get(r["surah_id"], float("nan")) for r in surah_rows]

    d_muq, p_muq = point_biserial(is_muq_vec, alphas_vec)
    d_med, p_med = point_biserial(is_medinan, alphas_vec)
    rho_len, p_len = spearman_rho(logN_vec, alphas_vec)
    rho_disp, p_disp = spearman_rho(disp_vec, alphas_vec)

    print(f"  muq-status        : Cohen's d={d_muq:+.3f}  p={p_muq:.4e}")
    print(f"  Medinan (1) vs Meccan (0): d={d_med:+.3f}  p={p_med:.4e}")
    print(f"  log(N) tokens     : ρ={rho_len:+.4f}  p={p_len:.4e}")
    print(f"  H-NEW-163 dispersion : ρ={rho_disp:+.4f}  p={p_disp:.4e}")

    alpha_bon_secondary = alpha_bon_primary / 4  # sub-Bonferroni 4 axes
    print(f"  sub-Bon α = {alpha_bon_secondary:.5f} (primary α_bon / 4 axes)")
    s1_passes = {
        "muq": p_muq < alpha_bon_secondary,
        "medinan": p_med < alpha_bon_secondary,
        "log_length": p_len < alpha_bon_secondary,
        "dispersion": p_disp < alpha_bon_secondary,
    }
    s1_any = any(s1_passes.values())
    print(f"  S1 any-axis passes: {s1_any}  {s1_passes}")

    # Strongest correlate
    axis_ps = [("muq", p_muq, d_muq),
               ("medinan", p_med, d_med),
               ("log_length", p_len, rho_len),
               ("dispersion", p_disp, rho_disp)]
    axis_ps.sort(key=lambda x: x[1] if not math.isnan(x[1]) else 1.0)
    strongest = axis_ps[0]
    print(f"  Strongest: {strongest[0]} (p={strongest[1]:.4e}, effect={strongest[2]:+.3f})")

    # --- Synthesis with H-NEW-159 ---
    # H-NEW-159 β: Quran mean 0.901 SD 0.067, Bukhārī mean 0.842 SD 0.027.
    # Quran has HIGHER β and 2.5× SD. Expected: similar pattern for α.
    # Correlate α_s with H-NEW-159 β_s? We need β_s per surah; recompute inline.
    print("\n[Synthesis with H-NEW-159] Recomputing Heap's β per surah for correlation ...")
    betas_by_surah = {}
    for sid, toks in q_by_surah.items():
        if len(toks) < 50:
            continue
        seen: set = set()
        ns, vs = [], []
        for i, tok in enumerate(toks, start=1):
            seen.add(tok)
            if i >= 100 and (i - 100) % 50 == 0:
                ns.append(i)
                vs.append(len(seen))
        if ns and ns[-1] != len(toks):
            ns.append(len(toks))
            vs.append(len(seen))
        if len(ns) < 3:
            betas_by_surah[sid] = float("nan")
            continue
        xs = [math.log(n) for n in ns]
        ys = [math.log(v) for v in vs]
        mx = sum(xs) / len(xs)
        my = sum(ys) / len(ys)
        num = sum((xs[i] - mx) * (ys[i] - my) for i in range(len(xs)))
        den = sum((xs[i] - mx) ** 2 for i in range(len(xs)))
        betas_by_surah[sid] = num / den if den > 0 else float("nan")

    betas_vec = [betas_by_surah.get(r["surah_id"], float("nan")) for r in surah_rows]
    rho_ab, p_ab = spearman_rho(alphas_vec, betas_vec)
    print(f"  Spearman ρ(α_s, β_s) = {rho_ab:+.4f}  p={p_ab:.4e}")
    # Interpretation helper
    if not math.isnan(rho_ab):
        if rho_ab < -0.3:
            synth_note = ("α and β are NEGATIVELY correlated: short-tailed surahs "
                          "(low α) grow vocabulary fast (high β). Consistent with "
                          "H-NEW-159 length-driven heterogeneity.")
        elif rho_ab > 0.3:
            synth_note = ("α and β are POSITIVELY correlated: unusual — surahs with "
                          "concentrated vocab (high α) ALSO grow fast. Flag for investigation.")
        else:
            synth_note = ("α and β are decoupled: the two laws capture independent axes "
                          "of per-surah variability.")
    else:
        synth_note = "Correlation undefined."
    print(f"  → {synth_note}")

    # --- Verdict ---
    print("\n[Verdict]")
    if p1_pass and p2_pass:
        verdict = "BOTH PRIMARY PASS — Quran α differs from Bukhārī in BOTH mean AND variance"
    elif p1_pass:
        verdict = "P1 ONLY — means differ, variances do not (after Bonferroni)"
    elif p2_pass:
        verdict = "P2 ONLY — variances differ, means do not (after Bonferroni)"
    else:
        verdict = "NULL — neither primary cell passes after Bonferroni"
    if s1_any:
        verdict += f"; secondary S1 pass on {[k for k,v in s1_passes.items() if v]}"
    else:
        verdict += "; secondary S1 NULL"
    print(f"  {verdict}")

    # Save outputs
    result = {
        "id": "H-NEW-172",
        "title": "Per-surah Zipf α: Quran vs Bukhārī bab-segments",
        "seed": SEED,
        "rules_tuple": ("(no-tashkeel, orthographic-token, graphemes, "
                        "basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)"),
        "bonferroni": {"k_primary": 3, "alpha_family": 0.05,
                       "alpha_bon_primary": alpha_bon_primary,
                       "k_secondary_within": 4,
                       "alpha_bon_secondary": alpha_bon_secondary},
        "mw5": {
            "alpha_true": 1.0, "alpha_hat": alpha_hat, "r2": r2_syn,
            "pass_0.1_tol": mw5_pass,
            "aux_0.8": alpha_hat_08, "aux_1.3": alpha_hat_13,
        },
        "quran": {
            "n_surahs_fit": len(alphas_q),
            "mean_alpha": mean_q, "sd_alpha": math.sqrt(var_q),
            "min_alpha": min(alphas_q), "max_alpha": max(alphas_q),
        },
        "bukhari": {
            "n_babs_fit": len(alphas_b),
            "mean_alpha": mean_b, "sd_alpha": math.sqrt(var_b),
            "min_alpha": min(alphas_b), "max_alpha": max(alphas_b),
        },
        "primary_cells": {
            "P1_means_welch_t": {"t": t_stat, "df": df, "p_two_sided": p_means,
                                 "pass_bonferroni": p1_pass,
                                 "direction": "Quran > Bukhari" if mean_q > mean_b else "Quran < Bukhari"},
            "P2_variances_brown_forsythe": {"t": t_lev, "p_two_sided": p_vars,
                                            "pass_bonferroni": p2_pass,
                                            "direction": "Quran > Bukhari" if var_q > var_b else "Quran < Bukhari"},
        },
        "secondary_s1": {
            "muq": {"cohens_d": d_muq, "p": p_muq, "pass_sub_bon": s1_passes["muq"]},
            "medinan_vs_meccan": {"cohens_d": d_med, "p": p_med,
                                  "pass_sub_bon": s1_passes["medinan"]},
            "log_length_spearman": {"rho": rho_len, "p": p_len,
                                    "pass_sub_bon": s1_passes["log_length"]},
            "dispersion_spearman": {"rho": rho_disp, "p": p_disp,
                                    "pass_sub_bon": s1_passes["dispersion"]},
            "any_pass": s1_any,
            "strongest": {"axis": strongest[0], "p": strongest[1], "effect": strongest[2]},
        },
        "synthesis_h_new_159": {
            "spearman_alpha_beta": rho_ab, "p": p_ab,
            "note": synth_note,
            "recall_h159_quran_mean_beta": 0.901,
            "recall_h159_quran_sd_beta": 0.067,
            "recall_h159_bukh_mean_beta": 0.842,
            "recall_h159_bukh_sd_beta": 0.027,
        },
        "verdict": verdict,
        "per_surah_sample": surah_rows[:20],  # truncate; full goes to CSV
        "per_bab_sample": bab_rows[:20],
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\n[write] {OUT_JSON}")

    # Full CSVs
    with OUT_CSV.open("w", encoding="utf-8") as f:
        f.write("surah_id,N,V,alpha,r2,n_fit_points,is_muq,period,beta_h159,dispersion_h163\n")
        for r in surah_rows:
            sid = r["surah_id"]
            f.write(f"{sid},{r['N']},{r['V']},{r['alpha']:.6f},{r['r2']:.6f},"
                    f"{r['n_fit_points']},{int(r['is_muq'])},{r['period']},"
                    f"{betas_by_surah.get(sid, float('nan')):.6f},"
                    f"{dispersion.get(sid, float('nan')):.6f}\n")
    print(f"[write] {OUT_CSV}")

    with OUT_BAB_CSV.open("w", encoding="utf-8") as f:
        f.write("bab_id,N,V,alpha,r2,n_fit_points\n")
        for r in bab_rows:
            f.write(f"{r['bab_id']},{r['N']},{r['V']},{r['alpha']:.6f},"
                    f"{r['r2']:.6f},{r['n_fit_points']}\n")
    print(f"[write] {OUT_BAB_CSV}")

    print("\nDONE.")


if __name__ == "__main__":
    main()
