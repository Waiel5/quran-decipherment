#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2810 — Re-deriving the hard-coded literals.

`findings/UNIT-DRIFT-DEFECT.md` §6.3 established UNVERIFIABLE: a claim whose headline number
is produced by no code in the repository. Such a number is consumed downstream as a fixed
input — sometimes as a decision threshold — so every result built on it inherits an unverified
constant while looking corroborated. This runner re-derives all nine.

  L1  0.759   H-NEW-192 Ridge   no script, no JSON  -> exhaustive C(21,5) feature search
  L2  0.817   H-NEW-192 RF      no script, no JSON  -> same, Channel B
  L3  0.836   H-NEW-183 Ridge   literal vs artifact
  L4  0.7395  H-NEW-233 Ridge   literal vs artifact
  L5  0.8485  H-NEW-233 RF      literal vs artifact
  L6  0.4138  H-NEW-88  RF top1 literal vs artifact
  L7  0.6552  H-NEW-165 RF top1 literal vs artifact
  L8  136     H-NEW-1710 Musa   re-derived from Leeds QAC directly
  L9  0.9230  H-NEW-1395 null   literal vs artifact

RUN HYGIENE — this is the first runner written under the corrected §7 rule that H-NEW-2790's
own defect produced: **a run script must never overwrite a file inside its own run directory.**
`results.json` is written EXACTLY ONCE, at completion. Progress checkpoints go to
`progress/NNNNNN.json` OUTSIDE the run directory, each written once and never rewritten.

Pre-reg : findings/phase-b-hypotheses/prereg-h-new-2810-unverifiable-rederivation.md
          SHA-256 embedded below, verified at runtime; mismatch -> SystemExit.
Seeds   : 20260509 primary / 20260519 replication.
Author  : Waiel Al-Shujaa.  Bismillahi al-Rahmani al-Rahim.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import os
import platform
import random
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # findings/phase-b-hypotheses
REPO = os.path.dirname(os.path.dirname(ROOT))     # repo root

PREREG_REL = ("findings/phase-b-hypotheses/"
              "prereg-h-new-2810-unverifiable-rederivation.md")
PREREG_SHA256 = "9e09aaa147b9a238b2514f42adbf28cbcd706bc6b43a855d45c24e6b966d16b4"

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
    "findings/phase-b-hypotheses/csv/h-new-88.json":
        "3c3933a84e1a8b1d646ffd04e92b631514dd51a24d5826cebfaa53b0c440ae4b",
    "findings/phase-b-hypotheses/csv/h-new-165-2.json":
        "57de33891f8fc6528ec7ad9a26e898cd0eb1d77951245b6554fc87310e1b4657",
    "findings/phase-b-hypotheses/csv/h-new-1395.json":
        "6220fb2bcc9aa5bb02ea1d06fa82245e11945790fd6e4e6216ad29e142c542d7",
    "findings/phase-b-hypotheses/csv/h-new-1710.json":
        "78443356452b34fd0251ab4b8ea24df21a9a96664b22b2a13613ac987b313e60",
    "surahs/Q028-al-qasas/csv/Q028-F-06.json":
        "11bfae66abecb608d10576bfc2b9eefd2d259d290909f28d99d09fb900af0368",
    SRC183_REL: "a30666c03c8bbdc0fa618099497ebe6962306cf7c712d5abf1b7adbbd025db2b",
    SRC233_REL: "ad69720a10159c43094336fab9890671743b545fbcfef5c53db1bbcb3478edd7",
}

SEED, SEED_REPL = 20260509, 20260519
TOL_RIDGE = 0.0005          # prereg §4
TOL_RF = 0.005
TOL_IMPORTANCE = 0.02
N_CHANNEL_B = 50
RF_TREES_B = 200

# prereg §3.3 — the ten features H-NEW-192 names, fixed in every candidate
FIXED_TEN = ["verse_count", "mean_verse_len", "eschat_density", "type_token_ratio",
             "divine_name_density", "loanword_density", "qul_density",
             "legal_term_density", "muq_cardinality", "refrain_score"]
# the two columns not in H-NEW-233's matrix, built from H-NEW-125 axes
EXTRA_AXES = {"divine_name_density": "divine_name_density",
              "legal_term_density": "legal_term_density"}
PUB_IMPORTANCE = [("verse_count", 0.416), ("mean_verse_len", 0.173),
                  ("eschat_density", 0.125), ("type_token_ratio", 0.095),
                  ("divine_name_density", 0.053), ("loanword_density", 0.048),
                  ("qul_density", 0.039), ("legal_term_density", 0.012),
                  ("muq_cardinality", 0.010), ("refrain_score", 0.009)]

