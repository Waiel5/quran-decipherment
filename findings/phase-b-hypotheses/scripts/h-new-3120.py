#!/usr/bin/env python3
"""
H-NEW-3120 — F-12 asbab-al-nuzul as a chronology instrument.

Arm A (PRE-REGISTERED): the text's own retrospective marker (QAC LEM:<i*, the particle
'idh) against chronology, tested as STEP vs GRADIENT.

Arm B (DESCRIPTIVE, NOT pre-registered -- see prereg 6.2): al-Wahidi coverage.
Arm C (DESCRIPTIVE): the instrument audit of prereg section 1.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-3120-asbab-chronology.md
Seed 20260509, 10000 permutations, alpha = 0.025 (Bonferroni k=2).
"""

import hashlib
import json
import os
import csv
import sys
import datetime
import numpy as np
from scipy.stats import spearmanr

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-3120-asbab-chronology.md")
EXPECTED_PREREG_SHA = "bede8fc660467763a26e1068ec2d0a3dce044491c1da9c1f6718837210539caa"
QAC = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
CHRON = os.path.join(ROOT, "data/revelation-order.csv")
ASBAB = os.path.join(ROOT, "data/literature/classical-tafsir/spa5k-tafsir-api/en-asbab-al-nuzul-by-al-wahidi")

SEED = 20260509
NPERM = 10000
ALPHA = 0.025          # Bonferroni k = 2, prereg section 4
PHASE_ORD = {"Early Meccan": 0, "Middle Meccan": 1, "Late Meccan": 2, "Medinan": 3}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------- gate
actual = sha256(PREREG)
if actual != EXPECTED_PREREG_SHA:
    raise SystemExit(
        f"PREREG SHA MISMATCH\n  expected {EXPECTED_PREREG_SHA}\n  actual   {actual}\n"
        "The pre-registration has changed since this script was locked. Refusing to run."
    )
qac_sha = sha256(QAC)
if qac_sha != EXPECTED_QAC_SHA:
    raise SystemExit(f"QAC SHA MISMATCH\n  expected {EXPECTED_QAC_SHA}\n  actual {qac_sha}")


# ---------------------------------------------------------------- load
def load_corpus():
    q = json.load(open(QURAN, encoding="utf-8"))
    nv, wc, mvl = {}, {}, {}
    for s in q:
        sid = s["id"]
        words = sum(len(v["text"].split()) for v in s["verses"])
        nv[sid] = s["total_verses"]
        wc[sid] = words
        mvl[sid] = words / s["total_verses"]
    return nv, wc, mvl


def load_chronology():
    rows = list(csv.DictReader(open(CHRON, encoding="utf-8")))
    per = {}
    for r in rows:
        per[int(r["mushaf_order"])] = {
            "period": r["period"],                      # Egyptian-standard Meccan/Medinan
            "noldeke_phase": r["noldeke_phase"],
            "noldeke_order": int(r["noldeke_order"]),
            "egyptian_order": int(r["revelation_order"]),
        }
    return per


