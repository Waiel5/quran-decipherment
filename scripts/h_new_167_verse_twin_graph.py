#!/usr/bin/env python3
"""H-NEW-167 — Graph-theoretic properties of the verse-twin network.

Builds a top-1 Jaccard (char-trigram) twin graph on 6,236 Quran verses,
symmetrises it, then evaluates:

  1. Power-law fit on degree distribution (Clauset-Shalizi-Newman).
  2. Clustering coefficient vs Erdős-Rényi null (n, m matched).
  3. Small-world ratio σ = (C/C_ER)/(L/L_ER).

Bonferroni-3 family, seed 20260419.

MW-5: synthetic planted-community graph (5 blocks) sanity-check.
"""

from __future__ import annotations

import json
import math
import os
import random
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import networkx as nx

ROOT = Path("/Users/grey/Downloads/quran")
QTEXT = ROOT / "quran-text" / "quran-no-tashkeel.json"
OUT = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-167.json"

SEED = 20260419


# ----------------------------------------------------------------------
# 1. Load verses
# ----------------------------------------------------------------------

def load_verses():
    with QTEXT.open(encoding="utf-8") as f:
        data = json.load(f)
    verses = []
    for s in data:
        sid = s["id"]
        for v in s["verses"]:
            verses.append((sid, v["id"], v["text"]))
    return verses


# ----------------------------------------------------------------------
# 2. Char-trigram sets + top-1 Jaccard
# ----------------------------------------------------------------------

def trigrams(text: str) -> frozenset:
    # whitespace-collapse already done in file; strip just in case
    t = " ".join(text.split())
    if len(t) < 3:
        return frozenset({t}) if t else frozenset()
    return frozenset(t[i:i + 3] for i in range(len(t) - 2))


def build_top1_edges(verses):
    """For each verse, find top-1 Jaccard twin across the corpus.

    Uses an inverted index of trigram → verse-ids to restrict pairwise
    work. For each verse we only compute |A ∩ B| for verses that share
    at least one trigram. Jaccard = |A ∩ B| / (|A| + |B| - |A ∩ B|).
    """
    n = len(verses)
    sets = [trigrams(v[2]) for v in verses]
    sizes = np.array([len(s) for s in sets], dtype=np.int32)

    # Inverted index.
    inv = defaultdict(list)
    for i, s in enumerate(sets):
        for g in s:
            inv[g].append(i)

    # For each verse, count trigram co-occurrences (intersection sizes).
    top1 = np.full(n, -1, dtype=np.int32)
    top1_sim = np.zeros(n, dtype=np.float64)

    for i in range(n):
        A = sets[i]
        if not A:
            continue
        inter = Counter()
        for g in A:
            for j in inv[g]:
                if j != i:
                    inter[j] += 1
        if not inter:
            continue
        best_j = -1
        best_sim = -1.0
        best_key = None
        size_i = sizes[i]
        for j, c in inter.items():
            union = size_i + sizes[j] - c
            if union <= 0:
                continue
            sim = c / union
            # tie-break by lower (surah, ayah) then lower idx
            key_j = (verses[j][0], verses[j][1], j)
            if sim > best_sim or (sim == best_sim and (best_key is None or key_j < best_key)):
                best_sim = sim
                best_j = j
                best_key = key_j
        top1[i] = best_j
        top1_sim[i] = best_sim

        if (i + 1) % 1000 == 0:
            print(f"  top-1 progress: {i+1}/{n}", file=sys.stderr)

    return top1, top1_sim


def build_graph(top1):
    g = nx.Graph()
    n = len(top1)
    g.add_nodes_from(range(n))
    for i, j in enumerate(top1):
        if j >= 0:
            g.add_edge(int(i), int(j))  # simple graph dedupes
    return g


# ----------------------------------------------------------------------
# 3. Power-law fit (Clauset-Shalizi-Newman on discrete data)
# ----------------------------------------------------------------------

