#!/usr/bin/env python3
"""H-NEW-930: Modular-arithmetic patterns in verse-count distribution.

PRE-REGISTERED 2026-05-07 by modular-arithmetic-specialist.

H1 (PRIMARY, Bonferroni-4): For each m ∈ {7, 11, 13, 19}, Pearson χ²
goodness-of-fit on residues V_s mod m (s=1..114) against uniform expected
(114/m per residue class). df = m - 1. α_bon = 0.05/4 = 0.0125.

H2 (SECONDARY, descriptive only): For each m where H1 rejects, two-sided
binomial test of count(V ≡ 0 mod m) against null = 1/m. Not in Bonferroni
family.

H4(a) SAFETY: mushaf-permutation null over the 114-multiset. (Mathematically
a no-op for the multiset-invariant χ² statistic — reported for sanity.)

H4(b) SAFETY: pre-Islamic poetry baseline — DATA-GAP if no clean
per-poem-line-count table on disk.

Rules-tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).

Verse-count source: quran-text/quran-no-tashkeel.json (114 surahs, total 6236;
Q1=7, Q2=286, Q108=3 — Hafs-Kūfan numbering verified).
"""
import hashlib
import json
import math
import random
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-930-modular-verse-counts-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-930.json"

EXPECTED_SHA = "93ba966620068d10984923ea63b76aee8a8ec30adaa648da0e718b8ddd0ff390"

SEED = 20260507
N_PERMS_SENS = 10000  # for m=19 multinomial-permutation sensitivity check
N_PERMS_MUSHAF = 10000  # for H4(a) mushaf-permutation sanity check

MODULI = [7, 11, 13, 19]
ALPHA = 0.05
BONFERRONI_K = 4
ALPHA_BON = ALPHA / BONFERRONI_K  # 0.0125


def sha256_file(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


# ---- χ² goodness-of-fit and chi² CDF (no scipy dependency) ----

def chi2_stat(observed, expected):
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))


def lower_incomplete_gamma_regularized(s, x, n_terms=200):
    """Regularized lower incomplete gamma P(s, x) via series expansion.
    For s > 0 and x >= 0. Numerically stable for moderate values.
    """
    if x <= 0:
        return 0.0
    # Use series: P(s,x) = (x^s e^{-x} / Gamma(s+1)) * Σ_{k=0}^∞ x^k / ((s+1)(s+2)...(s+k))
    # Equivalently the standard series for the regularized form.
    term = 1.0 / s
    total = term
    for k in range(1, n_terms):
        term *= x / (s + k)
        total += term
        if abs(term) < 1e-18 * abs(total):
            break
    # multiply by x^s e^{-x} / Gamma(s)
    log_pref = s * math.log(x) - x - math.lgamma(s)
    return math.exp(log_pref) * total


def chi2_sf(stat, df):
    """Survival function (upper-tail p) for chi-squared with df degrees of freedom."""
    if stat <= 0:
        return 1.0
    p = lower_incomplete_gamma_regularized(df / 2.0, stat / 2.0)
    return max(0.0, min(1.0, 1.0 - p))


# ---- Two-sided binomial test (no scipy) ----

def binomial_pmf(n, k, p):
    if k < 0 or k > n:
        return 0.0
    return math.exp(
        math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
        + k * math.log(p) + (n - k) * math.log1p(-p)
    )


def binomial_two_sided_p(n, k, p):
    """Two-sided binomial p-value: sum of pmf over outcomes with pmf <= pmf(k)."""
    p_obs = binomial_pmf(n, k, p)
    total = 0.0
    eps = 1e-12
    for i in range(n + 1):
        pi = binomial_pmf(n, i, p)
        if pi <= p_obs + eps:
            total += pi
    return min(1.0, total)


# ---- Multinomial permutation null for m=19 sensitivity ----

