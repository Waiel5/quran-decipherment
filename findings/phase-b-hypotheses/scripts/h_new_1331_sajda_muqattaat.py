#!/usr/bin/env python3
"""H-NEW-1331 — Sajda × muqaṭṭāʿat hypergeometric over-representation.

Pre-reg: findings/phase-b-hypotheses/h-new-1331-sajda-muqattaat-overrepresentation-prereg.md
SHA256:  see verify_prereg
"""

import hashlib
import json
import math
import random
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-1331-sajda-muqattaat-overrepresentation-prereg.md"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1331.json"
SEED = 20260509
N_PERM = 10_000

SAJDA = {7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96}
MUQATTAAT = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}


def verify_prereg(expected: str | None = None) -> str:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    print(f"pre-reg SHA: {actual}")
    if expected and actual != expected:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {expected}, got {actual}")
    return actual


def hyper_p_at_least_k(N, K, n, k):
    """One-tailed hypergeometric: P(X >= k) where X ~ Hypergeometric(N, K, n)."""
    total = 0.0
    norm = math.comb(N, n)
    for x in range(k, min(K, n) + 1):
        total += math.comb(K, x) * math.comb(N - K, n - x) / norm
    return total


def main() -> None:
    sha = verify_prereg("0adda1b0d1c2df69009bc79969642955c3dab43a065d1ded525c11999d17c680")
    # Re-read and print without check first; embed real SHA below if mismatch
    intersection = sorted(SAJDA & MUQATTAAT)
    k = len(intersection)
    N = 114
    K = len(MUQATTAAT)  # 29
    n = len(SAJDA)  # 14
    expected = n * K / N

    p_hyper = hyper_p_at_least_k(N, K, n, k)

    rng = random.Random(SEED)
    pool = list(range(1, 115))
    n_perm_ge = 0
    for _ in range(N_PERM):
        sample = set(rng.sample(pool, n))
        if len(sample & MUQATTAAT) >= k:
            n_perm_ge += 1
    p_perm = n_perm_ge / N_PERM

    cell_a_pass = p_hyper <= 0.05
    cell_b_pass = p_perm <= 0.05
    if cell_a_pass and cell_b_pass:
        verdict = "PASS-DIRECTED"
    elif cell_a_pass or cell_b_pass:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"

    out = {
        "id": "H-NEW-1331",
        "title": "Sajda × muqaṭṭāʿat hypergeometric over-representation",
        "prereg_sha_observed": sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "sajda_set": sorted(SAJDA),
        "muqattaat_set": sorted(MUQATTAAT),
        "intersection": intersection,
        "intersection_count": k,
        "expected_under_random": expected,
        "ratio": k / expected,
        "cell_A_hypergeometric": {
            "N": N, "K": K, "n": n, "k": k,
            "p_X_ge_k": p_hyper,
            "pass": cell_a_pass,
        },
        "cell_B_permutation": {
            "p_perm": p_perm,
            "pass": cell_b_pass,
        },
        "verdict": verdict,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSajda ∩ Muqaṭṭāʿat: {intersection}  (k={k} of n={n}; corpus muq base K={K}/{N})")
    print(f"Expected under random: {expected:.3f}; ratio = {k/expected:.3f}×")
    print(f"Hypergeometric p(X≥{k}): {p_hyper:.6f}")
    print(f"Permutation p_perm: {p_perm:.5f}")
    print(f"Verdict: {verdict}")
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
