#!/usr/bin/env python3
"""H-NEW-236.1 — Hinges-constrained generative simulator.

Pre-reg: findings/phase-b-hypotheses/h-new-236-1-hinges-constrained-simulator-prereg.md
Pre-reg SHA-256: b23f5cd6994567db74152ada7393747f740857f6766877e19f9c641dd3c696ee

Parent: h-new-236 (primary generative simulator; PARTIALLY-COMPLETE 2/4).
Grandparent: cross-finding-020 (the complete equation).

Extends H-NEW-236 by injecting H-NEW-130's 15 top-jumps (including the 3
universal hinges Q 14→15, Q 49→50, Q 56→57 as a subset) as HARD CONSTRAINTS:
every sampled ordering is required to preserve each hinge as an adjacency.

Seed 20260419.
"""

from __future__ import annotations

import json
import random
import statistics
from pathlib import Path

SEED = 20260419
N_SIM = 1000
N_RANDOM = 1000
SA_ITERS = 200
T_HOT = 0.05
T_COLD = 0.001

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H111_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1.json"

# ---------------------------------------------------------------------------
# Classical-block partition (inherited from H-NEW-236; LOCKED pre-reg)
# ---------------------------------------------------------------------------
BLOCKS_1INDEXED = {
    "fatiha":          list(range(1, 2)),      # Q 1 only
    "tiwal":           list(range(2, 10)),     # Q 2-9
    "middle_pre_hm":   list(range(10, 40)),    # Q 10-39
    "hawamim":         list(range(40, 47)),    # Q 40-46
    "middle_post_hm":  list(range(47, 49)),    # Q 47-48
    "mufassal_long":   list(range(49, 78)),    # Q 49-77
    "mufassal_short":  list(range(78, 115)),   # Q 78-114
}

BLOCK_ORDER = [
    "fatiha", "tiwal", "middle_pre_hm", "hawamim",
    "middle_post_hm", "mufassal_long", "mufassal_short",
]

# ---------------------------------------------------------------------------
# HINGE SET (H-NEW-130 top-15 + 3 universal; 15 unique; LOCKED pre-reg)
# ---------------------------------------------------------------------------
# Each hinge is a (surah_a, surah_b) pair, 1-indexed, meaning surah_b must
# immediately follow surah_a. The 3 universal hinges (Q 14→15, Q 49→50,
# Q 56→57) are already in the top-15 so the set is the top-15 as-is.
HINGES_1INDEXED = [
    (1, 2), (54, 55), (55, 56), (32, 33), (24, 25), (56, 57), (33, 34),
    (9, 10), (12, 13), (23, 24), (7, 8), (14, 15), (53, 54), (49, 50),
    (15, 16),
]
# 0-indexed form
HINGES = [(a - 1, b - 1) for (a, b) in HINGES_1INDEXED]

# Cross-block hinges (structural locks; both coincide with canonical block
# boundaries and are enforced by initialization, not 2-opt rejection):
#   Q 1→2  : fatiha→tiwal (Q 1 locked at pos 0; Q 2 locked at pos 1 = first tiwal slot)
#   Q 9→10 : tiwal→middle_pre_hm (Q 9 locked at pos 8 = last tiwal slot; Q 10 at pos 9)
CROSS_BLOCK_HINGES = [(1, 2), (9, 10)]
CROSS_BLOCK_HINGES_0 = [(a - 1, b - 1) for (a, b) in CROSS_BLOCK_HINGES]

# Within-block hinges (enforced by 2-opt rejection):
WITHIN_BLOCK_HINGES_1 = [
    (7, 8), (12, 13), (14, 15), (15, 16),
    (23, 24), (24, 25), (32, 33), (33, 34),
    (49, 50), (53, 54), (54, 55), (55, 56), (56, 57),
]
WITHIN_BLOCK_HINGES = [(a - 1, b - 1) for (a, b) in WITHIN_BLOCK_HINGES_1]


def load_d_matrix() -> list[list[float]]:
    with H111_JSON.open() as f:
        parent = json.load(f)
    n = 114
    D = [[0.0] * n for _ in range(n)]
    for i, j, d in parent["D_matrix_upper_triangular"]:
        D[i - 1][j - 1] = float(d)
        D[j - 1][i - 1] = float(d)
    return D


def path_length(tour: list[int], D: list[list[float]]) -> float:
    total = 0.0
    n = len(tour)
    for i in range(n - 1):
        total += D[tour[i]][tour[i + 1]]
    return total


