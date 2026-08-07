#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2790 — One harness, five flagged claims, one size-matched null.

`findings/UNIT-DRIFT-DEFECT.md` establishes that when a density is divided by a unit count
whose size drifts across the ordering under test, the measure is testing the drift. Five
claims hit all three of its screens. This runner puts each through the same three arms:

  A0  reproduce the published headline (fail-fast label, does NOT stop the run)
  A1  the size-only baseline — same model, same LOOCV, size columns only, no vocabulary
  A2  the size-matched null — permute the TARGET within quintiles of the drift channel
  A3  per-word re-normalisation of the density features
  A4  replication at the second seed

Claims (prereg §0, load-bearing order):
  C1  H-NEW-192  mushaf position, 15 compositional features   Ridge .759 / RF .817
  C2  H-NEW-183  Noldeke rank,   12 compositional features    Ridge .836 (baseline .446)
  C3  H-NEW-233  mushaf position, 29 features                 RF .8485 / Ridge .7395
  C4  H-NEW-74   qul density per 100 verses x Noldeke phase   KW H = 35.36, p = 1.02e-7
  C5  H-NEW-231  per-surah KL divergence                      CALIBRATION ARM ONLY

The 183 and 233 feature matrices and LOOCV routines are LIFTED from their frozen published
scripts as SHA-verified modules. Nothing is re-implemented.

Pre-reg : findings/phase-b-hypotheses/prereg-h-new-2790-flagged-batch.md
          SHA-256 embedded below, verified at runtime; mismatch -> SystemExit.
Seeds   : 20260509 primary / 20260519 replication. Published seed 20260419 inside A0 only.
Author  : Waiel Al-Shujaa.  Bismillahi al-Rahmani al-Rahim.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import platform
import random
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # findings/phase-b-hypotheses
REPO = os.path.dirname(os.path.dirname(ROOT))     # repo root

PREREG_REL = "findings/phase-b-hypotheses/prereg-h-new-2790-flagged-batch.md"
PREREG_SHA256 = "6bb7e77a100810e31743734cd105407d6d21cf6d477dee1a9096c5ebde6014a8"

SRC183_REL = "scripts/h_new_183_chronology_predictor.py"
SRC233_REL = "scripts/h_new_233_ensemble_predictor.py"

FROZEN = {
    "quran-text/quran-no-tashkeel.json":
        "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a",
    "data/revelation-order.csv":
        "74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7",
    "data/morphology/quranic-corpus-morphology-0.4.txt":
        "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46",
    "findings/phase-b-hypotheses/csv/h-new-123.json":
        "33bbeec06c1187b1a96448ecf87720a4915a49a827cf110685d4d277aa449f46",
    "findings/phase-b-hypotheses/csv/h-new-125.json":
        "8b2f7f1cf217562dd34be75519c80d29ceaebcc40b2b0c6fbe95bebb5d0442e1",
    "findings/phase-b-hypotheses/csv/h-new-168-per-surah-dispersion.csv":
        "7778d07f620d68b3a3fefbf5903c0e9e30665e25b58fe1f766d7f08cf6a07594",
    "findings/phase-b-hypotheses/csv/h-new-182-surah-vectors.csv":
        "30571ef0ee37f32881033ca22fcb368cffbaaf986d040491ed4396b2cb2b8acc",
    "findings/phase-b-hypotheses/csv/h-new-187-per-surah.csv":
        "7eee6ba49222e3fcd989ca2521114503fd5dcb3f907de6f1d343950970ed32ec",
    "findings/phase-b-hypotheses/csv/h-new-183.json":
        "246af4b198c2c7d5d4e2edf86d5d1924c37a35f5d4e6a5292b0e12291787a16f",
    "findings/phase-b-hypotheses/csv/h-new-233.json":
        "28715441baab9bef58735acb8fa7b63bd58686844fed25ee0f162ccfe67236a0",
    SRC183_REL: "a30666c03c8bbdc0fa618099497ebe6962306cf7c712d5abf1b7adbbd025db2b",
    SRC233_REL: "ad69720a10159c43094336fab9890671743b545fbcfef5c53db1bbcb3478edd7",
}

SEED, SEED_REPL = 20260509, 20260519
SEED_PUBLISHED = 20260419               # A0 only — reproducing a number needs its seed

N_PERM_RIDGE = 500                      # prereg §4
N_PERM_RF = 100
N_PERM_KW = 10000
RF_TREES_PUBLISHED = 500                # A0 gate
RF_TREES_NULL = 200                     # A2 cell, used for BOTH observed and null
K_STRATA, K_STRATA_2 = 5, 10

ALPHA_BON = 0.05 / 5                    # 0.01, prereg §7 — five-claim family
ALPHA_C4_PUB = 0.05 / 6                 # 0.008333, H-NEW-74's own bar; stricter, so it wins

TOL_RIDGE, TOL_RF, TOL_KW_H = 0.03, 0.05, 1.0     # prereg §4 A0