LITERALS = {
    "L1": {"value": 0.759, "claim": "H-NEW-192 Ridge LOOCV R2 (mushaf, 15 features)",
           "consumed": ["scripts/h_new_233_ensemble_predictor.py:532,571",
                        "scripts/h_new_250_equation_fit.py:670"]},
    "L2": {"value": 0.817, "claim": "H-NEW-192 RF LOOCV R2 (mushaf, 15 features)",
           "consumed": ["scripts/h_new_233_ensemble_predictor.py:533,572",
                        "scripts/h_new_250_equation_fit.py:671"]},
    "L3": {"value": 0.836, "claim": "H-NEW-183 Ridge LOOCV R2 (Noldeke)",
           "consumed": ["scripts/h_new_233_ensemble_predictor.py:573",
                        "scripts/h_new_250_equation_fit.py:674"],
           "artifact": ("findings/phase-b-hypotheses/csv/h-new-183.json",
                        ["model_A_ridge_full", "r2_loocv"])},
    "L4": {"value": 0.7395, "claim": "H-NEW-233 Ridge LOOCV R2 (29 features)",
           "consumed": ["scripts/h_new_250_equation_fit.py:672"],
           "artifact": ("findings/phase-b-hypotheses/csv/h-new-233.json",
                        ["model_A_ridge", "r2_loocv"])},
    "L5": {"value": 0.8485, "claim": "H-NEW-233 RF LOOCV R2 (29 features)",
           "consumed": ["scripts/h_new_250_equation_fit.py:673"],
           "artifact": ("findings/phase-b-hypotheses/csv/h-new-233.json",
                        ["model_B_rf", "r2_loocv"])},
    "L6": {"value": 0.4138, "claim": "H-NEW-88 RF LOOCV top-1 accuracy",
           "consumed": ["scripts/h_new_179_alpha_beta_predictor.py:533"],
           "artifact": ("findings/phase-b-hypotheses/csv/h-new-88.json",
                        ["results_by_classifier", "rf", "loocv_top1_accuracy"])},
    "L7": {"value": 0.6552, "claim": "H-NEW-165 RF top-1 accuracy",
           "consumed": ["scripts/h_new_275_bukhari_opener_phonological_replication.py:385"],
           "artifact": ("findings/phase-b-hypotheses/csv/h-new-165-2.json",
                        ["baseline_reference", "h_new_165_rf_top1"])},
    "L8": {"value": 136, "claim": "H-NEW-1710 total Musa mentions (corpus)",
           "consumed": ["scripts/Q028_F_06_musa_density_rank.py:126"],
           "artifact": ("findings/phase-b-hypotheses/csv/h-new-1710.json",
                        ["prophet_name_distribution", "Mūsā (موسى)", "total"])},
    "L9": {"value": 0.9230, "claim": "H-NEW-1395 null uniform mean",
           "consumed": ["scripts/Q030_F_08_alm_cluster_fr_cohesion.py:184"],
           "artifact": ("findings/phase-b-hypotheses/csv/h-new-1395.json",
                        ["cell_A", "null_mean"])},
}


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
if __name__ == "__main__":
    for _rel, _want in sorted(FROZEN.items()):
        _g = sha256_file(P(_rel))
        if _g != _want:
            die("FROZEN INPUT MISMATCH %s\n  expected %s\n  got      %s"
                % (_rel, _want, _g))
    log("[lock] %d frozen inputs VERIFIED" % len(FROZEN))


# ===========================================================================
# 1. INSTRUMENTS — lifted from the frozen published scripts
# ===========================================================================
def _load_module(rel, name):
    spec = importlib.util.spec_from_file_location(name, P(rel))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


M183 = _load_module(SRC183_REL, "h183_lift_2810")
M233 = _load_module(SRC233_REL, "h233_lift_2810")
loocv_ridge = M183.loocv_ridge
r2_score = M183.r2_score
impute_median = M183.impute_median
log("[MW-6] H-NEW-183 and H-NEW-233 modules lifted, both SHA-verified")


def round_half_up(x, nd):
    """Decimal round-half-up, so 0.8355 -> 0.836 rather than banker's 0.836/0.835 ambiguity."""
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal(repr(x)).quantize(Decimal("1." + "0" * nd), rounding=ROUND_HALF_UP))


def dig(d, path):
    for k in path:
        d = d[k]
    return d