def wrap_edge(tour: list[int], D: list[list[float]]) -> float:
    return D[tour[-1]][tour[0]]


def tail_cost(tour: list[int], D: list[list[float]], start_pos: int = 90) -> float:
    total = 0.0
    for i in range(start_pos, len(tour) - 1):
        total += D[tour[i]][tour[i + 1]]
    return total


def block_cost(tour: list[int], D: list[list[float]], positions: list[int]) -> float:
    total = 0.0
    positions_sorted = sorted(positions)
    for a, b in zip(positions_sorted, positions_sorted[1:]):
        if b == a + 1:
            total += D[tour[a]][tour[b]]
    return total


def compute_observables(tour: list[int], D: list[list[float]]) -> dict:
    l_path = path_length(tour, D)
    w = wrap_edge(tour, D)
    l_tail = tail_cost(tour, D, start_pos=90)
    tiwal_positions = list(range(1, 9))
    hawamim_positions = list(range(39, 46))
    mufassal_short_positions = list(range(77, 114))
    l_tiwal = block_cost(tour, D, tiwal_positions)
    l_hawamim = block_cost(tour, D, hawamim_positions)
    l_mufassal_short = block_cost(tour, D, mufassal_short_positions)
    return {
        "L_path": l_path,
        "W_wrap": w,
        "L_tiwal": l_tiwal,
        "L_hawamim": l_hawamim,
        "L_mufassal_short": l_mufassal_short,
        "L_tail_91_114": l_tail,
    }


# ---------------------------------------------------------------------------
# Hinge verification
# ---------------------------------------------------------------------------
def verify_hinges(tour: list[int]) -> dict:
    """Return dict of {hinge: True/False} indicating whether each hinge is preserved."""
    pos = {s: i for i, s in enumerate(tour)}
    result = {}
    for (a, b) in HINGES:
        result[(a + 1, b + 1)] = (pos[b] == pos[a] + 1)
    return result


def all_hinges_ok(tour: list[int]) -> bool:
    return all(verify_hinges(tour).values())


# ---------------------------------------------------------------------------
# Hinge-respecting within-block construction
# ---------------------------------------------------------------------------
def build_hinge_chains_for_block(block_members: list[int]) -> list[list[int]]:
    """For a given block (0-indexed members), collapse within-block hinges into chains.

    Returns a list of chains; each chain is a list of 0-indexed surahs that
    must appear as a contiguous run in the block's ordering.
    """
    # Build a graph: for each within-block hinge (a, b) where both a and b
    # are in block_members, add edge a→b.
    in_block = set(block_members)
    succ = {}   # a -> b
    pred = {}   # b -> a
    for (a, b) in WITHIN_BLOCK_HINGES:
        if a in in_block and b in in_block:
            if a in succ:
                # Should not happen for the locked 15 hinges; defensive.
                raise AssertionError(f"Hinge conflict: surah {a+1} has two successors ({succ[a]+1}, {b+1})")
            if b in pred:
                raise AssertionError(f"Hinge conflict: surah {b+1} has two predecessors ({pred[b]+1}, {a+1})")
            succ[a] = b
            pred[b] = a
    # Build chains
    chains = []
    visited = set()
    for s in block_members:
        if s in visited or s in pred:
            # not a chain head
            continue
        chain = [s]
        visited.add(s)
        cur = s
        while cur in succ:
            nxt = succ[cur]
            chain.append(nxt)
            visited.add(nxt)
            cur = nxt
        chains.append(chain)
    # Handle any surahs in cycles (shouldn't occur for the locked 15 hinges, but defensive)
    for s in block_members:
        if s not in visited:
            chain = [s]
            visited.add(s)
            cur = s
            while cur in succ and succ[cur] not in visited:
                nxt = succ[cur]
                chain.append(nxt)
                visited.add(nxt)
                cur = nxt
            chains.append(chain)
    return chains


