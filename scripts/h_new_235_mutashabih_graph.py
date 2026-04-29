#!/usr/bin/env python3
"""
H-NEW-235 — Mutashābih full verse-graph: Louvain communities + mushaf alignment.

Pre-reg: findings/phase-b-hypotheses/h-new-235-mutashabih-full-graph-prereg.md
Seed: 20260419. Rules: no-tashkeel, hafs-kufan, char-based Levenshtein.
"""
import json
import sys
import time
import random
from collections import defaultdict
from pathlib import Path

import numpy as np
import networkx as nx
import community as community_louvain
from rapidfuzz.distance import Levenshtein

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"
OUTDIR = ROOT / "findings" / "phase-b-hypotheses"
SCRIPTS = ROOT / "scripts"

SEED = 20260419
random.seed(SEED)
np.random.seed(SEED)

MIN_LEN = 10
N_GRAM = 4
MIN_SHARED_NGRAMS = 2
SIM_THRESHOLD = 0.7  # = ratio < 0.3
LOUVAIN_RES = 1.0
NULL_ITERS = 100
TIME_CAP_SECONDS = 30 * 60


def juz_of(surah: int, verse: int) -> int:
    """Return juzʾ (1..30) for a given (surah, verse), per standard mushaf boundaries."""
    # Standard juzʾ boundaries (surah, verse) for the START of each juzʾ.
    STARTS = [
        (1, 1), (2, 142), (2, 253), (3, 93), (4, 24), (4, 148),
        (6, 1), (7, 88), (8, 41), (9, 94), (11, 6), (12, 53),
        (15, 1), (17, 1), (18, 75), (21, 1), (23, 1), (25, 21),
        (27, 56), (29, 46), (33, 31), (36, 28), (39, 32), (41, 47),
        (46, 1), (51, 1), (58, 1), (67, 1), (78, 1),
    ]
    # juzʾ 30 effectively starts at (78,1)
    for i in range(len(STARTS) - 1, -1, -1):
        s, v = STARTS[i]
        if (surah, verse) >= (s, v):
            return i + 1
    return 1


def mufassal_tier(surah: int) -> str:
    """Classical al-Suyūṭī conservative tiers; short-mufaṣṣal Q 78–114."""
    if surah >= 78:
        return "short_mufassal"
    if 50 <= surah < 78:
        return "medium_mufassal"
    if 49 <= surah < 50:  # actually spans 49 forward in some accounts; keep conservative
        return "long_mufassal"
    return "pre_mufassal"


def load_verses():
    with open(QURAN_JSON) as f:
        data = json.load(f)
    verses = []  # list of dicts {idx, surah, verse, text}
    idx = 0
    for s in data:
        surah_id = s["id"]
        for v in s["verses"]:
            verses.append({
                "idx": idx,
                "surah": surah_id,
                "verse": v["id"],
                "text": v["text"],
                "len": len(v["text"]),
            })
            idx += 1
    return verses


def build_ngram_index(verses, n=N_GRAM, min_len=MIN_LEN):
    inverted = defaultdict(list)
    verse_ngrams = {}
    for v in verses:
        text = v["text"]
        if len(text) < min_len:
            continue
        grams = set()
        for i in range(len(text) - n + 1):
            g = text[i:i+n]
            grams.add(g)
        verse_ngrams[v["idx"]] = grams
        for g in grams:
            inverted[g].append(v["idx"])
    return inverted, verse_ngrams


def get_candidate_pairs(inverted, verse_ngrams, min_shared=MIN_SHARED_NGRAMS):
    """For each verse, count how many distinct 4-grams it shares with every other verse."""
    shared_count = defaultdict(int)
    # Skip n-grams appearing in too many verses (inflate candidate set without signal)
    NGRAM_DF_CAP = 200
    for g, vs in inverted.items():
        if len(vs) < 2 or len(vs) > NGRAM_DF_CAP:
            continue
        vs_sorted = sorted(vs)
        for i in range(len(vs_sorted)):
            vi = vs_sorted[i]
            for j in range(i + 1, len(vs_sorted)):
                vj = vs_sorted[j]
                shared_count[(vi, vj)] += 1
    # Keep pairs with ≥ min_shared shared distinct 4-grams
    cands = [pair for pair, c in shared_count.items() if c >= min_shared]
    return cands


