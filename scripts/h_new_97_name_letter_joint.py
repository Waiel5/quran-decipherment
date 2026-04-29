"""H-NEW-97 — Surah-name-class × muqaṭṭāʿat letter-set JOINT distribution.

Pre-reg: findings/phase-b-hypotheses/h-new-97-name-letter-joint-prereg.md

Cells:
  Cell 1 — PRIMARY χ² independence on 10 × 9 contingency (Monte-Carlo null 10K perms)
  Cell 2 — Per-cluster χ² vs uniform (ALM, ALR, HM each vs Uniform(9))
  Cell 3 — Cramer's V effect size
  Cell 4 — Per-cluster name-class rank profile (directional verification)

Seed: 20260417 ; Bonferroni k=4 ; α_bon = 0.0125
"""

from __future__ import annotations

import json
import math
import os
import random
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

REPO = "/Users/grey/Downloads/quran"
SEED = 20260417
N_PERM = 10_000
BON_K = 4
ALPHA_BON = 0.05 / BON_K  # 0.0125

# Locked 29 muqaṭṭaʿāt surahs
MUQ_SURAHS = [
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68,
]
assert len(MUQ_SURAHS) == 29

# Locked letter-set per surah (H-NEW-88 taxonomy)
# 14 distinct sets. 10-row collapse per pre-reg:
#  ALM, ALR, HM, TSM kept as cluster rows; ALMS, ALMR, KHYAS, HMASQ kept as
#  compound-singleton rows; SINGLE_SIMPLE pools {طه Q20, طس Q27, يس Q36, ص Q38,
#  ق Q50, ن Q68}.
LETTER_SET_14 = {
    2: "ALM", 3: "ALM", 29: "ALM", 30: "ALM", 31: "ALM", 32: "ALM",
    10: "ALR", 11: "ALR", 12: "ALR", 14: "ALR", 15: "ALR",
    40: "HM", 41: "HM", 43: "HM", 44: "HM", 45: "HM", 46: "HM",
    26: "TSM", 28: "TSM",
    7: "ALMS", 13: "ALMR", 19: "KHYAS", 42: "HMASQ",
    20: "TH", 27: "TS", 36: "YS", 38: "S", 50: "Q", 68: "N",
}

# 10-row collapse (LOCKED)
LETTER_SET_10 = {}
for s in MUQ_SURAHS:
    raw = LETTER_SET_14[s]
    if raw in ("TH", "TS", "YS", "S", "Q", "N"):
        LETTER_SET_10[s] = "SINGLE_SIMPLE"
    else:
        LETTER_SET_10[s] = raw

LETTER_SET_ROWS = ["ALM", "ALR", "HM", "TSM", "ALMS", "ALMR", "KHYAS", "HMASQ", "SINGLE_SIMPLE"]
# 9 rows used (the 10th row "SINGLE_COMPOUND" in pre-reg was hypothetical and
# ends up empty because all remaining compound-singletons are individually
# represented). Per pre-reg this is acceptable — empty rows drop.

# Locked 9 name-classes (from H-NEW-49)
NAME_CLASSES = [
    "PROPHET_PERSON",
    "ANIMAL_OBJECT",
    "DIVINE_ATTRIBUTE",
    "COSMOLOGICAL_NATURAL",
    "EVENT_ESCHATOLOGICAL",
    "SOCIAL_LEGAL",
    "REVELATION_RITUAL",
    "MUQATTAAT_LETTER",
    "OTHER_ABSTRACT",
]