def initial_hinge_respecting_tour(rng: random.Random) -> list[int]:
    """Build a tour that respects blocks AND all hinges.

    Strategy: within each block, (a) build the chain structure from within-block
    hinges, (b) shuffle the chains, (c) concatenate in shuffled order. For
    cross-block hinges Q 1→2 and Q 9→10: Q 1 is locked at position 0 (fatiha
    singleton), Q 2 is FORCED to be the first member of the tiwal block's
    shuffle (so Q 2 lands at position 1), and Q 9 is FORCED to be the last
    member of tiwal (position 8) with Q 10 forced to be first of
    middle_pre_hm (position 9).
    """
    tour_0indexed: list[int] = []
    for block_name in BLOCK_ORDER:
        members = [s - 1 for s in BLOCKS_1INDEXED[block_name]]
        chains = build_hinge_chains_for_block(members)
        # Cross-block hinge enforcement
        if block_name == "tiwal":
            # Q 2 (surah idx 1) MUST be first; Q 9 (surah idx 8) MUST be last
            # Within tiwal we also have within-block hinge (7, 8), so chain [6, 7]
            # exists. Q 9 is its own chain unless also hinged; check. (9 is idx 8;
            # no within-block hinge has idx 8 as source or target within tiwal.)
            # Start with Q 2's chain; end with Q 9's chain.
            q2_chain = None
            q9_chain = None
            other_chains = []
            for c in chains:
                if c[0] == 1:        # Q 2 idx 1
                    q2_chain = c
                elif c[-1] == 8:      # Q 9 idx 8
                    q9_chain = c
                else:
                    other_chains.append(c)
            if q2_chain is None:
                raise AssertionError("tiwal: no chain starts with Q 2")
            if q9_chain is None:
                # Q 9 is a standalone; find the chain containing idx 8 and require it ends with 8
                for c in list(other_chains):
                    if 8 in c:
                        if c[-1] != 8:
                            raise AssertionError(f"Q 9 must be last in its chain; got {c}")
                        q9_chain = c
                        other_chains.remove(c)
                        break
            if q9_chain is None:
                raise AssertionError("tiwal: Q 9 not found in any chain")
            rng.shuffle(other_chains)
            ordered_chains = [q2_chain] + other_chains + [q9_chain]
        elif block_name == "middle_pre_hm":
            # Q 10 (idx 9) MUST be first (cross-block hinge Q 9→10 locks this)
            q10_chain = None
            other_chains = []
            for c in chains:
                if c[0] == 9:
                    q10_chain = c
                else:
                    other_chains.append(c)
            if q10_chain is None:
                # Q 10 might be inside a chain; check
                for c in list(chains):
                    if 9 in c:
                        if c[0] != 9:
                            raise AssertionError(f"Q 10 must be first in its chain; got {c}")
                        q10_chain = c
                        break
                other_chains = [c for c in chains if c is not q10_chain]
            rng.shuffle(other_chains)
            ordered_chains = [q10_chain] + other_chains
        else:
            rng.shuffle(chains)
            ordered_chains = chains
        for c in ordered_chains:
            tour_0indexed.extend(c)
    assert len(tour_0indexed) == 114, f"Tour has {len(tour_0indexed)} surahs, expected 114"
    # Verify all hinges
    if not all_hinges_ok(tour_0indexed):
        failed = {k: v for k, v in verify_hinges(tour_0indexed).items() if not v}
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
POSITION_BLOCK = [None] * 114
for block_name, positions in POSITION_RANGES.items():
    for p in positions:
        POSITION_BLOCK[p] = block_name


# ---------------------------------------------------------------------------
# Hinge-respecting SA 2-opt
# ---------------------------------------------------------------------------
def swap_breaks_hinge(tour: list[int], pa: int, pb: int) -> bool:
    """Return True if the 2-opt reversal of tour[pa..pb] would break any
    within-block hinge (a adjacent → b adjacent requirement).

    A 2-opt reversal changes:
      - edge (pa-1, pa) → (pa-1, pb)      [broken if (tour[pa-1], tour[pa]) is a hinge]
      - edge (pb, pb+1) → (pa, pb+1)      [broken if (tour[pb], tour[pb+1]) is a hinge]
      - internal direction reversed: internal edges become (tour[i+1], tour[i])
        for i in [pa..pb-1]. For each internal pair (tour[i], tour[i+1]) that
        is a hinge (a, b), the reversal puts b before a in the tour, which
        BREAKS the hinge.
      - new boundary edges (pa-1 -> pb) and (pa -> pb+1): we must also
        check whether (tour[pa-1], tour[pb]) forms a hinge — which would be
        REVERSED, not FORMED, since reversal puts tour[pb] at pa. But per hinge
        rules, (tour[pa-1], tour[pa]_new = tour[pb]) must not NEGATIVELY create
        a backwards hinge. A hinge requires A->B, so creating a new adjacency
        (X, Y) doesn't "break" a hinge unless (Y, X) is a hinge and Y must come
        BEFORE X always — no such "inverse hinge" rule; we only enforce the
        existing hinge set. So the check is: the EXISTING hinges that were
        preserved before must remain preserved after.
    """
    hinge_set = set(WITHIN_BLOCK_HINGES) | set(CROSS_BLOCK_HINGES_0)
    n = len(tour)

    # 1. Check broken left-edge hinge: tour[pa-1], tour[pa] currently adjacent;
    #    after reversal the new pair is tour[pa-1], tour[pb]. If (tour[pa-1],
    #    tour[pa]) was a hinge, this breaks it UNLESS pa==0.
    if pa - 1 >= 0:
        if (tour[pa - 1], tour[pa]) in hinge_set:
            return True
    # 2. Right-edge hinge: tour[pb], tour[pb+1]. After reversal the new pair is
    #    tour[pa], tour[pb+1]. Broken if (tour[pb], tour[pb+1]) was a hinge.
    if pb + 1 < n:
        if (tour[pb], tour[pb + 1]) in hinge_set:
            return True
    # 3. Internal hinges: for each interior adjacency (tour[i], tour[i+1]),
    #    the reversal puts tour[i+1] at position (pa+pb-i-1) and tour[i] at
    #    (pa+pb-i). The new adjacency is (tour[i+1], tour[i]), which breaks
    #    the hinge (tour[i], tour[i+1]) if it was a hinge.
    for i in range(pa, pb):
        if (tour[i], tour[i + 1]) in hinge_set:
            return True
    return False


