#!/usr/bin/env python3
"""cross-finding-012 — Late-Meccan Scripture-Announcement Apparatus: joint-peak test.

Pre-reg: findings/phase-b-hypotheses/cross-finding-012-late-meccan-scripture-announcement-prereg.md

Tests whether 5 Pattern-B axes (H-NEW-125 INVERTED-U-peak-Late-Meccan) jointly peak at
the SAME Nöldeke-sub-bin, using:
  - Cell A: Kendall's W concordance over 5 axes' sub-bin rankings (primary, inferential)
  - Cell B: modal peak-bin ∈ {B5,B6,B7} AND ≥4/5 axes peak in {B5,B6,B7} (secondary)
  - Cell C: descriptive peak-bin coordinate disclosure

Axes (verbatim from H-NEW-125 per_surah_axis_values):
  1. qul_density
  2. book_reference_density
  3. eschatological_density
  4. muq_cardinality
  5. loanword_density

Sub-binning: equal-count octile over Nöldeke rank 1..114 (~14 surahs/bin).
Null: 10K Nöldeke-rank-shuffle perms. Seed 20260417.
Bonferroni k=3, α_bon = 0.0167.

MW-5 positive control: 5 Pattern-A monotone-up axes (allah, legal, pronoun, verse-length,
divine-name) should joint-peak at B8 (Medinan core, Nöldeke ranks 101-114).
"""
from __future__ import annotations

import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERM = 10_000
BON_K = 3
ALPHA_BON = 0.05 / BON_K  # 0.01666...
N_BINS = 8  # octile

UPSTREAM_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-125.json'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/cross-finding-012.json'

PATTERN_B_AXES = [
    'qul_density',
    'book_reference_density',
    'eschatological_density',
    'muq_cardinality',
    'loanword_density',
]

# Audit-036 mandated 4-axis sensitivity check: drop muq_cardinality because
# it is Pattern-B BY DEFINITION per scratch connection note, not independent
# evidence. See pre-reg §Inflated-independence-disclosure.
PATTERN_B_AXES_NOMUQ = [a for a in PATTERN_B_AXES if a != 'muq_cardinality']

PATTERN_A_POSCTRL_AXES = [
    'allah_density',
    'legal_term_density',
    'personal_pronoun_density',
    'mean_verse_length',
    'divine_name_density',
]

# ------------------------------------------------------------
# Load H-NEW-125 per-surah axis values (NO re-extraction)
# ------------------------------------------------------------
with open(UPSTREAM_JSON, encoding='utf-8') as f:
    h125 = json.load(f)

psv = h125['per_surah_axis_values']  # dict: str(sid) -> {name, noldeke_rank, noldeke_phase, axis_values}
assert len(psv) == 114, f"expected 114 surahs, got {len(psv)}"

# Build arrays indexed by surah id 1..114
sids = sorted(int(k) for k in psv.keys())
n = len(sids)
assert sids == list(range(1, 115))

noldeke_rank = np.array([psv[str(sid)]['noldeke_rank'] for sid in sids], dtype=int)
noldeke_phase = [psv[str(sid)]['noldeke_phase'] for sid in sids]
names = [psv[str(sid)]['name'] for sid in sids]

def axis_vector(axis_name):
    return np.array([psv[str(sid)]['axis_values'][axis_name] for sid in sids], dtype=float)

axis_vectors = {a: axis_vector(a) for a in (PATTERN_B_AXES + PATTERN_A_POSCTRL_AXES)}

# ------------------------------------------------------------
# Octile sub-binning (LOCKED breakpoints)
# Nöldeke rank is 1..114; octile over this range.
# Using numpy.digitize on equal-width rank ranges (since ranks are uniformly distributed 1..114).
# ------------------------------------------------------------
# Rank-to-bin via equal-count split of the 114 ranks into 8 groups
# bin edges chosen via np.quantile of np.arange(1,115) at [1/8..7/8]
edges = np.quantile(np.arange(1, 115), np.linspace(1/N_BINS, (N_BINS-1)/N_BINS, N_BINS-1))
# edges: array of length 7 giving the upper bounds of bins 1..7 (bin 8 open-ended)
def rank_to_bin(r_arr):
    """Map rank array to bin index 0..7 (i.e., B1..B8 labels = 0-indexed +1)."""
    return np.digitize(r_arr, edges, right=False)  # 0 for ≤edges[0], 7 for > edges[6]

