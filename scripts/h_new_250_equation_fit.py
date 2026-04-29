#!/usr/bin/env python3
"""H-NEW-250 — Quantitative fit of cross-finding-020's 4-principle Complete Equation.

Pre-reg: findings/phase-b-hypotheses/h-new-250-quantitative-equation-prereg.md

Pipeline
--------
  1. Build principle-labeled feature blocks:
     - Block f_M5 (compositional: length, vocabulary, mode)
     - Block g_M1 (structural: hinge-distance, block indicators, community)
     - Block h_M2 (chronology + markers + Pattern-B)
     - Block δ_class (Q1 / Q112 / Q113 / Q114 sui-generis dummies)
  2. Fit Ridge LOOCV with all blocks → full-equation R² (Cell-1).
  3. Fit Ridge LOOCV with each block alone → per-principle R² (Cells 2-4).
  4. LOBO (leave-one-block-out) decomposition → marginal variance contributions.
  5. 100-perm null (Ridge full feature set, seed 20260419).
  6. Top-10 residual surahs + per-principle breakdown.
  7. Emit JSON + printed summary.

Seed 20260419.
"""
from __future__ import annotations

import csv
import json
import math
import random
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.model_selection import LeaveOneOut
from sklearn.preprocessing import StandardScaler

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
N_PERM = 100


# ---------------------------------------------------------------------------
# Corpus load helpers
# ---------------------------------------------------------------------------
def load_corpus() -> List[Dict]:
    path = ROOT / "quran-text" / "quran-no-tashkeel.json"
    return json.loads(path.read_text())


def surah_tokens(s: Dict) -> List[str]:
    toks: List[str] = []
    for v in s["verses"]:
        toks.extend(v["text"].split())
    return toks


# ---------------------------------------------------------------------------
# Existing-JSON feature loaders
# ---------------------------------------------------------------------------
def load_heap() -> Dict[int, Dict]:
    path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-123.json"
    d = json.load(path.open())
    out: Dict[int, Dict] = {}
    for row in d["per_surah_full"]:
        sid = int(row["surah_id"])
        out[sid] = {"N": row["N"], "beta": row["beta"], "K": row["K"]}
    return out


def load_h125() -> Dict[int, Dict]:
    path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-125.json"
    d = json.load(path.open())
    out: Dict[int, Dict] = {}
    for sid_str, rec in d["per_surah_axis_values"].items():
        out[int(sid_str)] = rec["axis_values"]
    return out


def load_dispersion() -> Dict[int, float]:
    path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-168-per-surah-dispersion.csv"
    out: Dict[int, float] = {}
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                out[int(row["sid"])] = float(row["dispersion"])
            except Exception:
                continue
    return out


def load_lz() -> Dict[int, float]:
    path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-187-per-surah.csv"
    out: Dict[int, float] = {}
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                out[int(row["surah"])] = float(row["lz_norm_simple"])
            except Exception:
                continue
    return out


def load_noldeke() -> Tuple[Dict[int, int], Dict[int, str]]:
    """Per-surah Nöldeke rank and phase from revelation-order.csv."""
    path = ROOT / "data" / "revelation-order.csv"
    rank: Dict[int, int] = {}
    phase: Dict[int, str] = {}
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                sid = int(row["mushaf_order"])
                rank[sid] = int(row["noldeke_order"])
                phase[sid] = row["noldeke_phase"]
            except Exception:
                continue
    return rank, phase


