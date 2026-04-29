#!/usr/bin/env python3
"""H-NEW-236.1f - Late-tail scaffold repair sweep.

Pre-reg:
  findings/phase-b-hypotheses/h-new-236-1f-tail-repair-scaffold-prereg.md

Parents:
  H-NEW-236.1c Cell A (top-50 + Juz' 30 top-5; local closure but global
  over-correction)
  H-NEW-236.1b M_H top-100 (strict terminal mechanism pass)

Design:
  Start from the exact H-NEW-236.1c Cell A hinge set and add only the
  late-tail M_H edges inside Q 91-114 in a locked cumulative order.
  The question is the first k where L_path and L_tail_91_114 re-enter
  the simulator 95% CI while L_mufassal_short and Block-chi2 stay inside.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import statistics
from pathlib import Path

SEED = 20260423
N_SIM = 1000
N_RANDOM = 1000
SA_ITERS = 200
T_HOT = 0.05
T_COLD = 0.001

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H111_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
H2361B_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1b.json"
H2361C_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1c.json"
PREREG = (
    PROJECT_ROOT
    / "findings/phase-b-hypotheses/h-new-236-1f-tail-repair-scaffold-prereg.md"
)
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1f.json"

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

CELL_A_NAME = "cell_a_top50_plus_j30_top5"
CELL_MH_NAME = "cell_M_H_top100"
LATE_TAIL_EDGES_1INDEXED = [
    (91, 92),
    (92, 93),
    (95, 96),
    (96, 97),
    (97, 98),
    (98, 99),
    (99, 100),
    (100, 101),
    (101, 102),
    (109, 110),
]


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


def load_parent_cells(dmat: list[list[float]]) -> dict:
    with H2361C_JSON.open() as f:
        data_c = json.load(f)
    with H2361B_JSON.open() as f:
        data_b = json.load(f)

    cell_a = data_c["cells"][CELL_A_NAME]
    cell_mh = data_b["cells"][CELL_MH_NAME]

    base_hinges = [tuple(pair) for pair in cell_a["hinges_1indexed"]]
    mh_hinges = {tuple(pair) for pair in cell_mh["hinges_1indexed"]}
    late_tail_set = set(LATE_TAIL_EDGES_1INDEXED)
    missing = [pair for pair in LATE_TAIL_EDGES_1INDEXED if pair not in mh_hinges]
    if missing:
        raise AssertionError(f"Late-tail edges missing from H-NEW-236.1b M_H: {missing}")

    rank_map = {
        (row["a"], row["b"]): row["rank"]
        for row in canonical_edge_ranking(dmat)
    }
    late_tail_ranks = [
        {
            "edge_1indexed": [a, b],
            "global_rank": rank_map[(a, b)],
            "distance": float(dmat[a - 1][b - 1]),
        }
        for a, b in LATE_TAIL_EDGES_1INDEXED
    ]

    mh_tail_edges = sorted(
        [pair for pair in mh_hinges if pair in late_tail_set],
        key=lambda pair: rank_map[pair],
    )

    return {
        "cell_a_hinges_1indexed": base_hinges,
        "cell_a_parent_metrics": {
            "L_path": cell_a["full_analysis"]["L_path"],
            "L_tail_91_114": cell_a["full_analysis"]["L_tail_91_114"],
            "L_mufassal_short": cell_a["full_analysis"]["L_mufassal_short"],
            "Block_chi2": cell_a["block_chi2"],
            "sim_passes": cell_a["sim_passes"],
            "cell_verdict": cell_a["cell_verdict"],
        },
        "cell_mh_metrics": {
            "L_path": cell_mh["full_analysis"]["L_path"],
            "L_tail_91_114": cell_mh["full_analysis"]["L_tail_91_114"],
            "L_mufassal_short": cell_mh["full_analysis"]["L_mufassal_short"],
            "Block_chi2": cell_mh["block_chi2"],
            "sim_passes": cell_mh["sim_passes"],
            "cell_verdict": cell_mh["cell_verdict"],
        },
        "mh_tail_edges_sorted_by_rank_1indexed": mh_tail_edges,
        "late_tail_edge_ranks": late_tail_ranks,
    }


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

    chains = []
    visited = set()
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
    n = len(tour)
    if pa - 1 >= 0 and (tour[pa - 1], tour[pa]) in hinge_set:
        return True
    if pb + 1 < n and (tour[pb], tour[pb + 1]) in hinge_set:
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


def dedup_hinges(hinges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    seen: set[tuple[int, int]] = set()
    out: list[tuple[int, int]] = []
    for pair in hinges:
        if pair in seen:
            continue
        seen.add(pair)
        out.append(pair)
    return out


def run_cell(
    cell_name: str,
    seed_offset: int,
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
        "within_hinges_1indexed": [(a + 1, b + 1) for a, b in within_hinges],
        "cross_hinges_1indexed": [(a + 1, b + 1) for a, b in cross_hinges],
        "hinges_1indexed": [list(pair) for pair in hinges_1indexed],
        "valid_pairs_count": len(VALID_PAIRS),
        "sim_results": sim_results,
        "sa_summary": {
            "accepted_mean": statistics.mean(row["accepted"] for row in sa_stats),
            "accepted_min": min(row["accepted"] for row in sa_stats),
            "accepted_max": max(row["accepted"] for row in sa_stats),
            "rejected_by_hinge_mean": statistics.mean(row["rejected_by_hinge"] for row in sa_stats),
            "rejected_by_sa_mean": statistics.mean(row["rejected_by_sa"] for row in sa_stats),
        },
    }


def analyze_cell(
    cell_run: dict,
    empirical: dict,
    rand_results: list[dict],
    late_tail_added: list[tuple[int, int]],
) -> dict:
    sim_results = cell_run["sim_results"]
    full_analysis = {}
    for obs_name in ["L_path", "W_wrap", "L_tiwal", "L_hawamim", "L_mufassal_short", "L_tail_91_114"]:
        full_analysis[obs_name] = observable_analysis(
            empirical[obs_name],
            [row[obs_name] for row in sim_results],
            [row[obs_name] for row in rand_results],
        )
    block_stat = block_chi2(empirical, sim_results, rand_results)

    l_path_inside = full_analysis["L_path"]["sim_inside_95ci"]
    l_tail_inside = full_analysis["L_tail_91_114"]["sim_inside_95ci"]
    l_muf_inside = full_analysis["L_mufassal_short"]["sim_inside_95ci"]
    block_inside = block_stat["sim_inside_95ci"]
    w_wrap_inside = full_analysis["W_wrap"]["sim_inside_95ci"]

    primary_repair_pass = bool(l_path_inside and l_tail_inside and l_muf_inside and block_inside)
    four_obs_family_pass = bool(
        l_path_inside and w_wrap_inside and block_inside and l_tail_inside
    )

    if primary_repair_pass:
        verdict = "TAIL-SCAFFOLD-REPAIR"
    elif l_muf_inside and block_inside and (not l_path_inside or not l_tail_inside):
        verdict = "LOCAL-CLOSED-GLOBAL-NOT-YET-REPAIRED"
    elif (l_path_inside or l_tail_inside) and not (l_muf_inside and block_inside):
        verdict = "GLOBAL-REPAIR-BUT-LOCAL-REOPENED"
    else:
        verdict = "NO-REPAIR"

    primary_passes = sum([l_path_inside, l_tail_inside, l_muf_inside, block_inside])
    family_passes = sum([l_path_inside, w_wrap_inside, block_inside, l_tail_inside])

    return {
        "late_tail_added_1indexed": [list(pair) for pair in late_tail_added],
        "k_late_tail_edges_added": len(late_tail_added),
        "full_analysis": full_analysis,
        "block_chi2": block_stat,
        "l_path_gap_vs_sim_mean": empirical["L_path"] - full_analysis["L_path"]["sim_mean"],
        "l_tail_gap_vs_sim_mean": empirical["L_tail_91_114"] - full_analysis["L_tail_91_114"]["sim_mean"],
        "mufassal_gap_vs_sim_mean": empirical["L_mufassal_short"] - full_analysis["L_mufassal_short"]["sim_mean"],
        "primary_repair_pass": primary_repair_pass,
        "four_obs_family_pass": four_obs_family_pass,
        "primary_passes": primary_passes,
        "family_passes": family_passes,
        "cell_verdict": verdict,
        "sim_summaries": {
            key: summarize_distribution([row[key] for row in cell_run["sim_results"]])
            for key in ["L_path", "W_wrap", "L_tiwal", "L_hawamim", "L_mufassal_short", "L_tail_91_114"]
        },
        "sa_summary": cell_run["sa_summary"],
        "valid_pairs_count": cell_run["valid_pairs_count"],
        "sim_samples": cell_run["sim_results"][:25],
    }


def positive_control_check(cell_k0: dict, parent_cell_a: dict) -> dict:
    parent_l_path_mean = float(parent_cell_a["L_path"]["sim_mean"])
    parent_l_tail_mean = float(parent_cell_a["L_tail_91_114"]["sim_mean"])
    parent_l_muf_mean = float(parent_cell_a["L_mufassal_short"]["sim_mean"])

    cur_l_path = cell_k0["full_analysis"]["L_path"]
    cur_l_tail = cell_k0["full_analysis"]["L_tail_91_114"]
    cur_l_muf = cell_k0["full_analysis"]["L_mufassal_short"]
    cur_block = cell_k0["block_chi2"]

    same_signature = bool(
        cur_l_muf["sim_inside_95ci"]
        and cur_block["sim_inside_95ci"]
        and not cur_l_path["sim_inside_95ci"]
        and not cur_l_tail["sim_inside_95ci"]
        and cur_l_path["sim_percentile_of_empirical"] < 5.0
        and cur_l_tail["sim_percentile_of_empirical"] < 5.0
    )
    drifts = {
        "L_path_sim_mean_abs_delta": abs(cur_l_path["sim_mean"] - parent_l_path_mean),
        "L_tail_91_114_sim_mean_abs_delta": abs(cur_l_tail["sim_mean"] - parent_l_tail_mean),
        "L_mufassal_short_sim_mean_abs_delta": abs(cur_l_muf["sim_mean"] - parent_l_muf_mean),
    }
    drift_ok = bool(
        drifts["L_path_sim_mean_abs_delta"] <= 0.50
        and drifts["L_tail_91_114_sim_mean_abs_delta"] <= 0.75
        and drifts["L_mufassal_short_sim_mean_abs_delta"] <= 0.50
    )
    return {
        "same_signature_pass": same_signature,
        "drift_checks": drifts,
        "drift_pass": drift_ok,
        "positive_control_pass": bool(same_signature and drift_ok),
    }


def main() -> None:
    print("=" * 78)
    print("H-NEW-236.1f - Late-tail scaffold repair sweep")
    print("=" * 78)
    print(f"Seed={SEED}; N_SIM={N_SIM}; N_RANDOM={N_RANDOM}; SA_ITERS={SA_ITERS}")

    dmat = load_d_matrix()
    prereg_hash = prereg_sha256()
    parents = load_parent_cells(dmat)

    print(f"Pre-reg SHA-256: {prereg_hash}")
    print(f"Base cell loaded from H-NEW-236.1c: {CELL_A_NAME}")
    print(f"M_H cell loaded from H-NEW-236.1b: {CELL_MH_NAME}")
    print("Locked late-tail edges:")
    for edge in LATE_TAIL_EDGES_1INDEXED:
        print(f"  Q {edge[0]}->{edge[1]}")

    empirical_tour = list(range(114))
    empirical = compute_observables(empirical_tour, dmat)
    print("\nEmpirical observables:")
    for key, value in empirical.items():
        print(f"  {key:22s} = {value:.6f}")

    print("\nRunning shared random null...")
    rand_results = []
    for k in range(N_RANDOM):
        rand_results.append(simulate_random(k, dmat))
        if (k + 1) % 250 == 0:
            print(f"  random {k + 1}/{N_RANDOM}")

    base_hinges = parents["cell_a_hinges_1indexed"]
    cell_outputs = {}
    for k in range(0, len(LATE_TAIL_EDGES_1INDEXED) + 1):
        late_tail_added = LATE_TAIL_EDGES_1INDEXED[:k]
        hinges = dedup_hinges(base_hinges + late_tail_added)
        cell_name = f"cell_k_{k:02d}"
        print(
            f"\n-- Running {cell_name} (k={k}; |hinges|={len(hinges)}; "
            f"added_tail_edges={late_tail_added})..."
        )
        cell_run = run_cell(cell_name, seed_offset=k * 100_000, hinges_1indexed=hinges, dmat=dmat)
        analysis = analyze_cell(cell_run, empirical, rand_results, late_tail_added)
        cell_outputs[cell_name] = {
            "hinges_1indexed": cell_run["hinges_1indexed"],
            "within_hinges_1indexed": cell_run["within_hinges_1indexed"],
            "cross_hinges_1indexed": cell_run["cross_hinges_1indexed"],
            **analysis,
        }
        fa = analysis["full_analysis"]
        print(
            f"   verdict={analysis['cell_verdict']:34s} "
            f"path_in={fa['L_path']['sim_inside_95ci']} "
            f"tail_in={fa['L_tail_91_114']['sim_inside_95ci']} "
            f"muf_in={fa['L_mufassal_short']['sim_inside_95ci']} "
            f"block_in={analysis['block_chi2']['sim_inside_95ci']} "
            f"wrap_in={fa['W_wrap']['sim_inside_95ci']}"
        )

    cell_k0 = cell_outputs["cell_k_00"]
    positive_control = positive_control_check(cell_k0, parents["cell_a_parent_metrics"])
    print(
        "\nPositive control k=0: "
        f"{'PASS' if positive_control['positive_control_pass'] else 'FAIL'} "
        f"(same_signature={positive_control['same_signature_pass']}; "
        f"drift_pass={positive_control['drift_pass']})"
    )

    repair_cells = [
        name for name, cell in cell_outputs.items() if cell["primary_repair_pass"]
    ]
    family_4of4_cells = [
        name for name, cell in cell_outputs.items() if cell["four_obs_family_pass"]
    ]

    first_primary_repair_cell = repair_cells[0] if repair_cells else None
    first_primary_repair_k = (
        cell_outputs[first_primary_repair_cell]["k_late_tail_edges_added"]
        if first_primary_repair_cell is not None
        else None
    )
    first_family_4of4_cell = family_4of4_cells[0] if family_4of4_cells else None
    first_family_4of4_k = (
        cell_outputs[first_family_4of4_cell]["k_late_tail_edges_added"]
        if first_family_4of4_cell is not None
        else None
    )

    if positive_control["positive_control_pass"] and first_primary_repair_k is not None:
        overall_verdict = "LATE-TAIL-SCAFFOLD-REPAIR-CONFIRMED"
        architecture_reading = (
            "split-terminal architecture / distributed late-tail scaffold supported"
        )
    elif not positive_control["positive_control_pass"]:
        overall_verdict = "INSTRUMENT-FAIL-POSITIVE-CONTROL"
        architecture_reading = "no evidential read; k=0 failed to reproduce H-NEW-236.1c Cell A"
    else:
        overall_verdict = "NO-LATE-TAIL-ONLY-REPAIR"
        architecture_reading = (
            "late-tail-only scaffold not sufficient under hard-adjacency repair sweep"
        )

    print(f"\nPrimary repair cells: {repair_cells}")
    print(f"Family 4/4 cells:    {family_4of4_cells}")
    print(f"Overall verdict:     {overall_verdict}")
    print(f"Architecture read:   {architecture_reading}")

    output = {
        "finding_id": "h-new-236-1f",
        "title": "Late-tail scaffold repair sweep from H-NEW-236.1c Cell A",
        "pre_reg_sha256": prereg_hash,
        "parents": ["h-new-236-1c", "h-new-236-1b"],
        "grandparent": "h-new-236-1a -> h-new-236-1 -> h-new-236 -> cross-finding-020",
        "seed": SEED,
        "n_sim": N_SIM,
        "n_random": N_RANDOM,
        "sa_iters": SA_ITERS,
        "bonferroni_k": 11,
        "alpha_bon": 0.05 / 11.0,
        "rules_tuple": (
            "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, "
            "QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, "
            "stochastic 2-opt with classical-block + Q1-lock + length-stratification "
            "+ M2-muq constraints + H-NEW-236.1c Cell-A base + cumulative late-tail M_H "
            "edge preservation for k in {0..10}, seed 20260423)"
        ),
        "empirical": empirical,
        "base_cell_name": CELL_A_NAME,
        "base_cell_from_h2361c": {
            "hinges_1indexed": [list(pair) for pair in parents["cell_a_hinges_1indexed"]],
            "parent_metrics": parents["cell_a_parent_metrics"],
        },
        "reference_mh_cell_from_h2361b": parents["cell_mh_metrics"],
        "late_tail_scaffold_1indexed": [list(pair) for pair in LATE_TAIL_EDGES_1INDEXED],
        "late_tail_edge_ranks": parents["late_tail_edge_ranks"],
        "mh_tail_edges_sorted_by_rank_1indexed": [
            list(pair) for pair in parents["mh_tail_edges_sorted_by_rank_1indexed"]
        ],
        "positive_control_k0": positive_control,
        "random_baseline_summaries": {
            key: summarize_distribution([row[key] for row in rand_results])
            for key in ["L_path", "W_wrap", "L_tiwal", "L_hawamim", "L_mufassal_short", "L_tail_91_114"]
        },
        "cells": cell_outputs,
        "repair_cells_primary": repair_cells,
        "repair_cells_family_4of4": family_4of4_cells,
        "first_primary_repair_cell": first_primary_repair_cell,
        "first_primary_repair_k": first_primary_repair_k,
        "first_family_4of4_cell": first_family_4of4_cell,
        "first_family_4of4_k": first_family_4of4_k,
        "overall_verdict": overall_verdict,
        "architecture_reading": architecture_reading,
    }

    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
