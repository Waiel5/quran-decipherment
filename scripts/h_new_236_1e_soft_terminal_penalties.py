#!/usr/bin/env python3
"""H-NEW-236.1e - Soft terminal penalties on top-50 hinge baseline.

Pre-reg:
  findings/phase-b-hypotheses/h-new-236-1e-soft-terminal-penalties-prereg.md

Parent context:
  H-NEW-236.1a: top-50 closes L_path, leaves L_mufassal_short high.
  H-NEW-236.1b: hard M_R / M_L close L_mufassal_short but break L_path.
  H-NEW-236.1e: replace hard terminal adjacencies with a weighted soft penalty
  to test whether a softer terminal mechanism can recover block closure
  without losing the global path fit.
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

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H111_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
H2361A_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1a.json"
PREREG = (
    PROJECT_ROOT
    / "findings/phase-b-hypotheses/h-new-236-1e-soft-terminal-penalties-prereg.md"
)
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1e.json"

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

RHYME_CLASSES_MUFASSAL_SHORT: dict[int, str] = {
    78: "R-saj-mixed",
    79: "R-a",
    80: "R-saj-mixed",
    81: "R-saj-mixed",
    82: "R-saj-mixed",
    83: "R-un-in",
    84: "R-saj-mixed",
    85: "R-saj-mixed",
    86: "R-saj-mixed",
    87: "R-a",
    88: "R-a",
    89: "R-a",
    90: "R-saj-mixed",
    91: "R-a",
    92: "R-a",
    93: "R-a",
    94: "R-a",
    95: "R-a",
    96: "R-a",
    97: "R-r",
    98: "R-a",
    99: "R-saj-mixed",
    100: "R-a",
    101: "R-saj-mixed",
    102: "R-un-in",
    103: "R-r",
    104: "R-un-in",
    105: "R-un-in",
    106: "R-un-in",
    107: "R-un-in",
    108: "R-r",
    109: "R-un-in",
    110: "R-r",
    111: "R-s",
    112: "R-d-tawhid",
    113: "R-q",
    114: "R-s",
}

LITURGICAL_PAIRS_1INDEXED: list[tuple[int, int]] = [
    (87, 88),
    (93, 94),
    (109, 110),
    (113, 114),
]

LAMBDA_GRID = [
    ("cell_a_lambda_0p05", 0, 0.05),
    ("cell_b_lambda_0p10", 100_000, 0.10),
    ("cell_c_lambda_0p20", 200_000, 0.20),
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


def load_h2361a_top50_baseline() -> dict:
    with H2361A_JSON.open() as f:
        data = json.load(f)
    cell = data["cells"]["cell_b_top50"]
    return {
        "hinges_1indexed": [tuple(pair) for pair in cell["hinges_1indexed"]],
        "l_path_mean": float(cell["full_analysis"]["L_path"]["sim_mean"]),
        "l_path_ci_lo": float(cell["full_analysis"]["L_path"]["sim_ci_lo"]),
        "l_path_ci_hi": float(cell["full_analysis"]["L_path"]["sim_ci_hi"]),
        "l_path_gap": float(cell["l_path_gap_vs_sim_mean"]),
        "mufassal_mean": float(cell["full_analysis"]["L_mufassal_short"]["sim_mean"]),
        "mufassal_std": float(cell["full_analysis"]["L_mufassal_short"]["sim_std"]),
        "mufassal_gap": (
            float(cell["full_analysis"]["L_mufassal_short"]["empirical"])
            - float(cell["full_analysis"]["L_mufassal_short"]["sim_mean"])
        ),
        "mufassal_z": float(cell["block_chi2"]["per_block"]["L_mufassal_short"]["sim_z"]),
        "block_chi2": float(cell["block_chi2"]["empirical_stat_under_sim"]),
    }


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


def build_rhyme_pairs_1indexed() -> list[tuple[int, int]]:
    out = []
    for a in range(78, 114):
        b = a + 1
        if RHYME_CLASSES_MUFASSAL_SHORT[a] == RHYME_CLASSES_MUFASSAL_SHORT[b]:
            out.append((a, b))
    return out


RHYME_PAIRS_1INDEXED = build_rhyme_pairs_1indexed()


def build_preference_weights_1indexed() -> dict[tuple[int, int], int]:
    weights: dict[tuple[int, int], int] = {}
    for pair in RHYME_PAIRS_1INDEXED:
        weights[pair] = weights.get(pair, 0) + 1
    for pair in LITURGICAL_PAIRS_1INDEXED:
        weights[pair] = weights.get(pair, 0) + 2
    return dict(sorted(weights.items()))


PREFERENCE_WEIGHTS_1INDEXED = build_preference_weights_1indexed()
PREFERENCE_WEIGHTS_0INDEXED = {
    (a - 1, b - 1): weight for (a, b), weight in PREFERENCE_WEIGHTS_1INDEXED.items()
}
PREFERENCE_TOTAL_WEIGHT = sum(PREFERENCE_WEIGHTS_1INDEXED.values())


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
    if not hinges_0indexed:
        return True
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


def weighted_preferences_satisfied(
    tour: list[int], pref_weights_0indexed: dict[tuple[int, int], int]
) -> int:
    total = 0
    for i in range(len(tour) - 1):
        total += pref_weights_0indexed.get((tour[i], tour[i + 1]), 0)
    return total


def soft_preference_satisfied_delta(
    tour: list[int],
    pa: int,
    pb: int,
    pref_weights_0indexed: dict[tuple[int, int], int],
) -> int:
    delta = 0

    left = tour[pa - 1] if pa - 1 >= 0 else None
    right = tour[pb + 1] if pb + 1 < len(tour) else None

    if left is not None:
        delta -= pref_weights_0indexed.get((left, tour[pa]), 0)
        delta += pref_weights_0indexed.get((left, tour[pb]), 0)
    if right is not None:
        delta -= pref_weights_0indexed.get((tour[pb], right), 0)
        delta += pref_weights_0indexed.get((tour[pa], right), 0)

    for i in range(pa, pb):
        delta -= pref_weights_0indexed.get((tour[i], tour[i + 1]), 0)
        delta += pref_weights_0indexed.get((tour[i + 1], tour[i]), 0)

    return delta


def validate_soft_delta(pref_weights_0indexed: dict[tuple[int, int], int]) -> None:
    rng = random.Random(123456)
    dummy_hinges = [(a - 1, b - 1) for a, b in [(1, 2), (9, 10), (39, 40), (46, 47), (48, 49)]]
    within_hinges = [(a, b) for a, b in dummy_hinges if SURAH_TO_BLOCK[a + 1] == SURAH_TO_BLOCK[b + 1]]
    cross_hinges = [(a, b) for a, b in dummy_hinges if SURAH_TO_BLOCK[a + 1] != SURAH_TO_BLOCK[b + 1]]
    tour = initial_hinge_respecting_tour(rng, within_hinges, cross_hinges, dummy_hinges)

    for _ in range(200):
        pa, pb = rng.choice(VALID_PAIRS)
        if swap_breaks_hinge(tour, pa, pb, set(dummy_hinges)):
            continue
        old_val = weighted_preferences_satisfied(tour, pref_weights_0indexed)
        delta = soft_preference_satisfied_delta(tour, pa, pb, pref_weights_0indexed)
        trial = list(tour)
        trial[pa : pb + 1] = trial[pa : pb + 1][::-1]
        new_val = weighted_preferences_satisfied(trial, pref_weights_0indexed)
        if new_val - old_val != delta:
            raise AssertionError(
                f"Soft delta mismatch: old={old_val}, new={new_val}, delta={delta}, "
                f"pa={pa}, pb={pb}"
            )
        tour = trial


def sa_with_soft_penalty(
    tour: list[int],
    dmat: list[list[float]],
    rng: random.Random,
    hinge_set: set[tuple[int, int]],
    pref_weights_0indexed: dict[tuple[int, int], int],
    lambda_penalty: float,
    n_iters: int = SA_ITERS,
) -> tuple[list[int], dict]:
    current = list(tour)
    current_len = path_length(current, dmat)
    current_sat = weighted_preferences_satisfied(current, pref_weights_0indexed)
    current_score = current_len + lambda_penalty * (PREFERENCE_TOTAL_WEIGHT - current_sat)

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
            delta_len = new_cost - old_cost

            delta_sat = soft_preference_satisfied_delta(current, pa, pb, pref_weights_0indexed)
            delta_score = delta_len - lambda_penalty * delta_sat

            if delta_score < 0:
                current[pa : pb + 1] = current[pa : pb + 1][::-1]
                current_len += delta_len
                current_sat += delta_sat
                current_score += delta_score
                accept_count += 1
                continue

            if temperature > 1e-9:
                p_accept = math.exp(-delta_score / temperature) if delta_score / temperature < 50 else 0.0
            else:
                p_accept = 0.0

            if rng.random() < p_accept:
                current[pa : pb + 1] = current[pa : pb + 1][::-1]
                current_len += delta_len
                current_sat += delta_sat
                current_score += delta_score
                accept_count += 1
            else:
                reject_by_sa += 1

    return current, {
        "accepted": accept_count,
        "rejected_by_hinge": reject_by_hinge,
        "rejected_by_sa": reject_by_sa,
        "final_length": current_len,
        "final_pref_satisfied_weight": current_sat,
        "final_pref_missing_weight": PREFERENCE_TOTAL_WEIGHT - current_sat,
        "final_augmented_score": current_score,
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


def preference_metrics(tour: list[int]) -> dict:
    edge_set = {(tour[i] + 1, tour[i + 1] + 1) for i in range(len(tour) - 1)}
    rhyme_sat = sum(1 for pair in RHYME_PAIRS_1INDEXED if pair in edge_set)
    lit_sat = sum(1 for pair in LITURGICAL_PAIRS_1INDEXED if pair in edge_set)
    weighted_sat = sum(weight for pair, weight in PREFERENCE_WEIGHTS_1INDEXED.items() if pair in edge_set)
    return {
        "pref_weighted_satisfied": weighted_sat,
        "pref_weighted_missing": PREFERENCE_TOTAL_WEIGHT - weighted_sat,
        "pref_weighted_satisfied_pct": 100.0 * weighted_sat / PREFERENCE_TOTAL_WEIGHT,
        "rhyme_pairs_satisfied": rhyme_sat,
        "rhyme_pairs_missing": len(RHYME_PAIRS_1INDEXED) - rhyme_sat,
        "liturgical_pairs_satisfied": lit_sat,
        "liturgical_pairs_missing": len(LITURGICAL_PAIRS_1INDEXED) - lit_sat,
    }


def run_cell(
    cell_name: str,
    seed_offset: int,
    hinges_1indexed: list[tuple[int, int]],
    dmat: list[list[float]],
    lambda_penalty: float,
) -> dict:
    within_hinges, cross_hinges = classify_hinges(hinges_1indexed)
    hinges_0indexed = [(a - 1, b - 1) for a, b in hinges_1indexed]
    hinge_set = set(hinges_0indexed)

    sim_results = []
    sa_stats = []

    for sim_idx in range(N_SIM):
        rng = random.Random(SEED + seed_offset + sim_idx)
        init = initial_hinge_respecting_tour(rng, within_hinges, cross_hinges, hinges_0indexed)
        final, stats = sa_with_soft_penalty(
            init,
            dmat,
            rng,
            hinge_set,
            PREFERENCE_WEIGHTS_0INDEXED,
            lambda_penalty,
        )
        if not all_hinges_ok(final, hinges_0indexed):
            failed = {k: v for k, v in verify_hinges(final, hinges_0indexed).items() if not v}
            raise AssertionError(f"{cell_name}: hinge verification failed for sim {sim_idx}: {failed}")
        obs = compute_observables(final, dmat)
        obs.update(preference_metrics(final))
        obs["sim_idx"] = sim_idx
        sim_results.append(obs)
        sa_stats.append(stats)

    return {
        "within_hinges_1indexed": [(a + 1, b + 1) for a, b in within_hinges],
        "cross_hinges_1indexed": [(a + 1, b + 1) for a, b in cross_hinges],
        "sim_results": sim_results,
        "sa_summary": {
            "accepted_mean": statistics.mean(row["accepted"] for row in sa_stats),
            "accepted_min": min(row["accepted"] for row in sa_stats),
            "accepted_max": max(row["accepted"] for row in sa_stats),
            "rejected_by_hinge_mean": statistics.mean(row["rejected_by_hinge"] for row in sa_stats),
            "rejected_by_sa_mean": statistics.mean(row["rejected_by_sa"] for row in sa_stats),
            "final_pref_satisfied_weight_mean": statistics.mean(
                row["final_pref_satisfied_weight"] for row in sa_stats
            ),
            "final_pref_missing_weight_mean": statistics.mean(
                row["final_pref_missing_weight"] for row in sa_stats
            ),
            "final_augmented_score_mean": statistics.mean(
                row["final_augmented_score"] for row in sa_stats
            ),
        },
    }


def analyze_cell(cell_run: dict, empirical: dict, rand_results: list[dict], baseline: dict) -> dict:
    sim_results = cell_run["sim_results"]
    full_analysis = {}
    for obs_name in [
        "L_path",
        "W_wrap",
        "L_tiwal",
        "L_hawamim",
        "L_mufassal_short",
        "L_tail_91_114",
    ]:
        full_analysis[obs_name] = observable_analysis(
            empirical[obs_name],
            [row[obs_name] for row in sim_results],
            [row[obs_name] for row in rand_results],
        )

    block_stat = block_chi2(empirical, sim_results, rand_results)
    sim_passes = sum(
        [
            full_analysis["L_path"]["sim_inside_95ci"],
            full_analysis["W_wrap"]["sim_inside_95ci"],
            block_stat["sim_inside_95ci"],
            full_analysis["L_tail_91_114"]["sim_inside_95ci"],
        ]
    )

    l_path_inside = full_analysis["L_path"]["sim_inside_95ci"]
    mufassal_inside = full_analysis["L_mufassal_short"]["sim_inside_95ci"]
    primary_pass = bool(l_path_inside and mufassal_inside)
    full_four_pass = bool(primary_pass and sim_passes == 4)

    if full_four_pass:
        verdict = "SOFT-CLOSES-STRICT-4OF4"
    elif primary_pass:
        verdict = "SOFT-CLOSES-PRIMARY"
    elif mufassal_inside and not l_path_inside:
        verdict = "SOFT-PARSIMONY-CONFLICT"
    elif (not mufassal_inside) and l_path_inside:
        verdict = "SOFT-NULL"
    else:
        verdict = "SOFT-BROKEN"

    l_path_gap = full_analysis["L_path"]["empirical"] - full_analysis["L_path"]["sim_mean"]
    mufassal_gap = (
        full_analysis["L_mufassal_short"]["empirical"]
        - full_analysis["L_mufassal_short"]["sim_mean"]
    )
    mufassal_gap_closed_pct = 100.0 * (
        baseline["mufassal_gap"] - mufassal_gap
    ) / baseline["mufassal_gap"]

    pref_weight_vals = [row["pref_weighted_satisfied"] for row in sim_results]
    pref_pct_vals = [row["pref_weighted_satisfied_pct"] for row in sim_results]
    rhyme_sat_vals = [row["rhyme_pairs_satisfied"] for row in sim_results]
    lit_sat_vals = [row["liturgical_pairs_satisfied"] for row in sim_results]

    return {
        "full_analysis": full_analysis,
        "block_chi2": block_stat,
        "sim_passes": sim_passes,
        "l_path_inside_sim_95ci": l_path_inside,
        "mufassal_inside_sim_95ci": mufassal_inside,
        "primary_pass": primary_pass,
        "full_four_pass": full_four_pass,
        "l_path_gap_vs_sim_mean": l_path_gap,
        "mufassal_gap_vs_sim_mean": mufassal_gap,
        "mufassal_gap_closed_pct_vs_h2361a_top50": mufassal_gap_closed_pct,
        "cell_verdict": verdict,
        "preference_summary": {
            "weighted_satisfied_mean": statistics.mean(pref_weight_vals),
            "weighted_satisfied_ci95": list(ci_95(pref_weight_vals)),
            "weighted_satisfied_pct_mean": statistics.mean(pref_pct_vals),
            "rhyme_pairs_satisfied_mean": statistics.mean(rhyme_sat_vals),
            "liturgical_pairs_satisfied_mean": statistics.mean(lit_sat_vals),
        },
        "sim_summaries": {
            key: summarize_distribution([row[key] for row in sim_results])
            for key in [
                "L_path",
                "W_wrap",
                "L_tiwal",
                "L_hawamim",
                "L_mufassal_short",
                "L_tail_91_114",
                "pref_weighted_satisfied",
                "pref_weighted_satisfied_pct",
                "rhyme_pairs_satisfied",
                "liturgical_pairs_satisfied",
            ]
        },
        "sa_summary": cell_run["sa_summary"],
        "sim_samples": sim_results[:25],
    }


def main() -> None:
    print("=" * 78)
    print("H-NEW-236.1e - Soft terminal penalties on top-50 hinge baseline")
    print("=" * 78)
    print(f"Seed={SEED}; N_SIM={N_SIM}; N_RANDOM={N_RANDOM}; SA_ITERS={SA_ITERS}")

    dmat = load_d_matrix()
    baseline = load_h2361a_top50_baseline()
    prereg_hash = prereg_sha256()

    print(f"Pre-reg SHA-256: {prereg_hash}")
    print(
        "Preference weights: "
        f"{len(RHYME_PAIRS_1INDEXED)} rhyme pairs x1 + "
        f"{len(LITURGICAL_PAIRS_1INDEXED)} liturgical pairs x2 "
        f"= total weight {PREFERENCE_TOTAL_WEIGHT}"
    )
    validate_soft_delta(PREFERENCE_WEIGHTS_0INDEXED)
    print("Soft-penalty delta check: OK")

    ranked_edges = canonical_edge_ranking(dmat)
    top50 = [(row["a"], row["b"]) for row in ranked_edges[:50]]
    if top50 != baseline["hinges_1indexed"]:
        raise AssertionError("Top-50 hinge set drift vs H-NEW-236.1a baseline")

    empirical_tour = list(range(114))
    empirical = compute_observables(empirical_tour, dmat)
    empirical.update(preference_metrics(empirical_tour))
    print("\nEmpirical observables:")
    for key in [
        "L_path",
        "W_wrap",
        "L_tiwal",
        "L_hawamim",
        "L_mufassal_short",
        "L_tail_91_114",
        "pref_weighted_satisfied",
        "pref_weighted_satisfied_pct",
    ]:
        print(f"  {key:26s} = {empirical[key]:.6f}")

    print("\nRunning shared random null (MW-5 calibration)...")
    rand_results = []
    for k in range(N_RANDOM):
        rand_results.append(simulate_random(k, dmat))
        if (k + 1) % 250 == 0:
            print(f"  random {k + 1}/{N_RANDOM}")

    cell_specs = [("mw5_positive_control_soft0", 900_000, 0.0)] + LAMBDA_GRID
    cell_outputs = {}
    for cell_name, seed_offset, lambda_penalty in cell_specs:
        print(f"\n-- Running {cell_name} (lambda={lambda_penalty:.3f})...")
        cell_run = run_cell(cell_name, seed_offset, top50, dmat, lambda_penalty=lambda_penalty)
        analysis = analyze_cell(cell_run, empirical, rand_results, baseline)
        cell_outputs[cell_name] = {
            "lambda_penalty": lambda_penalty,
            "hinges_1indexed": top50,
            "within_hinges_1indexed": cell_run["within_hinges_1indexed"],
            "cross_hinges_1indexed": cell_run["cross_hinges_1indexed"],
            **analysis,
        }
        fa = analysis["full_analysis"]
        print(
            "   "
            f"L_path pct={fa['L_path']['sim_percentile_of_empirical']:6.2f}  "
            f"L_muf pct={fa['L_mufassal_short']['sim_percentile_of_empirical']:6.2f}  "
            f"pref_sat_mean={analysis['preference_summary']['weighted_satisfied_mean']:.2f}/{PREFERENCE_TOTAL_WEIGHT}  "
            f"verdict={analysis['cell_verdict']}"
        )

    pc = cell_outputs["mw5_positive_control_soft0"]
    pc_z = pc["block_chi2"]["per_block"]["L_mufassal_short"]["sim_z"]
    parent_z = baseline["mufassal_z"]
    pc_ok = math.isfinite(pc_z) and abs(pc_z - parent_z) <= 2.0

    non_control_cells = [name for name, _, _ in LAMBDA_GRID]
    strict_4of4 = [name for name in non_control_cells if cell_outputs[name]["full_four_pass"]]
    primary_only = [
        name
        for name in non_control_cells
        if cell_outputs[name]["primary_pass"] and not cell_outputs[name]["full_four_pass"]
    ]
    primary_conflict = [
        name for name in non_control_cells if cell_outputs[name]["cell_verdict"] == "SOFT-PARSIMONY-CONFLICT"
    ]

    if strict_4of4:
        overall_verdict = "SOFT TERMINAL MECHANISM CLOSES STRICTLY"
    elif primary_only:
        overall_verdict = "SOFT TERMINAL MECHANISM CLOSES PRIMARY TARGET ONLY"
    elif primary_conflict:
        overall_verdict = "SOFT TERMINAL MECHANISM SHOWS PARSIMONY CONFLICT ONLY"
    else:
        overall_verdict = "SOFT TERMINAL MECHANISM NULL"

    print(
        f"\nMW-5 positive control: top-50 soft0 mufassal z = {pc_z:+.3f} "
        f"(parent {parent_z:+.3f}; tol |delta|<=2.0 => {'OK' if pc_ok else 'FAIL'})"
    )
    print(f"Strict 4/4 cells: {strict_4of4}")
    print(f"Primary-only cells: {primary_only}")
    print(f"Parsimony-conflict cells: {primary_conflict}")
    print(f"Overall verdict: {overall_verdict}")

    output = {
        "finding_id": "h-new-236-1e",
        "title": "Soft terminal penalties on top-50 hinge baseline",
        "pre_reg_sha256": prereg_hash,
        "parent": "h-new-236-1b / h-new-236-1c",
        "grandparent": "h-new-236-1a -> h-new-236-1 -> h-new-236 -> cross-finding-020",
        "seed": SEED,
        "n_sim": N_SIM,
        "n_random": N_RANDOM,
        "sa_iters": SA_ITERS,
        "bonferroni_k": len(LAMBDA_GRID),
        "alpha_bon": 0.05 / len(LAMBDA_GRID),
        "rules_tuple": (
            "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, "
            "QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, "
            "stochastic 2-opt with classical-block + Q1-lock + length-stratification "
            "+ M2-muq + TOP-50-HINGE-BASELINE + SOFT-TERMINAL-PREFERENCE-PENALTY, seed 20260421)"
        ),
        "soft_penalty_spec": {
            "rhyme_pairs_1indexed": RHYME_PAIRS_1INDEXED,
            "liturgical_pairs_1indexed": LITURGICAL_PAIRS_1INDEXED,
            "pair_weights_1indexed": {f"{a}-{b}": w for (a, b), w in PREFERENCE_WEIGHTS_1INDEXED.items()},
            "pair_weighting_rule": "rhyme pair = 1, liturgical pair = 2, overlaps additive",
            "total_weight": PREFERENCE_TOTAL_WEIGHT,
            "lambda_grid": [
                {"cell_name": cell_name, "lambda_penalty": lambda_penalty}
                for cell_name, _, lambda_penalty in LAMBDA_GRID
            ],
        },
        "parent_h2361a_top50": baseline,
        "mw5_positive_control_pass": pc_ok,
        "mw5_positive_control_mufassal_z": pc_z,
        "empirical": empirical,
        "canonical_edge_ranking_top_60": ranked_edges[:60],
        "random_baseline_summaries": {
            key: summarize_distribution([row[key] for row in rand_results])
            for key in [
                "L_path",
                "W_wrap",
                "L_tiwal",
                "L_hawamim",
                "L_mufassal_short",
                "L_tail_91_114",
            ]
        },
        "cells": cell_outputs,
        "strict_4of4_cells": strict_4of4,
        "primary_only_cells": primary_only,
        "parsimony_conflict_cells": primary_conflict,
        "overall_verdict": overall_verdict,
    }

    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