bin_of_surah = rank_to_bin(noldeke_rank)  # shape (114,)
bin_counts = np.bincount(bin_of_surah, minlength=N_BINS)

print(f"[CF-012] Sub-bin breakpoints (rank upper bounds B1..B7): {edges}", file=sys.stderr)
print(f"[CF-012] Surahs per bin (B1..B8): {bin_counts.tolist()}", file=sys.stderr)

# Nöldeke Late-Meccan core band: ranks 70..90 per h-new-125 pre-reg
# Under the octile scheme, this maps to which bins?
lm_bin_mask = (noldeke_rank >= 70) & (noldeke_rank <= 90)
lm_bin_indices = sorted(set(bin_of_surah[lm_bin_mask].tolist()))
print(f"[CF-012] Nöldeke Late-Meccan (rank 70-90) spans bins (0-indexed): {lm_bin_indices}", file=sys.stderr)

# ------------------------------------------------------------
# Core statistics
# ------------------------------------------------------------
def per_bin_means(values, bin_assignments):
    """Return shape (N_BINS,) of mean axis value per bin; NaN for empty bins."""
    means = np.full(N_BINS, np.nan)
    for b in range(N_BINS):
        mask = bin_assignments == b
        if mask.sum() > 0:
            means[b] = values[mask].mean()
    return means

def rank_bins_by_mean(means):
    """Rank 1..N_BINS (1 = highest mean). NaN bins get rank = N_BINS (lowest)."""
    # Higher mean = rank 1
    order = np.argsort(-np.nan_to_num(means, nan=-np.inf), kind='stable')
    ranks = np.empty(N_BINS, dtype=float)
    for r, b in enumerate(order):
        ranks[b] = r + 1
    return ranks

def kendalls_w(ranking_matrix):
    """Kendall's coefficient of concordance W.
    ranking_matrix: shape (m, n) = m rankings of n items; each row contains ranks 1..n.
    W = 12*S / (m^2 * (n^3 - n)), S = sum_j (Rj - mean_R)^2, Rj = column sum.
    """
    m, nk = ranking_matrix.shape
    Rj = ranking_matrix.sum(axis=0)
    mean_R = m * (nk + 1) / 2.0
    S = np.sum((Rj - mean_R) ** 2)
    return (12.0 * S) / (m * m * (nk ** 3 - nk))

def compute_stats(axis_names, bin_assignments):
    """Compute (W, per_axis_peak_bin, per_axis_means, per_axis_ranks) for given bin assignment."""
    m = len(axis_names)
    ranking_matrix = np.empty((m, N_BINS), dtype=float)
    per_axis_peak = np.empty(m, dtype=int)
    per_axis_means = np.empty((m, N_BINS), dtype=float)
    for i, a in enumerate(axis_names):
        means = per_bin_means(axis_vectors[a], bin_assignments)
        per_axis_means[i] = means
        ranking_matrix[i] = rank_bins_by_mean(means)
        # argmax over the means (ignore NaN)
        per_axis_peak[i] = int(np.nanargmax(means))
    W = kendalls_w(ranking_matrix)
    return W, per_axis_peak, per_axis_means, ranking_matrix

def cell_b_criterion(per_axis_peak, target_bins):
    """Cell B: modal peak ∈ target_bins AND ≥4/5 axes peak in target_bins."""
    cnt = Counter(per_axis_peak.tolist())
    mode_peak, mode_count = cnt.most_common(1)[0]
    n_in_target = sum(1 for b in per_axis_peak if b in target_bins)
    return (mode_peak in target_bins) and (n_in_target >= 4), mode_peak, n_in_target

