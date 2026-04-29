"""H-NEW-45 — Muqaṭṭaʿāt Surah-Index Number-Theoretic Enrichment.

Pre-reg: findings/phase-b-hypotheses/h-new-45-muqattaat-surah-index-number-theory-prereg.md

Seed: 20260416
Bonferroni k = 8, α_bon = 0.00625
N_PERM = 100,000

Observed target set: the 29 surah indices that open with muqaṭṭaʿāt.
Null: uniform random sample of 29 surahs from {1..114}.

8 test cells:
  1. prime count (two-sided)
  2. twin-prime-BOTH (one-sided upper, post-hoc-flagged)
  3. Fibonacci count (two-sided)
  4. perfect-square count (two-sided)
  5. triangular count (two-sided)
  6. highly-composite count (two-sided)
  7. mod-19 chi² uniformity (two-sided)
  8. gap-entropy (two-sided)

+ MW-5 positive control on cell 2 using planted-signal family.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import random
import time
from collections import Counter
from typing import List, Tuple

REPO = "/Users/grey/Downloads/quran"
SEED = 20260416
N_PERM = 100_000
ALPHA_BON = 0.05 / 8
N_SURAHS = 114
K = 29  # muqaṭṭaʿāt-opened count

# The locked observed set
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
              36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
assert len(MUQ_SURAHS) == 29


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


PRIMES = frozenset(n for n in range(1, N_SURAHS + 1) if is_prime(n))
TWIN_PAIRS: List[Tuple[int, int]] = [(p, p + 2) for p in PRIMES
                                     if (p + 2) in PRIMES and (p + 2) <= N_SURAHS]
FIBS = frozenset({1, 2, 3, 5, 8, 13, 21, 34, 55, 89})
SQUARES = frozenset({i * i for i in range(1, 12) if i * i <= N_SURAHS})
TRIS = frozenset({k * (k + 1) // 2 for k in range(1, 15)
                  if k * (k + 1) // 2 <= N_SURAHS})
HCNS = frozenset({1, 2, 4, 6, 12, 24, 36, 48, 60, 84, 90, 96, 108})  # first 13 HCN ≤ 114


def cell_counts(S: set) -> dict:
    """Compute cell statistics for a surah-set S of size 29."""
    d = {}
    d["primes"] = sum(1 for n in S if n in PRIMES)
    d["twin_both"] = sum(1 for (a, b) in TWIN_PAIRS if a in S and b in S)
    d["fib"] = sum(1 for n in S if n in FIBS)
    d["sq"] = sum(1 for n in S if n in SQUARES)
    d["tri"] = sum(1 for n in S if n in TRIS)
    d["hcn"] = sum(1 for n in S if n in HCNS)

    # Cell 7: mod-19 chi²
    mod19 = Counter(n % 19 for n in S)
    # 19 cells, expected |S|/19 = 29/19 ≈ 1.526
    exp = len(S) / 19.0
    chi2 = sum(((mod19.get(r, 0) - exp) ** 2) / exp for r in range(19))
    d["mod19_chi2"] = chi2

    # Cell 8: gap-entropy
    sorted_S = sorted(S)
    gaps = [sorted_S[i + 1] - sorted_S[i] for i in range(len(sorted_S) - 1)]
    gap_counts = Counter(gaps)
    n_gaps = len(gaps)
    ent = -sum((c / n_gaps) * math.log2(c / n_gaps)
               for c in gap_counts.values() if c > 0)
    d["gap_entropy"] = ent

    return d


def run_null(rng: random.Random, n_perm: int) -> Tuple[List[dict], float]:
    """Run the permutation null; return list of cell-stat dicts and runtime."""
    t0 = time.time()
    out = []
    all_surahs = list(range(1, N_SURAHS + 1))
    for i in range(n_perm):
        S = set(rng.sample(all_surahs, K))
        out.append(cell_counts(S))
        if (i + 1) % 10000 == 0:
            print(f"  null {i+1}/{n_perm}  elapsed={time.time()-t0:.0f}s")
    return out, time.time() - t0


def empirical_p(obs: float, null_list: List[float], one_sided_upper: bool = False) -> dict:
    n = len(null_list)
    as_or_more_upper = sum(1 for x in null_list if x >= obs) + 1
    as_or_more_lower = sum(1 for x in null_list if x <= obs) + 1
    p_upper = as_or_more_upper / (n + 1)
    p_lower = as_or_more_lower / (n + 1)
    if one_sided_upper:
        return {"p_one_sided_upper": p_upper,
                "null_mean": sum(null_list) / n,
                "null_std": (sum((x - sum(null_list) / n) ** 2 for x in null_list) / n) ** 0.5}
    else:
        return {"p_upper": p_upper, "p_lower": p_lower,
                "p_two_sided": 2 * min(p_upper, p_lower),
                "null_mean": sum(null_list) / n,
                "null_std": (sum((x - sum(null_list) / n) ** 2 for x in null_list) / n) ** 0.5}


def mw5_positive_control(rng: random.Random, n_perm: int = 10000) -> dict:
    """Planted signal: pick 18 of the 20 twin-prime endpoint values, plus
    11 random fillers to make 29. Cell 2 should trigger STRONGLY.
    """
    twin_endpoints = sorted(set(a for (a, b) in TWIN_PAIRS) |
                            set(b for (a, b) in TWIN_PAIRS))
    # 19 distinct values (5 and 7 shared); pick all 19 + 10 fillers = 29
    non_endpoints = [n for n in range(1, N_SURAHS + 1)
                     if n not in set(twin_endpoints)]
    planted = set(twin_endpoints) | set(rng.sample(non_endpoints, K - len(twin_endpoints)))
    assert len(planted) == K
    obs = cell_counts(planted)

    all_surahs = list(range(1, N_SURAHS + 1))
    null_twin_both = []
    for i in range(n_perm):
        S = set(rng.sample(all_surahs, K))
        null_twin_both.append(sum(1 for (a, b) in TWIN_PAIRS if a in S and b in S))
    p = (sum(1 for x in null_twin_both if x >= obs["twin_both"]) + 1) / (n_perm + 1)
    return {"planted_twin_both": obs["twin_both"],
            "p_positive_control": p,
            "detect_at_alpha_bon_over_10": p < (ALPHA_BON / 10.0)}


def main():
    print("[H-NEW-45] observed ...")
    obs = cell_counts(MUQ_SURAHS)
    print(f"  observed: {obs}")

    print("[H-NEW-45] MW-5 positive control ...")
    rng_pc = random.Random(SEED + 1)
    pc = mw5_positive_control(rng_pc, n_perm=10000)
    print(f"  positive control: {pc}")

    print(f"[H-NEW-45] null n_perm={N_PERM} ...")
    rng = random.Random(SEED)
    nulls, runtime = run_null(rng, N_PERM)

    # Extract per-cell null distributions
    ncell = {
        "primes": [n["primes"] for n in nulls],
        "twin_both": [n["twin_both"] for n in nulls],
        "fib": [n["fib"] for n in nulls],
        "sq": [n["sq"] for n in nulls],
        "tri": [n["tri"] for n in nulls],
        "hcn": [n["hcn"] for n in nulls],
        "mod19_chi2": [n["mod19_chi2"] for n in nulls],
        "gap_entropy": [n["gap_entropy"] for n in nulls],
    }

    results = {}
    results["primes"] = empirical_p(obs["primes"], ncell["primes"])
    results["twin_both"] = empirical_p(obs["twin_both"], ncell["twin_both"], one_sided_upper=True)
    results["fib"] = empirical_p(obs["fib"], ncell["fib"])
    results["sq"] = empirical_p(obs["sq"], ncell["sq"])
    results["tri"] = empirical_p(obs["tri"], ncell["tri"])
    results["hcn"] = empirical_p(obs["hcn"], ncell["hcn"])
    results["mod19_chi2"] = empirical_p(obs["mod19_chi2"], ncell["mod19_chi2"])
    results["gap_entropy"] = empirical_p(obs["gap_entropy"], ncell["gap_entropy"])

    # Significance table
    sig = {}
    for k, r in results.items():
        if "p_one_sided_upper" in r:
            sig[k] = r["p_one_sided_upper"] < ALPHA_BON
        else:
            sig[k] = r["p_two_sided"] < ALPHA_BON

    n_sig = sum(sig.values())
    n_sig_prime_related = sum(1 for k in ["primes", "twin_both"] if sig.get(k, False))

    # Verdict
    if not pc["detect_at_alpha_bon_over_10"]:
        verdict = "NULL-BROKEN"
    elif n_sig == 0:
        verdict = "NULL"
    elif n_sig == 1:
        only = [k for k, v in sig.items() if v][0]
        if only == "twin_both":
            verdict = "EXPLORATORY-POST-HOC"
        else:
            verdict = "EXPLORATORY-POST-HOC"  # still post-hoc framing per pre-reg
    elif n_sig == 2:
        verdict = "EXPLORATORY"
    elif n_sig >= 3 and sig.get("twin_both", False) and n_sig_prime_related >= 2:
        verdict = "STRONG-POST-HOC"
    elif n_sig >= 3:
        verdict = "PARTIAL-PASS"
    else:
        verdict = "EXPLORATORY"

    # SHA of pre-reg
    preg_path = os.path.join(REPO, "findings/phase-b-hypotheses/"
                             "h-new-45-muqattaat-surah-index-number-theory-prereg.md")
    with open(preg_path, "rb") as f:
        preg_sha = hashlib.sha256(f.read()).hexdigest()

    out = {
        "hypothesis_id": "H-NEW-45",
        "run_date": "2026-04-16",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_family": "2026-04-16-H-NEW-45",
        "bonferroni_k": 8,
        "alpha_bon": ALPHA_BON,
        "prereg_sha256": preg_sha,
        "muq_surahs_locked": sorted(MUQ_SURAHS),
        "observed": obs,
        "positive_control": pc,
        "per_cell_results": results,
        "per_cell_significant_at_alpha_bon": sig,
        "n_significant": n_sig,
        "verdict": verdict,
        "runtime_seconds": runtime,
    }

    out_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-45.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[H-NEW-45] wrote {out_path}")
    print(f"[H-NEW-45] VERDICT: {verdict}")
    for k, r in results.items():
        p = r.get("p_one_sided_upper", r.get("p_two_sided"))
        print(f"  {k}: obs={obs[k]:.3f}  null_mean={r['null_mean']:.3f}  "
              f"null_std={r['null_std']:.3f}  p={p:.5f}  sig={sig[k]}")


if __name__ == "__main__":
    main()
