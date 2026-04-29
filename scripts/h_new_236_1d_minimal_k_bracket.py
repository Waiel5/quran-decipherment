#!/usr/bin/env python3
"""H-NEW-236.1d - Minimal-K bracket search for strict 4/4 closure.

Pre-reg:
  findings/phase-b-hypotheses/h-new-236-1d-minimal-k-bracket-prereg.md

Parent context:
  - H-NEW-236.1a: K=30 and K=50 close L_path but not mufaṣṣal-short.
  - H-NEW-236.1b: K=100 is sufficient for strict 4/4 closure.
  - H-NEW-236.1c: targeted Juz30 hinges close locally but overcorrect globally.

This run narrows the parsimony bracket by testing a locked K-grid around
the first mufaṣṣal-short entry in the hinge ranking.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import statistics
from pathlib import Path

SEED = 20260421
N_SIM = 1000
N_RANDOM = 1000
SA_ITERS = 200
T_HOT = 0.05
T_COLD = 0.001

CONTROL_K = 50
TESTED_KS = [73, 80, 85, 90, 95, 100]

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H111_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = (
    PROJECT_ROOT
    / "findings/phase-b-hypotheses/h-new-236-1d-minimal-k-bracket-prereg.md"
)
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1d.json"

BLOCKS_1INDEXED = {
    "fatiha": list(range(1, 2)),
    "tiwal": list(range(2, 10)),
    "middle_pre_hm": list(range(10, 40)),
    "hawamim": list(range(40, 47)),
    "middle_post_hm": list(range(47, 49)),
    "mufassal_long": list(range(49, 78)),
    "mufassal_short": list(range(78, 115)),
}

BLOCK_ORDER = [
    "fatiha",
    "tiwal",
    "middle_pre_hm",
    "hawamim",
    "middle_post_hm",
    "mufassal_long",
    "mufassal_short",
]

SURAH_TO_BLOCK = {
    surah: block_name
    for block_name, surahs in BLOCKS_1INDEXED.items()
    for surah in surahs
}


def prereg_sha256() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def load_d_matrix() -> list[list[float]]:
    with H111_JSON.open() as f:
        parent = json.load(f)
    dmat = [[0.0] * 114 for _ in range(114)]
    for i, j, d in parent["D_matrix_upper_triangular"]:
        dmat[i - 1][j - 1] = float(d)
        dmat[j - 1][i - 1] = float(d)
    return dmat


def canonical_edge_ranking(dmat: list[list[float]]) -> list[dict]:
    ranked = []
    for surah in range(1, 114):
        next_surah = surah + 1
        block_a = SURAH_TO_BLOCK[surah]
        block_b = SURAH_TO_BLOCK[next_surah]
        ranked.append(
            {
                "rank": None,
                "a": surah,
                "b": next_surah,
                "distance": float(dmat[surah - 1][next_surah - 1]),
                "block_a": block_a,
                "block_b": block_b,
                "cross_block": block_a != block_b,
            }
        )
    ranked.sort(key=lambda row: row["distance"], reverse=True)
    for rank, row in enumerate(ranked, start=1):
        row["rank"] = rank
    return ranked


def mufassal_short_internal_ranking(global_ranked: list[dict]) -> list[dict]:
    return [
        row
        for row in global_ranked
        if 78 <= row["a"] <= 113
        and row["b"] == row["a"] + 1
        and row["block_a"] == "mufassal_short"
        and row["block_b"] == "mufassal_short"
    ]


def top_k_hinges(global_ranked: list[dict], k: int) -> list[tuple[int, int]]:
    return [(row["a"], row["b"]) for row in global_ranked[:k]]


def classify_hinges(
    hinges_1indexed: list[tuple[int, int]]
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    cross = []
    within = []
    for a, b in hinges_1indexed:
        if SURAH_TO_BLOCK[a] == SURAH_TO_BLOCK[b]:
            within.append((a - 1, b - 1))
        else:
            cross.append((a - 1, b - 1))
    return within, cross


def path_length(tour: list[int], dmat: list[list[float]]) -> float:
    total = 0.0
    for i in range(len(tour) - 1):
        total += dmat[tour[i]][tour[i + 1]]
    return total


def wrap_edge(tour: list[int], dmat: list[list[float]]) -> float:
    return dmat[tour[-1]][tour[0]]


def tail_cost(tour: list[int], dmat: list[list[float]], start_pos: int = 90) -> float:
    total = 0.0
    for i in range(start_pos, len(tour) - 1):
        total += dmat[tour[i]][tour[i + 1]]
    return total


def block_cost(tour: list[int], dmat: list[list[float]], positions: list[int]) -> float:
    total = 0.0
    for a, b in zip(positions, positions[1:]):
        if b == a + 1:
            total += dmat[tour[a]][tour[b]]
    return total


def compute_observables(tour: list[int], dmat: list[list[float]]) -> dict:
    return {
        "L_path": path_length(tour, dmat),
        "W_wrap": wrap_edge(tour, dmat),
        "L_tiwal": block_cost(tour, dmat, list(range(1, 9))),
        "L_hawamim": block_cost(tour, dmat, list(range(39, 46))),
        "L_mufassal_short": block_cost(tour, dmat, list(range(77, 114))),
        "L_tail_91_114": tail_cost(tour, dmat, start_pos=90),
    }


def verify_hinges(tour: list[int], hinges_0indexed: list[tuple[int, int]]) -> dict:
    pos = {surah: idx for idx, surah in enumerate(tour)}
    return {(a + 1, b + 1): pos[b] == pos[a] + 1 for a, b in hinges_0indexed}


def all_hinges_ok(tour: list[int], hinges_0indexed: list[tuple[int, int]]) -> bool:
    return all(verify_hinges(tour, hinges_0indexed).values())


def build_hinge_chains_for_block(
    block_members: list[int], within_hinges: list[tuple[int, int]]
) -> list[list[int]]:
    in_block = set(block_members)
    succ: dict[int, int] = {}
    pred: dict[int, int] = {}
    for a, b in within_hinges:
        if a in in_block and b in in_block:
            if a in succ:
                raise AssertionError(f"Conflict: Q {a + 1} has two successors")
            if b in pred:
                raise AssertionError(f"Conflict: Q {b + 1} has two predecessors")
            succ[a] = b
            pred[b] = a

    chains: list[list[int]] = []
    visited: set[int] = set()
    for surah in block_members:
        if surah in visited or surah in pred:
            continue
        chain = [surah]
        visited.add(surah)
        cur = surah
        while cur in succ:
            nxt = succ[cur]
            chain.append(nxt)
            visited.add(nxt)
            cur = nxt
        chains.append(chain)

    for surah in block_members:
        if surah not in visited:
            chain = [surah]
            visited.add(surah)
            cur = surah
            while cur in succ and succ[cur] not in visited:
                nxt = succ[cur]
                chain.append(nxt)
                visited.add(nxt)
                cur = nxt
            chains.append(chain)

    return chains


def cross_block_maps(
    cross_hinges: list[tuple[int, int]]
) -> tuple[dict[str, int], dict[str, int]]:
    incoming_head_by_block: dict[str, int] = {}
    outgoing_tail_by_block: dict[str, int] = {}
    for a0, b0 in cross_hinges:
        a = a0 + 1
        b = b0 + 1
        block_a = SURAH_TO_BLOCK[a]
        block_b = SURAH_TO_BLOCK[b]
        incoming_head_by_block[block_b] = b0
        outgoing_tail_by_block[block_a] = a0
    return incoming_head_by_block, outgoing_tail_by_block


def initial_hinge_respecting_tour(
    rng: random.Random,
    within_hinges: list[tuple[int, int]],
    cross_hinges: list[tuple[int, int]],
    all_hinges: list[tuple[int, int]],
) -> list[int]:
    incoming_head_by_block, outgoing_tail_by_block = cross_block_maps(cross_hinges)
    tour_0indexed: list[int] = []

    for block_name in BLOCK_ORDER:
        members = [surah - 1 for surah in BLOCKS_1INDEXED[block_name]]
        chains = build_hinge_chains_for_block(members, within_hinges)
        chain_by_member = {member: chain for chain in chains for member in chain}

        start_chain = None
        end_chain = None
        if block_name in incoming_head_by_block:
            head = incoming_head_by_block[block_name]
            start_chain = chain_by_member[head]
            if start_chain[0] != head:
                raise AssertionError(
                    f"{block_name}: incoming head Q {head + 1} is not chain-start"
                )
        if block_name in outgoing_tail_by_block:
            tail = outgoing_tail_by_block[block_name]
            end_chain = chain_by_member[tail]
            if end_chain[-1] != tail:
                raise AssertionError(
                    f"{block_name}: outgoing tail Q {tail + 1} is not chain-end"
                )

        if start_chain is not None and end_chain is not None and start_chain is end_chain:
            if len(chains) != 1:
                raise AssertionError(
                    f"{block_name}: single chain would need to be both first and last"
                )
            ordered_chains = [start_chain]
        else:
            remaining = [c for c in chains if c is not start_chain and c is not end_chain]
            rng.shuffle(remaining)
            ordered_chains = []
            if start_chain is not None:
                ordered_chains.append(start_chain)
            ordered_chains.extend(remaining)
            if end_chain is not None:
                ordered_chains.append(end_chain)

        for chain in ordered_chains:
            tour_0indexed.extend(chain)

    if len(tour_0indexed) != 114:
        raise AssertionError(f"Tour has {len(tour_0indexed)} surahs, expected 114")
    if not all_hinges_ok(tour_0indexed, all_hinges):
        failed = {k: v for k, v in verify_hinges(tour_0indexed, all_hinges).items() if not v}
        raise AssertionError(f"Initial tour violates hinges: {failed}")
    return tour_0indexed


def within_block_positions() -> dict[str, list[int]]:
    pos_ranges: dict[str, list[int]] = {}
    offset = 0
    for block_name in BLOCK_ORDER:
        n_members = len(BLOCKS_1INDEXED[block_name])
        pos_ranges[block_name] = list(range(offset, offset + n_members))
        offset += n_members
    return pos_ranges


POSITION_RANGES = within_block_positions()


def swap_breaks_hinge(
    tour: list[int], pa: int, pb: int, hinge_set: set[tuple[int, int]]
) -> bool:
    if pa - 1 >= 0 and (tour[pa - 1], tour[pa]) in hinge_set:
        return True
    if pb + 1 < len(tour) and (tour[pb], tour[pb + 1]) in hinge_set:
        return True
    for i in range(pa, pb):
        if (tour[i], tour[i + 1]) in hinge_set:
            return True
    return False


def valid_pairs_for_sa() -> list[tuple[int, int]]:
    pairs = []
    for block_name, positions in POSITION_RANGES.items():
        if block_name == "fatiha":
            continue
        for idx_a in range(len(positions)):
            for idx_b in range(idx_a + 1, len(positions)):
                pairs.append((positions[idx_a], positions[idx_b]))
    return pairs


VALID_PAIRS = valid_pairs_for_sa()


def sa_within_block_hinge_respecting(
    tour: list[int],
    dmat: list[list[float]],
    rng: random.Random,
    hinge_set: set[tuple[int, int]],
    n_iters: int = SA_ITERS,
) -> tuple[list[int], dict]:
    current = list(tour)
    current_len = path_length(current, dmat)
    accept_count = 0
    reject_by_hinge = 0
    reject_by_sa = 0

    working_pairs = list(VALID_PAIRS)
    for it in range(n_iters):
        frac = it / max(1, n_iters - 1)
        temperature = T_HOT + frac * (T_COLD - T_HOT)
        rng.shuffle(working_pairs)
        batch_size = min(300, len(working_pairs))
        for pa, pb in working_pairs[:batch_size]:
            if swap_breaks_hinge(current, pa, pb, hinge_set):
                reject_by_hinge += 1
                continue

            left = current[pa - 1] if pa - 1 >= 0 else None
            right = current[pb + 1] if pb + 1 < len(current) else None
            if left is None or right is None:
                continue

            a = current[pa]
            b = current[pb]
            old_cost = dmat[left][a] + dmat[b][right]
            new_cost = dmat[left][b] + dmat[a][right]
            delta = new_cost - old_cost

            if delta < 0:
                current[pa : pb + 1] = current[pa : pb + 1][::-1]
                current_len += delta
                accept_count += 1
                continue

            if temperature > 1e-9:
                p_accept = math.exp(-delta / temperature) if delta / temperature < 50 else 0.0
            else:
                p_accept = 0.0

            if rng.random() < p_accept:
                current[pa : pb + 1] = current[pa : pb + 1][::-1]
                current_len += delta
                accept_count += 1
            else:
                reject_by_sa += 1

    return current, {
        "accepted": accept_count,
        "rejected_by_hinge": reject_by_hinge,
        "rejected_by_sa": reject_by_sa,
        "final_length": current_len,
    }


def percentile_of(value: float, distribution: list[float]) -> float:
    rank = sum(1 for v in distribution if v <= value)
    return 100.0 * rank / len(distribution)


def ci_95(distribution: list[float]) -> tuple[float, float]:
    s = sorted(distribution)
    n = len(s)
    lo_idx = int(0.025 * n)
    hi_idx = max(int(0.975 * n) - 1, 0)
    return s[lo_idx], s[hi_idx]


def summarize_distribution(values: list[float]) -> dict:
    lo, hi = ci_95(values)
    return {
        "mean": statistics.mean(values),
        "stdev": statistics.pstdev(values),
        "min": min(values),
        "max": max(values),
        "q025": lo,
        "q975": hi,
    }


def safe_z(value: float, mean: float, std: float) -> float:
    if std == 0.0:
        if value == mean:
            return 0.0
        return math.copysign(float("inf"), value - mean)
    return (value - mean) / std


def observable_analysis(empirical: float, sim_values: list[float], rand_values: list[float]) -> dict:
    sim_lo, sim_hi = ci_95(sim_values)
    rand_lo, rand_hi = ci_95(rand_values)
    return {
        "empirical": empirical,
        "sim_mean": statistics.mean(sim_values),
        "sim_std": statistics.pstdev(sim_values),
        "sim_ci_lo": sim_lo,
        "sim_ci_hi": sim_hi,
        "sim_percentile_of_empirical": percentile_of(empirical, sim_values),
        "sim_inside_95ci": sim_lo <= empirical <= sim_hi,
        "rand_mean": statistics.mean(rand_values),
        "rand_std": statistics.pstdev(rand_values),
        "rand_ci_lo": rand_lo,
        "rand_ci_hi": rand_hi,
        "rand_percentile_of_empirical": percentile_of(empirical, rand_values),
        "rand_inside_95ci": rand_lo <= empirical <= rand_hi,
    }


def block_chi2(empirical_obs: dict, sim_results: list[dict], rand_results: list[dict]) -> dict:
    block_keys = ["L_tiwal", "L_hawamim", "L_mufassal_short"]
    sim_means = {key: statistics.mean(row[key] for row in sim_results) for key in block_keys}
    sim_stds = {key: statistics.pstdev(row[key] for row in sim_results) for key in block_keys}
    rand_means = {key: statistics.mean(row[key] for row in rand_results) for key in block_keys}
    rand_stds = {key: statistics.pstdev(row[key] for row in rand_results) for key in block_keys}

    empirical_stat_sim = 0.0
    empirical_stat_rand = 0.0
    per_block = {}
    for key in block_keys:
        z_sim = safe_z(empirical_obs[key], sim_means[key], sim_stds[key])
        z_rand = safe_z(empirical_obs[key], rand_means[key], rand_stds[key])
        empirical_stat_sim += z_sim * z_sim if math.isfinite(z_sim) else 0.0
        empirical_stat_rand += z_rand * z_rand if math.isfinite(z_rand) else 0.0
        per_block[key] = {
            "empirical": empirical_obs[key],
            "sim_mean": sim_means[key],
            "sim_std": sim_stds[key],
            "sim_z": z_sim,
            "sim_z2": z_sim * z_sim if math.isfinite(z_sim) else float("inf"),
            "rand_mean": rand_means[key],
            "rand_std": rand_stds[key],
            "rand_z": z_rand,
            "rand_z2": z_rand * z_rand if math.isfinite(z_rand) else float("inf"),
        }

    sim_stats = []
    rand_stats = []
    for row in sim_results:
        stat = 0.0
        for key in block_keys:
            z = safe_z(row[key], sim_means[key], sim_stds[key])
            if math.isfinite(z):
                stat += z * z
        sim_stats.append(stat)
    for row in rand_results:
        stat = 0.0
        for key in block_keys:
            z = safe_z(row[key], rand_means[key], rand_stds[key])
            if math.isfinite(z):
                stat += z * z
        rand_stats.append(stat)

    sim_97_5 = sorted(sim_stats)[max(int(0.975 * len(sim_stats)) - 1, 0)]
    rand_97_5 = sorted(rand_stats)[max(int(0.975 * len(rand_stats)) - 1, 0)]
    return {
        "empirical_stat_under_sim": empirical_stat_sim,
        "empirical_stat_under_rand": empirical_stat_rand,
        "sim_97_5th_pct": sim_97_5,
        "rand_97_5th_pct": rand_97_5,
        "sim_percentile_of_empirical": percentile_of(empirical_stat_sim, sim_stats),
        "rand_percentile_of_empirical": percentile_of(empirical_stat_rand, rand_stats),
        "sim_inside_95ci": empirical_stat_sim <= sim_97_5,
        "rand_inside_95ci": empirical_stat_rand <= rand_97_5,
        "sim_block_means": sim_means,
        "sim_block_stds": sim_stds,
        "rand_block_means": rand_means,
        "rand_block_stds": rand_stds,
        "per_block": per_block,
    }


def simulate_random(rand_idx: int, dmat: list[list[float]]) -> dict:
    rng = random.Random(SEED + 900_000 + rand_idx)
    perm = list(range(114))
    rng.shuffle(perm)
    obs = compute_observables(perm, dmat)
    obs["rand_idx"] = rand_idx
    return obs


def run_cell(
    cell_name: str,
    seed_offset: int,
    k: int,
    hinges_1indexed: list[tuple[int, int]],
    dmat: list[list[float]],
) -> dict:
    within_hinges, cross_hinges = classify_hinges(hinges_1indexed)
    hinges_0indexed = [(a - 1, b - 1) for a, b in hinges_1indexed]
    hinge_set = set(hinges_0indexed)

    sim_results = []
    sa_stats = []
    for sim_idx in range(N_SIM):
        rng = random.Random(SEED + seed_offset + sim_idx)
        init = initial_hinge_respecting_tour(rng, within_hinges, cross_hinges, hinges_0indexed)
        final, stats = sa_within_block_hinge_respecting(init, dmat, rng, hinge_set)
        if not all_hinges_ok(final, hinges_0indexed):
            failed = {k: v for k, v in verify_hinges(final, hinges_0indexed).items() if not v}
            raise AssertionError(f"{cell_name}: hinge verification failed for sim {sim_idx}: {failed}")
        obs = compute_observables(final, dmat)
        obs["sim_idx"] = sim_idx
        sim_results.append(obs)
        sa_stats.append(stats)

    return {
        "k": k,
        "hinges_1indexed": hinges_1indexed,
        "within_hinges_1indexed": [(a + 1, b + 1) for a, b in within_hinges],
        "cross_hinges_1indexed": [(a + 1, b + 1) for a, b in cross_hinges],
        "sim_results": sim_results,
        "sa_summary": {
            "accepted_mean": statistics.mean(row["accepted"] for row in sa_stats),
            "accepted_min": min(row["accepted"] for row in sa_stats),
            "accepted_max": max(row["accepted"] for row in sa_stats),
            "rejected_by_hinge_mean": statistics.mean(row["rejected_by_hinge"] for row in sa_stats),
            "rejected_by_sa_mean": statistics.mean(row["rejected_by_sa"] for row in sa_stats),
        },
    }


def analyze_cell(cell_run: dict, empirical: dict, rand_results: list[dict]) -> dict:
    sim_results = cell_run["sim_results"]
    full_analysis = {}
    for obs_name in ["L_path", "W_wrap", "L_tiwal", "L_hawamim", "L_mufassal_short", "L_tail_91_114"]:
        full_analysis[obs_name] = observable_analysis(
            empirical[obs_name],
            [row[obs_name] for row in sim_results],
            [row[obs_name] for row in rand_results],
        )
    block_stat = block_chi2(empirical, sim_results, rand_results)

    pass_strict_4of4 = bool(
        full_analysis["L_path"]["sim_inside_95ci"]
        and full_analysis["W_wrap"]["sim_inside_95ci"]
        and block_stat["sim_inside_95ci"]
        and full_analysis["L_tail_91_114"]["sim_inside_95ci"]
    )
    mufassal_z = block_stat["per_block"]["L_mufassal_short"]["sim_z"]
    mufassal_pct = full_analysis["L_mufassal_short"]["sim_percentile_of_empirical"]
    mufassal_inside = full_analysis["L_mufassal_short"]["sim_inside_95ci"]

    if pass_strict_4of4:
        verdict = "STRICT-4/4-PASS"
    elif mufassal_inside:
        verdict = "LOCAL-BLOCK-PASS-GLOBAL-FAIL"
    else:
        verdict = "NULL"

    sim_passes = sum(
        [
            full_analysis["L_path"]["sim_inside_95ci"],
            full_analysis["W_wrap"]["sim_inside_95ci"],
            block_stat["sim_inside_95ci"],
            full_analysis["L_tail_91_114"]["sim_inside_95ci"],
        ]
    )

    return {
        "full_analysis": full_analysis,
        "block_chi2": block_stat,
        "sim_passes": sim_passes,
        "pass_strict_4of4": pass_strict_4of4,
        "mufassal_short_sim_z": mufassal_z,
        "mufassal_short_sim_percentile": mufassal_pct,
        "cell_verdict": verdict,
        "sim_summaries": {
            key: summarize_distribution([row[key] for row in sim_results])
            for key in ["L_path", "W_wrap", "L_tiwal", "L_hawamim", "L_mufassal_short", "L_tail_91_114"]
        },
        "sa_summary": cell_run["sa_summary"],
        "sim_samples": sim_results[:25],
    }


def main() -> None:
    print("=" * 78)
    print("H-NEW-236.1d - Minimal-K bracket search for strict 4/4 closure")
    print("=" * 78)
    print(f"Seed={SEED}; N_SIM={N_SIM}; N_RANDOM={N_RANDOM}; SA_ITERS={SA_ITERS}")
    print(f"Control K={CONTROL_K}; Tested K grid={TESTED_KS}")

    dmat = load_d_matrix()
    prereg_hash = prereg_sha256()
    ranked = canonical_edge_ranking(dmat)
    mufassal_internal = mufassal_short_internal_ranking(ranked)
    first_mufassal_internal_rank = mufassal_internal[0]["rank"]
    if first_mufassal_internal_rank != 73:
        raise AssertionError(
            f"Expected first mufaṣṣal-short internal rank 73, observed {first_mufassal_internal_rank}"
        )

    print(f"Pre-reg SHA-256: {prereg_hash}")
    print(
        "First mufaṣṣal-short internal edge enters ranking at "
        f"rank {first_mufassal_internal_rank}: "
        f"Q {mufassal_internal[0]['a']}->{mufassal_internal[0]['b']}"
    )

    empirical_tour = list(range(114))
    empirical = compute_observables(empirical_tour, dmat)
    print("\nEmpirical observables:")
    for key, value in empirical.items():
        print(f"  {key:22s} = {value:.6f}")

    print("\nRunning shared random null...")
    rand_results = []
    for idx in range(N_RANDOM):
        rand_results.append(simulate_random(idx, dmat))
        if (idx + 1) % 250 == 0:
            print(f"  random {idx + 1}/{N_RANDOM}")

    cell_specs = [("mw5_positive_control_top50", CONTROL_K, 0)]
    for offset_idx, k in enumerate(TESTED_KS, start=1):
        cell_specs.append((f"cell_top{k}", k, offset_idx * 100_000))

    cells = {}
    for cell_name, k, seed_offset in cell_specs:
        hinges = top_k_hinges(ranked, k)
        mufassal_included = [
            row for row in mufassal_internal if row["rank"] <= k
        ]
        print(
            f"\n-- Running {cell_name} (K={k}, |hinges|={len(hinges)}, "
            f"mufassal_internal_included={len(mufassal_included)})..."
        )
        cell_run = run_cell(cell_name, seed_offset, k, hinges, dmat)
        analysis = analyze_cell(cell_run, empirical, rand_results)
        cells[cell_name] = {
            "k": k,
            "hinge_count": len(hinges),
            "hinges_1indexed": hinges,
            "within_hinges_1indexed": cell_run["within_hinges_1indexed"],
            "cross_hinges_1indexed": cell_run["cross_hinges_1indexed"],
            "mufassal_short_internal_edges_included": [
                {
                    "rank": row["rank"],
                    "a": row["a"],
                    "b": row["b"],
                    "distance": row["distance"],
                }
                for row in mufassal_included
            ],
            **analysis,
        }
        print(
            f"   verdict={analysis['cell_verdict']:27s} "
            f"sim_passes={analysis['sim_passes']}/4 "
            f"L_path_pct={analysis['full_analysis']['L_path']['sim_percentile_of_empirical']:6.2f} "
            f"Block_pct={analysis['block_chi2']['sim_percentile_of_empirical']:6.2f} "
            f"Tail_pct={analysis['full_analysis']['L_tail_91_114']['sim_percentile_of_empirical']:6.2f} "
            f"Muf_z={analysis['mufassal_short_sim_z']:+7.3f}"
        )

    control = cells["mw5_positive_control_top50"]
    control_ok = (
        not control["pass_strict_4of4"]
        and not control["full_analysis"]["L_mufassal_short"]["sim_inside_95ci"]
        and control["mufassal_short_sim_z"] > 2.0
    )

    strict_pass_ks = [
        cells[f"cell_top{k}"]["k"]
        for k in TESTED_KS
        if cells[f"cell_top{k}"]["pass_strict_4of4"]
    ]
    strict_fail_ks = [
        cells[f"cell_top{k}"]["k"]
        for k in TESTED_KS
        if not cells[f"cell_top{k}"]["pass_strict_4of4"]
    ]

    smallest_tested_strict_pass_k = min(strict_pass_ks) if strict_pass_ks else None
    non_monotonic_after_first_pass = False
    tested_bracket = None
    if smallest_tested_strict_pass_k is not None:
        later_failures = [k for k in TESTED_KS if k > smallest_tested_strict_pass_k and k in strict_fail_ks]
        non_monotonic_after_first_pass = bool(later_failures)

        lower_candidates = [CONTROL_K]
        lower_candidates.extend(
            [k for k in TESTED_KS if k < smallest_tested_strict_pass_k and k in strict_fail_ks]
        )
        lower_exclusive = max(lower_candidates)
        tested_bracket = {
            "lower_exclusive": lower_exclusive,
            "upper_inclusive": smallest_tested_strict_pass_k,
            "label": f"({lower_exclusive}, {smallest_tested_strict_pass_k}]",
            "non_monotonic_after_first_pass": non_monotonic_after_first_pass,
        }

    print(
        f"\nMW-5 positive control top-50 status: {'OK' if control_ok else 'FAIL'} "
        f"(strict_pass={control['pass_strict_4of4']}, "
        f"mufassal_inside={control['full_analysis']['L_mufassal_short']['sim_inside_95ci']}, "
        f"z={control['mufassal_short_sim_z']:+.3f})"
    )
    print(f"Strict-pass Ks: {strict_pass_ks}")
    print(f"Strict-fail Ks: {strict_fail_ks}")
    print(f"Smallest tested strict-pass K: {smallest_tested_strict_pass_k}")
    print(f"Tested bracket: {tested_bracket['label'] if tested_bracket else 'none'}")

    output = {
        "finding_id": "h-new-236-1d",
        "title": "Minimal-K bracket search for strict 4/4 closure under top-K hinge extension",
        "date": "2026-04-18",
        "seed": SEED,
        "n_sim": N_SIM,
        "n_random": N_RANDOM,
        "sa_iters": SA_ITERS,
        "control_k": CONTROL_K,
        "tested_ks": TESTED_KS,
        "prereg_sha256": prereg_hash,
        "rules_tuple": (
            "(no-tashkeel, 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1, "
            "QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, "
            "stochastic 2-opt with classical-block + Q1-lock + length-stratification "
            "+ M2-muq + TOP-K-HINGE-PRESERVATION, seed 20260421)"
        ),
        "first_mufassal_short_internal_edge": {
            "rank": mufassal_internal[0]["rank"],
            "a": mufassal_internal[0]["a"],
            "b": mufassal_internal[0]["b"],
            "distance": mufassal_internal[0]["distance"],
        },
        "first_12_mufassal_short_internal_edges": [
            {
                "rank": row["rank"],
                "a": row["a"],
                "b": row["b"],
                "distance": row["distance"],
            }
            for row in mufassal_internal[:12]
        ],
        "empirical_observables": empirical,
        "mw5_positive_control_ok": control_ok,
        "strict_pass_ks": strict_pass_ks,
        "strict_fail_ks": strict_fail_ks,
        "smallest_tested_strict_pass_k": smallest_tested_strict_pass_k,
        "tested_bracket": tested_bracket,
        "cells": cells,
    }

    OUTPUT_JSON.write_text(json.dumps(output, indent=2))
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