# Target bins: {B5, B6, B7} = 0-indexed {4, 5, 6}
TARGET_BINS = {4, 5, 6}  # B5, B6, B7 (1-bin tolerance around Late-Meccan core B6)

# ------------------------------------------------------------
# Observed statistics (Pattern B, 5-axis)
# ------------------------------------------------------------
W_obs_B, peak_obs_B, means_obs_B, ranks_obs_B = compute_stats(PATTERN_B_AXES, bin_of_surah)
cell_b_obs_pass, mode_peak_obs_B, n_in_target_obs_B = cell_b_criterion(peak_obs_B, TARGET_BINS)

print(f"\n[CF-012] ===== PATTERN B 5-axis (observed) =====", file=sys.stderr)
print(f"  Kendall's W = {W_obs_B:.4f}", file=sys.stderr)
for i, a in enumerate(PATTERN_B_AXES):
    print(f"  {a}: peak bin B{peak_obs_B[i]+1}; means = {[f'{x:.3f}' for x in means_obs_B[i]]}", file=sys.stderr)
print(f"  Cell B criterion: modal peak = B{mode_peak_obs_B+1}; {n_in_target_obs_B}/5 in target {{B5,B6,B7}}; "
      f"PASS = {cell_b_obs_pass}", file=sys.stderr)

# ------------------------------------------------------------
# Audit-036 mandated 4-axis sensitivity check (drop muq_cardinality)
# ------------------------------------------------------------
W_obs_B4, peak_obs_B4, means_obs_B4, ranks_obs_B4 = compute_stats(PATTERN_B_AXES_NOMUQ, bin_of_surah)
cell_b_obs_pass_B4, mode_peak_obs_B4, n_in_target_obs_B4 = cell_b_criterion(peak_obs_B4, TARGET_BINS)
# 4-axis target: ≥ 3 of 4 in target (scaled down proportionally from 4/5)
cell_b4_strict_pass = (mode_peak_obs_B4 in TARGET_BINS) and (n_in_target_obs_B4 >= 3)

print(f"\n[CF-012] ===== PATTERN B 4-axis (muq-cardinality DROPPED; audit-036 sensitivity) =====", file=sys.stderr)
print(f"  Kendall's W = {W_obs_B4:.4f}", file=sys.stderr)
for i, a in enumerate(PATTERN_B_AXES_NOMUQ):
    print(f"  {a}: peak bin B{peak_obs_B4[i]+1}", file=sys.stderr)
print(f"  Cell B-4ax: modal peak = B{mode_peak_obs_B4+1}; {n_in_target_obs_B4}/4 in target; strict-PASS (≥3/4) = {cell_b4_strict_pass}", file=sys.stderr)

# ------------------------------------------------------------
# Observed statistics (Pattern A positive control)
# ------------------------------------------------------------
W_obs_A, peak_obs_A, means_obs_A, ranks_obs_A = compute_stats(PATTERN_A_POSCTRL_AXES, bin_of_surah)
# Positive control target: B8 = 0-indexed 7 (Medinan core); 1-bin tolerance = {B7, B8} = {6, 7}
POS_TARGET_BINS = {6, 7}
cell_b_obs_pass_A, mode_peak_obs_A, n_in_target_obs_A = cell_b_criterion(peak_obs_A, POS_TARGET_BINS)

print(f"\n[CF-012] ===== PATTERN A positive control (observed) =====", file=sys.stderr)
print(f"  Kendall's W = {W_obs_A:.4f}", file=sys.stderr)
for i, a in enumerate(PATTERN_A_POSCTRL_AXES):
    print(f"  {a}: peak bin B{peak_obs_A[i]+1}", file=sys.stderr)
print(f"  Positive control modal peak = B{mode_peak_obs_A+1}; {n_in_target_obs_A}/5 in {{B7,B8}}; "
      f"PASS = {cell_b_obs_pass_A}", file=sys.stderr)

