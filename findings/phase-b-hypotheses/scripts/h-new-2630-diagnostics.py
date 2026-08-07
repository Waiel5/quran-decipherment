#!/usr/bin/env python3
"""
H-NEW-2630 DIAGNOSTICS — post-hoc, MW-7 capped at alpha=0.05 single-test.
EXPLORATORY. Not a registered inference; no cell here may be promoted.

Question forced by the primary run: H5 improved legal-Medinan LOO recall
8/20 -> 16/20 by adding the conditional-mood balance C(s). But H2 reversed,
H3 failed, H4 failed under length control, and the MW-6 generalising control
fired. So is the H5 gain about conditional MOOD, or merely about conditional
PRESENCE / DENSITY (which would make it a length/genre proxy)?

Writes to an ADDITIONAL run directory. The primary run directory is retained.

Waiel Al-Shujaa, 2026-08-07.
"""
import json, hashlib, os, sys, datetime
import numpy as np
from scipy import stats

ROOT = "/Users/grey/Downloads/quran"
PREREG = "findings/phase-b-hypotheses/prereg-h-new-2630-conditional-register.md"
PREREG_SHA = "40f899a4bdb807d3ac39c679c532b51ab90fe7f020f4c01b4bd0dcd1281a2a5a"
QAC = "data/morphology/quranic-corpus-morphology-0.4.txt"
QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"

SEED, NPERM = 20260509, 10000
REALIS = {"<in"}
IRREALIS = {"law", "lawolaA^"}
GENERALISING = {"man", "maA", "{l~a*iY", ">am~aA", ">ayon", "Hayov2", "mahomaA", ">aY~"}
THREE = ["narrative", "legal_medinan", "eschatological_mufassal"]


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def gate():
    for rel, want in ((PREREG, PREREG_SHA), (QAC, QAC_SHA)):
        got = sha256(os.path.join(ROOT, rel))
        if got != want:
            raise SystemExit(f"SHA MISMATCH {rel}: {got} != {want}")
    print("[gate] pre-reg + QAC verified")


def load():
    per, T = {}, {}
    for ln in open(os.path.join(ROOT, QAC), encoding="utf-8", errors="replace"):
        if ln.startswith("#") or not ln.strip():
            continue
        p = ln.rstrip("\n").split("\t")
        if len(p) < 4:
            continue
        loc, tag, feats = p[0], p[2], p[3]
        try:
            s = int(loc.strip("()").split(":")[0])
        except ValueError:
            continue
        T[s] = T.get(s, 0) + 1
        if tag != "COND":
            continue
        lem = next((f[4:] for f in feats.split("|") if f.startswith("LEM:")), None)
        per.setdefault(s, {})
        per[s][lem] = per[s].get(lem, 0) + 1
    lab = {int(k): v for k, v in json.load(
        open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2500.json"))
    )["genre_proxy"]["surah_genre"].items()}
    V = {}
    for ln in open(os.path.join(ROOT, "data/hafs-verse-counts.tsv")):
        if ln.strip() and not ln.startswith("#"):
            a, b = ln.split("\t")[:2]
            V[int(a)] = int(b)
    return per, T, lab, V


def loo(F, y):
    F = np.asarray(F, float)
    mu, sd = F.mean(0), F.std(0); sd[sd == 0] = 1.0
    Z = (F - mu) / sd
    out = []
    for i in range(len(Z)):
        m = np.ones(len(Z), bool); m[i] = False
        cents = {c: Z[m & (y == c)].mean(0) for c in THREE}
        out.append(min(cents, key=lambda c: np.linalg.norm(Z[i] - cents[c])))
    return np.array(out)


