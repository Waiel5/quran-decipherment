#!/usr/bin/env python3
"""Q039-F-01 — Tanzīl-cluster (H-NEW-1100) Late-Meccan Nöldeke-peak co-localization.

Pre-reg: surahs/Q039-al-zumar/preregs/Q039-F-01-tanzil-cluster-noldeke-peak-prereg.md
Pre-reg SHA: 3634a4cb01d1efbcf3ff86880297f78081d62a93bfb692ae7bebfec0a89bfbe3
Seed: 20260509  |  α_bon: 0.0125  |  k: 4  |  bonferroni_family: Q039-novel-tests

Run from project root:  python3 surahs/Q039-al-zumar/scripts/Q039_F_01_tanzil_cluster.py
"""

import csv
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[3]
PREREG_PATH = PROJECT_ROOT / "surahs" / "Q039-al-zumar" / "preregs" / "Q039-F-01-tanzil-cluster-noldeke-peak-prereg.md"
EXPECTED_SHA = "3634a4cb01d1efbcf3ff86880297f78081d62a93bfb692ae7bebfec0a89bfbe3"
OUT_PATH = PROJECT_ROOT / "surahs" / "Q039-al-zumar" / "csv" / "Q039-F-01.json"
REVELATION_CSV = PROJECT_ROOT / "data" / "revelation-order.csv"

SEED = 20260509
N_PERM = 10_000
ALPHA_BON = 0.0125

TANZIL_CLUSTER = [32, 39, 40, 41, 45, 46]


def verify_prereg_sha() -> str:
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH\n  expected: {EXPECTED_SHA}\n  found:    {sha}\n"
        )
        sys.exit(1)
    return sha


def load_noldeke_ranks() -> dict[int, int]:
    ranks = {}
    with REVELATION_CSV.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ranks[int(row["mushaf_order"])] = int(row["noldeke_order"])
    return ranks


def main() -> None:
    sha = verify_prereg_sha()
    print(f"[OK] pre-reg SHA verified: {sha[:16]}...")

    ranks = load_noldeke_ranks()
    obs_ranks = [ranks[s] for s in TANZIL_CLUSTER]
    obs_var = float(np.var(obs_ranks, ddof=0))
    obs_mean = float(np.mean(obs_ranks))

    print(f"[INFO] observed tanzīl-cluster Nöldeke ranks: {obs_ranks}")
    print(f"[INFO] observed variance: {obs_var:.4f}")
    print(f"[INFO] observed mean: {obs_mean:.4f}")

    rng = np.random.default_rng(SEED)
    all_surahs = np.array(sorted(ranks.keys()))
    all_ranks = np.array([ranks[int(s)] for s in all_surahs])
    n = len(TANZIL_CLUSTER)

    null_vars = np.empty(N_PERM)
    null_means = np.empty(N_PERM)
    for i in range(N_PERM):
        idx = rng.choice(len(all_surahs), size=n, replace=False)
        sample = all_ranks[idx]
        null_vars[i] = sample.var(ddof=0)
        null_means[i] = sample.mean()

    p_var = float(np.mean(null_vars <= obs_var))  # one-tailed lower
    p_mean = float(np.mean(null_means >= obs_mean))  # one-tailed upper

    h1_pass = p_var <= ALPHA_BON
    h2_pass = p_mean <= ALPHA_BON

    if h1_pass and h2_pass:
        verdict = "CONFIRMED-DIRECTED"
    elif h1_pass or h2_pass:
        verdict = "PASS-DIRECTED"
    else:
        verdict = "NULL"

    print(f"\n[RESULT] H1 var-Nöldeke perm-p: {p_var:.6f}  (α_bon = {ALPHA_BON})  → {'PASS' if h1_pass else 'FAIL'}")
    print(f"[RESULT] H2 mean-Nöldeke perm-p: {p_mean:.6f}  (α_bon = {ALPHA_BON})  → {'PASS' if h2_pass else 'FAIL'}")
    print(f"[VERDICT] {verdict}")

    out = {
        "id": "Q039-F-01",
        "h_new_id": "H-NEW-1270",
        "title": "Tanzīl-cluster (H-NEW-1100) Late-Meccan Nöldeke-peak co-localization",
        "prereg_path": str(PREREG_PATH.relative_to(PROJECT_ROOT)),
        "prereg_sha": EXPECTED_SHA,
        "prereg_sha_verified": sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "bonferroni_k": 4,
        "bonferroni_family": "Q039-novel-tests",
        "tanzil_cluster": TANZIL_CLUSTER,
        "observed_noldeke_ranks": obs_ranks,
        "observed_variance": obs_var,
        "observed_mean": obs_mean,
        "null_variance_mean": float(null_vars.mean()),
        "null_variance_q025": float(np.quantile(null_vars, 0.025)),
        "null_variance_q975": float(np.quantile(null_vars, 0.975)),
        "null_mean_mean": float(null_means.mean()),
        "null_mean_q025": float(np.quantile(null_means, 0.025)),
        "null_mean_q975": float(np.quantile(null_means, 0.975)),
        "h1_p_variance_lowtail": p_var,
        "h2_p_mean_uppertail": p_mean,
        "h1_pass": h1_pass,
        "h2_pass": h2_pass,
        "verdict": verdict,
        "verdict_ceiling": "PASS-DIRECTED",
        "rules_tuple": [
            "no-tashkeel",
            "orthographic-token",
            "graphemes",
            "basmala-counted-only-in-Q1",
            "Hafs-Kufan",
            "mashriqi",
        ],
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\n[OK] wrote {OUT_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