# ------------------------------------------------------------
# Permutation null
# ------------------------------------------------------------
rng = np.random.default_rng(SEED)
n_ge_W_B = 0
n_cell_b_B = 0   # perms where Cell B criterion is met (target {B5,B6,B7})
n_ge_W_B4 = 0    # 4-axis sensitivity: W ≥ W_obs_B4
n_ge_W_A = 0
n_cell_b_A = 0   # positive control: perms where target {B7,B8} criterion met

W_perm_B = np.empty(N_PERM, dtype=float)
W_perm_B4 = np.empty(N_PERM, dtype=float)
W_perm_A = np.empty(N_PERM, dtype=float)

print(f"\n[CF-012] Running {N_PERM} permutations (seed {SEED})...", file=sys.stderr)

for p in range(N_PERM):
    # Permute the Nöldeke rank assignments across surahs
    perm_ranks = rng.permutation(noldeke_rank)
    perm_bins = rank_to_bin(perm_ranks)

    # Pattern B 5-axis W
    W_p_B, peak_p_B, _, _ = compute_stats(PATTERN_B_AXES, perm_bins)
    W_perm_B[p] = W_p_B
    if W_p_B >= W_obs_B:
        n_ge_W_B += 1
    cell_b_p, _, _ = cell_b_criterion(peak_p_B, TARGET_BINS)
    if cell_b_p:
        n_cell_b_B += 1

    # Pattern B 4-axis sensitivity
    W_p_B4, _, _, _ = compute_stats(PATTERN_B_AXES_NOMUQ, perm_bins)
    W_perm_B4[p] = W_p_B4
    if W_p_B4 >= W_obs_B4:
        n_ge_W_B4 += 1

    # Pattern A positive control
    W_p_A, peak_p_A, _, _ = compute_stats(PATTERN_A_POSCTRL_AXES, perm_bins)
    W_perm_A[p] = W_p_A
    if W_p_A >= W_obs_A:
        n_ge_W_A += 1
    cell_b_p_A, _, _ = cell_b_criterion(peak_p_A, POS_TARGET_BINS)
    if cell_b_p_A:
        n_cell_b_A += 1

    if (p + 1) % 2000 == 0:
        print(f"  [CF-012] perm {p+1}/{N_PERM}", file=sys.stderr)

# p-values
p_W_B = (1 + n_ge_W_B) / (1 + N_PERM)
p_cellb_B = (1 + n_cell_b_B) / (1 + N_PERM)
p_W_B4 = (1 + n_ge_W_B4) / (1 + N_PERM)
p_W_A = (1 + n_ge_W_A) / (1 + N_PERM)
p_cellb_A = (1 + n_cell_b_A) / (1 + N_PERM)

print(f"\n[CF-012] ===== RESULTS =====", file=sys.stderr)
print(f"  Cell A 5-axis (Pattern B Kendall's W): W_obs = {W_obs_B:.4f}, p_perm = {p_W_B:.5f}, "
      f"PASS @ α_bon={ALPHA_BON:.4f}: {p_W_B < ALPHA_BON}", file=sys.stderr)
print(f"  Cell A 4-axis (muq-DROPPED sensitivity): W_obs = {W_obs_B4:.4f}, p_perm = {p_W_B4:.5f}, "
      f"PASS @ α_bon={ALPHA_BON:.4f}: {p_W_B4 < ALPHA_BON}", file=sys.stderr)
print(f"  Cell B (Pattern B modal peak + 4/5 in {{B5,B6,B7}}): "
      f"observed PASS = {cell_b_obs_pass}, "
      f"mode bin = B{mode_peak_obs_B+1}, {n_in_target_obs_B}/5 in target, "
      f"p_perm = {p_cellb_B:.5f}, PASS @ α_bon: {p_cellb_B < ALPHA_BON and cell_b_obs_pass}", file=sys.stderr)