def main():
    gate()
    per, T, lab, V = load()
    S = sorted([s for s in lab if lab[s] in THREE])
    y = np.array([lab[s] for s in S])
    j = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2530.json")))
    F6 = np.array([[j["raw_feature_vectors"][str(s)][f] for f in j["features"]] for s in S], float)

    def cnt(s, keys):
        return sum(per.get(s, {}).get(k, 0) for k in keys)

    nR = np.array([cnt(s, REALIS) for s in S], float)
    nI = np.array([cnt(s, IRREALIS) for s in S], float)
    nG = np.array([cnt(s, GENERALISING) for s in S], float)
    Vv = np.array([V[s] for s in S], float)

    defined = (nR + nI) >= 1
    C = np.zeros(len(S))
    C[defined] = (nR[defined] - nI[defined]) / (nR[defined] + nI[defined])

    variants = {
        "0_baseline_six":        None,
        "1_mood_balance_C":      C,                                  # the H5 feature
        "2_has_any_conditional": defined.astype(float),              # presence only
        "3_total_cond_density":  (nR + nI) / Vv,                     # mood-BLIND density
        "4_realis_density_only": nR / Vv,
        "5_irrealis_density_only": nI / Vv,
        "6_generalising_density": nG / Vv,                           # excluded family
        "7_all_cond_density":    (nR + nI + nG) / Vv,                # every COND lemma
        "8_log_verse_count":     np.log(Vv),                         # pure length control
    }

    base_pred = loo(F6, y)
    base_recall = int(((y == "legal_medinan") & (base_pred == "legal_medinan")).sum())
    base_acc = float((base_pred == y).mean())
    print(f"[baseline] LOO acc={base_acc:.4f} legal recall={base_recall}/20\n")

    res = {}
    for name, col in variants.items():
        if col is None:
            res[name] = {"loo_acc": base_acc, "legal_recall": base_recall, "gain": 0}
            continue
        F = np.column_stack([F6, col])
        pred = loo(F, y)
        acc = float((pred == y).mean())
        rec = int(((y == "legal_medinan") & (pred == "legal_medinan")).sum())
        # feature-shuffle null on the gain (MW-7 capped, alpha=0.05)
        rng = np.random.default_rng(SEED)
        c2 = np.asarray(col, float).copy()
        obs = rec - base_recall
        hit = 0
        for _ in range(NPERM):
            rng.shuffle(c2)
            p = loo(np.column_stack([F6, c2]), y)
            g = int(((y == "legal_medinan") & (p == "legal_medinan")).sum()) - base_recall
            if g >= obs:
                hit += 1
        pv = (hit + 1) / (NPERM + 1)
        res[name] = {"loo_acc": acc, "legal_recall": rec, "gain": int(obs), "p_shuffle": pv}
        print(f"  {name:26} acc={acc:.4f}  legal={rec:2d}/20  gain={obs:+d}  p={pv:.5f}")

    # correlation of C with length, and of C with the mood contrast
    rho_CV = stats.spearmanr(C, Vv)
    rho_defV = stats.spearmanr(defined.astype(float), Vv)
    print(f"\n[assoc] Spearman C(s) vs verse-count: rho={rho_CV.statistic:+.4f} p={rho_CV.pvalue:.2e}")
    print(f"[assoc] Spearman has-conditional vs verse-count: rho={rho_defV.statistic:+.4f} p={rho_defV.pvalue:.2e}")
    n_undef = int((~defined).sum())
    undef_by_reg = {c: int(((~defined) & (y == c)).sum()) for c in THREE}
    print(f"[assoc] surahs with NO realis/irrealis conditional: {n_undef} of {len(S)}  by register {undef_by_reg}")

    # length-residualised d_R / d_I (MW-1 reporting requirement)
    def resid(v):
        X = np.column_stack([np.ones(len(v)), np.log(Vv), np.log([T[s] for s in S])])
        b, *_ = np.linalg.lstsq(X, v, rcond=None)
        return v - X @ b
    dR_res, dI_res = resid(nR / Vv), resid(nI / Vv)
    mr = {c: float(dR_res[y == c].mean()) for c in THREE}
    mi = {c: float(dI_res[y == c].mean()) for c in THREE}
    print(f"[MW-1] length-residualised mean d_R by register: { {k: round(v,5) for k,v in mr.items()} }")
    print(f"[MW-1] length-residualised mean d_I by register: { {k: round(v,5) for k,v in mi.items()} }")
    rng = np.random.default_rng(SEED)
    lab3 = y.copy(); idx = np.arange(len(y))
    obsR = dR_res[y == "legal_medinan"].mean() - dR_res[y != "legal_medinan"].mean()
    hit = 0
    for _ in range(NPERM):
        rng.shuffle(idx); sl = lab3[idx]
        if dR_res[sl == "legal_medinan"].mean() - dR_res[sl != "legal_medinan"].mean() >= obsR:
            hit += 1
    pR = (hit + 1) / (NPERM + 1)
    print(f"[MW-1] H1 re-run on length-residualised d_R: diff={obsR:+.6f} p={pR:.5f}")

    out = {"id": "H-NEW-2630-DIAGNOSTICS", "status": "EXPLORATORY (MW-7 capped, alpha=0.05)",
           "prereg_sha256": PREREG_SHA, "seed": SEED, "n_perm": NPERM,
           "baseline": {"loo_acc": base_acc, "legal_recall": base_recall},
           "variants": res,
           "spearman_C_vs_versecount": {"rho": float(rho_CV.statistic), "p": float(rho_CV.pvalue)},
           "spearman_hasCond_vs_versecount": {"rho": float(rho_defV.statistic), "p": float(rho_defV.pvalue)},
           "n_undefined_C": n_undef, "undefined_by_register": undef_by_reg,
           "length_residualised_dR_means": mr, "length_residualised_dI_means": mi,
           "H1_length_residualised": {"diff": float(obsR), "p": pR}}

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rd = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-2630", ts + "-diagnostics")
    os.makedirs(rd, exist_ok=True)
    json.dump(out, open(os.path.join(rd, "result.json"), "w"), indent=2, ensure_ascii=False)
    json.dump({"id": "H-NEW-2630-DIAGNOSTICS", "utc": ts,
               "status": "EXPLORATORY post-hoc, MW-7 capped; primary run retained separately",
               "prereg": PREREG, "prereg_sha256": PREREG_SHA,
               "script_relpath": "findings/phase-b-hypotheses/scripts/h-new-2630-diagnostics.py",
               "frozen_inputs": {QAC: QAC_SHA},
               "seed": SEED, "n_perm": NPERM,
               "python": sys.version.split()[0], "numpy": np.__version__},
              open(os.path.join(rd, "manifest.json"), "w"), indent=2)
    print(f"\n[run] {os.path.relpath(rd, ROOT)}")


if __name__ == "__main__":
    main()