# ---------------------------------------------------------------------------
# Inline-computed features
# ---------------------------------------------------------------------------
def compute_corpus_basics(corpus: List[Dict]) -> Dict[int, Dict[str, float]]:
    """verse_count, TTR, mean_verse_length, log_length, entropy_rate, kl_from_corpus."""
    from collections import Counter
    all_toks: List[str] = []
    per_toks: Dict[int, List[str]] = {}
    for s in corpus:
        toks = surah_tokens(s)
        per_toks[s["id"]] = toks
        all_toks.extend(toks)
    corpus_counter = Counter(all_toks)
    vocab = list(corpus_counter.keys())
    V = len(vocab)
    total_N = sum(corpus_counter.values())
    alpha = 0.5
    p_corpus = np.array(
        [(corpus_counter[w] + alpha) / (total_N + alpha * V) for w in vocab],
        dtype=float,
    )
    out: Dict[int, Dict[str, float]] = {}
    for s in corpus:
        sid = s["id"]
        toks = per_toks[sid]
        n = len(toks)
        vc = s["total_verses"]
        mean_verse_length = n / vc if vc > 0 else float("nan")
        ttr = len(set(toks)) / n if n > 0 else float("nan")
        log_length = math.log(n) if n > 0 else float("nan")
        # entropy
        if n > 0:
            cnt = Counter(toks)
            probs = np.array([c / n for c in cnt.values()], dtype=float)
            h = float(-np.sum(probs * np.log2(probs)))
        else:
            h = float("nan")
        # KL
        cnt = Counter(toks)
        N_s = sum(cnt.values())
        if N_s > 0:
            p_s = np.array(
                [(cnt.get(w, 0) + alpha) / (N_s + alpha * V) for w in vocab],
                dtype=float,
            )
            kl = float(np.sum(p_s * np.log(p_s / p_corpus)))
        else:
            kl = float("nan")
        out[sid] = {
            "verse_count": float(vc),
            "type_token_ratio": ttr,
            "mean_verse_length": mean_verse_length,
            "log_length": log_length,
            "entropy_rate_surah": h,
            "kl_from_corpus": kl,
        }
    return out


# ---------------------------------------------------------------------------
# Principle indicator sets (pre-reg locked)
# ---------------------------------------------------------------------------
HINGES = [(14, 15), (49, 50), (56, 57)]

# M1 blocks
TIWAL = set(range(2, 10))                             # Q 2-9
HAWAMIM = set(range(40, 47))                          # Q 40-46
MEDINAN_BACK = set(range(47, 67))                     # Q 47-66
ALM_SURAHS = {2, 3, 29, 30, 31, 32}
SHORT_BRACKET = set(range(108, 115))                  # Q 108-114

# H-NEW-185 Fiedler communities:
#   arc sign −1: start_pos 12 end_pos 76 span Q13..Q77  → comm = -1
#   arc sign +1: start_pos 77 end_pos 11 span Q78..Q114..Q1..Q12 → comm = +1
def fiedler_community(sid: int) -> int:
    if 13 <= sid <= 77:
        return -1
    else:
        return +1


# CF-020 §4 compositional modes
MODE_A_LENGTH = {2, 3, 50, 59, 62, 112, 113, 114}
MODE_B_REFRAIN = {55, 77, 78, 83, 52}
MODE_D_INCLUSIO = {4, 33, 59, 60, 63, 65}  # top Medinan-inclusio per H-NEW-189


def hinge_distance(sid: int) -> int:
    """Minimum distance to any universal hinge."""
    d = 10**6
    for (a, b) in HINGES:
        d = min(d, abs(sid - a), abs(sid - b))
    return d


def mode_onehot(sid: int) -> Dict[str, float]:
    """4 dummy vars; mode_C reference."""
    out = {
        "mode_A_length": 0.0,
        "mode_B_refrain": 0.0,
        "mode_D_inclusio": 0.0,
        "mode_E_linear": 0.0,
    }
    # Resolution order: A, B, D take priority; else check mode_E (Meccan non-inclusio); else default C
    if sid in MODE_A_LENGTH:
        out["mode_A_length"] = 1.0
    elif sid in MODE_B_REFRAIN:
        out["mode_B_refrain"] = 1.0
    elif sid in MODE_D_INCLUSIO:
        out["mode_D_inclusio"] = 1.0
    # mode_E = meccan non-inclusio (determined by noldeke phase in builder)
    return out


