#!/usr/bin/env python3
"""H-NEW-199: Positional ratio analysis of canonical celebrated verses.
Pre-reg: bonferroni_k=2, seed=20260419.
"""
import json
import math
from pathlib import Path

SEED = 20260419
BONFERRONI_K = 2
ALPHA = 0.05
ALPHA_CORR = ALPHA / BONFERRONI_K
TOL = 0.05
P0 = 2 * TOL  # prob of being within TOL of a fixed anchor under Uniform(0,1)

# Load verse counts
counts = {}
vpath = Path("/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv")
for line in vpath.read_text().strip().splitlines():
    parts = line.split("\t")
    if len(parts) >= 2:
        counts[int(parts[0])] = int(parts[1])

# Pre-registered target positions
targets = []
# Khawātim al-Ḥashr
for v in (22, 23, 24):
    targets.append(("HASHR", 59, v, counts[59]))
# Light-verse
targets.append(("NUR", 24, 35, counts[24]))
# al-Kursī
targets.append(("KURSI", 2, 255, counts[2]))
# al-Ikhlāṣ (all 4 verses)
for v in range(1, counts[112] + 1):
    targets.append(("IKHLAS", 112, v, counts[112]))
# al-Fātiḥa (first, middle, last)
targets.append(("FATIHA", 1, 1, counts[1]))
targets.append(("FATIHA", 1, 4, counts[1]))
targets.append(("FATIHA", 1, 7, counts[1]))

# Compute ratios
rows = []
for code, s, v, tot in targets:
    r = v / tot
    rows.append({"code": code, "surah": s, "verse": v, "total": tot, "ratio": r})

# Anchors
PHI_INV = (math.sqrt(5) - 1) / 2  # 0.618...
TWO_THIRDS = 2 / 3

def binom_sf(k, n, p):
    """P(X >= k) for X~Bin(n,p)"""
    from math import comb
    total = 0.0
    for i in range(k, n + 1):
        total += comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return total

def test_anchor(rows, anchor, label):
    distances = [abs(r["ratio"] - anchor) for r in rows]
    hits = sum(1 for d in distances if d <= TOL)
    n = len(rows)
    # one-sided: P(X >= hits | p=P0)
    pval = binom_sf(hits, n, P0)
    return {
        "label": label,
        "anchor": anchor,
        "tolerance": TOL,
        "n_positions": n,
        "hits": hits,
        "expected_hits": n * P0,
        "p_value": pval,
        "bonferroni_corrected_alpha": ALPHA_CORR,
        "promoted": (pval <= ALPHA_CORR) and (hits >= 3),
    }

# Descriptive
ratios = [r["ratio"] for r in rows]
mean_r = sum(ratios) / len(ratios)
var_r = sum((x - mean_r) ** 2 for x in ratios) / (len(ratios) - 1)

results = {
    "seed": SEED,
    "bonferroni_k": BONFERRONI_K,
    "alpha": ALPHA,
    "alpha_corrected": ALPHA_CORR,
    "tolerance": TOL,
    "p0_uniform_null": P0,
    "n_positions": len(rows),
    "positions": rows,
    "descriptive": {
        "mean_ratio": mean_r,
        "sample_variance": var_r,
        "uniform_expected_variance": 1 / 12,
    },
    "tests": [
        test_anchor(rows, PHI_INV, "golden_ratio_minus_1"),
        test_anchor(rows, TWO_THIRDS, "two_thirds"),
    ],
}

# Also report clustering at edges and the full distribution
edges = {
    "near_0.0": sum(1 for x in ratios if x <= 0.10),
    "near_0.5": sum(1 for x in ratios if 0.45 <= x <= 0.55),
    "near_0.618": sum(1 for x in ratios if abs(x - PHI_INV) <= 0.05),
    "near_0.667": sum(1 for x in ratios if abs(x - TWO_THIRDS) <= 0.05),
    "near_1.0": sum(1 for x in ratios if x >= 0.90),
}
results["edge_counts"] = edges

out = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-199-work/results.json")
out.write_text(json.dumps(results, indent=2, ensure_ascii=False))

# Print summary
print(f"n positions: {len(rows)}")
print(f"mean ratio:  {mean_r:.4f}")
print(f"sample var:  {var_r:.4f}  (uniform null: {1/12:.4f})")
print()
print("Individual ratios:")
for r in rows:
    a1 = abs(r["ratio"] - PHI_INV)
    a2 = abs(r["ratio"] - TWO_THIRDS)
    mark = []
    if a1 <= TOL: mark.append("phi")
    if a2 <= TOL: mark.append("2/3")
    print(f"  Q{r['surah']:3d}:{r['verse']:3d} / {r['total']:3d}  = {r['ratio']:.4f}  [{','.join(mark)}]")
print()
for t in results["tests"]:
    print(f"{t['label']:25s}  anchor={t['anchor']:.4f}  hits={t['hits']}/{t['n_positions']}  p={t['p_value']:.4g}  promoted={t['promoted']}")
print(f"\nedge counts: {edges}")
print(f"\nwrote {out}")
