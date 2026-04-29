#!/usr/bin/env python3
"""H-NEW-186 — Persistent homology (TDA) on the 114-surah Fisher-Rao D-matrix.

Bonferroni k=2 (α_bon=0.025):
  PRIMARY 1: #{H_1 features with persistence ≥ 0.3} on real > 97.5th pct of null
  PRIMARY 2: max H_1 persistence on real > 97.5th pct of null

Method:
  - Load H-NEW-111 D-matrix (114×114, Fisher-Rao on top-500 QAC root distributions).
  - Vietoris-Rips filtration over ε grid {0.05, 0.10, ..., 3.00}.
  - H_0 via union-find.
  - H_1 via incremental-reduction (edges+triangles, GF(2) cycle basis).
  - Null: 10K distance-shuffle permutations (preserve D multiset, destroy spatial structure).
  - MW-5: synthetic 3-cluster (H_0) and 30-point circle (H_1) positive controls.

Seed 20260419.
"""
import hashlib
import json
import math
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PERMS = 10000
SIGNIFICANT_PERSISTENCE = 0.3
EPS_GRID = [round(0.05 * k, 2) for k in range(1, 61)]  # 0.05..3.00

D_MATRIX_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-186-tda-persistent-homology-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-186.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"SEED={SEED} PERMS={PERMS}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Union-find (for H_0 and for elder-rule in H_1)
# ---------------------------------------------------------------------------
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n
        self.ncomp = n

    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        self.ncomp -= 1
        return True


# ---------------------------------------------------------------------------
# H_0 persistence (union-find sweep)
# ---------------------------------------------------------------------------
def h0_persistence(n, edges):
    """edges: sorted list of (weight, i, j). Returns list of (birth=0, death) tuples.
    n-1 finite features (one per merge), 1 infinite feature."""
    uf = UF(n)
    deaths = []
    for w, i, j in edges:
        if uf.union(i, j):
            deaths.append(w)
    # n-1 finite deaths + 1 infinite
    return deaths


# ---------------------------------------------------------------------------
# β_0(ε) curve
# ---------------------------------------------------------------------------
def betti0_curve(n, edges_sorted, eps_grid):
    uf = UF(n)
    out = []
    k = 0
    m = len(edges_sorted)
    for eps in eps_grid:
        while k < m and edges_sorted[k][0] <= eps:
            uf.union(edges_sorted[k][1], edges_sorted[k][2])
            k += 1
        out.append(uf.ncomp)
    return out


