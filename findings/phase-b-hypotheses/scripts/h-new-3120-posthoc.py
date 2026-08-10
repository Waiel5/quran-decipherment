#!/usr/bin/env python3
"""
H-NEW-3120 POST-HOC — corrected power audit for the NULL.

NOT pre-registered. Runs to its OWN run directory. The locked run
(runs/h-new-3120/20260809T090141Z) is untouched and retained.

WHY THIS EXISTS. The locked run's MDE routine generated synthetic datasets by permuting the
density vector GLOBALLY before adding the effect. That destroys the association between density
and the stratifying variable (mean verse length), so the synthetic null is tighter than the real
one and the MDE comes out optimistic -- visibly so: it returned MDE 0.0351 < observed 0.0363 <
critical 0.0457, which cannot all be true of one design. A shift alternative that is smaller than
the observed effect cannot have 80% power in a test the observed effect failed.

THE FIX. Synthetic datasets are now built by permuting density WITHIN the same strata the test
uses, which preserves the density-by-stratum structure, then adding the shift. Everything else is
identical to the locked routine.
"""

import hashlib, json, os, csv, datetime
import numpy as np

ROOT = "/Users/grey/Downloads/quran"
LOCKED = os.path.join(ROOT, "findings/phase-b-hypotheses/scripts/h-new-3120.py")
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-3120-asbab-chronology.md")
EXPECTED_PREREG_SHA = "bede8fc660467763a26e1068ec2d0a3dce044491c1da9c1f6718837210539caa"
LOCKED_RUN = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-3120/20260809T090141Z/result.json")
SEED = 20260509
ALPHA = 0.025
PHASE_ORD = {"Early Meccan": 0, "Middle Meccan": 1, "Late Meccan": 2, "Medinan": 3}


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


if sha256(PREREG) != EXPECTED_PREREG_SHA:
    raise SystemExit("PREREG SHA MISMATCH — refusing to run")

import importlib.util
spec = importlib.util.spec_from_file_location("locked", LOCKED)
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)


def power_curve(d, b, strata, deltas, rng_seed, nperm=4000, nsim=600):
    """
    Power at each delta. Synthetic data preserves the density-by-stratum structure by
    permuting WITHIN strata (the locked routine permuted globally -- that was the bug).
    """
    d = np.asarray(d, float); b = np.asarray(b, bool); n = len(d)
    rng = np.random.default_rng(rng_seed)
    P = np.empty((nperm, n), dtype=bool)
    for i in range(nperm):
        P[i] = L.permute_within(b.astype(int), strata, rng).astype(bool)
    kk = P.sum(axis=1).astype(float); kk[kk == 0] = np.nan
    nk = (n - P.sum(axis=1)).astype(float); nk[nk == 0] = np.nan
    out = {}
    for delta in deltas:
        hits = 0
        for _ in range(nsim):
            ds = np.empty(n)
            for st in np.unique(strata):                 # <-- WITHIN-STRATUM resample
                idx = np.where(strata == st)[0]
                ds[idx] = rng.permutation(d[idx])
            ds = ds + delta * b
            obs = ds[b].mean() - ds[~b].mean()
            s1 = P @ ds
            nulls = s1 / kk - (ds.sum() - s1) / nk
            if obs > np.nanquantile(nulls, 1 - ALPHA):
                hits += 1
        out[float(delta)] = hits / nsim
    return out


def mde_from_curve(curve):
    ds = sorted(curve)
    for x in ds:
        if curve[x] >= 0.80:
            return x
    return None


