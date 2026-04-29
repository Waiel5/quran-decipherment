#!/usr/bin/env python3
"""H-NEW-143.1 — Root-level rhetorical-bridge test across mushaf boundaries.

Pre-reg: findings/phase-b-hypotheses/h-new-143-1-prereg.md
Parent NULL: h-new-143 (surface-word NULL)

Tests whether QAC-STEM root overlap between last verse of surah i and first
verse of surah i+1 is LARGER at top-15 Fisher-Rao jump boundaries than at
other 98 boundaries. Also checks that 3 universal hinges have root-overlap
above 50th percentile.
"""

from __future__ import annotations

import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

sys.path.insert(0, "/Users/grey/Downloads/quran/scripts")

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
QAC_FILE = PROJECT_ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
H130 = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130.json"
H130B = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130b.json"
H130C = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-130c.json"
OUTPUT = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-143-1.json"
PREREG = PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-143-1-prereg.md"

UNIVERSAL_HINGES = {(14, 15), (49, 50), (56, 57)}


def load_roots_per_verse() -> dict[tuple[int, int], set[str]]:
    """Return {(chapter, verse): {root, ...}} from QAC STEM entries only."""
    root_re = re.compile(r"ROOT:([a-zA-Z~`]+)")
    per_verse: dict[tuple[int, int], set[str]] = defaultdict(set)
    with QAC_FILE.open() as f:
        for line in f:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            addr, _form, _pos, features = parts[0], parts[1], parts[2], parts[3]
            # addr like (14:52:3:3)
            m = re.match(r"\((\d+):(\d+):\d+:\d+\)", addr)
            if not m:
                continue
            ch, v = int(m.group(1)), int(m.group(2))
            if "STEM" not in features:
                continue
            root_m = root_re.search(features)
            if root_m:
                per_verse[(ch, v)].add(root_m.group(1))
    return dict(per_verse)


def surah_last_verse_number(per_verse: dict[tuple[int, int], set[str]], s: int) -> int:
    vs = [v for (ch, v) in per_verse.keys() if ch == s]
    return max(vs) if vs else 0


def mann_whitney_u(x: list[float], y: list[float]) -> tuple[float, float, float]:
    combined = [(v, 0) for v in x] + [(v, 1) for v in y]
    combined.sort(key=lambda v: v[0])
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg = (i + j + 2) / 2
        for k in range(i, j + 1):
            ranks[k] = avg
        i = j + 1
    R1 = sum(ranks[k] for k in range(len(combined)) if combined[k][1] == 0)
    n1, n2 = len(x), len(y)
    U1 = R1 - n1 * (n1 + 1) / 2
    mu = n1 * n2 / 2
    sigma = (n1 * n2 * (n1 + n2 + 1) / 12) ** 0.5
    # Use U1 for one-sided: if we expect top-15 > other, reject when R1 is high (U1 is low)
    # Two-sided z:
    z_two_sided = (U1 - mu) / sigma
    # One-sided upper-tail (top-15 > other): equivalent to R1 > mean_R1
    # If x are top-15 with higher values, R1 should be HIGHER than expected
    z_positive = z_two_sided  # we'll interpret sign
    p_two_sided = math.erfc(abs(z_two_sided) / math.sqrt(2))
    p_one_sided_upper = p_two_sided / 2 if z_two_sided > 0 else 1 - p_two_sided / 2
    return U1, z_two_sided, p_one_sided_upper


def load_top15(path: Path) -> set[tuple[int, int]]:
    with path.open() as f:
        return set((r["i"], r["j"]) for r in json.load(f)["top15_largest_jumps"])


