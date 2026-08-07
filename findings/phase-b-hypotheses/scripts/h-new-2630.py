#!/usr/bin/env python3
"""
H-NEW-2630 — Realis vs irrealis conditionals as the fourth register column
of the discourse-grammar law (cross-finding-028-formal).

Pre-registration is SHA-locked and verified at runtime. Frozen inputs are
SHA-locked and verified at runtime. Any mismatch is SystemExit.

Waiel Al-Shujaa, 2026-08-07.
"""
import json, hashlib, sys, os, datetime, itertools
import numpy as np
from scipy import stats

ROOT = "/Users/grey/Downloads/quran"

PREREG = "findings/phase-b-hypotheses/prereg-h-new-2630-conditional-register.md"
PREREG_SHA = "40f899a4bdb807d3ac39c679c532b51ab90fe7f020f4c01b4bd0dcd1281a2a5a"

FROZEN = {
    "data/morphology/quranic-corpus-morphology-0.4.txt":
        "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46",
    "findings/phase-b-hypotheses/csv/h-new-2500.json":
        "a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25",
    "findings/phase-b-hypotheses/csv/h-new-2530.json":
        "5ca17050c20b15734ad9a734e7bad7b938b616c924ec53dfcd24814a1473b68c",
    "data/hafs-verse-counts.tsv":
        "e1818fb04ac26b863ce1ade50193390d481345a3971919aeb120daf8946212ba",
}

SEED, SEED_REP, NPERM, K_BONF = 20260509, 20260519, 10000, 5
ALPHA_BONF = 0.05 / K_BONF

REALIS = {"<in"}
REALIS_WIDE = {"<in", "<iyn", "<im~aA", "<il~am"}
IRREALIS = {"law", "lawolaA^"}
GENERALISING = {"man", "maA"}          # MW-6 substantive control
EXPECT_COND_TOTAL = 1049
EXPECT_LEM = {"<in": 578, "law": 185, "lawolaA^": 35, "man": 184, "maA": 23}
THREE = ["narrative", "legal_medinan", "eschatological_mufassal"]


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def gate():
    got = sha256(os.path.join(ROOT, PREREG))
    if got != PREREG_SHA:
        raise SystemExit(f"PREREG SHA MISMATCH\n expected {PREREG_SHA}\n got      {got}")
    for rel, want in FROZEN.items():
        got = sha256(os.path.join(ROOT, rel))
        if got != want:
            raise SystemExit(f"FROZEN INPUT SHA MISMATCH {rel}\n expected {want}\n got {got}")
    print("[gate] pre-reg + 4 frozen inputs verified")


def load_qac():
    """Return per-surah counts keyed by lemma-class. POS tag must be exactly COND."""
    path = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
    cond_total, lem_counts = 0, {}
    per_surah = {}          # surah -> {lemma: count}
    tokens_per_surah = {}   # QAC segment count T(s)
    for ln in open(path, encoding="utf-8", errors="replace"):
        if ln.startswith("#") or not ln.strip():
            continue
        p = ln.rstrip("\n").split("\t")
        if len(p) < 4:
            continue
        loc, form, tag, feats = p[0], p[1], p[2], p[3]
        try:
            surah = int(loc.strip("()").split(":")[0])
        except ValueError:
            continue
        tokens_per_surah[surah] = tokens_per_surah.get(surah, 0) + 1
        if tag != "COND":                       # EXACT tag match, no substring
            continue
        lem = None
        for f in feats.split("|"):
            if f.startswith("LEM:"):
                lem = f[4:]
        cond_total += 1
        lem_counts[lem] = lem_counts.get(lem, 0) + 1
        per_surah.setdefault(surah, {})
        per_surah[surah][lem] = per_surah[surah].get(lem, 0) + 1

    # MW-6 assertions 1 and 2
    if cond_total != EXPECT_COND_TOTAL:
        raise SystemExit(f"MW-6 FAIL: POS:COND total {cond_total} != {EXPECT_COND_TOTAL}")
    for lem, want in EXPECT_LEM.items():
        if lem_counts.get(lem, 0) != want:
            raise SystemExit(f"MW-6 FAIL: LEM {lem} = {lem_counts.get(lem,0)} != {want}")
    print(f"[MW-6] POS:COND total {cond_total}; lemma marginals reproduce exactly")
    return per_surah, tokens_per_surah, lem_counts