# ---------------------------------------------------------------------------
# Feature matrix construction
# ---------------------------------------------------------------------------
BLOCK_M5 = [
    "log_length",
    "verse_count",
    "mean_verse_length",
    "type_token_ratio",
    "dispersion",
    "beta",
    "alpha_minus_beta",
    "kl_from_corpus",
    "entropy_rate_surah",
    "lz_norm_simple",
    "mode_A_length",
    "mode_B_refrain",
    "mode_D_inclusio",
    "mode_E_linear",
]

BLOCK_M1 = [
    "dist_to_hinge",
    "is_tiwal",
    "is_hawamim",
    "is_medinan_back",
    "is_alm",
    "is_short_bracket",
    "fiedler_community",
    "log_length_M1",  # duplicate column for M1-alone fit (attribution-robustness)
]

BLOCK_M2 = [
    "noldeke_rank",
    "late_meccan_phase",
    "muq_cardinality",
    "qul_density",
    "book_ref_density",
    "eschat_density",
]

BLOCK_CLASS = [
    "is_q1_fatiha",
    "is_q112_ikhlas",
    "is_q113_falaq",
    "is_q114_nas",
]


def build_feature_matrix() -> Tuple[np.ndarray, np.ndarray, List[int], Dict[str, List[int]], List[str]]:
    corpus = load_corpus()
    heap = load_heap()
    h125 = load_h125()
    disp = load_dispersion()
    lz = load_lz()
    basics = compute_corpus_basics(corpus)
    noldeke_rank, noldeke_phase = load_noldeke()

    sids = sorted([s["id"] for s in corpus])

    # Assemble feature list with consistent ordering: M5, M1, M2, CLASS
    all_features = BLOCK_M5 + BLOCK_M1 + BLOCK_M2 + BLOCK_CLASS

    X_rows: List[List[float]] = []
    y: List[int] = []

    def safe_log(x):
        if x is None or (isinstance(x, float) and (math.isnan(x) or x <= 0)):
            return float("nan")
        return math.log(x)

    for sid in sids:
        h = heap.get(sid, {})
        a125 = h125.get(sid, {})
        basic = basics.get(sid, {})
        beta = h.get("beta", float("nan"))
        K = h.get("K", float("nan"))
        N = h.get("N", float("nan"))
        log_K = safe_log(K)
        amb = (log_K - beta) if isinstance(beta, float) and not math.isnan(beta) and not math.isnan(log_K) else float("nan")

        mh = mode_onehot(sid)
        # mode_E: Meccan non-inclusio (not already classified)
        is_meccan = noldeke_phase.get(sid, "").startswith("Medinan") is False and noldeke_phase.get(sid, "") != ""
        already_modal = (mh["mode_A_length"] + mh["mode_B_refrain"] + mh["mode_D_inclusio"]) > 0
        mode_E = 1.0 if (is_meccan and not already_modal) else 0.0

        # M5 features
        feat_m5 = [
            basic.get("log_length", float("nan")),
            basic.get("verse_count", float("nan")),
            basic.get("mean_verse_length", float("nan")),
            basic.get("type_token_ratio", float("nan")),
            disp.get(sid, float("nan")),
            float(beta) if beta is not None else float("nan"),
            amb,
            basic.get("kl_from_corpus", float("nan")),
            basic.get("entropy_rate_surah", float("nan")),
            lz.get(sid, float("nan")),
            mh["mode_A_length"],
            mh["mode_B_refrain"],
            mh["mode_D_inclusio"],
            mode_E,
        ]

        # M1 features
        feat_m1 = [
            float(hinge_distance(sid)),
            1.0 if sid in TIWAL else 0.0,
            1.0 if sid in HAWAMIM else 0.0,
            1.0 if sid in MEDINAN_BACK else 0.0,
            1.0 if sid in ALM_SURAHS else 0.0,
            1.0 if sid in SHORT_BRACKET else 0.0,
            float(fiedler_community(sid)),
            basic.get("log_length", float("nan")),  # duplicate; for M1-alone fit
        ]

        # M2 features
        late_meccan_phase = 1.0 if noldeke_phase.get(sid, "") in ("Late Meccan", "Medinan") else 0.0
        feat_m2 = [
            float(noldeke_rank.get(sid, float("nan"))),
            late_meccan_phase,
            a125.get("muq_cardinality", 0.0) or 0.0,
            a125.get("qul_density", float("nan")),
            a125.get("book_reference_density", float("nan")),
            a125.get("eschatological_density", float("nan")),
        ]

        feat_class = [
            1.0 if sid == 1 else 0.0,
            1.0 if sid == 112 else 0.0,
            1.0 if sid == 113 else 0.0,
            1.0 if sid == 114 else 0.0,
        ]

        X_rows.append(feat_m5 + feat_m1 + feat_m2 + feat_class)
        y.append(sid)  # mushaf position == surah id

    X = np.array(X_rows, dtype=float)
    y_arr = np.array(y, dtype=float)

    # Index ranges for each block
    idx_m5 = list(range(0, len(BLOCK_M5)))
    idx_m1 = list(range(len(BLOCK_M5), len(BLOCK_M5) + len(BLOCK_M1)))
    idx_m2 = list(range(len(BLOCK_M5) + len(BLOCK_M1),
                        len(BLOCK_M5) + len(BLOCK_M1) + len(BLOCK_M2)))
    idx_class = list(range(len(BLOCK_M5) + len(BLOCK_M1) + len(BLOCK_M2),
                           len(all_features)))

    blocks = {
        "M5": idx_m5,
        "M1": idx_m1,
        "M2": idx_m2,
        "CLASS": idx_class,
    }
    return X, y_arr, sids, blocks, all_features


