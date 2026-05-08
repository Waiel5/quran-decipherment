#!/usr/bin/env python3
"""
H-NEW-920 — Discrete geodesic curvature of the mushaf path.

Pre-reg: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-920-geodesic-curvature-prereg.md
Pre-reg SHA-256 (locked): 2bd4c93ee87d0a5fac1c7331d16890966f21d46ad5c94455254bc6a915b32758
Seed: 20260507
Permutations: 10000

Computes turn_cost(i) = d_in(i) + d_out(i) - d_skip(i) at every interior position
i ∈ {2,...,113} of the canonical mushaf, then runs a 10000-permutation null over the
same H-NEW-111 FR distance matrix.

H1a: Bonferroni-3 boundary co-incidence test.
  B1 (Mufaṣṣal-onset Q 50, ±2): {48,49,50,51,52}
  B2 (Ḥawāmīm cluster Q 39→Q 40, ±2): {38,39,40,41,42}
  B3 (Medinan-block-onset Q 2): {2,3,4}
  PASS-DIRECTED if ≥2 of 3 cells fire (PASS = perm-p ≤ 0.01667 AND threshold met).
  Joint: ≥4 of top-10 fall inside the union.

H1b: empirical-mean(turn_cost) < perm-null 5th percentile (locally smoother than random).
"""

import json
import math
import hashlib
import random
import os
from collections import Counter

# -----------------------------------------------------------------------------
# 0. CONFIG and SHA verification
# -----------------------------------------------------------------------------
PROJECT = "/Users/grey/Downloads/quran"
PREREG_PATH = os.path.join(
    PROJECT, "findings/phase-b-hypotheses/h-new-920-geodesic-curvature-prereg.md"
)
EXPECTED_SHA = "2bd4c93ee87d0a5fac1c7331d16890966f21d46ad5c94455254bc6a915b32758"
H111_PATH = os.path.join(PROJECT, "findings/phase-b-hypotheses/csv/h-new-111.json")
OUTPUT_JSON = os.path.join(PROJECT, "findings/phase-b-hypotheses/csv/h-new-920.json")
SEED = 20260507
N_PERM = 10000
N_SURAHS = 114

with open(PREREG_PATH, "rb") as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(
        f"FAIL-FAST: pre-reg SHA mismatch.\n"
        f"  expected: {EXPECTED_SHA}\n"
        f"  actual  : {actual_sha}\n"
        f"  path    : {PREREG_PATH}\n"
        f"Pre-reg has been edited since SHA-locking. Re-lock or restore."
    )
print(f"[OK] Pre-reg SHA verified: {actual_sha}")

# -----------------------------------------------------------------------------
# 1. Load H-NEW-111 FR matrix
# -----------------------------------------------------------------------------
with open(H111_PATH, "r") as f:
    h111 = json.load(f)

# Build dense 114x114 matrix (1-indexed surahs -> 0-indexed numpy-free list)
D = [[0.0] * (N_SURAHS + 1) for _ in range(N_SURAHS + 1)]  # 1..114 indices
for entry in h111["D_matrix_upper_triangular"]:
    a, b, dist = entry
    D[a][b] = dist
    D[b][a] = dist
print(f"[OK] Loaded H-NEW-111 FR matrix: {len(h111['D_matrix_upper_triangular'])} pairs.")
print(f"     rules_tuple: {h111['rules_tuple']}")
print(f"     locked_params: {h111['locked_params']}")

def fr(a, b):
    return D[a][b]

