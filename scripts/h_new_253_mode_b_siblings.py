#!/usr/bin/env python3
"""
H-NEW-253 — Mode B siblings: 4-cell M-principle portrait applied to all 114 surahs.

For each of 114 surahs, compute the same 20-metric M-principle portrait as
H-NEW-234, using leave-one-out percentile (reference n=113). Count:
 - extreme-metric count (total metrics at pct ≤ 5 or ≥ 95)
 - cell-count (number of M-cells M1/M2/M3/M5 with at least 1 extreme metric)
Rank surahs by cell-count (primary) then extreme-metric count (secondary).

Pre-reg: findings/phase-b-hypotheses/h-new-253-mode-b-siblings-prereg.md
Seed: 20260419.  Bonferroni k=2, alpha_bon=0.025.
"""
from __future__ import annotations
import csv
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path

SEED = 20260419
BASE = Path("/Users/grey/Downloads/quran")
CSV = BASE / "findings/phase-b-hypotheses/csv"
OUT_JSON = CSV / "h-new-253.json"
OUT_CSV = CSV / "h-new-253-all-surah-profile.csv"

HINGE_WINDOW = set(range(49, 58))  # cross-finding-018 / H-NEW-148 ±58 mirror pair
MODE_B_CANDIDATES_EXAMPLES = [55, 77, 26]  # from H-NEW-234 descriptive sibling block


# Known refrain surahs (from classical ʿilm al-munāsabāt; used in descriptive
# interpretive cell, NOT in primary cell-count computation)
REFRAIN_SURAHS = {
    54: "fa-hal min muddakir",
    55: "fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān",
    77: "waylun yawmaʾidhin lil-mukadhdhibīn",
    26: "fa-ayyuhā l-kādhibūn (inter-pericope)",
    109: "lā aʿbudu mā taʿbudūn (anaphoric)",
}

# Classical oath-opener surahs per H-NEW-196 (descriptive context)
OATH_OPENERS = {37, 51, 52, 53, 56, 68, 69, 70, 75, 77, 79, 81, 85, 86, 89, 90, 91, 92, 93, 95, 100, 103}

# Eschatological-hub block (H-NEW-234 / CF-019)
Q50_56_HUB = set(range(50, 57))


def load_csv(path: Path, key_col: str) -> dict[int, dict[str, str]]:
    out: dict[int, dict[str, str]] = {}
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            k = row.get(key_col)
            if k is None or k == "":
                continue
            try:
                out[int(k)] = row
            except ValueError:
                continue
    return out


def to_float(s):
    if s is None or s == "" or (isinstance(s, str) and s.lower() == "nan"):
        return None
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def loo_percentile(target_val: float, all_vals_by_sid: dict[int, float], target_sid: int) -> float:
    """Leave-one-out percentile: target's rank within the other n-1 surahs."""
    refs = [v for sid, v in all_vals_by_sid.items()
            if sid != target_sid and v is not None and not math.isnan(v)]
    if not refs or target_val is None or (isinstance(target_val, float) and math.isnan(target_val)):
        return float("nan")
    below = sum(1 for v in refs if v < target_val)
    equal = sum(1 for v in refs if v == target_val)
    return 100.0 * (below + 0.5 * equal) / len(refs)


def two_sided_extremity(pct: float) -> float:
    if pct is None or math.isnan(pct):
        return float("nan")
    return min(pct, 100.0 - pct)


