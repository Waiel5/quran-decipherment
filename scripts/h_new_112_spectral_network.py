"""H-NEW-112 — Spectral Graph-Theoretic Analysis of the Meta-Cluster Network.

Pre-reg: findings/phase-b-hypotheses/h-new-112-spectral-network-prereg.md
Family:  h-new-112-spectral-analysis
Bonferroni k=3, α_bon=0.0167.
N_PERM=10,000.
Seed=20260417.

Data:
  H-NEW-89 incidence M (114 surahs × 11 cluster systems), locked verbatim.

Pipeline:
  1. Build M and A = M·Mᵀ (zero diagonal; weighted).
  2. Compute D, L = D − A, L_norm = I − D^(−1/2) A D^(−1/2).
  3. Full eigendecomposition of L_norm.
  4. C1: spectral gap λ_4 − λ_3 vs ER(n=114, m=E_obs) null, 10K draws.
  5. C2: Fiedler v_2 sign partition vs Meccan/Medinan, muqaṭṭāʿat, long/short (χ²).
  6. C3: k_eigengap ≥ 3 (one-sided threshold).
  7. Additional nulls: configuration-model, Barabási-Albert, stochastic-block-model.
  8. MW-5 positive control: planted 3-block SBM.
  9. Q 62 saddle/peak characterization.
  10. Dump full JSON.

Outputs:
  - findings/phase-b-hypotheses/csv/h-new-112.json
  - stdout summary
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.linalg import eigh

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260417
N_PERM = 10_000
# Post-audit-035 (2026-04-17): C3 demoted to descriptive-only (algorithmic threshold
# is not a hypothesis test). Bonferroni tightened from k=3 to k=2. α_bon = 0.025.
BONFERRONI_K = 2
ALPHA_BON = 0.05 / BONFERRONI_K  # 0.025
EPS = 1e-9

# ---- Locked cluster systems (verbatim from H-NEW-89 JSON) ----------------------------
CLUSTERS = {
    "C1_alif_lam_mim":      [2, 3, 29, 30, 31, 32],
    "C2_alif_lam_ra":       [10, 11, 12, 14, 15],
    "C3_ha_mim":            [40, 41, 42, 43, 44, 45, 46],
    "C4_ta_sin_mim":        [26, 27, 28],
    "C5_musabbihat":        [57, 59, 61, 62, 64],
    "C6_sab_al_tiwal":      [2, 3, 4, 5, 6, 7, 9],
    "C7_friday":            [18, 32, 62, 76],
    "C8_khawatim_extended": [59, 62],
    "C9_muawwidhatan":      [113, 114],
    "C10_zahrawan":         [2, 3],
    "C11_mufassal":         list(range(49, 115)),
}

# Muqaṭṭāʿat-opened surahs (29 classical canon; from H-NEW-56/cross-finding-008):
MUQATTAAT_SURAHS = {
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68,
}

N_SURAHS = 114
N_CLUSTERS = len(CLUSTERS)


# ---- Helpers -------------------------------------------------------------------------

def build_incidence():
    """M[s-1, c] = 1 if surah s in cluster c."""
    M = np.zeros((N_SURAHS, N_CLUSTERS), dtype=np.float64)
    for c_idx, (name, members) in enumerate(CLUSTERS.items()):
        for s in members:
            M[s - 1, c_idx] = 1.0
    return M


def build_adjacency(M):
    """Weighted surah-surah adjacency A = M M^T with zero diagonal."""
    A = M @ M.T
    np.fill_diagonal(A, 0.0)
    return A


def normalized_laplacian(A):
    """L_norm = I - D^(-1/2) A D^(-1/2) with ε regularizer for isolates."""
    d = A.sum(axis=1)
    d_reg = np.maximum(d, EPS)
    d_inv_sqrt = 1.0 / np.sqrt(d_reg)
    # For true isolates, d=0: L_norm row/col = 0 except diag=1 -> eigenvalue 1 contribution
    D_inv_sqrt = np.diag(d_inv_sqrt)
    L_norm = np.eye(len(A)) - D_inv_sqrt @ A @ D_inv_sqrt
    # Enforce symmetry (numerical):
    L_norm = 0.5 * (L_norm + L_norm.T)
    return L_norm, d


def combinatorial_laplacian(A):
    d = A.sum(axis=1)
    L = np.diag(d) - A
    return L


def spectrum(L):
    """Full eigendecomposition; ascending eigenvalues."""
    w, v = eigh(L)  # already ascending
    return w, v


def er_null_spectral_gap(n, n_edges, weight_multiset, rng, k_gap=3):
    """One ER(n, m) draw with weight-matched edge weights. Returns λ_{k_gap+1} − λ_{k_gap}."""
    # Draw m distinct edges uniformly from (n choose 2)
    n_pairs = n * (n - 1) // 2
    idx = rng.choice(n_pairs, size=n_edges, replace=False)
    # Convert pair index to (i,j): enumerate upper triangular
    i_arr, j_arr = np.triu_indices(n, k=1)
    src = i_arr[idx]; dst = j_arr[idx]
    weights = rng.permutation(weight_multiset)
    A = np.zeros((n, n))
    A[src, dst] = weights
    A[dst, src] = weights
    L_norm, _ = normalized_laplacian(A)
    w, _ = spectrum(L_norm)
    return w[k_gap] - w[k_gap - 1], w  # gap between positions k_gap and k_gap-1 (0-indexed: λ_{k+1}-λ_k)


def configuration_model_rewire(A, rng, n_swap_mult=10):
    """Degree-preserving edge swap on weighted adjacency (treat each weighted edge as a stub)."""
    n = len(A)
    # Extract edge list with weights
    i_arr, j_arr = np.triu_indices(n, k=1)
    weights = A[i_arr, j_arr]
    mask = weights > 0
    edges = list(zip(i_arr[mask].tolist(), j_arr[mask].tolist(), weights[mask].tolist()))
    n_edges = len(edges)
    if n_edges < 2:
        return A.copy()
    n_swaps = n_swap_mult * n_edges
    edges_arr = np.array(edges, dtype=[('u', int), ('v', int), ('w', float)])
    for _ in range(n_swaps):
        a, b = rng.integers(0, n_edges, size=2)
        if a == b:
            continue
        u1, v1, w1 = edges_arr[a]
        u2, v2, w2 = edges_arr[b]
        # Swap: new (u1, v2) and (u2, v1) keeping weights with original edge
        # Require no self-loops / duplicates
        if u1 == v2 or u2 == v1:
            continue
        if u1 == u2 or v1 == v2:
            continue
        # Check new pairs don't already exist
        # Build set (expensive; cheap heuristic: skip if any exists)
        edges_arr[a] = (u1, v2, w1)
        edges_arr[b] = (u2, v1, w2)
    A_new = np.zeros_like(A)
    for u, v, w in edges_arr:
        A_new[u, v] += w
        A_new[v, u] += w
    return A_new


def barabasi_albert_null(n, n_edges, weight_multiset, rng):
    """Simple BA: each new node attaches to m existing with prob ~ degree."""
    m_attach = max(1, round(n_edges / n))
    A = np.zeros((n, n))
    # seed with small clique
    for i in range(m_attach + 1):
        for j in range(i + 1, m_attach + 1):
            A[i, j] = 1; A[j, i] = 1
    for i in range(m_attach + 1, n):
        d = A.sum(axis=1)
        d[i:] = 0  # only existing nodes
        if d.sum() == 0:
            break
        p = d / d.sum()
        targets = rng.choice(n, size=m_attach, replace=False, p=p)
        for t in targets:
            A[i, t] = 1; A[t, i] = 1
    # Assign weights from multiset
    i_arr, j_arr = np.triu_indices(n, k=1)
    mask = A[i_arr, j_arr] > 0
    n_real = mask.sum()
    w_pool = rng.choice(weight_multiset, size=n_real, replace=True)
    A2 = np.zeros_like(A)
    A2[i_arr[mask], j_arr[mask]] = w_pool
    A2 = A2 + A2.T
    return A2


def sbm_null(n, block_sizes, p_in, p_out, rng, weight_multiset):
    """Stochastic block model with given block sizes, intra/inter edge probs."""
    A = np.zeros((n, n))
    # Build block assignment
    labels = np.concatenate([[i] * sz for i, sz in enumerate(block_sizes)])[:n]
    rng.shuffle(labels)
    for i in range(n):
        for j in range(i + 1, n):
            p = p_in if labels[i] == labels[j] else p_out
            if rng.random() < p:
                A[i, j] = 1; A[j, i] = 1
    # Weight assignment
    i_arr, j_arr = np.triu_indices(n, k=1)
    mask = A[i_arr, j_arr] > 0
    n_real = int(mask.sum())
    if n_real > 0 and len(weight_multiset) > 0:
        w_pool = rng.choice(weight_multiset, size=n_real, replace=True)
        A[i_arr[mask], j_arr[mask]] = w_pool
        A = np.triu(A) + np.triu(A, 1).T
    return A, labels


def chi2_2x2(a, b, c, d):
    """χ² test on 2×2 table [[a,b],[c,d]]. Returns χ² and p."""
    table = np.array([[a, b], [c, d]])
    if table.sum() == 0 or np.any(table.sum(axis=0) == 0) or np.any(table.sum(axis=1) == 0):
        return 0.0, 1.0
    chi2, p, _, _ = stats.chi2_contingency(table, correction=False)
    return chi2, p


def count_components(A):
    """Return number of connected components via BFS on the unweighted adjacency."""
    n = len(A)
    visited = [False] * n
    n_comp = 0
    for start in range(n):
        if visited[start]:
            continue
        n_comp += 1
        stack = [start]
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            for v in np.where(A[u] > 0)[0]:
                if not visited[v]:
                    stack.append(int(v))
    return n_comp


# ---- MW-5 positive control -----------------------------------------------------------

def mw5_positive_control(rng):
    """Planted 3-block SBM: 38+38+38=114; p_in=0.3, p_out=0.02."""
    n = 114
    block_sizes = [38, 38, 38]
    labels = np.concatenate([[i] * sz for i, sz in enumerate(block_sizes)])
    # DO NOT shuffle: keep labels contiguous for clarity
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            p = 0.3 if labels[i] == labels[j] else 0.02
            if rng.random() < p:
                A[i, j] = 1; A[j, i] = 1
    L_norm, _ = normalized_laplacian(A)
    w, v = spectrum(L_norm)
    gap_k3 = w[3] - w[2]
    # Eigengap heuristic: for 1-indexed eigenvalues, if largest gap is between λ_k and λ_{k+1},
    # then k communities. gaps_early[i] corresponds to gap between w[i+1] (0-idx) and w[i+2] (0-idx),
    # which is 1-indexed gap after λ_{i+2}. So community count = i+2.
    # gaps_early[i] = w[i+2] - w[i+1] for i = 0..7 (covers gaps after λ_2 through λ_9).
    gaps_early = [w[i + 2] - w[i + 1] for i in range(min(9, n - 2))]
    best_i = int(np.argmax(gaps_early))
    k_eigengap = best_i + 2  # community count = 1-indexed eigenvalue position before gap
    return {
        "planted_k": 3,
        "gap_k3": float(gap_k3),
        "k_eigengap": k_eigengap,
        "gaps_after_lambda_k": {str(i + 2): float(g) for i, g in enumerate(gaps_early)},
        "spectrum_head": [float(x) for x in w[:10]],
    }


# ---- Main pipeline -------------------------------------------------------------------

def main():
    rng = np.random.default_rng(SEED)

    start = time.time()
    out = {
        "id": "H-NEW-112",
        "date": "2026-04-17",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "bonferroni_family": "h-new-112-spectral-analysis",
        "rules_tuple": "no-tashkeel; weighted A=M*M^T; L_norm; ε=1e-9 isolate reg",
    }

    # -------- Build the network --------------------------------------------------------
    M = build_incidence()
    A = build_adjacency(M)
    L_comb = combinatorial_laplacian(A)
    L_norm, d = normalized_laplacian(A)

    n_comp = count_components(A)

    w_norm, V_norm = spectrum(L_norm)
    w_comb, V_comb = spectrum(L_comb)

    # Edge count (unweighted): number of nonzero off-diagonal entries / 2
    E_obs = int((A > 0).sum() // 2)
    weight_multiset = A[np.triu_indices(N_SURAHS, k=1)]
    weight_multiset = weight_multiset[weight_multiset > 0]

    out["graph"] = {
        "n_nodes": N_SURAHS,
        "n_edges": E_obs,
        "n_components": n_comp,
        "weighted_degree_range": [float(d.min()), float(d.max())],
        "weighted_degree_mean": float(d.mean()),
        "n_isolates": int((d == 0).sum()),
        "weight_multiset_stats": {
            "n_edges_positive": int(len(weight_multiset)),
            "max_weight": float(weight_multiset.max()) if len(weight_multiset) else 0,
            "mean_weight": float(weight_multiset.mean()) if len(weight_multiset) else 0,
            "weight_counts": {str(int(w)): int((weight_multiset == w).sum()) for w in np.unique(weight_multiset)},
        },
    }

    # -------- Full spectrum dump -------------------------------------------------------
    out["spectrum_L_norm"] = [float(x) for x in w_norm]
    out["spectrum_L_comb"] = [float(x) for x in w_comb]

    # Fiedler vector (second-smallest eigenvector of L_norm)
    v_fiedler = V_norm[:, 1]
    # Canonicalize sign: ensure largest-magnitude entry is positive
    if v_fiedler[np.argmax(np.abs(v_fiedler))] < 0:
        v_fiedler = -v_fiedler

    out["fiedler"] = {
        "lambda_2": float(w_norm[1]),
        "vector": [float(x) for x in v_fiedler],
        "sign_partition_plus": [int(i + 1) for i in range(N_SURAHS) if v_fiedler[i] > 0],
        "sign_partition_minus": [int(i + 1) for i in range(N_SURAHS) if v_fiedler[i] < 0],
        "sign_partition_zero": [int(i + 1) for i in range(N_SURAHS) if v_fiedler[i] == 0],
    }

    # -------- Eigengap heuristic k_eigengap ---------------------------------------------
    # gaps_after[i] = w[i+1] - w[i] (0-indexed), corresponds to 1-indexed gap after λ_{i+1}.
    # Number of communities = i+1 where gap_after[i] is largest (for i ≥ 1 to skip trivial 0).
    # We search i in 1..min(n-1, 20) to find dominant spectral structure.
    gaps_after = [(i + 1, float(w_norm[i + 1] - w_norm[i])) for i in range(1, min(30, N_SURAHS - 1))]
    # k_eigengap = 1-indexed position k s.t. largest gap is AFTER λ_k → k communities
    best_k_eg = max(gaps_after, key=lambda x: x[1])[0]
    k_eigengap = int(best_k_eg)
    # Primary C1 gap: λ_{k+1} − λ_k at LOCKED k=3 (from pre-reg)
    gap_k3 = float(w_norm[3] - w_norm[2])  # 1-indexed: λ_4 - λ_3 = w[3] - w[2] (0-indexed)

    out["eigengap_analysis"] = {
        "gaps_after_lambda_k_1_indexed": {str(k): g for k, g in gaps_after[:15]},
        "k_eigengap": int(k_eigengap),
        "gap_k3_primary_locked": gap_k3,
        "note": "With 25 connected components (21 isolates + 4 non-trivial), λ_1..λ_25 = 0. Locked k=3 gap is structurally degenerate to 0.",
    }

    # -------- MW-5 positive control ---------------------------------------------------
    out["mw5_positive_control"] = mw5_positive_control(np.random.default_rng(SEED + 1))
    mw5_ok = (out["mw5_positive_control"]["gap_k3"] > 0.1 and
              out["mw5_positive_control"]["k_eigengap"] == 3)
    out["mw5_gate_passed"] = bool(mw5_ok)

    # -------- C1 Primary: Spectral gap vs ER null -------------------------------------
    print(f"[C1] Running {N_PERM} ER(n=114, m={E_obs}) draws...")
    t0 = time.time()
    er_gaps = np.zeros(N_PERM)
    rng_c1 = np.random.default_rng(SEED + 100)
    for i in range(N_PERM):
        er_gaps[i], _ = er_null_spectral_gap(N_SURAHS, E_obs, weight_multiset, rng_c1, k_gap=3)
        if (i + 1) % 2000 == 0:
            print(f"  {i+1}/{N_PERM}  elapsed={time.time()-t0:.1f}s")

    er_p = float((1 + (er_gaps >= gap_k3).sum()) / (1 + N_PERM))
    out["C1_primary_ER"] = {
        "observed_gap_k3": gap_k3,
        "null_mean_gap": float(er_gaps.mean()),
        "null_std_gap": float(er_gaps.std()),
        "null_max_gap": float(er_gaps.max()),
        "null_min_gap": float(er_gaps.min()),
        "p_one_sided_upper": er_p,
        "bonferroni_pass": bool(er_p < ALPHA_BON),
    }
    print(f"[C1] observed={gap_k3:.4f} null_mean={er_gaps.mean():.4f} p={er_p:.4g}  pass={er_p < ALPHA_BON}")

    # -------- Secondary nulls: Configuration-model, BA, SBM ----------------------------
    N_AUX = 1000  # smaller (computationally heavier)
    print(f"[aux] {N_AUX} configuration-model swaps...")
    cm_gaps = np.zeros(N_AUX)
    rng_aux1 = np.random.default_rng(SEED + 200)
    for i in range(N_AUX):
        A_cm = configuration_model_rewire(A, rng_aux1, n_swap_mult=5)
        Lc, _ = normalized_laplacian(A_cm)
        wc, _ = spectrum(Lc)
        cm_gaps[i] = wc[3] - wc[2]
    cm_p = float((1 + (cm_gaps >= gap_k3).sum()) / (1 + N_AUX))

    print(f"[aux] {N_AUX} BA null draws...")
    ba_gaps = np.zeros(N_AUX)
    rng_aux2 = np.random.default_rng(SEED + 300)
    for i in range(N_AUX):
        A_ba = barabasi_albert_null(N_SURAHS, E_obs, weight_multiset, rng_aux2)
        Lba, _ = normalized_laplacian(A_ba)
        wba, _ = spectrum(Lba)
        ba_gaps[i] = wba[3] - wba[2]
    ba_p = float((1 + (ba_gaps >= gap_k3).sum()) / (1 + N_AUX))

    print(f"[aux] {N_AUX} SBM null draws (planted 3 blocks)...")
    # Observed edge density ~ E_obs / (114*113/2) ≈ small; SBM p_in/p_out calibrated
    edge_density = E_obs / (N_SURAHS * (N_SURAHS - 1) / 2)
    p_in_sbm = min(0.9, 3 * edge_density)
    p_out_sbm = max(0.001, 0.3 * edge_density)
    sbm_gaps = np.zeros(N_AUX)
    rng_aux3 = np.random.default_rng(SEED + 400)
    for i in range(N_AUX):
        A_sbm, _ = sbm_null(N_SURAHS, [29, 9, 76], p_in_sbm, p_out_sbm, rng_aux3, weight_multiset)
        Ls, _ = normalized_laplacian(A_sbm)
        ws, _ = spectrum(Ls)
        sbm_gaps[i] = ws[3] - ws[2]
    sbm_p = float((1 + (sbm_gaps >= gap_k3).sum()) / (1 + N_AUX))

    out["C1_secondary_nulls"] = {
        "configuration_model": {"n": N_AUX, "mean": float(cm_gaps.mean()), "p_one_sided_upper": cm_p},
        "barabasi_albert": {"n": N_AUX, "mean": float(ba_gaps.mean()), "p_one_sided_upper": ba_p},
        "sbm_planted_3block": {
            "n": N_AUX,
            "block_sizes": [29, 9, 76],
            "p_in": p_in_sbm,
            "p_out": p_out_sbm,
            "mean": float(sbm_gaps.mean()),
            "p_one_sided_upper": sbm_p,
        },
    }
    print(f"[aux] CM p={cm_p:.4g}  BA p={ba_p:.4g}  SBM3 p={sbm_p:.4g}")

    # -------- C2 Secondary: Fiedler sign-partition ------------------------------------
    # Load surah metadata
    with open(REPO / "quran-text/quran-no-tashkeel.json") as f:
        qdata = json.load(f)
    surah_type = {d["id"]: d["type"] for d in qdata}
    surah_verse_count = {d["id"]: d["total_verses"] for d in qdata}

    # Build three binary classifications
    sign_binary = np.array([1 if v_fiedler[s - 1] > 0 else 0 for s in range(1, N_SURAHS + 1)])

    # Meccan=1, Medinan=0
    meccan_binary = np.array([1 if surah_type[s] == "meccan" else 0 for s in range(1, N_SURAHS + 1)])

    # muqaṭṭāʿat = 1
    muq_binary = np.array([1 if s in MUQATTAAT_SURAHS else 0 for s in range(1, N_SURAHS + 1)])

    # long/short median split of verse count
    verse_counts = np.array([surah_verse_count[s] for s in range(1, N_SURAHS + 1)])
    median_vc = float(np.median(verse_counts))
    long_binary = (verse_counts > median_vc).astype(int)

    fiedler_tests = {}
    for name, binary in [("meccan_vs_medinan", meccan_binary),
                         ("muqattaat_vs_not", muq_binary),
                         ("long_vs_short", long_binary)]:
        # 2x2 table
        a = int(((sign_binary == 1) & (binary == 1)).sum())
        b = int(((sign_binary == 1) & (binary == 0)).sum())
        c = int(((sign_binary == 0) & (binary == 1)).sum())
        d_ = int(((sign_binary == 0) & (binary == 0)).sum())
        chi2, p = chi2_2x2(a, b, c, d_)
        fiedler_tests[name] = {
            "table": [[a, b], [c, d_]],
            "chi2": float(chi2),
            "p": float(p),
            "pass": bool(p < ALPHA_BON),
        }

    any_pass = any(t["pass"] for t in fiedler_tests.values())
    out["C2_fiedler_tests"] = fiedler_tests
    out["C2_any_pass"] = bool(any_pass)
    out["C2_bonferroni_pass"] = bool(any_pass)

    # -------- C3 Spectral community detection ------------------------------------------
    # Use eigengap heuristic - k_eigengap is the k where gap between λ_k and λ_{k+1} is max
    # k-means on top-k eigenvectors
    from sklearn.cluster import KMeans
    k_use = k_eigengap
    embed = V_norm[:, :k_use + 1]  # include λ_1=0 eigenvector
    # Row-normalize (Ng-Jordan-Weiss)
    row_norms = np.linalg.norm(embed, axis=1, keepdims=True)
    row_norms[row_norms == 0] = 1
    embed_norm = embed / row_norms
    km = KMeans(n_clusters=k_use, n_init=20, random_state=SEED)
    communities = km.fit_predict(embed_norm)

    # Count community sizes
    from collections import Counter
    comm_counts = Counter(communities.tolist())

    # Identify bridge-surahs: those near boundaries between clusters
    # Use distance to second-nearest centroid / distance to nearest centroid ratio
    distances = km.transform(embed_norm)
    sorted_d = np.sort(distances, axis=1)
    bridge_score = sorted_d[:, 1] / (sorted_d[:, 0] + 1e-12)  # low = ambiguous
    # Lower bridge_score = more bridge-like
    bridge_ranked = sorted(
        [(int(s + 1), float(bridge_score[s]), int(communities[s])) for s in range(N_SURAHS)],
        key=lambda x: x[1],
    )[:15]

    out["C3_communities"] = {
        "k_eigengap": int(k_eigengap),
        "k_used_for_clustering": int(k_use),
        "community_sizes": {str(k): int(v) for k, v in comm_counts.items()},
        "n_communities_with_members": int(len(comm_counts)),
        "assignments": {str(s + 1): int(communities[s]) for s in range(N_SURAHS)},
        "top_15_bridges_low_score": [{"surah": s, "bridge_score": sc, "community": c} for s, sc, c in bridge_ranked],
        "pass_threshold_k_geq_3": bool(k_use >= 3),
    }

    # -------- Q 62 characterization ----------------------------------------------------
    q62_idx = 61  # surah 62 → 0-indexed 61
    q62_v2 = float(v_fiedler[q62_idx])
    q62_v2_rank = int((np.argsort(v_fiedler) == q62_idx).nonzero()[0][0]) + 1  # 1-indexed rank
    # Neighbors of Q 62 in A
    q62_neighbors = [(i + 1, float(A[q62_idx, i])) for i in range(N_SURAHS) if A[q62_idx, i] > 0]
    q62_neighbors_v2 = [(s, w, float(v_fiedler[s - 1])) for s, w in q62_neighbors]
    # Saddle detection: do neighbors span both sign classes?
    nbr_signs = [1 if x[2] > 0 else (-1 if x[2] < 0 else 0) for x in q62_neighbors_v2]
    q62_sign = 1 if q62_v2 > 0 else (-1 if q62_v2 < 0 else 0)
    is_saddle = (1 in nbr_signs) and (-1 in nbr_signs)
    # Is Q 62 extreme in v_2 among its neighbors? (peak)
    nbr_v2_vals = [x[2] for x in q62_neighbors_v2]
    is_peak_pos = q62_v2 > max(nbr_v2_vals) if nbr_v2_vals else False
    is_peak_neg = q62_v2 < min(nbr_v2_vals) if nbr_v2_vals else False

    out["Q62_characterization"] = {
        "v2_value": q62_v2,
        "v2_rank_ascending": q62_v2_rank,
        "v2_sign": q62_sign,
        "community_assignment": int(communities[q62_idx]),
        "weighted_degree": float(d[q62_idx]),
        "neighbors": [{"surah": s, "weight": w, "v2": v2} for s, w, v2 in q62_neighbors_v2],
        "is_saddle_sign_bridge": bool(is_saddle),
        "is_peak_positive": bool(is_peak_pos),
        "is_peak_negative": bool(is_peak_neg),
        "classification": ("saddle" if is_saddle else ("peak" if (is_peak_pos or is_peak_neg) else "neutral")),
    }

    # -------- Final verdict (post-audit-035: Bonferroni-2, C3 descriptive-only) -------
    cells_pass = {
        "C1_spectral_gap_ER": out["C1_primary_ER"]["bonferroni_pass"],
        "C2_fiedler_any_match": out["C2_bonferroni_pass"],
    }
    out["C3_status_post_audit_035"] = "DESCRIPTIVE_ONLY (demoted per audit-035; not Bonferroni-counted)"
    n_pass = sum(cells_pass.values())
    # With k=2: PASS requires both cells, MARGINAL is 1/2, NULL is 0/2
    verdict = "PASS" if n_pass == 2 else ("MARGINAL" if n_pass == 1 else "NULL")

    out["cells_pass"] = cells_pass
    out["n_cells_pass"] = int(n_pass)
    out["verdict"] = verdict
    out["elapsed_seconds"] = round(time.time() - start, 1)

    # Dump JSON
    out_path = REPO / "findings/phase-b-hypotheses/csv/h-new-112.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path}")
    print(f"Elapsed: {out['elapsed_seconds']}s")
    print(f"\nVERDICT: {verdict} ({n_pass}/2 cells; post-audit-035 Bonferroni-2)")
    print(f"  C1 spectral gap ER p={out['C1_primary_ER']['p_one_sided_upper']:.4g} pass={cells_pass['C1_spectral_gap_ER']}")
    print(f"  C2 Fiedler any-match pass={cells_pass['C2_fiedler_any_match']}")
    for name, t in fiedler_tests.items():
        print(f"     - {name}: χ²={t['chi2']:.3f}  p={t['p']:.4g}  pass={t['pass']}")
    print(f"  [DESCRIPTIVE] k_eigengap={k_eigengap} (not Bonferroni-counted)")
    print(f"\nQ 62: v_2={q62_v2:.4f}, rank={q62_v2_rank}/114, community={int(communities[q62_idx])}")
    print(f"      classification: {out['Q62_characterization']['classification']}")
    print(f"\nMW-5 positive control: gate passed = {mw5_ok}")


if __name__ == "__main__":
    main()
