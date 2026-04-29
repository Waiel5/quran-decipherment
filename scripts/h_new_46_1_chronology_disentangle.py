"""H-NEW-46.1 — Disentangle muqaṭṭaʿāt-vs-length from Meccan/Medinan chronology.

Pre-reg: findings/phase-b-hypotheses/h-new-46-1-chronology-disentangle-prereg.md

Question: does muqaṭṭaʿāt presence still predict surah length AFTER controlling
for Meccan-vs-Medinan revelation period?

Chronology source LOCKED before computation:
  Tanzil Egyptian Standard (data/revelation-order.csv 'period' column).
  Aligns with al-Suyūṭī al-Itqān nawʿ 9 standard 86 Meccan / 28 Medinan split.

Seed: 20260416
Bonferroni k = 7, α_bon = 0.05/7 ≈ 0.007143
N_PERM = 100,000 (where applicable)

7 test cells:
  A1 — Mean verse-count, Meccan stratum (one-sided upper)
  A2 — Top-K representation, Meccan stratum (one-sided upper)
  B1 — Mean verse-count, Medinan stratum (one-sided upper, exact enum)
  B2 — Top-K representation, Medinan stratum (one-sided upper, exact)
  C1 — Stratified Mann-Whitney by period (van Elteren, two-sided)
  C2 — OLS coefficient on muq indicator after period control (t-test + HC1)
  C3 — Permutation residualized null (MW-1 equivalent, one-sided upper)

+ MW-5 positive control on cells A1 and B1.
+ MW-7 internal-error gate.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import random
import statistics
import sys
import time
from itertools import combinations
from typing import Dict, List, Tuple

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))

from tools.loader import load_quran  # noqa: E402

SEED = 20260416
N_PERM = 100_000
BON_K = 7
ALPHA_BON = 0.05 / BON_K
N_SURAHS = 114

# Locked muqaṭṭaʿāt-opened set (matches H-NEW-46)
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
              36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
assert len(MUQ_SURAHS) == 29


def load_verse_counts() -> List[int]:
    """Return list of 114 verse counts indexed by surah_id - 1."""
    surahs = load_quran("no-tashkeel")
    assert len(surahs) == N_SURAHS
    counts = [0] * N_SURAHS
    for s in surahs:
        counts[s.id - 1] = len(s.verses)
    assert counts[1] == 286, f"expected Q 2 to have 286 verses, got {counts[1]}"
    return counts


def load_chronology() -> Dict[int, str]:
    """Return mapping surah_id -> 'Meccan' or 'Medinan' from Tanzil/Egyptian std."""
    path = os.path.join(REPO, "data/revelation-order.csv")
    out: Dict[int, str] = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            sid = int(row["mushaf_order"])
            period = row["period"].strip()
            assert period in ("Meccan", "Medinan"), f"bad period: {period}"
            out[sid] = period
    assert len(out) == N_SURAHS
    return out


def empirical_p(obs: float, null_list: List[float], direction: str) -> dict:
    n = len(null_list)
    as_or_more_upper = sum(1 for x in null_list if x >= obs) + 1
    as_or_more_lower = sum(1 for x in null_list if x <= obs) + 1
    p_upper = as_or_more_upper / (n + 1)
    p_lower = as_or_more_lower / (n + 1)
    mu = sum(null_list) / n
    sd = (sum((x - mu) ** 2 for x in null_list) / n) ** 0.5
    base = {"null_mean": mu, "null_std": sd, "p_upper": p_upper, "p_lower": p_lower}
    if direction == "upper":
        base["p"] = p_upper
    elif direction == "lower":
        base["p"] = p_lower
    elif direction == "two_sided":
        base["p"] = min(1.0, 2 * min(p_upper, p_lower))
    else:
        raise ValueError(direction)
    return base


def cell_A1_mecca_mean(muq_mecc: List[int], non_muq_mecc: List[int],
                       verse_counts: List[int], rng: random.Random) -> dict:
    """Mean verse-count of muq-Meccan vs random K-from-86 within Meccan."""
    all_mecc = muq_mecc + non_muq_mecc
    K = len(muq_mecc)
    obs_mean = statistics.fmean(verse_counts[s - 1] for s in muq_mecc)
    null_means = []
    for _ in range(N_PERM):
        S = rng.sample(all_mecc, K)
        null_means.append(statistics.fmean(verse_counts[s - 1] for s in S))
    res = empirical_p(obs_mean, null_means, "upper")
    res["observed"] = obs_mean
    res["K"] = K
    res["n_pool"] = len(all_mecc)
    return res


def cell_A2_mecca_topK(muq_mecc: List[int], non_muq_mecc: List[int],
                       verse_counts: List[int], rng: random.Random) -> dict:
    """How many of the K=26 muq-Meccan are in the top-K longest Meccan surahs?"""
    all_mecc = muq_mecc + non_muq_mecc
    K = len(muq_mecc)
    sorted_mecc = sorted(all_mecc, key=lambda i: (-verse_counts[i - 1], i))
    topK = set(sorted_mecc[:K])
    obs = sum(1 for s in muq_mecc if s in topK)
    null_counts = []
    for _ in range(N_PERM):
        S = rng.sample(all_mecc, K)
        null_counts.append(sum(1 for s in S if s in topK))
    res = empirical_p(obs, null_counts, "upper")
    res["observed"] = obs
    res["K"] = K
    res["topK_set"] = sorted(topK)
    return res


def cell_B1_medina_mean_exact(muq_medi: List[int], non_muq_medi: List[int],
                              verse_counts: List[int]) -> dict:
    """Mean verse-count of muq-Medinan vs ALL combinations 3-from-28 (exact)."""
    all_medi = muq_medi + non_muq_medi
    K = len(muq_medi)
    obs_mean = statistics.fmean(verse_counts[s - 1] for s in muq_medi)
    null_means = []
    for combo in combinations(all_medi, K):
        null_means.append(statistics.fmean(verse_counts[s - 1] for s in combo))
    n_total = len(null_means)
    n_ge = sum(1 for x in null_means if x >= obs_mean)
    p = n_ge / n_total  # exact, no +1 padding
    mu = sum(null_means) / n_total
    sd = (sum((x - mu) ** 2 for x in null_means) / n_total) ** 0.5
    return {"observed": obs_mean, "null_mean": mu, "null_std": sd,
            "K": K, "n_pool": len(all_medi), "n_combinations": n_total,
            "p_upper": p, "p_lower": 1 - p, "p": p}


def cell_B2_medina_topK_exact(muq_medi: List[int], non_muq_medi: List[int],
                              verse_counts: List[int]) -> dict:
    """How many of the K=3 muq-Medinan are in the top-K longest Medinan surahs?"""
    all_medi = muq_medi + non_muq_medi
    K = len(muq_medi)
    sorted_medi = sorted(all_medi, key=lambda i: (-verse_counts[i - 1], i))
    topK = set(sorted_medi[:K])
    obs = sum(1 for s in muq_medi if s in topK)
    null_counts = []
    for combo in combinations(all_medi, K):
        null_counts.append(sum(1 for s in combo if s in topK))
    n_total = len(null_counts)
    n_ge = sum(1 for x in null_counts if x >= obs)
    p = n_ge / n_total
    mu = sum(null_counts) / n_total
    sd = (sum((x - mu) ** 2 for x in null_counts) / n_total) ** 0.5
    return {"observed": obs, "null_mean": mu, "null_std": sd,
            "K": K, "n_pool": len(all_medi), "n_combinations": n_total,
            "topK_set": sorted(topK),
            "p_upper": p, "p_lower": 1 - p, "p": p}


def mw_u_stat(group_a: List[float], group_b: List[float]) -> Tuple[float, float, float]:
    """Return (U_a, mean_a, mean_b). U_a = sum_{a in A} #{b in B : b<a} + 0.5*#{b in B : b==a}."""
    U = 0.0
    for a in group_a:
        U += sum(1 for b in group_b if b < a) + 0.5 * sum(1 for b in group_b if b == a)
    return U, sum(group_a) / len(group_a), sum(group_b) / len(group_b)