def _discrete_pl_mle(ks, kmin):
    # alpha MLE for discrete power law (Clauset et al. 2009 eq A9 approx.)
    ks = np.asarray([k for k in ks if k >= kmin], dtype=np.float64)
    n = len(ks)
    if n < 10 or kmin < 1:
        return float("nan"), float("nan"), n
    # better numerical form: alpha = 1 + n / sum(log(k / (kmin - 0.5)))
    # for kmin = 1 we fall back to continuous approx with shift.
    shift = kmin - 0.5 if kmin > 0.5 else 1e-9
    alpha = 1.0 + n / np.sum(np.log(ks / shift))
    return alpha, shift, n


def _discrete_pl_pmf(k, alpha, kmin, kmax=10_000):
    ks = np.arange(kmin, kmax + 1)
    w = ks.astype(np.float64) ** (-alpha)
    Z = w.sum()
    if k < kmin or k > kmax:
        return 0.0
    return (k ** (-alpha)) / Z


def _discrete_pl_cdf(ks, alpha, kmin, kmax=None):
    if kmax is None:
        kmax = int(max(np.max(ks), kmin)) + 1
    grid = np.arange(kmin, kmax + 1)
    w = grid.astype(np.float64) ** (-alpha)
    Z = w.sum()
    cdf = np.cumsum(w) / Z
    # Lookup
    out = np.zeros_like(ks, dtype=np.float64)
    for i, k in enumerate(ks):
        if k < kmin:
            out[i] = 0.0
        elif k >= kmax:
            out[i] = 1.0
        else:
            out[i] = cdf[int(k) - kmin]
    return out


def powerlaw_fit(degrees):
    """Clauset-Shalizi-Newman: scan k_min, pick one that minimises KS."""
    degs = np.asarray([d for d in degrees if d >= 1], dtype=np.int64)
    if len(degs) < 20:
        return dict(ok=False, reason="too few nonzero degrees")

    best = None
    kmin_candidates = list(range(1, max(2, int(np.percentile(degs, 95)))))
    for kmin in kmin_candidates:
        tail = degs[degs >= kmin]
        if len(tail) < 20:
            continue
        alpha, shift, n = _discrete_pl_mle(tail, kmin)
        if not math.isfinite(alpha) or alpha <= 1:
            continue
        # Empirical CDF of tail
        sorted_tail = np.sort(tail)
        emp_cdf = np.arange(1, len(sorted_tail) + 1) / len(sorted_tail)
        the_cdf = _discrete_pl_cdf(sorted_tail, alpha, kmin)
        ks = np.max(np.abs(emp_cdf - the_cdf))
        if best is None or ks < best["ks"]:
            best = dict(kmin=int(kmin), alpha=float(alpha), ks=float(ks),
                        n_tail=int(len(tail)))

    if best is None:
        return dict(ok=False, reason="no valid kmin")

    # Bootstrap KS p-value by sampling synthetic power-law + noise (semi-
    # parametric CSN). We resample |tail| points from the fitted discrete PL
    # and recompute KS; fraction with KS >= observed = p-value.
    rng = np.random.default_rng(SEED)
    kmin = best["kmin"]
    alpha = best["alpha"]
    n_tail = best["n_tail"]
    # precompute CDF for sampling
    kmax = max(int(degs.max()) * 2, kmin + 50)
    grid = np.arange(kmin, kmax + 1)
    w = grid.astype(np.float64) ** (-alpha)
    Z = w.sum()
    pmf = w / Z
    cdf = np.cumsum(pmf)

    n_boot = 500
    ks_null = []
    for _ in range(n_boot):
        u = rng.random(n_tail)
        sample = grid[np.searchsorted(cdf, u)]
        a_b, _, _ = _discrete_pl_mle(sample, kmin)
        if not math.isfinite(a_b) or a_b <= 1:
            continue
        s_sort = np.sort(sample)
        emp = np.arange(1, len(s_sort) + 1) / len(s_sort)
        the = _discrete_pl_cdf(s_sort, a_b, kmin, kmax=kmax)
        ks_null.append(np.max(np.abs(emp - the)))
    ks_null = np.asarray(ks_null)
    p_value = float(np.mean(ks_null >= best["ks"])) if len(ks_null) else float("nan")
    best["ks_bootstrap_p"] = p_value
    best["ok"] = True
    return best


