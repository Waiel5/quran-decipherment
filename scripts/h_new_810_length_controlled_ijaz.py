#!/usr/bin/env python3
"""
H-NEW-810 — Length-controlled iʿjāz partial correlation.

Tests whether the H-NEW-730 anti-twinning (r(content, rhyme) = -0.864) survives
partialling out verse-length (letters/verse and words/verse from H-NEW-770).

Three partial-r tests:
    T1: r(d_content, d_rhyme   | letters_per_verse)
    T2: r(d_content, d_rhyme   | words_per_verse)
    T3: r(d_content, d_phoneme | letters_per_verse)

Permutation null (10000 perms, shuffle the rhyme/phoneme vector only).
Bonferroni-3 → α_bon = 0.01667.

Pre-reg SHA: 4f3970eb430bd44d33c89d5577feffd3361866e9f80db6d93000e4e555161bb1
Seed:        20260448
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import sys
from pathlib import Path

import numpy as np

PREREG_SHA = "4f3970eb430bd44d33c89d5577feffd3361866e9f80db6d93000e4e555161bb1"
SEED = 20260448
N_PERM = 10000
ALPHA_BON = 0.05 / 3.0  # 0.01666...

ROOT = Path("/Users/grey/Downloads/quran")
PREREG_PATH = ROOT / "findings/phase-b-hypotheses/h-new-810-length-controlled-ijaz-prereg.md"
H730_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-730.json"
H770_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-770.json"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-810.json"


def verify_prereg_sha() -> str:
    actual = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if actual != PREREG_SHA:
        raise SystemExit(
            f"PREREG SHA MISMATCH.\n  expected: {PREREG_SHA}\n  actual:   {actual}\n"
            f"Refusing to run — prereg has been edited since hashing."
        )
    return actual


def pearson_r(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    xm = x - x.mean()
    ym = y - y.mean()
    num = float((xm * ym).sum())
    den = float(math.sqrt((xm * xm).sum() * (ym * ym).sum()))
    if den == 0.0:
        return float("nan")
    return num / den


def partial_r(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> dict:
    """r(X, Y | Z) via the standard correlation-matrix formula."""
    r_xy = pearson_r(x, y)
    r_xz = pearson_r(x, z)
    r_yz = pearson_r(y, z)
    denom = math.sqrt(max(0.0, (1.0 - r_xz * r_xz) * (1.0 - r_yz * r_yz)))
    pr = (r_xy - r_xz * r_yz) / denom if denom > 0 else float("nan")
    return {"r_xy": r_xy, "r_xz": r_xz, "r_yz": r_yz, "partial_r": pr}


def fisher_z(r: float) -> float:
    if r >= 1.0:
        return float("inf")
    if r <= -1.0:
        return float("-inf")
    return 0.5 * math.log((1.0 + r) / (1.0 - r))


def perm_null_partial(
    x: np.ndarray, y: np.ndarray, z: np.ndarray, n_perm: int, rng: np.random.Generator
) -> dict:
    """
    Permutation null for r(X, Y | Z): shuffle Y only.
    One-sided lower-tail (we expect strongly negative partial r).
    """
    observed = partial_r(x, y, z)["partial_r"]
    n = y.size
    null_vals = np.empty(n_perm, dtype=float)
    for i in range(n_perm):
        perm_idx = rng.permutation(n)
        y_perm = y[perm_idx]
        null_vals[i] = partial_r(x, y_perm, z)["partial_r"]
    # Lower-tail empirical p (proportion of nulls ≤ observed).
    le = int(np.sum(null_vals <= observed))
    p_one_sided = (le + 1) / (n_perm + 1)
    return {
        "observed_partial_r": float(observed),
        "perm_p_one_sided_lower": float(p_one_sided),
        "null_mean": float(np.mean(null_vals)),
        "null_std": float(np.std(null_vals, ddof=1)),
        "null_min": float(np.min(null_vals)),
        "null_max": float(np.max(null_vals)),
        "null_pct_at_or_below_obs": le,
        "n_perm": n_perm,
    }


def classify(partial_r_val: float, perm_p: float) -> str:
    """Apply locked thresholds from prereg §7."""
    if partial_r_val <= -0.5 and perm_p <= ALPHA_BON:
        return "PASS-INDEPENDENT"
    if -0.5 < partial_r_val <= -0.3:
        return "PARTIAL-DEPENDENT"
    if partial_r_val > -0.3:
        return "PASS-LENGTH-DRIVEN"
    # partial r ≤ -0.5 but perm p > α_bon → directional but unstable.
    return "DIRECTIONAL-UNSTABLE"


def main() -> int:
    actual_sha = verify_prereg_sha()
    rng = np.random.default_rng(SEED)

    with H730_JSON.open() as f:
        h730 = json.load(f)
    with H770_JSON.open() as f:
        h770 = json.load(f)

    d_content = np.array(h730["d_content"], dtype=float)
    d_rhyme = np.array(h730["d_rhyme"], dtype=float)
    d_phoneme = np.array(h730["d_phoneme"], dtype=float)
    starts_730 = np.array(h730["starts"], dtype=int)

    letters = np.array(h770["metric_letters_per_verse"]["window_obs"], dtype=float)
    words = np.array(h770["metric_words_per_verse"]["window_obs"], dtype=float)
    starts_770 = np.array(h770["starts"], dtype=int)

    # Sanity: lengths and orderings must match.
    n = 100
    for name, arr in (
        ("d_content", d_content),
        ("d_rhyme", d_rhyme),
        ("d_phoneme", d_phoneme),
        ("letters", letters),
        ("words", words),
        ("starts_730", starts_730),
        ("starts_770", starts_770),
    ):
        if arr.size != n:
            raise SystemExit(f"Length mismatch: {name}.size = {arr.size} != {n}")
    if not np.array_equal(starts_730, starts_770):
        raise SystemExit("starts vectors differ between H-NEW-730 and H-NEW-770")

    # Re-derive original H-NEW-730 r values (no length control) for the report.
    r_content_rhyme = pearson_r(d_content, d_rhyme)
    r_content_phoneme = pearson_r(d_content, d_phoneme)

    # Three partial-r tests.
    tests = {}

    # T1: r(d_content, d_rhyme | letters_per_verse)
    t1 = partial_r(d_content, d_rhyme, letters)
    t1_perm = perm_null_partial(d_content, d_rhyme, letters, N_PERM, rng)
    t1["fisher_z"] = fisher_z(t1["partial_r"])
    t1["perm_null"] = t1_perm
    t1["alpha_bon"] = ALPHA_BON
    t1["passes_alpha_bon"] = bool(t1_perm["perm_p_one_sided_lower"] <= ALPHA_BON)
    t1["classification"] = classify(t1["partial_r"], t1_perm["perm_p_one_sided_lower"])
    tests["T1_content_rhyme_given_letters"] = t1

    # T2: r(d_content, d_rhyme | words_per_verse)
    t2 = partial_r(d_content, d_rhyme, words)
    t2_perm = perm_null_partial(d_content, d_rhyme, words, N_PERM, rng)
    t2["fisher_z"] = fisher_z(t2["partial_r"])
    t2["perm_null"] = t2_perm
    t2["alpha_bon"] = ALPHA_BON
    t2["passes_alpha_bon"] = bool(t2_perm["perm_p_one_sided_lower"] <= ALPHA_BON)
    t2["classification"] = classify(t2["partial_r"], t2_perm["perm_p_one_sided_lower"])
    tests["T2_content_rhyme_given_words"] = t2

    # T3: r(d_content, d_phoneme | letters_per_verse)
    t3 = partial_r(d_content, d_phoneme, letters)
    t3_perm = perm_null_partial(d_content, d_phoneme, letters, N_PERM, rng)
    t3["fisher_z"] = fisher_z(t3["partial_r"])
    t3["perm_null"] = t3_perm
    t3["alpha_bon"] = ALPHA_BON
    t3["passes_alpha_bon"] = bool(t3_perm["perm_p_one_sided_lower"] <= ALPHA_BON)
    t3["classification"] = classify(t3["partial_r"], t3_perm["perm_p_one_sided_lower"])
    tests["T3_content_phoneme_given_letters"] = t3

    # Aggregate verdict on the iʿjāz axis (T1 & T2 jointly).
    cls = (t1["classification"], t2["classification"])
    if cls == ("PASS-INDEPENDENT", "PASS-INDEPENDENT"):
        ijaz_verdict = "LENGTH-INDEPENDENT"
    elif "PASS-LENGTH-DRIVEN" in cls and "PASS-INDEPENDENT" not in cls:
        ijaz_verdict = "LENGTH-DRIVEN"
    elif "PASS-INDEPENDENT" in cls and "PASS-LENGTH-DRIVEN" in cls:
        ijaz_verdict = "METRIC-FRAGILE"
    else:
        ijaz_verdict = "PARTIAL-DEPENDENT"

    # Phoneme axis verdict (T3 alone).
    if t3["classification"] == "PASS-INDEPENDENT":
        phoneme_verdict = "LENGTH-INDEPENDENT"
    elif t3["classification"] == "PASS-LENGTH-DRIVEN":
        phoneme_verdict = "LENGTH-DRIVEN"
    elif t3["classification"] == "PARTIAL-DEPENDENT":
        phoneme_verdict = "PARTIAL-DEPENDENT"
    else:
        phoneme_verdict = t3["classification"]

    out = {
        "id": "H-NEW-810",
        "prereg_sha": actual_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "K": 15,
        "n_windows": n,
        "parents": {
            "h_new_730": {
                "json": str(H730_JSON),
                "r_content_rhyme_recomputed": r_content_rhyme,
                "r_content_rhyme_reported": h730["content_x_rhyme"]["pearson_r"],
                "r_content_phoneme_recomputed": r_content_phoneme,
                "r_content_phoneme_reported": h730["content_x_phoneme"]["pearson_r"],
            },
            "h_new_770": {
                "json": str(H770_JSON),
                "r_letters_vs_content": h770["metric_letters_per_verse"][
                    "pearson_r_vs_content_d"
                ],
                "r_words_vs_content": h770["metric_words_per_verse"][
                    "pearson_r_vs_content_d"
                ],
            },
        },
        "tests": tests,
        "verdict": {
            "ijaz_axis_T1_T2": ijaz_verdict,
            "phoneme_axis_T3": phoneme_verdict,
            "summary": (
                f"T1 (content×rhyme | letters): partial r = {tests['T1_content_rhyme_given_letters']['partial_r']:.4f}, "
                f"p = {tests['T1_content_rhyme_given_letters']['perm_null']['perm_p_one_sided_lower']:.5f} → {t1['classification']}; "
                f"T2 (content×rhyme | words): partial r = {tests['T2_content_rhyme_given_words']['partial_r']:.4f}, "
                f"p = {tests['T2_content_rhyme_given_words']['perm_null']['perm_p_one_sided_lower']:.5f} → {t2['classification']}; "
                f"T3 (content×phoneme | letters): partial r = {tests['T3_content_phoneme_given_letters']['partial_r']:.4f}, "
                f"p = {tests['T3_content_phoneme_given_letters']['perm_null']['perm_p_one_sided_lower']:.5f} → {t3['classification']}; "
                f"original r(content,rhyme) = {r_content_rhyme:.4f}; "
                f"original r(content,phoneme) = {r_content_phoneme:.4f}."
            ),
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(out["verdict"]["summary"])
    print(f"ijaz_axis_T1_T2 verdict: {ijaz_verdict}")
    print(f"phoneme_axis_T3 verdict: {phoneme_verdict}")
    print(f"Wrote: {OUT_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