# -----------------------------------------------------------------------------
# 2. Curvature computation on a path
# -----------------------------------------------------------------------------
def compute_curvature(path):
    """
    path: list of length 114 with surah-IDs 1..114 (some permutation).
    Returns:
        turn_costs: list of length 112, indexed by interior path-position i ∈ {2..113}
                    (so turn_costs[0] corresponds to i=2, ..., turn_costs[111] to i=113)
        turning_angles: list of length 112 (same indexing) in radians
    """
    turn_costs = []
    turning_angles = []
    for i in range(1, len(path) - 1):  # i in 0-indexed: 1..112 → maps to path-pos 2..113
        s_prev = path[i - 1]
        s_curr = path[i]
        s_next = path[i + 1]
        d_in = fr(s_prev, s_curr)
        d_out = fr(s_curr, s_next)
        d_skip = fr(s_prev, s_next)
        tc = d_in + d_out - d_skip
        turn_costs.append(tc)
        # turning_angle (Euclidean-pseudo)
        denom = 2.0 * d_in * d_out
        if denom == 0:
            turning_angles.append(float("nan"))
        else:
            cos_theta = (d_in * d_in + d_out * d_out - d_skip * d_skip) / denom
            cos_theta = max(-1.0, min(1.0, cos_theta))
            turning_angles.append(math.acos(cos_theta))
    return turn_costs, turning_angles

# -----------------------------------------------------------------------------
# 3. Empirical mushaf curvature spectrum
# -----------------------------------------------------------------------------
mushaf_path = list(range(1, N_SURAHS + 1))  # [1, 2, ..., 114]
emp_tc, emp_ta = compute_curvature(mushaf_path)
assert len(emp_tc) == 112

# top-10 by turn_cost (path-positions 2..113 = path-index i+1 for tc list i=0..111)
emp_pairs = [(i + 2, tc) for i, tc in enumerate(emp_tc)]  # (path-position, turn_cost)
emp_pairs_sorted = sorted(emp_pairs, key=lambda x: -x[1])
top10 = emp_pairs_sorted[:10]
top10_positions = [p for p, _ in top10]

print("\n[EMPIRICAL] top-10 curvature positions (path-position, turn_cost, surah-triple):")
for rank, (pos, tc) in enumerate(top10, 1):
    s_prev = mushaf_path[pos - 2]
    s_curr = mushaf_path[pos - 1]
    s_next = mushaf_path[pos]
    print(
        f"  rank {rank:2d}: position {pos:3d}  Q{s_prev:3d}→Q{s_curr:3d}→Q{s_next:3d}  "
        f"turn_cost={tc:.6f}"
    )

emp_mean_tc = sum(emp_tc) / len(emp_tc)
print(f"\n[EMPIRICAL] mean turn_cost = {emp_mean_tc:.6f}")
print(f"[EMPIRICAL] median turn_cost = {sorted(emp_tc)[len(emp_tc)//2]:.6f}")

# -----------------------------------------------------------------------------
# 4. Boundary windows (PRE-COMMITTED in pre-reg §2.1)
# -----------------------------------------------------------------------------
B1 = set([48, 49, 50, 51, 52])  # Mufaṣṣal-onset Q 50 ±2
B2 = set([38, 39, 40, 41, 42])  # Ḥawāmīm cluster Q 39→40 ±2
B3 = set([2, 3, 4])             # Medinan-block-onset Q 2 (clipped at lower bound)
B_union = B1 | B2 | B3

def hits_in(positions, window):
    return sum(1 for p in positions if p in window)

emp_b1 = hits_in(top10_positions, B1)
emp_b2 = hits_in(top10_positions, B2)
emp_b3 = hits_in(top10_positions, B3)
emp_joint = hits_in(top10_positions, B_union)

print(f"\n[EMPIRICAL] B1 (Mufaṣṣal-onset {sorted(B1)}) hits in top-10: {emp_b1}")
print(f"[EMPIRICAL] B2 (Ḥawāmīm boundary {sorted(B2)}) hits in top-10: {emp_b2}")
print(f"[EMPIRICAL] B3 (Medinan onset {sorted(B3)}) hits in top-10: {emp_b3}")
print(f"[EMPIRICAL] JOINT B1∪B2∪B3 ({len(B_union)} positions) hits in top-10: {emp_joint}")

# -----------------------------------------------------------------------------
# 5. Permutation null (10000 perms)
# -----------------------------------------------------------------------------
print(f"\n[NULL] Running {N_PERM} permutations (seed {SEED})...")