# ----------------------------------------------------------------------
# 4. Clustering, path-length, small-world, ER null
# ----------------------------------------------------------------------

def er_null_stats(n, m, k_reps=50, rng=None):
    rng = rng or np.random.default_rng(SEED)
    C_list = []
    L_list = []
    for _ in range(k_reps):
        seed = int(rng.integers(0, 2**31 - 1))
        g = nx.gnm_random_graph(n, m, seed=seed)
        C_list.append(nx.average_clustering(g))
        # mean shortest-path on largest CC
        cc = max(nx.connected_components(g), key=len)
        sub = g.subgraph(cc).copy()
        # sample path-length for speed if large
        L_list.append(_mean_shortest_path(sub))
    return np.asarray(C_list), np.asarray(L_list)


def _mean_shortest_path(g, sample=200, rng=None):
    n = g.number_of_nodes()
    if n <= sample:
        return nx.average_shortest_path_length(g)
    rng = rng or np.random.default_rng(SEED)
    nodes = list(g.nodes())
    pick = rng.choice(len(nodes), size=sample, replace=False)
    totals = []
    counts = []
    for idx in pick:
        src = nodes[int(idx)]
        lengths = nx.single_source_shortest_path_length(g, src)
        # exclude self
        vals = [v for k, v in lengths.items() if k != src]
        if vals:
            totals.append(sum(vals))
            counts.append(len(vals))
    return sum(totals) / sum(counts)


# ----------------------------------------------------------------------
# 5. Mechanical witness MW-5: planted-community graph
# ----------------------------------------------------------------------

def planted_community_graph(n_blocks=5, block_size=1000, p_in=0.01, p_out=0.0005, seed=42):
    rng = np.random.default_rng(seed)
    N = n_blocks * block_size
    g = nx.Graph()
    g.add_nodes_from(range(N))
    # intra-block
    for b in range(n_blocks):
        start = b * block_size
        for i in range(start, start + block_size):
            for j in range(i + 1, start + block_size):
                if rng.random() < p_in:
                    g.add_edge(i, j)
    # inter-block
    for b1 in range(n_blocks):
        for b2 in range(b1 + 1, n_blocks):
            s1 = b1 * block_size
            s2 = b2 * block_size
            for i in range(s1, s1 + block_size):
                for j in range(s2, s2 + block_size):
                    if rng.random() < p_out:
                        g.add_edge(i, j)
    return g


# ----------------------------------------------------------------------
# 6. Main run
# ----------------------------------------------------------------------

