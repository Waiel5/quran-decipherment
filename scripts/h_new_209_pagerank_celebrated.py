#!/usr/bin/env python3
"""H-NEW-209 — PageRank verse-twin hubs cross-referenced with classical celebrated verses.

Reconstructs the verse-twin graph (top-1 char-trigram Jaccard, symmetrised)
per H-NEW-167, computes PageRank on the undirected graph, extracts the
top-50 verses by PageRank, and tests whether the intersection with a
pre-registered list of classical celebrated verses exceeds chance.

Celebrated verse set (union, deduplicated):
  - Q 1:1   basmala
  - Q 1:1-7 al-Fatiha (7 verses)
  - Q 2:255 ayat al-kursi
  - Q 24:35 ayat al-nur
  - Q 59:22-24 (3 verses, khawatim al-Hashr)
  - Q 112:1-4 (al-Ikhlas, 4 verses)
  - Mu'awwidhatan: Q 113:1-5 (5 verses), Q 114:1-6 (6 verses)

Pre-registered alpha = 0.05, Bonferroni_k = 1 (single outer test).
Seed = 20260419.

The null hypothesis is: "top-50 PageRank verses are no more enriched in
celebrated-verses than a random set of 50 verses from the 6236 corpus."
Two independent p-values reported:
  (a) hypergeometric exact test
  (b) 10,000-iteration permutation test (seed 20260419)

Outputs: findings/phase-b-hypotheses/csv/h-new-209.json (main result)
         findings/phase-b-hypotheses/csv/h-new-209-top50.csv (top-50 verses)
"""

from __future__ import annotations

import csv
import json
import math
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import networkx as nx

ROOT = Path("/Users/grey/Downloads/quran")
QTEXT = ROOT / "quran-text" / "quran-no-tashkeel.json"
OUTDIR = ROOT / "findings" / "phase-b-hypotheses" / "csv"
OUT_JSON = OUTDIR / "h-new-209.json"
OUT_TOP50 = OUTDIR / "h-new-209-top50.csv"

SEED = 20260419
N_PERM = 10000
TOP_K = 50
ALPHA = 0.05
BONFERRONI_K = 1


# ----------------------------------------------------------------------
# Classical celebrated verse set (pre-registered)
# ----------------------------------------------------------------------
def celebrated_verses():
    s = set()
    # Q 1:1 basmala is Q 1:1; al-Fatiha full = Q 1:1..1:7
    for a in range(1, 8):
        s.add((1, a))
    # Q 2:255 ayat al-kursi
    s.add((2, 255))
    # Q 24:35 ayat al-nur
    s.add((24, 35))
    # Q 59:22-24 khawatim al-Hashr
    for a in (22, 23, 24):
        s.add((59, a))
    # Q 112:1-4 al-Ikhlas
    for a in range(1, 5):
        s.add((112, a))
    # Q 113:1-5 al-Falaq (first of mu'awwidhatan)
    for a in range(1, 6):
        s.add((113, a))
    # Q 114:1-6 al-Nas (second of mu'awwidhatan)
    for a in range(1, 7):
        s.add((114, a))
    return s


# ----------------------------------------------------------------------
# Load verses
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
# Top-1 Jaccard twin graph (identical to H-NEW-167)
# ----------------------------------------------------------------------
def trigrams(text: str) -> frozenset:
    t = " ".join(text.split())
    if len(t) < 3:
        return frozenset({t}) if t else frozenset()
    return frozenset(t[i:i + 3] for i in range(len(t) - 2))


def build_top1(verses):
    n = len(verses)
    sets = [trigrams(v[2]) for v in verses]
    sizes = np.array([len(s) for s in sets], dtype=np.int32)
    inv = defaultdict(list)
    for i, s in enumerate(sets):
        for g in s:
            inv[g].append(i)
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
            key_j = (verses[j][0], verses[j][1], j)
            if sim > best_sim or (sim == best_sim and (best_key is None or key_j < best_key)):
                best_sim = sim
                best_j = j
                best_key = key_j
        top1[i] = best_j
        top1_sim[i] = best_sim
        if (i + 1) % 1000 == 0:
            print(f"  top1 progress: {i+1}/{n}", file=sys.stderr)
    return top1, top1_sim