def compute_similarity_edges(cands, verses, threshold=SIM_THRESHOLD):
    """Exact Levenshtein on candidate pairs; keep those with 1 - d/max_len >= threshold."""
    edges = []
    by_idx = {v["idx"]: v for v in verses}
    for vi, vj in cands:
        t1 = by_idx[vi]["text"]
        t2 = by_idx[vj]["text"]
        max_len = max(len(t1), len(t2))
        if max_len == 0:
            continue
        # Early-cutoff: if length ratio < threshold, skip
        min_len = min(len(t1), len(t2))
        if min_len / max_len < threshold:
            continue
        d = Levenshtein.distance(t1, t2)
        sim = 1.0 - d / max_len
        if sim >= threshold:
            edges.append((vi, vj, sim, d))
    return edges


def main():
    t0 = time.time()
    print(f"[H-NEW-235] Seed {SEED}", flush=True)

    verses = load_verses()
    print(f"Loaded {len(verses)} verses", flush=True)

    print("Building 4-gram inverted index...", flush=True)
    inverted, verse_ngrams = build_ngram_index(verses)
    print(f"  unique 4-grams: {len(inverted)}; verses indexed: {len(verse_ngrams)}", flush=True)

    print("Building candidate pairs (shared ≥ 2 4-grams)...", flush=True)
    cands = get_candidate_pairs(inverted, verse_ngrams)
    print(f"  candidate pairs: {len(cands):,}", flush=True)

    print("Computing exact Levenshtein on candidates...", flush=True)
    edges = compute_similarity_edges(cands, verses)
    print(f"  high-similarity edges (sim >= {SIM_THRESHOLD}): {len(edges):,}", flush=True)

    # Build graph
    G = nx.Graph()
    for v in verses:
        G.add_node(v["idx"], surah=v["surah"], verse=v["verse"])
    for vi, vj, sim, d in edges:
        G.add_edge(vi, vj, weight=sim, lev=d)
    print(f"  graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges", flush=True)

    # Drop isolated nodes for modularity calc? Keep them; Louvain handles.
    # Louvain (degree-weighted)
    print("Running Louvain community detection...", flush=True)
    partition = community_louvain.best_partition(G, weight="weight",
                                                  random_state=SEED, resolution=LOUVAIN_RES)
    Q_obs = community_louvain.modularity(partition, G, weight="weight")
    n_comm = len(set(partition.values()))
    # Only consider communities with > 1 node (isolated nodes form singletons)
    comm_sizes = defaultdict(int)
    for v_idx, c in partition.items():
        comm_sizes[c] += 1
    nontrivial = sum(1 for s in comm_sizes.values() if s > 1)
    print(f"  modularity Q = {Q_obs:.4f}", flush=True)
    print(f"  communities total: {n_comm}; non-trivial (size>1): {nontrivial}", flush=True)

    # --- Null: degree-preserving rewire ---
    print(f"Null model: degree-preserving rewiring x {NULL_ITERS}...", flush=True)
    # Reduced graph: only nodes with degree > 0 (rewire ignores isolates)
    # Compute on induced subgraph of edges
    G_conn = G.edge_subgraph(G.edges()).copy()
    null_Q = []
    n_swap_per_iter = max(10 * G_conn.number_of_edges(), 100)
    null_iters_actual = NULL_ITERS
    for it in range(NULL_ITERS):
        if time.time() - t0 > TIME_CAP_SECONDS * 0.6 and it >= 20:
            print(f"  [time-cap] stopping null at iter {it}", flush=True)
            null_iters_actual = it
            break
        G_null = G_conn.copy()
        try:
            nx.double_edge_swap(G_null, nswap=n_swap_per_iter, max_tries=n_swap_per_iter * 10, seed=SEED + it)
        except nx.NetworkXAlgorithmError:
            pass
        p_null = community_louvain.best_partition(G_null, weight="weight",
                                                    random_state=SEED + it, resolution=LOUVAIN_RES)
        Q_null = community_louvain.modularity(p_null, G_null, weight="weight")
        null_Q.append(Q_null)
        if it % 10 == 0:
            print(f"    iter {it}: Q_null={Q_null:.4f}", flush=True)
    null_Q = np.array(null_Q)
    z_Q = (Q_obs - null_Q.mean()) / (null_Q.std() + 1e-12) if len(null_Q) else float("nan")
    print(f"  null mean Q = {null_Q.mean():.4f} +/- {null_Q.std():.4f}", flush=True)
    print(f"  z(Q_obs vs null) = {z_Q:.2f}", flush=True)

    # --- T2: within-partition edge fractions ---
    idx_to_v = {v["idx"]: v for v in verses}
    def _classify_edges(graph):
        within_surah = 0
        within_juz = 0
        within_muf = 0
        total = 0
        for u, v in graph.edges():
            total += 1
            su, vu = idx_to_v[u]["surah"], idx_to_v[u]["verse"]
            sv, vv = idx_to_v[v]["surah"], idx_to_v[v]["verse"]
            if su == sv:
                within_surah += 1
            if juz_of(su, vu) == juz_of(sv, vv):
                within_juz += 1
            if mufassal_tier(su) == mufassal_tier(sv):
                within_muf += 1
        return within_surah / total, within_juz / total, within_muf / total, total

    obs_s, obs_j, obs_m, total_e = _classify_edges(G_conn)
    print(f"Edge within-surah fraction: {obs_s:.4f}", flush=True)
    print(f"Edge within-juz   fraction: {obs_j:.4f}", flush=True)
    print(f"Edge within-mufassal fraction: {obs_m:.4f}", flush=True)
    print(f"Total edges classified: {total_e}", flush=True)

    # Null for T2: use the edge-rewired graphs we already created
    # (re-do quickly since we didn't store them — do 50 fresh)
    null_frac_s = []
    null_frac_j = []
    null_frac_m = []
    NT2 = 50
    for it in range(NT2):
        if time.time() - t0 > TIME_CAP_SECONDS * 0.85:
            print(f"  [time-cap] stopping T2 null at iter {it}", flush=True)
            NT2 = it
            break
        G_null = G_conn.copy()
        try:
            nx.double_edge_swap(G_null, nswap=n_swap_per_iter, max_tries=n_swap_per_iter * 10, seed=SEED * 2 + it)
        except nx.NetworkXAlgorithmError:
            pass
        s, j, m, _ = _classify_edges(G_null)
        null_frac_s.append(s); null_frac_j.append(j); null_frac_m.append(m)
    null_frac_s = np.array(null_frac_s); null_frac_j = np.array(null_frac_j); null_frac_m = np.array(null_frac_m)
    def _z(obs, null):
        if len(null) == 0: return float("nan"), float("nan"), float("nan")
        return (obs - null.mean()) / (null.std() + 1e-12), null.mean(), null.std()
    z_s, mu_s, sd_s = _z(obs_s, null_frac_s)
    z_j, mu_j, sd_j = _z(obs_j, null_frac_j)
    z_m, mu_m, sd_m = _z(obs_m, null_frac_m)
    print(f"  within-surah: z={z_s:.2f} (null mu={mu_s:.4f} sd={sd_s:.4f})", flush=True)
    print(f"  within-juz:   z={z_j:.2f} (null mu={mu_j:.4f} sd={sd_j:.4f})", flush=True)
    print(f"  within-muf:   z={z_m:.2f} (null mu={mu_m:.4f} sd={sd_m:.4f})", flush=True)

    # MW-5 cheat control: shuffle verse-to-surah labels and recompute within-surah
    rng = np.random.RandomState(SEED + 999)
    shuffled_surahs = [v["surah"] for v in verses]
    rng.shuffle(shuffled_surahs)
    shuf_idx_to_surah = {v["idx"]: shuffled_surahs[i] for i, v in enumerate(verses)}
    def _within_shuffled(graph, idx_to_surah_shuf):
        w, t = 0, 0
        for u, v in graph.edges():
            t += 1
            if idx_to_surah_shuf[u] == idx_to_surah_shuf[v]:
                w += 1
        return w / t
    obs_s_shuf = _within_shuffled(G_conn, shuf_idx_to_surah)
    print(f"MW-5 cheat control (shuffled-surah labels): within-surah fraction {obs_s_shuf:.4f} (should be near chance)", flush=True)

    # --- S3: long-arc cross-surah edges matching ring-topology ---
    # Define "long arc" = cross-surah with |s1 - s2| >= 50 (front-to-back)
    long_arc = 0
    front_back_edges = []
    for u, v, d in G_conn.edges(data=True):
        su = idx_to_v[u]["surah"]; sv = idx_to_v[v]["surah"]
        if abs(su - sv) >= 50:
            long_arc += 1
            front_back_edges.append((idx_to_v[u], idx_to_v[v], d.get("weight", 0)))
    print(f"S3: long-arc (|surah_diff| >= 50) edges: {long_arc}", flush=True)

    # --- S4: top-5 highest-sim BEYOND H-NEW-210 top-50 ---
    # Load H-NEW-210 top-50 keys
    import csv
    top50_keys = set()
    with open(OUTDIR / "h-new-210-top50.csv") as f:
        r = csv.DictReader(f)
        for row in r:
            a = (int(row["s1"]), int(row["v1"]))
            b = (int(row["s2"]), int(row["v2"]))
            key = tuple(sorted([a, b]))
            top50_keys.add(key)

    # Sort edges by sim desc
    all_ranked = []
    for u, v, data in G_conn.edges(data=True):
        a = (idx_to_v[u]["surah"], idx_to_v[u]["verse"])
        b = (idx_to_v[v]["surah"], idx_to_v[v]["verse"])
        key = tuple(sorted([a, b]))
        if key in top50_keys:
            continue
        # Cross-surah only (match H-NEW-210 protocol)
        if a[0] == b[0]:
            continue
        all_ranked.append((data["weight"], data.get("lev", -1), idx_to_v[u], idx_to_v[v]))
    all_ranked.sort(key=lambda x: (-x[0], x[1]))
    top5_beyond = all_ranked[:5]

    # Community theme sampling: 5 largest nontrivial communities
    comm_nodes = defaultdict(list)
    for v_idx, c in partition.items():
        comm_nodes[c].append(v_idx)
    comm_sorted = sorted(comm_nodes.items(), key=lambda x: -len(x[1]))
    # Restrict to communities appearing in G_conn (have edges)
    connected_nodes = set(G_conn.nodes())
    comm_sorted = [(c, [n for n in ns if n in connected_nodes]) for c, ns in comm_sorted]
    comm_sorted = [x for x in comm_sorted if len(x[1]) >= 2]
    top_communities = comm_sorted[:5]

    # Write out summary JSON
    summary = {
        "seed": SEED,
        "corpus_n_verses": len(verses),
        "candidate_pairs": len(cands),
        "edges_high_sim": len(edges),
        "graph_nodes": G.number_of_nodes(),
        "graph_edges": G.number_of_edges(),
        "connected_graph_nodes": G_conn.number_of_nodes(),
        "modularity_obs": Q_obs,
        "modularity_null_mean": float(null_Q.mean()) if len(null_Q) else None,
        "modularity_null_std": float(null_Q.std()) if len(null_Q) else None,
        "modularity_z": float(z_Q) if len(null_Q) else None,
        "null_iters": null_iters_actual,
        "n_communities_total": n_comm,
        "n_nontrivial_communities": nontrivial,
        "within_surah_obs": obs_s,
        "within_juz_obs": obs_j,
        "within_mufassal_obs": obs_m,
        "within_surah_null_mean": float(null_frac_s.mean()) if len(null_frac_s) else None,
        "within_juz_null_mean": float(null_frac_j.mean()) if len(null_frac_j) else None,
        "within_mufassal_null_mean": float(null_frac_m.mean()) if len(null_frac_m) else None,
        "within_surah_z": float(z_s) if len(null_frac_s) else None,
        "within_juz_z": float(z_j) if len(null_frac_j) else None,
        "within_mufassal_z": float(z_m) if len(null_frac_m) else None,
        "within_surah_mw5_shuffle": obs_s_shuf,
        "long_arc_edges": long_arc,
        "elapsed_seconds": time.time() - t0,
    }
    out_json = OUTDIR / "h-new-235-summary.json"
    with open(out_json, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary -> {out_json}", flush=True)

    # Top-5 beyond
    print("\nTOP-5 beyond H-NEW-210:", flush=True)
    for i, (sim, d, vi, vj) in enumerate(top5_beyond, 1):
        print(f"  {i}. sim={sim:.4f} d={d}  Q{vi['surah']}:{vi['verse']} <-> Q{vj['surah']}:{vj['verse']}", flush=True)
        print(f"     {vi['text']}", flush=True)
        print(f"     {vj['text']}", flush=True)

    # Write top-5 CSV
    top5_csv = OUTDIR / "h-new-235-top5-beyond-210.csv"
    with open(top5_csv, "w") as f:
        f.write("rank,sim,lev_distance,s1,v1,s2,v2,text1,text2\n")
        for i, (sim, d, vi, vj) in enumerate(top5_beyond, 1):
            t1 = vi['text'].replace(",", " ")
            t2 = vj['text'].replace(",", " ")
            f.write(f"{i},{sim:.4f},{d},{vi['surah']},{vi['verse']},{vj['surah']},{vj['verse']},{t1},{t2}\n")
    print(f"Top-5 CSV -> {top5_csv}", flush=True)

    # Dump top-community sample (IDs + surahs)
    comm_sample = []
    for c, ns in top_communities:
        surahs = sorted({idx_to_v[n]["surah"] for n in ns})
        example_verses = [(idx_to_v[n]["surah"], idx_to_v[n]["verse"], idx_to_v[n]["text"][:60]) for n in ns[:5]]
        comm_sample.append({
            "community_id": c,
            "size": len(ns),
            "surahs_spanned": surahs,
            "example_verses": example_verses,
        })
    comm_json = OUTDIR / "h-new-235-top-communities.json"
    with open(comm_json, "w") as f:
        json.dump(comm_sample, f, indent=2, ensure_ascii=False)
    print(f"Top communities -> {comm_json}", flush=True)

    # Save full edge-list as CSV (compact)
    edges_csv = OUTDIR / "h-new-235-edges.csv"
    with open(edges_csv, "w") as f:
        f.write("s1,v1,s2,v2,sim,lev\n")
        for u, v, d in G_conn.edges(data=True):
            a = (idx_to_v[u]["surah"], idx_to_v[u]["verse"])
            b = (idx_to_v[v]["surah"], idx_to_v[v]["verse"])
            if a > b:
                a, b = b, a
            f.write(f"{a[0]},{a[1]},{b[0]},{b[1]},{d.get('weight',0):.4f},{d.get('lev',-1)}\n")
    print(f"Full edges CSV -> {edges_csv}", flush=True)

    print(f"\nDONE in {time.time()-t0:.1f} sec", flush=True)

    # Decision rule evaluation
    T1_pass = (Q_obs > 0.3) and (z_Q > 1.96 if not np.isnan(z_Q) else False)
    T2_any = any(z > 1.96 for z in [z_s, z_j, z_m] if not np.isnan(z))
    zs = [z for z in [z_s, z_j, z_m] if not np.isnan(z)]
    import math
    stouffer = sum(zs) / math.sqrt(len(zs)) if zs else float("nan")
    T2_pass = T2_any and (stouffer > 1.96)
    overall = "PASS" if (T1_pass and T2_pass) else ("PASS-DIRECTED" if T1_pass else ("DIRECTED-T2" if T2_pass else "NULL-CONSISTENT"))
    print(f"\nT1 (modularity > 0.3 AND z > 1.96): {T1_pass}  (Q={Q_obs:.4f}, z={z_Q:.2f})")
    print(f"T2 (any within-partition z > 1.96 AND Stouffer > 1.96): {T2_pass}  (Stouffer={stouffer:.2f})")
    print(f"OVERALL VERDICT: {overall}")


if __name__ == "__main__":
    main()