def main() -> None:
    per_verse = load_roots_per_verse()
    print(f"Loaded QAC-STEM roots for {len(per_verse)} verses")

    # Compute last-verse root set and first-verse root set per surah
    last_roots: dict[int, set[str]] = {}
    first_roots: dict[int, set[str]] = {}
    for s in range(1, 115):
        last_v = surah_last_verse_number(per_verse, s)
        first_v = 1
        last_roots[s] = per_verse.get((s, last_v), set())
        first_roots[s] = per_verse.get((s, first_v), set())

    # Bridge metrics for all 113 boundaries
    bridges: dict[tuple[int, int], dict] = {}
    for i in range(1, 114):
        a = last_roots[i]
        b = first_roots[i + 1]
        overlap = a & b
        union = a | b
        bridges[(i, i + 1)] = {
            "overlap_count": len(overlap),
            "cos": len(overlap) / math.sqrt(len(a) * len(b)) if len(a) and len(b) else 0.0,
            "jaccard": len(overlap) / len(union) if union else 0.0,
            "a_size": len(a), "b_size": len(b),
            "shared_roots": sorted(list(overlap)),
        }

    # Load FR top-15 sets
    root_top15 = load_top15(H130)
    char_top15 = load_top15(H130B)
    vlen_top15 = load_top15(H130C)
    union_top15 = root_top15 | char_top15 | vlen_top15

    # Primary: Mann-Whitney U, top-15 (union) vs other
    union_in = [bridges[p]["cos"] for p in union_top15 if p in bridges]
    union_out = [b["cos"] for p, b in bridges.items() if p not in union_top15]
    U_union, z_union, p_union = mann_whitney_u(union_in, union_out)

    # Per-feature top-15 tests (3 sub-tests)
    per_feature = {}
    for name, top_set in [("root", root_top15), ("char_4gram", char_top15), ("vlen", vlen_top15)]:
        in_vals = [bridges[p]["cos"] for p in top_set if p in bridges]
        out_vals = [b["cos"] for p, b in bridges.items() if p not in top_set]
        U, z, p_upper = mann_whitney_u(in_vals, out_vals)
        per_feature[name] = {
            "mean_top15": mean(in_vals),
            "mean_other": mean(out_vals),
            "U": U, "z": z,
            "p_one_sided_upper": p_upper,
        }

    # Universal hinges rank
    all_cos = sorted(bridges.items(), key=lambda x: x[1]["cos"])
    cos_to_rank = {p: rank + 1 for rank, (p, _) in enumerate(all_cos)}
    univ_ranks = {p: cos_to_rank[p] for p in UNIVERSAL_HINGES}
    univ_cos = {str(p): bridges[p]["cos"] for p in UNIVERSAL_HINGES}
    univ_shared = {str(p): bridges[p]["shared_roots"] for p in UNIVERSAL_HINGES}
    # percentile: rank / 113
    univ_percentile = {str(p): univ_ranks[p] / 113 for p in UNIVERSAL_HINGES}
    above_50 = sum(1 for p in UNIVERSAL_HINGES if univ_percentile[str(p)] > 0.5)

    # Top-10 strongest root bridges
    strongest = sorted(bridges.items(), key=lambda x: -x[1]["cos"])[:10]

    # Primary verdict
    primary_pass = p_union < 0.0167 and mean(union_in) > mean(union_out)

    # Secondary universal verdict
    universal_pass_full = above_50 == 3
    universal_pass_partial = above_50 >= 2

    # MW-5: sort-by-length synth ordering
    from h_new_130_fisher_rao_residuals import load_verse_counts
    verse_counts = load_verse_counts()
    order = sorted(range(1, 115), key=lambda s: (-verse_counts[s], s))
    synth_bridges = []
    for i in range(len(order) - 1):
        a = last_roots[order[i]]
        b = first_roots[order[i + 1]]
        overlap = a & b
        cos = len(overlap) / math.sqrt(len(a) * len(b)) if len(a) and len(b) else 0.0
        synth_bridges.append(cos)

    output = {
        "finding_id": "h-new-143-1",
        "title": "Root-level rhetorical-bridge test across mushaf boundaries",
        "pre_reg_path": str(PREREG),
        "parent_finding": "h-new-143 (surface NULL)",
        "parent_h142": "h-new-142 (post-hoc rhetorical-bridge observations)",
        "method": "QAC-STEM root-set overlap between last verse of surah i and first verse of surah i+1. Primary metric: cosine. Mann-Whitney U one-sided upper-tail.",
        "n_boundaries": 113,
        "zero_overlap_count": sum(1 for b in bridges.values() if b["overlap_count"] == 0),
        "primary_union_top15_vs_other": {
            "union_top15_size": len(union_top15),
            "mean_top15": mean(union_in),
            "mean_other": mean(union_out),
            "U": U_union,
            "z_two_sided": z_union,
            "p_one_sided_upper": p_union,
            "alpha_bon": 0.0167,
            "pass": primary_pass,
        },
        "per_feature_top15": per_feature,
        "universal_hinges": {
            str(p): {
                "pair": list(p),
                "cos": univ_cos[str(p)],
                "rank_of_113_ascending": univ_ranks[p],
                "percentile": univ_percentile[str(p)],
                "above_50th_percentile": univ_percentile[str(p)] > 0.5,
                "shared_roots": univ_shared[str(p)],
            } for p in UNIVERSAL_HINGES
        },
        "universal_hinges_summary": {
            "n_above_50th_percentile": above_50,
            "pass_full": universal_pass_full,
            "pass_partial": universal_pass_partial,
        },
        "top10_strongest_root_bridges": [
            {"pair": list(p), "cos": v["cos"], "shared_roots": v["shared_roots"]}
            for p, v in strongest
        ],
        "mw5_sort_by_length_control": {
            "synth_mean_cos": mean(synth_bridges),
            "mushaf_mean_cos": mean([b["cos"] for b in bridges.values()]),
            "note": "Sanity: sort-by-length gives different bridge-distribution than mushaf-adjacent.",
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # Console
    print("=" * 70)
    print("H-NEW-143.1 — Root-level bridge test")
    print("=" * 70)
    print(f"Zero-root-overlap boundaries: {output['zero_overlap_count']} of 113")
    print()
    print(f"PRIMARY: top-15 union vs other")
    print(f"  mean_top15: {mean(union_in):.4f}")
    print(f"  mean_other: {mean(union_out):.4f}")
    print(f"  z: {z_union:+.3f}")
    print(f"  p_one_sided_upper: {p_union:.5f}")
    print(f"  PASS: {primary_pass}")
    print()
    print(f"Per-feature top-15:")
    for name, r in per_feature.items():
        print(f"  {name:<12}: top15={r['mean_top15']:.4f} other={r['mean_other']:.4f} z={r['z']:+.3f} p_upper={r['p_one_sided_upper']:.4f}")
    print()
    print(f"Universal hinges ({len(UNIVERSAL_HINGES)}):")
    for p in sorted(UNIVERSAL_HINGES):
        ui = output["universal_hinges"][str(p)]
        print(f"  Q{p[0]}→Q{p[1]}: cos={ui['cos']:.4f} rank={ui['rank_of_113_ascending']}/113 "
              f"pct={ui['percentile']:.2f} shared={ui['shared_roots']}")
    print(f"  Above-P50: {above_50} of 3 (PASS_full={universal_pass_full}; PASS_partial={universal_pass_partial})")
    print()
    print("Top-10 strongest ROOT-level bridges:")
    for row in output["top10_strongest_root_bridges"]:
        print(f"  Q{row['pair'][0]:3d}→Q{row['pair'][1]:3d}  cos={row['cos']:.4f}  shared={row['shared_roots']}")
    print()
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()