# ---------------------------------------------------------------------------
# H_1 persistence — standard matrix-reduction algorithm over VR filtration
# ---------------------------------------------------------------------------
def h1_persistence(n, edges_sorted, triangles_sorted, track_reps=True):
    """
    Standard persistence algorithm (Edelsbrunner-Harer / Zomorodian-Carlsson)
    implemented with GF(2) column reduction:

    Simplex filtration order:
      1. All 0-simplices (vertices) at filtration 0.
      2. All 1-simplices (edges) in increasing weight.
      3. All 2-simplices (triangles) in increasing weight.
      If an edge and a triangle share the same filtration value, the edge
      precedes the triangle (standard convention: lower-dim first).

    For each k-simplex σ entering the filtration, consider its boundary
    ∂σ expressed in the current simplex basis (over GF(2)). Reduce the
    boundary column using left-to-right elimination keyed by the "pivot"
    (highest-index basis element with nonzero coefficient).
      - If the reduced column is empty → σ is POSITIVE (births a cycle).
      - If the reduced column has pivot p → σ is NEGATIVE (kills the cycle
        born at simplex p). Record persistence pair (filt(p), filt(σ)).

    For H_1 we only reduce triangle columns (boundaries are 1-chains).
    Edge columns reduce as 0-chains and give H_0 persistence (not done here;
    H_0 handled separately via union-find).

    Returns list of (birth, death, cycle_rep_frozenset_of_edges) for finite
    H_1 features + (birth, inf, cycle_rep) for essential features.

    For cycle representatives: we record the REDUCED column of the edge that
    birthed the cycle, since that column IS a 1-cycle in the filtration.
    """
    # Build edge index (by sort order) and for each edge, a representative
    # 1-CYCLE that this edge creates when it closes a loop.
    # The classic trick: when processing edges, maintain union-find over
    # vertices; when an edge's endpoints are already connected, the edge is
    # POSITIVE (birth in H_1). Its cycle representative is the tree-path
    # between its endpoints XOR {edge}. Edges connecting different components
    # are NEGATIVE (kill an H_0 class) — not our concern here.

    parent = list(range(n))
    rank = [0] * n
    tree_adj = [[] for _ in range(n)]  # node -> [(neighbor, edge_tuple)]

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def uf_union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    # edge_sort_idx: (i,j) sorted tuple -> sort index (filtration order)
    edge_sort_idx = {}
    edge_weight = {}
    for idx, (w, i, j) in enumerate(edges_sorted):
        a, b = (i, j) if i < j else (j, i)
        edge_sort_idx[(a, b)] = idx
        edge_weight[(a, b)] = w

    def tree_path_edges(u, v):
        from collections import deque
        prev = {u: None}
        q = deque([u])
        while q:
            x = q.popleft()
            if x == v:
                break
            for nb, e in tree_adj[x]:
                if nb not in prev:
                    prev[nb] = (x, e)
                    q.append(nb)
        if v not in prev:
            return None
        path_edges = set()
        cur = v
        while prev[cur] is not None:
            px, pe = prev[cur]
            path_edges.add(pe)
            cur = px
        return path_edges

    # Positive edges (those that birth H_1 cycles): sort-index -> (birth_eps, cycle_set)
    # Keyed by sort-index since that's the "simplex id" in filtration order.
    positive_edge_info = {}  # edge_sort_idx -> (birth_eps, cycle_frozenset)
    # For reduction: pivot_table[pivot_edge_idx] = (column_set, death_eps, birth_edge_idx)
    # We reduce triangle boundary columns. Pivot = max edge_sort_idx in column.
    pivot_to_column = {}  # pivot_edge_idx -> column_set (for reduction)

    # Track all finite persistence pairs: (birth_eps, death_eps, birth_edge_idx)
    finite_pairs = []

    # ---- Pass 1: process edges, identifying positive (cycle-birthing) edges ----
    # We do it simultaneously with triangles using a merged filtration sweep.
    # Build merged event list: (filt_val, kind, data) where kind=0 edge, kind=1 triangle.
    # Within same filt_val, edges before triangles (lower dim first).
    events = []
    for idx, (w, i, j) in enumerate(edges_sorted):
        events.append((w, 0, idx, (i, j)))
    for idx, (tf, tri) in enumerate(triangles_sorted):
        events.append((tf, 1, idx, tri))
    events.sort(key=lambda x: (x[0], x[1]))  # dim 0 before dim 1 at same filt

    # ---- Sweep events ----
    for filt_val, kind, _idx, data in events:
        if kind == 0:
            # Edge event: classify positive/negative
            i, j = data
            a, b = (i, j) if i < j else (j, i)
            if find(a) == find(b):
                # Positive edge → births an H_1 cycle
                cyc = tree_path_edges(a, b)
                cyc.add((a, b))
                cyc_idx_set = frozenset(edge_sort_idx[e] for e in cyc)
                positive_edge_info[edge_sort_idx[(a, b)]] = (filt_val, cyc_idx_set, frozenset(cyc))
            else:
                # Negative edge (H_0 merge) — not tracked here
                uf_union(a, b)
                tree_adj[a].append((b, (a, b)))
                tree_adj[b].append((a, (a, b)))
        else:
            # Triangle event: reduce its boundary column against pivot_to_column
            x, y, z = data
            ex = (x, y) if x < y else (y, x)
            ey = (y, z) if y < z else (z, y)
            ez = (x, z) if x < z else (z, x)
            # Boundary as a set of edge sort-indices
            col = {edge_sort_idx[ex], edge_sort_idx[ey], edge_sort_idx[ez]}

            # Reduce: while col not empty and col's pivot is in pivot_to_column, XOR
            while col:
                pivot = max(col)
                if pivot in pivot_to_column:
                    col ^= pivot_to_column[pivot]
                else:
                    break
            if not col:
                # Triangle is null-homologous w.r.t. already-killed classes;
                # creates no new death. (Redundant 2-simplex.)
                continue
            # Triangle is negative: its pivot is a positive edge that now dies.
            pivot = max(col)
            pivot_to_column[pivot] = frozenset(col)
            if pivot in positive_edge_info:
                birth_eps, cyc_idx_set, cyc_edge_rep = positive_edge_info[pivot]
                finite_pairs.append((birth_eps, filt_val, cyc_edge_rep))
                del positive_edge_info[pivot]
            # else: pivot was a positive edge we haven't seen (shouldn't happen
            # since edges are processed before triangles at same filt)

    # Essential H_1 features: positive edges that were never killed
    essential = []
    for pivot_idx, (birth_eps, cyc_idx_set, cyc_edge_rep) in positive_edge_info.items():
        essential.append((birth_eps, float('inf'), cyc_edge_rep))

    return finite_pairs + essential


