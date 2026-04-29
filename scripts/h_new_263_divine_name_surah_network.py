#!/usr/bin/env python3
"""H-NEW-263 — divine-name surah-overlap network.

Locked pre-reg:
  findings/phase-b-hypotheses/h-new-263-divine-name-surah-network-prereg.md

Observed data:
  findings/phase-b-hypotheses/divine-names-by-verse.csv

Outputs:
  findings/phase-b-hypotheses/csv/h-new-263.json
"""

from __future__ import annotations

import csv
import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path("/Users/grey/Downloads/quran")
DIVINE_CSV = ROOT / "findings" / "phase-b-hypotheses" / "divine-names-by-verse.csv"
NAMES_TXT = ROOT / "data" / "asma-al-husna.txt"
PREREG = (
    ROOT
    / "findings"
    / "phase-b-hypotheses"
    / "h-new-263-divine-name-surah-network-prereg.md"
)
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-263.json"

SEED = 20260418
BONFERRONI_K = 2
ALPHA_BON = 0.05 / BONFERRONI_K
N_PERM = 300
N_PERM_MW5 = 120
ACCEPTED_SWAPS_PER_PERM = 500
HUB_THRESHOLD = 2
POS_CTRL_HUB_SURAH = 57


def sha256_hex(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_canonical_names(path: Path) -> list[str]:
    out: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        out.append(s)
    return out


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


def transitivity_from_adj(A: np.ndarray) -> float:
    A = A.astype(np.int64)
    deg = A.sum(axis=1)
    triples = int(((deg * (deg - 1)) // 2).sum())
    if triples == 0:
        return 0.0
    triangles = int(np.trace(A @ A @ A) // 6)
    return 3.0 * triangles / triples


def summarise_projection(W: np.ndarray) -> dict[str, Any]:
    triu = np.triu(W, 1)
    edge_mask = triu > 0
    edge_mask2 = triu >= HUB_THRESHOLD
    H = int((triu.astype(np.int64) ** 2).sum())
    strength = W.sum(axis=1).astype(float)
    A2 = (W >= HUB_THRESHOLD).astype(np.uint8)
    np.fill_diagonal(A2, 0)
    strength2 = (W * (W >= HUB_THRESHOLD)).sum(axis=1).astype(float)
    degree2 = A2.sum(axis=1).astype(int)
    trans2 = transitivity_from_adj(A2)

    top_edges = []
    for i in range(W.shape[0]):
        for j in range(i + 1, W.shape[1]):
            w = int(W[i, j])
            if w == 0:
                continue
            top_edges.append({"surah_a": i + 1, "surah_b": j + 1, "shared_names": w})
    top_edges.sort(key=lambda row: (-row["shared_names"], row["surah_a"], row["surah_b"]))

    top_strength = [
        {"surah": i + 1, "strength": int(v)}
        for i, v in sorted(enumerate(strength), key=lambda t: (-t[1], t[0]))[:10]
    ]
    top_strength2 = [
        {
            "surah": i + 1,
            "strength_ge2": int(strength2[i]),
            "degree_ge2": int(degree2[i]),
        }
        for i, _ in sorted(enumerate(strength2), key=lambda t: (-t[1], t[0]))[:10]
    ]

    return {
        "H_sum_w_sq": H,
        "edge_count_ge1": int(edge_mask.sum()),
        "edge_count_ge2": int(edge_mask2.sum()),
        "max_shared_names": int(triu.max()) if triu.size else 0,
        "strength": strength,
        "strength_ge2": strength2,
        "degree_ge2": degree2,
        "transitivity_ge2": float(trans2),
        "top_edges": top_edges[:15],
        "top_strength": top_strength,
        "top_strength_ge2": top_strength2,
    }


def permutation_null(
    B: np.ndarray,
    n_perm: int,
    rng: random.Random,
    label: str,
) -> dict[str, Any]:
    H_null = np.empty(n_perm, dtype=float)
    strength2_null = np.empty((n_perm, B.shape[0]), dtype=float)
    trans2_null = np.empty(n_perm, dtype=float)
    accepted_swap_counts: list[int] = []

    for i in range(n_perm):
        Bn = swap_randomize_fixed_margins(B, rng)
        accepted_swap_counts.append(ACCEPTED_SWAPS_PER_PERM)
        Wn = weighted_projection(Bn)
        summary = summarise_projection(Wn)
        H_null[i] = summary["H_sum_w_sq"]
        strength2_null[i, :] = summary["strength_ge2"]
        trans2_null[i] = summary["transitivity_ge2"]
        if (i + 1) % 50 == 0 or i + 1 == n_perm:
            print(f"[{label}] permutation {i + 1}/{n_perm}", flush=True)

    return {
        "H_null": H_null,
        "strength_ge2_null": strength2_null,
        "transitivity_ge2_null": trans2_null,
        "accepted_swaps_per_perm": accepted_swap_counts,
    }


def empirical_upper_p(null_values: np.ndarray, observed: float) -> float:
    ge = int(np.sum(null_values >= observed))
    return (1 + ge) / (len(null_values) + 1)


def hub_test(obs_strength2: np.ndarray, null_strength2: np.ndarray) -> dict[str, Any]:
    null_mean = null_strength2.mean(axis=0)
    null_sd = null_strength2.std(axis=0, ddof=1)
    null_sd = np.where(null_sd == 0, 1.0, null_sd)
    obs_z = (obs_strength2 - null_mean) / null_sd
    null_z = (null_strength2 - null_mean) / null_sd
    max_null_z = null_z.max(axis=1)
    z_max_obs = float(obs_z.max())
    p_exist = empirical_upper_p(max_null_z, z_max_obs)

    ranked = []
    for idx in np.argsort(-obs_z):
        sid = int(idx + 1)
        z = float(obs_z[idx])
        p_raw = empirical_upper_p(null_strength2[:, idx], float(obs_strength2[idx]))
        p_adj = empirical_upper_p(max_null_z, z)
        ranked.append(
            {
                "surah": sid,
                "strength_ge2_obs": int(obs_strength2[idx]),
                "null_mean": float(null_mean[idx]),
                "null_sd": float(null_sd[idx]),
                "z": z,
                "p_raw": float(p_raw),
                "p_adj_fwer": float(p_adj),
            }
        )
    return {
        "z_max_obs": z_max_obs,
        "p_exist": float(p_exist),
        "null_mean_per_surah": null_mean.tolist(),
        "null_sd_per_surah": null_sd.tolist(),
        "ranked_surahs": ranked[:15],
    }


def build_positive_control(
    n_surahs: int,
    n_names: int,
    observed_row_sums: np.ndarray,
    seed: int,
) -> np.ndarray:
    rng = random.Random(seed)
    B = np.zeros((n_surahs, n_names), dtype=np.uint8)

    block_rows = [
        list(range(0, 38)),
        list(range(38, 76)),
        list(range(76, 114)),
    ]
    block_cols = [
        list(range(0, 16)),
        list(range(16, 32)),
        list(range(32, 48)),
    ]
    common_cols = list(range(48, 58))
    hub_idx = POS_CTRL_HUB_SURAH - 1

    for r in range(n_surahs):
        target = max(1, int(observed_row_sums[r]))
        block_id = min(r // 38, 2)
        if r == hub_idx:
            picks = set()
            for cols in block_cols:
                picks.update(rng.sample(cols, min(5, len(cols))))
            picks.update(rng.sample(common_cols, 3))
            for c in sorted(picks)[: min(len(picks), n_names)]:
                B[r, c] = 1
            continue

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
            candidate = rng.randrange(n_names)
            picks.add(candidate)
        for c in picks:
            B[r, c] = 1
    return B


def evaluate_matrix(
    B: np.ndarray,
    rng_seed: int,
    n_perm: int,
    label: str,
) -> dict[str, Any]:
    W = weighted_projection(B)
    summary = summarise_projection(W)
    null = permutation_null(B, n_perm=n_perm, rng=random.Random(rng_seed), label=label)
    H_obs = float(summary["H_sum_w_sq"])
    p_H = empirical_upper_p(null["H_null"], H_obs)
    hub = hub_test(summary["strength_ge2"], null["strength_ge2_null"])
    return {
        "summary": summary,
        "null": {
            "H_mean": float(np.mean(null["H_null"])),
            "H_sd": float(np.std(null["H_null"], ddof=1)),
            "p_H": float(p_H),
            "transitivity_ge2_mean": float(np.mean(null["transitivity_ge2_null"])),
            "transitivity_ge2_sd": float(np.std(null["transitivity_ge2_null"], ddof=1)),
        },
        "hub": hub,
    }


def verdict(cell_a_pass: bool, cell_b_pass: bool, mw5_pass: bool) -> str:
    if not mw5_pass:
        return "PIPELINE-BROKEN"
    if cell_a_pass and cell_b_pass:
        return "PASS-STRUCTURE-AND-HUB"
    if cell_a_pass and not cell_b_pass:
        return "PASS-STRUCTURE-NO-HUB"
    if (not cell_a_pass) and cell_b_pass:
        return "HUB-ONLY"
    return "NULL"


def main() -> None:
    canonical_names = load_canonical_names(NAMES_TXT)
    attested_names, B = load_surah_name_sets(DIVINE_CSV)
    prereg_sha = sha256_hex(PREREG)

    print("[observed] starting null", flush=True)
    observed = evaluate_matrix(B, rng_seed=SEED, n_perm=N_PERM, label="observed")

    row_sums = B.sum(axis=1)
    pos_B = build_positive_control(
        n_surahs=B.shape[0],
        n_names=B.shape[1],
        observed_row_sums=row_sums,
        seed=SEED + 1,
    )
    print("[mw5] starting null", flush=True)
    mw5 = evaluate_matrix(pos_B, rng_seed=SEED + 2, n_perm=N_PERM_MW5, label="mw5")

    cell_a_pass = observed["null"]["p_H"] < ALPHA_BON
    cell_b_pass = observed["hub"]["p_exist"] < ALPHA_BON
    mw5_structure_pass = mw5["null"]["p_H"] < 0.05
    mw5_hub_pass = mw5["hub"]["p_exist"] < 0.05
    mw5_pass = mw5_structure_pass and mw5_hub_pass

    out = {
        "id": "H-NEW-263",
        "title": "Divine-name surah-overlap network",
        "seed": SEED,
        "pre_reg_sha256": prereg_sha,
        "source_csv": str(DIVINE_CSV),
        "n_surahs": 114,
        "n_canonical_names": len(canonical_names),
        "n_attested_names": len(attested_names),
        "n_perm": N_PERM,
        "n_perm_mw5": N_PERM_MW5,
        "accepted_swaps_per_perm": ACCEPTED_SWAPS_PER_PERM,
        "hub_threshold": HUB_THRESHOLD,
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "observed": {
            "H_sum_w_sq": int(observed["summary"]["H_sum_w_sq"]),
            "H_null_mean": observed["null"]["H_mean"],
            "H_null_sd": observed["null"]["H_sd"],
            "H_p_upper": observed["null"]["p_H"],
            "edge_count_ge1": int(observed["summary"]["edge_count_ge1"]),
            "edge_count_ge2": int(observed["summary"]["edge_count_ge2"]),
            "max_shared_names": int(observed["summary"]["max_shared_names"]),
            "transitivity_ge2": observed["summary"]["transitivity_ge2"],
            "transitivity_ge2_null_mean": observed["null"]["transitivity_ge2_mean"],
            "transitivity_ge2_null_sd": observed["null"]["transitivity_ge2_sd"],
            "cell_a_pass": cell_a_pass,
            "top_edges": observed["summary"]["top_edges"],
            "top_strength": observed["summary"]["top_strength"],
            "top_strength_ge2": observed["summary"]["top_strength_ge2"],
        },
        "hub_test": {
            "z_max_obs": observed["hub"]["z_max_obs"],
            "p_exist": observed["hub"]["p_exist"],
            "cell_b_pass": cell_b_pass,
            "ranked_surahs": observed["hub"]["ranked_surahs"],
        },
        "mw5_positive_control": {
            "description": (
                "Synthetic 3-block surah-name incidence matrix with one planted cross-block hub"
            ),
            "structure_p": mw5["null"]["p_H"],
            "hub_p": mw5["hub"]["p_exist"],
            "structure_pass_raw_0_05": mw5_structure_pass,
            "hub_pass_raw_0_05": mw5_hub_pass,
            "pass": mw5_pass,
            "H_sum_w_sq": int(mw5["summary"]["H_sum_w_sq"]),
            "edge_count_ge2": int(mw5["summary"]["edge_count_ge2"]),
            "top_strength_ge2": mw5["summary"]["top_strength_ge2"][:5],
            "hub_ranked_surahs": mw5["hub"]["ranked_surahs"][:5],
        },
        "verdict": verdict(cell_a_pass, cell_b_pass, mw5_pass),
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"wrote {OUT_JSON}")
    print(f"observed H = {out['observed']['H_sum_w_sq']}")
    print(f"observed p_H = {out['observed']['H_p_upper']:.6f}")
    print(f"observed hub p = {out['hub_test']['p_exist']:.6f}")
    print(f"mw5 pass = {out['mw5_positive_control']['pass']}")
    print(f"verdict = {out['verdict']}")


if __name__ == "__main__":
    main()
