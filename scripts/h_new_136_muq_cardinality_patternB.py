#!/usr/bin/env python3
"""H-NEW-136 — Muqaṭṭāʿat cardinality × Pattern-B composite Spearman correlation.

Pre-reg: scratch/theorist-2026-04-17-unified-equation.md §7
Executed inline by team-lead 2026-04-17; this script provides reproducibility
for what was run and writes the JSON artifact.

Test: Spearman ρ(muq_cardinality, Pattern-B composite) on the 29 muq-opened surahs.
Pattern-B composite = mean of z-normed(qul_density, book_reference_density,
eschatological_density, loanword_density) over all 114 surahs.

Seed: 20260418 (per theorist pre-reg). Permutations: 10,000. Bonferroni k=1 (α=0.05).
PASS-DIRECTED if ρ > +0.3 AND one-sided perm p < 0.05.
STRONG-PASS if ρ > +0.5 AND one-sided perm p < 0.01.
"""

from __future__ import annotations

import json
import math
import random
from pathlib import Path

SEED = 20260418
N_PERMS = 10_000
PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
H125_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-125.json"
OUTPUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-136.json"

MUQ_SET = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
           31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]
PATTERN_B_AXES = ("qul_density", "book_reference_density",
                  "eschatological_density", "loanword_density")


def spearman_rho(x: list[float], y: list[float]) -> float:
    n = len(x)
    rx = _rank(x)
    ry = _rank(y)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx2 = sum((rx[i] - mx) ** 2 for i in range(n))
    dy2 = sum((ry[i] - my) ** 2 for i in range(n))
    denom = math.sqrt(dx2 * dy2)
    return num / denom if denom > 0 else 0.0


def _rank(vals: list[float]) -> list[float]:
    """Average-tie ranking (1-indexed)."""
    indexed = sorted(range(len(vals)), key=lambda i: vals[i])
    ranks = [0.0] * len(vals)
    i = 0
    while i < len(indexed):
        j = i
        while j + 1 < len(indexed) and vals[indexed[j + 1]] == vals[indexed[i]]:
            j += 1
        avg = (i + j + 2) / 2  # 1-indexed avg of positions i+1..j+1
        for k in range(i, j + 1):
            ranks[indexed[k]] = avg
        i = j + 1
    return ranks


def zscore(vals: list[float]) -> list[float]:
    mu = sum(vals) / len(vals)
    var = sum((v - mu) ** 2 for v in vals) / len(vals)
    sd = math.sqrt(var) if var > 0 else 1.0
    return [(v - mu) / sd for v in vals]


