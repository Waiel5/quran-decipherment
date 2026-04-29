#!/usr/bin/env python3
"""H-NEW-276 — deeper null for the H-NEW-263 hub question.

This follow-up freezes the H-NEW-263 observed construction and hub statistic:
  - surah x attested-divine-name binary incidence
  - weighted projection W = B @ B.T, diagonal zeroed
  - conservative hub screen W >= 2
  - S2[i] = sum_j W[i, j] * 1[W[i, j] >= 2]
  - Z2[i] null-standardized from fixed-margin permutations
  - Zmax = max_i Z2[i]

Only the null resolution is deepened. The fixed-margin null family, swap depth,
and family-wise decision threshold are inherited unchanged from H-NEW-263.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import random
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path("/Users/grey/Downloads/quran")
DIVINE_CSV = ROOT / "findings" / "phase-b-hypotheses" / "divine-names-by-verse.csv"
PREREG = (
    ROOT
    / "findings"
    / "phase-b-hypotheses"
    / "h-new-276-q27-hub-resolution-prereg.md"
)
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-276.json"

SEED = 20260694
HUB_THRESHOLD = 2
Q27_SURAH = 27
N_PERM = 10000
ACCEPTED_SWAPS_PER_PERM = 500
INHERITED_ALPHA_BON = 0.025
MAX_WORKERS = min(12, os.cpu_count() or 1)
CHUNK_SIZE = 50

_WORKER_B: np.ndarray | None = None


def sha256_hex(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_surah_name_sets(path: Path) -> tuple[list[str], np.ndarray]:
    per_surah: dict[int, set[str]] = defaultdict(set)
    attested_names: set[str] = set()
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["surah"])
            names = [x for x in row["names_translit"].split("|") if x]
            for name in names:
                per_surah[sid].add(name)
                attested_names.add(name)

    names_sorted = sorted(attested_names)
    name_idx = {name: idx for idx, name in enumerate(names_sorted)}
    B = np.zeros((114, len(names_sorted)), dtype=np.uint8)
    for sid in range(1, 115):
        for name in per_surah.get(sid, set()):
            B[sid - 1, name_idx[name]] = 1
    return names_sorted, B


def swap_randomize_fixed_margins(
    matrix: np.ndarray,
    rng: random.Random,
    accepted_target: int = ACCEPTED_SWAPS_PER_PERM,
) -> np.ndarray:
    B = matrix.copy()
    n_rows, n_cols = B.shape
    accepted = 0
    tries = 0
    max_tries = accepted_target * 1000
    while accepted < accepted_target and tries < max_tries:
        tries += 1
        r1, r2 = rng.sample(range(n_rows), 2)
        c1, c2 = rng.sample(range(n_cols), 2)
        a = int(B[r1, c1])
        b = int(B[r1, c2])
        c = int(B[r2, c1])
        d = int(B[r2, c2])
        if a == 1 and d == 1 and b == 0 and c == 0:
            B[r1, c1] = 0
            B[r2, c2] = 0
            B[r1, c2] = 1
            B[r2, c1] = 1
            accepted += 1
        elif a == 0 and d == 0 and b == 1 and c == 1:
            B[r1, c2] = 0
            B[r2, c1] = 0
            B[r1, c1] = 1
            B[r2, c2] = 1
            accepted += 1
    if accepted < accepted_target:
        raise RuntimeError(
            f"Accepted only {accepted} swaps out of target {accepted_target}; "
            "increase max_tries or reduce accepted_target."
        )
    return B


def weighted_projection(B: np.ndarray) -> np.ndarray:
    W = B.astype(np.int16) @ B.T.astype(np.int16)
    np.fill_diagonal(W, 0)
    return W


def hub_strength_ge2(W: np.ndarray) -> np.ndarray:
    return (W * (W >= HUB_THRESHOLD)).sum(axis=1).astype(np.int16)


def empirical_upper_p(null_values: np.ndarray, observed: float) -> tuple[float, int]:
    ge = int(np.sum(null_values >= observed))
    p = (1 + ge) / (len(null_values) + 1)
    return float(p), ge


def binomial_mc_se(p: float, n: int) -> float:
    if n <= 0:
        return 0.0
    return math.sqrt(max(p * (1.0 - p), 0.0) / n)


def init_worker(B: np.ndarray) -> None:
    global _WORKER_B
    _WORKER_B = B


def run_chunk(task: tuple[int, int]) -> tuple[int, np.ndarray]:
    start, size = task
    if _WORKER_B is None:
        raise RuntimeError("worker matrix not initialized")
    out = np.empty((size, _WORKER_B.shape[0]), dtype=np.int16)
    for offset in range(size):
        perm_idx = start + offset
        rng = random.Random(SEED + perm_idx)
        Bn = swap_randomize_fixed_margins(_WORKER_B, rng)
        Wn = weighted_projection(Bn)
        out[offset, :] = hub_strength_ge2(Wn)
    return start, out


def ranked_surahs_from_null(
    obs_strength2: np.ndarray,
    null_strength2: np.ndarray,
) -> dict[str, Any]:
    null_mean = null_strength2.mean(axis=0)
    null_sd = null_strength2.std(axis=0, ddof=1)
    null_sd = np.where(null_sd == 0, 1.0, null_sd)
    obs_z = (obs_strength2 - null_mean) / null_sd
    null_z = (null_strength2 - null_mean) / null_sd
    max_null_z = null_z.max(axis=1)

    z_max_obs = float(obs_z.max())
    p_exist, ge_max = empirical_upper_p(max_null_z, z_max_obs)

    ranked = []
    for idx in np.argsort(-obs_z):
        sid = int(idx + 1)
        p_raw, ge_raw = empirical_upper_p(null_strength2[:, idx], float(obs_strength2[idx]))
        p_adj, ge_adj = empirical_upper_p(max_null_z, float(obs_z[idx]))
        ranked.append(
            {
                "surah": sid,
                "strength_ge2_obs": int(obs_strength2[idx]),
                "null_mean": float(null_mean[idx]),
                "null_sd": float(null_sd[idx]),
                "z": float(obs_z[idx]),
                "p_raw": float(p_raw),
                "p_adj_fwer": float(p_adj),
                "ge_raw_count": int(ge_raw),
                "ge_adj_count": int(ge_adj),
            }
        )

    top = ranked[0]
    q27 = next(row for row in ranked if row["surah"] == Q27_SURAH)
    return {
        "z_max_obs": z_max_obs,
        "p_exist": float(p_exist),
        "ge_max_count": int(ge_max),
        "mc_se_p_exist": float(binomial_mc_se(p_exist, len(null_strength2))),
        "cell_b_pass_inherited_alpha_0_025": bool(p_exist < INHERITED_ALPHA_BON),
        "ranked_surahs": ranked,
        "top_surah": top["surah"],
        "q27": {
            **q27,
            "is_top_rank": bool(top["surah"] == Q27_SURAH),
            "rank": int(next(i + 1 for i, row in enumerate(ranked) if row["surah"] == Q27_SURAH)),
            "passes_inherited_alpha_0_025": bool(q27["p_adj_fwer"] < INHERITED_ALPHA_BON),
            "mc_se_p_raw": float(binomial_mc_se(q27["p_raw"], len(null_strength2))),
            "mc_se_p_adj": float(binomial_mc_se(q27["p_adj_fwer"], len(null_strength2))),
        },
    }


def verdict(hub: dict[str, Any]) -> str:
    if hub["cell_b_pass_inherited_alpha_0_025"]:
        if hub["top_surah"] == Q27_SURAH:
            return "Q27-HUB-CONFIRMED-DEEP-NULL"
        return "ALT-HUB-CONFIRMED-DEEP-NULL"
    return "NO-HUB-SURVIVES-DEEP-NULL"


def main() -> None:
    attested_names, B = load_surah_name_sets(DIVINE_CSV)
    prereg_sha = sha256_hex(PREREG)
    W_obs = weighted_projection(B)
    obs_strength2 = hub_strength_ge2(W_obs)

    null_strength2 = np.empty((N_PERM, B.shape[0]), dtype=np.int16)
    tasks = [
        (start, min(CHUNK_SIZE, N_PERM - start))
        for start in range(0, N_PERM, CHUNK_SIZE)
    ]

    print(
        f"[h-new-276] starting deep null: n_perm={N_PERM}, "
        f"workers={MAX_WORKERS}, chunk_size={CHUNK_SIZE}",
        flush=True,
    )
    completed = 0
    try:
        with ProcessPoolExecutor(
            max_workers=MAX_WORKERS,
            initializer=init_worker,
            initargs=(B,),
        ) as ex:
            for start, chunk in ex.map(run_chunk, tasks):
                null_strength2[start : start + chunk.shape[0], :] = chunk
                completed += chunk.shape[0]
                if completed % 500 == 0 or completed == N_PERM:
                    print(f"[h-new-276] completed {completed}/{N_PERM}", flush=True)
    except PermissionError:
        print("[h-new-276] process pool denied; falling back to serial execution", flush=True)
        init_worker(B)
        for task in tasks:
            start, chunk = run_chunk(task)
            null_strength2[start : start + chunk.shape[0], :] = chunk
            completed += chunk.shape[0]
            if completed % 500 == 0 or completed == N_PERM:
                print(f"[h-new-276] completed {completed}/{N_PERM}", flush=True)

    hub = ranked_surahs_from_null(obs_strength2, null_strength2)
    out = {
        "id": "H-NEW-276",
        "title": "Deep-null follow-up to H-NEW-263 hub existence",
        "parent_hypothesis": "H-NEW-263",
        "seed": SEED,
        "pre_reg_sha256": prereg_sha,
        "source_csv": str(DIVINE_CSV),
        "n_surahs": int(B.shape[0]),
        "n_attested_names": int(len(attested_names)),
        "n_perm": N_PERM,
        "accepted_swaps_per_perm": ACCEPTED_SWAPS_PER_PERM,
        "hub_threshold": HUB_THRESHOLD,
        "inherited_alpha_bon": INHERITED_ALPHA_BON,
        "n_workers": MAX_WORKERS,
        "chunk_size": CHUNK_SIZE,
        "observed": {
            "q27_strength_ge2": int(obs_strength2[Q27_SURAH - 1]),
            "top_strength_ge2": [
                {
                    "surah": int(i + 1),
                    "strength_ge2": int(obs_strength2[i]),
                }
                for i in np.argsort(-obs_strength2)[:10]
            ],
        },
        "hub_test_deep_null": {
            "z_max_obs": hub["z_max_obs"],
            "p_exist": hub["p_exist"],
            "ge_max_count": hub["ge_max_count"],
            "mc_se_p_exist": hub["mc_se_p_exist"],
            "cell_b_pass_inherited_alpha_0_025": hub["cell_b_pass_inherited_alpha_0_025"],
            "top_surah": hub["top_surah"],
            "top_ranked_surahs": hub["ranked_surahs"][:15],
            "q27": hub["q27"],
        },
        "verdict": verdict(hub),
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"wrote {OUT_JSON}")
    print(f"z_max_obs = {out['hub_test_deep_null']['z_max_obs']:.6f}")
    print(f"p_exist = {out['hub_test_deep_null']['p_exist']:.6f}")
    print(
        "q27 = "
        f"rank {out['hub_test_deep_null']['q27']['rank']}, "
        f"z {out['hub_test_deep_null']['q27']['z']:.6f}, "
        f"p_adj {out['hub_test_deep_null']['q27']['p_adj_fwer']:.6f}"
    )
    print(f"verdict = {out['verdict']}")


if __name__ == "__main__":
    main()