print(f"  Cell B-4ax (3/4 in target, muq-DROPPED): observed PASS = {cell_b4_strict_pass}, "
      f"mode = B{mode_peak_obs_B4+1}, {n_in_target_obs_B4}/4 in target", file=sys.stderr)
print(f"  POS-CTRL Pattern A Kendall's W: W_obs = {W_obs_A:.4f}, p_perm = {p_W_A:.5f}, "
      f"PASS: {p_W_A < ALPHA_BON}", file=sys.stderr)
print(f"  POS-CTRL Pattern A Cell B (target {{B7,B8}}): "
      f"observed PASS = {cell_b_obs_pass_A}, "
      f"mode bin = B{mode_peak_obs_A+1}, {n_in_target_obs_A}/5 in target, "
      f"p_perm = {p_cellb_A:.5f}", file=sys.stderr)

# MW-5 validity check
mw5_ok = (p_W_A < ALPHA_BON) and cell_b_obs_pass_A
print(f"  MW-5 POSITIVE CONTROL: {'PASS' if mw5_ok else 'FAIL - PIPELINE BROKEN'}", file=sys.stderr)

# Overall verdict
overall_pass = (
    p_W_B < ALPHA_BON
    and cell_b_obs_pass
    and p_cellb_B < ALPHA_BON
    and mw5_ok
)
print(f"\n[CF-012] ===== OVERALL VERDICT =====", file=sys.stderr)
print(f"  {'PASS-DIRECTED' if overall_pass else 'FAIL / NULL'}", file=sys.stderr)

# ------------------------------------------------------------
# Serialize results
# ------------------------------------------------------------
def bin_label(b):
    return f"B{b+1}"

# Identify surahs in modal peak bin (Pattern B)
surahs_in_mode = [
    {'sid': int(sid), 'name': psv[str(sid)]['name'], 'noldeke_rank': int(psv[str(sid)]['noldeke_rank'])}
    for sid in sids if bin_of_surah[sid - 1] == mode_peak_obs_B
]

# Per-bin surah distribution (full, all 8 bins)
surahs_by_bin = {}
for b in range(N_BINS):
    surahs_by_bin[bin_label(b)] = [
        {'sid': int(sid), 'name': psv[str(sid)]['name'],
         'noldeke_rank': int(psv[str(sid)]['noldeke_rank']),
         'noldeke_phase': psv[str(sid)]['noldeke_phase']}
        for sid in sids if bin_of_surah[sid - 1] == b
    ]

# W_perm distribution summary
W_perm_B_summary = {
    'mean': float(W_perm_B.mean()),
    'sd': float(W_perm_B.std()),
    'p50': float(np.percentile(W_perm_B, 50)),
    'p95': float(np.percentile(W_perm_B, 95)),
    'p99': float(np.percentile(W_perm_B, 99)),
    'p99_9': float(np.percentile(W_perm_B, 99.9)),
    'max': float(W_perm_B.max()),
}