# Stats accumulators
perm_means = []
# count how often the perm spectrum hits each window at-or-above the empirical
b1_perm_hits_dist = Counter()
b2_perm_hits_dist = Counter()
b3_perm_hits_dist = Counter()
joint_perm_hits_dist = Counter()
perm_hits_per_position_top10 = Counter()  # which path-positions get into top-10 across perms

# For directional p-values
ge_emp_b1 = 0
ge_emp_b2 = 0
ge_emp_b3 = 0
ge_emp_joint = 0
le_emp_mean = 0   # for H1b: P(perm_mean ≤ emp_mean) — directional lower-tail
ge_emp_mean = 0   # for reverse-direction monitoring

rng = random.Random(SEED)

for r in range(N_PERM):
    perm = list(range(1, N_SURAHS + 1))
    rng.shuffle(perm)
    p_tc, _ = compute_curvature(perm)
    # mean
    p_mean = sum(p_tc) / len(p_tc)
    perm_means.append(p_mean)
    if p_mean <= emp_mean_tc:
        le_emp_mean += 1
    if p_mean >= emp_mean_tc:
        ge_emp_mean += 1
    # top-10 path-positions
    p_pairs = [(i + 2, tc) for i, tc in enumerate(p_tc)]
    p_pairs.sort(key=lambda x: -x[1])
    p_top10 = [p for p, _ in p_pairs[:10]]
    # boundary hits
    h1 = hits_in(p_top10, B1)
    h2 = hits_in(p_top10, B2)
    h3 = hits_in(p_top10, B3)
    hj = hits_in(p_top10, B_union)
    b1_perm_hits_dist[h1] += 1
    b2_perm_hits_dist[h2] += 1
    b3_perm_hits_dist[h3] += 1
    joint_perm_hits_dist[hj] += 1
    if h1 >= emp_b1:
        ge_emp_b1 += 1
    if h2 >= emp_b2:
        ge_emp_b2 += 1
    if h3 >= emp_b3:
        ge_emp_b3 += 1
    if hj >= emp_joint:
        ge_emp_joint += 1
    for p in p_top10:
        perm_hits_per_position_top10[p] += 1

p_b1 = ge_emp_b1 / N_PERM
p_b2 = ge_emp_b2 / N_PERM
p_b3 = ge_emp_b3 / N_PERM
p_joint = ge_emp_joint / N_PERM
p_mean_lower = le_emp_mean / N_PERM
p_mean_upper = ge_emp_mean / N_PERM

# Perm-null mean stats
perm_means_sorted = sorted(perm_means)
def percentile(s, q):
    k = int(round(q / 100.0 * (len(s) - 1)))
    return s[max(0, min(len(s) - 1, k))]
null_mean = sum(perm_means) / len(perm_means)
null_std = math.sqrt(sum((m - null_mean) ** 2 for m in perm_means) / len(perm_means))
null_p05 = percentile(perm_means_sorted, 5)
null_p50 = percentile(perm_means_sorted, 50)
null_p95 = percentile(perm_means_sorted, 95)

print(f"[NULL] mean turn_cost  emp={emp_mean_tc:.6f}  null_mean={null_mean:.6f}  std={null_std:.6f}")
print(f"[NULL] null pcts: 5%={null_p05:.6f} 50%={null_p50:.6f} 95%={null_p95:.6f}")
print(f"[NULL] H1b lower-tail p (perm mean ≤ emp mean) = {p_mean_lower:.5f}")
print(f"[NULL] H1b upper-tail p (perm mean ≥ emp mean) = {p_mean_upper:.5f}")
z_emp = (emp_mean_tc - null_mean) / null_std if null_std > 0 else float("nan")
print(f"[NULL] empirical mean z-score vs perm null = {z_emp:+.3f}")