PUBLISHED = {
    "C1": {"finding": "H-NEW-192", "ridge_r2": 0.759, "rf_r2": 0.817,
           "ridge_mae": 10.81, "rf_mae": 7.96},
    "C2": {"finding": "H-NEW-183", "ridge_r2": 0.836, "ridge_mae": 8.74,
           "length_only_r2": 0.446, "length_only_mae": 19.30, "rf_r2": 0.844},
    "C3": {"finding": "H-NEW-233", "rf_r2": 0.8485, "ridge_r2": 0.7395,
           "rf_mae": 7.24, "ridge_mae": 10.66},
    "C4": {"finding": "H-NEW-74", "kw_H": 35.36, "kw_df": 3, "kw_p": 1.02e-7,
           "phase_means": {"Early Meccan": 1.74, "Middle Meccan": 4.89,
                           "Late Meccan": 8.95, "Medinan": 4.93}},
    "C5": {"finding": "H-NEW-231", "claim": "length is the dominant explanatory axis"},
}

# RECON-B substitutions for C1 (prereg §3)
RECON_B_SWAP = {"allah_density": "divine_name_density",
                "book_ref_density": "legal_term_density"}


def P(rel):
    return os.path.join(REPO, rel)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def die(msg):
    raise SystemExit("[FATAL] " + msg)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


# ===========================================================================
# 0. LOCKS
# ===========================================================================
_got = sha256_file(P(PREREG_REL))
if _got != PREREG_SHA256:
    die("PRE-REG SHA MISMATCH\n  expected %s\n  got      %s" % (PREREG_SHA256, _got))
log("[lock] pre-reg %s VERIFIED" % PREREG_SHA256[:16])
# Guarded so a `spawn`ed permutation worker does not re-hash a 20 MB morphology file
# twelve times over. The parent verifies every input before any worker exists; a worker
# that got a different file would have to have had it swapped mid-run.
if __name__ == "__main__":
    for _rel, _want in sorted(FROZEN.items()):
        _g = sha256_file(P(_rel))
        if _g != _want:
            die("FROZEN INPUT MISMATCH %s\n  expected %s\n  got      %s"
                % (_rel, _want, _g))
    log("[lock] %d frozen inputs VERIFIED" % len(FROZEN))


# ===========================================================================
# 1. INSTRUMENTS — lifted from the frozen published scripts (prereg §3)
# ===========================================================================
def _load_module(rel, name):
    spec = importlib.util.spec_from_file_location(name, P(rel))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


M183 = _load_module(SRC183_REL, "h183_lift")
M233 = _load_module(SRC233_REL, "h233_lift")
log("[MW-6] H-NEW-183 and H-NEW-233 modules lifted, both SHA-verified")

loocv_ridge = M183.loocv_ridge
r2_score = M183.r2_score
mae_score = M183.mae
impute_median = M183.impute_median

from sklearn.ensemble import RandomForestRegressor          # noqa: E402
from sklearn.model_selection import LeaveOneOut             # noqa: E402


def loocv_rf(X, y, n_estimators, seed):
    """H-NEW-183's loocv_rf, with n_estimators and random_state resolved at CALL time.

    A default argument would bind at definition time — the H-NEW-2770 disclosure.
    n_jobs=1: the forests are tiny (113 rows) so thread overhead dominates, and the
    permutation loop is parallelised across DRAWS instead (see `_rf_r2_worker`).
    """
    n = X.shape[0]
    preds = np.zeros(n, dtype=float)
    for tr, te in LeaveOneOut().split(X):
        Xtr, meds = impute_median(X[tr])
        Xte, _ = impute_median(X[te], medians=meds)
        m = RandomForestRegressor(n_estimators=n_estimators, max_depth=None,
                                  random_state=seed, n_jobs=1)
        m.fit(Xtr, y[tr])
        preds[te] = m.predict(Xte)
    return preds


def rf_loocv_r2(X, y, trees, seed):
    """The same LOOCV RF as above, written self-contained so it can be shipped to a
    worker process: it closes over no dynamically-loaded module, only numpy + sklearn.

    Asserted bit-identical to the lifted H-NEW-183 routine at startup — see `_verify_rf`.
    """
    import numpy as _np
    from sklearn.ensemble import RandomForestRegressor as _RF
    from sklearn.model_selection import LeaveOneOut as _LOO

    def _imp(A, meds=None):
        A2 = A.copy()
        if meds is None:
            meds = _np.nanmedian(A2, axis=0)
        ind = _np.where(_np.isnan(A2))
        A2[ind] = _np.take(meds, ind[1])
        return A2, meds

    preds = _np.zeros(len(y))
    for tr, te in _LOO().split(X):
        Xtr, meds = _imp(X[tr])
        Xte, _ = _imp(X[te], meds)
        m = _RF(n_estimators=trees, max_depth=None, random_state=seed, n_jobs=1)
        m.fit(Xtr, y[tr])
        preds[te] = m.predict(Xte)
    ss_res = float(_np.sum((y - preds) ** 2))
    ss_tot = float(_np.sum((y - y.mean()) ** 2))
    return 1.0 - ss_res / ss_tot