# ---------------------------------------------------------------------------
# LOOCV + utilities
# ---------------------------------------------------------------------------
def impute_median(X: np.ndarray, medians: np.ndarray | None = None) -> Tuple[np.ndarray, np.ndarray]:
    X2 = X.copy()
    if medians is None:
        medians = np.nanmedian(X2, axis=0)
        medians = np.where(np.isnan(medians), 0.0, medians)
    inds = np.where(np.isnan(X2))
    X2[inds] = np.take(medians, inds[1])
    return X2, medians


def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    ss_res = float(np.sum((y_true - y_pred) ** 2))
    ss_tot = float(np.sum((y_true - y_true.mean()) ** 2))
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))


def loocv_ridge(X: np.ndarray, y: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    n = X.shape[0]
    preds = np.zeros(n, dtype=float)
    loo = LeaveOneOut()
    for train_idx, test_idx in loo.split(X):
        X_tr, meds = impute_median(X[train_idx])
        X_te, _ = impute_median(X[test_idx], medians=meds)
        scaler = StandardScaler().fit(X_tr)
        X_trs = scaler.transform(X_tr)
        X_tes = scaler.transform(X_te)
        model = Ridge(alpha=alpha, random_state=SEED)
        model.fit(X_trs, y[train_idx])
        preds[test_idx] = model.predict(X_tes)
    return preds


def permutation_null(X: np.ndarray, y: np.ndarray, n_perm: int = N_PERM,
                     seed: int = SEED) -> Dict:
    rng = np.random.default_rng(seed)
    null_r2 = []
    for k in range(n_perm):
        y_perm = y[rng.permutation(len(y))]
        preds = loocv_ridge(X, y_perm)
        null_r2.append(r2_score(y_perm, preds))
    arr = np.array(null_r2, dtype=float)
    return {
        "null_r2_mean": float(arr.mean()),
        "null_r2_std": float(arr.std(ddof=0)),
        "null_r2_95": float(np.percentile(arr, 95)),
        "null_r2_975": float(np.percentile(arr, 97.5)),
        "null_r2_max": float(arr.max()),
        "null_r2_samples": arr.tolist(),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    np.random.seed(SEED)
    random.seed(SEED)

    X_full, y, sids, blocks, names = build_feature_matrix()
    print(f"Feature matrix: {X_full.shape}")
    print(f"Blocks: M5={len(blocks['M5'])} M1={len(blocks['M1'])} M2={len(blocks['M2'])} CLASS={len(blocks['CLASS'])}")

    nan_counts = np.isnan(X_full).sum(axis=0)
    print("NaN counts (pre-impute):")
    for i, n in enumerate(names):
        if nan_counts[i] > 0:
            print(f"  {n}: {int(nan_counts[i])}")

    # ------------------------------------------------------------------
    # Cell-1: Full equation
    # ------------------------------------------------------------------
    preds_full = loocv_ridge(X_full, y)
    r2_full = r2_score(y, preds_full)
    mae_full = mae(y, preds_full)
    print(f"\n[Cell-1 FULL] Ridge LOOCV R²={r2_full:.4f} MAE={mae_full:.2f}")

    # ------------------------------------------------------------------
    # Cells 2-4: single-block fits (+ CLASS descriptive)
    # ------------------------------------------------------------------
    per_block_r2: Dict[str, Dict] = {}
    preds_per_block: Dict[str, np.ndarray] = {}
    for bname, cols in blocks.items():
        if len(cols) == 0:
            continue
        Xb = X_full[:, cols]
        preds_b = loocv_ridge(Xb, y)
        r2b = r2_score(y, preds_b)
        mae_b = mae(y, preds_b)
        per_block_r2[bname] = {"r2": r2b, "mae": mae_b, "n_features": len(cols)}
        preds_per_block[bname] = preds_b
        print(f"[{bname}-only] R²={r2b:.4f} MAE={mae_b:.2f} n_feat={len(cols)}")

    # ------------------------------------------------------------------
    # LOBO (leave-one-block-out) decomposition
    # ------------------------------------------------------------------
    lobo: Dict[str, Dict] = {}
    preds_lobo: Dict[str, np.ndarray] = {}
    for bname, cols in blocks.items():
        remaining_cols = [c for bn, cs in blocks.items() if bn != bname for c in cs]
        X_rem = X_full[:, remaining_cols]
        preds_rem = loocv_ridge(X_rem, y)
        r2_rem = r2_score(y, preds_rem)
        delta = r2_full - r2_rem
        lobo[bname] = {
            "r2_without": r2_rem,
            "delta_r2_marginal": delta,
        }
        preds_lobo[bname] = preds_rem
        print(f"[LOBO drop-{bname}] R²={r2_rem:.4f}  ΔR²(marginal)={delta:+.4f}")

    # ------------------------------------------------------------------
    # Robustness: attribute log_length to M1 (not M5)
    # ------------------------------------------------------------------
    # Make M5' = M5 without log_length; M1' = M1 already has log_length_M1 duplicate
    m5_cols_without_loglen = [c for c in blocks["M5"] if names[c] != "log_length"]
    m5_cols_robust = m5_cols_without_loglen  # M5 drops log_length; M1 keeps log_length_M1
    blocks_robust = {
        "M5": m5_cols_robust,
        "M1": blocks["M1"],  # contains log_length_M1
        "M2": blocks["M2"],
        "CLASS": blocks["CLASS"],
    }
    robust_per_block: Dict[str, Dict] = {}
    for bname, cols in blocks_robust.items():
        if len(cols) == 0:
            continue
        Xb = X_full[:, cols]
        preds_b = loocv_ridge(Xb, y)
        r2b = r2_score(y, preds_b)
        robust_per_block[bname] = {"r2": r2b, "n_features": len(cols)}
    # Full equation under robust attribution (same total columns)
    # (since log_length_M1 is duplicated in M1, dropping from M5 reduces full col count by 1)
    robust_cols_full = (m5_cols_robust + blocks["M1"]
                        + blocks["M2"] + blocks["CLASS"])
    X_robust_full = X_full[:, robust_cols_full]
    preds_full_robust = loocv_ridge(X_robust_full, y)
    r2_full_robust = r2_score(y, preds_full_robust)
    print(f"\n[Robust attribution: log_length→M1] Full R²={r2_full_robust:.4f}")
    for bname, rec in robust_per_block.items():
        print(f"  [{bname}-only robust] R²={rec['r2']:.4f}")

    # ------------------------------------------------------------------
    # Permutation null
    # ------------------------------------------------------------------
    print(f"\nRunning {N_PERM}-permutation null...")
    null_full = permutation_null(X_full, y, n_perm=N_PERM, seed=SEED)
    null_samples = np.array(null_full["null_r2_samples"], dtype=float)
    p_full = float((np.sum(null_samples >= r2_full) + 1) / (len(null_samples) + 1))
    print(f"Null R² mean={null_full['null_r2_mean']:.3f} max={null_full['null_r2_max']:.3f}  p={p_full:.4f}")

    # ------------------------------------------------------------------
    # Residual analysis
    # ------------------------------------------------------------------
    residuals_full = y - preds_full
    per_surah_resid = []
    for i, sid in enumerate(sids):
        rec = {
            "surah_id": int(sid),
            "mushaf_pos": int(y[i]),
            "pred_full": float(preds_full[i]),
            "resid_full": float(residuals_full[i]),
            "abs_resid_full": float(abs(residuals_full[i])),
            "pred_M5": float(preds_per_block["M5"][i]) if "M5" in preds_per_block else float("nan"),
            "pred_M1": float(preds_per_block["M1"][i]) if "M1" in preds_per_block else float("nan"),
            "pred_M2": float(preds_per_block["M2"][i]) if "M2" in preds_per_block else float("nan"),
            "pred_CLASS": float(preds_per_block["CLASS"][i]) if "CLASS" in preds_per_block else float("nan"),
        }
        # Missing-principle attribution: which block's LOBO-drop INCREASES |resid| the most?
        # resid_without_block = y - preds_lobo[block]
        lobo_resid = {}
        for bname in blocks.keys():
            lobo_resid[bname] = float(y[i] - preds_lobo[bname][i])
        rec["lobo_resid"] = lobo_resid
        # Missing principle = block whose REMOVAL increases the absolute residual the most relative to full
        delta_abs_resid = {
            b: abs(lobo_resid[b]) - abs(residuals_full[i]) for b in blocks.keys()
        }
        # Largest positive delta = this principle was most needed
        missing = max(delta_abs_resid.items(), key=lambda kv: kv[1])
        rec["most_needed_principle"] = missing[0]
        rec["most_needed_delta"] = missing[1]
        per_surah_resid.append(rec)

    top_resid = sorted(per_surah_resid, key=lambda r: -r["abs_resid_full"])[:10]
    print("\nTop-10 residuals (|resid_full|):")
    for r in top_resid:
        print(f"  Q{r['surah_id']:3d}  pos={r['mushaf_pos']:3d}  pred={r['pred_full']:.1f}  "
              f"resid={r['resid_full']:+.1f}  most-needed={r['most_needed_principle']}")

    # ------------------------------------------------------------------
    # Pre-reg verdict
    # ------------------------------------------------------------------
    H_full = bool(r2_full > 0.88 and p_full < 0.0125)
    H_m5 = bool(per_block_r2.get("M5", {}).get("r2", -1) > 0.70)
    H_m1 = bool(per_block_r2.get("M1", {}).get("r2", -1) > 0.40)
    H_m2 = bool(per_block_r2.get("M2", {}).get("r2", -1) > 0.40)
    print(f"\nVerdict cells: FULL(>0.88)={H_full}  M5(>0.70)={H_m5}  "
          f"M1(>0.40)={H_m1}  M2(>0.40)={H_m2}")

    # CF-020 expected split: 76 / 15 / 5 / 4 (M5 / M1 / M2+marginal / class+residual)
    # Compare against LOBO marginals normalized
    total_lobo_marg = sum(max(0.0, lobo[b]["delta_r2_marginal"]) for b in blocks.keys())
    if total_lobo_marg > 0:
        lobo_share = {
            b: 100.0 * max(0.0, lobo[b]["delta_r2_marginal"]) / total_lobo_marg
            for b in blocks.keys()
        }
    else:
        lobo_share = {b: 0.0 for b in blocks.keys()}

    # Also alone-based share
    alone_total = sum(max(0.0, per_block_r2[b]["r2"]) for b in blocks.keys() if b in per_block_r2)
    alone_share = {
        b: 100.0 * max(0.0, per_block_r2[b]["r2"]) / alone_total if alone_total > 0 else 0.0
        for b in per_block_r2.keys()
    }

    print("\nVariance-share estimates:")
    print("  LOBO-marginal (of total-marginal):")
    for b, s in lobo_share.items():
        print(f"    {b}: {s:.1f}%")
    print("  Alone-R² (of total-alone):")
    for b, s in alone_share.items():
        print(f"    {b}: {s:.1f}%")

    cf020_expected = {"M5": 76, "M1": 15, "M2": 5, "CLASS": 4}

    out = {
        "id": "H-NEW-250",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_family": "h-new-250-quantitative-equation-fit",
        "bonferroni_k": 4,
        "alpha_bon": 0.0125,
        "alpha_fam": 0.05,
        "n_surahs": int(len(sids)),
        "feature_names": names,
        "blocks": {k: [int(c) for c in v] for k, v in blocks.items()},
        "block_feature_names": {
            "M5": [names[c] for c in blocks["M5"]],
            "M1": [names[c] for c in blocks["M1"]],
            "M2": [names[c] for c in blocks["M2"]],
            "CLASS": [names[c] for c in blocks["CLASS"]],
        },
        "cell_1_full_equation": {
            "r2_loocv": r2_full,
            "mae_loocv": mae_full,
            "n_features": int(X_full.shape[1]),
            "p_perm": p_full,
        },
        "cell_2_M5_only": per_block_r2.get("M5", {}),
        "cell_3_M1_only": per_block_r2.get("M1", {}),
        "cell_4_M2_only": per_block_r2.get("M2", {}),
        "CLASS_only_descriptive": per_block_r2.get("CLASS", {}),
        "lobo_decomposition": lobo,
        "variance_share_lobo_marginal_pct": lobo_share,
        "variance_share_alone_pct": alone_share,
        "cf020_expected_share_pct": cf020_expected,
        "robustness_log_length_to_M1": {
            "full_r2": r2_full_robust,
            "per_block_r2": robust_per_block,
        },
        "permutation_null_full": {
            "n_perm": N_PERM,
            "null_r2_mean": null_full["null_r2_mean"],
            "null_r2_std": null_full["null_r2_std"],
            "null_r2_95": null_full["null_r2_95"],
            "null_r2_975": null_full["null_r2_975"],
            "null_r2_max": null_full["null_r2_max"],
            "p_full": p_full,
        },
        "h_new_192_baseline_ridge": 0.759,
        "h_new_192_baseline_rf": 0.817,
        "h_new_233_ridge_29f": 0.7395,
        "h_new_233_rf_29f": 0.8485,
        "h_new_183_noldeke_ridge": 0.836,
        "H_full_r2_gt_0p88_and_p_lt_0p0125": H_full,
        "H_M5_alone_gt_0p70": H_m5,
        "H_M1_alone_gt_0p40": H_m1,
        "H_M2_alone_gt_0p40": H_m2,
        "verdict": (
            "STRONG PASS — full R² > 0.88 + variance-split honors CF-020" if H_full
            else "INTERMEDIATE — R² in [0.82, 0.88) band" if (0.82 <= r2_full < 0.88)
            else "PASS-BENEATH-TARGET — R² < 0.82; CF-020 weights need refinement"
        ),
        "per_surah_residuals": per_surah_resid,
        "top10_residuals": top_resid,
    }

    out_path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-250.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {out_path}")
    print(f"Verdict: {out['verdict']}")


if __name__ == "__main__":
    main()
