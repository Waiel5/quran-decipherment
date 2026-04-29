"""H-NEW-200 — Surah-name etymology class × cluster prediction.

Pre-reg: findings/phase-b-hypotheses/h-new-200-name-class-predictor-prereg.md

Tests:
  T1 — Mushaf position vs 9-class etymology (Kruskal-Wallis H + permutation p)
  T2 — Meccan/Medinan vs 9-class etymology (χ² + permutation p; pool if min-exp < 5)
  T3 — Nöldeke compositional-phase (4-way) vs 9-class etymology (χ² + permutation p; pool if min-exp < 5)

Seed: 20260419 ; Bonferroni k=3 ; α_bon = 0.0167
"""
from __future__ import annotations

import csv
import json
import math
import os
import random
import sys
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))

# Reuse locked taxonomy from H-NEW-49
sys.path.insert(0, os.path.join(REPO, "scripts"))
from h_new_49_surah_name_class import SURAH_CLASS, CLASSES  # noqa: E402

SEED = 20260419
N_PERM = 100_000
BON_K = 3
ALPHA_BON = 0.05 / BON_K  # 0.01667
N_SURAHS = 114

REV_ORDER_CSV = os.path.join(REPO, "data", "revelation-order.csv")


def load_revelation_order() -> Dict[int, Dict[str, str]]:
    """Return mushaf_id -> {revelation_order, type, noldeke_phase}."""
    out: Dict[int, Dict[str, str]] = {}
    with open(REV_ORDER_CSV, "r", encoding="utf-8") as fh:
        rdr = csv.DictReader(fh)
        for row in rdr:
            sid = int(row["mushaf_order"])
            out[sid] = {
                "revelation_order": int(row["revelation_order"]),
                "type": row["period"].strip().lower(),  # "meccan" or "medinan"
                "noldeke_order": int(row["noldeke_order"]),
                "noldeke_phase": row["noldeke_phase"].strip(),  # "Early Meccan", etc.
            }
    assert len(out) == N_SURAHS
    return out


# ----------------------------------------------------------------------
# Stat helpers (no scipy)
# ----------------------------------------------------------------------

def chi2_contingency(observed: List[List[float]]) -> Tuple[float, int, List[List[float]]]:
    """Pearson χ² for a contingency table. Returns (chi2, df, expected)."""
    rows = len(observed)
    cols = len(observed[0]) if rows else 0
    row_tot = [sum(r) for r in observed]
    col_tot = [sum(observed[i][j] for i in range(rows)) for j in range(cols)]
    grand = sum(row_tot)
    if grand == 0:
        return (0.0, 0, observed)
    expected = [[row_tot[i] * col_tot[j] / grand for j in range(cols)]
                for i in range(rows)]
    chi2 = 0.0
    for i in range(rows):
        for j in range(cols):
            e = expected[i][j]
            if e > 0:
                chi2 += (observed[i][j] - e) ** 2 / e
    df = (rows - 1) * (cols - 1)
    return (chi2, df, expected)


