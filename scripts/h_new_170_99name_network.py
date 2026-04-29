#!/usr/bin/env python3
"""
H-NEW-170 — Full 99-name divine-attribute co-occurrence network analysis.

Pre-registered at findings/phase-b-hypotheses/h-new-170-99name-network-prereg.md.

Pipeline:
  1. Build occurrence matrix M[99, 6236]
  2. Compute co-occurrence C, expected E, z-score (phi-like)
  3. Edges kept at z > 2
  4. Global clustering coefficient + degree distribution + top-5 hubs
  5. Null: marginal-preserving name-shuffle, K=1000, seed 20260419
  6. Structure test p-value
  7. Ghazālī 3-partition modularity vs random 3-partitions

Runtime: ~1-2 min.
Seed: 20260419.
Bonferroni k=2, alpha_bon=0.025.
"""
from __future__ import annotations

import json
import math
import random
import re
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
NAMES_TXT = ROOT / "data/asma-al-husna.txt"
OUTPUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-170-99name-network.json"

SEED = 20260419
N_PERMS_STRUCTURE = 1000
N_PERMS_GHAZALI = 1000
Z_THRESHOLD = 2.0
BONFERRONI_K = 2
ALPHA_BON = 0.025

ARABIC_LETTER = r"[\u0621-\u064A]"
NON_AR = r"[^\u0621-\u064A]"


def load_names(path: Path) -> list[str]:
    names = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        names.append(s)
    return names


def name_forms(name: str) -> list[list[str]]:
    """For a (possibly multi-word) name, return list of constituent-alternatives.
    Each constituent yields a list of acceptable surface forms.
    Name is matched if for EACH constituent at least one form is present (whole-word).
    """
    parts = name.split()
    constituents = []
    for p in parts:
        alts = [p]
        # If starts with ال, add stem (without ال)
        if p.startswith("ال") and len(p) > 2:
            alts.append(p[2:])
        constituents.append(alts)
    return constituents


def verse_contains_name(verse_text: str, constituents: list[list[str]]) -> bool:
    """Verse contains the name iff every constituent has at least one form present as whole word."""
    for alts in constituents:
        found = False
        for form in alts:
            pattern = r"(^|" + NON_AR + r")" + re.escape(form) + r"($|" + NON_AR + r")"
            if re.search(pattern, verse_text):
                found = True
                break
        if not found:
            return False
    return True