def _verify_rf(X, y):
    """The parallel worker must be bit-identical to the lifted routine, not merely close."""
    a = rf_loocv_r2(X, y, 200, M183.SEED)
    b = r2_score(y, M183.loocv_rf(X, y, 200))
    if a != b:
        die("RF worker is not bit-identical to the lifted H-NEW-183 routine: %.15f vs %.15f"
            % (a, b))
    log("[MW-6] parallel RF worker asserted bit-identical to the lifted routine (%.12f)" % a)


# ===========================================================================
# 2. STATISTICS (explicit; the Spearman is asserted equal to H-NEW-2770's)
# ===========================================================================
def rank_array(values):
    order = sorted(range(len(values)), key=lambda i: values[i])
    out = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            out[order[k]] = avg
        i = j + 1
    return out


def spearman_rho(a, b):
    ra, rb = rank_array(list(a)), rank_array(list(b))
    n = len(ra)
    ma, mb = sum(ra) / n, sum(rb) / n
    num = sum((ra[i] - ma) * (rb[i] - mb) for i in range(n))
    da = math.sqrt(sum((x - ma) ** 2 for x in ra))
    db = math.sqrt(sum((x - mb) ** 2 for x in rb))
    return num / (da * db) if da and db else float("nan")


def quintiles(values, k):
    """Stratum id per element, by k-quantile of `values`. H-NEW-2770's routine verbatim."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    out = [0] * len(values)
    per = len(values) / k
    for pos, i in enumerate(order):
        out[i] = min(k - 1, int(pos / per))
    return out


def strata_groups(strata):
    g = defaultdict(list)
    for i, s in enumerate(strata):
        g[s].append(i)
    return list(g.values())


def perm_p(null_vals, obs):
    return (sum(1 for v in null_vals if v >= obs - 1e-15) + 1) / (len(null_vals) + 1)


def kruskal_wallis(groups):
    """H with tie correction, and the untied H, both returned. Explicit, no scipy."""
    allv = [v for g in groups for v in g]
    N = len(allv)
    r = rank_array(allv)
    idx, ranks = 0, []
    for g in groups:
        ranks.append(r[idx:idx + len(g)])
        idx += len(g)
    H = 12.0 / (N * (N + 1)) * sum(sum(rk) ** 2 / len(rk) for rk in ranks) - 3 * (N + 1)
    counts = Counter(allv)
    tie = sum(c ** 3 - c for c in counts.values() if c > 1)
    corr = 1.0 - tie / (N ** 3 - N) if N > 1 else 1.0
    return H, (H / corr if corr > 0 else float("nan")), corr


def epsilon_squared(H, N, k):
    return (H - k + 1) / (N - k)


# ===========================================================================
# 3. CORPUS + SIZE COLUMNS (the harness's own, from the frozen JSON)
# ===========================================================================
QURAN = json.load(open(P("quran-text/quran-no-tashkeel.json"), encoding="utf-8"))
SIDS = list(range(1, 115))
NV = {i + 1: len(s["verses"]) for i, s in enumerate(QURAN)}
NW = {i + 1: sum(len(v["text"].split()) for v in s["verses"]) for i, s in enumerate(QURAN)}
MVL = {s: NW[s] / NV[s] for s in SIDS}
LOGWC = {s: math.log(NW[s]) for s in SIDS}

H125 = json.load(open(P("findings/phase-b-hypotheses/csv/h-new-125.json"), encoding="utf-8"))
PSV = H125["per_surah_axis_values"]
NOLD_RANK = {int(k): v["noldeke_rank"] for k, v in PSV.items()}
NOLD_PHASE = {int(k): v["noldeke_phase"] for k, v in PSV.items()}
AXES = {int(k): v["axis_values"] for k, v in PSV.items()}

Y_MUSHAF = np.array([float(s) for s in SIDS])
Y_NOLD = np.array([float(NOLD_RANK[s]) for s in SIDS])

SIZE_COLS = {"log_word_count": [LOGWC[s] for s in SIDS],
             "verse_count": [float(NV[s]) for s in SIDS],
             "mean_verse_length": [MVL[s] for s in SIDS]}
X_SIZE3 = np.array([[SIZE_COLS[c][i] for c in
                     ("log_word_count", "verse_count", "mean_verse_length")]
                    for i in range(114)], dtype=float)

CHANNEL = {"mushaf": ("log_word_count", SIZE_COLS["log_word_count"]),
           "noldeke": ("mean_verse_length", SIZE_COLS["mean_verse_length"])}


def channel_table():
    out = {}
    for ordering, y in (("mushaf", [float(s) for s in SIDS]),
                        ("noldeke", [float(NOLD_RANK[s]) for s in SIDS])):
        out[ordering] = {c: round(spearman_rho(SIZE_COLS[c], y), 4) for c in SIZE_COLS}
    out["cross_mushaf_vs_noldeke"] = round(
        spearman_rho([float(s) for s in SIDS], [float(NOLD_RANK[s]) for s in SIDS]), 4)
    return out


# ===========================================================================
# 4. THE THREE ARMS, one function each — used by every claim
# ===========================================================================
def fit_r2(X, y, model, seed, rf_trees=RF_TREES_PUBLISHED):
    if model == "ridge":
        preds = loocv_ridge(X, y)
    else:
        preds = loocv_rf(X, y, rf_trees, seed)
    return r2_score(y, preds), mae_score(y, preds), preds


def size_baseline(y, ordering, model, seed, rf_trees):
    """Arm A1 — size-only baselines: S1 (primary channel alone), S3 (three size columns).

    No vocabulary, no morphology, no phonology. Same model class, same LOOCV, same seed.
    """
    chan_name, chan = CHANNEL[ordering]
    X_s1 = np.array(chan, dtype=float).reshape(-1, 1)
    r2_s1, mae_s1, _ = fit_r2(X_s1, y, model, seed, rf_trees)
    r2_s3, mae_s3, _ = fit_r2(X_SIZE3, y, model, seed, rf_trees)
    return {"channel": chan_name, "r2_S1": r2_s1, "mae_S1": mae_s1,
            "r2_S3": r2_s3, "mae_S3": mae_s3}


def arm_A2(X_full, y, ordering, model, seed, n_perm, k, rf_trees):
    """Size-matched null: permute the TARGET within k-quantile bins of the drift channel."""
    chan_name, chan = CHANNEL[ordering]
    groups = strata_groups(quintiles(chan, k))
    rng = random.Random(seed)
    obs, _, _ = fit_r2(X_full, y, model, seed, rf_trees)

    # The draw SEQUENCE is generated serially so it is identical whether or not the
    # evaluation is parallelised; only the (independent) model fits are distributed.
    draws, yy = [], list(y)
    for _ in range(n_perm):
        for idx in groups:
            vals = [yy[i] for i in idx]
            rng.shuffle(vals)
            for i, v in zip(idx, vals):
                yy[i] = v
        draws.append(list(yy))

    if model == "rf":
        # joblib/loky, not raw multiprocessing: `fork` deadlocks against sklearn's
        # thread pools on macOS and `spawn` re-imports this module per worker. Both were
        # observed hanging. The draws are already fixed above, so parallelising the fits
        # cannot change a single value.
        from joblib import Parallel, delayed
        # batch_size=1: joblib's `auto` batching lumped every draw into ONE batch, so a
        # single worker ran them serially while the rest idled at 0% CPU. Observed.
        nulls = Parallel(n_jobs=min(8, os.cpu_count()), backend="loky", batch_size=1)(
            delayed(rf_loocv_r2)(X_full, np.array(d, dtype=float), rf_trees, seed)
            for d in draws)
    else:
        nulls = [fit_r2(X_full, np.array(d, dtype=float), model, seed, rf_trees)[0]
                 for d in draws]
    arr = np.array(nulls)
    return {"channel": chan_name, "k_strata": k, "n_perm": n_perm,
            "observed_r2": obs, "null_mean": float(arr.mean()),
            "null_sd": float(arr.std(ddof=0)),
            "null_p50": float(np.percentile(arr, 50)),
            "null_p95": float(np.percentile(arr, 95)),
            "null_p99": float(np.percentile(arr, 99)),
            "null_max": float(arr.max()),
            "observed_pctile": float(100.0 * (arr < obs).mean()),
            "p": perm_p(nulls, obs),
            "beats_max": bool(obs > arr.max())}


# ===========================================================================
# 5. FEATURE MATRICES
# ===========================================================================
def build_matrices():
    X183, y183, sids183, names183 = M183.build_feature_matrix()
    X233, y233, sids233, names233 = M233.build_feature_matrix()
    if sids183 != SIDS or sids233 != SIDS:
        die("surah id ordering mismatch between the lifted matrices and the harness")
    base = M233.BASE_FEATURES
    idx = [names233.index(f) for f in base]
    X_reconA = X233[:, idx]
    # RECON-B: swap two columns for the two features H-NEW-192 names but BASE lacks
    X_reconB = X_reconA.copy()
    namesB = list(base)
    for src, dst in RECON_B_SWAP.items():
        j = namesB.index(src)
        namesB[j] = dst
        X_reconB[:, j] = np.array([AXES[s][dst] for s in SIDS], dtype=float)
    return {"X183": X183, "names183": names183, "y183": y183,
            "X233": X233, "names233": names233, "y233": y233,
            "X_reconA": X_reconA, "names_reconA": list(base),
            "X_reconB": X_reconB, "names_reconB": namesB}


DENSITY_FEATURES = {"allah_density", "qul_density", "book_ref_density",
                    "loanword_density", "eschat_density", "divine_name_density",
                    "legal_term_density"}
DENSITY_TO_AXIS = {"allah_density": "allah_density", "qul_density": "qul_density",
                   "book_ref_density": "book_reference_density",
                   "loanword_density": "loanword_density",
                   "eschat_density": "eschatological_density",
                   "divine_name_density": "divine_name_density",
                   "legal_term_density": "legal_term_density"}


def per_word_matrix(X, names):
    """A3: replace each per-verse density column by its exact per-word form."""
    X2 = X.copy()
    swapped = []
    for j, nm in enumerate(names):
        if nm in DENSITY_FEATURES:
            ax = DENSITY_TO_AXIS[nm]
            X2[:, j] = np.array([100.0 * (AXES[s][ax] * NV[s] / 100.0) / NW[s]
                                 for s in SIDS], dtype=float)
            swapped.append(nm)
    return X2, swapped


# ===========================================================================
# 6. CLAIM RUNNERS
# ===========================================================================
def classify_predictor(reproduced, p_a2, r2_full, r2_s3):
    """prereg §6, transcribed clause-for-clause. Do not paraphrase."""
    if not reproduced:
        return "DID-NOT-REPRODUCE"
    if p_a2 >= ALPHA_BON or r2_s3 >= r2_full - 0.02:
        return "DOES-NOT-SURVIVE"
    if 0.02 <= (r2_full - r2_s3) < 0.10:
        return "GENRE-SHARED-BUT-LARGER"
    if (r2_full - r2_s3) >= 0.10:
        return "SURVIVES"
    return "UNCLASSIFIED"


def run_predictor_claim(cid, X, names, y, ordering, model, pub_r2, seed, args):
    tag = "%s/%s" % (cid, model)
    log("\n  [%s] n_features=%d ordering=%s" % (tag, X.shape[1], ordering))
    t0 = time.time()
    rf_trees_gate = RF_TREES_PUBLISHED
    r2_pub_seed, mae_pub, _ = fit_r2(X, y, model, SEED_PUBLISHED, rf_trees_gate)
    tol = TOL_RIDGE if model == "ridge" else TOL_RF
    reproduced = abs(r2_pub_seed - pub_r2) <= tol if pub_r2 is not None else None
    log("    A0 published %.4f  recomputed %.4f  (tol %.2f) -> %s"
        % (pub_r2 if pub_r2 else float("nan"), r2_pub_seed, tol, reproduced))

    rf_trees = RF_TREES_NULL if model == "rf" else RF_TREES_PUBLISHED
    r2_full, mae_full, _ = fit_r2(X, y, model, seed, rf_trees)
    base = size_baseline(y, ordering, model, seed, rf_trees)
    log("    A1 full %.4f | S1(%s) %.4f | S3 %.4f | dR2 %+0.4f"
        % (r2_full, base["channel"], base["r2_S1"], base["r2_S3"],
           r2_full - base["r2_S3"]))

    n_perm = (N_PERM_RIDGE if model == "ridge" else N_PERM_RF)
    if args.smoke:
        n_perm = 6
    a2 = arm_A2(X, y, ordering, model, seed, n_perm, K_STRATA, rf_trees)
    a2b = arm_A2(X, y, ordering, model, seed, max(2, n_perm // 5), K_STRATA_2, rf_trees)
    log("    A2 obs %.4f vs null mean %.4f  p95 %.4f  max %.4f  p=%.4f  pct=%.1f"
        % (a2["observed_r2"], a2["null_mean"], a2["null_p95"], a2["null_max"],
           a2["p"], a2["observed_pctile"]))

    Xpw, swapped = per_word_matrix(X, names)
    r2_pw, mae_pw, _ = fit_r2(Xpw, y, model, seed, rf_trees)
    log("    A3 per-word densities (%d cols) R2 %.4f (delta %+0.4f)"
        % (len(swapped), r2_pw, r2_pw - r2_full))

    verdict = classify_predictor(reproduced, a2["p"], r2_full, base["r2_S3"])
    log("    -> %s   [%.0fs]" % (verdict, time.time() - t0))
    return {"claim": cid, "model": model, "ordering": ordering,
            "n_features": int(X.shape[1]), "features": list(names),
            "A0": {"published_r2": pub_r2, "recomputed_r2": r2_pub_seed,
                   "mae": mae_pub, "tolerance": tol, "reproduced": reproduced,
                   "seed_used": SEED_PUBLISHED,
                   "rf_trees": rf_trees_gate if model == "rf" else None},
            "A1": dict(base, r2_full=r2_full, mae_full=mae_full,
                       delta_r2_full_minus_S3=r2_full - base["r2_S3"],
                       rf_trees=rf_trees if model == "rf" else None),
            "A2": a2, "A2_k10": a2b,
            "A3": {"r2_per_word": r2_pw, "delta": r2_pw - r2_full,
                   "columns_swapped": swapped},
            "verdict": verdict}


def run_C4(seed, args):
    """qul density x Noldeke 4-phase Kruskal-Wallis, per verse and per word."""
    log("\n  [C4] H-NEW-74 Cell 6 — qul density x Noldeke phase")
    order = ["Early Meccan", "Middle Meccan", "Late Meccan", "Medinan"]
    pv = {s: AXES[s]["qul_density"] for s in SIDS}
    cnt = {s: pv[s] * NV[s] / 100.0 for s in SIDS}
    pw = {s: 100.0 * cnt[s] / NW[s] for s in SIDS}
    total_qul = sum(cnt.values())

    def groups_of(d):
        return [[d[s] for s in SIDS if NOLD_PHASE[s] == ph] for ph in order]

    res = {"claim": "C4", "finding": "H-NEW-74", "qul_total_recovered": total_qul,
           "phase_order": order}
    for label, d in (("per_verse", pv), ("per_word", pw)):
        g = groups_of(d)
        H, Hc, corr = kruskal_wallis(g)
        N = sum(len(x) for x in g)
        res[label] = {
            "n": [len(x) for x in g],
            "mean": [float(np.mean(x)) for x in g],
            "median": [float(np.median(x)) for x in g],
            "H_uncorrected": H, "H_tie_corrected": Hc, "tie_correction": corr,
            "epsilon_squared": epsilon_squared(Hc, N, 4)}
    a0_pub = PUBLISHED["C4"]["kw_H"]
    got = res["per_verse"]["H_tie_corrected"]
    got_unc = res["per_verse"]["H_uncorrected"]
    reproduced = min(abs(got - a0_pub), abs(got_unc - a0_pub)) <= TOL_KW_H
    log("    A0 published H=%.2f  recomputed H=%.4f (untied %.4f) -> %s"
        % (a0_pub, got, got_unc, reproduced))

    # A2 — permute the phase LABEL within MVL quintiles
    n_perm = 200 if args.smoke else N_PERM_KW
    chan = SIZE_COLS["mean_verse_length"]
    groups = strata_groups(quintiles(chan, K_STRATA))
    phases = [NOLD_PHASE[s] for s in SIDS]
    rng = random.Random(seed)
    out = {}
    for label, d in (("per_verse", pv), ("per_word", pw)):
        vals = [d[s] for s in SIDS]
        obs = res[label]["H_tie_corrected"]
        pp = list(phases)
        nulls, free = [], []
        for _ in range(n_perm):
            for idx in groups:
                sub = [pp[i] for i in idx]
                rng.shuffle(sub)
                for i, v in zip(idx, sub):
                    pp[i] = v
            g = [[vals[i] for i in range(114) if pp[i] == ph] for ph in order]
            if min(len(x) for x in g) == 0:
                continue
            nulls.append(kruskal_wallis(g)[1])
        pf = list(phases)
        for _ in range(n_perm):
            rng.shuffle(pf)
            g = [[vals[i] for i in range(114) if pf[i] == ph] for ph in order]
            if min(len(x) for x in g) == 0:
                continue
            free.append(kruskal_wallis(g)[1])
        out[label] = {"observed_H": obs, "n_perm": len(nulls),
                      "null_mean_stratified": float(np.mean(nulls)),
                      "null_p95_stratified": float(np.percentile(nulls, 95)),
                      "p_stratified": perm_p(nulls, obs),
                      "null_mean_free": float(np.mean(free)),
                      "p_free_shuffle": perm_p(free, obs)}
        log("    A2 %-9s H=%.3f  strat-null mean %.3f p95 %.3f  p_strat=%.5f "
            "| free-shuffle p=%.5f"
            % (label, obs, out[label]["null_mean_stratified"],
               out[label]["null_p95_stratified"], out[label]["p_stratified"],
               out[label]["p_free_shuffle"]))
    res["A2"] = out
    res["A0_reproduced"] = reproduced

    e_pv = res["per_verse"]["epsilon_squared"]
    e_pw = res["per_word"]["epsilon_squared"]
    drop = 1.0 - (e_pw / e_pv) if e_pv else float("nan")
    res["epsilon_squared_drop_fraction"] = drop
    p_st = out["per_verse"]["p_stratified"]
    p_pw = out["per_word"]["p_stratified"]
    if not reproduced:
        v = "DID-NOT-REPRODUCE"
    elif p_st >= ALPHA_C4_PUB or p_pw >= ALPHA_C4_PUB:
        v = "DOES-NOT-SURVIVE"
    elif drop >= 0.50:
        v = "GENRE-SHARED-BUT-LARGER"
    else:
        v = "SURVIVES"
    res["verdict"] = v
    log("    eps2 per-verse %.4f -> per-word %.4f (drop %.1f%%)  -> %s"
        % (e_pv, e_pw, 100 * drop, v))
    return res


def run_C5(seed):
    """Calibration arm: does the harness recover H-NEW-231's self-declared length axis?"""
    log("\n  [C5] H-NEW-231 — calibration (KL divergence vs length)")
    corpus_counts = Counter()
    per_surah = {}
    for i, s in enumerate(QURAN):
        c = Counter()
        for v in s["verses"]:
            c.update(v["text"].split())
        per_surah[i + 1] = c
        corpus_counts.update(c)
    vocab = sorted(corpus_counts)
    V = len(vocab)
    pos = {w: i for i, w in enumerate(vocab)}
    tot = sum(corpus_counts.values())
    a = 0.5
    qv = np.array([(corpus_counts[w] + a) / (tot + a * V) for w in vocab])
    log_q_sum = float(np.log(qv).sum())
    kl = {}
    for s in SIDS:
        c = per_surah[s]
        n = sum(c.values())
        denom = n + a * V
        p0 = a / denom                       # smoothed mass on every UNSEEN type
        # KL is a sum over the WHOLE vocabulary, not only the types the surah contains:
        # the smoothed p puts mass p0 on every unseen type, and that mass is where the
        # length dependence lives. Summing only over present types drops it entirely.
        acc = 0.0
        log_q_seen = 0.0
        for w, k in c.items():
            j = pos[w]
            p = (k + a) / denom
            acc += p * math.log(p / qv[j])
            log_q_seen += math.log(qv[j])
        n_unseen = V - len(c)
        acc += p0 * (n_unseen * math.log(p0) - (log_q_sum - log_q_seen))
        kl[s] = acc
    logtok = [math.log10(NW[s]) for s in SIDS]
    klv = [kl[s] for s in SIDS]
    rho = spearman_rho(klv, logtok)
    x = np.array(logtok).reshape(-1, 1)
    yv = np.array(klv)
    r2, _, _ = fit_r2(x, yv, "ridge", seed, RF_TREES_PUBLISHED)
    pear = float(np.corrcoef(logtok, klv)[0, 1])
    log("    rho(KL, log10 tokens) = %+0.4f | pearson %+0.4f | LOOCV R2 (length only) %.4f"
        % (rho, pear, r2))
    return {"claim": "C5", "finding": "H-NEW-231", "spearman_kl_vs_logtokens": rho,
            "pearson": pear, "loocv_r2_length_only": r2,
            "D4_passes": abs(rho) >= 0.70}


