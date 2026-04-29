#!/usr/bin/env python3
"""H-NEW-201 — PageRank on the verse-twin similarity graph (downstream of H-NEW-167).

Builds a top-K=5 directed weighted graph on 6,236 Quran verses where
edge weight = char-trigram Jaccard similarity. Runs PageRank for
exactly 100 iterations (damping 0.85). Reports top-10, compares
against classical-top-100, and tests the al-Fātiḥa 7-verse PageRank
sum vs random 7-verse bundles (Bonferroni k=2).

Pre-reg: findings/phase-b-hypotheses/h-new-201-pagerank-verse-twin-prereg.md
Seed: 20260419.
"""

from __future__ import annotations

import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

ROOT = Path("/Users/grey/Downloads/quran")
QTEXT = ROOT / "quran-text" / "quran-no-tashkeel.json"
TOP100_MD = ROOT / "findings" / "verse-commentaries-top100.md"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-201.json"
OUT_MD = ROOT / "findings" / "phase-b-hypotheses" / "h-new-201-pagerank-verse-twin.md"

SEED = 20260419
TOP_K = 5
DAMPING = 0.85
N_ITER = 100
N_BOOT_BUNDLES = 10_000
BONFERRONI_K = 2
ALPHA_FAMILY = 0.05
ALPHA_TEST = ALPHA_FAMILY / BONFERRONI_K  # 0.025


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
# 2. Char-trigram sets + top-K Jaccard
# ----------------------------------------------------------------------

def trigrams(text: str) -> frozenset:
    t = " ".join(text.split())
    if len(t) < 3:
        return frozenset({t}) if t else frozenset()
    return frozenset(t[i:i + 3] for i in range(len(t) - 2))


def build_topk_edges(verses, k=TOP_K):
    """For each verse, find top-K Jaccard neighbours across the corpus.

    Returns (neighbours, sims) each shape (N, k) with -1 / 0.0 padding.
    """
    n = len(verses)
    sets = [trigrams(v[2]) for v in verses]
    sizes = np.array([len(s) for s in sets], dtype=np.int32)

    inv = defaultdict(list)
    for i, s in enumerate(sets):
        for g in s:
            inv[g].append(i)

    neigh = np.full((n, k), -1, dtype=np.int32)
    sims = np.zeros((n, k), dtype=np.float64)

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
        size_i = sizes[i]
        # Compute Jaccard for all candidates; keep top-k
        items = []
        for j, c in inter.items():
            union = size_i + sizes[j] - c
            if union <= 0:
                continue
            sim = c / union
            # tie-break: higher sim first; then lower (surah, ayah, idx)
            key_j = (verses[j][0], verses[j][1], j)
            items.append((sim, key_j, j))
        if not items:
            continue
        # sort by (-sim, key_j); pick first k
        items.sort(key=lambda x: (-x[0], x[1]))
        for rank, (sim, _, j) in enumerate(items[:k]):
            neigh[i, rank] = j
            sims[i, rank] = sim

        if (i + 1) % 1000 == 0:
            print(f"  top-{k} progress: {i+1}/{n}", file=sys.stderr)

    return neigh, sims


# ----------------------------------------------------------------------
# 3. PageRank (weighted directed, 100 iterations, no early stop)
# ----------------------------------------------------------------------

def pagerank_topk(neigh, sims, damping=DAMPING, n_iter=N_ITER):
    """Power-iteration PageRank on a top-K weighted directed graph.

    - Each row i of neigh gives up to K out-neighbours with weights sims[i,:].
    - Weights normalised per source node before the step.
    - Dangling nodes (sum weight 0) redistribute mass uniformly.
    - Personalisation uniform.
    - Exactly n_iter iterations; convergence trace recorded at 10/50/100.
    """
    N = neigh.shape[0]
    K = neigh.shape[1]

    # Normalise weights per row; build compact COO arrays
    row_sum = sims.sum(axis=1)  # (N,)
    is_dangling = row_sum <= 0
    # Avoid div by zero
    safe_row = np.where(is_dangling, 1.0, row_sum)
    normed = sims / safe_row[:, None]   # rows of dangling verses are zero
    # Columns = neighbour idx
    # We vectorise with np.add.at per iteration.

    p = np.full(N, 1.0 / N, dtype=np.float64)
    teleport = np.full(N, (1.0 - damping) / N, dtype=np.float64)

    trace = {}
    for t in range(1, n_iter + 1):
        # Dangling mass redistribute uniformly
        dangling_mass = float(p[is_dangling].sum())
        base = teleport + damping * dangling_mass / N   # (N,)

        new_p = np.copy(base)
        # Contribution from non-dangling:
        # for each i not dangling, for k in range(K):
        #    if neigh[i,k] >= 0:
        #        new_p[neigh[i,k]] += damping * p[i] * normed[i,k]
        # Vectorised:
        contrib_src = (damping * p)[:, None] * normed  # (N, K)
        # Mask invalid
        valid = neigh >= 0
        flat_idx = neigh[valid]
        flat_val = contrib_src[valid]
        np.add.at(new_p, flat_idx, flat_val)

        # sanity: total mass should be ~ 1
        # (teleport sum = 1 - damping; dangling contributes damping * dang_mass;
        #  non-dangling contribute damping * (1 - dang_mass))
        if t in (10, 50, 100):
            l1 = float(np.abs(new_p - p).sum())
            trace[t] = dict(l1_change=l1, total_mass=float(new_p.sum()))

        p = new_p

    return p, trace