def load_idh():
    """QAC segments whose lemma is exactly <i* (the particle 'idh). Locked rule, prereg 2."""
    counts = {s: 0 for s in range(1, 115)}
    tokens = []
    with open(QAC, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
            lem = None
            for tok in feats.split("|"):
                if tok.startswith("LEM:"):
                    lem = tok[4:]
                    break
            if lem != "<i*":
                continue
            s, v = loc.strip("()").split(":")[:2]
            counts[int(s)] += 1
            tokens.append((int(s), int(v), form, tag))
    return counts, tokens


def load_asbab_coverage():
    """Arm B / Arm C descriptive. Returns per-surah non-empty entry count, and presence."""
    cov, present = {}, set()
    for fn in os.listdir(ASBAB):
        if not fn.endswith(".json"):
            continue
        s = int(fn[:-5])
        present.add(s)
        d = json.load(open(os.path.join(ASBAB, fn), encoding="utf-8"))
        cov[s] = len([a for a in (d.get("ayahs") or []) if (a.get("text") or "").strip()])
    return cov, present


# ---------------------------------------------------------------- strata
def make_strata(values, nbins):
    """Quantile bins. Returns integer stratum id per element."""
    v = np.asarray(values, dtype=float)
    qs = np.quantile(v, np.linspace(0, 1, nbins + 1))
    qs[0] -= 1e-9
    qs[-1] += 1e-9
    return np.clip(np.digitize(v, qs[1:-1], right=True), 0, nbins - 1)


def stratum_informativeness(strata, labels):
    """Fraction of strata containing >=2 distinct labels, and fraction of units in them."""
    info_units = 0
    info_strata = 0
    uniq = np.unique(strata)
    for st in uniq:
        m = strata == st
        if len(np.unique(np.asarray(labels)[m])) >= 2:
            info_strata += 1
            info_units += int(m.sum())
    return info_strata / len(uniq), info_units / len(strata)


def permute_within(labels, strata, rng):
    out = np.array(labels, copy=True)
    for st in np.unique(strata):
        idx = np.where(strata == st)[0]
        out[idx] = rng.permutation(out[idx])
    return out


# ---------------------------------------------------------------- statistics
def stat_step(density, binary):
    """mean(density | 1) - mean(density | 0). Locked positive = Medinan higher."""
    b = np.asarray(binary, dtype=bool)
    if b.all() or (~b).all():
        return np.nan
    return float(density[b].mean() - density[~b].mean())


def stat_rank(density, ordinal):
    r, _ = spearmanr(density, ordinal)
    return float(r)


def perm_test(density, labels, statfn, settings, rng_seed, nperm=NPERM):
    """One-sided (upper tail). Returns dict setting -> (obs, p, n_distinct_null, tie_at_obs)."""
    obs = statfn(density, labels)
    out = {}
    for name, strata in settings:
        rng = np.random.default_rng(rng_seed)
        nulls = np.empty(nperm)
        for i in range(nperm):
            nulls[i] = statfn(density, permute_within(labels, strata, rng))
        ge = int(np.sum(nulls >= obs))
        p = (1.0 + ge) / (1.0 + nperm)
        out[name] = {
            "obs": obs,
            "p": p,
            "n_distinct_null": int(len(np.unique(nulls))),
            "frac_null_eq_obs": float(np.mean(np.isclose(nulls, obs))),
            "null_mean": float(nulls.mean()),
            "null_sd": float(nulls.std(ddof=1)),
            "crit_value": float(np.quantile(nulls, 1 - ALPHA)),
        }
    return out


def worst(res):
    """Worst (largest) p across settings, and which setting produced it."""
    k = max(res, key=lambda x: res[x]["p"])
    return res[k]["p"], k


# ---------------------------------------------------------------- MDE
def compute_mde(density, binary, strata, rng_seed, crit, nperm=2000, nsim=300, nbisect=12):
    """
    Simulated MDE at 80% power for the STEP statistic, per prereg section 5 and h-new-3030 3.5.

    Synthetic datasets are generated under a known alternative: the observed densities are
    permuted (destroying any real association), then a shift delta is added to the label==1
    group. The permutation test is then run on each synthetic dataset and power is the fraction
    rejecting at ALPHA. Bisection on delta finds the smallest one reaching 80% power.

    The inner permutation test is vectorised: a within-stratum permutation matrix is built once
    and reused across simulations (documented approximation -- it correlates the null draws
    across simulations but not within any one test).

    UNTESTABLE-AT-THIS-N branch: if the maximum attainable value of the statistic under any
    relabelling is at or below the critical value, no effect of any size could have been
    detected, and the null is reported as untestable rather than as evidence of absence.
    """
    b = np.asarray(binary, dtype=bool)
    d = np.asarray(density, dtype=float)
    n = len(d)
    k = int(b.sum())
    if not (0 < k < n):
        return {"untestable": True, "s_max": None, "crit": crit, "mde": None}
    srt = np.sort(d)
    s_max = float(srt[::-1][:k].mean() - srt[: n - k].mean())
    if s_max <= crit:
        return {"untestable": True, "s_max": s_max, "crit": crit, "mde": None}

    rng = np.random.default_rng(rng_seed)
    # within-stratum permutation matrix of the LABEL vector, built once
    P = np.empty((nperm, n), dtype=bool)
    for i in range(nperm):
        P[i] = permute_within(b.astype(int), strata, rng).astype(bool)
    kk = P.sum(axis=1).astype(float)
    kk[kk == 0] = np.nan
    nk = (n - P.sum(axis=1)).astype(float)
    nk[nk == 0] = np.nan

    def power_at(delta):
        hits = 0
        for _ in range(nsim):
            ds = rng.permutation(d)
            ds = ds + delta * b            # known effect delta on the label==1 group
            obs = ds[b].mean() - ds[~b].mean()
            s1 = P @ ds
            nulls = s1 / kk - (ds.sum() - s1) / nk
            if obs > np.nanquantile(nulls, 1 - ALPHA):
                hits += 1
        return hits / nsim

    lo, hi = 0.0, max(s_max, crit * 4 if crit > 0 else 1.0)
    if power_at(hi) < 0.80:
        return {"untestable": False, "s_max": s_max, "crit": crit, "mde": None,
                "note": "80% power not reached at the maximum attainable shift"}
    for _ in range(nbisect):
        mid = (lo + hi) / 2
        if power_at(mid) >= 0.80:
            hi = mid
        else:
            lo = mid
    return {"untestable": False, "s_max": s_max, "crit": crit, "mde": float(hi),
            "power_at_mde": power_at(hi), "n_sim": nsim, "n_perm_inner": nperm}


# ---------------------------------------------------------------- main
def main():
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-3120", stamp)
    os.makedirs(run_dir, exist_ok=False)          # write-once, prereg / standing rule 3

    nv, wc, mvl = load_corpus()
    per = load_chronology()
    idh, idh_tokens = load_idh()
    cov, present = load_asbab_coverage()

    S = list(range(1, 115))
    density = np.array([idh[s] / nv[s] for s in S])

    # ---- length settings (prereg section 4). L0 unstratified + 3 vars x 2 granularities.
    zero = np.zeros(len(S), dtype=int)
    settings = [("L0 unstratified", zero)]
    for tag, vals in (("L1 verse count", [nv[s] for s in S]),
                      ("L2 word count", [wc[s] for s in S]),
                      ("L3 mean verse length", [mvl[s] for s in S])):
        for gname, nb in (("quintile", 5), ("decile", 10)):
            settings.append((f"{tag} {gname}", make_strata(vals, nb)))

    results = {"prereg_sha256": EXPECTED_PREREG_SHA, "qac_sha256": qac_sha,
               "seed": SEED, "n_perm": NPERM, "alpha": ALPHA, "utc": stamp}

    # ---- census
    results["census"] = {
        "idh_tokens_total": int(sum(idh.values())),
        "surahs_with_idh": int(sum(1 for s in S if idh[s] > 0)),
        "tie_fraction_density": float(
            (lambda u, c: (c[c > 1].sum() - len(c[c > 1])) / len(density))(
                *np.unique(density, return_counts=True))),
        "n_distinct_density": int(len(np.unique(density))),
    }

    # ---- tie-fraction gate (prereg section 4 / TIED-OUTCOME-DEFECT)
    results["exact_test_triggered"] = bool(results["census"]["tie_fraction_density"] > 0.50)

    # ---- R1 Nöldeke (PRIMARY)
    nold_bin = np.array([1 if per[s]["noldeke_phase"] == "Medinan" else 0 for s in S])
    nold_ord = np.array([PHASE_ORD[per[s]["noldeke_phase"]] for s in S])
    h1 = perm_test(density, nold_bin, stat_step, settings, SEED)
    h2 = perm_test(density, nold_ord, stat_rank, settings, SEED)
    results["R1_noldeke"] = {"H1_step": h1, "H2_gradient": h2}
    p1, w1 = worst(h1)
    p2, w2 = worst(h2)
    results["R1_noldeke"]["H1_worst"] = {"p": p1, "setting": w1, "obs": h1[w1]["obs"]}
    results["R1_noldeke"]["H2_worst"] = {"p": p2, "setting": w2, "obs": h2[w2]["obs"]}

    # ---- R2 Egyptian standard (ROBUSTNESS)
    egy_bin = np.array([1 if per[s]["period"] == "Medinan" else 0 for s in S])
    egy_rank = np.array([per[s]["egyptian_order"] for s in S])
    e1 = perm_test(density, egy_bin, stat_step, settings, SEED)
    e2 = perm_test(density, egy_rank, stat_rank, settings, SEED)
    pe1, we1 = worst(e1)
    pe2, we2 = worst(e2)
    results["R2_egyptian"] = {
        "H1_step": e1, "H2_gradient": e2,
        "H1_worst": {"p": pe1, "setting": we1, "obs": e1[we1]["obs"]},
        "H2_worst": {"p": pe2, "setting": we2, "obs": e2[we2]["obs"]},
        "binary_disagreements_with_noldeke": [s for s in S if nold_bin[S.index(s)] != egy_bin[S.index(s)]],
    }

    # ---- U1 token level (reported, NOT verdict-bearing; UNIT-DRIFT-DEFECT)
    tok_phase = [PHASE_ORD[per[s]["noldeke_phase"]] for (s, _v, _f, _t) in idh_tokens]
    verse_phase = []
    for s in S:
        verse_phase.extend([PHASE_ORD[per[s]["noldeke_phase"]]] * nv[s])
    results["U1_token_level"] = {
        "mean_phase_ordinal_of_idh_tokens": float(np.mean(tok_phase)),
        "mean_phase_ordinal_of_all_verses": float(np.mean(verse_phase)),
        "difference": float(np.mean(tok_phase) - np.mean(verse_phase)),
        "n_tokens": len(idh_tokens),
    }

    # ---- Meccan-internal contrast (S2), prereg section 3.1
    M = [s for s in S if per[s]["noldeke_phase"] != "Medinan"]
    mdens = np.array([idh[s] / nv[s] for s in M])
    m_ord = np.array([PHASE_ORD[per[s]["noldeke_phase"]] for s in M])
    m_bin = np.array([1 if per[s]["noldeke_phase"] == "Late Meccan" else 0 for s in M])
    mzero = np.zeros(len(M), dtype=int)
    msettings = [("L0 unstratified", mzero)]
    for tag, vals in (("L1 verse count", [nv[s] for s in M]),
                      ("L2 word count", [wc[s] for s in M]),
                      ("L3 mean verse length", [mvl[s] for s in M])):
        for gname, nb in (("quintile", 5), ("decile", 10)):
            msettings.append((f"{tag} {gname}", make_strata(vals, nb)))
    h1m = perm_test(mdens, m_bin, stat_step, msettings, SEED)
    h2m = perm_test(mdens, m_ord, stat_rank, msettings, SEED)
    pm1, wm1 = worst(h1m)
    pm2, wm2 = worst(h2m)
    results["meccan_internal"] = {
        "n_surahs": len(M),
        "H1m_step_late_vs_earlymid": h1m, "H2m_gradient": h2m,
        "H1m_worst": {"p": pm1, "setting": wm1, "obs": h1m[wm1]["obs"]},
        "H2m_worst": {"p": pm2, "setting": wm2, "obs": h2m[wm2]["obs"]},
    }

    # ---- stratum informativeness
    results["stratum_informativeness"] = {
        name: dict(zip(("frac_strata_informative", "frac_units_informative"),
                       stratum_informativeness(st, nold_bin)))
        for name, st in settings
    }

    # ---- phase profile (descriptive)
    prof = {}
    for ph in PHASE_ORD:
        ss = [s for s in S if per[s]["noldeke_phase"] == ph]
        prof[ph] = {
            "n_surahs": len(ss),
            "idh_tokens": int(sum(idh[s] for s in ss)),
            "verses": int(sum(nv[s] for s in ss)),
            "tokens_per_verse": float(sum(idh[s] for s in ss) / sum(nv[s] for s in ss)),
            "mean_surah_density": float(np.mean([idh[s] / nv[s] for s in ss])),
        }
    results["phase_profile"] = prof

    # =========================== VERDICT — transcribed from prereg section 5 ===========================
    #   PASS      := sign(H1) > 0 AND p_worst(H1) < 0.025 AND sign(H2) > 0 AND p_worst(H2) < 0.025
    #   PARTIAL   := exactly one of {H1, H2} satisfies its clause
    #   NULL      := neither satisfies its clause
    h1_ok = (h1[w1]["obs"] > 0) and (p1 < ALPHA)
    h2_ok = (h2[w2]["obs"] > 0) and (p2 < ALPHA)
    if h1_ok and h2_ok:
        verdict = "PASS"
    elif h1_ok or h2_ok:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"
    results["verdict"] = verdict
    results["verdict_inputs"] = {"H1_sign_ok": bool(h1[w1]["obs"] > 0), "H1_p_worst": p1,
                                 "H2_sign_ok": bool(h2[w2]["obs"] > 0), "H2_p_worst": p2}

    #   STEP-REPLICATED     := S1 AND S2
    #   GRADIENT-FOUND      := S2 fails
    #   SHAPE-INDETERMINATE := otherwise
    S1 = bool(p1 < p2)
    # prereg 3.1: S2 holds iff BOTH H1m and H2m FAIL to clear alpha. GRADIENT-FOUND requires the
    # Meccan-internal contrast to be "significant, correct sign" -- so a wrong-signed significant
    # result does NOT break S2. Sign is checked explicitly rather than relying on the one-sided
    # tail to imply it.
    h1m_live = bool((h1m[wm1]["obs"] > 0) and (pm1 < ALPHA))
    h2m_live = bool((h2m[wm2]["obs"] > 0) and (pm2 < ALPHA))
    S2 = bool(not (h1m_live or h2m_live))
    S3 = bool(max(pe1, pe2) > max(p1, p2))
    if S1 and S2:
        shape = "STEP-REPLICATED"
    elif not S2:
        shape = "GRADIENT-FOUND"
    else:
        shape = "SHAPE-INDETERMINATE"
    results["shape_verdict"] = shape
    results["shape_inputs"] = {"S1_binary_beats_rank": S1, "S2_meccan_internal_null": S2,
                               "S3_egyptian_weaker": S3}

    # ---- MDE, required when the verdict rests on an absence (prereg section 5)
    results["mde"] = {}
    if verdict != "PASS":
        results["mde"]["H1_full_corpus"] = compute_mde(
            density, nold_bin, dict(settings)[w1], SEED, h1[w1]["crit_value"])
    if S2:
        results["mde"]["H1m_meccan_internal"] = compute_mde(
            mdens, m_bin, dict(msettings)[wm1], SEED, h1m[wm1]["crit_value"])

    # ---- Arm B / C descriptive (NOT pre-registered, prereg 6.2)
    covrate114 = np.array([cov.get(s, 0) / nv[s] for s in S])
    S77 = list(range(1, 78))
    covrate77 = np.array([cov.get(s, 0) / nv[s] for s in S77])
    def desc(rate, idx):
        out = {}
        for k, v in (("verse count", [nv[s] for s in idx]),
                     ("word count", [wc[s] for s in idx]),
                     ("mean verse length", [mvl[s] for s in idx]),
                     ("noldeke phase ordinal", [PHASE_ORD[per[s]["noldeke_phase"]] for s in idx]),
                     ("egyptian rank", [per[s]["egyptian_order"] for s in idx]),
                     ("mushaf index", list(idx))):
            r, p = spearmanr(rate, v)
            out[k] = {"rho": float(r), "p": float(p)}
        u, c = np.unique(rate, return_counts=True)
        out["tie_fraction"] = float((c[c > 1].sum() - len(c[c > 1])) / len(rate))
        return out
    med_entries = sum(c for s, c in cov.items() if per[s]["period"] == "Medinan")
    all_entries = sum(cov.values())
    results["armBC_descriptive_NOT_preregistered"] = {
        "surahs_present": sorted(present),
        "surahs_absent": [s for s in S if s not in present],
        "n_absent": len(S) - len(present),
        "absent_phase_counts": {ph: sum(1 for s in S if s not in present
                                        and per[s]["noldeke_phase"] == ph) for ph in PHASE_ORD},
        "zero_entry_files_inside_block": [s for s in sorted(present) if cov.get(s, 0) == 0],
        "entries_total": all_entries,
        "medinan_entry_fraction": float(med_entries / all_entries),
        "corpus_medinan_verse_share": float(
            sum(nv[s] for s in S if per[s]["period"] == "Medinan") / sum(nv.values())),
        "channels_all114_absent_as_zero": desc(covrate114, S),
        "channels_window_1_77": desc(covrate77, S77),
    }

    with open(os.path.join(run_dir, "result.json"), "x", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    with open(os.path.join(run_dir, "manifest.txt"), "x", encoding="utf-8") as f:
        f.write(f"H-NEW-3120  {stamp}\n")
        f.write(f"prereg    {PREREG}\n  sha256 {EXPECTED_PREREG_SHA}\n")
        f.write(f"qac       {QAC}\n  sha256 {qac_sha}\n")
        f.write(f"quran     {QURAN}\n  sha256 {sha256(QURAN)}\n")
        f.write(f"chron     {CHRON}\n  sha256 {sha256(CHRON)}\n")
        f.write(f"script    {__file__}\n  sha256 {sha256(os.path.abspath(__file__))}\n")
        f.write(f"seed {SEED}  nperm {NPERM}  alpha {ALPHA}\n")
        f.write(f"VERDICT {verdict}   SHAPE {shape}\n")

    print(f"run_dir  {run_dir}")
    print(f"VERDICT  {verdict}")
    print(f"SHAPE    {shape}")
    print(f"  H1 obs {h1[w1]['obs']:+.6f}  p_worst {p1:.4f}  ({w1})")
    print(f"  H2 obs {h2[w2]['obs']:+.6f}  p_worst {p2:.4f}  ({w2})")
    print(f"  R2 H1 obs {e1[we1]['obs']:+.6f} p {pe1:.4f} | H2 obs {e2[we2]['obs']:+.6f} p {pe2:.4f}")
    print(f"  Meccan-internal H1m p {pm1:.4f} ({wm1}) | H2m p {pm2:.4f} ({wm2})")
    print(f"  S1 {S1}  S2 {S2}  S3 {S3}")
    print(f"  tie fraction {results['census']['tie_fraction_density']:.4f}  "
          f"exact triggered {results['exact_test_triggered']}")


if __name__ == "__main__":
    main()