# ===========================================================================
# 2. ARM A — literal vs artifact (L3-L7, L9) and the L8 corpus re-derivation
# ===========================================================================
def arm_literal_vs_artifact(tag):
    spec = LITERALS[tag]
    rel, path = spec["artifact"]
    d = json.load(open(P(rel), encoding="utf-8"))
    actual = dig(d, path)
    lit = spec["value"]
    nd = len(repr(lit).split(".")[1]) if "." in repr(lit) else 0
    rounded = round_half_up(actual, nd) if nd else float(actual)
    ok = abs(rounded - lit) < 10 ** (-(nd + 3))
    return {"tag": tag, "literal": lit, "artifact_path": rel + " -> /" + "/".join(map(str, path)),
            "artifact_value": actual, "literal_precision_dp": nd,
            "artifact_rounded_to_that_precision": rounded,
            "verdict": "CONFIRMS" if ok else "CORRECTS"}


MUSA_LEMMA_RE = re.compile(r"LEM:muwsaY`")   # Q028_F_06_musa_density_rank.py:24, verbatim


def arm_L8():
    """Re-derive the Musa total from the Leeds QAC directly (prereg §3.2)."""
    per_surah = Counter()
    total = 0
    with open(P("data/morphology/quranic-corpus-morphology-0.4.txt"), encoding="utf-8") as f:
        for line in f:
            if not line.startswith("("):
                continue
            if MUSA_LEMMA_RE.search(line):
                loc = line.split("\t", 1)[0].strip("()")
                sid = int(loc.split(":")[0])
                per_surah[sid] += 1
                total += 1
    q28 = json.load(open(P("surahs/Q028-al-qasas/csv/Q028-F-06.json"), encoding="utf-8"))
    d1710 = json.load(open(P("findings/phase-b-hypotheses/csv/h-new-1710.json"), encoding="utf-8"))
    art = dig(d1710, LITERALS["L8"]["artifact"][1])
    lit = LITERALS["L8"]["value"]
    return {"tag": "L8", "literal": lit,
            "rederived_from_QAC": total,
            "h_new_1710_json_value": art,
            "Q028_F_06_own_recount": q28.get("corpus_total_musa_qac"),
            "q28_surah_count_rederived": per_surah.get(28, 0),
            "q28_surah_count_published": q28.get("q28_absolute_count_qac"),
            "verdict": "CONFIRMS" if (total == lit == art == q28.get("corpus_total_musa_qac"))
                       else "CORRECTS"}


# ===========================================================================
# 3. ARM B — the exhaustive feature-set search for L1/L2 (prereg §3.3)
# ===========================================================================
def build_pool():
    X233, y233, sids, names233 = M233.build_feature_matrix()
    if sids != list(range(1, 115)):
        die("surah id ordering mismatch in the lifted 233 matrix")
    h125 = json.load(open(P("findings/phase-b-hypotheses/csv/h-new-125.json"),
                          encoding="utf-8"))["per_surah_axis_values"]
    cols = {n: X233[:, i] for i, n in enumerate(names233)}
    for name, axis in EXTRA_AXES.items():
        cols[name] = np.array([h125[str(s)]["axis_values"][axis] for s in sids], dtype=float)
    missing = [f for f in FIXED_TEN if f not in cols]
    if missing:
        die("named feature(s) absent from the pool: %s" % missing)
    free = sorted(k for k in cols if k not in FIXED_TEN)
    y_mushaf = np.array([float(s) for s in sids])
    return cols, free, y_mushaf


def arm_exhaustive(cols, free, y, progress_dir, args):
    from math import comb
    k = 5
    total = comb(len(free), k)
    log("[L1/L2] exhaustive search: C(%d,%d) = %d candidate 15-feature sets"
        % (len(free), k, total))
    target = LITERALS["L1"]["value"]
    fixed = np.column_stack([cols[f] for f in FIXED_TEN])
    rows = []
    t0 = time.time()
    limit = 60 if args.smoke else None
    for i, combo in enumerate(itertools.combinations(free, k)):
        if limit and i >= limit:
            break
        X = np.column_stack([fixed] + [cols[c] for c in combo])
        r2 = r2_score(y, loocv_ridge(X, y))
        rows.append((r2, combo))
        if (i + 1) % 2000 == 0:
            # write-once checkpoint OUTSIDE the run directory (prereg §8)
            cp = os.path.join(progress_dir, "%06d.json" % (i + 1))
            with open(cp, "x", encoding="utf-8") as fh:
                json.dump({"evaluated": i + 1, "of": total,
                           "elapsed_s": round(time.time() - t0, 1),
                           "best_abs_dev_so_far": min(abs(r - target) for r, _ in rows)},
                          fh)
            log("    %6d / %d   %.0fs   closest |dR2| so far %.4f"
                % (i + 1, total, time.time() - t0,
                   min(abs(r - target) for r, _ in rows)))
    rows.sort(key=lambda t: abs(t[0] - target))
    allr2 = np.array([r for r, _ in rows])
    matches = [(r, c) for r, c in rows if abs(r - target) <= TOL_RIDGE]
    return {"n_evaluated": len(rows), "n_total_space": total,
            "target": target, "tolerance": TOL_RIDGE,
            "n_matches": len(matches),
            "matches": [{"r2": r, "extra_features": list(c)} for r, c in matches[:20]],
            "closest": [{"r2": r, "abs_dev": abs(r - target), "extra_features": list(c)}
                        for r, c in rows[:10]],
            "distribution": {"min": float(allr2.min()), "p05": float(np.percentile(allr2, 5)),
                             "median": float(np.median(allr2)),
                             "p95": float(np.percentile(allr2, 95)),
                             "max": float(allr2.max()), "mean": float(allr2.mean()),
                             "sd": float(allr2.std(ddof=0))},
            "min_abs_dev_from_literal": float(np.abs(allr2 - target).min())}, rows