def load_name_class() -> Dict[int, str]:
    with open(os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-49.json")) as f:
        d = json.load(f)
    return {int(k): v["class"] for k, v in d["surah_class_assignments"].items()}


def build_contingency(surahs: List[int],
                      name_class: Dict[int, str],
                      letter_set: Dict[int, str],
                      row_labels: List[str],
                      col_labels: List[str]) -> List[List[int]]:
    idx_row = {r: i for i, r in enumerate(row_labels)}
    idx_col = {c: i for i, c in enumerate(col_labels)}
    tab = [[0 for _ in col_labels] for _ in row_labels]
    for s in surahs:
        r = letter_set[s]
        c = name_class[s]
        tab[idx_row[r]][idx_col[c]] += 1
    return tab


def chi_square_stat(tab: List[List[int]]) -> Tuple[float, int, List[List[float]]]:
    """Compute χ² statistic, df, and expected-cell matrix.

    Rows/columns with zero total are dropped before computation (standard χ²
    practice). df = (R_used - 1) * (C_used - 1).
    """
    row_tot = [sum(r) for r in tab]
    col_tot = [sum(tab[i][j] for i in range(len(tab))) for j in range(len(tab[0]))]
    N = sum(row_tot)

    # Drop zero-total rows and columns
    keep_rows = [i for i, t in enumerate(row_tot) if t > 0]
    keep_cols = [j for j, t in enumerate(col_tot) if t > 0]
    sub = [[tab[i][j] for j in keep_cols] for i in keep_rows]
    rt = [row_tot[i] for i in keep_rows]
    ct = [col_tot[j] for j in keep_cols]

    chi2 = 0.0
    exp = [[0.0 for _ in keep_cols] for _ in keep_rows]
    for i, ri in enumerate(rt):
        for j, cj in enumerate(ct):
            e = ri * cj / N if N > 0 else 0.0
            exp[i][j] = e
            if e > 0:
                chi2 += (sub[i][j] - e) ** 2 / e
    df = (len(keep_rows) - 1) * (len(keep_cols) - 1)
    return chi2, df, exp


def cramer_v(chi2: float, N: int, R: int, C: int) -> float:
    k = min(R - 1, C - 1)
    if k <= 0 or N <= 0:
        return 0.0
    return math.sqrt(chi2 / (N * k))


def monte_carlo_chi2_pvalue(tab: List[List[int]],
                             row_assign: List[str],
                             col_assign: List[str],
                             row_labels: List[str],
                             col_labels: List[str],
                             n_perm: int,
                             rng: random.Random) -> Tuple[float, float, List[float]]:
    """Permute the column (name-class) assignment over the 29 surahs,
    preserving both row (letter-set) AND column marginals.

    Returns (observed chi2, p_mc, null_distribution).
    """
    obs_chi2, _, _ = chi_square_stat(tab)
    null_stats = []
    # row_assign[i] = letter-set for surah i; col_assign[i] = name-class
    perms_col = list(col_assign)
    ge = 0
    for _ in range(n_perm):
        rng.shuffle(perms_col)
        # rebuild contingency
        ncol = len(col_labels)
        nrow = len(row_labels)
        tab2 = [[0 for _ in range(ncol)] for _ in range(nrow)]
        idx_row = {r: i for i, r in enumerate(row_labels)}
        idx_col = {c: j for j, c in enumerate(col_labels)}
        for r_lab, c_lab in zip(row_assign, perms_col):
            tab2[idx_row[r_lab]][idx_col[c_lab]] += 1
        s, _, _ = chi_square_stat(tab2)
        null_stats.append(s)
        if s >= obs_chi2:
            ge += 1
    p_mc = (ge + 1) / (n_perm + 1)
    return obs_chi2, p_mc, null_stats


def per_cluster_chi2_vs_uniform(cluster_surahs: List[int],
                                 name_class: Dict[int, str],
                                 cols: List[str],
                                 n_perm: int,
                                 rng: random.Random) -> Dict:
    """χ² goodness-of-fit vs uniform over name-class columns for a single
    cluster. Monte-Carlo null = draw from Uniform({cols}) n_perm times."""
    n = len(cluster_surahs)
    counts = Counter(name_class[s] for s in cluster_surahs)
    C = len(cols)
    e = n / C
    obs = sum(((counts.get(c, 0) - e) ** 2) / e for c in cols)
    ge = 0
    null_vals = []
    for _ in range(n_perm):
        # sample n labels uniformly from cols
        samp = Counter(rng.choice(cols) for _ in range(n))
        v = sum(((samp.get(c, 0) - e) ** 2) / e for c in cols)
        null_vals.append(v)
        if v >= obs:
            ge += 1
    p_mc = (ge + 1) / (n_perm + 1)
    return {
        "n": n,
        "counts": dict(counts),
        "chi2_obs": obs,
        "p_mc": p_mc,
        "null_mean": sum(null_vals) / len(null_vals),
    }


def rank_profile(cluster_surahs: List[int],
                  name_class: Dict[int, str]) -> List[Tuple[str, int]]:
    c = Counter(name_class[s] for s in cluster_surahs)
    return sorted(c.items(), key=lambda x: (-x[1], x[0]))


def main():
    rng = random.Random(SEED)
    name_class = load_name_class()

    # Primary 10×9 contingency (SINGLE_SIMPLE merged)
    letter_set_primary = {s: LETTER_SET_10[s] for s in MUQ_SURAHS}
    rows = LETTER_SET_ROWS  # 9 rows (SINGLE_COMPOUND dropped as empty)
    cols = NAME_CLASSES
    tab = build_contingency(MUQ_SURAHS, name_class, letter_set_primary, rows, cols)

    # Cell 1
    row_assign = [letter_set_primary[s] for s in MUQ_SURAHS]
    col_assign = [name_class[s] for s in MUQ_SURAHS]
    obs_chi2, p_mc, null_dist = monte_carlo_chi2_pvalue(
        tab, row_assign, col_assign, rows, cols, N_PERM, rng,
    )

    # Rebuild df/expected
    _, df, expected = chi_square_stat(tab)
    # Also used rows/cols counts for Cramer's V
    used_rows = sum(1 for r in tab if sum(r) > 0)
    used_cols = 0
    for j in range(len(cols)):
        col_tot_j = sum(tab[i][j] for i in range(len(tab)))
        if col_tot_j > 0:
            used_cols += 1
    v = cramer_v(obs_chi2, N=29, R=used_rows, C=used_cols)

    # Cell 2 — per-cluster χ² vs uniform (ALM, ALR, HM)
    clusters = {
        "ALM": [s for s in MUQ_SURAHS if letter_set_primary[s] == "ALM"],
        "ALR": [s for s in MUQ_SURAHS if letter_set_primary[s] == "ALR"],
        "HM":  [s for s in MUQ_SURAHS if letter_set_primary[s] == "HM"],
    }
    per_cluster = {}
    for k, surahs in clusters.items():
        per_cluster[k] = per_cluster_chi2_vs_uniform(
            surahs, name_class, cols, N_PERM, rng,
        )

    # Cell 4 — rank profile
    rank = {k: rank_profile(s, name_class) for k, s in clusters.items()}

    # Build output
    out = {
        "id": "H-NEW-97",
        "seed": SEED,
        "bonferroni_k": BON_K,
        "bonferroni_family": "h-new-97-name-letter-joint",
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(hafs-kufan; no-tashkeel; canonical 114; 29-muqaṭṭaʿāt; H-NEW-49 9-class; H-NEW-88 letter-sets collapsed to 10 rows — SINGLE_SIMPLE merged)",
        "n_muqattaat": 29,
        "letter_set_rows_used": rows,
        "name_classes": cols,
        "per_surah": [
            {
                "surah": s,
                "letter_set_14": LETTER_SET_14[s],
                "letter_set_10": LETTER_SET_10[s],
                "name_class": name_class[s],
            }
            for s in MUQ_SURAHS
        ],
        "contingency": {
            "rows": rows,
            "cols": cols,
            "table": tab,
            "row_totals": [sum(r) for r in tab],
            "col_totals": [sum(tab[i][j] for i in range(len(tab))) for j in range(len(cols))],
        },
        "cell_1_primary_chi2": {
            "chi2_obs": obs_chi2,
            "df": df,
            "p_mc": p_mc,
            "n_perm": N_PERM,
            "alpha_bon": ALPHA_BON,
            "verdict": "REJECT_INDEPENDENCE" if p_mc < ALPHA_BON else "FAIL_TO_REJECT",
            "null_mean": sum(null_dist) / len(null_dist),
            "null_q95": sorted(null_dist)[int(0.95 * len(null_dist))],
            "null_max": max(null_dist),
        },
        "cell_2_per_cluster_chi2_vs_uniform": per_cluster,
        "cell_3_cramers_v": {
            "chi2": obs_chi2,
            "N": 29,
            "used_rows": used_rows,
            "used_cols": used_cols,
            "V": v,
            "interpretation": (
                "large" if v > 0.5 else ("medium" if v > 0.3 else "small")
            ),
        },
        "cell_4_rank_profile": {
            k: [{"class": c, "count": n} for c, n in v]
            for k, v in rank.items()
        },
        "directional_checks": {
            "ALR_modal_PROPHET_PERSON": rank["ALR"][0][0] == "PROPHET_PERSON" if rank["ALR"] else False,
            "HM_no_PROPHET_PERSON": "PROPHET_PERSON" not in [c for c, _ in rank["HM"]],
            "ALM_mixed_no_class_majority": rank["ALM"][0][1] <= 3 if rank["ALM"] else False,
        },
    }

    with open(os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-97.json"), "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    # Print summary
    print("=" * 70)
    print("H-NEW-97 — Surah-name-class × muqaṭṭāʿat letter-set JOINT")
    print("=" * 70)
    print(f"Seed: {SEED}; Bonferroni k={BON_K}; α_bon={ALPHA_BON}")
    print()
    print("Contingency table (10 letter-set rows × 9 name-class cols):")
    print(f"{'row':<16s} " + " ".join(f"{c[:7]:>7s}" for c in cols) + "  TOT")
    for i, r in enumerate(rows):
        row_sum = sum(tab[i])
        print(f"{r:<16s} " + " ".join(f"{tab[i][j]:>7d}" for j in range(len(cols))) + f"  {row_sum:>3d}")
    col_totals = [sum(tab[i][j] for i in range(len(tab))) for j in range(len(cols))]
    print(f"{'TOT':<16s} " + " ".join(f"{c:>7d}" for c in col_totals) + f"  {sum(col_totals):>3d}")
    print()
    print(f"Cell 1 χ² = {obs_chi2:.4f}, df = {df}")
    print(f"  Monte-Carlo p (N={N_PERM}): {p_mc:.6f}")
    print(f"  Null mean: {sum(null_dist)/len(null_dist):.3f}, q95: {sorted(null_dist)[int(0.95*len(null_dist))]:.3f}")
    print(f"  Verdict: {'REJECT' if p_mc < ALPHA_BON else 'FAIL-TO-REJECT'} at α_bon={ALPHA_BON}")
    print()
    print("Cell 2 — per-cluster χ² vs Uniform(9):")
    for k, r in per_cluster.items():
        print(f"  {k} (n={r['n']}): χ²={r['chi2_obs']:.3f}, p_mc={r['p_mc']:.4f}")
        for c, cnt in sorted(r['counts'].items(), key=lambda x: -x[1]):
            print(f"      {c}: {cnt}")
    print()
    print(f"Cell 3 — Cramer's V = {v:.4f} ({out['cell_3_cramers_v']['interpretation']})")
    print()
    print("Cell 4 — rank profile:")
    for k, lst in rank.items():
        print(f"  {k}: " + ", ".join(f"{c}={n}" for c, n in lst))
    print()
    print("Directional checks:")
    for k, vv in out["directional_checks"].items():
        print(f"  {k}: {vv}")


if __name__ == "__main__":
    main()