def load_labels():
    j = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2500.json")))
    labels = {int(k): v for k, v in j["genre_proxy"]["surah_genre"].items()}
    j30 = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2530.json")))
    want = j30["n_per_genre"]
    got = {}
    for v in labels.values():
        got[v] = got.get(v, 0) + 1
    if got != want:
        raise SystemExit(f"MW-6 FAIL: genre marginals {got} != h-new-2530 {want}")
    print(f"[MW-6] genre marginals reproduce h-new-2530 exactly: {want}")
    return labels, j30


def verse_counts():
    d = {}
    for ln in open(os.path.join(ROOT, "data/hafs-verse-counts.tsv")):
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        a, b = ln.split("\t")[:2]
        d[int(a)] = int(b)
    return d


# ---------- statistics ----------

def perm_p_diff(vals, labels, target, rng, nperm=NPERM, direction="greater"):
    """mean(target) - mean(rest); class-size-preserving label shuffle."""
    vals = np.asarray(vals, float)
    lab = np.asarray(labels)
    m = lab == target
    obs = vals[m].mean() - vals[~m].mean()
    idx = np.arange(len(vals))
    cnt = 0
    for _ in range(nperm):
        rng.shuffle(idx)
        sl = lab[idx]
        d = vals[sl == target].mean() - vals[sl != target].mean()
        if (direction == "greater" and d >= obs) or (direction == "less" and d <= obs):
            cnt += 1
    return float(obs), (cnt + 1) / (nperm + 1)


def perm_p_kw(vals, labels, rng, nperm=NPERM):
    vals = np.asarray(vals, float)
    lab = np.asarray(labels)
    groups = [vals[lab == c] for c in THREE]
    obs = stats.kruskal(*groups).statistic
    idx = np.arange(len(vals))
    cnt = 0
    for _ in range(nperm):
        rng.shuffle(idx)
        sl = lab[idx]
        h = stats.kruskal(*[vals[sl == c] for c in THREE]).statistic
        if h >= obs:
            cnt += 1
    return float(obs), (cnt + 1) / (nperm + 1)


def residualise(y, X):
    """OLS residuals of y on [1, X...]."""
    X = np.column_stack([np.ones(len(y))] + [np.asarray(c, float) for c in X])
    beta, *_ = np.linalg.lstsq(X, np.asarray(y, float), rcond=None)
    return np.asarray(y, float) - X @ beta


def loo_nearest_centroid(F, y):
    F = np.asarray(F, float); y = np.asarray(y)
    mu, sd = F.mean(0), F.std(0); sd[sd == 0] = 1.0
    Z = (F - mu) / sd
    pred = []
    for i in range(len(Z)):
        m = np.ones(len(Z), bool); m[i] = False
        cents = {c: Z[m & (y == c)].mean(0) for c in THREE}
        pred.append(min(cents, key=lambda c: np.linalg.norm(Z[i] - cents[c])))
    return np.array(pred)