def main() -> None:
    with H125_JSON.open() as f:
        h125 = json.load(f)
    psv = h125["per_surah_axis_values"]

    # For each Pattern-B axis, compute z-score over all 114 surahs
    axis_z: dict[str, dict[int, float]] = {}
    for axis in PATTERN_B_AXES:
        vals_by_s: list[tuple[int, float]] = []
        for s_str, entry in psv.items():
            s = int(s_str)
            vals_by_s.append((s, float(entry["axis_values"][axis])))
        vals_by_s.sort()
        surahs = [s for s, _ in vals_by_s]
        vals = [v for _, v in vals_by_s]
        z = zscore(vals)
        axis_z[axis] = dict(zip(surahs, z))

    # Per-surah Pattern-B composite = mean of the 4 z-scores
    composite: dict[int, float] = {}
    for s in range(1, 115):
        composite[s] = sum(axis_z[a][s] for a in PATTERN_B_AXES) / len(PATTERN_B_AXES)

    # muq_cardinality per muq surah
    muq_card: dict[int, int] = {}
    for s in MUQ_SET:
        muq_card[s] = int(psv[str(s)]["axis_values"]["muq_cardinality"])

    # Primary test: Spearman ρ on 29 surahs
    xs = [muq_card[s] for s in MUQ_SET]
    ys = [composite[s] for s in MUQ_SET]
    rho_obs = spearman_rho(xs, ys)

    # Permutation null: shuffle muq_card within the 29 surahs
    rng = random.Random(SEED)
    xs_perm_bag = list(xs)
    n_ge_one_sided = 0
    n_ge_two_sided = 0
    for _ in range(N_PERMS):
        rng.shuffle(xs_perm_bag)
        rho_perm = spearman_rho(xs_perm_bag, ys)
        if rho_perm >= rho_obs:
            n_ge_one_sided += 1
        if abs(rho_perm) >= abs(rho_obs):
            n_ge_two_sided += 1
    p_one = (n_ge_one_sided + 1) / (N_PERMS + 1)
    p_two = (n_ge_two_sided + 1) / (N_PERMS + 1)

    # PASS criteria
    pass_directed = (rho_obs > 0.3) and (p_one < 0.05)
    strong_pass = (rho_obs > 0.5) and (p_one < 0.01)

    # By-cardinality breakdown
    by_card: dict[int, list[tuple[int, float]]] = {}
    for s in MUQ_SET:
        by_card.setdefault(muq_card[s], []).append((s, composite[s]))
    card_summary = {}
    for card, entries in sorted(by_card.items()):
        card_summary[card] = {
            "n": len(entries),
            "mean_composite": sum(c for _, c in entries) / len(entries),
            "surahs": [s for s, _ in entries],
        }

    # MW-5 positive control: Pattern-B axes rho vs Nöldeke across 114
    mw5 = {}
    for axis in PATTERN_B_AXES:
        result = h125["per_axis_results"].get(axis)
        if result:
            mw5[axis] = {
                "rho_spearman_vs_noldeke": result.get("rho_spearman"),
                "p_perm_two_sided": result.get("p_two_sided_perm"),
                "bonferroni_survives_h125": result.get("bonferroni_survives"),
            }

    output = {
        "finding_id": "H-NEW-136",
        "title": "Muqattaat cardinality × Pattern-B composite Spearman correlation",
        "pre_reg_path": "scratch/theorist-2026-04-17-unified-equation.md §7",
        "seed": SEED,
        "n_perms": N_PERMS,
        "muq_surahs": MUQ_SET,
        "n_muq": len(MUQ_SET),
        "pattern_B_axes": list(PATTERN_B_AXES),
        "bonferroni_k": 1,
        "alpha_bon": 0.05,
        "direction_preregistered": "POSITIVE (one-sided)",
        "primary": {
            "rho_spearman": rho_obs,
            "p_one_sided_perm": p_one,
            "p_two_sided_perm": p_two,
            "n_ge_one_sided": n_ge_one_sided,
            "n_ge_two_sided": n_ge_two_sided,
            "pass_directed": pass_directed,
            "strong_pass": strong_pass,
            "verdict": ("STRONG-PASS" if strong_pass
                        else ("PASS-DIRECTED" if pass_directed else "NULL")),
        },
        "by_cardinality": card_summary,
        "per_surah_composite": {
            str(s): {
                "muq_cardinality": muq_card[s],
                "composite_z": composite[s],
                "qul_z": axis_z["qul_density"][s],
                "book_z": axis_z["book_reference_density"][s],
                "eschat_z": axis_z["eschatological_density"][s],
                "loan_z": axis_z["loanword_density"][s],
            }
            for s in MUQ_SET
        },
        "mw5_positive_control": {
            "description": "Pattern-B axes vs Nöldeke-rank across 114 surahs (inherited from H-NEW-125)",
            "axis_results": mw5,
            "all_axes_bonferroni_survive_in_h125":
                all(v.get("bonferroni_survives_h125") for v in mw5.values()),
        },
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # Console summary
    print("=" * 70)
    print("H-NEW-136 — Muqattaat cardinality × Pattern-B composite")
    print("=" * 70)
    print(f"N = {len(MUQ_SET)} muqaṭṭāʿat-opened surahs")
    print(f"Spearman ρ = {rho_obs:+.4f}")
    print(f"One-sided perm p = {p_one:.5f}  (n_ge = {n_ge_one_sided}/{N_PERMS})")
    print(f"Two-sided perm p = {p_two:.5f}  (n_ge = {n_ge_two_sided}/{N_PERMS})")
    print(f"PASS-DIRECTED: {pass_directed}")
    print(f"STRONG-PASS:   {strong_pass}")
    print(f"Verdict: {output['primary']['verdict']}")
    print()
    print("By-cardinality means:")
    for card, summ in card_summary.items():
        print(f"  card={card}: n={summ['n']}, mean composite Z = {summ['mean_composite']:+.3f}, surahs={summ['surahs']}")
    print()
    print(f"Output JSON: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
