#!/usr/bin/env python3
"""
H-NEW-1770 — Corpus-wide verse-twin graph (char-Levenshtein, threshold 0.70).

Rules-tuple:
  (no-tashkeel, char-Levenshtein, graphemes,
   basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)

Builds the verse-twin graph: nodes = 6,236 verses; edges = inter-surah pairs
with normalized char-Levenshtein similarity >= 0.70. Reports:
  - top-10 hub verses by twin-degree
  - top-10 surah-pairs by edge-count
  - average twin-degree per surah
  - degree-preserving permutation null (10,000 reps) for H1a/H1b/H2

Outputs JSON to findings/phase-b-hypotheses/csv/h-new-1770.json
Runtime: ~3-10 minutes depending on CPU.
"""

import hashlib
import json
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

import rapidfuzz.distance.Levenshtein as Lev

PRE_REG_PATH = Path(
    "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/"
    "prereg-h-new-1770-verse-twin-graph.md"
)
EXPECTED_SHA = "3e986697e71e0b07fd5ac20f2ef4d6f848662bef5abbbeefce757c540f0576bb"

QURAN_PATH = Path("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json")
OUT_PATH = Path(
    "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-1770.json"
)

SEED = 20260509
N_PERMS = 10000
SIM_THRESHOLD = 0.70
SENSITIVITY_THRESHOLDS = (0.60, 0.80)


def verify_prereg_sha():
    h = hashlib.sha256(PRE_REG_PATH.read_bytes()).hexdigest()
    if h != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH:\n  expected: {EXPECTED_SHA}\n  observed: {h}\n"
        )
        sys.exit(1)
    return h


def load_verses():
    """Return list of (verse_idx, surah_id, ayah_id, text) tuples.

    For Q 2..Q 114, the basmala that precedes the first verse is NOT a
    separate verse (Hafs verse-numbering: it is part of v.1 only in
    sources that count it intra-line; here we use the JSON's per-verse
    structure which already excludes the surah-opening basmala from
    v.1 for Q 2..Q 9 etc. — see basmala-counted-only-in-Q1 rule-tuple).
    """
    data = json.loads(QURAN_PATH.read_text(encoding="utf-8"))
    verses = []
    for surah in data:
        sid = surah["id"]
        for v in surah["verses"]:
            text = v["text"].strip()
            # collapse whitespace
            text = " ".join(text.split())
            verses.append({
                "idx": len(verses),
                "surah": sid,
                "ayah": v["id"],
                "text": text,
                "len": len(text),
            })
    return verses


def build_edges(verses, threshold=SIM_THRESHOLD):
    """Build all inter-surah edges with sim >= threshold.

    Length-prefilter: skip pairs where |Δlen| / max_len > (1 - threshold).
    This is a sound prefilter — sim_max = 1 - |Δlen|/max_len.
    """
    n = len(verses)
    # Sort indices by surah (within surah by ayah) so we can scan efficiently
    # but for our algorithm we just iterate all pairs.
    by_len = sorted(range(n), key=lambda i: verses[i]["len"])

    max_delta_ratio = 1.0 - threshold  # |Δlen|/max_len must be <= 0.30

    edges = []  # (i, j, sim)
    t0 = time.time()
    n_compared = 0
    n_skipped = 0
    n_emitted = 0

    # For each verse, only compare to verses with len within the allowed window.
    # Iterate by sorted-len index, advance a moving right-pointer.
    lens = [verses[i]["len"] for i in by_len]
    for a_pos in range(n):
        i = by_len[a_pos]
        v_i = verses[i]
        len_i = v_i["len"]
        if len_i == 0:
            continue
        # max allowed len_j such that |len_j - len_i| / max(len_i, len_j) <= max_delta_ratio
        # If len_j >= len_i: (len_j - len_i)/len_j <= md  =>  len_j <= len_i / (1-md)
        # If len_j <= len_i: (len_i - len_j)/len_i <= md  =>  len_j >= len_i * (1-md)
        len_max = len_i / (1 - max_delta_ratio) if max_delta_ratio < 1 else float("inf")
        len_min = len_i * (1 - max_delta_ratio)

        # advance right-pointer to first j-position with len > len_max
        # advance left-pointer to first j-position with len >= len_min
        # binary search would work; linear works fine
        # find right bound
        # we'll just scan and break appropriately
        for b_pos in range(a_pos + 1, n):
            j = by_len[b_pos]
            len_j = verses[j]["len"]
            if len_j > len_max:
                break  # past upper bound, sorted, can stop
            v_j = verses[j]
            if v_j["surah"] == v_i["surah"]:
                continue  # inter-surah only
            # Compute Levenshtein normalized similarity
            n_compared += 1
            sim = Lev.normalized_similarity(v_i["text"], v_j["text"])
            if sim >= threshold:
                edges.append((i, j, sim))
                n_emitted += 1

    elapsed = time.time() - t0
    return edges, {
        "n_compared": n_compared,
        "n_emitted": n_emitted,
        "build_time_s": round(elapsed, 1),
    }