def kruskal_wallis(groups: List[List[float]]) -> Tuple[float, int]:
    """Kruskal-Wallis H with tie correction.

    Returns (H, df). groups is list of arrays of values for each class.
    """
    all_vals: List[Tuple[float, int]] = []
    for gi, g in enumerate(groups):
        for v in g:
            all_vals.append((v, gi))
    all_vals.sort(key=lambda x: x[0])
    N = len(all_vals)
    # Compute ranks (midranks for ties)
    ranks = [0.0] * N
    i = 0
    tie_corr_sum = 0.0
    while i < N:
        j = i
        while j + 1 < N and all_vals[j + 1][0] == all_vals[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1.0  # 1-indexed midrank
        t = j - i + 1
        if t > 1:
            tie_corr_sum += t ** 3 - t
        for k in range(i, j + 1):
            ranks[k] = avg_rank
        i = j + 1
    # Sum ranks per group
    sum_r: Dict[int, float] = defaultdict(float)
    n_r: Dict[int, int] = defaultdict(int)
    for idx, (_v, gi) in enumerate(all_vals):
        sum_r[gi] += ranks[idx]
        n_r[gi] += 1
    H = 12.0 / (N * (N + 1)) * sum((sum_r[gi] ** 2) / n_r[gi] for gi in sum_r) - 3 * (N + 1)
    # Tie correction
    if tie_corr_sum > 0 and N > 1:
        C = 1 - tie_corr_sum / (N ** 3 - N)
        if C > 0:
            H = H / C
    df = len(groups) - 1
    return (H, df)


def pool_low_expected(
    observed_rows: List[List[int]],
    col_names: List[str],
    pool_order: List[str],
) -> Tuple[List[List[int]], List[str]]:
    """Pool columns (classes) in pool_order until min expected ≥ 5."""
    cols = list(col_names)
    tab = [list(r) for r in observed_rows]
    while True:
        _chi2, _df, exp = chi2_contingency(tab)
        min_exp = min(min(r) for r in exp) if exp else 0.0
        if min_exp >= 5.0:
            break
        # Find next col in pool_order that is still unpooled
        to_pool_name = None
        for name in pool_order:
            if name in cols:
                to_pool_name = name
                break
        if to_pool_name is None:
            break
        # Merge into POOLED_OTHER (create if needed)
        pi = cols.index(to_pool_name)
        if "POOLED_OTHER" not in cols:
            # Rename this col
            cols[pi] = "POOLED_OTHER"
        else:
            # Merge into existing POOLED_OTHER
            po = cols.index("POOLED_OTHER")
            for i in range(len(tab)):
                tab[i][po] += tab[i][pi]
            # Drop pi
            for i in range(len(tab)):
                del tab[i][pi]
            del cols[pi]
    return tab, cols


# ----------------------------------------------------------------------
# Build the data frame
# ----------------------------------------------------------------------

def build_table() -> List[dict]:
    """Build per-surah records with class + mushaf + type + phase."""
    rev = load_revelation_order()
    records: List[dict] = []
    for sid in range(1, N_SURAHS + 1):
        translit, gloss, cls, roots = SURAH_CLASS[sid]
        r = rev[sid]
        records.append({
            "surah_id": sid,
            "translit": translit,
            "gloss": gloss,
            "class": cls,
            "mushaf_rank": sid,  # mushaf ID is the mushaf rank
            "revelation_order": r["revelation_order"],
            "type": r["type"],
            "noldeke_phase": r["noldeke_phase"],
        })
    return records


# ----------------------------------------------------------------------
# T1 — Mushaf position vs class (Kruskal-Wallis + permutation)
# ----------------------------------------------------------------------

def t1_mushaf_position(records: List[dict], rng: random.Random) -> dict:
    classes = CLASSES
    # Build groups
    groups = [[] for _ in classes]
    cls_of_sid = [None] * (N_SURAHS + 1)
    for rec in records:
        gi = classes.index(rec["class"])
        groups[gi].append(rec["mushaf_rank"])
        cls_of_sid[rec["surah_id"]] = gi
    H_obs, df = kruskal_wallis(groups)
    # Class medians
    medians = {}
    for i, g in enumerate(groups):
        if g:
            sg = sorted(g)
            m = len(sg)
            med = sg[m // 2] if m % 2 == 1 else 0.5 * (sg[m // 2 - 1] + sg[m // 2])
            medians[classes[i]] = med
        else:
            medians[classes[i]] = None
    # Class sizes
    sizes = {classes[i]: len(g) for i, g in enumerate(groups)}

    # Permutation test: shuffle class-labels across the 114 surahs.
    all_vals = [rec["mushaf_rank"] for rec in records]
    all_labels_tmpl = [classes.index(rec["class"]) for rec in records]
    n_cls = len(classes)
    perm_labels = list(all_labels_tmpl)
    n_greater_eq = 0
    for it in range(N_PERM):
        rng.shuffle(perm_labels)
        g = [[] for _ in range(n_cls)]
        for i, lab in enumerate(perm_labels):
            g[lab].append(all_vals[i])
        H_p, _ = kruskal_wallis(g)
        if H_p >= H_obs:
            n_greater_eq += 1
    p_perm = (n_greater_eq + 1) / (N_PERM + 1)
    return {
        "test": "Kruskal-Wallis H on mushaf_rank across 9 etymology classes",
        "H_obs": H_obs,
        "df": df,
        "n_perm": N_PERM,
        "n_perm_ge_obs": n_greater_eq,
        "p_perm_two_sided": p_perm,
        "class_sizes": sizes,
        "class_medians_mushaf_rank": medians,
        "alpha_bon": ALPHA_BON,
        "pass_at_alpha_bon": p_perm < ALPHA_BON,
    }


# ----------------------------------------------------------------------
# T2 — Meccan/Medinan vs class (χ² + permutation)
# ----------------------------------------------------------------------

def t2_meccan_medinan(records: List[dict], rng: random.Random) -> dict:
    classes = CLASSES
    # Build 2xK table: rows = [meccan, medinan]
    row_names = ["meccan", "medinan"]
    tab = [[0 for _ in classes] for _ in row_names]
    for rec in records:
        ri = row_names.index(rec["type"])
        ci = classes.index(rec["class"])
        tab[ri][ci] += 1

    # Pool if needed
    pool_order = ["OTHER_ABSTRACT", "MUQATTAAT_LETTER", "REVELATION_RITUAL"]
    tab_used, cols_used = pool_low_expected(tab, list(classes), pool_order)
    chi2_obs, df_used, exp_used = chi2_contingency(tab_used)
    # Also record full table
    chi2_full, df_full, exp_full = chi2_contingency(tab)

    # Permutation: shuffle class labels across 114; recompute χ² on SAME pooling scheme
    # (we need to re-apply the pooling on each perm? pre-reg says pooling is on observed
    # table; we use the same col set as observed pooling.)
    sids_labels = [classes.index(rec["class"]) for rec in records]
    types_idx = [row_names.index(rec["type"]) for rec in records]
    # Determine which class-indices got pooled into POOLED_OTHER
    if "POOLED_OTHER" in cols_used:
        pooled_set = set()
        kept_cols = []
        for name in classes:
            if name in cols_used:
                kept_cols.append(name)
            else:
                pooled_set.add(classes.index(name))
        # Build mapping: class_idx -> col in perm table
        col_map = {}
        for ci, cname in enumerate(classes):
            if cname in cols_used:
                col_map[ci] = cols_used.index(cname)
            else:
                col_map[ci] = cols_used.index("POOLED_OTHER")
    else:
        kept_cols = list(classes)
        col_map = {i: i for i in range(len(classes))}

    n_cls_used = len(cols_used)
    perm_labels = list(sids_labels)
    n_greater_eq = 0
    for _ in range(N_PERM):
        rng.shuffle(perm_labels)
        ptab = [[0 for _ in range(n_cls_used)] for _ in row_names]
        for i, cidx in enumerate(perm_labels):
            ptab[types_idx[i]][col_map[cidx]] += 1
        chi2_p, _, _ = chi2_contingency(ptab)
        if chi2_p >= chi2_obs:
            n_greater_eq += 1
    p_perm = (n_greater_eq + 1) / (N_PERM + 1)

    return {
        "test": "χ² Meccan/Medinan × class (pooled if needed)",
        "table_full_observed": tab,
        "classes_full": list(classes),
        "row_names": row_names,
        "table_used_observed": tab_used,
        "classes_used": cols_used,
        "expected_used": exp_used,
        "chi2_full": chi2_full,
        "df_full": df_full,
        "chi2_obs": chi2_obs,
        "df_used": df_used,
        "n_perm": N_PERM,
        "n_perm_ge_obs": n_greater_eq,
        "p_perm": p_perm,
        "alpha_bon": ALPHA_BON,
        "pass_at_alpha_bon": p_perm < ALPHA_BON,
    }


# ----------------------------------------------------------------------
# T3 — Nöldeke phase (4-way) vs class (χ² + permutation)
# ----------------------------------------------------------------------

def t3_noldeke_phase(records: List[dict], rng: random.Random) -> dict:
    classes = CLASSES
    phase_names = ["Early Meccan", "Middle Meccan", "Late Meccan", "Medinan"]
    tab = [[0 for _ in classes] for _ in phase_names]
    for rec in records:
        ri = phase_names.index(rec["noldeke_phase"])
        ci = classes.index(rec["class"])
        tab[ri][ci] += 1

    pool_order = ["OTHER_ABSTRACT", "MUQATTAAT_LETTER", "REVELATION_RITUAL"]
    tab_used, cols_used = pool_low_expected(tab, list(classes), pool_order)
    chi2_obs, df_used, exp_used = chi2_contingency(tab_used)
    chi2_full, df_full, exp_full = chi2_contingency(tab)

    phase_idx = [phase_names.index(rec["noldeke_phase"]) for rec in records]
    sids_labels = [classes.index(rec["class"]) for rec in records]
    if "POOLED_OTHER" in cols_used:
        col_map = {}
        for ci, cname in enumerate(classes):
            if cname in cols_used:
                col_map[ci] = cols_used.index(cname)
            else:
                col_map[ci] = cols_used.index("POOLED_OTHER")
    else:
        col_map = {i: i for i in range(len(classes))}

    n_cls_used = len(cols_used)
    perm_labels = list(sids_labels)
    n_greater_eq = 0
    for _ in range(N_PERM):
        rng.shuffle(perm_labels)
        ptab = [[0 for _ in range(n_cls_used)] for _ in phase_names]
        for i, cidx in enumerate(perm_labels):
            ptab[phase_idx[i]][col_map[cidx]] += 1
        chi2_p, _, _ = chi2_contingency(ptab)
        if chi2_p >= chi2_obs:
            n_greater_eq += 1
    p_perm = (n_greater_eq + 1) / (N_PERM + 1)

    return {
        "test": "χ² Nöldeke 4-phase × class (pooled if needed)",
        "phases": phase_names,
        "table_full_observed": tab,
        "classes_full": list(classes),
        "table_used_observed": tab_used,
        "classes_used": cols_used,
        "expected_used": exp_used,
        "chi2_full": chi2_full,
        "df_full": df_full,
        "chi2_obs": chi2_obs,
        "df_used": df_used,
        "n_perm": N_PERM,
        "n_perm_ge_obs": n_greater_eq,
        "p_perm": p_perm,
        "alpha_bon": ALPHA_BON,
        "pass_at_alpha_bon": p_perm < ALPHA_BON,
    }


# ----------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------

def main():
    print(f"H-NEW-200 — seed={SEED}, N_PERM={N_PERM}, Bon-k={BON_K}, α_bon={ALPHA_BON:.5f}")
    rng = random.Random(SEED)

    records = build_table()

    # Class distribution
    class_dist = Counter(r["class"] for r in records)
    print("\nClass distribution (9-way):")
    for c in CLASSES:
        print(f"  {c:25s} {class_dist.get(c, 0):3d}")

    # T1
    print("\n--- T1: Mushaf position vs class (Kruskal-Wallis) ---")
    t1 = t1_mushaf_position(records, rng)
    print(f"H_obs = {t1['H_obs']:.4f} (df={t1['df']})")
    print(f"Perm p (two-sided) = {t1['p_perm_two_sided']:.6f}  (PASS={t1['pass_at_alpha_bon']})")
    print("Class medians (mushaf-rank):")
    for c, m in t1["class_medians_mushaf_rank"].items():
        print(f"  {c:25s}  n={t1['class_sizes'][c]:3d}  median_rank={m}")

    # T2
    print("\n--- T2: Meccan/Medinan vs class (χ²) ---")
    t2 = t2_meccan_medinan(records, rng)
    print(f"χ²_obs = {t2['chi2_obs']:.4f} (df_used={t2['df_used']}); classes_used={t2['classes_used']}")
    print(f"Perm p = {t2['p_perm']:.6f}  (PASS={t2['pass_at_alpha_bon']})")
    print(f"Full table (no pooling) χ² = {t2['chi2_full']:.4f} (df={t2['df_full']})")

    # T3
    print("\n--- T3: Nöldeke phase (4-way) vs class (χ²) ---")
    t3 = t3_noldeke_phase(records, rng)
    print(f"χ²_obs = {t3['chi2_obs']:.4f} (df_used={t3['df_used']}); classes_used={t3['classes_used']}")
    print(f"Perm p = {t3['p_perm']:.6f}  (PASS={t3['pass_at_alpha_bon']})")
    print(f"Full table (no pooling) χ² = {t3['chi2_full']:.4f} (df={t3['df_full']})")

    # Save
    out_dir_csv = os.path.join(REPO, "findings/phase-b-hypotheses/csv")
    os.makedirs(out_dir_csv, exist_ok=True)
    out_json = os.path.join(out_dir_csv, "h-new-200.json")
    out = {
        "id": "H-NEW-200",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": BON_K,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(hafs-kufan; no-tashkeel; canonical 114; Tanzil+Wikipedia Nöldeke rev-order; locked H-NEW-49 9-way taxonomy)",
        "n_surahs": N_SURAHS,
        "classes": CLASSES,
        "class_distribution": dict(class_dist),
        "T1_mushaf_position": t1,
        "T2_meccan_medinan": t2,
        "T3_noldeke_phase": t3,
    }
    with open(out_json, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
    print(f"\nSaved -> {out_json}")

    # Per-surah CSV
    out_csv = os.path.join(out_dir_csv, "h-new-200-per-surah.csv")
    with open(out_csv, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["surah_id", "translit", "gloss", "class",
                    "mushaf_rank", "revelation_order", "type", "noldeke_phase"])
        for rec in records:
            w.writerow([rec["surah_id"], rec["translit"], rec["gloss"], rec["class"],
                        rec["mushaf_rank"], rec["revelation_order"], rec["type"],
                        rec["noldeke_phase"]])
    print(f"Saved -> {out_csv}")

    # Short verdict
    print("\n=== VERDICT ===")
    for key, res in [("T1 mushaf-pos", t1), ("T2 meccan/medinan", t2), ("T3 noldeke-phase", t3)]:
        p = res.get("p_perm_two_sided", res.get("p_perm"))
        print(f"  {key:25s} p_perm={p:.6f}  {'PASS' if p < ALPHA_BON else 'NULL'} @ α_bon={ALPHA_BON:.5f}")


if __name__ == "__main__":
    main()
