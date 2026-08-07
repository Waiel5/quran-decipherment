#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2640 — POST-HOC SUPPLEMENT. NOT PRE-REGISTERED.

Every number produced here is descriptive, MW-7-capped at single-test α = 0.05, and
carries NO Bonferroni standing. It exists to answer one fair objection to the registered
NULL, and it was written to be reported whatever it returned.

The objection: the primary test fed the classifier the LENGTH-RESIDUALISED modality
indices. The residualisation is on [log n_verses, mean words/verse], and mean verse
length is itself a known register signature (H-NEW-770 verse-length compression-tail).
So the control could have removed the effect along with the confound, and the registered
I3 (Δ_LOO = −0.088) might be an artefact of that choice rather than evidence that
modality carries no register information.

Three diagnostics:
  P1. The same eight-feature classifier on RAW (un-residualised) D and E.
  P2. Collinearity of D and E with the two length covariates (R² of the OLS fit).
  P3. Face-validity of the deontic index — its ten highest-density surahs.

Reads the same frozen inputs, verified by SHA-256. Writes to its OWN immutable run
directory; the primary run directory is never touched.

Author: Waiel Al-Shujaa.
"""
import json, math, os, sys, datetime, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CSV = os.path.join(ROOT, "csv")

# Re-use the primary script wholesale: it re-verifies every SHA and rebuilds every index
# from the frozen inputs. Its own run-directory write is harmless (a second immutable
# directory, retained per prereg §8).
spec = importlib.util.spec_from_file_location("h2640", os.path.join(HERE, "h-new-2640.py"))
M = importlib.util.module_from_spec(spec)
_stdout = sys.stdout
sys.stdout = open(os.devnull, "w")
spec.loader.exec_module(M)
sys.stdout.close()
sys.stdout = _stdout

S91, LAB91, THREE = M.S91, M.LAB91, M.THREE
print(f"[posthoc] primary module loaded; N={len(S91)}, LOO6={M.acc6:.5f}")
print("[posthoc] NOT PRE-REGISTERED — descriptive only, MW-7 cap α=0.05, no Bonferroni standing\n")

dens_D = M.density(M.cnt_D_T1, "word")
dens_E = M.density(M.cnt_E_T1, "word")

# --- P1: classifier on RAW (un-residualised) D and E ------------------------
zD_raw = M.zcol([dens_D[s] for s in S91])
zE_raw = M.zcol([dens_E[s] for s in S91])
Z8raw = [M.Z6[i] + [zD_raw[i], zE_raw[i]] for i in range(len(S91))]
acc8raw, conf8raw = M.loo_exact(Z8raw, LAB91)

# and each index alone, on top of the six
res_single = {}
for nm, zc in (("D_raw_only", zD_raw), ("E_raw_only", zE_raw)):
    Z7 = [M.Z6[i] + [zc[i]] for i in range(len(S91))]
    a7, c7 = M.loo_exact(Z7, LAB91)
    res_single[nm] = {"loo": round(a7, 5), "delta": round(a7 - M.acc6, 5),
                      "legal_recall": c7["legal_medinan"]["legal_medinan"]}

print("P1 — classifier with RAW (un-residualised) modality features")
print(f"   six-feature baseline (H-NEW-2530)  LOO = {M.acc6:.5f}   legal recall {M.LEGAL_RECALL_6}/20")
print(f"   + raw D and raw E                  LOO = {acc8raw:.5f}   "
      f"Δ = {acc8raw - M.acc6:+.5f}   legal recall {conf8raw['legal_medinan']['legal_medinan']}/20")
for nm, r in res_single.items():
    print(f"   + {nm:<16}               LOO = {r['loo']:.5f}   Δ = {r['delta']:+.5f}   "
          f"legal recall {r['legal_recall']}/20")
print(f"   registered (residualised) comparison: Δ = {M.RESULTS['T1_primary']['delta_loo']:+.5f}")

# --- P2: how much of each index IS length? ---------------------------------
def r2(dens):
    y = [dens[s] for s in S91]
    resid, beta = M.residualise(dens)
    m = sum(y) / len(y)
    sst = sum((v - m) ** 2 for v in y)
    sse = sum(resid[s] ** 2 for s in S91)
    return 1.0 - sse / sst, beta

r2D, bD = r2(dens_D)
r2E, bE = r2(dens_E)
r2J, bJ = r2(M.density(M.cnt_J, "word"))
print(f"\nP2 — variance absorbed by the two length covariates [log n_verses, mean words/verse]")
print(f"   D (deontic)   R² = {r2D:.4f}   β = {[round(b,4) for b in bD]}")
print(f"   E (epistemic) R² = {r2E:.4f}   β = {[round(b,4) for b in bE]}")
print(f"   J (raw JUS)   R² = {r2J:.4f}   β = {[round(b,4) for b in bJ]}")

# --- P4: pooled token-weighted rates — is this a null effect, or a null instrument?
# The registered statistic is an UNWEIGHTED mean over per-surah densities. Surah size
# spans 10 to 6116 word-tokens, so a 10-word surah with two imperatives contributes a
# density of 200/1000 with the same weight as al-Baqara. Pooling over tokens removes
# that. Descriptive, MW-7 capped, no inferential standing.
import random as _rnd

def pooled(cnt):
    out = {}
    for c in THREE:
        ss = [s for s in S91 if M.GENRE[s] == c]
        out[c] = 1000.0 * sum(cnt[s] for s in ss) / sum(M.NW[s] for s in ss)
    return out

def pooled_spread(cnt, labels):
    """max-min pooled rate across the three registers, for a permutation test."""
    tot = {c: [0, 0] for c in THREE}
    for i, s in enumerate(S91):
        t = tot[labels[i]]
        t[0] += cnt[s]
        t[1] += M.NW[s]
    r = [1000.0 * t[0] / t[1] for t in tot.values()]
    return max(r) - min(r)

print("\nP4 — POOLED (token-weighted) rates per 1000 word-tokens, and their argmax")
p4 = {}
for nm, cnt in (("D_deontic", M.cnt_D_T1), ("E_epistemic", M.cnt_E_T1),
                ("J_rawJUS", M.cnt_J), ("N_lam", M.cnt_Nlam),
                ("C_cond_jussive", M.cnt_Ccond)):
    pr = pooled(cnt)
    obs = max(pr.values()) - min(pr.values())
    rng = _rnd.Random(M.SEED)
    ge = 0
    for _ in range(M.N_PERM):
        pl = LAB91[:]
        rng.shuffle(pl)
        if pooled_spread(cnt, pl) >= obs:
            ge += 1
    p = (ge + 1) / (M.N_PERM + 1)
    am = max(pr, key=pr.get)
    p4[nm] = {"pooled": {k: round(v, 3) for k, v in pr.items()}, "argmax": am,
              "spread": round(obs, 3), "perm_p_descriptive": round(p, 6)}
    print(f"   {nm:<12} " + "  ".join(f"{c[:12]}={pr[c]:7.3f}" for c in THREE) +
          f"   argmax={am:<24} spread={obs:6.3f}  p={p:.5f}")
print("   (locked directions were: D -> legal_medinan, E -> eschatological_mufassal)")

nsmall = sum(1 for s in S91 if M.NW[s] < 50)
print(f"\nP5 — instrument reliability: {nsmall}/{len(S91)} surahs have < 50 word-tokens; "
      f"corpus range {min(M.NW[s] for s in S91)}–{max(M.NW[s] for s in S91)} tokens")

# --- P3: face validity of the deontic index --------------------------------
top = sorted(S91, key=lambda s: -dens_D[s])[:10]
bot = sorted(S91, key=lambda s: dens_D[s])[:5]
print("\nP3 — deontic index face validity (raw density per 1000 word-tokens)")
print("   highest:")
for s in top:
    print(f"     Q{s:<4} {dens_D[s]:7.2f}   {M.GENRE[s]:<26} "
          f"D={M.cnt_D_T1[s]:4d}  words={M.NW[s]:5d}")
print("   lowest:")
for s in bot:
    print(f"     Q{s:<4} {dens_D[s]:7.2f}   {M.GENRE[s]:<26} "
          f"D={M.cnt_D_T1[s]:4d}  words={M.NW[s]:5d}")

# --- emit -------------------------------------------------------------------
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join(ROOT, "runs", "h-new-2640", f"{stamp}-posthoc")
if os.path.exists(RUNDIR):
    raise SystemExit(f"[FATAL] run directory exists (immutability): {RUNDIR}")
os.makedirs(RUNDIR)
out = {
    "id": "H-NEW-2640-POSTHOC",
    "status": "NOT PRE-REGISTERED — descriptive, MW-7 capped at single-test alpha=0.05, "
              "no Bonferroni standing, no verdict authority",
    "prereg_sha256_of_primary": M.PREREG_SHA256,
    "P1_raw_feature_classifier": {
        "loo6_baseline": round(M.acc6, 5), "legal_recall_6": M.LEGAL_RECALL_6,
        "loo8_raw_DE": round(acc8raw, 5), "delta_raw": round(acc8raw - M.acc6, 5),
        "legal_recall_8_raw": conf8raw["legal_medinan"]["legal_medinan"],
        "confusion8_raw": conf8raw,
        "single_feature": res_single,
        "registered_residualised_delta": M.RESULTS["T1_primary"]["delta_loo"]},
    "P2_length_collinearity_R2": {"D": round(r2D, 4), "E": round(r2E, 4), "J_rawJUS": round(r2J, 4)},
    "P4_pooled_token_weighted": p4,
    "P5_instrument_reliability": {"surahs_under_50_tokens": nsmall, "n": len(S91),
                                  "token_range": [min(M.NW[s] for s in S91),
                                                  max(M.NW[s] for s in S91)]},
    "P3_deontic_top10": [{"surah": s, "density": round(dens_D[s], 3),
                          "register": M.GENRE[s], "count": M.cnt_D_T1[s]} for s in top],
    "P3_deontic_bottom5": [{"surah": s, "density": round(dens_D[s], 3),
                            "register": M.GENRE[s], "count": M.cnt_D_T1[s]} for s in bot],
}
with open(os.path.join(RUNDIR, "result.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
with open(os.path.join(RUNDIR, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump({"id": "H-NEW-2640-POSTHOC", "utc": stamp,
               "script_sha256": M.sha256_file(os.path.abspath(__file__)),
               "prereg_sha256_of_primary": M.PREREG_SHA256,
               "inputs_sha256": {os.path.relpath(p, M.REPO): M.FROZEN[p] for p in M.FROZEN},
               "status": "post-hoc supplement, no verdict authority",
               "immutability": "Immutable. Never delete or overwrite, per prereg §8."},
              f, ensure_ascii=False, indent=2)
with open(os.path.join(CSV, "h-new-2640-posthoc.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\n[run] {RUNDIR}")