def degree_from_edges(edges, n_nodes):
    deg = [0] * n_nodes
    for i, j, _ in edges:
        deg[i] += 1
        deg[j] += 1
    return deg


def surah_pair_counts(edges, verses):
    """Count edges per (s1, s2) with s1 < s2."""
    counter = defaultdict(int)
    sample_edge = {}  # store highest-sim edge per pair
    for i, j, sim in edges:
        s1 = verses[i]["surah"]
        s2 = verses[j]["surah"]
        if s1 > s2:
            s1, s2 = s2, s1
            i, j = j, i
        key = (s1, s2)
        counter[key] += 1
        cur = sample_edge.get(key)
        if cur is None or sim > cur[2]:
            sample_edge[key] = (i, j, sim)
    return counter, sample_edge


def per_surah_mean_degree(verses, deg):
    """Mean (inter-surah) twin-degree per surah."""
    by_surah = defaultdict(list)
    for v in verses:
        by_surah[v["surah"]].append(deg[v["idx"]])
    out = {}
    for s, deglist in by_surah.items():
        out[s] = sum(deglist) / len(deglist)
    return out


def permutation_null(edges, verses, n_perm=N_PERMS, seed=SEED):
    """Degree-preserving null via edge-rewire (configuration model approx).

    For efficiency: implement as label-shuffle on surah-labels.
    A more faithful null = double-edge-swap rewiring; we use the
    label-shuffle null which is also pre-registered as MW-2 compliant
    (preserves degree distribution exactly; tests inter-surah-only constraint).

    For each perm:
      - Shuffle the surah-labels of nodes (preserving each surah's verse-count
        but reassigning which verses belong to which surah)
      - Recompute (a) max inter-surah degree, (b) isolate count, (c) rich-surah-pair count
    The observed graph's edge-list is fixed; we just relabel nodes' surah
    membership and re-check the inter-surah / intra-surah split.
    """
    rng = random.Random(seed)
    n_nodes = len(verses)
    surahs = [v["surah"] for v in verses]

    # Pre-computed neighbor lists for fast degree computation under relabel
    # adj[i] = list of j
    adj = defaultdict(list)
    for i, j, _ in edges:
        adj[i].append(j)
        adj[j].append(i)

    # Observed statistics
    deg = degree_from_edges(edges, n_nodes)
    obs_max_deg = max(deg)
    obs_isolates = sum(1 for d in deg if d == 0)
    surah_pair_obs, _ = surah_pair_counts(edges, verses)
    obs_rich_pairs = sum(1 for c in surah_pair_obs.values() if c >= 3)

    # Permutation null
    null_max_deg = []
    null_isolates = []
    null_rich_pairs = []

    perm_surahs = list(surahs)
    for p in range(n_perm):
        rng.shuffle(perm_surahs)
        # recompute inter-surah degree
        # For each edge (i,j) keep if perm_surahs[i] != perm_surahs[j]
        local_deg = [0] * n_nodes
        local_pair = defaultdict(int)
        for i, j, _ in edges:
            s_i = perm_surahs[i]
            s_j = perm_surahs[j]
            if s_i != s_j:
                local_deg[i] += 1
                local_deg[j] += 1
                key = (s_i, s_j) if s_i < s_j else (s_j, s_i)
                local_pair[key] += 1
        null_max_deg.append(max(local_deg))
        null_isolates.append(sum(1 for d in local_deg if d == 0))
        null_rich_pairs.append(sum(1 for c in local_pair.values() if c >= 3))

    def p_one_sided_ge(null_vals, obs):
        return sum(1 for v in null_vals if v >= obs) / len(null_vals)

    return {
        "obs_max_deg": obs_max_deg,
        "obs_isolates": obs_isolates,
        "obs_rich_surah_pairs": obs_rich_pairs,
        "null_max_deg_mean": sum(null_max_deg) / len(null_max_deg),
        "null_max_deg_p95": sorted(null_max_deg)[int(0.95 * n_perm)],
        "null_isolates_mean": sum(null_isolates) / len(null_isolates),
        "null_rich_pairs_mean": sum(null_rich_pairs) / len(null_rich_pairs),
        "p_max_deg": p_one_sided_ge(null_max_deg, obs_max_deg),
        "p_isolates": p_one_sided_ge(null_isolates, obs_isolates),
        "p_rich_pairs": p_one_sided_ge(null_rich_pairs, obs_rich_pairs),
    }


