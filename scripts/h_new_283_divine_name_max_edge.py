#!/usr/bin/env python3
"""H-NEW-283 -- divine-name surah max-edge under fixed-margin null.

This follow-up freezes the same observed construction used by H-NEW-263 and
H-NEW-276:
  - surah x attested-divine-name binary incidence
  - weighted projection W = B @ B.T, diagonal zeroed
  - fixed-margin bipartite double-edge-swap null

The primary inferential object is the corpus-level max edge weight:
  M = max_{i<j} shared_names(i,j)

The max statistic itself is the adjustment; the reported p-value is
P_null(M >= M_obs).
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
PREREG = ROOT / "findings" / "phase-b-hypotheses" / "h-new-283-divine-name-max-edge-prereg.md"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-283.json"

SEED = 20260694
N_PERM = 10000
ACCEPTED_SWAPS_PER_PERM = 500
ALPHA = 0.025
N_PERM_MW5 = 120
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


def max_shared_names(W: np.ndarray) -> int:
    triu = np.triu(W, 1)
    return int(triu.max()) if triu.size else 0


def empirical_upper_p(null_values: np.ndarray, observed: float) -> tuple[float, int]:
    ge = int(np.sum(null_values >= observed))
    p = (1 + ge) / (len(null_values) + 1)
    return float(p), ge


def binomial_mc_se(p: float, n: int) -> float:
    if n <= 0:
        return 0.0
    return math.sqrt(max(p * (1.0 - p), 0.0) / n)


def summarize_projection(W: np.ndarray) -> dict[str, Any]:
    triu = np.triu(W, 1)
    max_shared = int(triu.max()) if triu.size else 0

    max_edges = []
    top_edges = []
    for i in range(W.shape[0]):
        for j in range(i + 1, W.shape[1]):
            w = int(W[i, j])
            if w == 0:
                continue
            row = {"surah_a": i + 1, "surah_b": j + 1, "shared_names": w}
            top_edges.append(row)
            if w == max_shared:
                max_edges.append(row)
    top_edges.sort(key=lambda row: (-row["shared_names"], row["surah_a"], row["surah_b"]))
    max_edges.sort(key=lambda row: (row["surah_a"], row["surah_b"]))

    q2_q3 = next(
        (
            row
            for row in top_edges
            if row["surah_a"] == 2 and row["surah_b"] == 3
        ),
        None,
    )

    return {
        "M_max_shared_names": max_shared,
        "top_edges": top_edges[:15],
        "max_edges": max_edges,
        "max_edge_count": len(max_edges),
        "q2_q3_edge": q2_q3,
        "q2_q3_is_unique_max_edge": bool(
            q2_q3 is not None
            and len(max_edges) == 1
            and max_edges[0]["surah_a"] == 2
            and max_edges[0]["surah_b"] == 3
        ),
    }


def build_positive_control(
    n_surahs: int,
    n_names: int,
    observed_row_sums: np.ndarray,
    seed: int,
) -> np.ndarray:
    rng = random.Random(seed)
    B = np.zeros((n_surahs, n_names), dtype=np.uint8)

    block_cols = [
        list(range(0, 16)),
        list(range(16, 32)),
        list(range(32, 48)),
    ]
    common_cols = list(range(48, 58))
    planted_pair = {55, 56}
    planted_core = list(range(0, min(20, n_names)))

    for r in range(n_surahs):
        target = max(1, int(observed_row_sums[r]))
        if r in planted_pair:
            target = max(target, len(planted_core))
            picks = set(planted_core)
            available = [c for c in range(n_names) if c not in picks]
            extra = target - len(picks)
            if extra > 0:
                picks.update(rng.sample(available, extra))
            for c in picks:
                B[r, c] = 1
            continue

        block_id = min(r // 38, 2)
        block_pool = block_cols[block_id]
        outside_pool = [c for c in range(n_names) if c not in block_pool]
        n_block = min(len(block_pool), max(2, round(target * 0.7)))
        n_common = min(len(common_cols), max(1, round(target * 0.2)))
        n_outside = max(0, target - n_block - n_common)

        picks = set(rng.sample(block_pool, n_block))
        available_common = [c for c in common_cols if c not in picks]
        if available_common and n_common > 0:
            picks.update(rng.sample(available_common, min(n_common, len(available_common))))
        available_outside = [c for c in outside_pool if c not in picks]
        if available_outside and n_outside > 0:
            picks.update(rng.sample(available_outside, min(n_outside, len(available_outside))))

        while len(picks) < target:
            picks.add(rng.randrange(n_names))
        for c in picks:
            B[r, c] = 1
    return B


def init_worker(B: np.ndarray) -> None:
    global _WORKER_B
    _WORKER_B = B


def run_chunk(task: tuple[int, int]) -> tuple[int, np.ndarray]:
    start, size = task
    if _WORKER_B is None:
        raise RuntimeError("worker matrix not initialized")
    out = np.empty((size, 1), dtype=np.int16)
    for offset in range(size):
        perm_idx = start + offset
        rng = random.Random(SEED + perm_idx)
        Bn = swap_randomize_fixed_margins(_WORKER_B, rng)
        Wn = weighted_projection(Bn)
        out[offset, 0] = max_shared_names(Wn)
    return start, out


def permutation_null(B: np.ndarray, n_perm: int) -> np.ndarray:
    null = np.empty(n_perm, dtype=np.int16)
    tasks = [
        (start, min(CHUNK_SIZE, n_perm - start))
        for start in range(0, n_perm, CHUNK_SIZE)
    ]
    print(
        f"[h-new-283] starting null: n_perm={n_perm}, workers={MAX_WORKERS}, chunk_size={CHUNK_SIZE}",
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
                null[start : start + chunk.shape[0]] = chunk[:, 0]
                completed += chunk.shape[0]
                if completed % 500 == 0 or completed == n_perm:
                    print(f"[h-new-283] completed {completed}/{n_perm}", flush=True)
    except PermissionError:
        print("[h-new-283] process pool denied; falling back to serial execution", flush=True)
        init_worker(B)
        for task in tasks:
            start, chunk = run_chunk(task)
            null[start : start + chunk.shape[0]] = chunk[:, 0]
            completed += chunk.shape[0]
            if completed % 500 == 0 or completed == n_perm:
                print(f"[h-new-283] completed {completed}/{n_perm}", flush=True)
    return null


def evaluate_matrix(B: np.ndarray, rng_seed: int, n_perm: int) -> dict[str, Any]:
    W = weighted_projection(B)
    summary = summarize_projection(W)
    null = permutation_null(B, n_perm=n_perm)
    M_obs = float(summary["M_max_shared_names"])
    p_M, ge_M = empirical_upper_p(null, M_obs)
    return {
        "summary": summary,
        "null": {
            "M_mean": float(np.mean(null)),
            "M_sd": float(np.std(null, ddof=1)),
            "p_M": float(p_M),
            "ge_count": int(ge_M),
            "mc_se_p_M": float(binomial_mc_se(p_M, len(null))),
        },
    }


def verdict(primary_pass: bool, mw5_pass: bool) -> str:
    if not mw5_pass:
        return "PIPELINE-BROKEN"
    return "MAX-EDGE-PASS" if primary_pass else "MAX-EDGE-NO-PASS"


def main() -> None:
    attested_names, B = load_surah_name_sets(DIVINE_CSV)
    prereg_sha = sha256_hex(PREREG)

    print("[observed] starting null", flush=True)
    observed = evaluate_matrix(B, rng_seed=SEED, n_perm=N_PERM)

    row_sums = B.sum(axis=1)
    pos_B = build_positive_control(
        n_surahs=B.shape[0],
        n_names=B.shape[1],
        observed_row_sums=row_sums,
        seed=SEED + 1,
    )
    print("[mw5] starting null", flush=True)
    mw5 = evaluate_matrix(pos_B, rng_seed=SEED + 2, n_perm=N_PERM_MW5)

    primary_pass = observed["null"]["p_M"] < ALPHA
    mw5_pass = mw5["null"]["p_M"] < 0.05

    out = {
        "id": "H-NEW-283",
        "title": "Divine-name surah max-edge under fixed-margin null",
        "parent_hypothesis": "H-NEW-263",
        "follow_up": "H-NEW-276",
        "seed": SEED,
        "pre_reg_sha256": prereg_sha,
        "source_csv": str(DIVINE_CSV),
        "n_surahs": int(B.shape[0]),
        "n_attested_names": int(len(attested_names)),
        "n_perm": N_PERM,
        "accepted_swaps_per_perm": ACCEPTED_SWAPS_PER_PERM,
        "alpha": ALPHA,
        "observed": {
            "M_obs": int(observed["summary"]["M_max_shared_names"]),
            "M_null_mean": observed["null"]["M_mean"],
            "M_null_sd": observed["null"]["M_sd"],
            "M_p_upper": observed["null"]["p_M"],
            "M_ge_count": observed["null"]["ge_count"],
            "mc_se_p_M": observed["null"]["mc_se_p_M"],
            "primary_pass_alpha_0_025": primary_pass,
            "top_edges": observed["summary"]["top_edges"],
            "max_edges": observed["summary"]["max_edges"],
            "max_edge_count": observed["summary"]["max_edge_count"],
            "q2_q3_edge": observed["summary"]["q2_q3_edge"],
            "q2_q3_is_unique_max_edge": observed["summary"]["q2_q3_is_unique_max_edge"],
        },
        "mw5_positive_control": {
            "description": "Synthetic planted-pair incidence matrix from the parent-line control family",
            "M_obs": int(mw5["summary"]["M_max_shared_names"]),
            "M_null_mean": mw5["null"]["M_mean"],
            "M_null_sd": mw5["null"]["M_sd"],
            "M_p_upper": mw5["null"]["p_M"],
            "M_ge_count": mw5["null"]["ge_count"],
            "pass": mw5_pass,
        },
        "verdict": verdict(primary_pass, mw5_pass),
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"wrote {OUT_JSON}")
    print(f"M_obs = {out['observed']['M_obs']}")
    print(f"p_upper = {out['observed']['M_p_upper']:.6f}")
    print(
        f"q2_q3_unique_max_edge = {out['observed']['q2_q3_is_unique_max_edge']}"
    )
    print(f"mw5 pass = {out['mw5_positive_control']['pass']}")
    print(f"verdict = {out['verdict']}")


if __name__ == "__main__":
    main()