def sa_within_block_hinge_respecting(tour: list[int], D: list[list[float]],
                                     rng: random.Random,
                                     n_iters: int = SA_ITERS) -> list[int]:
    """Simulated-annealing 2-opt with within-block swaps AND hinge preservation.

    Q 1 (position 0) is LOCKED. Q 2 (position 1) is LOCKED (cross-block hinge
    Q 1→2). Q 9 (position 8) and Q 10 (position 9) are LOCKED (cross-block
    hinge). Additional within-block hinges are preserved by 2-opt rejection.
    """
    import math
    current = list(tour)
    current_len = path_length(current, D)
    n = len(current)
    valid_pairs = []
    for block_name, positions in POSITION_RANGES.items():
        if block_name == "fatiha":
            continue
        for idx_a in range(len(positions)):
            for idx_b in range(idx_a + 1, len(positions)):
                pa, pb = positions[idx_a], positions[idx_b]
                if pa >= 1:  # Q1 lock
                    # Also exclude the cross-block-hinge locked positions:
                    # pa == 1 (Q 2 locked), pa == 8 (Q 9 locked), pa == 9 (Q 10 locked),
                    # pb in {1, 8, 9}
                    if pa in (1, 8, 9) or pb in (1, 8, 9):
                        continue
                    valid_pairs.append((pa, pb))

    accept_count = 0
    reject_by_hinge = 0
    reject_by_sa = 0
    for it in range(n_iters):
        frac = it / max(1, n_iters - 1)
        T = T_HOT + frac * (T_COLD - T_HOT)
        rng.shuffle(valid_pairs)
        batch_size = min(300, len(valid_pairs))
        for pa, pb in valid_pairs[:batch_size]:
            # Reject if hinge-breaking
            if swap_breaks_hinge(current, pa, pb):
                reject_by_hinge += 1
                continue
            left = current[pa - 1]
            right = current[pb + 1] if pb + 1 < n else None
            a = current[pa]
            b = current[pb]
            if right is None:
                continue
            old_cost = D[left][a] + D[b][right]
            new_cost = D[left][b] + D[a][right]
            delta = new_cost - old_cost
            if delta < 0:
                current[pa:pb + 1] = current[pa:pb + 1][::-1]
                current_len += delta
                accept_count += 1
            else:
                if T > 1e-9:
                    p = math.exp(-delta / T) if delta / T < 50 else 0.0
                else:
                    p = 0.0
                if rng.random() < p:
                    current[pa:pb + 1] = current[pa:pb + 1][::-1]
                    current_len += delta
                    accept_count += 1
                else:
                    reject_by_sa += 1
    return current, {"accepted": accept_count,
                     "rejected_by_hinge": reject_by_hinge,
                     "rejected_by_sa": reject_by_sa}