def cell_C1_stratified_mw(muq_mecc: List[int], non_muq_mecc: List[int],
                          muq_medi: List[int], non_muq_medi: List[int],
                          verse_counts: List[int], rng: random.Random) -> dict:
    """van Elteren stratified Mann-Whitney across two strata.

    Within each stratum compute U_observed, then combined-z via van Elteren formula.
    Two-sided p reported analytically AND by permutation cross-check.
    """
    strata = []
    for muq, non_muq, name in [(muq_mecc, non_muq_mecc, "Meccan"),
                                (muq_medi, non_muq_medi, "Medinan")]:
        a = [verse_counts[s - 1] for s in muq]
        b = [verse_counts[s - 1] for s in non_muq]
        n1, n2 = len(a), len(b)
        N = n1 + n2
        U, mean_a, mean_b = mw_u_stat(a, b)
        # mean and variance of U under H0 (no ties for now; ties handled below)
        mu_U = n1 * n2 / 2.0
        # tie-corrected variance
        from collections import Counter
        all_vals = a + b
        tie_terms = sum(t * (t * t - 1) for t in Counter(all_vals).values() if t > 1)
        var_U = (n1 * n2 / 12.0) * ((N + 1) - tie_terms / (N * (N - 1)))
        strata.append({
            "name": name, "n1": n1, "n2": n2, "N": N,
            "U": U, "mu_U": mu_U, "var_U": var_U,
            "mean_muq": mean_a, "mean_non_muq": mean_b,
        })

    # van Elteren: combined z = sum (U_i - mu_i) / sqrt(sum var_i)
    # weights = 1 (equal-stratum); also report inverse-variance weighting
    sum_diff = sum(s["U"] - s["mu_U"] for s in strata)
    sum_var = sum(s["var_U"] for s in strata)
    z_combined = sum_diff / math.sqrt(sum_var)
    # two-sided p
    p_two_sided = 2 * (1 - 0.5 * (1 + math.erf(abs(z_combined) / math.sqrt(2))))

    # permutation cross-check: within each stratum, randomly relabel muq vs non-muq
    rng_perm = random.Random(SEED + 4242)
    perm_diffs = []
    for _ in range(N_PERM):
        diff = 0.0
        for s in strata:
            pool_size = s["n1"] + s["n2"]
            # we need to re-build the pool of values for this stratum
            # but we don't carry it in s; rebuild from input
            pass
        # rebuild more cleanly below
        break
    # actually do the permutation properly
    perm_diffs = []
    pools = []
    for muq, non_muq in [(muq_mecc, non_muq_mecc), (muq_medi, non_muq_medi)]:
        vals = [verse_counts[s - 1] for s in muq + non_muq]
        n1 = len(muq)
        pools.append((vals, n1))
    for _ in range(N_PERM):
        diff = 0.0
        for vals, n1 in pools:
            shuffled = vals[:]
            rng_perm.shuffle(shuffled)
            a = shuffled[:n1]
            b = shuffled[n1:]
            n2 = len(b)
            U, _, _ = mw_u_stat(a, b)
            mu_U = n1 * n2 / 2.0
            diff += (U - mu_U)
        perm_diffs.append(diff)
    n_extreme = sum(1 for x in perm_diffs if abs(x) >= abs(sum_diff))
    p_perm = (n_extreme + 1) / (N_PERM + 1)

    return {
        "strata": strata,
        "sum_diff_obs": sum_diff,
        "sum_var": sum_var,
        "z_combined": z_combined,
        "p_analytic_two_sided": p_two_sided,
        "p_perm_two_sided": p_perm,
        "p": max(p_two_sided, p_perm),  # headline = more conservative
    }


