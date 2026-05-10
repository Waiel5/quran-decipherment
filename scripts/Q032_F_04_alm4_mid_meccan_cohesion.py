#!/usr/bin/env python3
"""
Q032-F-04 — ALM-4 mid-Meccan cluster {Q 29, 30, 31, 32} Fisher-Rao cohesion.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q032-al-sajda/Q032-F-04-alm4-mid-meccan-cohesion-prereg.md
SHA256:  363410f7172124d9e93c7d106a81e32ba4759747d55893efb345522527648d48

Two-cell test: uniform null (4-of-113) + length-matched null (4-of-X, length-banded).
"""

from __future__ import annotations
import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q032-al-sajda/Q032-F-04-alm4-mid-meccan-cohesion-prereg.md"
EXPECTED_SHA = "363410f7172124d9e93c7d106a81e32ba4759747d55893efb345522527648d48"
OUT = ROOT / "surahs/Q032-al-sajda/csv/Q032-F-04.json"
SEED = 20260509
N_PERM = 10000
CLUSTER = [29, 30, 31, 32]


def sha_verify():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}", file=sys.stderr)
        sys.exit(1)
    return actual


def load_fr():
    with (ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json").open(encoding="utf-8") as f:
        d = json.load(f)
    fr = {}
    for a, b, v in d["D_matrix_upper_triangular"]:
        fr[(min(a, b), max(a, b))] = v
    stats = d["distance_matrix_stats"]
    return fr, stats


def mean_intra(fr, surahs):
    n = len(surahs)
    pairs = [(surahs[i], surahs[j]) for i in range(n) for j in range(i + 1, n)]
    return sum(fr[(min(a, b), max(a, b))] for a, b in pairs) / len(pairs)


def load_surah_words():
    with (ROOT / "quran-text/quran-no-tashkeel.json").open(encoding="utf-8") as f:
        q = json.load(f)
    words = {}
    for i, surah in enumerate(q):
        words[i + 1] = sum(len(v["text"].split()) for v in surah["verses"])
    return words


def main():
    sha_actual = sha_verify()
    fr, fr_stats = load_fr()
    words = load_surah_words()

    # Observed
    T_obs = mean_intra(fr, CLUSTER)
    within_pairs = []
    for i in range(len(CLUSTER)):
        for j in range(i + 1, len(CLUSTER)):
            a, b = CLUSTER[i], CLUSTER[j]
            within_pairs.append({"a": a, "b": b, "d": fr[(min(a, b), max(a, b))]})

    rng_a = random.Random(SEED)
    rng_b = random.Random(SEED + 1)

    # Cell A — uniform null (4-of-113 exclude Q1)
    pool_a = [s for s in range(2, 115)]
    null_a = []
    for _ in range(N_PERM):
        sample = rng_a.sample(pool_a, 4)
        null_a.append(mean_intra(fr, sample))
    null_a.sort()
    p_a = sum(1 for v in null_a if v <= T_obs) / N_PERM
    pct5_a = null_a[int(0.05 * N_PERM)]
    median_a = null_a[N_PERM // 2]

    # Cell B — length-matched null (4-of-X)
    # Length band from Q030-F-08 (IQR of large-band): 543-815
    band_low, band_high = 543, 815
    pool_b = [s for s in pool_a if band_low <= words[s] <= band_high]
    null_b = []
    n_accepted = 0
    for _ in range(N_PERM):
        if len(pool_b) < 4:
            break
        sample = rng_b.sample(pool_b, 4)
        null_b.append(mean_intra(fr, sample))
        n_accepted += 1
    null_b.sort()
    p_b = sum(1 for v in null_b if v <= T_obs) / max(n_accepted, 1)
    pct5_b = null_b[int(0.05 * n_accepted)] if n_accepted else float("nan")
    median_b = null_b[n_accepted // 2] if n_accepted else float("nan")

    pass_a = p_a <= 0.025
    pass_b = p_b <= 0.025

    if pass_a and pass_b:
        verdict = "PASS-DIRECTED (both cells)"
    elif pass_a or pass_b:
        verdict = "PARTIAL (1/2 cells)"
    else:
        verdict = "NULL"

    # MW-5 positive control: ḤM-7 cluster (which H-NEW-1395 confirmed NULL); we expect higher T_obs than ALM-4
    HM_7 = [40, 41, 42, 43, 44, 45, 46]
    T_HM_7 = mean_intra(fr, HM_7)

    out = {
        "test_id": "Q032-F-04",
        "title": "ALM-4 mid-Meccan cluster {Q 29, 30, 31, 32} Fisher-Rao cohesion",
        "prereg_sha_expected": EXPECTED_SHA,
        "prereg_sha_actual": sha_actual,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": 0.025,
        "cluster": CLUSTER,
        "cluster_total_words": sum(words[s] for s in CLUSTER),
        "cluster_per_surah_words": {s: words[s] for s in CLUSTER},
        "T_obs_mean_pairwise_FR": T_obs,
        "within_cluster_pair_distances": sorted(within_pairs, key=lambda r: r["d"]),
        "corpus_pairwise_FR_stats": fr_stats,
        "cell_A_uniform": {
            "n_perm": N_PERM,
            "null_5pct": pct5_a,
            "null_50pct": median_a,
            "p_one_sided_le": p_a,
            "pass_alpha_bon": pass_a,
        },
        "cell_B_length_matched": {
            "band_low_words": band_low,
            "band_high_words": band_high,
            "pool_size": len(pool_b),
            "n_accepted": n_accepted,
            "null_5pct": pct5_b,
            "null_50pct": median_b,
            "p_one_sided_le": p_b,
            "pass_alpha_bon": pass_b,
        },
        "mw5_positive_control_HM_7": {
            "cluster": HM_7,
            "T_obs": T_HM_7,
            "comparison_note": ("ALM-4 (T_obs={:.4f}) vs HM-7 (T_obs={:.4f}); H-NEW-1395 CONFIRMED-NULL HM-7. "
                                "Lower T_obs = tighter cluster.").format(T_obs, T_HM_7),
        },
        "comparison_to_Q030_F_08_ALM_6": {
            "ALM_6_T_obs": 0.9256812,
            "ALM_4_T_obs": T_obs,
            "delta": T_obs - 0.9256812,
            "interpretation": ("Negative delta = removing Q 2 + Q 3 from ALM-6 to form ALM-4 "
                               "tightens (or loosens) the cluster mean by this amount."),
        },
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"WROTE {OUT}")
    print(f"verdict: {verdict}; T_obs={T_obs:.4f}; p_uniform={p_a:.4f}; p_len_matched={p_b:.4f}")


if __name__ == "__main__":
    main()