def load_verses(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    verses = []
    for surah in data:
        for v in surah["verses"]:
            verses.append(v["text"])
    return verses


def build_occurrence_matrix(names: list[str], verses: list[str]) -> np.ndarray:
    M = np.zeros((len(names), len(verses)), dtype=np.uint8)
    for i, name in enumerate(names):
        cts = name_forms(name)
        for v_idx, v_text in enumerate(verses):
            if verse_contains_name(v_text, cts):
                M[i, v_idx] = 1
    return M


def compute_zscore_matrix(M: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Returns (C, E, Z) for n_names x n_names."""
    n_names, N = M.shape
    n_i = M.sum(axis=1).astype(np.float64)
    p_i = n_i / N
    # C = M @ M.T is co-occurrence (including diagonal = n_i)
    C = (M.astype(np.int32) @ M.T.astype(np.int32)).astype(np.float64)
    E = np.outer(n_i, n_i) / N
    # variance factor (1 - p_i)(1 - p_j)
    one_minus_p = 1.0 - p_i
    var_factor = np.outer(one_minus_p, one_minus_p)
    denom = np.sqrt(np.maximum(E * var_factor, 1e-12))
    Z = (C - E) / denom
    # zero the diagonal and any undefined entries
    np.fill_diagonal(Z, 0.0)
    Z[E <= 0] = 0.0
    return C, E, Z


def global_clustering_coefficient(adj: np.ndarray) -> float:
    """Transitivity: 3 * triangles / connected_triples.
    adj: n x n binary symmetric matrix with zero diagonal.
    """
    # Triangles: trace(A^3) / 6; number of triangles
    # Using matrix mult
    A = adj.astype(np.int64)
    A2 = A @ A
    triangles = (A2 * A).sum() / 6  # closed triangles

    # Connected triples: for each node, k*(k-1)/2
    degs = A.sum(axis=1)
    connected_triples = (degs * (degs - 1) // 2).sum()

    if connected_triples == 0:
        return 0.0
    # Transitivity = 3 * triangles / connected_triples
    return float(3 * triangles / connected_triples)


def permute_occurrence(M: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Permute each row independently: randomly place the same number of 1s in random verses."""
    n_names, N = M.shape
    M_new = np.zeros_like(M)
    marginals = M.sum(axis=1)
    for i in range(n_names):
        k = int(marginals[i])
        if k == 0:
            continue
        idx = rng.choice(N, size=k, replace=False)
        M_new[i, idx] = 1
    return M_new


def compute_modularity(adj_weighted: np.ndarray, partition: list[int]) -> float:
    """Newman modularity on undirected weighted graph.
    Q = (1/2m) * sum_{i,j} [A_ij - k_i k_j / 2m] * delta(c_i, c_j)
    """
    W = adj_weighted.copy()
    np.fill_diagonal(W, 0.0)
    # symmetrize (should already be symmetric)
    W = (W + W.T) / 2.0
    twom = W.sum()
    if twom == 0:
        return 0.0
    k = W.sum(axis=1)
    # same-community indicator
    parts = np.array(partition)
    same = (parts[:, None] == parts[None, :]).astype(np.float64)
    expected = np.outer(k, k) / twom
    Q = ((W - expected) * same).sum() / twom
    return float(Q)


# Ghazālī family assignment (locked in pre-reg)
GHAZALI_KNOWING = {
    "العليم", "الحكيم", "السميع", "البصير", "اللطيف", "الخبير",
    "الحسيب", "المحصي", "الشهيد", "الحفيظ", "الرقيب", "الحكم",
    "المقيت", "الحق", "العدل", "الواجد",
}
GHAZALI_WILLING = {
    "الرحمن", "الرحيم", "الملك", "القدوس", "السلام", "المؤمن",
    "المهيمن", "الغفار", "الوهاب", "الرزاق", "الفتاح", "الغفور",
    "الشكور", "الكريم", "المجيب", "الواسع", "الودود", "الباعث",
    "الولي", "الحميد", "المحيي", "التواب", "العفو", "الرؤوف",
    "المقسط", "الجامع", "النور", "الهادي", "البديع", "الرشيد",
    "الصبور", "البر", "مالك الملك", "ذو الجلال والإكرام",
    "الوكيل", "المجيد", "الحليم", "الباقي",
}
GHAZALI_ABLE = {
    "الله", "العزيز", "الجبار", "المتكبر", "الخالق", "البارئ",
    "المصور", "القهار", "القابض", "الباسط", "الخافض", "الرافع",
    "المعز", "المذل", "العظيم", "العلي", "الكبير", "الجليل",
    "القوي", "المتين", "المبدئ", "المعيد", "المميت", "الحي",
    "القيوم", "الماجد", "الواحد", "الصمد", "القادر", "المقتدر",
    "المقدم", "المؤخر", "الأول", "الآخر", "الظاهر", "الباطن",
    "الوالي", "المتعالي", "المنتقم", "الغني", "المغني", "المانع",
    "الضار", "النافع", "الوارث",
}


def ghazali_partition(names: list[str]) -> list[int]:
    """Return integer labels: 0=Knowing, 1=Willing, 2=Able."""
    part = []
    errors = []
    for n in names:
        if n in GHAZALI_KNOWING:
            part.append(0)
        elif n in GHAZALI_WILLING:
            part.append(1)
        elif n in GHAZALI_ABLE:
            part.append(2)
        else:
            errors.append(n)
            part.append(-1)
    if errors:
        raise RuntimeError(f"Unassigned names: {errors}")
    return part


def main() -> None:
    print("H-NEW-170 — 99-name co-occurrence network", flush=True)
    print(f"Seed: {SEED}, z-threshold: {Z_THRESHOLD}", flush=True)
    rng = np.random.default_rng(SEED)
    random.seed(SEED)

    # Load
    names = load_names(NAMES_TXT)
    print(f"Loaded {len(names)} names", flush=True)
    assert len(names) == 99, f"expected 99 names, got {len(names)}"

    verses = load_verses(QURAN_JSON)
    N = len(verses)
    print(f"Loaded {N} verses", flush=True)
    assert N >= 6230

    # Validate Ghazālī partition before running
    part = ghazali_partition(names)
    g_counts = [part.count(k) for k in range(3)]
    print(f"Ghazālī partition sizes: Knowing={g_counts[0]}, Willing={g_counts[1]}, Able={g_counts[2]}", flush=True)
    assert sum(g_counts) == 99

    # Build occurrence matrix
    print("\nBuilding occurrence matrix …", flush=True)
    M = build_occurrence_matrix(names, verses)
    marginals = M.sum(axis=1)
    total_occ_verses = int((M.sum(axis=0) > 0).sum())
    print(f"  Names occurring at least once: {int((marginals > 0).sum())}/99", flush=True)
    print(f"  Verses containing at least one name: {total_occ_verses}/{N}", flush=True)
    print(f"  Top 10 most frequent names:", flush=True)
    sorted_idx = np.argsort(-marginals)
    for k in range(10):
        i = sorted_idx[k]
        print(f"    {names[i]}: {int(marginals[i])} verses", flush=True)

    # Co-occurrence, z-score
    print("\nComputing z-score matrix …", flush=True)
    C, E, Z = compute_zscore_matrix(M)

    # Edge set
    adj = (Z > Z_THRESHOLD).astype(np.int64)
    np.fill_diagonal(adj, 0)
    # symmetrize for safety
    adj = np.maximum(adj, adj.T)
    n_edges = int(adj.sum() // 2)
    print(f"  Edges with z > {Z_THRESHOLD}: {n_edges}", flush=True)

    # Degree distribution
    degrees = adj.sum(axis=1)
    print(f"  Degree: mean={degrees.mean():.2f}, max={degrees.max()}, median={int(np.median(degrees))}", flush=True)
    print(f"  Isolated nodes (deg=0): {int((degrees == 0).sum())}", flush=True)

    # Top-5 hubs
    top5_idx = np.argsort(-degrees)[:5]
    top5 = []
    print("  Top-5 hub names (by degree):", flush=True)
    for i in top5_idx:
        top5.append({"name": names[i], "degree": int(degrees[i]), "n_verses": int(marginals[i])})
        print(f"    {names[i]} (deg={int(degrees[i])}, verses={int(marginals[i])})", flush=True)

    # Global clustering coefficient
    C_global = global_clustering_coefficient(adj)
    print(f"\n  Global clustering coefficient (transitivity): {C_global:.4f}", flush=True)

    # Null permutations for structure
    print(f"\nPermutation null ({N_PERMS_STRUCTURE} iters) — clustering coefficient …", flush=True)
    C_null_samples = []
    n_edges_null = []
    for k in range(N_PERMS_STRUCTURE):
        M_perm = permute_occurrence(M, rng)
        _, _, Z_perm = compute_zscore_matrix(M_perm)
        adj_perm = (Z_perm > Z_THRESHOLD).astype(np.int64)
        np.fill_diagonal(adj_perm, 0)
        adj_perm = np.maximum(adj_perm, adj_perm.T)
        c_null = global_clustering_coefficient(adj_perm)
        C_null_samples.append(c_null)
        n_edges_null.append(int(adj_perm.sum() // 2))
        if (k + 1) % 100 == 0:
            print(f"  perm {k+1}/{N_PERMS_STRUCTURE}", flush=True)

    C_null_arr = np.array(C_null_samples)
    null_mean = C_null_arr.mean()
    null_std = C_null_arr.std()
    # p-value: fraction of nulls >= observed (one-sided, observed > null)
    p_cluster = float((C_null_arr >= C_global).sum() + 1) / (len(C_null_arr) + 1)
    print(f"  Null clustering: mean={null_mean:.4f}, std={null_std:.4f}", flush=True)
    print(f"  Null edges: mean={np.mean(n_edges_null):.1f}", flush=True)
    print(f"  Observed: {C_global:.4f}", flush=True)
    print(f"  p(C_null >= C_obs) = {p_cluster:.4f}", flush=True)

    structure_pass = p_cluster < ALPHA_BON
    print(f"  Structure test (alpha={ALPHA_BON}): {'PASS' if structure_pass else 'FAIL'}", flush=True)

    # Ghazālī modularity test
    print("\nGhazālī 3-partition modularity …", flush=True)
    # Weighted adj: max(Z, 0) with z>0 so all "positive" co-occurrences count
    W = np.maximum(Z, 0.0).copy()
    np.fill_diagonal(W, 0.0)

    Q_obs = compute_modularity(W, part)
    print(f"  Observed modularity Q = {Q_obs:.4f}", flush=True)

    # Null: random 3-partitions matching sizes of Ghazālī groups
    Q_null_samples = []
    sizes = g_counts
    label_pool = [0] * sizes[0] + [1] * sizes[1] + [2] * sizes[2]
    assert len(label_pool) == 99
    for k in range(N_PERMS_GHAZALI):
        shuffled = label_pool[:]
        random.shuffle(shuffled)
        Q_null_samples.append(compute_modularity(W, shuffled))

    Q_null_arr = np.array(Q_null_samples)
    Q_null_mean = Q_null_arr.mean()
    Q_null_std = Q_null_arr.std()
    p_mod = float((Q_null_arr >= Q_obs).sum() + 1) / (len(Q_null_arr) + 1)
    print(f"  Null Q: mean={Q_null_mean:.4f}, std={Q_null_std:.4f}", flush=True)
    print(f"  p(Q_null >= Q_obs) = {p_mod:.4f}", flush=True)
    ghazali_pass = p_mod < ALPHA_BON
    print(f"  Ghazālī modularity test (alpha={ALPHA_BON}): {'PASS' if ghazali_pass else 'FAIL'}", flush=True)

    # Verdict
    print("\n=== VERDICT ===", flush=True)
    if structure_pass and ghazali_pass:
        verdict = "PASS-STRUCTURE-AND-GHAZALI"
    elif structure_pass:
        verdict = "PASS-STRUCTURE-ONLY"
    elif ghazali_pass:
        verdict = "PASS-GHAZALI-ONLY"
    else:
        verdict = "FAIL"
    print(f"  {verdict}", flush=True)

    # Top co-occurring pairs (for interpretation)
    print("\nTop-20 name pairs by z-score:", flush=True)
    pairs = []
    for i, j in combinations(range(99), 2):
        if E[i, j] > 0:
            pairs.append((names[i], names[j], int(C[i, j]), float(E[i, j]), float(Z[i, j])))
    pairs.sort(key=lambda x: -x[4])
    for k, (a, b, obs, exp, z) in enumerate(pairs[:20]):
        print(f"  {k+1:>2}. {a} + {b}: obs={obs}, exp={exp:.2f}, z={z:+.2f}", flush=True)

    # Build edge list for output (only edges with z > threshold)
    edge_list = []
    for i, j in combinations(range(99), 2):
        if Z[i, j] > Z_THRESHOLD:
            edge_list.append({
                "name_a": names[i],
                "name_b": names[j],
                "obs": int(C[i, j]),
                "expected": float(E[i, j]),
                "z": float(Z[i, j]),
            })
    edge_list.sort(key=lambda d: -d["z"])

    # Per-name degree, with classification
    name_table = []
    fam_label = {0: "Knowing", 1: "Willing", 2: "Able"}
    for i, name in enumerate(names):
        name_table.append({
            "name": name,
            "n_verses": int(marginals[i]),
            "degree": int(degrees[i]),
            "ghazali_family": fam_label[part[i]],
        })

    out = {
        "id": "H-NEW-170",
        "title": "Full 99-name divine-attribute co-occurrence network",
        "seed": SEED,
        "n_verses": N,
        "n_names": 99,
        "z_threshold": Z_THRESHOLD,
        "n_edges_above_threshold": n_edges,
        "degree_distribution": {
            "mean": float(degrees.mean()),
            "max": int(degrees.max()),
            "median": float(np.median(degrees)),
            "min": int(degrees.min()),
            "isolated_count": int((degrees == 0).sum()),
        },
        "top5_hubs": top5,
        "clustering_coefficient_observed": C_global,
        "clustering_null": {
            "n_perms": N_PERMS_STRUCTURE,
            "mean": float(null_mean),
            "std": float(null_std),
            "edges_mean": float(np.mean(n_edges_null)),
            "edges_std": float(np.std(n_edges_null)),
            "p_value": p_cluster,
            "alpha_bon": ALPHA_BON,
            "pass": bool(structure_pass),
        },
        "ghazali_modularity": {
            "partition_sizes": {"Knowing": g_counts[0], "Willing": g_counts[1], "Able": g_counts[2]},
            "Q_observed": Q_obs,
            "null_mean": float(Q_null_mean),
            "null_std": float(Q_null_std),
            "n_perms": N_PERMS_GHAZALI,
            "p_value": p_mod,
            "alpha_bon": ALPHA_BON,
            "pass": bool(ghazali_pass),
        },
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "verdict": verdict,
        "top20_pairs": [
            {"name_a": a, "name_b": b, "obs": obs, "expected": exp, "z": z}
            for (a, b, obs, exp, z) in pairs[:20]
        ],
        "edges": edge_list,
        "name_table": name_table,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUTPUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
