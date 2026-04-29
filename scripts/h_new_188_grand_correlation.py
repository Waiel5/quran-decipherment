#!/usr/bin/env python3
"""H-NEW-188 — Grand correlation/covariance matrix of all per-surah structural measures.

Pre-reg: findings/phase-b-hypotheses/h-new-188-grand-correlation-prereg.md
Seed: 20260419. Bonferroni k=2.

Builds 114 × 19 feature dataframe, computes Pearson correlation matrix,
hierarchical clustering by 1-|r|, PCA (top-3 factors), and tests Pattern-B
bundle coherence via permutation null.

Outputs:
- findings/phase-b-hypotheses/csv/h-new-188.json
- findings/phase-b-hypotheses/csv/h-new-188-corrmatrix.csv
- findings/phase-b-hypotheses/csv/h-new-188-loadings.csv
"""

from __future__ import annotations

import csv
import json
import math
import random
from pathlib import Path

import numpy as np

SEED = 20260419
N_PERMS = 10_000
PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H125 = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-125.json"
H172 = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-172-per-surah.csv"
H168 = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-168-per-surah-dispersion.csv"
OUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-188.json"
OUT_CORR = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-188-corrmatrix.csv"
OUT_LOAD = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-188-loadings.csv"

CONTENT_AXES = [
    "surah_length", "mean_verse_length", "muq_cardinality",
    "allah_density", "qul_density", "prophet_narrative_density",
    "legal_term_density", "eschatological_density", "book_reference_density",
    "oath_density", "divine_name_density", "personal_pronoun_density",
    "rhyme_letter_diversity", "refrain_density", "loanword_density",
]
ZIPF_HEAP_DISP = ["alpha_zipf", "beta_heap", "dispersion"]
ALL_FEATURES = CONTENT_AXES + ZIPF_HEAP_DISP + ["noldeke_rank"]
PATTERN_B_BUNDLE = ["qul_density", "book_reference_density",
                    "eschatological_density", "loanword_density",
                    "muq_cardinality"]


def load_data():
    h125 = json.load(H125.open())
    psv = h125["per_surah_axis_values"]

    # h-172 keyed on surah_id
    h172 = {}
    with H172.open() as f:
        for row in csv.DictReader(f):
            s = int(row["surah_id"])
            a = _ffloat(row.get("alpha"))
            b = _ffloat(row.get("beta_h159"))
            d = _ffloat(row.get("dispersion_h163"))
            h172[s] = {"alpha_zipf": a, "beta_heap": b, "dispersion_h172": d}

    # h-168 dispersion fallback (all 114)
    h168 = {}
    with H168.open() as f:
        for row in csv.DictReader(f):
            s = int(row["sid"])
            h168[s] = _ffloat(row.get("dispersion"))

    rows = []
    for s_str in sorted(psv.keys(), key=int):
        s = int(s_str)
        axes = psv[s_str]["axis_values"]
        rec = {"surah": s, "name": psv[s_str].get("name", ""),
               "noldeke_rank": psv[s_str].get("noldeke_rank", float("nan"))}
        for ax in CONTENT_AXES:
            rec[ax] = axes.get(ax, float("nan"))
        # merge alpha, beta
        rec["alpha_zipf"] = h172.get(s, {}).get("alpha_zipf", float("nan"))
        rec["beta_heap"] = h172.get(s, {}).get("beta_heap", float("nan"))
        # dispersion: prefer h-168 (all 114), fall back to h-172
        d168 = h168.get(s, float("nan"))
        d172 = h172.get(s, {}).get("dispersion_h172", float("nan"))
        rec["dispersion"] = d168 if not math.isnan(d168) else d172
        rows.append(rec)
    return rows


def _ffloat(x):
    try:
        if x is None:
            return float("nan")
        s = str(x).strip()
        if not s or s.lower() == "nan":
            return float("nan")
        return float(s)
    except Exception:
        return float("nan")


def pairwise_pearson(X: np.ndarray):
    """X shape (N,M). Return M×M Pearson corr with pairwise-complete obs.
    NaNs are treated as missing.
    """
    N, M = X.shape
    corr = np.zeros((M, M))
    n_used = np.zeros((M, M), dtype=int)
    for i in range(M):
        for j in range(i, M):
            xi, xj = X[:, i], X[:, j]
            mask = ~(np.isnan(xi) | np.isnan(xj))
            n = mask.sum()
            n_used[i, j] = n_used[j, i] = n
            if n < 3:
                corr[i, j] = corr[j, i] = float("nan")
                continue
            a = xi[mask]
            b = xj[mask]
            amu = a.mean(); bmu = b.mean()
            asd = a.std(ddof=0); bsd = b.std(ddof=0)
            if asd == 0 or bsd == 0:
                corr[i, j] = corr[j, i] = float("nan")
                continue
            r = float(((a - amu) * (b - bmu)).sum() / (n * asd * bsd))
            corr[i, j] = corr[j, i] = r
    return corr, n_used