def analyse_graph(g, label, verses=None, n_er=50):
    result = {"label": label}
    n = g.number_of_nodes()
    m = g.number_of_edges()
    result["n_nodes"] = n
    result["n_edges"] = m

    degs = np.asarray([d for _, d in g.degree()], dtype=np.int64)
    result["mean_degree"] = float(degs.mean())
    result["median_degree"] = float(np.median(degs))
    result["max_degree"] = int(degs.max())
    result["n_isolates"] = int(np.sum(degs == 0))

    # Component stats
    ccs = list(nx.connected_components(g))
    sizes = sorted((len(c) for c in ccs), reverse=True)
    result["n_components"] = len(ccs)
    result["largest_component_size"] = sizes[0] if sizes else 0
    result["component_size_hist"] = dict(Counter(sizes))

    # Clustering
    C_obs = nx.average_clustering(g)
    result["avg_clustering"] = float(C_obs)

    # Mean shortest-path on largest CC
    lcc_nodes = max(ccs, key=len) if ccs else set()
    lcc = g.subgraph(lcc_nodes).copy()
    L_obs = _mean_shortest_path(lcc) if lcc.number_of_nodes() > 1 else float("nan")
    result["mean_shortest_path_lcc"] = float(L_obs)

    # Assortativity
    try:
        result["degree_assortativity"] = float(nx.degree_assortativity_coefficient(g))
    except Exception as e:
        result["degree_assortativity"] = None
        result["assortativity_error"] = str(e)

    # Power-law fit (undirected degree dist)
    pl = powerlaw_fit(degs)
    result["powerlaw"] = pl

    # ER null stats
    t0 = time.time()
    C_er, L_er = er_null_stats(n, m, k_reps=n_er, rng=np.random.default_rng(SEED + hash(label) % 1000))
    result["er_mean_clustering"] = float(C_er.mean())
    result["er_std_clustering"] = float(C_er.std())
    result["er_mean_path_length"] = float(L_er.mean())
    result["er_std_path_length"] = float(L_er.std())
    result["er_time_sec"] = time.time() - t0
    result["er_n_reps"] = int(n_er)

    # Clustering test (one-sided p = fraction of ER reps with C_er >= C_obs)
    result["clustering_p_one_sided"] = float(np.mean(C_er >= C_obs))

    # Small-world ratio
    if L_obs > 0 and C_er.mean() > 0 and L_er.mean() > 0:
        sigma = (C_obs / C_er.mean()) / (L_obs / L_er.mean())
    else:
        sigma = float("nan")
    result["small_world_sigma"] = float(sigma)

    # Pass/fail
    alpha = 0.0167
    pl_pass = bool(pl.get("ok") and pl.get("ks_bootstrap_p", 0) > alpha and 1.5 < pl.get("alpha", 0) < 4)
    clust_pass = bool(result["clustering_p_one_sided"] < alpha)
    sw_pass = bool(sigma >= 2)
    result["pl_pass"] = pl_pass
    result["clustering_pass"] = clust_pass
    result["small_world_pass"] = sw_pass

    # Top-10 hubs
    if verses is not None:
        top = sorted(g.degree(), key=lambda x: (-x[1], x[0]))[:10]
        result["top10_hubs"] = [
            dict(idx=int(i), surah=verses[i][0], ayah=verses[i][1], degree=int(d),
                 text_preview=verses[i][2][:80])
            for i, d in top
        ]

    return result


def main():
    random.seed(SEED)
    np.random.seed(SEED)

    print("[1/4] Loading verses…", file=sys.stderr)
    verses = load_verses()
    n_total = len(verses)
    assert n_total == 6236, f"Expected 6236 verses, got {n_total}"
    print(f"  loaded {n_total} verses", file=sys.stderr)

    print("[2/4] Building top-1 Jaccard twin edges…", file=sys.stderr)
    t0 = time.time()
    top1, top1_sim = build_top1_edges(verses)
    print(f"  done in {time.time() - t0:.1f}s", file=sys.stderr)
    print(f"  median sim = {np.median(top1_sim):.3f}, "
          f"min = {top1_sim.min():.3f}, "
          f"max = {top1_sim.max():.3f}", file=sys.stderr)

    g = build_graph(top1)
    print(f"  graph: {g.number_of_nodes()} nodes, {g.number_of_edges()} edges",
          file=sys.stderr)

    print("[3/4] Analysing observed graph + ER null…", file=sys.stderr)
    obs = analyse_graph(g, label="observed", verses=verses, n_er=50)
    print(f"  clustering_obs={obs['avg_clustering']:.4f}, "
          f"L_obs={obs['mean_shortest_path_lcc']:.3f}, "
          f"σ={obs['small_world_sigma']:.3f}", file=sys.stderr)

    print("[4/4] MW-5: planted-community graph…", file=sys.stderr)
    mw_g = planted_community_graph(n_blocks=5, block_size=1000,
                                   p_in=0.01, p_out=0.0005, seed=SEED + 1)
    mw = analyse_graph(mw_g, label="mw5_planted_community", verses=None, n_er=20)

    out = dict(
        hypothesis="H-NEW-167",
        seed=SEED,
        rules_tuple="(no-tashkeel; whitespace-collapsed; basmala-only-in-Q1)",
        method="top-1 char-trigram Jaccard, symmetrised OR, undirected simple graph",
        observed=obs,
        mechanical_witness=mw,
        prereg="findings/phase-b-hypotheses/h-new-167-verse-twin-graph-prereg.md",
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2, default=str)
    print(f"wrote {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