result = {
    'id': 'cross-finding-012',
    'title': 'Late-Meccan Scripture-Announcement Apparatus — joint-peak concordance test',
    'bonferroni_family': 'cross-finding-012-joint-peak',
    'bonferroni_k': BON_K,
    'alpha_bon': ALPHA_BON,
    'direction': 'Late-Meccan-peak (B5/B6/B7 modal); 1-sided on W',
    'n_perm': N_PERM,
    'seed': SEED,
    'n_bins': N_BINS,
    'bin_rank_upper_edges': edges.tolist(),
    'bin_counts': bin_counts.tolist(),
    'late_meccan_band_bins_0indexed': lm_bin_indices,
    'target_bins_cell_b_0indexed': sorted(TARGET_BINS),

    'pattern_b': {
        'axes': PATTERN_B_AXES,
        'kendall_w_observed': float(W_obs_B),
        'kendall_w_p_perm': float(p_W_B),
        'kendall_w_bonferroni_survives': bool(p_W_B < ALPHA_BON),
        'per_axis_peak_bin': {a: bin_label(peak_obs_B[i]) for i, a in enumerate(PATTERN_B_AXES)},
        'per_axis_means_by_bin': {
            a: {bin_label(b): (float(means_obs_B[i, b]) if not math.isnan(means_obs_B[i, b]) else None)
                for b in range(N_BINS)}
            for i, a in enumerate(PATTERN_B_AXES)
        },
        'per_axis_ranks_by_bin': {
            a: {bin_label(b): float(ranks_obs_B[i, b]) for b in range(N_BINS)}
            for i, a in enumerate(PATTERN_B_AXES)
        },
        'cell_b_observed_pass': bool(cell_b_obs_pass),
        'cell_b_mode_peak_bin': bin_label(mode_peak_obs_B),
        'cell_b_n_axes_in_target': int(n_in_target_obs_B),
        'cell_b_p_perm': float(p_cellb_B),
        'cell_b_bonferroni_survives': bool(p_cellb_B < ALPHA_BON and cell_b_obs_pass),
        'w_perm_distribution': W_perm_B_summary,
        'surahs_in_mode_peak_bin': surahs_in_mode,
    },

    'pattern_b_4axis_sensitivity_audit036': {
        'axes': PATTERN_B_AXES_NOMUQ,
        'rationale': "muq_cardinality is Pattern-B BY DEFINITION per scratch connection note; dropping it tests whether the joint-peak signal survives on truly-evidentiary axes alone.",
        'kendall_w_observed': float(W_obs_B4),
        'kendall_w_p_perm': float(p_W_B4),
        'kendall_w_bonferroni_survives': bool(p_W_B4 < ALPHA_BON),
        'per_axis_peak_bin': {a: bin_label(peak_obs_B4[i]) for i, a in enumerate(PATTERN_B_AXES_NOMUQ)},
        'cell_b_4axis_strict_pass': bool(cell_b4_strict_pass),
        'cell_b_mode_peak_bin': bin_label(mode_peak_obs_B4),
        'cell_b_n_axes_in_target': int(n_in_target_obs_B4),
        'n_axes': 4,
    },

    'pattern_a_positive_control': {
        'axes': PATTERN_A_POSCTRL_AXES,
        'target_bins_0indexed': sorted(POS_TARGET_BINS),
        'kendall_w_observed': float(W_obs_A),
        'kendall_w_p_perm': float(p_W_A),
        'per_axis_peak_bin': {a: bin_label(peak_obs_A[i]) for i, a in enumerate(PATTERN_A_POSCTRL_AXES)},
        'cell_b_observed_pass': bool(cell_b_obs_pass_A),
        'cell_b_mode_peak_bin': bin_label(mode_peak_obs_A),
        'cell_b_n_axes_in_target': int(n_in_target_obs_A),
        'cell_b_p_perm': float(p_cellb_A),
        'mw5_pipeline_valid': bool(mw5_ok),
    },

    'surahs_by_bin': surahs_by_bin,

    'verdict': {
        'cell_a_kw_pass_5axis': bool(p_W_B < ALPHA_BON),
        'cell_a_kw_pass_4axis_sensitivity': bool(p_W_B4 < ALPHA_BON),
        'cell_b_joint_peak_pass': bool(cell_b_obs_pass and p_cellb_B < ALPHA_BON),
        'cell_b_4axis_strict_pass': bool(cell_b4_strict_pass),
        'mw5_pos_control_pass': bool(mw5_ok),
        'verdict_ceiling': 'PASS-DIRECTED (post-hoc-noticed; requires independent replication for CONFIRMED)',
        'overall': 'PASS-DIRECTED' if overall_pass else 'FAIL-OR-NULL',
    },

    'pre_reg': 'findings/phase-b-hypotheses/cross-finding-012-late-meccan-scripture-announcement-prereg.md',
    'upstream_json': str(UPSTREAM_JSON.relative_to(ROOT)),
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"\n[CF-012] Results written to {OUT_JSON.relative_to(ROOT)}", file=sys.stderr)