def pairwise_spearman(X: np.ndarray):
    """Spearman via ranking, pairwise-complete."""
    N, M = X.shape
    corr = np.zeros((M, M))
    for i in range(M):
        for j in range(i, M):
            xi, xj = X[:, i], X[:, j]
            mask = ~(np.isnan(xi) | np.isnan(xj))
            if mask.sum() < 3:
                corr[i, j] = corr[j, i] = float("nan")
                continue
            a = _rank_avg(xi[mask])
            b = _rank_avg(xj[mask])
            amu = a.mean(); bmu = b.mean()
            asd = a.std(ddof=0); bsd = b.std(ddof=0)
            if asd == 0 or bsd == 0:
                corr[i, j] = corr[j, i] = float("nan")
                continue
            r = float(((a - amu) * (b - bmu)).sum() / (len(a) * asd * bsd))
            corr[i, j] = corr[j, i] = r
    return corr


def _rank_avg(vals: np.ndarray) -> np.ndarray:
    order = np.argsort(vals, kind="mergesort")
    ranks = np.empty_like(vals, dtype=float)
    i = 0
    n = len(vals)
    while i < n:
        j = i
        while j + 1 < n and vals[order[j + 1]] == vals[order[i]]:
            j += 1
        avg = (i + j + 2) / 2.0  # 1-indexed mean
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def median_impute(X: np.ndarray) -> np.ndarray:
    X = X.copy()
    M = X.shape[1]
    for j in range(M):
        col = X[:, j]
        mask = np.isnan(col)
        if mask.any():
            med = np.nanmedian(col)
            X[mask, j] = med
    return X


def zscore_cols(X: np.ndarray) -> np.ndarray:
    X = X.copy().astype(float)
    mu = X.mean(axis=0)
    sd = X.std(axis=0, ddof=0)
    sd[sd == 0] = 1.0
    return (X - mu) / sd


def pca_svd(X_z: np.ndarray):
    """PCA via SVD. X_z is z-scored (N,M). Returns eigenvalues, loadings (M,M)."""
    N, M = X_z.shape
    # covariance = X_z.T @ X_z / N (since z-scored)
    cov = (X_z.T @ X_z) / N
    # symmetric eigen-decomp
    eigvals, eigvecs = np.linalg.eigh(cov)
    # sort descending
    order = np.argsort(eigvals)[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]
    # loadings = eigvec scaled by sqrt(eigval) (column) — standard definition
    loadings = eigvecs * np.sqrt(np.maximum(eigvals, 0))[np.newaxis, :]
    return eigvals, eigvecs, loadings


def hierarchical_cluster(dist: np.ndarray, labels: list[str]):
    """Complete-linkage agglomerative clustering. Returns merge order list."""
    M = dist.shape[0]
    # active clusters: map cluster-id -> list of leaf labels
    clusters = {i: [labels[i]] for i in range(M)}
    # pair distance as dict
    D = {(i, j): float(dist[i, j]) for i in range(M) for j in range(i + 1, M)}
    next_id = M
    merges = []
    while len(clusters) > 1:
        # find min
        kmin, vmin = min(D.items(), key=lambda kv: kv[1])
        i, j = kmin
        new_id = next_id
        next_id += 1
        merges.append({"a": i, "b": j, "dist": vmin,
                       "members": clusters[i] + clusters[j]})
        # update distances: complete linkage
        new_dists = {}
        for k in list(clusters.keys()):
            if k in (i, j):
                continue
            di = D.get((min(i, k), max(i, k)), float("inf"))
            dj = D.get((min(j, k), max(j, k)), float("inf"))
            new_dists[(min(new_id, k), max(new_id, k))] = max(di, dj)
        # remove old
        D = {k: v for k, v in D.items() if i not in k and j not in k}
        D.update(new_dists)
        clusters.pop(i)
        clusters.pop(j)
        clusters[new_id] = merges[-1]["members"]
    return merges