# ----------------------------------------------------------------------
# 4. Classical-top-100 loader
# ----------------------------------------------------------------------

def load_classical_top100():
    """Parse verse-commentaries-top100.md headings for (surah, ayah) refs."""
    pat = re.compile(r"^### (\d+):(\d+)\s")
    refs = []
    seen = set()
    if not TOP100_MD.exists():
        return refs, False
    with TOP100_MD.open(encoding="utf-8") as f:
        for line in f:
            m = pat.match(line)
            if m:
                s = int(m.group(1))
                a = int(m.group(2))
                key = (s, a)
                if key not in seen:
                    seen.add(key)
                    refs.append(key)
    return refs, True


# ----------------------------------------------------------------------
# 5. Main
# ----------------------------------------------------------------------

def main():
    np.random.seed(SEED)

    print("[1/5] Loading verses…", file=sys.stderr)
    verses = load_verses()
    N = len(verses)
    assert N == 6236, f"Expected 6236 verses, got {N}"

    # Index lookup for (surah, ayah) → verse-idx
    idx_of = {(s, a): i for i, (s, a, _) in enumerate(verses)}

    print(f"[2/5] Building top-{TOP_K} Jaccard edges…", file=sys.stderr)
    t0 = time.time()
    neigh, sims = build_topk_edges(verses, k=TOP_K)
    print(f"  done in {time.time() - t0:.1f}s", file=sys.stderr)

    # Edge count (directed, non -1)
    n_edges = int((neigh >= 0).sum())
    # Dangling nodes
    row_sum = sims.sum(axis=1)
    n_dangling = int((row_sum <= 0).sum())

    print(f"  directed edges: {n_edges}, dangling: {n_dangling}",
          file=sys.stderr)
    print(f"  mean top-1 sim: {sims[:,0].mean():.4f}, "
          f"mean top-5 sim: {sims[:,4].mean():.4f}",
          file=sys.stderr)

    print(f"[3/5] Running PageRank ({N_ITER} iters, α={DAMPING})…", file=sys.stderr)
    t0 = time.time()
    pr, trace = pagerank_topk(neigh, sims, damping=DAMPING, n_iter=N_ITER)
    print(f"  done in {time.time() - t0:.2f}s", file=sys.stderr)
    print(f"  convergence trace: {trace}", file=sys.stderr)

    # Top-20 by PageRank
    order = np.argsort(-pr)
    top20 = []
    for rank, i in enumerate(order[:20], 1):
        s, a, text = verses[int(i)]
        top20.append(dict(
            rank=rank, idx=int(i), surah=s, ayah=a,
            pagerank=float(pr[i]),
            text_preview=text[:80],
        ))

    # Top-10 (just take first 10 of top20)
    top10 = top20[:10]

    print(f"[4/5] T1 — classical-top-100 overlap…", file=sys.stderr)
    classical, loaded = load_classical_top100()
    if not loaded:
        t1_result = dict(
            test="T1_classical_celebration_top10",
            status="DESCRIPTIVE_downgraded",
            reason="verse-commentaries-top100.md not found",
        )
    else:
        top10_refs = [(v["surah"], v["ayah"]) for v in top10]
        classical_set = set(classical)
        hits = [ref for ref in top10_refs if ref in classical_set]
        # Binomial one-sided under null p = len(classical)/N
        p_null = len(classical) / N
        from math import comb
        n_hits = len(hits)
        p_value = 0.0
        for k in range(n_hits, 11):
            p_value += comb(10, k) * (p_null ** k) * ((1 - p_null) ** (10 - k))
        t1_result = dict(
            test="T1_classical_celebration_top10",
            status="TESTED",
            n_classical=len(classical),
            p_null=p_null,
            top10_hits=hits,
            n_hits=n_hits,
            p_value_binomial=float(p_value),
            alpha_test=ALPHA_TEST,
            pass_=bool(p_value < ALPHA_TEST and n_hits >= 3),
        )

    print(f"[5/5] T2 — al-Fātiḥa PageRank sum vs random 7-bundles…",
          file=sys.stderr)
    fatiha_idx = [idx_of[(1, a)] for a in range(1, 8)]
    S_F = float(pr[fatiha_idx].sum())

    rng = np.random.default_rng(SEED)
    # Sample 10,000 random 7-subsets from {0..N-1} without replacement
    # using vectorised partial sort
    bundle_sums = np.empty(N_BOOT_BUNDLES, dtype=np.float64)
    all_idx = np.arange(N)
    for b in range(N_BOOT_BUNDLES):
        pick = rng.choice(N, size=7, replace=False)
        bundle_sums[b] = pr[pick].sum()

    p2 = float(np.mean(bundle_sums >= S_F))
    t2_result = dict(
        test="T2_fatiha_pagerank_sum",
        status="TESTED",
        fatiha_idxs=fatiha_idx,
        S_F=S_F,
        n_null_bundles=N_BOOT_BUNDLES,
        null_mean=float(bundle_sums.mean()),
        null_std=float(bundle_sums.std()),
        null_p97_5=float(np.percentile(bundle_sums, 97.5)),
        null_p99_9=float(np.percentile(bundle_sums, 99.9)),
        S_F_zscore=float((S_F - bundle_sums.mean()) / bundle_sums.std()),
        p_value=p2,
        alpha_test=ALPHA_TEST,
        pass_=bool(p2 < ALPHA_TEST),
    )

    # Q 1 aggregate rank: sum-of-PageRank over the 7 Fātiḥa verses,
    # compared to all bundles. Equivalent descriptive: z-score already
    # above; the exact percentile = 1 - p2.
    q1_aggregate_rank = dict(
        q1_sum_pagerank=S_F,
        percentile_vs_null=float(100.0 * (1.0 - p2)),
        z_vs_null=float((S_F - bundle_sums.mean()) / bundle_sums.std()),
    )

    # H-NEW-167 hub overlap (sanity)
    h167_hubs_refs = [
        (55, 13), (77, 15), (26, 108), (26, 8), (26, 9),
        (1, 2), (2, 136), (3, 16), (6, 21), (26, 226),
    ]
    top10_refs = [(v["surah"], v["ayah"]) for v in top10]
    h167_overlap = [r for r in top10_refs if r in set(h167_hubs_refs)]

    out = dict(
        hypothesis="H-NEW-201",
        seed=SEED,
        rules_tuple="(no-tashkeel; whitespace-collapsed; basmala-only-in-Q1)",
        method=dict(
            graph="top-K=5 directed weighted (edge weight = Jaccard), "
                  "no symmetrisation",
            pagerank=f"damping={DAMPING}, n_iter={N_ITER}, "
                     "uniform personalisation, dangling → uniform",
            bonferroni_k=BONFERRONI_K,
            alpha_family=ALPHA_FAMILY,
            alpha_test=ALPHA_TEST,
        ),
        graph_stats=dict(
            n_nodes=N,
            n_directed_edges=n_edges,
            n_dangling=n_dangling,
            mean_top1_sim=float(sims[:, 0].mean()),
            mean_top5_sim=float(sims[:, 4].mean()),
            convergence_trace=trace,
        ),
        top20_by_pagerank=top20,
        T1=t1_result,
        T2=t2_result,
        q1_aggregate_rank=q1_aggregate_rank,
        h167_hub_overlap=dict(
            h167_top10_refs=h167_hubs_refs,
            h201_top10_refs=top10_refs,
            overlap=h167_overlap,
            overlap_count=len(h167_overlap),
        ),
        prereg="findings/phase-b-hypotheses/h-new-201-pagerank-verse-twin-prereg.md",
    )

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2, default=str)
    print(f"wrote {OUT_JSON}", file=sys.stderr)

    # Print concise result summary to stdout
    print("\n=== H-NEW-201 SUMMARY ===")
    print(f"N={N}, edges={n_edges}, dangling={n_dangling}, "
          f"top-1 mean sim={sims[:,0].mean():.4f}")
    print(f"PR converged: {trace}")
    print("\nTop-10 by PageRank:")
    for v in top10:
        print(f"  {v['rank']:2d}. Q {v['surah']}:{v['ayah']:<4} "
              f"PR={v['pagerank']:.6f}  {v['text_preview']}")
    print(f"\nT1 (classical-top-100 overlap): {t1_result}")
    print(f"\nT2 (Fātiḥa PR sum): S_F={S_F:.6f}, "
          f"null_mean={bundle_sums.mean():.6f}, "
          f"z={t2_result['S_F_zscore']:.2f}, "
          f"p={p2:.5f}, pass={t2_result['pass_']}")
    print(f"\nQ1 aggregate: percentile vs null = "
          f"{q1_aggregate_rank['percentile_vs_null']:.2f}")


if __name__ == "__main__":
    main()