def main() -> None:
    random.seed(SEED)

    # --- Load sources ---
    zipf = load_csv(CSV / "h-new-172-per-surah.csv", "surah_id")
    phono = load_csv(CSV / "h-new-182-surah-vectors.csv", "surah_id")
    entropy = load_csv(CSV / "h-new-195-per-surah.csv", "sid")
    acf = load_csv(CSV / "h-new-181-per-surah.csv", "sid")
    lz = load_csv(CSV / "h-new-187-per-surah.csv", "surah")
    disp = load_csv(CSV / "h-new-168-per-surah-dispersion.csv", "sid")
    zipf_class = load_csv(CSV / "zipf-per-surah.csv", "mushaf_order")

    # --- KL divergence from corpus (α=0.1 Dirichlet per H-NEW-234) ---
    kl_map: dict[int, float] = {}
    try:
        txt_path = BASE / "quran-text/quran-no-tashkeel.json"
        with txt_path.open() as f:
            qurtxt = json.load(f)
        corpus_counts: Counter = Counter()
        per_surah_counts: dict[int, Counter] = {}
        for s in qurtxt:
            sid = int(s["id"])
            sc: Counter = Counter()
            for v in s.get("verses", []):
                toks = v.get("text", "").split()
                sc.update(toks)
            per_surah_counts[sid] = sc
            corpus_counts.update(sc)
        V = len(corpus_counts)
        alpha = 0.1
        N_corpus = sum(corpus_counts.values())
        denom_corpus = N_corpus + alpha * V
        for sid, sc in per_surah_counts.items():
            N_s = sum(sc.values())
            denom_s = N_s + alpha * V
            kl = 0.0
            for w in corpus_counts:
                p_s = (sc.get(w, 0) + alpha) / denom_s
                p_c = (corpus_counts[w] + alpha) / denom_corpus
                kl += p_s * math.log(p_s / p_c)
            kl_map[sid] = kl
    except Exception as e:
        print(f"[warn] KL recompute failed: {e!r}")
        kl_map = {}

    # --- Build master frame ---
    master: dict[int, dict] = {}
    for sid in range(1, 115):
        row: dict = {"sid": sid}
        r172 = zipf.get(sid, {})
        row["N_tokens"] = to_float(r172.get("N"))
        row["zipf_alpha"] = to_float(r172.get("alpha"))
        row["heap_beta"] = to_float(r172.get("beta_h159"))
        row["is_muq"] = int(to_float(r172.get("is_muq")) or 0)

        r182 = phono.get(sid, {})
        row["emphatic"] = to_float(r182.get("emphatic"))
        row["pharyngeal"] = to_float(r182.get("pharyngeal"))

        r195 = entropy.get(sid, {})
        row["H_unigram"] = to_float(r195.get("H_unigram"))
        row["residual_H_cond"] = to_float(r195.get("residual_H_cond"))

        racf = acf.get(sid, {})
        row["z_Q_ljung_box"] = to_float(racf.get("z_Q"))
        row["acf_1"] = to_float(racf.get("acf_1"))
        row["acf_2"] = to_float(racf.get("acf_2"))
        row["max_abs_acf"] = to_float(racf.get("max_abs_acf"))

        rlz = lz.get(sid, {})
        row["lz_norm_log"] = to_float(rlz.get("lz_norm_log"))
        row["gzip_ratio"] = to_float(rlz.get("gzip_ratio"))

        rdisp = disp.get(sid, {})
        row["dispersion_h168"] = to_float(rdisp.get("dispersion"))

        rn = zipf_class.get(sid, {})
        row["noldeke_order"] = to_float(rn.get("noldeke_order"))

        row["kl_from_corpus"] = kl_map.get(sid)

        if row["zipf_alpha"] is not None and row["heap_beta"] is not None:
            row["alpha_beta_residual"] = row["zipf_alpha"] - (-3.526 * row["heap_beta"] + 3.689)
        else:
            row["alpha_beta_residual"] = None

        if row["noldeke_order"] is not None:
            row["mushaf_minus_noldeke"] = sid - row["noldeke_order"]
        else:
            row["mushaf_minus_noldeke"] = None

        master[sid] = row

    # --- Metric manifest (principle, name, kind) ---
    metrics_manifest = [
        # M1 (2)
        ("M1", "mushaf_position_is_structural_hinge", "boolean"),
        ("M1", "mushaf_minus_noldeke", "two_sided"),
        # M2 (2)
        ("M2", "is_muq", "boolean"),
        ("M2", "noldeke_order", "two_sided"),
        # M3 (8)
        ("M3", "residual_H_cond", "two_sided"),
        ("M3", "z_Q_ljung_box", "two_sided"),
        ("M3", "acf_1", "two_sided"),
        ("M3", "acf_2", "two_sided"),
        ("M3", "max_abs_acf", "two_sided"),
        ("M3", "H_unigram", "two_sided"),
        ("M3", "emphatic", "two_sided"),
        ("M3", "pharyngeal", "two_sided"),
        # M5 (8)
        ("M5", "N_tokens", "two_sided"),
        ("M5", "kl_from_corpus", "two_sided"),
        ("M5", "zipf_alpha", "two_sided"),
        ("M5", "heap_beta", "two_sided"),
        ("M5", "alpha_beta_residual", "two_sided"),
        ("M5", "lz_norm_log", "two_sided"),
        ("M5", "gzip_ratio", "two_sided"),
        ("M5", "dispersion_h168", "two_sided"),
    ]

    # --- Pre-compute per-metric value arrays by sid ---
    metric_vals: dict[str, dict[int, float]] = {}
    for _, m, kind in metrics_manifest:
        if m in ("mushaf_position_is_structural_hinge",):
            continue
        metric_vals[m] = {sid: master[sid].get(m) for sid in range(1, 115)
                          if master[sid].get(m) is not None
                          and not (isinstance(master[sid].get(m), float) and math.isnan(master[sid].get(m)))}

    # --- Per-surah portrait ---
    surah_portraits: dict[int, dict] = {}

    def is_extreme_for(sid: int, metric: str, kind: str) -> tuple[bool, float, float]:
        """Return (is_extreme, pct, extremity) for a single (sid, metric)."""
        val = master[sid].get(metric)
        if metric == "mushaf_position_is_structural_hinge":
            # Boolean hit: in window → extreme (True); else TYPICAL
            hit = 1 if sid in HINGE_WINDOW else 0
            return (hit == 1, float("nan"), 0.0 if hit else 50.0)
        if metric == "is_muq":
            # Muq boolean: "extreme" is being muq (True). ~25/113 = 22%.
            # For uniformity with H-NEW-234 (which called Q 55 non-muq
            # "TYPICAL"), treat being muq as 1-direction extreme only.
            return (val == 1, float("nan"), 0.0 if val == 1 else 50.0)
        if val is None or (isinstance(val, float) and math.isnan(val)):
            return (False, float("nan"), float("nan"))
        pct = loo_percentile(val, metric_vals[metric], sid)
        ext = two_sided_extremity(pct)
        is_ext = (not math.isnan(ext)) and (ext <= 5.0)
        return (is_ext, pct, ext)

    for sid in range(1, 115):
        portrait: dict = {
            "sid": sid,
            "metrics": [],
            "extreme_metrics_count": 0,
            "cells": defaultdict(lambda: {"extreme_metrics": [], "n_extreme": 0}),
        }
        cells_with_extreme: set[str] = set()
        for principle, metric, kind in metrics_manifest:
            is_ext, pct, ext = is_extreme_for(sid, metric, kind)
            val = master[sid].get(metric)
            portrait["metrics"].append({
                "principle": principle,
                "metric": metric,
                "value": val,
                "percentile": pct,
                "extremity": ext,
                "is_extreme": is_ext,
            })
            if is_ext:
                portrait["extreme_metrics_count"] += 1
                portrait["cells"][principle]["extreme_metrics"].append(metric)
                portrait["cells"][principle]["n_extreme"] += 1
                cells_with_extreme.add(principle)
        portrait["cells"] = dict(portrait["cells"])
        portrait["cell_count"] = len(cells_with_extreme)
        portrait["cells_extreme"] = sorted(cells_with_extreme)
        surah_portraits[sid] = portrait

    # --- Rank by cell-count desc, then extreme-metric count desc ---
    ranked = sorted(
        surah_portraits.values(),
        key=lambda p: (-p["cell_count"], -p["extreme_metrics_count"], p["sid"]),
    )

    # --- Top-10 ---
    top10 = ranked[:10]

    # --- MW-5 random-feature-label permutation ---
    #   Shuffle (principle) labels across metrics 1000 times; recompute
    #   surah cell-counts; record #{surahs at cell-count ≥ 3}.
    baseline_ge3 = sum(1 for p in surah_portraits.values() if p["cell_count"] >= 3)

    # For the permutation we use the precomputed is_extreme boolean per
    # (sid, metric) (these do NOT depend on the principle label).
    sid_metric_extreme: dict[int, dict[str, bool]] = {}
    for sid in range(1, 115):
        d = {}
        for mrec in surah_portraits[sid]["metrics"]:
            d[mrec["metric"]] = mrec["is_extreme"]
        sid_metric_extreme[sid] = d

    principles_list = [p for (p, _, _) in metrics_manifest]
    metrics_list = [m for (_, m, _) in metrics_manifest]

    perm_counts = []
    rng = random.Random(SEED + 1)
    for _ in range(1000):
        shuffled = principles_list[:]
        rng.shuffle(shuffled)
        assign = dict(zip(metrics_list, shuffled))
        ge3 = 0
        for sid in range(1, 115):
            cells = set()
            for m, is_ext in sid_metric_extreme[sid].items():
                if is_ext:
                    cells.add(assign[m])
            if len(cells) >= 3:
                ge3 += 1
        perm_counts.append(ge3)
    perm_counts.sort()
    # Empirical p: P(perm_ge3 >= baseline_ge3)
    p_mw5 = sum(1 for c in perm_counts if c >= baseline_ge3) / len(perm_counts)
    null_mean = sum(perm_counts) / len(perm_counts)
    null_sd = math.sqrt(sum((c - null_mean) ** 2 for c in perm_counts) / len(perm_counts))

    # --- Interpretive: shared content-profile analysis ---
    candidates_ge3 = [p for p in ranked if p["cell_count"] >= 3]
    cand_sids = [p["sid"] for p in candidates_ge3]
    cand_analysis = {
        "candidates": cand_sids,
        "n_refrain": sum(1 for s in cand_sids if s in REFRAIN_SURAHS),
        "n_oath_opener": sum(1 for s in cand_sids if s in OATH_OPENERS),
        "n_in_Q50_56_hub": sum(1 for s in cand_sids if s in Q50_56_HUB),
        "n_muq": sum(1 for s in cand_sids if master[s].get("is_muq") == 1),
    }

    # --- Verdict ---
    n_ge3 = len(candidates_ge3)
    if n_ge3 >= 3 and p_mw5 < 0.025:
        verdict = "REPLICABLE-CATEGORY (≥3 candidates at p < 0.025)"
    elif n_ge3 >= 3:
        verdict = f"DESCRIPTIVE-CATEGORY (≥3 candidates but MW-5 p={p_mw5:.4f} not < 0.025)"
    elif n_ge3 == 2:
        verdict = "2-EXEMPLAR phenomenon (Q 55 + one sibling)"
    elif n_ge3 == 1:
        verdict = "Q 55-UNIQUE (ʿarūs al-Qurʾān empirically unique)"
    else:
        verdict = "NO Mode B signature found"

    # --- Output ---
    out = {
        "id": "H-NEW-253",
        "seed": SEED,
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "n_surahs": 114,
        "n_metrics": len(metrics_manifest),
        "baseline_n_surahs_cell_count_ge3": baseline_ge3,
        "mw5": {
            "n_permutations": 1000,
            "null_mean_surahs_ge3": null_mean,
            "null_sd": null_sd,
            "null_max": max(perm_counts),
            "null_min": min(perm_counts),
            "p_empirical": p_mw5,
        },
        "top_20": [
            {
                "rank": i + 1,
                "sid": p["sid"],
                "cell_count": p["cell_count"],
                "cells_extreme": p["cells_extreme"],
                "extreme_metrics_count": p["extreme_metrics_count"],
                "extreme_metrics_by_cell": {k: v["extreme_metrics"] for k, v in p["cells"].items()},
            }
            for i, p in enumerate(ranked[:20])
        ],
        "candidate_ge3_shared_profile": cand_analysis,
        "verdict": verdict,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False))

    with OUT_CSV.open("w") as f:
        w = csv.writer(f)
        w.writerow(["sid", "cell_count", "extreme_metrics_count", "cells_extreme",
                    "M1_extreme", "M2_extreme", "M3_extreme", "M5_extreme"])
        for p in ranked:
            m1 = ";".join(p["cells"].get("M1", {"extreme_metrics": []}).get("extreme_metrics", []))
            m2 = ";".join(p["cells"].get("M2", {"extreme_metrics": []}).get("extreme_metrics", []))
            m3 = ";".join(p["cells"].get("M3", {"extreme_metrics": []}).get("extreme_metrics", []))
            m5 = ";".join(p["cells"].get("M5", {"extreme_metrics": []}).get("extreme_metrics", []))
            w.writerow([p["sid"], p["cell_count"], p["extreme_metrics_count"],
                        ",".join(p["cells_extreme"]), m1, m2, m3, m5])

    # --- Console summary ---
    print(f"=== H-NEW-253 Mode B siblings (seed {SEED}) ===")
    print(f"  n_surahs = 114, n_metrics = {len(metrics_manifest)}")
    print(f"  Baseline: #{{surahs with cell_count ≥ 3}} = {baseline_ge3}")
    print(f"  MW-5 null: mean={null_mean:.2f} sd={null_sd:.2f} max={max(perm_counts)} p={p_mw5:.4f}")
    print(f"\n  Top-10 Mode-B candidates (cell_count desc, ext_metric desc):")
    for i, p in enumerate(ranked[:10]):
        print(f"  rank {i+1:2d}: Q{p['sid']:3d}  cell_count={p['cell_count']}  "
              f"extreme_metrics={p['extreme_metrics_count']:2d}  "
              f"cells={p['cells_extreme']}")
    print(f"\n  Candidates cell_count≥3: {cand_sids}")
    print(f"    n_refrain: {cand_analysis['n_refrain']} / {len(cand_sids)}")
    print(f"    n_oath_opener: {cand_analysis['n_oath_opener']} / {len(cand_sids)}")
    print(f"    n_in_Q50_56_hub: {cand_analysis['n_in_Q50_56_hub']} / {len(cand_sids)}")
    print(f"    n_muq: {cand_analysis['n_muq']} / {len(cand_sids)}")
    print(f"\n*** Verdict: {verdict} ***")


if __name__ == "__main__":
    main()