def cell_C2_ols(period: Dict[int, str], verse_counts: List[int]) -> dict:
    """OLS: verse_count = b0 + b1 * I(Medinan) + b2 * I(muqaṭṭaʿāt) + e

    Pure-Python OLS (no numpy dependency in this script). Closed-form via normal equations.
    Reports both classical-t p and HC1 robust SE p.
    """
    # Build design matrix and y
    surah_ids = list(range(1, N_SURAHS + 1))
    n = len(surah_ids)
    X = []
    y = []
    for sid in surah_ids:
        x_int = 1.0
        x_med = 1.0 if period[sid] == "Medinan" else 0.0
        x_muq = 1.0 if sid in MUQ_SURAHS else 0.0
        X.append([x_int, x_med, x_muq])
        y.append(float(verse_counts[sid - 1]))

    # Compute X'X (3x3) and X'y (3,)
    p = 3
    XtX = [[0.0] * p for _ in range(p)]
    Xty = [0.0] * p
    for i in range(n):
        for j in range(p):
            for k in range(p):
                XtX[j][k] += X[i][j] * X[i][k]
            Xty[j] += X[i][j] * y[i]

    # Invert XtX (3x3 via cofactor)
    def inv3(m):
        a, b, c = m[0]
        d, e, f = m[1]
        g, h, i = m[2]
        det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
        inv = [
            [(e*i - f*h)/det, -(b*i - c*h)/det,  (b*f - c*e)/det],
            [-(d*i - f*g)/det, (a*i - c*g)/det, -(a*f - c*d)/det],
            [(d*h - e*g)/det, -(a*h - b*g)/det,  (a*e - b*d)/det],
        ]
        return inv, det

    XtX_inv, det_XtX = inv3(XtX)
    # beta = XtX_inv @ Xty
    beta = [sum(XtX_inv[j][k] * Xty[k] for k in range(p)) for j in range(p)]
    # residuals
    yhat = [sum(X[i][j] * beta[j] for j in range(p)) for i in range(n)]
    resid = [y[i] - yhat[i] for i in range(n)]
    rss = sum(r * r for r in resid)
    sigma2_classical = rss / (n - p)
    # classical Var(beta) = sigma2 * XtX_inv
    se_classical = [math.sqrt(sigma2_classical * XtX_inv[j][j]) for j in range(p)]
    # HC1 robust: Var(beta) = (n/(n-p)) * XtX_inv @ X'diag(e^2)X @ XtX_inv
    # build X'diag(e^2)X
    XeX = [[0.0] * p for _ in range(p)]
    for i in range(n):
        e2 = resid[i] * resid[i]
        for j in range(p):
            for k in range(p):
                XeX[j][k] += X[i][j] * e2 * X[i][k]
    # bread @ meat @ bread
    middle = [[sum(XtX_inv[j][k] * XeX[k][m] for k in range(p)) for m in range(p)]
              for j in range(p)]
    sandwich = [[sum(middle[j][k] * XtX_inv[k][m] for k in range(p)) for m in range(p)]
                for j in range(p)]
    hc1_factor = n / (n - p)
    var_robust = [hc1_factor * sandwich[j][j] for j in range(p)]
    se_robust = [math.sqrt(v) for v in var_robust]
    # t-stat for each coef; df = n - p
    df = n - p
    # two-sided p-value via t-distribution; use scipy-free approximation
    def t_two_sided_p(t, df):
        # use Student's t cdf via incomplete beta — pure python via continued fraction.
        # For df=111 we can approximate with normal (df > 30 normal is fine).
        # For more accuracy: use survival function for t.
        # We'll just use the normal approximation since df=111.
        z = abs(t)
        return 2 * (1 - 0.5 * (1 + math.erf(z / math.sqrt(2))))

    t_classical = [beta[j] / se_classical[j] for j in range(p)]
    t_robust = [beta[j] / se_robust[j] for j in range(p)]
    p_classical = [t_two_sided_p(t, df) for t in t_classical]
    p_robust = [t_two_sided_p(t, df) for t in t_robust]

    coef_names = ["intercept", "I(Medinan)", "I(muqattaat)"]
    results = {}
    for j in range(p):
        results[coef_names[j]] = {
            "beta": beta[j],
            "se_classical": se_classical[j],
            "t_classical": t_classical[j],
            "p_classical": p_classical[j],
            "se_robust_HC1": se_robust[j],
            "t_robust_HC1": t_robust[j],
            "p_robust_HC1": p_robust[j],
        }
    # headline: muq coefficient, conservative p = max of classical / HC1
    muq_coef = beta[2]
    muq_p_headline = max(p_classical[2], p_robust[2])
    return {
        "n": n,
        "df": df,
        "coefficients": results,
        "muq_coef": muq_coef,
        "muq_p_headline": muq_p_headline,
        "p": muq_p_headline,
        "rss": rss,
        "r_squared": 1 - rss / sum((y[i] - sum(y) / n) ** 2 for i in range(n)),
    }


