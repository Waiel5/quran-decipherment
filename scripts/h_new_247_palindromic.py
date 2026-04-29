#!/usr/bin/env python3
"""H-NEW-247 — Palindromic surah-pair symmetry test (k paired with 115-k).

Parent: cross-finding-013 (mushaf topological ring, CONFIRMED).
Sibling: H-NEW-204 (reverse-mushaf boundary Spearman secondary NULL).

Four cells, Bonferroni k=4, α_bon = 0.0125, seed 20260419, 1000 perms:
  (a) Fisher-Rao proximity: mean d_FR over 57 palindromic pairs < random
  (b) Shared top-50 roots: mean |roots(i) ∩ roots(j)| > random
  (c) Muqaṭṭaʿāt concordance count > random
  (d) Length-reflection Spearman: corr(log n_v(k), log n_v(115-k)) > random

MW-5: mushaf canonical partition included as sanity anchor (confirms
analytic observed statistic). Null draws randomize pair assignment.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

SEED = 20260419
PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
QAC_FILE = PROJECT_ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN_JSON = PROJECT_ROOT / "quran-text/quran-no-tashkeel.json"
PREREG = PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-247-palindromic-symmetry-prereg.md"
OUTPUT = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-247.json"

N_PERMS = 1000
BONFERRONI_K = 4
ALPHA = 0.05
ALPHA_BON = ALPHA / BONFERRONI_K  # 0.0125

MUQ_SURAHS = frozenset({
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68,
})

PALINDROMIC_PAIRS = [(k, 115 - k) for k in range(1, 58)]  # 57 pairs
assert len(PALINDROMIC_PAIRS) == 57
assert PALINDROMIC_PAIRS[0] == (1, 114)
assert PALINDROMIC_PAIRS[-1] == (57, 58)


# ---------------------------------------------------------------------------
# Load parent Fisher-Rao D matrix (114x114)
# ---------------------------------------------------------------------------
def load_d_matrix() -> dict[tuple[int, int], float]:
    with H_NEW_111_JSON.open() as f:
        parent = json.load(f)
    D: dict[tuple[int, int], float] = {}
    for entry in parent["D_matrix_upper_triangular"]:
        i, j, d = int(entry[0]), int(entry[1]), float(entry[2])
        D[(i, j)] = d
        D[(j, i)] = d
    for i in range(1, 115):
        D[(i, i)] = 0.0
    return D


# ---------------------------------------------------------------------------
# Parse QAC — per-surah root-token lists
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")


def load_per_surah_top_roots(k_top: int = 50) -> dict[int, frozenset[str]]:
    per_surah_counts: dict[int, Counter[str]] = defaultdict(Counter)
    with QAC_FILE.open(encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1))
            feat = parts[3]
            if "STEM" not in feat:
                continue
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            per_surah_counts[sid][rm.group(1)] += 1
    out: dict[int, frozenset[str]] = {}
    for sid in range(1, 115):
        top = [r for r, _ in per_surah_counts[sid].most_common(k_top)]
        out[sid] = frozenset(top)
    return out


def load_surah_lengths() -> dict[int, int]:
    with QURAN_JSON.open() as f:
        q = json.load(f)
    return {s["id"]: len(s["verses"]) for s in q}


# ---------------------------------------------------------------------------
# Cell statistics (applied to a pair-list)
# ---------------------------------------------------------------------------
def stat_a_fr(pairs: list[tuple[int, int]], D: dict) -> float:
    return sum(D[(i, j)] for i, j in pairs) / len(pairs)


def stat_b_shared_roots(
    pairs: list[tuple[int, int]], top_roots: dict[int, frozenset[str]]
) -> float:
    return sum(len(top_roots[i] & top_roots[j]) for i, j in pairs) / len(pairs)


def stat_c_muq_concordance(pairs: list[tuple[int, int]]) -> int:
    n = 0
    for i, j in pairs:
        mi = i in MUQ_SURAHS
        mj = j in MUQ_SURAHS
        if mi == mj:
            n += 1
    return n


def stat_d_spearman_length(
    pairs: list[tuple[int, int]], lengths: dict[int, int]
) -> float:
    xs = [math.log(lengths[i]) for i, _ in pairs]
    ys = [math.log(lengths[j]) for _, j in pairs]
    return spearman_rho(xs, ys)


def spearman_rho(x: list[float], y: list[float]) -> float:
    n = len(x)
    assert n == len(y)

    def ranks(v: list[float]) -> list[float]:
        sorted_idx = sorted(range(n), key=lambda k: v[k])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[sorted_idx[j + 1]] == v[sorted_idx[i]]:
                j += 1
            avg_rank = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                r[sorted_idx[k]] = avg_rank
            i = j + 1
        return r

    rx, ry = ranks(x), ranks(y)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((rx[k] - mx) * (ry[k] - my) for k in range(n))
    dx = math.sqrt(sum((rx[k] - mx) ** 2 for k in range(n)))
    dy = math.sqrt(sum((ry[k] - my) ** 2 for k in range(n)))
    if dx == 0 or dy == 0:
        return 0.0
    return num / (dx * dy)


def random_pairing(rng: random.Random) -> list[tuple[int, int]]:
    surahs = list(range(1, 115))
    rng.shuffle(surahs)
    return [(surahs[i], surahs[i + 1]) for i in range(0, 114, 2)]


def permutation_p_one_sided(null_values: list[float], observed: float, direction: str) -> tuple[float, float]:
    """Return (p, z). direction: 'lower' or 'upper'."""
    n = len(null_values)
    mu = statistics.mean(null_values)
    sd = statistics.stdev(null_values) if n > 1 else 0.0
    z = (observed - mu) / sd if sd > 0 else 0.0
    if direction == "lower":
        n_extreme = sum(1 for v in null_values if v <= observed)
    else:
        n_extreme = sum(1 for v in null_values if v >= observed)
    p = (n_extreme + 1) / (n + 1)
    return p, z


def main() -> None:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    parent_sha = hashlib.sha256(H_NEW_111_JSON.read_bytes()).hexdigest()

    print(f"prereg sha256: {prereg_sha}")
    print(f"parent h-new-111 sha256: {parent_sha}")
    print(f"seed: {SEED}")
    print(f"n_perms: {N_PERMS}")
    print(f"bonferroni_k: {BONFERRONI_K}, alpha_bon: {ALPHA_BON}")

    print("\n[1/4] Loading Fisher-Rao D matrix...")
    D = load_d_matrix()
    n_edges = sum(1 for k in D if k[0] < k[1])
    assert n_edges == 114 * 113 // 2, f"expected 6441, got {n_edges}"

    print("[2/4] Parsing QAC per-surah top-50 roots...")
    top_roots = load_per_surah_top_roots(k_top=50)
    assert len(top_roots) == 114

    print("[3/4] Loading surah lengths...")
    lengths = load_surah_lengths()
    assert len(lengths) == 114

    # --- Observed statistics ---
    print("\n[4/4] Computing observed + null permutation distributions...")
    obs_a = stat_a_fr(PALINDROMIC_PAIRS, D)
    obs_b = stat_b_shared_roots(PALINDROMIC_PAIRS, top_roots)
    obs_c = stat_c_muq_concordance(PALINDROMIC_PAIRS)
    obs_d = stat_d_spearman_length(PALINDROMIC_PAIRS, lengths)

    # Per-pair breakdown for reporting
    pair_fr_list = sorted(
        [(i, j, D[(i, j)]) for i, j in PALINDROMIC_PAIRS],
        key=lambda x: x[2],
    )
    pair_shared_list = sorted(
        [(i, j, len(top_roots[i] & top_roots[j])) for i, j in PALINDROMIC_PAIRS],
        key=lambda x: -x[2],
    )

    # --- Null distribution ---
    rng = random.Random(SEED)
    null_a = []
    null_b = []
    null_c = []
    null_d = []
    for t in range(N_PERMS):
        pr = random_pairing(rng)
        null_a.append(stat_a_fr(pr, D))
        null_b.append(stat_b_shared_roots(pr, top_roots))
        null_c.append(stat_c_muq_concordance(pr))
        null_d.append(stat_d_spearman_length(pr, lengths))
        if (t + 1) % 200 == 0:
            print(f"  perm {t+1}/{N_PERMS}")

    p_a, z_a = permutation_p_one_sided(null_a, obs_a, "lower")
    p_b, z_b = permutation_p_one_sided(null_b, obs_b, "upper")
    p_c, z_c = permutation_p_one_sided(null_c, obs_c, "upper")
    p_d, z_d = permutation_p_one_sided(null_d, obs_d, "upper")

    def verdict(p: float) -> str:
        return "PASS" if p < ALPHA_BON else "NULL"

    results = {
        "finding_id": "h-new-247",
        "title": "Palindromic surah-pair symmetry test (k paired with 115-k)",
        "parent_finding": "cross-finding-013",
        "sibling_context": ["h-new-204", "h-new-158"],
        "date": "2026-04-17",
        "seed": SEED,
        "n_perms": N_PERMS,
        "bonferroni_k": BONFERRONI_K,
        "alpha": ALPHA,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(no-tashkeel, 114 surahs, 57 pairs {(k,115-k)}, QAC-STEM K=500 via H-NEW-111, Hafs-Kufan)",
        "prereg_sha256": prereg_sha,
        "parent_h_new_111_sha256": parent_sha,
        "palindromic_pairs": PALINDROMIC_PAIRS,
        "muqattaat_surahs": sorted(MUQ_SURAHS),
        "cells": {
            "a_fisher_rao_mean_distance": {
                "description": "Mean FR distance over 57 palindromic pairs (one-sided lower)",
                "observed": obs_a,
                "null_mean": statistics.mean(null_a),
                "null_sd": statistics.stdev(null_a),
                "null_min": min(null_a),
                "null_max": max(null_a),
                "z": z_a,
                "p_perm_one_sided_lower": p_a,
                "pass": p_a < ALPHA_BON,
                "verdict": verdict(p_a),
            },
            "b_shared_top50_roots": {
                "description": "Mean |top50(i) ∩ top50(j)| over 57 pairs (one-sided upper)",
                "observed": obs_b,
                "null_mean": statistics.mean(null_b),
                "null_sd": statistics.stdev(null_b),
                "null_min": min(null_b),
                "null_max": max(null_b),
                "z": z_b,
                "p_perm_one_sided_upper": p_b,
                "pass": p_b < ALPHA_BON,
                "verdict": verdict(p_b),
            },
            "c_muq_concordance_count": {
                "description": "Count of 57 pairs where muq-status concords (one-sided upper)",
                "observed": obs_c,
                "null_mean": statistics.mean(null_c),
                "null_sd": statistics.stdev(null_c),
                "null_min": min(null_c),
                "null_max": max(null_c),
                "z": z_c,
                "p_perm_one_sided_upper": p_c,
                "pass": p_c < ALPHA_BON,
                "verdict": verdict(p_c),
            },
            "d_length_log_spearman": {
                "description": "Spearman rho between log n_v(k) and log n_v(115-k), k=1..57 (one-sided upper)",
                "observed": obs_d,
                "null_mean": statistics.mean(null_d),
                "null_sd": statistics.stdev(null_d),
                "null_min": min(null_d),
                "null_max": max(null_d),
                "z": z_d,
                "p_perm_one_sided_upper": p_d,
                "pass": p_d < ALPHA_BON,
                "verdict": verdict(p_d),
            },
        },
        "n_cells_pass": sum(
            int(p < ALPHA_BON) for p in (p_a, p_b, p_c, p_d)
        ),
        "top5_palindromic_pairs_by_fr_proximity": [
            {"i": i, "j": j, "d_fr": round(d, 6)}
            for i, j, d in pair_fr_list[:5]
        ],
        "bottom5_palindromic_pairs_by_fr_proximity": [
            {"i": i, "j": j, "d_fr": round(d, 6)}
            for i, j, d in pair_fr_list[-5:]
        ],
        "top5_palindromic_pairs_by_shared_roots": [
            {"i": i, "j": j, "shared": s}
            for i, j, s in pair_shared_list[:5]
        ],
        "muq_status_of_pairs": [
            {
                "i": i,
                "j": j,
                "i_muq": i in MUQ_SURAHS,
                "j_muq": j in MUQ_SURAHS,
                "concord": (i in MUQ_SURAHS) == (j in MUQ_SURAHS),
            }
            for i, j in PALINDROMIC_PAIRS
        ],
        "leave_q1_out_sensitivity": {
            "description": "Drop pair (1,114) and recompute observed stats; if all observed stats move materially toward null, (1,114) is driving the signal.",
            "obs_a_without_q1": stat_a_fr(PALINDROMIC_PAIRS[1:], D),
            "obs_b_without_q1": stat_b_shared_roots(PALINDROMIC_PAIRS[1:], top_roots),
            "obs_c_without_q1": stat_c_muq_concordance(PALINDROMIC_PAIRS[1:]),
            "obs_d_without_q1": stat_d_spearman_length(PALINDROMIC_PAIRS[1:], lengths),
        },
        "mw5_control_random_draw_z_mean": {
            "cell_a": statistics.mean((v - statistics.mean(null_a)) / statistics.stdev(null_a) for v in null_a) if statistics.stdev(null_a) > 0 else 0,
            "note": "Should be ~0 by construction; any drift indicates bug.",
        },
        "verdict_overall": None,  # filled below
    }

    n_pass = results["n_cells_pass"]
    if n_pass == 0:
        overall = "NULL (palindromic pairing is not structural; consistent with H-NEW-204)"
    elif n_pass == 1:
        overall = "DIMENSION-SPECIFIC partial pass"
    elif n_pass <= 3:
        overall = "PASS-DIRECTED (multi-axis palindromic layer)"
    else:
        overall = "STRONG PASS (4/4 cells confirm full palindromic symmetry)"
    results["verdict_overall"] = overall

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\nWrote {OUTPUT}")

    # Console summary
    print("\n" + "=" * 72)
    print(f"H-NEW-247 — palindromic symmetry test (α_bon={ALPHA_BON})")
    print("=" * 72)
    for cell_key, cell in results["cells"].items():
        print(f"  [{cell_key}]")
        print(
            f"    observed={cell['observed']:.4f}  null_mean={cell['null_mean']:.4f}  "
            f"z={cell['z']:+.3f}  p={cell['p_perm_one_sided_lower' if 'lower' in cell else 'p_perm_one_sided_upper']:.4f}  "
            f"→ {cell['verdict']}"
        ) if False else None
        pkey = [k for k in cell if k.startswith("p_perm")][0]
        print(
            f"    observed={cell['observed']:.4f}  null_mean={cell['null_mean']:.4f}  "
            f"z={cell['z']:+.3f}  p={cell[pkey]:.4f}  → {cell['verdict']}"
        )
    print(f"\n  cells PASS: {n_pass}/4  →  {overall}")
    print("\n  Top-5 palindromic pairs by FR proximity:")
    for row in results["top5_palindromic_pairs_by_fr_proximity"]:
        print(f"    Q{row['i']:3d} ↔ Q{row['j']:3d}   d_FR = {row['d_fr']:.4f}")


if __name__ == "__main__":
    main()