def simulate_one(sim_idx: int, D: list[list[float]]) -> dict:
    rng = random.Random(SEED + sim_idx)
    init = initial_hinge_respecting_tour(rng)
    final, sa_stats = sa_within_block_hinge_respecting(init, D, rng)
    # MW-HINGE check
    if not all_hinges_ok(final):
        failed = {k: v for k, v in verify_hinges(final).items() if not v}
        raise AssertionError(f"sim {sim_idx}: hinge verification FAILED {failed}")
    obs = compute_observables(final, D)
    obs["sim_idx"] = sim_idx
    return obs


def simulate_random(rand_idx: int, D: list[list[float]]) -> dict:
    """Unconstrained random permutation (MW-5 calibration; UNCHANGED from H-NEW-236)."""
    rng = random.Random(SEED + 100_000 + rand_idx)
    perm = list(range(114))
    rng.shuffle(perm)
    obs = compute_observables(perm, D)
    obs["rand_idx"] = rand_idx
    return obs


# ---------------------------------------------------------------------------
# Percentile + decision
# ---------------------------------------------------------------------------
def percentile_of(value: float, distribution: list[float]) -> float:
    n = len(distribution)
    rank = sum(1 for v in distribution if v <= value)
    return 100.0 * rank / n


def ci_95(distribution: list[float]) -> tuple[float, float]:
    s = sorted(distribution)
    n = len(s)
    lo_idx = int(0.025 * n)
    hi_idx = int(0.975 * n) - 1
    hi_idx = max(hi_idx, 0)
    return s[lo_idx], s[hi_idx]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    random.seed(SEED)
    print("=" * 70)
    print("H-NEW-236.1 — Hinges-constrained 4-principle + M1.3 generative simulator")
    print("=" * 70)
    print(f"Seed: {SEED}; N_SIM={N_SIM}; N_RANDOM={N_RANDOM}; SA_ITERS={SA_ITERS}")
    print(f"Hinges (15 unique): {HINGES_1INDEXED}")
    print(f"Cross-block hinges (structural lock): {CROSS_BLOCK_HINGES}")
    print(f"Within-block hinges (2-opt rejection): {WITHIN_BLOCK_HINGES_1}")
    print()

    print("Loading Fisher-Rao D-matrix (h-new-111.json)…")
    D = load_d_matrix()
    print(f"  D is 114x114; D[0][1]={D[0][1]:.4f}, D[0][113]={D[0][113]:.4f}")

    empirical_tour = list(range(114))
    empirical = compute_observables(empirical_tour, D)
    print()
    print("Empirical mushaf observables:")
    for k, v in empirical.items():
        print(f"  {k:22s} = {v:.4f}")
    assert abs(empirical["L_path"] - 85.76) < 0.5, \
        f"MW-1 FAIL: empirical L_path = {empirical['L_path']:.3f}, expected ~85.76"
    print(f"  MW-1 PASS: L_path = {empirical['L_path']:.3f} matches H-NEW-111 (~85.76)")
    # Verify empirical mushaf satisfies all hinges (sanity: the 15 hinges
    # are by construction contiguous pairs in canonical mushaf)
    emp_hinge_status = verify_hinges(empirical_tour)
    assert all(emp_hinge_status.values()), \
        f"Empirical mushaf violates some hinges: {emp_hinge_status}"
    print(f"  MW-HINGE PASS (empirical): all 15 hinges satisfied in canonical mushaf")

    print()
    print(f"Running {N_SIM} hinges-constrained generative simulations…")
    sim_results: list[dict] = []
    for k in range(N_SIM):
        res = simulate_one(k, D)
        sim_results.append(res)
        if (k + 1) % 100 == 0:
            print(f"  simulated {k + 1}/{N_SIM}; L_path={res['L_path']:.3f}")
    print(f"  Done {N_SIM} simulations.")

    print()
    print(f"Running {N_RANDOM} random permutations (MW-5 calibration)…")
    rand_results: list[dict] = []
    for k in range(N_RANDOM):
        res = simulate_random(k, D)
        rand_results.append(res)
        if (k + 1) % 250 == 0:
            print(f"  random {k + 1}/{N_RANDOM}")
    print(f"  Done {N_RANDOM} random permutations.")

    obs_names = ["L_path", "W_wrap", "L_tiwal", "L_hawamim",
                 "L_mufassal_short", "L_tail_91_114"]

    def series(name: str, src: list[dict]) -> list[float]:
        return [r[name] for r in src]

    sim_dist = {n: series(n, sim_results) for n in obs_names}
    rand_dist = {n: series(n, rand_results) for n in obs_names}

    def analyse(obs_name: str, emp_val: float) -> dict:
        sim_vals = sim_dist[obs_name]
        rand_vals = rand_dist[obs_name]
        sim_lo, sim_hi = ci_95(sim_vals)
        rand_lo, rand_hi = ci_95(rand_vals)
        sim_pct = percentile_of(emp_val, sim_vals)
        rand_pct = percentile_of(emp_val, rand_vals)
        sim_inside = sim_lo <= emp_val <= sim_hi
        rand_inside = rand_lo <= emp_val <= rand_hi
        return {
            "observable": obs_name,
            "empirical": emp_val,
            "sim_mean": statistics.mean(sim_vals),
            "sim_std": statistics.pstdev(sim_vals),
            "sim_ci_lo": sim_lo,
            "sim_ci_hi": sim_hi,
            "sim_percentile_of_empirical": sim_pct,
            "sim_inside_95ci": sim_inside,
            "rand_mean": statistics.mean(rand_vals),
            "rand_std": statistics.pstdev(rand_vals),
            "rand_ci_lo": rand_lo,
            "rand_ci_hi": rand_hi,
            "rand_percentile_of_empirical": rand_pct,
            "rand_inside_95ci": rand_inside,
        }

    analysis = {}
    for n in obs_names:
        analysis[n] = analyse(n, empirical[n])

    # Block-χ² statistic (same formula as H-NEW-236)
    def block_stat_for(res_list):
        means = {b: statistics.mean(series(b, res_list))
                 for b in ["L_tiwal", "L_hawamim", "L_mufassal_short"]}
        stds = {b: max(statistics.pstdev(series(b, res_list)), 1e-9)
                for b in ["L_tiwal", "L_hawamim", "L_mufassal_short"]}
        sums = []
        for r in res_list:
            z_tiwal = (r["L_tiwal"] - means["L_tiwal"]) / stds["L_tiwal"]
            z_hm = (r["L_hawamim"] - means["L_hawamim"]) / stds["L_hawamim"]
            z_ms = (r["L_mufassal_short"] - means["L_mufassal_short"]) / stds["L_mufassal_short"]
            sums.append(z_tiwal ** 2 + z_hm ** 2 + z_ms ** 2)
        return sums, means, stds

    sim_block_stat, sim_block_means, sim_block_stds = block_stat_for(sim_results)
    rand_block_stat, rand_block_means, rand_block_stds = block_stat_for(rand_results)

    emp_block_stat_sim = (
        ((empirical["L_tiwal"] - sim_block_means["L_tiwal"]) / sim_block_stds["L_tiwal"]) ** 2 +
        ((empirical["L_hawamim"] - sim_block_means["L_hawamim"]) / sim_block_stds["L_hawamim"]) ** 2 +
        ((empirical["L_mufassal_short"] - sim_block_means["L_mufassal_short"]) / sim_block_stds["L_mufassal_short"]) ** 2
    )
    emp_block_stat_rand = (
        ((empirical["L_tiwal"] - rand_block_means["L_tiwal"]) / rand_block_stds["L_tiwal"]) ** 2 +
        ((empirical["L_hawamim"] - rand_block_means["L_hawamim"]) / rand_block_stds["L_hawamim"]) ** 2 +
        ((empirical["L_mufassal_short"] - rand_block_means["L_mufassal_short"]) / rand_block_stds["L_mufassal_short"]) ** 2
    )

    sim_block_97_5 = sorted(sim_block_stat)[int(0.975 * len(sim_block_stat)) - 1]
    rand_block_97_5 = sorted(rand_block_stat)[int(0.975 * len(rand_block_stat)) - 1]
    sim_block_pct = percentile_of(emp_block_stat_sim, sim_block_stat)
    rand_block_pct = percentile_of(emp_block_stat_rand, rand_block_stat)

    primary_obs = {
        "O1_L_path":       analysis["L_path"],
        "O2_W_wrap":       analysis["W_wrap"],
        "O3_block_chi2":   {
            "empirical_stat_under_sim":  emp_block_stat_sim,
            "empirical_stat_under_rand": emp_block_stat_rand,
            "sim_97_5th_pct":            sim_block_97_5,
            "rand_97_5th_pct":           rand_block_97_5,
            "sim_percentile_of_empirical":  sim_block_pct,
            "rand_percentile_of_empirical": rand_block_pct,
            "sim_inside_95ci":  emp_block_stat_sim <= sim_block_97_5,
            "rand_inside_95ci": emp_block_stat_rand <= rand_block_97_5,
            "sim_block_means": sim_block_means,
            "sim_block_stds":  sim_block_stds,
        },
        "O4_L_tail_91_114": analysis["L_tail_91_114"],
    }

    sim_passes = (
        int(primary_obs["O1_L_path"]["sim_inside_95ci"])
        + int(primary_obs["O2_W_wrap"]["sim_inside_95ci"])
        + int(primary_obs["O3_block_chi2"]["sim_inside_95ci"])
        + int(primary_obs["O4_L_tail_91_114"]["sim_inside_95ci"])
    )
    rand_passes = (
        int(primary_obs["O1_L_path"]["rand_inside_95ci"])
        + int(primary_obs["O2_W_wrap"]["rand_inside_95ci"])
        + int(primary_obs["O3_block_chi2"]["rand_inside_95ci"])
        + int(primary_obs["O4_L_tail_91_114"]["rand_inside_95ci"])
    )

    # Primary-cell decision for this pre-reg
    primary_pct = primary_obs["O1_L_path"]["sim_percentile_of_empirical"]
    primary_inside_strict = primary_obs["O1_L_path"]["sim_inside_95ci"]
    primary_inside_relaxed = 5.0 <= primary_pct <= 95.0

    if primary_inside_strict:
        primary_verdict = "EQUATION-COMPLETE — M1.3 hinges close the gap; empirical L_path INSIDE sim 95% CI"
    elif primary_inside_relaxed:
        primary_verdict = "NEARLY-COMPLETE — empirical inside [5,95] but not strict 95% CI"
    else:
        # Did the gap narrow vs H-NEW-236?
        sim_mean = primary_obs["O1_L_path"]["sim_mean"]
        emp_val = primary_obs["O1_L_path"]["empirical"]
        gap = emp_val - sim_mean
        h236_gap = 85.76 - 79.45  # 6.31
        if abs(gap) < abs(h236_gap) * 0.5:
            primary_verdict = f"PARTIAL-CLOSURE — gap narrowed ({gap:.2f} vs H-NEW-236's {h236_gap:.2f}); more of residual accounted for"
        elif abs(gap) < abs(h236_gap):
            primary_verdict = f"MINOR-CLOSURE — gap modestly narrowed ({gap:.2f} vs H-NEW-236's {h236_gap:.2f})"
        else:
            primary_verdict = f"NO-CLOSURE — gap unchanged or widened ({gap:.2f} vs H-NEW-236's {h236_gap:.2f}); hinges are NOT the driver"

    if sim_passes == 4:
        overall_verdict = "EQUATION-COMPLETE (4/4 inside 95% CI)"
    elif sim_passes == 3:
        overall_verdict = "NEARLY-COMPLETE (3/4 inside sim CI)"
    elif sim_passes >= 2:
        overall_verdict = f"PARTIALLY-COMPLETE ({sim_passes}/4 inside sim CI)"
    else:
        overall_verdict = f"INSUFFICIENT ({sim_passes}/4 inside sim CI)"

    print()
    print("=" * 70)
    print("PRIMARY DECISION — O1 L_path (k=1 Bonferroni; α_bon=0.05)")
    print("=" * 70)
    print(f"  Primary cell: L_path pct = {primary_pct:.2f}")
    print(f"  Empirical L_path = {primary_obs['O1_L_path']['empirical']:.4f}")
    print(f"  Sim mean L_path  = {primary_obs['O1_L_path']['sim_mean']:.4f}")
    print(f"  Sim std L_path   = {primary_obs['O1_L_path']['sim_std']:.4f}")
    print(f"  Sim 95% CI L_path = [{primary_obs['O1_L_path']['sim_ci_lo']:.4f}, {primary_obs['O1_L_path']['sim_ci_hi']:.4f}]")
    print(f"  INSIDE 95% CI strict?   {primary_inside_strict}")
    print(f"  INSIDE [5, 95] relaxed? {primary_inside_relaxed}")
    print(f"  Primary verdict: {primary_verdict}")
    print()
    print(f"Simulated distribution passes (empirical inside 95% CI): {sim_passes}/4")
    print(f"Random distribution passes (MW-5 calibration):           {rand_passes}/4")
    print()
    for o_name, o_data in primary_obs.items():
        if "observable" in o_data:
            emp = o_data["empirical"]
            sim_lo, sim_hi = o_data["sim_ci_lo"], o_data["sim_ci_hi"]
            sim_in = o_data["sim_inside_95ci"]
            sim_pct = o_data["sim_percentile_of_empirical"]
            rand_lo, rand_hi = o_data["rand_ci_lo"], o_data["rand_ci_hi"]
            rand_in = o_data["rand_inside_95ci"]
            rand_pct = o_data["rand_percentile_of_empirical"]
            print(f"{o_name}:")
            print(f"  empirical = {emp:.4f}")
            print(f"  SIM 95% CI [{sim_lo:.4f}, {sim_hi:.4f}], pct={sim_pct:.1f}, inside={sim_in}")
            print(f"  RAND 95% CI [{rand_lo:.4f}, {rand_hi:.4f}], pct={rand_pct:.1f}, inside={rand_in}")
        else:
            print(f"{o_name}:")
            print(f"  empirical stat (vs sim) = {o_data['empirical_stat_under_sim']:.4f}")
            print(f"  sim 97.5th pct = {o_data['sim_97_5th_pct']:.4f}; inside={o_data['sim_inside_95ci']}")
            print(f"  rand 97.5th pct = {o_data['rand_97_5th_pct']:.4f}; rand inside={o_data['rand_inside_95ci']}")
    print()
    print("=" * 70)
    print(f"OVERALL 4-OBSERVABLE VERDICT: {overall_verdict}")
    print(f"PRIMARY CELL (L_path pct) VERDICT: {primary_verdict}")
    print("=" * 70)

    mw5_expected = rand_passes <= 1
    print()
    print(f"MW-5 sanity: random-null should FAIL ≥3 of 4 (i.e. pass ≤1 of 4):")
    print(f"  random passes = {rand_passes}/4")
    print(f"  MW-5 {'PASS' if mw5_expected else 'FAIL'}: rand_passes={rand_passes}")

    output = {
        "finding_id": "h-new-236-1",
        "title": "Hinges-constrained generative simulator — inject H-NEW-130 15 top-jumps as hard constraints",
        "pre_reg_sha256": "b23f5cd6994567db74152ada7393747f740857f6766877e19f9c641dd3c696ee",
        "parent": "h-new-236",
        "grandparent": "cross-finding-020",
        "seed": SEED,
        "n_sim": N_SIM,
        "n_random": N_RANDOM,
        "sa_iters": SA_ITERS,
        "hinges_1indexed": HINGES_1INDEXED,
        "cross_block_hinges": CROSS_BLOCK_HINGES,
        "within_block_hinges": WITHIN_BLOCK_HINGES_1,
        "empirical": empirical,
        "primary_obs": primary_obs,
        "sim_passes": sim_passes,
        "rand_passes": rand_passes,
        "primary_cell_verdict": primary_verdict,
        "overall_4obs_verdict": overall_verdict,
        "mw5_pass": mw5_expected,
        "rules_tuple": "(no-tashkeel, 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + 15-HINGE-PRESERVATION)",
        "full_analysis": analysis,
        "sim_summaries": {
            n: {
                "mean": statistics.mean(sim_dist[n]),
                "stdev": statistics.pstdev(sim_dist[n]),
                "min":  min(sim_dist[n]),
                "max":  max(sim_dist[n]),
                "q025": sorted(sim_dist[n])[int(0.025 * N_SIM)],
                "q975": sorted(sim_dist[n])[int(0.975 * N_SIM) - 1],
            }
            for n in obs_names
        },
        "rand_summaries": {
            n: {
                "mean": statistics.mean(rand_dist[n]),
                "stdev": statistics.pstdev(rand_dist[n]),
                "min":  min(rand_dist[n]),
                "max":  max(rand_dist[n]),
                "q025": sorted(rand_dist[n])[int(0.025 * N_RANDOM)],
                "q975": sorted(rand_dist[n])[int(0.975 * N_RANDOM) - 1],
            }
            for n in obs_names
        },
        "h236_comparison": {
            "h236_sim_mean_L_path": 79.45,
            "h236_sim_ci_L_path":   [79.28, 79.63],
            "h236_empirical_L_path": 85.76,
            "h236_gap_L_path":       6.31,
            "h236_1_sim_mean_L_path": primary_obs["O1_L_path"]["sim_mean"],
            "h236_1_sim_ci_L_path":  [primary_obs["O1_L_path"]["sim_ci_lo"],
                                       primary_obs["O1_L_path"]["sim_ci_hi"]],
            "h236_1_gap_L_path":      primary_obs["O1_L_path"]["empirical"] - primary_obs["O1_L_path"]["sim_mean"],
        },
        "sim_samples": sim_results[:50],
        "rand_samples": rand_results[:50],
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nWrote {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