def cell_C3_residualized_perm(period: Dict[int, str], verse_counts: List[int],
                              rng: random.Random) -> dict:
    """Residualize length on period (subtract within-period mean), then test
    mean-residual for muq vs non-muq via uniform 29-from-114 permutation null.
    One-sided upper.
    """
    # within-period mean
    mecc_lens = [verse_counts[s - 1] for s in range(1, N_SURAHS + 1) if period[s] == "Meccan"]
    medi_lens = [verse_counts[s - 1] for s in range(1, N_SURAHS + 1) if period[s] == "Medinan"]
    mu_mecc = sum(mecc_lens) / len(mecc_lens)
    mu_medi = sum(medi_lens) / len(medi_lens)
    resid = [0.0] * N_SURAHS
    for sid in range(1, N_SURAHS + 1):
        if period[sid] == "Meccan":
            resid[sid - 1] = verse_counts[sid - 1] - mu_mecc
        else:
            resid[sid - 1] = verse_counts[sid - 1] - mu_medi
    obs = statistics.fmean(resid[s - 1] for s in MUQ_SURAHS)
    all_surahs = list(range(1, N_SURAHS + 1))
    null_means = []
    for _ in range(N_PERM):
        S = rng.sample(all_surahs, len(MUQ_SURAHS))
        null_means.append(statistics.fmean(resid[s - 1] for s in S))
    res = empirical_p(obs, null_means, "upper")
    res["observed_mean_resid"] = obs
    res["mu_mecc"] = mu_mecc
    res["mu_medi"] = mu_medi
    res["observed"] = obs
    return res


