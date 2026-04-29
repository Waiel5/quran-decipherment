#!/usr/bin/env python3
"""H-NEW-233 — Ensemble mushaf-position predictor with 29-feature expanded set.

Pre-reg: findings/phase-b-hypotheses/h-new-233-ensemble-mushaf-predictor-prereg.md

Pipeline
--------
  1. Load base 15 features from H-NEW-123 (β/K), H-NEW-125 (axis-values),
     H-NEW-168 (dispersion), and raw corpus for verse_count/TTR/refrain_score.
  2. Load expansion features:
       - phonological means (H-NEW-182) from h-new-182-surah-vectors.csv
       - KL-divergence (H-NEW-231 computed here inline)
       - per-surah Hurst (DFA on word-counts-per-verse, computed inline)
       - LZ76-norm (H-NEW-187) from h-new-187-per-surah.csv
       - entropy rate (unigram Shannon per surah, inline)
       - (α, β) residual: α regressed on β + log_length (inline)
  3. Target y = mushaf position (1..114).
  4. Ridge full LOOCV, RF full LOOCV.
  5. 100-perm null for Ridge (seed 20260419).
  6. Emit JSON.

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
from sklearn.ensemble import RandomForestRegressor
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


def surah_verse_word_counts(s: Dict) -> List[int]:
    return [len(v["text"].split()) for v in s["verses"]]


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


def load_phonological() -> Dict[int, Dict[str, float]]:
    path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-182-surah-vectors.csv"
    out: Dict[int, Dict[str, float]] = {}
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["surah_id"])
            out[sid] = {
                "phon_labial": float(row["labial"]),
                "phon_alveolar": float(row["alveolar"]),
                "phon_palatal": float(row["palatal"]),
                "phon_velar": float(row["velar"]),
                "phon_pharyngeal": float(row["pharyngeal"]),
                "phon_glottal": float(row["glottal"]),
                "phon_emphatic": float(row["emphatic"]),
                "phon_voiced": float(row["voiced"]),
                "phon_continuant": float(row["continuant"]),
            }
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


# ---------------------------------------------------------------------------
# Inline-computed features
# ---------------------------------------------------------------------------
def compute_verse_count_ttr_refrain(corpus: List[Dict]) -> Dict[int, Dict[str, float]]:
    """verse_count, type-token ratio, refrain_score (max run of identical verse texts / verse_count)."""
    out: Dict[int, Dict[str, float]] = {}
    for s in corpus:
        sid = s["id"]
        toks = surah_tokens(s)
        n = len(toks)
        vc = s["total_verses"]
        v_texts = [v["text"].strip() for v in s["verses"]]
        # TTR
        if n > 0:
            ttr = len(set(toks)) / n
        else:
            ttr = float("nan")
        # refrain score: fraction of verses that are duplicates (any duplicate verse text)
        from collections import Counter
        c = Counter(v_texts)
        dup = sum(cnt for cnt in c.values() if cnt > 1)
        refrain_score = dup / vc if vc > 0 else 0.0
        out[sid] = {
            "verse_count": vc,
            "type_token_ratio": ttr,
            "refrain_score": refrain_score,
        }
    return out


def compute_kl_from_corpus(corpus: List[Dict], alpha: float = 0.5) -> Dict[int, float]:
    """KL(p_surah || p_corpus), Dirichlet-smoothed, over corpus vocabulary."""
    from collections import Counter
    all_toks: List[str] = []
    per_surah_toks: Dict[int, List[str]] = {}
    for s in corpus:
        toks = surah_tokens(s)
        per_surah_toks[s["id"]] = toks
        all_toks.extend(toks)
    corpus_counter = Counter(all_toks)
    vocab = list(corpus_counter.keys())
    V = len(vocab)
    vocab_idx = {w: i for i, w in enumerate(vocab)}
    total_N = sum(corpus_counter.values())
    p_corpus = np.array(
        [(corpus_counter[w] + alpha) / (total_N + alpha * V) for w in vocab],
        dtype=float,
    )
    out: Dict[int, float] = {}
    for sid, toks in per_surah_toks.items():
        cnt = Counter(toks)
        N_s = sum(cnt.values())
        p_s = np.array(
            [(cnt.get(w, 0) + alpha) / (N_s + alpha * V) for w in vocab],
            dtype=float,
        )
        kl = float(np.sum(p_s * np.log(p_s / p_corpus)))
        out[sid] = kl
    return out


def compute_entropy_rate(corpus: List[Dict]) -> Dict[int, float]:
    """Unigram Shannon entropy per surah, bits."""
    from collections import Counter
    out: Dict[int, float] = {}
    for s in corpus:
        toks = surah_tokens(s)
        n = len(toks)
        if n == 0:
            out[s["id"]] = float("nan")
            continue
        cnt = Counter(toks)
        probs = np.array([c / n for c in cnt.values()], dtype=float)
        h = float(-np.sum(probs * np.log2(probs)))
        out[s["id"]] = h
    return out


def dfa_hurst(x: np.ndarray, min_scale: int = 8) -> float:
    """DFA α (Hurst) on 1D series. NaN if insufficient length."""
    n = len(x)
    if n < 2 * min_scale:
        return float("nan")
    # integrate mean-centered
    y = np.cumsum(x - x.mean())
    # scales: powers-of-2 up to n//4, min_scale
    scales: List[int] = []
    s = min_scale
    while s <= n // 4 and s < n:
        scales.append(s)
        s *= 2
    if len(scales) < 3:
        # fall back to linear scales
        scales = [min_scale, max(min_scale + 4, n // 8), max(min_scale + 8, n // 4)]
        scales = [s for s in scales if s <= n // 2]
    if len(scales) < 3:
        return float("nan")
    Fns: List[float] = []
    for s in scales:
        # split y into non-overlapping windows of length s
        n_windows = n // s
        if n_windows < 2:
            Fns.append(float("nan"))
            continue
        rms_list: List[float] = []
        for k in range(n_windows):
            seg = y[k * s:(k + 1) * s]
            xs = np.arange(s, dtype=float)
            # linear detrend
            coef = np.polyfit(xs, seg, 1)
            trend = np.polyval(coef, xs)
            rms = float(np.sqrt(np.mean((seg - trend) ** 2)))
            rms_list.append(rms)
        Fns.append(float(np.mean(rms_list)))
    valid = [(s, f) for s, f in zip(scales, Fns) if not math.isnan(f) and f > 0]
    if len(valid) < 3:
        return float("nan")
    log_s = np.log([v[0] for v in valid])
    log_f = np.log([v[1] for v in valid])
    slope, _ = np.polyfit(log_s, log_f, 1)
    return float(slope)


def compute_hurst_per_surah(corpus: List[Dict]) -> Dict[int, float]:
    out: Dict[int, float] = {}
    for s in corpus:
        wc = np.array(surah_verse_word_counts(s), dtype=float)
        out[s["id"]] = dfa_hurst(wc, min_scale=8)
    return out


def compute_alpha_beta_residual(heap: Dict[int, Dict]) -> Dict[int, float]:
    """Residual of α (log K) regressed on β and log(N)."""
    sids = sorted(heap.keys())
    alphas, betas, logN = [], [], []
    for sid in sids:
        h = heap[sid]
        K = h.get("K")
        beta = h.get("beta")
        N = h.get("N")
        if K is None or beta is None or N is None or K <= 0 or N <= 0:
            alphas.append(np.nan); betas.append(np.nan); logN.append(np.nan)
        else:
            alphas.append(math.log(K))
            betas.append(float(beta))
            logN.append(math.log(N))
    arr = np.array([alphas, betas, logN], dtype=float).T
    # complete-case regression
    mask = ~np.isnan(arr).any(axis=1)
    X_fit = arr[mask][:, [1, 2]]
    y_fit = arr[mask][:, 0]
    lr = LinearRegression().fit(X_fit, y_fit)
    # predict for all available
    residuals: Dict[int, float] = {}
    for i, sid in enumerate(sids):
        beta = arr[i, 1]
        log_N = arr[i, 2]
        a = arr[i, 0]
        if np.isnan(a) or np.isnan(beta) or np.isnan(log_N):
            residuals[sid] = float("nan")
        else:
            pred = lr.predict([[beta, log_N]])[0]
            residuals[sid] = float(a - pred)
    return residuals


# ---------------------------------------------------------------------------
# Feature matrix
# ---------------------------------------------------------------------------
BASE_FEATURES = [
    "alpha", "beta", "alpha_minus_beta", "log_length", "mean_verse_len",
    "allah_density", "qul_density", "book_ref_density", "loanword_density",
    "eschat_density", "dispersion", "muq_cardinality",
    "verse_count", "type_token_ratio", "refrain_score",
]

EXPANSION_FEATURES = [
    "phon_labial", "phon_alveolar", "phon_palatal", "phon_velar",
    "phon_pharyngeal", "phon_glottal", "phon_emphatic", "phon_voiced",
    "phon_continuant",
    "kl_from_corpus", "hurst_verse_len", "lz_norm_simple",
    "entropy_rate_surah", "alpha_beta_residual",
]

FEATURE_NAMES = BASE_FEATURES + EXPANSION_FEATURES


def build_feature_matrix() -> Tuple[np.ndarray, np.ndarray, List[int], List[str]]:
    corpus = load_corpus()
    heap = load_heap()
    h125 = load_h125()
    disp = load_dispersion()
    phon = load_phonological()
    lz = load_lz()
    vctt = compute_verse_count_ttr_refrain(corpus)
    kl = compute_kl_from_corpus(corpus)
    hurst = compute_hurst_per_surah(corpus)
    entropy = compute_entropy_rate(corpus)
    alpha_beta_res = compute_alpha_beta_residual(heap)

    sids = sorted([s["id"] for s in corpus])
    X_rows: List[List[float]] = []
    y: List[int] = []

    def safe_log(x):
        if x is None or (isinstance(x, float) and (math.isnan(x) or x <= 0)):
            return float("nan")
        return math.log(x)

    for sid in sids:
        h = heap.get(sid, {})
        a = h125.get(sid, {})
        beta = h.get("beta", float("nan"))
        K = h.get("K", float("nan"))
        N = h.get("N", float("nan"))
        log_K = safe_log(K)
        log_N = safe_log(N)
        beta_v = beta if beta is not None else float("nan")
        alpha_proxy = log_K
        if isinstance(beta_v, float) and math.isnan(beta_v) or (isinstance(alpha_proxy, float) and math.isnan(alpha_proxy)):
            amb = float("nan")
        else:
            amb = alpha_proxy - beta_v

        row_base = [
            alpha_proxy,
            beta_v if beta_v is not None else float("nan"),
            amb,
            log_N,
            a.get("mean_verse_length", float("nan")),
            a.get("allah_density", float("nan")),
            a.get("qul_density", float("nan")),
            a.get("book_reference_density", float("nan")),
            a.get("loanword_density", float("nan")),
            a.get("eschatological_density", float("nan")),
            disp.get(sid, float("nan")),
            a.get("muq_cardinality", float("nan")),
            vctt.get(sid, {}).get("verse_count", float("nan")),
            vctt.get(sid, {}).get("type_token_ratio", float("nan")),
            vctt.get(sid, {}).get("refrain_score", float("nan")),
        ]

        p = phon.get(sid, {})
        row_exp = [
            p.get("phon_labial", float("nan")),
            p.get("phon_alveolar", float("nan")),
            p.get("phon_palatal", float("nan")),
            p.get("phon_velar", float("nan")),
            p.get("phon_pharyngeal", float("nan")),
            p.get("phon_glottal", float("nan")),
            p.get("phon_emphatic", float("nan")),
            p.get("phon_voiced", float("nan")),
            p.get("phon_continuant", float("nan")),
            kl.get(sid, float("nan")),
            hurst.get(sid, float("nan")),
            lz.get(sid, float("nan")),
            entropy.get(sid, float("nan")),
            alpha_beta_res.get(sid, float("nan")),
        ]

        X_rows.append(row_base + row_exp)
        y.append(sid)  # mushaf position == surah id

    X = np.array(X_rows, dtype=float)
    y_arr = np.array(y, dtype=float)
    return X, y_arr, sids, FEATURE_NAMES


# ---------------------------------------------------------------------------
# LOOCV
# ---------------------------------------------------------------------------
def impute_median(X: np.ndarray, medians: np.ndarray | None = None) -> Tuple[np.ndarray, np.ndarray]:
    X2 = X.copy()
    if medians is None:
        medians = np.nanmedian(X2, axis=0)
        # guard: if a column is entirely NaN, use 0
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


def loocv_rf(X: np.ndarray, y: np.ndarray, n_estimators: int = 500) -> np.ndarray:
    n = X.shape[0]
    preds = np.zeros(n, dtype=float)
    loo = LeaveOneOut()
    for train_idx, test_idx in loo.split(X):
        X_tr, meds = impute_median(X[train_idx])
        X_te, _ = impute_median(X[test_idx], medians=meds)
        model = RandomForestRegressor(
            n_estimators=n_estimators, max_depth=None, random_state=SEED, n_jobs=1,
        )
        model.fit(X_tr, y[train_idx])
        preds[test_idx] = model.predict(X_te)
    return preds


def permutation_null(X: np.ndarray, y: np.ndarray, n_perm: int = N_PERM,
                     seed: int = SEED, model: str = "ridge") -> Dict:
    rng = np.random.default_rng(seed)
    null_r2 = []
    for k in range(n_perm):
        y_perm = y[rng.permutation(len(y))]
        if model == "ridge":
            preds = loocv_ridge(X, y_perm)
        else:
            preds = loocv_rf(X, y_perm)
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

    X_full, y, sids, names = build_feature_matrix()
    print(f"Feature matrix: {X_full.shape}")
    print(f"NaN counts per feature (pre-impute):")
    for i, n in enumerate(names):
        nanc = int(np.isnan(X_full[:, i]).sum())
        if nanc > 0:
            print(f"  {n}: {nanc}")

    # Model A: Ridge LOOCV
    preds_A = loocv_ridge(X_full, y)
    r2_A = r2_score(y, preds_A); mae_A = mae(y, preds_A)
    print(f"Ridge LOOCV: R²={r2_A:.4f} MAE={mae_A:.2f}")

    # Model B: RF LOOCV
    preds_B = loocv_rf(X_full, y)
    r2_B = r2_score(y, preds_B); mae_B = mae(y, preds_B)
    print(f"RF LOOCV:    R²={r2_B:.4f} MAE={mae_B:.2f}")

    # Feature importances (single-fit RF on full data w/ median imputation)
    X_imp, _ = impute_median(X_full)
    rf_full = RandomForestRegressor(n_estimators=500, random_state=SEED, n_jobs=1)
    rf_full.fit(X_imp, y)
    rf_imp = rf_full.feature_importances_.tolist()

    # Ridge coefficients on scaled
    scaler = StandardScaler().fit(X_imp)
    X_imp_s = scaler.transform(X_imp)
    ridge_full = Ridge(alpha=1.0, random_state=SEED).fit(X_imp_s, y)
    ridge_coefs = ridge_full.coef_.tolist()

    # Permutation null Ridge
    null_ridge = permutation_null(X_full, y, n_perm=N_PERM, seed=SEED, model="ridge")
    null_samples_r = np.array(null_ridge["null_r2_samples"], dtype=float)
    p_ridge = float((np.sum(null_samples_r >= r2_A) + 1) / (len(null_samples_r) + 1))

    # Per-surah preds + residuals
    per_surah = [
        {
            "surah_id": int(sids[i]),
            "mushaf_pos": int(y[i]),
            "pred_ridge": float(preds_A[i]),
            "pred_rf": float(preds_B[i]),
            "resid_ridge": float(y[i] - preds_A[i]),
            "resid_rf": float(y[i] - preds_B[i]),
        }
        for i in range(len(sids))
    ]

    # Pre-reg tests
    H1 = bool(r2_A > 0.759 and p_ridge < 0.025)
    H2 = bool(r2_B > 0.817)

    feature_importance = sorted(
        zip(names, rf_imp), key=lambda x: -x[1]
    )

    out = {
        "id": "H-NEW-233",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_family": "h-new-233-ensemble-mushaf-predictor",
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "alpha_fam": 0.05,
        "n_surahs": int(len(sids)),
        "feature_names": names,
        "n_features": len(names),
        "model_A_ridge": {
            "r2_loocv": r2_A,
            "mae_loocv": mae_A,
            "ridge_alpha": 1.0,
        },
        "model_B_rf": {
            "r2_loocv": r2_B,
            "mae_loocv": mae_B,
            "n_estimators": 500,
        },
        "rf_feature_importance_sorted": feature_importance,
        "ridge_fit_coefs_on_scaled": dict(zip(names, ridge_coefs)),
        "permutation_null_ridge": {
            "n_perm": N_PERM,
            "null_r2_mean": null_ridge["null_r2_mean"],
            "null_r2_std": null_ridge["null_r2_std"],
            "null_r2_95": null_ridge["null_r2_95"],
            "null_r2_975": null_ridge["null_r2_975"],
            "null_r2_max": null_ridge["null_r2_max"],
            "p_one_sided_ridge": p_ridge,
        },
        "h_new_192_baseline_ridge": 0.759,
        "h_new_192_baseline_rf": 0.817,
        "h_new_183_noldeke_ceiling_ridge": 0.836,
        "H1_ridge_beats_baseline_and_p_lt_0p025": H1,
        "H2_rf_beats_baseline": H2,
        "verdict": (
            "STRONG PASS — R² > 0.90" if r2_B > 0.90 or r2_A > 0.90
            else "PASS — beats H-NEW-192 baseline" if (H1 or H2)
            else "NULL — no improvement over H-NEW-192"
        ),
        "per_surah_predictions": per_surah,
    }

    out_path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-233.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {out_path}")
    print(f"Verdict: {out['verdict']}")
    print(f"H1={H1}  H2={H2}")
    print(f"Top-10 RF importances:")
    for n, imp in feature_importance[:10]:
        print(f"  {n}: {imp:.4f}")
    # Top residuals (|resid| RF)
    top_resid = sorted(per_surah, key=lambda r: -abs(r["resid_rf"]))[:10]
    print("Top-10 RF residuals (|resid|):")
    for r in top_resid:
        print(f"  Q{r['surah_id']:3d}  actual={r['mushaf_pos']:3d}  pred={r['pred_rf']:.1f}  resid={r['resid_rf']:+.1f}")


if __name__ == "__main__":
    main()