def bundle_test(loadings: np.ndarray, feature_names: list[str],
                bundle: list[str], n_perms: int, seed: int):
    """Pre-reg test: max over PC1..PC3 of mean absolute loading of the bundle.
    Null: random 5-feature subsets.
    """
    name_to_idx = {n: i for i, n in enumerate(feature_names)}
    bundle_idx = [name_to_idx[b] for b in bundle]
    # observed mean|L| per PC, take max
    obs_per_pc = [float(np.mean(np.abs(loadings[bundle_idx, pc])))
                  for pc in range(3)]
    obs_max = max(obs_per_pc)

    rng = random.Random(seed)
    all_idx = list(range(len(feature_names)))
    n_ge = 0
    null_vals = []
    for _ in range(n_perms):
        draw = rng.sample(all_idx, len(bundle))
        vals = [float(np.mean(np.abs(loadings[draw, pc]))) for pc in range(3)]
        mx = max(vals)
        null_vals.append(mx)
        if mx >= obs_max:
            n_ge += 1
    p_one = (n_ge + 1) / (n_perms + 1)
    null_mean = float(np.mean(null_vals))
    null_p95 = float(np.percentile(null_vals, 95))
    return {
        "bundle": bundle,
        "bundle_indices": bundle_idx,
        "obs_mean_abs_loading_per_pc": {f"PC{k+1}": obs_per_pc[k] for k in range(3)},
        "obs_max_over_top3_pc": obs_max,
        "pc_of_obs_max": int(np.argmax(obs_per_pc) + 1),
        "null_mean": null_mean,
        "null_p95": null_p95,
        "p_one_sided": p_one,
        "pass_pre_reg": bool(obs_max > null_p95),
    }