def mw5_positive_control_A1(non_muq_mecc: List[int], all_mecc: List[int],
                             verse_counts: List[int]) -> dict:
    """Plant the 26 LONGEST Meccan surahs as fake-muq; cell A1 should give p < 1e-4."""
    K = 26
    sorted_mecc = sorted(all_mecc, key=lambda i: (-verse_counts[i - 1], i))
    planted = sorted_mecc[:K]
    planted_mean = statistics.fmean(verse_counts[s - 1] for s in planted)
    rng = random.Random(SEED + 99)
    null_means = []
    for _ in range(10_000):
        S = rng.sample(all_mecc, K)
        null_means.append(statistics.fmean(verse_counts[s - 1] for s in S))
    p = (sum(1 for x in null_means if x >= planted_mean) + 1) / (10_001)
    return {"planted_mean_len_A1": planted_mean,
            "p_pc_A1": p,
            "detect_lt_1e_minus_3": p < 1e-3}


def mw5_positive_control_B1(all_medi: List[int], verse_counts: List[int]) -> dict:
    """Plant the 3 LONGEST Medinan surahs as fake-muq-Medinan; cell B1 should
    give p = 1/3276 ≈ 3.05e-4 (combinatorial floor: there's exactly one
    'three longest' combination)."""
    K = 3
    sorted_medi = sorted(all_medi, key=lambda i: (-verse_counts[i - 1], i))
    planted = sorted_medi[:K]
    planted_mean = statistics.fmean(verse_counts[s - 1] for s in planted)
    null_means = []
    for combo in combinations(all_medi, K):
        null_means.append(statistics.fmean(verse_counts[s - 1] for s in combo))
    n_total = len(null_means)
    n_ge = sum(1 for x in null_means if x >= planted_mean)
    p = n_ge / n_total
    return {"planted_mean_len_B1": planted_mean,
            "p_pc_B1": p,
            "n_combinations": n_total,
            "detect_at_floor": p <= 1.0 / n_total + 1e-12}