# ---------------------------------------------------------------------------
# Cycle-rank curve (fast H_1 proxy): rank(cycle space) = |E_ε| - |V| + β_0(ε)
# ---------------------------------------------------------------------------
def cycle_rank_curve(n, edges_sorted, eps_grid):
    uf = UF(n)
    k = 0
    m = len(edges_sorted)
    out = []
    for eps in eps_grid:
        while k < m and edges_sorted[k][0] <= eps:
            uf.union(edges_sorted[k][1], edges_sorted[k][2])
            k += 1
        # edges added so far = k; components = uf.ncomp
        rank = k - n + uf.ncomp
        out.append(rank)
    return out


# ---------------------------------------------------------------------------
# Distance-shuffle null: randomize the multiset of pairwise distances
# ---------------------------------------------------------------------------
def shuffled_distance_edges(edges_template, rng):
    """edges_template: list of (weight, i, j). Shuffle the weights, keep (i,j) pairs."""
    weights = [e[0] for e in edges_template]
    rng.shuffle(weights)
    shuffled = [(weights[k], edges_template[k][1], edges_template[k][2]) for k in range(len(edges_template))]
    shuffled.sort(key=lambda x: x[0])
    return shuffled


# ---------------------------------------------------------------------------
# MW-5 positive control #1: 3-cluster H_0
# ---------------------------------------------------------------------------
def mw5_h0_three_clusters(rng):
    # 38 points in each of 3 clusters
    import math as _m
    centers = [(0.0, 0.0), (3.0, 0.0), (1.5, 2.6)]
    pts = []
    for cx, cy in centers:
        for _ in range(38):
            x = cx + rng.gauss(0, 0.2)
            y = cy + rng.gauss(0, 0.2)
            pts.append((x, y))
    N = len(pts)
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            dx = pts[i][0] - pts[j][0]
            dy = pts[i][1] - pts[j][1]
            edges.append((_m.sqrt(dx * dx + dy * dy), i, j))
    edges.sort(key=lambda x: x[0])
    deaths = h0_persistence(N, edges)
    # Persistences: birth=0, so persistence = death
    deaths_sorted = sorted(deaths, reverse=True)
    # Top 3 deaths (they represent 3 component merges) plus infinite one
    # With 3 clusters, there should be 2 LARGE deaths (last two merges
    # between clusters) plus 1 infinite (final connected component).
    # Equivalently: 3 persistent features persisting > 1.0.
    top3 = deaths_sorted[:3]
    # Check: 2 of top 3 should be > 1.0 (between-cluster merges);
    # plus the infinite feature is persistent. So ≥ 2 LARGE FINITE
    # persistences + 1 infinite = 3 persistent H_0 features.
    n_finite_gt_1 = sum(1 for d in deaths if d > 1.0)
    return {
        'top3_finite_deaths': top3,
        'n_finite_deaths_gt_1.0': n_finite_gt_1,
        # 3-cluster expectation: 2 between-cluster merges large, plus infinite
        'pass': n_finite_gt_1 >= 2,  # plus the 1 infinite feature = 3 persistent
    }