def multinomial_perm_pvalue(observed_counts, n, m, n_perms, seed):
    """Generate n_perms uniform-multinomial samples (n=114, m bins, p=1/m each),
    compute χ² for each, return p = fraction with chi² >= observed."""
    rng = random.Random(seed)
    expected = [n / m] * m
    obs_chi2 = chi2_stat(observed_counts, expected)
    cnt = 0
    for _ in range(n_perms):
        bins = [0] * m
        for _i in range(n):
            bins[rng.randrange(m)] += 1
        if chi2_stat(bins, expected) >= obs_chi2:
            cnt += 1
    return cnt / n_perms, obs_chi2


# ---- Main ----

def main():
    print("=== H-NEW-930 — Modular-arithmetic patterns in verse-count distribution ===")
    print(f"Pre-reg: {PREREG}")
    actual_sha = sha256_file(PREREG)
    print(f"Pre-reg SHA (computed): {actual_sha}")
    print(f"Pre-reg SHA (expected): {EXPECTED_SHA}")
    if actual_sha != EXPECTED_SHA:
        raise SystemExit(
            f"FATAL: pre-reg SHA mismatch — pre-commit violation. "
            f"Got {actual_sha}, expected {EXPECTED_SHA}."
        )
    print("Pre-reg SHA verified OK.")

    # Load verse counts
    with open(QURAN_JSON) as f:
        quran = json.load(f)
    assert len(quran) == 114, f"Expected 114 surahs, got {len(quran)}"
    verse_counts = []
    for s in quran:
        vc = s["total_verses"]
        assert vc == len(s["verses"]), (
            f"Surah {s['id']} total_verses={vc} != len(verses)={len(s['verses'])}"
        )
        verse_counts.append(vc)
    total_verses = sum(verse_counts)
    assert total_verses == 6236, f"Expected 6236 verses, got {total_verses}"
    assert verse_counts[0] == 7, f"Expected Q1=7, got {verse_counts[0]}"
    assert verse_counts[1] == 286, f"Expected Q2=286, got {verse_counts[1]}"
    assert verse_counts[107] == 3, f"Expected Q108=3, got {verse_counts[107]}"
    print(f"Verse-counts loaded: 114 surahs, total {total_verses}, "
          f"min {min(verse_counts)}, max {max(verse_counts)}.")

    n = 114
    results = {
        "id": "H-NEW-930",
        "title": "Modular-arithmetic patterns in verse-count distribution",
        "prereg_sha256": actual_sha,
        "seed": SEED,
        "rules_tuple": (
            "(no-tashkeel, orthographic-token, graphemes, "
            "basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
        ),
        "n_surahs": n,
        "total_verses": total_verses,
        "verse_count_min": min(verse_counts),
        "verse_count_max": max(verse_counts),
        "moduli": MODULI,
        "bonferroni_k": BONFERRONI_K,
        "alpha": ALPHA,
        "alpha_bon": ALPHA_BON,
        "per_modulus": {},
        "family_verdict": None,
        "n_rejects_at_alpha_bon": 0,
        "h2_residue_zero": {},
        "h4a_mushaf_permutation_invariant": True,
        "h4a_note": (
            "χ²(V mod m) depends only on the multiset {V_s}, not on the surah-position "
            "assignment. Mushaf-permutation null is mathematically a no-op for this "
            "statistic. Sanity-check verified empirically below for m=19."
        ),
        "h4b_data_gap": True,
        "h4b_note": (
            "No clean per-poem line-count tabulation on disk in tabular form for "
            "pre-Islamic dīwān corpus. Reported as DATA-GAP."
        ),
    }

    n_rejects = 0
    print()
    print(f"{'m':>3} {'chi2':>10} {'df':>3} {'p_chi2':>12} {'verdict':>20}")
    print("-" * 55)

    for m in MODULI:
        residues = [v % m for v in verse_counts]
        observed = [residues.count(k) for k in range(m)]
        expected = [n / m] * m
        chi2 = chi2_stat(observed, expected)
        df = m - 1
        p = chi2_sf(chi2, df)

        if p < ALPHA_BON:
            verdict = "REJECT-UNIFORM (CONFIRMED)"
            n_rejects += 1
        elif p < ALPHA:
            verdict = "DIRECTIONAL (uncorrected)"
        else:
            verdict = "NULL (uniform-consistent)"

        # Sensitivity: multinomial-perm p for m=19 (per honest-limits §6.2)
        sens = None
        if m == 19:
            sens_p, sens_chi2 = multinomial_perm_pvalue(
                observed, n, m, N_PERMS_SENS, SEED
            )
            sens = {
                "n_perms": N_PERMS_SENS,
                "p_perm": sens_p,
                "chi2_observed_check": sens_chi2,
                "note": (
                    "Multinomial-permutation sensitivity check; expected cell E=6 is "
                    "just above the χ²-asymptotic E≥5 floor."
                ),
            }

        results["per_modulus"][m] = {
            "modulus": m,
            "expected_per_cell": n / m,
            "observed_residue_counts": dict(zip(range(m), observed)),
            "chi2": chi2,
            "df": df,
            "p_chi2": p,
            "verdict": verdict,
            "rejected_at_alpha_bon": p < ALPHA_BON,
            "sensitivity_perm_check": sens,
        }
        print(f"{m:>3} {chi2:>10.4f} {df:>3} {p:>12.6f} {verdict:>20}")

    results["n_rejects_at_alpha_bon"] = n_rejects

    if n_rejects == 0:
        family = "NULL-FAMILY: verse-counts modularly random under {7,11,13,19}"
    elif n_rejects == 1:
        family = "PASS-DIRECTED-SINGLE: 1 of 4 reject; capped at α=0.05 single-test"
    elif n_rejects == 2:
        family = "DOUBLE-PASS: 2 of 4 reject"
    else:
        family = f"STRONG NON-UNIFORMITY: {n_rejects} of 4 reject"
    results["family_verdict"] = family
    print()
    print(f"Family verdict: {family}")

    # H2: residue-0 binomial for m where H1 rejected (descriptive)
    print()
    print("H2 (SECONDARY, residue-0 two-sided binomial; descriptive only):")
    for m, res in results["per_modulus"].items():
        if res["rejected_at_alpha_bon"]:
            o0 = res["observed_residue_counts"][0]
            p_bin = binomial_two_sided_p(n, o0, 1.0 / m)
            results["h2_residue_zero"][m] = {
                "modulus": m,
                "count_residue_0": o0,
                "expected_residue_0": n / m,
                "p_two_sided_binomial": p_bin,
                "direction": (
                    "over-represented" if o0 > n / m else
                    "under-represented" if o0 < n / m else
                    "exact-match"
                ),
                "passes_alpha_005_uncorrected": p_bin < 0.05,
            }
            print(f"  m={m}: O_0={o0}, E_0={n/m:.3f}, p_binom={p_bin:.4f}")
        else:
            # Still report the residue-0 count for transparency, but no test
            o0 = res["observed_residue_counts"][0]
            results["h2_residue_zero"][m] = {
                "modulus": m,
                "count_residue_0": o0,
                "expected_residue_0": n / m,
                "p_two_sided_binomial": None,
                "note": "H1 did not reject; H2 not invoked (per pre-reg).",
            }

    # H4(a) sanity: empirical multiset-permutation check for m=19
    print()
    print("H4(a) sanity: mushaf-permutation null for m=19 (should be exactly invariant)…")
    rng = random.Random(SEED + 1)
    chi2_19 = results["per_modulus"][19]["chi2"]
    n_perms_check = 1000  # suffices for invariance demonstration
    diffs = 0
    for _ in range(n_perms_check):
        perm = verse_counts[:]
        rng.shuffle(perm)
        residues = [v % 19 for v in perm]
        observed = [residues.count(k) for k in range(19)]
        chi2_p = chi2_stat(observed, [n / 19] * 19)
        if abs(chi2_p - chi2_19) > 1e-9:
            diffs += 1
    results["h4a_empirical_invariance_check"] = {
        "n_perms": n_perms_check,
        "n_chi2_differs_from_observed": diffs,
        "invariance_confirmed": diffs == 0,
    }
    print(f"  Permutations with χ² differing from observed: {diffs} / {n_perms_check} "
          f"(must be 0).")

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults written: {OUT_JSON}")


if __name__ == "__main__":
    main()