def rf_importance_and_r2(X, y, trees, seed):
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import LeaveOneOut
    preds = np.zeros(len(y))
    for tr, te in LeaveOneOut().split(X):
        Xtr, meds = impute_median(X[tr])
        Xte, _ = impute_median(X[te], medians=meds)
        m = RandomForestRegressor(n_estimators=trees, random_state=seed, n_jobs=1)
        m.fit(Xtr, y[tr])
        preds[te] = m.predict(Xte)
    Xf, _ = impute_median(X)
    full = RandomForestRegressor(n_estimators=trees, random_state=seed, n_jobs=1).fit(Xf, y)
    return r2_score(y, preds), full.feature_importances_


def arm_channel_B(cols, y, rows, args):
    """RF importance-vector match on the N closest Ridge candidates plus N controls."""
    n = 6 if args.smoke else N_CHANNEL_B
    rng = random.Random(SEED)
    top = rows[:n]
    pool = rows[n:] if len(rows) > n else rows
    ctrl = rng.sample(pool, min(n, len(pool)))
    fixed = np.column_stack([cols[f] for f in FIXED_TEN])
    out = {"n_trees": RF_TREES_B, "seed": SEED, "target_rf_r2": LITERALS["L2"]["value"]}

    def score(group, label):
        res = []
        for r2ridge, combo in group:
            names = FIXED_TEN + list(combo)
            X = np.column_stack([fixed] + [cols[c] for c in combo])
            rf_r2, imp = rf_importance_and_r2(X, y, RF_TREES_B, SEED)
            im = dict(zip(names, imp))
            devs = [abs(im[f] - v) for f, v in PUB_IMPORTANCE]
            order_got = [f for f, _ in sorted(im.items(), key=lambda kv: -kv[1])][:10]
            res.append({"extra_features": list(combo), "ridge_r2": r2ridge, "rf_r2": rf_r2,
                        "rf_r2_abs_dev_from_literal": abs(rf_r2 - LITERALS["L2"]["value"]),
                        "importance_max_abs_dev": max(devs),
                        "rank_order_matches": order_got == [f for f, _ in PUB_IMPORTANCE],
                        "five_extra_importance_mass": float(sum(im[c] for c in combo))})
        res.sort(key=lambda d: d["importance_max_abs_dev"])
        out[label] = res
        return res
    a = score(top, "closest_ridge_candidates")
    b = score(ctrl, "random_controls")
    out["best_importance_max_abs_dev_overall"] = min(
        [d["importance_max_abs_dev"] for d in a + b])
    out["best_rf_r2_abs_dev_overall"] = min([d["rf_r2_abs_dev_from_literal"] for d in a + b])
    out["any_rank_order_match"] = any(d["rank_order_matches"] for d in a + b)
    out["published_importance_sum_of_named_ten"] = round(sum(v for _, v in PUB_IMPORTANCE), 3)
    return out


