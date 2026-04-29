#!/usr/bin/env python3
"""H-NEW-258 — Cross-corpus replication of H-NEW-236 M_H scaffold logic on Bukhari.

This script intentionally inherits the exact Bukhari segmentation/order
instrument used in the on-disk H-NEW-147 file lineage (whose JSON id is
`h-new-145`): split `bukhari-noquran.txt` on `باب`, tokenize on whitespace,
sort segments by token count descending, retain the top 114 in that retained
order, light-stem, build a top-500-root Fisher-Rao distance matrix, and then
test whether top-K preserved canonical consecutive edges make the inherited
canonical order generatively typical under a constrained local-search family.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import re
import statistics
from collections import Counter
from pathlib import Path

SEED = 20260424
K_GRID = [0, 15, 30, 50, 100]
PRIMARY_KS = [15, 30, 50, 100]
K_TOP_ROOTS = 500
DIRICHLET_ALPHA = 0.5
N_SIM = 300
N_LOCAL_ITERS = 350
T_HOT = 0.05
T_COLD = 0.001
N_CONTROL_RESTARTS = 10
CONTROL_TOLERANCE = 0.5

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
BUKHARI_TXT = PROJECT_ROOT / "data/baseline-corpora/raw/bukhari-noquran.txt"
PREREG = PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-258-bukhari-mh-replication-prereg.md"
H147_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-147.json"
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-258.json"

STRIP_PREFIXES = ["ال", "وال", "بال", "فال", "كال", "لل", "و", "ف", "ل", "ب", "ك", "س"]
STRIP_SUFFIXES = ["ون", "ين", "ان", "ات", "ها", "هم", "هن", "كم", "كن", "نا", "تم", "تن", "ة", "ه", "ي", "ا", "ت", "ن"]
DIACRITIC_RE = re.compile(r"[\u06D6-\u06DF\u0610-\u061A\u0615-\u061A\u064B-\u065F\u0670]+")


def prereg_sha256() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def light_stem(token: str) -> str:
    t = token
    if len(t) < 3:
        return t
    for prefix in sorted(STRIP_PREFIXES, key=lambda x: -len(x)):
        if len(t) > len(prefix) + 2 and t.startswith(prefix):
            t = t[len(prefix) :]
            break
    for suffix in sorted(STRIP_SUFFIXES, key=lambda x: -len(x)):
        if len(t) > len(suffix) + 2 and t.endswith(suffix):
            t = t[: -len(suffix)]
            break
    return t


def load_bukhari_segments() -> list[list[str]]:
    """Exact inherited H-NEW-147 segmentation/order instrument."""
    text = BUKHARI_TXT.read_text(encoding="utf-8")
    text = DIACRITIC_RE.sub("", text)
    segments = re.split(r"\bباب\b", text)
    seg_tokens = [segment.split() for segment in segments if segment.strip()]
    seg_tokens.sort(key=len, reverse=True)
    return seg_tokens[:114]


def build_distribution_matrix(corpus_tokens: list[list[str]], k_top: int = K_TOP_ROOTS) -> list[list[float]]:
    stemmed = [[light_stem(token) for token in segs] for segs in corpus_tokens]
    global_freq: Counter[str] = Counter()
    for segs in stemmed:
        global_freq.update(segs)
    top_k = [root for root, _ in global_freq.most_common(k_top)]
    top_k_index = {root: idx for idx, root in enumerate(top_k)}

    n_segments = len(stemmed)
    mat = [[DIRICHLET_ALPHA] * k_top for _ in range(n_segments)]
    for idx, segs in enumerate(stemmed):
        for token in segs:
            if token in top_k_index:
                mat[idx][top_k_index[token]] += 1.0
    for idx in range(n_segments):
        total = sum(mat[idx])
        mat[idx] = [x / total for x in mat[idx]]
    return mat


def fisher_rao(p: list[float], q: list[float]) -> float:
    score = 0.0
    for pk, qk in zip(p, q):
        score += math.sqrt(pk * qk)
    score = max(-1.0, min(1.0, score))
    return 2.0 * math.acos(score)


def build_distance_matrix(dist_mat: list[list[float]]) -> list[list[float]]:
    n = len(dist_mat)
    dmat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = fisher_rao(dist_mat[i], dist_mat[j])
            dmat[i][j] = dist
            dmat[j][i] = dist
    return dmat


def path_length(order: list[int], dmat: list[list[float]]) -> float:
    return sum(dmat[order[i]][order[i + 1]] for i in range(len(order) - 1))


def two_opt_path(tour: list[int], dmat: list[list[float]], patience: int = 100) -> tuple[list[int], float]:
    """Exact H-NEW-147-style open-path 2-opt, reused only for control reproduction."""
    best = list(tour)
    n = len(best)
    best_length = path_length(best, dmat)
    iters_no_improve = 0
    while iters_no_improve < patience:
        improved = False
        for i in range(n - 1):
            for j in range(i + 2, n):
                if j == n - 1 and i == 0:
                    continue
                a, b = best[i], best[i + 1]
                old_cost = dmat[a][b]
                if j + 1 < n:
                    c, d = best[j], best[j + 1]
                    old_cost += dmat[c][d]
                    new_cost = dmat[a][c] + dmat[b][d]
                else:
                    c = best[j]
                    new_cost = dmat[a][c]
                delta = new_cost - old_cost
                if delta < -1e-10:
                    best[i + 1 : j + 1] = best[i + 1 : j + 1][::-1]
                    best_length += delta
                    improved = True
        iters_no_improve = 0 if improved else iters_no_improve + 1
    return best, best_length


def canonical_edge_ranking(dmat: list[list[float]]) -> list[dict]:
    rows: list[dict] = []
    for idx in range(113):
        rows.append(
            {
                "rank": None,
                "a": idx,
                "b": idx + 1,
                "a_1indexed": idx + 1,
                "b_1indexed": idx + 2,
                "distance": float(dmat[idx][idx + 1]),
            }
        )
    rows.sort(key=lambda row: row["distance"], reverse=True)
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    return rows


def build_hinge_chains(n_nodes: int, hinge_edges: list[tuple[int, int]]) -> list[list[int]]:
    succ: dict[int, int] = {}
    pred: dict[int, int] = {}
    for a, b in hinge_edges:
        if a in succ:
            raise AssertionError(f"Node {a} has two successors")
        if b in pred:
            raise AssertionError(f"Node {b} has two predecessors")
        succ[a] = b
        pred[b] = a

    chains: list[list[int]] = []
    visited: set[int] = set()
    for node in range(n_nodes):
        if node in visited or node in pred:
            continue
        chain = [node]
        visited.add(node)
        cur = node
        while cur in succ:
            nxt = succ[cur]
            chain.append(nxt)
            visited.add(nxt)
            cur = nxt
        chains.append(chain)

    for node in range(n_nodes):
        if node not in visited:
            chains.append([node])
            visited.add(node)

    # Preserve canonical chain order as the reference order.
    chains.sort(key=lambda chain: chain[0])
    return chains


def chain_internal_cost(chain: list[int], dmat: list[list[float]]) -> float:
    if len(chain) < 2:
        return 0.0
    return sum(dmat[chain[i]][chain[i + 1]] for i in range(len(chain) - 1))


def chain_order_cost(order: list[int], chains: list[list[int]], dmat: list[list[float]]) -> float:
    total = 0.0
    for idx in order:
        total += chain_internal_cost(chains[idx], dmat)
    for left_idx, right_idx in zip(order, order[1:]):
        left_tail = chains[left_idx][-1]
        right_head = chains[right_idx][0]
        total += dmat[left_tail][right_head]
    return total


def optimize_chain_order(chains: list[list[int]], dmat: list[list[float]], rng: random.Random) -> tuple[list[int], float]:
    m = len(chains)
    order = list(range(m))
    rng.shuffle(order)
    current = list(order)
    current_cost = chain_order_cost(current, chains, dmat)
    best = list(current)
    best_cost = current_cost

    if m < 2:
        return best, best_cost

    for step in range(N_LOCAL_ITERS):
        frac = step / max(1, N_LOCAL_ITERS - 1)
        temperature = T_HOT + frac * (T_COLD - T_HOT)
        i, j = sorted(rng.sample(range(m), 2))
        proposal = current[:i] + current[i : j + 1][::-1] + current[j + 1 :]
        proposal_cost = chain_order_cost(proposal, chains, dmat)
        delta = proposal_cost - current_cost
        accept = delta < 0
        if not accept and temperature > 1e-9:
            ratio = delta / temperature
            p_accept = math.exp(-ratio) if ratio < 50 else 0.0
            accept = rng.random() < p_accept
        if accept:
            current = proposal
            current_cost = proposal_cost
            if current_cost < best_cost:
                best = list(current)
                best_cost = current_cost

    return best, best_cost


def flatten_chain_order(order: list[int], chains: list[list[int]]) -> list[int]:
    out: list[int] = []
    for idx in order:
        out.extend(chains[idx])
    return out


def percentile_of(value: float, distribution: list[float]) -> float:
    count = sum(1 for x in distribution if x <= value)
    return 100.0 * count / len(distribution)


def quantile(xs: list[float], q: float) -> float:
    if not xs:
        raise ValueError("empty distribution")
    ys = sorted(xs)
    pos = q * (len(ys) - 1)
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return ys[lo]
    frac = pos - lo
    return ys[lo] * (1.0 - frac) + ys[hi] * frac


def load_parent_reference() -> dict:
    with H147_JSON.open() as f:
        data = json.load(f)
    return {
        "L_canonical": float(data["bukhari"]["L_canonical"]),
        "L_2opt": float(data["bukhari"]["L_2opt"]),
        "R": float(data["bukhari"]["R"]),
        "z_score": float(data["bukhari"]["z_score"]),
    }


def reproduce_h147_control(dmat: list[list[float]]) -> dict:
    canonical = list(range(len(dmat)))
    l_canonical = path_length(canonical, dmat)
    best_length = float("inf")
    for restart in range(N_CONTROL_RESTARTS):
        rng = random.Random(SEED + 7000 + restart)
        init = list(range(len(dmat)))
        if restart > 0:
            rng.shuffle(init)
        _, refined = two_opt_path(init, dmat)
        best_length = min(best_length, refined)
    parent = load_parent_reference()
    return {
        "recomputed_L_canonical": l_canonical,
        "recomputed_L_2opt_best10": best_length,
        "parent_L_canonical": parent["L_canonical"],
        "parent_L_2opt": parent["L_2opt"],
        "delta_L_canonical": l_canonical - parent["L_canonical"],
        "delta_L_2opt": best_length - parent["L_2opt"],
        "pass": abs(l_canonical - parent["L_canonical"]) <= CONTROL_TOLERANCE
        and abs(best_length - parent["L_2opt"]) <= CONTROL_TOLERANCE,
    }


def run_cell(k: int, ranked_edges: list[dict], dmat: list[list[float]], empirical_l_path: float, baseline_gap: float | None) -> dict:
    hinge_edges = [(row["a"], row["b"]) for row in ranked_edges[:k]]
    chains = build_hinge_chains(len(dmat), hinge_edges)
    samples: list[float] = []
    sample_orders: list[list[int]] = []
    for sim_idx in range(N_SIM):
        rng = random.Random(SEED + k * 1000 + sim_idx)
        best_chain_order, best_cost = optimize_chain_order(chains, dmat, rng)
        samples.append(best_cost)
        if sim_idx < 3:
            sample_orders.append(flatten_chain_order(best_chain_order, chains))

    sim_mean = statistics.mean(samples)
    sim_sd = statistics.pstdev(samples) if len(samples) > 1 else 0.0
    ci_low = quantile(samples, 0.025)
    ci_high = quantile(samples, 0.975)
    pct = percentile_of(empirical_l_path, samples)
    gap = empirical_l_path - sim_mean
    closure_pct = None
    if baseline_gap is not None and baseline_gap != 0:
        closure_pct = 100.0 * (baseline_gap - gap) / baseline_gap

    if empirical_l_path < ci_low:
        status = "OPEN-LOW"
    elif empirical_l_path > ci_high:
        status = "OPEN-HIGH"
    else:
        status = "CLOSED"

    return {
        "K": k,
        "n_hinges": k,
        "chain_count": len(chains),
        "free_chain_boundaries": max(0, len(chains) - 1),
        "hinges_1indexed": [(a + 1, b + 1) for a, b in hinge_edges],
        "sim_n": N_SIM,
        "L_path": {
            "empirical": empirical_l_path,
            "sim_mean": sim_mean,
            "sim_sd": sim_sd,
            "sim_ci_95": [ci_low, ci_high],
            "empirical_percentile": pct,
            "empirical_inside_ci": ci_low <= empirical_l_path <= ci_high,
            "mean_gap_emp_minus_sim": gap,
            "closure_pct_vs_k0_mean_gap": closure_pct,
            "min_sample": min(samples),
            "max_sample": max(samples),
        },
        "verdict": status,
        "sample_orders_preview_1indexed": [[node + 1 for node in order] for order in sample_orders],
    }


def overall_verdict(cells: dict[str, dict]) -> tuple[str, int | None]:
    first_closing = None
    for k in PRIMARY_KS:
        if cells[f"K{k}"]["verdict"] == "CLOSED":
            first_closing = k
            break
    if cells["K100"]["verdict"] != "CLOSED":
        return "NO-ANALOGUE", first_closing
    if first_closing is not None and first_closing <= 50:
        return "LOOSE-ANALOGUE", first_closing
    return "HIGH-DENSITY-ANALOGUE", first_closing


def main() -> None:
    segments = load_bukhari_segments()
    if len(segments) != 114:
        raise AssertionError(f"Expected 114 retained segments, got {len(segments)}")

    dist_mat = build_distribution_matrix(segments, K_TOP_ROOTS)
    dmat = build_distance_matrix(dist_mat)
    empirical_order = list(range(len(dmat)))
    empirical_l_path = path_length(empirical_order, dmat)

    control = reproduce_h147_control(dmat)
    ranked_edges = canonical_edge_ranking(dmat)

    cells: dict[str, dict] = {}
    baseline_gap = None
    for k in K_GRID:
        cell = run_cell(k, ranked_edges, dmat, empirical_l_path, baseline_gap)
        cells[f"K{k}"] = cell
        if k == 0:
            baseline_gap = cell["L_path"]["mean_gap_emp_minus_sim"]

    verdict, first_closing = overall_verdict(cells)
    parent = load_parent_reference()

    output = {
        "finding_id": "h-new-258",
        "title": "Bukhari M_H replication on the H-147 instrument",
        "seed": SEED,
        "pre_reg_sha256": prereg_sha256(),
        "parents": {
            "h_new_147_file_lineage": "findings/phase-b-hypotheses/h-new-147-bukhari-cross-corpus.md",
            "h_new_147_on_disk_json_id": "h-new-145",
            "h_new_236_1b": "findings/phase-b-hypotheses/h-new-236-1b-mufassal-terminal-mechanism.md",
        },
        "instrument_disclosure": {
            "inherits_h147_length_sorted_retained_order": True,
            "inherits_h147_finding_id_mismatch": True,
            "segment_selection": "Split on literal باب, sort by token count descending, retain top 114 in that post-sort order.",
        },
        "control_reproduction": control,
        "parent_reference": parent,
        "bukhari_retained_segment_token_lengths": [len(seg) for seg in segments],
        "empirical_L_path": empirical_l_path,
        "canonical_edge_ranking_top20": [
            {
                "rank": row["rank"],
                "edge_1indexed": [row["a_1indexed"], row["b_1indexed"]],
                "distance": row["distance"],
            }
            for row in ranked_edges[:20]
        ],
        "cells": cells,
        "primary_ks": PRIMARY_KS,
        "overall_verdict": verdict,
        "first_closing_k": first_closing,
        "k100_closes": cells["K100"]["verdict"] == "CLOSED",
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(json.dumps(
        {
            "control_pass": control["pass"],
            "empirical_L_path": empirical_l_path,
            "overall_verdict": verdict,
            "first_closing_k": first_closing,
            "k100_status": cells["K100"]["verdict"],
        },
        indent=2,
        ensure_ascii=False,
    ))


if __name__ == "__main__":
    main()