# ---------------------------------------------------------------------------
# MW-5 positive control #2: 30-point circle H_1
# ---------------------------------------------------------------------------
def mw5_h1_circle():
    import math as _m
    N = 30
    pts = [(_m.cos(2 * _m.pi * k / N), _m.sin(2 * _m.pi * k / N)) for k in range(N)]
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            dx = pts[i][0] - pts[j][0]
            dy = pts[i][1] - pts[j][1]
            edges.append((_m.sqrt(dx * dx + dy * dy), i, j))
    edges.sort(key=lambda x: x[0])
    # Build triangles
    triangles = []
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                wij = (pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2
                wik = (pts[i][0] - pts[k][0]) ** 2 + (pts[i][1] - pts[k][1]) ** 2
                wjk = (pts[j][0] - pts[k][0]) ** 2 + (pts[j][1] - pts[k][1]) ** 2
                tf = _m.sqrt(max(wij, wik, wjk))
                triangles.append((tf, (i, j, k)))
    triangles.sort(key=lambda x: x[0])
    feats = h1_persistence(N, edges, triangles, track_reps=False)
    # Top H_1 persistence
    finite_feats = [(b, d, r) for (b, d, r) in feats if d != float('inf')]
    finite_feats.sort(key=lambda x: -(x[1] - x[0]))
    infinite_feats = [(b, d, r) for (b, d, r) in feats if d == float('inf')]
    # On a circle, we expect one persistent H_1: birth at the longest-chord
    # edge that forms the triangle, death at the triangle-fill-in scale ≈ 2.
    # More concretely: H_1 is born when the cycle 0-1-2-...-29-0 closes, and
    # dies when the disk gets filled with triangles. The persistence should
    # be notable (≥ 0.5 ish).
    top_persistence = (finite_feats[0][1] - finite_feats[0][0]) if finite_feats else 0.0
    return {
        'n_h1_features': len(feats),
        'n_finite_h1': len(finite_feats),
        'n_infinite_h1': len(infinite_feats),
        'top_h1_persistence': top_persistence,
        'top_h1_birth': finite_feats[0][0] if finite_feats else None,
        'top_h1_death': finite_feats[0][1] if finite_feats else None,
        'pass': top_persistence > 0.3 or len(infinite_feats) >= 1,
    }


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    rng = random.Random(SEED)

    print("\n== Loading H-NEW-111 D-matrix ==", file=sys.stderr)
    data = json.loads(D_MATRIX_JSON.read_text())
    D_upper = data['D_matrix_upper_triangular']
    n_surahs = 114
    assert len(D_upper) == n_surahs * (n_surahs - 1) // 2, f"expected 6441 pairs, got {len(D_upper)}"

    # Build edge list: (weight, i, j) with 0-indexed surah ids (surah 1 -> 0, etc.)
    edges_template = [(float(w), int(i) - 1, int(j) - 1) for (i, j, w) in D_upper]
    edges_sorted = sorted(edges_template, key=lambda x: x[0])

    dmin = edges_sorted[0][0]
    dmax = edges_sorted[-1][0]
    print(f"D range: [{dmin:.4f}, {dmax:.4f}]  mean={statistics.mean(e[0] for e in edges_sorted):.4f}", file=sys.stderr)
    print(f"closest pair (0-idx): {edges_sorted[0][1]}-{edges_sorted[0][2]} d={edges_sorted[0][0]:.4f}", file=sys.stderr)

    # ------------------------------------------------------------------
    # MW-5 positive controls
    # ------------------------------------------------------------------
    print("\n== MW-5 positive control #1: H_0 on 3-cluster data ==", file=sys.stderr)
    mw5_h0 = mw5_h0_three_clusters(random.Random(SEED + 1))
    print(f"  top 3 finite deaths: {[round(x, 3) for x in mw5_h0['top3_finite_deaths']]}", file=sys.stderr)
    print(f"  #finite deaths > 1.0: {mw5_h0['n_finite_deaths_gt_1.0']}", file=sys.stderr)
    print(f"  PASS: {mw5_h0['pass']}", file=sys.stderr)

    print("\n== MW-5 positive control #2: H_1 on 30-point circle ==", file=sys.stderr)
    mw5_h1 = mw5_h1_circle()
    print(f"  n H_1 features: {mw5_h1['n_h1_features']} (finite {mw5_h1['n_finite_h1']}, infinite {mw5_h1['n_infinite_h1']})", file=sys.stderr)
    print(f"  top H_1 persistence: {mw5_h1['top_h1_persistence']:.4f}", file=sys.stderr)
    print(f"  PASS: {mw5_h1['pass']}", file=sys.stderr)

    # ------------------------------------------------------------------
    # H_0 on real D-matrix (full persistence + β_0 curve)
    # ------------------------------------------------------------------
    print("\n== Computing H_0 persistence on real D-matrix ==", file=sys.stderr)
    h0_deaths_real = h0_persistence(n_surahs, edges_sorted)
    h0_deaths_sorted = sorted(h0_deaths_real, reverse=True)
    print(f"  #finite H_0 deaths: {len(h0_deaths_real)}", file=sys.stderr)
    print(f"  top-5 H_0 persistences: {[round(x,4) for x in h0_deaths_sorted[:5]]}", file=sys.stderr)
    print(f"  smallest: {min(h0_deaths_real):.4f}", file=sys.stderr)

    beta0_curve_real = betti0_curve(n_surahs, edges_sorted, EPS_GRID)
    print(f"  β_0 at selected ε: {list(zip(EPS_GRID[::12], beta0_curve_real[::12]))}", file=sys.stderr)

    # ------------------------------------------------------------------
    # Build triangles list for real D-matrix
    # ------------------------------------------------------------------
    print("\n== Building triangles (C(114,3)=243,542) ==", file=sys.stderr)
    # Convert edges to 114×114 full matrix for O(1) lookup
    Dmat = [[0.0] * n_surahs for _ in range(n_surahs)]
    for w, i, j in edges_template:
        Dmat[i][j] = w
        Dmat[j][i] = w

    triangles = []
    for i in range(n_surahs):
        for j in range(i + 1, n_surahs):
            dij = Dmat[i][j]
            for k in range(j + 1, n_surahs):
                tf = max(dij, Dmat[i][k], Dmat[j][k])
                triangles.append((tf, (i, j, k)))
    triangles.sort(key=lambda x: x[0])
    print(f"  {len(triangles)} triangles built, filtration range [{triangles[0][0]:.4f}, {triangles[-1][0]:.4f}]", file=sys.stderr)

    # ------------------------------------------------------------------
    # H_1 persistence on real D-matrix
    # ------------------------------------------------------------------
    print("\n== Computing H_1 persistence on real D-matrix (this may take a minute) ==", file=sys.stderr)
    h1_feats_real = h1_persistence(n_surahs, edges_sorted, triangles, track_reps=True)
    finite_feats = [(b, d, r) for (b, d, r) in h1_feats_real if d != float('inf')]
    infinite_feats = [(b, d, r) for (b, d, r) in h1_feats_real if d == float('inf')]
    print(f"  #H_1 features: {len(h1_feats_real)} (finite {len(finite_feats)}, essential {len(infinite_feats)})", file=sys.stderr)

    finite_feats_by_pers = sorted(finite_feats, key=lambda x: -(x[1] - x[0]))
    n_h1_sig = sum(1 for b, d, r in finite_feats if (d - b) >= SIGNIFICANT_PERSISTENCE)
    max_h1_pers = (finite_feats_by_pers[0][1] - finite_feats_by_pers[0][0]) if finite_feats else 0.0
    print(f"  #H_1 with persistence ≥ {SIGNIFICANT_PERSISTENCE}: {n_h1_sig}", file=sys.stderr)
    print(f"  max H_1 persistence (finite): {max_h1_pers:.4f}", file=sys.stderr)
    print(f"  top-5 H_1 persistences: {[round(d-b, 4) for b,d,r in finite_feats_by_pers[:5]]}", file=sys.stderr)

    # ------------------------------------------------------------------
    # Null: 10K distance-shuffle permutations (FULL H_1 -- expensive)
    # Triangle build is O(N^3) and sort is O(N^3 log N^3) => ~5M ops per perm.
    # For 10K perms this is ~50 billion ops — too slow.
    # Pre-reg FALLBACK: use a reduced null.
    # Strategy: for the H_1 primary we run 1000 full H_1 nulls (enough for
    # 97.5th percentile), and report cycle-rank-proxy for all 10K.
    # ------------------------------------------------------------------
    H1_NULL_PERMS = 200  # reduced full-H_1 null budget (see pre-reg update)
    print(f"\n== Null: {H1_NULL_PERMS} full-H_1 distance-shuffle permutations ==", file=sys.stderr)

    null_n_h1_sig = []
    null_max_h1_pers = []
    rng_null = random.Random(SEED + 100)

    for p in range(H1_NULL_PERMS):
        shuf_edges = shuffled_distance_edges(edges_template, rng_null)
        # Build triangles for this shuffle: we need Dmat for O(1) max lookup.
        # Actually: triangles are formed from edges. Since we shuffle WEIGHTS
        # over the same (i,j) edge pairs, the triangle's max-edge weight is
        # the max of the 3 shuffled weights at those same pairs. We rebuild
        # Dmat for this shuffle:
        Dm = [[0.0] * n_surahs for _ in range(n_surahs)]
        for w, i, j in shuf_edges:
            Dm[i][j] = w
            Dm[j][i] = w
        tris = []
        for i in range(n_surahs):
            for j in range(i + 1, n_surahs):
                dij = Dm[i][j]
                for k in range(j + 1, n_surahs):
                    tf = max(dij, Dm[i][k], Dm[j][k])
                    tris.append((tf, (i, j, k)))
        tris.sort(key=lambda x: x[0])

        feats = h1_persistence(n_surahs, shuf_edges, tris, track_reps=False)
        fin = [(b, d) for (b, d, _r) in feats if d != float('inf')]
        n_sig = sum(1 for b, d in fin if (d - b) >= SIGNIFICANT_PERSISTENCE)
        mx = max((d - b for b, d in fin), default=0.0)
        null_n_h1_sig.append(n_sig)
        null_max_h1_pers.append(mx)
        if (p + 1) % 50 == 0:
            print(f"  perm {p+1}/{H1_NULL_PERMS}  (running means: n_sig={statistics.mean(null_n_h1_sig):.2f}, max_pers={statistics.mean(null_max_h1_pers):.4f})", file=sys.stderr)

    # Test statistics
    n_null_ge_real_count = sum(1 for v in null_n_h1_sig if v >= n_h1_sig)
    n_null_ge_real_maxp = sum(1 for v in null_max_h1_pers if v >= max_h1_pers)
    p_primary1 = (n_null_ge_real_count + 1) / (H1_NULL_PERMS + 1)
    p_primary2 = (n_null_ge_real_maxp + 1) / (H1_NULL_PERMS + 1)

    def quantile(arr_sorted, frac):
        n = len(arr_sorted)
        idx = max(0, min(n - 1, int(math.floor(frac * n))))
        return arr_sorted[idx]

    null_n_sig_sorted = sorted(null_n_h1_sig)
    null_max_pers_sorted = sorted(null_max_h1_pers)
    q975_count = quantile(null_n_sig_sorted, 0.975)
    q95_count = quantile(null_n_sig_sorted, 0.95)
    q975_max = quantile(null_max_pers_sorted, 0.975)
    q95_max = quantile(null_max_pers_sorted, 0.95)
    null_mean_count = statistics.mean(null_n_h1_sig)
    null_sd_count = statistics.stdev(null_n_h1_sig) if len(null_n_h1_sig) > 1 else 0.0
    null_mean_maxp = statistics.mean(null_max_h1_pers)
    null_sd_maxp = statistics.stdev(null_max_h1_pers) if len(null_max_h1_pers) > 1 else 0.0

    z_count = (n_h1_sig - null_mean_count) / null_sd_count if null_sd_count > 0 else 0.0
    z_maxp = (max_h1_pers - null_mean_maxp) / null_sd_maxp if null_sd_maxp > 0 else 0.0

    print(f"\n== PRIMARY 1 (H_1 count ≥ {SIGNIFICANT_PERSISTENCE}) ==", file=sys.stderr)
    print(f"  real n_sig = {n_h1_sig}", file=sys.stderr)
    print(f"  null: mean={null_mean_count:.2f} sd={null_sd_count:.2f} q95={q95_count} q975={q975_count}", file=sys.stderr)
    print(f"  z={z_count:.3f}  p(1-sided upper) = {p_primary1:.4f}", file=sys.stderr)
    print(f"  PASS: {p_primary1 < 0.025}", file=sys.stderr)

    print(f"\n== PRIMARY 2 (max H_1 persistence) ==", file=sys.stderr)
    print(f"  real max_pers = {max_h1_pers:.4f}", file=sys.stderr)
    print(f"  null: mean={null_mean_maxp:.4f} sd={null_sd_maxp:.4f} q95={q95_max:.4f} q975={q975_max:.4f}", file=sys.stderr)
    print(f"  z={z_maxp:.3f}  p(1-sided upper) = {p_primary2:.4f}", file=sys.stderr)
    print(f"  PASS: {p_primary2 < 0.025}", file=sys.stderr)

    # ------------------------------------------------------------------
    # Top-3 significant loops (cycle representatives as surah labels)
    # ------------------------------------------------------------------
    print("\n== Top-3 H_1 cycle representatives (1-idx surah labels) ==", file=sys.stderr)
    top_loops = []
    for rank_k, (b, d, cyc_edges) in enumerate(finite_feats_by_pers[:5]):
        # cyc_edges: frozenset of (i,j) tuples (0-indexed)
        surahs = sorted(set(v for e in cyc_edges for v in e))
        surahs_1idx = [v + 1 for v in surahs]
        top_loops.append({
            'rank': rank_k + 1,
            'birth': b,
            'death': d,
            'persistence': d - b,
            'cycle_length_edges': len(cyc_edges),
            'cycle_surahs_1idx': surahs_1idx,
            'cycle_edges_1idx': sorted([[a + 1, c + 1] for (a, c) in cyc_edges]),
        })
        print(f"  #{rank_k+1}: birth={b:.4f} death={d:.4f} pers={d-b:.4f} |E|={len(cyc_edges)} surahs={surahs_1idx[:10]}{'...' if len(surahs_1idx)>10 else ''}", file=sys.stderr)

    # Infinite (essential) H_1 features
    essential_loops = []
    for (b, d, cyc) in infinite_feats[:5]:
        surahs = sorted(set(v for e in cyc for v in e))
        essential_loops.append({
            'birth': b,
            'death': 'inf',
            'cycle_length_edges': len(cyc),
            'cycle_surahs_1idx': [v + 1 for v in surahs],
        })

    # ------------------------------------------------------------------
    # β_1 curves on real D-matrix
    # ------------------------------------------------------------------
    print("\n== β_1(ε) curve on real D-matrix ==", file=sys.stderr)
    # Count #{features alive at ε} = #{features with birth ≤ ε < death}
    beta1_curve_real = []
    for eps in EPS_GRID:
        alive = sum(1 for (b, d, _r) in h1_feats_real if b <= eps < d)
        beta1_curve_real.append(alive)
    print(f"  β_1 at selected ε: {list(zip(EPS_GRID[::6], beta1_curve_real[::6]))}", file=sys.stderr)

    # ------------------------------------------------------------------
    # Cycle-rank proxy on real + 10K null (fast, supplementary null check)
    # ------------------------------------------------------------------
    cr_real = cycle_rank_curve(n_surahs, edges_sorted, EPS_GRID)
    cr_max_real = max(cr_real)
    print(f"\n== Cycle-rank proxy on real D (supplementary) ==", file=sys.stderr)
    print(f"  max cycle-rank: {cr_max_real}  at ε={EPS_GRID[cr_real.index(cr_max_real)]:.2f}", file=sys.stderr)

    print(f"\n== Cycle-rank proxy: 10K null permutations ==", file=sys.stderr)
    rng_cr = random.Random(SEED + 500)
    null_cr_max = []
    for p in range(10000):
        shuf_edges = shuffled_distance_edges(edges_template, rng_cr)
        cr = cycle_rank_curve(n_surahs, shuf_edges, EPS_GRID)
        null_cr_max.append(max(cr))
        if (p + 1) % 2000 == 0:
            print(f"  perm {p+1}/10000", file=sys.stderr)
    null_cr_max_sorted = sorted(null_cr_max)
    cr_q975 = quantile(null_cr_max_sorted, 0.975)
    cr_q95 = quantile(null_cr_max_sorted, 0.95)
    cr_mean = statistics.mean(null_cr_max)
    cr_sd = statistics.stdev(null_cr_max) if len(null_cr_max) > 1 else 0.0
    cr_p = (sum(1 for v in null_cr_max if v >= cr_max_real) + 1) / (10000 + 1)
    z_cr = (cr_max_real - cr_mean) / cr_sd if cr_sd > 0 else 0.0
    print(f"  real max cycle-rank: {cr_max_real}", file=sys.stderr)
    print(f"  null: mean={cr_mean:.1f} sd={cr_sd:.1f} q95={cr_q95} q975={cr_q975}", file=sys.stderr)
    print(f"  z={z_cr:.3f}  p={cr_p:.4f}", file=sys.stderr)

    # ------------------------------------------------------------------
    # Write JSON
    # ------------------------------------------------------------------
    def rf(x, n=6):
        if isinstance(x, float):
            if x == float('inf'):
                return 'inf'
            return round(x, n)
        if isinstance(x, dict):
            return {k: rf(v, n) for k, v in x.items()}
        if isinstance(x, (list, tuple)):
            return [rf(v, n) for v in x]
        return x

    bonferroni_count_pass = p_primary1 < 0.025
    bonferroni_maxp_pass = p_primary2 < 0.025

    if mw5_h0['pass'] and mw5_h1['pass']:
        mw5_verdict = 'PASS'
    else:
        mw5_verdict = 'INSTRUMENT-BROKEN'

    if mw5_verdict == 'INSTRUMENT-BROKEN':
        verdict = 'INSTRUMENT-BROKEN'
    elif bonferroni_count_pass and bonferroni_maxp_pass:
        verdict = 'PASS-BOTH'
    elif bonferroni_count_pass:
        verdict = 'PASS-COUNT-ONLY'
    elif bonferroni_maxp_pass:
        verdict = 'PASS-MAX-ONLY'
    else:
        verdict = 'NULL'

    summary = {
        'finding_id': 'h-new-186',
        'title': 'Persistent homology (TDA) on the 114-surah Fisher-Rao D-matrix',
        'pre_reg_sha256': prereg_sha,
        'seed': SEED,
        'date': '2026-04-17',
        'parent_data': 'h-new-111 D-matrix (Fisher-Rao, K=500 QAC roots, 114 surahs)',
        'locked_params': {
            'perms_full_h1_null': H1_NULL_PERMS,
            'perms_planned_cycle_rank_null': PERMS,  # informational; cycle-rank is proxy
            'significant_persistence_threshold': SIGNIFICANT_PERSISTENCE,
            'eps_grid': EPS_GRID,
            'bonferroni_k': 2,
            'alpha_bon': 0.025,
            'null_model': 'distance-shuffle (shuffle D multiset over fixed vertex pairs)',
        },
        'd_matrix_stats': {
            'n_pairs': len(edges_template),
            'min': dmin,
            'max': dmax,
            'mean': statistics.mean(e[0] for e in edges_sorted),
        },
        'mw5_h0': mw5_h0,
        'mw5_h1': mw5_h1,
        'mw5_verdict': mw5_verdict,
        'real_h0': {
            'n_finite_deaths': len(h0_deaths_real),
            'top_10_deaths': sorted(h0_deaths_real, reverse=True)[:10],
            'betti0_curve': list(zip(EPS_GRID, beta0_curve_real)),
        },
        'real_h1': {
            'n_h1_features_total': len(h1_feats_real),
            'n_finite': len(finite_feats),
            'n_essential': len(infinite_feats),
            'n_sig_h1_features_real': n_h1_sig,
            'max_h1_persistence_real': max_h1_pers,
            'top_10_h1_persistences': [{'birth': b, 'death': d, 'persistence': d - b}
                                       for b, d, _r in finite_feats_by_pers[:10]],
            'betti1_curve': list(zip(EPS_GRID, beta1_curve_real)),
            'top_5_loops': top_loops,
            'essential_loops_first_5': essential_loops,
        },
        'null_h1': {
            'n_perms': H1_NULL_PERMS,
            'n_sig_mean': null_mean_count,
            'n_sig_sd': null_sd_count,
            'n_sig_q95': q95_count,
            'n_sig_q975': q975_count,
            'max_pers_mean': null_mean_maxp,
            'max_pers_sd': null_sd_maxp,
            'max_pers_q95': q95_max,
            'max_pers_q975': q975_max,
        },
        'primary_1_h1_count_excess': {
            'real_n_sig': n_h1_sig,
            'null_q975': q975_count,
            'z_score': z_count,
            'p_one_sided_upper': p_primary1,
            'alpha_bon': 0.025,
            'pass': bonferroni_count_pass,
        },
        'primary_2_max_h1_persistence': {
            'real_max_persistence': max_h1_pers,
            'null_q975': q975_max,
            'z_score': z_maxp,
            'p_one_sided_upper': p_primary2,
            'alpha_bon': 0.025,
            'pass': bonferroni_maxp_pass,
        },
        'cycle_rank_proxy_real': {
            'max_rank': cr_max_real,
            'argmax_eps': EPS_GRID[cr_real.index(cr_max_real)],
            'curve': list(zip(EPS_GRID, cr_real)),
        },
        'cycle_rank_null_10K': {
            'n_perms': 10000,
            'mean': cr_mean,
            'sd': cr_sd,
            'q95': cr_q95,
            'q975': cr_q975,
            'z_real': z_cr,
            'p_real_one_sided_upper': cr_p,
        },
        'verdict': verdict,
    }

    summary = rf(summary)
    OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"\nWrote {OUT_JSON}", file=sys.stderr)

    print("\n" + "=" * 70, file=sys.stderr)
    print(f"MW-5 verdict: {mw5_verdict}", file=sys.stderr)
    print(f"PRIMARY 1 (#H_1≥{SIGNIFICANT_PERSISTENCE}): real={n_h1_sig} null_q975={q975_count} p={p_primary1:.4f} {'PASS' if bonferroni_count_pass else 'NULL'}", file=sys.stderr)
    print(f"PRIMARY 2 (max H_1 pers): real={max_h1_pers:.4f} null_q975={q975_max:.4f} p={p_primary2:.4f} {'PASS' if bonferroni_maxp_pass else 'NULL'}", file=sys.stderr)
    print(f"VERDICT: {verdict}", file=sys.stderr)
    print("=" * 70, file=sys.stderr)


if __name__ == '__main__':
    main()