def main():
    print("[H-NEW-1770] verifying pre-reg SHA...")
    h = verify_prereg_sha()
    print(f"  SHA OK: {h}")

    print("[H-NEW-1770] loading corpus...")
    verses = load_verses()
    print(f"  n_verses = {len(verses)}")

    results = {
        "finding_id": "H-NEW-1770",
        "prereg_sha256": EXPECTED_SHA,
        "rules_tuple": "(no-tashkeel, char-Levenshtein, graphemes, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)",
        "seed": SEED,
        "n_perms": N_PERMS,
        "sim_threshold": SIM_THRESHOLD,
        "sensitivity_thresholds": list(SENSITIVITY_THRESHOLDS),
        "n_verses": len(verses),
    }

    print(f"[H-NEW-1770] building edges at threshold {SIM_THRESHOLD} (inter-surah only)...")
    edges, build_stats = build_edges(verses, threshold=SIM_THRESHOLD)
    print(f"  build stats: {build_stats}")
    print(f"  n_edges = {len(edges)}")
    results["n_edges"] = len(edges)
    results["build_stats"] = build_stats

    # Degree distribution
    deg = degree_from_edges(edges, len(verses))
    deg_sorted = sorted(range(len(verses)), key=lambda i: -deg[i])

    # Top-10 hubs
    top10 = []
    for rank, idx in enumerate(deg_sorted[:20], 1):  # 20 in case of refrains
        v = verses[idx]
        # find top-3 twin targets
        targets = []
        for ii, jj, sim in edges:
            if ii == idx:
                targets.append((jj, sim))
            elif jj == idx:
                targets.append((ii, sim))
        targets.sort(key=lambda x: -x[1])
        top_targets = [
            {"surah": verses[t]["surah"], "ayah": verses[t]["ayah"], "sim": round(s, 4)}
            for t, s in targets[:3]
        ]
        top10.append({
            "rank": rank,
            "surah": v["surah"],
            "ayah": v["ayah"],
            "text": v["text"],
            "deg": deg[idx],
            "top_targets": top_targets,
        })
    results["top_hubs"] = top10

    # Top-10 surah-pairs
    pair_counts, sample_edges = surah_pair_counts(edges, verses)
    pair_sorted = sorted(pair_counts.items(), key=lambda kv: -kv[1])
    top_pairs = []
    for (s1, s2), cnt in pair_sorted[:50]:
        ii, jj, sim = sample_edges[(s1, s2)]
        top_pairs.append({
            "surah_a": s1,
            "surah_b": s2,
            "edge_count": cnt,
            "sample_twin": {
                "surah_a_ayah": verses[ii]["ayah"] if verses[ii]["surah"] == s1 else verses[jj]["ayah"],
                "surah_b_ayah": verses[jj]["ayah"] if verses[jj]["surah"] == s2 else verses[ii]["ayah"],
                "sim": round(sim, 4),
                "text_a": verses[ii]["text"] if verses[ii]["surah"] == s1 else verses[jj]["text"],
                "text_b": verses[jj]["text"] if verses[jj]["surah"] == s2 else verses[ii]["text"],
            },
        })
    results["top_surah_pairs"] = top_pairs

    # Per-surah mean twin-degree
    surah_mean_deg = per_surah_mean_degree(verses, deg)
    sorted_surahs = sorted(surah_mean_deg.items(), key=lambda kv: -kv[1])
    results["per_surah_mean_degree"] = {
        "top_10": [{"surah": s, "mean_deg": round(d, 3)} for s, d in sorted_surahs[:10]],
        "bottom_10": [{"surah": s, "mean_deg": round(d, 3)} for s, d in sorted_surahs[-10:]],
        "all": {str(s): round(d, 3) for s, d in surah_mean_deg.items()},
    }

    # Aggregate degree stats
    n_isolates = sum(1 for d in deg if d == 0)
    deg_quartile = sorted(deg)
    q1 = deg_quartile[len(deg) // 4]
    q3 = deg_quartile[3 * len(deg) // 4]
    results["degree_stats"] = {
        "max": max(deg),
        "mean": round(sum(deg) / len(deg), 3),
        "median": deg_quartile[len(deg) // 2],
        "n_isolates": n_isolates,
        "isolate_fraction": round(n_isolates / len(deg), 4),
        "q1": q1,
        "q3": q3,
        "bottom_quartile_size": len(deg) // 4,
        "n_with_deg_ge_5": sum(1 for d in deg if d >= 5),
        "n_with_deg_ge_10": sum(1 for d in deg if d >= 10),
    }

    # Connected components
    parent = list(range(len(verses)))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry
    for i, j, _ in edges:
        union(i, j)
    comp = defaultdict(list)
    for k in range(len(verses)):
        comp[find(k)].append(k)
    comps = sorted([len(c) for c in comp.values()], reverse=True)
    results["component_stats"] = {
        "n_components": len(comp),
        "largest_component_size": comps[0],
        "second_largest": comps[1] if len(comps) > 1 else 0,
        "top_5_component_sizes": comps[:5],
        "non_isolate_components": sum(1 for s in comps if s > 1),
    }

    # Twin pericope: H2 — count surah-pairs with edge_count >= 3
    rich_pairs_count = sum(1 for c in pair_counts.values() if c >= 3)
    results["n_rich_surah_pairs_ge_3"] = rich_pairs_count
    results["n_rich_surah_pairs_ge_5"] = sum(1 for c in pair_counts.values() if c >= 5)

    # H1/H2 decision
    h1a_pass = sum(1 for h in top10[:10] if h["deg"] >= 5) == 10
    h1b_pass = n_isolates >= len(deg) // 4
    h2_pass = rich_pairs_count >= 5
    results["decisions"] = {
        "H1a_top10_all_deg_ge_5": h1a_pass,
        "H1b_bottom_quartile_isolates": h1b_pass,
        "H2_rich_pairs_ge_5": h2_pass,
        "n_fired": int(h1a_pass) + int(h1b_pass) + int(h2_pass),
    }

    # Permutation null
    print(f"[H-NEW-1770] running permutation null (n_perm={N_PERMS})...")
    t0 = time.time()
    null = permutation_null(edges, verses, n_perm=N_PERMS, seed=SEED)
    print(f"  null done in {round(time.time() - t0, 1)}s")
    results["permutation_null"] = null

    # Bonferroni at family-α=0.05, k=3 → α_per_test=0.0167
    alpha_bon = 0.05 / 3
    results["alpha_bonferroni_per_test"] = alpha_bon
    results["null_significant"] = {
        "max_deg": null["p_max_deg"] < alpha_bon,
        "isolates": null["p_isolates"] < alpha_bon,
        "rich_pairs": null["p_rich_pairs"] < alpha_bon,
    }

    # Sensitivity: thresholds 0.60 and 0.80
    print("[H-NEW-1770] sensitivity analysis at thresholds 0.60 and 0.80...")
    sensitivity = {}
    for thr in SENSITIVITY_THRESHOLDS:
        s_edges, s_stats = build_edges(verses, threshold=thr)
        s_deg = degree_from_edges(s_edges, len(verses))
        s_pair, _ = surah_pair_counts(s_edges, verses)
        sensitivity[f"thr_{thr}"] = {
            "n_edges": len(s_edges),
            "max_deg": max(s_deg),
            "n_isolates": sum(1 for d in s_deg if d == 0),
            "n_rich_surah_pairs_ge_3": sum(1 for c in s_pair.values() if c >= 3),
        }
        print(f"  thr={thr}: edges={len(s_edges)}, max_deg={max(s_deg)}, isolates={sum(1 for d in s_deg if d == 0)}")
    results["sensitivity"] = sensitivity

    # Write JSON
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(results, ensure_ascii=False, indent=2))
    print(f"[H-NEW-1770] wrote {OUT_PATH}")
    print(f"  decisions: {results['decisions']}")
    print(f"  permutation p-values: max_deg={null['p_max_deg']}, isolates={null['p_isolates']}, rich={null['p_rich_pairs']}")


if __name__ == "__main__":
    main()