def main():
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rd = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-3120-posthoc", stamp)
    os.makedirs(rd, exist_ok=False)

    locked = json.load(open(LOCKED_RUN))
    nv, wc, mvl = L.load_corpus(); per = L.load_chronology(); idh, toks = L.load_idh()
    S = list(range(1, 115))
    d = np.array([idh[s] / nv[s] for s in S])
    b = np.array([1 if per[s]["noldeke_phase"] == "Medinan" else 0 for s in S])

    res = {"NOT_PREREGISTERED": True, "utc": stamp, "locked_run": LOCKED_RUN,
           "prereg_sha256": EXPECTED_PREREG_SHA, "seed": SEED, "alpha": ALPHA}

    # ---- full corpus, at the worst channel that governed H1 (L3 mean verse length quintile)
    w1 = locked["R1_noldeke"]["H1_worst"]["setting"]
    obs1 = locked["R1_noldeke"]["H1_worst"]["obs"]
    crit1 = locked["R1_noldeke"]["H1_step"][w1]["crit_value"]
    st1 = L.make_strata([mvl[s] for s in S], 5 if "quintile" in w1 else 10)
    grid = [round(x, 4) for x in np.arange(0.0, 0.161, 0.005)]
    c1 = power_curve(d, b, st1, grid, SEED)
    srt = np.sort(d); k = int(b.sum())
    smax1 = float(srt[::-1][:k].mean() - srt[: len(d) - k].mean())
    res["H1_full_corpus"] = {
        "worst_setting": w1, "observed": obs1, "critical_value": crit1,
        "s_max_attainable": smax1, "untestable": bool(smax1 <= crit1),
        "obs_over_crit": obs1 / crit1,
        "power_curve": c1, "MDE_80": mde_from_curve(c1),
        "power_at_observed_effect": c1.get(round(round(obs1 / 0.005) * 0.005, 4)),
    }

    # ---- Meccan-internal (S2), at the channel that governed H1m
    M = [s for s in S if per[s]["noldeke_phase"] != "Medinan"]
    dm = np.array([idh[s] / nv[s] for s in M])
    bm = np.array([1 if per[s]["noldeke_phase"] == "Late Meccan" else 0 for s in M])
    wm1 = locked["meccan_internal"]["H1m_worst"]["setting"]
    obsm = locked["meccan_internal"]["H1m_worst"]["obs"]
    critm = locked["meccan_internal"]["H1m_step_late_vs_earlymid"][wm1]["crit_value"]
    stm = L.make_strata([mvl[s] for s in M], 5 if "quintile" in wm1 else 10)
    cm = power_curve(dm, bm, stm, grid, SEED)
    srtm = np.sort(dm); km = int(bm.sum())
    smaxm = float(srtm[::-1][:km].mean() - srtm[: len(dm) - km].mean())
    res["H1m_meccan_internal"] = {
        "worst_setting": wm1, "observed": obsm, "critical_value": critm,
        "s_max_attainable": smaxm, "untestable": bool(smaxm <= critm),
        "obs_over_crit": obsm / critm, "n_surahs": len(M),
        "power_curve": cm, "MDE_80": mde_from_curve(cm),
    }

    # ---- context: how large is the corpus-level effect this design failed to find?
    res["context"] = {
        "corpus_effect_L0_would_have_been_significant_at": locked["R1_noldeke"]["H1_step"]["L0 unstratified"]["p"],
        "swing_H1_L0_to_worst": locked["R1_noldeke"]["H1_worst"]["p"] / locked["R1_noldeke"]["H1_step"]["L0 unstratified"]["p"],
        "swing_H2_L0_to_worst": locked["R1_noldeke"]["H2_worst"]["p"] / locked["R1_noldeke"]["H2_gradient"]["L0 unstratified"]["p"],
    }

    with open(os.path.join(rd, "result.json"), "x", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
    with open(os.path.join(rd, "manifest.txt"), "x", encoding="utf-8") as f:
        f.write(f"H-NEW-3120 POST-HOC power audit {stamp}\nNOT PRE-REGISTERED\n")
        f.write(f"locked run retained at {LOCKED_RUN}\n")
        f.write(f"script sha256 {sha256(os.path.abspath(__file__))}\n")

    print("run_dir", rd)
    for key in ("H1_full_corpus", "H1m_meccan_internal"):
        v = res[key]
        print(f"\n{key}  ({v['worst_setting']})")
        print(f"  observed {v['observed']:+.5f}   crit {v['critical_value']:.5f}   "
              f"s_max {v['s_max_attainable']:.5f}   obs/crit {v['obs_over_crit']:.3f}")
        print(f"  UNTESTABLE branch fired: {v['untestable']}")
        print(f"  MDE at 80% power: {v['MDE_80']}")
    print("\ncontext:", res["context"])


if __name__ == "__main__":
    main()