print(f"\n[NULL] H1a perm-p values:")
print(f"       B1 (≥{emp_b1}): p = {p_b1:.5f}   threshold α_bon = 0.01667")
print(f"       B2 (≥{emp_b2}): p = {p_b2:.5f}   threshold α_bon = 0.01667")
print(f"       B3 (≥{emp_b3}): p = {p_b3:.5f}   threshold α_bon = 0.01667")
print(f"       JOINT (≥{emp_joint}): p = {p_joint:.5f}  threshold α = 0.05")

# -----------------------------------------------------------------------------
# 6. Verdicts
# -----------------------------------------------------------------------------
ALPHA_BON = 0.05 / 3.0

def cell_verdict(hits, threshold, p):
    if hits >= threshold and p <= ALPHA_BON:
        return "PASS"
    elif hits >= threshold and p <= 0.05:
        return "DIRECTIONAL"
    elif hits >= threshold:
        return "DIRECTION-MET-NOT-SIG"
    else:
        return "NULL"

v_b1 = cell_verdict(emp_b1, 2, p_b1)
v_b2 = cell_verdict(emp_b2, 2, p_b2)
v_b3 = cell_verdict(emp_b3, 1, p_b3)

joint_pass = (emp_joint >= 4) and (p_joint <= 0.05)
n_pass = sum(1 for v in [v_b1, v_b2, v_b3] if v == "PASS")
if n_pass >= 2:
    h1a_overall = "PASS-DIRECTED"
elif n_pass == 1:
    h1a_overall = "DIRECTIONAL"
else:
    h1a_overall = "NULL"

# H1b
if p_mean_upper <= 0.05:
    h1b_verdict = "REVERSE-PRE-COMMIT-VIOLATION"
elif p_mean_lower <= 0.05:
    h1b_verdict = "PASS"
else:
    h1b_verdict = "NULL-NEUTRAL"

# Overall
if h1a_overall == "PASS-DIRECTED" and h1b_verdict == "PASS":
    overall = "PASS-DIRECTED (both H1a + H1b)"
elif h1a_overall == "PASS-DIRECTED":
    overall = "PASS-DIRECTED (H1a only)"
elif h1b_verdict == "PASS":
    overall = "PASS-DIRECTED (H1b only)"
elif h1a_overall == "DIRECTIONAL" or h1b_verdict in ("PASS",):
    overall = "DIRECTIONAL"
elif h1b_verdict == "REVERSE-PRE-COMMIT-VIOLATION":
    overall = "PRE-COMMIT VIOLATION on H1b"
else:
    overall = "NULL"

print(f"\n[VERDICTS]")
print(f"  H1a.B1: hits={emp_b1}  p={p_b1:.5f}  verdict={v_b1}")
print(f"  H1a.B2: hits={emp_b2}  p={p_b2:.5f}  verdict={v_b2}")
print(f"  H1a.B3: hits={emp_b3}  p={p_b3:.5f}  verdict={v_b3}")
print(f"  H1a JOINT: hits={emp_joint}  p={p_joint:.5f}  pass≥4: {joint_pass}")
print(f"  H1a overall: {h1a_overall}")
print(f"  H1b: emp_mean={emp_mean_tc:.6f}  null_mean={null_mean:.6f}  z={z_emp:+.3f}  verdict={h1b_verdict}")
print(f"  OVERALL: {overall}")

# -----------------------------------------------------------------------------
# 7. Write JSON
# -----------------------------------------------------------------------------
top10_records = []
for rank, (pos, tc) in enumerate(top10, 1):
    s_prev = mushaf_path[pos - 2]
    s_curr = mushaf_path[pos - 1]
    s_next = mushaf_path[pos]
    top10_records.append({
        "rank": rank,
        "path_position": pos,
        "surah_prev": s_prev,
        "surah_curr": s_curr,
        "surah_next": s_next,
        "turn_cost": tc,
        "turning_angle_rad": emp_ta[pos - 2],
        "turning_angle_deg": emp_ta[pos - 2] * 180.0 / math.pi,
        "in_B1_mufassal": pos in B1,
        "in_B2_hawamim": pos in B2,
        "in_B3_medinan": pos in B3,
        "in_B_union": pos in B_union,
    })

