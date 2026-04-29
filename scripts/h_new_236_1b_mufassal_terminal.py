#!/usr/bin/env python3
"""H-NEW-236.1b - Mufassal-short terminal-block mechanism test.

Pre-reg:
  findings/phase-b-hypotheses/h-new-236-1b-mufassal-terminal-mechanism-prereg.md
  SHA-256: 8c006dfc7e79c74083cfef054787b637d110c9f400285403703ff0a868db7df6

Parent:
  H-NEW-236.1a (top-50 hinges: L_path closes; hawamim closes; mufassal-short z=+10.66 remains).

Four mechanism cells tested on top of the H-NEW-236.1a top-50 hinge baseline:
  M_H: hinge-100 (extend hinges to top-100 FR consecutive edges)
  M_R: rhyme-class preservation within mufassal-short
  M_L: liturgical recitation-pair adjacency constraints
  M_B: sub-block partition of mufassal-short into {Q 78-88, Q 89-107, Q 108-114}

Plus a MW-5 positive control (top-50 baseline under new seed) to verify
that the instrument reproduces the H-NEW-236.1a mufassal-short z=+10.66.

Seed: 20260420 (new day per project convention).
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import statistics
from pathlib import Path

SEED = 20260420
N_SIM = 1000
N_RANDOM = 1000
SA_ITERS = 200
T_HOT = 0.05
T_COLD = 0.001

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H111_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
H2361A_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1a.json"
PREREG = PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-236-1b-mufassal-terminal-mechanism-prereg.md"
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1b.json"

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

# ---------------------------------------------------------------------------
# Pre-committed mechanism specifications (LOCKED pre-run; see prereg §3).
# ---------------------------------------------------------------------------

# M_R rhyme-class assignment (mufassal-short Q 78-114 only).
# Classes: R-a, R-un/in, R-r, R-saj'-mixed, R-d-tawhid, R-s, R-q.
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

# M_L liturgical recitation-pair adjacencies (LOCKED).
# Pairs on top of top-50 baseline; duplicates against top-50 are silently deduped.
M_L_PAIRS_1INDEXED: list[tuple[int, int]] = [
    (87, 88),    # sabbih-openers
    (93, 94),    # al-Duha / al-Sharh consolation pair
    (109, 110),  # al-Kafirun / al-Nasr
    (113, 114),  # al-muawwidhatan
]

# M_B sub-block boundaries: segments within mufassal-short that cannot be crossed by 2-opt swaps.
M_B_SUBBLOCKS_1INDEXED: list[list[int]] = [
    list(range(78, 89)),   # Q 78-88 eschatological panorama
    list(range(89, 108)),  # Q 89-107 ethical-theological
    list(range(108, 115)), # Q 108-114 closing refrains
]

# ---------------------------------------------------------------------------
# I/O + edge-ranking utilities (adapted from h_new_236_1a_extended_hinges.py)
# ---------------------------------------------------------------------------


def prereg_sha256() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def load_d_matrix() -> list[list[float]]:
    with H111_JSON.open() as f:
        parent = json.load(f)
    n = 114
    dmat = [[0.0] * n for _ in range(n)]
    for i, j, d in parent["D_matrix_upper_triangular"]:
        dmat[i - 1][j - 1] = float(d)
        dmat[j - 1][i - 1] = float(d)
    return dmat


def load_parent_mufassal_short_stats() -> dict:
    """Load the H-NEW-236.1a top-50 mufassal-short sim stats for MW-5 positive control check."""
    with H2361A_JSON.open() as f:
        data = json.load(f)
    cell_b = data["cells"]["cell_b_top50"]
    return {
        "mufassal_short_sim_mean": cell_b["full_analysis"]["L_mufassal_short"]["sim_mean"],
        "mufassal_short_sim_std": cell_b["full_analysis"]["L_mufassal_short"]["sim_std"],
        "mufassal_short_sim_z": cell_b["block_chi2"]["per_block"]["L_mufassal_short"]["sim_z"],
        "l_path_sim_mean": cell_b["full_analysis"]["L_path"]["sim_mean"],
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


def classify_hinges(hinges_1indexed: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    cross: list[tuple[int, int]] = []
    within: list[tuple[int, int]] = []
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


# ---------------------------------------------------------------------------
# Initial-tour construction (chain-based; same family as H-NEW-236.1a)
# ---------------------------------------------------------------------------


def build_hinge_chains_for_block(block_members: list[int], within_hinges: list[tuple[int, int]]) -> list[list[int]]:
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


def cross_block_maps(cross_hinges: list[tuple[int, int]]) -> tuple[dict[str, int], dict[str, int]]:
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
    mufassal_sub_blocks_1indexed: list[list[int]] | None = None,
) -> list[int]:
    """Build a hinge-respecting initial tour.

    If `mufassal_sub_blocks_1indexed` is supplied, the mufassal_short block is
    further partitioned so that each sub-block's members occupy the correct
    canonical position sub-segment before any 2-opt swap runs. This is what
    M_B requires: the within-block SA is only allowed inside each sub-block,
    so the initial placement must already respect the sub-block boundaries.
    """
    incoming_head_by_block, outgoing_tail_by_block = cross_block_maps(cross_hinges)
    tour_0indexed: list[int] = []

    for block_name in BLOCK_ORDER:
        members = [surah - 1 for surah in BLOCKS_1INDEXED[block_name]]
        if block_name == "mufassal_short" and mufassal_sub_blocks_1indexed is not None:
            # Build each sub-block independently and concatenate in canonical sub-block order.
            for sub_block in mufassal_sub_blocks_1indexed:
                sub_members = [surah - 1 for surah in sub_block]
                sub_chains = build_hinge_chains_for_block(sub_members, within_hinges)
                # No cross-sub-block hinge incoming/outgoing is permitted under M_B.
                # (All within-block hinges must stay within a single sub-block; see §3.4.)
                rng.shuffle(sub_chains)
                for chain in sub_chains:
                    tour_0indexed.extend(chain)
            continue

        chains = build_hinge_chains_for_block(members, within_hinges)
        chain_by_member = {
            member: chain
            for chain in chains
            for member in chain
        }

        start_chain = None
        end_chain = None
        if block_name in incoming_head_by_block:
            head = incoming_head_by_block[block_name]
            start_chain = chain_by_member[head]
            if start_chain[0] != head:
                raise AssertionError(
                    f"{block_name}: incoming cross-block head Q {head + 1} is not chain-start: {start_chain}"
                )
        if block_name in outgoing_tail_by_block:
            tail = outgoing_tail_by_block[block_name]
            end_chain = chain_by_member[tail]
            if end_chain[-1] != tail:
                raise AssertionError(
                    f"{block_name}: outgoing cross-block tail Q {tail + 1} is not chain-end: {end_chain}"
                )

        if start_chain is not None and end_chain is not None and start_chain is end_chain:
            if len(chains) != 1:
                raise AssertionError(
                    f"{block_name}: single chain would need to be both first and last, but block has extra chains"
                )
            ordered_chains = [start_chain]
        else:
            remaining = [chain for chain in chains if chain is not start_chain and chain is not end_chain]
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


# ---------------------------------------------------------------------------
# 2-opt SA with hinge + per-cell-mechanism constraints
# ---------------------------------------------------------------------------


def within_block_positions() -> dict[str, list[int]]:
    pos_ranges: dict[str, list[int]] = {}
    offset = 0
    for block_name in BLOCK_ORDER:
        n_members = len(BLOCKS_1INDEXED[block_name])
        pos_ranges[block_name] = list(range(offset, offset + n_members))
        offset += n_members
    return pos_ranges


POSITION_RANGES = within_block_positions()


def valid_pairs_for_sa(sub_block_pos_segments: list[list[int]] | None = None) -> list[tuple[int, int]]:
    """Return the list of (pa, pb) position pairs that 2-opt may attempt.

    Standard case: all within-block pairs (except fatiha which has only 1 member).

    If sub_block_pos_segments is supplied, it REPLACES the mufassal-short entry:
    only pairs within the same sub-block-position segment are allowed.
    """
    pairs: list[tuple[int, int]] = []
    for block_name, positions in POSITION_RANGES.items():
        if block_name == "fatiha":
            continue
        if block_name == "mufassal_short" and sub_block_pos_segments is not None:
            for seg in sub_block_pos_segments:
                for idx_a in range(len(seg)):
                    for idx_b in range(idx_a + 1, len(seg)):
                        pairs.append((seg[idx_a], seg[idx_b]))
            continue
        for idx_a in range(len(positions)):
            for idx_b in range(idx_a + 1, len(positions)):
                pairs.append((positions[idx_a], positions[idx_b]))
    return pairs


def swap_breaks_constraint(
    tour: list[int],
    pa: int,
    pb: int,
    hinge_set: set[tuple[int, int]],
) -> bool:
    """True if reversing tour[pa:pb+1] would break any adjacency hinge."""
    n = len(tour)
    if pa - 1 >= 0 and (tour[pa - 1], tour[pa]) in hinge_set:
        return True
    if pb + 1 < n and (tour[pb], tour[pb + 1]) in hinge_set:
        return True
    for i in range(pa, pb):
        if (tour[i], tour[i + 1]) in hinge_set:
            return True
    return False


def sa_with_constraints(
    tour: list[int],
    dmat: list[list[float]],
    rng: random.Random,
    hinge_set: set[tuple[int, int]],
    valid_pairs: list[tuple[int, int]],
    n_iters: int = SA_ITERS,
) -> tuple[list[int], dict]:
    current = list(tour)
    current_len = path_length(current, dmat)
    n = len(current)
    accept_count = 0
    reject_by_hinge = 0
    reject_by_sa = 0

    working_pairs = list(valid_pairs)
    for it in range(n_iters):
        frac = it / max(1, n_iters - 1)
        temperature = T_HOT + frac * (T_COLD - T_HOT)
        rng.shuffle(working_pairs)
        batch_size = min(300, len(working_pairs))
        for pa, pb in working_pairs[:batch_size]:
            if swap_breaks_constraint(current, pa, pb, hinge_set):
                reject_by_hinge += 1
                continue

            left = current[pa - 1] if pa - 1 >= 0 else None
            right = current[pb + 1] if pb + 1 < n else None
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


# ---------------------------------------------------------------------------
# Distribution / analysis utilities
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Per-cell constraint builders
# ---------------------------------------------------------------------------


def build_baseline_top50(dmat: list[list[float]]) -> list[tuple[int, int]]:
    ranked = canonical_edge_ranking(dmat)
    return [(row["a"], row["b"]) for row in ranked[:50]]


def build_cell_M_H(dmat: list[list[float]]) -> list[tuple[int, int]]:
    """Top-100 canonical Fisher-Rao consecutive edges."""
    ranked = canonical_edge_ranking(dmat)
    return [(row["a"], row["b"]) for row in ranked[:100]]


def build_cell_M_R(baseline_top50: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Baseline top-50 + same-rhyme-class adjacent pairs within mufassal-short
    that are adjacent in canonical order.
    """
    extra: list[tuple[int, int]] = []
    for a in range(78, 114):
        b = a + 1
        cls_a = RHYME_CLASSES_MUFASSAL_SHORT.get(a)
        cls_b = RHYME_CLASSES_MUFASSAL_SHORT.get(b)
        if cls_a is not None and cls_a == cls_b:
            extra.append((a, b))
    return dedup_hinges(baseline_top50 + extra)