def mw7_internal_error_gate(muq_mecc: List[int], muq_medi: List[int],
                            verse_counts: List[int]) -> dict:
    """Manual recompute of muq-Meccan and muq-Medinan means, error if mismatch."""
    mecc_vals = [verse_counts[s - 1] for s in muq_mecc]
    medi_vals = [verse_counts[s - 1] for s in muq_medi]
    mecc_mean = sum(mecc_vals) / len(mecc_vals)
    medi_mean = sum(medi_vals) / len(medi_vals)
    return {
        "muq_mecc_mean_manual": mecc_mean,
        "muq_medi_mean_manual": medi_mean,
        "muq_mecc_lens": mecc_vals,
        "muq_medi_lens": medi_vals,
        "muq_mecc_count": len(mecc_vals),
        "muq_medi_count": len(medi_vals),
        "ok": (len(mecc_vals) + len(medi_vals)) == 29,
    }


def main():
    print("[H-NEW-46.1] loading data ...")
    verse_counts = load_verse_counts()
    period = load_chronology()

    # split surahs by period
    all_mecc = [s for s in range(1, N_SURAHS + 1) if period[s] == "Meccan"]
    all_medi = [s for s in range(1, N_SURAHS + 1) if period[s] == "Medinan"]
    assert len(all_mecc) == 86, f"expected 86 Meccan, got {len(all_mecc)}"
    assert len(all_medi) == 28, f"expected 28 Medinan, got {len(all_medi)}"

    muq_mecc = sorted(s for s in MUQ_SURAHS if period[s] == "Meccan")
    muq_medi = sorted(s for s in MUQ_SURAHS if period[s] == "Medinan")
    non_muq_mecc = sorted(s for s in all_mecc if s not in MUQ_SURAHS)
    non_muq_medi = sorted(s for s in all_medi if s not in MUQ_SURAHS)
    assert len(muq_mecc) == 26 and len(muq_medi) == 3
    assert len(non_muq_mecc) == 60 and len(non_muq_medi) == 25

    print(f"  Meccan: {len(all_mecc)} ({len(muq_mecc)} muq, {len(non_muq_mecc)} non-muq)")
    print(f"  Medinan: {len(all_medi)} ({len(muq_medi)} muq, {len(non_muq_medi)} non-muq)")
    print(f"  muq-Meccan: {muq_mecc}")
    print(f"  muq-Medinan: {muq_medi}")

    print("[H-NEW-46.1] MW-7 internal-error gate ...")
    mw7 = mw7_internal_error_gate(muq_mecc, muq_medi, verse_counts)
    print(f"  muq-Meccan mean = {mw7['muq_mecc_mean_manual']:.3f}  "
          f"(n={mw7['muq_mecc_count']})")
    print(f"  muq-Medinan mean = {mw7['muq_medi_mean_manual']:.3f}  "
          f"(n={mw7['muq_medi_count']})")
    if not mw7["ok"]:
        print("  ERROR: total muq != 29")
        sys.exit(1)

    print("[H-NEW-46.1] MW-5 positive controls ...")
    pc_A1 = mw5_positive_control_A1(non_muq_mecc, all_mecc, verse_counts)
    pc_B1 = mw5_positive_control_B1(all_medi, verse_counts)
    print(f"  PC-A1 planted-mean={pc_A1['planted_mean_len_A1']:.2f}  p={pc_A1['p_pc_A1']:.6f}  "
          f"detect<1e-3={pc_A1['detect_lt_1e_minus_3']}")
    print(f"  PC-B1 planted-mean={pc_B1['planted_mean_len_B1']:.2f}  p={pc_B1['p_pc_B1']:.6f}  "
          f"at-floor={pc_B1['detect_at_floor']}")

    print("[H-NEW-46.1] cell A1 — Meccan-stratum mean ...")
    rng_a1 = random.Random(SEED)
    A1 = cell_A1_mecca_mean(muq_mecc, non_muq_mecc, verse_counts, rng_a1)
    print(f"  obs={A1['observed']:.2f}  null_mean={A1['null_mean']:.2f}  "
          f"null_std={A1['null_std']:.2f}  p={A1['p']:.6f}")

    print("[H-NEW-46.1] cell A2 — Meccan-stratum top-K count ...")
    rng_a2 = random.Random(SEED + 1)
    A2 = cell_A2_mecca_topK(muq_mecc, non_muq_mecc, verse_counts, rng_a2)
    print(f"  obs={A2['observed']}/{A2['K']}  null_mean={A2['null_mean']:.2f}  "
          f"null_std={A2['null_std']:.2f}  p={A2['p']:.6f}")

    print("[H-NEW-46.1] cell B1 — Medinan-stratum mean (exact enumeration) ...")
    B1 = cell_B1_medina_mean_exact(muq_medi, non_muq_medi, verse_counts)
    print(f"  obs={B1['observed']:.2f}  null_mean={B1['null_mean']:.2f}  "
          f"null_std={B1['null_std']:.2f}  p={B1['p']:.6f}  "
          f"({B1['n_combinations']} combos)")

    print("[H-NEW-46.1] cell B2 — Medinan-stratum top-K count (exact) ...")
    B2 = cell_B2_medina_topK_exact(muq_medi, non_muq_medi, verse_counts)
    print(f"  obs={B2['observed']}/{B2['K']}  null_mean={B2['null_mean']:.2f}  "
          f"null_std={B2['null_std']:.2f}  p={B2['p']:.6f}")

    print("[H-NEW-46.1] cell C1 — stratified Mann-Whitney (van Elteren) ...")
    rng_c1 = random.Random(SEED + 2)
    C1 = cell_C1_stratified_mw(muq_mecc, non_muq_mecc, muq_medi, non_muq_medi,
                                verse_counts, rng_c1)
    print(f"  z_combined={C1['z_combined']:.3f}  "
          f"p_analytic={C1['p_analytic_two_sided']:.6f}  "
          f"p_perm={C1['p_perm_two_sided']:.6f}  headline_p={C1['p']:.6f}")

    print("[H-NEW-46.1] cell C2 — OLS verse_count ~ Medinan + muqaṭṭaʿāt ...")
    C2 = cell_C2_ols(period, verse_counts)
    print(f"  beta_muq={C2['muq_coef']:.3f}  p_classical={C2['coefficients']['I(muqattaat)']['p_classical']:.6f}  "
          f"p_HC1={C2['coefficients']['I(muqattaat)']['p_robust_HC1']:.6f}  "
          f"headline_p={C2['p']:.6f}  R^2={C2['r_squared']:.4f}")

    print("[H-NEW-46.1] cell C3 — period-residualized 29-from-114 perm null ...")
    rng_c3 = random.Random(SEED + 3)
    C3 = cell_C3_residualized_perm(period, verse_counts, rng_c3)
    print(f"  obs_mean_resid={C3['observed_mean_resid']:.3f}  "
          f"null_mean={C3['null_mean']:.3f}  null_std={C3['null_std']:.3f}  "
          f"p={C3['p']:.6f}")

    cells = {
        "A1_mecca_mean": A1,
        "A2_mecca_topK": A2,
        "B1_medina_mean_exact": B1,
        "B2_medina_topK_exact": B2,
        "C1_stratified_mw": C1,
        "C2_ols": C2,
        "C3_residualized_perm": C3,
    }
    sig = {k: (v["p"] < ALPHA_BON) for k, v in cells.items()}
    n_sig = sum(sig.values())

    # Verdict
    muq_coef_pos_and_sig = (C2["muq_coef"] > 0 and
                            C2["coefficients"]["I(muqattaat)"]["p_classical"] < ALPHA_BON)
    if not pc_A1["detect_lt_1e_minus_3"] or not pc_B1["detect_at_floor"]:
        verdict = "NULL-BROKEN"
    elif n_sig == 0:
        verdict = "NULL"
    elif n_sig in (1, 2):
        verdict = "EXPLORATORY"
    elif n_sig in (3, 4, 5):
        verdict = "PARTIAL-PASS" if C2["muq_coef"] > 0 else "PARTIAL-PASS-MIXED-SIGN"
    elif n_sig in (6, 7):
        if muq_coef_pos_and_sig:
            verdict = "STRONG-PASS"
        else:
            verdict = "STRONG-PASS-COEF-CAVEAT"
    else:
        verdict = "UNDEFINED"

    # SHA of pre-reg
    preg_path = os.path.join(REPO, "findings/phase-b-hypotheses/"
                             "h-new-46-1-chronology-disentangle-prereg.md")
    with open(preg_path, "rb") as f:
        preg_sha = hashlib.sha256(f.read()).hexdigest()

    out = {
        "hypothesis_id": "H-NEW-46.1",
        "parent_finding": "H-NEW-46",
        "run_date": "2026-04-15",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_family": "2026-04-16-Wave-Muqattaat-Extended-Disentangle",
        "bonferroni_k": BON_K,
        "alpha_bon": ALPHA_BON,
        "chronology_source": "Tanzil Egyptian Standard period field "
                             "(aligns with al-Suyūṭī al-Itqān nawʿ 9 standard 86/28)",
        "chronology_file": "data/revelation-order.csv",
        "prereg_sha256": preg_sha,
        "muq_surahs_locked": sorted(MUQ_SURAHS),
        "muq_mecc": muq_mecc,
        "muq_medi": muq_medi,
        "non_muq_mecc": non_muq_mecc,
        "non_muq_medi": non_muq_medi,
        "n_meccan": len(all_mecc),
        "n_medinan": len(all_medi),
        "mw7_internal_gate": mw7,
        "mw5_positive_controls": {"A1": pc_A1, "B1": pc_B1},
        "cells": cells,
        "significant_at_alpha_bon": sig,
        "n_significant": n_sig,
        "muq_coef": C2["muq_coef"],
        "muq_coef_p_classical": C2["coefficients"]["I(muqattaat)"]["p_classical"],
        "muq_coef_p_HC1": C2["coefficients"]["I(muqattaat)"]["p_robust_HC1"],
        "verdict": verdict,
    }

    out_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-46-1.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[H-NEW-46.1] wrote {out_path}")
    print(f"[H-NEW-46.1] VERDICT: {verdict}  (n_sig={n_sig}/7)")
    print(f"[H-NEW-46.1] OLS muq coef = {C2['muq_coef']:.3f} verses  "
          f"(p_classical={C2['coefficients']['I(muqattaat)']['p_classical']:.6f}, "
          f"p_HC1={C2['coefficients']['I(muqattaat)']['p_robust_HC1']:.6f})")
    for k in cells:
        print(f"  {k}: p={cells[k]['p']:.6f}  sig={sig[k]}")


if __name__ == "__main__":
    main()