def main():
    gate()
    per_surah, T, lem_counts = load_qac()
    labels, j2530 = load_labels()
    V = verse_counts()

    def counts(s, keys):
        return sum(per_surah.get(s, {}).get(k, 0) for k in keys)

    surahs3 = sorted([s for s in labels if labels[s] in THREE])
    y3 = np.array([labels[s] for s in surahs3])
    print(f"[data] 3-register N = {len(surahs3)}")

    out = {
        "id": "H-NEW-2630",
        "prereg_sha256": PREREG_SHA,
        "frozen_inputs": FROZEN,
        "seed_primary": SEED, "seed_replication": SEED_REP,
        "n_perm": NPERM, "bonferroni_k": K_BONF, "alpha_bonferroni": ALPHA_BONF,
        "lemma_marginals": lem_counts,
        "n_three_register": len(surahs3),
        "cells": {},
    }

    for tuple_name, realis_set, denom in [
        ("A_perVerse", REALIS, "V"),
        ("B_perToken", REALIS, "T"),
        ("C_wideRealis", REALIS_WIDE, "V"),
    ]:
        den = {s: (V[s] if denom == "V" else T[s]) for s in surahs3}
        nR = np.array([counts(s, realis_set) for s in surahs3], float)
        nI = np.array([counts(s, IRREALIS) for s in surahs3], float)
        dR = nR / np.array([den[s] for s in surahs3], float)
        dI = nI / np.array([den[s] for s in surahs3], float)

        rng = np.random.default_rng(SEED)
        h1_obs, h1_p = perm_p_diff(dR, y3, "legal_medinan", rng, direction="greater")
        rng = np.random.default_rng(SEED)
        h2_obs, h2_p = perm_p_diff(dI, y3, "legal_medinan", rng, direction="less")

        # C(s): defined only where nR+nI >= 1
        defined = (nR + nI) >= 1
        C = (nR[defined] - nI[defined]) / (nR[defined] + nI[defined])
        yC = y3[defined]
        sC = [surahs3[i] for i in range(len(surahs3)) if defined[i]]
        rng = np.random.default_rng(SEED)
        h3_H, h3_p = perm_p_kw(C, yC, rng)
        meansC = {c: float(C[yC == c].mean()) for c in THREE}
        h3_order_ok = meansC["legal_medinan"] == max(meansC.values())

        # H4 — length-residualised C on log V and log T
        lv = np.log([V[s] for s in sC]); lt = np.log([T[s] for s in sC])
        Cres = residualise(C, [lv, lt])
        rng = np.random.default_rng(SEED)
        h4_H, h4_p = perm_p_kw(Cres, yC, rng)
        meansCres = {c: float(Cres[yC == c].mean()) for c in THREE}
        h4_order_ok = meansCres["legal_medinan"] == max(meansCres.values())

        cell = {
            "denominator": denom, "realis_set": sorted(realis_set),
            "n_defined_C": int(defined.sum()),
            "mean_dR_by_register": {c: float(dR[y3 == c].mean()) for c in THREE},
            "mean_dI_by_register": {c: float(dI[y3 == c].mean()) for c in THREE},
            "H1_realis_legal_vs_rest": {"obs_diff": h1_obs, "p": h1_p,
                                        "pass": bool(h1_obs > 0 and h1_p < ALPHA_BONF)},
            "H2_irrealis_legal_vs_rest": {"obs_diff": h2_obs, "p": h2_p,
                                          "pass": bool(h2_obs < 0 and h2_p < ALPHA_BONF)},
            "H3_balance_KW": {"H": h3_H, "p": h3_p, "means": meansC,
                              "legal_highest": bool(h3_order_ok),
                              "pass": bool(h3_p < ALPHA_BONF and h3_order_ok)},
            "H4_length_residualised_KW": {"H": h4_H, "p": h4_p, "means": meansCres,
                                          "legal_highest": bool(h4_order_ok),
                                          "pass": bool(h4_p < ALPHA_BONF and h4_order_ok)},
        }
        out["cells"][tuple_name] = cell
        print(f"\n=== tuple {tuple_name} (denominator {denom}) ===")
        print(f"  mean d_R  {cell['mean_dR_by_register']}")
        print(f"  mean d_I  {cell['mean_dI_by_register']}")
        print(f"  H1 diff={h1_obs:+.6f} p={h1_p:.5f} pass={cell['H1_realis_legal_vs_rest']['pass']}")
        print(f"  H2 diff={h2_obs:+.6f} p={h2_p:.5f} pass={cell['H2_irrealis_legal_vs_rest']['pass']}")
        print(f"  H3 H={h3_H:.4f} p={h3_p:.5f} means={ {k:round(v,4) for k,v in meansC.items()} } legal_highest={h3_order_ok}")
        print(f"  H4 H={h4_H:.4f} p={h4_p:.5f} means={ {k:round(v,4) for k,v in meansCres.items()} } legal_highest={h4_order_ok}")

    # ---- MW-6 substantive control: generalising conditionals ----
    nG = np.array([counts(s, GENERALISING) for s in surahs3], float)
    nR = np.array([counts(s, REALIS) for s in surahs3], float)
    nI = np.array([counts(s, IRREALIS) for s in surahs3], float)
    defG = (nG + nR + nI) >= 1
    Cg = (nG[defG] - (nR + nI)[defG]) / (nG + nR + nI)[defG]
    rng = np.random.default_rng(SEED)
    g_H, g_p = perm_p_kw(Cg, y3[defG], rng)
    dG = nG / np.array([V[s] for s in surahs3], float)
    rng = np.random.default_rng(SEED)
    gd_obs, gd_p = perm_p_diff(dG, y3, "legal_medinan", rng, direction="greater")
    out["MW6_generalising_control"] = {
        "note": "man/maA generalising conditionals; if these separate as strongly, the axis is not MOOD",
        "KW_H": g_H, "KW_p": g_p,
        "density_legal_vs_rest_diff": gd_obs, "density_p": gd_p}
    print(f"\n[MW-6 control] generalising man/maA: KW H={g_H:.4f} p={g_p:.5f}; "
          f"density diff={gd_obs:+.6f} p={gd_p:.5f}")

    # ---- MW-5 replication at seed 20260519 (tuple A, H3+H4) ----
    den = {s: V[s] for s in surahs3}
    nR = np.array([counts(s, REALIS) for s in surahs3], float)
    nI = np.array([counts(s, IRREALIS) for s in surahs3], float)
    defined = (nR + nI) >= 1
    C = (nR[defined] - nI[defined]) / (nR[defined] + nI[defined])
    yC = y3[defined]; sC = [surahs3[i] for i in range(len(surahs3)) if defined[i]]
    rng = np.random.default_rng(SEED_REP)
    r3_H, r3_p = perm_p_kw(C, yC, rng)
    Cres = residualise(C, [np.log([V[s] for s in sC]), np.log([T[s] for s in sC])])
    rng = np.random.default_rng(SEED_REP)
    r4_H, r4_p = perm_p_kw(Cres, yC, rng)
    out["MW5_replication_seed20260519"] = {"H3_H": r3_H, "H3_p": r3_p,
                                           "H4_H": r4_H, "H4_p": r4_p}
    print(f"[MW-5] replication seed {SEED_REP}: H3 p={r3_p:.5f}  H4 p={r4_p:.5f}")

    # ---- H5 — classifier with and without the conditional feature ----
    rv = j2530["raw_feature_vectors"]
    feats6 = j2530["features"]
    F6 = np.array([[rv[str(s)][f] for f in feats6] for s in surahs3], float)
    # conditional feature: C(s), with undefined -> 0.0 (no conditional => no lean)
    Cfull = np.zeros(len(surahs3))
    Cfull[defined] = C
    F7 = np.column_stack([F6, Cfull])

    res = {}
    for name, F in (("six_feature_baseline", F6), ("seven_with_conditional", F7)):
        pred = loo_nearest_centroid(F, y3)
        acc = float((pred == y3).mean())
        legal_recall = int(((y3 == "legal_medinan") & (pred == "legal_medinan")).sum())
        conf = {a: {b: int(((y3 == a) & (pred == b)).sum()) for b in THREE} for a in THREE}
        res[name] = {"loo_acc": acc, "legal_recall_of_20": legal_recall, "confusion": conf}
        print(f"[H5] {name}: LOO acc={acc:.4f}  legal recall={legal_recall}/20")

    base = res["six_feature_baseline"]["legal_recall_of_20"]
    new = res["seven_with_conditional"]["legal_recall_of_20"]
    # permutation null on the IMPROVEMENT: shuffle the conditional feature across surahs
    rng = np.random.default_rng(SEED)
    obs_gain = new - base
    cnt = 0
    Cperm = Cfull.copy()
    for _ in range(NPERM):
        rng.shuffle(Cperm)
        p = loo_nearest_centroid(np.column_stack([F6, Cperm]), y3)
        g = int(((y3 == "legal_medinan") & (p == "legal_medinan")).sum()) - base
        if g >= obs_gain:
            cnt += 1
    h5_p = (cnt + 1) / (NPERM + 1)
    out["H5_classifier"] = {**res, "baseline_legal_recall": base,
                            "new_legal_recall": new, "gain": int(obs_gain),
                            "p_feature_shuffle": h5_p,
                            "pass": bool(obs_gain > 0 and h5_p < ALPHA_BONF)}
    print(f"[H5] gain={obs_gain:+d} legal-recall, p={h5_p:.5f}, "
          f"pass={out['H5_classifier']['pass']}")

    # ---- write immutable run dir ----
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rd = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-2630", ts)
    os.makedirs(rd, exist_ok=True)
    json.dump(out, open(os.path.join(rd, "result.json"), "w"), indent=2, ensure_ascii=False)
    manifest = {
        "id": "H-NEW-2630", "utc": ts,
        "prereg": PREREG, "prereg_sha256": PREREG_SHA,
        "script_relpath": "findings/phase-b-hypotheses/scripts/h-new-2630.py",
        "frozen_inputs": FROZEN,
        "seed_primary": SEED, "seed_replication": SEED_REP,
        "n_perm": NPERM, "bonferroni_k": K_BONF, "alpha_bonferroni": ALPHA_BONF,
        "python": sys.version.split()[0],
        "numpy": np.__version__, "scipy": stats.__name__ and __import__("scipy").__version__,
    }
    json.dump(manifest, open(os.path.join(rd, "manifest.json"), "w"), indent=2)
    json.dump(out, open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2630.json"), "w"),
              indent=2, ensure_ascii=False)
    print(f"\n[run] {os.path.relpath(rd, ROOT)}")


if __name__ == "__main__":
    main()