# ===========================================================================
# 7. MAIN
# ===========================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--only", default="", help="comma-separated claim ids, e.g. C1,C2")
    args = ap.parse_args()

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rundir = os.path.join(REPO, "findings/phase-b-hypotheses/runs",
                          "h-new-2790-SMOKE" if args.smoke else "h-new-2790", stamp)
    os.makedirs(rundir, exist_ok=False)
    log("[run] %s" % os.path.relpath(rundir, REPO))

    T0 = time.time()
    chan = channel_table()
    log("[§2] drift channels: %s" % json.dumps(chan))

    # Spearman cross-check against the published drift table (prereg §2)
    expect = {"mushaf": {"log_word_count": -0.9342, "verse_count": -0.8446,
                         "mean_verse_length": -0.7131},
              "noldeke": {"mean_verse_length": 0.9038, "log_word_count": 0.6892,
                          "verse_count": 0.3903}}
    for o in expect:
        for c, want in expect[o].items():
            if abs(chan[o][c] - want) > 0.0005:
                die("§2 channel check failed: %s/%s got %.4f expected %.4f"
                    % (o, c, chan[o][c], want))
    log("[§2] all six channel correlations reproduce UNIT-DRIFT-DEFECT §3")

    M = build_matrices()
    log("[matrices] 183=%s  233=%s  reconA=%s  reconB=%s"
        % (M["X183"].shape, M["X233"].shape, M["X_reconA"].shape, M["X_reconB"].shape))
    _verify_rf(M["X183"], M["y183"])

    # What H-NEW-183's published "length-only baseline" actually is (prereg §9)
    j183 = json.load(open(P("findings/phase-b-hypotheses/csv/h-new-183.json"),
                          encoding="utf-8"))
    lo = j183.get("model_B_ridge_length_only", {})
    logN = M["X183"][:, M["names183"].index("log_length")]
    baseline_probe = {
        "declared_features": lo.get("features"),
        "published_r2": lo.get("r2_loocv", lo.get("r2")),
        "rho_log_length_vs_noldeke": round(spearman_rho(list(logN), list(Y_NOLD)), 4),
        "rho_log_length_vs_my_log_word_count": round(
            spearman_rho(list(logN), SIZE_COLS["log_word_count"]), 4),
        "rho_log_length_vs_verse_count": round(
            spearman_rho(list(logN), SIZE_COLS["verse_count"]), 4)}
    log("[probe] H-NEW-183 length-only baseline = %s ; rho(log_length, Noldeke) = %+0.4f ; "
        "rho(log_length, my log word count) = %+0.4f ; rho(log_length, verse count) = %+0.4f"
        % (baseline_probe["declared_features"],
           baseline_probe["rho_log_length_vs_noldeke"],
           baseline_probe["rho_log_length_vs_my_log_word_count"],
           baseline_probe["rho_log_length_vs_verse_count"]))

    want = set(x.strip() for x in args.only.split(",") if x.strip())
    cells = {}

    def snapshot(partial=True):
        """Write results after every cell. A long run on a contended machine must never
        be lost to a crash or a kill; the final write below is byte-identical in form."""
        with open(os.path.join(rundir, "results.json"), "w", encoding="utf-8") as fh:
            json.dump({"finding_id": "H-NEW-2790", "partial": partial,
                       "prereg_sha256": PREREG_SHA256, "prereg": PREREG_REL,
                       "seeds": {"primary": SEED, "replication": SEED_REPL,
                                 "published_used_in_A0_only": SEED_PUBLISHED},
                       "alpha_bon": ALPHA_BON, "alpha_C4_published": ALPHA_C4_PUB,
                       "drift_channels": chan,
                       "h_new_183_length_only_baseline_probe": baseline_probe,
                       "cells": cells, "smoke": args.smoke,
                       "elapsed_s": round(time.time() - T0, 1)},
                      fh, ensure_ascii=False, indent=2, default=float)
    for seed_label, seed in (("PRIMARY", SEED), ("REPLICATION", SEED_REPL)):
        log("\n" + "=" * 74 + "\nCELL %s seed=%d\n" % (seed_label, seed) + "=" * 74)
        C = {}
        if not want or "C1" in want:
            C["C1_reconA_ridge"] = run_predictor_claim(
                "C1-RECON-A", M["X_reconA"], M["names_reconA"], Y_MUSHAF, "mushaf",
                "ridge", PUBLISHED["C1"]["ridge_r2"], seed, args)
            C["C1_reconA_rf"] = run_predictor_claim(
                "C1-RECON-A", M["X_reconA"], M["names_reconA"], Y_MUSHAF, "mushaf",
                "rf", PUBLISHED["C1"]["rf_r2"], seed, args)
            C["C1_reconB_ridge"] = run_predictor_claim(
                "C1-RECON-B", M["X_reconB"], M["names_reconB"], Y_MUSHAF, "mushaf",
                "ridge", PUBLISHED["C1"]["ridge_r2"], seed, args)
            C["C1_reconB_rf"] = run_predictor_claim(
                "C1-RECON-B", M["X_reconB"], M["names_reconB"], Y_MUSHAF, "mushaf",
                "rf", PUBLISHED["C1"]["rf_r2"], seed, args)
            cells[seed_label] = C; snapshot()
        if not want or "C2" in want:
            C["C2_ridge"] = run_predictor_claim(
                "C2", M["X183"], M["names183"], Y_NOLD, "noldeke", "ridge",
                PUBLISHED["C2"]["ridge_r2"], seed, args)
            C["C2_rf"] = run_predictor_claim(
                "C2", M["X183"], M["names183"], Y_NOLD, "noldeke", "rf",
                PUBLISHED["C2"]["rf_r2"], seed, args)
            cells[seed_label] = C; snapshot()
        if not want or "C3" in want:
            C["C3_rf"] = run_predictor_claim(
                "C3", M["X233"], M["names233"], Y_MUSHAF, "mushaf", "rf",
                PUBLISHED["C3"]["rf_r2"], seed, args)
            C["C3_ridge"] = run_predictor_claim(
                "C3", M["X233"], M["names233"], Y_MUSHAF, "mushaf", "ridge",
                PUBLISHED["C3"]["ridge_r2"], seed, args)
            cells[seed_label] = C; snapshot()
        if not want or "C4" in want:
            C["C4"] = run_C4(seed, args)
            cells[seed_label] = C; snapshot()
        if not want or "C5" in want:
            C["C5"] = run_C5(seed)
        cells[seed_label] = C

    # seed fragility
    frag = []
    for k in cells["PRIMARY"]:
        a = cells["PRIMARY"][k].get("verdict")
        b = cells["REPLICATION"].get(k, {}).get("verdict")
        if a is not None and a != b:
            frag.append({"cell": k, "primary": a, "replication": b})

    out = {"finding_id": "H-NEW-2790",
           "prereg_sha256": PREREG_SHA256,
           "prereg": PREREG_REL,
           "seeds": {"primary": SEED, "replication": SEED_REPL,
                     "published_used_in_A0_only": SEED_PUBLISHED},
           "alpha_bon": ALPHA_BON, "alpha_C4_published": ALPHA_C4_PUB,
           "drift_channels": chan,
           "h_new_183_length_only_baseline_probe": baseline_probe,
           "cells": cells, "seed_fragile": frag,
           "elapsed_s": round(time.time() - T0, 1),
           "smoke": args.smoke}
    with open(os.path.join(rundir, "results.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2, default=float)
    manifest = {"finding_id": "H-NEW-2790", "run_utc": stamp,
                "prereg": {"path": PREREG_REL, "sha256": PREREG_SHA256},
                "script": {"path": "findings/phase-b-hypotheses/scripts/h-new-2790.py",
                           "sha256": sha256_file(os.path.abspath(__file__))},
                "frozen_inputs": [{"path": k, "sha256": v}
                                  for k, v in sorted(FROZEN.items())],
                "python": platform.python_version(),
                "platform": platform.platform(),
                "libs": {}}
    try:
        import sklearn
        manifest["libs"] = {"numpy": np.__version__, "sklearn": sklearn.__version__}
    except Exception:
        pass
    with open(os.path.join(rundir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    if not args.smoke:
        with open(P("findings/phase-b-hypotheses/csv/h-new-2790.json"), "w",
                  encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2, default=float)
    log("\n[done] %.0fs -> %s" % (out["elapsed_s"], os.path.relpath(rundir, REPO)))
    for k, v in cells["PRIMARY"].items():
        if "verdict" in v:
            log("  %-22s %s" % (k, v["verdict"]))
    if frag:
        log("  SEED-FRAGILE cells: %s" % frag)


if __name__ == "__main__":
    main()
