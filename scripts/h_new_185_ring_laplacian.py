#!/usr/bin/env python3
"""H-NEW-185 — Spectral graph Laplacian analysis of mushaf ring.

Pre-registered tests (Bonferroni k=2, alpha_bon=0.025):
  H1a — Fiedler sign-flip aligns with Q 50 pivot (within +/- 5 ring positions)
  H1b — Spectral gap Delta = lambda_2 - lambda_1 > null (upper-tail, random re-wiring)

Seed 20260419. Parent: H-NEW-111 D matrix from csv/h-new-111.json.
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PERMS = 10000
EPS = 1e-6
AXIS_TOL = 5  # +/- 5 ring positions

PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-185-ring-laplacian-prereg.md'
H111_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-185.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"SEED={SEED} PERMS={PERMS} EPS={EPS} AXIS_TOL={AXIS_TOL}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Load D matrix from H-NEW-111
# ---------------------------------------------------------------------------
h111 = json.loads(H111_JSON.read_text())
D = np.zeros((114, 114), dtype=np.float64)
for entry in h111['D_matrix_upper_triangular']:
    i, j, d = entry
    # i, j are 1-indexed in the JSON; convert to 0-indexed
    ii, jj = i - 1, j - 1
    D[ii, jj] = d
    D[jj, ii] = d

print(f"D matrix: shape={D.shape}, range=[{D.min():.4f}, {D.max():.4f}]", file=sys.stderr)

# ---------------------------------------------------------------------------
# 2. Extract the 114 ring edges (consecutive + wrap-around)
# ---------------------------------------------------------------------------
# In the ring, node at position p (0-indexed) is surah p+1. The mushaf
# order is the identity mapping on the ring: position p <-> surah p+1.
# Ring edges: (0,1), (1,2), ..., (112, 113), (113, 0).
ring_edges = [(p, (p + 1) % 114) for p in range(114)]
assert len(ring_edges) == 114

edge_weights_mushaf = np.array([D[i, j] for i, j in ring_edges])
print(f"Ring edge weights (mushaf): mean={edge_weights_mushaf.mean():.4f}, "
      f"range=[{edge_weights_mushaf.min():.4f}, {edge_weights_mushaf.max():.4f}]",
      file=sys.stderr)

# ---------------------------------------------------------------------------
# 3. Build normalized Laplacian given a ring-position-to-surah assignment
# ---------------------------------------------------------------------------
def build_ring_laplacian(assignment):
    """assignment: length-114 array; assignment[p] = surah_id (0-indexed)
    at ring position p. Returns L_sym (114x114 np array).
    """
    A = np.zeros((114, 114), dtype=np.float64)
    for p in range(114):
        s_here = assignment[p]
        s_next = assignment[(p + 1) % 114]
        w = D[s_here, s_next]
        aff = 1.0 / (w + EPS)
        A[s_here, s_next] += aff
        A[s_next, s_here] += aff
    deg = A.sum(axis=1)
    # avoid div-by-zero (all nodes have degree > 0 because ring is connected)
    d_inv_sqrt = 1.0 / np.sqrt(deg)
    D_inv_sqrt = np.diag(d_inv_sqrt)
    L_unnorm = np.diag(deg) - A
    L_sym = D_inv_sqrt @ L_unnorm @ D_inv_sqrt
    # Symmetrize to fight float roundoff
    L_sym = 0.5 * (L_sym + L_sym.T)
    return L_sym, A, deg


def spectrum(L):
    eigvals, eigvecs = eigh(L)
    # sort ascending (eigh returns ascending, but make sure)
    idx = np.argsort(eigvals)
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]
    return eigvals, eigvecs


# ---------------------------------------------------------------------------
# 4. Mushaf ring spectrum
# ---------------------------------------------------------------------------
mushaf_assign = np.arange(114, dtype=np.int64)  # identity: position p -> surah p
L_mu, A_mu, deg_mu = build_ring_laplacian(mushaf_assign)
eigvals_mu, eigvecs_mu = spectrum(L_mu)
print(f"\nMushaf spectrum: lambda_0={eigvals_mu[0]:.6e} (should ~= 0)",
      file=sys.stderr)
print(f"  lambda_1={eigvals_mu[1]:.6f}, lambda_2={eigvals_mu[2]:.6f}, "
      f"lambda_3={eigvals_mu[3]:.6f}", file=sys.stderr)

# Sanity: lambda_0 should be numerically 0
assert abs(eigvals_mu[0]) < 1e-9, f"lambda_0 = {eigvals_mu[0]} not near 0"

spectral_gap_mu = eigvals_mu[2] - eigvals_mu[1]
print(f"  Delta = lambda_2 - lambda_1 = {spectral_gap_mu:.6f}", file=sys.stderr)

fiedler = eigvecs_mu[:, 1]
# Fiedler sign along ring positions (position p -> surah p -> fiedler[p])
fiedler_by_position = fiedler[mushaf_assign]

# ---------------------------------------------------------------------------
# 5. Find Fiedler sign-flip positions along the ring
# ---------------------------------------------------------------------------
def find_sign_flips(vec):
    """Return list of ring-position indices p where sign(vec[p]) != sign(vec[(p+1) mod N])."""
    N = len(vec)
    signs = np.sign(vec)
    # Replace exact-zero with +1 (extremely rare for float eigenvectors)
    signs = np.where(signs == 0, 1.0, signs)
    flips = []
    for p in range(N):
        if signs[p] != signs[(p + 1) % N]:
            flips.append(p)  # flip occurs between position p and p+1
    return flips


flips = find_sign_flips(fiedler_by_position)
print(f"  Fiedler sign-flip positions (ring 0-indexed): {flips}", file=sys.stderr)
print(f"  #flips = {len(flips)}", file=sys.stderr)

# Translate to surah boundaries (ring position p -> between surah p+1 and p+2)
flip_surah_boundaries = [(p + 1, ((p + 1) % 114) + 1) for p in flips]
print(f"  Flip boundaries (surah_i -> surah_{{i+1}}): {flip_surah_boundaries}",
      file=sys.stderr)

# Axis A: distance from Q 50 (mushaf-position 49 in 0-indexed, or position 49
# is the edge between surah 50 and surah 51; flip at position 49 means between
# surah 50 and 51, which is AT Q 50).
# Distance from Q 50: minimum |p - 49| over all flips (taking care of ring wraparound
# with the distance to a POSITION-49-anchored window).
def dist_to_position_ring(p, anchor, N=114):
    d = abs(p - anchor)
    return min(d, N - d)


if flips:
    dists_to_50 = [dist_to_position_ring(p, 49) for p in flips]
    obs_axis_distance = min(dists_to_50)
else:
    obs_axis_distance = 114  # no sign flips = entire Fiedler one sign (impossible for lambda_1>0 but guard)

print(f"\nH1a observed: min distance from Q 50 to Fiedler flip = {obs_axis_distance}",
      file=sys.stderr)
pass_h1a_raw = obs_axis_distance <= AXIS_TOL
print(f"  within +/-{AXIS_TOL}? {'YES' if pass_h1a_raw else 'NO'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. Null: random re-wiring of edge weights to ring positions
# ---------------------------------------------------------------------------
# Per pre-reg: random permutation of the surah-ID-to-ring-position assignment.
# This preserves the MULTISET of pairwise-distance edges that the ring uses
# (actually it preserves the set of nodes; the edge-weight multiset CHANGES
# because different neighborings are created). Let me re-read pre-reg...
#
# Pre-reg says: "randomly permuting the 114 surah-ID-to-ring-position
# assignment (i.e., re-wiring the consecutive edges while preserving the
# unweighted ring structure)."
#
# This is the standard mushaf-order null: random surah permutations forming
# a Hamiltonian cycle. Edge weights are induced by D given the new cycle.

rng = np.random.default_rng(SEED)
null_gap = np.zeros(PERMS, dtype=np.float64)
null_axis_dist = np.zeros(PERMS, dtype=np.int32)
null_lambda1 = np.zeros(PERMS, dtype=np.float64)
null_lambda2 = np.zeros(PERMS, dtype=np.float64)

print(f"\nRunning {PERMS} random-rewiring perms...", file=sys.stderr)
for t in range(PERMS):
    perm_assign = rng.permutation(114).astype(np.int64)
    L_p, _, _ = build_ring_laplacian(perm_assign)
    ev_p, evc_p = spectrum(L_p)
    null_lambda1[t] = ev_p[1]
    null_lambda2[t] = ev_p[2]
    null_gap[t] = ev_p[2] - ev_p[1]

    # For null axis distance: find the Fiedler sign-flips IN RING-POSITION
    # space (not surah space). Fiedler[p] = eigenvector entry for the NODE
    # at ring position p = the surah perm_assign[p]. So Fiedler-by-position:
    # evc_p[:,1][perm_assign]
    fie_p = evc_p[:, 1][perm_assign]
    fp = find_sign_flips(fie_p)
    if fp:
        null_axis_dist[t] = min(dist_to_position_ring(p, 49) for p in fp)
    else:
        null_axis_dist[t] = 114
    if (t + 1) % 2000 == 0:
        print(f"  perm {t+1}/{PERMS}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. P-values
# ---------------------------------------------------------------------------
# H1a: p = fraction of perms with axis_dist <= observed  (lower tail; smaller = more aligned)
n_le_obs_axis = int((null_axis_dist <= obs_axis_distance).sum())
p_h1a = (n_le_obs_axis + 1) / (PERMS + 1)

# H1b: p = fraction of perms with gap >= observed (upper tail)
n_ge_obs_gap = int((null_gap >= spectral_gap_mu).sum())
p_h1b = (n_ge_obs_gap + 1) / (PERMS + 1)

print(f"\n=== RESULTS ===", file=sys.stderr)
print(f"H1a Fiedler-Q50 alignment:", file=sys.stderr)
print(f"  obs axis_dist = {obs_axis_distance}", file=sys.stderr)
print(f"  null mean axis_dist = {null_axis_dist.mean():.2f}, "
      f"median = {np.median(null_axis_dist):.1f}", file=sys.stderr)
print(f"  #{{null <= obs}} = {n_le_obs_axis} / {PERMS}", file=sys.stderr)
print(f"  p_H1a = {p_h1a:.6f}   (alpha_bon=0.025, "
      f"verdict: {'PASS' if p_h1a < 0.025 else 'NULL'})", file=sys.stderr)

print(f"\nH1b Spectral gap:", file=sys.stderr)
print(f"  obs Delta = {spectral_gap_mu:.6f}", file=sys.stderr)
print(f"  null Delta: mean={null_gap.mean():.6f}, sd={null_gap.std():.6f}, "
      f"min={null_gap.min():.6f}, max={null_gap.max():.6f}", file=sys.stderr)
print(f"  #{{null >= obs}} = {n_ge_obs_gap} / {PERMS}", file=sys.stderr)
print(f"  p_H1b = {p_h1b:.6f}   (alpha_bon=0.025, "
      f"verdict: {'PASS' if p_h1b < 0.025 else 'NULL'})", file=sys.stderr)

# z-score
z_gap = (spectral_gap_mu - null_gap.mean()) / (null_gap.std() + 1e-12)
print(f"  z(gap) = {z_gap:.3f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. Descriptive: eigenvector centrality for lambda_2
# ---------------------------------------------------------------------------
v2 = eigvecs_mu[:, 2]
abs_v2 = np.abs(v2)
top10_v2_idx = np.argsort(-abs_v2)[:10]
top10_v2 = [(int(idx + 1), float(v2[idx]), float(abs_v2[idx])) for idx in top10_v2_idx]
print(f"\nTop-10 surahs by |v_2| (lambda_2 eigenvector centrality):", file=sys.stderr)
for s, val, absval in top10_v2:
    print(f"  Q{s:3d}  v2={val:+.4f}", file=sys.stderr)

abs_v1 = np.abs(fiedler)
top10_v1_idx = np.argsort(-abs_v1)[:10]
top10_v1 = [(int(idx + 1), float(fiedler[idx]), float(abs_v1[idx])) for idx in top10_v1_idx]
print(f"\nTop-10 surahs by |Fiedler v_1| (community hubs):", file=sys.stderr)
for s, val, absval in top10_v1:
    print(f"  Q{s:3d}  v1={val:+.4f}", file=sys.stderr)

# Report the two Fiedler communities
pos_community = sorted(int(i + 1) for i in range(114) if fiedler[i] > 0)
neg_community = sorted(int(i + 1) for i in range(114) if fiedler[i] <= 0)
print(f"\nFiedler sign partition:", file=sys.stderr)
print(f"  (+) community: {len(pos_community)} surahs; first/last: "
      f"Q{pos_community[0]}..Q{pos_community[-1]}", file=sys.stderr)
print(f"  (-) community: {len(neg_community)} surahs; first/last: "
      f"Q{neg_community[0]}..Q{neg_community[-1]}", file=sys.stderr)

# Identify the arcs along the ring (contiguous runs by position)
fiedler_signs = np.sign(fiedler_by_position)
fiedler_signs = np.where(fiedler_signs == 0, 1.0, fiedler_signs)
# Find runs
arcs = []
start_pos = 0
cur_sign = fiedler_signs[0]
for p in range(1, 114):
    if fiedler_signs[p] != cur_sign:
        arcs.append((cur_sign, start_pos, p - 1))
        start_pos = p
        cur_sign = fiedler_signs[p]
arcs.append((cur_sign, start_pos, 113))
# Check wrap-around merging
if len(arcs) > 1 and arcs[0][0] == arcs[-1][0]:
    # Merge last arc into first (wrap-around)
    last_sign, last_start, last_end = arcs[-1]
    first_sign, first_start, first_end = arcs[0]
    arcs = arcs[1:-1] + [(first_sign, last_start, first_end)]

arcs_info = []
for sign, s, e in arcs:
    if s <= e:
        length = e - s + 1
        span = f"Q{s+1}..Q{e+1}"
    else:
        length = (113 - s + 1) + (e + 1)
        span = f"Q{s+1}..Q114..Q1..Q{e+1}"
    arcs_info.append({'sign': int(sign), 'start_pos': int(s), 'end_pos': int(e),
                      'length': int(length), 'span': span})
    print(f"  arc sign={int(sign):+d}  positions {s}..{e} ({span}) len={length}",
          file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. Verdict
# ---------------------------------------------------------------------------
pass_h1a = p_h1a < 0.025
pass_h1b = p_h1b < 0.025
if pass_h1a and pass_h1b:
    verdict = 'PASS-DIRECTED'
elif pass_h1a and not pass_h1b:
    verdict = 'WEAK-PASS (Fiedler-axis only)'
elif (not pass_h1a) and pass_h1b:
    verdict = 'WEAK-PASS (gap only)'
else:
    verdict = 'NULL'

print(f"\n\n===== FINAL VERDICT: {verdict} =====", file=sys.stderr)

# ---------------------------------------------------------------------------
# 10. Output
# ---------------------------------------------------------------------------
summary = {
    'finding_id': 'h-new-185',
    'title': 'Spectral graph Laplacian analysis of mushaf ring',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'perms': PERMS,
    'rules_tuple': '(no-tashkeel, QAC-STEM root tokens K=500, QAC v0.4, Dirichlet-0.5, L1-norm, mushaf ring topology, Hafs-Kufan, Fisher-Rao angular distance)',
    'locked_params': {
        'affinity': '1/(w+eps), eps=1e-6',
        'laplacian': 'normalized symmetric L_sym = D^-1/2 (D_diag - A) D^-1/2',
        'null_model': 'random permutation of surah-to-ring-position assignment',
        'axis': 'Q50 mid-mushaf pivot',
        'axis_tolerance_positions': AXIS_TOL,
        'bonferroni_k': 2,
        'alpha_bon': 0.025,
    },
    'mushaf_spectrum': {
        'lambda_0': float(eigvals_mu[0]),
        'lambda_1': float(eigvals_mu[1]),
        'lambda_2': float(eigvals_mu[2]),
        'lambda_3': float(eigvals_mu[3]),
        'lambda_top10': [float(x) for x in eigvals_mu[:10]],
        'lambda_max': float(eigvals_mu[-1]),
        'spectral_gap': float(spectral_gap_mu),
    },
    'fiedler': {
        'sign_flip_positions': flips,
        'sign_flip_surah_boundaries': [list(b) for b in flip_surah_boundaries],
        'n_flips': len(flips),
        'pos_community_size': len(pos_community),
        'neg_community_size': len(neg_community),
        'arcs': arcs_info,
        'min_distance_to_Q50': int(obs_axis_distance),
        'top10_abs_v1': [{'surah': s, 'v1': val, 'abs_v1': absval}
                         for (s, val, absval) in top10_v1],
    },
    'lambda2_centrality': {
        'top10_abs_v2': [{'surah': s, 'v2': val, 'abs_v2': absval}
                         for (s, val, absval) in top10_v2],
    },
    'primary_H1a_fiedler_Q50_alignment': {
        'observed_axis_distance': int(obs_axis_distance),
        'null_mean_axis_distance': float(null_axis_dist.mean()),
        'null_median_axis_distance': float(np.median(null_axis_dist)),
        'n_null_le_obs': n_le_obs_axis,
        'p_value_one_sided_lower': float(p_h1a),
        'alpha_bon': 0.025,
        'pass_H1a': bool(pass_h1a),
    },
    'primary_H1b_spectral_gap': {
        'observed_gap': float(spectral_gap_mu),
        'null_gap_mean': float(null_gap.mean()),
        'null_gap_sd': float(null_gap.std()),
        'null_gap_min': float(null_gap.min()),
        'null_gap_max': float(null_gap.max()),
        'null_gap_q025': float(np.quantile(null_gap, 0.025)),
        'null_gap_q05': float(np.quantile(null_gap, 0.05)),
        'null_gap_q50': float(np.quantile(null_gap, 0.50)),
        'null_gap_q95': float(np.quantile(null_gap, 0.95)),
        'null_gap_q975': float(np.quantile(null_gap, 0.975)),
        'z_score': float(z_gap),
        'n_null_ge_obs': n_ge_obs_gap,
        'p_value_one_sided_upper': float(p_h1b),
        'alpha_bon': 0.025,
        'pass_H1b': bool(pass_h1b),
    },
    'verdict': verdict,
    'verdict_ceiling': 'PASS-DIRECTED (CONFIRMED requires char-4-gram feature-space replication)',
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote {OUT_JSON}", file=sys.stderr)