# ===========================================================================
# 4. MAIN
# ===========================================================================
def classify_L1_L2(exh, chB):
    """prereg §5, transcribed clause-for-clause. Do not paraphrase."""
    if exh["n_matches"] > 0:
        return "CONFIRMS-BY-RECOVERY", "RECOVERED"
    return "IRRECOVERABLE", "IRRECOVERABLE"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    tag = "h-new-2810-SMOKE" if args.smoke else "h-new-2810"
    rundir = os.path.join(REPO, "findings/phase-b-hypotheses/runs", tag, stamp)
    os.makedirs(rundir, exist_ok=False)
    # progress lives OUTSIDE the run directory — prereg §8, UNIT-DRIFT-DEFECT §7
    progress_dir = os.path.join(REPO, "findings/phase-b-hypotheses/runs",
                                tag + "-progress", stamp)
    os.makedirs(progress_dir, exist_ok=False)
    log("[run] %s" % os.path.relpath(rundir, REPO))
    log("[run] progress (outside run dir) %s" % os.path.relpath(progress_dir, REPO))

    T0 = time.time()
    results = {}

    log("\n=== ARM A: literal vs artifact ===")
    for t in ("L3", "L4", "L5", "L6", "L7", "L9"):
        r = arm_literal_vs_artifact(t)
        results[t] = r
        log("  %s literal %-8s artifact %-22s -> %s"
            % (t, r["literal"], "%.10f" % r["artifact_value"], r["verdict"]))

    log("\n=== ARM A': L8 re-derived from the corpus ===")
    r8 = arm_L8()
    results["L8"] = r8
    log("  L8 literal %s | QAC re-derivation %s | h-new-1710.json %s | Q028's own recount %s -> %s"
        % (r8["literal"], r8["rederived_from_QAC"], r8["h_new_1710_json_value"],
           r8["Q028_F_06_own_recount"], r8["verdict"]))

    log("\n=== ARM B: exhaustive feature-set search for L1/L2 ===")
    cols, free, y = build_pool()
    log("  pool = %d columns; %d fixed by name; %d free -> choose 5"
        % (len(cols), len(FIXED_TEN), len(free)))
    exh, rows = arm_exhaustive(cols, free, y, progress_dir, args)
    log("  matches within %.4f of %.3f : %d" % (TOL_RIDGE, exh["target"], exh["n_matches"]))
    log("  closest achievable R2 = %.6f (|dev| %.6f); space min %.4f max %.4f"
        % (exh["closest"][0]["r2"], exh["min_abs_dev_from_literal"],
           exh["distribution"]["min"], exh["distribution"]["max"]))
    chB = arm_channel_B(cols, y, rows, args)
    log("  Channel B: best importance max-abs-dev %.4f | best RF R2 dev %.4f | rank match %s"
        % (chB["best_importance_max_abs_dev_overall"], chB["best_rf_r2_abs_dev_overall"],
           chB["any_rank_order_match"]))
    v1, v2 = classify_L1_L2(exh, chB)
    results["L1"] = {"tag": "L1", "literal": LITERALS["L1"]["value"],
                     "exhaustive_search": exh, "verdict": v1}
    results["L2"] = {"tag": "L2", "literal": LITERALS["L2"]["value"],
                     "channel_B": chB, "verdict": v2}
    log("  -> L1 %s | L2 %s" % (v1, v2))

    out = {"finding_id": "H-NEW-2810", "prereg": PREREG_REL,
           "prereg_sha256": PREREG_SHA256,
           "seeds": {"primary": SEED, "replication": SEED_REPL},
           "literals": {k: {"value": v["value"], "claim": v["claim"],
                            "consumed_at": v["consumed"]} for k, v in LITERALS.items()},
           "results": results,
           "verdicts": {k: results[k]["verdict"] for k in sorted(results)},
           "elapsed_s": round(time.time() - T0, 1), "smoke": args.smoke}

    # ---- the ONLY write into the run directory, at completion (prereg §8) ----
    with open(os.path.join(rundir, "results.json"), "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2, default=float)
    manifest = {"finding_id": "H-NEW-2810", "run_utc": stamp,
                "prereg": {"path": PREREG_REL, "sha256": PREREG_SHA256},
                "script": {"path": "findings/phase-b-hypotheses/scripts/h-new-2810.py",
                           "sha256": sha256_file(os.path.abspath(__file__))},
                "frozen_inputs": [{"path": k, "sha256": v} for k, v in sorted(FROZEN.items())],
                "progress_dir_outside_run": os.path.relpath(progress_dir, REPO),
                "python": platform.python_version(), "platform": platform.platform()}
    try:
        import sklearn
        manifest["libs"] = {"numpy": np.__version__, "sklearn": sklearn.__version__}
    except Exception:
        pass
    with open(os.path.join(rundir, "manifest.json"), "x", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    if not args.smoke:
        with open(P("findings/phase-b-hypotheses/csv/h-new-2810.json"), "w",
                  encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2, default=float)
    log("\n[done] %.0fs -> %s" % (out["elapsed_s"], os.path.relpath(rundir, REPO)))
    for k in sorted(out["verdicts"]):
        log("  %-4s %s" % (k, out["verdicts"][k]))


if __name__ == "__main__":
    main()