def build_graph(top1):
    g = nx.Graph()
    n = len(top1)
    g.add_nodes_from(range(n))
    for i, j in enumerate(top1):
        if j >= 0:
            g.add_edge(int(i), int(j))
    return g


# ----------------------------------------------------------------------
# Hypergeometric p-value (one-sided, P(X >= k))
# ----------------------------------------------------------------------
def hypergeom_sf(k, N, K, n):
    """P(X >= k) where X ~ Hypergeom(N, K, n).
    N = pop size, K = pop successes, n = sample size, k = observed successes.
    """
    # exact sum of PMF
    from math import comb
    total = comb(N, n)
    if total == 0:
        return float("nan")
    p = 0.0
    kmin = k
    kmax = min(K, n)
    for x in range(kmin, kmax + 1):
        p += comb(K, x) * comb(N - K, n - x) / total
    return p


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    rng = np.random.default_rng(SEED)

    print("[1/5] Loading verses…", file=sys.stderr)
    verses = load_verses()
    assert len(verses) == 6236, f"expected 6236 verses, got {len(verses)}"
    idx_by_sa = {(s, a): i for i, (s, a, _t) in enumerate(verses)}

    cset = celebrated_verses()
    # Filter to ones present in corpus (all should be)
    cset_idx = {idx_by_sa[sa] for sa in cset if sa in idx_by_sa}
    K_celeb = len(cset_idx)
    print(f"  celebrated set: {K_celeb} verses (pre-registered union)", file=sys.stderr)

    print("[2/5] Building top-1 Jaccard twin graph…", file=sys.stderr)
    t0 = time.time()
    top1, top1_sim = build_top1(verses)
    print(f"  done in {time.time() - t0:.1f}s", file=sys.stderr)
    g = build_graph(top1)
    n_nodes = g.number_of_nodes()
    n_edges = g.number_of_edges()
    print(f"  graph: {n_nodes} nodes, {n_edges} edges", file=sys.stderr)

    print("[3/5] Computing PageRank…", file=sys.stderr)
    # PageRank on undirected (NetworkX treats undirected as bidirectional)
    pr = nx.pagerank(g, alpha=0.85, max_iter=500, tol=1.0e-10)
    # Rank: descending PR, tie-break by (surah, ayah)
    ranked = sorted(
        pr.items(),
        key=lambda kv: (-kv[1], verses[kv[0]][0], verses[kv[0]][1])
    )
    top_idx = [i for i, _ in ranked[:TOP_K]]
    top_set = set(top_idx)

    # Intersection
    hits_idx = sorted(top_set & cset_idx)
    k_hits = len(hits_idx)
    print(f"  top-{TOP_K} PageRank ∩ celebrated = {k_hits}", file=sys.stderr)

    # ------------------------------------------------------------------
    # Null 1: hypergeometric
    # ------------------------------------------------------------------
    N = n_nodes
    p_hyper = hypergeom_sf(k_hits, N, K_celeb, TOP_K)
    expected = TOP_K * K_celeb / N
    print(f"  expected under uniform = {expected:.3f}, "
          f"hypergeom P(X>={k_hits}) = {p_hyper:.4g}", file=sys.stderr)

    # ------------------------------------------------------------------
    # Null 2: permutation — random 50-subsets of {0..N-1}
    # ------------------------------------------------------------------
    print(f"[4/5] Permutation test ({N_PERM} iters, seed {SEED})…", file=sys.stderr)
    rng_perm = np.random.default_rng(SEED)
    all_idx = np.arange(N)
    ge_count = 0
    null_hits = np.zeros(N_PERM, dtype=np.int32)
    cset_arr = np.zeros(N, dtype=bool)
    for ci in cset_idx:
        cset_arr[ci] = True
    for t in range(N_PERM):
        samp = rng_perm.choice(N, size=TOP_K, replace=False)
        h = int(cset_arr[samp].sum())
        null_hits[t] = h
        if h >= k_hits:
            ge_count += 1
    p_perm = (ge_count + 1) / (N_PERM + 1)  # add-one smoothing

    # ------------------------------------------------------------------
    # Decision
    # ------------------------------------------------------------------
    alpha_corr = ALPHA / BONFERRONI_K
    pass_hyper = bool(p_hyper < alpha_corr)
    pass_perm = bool(p_perm < alpha_corr)

    # ------------------------------------------------------------------
    # Write top-50 table
    # ------------------------------------------------------------------
    print("[5/5] Writing outputs…", file=sys.stderr)
    OUTDIR.mkdir(parents=True, exist_ok=True)
    with OUT_TOP50.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "surah", "ayah", "idx", "pagerank",
                    "degree", "celebrated", "text_preview"])
        for rank, (i, p) in enumerate(ranked[:TOP_K], 1):
            s, a, t = verses[i]
            w.writerow([rank, s, a, i, f"{p:.8f}", g.degree(i),
                        int(i in cset_idx), t[:100]])

    out = dict(
        hypothesis="H-NEW-209",
        title="PageRank verse-twin hubs vs classical celebrated verses",
        seed=SEED,
        alpha=ALPHA,
        bonferroni_k=BONFERRONI_K,
        alpha_corrected=alpha_corr,
        method=(
            "Reconstruct H-NEW-167 top-1 Jaccard char-trigram verse-twin graph; "
            "symmetrise (undirected); compute NetworkX PageRank (alpha=0.85, "
            "tol=1e-10); take top-50 by PageRank, tie-break (surah, ayah); "
            "test intersection with pre-registered celebrated set against "
            "hypergeometric null and 10,000-iter permutation null."
        ),
        rules_tuple="(no-tashkeel; whitespace-collapsed; basmala-only-in-Q1)",
        graph=dict(
            n_nodes=n_nodes,
            n_edges=n_edges,
            n_components=nx.number_connected_components(g),
        ),
        celebrated_set=dict(
            spec=(
                "Q1:1-7 (al-Fatiha incl. basmala), Q2:255 (kursi), Q24:35 (nur), "
                "Q59:22-24 (khawatim Hashr), Q112:1-4 (Ikhlas), "
                "Q113:1-5 (Falaq), Q114:1-6 (Nas)"
            ),
            size=K_celeb,
            members=sorted(cset),
        ),
        result=dict(
            top_k=TOP_K,
            hits=k_hits,
            hits_detail=[
                dict(surah=verses[i][0], ayah=verses[i][1],
                     pagerank=float(pr[i]), degree=int(g.degree(i)),
                     text_preview=verses[i][2][:100])
                for i in hits_idx
            ],
            expected_under_uniform=expected,
            p_hypergeom=p_hyper,
            p_permutation=p_perm,
            permutation_null_mean=float(null_hits.mean()),
            permutation_null_std=float(null_hits.std()),
            permutation_null_max=int(null_hits.max()),
            n_perm=N_PERM,
        ),
        decision=dict(
            exceeds_chance_hypergeom=pass_hyper,
            exceeds_chance_permutation=pass_perm,
            verdict=(
                "PASS" if (pass_hyper and pass_perm) else
                ("MIXED" if (pass_hyper or pass_perm) else "FAIL")
            ),
        ),
        top10_pagerank=[
            dict(rank=r+1, surah=verses[i][0], ayah=verses[i][1],
                 pagerank=float(p), degree=int(g.degree(i)),
                 celebrated=bool(i in cset_idx),
                 text_preview=verses[i][2][:100])
            for r, (i, p) in enumerate(ranked[:10])
        ],
    )
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2, default=str)
    print(f"wrote {OUT_JSON}", file=sys.stderr)
    print(f"wrote {OUT_TOP50}", file=sys.stderr)
    print(f"\nVERDICT: {out['decision']['verdict']}", file=sys.stderr)
    print(f"  hits={k_hits}/{TOP_K}, expected={expected:.2f}", file=sys.stderr)
    print(f"  p_hyper={p_hyper:.4g}, p_perm={p_perm:.4g}, alpha_corr={alpha_corr}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