def build_cell_M_L(baseline_top50: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return dedup_hinges(baseline_top50 + M_L_PAIRS_1INDEXED)


def build_cell_M_B(baseline_top50: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """M_B adds no new hinges; it restricts the 2-opt moveset via sub-block partition."""
    return list(baseline_top50)


def dedup_hinges(hinges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    seen: set[tuple[int, int]] = set()
    out: list[tuple[int, int]] = []
    for pair in hinges:
        if pair in seen:
            continue
        seen.add(pair)
        out.append(pair)
    return out


def mufassal_short_sub_block_position_segments() -> list[list[int]]:
    """Position segments within mufassal_short corresponding to the 3 pre-committed sub-blocks.

    The mufassal_short block occupies tour positions 77..113 (0-indexed), 37 positions total,
    one position per surah Q 78..114 in canonical order. The sub-blocks are:
      B1 = Q 78-88  -> positions 77..87
      B2 = Q 89-107 -> positions 88..106
      B3 = Q 108-114-> positions 107..113
    """
    return [
        list(range(77, 88)),
        list(range(88, 107)),
        list(range(107, 114)),
    ]


def verify_sub_block_constraint(tour: list[int], segments: list[list[int]]) -> bool:
    """After running, confirm that every surah remains in its pre-committed sub-block segment."""
    for seg in segments:
        expected_members = {pos + 1 for pos in seg}  # 1-indexed surahs
        actual = {tour[pos] + 1 for pos in seg}
        if expected_members != actual:
            return False
    return True


# ---------------------------------------------------------------------------
# Per-cell runner
# ---------------------------------------------------------------------------


def run_cell(
    cell_name: str,
    seed_offset: int,
    hinges_1indexed: list[tuple[int, int]],
    dmat: list[list[float]],
    use_sub_block: bool = False,
) -> dict:
    within_hinges, cross_hinges = classify_hinges(hinges_1indexed)
    hinges_0indexed = [(a - 1, b - 1) for a, b in hinges_1indexed]
    hinge_set = set(hinges_0indexed)

    sub_block_segments = mufassal_short_sub_block_position_segments() if use_sub_block else None
    mufassal_sub_blocks_1i = M_B_SUBBLOCKS_1INDEXED if use_sub_block else None
    cell_valid_pairs = valid_pairs_for_sa(sub_block_segments)

    sim_results = []
    sa_stats = []

    for sim_idx in range(N_SIM):
        rng = random.Random(SEED + seed_offset + sim_idx)
        init = initial_hinge_respecting_tour(
            rng, within_hinges, cross_hinges, hinges_0indexed,
            mufassal_sub_blocks_1indexed=mufassal_sub_blocks_1i,
        )
        final, stats = sa_with_constraints(init, dmat, rng, hinge_set, cell_valid_pairs)
        if not all_hinges_ok(final, hinges_0indexed):
            failed = {k: v for k, v in verify_hinges(final, hinges_0indexed).items() if not v}
            raise AssertionError(f"{cell_name}: hinge verification failed for sim {sim_idx}: {failed}")
        if use_sub_block:
            if not verify_sub_block_constraint(final, sub_block_segments):
                raise AssertionError(f"{cell_name}: sub-block constraint violated at sim {sim_idx}")
        obs = compute_observables(final, dmat)
        obs["sim_idx"] = sim_idx
        sim_results.append(obs)
        sa_stats.append(stats)

    return {
        "within_hinges_1indexed": [(a + 1, b + 1) for a, b in within_hinges],
        "cross_hinges_1indexed": [(a + 1, b + 1) for a, b in cross_hinges],
        "hinges_1indexed": hinges_1indexed,
        "use_sub_block": use_sub_block,
        "valid_pairs_count": len(cell_valid_pairs),
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

    # Primary pre-reg criterion: L_mufassal_short percentile under sim
    mufassal_pct = full_analysis["L_mufassal_short"]["sim_percentile_of_empirical"]
    mufassal_pass_97_5 = mufassal_pct <= 97.5
    l_path_inside = full_analysis["L_path"]["sim_inside_95ci"]
    pass_strict = bool(mufassal_pass_97_5 and l_path_inside)
    mufassal_z = block_stat["per_block"]["L_mufassal_short"]["sim_z"]
    pass_loose = bool(math.isfinite(mufassal_z) and mufassal_z <= 2.0)

    if pass_strict:
        verdict = "MECHANISM-CLOSES-STRICT"
    elif pass_loose and not l_path_inside:
        verdict = "PARSIMONY-CONFLICT"
    elif pass_loose and l_path_inside:
        verdict = "MECHANISM-CLOSES-LOOSE"
    elif not mufassal_pass_97_5 and l_path_inside:
        verdict = "MECHANISM-NULL"
    else:
        verdict = "MECHANISM-BROKEN"

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
        "mufassal_short_sim_percentile": mufassal_pct,
        "mufassal_short_sim_z": mufassal_z,
        "l_path_inside_sim_95ci": l_path_inside,
        "pass_strict": pass_strict,
        "pass_loose": pass_loose,
        "cell_verdict": verdict,
        "sim_summaries": {
            key: summarize_distribution([row[key] for row in cell_run["sim_results"]])
            for key in ["L_path", "W_wrap", "L_tiwal", "L_hawamim", "L_mufassal_short", "L_tail_91_114"]
        },
        "sa_summary": cell_run["sa_summary"],
        "valid_pairs_count": cell_run["valid_pairs_count"],
        "sim_samples": cell_run["sim_results"][:25],
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print("=" * 78)
    print("H-NEW-236.1b - Mufassal-short terminal-block mechanism test")
    print("=" * 78)
    print(f"Seed={SEED}; N_SIM={N_SIM}; N_RANDOM={N_RANDOM}; SA_ITERS={SA_ITERS}")

    dmat = load_d_matrix()
    parent_stats = load_parent_mufassal_short_stats()
    prereg_hash = prereg_sha256()
    print(f"Pre-reg SHA-256: {prereg_hash}")
    print(
        "Parent H-NEW-236.1a top-50 mufassal-short sim: "
        f"mean={parent_stats['mufassal_short_sim_mean']:.6f}, "
        f"std={parent_stats['mufassal_short_sim_std']:.6f}, "
        f"z={parent_stats['mufassal_short_sim_z']:.4f}"
    )

    baseline_top50 = build_baseline_top50(dmat)

    # Each cell's hinge set
    cells_spec = [
        ("mw5_positive_control_top50", 0, baseline_top50, False),
        ("cell_M_H_top100", 100_000, build_cell_M_H(dmat), False),
        ("cell_M_R_rhyme", 200_000, build_cell_M_R(baseline_top50), False),
        ("cell_M_L_liturgical", 300_000, build_cell_M_L(baseline_top50), False),
        ("cell_M_B_subblock", 400_000, build_cell_M_B(baseline_top50), True),
    ]

    empirical_tour = list(range(114))
    empirical = compute_observables(empirical_tour, dmat)
    print("\nEmpirical observables:")
    for key, value in empirical.items():
        print(f"  {key:22s} = {value:.6f}")

    print("\nRunning shared random null (MW-5 calibration)...")
    rand_results = []
    for k in range(N_RANDOM):
        rand_results.append(simulate_random(k, dmat))
        if (k + 1) % 250 == 0:
            print(f"  random {k + 1}/{N_RANDOM}")

    cell_outputs = {}
    for cell_name, seed_offset, hinges, use_sub_block in cells_spec:
        print(f"\n-- Running {cell_name} (|hinges|={len(hinges)}; use_sub_block={use_sub_block})...")
        cell_run = run_cell(cell_name, seed_offset, hinges, dmat, use_sub_block=use_sub_block)
        analysis = analyze_cell(cell_run, empirical, rand_results)
        cell_outputs[cell_name] = {
            "hinges_1indexed": hinges,
            "within_hinges_1indexed": cell_run["within_hinges_1indexed"],
            "cross_hinges_1indexed": cell_run["cross_hinges_1indexed"],
            "use_sub_block": use_sub_block,
            "valid_pairs_count": cell_run["valid_pairs_count"],
            **analysis,
        }
        fa = analysis["full_analysis"]
        ms = analysis["mufassal_short_sim_percentile"]
        ms_z = analysis["mufassal_short_sim_z"]
        lp_in = analysis["l_path_inside_sim_95ci"]
        verdict = analysis["cell_verdict"]
        print(
            f"   verdict={verdict:26s}  "
            f"mufassal_short: pct={ms:6.2f}  z={ms_z:+7.3f}  "
            f"L_path inside={lp_in}  "
            f"sim_passes={analysis['sim_passes']}/4"
        )

    # MW-5 positive control check
    pc = cell_outputs["mw5_positive_control_top50"]
    pc_z = pc["mufassal_short_sim_z"]
    parent_z = parent_stats["mufassal_short_sim_z"]
    pc_ok = math.isfinite(pc_z) and abs(pc_z - parent_z) <= 2.0
    print(
        f"\nMW-5 positive control: top-50 baseline mufassal-short z = {pc_z:+.3f} "
        f"(parent {parent_z:+.3f}; tol |delta|<=2.0 => {'OK' if pc_ok else 'FAIL'})"
    )

    # Overall verdict
    mechanism_cells = [k for k in cell_outputs if k.startswith("cell_M_")]
    any_strict = any(cell_outputs[c]["pass_strict"] for c in mechanism_cells)
    any_loose = any(cell_outputs[c]["pass_loose"] for c in mechanism_cells)
    strict_pass_cells = [c for c in mechanism_cells if cell_outputs[c]["pass_strict"]]
    loose_pass_cells = [c for c in mechanism_cells if cell_outputs[c]["pass_loose"]]

    if any_strict:
        oq15_verdict = "OQ-15 CAUSAL-GENERATIVE-LAYER CONFIRMED"
    elif any_loose:
        oq15_verdict = "PARSIMONY-CONFLICT or loose-pass only; layer remains NEAR-COMPLETE"
    else:
        oq15_verdict = "NO MECHANISM CLOSES; layer remains NEAR-COMPLETE with R12a OPEN"

    print(f"\nPre-reg k=4 alpha_bon=0.0125; MW-5 positive control: {'OK' if pc_ok else 'FAIL'}")
    print(f"Strict-pass cells: {strict_pass_cells}")
    print(f"Loose-pass cells:  {loose_pass_cells}")
    print(f"Overall verdict:   {oq15_verdict}")

    output = {
        "finding_id": "h-new-236-1b",
        "title": "Mufassal-short terminal-block mechanism test (M_H / M_R / M_L / M_B)",
        "pre_reg_sha256": prereg_hash,
        "parent": "h-new-236-1a",
        "grandparent": "h-new-236-1 -> h-new-236 -> cross-finding-020",
        "seed": SEED,
        "n_sim": N_SIM,
        "n_random": N_RANDOM,
        "sa_iters": SA_ITERS,
        "bonferroni_k": 4,
        "alpha_bon": 0.0125,
        "rules_tuple": (
            "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, "
            "QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, "
            "stochastic 2-opt with classical-block + Q1-lock + length-stratification "
            "+ M2-muq + TOP-50-HINGE-BASELINE + per-cell mechanism-constraint, seed 20260420)"
        ),
        "parent_stats_reproduced": parent_stats,
        "mw5_positive_control_pass": pc_ok,
        "mw5_positive_control_z": pc_z,
        "empirical": empirical,
        "rhyme_class_assignment": RHYME_CLASSES_MUFASSAL_SHORT,
        "liturgical_pairs_1indexed": M_L_PAIRS_1INDEXED,
        "sub_blocks_1indexed": M_B_SUBBLOCKS_1INDEXED,
        "random_baseline_summaries": {
            key: summarize_distribution([row[key] for row in rand_results])
            for key in ["L_path", "W_wrap", "L_tiwal", "L_hawamim", "L_mufassal_short", "L_tail_91_114"]
        },
        "cells": cell_outputs,
        "strict_pass_cells": strict_pass_cells,
        "loose_pass_cells": loose_pass_cells,
        "any_strict": any_strict,
        "any_loose": any_loose,
        "oq15_causal_generative_verdict": oq15_verdict,
    }

    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
