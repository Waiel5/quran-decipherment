#!/usr/bin/env python3
"""H-NEW-203 — Full 30-juzʾ partition against Fisher-Rao structural geometry.

Two pre-registered primary tests (bonferroni_k=2, alpha_bon=0.025):
  T1. Boundary concentration: sum of windowed Fisher-Rao jumps at the 29
      juzʾ-internal cuts vs. null (10k random 29-cut samples).
  T2. Segment coherence: mean FR distance verse→segment-centroid under
      canonical juzʾ partition vs. null (10k length-multiset-preserving
      random partitions into 30 contiguous segments).

Plus secondaries: per-boundary rank, surah-seam-matched null, per-juzʾ
coherence, scramble-corpus MW-5.

Pre-reg: findings/phase-b-hypotheses/h-new-203-prereg.md
Seed: 20260419. Deterministic. Numpy-accelerated.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

ROOT = Path("/Users/grey/Downloads/quran")
sys.path.insert(0, str(ROOT))
from analysis.tools.loader import load_quran  # noqa: E402

SEED = 20260419
N_PERM = 10000
W = 20
K_TOP = 500
DIRICHLET_ALPHA = 0.5
ALPHA_BON = 0.025
N_JUZ_INTERNAL = 29
N_TOTAL_VERSES = 6236

PREREG_PATH = ROOT / "findings/phase-b-hypotheses/h-new-203-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-203.json"
QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"

JUZ_STARTS = [
    (1, 1, 1), (2, 2, 142), (3, 2, 253), (4, 3, 93), (5, 4, 24),
    (6, 4, 148), (7, 5, 82), (8, 6, 111), (9, 7, 88), (10, 8, 41),
    (11, 9, 93), (12, 11, 6), (13, 12, 53), (14, 15, 1), (15, 17, 1),
    (16, 18, 75), (17, 21, 1), (18, 23, 1), (19, 25, 21), (20, 27, 56),
    (21, 29, 46), (22, 33, 31), (23, 36, 28), (24, 39, 32), (25, 41, 47),
    (26, 46, 1), (27, 51, 31), (28, 58, 1), (29, 67, 1), (30, 78, 1),
]
JUZ_SURAH_ALIGNED = {14, 15, 17, 18, 26, 29, 30}

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")


def load_per_verse_roots():
    per_verse_roots = defaultdict(list)
    global_counts = Counter()
    with open(QAC_FILE, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1)); vid = int(m.group(2)); feat = parts[3]
            if "STEM" not in feat:
                continue
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            per_verse_roots[(sid, vid)].append(rm.group(1))
            global_counts[rm.group(1)] += 1
    return per_verse_roots, global_counts


def build_corpus():
    surahs = load_quran("no-tashkeel")
    verse_surah, verse_id, surah_start_positions = [], [], []
    g = 0
    for s in surahs:
        surah_start_positions.append(g + 1)
        for v in s.verses:
            g += 1
            verse_surah.append(s.id); verse_id.append(v.id)
    assert g == N_TOTAL_VERSES
    return verse_surah, verse_id, surah_start_positions


def juz_positions(verse_surah, verse_id):
    pos_of = {(sid, vid): i + 1 for i, (sid, vid) in enumerate(zip(verse_surah, verse_id))}
    return [pos_of[(sid, vid)] for (_j, sid, vid) in JUZ_STARTS]


def build_count_matrix(per_verse_roots, global_counts, verse_surah, verse_id):
    top_roots = [r for r, _ in global_counts.most_common(K_TOP)]
    idx = {r: i for i, r in enumerate(top_roots)}
    n = len(verse_surah)
    C = np.zeros((n, K_TOP), dtype=np.float64)
    totals = np.zeros(n, dtype=np.int64)
    for i, (sid, vid) in enumerate(zip(verse_surah, verse_id)):
        roots = per_verse_roots.get((sid, vid), [])
        for r in roots:
            j = idx.get(r)
            if j is not None:
                C[i, j] += 1.0
        totals[i] = len(roots)
    return C, top_roots, totals


def smooth_norm_rows(M):
    """Dirichlet-smooth + L1-normalize row-wise."""
    X = M + DIRICHLET_ALPHA
    s = X.sum(axis=1, keepdims=True)
    return X / s


def fr_distance_rows(SQA, SQB):
    """Row-wise Fisher-Rao distance between sqrt-prob matrices."""
    bc = np.einsum("ij,ij->i", SQA, SQB)
    bc = np.clip(bc, -1.0, 1.0)
    return 2.0 * np.arccos(bc)


def precompute_cut_distances(C):
    """All 6235 cut distances. For cut p (1-indexed cut between verses p-1 and p),
    window-before = verses [max(0,p-1-W) .. p-1), window-after = [p-1 .. min(n,p-1+W)).
    Uses cumulative-sum for O(1) pooling."""
    n = C.shape[0]
    # cumsum row prefix: cum[i] = sum of rows 0..i-1, shape (n+1, K)
    cum = np.zeros((n + 1, K_TOP), dtype=np.float64)
    cum[1:] = np.cumsum(C, axis=0)

    n_cuts = n - 1
    # cut p (1-indexed global verse pos that cut precedes, p in 2..n) → cut index p-2 in 0..n-2
    # before: rows [max(0,p-1-W) .. p-1), after: rows [p-1 .. min(n,p-1+W))
    ps = np.arange(2, n + 1)  # 1-indexed cut positions
    b_lo = np.maximum(0, (ps - 1) - W)
    b_hi = ps - 1
    a_lo = ps - 1
    a_hi = np.minimum(n, (ps - 1) + W)
    before = cum[b_hi] - cum[b_lo]
    after = cum[a_hi] - cum[a_lo]
    pb = smooth_norm_rows(before)
    pa = smooth_norm_rows(after)
    sqpb = np.sqrt(pb); sqpa = np.sqrt(pa)
    return fr_distance_rows(sqpb, sqpa)


# ---------------------------------------------------------------------------
# Test 1
# ---------------------------------------------------------------------------

def test1_boundary_concentration(all_cut_d, juz_internal):
    obs_vals = np.array([all_cut_d[p - 2] for p in juz_internal])
    T_obs = float(obs_vals.sum())

    rng = np.random.default_rng(SEED + 1)
    n_cuts = len(all_cut_d)
    # Efficient: sample without replacement, 29 indices, n_perm times
    T_null = np.empty(N_PERM, dtype=np.float64)
    for i in range(N_PERM):
        sample_idx = rng.choice(n_cuts, size=N_JUZ_INTERNAL, replace=False)
        T_null[i] = all_cut_d[sample_idx].sum()

    count_ge = int((T_null >= T_obs).sum())
    p = (1 + count_ge) / (N_PERM + 1)
    mean = float(T_null.mean()); sd = float(T_null.std(ddof=1))
    z = (T_obs - mean) / sd if sd > 0 else 0.0
    return {
        "T_obs": T_obs, "null_mean": mean, "null_sd": sd, "z": float(z),
        "p_one_sided_upper": p, "pass": p < ALPHA_BON,
        "obs_per_boundary": obs_vals.tolist(),
    }


def test1_surah_matched(all_cut_d, juz_internal, surah_start_positions, n):
    surah_seam_set = set(surah_start_positions[1:])
    n_surah_aligned_obs = sum(1 for p in juz_internal if p in surah_seam_set)
    seam_cuts = np.array([p - 2 for p in surah_seam_set if 2 <= p <= n], dtype=np.int64)
    intra_cuts = np.array([p - 2 for p in range(2, n + 1) if p not in surah_seam_set], dtype=np.int64)

    obs_vals = np.array([all_cut_d[p - 2] for p in juz_internal])
    T_obs = float(obs_vals.sum())

    rng = np.random.default_rng(SEED + 2)
    T_null = np.empty(N_PERM, dtype=np.float64)
    for i in range(N_PERM):
        s_sel = rng.choice(seam_cuts, size=n_surah_aligned_obs, replace=False)
        i_sel = rng.choice(intra_cuts, size=N_JUZ_INTERNAL - n_surah_aligned_obs, replace=False)
        T_null[i] = all_cut_d[s_sel].sum() + all_cut_d[i_sel].sum()

    count_ge = int((T_null >= T_obs).sum())
    p = (1 + count_ge) / (N_PERM + 1)
    mean = float(T_null.mean()); sd = float(T_null.std(ddof=1))
    z = (T_obs - mean) / sd if sd > 0 else 0.0
    return {
        "T_obs": T_obs, "null_mean": mean, "null_sd": sd, "z": float(z),
        "p_one_sided_upper": p, "n_surah_aligned": n_surah_aligned_obs,
        "descriptive_only": True,
    }


# ---------------------------------------------------------------------------
# Test 2
# ---------------------------------------------------------------------------

def per_verse_windowed_dist_clipped(C, cum, seg_lo, seg_hi):
    """For each verse v in [seg_lo, seg_hi), compute windowed root dist
    clipped to [seg_lo, seg_hi). Returns (seg_len, K_TOP) sqrt-prob matrix.
    """
    L = seg_hi - seg_lo
    vs = np.arange(seg_lo, seg_hi)
    lo = np.maximum(seg_lo, vs - W)
    hi = np.minimum(seg_hi, vs + W + 1)
    pooled = cum[hi] - cum[lo]
    P = smooth_norm_rows(pooled)
    return np.sqrt(P)


def partition_coherence(C, cum, cut_positions_1idx, n):
    """cut_positions_1idx: 29 1-indexed cut positions (start of segments 2..30).
    Segments: 0-indexed half-open [lo, hi).
    """
    cuts = sorted(cut_positions_1idx)
    lo = 0
    total_sum = 0.0
    total_count = 0
    per_seg_mean = []
    segs = []
    for c in cuts:
        segs.append((lo, c - 1))
        lo = c - 1
    segs.append((lo, n))
    for (s_lo, s_hi) in segs:
        L = s_hi - s_lo
        if L <= 0:
            per_seg_mean.append(0.0)
            continue
        # centroid
        cent = cum[s_hi] - cum[s_lo]
        cent_p = smooth_norm_rows(cent.reshape(1, -1))
        cent_sq = np.sqrt(cent_p)  # (1, K)
        # per-verse clipped
        SQV = per_verse_windowed_dist_clipped(C, cum, s_lo, s_hi)  # (L, K)
        bc = SQV @ cent_sq.T  # (L, 1)
        bc = np.clip(bc.ravel(), -1.0, 1.0)
        d = 2.0 * np.arccos(bc)
        seg_sum = float(d.sum())
        total_sum += seg_sum
        total_count += L
        per_seg_mean.append(seg_sum / L)
    T2 = total_sum / total_count
    return T2, per_seg_mean


def test2_segment_coherence(C, cum, juz_positions_1idx, n):
    cuts_obs = juz_positions_1idx[1:]
    T_obs, per_seg_obs = partition_coherence(C, cum, cuts_obs, n)

    starts = list(juz_positions_1idx) + [n + 1]
    seg_lens = [starts[i + 1] - starts[i] for i in range(30)]
    assert sum(seg_lens) == n

    rng = random.Random(SEED + 3)
    T_null = np.empty(N_PERM, dtype=np.float64)
    lengths_arr = list(seg_lens)
    for i in range(N_PERM):
        perm = lengths_arr[:]
        rng.shuffle(perm)
        cuts = []
        pos = 1
        for L in perm[:-1]:
            pos += L
            cuts.append(pos)
        T_val, _ = partition_coherence(C, cum, cuts, n)
        T_null[i] = T_val

    count_le = int((T_null <= T_obs).sum())
    p = (1 + count_le) / (N_PERM + 1)
    mean = float(T_null.mean()); sd = float(T_null.std(ddof=1))
    z = (T_obs - mean) / sd if sd > 0 else 0.0
    return {
        "T_obs": T_obs, "null_mean": mean, "null_sd": sd, "z": float(z),
        "p_one_sided_lower": p, "pass": p < ALPHA_BON,
        "segment_lengths": seg_lens, "per_segment_mean_dist": per_seg_obs,
    }


# ---------------------------------------------------------------------------
# MW-5
# ---------------------------------------------------------------------------

def mw5_scramble(C, juz_internal, n):
    rng = np.random.default_rng(SEED + 4)
    perm = rng.permutation(n)
    C_scr = C[perm]
    all_d = precompute_cut_distances(C_scr)
    return float(sum(all_d[p - 2] for p in juz_internal))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    prereg_sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED={SEED} W={W} K_TOP={K_TOP} DIR={DIRICHLET_ALPHA} PERMS={N_PERM}", file=sys.stderr)

    verse_surah, verse_id, surah_start_positions = build_corpus()
    n = len(verse_surah)
    print(f"corpus: {n} verses, {len(surah_start_positions)} surahs", file=sys.stderr)

    per_verse_roots, global_counts = load_per_verse_roots()
    total_tokens = sum(len(v) for v in per_verse_roots.values())
    print(f"QAC: {total_tokens} root tokens, {len(global_counts)} distinct", file=sys.stderr)

    C, top_roots, totals = build_count_matrix(
        per_verse_roots, global_counts, verse_surah, verse_id
    )
    mean_tokens = float(totals.mean())
    nonempty = int((totals > 0).sum())
    print(f"per-verse: mean={mean_tokens:.2f} roots, nonempty={nonempty}/{n}", file=sys.stderr)

    jpos = juz_positions(verse_surah, verse_id)
    juz_internal = jpos[1:]
    assert len(juz_internal) == N_JUZ_INTERNAL

    # Precompute cumsum
    cum = np.zeros((n + 1, K_TOP), dtype=np.float64)
    cum[1:] = np.cumsum(C, axis=0)

    print("Precomputing all cut-distances...", file=sys.stderr)
    all_cut_d = precompute_cut_distances(C)
    assert len(all_cut_d) == n - 1

    # Test 1
    print(f"Test 1: {N_PERM} perms...", file=sys.stderr)
    t1 = test1_boundary_concentration(all_cut_d, juz_internal)
    print(f"  T1 obs={t1['T_obs']:.4f} null={t1['null_mean']:.4f}±{t1['null_sd']:.4f} z={t1['z']:.3f} p={t1['p_one_sided_upper']:.5f} pass={t1['pass']}", file=sys.stderr)

    # S2 matched
    print("S2: surah-seam-matched...", file=sys.stderr)
    t1_matched = test1_surah_matched(all_cut_d, juz_internal, surah_start_positions, n)
    print(f"  T1_matched p={t1_matched['p_one_sided_upper']:.5f} z={t1_matched['z']:.3f}", file=sys.stderr)

    # S1 per-boundary rank
    all_arr = np.asarray(all_cut_d)
    per_boundary_ranks = []
    for k, p in enumerate(juz_internal):
        juz_k = k + 2
        d_val = float(all_cut_d[p - 2])
        # percentile_rank: fraction of cuts with d < d_val
        pr = float((all_arr < d_val).sum()) / (len(all_arr) - 1)
        per_boundary_ranks.append({
            "juz_start": juz_k, "global_pos": p,
            "surah": JUZ_STARTS[juz_k - 1][1], "verse_id": JUZ_STARTS[juz_k - 1][2],
            "surah_aligned": juz_k in JUZ_SURAH_ALIGNED,
            "D": d_val, "percentile_rank": pr,
        })
    mean_rank = sum(r["percentile_rank"] for r in per_boundary_ranks) / len(per_boundary_ranks)
    above_90 = sum(1 for r in per_boundary_ranks if r["percentile_rank"] >= 0.90)
    above_75 = sum(1 for r in per_boundary_ranks if r["percentile_rank"] >= 0.75)

    # Test 2
    print(f"Test 2: {N_PERM} perms...", file=sys.stderr)
    t2 = test2_segment_coherence(C, cum, jpos, n)
    print(f"  T2 obs={t2['T_obs']:.5f} null={t2['null_mean']:.5f}±{t2['null_sd']:.5f} z={t2['z']:.3f} p={t2['p_one_sided_lower']:.5f} pass={t2['pass']}", file=sys.stderr)

    # Per-juzʾ
    per_juz_coh = [
        {"juz": k + 1, "mean_centroid_dist": t2["per_segment_mean_dist"][k],
         "segment_length": t2["segment_lengths"][k]}
        for k in range(30)
    ]
    per_juz_coh_sorted = sorted(per_juz_coh, key=lambda x: x["mean_centroid_dist"])

    # MW-5
    print("MW-5...", file=sys.stderr)
    T1_scr = mw5_scramble(C, juz_internal, n)
    delta = t1["T_obs"] - T1_scr
    delta_sd = delta / t1["null_sd"] if t1["null_sd"] > 0 else 0.0
    mw5_broken = abs(delta_sd) < 0.2

    # Verdict
    if mw5_broken:
        verdict = "INSTRUMENT-BROKEN"
    elif t1["pass"] and t2["pass"]:
        verdict = "STRONG-PASS"
    elif t1["pass"]:
        verdict = "BOUNDARY-ONLY"
    elif t2["pass"]:
        verdict = "COHERENCE-ONLY"
    else:
        # Check for sign-reversal in Test 2 (juzʾ LESS coherent than matched random)
        if t2["z"] > 2.0:
            verdict = "NULL-with-SIGN-REVERSAL-EXPLORATORY (T2)"
        else:
            verdict = "NULL"

    output = {
        "finding_id": "h-new-203",
        "title": "Full 30-juzʾ partition against Fisher-Rao structural geometry",
        "pre_reg_path": str(PREREG_PATH),
        "pre_reg_sha256": prereg_sha,
        "date": "2026-04-17",
        "seed": SEED,
        "rules_tuple": "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan, 30-juzʾ canonical partition)",
        "parameters": {
            "window_W": W, "K_top_roots": K_TOP,
            "dirichlet_alpha": DIRICHLET_ALPHA,
            "n_perm": N_PERM, "alpha_bon": ALPHA_BON, "bonferroni_k": 2,
        },
        "corpus": {
            "n_verses": n, "mean_root_tokens_per_verse": mean_tokens,
            "verses_with_no_roots": n - nonempty,
        },
        "verdict": verdict,
        "test1_boundary_concentration": {
            "T_obs": t1["T_obs"], "null_mean": t1["null_mean"],
            "null_sd": t1["null_sd"], "z": t1["z"],
            "p_one_sided_upper": t1["p_one_sided_upper"], "pass": t1["pass"],
        },
        "test2_segment_coherence": {
            "T_obs": t2["T_obs"], "null_mean": t2["null_mean"],
            "null_sd": t2["null_sd"], "z": t2["z"],
            "p_one_sided_lower": t2["p_one_sided_lower"], "pass": t2["pass"],
            "sign_note": "T2_obs > null → juzʾ segments are LESS coherent than length-matched random partitions" if t2["z"] > 0 else "T2_obs ≤ null → juzʾ segments are MORE coherent than length-matched random partitions",
        },
        "secondary_S1_per_boundary": {
            "mean_percentile_rank": mean_rank,
            "n_above_90th": above_90, "n_above_75th": above_75,
            "per_boundary": per_boundary_ranks,
        },
        "secondary_S2_surah_seam_matched_null": t1_matched,
        "secondary_S3_per_juz_coherence": {
            "per_juz": per_juz_coh,
            "ranked_most_coherent_first": per_juz_coh_sorted[:5],
            "ranked_least_coherent_first": per_juz_coh_sorted[-5:],
        },
        "secondary_S4_mw5_scramble": {
            "T1_obs": t1["T_obs"], "T1_scramble": T1_scr,
            "delta": delta, "delta_in_null_sd_units": delta_sd,
            "instrument_broken": mw5_broken,
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print("H-NEW-203 — 30-juzʾ × Fisher-Rao")
    print("=" * 70)
    print(f"Verdict: {verdict}")
    print()
    print(f"Test 1 (boundary concentration):")
    print(f"  T1_obs={t1['T_obs']:.4f}  null={t1['null_mean']:.4f}±{t1['null_sd']:.4f}")
    print(f"  z={t1['z']:.3f}  p={t1['p_one_sided_upper']:.5f}  α_bon={ALPHA_BON}  pass={t1['pass']}")
    print()
    print(f"Test 2 (segment coherence):")
    print(f"  T2_obs={t2['T_obs']:.5f}  null={t2['null_mean']:.5f}±{t2['null_sd']:.5f}")
    print(f"  z={t2['z']:.3f}  p={t2['p_one_sided_lower']:.5f}  α_bon={ALPHA_BON}  pass={t2['pass']}")
    if t2["z"] > 0:
        print(f"  *** T2 SIGN: juzʾ segments are LESS coherent than matched random (z=+{t2['z']:.2f}) ***")
    print()
    print(f"S1 per-boundary rank: mean pct={mean_rank:.3f}  #≥p90={above_90}/29  #≥p75={above_75}/29")
    print(f"S2 surah-seam matched: p={t1_matched['p_one_sided_upper']:.5f}  z={t1_matched['z']:.3f}")
    print()
    print("Top-5 most-coherent juzʾ:")
    for r in per_juz_coh_sorted[:5]:
        print(f"  juzʾ {r['juz']:2d}  d={r['mean_centroid_dist']:.4f}  len={r['segment_length']}")
    print("Top-5 least-coherent juzʾ:")
    for r in per_juz_coh_sorted[-5:]:
        print(f"  juzʾ {r['juz']:2d}  d={r['mean_centroid_dist']:.4f}  len={r['segment_length']}")
    print()
    print(f"MW-5: obs={t1['T_obs']:.4f}  scr={T1_scr:.4f}  Δ={delta:+.4f} ({delta_sd:+.2f} null-SD)")
    print(f"Output: {OUT_JSON}")


if __name__ == "__main__":
    main()