# All 112 turn-costs with positions
all_curvature = [
    {
        "path_position": i + 2,
        "surah_prev": mushaf_path[i],
        "surah_curr": mushaf_path[i + 1],
        "surah_next": mushaf_path[i + 2],
        "turn_cost": emp_tc[i],
        "turning_angle_rad": emp_ta[i],
        "turning_angle_deg": emp_ta[i] * 180.0 / math.pi,
    }
    for i in range(112)
]

# Top-30 most-frequent perm-top10 path-positions (for diagnostic)
perm_top_positions = perm_hits_per_position_top10.most_common(30)

out = {
    "finding_id": "h-new-920",
    "title": "Discrete geodesic curvature of the mushaf path",
    "pre_reg_sha256": EXPECTED_SHA,
    "seed": SEED,
    "n_perm": N_PERM,
    "date": "2026-05-07",
    "rules_tuple_inherited_from_h111": h111["rules_tuple"],
    "locked_params_inherited_from_h111": h111["locked_params"],
    "primary_metric": "turn_cost = d_in + d_out - d_skip (FR triangle slack)",
    "secondary_metric": "turning_angle (Euclidean-pseudo, diagnostic only)",
    "boundaries_pre_committed": {
        "B1_mufassal_onset_Q50": sorted(B1),
        "B2_hawamim_cluster_Q40": sorted(B2),
        "B3_medinan_block_onset_Q2": sorted(B3),
        "B_union": sorted(B_union),
    },
    "empirical": {
        "mean_turn_cost": emp_mean_tc,
        "median_turn_cost": sorted(emp_tc)[len(emp_tc) // 2],
        "min_turn_cost": min(emp_tc),
        "max_turn_cost": max(emp_tc),
        "top10": top10_records,
        "all_112_curvature": all_curvature,
        "boundary_hits": {
            "B1_hits": emp_b1,
            "B2_hits": emp_b2,
            "B3_hits": emp_b3,
            "JOINT_hits": emp_joint,
        },
    },
    "perm_null": {
        "n_perm": N_PERM,
        "mean_turn_cost_null_mean": null_mean,
        "mean_turn_cost_null_std": null_std,
        "mean_turn_cost_null_p05": null_p05,
        "mean_turn_cost_null_p50": null_p50,
        "mean_turn_cost_null_p95": null_p95,
        "empirical_mean_z": z_emp,
        "p_mean_lower_tail": p_mean_lower,
        "p_mean_upper_tail": p_mean_upper,
        "p_b1": p_b1,
        "p_b2": p_b2,
        "p_b3": p_b3,
        "p_joint": p_joint,
        "b1_hits_distribution": dict(b1_perm_hits_dist),
        "b2_hits_distribution": dict(b2_perm_hits_dist),
        "b3_hits_distribution": dict(b3_perm_hits_dist),
        "joint_hits_distribution": dict(joint_perm_hits_dist),
        "top30_most_frequent_top10_positions_in_perm_null": [
            {"position": p, "freq": c} for p, c in perm_top_positions
        ],
    },
    "verdicts": {
        "alpha_bonferroni_3": ALPHA_BON,
        "H1a_B1": v_b1,
        "H1a_B2": v_b2,
        "H1a_B3": v_b3,
        "H1a_overall": h1a_overall,
        "H1a_joint_pass_geq4_in_union_alpha_05": joint_pass,
        "H1b": h1b_verdict,
        "overall": overall,
    },
    "anchors": {
        "h_new_111": "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json",
        "cross_finding_011": "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/cross-finding-011-mushaf-fisher-rao-confirmed.md",
        "h_new_130": "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-130-fisher-rao-residuals.md",
        "h_new_236_1": "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-236-1-hinges-constrained-simulator.md",
        "cross_finding_020": "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md",
    },
}

with open(OUTPUT_JSON, "w") as f:
    json.dump(out, f, indent=2)
print(f"\n[OK] Wrote: {OUTPUT_JSON}")
print(f"[DONE] H-NEW-920 complete. Overall verdict: {overall}")