def main():
    rows = load_data()
    n = len(rows)
    assert n == 114
    feature_names = ALL_FEATURES  # 19
    M = len(feature_names)

    X = np.full((n, M), np.nan, dtype=float)
    for i, r in enumerate(rows):
        for j, f in enumerate(feature_names):
            v = r.get(f, float("nan"))
            try:
                X[i, j] = float(v) if v is not None and not (isinstance(v, float) and math.isnan(v)) else float("nan")
            except Exception:
                X[i, j] = float("nan")

    n_nan = int(np.isnan(X).sum())
    n_missing_per = np.isnan(X).sum(axis=0).tolist()

    # Pearson and Spearman
    corr_p, n_used = pairwise_pearson(X)
    corr_s = pairwise_spearman(X)

    # Hierarchical clustering by 1-|r|
    dist = 1 - np.abs(np.nan_to_num(corr_p, nan=0.0))
    np.fill_diagonal(dist, 0.0)
    merges = hierarchical_cluster(dist, feature_names)

    # PCA on median-imputed z-scored matrix
    X_imp = median_impute(X)
    X_z = zscore_cols(X_imp)
    eigvals, eigvecs, loadings = pca_svd(X_z)
    total_var = float(np.sum(eigvals))
    pct_var = (eigvals / total_var * 100).tolist()
    cum_var = np.cumsum(eigvals) / total_var * 100
    top3_cum = float(cum_var[2])

    # Sensitivity: listwise-complete PCA
    mask_complete = ~np.any(np.isnan(X), axis=1)
    n_complete = int(mask_complete.sum())
    if n_complete >= M + 5:
        X_c = zscore_cols(X[mask_complete])
        ev_c, _, load_c = pca_svd(X_c)
        pct_c = (ev_c / np.sum(ev_c) * 100).tolist()
    else:
        ev_c = None; load_c = None; pct_c = None

    # Pattern-B bundle test
    bundle_result = bundle_test(loadings, feature_names, PATTERN_B_BUNDLE,
                                 N_PERMS, SEED)

    # Sensitivity bundle test on listwise PCA
    bundle_listwise = None
    if load_c is not None:
        bundle_listwise = bundle_test(load_c, feature_names, PATTERN_B_BUNDLE,
                                       N_PERMS, SEED + 1)

    # Highest pairwise |r| summaries
    pair_abs = []
    for i in range(M):
        for j in range(i + 1, M):
            rr = corr_p[i, j]
            if not math.isnan(rr):
                pair_abs.append((feature_names[i], feature_names[j], float(rr)))
    pair_abs.sort(key=lambda t: abs(t[2]), reverse=True)
    top_pairs = pair_abs[:25]
    bottom_pairs = sorted(pair_abs, key=lambda t: abs(t[2]))[:10]

    # Top-3 loadings human-readable
    def top_loadings(pc_idx, k=6):
        L = loadings[:, pc_idx]
        idx = np.argsort(np.abs(L))[::-1][:k]
        return [{"feature": feature_names[i], "loading": float(L[i])}
                for i in idx]

    factor_summary = []
    for pc in range(3):
        factor_summary.append({
            "pc": pc + 1,
            "eigenvalue": float(eigvals[pc]),
            "pct_var": float(pct_var[pc]),
            "cum_pct_var": float(cum_var[pc]),
            "top_loadings": top_loadings(pc, k=6),
        })

    out = {
        "finding_id": "H-NEW-188",
        "title": "Grand correlation matrix + factor analysis of per-surah measures",
        "pre_reg": "findings/phase-b-hypotheses/h-new-188-grand-correlation-prereg.md",
        "seed": SEED,
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "n_surahs": n,
        "n_features": M,
        "feature_names": feature_names,
        "missing_per_feature": dict(zip(feature_names, n_missing_per)),
        "total_nan_cells": n_nan,
        "pearson_matrix": corr_p.tolist(),
        "spearman_matrix": corr_s.tolist(),
        "n_used_pairwise": n_used.tolist(),
        "pca_imputed": {
            "eigenvalues": eigvals.tolist(),
            "pct_variance": pct_var,
            "cumulative_pct_variance": cum_var.tolist(),
            "top3_cum_pct": top3_cum,
            "loadings": loadings.tolist(),
            "factor_summary_top3": factor_summary,
        },
        "pca_listwise_complete": {
            "n_complete": n_complete,
            "eigenvalues": ev_c.tolist() if ev_c is not None else None,
            "pct_variance": pct_c,
            "loadings": load_c.tolist() if load_c is not None else None,
        },
        "top_pairs_by_abs_r": [{"a": a, "b": b, "r": rr}
                                for a, b, rr in top_pairs],
        "weakest_pairs_by_abs_r": [{"a": a, "b": b, "r": rr}
                                    for a, b, rr in bottom_pairs],
        "hierarchical_merges": [
            {"dist": m["dist"], "size": len(m["members"]),
             "members": m["members"]}
            for m in merges
        ],
        "pattern_b_bundle_test": bundle_result,
        "pattern_b_bundle_test_listwise_sensitivity": bundle_listwise,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)

    # Corr matrix CSV
    with OUT_CORR.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow([""] + feature_names)
        for i, row in enumerate(corr_p):
            w.writerow([feature_names[i]] +
                       [f"{v:.4f}" if not math.isnan(v) else "" for v in row])

    # Loadings CSV
    with OUT_LOAD.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["feature"] + [f"PC{k+1}" for k in range(M)])
        for i, fname in enumerate(feature_names):
            w.writerow([fname] + [f"{loadings[i, k]:.4f}" for k in range(M)])

    # Console summary
    print("=" * 76)
    print("H-NEW-188 — Grand correlation matrix + factor analysis")
    print("=" * 76)
    print(f"N surahs = {n}  |  M features = {M}")
    print(f"NaN cells = {n_nan}  |  missing per feature = "
          f"{dict(zip(feature_names, n_missing_per))}")
    print()
    print("Top-3 factor variance:")
    for fs in factor_summary:
        print(f"  PC{fs['pc']}: λ={fs['eigenvalue']:.3f}  "
              f"{fs['pct_var']:.2f}% (cum {fs['cum_pct_var']:.2f}%)")
        for tl in fs["top_loadings"]:
            print(f"      {tl['feature']:<30s}  {tl['loading']:+.3f}")
    print(f"\nCumulative top-3 variance: {top3_cum:.2f}%")
    print()
    print("Top 10 |r| pairs:")
    for a, b, rr in top_pairs[:10]:
        print(f"  r={rr:+.3f}  {a} × {b}")
    print()
    print("Pattern-B bundle test (corpus-wide, imputed):")
    br = bundle_result
    for pc, v in br["obs_mean_abs_loading_per_pc"].items():
        print(f"  mean|L| on {pc} = {v:.3f}")
    print(f"  obs max over PC1..3 = {br['obs_max_over_top3_pc']:.3f}  "
          f"(on PC{br['pc_of_obs_max']})")
    print(f"  null mean = {br['null_mean']:.3f}  p95 = {br['null_p95']:.3f}")
    print(f"  one-sided p = {br['p_one_sided']:.4f}")
    print(f"  PASS pre-reg: {br['pass_pre_reg']}")
    if bundle_listwise:
        print(f"  Listwise sensitivity (n={n_complete}): "
              f"obs_max={bundle_listwise['obs_max_over_top3_pc']:.3f}  "
              f"p={bundle_listwise['p_one_sided']:.4f}  "
              f"PASS={bundle_listwise['pass_pre_reg']}")
    print()
    print(f"Outputs:\n  {OUT_JSON}\n  {OUT_CORR}\n  {OUT_LOAD}")


if __name__ == "__main__":
    main()
